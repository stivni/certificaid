---
title: "BTW — Dienstverlening"
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
gegenereerd_uit: "data/concepten/records/btw-dienstverlening.json"
---

_Verrichting_ · ook: btw-dienst · dienstverrichting btw · prestation de services

## Definitie

Een dienstverrichting in de zin van het W.BTW is elke handeling die geen levering van goederen is (art. 18, §1 W.BTW — restdefinitie). Concreet: arbeidsprestaties, intellectuele prestaties, overdracht of vestiging van rechten, verhuur, vervoer, bewaring, advies, telecommunicatie, elektronische diensten, werken in onroerende staat, cateringdiensten. De definitie is bewust ruim en negatief geformuleerd om alle economisch waardevolle handelingen te dekken die niet leiden tot overdracht van een lichamelijk goed.

<small>📖 W.BTW — art. 18, §1 — _wettekst_ · Richtlijn 2006/112/EG — art. 24 — _richtlijn_</small>

## Substantie

Diensten verschillen op drie cruciale punten van leveringen: (1) plaats van handeling — art. 21 hanteert het 'bestemmingslandbeginsel' (B2B: plaats van afnemer; B2C: plaats van dienstverrichter, met talrijke uitzonderingen voor onroerende, vervoer-, restaurant-, evenement- en elektronische diensten); (2) opeisbaarheid — art. 22 W.BTW: btw wordt opeisbaar zodra de dienst is voltooid of zodra de prijs vooraf wordt geïncasseerd, niet bij ter-beschikkingstelling van een goed; (3) bij grensoverschrijdende B2B-diensten geldt de verleggingsregeling (medecontractant betaalt btw in zijn eigen land) — een fundamenteel verschil met intracommunautaire goederenleveringen.

<small>🔗 W.BTW — art. 18 + art. 21 + art. 22 + art. 51, §2, 1° — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Rationale

Door dienst negatief te definiëren als restcategorie zorgt het W.BTW dat geen enkele economische handeling onbelast blijft door definitie-mazen: elk wat geen levering is en geen vrijstelling geniet, is per definitie een belastbare dienst. Dit principe van 'algemene heffing op verbruik' staat centraal in Richtlijn 2006/112/EG. De gelijkstellingen in art. 19 sluiten — naar analogie met art. 12 voor leveringen — privégebruik en gratis diensten in om btw-neutraliteit te waarborgen.

<small>🔗 Richtlijn 2006/112/EG — art. 1 + art. 24-26 — _richtlijn_ · W.BTW — art. 19 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Gebruikscontext


**✅ Voor**
- 🔗 Alle prestaties van belastingplichtigen die geen overdracht van een lichamelijk goed inhouden: advies, audit, accountancy, juridische dienstverlening, IT-ontwikkeling, hosting, SaaS, design, marketing, verhuur (al dan niet vrijgesteld), transport, bewaring, onderaanneming, bouwwerken (werk in onroerende staat), restaurant, hotelovernachting, cultuur- en sportprestaties.

**⛔ Uitsluitingen**
- 📖 Loonprestaties van een werknemer voor zijn werkgever (geen zelfstandigheid — geen belastingplichtige in de zin van art. 4 W.BTW) en handelingen die het W.BTW expliciet vrijstelt (art. 44: medisch, onderwijs, sociaal, financieel, verzekering, art. 41-42: internationaal vervoer).

**⚠️ Risico**
- 📖 Bij grensoverschrijdende B2B-diensten ligt de plaats van handeling bij de afnemer (art. 21, §2) — Belgische dienstverrichter factureert dan zonder btw met vermelding 'btw verlegd' (art. 51, §2, 1°). Wanneer de accountant deze regel mist en wel btw aanrekent, moet hij die btw afdragen aan de Belgische Schatkist (art. 51, §1, 3°) terwijl de afnemer ze niet kan recupereren — dubbele belasting.

## Sub-concepten

### 📦 Gewone dienstverrichting — art. 18 W.BTW

#### Definitie

Art. 18, §1 W.BTW: dienst = elke handeling die geen levering van een goed is. Art. 18, §1, tweede lid noemt een niet-limitatieve lijst voorbeelden: materieel of intellectueel werk (incl. werk in onroerende staat als aannemingscontract), overdracht of vestiging van een onlichamelijk goed (rechten, octrooien, licenties), verbintenis om iets niet te doen of een handeling te dulden, voltooiing van een dienst ingevolge vordering van overheid, ter beschikking stellen van personeel.

<small>📖 W.BTW — art. 18, §1 — _wettekst_</small>

### 📦 Gelijkstellingen met dienst — art. 19 W.BTW

#### Substantie

Art. 19 W.BTW stelt bepaalde situaties met dienstverrichting onder bezwarende titel gelijk om btw-neutraliteit te bewaren bij privégebruik van bedrijfsgoederen en bij gratis diensten — spiegelbeeld van art. 12 voor leveringen.

<small>📖 W.BTW — art. 19 — _wettekst_</small>

#### 🧭 Gelijkstellingen art. 19 W.BTW

**Substantie**: Twee categorieën gelijkstellingen.

<small>📖 W.BTW — art. 19 — _wettekst_</small>

### 📦 Specifieke dienstcategorieën met eigen plaats-van-handeling-regel

#### Substantie

Voor bepaalde diensten geldt een specifieke plaats-van-handeling-regel die afwijkt van de B2B/B2C-hoofdregels. Deze regel volgt vaak het 'plaats van werkelijk gebruik'-beginsel.

<small>🔗 W.BTW — art. 21bis + art. 22 — _wettekst_</small>

#### 🧭 Specifieke dienstcategorieën — plaats van handeling

**Substantie**: Zes specifieke categorieën met eigen plaatsbepaling.

<small>📖 W.BTW — art. 21bis — _wettekst_</small>

## Valkuilen

> [!warning]- Werk in onroerende staat = dienst, niet levering
> **Verkeerde assumptie**: Bij een aannemer die materialen levert en plaatst, is het 'leveringsdeel' een levering en het 'plaatsingsdeel' een dienst.
>
> **Kernpunt**: Werk in onroerende staat (bouw, renovatie, installatie van keuken/badkamer, schilderwerk) is volledig dienstverrichting in de zin van art. 18, §1, 1° W.BTW — ook al worden materialen in het werk geïntegreerd. Geen splitsing. Belang: verleggingsregeling 'medecontractant' (KB nr. 1 art. 20) is van toepassing bij B2B-werk in onroerende staat tussen Belgische btw-plichtigen.
>
> <small>📖 W.BTW — art. 18, §1, 1° — _wettekst_ · K.B. nr. 1 van 29-12-1992 — art. 20 — _kb_</small>

> [!warning]- SaaS en software-downloads zijn diensten
> **Verkeerde assumptie**: Wanneer een klant software 'koopt' (download of licentie), is dat een levering van goederen.
>
> **Kernpunt**: Software die elektronisch wordt geleverd (download, SaaS, licentie zonder fysieke drager) is een elektronische dienst (art. 18, §1, 2° W.BTW). Plaats van handeling B2C = afnemer-land (OSS-aangifte). Alleen software op fysieke drager (DVD, USB) = levering van goed. Het onderscheid is cruciaal voor de internationale facturatie.
>
> <small>🔗 W.BTW — art. 18 + art. 21bis — _wettekst_ · Uitvoeringsverordening (EU) 282/2011 — art. 7 — _richtlijn_</small>

> [!warning]- Gratis dienst kan toch btw-belast zijn
> **Verkeerde assumptie**: Een dienst zonder factuur of zonder geldelijke vergoeding kan geen btw-handeling zijn.
>
> **Kernpunt**: Art. 19, §2 W.BTW stelt een gratis dienst gelijk met een dienst onder bezwarende titel wanneer ze wordt verricht voor andere doeleinden dan de economische activiteit (privé, gratis voor familie). De maatstaf van heffing is dan de gemaakte kosten — niet de marktwaarde.
>
> <small>📖 W.BTW — art. 19, §2 + art. 33 — _wettekst_</small>

## Verder lezen (scope-out)

- → Levering goederen (afbakening) → [[btw-levering-goederen]] _(moet-verwijzen)_
- → Plaats-van-handeling diensten (B2B-hoofdregel · B2C-uitzonderingen) → [[plaats-van-handeling-btw]] _(moet-verwijzen)_
- → Opeisbaarheid bij dienstverlening → [[opeisbaarheid-btw]] _(moet-verwijzen)_

## Relaties

### `valt_onder`
- [[btw]]
### `vergelijkbaar_met`
- [[btw-levering-goederen]] — Dienst (art. 18) is de restcategorie tegenover levering (art. 10). De afbakening bepaalt plaats van handeling, opeisbaarheid en bij grensoverschrijdende handel het regime (verleggingsregeling vs intracommunautaire levering).
    - **Gelijkenissen**:
        - Beide vereisen een belastingplichtige als uitvoerder
        - Beide moeten onder bezwarende titel gebeuren (behoudens gelijkstellingen)
        - Beide vallen onder de algemene btw-tarieven
    - **Verschillen**:
        - Dienst = restdefinitie ('alles wat geen levering is'); levering = overdracht macht over lichamelijk goed
        - Dienst B2B grensoverschrijdend = verleggingsregeling (afnemer betaalt btw); levering ICL = 0 % bij overdracht
        - Tijdstip dienst = voltooiing (art. 22); tijdstip levering = ter-beschikkingstelling (art. 16)
        - Bij gemengde prestaties (levering + dienst): hoofdprestatie-regel HvJ-EU Levob
