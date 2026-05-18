---
title: Toepassen van de ABC-methode (Activity Based Costing) op een productlijn
tags:
- competentie
- po-1-8
programmaonderdelen:
- '1.8'
status: voorgesteld
schema_version: '1.5'
gegenereerd_uit: data/concepten/records/toepassen-abc-methode-op-productlijn.json
gegenereerd_op: '2026-05-18'
---
# Toepassen van de ABC-methode (Activity Based Costing) op een productlijn

**⚖️ 5% · 🤖 95%**

> ABC-methode is internationale vakdoctrine (Cooper-Kaplan) zonder Belgische trusted wettelijke of CBN-bron. Wettelijk raakvlak is enkel dat een ABC-toerekening kan dienen als 'evenredig deel' indirecte productiekosten conform KB 21.10.2018 art. 22, mits consistent toegepast. Vereist mens-review wegens praktijk_pct > 70%.

## Aanbevolen werkwijze

### 1. Identificeren van de activiteiten in het productieproces

Breek het productieproces op in afgebakende activiteiten — herhalende handelingen of stappen die resources consumeren.

**Waarom?** Activiteit (niet kostencentrum) is het hart van ABC; alleen op activiteit-niveau is de oorzaak-gevolg-relatie scherp genoeg om verdeelsleutels te kiezen.

**📥 Input**:
- Procesbeschrijving + workflow → **Stappen per productlijn** _(document)_

**📤 Output**:
- Activiteiten-lijst → **5-15 activiteiten met scope-omschrijving** _(document)_

**🛠️ Hoe**:

1. Volg [[abc-methode]] §activiteit-identificatie: lijst activiteiten op die
   resources verbruiken en die per output verschillen (machine-instellen, kwaliteitscontrole,
   order-verwerking, transport tussen centra).
2. Vermijd te grove activiteiten (verliezen onderscheidend vermogen) en
   te fijne (administratieve last).
3. Voor Yperse Werkplaats BV bijvoorbeeld: machine-instelling, weven,
   afwerken, kwaliteitscontrole, ompakken, verzending.


**Grondslag**: [[abc-methode]] §activiteit-identificatie

### 2. Kiezen van een cost-driver per activiteit

Selecteer per activiteit een cost-driver — een meeteenheid die het verbruik van de activiteit weerspiegelt.

**Waarom?** De cost-driver bepaalt hoe activiteitskost aan een product wordt toegerekend; verkeerde keuze = verkeerde kostprijs.

**📥 Input**:
- Activiteiten-lijst uit stap 1 → **Per activiteit + omschrijving** _(document)_
- Procesmetingen → **Wat varieert per product (aantal instellingen, aantal orders, ...)** _(boekhoudkundig-bedrag)_

**📤 Output**:
- Tabel activiteit × cost-driver → **Per activiteit een driver + meeteenheid** _(document)_

**🛠️ Hoe**:

1. Volg [[abc-methode]] §cost-driver-keuze: kies een driver met sterke
   oorzakelijkheid en meetbaarheid.
2. Drie types drivers:
   - Transactional (aantal voorbereidingen, aantal orders).
   - Duration (uren machine-instelling).
   - Intensity (specifiek verbruik per uitvoering).
3. Test causaliteit: stijgt de activiteitskost als de driver-waarde stijgt?
4. Documenteer de driver-keuze met motivering — vermijd 'machine-uren-voor-alles'.


**Grondslag**: [[abc-methode]] §cost-driver-keuze, [[verdeelsleutel]] §oorzakelijkheidsprincipe

### 3. Berekenen van het cost-driver-tarief per activiteit

Bereken per activiteit: tarief = totaal activiteitskost / totaal driver-eenheden.

**Waarom?** Dit tarief is de prijs van één eenheid driver — de basis voor toerekening aan dragers.

**📥 Input**:
- Activiteitskost per soort → **Bedragen toegewezen aan activiteit** _(boekhoudkundig-bedrag)_
- Totale driver-eenheden → **Aantal per periode** _(boekhoudkundig-bedrag)_

**📤 Output**:
- Cost-driver-tarief per activiteit → **€ per eenheid driver** _(boekhoudkundig-bedrag)_

**🛠️ Hoe**:

1. Verzamel de totale kost per activiteit uit klasse-9-rekeningen of uit
   interviews + tijds-allocaties.
2. Tel de driver-eenheden over de periode op (bv. 200 machine-instellingen per jaar).
3. Tarief = totaalkost / totaal driver-eenheden.
4. Verifieer de tarieven op redelijkheid (vergelijk met externe benchmarks).


**Grondslag**: [[abc-methode]] §tarief-per-driver

### 4. Toewijzen aan kostendragers (producten of orders)

Vermenigvuldig per product/order/klant het verbruik van elke activiteit met het bijbehorende cost-driver-tarief.

**Waarom?** Dit geeft de echte ABC-kostprijs: niet één opslag per productiecentrum, maar een gestaffelde toerekening op basis van werkelijk activiteitsverbruik.

**📥 Input**:
- Cost-driver-tarieven uit stap 3 → **€ per eenheid driver** _(boekhoudkundig-bedrag)_
- Verbruik per product per activiteit → **Aantal driver-eenheden per product** _(boekhoudkundig-bedrag)_

**📤 Output**:
- ABC-kostprijs per kostendrager → **Direct + per activiteit + totaal** _(nieuwe-balanspost)_

**🛠️ Hoe**:

1. Volg [[abc-methode]] §toerekening: per kostendrager × per activiteit:
   kost = driver-verbruik × cost-driver-tarief.
2. Tel toegerekende activiteitskosten op + direct toewijsbare kosten
   (materiaal + directe arbeid).
3. Vergelijk met de uitkomst van traditionele [[volledige-kostencalculatie]] op één
   opslagbasis — toon waar de twee uitkomsten significant verschillen
   (typisch: laag-volume specialiteiten worden onder traditioneel onderbelast).


> [!example]- Voorbeeld: Yperse Werkplaats BV — vergelijking kostprijs voor twee productlijnen (tapijt-standaard 25.000 stuks/jaar en kleed-handg…
> Yperse Werkplaats BV — vergelijking kostprijs voor twee productlijnen (tapijt-standaard 25.000 stuks/jaar en kleed-handgeknoopt 500 stuks/jaar) met de traditionele methode versus ABC. Indirecte productiekost in totaal € 800.000.
>
> 1. **Traditionele toewijzing (één opslag op machine-uren)** 🧮
>
>    Totaal machine-uren = 25.000 × 0,4 + 500 × 1,2 = 10.600 uur
>    
>    Tarief = € 800.000 / 10.600 u = € 75,47/mach-uur
>    
>    Indirect tapijt-standaard = 0,4 u × € 75,47 = **€ 30,19**
>    
>    Indirect kleed-handgeknoopt = 1,2 u × € 75,47 = **€ 90,57**
>    
>
> 2. **ABC-toewijzing** 🧮
>
>    | Activiteit             | Tarief         | Verbruik standaard | Verbruik luxe  |
>    |------------------------|---------------:|-------------------:|---------------:|
>    | Machine-instelling     | € 600/instelling | 1 / 100 stuks    | 1 / 5 stuks    |
>    | Weven (uur)            | € 35/mach-uur  | 0,4 uur            | 1,2 uur        |
>    | Kwaliteitscontrole     | € 8/eenheid    | 1                  | 1              |
>    | Afwerking (uur)        | € 60/arb-uur   | 0,1 uur            | 1,5 uur        |
>    | Verzending             | € 15/order     | 1/50 stuks         | 1/2 stuks      |
>    
>    Indirect tapijt-standaard
>      = € 600/100 + 0,4×35 + 8 + 0,1×60 + 15/50
>      = € 6 + € 14 + € 8 + € 6 + € 0,30 = **€ 34,30**
>    
>    Indirect kleed-handgeknoopt
>      = € 600/5 + 1,2×35 + 8 + 1,5×60 + 15/2
>      = € 120 + € 42 + € 8 + € 90 + € 7,50 = **€ 267,50**
>    
>
> 3. **Verschil-interpretatie** 💬
>
>    Traditioneel: standaard € 30,19, luxe € 90,57.
>    ABC: standaard € 34,30, luxe € 267,50.
>    
>    Luxe-product werd onder traditioneel ernstig onderschat (€ 90 vs. € 267,50)
>    omdat het veel meer voorbereidingen, kwaliteitscontroles en small-batch-
>    verzendingen vergt — typische ABC-bevinding voor laag-volume specialiteiten.
>    
>

**Grondslag**: [[abc-methode]] §toerekening, [[costing-methodes-vergelijking]] §ABC-vs-traditioneel

### 5. Interpreteren en stuurinformatie afleiden

Vertaal de ABC-resultaten naar concrete management-acties: productmix-keuze, prijsbeleid, proces-rationalisatie.

**Waarom?** ABC heeft pas waarde als de resultaten beslissingen sturen — anders is het een dure rekening-oefening.

**📥 Input**:
- ABC-kostprijzen uit stap 4 → **Per product** _(boekhoudkundig-bedrag)_
- Verkoopprijzen + volumes → **€ per stuk + aantal** _(boekhoudkundig-bedrag)_

**📤 Output**:
- Stuurnota met conclusies → **Prijs- of productmix-acties** _(conclusie)_

**🛠️ Hoe**:

1. Vergelijk ABC-kostprijs met verkoopprijs: identificeer verlies-makende
   producten die onder traditionele kostprijs winstgevend leken.
2. Bekijk activiteit-drivers met hoogste totaalkost: kunnen die geëlimineerd
   of geautomatiseerd worden?
3. Onderzoek of orderbeleid wijzigt: minimum-batch-groottes invoeren als
   machine-instelling de grote driver is.
4. Documenteer aanbevelingen + verwachte impact.


**Grondslag**: [[abc-methode]] §interpretatie

> [!warning]- Pas ABC selectief toe op productlijnen of beslissingen waar de extra precisie waarde toevoegt.
>
> _Vaak fout gedaan_: ABC opzetten voor het volledige bedrijf — administratief overweldigend en zelden onderhouden.
>
> _Grondslag_: [[abc-methode]] §scope-beperking

> [!warning]- Test elke driver op causale stabiliteit voordat je tarieven berekent.
>
> _Vaak fout gedaan_: Een driver kiezen op administratief gemak (bv. tijd geboekt) zonder oorzakelijke band met de activiteit.
>
> _Grondslag_: [[abc-methode]] §cost-driver-keuze


## Voorbeelden

> [!example]- Yperse Werkplaats BV — productmix tapijt-standaard (25.000 stuks) versus kleed-handgeknoopt (500 stuks)
> **Conclusie**: Traditioneel onderschatte kleed-handgeknoopt met € 177 per stuk (€ 90,57 traditioneel vs. € 267,50 ABC). Aanbeveling: prijs verhogen of minimum-batch-grootte invoeren voor de handgeknoopte productlijn.
>
> **Grondslag**: [[abc-methode]] §toerekening, [[costing-methodes-vergelijking]] §ABC-vs-traditioneel
>
> **Redenering**: Laag-volume specialiteit vergt veel set-up en kwaliteitscontrole per eenheid; één globale opslag op machine-uren maskeert die complexiteit volledig.


## Gebaseerd op concepten

[[abc-methode]] · [[indirecte-kosten]] · [[volledige-kostencalculatie]] · [[verdeelsleutel]] · [[kostprijs-per-eenheid]] · [[kostendrager]] · [[overige-kosten]] · [[costing-methodes-vergelijking]]
## Voortkomend uit

- **Taken**: 1.8.taak.1
- **Kenniselementen**: 1.8.III, 1.8.III.F, 1.8.II.A, 1.8.II.D
