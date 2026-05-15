# ADR-002: Examenprogramma als scoping-anker

**Status**: Draft
**Datum**: 2026-05-07

## Context

Het ITAA-examenprogramma definieert per programmaonderdeel een lijst **taken**, **doelstellingen** en **kenniselementen** — eindtermen die de stagiair moet kunnen demonstreren. Dat is de enige externe definitie van wat getoetst kan worden. Zonder zo'n anker blijven vragen als "is mijn conceptenset volledig?" en "welke concepten zijn examen-relevant?" subjectief.

Eerdere iteraties gebruikten *vakken* als organisatie-eenheid voor leerstof. Dat is onjuist: vakken zijn een examen-organisatielaag, geen kennislaag. Concepten kunnen vakoverschrijdend zijn (antiwitwaswetgeving komt voor in deontologie én in fiscaliteit). Een concept-per-vak-organisatie produceert duplicatie.

## Beslissing

**Het examenprogramma is de externe scope-definitie.** Concepten worden geëxtraheerd om kenniselementen af te dekken; vakindeling speelt alleen mee in de output-laag van de programmaonderdeel-fiches.

1. **Het examenprogramma wordt expliciet ingelezen** als gestructureerde data — één globaal bestand `data/programma/programma.json` (sinds 2026-05-10; was per-PO in `data/programmaonderdelen/`), met taken, doelstellingen en kenniselementen elk gecodeerd. Provenance-getagd zoals elk ander artefact (ADR-004).

2. **Eenrichtings-koppeling: programmaonderdeel-JSON kent concepten, concept-records weten van niets**:

   ```json
   // data/programma/programma.json (één globaal bestand, sinds 2026-05-10) — ENIGE WAARHEID
   "kenniselementen": [
     {"deel": 1, "code": "4.0.I.D.7", "tekst": "Beroepsgeheim",
      "concepten": ["beroepsgeheim-gecertificeerd-accountant", "doorbreking-beroepsgeheim"]}
   ]
   ```

   Concept-records bevatten **geen** veld `afdekt_kenniselementen` of vergelijkbaar. De concept-laag heeft geen kennis van het examenprogramma. Dezelfde regel geldt voor de examen-laag: examenvraag-records mogen `vereiste_concepten` lijsten dragen, maar concept-records weten nooit dat een examenvraag naar hen verwijst.

   **Waarom**: dependencies stromen één kant op (programma → concepten, examen → concepten). Concepten worden zo portable — bij hervorming van het examenprogramma (codes herschikt) raakt de conceptenset niet. Een concept is een tijdloos fenomeen, geen taxonomie-entry van een specifieke programma-versie.

   Eén concept kan meerdere kenniselementen afdekken; één kenniselement kan meerdere concepten vragen. Hetzelfde patroon geldt voor taken/doelstellingen die `concepten`-lijsten kunnen dragen (procedure/skill-concepten zijn vaak gekoppeld aan een taak, niet aan een kenniselement).

3. **Dekkingscheck** is een eerste-orde regressietest, gelezen uit programmaonderdeel-JSON:
   - Voor elk kenniselement (en elke taak/doelstelling): minstens één concept-id in de `concepten`-lijst
   - Voor elk kenniselement: minstens één voorbeeldvraag of examenpatroon dat hem toetst
   - Gat-rapport stuurt nieuwe extractie-rondes (ADR-008)

   Wie "welke kenniselementen dekt concept X af?" wil weten: bouwt een **in-memory reverse-index** bij build (één pass over programmaonderdeel-JSON's). Geen state op concepten zelf nodig.

4. **Anti-circulariteit**: het examenprogramma stuurt *welke* concepten nodig zijn, niet *wat* een concept inhoudt. Concept-inhoud komt uit bronnen, niet uit de tekst van het examenprogramma zelf. Examenvraag-tekst kan via chunk-provenance wel als bron-input dienen voor een concept (een passage uit een Mvt of een toelichting op een voorbeeldexamen kan geciteerd worden) — maar dat is een **chunk-id** in `_provenance.inputs`, niet een examenvraag-link in concept-velden zelf.

## Gevolgen

- Nieuwe of gewijzigde kenniselementen in het examenprogramma → programmaonderdeel-JSON wijzigt; concept-records onaangeraakt. Stale-marking gebeurt via bron-chunk-input-veranderingen (ADR-004), niet via programma-wijzigingen.
- Programmaonderdelen leven in `data/programma/programma.json` (één globaal bestand), versie-getagd. Schema breidt uit met `concepten`-lijst per kenniselement (en optioneel per taak/doelstelling).
- Geen sync-tooling nodig — koppeling is eenrichting, geen cache te onderhouden.
- Reverse-index utility (`tools/lib/coverage.py`) bouwt op aanvraag een concept→kenniselementen-mapping voor dekkingsrapporten.
- Dekkingscheck draait per snapshot vóór publicatie van leermateriaal (ADR-010).
- Vakken blijven bestaan als label op programmaonderdeel-fiches en als examen-organisatie, niet als kennis-organisatie.
