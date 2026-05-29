---
title: "Aanslagbiljet personenbelasting"
concept_type: "procedure"
schema_version: "2.2"
status: "concept"
categorieen:
  - regeling
  - gebeurtenis
ankers:
  - 2.2.IV
  - 2.2.taak.2
  - 2.2.taak.4
tags:
  - concept
  - schema-2.2
  - type-procedure
  - cat-regeling
  - cat-gebeurtenis
  - status-concept
gegenereerd_uit: "data/concepten/records/aanslagbiljet-pb.json"
---

_Procedure_ · ook: avertissement-extrait de rôle IPP · AB PB

## Definitie

Het aanslagbiljet personenbelasting (Frans: 'avertissement-extrait de rôle') is het officiële document dat de FOD Financiën aan de belastingplichtige verzendt na inkohiering van de aanslag. Het bevat: de berekende belasting per AJ, de inkohieringsgegevens (kohiernummer, datum), de verrekening van voorheffingen en voorafbetalingen, het uiteindelijk saldo (te betalen of terug te krijgen), de betaaltermijn van twee maanden, en de wettelijke vermelding van de bezwaartermijn. Het aanslagbiljet is geen op zich titel voor uitvoering — die rol heeft het kohier (art. 297-298 WIB92) — maar wel het instrument waarmee de aanslag aan de belastingplichtige ter kennis wordt gebracht.

<small>📖 WIB92 — art. 298 — _wettekst_ · WIB92 — art. 304 §2 — _wettekst_ · WIB92 — art. 353 — _wettekst_</small>

## Substantie

Het aanslagbiljet sluit de fiscale jaar-cyclus voor de belastingplichtige: na aangifte → verwerking door fiscus → berekening → inkohiering → verzending aanslagbiljet. Praktisch heeft het 4 functies: (1) **informatieve functie** — de belastingplichtige krijgt overzicht van de berekening met alle componenten (belastbaar inkomen per categorie, schijven-toepassing, verminderingen, opcentiemen, voorheffingen-verrekening); (2) **vervaltermijn-start** — verzendingsdatum start de bezwaartermijn (1 jaar, art. 371) en de betaaltermijn (2 maanden, art. 304 §2); (3) **executoriale werking** — bij niet-betaling kan de fiscus dwangbevel uitvaardigen op basis van het onderliggende kohier; (4) **fiscaal bewijsstuk** voor latere referenties (kredietaanvraag, regularisatie, kwijtschelding). Het wordt verzonden per post (klassiek) of via eBox (digitaal, voor wie eBox geactiveerd heeft).

<small>🔗 WIB92 — art. 298 — _wettekst_ · WIB92 — art. 304 §2 — _wettekst_ · WIB92 — art. 371 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Rationale

De ratio legis van het aanslagbiljet is rechtsbescherming + transparantie: de belastingplichtige krijgt zwart-op-wit hoe de fiscus zijn aangifte heeft verwerkt en welke schuld is gevestigd. Dit activeert het recht op bezwaar (art. 366 WIB92 — directeur-administratie) — zonder formele kennisgeving zou de bezwaartermijn niet eerlijk kunnen lopen. De inkohiering zelf (art. 298) is de juridische act die de schuld doet ontstaan en uitvoerbaar maakt; het aanslagbiljet maakt die act zichtbaar voor de belastingplichtige. De twee-maanden-betaaltermijn (art. 304 §2) geeft tijd voor controle + eventuele financiering, terwijl de fiscus toch op kort termijn liquiditeit krijgt.

<small>🔗 WIB92 — art. 298 — _wettekst_ · WIB92 — art. 304 — _wettekst_ · WIB92 — art. 366 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Gebruikscontext

**Status**: `in-voege` · basis: WIB92 art. 297-310 (inkohiering + kennisgeving) + art. 304 §2 (betaaltermijn) + art. 366-377 (bezwaar) + art. 410-419 (invordering)

Stabiel kader. Wijzigingen recent: digitalisatie via eBox (2018+) voor automatische digitale aflevering aanslagbiljet wanneer de belastingplichtige hiervoor opteerde.

**✅ Voor**
- 📖 Elke PB-belastingplichtige nadat de fiscus zijn aangifte heeft verwerkt en de aanslag heeft gevestigd via inkohiering. Ook bij ambtshalve aanslag (niet-aangifte) ontvangt de belastingplichtige een aanslagbiljet — typisch dan met belastingverhoging.

**▶️ Trigger start**
- 📖 Inkohiering van de aanslag (art. 298 WIB92): de directeur (of zijn gedelegeerde) ondertekent het kohier, dat een lijst is van alle belastingschulden gevestigd voor een gegeven aanslagjaar. Vanaf dat ogenblik bestaat de schuld in rechte. De FOD verzendt dan het aanslagbiljet aan de belastingplichtige — typisch enkele weken na inkohiering.

**⏹ Trigger einde**
- 📖 Aanslagbiljet 'sluit' bij effectieve betaling van het saldo of bij terugbetaling van het terug-te-krijgen-bedrag door de FOD. Bij niet-betaling binnen 2 maanden: nalatigheidsinteresten (art. 414 WIB92, ECB-referentievoet + 4 % marge) + mogelijke dwangbevel-procedure. Bij bezwaar: aanslagbiljet blijft uitvoerbaar (geen schorsende werking), tenzij directeur opschorting verleent (art. 410 §2).

**👍 Voordeel**
- 🔗 Voor de belastingplichtige: het aanslagbiljet is een betrouwbaar bewijsstuk van de definitief vastgestelde belasting voor een AJ. Banken (kredietaanvraag), notarissen (vermogensoverzicht), pensioenfondsen (inkomenscontrole) erkennen het aanslagbiljet als gestandaardiseerd document.

**⚠️ Risico**
- 📖 Niet-betaling binnen 2 maanden = nalatigheidsinteresten + dwangbevel-procedure (deurwaarder kan optreden). De fiscus heeft sterke invorderingsbevoegdheden: beslag op loon, op bankrekening, op onroerend goed (hypotheek-inschrijving). Een aanslag-schuld die langer onbetaald blijft escaleert snel.
- 📖 Bezwaartermijn (1 jaar vanaf 3de werkdag volgend op verzending) is een vervaltermijn — strikt. Bij missen van de termijn: bezwaar onontvankelijk, aanslag definitief, enkel ambtshalve ontheffing voor specifieke gronden mogelijk (art. 376 — beperkt). Stagiair moet de termijn altijd onmiddellijk noteren bij ontvangst.

## Bouwstenen

### ⚙️ Inkohiering (enrôlement)

De inkohiering is de juridische act waarbij de fiscus de berekende belasting opneemt in het kohier — een door de bevoegde directeur ondertekende lijst van alle belastingschulden voor een AJ (art. 298 WIB92). Het kohier is een uitvoerbare titel: het maakt de belastingschuld in rechte gevestigd en uitvoerbaar (de fiscus kan zonder verdere gerechtelijke tussenkomst dwangmaatregelen uitvaardigen bij niet-betaling). Inkohiering moet gebeuren binnen wettelijke termijnen (art. 359 — uiterlijk 30 juni van het jaar volgend op het AJ, met verlengingen tot 30 juni AJ+3 bij eerlijke aangifte, AJ+5 bij niet-aangifte, AJ+7 bij fraude).

<small>📖 WIB92 — art. 298 — _wettekst_ · WIB92 — art. 359 — _wettekst_</small>

### ⚙️ Inhoud van het aanslagbiljet

**Substantie**: Het aanslagbiljet bevat verplicht: (a) identificatie belastingplichtige (naam, nationaal nummer, adres); (b) aanslagjaar + kohierjaar + artikelnummer (kohier-identifier); (c) datum van inkohiering + datum van verzending; (d) detail van de berekening per inkomenscategorie (onroerend, roerend, beroeps, divers — bedragen netto per categorie); (e) belastbaar inkomen + schijven-toepassing (art. 130); (f) verminderingen (belastingvrije som, kinderen, giften, pensioensparen, dienstencheques); (g) federale belasting Staat na vermindering; (h) aanvullende gemeentebelasting (% × federale Staat); (i) totaal verschuldigd; (j) verrekening: bedrijfsvoorheffing, voorafbetalingen, roerende voorheffing, dienstcheque-attesten; (k) saldo te betalen of terug te krijgen; (l) betaal-instructies + uiterste datum; (m) wettelijke vermelding bezwaartermijn (1 jaar) + adres directeur.

<small>📖 WIB92 — art. 304 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### 📜 Betaaltermijn: 2 maanden vanaf verzending

De verschuldigde belasting moet betaald worden binnen twee maanden vanaf de datum van verzending van het aanslagbiljet (art. 304 §2 WIB92). Bij overschrijding: nalatigheidsinteresten verschuldigd vanaf de eerste dag na de termijn (art. 414 — ECB-referentievoet aangevuld met 4 % marge; bv. ~7-9 % per jaar in recente jaren). Betalingsfaciliteit kan aangevraagd worden bij ontvanger (art. 413/1) — spreiding tot 12 maanden vaak toegekend bij bewezen tijdelijke moeilijkheden.

<small>📖 WIB92 — art. 304 §2 — _wettekst_ · WIB92 — art. 414 — _wettekst_ · WIB92 — art. 413/1 — _wettekst_</small>

### ⚙️ Terugbetaling bij teruggave-saldo

**Substantie**: Wanneer voorheffingen + voorafbetalingen > totaal verschuldigde belasting: saldo wordt teruggestort door FOD Financiën op de bankrekening die de belastingplichtige in vak I van zijn aangifte heeft opgegeven (of in MyMinfin geregistreerd). Standaardtermijn: 2 maanden vanaf datum aanslagbiljet (parallel aan betaaltermijn — maar voor terug-richting). FOD betaalt geen interest op terugbetalingen kleiner dan een wettelijk plafond of bij te late aangifte. Bij andere openstaande fiscale schulden: compensatie (art. 334 — terugbetaling wordt eerst aangerekend op openstaande aanslagen).

<small>📖 WIB92 — art. 304 — _wettekst_ · WIB92 — art. 334 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### ↪️ Ambtshalve aanslag + rechtzettings-bericht

Wanneer de fiscus afwijkt van de ingediende aangifte (correctie wegens fout, verzwegen inkomen, niet-aftrekbare uitgave), wordt EERST een rechtzettings-bericht (art. 346 WIB92) gestuurd. De belastingplichtige heeft 1 maand om te reageren met opmerkingen. Pas DAN wordt de gewijzigde aanslag ingekohierd en het aanslagbiljet verzonden. Bij niet-aangifte: ambtshalve aanslag (art. 351) op basis van schatting + belastingverhoging 10-200 % (art. 444). Het ambtshalve aanslagbiljet vermeldt expliciet dat het op deze grondslag is gevestigd — relevant voor verdere bezwaarmotivering.

<small>📖 WIB92 — art. 346 — _wettekst_ · WIB92 — art. 351 — _wettekst_ · WIB92 — art. 444 — _wettekst_</small>

### 📜 Bezwaartermijn: 1 jaar vanaf 3de werkdag na verzending

De bezwaartermijn is één jaar te rekenen vanaf de 3de werkdag volgend op de verzending van het aanslagbiljet (art. 371 WIB92). Bezwaar moet schriftelijk ingediend worden bij de directeur van de bevoegde controle (of via MyMinfin online); gemotiveerd; eenvoudige aangetekende brief volstaat (post-zegel datum = datum bezwaar). Niet-schorsende werking: betaaltermijn 2 maanden loopt door — de belastingplichtige moet betalen om interesten te vermijden, of expliciet opschorting aanvragen (art. 410 §2).

<small>📖 WIB92 — art. 366 — _wettekst_ · WIB92 — art. 371 — _wettekst_ · WIB92 — art. 410 — _wettekst_</small>

## Voorbeelden

> [!example]- Typisch aanslagbiljet werknemer — saldo terug te krijgen
> _Dhr. Vermeulen, alleenstaande werknemer, brutoloon 42.000 EUR (BV ingehouden 8.500 EUR). Aangifte ingediend juli AJ 2026. Aanslagbiljet ontvangen begin november AJ 2026._
>
> | Rubriek | Bedrag (EUR) |
>
> | --- | --- |
>
> | Beroepsinkomen netto (na forfait) | 36.480 |
>
> | Belastbaar inkomen | 36.480 |
>
> | Belasting volgens schijven art. 130 | 8.900 |
>
> | − Belastingvrije som vermindering | −2.660 |
>
> | Federale basisbelasting na vermindering | 6.240 |
>
> | + Aanvullende gemeentebelasting 7 % | +437 |
>
> | = Totaal verschuldigd | 6.677 |
>
> | − Bedrijfsvoorheffing | −8.500 |
>
> | = Saldo terug te krijgen | 1.823 |
>
> Aanslagbiljet-flow:
>
> ```mermaid
> flowchart TD
>   A[31 dec 2025 boekjaar einde IJ] --> B[15 jul 2026 aangifte ingediend via TaxOnWeb]
>   B --> C[Augustus-oktober 2026 fiscus verwerkt + berekent]
>   C --> D[Inkohiering oktober 2026 art. 298]
>   D --> E[Verzending aanslagbiljet begin november 2026 art. 304]
>   E --> F{Saldo?}
>   F -->|Terugbetaling 1823 EUR| G[FOD stort binnen 2 maanden]
>   F -->|Geen actie| H[Bezwaartermijn loopt 1 jaar art. 371]
>   E --> I[Aanslag wordt definitief na 1 jaar zonder bezwaar]
> ```
>
> Dhr. Vermeulen krijgt 1.823 EUR teruggestort omdat de bedrijfsvoorheffing aan bron meer was dan zijn werkelijke aanslag. Hij heeft 1 jaar tijd om bezwaar te maken indien hij meent dat de berekening fout is (bv. verminderingen niet correct toegepast).
>
> <small>🔗 WIB92 — art. 304 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

> [!example]- Zelfstandige met bijbetaling — termijn + facilitatie
> _Mevr. Janssens, zelfstandige consultant. Aangifte ingediend oktober AJ 2026 (mandataris-termijn). Geen voorafbetalingen verricht. Berekende PB 18.500 EUR, gemeentebelasting 1.300 EUR, belastingvermeerdering wegens geen VA: 1.480 EUR. Geen bedrijfsvoorheffing (zelfstandige). Aanslagbiljet ontvangen januari AJ+1._
>
> **Berekening:**
>
> - Stap 1 — totaal verschuldigd op aanslagbiljet: 18.500 + 1.300 + 1.480 = 21.280 EUR
> - Stap 2 — verrekening voorheffingen: 0 EUR (zelfstandige, geen BV) + voorafbetalingen 0 EUR = 0
> - Stap 3 — saldo bij te betalen: 21.280 EUR
> - Stap 4 — verzending aanslagbiljet 15 januari AJ+1 → betaaltermijn 2 maanden = uiterste betaaldatum 15 maart AJ+1
> - Stap 5 — Mevr. Janssens kan niet meteen 21.280 EUR betalen → aanvraagt betalingsfaciliteit (art. 413/1) bij ontvanger via MyMinfin: 'gespreid 6 maandtermijnen'
> - Stap 6 — ontvanger keurt goed: 6 × 3.547 EUR (gespreid maart-augustus AJ+1)
> - Stap 7 — nalatigheidsinteresten lopen WEL door op het saldo (art. 414) — orde van grootte 8 %/jaar
>
> → **Resultaat**: Bijbetaling van 21.280 EUR met 1.480 EUR vermeerdering wegens geen VA — een typische 'wake-up call' voor zelfstandigen die geen voorafbetalingen plannen. Volgend jaar adviseert de accountant zeker VA-planning om vermeerdering te vermijden.
>
> <small>🔗 WIB92 — art. 304 §2 — _wettekst_ · WIB92 — art. 157 — _wettekst_ · WIB92 — art. 414 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

> [!example]- Ambtshalve correctie + rechtzettings-bericht
> _Dhr. Peeters dient aangifte in waarin hij vergeet een buitenlandse pensioen-uitkering van 4.500 EUR (Frankrijk) aan te geven. Fiscus detecteert via CRS-uitwisseling met Franse fiscus. Stuurt rechtzettings-bericht in oktober AJ 2026._
>
> Procedure-flow rechtzetting:
>
> ```mermaid
> flowchart TD
>   A[Aangifte ingediend juli AJ 2026 zonder NL-pensioen] --> B[Fiscus detecteert via CRS]
>   B --> C[Oktober 2026 rechtzettings-bericht art. 346 verzonden]
>   C --> D{Reactie binnen 1 maand?}
>   D -->|Akkoord met correctie| E[Aanslag op gecorrigeerde basis + verhoging 10 percent vergetelijkheid]
>   D -->|Geen reactie| E
>   D -->|Niet akkoord met argumenten| F[Discussie met controleur]
>   F --> G[Beslissing fiscus over correctie]
>   E --> H[Inkohiering met gecorrigeerde grondslag]
>   H --> I[Aanslagbiljet met verhoging]
>   I --> J{Bezwaartermijn 1 jaar}
>   J -->|Bezwaar mogelijk| K[Directeur beslist art. 366]
>   J -->|Geen bezwaar| L[Aanslag definitief]
> ```
>
> Dhr. Peeters reageert in november: erkent vergetelheid, vraagt om gematigde verhoging. Aanslagbiljet komt eind december: gecorrigeerde belasting + verhoging 10 % (eerste overtreding, geen opzet). Betaaltermijn 2 maanden. Bezwaartermijn 1 jaar — geen bezwaar mogelijk hier want feit erkend.
>
> <small>🔗 WIB92 — art. 346 — _wettekst_ · WIB92 — art. 444 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Valkuilen

> [!warning]- Bezwaartermijn vanaf 'datum aanslagbiljet' verkeerd berekenen
> **Verkeerde assumptie**: Bezwaartermijn = 1 jaar vanaf de datum die op het aanslagbiljet staat als 'datum aanslagbiljet'.
>
> **Kernpunt**: De wettelijke termijn (art. 371 WIB92) is 1 jaar vanaf de 3DE WERKDAG VOLGEND OP DE VERZENDING. Dat is technisch niet altijd hetzelfde als de 'datum aanslagbiljet' (= datum inkohiering). Vraag bij twijfel het 'datum verzending' op via MyMinfin of via vraag aan ontvanger. Bij digitale verzending via eBox: datum eBox-aflevering geldt.
>
> <small>📖 WIB92 — art. 371 — _wettekst_</small>

> [!warning]- Aanslagbiljet zien als 'voorstel'
> **Verkeerde assumptie**: Het aanslagbiljet is een voorstel waar de belastingplichtige tegen kan inbrengen, vergelijkbaar met een offerte.
>
> **Kernpunt**: Het aanslagbiljet maakt een DEFINITIEVE belastingschuld zichtbaar (al gevestigd door inkohiering). Niet-schorsende werking van bezwaar: zelfs als de belastingplichtige bezwaar indient, blijft de schuld uitvoerbaar — moet betaald worden binnen 2 maanden om nalatigheidsinteresten te vermijden. Pas na succesvol bezwaar wordt het teveel betaald terugbetaald.
>
> <small>📖 WIB92 — art. 410 — _wettekst_ · WIB92 — art. 304 §2 — _wettekst_</small>

> [!warning]- Termijn 30 juni AJ+1 verwarren met aanslagbiljet-termijn
> **Verkeerde assumptie**: Aanslagbiljet moet uiterlijk 30 juni AJ+1 worden VERZONDEN.
>
> **Kernpunt**: Art. 359 WIB92 zegt dat de INKOHIERING uiterlijk 30 juni AJ+1 moet plaatsvinden (gewone aanslagtermijn — verlengingen mogelijk). Het AANSLAGBILJET wordt typisch enkele weken na inkohiering verzonden — kan dus ook in juli-augustus AJ+1 nog landen. Bij verlengde termijnen (AJ+3, AJ+5, AJ+7 — fraude): aanslagbiljet kan veel later komen.
>
> <small>📖 WIB92 — art. 359 — _wettekst_</small>

> [!warning]- Terugbetaling = automatisch op dezelfde rekening
> **Verkeerde assumptie**: FOD stort terug op de bankrekening waarop de belastingplichtige zijn loon ontvangt, of op de meest recent gebruikte rekening.
>
> **Kernpunt**: De terugbetaling gaat naar de bankrekening die EXPLICIET in vak I van de aangifte is opgegeven (of geregistreerd in MyMinfin). Wijzigingen in rekening tussen aangifte en aanslag worden NIET automatisch opgepikt. Bij verkeerd nummer: terugbetaling 'wacht' op aanslagbiljet-rekening, kan via MyMinfin geactualiseerd worden, maar elke wijziging vraagt actie.
>
> <small>🔗 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Accountant-perspectieven

### Eigen kantoor — aanslagbiljetten opvolgen voor cliënten

_De accountant die voor cliënten de ontvangen aanslagbiljetten controleert, betaling coordineert, en bezwaartermijnen bewaakt._

#### 💰 Fiscaal adviseur

##### 👣 Controle aanslagbiljet ↔ aangifte

Bij ontvangst van het aanslagbiljet (per post of via MyMinfin volmacht): systematisch vergelijken met de ingediende aangifte + de werkpapieren van de aangifte-voorbereiding. Controleer per rubriek: (a) belastbaar inkomen per categorie correct overgenomen?; (b) verminderingen (pensioensparen, giften, dienstencheques) volledig toegepast?; (c) voorheffingen volledig verrekend (BV, RV, dienstencheque-attesten)?; (d) gemeentebelasting-tarief klopt (per gemeente verschillend); (e) eventuele belastingverhoging bij correctie — gemotiveerd? Documenteer afwijkingen in dossier-notitie + beslis: aanvaarden of bezwaar voorbereiden.

<small>🔗 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

##### 👣 Bezwaartermijn bewaken (1 jaar)

Bij ontvangst van het aanslagbiljet: noteer onmiddellijk in agenda/dossier-systeem de bezwaartermijn (1 jaar + 3 werkdagen na verzending — typisch dus rond ~10-15 dagen na 'datum aanslagbiljet'). Stel reminder 30 + 60 + 90 dagen vóór de eindtermijn. Reden: bezwaargronden moeten tijdig geargumenteerd worden, eventueel met aanvullende stukken (bv. ontbrekende attesten) — laatste-minuut bezwaar is foutgevoelig. Bij twijfel: bezwaar instellen ('beschermend bezwaar') en daarna intrekken indien niet meer nodig.

<small>🔗 WIB92 — art. 371 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

#### 🧭 Adviseur

##### 🧭 Communicatie naar cliënt — vermijd verrassingen

Cliënten zijn vaak verrast bij aanslagbiljet — vooral bij bijbetaling. Beste praktijk: na aangifte een schatting van het verwachte saldo communiceren aan cliënt (vooral bij zelfstandigen, met opmerking over vermeerdering geen VA). Bij ontvangst aanslagbiljet: korte note 'controle uitgevoerd, akkoord, x EUR te betalen vóór dd-mm of x EUR terug binnen 2 maanden'. Bij correctie of verhoging: bel cliënt direct + leg uit waarom + plan bezwaar of aanvaarden. Een cliënt die geïnformeerd is, gaat geen paniek-mailen.

<small>🔗 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Verder lezen (scope-out)

- → Belastingberekening als voorafgaande stap → [[belastingberekening-pb]] _(moet-verwijzen)_
- → Generieke aanslag-cyclus (fiscale-procedure) → [[aanslag-cyclus]] _(moet-verwijzen)_
- → Bezwaarprocedure (administratief verhaal) → [[bezwaarprocedure]] _(moet-verwijzen)_
- → Invorderingsprocedure bij niet-betaling → [[invorderingsprocedure]] _(moet-verwijzen)_
- → Aangifte PB (input van procedure) → [[aangifte-pb]] _(moet-verwijzen)_

## Relaties

### `valt_onder`
- [[personenbelasting]]
### `vereist`
- [[belastingberekening-pb]] — Berekening moet voltooid zijn vooraleer kan worden ingekohierd + aanslagbiljet verzonden.
- [[aangifte-pb]] — Aangifte (of ambtshalve aanslag bij niet-aangifte) is procesmatige voorwaarde.
### `triggert`
- [[bezwaarprocedure]] — Verzending aanslagbiljet start de bezwaartermijn van 1 jaar (art. 371 WIB92).
- [[invorderingsprocedure]] — Bij niet-betaling binnen 2 maanden: invorderingsprocedure (nalatigheidsinteresten, dwangbevel, beslag).
### `vergelijkbaar_met`
- [[aanslag-cyclus]]
    - **Gelijkenissen**:
        - Beide concepten beschrijven de fiscale aanslag-flow
        - Beide bevatten inkohiering + kennisgeving + bezwaar-fase
    - **Verschillen**:
        - Aanslagbiljet PB is specifiek voor de natuurlijke persoon (PB-vorm); aanslag-cyclus is generiek over alle inkomstenbelastingen
        - Aanslagbiljet PB heeft eigenheden zoals gemeentebelasting-opslag + VVA-aanslag-flow; aanslag-cyclus dekt PB + VenB + RPB + BNI
    - ⚠️ **Verwarringsrisico**: Aanslagbiljet PB is het concrete document; aanslag-cyclus is het abstract proces. Stagiair moet weten welke van de twee in een examenvraag wordt bedoeld.
