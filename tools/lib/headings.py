"""
Library-module: detecteer per-wet structuurhiërarchie en converteer
structuurlabels naar Markdown-headings op de juiste niveaus.

Algoritme (ADR-005 §7, ADR-006 §4.1):
1. detect_hierarchy(body) → ranks volgens vaste Belgische wettekst-hiërarchie
2. apply_conditional_flattening(ranks) → (reduced_ranks, merge_parent)
   - bij overflow (>5 niveaus) default merge-groepen toepassen
3. build_level_map(ranks, merge_parent) → label → MD-niveau
4. inject_headings(body, level_map, merge_parent) → nieuwe body
5. update_frontmatter_chunk(...) → chunk:-blok in YAML-frontmatter

Voor pipeline-gebruik (convert.py): één-stap helper process_wettekst(text).

Deze module bevat enkel de logica — geen CLI of bestands-IO. Heading-injectie
gebeurt nu binnen de unified `convert.py`-pipeline via `process_wettekst()`;
de oude `tools/etl/inject_wettekst_headings.py` is geschrapt in fase D1.
"""
from __future__ import annotations

import re

# ─── Frontmatter-detectie ────────────────────────────────────────────────────

_FRONTMATTER_RE = re.compile(r"\A---\r?\n(.*?)\r?\n---\r?\n", re.DOTALL)

# ─── Label-definities ─────────────────────────────────────────────────────────

# Vaste Belgische wettekst-hiërarchie (ADR-005 §7, ADR-006 §4.1).
# De volgorde van labels is altijd dezelfde; alleen de AANWEZIGHEID varieert per wet.
# Containment-analyse bleek onbetrouwbaar bij sparse nesting (ONDERAFDELING optioneel
# binnen AFDELING), inconsistente BOEK-sectienummering (Antiwitwaswet: BOEK I impliciet),
# en kleine documenten met weinig structuurlabels.
BELGISCHE_HIERARCHIE: list[str] = [
    "DEEL", "BOEK", "TITEL", "HOOFDSTUK", "AFDELING", "ONDERAFDELING",
]

# Herkende structuurlabels voor de Belgische wetshiërarchie.
# SECTIE, PARAGRAAF en ONDERDEEL zijn bewust weggelaten: zij komen in Belgische
# wetteksten zelden voor als sectie-heading en "paragraaf" verschijnt frequent
# als verwijzing in body-tekst (bv. "overeenkomstig paragraaf 1.") wat anders
# tot false positives leidt in de containment-detectie.
STRUCTUURLABELS = [
    "BOEK", "DEEL", "TITEL", "HOOFDSTUK", "AFDELING", "ONDERAFDELING",
]

# Merge-groepen (ADR-005 §7, ADR-006 §4.1):
# (absorbed_label, absorbing_label)
# - absorbed_label verdwijnt als zelfstandige heading
# - absorbing_label krijgt een prefix met de absorbed context
#   bv. ("DEEL", "BOEK") → "## DEEL I - BOEK 2. Titel"
DEFAULT_MERGE_GROUPS: list[tuple[str, str]] = [
    ("DEEL", "BOEK"),
    ("AFDELING", "ONDERAFDELING"),
]

# ─── Regex-patronen ───────────────────────────────────────────────────────────

# Keyword-patroon (case-insensitive voor het sleutelwoord zelf)
# Bevat enkel de zes erkende structuurlabels (zie STRUCTUURLABELS hierboven).
_KEYWORD_PAT = r"(BOEK|DEEL|TITEL|HOOFDSTUK|AFDELING|ONDERAFDELING)"
_KEYWORD_RE = re.compile(
    r"^[\s\xa0]*" + _KEYWORD_PAT + r"\s+",
    re.IGNORECASE,
)

# Nummer-validatie: Romein UPPERCASE of Arabisch (case-sensitive — geen IGNORECASE).
# Dit voorkomt dat gewone woorden als "van", "voor" etc. als Romein worden herkend.
_NR_RE = re.compile(r"[IVXLCDM]+[a-z]*|\d+(?:\.\d+)*[a-z]*")

# Artikel-heading: "Art. X" of "Par. X" met eventueel heading-prefix
_ART_RE = re.compile(r"^(?:#{1,6}\s+)?(Art\.|Par\.)\s+")

# H1 wet-naam: één # zonder verdere structuurlabel — NIET aanraken
_H1_RE = re.compile(r"^# [^#]")


def _strip_heading_prefix(line: str) -> str:
    """Verwijder leading markdown heading-markeringen (### etc.)."""
    return re.sub(r"^#{1,6}\s+", "", line)


def _get_label(line: str) -> str | None:
    """
    Haal het structuurlabel op uit een regel (negeert eventuele heading-prefix).

    Twee-staps aanpak:
    1. Keyword-match: case-insensitive (TITEL, Titel, titel → allemaal OK)
    2. Nummer-validatie: case-sensitive Romein (uppercase) of Arabisch
       → voorkomt false positives zoals "deel van de activa" (lowercase 'v')

    Geeft uppercase keyword terug of None.
    """
    plain = _strip_heading_prefix(line).strip()
    if not plain:
        return None

    # Stap 1: keyword
    m = _KEYWORD_RE.match(plain)
    if not m:
        return None
    keyword = m.group(1).upper()

    # Stap 2: nummer (case-sensitive)
    rest = plain[m.end():]
    nr_m = _NR_RE.match(rest)
    if not nr_m:
        return None

    # Stap 3: na nummer moet einde, scheidingsteken, of HOOFDLETTER (titel) volgen.
    # "Paragraaf 1 is evenwel..." → lowercase 'i' → afwijzen (body-tekst).
    # "AFDELING 1. Algemene..." → '.' → accepteren.
    # "BOEK II VERPLICHTINGEN" → hoofdletter 'V' → accepteren.
    after_nr = rest[nr_m.end():]
    if after_nr:
        after_stripped = after_nr.lstrip()
        if after_stripped and not re.match(r"[\.\-–—:]|[A-Z]", after_stripped):
            return None

    return keyword


def _is_article(line: str) -> bool:
    """Geeft True als de regel een artikel-heading is (Art. of Par.)."""
    plain = _strip_heading_prefix(line).strip()
    return bool(_ART_RE.match(plain))


# ─── Hiërarchie-detectie ─────────────────────────────────────────────────────


def detect_hierarchy(body: str) -> list[str]:
    """
    Detecteer welke structuurlabels aanwezig zijn en orden ze volgens de
    vaste Belgische wettekst-hiërarchie (ADR-005 §7).

    Algoritme:
    1. Scan alle regels op structuurlabels en artikel-headings
    2. Filter op labels die daadwerkelijk aanwezig zijn in het document
    3. Orden volgens BELGISCHE_HIERARCHIE (altijd DEEL > BOEK > TITEL > HOOFDSTUK > ...)
    4. Voeg "Art." toe als laagste rank (chunk-grens)

    Returns: lijst van uppercase labels van hoogste naar laagste, eindigend op "Art."
    Voorbeeld WVV:           ["DEEL", "BOEK", "TITEL", "HOOFDSTUK", "AFDELING", "ONDERAFDELING", "Art."]
    Voorbeeld WIB92:         ["TITEL", "HOOFDSTUK", "AFDELING", "ONDERAFDELING", "Art."]
    Voorbeeld Wet-ITAA-2019: ["HOOFDSTUK", "AFDELING", "ONDERAFDELING", "Art."]
    Voorbeeld simpele wet:   ["Art."]
    """
    present: set[str] = set()

    for line in body.split("\n"):
        label = _get_label(line)
        if label:
            present.add(label)

    aanwezig = [l for l in BELGISCHE_HIERARCHIE if l in present]
    aanwezig.append("Art.")
    return aanwezig


# ─── Conditional flattening ───────────────────────────────────────────────────

def apply_conditional_flattening(
    ranks: list[str],
    merge_groups: list[tuple[str, str]] | None = None,
) -> tuple[list[str], dict[str, str]]:
    """
    Reduceer ranks naar ≤5 niveaus via merge-groepen bij overflow (ADR-006 §4.1).

    H1 = wet-naam (vast), H2–H6 = structuurlabels + Art. → max 5 slots.
    Bij > 5 ranks worden merge-groepen toegepast:
    - absorbed_label verdwijnt als rank; absorbing_label behoudt zijn rank
    - In de output krijgt absorbing_label een prefix met absorbed context

    Niet-samenhangende merges (bv. TITEL+HOOFDSTUK) worden NIET automatisch
    gedaan — te veel informatieverlies; geeft een waarschuwing.

    Returns:
        - reduced_ranks: lijst na merges (streeft naar ≤5 items incl. "Art.")
        - merge_parent: dict {absorbing_label: absorbed_label}
          bv. {BOEK: "DEEL", ONDERAFDELING: "AFDELING"}
    """
    if merge_groups is None:
        merge_groups = DEFAULT_MERGE_GROUPS

    current = list(ranks)
    merge_parent: dict[str, str] = {}

    while len(current) > 5:
        merged = False
        for absorbed, absorbing in merge_groups:
            if absorbed in current and absorbing in current:
                current.remove(absorbed)
                merge_parent[absorbing] = absorbed
                merged = True
                break  # één merge per iteratie

        if not merged:
            break  # geen geschikte merge-groep; doorgaan met >5 niveaus (waarschuwing)

    return current, merge_parent


# ─── Level-map berekenen ──────────────────────────────────────────────────────

def build_level_map(
    ranks: list[str],
    merge_parent: dict[str, str],
) -> dict[str, int]:
    """
    Bouw level_map: label → markdown-heading-niveau (2–6).

    H2 = ranks[0] (hoogste structuurlabel na flattening)
    H3 = ranks[1]
    ...
    Hn = "Art." (laagste, = chunk-grens)

    Absorbed labels (bv. DEEL bij DEEL+BOEK merge) krijgen hetzelfde niveau als
    hun absorbing label (bv. BOEK→H2, DEEL→H2) zodat ze gecombineerd kunnen worden.
    """
    level_map: dict[str, int] = {}
    for i, label in enumerate(ranks):
        level = i + 2  # H2, H3, H4, H5, H6
        level_map[label] = level

    # Absorbed labels: zelfde niveau als hun absorbing label
    for absorbing, absorbed in merge_parent.items():
        if absorbing in level_map:
            level_map[absorbed] = level_map[absorbing]

    return level_map


# ─── Body-conversie ───────────────────────────────────────────────────────────

def inject_headings(
    body: str,
    level_map: dict[str, int],
    merge_parent: dict[str, str],
) -> tuple[str, int]:
    """
    Converteer structuurlabels en artikel-headings naar correcte MD-niveaus.

    Verwerking per regel:
    - H1 wet-naam (start met "# "): NIET aanraken
    - Structuurlabel dat absorbed is (bv. DEEL bij DEEL+BOEK):
      → opslaan als pending context; geen heading emitteren
    - Structuurlabel dat absorbing is (bv. BOEK):
      → indien pending DEEL beschikbaar: "## DEEL I - BOEK 2. Titel"
      → anders: "## BOEK 2. Titel" (standalone)
    - Overig structuurlabel: vervang met correct niveau
    - Art./Par.-heading: vervang met chunk-niveau
    - Pending absorbed labels worden geflushed als:
      (a) absorbing label verschijnt → combineren
      (b) een ander label/artikel verschijnt → standalone emitteren
      (c) einde document → standalone emitteren

    Returns: (nieuwe_body, aantal_conversies)
    """
    lines = body.split("\n")
    resultaat: list[str] = []
    n_conversies = 0

    # pending_merge: {absorbing_label → absorbed_heading_text}
    # Eenmalige consumption-tracking: helpt te bepalen of een absorbed-label
    # standalone moet worden geflushed als er geen absorbing volgt. Wordt bij de
    # eerste matching absorbing-emit gepopt.
    # bv. {BOEK: "DEEL I. Vennootschapsrecht."} → flusht standalone als geen BOEK volgt.
    pending_merge: dict[str, str] = {}

    # merge_context: {absorbing_label → laatste absorbed_heading_text}
    # Persistente context — herhaalt het absorbed-prefix voor ELKE absorbing
    # binnen die scope (bv. DEEL I → BOEK 1, BOEK 2, BOEK 3 krijgen allemaal
    # "DEEL I -" prefix tot een nieuwe DEEL het overschrijft). Lezers verwachten
    # de DEEL-context bij elk BOEK te zien, niet alleen het eerste.
    merge_context: dict[str, str] = {}

    # Inverse van merge_parent voor snelle lookup
    # {absorbed_label → absorbing_label}
    absorbed_to_absorbing: dict[str, str] = {
        absorbed: absorbing for absorbing, absorbed in merge_parent.items()
    }

    def flush_pending(exclude_absorbing: str | None = None) -> None:
        """
        Emit alle pending absorbed labels als zelfstandige heading.
        exclude_absorbing: sla die absorbing label over (wordt zelf gecombineerd).
        """
        nonlocal n_conversies
        for absorbing_label in list(pending_merge.keys()):
            if absorbing_label == exclude_absorbing:
                continue
            absorbed_text = pending_merge.pop(absorbing_label)
            emit_level = level_map.get(absorbing_label, 2)
            prefix = "#" * emit_level
            resultaat.append(f"{prefix} {absorbed_text}")
            n_conversies += 1

    for line in lines:
        stripped = line.strip()

        # Lege regel: doorlaten
        if not stripped:
            resultaat.append(line)
            continue

        # H1 wet-naam: NIET aanraken (start met "# " gevolgd door niet-#)
        if _H1_RE.match(line):
            resultaat.append(line)
            continue

        # Detecteer label of artikel
        label = _get_label(line)
        is_art = _is_article(line)

        if label:
            plain = _strip_heading_prefix(line).strip()

            if label in absorbed_to_absorbing:
                # Absorbed label (bv. DEEL): flush eerder pending (zelfde absorbing),
                # dan opslaan als pending én als persistente context voor herhaling.
                absorbing = absorbed_to_absorbing[label]
                # Flush reeds-pending voor dezelfde absorbing (nieuwe sectie waarvan
                # de vorige absorbed nog niet door een absorbing was geconsumeerd —
                # zeldzaam, maar voorkomt verlies van inhoud)
                if absorbing in pending_merge:
                    old_text = pending_merge.pop(absorbing)
                    lvl = level_map.get(absorbing, 2)
                    resultaat.append(f"{'#' * lvl} {old_text}")
                    n_conversies += 1
                # Flush pending voor andere absorbing labels (structuurwijziging)
                flush_pending(exclude_absorbing=absorbing)
                # Sla op: pending voor consumption-tracking + context voor herhaling
                pending_merge[absorbing] = plain
                merge_context[absorbing] = plain
                n_conversies += 1
                continue

            # Geen absorbed label: flush alle pending die dit label "overtroeft"
            # (d.w.z. het pending absorbed level >= huidig level).
            #
            # Belangrijk: als dit label een absorbing-label is met pending absorbed
            # (bv. BOEK terwijl pending_merge[BOEK] = "DEEL I"), dan moeten we die
            # specifieke pending NIET flushen — die wordt direct hierna gecombineerd
            # tot één heading "## DEEL I - BOEK 2. Titel". Anders mist de merge.
            exclude_from_flush = label if (label in merge_parent and label in pending_merge) else None
            current_level = level_map.get(label, 99)
            for absorbing_label in list(pending_merge.keys()):
                if absorbing_label == exclude_from_flush:
                    continue
                if level_map.get(absorbing_label, 99) >= current_level:
                    flush_pending(exclude_absorbing=exclude_from_flush)
                    break
            else:
                flush_pending(exclude_absorbing=exclude_from_flush)

            if label in level_map:
                level = level_map[label]
                prefix = "#" * level

                if label in merge_parent:
                    # Absorbing label: pop pending (consumption-tracking voorkomt
                    # dat de absorbed nog standalone wordt geflushed), maar gebruik
                    # de PERSISTENTE merge_context voor de prefix-herhaling.
                    if label in pending_merge:
                        pending_merge.pop(label)
                    prefix_text = merge_context.get(label)
                    if prefix_text:
                        heading_line = f"{prefix} {prefix_text} - {plain}"
                    else:
                        # Geen context bekend → standalone (bv. BOEK zonder DEEL ervoor)
                        heading_line = f"{prefix} {plain}"
                else:
                    heading_line = f"{prefix} {plain}"

                resultaat.append(heading_line)
                n_conversies += 1
                continue

        if is_art:
            # Flush alle pending absorbed labels (we gaan nu naar artikel-niveau)
            flush_pending()

            plain = _strip_heading_prefix(line).strip()
            art_level = level_map.get("Art.", 2)
            prefix = "#" * art_level
            new_line = f"{prefix} {plain}"
            if new_line != line.rstrip():
                n_conversies += 1
            resultaat.append(new_line)
            continue

        # Gewone body-regel: doorlaten
        resultaat.append(line)

    # Flush resterende pending labels aan einde document
    flush_pending()

    return "\n".join(resultaat), n_conversies


# ─── Frontmatter chunk-blok ───────────────────────────────────────────────────

def update_frontmatter_chunk(
    frontmatter_raw: str,
    chunk_level: int,
    chunk_type: str = "Art.",
) -> str:
    """
    Voeg het chunk:-blok toe aan de YAML frontmatter, of vervang het bestaande.

    frontmatter_raw bevat het volledige blok incl. "---" delimiters.
    """
    chunk_block = (
        f"chunk:\n"
        f"  level: {chunk_level}\n"
        f'  type: "{chunk_type}"\n'
        f"  sub_strategy: null"
    )

    closing = "\n---\n"
    if not frontmatter_raw.endswith(closing):
        return frontmatter_raw  # onverwacht formaat; niet aanraken

    before = frontmatter_raw[: -len(closing)]

    # Verwijder bestaand chunk-blok als aanwezig
    # Matcht vanaf "\nchunk:" tot de volgende top-level key (niet-ingesprongen)
    before = re.sub(
        r"\nchunk:.*?(?=\n[a-zA-Z]|\Z)",
        "",
        before,
        flags=re.DOTALL,
    )

    return before + "\n" + chunk_block + closing


# ─── High-level helper voor pipeline-gebruik ─────────────────────────────────

def process_wettekst(text: str) -> tuple[str, dict]:
    """
    Volledige één-stap conversie: MD-tekst (frontmatter+body) → (nieuwe_tekst, info).

    Bedoeld voor gebruik in convert.py-pipeline (fase B1): één regel volstaat
    om een wettekst-MD volledig te verrijken (structuurheadings + chunk-blok).

    Stappen (zie module-docstring):
    1. detect_hierarchy(body)
    2. apply_conditional_flattening(ranks)
    3. build_level_map(reduced_ranks, merge_parent)
    4. inject_headings(body, level_map, merge_parent)
    5. update_frontmatter_chunk(frontmatter_raw, chunk_level)

    Args:
        text: volledige MD-tekst inclusief eventuele YAML-frontmatter.

    Returns:
        - nieuwe_tekst: volledige MD-tekst na conversie
        - info: dict met
            - "ranks":          oorspronkelijk gedetecteerde hiërarchie incl. "Art."
            - "reduced_ranks":  ranks na conditional flattening
            - "merge_parent":   {absorbing_label: absorbed_label}
            - "level_map":      label → MD-niveau
            - "chunk_level":    MD-niveau van "Art." (chunk-grens)
            - "n_conversies":   aantal heading-vervangingen door inject_headings
    """
    m = _FRONTMATTER_RE.match(text)
    if m:
        frontmatter_raw = text[: m.end()]
        body = text[m.end():]
    else:
        frontmatter_raw = ""
        body = text

    ranks = detect_hierarchy(body)
    reduced_ranks, merge_parent = apply_conditional_flattening(ranks)
    level_map = build_level_map(reduced_ranks, merge_parent)
    chunk_level = level_map.get("Art.", 2)

    nieuwe_body, n_conversies = inject_headings(body, level_map, merge_parent)
    nieuwe_frontmatter = update_frontmatter_chunk(frontmatter_raw, chunk_level)

    nieuwe_tekst = nieuwe_frontmatter + nieuwe_body

    info = {
        "ranks": ranks,
        "reduced_ranks": reduced_ranks,
        "merge_parent": merge_parent,
        "level_map": level_map,
        "chunk_level": chunk_level,
        "n_conversies": n_conversies,
    }
    return nieuwe_tekst, info
