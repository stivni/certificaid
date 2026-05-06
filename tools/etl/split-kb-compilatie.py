#!/usr/bin/env python3
"""
Splits WBTW-KB-compilatie.md in losse KB-MDs.

Gebruik:
    python tools/etl/split-kb-compilatie.py [--out DIR]

Detecteert KB-grenzen via FOD page-header markers ("FOD Financiën … Btw KB nr. X").
Voor elk uniek KB worden de aaneengesloten line-ranges samengevoegd, en geschreven
naar `<OUT>/WBTW-KB{nr}-{slug}.md` met YAML-frontmatter.
"""
import argparse
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
COMPILATIE_MD = ROOT / "resources" / "bronnen" / "wetteksten" / "WBTW-KB-compilatie.md"

# Slug per KB-id. Gebruikt bestaande conventies waar mogelijk.
SLUG_MAP = {
    "1": "voldoening",
    "2": "forfaitaire",
    "2bis": "cafehouders",
    "3": "aftrekken",
    "4": "teruggaven",
    "6": "internationaal-vervoer",
    "7": "invoer",
    "8": "afronding",
    "9": "ambtelijke-aanslag",
    "10": "uitoefening-keuzen",
    "11": "verleggen-maatstaf",
    "13": "tabaksfabricaten",
    "14": "vervreemdingen-gebouwen",
    "15": "schatting-onroerende",
    "16": "vismijn",
    "18": "uitvoer-vrijstellingen",
    "19": "kleine-ondernemingen",
    "20": "tarieven",
    "22": "landbouwondernemers",
    "23": "jaarlijkse-lijst",
    "24": "voldoening-bijzondere",
    "27": "vlees-slachtdieren",
    "30": "financieringshuur",
    "31": "niet-gevestigd",
    "35": "reisbureaus",
    "39": "regeling-93duodecies",
    "41": "proportionele-geldboeten",
    "44": "geldboeten",
    "45": "vrijstelling-diplomaten",
    "46": "intracommunautaire-aangifte",
    "47": "controle-vervoermiddelen-1996",
    "48": "levering-vervoermiddelen",
    "50": "intracommunautaire-opgave",
    "51": "accijnsproducten",
    "52": "intracommunautaire-vrijstellingen",
    "53": "winstmarge-tweedehands",
    "54": "entrepot",
    "55": "btw-eenheid",
    "56": "teruggaaf",
    "57": "plaats-diensten",
    "58": "mededeling-pas-opgerichte",
    "59": "handelsgeschenken",
    "07.06.2007": "uitvoering-84quinquies",
    "30.12.2009": "gks",
    "01.10.2013": "certificatie-gks",
    "04.04.2014": "verificatie-vervoermiddelen",
    "29.08.2019": "registers",
}

# Fallback titel/datum voor KBs waar regex de titel niet vindt
TITLE_FALLBACK = {
    "3": ("K.B. nr. 3 van 10 december 1969, met betrekking tot de aftrekken voor de toepassing van de belasting over de toegevoegde waarde", "10.12.1969"),
    "14": ("K.B. nr. 14 van 3 juni 1970, met betrekking tot de vervreemdingen van gebouwen, gedeelten van gebouwen en het bijhorende terrein", "03.06.1970"),
    "01.10.2013": ("K.B. 1 oktober 2013 met betrekking tot de toepassingsmodaliteiten ten aanzien van de certificatie van een geregistreerd kassasysteem in de horecasector", "01.10.2013"),
}

NL_MONTHS = {
    "januari": 1, "februari": 2, "maart": 3, "april": 4,
    "mei": 5, "juni": 6, "juli": 7, "augustus": 8,
    "september": 9, "oktober": 10, "november": 11, "december": 12,
}


def parse_dutch_date(date_str: str) -> str:
    if not date_str:
        return ""
    m = re.match(r'(\d{1,2})\s+(\w+)\s+(\d{4})', date_str)
    if m and m.group(2).lower() in NL_MONTHS:
        return f"{int(m.group(1)):02d}.{NL_MONTHS[m.group(2).lower()]:02d}.{m.group(3)}"
    if re.match(r'\d{2}\.\d{2}\.\d{4}', date_str):
        return date_str
    return ""


def find_kb_segments(lines: list[str]) -> list[tuple[str, list[tuple[int, int]]]]:
    """Returnt lijst van (kb_id, [(start, end), ...]) — meerdere ranges per KB mogelijk."""
    markers = []
    for i, line in enumerate(lines):
        s = line.strip()
        m = re.match(
            r'^FOD Financi.n.+?(?:Btw|BTW)\s+KB\s+'
            r'(?:nr\.?\s+(\d+\w*)|(\d{2}[\.\-/]\d{2}[\.\-/]\d{4}))',
            s, re.I,
        )
        if m:
            kb = m.group(1) or m.group(2)
            markers.append((i, kb))

    segments = []
    prev_kb = None
    seg_start = None
    for i, kb in markers:
        if kb != prev_kb:
            if prev_kb is not None:
                segments.append((prev_kb, seg_start, i - 1))
            seg_start = i
            prev_kb = kb
    if prev_kb is not None:
        segments.append((prev_kb, seg_start, len(lines) - 1))

    # Eerste KB heeft soms content vóór de eerste page-marker (begin van compilatie-body).
    # Vind eerste echte content-line na de compilatie-frontmatter + H1 + datum-zin.
    if segments:
        first_body_line = 0
        in_frontmatter = False
        passed_h1 = False
        for i, line in enumerate(lines):
            s = line.rstrip()
            if i == 0 and s == "---":
                in_frontmatter = True
                continue
            if in_frontmatter and s == "---":
                in_frontmatter = False
                continue
            if in_frontmatter:
                continue
            if s.startswith("# "):
                passed_h1 = True
                continue
            if passed_h1 and s.strip():
                first_body_line = i
                break
        # Vergroot eerste segment naar voren
        kb_id, _, end = segments[0]
        segments[0] = (kb_id, first_body_line, end)

    # Groepeer alle ranges per KB-id
    from collections import OrderedDict
    grouped = OrderedDict()
    for kb, s, e in segments:
        grouped.setdefault(kb, []).append((s, e))
    return list(grouped.items())


TITLE_TERMINATORS = re.compile(
    r'^\s*(\(|FOD\s+Financi|##\s+Art|HOOFDSTUK|Officieuze|Laatst|Gewijzigd|Ingevoerd|Dit\s+koninklijk|De\s+tekst|$)',
    re.I,
)


def extract_titel(body_lines: list[str], kb_id: str) -> tuple[str, str]:
    """Probeer (officiele_titel, datum_dd.mm.yyyy) uit de body-lijnen te halen.

    Titels lopen vaak over meerdere lijnen — accumuleer tot een terminator.
    """
    if kb_id in TITLE_FALLBACK:
        return TITLE_FALLBACK[kb_id]

    for idx, ln in enumerate(body_lines[:120]):
        s = ln.strip()
        m_nr = re.match(
            r'^Koninklijk\s+[Bb]esluit\s+nr\.?\s+(\d+\w*),?\s*(?:van\s+(\d{1,2}\s+\w+\s+\d{4}),?\s*)?(.*)$',
            s,
        )
        m_datum = None
        if not m_nr:
            m_datum = re.match(
                r'^Koninklijk\s+[Bb]esluit,?\s+van\s+(\d{1,2}\s+\w+\s+\d{4}),?\s*(.*)$',
                s,
            )
        if not (m_nr or m_datum):
            continue

        # Build prefix
        if m_nr:
            nr = m_nr.group(1)
            datum_str = m_nr.group(2) or ""
            rest_first = m_nr.group(3) or ""
        else:
            nr = ""
            datum_str = m_datum.group(1)
            rest_first = m_datum.group(2) or ""

        # Verzamel rest tot een terminator
        rest_parts = [rest_first.strip()] if rest_first.strip() else []
        for nxt in body_lines[idx + 1:idx + 8]:
            ns = nxt.strip()
            if not ns:
                break
            if TITLE_TERMINATORS.match(ns):
                break
            rest_parts.append(ns)
        rest = " ".join(rest_parts).strip().rstrip(".")

        if nr and datum_str:
            titel = f"K.B. nr. {nr} van {datum_str}"
        elif nr:
            titel = f"K.B. nr. {nr}"
        else:
            titel = f"K.B. van {datum_str}"
        if rest:
            titel = f"{titel}, {rest}"
        return titel, parse_dutch_date(datum_str)

    return "", ""


# Cleanup-patronen voor body: strip page-headers/footers en bijwerkings-marginalia
BODY_NOISE = [
    re.compile(r'^FOD Financi.n.+?(?:Btw|BTW)\s+KB.+', re.I),
    re.compile(r'^Btw KB nr\.\s+\d+\s+-\s+bijw.+', re.I),
    re.compile(r'^\s*-\s*\d+\s*-\s*$'),                      # "- 1 -" page numbers
    re.compile(r'^KB\d+\w*\s+pg\..+', re.I),                  # "KB30 pg. Bijw/1 ..."
    re.compile(r'^-\s*KB\d+\w*\s+pg\..+', re.I),
    re.compile(r'^-\s*Recente wijzigingen\s*/\s*\d+\s*-\s*$'),
    re.compile(r'^-\s*Bijlage\s*/\s*\d+\s*-\s*$'),
    re.compile(r'^Recente wijzigingen\s+www\.fisconetplus.+', re.I),
    re.compile(r'^Lijst van de bijwerkingen\b.+', re.I),
    re.compile(r'^www\.fisconetplus\.be\b'),
]


def clean_body(body: str) -> str:
    out_lines = []
    prev_blank = False
    for ln in body.splitlines():
        if any(p.match(ln.strip()) for p in BODY_NOISE):
            continue
        if not ln.strip():
            if prev_blank:
                continue
            prev_blank = True
        else:
            prev_blank = False
        out_lines.append(ln)
    return "\n".join(out_lines).strip() + "\n"


def build_body(lines: list[str], ranges: list[tuple[int, int]]) -> str:
    parts = []
    for s, e in ranges:
        parts.extend(lines[s:e + 1])
        parts.append("")
    return "\n".join(parts).strip() + "\n"


def kb_label(kb_id: str) -> str:
    """Geef een leesbare label terug (KB7 of KB30dec2009)."""
    if re.match(r'^\d{2}[\.\-/]\d{2}[\.\-/]\d{4}$', kb_id):
        m = re.match(r'(\d{2})[\.\-/](\d{2})[\.\-/](\d{4})', kb_id)
        d, mo, y = m.groups()
        month_short = ["", "jan", "feb", "mrt", "apr", "mei", "jun",
                       "jul", "aug", "sep", "okt", "nov", "dec"][int(mo)]
        return f"KB{d}{month_short}{y}"
    return f"KB{kb_id}"


def write_kb(kb_id: str, ranges: list[tuple[int, int]], lines: list[str], out_dir: Path) -> dict:
    raw_body = build_body(lines, ranges)
    titel, datum = extract_titel(raw_body.splitlines(), kb_id)
    body = clean_body(raw_body)
    body_lines = body.splitlines()
    label = kb_label(kb_id)
    slug = SLUG_MAP.get(kb_id, "")
    fname = f"WBTW-{label}-{slug}.md" if slug else f"WBTW-{label}.md"
    out_path = out_dir / fname

    tags = '["VI.B", "2.4"]'
    sectie = "VI.B"

    titel_or_label = titel or f"BTW {label}"
    datum_or_unknown = datum or "?"

    frontmatter = f"""---
tags: {tags}
itaa-lex-sectie: "{sectie}"
wet: "{titel_or_label.replace('"', chr(92) + chr(34))}"
status: "beschikbaar"
bijgewerkt: "{datum_or_unknown}"
bron: "Afgesplitst uit WBTW-KB-compilatie (Fisconetplus, t.e.m. 06.03.2020)"
---

# {titel_or_label}

*Bijgewerkt tot en met {datum_or_unknown} — afgesplitst uit de Fisconet-compilatie van 06.03.2020.*

"""
    out_path.write_text(frontmatter + body)
    return {
        "kb_id": kb_id,
        "label": label,
        "slug": slug,
        "fname": fname,
        "datum": datum,
        "titel": titel,
        "body_lines": len(body_lines),
        "n_ranges": len(ranges),
    }


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--out", default="/tmp/split-kb",
                        help="Output directory (default: /tmp/split-kb)")
    args = parser.parse_args()

    out_dir = Path(args.out)
    out_dir.mkdir(exist_ok=True, parents=True)
    for f in out_dir.glob("WBTW-KB*.md"):
        f.unlink()

    text = COMPILATIE_MD.read_text()
    lines = text.splitlines()

    grouped = find_kb_segments(lines)
    print(f"Unieke KBs in compilatie: {len(grouped)}")

    results = []
    for kb_id, ranges in grouped:
        r = write_kb(kb_id, ranges, lines, out_dir)
        results.append(r)
        warn = "  ⚠️ titel ontbreekt" if not r["titel"] else ""
        warn2 = f"  ⚠️ {r['n_ranges']} ranges" if r["n_ranges"] > 1 else ""
        print(f"  {r['label']:>15s} → {r['fname']:55s} {r['datum'] or '?':12s} ({r['body_lines']} regels){warn}{warn2}")

    print(f"\nGeschreven naar: {out_dir}")


if __name__ == "__main__":
    main()
