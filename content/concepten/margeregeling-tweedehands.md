---
title: "Margeregeling tweedehandsgoederen"
concept_type: "regime"
schema_version: "2.2"
status: "concept"
categorieen:
  - regeling
ankers:
  - 2.4.IV
tags:
  - concept
  - schema-2.2
  - type-regime
  - cat-regeling
  - status-concept
gegenereerd_uit: "data/concepten/records/margeregeling-tweedehands.json"
---

_Regime_ · ook: winstmargeregeling · art. 58 §4 WBTW · marge-regime tweedehands

## Definitie

De margeregeling (WBTW art. 58 §4) is een bijzondere BTW-regeling voor belastingplichtige wederverkopers van tweedehandsgoederen, kunstvoorwerpen, voorwerpen voor verzamelingen en antiquiteiten. In plaats van BTW te berekenen op de volledige verkoopprijs, wordt BTW geheven enkel op de WINSTMARGE — het verschil tussen verkoopprijs en aankoopprijs (verminderd met de erin begrepen BTW). Doel: voorkomen dat tweedehandsgoederen dubbel BTW dragen (eerste verkoop nieuw + herverkoop tweedehands).

<small>📖 WBTW — art. 58 §4 — _wettekst_ · KB nr. 53 — art. 2 — _kb_</small>

## Substantie

Praktisch: een tweedehandshandelaar in auto's koopt een wagen aan voor 5.000 EUR van een particulier (geen BTW want particulier is geen belastingplichtige). Hij verkoopt door voor 7.000 EUR. Onder normale BTW zou hij 21 % op 7.000 = 1.470 EUR BTW moeten heffen → cumul. Onder marge: BTW op (7.000 − 5.000) = 2.000 EUR marge × 21/121 = 347 EUR BTW (de marge bevat BTW). De factuur aan de koper vermeldt GEEN BTW (omdat onder margeregeling) — koper kan dus ook GEEN aftrek claimen.

<small>🔗 WBTW — art. 58 §4, 2°-3° — _wettekst_ · claude-sonnet-4-5 — _ai_model_ — (2026-05-28)</small>

## Rationale

Zonder margeregeling zou tweedehandshandel niet leefbaar zijn: BTW al betaald bij eerste verkoop (door particulier of vrijgestelde) zou opnieuw geheven worden bij elke heruitverkoop. Het regime herstelt economische neutraliteit: BTW wordt enkel geheven op de toegevoegde waarde (= marge van de wederverkoper). EU-grondslag: art. 311-325 Richtlijn 2006/112.

<small>📖 Richtlijn 2006/112/EG — art. 311-325 (titel XII hoofdstuk 4) — _richtlijn_</small>

## Gebruikscontext

**Status**: `in-voege` · basis: WBTW art. 58 §4 + KB nr. 53 (23-12-1994)

Stabiel sinds 1995 (Belgische omzetting Richtlijn 94/5).

**📋 Voorwaarden**
- 📖 Cumulatieve toepassingsvoorwaarden: (1) de leverancier is een belastingplichtige WEDERVERKOPER (= zijn beroep is aan-/verkoop van tweedehands of antiek) — niet een toevallige verkoop; (2) de goederen zijn gebruikte goederen, kunstvoorwerpen, voorwerpen voor verzamelingen of antiquiteiten; (3) de aankoop gebeurde van: een NIET-belastingplichtige (particulier); een vrijgestelde belastingplichtige (art. 44); een belastingplichtige onder de vrijstellingsregeling (art. 56bis kleine onderneming); of een andere wederverkoper die zelf de margeregeling toepaste.

## Sub-concepten

### 📦 Marge per goed (individueel)

#### Definitie

Standaardmethode: voor elk goed afzonderlijk wordt de marge berekend = verkoopprijs − aankoopprijs. Wanneer marge negatief is (verlies): geen BTW verschuldigd (geen recuperatie, het verlies blijft als economische verlies). Werkt vooral bij specifieke, identificeerbare goederen (auto's, kunst, antiek).

<small>📖 KB nr. 53 — art. 3, eerste lid — _kb_</small>

### 📦 Globale margeregeling (per aangiftetijdvak)

#### Definitie

Voor fungibele of niet-individueel-identificeerbare voorwerpen (bv. kledingstukken, kleine objecten, postzegels, munten): in plaats van marge per goed mag de wederverkoper kiezen voor GLOBALE marge per aangiftetijdvak = (totaal verkoopprijzen van alle marge-goederen) − (totaal aankoopprijzen van alle marge-goederen in datzelfde tijdvak). Eindejaarsregularisatie: totale jaarmarge ofwel positief = BTW geheven, ofwel negatief = geen overdracht naar volgend jaar.

<small>📖 KB nr. 53 — art. 3, derde-vijfde lid — _kb_ · Richtlijn 2006/112/EG — art. 318 — _richtlijn_</small>

## Bouwstenen

### 🧮 Formule berekening BTW op marge

Marge incl. BTW = verkoopprijs − aankoopprijs. BTW-bedrag = marge_incl_BTW × tarief / (100 + tarief). Bv. tarief 21 % → BTW = marge × 21/121. Maatstaf van heffing = marge_incl_BTW − BTW.

<small>📖 WBTW — art. 58 §4, 5° — _wettekst_ · Richtlijn 2006/112/EG — art. 315 — _richtlijn_</small>

### 📜 Facturatie onder margeregeling

De factuur uitgereikt onder margeregeling vermeldt GEEN BTW-bedrag of -tarief afzonderlijk. Verplichte vermelding: 'Bijzondere regeling — gebruikte goederen' / 'Bijzondere regeling — kunstvoorwerpen' / 'Bijzondere regeling — voorwerpen voor verzamelingen en antiquiteiten' (Richtlijn art. 226, 14). Doel: de koper kan zien dat hij geen recht op aftrek heeft, en de prijs is incl. een impliciete marge-BTW.

<small>📖 WBTW — art. 58 §4, 7° — _wettekst_ · Richtlijn 2006/112/EG — art. 226, 14 — _richtlijn_</small>

### 📜 Geen recht op aftrek bij koper

De koper die een goed onder margeregeling koopt, kan GEEN BTW aftrekken (de BTW staat niet op factuur en is impliciet in de marge geconsolideerd). Dit is logisch: zou aftrek mogelijk zijn, dan zou het regime ineffectief worden (negatieve marge-belasting). Bij doorverkoop door koper-belastingplichtige: hij kan zelf opnieuw margeregeling toepassen (als wederverkoper), of normale regeling kiezen (dan BTW op volledige prijs — meestal nadelig).

<small>📖 WBTW — art. 45 §5 — _wettekst_</small>

### 📜 Inventarisplicht wederverkoper

De wederverkoper moet jaarlijks een INVENTARIS van de voorraad opmaken van goederen onderworpen aan de margeregeling (KB nr. 53 art. 2). Per goed: aankoopdatum, aankoopprijs, beschrijving. Onontbeerlijk voor BTW-controle en voor de marge-berekening bij doorverkoop.

<small>📖 KB nr. 53 — art. 2 — _kb_</small>

## Voorbeelden

> [!example]- Tweedehands auto — winstmarge
> _Garage Aurelia (BVBA, BTW-belastingplichtige wederverkoper) koopt op 15 maart 2026 een tweedehands wagen van een particulier voor 8.000 EUR. Verkoopt door op 20 april 2026 voor 12.000 EUR._
>
> **Berekening:**
>
> - Stap 1 — toets voorwaarden: wederverkoper ✓; gebruikt goed ✓; aankoop van particulier ✓ → margeregeling toepasselijk
> - Stap 2 — marge incl. BTW = 12.000 − 8.000 = 4.000 EUR
> - Stap 3 — BTW = 4.000 × 21/121 = 694,21 EUR
> - Stap 4 — maatstaf van heffing = 4.000 − 694,21 = 3.305,79 EUR
> - Stap 5 — factuur aan koper: 'Bijzondere regeling — gebruikte goederen — totaal te betalen 12.000 EUR' (geen BTW vermeld)
> - Stap 6 — BTW-aangifte: rooster 03 (binnenlandse leveringen 21 %): 3.305,79 EUR; rooster 54 (verschuldigde BTW): 694,21 EUR. Koopprijs niet in rooster 81/82 (geen aftrek).
>
> → **Resultaat**: Vergelijking met normale regeling: 12.000 × 21/121 = 2.082 EUR BTW. Margeregeling = 694 EUR. Besparing: 1.388 EUR voor de keten. Het tweedehandshandelaarschap is concurrentieel met particuliere verkoop dankzij dit regime.
>
> <small>📖 WBTW — art. 58 §4 — _wettekst_ · KB nr. 53 — art. 3 — _kb_</small>

> [!example]- Globale margeregeling — tweedehandskledingwinkel
> _Aurelia Vintage VOF verkoopt tweedehandskleding gekocht van particulieren via 'kilo-aankoop' (niet per stuk gewaardeerd). Q1 2026: totaal aankoopprijzen 5.000 EUR; totaal verkoopprijzen 9.000 EUR._
>
> **Berekening:**
>
> - Stap 1 — fungibele goederen + niet individueel waardeerbaar → globale marge toegelaten (KB nr. 53 art. 3)
> - Stap 2 — globale marge Q1 = 9.000 − 5.000 = 4.000 EUR incl. BTW
> - Stap 3 — BTW Q1 = 4.000 × 21/121 = 694,21 EUR
> - Stap 4 — Q4-jaarregularisatie: totaal jaarverkoop − totaal jaaraankoop − reeds aangegeven marges Q1-Q3 = eventuele resterende marge of negatieve marge (negatief = geen overdracht)
>
> → **Resultaat**: Globale methode vermijdt aankoopprijs-tracking per individueel kledingstuk. Eindejaars-regularisatie blijft verplicht.
>
> <small>📖 KB nr. 53 — art. 3, derde-vijfde lid — _kb_</small>

## Valkuilen

> [!warning]- Margeregeling toepassen op alle aankopen
> **Verkeerde assumptie**: 'Ik ben tweedehandshandelaar, dus alles is marge.'
>
> **Kernpunt**: Margeregeling werkt enkel voor aankopen van particulieren, vrijgestelde belastingplichtigen, kleine ondernemingen (art. 56bis) of andere wederverkopers onder margeregeling. Kopen van een normale BTW-plichtige (bv. fleet-management-bedrijf dat zijn wagenpark vernieuwt) = aankoop MET BTW → normale regime (BTW-aftrek bij aankoop + BTW op volledige verkoopprijs). Voor elk goed registreren wat de status van de leverancier was.
>
> <small>📖 WBTW — art. 58 §4, 2° — _wettekst_</small>

> [!warning]- BTW-aftrek claimen op aankoopprijs onder marge
> **Verkeerde assumptie**: 'Bij de aankoop van een tweedehands wagen voor 8.000 EUR kan ik 8.000 × 21/121 = 1.388 EUR BTW recupereren.'
>
> **Kernpunt**: Bij aankoop van een particulier was er GEEN BTW op de aankoop (particulier is niet BTW-plichtig). Er is dus niets om af te trekken. Het marge-mechanisme is ZELF de neutraliteits-correctie — geen aanvullende aftrek. Indien wel BTW op aankoop (bv. bij aankoop van een belastingplichtige): keuze normale regeling met aftrek + volledige BTW op verkoop OF margeregeling toepassen (mits voorwaarden) — niet beide.
>
> <small>📖 WBTW — art. 45 §5 — _wettekst_</small>

> [!warning]- Negatieve marge regenereren in volgend jaar
> **Verkeerde assumptie**: 'In Q4 had ik negatieve marge → ik schuif door naar Q1 volgend jaar.'
>
> **Kernpunt**: KB nr. 53 art. 3 expliciet: een negatieve totale jaarmarge geeft GEEN recht op overdracht naar volgend jaar. Het verlies blijft als economisch verlies bij de wederverkoper. Praktisch: regel je verkopen zodat globale jaarmarge positief blijft.
>
> <small>📖 KB nr. 53 — art. 3, vijfde lid — _kb_</small>

## Accountant-perspectieven

### Kantoor begeleidt tweedehandshandelaar

_De accountant bij een cliënt-wederverkoper (garage tweedehands, antiekhandelaar, kunstgalerij, vintage-kledingwinkel)._

#### 📒 Boekhouder

##### 👣 Marge-administratie opzetten

Voor elke aankoop: leverancierscategorie noteren (particulier / belastingplichtige / vrijgestelde / kleine onderneming) → bepaalt of margeregeling toepasselijk is. Per goed (of per categorie bij globaal): aankoopdatum + aankoopprijs in apart marge-register. Bij verkoop: linken aankoop ↔ verkoop, berekening marge, BTW-bedrag splitsen. Jaarlijkse inventaris opmaken (KB nr. 53 art. 2).

<small>🔗 KB nr. 53 — art. 2 + art. 3 — _kb_ · claude-sonnet-4-5 — _ai_model_ — (2026-05-28)</small>

#### 🧭 Adviseur

##### 🧭 Marge vs normale regeling — wanneer kiezen

Marge = voordelig wanneer hoge verkoopprijs en gering verschil met aankoop (lage marge ⇒ lage BTW). Normaal = voordelig wanneer aankoop MET BTW (aftrek) en lage verkoopmarge bij belastingplichtige koper (die ook aftrekt). De wederverkoper mag per LEVERING kiezen, mits niet onder voorbehoud (art. 58 §4, 4°). Belangrijk: B2B-verkoop met aftrekbare BTW kan ook normale regeling vereisen vanuit klant-vraag.

<small>🔗 WBTW — art. 58 §4, 4° — _wettekst_ · claude-sonnet-4-5 — _ai_model_ — (2026-05-28)</small>

## Verder lezen (scope-out)

- ↪ BTW-tarieven (op marge wel toe te passen) → [[btw-tarieven]] _(mag-verwijzen)_

## Relaties

### `valt_onder`
- [[btw]]
### `alternatief_referentiestelsel`
- [[btw]] — Margeregeling is een keuze-alternatief voor de normale BTW-regeling — niet beide tegelijk.
