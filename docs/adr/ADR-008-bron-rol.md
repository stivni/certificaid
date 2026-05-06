# ADR-008: bron_rol classificatiesysteem

**Status**: Draft  
**Datum**: 2026-05-06

## Context

Niet alle bronnen zijn gelijkwaardig. Een wettekst die studenten bij het examen kunnen raadplegen (ITAA-LEX) heeft een andere status dan een toelichting van FOD Financiën of een CBN-advies. Bij concept-extractie en retrieval moet duidelijk zijn welk gewicht een bron heeft — anders worden praktijkgidsen geciteerd als primaire rechtsbronnen.

## Beslissing

**Vijf waarden voor `bron_rol` in `source_config.yaml`:**

| Waarde | Autoriteit | Bij examen? | Gebruik |
|---|---|---|---|
| `itaa_lex` | Hoogste — wettekst | ✅ Ja | Primaire bron voor feitelijke beweringen |
| `normatief` | Hoog — wettekst buiten ITAA-LEX | ❌ Nee | Juridische grondslag, niet citeerbaar bij examen |
| `interpretatief` | Middel — CBN/ITAA-normen | ❌ Nee | Boekhoudkundige/professionele interpretatie |
| `praktijkgids` | Laag — toelichtingen, gidsen | ❌ Nee | Uitleg van HOE; niet als rechtsbron citeren |
| `formulier` | Referentie — aangifteformulieren | ❌ Nee | Code-referentie; geen conceptinhoud |

**Koppeling aan confidence-labeling** (ADR-007):
- `itaa_lex` + `interpretatief` → `confidence: grounded` bij concept-extractie
- `praktijkgids` → `confidence: inferred` tenzij expliciete wetsreferentie

**Koppeling aan RAG-retrieval**: `bron_rol` zit als metadata op elke chunk. Kan gebruikt worden als filter bij gerichte retrieval (bv. "alleen itaa_lex-bronnen voor definitievragen").

## Gevolgen

- Elke entry in `source_config.yaml` heeft een verplicht `bron_rol`-veld
- `docs/bronnen-pipeline.md` documenteert de toewijzingslogica
- ITAA-LEX.md "Andere bronnen" sectie volgt dezelfde indeling
