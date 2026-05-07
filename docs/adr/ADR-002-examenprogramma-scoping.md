# ADR-002: Examenprogramma als scoping-anker

**Status**: Draft
**Datum**: 2026-05-07

## Context

Het ITAA-examenprogramma definieert per programmaonderdeel een lijst **taken**, **doelstellingen** en **kenniselementen** — eindtermen die de stagiair moet kunnen demonstreren. Dat is de enige externe definitie van wat getoetst kan worden. Zonder zo'n anker blijven vragen als "is mijn conceptenset volledig?" en "welke concepten zijn examen-relevant?" subjectief.

Eerdere iteraties gebruikten *vakken* als organisatie-eenheid voor leerstof. Dat is onjuist: vakken zijn een examen-organisatielaag, geen kennislaag. Concepten kunnen vakoverschrijdend zijn (antiwitwaswetgeving komt voor in deontologie én in fiscaliteit). Een concept-per-vak-organisatie produceert duplicatie.

## Beslissing

**Het examenprogramma is de externe scope-definitie.** Concepten worden geëxtraheerd om kenniselementen af te dekken; vakindeling speelt alleen mee in de output-laag van de programmaonderdeel-fiches.

1. **Het examenprogramma wordt expliciet ingelezen** als gestructureerde data — één bestand per programmaonderdeel in `data/programmaonderdelen/`, met taken, doelstellingen en kenniselementen elk gecodeerd. Provenance-getagd zoals elk ander artefact (ADR-004).

2. **Concept ↔ kenniselement-koppeling** is een verplicht veld op elk concept-record (`afdekt_kenniselementen: [...]`). Eén concept kan meerdere kenniselementen afdekken, één kenniselement kan meerdere concepten vragen.

3. **Dekkingscheck** is een eerste-orde regressietest:
   - Voor elk kenniselement: minstens één concept-record dat hem afdekt
   - Voor elk kenniselement: minstens één voorbeeldvraag of examenpatroon dat hem toetst
   - Gat-rapport stuurt nieuwe extractie-rondes (ADR-008)

4. **Anti-circulariteit**: het examenprogramma stuurt *welke* concepten nodig zijn, niet *wat* een concept inhoudt. Concept-inhoud komt uit bronnen + voorbeeldexamens, niet uit de tekst van het examenprogramma zelf.

## Gevolgen

- Nieuwe of gewijzigde kenniselementen in het examenprogramma → stale-flag op gerelateerde concept-records → herextractie of -uitbreiding.
- Programmaonderdeel-bestanden leven in `data/programmaonderdelen/` (één JSON per programmaonderdeel), versie-getagd.
- Dekkingscheck draait per snapshot vóór publicatie van leermateriaal (ADR-010).
- Vakken blijven bestaan als label op programmaonderdeel-fiches en als examen-organisatie, niet als kennis-organisatie.
