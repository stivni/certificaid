---
title: Toepassen van de volledige kostencalculatie (full costing) op een productie-eenheid
tags:
- competentie
- po-1-8
programmaonderdelen:
- '1.8'
status: voorgesteld
schema_version: '1.1'
gegenereerd_uit: data/concepten/competenties/toepassen-volledige-kostencalculatie.yaml
gegenereerd_op: '2026-05-17'
---
# Toepassen van de volledige kostencalculatie (full costing) op een productie-eenheid

**⚖️ 35% · 🤖 65%**

> De volledige bedrijfskostprijs is vakdoctrine, maar de wettelijke vervaardigingsprijs (KB 21.10.2018 art. 22 + CBN 132/7) gebruikt dezelfde mechanica met expliciete verplichting indirecte productiekosten op te nemen. Voor voorraadwaardering wordt de procedure dus deels wettelijk gestuurd.

## Aanbevolen werkwijze

### 1. Identificeren van directe versus indirecte kosten

Splits alle kosten in twee groepen: direct toewijsbaar aan de kostendrager versus niet rechtstreeks toewijsbaar.

**Waarom?** Alleen op deze tweedeling werkt de toewijzingslogica van full costing — directe kosten kunnen rechtstreeks, indirecte vereisen een sleutel.

**📥 Input**:
- Kostenoverzicht per kostensoort → **Bedragen per categorie** _(boekhoudkundig-bedrag)_

**📤 Output**:
- Twee kolommen direct / indirect → **Bedragen geclassificeerd** _(document)_

**🛠️ Hoe**:

1. Pas [[directe-kosten]] §toewijsbaarheid toe: kan elke kost ondubbelzinnig aan
   één product of order gehecht worden zonder verdeelsleutel?
2. Pas [[indirecte-kosten]] §gemeenschappelijke-kost toe op de rest:
   verlichting werkplaats, leiding, onderhoud, afschrijving algemene installaties.
3. Let op: een kost kan direct én variabel zijn, of direct én vast — dimensies overlappen.
   Voor full costing telt vooral de directe/indirecte-as.
4. Documenteer twijfelgevallen (bv. werkkledij): kies één categorie en houd consistent vol.


**Grondslag**: [[directe-kosten]] §toewijsbaarheid, [[indirecte-kosten]] §gemeenschappelijke-kost

### 2. Verdelen van indirecte kosten over kostencentra (primaire verdeling)

Alloceer elke indirecte-kosten-soort naar een kostencentrum (hulp- of hoofd-centrum) volgens een verdeelsleutel.

**Waarom?** De kost moet eerst landen waar hij verbruikt is voordat hij kan worden doorgesluisd naar dragers.

**📥 Input**:
- Indirecte kosten uit stap 1 → **Bedragen per indirecte soort** _(boekhoudkundig-bedrag)_
- Sleutelmatrix uit [[opzetten-analytisch-rekeningenstelsel]] → **Per soort een toewijzingsbasis** _(document)_

**📤 Output**:
- Tabel kostencentrum × kostensoort → **Bedrag per cel** _(boekhoudkundig-bedrag)_

**🛠️ Hoe**:

1. Volg [[verdeelsleutel]] §oorzakelijkheidsprincipe.
2. Pas per indirecte-kosten-soort de gekozen sleutel toe:
   - Huur fabriek: m² per centrum.
   - Energie: machine-uren of kWh-meting per centrum.
   - Leiding/admin: aantal medewerkers per centrum.
3. Maak een matrix kostencentrum (kolommen) × kostensoort (rijen).
4. Som per kolom: totaal toegewezen aan elk centrum.


**Grondslag**: [[verdeelsleutel]] §oorzakelijkheidsprincipe, [[kostencentrum]] §primaire-verdeling

### 3. Verdelen van hulp-centra over hoofd-centra (secundaire verdeling)

Verdeel de kost van ondersteunende kostencentra (onderhoud, stroom) over de productiecentra die er gebruik van maken.

**Waarom?** Hulp-centra dragen geen product; hun kost moet doorrollen naar de hoofd-centra waar productie gebeurt.

**📥 Input**:
- Primaire verdeling uit stap 2 → **Totalen per centrum** _(boekhoudkundig-bedrag)_

**📤 Output**:
- Tabel hoofd-centra met volledige indirecte kost → **Totaal per hoofd-centrum** _(boekhoudkundig-bedrag)_

**🛠️ Hoe**:

1. Bepaal de verdeelsleutel hulp→hoofd (bv. onderhoudsuren per centrum,
   kWh-verbruik per centrum).
2. Verdeel het totaal van elk hulp-centrum over de hoofd-centra met deze sleutel.
3. Als hulp-centra onderling diensten leveren: gebruik trapsgewijze of
   gelijktijdige (matrix) verdeling — voor stagiair volstaat trapsgewijs.
4. Resultaat: elk hoofd-centrum bevat zowel zijn eigen primaire kost als zijn
   aandeel in de hulp-centra.


**Grondslag**: [[kostencentrum]] §secundaire-verdeling, [[verdeelsleutel]] §primair-secundair

### 4. Doorrekenen naar kostendragers

Bereken per hoofd-centrum een opslag-tarief (bv. per machine-uur of per directe-arbeidsuur) en pas dit toe op de dragers.

**Waarom?** Pas dan zit alle indirecte kost in de kostprijs van het product of de order — de basis voor voorraadwaardering en prijszetting.

**📥 Input**:
- Indirecte kost per hoofd-centrum uit stap 3 → **Bedrag per centrum** _(boekhoudkundig-bedrag)_
- Werkelijke productie-data → **Uren of eenheden per drager per centrum** _(boekhoudkundig-bedrag)_

**📤 Output**:
- Kostprijs per kostendrager → **Direct + indirect = totaal** _(nieuwe-balanspost)_

**🛠️ Hoe**:

1. Bereken per hoofd-centrum een opslag-tarief:
   tarief = totaal indirecte kost centrum / totaal eenheden activiteit centrum.
2. Vermenigvuldig het tarief met de eenheden activiteit die elke drager
   in dat centrum heeft verbruikt.
3. Tel direct toegewezen kosten (uit stap 1) en doorberekend indirect bij elkaar
   op volgens [[volledige-kostencalculatie]] §sommatie.
4. Vergelijk met [[vervaardigingsprijs]] §wettelijke-componenten als de
   kostprijs ook voor balans-voorraadwaardering wordt gebruikt — productie-onafhankelijke
   overhead (commercieel, administratief) hoort dan NIET mee.


> [!example]- Voorbeeld: Yperse Werkplaats BV — kostprijs van een serie van 1.000 tapijten-standaard die gepasseerd zijn door Spinnerij, Weverij…
> Yperse Werkplaats BV — kostprijs van een serie van 1.000 tapijten-standaard die gepasseerd zijn door Spinnerij, Weverij en Confectie.
>
> 1. **Directe kosten van de serie** 🧮
>
>    | Component                       | Bedrag       |
>    |---------------------------------|-------------:|
>    | Wol (5.000 kg × € 5,00)         | € 25.000     |
>    | Directe arbeid Spinnerij (320 u × € 25)  | €  8.000 |
>    | Directe arbeid Weverij (200 u × € 25)    | €  5.000 |
>    | Directe arbeid Confectie (160 u × € 25)  | €  4.000 |
>    | **Totaal directe kosten**       | **€ 42.000** |
>    
>
> 2. **Opslag-tarieven per hoofd-centrum (jaarbasis)** 🧮
>
>    | Centrum   | Indirecte kost | Activiteit   | Tarief        |
>    |-----------|---------------:|-------------:|--------------:|
>    | Spinnerij | € 200.000      | 8.000 mach-u | € 25/mach-uur |
>    | Weverij   | € 320.000      | 6.400 mach-u | € 50/mach-uur |
>    | Confectie | € 280.000      | 7.000 arb-u  | € 40/arb-uur  |
>    
>
> 3. **Indirecte kost toegewezen aan de serie** 🧮
>
>    | Centrum   | Activiteit serie | Tarief        | Bedrag       |
>    |-----------|-----------------:|--------------:|-------------:|
>    | Spinnerij | 200 mach-u       | € 25/mach-uur | €  5.000     |
>    | Weverij   | 160 mach-u       | € 50/mach-uur | €  8.000     |
>    | Confectie | 160 arb-u        | € 40/arb-uur  | €  6.400     |
>    | **Totaal indirect serie**    |               | **€ 19.400** |
>    
>
> 4. **Totale kostprijs en kostprijs per eenheid** 🧮
>
>    Totale kostprijs serie = € 42.000 + € 19.400 = **€ 61.400**
>    
>    Kostprijs per tapijt = € 61.400 / 1.000 = **€ 61,40**
>    
>

**Grondslag**: [[volledige-kostencalculatie]] §toewijzing-naar-drager, [[kostprijs-per-eenheid]] §drie-gebruiksdoelen, [[vervaardigingsprijs]] §wettelijke-componenten, KB 21.10.2018 art. 22

> [!warning]- Toets bij het rapporteren of de kostprijs voor balans-voorraadwaardering wordt gebruikt — neem dan alleen productie-overhead op, niet commercieel/administratief.
>
> _Vaak fout gedaan_: Volledige bedrijfskostprijs (inclusief verkoop en administratie) blindelings als voorraadwaarde op de balans plaatsen.
>
> _Grondslag_: [[vervaardigingsprijs]] §scope, CBN 132/7 §2.1

> [!warning]- Documenteer activiteit-eenheid (machine-uren, arbeids-uren) per centrum consistent.
>
> _Vaak fout gedaan_: In het ene centrum mach-uren als sleutel gebruiken en in het andere arb-uren zonder uitleg — onvergelijkbaar.
>
> _Grondslag_: [[verdeelsleutel]] §oorzakelijkheidsprincipe


## Voorbeelden

> [!example]- Yperse Werkplaats BV (productie wollen tapijten) berekent kostprijs van een serie tapijten-standaard die drie productiec…
> **Conclusie**: Kostprijs van € 61,40 per tapijt waarvan € 42 direct en € 19,40 doorberekend indirect.
>
> **Grondslag**: [[volledige-kostencalculatie]] §sommatie, [[kostprijs-per-eenheid]]
>
> **Redenering**: Drie productiecentra met elk een eigen opslag-tarief; trapsgewijze verdeling van indirect levert kost per eenheid op die zowel voor balans (mits scope vervaardigingsprijs) als voor prijszetting bruikbaar is.


## Gebaseerd op concepten

[[volledige-kostencalculatie]] · [[directe-kosten]] · [[indirecte-kosten]] · [[variabele-kosten]] · [[vaste-kosten]] · [[kostencentrum]] · [[kostendrager]] · [[verdeelsleutel]] · [[kostprijs-per-eenheid]] · [[vervaardigingsprijs]]
## Voortkomend uit

- **Taken**: 1.8.taak.1
- **Kenniselementen**: 1.8.III, 1.8.III.A, 1.8.II, 1.8.II.A
