---
title: "Gewestelijke fiscale procedure"
concept_type: "procedure"
schema_version: "2.2"
status: "concept"
categorieen:
  - gebeurtenis
ankers:
  - 2.7.I.A
  - 2.7.I.B
tags:
  - concept
  - schema-2.2
  - type-procedure
  - cat-gebeurtenis
  - status-concept
gegenereerd_uit: "data/concepten/records/gewestelijke-fiscale-procedure.json"
---

_Procedure_ · ook: procedure Vlaamse Codex Fiscaliteit · procedure gewestbelastingen

## Definitie

De gewestelijke fiscale procedure is de regeling voor de vestiging, betwisting en invordering van gewest-belastingen — voornamelijk erfbelasting, registratiebelasting, onroerende voorheffing, verkeersbelasting en (Vlaanderen) belasting op leegstand. Elk gewest heeft een eigen codex: de Vlaamse Codex Fiscaliteit (VCF) — beheerd door Vlabel; de Brusselse Codex Fiscale Procedure (Bruxelles Fiscalité); en het Waals Wetboek (Walfin). De procedures lijken sterk op de federale (taxatie, bezwaar, gerechtelijk) maar verschillen in termijnen, organen en eigen accenten (bv. eigen bemiddelingsdienst).

<small>📖 Vlaamse Codex Fiscaliteit — Titel 3 — _wettekst_ · Brusselse Codex Fiscale Procedure — Ordonnantie 6 maart 2019 — _wettekst_</small>

## Substantie

Voor de accountant is het cruciaal te weten of een belasting federaal of gewestelijk is: voor erfbelasting in Vlaanderen schrijf je een bezwaar aan Vlabel, niet aan de federale gewestelijke directie. Termijnen verschillen (Vlabel-bezwaar: 3 maanden vanaf aanslagbiljet, niet 6 maanden zoals federaal). Bemiddeling loopt via Vlabel-bemiddeling (niet de federale FBD). Het gerechtelijk vervolg is identiek aan federaal: rechtbank van eerste aanleg → hof van beroep → Cassatie.

<small>🔗 Vlaamse Codex Fiscaliteit — art. 3.5.0.0.1 + Hoofdstuk 5 (bezwaar) — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Rationale

Sinds de overheveling van fiscale bevoegdheden naar de gewesten (vooral via de bijzondere financieringswet en de overname inning door Vlabel sinds 2015) hebben de gewesten autonomie gekregen over eigen tarieven én procedures. Het resultaat is een gefragmenteerd landschap dat de stagiair moet kunnen navigeren — niet alles is federaal. De Brusselse Codex 2019 is een eerste poging tot codificatie; Wallonië werkt nog met versnipperde regels.

<small>🔗 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Gebruikscontext

**Status**: `in-voege` · basis: VCF (sinds 2014) + Brusselse Codex (sinds 2020) + Walfin

Vlabel int Vlaamse heffingen sinds 1 januari 2015 (erfbelasting, registratie, onroerende voorheffing); de Brusselse Codex Fiscale Procedure is in werking sinds 1 januari 2020. Wallonië hervormt geleidelijk.

## Bouwstenen

### 📜 Vlaamse Codex Fiscaliteit (VCF) — Vlabel

Vlabel (Vlaamse Belastingdienst) int de Vlaamse heffingen: erfbelasting, registratie-belastingen, onroerende voorheffing, verkeersbelasting, leegstandsheffing. Procedure in Titel 3 VCF. Bezwaar bij Vlabel binnen 3 maanden vanaf de derde werkdag na verzending aanslagbiljet (art. 3.5.0.0.1). Beslissing door Vlabel. Beroep bij rechtbank van eerste aanleg van Brussel (Vlaanderen heeft gecentraliseerde fiscale rechtspraak in Brussel voor Vlabel-zaken).

<small>📖 Vlaamse Codex Fiscaliteit — art. 3.5.0.0.1 + Hoofdstuk 5 — _wettekst_</small>

### 📜 Brusselse Codex Fiscale Procedure — Bruxelles Fiscalité

Brussel hervormde zijn fiscale procedure in de Ordonnantie van 6 maart 2019 (Brusselse Codex Fiscale Procedure, in werking 1 januari 2020). Bruxelles Fiscalité is de gewestelijke fiscale administratie. De Codex bevat eigen regels over bewijsmiddelen (art. 53), onderzoeksbevoegdheden, sancties (art. 86 — administratieve boete), en gedwongen invordering (art. 57 — toerekening betalingen). Bruxelles Fiscalité kan ook gemeentebelastingen innen via akkoordprotocol (art. 118).

<small>📖 Brusselse Codex Fiscale Procedure — Ordonnantie 6 maart 2019, art. 53 + 57 + 86 + 118 — _wettekst_</small>

### 📜 Waalse fiscale procedure

Wallonië heeft (nog) geen volledig eigen codex maar versnipperde regels (Walfin — Service public de Wallonie / Recettes wallonnes). De inning van gewest-heffingen wordt geleidelijk overgenomen van de federale fiscus (erfbelasting + registratie sinds 2021). Procedure leunt aan bij federale regels met eigen accenten.

<small>🔗 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### 🧭 Verschillen met federale procedure

Belangrijkste verschillen tussen Vlaamse en federale procedure: (1) bezwaartermijn 3 maanden (VCF) vs 6 maanden (WIB92); (2) bezwaaradres = Vlabel, niet de gewestelijke directie; (3) eigen bemiddelingsdienst Vlabel — niet de federale FBD; (4) gerechtelijk vervolg op één locatie (rechtbank Brussel) voor Vlabel-dossiers. Brussel volgt eigen Codex met meer afwijkingen. Wallonië hybride.

<small>🔗 Vlaamse Codex Fiscaliteit — art. 3.5.0.0.1 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Valkuilen

> [!warning]- Vlabel ≠ FOD Financiën
> **Verkeerde assumptie**: Bezwaar tegen erfbelasting moet bij de federale gewestelijke directie ingediend worden.
>
> **Kernpunt**: Erfbelasting is in Vlaanderen een Vlabel-bevoegdheid sinds 2015. Bezwaar gaat naar Vlabel met een termijn van 3 maanden (niet 6 zoals federaal). Aanslagen onder oude federale-inningsdocumenten kunnen verwarrend zijn — kijk altijd naar de uitvoerende dienst op het biljet.
>
> <small>📖 Vlaamse Codex Fiscaliteit — art. 3.5.0.0.1 — _wettekst_</small>

> [!warning]- Niet alle 'gewestbelastingen' = autonome gewestbelastingen
> **Verkeerde assumptie**: Alles wat in een gewest gevorderd wordt, valt onder gewestelijke procedure.
>
> **Kernpunt**: Onderscheid: (1) gewestbelastingen sensu stricto (volledig gewestelijk: erfbelasting Vlabel, leegstand); (2) aanvullingen op federale belasting (bv. aanvullende gemeentebelasting PB — federaal geïnd); (3) federale belastingen met regionale opcentiemen. Procedure volgt de inningsdienst, niet de bestemming.
>
> <small>🔗 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Syntheses

### 🧩 Matrix

Bezwaartermijn en bemiddelingsdienst per gewestelijke belastingautoriteit.

| Vlabel (Vlaanderen) | Bruxelles Fiscalité | Walfin (Wallonië) | Federaal (WIB92) |
| --- | --- | --- | --- |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |
|  |  |  |  |

## Verder lezen (scope-out)

- → Federale fiscale procedure (verschillen) → [[fiscale-procedure]] _(moet-verwijzen)_
- ✂ Lokale belasting-reglement (apart pad)

## Relaties

### `valt_onder`
- [[lokale-en-regionale-belastingen]]
### `vergelijkbaar_met`
- [[fiscale-procedure]]
