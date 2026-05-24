---
title: "NotebookLM-afgeleiden — Boekhoudrecht"
description: "Prompts per output-type voor het programmaonderdeel Boekhoudrecht. Bronset = `1-2-boekhoudrecht-notebooklm-bundle.md`. Eén intro-podcast + twee deep-dives + optionele recap + één slidedeck + één overzichts-infographic + twee cluster-infographics. Stuurt op leeruitkomsten — NotebookLM krijgt creatieve vrijheid in vorm."
gegenereerd_op: "2026-05-19"
status: experiment
---

# Afgeleiden-plan — Boekhoudrecht

> **Bronset (zelfde voor alle afgeleiden):** `exports/1.2/1-2-boekhoudrecht-notebooklm-bundle.md`
> **Daglimiet podcasts (NL):** 3 afleveringen/dag in NotebookLM. Plan past in 1 dag (3 podcasts) + optionele recap dag 2.

---

## Inhoud van dit plan

| Output-type | Aantal | Wat |
|---|---|---|
| 🎙️ Inleidende podcast | 1 | Mentale kapstok: waarom boekhoudrecht, rechtsbronnen-piramide, autoriteiten-landschap, algemeen kader |
| 🎙️ Deep-dive podcasts | 2 | Grootte-cascade + boekhoudplicht-kwalificatie · Jaarrekening: beginselen, getrouw beeld en openbaarmaking |
| 🎙️ Recap podcast (optioneel) | 1 | Consolidatie zonder nieuwe stof |
| 📊 Diapresentatie | 1 | Eén deck voor het hele programmaonderdeel |
| 🎨 Overzichts-infographic | 1 | Visualiseert de architectuur van het programmaonderdeel (rechtsbronnen → actoren → grootte → jaarrekening → openbaarmaking) |
| 🎨 Cluster-infographics | 2 | Grootte-cascade-beslisboom · Jaarrekening-redeneerkader (beginselen + getrouw-beeld-overrule) |

---

## Cognitieve kaart van het programmaonderdeel

Wat zit er inhoudelijk in Boekhoudrecht? Vier zwaartepunten — de intro dekt ze allemaal oppervlakkig, deep-dives zoomen in op de twee zwaartepunten waar de echte examenklassiekers + valkuilen zitten.

| # | Zwaartepunt | Inhoud | Diepduik-waardig? |
|---|---|---|---|
| 1 | Rechtsbronnen + actoren-landschap | Rechtsbronnen-piramide (EU → wet → KB → CBN → rechtspraak), administratieve autoriteiten (FOD Economie, CBN, NBB, ITAA, BIBC), wie maakt / controleert / publiceert | Nee — komt in intro |
| 2 | Grootte-cascade + boekhoudplicht-kwalificatie | Onderneming-begrip, drempelwaarden micro/klein/groot, dubbele versus vereenvoudigde boekhouding, VZW/IVZW/stichting-regimes, jaarrekening-schema (volledig/verkort/micro) | **Ja — deep-dive 1** |
| 3 | Jaarrekening: beginselen + getrouw beeld + openbaarmaking | Zeven boekhoudbeginselen, getrouw-beeld-overrule, commissaris-benoeming, neerlegging bij NBB, sanctiekader | **Ja — deep-dive 2** |
| 4 | Boekjaarcyclus + administratieve verplichtingen | Proefbalans → afsluiting → neerlegging, bewaartermijnen, dagboeken, audit-trail | Nee — komt in intro |

---

## Doelpubliek, voorbeelden, examen-stress — verwerkt in elke prompt

De volgende drie verankeringen staan IN elke prompt hieronder ingewerkt. Ter referentie hier afzonderlijk.

**Doelpubliek (gemengd):** primair een ervaren beroepsbeoefenaar (typisch 5-15 jaar in het accountancyberoep) die zich voorbereidt op het ITAA-bekwaamheidsexamen Gecertificeerd Accountant — niet noodzakelijk dagelijks actief in dit deelgebied. Daarnaast luistert er af en toe een geïnteresseerde leek mee (partner, kennis). De stof moet voor de beroepsbeoefenaar **voldoende diep** zijn (concept-nuance, multi-conceptueel redeneren, de subtiele uitzonderingen in de grootte-cascade) maar voor de leek **volgbaar** (geen pure jargon-stapeling, geen legalese). Toon: een vakgesprek tussen twee gecertificeerde accountants — of tussen een gecertificeerd accountant en een kandidaat-GA. De stagiair die zich op het examen voorbereidt luistert mee, maar wordt niet als publiek toegesproken. Vaktermen worden gebruikt zoals ze in de praktijk vallen, maar concepten worden kort gepositioneerd wanneer nuance telt. Geen pedagogische "wat is een vennootschap"-momenten; wel "let op — een onderneming in de zin van het WER is iets anders dan een onderneming in de zin van het WVV".

**Voorbeelden:** concrete casussen in het bundle (zoals `Meubelzaak Mertens BV`, `Rotex Roeselare NV`, `Transport Tongeren BV`) zijn illustraties van een onderliggend principe — niet feiten over die ondernemingen, niet de wereldwijde regel. Spreek het principe uit via de illustratie en blijf bij het principe. Vermijd zinnen als "bij Meubelzaak Mertens is het altijd zo" — wel: "in deze illustratie zien we hoe de groottecriteria spelen wanneer een vennootschap net rond de klein/groot-drempel zit".

**Examen-tone:** spreek niet uit naam van de examinator. Voorbeeldexamens zijn data over wat in het verleden gevraagd is, geen voorschriften voor wat absoluut moet. Vermijd stress-taal als "je moet absoluut", "de examinator verwacht", "u moet". Mag wel: "op integratieniveau wordt vaak verwacht", "in voorbeeldexamens komen geregeld vragen rond de grootte-cascade", "wie deze stof beheerst kan...". Toon van een collega die mee voorbereidt, niet een examinator die toetst.

---

## Anti-fabricatie

Geldt in elke prompt: **gebruik UITSLUITEND inhoud uit het geüploade document `1-2-boekhoudrecht-notebooklm-bundle.md`.** Geen externe bronnen, geen aanvullingen uit andere wetgevingen, geen verzonnen voorbeelden. Bij twijfel: zeg "dit staat niet in het bundle". Belgische context (WVV, KB WVV, CBN, ITAA-normen) — niet Nederland.

---

# 🎙️ Inleidende podcast (±20 min)

```text
Gebruik UITSLUITEND inhoud uit het geüploade document `1-2-boekhoudrecht-notebooklm-bundle.md`. Geen externe bronnen, geen aanvullingen uit andere wetgevingen, geen verzonnen voorbeelden. Bij twijfel: zeg "dit staat niet in het bundle". Belgische context (WVV, KB WVV, CBN, ITAA-normen) — niet Nederland.

Doelpubliek (gemengd): primair een ervaren beroepsbeoefenaar (5-15 jaar accountancy-ervaring) die het ITAA-examen voorbereidt — niet noodzakelijk dagelijks in dit deelgebied. Daarnaast luistert af en toe een geïnteresseerde leek mee. Toon: vakgesprek tussen twee gecertificeerde accountants (of GA + kandidaat-GA). De stagiair-luisteraar vangt het gesprek op, wordt niet rechtstreeks aangesproken. Voldoende diep voor de beroepsbeoefenaar (concept-nuance, multi-conceptueel redeneren), volgbaar voor de leek (geen pure jargon-stapeling, geen legalese). Vaktermen worden gebruikt zoals in de praktijk; concepten worden kort gepositioneerd waar nuance telt. Geen pedagogische "wat is een vennootschap"-uitleg; wel kort verduidelijken wanneer een term in de boekhoudrechtelijke context een specifieke betekenis krijgt (bv. "onderneming" in WER versus WVV).

Behandel concrete casussen uit het bundle (zoals `Meubelzaak Mertens BV`, `Rotex Roeselare NV`, `Transport Tongeren BV`) als illustraties van een onderliggend principe, niet als feiten over die ondernemingen of als wereldwijde regel.

Spreek niet uit naam van de examinator. Voorbeeldexamens zijn data, geen voorschriften. Vermijd "je moet absoluut" / "de examinator verwacht". Toon van een collega die meeloopt met het examenvoorbereidingstraject, niet van een autoriteit.


Dit is de inleidende aflevering over Boekhoudrecht. Doel: de luisteraar krijgt een coherent overzicht van het hele programmaonderdeel én de mentale kapstok om de deep-dive-afleveringen straks te plaatsen.

Wat de luisteraar na deze aflevering moet kunnen:
- De bestaansreden van een afzonderlijk boekhoudrecht plaatsen: waarom een regelmatige en getrouwe boekhouding niet enkel een fiscale of vennootschapsrechtelijke aangelegenheid is
- De rechtsbronnen-piramide schetsen (EU-richtlijnen → WVV / WER → KB WVV → CBN-adviezen → rechtspraak) en aanvoelen wanneer welke bron primeert
- Het autoriteiten-landschap benoemen: FOD Economie, CBN, NBB, ITAA, BIBC — wie maakt regels, wie controleert, wie publiceert
- De vier zwaartepunten van het programmaonderdeel noemen (rechtsbronnen + actoren, grootte-cascade + boekhoudplicht, jaarrekening + beginselen + openbaarmaking, boekjaarcyclus) en weten welk type vragen ze typisch oproepen
- Aanvoelen waar de stof "rustig" is voor een ervaren beroepsbeoefenaar en waar de echte cognitieve last zit (de twee deep-dives die volgen)

Onderwerpen die aan bod moeten komen (volgorde en pacing vrij):
- Waarom een eigen boekhoudrecht? Regelmatige en getrouwe boekhouding als spil tussen ondernemers, schuldeisers, overheid en aandeelhouders
- De rechtsbronnen-piramide met de spanning tussen wet (algemeen, bindend) en CBN-adviezen (specifiek, gezaghebbend maar geen wet)
- Het actoren-landschap: wie maakt (wetgever + KB), wie adviseert (CBN), wie controleert (FOD Economie, NBB voor neerlegging, ITAA voor beroep), wie tuchtrecht (BIBC)
- Een korte tour langs de boekjaarcyclus: proefbalans → afsluiting → neerlegging → bewaartermijnen — alleen positioneren, geen detail; senior luisteraar weet de basis
- Waarom de grootte-cascade + boekhoudplicht een eigen deep-dive verdient (drempelcombinaties, uitzonderingsregimes, VZW-kantelpunten)
- Waarom de jaarrekening + beginselen + getrouw beeld + openbaarmaking een eigen deep-dive verdient (overrule-mechanisme, commissaris-vraag, sanctiekader)

Tone-hints: spreek de luisteraar aan als collega die het deelgebied wil opfrissen voor het examen, niet als beginner. Vermijd "let's dive in"-openings. Geen cijferreeksen — audio-medium.
```

---

# 🎙️ Deep-dive 1 — Grootte-cascade + boekhoudplicht-kwalificatie (±20 min)

```text
Gebruik UITSLUITEND inhoud uit het geüploade document `1-2-boekhoudrecht-notebooklm-bundle.md`. Geen externe bronnen, geen aanvullingen uit andere wetgevingen, geen verzonnen voorbeelden. Bij twijfel: zeg "dit staat niet in het bundle". Belgische context (WVV, KB WVV, CBN, ITAA-normen) — niet Nederland.

Doelpubliek (gemengd): ervaren beroepsbeoefenaar (5-15 jaar accountancy-ervaring) bereidt het ITAA-examen voor, soms luistert een geïnteresseerde leek mee. Toon: vakgesprek tussen twee gecertificeerde accountants (of GA + kandidaat-GA). De stagiair-luisteraar vangt het gesprek op, wordt niet rechtstreeks aangesproken. Voldoende diep voor de beroepsbeoefenaar, volgbaar voor de leek. Vaktermen worden gebruikt zoals in de praktijk; concepten worden kort gepositioneerd waar nuance telt. Geen pedagogische basisuitleg.

Behandel concrete casussen uit het bundle (zoals `Meubelzaak Mertens BV`, `Rotex Roeselare NV`) als illustraties van een onderliggend principe, niet als feiten of als wereldwijde regel.

Spreek niet uit naam van de examinator. Voorbeeldexamens zijn data, geen voorschriften. Toon van een collega die meedenkt, niet van een autoriteit.


Deep-dive-aflevering: de grootte-cascade is de meest geziene examen-valkuil in dit programmaonderdeel — drempels, uitzonderingen, kantelpunten, en de gevolgen voor het boekhoudregime + het jaarrekening-schema. Bouwt op de rechtsbronnen-piramide uit de inleidende aflevering. Geen herhaling van die basis — direct in de cognitieve last.

Wat de luisteraar na deze aflevering moet kunnen:
- Het onderneming-begrip plaatsen: wanneer geldt het WER-begrip, wanneer het WVV-begrip, en waarom de boekhoudplicht in artikel III.82 WER vasthangt aan het ene en de vennootschappelijke verplichtingen aan het andere
- De drie groottecategorieën (micro / klein / groot) toepassen op een concrete vennootschap, inclusief de consolidatieregel bij moeder-dochter en de twee-op-drie-criteria + opeenvolgende-boekjaren-regel
- Bepalen welk boekhoudregime van toepassing is (dubbele boekhouding versus vereenvoudigde boekhouding) en wanneer een onderneming zelfs zonder boekhoudplicht is
- Voor een VZW, IVZW of stichting kwalificeren welk regime geldt (klein versus groot, eenvoudige versus dubbele, jaarrekening-verplichting ja/nee)
- Het jaarrekening-schema kiezen (volledig / verkort / micro) op basis van de groottekwalificatie en de gevolgen voor de inhoudsverplichting van de jaarrekening
- De gevolgen van een kantelpunt (van klein naar groot, of andersom) duiden voor commissaris-benoeming en openbaarmakingsregime

Onderwerpen die aan bod moeten komen (volgorde en pacing vrij):
- Het onderneming-begrip in WER versus WVV — de subtiele maar examen-relevante asymmetrie
- De drempels per groottecategorie (omzet, balanstotaal, personeel) — niet als cijferreeks oplezen, wel het concept van twee-op-drie + opeenvolgende boekjaren positioneren
- Consolidatie van groottecriteria bij groepsstructuren (moeder + dochters), en waarom dat de kwalificatie kantelt
- Boekhoudregime-keuze: dubbele versus vereenvoudigde boekhouding, met de drempel waaronder een natuurlijke persoon-onderneming kan vereenvoudigd
- VZW / IVZW / stichting: drempels + verplichtingen + verschil met handelsvennootschappen, zonder in het verenigingsrecht te verdwalen
- Jaarrekening-schema (volledig / verkort / micro) als rechtstreeks gevolg van de groottekwalificatie
- Eén kantelpunt-illustratie uit het bundle: wat gebeurt er als een vennootschap van klein naar groot kantelt (commissaris, schema-wijziging, openbaarmaking)

Tone-hints: dichte stof met veel drempelwaarden — pacing en accentuering aan de hosts. Geen cijferreeksen voorlezen in audio; concepten en relaties primeren. Vermijd "let's dive in"-openings. Behandel de kantelpunt-illustratie uit het bundle als illustratie van het principe, niet als de norm.
```

---

# 🎙️ Deep-dive 2 — Jaarrekening: beginselen, getrouw beeld en openbaarmaking (±20 min)

```text
Gebruik UITSLUITEND inhoud uit het geüploade document `1-2-boekhoudrecht-notebooklm-bundle.md`. Geen externe bronnen, geen aanvullingen uit andere wetgevingen, geen verzonnen voorbeelden. Bij twijfel: zeg "dit staat niet in het bundle". Belgische context (WVV, KB WVV, CBN, ITAA-normen) — niet Nederland.

Doelpubliek (gemengd): ervaren beroepsbeoefenaar (5-15 jaar accountancy-ervaring) bereidt het ITAA-examen voor, soms luistert een geïnteresseerde leek mee. Toon: vakgesprek tussen twee gecertificeerde accountants (of GA + kandidaat-GA). De stagiair-luisteraar vangt het gesprek op, wordt niet rechtstreeks aangesproken. Voldoende diep voor de beroepsbeoefenaar, volgbaar voor de leek. Vaktermen worden gebruikt zoals in de praktijk; concepten worden kort gepositioneerd waar nuance telt. Geen pedagogische basisuitleg.

Behandel concrete casussen uit het bundle als illustraties van een onderliggend principe, niet als feiten over die ondernemingen of als wereldwijde regel.

Spreek niet uit naam van de examinator. Voorbeeldexamens zijn data, geen voorschriften. Toon van een collega die meedenkt, niet van een autoriteit.


Deep-dive-aflevering: de jaarrekening als juridisch document — welke beginselen sturen waardering, hoe werkt de getrouw-beeld-overrule, wie controleert (commissaris), wie publiceert (NBB), en wat zijn de sancties bij niet-naleving. Bouwt op het overzicht uit de inleidende aflevering. Geen herhaling van die basis — direct in de cognitieve last.

Wat de luisteraar na deze aflevering moet kunnen:
- De zeven boekhoudbeginselen in drie functionele lagen plaatsen (voorwaarden voor regelmatigheid / waarderingssturing / eindbeginsel getrouw beeld)
- Het overrule-mechanisme van getrouw beeld beschrijven (KB WVV art. 3:1 derde lid) — wanneer afwijken van een beginsel niet enkel mag maar verplicht is, en welke toelichtingsplicht erbij hoort
- Beoordelen of een vennootschap een commissaris moet benoemen, op basis van de groottekwalificatie + uitzonderingen, en welk regime van toepassing is (commissaris versus geen commissaris)
- De openbaarmakings-keten volgen: opmaak → goedkeuring algemene vergadering → neerlegging NBB binnen 30 dagen → publicatie — én weten welke termijnen tellen
- Het sanctiekader plaatsen bij niet-tijdige neerlegging (administratieve, fiscale, civielrechtelijke gevolgen) en bij niet-getrouwe jaarrekening (bestuurdersaansprakelijkheid, strafrechtelijke risico's)
- De rol van CBN-adviezen positioneren: gezaghebbend maar niet wettelijk bindend — wat dat betekent in de praktijk

Onderwerpen die aan bod moeten komen (volgorde en pacing vrij):
- De drie-lagen-structuur van de zeven boekhoudbeginselen, met de spanning tussen voorzichtigheid en getrouw beeld als concreet voorbeeld
- Het overrule-mechanisme: wanneer een beginsel afwijken vereist om tot getrouw beeld te komen, met toelichtingsplicht
- Commissaris-regime: wanneer benoeming verplicht, wat de uitzonderingen zijn, wat het verschil maakt voor de openbaarmaking
- Openbaarmaking bij de NBB: termijnen, schema-keuze, taal, vorm — overzichtsniveau
- Sanctiekader: getrapt — administratief eerst, dan fiscaal/civielrechtelijk, dan strafrechtelijk bij opzet
- CBN-adviezen als levend rechtsdomein — gezaghebbend, geen wet, maar moeilijk te negeren in de praktijk

Tone-hints: minder cijferdicht dan deep-dive 1, meer juridisch-redeneerwerk. Vermijd "let's dive in"-openings. Het overrule-mechanisme is het cognitieve hoogtepunt — geef het ademruimte.
```

---

# 🎙️ Recap podcast (optioneel, ±8-10 min)

```text
Gebruik UITSLUITEND inhoud uit het geüploade document `1-2-boekhoudrecht-notebooklm-bundle.md`. Geen externe bronnen, geen aanvullingen uit andere wetgevingen, geen verzonnen voorbeelden. Bij twijfel: zeg "dit staat niet in het bundle". Belgische context (WVV, KB WVV, CBN, ITAA-normen) — niet Nederland.

Doelpubliek (gemengd): ervaren beroepsbeoefenaar (5-15 jaar accountancy-ervaring) die de drie eerdere afleveringen al gehoord heeft, soms een geïnteresseerde leek mee. Toon: vakgesprek tussen gecertificeerde accountants (of GA + kandidaat-GA), volgbaar voor de leek. De stagiair-luisteraar vangt het gesprek op, wordt niet rechtstreeks aangesproken.

Behandel casussen uit het bundle als illustraties van een principe, niet als feiten of wereldwijde regel. Spreek niet uit naam van de examinator.


Korte consolidatie-aflevering. Geen nieuwe stof.

Wat de luisteraar na deze recap moet kunnen:
- De vier zwaartepunten van Boekhoudrecht in eigen woorden positioneren (rechtsbronnen + actoren → grootte-cascade + boekhoudplicht → jaarrekening + beginselen + openbaarmaking → boekjaarcyclus)
- Per zwaartepunt het kernspanningsveld benoemen (waar zit de cognitieve last, niet waar de feitenkennis)

Onderwerpen die aan bod moeten komen (één keer kort per blok):
- Rechtsbronnen-piramide + actoren-landschap
- Grootte-cascade + boekhoudplicht-kwalificatie + jaarrekening-schema-keuze
- Boekhoudbeginselen in drie lagen + getrouw-beeld-overrule + commissaris + neerlegging
- Boekjaarcyclus en bewaarverplichtingen — overzichtsniveau

Tone-hints: consolidatie, geen nieuwe voorbeelden. Vermijd "let's dive in"-openings.
```

---

# 📊 Diapresentatie — één deck voor het hele programmaonderdeel

```text
Gebruik UITSLUITEND inhoud uit het geüploade document `1-2-boekhoudrecht-notebooklm-bundle.md`. Geen externe bronnen, geen aanvullingen uit andere wetgevingen, geen verzonnen voorbeelden. Bij twijfel: zeg "dit staat niet in het bundle". Belgische context (WVV, KB WVV, CBN, ITAA-normen) — niet Nederland.

Doelpubliek (gemengd): primair een ervaren beroepsbeoefenaar (5-15 jaar accountancy-ervaring) die de stof opfrist voor het ITAA-examen — niet noodzakelijk dagelijks in dit deelgebied. Daarnaast kan een geïnteresseerde leek het deck bekijken. Toon: vakgesprek tussen twee gecertificeerde accountants (of GA + kandidaat-GA). De stagiair-luisteraar vangt het gesprek op, wordt niet rechtstreeks aangesproken. Vaktermen worden gebruikt zoals in de praktijk; concepten worden gepositioneerd waar nuance telt. Geen pure jargon-stapeling, geen legalese.

Casussen uit het bundle zijn illustraties van een onderliggend principe, niet feiten over die ondernemingen.


Eén slidedeck dat het volledige programmaonderdeel Boekhoudrecht dekt op overzichtsniveau. NotebookLM bepaalt zelf het aantal slides, de volgorde van details binnen elk zwaartepunt, en de visuele indeling.

Wat de student na het doorbladeren van deze deck moet kunnen:
- De rechtsbronnen-piramide reproduceren en aangeven welke bron primeert bij conflict
- Het autoriteiten-landschap schetsen (FOD Economie, CBN, NBB, ITAA, BIBC) en per autoriteit één kernopdracht benoemen
- Een vennootschap kwalificeren als micro / klein / groot en het bijhorende jaarrekening-schema bepalen
- Het VZW / IVZW / stichting-regime onderscheiden van het handelsvennootschap-regime
- De zeven boekhoudbeginselen in drie functionele lagen plaatsen en de getrouw-beeld-overrule beschrijven
- Beoordelen wanneer een commissaris benoemd moet worden
- De openbaarmakings-keten + termijnen + sanctiekader bij de NBB schetsen

Inhoudelijke clusters die in het deck moeten landen:
- Rechtsbronnen-piramide (EU → wet → KB → CBN → rechtspraak) + autoriteiten-landschap
- Onderneming-begrip (WER versus WVV) + boekhoudplicht-grondslag
- Grootte-cascade: drempelwaarden, twee-op-drie-regel, opeenvolgende boekjaren, consolidatie bij groepen — overzichtsniveau via vergelijkingstabel
- Boekhoudregime + jaarrekening-schema (volledig / verkort / micro) — gevolg van de groottekwalificatie
- VZW / IVZW / stichting — afwijkend regime, kantelpunten
- Boekhoudbeginselen in drie lagen + getrouw-beeld-overrule
- Commissaris + openbaarmaking bij NBB + sanctiekader

Stijl: NotebookLM bepaalt zelf alle vormaspecten. Cruciale tabellen en diagrammen uit het bundle (rechtsbronnen-piramide, groottedrempel-matrix, beginselen-overzicht) mogen letterlijk over. Eén deck, gemaakt om snel doorheen te bladeren als revisie — niet om de detail-stof te vervangen.
```

---

# 🎨 Overzichts-infographic — structuur van het hele programmaonderdeel

```text
Gebruik UITSLUITEND inhoud uit het geüploade document `1-2-boekhoudrecht-notebooklm-bundle.md`. Geen externe bronnen, geen aanvullingen uit andere wetgevingen, geen verzonnen voorbeelden. Bij twijfel: zeg "dit staat niet in het bundle". Belgische context (WVV, KB WVV, CBN, ITAA-normen) — niet Nederland.

Doelpubliek (gemengd): ervaren beroepsbeoefenaar bereidt het ITAA-examen voor, met af en toe een geïnteresseerde leek die meekijkt. Vaktermen gebruiken zoals in de praktijk; geen pure jargon-stapeling, geen legalese.

Casussen uit het bundle zijn illustraties van een onderliggend principe.


Eén infographic-pagina die het hele programmaonderdeel Boekhoudrecht visueel ordent. NotebookLM bepaalt zelf de indeling, kleurkeuze en grafische metaforen.

Centrale boodschap: Boekhoudrecht leest van bron naar uitvoering — eerst de rechtsbronnen-piramide en de autoriteiten die het stelsel bemannen, dan de grootte-cascade die bepaalt welk regime van toepassing is, dan de jaarrekening met haar beginselen en de getrouw-beeld-overrule als eindbeginsel, en tot slot de openbaarmakings-keten naar de NBB met haar sanctiekader.

Wat de student na het bekijken van deze infographic moet kunnen:
- De architectuur van het programmaonderdeel beschrijven in vier zwaartepunten
- Per zwaartepunt benoemen welk type cognitieve last erin zit (rechtsbronnen-hiërarchie, drempel-cascade, beginselen-conflict-redenering, procedurele keten)
- Wijzen op de twee blokken waar de echte examenklassiekers zitten

Inhoudelijke elementen die moeten doorkomen:
- De rechtsbronnen-piramide met de vijf lagen (EU → wet → KB → CBN → rechtspraak)
- Het actoren-landschap als afzonderlijke laag (FOD Economie, CBN, NBB, ITAA, BIBC) met telkens één kernopdracht
- De vier zwaartepunten als architectonisch overzicht
- Per zwaartepunt: één zin "wat zit erin" + één zin "waar de last zit"
- Aanduiding welke twee blokken in deep-dive-afleveringen worden uitgewerkt

Stijl: NotebookLM kiest de indeling. Houd de accentkleuren coherent over alle infographics voor Boekhoudrecht (dit deck + de twee cluster-infographics hieronder).
```

---

# 🎨 Cluster-infographic 1 — Grootte-cascade + boekhoudplicht-beslisboom

```text
Gebruik UITSLUITEND inhoud uit het geüploade document `1-2-boekhoudrecht-notebooklm-bundle.md`. Geen externe bronnen, geen aanvullingen uit andere wetgevingen, geen verzonnen voorbeelden. Bij twijfel: zeg "dit staat niet in het bundle". Belgische context (WVV, KB WVV, CBN, ITAA-normen) — niet Nederland.

Doelpubliek: ervaren beroepsbeoefenaar die de stof opfrist. Casussen uit het bundle zijn illustraties.


Eén infographic-pagina die de grootte-cascade + boekhoudplicht-kwalificatie als beslisboom uitwerkt — dieper dan de overzichts-infographic.

Centrale boodschap: van rechtspersoon naar boekhoudregime + jaarrekening-schema loopt één beslis-cascade: eerst onderneming-kwalificatie (WER), dan drempel-cascade (micro / klein / groot, met twee-op-drie + opeenvolgende boekjaren + consolidatie), dan regime-keuze (vereenvoudigd versus dubbel), dan schema-keuze (volledig / verkort / micro), en VZW / IVZW / stichting volgen een parallel spoor.

Wat de student na het bekijken van deze infographic moet kunnen:
- Een vennootschap door de beslisboom voeren en uitkomen op het juiste boekhoudregime + jaarrekening-schema
- De drie hoofdsporen onderscheiden (handelsvennootschap / natuurlijke persoon-onderneming / VZW-IVZW-stichting)
- Het kantelpunt-moment herkennen wanneer een onderneming van categorie verandert en wat dan administratief gebeurt

Inhoudelijke elementen die moeten doorkomen:
- De beslisboom van onderneming-kwalificatie naar schema-keuze
- De drempelwaarden per categorie (visueel, niet als tekst-tabel) met expliciete twee-op-drie + opeenvolgende-boekjaren-aanduiding
- De consolidatieregel bij moedervennootschappen — kort visueel
- Het parallelle VZW-spoor met zijn eigen drempelregime
- Eén grenscasus uit het bundle als illustratief vertrekpunt (vennootschap die rond klein/groot-drempel zit)
- Kantelpunt-gevolg: commissaris, schema-wissel, openbaarmaking

Stijl: NotebookLM kiest de indeling. Coherent met de overzichts-infographic + de andere cluster-infographic.
```

---

# 🎨 Cluster-infographic 2 — Jaarrekening-redeneerkader: beginselen + getrouw-beeld-overrule

```text
Gebruik UITSLUITEND inhoud uit het geüploade document `1-2-boekhoudrecht-notebooklm-bundle.md`. Geen externe bronnen, geen aanvullingen uit andere wetgevingen, geen verzonnen voorbeelden. Bij twijfel: zeg "dit staat niet in het bundle". Belgische context (WVV, KB WVV, CBN, ITAA-normen) — niet Nederland.

Doelpubliek: ervaren beroepsbeoefenaar die de stof opfrist. Casussen uit het bundle zijn illustraties.


Eén infographic-pagina die het jaarrekening-redeneerkader visueel uitwerkt — de zeven beginselen in drie functionele lagen, de getrouw-beeld-overrule als eindbeginsel, en de bridge naar commissaris-controle + openbaarmaking.

Centrale boodschap: een Belgische jaarrekening wordt gestuurd door zeven beginselen in drie lagen — voorwaarden voor regelmatigheid (volledigheid, juistheid, tijdigheid), waarderingssturing (voorzichtigheid, oprechtheid, continuïteit, consistentie) en eindbeginsel (getrouw beeld). Het eindbeginsel overrulet de andere wanneer de letterlijke toepassing geen getrouw beeld geeft — met toelichtingsplicht.

Wat de student na het bekijken van deze infographic moet kunnen:
- De zeven beginselen in de drie lagen plaatsen en uitleggen welke laag wat doet
- De getrouw-beeld-overrule reproduceren: wanneer en hoe afwijken, met welke toelichting
- De brug zien tussen waarderingsbeginselen, commissaris-controle (extern oog) en openbaarmaking (extern resultaat)

Inhoudelijke elementen die moeten doorkomen:
- De drie-lagen-structuur visueel — niet als opsomming maar als architectuur
- Het overrule-mechanisme als afzonderlijk kantelvlak boven de drie lagen
- De commissaris-vraag als beslis-step (verplicht / niet verplicht / uitzondering) — kort
- De openbaarmakings-keten naar de NBB + de getrapte sanctiestructuur
- CBN-adviezen als invloed-laag naast de wet, niet erbinnen

Stijl: NotebookLM kiest de indeling. Coherent met de overzichts-infographic + de andere cluster-infographic.
```

---

## Plan-samenvatting (1 oogopslag)

| Volgorde | Output | Lengte / formaat | Daglimiet? |
|---|---|---|---|
| 1 | 🎙️ Inleidende podcast | ±20 min | Telt in 3/dag NL-podcasts |
| 2 | 🎙️ Deep-dive 1 — grootte-cascade + boekhoudplicht | ±20 min | Telt in 3/dag |
| 3 | 🎙️ Deep-dive 2 — jaarrekening: beginselen + getrouw beeld + openbaarmaking | ±20 min | Telt in 3/dag |
| 4 | 🎙️ Recap (optioneel, dag 2) | ±8-10 min | Telt in 3/dag |
| — | 📊 Slidedeck (één voor heel programmaonderdeel) | Aantal slides vrij | Geen limiet |
| — | 🎨 Overzichts-infographic | Eén pagina | Geen limiet |
| — | 🎨 Cluster-infographic 1 — grootte-cascade-beslisboom | Eén pagina | Geen limiet |
| — | 🎨 Cluster-infographic 2 — jaarrekening-redeneerkader | Eén pagina | Geen limiet |

Plan past in 1 dag voor de drie kern-podcasts; visuele afgeleiden parallel.
