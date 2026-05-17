# Concept-extractie PO 1.9 — eindrapport

**Programmaonderdeel**: 1.9 Financiële analyse (bekwaamheid)
**Run**: `concept-extractie-v4-2026-05-17T10:00Z`
**Model**: claude-opus-4-7 (subagent)
**Schema**: 1.4
**Budget**: ~1.5u (kleiner dan andere PO's wegens groot hergebruik PO 1.3)

---

## Strategy — cross-PO uitbreiding

PO 1.9 behandelt hetzelfde onderwerp als PO 1.3 (analyse jaarrekening) maar op bekwaamheid-niveau. PO 1.3 heeft al 33 records in `data/concepten/records/`. De strategie was:

1. **Fase A**: bestaande PO 1.3-records uitbreiden met PO 1.9-anchors in `linked_anchors[]` — geen content-wijzigingen.
2. **Fase B**: enkel nieuwe records aanmaken voor concepten die in PO 1.9 dieper of nieuw zijn (faillissement-modellen, IT-tools, kasstroom-segmenten, BBK, financieringsbronnen-in-cashflow-context, RR-herwerking, TW, falen-fenomeen, ratio-interpretatie).

**Anti-collision**: geen enkel record dat al voor PO 1.3 bestond, werd overschreven. Alleen `linked_anchors[]` werd uitgebreid.

---

## Totaal

- **13 nieuwe concept-records** in `data/concepten/records/`
- **25 bestaande records uitgebreid** met PO 1.9-anchors
- **38 records totaal** linked aan PO 1.9 (25 + 13)
- **1 synthese-record** (`kwantitatieve-financiele-diagnose`) — kasstroom-overzicht-segmenten ook synthese
- **0 records overschreven** (anti-collision OK)

---

## Fase A — Uitgebreide bestaande PO 1.3-records (25)

| Record | Toegevoegde 1.9-anchor(s) | Rationale |
|---|---|---|
| `analytische-balans` | 1.9.II, 1.9.III, 1.9.III.A, 1.9.taak.1 | Herstructurering balans = kern 1.9.III.A |
| `bestuursverslag` | 1.9.I | Inleiding/context (toelating) |
| `cashflow-analyse` | 1.9.IV, 1.9.IV.C, 1.9.IV.G, 1.9.IV.H, 1.9.taak.1 | Cashflow + kasstroom-context |
| `cijferanalyses-controle-norm` | 1.9.V.E, 1.9.VI.A | Interpretatie ratio's + diagnose |
| `current-ratio` | 1.9.V.D, 1.9.taak.1 | Liquiditeit |
| `debt-equity-ratio` | 1.9.V.C, 1.9.taak.1 | Solvabiliteit |
| `doelstellingen-financiele-analyse` | 1.9.I, 1.9.taak.1 | Inleiding |
| `gebruikers-jaarrekening` | 1.9.I | Inleiding |
| `getrouw-beeld-jaarrekening` | 1.9.I, 1.9.II | Algemeen kader |
| `historische-evolutie-financiele-analyse` | 1.9.III.D, 1.9.V.E | Horizontale + interpretatie |
| `horizontale-analyse-jaarrekening` | 1.9.III, 1.9.III.D, 1.9.taak.1 | Direct 1.9.III.D |
| `intake-financiele-analyse` | 1.9.I | Toelating-context |
| `jaarrekening-als-studieobject` | 1.9.II, 1.9.taak.1 | Individuele jaarrekening + balansaggregaten |
| `liquiditeitsratio` | 1.9.V, 1.9.V.D, 1.9.V.E, 1.9.taak.1 | Liquiditeit |
| `liquiditeitstoets-beslisboom` | 1.9.V.D, 1.9.V.E | Beslisboom liquiditeit |
| `quick-ratio` | 1.9.V.D | Liquiditeit |
| `ratio-covenants` | 1.9.V.E | Interpretatie |
| `ratio-vier-doelen-vergelijking` | 1.9.V, 1.9.V.E | Synthese ratio's |
| `rentabiliteit-eigen-vermogen-roe` | 1.9.V, 1.9.V.B, 1.9.taak.1 | Rentabiliteit |
| `rentabiliteit-totaal-activa-roa` | 1.9.V, 1.9.V.B, 1.9.taak.1 | Rentabiliteit |
| `risicoparagraaf-bestuursverslag` | 1.9.VI.A | Falen-indicatoren |
| `sectorvergelijking-financiele-analyse` | 1.9.III.E, 1.9.V.E | Verticale + interpretatie |
| `solvabiliteitsratio` | 1.9.V, 1.9.V.C, 1.9.taak.1 | Solvabiliteit |
| `verticale-analyse-jaarrekening` | 1.9.III, 1.9.III.E, 1.9.taak.1 | Verticale = 1.9.III.E |
| `werkkapitaal` | 1.9.IV.D, 1.9.V.D | Bedrijfskapitaal-behoefte |

**Niet uitgebreid** (irrelevant voor 1.9 — toezicht / structuur / specifieke 1.2-context):
`algemene-vergadering-toezichtsfunctie`, `commissaris-toezicht-jaarrekening`, `corporate-governance-verklaring`, `kamer-ondernemingen-in-moeilijkheden`, `klasse-0-niet-in-balans`, `materieel-belang-jaarrekening`, `niet-in-balans-opgenomen-rechten-verplichtingen`, `ondernemingsraad-sociaal-economische-info`.

---

## Fase B — Nieuwe records (13)

| Slug | node_type | Primair anchor | Rationale | Confidence |
|---|---|---|---|---|
| `toegevoegde-waarde-financiele-analyse` | methode | 1.9.V.A | Toegevoegde waarde als economische maatstaf — niet in PO 1.3 | inferred-common-knowledge |
| `tabel-waardemutaties` | methode | 1.9.IV.B | Mutatietabel vaste activa (NBB) | grounded |
| `kasstroomoverzicht-drie-segmenten` | synthese | 1.9.IV.G | CFO+CFI+CFF — anders dan single cashflow-bedrag | inferred-common-knowledge |
| `behoefte-aan-bedrijfskapitaal` | begrip | 1.9.IV.D | BBK — geen PO 1.3-record | inferred-common-knowledge |
| `financiering-met-eigen-vermogen` | begrip | 1.9.IV.F | EV als financieringsbron | grounded |
| `financiering-met-derdenkapitaal` | begrip | 1.9.IV.E | VV als financieringsbron | grounded |
| `altman-z-score` | methode | 1.9.VI.B | Faillissement-predictie | inferred-common-knowledge |
| `ohlson-o-score` | methode | 1.9.VI.B | Logit-model | inferred-common-knowledge |
| `kwantitatieve-financiele-diagnose` | synthese | 1.9.VI | Modellen-overzicht | inferred-common-knowledge |
| `falen-van-de-onderneming` | fenomeen | 1.9.VI.A | Distress-fenomeen (drie stadia) | inferred-common-knowledge |
| `financiele-analyse-software` | begrip | 1.9.VII.A | IT-tools (Bel-First, NBB-Online, Graydon, Belfius Score) | inferred |
| `interpretatie-financiele-ratios` | methode | 1.9.V.E | Bekwaamheid-niveau ratio-lezing | inferred-common-knowledge |
| `herstructurering-resultatenrekening` | methode | 1.9.III.B | RR-herwerking volledig + verkort + micro | grounded |

---

## Per-anchor mapping (volledig overzicht — 31 anchors)

| Anchor | Records (primair of secundair gelinkt) |
|---|---|
| **1.9.taak.1** | `cashflow-analyse`, `analytische-balans`, `horizontale-analyse-jaarrekening`, `verticale-analyse-jaarrekening`, `current-ratio`, `debt-equity-ratio`, `liquiditeitsratio`, `solvabiliteitsratio`, `rentabiliteit-eigen-vermogen-roe`, `rentabiliteit-totaal-activa-roa`, `jaarrekening-als-studieobject`, `doelstellingen-financiele-analyse`, `toegevoegde-waarde-financiele-analyse`, `behoefte-aan-bedrijfskapitaal`, `kasstroomoverzicht-drie-segmenten`, `interpretatie-financiele-ratios` |
| **1.9.I** | `bestuursverslag`, `doelstellingen-financiele-analyse`, `gebruikers-jaarrekening`, `getrouw-beeld-jaarrekening`, `intake-financiele-analyse` |
| **1.9.II** | `analytische-balans`, `getrouw-beeld-jaarrekening`, `jaarrekening-als-studieobject` |
| **1.9.III** | `analytische-balans`, `horizontale-analyse-jaarrekening`, `verticale-analyse-jaarrekening`, `herstructurering-resultatenrekening` |
| **1.9.III.A** | `analytische-balans` |
| **1.9.III.B** | `herstructurering-resultatenrekening` |
| **1.9.III.C** | `herstructurering-resultatenrekening` |
| **1.9.III.D** | `horizontale-analyse-jaarrekening`, `historische-evolutie-financiele-analyse` |
| **1.9.III.E** | `verticale-analyse-jaarrekening`, `sectorvergelijking-financiele-analyse` |
| **1.9.IV** | `cashflow-analyse`, `behoefte-aan-bedrijfskapitaal`, `kasstroomoverzicht-drie-segmenten`, `financiering-met-eigen-vermogen`, `financiering-met-derdenkapitaal`, `tabel-waardemutaties` |
| **1.9.IV.A** | (overkoepelend — gedekt door [[cashflow-analyse]] + [[behoefte-aan-bedrijfskapitaal]]) ⚠️ geen specifiek record |
| **1.9.IV.B** | `tabel-waardemutaties` |
| **1.9.IV.C** | `cashflow-analyse` |
| **1.9.IV.D** | `behoefte-aan-bedrijfskapitaal`, `werkkapitaal` |
| **1.9.IV.E** | `financiering-met-derdenkapitaal` |
| **1.9.IV.F** | `financiering-met-eigen-vermogen` |
| **1.9.IV.G** | `cashflow-analyse`, `kasstroomoverzicht-drie-segmenten` |
| **1.9.IV.H** | `cashflow-analyse`, `kasstroomoverzicht-drie-segmenten` |
| **1.9.V** | `liquiditeitsratio`, `solvabiliteitsratio`, `rentabiliteit-eigen-vermogen-roe`, `rentabiliteit-totaal-activa-roa`, `ratio-vier-doelen-vergelijking`, `interpretatie-financiele-ratios` |
| **1.9.V.A** | `toegevoegde-waarde-financiele-analyse` |
| **1.9.V.B** | `rentabiliteit-eigen-vermogen-roe`, `rentabiliteit-totaal-activa-roa` |
| **1.9.V.C** | `solvabiliteitsratio`, `debt-equity-ratio` |
| **1.9.V.D** | `liquiditeitsratio`, `current-ratio`, `quick-ratio`, `werkkapitaal`, `liquiditeitstoets-beslisboom` |
| **1.9.V.E** | `interpretatie-financiele-ratios`, `liquiditeitsratio`, `ratio-vier-doelen-vergelijking`, `ratio-covenants`, `historische-evolutie-financiele-analyse`, `sectorvergelijking-financiele-analyse`, `cijferanalyses-controle-norm`, `liquiditeitstoets-beslisboom` |
| **1.9.VI** | `kwantitatieve-financiele-diagnose`, `falen-van-de-onderneming` |
| **1.9.VI.A** | `falen-van-de-onderneming`, `risicoparagraaf-bestuursverslag`, `cijferanalyses-controle-norm` |
| **1.9.VI.B** | `altman-z-score`, `ohlson-o-score`, `kwantitatieve-financiele-diagnose` |
| **1.9.VII** | `financiele-analyse-software` |
| **1.9.VII.A** | `financiele-analyse-software` |
| **1.9.VII.B** | `financiele-analyse-software` |
| **1.9.VII.C** | `financiele-analyse-software` |

**Niet expliciet gedekt**: 1.9.IV.A (overkoepelend "kasstroom en bedrijfscyclus" — gedekt door [[cashflow-analyse]] + [[behoefte-aan-bedrijfskapitaal]] + [[kasstroomoverzicht-drie-segmenten]] samen, maar geen apart bedrijfscyclus-record. Mogelijk later als gap-analyse blijkt dat een aparte bedrijfscyclus-fiche zin heeft).

---

## Cross-PO overlap-analyse PO 1.3 ↔ PO 1.9

### Wat blijft hetzelfde (gedeeld tussen 1.3 en 1.9)
- Alle ratio-records (`current-ratio`, `quick-ratio`, `solvabiliteitsratio`, ...): definitie + formule blijven identiek; alleen `linked_anchors[]` uitgebreid.
- Herstructurering balans (`analytische-balans`), horizontale/verticale analyse: dezelfde methode op beide niveaus.
- Concepten rond bestuursverslag, getrouw beeld, gebruikers: identiek.

### Wat PO 1.9 specifiek toevoegt boven 1.3
- **Toegevoegde waarde** (productiviteit-doel) — niet in PO 1.3
- **Behoefte aan bedrijfskapitaal (BBK)** — diepere kasstroom-anker dan PO 1.3 levert
- **Kasstroomoverzicht-drie-segmenten** — 1.3 had alleen cashflow-bedrag
- **Mutatietabel vaste activa** — 1.3 toetste dit niet
- **Financieringsbronnen-context** (EV vs VV) — 1.3 had dit niet als afzonderlijke onderwerpen
- **Falen-van-de-onderneming + Altman + Ohlson** — PO 1.9-exclusief (bekwaamheid-VI.A/VI.B)
- **IT-tools (financiele-analyse-software)** — PO 1.9-exclusief (VII)
- **Interpretatie-bekwaamheid-laag** — meta-skill om ratio's te lezen, niet alleen berekenen
- **RR-herwerking (volledig + verkort + micro)** — 1.3 dekte alleen balans-herwerking expliciet

### Wat van PO 1.3 NIET relevant is voor 1.9
- Toezichtsorganen (commissaris, algemene vergadering): PO 1.3.I.D-context.
- Bestuursverslag-deelaspecten (corporate-governance, materieel belang): vooral PO 1.3-context (wettelijke verplichting).
- Klasse 0 niet-in-balans: PO 1.3.II.D-context.

---

## Voorbeeld-discipline (Regel 14a + Regel 7)

Alle voorbeelden gebruiken:
- Cast-naam: **Rotex Roeselare NV** (hoofd) + waar relevant **Verffabriek Veurne BV** (distress-case) + **Meubelzaak Mertens BV** (verkort schema).
- Bedragen in €-format met duizendtal-punt: `€ 50.000.000`, `€ 12.000.000`, etc.
- Plausibel voor een grote NV: balanstotaal € 30M, omzet € 50M, EV € 12M, VV € 18M.
- Geen abstracte getallen.

---

## Claims `inferred-common-knowledge` — concentratie

Voor PO 1.9 was bron-gap groter dan PO 1.4 omdat:
- Faillissement-modellen (Altman 1968, Ohlson 1980) zijn internationale vakdoctrine zonder Belgische wettekst-basis.
- BBK en kasstroom-segmenten zijn analytische conventies; KB WVV-schema's leveren niet de structuur direct.
- IT-tools zijn commerciële markt-realiteit zonder normatieve bron.

Dit is **bewust** geaccepteerd: het PO 1.9-examen toetst conceptueel begrip van deze vakdoctrine; bronvermelding tot het origineel werk (Altman 1968, Ohlson 1980) + verwijzing naar Belgische vakliteratuur volstaat.

---

## Open observaties / follow-up

1. **1.9.IV.A "Kasstroom en bedrijfscyclus"** — geen apart record gemaakt; lijkt overkoepelend voor IV.B-IV.H. Als follow-up: overweeg een synthese-record `kasstroom-bedrijfscyclus-overzicht` dat de exploitatiecyclus visueel met cash-conversion-cycle in beeld brengt.
2. **Belgische faillissement-modellen** — Score Belfius / Graydon Multiscore zijn in `financiele-analyse-software` gemeld maar niet als aparte methode-records. Reden: propriëtair, geen publieke formule. Voor examen niet kritisch.
3. **PO 1.9.VII.C "Interpreteren van de gegevens"** — gedekt door `interpretatie-financiele-ratios` én `financiele-analyse-software` (twee perspectieven: tool-output-interpretatie + algemene ratio-interpretatie). Geen aparte record.
4. **Toegevoegde waarde-record** raakt mogelijk ook PO 1.7 (analytische boekhouding). Vergelijking met PO 1.7-records bij hun extractie aanbevolen.
5. **`bron_gap` consistent gelogd** in `_provenance` van nieuwe records — zoekvraag voor latere bronnenophalingsronde (vakliteratuur Ooghe-Van Wymeersch, Vereeck, ...).

---

## Anti-collision check

Verificatie van alle 13 nieuwe slugs vs bestaande records: geen dubbels (alle nieuwe slugs zijn uniek; bestaande records werden NIET overschreven).

```
13 nieuwe slugs:
  toegevoegde-waarde-financiele-analyse    # nieuw
  tabel-waardemutaties                     # nieuw
  kasstroomoverzicht-drie-segmenten        # nieuw (verschilt van bestaand cashflow-analyse)
  behoefte-aan-bedrijfskapitaal            # nieuw (verschilt van bestaand werkkapitaal)
  financiering-met-eigen-vermogen          # nieuw
  financiering-met-derdenkapitaal          # nieuw
  altman-z-score                           # nieuw
  ohlson-o-score                           # nieuw
  kwantitatieve-financiele-diagnose        # nieuw
  falen-van-de-onderneming                 # nieuw
  financiele-analyse-software              # nieuw
  interpretatie-financiele-ratios          # nieuw
  herstructurering-resultatenrekening      # nieuw (verschilt van analytische-balans)
```

---

## Cast — gebruikte rolverdeling

| Rol | Cast-naam | Gebruikt in records |
|---|---|---|
| Grote NV volledig schema | **Rotex Roeselare NV** | Alle 13 nieuwe records — hoofdvoorbeeld |
| BV in vereffening / distress | **Verffabriek Veurne BV** | `falen-van-de-onderneming`, `altman-z-score`, `ohlson-o-score` |
| Kleine BV verkort schema | **Meubelzaak Mertens BV** | `herstructurering-resultatenrekening` |
| Beursgenoteerde NV (IFRS) | **Zelena Bio NV** | `kasstroomoverzicht-drie-segmenten` (IFRS-context) |
