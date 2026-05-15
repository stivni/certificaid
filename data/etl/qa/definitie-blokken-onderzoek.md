# Definitie-blokken in BE-wetteksten en CBN-adviezen — Empirisch onderzoek

**Datum**: 2026-05-14  
**Doel**: Informatieverzameling voor de adaptive chunker (`chunk.sub_strategy: "per_definitieblok"` in ADR-006 §4.2)  
**Corpus**: 133 wetteksten + 437 CBN-adviezen in `resources/bronnen/`

---

## 1. Inventaris definitie-artikelen

### 1.1 Artikelen met definitie-naam in de heading

| Bron | Artikel-ref | Heading-naam (exact) | Heeft intro-zin? | Aantal 1°-items (geschat) |
|---|---|---|---|---|
| WIB92.md | Art. 2 | *(geen naam, wel definitie-inhoud)* | Ja — meerdere per §: "Er wordt verstaan onder:", "Voor de toepassing van … wordt verstaan onder:" | 40+ (genummerd met °) |
| WBTW.md | Art. 1 §2/6/7/8/12/13/15/19-23 | *(geen naam)* | Ja — "Voor de toepassing van dit Wetboek … wordt verstaan onder:" | ~40 items verspreid over §§ |
| Brusselse-Codex-Fiscale-Procedure.md | Art. 4 | `Art. 4. Voor de toepassing van deze Codex wordt verstaan onder :` | Ja (ingebakken in heading-tekst) | 11 |
| VCF.md | Art. 1.1.0.0.2 | *(geen naam)* onder `Hoofdstuk 1 - Algemene bepalingen en definities` | Ja — "In deze codex wordt verstaan onder :" | 57 |
| Klokkenluiderswet-2022.md | Art. 7 | Onder `Afdeling 4. - Definities` | Ja — "gelden de volgende definities:" | 21 |
| AVG-wet-2018.md | Art. 26 | Onder `HOOFDSTUK I. - Definities` (×4 titels) | Ja — "de toepassing van deze titel wordt verstaan onder :" | 17 |
| AVG-wet-2018.md | Art. 72, 106, 138 | `Art. 72. § 1. De definities bedoeld in ...` | Nee (verwijst terug naar Art. 26) | 0 (cross-ref) |
| Wet-beroepskwalificaties-2008.md | Art. 2 | *(geen naam)* | Ja — "In deze wet wordt verstaan onder :" | 6 |
| Strafwetboek2024-boek1.md | Art. 4 | `Art. 4. Interpretatie van de strafwet` | Nee (proza) | 0 |
| Strafwetboek2024-boek1.md | Art. 17 | `Art. 17. Definitie van daderschap` | Nee (proza) | 0 |
| Strafwetboek2024-boek1.md | Art. 33 | `Art. 33. Definitie` | Nee (proza) | 0 |
| BW-boek4-nalatenschappen.md | Art. 4.193 | `Art. 4.193. Definitie van het algemeen legaat` | Nee (proza) | 0 |
| BW-boek4-nalatenschappen.md | Art. 4.201 | `Art. 4.201. Definitie van het bijzonder legaat` | Nee (proza) | 0 |
| BTW-richtlijn-2006-112.md | Diverse | `Hoofdstuk 1 - Definitie`, `Afdeling 1 - Definitie`, `Afdeling 1 - Definities` | Wisselend | Wisselend |
| WER.md | Hfdst 6–14 | `HOOFDSTUK 6. - Definities eigen aan boek VIII` (×9) | Ja — "gelden de volgende definities:" | 5–20 per hoofdstuk |
| WVV.md | Art. 12:2–12:11 | Onder `HOOFDSTUK 2. Definities.` | Nee — definitie-tekst zonder intro | Elk artikel = 1 definitie |
| WVV.md | Hfdst 1 Boek 16 | `HOOFDSTUK 1. Definities en toepasselijk recht.` | Nee (verwijst naar Europese verordening) | 0 |
| Strafwetboek2024-boek2.md | Diverse | `Onderafdeling 1. Definities`, `Afdeling 1. Definities` (×4) | Ja — "wordt verstaan onder" of proza | 3–10 |
| Oud-BW.md | Diversen | `Definities` in afdelingnaam | Wisselend | Wisselend |
| VCF.md | Div. | `Hoofdstuk 1 - Algemene bepalingen en definities` | Ja | Zie boven |
| Wet-verzekeringen-2014.md | Div. | `TITEL I. — Toepassingsgebied en definities` | Ja (verwacht) | Groot |
| KB-WVV-2019.md | Div. | `TITEL 1. - Definities` | Ja (verwacht) | Meerdere |
| X-oeso-model-verdrag.md | Art. 3 | `Art. 3 — General Definitions` | Ja (EN) | ~10 |
| WBTW.md | Art. 58bis | Onder `Onderafd. 1: Definities` | Ja | ~5 |
| Registratierechten-Waals.md | Art. 50bis en div. | *(geen naam)* | Ja — "Voor de toepassing van deze afdeling wordt verstaan onder:" | 2–8 per artikel |

### 1.2 Bevindingen inventaris

**Totaal geïdentificeerde definitie-secties** (headings met "definities"/"begrippen"/"interpretatie" of artikelen met systematisch definitie-blok-inhoud): **~35–40** locaties verspreid over **~20 bestanden**.

**Belangrijkste observaties**:
- De meeste grote definitie-blokken zitten in artikelen **zonder** "Definitie(s)" in de heading-naam. Voorbeelden: WIB92 Art. 2, WBTW Art. 1, VCF Art. 1.1.0.0.2.
- Artikelen met "Definitie" in de naam zijn vaak *enkelvoudige definities* (proza, geen 1°-lijst) — bv. Strafwetboek Art. 17, BW-boek4 Art. 4.193.
- Echte **definitie-blokken met 1°-lijst** zitten vaker in artikelen met een *afdeling- of hoofdstuk-naam* "Definities", maar het artikel zelf heeft geen definitie-naam.

---

## 2. Intro-patroon-frequenties

Gemeten over 133 wetteksten (`resources/bronnen/wetteksten/`):

| Patroon | Totaal matches | Definitie-blok? (schatting) | Sample-voorbeelden |
|---|---|---|---|
| `wordt verstaan onder` (alle vormen) | **167** | ~120 echte definitie-blokken (rest: enkelvoudige sub-definities in lopende tekst) | Zie §2.1 |
| `Voor de toepassing van ... wordt verstaan onder` | **120** | ~110 definitie-blokken | WIB92 r.4869, AVG r.298, Registratierechten-Waals r.918 |
| `Er wordt verstaan onder` | **7** | 7 definitie-blokken | WIB92 r.145,206,220,272; Oud-BW r.2693; fiscaal-memento r.11629,12272 |
| `In deze codex/wet/dit ... wordt verstaan` | **6** | 6 definitie-blokken | VCF r.57; Wet-beroepskwalificaties r.40 |
| `gelden de volgende definities` | **12** | 12 definitie-blokken | Klokkenluiderswet r.152; WER Hfdst 6-14 (×9) |
| `hebben de volgende termen de betekenis` | **2** | 2 definitie-blokken | WIB92 r.66, r.2095 |
| `in de zin van` | **906** | Bijna nooit definitie-blok intro | Verwijzing in lijn, geen blok-opener |
| `worden de volgende termen als volgt gedefinieerd` | ~1 | 1 | WIB92 r.14909 |

### 2.1 Top-3 meest-voorkomende intro-patronen

**Rang 1 — `Voor de toepassing van [scope] wordt verstaan onder :` (120 matches)**

Meest uniform patroon in Belgische wetteksten. Scope varieert:
- "Voor de toepassing van dit Wetboek en de uitvoeringsbesluiten ervan wordt verstaan onder:" (WBTW r.185, r.231, r.347)
- "Voor de toepassing van deze afdeling wordt verstaan onder:" (Registratierechten-Waals r.918, r.2106)
- "Voor de toepassing van deze wet wordt verstaan onder :" (AVG r.77)
- "Voor de toepassing van het pensioensparen ... wordt verstaan onder :" (WIB92 r.4869)
- Gevolgd altijd door een genummerde lijst (1°, 2°, ...) of streepjeslijst.

**Rang 2 — `Er wordt verstaan onder :` (7 matches)**

Kortere vorm, zonder scope-verwijzing. Frequenter in WIB92 (Art. 2, §5 en §6 sub-blokken):
- "Er wordt verstaan onder :" gevolgd door a)/b)/c) of 1°/2°/... (WIB92 r.145)
- Voorkomt BINNEN een groter artikel na een definitie-label zoals "5° Vennootschappen" (sub-blok van Art. 2).

**Rang 3 — `gelden de volgende definities :` (12 matches)**

Moderne formulering, frequenter in post-2010 wetgeving:
- "Voor de toepassing van deze wet en van de besluiten en reglementen tot uitvoering ervan, gelden de volgende definities:" (Klokkenluiderswet r.152)
- "Voor de toepassing van boek VIII gelden de volgende definities :" (WER r.92)
- "Voor de toepassing van dit besluit gelden de volgende definities:" (WBTW-MB29apr2024 r.50)

---

## 3. Cross-check: heading-naam vs. intro-zin

### 3.1 Heeft heading-naam "definities/begrippen" altijd een intro-zin?

**Nee** — bij headings op het niveau van HOOFDSTUK/AFDELING (bv. "HOOFDSTUK 6. - Definities eigen aan boek VIII") volgt de intro-zin in de eerste zin van het artikel eronder. De intro-zin **staat niet in de heading zelf** maar vlak na de article-heading.

**Speciale gevallen zonder intro-zin**:
- **WVV HOOFDSTUK 2. Definities.** (r.363): bevat 10+ artikelen elk met één definitie in proza-vorm. Geen "wordt verstaan onder"-intro. De term wordt gedefinieerd door het artikel zelf te lezen.
- **Strafwetboek Art. 17 "Definitie van daderschap"** en **Art. 33 "Definitie"**: proza-definities zonder intro-zin en zonder 1°-lijst.
- **BW-boek4 Art. 4.193 "Definitie van het algemeen legaat"**: proza.

### 3.2 Heeft intro-zin altijd definitie-naam in heading?

**Nee** — de meeste artikelen met een `wordt verstaan onder`-intro hebben **geen** "definitie(s)" of "begrippen" in de heading. Voorbeelden:
- WIB92 Art. 2 (heading: alleen `###### Art. 2`, geen naam)
- WBTW Art. 1 (heading: `##### Art. 1`, geen naam)
- VCF Art. 1.1.0.0.2 (heading: `###### Art. 1.1.0.0.2.`, geen naam)
- Registratierechten-Waals Art. 50bis (geen naam)

### 3.3 Conclusie cross-check

| Detectiemethode | Precision | Recall | Opmerkingen |
|---|---|---|---|
| Heading-naam bevat "definitie(s)/begrippen/begripsbepalingen" | Laag (veel FP: enkele proza-definities, geen 1°-lijst) | Laag (mist de meeste grote definitie-blokken die geen naam in heading hebben) | Niet voldoende als enige detector |
| Intro-zin `wordt verstaan onder` + ≥2 genummerde items erna | Hoog | Hoog | Betrouwbaarste combinatie |
| `gelden de volgende definities` + ≥2 items | Hoog | Gemiddeld (12 matches) | Aanvullend patroon voor post-2010 |
| Sectie-naam "Definities" op HOOFDSTUK/AFDELING-niveau | Gemiddeld | Gemiddeld | Signaal voor container, niet voor items |

**Aanbeveling**: Heading-naam is **onvoldoende** als enige detector. Intro-zin is onmisbaar.

---

## 4. Definitie-blok-syntaxis

### 4.1 Structuurvarianten

**Variant A — Klassiek Belgisch model** (meest frequent, ~80% van gevallen):

```
###### Art. N

[Intro-zin], wordt verstaan onder :
1° "TERM" : definitie-tekst... ;
2° "TERM" : definitie-tekst... ;
...
```

*Kenmerken*:
- Term staat tussen aanhalingstekens (`"..."` of `"..."`)
- Scheider is ` : ` (spatie-dubbelpunt-spatie)
- Opsomming eindigt op `;`
- Soms ook afsluitende `.` na het laatste item

*Voorbeelden*:
- AVG r.299: `1° "persoonsgegevens" : alle informatie over...`
- Klokkenluiderswet r.153: `1° "inbreuken": handelingen of nalatingen die:`
- Registratierechten-Waals r.5641: `1° "richtlijn": de richtlijn 2011/16/EU...`

**Variant B — Zonder aanhalingstekens** (minder frequent, ~15%):

```
###### Art. N

[Intro-zin] wordt verstaan onder :
1° TERM : definitie-tekst... ;
2° TERM : definitie-tekst...
```

*Kenmerken*:
- Term zonder aanhalingstekens, hoofdletter
- WIB92 Art. 2: `1° Rijksinwoners` (term op eigen regel, sub-definitie daarna)
- WIB92 Art. 2 §5: `5° Vennootschappen` → gevolgd door `Er wordt verstaan onder :` als sub-intro

*Voorbeelden (WIB92 r.68–160)*:
```
1° Rijksinwoners

Onder rijksinwoners worden verstaan :

a) de natuurlijke personen die:
- hun woonplaats in België hebben...
```

**Variant C — WBTW-stijl, inline definitie per §**:

```
§ N. Voor de toepassing van dit Wetboek... wordt verstaan onder "TERM": definitie-tekst.
```
*Enkelvoudige definitie, geen lijst. Niet geschikt voor per-definitie-chunking.*

**Variant D — Streepjeslijst** (zeldzaam, Registratierechten-Waals Art. 50bis):

```
Voor de toepassing van deze afdeling wordt verstaan onder:

- echtgeno(o)t(e) of wettelijke samenwonende, de persoon die...
- wettelijke samenwonende: de persoon die...
```

*Scheider is `,` of `:`, geen aanhalingstekens, geen cijfer-prefix.*

**Variant E — Backtick-quoted term** (WBTW-MB29apr2024, technische besluiten):

```
Voor de toepassing van dit besluit gelden de volgende definities:
1° `Kassasysteem': elk geïnformatiseerd systeem...
2° `Gecertificeerd kassasysteem': ...
```

*Backtick + apostrof als quote-delimiters in technische MB's.*

### 4.2 Pseudo-regex voor een individuele definitie (één 1°-item)

```regex
# Genummerd item (betrouwbaar)
^(\d+°[/\d]*)\s+              # Nummer: 1°, 2°/1, 4°/1, ...
(?:"([^"]+)"|'([^']+)'|`([^']+)'|([A-ZÀÁÂ][^:\n]+?))  # Term: quoted of unquoted
\s*[:-]\s*                    # Scheider: " : " of ": " of ","
(.+?)                         # Definitie-tekst
(?:;|\.\s*$|(?=\n\d+°))       # Einde: ; of . of volgend item
```

Vereenvoudigde variant voor praktisch gebruik:
```regex
^\d+°[/\d]*\s+(?:"[^"]+"|[A-Z][^:\n]+?)\s*[:-]\s*\S
```

### 4.3 Lengtestatistieken definitie-items

| Corpus | Aantal items | Gem. lengte | Min | Max | Mediaan |
|---|---|---|---|---|---|
| WIB92 Art. 2 (r.64–577) | 40 | 1.469 chars | 5 chars | 8.936 chars | 752 chars |
| AVG Art. 26 (r.298–331) | 17 | 484 chars | 133 chars | 2.678 chars | ~400 chars |
| Klokkenluiderswet Art. 7 (r.152–182) | 21 | 321 chars | 79 chars | 1.990 chars | ~250 chars |
| VCF Art. 1.1.0.0.2 (r.57–200) | 57 | 355 chars | 16 chars | 4.266 chars | ~250 chars |

**Conclusie**: Typische definitie-items zijn 250–750 chars. Maar uitschieters tot 8.000+ chars komen voor (WIB92 definitie van "fusie" met subcategoriëen a)/b)/c)). Dit bevestigt dat bin-packing van alle items in één chunk **niet** kan: 40 items × 1.469 gem. = ~59.000 chars >> 24.000 chars hard max.

---

## 5. CBN-adviezen: hebben die definitie-blokken?

### 5.1 Bevindingen na inspectie van 10+ adviezen

**Antwoord: Nee — CBN-adviezen hebben géén definitie-blokken in wettekst-formaat.**

Specifieke bevindingen per advies:

| Advies | Definitie-patroon | Formaat |
|---|---|---|
| CBN-2012-16 (wentelkredieten) | "In wat volgt wordt verstaan onder een wentelkrediet, een kredietvorm..." | Enkelvoudige definitie in proza, geen 1°-lijst |
| CBN-2011-11 (partiële splitsingen) | "Onder partiële splitsing wordt verstaan..." | Enkelvoudige definitie in lopende tekst |
| CBN-2017-02 (gezamenlijke controle) | "Onder gezamenlijke controle wordt verstaan, de controle die..." | Enkelvoudige definitie in proza |
| CBN-2022-11 (vermogensmutatiemethode) | "Onder 'controle' ... wordt verstaan...", "Onder 'geassocieerde vennootschap' wordt verstaan..." | Twee losse definities in proza, aparte zinnen |
| CBN-2019-09 (boekhoudplichtige onderneming) | Heeft `## Wettelijke definities` heading + `1°` items | Maar 1°-items zijn een **citaat van wettekst** (art. III.82 WER), niet CBN eigen definities |
| CBN-2018-18 (going concern) | "Onder gedeeltelijke discontinuïteit wordt verstaan de stopzetting van een bedrijfsonderdeel..." | Enkelvoudige definitie in proza |
| CBN-2012-10 | Voetnoot: "Art. 12 W.Venn.: onder 'geassocieerde vennootschap' wordt verstaan..." | Definitie in voetnoot, niet in body |
| CBN-2009-13 (tax shelter) | "Onder Young Innovative Company wordt verstaan..." | Enkelvoudige definitie in body |

### 5.2 Conclusie CBN-adviezen

CBN-adviezen bevatten:
1. **Enkelvoudige ingebedde definities** ("Onder X wordt verstaan Y") — in proza, geen lijst-formaat
2. **Wettekst-citaten** in 1°-formaat als bronverwijzing (niet als eigen definitie-blok)
3. **Geen eigen definitie-blokken** met meerdere genummerde items in wettekst-stijl

De `per_definitieblok`-strategie is **niet van toepassing** op CBN-adviezen. De bestaande chunk-strategie (hele advies ≤40K / per sectie >40K) volstaat.

---

## 6. Aanbevolen detectie-strategie

### 6.1 Sterke signalen (zelfstandig voldoende)

Deze patronen identificeren een definitie-blok met hoge betrouwbaarheid als ze gevolgd worden door ≥3 genummerde items (`\d+°`):

| Patroon | Regex | Geschatte precision | Recall |
|---|---|---|---|
| **S1** `wordt verstaan onder :` aan het einde van een zin/alinea | `\bwordt verstaan onder\s*:?\s*$` | ~85% | ~75% |
| **S2** `gelden de volgende definities :` | `gelden de volgende definities\s*:` | ~95% | ~10% |
| **S3** `hebben de volgende termen de betekenis` | `hebben de volgende termen` | ~95% | ~2% |

**Combinatieregel (aanbevolen)**: Patroon S1/S2/S3 gevolgd door ≥3 regels die beginnen met `^\d+°` binnen de volgende 20 regels.

### 6.2 Zwakke signalen (combinatie vereist)

| Patroon | Vereiste combinatie | Reden voor zwakte |
|---|---|---|
| Heading bevat "definities/begrippen" | + ≥3 `\d+°`-items in het artikel | Veel headings met "definitie" zijn enkelvoudige proza-definities |
| `in de zin van` | + intro-patroon in zelfde artikel | Bijna altijd verwijzing, nooit zelf een blok-opener |
| Sectienaam "Definities" op HOOFDSTUK-niveau | + artikel met intro-patroon | Container-heading, items zitten in subartikel |

### 6.3 Bijzondere gevallen

**WVV-stijl "één-definitie-per-artikel"**: WVV HOOFDSTUK 2 bevat 10 artikelen elk met één definitie in proza. Geen intro-zin, geen 1°-lijst. Detectie: via ouder-heading "HOOFDSTUK 2. Definities." maar elk artikel is al zelf een chunk → geen verdere splitsing nodig.

**Streepjeslijst** (Registratierechten-Waals Art. 50bis): `^-\s+\w.*:` na intro-zin. Zeldzaam (<5 gevallen). Kan als variant worden opgenomen.

---

## 7. Definitie-blok-syntax: regex en pseudo-code

### 7.1 Detectie van definitie-blok-start

```python
import re

INTRO_PATTERNS = [
    # Patroon 1: "wordt verstaan onder" (hoofdpatroon)
    re.compile(r'\bwordt verstaan onder\s*[:;]?\s*$', re.MULTILINE),
    # Patroon 2: "gelden de volgende definities"
    re.compile(r'gelden de volgende definitie[s]?\s*[:;]?\s*$', re.MULTILINE | re.IGNORECASE),
    # Patroon 3: "hebben de volgende termen de betekenis"
    re.compile(r'hebben de volgende termen\b', re.MULTILINE | re.IGNORECASE),
    # Patroon 4: "worden de volgende termen als volgt gedefinieerd"
    re.compile(r'worden de volgende termen als volgt gedefinieerd', re.MULTILINE | re.IGNORECASE),
]

# Definitie-item regex
DEFINITIE_ITEM = re.compile(
    r'^(\d+°[/\d]*)\s+'          # Nummer (1°, 2°/1, ...)
    r'(?:"([^"]+)"|'              # Quoted term met "..."
    r"\"([^\"]+)\"|"              # Quoted term met "..."
    r'`([^\']+)\'|'               # Backtick-quoted term
    r'([A-ZÀÁÂÄÈÉÊËÏÎÙÛÜ][^:\n]{1,60}?))'  # Unquoted term (hoofdletter)
    r'\s*[:-]\s*'                 # Scheider
    r'(\S.+)',                    # Definitie-tekst
    re.MULTILINE
)

def heeft_definitie_blok(artikel_tekst: str, min_items: int = 3) -> bool:
    """True als artikel een definitie-blok bevat met >= min_items."""
    for patroon in INTRO_PATTERNS:
        if patroon.search(artikel_tekst):
            items = DEFINITIE_ITEM.findall(artikel_tekst)
            if len(items) >= min_items:
                return True
    return False
```

### 7.2 Splitsing in individuele definities

```python
def splits_definitie_blok(artikel_tekst: str) -> list[dict]:
    """
    Splits een artikel met definitie-blok in afzonderlijke definities.
    Elke definitie krijgt: nummer, term, tekst.
    Behoudt de intro-zin als context.
    """
    lines = artikel_tekst.split('\n')
    intro_lines = []
    definitie_items = []
    current_item = None
    
    for line in lines:
        # Detecteer start van nieuw item
        match = re.match(r'^(\d+°[/\d]*)\s+', line)
        if match:
            if current_item:
                definitie_items.append(current_item)
            current_item = {
                'nummer': match.group(1),
                'tekst': line,
                'intro_context': '\n'.join(intro_lines[-5:])  # laatste 5 intro-regels
            }
        elif current_item:
            current_item['tekst'] += '\n' + line
        else:
            intro_lines.append(line)
    
    if current_item:
        definitie_items.append(current_item)
    
    return definitie_items
```

---

## 8. Aanbeveling: chunker-mode

### 8.1 Is één-chunk-per-definitie nodig?

**Ja, voor grote definitie-artikelen.** Onderbouwing:

| Definitie-artikel | Totale grootte | Aantal items | Gemiddeld per item | Conclusie |
|---|---|---|---|---|
| WIB92 Art. 2 | ~26.000 chars | 40 items | 1.469 chars | Overschrijdt 24K-max; splitsing verplicht |
| VCF Art. 1.1.0.0.2 | ~8.000 chars | 57 items | 355 chars | Past in één chunk maar is voor retrieval onhandig |
| Klokkenluiderswet Art. 7 | ~5.200 chars | 21 items | 321 chars | Past in één chunk; splitsing optioneel |
| AVG Art. 26 | ~8.366 chars | 17 items | 484 chars | Past in één chunk; splitsing optioneel |

**Kritisch geval — WIB92 Art. 2**: 26.000 chars overschrijdt de 24K hard max. De bestaande `split_long_chunk` (paragraph-split) zal dit knippen op willekeurige plaatsen → definitie 6°/1 "fusie" (8.936 chars) loopt over naar een volgend fragment zonder context. Per-definitie-chunking lost dit correct op.

**Retrieval-argument**: Een query over "wat is een rijksinwoner" die terecht in WIB92 Art. 2 1° uitkomt, moet **niet** 26.000 chars context meedragen. Eén chunk per definitie geeft precisere embeddings en snellere reranking.

### 8.2 Aanbeveling

1. **Implementeer `per_definitieblok`** als opt-in sub-strategie in de chunker, zoals voorzien in ADR-006 §4.2.

2. **Activeer standaard voor**: bestanden met `sub_strategy: "per_definitieblok"` in frontmatter (momenteel: Antiwitwaswet-2017.md). Voeg ook toe aan WIB92 en WBTW (grote definitie-artikelen).

3. **Detectie-logica** (dubbele drempel aanbevolen):
   - **Sterk signaal** (direct splitsen): intro-patroon S1/S2/S3 + ≥5 `\d+°`-items
   - **Zwak signaal** (splitsen als >12K chars): intro-patroon S1/S2/S3 + ≥3 items

4. **Behoud intro-zin als context** in elke chunk: de breadcrumb moet de intro-zin bevatten ("Voor de toepassing van dit Wetboek wordt verstaan onder") zodat het embedding-model de wettelijke scope snapt.

5. **CBN-adviezen**: geen aanpassing nodig. Enkelvoudige ingebedde definities zijn geen definitie-blokken.

6. **Bin-packing is onvoldoende** voor WIB92 Art. 2 (overschrijdt 24K hard max). Voor kleine definitie-artikelen (≤12K, ≤10 items) is bin-packing acceptabel als fallback.

---

## Bijlage: Bestandslocaties voor verdere verificatie

- **WIB92 definitie-blok**: `/Users/stivni/Documents/ITAA/certificaid/resources/bronnen/wetteksten/WIB92.md` r.64–577 (Art. 2)
- **WBTW definitie-blokken**: r.181–369 (Art. 1 diverse §§)
- **AVG Art. 26**: r.296–332
- **Klokkenluiderswet Art. 7**: r.148–182
- **VCF Art. 1.1.0.0.2**: r.49–200
- **Brusselse Codex Art. 4**: r.61–79
- **Registratierechten-Waals streepjeslijst**: r.918–930 (Art. 50bis)
- **WBTW-MB29apr2024 backtick-variant**: r.50–87
- **WER definitie-hoofdstukken**: r.88–246 (Hfdst 6–14)
- **WVV enkelvoudige definitie-per-artikel stijl**: r.363–410 (Hfdst 2)
