---
title: "Factuur (BTW)"
concept_type: "instrument"
schema_version: "2.2"
status: "concept"
categorieen:
  - entiteit
  - regeling
ankers:
  - 2.4.I
tags:
  - concept
  - schema-2.2
  - type-instrument
  - cat-entiteit
  - cat-regeling
  - status-concept
gegenereerd_uit: "data/concepten/records/factuur-btw.json"
---

_Instrument_ · ook: BTW-factuur · verkoopfactuur · e-factuur

## Definitie

De BTW-factuur is het officiële document waarop de leverancier de aan zijn afnemer aangerekende BTW vermeldt en dat als bewijsstuk dient voor het uitoefenen van het aftrekrecht door de afnemer. Sinds 1 januari 2026 is voor B2B-handelingen tussen Belgische belastingplichtigen de gestructureerde elektronische factuur (e-factuur volgens Peppol BIS-norm + EN 16931) de verplichte standaardvorm — de papieren factuur wordt uitzondering.

<small>📖 WBTW — art. 53 §2bis — _wettekst_ · WBTW — art. 1, 2° — _wettekst_</small>

## Substantie

Drie functies tegelijk: (1) commercieel betalingsverzoek; (2) BTW-bewijsstuk — leverancier verwerkt rooster 03/54, afnemer rooster 59; (3) fiscaal bewijs van de transactie voor inkomstenbelasting + boekhoudplicht. Door deze drievoudige functie zijn de inhoudelijke eisen strikt: ontbreekt een verplichte vermelding, dan kan dit gevolgen hebben voor BTW-aftrek bij de ontvanger of beboete worden bij controle. De e-factuur (vanaf 2026) zorgt voor automatische verwerking en realtime cross-check tussen aangiftes.

<small>🔗 WBTW — art. 53 — _wettekst_ · KB nr. 1 — art. 5 — _kb_ · claude-sonnet-4-5 — _ai_model_ — (2026-05-28)</small>

## Rationale

De factuur is de hoeksteen van het self-assessment BTW-systeem: zonder dit document kan de fiscus de keten verkoop ↔ aankoop niet cross-checken. De e-invoicing-hervorming is een Europese trend (Italië voorop, België volgt 2026) om carrousel-fraude te bestrijden door realtime data-stromen naar de belastingadministratie. Tegelijk vermindert het de administratieve last voor bedrijven (automatische verwerking).

<small>🔗 Richtlijn 2006/112/EG — art. 233 + art. 217-240 — _richtlijn_ · claude-sonnet-4-5 — _ai_model_ — (2026-05-28)</small>

## Gebruikscontext

**Status**: `in-voege` · sinds **2026-01-01** · basis: WBTW art. 53 §2bis (W 06-02-2024) — verplichte gestructureerde e-facturatie B2B

Verplichte e-invoicing voor B2B-handelingen tussen Belgische BTW-belastingplichtigen sinds 01-01-2026 (W 06-02-2024). Belangrijkste uitzonderingen: belastingplichtige onderworpen aan kleine-ondernemingsregeling art. 56 (vrijstellingsregeling jaaromzet ≤ 25.000 EUR) en gefailleerde belastingplichtige. Voor B2C blijft de keuze tussen papier en elektronisch (mits aanvaarding klant).

**▶️ Trigger start**
- 📖 Factuurplicht ontstaat bij elke levering van goederen of dienst aan een belastingplichtige medecontractant (B2B) en bij sommige handelingen aan particulieren (B2C — bv. nieuw vervoermiddel, vastgoed nieuwbouw, leveringen op afstand).

## Bouwstenen

### 📏 Termijn factuur uitreiken

De factuur moet uitgereikt worden uiterlijk de 15de dag van de maand volgend op de maand waarin de BTW opeisbaar is geworden (= maand van levering of dienst, of maand van betaling bij vooruitbetaling). Voor intracommunautaire leveringen: idem (art. 53 §3).

<small>📖 WBTW — art. 53 §2 + §3 — _wettekst_</small>

### 📜 Verplichte vermeldingen (KB nr. 1 art. 5)

Lijst verplichte vermeldingen op elke BTW-factuur: (1) datum uitreiking; (2) opeenvolgend factuurnummer (eigen reeks); (3) naam/adres/BTW-nummer leverancier; (4) naam/adres/BTW-nummer afnemer (bij B2B); (5) datum belastbaar feit indien verschillend van factuurdatum; (6) beschrijving en hoeveelheid van goederen of voorwerp van de diensten; (7) eenheidsprijs + kortingen; (8) maatstaf van heffing per tarief; (9) BTW-tarief per categorie; (10) totaal BTW; (11) totaal incl. BTW; (12) bij verlegging of vrijstelling: vermelding van het toepasselijke regime ('BTW verlegd', 'vrijgesteld art. 39bis', ...).

<small>📖 KB nr. 1 — art. 5 §1 1°-7° — _kb_</small>

### ⚙️ Gestructureerde e-factuur — Peppol BIS / EN 16931

Vanaf 2026: B2B-facturen tussen Belgische belastingplichtigen moeten gestructureerd elektronisch worden uitgereikt en ontvangen via het Peppol-netwerk (Belgisch standaardkanaal). Formaat: UBL/Peppol BIS Billing 3.0, conform Europese normen EN 16931-1 (semantiek) + CEN/TS 16931-2 (syntaxis). Een PDF op e-mail = GEEN gestructureerde e-factuur (geen machinaal verwerkbaar). Software-pakketten verzorgen aansluiting via Peppol-access points.

<small>📖 WBTW — art. 53 §2bis — _wettekst_</small>

### ⚙️ Creditnota — correctie van een factuur

Een creditnota (verbeteringsstuk) wijzigt of annuleert een oorspronkelijke factuur: bij retour van goederen, prijsvermindering achteraf, factuur-aanvulling, fout. Vereisten: zelfde formaat als de oorspronkelijke factuur (sinds 2026 ook e-factuur als de oorspronkelijke dat was), expliciete verwijzing naar de oorspronkelijke factuur, datum + nummer, en omkering van bedragen (negatieve bedragen of credit-aanduiding). BTW-effect: bij de leverancier rooster 48 (creditnota op uitgaande); bij de afnemer rooster 64 (creditnota op aankoop) — beide doen de oorspronkelijke aftrek of belastingschuld omkeren.

<small>📖 WBTW — art. 53 §2 lid 3 ('document dat wijzigingen aanbrengt geldt als factuur') — _wettekst_</small>

### 📜 Bewaarplicht facturen

Belastingplichtigen moeten alle uitgaande en inkomende facturen bewaren gedurende 10 jaar (algemene fiscale bewaartermijn art. 60 WBTW + art. 315 WIB92). Elektronische facturen mogen elektronisch bewaard, mits authenticiteit van de oorsprong, integriteit van de inhoud en leesbaarheid gewaarborgd (art. 233 Richtlijn 2006/112). Bij controle moet de belastingplichtige de facturen onmiddellijk kunnen voorleggen.

<small>📖 WBTW — art. 60 — _wettekst_ · Richtlijn 2006/112/EG — art. 233 + art. 244-247 — _richtlijn_</small>

## Voorbeelden

> [!example]- Standaard B2B-factuur 21 %
> _Aurelia Holding NV (BTW BE0123.456.789) factureert aan Zelena Bio NV (BTW BE0987.654.321) op 12 maart 2026: 5 software-licenties à 1.000 EUR netto = 5.000 EUR._
>
> **📋 Factuur 2026-0034 — verplichte vermeldingen**
>
> - Datum uitreiking: 12 maart 2026
>
> - Factuurnummer: 2026-0034
>
> - Leverancier: Aurelia Holding NV — BTW BE0123.456.789 — Adres: ...
>
> - Afnemer: Zelena Bio NV — BTW BE0987.654.321 — Adres: ...
>
> - Datum belastbaar feit: 10 maart 2026 (leveringsdatum)
>
> - Beschrijving: 5 × Softwarelicentie ABC, jaarabonnement
>
> - Eenheidsprijs: 1.000 EUR — Hoeveelheid: 5
>
> - Maatstaf van heffing 21 %: 5.000 EUR
>
> - BTW 21 %: 1.050 EUR
>
> - Totaal te betalen: 6.050 EUR
>
> - Vermelding regime: standaardregime BTW
>
> <small>📖 KB nr. 1 — art. 5 §1 — _kb_</small>

> [!example]- Creditnota wegens retour
> _Zelena Bio NV retourneert 2 van de 5 licenties uit voorbeeld hierboven. Aurelia maakt creditnota._
>
> **📋 Creditnota 2026-CN-005**
>
> - Datum uitreiking: 25 maart 2026
>
> - Nummer: 2026-CN-005
>
> - Verwijzing naar oorspronkelijke factuur: 2026-0034 dd 12-03-2026
>
> - Reden: retour 2 licenties
>
> - Maatstaf van heffing: -2.000 EUR (21 %)
>
> - BTW 21 %: -420 EUR
>
> - Totaal: -2.420 EUR
>
> **📒 Boeking bij Aurelia (leverancier)**
>
> | Rekening | Debet | Credit | Omschrijving |
> | --- | --- | --- | --- |
> | 451 — Te betalen BTW | 420 |  | Vermindering verschuldigde BTW (rooster 48) |
> | 70 — Omzet | 2.000 |  | Vermindering omzet |
> | 400 — Handelsdebiteur Zelena |  | 2.420 | Verminderde vordering |
>
> <small>🔗 WBTW — art. 53 §2 lid 3 — _wettekst_ · KB 21-10-2018 (MAR) — Klasse 4 — rekeningen 400 + 451 — _kb_ · claude-sonnet-4-5 — _ai_model_ — (2026-05-28)</small>

## Valkuilen

> [!warning]- PDF op e-mail = e-factuur
> **Verkeerde assumptie**: 'Ik stuur mijn factuur per e-mail als PDF — dat is een elektronische factuur sinds 2026.'
>
> **Kernpunt**: Sinds 2026 vereist B2B-tussen-Belgische-belastingplichtigen een GESTRUCTUREERDE e-factuur (machinaal verwerkbaar UBL/Peppol-formaat via Peppol-netwerk). Een PDF op e-mail is GEEN gestructureerde e-factuur. Boete + verlies aftrekrecht mogelijk. Software aansluiten op Peppol is nodig.
>
> <small>📖 WBTW — art. 53 §2bis — _wettekst_ · WBTW — art. 1, 2° — _wettekst_</small>

> [!warning]- Verlegging vergeten te vermelden
> **Verkeerde assumptie**: Bij IC-levering of B2B-bouwsector volstaat de factuur zonder BTW.
>
> **Kernpunt**: Bij elke verlegging moet de factuur expliciet de vermelding bevatten: 'BTW verlegd' (bij IC-levering: 'Vrijstelling art. 39bis WBTW'; bij bouwwerk in onroerende staat: 'BTW verlegd — medecontractant'). Ontbreekt de vermelding, dan riskeert de leverancier zelf de BTW te moeten betalen.
>
> <small>📖 KB nr. 1 — art. 5 §1, 7° — _kb_</small>

> [!warning]- Factuur 'corrigeren' door overschrijven of een nieuwe te maken zonder verwijzing
> **Verkeerde assumptie**: Een foute factuur kan ik gewoon weggooien en een nieuwe maken.
>
> **Kernpunt**: Een uitgereikte factuur kan enkel gewijzigd worden via een verbeteringsstuk (creditnota) dat expliciet en ondubbelzinnig verwijst naar de oorspronkelijke factuur. Een tweede factuur zonder verwijzing leidt tot dubbele BTW-verplichting voor de leverancier (art. 51 §1, 3° WBTW: 'wie BTW vermeldt op factuur, is BTW schuldig').
>
> <small>📖 WBTW — art. 53 §2 lid 3 — _wettekst_ · WBTW — art. 51 §1, 3° — _wettekst_</small>

## Accountant-perspectieven

### Kantoor adviseert cliënt over facturatie

_De accountant bij invoering en bewaking van het facturatie-proces van de cliënt._

#### 🧭 Adviseur

##### 👣 Implementatie e-invoicing 2026 — checklist

Stappen voor cliënt: (1) software-keuze met Peppol-aansluiting (gangbare pakketten: Exact, Yuki, Octopus); (2) registratie op Peppol-access point; (3) configuratie verplichte vermeldingen volgens KB nr. 1 art. 5; (4) test-runs met cliënten en leveranciers; (5) archivering-proces e-facturen (10 jaar). Begeleiding: aandachtspunt — kleine-onderneming-regeling-cliënten zijn vrijgesteld van e-invoicing maar moeten wel kunnen ontvangen.

<small>🔗 WBTW — art. 53 §2bis — _wettekst_ · claude-sonnet-4-5 — _ai_model_ — (2026-05-28)</small>

#### 📒 Boekhouder

##### 👣 Validatie ingaande facturen

Bij elke ingaande factuur: checken op verplichte vermeldingen vóór codering. Ontbrekend BTW-nummer afnemer, factuurdatum, of regime-vermelding = retour aan leverancier voor correctie. Eventuele cross-check BTW-nummer via VIES voor IC-aankopen. Bij e-factuur: automatische validatie door software maar kantoor blijft eindverantwoordelijk.

<small>🔗 KB nr. 1 — art. 5 — _kb_ · claude-sonnet-4-5 — _ai_model_ — (2026-05-28)</small>

## Verder lezen (scope-out)

- → BTW (algemeen kader) → [[btw]] _(moet-verwijzen)_
- → BTW-aftrek bij ontvanger → [[btw-aftrek]] _(moet-verwijzen)_

## Relaties

### `valt_onder`
- [[btw]]
### `vereist`
- [[btw]] — Factuur is uitvoerend instrument voor het BTW-systeem (factureren van verschuldigde BTW).
### `triggert`
- [[btw-aftrek]] — Regelmatige factuur is voorwaarde voor uitoefening van aftrekrecht bij ontvanger (KB nr. 3 art. 3).
