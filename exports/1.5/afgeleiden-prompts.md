---
title: "NotebookLM-afgeleiden — Europese wetgeving en IFRS"
description: "Prompts per output-type voor het programmaonderdeel Europese wetgeving en IFRS. Bronset = `1-5-beginselen-van-de-europese-wetgeving-notebooklm-bundle.md`. Eén intro-podcast + drie deep-dives + één slidedeck + één algemene infographic + drie cluster-infographics. Stuurt op leeruitkomsten — NotebookLM krijgt creatieve vrijheid in vorm."
gegenereerd_op: "2026-05-19"
status: experiment
---

# Afgeleiden-plan — Europese wetgeving en IFRS

> **Bronset (zelfde voor alle afgeleiden):** `exports/1.5/1-5-beginselen-van-de-europese-wetgeving-notebooklm-bundle.md`
> **Daglimiet podcasts (NL):** 3 afleveringen/dag in NotebookLM. Plan: intro + drie deep-dives. Strategie — intro + deep-dive 1 + deep-dive 2 op dag 1 (3/3); deep-dive 3 + optionele recap op dag 2.

---

## Inhoud van dit plan

| Output-type | Aantal | Wat |
|---|---|---|
| 🎙️ Inleidende podcast | 1 | Twee referentiestelsels + Europese architectuur + endorsement + IFRS-toepassingsgebied België |
| 🎙️ Deep-dive podcasts | 3 | IFRS-presentatie + vaste activa + impairment (IAS 1, 16, 38, 36) · IFRS-opbrengsten + voorraden + leasing (IFRS 15, IAS 2, IFRS 16) · Stelselwissel + foutcorrecties (IFRS 1, CBN 2022/08) |
| 🎙️ Recap podcast (optioneel) | 1 | Consolidatie zonder nieuwe stof |
| 📊 Diapresentatie | 1 | Eén deck voor het hele programmaonderdeel |
| 🎨 Overzichts-infographic | 1 | Visualiseert de architectuur BE GAAP ↔ IFRS-EU ↔ IFRS-IASB + endorsement |
| 🎨 Cluster-infographics | 3 | Hoofdverschillen-matrix BE GAAP vs. IFRS · Vijf-componenten IFRS-jaarrekening · Stelselwissel-stappenplan (BE GAAP → IFRS én omgekeerd) |

---

## Cognitieve kaart van het programmaonderdeel

Wat zit er inhoudelijk in Europese wetgeving en IFRS? Vijf zwaartepunten — de intro dekt het overkoepelend kader, de drie deep-dives splitsen de IFRS-stof in twee thematische blokken plus een procedureel slot.

| # | Zwaartepunt | Inhoud | Diepduik-waardig? |
|---|---|---|---|
| 1 | Twee referentiestelsels + Europese architectuur | BE GAAP versus IFRS als filosofieën (rule-based versus principle-based), Boekhoudrichtlijn 2013/34/EU versus Verordening 1606/2002, endorsement-procedure, IFRS-toepassingsgebied België (enkelvoudig altijd BE GAAP; geconsolideerd alleen verplicht IFRS bij EU-beursgenoteerd of financiële sector) | Nee — komt in intro |
| 2 | IFRS — presentatie + vaste activa + impairment | IAS 1 (vijf componenten, presentatiebeginselen), IAS 16 (materiële vaste activa, kostprijsmodel / herwaarderingsmodel, componentenbenadering), IAS 38 (immateriële activa — onderzoek versus ontwikkeling), IAS 36 (bijzondere waardevermindering, één impairment-model) | **Ja — deep-dive 1** |
| 3 | IFRS — opbrengsten + voorraden + leasing | IFRS 15 (5-stappen-model, prestatieverplichtingen), IAS 2 (voorraadwaardering, LIFO verboden), IFRS 16 (alle leases on-balance voor lessee, right-of-use-actief + leaseverplichting, sale-and-leaseback) | **Ja — deep-dive 2** |
| 4 | Stelselwissel + foutcorrecties | IFRS 1 (eerste IFRS-toepassing als project: openingsbalans, vrijstellingen, aansluitingstabellen), CBN 2022/08 (IFRS → BE GAAP), foutcorrecties en wijziging van waarderingsregels | **Ja — deep-dive 3** |
| 5 | Cheatsheet + valkuilen | Hoofdverschillen-matrix, drie thematische clusters (balansomvang, resultaatdynamiek, opnamecriteria), BE GAAP / IFRS-EU / IFRS-IASB-onderscheid | Verspreid over deep-dives en infographics |

---

## Doelpubliek, voorbeelden, examen-stress — verwerkt in elke prompt

De volgende drie verankeringen staan IN elke prompt hieronder ingewerkt. Ter referentie hier afzonderlijk.

**Doelpubliek (gemengd):** primair een ervaren beroepsbeoefenaar (typisch 5-15 jaar in het accountancyberoep) die zich voorbereidt op het ITAA-bekwaamheidsexamen Gecertificeerd Accountant — niet noodzakelijk dagelijks met IFRS-dossiers bezig. Daarnaast luistert er af en toe een geïnteresseerde leek mee. De stof moet voor de beroepsbeoefenaar **voldoende diep** zijn (concept-nuance, examensubtiliteiten, multi-conceptueel redeneren tussen twee stelsels) maar voor de leek **volgbaar** (geen pure jargon-stapeling, geen legalese). Toon: een vakgesprek tussen twee gecertificeerde accountants — of tussen een gecertificeerd accountant en een kandidaat-GA. De stagiair die zich op het examen voorbereidt luistert mee, maar wordt niet als publiek toegesproken. Vaktermen worden gebruikt zoals ze in de praktijk vallen, maar concepten worden kort gepositioneerd wanneer nuance telt. Geen pedagogische "wat is een balans"-uitleg; wel "let op — onder IFRS heeft 'impairment' een specifieke betekenis die verschilt van wat we onder BE GAAP 'waardevermindering' noemen".

**Voorbeelden:** waar het bundle geen specifieke vennootschapsnaam noemt, hanteer "een Belgische beursgenoteerde groep" als generiek anker — geen feit over een bestaande onderneming, alleen een illustratie van het principe (typisch geval waarin de geconsolideerde rekening verplicht onder IFRS valt terwijl de enkelvoudige onder BE GAAP blijft). Spreek het principe uit via de illustratie en blijf bij het principe. Vermijd zinnen die suggereren dat één illustratie de norm vormt.

**Examen-tone:** spreek niet uit naam van de examinator. Voorbeeldexamens zijn data over wat in het verleden gevraagd is, geen voorschriften voor wat absoluut moet. Vermijd stress-taal als "je moet absoluut", "de examinator verwacht", "u moet". Mag wel: "op integratieniveau wordt vaak verwacht", "in voorbeeldexamens komen geregeld vergelijkingsvragen BE GAAP versus IFRS voor", "wie deze stof beheerst kan...". Toon van een collega die mee voorbereidt, niet een examinator die toetst.

---

## Drie-stelsels-valkuil — verwerkt in elke prompt

In elke prompt wordt expliciet onderscheiden tussen drie noties die makkelijk dooreenlopen:
- **BE GAAP** — het Belgische boekhoudrecht onder KB WVV; geldt altijd voor de enkelvoudige statutaire jaarrekening
- **IFRS-EU** — IFRS-standaarden zoals goedgekeurd door de Europese Commissie via de endorsement-procedure (Verordening 1606/2002); afdwingbaar binnen de EU
- **IFRS-IASB** — IFRS-standaarden zoals uitgegeven door de IASB, los van endorsement; niet automatisch van toepassing in de EU

Een 'IFRS-onder-verordening'-vraag gaat altijd over IFRS-EU, niet IFRS-IASB. Een nog niet door de Commissie goedgekeurde IASB-standaard is in België niet afdwingbaar.

---

## Anti-fabricatie

Geldt in elke prompt: **gebruik UITSLUITEND inhoud uit het geüploade document `1-5-beginselen-van-de-europese-wetgeving-notebooklm-bundle.md`.** Geen externe bronnen, geen aanvullingen uit andere wetgevingen, geen verzonnen voorbeelden. Bij twijfel: zeg "dit staat niet in het bundle". Belgische context (WVV, KB WVV, CBN, IFRS-EU zoals geëndorseerd via Verordening 1606/2002, IASB) — niet Nederland.

---

# 🎙️ Inleidende podcast (±20 min)

```text
Gebruik UITSLUITEND inhoud uit het geüploade document `1-5-beginselen-van-de-europese-wetgeving-notebooklm-bundle.md`. Geen externe bronnen, geen aanvullingen uit andere wetgevingen, geen verzonnen voorbeelden. Bij twijfel: zeg "dit staat niet in het bundle". Belgische context (WVV, KB WVV, CBN, IFRS-EU via Verordening 1606/2002, IASB) — niet Nederland.

Doelpubliek (gemengd): primair een ervaren beroepsbeoefenaar (5-15 jaar accountancy-ervaring) die het ITAA-examen voorbereidt — niet noodzakelijk dagelijks met IFRS-dossiers bezig. Daarnaast luistert af en toe een geïnteresseerde leek mee. Toon: vakgesprek tussen twee gecertificeerde accountants (of GA + kandidaat-GA). De stagiair-luisteraar vangt het gesprek op, wordt niet rechtstreeks aangesproken. Voldoende diep voor de beroepsbeoefenaar (concept-nuance, multi-conceptueel redeneren tussen twee stelsels), volgbaar voor de leek (geen pure jargon-stapeling, geen legalese). Vaktermen worden gebruikt zoals in de praktijk; concepten worden kort gepositioneerd waar nuance telt. Geen pedagogische "wat is een balans"-uitleg; wel kort verduidelijken wanneer een term in IFRS-context anders ingevuld wordt dan in BE GAAP.

Drie-stelsels-valkuil expliciet meenemen: maak het onderscheid tussen BE GAAP (KB WVV, enkelvoudig statutair), IFRS-EU (goedgekeurd door de Europese Commissie via endorsement, afdwingbaar binnen de EU) en IFRS-IASB (uitgegeven door IASB, niet automatisch in EU). Een 'IFRS-onder-verordening'-vraag gaat altijd over IFRS-EU.

Waar het bundle geen specifieke vennootschapsnaam noemt, hanteer "een Belgische beursgenoteerde groep" als generiek anker — geen feit, alleen illustratie van het principe.

Spreek niet uit naam van de examinator. Voorbeeldexamens zijn data, geen voorschriften. Vermijd "je moet absoluut" / "de examinator verwacht". Toon van een collega die meeloopt met het examenvoorbereidingstraject, niet van een autoriteit.

Dit is de inleidende aflevering over Europese wetgeving en IFRS. Doel: de luisteraar krijgt een coherent overzicht van het programmaonderdeel én de mentale kapstok om de drie deep-dive-afleveringen straks te plaatsen. Focus van deze intro: het Europese kader + het toepassingsgebied — vóór je in de IFRS-techniek duikt, moet je weten op welke jaarrekening welk stelsel van toepassing is.

Wat de luisteraar na deze aflevering moet kunnen:
- De twee referentiestelsels positioneren als filosofieën: BE GAAP rule-based, juridisch-fiscaal georiënteerd, vaste schema's, voorzichtigheidsbeginsel; IFRS principle-based, investeerders-georiënteerd, reële waarde, professional judgment
- Het Europese tweesporenbeleid beschrijven: Boekhoudrichtlijn 2013/34/EU als minimumkern voor élke jaarrekening (omgezet via KB WVV) versus Verordening 1606/2002 die IFRS oplegt aan een specifieke ring
- De endorsement-procedure schetsen: IASB geeft uit → Europese Commissie keurt goed via EFRAG-advies en comitologie → pas dan afdwingbaar in de EU
- Het IFRS-toepassingsgebied in België bepalen: enkelvoudige statutaire jaarrekening = altijd BE GAAP; geconsolideerde rekening = verplicht IFRS bij EU-beursgenoteerd of bij krediet-/verzekeringsinstelling, anders BE GAAP-consolidatie (met beperkte vrijwillige optie)
- Aanvoelen waar de echte cognitieve last zit (de drie deep-dives die volgen): twee thematische IFRS-blokken plus het procedurele werk rond stelselwissel

Onderwerpen die aan bod moeten komen (volgorde en pacing vrij):
- Waarom twee stelsels naast elkaar bestaan — dezelfde economische werkelijkheid, twee filosofieën (juridisch-fiscaal versus investeerders-georiënteerd)
- BE GAAP versus IFRS in één zin per stelsel — wat de toon kleurt
- Het Europese tweesporenbeleid: harmonisatie via richtlijn (KB WVV) + verordening (IFRS voor beursgenoteerden geconsolideerd)
- Endorsement-procedure als filter: niet elke IASB-standaard belandt automatisch in EU-recht (drie-stelsels-valkuil expliciet aanstippen)
- Toepassingsgebied België: enkelvoudig altijd BE GAAP; geconsolideerd alleen IFRS bij beursnotering / financiële sector / beperkte vrijwillige opties — beslis-redenering kort doorlopen
- Aankondiging van de drie deep-dives: presentatie + vaste activa + impairment / opbrengsten + voorraden + leasing / stelselwissel + foutcorrecties

Tone-hints: spreek de luisteraar aan als collega die het deelgebied wil opfrissen voor het examen, niet als beginner. Vermijd "let's dive in"-openings. Geen cijferreeksen — audio-medium.
```

---

# 🎙️ Deep-dive 1 — IFRS-presentatie + vaste activa + impairment (IAS 1, 16, 38, 36) (±20 min)

```text
Gebruik UITSLUITEND inhoud uit het geüploade document `1-5-beginselen-van-de-europese-wetgeving-notebooklm-bundle.md`. Geen externe bronnen, geen aanvullingen uit andere wetgevingen, geen verzonnen voorbeelden. Bij twijfel: zeg "dit staat niet in het bundle". Belgische context (WVV, KB WVV, CBN, IFRS-EU via Verordening 1606/2002, IASB) — niet Nederland.

Doelpubliek (gemengd): ervaren beroepsbeoefenaar (5-15 jaar accountancy-ervaring) bereidt het ITAA-examen voor, soms luistert een geïnteresseerde leek mee. Toon: vakgesprek tussen twee gecertificeerde accountants (of GA + kandidaat-GA). De stagiair-luisteraar vangt het gesprek op, wordt niet rechtstreeks aangesproken. Voldoende diep voor de beroepsbeoefenaar, volgbaar voor de leek. Vaktermen worden gebruikt zoals in de praktijk; concepten worden kort gepositioneerd waar nuance telt. Geen pedagogische basisuitleg.

Drie-stelsels-valkuil: maak telkens expliciet of een regel uit BE GAAP, IFRS-EU of IFRS-IASB komt. Een IFRS-standaard die nog niet via endorsement is doorgekomen, is binnen de EU niet afdwingbaar — speelt zelden in de stof maar is een examen-haakje.

Behandel "een Belgische beursgenoteerde groep" als generiek illustratie-anker waar het bundle geen specifieke vennootschapsnaam noemt — geen feit, alleen voorbeeld van het principe.

Spreek niet uit naam van de examinator. Voorbeeldexamens zijn data, geen voorschriften. Toon van een collega die meedenkt, niet van een autoriteit.

Deep-dive-aflevering: drie nauw samenhangende IFRS-blokken — presentatie (IAS 1), waardering van vaste activa (IAS 16 materieel + IAS 38 immaterieel) en impairment (IAS 36). Bouwt op de inleidende aflevering (twee stelsels + Europese architectuur). Geen herhaling van die basis — direct in de cognitieve last.

Wat de luisteraar na deze aflevering moet kunnen:
- De vijf verplichte componenten van een IFRS-jaarrekening opnoemen (balans · totaalresultaat · mutaties eigen vermogen · kasstroom · toelichting) en zien dat dit méér is dan wat KB WVV verplicht voor BE GAAP — IFRS dwingt mutatieoverzicht eigen vermogen en kasstroomoverzicht voor iedereen
- De vijf algemene presentatiebeginselen IFRS plaatsen (going concern, accruals, materialiteit, consistentie, verbod op compensatie) en het brede begrip totaalresultaat duiden (winst of verlies + OCI)
- De keuze tussen kostprijsmodel en herwaarderingsmodel (IAS 16) per categorie maken — en waarom BE GAAP veel terughoudender is met structurele herwaardering
- De componentenbenadering toepassen: bestanddelen met een aanzienlijke kostprijs en afwijkende levensduur afzonderlijk afschrijven
- Het IFRS-onderscheid onderzoek versus ontwikkeling (IAS 38) hanteren: onderzoek = altijd kost (verbod op activering); ontwikkeling = activering verplicht bij 6 cumulatieve criteria. Plaatsen tegen BE GAAP (KB WVV art. 3:31 staat activering onderzoek wel toe)
- Het impairment-model (IAS 36) toepassen: bij triggering events → terugwinbare waarde berekenen (= hoogste van reële waarde -/- verkoopkosten en bedrijfswaarde) → bijzondere waardevermindering wanneer boekwaarde > terugwinbare waarde. Voor goodwill: altijd jaarlijkse impairment-test (geen afschrijving). Plaatsen tegen BE GAAP-goodwill (afschrijving over vermoedelijke gebruiksduur, default 5 jaar)
- Aanvoelen waarom IFRS-resultaat volatieler is dan BE GAAP — impairment-shocks versus gladde afschrijving

Onderwerpen die aan bod moeten komen (volgorde en pacing vrij):
- IAS 1 vijf componenten + vijf algemene presentatiebeginselen — kort, want het is meer mapping-werk dan diepe redenering
- Balans onder IFRS: vlottend versus niet-vlottend; resultaat: totaalresultaat = P&L + OCI (waarom OCI bestaat)
- IAS 16: kostprijsmodel versus herwaarderingsmodel, keuze per categorie, intercalaire interesten als optie, componentenbenadering — telkens met BE GAAP als contrast
- IAS 38: onderzoek (kost) versus ontwikkeling (activering verplicht bij 6 criteria); contrast met BE GAAP-activering onderzoek
- IAS 36: één impairment-model voor alles → triggering events → boekwaarde tegen terugwinbare waarde → bijzondere waardevermindering of terugname (let op irreversibiliteit goodwill)
- Goodwill-behandeling: BE GAAP afschrijven (default 5 jaar, langer mits motivering) versus IFRS jaarlijkse impairment-test zonder afschrijving — waarom IFRS-resultaat daardoor schokkeriger verloopt
- Korte aanstip: BE GAAP versus IFRS-EU versus IFRS-IASB — wat afdwingbaar is in België

Tone-hints: dichte stof — pacing en accentuering aan de hosts. Vermijd "let's dive in"-openings. Geen cijferreeksen behalve waar één doorgewerkte stap de redenering draagt (bv. terugwinbare waarde-formule). Houd telkens BE GAAP en IFRS visueel naast elkaar in de redenering — dat is het examen-haakje van het programmaonderdeel.
```

---

# 🎙️ Deep-dive 2 — IFRS-opbrengsten + voorraden + leasing (IFRS 15, IAS 2, IFRS 16) (±20 min)

```text
Gebruik UITSLUITEND inhoud uit het geüploade document `1-5-beginselen-van-de-europese-wetgeving-notebooklm-bundle.md`. Geen externe bronnen, geen aanvullingen uit andere wetgevingen, geen verzonnen voorbeelden. Bij twijfel: zeg "dit staat niet in het bundle". Belgische context (WVV, KB WVV, CBN, IFRS-EU via Verordening 1606/2002, IASB) — niet Nederland.

Doelpubliek (gemengd): ervaren beroepsbeoefenaar (5-15 jaar accountancy-ervaring) bereidt het ITAA-examen voor, soms luistert een geïnteresseerde leek mee. Toon: vakgesprek tussen twee gecertificeerde accountants (of GA + kandidaat-GA). De stagiair-luisteraar vangt het gesprek op, wordt niet rechtstreeks aangesproken. Voldoende diep voor de beroepsbeoefenaar, volgbaar voor de leek. Vaktermen worden gebruikt zoals in de praktijk; concepten worden kort gepositioneerd waar nuance telt. Geen pedagogische basisuitleg.

Drie-stelsels-valkuil: maak telkens expliciet of een regel uit BE GAAP, IFRS-EU of IFRS-IASB komt. IFRS 15 en IFRS 16 zijn EU-geëndorseerd; IAS 2 ook.

Behandel "een Belgische beursgenoteerde groep" als generiek illustratie-anker waar het bundle geen specifieke vennootschapsnaam noemt — geen feit, alleen voorbeeld van het principe.

Spreek niet uit naam van de examinator. Voorbeeldexamens zijn data, geen voorschriften. Toon van een collega die meedenkt, niet van een autoriteit.

Deep-dive-aflevering: drie thema's waar IFRS scherp afwijkt van BE GAAP op een manier die de balans en het resultaatprofiel direct verandert — opbrengsten (IFRS 15), voorraden (IAS 2) en leasing (IFRS 16). Bouwt op de inleidende aflevering en deep-dive 1. Geen herhaling — direct in de cognitieve last.

Wat de luisteraar na deze aflevering moet kunnen:
- Het 5-stappen-model van IFRS 15 toepassen: contract identificeren → prestatieverplichtingen identificeren → transactieprijs bepalen → toewijzen aan prestatieverplichtingen → opbrengst opnemen wanneer / naarmate een prestatieverplichting wordt vervuld
- Het contrast met BE GAAP duiden: KB WVV art. 3:18 — opbrengst aangenomen wanneer winsten gerealiseerd zijn op balansdatum (realisatiebeginsel). Het verschil zit vooral in de tijdsbepaling en in de splitsing van een contract in meerdere prestatieverplichtingen
- IAS 2-regels voor voorraadwaardering hanteren: enkel FIFO of gewogen gemiddelde toegelaten (LIFO verboden); contrast met BE GAAP waar LIFO wél is toegestaan — een LIFO-gebruiker die overstapt naar IFRS moet herrekenen
- IFRS 16 toepassen op de lessee-kant: alle leases on-balance → right-of-use-actief + leaseverplichting → afschrijving op het actief + financieringskosten op de verplichting. Het BE GAAP-onderscheid operationeel versus financieel verdwijnt aan lessee-kant; aan lessor-kant blijft het bestaan
- De balans- en ratio-impact aanvoelen: IFRS toont meer activa én meer schulden bij lessees — debt/equity stijgt, EBITDA stijgt (huurlast wordt afschrijving + interest)
- Sale-and-leaseback onder IFRS 16 schetsen: opname als verkoop afhankelijk van overdracht van controle (IFRS 15-toets); zo ja: deel van de winst gerealiseerd, deel uitgesteld via right-of-use; zo nee: financieringstransactie

Onderwerpen die aan bod moeten komen (volgorde en pacing vrij):
- IFRS 15 5-stappen-model — geen losse memorisatie maar als ketting (contract → prestatieverplichtingen → prijs → toewijzing → opname). Vergelijking met BE GAAP-realisatiebeginsel
- Typische valkuilen IFRS 15: combinatie van goederen en diensten in één contract, opname over tijd versus op één moment, variabele vergoedingen
- IAS 2 voorraadwaardering: FIFO of gewogen gemiddelde (LIFO verboden). Lower of cost or net realisable value als algemeen kader
- IFRS 16 lessee-zijde: alle leases on-balance, right-of-use-actief + leaseverplichting; afschrijving + interest in resultaat (in plaats van vlakke huurlast). Vergelijk met BE GAAP: alleen financiële lease op balans, operationele lease off-balance
- IFRS 16 lessor-zijde: onderscheid operationeel versus finance lease blijft (in tegenstelling tot lessee-zijde) — een nuance die in examens makkelijk wegzakt
- Sale-and-leaseback onder IFRS 16: overdracht van controle als scharnier
- Korte stip op de cluster-redenering uit de hoofdverschillen-matrix: deze drie thema's vallen samen onder 'balansomvang' en 'resultaatdynamiek' — IFRS-resultaat is hier volatieler dan BE GAAP

Tone-hints: drie thematische blokken — laat de hosts elk apart afhandelen, niet versmolten. Vermijd "let's dive in"-openings. Geen cijferreeksen behalve waar één doorgewerkte stap (bv. een lease-amortisatieschema-conceptueel) de redenering draagt. Houd telkens BE GAAP als contrast vlak naast IFRS.
```

---

# 🎙️ Deep-dive 3 — Stelselwissel + foutcorrecties (IFRS 1, CBN 2022/08) (±20 min)

```text
Gebruik UITSLUITEND inhoud uit het geüploade document `1-5-beginselen-van-de-europese-wetgeving-notebooklm-bundle.md`. Geen externe bronnen, geen aanvullingen uit andere wetgevingen, geen verzonnen voorbeelden. Bij twijfel: zeg "dit staat niet in het bundle". Belgische context (WVV, KB WVV, CBN, IFRS-EU via Verordening 1606/2002, IASB) — niet Nederland.

Doelpubliek (gemengd): ervaren beroepsbeoefenaar (5-15 jaar accountancy-ervaring) bereidt het ITAA-examen voor, soms luistert een geïnteresseerde leek mee. Toon: vakgesprek tussen twee gecertificeerde accountants (of GA + kandidaat-GA). De stagiair-luisteraar vangt het gesprek op, wordt niet rechtstreeks aangesproken. Voldoende diep voor de beroepsbeoefenaar, volgbaar voor de leek. Vaktermen worden gebruikt zoals in de praktijk; concepten worden kort gepositioneerd waar nuance telt. Geen pedagogische basisuitleg.

Drie-stelsels-valkuil: IFRS 1 is een IFRS-EU-standaard; CBN 2022/08 is een Belgisch advies dat de retour-richting (IFRS → BE GAAP) procedureel begeleidt. Voor de heenrichting (BE GAAP → IFRS) is IFRS 1 leidend.

Behandel "een Belgische beursgenoteerde groep" als generiek illustratie-anker waar het bundle geen specifieke vennootschapsnaam noemt — geen feit, alleen voorbeeld van het principe.

Spreek niet uit naam van de examinator. Voorbeeldexamens zijn data, geen voorschriften. Toon van een collega die meedenkt, niet van een autoriteit.

Deep-dive-aflevering: het procedurele werk rond een stelselwissel. Bouwt op de twee thematische IFRS-deep-dives — je weet nu wáár BE GAAP en IFRS verschillen, hier leer je hoé je van het ene naar het andere overstapt. Geen herhaling — direct in de procedurele kern.

Wat de luisteraar na deze aflevering moet kunnen:
- IFRS 1 als project plaatsen: niet een mechanische cijferconversie maar een traject met openingsbalans, vrijstellingen-keuze, aansluitingstabellen en communicatie naar gebruikers — typisch maanden werk
- De vijf stappen van een eerste IFRS-toepassing schetsen: bepaal datum van overgang → stel openingsbalans op (retrospectief alsof altijd IFRS) → pas verplichte uitzonderingen en optionele vrijstellingen toe → maak aansluitingstabellen (eigen vermogen + resultaat van vergelijkende periode) → presenteer de eerste IFRS-jaarrekening
- Aanvoelen waarom het aanpassingsverschil rechtstreeks in de ingehouden winsten landt — niet in het resultaat van de overgangsperiode (anders zou de overgang als 'gerealiseerd' verschijnen, wat niet de bedoeling is)
- Typische voorbeelden van aanpassingen op overgang noemen: geactiveerde onderzoekskosten schrappen (IAS 38), operationele leases on-balance brengen (IFRS 16), voorzieningen herijken aan IAS 37-criteria, goodwill-afschrijving stopzetten + impairment-test op overgangsdatum (IAS 36)
- De omgekeerde richting (IFRS → BE GAAP) plaatsen via CBN 2022/08 als procedureel kader: vergelijkbare logica maar in spiegelbeeld — bv. right-of-use uitboeken, ontwikkelingskosten herbeoordelen
- Foutcorrecties versus wijziging van waarderingsregels onderscheiden: foutcorrectie = retroactief, herstelt vorige fout in beginbalans en in vergelijkende cijfers; wijziging waarderingsregels = prospectief of retroactief afhankelijk van het regime, met aankondiging in toelichting

Onderwerpen die aan bod moeten komen (volgorde en pacing vrij):
- Stelselwissel als project, geen druk-op-een-knop — waarom maanden werk
- IFRS 1 vijf stappen — datum van overgang, openingsbalans, vrijstellingen, aansluitingstabellen, eerste jaarrekening
- Verplichte uitzonderingen versus optionele vrijstellingen — kort positioneren, niet detail
- Aanpassingsverschil in ingehouden winsten (niet in resultaat van overgangsperiode)
- Concrete aanpassings-voorbeelden uit het bundle: onderzoekskosten schrappen, leases on-balance, voorzieningen herijken, goodwill-afschrijving stopzetten
- CBN 2022/08: de retour-richting IFRS → BE GAAP procedureel — spiegelbeeld-logica
- Foutcorrecties versus wijziging van waarderingsregels — retroactief versus prospectief, toelichting-vereisten
- Korte stip: communicatie naar gebruikers van de jaarrekening is even belangrijk als de cijfers — wie leest deze rekening en verwacht consistentie?

Tone-hints: procedure-aflevering, dus stappenwerk; laat de hosts elke stap zichtbaar afhandelen. Vermijd "let's dive in"-openings. Geen cijferreeksen behalve waar één doorgewerkt voorbeeld de redenering draagt (bv. één aanpassing in de openingsbalans). Behandel concrete aanpassingen als illustraties van het principe, niet als limitatieve opsomming.
```

---

# 🎙️ Recap podcast (optioneel, ±8-10 min)

```text
Gebruik UITSLUITEND inhoud uit het geüploade document `1-5-beginselen-van-de-europese-wetgeving-notebooklm-bundle.md`. Geen externe bronnen, geen aanvullingen uit andere wetgevingen, geen verzonnen voorbeelden. Bij twijfel: zeg "dit staat niet in het bundle". Belgische context (WVV, KB WVV, CBN, IFRS-EU via Verordening 1606/2002, IASB) — niet Nederland.

Doelpubliek (gemengd): ervaren beroepsbeoefenaar (5-15 jaar accountancy-ervaring) die de vier eerdere afleveringen al gehoord heeft, soms een geïnteresseerde leek mee. Toon: vakgesprek tussen gecertificeerde accountants (of GA + kandidaat-GA), volgbaar voor de leek. De stagiair-luisteraar vangt het gesprek op, wordt niet rechtstreeks aangesproken.

Drie-stelsels-valkuil één keer kort herhalen: BE GAAP / IFRS-EU / IFRS-IASB. Spreek niet uit naam van de examinator.

Korte consolidatie-aflevering. Geen nieuwe stof.

Wat de luisteraar na deze recap moet kunnen:
- De vijf zwaartepunten van het programmaonderdeel positioneren (twee stelsels + Europees kader → presentatie + vaste activa + impairment → opbrengsten + voorraden + leasing → stelselwissel → cheatsheet-clusters)
- Per zwaartepunt het kernspanningsveld benoemen (waar zit de cognitieve last, niet waar de feitenkennis)

Onderwerpen die aan bod moeten komen (één keer kort per blok):
- Twee referentiestelsels + Europese architectuur + endorsement + IFRS-toepassingsgebied België
- IFRS-presentatie + vaste activa + impairment — vooral de impairment-redenering en het goodwill-contrast
- IFRS-opbrengsten + voorraden + leasing — vooral de balans-impact van IFRS 16 lessee-zijde
- Stelselwissel: project, geen knop; aanpassingsverschil in ingehouden winsten
- Drie thematische clusters uit de hoofdverschillen-matrix: balansomvang, resultaatdynamiek, opnamecriteria

Tone-hints: consolidatie, geen nieuwe voorbeelden. Vermijd "let's dive in"-openings.
```

---

# 📊 Diapresentatie — één deck voor het hele programmaonderdeel

```text
Gebruik UITSLUITEND inhoud uit het geüploade document `1-5-beginselen-van-de-europese-wetgeving-notebooklm-bundle.md`. Geen externe bronnen, geen aanvullingen uit andere wetgevingen, geen verzonnen voorbeelden. Bij twijfel: zeg "dit staat niet in het bundle". Belgische context (WVV, KB WVV, CBN, IFRS-EU via Verordening 1606/2002, IASB) — niet Nederland.

Doelpubliek (gemengd): primair een ervaren beroepsbeoefenaar (5-15 jaar accountancy-ervaring) die de stof opfrist voor het ITAA-examen — niet noodzakelijk dagelijks met IFRS-dossiers bezig. Daarnaast kan een geïnteresseerde leek het deck bekijken. Toon: vakgesprek tussen twee gecertificeerde accountants (of GA + kandidaat-GA). De stagiair-luisteraar vangt het gesprek op, wordt niet rechtstreeks aangesproken. Vaktermen worden gebruikt zoals in de praktijk; concepten worden gepositioneerd waar nuance telt. Geen pure jargon-stapeling, geen legalese.

Drie-stelsels-valkuil expliciet vasthouden in het deck: BE GAAP (KB WVV, statutair) / IFRS-EU (endorsed, afdwingbaar in EU) / IFRS-IASB (uitgegeven door IASB, niet automatisch EU-recht).

"Een Belgische beursgenoteerde groep" als generiek illustratie-anker waar het bundle geen specifieke vennootschapsnaam noemt — illustratie, geen feit.

Eén slidedeck dat het volledige programmaonderdeel Europese wetgeving en IFRS dekt op overzichtsniveau. NotebookLM bepaalt zelf het aantal slides, de volgorde van details binnen elk zwaartepunt, en de visuele indeling.

Wat de student na het doorbladeren van deze deck moet kunnen:
- Het Europese tweesporenbeleid plaatsen (richtlijn 2013/34/EU + verordening 1606/2002) en het IFRS-toepassingsgebied in België toepassen (enkelvoudig = BE GAAP; geconsolideerd = IFRS bij beursnotering / financiële sector)
- De endorsement-procedure schetsen + het BE GAAP / IFRS-EU / IFRS-IASB-onderscheid hanteren
- De vijf componenten van een IFRS-jaarrekening opnoemen + de vijf algemene presentatiebeginselen
- De hoofdverschillen BE GAAP versus IFRS clusteren in drie groepen — balansomvang, resultaatdynamiek, opnamecriteria
- Per IFRS-domein de kernregel benoemen: IAS 16 (kostprijs of herwaardering, componentenbenadering), IAS 38 (onderzoek = kost, ontwikkeling = 6 criteria), IAS 36 (impairment-model + goodwill-test), IFRS 15 (5-stappen-model), IAS 2 (FIFO of gewogen gemiddelde, LIFO verboden), IFRS 16 (alle leases on-balance lessee)
- De vijf stappen van IFRS 1 schetsen + de positie van het aanpassingsverschil (ingehouden winsten, niet resultaat)

Inhoudelijke clusters die in het deck moeten landen:
- Twee referentiestelsels + filosofieën (rule-based versus principle-based) + Europese architectuur — diagram uit het bundle mag letterlijk over
- IFRS-toepassingsgebied beslisboom (welke jaarrekening? welk niveau? beursnotering?)
- Endorsement-procedure als filter — drie-stelsels-valkuil expliciet
- Hoofdverschillen BE GAAP versus IFRS — overzichtstabel uit het bundle mag letterlijk over
- Drie thematische clusters van verschil (balansomvang · resultaatdynamiek · opnamecriteria)
- IAS 1 vijf componenten + vijf presentatiebeginselen
- IAS 16 + IAS 38 + IAS 36: vaste activa + impairment — kernregels + contrast met BE GAAP
- IFRS 15 5-stappen-model + IAS 2 voorraden + IFRS 16 leasing (lessee on-balance, lessor onderscheid blijft)
- IFRS 1 stappenplan + CBN 2022/08 voor retour-richting
- Foutcorrecties versus wijziging waarderingsregels

Stijl: NotebookLM bepaalt zelf alle vormaspecten. Cruciale tabellen, beslisbomen en de hoofdverschillen-matrix uit het bundle mogen letterlijk over. Eén deck, gemaakt om snel doorheen te bladeren als revisie — niet om de detail-stof te vervangen.
```

---

# 🎨 Overzichts-infographic — architectuur BE GAAP / IFRS-EU / IFRS-IASB + endorsement

```text
Gebruik UITSLUITEND inhoud uit het geüploade document `1-5-beginselen-van-de-europese-wetgeving-notebooklm-bundle.md`. Geen externe bronnen, geen aanvullingen uit andere wetgevingen, geen verzonnen voorbeelden. Bij twijfel: zeg "dit staat niet in het bundle". Belgische context (WVV, KB WVV, CBN, IFRS-EU via Verordening 1606/2002, IASB) — niet Nederland.

Doelpubliek (gemengd): ervaren beroepsbeoefenaar bereidt het ITAA-examen voor, met af en toe een geïnteresseerde leek die meekijkt. Vaktermen gebruiken zoals in de praktijk; geen pure jargon-stapeling, geen legalese.

Drie-stelsels-valkuil is het centrale beeld van deze infographic: BE GAAP / IFRS-EU / IFRS-IASB moeten visueel uit elkaar staan.

Eén infographic-pagina die de architectuur van het programmaonderdeel visueel ordent. NotebookLM bepaalt zelf de indeling, kleurkeuze en grafische metaforen.

Centrale boodschap: dezelfde economische werkelijkheid wordt onder twee fundamenteel verschillende kaders afgebeeld — BE GAAP voor de enkelvoudige Belgische statutaire jaarrekening, IFRS-EU voor de geconsolideerde rekening van EU-beursgenoteerden (en de financiële sector). Het Europese kader rust op twee instrumenten (richtlijn + verordening), en alleen IFRS-IASB-standaarden die door de Europese Commissie zijn geëndorseerd (via EFRAG + comitologie) worden IFRS-EU en zijn afdwingbaar in de EU.

Wat de student na het bekijken van deze infographic moet kunnen:
- Het Europese tweesporenbeleid plaatsen (richtlijn 2013/34/EU = minimumkern voor élke jaarrekening, omgezet via KB WVV; verordening 1606/2002 = IFRS-plicht voor specifieke ring)
- Het IFRS-toepassingsgebied in België beredeneren: enkelvoudig → BE GAAP; geconsolideerd + EU-beursgenoteerd → IFRS-EU; geconsolideerd + financiële sector → IFRS-EU; overige geconsolideerd → BE GAAP-consolidatie
- De drie stelsels uit elkaar houden (BE GAAP / IFRS-EU / IFRS-IASB) en herkennen dat een nog-niet-geëndorseerde IASB-standaard niet afdwingbaar is in de EU
- De endorsement-keten schetsen (IASB → EFRAG-advies → Commissie → comitologie → afdwingbaar)

Inhoudelijke elementen die moeten doorkomen:
- Drie 'lanen' of zones voor de drie stelsels — visueel uit elkaar
- Europese architectuur: richtlijn versus verordening, met pijl naar nationale omzetting (KB WVV) versus directe werking (IFRS-EU)
- Endorsement-keten als filter — wat passeert wel, wat niet
- Beslisboom IFRS-toepassingsgebied België — vereenvoudigd
- Korte aanstip van waar de vier deep-dive-blokken in deze architectuur zitten (1: presentatie + vaste activa + impairment; 2: opbrengsten + voorraden + leasing; 3: stelselwissel)

Stijl: NotebookLM kiest de indeling. Houd de accentkleuren coherent over alle infographics voor Europese wetgeving en IFRS (dit deck + de drie cluster-infographics hieronder).
```

---

# 🎨 Cluster-infographic 1 — Hoofdverschillen-matrix BE GAAP versus IFRS

```text
Gebruik UITSLUITEND inhoud uit het geüploade document `1-5-beginselen-van-de-europese-wetgeving-notebooklm-bundle.md`. Geen externe bronnen, geen aanvullingen uit andere wetgevingen, geen verzonnen voorbeelden. Bij twijfel: zeg "dit staat niet in het bundle". Belgische context (WVV, KB WVV, CBN, IFRS-EU via Verordening 1606/2002, IASB) — niet Nederland.

Doelpubliek: ervaren beroepsbeoefenaar die de stof opfrist. "Een Belgische beursgenoteerde groep" als generiek illustratie-anker.

Drie-stelsels-valkuil: maak in de matrix expliciet dat IFRS-kolom IFRS-EU bedoelt (de geëndorseerde versie).

Eén infographic-pagina die de hoofdverschillen tussen BE GAAP en IFRS naast elkaar plaatst, gegroepeerd in drie thematische clusters.

Centrale boodschap: de verschillen tussen BE GAAP en IFRS zijn niet willekeurig — ze vallen in drie clusters die je in een examencasus systematisch kunt afgaan: (a) balansomvang (IFRS toont meer activa én meer schulden), (b) resultaatdynamiek (IFRS is volatieler), (c) opnamecriteria (IFRS strikter voor activering maar dwingender voor andere posten).

Wat de student na het bekijken van deze infographic moet kunnen:
- Voor een gegeven post (vaste activa / goodwill / leasing / onderzoek / ontwikkeling / opbrengsten / voorraden / voorzieningen / reële waarde / uitgestelde belastingen) de BE GAAP-behandeling en de IFRS-behandeling naast elkaar plaatsen
- De post toewijzen aan een van de drie thematische clusters
- Bij een examenvraag "noem drie verschillen tussen BE GAAP en IFRS" telkens uit één cluster kiezen om coverage te tonen

Inhoudelijke elementen die moeten doorkomen:
- Matrix met drie kolommen (post · BE GAAP · IFRS-EU) — gebaseerd op de hoofdverschillen-tabel uit het bundle (algemeen kader · componenten jaarrekening · materiële vaste activa · onderzoekskosten · ontwikkelingskosten · goodwill · leasing lessee · opbrengsten · voorraden · voorzieningen · reële waarde · uitgestelde belastingen)
- Visuele markering per rij naar welk cluster de post behoort (balansomvang · resultaatdynamiek · opnamecriteria)
- Korte 'kerngevolg'-kolom — het belangrijkste praktijkverschil per post
- Apart accent: goodwill (BE GAAP afschrijving default 5 jaar versus IFRS impairment-only) en leasing lessee (BE GAAP financieel/operationeel onderscheid versus IFRS alles on-balance)

Stijl: NotebookLM kiest de indeling. Coherent met de overzichts-infographic + de andere cluster-infographics.
```

---

# 🎨 Cluster-infographic 2 — Vijf-componenten IFRS-jaarrekening + presentatiebeginselen

```text
Gebruik UITSLUITEND inhoud uit het geüploade document `1-5-beginselen-van-de-europese-wetgeving-notebooklm-bundle.md`. Geen externe bronnen, geen aanvullingen uit andere wetgevingen, geen verzonnen voorbeelden. Bij twijfel: zeg "dit staat niet in het bundle". Belgische context (WVV, KB WVV, CBN, IFRS-EU via Verordening 1606/2002, IASB) — niet Nederland.

Doelpubliek: ervaren beroepsbeoefenaar die de stof opfrist. Illustratie-anker: "een Belgische beursgenoteerde groep" — illustratie, geen feit.

Drie-stelsels-valkuil: presentatie-eisen zijn IFRS-EU (IAS 1 zoals geëndorseerd).

Eén infographic-pagina die de vijf verplichte componenten van een IFRS-jaarrekening + de vijf algemene presentatiebeginselen visueel ordent.

Centrale boodschap: een IFRS-jaarrekening is breder dan een typische BE GAAP-jaarrekening — vijf componenten zijn voor iedereen verplicht (niet alleen voor groot schema), en vijf algemene beginselen sturen elke component.

Wat de student na het bekijken van deze infographic moet kunnen:
- De vijf componenten opnoemen (balans · totaalresultaat · mutatieoverzicht eigen vermogen · kasstroomoverzicht · toelichting) en aangeven welke onder BE GAAP niet algemeen verplicht zijn
- De vijf presentatiebeginselen plaatsen (going concern · accruals · materialiteit · consistentie · verbod op compensatie) en aanvoelen waar elk effect heeft (bv. compensatie-verbod tussen vorderingen/schulden of opbrengsten/kosten)
- Het brede begrip totaalresultaat duiden (P&L + OCI) en weten dat OCI bestanddelen bevat die later eventueel naar P&L recycleren

Inhoudelijke elementen die moeten doorkomen:
- Vijf componenten als verticale kolommen of segmenten, met per component één zin "wat zit erin"
- Vijf presentatiebeginselen als overkoepelende laag — geen losse weetjes maar als sturende principes
- Korte aanstip: balanspresentatie vlottend versus niet-vlottend (IFRS-standaard); totaalresultaat = P&L + OCI; mutatieoverzicht eigen vermogen niet vergeten
- Mini-contrast met BE GAAP: KB WVV verplicht voor klein/micro een verkorter schema; IFRS dwingt alle vijf componenten ongeacht omvang

Stijl: NotebookLM kiest de indeling. Coherent met de overzichts-infographic + de andere cluster-infographics.
```

---

# 🎨 Cluster-infographic 3 — Stelselwissel-stappenplan (BE GAAP → IFRS én IFRS → BE GAAP)

```text
Gebruik UITSLUITEND inhoud uit het geüploade document `1-5-beginselen-van-de-europese-wetgeving-notebooklm-bundle.md`. Geen externe bronnen, geen aanvullingen uit andere wetgevingen, geen verzonnen voorbeelden. Bij twijfel: zeg "dit staat niet in het bundle". Belgische context (WVV, KB WVV, CBN, IFRS-EU via Verordening 1606/2002, IASB) — niet Nederland.

Doelpubliek: ervaren beroepsbeoefenaar die de stof opfrist. Illustratie-anker: "een Belgische beursgenoteerde groep" — illustratie, geen feit.

Drie-stelsels-valkuil: IFRS 1 = IFRS-EU-standaard; CBN 2022/08 = Belgisch advies voor retour-richting.

Eén infographic-pagina die het stelselwissel-traject visueel uitwerkt — heen (BE GAAP → IFRS via IFRS 1) en terug (IFRS → BE GAAP via CBN 2022/08).

Centrale boodschap: een stelselwissel is geen druk-op-een-knop maar een procedureel project van maanden, met een retroactieve openingsbalans en het aanpassingsverschil in ingehouden winsten — niet in het resultaat van de overgangsperiode.

Wat de student na het bekijken van deze infographic moet kunnen:
- De vijf stappen van IFRS 1 in volgorde noemen (datum van overgang → openingsbalans → vrijstellingen + uitzonderingen → aansluitingstabellen → eerste IFRS-jaarrekening)
- Aanduiden waar het aanpassingsverschil belandt (ingehouden winsten) en waarom (anders zou de overgang als gerealiseerd verschijnen)
- Drie of vier typische aanpassingen op overgang noemen (onderzoekskosten schrappen · leases on-balance · voorzieningen herijken · goodwill-afschrijving stoppen + impairment-test)
- De retour-richting via CBN 2022/08 als spiegelbeeld plaatsen (right-of-use uitboeken, ontwikkelingskosten herbeoordelen)

Inhoudelijke elementen die moeten doorkomen:
- Tijdlijn-element met datum van overgang als ankerpunt
- Vijf-stappen-blok voor IFRS 1
- Apart blok voor het aanpassingsverschil → ingehouden winsten (visueel benadrukken dat het NIET door het resultaat loopt)
- Voorbeelden-cluster: typische aanpassingen die de openingsbalans raken
- Spiegelbeeld-blok: CBN 2022/08 voor de retour-richting
- Korte aanstip van foutcorrecties versus wijziging waarderingsregels — retroactief versus prospectief, toelichting-vereisten

Stijl: NotebookLM kiest de indeling. Coherent met de overzichts-infographic + de andere cluster-infographics.
```

---

## Plan-samenvatting (1 oogopslag)

| Volgorde | Output | Lengte / formaat | Daglimiet? |
|---|---|---|---|
| 1 | 🎙️ Inleidende podcast | ±20 min | Dag 1 — telt in 3/dag |
| 2 | 🎙️ Deep-dive 1 — presentatie + vaste activa + impairment | ±20 min | Dag 1 — telt in 3/dag |
| 3 | 🎙️ Deep-dive 2 — opbrengsten + voorraden + leasing | ±20 min | Dag 1 — telt in 3/dag (3/3) |
| 4 | 🎙️ Deep-dive 3 — stelselwissel + foutcorrecties | ±20 min | Dag 2 — telt in 3/dag |
| 5 | 🎙️ Recap (optioneel) | ±8-10 min | Dag 2 — telt in 3/dag |
| — | 📊 Slidedeck (één voor heel programmaonderdeel) | Aantal slides vrij | Geen limiet |
| — | 🎨 Overzichts-infographic | Eén pagina | Geen limiet |
| — | 🎨 Cluster-infographic 1 — hoofdverschillen-matrix | Eén pagina | Geen limiet |
| — | 🎨 Cluster-infographic 2 — vijf componenten + presentatiebeginselen | Eén pagina | Geen limiet |
| — | 🎨 Cluster-infographic 3 — stelselwissel-stappenplan | Eén pagina | Geen limiet |

Plan past in 2 dagen (intro + 2 deep-dives dag 1; deep-dive 3 + optionele recap dag 2). Visuele afgeleiden parallel.
