---
title: Verwerken van een leaseovereenkomst onder IFRS 16 als lessee (right-of-use
  + lease-verplichting)
tags:
- competentie
- po-1-5
programmaonderdelen:
- '1.5'
status: voorgesteld
schema_version: '1.5'
gegenereerd_uit: data/concepten/records/verwerken-leasing-ifrs-lessee.json
gegenereerd_op: '2026-05-18'
---
# Verwerken van een leaseovereenkomst onder IFRS 16 als lessee (right-of-use + lease-verplichting)

**⚖️ 80% · 🤖 20%**

> De single-model-benadering, eerste waardering en afschrijvings-/rente-splitsing zijn volledig in IFRS 16 alinea's 22-45 geregeld. Het praktijk-aandeel zit in de keuze of de vrijstellingen (kortlopend, lage waarde) worden toegepast en in het bepalen van de marginale rentevoet wanneer de impliciete rentevoet niet bekend is.

## Aanbevolen werkwijze

### 1. Identificeer of het contract een lease bevat

Toets of het contract het recht verleent om gedurende een periode het gebruik van een geïdentificeerd actief te beheersen in ruil voor een vergoeding.

**Waarom?** IFRS 16 alinea 9-11 (bijlage B9-B33) bepaalt dat enkel contracten met 'identified asset' + 'right to direct the use' onder de standaard vallen. Servicecontracten zonder beheersing van een actief vallen erbuiten.

**📥 Input**:
- Contract (huur, leasing, gebruiksrecht) → **Identificatie actief + beheersingsrechten** _(document)_

**📤 Output**:
- Werkpapier lease-kwalificatie → **Lease ja/nee + grondslag** _(conclusie)_

**🛠️ Hoe**:

1. Lees het contract van Zelena Bio NV voor de Antwerpse productiehal: huur 10 jaar, vaste betaling € 480.000/jaar, geen variabele componenten gekoppeld aan omzet, geen koopoptie.
2. Toets op 'identified asset': specifiek de hal in Antwerpen (niet een willekeurig gebouw uit de portefeuille van Vastgoed Veurne NV) → ja.
3. Toets op 'right to direct the use': Zelena beslist wanneer en hoe de hal wordt gebruikt → ja.
4. Conclusie: contract bevat een lease in de zin van IFRS 16. Documenteer in werkpapier.


**Grondslag**: [[leasing-ifrs]] §kwalificatie, IFRS 16 alinea 9 + B9-B33

### 2. Beslis of een vrijstelling wordt toegepast

Beoordeel of de lease kortlopend is (≤ 12 maanden zonder koopoptie) of een lage waarde betreft (≤ ca. € 5.000 als nieuw — alinea 5-6 + B3-B8). Bij gekozen vrijstelling: huurlast lineair in W&V, géén balansopname.

**Waarom?** De vrijstellingen verminderen administratie voor kleine of korte leases. Wie ze niet gebruikt mag dat (alinea 5 is een keuze), maar dan moet de lease op de balans.

**📥 Input**:
- Contract kenmerken uit stap 1 → **Duur + waarde-onderwerp** _(document)_

**📤 Output**:
- Werkpapier lease-kwalificatie → **Vrijstelling ja/nee + categorie** _(conclusie)_

**🛠️ Hoe**:

1. Volg [[leasing-ifrs]] §vrijstellingen voor de twee criteria.
2. Zelena's productiehal: 10 jaar (niet kortlopend); waarde productiehal ≫ € 5.000 (niet lage waarde) → geen vrijstelling, **on-balance**.
3. Voor klein bureeluitrustinghuur (≤ € 5.000 per stuk, bv. printer-leasing): vrijstelling 'lage waarde' kan gekozen worden — keuze per individueel onderliggend actief (alinea 8).
4. Documenteer beslissing.


**Grondslag**: [[leasing-ifrs]] §vrijstellingen, IFRS 16 alinea 5-8 + B3-B8

### 3. Bepaal de leaseperiode en de leasebetalingen die meetellen

Stel de niet-opzegbare leaseperiode vast + verlengingsopties die de lessee redelijk zeker zal uitoefenen + opzegtermijnen die niet zullen worden uitgeoefend. Identificeer alle leasebetalingen die in de eerste waardering meegaan.

**Waarom?** Foute leaseperiode of weggelaten variabele componenten leiden tot een te lage leaseverplichting en ROU-actief — met fout afschrijvings- en rente-patroon over de hele looptijd.

**📥 Input**:
- Contract Zelena Bio NV — Antwerpse hal → **Niet-opzegbare periode + opties** _(document)_

**📤 Output**:
- Werkpapier waardering → **Leaseperiode + lijst betalingen** _(document)_

**🛠️ Hoe**:

1. Volg [[leaseverplichting-ifrs]] §welke-betalingen-tellen-mee voor de inventaris van betalingen.
2. Zelena's contract: 10 jaar niet-opzegbaar + verlengingsoptie 3 jaar. Beoordeel waarschijnlijkheid uitoefening — bij Zelena: nog niet redelijk zeker → leaseperiode = **10 jaar**.
3. Inventaris betalingen: vaste basishuur € 480.000/jaar = in de verplichting. Een eventuele omzet-afhankelijke topup van 1% × omzet: **NIET** in de verplichting (variabel naar prestatie — alinea 27); jaarlijks als kost wanneer verschuldigd.
4. Restwaardegarantie: bij Zelena nihil.
5. Documenteer in werkpapier: leaseperiode + cashflow-tabel van vaste betalingen.


**Grondslag**: [[leasing-ifrs]] §leaseperiode, IFRS 16 alinea 18-21 + 27

> [!warning]- Variabele betalingen die afhangen van toekomstig gebruik of prestatie (bv. omzet-topup) NIET in de eerste waardering opnemen — alleen vaste of in-wezen-vaste betalingen.
>
> _Vaak fout gedaan_: Variabele omzet-huur in de leaseverplichting opnemen op basis van een schatting. Dit overschat zowel actief als schuld.
>
> _Grondslag_: [[leaseverplichting-ifrs]] §welke-betalingen, IFRS 16 alinea 27 + 38(b)

### 4. Bereken en boek de eerste waardering van ROU-actief en leaseverplichting

Leaseverplichting = contante waarde van leasebetalingen tegen impliciete rentevoet (of marginale rentevoet lessee). ROU-actief = leaseverplichting + initiële directe kosten + ontmantelings-/herstelverplichting − ontvangen prikkels.

**Waarom?** IFRS 16 vereist een gespiegelde balansopname: de lessee toont het gebruiksrecht aan de actief-zijde en de financieringsverplichting aan de passief-zijde. Symmetrie is essentieel.

**📥 Input**:
- Leaseperiode + betalingen uit stap 3 → **Cashflow-tabel** _(boekhoudkundig-bedrag)_
- Marginale rentevoet lessee → **IBR (incremental borrowing rate)** _(percentage)_

**📤 Output**:
- Geboekte balanspost ROU + Leaseverplichting → **Bedragen op aanvangsdatum** _(nieuwe-balanspost)_

**🛠️ Hoe**:

1. Volg [[leaseverplichting-ifrs]] §berekening-eerste-waardering voor de contante-waarde-formule.
2. Zelena Bio NV: impliciete rentevoet onbekend (verhuurder geeft geen kostprijs) → gebruik marginale rentevoet 4 % (gebaseerd op 10-jarige bankfinanciering met vastgoed-onderpand).
3. Bereken leaseverplichting = € 480.000 × annuïteitfactor(10 jaar; 4 %) = € 480.000 × 8,1109 = **€ 3.893.232 ≈ € 3.894.000**.
4. ROU-actief = leaseverplichting € 3.894.000 + initiële directe kosten € 0 + ontmanteling € 0 − prikkels € 0 = **€ 3.894.000**.
5. Boek de eerste waardering op aanvangsdatum (1 januari 2026).


> [!example]- Voorbeeld: Zelena Bio NV op aanvangsdatum 1 januari 2026: 10-jarige huur productiehal Antwerpen, vaste betaling € 480.000/jaar, mar…
> Zelena Bio NV op aanvangsdatum 1 januari 2026: 10-jarige huur productiehal Antwerpen, vaste betaling € 480.000/jaar, marginale rentevoet 4 %.
>
> 1. **Berekening leaseverplichting** 🧮
>
>    annuïteitfactor(10 jaar; 4 %) = (1 − (1 + 0,04)^−10) / 0,04 = **8,1109**
>    leaseverplichting = € 480.000 × 8,1109
>                      = **€ 3.894.000** (afgerond)
>    
>
> 2. **Boeking eerste waardering** 📝
>
>    Debiteer:  Right-of-use actief — gebouw      € 3.894.000
>    Crediteer: Leaseverplichting                  € 3.894.000
>    
>    (Symmetrische balansopname; geen impact op W&V op aanvangsdatum.)
>    
>
> 3. **Impactbalans Zelena Bio NV (vóór versus na opname)** 📊
>
>    | Geconsolideerde balans (uittreksel)  | Vóór (€)        | Na (€)          |
>    |--------------------------------------|----------------:|----------------:|
>    | Materiële vaste activa               |      85.000.000 |      85.000.000 |
>    | **Right-of-use actief**              |               0 |   **3.894.000** |
>    | Vlottende activa                     |      40.000.000 |      40.000.000 |
>    | **Totaal activa**                    |     125.000.000 |     128.894.000 |
>    | Eigen vermogen                       |      80.000.000 |      80.000.000 |
>    | **Leaseverplichting (langlopend)**   |               0 |   **3.413.760** |
>    | **Leaseverplichting (kortlopend)**   |               0 |     **480.240** |
>    | Andere schulden                      |      45.000.000 |      45.000.000 |
>    | **Totaal passiva**                   |     125.000.000 |     128.894.000 |
>    
>

**Grondslag**: [[leasing-ifrs]] §eerste-waardering, [[right-of-use-actief]] §componenten, IFRS 16 alinea 22-26

### 5. Boek de jaarlijkse verwerking: afschrijving ROU + rente leaseverplichting

Schrijf ROU-actief lineair af over leaseperiode (of lager van leaseperiode/gebruiksduur indien koopoptie zeker). Pas effectieve rentemethode toe op leaseverplichting: rente over openstaand saldo + aflossing hoofdsom uit betaling.

**Waarom?** Het IFRS 16-resultaatpatroon is **front-loaded**: rente is hoger in beginjaren (groot saldo) en daalt; afschrijving is lineair. Totale jaarlijkse W&V-impact is dus hoger in beginjaren dan onder BE-GAAP-huurlast.

**📥 Input**:
- Boekwaarden ROU + leaseverplichting begin boekjaar → **Bedragen** _(boekhoudkundig-bedrag)_
- Cashflow-tabel + rentevoet → **Jaarlijkse betaling + IBR** _(boekhoudkundig-bedrag)_

**📤 Output**:
- Boekingen W&V + balans → **Afschrijving + rente + aflossing** _(boekingsregel)_

**🛠️ Hoe**:

1. Volg [[leaseverplichting-ifrs]] §effectieve-rentemethode voor de splitsing rente/aflossing.
2. Voor Zelena Bio jaar 1 (2026):
   - Afschrijving ROU = € 3.894.000 / 10 = **€ 389.400** (lineair).
   - Rente leaseverplichting = 4 % × € 3.894.000 = **€ 155.760**.
   - Betaling € 480.000; aflossing hoofdsom = € 480.000 − € 155.760 = **€ 324.240**.
   - Boekwaarde ROU einde jaar 1 = € 3.894.000 − € 389.400 = € 3.504.600.
   - Boekwaarde leaseverplichting einde jaar 1 = € 3.894.000 − € 324.240 = € 3.569.760.
3. Boekingen per kwartaal of jaareinde:
   - Debet 'Afschrijving ROU' / credit 'Cumulatieve afschrijving ROU' € 389.400.
   - Debet 'Rentelast leaseverplichting' / credit 'Leaseverplichting' € 155.760.
   - Debet 'Leaseverplichting' / credit 'Bank' € 480.000.
4. Aandachtspunt: jaar 2 rente = 4 % × € 3.569.760 = € 142.790; dus de jaarlijkse W&V-last daalt langzaam.


> [!example]- Voorbeeld: Zelena Bio NV jaar 1 (2026) verwerking lease productiehal Antwerpen — eerste boekjaar
> Zelena Bio NV jaar 1 (2026) verwerking lease productiehal Antwerpen — eerste boekjaar.
>
> 1. **Splitsing van de € 480.000 betaling jaar 1** 🧮
>
>    betaling totaal       = € 480.000
>    ─ rente               = 4 % × € 3.894.000 = **€ 155.760**
>    ─ aflossing hoofdsom  = € 480.000 − € 155.760 = **€ 324.240**
>    
>
> 2. **Boekingen jaar 1 (samengevat)** 📝
>
>    (a) Afschrijving ROU
>    Debiteer:  Afschrijvingskosten ROU              € 389.400
>    Crediteer: Cumulatieve afschrijving ROU         € 389.400
>    
>    (b) Rente + betaling
>    Debiteer:  Rentelast leaseverplichting          € 155.760
>    Debiteer:  Leaseverplichting (aflossing)        € 324.240
>    Crediteer: Bank                                  € 480.000
>    
>
> 3. **Totale W&V-impact jaar 1** 🧮
>
>    afschrijving ROU                  = € 389.400
>    + rentelast                       = € 155.760
>    **= € 545.160** (versus € 480.000 huurlast onder BE-GAAP)
>    
>    Verschil = € 65.160 hogere W&V-last in jaar 1 onder IFRS — front-loaded patroon.
>    
>

**Grondslag**: [[leasing-ifrs]] §verwerking, [[leaseverplichting-ifrs]] §effectieve-rentemethode, IFRS 16 alinea 30-38

> [!warning]- Hou rente en afschrijving strikt gescheiden in de W&V — de splitsing is een kerncomponent van IFRS 16-rapportering.
>
> _Vaak fout gedaan_: Het totaal betaalde bedrag (€ 480.000) als 'huurkost' boeken, alsof het BE-GAAP was. Dat negeert zowel de balansopname als de splitsing rente/afschrijving.
>
> _Grondslag_: [[leaseverplichting-ifrs]] §effectieve-rentemethode


## Voorbeelden

> [!example]- Vergelijking: Zelena Bio NV (IFRS) versus Rotex Roeselare NV (BE-GAAP) sluiten elk een identiek 10-jarig huurcontract vo…
> **Conclusie**: Zelena onder IFRS 16: ROU-actief € 3.894.000 + leaseverplichting € 3.894.000 op aanvangsdatum; W&V-last jaar 1 = afschrijving € 389.400 + rente € 155.760 = € 545.160. Rotex onder BE-GAAP (CBN 2015/04 — operationele lease): geen balansopname; W&V-last = € 480.000 (huurlast). Verschil EBITDA: Zelena toont € 480.000 hoger EBITDA (geen huur in EBITDA, wel afschrijving daaronder); ratio's debt/equity stijgen voor Zelena.
>
> **Grondslag**: [[leasing-ifrs]] §single-model; [[leasing]] §be-gaap-onderscheid; [[ifrs-16-lessee-vs-lessor-overzicht]] §vergelijkingstabel
>
> **Redenering**: IFRS 16 schaft het lessee-onderscheid operationeel/financieel af; BE-GAAP behoudt het. Dezelfde economische realiteit, twee verschillende balansposities en verschillende W&V-patronen. Examenvragen toetsen vaak dit verschil door één feiten-situatie onder beide stelsels te laten verwerken.


## Gebaseerd op concepten

[[leasing-ifrs]] · [[right-of-use-actief]] · [[leaseverplichting-ifrs]] · [[ifrs-16-lessee-vs-lessor-overzicht]] · [[leasing]]
## Voortkomend uit

- **Taken**: 1.5.taak.1
- **Kenniselementen**: 1.5.V.C, 1.5.V, 1.5.IV.C
