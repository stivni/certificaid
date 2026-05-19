---
title: Uitvoeren van de eerste toepassing van IFRS overeenkomstig IFRS 1
tags:
- concept
- competentie
- po-1-5
linked_anchors:
- 1.5.taak.1
- 1.5.IV.A
- 1.5.IV
- 1.5.IV.C
programmaonderdelen:
- '1.5'
confidence: inferred
node_type: competentie
status: voorgesteld
schema_version: '1.5'
gegenereerd_uit: data/concepten/records/uitvoeren-eerste-toepassing-ifrs.json
gegenereerd_op: '2026-05-18'
---
# Uitvoeren van de eerste toepassing van IFRS overeenkomstig IFRS 1 🤖


## Stappen

### 1. Stel de datum van overgang naar IFRS vast

Identificeer de begindatum van de vergelijkende periode in de eerste IFRS-jaarrekening — dat is de overgangsdatum.

**Waarom?** Op die datum moet de openingsbalans al volledig IFRS-conform zijn. Foute overgangsdatum = alle openingscijfers verkeerd in de tijd geplaatst.

**📥 Input**:
- Bestuursbeslissing tot IFRS-toepassing → **Eerste IFRS-verslagperiode** _(datum)_

**📤 Output**:
- IFRS-overgangsdossier → **Datum van overgang naar IFRS** _(datum)_

**🛠️ Hoe**:

1. Volg [[ifrs-eerste-toepassing]] §stap-1 voor de definitie van overgangsdatum.
2. Zelena Bio NV beslist begin 2027 voor het eerst IFRS toe te passen voor boekjaar eindigend 31 december 2027.
3. Vergelijkende periode = boekjaar 2026 → overgangsdatum = **1 januari 2026**.
4. Documenteer in het IFRS-overgangsdossier.


**Grondslag**: [[ifrs-eerste-toepassing]] §stap-1, IFRS 1 alinea 3 en 6

### 2. Stel het IFRS-openingsoverzicht financiële positie op

Maak op de overgangsdatum een balans die volledig voldoet aan IFRS — vier acties: opnemen, niet-opnemen, herclassificeren, herwaarderen volgens IFRS-grondslagen.

**Waarom?** De openingsbalans is het IFRS-vertrekpunt. Het verschil met BE-GAAP-balans gaat rechtstreeks naar ingehouden winsten — niet via resultaat.

**📥 Input**:
- Belgisch-GAAP-balans op overgangsdatum → **Alle activa en passiva** _(boekhoudkundig-bedrag)_
- IFRS-grondslagenkeuze → **Per categorie: kostprijs- of reëlewaardemodel** _(beleidskeuze)_

**📤 Output**:
- IFRS-openingsbalans → **Volledige balans per overgangsdatum** _(jaarrekening-overzicht)_

**🛠️ Hoe**:

1. Volg [[ifrs-eerste-toepassing]] §stap-2 voor de vier acties.
2. Doorloop elke balanspost van Zelena Bio NV per 1 januari 2026 en check op basis van [[be-gaap-vs-ifrs-overzicht]] §vergelijkingstabel waar IFRS afwijkt.
3. Voorbeeld-aanpassingen: schrap geactiveerde onderzoekskosten € 2.500.000 (IAS 38 art. 54); neem operationele leasing on-balance (IFRS 16: ROU + leaseverplichting); stop goodwill-afschrijving en plaats goodwill onder jaarlijkse impairment-test (IAS 36).
4. Documenteer per balanspost: actie + bedrag + IFRS-grondslag.


> [!example]- Voorbeeld: Zelena Bio NV op overgangsdatum 1 januari 2026: BE-GAAP-eigen vermogen € 125.000.000
> Zelena Bio NV op overgangsdatum 1 januari 2026: BE-GAAP-eigen vermogen € 125.000.000. Aanpassingen volgens vier acties.
>
> 1. **Vier acties toegepast** 🧮
>
>    | Actie                                                              | Bedrag (€)    |
>    |--------------------------------------------------------------------|-------------:|
>    | (b) Schrap geactiveerde onderzoekskosten (IAS 38 art. 54)          |  −2.500.000  |
>    | (a) Neem gebruiksrecht wagenpark op (IFRS 16)                      | +20.000.000  |
>    | (a) Neem leaseverplichting wagenpark op (IFRS 16)                  | −24.000.000  |
>    | (d) Terreinen op reële waarde — vrijstelling IFRS 1 D5             |  +6.000.000  |
>    | (d) Terugname jaarlijkse goodwill-afschrijving 2020-2025 (IFRS 3) |  +1.500.000  |
>    | **Netto-impact op ingehouden winsten**                             |  **+1.000.000** |
>    
>
> 2. **Eigen-vermogen-aansluiting** 🧮
>
>    EV onder BE-GAAP per 1 januari 2026 = € 125.000.000
>    + netto-aanpassingen volgens vier acties = € 1.000.000
>    = **EV onder IFRS per 1 januari 2026 = € 126.000.000**
>    
>

**Grondslag**: [[ifrs-eerste-toepassing]] §stap-2, IFRS 1 alinea 10 + 11

### 3. Pas verplichte uitzonderingen en gekozen vrijstellingen toe

Beoordeel per balanspost welke verplichte uitzonderingen (IFRS 1 bijlage B) en welke optionele vrijstellingen (bijlagen C-D-E) van toepassing zijn of worden gekozen.

**Waarom?** Volledige retroactieve toepassing zou misleidende resultaten geven of praktisch onhaalbaar zijn. De uitzonderingen + vrijstellingen kalibreren de overgang op een redelijke kostengrens.

**📥 Input**:
- Lijst balansposten + IFRS-grondslagenkeuze stap 2 → **Per post: hypothese over te gebruiken vrijstelling** _(beleidskeuze)_
- IFRS 1 bijlagen B-C-D-E → **Toepasselijke uitzonderingen en vrijstellingen** _(regelset)_

**📤 Output**:
- IFRS-overgangsdossier → **Keuzen en motivering per categorie** _(beleidskeuze)_

**🛠️ Hoe**:

1. Volg [[ifrs-eerste-toepassing]] §stap-3 voor de structuur uitzonderingen versus vrijstellingen.
2. Verplichte uitzonderingen (bijlage B) toetsen: schattingen onder BE-GAAP **niet** herzien tenzij objectieve aanwijzing van fout (alinea 14-15); hedge-aanwijzingen niet retroactief; niet-beheersbelangen prospectief.
3. Optionele vrijstellingen (bijlage D) overwegen: D5 'reële waarde als veronderstelde kostprijs' voor materiële vaste activa — Zelena's terreinen op € 18.000.000 (reële waarde) i.p.v. € 12.000.000 (BE-GAAP-kostprijs); D7 'cumulatieve omrekeningsverschillen op nul zetten'; D1 'IFRS 3 bedrijfscombinaties niet retroactief'.
4. Documenteer per gebruikte vrijstelling: motivering + impact op eigen vermogen.


**Grondslag**: [[ifrs-eerste-toepassing]] §stap-3, IFRS 1 alinea 13-17 + bijlagen B-D

> [!warning]- Beslis bewust over D5: reële waarde als veronderstelde kostprijs mag alleen bij eerste toepassing — niet later.
>
> _Vaak fout gedaan_: De vrijstelling D5 op een later moment alsnog willen gebruiken — IFRS 1 staat dat niet toe.
>
> _Grondslag_: [[ifrs-eerste-toepassing]] §uitzonderingen-en-vrijstellingen

### 4. Verwerk het aanpassingsverschil rechtstreeks in ingehouden winsten

Boek het saldo tussen BE-GAAP- en IFRS-eigen-vermogen op overgangsdatum als correctie op de openingspost 'Ingehouden winsten' — NIET via winst of verlies.

**Waarom?** Het aanpassingsverschil weerspiegelt feiten van vóór de overgangsdatum. Via W&V boeken zou één jaar belasten met correcties die op meerdere voorgaande jaren slaan.

**📥 Input**:
- EV onder BE-GAAP op overgangsdatum → **Bedrag** _(boekhoudkundig-bedrag)_
- EV onder IFRS op overgangsdatum (uit stappen 2-3) → **Bedrag** _(boekhoudkundig-bedrag)_

**📤 Output**:
- IFRS-openingsbalans → **Ingehouden winsten — aangepast** _(boekhoudkundig-bedrag)_

**🛠️ Hoe**:

1. Volg [[ifrs-eerste-toepassing]] §stap-4 voor de boekingsregel.
2. Voor Zelena Bio NV: aanpassingsverschil = € 126.000.000 − € 125.000.000 = +€ 1.000.000.
3. Boek het volledige verschil onder 'Ingehouden winsten' in de IFRS-openingsbalans per 1 januari 2026.
4. Hou de splitsing per categorie bij voor de toelichting: aandeel goodwill-correctie / aandeel leasing-correctie / aandeel onderzoek-schrap / aandeel terreinen-uplift.


**Grondslag**: [[ifrs-eerste-toepassing]] §stap-4, IFRS 1 alinea 11

### 5. Stel aansluitingstabellen en toelichting op

Maak in de eerste IFRS-jaarrekening de verplichte aansluitingen: EV op overgangsdatum, EV op einddatum laatste BE-GAAP-periode, en totaalresultaat over de laatste BE-GAAP-periode.

**Waarom?** Gebruikers (beleggers, analisten, commissaris) moeten traceerbaar de overgang kunnen volgen. Zonder aansluiting lijkt de overgang een 'cijfermachine' zonder verklaring.

**📥 Input**:
- BE-GAAP-cijfers vergelijkende periode → **EV + totaalresultaat** _(boekhoudkundig-bedrag)_
- IFRS-cijfers vergelijkende periode (parallel rapportering) → **EV + totaalresultaat** _(boekhoudkundig-bedrag)_

**📤 Output**:
- Toelichting eerste IFRS-jaarrekening → **Aansluitingstabellen + grondslagen-toelichting** _(toelichtingsnoot)_

**🛠️ Hoe**:

1. Volg [[ifrs-eerste-toepassing]] §stap-5 voor de drie verplichte aansluitingen.
2. Aansluitingstabel EV op overgangsdatum: startlijn 'EV BE-GAAP', per aanpassing één regel met grondslag, eindlijn 'EV IFRS'.
3. Idem voor EV op 31 december 2026 (einddatum vergelijkende periode).
4. Aansluiting totaalresultaat 2026 (BE-GAAP → IFRS): begin met BE-GAAP-resultaat, lijst per IFRS-correctie de impact op resultaat versus OCI.
5. Voeg toe: lijst gebruikte vrijstellingen IFRS 1 + impact + IAS 36-info indien impairment voor het eerst opgenomen.
6. Drie balansen presenteren in eerste IFRS-jaarrekening (IAS 1 alinea 40A): overgangsdatum + einde vergelijkende + einde eerste IFRS-periode.


**Grondslag**: [[ifrs-eerste-toepassing]] §stap-5, IFRS 1 alinea 23-25 + IAS 1 alinea 40A

> [!warning]- Drie balansen presenteren in de eerste IFRS-jaarrekening — niet twee.
>
> _Vaak fout gedaan_: Alleen de eindbalans en vergelijkbare balans tonen. Bij eerste IFRS-jaarrekening is een derde balans (op overgangsdatum) verplicht.
>
> _Grondslag_: [[jaarrekening-componenten-ifrs]] §drie-balansen-bij-eerste-toepassing


## Zie ook

- **Vereist kennis van**: [[ifrs-eerste-toepassing]]
- **Vereist kennis van**: [[stelselwissel-jaarrekening]]

## Voorbeelden



