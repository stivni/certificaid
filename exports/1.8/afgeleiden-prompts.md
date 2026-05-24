---
title: "NotebookLM-afgeleiden — Analytische boekhouding"
description: "Prompts per output-type voor het programmaonderdeel Analytische boekhouding. Bronset = `1-8-analytische-boekhouding-notebooklm-bundle.md`. Eén intro-podcast + één deep-dive + één recap + één slidedeck + één algemene infographic + één cluster-infographic. Stuurt op leeruitkomsten — NotebookLM krijgt creatieve vrijheid in vorm."
gegenereerd_op: "2026-05-19"
status: experiment
---

# Afgeleiden-plan — Analytische boekhouding

> **Bronset (zelfde voor alle afgeleiden):** `exports/1.8/1-8-analytische-boekhouding-notebooklm-bundle.md`
> **Daglimiet podcasts (NL):** 3 afleveringen/dag in NotebookLM. Plan past in 1 dag (3 podcasts).

---

## Inhoud van dit plan

| Output-type | Aantal | Wat |
|---|---|---|
| 🎙️ Inleidende podcast | 1 | Mentale kapstok + vlieg-over hele programmaonderdeel |
| 🎙️ Deep-dive podcasts | 1 | Beslissings-kostprijs + budget + verschillen |
| 🎙️ Recap podcast (optioneel) | 1 | Consolidatie zonder nieuwe stof |
| 📊 Diapresentatie | 1 | Eén deck voor het hele programmaonderdeel |
| 🎨 Overzichts-infographic | 1 | Visualiseert de structuur en redeneerkader van het hele programmaonderdeel |
| 🎨 Cluster-infographic | 1 | Beslissings-kosten + break-even + budgetverschillen |

---

## Cognitieve kaart van het programmaonderdeel

Wat zit er inhoudelijk in Analytische boekhouding? Vier zwaartepunten — de intro dekt ze allemaal oppervlakkig, één deep-dive zoomt in op het zwaarste blok.

| # | Zwaartepunt | Inhoud | Diepduik-waardig? |
|---|---|---|---|
| 1 | Architectuur + redeneerkader | Drie-assen-skelet (kostensoort / kostencentrum / kostendrager), verdeelsleutels, registratiesystemen, brug naar algemene boekhouding | Nee — komt in intro |
| 2 | Kostentypologie + wettelijke vervaardigingsprijs | 2×2-typologie (gedrag × toewijsbaarheid), full costing als wettelijk spoor (KB 21.10.2018 + CBN 132/7), voorraadwaardering | Nee — komt in intro |
| 3 | Beslissings-kostprijs + budget + verschillen | Direct costing + contributiemarge + break-even + ABC + vier beslissings-kosten + make-or-buy + master-budget + statisch vs. flexibel budget + verschillenboekhouding | **Ja — deep-dive** |
| 4 | Brug naar algemene boekhouding + financiële analyse | Vervaardigingsprijs als balans-hekje, master-budget als vooruitzicht | Nee — komt in intro |

---

## Doelpubliek, voorbeelden, examen-stress — verwerkt in elke prompt

De volgende drie verankeringen staan IN elke prompt hieronder ingewerkt. Ter referentie hier afzonderlijk.

**Doelpubliek (gemengd):** primair een ervaren beroepsbeoefenaar (typisch 5-15 jaar in het accountancyberoep) die zich voorbereidt op het ITAA-bekwaamheidsexamen Gecertificeerd Accountant — niet noodzakelijk dagelijks actief in management accounting. Daarnaast luistert er af en toe een geïnteresseerde leek mee. De stof moet voor de beroepsbeoefenaar **voldoende diep** zijn (multi-conceptueel redeneren, methode-keuze verantwoorden) maar voor de leek **volgbaar** (geen pure jargon-stapeling). Toon: een vakgesprek tussen twee gecertificeerde accountants — of tussen een gecertificeerd accountant en een kandidaat-GA. De stagiair die zich op het examen voorbereidt luistert mee, maar wordt niet als publiek toegesproken. Vaktermen worden gebruikt zoals in de praktijk, maar concepten worden kort gepositioneerd wanneer nuance telt — bijvoorbeeld dat "direct" en "variabel" niét synoniem zijn ondanks de intuïtieve overlap.

**Voorbeelden:** concrete casussen in het bundle (zoals `Yperse Werkplaats BV`) zijn illustraties van een onderliggend principe — niet feiten over die ondernemingen, niet de wereldwijde regel. Spreek het principe uit via de illustratie en blijf bij het principe. Vermijd zinnen als "bij Yperse Werkplaats is het altijd zo" — wel: "in deze illustratie zien we hoe het principe X werkt wanneer Y".

**Examen-tone:** spreek niet uit naam van de examinator. Voorbeeldexamens zijn data over wat in het verleden gevraagd is, geen voorschriften voor wat absoluut moet. Vermijd stress-taal als "je moet absoluut", "de examinator verwacht", "u moet". Mag wel: "op integratieniveau wordt vaak verwacht", "wie deze stof beheerst kan...". Toon van een collega die mee voorbereidt, niet een examinator die toetst.

---

## Anti-fabricatie

Geldt in elke prompt: **gebruik UITSLUITEND inhoud uit het geüploade document `1-8-analytische-boekhouding-notebooklm-bundle.md`.** Geen externe bronnen, geen aanvullingen uit andere wetgevingen, geen verzonnen voorbeelden. Bij twijfel: zeg "dit staat niet in het bundle". Belgische context (WVV, KB WVV, CBN, ITAA-normen) — niet Nederland.

---

# 🎙️ Inleidende podcast (±18-22 min)

```text
Gebruik UITSLUITEND inhoud uit het geüploade document `1-8-analytische-boekhouding-notebooklm-bundle.md`. Geen externe bronnen, geen aanvullingen uit andere wetgevingen, geen verzonnen voorbeelden. Bij twijfel: zeg "dit staat niet in het bundle". Belgische context (WVV, KB WVV, CBN, ITAA-normen) — niet Nederland.

Doelpubliek (gemengd): primair een ervaren beroepsbeoefenaar (5-15 jaar accountancy-ervaring) die het ITAA-examen voorbereidt — niet noodzakelijk dagelijks in management accounting actief. Daarnaast luistert af en toe een geïnteresseerde leek mee. Toon: vakgesprek tussen twee gecertificeerde accountants (of GA + kandidaat-GA). De stagiair-luisteraar vangt het gesprek op, wordt niet rechtstreeks aangesproken. Voldoende diep voor de beroepsbeoefenaar (concept-nuance, multi-conceptueel redeneren), volgbaar voor de leek (geen pure jargon-stapeling, geen legalese). Vaktermen worden gebruikt zoals in de praktijk; concepten worden kort gepositioneerd waar nuance telt — bijvoorbeeld dat 'direct' en 'variabel' niet synoniem zijn. Geen pedagogische "wat is een kostprijs"-uitleg.

Behandel concrete casussen uit het bundle (zoals `Yperse Werkplaats BV`) als illustraties van een onderliggend principe, niet als feiten over die ondernemingen of als wereldwijde regel.

Spreek niet uit naam van de examinator. Voorbeeldexamens zijn data, geen voorschriften. Vermijd "je moet absoluut" / "de examinator verwacht". Toon van een collega die meeloopt met het examenvoorbereidingstraject, niet van een autoriteit.

Dit is de inleidende aflevering over Analytische boekhouding en management accounting. Doel: de luisteraar krijgt een coherent overzicht van het hele programmaonderdeel én de mentale kapstok om de deep-dive die volgt te plaatsen.

Wat de luisteraar na deze aflevering moet kunnen:
- De architectuur van een analytische boekhouding plaatsen via het drie-assen-skelet (kostensoort, kostencentrum, kostendrager) en aanduiden waarom de inrichting bedrijfsafhankelijk is
- De 2×2-typologie van kosten benoemen (gedrag × toewijsbaarheid) en uitleggen waarom de assen niet samenvallen — direct ≠ variabel
- Het verschil tussen algemene en analytische boekhouding scherp stellen (extern verslag per kostensoort versus interne sturing per drager/centrum) en de rol van een waarderingsneutraal registratiesysteem op de brug ertussen
- De wettelijke vervaardigingsprijs (KB 21.10.2018 + CBN 132/7) als ankerpunt voor voorraadwaardering positioneren en aanvoelen wanneer full costing het verplichte spoor is
- Aanvoelen waar de stof "rustig" is voor een ervaren beroepsbeoefenaar (typologie, registratie) en waar de echte cognitieve last zit (de deep-dive die volgt over beslissings-kostprijs, budget en verschillen)

Onderwerpen die aan bod moeten komen (volgorde en pacing vrij):
- Waarom een tweede boekhouding bestaat — wat de algemene boekhouding niet kan beantwoorden, en wat de analytische daaraan toevoegt
- Het drie-assen-skelet: kostensoort, kostencentrum, kostendrager — wat ze elk zijn, hoe verdeelsleutels ze verbinden, waarom klasse 9 in het MAR vrij ingericht is
- De 2×2-typologie van kosten (gedrag × toewijsbaarheid) met de waarschuwing dat de assen onafhankelijk zijn — een examenvalkuil
- Registratiesystemen op een rij (waarderingsneutraal, eenvoudige integratie, proportionele integratie) — alleen positioneren, geen detail
- De wettelijke vervaardigingsprijs als hekje naar de balans (KB 21.10.2018 + CBN 132/7): full costing voor voorraad zelfvervaardigde producten
- De brug naar algemene boekhouding én de vooruitblik via het master-budget — kort positioneren
- Waarom het blok beslissings-kostprijs + budget + verschillen een eigen deep-dive verdient (multi-methode-keuze, verschil tussen relevant en niet-relevant, oorzaakanalyse via flexibel budget)

Tone-hints: spreek de luisteraar aan als collega die het deelgebied wil opfrissen voor het examen, niet als beginner. Vermijd "let's dive in"-openings. Geen cijferreeksen — audio-medium.
```

---

# 🎙️ Deep-dive — Beslissings-kostprijs, budget en verschillen (±20-25 min)

```text
Gebruik UITSLUITEND inhoud uit het geüploade document `1-8-analytische-boekhouding-notebooklm-bundle.md`. Geen externe bronnen, geen aanvullingen uit andere wetgevingen, geen verzonnen voorbeelden. Bij twijfel: zeg "dit staat niet in het bundle". Belgische context (WVV, KB WVV, CBN, ITAA-normen) — niet Nederland.

Doelpubliek (gemengd): ervaren beroepsbeoefenaar (5-15 jaar accountancy-ervaring) bereidt het ITAA-examen voor, soms luistert een geïnteresseerde leek mee. Toon: vakgesprek tussen twee gecertificeerde accountants (of GA + kandidaat-GA). De stagiair-luisteraar vangt het gesprek op, wordt niet rechtstreeks aangesproken. Voldoende diep voor de beroepsbeoefenaar, volgbaar voor de leek. Vaktermen worden gebruikt zoals in de praktijk; concepten worden kort gepositioneerd waar nuance telt. Geen pedagogische basisuitleg.

Behandel concrete casussen uit het bundle (`Yperse Werkplaats BV`) als illustraties van een onderliggend principe, niet als feiten of als wereldwijde regel.

Spreek niet uit naam van de examinator. Voorbeeldexamens zijn data, geen voorschriften. Toon van een collega die meedenkt, niet van een autoriteit.

Deep-dive-aflevering: de cognitief zware kern van het programmaonderdeel — methode-keuze voor beslissingen, het master-budget als vooruitzicht, en verschillenboekhouding als terugblik. Bouwt op de inleidende aflevering (drie-assen-skelet + 2×2-typologie + wettelijke vervaardigingsprijs). Geen herhaling van die basis — direct in de cognitieve last.

Wat de luisteraar na deze aflevering moet kunnen:
- De keuze tussen full costing en direct costing verantwoorden vanuit het doel van de berekening — voorraadwaardering versus korte-termijn-beslissing — en aanvoelen waarom dezelfde realiteit twee verschillende cijfers oplevert
- Contributiemarge gebruiken als hefboom voor break-even en veiligheidsmarge, en uitleggen waarom de break-even-redenering niet werkt zonder eerst de vast/variabel-splitsing
- Beoordelen wanneer een overhead-zware structuur de klassieke uur-sleutel ontgroeit en de ABC-methode een fijnmaziger antwoord geeft
- De vier beslissings-kosten onderscheiden (marginale kost, opportuniteitskost, sunk cost, gemiddelde kost) en per type aangeven welke vraag erbij past — extra-order, lange-termijn-richtprijs, make-or-buy
- Een make-or-buy-redenering opbouwen die vermijdbare kosten correct identificeert, opportuniteitskost meeneemt en sunk costs expliciet wegstreept — inclusief de kwalitatieve weging die boven het cijfer komt
- Een master-budget plaatsen in de budgetcyclus en aangeven waarom alleen een flexibel budget — niet een statisch — een eerlijke afwijkingsanalyse mogelijk maakt
- Een totaalverschil tussen werkelijk en standaard opsplitsen in prijs- en hoeveelheidscomponent en de scheidslijn tussen volume-effect en inefficiëntie benoemen

Onderwerpen die aan bod moeten komen (volgorde en pacing vrij):
- Direct costing + contributiemarge + break-even — het beslissings-spoor, met de waarschuwing dat full costing voor diezelfde casus tot een ander cijfer leidt
- ABC-methode als alternatief wanneer overhead het kostengedrag domineert — wanneer overwegen, wat het laat zien dat een uur-sleutel verbergt
- Vier beslissings-kosten: marginaal, opportuniteit, sunk, gemiddeld — en de match met het vraagtype
- Make-or-buy als integratie: vermijdbare kosten, opportuniteitskost meewegen, sunk costs negeren, kwalitatieve factoren benoemen
- Master-budget + budgetprocedure — vaste sequentie van deelbudgetten, pro-forma resultatenrekening / balans / kasstroom
- Statisch versus flexibel budget — de scheidslijn waarop de afwijkings-analyse staat of valt
- Verschillenboekhouding: totaalverschil → prijs- en hoeveelheidscomponent — toegelicht via het arbeids-voorbeeld (tariefverschil versus efficiëntieverschil) als illustratie van een patroon dat ook voor materiaal en overhead werkt
- Korte sluiting: grenzen van kostencalculatie — elke kostprijs draagt aannames (verdeelsleutel, capaciteitsniveau, afbakening direct/indirect)

Tone-hints: dichte stof — pacing en accentuering aan de hosts. Vermijd "let's dive in"-openings. Geen cijferreeksen. Behandel illustraties uit het bundle (zoals `Yperse Werkplaats BV` indien aanwezig) als voorbeelden van het principe, niet als de norm.
```

---

# 🎙️ Recap podcast (optioneel, ±8-10 min)

```text
Gebruik UITSLUITEND inhoud uit het geüploade document `1-8-analytische-boekhouding-notebooklm-bundle.md`. Geen externe bronnen, geen aanvullingen uit andere wetgevingen, geen verzonnen voorbeelden. Bij twijfel: zeg "dit staat niet in het bundle". Belgische context (WVV, KB WVV, CBN, ITAA-normen) — niet Nederland.

Doelpubliek (gemengd): ervaren beroepsbeoefenaar (5-15 jaar accountancy-ervaring) die de twee eerdere afleveringen al gehoord heeft, soms een geïnteresseerde leek mee. Toon: vakgesprek tussen gecertificeerde accountants (of GA + kandidaat-GA), volgbaar voor de leek. De stagiair-luisteraar vangt het gesprek op, wordt niet rechtstreeks aangesproken.

Behandel casussen uit het bundle als illustraties van een principe, niet als feiten of wereldwijde regel. Spreek niet uit naam van de examinator.

Korte consolidatie-aflevering. Geen nieuwe stof.

Wat de luisteraar na deze recap moet kunnen:
- De vier zwaartepunten van Analytische boekhouding in eigen woorden positioneren (architectuur → typologie + vervaardigingsprijs → beslissings-kostprijs + budget + verschillen → brug)
- Per zwaartepunt het kernspanningsveld benoemen — waar zit de cognitieve last, niet waar de feitenkennis
- De vier verwarringsparen uit de cheatsheet snel uit het hoofd maken (direct ≠ variabel, full costing ≠ direct costing, statisch ≠ flexibel, marginaal ≠ gemiddeld)

Onderwerpen die aan bod moeten komen (één keer kort per blok):
- Drie-assen-skelet + brug algemene/analytische via waarderingsneutraal registratiesysteem
- 2×2-typologie + wettelijke vervaardigingsprijs voor voorraadwaardering
- Beslissings-kostprijs (direct costing, ABC, vier beslissings-kosten) + master-budget + verschillen-splitsing
- De grootste examenvalkuilen: direct/variabel-verwarring, methode-keuze zonder doel-vraag, statisch-budget-afwijkingsanalyse

Tone-hints: consolidatie, geen nieuwe voorbeelden. Vermijd "let's dive in"-openings.
```

---

# 📊 Diapresentatie — één deck voor het hele programmaonderdeel

```text
Gebruik UITSLUITEND inhoud uit het geüploade document `1-8-analytische-boekhouding-notebooklm-bundle.md`. Geen externe bronnen, geen aanvullingen uit andere wetgevingen, geen verzonnen voorbeelden. Bij twijfel: zeg "dit staat niet in het bundle". Belgische context (WVV, KB WVV, CBN, ITAA-normen) — niet Nederland.

Doelpubliek (gemengd): primair een ervaren beroepsbeoefenaar (5-15 jaar accountancy-ervaring) die de stof opfrist voor het ITAA-examen — niet noodzakelijk dagelijks in management accounting actief. Daarnaast kan een geïnteresseerde leek het deck bekijken. Toon: vakgesprek tussen twee gecertificeerde accountants (of GA + kandidaat-GA). De stagiair-luisteraar vangt het gesprek op, wordt niet rechtstreeks aangesproken. Vaktermen worden gebruikt zoals in de praktijk; concepten worden gepositioneerd waar nuance telt. Geen pure jargon-stapeling, geen legalese.

Casussen uit het bundle (`Yperse Werkplaats BV`) zijn illustraties van een onderliggend principe, niet feiten over die ondernemingen.

Eén slidedeck dat het volledige programmaonderdeel Analytische boekhouding dekt op overzichtsniveau. NotebookLM bepaalt zelf het aantal slides, de volgorde van details binnen elk zwaartepunt, en de visuele indeling.

Wat de student na het doorbladeren van deze deck moet kunnen:
- Het drie-assen-skelet (kostensoort, kostencentrum, kostendrager) schematisch reproduceren met verdeelsleutels en klasse 9 als plaatsing in het MAR
- De 2×2-typologie van kosten visueel onderscheiden — gedrag op de ene as, toewijsbaarheid op de andere — en aanduiden waarom de assen niet samenvallen
- De wettelijke samenstelling van de vervaardigingsprijs (KB 21.10.2018 + CBN 132/7) benoemen en aangeven welke kostencomponenten erbij horen
- De methode-keuze full costing versus direct costing motiveren vanuit het doel (voorraadwaardering versus korte-termijn-beslissing) en het ABC-alternatief plaatsen
- De vier beslissings-kosten (marginaal, opportuniteit, sunk, gemiddeld) per type matchen aan een vraagtype
- De budgetcyclus schetsen van master-budget tot verschillenboekhouding en de scheidslijn statisch / flexibel budget aanduiden
- Een verschillen-splitsing in prijs- en hoeveelheidscomponent volgen via het arbeids-voorbeeld

Inhoudelijke clusters die in het deck moeten landen:
- Architectuur: drie-assen-skelet + verdeelsleutels + klasse 9 + registratiesystemen + brug naar algemene boekhouding
- Kostentypologie: 2×2 (gedrag × toewijsbaarheid) — overzichtsniveau, met expliciete waarschuwing direct ≠ variabel
- Wettelijke vervaardigingsprijs + voorraadwaardering (KB 21.10.2018 + CBN 132/7) als balans-hekje
- Kostencalculatie vergeleken: full costing, direct costing, werkelijke versus voorbepaalde kosten, ABC — wanneer welke
- Beslissings-kosten en make-or-buy — vier types + de redeneerlijn
- Budget en verschillen: master-budget → budgetprocedure → statisch versus flexibel → verschillenboekhouding (prijs/hoeveelheid)
- Vergelijkingsparen-matrix uit het bundle — als leesbare tabel
- Synthese-stappenplan voor een geïntegreerde casus

Stijl: NotebookLM bepaalt zelf alle vormaspecten. Cruciale tabellen en diagrammen uit het bundle mogen letterlijk over (de typologie-matrix, de methode-vergelijking, de vergelijkingsparen-matrix). Eén deck, gemaakt om snel doorheen te bladeren als revisie — niet om de detail-stof te vervangen.
```

---

# 🎨 Overzichts-infographic — structuur van het hele programmaonderdeel

```text
Gebruik UITSLUITEND inhoud uit het geüploade document `1-8-analytische-boekhouding-notebooklm-bundle.md`. Geen externe bronnen, geen aanvullingen uit andere wetgevingen, geen verzonnen voorbeelden. Bij twijfel: zeg "dit staat niet in het bundle". Belgische context (WVV, KB WVV, CBN, ITAA-normen) — niet Nederland.

Doelpubliek (gemengd): ervaren beroepsbeoefenaar bereidt het ITAA-examen voor, met af en toe een geïnteresseerde leek die meekijkt. Vaktermen gebruiken zoals in de praktijk; geen pure jargon-stapeling, geen legalese.

Casussen uit het bundle zijn illustraties van een onderliggend principe.

Eén infographic-pagina die het hele programmaonderdeel Analytische boekhouding visueel ordent. NotebookLM bepaalt zelf de indeling, kleurkeuze en grafische metaforen.

Centrale boodschap: Analytische boekhouding leest van architectuur naar beslissing — eerst het drie-assen-skelet dat elke kost een plaats geeft, dan de typologie + wettelijke vervaardigingsprijs als gedeeld referentiekader, vervolgens de methode-keuzes die afhangen van wat je wil weten (voorraadwaardering, beslissing, planning, opvolging), en tenslotte de brug naar algemene boekhouding en financiële analyse.

Wat de student na het bekijken van deze infographic moet kunnen:
- De architectuur van het programmaonderdeel beschrijven in vier zwaartepunten
- Per zwaartepunt benoemen welk type cognitieve last erin zit (architectuur-keuze, typologie, methode-keuze + redeneerlijn, brug)
- Wijzen op het blok waar de echte examenklassiekers zitten (beslissings-kostprijs + budget + verschillen)

Inhoudelijke elementen die moeten doorkomen:
- Het drie-assen-skelet als visueel anker (kostensoort, kostencentrum, kostendrager + verdeelsleutels)
- De 2×2-typologie van kosten met de expliciete vermelding dat gedrag en toewijsbaarheid onafhankelijke assen zijn
- De wettelijke vervaardigingsprijs (KB 21.10.2018 + CBN 132/7) als hekje naar de balans
- De vier zwaartepunten als architectonisch overzicht — per zwaartepunt één zin "wat zit erin" + één zin "waar de last zit"
- Aanduiding welk blok in de deep-dive wordt uitgewerkt

Stijl: NotebookLM kiest de indeling. Houd de accentkleuren coherent met de cluster-infographic hieronder.
```

---

# 🎨 Cluster-infographic — Beslissings-kosten, break-even en budgetverschillen

```text
Gebruik UITSLUITEND inhoud uit het geüploade document `1-8-analytische-boekhouding-notebooklm-bundle.md`. Geen externe bronnen, geen aanvullingen uit andere wetgevingen, geen verzonnen voorbeelden. Bij twijfel: zeg "dit staat niet in het bundle". Belgische context (WVV, KB WVV, CBN, ITAA-normen) — niet Nederland.

Doelpubliek: ervaren beroepsbeoefenaar die de stof opfrist. Casussen uit het bundle (`Yperse Werkplaats BV`) zijn illustraties — geen feit, geen norm.

Eén infographic-pagina die het deep-dive-blok dieper uitwerkt dan de overzichts-infographic.

Centrale boodschap: in het beslissings-spoor van analytische boekhouding draait alles om de juiste lens kiezen — full costing voor balans, direct costing en contributiemarge voor korte-termijn-beslissingen, ABC bij overhead-dominantie, en bij planning + opvolging het master-budget met een flexibel budget als enige eerlijke vergelijkingsbasis voor verschillen.

Wat de student na het bekijken van deze infographic moet kunnen:
- De vier beslissings-kosten (marginaal, opportuniteit, sunk, gemiddeld) zij-aan-zij plaatsen met telkens het type vraag dat erbij past
- De break-even-redenering schematisch volgen (vast/variabel-splitsing → contributiemarge per eenheid → break-even-volume of -omzet → veiligheidsmarge)
- De scheidslijn statisch / flexibel budget visualiseren en aanduiden waarom alleen het flexibel budget volume-effect van inefficiëntie scheidt
- Een verschillen-splitsing in prijs- en hoeveelheidscomponent schematisch volgen via het arbeids-voorbeeld

Inhoudelijke elementen die moeten doorkomen:
- Vier beslissings-kosten met telkens: wat is het + bij welk vraagtype + bij welke valkuil
- Break-even-mechaniek als visueel diagram (drempel, contributiemarge per eenheid, veiligheidsmarge)
- ABC-methode kort als alternatief wanneer overhead het kostengedrag domineert
- Statisch versus flexibel budget — visuele scheidslijn met de afwijkingsanalyse als consequentie
- Verschillen-splitsing prijs/hoeveelheid op het arbeids-voorbeeld (tariefverschil / efficiëntieverschil) — illustratief voor materiaal en overhead
- Make-or-buy als integratie-redenering: vermijdbaar + opportuniteit + sunk wegstrepen

Stijl: NotebookLM kiest de indeling. Coherent met de overzichts-infographic.
```

---

## Plan-samenvatting (1 oogopslag)

| Volgorde | Output | Lengte / formaat | Daglimiet? |
|---|---|---|---|
| 1 | 🎙️ Inleidende podcast | ±18-22 min | Telt in 3/dag NL-podcasts |
| 2 | 🎙️ Deep-dive — beslissings-kostprijs + budget + verschillen | ±20-25 min | Telt in 3/dag |
| 3 | 🎙️ Recap (optioneel) | ±8-10 min | Telt in 3/dag |
| — | 📊 Slidedeck (één voor heel programmaonderdeel) | Aantal slides vrij | Geen limiet |
| — | 🎨 Overzichts-infographic | Eén pagina | Geen limiet |
| — | 🎨 Cluster-infographic — beslissings-kosten + break-even + verschillen | Eén pagina | Geen limiet |

Plan past in 1 dag voor alle drie de podcasts; visuele afgeleiden parallel.
