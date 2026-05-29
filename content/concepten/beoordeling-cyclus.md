---
title: "Beoordeling-cyclus (review engagement)"
concept_type: "procedure"
schema_version: "2.2"
status: "concept"
categorieen:
  - kader
ankers:
  - 1.6.I.A
  - 1.6.I.B
tags:
  - concept
  - schema-2.2
  - type-procedure
  - cat-kader
  - status-concept
gegenereerd_uit: "data/concepten/records/beoordeling-cyclus.json"
---

_Procedure_ · ook: review engagement · beoordelingsopdracht · limited assurance engagement · ISRE-opdracht

## Definitie

De beoordeling (review engagement) is een assurance-opdracht met **beperkte mate van zekerheid** (limited assurance) over historische financiële informatie. De beroepsbeoefenaar voert procedures uit — voornamelijk navraag bij management en cijferanalyses (ISA 520 / ISRE 2400) — en formuleert een **conclusie in negatieve vorm**: ‘niets is ons onder de aandacht gekomen waaruit zou blijken dat de financiële overzichten geen getrouw beeld geven’. Normenkader: ISRE 2400 (herzien) voor beoordeling jaarrekening; ISRE 2410 voor tussentijdse financiële informatie door (onafhankelijke) auditor van de entiteit; ITAA-KMO-controlenorm hoofdstuk 4 voor BE-KMO-context.

<small>📖 ITAA-norm-kmo-controlenorm — § 1.1.2 (beperkte mate van zekerheid) — _norm_</small>

## Substantie

Een beoordeling is *geen controle-light*. Het is een **andersoortige opdracht** met een fundamenteel ander zekerheidsprofiel: in plaats van substantieel bewijswerk en risico-georiënteerde detail-tests komt het accent op (1) navraag bij management en governance over de financiële posten en transacties; (2) cijferanalyses — vergelijking met budget, voorgaande jaren, sector, plausibiliteit van ratio's en relaties. Externe bevestigingen, fysieke voorraadopname, herperformance van interne controles — al die diepwerk-procedures zijn **niet** vereist tenzij de procedures iets aan het licht brengen dat ze afdwingt.

Wat klinkt als een ‘zwakker’ product is feitelijk een ander product met een ander doel: een tussentijds rapport voor een aandeelhouder of bank, een snelle assurance-check op een kwartaalrapportering, een KMO-jaarafsluiting waar geen wettelijke controle vereist is maar wel ‘meer dan samenstelling’ gewenst.

<small>📖 ISRE 2400 (herzien) — Doelstellingen + Vereisten — procedures — _norm_ · ISA 520 — Cijferanalyses — _norm_</small>

## Rationale

Waarom een tussenniveau? Niet elke stakeholder heeft reasonable assurance nodig. Een KMO-bank die jaarlijks het kredietdossier opnieuw beoordeelt, kan met limited assurance leven — hij wil weten of er rode vlaggen zijn opgedoken sinds vorige check. Tussentijdse rapportering (Q2-cijfers) leent zich niet voor volwaardige audit-werk binnen weken na afsluiting — review past beter. De negatief geformuleerde conclusie weerspiegelt eerlijk de beperkte zekerheid: de auditor zegt niet ‘alles is OK’ maar ‘in wat ik zag is niets opgevallen’.

<small>🔗 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Gebruikscontext

**Status**: `in-voege` · basis: ISRE 2400 (herzien) · ISRE 2410 · ITAA-norm-kmo-controlenorm hfdst 4 + Bijlage 4 (modelverslag)

ISRE-stelsel sluit aan op IAASB-framework; de ITAA-KMO-controlenorm operationaliseert de beoordeling voor KMO en kleine (i)vzw/stichting in België.

**✅ Voor**
- 📖 Typische gebruikssituaties: (a) tussentijdse rapportering (Q1/Q2-cijfers) voor banken of investeerders; (b) jaarafsluiting van KMO zonder wettelijke commissaris maar waar bank/aandeelhouder meer dan samenstelling wil; (c) wettelijk voorbehouden review-mandaten (bv. omzettingsverslag staat van activa en passiva — ITAA-norm-omzetting); (d) due-diligence-toepassingen waar tijd/budget audit niet toelaat.

## Sub-concepten

### 📦 ISRE 2400 (herzien) — beoordeling historische jaarrekening

#### Definitie

Internationale standaard voor beoordelingsopdrachten over historische financiële overzichten waar de beroepsbeoefenaar **niet** de auditor van de entiteit is (of wel de auditor maar dan specifiek voor andere opdrachten dan de wettelijke controle). Vereist: opdrachtbrief, onafhankelijkheid, planning gebaseerd op inzicht in entiteit + risico-inschatting van waar materiële afwijkingen kunnen voorkomen, procedures (voornamelijk navraag + cijferanalyses), schriftelijke bevestiging management, conclusie in negatieve formulering. Aangepaste conclusie (met voorbehoud / negatief / onthouding) volgt vergelijkbare logica als ISA 705 voor audit.

<small>🔗 ISRE 2400 (herzien) — Toepassingsgebied + Vereisten — _norm_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### 📦 ISRE 2410 — beoordeling tussentijdse financiële informatie door auditor entiteit

#### Definitie

Specifiek voor het geval waarin de **commissaris/auditor van de entiteit** een review uitvoert op tussentijdse financiële informatie (typisch Q1, H1, 9M-cijfers van beursgenoteerde of grote groepen). Voordeel: hij kent de entiteit al uit zijn jaarcontrole en kan voortbouwen op zijn kennis-entiteit en risico-inschatting. Procedures blijven beperkt (navraag + cijferanalyses), conclusie is negatief geformuleerd.

<small>🔗 ISRE 2410 — Toepassingsgebied — _norm_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### 📦 KMO-review onder ITAA-controlenorm hoofdstuk 4

#### Definitie

Belgische uitwerking voor KMO en kleine (i)vzw/stichting. Werkstroom volgt dezelfde 4-fase-cyclus als de controleopdracht (aanvaarden · plannen · bewijswerk-beperkt-tot-navraag-en-analyse · afronden + verklaring) maar elke fase is **proportioneel afgestemd** op limited assurance:

- **Plannen** — inzicht in entiteit, risico-inschatting van plekken waar materiële afwijking waarschijnlijker is; geen volledige IC-evaluatie zoals bij audit.
- **Bewijswerk** — navraag bij management + cijferanalyses ISA 520; aanvullende procedures alleen indien navraag/analyse inconsistenties oplevert.
- **Afronden** — geaccumuleerde misstatements-evaluatie + schriftelijke bevestiging management + ondertekenen beoordelingsverslag.

De ITAA-KMO-controlenorm Bijlage 4 levert het standaard-model voor het beoordelingsverslag.

<small>📖 ITAA-norm-kmo-controlenorm — § 2.1.1 evenredigheid + hfdst 4 + Bijlage 4 — _norm_</small>

## Bouwstenen

### 📜 Negatieve oordeelsformulering — standaardtekst

Standaardformulering ITAA-modellen: *‘Op grond van de beoordeling is niets onder onze aandacht gekomen dat ons ertoe aanzet van mening te zijn dat [de financiële overzichten / staat van activa en passiva], in alle van materieel belang zijnde opzichten, niet is opgesteld in overeenstemming met het van toepassing zijnde stelsel inzake financiële verslaggeving.’*

Aangepaste conclusies (analoog aan ISA 705): conclusie met voorbehoud, ongunstige conclusie, of geen conclusie geformuleerd (oordeelonthouding). De materieel-en-diepgaand-test van ISA 705 wordt overeenkomstig toegepast.

<small>📖 ITAA-norm-omzetting-vennootschap — Conclusie — _norm_ · ITAA-norm-kmo-controlenorm — Bijlage 4 voorbeeldverslag — _norm_</small>

### ✴️ Evenredigheidsbeginsel (KMO)

ITAA-KMO-controlenorm § 2.1.1: de toepassing van de norm is evenredig met de omvang en aard van de activiteiten van de KMO of kleine vzw. Praktisch: een KMO met 8 personeelsleden en 10 miljoen omzet vergt geen formeel auditcomité-charter of uitgebreid risico-inschattingsproces. De auditor schaalt zijn werk maar zonder de essentie (risico-inschatting per assertion, materialiteit, gedocumenteerde aanpak) op te geven.

<small>📖 ITAA-norm-kmo-controlenorm — § 2.1.1 — _norm_</small>

### ⚙️ Cijferanalyse (ISA 520) als hoofdprocedure in review

In een review draagt de cijferanalyse veel meer gewicht dan in een audit. Typische analyses: (a) jaar-op-jaar-vergelijking per post; (b) maand-op-maand-trends en seizoens-patronen; (c) bruto-marge-evolutie per product/segment; (d) loonkost / FTE-evolutie; (e) DSO/DPO/DOH-werkkapitaal-ratio's; (f) consistentie tussen omzet (klant-cyclus) en kasontvangsten (banken). Bevindingen die buiten verwachte range vallen → opvolgvragen → eventueel aanvullende procedures (ISA 520 par. 7).

<small>📖 ISA 520 — Vereisten par. 5-7 — _norm_</small>

## Valkuilen

> [!warning]- Review = mini-audit
> **Verkeerde assumptie**: Bij een review doe ik gewoon een paar audit-procedures minder.
>
> **Kernpunt**: Review en audit zijn fundamenteel verschillend in **type bewijs**: review steunt voornamelijk op navraag + cijferanalyse; audit op substantieve detail-tests. Bovendien is de **oordeelsformulering** anders (negatief vs positief). Stakeholders die ‘met-voorbehoud-audit’ verwachten als ze een review-conclusie zien, lopen verkeerd — daarom altijd het type opdracht expliciet vermelden in opdrachtbrief en verslag.
>
> <small>📖 ITAA-norm-kmo-controlenorm — § 1.1.2 — _norm_</small>

> [!warning]- Negatief oordeel = ‘alles in orde’
> **Verkeerde assumptie**: ‘Niets is ons onder de aandacht gekomen’ betekent dat de jaarrekening getrouw is.
>
> **Kernpunt**: De formulering is bewust beperkt: het zegt alleen dat **bij de uitgevoerde procedures** geen materiële afwijkingen opvielen. Het sluit niet uit dat een diepere audit problemen had blootgelegd. De gebruiker moet beseffen dat de zekerheid lager is dan bij een audit-oordeel.
>
> <small>🔗 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

> [!warning]- Review vrijstelt onafhankelijkheid
> **Verkeerde assumptie**: Bij een KMO-review die geen wettelijke controle is, geldt minder strikte onafhankelijkheid.
>
> **Kernpunt**: Onafhankelijkheid (IESBA-code) en deontologie (ITAA) gelden voor **alle assurance-opdrachten** — review inbegrepen. Boekhouder die ook eigen werk reviewt = zelf-review-bedreiging die niet weg te safeguarden is — kan dus de review niet uitvoeren.
>
> <small>🔗 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Syntheses

### 🧩 Matrix

Vergelijking controle vs beoordeling.

| Aspect | Controle (audit) | Beoordeling (review) |
| --- | --- | --- |
| Zekerheidsniveau | Redelijk (reasonable) | Beperkt (limited) |
| Norm | ISA-stelsel + ITAA-KMO-controlenorm | ISRE 2400/2410 + ITAA-KMO-controlenorm |
| Hoofdprocedures | Substantive procedures (inspectie, externe bevestiging, herperformance) + cijferanalyse + tests of controls | Navraag + cijferanalyses (ISA 520) |
| Oordeelsvorm | Positief — ‘geven een getrouw beeld’ | Negatief — ‘niets is ons onder de aandacht gekomen’ |
| Externe bevestigingen | Standaard procedure | Niet vereist tenzij navraag/analyse problemen oplevert |
| Bijwonen voorraad-opname | Vereist (ISA 501) | Niet vereist |
| Typische tijdsinvestering | Hoog | Beduidend lager (vaak 30-50%) |
| Gebruikssituatie | Wettelijke commissaris · krediet-audit · M&A-audit | Tussentijdse rapportering · KMO zonder commissaris · omzettingsverslag |

## Accountant-perspectieven

### De accountant als review-uitvoerder

#### 🔍 Auditor

##### 👣 Concrete werkstroom KMO-review

(1) Aanvaarden: opdrachtbrief met expliciete vermelding ‘beoordelings-/reviewopdracht onder ITAA-KMO-controlenorm’; onafhankelijkheid checken. (2) Plannen: inzicht entiteit (kort als KMO bekend), risico-inschatting per assertion, materialiteit, werkprogramma op maat. (3) Procedures: management-interviews per cyclus + cijferanalyses (jaar-op-jaar, ratio's, bruto-marge per product); follow-up van uitzonderingen. (4) Afronden: clearing memo (geaccumuleerde misstatements), schriftelijke bevestiging management, beoordelingsverslag opstellen volgens ITAA-Bijlage-4-model met negatieve conclusie.

<small>📖 ITAA-norm-kmo-controlenorm — hfdst 4 + Bijlage 4 — _norm_</small>

## Verder lezen (scope-out)

- → Parent — opdracht-types-overzicht → [[opdracht-types]] _(moet-verwijzen)_
- → Gemeenschappelijke 4-fase-cyclus → [[controleopdracht]] _(moet-verwijzen)_
- → Verslag-vorm (negatieve oordeelsstijl) → [[controleverklaring]] _(moet-verwijzen)_

## Relaties

### `valt_onder`
- [[opdracht-types]]
### `vergelijkbaar_met`
- [[controleopdracht]]
    - **Gelijkenissen**:
        - Beide assurance-opdrachten over historische financiële informatie
        - Beide vergen onafhankelijkheid, opdrachtbrief, risico-georiënteerde planning
        - Beide eindigen met geschreven verslag aan gebruikers
    - **Verschillen**:
        - Zekerheidsniveau: redelijk (controle) vs beperkt (review)
        - Procedures: substantive + tests of controls (controle) vs navraag + cijferanalyses (review)
        - Oordeelsformulering: positief vs negatief
        - Tijdsinvestering: typisch 2-3x meer bij controle
    - ⚠️ **Verwarringsrisico**: Gebruikers verwarren beide types; verslag moet expliciet vermelden welk type opdracht.
### `triggert`
- [[controleverklaring]]
