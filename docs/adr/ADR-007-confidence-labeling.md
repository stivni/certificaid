# ADR-007: Confidence-labeling systeem

**Status**: Draft  
**Datum**: 2026-05-06

## Context

Studenten moeten weten of een uitspraak in een fiche of tutor-antwoord direct traceerbaar is naar een wettekst, dan wel een redenering of constructie is. Een fout geciteerde wet of een onterechte "grounded" claim kan leiden tot foutieve antwoorden op het examen.

Tegelijk zijn niet alle uitspraken gelijkwaardig traceerbaar: valkuilen en praktijkvoorbeelden zijn vaak redeneringen, terwijl definities en procedures letterlijk uit de wet komen.

## Beslissing

**Twee niveaus, consequent toegepast in fiches én tutor:**

| Label | Symbool | Betekenis | Gebruik |
|---|---|---|---|
| `grounded` | ⚖️ | Direct traceerbaar naar een bron met hoge autoriteit | Definitie, artikel, verplichting uit wettekst of CBN-advies |
| `inferred` | 🤖 | Redenering, constructie of analogie zonder directe bronverwijzing | Valkuilen, praktijkvoorbeelden, competentie-heuristieken |

**Koppeling aan `bron_rol`** (zie ADR-008):
- Chunks uit `bron_rol: itaa_lex` of `interpretatief` → `confidence: grounded`
- Chunks uit `bron_rol: praktijkgids` → `confidence: inferred` tenzij expliciete wetsreferentie aanwezig

**In concept records**: elk veld (`main_rule`, `exceptions`, `pitfalls`, ...) heeft een eigen `confidence`-waarde. Het totale confidence-getal van een concept is het gewogen gemiddelde.

**In tutor-antwoorden**: elke claim wordt inline gelabeld met ⚖️ of 🤖. De student ziet direct wat geciteerd en wat geconstrueerd is.

## Gevolgen

- Valkuilen en voorbeeldvragen mogen 🤖 bevatten — dat is expliciet toegestaan en verwacht
- Een materie-sectie zonder bronverwijzing is altijd ⚠️ te verifiëren, nooit stilzwijgend grounded
- Tutor-systeem prompt verplicht labeling; Claude mag niet weglaten bij twijfel
