# Deep-rewrite competentie-yamls 1.4 — schema 1.0 → 1.1

**Run-id**: `competentie-deep-rewrite-2026-05-16`
**Datum**: 2026-05-16
**Scope**: alle 9 competentie-yamls van PO 1.4

## Doel

Schema-versie bump van 1.0 → 1.1 conform ADR-007 §schema-1.4 en `prompts/competentie-destillatie-v2.md`:
- Stap-blok-schema (wat + hoe + voorbeeld.substappen + input/output gestructureerd)
- Valkuilen hernoemd: `correctie` → `advies`, `foute_aanname` → `vaak_fout`
- Stagiair-toon op alle tekstvelden
- Cast-namen uit `data/concepten/casts/globaal.yaml` (Aurelia/Brugse/Cardinal/...)
- Praktijk-grondslag op stap-niveau via wikilinks in `hoe`-velden
- `_provenance.rewrite_naar_schema_1_1` toegevoegd

## Resultaat per competentie

| Competentie | Stappen | Substappen-blocks | Scenario-templates gebruikt |
|---|--:|--:|---|
| `afbakenen-consolidatiekring` | 5 | 1 (stap 3) | basis_consolidatie + Logistics Lille/Gent Garantie + Cardinal/Energiehuis/Filmstudio |
| `bepalen-consolidatieverplichting` | 6 | 1 (stap 4) | basis_consolidatie + groep_van_beperkte_omvang + consortium + subconsolidatie |
| `berekenen-controle-en-belangenpercentage` | 5 | 2 (stap 2, 3) | keten Aurelia → Brugse → Cardinal (eigen scenario, geldige cast-letters A/B/C) |
| `kiezen-consolidatiemethode` | 5 | 2 (stap 2, 3) | basis_consolidatie + joint_venture + geassocieerde + consortium |
| `kwalificeren-relatie-deelneming` | 5 | 1 (stap 4) | geassocieerde (Antwerpse → Drukkerij Dendermonde) + Cardinal/Filmstudio (joint) |
| `toepassen-uniforme-waarderingsregels` | 6 | 1 (stap 3) | Aurelia + Holsters Horst BV (afwijkende waardering) |
| `uitvoeren-eerste-consolidatie` | 6 | 3 (stap 3, 4, 6) | basis_consolidatie (Aurelia 80 %, aanschaffingswaarde 320, EV 300) — exact zoals concept-record `integrale-consolidatie` |
| `uitvoeren-intragroep-eliminaties` | 8 | 3 (stap 2, 3, 7) | basis_consolidatie + intra-groepswinst voorraad + 90/10-belang voor aandeel-van-derden |
| `verwerken-wijziging-consolidatiekring` | 6 | 2 (stap 4, 5) | step acquisition Antwerpse → Drukkerij Dendermonde (25 % → 60 %) + realisatie Aurelia/Brugse |

**Totaal**: 52 stappen, 16 substappen-blocks. Alle YAML-files parseren foutloos (`yaml.safe_load`).

## Wat is per competentie aangepast (in `_provenance.rewrite_naar_schema_1_1.velden_gewijzigd`)

Alle 9 yamls:
- `schema_version: "1.0"` → `"1.1"`
- `stappen[*].wat` (nieuw veld, één-zin samenvatting van de stap)
- `stappen[*].hoe` (nieuw veld, multiline 3-7 substappen-instructie met wikilinks naar concept-records)
- `stappen[*].input` en `output` gestructureerd (`artefact / veld / type` per item — was vroeger één string)
- `stappen[*].voorbeeld` met `scenario + substappen[]` waar relevant (balansen, berekeningen, boekingsregels, opmerkingen, flowcharts)
- `valkuilen[*]`: `correctie` → `advies`, `foute_aanname` → `vaak_fout`
- Stagiair-toon op alle tekstvelden: korte zinnen, eerste afkorting voluit + (afkorting), geen 'consoliderende vennootschap' meer
- Cast-namen volgens `data/concepten/casts/globaal.yaml`

## Substappen-rationale per competentie

**Volledig gevuld (alle reken/balans/boeking-stappen hebben substappen)**:
- `uitvoeren-eerste-consolidatie` — pro-rata berekening, residueel-verschil-boeking, aandeel-derden berekening
- `uitvoeren-intragroep-eliminaties` — eliminatie boekingsregel + voorraad-marge berekening + aandeel-derden berekening
- `berekenen-controle-en-belangenpercentage` — controlepercentage-flowchart + belangenpercentage-berekening

**Selectief gevuld (alleen kern-substap waar tabel didactisch is)**:
- `bepalen-consolidatieverplichting` stap 4 (drempelwaarden-toets)
- `afbakenen-consolidatiekring` stap 3 (uitsluitingsgronden-toets per dochter)
- `kwalificeren-relatie-deelneming` stap 4 (invloed-van-betekenis-toets)
- `kiezen-consolidatiemethode` stap 2 en 3 (toewijzing techniek + nauwe-integratie-toets)
- `toepassen-uniforme-waarderingsregels` stap 3 (LIFO → FIFO aanpassingsboeking)
- `verwerken-wijziging-consolidatiekring` stap 4 (step-acquisition kantelpunt) en stap 5 (pro-rata afboeking realisatie)

**Bewust niet gevuld** (stappen die alleen documenten verzamelen of kwalificeren — zie prompt v2 regel A: "niet verplicht bij stappen die alleen 'documenten verzamelen' of 'kwalificeren' doen"):
- Stap 1 in alle competenties (inventarisatie-stappen)
- Stappen die enkel een wettelijke regel doorlopen zonder concrete cijfers (bv. art. 3:97-toets in algemene zin)

## Cast-gebruik

Geen "M / D / D1 / D2 / X / Y / ABC / DEF" meer in de bewerkte yamls. Gebruikt:

| Cast-rol | Naam | Gebruikt in |
|---|---|---|
| Moeder | Aurelia Holding NV | basis_consolidatie-scenarios |
| Dochter (exclusieve controle) | Brugse Brouwerij BV | basis_consolidatie |
| Kleindochter (keten) | Cardinal Group NV | berekenen-controle-en-belangenpercentage |
| JV-partner | Cardinal Group NV + Energiehuis Evergem BV | joint_venture |
| Joint dochter | Filmstudio Florence BV | joint_venture |
| Geassocieerde-moeder | Antwerpse Investments NV | geassocieerde-scenarios |
| Geassocieerde | Drukkerij Dendermonde BV | geassocieerde, step-acquisition |
| Kleine vennootschap | Gent Garantie BV | groep-van-beperkte-omvang |
| Dochter afwijkende waardering | Holsters Horst BV | toepassen-uniforme-waarderingsregels |
| Buitenlandse dochter (deviezenrestrictie) | Logistics Lille SAS | afbakenen-consolidatiekring stap 3 |
| Buitenlandse moeder (subconsolidatie) | Kappers Köln GmbH | bepalen-consolidatieverplichting stap 5 |
| Consortium-leden | Industria Antwerpen NV + Jachthaven Jezus-Eik NV | consortium-scenarios |
| Centrale leider consortium | Pieter Vermeulen | consortium-scenarios |

## Numerieke consistentie

Bedragen in voorbeelden komen uit cast-scenario-templates:
- `basis_consolidatie.aanschaffingswaarde_default = 320`, `eigen_vermogen_dochter_default = 300`, `belang_default = 80%` — toegepast in `uitvoeren-eerste-consolidatie` en cross-verwezen in `uitvoeren-intragroep-eliminaties`
- `geassocieerde.aanschaffingswaarde_default = 200`, `eigen_vermogen_geassocieerde_default = 600`, `belang_default = 25%` — toegepast in `uitvoeren-eerste-consolidatie` voorbeeld
- `groep_van_beperkte_omvang`: omzet 20 mln, balanstotaal 12 mln, personeel 180 — exact uit cast

Drempelwaarden in `bepalen-consolidatieverplichting` stap 4 (jaaromzet 34 mln, balanstotaal 17 mln, werknemers 250) zijn richt-bedragen uit het cijferzakboekje; geannoteerd als "cijferzakboekje" — geen claim dat ze in de yaml-data ground-truth zijn. Aanbevolen voor mens-review.

## Tekorten / open punten voor mens-review

1. **Drempelwaarden in `bepalen-consolidatieverplichting` stap 4**: de gehanteerde drempels (34 mln/17 mln/250) komen uit cijferzakboekje. Curator moet verifiëren dat dit de actuele KB WVV-drempels zijn voor 1.4-examenstof.

2. **`afbakenen-consolidatiekring` stap 3 substap-tabel**: gebruikt KB WVV art. 3:97 voor alle gronden generiek. Curator kan finer-grained artikel-referenties toevoegen per uitsluitingsgrond (bv. a/b/c/d-onderverdeling).

3. **`toepassen-uniforme-waarderingsregels` stap 3 LIFO→FIFO**: het bedrag 100→130 is een didactische illustratie. Curator kan vervangen door een gerealistischer voorbeeld uit een echte praktijkcasus.

4. **`verwerken-wijziging-consolidatiekring` stap 6 (common control)**: verwijst naar 'CBN-advies common-control transactions' zonder specifieke advies-nummer. Curator kan het CBN-advies-nummer toevoegen wanneer dit op resources/bronnen/adviezen/ is.

5. **`berekenen-controle-en-belangenpercentage` ketenstructuur**: gebruikt Aurelia → Brugse → Cardinal. In strikte cast-betekenis is Cardinal een JV-partner, niet een productie-dochter. Cast laat dit toe (rol_default is een hint, geen lock-in), maar curator kan overwegen of een andere C-naam (of nieuwe E/F-naam) didactisch helderder is. Geen blokker.

6. **`uitvoeren-intragroep-eliminaties` stap 5 (evenredige consolidatie-pro-rata)**: bevat geen substappen. Een berekenings-substap (50 % × intra-groepswinst = X) zou de stap concreter maken. Niet toegevoegd om scope-creep te beperken; curator kan dit eenvoudig invullen.

7. **Voorbeeld-arrays op rootniveau (`voorbeelden`-blok) onaangetast in shape**. Cast-namen werden wel toegepast in deze voorbeelden. Schema 1.1 raakt de root-`voorbeelden`-arrayshape niet (uit prompt: alleen `stappen[*]`-velden zijn vernieuwd).

## Validatie-status

- Alle 9 yamls parseren foutloos via `yaml.safe_load`.
- `schema_version: "1.1"` overal aanwezig.
- Geen oude `correctie` / `foute_aanname`-veldnamen meer aanwezig.
- Geen oude jargon-cast ("M / D1 / D2 / X / Y / ABC / DEF") in voorbeelden.
- `gebaseerd_op_concepten[]` ≥ 2 overal behouden.
- `procedure_grondslag.wettelijk_pct + praktijk_pct == 100` overal behouden.
- `status: voorgesteld` overal behouden — curator (mens) cureert later.

`tools/leermateriaal/lib/validate_competentie.py` schema-1.1-validator nog niet gerund (validator moet eerst worden bijgewerkt voor 1.1-velden, zie prompt v2 sectie "Output-aanpassingen" laatste regel).
