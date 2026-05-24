---
title: "NotebookLM-afgeleiden — Geconsolideerde jaarrekening"
description: "Prompts per output-type voor het programmaonderdeel Geconsolideerde jaarrekening. Bronset = `1-4-geconsolideerde-jaarrekening-notebooklm-bundle.md`. Eén intro-podcast + twee deep-dives + één slidedeck + één algemene infographic + twee cluster-infographics. Stuurt op leeruitkomsten — NotebookLM krijgt creatieve vrijheid in vorm."
gegenereerd_op: "2026-05-19"
status: experiment
---

# Afgeleiden-plan — Geconsolideerde jaarrekening

> **Bronset (zelfde voor alle afgeleiden):** `exports/1.4/1-4-geconsolideerde-jaarrekening-notebooklm-bundle.md`
> **Daglimiet podcasts (NL):** 3 afleveringen/dag in NotebookLM. Plan past in 1 dag (3 podcasts) + optionele recap dag 2.

---

## Inhoud van dit plan

| Output-type | Aantal | Wat |
|---|---|---|
| 🎙️ Inleidende podcast | 1 | Gatekeeper (moet ik consolideren?) + algemeen kader |
| 🎙️ Deep-dive podcasts | 2 | Kwalificeren + kiezen (relatie → percentage → methode) · Uitvoeren (harmoniseren + eerste consolidatie + eliminaties + kringwijzigingen) |
| 🎙️ Recap podcast (optioneel) | 1 | Consolidatie zonder nieuwe stof |
| 📊 Diapresentatie | 1 | Eén deck voor het hele programmaonderdeel |
| 🎨 Overzichts-infographic | 1 | Visualiseert de natuurlijke werkvolgorde van een consolidatiedossier |
| 🎨 Cluster-infographics | 2 | Beslisboom consolidatieplicht + methodes-matrix · Controle- vs. belangenpercentage in een keten |

---

## Cognitieve kaart van het programmaonderdeel

Wat zit er inhoudelijk in Geconsolideerde jaarrekening? Drie zwaartepunten — de intro dekt de gatekeeper en het algemeen kader, de twee deep-dives splitsen de kerntechniek in *kwalificeren + kiezen* enerzijds en *uitvoeren* anderzijds.

| # | Zwaartepunt | Inhoud | Diepduik-waardig? |
|---|---|---|---|
| 1 | Gatekeeper + algemeen kader | Waarom consolideren, vijf parallelle toetsen voor de consolidatieplicht, vrijstelling beperkte omvang, vrijstelling subconsolidatie, consortium-piste | Nee — komt in intro |
| 2 | Kwalificeren + kiezen | Relatie kwalificeren (exclusieve controle / gezamenlijke controle / invloed van betekenis) → controlepercentage versus belangenpercentage in een keten → methode (integraal / evenredig / vermogensmutatie / horizontaal) | **Ja — deep-dive 1** |
| 3 | Uitvoeren | Uniforme waarderingsregels harmoniseren → eerste consolidatie → consolidatieverschil → intragroep-eliminaties → minderheidsbelangen → kringwijzigingen en step acquisition | **Ja — deep-dive 2** |

---

## Doelpubliek, voorbeelden, examen-stress — verwerkt in elke prompt

De volgende drie verankeringen staan IN elke prompt hieronder ingewerkt. Ter referentie hier afzonderlijk.

**Doelpubliek (gemengd):** primair een ervaren beroepsbeoefenaar (typisch 5-15 jaar in het accountancyberoep) die zich voorbereidt op het ITAA-bekwaamheidsexamen Gecertificeerd Accountant — niet noodzakelijk dagelijks in consolidatiedossiers. Daarnaast luistert er af en toe een geïnteresseerde leek mee. De stof moet voor de beroepsbeoefenaar **voldoende diep** zijn (concept-nuance, examensubtiliteiten, multi-conceptueel redeneren) maar voor de leek **volgbaar** (geen pure jargon-stapeling, geen legalese). Toon: een vakgesprek tussen twee gecertificeerde accountants — of tussen een gecertificeerd accountant en een kandidaat-GA. De stagiair die zich op het examen voorbereidt luistert mee, maar wordt niet als publiek toegesproken. Vaktermen worden gebruikt zoals ze in de praktijk vallen, maar concepten worden kort gepositioneerd wanneer nuance telt. Geen pedagogische "laten we eens uitleggen wat een dochteronderneming is"-momenten; wel "let op — in deze context betekent 'controle' niet zomaar 'meerderheid van aandelen' maar 'meerderheid van stemrechten of controle in feite'".

**Voorbeelden:** de concrete keten in het bundle (`Aurelia Holding NV` met de structuur Aurelia → A (70%) → C (60%) en Aurelia → B (30%) → C (20%)) is een illustratie van een onderliggend principe — niet een feit over een bestaande onderneming, niet de wereldwijde regel. Spreek het principe uit via de illustratie en blijf bij het principe. Vermijd zinnen als "bij Aurelia is het altijd zo" — wel: "in deze illustratie zien we waarom een keten breekt zodra er een niet-gecontroleerde schakel tussen zit".

**Examen-tone:** spreek niet uit naam van de examinator. Voorbeeldexamens zijn data over wat in het verleden gevraagd is, geen voorschriften voor wat absoluut moet. Vermijd stress-taal als "je moet absoluut", "de examinator verwacht", "u moet". Mag wel: "op integratieniveau wordt vaak verwacht", "in voorbeeldexamens komen geregeld diagrammen met percentages voor", "wie deze stof beheerst kan...". Toon van een collega die mee voorbereidt, niet een examinator die toetst.

---

## Anti-fabricatie

Geldt in elke prompt: **gebruik UITSLUITEND inhoud uit het geüploade document `1-4-geconsolideerde-jaarrekening-notebooklm-bundle.md`.** Geen externe bronnen, geen aanvullingen uit andere wetgevingen, geen verzonnen voorbeelden. Bij twijfel: zeg "dit staat niet in het bundle". Belgische context (WVV, KB WVV, CBN, IFRS-EU voor IFRS-raamwerk-aspect) — niet Nederland.

---

# 🎙️ Inleidende podcast (±20 min)

```text
Gebruik UITSLUITEND inhoud uit het geüploade document `1-4-geconsolideerde-jaarrekening-notebooklm-bundle.md`. Geen externe bronnen, geen aanvullingen uit andere wetgevingen, geen verzonnen voorbeelden. Bij twijfel: zeg "dit staat niet in het bundle". Belgische context (WVV, KB WVV, CBN, IFRS-EU voor IFRS-raamwerk-aspect) — niet Nederland.

Doelpubliek (gemengd): primair een ervaren beroepsbeoefenaar (5-15 jaar accountancy-ervaring) die het ITAA-examen voorbereidt — niet noodzakelijk dagelijks in consolidatiedossiers. Daarnaast luistert af en toe een geïnteresseerde leek mee. Toon: vakgesprek tussen twee gecertificeerde accountants (of GA + kandidaat-GA). De stagiair-luisteraar vangt het gesprek op, wordt niet rechtstreeks aangesproken. Voldoende diep voor de beroepsbeoefenaar (concept-nuance, multi-conceptueel redeneren), volgbaar voor de leek (geen pure jargon-stapeling, geen legalese). Vaktermen worden gebruikt zoals in de praktijk; concepten worden kort gepositioneerd waar nuance telt. Geen pedagogische "wat is een dochter"-uitleg; wel kort verduidelijken wanneer een term in deze context een specifieke betekenis krijgt (controle ≠ meerderheid van aandelen; belangenpercentage ≠ controlepercentage).

Behandel de concrete groepsstructuur uit het bundle (`Aurelia Holding NV` met de keten Aurelia → A (70%) → C (60%) en Aurelia → B (30%) → C (20%)) als illustratie van een onderliggend principe, niet als feit over een bestaande onderneming of als wereldwijde regel.

Spreek niet uit naam van de examinator. Voorbeeldexamens zijn data, geen voorschriften. Vermijd "je moet absoluut" / "de examinator verwacht". Toon van een collega die meeloopt met het examenvoorbereidingstraject, niet van een autoriteit.

Dit is de inleidende aflevering over Geconsolideerde jaarrekening. Doel: de luisteraar krijgt een coherent overzicht van het programmaonderdeel én de mentale kapstok om de twee deep-dive-afleveringen straks te plaatsen. Focus van deze intro: de gatekeeper-vraag (moet ik überhaupt consolideren?) en het algemeen kader (waarom bestaat een geconsolideerde jaarrekening, wat lost ze op).

Wat de luisteraar na deze aflevering moet kunnen:
- Verwoorden waarom een geconsolideerde jaarrekening bestaat — de juridische pluraliteit van een groep economisch herleiden tot één geheel, onderlinge stromen schrappen, derden afzonderen
- De vijf parallelle toetsen voor consolidatieplicht opnoemen (rechtspersoonlijkheid moeder · controle bestaat · eventueel consortium-piste · groottecriteria op geconsolideerde basis · vrijstelling subconsolidatie) en aanvoelen dat één 'nee' in een van die toetsen de plicht wegneemt
- Het verschil tussen "groep van beperkte omvang" en "vrijstelling subconsolidatie" plaatsen, plus weten dat beursnotering beide vrijstellingen breekt
- Aanvoelen dat de echte cognitieve last in twee blokken zit: (a) kwalificeren + kiezen — relatie → percentage → methode, en (b) uitvoeren — harmoniseren + eerste consolidatie + eliminaties + kringwijzigingen — en weten dat de twee deep-dives die volgen

Onderwerpen die aan bod moeten komen (volgorde en pacing vrij):
- Waarom een geconsolideerde jaarrekening — onderlinge verkopen en leningen tussen moeder en dochter kunnen op enkelvoudige basis een gezond plaatje tonen dat economisch niet bestaat
- De drie werkwoorden van het consolidatiewerk: kwalificeren (welke relatie is het?), kiezen (welke techniek hoort daarbij?) en rekenen (eliminaties + derden afzonderen)
- De vijf gatekeeper-toetsen als parallelle filters, niet als opeenvolgende stappen — elke toets kan op zich de plicht wegnemen
- Consortium als horizontale variant — leden onder gemeenschappelijke leiding zonder echte moeder, eventueel een natuurlijke persoon als leiding
- De vrijstellingen 'groep van beperkte omvang' en 'subconsolidatie' kort positioneren, met beursnotering als breekpunt
- Aankondiging van de twee deep-dives: relatie → percentage → methode versus uitvoeren van de consolidatie zelf
- Korte aanstip van het IFRS-raamwerk (IFRS 3/10/11/12) als alternatief regime — alleen positioneren, geen detail

Tone-hints: spreek de luisteraar aan als collega die het deelgebied wil opfrissen voor het examen, niet als beginner. Vermijd "let's dive in"-openings. Geen cijferreeksen — audio-medium.
```

---

# 🎙️ Deep-dive 1 — Kwalificeren + kiezen: van relatie naar methode (±20 min)

```text
Gebruik UITSLUITEND inhoud uit het geüploade document `1-4-geconsolideerde-jaarrekening-notebooklm-bundle.md`. Geen externe bronnen, geen aanvullingen uit andere wetgevingen, geen verzonnen voorbeelden. Bij twijfel: zeg "dit staat niet in het bundle". Belgische context (WVV, KB WVV, CBN, IFRS-EU voor IFRS-raamwerk-aspect) — niet Nederland.

Doelpubliek (gemengd): ervaren beroepsbeoefenaar (5-15 jaar accountancy-ervaring) bereidt het ITAA-examen voor, soms luistert een geïnteresseerde leek mee. Toon: vakgesprek tussen twee gecertificeerde accountants (of GA + kandidaat-GA). De stagiair-luisteraar vangt het gesprek op, wordt niet rechtstreeks aangesproken. Voldoende diep voor de beroepsbeoefenaar, volgbaar voor de leek. Vaktermen worden gebruikt zoals in de praktijk; concepten worden kort gepositioneerd waar nuance telt. Geen pedagogische basisuitleg.

Behandel de groepsstructuur uit het bundle (`Aurelia Holding NV` → A (70%) → C (60%) én Aurelia → B (30%) → C (20%)) als illustratie van een onderliggend principe, niet als feit over een bestaande onderneming of als wereldwijde regel.

Spreek niet uit naam van de examinator. Voorbeeldexamens zijn data, geen voorschriften. Toon van een collega die meedenkt, niet van een autoriteit.

Deep-dive-aflevering: de keten "relatie → percentage → methode". Bouwt op de inleidende aflevering (gatekeeper + algemeen kader). Geen herhaling van die basis — direct in de cognitieve last.

Wat de luisteraar na deze aflevering moet kunnen:
- Een deelneming kwalificeren via drie filters — exclusieve controle, gezamenlijke controle of invloed van betekenis — en aanduiden welke wettelijke drempelvermoedens daarbij spelen (> 50 % stemrechten · vennoten-overeenkomst · ≥ 20 % stemrechten)
- Het cruciale onderscheid maken tussen controlepercentage (stemrechten — niet doorvermenigvuldigen door een gecontroleerde schakel) en belangenpercentage (kapitaalaandeel — wel doorlopend vermenigvuldigen)
- Begrijpen waarom een keten "breekt" bij een niet-gecontroleerde tussenschakel: de stemrechten van die tussenschakel zijn niet van de moeder, dus tellen niet mee voor het controlepercentage hogerop
- De vier consolidatietechnieken aan de juiste kwalificatie koppelen — integraal bij exclusieve controle, evenredig bij gezamenlijke controle (mits geïntegreerd), vermogensmutatie bij invloed van betekenis of losse gemeenschappelijke dochter, horizontaal bij consortium
- Een grenscasus duiden waarbij een gemeenschappelijke dochter los van de groep opereert: de evenredige consolidatie kantelt naar vermogensmutatie

Onderwerpen die aan bod moeten komen (volgorde en pacing vrij):
- Drie kwalificatie-filters — exclusieve controle / gezamenlijke controle / invloed van betekenis — met de wettelijke drempelvermoedens, en het scharnier tussen 'controle' en 'invloed van betekenis' (de eerste maakt iemand moeder, de tweede leidt tot vermogensmutatie zonder consolidatieplicht)
- Controlepercentage versus belangenpercentage: waarom het twee verschillende sommen zijn met een verschillende reken-conventie
- De illustratie uit het bundle (Aurelia → A → C en Aurelia → B → C): waarom A's stem in C wél meetelt voor Aurelia's controle (Aurelia heeft exclusieve controle over A) en B's stem in C niét meetelt (Aurelia heeft enkel invloed van betekenis over B → keten breekt). Belangenpercentage loopt wél door beide kanten — 70 % × 60 % + 30 % × 20 %
- De vier consolidatietechnieken naast elkaar — wat verschilt op de balans, en hoe derden-belangen verschijnen (apart bij integraal, niet apart bij evenredig of vermogensmutatie)
- Het kantelpunt 'gemeenschappelijke dochter die los van de groep opereert' — van evenredige consolidatie naar vermogensmutatie
- Horizontale consolidatie als buitenbeentje (geen moeder, alleen consortium-leden onder gemeenschappelijke leiding — die leiding kan een natuurlijke persoon zijn)
- Korte stip op IFRS (IFRS 10 controle-definitie, IFRS 11 joint arrangements) — alleen positioneren, geen detail buiten het bundle

Tone-hints: dichte stof — pacing en accentuering aan de hosts. Vermijd "let's dive in"-openings. Geen cijferreeksen behalve waar één doorgewerkt voorbeeld de redenering draagt. Behandel de Aurelia-illustratie expliciet als voorbeeld, niet als de norm.
```

---

# 🎙️ Deep-dive 2 — Uitvoeren: harmoniseren, eerste consolidatie, eliminaties, kringwijzigingen (±20 min)

```text
Gebruik UITSLUITEND inhoud uit het geüploade document `1-4-geconsolideerde-jaarrekening-notebooklm-bundle.md`. Geen externe bronnen, geen aanvullingen uit andere wetgevingen, geen verzonnen voorbeelden. Bij twijfel: zeg "dit staat niet in het bundle". Belgische context (WVV, KB WVV, CBN, IFRS-EU voor IFRS-raamwerk-aspect) — niet Nederland.

Doelpubliek (gemengd): ervaren beroepsbeoefenaar (5-15 jaar accountancy-ervaring) bereidt het ITAA-examen voor, soms luistert een geïnteresseerde leek mee. Toon: vakgesprek tussen twee gecertificeerde accountants (of GA + kandidaat-GA). De stagiair-luisteraar vangt het gesprek op, wordt niet rechtstreeks aangesproken. Voldoende diep voor de beroepsbeoefenaar, volgbaar voor de leek. Vaktermen worden gebruikt zoals in de praktijk; concepten worden kort gepositioneerd waar nuance telt. Geen pedagogische basisuitleg.

Behandel de groepsstructuur uit het bundle (`Aurelia Holding NV`-keten) als illustratie van een onderliggend principe, niet als feit over een bestaande onderneming of als wereldwijde regel.

Spreek niet uit naam van de examinator. Voorbeeldexamens zijn data, geen voorschriften. Toon van een collega die meedenkt, niet van een autoriteit.

Deep-dive-aflevering: het feitelijke uitvoeren van de consolidatie zodra je weet welke methode bij welke entiteit hoort. Bouwt op deep-dive 1 (kwalificeren + kiezen). Geen herhaling — direct in de uitvoering.

Wat de luisteraar na deze aflevering moet kunnen:
- Verwoorden waarom uniforme waarderingsregels nodig zijn vóór je optelt: dezelfde regels die de moeder enkelvoudig hanteert gelden ook geconsolideerd, behoudens gemotiveerde uitzonderingen — anders tel je appelen bij peren
- De stappen van de eerste consolidatie volgen: aankoopprijs van de aandelen vergelijken met het pro-rata aandeel in het eigen vermogen op aankoopdatum → eerst stille meer- of minderwaarden op identificeerbare activa toerekenen → het residu boeken als consolidatieverschil (positief = goodwill-achtig, negatief = bargain purchase in BE GAAP-versie)
- De vier hoofdtypes intragroep-eliminaties herkennen — onderlinge vorderingen tegen schulden, onderlinge opbrengsten tegen kosten, niet-gerealiseerde winsten op voorraden, niet-gerealiseerde winsten op vaste activa — en het belangenpercentage gebruiken om het derden-deel correct af te zonderen
- De aparte presentatiepost 'belangen van derden' (passief) en 'aandeel van derden in het resultaat' (resultatenrekening) plaatsen, en weten dat die posten *uitsluitend bij integrale consolidatie* bestaan
- Een kringwijziging procedureel doorlopen: nieuwe verwerving → eerste consolidatie; verkoop → uitsluiten + resultaat realiseren; step acquisition → al gehouden belang herwaarderen op het moment dat controle ontstaat; kantel-moment van geassocieerde naar dochter → overgang tussen technieken
- De afsluitingsdatum-regel duiden: maximaal 3 maanden afwijking tussen dochter en geconsolideerde jaarrekening, mits motivering in de toelichting

Onderwerpen die aan bod moeten komen (volgorde en pacing vrij):
- Harmoniseren van waarderingsregels als eerste stap — waarom je niet zomaar mag optellen
- De eerste consolidatie als drie-stappen-redenering: vergelijken → toerekenen aan stille meer-/minderwaarden → residu in consolidatieverschil. De vier voornaamste oorzaken van een positief consolidatieverschil (uit het bundle)
- Intragroep-eliminaties — vorderingen ↔ schulden, opbrengsten ↔ kosten, niet-gerealiseerde winsten in voorraden, niet-gerealiseerde winsten in vaste activa
- Aandeel van derden in resultaat én balans — bestaat alleen bij integrale consolidatie (essentieel examenfeit); bij evenredige consolidatie en vermogensmutatie zit het derden-deel niet apart in de cijfers
- Kringwijzigingen: nieuwe verwerving, verkoop, step acquisition (al gehouden belang herwaarderen op het kantel-moment), overgang geassocieerde → dochter
- De afsluitingsdatum-regel (max. 3 maanden afwijking, motivering in toelichting) als veelvoorkomende examenvraag
- Korte stip op het jaarverslag bij de groep — narratief stuk naast de cijfers; weten welk type informatie waarin thuishoort

Tone-hints: stappenwerk met meerdere haakjes — laat de hosts elke fase apart afhandelen. Vermijd "let's dive in"-openings. Geen cijferreeksen behalve waar één doorgewerkte stap de redenering draagt. Behandel het bundle-voorbeeld als illustratie van het principe, niet als de norm.
```

---

# 🎙️ Recap podcast (optioneel, ±8-10 min)

```text
Gebruik UITSLUITEND inhoud uit het geüploade document `1-4-geconsolideerde-jaarrekening-notebooklm-bundle.md`. Geen externe bronnen, geen aanvullingen uit andere wetgevingen, geen verzonnen voorbeelden. Bij twijfel: zeg "dit staat niet in het bundle". Belgische context (WVV, KB WVV, CBN, IFRS-EU voor IFRS-raamwerk-aspect) — niet Nederland.

Doelpubliek (gemengd): ervaren beroepsbeoefenaar (5-15 jaar accountancy-ervaring) die de drie eerdere afleveringen al gehoord heeft, soms een geïnteresseerde leek mee. Toon: vakgesprek tussen gecertificeerde accountants (of GA + kandidaat-GA), volgbaar voor de leek. De stagiair-luisteraar vangt het gesprek op, wordt niet rechtstreeks aangesproken.

Behandel de Aurelia-keten uit het bundle als illustratie van een principe, niet als feit of wereldwijde regel. Spreek niet uit naam van de examinator.

Korte consolidatie-aflevering. Geen nieuwe stof.

Wat de luisteraar na deze recap moet kunnen:
- De natuurlijke werkvolgorde van een consolidatiedossier in eigen woorden positioneren (gatekeeper → kwalificeren → kiezen → uitvoeren)
- Per blok het kernspanningsveld benoemen (waar zit de cognitieve last, niet waar de feitenkennis)

Onderwerpen die aan bod moeten komen (één keer kort per blok):
- Gatekeeper: vijf parallelle toetsen voor de consolidatieplicht
- Kwalificeren: drie filters (exclusieve controle / gezamenlijke controle / invloed van betekenis)
- Controlepercentage versus belangenpercentage — twee verschillende sommen, één keten breekt waar geen controle is
- Kiezen: vier technieken aan de drie kwalificaties gekoppeld (+ horizontaal voor consortium)
- Uitvoeren: harmoniseren → eerste consolidatie + consolidatieverschil → intragroep-eliminaties + derden → kringwijzigingen

Tone-hints: consolidatie, geen nieuwe voorbeelden. Vermijd "let's dive in"-openings.
```

---

# 📊 Diapresentatie — één deck voor het hele programmaonderdeel

```text
Gebruik UITSLUITEND inhoud uit het geüploade document `1-4-geconsolideerde-jaarrekening-notebooklm-bundle.md`. Geen externe bronnen, geen aanvullingen uit andere wetgevingen, geen verzonnen voorbeelden. Bij twijfel: zeg "dit staat niet in het bundle". Belgische context (WVV, KB WVV, CBN, IFRS-EU voor IFRS-raamwerk-aspect) — niet Nederland.

Doelpubliek (gemengd): primair een ervaren beroepsbeoefenaar (5-15 jaar accountancy-ervaring) die de stof opfrist voor het ITAA-examen — niet noodzakelijk dagelijks in consolidatiedossiers. Daarnaast kan een geïnteresseerde leek het deck bekijken. Toon: vakgesprek tussen twee gecertificeerde accountants (of GA + kandidaat-GA). De stagiair-luisteraar vangt het gesprek op, wordt niet rechtstreeks aangesproken. Vaktermen worden gebruikt zoals in de praktijk; concepten worden gepositioneerd waar nuance telt. Geen pure jargon-stapeling, geen legalese.

De Aurelia-keten uit het bundle is een illustratie van een principe, geen feit over een bestaande onderneming.

Eén slidedeck dat het volledige programmaonderdeel Geconsolideerde jaarrekening dekt op overzichtsniveau. NotebookLM bepaalt zelf het aantal slides, de volgorde van details binnen elk zwaartepunt, en de visuele indeling.

Wat de student na het doorbladeren van deze deck moet kunnen:
- De vijf parallelle toetsen voor de consolidatieplicht herkennen + de twee vrijstellingen (groep van beperkte omvang · subconsolidatie) met beursnotering als breekpunt
- Een deelneming kwalificeren als exclusieve controle, gezamenlijke controle of invloed van betekenis op basis van de wettelijke drempelvermoedens
- Een ketenstructuur uitrekenen: controlepercentage (niet vermenigvuldigen door een gecontroleerde schakel; keten breekt bij geen controle) versus belangenpercentage (wel doorlopend vermenigvuldigen langs alle paden)
- De vier consolidatietechnieken kiezen op basis van de kwalificatie (integraal · evenredig · vermogensmutatie · horizontaal)
- De stappen van een eerste consolidatie schetsen + de definitie en vier oorzaken van een positief consolidatieverschil
- De drie hoofdtypes intragroep-eliminaties opnoemen + weten dat 'aandeel van derden' alleen bij integrale consolidatie als aparte post verschijnt
- De drempelwaarden uit de cheatsheet plaatsen (> 50 % stemrechten · ≥ 20 % stemrechten · 3 maanden afwijking afsluitingsdatum)

Inhoudelijke clusters die in het deck moeten landen:
- Gatekeeper-beslisboom voor de consolidatieplicht (vijf parallelle toetsen) — beslisboom uit het bundle mag letterlijk over
- Begrippenkader: controle (in rechte / in feite) · moeder · dochter · gemeenschappelijke dochter · geassocieerde · consortium
- Kwalificatie-trio: exclusieve controle / gezamenlijke controle / invloed van betekenis — met wettelijke drempelvermoedens
- Ketenredenering: controlepercentage versus belangenpercentage, met de illustratie Aurelia → A (70%) → C (60%) én Aurelia → B (30%) → C (20%)
- Vier consolidatietechnieken — methodes-matrix uit het bundle mag letterlijk over (voorwaarde · balans-effect · belangen van derden · consolidatieverschil)
- Uitvoeren: harmoniseren waarderingsregels → eerste consolidatie + drie-stappen-toerekening → intragroep-eliminaties → minderheidsbelangen
- Kringwijzigingen: nieuwe verwerving · verkoop · step acquisition · kantel-moment geassocieerde → dochter
- Cheatsheet drempelwaarden + vergelijkingsparen-matrix
- IFRS-aanstip (IFRS 3/10/11/12) — alleen positionerend, geen detail

Stijl: NotebookLM bepaalt zelf alle vormaspecten. Cruciale tabellen, beslisbomen en de methodes-matrix uit het bundle mogen letterlijk over. Eén deck, gemaakt om snel doorheen te bladeren als revisie — niet om de detail-stof te vervangen.
```

---

# 🎨 Overzichts-infographic — werkvolgorde van een consolidatiedossier

```text
Gebruik UITSLUITEND inhoud uit het geüploade document `1-4-geconsolideerde-jaarrekening-notebooklm-bundle.md`. Geen externe bronnen, geen aanvullingen uit andere wetgevingen, geen verzonnen voorbeelden. Bij twijfel: zeg "dit staat niet in het bundle". Belgische context (WVV, KB WVV, CBN, IFRS-EU voor IFRS-raamwerk-aspect) — niet Nederland.

Doelpubliek (gemengd): ervaren beroepsbeoefenaar bereidt het ITAA-examen voor, met af en toe een geïnteresseerde leek die meekijkt. Vaktermen gebruiken zoals in de praktijk; geen pure jargon-stapeling, geen legalese.

De Aurelia-keten uit het bundle is een illustratie van een principe.

Eén infographic-pagina die de natuurlijke werkvolgorde van een consolidatiedossier visueel ordent. NotebookLM bepaalt zelf de indeling, kleurkeuze en grafische metaforen.

Centrale boodschap: een consolidatiedossier leest van *gatekeeper* naar *uitvoering* — eerst aftoetsen of er überhaupt moet worden geconsolideerd, dan elke deelneming kwalificeren, dan per kwalificatie een techniek kiezen, en pas dan de feitelijke optelling met harmonisatie, eerste consolidatie en eliminaties uitvoeren.

Wat de student na het bekijken van deze infographic moet kunnen:
- De vier fases van een consolidatiedossier in volgorde opnoemen (gatekeeper → kwalificeren → kiezen → uitvoeren)
- Per fase benoemen welk type cognitieve last erin zit (toetsen-check, drempel-redenering, conditioneel methode-mapping, multi-stappen uitvoering)
- Wijzen op de twee blokken waar de meeste examenklassiekers zitten (ketenredenering controle/belang + eerste consolidatie / consolidatieverschil)

Inhoudelijke elementen die moeten doorkomen:
- De vier fases als architectonisch overzicht, met pijl-doorloop
- Per fase: één zin "wat zit erin" + één zin "waar de last zit"
- Aanduiding welke twee blokken in deep-dive-afleveringen worden uitgewerkt
- Een mini-glossary van drie verwarrings-paren (controle ↔ controlepercentage · controlepercentage ↔ belangenpercentage · integrale ↔ evenredige consolidatie)

Stijl: NotebookLM kiest de indeling. Houd de accentkleuren coherent over alle infographics voor Geconsolideerde jaarrekening (dit deck + de twee cluster-infographics hieronder).
```

---

# 🎨 Cluster-infographic 1 — Beslisboom consolidatieplicht + methodes-matrix

```text
Gebruik UITSLUITEND inhoud uit het geüploade document `1-4-geconsolideerde-jaarrekening-notebooklm-bundle.md`. Geen externe bronnen, geen aanvullingen uit andere wetgevingen, geen verzonnen voorbeelden. Bij twijfel: zeg "dit staat niet in het bundle". Belgische context (WVV, KB WVV, CBN, IFRS-EU voor IFRS-raamwerk-aspect) — niet Nederland.

Doelpubliek: ervaren beroepsbeoefenaar die de stof opfrist. De keten uit het bundle is een illustratie.

Eén infographic-pagina die de gatekeeper-beslisboom (consolidatieplicht) en de methodes-matrix (welke techniek bij welke relatie) op één blad combineert.

Centrale boodschap: het kwalificeren begint vóór de techniek-keuze. Eerst doorloop je vijf parallelle toetsen die elk de plicht kunnen wegnemen; pas dan koppel je per entiteit een kwalificatie aan een methode.

Wat de student na het bekijken van deze infographic moet kunnen:
- De vijf gatekeeper-toetsen achter elkaar opnoemen en aangeven waar elk de plicht wegneemt (geen rechtspersoonlijkheid · geen controle · groep van beperkte omvang · subconsolidatie · enkel consortium)
- De drie kwalificaties (exclusieve controle / gezamenlijke controle / invloed van betekenis) koppelen aan hun bijbehorende techniek (integraal / evenredig / vermogensmutatie) + de buitenbeen-variant horizontaal voor consortium
- Aanvoelen waarom evenredige consolidatie en vermogensmutatie kunnen wisselen bij een gemeenschappelijke dochter (afhankelijk van integratie in de groep)

Inhoudelijke elementen die moeten doorkomen:
- Beslisboom-vorm met vijf parallelle toetsen + uitkomsten (vrijstelling beperkte omvang, vrijstelling subconsolidatie, consortium-piste, consolideren)
- Beursnotering als breekpunt op beide vrijstellingen — apart accent
- Methodes-matrix met vier rijen: voor elke techniek (voorwaarde · op-balans-effect · belangen van derden · consolidatieverschil mogelijk?)
- Korte aanstip van het kantel-moment 'gemeenschappelijke dochter los van de groep → vermogensmutatie i.p.v. evenredig'

Stijl: NotebookLM kiest de indeling. Coherent met de overzichts-infographic + de andere cluster-infographic.
```

---

# 🎨 Cluster-infographic 2 — Controlepercentage versus belangenpercentage in een keten

```text
Gebruik UITSLUITEND inhoud uit het geüploade document `1-4-geconsolideerde-jaarrekening-notebooklm-bundle.md`. Geen externe bronnen, geen aanvullingen uit andere wetgevingen, geen verzonnen voorbeelden. Bij twijfel: zeg "dit staat niet in het bundle". Belgische context (WVV, KB WVV, CBN, IFRS-EU voor IFRS-raamwerk-aspect) — niet Nederland.

Doelpubliek: ervaren beroepsbeoefenaar die de stof opfrist. De Aurelia-keten uit het bundle is een illustratie, geen feit.

Eén infographic-pagina die het verschil tussen controlepercentage en belangenpercentage in een keten visueel uitwerkt.

Centrale boodschap: in een ketenstructuur loopt het belangenpercentage door alle paden (vermenigvuldigen langs elke schakel, alle paden optellen), maar het controlepercentage breekt zodra er een niet-gecontroleerde schakel tussen zit — daar zit het meest klassieke struikelblok van het programmaonderdeel.

Wat de student na het bekijken van deze infographic moet kunnen:
- Voor een gegeven keten het controlepercentage en het belangenpercentage afzonderlijk uitrekenen
- Het breekpunt in een keten herkennen (geen exclusieve controle op een tussenschakel)
- De methode-keuze terugkoppelen aan het controlepercentage (niet aan het belangenpercentage)

Inhoudelijke elementen die moeten doorkomen:
- De Aurelia-keten uit het bundle als illustratie: Aurelia → A (70%) → C (60%) én Aurelia → B (30%) → C (20%), met expliciete vermelding dat het een voorbeeld is, geen regel of feit
- Per pad een visualisatie van wat het pad bijdraagt aan controle (60 % via A, 0 % via B want keten breekt) en aan belang (42 % via A + 6 % via B = 48 %)
- Een korte aanstip van het algemene principe los van de illustratie: stemrechten tellen alleen als de tussenschakel gecontroleerd wordt; kapitaalaandeel loopt altijd door
- Een mini-vergelijkingstabel: "wanneer gebruik ik welk percentage?" — controlepercentage voor methode-keuze en consolidatieplicht; belangenpercentage voor winstaandeel en aandeel van derden

Stijl: NotebookLM kiest de indeling. Coherent met de overzichts-infographic + de andere cluster-infographic.
```

---

## Plan-samenvatting (1 oogopslag)

| Volgorde | Output | Lengte / formaat | Daglimiet? |
|---|---|---|---|
| 1 | 🎙️ Inleidende podcast | ±20 min | Telt in 3/dag NL-podcasts |
| 2 | 🎙️ Deep-dive 1 — kwalificeren + kiezen | ±20 min | Telt in 3/dag |
| 3 | 🎙️ Deep-dive 2 — uitvoeren | ±20 min | Telt in 3/dag |
| 4 | 🎙️ Recap (optioneel, dag 2) | ±8-10 min | Telt in 3/dag |
| — | 📊 Slidedeck (één voor heel programmaonderdeel) | Aantal slides vrij | Geen limiet |
| — | 🎨 Overzichts-infographic | Eén pagina | Geen limiet |
| — | 🎨 Cluster-infographic 1 — beslisboom + methodes-matrix | Eén pagina | Geen limiet |
| — | 🎨 Cluster-infographic 2 — controle vs. belang in keten | Eén pagina | Geen limiet |

Plan past in 1 dag voor de drie kern-podcasts; visuele afgeleiden parallel.
