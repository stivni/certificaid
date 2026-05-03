---
tags: ["1.5", wip, competentie]
niveau: integratie
status: draft
bouwversie: 2
programmaonderdelen: ["1.5", "1.4"]
itaa-lex-secties:
  - EU (Verordening 1606/2002, Richtlijn 2013/34/EU)
  - XV (WVV art. 3:1, 3:30; KB WVV art. 3:1)
procedure-grondslag: "Verordening (EG) 1606/2002 + KB WVV — wettelijk genormeerd toepassingskader"
---

# IFRS-toepassingskader bepalen

Voor een gegeven entiteit vaststellen welk **boekhoudkader** van toepassing is op haar enkelvoudige jaarrekening en haar geconsolideerde jaarrekening: Belgisch GAAP, IFRS verplicht, of IFRS optioneel. Deze beoordeling is een vereiste **eerste stap** vóór elke jaarrekeningopdracht voor entiteiten die mogelijk onder IFRS vallen — een verkeerd kader betekent een fundamenteel verkeerde jaarrekening.

> [!info]- Grondslag van deze werkwijze (⚖️ 100%)
>
> Deze werkwijze volgt rechtstreeks uit [Verordening (EG) 1606/2002](https://eur-lex.europa.eu/legal-content/NL/TXT/?uri=CELEX:32002R1606) art. 4-5 (toepassingsgebied IFRS) en [[bronnen/wetteksten/XV-KB-wvv|KB WVV]] art. 3:1 en 3:30. Geen analytische conventie — de regels zijn dwingend en gespecificeerd in de wettekst.

## Aanbevolen werkwijze

### 1. 🔍 Type jaarrekening identificeren

> 📥 **Nodig**:
> - Doel van de jaarrekening (statutair / consolidatie / managementsrapportering)
> - Rechtsvorm en juridische structuur van de entiteit
>
> 📤 **Uitkomst**:
> - Type jaarrekening: **enkelvoudig (statutair)** of **geconsolideerd**

**Waarom**: het toepassingskader hangt eerst en vooral af van het *type* jaarrekening, niet van de entiteit zelf. Eenzelfde groep maakt zowel een enkelvoudige als een geconsolideerde jaarrekening, met mogelijk verschillende kaders.

- **Enkelvoudige jaarrekening**: de jaarrekening van één rechtspersoon op basis van haar eigen boekhouding — wettelijk verplicht voor elke vennootschap met rechtspersoonlijkheid en elke vzw die boekhoudplichtig is ([[bronnen/wetteksten/XV-wvv#art-31|WVV art. 3:1]])
- **Geconsolideerde jaarrekening**: jaarrekening die de moedervennootschap met haar dochterondernemingen alsof het één economische entiteit betreft consolideert ([[bronnen/wetteksten/XV-wvv|WVV art. 3:23]])

> [!info]- Concreet: KBC Group NV
>
> KBC Group NV produceert jaarlijks twee jaarrekeningen die elk een eigen kader volgen:
> 1. **Enkelvoudige (statutaire) jaarrekening van KBC Group NV** alleen — basis voor dividend en vennootschapsbelasting
> 2. **Geconsolideerde jaarrekening** van KBC Group + alle dochters wereldwijd — basis voor beurscommunicatie en ratings
>
> 🤖 *AI-aanvulling*

### 2. 🔀 Notering controleren

> 📥 **Nodig**:
> - Type jaarrekening (stap 1)
> - Lijst van uitgegeven effecten (aandelen, obligaties)
> - Beurzen waarop deze effecten zijn toegelaten
>
> 📤 **Uitkomst**:
> - Status: **genoteerd op een gereglementeerde EU-markt** of **niet-genoteerd**

**Waarom**: notering op een gereglementeerde EU-markt activeert de **dwingende** IFRS-toepassing voor de geconsolideerde jaarrekening — ongeacht groottecriteria of andere overwegingen.

**Gereglementeerde EU-markten** (Richtlijn 2014/65/EU, MiFID II):
- Euronext Brussels, Amsterdam, Paris, Lisbon, Dublin, Oslo, Milan
- Deutsche Börse (Frankfurt)
- London Stock Exchange (UK — sinds Brexit niet meer EU)
- Nasdaq Stockholm, Helsinki, Copenhagen
- BME (Madrid)
- Wiener Börse, en andere

**Niet** gereglementeerde markten (verplichten geen IFRS):
- Multilaterale handelsfaciliteiten (MTF, bv. Euronext Growth)
- OTC-markten
- Crowdfundingplatformen

> [!warning]- Notering op een MTF activeert IFRS niet
> ❌ *"Een vennootschap met aandelen op Euronext Growth moet IFRS toepassen."*
>
> Verordening 1606/2002 art. 4 koppelt de IFRS-verplichting aan **gereglementeerde markten** in de zin van Richtlijn 2014/65/EU (MiFID II). Multilaterale handelsfaciliteiten (MTF) zoals **Euronext Growth** of **Euronext Access** vallen daar niet onder. Een vennootschap die enkel op zo'n MTF noteert, blijft Belgisch GAAP toepassen voor haar geconsolideerde rekeningen — tenzij ze vrijwillig voor IFRS kiest.
>
> 🤖 *AI-aanvulling op basis van Verord. 1606/2002 art. 4 + Richtlijn 2014/65/EU*

### 3. 🔀 Kader bepalen voor de jaarrekening

> 📥 **Nodig**:
> - Type jaarrekening (stap 1)
> - Notering (stap 2)
>
> 📤 **Uitkomst**:
> - Toepasselijk kader: **Belgisch GAAP**, **IFRS verplicht**, of **IFRS optioneel** (met keuzemoment)

**Waarom**: de wet geeft een gesloten matrix — er is geen ruimte voor afwijkingen, behalve waar uitdrukkelijk toegestaan.

```
                    Genoteerd op EU-          Niet-genoteerd
                    gereglementeerde markt
─────────────────── ────────────────────── ───────────────────────
Geconsolideerd      IFRS VERPLICHT          IFRS OPTIONEEL — eens
                    (Verord. 1606/2002      gekozen onomkeerbaar
                    art. 4)                 (KB WVV art. 3:30)

Enkelvoudig         Belgisch GAAP           Belgisch GAAP
(statutair BE)      (KB WVV — IFRS niet     (KB WVV — IFRS niet
                    toegestaan)             toegestaan)
```

Toelichting per cel:

- **Genoteerd, geconsolideerd**: IFRS is **verplicht** sinds 2005 ([[ifrs-rechtskader#-verordening-eg-nr-16062002|Verordening 1606/2002]]). De entiteit kan niet kiezen.
- **Niet-genoteerd, geconsolideerd**: IFRS is **optioneel**. België heeft de lidstaatoptie van Verord. 1606/2002 art. 5 geactiveerd via [[bronnen/wetteksten/XV-KB-wvv|KB WVV art. 3:30]]. **Eenmaal gekozen** is de keuze in principe onomkeerbaar — terugkeer naar Belgisch GAAP enkel mogelijk in uitzonderlijke omstandigheden, met motivatie.
- **Enkelvoudig (Belgische statutaire jaarrekening)**: **altijd Belgisch GAAP**, ongeacht notering. IFRS is **niet toegestaan** voor de Belgische statutaire jaarrekening, omdat die als basis dient voor:
  - Dividenduitkering (uitkeerbaar resultaat onder Belgisch concept)
  - Vennootschapsbelasting (fiscale balans afgeleid van boekhoudkundige balans)
  - Alarmbelprocedure (nettoactief volgens Belgisch GAAP)
  - Groottecriteria (drempelwaarden meten op Belgisch GAAP-cijfers)

> [!warning]- IFRS vervangt nooit de Belgische statutaire jaarrekening
> ❌ *"Een Belgische dochter van een IFRS-groep mag haar statutaire jaarrekening in IFRS opstellen."*
>
> De Belgische dochter blijft **statutair Belgisch GAAP** toepassen voor haar NBB-neerlegging en fiscale aangifte. Voor de IFRS-consolidatie van de moedergroep worden de Belgische cijfers via consolidatieboekingen omgezet naar IFRS — die omzetting bestaat enkel in de consolidatie, niet in de individuele boekhouding.
>
> 🤖 *AI-aanvulling op basis van Verord. 1606/2002 + KB WVV*

> [!info]- Concreet: niet-genoteerde groep kiest IFRS
>
> Een Belgische niet-genoteerde groep met dochters in 6 EU-landen overweegt IFRS voor de geconsolideerde jaarrekening, omdat haar bankenpool dat als rapporteringsstandaard verlangt voor een nieuwe €100M kredietlijn.
>
> Beslissingstraject:
> 1. KB WVV art. 3:30 staat de keuze toe — **OK**
> 2. Eenmaal gekozen, blijft de IFRS-keuze in principe onomkeerbaar — financiële impact moet vooraf worden ingeschat (extra rapporteringskost, training, interne audit)
> 3. **Statutaire jaarrekening** van de moeder en alle Belgische dochters blijft Belgisch GAAP — hier verandert niets
>
> Vermelding van de keuze in het jaarverslag en in de toelichting bij de eerste IFRS-geconsolideerde jaarrekening — overgang volgens [[presentatie-jaarrekening-ifrs#-eerste-toepassing-van-ifrs-ifrs-1|IFRS 1: First-time adoption]].
>
> 🤖 *AI-aanvulling*

### 4. 🔀 Eerste toepassing checken

> 📥 **Nodig**:
> - Toepasselijk kader (stap 3)
> - Geschiedenis: heeft de entiteit eerder al onder dit kader gerapporteerd?
>
> 📤 **Uitkomst**:
> - Status: **first-time adoption** of **continuing application**
> - Indien first-time: transitiedatum vastgelegd

**Waarom**: een entiteit die voor het eerst IFRS toepast, valt onder een specifieke standaard ([[presentatie-jaarrekening-ifrs#-eerste-toepassing-van-ifrs-ifrs-1|IFRS 1]]) die de overgang structureert. Dit heeft gevolgen voor de timing en de werklast van de opdracht.

- **Continuing application**: de entiteit past het kader al toe → enkel jaarlijkse update
- **First-time adoption** (IFRS 1):
  - **Transitiedatum** = begin van de vroegste vergelijkende periode in de eerste IFRS-jaarrekening
  - Opening IFRS-balans op transitiedatum opstellen
  - Reconciliatietabellen opstellen (eigen vermogen, totaalresultaat) tussen vorig kader en IFRS

### 5. 💬 Conclusie en planning

> 📥 **Nodig**:
> - Toepasselijke kaders per type jaarrekening (stap 3)
> - First-time vs. continuing (stap 4)
>
> 📤 **Uitkomst**:
> - Schriftelijk advies aan cliënt: welke jaarrekeningen zijn vereist, in welk kader, en met welke timing
> - Inschatting van de bijkomende werkzaamheden bij IFRS (eerste toepassing of jaarlijkse update)

**Waarom**: de uitkomst van de toepassingskaderbepaling is geen *technische* bevinding — het bepaalt het volledige werkprogramma van de opdracht en stuurt verwachtingen bij de cliënt. Conclusie expliciet en schriftelijk vastleggen voorkomt latere discussies over scope en honorarium.

Beantwoord in de conclusie:
- **Hoeveel jaarrekeningen** moet de entiteit produceren? (1 of 2)
- **Welk kader** geldt voor elke jaarrekening?
- **Wie controleert** elke jaarrekening? (commissaris voor statutaire grote vennootschap; auditrapport IFRS bij genoteerde groep)
- **Welke deadlines** gelden?

## Voorbeelden

> [!example]- Beursgenoteerde Belgische groep
>
> **Situatie**: Solvay NV — Belgische chemiegroep, genoteerd op Euronext Brussels en Paris. Heeft 60+ dochterondernemingen wereldwijd.
>
> **Conclusie**:
> - **Geconsolideerde jaarrekening**: IFRS verplicht
> - **Enkelvoudige (statutaire) jaarrekening**: Belgisch GAAP (KB WVV)
> - Elke Belgische dochter: eigen statutaire jaarrekening Belgisch GAAP, neerlegging NBB
>
> **Grondslag**:
> - [[ifrs-rechtskader#-verordening-eg-nr-16062002|Verordening 1606/2002]] art. 4 — IFRS verplicht voor geconsolideerde rekeningen van EU-genoteerde vennootschappen
> - [[bronnen/wetteksten/XV-KB-wvv|KB WVV art. 3:1]] — statutaire jaarrekening volgens Belgisch GAAP, IFRS niet toegestaan
>
> **Redenering**: Solvay NV is genoteerd → IFRS verplicht voor consolidatie. De statutaire jaarrekening blijft Belgisch GAAP omdat dividend, vennootschapsbelasting en alarmbelprocedure die als referentie nemen. Beide jaarrekeningen worden gepubliceerd, met aparte controleverklaringen.
>
> 🤖 *AI-aanvulling*

> [!example]- Niet-genoteerde KMO-groep
>
> **Situatie**: een Belgische niet-genoteerde holding met 4 industriële dochters in BE, NL, FR. Geen extern kapitaal (familieaandeelhouder). Bankrelatie verlangt geen specifieke standaard.
>
> **Conclusie**:
> - **Geconsolideerde jaarrekening**: Belgisch GAAP volstaat (consolidatieplicht volgt uit groottecriteria, kader is keuzevrij — IFRS optioneel maar niet vereist)
> - **Enkelvoudige (statutaire) jaarrekening**: Belgisch GAAP voor moeder + Belgische dochters; lokale GAAP voor NL en FR dochters
>
> **Grondslag**:
> - [[ifrs-rechtskader#-toepassingsgebied-van-ifrs-in-belgië|Toepassingsgebied IFRS in België]]
> - [[bronnen/wetteksten/XV-KB-wvv|KB WVV art. 3:30]] — IFRS is een optie voor niet-genoteerde geconsolideerde rekeningen
>
> **Redenering**: zonder noteringsplicht en zonder externe vereiste, is Belgisch GAAP de meest economische keuze. IFRS-conversie zou jaarlijks ~5-10% extra rapporteringskost veroorzaken zonder duidelijke meerwaarde — wel een serieuze drempel om later via IPO de markten op te gaan.
>
> 🤖 *AI-aanvulling*

## Motiveren op het examen

**Een volledig antwoord bevat:**
1. **Type jaarrekening** identificeren (enkelvoudig of geconsolideerd)
2. **Notering** verifiëren — gereglementeerde EU-markt of niet
3. Het **kader** afleiden uit de matrix (Belgisch GAAP / IFRS verplicht / IFRS optioneel)
4. Bevestigen dat de **statutaire jaarrekening** altijd Belgisch GAAP blijft
5. Verwijzen naar de wettelijke grondslag: Verordening 1606/2002 of KB WVV art. 3:30

**Voorbeeldvragen**

> [!question]- Welke jaarrekeningen moet een genoteerde groep produceren?
>
> Een Belgische vennootschap is genoteerd op Euronext Brussels. Welk(e) jaarrekeningkader(s) moet zij toepassen, en voor welk(e) jaarrekening(en)?
>
> > [!success]- Antwoord
> >
> > **Twee jaarrekeningen, twee kaders.**
> >
> > 1. **Geconsolideerde jaarrekening: IFRS verplicht** krachtens [Verordening (EG) 1606/2002](https://eur-lex.europa.eu/legal-content/NL/TXT/?uri=CELEX:32002R1606) art. 4 — gevolg van notering op gereglementeerde EU-markt.
> > 2. **Enkelvoudige (statutaire) jaarrekening: Belgisch GAAP** volgens [[bronnen/wetteksten/XV-KB-wvv|KB WVV]] — IFRS is **niet** toegestaan voor de Belgische statutaire jaarrekening, omdat die als basis dient voor dividend, vennootschapsbelasting, alarmbelprocedure en groottecriteria.
> >
> > De controleverklaring van de commissaris staat in beide jaarrekeningen — twee controles, twee referentiekaders.
> >
> > *Zie: [[ifrs-toepassingskader-bepalen|stap 3: Kader bepalen]]*
>
> 🤖 *AI-aanvulling*
