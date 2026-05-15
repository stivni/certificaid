# Sub-marker onderzoek — adaptive chunker

**Datum**: 2026-05-14  
**Corpus**: 118 trusted wetteksten in `resources/bronnen/wetteksten/`  
**Doel**: Empirische basis voor adaptive sub-chunking triggers en regex-patronen

---

## 1. Top-30 grote artikel-chunks

Gesorteerd op char-count na huidige `split_wettekst` + `split_long_chunk` (drempel 8000 chars). De meeste raken de harde grens van 7990–7999 chars, wat bevestigt dat `split_long_chunk` al actief is maar op een arbitraire tekstgrens snijdt in plaats van op een logische sub-grens.

| Nr | Bron | Artikel | Chars | Primaire sub-marker |
|----|------|---------|------:|---------------------|
| 1 | Oud-BW.md | Art. 1649quinquies | 7999 | *geen (inline)* |
| 2 | Oud-BW.md | Art. 8_WAALS_GEWEST | 7999 | *geen (inline)* |
| 3 | Oud-BW.md | Art. 3 | 7999 | *geen (inline)* |
| 4 | BTW-richtlijn-2006-112.md | Artikel 410 | 7998 | *geen (correspondentetabel)* |
| 5 | Oud-BW.md | Art. 492/1 | 7998 | *geen (inline)* |
| 6 | BTW-richtlijn-2006-112.md | Artikel 410 | 7997 | *geen (correspondentetabel)* |
| 7 | Oud-BW.md | Art. 488bis | 7997 | *geen (inline)* |
| 8 | Oud-BW.md | Art. 488bis | 7995 | *geen (inline)* |
| 9 | Registratierechten-federaal.md | Art. 289bis/2 | 7995 | `§ N` |
| 10 | WBTW.md | Art. 42 | 7995 | `N°` |
| 11 | Oud-BW.md | Art. 19 | 7993 | *geen (inline)* |
| 12 | EU-Richtlijn-fusie-2009-133.md | Artikel 19 | 7992 | `a)` |
| 13 | Oud-BW.md | Art. 488bis | 7992 | *geen (inline)* |
| 14 | BTW-richtlijn-2006-112.md | Artikel 410 | 7991 | `N)` |
| 15 | WBTW.md | Art. 39quater | 7991 | `N°` |
| 16 | Registratierechten-Brussel.md | Art. 161 | 7990 | `N°` |
| 17 | VCF.md | Art. 3.12.2.0.1 | 7990 | `-` *(historieklijst, geen logische grens)* |
| 18 | Registratierechten-federaal.md | Art. 289bis | 7989 | `a)` |
| 19 | Registratierechten-federaal.md | Art. 289bis/2 | 7989 | `§ N` |
| 20 | Richtlijn-2013-34-EU.md | Art. 48quater | 7989 | `N.` |
| 21 | WDRT.md | Art. 211bis | 7989 | `§ N` |
| 22 | Registratierechten-federaal.md | Art. 289bis/2 | 7987 | `a)` |
| 23 | Richtlijn-2013-34-EU.md | Artikel 55 | 7985 | `N.` |
| 24 | WBTW-KB41-proportionele-geldboeten.md | Art. 6 | 7985 | `-` *(tabelcellen, geen logische grens)* |
| 25 | Registratierechten-federaal.md | Art. 289bis/2 | 7984 | `§ N` |
| 26 | BTW-richtlijn-2006-112.md | Artikel 410 | 7982 | `a)` |
| 27 | WBTW-KB20-tarieven.md | Art. 3 | 7982 | `N°` |
| 28 | Registratierechten-Brussel.md | Art. 289bis | 7981 | `a)` |
| 29 | Registratierechten-federaal.md | Artikel 162 | 7981 | `N°` |
| 30 | WBTW.md | Art. 109 | 7981 | `-` *(wijzigingslijst, geen logische grens)* |

**Opmerkingen bij de tabel**:
- Nrs. 1–8 en 11, 13: Oud-BW heeft `§` en `N°` **inline** in de tekst (ETL-artefact: de PDF-conversiepipeline heeft de paragraaftekens niet op eigen regels geplaatst). Dit zijn niet-detecteerbare sub-grenzen zonder ETL-fix.
- Nr. 4 + 6 + 14: BTW-richtlijn Artikel 410 is een **correspondentetabel** (oude art. → nieuwe art.). Bevat geen logische sub-grenzen; het patroon is een compacte matrix. Sub-chunking helpt hier niet.
- Nr. 17: VCF — de streepjes zijn **historiekregels** (`- afdeling 3 toegevoegd door art. 273...`), geen inhoudelijke sub-grenzen.
- Nr. 24 + 30: KB41 bijlage en WBTW Art. 109 — streepjes zijn **tabelcellen** (boetes) of **wijzigingslijsten**, geen logische grenzen.

---

## 2. Patronen-frequentie

Geteld over alle 118 trusted wetteksten (enkel regels die BEGINNEN met het patroon, d.w.z. marker-positie).

| Patroon | Beschrijving | Totaal voorkomens | Primaire bronnen |
|---------|-------------|------------------:|-----------------|
| `N°` | Genummerd item Belgische stijl | **10.466** | WBTW, WIB92, WVV, VCF, alle Reg.rechten |
| `§ N.` | Paragraaf met punt (dominant) | **4.188** | AVG-wet, alle BE wetboeken |
| `§ N` | Paragraaf zonder punt | **388** | Antiwitwaswet, WDRT |
| `a)` `b)` `c)` | Letterlijk sub-item | **4.013** | Alle bronnen — EU én BE |
| `-` streepje | Lijstitem met koppelteken | **3.438** | Veel bronnen — maar vaak tabelcellen of historiek |
| `N.` | EU lid-stijl (N. Hoofdletter) | **1.391** | EU-AVG, Richtlijn-2013-34-EU, BTW-richtlijn |
| `N)` | Haak-genummerd EU-stijl | **351** | BTW-richtlijn, Richtlijn-2013-34-EU, VCF, Reg.rechten |
| `i)` `ii)` `iii)` | Romeinse cijfers klein | **220** | EU-bronnen + WBTW-KB1, VCF |
| `I.` `II.` `III.` | Romeinse cijfers groot | **149** | Successierechten (alle), Richtlijn-2013-34, Oud-BW |
| `N°bis/ter/...` | Genummerd item met latijns suffix | **131** | Oud-BW (dominant: 4°bis, 4°ter, ...) |
| `A)` `B)` `C)` | Hoofdletter-haak | **39** | Zeldzaam — KB41 bijlage |
| `§N` (geplakt) | Paragraaf zonder spatie | **7** | VCF, WBTW-KB7 |

### Exacte spatiering van `§ N`

| Variant | Totaal | Voorbeeld |
|---------|-------:|-----------|
| `§ N.` (spatie + punt) | 4.188 | `§ 1.   Van de belasting zijn vrijgesteld:` |
| `§ N` (spatie, geen punt) | 388 | `§ 2   In de zin van § 1 wordt verstaan` |
| `§  N` (twee spaties) | 4 | Zeldzaam artefact in WBTW |
| `§N.` (geplakt + punt) | 2 | VCF (zeldzaam) |
| `§N` (volledig geplakt) | 5 | VCF, WBTW-KB7 |

**Conclusie**: De dominante variant is `§ N.` (spatie + punt). De bestaande regex `_SUB_PARAGRAAF_RE = r'^\s*(§\s*\d+(?:bis|ter|quater)?)'` vangt alle varianten correct op — nul misses in de corpus.

### Exacte context van `N°`

| Variant na `°` | Totaal | Interpretatie |
|----------------|-------:|---------------|
| `° ` (spatie) — échte marker | 10.072 | Correct opgevangen door `_SUB_DEFBLOK_RE` |
| `°,` of `°.` — referentie in zin | ~300 | Valse vriend: `3°, van het Wetboek` |
| `°bis`/`°ter` — marker met suffix | 131 | **Gemist** door huidige regex (eist spatie na `°`) |
| `°)` — sluitingshaak | ~50 | Annotatie-artefact Oud-BW: `1°)>` |

---

## 3. Aanbevolen regex-patronen (geordend meest → minst frequent)

### Patroon 1 — `N°` (definitieblok, Belgische stijl) — **10.466 occurrences**

```python
_SUB_DEFBLOK_RE = re.compile(r'^\s*(\d+°(?:bis|ter|quater|quinquies|sexies|septies|octies|nonies)?(?:\s*/\d+)?)\s')
```

**Huidig**: `r'^\s*(\d+°(?:\s*/\d+)?)\s'`  
**Verschil**: ontbreekt `bis/ter/quater...`-suffix **na** het `°`-teken. De huidige regex vangt `1°/2` (gecombineerde notatie) maar mist `4°bis.`, `4°ter.` etc. (131 gevallen, voornamelijk in Oud-BW).

Concrete voorbeelden uit corpus:
- `Oud-BW.md` r. 4°bis: `4°bis. (de schuldvordering [7 van Fedris]7 voor de uitkeringen...`
- `Oud-BW.md` r. 4°ter: `4°ter. (De bijdragen en bijdrageopslagen verschuldigd aan de Rijksdienst...`
- `Oud-BW.md` r. 4°quinquies: `4°quinquies. (...) <W 2002-06-26/55, art. 83, Inwerkingtreding : 01-04...`

### Patroon 2 — `§ N` (paragraaf, Belgische stijl) — **4.576 occurrences**

```python
_SUB_PARAGRAAF_RE = re.compile(r'^\s*(§\s*\d+(?:bis|ter|quater)?)')
```

**Huidig**: identiek — **geen aanpassing nodig**. De bestaande regex heeft nul misses op de volledige corpus.

Concrete voorbeelden:
- `AVG-wet-2018.md` regel 8: `§ 1. Deze wet is van toepassing op de verwerking van persoonsgegeven...`
- `WBTW.md` Art. 42: `§ 1.   Van de belasting zijn vrijgesteld:` (meerdere spaties na punt)
- `VCF.md`: `§1. Voor de invordering van de belastingen...` (geplakt, ook gedekt)

### Patroon 3 — `a)` `b)` `c)` (letterlijk sub-item) — **4.013 occurrences**

```python
_SUB_LETTER_RE = re.compile(r'^\s*([a-z])\)\s+\S')
```

**Nieuw patroon**. Aanwezig in zowel BE als EU-bronnen. Treedt op als sub-niveau onder `N°` (BE) of `N.` (EU).

Concrete voorbeelden:
- `WBTW.md` Art. 42 §1: `a)    van schepen voor de vaart op volle zee...`
- `EU-Richtlijn-fusie-2009-133.md` Artikel 19: `a) de activa en passiva van het vermogen van één of meer vennootschappen...`
- `Registratierechten-federaal.md` Art. 289bis: `a) lidstaten; b) derde landen met doeltreffende systemen...`

**Attentie**: geldt als sub-sub-marker (niveau 3), niet als top-level split-punt. In bin-pack-strategie: gebruik als secundaire grens als `§ N` of `N°` ontbreekt maar `a)` wel aanwezig is.

### Patroon 4 — `N.` (EU lid-stijl) — **1.391 occurrences**

```python
_SUB_LID_EU_RE = re.compile(r'^(\d+)\.\s+[A-ZÀ-ÿ]')
```

**Nieuw patroon**. Exclusief in EU-teksten (richtlijnen, verordeningen). Structureel equivalent van `§ N` in BE-teksten.

Concrete voorbeelden:
- `EU-AVG-Verordening-2016-679.md` Art. 4: `1. Bij deze verordening worden regels vastgesteld betreffende...`
- `Richtlijn-2013-34-EU.md` Art. 48quater: `2. De in lid 1 bedoelde informatie omvat:`
- `BTW-richtlijn-2006-112.md` Art. 9: `1. Als „belastingplichtige" wordt beschouwd...`

**Detectierisico**: `N.` + hoofdletter is betrouwbaar als start-van-regel-test. Valse vrienden (`overeenkomstig artikel 39. § 1.`) staan nooit aan het begin van een regel.

### Patroon 5 — `N)` (haak-genummerd, EU/Vlaamse stijl) — **351 occurrences**

```python
_SUB_HAAK_N_RE = re.compile(r'^(\d+)\)\s+\S')
```

**Nieuw patroon**. Treedt op in EU-richtlijnen (BTW-richtlijn, Richtlijn-2013-34-EU) en in de VCF en WIB92.

Concrete voorbeelden:
- `BTW-richtlijn-2006-112.md` Art. 226: `1) de datum van uitreiking van de factuur;`
- `Richtlijn-2013-34-EU.md` Art. 48quater §2: `a) de naam... b) een korte beschrijving...`
- `VCF.md` Art. 3.12.2.0.1: `1°de voorwaarden van het abattement...` (soms `1)` in sub-lijsten)

### Patroon 6 — `i)` `ii)` `iii)` (Romeinse sub-items) — **220 occurrences**

```python
_SUB_ROMAN_LC_RE = re.compile(r'^\s*(i{1,3}|iv|vi{0,3}|ix|xi{0,3})\)\s+\S')
```

**Nieuw patroon**. Vrijwel uitsluitend in EU-bronnen als sub-niveau onder `a)`. Treedt ook op in WBTW-KB1, VCF, WIB92 en Strafwetboek 2024.

Concrete voorbeelden:
- `BTW-richtlijn-2006-112.md` Art. 52: `i) door een als zodanig handelende belastingplichtige...`
- `EU-Richtlijn-fusie-2009-133.md` Art. 3: `i) de activa en passiva van het vermogen van één of meer vennootschappen...`
- `VCF.md` Art. 3.12.2.0.1: `i) de voor- en achternaam van de bedrijfsrevisor...`

### Patroon 7 — `I.` `II.` `III.` (Romeinse grote titels) — **149 occurrences**

```python
_SUB_ROMAN_UC_RE = re.compile(r'^([IVX]+)\.\s+[A-ZÀ-ÿ]')
```

**Nieuw patroon**. Treedt op in Successierechten (alle drie gewesten) als categorie-opsomming, in Richtlijn-2013-34-EU als bijlage-structuur, en in Oud-BW als sub-categorie.

Concrete voorbeelden:
- `Successierechten-federaal.md` Art. 17: `I. Voor de in het buitenland gelegen onroerende goederen...`
- `Successierechten-federaal.md` Art. 17: `II. Voor het kapitaal en de interesten vervallen of verkregen...`
- `Richtlijn-2013-34-EU.md` Bijlage III: `I. Immateriële vaste activa` / `II. Materiële vaste activa`

---

## 4. Edge cases en valse vrienden

### Valse vriend 1 — `§ N` als verwijzing in lopende zin

**Frequentie**: 8.145 inline occurrences tegenover 4.576 marker-occurrences (ratio 1,8:1).

**Patroon**: `§` die NIET aan het begin van een regel staat.

**Voorbeelden** (`AVG-wet-2018.md`):
```
In de in de artikelen 37, § 2, 38, § 2, 39, § 4, en 62, § 1, bedoelde gevallen...
de in § 1 verwerken, zijn bovendien gebonden door...
en aan artikel 20, § 1, 6°, van deze wet en mag de betrokkene...
```

**Detectieregel**: de bestaande regex `r'^\s*(§\s*\d+...)'` met `^` (begin-van-regel) is volledig correct. Inline `§`-verwijzingen staan nooit aan het begin van een regel in de huidige corpus. Bevestigd: nul vals-positieven in 118 bronnen.

### Valse vriend 2 — `N°` als verwijzing in lopende zin

**Frequentie**: 9.842 inline occurrences tegenover 10.466 marker-occurrences (ratio bijna 1:1).

**Patroon**: `N°` gevolgd door `,` of `.` (komma of punt) of gekoppeld aan ander woord.

**Voorbeelden** (`AVG-wet-2018.md`):
```
in het eerste lid, 3°, bedoelde besluit verduidelijkt...
in artikel 125, § 1, 1°, van de wet van 13 juni 2005...
het organisme vermeld in § 1, 1° en 2°, wordt zo snel mogelijk...
```

**Detectieregel**: de huidige `_SUB_DEFBLOK_RE` eist een **spatie NA het `°`-teken** (`\d+°...?\s`). Dit is de correcte filter: echte markers worden gevolgd door spatie (dan de inhoud van het item), referenties worden gevolgd door `,` `,` `.` of sluitingshaak. De 394 gemiste items zijn bijna uitsluitend referenties (`1°, van het Wetboek`, `3°-classificatie`, `1°)>` annotaties).

### Valse vriend 3 — `N.` als artikelverwijzing

**Frequentie**: 310 inline verwijzingen van de vorm `overeenkomstig artikel N.` tegenover 1.391 marker-occurrences.

**Patroon**: `N.` gevolgd door een KLEINE letter of spatie-dan-`§` (vervolgzin).

**Voorbeelden** (`AVG-wet-2018.md`):
```
overeenkomstig artikel 39.  ###### Art. 33  § 1
ing bedoeld in artikel 22. § 2. De functionaris
```

**Detectieregel**: eis `^\d+\.\s+[A-ZÀ-ÿ]` — de eerste letter NA de punt-spatie moet een **hoofdletter** zijn. Artikelverwijzingen zijn altijd gevolgd door een kleine letter of een `§`. Bevestigd in corpus: geen valse positieven bij hoofdletter-eis.

### Valse vriend 4 — `-` streepje als tabelcel of historiekregel

**Frequentie**: 3.438 occurrences — maar een groot deel is geen logische sub-grens.

**Typen false friends**:
1. **Tabelcellen** (KB41 bijlage): `- minder dan of gelijk aan 1.250 EUR 5 pct.`
2. **Historiekregels** (VCF): `- afdeling 3 toegevoegd door art. 273 van het decreet van 19 dec. 2014`
3. **Opsomminglijsten** met wijzigingen (WBTW Art. 109): `- art. 12 (§ 1, eerste lid, 2°, vervangen en § 1, aangevuld met een lid)`

**Detectieregel**: streepjes zijn **zelden bruikbaar als sub-grens** voor chunking. Ze markeren geen zelfstandige conceptuele eenheden. Uitzondering: als een artikel ALLEEN streepjes heeft (geen `§`, `N°`, `N.`, `a)`) EN de streepjes bevatten substantiële inhoud (>100 chars per item), dan kan bin-packing op streepjes worden toegepast als fallback. In de praktijk bevatten de 30 grootste chunks slechts 3 gevallen met streepjes als primaire structuur — en alle 3 zijn geen logische grenzen.

### Valse vriend 5 — Oud-BW inline paragrafen

**Probleem**: In Oud-BW staan `§` en `N°` **inline** in de alineatekst, niet op eigen regels. De ETL-conversie heeft de structuur samengevloeid.

**Voorbeeld** (`Oud-BW.md` Art. 1649quinquies):
```
<Ingevoegd bij W 2004-09-01/38, art. 3, Inwerkingtreding : 01-01-2005> § 1. Naast desgevallend 
schadevergoeding, heeft de consument het recht...
[2 Onverminderd het tweede lid is de verkoper ... de consument: 1° heeft nagelaten de verkoper 
onverwijld nadat het gebrek...; 2° heeft nagelaten het dier...]2
§ 2. [1 In eerste instantie heeft de consument het recht...]
```

**Gevolg**: `_detect_sub_boundaries` detecteert nul grenzen in deze chunks. De 8 Oud-BW chunks in de top-30 zijn **niet sub-chunkbaar** met de huidige aanpak. Oplossing vereist ETL-fix (eigen regels voor `§ N`).

**Bronnen met ernstig inline probleem** (inline >> begin-van-regel):
- `Oud-BW.md`: 591 inline vs 466 begin
- `WER.md`: 2.443 inline vs 119 begin — ernstig ETL-probleem
- `WIB92.md`: 1.765 inline vs 939 begin — gedeeltelijk ETL-probleem
- `WBTW.md`: 1.040 inline vs 408 begin

---

## 5. Verificatie bestaande `_detect_sub_boundaries` functie

### Huidige implementatie

```python
_SUB_DEFBLOK_RE = re.compile(r'^\s*(\d+°(?:\s*/\d+)?)\s')
_SUB_PARAGRAAF_RE = re.compile(r'^\s*(§\s*\d+(?:bis|ter|quater)?)')

def _detect_sub_boundaries(text_lines):
    boundaries = []
    for i, line in enumerate(text_lines):
        m = _SUB_DEFBLOK_RE.match(line)
        if m:
            boundaries.append((i, "definitieblok", m.group(1)))
            continue
        m = _SUB_PARAGRAAF_RE.match(line)
        if m:
            boundaries.append((i, "paragraaf", m.group(1).replace(" ", "")))
    return boundaries
```

### Correctheid per patroon

| Patroon | Match-rate | Probleem |
|---------|----------:|---------|
| `§ N` (alle varianten) | **100%** (0 misses) | Geen — regex is correct en volledig |
| `N°` (standaard) | **96%** (394 misses) | Mist `N°bis`, `N°ter` etc. — 131 gevallen |
| `N°` valse vrienden | **0 vals-positieven** | Spatie-eis na `°` werkt correct |
| `N.` (EU lid) | **niet geïmplementeerd** | 1.391 EU-markers niet herkend |
| `a)` (letter-sub) | **niet geïmplementeerd** | 4.013 sub-items niet herkend |
| `N)` (haak) | **niet geïmplementeerd** | 351 EU/Vlaamse items niet herkend |
| `i)` (Romani) | **niet geïmplementeerd** | 220 EU sub-items niet herkend |

### Bevinding

De bestaande `_detect_sub_boundaries` is functioneel voor Belgische wetboeken met `§ N` en `N°` structuur. Ze mist echter:
1. `N°bis/ter/quater` suffixen (Oud-BW, sporadisch elders)
2. Alle EU-structuurpatronen (`N.`, `a)`, `N)`, `i)`)
3. Werkt niet op inline-paragrafen (ETL-artefact in WER, WIB92, Oud-BW, WBTW)

---

## 6. Detectieregel: marker vs. body-referentie

De centrale vraag: hoe onderscheid je een sub-marker van een verwijzing naar dezelfde syntax in lopende tekst?

### Regels in volgorde van betrouwbaarheid

**Regel 1 — Start-van-regel-eis (90%+ precision)**  
Een sub-marker BEGINT een regel. Gebruik altijd `^` (of `re.MULTILINE`). In de volledige corpus van 118 wetteksten produceren alle start-van-regel-checks nul vals-positieven voor `§ N` en bijna nul voor `N.`.

**Regel 2 — Volgt op lege regel of andere marker (versterkt)**  
Van de 10.466 `N°`-markers:
- 61,8% (6.470) staat direct na een lege regel
- 26,2% (2.746) staat direct na een andere marker (sub-sub)
- 11,9% (1.250) staat direct na inhoudstekst (geen lege regel, maar begin van een blok)

De lege-regel-eis verhoogt de zekerheid dat het een marker is, maar is niet verplicht voor correctheid (de start-van-regel-eis alleen is al voldoende).

**Regel 3 — Syntaxis na het marker-token (verfijning)**
- `§ N` → gevolgd door `.` of spatie (betrouwbaar)
- `N°` → gevolgd door spatie (betrouwbaar); gevolgd door `,` of `.` = referentie
- `N.` → gevolgd door hoofdletter (betrouwbaar); gevolgd door kleine letter = artikelverwijzing
- `a)` → gevolgd door niet-leeg karakter (betrouwbaar)
- `N)` → gevolgd door niet-leeg karakter (betrouwbaar)

**Regel 4 — Positie in markdown-structuur**  
Regels die beginnen met `##` of `###` zijn headings; alles na de heading-lijn en vóór de volgende heading is de artikel-body. Sub-markers bevinden zich altijd in de body, nooit in een heading.

### Samengevatte detectieregel

```
Sub-marker = regel die:
  1. Begint (na optionele spaties) met een van de herkende patronen, EN
  2. Het token onmiddellijk gevolgd wordt door spatie/hoofdletter (patroon-specifiek), EN
  3. Zich bevindt in de body van een artikel-chunk (niet in een heading of breadcrumb)
```

---

## Samenvatting bevindingen voor de adaptive chunker

### Top-5 aanbevelingen

1. **Prioriteit 1 — `N°` uitbreiden met suffixen**: Pas `_SUB_DEFBLOK_RE` aan om `N°bis`, `N°ter`, etc. op te vangen. Dit dekt 131 gemiste markers in Oud-BW.

2. **Prioriteit 2 — EU `N.` toevoegen**: Implementeer `_SUB_LID_EU_RE` voor EU-richtlijnen en -verordeningen. Dit dekt 1.391 markers die nu volledig worden gemist. Zonder dit zijn alle EU-tekstchunks (BTW-richtlijn, EU-AVG, Richtlijn-2013-34-EU) niet sub-chunkbaar.

3. **Prioriteit 3 — `a)` als secundaire grens**: Voeg `_SUB_LETTER_RE` toe als niveau-2 marker (gebruik wanneer `§ N` en `N°` ontbreken). Dekt 4.013 sub-items.

4. **Prioriteit 4 — `N)` als EU/Vlaamse variant**: Voeg `_SUB_HAAK_N_RE` toe voor BTW-richtlijn en VCF/WIB92.

5. **Prioriteit 5 — ETL-probleem melden**: Oud-BW, WER en WBTW hebben inline `§`/`N°` (niet op eigen regels). Dit is een ETL-fix, geen chunker-fix. De betreffende chunks zijn voorlopig niet sub-chunkbaar.

### Aanbevolen volgorde voor implementatie

```
1. § N      → reeds gedekt, uitstekend
2. N°       → uitbreiden met °bis/ter-suffix  
3. N. (EU)  → nieuw, hoge prioriteit (EU-bronnen)
4. a)       → nieuw, medium prioriteit
5. N)       → nieuw, lage prioriteit (overlap met a))
6. i)/ii)   → nieuw, laagste prioriteit (diep genest, zelden top-level)
7. -        → NIET implementeren als marker (teveel false friends)
```
