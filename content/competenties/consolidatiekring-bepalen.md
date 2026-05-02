---
tags: ["1.4", wip, competentie]
niveau: toepassen
status: draft
programmaonderdelen: ["1.4"]
itaa-lex-secties:
  - XV (WVV art. 1:19, 1:21, 1:26, 3:22–3:29)
  - XV (KB) (KB-WVV art. 3:96–3:102)
bouwversie: 0
---

# Consolidatiekring bepalen

Vaststellen welke entiteiten deel uitmaken van de consolidatiekring en welke methode op elke entiteit van toepassing is — dit is de eerste stap vóór enige consolidatieberekening. De uitkomst is een gestructureerde lijst van alle te consolideren entiteiten met hun methode: integraal, evenredig of vermogensmutatie.

> [!info]- Grondslag van deze werkwijze (🤖 20% · ⚖️ 80%)
>
> De procedure volgt rechtstreeks uit het [[bronnen/wetteksten/XV-wvv|WVV]] (art. 3:23–3:27 voor de consolidatieplicht en vrijstellingen) en het [[bronnen/wetteksten/XV-KB-wvv|KB-WVV]] (art. 3:96–3:102 voor weglatingen en methodekeuze; art. 3:124 voor het vermoeden van invloed van betekenis). De volgorde van de stappen — eerst consolidatieplicht, dan type relatie per entiteit, dan weglatingen, dan documentatie — is een analytische conventie 🤖 die de wettelijke logica van algemeen kader naar concrete uitvoering volgt.

## Aanbevolen werkwijze

### 1. 🔍 Consolidatieverplichting nagaan

> 📥 **Nodig**:
> - Eigendomsstructuur van de vennootschap (aandeelhouderregister, statuten)
> - Financiële gegevens van de groep (balanstotaal, netto-omzet, werknemers)
>
> 📤 **Uitkomst**:
> - Oordeel: wel of geen consolidatieplicht

**Waarom**: zonder vaststelling van de consolidatieplicht wordt ofwel onnodig werk verricht (vrijgestelde groep), ofwel een wettelijke verplichting genegeerd. De plicht is bovendien niet-discretionair: zodra één vennootschap in de groep genoteerd is, vervallen alle vrijstellingen.

Bepaal of de vennootschap onderworpen is aan de consolidatieverplichting op basis van twee vragen:

**Vraag 1 — Is er een moeder-dochterrelatie of consortium?** Controleer of de vennootschap exclusieve of gezamenlijke controle uitoefent over één of meer dochterondernemingen, dan wel deel uitmaakt van een [[consolidatiekring#-consortium|consortium]]. ([[bronnen/wetteksten/XV-wvv#art-323|WVV art. 3:23–3:24]])

**Vraag 2 — Gelden vrijstellingen?** Indien een moeder-dochterrelatie of consortium bestaat, controleer dan of de vrijstelling voor [[consolidatiekring#-vrijstellingen-van-de-consolidatieverplichting|groepen van beperkte omvang]] (WVV art. 3:25) of de [[consolidatiekring#-vrijstellingen-van-de-consolidatieverplichting|vrijstelling als dochtervennootschap van hogere moeder]] (WVV art. 3:26) van toepassing is.

**Let op**: beide vrijstellingen vervallen zodra **één van de te consolideren vennootschappen is genoteerd** (WVV art. 3:27). Controleer dit altijd als eerste.

*(Grondslag: [[bronnen/wetteksten/XV-wvv#art-323|WVV art. 3:23–3:27]])*

> [!warning]- Een genoteerde vennootschap in de groep maakt alle vrijstellingen ongeldig
> ❌ *"De groep is klein genoeg voor de vrijstelling, dus hoeft er niet geconsolideerd te worden."*
>
> Zodra één vennootschap in de groep genoteerd is, vervallen alle vrijstellingen en geldt de consolidatieplicht ongeacht de omvang van de groep.
>
> 🤖 *AI-aanvulling*

### 2. 🔍 Type relatie per entiteit vaststellen

> 📥 **Nodig**:
> - Stemrechtpercentages per participatie
> - Aard van de controle (exclusief, gezamenlijk, invloed van betekenis)
>
> 📤 **Uitkomst**:
> - Per entiteit: type relatie (dochter / gemeenschappelijke dochter / geassocieerde vennootschap)

**Waarom**: het type controle bepaalt rechtstreeks welke consolidatiemethode wettelijk verplicht is. Een verkeerde classificatie (bv. evenredig waar integraal moet) leidt tot een materieel afwijkende geconsolideerde jaarrekening en een onjuiste weergave van de belangen van derden.

Beoordeel voor elke participatie het type relatie:

| Type relatie | Criterium | Methode |
|---|---|---|
| Exclusieve controle | Meerderheid stemrechten of feitelijke controle | Integrale consolidatie |
| Gezamenlijke controle | Contractueel gedeelde zeggenschap | Evenredige consolidatie |
| Invloed van betekenis | Vermoeden bij ≥ 20% stemrechten | Vermogensmutatiemethode |

*(Grondslag: [[bronnen/wetteksten/XV-KB-wvv#art-3124|KB-WVV art. 3:124]]; [[bronnen/wetteksten/XV-wvv#art-121|WVV art. 1:21]])*

> [!info]- Concreet: type relatie bepalen voor drie participaties
>
> ```
> Groep M heeft participaties in drie entiteiten:
>
> Entiteit A: M bezit 75% van de stemrechten
>   → Exclusieve controle → integrale consolidatie
>
> Entiteit B: M en N (ongelieerde partij) bezitten elk 50%, contractueel
>             overeengekomen dat beide partijen gezamenlijk beslissen
>   → Gezamenlijke controle → evenredige consolidatie
>
> Entiteit C: M bezit 25% van de stemrechten, geen bestuurszetel,
>             geen andere aanwijzingen van controle
>   → Vermoeden invloed van betekenis (≥20%) → vermogensmutatiemethode
> ```
>
> 🤖 *AI-aanvulling*

### 3. 🔀 Weglatingen en verplichte uitsluitingen beoordelen

> 📥 **Nodig**:
> - [[consolidatiekring-bepalen#2--type-relatie-per-entiteit-vaststellen|Type relatie per entiteit]]
> - Specifieke omstandigheden (omvang, beperkingen, vereffening, verkoopintentie)
>
> 📤 **Uitkomst**:
> - Per entiteit: opnemen in consolidatiekring of weglaten/uitsluiten, met motivering

**Waarom**: niet elke entiteit waarover controle bestaat moet effectief in de kring opgenomen worden. De wet voorziet specifieke weglatingsgronden (verwaarloosbaar, controlebeperkingen, vereffening) die een gemotiveerde keuze vereisen — een ongemotiveerde weglating maakt de geconsolideerde jaarrekening niet getrouw.

Doorloop elke dochteronderneming op mogelijke weglatingsgronden ([[bronnen/wetteksten/XV-KB-wvv#art-397|KB-WVV art. 3:97–3:100]]):

- **Verwaarloosbare betekenis**: individueel of gezamenlijk te verwaarloosbaar voor de beoordeling van het geconsolideerde vermogen/resultaat.
- **Effectieve controlebeperkingen**: ingrijpende en duurzame beperkingen belemmeren de uitoefening van controlebevoegdheid.
- **Onevenredige kosten of vertraging**: verkrijging van gegevens is niet haalbaar.
- **Uitsluitend met verkoopintentie**: aandelen worden gehouden voor latere vervreemding.
- **Vereffening of bedrijfsstop** (verplichte weglating): via vermogensmutatiemethode opnemen.

Elke weglating vergt **motivering in de toelichting**.

*(Grondslag: [[bronnen/wetteksten/XV-KB-wvv#art-397|KB-WVV art. 3:97–3:100]])*

### 4. 💬 Consolidatiekring documenteren

> 📥 **Nodig**:
> - [[consolidatiekring-bepalen#3--weglatingen-en-verplichte-uitsluitingen-beoordelen|Beslissingen per entiteit]]
>
> 📤 **Uitkomst**:
> - Definitieve consolidatiekring met methode per entiteit
> - Toelichting-tekst voor weglatingen en bijzondere gevallen

**Waarom**: de consolidatiekring is het fundament van alle volgende consolidatiewerken. Een onvolledige of fout gemotiveerde kring veroorzaakt fouten in elke daaropvolgende berekening — bovendien is de motivering van weglatingen wettelijk verplicht in de toelichting.

Stel een overzicht op van alle entiteiten:

```
Entiteit        | % bezit | Methode             | Opmerking
----------------|---------|---------------------|----------
Moeder M        | 100%    | consoliderende vnnt  |
Dochter D1      | 80%     | Integraal           | belangen derden = 20%
Dochter D2      | 100%    | Integraal           |
JV J1           | 50%     | Evenredig           | gezamenlijke controle met X
Associé A1      | 30%     | Vermogensmutatie    |
Dochter D3      | 60%     | Weglating (art. 97) | in vereffening → VM-methode
```

*(Grondslag: [[bronnen/wetteksten/XV-KB-wvv#art-396|KB-WVV art. 3:96]], [[bronnen/wetteksten/XV-KB-wvv#art-3102|art. 3:102]])*

## Voorbeelden

> [!example]- Groep met gemengde participatiestructuur
>
> **Situatie**: Holding H bezit:
> - 90% van Dochter D1
> - 50% van Joint Venture J (de andere 50% is in handen van externe partij X, met gezamenlijke controle contractueel vastgelegd)
> - 25% van Associé A (H heeft een zetel in de RvB maar geen controle)
> - 100% van D2 (in vereffening)
>
> **Conclusie**:
> - D1 → integrale consolidatie (exclusieve controle), belangen van derden = 10%
> - J → evenredige consolidatie (gezamenlijke controle), pro rata 50%
> - A → vermogensmutatiemethode (invloed van betekenis)
> - D2 → buiten consolidatiekring (vereffening, art. 3:99), via vermogensmutatiemethode (art. 3:100)
>
> **Grondslag**: KB-WVV art. 3:96–3:100, 3:124
>
> **Redenering**: D1 valt onder exclusieve controle (90% stemrechten). J heeft contractueel vastgelegde gezamenlijke controle → evenredig. A heeft 25% → vermoeden van invloed van betekenis zonder controle → equity-methode. D2 in vereffening → verplicht buiten de consolidatiekring, maar via VM-methode.
>
> 🤖 *AI-aanvulling*

## Motiveren op het examen

**Een volledig antwoord bevat:**
1. Vaststelling of de consolidatieverplichting geldt (met vermelding WVV art. 3:23 of 3:24)
2. Toetsing van eventuele vrijstellingen (omvang, beursnotering — WVV art. 3:25–3:27)
3. Classificatie van elke entiteit (type relatie + methode, met grondslag KB-WVV art. 3:124)
4. Beoordeling weglatingen (art. 3:97–3:100) indien relevant, met motivering

**Typische vraagvormen**

> [!question]- Bepaal de consolidatiekring
>
> Vennootschap A bezit 75% van B, 50% van C (samen met D, gezamenlijke controle), en 20% van E (geen controle, wel een RvB-zetel). A behoort zelf tot een kleine groep die niet meer dan één van de criteria van art. 1:26 WVV overschrijdt. Geen van de vennootschappen is genoteerd.
>
> Stel de consolidatiekring vast met de methode per entiteit. Is A vrijgesteld van de consolidatieplicht?
>
> > [!success]- Antwoord
> >
> > **Vrijstelling**: A behoort tot een groep van beperkte omvang (art. 1:26 WVV) en geen enkele vennootschap is genoteerd → A is vrijgesteld van de consolidatieverplichting (WVV art. 3:25, 3:27). Ze hoeft geen geconsolideerde jaarrekening op te stellen.
> >
> > Indien A toch consolideert:
> > - B → integrale consolidatie (75% exclusieve controle), belangen van derden = 25%
> > - C → evenredige consolidatie (50%, gezamenlijke controle)
> > - E → vermogensmutatiemethode (20%, vermoeden invloed van betekenis)
>
> 🤖 *AI-aanvulling*
