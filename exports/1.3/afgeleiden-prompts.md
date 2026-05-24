---
title: "NotebookLM-afgeleiden — Analyse van de jaarrekening"
description: "Prompts per output-type voor het programmaonderdeel Analyse van de jaarrekening. Bronset = `1-3-analyse-notebooklm-bundle.md`. Eén intro-podcast + twee deep-dives + optionele recap + één slidedeck + één overzichts-infographic + twee cluster-infographics. Stuurt op leeruitkomsten — NotebookLM krijgt creatieve vrijheid in vorm."
gegenereerd_op: "2026-05-19"
status: experiment
---

# Afgeleiden-plan — Analyse van de jaarrekening

> **Bronset (zelfde voor alle afgeleiden):** `exports/1.3/1-3-analyse-notebooklm-bundle.md`
> **Daglimiet podcasts (NL):** 3 afleveringen/dag in NotebookLM. Plan past in 1 dag (3 podcasts) + optionele recap dag 2.

---

## Inhoud van dit plan

| Output-type | Aantal | Wat |
|---|---|---|
| 🎙️ Inleidende podcast | 1 | Mentale kapstok: gebruiker-doel-ratio, vier analyse-doelen, analytische balans als vertrekpunt |
| 🎙️ Deep-dive podcasts | 2 | Ratio-families: berekening + interpretatie · Van losse ratio's naar coherente diagnose |
| 🎙️ Recap podcast (optioneel) | 1 | Consolidatie zonder nieuwe stof |
| 📊 Diapresentatie | 1 | Eén deck voor het hele programmaonderdeel |
| 🎨 Overzichts-infographic | 1 | Visualiseert de analyse-cyclus (gebruiker → analytische balans → ratio's → diagnose → advies) |
| 🎨 Cluster-infographics | 2 | Ratio-families-overzicht (vier doelen, hun ratio's en grens-waarden) · Diagnose-synthese (drie assen + off-balance + bestuursverslag) |

---

## Cognitieve kaart van het programmaonderdeel

Wat zit er inhoudelijk in Analyse van de jaarrekening? Vier zwaartepunten — de intro dekt ze allemaal oppervlakkig, deep-dives zoomen in op de twee zwaartepunten waar de echte cognitieve last zit.

| # | Zwaartepunt | Inhoud | Diepduik-waardig? |
|---|---|---|---|
| 1 | Fundament: gebruiker, doel, analytische balans | Wie analyseert wat met welk doel (gebruikers en hun belang), de vier analyse-doelen, herwerking van de jaarrekening tot een analytische balans, verticale + horizontale analyse als opwarming | Nee — komt in intro |
| 2 | Ratio-families: berekening + interpretatie | Liquiditeit (current / quick / cash + werkkapitaalbehoefte), solvabiliteit (solvabiliteitsratio, schuldgraad, gearing), rentabiliteit (ROE, ROA, gross/operating/net margin), werkkapitaal + kasstroom-indicatoren | **Ja — deep-dive 1** |
| 3 | Van losse ratio's naar diagnose | Drie analyse-assen samenbrengen (liquiditeit + solvabiliteit + rentabiliteit), off-balance posten en toelichting confronteren, bestuursverslag + niet-financiële informatie kritisch lezen, sector-benchmark en trend-analyse, formuleren van een financiële diagnose + verbeteradvies | **Ja — deep-dive 2** |
| 4 | Toezicht + kritische blik op de analyse zelf | Toezichtsorganen rond de jaarrekening positioneren, wat een ratio-analyse NIET kan zeggen, beperkingen van historische cijfers | Nee — komt in intro |

---

## Doelpubliek, voorbeelden, examen-stress — verwerkt in elke prompt

De volgende drie verankeringen staan IN elke prompt hieronder ingewerkt. Ter referentie hier afzonderlijk.

**Doelpubliek (gemengd):** primair een ervaren beroepsbeoefenaar (typisch 5-15 jaar in het accountancyberoep) die zich voorbereidt op het ITAA-bekwaamheidsexamen Gecertificeerd Accountant — niet noodzakelijk dagelijks actief in dit deelgebied. Daarnaast luistert er af en toe een geïnteresseerde leek mee (partner, kennis). De stof moet voor de beroepsbeoefenaar **voldoende diep** zijn (ratio-nuance, redeneren over wat een ratio NIET zegt, multi-conceptueel diagnoseren) maar voor de leek **volgbaar** (geen pure jargon-stapeling, geen formule-stortvloed). Toon: een vakgesprek tussen twee gecertificeerde accountants — of tussen een gecertificeerd accountant en een kandidaat-GA. De stagiair die zich op het examen voorbereidt luistert mee, maar wordt niet als publiek toegesproken. Vaktermen worden gebruikt zoals ze in de praktijk vallen, maar concepten worden kort gepositioneerd wanneer nuance telt. Geen pedagogische "wat is een ratio"-momenten; wel "let op — solvabiliteit en liquiditeit gaan over totaal andere tijdshorizonten, vermijd dat ze in één adem als 'gezondheid' worden samengevat".

**Voorbeelden:** de illustratie `Rotex Roeselare NV` uit het bundle is een doorlopend voorbeeld — illustratie van een onderliggend principe, niet een feit over die onderneming, niet de wereldwijde regel. Spreek het principe uit via de illustratie en blijf bij het principe. Vermijd zinnen als "bij Rotex is het altijd zo" — wel: "in de Rotex-illustratie zien we hoe een current ratio onder 1 niet automatisch alarmerend is wanneer de werkkapitaalbehoefte structureel negatief is".

**Examen-tone:** spreek niet uit naam van de examinator. Voorbeeldexamens zijn data over wat in het verleden gevraagd is, geen voorschriften voor wat absoluut moet. Vermijd stress-taal als "je moet absoluut", "de examinator verwacht", "u moet". Mag wel: "op integratieniveau wordt vaak verwacht dat je een ratio plaatst in context", "in voorbeeldexamens komen geregeld diagnose-vragen waar drie ratio-families samenspelen", "wie deze stof beheerst kan...". Toon van een collega die mee voorbereidt, niet een examinator die toetst.

---

## Anti-fabricatie

Geldt in elke prompt: **gebruik UITSLUITEND inhoud uit het geüploade document `1-3-analyse-notebooklm-bundle.md`.** Geen externe bronnen, geen aanvullingen uit andere wetgevingen, geen verzonnen voorbeelden. Bij twijfel: zeg "dit staat niet in het bundle". Belgische context (WVV, KB WVV, CBN) — niet Nederland.

---

# 🎙️ Inleidende podcast (±20 min)

```text
Gebruik UITSLUITEND inhoud uit het geüploade document `1-3-analyse-notebooklm-bundle.md`. Geen externe bronnen, geen aanvullingen uit andere wetgevingen, geen verzonnen voorbeelden. Bij twijfel: zeg "dit staat niet in het bundle". Belgische context (WVV, KB WVV, CBN) — niet Nederland.

Doelpubliek (gemengd): primair een ervaren beroepsbeoefenaar (5-15 jaar accountancy-ervaring) die het ITAA-examen voorbereidt — niet noodzakelijk dagelijks in dit deelgebied. Daarnaast luistert af en toe een geïnteresseerde leek mee. Toon: vakgesprek tussen twee gecertificeerde accountants (of GA + kandidaat-GA). De stagiair-luisteraar vangt het gesprek op, wordt niet rechtstreeks aangesproken. Voldoende diep voor de beroepsbeoefenaar (ratio-nuance, multi-conceptueel redeneren), volgbaar voor de leek (geen pure jargon-stapeling, geen formule-stortvloed). Vaktermen worden gebruikt zoals in de praktijk; concepten worden kort gepositioneerd waar nuance telt. Geen pedagogische "wat is een balans"-uitleg; wel kort verduidelijken wanneer een term in de analyse-context een specifieke betekenis krijgt.

Behandel de illustratie `Rotex Roeselare NV` uit het bundle als illustratie van een onderliggend principe, niet als een feit over die onderneming of als wereldwijde regel.

Spreek niet uit naam van de examinator. Voorbeeldexamens zijn data, geen voorschriften. Vermijd "je moet absoluut" / "de examinator verwacht". Toon van een collega die meeloopt met het examenvoorbereidingstraject, niet van een autoriteit.


Dit is de inleidende aflevering over Analyse van de jaarrekening. Doel: de luisteraar krijgt een coherent overzicht van het hele programmaonderdeel én de mentale kapstok om de deep-dive-afleveringen straks te plaatsen.

Wat de luisteraar na deze aflevering moet kunnen:
- De gebruiker-doel-ratio-driehoek plaatsen: wie analyseert (kredietverstrekker / aandeelhouder / leverancier / werknemer / overheid), met welk doel, en hoe dat de keuze van ratio's stuurt
- De vier analyse-doelen onderscheiden (liquiditeit / solvabiliteit / rentabiliteit / waardecreatie + cashflow) en aanvoelen dat ze niet inwisselbaar zijn
- Het idee van een analytische balans plaatsen — waarom de officiële balans wordt herwerkt voor analyse-doeleinden, en welke verschuivingen typisch gebeuren
- De vier zwaartepunten van het programmaonderdeel noemen (fundament / ratio-families / diagnose-synthese / kritische blik) en weten welk type vragen ze typisch oproepen
- Aanvoelen waar de stof "rustig" is voor een ervaren beroepsbeoefenaar en waar de echte cognitieve last zit (de twee deep-dives die volgen)

Onderwerpen die aan bod moeten komen (volgorde en pacing vrij):
- Waarom een jaarrekening analyseren? De vraag verschilt per gebruiker — een kredietverstrekker stelt andere vragen dan een potentiële koper of een werknemer
- De vier analyse-doelen als kapstok: liquiditeit (kortetermijn-verplichtingen), solvabiliteit (langetermijn-structuur), rentabiliteit (verdienvermogen), waardecreatie + cashflow (echte geldstroom versus boekhoudkundig resultaat)
- De analytische balans als instrument — kort positioneren, niet de detail-herwerking; senior luisteraar herkent het mechanisme
- Verticale en horizontale analyse als opwarming voor de ratio's
- Waarom de ratio-families een eigen deep-dive verdienen (de échte risico-zone: een ratio fout interpreteren = diagnose fout = advies fout)
- Waarom de diagnose-synthese een eigen deep-dive verdient (van losse cijfers naar een coherent verhaal — examen-integratie bij uitstek)
- Korte sluiting: wat een ratio-analyse NIET kan zeggen — beperking als deel van het redeneerkader

Tone-hints: spreek de luisteraar aan als collega die het deelgebied wil opfrissen voor het examen, niet als beginner. Vermijd "let's dive in"-openings. Geen cijferreeksen voorlezen — audio-medium; concepten en relaties primeren.
```

---

# 🎙️ Deep-dive 1 — Ratio-families: berekening + interpretatie (±20 min)

```text
Gebruik UITSLUITEND inhoud uit het geüploade document `1-3-analyse-notebooklm-bundle.md`. Geen externe bronnen, geen aanvullingen uit andere wetgevingen, geen verzonnen voorbeelden. Bij twijfel: zeg "dit staat niet in het bundle". Belgische context (WVV, KB WVV, CBN) — niet Nederland.

Doelpubliek (gemengd): ervaren beroepsbeoefenaar (5-15 jaar accountancy-ervaring) bereidt het ITAA-examen voor, soms luistert een geïnteresseerde leek mee. Toon: vakgesprek tussen twee gecertificeerde accountants (of GA + kandidaat-GA). De stagiair-luisteraar vangt het gesprek op, wordt niet rechtstreeks aangesproken. Voldoende diep voor de beroepsbeoefenaar, volgbaar voor de leek. Vaktermen worden gebruikt zoals in de praktijk; concepten worden kort gepositioneerd waar nuance telt. Geen pedagogische basisuitleg.

Behandel de illustratie `Rotex Roeselare NV` uit het bundle als illustratie van een onderliggend principe, niet als een feit of als wereldwijde regel.

Spreek niet uit naam van de examinator. Voorbeeldexamens zijn data, geen voorschriften. Toon van een collega die meedenkt, niet van een autoriteit.


Deep-dive-aflevering: de vier ratio-families systematisch — wat ze meten, hoe ze berekenen, wat de typische valkuilen zijn bij interpretatie. Bouwt op de gebruiker-doel-ratio-driehoek en de analytische balans uit de inleidende aflevering. Geen herhaling van die basis — direct in de cognitieve last.

Wat de luisteraar na deze aflevering moet kunnen:
- De liquiditeitsratio's onderscheiden (current ratio, quick ratio, cash ratio) en aangeven welke je gebruikt bij welk type onderneming (productie versus dienst, voorraad-zwaar versus voorraad-licht)
- De werkkapitaalbehoefte plaatsen naast de liquiditeitsratio's en uitleggen waarom een negatieve werkkapitaalbehoefte een lage current ratio kan rechtvaardigen
- De solvabiliteitsratio's interpreteren (solvabiliteitsratio = eigen vermogen / totaal vermogen, schuldgraad, gearing) en aangeven welke een lange-termijn-zorg signaleren
- De rentabiliteitsratio's correct positioneren (ROE als aandeelhoudersperspectief, ROA als activum-rendement, marges per niveau van de resultatenrekening) en de DuPont-redeneerlijn aanvoelen
- Beoordelen welke ratio een misleidend signaal kan geven en hoe je dat detecteert (boekhoudkundige effecten, eenmalige posten, off-balance financiering)
- De grens-waarden uit het bundle plaatsen als richtwaarde — niet als wet — en weten dat sectorvergelijking essentieel is

Onderwerpen die aan bod moeten komen (volgorde en pacing vrij):
- Liquiditeit: current / quick / cash — wanneer welke
- Werkkapitaalbehoefte als verfijning — het Rotex-voorbeeld uit het bundle als illustratie van "lage current ratio hoeft geen probleem te zijn"
- Solvabiliteit: solvabiliteitsratio, schuldgraad, gearing — en hoe ze samenhangen
- Rentabiliteit: ROE / ROA / marges — wat ze afzonderlijk zeggen, hoe ze samenkomen in een DuPont-achtige decompositie
- De drie kritische valkuilen bij interpretatie: (a) ratio zonder context, (b) eenmalige posten die het beeld vertekenen, (c) off-balance financiering die solvabiliteit flatteert
- Grens-waarden + sector-benchmark als richtsnoer, niet als regel
- Korte brug naar deep-dive 2: één ratio alleen is geen diagnose

Tone-hints: dichte stof met veel formules — pacing en accentuering aan de hosts. Geen formules voorlezen in audio; spreek over wat een ratio meet en wat ze NIET vangt. Vermijd "let's dive in"-openings.
```

---

# 🎙️ Deep-dive 2 — Van losse ratio's naar coherente diagnose (±20 min)

```text
Gebruik UITSLUITEND inhoud uit het geüploade document `1-3-analyse-notebooklm-bundle.md`. Geen externe bronnen, geen aanvullingen uit andere wetgevingen, geen verzonnen voorbeelden. Bij twijfel: zeg "dit staat niet in het bundle". Belgische context (WVV, KB WVV, CBN) — niet Nederland.

Doelpubliek (gemengd): ervaren beroepsbeoefenaar (5-15 jaar accountancy-ervaring) bereidt het ITAA-examen voor, soms luistert een geïnteresseerde leek mee. Toon: vakgesprek tussen twee gecertificeerde accountants (of GA + kandidaat-GA). De stagiair-luisteraar vangt het gesprek op, wordt niet rechtstreeks aangesproken. Voldoende diep voor de beroepsbeoefenaar, volgbaar voor de leek. Vaktermen worden gebruikt zoals in de praktijk; concepten worden kort gepositioneerd waar nuance telt. Geen pedagogische basisuitleg.

Behandel de illustratie `Rotex Roeselare NV` uit het bundle als illustratie van een onderliggend principe, niet als een feit of als wereldwijde regel.

Spreek niet uit naam van de examinator. Voorbeeldexamens zijn data, geen voorschriften. Toon van een collega die meedenkt, niet van een autoriteit.


Deep-dive-aflevering: van losse ratio's naar een coherent diagnose-verhaal. Hoe combineer je liquiditeit + solvabiliteit + rentabiliteit, hoe weeg je off-balance posten en de toelichting mee, hoe lees je het bestuursverslag kritisch, en hoe formuleer je een diagnose + verbeteradvies dat hangt? Bouwt op deep-dive 1. Geen herhaling van ratio-berekeningen — focus op synthese.

Wat de luisteraar na deze aflevering moet kunnen:
- De drie analyse-assen (liquiditeit / solvabiliteit / rentabiliteit) tegelijk lezen en herkennen wanneer ze elkaar versterken of tegenspreken
- Off-balance posten (operationele leasing, hangende rechtszaken, garantieverplichtingen) confronteren met de balans-ratio's en weten hoe ze het beeld kantelen
- De toelichting en het bestuursverslag kritisch lezen: waar zit het signaal, waar de cosmetiek, waar de niet-financiële indicatie (continuïteitstwijfels, governance-incidenten)
- Een trend over meerdere jaren + een sectorvergelijking inzetten als context — niet als doel op zich
- Een financiële diagnose formuleren: kernspanningsveld benoemen, oorzaak hypothetiseren (operationeel / financieel / structureel), concreet verbeteradvies aan het bestuur formuleren
- Aanvoelen wat een ratio-analyse NIET kan zeggen (toekomst, kwaliteit management, marktpositie) — kritische blik als sluitstuk

Onderwerpen die aan bod moeten komen (volgorde en pacing vrij):
- Het samenspel van de drie assen — typische combinaties (rendabel maar onsolide / solide maar weinig rendabel / liquide maar verliesmakend) en wat ze betekenen
- Off-balance posten: hoe ze de ratio's flatteren of vertekenen, met focus op operationele leasing en hangende rechtszaken
- Toelichting + bestuursverslag + niet-financiële informatie als signaal-bronnen, niet als verplichting alleen
- Trend-analyse en sectorbenchmark als context-instrumenten, met de waarschuwing voor cycli en uitschieters
- De Rotex-illustratie uit het bundle als doorlopend voorbeeld van "drie assen + off-balance samen lezen"
- Het formuleren van de diagnose: oorzaak versus symptoom, structureel versus eenmalig
- Verbeteradvies aan het bestuur — concreet, niet generiek
- Korte sluiting: wat een analyse NIET zegt (toekomstprognose, managementkwaliteit) — beperkingen als deel van de professionele houding

Tone-hints: dit is examen-integratie-stof bij uitstek — pacing dien-baar aan de redenering. Behandel de Rotex-illustratie expliciet als voorbeeld, niet als de norm. Vermijd "let's dive in"-openings.
```

---

# 🎙️ Recap podcast (optioneel, ±8-10 min)

```text
Gebruik UITSLUITEND inhoud uit het geüploade document `1-3-analyse-notebooklm-bundle.md`. Geen externe bronnen, geen aanvullingen uit andere wetgevingen, geen verzonnen voorbeelden. Bij twijfel: zeg "dit staat niet in het bundle". Belgische context (WVV, KB WVV, CBN) — niet Nederland.

Doelpubliek (gemengd): ervaren beroepsbeoefenaar (5-15 jaar accountancy-ervaring) die de drie eerdere afleveringen al gehoord heeft, soms een geïnteresseerde leek mee. Toon: vakgesprek tussen gecertificeerde accountants (of GA + kandidaat-GA), volgbaar voor de leek. De stagiair-luisteraar vangt het gesprek op, wordt niet rechtstreeks aangesproken.

Behandel de Rotex-illustratie uit het bundle als illustratie van een principe, niet als feit of wereldwijde regel. Spreek niet uit naam van de examinator.


Korte consolidatie-aflevering. Geen nieuwe stof.

Wat de luisteraar na deze recap moet kunnen:
- De vier zwaartepunten van Analyse van de jaarrekening in eigen woorden positioneren (fundament → ratio-families → diagnose-synthese → kritische blik)
- Per zwaartepunt het kernspanningsveld benoemen (waar zit de cognitieve last, niet waar de feitenkennis)

Onderwerpen die aan bod moeten komen (één keer kort per blok):
- Gebruiker-doel-ratio-driehoek + analytische balans als vertrekpunt
- De vier ratio-families en hun interpretatieve valkuilen
- Synthese: drie assen tegelijk lezen + off-balance + bestuursverslag + diagnose-formulering
- Wat analyse NIET kan zeggen — de kritische blik

Tone-hints: consolidatie, geen nieuwe voorbeelden. Vermijd "let's dive in"-openings.
```

---

# 📊 Diapresentatie — één deck voor het hele programmaonderdeel

```text
Gebruik UITSLUITEND inhoud uit het geüploade document `1-3-analyse-notebooklm-bundle.md`. Geen externe bronnen, geen aanvullingen uit andere wetgevingen, geen verzonnen voorbeelden. Bij twijfel: zeg "dit staat niet in het bundle". Belgische context (WVV, KB WVV, CBN) — niet Nederland.

Doelpubliek (gemengd): primair een ervaren beroepsbeoefenaar (5-15 jaar accountancy-ervaring) die de stof opfrist voor het ITAA-examen — niet noodzakelijk dagelijks in dit deelgebied. Daarnaast kan een geïnteresseerde leek het deck bekijken. Toon: vakgesprek tussen twee gecertificeerde accountants (of GA + kandidaat-GA). De stagiair-luisteraar vangt het gesprek op, wordt niet rechtstreeks aangesproken. Vaktermen worden gebruikt zoals in de praktijk; concepten worden gepositioneerd waar nuance telt. Geen pure jargon-stapeling, geen formule-stortvloed.

De Rotex-illustratie uit het bundle is een voorbeeld van een onderliggend principe, geen feit over die onderneming.


Eén slidedeck dat het volledige programmaonderdeel Analyse van de jaarrekening dekt op overzichtsniveau. NotebookLM bepaalt zelf het aantal slides, de volgorde van details binnen elk zwaartepunt, en de visuele indeling.

Wat de student na het doorbladeren van deze deck moet kunnen:
- De gebruiker-doel-ratio-driehoek toepassen op een concrete analyse-vraag
- De vier analyse-doelen en hun typische ratio's reproduceren
- Een analytische balans herkennen op de typische herwerkings-bewegingen ten opzichte van de officiële balans
- De vier ratio-families correct lezen (liquiditeit / solvabiliteit / rentabiliteit / werkkapitaal-cashflow) met aandacht voor interpretatie-valkuilen
- Een diagnose synthetiseren uit meerdere ratio-families + off-balance posten + bestuursverslag
- Aangeven wat een ratio-analyse NIET kan zeggen

Inhoudelijke clusters die in het deck moeten landen:
- Gebruikers, doelen en de analytische balans als vertrekpunt — overzichtsniveau
- Vier analyse-doelen + hun ratio's — vergelijkingstabel uit het bundle
- Liquiditeitsfamilie + werkkapitaalbehoefte — beslisboom welke ratio bij welk type onderneming
- Solvabiliteits- en rentabiliteitsfamilie — focus op interpretatie, niet alleen formules
- Diagnose-synthese: drie assen + off-balance + bestuursverslag
- Trend + sectorbenchmark als context
- Kritische blik: wat de analyse NIET zegt

Stijl: NotebookLM bepaalt zelf alle vormaspecten. Cruciale tabellen en diagrammen uit het bundle (de vier-analyse-doelen-tabel, de liquiditeitsbeslisboom, de vergelijkingsparen-matrix) mogen letterlijk over. Eén deck, gemaakt om snel doorheen te bladeren als revisie — niet om de detail-stof te vervangen.
```

---

# 🎨 Overzichts-infographic — structuur van het hele programmaonderdeel

```text
Gebruik UITSLUITEND inhoud uit het geüploade document `1-3-analyse-notebooklm-bundle.md`. Geen externe bronnen, geen aanvullingen uit andere wetgevingen, geen verzonnen voorbeelden. Bij twijfel: zeg "dit staat niet in het bundle". Belgische context (WVV, KB WVV, CBN) — niet Nederland.

Doelpubliek (gemengd): ervaren beroepsbeoefenaar bereidt het ITAA-examen voor, met af en toe een geïnteresseerde leek die meekijkt. Vaktermen gebruiken zoals in de praktijk; geen pure jargon-stapeling, geen formule-stortvloed.

De Rotex-illustratie uit het bundle is een voorbeeld van een onderliggend principe.


Eén infographic-pagina die het hele programmaonderdeel Analyse van de jaarrekening visueel ordent. NotebookLM bepaalt zelf de indeling, kleurkeuze en grafische metaforen.

Centrale boodschap: financiële analyse leest als een cyclus — van gebruiker en doel (waarom analyseer ik?) via analytische balans (wat is het echte cijfer-vertrekpunt?) naar de vier ratio-families (wat meten we?) en uiteindelijk naar coherente diagnose + verbeteradvies (wat betekent het en wat doen we ermee?). Het sluitstuk is de kritische blik: wat de analyse NIET kan zeggen.

Wat de student na het bekijken van deze infographic moet kunnen:
- De architectuur van het programmaonderdeel beschrijven als analyse-cyclus in vier zwaartepunten
- Per zwaartepunt benoemen welk type cognitieve last erin zit (kader-keuze, technische berekening + interpretatie, synthese-redenering, professionele houding)
- Wijzen op de twee blokken waar de echte examenklassiekers zitten

Inhoudelijke elementen die moeten doorkomen:
- De analyse-cyclus als hoofdstructuur: gebruiker → analytische balans → ratio's → diagnose → advies → kritische blik
- De vier zwaartepunten als architectonisch overzicht
- Per zwaartepunt: één zin "wat zit erin" + één zin "waar de last zit"
- Aanduiding welke twee blokken in deep-dive-afleveringen worden uitgewerkt

Stijl: NotebookLM kiest de indeling. Houd de accentkleuren coherent over alle infographics voor Analyse van de jaarrekening (dit deck + de twee cluster-infographics hieronder).
```

---

# 🎨 Cluster-infographic 1 — Ratio-families-overzicht

```text
Gebruik UITSLUITEND inhoud uit het geüploade document `1-3-analyse-notebooklm-bundle.md`. Geen externe bronnen, geen aanvullingen uit andere wetgevingen, geen verzonnen voorbeelden. Bij twijfel: zeg "dit staat niet in het bundle". Belgische context (WVV, KB WVV, CBN) — niet Nederland.

Doelpubliek: ervaren beroepsbeoefenaar die de stof opfrist. De Rotex-illustratie uit het bundle is een voorbeeld.


Eén infographic-pagina die de vier ratio-families zij-aan-zij plaatst — dieper dan de overzichts-infographic.

Centrale boodschap: bij financiële analyse zijn er vier ratio-families, elk met een eigen tijdshorizon en perspectief — liquiditeit (kortetermijn, kasvermogen), solvabiliteit (langetermijn, structurele draagkracht), rentabiliteit (verdienvermogen op meerdere niveaus), werkkapitaal + kasstroom (operationele cyclus). Ratio's zijn niet inwisselbaar; een lage current ratio bij negatieve werkkapitaalbehoefte is iets totaal anders dan bij een productie-onderneming.

Wat de student na het bekijken van deze infographic moet kunnen:
- Per ratio-familie de kernratio's en hun perspectief plaatsen
- De richtwaarden uit het bundle reproduceren als richtsnoer, niet als wet
- De typische valkuil per familie benoemen (current ratio zonder werkkapitaalbehoefte / solvabiliteit zonder off-balance / ROE zonder DuPont-decompositie / marges zonder eenmalige posten)

Inhoudelijke elementen die moeten doorkomen:
- De vier ratio-families als vier kwadranten of vier lanen
- Per familie: kernratio's, wat ze meten, richtwaarde, kernvalkuil
- De werkkapitaalbeslisboom uit het bundle (welke liquiditeitsratio bij welk type onderneming)
- Eén Rotex-aanwijzing als illustratief moment (lage current ratio + negatieve werkkapitaalbehoefte) — expliciet als voorbeeld
- Korte verwijzing naar sector-benchmark als noodzakelijke context

Stijl: NotebookLM kiest de indeling. Coherent met de overzichts-infographic + de andere cluster-infographic.
```

---

# 🎨 Cluster-infographic 2 — Diagnose-synthese: drie assen + off-balance + bestuursverslag

```text
Gebruik UITSLUITEND inhoud uit het geüploade document `1-3-analyse-notebooklm-bundle.md`. Geen externe bronnen, geen aanvullingen uit andere wetgevingen, geen verzonnen voorbeelden. Bij twijfel: zeg "dit staat niet in het bundle". Belgische context (WVV, KB WVV, CBN) — niet Nederland.

Doelpubliek: ervaren beroepsbeoefenaar die de stof opfrist. De Rotex-illustratie uit het bundle is een voorbeeld.


Eén infographic-pagina die het diagnose-synthese-mechanisme visueel uitwerkt — hoe drie ratio-assen samenkomen, hoe off-balance posten en de toelichting het beeld kantelen, en hoe het bestuursverslag een extra signaal-laag toevoegt.

Centrale boodschap: een financiële diagnose is geen optelsom van ratio's — het is een redeneerlijn die drie assen (liquiditeit / solvabiliteit / rentabiliteit) samenleest, off-balance posten en hangende rechtszaken meeneemt, en het bestuursverslag + niet-financiële informatie als signaalbron benut. De diagnose noemt oorzaak (operationeel / financieel / structureel) en mondt uit in een concreet verbeteradvies.

Wat de student na het bekijken van deze infographic moet kunnen:
- De drie analyse-assen als gelijktijdige lezing toepassen op een casus
- Off-balance posten correct positioneren ten opzichte van de balans-ratio's
- Het bestuursverslag lezen als signaalbron — niet enkel als verplichting
- Een diagnose-uitspraak formuleren (kernspanningsveld + oorzaak + advies)

Inhoudelijke elementen die moeten doorkomen:
- De drie assen als gelijktijdige lezing — typische combinaties en hun betekenis
- Off-balance + toelichting als correctie-laag op de ratio's
- Bestuursverslag + niet-financiële informatie als signaal-laag
- Trend + sectorbenchmark als context-laag
- De Rotex-illustratie als doorlopend voorbeeld — expliciet als voorbeeld, niet als regel
- De diagnose-uitspraak als sluitstuk: kernspanningsveld → oorzaak → advies
- Kritische blik: wat de analyse NIET zegt — kort als rand-element

Stijl: NotebookLM kiest de indeling. Coherent met de overzichts-infographic + de andere cluster-infographic.
```

---

## Plan-samenvatting (1 oogopslag)

| Volgorde | Output | Lengte / formaat | Daglimiet? |
|---|---|---|---|
| 1 | 🎙️ Inleidende podcast | ±20 min | Telt in 3/dag NL-podcasts |
| 2 | 🎙️ Deep-dive 1 — ratio-families | ±20 min | Telt in 3/dag |
| 3 | 🎙️ Deep-dive 2 — van ratio's naar diagnose | ±20 min | Telt in 3/dag |
| 4 | 🎙️ Recap (optioneel, dag 2) | ±8-10 min | Telt in 3/dag |
| — | 📊 Slidedeck (één voor heel programmaonderdeel) | Aantal slides vrij | Geen limiet |
| — | 🎨 Overzichts-infographic | Eén pagina | Geen limiet |
| — | 🎨 Cluster-infographic 1 — ratio-families | Eén pagina | Geen limiet |
| — | 🎨 Cluster-infographic 2 — diagnose-synthese | Eén pagina | Geen limiet |

Plan past in 1 dag voor de drie kern-podcasts; visuele afgeleiden parallel.
