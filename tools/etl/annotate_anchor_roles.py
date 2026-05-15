"""Annoteer elke node in data/programma/programma.json met `anchor_role`.

Drie rollen:
  * "anchor"    - match-eenheid, krijgt eigen embedding-vector
  * "reference" - directe bron-pointer, geen embedding, hangt aan parent-anker
  * "context"   - vocabulair-vouw onder parent-anker, geen eigen embedding

Voor reference-nodes zetten we ook `source_files` (lijst van bestandnamen uit
`data/bronnen-index.json`) en `scope` (artikelnummer/sectie of "geheel").

Voor parent-nodes met een herkenbaar template-patroon (bv. PO 1.1.II's
"Voor elk hieronder vermeld deel moeten de volgende elementen gekend zijn:")
zetten we `intro_template` als lijst van strings.

Beslissingsregels — zie ADR-018 (anchor-rollen schema-uitbreiding) of de
prompt waar dit script uit voortkomt.
"""

from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[2]
PROGRAMMA = ROOT / "data" / "programma.json"
BRONNEN = ROOT / "data" / "bronnen-index.json"


# =============================================================================
# Bron-resolver: matcht referentie-tekst naar bron-bestanden
# =============================================================================


def build_resolver(bronnen: list[dict]) -> "BronResolver":
    return BronResolver(bronnen)


class BronResolver:
    """Resolves wet-references to source files via curated rules.

    Strategy: gebruik handgeschreven regex-regels die mappen naar exacte
    bestand-stems uit de bronnen-index. Vermijd fuzzy-matching want dat
    levert false positives bij CBN-adviezen die toevallig wettermen
    bevatten.
    """

    def __init__(self, bronnen: list[dict]) -> None:
        self.bronnen = bronnen
        self.by_stem = {b["stem"]: b for b in bronnen}
        # Bouw een regex-naar-stems map. Volgorde telt: meer specifieke
        # patronen eerst.
        self.rules: list[tuple[re.Pattern, list[str]]] = [
            # === EU-richtlijnen / verordeningen ===
            (re.compile(r"verordening.{0,30}1606/2002", re.I), ["EU-IFRS-verordening-1606-2002"]),
            (re.compile(r"richtlijn.{0,5}2013/34", re.I), ["Richtlijn-2013-34-EU"]),
            (re.compile(r"richtlijn.{0,10}\(eu\).{0,10}2018/1673", re.I), ["EU-Richtlijn-witwassen-2018-1673"]),
            (re.compile(r"richtlijn.{0,5}2018/1673", re.I), ["EU-Richtlijn-witwassen-2018-1673"]),
            (re.compile(r"avg.{0,5}verordening|verordening.{0,30}2016/679|gdpr", re.I), ["EU-AVG-Verordening-2016-679"]),
            (re.compile(r"fusierichtlijn|richtlijn.{0,5}2009/133", re.I), ["EU-Richtlijn-fusie-2009-133"]),
            (re.compile(r"moeder.?dochter.?richtlijn|richtlijn.{0,5}2011/96", re.I), ["EU-Richtlijn-moeder-dochter-2011-96"]),
            (re.compile(r"interest.?(en\s+)?royalt|richtlijn.{0,5}2003/49", re.I), ["EU-Richtlijn-interest-royalties-2003-49"]),
            (re.compile(r"btw.?richtlijn|richtlijn.{0,5}2006/112", re.I), ["BTW-richtlijn-2006-112"]),
            (re.compile(r"btw.?teruggaaf.?richtlijn|richtlijn.{0,5}2008/9", re.I), ["BTW-teruggaaf-richtlijn-2008-9"]),
            (re.compile(r"btw.?dertiende.?richtlijn", re.I), ["BTW-dertiende-richtlijn-1986"]),
            (re.compile(r"btw.?uitvoeringsverordening|verordening.{0,5}282/2011", re.I), ["BTW-uitvoeringsverordening-282-2011"]),
            # === Belgische wetboeken ===
            (re.compile(r"wetboek.{0,5}van.{0,5}vennootschappen.{0,5}en.{0,5}verenigingen|\bWVV\b", re.I), ["WVV"]),
            (re.compile(r"\bKB.{0,15}WVV|koninklijk.?besluit.{0,30}29\s*april\s*2019", re.I), ["KB-WVV-2019"]),
            (re.compile(r"wetboek.{0,5}van.{0,5}economisch.{0,5}recht|\bWER\b", re.I), ["WER"]),
            (re.compile(r"\bWIB\s*92\b|wetboek.{0,5}inkomstenbelastingen", re.I), ["WIB92"]),
            (re.compile(r"\bKB\s*WIB|koninklijk.?besluit.{0,30}WIB", re.I), ["KB-WIB92"]),
            # Btw-Wetboek + KB + MB als compilatie-pointer (PO 2.4.I)
            # NB: WBTW-KB-compilatie.md is legacy verwijderd (2026-05-11);
            # de individuele KB/MB-splits zijn de canonical bronnen.
            (re.compile(r"btw\s*-\s*wetboek\s*-\s*KB\s*-\s*MB", re.I), ["WBTW"]),
            (re.compile(r"\bWBTW\b|btw.?wetboek|wetboek.{0,5}btw", re.I), ["WBTW"]),
            (re.compile(r"\bWDRT\b|wetboek.{0,5}diverse.{0,5}rechten", re.I), ["WDRT"]),
            (re.compile(r"wetboek.{0,5}invordering|\bWIB.?inv\b", re.I), ["Wetboek-Invordering"]),
            # === Antiwitwas / Klokkenluider / AVG ===
            (re.compile(r"antiwitwaswet|aww\b", re.I), ["Antiwitwaswet-2017"]),
            (re.compile(r"klokkenluiderswet", re.I), ["Klokkenluiderswet-2022"]),
            (re.compile(r"avg.?wet|wet.{0,40}verwerking.{0,5}van.{0,5}persoonsgegevens", re.I), ["AVG-wet-2018"]),
            # === Strafwetboek ===
            (re.compile(r"strafwetboek\s*2024|nieuw.?strafwetboek", re.I), ["Strafwetboek2024-boek1", "Strafwetboek2024-boek2"]),
            (re.compile(r"strafwetboek", re.I), ["Strafwetboek-1867"]),
            # === Burgerlijk Wetboek ===
            (re.compile(r"oud.?burgerlijk.?wetboek|oud\s*BW", re.I), ["Oud-BW"]),
            (re.compile(r"\bBW\b.{0,5}boek\s*1|boek\s*1.{0,5}BW|algemene.{0,5}bepalingen.{0,5}BW", re.I), ["BW-boek1-algemene-bepalingen"]),
            (re.compile(r"relatievermogensrecht|huwelijksvermogensrecht.{0,40}\bBW\b", re.I), ["BW-boek2-relatievermogensrecht"]),
            (re.compile(r"\bBW\b.{0,5}boek\s*3|goederenrecht", re.I), ["BW-boek3-goederen"]),
            (re.compile(r"nalatenschap|erfrecht.{0,40}\bBW\b", re.I), ["BW-boek4-nalatenschappen"]),
            (re.compile(r"verbintenissen.{0,5}BW|\bBW\b.{0,5}verbintenissen", re.I), ["BW-boek5-verbintenissen"]),
            (re.compile(r"bewijsrecht|\bBW\b.{0,5}bewijs", re.I), ["BW-boek8-bewijs"]),
            (re.compile(r"zekerheden.{0,5}BW|\bBW\b.{0,5}zekerheden", re.I), ["BW-boek9-zekerheden"]),
            # === Successie / Registratie ===
            (re.compile(r"successierechten.{0,5}brussel", re.I), ["Successierechten-Brussel"]),
            (re.compile(r"successierechten.{0,5}wa(a|)l", re.I), ["Successierechten-Waals"]),
            (re.compile(r"successierechten.{0,5}federa", re.I), ["Successierechten-federaal"]),
            (re.compile(r"\bVCF\b|vlaamse.{0,5}codex.{0,5}fiscaliteit", re.I), ["VCF"]),
            (re.compile(r"registratierechten.{0,5}brussel", re.I), ["Registratierechten-Brussel"]),
            (re.compile(r"registratierechten.{0,5}wa(a|)l", re.I), ["Registratierechten-Waals"]),
            (re.compile(r"registratierechten.{0,5}federa", re.I), ["Registratierechten-federaal"]),
            (re.compile(r"brusselse.?codex.?fiscale.?procedure", re.I), ["Brusselse-Codex-Fiscale-Procedure"]),
            (re.compile(r"decreet.{0,30}waals.{0,5}directe.{0,5}belastingen|waalse.{0,5}directe.{0,5}belastingen", re.I), ["Decr-Waals-Directe-Belastingen"]),
            # === ITAA / Beroep / Plichtenleer ===
            (re.compile(r"wet.{0,30}17\s*maart\s*2019|wet.?ITAA|wet.{0,5}van.{0,5}17\s*maart\s*2019", re.I), ["Wet-ITAA-2019"]),
            (re.compile(r"KB.{0,5}1998.{0,5}plichtenleer|plichtenleer.{0,5}accountant", re.I), ["KB-1998-plichtenleer"]),
            (re.compile(r"wet.{0,30}beroepskwalificaties", re.I), ["Wet-beroepskwalificaties-2008"]),
            # === Overig ===
            (re.compile(r"\bMAR.{0,5}vzw|MAR.{0,5}van.{0,5}boekhoudplichtige", re.I), ["MAR-vzw"]),
            (re.compile(r"\bKB\s*21\s*oktober\s*2018|KB.{0,5}21/10/2018|koninklijk.?besluit.{0,30}21\s*oktober\s*2018", re.I), ["KB-21-10-2018"]),
            (re.compile(r"WER.{0,5}boek\s*VIII|boek\s*VIII.{0,5}WER|WER.{0,30}normalisatie", re.I), ["WER-Boek-VIII-normalisatie"]),
            # Boek XX WER (insolventiewetgeving)
            (re.compile(r"boek\s*XX\s+(van\s+)?(het\s+)?wetboek\s+economisch", re.I), ["WER"]),
            (re.compile(r"insolventie.{0,20}WER", re.I), ["WER"]),
            (re.compile(r"verdrag.?WABB|WABB", re.I), ["Verdrag-WABB"]),
            (re.compile(r"oeso.?model|oecd.?model.?verdrag|x.?oeso", re.I), ["X-oeso-model-verdrag"]),
            (re.compile(r"wet.{0,30}voorafgaande.?beslissingen", re.I), ["Wet-voorafgaande-beslissingen-2002"]),
            (re.compile(r"wet.{0,30}arbeidsovereenkomsten", re.I), ["Wet-arbeidsovereenkomsten-1978"]),
            (re.compile(r"wet.{0,30}betalingsachterstand", re.I), ["Wet-betalingsachterstand-2002"]),
            (re.compile(r"wet.{0,30}verzekeringen.{0,5}2014|wet\s*4\s*april\s*2014", re.I), ["Wet-verzekeringen-2014"]),
            (re.compile(r"belgische.?grondwet|grondwet$", re.I), ["BE-Grondwet"]),  # niet in index → source_lookup_failed
        ]
        # cache: known stems
        self._known_stems = set(self.by_stem.keys())

    def resolve(self, text: str) -> tuple[list[str], bool]:
        """Returns (matched_files, lookup_failed).

        - matched_files: list of source-bestand-namen ('.md' achter stem)
        - lookup_failed: True als geen enkele regel matcht
        """
        matched: list[str] = []
        for pat, stems in self.rules:
            if pat.search(text):
                for s in stems:
                    fname = f"{s}.md"
                    if s in self._known_stems and fname not in matched:
                        matched.append(fname)
        return matched, len(matched) == 0


# =============================================================================
# Reference-detector: heuristieken om reference-nodes te herkennen
# =============================================================================


# Sterke patronen: tekst is duidelijk een wet-pointer
REF_PATTERNS_STRONG = [
    # Verordening (EG/EU) nr. <nummer> ...
    re.compile(r"\bverordening\b\s*\(?(?:eg|eu)\)?\s*(?:nr\.?\s*)?\d", re.I),
    # Richtlijn YYYY/NN/EU of (EU) YYYY/NNNN
    re.compile(r"\brichtlijn\b.{0,15}\d{4}/\d+", re.I),
    # Wetboek van X (en Y), Wetboek X, WVV, WIB, WBTW, WER, WDRT
    re.compile(r"\bwetboek\b\s+(van|inkomstenbelastingen|btw|economisch|invordering|diverse)", re.I),
    re.compile(r"\b(WVV|WIB(?:\s*92)?|WBTW|WER|WDRT)\b"),
    # KB van <datum>, koninklijk besluit van <datum>
    re.compile(r"\b(koninklijk\s*besluit|KB)\b.{0,30}\d{1,2}\s+(jan|feb|maa|apr|mei|jun|jul|aug|sep|okt|nov|dec)", re.I),
    re.compile(r"\b(koninklijk\s*besluit|KB)\b.{0,30}\d{4}", re.I),
    # Wet van <datum> / Wet betreffende / Wet inzake / Wet ITAA / Antiwitwaswet etc.
    re.compile(r"\bwet\s+(van|betreffende|inzake|op)\b", re.I),
    re.compile(r"\b(antiwitwaswet|klokkenluiderswet|wet\s*ITAA)\b", re.I),
    # Boek-aanduidingen WER/BW/Strafwetboek
    re.compile(r"\bboek\s+[IVX]+\b.{0,40}(WER|wetboek\s*economisch\s*recht|burgerlijk\s*wetboek|strafwetboek)", re.I),
    # AVG, GDPR
    re.compile(r"\b(AVG|GDPR)\b"),
    # Strafwetboek, Burgerlijk Wetboek, Belgische Grondwet
    re.compile(r"\b(strafwetboek|burgerlijk\s*wetboek|belgische\s*grondwet)\b", re.I),
    # Successierechten <regio>, Registratierechten <regio>, VCF, Brusselse Codex Fiscale Procedure
    re.compile(r"\b(successierechten|registratierechten)\b.{0,5}(brussel|wa(a|)l|federa)", re.I),
    re.compile(r"\b(VCF|brusselse\s*codex\s*fiscale\s*procedure)\b", re.I),
    # OESO-modelverdrag, WABB, Wet voorafgaande beslissingen
    re.compile(r"\b(oeso.?model|WABB|wet.{0,30}voorafgaande.?beslissingen)", re.I),
    # MAR (minimum algemeen rekeningstelsel) als concrete brontekst
    re.compile(r"\bMAR\s+vzw\b", re.I),
]


META_EXCLUDES = {
    "wetten van de federale staat",
    "koninklijke besluiten op boekhoudkundig gebied",
    "rechtsleer en adviezen van de cbn",
    "rechtsleer en adviezen",
    "rechtspraak",
    "verdragen",
    "algemene principes",
    "europese rechtsnormen",
    "filosofie van het koninklijk besluit",
    # Meta-grouping titels die op een wet wijzen maar zelf een container
    # vormen voor conceptuele anker-children (geen directe wet-pointer):
    "andere in het kb/wvv ontwikkelde boekhoudkundige beginselen",
}


def looks_like_reference(text: str, *, has_anchor_children: bool = False) -> bool:
    """Heuristiek: bevat de tekst een directe wet/richtlijn-aanduiding?

    Conservatief: enkel matchen als de tekst een duidelijke wet-pointer is.
    Algemene woorden als 'koninklijk besluit' of 'wet' alleen tellen niet —
    er moet een datum, nummer of specifieke afkorting bij staan.

    Als de node anchor-children heeft, dan is het zelf een anchor-cluster
    (de wetbron is alleen de origin van de eronder vallende concepten).
    """
    if not text:
        return False
    t = text.strip()
    if t.lower().rstrip(".:") in META_EXCLUDES:
        return False
    if has_anchor_children:
        # Hint: een container-node die grotendeels conceptuele anker-children
        # bevat is zelf geen pure reference, ook al staat er een wetnaam in.
        return False
    for pat in REF_PATTERNS_STRONG:
        if pat.search(t):
            return True
    return False


SCOPE_PATTERNS = [
    re.compile(r"\bart(?:ikel|\.)\s*([IVX]+\.\d+(?:[a-z]+)?(?:\s*tot\s*[IVX]+\.\d+(?:[a-z]+)?)?)", re.I),
    re.compile(r"\bartikel\s*(\d+(?:bis|ter|quater|quinquies|sexies|septies)?)", re.I),
    re.compile(r"\bart\.\s*(\d+(?:bis|ter|quater|quinquies|sexies|septies)?)", re.I),
    re.compile(r"§\s*(\d+)", re.I),
    re.compile(r"\bboek\s+([IVX]+|\d+|[A-Z][a-z]+)\b", re.I),
]


def detect_scope(text: str) -> str:
    for pat in SCOPE_PATTERNS:
        m = pat.search(text)
        if m:
            return m.group(0)
    return "geheel"


# =============================================================================
# Hoofdverwerking
# =============================================================================


def annotate_node(
    node: dict,
    *,
    kind: str,
    parent_kind: str | None,
    resolver: BronResolver,
    counters: dict[str, int],
) -> None:
    """Annoteer recursief één node in de boom."""
    code = node.get("code", "")
    text = node.get("tekst", "") or ""

    # === Default-rol per kind ===
    if kind == "taak":
        role = "anchor"
    elif kind in ("subtaak", "doelstelling", "subdoel"):
        role = "context"
    elif kind == "kenniselement_top":
        # Hoofdgroep R (bv. 1.1.I) → standaard anchor.
        # Speciaal: PO 1.5 heeft kenniselementen op top-niveau die zelf
        # wet-references zijn (1.5.I = Richtlijn 2013/34/EU,
        # 1.5.II = Verordening 1606/2002).
        if looks_like_reference(text) and len(text) > 60:
            role = "reference"
        else:
            role = "anchor"
    elif kind == "kenniselement_sub":
        # Standaard: behandeld o.b.v. code-diepte en tekst
        depth = max(0, len(code.split(".")) - 3)  # 0=R, 1=R.L, 2=R.L.N, 3=R.L.N.l/N
        if looks_like_reference(text):
            role = "reference"
        elif depth == 0 or depth == 1:
            # R of R.L → meestal anchor, tenzij heel kort is
            role = "anchor"
        else:
            # R.L.N en dieper → standaard context (vocabulair-vouw)
            role = "context"
    else:
        role = "context"

    node["anchor_role"] = role

    # === Reference-extra-velden ===
    if role == "reference":
        files, failed = resolver.resolve(text)
        node["source_files"] = files
        if failed:
            node["source_lookup_failed"] = True
            counters["source_lookup_failed"] += 1
        node["scope"] = detect_scope(text)

    counters[role] += 1
    counters["total"] += 1

    # === Recursie ===
    for sub in node.get("subtaken", []):
        annotate_node(sub, kind="subtaak", parent_kind=kind, resolver=resolver, counters=counters)
    for d in node.get("doelstellingen", []):
        annotate_node(d, kind="doelstelling", parent_kind=kind, resolver=resolver, counters=counters)
    for sd in node.get("subdoelen", []):
        annotate_node(sd, kind="subdoel", parent_kind=kind, resolver=resolver, counters=counters)
    for ki in node.get("subitems", []):
        annotate_node(
            ki,
            kind="kenniselement_sub",
            parent_kind=kind,
            resolver=resolver,
            counters=counters,
        )


# =============================================================================
# Intro-template injectie: handmatig aangelegde lijst van bekende patronen
# =============================================================================


INTRO_TEMPLATES: dict[str, list[str]] = {
    # PO 1.1.II "DE GEWONE BEDRIJFSUITOEFENING" — PDF p.9
    # "Voor elk hieronder vermeld deel moeten de volgende elementen gekend zijn:"
    "1.1.II": [
        "Algemeenheden en definities",
        "Boekings- en waarderingsregels",
        "Gebruikelijke boekhoudschema's (boekingen in verband met fiscale verplichtingen: bv. btw, Ven.B)",
        "Presentatie van de rekeningen en andere informatie",
    ],
    # PO 2.7.I.B "GEWESTELIJKE FISCALITEIT - Types" — PDF p.39
    # "Voor elk type, de algemene principes kennen betreffende:" (Overgedragen
    # belastingen, Fiscale bevoegdheid van gemeenschappen en gewesten,
    # Autonome belastingen, Vestiging en invordering van belastingen)
    "2.7.I.B": [
        "Overgedragen belastingen",
        "Fiscale bevoegdheid van gemeenschappen en gewesten",
        "Autonome belastingen",
        "Vestiging en invordering van belastingen",
    ],
    # PO 2.7.II.B "LOKALE BELASTINGEN - Types" — zelfde patroon
    "2.7.II.B": [
        "Bevoegdheid om de belasting te heffen",
        "Belastingreglementering",
        "Vestiging en invordering, en vervolging",
        "Regeling van geschillen",
    ],
}


def inject_intro_templates(data: dict) -> int:
    """Zet intro_template op de juiste parent-nodes; return aantal geïnjecteerd."""
    n = 0

    def walk(node: dict) -> None:
        nonlocal n
        code = node.get("code", "")
        if code in INTRO_TEMPLATES:
            node["intro_template"] = INTRO_TEMPLATES[code]
            n += 1
        for sub in node.get("subtaken", []):
            walk(sub)
        for d in node.get("doelstellingen", []):
            walk(d)
        for sd in node.get("subdoelen", []):
            walk(sd)
        for ki in node.get("subitems", []):
            walk(ki)

    for po in data["programmaonderdelen"]:
        for taak in po.get("taken", []):
            walk(taak)
        for ke in po.get("kenniselementen", []):
            walk(ke)
    return n


# =============================================================================
# Entry-point
# =============================================================================


def main() -> None:
    with PROGRAMMA.open() as f:
        data = json.load(f)
    with BRONNEN.open() as f:
        idx = json.load(f)
    bronnen = idx["bronnen"]

    resolver = build_resolver(bronnen)
    counters: dict[str, int] = {
        "anchor": 0,
        "reference": 0,
        "context": 0,
        "source_lookup_failed": 0,
        "total": 0,
    }

    for po in data["programmaonderdelen"]:
        for taak in po.get("taken", []):
            annotate_node(taak, kind="taak", parent_kind=None, resolver=resolver, counters=counters)
        for ke in po.get("kenniselementen", []):
            annotate_node(
                ke,
                kind="kenniselement_top",
                parent_kind=None,
                resolver=resolver,
                counters=counters,
            )

    n_templates = inject_intro_templates(data)

    with PROGRAMMA.open("w") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
        f.write("\n")

    print(f"Totaal nodes geannoteerd: {counters['total']}")
    print(f"  anchor:    {counters['anchor']}")
    print(f"  reference: {counters['reference']}")
    print(f"  context:   {counters['context']}")
    print(f"  source_lookup_failed: {counters['source_lookup_failed']}")
    print(f"intro_template-blokken: {n_templates}")


if __name__ == "__main__":
    main()
