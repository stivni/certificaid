---
title: Leaseverplichting onder IFRS 16
tags:
- concept
- begrip
- po-1-5
linked_anchors:
- 1.5.V.C
- 1.5.V
programmaonderdelen:
- '1.5'
confidence: grounded
node_type: begrip
status: seed
schema_version: '1.5'
gegenereerd_uit: data/concepten/records/leaseverplichting-ifrs.json
gegenereerd_op: '2026-05-18'
---
# Leaseverplichting onder IFRS 16 ⚖️

> [!summary] Korte inhoud
> De **leaseverplichting** is de financiële verplichting die de lessee op de aanvangsdatum onder IFRS 16 op zijn balans opneemt: de **contante waarde van leasebetalingen die op aanvangsdatum nog niet zijn verricht** (alinea 26).

> [!info] Behoort tot: [[leasing-ifrs]]

De **leaseverplichting** is de financiële verplichting die de lessee op de aanvangsdatum onder IFRS 16 op zijn balans opneemt: de **contante waarde van leasebetalingen die op aanvangsdatum nog niet zijn verricht** (alinea 26). Disconteringsvoet: **impliciete rentevoet van de leaseovereenkomst** indien gemakkelijk bepaalbaar; anders **marginale rentevoet van de lessee** (rentevoet die de lessee zou betalen om geleende middelen te krijgen voor een soortgelijke transactie). Na eerste opname (alinea 36): boekwaarde verhogen met rente op leaseverplichting (effectieve-rentemethode); boekwaarde verminderen met verrichte leasebetalingen; boekwaarde herwaarderen bij wijzigingen in leaseperiode, aankoopoptie-beoordeling, restwaardegaranties, of index/rentevoet-aanpassingen.

_Bron: IFRS 16 alinea 26-43_


## Bouwstenen

### Welke betalingen tellen mee ⚖️

Bij eerste waardering tellen mee (alinea 27): (a) vaste betalingen (incl. in wezen vaste); (b) variabele leasebetalingen afhankelijk van index/rentevoet, gewaardeerd op basis van index op aanvangsdatum; (c) bedragen verschuldigd uit restwaardegaranties; (d) uitoefenprijs aankoopoptie indien redelijk zeker uitgeoefend; (e) boete voor beëindiging indien leaseperiode dat reflecteert. NIET meegerekend: variabele betalingen die afhangen van toekomstig gebruik of prestatie (bv. omzet-afhankelijke huur).

**Waarom?** Alleen betalingen waarvan op aanvangsdatum vaststaat (of redelijk zeker is) dat ze verschuldigd zullen zijn, horen in de verplichting. Te onzekere variabele betalingen worden als kost geboekt op het moment ze ontstaan.

**Voorbeeld**: Zelena's Antwerpse huur: vaste basishuur € 480.000/jaar in de verplichting. Een omzet-afhankelijke topup van 1% over € 10.000.000 omzet (variabel naar prestatie): NIET in verplichting, jaarlijks als huurkost wanneer verschuldigd.

_Grondslag: IFRS 16 alinea 27 + 38(b)_

### Disconteringsvoet — impliciet of marginaal ⚖️

Eerste keuze: **impliciete rentevoet van de leaseovereenkomst** (rate that equates the present value of lease payments + unguaranteed residual value to the fair value of the underlying asset + initial direct costs of lessor). In de praktijk is die voor de lessee zelden gemakkelijk bepaalbaar. Tweede keuze: **marginale rentevoet van de lessee** (incremental borrowing rate, IBR) — wat de lessee zou betalen om geleende middelen te bekomen voor een soortgelijke termijn en zekerheid.

**Waarom?** De impliciete rentevoet is theoretisch zuiver maar vereist info over de cost-side van de lessor — typisch ontoegankelijk voor de lessee. De marginale rentevoet is een redelijke proxy met data die de lessee zelf heeft.

**Voorbeeld**: Zelena Bio kent de impliciete rentevoet van haar Antwerpse huurcontract niet (verhuurder geeft geen kostprijs). Zij gebruikt haar IBR = 4% (gebaseerd op haar bank-lenenkost voor 10-jarige financiering met vastgoed als onderpand). Verplichting berekend op 4%.

_Grondslag: IFRS 16 alinea 26 + definitie 'marginale rentevoet van de lessee'_

### Effectieve rentemethode na opname ⚖️

Na eerste opname (alinea 36-37): boekwaarde wordt periodiek verhoogd met rente (effectieve rentevoet × openstaande hoofdsom) en verlaagd met de werkelijke leasebetalingen. De rente is een **constant percentage** op het dalende saldo — daardoor neemt de rentelast af terwijl de hoofdsom-aflossing toeneemt over de leaseperiode.

**Waarom?** Een leaseverplichting is in essentie een gefinancierde schuld — de rentemethode is dezelfde als voor een bancaire lening. Het effectieve-rente-principe waarborgt dat de totale rentekosten correct gespreid worden over de leaseperiode.

**Voorbeeld**: Zelena's Antwerpse huur jaar 1: rente € 155.760, hoofdsomaflossing € 324.240, totaal betaald € 480.000. Jaar 2: rente 4% × € 3.569.760 = € 142.790, hoofdsom € 337.210. Rente daalt; hoofdsom-aflossing stijgt.

_Grondslag: IFRS 16 alinea 36-37_

### Herwaardering bij wijzigingen ⚖️

De leaseverplichting wordt herwaardeerd bij (alinea 40-43): (a) verandering in leaseperiode of beoordeling aankoopoptie — dan op basis van **herziene disconteringsvoet**; (b) verandering in restwaardegarantie of in variabele betalingen door index/rentevoet — op basis van **ongewijzigde disconteringsvoet**, tenzij de verandering door variabele rentevoet is (dan herziene rentevoet). De herwaarderingen passen het ROU-actief aan; zou de aanpassing ROU onder nul drukken, dan rest in W&V.

**Waarom?** Een leaseperiode-verlenging of aankoopoptie-uitoefening verandert de aard van de schuld substantieel — nieuwe disconteringsvoet past. Een index-aanpassing is incrementeel — oude voet aanhouden.

**Voorbeeld**: Zelena Bio besluit in 2030 (na 5 jaar) de verlengingsoptie van 3 extra jaar uit te oefenen. Herziene leaseverplichting = contante waarde resterende 8 jaar × € 480.000 + 3 extra × € 480.000 = met herziene IBR van 5% (gestegen sinds 2026). Nieuwe verplichting hoger; ROU-actief stijgt parallel.

_Grondslag: IFRS 16 alinea 40-43_


## In de praktijk

<h3 id="presentatie-apart-van-andere-schulden">Presentatie — apart van andere schulden</h3>

> [!tip]- Presentatie — apart van andere schulden
> Een lessee moet leaseverplichtingen apart presenteren in het overzicht financiële positie OF in de toelichting (alinea 47b). De looptijdanalyse (alinea 58) is verplicht — analoog aan IFRS 7-rapportering voor financiële verplichtingen. ⚖️


## Zie ook

- **Vereist kennis van**: [[right-of-use-actief]]

## Bronnen

[^1]: `IFRS-16-leaseovereenkomsten__sec_waardering`
[^2]: `IFRS-16-leaseovereenkomsten__sec_presentatie`
