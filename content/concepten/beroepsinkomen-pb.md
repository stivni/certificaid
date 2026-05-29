---
title: "Beroepsinkomen (PB)"
concept_type: "kader"
schema_version: "2.2"
status: "concept"
categorieen:
  - kader
  - regeling
ankers:
  - 2.2.VI
  - 2.2.VI.A
  - 2.2.VI.B
  - 2.2.X
tags:
  - concept
  - schema-2.2
  - type-kader
  - cat-kader
  - cat-regeling
  - status-concept
gegenereerd_uit: "data/concepten/records/beroepsinkomen-pb.json"
---

_Kader_ · ook: revenu professionnel · beroepsinkomsten

## Definitie

Beroepsinkomen is de derde inkomenscategorie van de personenbelasting (art. 23 WIB92): inkomsten die rechtstreeks of onrechtstreeks voortkomen uit werkzaamheden van alle aard. De wet onderscheidt vijf species: (1) winst (handelaar/onderneming), (2) baten (vrij beroep), (3) winst en baten van een vorige beroepswerkzaamheid (stopzettingsmeerwaarden), (4) bezoldigingen (werknemers, bedrijfsleiders, meewerkende echtgenoten) en (5) pensioenen, renten en vervangingsinkomsten. Het netto-beroepsinkomen is het brutobedrag verminderd met beroepskosten (werkelijk of forfait), beroepsverliezen van het tijdperk en overgedragen verliezen van vorige tijdperken.

<small>📖 WIB92 — art. 23 — _wettekst_</small>

## Substantie

Beroepsinkomen is de hoofdas van de Belgische personenbelasting: het draagt de progressie (schijven tot 50 %), de bedrijfsvoorheffing aan de bron en de aftrekbare beroepskosten. Vijf species lijken juridisch onderscheiden maar lopen door elkaar: een arts is 'baten', maar in een doktersvennootschap wordt hij 'bedrijfsleider' met bezoldigingen; een zelfstandige boekhouder is 'baten' tot hij een eenmanszaak omzet in BV (dan winst → bezoldiging). De stagiair moet daarom eerst de juiste species identificeren, dan de aftrek-mechaniek (forfait vs werkelijk) en pas dan de indexering en barema-toepassing.

<small>🔗 WIB92 — art. 23, 30 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Rationale

De vijf-species-structuur weerspiegelt het socio-economisch onderscheid tussen arbeid (loontrekkende), kapitaal+arbeid (zelfstandige/bedrijfsleider) en passieve vervanging (pensioen/werkloosheid). Het brutering→aftrek-schema (art. 23 § 2 WIB) zorgt voor symmetrie: ieder belastingplichtige draagt alleen netto-arbeidsinkomsten af. Het forfaitair kostenpercentage (art. 51 WIB) biedt loontrekkenden vereenvoudiging en eenheid (30 % werknemers, 3 % bedrijfsleiders), terwijl zelfstandigen typisch werkelijke kosten verantwoorden.

<small>🔗 WIB92 — art. 23, 51 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Gebruikscontext

**Status**: `in-voege` · basis: WIB92 art. 23-89

**✅ Voor**
- 📖 Bij elke PB-aangifte (vak IV werknemers, vak XVI bedrijfsleiders, vak XVII winst, vak XVIII baten, vak V pensioenen).
- 🔗 Bij omzetting eenmanszaak → vennootschap: verschuiving van 'winst' (PB-art. 23-1°) naar 'bezoldiging bedrijfsleider' (art. 30-2°/32).

## Bouwstenen

### 💡 Species 1 — Winst

Inkomen van handelaars, nijveraars en landbouwers uit hun beroepswerkzaamheid (art. 23 § 1, 1° + art. 24 e.v. WIB92). Aangifte vak XVII PB. Belastbaar zijn alle ondernemingsopbrengsten verminderd met aankoop handelsgoederen + beroepskosten.

<small>📖 WIB92 — art. 23 § 1-1° — _wettekst_</small>

### 💡 Species 2 — Baten

Inkomen van beoefenaars van vrije beroepen, ambten, posten en alle andere niet als loontrekkende uitgeoefende winstgevende bezigheid (art. 23 § 1, 2° + art. 27 WIB92). Aangifte vak XVIII PB. Typisch: arts, advocaat, architect, accountant in persoon. Forfaitair kostenpercentage is dégressief: 28,7 % / 10 % / 5 % / 3 % (art. 51).

<small>📖 WIB92 — art. 23 § 1-2°, art. 51-4° — _wettekst_</small>

### 💡 Species 3 — Winst en baten van een vorige beroepswerkzaamheid

Inkomen verkregen na stopzetting van de beroepswerkzaamheid: stopzettingsmeerwaarden, terugnemingen, nagekomen baten (art. 23 § 1, 3° + art. 28 WIB92). Vaak afzonderlijk belast aan 16,5 % of 33 % (zie record stopzettingsmeerwaarde).

<small>📖 WIB92 — art. 23 § 1-3° — _wettekst_</small>

### 💡 Species 4 — Bezoldigingen

Drie sub-categorieën (art. 30 WIB92): (1) werknemers (art. 31 — arbeidsovereenkomst), (2) bedrijfsleiders (art. 32 — mandataris of leidende functie buiten arbeidsovereenkomst), (3) meewerkende echtgenoten (art. 33). Aangifte vak IV werknemers, vak XVI bedrijfsleiders. Bezoldigingen omvatten loon, voordelen alle aard, premies, tantièmes en gelijkgestelde voordelen.

<small>📖 WIB92 — art. 30 — _wettekst_ · WIB92 — art. 32 — _wettekst_</small>

### 💡 Species 5 — Pensioenen, renten en vervangingsinkomsten

Wettelijke + aanvullende pensioenen, werkloosheidsuitkeringen, ZIV-uitkeringen, brugpensioenen en andere vervangingsinkomsten die een tijdelijke of definitieve derving van bezoldiging compenseren (art. 23 § 1, 5° + art. 34 + art. 146 WIB92). Aangifte vak V PB. Specifieke belastingvermindering art. 147-154.

<small>📖 WIB92 — art. 23 § 1-5° — _wettekst_ · WIB92 — art. 146 — _wettekst_</small>

### 👣 Bewerking bruto → netto (art. 23 § 2 WIB)

**Substantie**: Drie stappen in vaste volgorde (art. 23 § 2): (a) bruto-inkomen per beroepswerkzaamheid − aftrekbare beroepskosten (werkelijk gerechtvaardigd óf forfaitair via art. 51) = netto per werkzaamheid; (b) eventuele beroepsverliezen van het belastbare tijdperk worden afgetrokken van andere beroepswerkzaamheden van dezelfde belastingplichtige; (c) van het saldo worden overgedragen beroepsverliezen van vorige tijdperken afgetrokken. Vrijgestelde inkomsten worden eerst uitgesloten.

<small>📖 WIB92 — art. 23 § 2 — _wettekst_</small>

### 📜 Forfaitair kostenpercentage (art. 51 WIB)

Bij gebrek aan bewezen werkelijke kosten worden beroepskosten forfaitair bepaald op: werknemers 30 % (max € 2.950); bedrijfsleiders 3 % (max € 1.555,50); meewerkende echtgenoten 5 % (max € 2.592,50); baten (dégressief) 28,7 % / 10 % / 5 % / 3 % op schijven (max € 2.592,50); winst 30 % (max € 2.950). Plafonds zijn niet-geïndexeerde bedragen — zie Cijferzakboekje voor geïndexeerd plafond aanslagjaar.

<small>📖 WIB92 — art. 51 — _wettekst_</small>

### 📜 Werkelijke beroepskosten — bewijslast (art. 49 WIB)

Werkelijke beroepskosten zijn aftrekbaar als de belastingplichtige bewijst dat ze in het belastbare tijdperk gedaan of gedragen werden om belastbare inkomsten te verkrijgen of te behouden, én dat hij de echtheid en het bedrag verantwoordt door bewijsstukken (subsidiair: alle door gemeen recht toegelaten bewijsmiddelen, behalve de eed). Niet-aftrekbare uitgaven (art. 53) blijven uitgesloten — zie record beroepskosten.

<small>📖 WIB92 — art. 49 — _wettekst_</small>

### ↪️ Meewerkende echtgenoot — bezoldigingsregime (art. 33)

Een echtgenoot die de zelfstandige helpt zonder andere beroepsinkomsten kan een deel van diens beroepsinkomen krijgen toegerekend als 'bezoldiging meewerkende echtgenoot' (art. 30-3° + art. 33 WIB92). Sinds 2003 verplicht 'maxistatuut' (eigen sociale-zekerheids-bijdragen). Forfaitkosten 5 % met plafond € 2.592,50 (niet-geïndexeerd, art. 51). Niet verwarren met huwelijksquotient — daar is er géén meewerk-activiteit.

<small>📖 WIB92 — art. 30-3°, 33 — _wettekst_</small>

## Voorbeelden

> [!example]- Werknemer met bruto € 45.000 — netto beroepsinkomen via forfait
> _Loontrekkende, geen werkelijke kosten geclaimd, aanslagjaar fictief op niet-geïndexeerde bedragen._
>
> **Berekening:**
>
> Berekening:
>
> | Stap | Bedrag |
> |---|---|
> | Bruto-bezoldigingen (fiche 281.10 code 250) | € 45.000,00 |
> | Persoonlijke RSZ-bijdragen werknemer (13,07 %, art. 52-7°/52-14 WIB) | − € 5.881,50 |
> | Netto belastbaar vóór forfaitkosten | € 39.118,50 |
> | Forfaitair kostenforfait 30 % | € 11.735,55 |
> | → begrensd op plafond (niet-geïndexeerd € 2.950) | − € 2.950,00 |
> | **Netto beroepsinkomen** | **€ 36.168,50** |
>
> In de aangifte: code 1250-11 (bruto) — code 1255-06 (RSZ) — forfait wordt automatisch berekend; bij keuze werkelijke kosten code 1258/1271.
>
> <small>🔗 WIB92 — art. 23, 51, 52-7° — _wettekst_ · aangifte-PB-2025-bezoldigingen — vak IV — _aangifte_</small>

> [!example]- Bedrijfsleider met bruto € 60.000 — netto beroepsinkomen + bedrijfsvoorheffing
> _Zaakvoerder BV. Geen werkelijke kosten geclaimd. Sociale bijdrage zelfstandige zelf afgehouden buiten loonadministratie._
>
> **Berekening:**
>
> Berekening:
>
> | Stap | Bedrag |
> |---|---|
> | Bruto-bezoldiging bedrijfsleider (fiche 281.20 code 400) | € 60.000,00 |
> | Sociale bijdragen zelfstandige (≈ 20,5 % schatting) | − € 12.300,00 |
> | Netto belastbaar vóór forfaitkosten | € 47.700,00 |
> | Forfaitair kostenforfait 3 % | € 1.431,00 |
> | → begrensd op plafond (niet-geïndexeerd € 1.555,50) | − € 1.431,00 |
> | **Netto beroepsinkomen** | **€ 46.269,00** |
>
> Aangifte: code 1401-54. Hier kunnen werkelijke kosten gunstig zijn (kantooronkosten + autokosten + interest art. 52-11°).
>
> Boeking bezoldiging bedrijfsleider in vennootschap (maandelijks bruto € 5.000):
>
> | Rekening | Omschrijving | Debet | Credit |
> |---|---|---|---|
> | 618 | Bezoldigingen bestuurders, zaakvoerders, beherende vennoten | 5.000 | |
> | | aan 4530 Bedrijfsvoorheffing | | (variabel) |
> | | aan 416/489 R/C zaakvoerder | | (saldo) |
>
> <small>🔗 WIB92 — art. 30-2°, 32, 51-2° — _wettekst_ · aangifte-PB-2025-bezoldigingen — vak XVI code 1401 — _aangifte_</small>

> [!example]- Vrij beroep — baten arts € 80.000, forfait-cascade
> _Arts in eigen praktijk (niet in vennootschap). Aangifte vak XVIII PB._
>
> **Berekening:**
>
> Baten-forfait dégressief (art. 51-4°, niet-geïndexeerd):
>
> | Schijf | % | Bedrag | Forfait |
> |---|---|---|---|
> | Eerste € 3.750 | 28,7 % | 3.750 | 1.076,25 |
> | 3.750-7.450 | 10 % | 3.700 | 370,00 |
> | 7.450-12.400 | 5 % | 4.950 | 247,50 |
> | > 12.400 | 3 % | 67.600 | 2.028,00 |
> | Som forfait (theoretisch) | | | 3.721,75 |
> | → begrensd op plafond € 2.592,50 (niet-geïndexeerd) | | | **2.592,50** |
>
> Netto beroepsinkomen = € 80.000 − € 2.592,50 = € 77.407,50. In de praktijk claimt arts werkelijke kosten (assistente, huur kabinet, IT) ver boven dat plafond.
>
> <small>🔗 WIB92 — art. 51-4° — _wettekst_</small>

## Valkuilen

> [!warning]- Bezoldiging meewerkende echtgenoot ≠ huwelijksquotient
> **Verkeerde assumptie**: Beide regimes 'verschuiven' inkomen van één naar andere echtgenoot, dus ze zijn varianten van hetzelfde mechanisme.
>
> **Kernpunt**: Meewerkende echtgenoot (art. 30-3°/33) vereist effectieve meewerk-activiteit + eigen sociale-zekerheids-statuut (maxistatuut). Huwelijksquotient (art. 87) is automatische toerekening (30 %, plafond ± € 6.700 niet-geïndexeerd) bij grote inkomensongelijkheid zonder dat de andere echtgenoot meewerkt. Beide kunnen niet samen toegepast worden.
>
> <small>🔗 WIB92 — art. 33, 87 — _wettekst_</small>

> [!warning]- Forfaitair plafond wordt vaak niet bereikt — werkelijke kosten kunnen gunstig zijn
> **Verkeerde assumptie**: Het forfait (30 % werknemers / 3 % bedrijfsleiders) is altijd zo gunstig dat werkelijke kosten geen meerwaarde geven.
>
> **Kernpunt**: Bij werknemers met lange woon-werk-trajecten of een eigen werkkring zijn werkelijke kosten (autokosten 0,15 €/km woon-werk + werkkamer + IT) typisch hoger dan het plafond. Bij bedrijfsleiders is het plafond € 1.555,50 (niet-geïndexeerd) bijna altijd te laag → werkelijke kosten zijn de norm.
>
> <small>🔗 WIB92 — art. 49, 51 — _wettekst_</small>

## Accountant-perspectieven

### Stagiair die de PB-aangifte van een cliënt opmaakt

_Per inkomensspecies komt de informatie van een andere fiche en gaat ze in een ander aangiftevak. De stagiair moet vooraf de juiste species identificeren._

#### 💰 Fiscaal adviseur

##### 👣 Species-classificatie vóór aangifte

**Substantie**: (1) Identificeer juridisch statuut: arbeidsovereenkomst → werknemer (vak IV); mandaat/leiding zonder arbeidsovereenkomst → bedrijfsleider (vak XVI); zelfstandige handelaar/nijveraar → winst (vak XVII); vrij beroep → baten (vak XVIII); pensioen/uitkering → vak V. (2) Verzamel fiches 281.10/281.20/281.50/281.11. (3) Match fiche-codes op aangifte-codes. (4) Beslis forfait of werkelijke kosten op basis van fiche + werkelijke uitgaven cliënt.

<small>🔗 WIB92 — art. 23, 30 — _wettekst_ · aangifte-PB-2025-bezoldigingen — _aangifte_</small>

## Verder lezen (scope-out)

- → Werknemersbezoldiging detail (loon · vakantiegeld · eindejaarspremie · opzegvergoeding) → [[werknemersbezoldiging]] _(moet-verwijzen)_
- → Bedrijfsleidersbezoldiging detail (45.000-EUR-regel · bezoldigingstheorie) → [[bedrijfsleidersbezoldiging]] _(moet-verwijzen)_
- → Winst/baten zelfstandige → [[winst-baten-zelfstandige]] _(moet-verwijzen)_
- → Beroepskosten aftrekbaarheid (forfait vs werkelijk) → [[beroepskosten]] _(moet-verwijzen)_
- → Stopzettingsmeerwaarde bij cessatie → [[stopzettingsmeerwaarde]] _(moet-verwijzen)_
- → Voordelen-alle-aard (filter-overzicht) → [[voordelen-alle-aard]] _(moet-verwijzen)_

## Relaties

### `valt_onder`
- [[personenbelasting]]
### `bevat`
- [[werknemersbezoldiging]]
- [[bedrijfsleidersbezoldiging]]
- [[winst-baten-zelfstandige]]
- [[voordelen-alle-aard]]
### `vereist`
- [[beroepskosten]]
### `triggert`
- [[bedrijfsvoorheffing]]
