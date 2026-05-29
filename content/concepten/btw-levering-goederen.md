---
title: "BTW — Levering van goederen"
concept_type: "verrichting"
schema_version: "2.2"
status: "concept"
categorieen:
  - gebeurtenis
  - regeling
ankers:
  - 2.4.I
tags:
  - concept
  - schema-2.2
  - type-verrichting
  - cat-gebeurtenis
  - cat-regeling
  - status-concept
gegenereerd_uit: "data/concepten/records/btw-levering-goederen.json"
---

_Verrichting_ · ook: btw-levering · levering van een goed · livraison de biens

## Definitie

Een levering van een goed in de zin van het W.BTW is de overdracht of overgang van de macht om als een eigenaar over een lichamelijk goed te beschikken (art. 10, §1 W.BTW). Het materiële begrip 'overdracht van de beschikkingsmacht' is ruimer dan de civielrechtelijke eigendomsoverdracht: het volstaat dat de afnemer feitelijk kan beslissen over het goed als ware hij eigenaar — ook als de juridische eigendom nog niet is overgegaan (bv. eigendomsvoorbehoud, financiële lease met aankoopoptie).

<small>📖 W.BTW — art. 10, §1 — _wettekst_ · Richtlijn 2006/112/EG — art. 14 — _richtlijn_</small>

## Substantie

De kwalificatie 'levering van goederen' (vs dienstverrichting) is cruciaal omdat ze de plaats-van-handeling-regels bepaalt (art. 14-15 vs art. 21), de opeisbaarheid (art. 16 vs art. 22) en bij internationale handel de scheidingslijn tussen intracommunautaire levering (art. 39bis), uitvoer (art. 39) en gewone binnenlandse levering. Het W.BTW gebruikt het feitelijke beschikkingscriterium om misbruik via splitsing of via afwijkende juridische structuren te neutraliseren: wie de feitelijke macht over het goed verkrijgt, wordt geacht het ontvangen te hebben, ongeacht de civiele kwalificatie van de overeenkomst.

<small>🔗 W.BTW — art. 10 + art. 14-16 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Rationale

Ratio: het W.BTW kiest voor een economisch-functioneel begrip levering — niet voor een formele civielrechtelijke definitie — om twee redenen: (1) harmonisatie met het EU-recht (HvJ-EU Safe Rekencentrum, C-320/88: overdracht van de macht 'as if owner'); (2) anti-misbruik — partijen mogen door de keuze van contractvorm (huurkoop, lease met aankoopoptie, eigendomsvoorbehoud) het btw-tijdstip niet wegschuiven. De gelijkstellingen in art. 12 zorgen voor neutraliteit bij eigen verbruik, onttrekkingen en gratis afgiften — anders zou wie zijn eigen voorraad gebruikt of weggeeft, btw-vrij ontsnappen aan het stelsel.

<small>🔗 HvJ-EU Safe Rekencentrum (C-320/88) — 08-02-1990 — _rechtspraak_ · W.BTW — art. 12 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Gebruikscontext


**✅ Voor**
- 📖 Alle situaties waarin een belastingplichtige onder bezwarende titel een lichamelijk goed overdraagt aan een afnemer: verkoop (cash of op rekening), ruil, levering tegen vergoeding in natura, koop-en-verkoop in commissie, huurkoop, financiële lease met aankoopoptie (art. 10, §2, b), levering door of namens overheid op grond van wet of besluit (art. 10, §2, a).

**⛔ Uitsluitingen**
- 📖 Niet-lichamelijke goederen (vorderingen, rechten, software-licenties, elektriciteit-overdracht zonder vervoer) — kwalificeren als dienstverlening (art. 18) tenzij specifiek anders bepaald (elektriciteit, gas, warmte, koeling worden door art. 9 als 'lichamelijk goed' beschouwd voor btw-doeleinden). Operationele leasing zonder aankoopoptie blijft dienstverlening.

**🟢 Indicaties**
- 🔗 Signalen die op levering wijzen: fysieke overdracht van het goed, factuur met productcode + aantal, transportdocument, eigendomsoverdracht volgens INCOTERMS, overhandiging sleutels (bij voertuig/gebouw).

**🔴 Contra-indicaties**
- 🔗 Signalen die op dienst wijzen: factuur per uur, periodieke abonnementsbetaling, opdracht 'tot doen' eerder dan 'tot geven', focus op resultaat-arbeid (advies, ontwerp, bewaring, vervoer). Bij combinatie (gemengde prestatie): bekijk de hoofdprestatie (HvJ-EU CPP, Levob).

**⚠️ Risico**
- 🔗 Foutieve kwalificatie als dienstverlening waar het in wezen een levering betreft (of omgekeerd) leidt tot foute plaats-van-handeling-toepassing (intracommunautaire vs binnenlandse btw), fout opeisbaarheidstijdstip en mogelijk tot dubbele heffing of niet-heffing. Bij verleggingsregeling (medecontractant betaalt btw): foute kwalificatie maakt verlegging onterecht — afnemer moet alsnog gewone btw betalen + boete + interesten.

## Sub-concepten

### 📦 Gewone levering — art. 10 W.BTW

#### Definitie

Art. 10, §1 W.BTW: de overdracht of overgang van de macht om als eigenaar over een lichamelijk goed te beschikken. Art. 10, §2 stelt drie bijzondere situaties uitdrukkelijk gelijk: (a) overdracht ingevolge vordering van of namens de overheid (onteigening tegen vergoeding); (b) huur met automatische eigendomsovergang of koop-op-afbetaling (financiële lease); (c) overdracht ingevolge koop of verkoop in commissie. Art. 10, §3: ook verbruiklening (afgifte + teruggaaf) wordt als levering aangemerkt.

<small>📖 W.BTW — art. 10 — _wettekst_</small>

### 📦 Gelijkstellingen met levering — art. 12 W.BTW

#### Substantie

Art. 12 W.BTW stelt vier situaties met een levering onder bezwarende titel gelijk om btw-neutraliteit te verzekeren bij eigen verbruik, onttrekkingen of gratis afgiften. Bij elk van deze 'fictieve leveringen' is de belastingplichtige zelf zowel leverancier als afnemer, of geeft hij iets weg waarvoor hij de input-btw al had afgetrokken. Zonder gelijkstelling zou hij btw-vrij ontsnappen.

<small>📖 W.BTW — art. 12 — _wettekst_</small>

#### 🧭 Vier gelijkstellingen art. 12 W.BTW

**Substantie**: Vier scenario's waarin geen civiele overdracht plaatsvindt maar btw toch verschuldigd is.

<small>📖 W.BTW — art. 12 — _wettekst_</small>

### 📦 Tijdstip van de levering — art. 16 W.BTW

#### Definitie

Het tijdstip van de levering is in beginsel het moment waarop het goed ter beschikking van de afnemer wordt gesteld (art. 16, §1 W.BTW). Bijzondere regels: bij verzending of vervoer = vertrek van de verzending; bij installatie of montage = na afronding; bij goederen met aankoopoptie = afgifte; bij koop-op-afbetaling = afgifte; bij doorlopende leveringen (water, gas, elektriciteit) = einde van de afrekenperiode (max 1 jaar).

<small>📖 W.BTW — art. 16 — _wettekst_</small>

## Voorbeelden

> [!example]- Levering versus dienst — vijf concrete casussen
> _Toets telkens: is er overdracht van de macht 'als eigenaar' over een lichamelijk goed?_
>
> | Casus | Kwalificatie | Reden |
>
> | --- | --- | --- |
>
> | Aankoop laptop bij Coolblue voor 1 000 EUR | Levering | Lichamelijk goed + macht 'als eigenaar' overgaat bij afgifte |
>
> | Maandelijkse SaaS-licentie cloudboekhoudpakket | Dienst | Geen lichamelijk goed — gebruiksrecht op software |
>
> | Operationele lease auto 5 jaar zonder aankoopoptie | Dienst | Geen automatische eigendomsovergang — gebruiksrecht |
>
> | Financiële lease laptop met aankoopoptie 1 EUR aan einde | Levering (vanaf afgifte) | Art. 10, §2, b — bedingt dat eigendom uiterlijk bij laatste termijn overgaat |
>
> | Aannemer levert en plaatst keuken in nieuwbouw | Werk in onroerende staat (= dienst, art. 18, §1, 1°) | Inkluderende werken op onroerend goed zijn dienst, niet levering |
>
> <small>🔗 W.BTW — art. 10 + art. 18 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Valkuilen

> [!warning]- Civiele eigendom ≠ btw-levering
> **Verkeerde assumptie**: Btw is verschuldigd pas wanneer de civiele eigendom overgaat (na betaling laatste termijn).
>
> **Kernpunt**: Btw kijkt naar de feitelijke beschikkingsmacht 'als eigenaar', niet naar de civiele eigendom. Bij eigendomsvoorbehoud of financiële lease met aankoopoptie is de levering — en dus de btw — verschuldigd bij de afgifte van het goed, niet bij de eigendomsovergang. Anders kunnen partijen via contractuele truc de btw uitstellen.
>
> <small>📖 W.BTW — art. 10, §2, b + art. 16 — _wettekst_ · HvJ-EU Safe Rekencentrum (C-320/88) — 08-02-1990 — _rechtspraak_</small>

> [!warning]- Levering + dienst in één factuur
> **Verkeerde assumptie**: Bij een gemengde prestatie (bv. levering keuken + plaatsing) splits je de factuur in twee btw-regimes.
>
> **Kernpunt**: Bij gemengde prestaties bekijk je de hoofdprestatie (HvJ-EU Levob, Card Protection Plan). Als de plaatsing van een keuken het hoofdvoorwerp is en de levering van materialen accessoir, kwalificeert het geheel als werk in onroerende staat (dienst, art. 18 — relevant voor verleggingsregeling onroerende werken). Als de levering hoofdvoorwerp is en de plaatsing slechts klein hulpwerk, geldt het regime levering. Splitsen wordt enkel toegestaan als de prestaties objectief deelbaar én onafhankelijk zijn.
>
> <small>🔗 HvJ-EU Levob (C-41/04) — 27-10-2005 — _rechtspraak_ · HvJ-EU CPP (C-349/96) — 25-02-1999 — _rechtspraak_</small>

> [!warning]- Gratis afgifte = levering
> **Verkeerde assumptie**: Wat je gratis weggeeft, is geen 'levering onder bezwarende titel' — dus geen btw verschuldigd.
>
> **Kernpunt**: Art. 12, §1, 3° W.BTW stelt gratis afgifte gelijk met een levering onder bezwarende titel — voor zover op de aankoop btw werd afgetrokken. Uitzondering: monsters en reclamegeschenken van maximum 50 EUR per stuk per begunstigde per jaar. Een schenk van voorraad aan een goed doel boven die drempel is dus btw-belast (maatstaf = aankoopprijs of kostprijs).
>
> <small>📖 W.BTW — art. 12, §1, 3° — _wettekst_</small>

## Verder lezen (scope-out)

- → Dienstverlening (afbakening) → [[btw-dienstverlening]] _(moet-verwijzen)_
- → Plaats-van-handeling regels → [[plaats-van-handeling-btw]] _(moet-verwijzen)_
- → Opeisbaarheid (tijdstip BTW verschuldigd) → [[opeisbaarheid-btw]] _(moet-verwijzen)_
- → Eigen werkzaamheid (art 19 W.BTW) → [[eigen-werkzaamheid-btw]] _(moet-verwijzen)_

## Relaties

### `valt_onder`
- [[btw]]
### `vergelijkbaar_met`
- [[btw-dienstverlening]] — Levering (art. 10) en dienstverrichting (art. 18) zijn de twee fundamentele soorten belastbare handelingen onder het W.BTW. De afbakening bepaalt plaats-van-handeling, opeisbaarheidstijdstip en bij grensoverschrijdende handel de regime-keuze.
    - **Gelijkenissen**:
        - Beide vereisen een belastingplichtige als uitvoerder
        - Beide moeten onder bezwarende titel gebeuren (behoudens gelijkstellingen)
        - Beide vallen onder de algemene btw-tarieven (0/6/12/21 %)
    - **Verschillen**:
        - Levering = overdracht macht op lichamelijk goed; dienst = elke andere handeling
        - Plaats van levering = vertrek goed (art. 14-15); plaats van dienst = afnemer-B2B of dienstverrichter-B2C (art. 21)
        - Tijdstip levering = ter beschikkingstelling; tijdstip dienst = voltooiing prestatie (art. 22)
        - Intracommunautair: levering = 0 % bij ICL (art. 39bis); dienst B2B = verlegging naar afnemer
    - ⚠️ **Verwarringsrisico**: Bij gemengde prestaties (levering + plaatsing) is de afbakening het meest betwist — hoofdprestatie-regel (HvJ-EU Levob/CPP) is leidend.
