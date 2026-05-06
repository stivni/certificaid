# ADR-014: Twee werkwijze-modi — design/sparring vs. werk

**Status**: Draft  
**Datum**: 2026-05-06

## Context

Zonder expliciete afbakening ontstaat verwarring over wanneer Claude zelfstandig beslissingen neemt en wanneer er eerst een gesprek plaatsvindt. Bij uitvoerende taken (indexeren, fiches schrijven) is autonomie gewenst; bij architectuurkeuzes is het risico van stille aannames te groot — die kunnen later moeilijk te corrigeren zijn zonder regressies.

## Beslissing

**Twee expliciete modi, altijd bewust van welke actief is:**

### Design/sparring-modus

Actief wanneer: een beslissing nog open is, trade-offs afgewogen moeten worden, of een architectuurkeuze raakvlakken heeft met meerdere onderdelen.

Regels:
- Claude vraagt vóór het implementeren — ook als de richting al duidelijk lijkt
- Discussie verloopt iteratief: voorstel → feedback → bijsturing
- Het resultaat **moet** landen in een nieuw of bijgewerkt ADR vóór de uitvoering start
- Planmode is het vanzelfsprekende instrument voor deze modus

### Werk-modus

Actief wanneer: de aanpak bepaald is via bestaande ADRs en de taak uitvoerend van aard is (indexeren, fiches schrijven, bronnen verwerken, scripts draaien).

Regels:
- Claude werkt zelfstandig en minimiseert onnodige validatievragen
- Werkt altijd binnen de spelregels van de bestaande ADRs
- Bij twijfel of een keuze buiten de scope van bestaande ADRs valt: schakel terug naar design-modus vóór je verdergaat
- Kleine implementatiekeuzes (variabelenamen, volgorde van stappen) vallen onder werk-modus

## Grens tussen de modi

| Werk-modus (autonoom OK) | Design-modus (eerst bespreken) |
|---|---|
| Index herbouwen | Ander embedding model kiezen |
| Fiche schrijven conform content-richtlijnen | Nieuw ficheformat introduceren |
| Bron toevoegen conform bronnen-pipeline | Nieuw bron_rol-type toevoegen |
| Bug fixen in bestaande code | Architectuur van een script herontwerpen |
| Bestaande ADR uitvoeren | Bestaande ADR aanpassen of tegenspreken |

## Gevolgen

- Claude kondigt expliciet aan welke modus actief is bij het begin van een complexe taak
- Bij onverwachte situaties tijdens werk-modus: pauzeren en de gebruiker informeren vóór verder te gaan
- ADR-INDEX bevat de TODO-checklist voor de bevestigingsronde — die ronde is een design-modus activiteit
