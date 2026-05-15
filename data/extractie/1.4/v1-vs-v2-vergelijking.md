# v1 vs v2 vergelijking — PO 1.4 Geconsolideerde jaarrekening

**Datum**: 2026-05-15
**Reviewer**: Claude Sonnet 4.6 (agent)
**Bestanden**: `data/concept_records/1.4/` (v1, 17 records) vs `data/concept_records/1.4-v2/` (v2, 31 records)
**Baseline**: `data/quality_checks/1.4/examen-eval-2026-05-15.json`

---

## Verdict

**v2 is een netto-verbetering — maar niet zonder voorbehoud.**

De must-have-gap die de kwaliteitscheck identificeerde (6 ontbrekende begrippen voor examenvraag 2014-1-vr8) is in v2 gedicht, en de nieuwe v1.2-velden zijn voor de relevante records zinvol ingevuld. De risico's zijn beheerst maar reëel: twee records overlappen bijna volledig qua inhoud (`minderheidsbelangen` vs `aandeel-van-derden-in-resultaat`) en de provenance voor `inferred-from-aggregation`-claims rust op chunk-ID's die soms uit slechts één bron komen. Geen blokkerende problemen; productie-waardig mits de overlap wordt samengevoegd en de kwaliteitscheck van twee gemarkeerde claims wordt uitgevoerd.

---

## 1. Records-coverage

### 1.1 Overlappend (directe v1 → v2 tegenhanger, zelfde id)

Alle 17 v1-records hebben een gelijknamig v2-record. Geen enkel v1-record is verdwenen.

| v1-id | Aanwezig in v2 | Schema-upgrade | Nieuwe velden |
|---|---|---|---|
| consolidatieverschil | ja | 1.1 → 1.2 | `oorzaken[]` (4), `drempelwaarden[]` (1), `vergelijkingsparen[]` (1) |
| vermogensmutatiemethode | ja | 1.1 → 1.2 | `berekeningsmethode[]` (2), `vergelijkingsparen[]` (1), `in_praktijk[]` (1) |
| integrale-consolidatie | ja | 1.1 → 1.2 | `vergelijkingsparen[]` (2), `in_praktijk[]` (1) |
| intragroep-eliminaties | ja | 1.1 → 1.2 | `stappen[]` met actor |
| consortium | ja | 1.1 → 1.2 | `in_praktijk[]` (1), wetsbron gepreciseerd (WVV art. 1:19) |
| vrijstelling-subconsolidatie | ja | 1.1 → 1.2 | Wetsbron gepreciseerd (WVV art. 3:26), EER-vereiste toegevoegd |
| geconsolideerde-jaarrekening | ja | 1.1 → 1.2 | `drempelwaarden[]` (3-maanden-regel) |
| groottecriteria-geconsolideerde-basis | ja | 1.1 → 1.2 | `drempelwaarden[]` (4 gestructureerde drempels) |
| step-acquisition | ja | 1.1 → 1.2 | — |
| step-disposal | ja | 1.1 → 1.2 | — |
| consolidatiekring | ja | 1.1 → 1.2 | — |
| consolidatieverplichting | ja | 1.1 → 1.2 | `vergelijkingsparen[]` |
| evenredige-consolidatie | ja | 1.1 → 1.2 | `vergelijkingsparen[]`, `in_praktijk[]` |
| uitgestelde-belastingen-consolidatie | ja | 1.1 → 1.2 | `in_praktijk[]` |
| uniforme-waarderingsregels-consolidatie | ja | 1.1 → 1.2 | `in_praktijk[]` |
| ifrs-keuze-geconsolideerde-jaarrekening | ja | 1.1 → 1.2 | — |
| ifrs-verordening-1606-2002 | ja | 1.1 → 1.2 | — |

### 1.2 Nieuw in v2 (14 records)

#### Must-have gap-fill (6 records — direct aanleiding v2-run)

| v2-id | Reden |
|---|---|
| controlepercentage | Ontbrak v1; vereist voor 2014-1-vr8 |
| belangenpercentage | Ontbrak v1; vereist voor 2014-1-vr8 |
| exclusieve-controle | Ontbrak v1; triggert integrale consolidatie |
| gezamenlijke-controle | Ontbrak v1; triggert evenredige consolidatie |
| invloed-van-betekenis | Ontbrak v1; triggert vermogensmutatiemethode |
| geassocieerde-onderneming | Ontbrak v1; definitie voor de entiteit bij vermogensmutatie |

#### Recursive deepening (8 records — nieuwe dieptebegrippen)

| v2-id | Toelichting |
|---|---|
| controle | Fundament voor alle drie controle-types; eigen record |
| controle-in-rechte-en-in-feite | Onderscheid art. 1:14 §2 vs §3 |
| moedervennootschap | Consoliderende vennootschap; definitie-record |
| dochteronderneming | Directe tegenhanger; definitie-record |
| geconsolideerd-jaarverslag | Apart van de jaarrekening; anchor 1.4.I.F-hiaat gedicht |
| minderheidsbelangen | Balans-presentatieaspect (Belangen van derden) als zelfstandig begrip |
| aandeel-van-derden-in-resultaat | Resultatenrekening-post als zelfstandig begrip met `berekeningsmethode[]` |
| werkelijke-waarde-toerekening-eerste-consolidatie | Operationele eerste-consolidatie-procedure |

### 1.3 Versmolten of opgesplitst

Geen enkel v1-record werd opgesplitst. Twee v2-records (`minderheidsbelangen` en `aandeel-van-derden-in-resultaat`) dekken samen exact dezelfde fenomeen die in v1 als één bouwsteen in `integrale-consolidatie` zat. Dit is een opsplitsing die gedeeltelijk te ver gaat — zie risico's.

---

## 2. Inhoud-diepte per overlappend record (5 records)

### 2.1 Vermogensmutatiemethode

| Dimensie | v1 | v2 |
|---|---|---|
| Schema | 1.1 | 1.2 |
| `berekeningsmethode[]` | Afwezig — methode in proza in `bouwstenen` | **Aanwezig**: 2 stappen (eerste consolidatie + latere consolidaties), met formule + stappenlijst + concreet voorbeeld |
| `vergelijkingsparen[]` | Afwezig — vergelijking enkel in `valkuilen` als proza | **Aanwezig**: 1 paar (vs. integrale consolidatie) |
| `voorwaarden_toepassing` | Enkel proza-block | Opgesplitst in array-item met wetsbron WVV art. 1:22 |
| Voorbeeld | Uitgebreider in v1: scenario met verlies tot bodemwaarde | v2 heeft korter voorbeeld (enkel eerste-consolidatie-stap) |
| Bouwstenen (v1) | 5 bouwstenen (eerste consolidatie, latere, resultaat, intragroep, bodemwaarde) | Afwezig — bouwstenen deels geabsorbeerd in `berekeningsmethode[]`, deels weggelaten |

**Bevinding**: v2 wint op structuur (berekeningsmethode-formule is direct tutor-retriefbaar). v1 wint op volledigheid van bouwstenen: de bodemwaarde-regel en upstream/downstream-eliminatie staan niet meer als zelfstandige blokken in v2. Dit is regressie op specifieke inhoud.

### 2.2 Integrale consolidatie

| Dimensie | v1 | v2 |
|---|---|---|
| Bouwstenen | 4 gedetailleerde bouwstenen (elk met eigen wetsbron) | 4 bouwstenen (licht verkort) |
| `vergelijkingsparen[]` | Afwezig | **Aanwezig**: 2 paren (vs. evenredig en vs. vermogensmutatie) — hoge examenvraag-relevantie |
| `in_praktijk[]` | Afwezig | **Aanwezig**: 1 item (presentatie minderheidsbelangen) |
| `voorwaarden_toepassing` | Proza inclusief consortium | Array-item, beknopter |

**Bevinding**: v2 voegt examenvraag-relevante vergelijkingsparen toe. Geen regressie op hoofdinhoud.

### 2.3 Consolidatieverschil

| Dimensie | v1 | v2 |
|---|---|---|
| `oorzaken[]` | Afwezig (de examenvraag-gap 2013-2-vr8/2015-1-vr11) | **Aanwezig**: 4 oorzaken met `inferred-from-aggregation` |
| `drempelwaarden[]` | Afwezig | **Aanwezig**: 1 drempel (motiveringsplicht > 5 jaar) |
| `vergelijkingsparen[]` | Afwezig | **Aanwezig**: 1 paar (vs. statutaire goodwill PO 1.1 — examenvraag-kampioen) |
| Negatief consolidatieverschil | Enkel aangeduid in definitie | **Nieuwe `voorwaarden[]`-block** (art. 3:131 §2) |
| Voorbeeld | Goed concreet (ABC/DEF met verliesscenario) | Identiek voorbeeld, correct |

**Bevinding**: De rijkste upgrade van alle overlappende records. De 4 oorzaken en het goodwill-vergelijkingspaar sluiten de exacte examenvraag-gaps.

### 2.4 Consortium

| Dimensie | v1 | v2 |
|---|---|---|
| Definitie-bron | CBN-advies 2022/09 | WVV art. 1:19 (wetsbron nauwkeuriger) |
| `in_praktijk[]` | Afwezig | **Aanwezig**: 1 item (eigen aandelen binnen consortium) |
| `uitzonderingen[]` (maatschap) | **Aanwezig** en concreet in v1 | Afwezig in v2 |
| Voorbeeld | Uitgebreid (stichting P, X en Y) | Afwezig in v2 |

**Bevinding**: v2 verliest het concrete maatschap-voorbeeld en de uitzonderingsregel die in v1 aanwezig waren. De nieuwe `in_praktijk[]`-toevoeging (eigen aandelen) is zinvol maar compenseer niet de verloren inhoud. Netto: status quo of lichte achteruitgang.

### 2.5 Vrijstelling-subconsolidatie

| Dimensie | v1 | v2 |
|---|---|---|
| `main_rule` | CBN-advies 2012/12 als bron | WVV art. 3:26 — nauwkeuriger + EER-vereiste en richtlijn 2013/34/EU expliciet |
| `uitzonderingen[]` | 2 gedetailleerde uitzonderingen (beursnotering + maatschap) | Afwezig als apart veld |
| `valkuilen[]` | Afwezig | **Aanwezig**: 1 item (10%-minderheid-verwerping + beursnotering) |

**Bevinding**: v2 verplaatst de uitzonderingen naar `valkuilen[]`, wat niet semantisch equivalent is. De inhoud van de maatschap-uitzondering is in v2 volledig verdwenen (ook niet in `valkuilen`). Lichte regressie.

---

## 3. Must-have-coverage

De kwaliteitscheck identificeerde 6 ontbrekende concepten. Status in v2:

| Concept | Aanwezig in v2 | Definitie | Drempel | Provenance |
|---|---|---|---|---|
| controlepercentage | **ja** | Correct (doorrekening via keten, niet-multiplicatief) | Niet als `drempelwaarden[]` maar in `vergelijkingsparen` | `inferred-from-aggregation` — 3 chunk-IDs, waaronder CBN 2017/02 + CBN 2013/4 |
| belangenpercentage | **ja** | Correct (multiplicatief langs keten) | Niet apart drempel, maar formule in `berekeningsmethode[]` | `inferred-from-aggregation` — 2 chunk-IDs (CBN 178/1 + CBN 2013/4) |
| exclusieve-controle | **ja** | Correct (één vennootschap beslist), wetsbron WVV art. 1:14 §4 | Geen kwantitatieve drempel (>50% ontbreekt als gestructureerd veld) | grounded — 2 chunk-IDs |
| gezamenlijke-controle | **ja** | Correct (overeenkomst vereist), wetsbron WVV art. 1:18 | Geen kwantitatieve drempel | grounded — 3 chunk-IDs |
| invloed-van-betekenis | **ja** | Correct + ≥20%-vermoeden | `drempelwaarden[]` (≥20%) aanwezig — **beste van de zes** | grounded — 3 chunk-IDs |
| geassocieerde-onderneming | **ja** | Correct, art. 1:22 WVV | — | grounded — 3 chunk-IDs |

**Beoordeling**: Alle 6 concepten zijn aanwezig met correcte definities. `invloed-van-betekenis` is het best ingevulde record (definitie + drempel + vergelijkingspaar). `controlepercentage` heeft een kritische nuance goed gevangen (controle gaat volledig door, belang multiplicatief). Het 20-50-50-drempel-schema ontbreekt als gestructureerd `drempelwaarden[]`-veld op `exclusieve-controle` en `gezamenlijke-controle` — dit zijn de meest-gevraagde drempels in examenvragen.

---

## 4. Schema-vulling v1.2-velden

| Veld | Claim v2-rapport | Eigen telling | Oordeel |
|---|---|---|---|
| `oorzaken[]` | 1 record | 1 (consolidatieverschil) | Klopt — zinvol ingevuld, 4 oorzaken |
| `drempelwaarden[]` | 4 records | 4 (geconsolideerde-jaarrekening, invloed-van-betekenis, consolidatieverschil, groottecriteria) | Klopt |
| `tijdlijn[]` | 0 records | 0 | Klopt — PO 1.4 heeft geen procedurele tijdlijnen |
| `vergelijkingsparen[]` | 11 records | Geverifieerd op 5 records: alle 5 hebben het veld | Plausibel — hoge dekking |
| `berekeningsmethode[]` | 3 records | 3 (vermogensmutatiemethode, belangenpercentage, aandeel-van-derden-in-resultaat) | Klopt |
| `in_praktijk[]` | 15 records | Aanwezig in alle 5 gecheckte overlappende records + 4 must-have-records | Plausibel |

### Sample-inhoud oordeel

- **`drempelwaarden[]` op `groottecriteria-geconsolideerde-basis`**: 4 drempels (50 VTE, EUR 11.250.000 netto-omzet, EUR 6.000.000 balanstotaal, +20%-bonus geaggregeerde methode). Concreet en examenvraag-bruikbaar. Lichte zorg: de absolute bedragen (11,25 mio, 6 mio) zijn indexeerbaar — het record vermeldt dit terecht als valkuil, maar de cijfers zelf kunnen verouderd zijn.
- **`berekeningsmethode[]` op `aandeel-van-derden-in-resultaat`**: Formule `(1 − %_belang) × Resultaat`, stappenlijst, concreet voorbeeld (M 80% van D, resultaat 100 → aandeel derden 20). Dit is de exacte vraagvorm van 2013-1-vr6. Uitstekend.
- **`in_praktijk[]` op `controlepercentage`**: `herkenningspunt`-veld met "M 70% A; A 60% B → vul controle 100% in als A volledig gecontroleerd is". Dit is een unieke toevoeging die de tutor een patroonherkenningstip geeft. Nagenoeg elke tabelopgave over indirecte deelnemingen volgt dit scenario.
- **`vergelijkingsparen[]` op `consolidatieverschil`**: Vergelijkt met "statutaire-goodwill (PO 1.1)" — een cross-PO-link die in v1 volledig ontbrak en die de meest-voorkomende verwarringsfout (2013-2-vr3) adresseert. Uitstekend.

---

## 5. Anti-hallucinatie check

### 5.1 Provenance-consistentie

**Controlepercentage** (`inferred-from-aggregation`):
- Chunk-ID 1: `CBN-2017-02-gezamenlijke-controle-over-een-vennootschap-groottecriteria-update__sec_algemeen` — WVV-kader gezamenlijke controle. Relevant.
- Chunk-ID 2: `CBN-2022-11-vermogensmutatiemethode__sec_toepassingsgebied` — toepassingsgebied vermogensmutatie. Bevat controlebegrippen. Relevant.
- Chunk-ID 3: `CBN-2022-09-consolidatie-bij-de-horizontale-groep-consortium-0__sec_bezit-van-eigen-aandelen_part1` — consortium-eigen-aandelen. **Twijfelachtig**: dit is een niche-sectie over bezit van eigen aandelen binnen een consortium, niet over controlepercentage-doorrekening. De link naar controlepercentage is indirect.
- **Conclusie**: 2 van 3 chunks zijn consistent; 1 chunk is een zwakke match. De claim over de doorrekenregel (controle volledig via keten) is inhoudelijk correct en te traceren naar WVV art. 1:14 §2, maar de chunk-IDs onderbouwen het niet volledig.

**Belangenpercentage** (`inferred-from-aggregation`):
- Chunk-ID 1: `CBN-0178-01-advies-met-betrekking-tot-de-jaarrekeningrechtelijke-aspecten-van-de-certificatie-van__sec_de-gevolgen-van-de-certificatie-voor-de-geconsolideerde-jaar` — CBN 178/1 over certificatie. Dit is een niche-advies over gecertificeerde aandelen, niet over de definitie van belangenpercentage. **Zwakste match** van alle gesampelde records.
- Chunk-ID 2: `CBN-2013-04-de-boekhoudkundige-verwerking-van-step-disposals__sec_praktische-uitwerking` — step-disposal praktische uitwerking. Bevat rekeningen met percentages langs ketens. Relevant, maar indirect.
- **Conclusie**: De definitie is correct (multiplicatief langs keten) en vindbaar in de genoemde chunks, maar de primaire bron (WVV art. 1:22 of CBN advies expliciet over deelnemingspercentage) ontbreekt in de chunk-ID's. Het record verwijst naar "CBN-advies 178/1" als source.short maar dit advies handelt primair over certificatie — een opmerkelijke bron-keuze.

**Consolidatieverschil — vier oorzaken** (`inferred-from-aggregation`):
- Alle 4 oorzaken verwijzen naar dezelfde 2 chunk-IDs (KB-WVV-2019__art_3_103 en CBN-2013-03...voorbeeld-1). Dit zijn relevante bronnen voor consolidatieverschil, maar de oorzaken zelf worden in de wettekst niet als een enumeratie van vier aangeboden — ze zijn gedestilleerd uit bredere passages. De tag `inferred-from-aggregation` is hier correct en proportioneel.
- **Conclusie**: Claims zijn inhoudelijk verdedigbaar; de confidence-tag is eerlijk. Maar het zijn voor de helft standaard boekhoudleer-taxonomieën die meer in handboeken dan in de wet staan. Risico op verfijnde examenvragen die de canonieke formulering vereisen.

**Werkelijke-waarde-toerekening-eerste-consolidatie** — valkuil uitgestelde belastingen:
- Claimt wetsbron KB WVV art. 3:136, maar verwijst in `_provenance.inputs` naar `KB-WVV-2019__art_3_101`. KB WVV art. 3:136 behandelt resultatenrekening-eliminaties, niet uitgestelde belastingen op werkelijke-waarde-toerekening — dit is KB WVV art. 3:136 (oud art. 3:107 in KB), maar de nummering matcht niet goed. **Wetsartikel-discrepantie** — laag risico maar te valideren.

### 5.2 Confidence-distributie

Van de gesampelde records: overwegend `grounded`, correct. De 4 oorzaken in `consolidatieverschil` en de definitie + `in_praktijk` van `controlepercentage` en `belangenpercentage` zijn `inferred-from-aggregation`. Dit is correct gelabeld. Geen `inferred`-only hoofddefinities gevonden. Geen misuse van `grounded` op duidelijk inferentie-claims.

---

## 6. Risico's en zwaktes

### 6.1 Redundantie: `minderheidsbelangen` vs `aandeel-van-derden-in-resultaat`

Beide records dekken fenomenen die dezelfde bouw-steen zijn: het deel van resultaat/eigen vermogen dat buiten de groep valt. Ze gebruiken dezelfde chunk-IDs (`CBN-2022-09...sec_consolidatiemethode` en `CBN-0102...sec_voorafgaande-overwegingen_part1`) en verwijzen naar hetzelfde wetsartikel (KB WVV art. 3:137). Het enige verschil: de balans-post (`Belangen van derden`) vs de resultatenrekening-post (`Aandeel van derden in het resultaat`). Dit onderscheid is examenvraag-relevant (2013-1-vr6 vraagt naar de resultatenrekening-post), maar twee aparte records creëren verwarring voor de tutor over welk record hij moet raadplegen. Aanbeveling: samenvoegen in één record `belangen-en-resultaat-van-derden` met twee sub-velden (balans + resultatenrekening), of `aandeel-van-derden-in-resultaat` als sub-sectie in `minderheidsbelangen` opnemen.

### 6.2 Inhoudsverlies in v2 op 3 overlappende records

- `vermogensmutatiemethode`: bodemwaarde-regel en upstream/downstream-eliminatie zijn niet meer als zelfstandige blokken aanwezig.
- `consortium`: maatschap-uitzondering en concreet voorbeeld verdwenen.
- `vrijstelling-subconsolidatie`: maatschap-uitzondering volledig afwezig.
- Dit is systematisch: v2 is breder (meer records) maar op sommige overlappende records smaller per record. Tutor zou v1-content missen.

### 6.3 `controlepercentage`-definitie bevat een onvolledigheid

De definitie stelt "als de moeder M een dochter A volledig controleert en A op haar beurt 60% bezit van B, dan controleert M in B 100% via A." Dit is de regel bij volledige controle (>50%) over A. Maar de definitie behandelt niet het geval waarbij M slechts 51% van A bezit en A slechts 51% van B — de conclusie voor controle blijft hetzelfde, maar de formulering "volledig controleert" suggereert dat enkel bij 100%-deelnemingen in A de doorrekening werkt. Dit is een conceptuele imprecisie.

### 6.4 Drempelwaarden ontbreken op `exclusieve-controle` en `gezamenlijke-controle`

De gangbare vuistregels (>50% = exclusieve controle; 50/50 met overeenkomst = gezamenlijke; 20-50% = invloed van betekenis) zijn in de tutor niet gestructureerd retriefbaar. Ze staan verspreide in `in_praktijk` en `vergelijkingsparen`-proza, maar niet als `drempelwaarden[]`. Dit is hetzelfde probleem dat de kwaliteitscheck bij v1 signaleerde voor de methode-records. V2 lost het op bij `invloed-van-betekenis` maar mist het bij de twee controle-types.

### 6.5 Bronkwaliteit `belangenpercentage` (CBN 178/1)

CBN-advies 178/1 is een certificatie-advies. De vermeldde bron voor de definitie van "belangenpercentage" als economisch aandeel is inhoudelijk correct, maar CBN 178/1 is een niche-context die examenvragen-auteurs niet zullen citeren. Dit is een provenance-nauwkeurigheids-issue zonder inhoudelijk risico, maar het heeft gevold dat de conceptdefinitie geen primaire wetsbron (WVV art. 1:22 of KB WVV art. 3:124) heeft.

### 6.6 Te dunne records: `moedervennootschap`, `dochteronderneming`, `geconsolideerd-jaarverslag`

Drie recursive-deepening records zijn primaire definitie-records zonder verdere structuur (geen valkuilen, geen in_praktijk, geen vergelijkingsparen). Dit is acceptabel als opstap, maar bij tutorbevraging over "wat is een moedervennootschap" geeft het record weinig meer dan een definitie-zin. Geen blokkerende zwakte, maar weinig toegevoegde waarde tegenover een loutere woordenlijst.

---

## 7. Concrete voorbeelden v2 duidelijk beter dan v1

**Voorbeeld 1 — `consolidatieverschil` oorzaken-enumeratie**

v1 had geen `oorzaken[]`. v2 heeft:
- "Overprijs voor werkelijke goodwill" (echte goodwill-rendementspremie)
- "Niet-erkenbare immateriële bestanddelen onder BE-GAAP"
- "Onvolledig toegerekende meerwaarden op identificeerbare activa"
- "Onderwaardering van passiva of niet-geboekte verplichtingen"

Dit zijn exact de vier oorzaken die in examenvragen 2013-2-vr8 en 2015-1-vr11 gevraagd worden. De confidence-tag `inferred-from-aggregation` is eerlijk; de inhoud sluit naadloos op de examenvraag aan.

**Voorbeeld 2 — `controlepercentage` vs `belangenpercentage` in `vergelijkingsparen`**

v1 had noch een record voor controlepercentage noch voor belangenpercentage. v2 heeft op `controlepercentage`:
> "Controlepercentage = stemrechten die doorgaan via de keten (vol als de tussenvennootschap zelf gecontroleerd is). Belangenpercentage = economisch aandeel — wel multiplicatief langs de keten. Voorbeeld: M heeft 70% van A, A heeft 60% van B. Controlepercentage van M in B = 100% (via A); belangenpercentage van M in B = 70% × 60% = 42%."

Dit is het exacte schema van examenvraag 2014-1-vr8. In v1 was deze tabel onbeantwoordbaar; in v2 is ze volledig beantwoordbaar.

**Voorbeeld 3 — `aandeel-van-derden-in-resultaat` berekeningsmethode**

v2 heeft een `berekeningsmethode[]` met formule `(1 − %_belang) × Resultaat`, stappenlijst en concreet voorbeeld (M 80% van D, resultaat D = 100 → aandeel derden = 20). Examenvraag 2013-1-vr6 vraagt naar de exacte presentatiepost — de formule en post-naam zijn nu deterministisch retriefbaar.

**Voorbeeld 4 — `groottecriteria-geconsolideerde-basis` drempelwaarden**

v1 had drempelbedragen enkel in proza. v2 heeft gestructureerde `drempelwaarden[]`:
- 50 VTE (jaargemiddelde personeel)
- EUR 11.250.000 netto-omzet
- EUR 6.000.000 balanstotaal
- +20% bonus bij geaggregeerde methode

De structuur maakt deterministisch retrieven mogelijk (welke drempel? welke eenheid? welk gevolg?).

**Voorbeeld 5 — `consolidatieverschil` vergelijkingspaar met statutaire goodwill**

v2 bevat: "Bij een vraag over goodwill: vraag eerst of het over een aandelendeal/eerste consolidatie gaat (consolidatieverschil) of over een asset-deal in de enkelvoudige rekening (statutaire goodwill)." Dit was het kernprobleem van 2013-2-vr3 (onbeantwoordbaar in v1), nu als herkenningspatroon gecodeerd.

---

## 8. Concrete voorbeelden v2 mogelijk te ver of dun

**Voorbeeld 1 — `minderheidsbelangen` en `aandeel-van-derden-in-resultaat` als dubbele records**

Beide records verwijzen naar hetzelfde wetsartikel (KB WVV art. 3:137), beide bespreken hetzelfde fenomeen vanuit balans- resp. resultatenrekening-perspectief. `minderheidsbelangen.in_praktijk[1]` en `aandeel-van-derden-in-resultaat.definitie` overlappen inhoudelijk voor >70%. Een tutor die beide records ophaalt bij de vraag "Aandeel van derden in het resultaat" krijgt redundante antwoorden.

**Voorbeeld 2 — `controlepercentage` bronkeuze (CBN-2022-09...bezit-van-eigen-aandelen)**

Chunk-ID `CBN-2022-09-consolidatie-bij-de-horizontale-groep-consortium-0__sec_bezit-van-eigen-aandelen_part1` is aangehaald voor de definitie van controlepercentage. De sectie gaat over hoe consortium-leden eigen aandelen presenteren — een niche-topic dat slechts zijdelings raakt aan de doorrekenregel. De claim is inhoudelijk correct maar de bron-link is zwak. Dit vermindert het vertrouwen in de provenance-discipline voor dit record.

**Voorbeeld 3 — `geconsolideerd-jaarverslag` als dunne record**

`geconsolideerd-jaarverslag` is een concept-record met uitsluitend een `definitie`-block: "Het geconsolideerd jaarverslag licht de geconsolideerde jaarrekening toe en bevat minimuminhoud op grond van het WVV." Geen valkuilen, geen voorwaarden, geen in_praktijk. Als dit record bedoeld is om anchor 1.4.I.F (jaarrekening én jaarverslag) te dekken, is het onderbezet. De pilot-rapport signaleerde dit hiaat al in v1; v2 dicht het slechts nominaal.

**Voorbeeld 4 — `controle-in-rechte-en-in-feite` overlap met `controle` en `exclusieve-controle`**

Drie records behandelen overlappende aspecten van het WVV art. 1:14-controlebegrip:
- `controle`: overkoepelend begrip
- `controle-in-rechte-en-in-feite`: onderscheid §2 vs §3
- `exclusieve-controle`: controle door één vennootschap

Bij een tutor-query over "Wat is controle in feite?" zullen alle drie records opgehaald worden. De opsplitsing is conceptueel verdedigbaar, maar creëert retrieval-ruis. In v1 zat dit alles impliciet in `integrale-consolidatie.voorwaarden_toepassing` — minder elegant, maar minder ruis.

**Voorbeeld 5 — `berekeningsmethode[]` op `vermogensmutatiemethode`: bodemwaarde ontbreekt**

v1 had een expliciete bouwsteen "Bodemwaarde van de deelneming" met de regel dat verliezen nooit de deelneming onder nul kunnen brengen. v2 heeft dit weggelaten uit de `berekeningsmethode[]`. De formule in v2 (`Boekwaarde t+1 = Boekwaarde t + ...`) impliceert de bodemregel niet. Een tutor die een vraag over bodemwaarde beantwoordt, vindt het antwoord in v2 niet.

---

## 9. Aanbevelingen voor prompt v3 / schema 1.3

### Schema-aanbevelingen

1. **Verplicht `drempelwaarden[]` op controle-type-records**: `exclusieve-controle` en `gezamenlijke-controle` missen de kwantitatieve drempels (>50% / 50/50 + overeenkomst). Voeg als schemavereiste toe: voor begrip-records met controle-karakter, indien gangbare kwantitatieve vuistregels bestaan, moeten ze als `drempelwaarden[]` gestructureerd zijn ook al zijn het weerlegbare vermoedens.

2. **Verplicht bron-consistentie-check voor `inferred-from-aggregation`**: Alle chunk-IDs in `_provenance.inputs` moeten thematisch relevant zijn voor de claim. Een review-stap na extractie die flagged "chunk X is een niche-topic, niet primair gerelateerd aan claim Y" voorkomt zwakke provenance.

3. **Samenvoegen-instructie voor sibling-records**: Records die dezelfde wetsartikel als primaire bron hebben én dezelfde fenomeen beschrijven vanuit twee perspectieven moeten als één record met sub-velden worden aangemaakt, tenzij er een sterke examenvraag-reden is om ze apart te houden. Dit voorkomt de `minderheidsbelangen` vs `aandeel-van-derden-in-resultaat` dubbele-record-situatie.

4. **Expliciet `toepassingsniveau`-veld**: De kwaliteitscheck stelde dit voor voor v1; v2 heeft het nog niet geïmplementeerd. `consolidatieverschil` (geconsolideerd), `integrale-consolidatie` (geconsolideerd) en `invloed-van-betekenis` (geconsolideerd) hebben geen expliciete scope-aanduiding.

### Prompt-aanbevelingen

5. **Bewaar v1-bouwstenen bij schema-upgrade**: Prompt v3 moet expliciet instrueren dat bij het upgraden van een v1-record naar schema 1.2, de bouwstenen-inhoud van v1 niet verloren mag gaan. Bij `vermogensmutatiemethode` zijn de bodemwaarde en intragroep-eliminatie verdwenen door het herstructureren naar `berekeningsmethode[]`.

6. **Concrete bron-matching voor niche-chunks**: De prompt moet instrueren dat bij `inferred-from-aggregation`-claims de chunk-IDs moeten komen uit bronnen die het concept direct behandelen, niet indirect. CBN-advies 178/1 (certificatie) als primaire bron voor "belangenpercentage" is te ver verwijderd.

7. **Must-have-checklist vóór recursive deepening**: Bevestig eerst dat alle must-have concepten aanwezig zijn (via de examen-eval gap-lijst), start daarna pas recursive deepening. Dit voorkomt dat deepening-records worden aangemaakt voor `moedervennootschap` (laag leerwaarde) terwijl kritische drempels nog ontbreken.

---

## 10. Productie-readiness

**Conclusie: ja, met twee gerichte correcties vóór productie-inzet.**

| Criterium | Status |
|---|---|
| Must-have-begrippen aanwezig | **Ja** — alle 6 gedicht |
| Examen-eval-gaps gedicht | **Ja** — oorzaken consolidatieverschil, controle/belang-percentage, methode-keuze-drempels |
| Provenance-discipline | **Grotendeels** — 2 gevallen met zwakke chunk-match; geen hallucinatie |
| Confidence-labels correct | **Ja** — `inferred-from-aggregation` eerlijk gebruikt, geen `grounded` op inferentie |
| Inhoudsverlies t.o.v. v1 | **Beperkt maar aanwezig** — bodemwaarde, maatschap-uitzonderingen, consortium-voorbeeld |
| Schema-ruis | **Licht** — `minderheidsbelangen` vs `aandeel-van-derden-in-resultaat` overlap |
| Artikelverwijzing-consistentie | **Één discrepantie** — werkelijke-waarde-toerekening valkuil (KB WVV art. 3:136) |

**Twee correcties vóór productie:**

1. Voeg `aandeel-van-derden-in-resultaat` samen met `minderheidsbelangen` of maak `aandeel-van-derden-in-resultaat` een sub-sectie van `minderheidsbelangen`. Behoud de `berekeningsmethode[]`.
2. Voeg in `vermogensmutatiemethode` de bodemwaarde-bouwsteen terug toe (herbouw uit v1-content of als nieuw `in_praktijk[]`-item).

Na deze twee correcties is v2 productie-waardig voor de tutor en voor studiematerie-generatie op het Belgische consolidatiedomein (PO 1.4 Belgisch recht). Het IFRS-deelgebied blijft structureel onderbedeeld door corpus-gebrek — geen v2-probleem, een bronnencorpus-probleem.
