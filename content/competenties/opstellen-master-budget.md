---
title: Opstellen van een master-budget (operationeel + financieel)
tags:
- competentie
- po-1-8
programmaonderdelen:
- '1.8'
status: voorgesteld
schema_version: '1.1'
gegenereerd_uit: data/concepten/competenties/opstellen-master-budget.yaml
gegenereerd_op: '2026-05-17'
---
# Opstellen van een master-budget (operationeel + financieel)

**⚖️ 5% · 🤖 95%**

> Budgetbeheer en master-budget zijn integraal vakdoctrine. Het enige wettelijke raakpunt is dat het bestuursorgaan via WVV-bepalingen (bv. art. 7:228, 5:153) een alarmbelprocedure moet starten wanneer het netto-actief dreigt onder kritieke drempels te dalen — daarbij is een budget vaak praktisch instrument, maar niet wettelijk verplicht. Vereist mens-review wegens praktijk_pct > 70%.

## Aanbevolen werkwijze

### 1. Plannen van de budgetcyclus en uitgangspunten

Bepaal de horizon (jaarbudget, eventueel rolling-forecast), de granulariteit (per maand, per kwartaal) en de top-down/bottom-up-mix.

**Waarom?** Zonder afgesproken cyclus en uitgangspunten loopt het budgetproces vast in onderhandelingen en blijft het zonder eigenaarschap.

**📥 Input**:
- Strategisch plan + commerciële verwachtingen → **Groei-aannames, prijsbeleid** _(document)_
- Vorig jaar-budget + werkelijke cijfers → **Realisatie + verschillen** _(boekhoudkundig-bedrag)_

**📤 Output**:
- Budget-kalender + uitgangspuntennota → **Mijlpalen, verantwoordelijken, basisaannames** _(document)_

**🛠️ Hoe**:

1. Lees [[budget-cyclus]] §fasen: voorbereiden, opstellen, goedkeuren, opvolgen.
2. Definieer planninghorizon (typisch 12 maanden, eventueel rolling).
3. Documenteer basis-aannames (inflatie-index, loonindexering, energieprijs-scenario).
4. Plan de top-down-richtlijnen door directie en de bottom-up-input door
   afdelingsverantwoordelijken volgens [[budgetprocedure]] §participatie.


**Grondslag**: [[budget-cyclus]] §fasen, [[budgetprocedure]] §participatie, [[budgetbeheer]] §doel

### 2. Opstellen van het verkoop- en productiebudget

Bouw het verkoopbudget (volume × prijs per productlijn × periode) en leid daaruit het productiebudget af (rekening houdend met voorraadwijzigingen).

**Waarom?** Het verkoopbudget is het anker van het master-budget — alle andere onderdelen volgen uit het verwachte volume.

**📥 Input**:
- Marktanalyse + orderboek + sales-prognoses → **Volume + prijs per maand per productlijn** _(boekhoudkundig-bedrag)_

**📤 Output**:
- Verkoopbudget + productiebudget → **Volumes + omzet per periode** _(nieuwe-balanspost)_

**🛠️ Hoe**:

1. Bouw het verkoopbudget per productlijn per maand: volume × verkoopprijs.
2. Productie-volume = verkoopvolume + eindvoorraad gewenst − aanvangsvoorraad.
3. Splits productievolume per kostencentrum (Spinnerij/Weverij/Confectie bij
   Yperse Werkplaats BV).
4. Documenteer de aannames (sales-conversiepercentage, seizoenseffect).


> [!example]- Voorbeeld: Yperse Werkplaats BV — jaarverkoopbudget tapijt-standaard: 25.000 stuks à € 60
> Yperse Werkplaats BV — jaarverkoopbudget tapijt-standaard: 25.000 stuks à € 60.
>
> 1. **Verkoopbudget tapijt-standaard** 📊
>
>    | Kwartaal | Volume (stuks) | Omzet         |
>    |----------|---------------:|--------------:|
>    | Q1       |  5.000         | €   300.000   |
>    | Q2       |  6.500         | €   390.000   |
>    | Q3       |  6.000         | €   360.000   |
>    | Q4       |  7.500         | €   450.000   |
>    | **Totaal** | **25.000**   | **€ 1.500.000** |
>    
>

**Grondslag**: [[master-budget]] §verkoopbudget, [[budgetprocedure]] §uitgangspunten

### 3. Opstellen van de afgeleide operationele budgetten

Bouw uit het productie-budget de afgeleide budgetten: inkoop grondstoffen, directe arbeid, indirecte productiekosten, commerciële + administratieve kosten.

**Waarom?** Pas dan staat de volledige bedrijfskostenstructuur op tafel — operationeel budget = verkoop − totale operationele kosten.

**📥 Input**:
- Productiebudget uit stap 2 → **Volume per centrum** _(boekhoudkundig-bedrag)_
- Normverbruik en standaard-tarieven → **Kg/uur per eenheid, € per kg, € per uur** _(boekhoudkundig-bedrag)_

**📤 Output**:
- Vier afgeleide budgetten → **Inkoop, arbeid, indirect, S&A** _(nieuwe-balanspost)_

**🛠️ Hoe**:

1. Inkoopbudget = productievolume × normverbruik × inkoopprijs (verhoog met
   wenselijke voorraadtoename).
2. Arbeidsbudget = productievolume × normuren × standaard-uurtarief
   (€ 25/u bij Yperse).
3. Indirect-productie-budget per kostencentrum volgens
   [[toepassen-volledige-kostencalculatie]] stap 2-3.
4. Commercieel + administratief budget op basis van vorig jaar + indexering.


**Grondslag**: [[master-budget]] §afgeleide-budgetten, [[volledige-kostencalculatie]] §toewijzing-naar-drager, [[budgetprocedure]] §participatie

### 4. Bouwen van het financiële luik (cashflow + budget-balans + budget-RR)

Vertaal de operationele budgetten naar een budget-kasstroomoverzicht, een budget-balans en een budget-resultatenrekening.

**Waarom?** Het financiële luik toont of de operationele plannen leiden tot positieve cashflow, gezonde solvabiliteit en winstgevendheid.

**📥 Input**:
- Operationele budgetten uit stap 3 → **Verkoop, inkoop, arbeid, etc.** _(boekhoudkundig-bedrag)_
- Openingsbalans → **Vorderingen + schulden + kas** _(boekhoudkundig-bedrag)_

**📤 Output**:
- Master-budget-bundel → **Cashflow, balans, RR per kwartaal** _(nieuwe-balanspost)_

**🛠️ Hoe**:

1. Budget-RR: omzet − variabele kosten − vaste kosten − belasting = budget-resultaat.
2. Cashflow-budget: omzet × inning-pattern − inkopen × betaal-pattern − salarissen
   − BTW − belastingen − investeringen = netto kasstroom.
3. Budget-balans: openingsbalans + budgetbewegingen volgens
   [[master-budget]] §integratie-RR-en-balans.
4. Test: dekt cashflow alle kasuitgaven? Anders kredietlijn of timing aanpassen.


> [!example]- Voorbeeld: Yperse Werkplaats BV — geconsolideerd master-budget jaar 20X2
> Yperse Werkplaats BV — geconsolideerd master-budget jaar 20X2.
>
> 1. **Budget-RR (samenvatting)** 📊
>
>    | Component                | Bedrag         |
>    |--------------------------|---------------:|
>    | Omzet                    | € 1.500.000    |
>    | − Variabele kosten       | € 325.000      |
>    | **Contributiemarge**     | **€ 1.175.000** |
>    | − Vaste kosten           | € 800.000      |
>    | **Bedrijfsresultaat**    | **€ 375.000**  |
>    | − Belasting (25 %)       | € 93.750       |
>    | **Netto resultaat**      | **€ 281.250**  |
>    
>

**Grondslag**: [[master-budget]] §integratie-RR-en-balans, [[budget-cyclus]] §financieel-luik

### 5. Beslissen statisch versus flexibel + goedkeuren

Beslis of het budget statisch (één volume) of flexibel (meerdere volume-scenario's) wordt opgevolgd en laat het door directie of bestuur formeel goedkeuren.

**Waarom?** Statisch en flexibel hebben elk eigen sturings-toepassing; zonder formele goedkeuring blijft het budget vrijblijvend.

**📥 Input**:
- Master-budget-draft uit stap 4 → **Volledige bundel** _(document)_
- Verwachte volume-variabiliteit → **Bandbreedte** _(document)_

**📤 Output**:
- Goedgekeurd master-budget → **Statisch of flexibel + bandbreedte** _(document)_

**🛠️ Hoe**:

1. Vergelijk [[statisch-budget]] (één volume, snel maar starre referentie) tegen
   [[flexibel-budget]] (meerdere niveaus, beter voor variantie-analyse achteraf).
2. Voor stabiele productie: statisch budget volstaat.
3. Voor seizoenale of grillige vraag: flexibel met range bv. 80 %–120 % van baseline.
4. Leg goedkeuringstraject vast in raadsbesluit; communiceer aan afdelings-
   verantwoordelijken samen met hun deel-budget.


**Grondslag**: [[statisch-budget]], [[flexibel-budget]], [[master-budget]] §goedkeuring

> [!warning]- Plan vooraf welke variantie-versie van het budget gebruikt zal worden bij verschillen-analyse achteraf.
>
> _Vaak fout gedaan_: Statisch budget bouwen en achteraf willen flexibiliseren — leidt tot inconsistente verschillen-analyse.
>
> _Grondslag_: [[flexibel-budget]] §gebruik-in-variantie-analyse


## Voorbeelden

> [!example]- Yperse Werkplaats BV bouwt het jaarbudget 20X2: verkoop 25.000 tapijten à € 60, vaste kosten € 800.000
> **Conclusie**: Master-budget met budget-RR (netto resultaat € 281.250), positieve cashflow per kwartaal, statisch budget gekozen wegens stabiele productie.
>
> **Grondslag**: [[master-budget]] §integratie-RR-en-balans, [[statisch-budget]]
>
> **Redenering**: Productie volgt stabiele jaarprognose; geen seizoenpieken meer dan ± 25 %, dus statisch budget is bruikbaar zonder informatieverlies.


## Gebaseerd op concepten

[[master-budget]] · [[budgetbeheer]] · [[budgetprocedure]] · [[budget-cyclus]] · [[statisch-budget]] · [[flexibel-budget]] · [[vaste-kosten]] · [[variabele-kosten]] · [[volledige-kostencalculatie]]
## Voortkomend uit

- **Taken**: 1.8.taak.1
- **Kenniselementen**: 1.8.V, 1.8.VI, 1.8.VI.A, 1.8.VI.B, 1.8.VI.C, 1.8.VI.D
