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
import chromadb
import streamlit as st

ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(ROOT / "tools"))

from lib.retrieval import (
    EMBEDDING_MODEL,
    build_retrieval_stack,
    open_collections,
    retrieve_and_rerank,
    RetrievalResult,
)

CHROMA_PATH   = ROOT / "data" / "chroma_db"
PATTERNS_DIR  = ROOT / "data" / "exam_patterns"
QUESTIONS_DIR = ROOT / "data" / "generated_questions"
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


# ---------------------------------------------------------------------------
# RAG setup (gecached)
# ---------------------------------------------------------------------------

@st.cache_resource
def load_rag():
    """Laad ChromaDB, embedding-functie en reranker (één keer per Streamlit-sessie)."""
    client, ef, reranker = build_retrieval_stack(CHROMA_PATH)
    collections = open_collections(client, ef, ALL_COLS)
    return client, ef, reranker, collections


def retrieve_two_pass(
    collections: dict,
    reranker,
    query: str,
    selected_cols: list[str],
    po_filter: str | None = None,
    bron_rollen: list[str] | None = None,
) -> tuple[list[RetrievalResult], str]:
    """
    Twee-pass retrieval (ADR-006):

    Pass 1: zoek in concepten-collection (gecureerde kennislaag).
            Als score ≥ CONCEPT_RERANK_THRESH → gebruik als primaire context.

    Pass 2: zoek altijd in bronnen-collection (unified, optioneel gefilterd op bron_rol).
            Resultaten gecombineerd met Pass 1.

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
    api_key = os.environ.get("ANTHROPIC_API_KEY")
    if not api_key:
        st.error("❌ ANTHROPIC_API_KEY niet ingesteld.")
        st.stop()
    return anthropic.Anthropic(api_key=api_key)


def ask_claude(client: anthropic.Anthropic, question: str, context: str,
               history: list[dict]) -> str:
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

    response = client.messages.create(
        model=CLAUDE_MODEL,
        max_tokens=2048,
        system=SYSTEM_PROMPT,
        messages=messages,
    )
    return response.content[0].text


# ---------------------------------------------------------------------------
# Patroonbibliotheek laden
# ---------------------------------------------------------------------------

@st.cache_data(ttl=300)
def load_patterns() -> list[dict]:
    """Laad alle examenpatronen uit data/exam_patterns/."""
    patterns = []
    if PATTERNS_DIR.exists():
        for f in sorted(PATTERNS_DIR.glob("*.json")):
            try:
                patterns.append(json.loads(f.read_text()))
            except Exception:
                pass
    return patterns


def select_patterns_for_concept(patterns: list[dict], concept: str,
                                 po_filter: str) -> list[dict]:
    """Kies de meest relevante patronen voor een concept en PO."""
    if not patterns:
        return []

    concept_lower = concept.lower()
    relevant = []
    for p in patterns:
        score = 0
        # Match op thema's
        for thema in p.get("typische_themas", []):
            if thema.lower() in concept_lower or concept_lower in thema.lower():
                score += 2
        # Match op PO
        if po_filter and po_filter != "Alle PO's":
            if po_filter in p.get("pos_geobserveerd", []):
                score += 1
        # Alle patronen zijn relevant als fallback
        relevant.append((score, p))

    relevant.sort(key=lambda x: x[0], reverse=True)
    # Geef top-3 terug, maar minstens 1 van elk cognitief niveau indien beschikbaar
    selected = [p for _, p in relevant[:3]]
    return selected


# ---------------------------------------------------------------------------
# Case generator (patroonbewust)
# ---------------------------------------------------------------------------

def generate_case(client: anthropic.Anthropic, concept: str, po_filter: str,
                  collections: dict, reranker,
                  patroon: dict | None = None) -> tuple[str, str]:
    """
    Genereer een examenvraag. Geeft (vraag_tekst, gvraag_id) terug.
    Als patroon opgegeven: gebruik dat patroon als template.
    """
    chunks, _ = retrieve_two_pass(collections, reranker, concept, ALL_COLS)
    context = format_context(chunks, max_chars=3000)

    if patroon:
        patroon_instructie = f"""
Gebruik het volgende **examenpatroon** als template voor de vraagstelling:

Patroon: **{patroon['naam']}**
Beschrijving: {patroon['beschrijving']}
Vraagtype: {', '.join(patroon.get('vraagtypen', []))}
Cognitieve laag: {patroon.get('cognitieve_laag', '')}
Typische formulering: {'; '.join(patroon.get('typische_formulering', [])[:2])}
Valkuil die het patroon uitlokt: {patroon.get('valkuil', '')}

De vraag moet dit patroon volgen — niet alleen het onderwerp behandelen, maar ook de manier van vragen nabootsen.
"""
    else:
        patroon_instructie = "Kies zelf een passend vraagtype (J/F, MC, open, berekening) op integratieniveau."

    prompt = f"""Genereer een realistische examenvraag voor het ITAA-bekwaamheidsexamen over: **{concept}**

{patroon_instructie}

Gebruik de aangeleverde bronnen voor feitelijke correctheid.
Schrijf in het Nederlands.

Formaat (verplicht):
**Situatie**: [concrete casus of context, 2-4 zinnen]
**Vraag**: [de eigenlijke examenvraaag]
**Antwoord**: [volledig antwoord: conclusie → grondslag → redenering]

Bronnen:
{context}"""

    response = client.messages.create(
        model=CLAUDE_MODEL,
        max_tokens=1500,
        messages=[{"role": "user", "content": prompt}],
    )
    generated_text = response.content[0].text

    # Sla op als generated_question JSON
    gvraag_id = _save_generated_question(concept, po_filter, patroon, generated_text)

    return generated_text, gvraag_id


def _save_generated_question(concept: str, po_filter: str, patroon: dict | None,
                               generated_text: str) -> str:
    """Sla de gegenereerde vraag op als JSON."""
    import re as _re
    from datetime import date as _date

    QUESTIONS_DIR.mkdir(parents=True, exist_ok=True)

    slug = _re.sub(r"[^a-z0-9]", "-", concept.lower())[:40].strip("-")
    existing = list(QUESTIONS_DIR.glob(f"gvraag-{slug}-*.json"))
    idx = len(existing) + 1
    gvraag_id = f"gvraag:{slug}-{idx:03d}"
    filename = f"gvraag-{slug}-{idx:03d}.json"

    # Extraheer vraag en antwoord uit de gegenereerde tekst
    vraag_match = _re.search(r"\*\*Vraag\*\*:(.*?)(?=\*\*Antwoord\*\*|$)", generated_text, _re.DOTALL)
    antwoord_match = _re.search(r"\*\*Antwoord\*\*:(.*)", generated_text, _re.DOTALL)

    record = {
        "id": gvraag_id,
        "concept_id": f"concept:{slug}",
        "po": po_filter if po_filter != "Alle PO's" else None,
        "patroon_id": patroon["id"] if patroon else None,
        "patroon_versie": patroon["versie"] if patroon else None,
        "vraagtype": patroon["vraagtypen"][0] if patroon and patroon.get("vraagtypen") else "open",
        "cognitieve_laag": patroon.get("cognitieve_laag") if patroon else "integratie",
        "vraag": vraag_match.group(1).strip() if vraag_match else generated_text,
        "antwoord": antwoord_match.group(1).strip() if antwoord_match else "",
        "gegenereerd_op": _date.today().isoformat(),
        "gegenereerd_door": CLAUDE_MODEL,
        "status": "actief",
        "herzieningsstatus": None,
        "herzieningsreden": None,
    }

    (QUESTIONS_DIR / filename).write_text(
        json.dumps(record, ensure_ascii=False, indent=2)
    )
    return gvraag_id


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
    _, ef, reranker, collections = load_rag()
    claude = get_claude()

    active_cols = [n for n in ALL_COLS if n in collections]
    if not active_cols:
        st.error("❌ Geen RAG-collections gevonden. Run eerst `python tools/rag/rag_index.py`.")
        st.stop()

    # --- Sidebar ---
    with st.sidebar:
        st.header("Instellingen")

        po_filter = st.selectbox(
            "Programmaonderdeel (optioneel)",
            ["Alle PO's", "1.1", "1.2", "1.3", "1.4", "1.5",
             "2.1", "2.2", "2.3", "2.4", "2.5", "2.6", "2.7", "2.8",
             "3.1", "3.2", "4.0"],
            index=0,
        )

        modus = st.radio(
            "Modus",
            ["Vraag & Antwoord", "Examenvraag genereren", "Concept opzoeken"],
        )

        st.divider()
        st.caption("Bron-types")
        bron_rol_selectie = {
            rol: st.checkbox(rol, value=True)
            for rol in ALLE_BRON_ROLLEN
        }
        actieve_bron_rollen = [r for r, aan in bron_rol_selectie.items() if aan] or None

        st.divider()
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

            # RAG retrieval
            query = prompt
            if po_filter != "Alle PO's":
                query = f"PO {po_filter} {prompt}"

            with st.spinner("Bronnen zoeken..."):
                chunks, _mode = retrieve_two_pass(
                    collections, reranker, query, ALL_COLS,
                    po_filter=po_filter if po_filter != "Alle PO's" else None,
                    bron_rollen=actieve_bron_rollen,
                )

            context = format_context(chunks)
            sources_display = format_sources_display(chunks)

            # Claude antwoord
            with st.chat_message("assistant"):
                with st.spinner("Antwoord genereren..."):
                    history = [m for m in st.session_state.messages[:-1]]
                    answer = ask_claude(claude, prompt, context, history)
                st.markdown(answer)
                with st.expander("📎 Gebruikte bronnen"):
                    st.text(sources_display)

            st.session_state.messages.append({
                "role": "assistant",
                "content": answer,
                "sources": sources_display,
            })

    # --- Modus: Examenvraag genereren ---
    elif modus == "Examenvraag genereren":
        st.subheader("Examenvraag genereren")

        patterns = load_patterns()

        concept_input = st.text_input(
            "Concept of onderwerp",
            placeholder="bv. 'btw-vrijstelling kleine onderneming'",
        )

        # Patroonkeuze
        patroon_keuze = None
        if patterns:
            patroon_namen = ["Automatisch (beste match)"] + [p["naam"] for p in patterns]
            patroon_select = st.selectbox(
                "Examenpatroon",
                patroon_namen,
                help="Kies een patroon om de vraagstijl te sturen, of laat automatisch kiezen.",
            )

            if patroon_select != "Automatisch (beste match)":
                patroon_keuze = next((p for p in patterns if p["naam"] == patroon_select), None)
            elif concept_input:
                matches = select_patterns_for_concept(patterns, concept_input, po_filter)
                patroon_keuze = matches[0] if matches else None

            if patroon_keuze:
                with st.expander(f"ℹ️ Patroon: {patroon_keuze['naam']}"):
                    st.markdown(f"**{patroon_keuze['beschrijving']}**")
                    st.markdown(f"Cognitieve laag: `{patroon_keuze.get('cognitieve_laag', '?')}`")
                    st.markdown(f"Valkuil: _{patroon_keuze.get('valkuil', '?')}_")
        else:
            st.info("💡 Geen examenpatronen geladen. Run `python tools/examen/extract_exam_patterns.py` om patronen te extraheren.")

        if st.button("Genereer oefenvraag", disabled=not concept_input):
            with st.spinner("Vraag genereren..."):
                case_text, gvraag_id = generate_case(
                    claude, concept_input, po_filter, collections, reranker, patroon_keuze
                )

            st.markdown("---")
            if patroon_keuze:
                st.caption(f"Patroon: **{patroon_keuze['naam']}** · `{gvraag_id}`")

            # Toon situatie + vraag (niet het antwoord)
            antwoord_pos = case_text.find("**Antwoord**")
            vraag_deel = case_text[:antwoord_pos].strip() if antwoord_pos > 0 else case_text
            st.markdown(vraag_deel)

            # Antwoord achter klik
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
                    collections, reranker, concept_search, ALL_COLS,
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
