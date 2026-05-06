# ADR-006: Drie-lagenmodel voor studiemateriaal

**Status**: Draft  
**Datum**: 2026-05-06

## Context

Het ITAA-bekwaamheidsexamen toetst bekwaamheid — het vermogen om technieken correct toe te passen in onbekende situaties. Dat vereist drie soorten kennis die elk een eigen type content vragen: weten wat iets is, kunnen toepassen hoe het werkt, en integreren over meerdere domeinen heen.

Een enkele "notitie per onderwerp" dekt dit niet: een definitie is geen procedure, en een procedure is geen integratieoefening. Ze moeten expliciet gescheiden worden zodat elk type inhoud op de juiste manier bestudeerd en bevraagd kan worden.

## Beslissing

**Drie lagen, elk met een eigen content-type en canonieke locatie:**

| Laag | Vraag | Locatie | Bron van waarheid |
|---|---|---|---|
| **Materie** | Wat is X? Hoe werkt X? | `content/materie/` | Wetteksten, CBN-adviezen |
| **Competentie** | Hoe pak ik dit type taak aan? | `content/competenties/` | ITAA-normen, CBN, beroepspraktijk |
| **Synthese** | Hoe combineer ik competenties? | Voorbeeldvragen bij PO-fiches | Voorbeeldexamens |

**Canonieke thuisplaats**: elk stuk inhoud heeft één vaste plek — nooit in beide lagen tegelijk. Een competentie citeert materie kort als context maar herhaalt ze nooit volledig.

**Concept = fenomeen**, niet een juridische structuur of vakindeling. Een concept dat in meerdere vakken voorkomt, krijgt één fiche die alle contexten dekt.

## Gevolgen

- Nieuwe content vraagt altijd om een expliciete laag-keuze vóór het schrijven
- Links tussen lagen zijn verplicht (materie ↔ competentie, competentie ↔ PO-fiche)
- Duplicatie is een signaal dat de canonieke thuisplaats niet gevonden is
- CLAUDE.md is de gezaghebbende bron voor de regels per laag
