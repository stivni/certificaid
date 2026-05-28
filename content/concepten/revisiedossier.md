---
title: "Revisiedossier"
concept_type: "instrument"
schema_version: "2.2"
status: "concept"
categorieen:
  - entiteit
ankers:
  - 1.6.III.D
  - 1.6.IV
tags:
  - concept
  - schema-2.2
  - type-instrument
  - cat-entiteit
  - status-concept
gegenereerd_uit: "data/concepten/records/revisiedossier.json"
---

# Revisiedossier

_Instrument_

🏢 Entiteit · Anchors: `1.6.III.D` · `1.6.IV` · Wave: `skeleton-controle-beroep-2026-05-28`

> [!info] 📝 **Concept** — content gevuld door cluster-extract; niet door mens-verify gegaan.

**Synoniemen**: audit working papers · auditdossier · werkdocumenten · audit file · controledossier · werkdossier — **Vertalingen**: fr: dossier de révision · en: audit working papers / audit file

## Definitie

📖 Het revisiedossier is de **gestructureerde verzameling van alle werkdocumenten, controlebewijzen en conclusies** die de gecertificeerd accountant of bedrijfsrevisor tijdens een opdracht opbouwt. ISA 230 schrijft voor dat de documentatie ‘voldoende is om een ervaren auditor die voorheen niet bij de controle betrokken was in staat te stellen om inzicht te verwerven in (a) aard, timing en omvang van de uitgevoerde controlewerkzaamheden, (b) uitkomsten en verkregen informatie, (c) significante aangelegenheden + getrokken conclusies + significante professionele oordeelsvorming’. Het dossier wordt logisch verdeeld in een **permanent gedeelte** (multi-jaar-stabiele info) en een **lopend gedeelte** (per boekjaar).

<small>📚 ISA 230 — par. 8 — _norm_ · ITAA-norm-algemene-controlenorm — § 4 Werkdocumenten — _norm_</small>

## Substantie

🔗 Het dossier is meer dan een archief — het is **bewijslast-architectuur** in fysieke vorm. Bij latere tucht- of aansprakelijkheidsvragen is het revisiedossier het enige document dat aantoont *wat* de auditor deed en *waarom* hij zijn conclusies trok. Een werkdocument moet zelf-verklarend zijn (titel, doel, bron, uitgevoerde procedure, conclusie, verantwoordelijke, reviewer, datum). De ‘ervaren-auditor-test’ uit ISA 230 par. 8 is de centrale norm: een collega die het dossier voor het eerst openslaat, moet binnen aanvaardbare tijd kunnen reconstrueren wat is gedaan.

De scheiding permanent vs lopend dossier is niet alleen efficiëntie maar ook **methodologie**: het permanente dossier vormt de basisinzichten waarop elke jaarlijkse controle voortbouwt, terwijl het lopende dossier het verhaal van één controlecyclus vertelt — van planning over bewijs tot eindoordeel.

<small>📚 ISA 230 — par. 8 ervaren-auditor-test — _norm_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Rationale

🔗 Waarom dossier-discipline? (1) **Bewijsbaar werk**: zonder dossier bestaat het werk niet voor een tuchtprocedure of rechter — adagium ‘not documented = not done’. (2) **Reviewability**: senior reviewers en eventuele engagement quality reviewer moeten op basis van het dossier kunnen oordelen. (3) **Kennisoverdracht**: bij teamwissel of opvolger-auditor (initiële controle) levert het permanente dossier de basisinzichten. (4) **Toetsing door toezichthouder**: ITAA inspecteert kwaliteit periodiek; ontbreken dossier-documentatie = tuchtfout. (5) **Vertrouwelijkheid + ownership**: het dossier is eigendom van het kantoor (niet van cliënt), valt onder beroepsgeheim, mag niet zomaar worden gedeeld.

<small>📚 ISA 230 — _norm_ · ITAA-norm-intern-kwaliteitsmanagement — _norm_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Gebruikscontext

**Status**: `in-voege` · basis: ISA 230 · ISA 220 (herzien) · ITAA-norm-intern-kwaliteitsmanagement (inwerkingtreding 3 september 2025) · ITAA-norm-algemene-controlenorm § 4 · Wet 7 december 2016 (bedrijfsrevisorenwet) art. 19 (dossier-bewaring)

ITAA-norm-intern-kwaliteitsmanagement vervangt vroegere ISQC 1; treedt in werking 3/9/2025 conform art. 72 Wet 17/3/2019.

**📋 Voorwaarden**
- 📖 ISA 230 par. 14-16: de auditor moet de **administratieve afronding van het definitieve controledossier** voltooien binnen **60 dagen na de datum van de controleverklaring**. Vanaf dat moment mogen geen nieuwe documenten toegevoegd of verwijderd worden, alleen administratieve aanpassingen (paginanummering, indexering) die niet de inhoud beïnvloeden.

## Sub-concepten

### 📦 Permanent dossier  
_`instrument` (subconcept)_

#### Definitie

🔗 Multi-jaar-stabiele informatie over de entiteit, ondersteunt elke jaarlijkse controle:

- **Juridische structuur**: statuten + wijzigingen, KBO-uittreksel, aandeelhoudersregister, organogram, deelnemingen-overzicht, lijst verbonden partijen.
- **Governance**: samenstelling bestuur + commissaris-mandaat, charter auditcomité, RACI-matrices.
- **Materiële contracten**: bankkredieten + covenants, huurcontracten, leasingen, grote leveranciers- en klantcontracten, IP-licenties.
- **IT-architectuur**: systemen, datastromen, IT-controle-evaluatie, segregation-of-duties-matrix.
- **Verslaggevingsstelsel**: gekozen stelsel (BE-GAAP/IFRS-EU), waarderingsregels, accounting manual.
- **Sector-context**: marktonderzoek, regulatory framework, benchmarks.
- **Historiek vorige controles**: management letters, gesignaleerde IC-deficiënties + remediëring, going-concern-analyses.

Wordt jaarlijks geactualiseerd, niet herschreven.

<small>📚 ITAA-norm-algemene-controlenorm — § 4 — _norm_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### 📦 Lopend dossier (jaardossier)  
_`instrument` (subconcept)_

#### Definitie

📖 Werkdocumenten van de huidige controlecyclus, gestructureerd per fase:

**Fase 1 — Aanvaarden**: continuering-memo, onafhankelijkheidschek, opdrachtbrief, KYC-update.

**Fase 2 — Plannen**: kennis-entiteit-update, walk-throughs, IC-evaluatie, materialiteits-bepaling, risico-inschatting per assertion, team-bespreking-memo fraude, audit strategy, werkprogramma per cyclus, budget + tijdsplanning.

**Fase 3 — Bewijswerk**: werkdocumenten per programmapunt (titel · doel · bron · procedure · uitkomst · conclusie · uitvoerder · reviewer · datum), cyclus-werkdocumenten (verkopen/aankopen/voorraad/lonen/...), externe bevestigingen ontvangen, schattingen-evaluaties, fraude-procedures, NOCLAR-inquiries.

**Fase 4 — Afronden**: subsequent-events-memo, going-concern-analyse, clearing memo (SAD-list), overall analytical review, LOR ondertekend, ISA 260-memo bestuur, ISA 265-management-letter, ondertekende verklaring + eventueel EQR-review.

Elk werkdocument verwijst naar het werkprogramma-punt waar het bewijs voor levert.

<small>📚 ISA 230 — par. 8-13 vorm + inhoud — _norm_</small>

## Bouwstenen

### 📜 Ervaren-auditor-test (ISA 230 par. 8)  
_`regel`_

📖 De centrale documentatie-norm: een ervaren auditor die *niet* bij de controle betrokken was moet uit het dossier kunnen reconstrueren (a) wát is uitgevoerd (aard, timing, omvang procedures), (b) uitkomsten en verkregen informatie, (c) significante aangelegenheden + conclusies + de professionele oordeelsvorming die tot die conclusies leidde. Maatstaf voor: wat moet er minstens in elk werkdocument staan, hoe gedetailleerd, met welke verwijzingen.

Praktische implicatie: een dossier met cijfer-tabellen zonder uitleg van bron, procedure en conclusie zakt door deze test — ook al ‘kloppen’ de cijfers.

<small>📚 ISA 230 — par. 8 + A6-A7 — _norm_</small>

### 📜 Onderscheidende kenmerken van geteste items vastleggen  
_`regel`_

📖 ISA 230 par. 9: bij documentatie van uitgevoerde procedures moet de auditor vastleggen (a) de onderscheidende kenmerken van geteste items (welke specifieke transacties, welke facturen, welke saldi); (b) wie de werkzaamheden heeft uitgevoerd; (c) de datum; (d) wie de werkzaamheden heeft beoordeeld; (e) de datum + omvang van de beoordeling. Reden: zonder traceability is herhaalbaarheid en controleerbaarheid niet mogelijk.

<small>📚 ISA 230 — par. 9 + A12 — _norm_</small>

### 📜 Bewaartermijn dossier  
_`regel`_

📖 Het revisiedossier moet bewaard worden gedurende ten minste **vijf jaar** vanaf de datum van de controleverklaring (ISA 230 + Wet 7 december 2016 art. 19 voor bedrijfsrevisoren). Voor antiwitwas-aspecten: 10 jaar (ITAA-norm AWW). Praktijk vaak langer (verjaringstermijnen contractuele aansprakelijkheid 10 jaar in BE).

<small>📚 ITAA-norm-aww-richtlijn-bibf — § 6 Documentatie en bewaring — _norm_ · Wet 7 december 2016 — art. 19 — _wettekst_</small>

### 📜 Eigendom dossier + toegang derden  
_`regel`_

🔗 Het revisiedossier is eigendom van het auditkantoor — niet van de cliënt. De cliënt heeft géén recht op inzage in de werkdocumenten van de auditor. Toegang door derden: (a) ITAA-inspecteurs in kader van kwaliteitstoetsing; (b) opvolger-auditor met toestemming cliënt (overdrachtsgesprek); (c) gerechtelijke autoriteiten op gemotiveerd verzoek (binnen grenzen beroepsgeheim — art. 458 SW + art. 75/86 Wet 7 december 2016).

<small>📚 ITAA-norm-intern-kwaliteitsmanagement — par. 12 (boeken/documenten cliënt na beëindiging) — _norm_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Valkuilen

### ⚠️ Dossier = verzameling losse Excels

**Verkeerde assumptie**: Een dossier is een map met de spreadsheets en gescande documenten van het audit-jaar.

**Kernpunt**: Een dossier is een gestructureerd verhaal: per cyclus per assertion een werkdocument dat doel, bron, procedure, uitkomst en conclusie expliciet verbindt aan het werkprogramma. Cross-references tussen werkdocumenten zijn essentieel. Een ongedocumenteerde Excel (geen bron, geen procedure-beschrijving) is geen audit-werkdocument.

<small>📚 ISA 230 — par. 8 — _norm_</small>

### ⚠️ Dossier afwerken na uitgifte verklaring

**Verkeerde assumptie**: Na ondertekening kan ik de losse eindjes nog vlot afwerken — niemand kijkt mee.

**Kernpunt**: ISA 230 par. 14-16: administratieve afronding mag tot 60 dagen na verklaring; daarna **geen nieuwe inhoud** toevoegen of verwijderen. Een werkdocument later ‘bedenken’ om een gat te dichten is fraude in het dossier — direct tuchtfout en bewijslast omgekeerd.

<small>📚 ISA 230 — par. 14-16 — _norm_</small>

### ⚠️ Cliënt vraagt om bepaalde werkdocumenten — uitleveren

**Verkeerde assumptie**: De cliënt betaalt voor de controle, hij krijgt inzage in alle werkdocumenten op vraag.

**Kernpunt**: Het dossier is eigendom van het kantoor, niet van de cliënt. Uitlevering van werkdocumenten aan cliënt is uitzonderlijk en op gemotiveerde basis (vaak in conflict met onafhankelijkheid — zelf-review-bedreiging). Bij wisseling auditor: overdracht via overdrachtsgesprek + gestructureerd informatiedeel, niet bulk-overdracht van werkdocumenten.

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Accountant-perspectieven

### De accountant als dossier-houder

#### 🔍 Auditor

##### 👣 Standaard-template werkdocument  
_`stap`_

📖 Elk werkdocument bevat: (1) titel + cliënt + boekjaar + werkprogramma-referentie; (2) doel (welke assertion test ik?); (3) bron (welke documenten/data, hoe verkregen, betrouwbaarheid); (4) uitgevoerde procedure (welke stappen, welke steekproef, welk criterium); (5) uitkomsten (cijfers, observaties); (6) conclusie + impact op vervolgprocedures of oordeel; (7) opgesteld door (initialen + datum); (8) gereviewd door (initialen + datum) + commentaar reviewer; (9) cross-references naar andere werkdocumenten.

<small>📚 ISA 230 — par. 8-9 — _norm_ · ITAA-norm-algemene-controlenorm — § 4 — _norm_</small>

## Verder lezen (scope-out)

- → Cyclus-context (output van bewijswerk) → [[controleopdracht]] _(moet-verwijzen)_
- → Bewijs dat in dossier wordt opgenomen → [[audit-bewijs]] _(moet-verwijzen)_
- → Planning-documentatie → [[audit-planning]] _(moet-verwijzen)_
- → ISQM-dossiervorming-eisen → [[kwaliteitsmanagement-opdracht]] _(moet-verwijzen)_
- → Vertrouwelijkheid + beroepsgeheim-aspect → [[beroepsgeheim]] _(moet-verwijzen)_

## Relaties

### `valt_onder`
- [[controleopdracht]]
### `vereist`
- [[kwaliteitsmanagement-opdracht]]
- [[beroepsgeheim]]
