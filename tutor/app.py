"""
Certificaid Studietutor — Streamlit interface.

Gebruik:
  streamlit run tutor/app.py

ANTHROPIC_API_KEY wordt automatisch geladen uit .env in de project-root.
"""

import json
import os
import re
import sys
from pathlib import Path

# Laad .env vanuit project-root (vóór andere imports die de key nodig hebben)
_env_file = Path(__file__).parent.parent / ".env"
if _env_file.exists():
    for _line in _env_file.read_text().splitlines():
        _line = _line.strip()
        if _line and not _line.startswith("#") and "=" in _line:
            _k, _v = _line.split("=", 1)
            os.environ[_k.strip()] = _v.strip()

import anthropic
import streamlit as st  # noqa: E402 (streamlit voor sys.path-insert)

ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(ROOT / "tools"))

from lib.retrieval import (
    EMBEDDING_MODEL,
    build_retrieval_stack,
    open_collections,
    retrieve_and_rerank,
    RetrievalResult,
)

# CHROMA_PATH: leesbaar via env-var. Standaard = data/rag/main (unified index, ADR-006).
_chroma_env = os.environ.get("CERTIFICAID_CHROMA_PATH")
CHROMA_PATH   = Path(_chroma_env) if _chroma_env else ROOT / "data" / "rag" / "main"
PATTERNS_DIR  = ROOT / "data" / "programma" / "exam_patterns"
QUESTIONS_DIR = ROOT / "data" / "programma" / "gegenereerde_vragen"
CONCEPTEN_DIR = ROOT / "content" / "concepten"
CLAUDE_MODEL  = "claude-sonnet-4-6"

# ADR-006: twee collections
BRONNEN_COLS = ["bronnen"]
ALL_COLS     = ["bronnen", "concepten"]

# Bron-rollen voor filtering binnen de bronnen-collection (ADR-006 §3)
ALLE_BRON_ROLLEN = ["wettekst", "norm", "advies"]

# Rerank-instellingen per modus (ADR-005)
TUTOR_BI_TOP_N       = 30
TUTOR_RERANK_THRESH  = 0.60
TUTOR_MAX_RESULTS    = 10
CONCEPT_RERANK_THRESH = 0.65   # hogere drempel: concept-laag is al gecureerd

SYSTEM_PROMPT = """Je bent een studietutor voor het ITAA-bekwaamheidsexamen Gecertificeerd Accountant.

Jouw antwoorden volgen altijd de structuur: **Conclusie → Grondslag → Redenering**.

Regels:
- Elke feitelijke bewering krijgt een bronverwijzing (wet, artikel, CBN-advies, ITAA-norm).
- Claims die niet in de bronnen staan, label je expliciet als 🤖 (redenering/constructie).
- Gebruik ⚖️ voor wettelijk verankerde uitspraken, 🤖 voor analytische redenering.
- Exacte bedragen en tarieven hoef je niet uit het hoofd te kennen — verwijs naar ITAA-LEX of het Cijferzakboekje.
- Wees beknopt maar volledig. Geen onnodige uitweidingen.
- Schrijf in het Nederlands.

Stijl:
- Conclusie: één vetgedrukte zin met het antwoord.
- Grondslag: welke wet/artikel/norm is van toepassing?
- Redenering: waarom geldt deze conclusie in de gegeven situatie?
"""

EXPLAIN_SYSTEM_PROMPT = """Je bent een didactische studietutor voor het ITAA-bekwaamheidsexamen Gecertificeerd Accountant.

Je legt een concept stap voor stap uit aan een stagiair GA/GBA met boekhoudkundige en fiscale basiskennis — geen jurist. Doel: het concept écht laten begrijpen, niet alleen feiten opsommen.

Structuur:
1. **Kern in één zin** — wat is het, in gewone taal.
2. **Waarom bestaat dit?** — welk probleem lost de regel op? (intuïtie boven jargon)
3. **Bouwstenen** — de onderliggende voorwaarden of elementen, één per één.
4. **Hoe herken je het in een casus** — concrete signalen, met een mini-voorbeeld.
5. **Veelgemaakte fouten / valkuilen** — wat verwart studenten meestal? Welke uitzonderingen worden gemist?
6. **Checkvraag** — één korte vraag die de gebruiker uitnodigt om het concept toe te passen (geen antwoord geven).

Regels:
- Elke feitelijke claim krijgt een bronverwijzing (wet/artikel, CBN-advies, ITAA-norm) met ⚖️.
- Eigen redenering / didactische illustraties: label met 🤖.
- Gebruik de aangeleverde concept-fiche als ruggengraat — het meeste staat daar al klaar.
- Schrijf in het Nederlands. Korte zinnen. Geen jargon zonder uitleg.
- Eindig altijd met de checkvraag — niet met een samenvatting.
"""


# ---------------------------------------------------------------------------
# RAG setup (gecached)
# ---------------------------------------------------------------------------

def _tutor_device() -> str:
    """
    Kies het beste device voor query-time retrieval in de tutor.

    MPS is hier wél gewenst — de tutor IS de primaire taak, niet een achtergrond-
    build-stap. Gebruik MPS als het beschikbaar is voor ~1.7× snellere embedding +
    reranking. Fallback naar CPU als torch/MPS niet beschikbaar is.
    """
    try:
        import torch
        if torch.backends.mps.is_available():
            return "mps"
    except Exception:
        pass
    return "cpu"


@st.cache_resource
def load_rag():
    """
    Laad ChromaDB, embedding-functie en reranker (één keer per Streamlit-sessie).

    Bi-encoder op MPS (query-embedding is klein, ~50ms sneller dan CPU).
    Reranker altijd op CPU: de forward-pass over 30 paren verbruikt te veel actief
    MPS-geheugen op een Mac waar Claude Desktop ook MPS-geheugen bezet.
    """
    device = _tutor_device()
    client, ef, reranker = build_retrieval_stack(
        CHROMA_PATH, device=device, reranker_device="cpu"
    )
    collections = open_collections(client, ef, ALL_COLS)
    return client, ef, reranker, collections, device


@st.cache_data(ttl=300)
def _bron_rol_counts(chroma_path_str: str) -> dict:
    """Tel chunks per bron_rol — gecached 5 minuten zodat dit niet bij elke rerun draait."""
    import chromadb as _chromadb
    _client = _chromadb.PersistentClient(path=chroma_path_str)
    try:
        _col = _client.get_collection("bronnen")
        counts = {}
        for rol in ALLE_BRON_ROLLEN:
            try:
                res = _col.get(where={"bron_rol": {"$eq": rol}}, include=[])
                counts[rol] = len(res["ids"])
            except Exception:
                counts[rol] = 0
        counts["_totaal"] = _col.count()
        return counts
    except Exception:
        return {}


def retrieve_two_pass(
    collections: dict,
    reranker,           # CrossEncoder | None — None = sla reranking over
    query: str,
    po_filter: str | None = None,
    bron_rollen: list[str] | None = None,
) -> tuple[list[RetrievalResult], str]:
    """
    Twee-pass retrieval (ADR-006):

    Pass 1: zoek in concepten-collection (gecureerde kennislaag).
            Resultaten met rerank_score ≥ CONCEPT_RERANK_THRESH als primaire context.

    Pass 2: zoek altijd in bronnen-collection (unified, optioneel gefilterd op bron_rol).
            Resultaten van beide passes worden samengevoegd.

    po_filter: als opgegeven, wordt het als prefix aan de query toegevoegd (zachte sturing;
               er is geen programmaonderdeel-metadata in de huidige bronnen-collection).

    Retourneert (chunks, retrieval_mode).
    """
    expanded_query = f"PO {po_filter} {query}" if po_filter else query

    # Pass 1: concepten-laag
    concept_results: list[RetrievalResult] = []
    if "concepten" in collections:
        concept_results = retrieve_and_rerank(
            expanded_query,
            collections,
            ["concepten"],
            reranker,
            bi_top_n=15,
            rerank_threshold=CONCEPT_RERANK_THRESH,
            max_results=3,
            expand_context=False,
        )

    # Pass 2: bronnen-laag (unified collection met optionele bron_rol-filter)
    bronnen_results = retrieve_and_rerank(
        expanded_query,
        collections,
        BRONNEN_COLS,
        reranker,
        bi_top_n=TUTOR_BI_TOP_N,
        rerank_threshold=TUTOR_RERANK_THRESH,
        max_results=TUTOR_MAX_RESULTS,
        expand_context=True,
        bron_rollen=bron_rollen,
    )

    all_results = concept_results + bronnen_results
    mode = "concept+bronnen" if concept_results else "bronnen"
    return all_results, mode


def format_context(chunks: list[RetrievalResult], max_chars: int = 7000) -> str:
    parts = []
    total = 0
    for i, chunk in enumerate(chunks, 1):
        ref = chunk.label()
        score = chunk.rerank_score if chunk.rerank_score >= 0 else chunk.score
        text = chunk.text[:1200]
        part = f"[Bron {i}: {ref} | score: {score:.3f}]\n{text}"
        if total + len(part) > max_chars:
            break
        parts.append(part)
        total += len(part)
    return "\n\n---\n\n".join(parts)


def format_sources_display(chunks: list[RetrievalResult]) -> str:
    """Formatteer bronvermeldingen voor display onder het antwoord."""
    seen = set()
    refs = []
    for chunk in chunks[:8]:
        ref = chunk.label()
        if ref not in seen:
            seen.add(ref)
            score = chunk.rerank_score if chunk.rerank_score >= 0 else chunk.score
            tag = " [concept]" if chunk.collection == "concepten" else ""
            refs.append(f"- {ref}{tag} (relevantie: {int(score * 100)}%)")
    return "\n".join(refs) if refs else "Geen specifieke bronnen"


# ---------------------------------------------------------------------------
# Claude API
# ---------------------------------------------------------------------------

@st.cache_resource
def get_claude():
    # Lokaal: uit .env / os.environ. Streamlit Cloud: uit st.secrets.
    api_key = os.environ.get("ANTHROPIC_API_KEY") or st.secrets.get("ANTHROPIC_API_KEY")
    if not api_key:
        st.error("❌ ANTHROPIC_API_KEY niet ingesteld (env-var of st.secrets).")
        st.stop()
    return anthropic.Anthropic(api_key=api_key)


def ask_claude_stream(client: anthropic.Anthropic, question: str, context: str,
                      history: list[dict], system_prompt: str = SYSTEM_PROMPT,
                      max_tokens: int = 2048):
    """
    Generator die Claude's antwoord token voor token streamt.
    Gebruik met st.write_stream() voor directe weergave terwijl Claude nog schrijft.
    """
    messages = []
    # Voeg gespreksgeschiedenis toe (max 6 beurten)
    for turn in history[-6:]:
        messages.append({"role": turn["role"], "content": turn["content"]})

    user_content = f"""Vraag: {question}

---
Aangeleverde bronnen (gebruik deze als primaire referentie):

{context}
---"""
    messages.append({"role": "user", "content": user_content})

    with client.messages.stream(
        model=CLAUDE_MODEL,
        max_tokens=max_tokens,
        system=system_prompt,
        messages=messages,
    ) as stream:
        yield from stream.text_stream


# ---------------------------------------------------------------------------
# Patroonbibliotheek laden — nieuw schema (vraagvormen + complexiteitspatronen)
# ---------------------------------------------------------------------------

@st.cache_data(ttl=300)
def load_vraagvormen() -> list[dict]:
    """Laad data/programma/exam_patterns/vraagvormen.json (10 vraagvormen)."""
    f = PATTERNS_DIR / "vraagvormen.json"
    if not f.exists():
        return []
    try:
        return json.loads(f.read_text()).get("vraagvormen", [])
    except Exception:
        return []


@st.cache_data(ttl=300)
def load_complexiteitspatronen() -> list[dict]:
    """Laad data/programma/exam_patterns/complexiteitspatronen.json (15 patronen)."""
    f = PATTERNS_DIR / "complexiteitspatronen.json"
    if not f.exists():
        return []
    try:
        return json.loads(f.read_text()).get("complexiteitspatronen", [])
    except Exception:
        return []


def _format_vraagvormen_for_prompt(vraagvormen: list[dict]) -> str:
    """Compacte tekstuele lijst voor in de prompt."""
    lines = []
    for v in vraagvormen:
        lines.append(
            f"- `{v['id']}` — {v['naam']} ({v.get('cognitieve_laag', '?')})\n"
            f"  Format: {v.get('format', '')[:160]}"
        )
    return "\n".join(lines)


def _format_complexiteit_for_prompt(patronen: list[dict]) -> str:
    """Compacte tekstuele lijst voor in de prompt."""
    lines = []
    for p in patronen:
        lines.append(
            f"- `{p['id']}` — {p['naam']} "
            f"(kennisdiepte={p.get('kennisdiepte','?')}, camouflage={p.get('camouflage','?')})\n"
            f"  {p.get('beschrijving', '')[:180]}"
        )
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Case generator — auto-patroon (Claude kiest vraagvorm + complexiteit)
# ---------------------------------------------------------------------------

def generate_case(client: anthropic.Anthropic, concept: str, po_filter: str,
                  collections: dict, active_reranker,
                  vraagvormen: list[dict], complexiteitspatronen: list[dict],
                  ) -> tuple[str, str, dict]:
    """
    Genereer een realistische examenvraag.

    Claude kiest zelf:
      - één `vraagvorm` (formaat: MC, J/F, open, berekening, ...)
      - één `complexiteitspatroon` (kennisdiepte + camouflage)

    Retourneert (volledige_tekst, gvraag_id, gekozen_patroon_dict).
    """
    chunks, _ = retrieve_two_pass(collections, active_reranker, concept)
    context = format_context(chunks, max_chars=3500)

    vraagvormen_blok = _format_vraagvormen_for_prompt(vraagvormen)
    complex_blok = _format_complexiteit_for_prompt(complexiteitspatronen)

    po_hint = f" (programmaonderdeel {po_filter})" if po_filter and po_filter != "Alle PO's" else ""

    prompt = f"""Genereer één realistische examenvraag voor het ITAA-bekwaamheidsexamen over:
**{concept}**{po_hint}

Beschikbare **vraagvormen** (kies precies één — gebruik exact het `id`):
{vraagvormen_blok}

Beschikbare **complexiteitspatronen** (kies precies één — gebruik exact het `id`):
{complex_blok}

Stappen:
1. Kies de meest passende vraagvorm + complexiteitspatroon voor dit concept.
2. Bouw de vraag volgens dat vraagvorm-formaat en met de gekozen camouflage/diepte.
3. Schrijf in het Nederlands. Gebruik de bronnen voor feitelijke correctheid.

Antwoord exact in dit formaat (verplicht, geen extra inleiding):

**Vraagvorm**: <vraagvorm-id>
**Complexiteit**: <complexiteitspatroon-id>
**Motivering keuze**: <1-2 zinnen waarom deze combinatie past>

**Situatie**: <concrete casus, 2-4 zinnen — of leeg bij abstracte feitenvraag>
**Vraag**: <de eigenlijke examenvraag>
**Antwoord**: <volledig antwoord: conclusie → grondslag (wet/norm/advies) → redenering>

Bronnen:
{context}"""

    response = client.messages.create(
        model=CLAUDE_MODEL,
        max_tokens=2000,
        messages=[{"role": "user", "content": prompt}],
    )
    generated_text = response.content[0].text

    gekozen = _extract_chosen_patterns(generated_text, vraagvormen, complexiteitspatronen)
    gvraag_id = _save_generated_question(concept, po_filter, gekozen, generated_text)
    return generated_text, gvraag_id, gekozen


def _extract_chosen_patterns(text: str, vraagvormen: list[dict],
                              complexiteitspatronen: list[dict]) -> dict:
    """Haal de door Claude gekozen vraagvorm + complexiteitspatroon uit de output."""
    vv_match = re.search(r"\*\*Vraagvorm\*\*:\s*`?([\w-]+)`?", text)
    cx_match = re.search(r"\*\*Complexiteit\*\*:\s*`?([\w-]+)`?", text)
    vv_id = vv_match.group(1) if vv_match else None
    cx_id = cx_match.group(1) if cx_match else None
    return {
        "vraagvorm_id": vv_id,
        "vraagvorm": next((v for v in vraagvormen if v["id"] == vv_id), None),
        "complexiteit_id": cx_id,
        "complexiteit": next((p for p in complexiteitspatronen if p["id"] == cx_id), None),
    }


def _save_generated_question(concept: str, po_filter: str, gekozen: dict,
                               generated_text: str) -> str:
    """Sla de gegenereerde vraag op als JSON."""
    from datetime import date as _date

    QUESTIONS_DIR.mkdir(parents=True, exist_ok=True)

    slug = re.sub(r"[^a-z0-9]", "-", concept.lower())[:40].strip("-")
    existing = list(QUESTIONS_DIR.glob(f"gvraag-{slug}-*.json"))
    idx = len(existing) + 1
    gvraag_id = f"gvraag:{slug}-{idx:03d}"
    filename = f"gvraag-{slug}-{idx:03d}.json"

    vraag_match = re.search(r"\*\*Vraag\*\*:(.*?)(?=\*\*Antwoord\*\*|$)", generated_text, re.DOTALL)
    antwoord_match = re.search(r"\*\*Antwoord\*\*:(.*)", generated_text, re.DOTALL)
    situatie_match = re.search(r"\*\*Situatie\*\*:(.*?)(?=\*\*Vraag\*\*|$)", generated_text, re.DOTALL)

    vraagvorm = gekozen.get("vraagvorm") or {}

    record = {
        "id": gvraag_id,
        "concept_id": f"concept:{slug}",
        "po": po_filter if po_filter != "Alle PO's" else None,
        "vraagvorm_id": gekozen.get("vraagvorm_id"),
        "complexiteit_id": gekozen.get("complexiteit_id"),
        "cognitieve_laag": vraagvorm.get("cognitieve_laag"),
        "situatie": situatie_match.group(1).strip() if situatie_match else None,
        "vraag": vraag_match.group(1).strip() if vraag_match else generated_text,
        "antwoord": antwoord_match.group(1).strip() if antwoord_match else "",
        "gegenereerd_op": _date.today().isoformat(),
        "gegenereerd_door": CLAUDE_MODEL,
        "status": "actief",
    }

    (QUESTIONS_DIR / filename).write_text(
        json.dumps(record, ensure_ascii=False, indent=2)
    )
    return gvraag_id


# ---------------------------------------------------------------------------
# Concept-fiches uit content/concepten/ (Leg me uit-modus)
# ---------------------------------------------------------------------------

@st.cache_data(ttl=300)
def load_concept_fiches_index() -> list[dict]:
    """
    Scan content/concepten/*.md en geef een index met {slug, title, path, tags, pos}.
    Frontmatter wordt minimaal geparsed (geen externe afhankelijkheid).
    """
    fiches = []
    if not CONCEPTEN_DIR.exists():
        return fiches
    for f in sorted(CONCEPTEN_DIR.glob("*.md")):
        meta, _ = _parse_fiche(f)
        fiches.append({
            "slug": f.stem,
            "title": meta.get("title", f.stem),
            "path": f,
            "tags": meta.get("tags", []),
            "programmaonderdelen": meta.get("programmaonderdelen", []),
            "node_type": meta.get("node_type", ""),
        })
    return fiches


def _parse_fiche(path: Path) -> tuple[dict, str]:
    """Parse YAML-frontmatter + body uit een markdown-fiche. Geen yaml-dep nodig."""
    text = path.read_text()
    if not text.startswith("---\n"):
        return {}, text
    end = text.find("\n---\n", 4)
    if end == -1:
        return {}, text
    fm_raw = text[4:end]
    body = text[end + 5:]

    meta: dict = {}
    current_list_key: str | None = None
    for line in fm_raw.splitlines():
        if not line.strip():
            current_list_key = None
            continue
        if line.startswith("- ") and current_list_key:
            val = line[2:].strip().strip("'\"")
            meta[current_list_key].append(val)
        elif ":" in line and not line.startswith(" "):
            key, _, val = line.partition(":")
            key = key.strip()
            val = val.strip()
            if val == "":
                meta[key] = []
                current_list_key = key
            else:
                meta[key] = val.strip("'\"")
                current_list_key = None
    return meta, body


def find_relevant_fiches(query: str, fiches: list[dict], max_n: int = 3) -> list[dict]:
    """
    Eenvoudige slug/title-match. Geen embedding nodig — slug-overlap volstaat naast de RAG-pass.
    """
    q = query.lower()
    q_tokens = [t for t in re.split(r"[^a-zà-ÿ0-9]+", q) if len(t) >= 4]
    scored = []
    for fi in fiches:
        slug = fi["slug"].lower()
        title = fi["title"].lower()
        score = 0
        if q in slug or slug in q:
            score += 5
        if q in title or title in q:
            score += 4
        for tok in q_tokens:
            if tok in slug:
                score += 2
            if tok in title:
                score += 1
        if score > 0:
            scored.append((score, fi))
    scored.sort(key=lambda x: x[0], reverse=True)
    return [fi for _, fi in scored[:max_n]]


def format_fiche_context(fiches_paths: list[Path], max_chars: int = 6000) -> str:
    """Lees fiches en concateneer body's met een korte header per fiche."""
    parts = []
    total = 0
    for p in fiches_paths:
        meta, body = _parse_fiche(p)
        title = meta.get("title", p.stem)
        block = f"### Concept-fiche: {title} (`{p.stem}`)\n\n{body.strip()}"
        if total + len(block) > max_chars:
            block = block[: max_chars - total]
        parts.append(block)
        total += len(block)
        if total >= max_chars:
            break
    return "\n\n---\n\n".join(parts)


# ---------------------------------------------------------------------------
# Streamlit UI
# ---------------------------------------------------------------------------

def main():
    st.set_page_config(
        page_title="Certificaid Tutor",
        page_icon="📚",
        layout="wide",
    )

    st.title("📚 Certificaid Studietutor")
    st.caption("ITAA-bekwaamheidsexamen — Gecertificeerd Accountant")

    # Laad resources
    _, ef, reranker, collections, rag_device = load_rag()
    claude = get_claude()

    active_cols = [n for n in ALL_COLS if n in collections]
    if not active_cols:
        st.error("❌ Geen RAG-collections gevonden. Run eerst `python tools/rag/rag_index.py`.")
        st.stop()

    # --- Sidebar ---
    with st.sidebar:
        st.header("Instellingen")

        po_filter = st.selectbox(
            "Programmaonderdeel",
            ["Alle PO's", "1.1", "1.2", "1.3", "1.4", "1.5",
             "2.1", "2.2", "2.3", "2.4", "2.5", "2.6", "2.7", "2.8",
             "3.1", "3.2", "4.0"],
            index=0,
            help="Stuurt de zoekopdracht zachter in de richting van dit programmaonderdeel. "
                 "Geen harde filter — bronnen zijn niet per PO gepartitioneerd.",
        )

        modus = st.radio(
            "Modus",
            ["Vraag & Antwoord", "Leg me uit", "Examenvraag genereren", "Concept opzoeken"],
        )

        st.divider()
        st.caption("Bron-types")
        bron_rol_selectie = {
            rol: st.checkbox(rol, value=True)
            for rol in ALLE_BRON_ROLLEN
        }
        actieve_bron_rollen = [r for r, aan in bron_rol_selectie.items() if aan] or None

        gebruik_reranker = st.checkbox(
            "Reranker",
            value=False,
            help="Cross-encoder rerankt de kandidaten nauwkeuriger, maar voegt 1–3 s "
                 "latency toe. Met 400 chunks en bge-m3 is de bi-encoder alleen al goed.",
        )

        st.divider()
        # Toon tellingen per bron_rol — gecached zodat dit niet bij elke rerun draait.
        if "bronnen" in collections:
            counts = _bron_rol_counts(str(CHROMA_PATH))
            totaal_concepten = collections["concepten"].count() if "concepten" in collections else 0
            st.caption(
                f"**Index:** `{CHROMA_PATH.name}`  \n"
                f"**Device:** embed=`{rag_device}` · rerank=`cpu`  \n"
                + "  \n".join(
                    f"· {rol}: {counts.get(rol, 0):,}" for rol in ALLE_BRON_ROLLEN
                )
                + f"  \n· concepten: {totaal_concepten:,}"
                + f"  \n**Totaal:** {counts.get('_totaal', 0) + totaal_concepten:,}"
            )
        else:
            total_docs = sum(collections[n].count() for n in active_cols if n in collections)
            st.caption(f"Collections: {', '.join(active_cols)}")
            st.caption(f"Geïndexeerde chunks: {total_docs:,}")

        if st.button("🗑️ Gesprek wissen"):
            st.session_state.messages = []
            st.rerun()

    # --- Hoofdscherm ---
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Toon gespreksgeschiedenis
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])
            if msg.get("sources"):
                with st.expander("📎 Gebruikte bronnen"):
                    st.text(msg["sources"])

    # --- Modus: Vraag & Antwoord ---
    if modus == "Vraag & Antwoord":
        if prompt := st.chat_input("Stel een vraag over de examenstof..."):
            # Toon gebruikersvraag
            with st.chat_message("user"):
                st.markdown(prompt)
            st.session_state.messages.append({"role": "user", "content": prompt})

            # RAG retrieval — po_filter-prefix wordt intern door retrieve_two_pass toegevoegd.
            active_reranker = reranker if gebruik_reranker else None
            with st.spinner("Bronnen zoeken..."):
                chunks, _mode = retrieve_two_pass(
                    collections, active_reranker, prompt,
                    po_filter=po_filter if po_filter != "Alle PO's" else None,
                    bron_rollen=actieve_bron_rollen,
                )

            context = format_context(chunks)
            sources_display = format_sources_display(chunks)

            # Claude antwoord — gestreamd zodat tekst direct zichtbaar is
            with st.chat_message("assistant"):
                history = [m for m in st.session_state.messages[:-1]]
                answer = st.write_stream(
                    ask_claude_stream(claude, prompt, context, history)
                )
                with st.expander("📎 Gebruikte bronnen"):
                    st.text(sources_display)

            st.session_state.messages.append({
                "role": "assistant",
                "content": answer,
                "sources": sources_display,
            })

    # --- Modus: Leg me uit ---
    elif modus == "Leg me uit":
        st.subheader("🪄 Leg me uit")
        st.caption(
            "Vrije tekst → de tutor zoekt relevante concept-fiches en bronnen, en geeft "
            "een stap-voor-stap didactische uitleg met checkvraag."
        )

        if uitleg_prompt := st.chat_input("Welk concept of welke regel moet ik uitleggen?"):
            with st.chat_message("user"):
                st.markdown(uitleg_prompt)
            st.session_state.messages.append({"role": "user", "content": uitleg_prompt})

            active_reranker = reranker if gebruik_reranker else None

            with st.spinner("Concepten en bronnen zoeken..."):
                # 1. RAG-pass (concept-collectie + bronnen)
                chunks, _mode = retrieve_two_pass(
                    collections, active_reranker, uitleg_prompt,
                    po_filter=po_filter if po_filter != "Alle PO's" else None,
                    bron_rollen=actieve_bron_rollen,
                )
                # 2. Slug/title-match op de 30 concept-fiches in content/concepten/
                fiches_index = load_concept_fiches_index()
                matched_fiches = find_relevant_fiches(uitleg_prompt, fiches_index, max_n=2)

            bronnen_context = format_context(chunks, max_chars=5000)
            fiche_context = format_fiche_context([f["path"] for f in matched_fiches])

            combined_context_parts = []
            if fiche_context:
                combined_context_parts.append(
                    "## Beschikbare concept-fiches (primaire ruggengraat)\n\n" + fiche_context
                )
            if bronnen_context:
                combined_context_parts.append(
                    "## Aanvullende bronnen (wet/norm/advies)\n\n" + bronnen_context
                )
            full_context = "\n\n=====\n\n".join(combined_context_parts) or "(geen)"

            sources_display = format_sources_display(chunks)
            if matched_fiches:
                sources_display = (
                    "**Concept-fiches:**\n"
                    + "\n".join(f"- 📘 {fi['title']} (`{fi['slug']}`)" for fi in matched_fiches)
                    + "\n\n**Bronnen:**\n"
                    + sources_display
                )

            with st.chat_message("assistant"):
                history = [m for m in st.session_state.messages[:-1]]
                answer = st.write_stream(
                    ask_claude_stream(
                        claude, uitleg_prompt, full_context, history,
                        system_prompt=EXPLAIN_SYSTEM_PROMPT,
                        max_tokens=2500,
                    )
                )
                with st.expander("📎 Gebruikte bronnen"):
                    st.markdown(sources_display)

            st.session_state.messages.append({
                "role": "assistant",
                "content": answer,
                "sources": sources_display,
            })

    # --- Modus: Examenvraag genereren ---
    elif modus == "Examenvraag genereren":
        st.subheader("Examenvraag genereren")
        st.caption(
            "Claude kiest zelf een passende vraagvorm (10) en complexiteitspatroon (15) "
            "op basis van het concept en de bronnen."
        )

        vraagvormen = load_vraagvormen()
        complexiteitspatronen = load_complexiteitspatronen()

        if not vraagvormen or not complexiteitspatronen:
            st.warning(
                "⚠️ `data/programma/exam_patterns/vraagvormen.json` of "
                "`complexiteitspatronen.json` ontbreekt."
            )

        concept_input = st.text_input(
            "Concept of onderwerp",
            placeholder="bv. 'consolidatiekring' of 'btw-vrijstelling kleine onderneming'",
        )

        if st.button("Genereer oefenvraag",
                     disabled=not concept_input or not vraagvormen or not complexiteitspatronen):
            with st.spinner("Vraag genereren..."):
                case_text, gvraag_id, gekozen = generate_case(
                    claude, concept_input, po_filter, collections,
                    reranker if gebruik_reranker else None,
                    vraagvormen, complexiteitspatronen,
                )

            st.markdown("---")
            vv = gekozen.get("vraagvorm")
            cx = gekozen.get("complexiteit")
            if vv or cx:
                bits = []
                if vv:
                    bits.append(f"Vraagvorm: **{vv['naam']}**")
                if cx:
                    bits.append(f"Complexiteit: **{cx['naam']}**")
                st.caption(" · ".join(bits) + f" · `{gvraag_id}`")

            # Toon meta + situatie + vraag (niet het antwoord)
            antwoord_pos = case_text.find("**Antwoord**")
            vraag_deel = case_text[:antwoord_pos].strip() if antwoord_pos > 0 else case_text
            st.markdown(vraag_deel)

            with st.expander("💡 Toon antwoord"):
                if antwoord_pos > 0:
                    st.markdown(case_text[antwoord_pos:].replace("**Antwoord**:", "").strip())
                else:
                    st.markdown("_Antwoord niet gevonden in gegenereerde tekst._")

    # --- Modus: Concept opzoeken ---
    elif modus == "Concept opzoeken":
        st.subheader("Concept opzoeken")

        concept_search = st.text_input(
            "Conceptnaam of trefwoord",
            placeholder="bv. 'continuiteitsrisico'",
        )

        if concept_search:
            with st.spinner("Zoeken..."):
                chunks, mode = retrieve_two_pass(
                    collections, reranker if gebruik_reranker else None, concept_search,
                    bron_rollen=actieve_bron_rollen,
                )

            st.markdown(f"**Top resultaten voor:** _{concept_search}_ _(mode: {mode})_")
            for i, chunk in enumerate(chunks[:8], 1):
                score = chunk.rerank_score if chunk.rerank_score >= 0 else chunk.score
                tag = " 🗂️" if chunk.collection == "concepten" else ""
                with st.expander(f"[{i}] {chunk.label()}{tag} ({int(score*100)}% relevant)"):
                    st.text(chunk.text[:800])


if __name__ == "__main__":
    main()
