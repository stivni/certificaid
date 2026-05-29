---
title: "Leasing"
concept_type: "instrument"
schema_version: "2.2"
status: "concept"
categorieen:
  - regeling
ankers:
  - 3.0.IV.D
tags:
  - concept
  - schema-2.2
  - type-instrument
  - cat-regeling
  - status-concept
gegenereerd_uit: "data/concepten/records/leasing.json"
---

_Instrument_ · ook: huur-koop · leaseovereenkomst · lease

## Definitie

Leasing is een driepartijenstructuur voor de financiering van een vast actief: de leasinggever (typisch een gespecialiseerde financiele instelling) koopt het actief bij de leverancier en stelt het tegen periodieke vergoeding ter beschikking van de leasingnemer, die het in zijn beroepsactiviteit gebruikt. Het contract bestaat voor een bepaalde looptijd; aan het einde kan de leasingnemer het actief in eigendom verwerven via een koopoptie, het actief teruggeven, of het contract verlengen. Boekhoudkundig zijn er twee verwerkingen, afhankelijk van de kwalificatie: financiele leasing (on-balance bij de leasingnemer als vast actief + leasingschuld) of operationele leasing (off-balance, gewoon als huurkost in resultaat).

<small>📖 CBN-advies 2015/4 — Algemene structuur leasing — _cbn_ · CBN-advies 2021/05 — Onderscheid financiele vs operationele leasing - boekhoudkundige verwerking — _cbn_</small>

## Substantie

Economisch is leasing een vorm van actief-specifieke financiering: in plaats van het actief zelf te kopen (met eigen middelen of een banklening), 'huurt' de onderneming het volledig - met aan het einde meestal een keuze om het over te nemen. Het verschil met een huurcontract zit in de financieringsfunctie: bij een echte leasing wordt het bedrag van de huurpenningen zo berekend dat het volledige geinvesteerde kapitaal van de leasinggever wordt terugverdiend (inclusief rente). Bij een huurcontract betaalt de huurder enkel voor het gebruiksrecht. Dit onderscheid is bepalend voor de kwalificatie: zodra de huurpenningen samen het geinvesteerde kapitaal volledig wedersamenstellen, spreken we van financiele leasing (BE-GAAP). Bij IFRS 16 (sinds 2019) is dit onderscheid voor de lessee verdwenen - bijna elke lease komt op de balans.

<small>📖 CBN-advies 2015/4 — Wedersamenstelling kapitaal als kwalificatiecriterium — _cbn_ · IFRS 16 (Verordening (EU) 2023/1803) — Lessee - geen onderscheid financieel/operationeel meer — _wettekst_</small>

## Rationale

Leasing biedt een KMO drie voordelen tegelijk: (1) volledige financiering van een investering zonder eigen inbreng; (2) de leasinggever blijft juridisch eigenaar tijdens de looptijd, wat de zekerheid voor hem maximaliseert (het actief zelf is de waarborg); (3) bij operationele leasing (BE-GAAP) blijft de schuld off-balance, wat de solvabiliteitsratio's verbetert. Voor activa met snelle technologische veroudering (IT, machines) biedt leasing bovendien een uitstap-mogelijkheid - je kunt het actief teruggeven in plaats van het te verkopen. IFRS 16 heeft het off-balance-voordeel grotendeels weggenomen voor IFRS-rapporterende vennootschappen omdat verschuilen-met-leasing een misbruik werd geacht.

<small>🔗 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Gebruikscontext

**Status**: `in-voege` · basis: BE-GAAP: KB WVV art. 3:89 + CBN-adviezen 2015/4. IFRS 16: Verordening (EU) 2023/1803 (verplicht voor EU-genoteerde groepen sinds 2019).

**✅ Voor**
- 🔗 Financiering van duurzame bedrijfsmiddelen: voertuigen, machines, IT-uitrusting, kantooruitrusting, gebouwen. Vooral nuttig wanneer de onderneming het actief wil gebruiken zonder zelf eigenaar te worden, of wanneer ze de fiscale en boekhoudkundige voordelen van off-balance-financiering wil benutten (operationele leasing onder BE-GAAP).

**📋 Voorwaarden**
- 🔗 Schriftelijke leaseovereenkomst tussen leasinggever en leasingnemer met vermelding van: het actief, de looptijd, de leasingvergoeding, eventuele koopoptie + uitoefenprijs, eindbestemming. Voor financiele leasing van immateriele activa (software, octrooien) gelden vergelijkbare maar specifieke regels (CBN-advies 2012/13).

**⚠️ Risico**
- 📖 Misclassificatie BE-GAAP/IFRS: een onjuiste kwalificatie als operationele leasing (om off-balance te blijven) terwijl de substantie financiele leasing aanduidt, vertekent het beeld van het vermogen. Bij een audit of bij een groepsovergang naar IFRS-rapportering komt dit aan het licht en moet herclassificatie gebeuren. De economische realiteit primeert over de juridische vorm (zowel CBN 2015/4 als IFRS 16 alinea 63).

## Bouwstenen

### 📜 Kwalificatie financiele leasing - BE-GAAP (CBN 2015/4)

Twee samenhangende criteria bepalen of een leasing financieel is onder BE-GAAP: (1) Wedersamenstelling van het kapitaal - de totale contractuele lease-vergoedingen samen met de uitoefenprijs van een eventuele koopoptie moeten het volledig geinvesteerde kapitaal van de leasinggever wedersamentellen; (2) De koopoptie wordt enkel meegerekend in de wedersamenstelling wanneer de uitoefenprijs niet meer bedraagt dan 15% van het kapitaal dat de leasinggever in het goed heeft geinvesteerd - de '15%-regel'. Boven 15% wordt verondersteld dat de optie niet automatisch zal gelicht worden en dus geen onderdeel vormt van de financieringsfunctie. Bij een dergelijke koopoptie, of bij automatische eigendomsoverdracht, wordt de leasing als financieel gekwalificeerd, on-balance bij de leasingnemer.

<small>📖 CBN-advies 2015/4 — Aankoopoptie - 15%-regel — _cbn_ · KB WVV — art. 3:89 — _kb_</small>

### 📜 Kwalificatie IFRS 16 - lessee perspectief

IFRS 16 schaft het onderscheid financieel/operationeel af aan lessee-zijde. Bij elke leaseovereenkomst (= contract dat tegen vergoeding gedurende een bepaalde periode het recht verleent zeggenschap uit te oefenen over het gebruik van een geidentificeerd actief) boekt de lessee een right-of-use (RoU)-actief + een leaseverplichting tegen contante waarde van de toekomstige leasebetalingen. Vrijstellingen: (a) short-term leases (looptijd <=12 maanden); (b) leases van low-value actief (drempel ~5000 USD per nieuw actief). Voor deze vrijgestelde leases mag de lessee de leasebetalingen op tijdsevenredige basis als kost opnemen. Voor de lessor (verhuurder) bleef het onderscheid finance/operating wel bestaan.

<small>📖 IFRS 16 (Verordening (EU) 2023/1803) — Alinea 5 + alinea 9 + B3-B8 — _wettekst_</small>

### ⚙️ Twee stelsels naast elkaar - BE-GAAP vs IFRS 16

Voor dezelfde leaseovereenkomst kan de boekhoudkundige verwerking verschillen naargelang het referentiestelsel: in de enkelvoudige Belgische jaarrekening (BE-GAAP) blijft een operationele leasing off-balance; in de geconsolideerde jaarrekening van een IFRS-rapporterende groep (typisch beursgenoteerd of dochter van) wordt diezelfde leasing on-balance gebracht onder IFRS 16. Voor KMO-cliënten zonder IFRS-verplichting blijft de BE-GAAP-kwalificatie de enige relevante. Voor groepscliënten: dubbele rapportering met reconciliatie tussen beide stelsels.

<small>🔗 KB WVV — art. 3:89 + boekhoudreglementering enkelvoudig — _kb_ · IFRS 16 (Verordening (EU) 2023/1803) — Algemeen referentiestelsel - lessee on-balance — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### 📏 15%-drempel koopoptie (BE-GAAP)

De koopoptie van de leasingnemer wordt enkel in de wedersamenstelling van het kapitaal opgenomen wanneer de uitoefenprijs ten hoogste 15% bedraagt van het door de leasinggever geinvesteerde kapitaal. Een koopoptie boven 15% wordt geacht onzeker te zijn - de leasingnemer zal mogelijk niet uitoefenen - en wordt buiten beschouwing gelaten. Gevolg: bij een lease met koopoptie van 5% wordt de optie meegeteld -> wedersamenstelling vaak volledig -> financiele leasing. Bij koopoptie 25%: optie niet meegeteld -> wedersamenstelling vaak onvolledig -> operationele leasing.

<small>📖 CBN-advies 2015/4 — 15%-grens koopoptie leasingnemer — _cbn_</small>

## Voorbeelden

> [!example]- Kwalificatie BE-GAAP - dezelfde machine, twee koopoptie-scenarios
> _Leasinggever koopt een productiemachine voor 100.000 EUR en sluit een leaseovereenkomst af met BV Optima voor 5 jaar. Jaarlijkse leasingvergoeding: 20.000 EUR. Twee varianten van koopoptie._
>
> **Berekening:**
>
> - Variant A - koopoptie 10.000 EUR (= 10% van geinvesteerd kapitaal): onder 15%-drempel, optie meegerekend. Totale wedersamenstelling = 5 x 20.000 + 10.000 = 110.000 EUR. Dat dekt het kapitaal 100.000 EUR + financieringsmarge -> financiele leasing.
> - Variant B - koopoptie 25.000 EUR (= 25% van geinvesteerd kapitaal): boven 15%-drempel, optie buiten beschouwing. Wedersamenstelling = 5 x 20.000 = 100.000 EUR -> dekt enkel het kapitaal, geen rentemarge. Daarbij komt de onzekerheid over de uitoefening van de koopoptie -> kwalificeert eerder als operationele leasing.
> - Conclusie: kleine wijziging in de koopoptie-prijs leidt tot fundamenteel andere boekhoudkundige verwerking. Bij variant A: BV Optima boekt machine (rekening 23) + leasingschuld (rekening 172). Bij variant B: BV Optima boekt enkel leasingvergoeding als huurkost (rekening 610).
>
> <small>🔗 CBN-advies 2015/4 — 15%-regel toepassing — _cbn_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Valkuilen

> [!warning]- Operationele leasing kiezen om off-balance te blijven, ondanks substantie van financiele leasing
> **Verkeerde assumptie**: Door de koopoptie net boven 15% te zetten, blijven we operationele leasing en houden we de schuld off-balance.
>
> **Kernpunt**: Zowel CBN 2015/4 (BE-GAAP) als IFRS 16 alinea 63 stellen dat de economische realiteit primeert over de juridische vorm. Een constructie die louter bedoeld is om de kwalificatie te ontwijken (bv. een onrealistisch hoge koopoptie die niemand zal lichten), kan door de commissaris of auditor herclassificeerd worden. Bij IFRS-rapportering is dit risico groter omdat IFRS 16 al van bij de aanvang lessee-on-balance vereist.
>
> <small>📖 CBN-advies 2015/4 — Economische realiteit primeert — _cbn_ · IFRS 16 (Verordening (EU) 2023/1803) — alinea 63 — _wettekst_</small>

> [!warning]- BE-GAAP en IFRS-verwerking door elkaar halen
> **Verkeerde assumptie**: Onder IFRS 16 staat alle leasing op de balans, dus dat geldt ook voor de Belgische jaarrekening.
>
> **Kernpunt**: BE-GAAP en IFRS 16 zijn twee verschillende referentiestelsels. Voor een KMO-cliënt die enkel een enkelvoudige Belgische jaarrekening neerlegt, gelden de CBN-2015/4-criteria (15%-regel, wedersamenstelling, ...). Pas bij IFRS-verplichting (typisch beursgenoteerde groep of grote consolidatie) komt IFRS 16 in beeld. Voor een groepscliënt: enkelvoudig BE-GAAP + geconsolideerd IFRS 16, met reconciliatie.
>
> <small>🔗 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Accountant-perspectieven

### Leasingnemer (cliëntvennootschap)

_De accountant die een cliënt begeleidt bij het afsluiten en boekhouden van een lease-overeenkomst._

#### 🧭 Adviseur

##### 📜 Afweging financiering vs leasing

Bij elke grote actief-investering: vergelijk drie opties - (1) eigen middelen (geen financieringskosten, gebruikt liquiditeit); (2) banklening (eigenaarschap onmiddellijk + waarborgenstructuur); (3) leasing (volledige financiering + leasinggever blijft juridisch eigenaar). Aandachtspunten: totale cost-of-ownership over de levensduur (rente + restwaarde + onderhoud); fiscale aftrekbaarheid (huurpenningen vs afschrijving + rente); impact op solvabiliteitsratio (off-balance bij operationele leasing BE-GAAP); flexibiliteit (terugnamemogelijkheid bij snelle technologische veroudering).

<small>🔗 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

#### 📒 Boekhouder

##### 👣 Kwalificatie financieel of operationeel

Bij elke nieuwe leaseovereenkomst: (1) Lees het contract: looptijd, leasebedrag, eventuele koopoptie + uitoefenprijs, eindbestemming. (2) Bereken de wedersamenstelling van het kapitaal: som van leasevergoedingen + (koopoptie indien <=15% van kapitaal) -> minstens gelijk aan geinvesteerd kapitaal van leasinggever? (3) Indien ja en koopoptie <=15%: financiele leasing -> on-balance verwerken (zie record financiele-leasing). Indien nee: operationele leasing -> off-balance (zie record operationele-leasing). (4) Voor IFRS-rapporterende cliënten: pas IFRS 16 toe naast BE-GAAP en hou een reconciliatie bij.

<small>📖 CBN-advies 2015/4 — Kwalificatiestappen — _cbn_</small>

## Verder lezen (scope-out)

- → Financiele leasing (specifieke modaliteit) → [[financiele-leasing]] _(moet-verwijzen)_
- → Operationele leasing (specifieke modaliteit) → [[operationele-leasing]] _(moet-verwijzen)_
- → Banklening - primaire vergelijking (eigendoms-financiering) → [[banklening-investeringskrediet]] _(moet-verwijzen)_
- ↪ Autokosten - mobiliteit-perspectief op leasingwagen → [[autokosten]] _(mag-verwijzen)_

## Relaties

### `bevat`
- [[financiele-leasing]]
- [[operationele-leasing]]
### `vergelijkbaar_met`
- [[banklening-investeringskrediet]]
    - **Gelijkenissen**:
        - Beide financieren een specifiek actief
        - Beide leiden tot een periodieke betalingsverplichting
    - **Verschillen**:
        - Banklening: vennootschap wordt onmiddellijk eigenaar; krediet apart op het passief
        - Leasing: leasinggever blijft juridisch eigenaar; bij financiele leasing wordt het actief wel als economisch eigendom on-balance gebracht bij de lessee
        - Banklening: koper kiest eigen waarborgen; leasing: actief zelf is de waarborg
        - Banklening: aftrek via afschrijving + rente; operationele leasing: volledige huurpenning aftrekbaar (eenvoudiger)
    - ⚠️ **Verwarringsrisico**: Verwar leasing niet met een huurcontract. Een huurcontract financiert enkel gebruiksrecht; leasing combineert gebruiksrecht met financiering van het kapitaal.
