# ADR-002: TDK als scoping-anker

**Status**: Draft
**Datum**: 2026-05-07

## Context

Het ITAA-examenprogramma definieert per vak een lijst **taakdoelkennis (TDK)** — eindtermen die de stagiair moet kunnen demonstreren. Dat is de enige externe definitie van wat getoetst kan worden. Zonder zo'n anker blijven vragen als "is mijn conceptenset volledig?" en "welke concepten zijn examen-relevant?" subjectief.

Eerdere iteraties gebruikten *vakken* als organisatie-eenheid voor leerstof. Dat is onjuist: vakken zijn een examen-organisatielaag, geen kennislaag. Concepten kunnen vakoverschrijdend zijn (AWW komt voor in deontologie én in fiscaliteit). Een concept-per-vak-organisatie produceert duplicatie.

## Beslissing

**TDK-tekst is de externe scope-definitie.** Concepten worden geëxtraheerd om TDK-elementen af te dekken; vakindeling speelt alleen mee in de PO-output-laag.

1. **TDK-set wordt expliciet ingelezen** als gestructureerde data (per PO een lijst TDK-elementen met tekst, code, en verwijzing naar bron-pagina van het programma). Provenance-getagd zoals elk ander artefact (ADR-004).

2. **Concept ↔ TDK-koppeling** is een verplicht veld op elk concept-record (`afdekt_tdk: [...]`). Eén concept kan meerdere TDK's afdekken, één TDK kan meerdere concepten vragen.

3. **Dekkingscheck** is een eerste-orde regressietest:
   - Voor elke TDK: minstens één concept-record dat hem afdekt
   - Voor elke TDK: minstens één voorbeeldvraag of examenpatroon dat hem toetst
   - Gat-rapport stuurt nieuwe extractie-rondes (ADR-008)

4. **Anti-circularity-regel**: TDK-tekst stuurt *welke* concepten nodig zijn, niet *wat* een concept inhoudt. Concept-inhoud komt uit bronnen + voorbeeldexamens, niet uit de TDK-tekst zelf.

## Gevolgen

- Nieuwe of gewijzigde TDK in het programma → concept-stale-flag op gerelateerde records → herextractie of -uitbreiding.
- TDK-bestanden leven in `data/tdk/` (één JSON of YAML per PO), versie-getagd.
- Dekkingscheck draait per snapshot vóór publicatie van leermateriaal (ADR-010).
- Vakken blijven bestaan als label op PO-fiches en als examen-organisatie, niet als kennis-organisatie.
