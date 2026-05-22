# ADR-001: Lagen-architectuur

**Status**: Draft
**Datum**: 2026-05-07

## Context

Certificaid moet een ITAA-bekwaamheidsexamen afdekken vanuit een mix van inputs (wetteksten, CBN-adviezen, normen, voorbeeldexamens, kenniselementen uit het examenprogramma) tot uiteindelijk leermateriaal en een interactieve tutor. Eerdere iteraties wankelden tussen "bron is leerstof" (te dicht bij artikelen, geen samenhang) en "vakindeling is leerstof" (artificiële splitsing van vakoverschrijdende fenomenen). Een expliciete lagenstructuur ontbrak; concept-, examenpatroon- en outputlagen liepen door elkaar.

## Beslissing

Vier opeenvolgende lagen + één parallelle observatielaag, met twee cross-cutting concerns (provenance, reprocessing) die elke laag raken:

```
[ruwe bronnen]                              ← inputs
    ↓ ETL                                   (ADR-005)
[leesbare bron-MD]
    ↓ indexering                            (ADR-006)
[bronnen-RAG]
    ↓ extractie ← examenprogramma-scoping (ADR-002)  (ADR-008)
[concepten] ←→ examenpatronen               (ADR-009)
    ↓ indexering                            (ADR-006)
[concepten-RAG]
    ↓
[leermateriaal-snapshots] + [tutor]         ← outputs (ADR-010)

cross-cutting: reprocessing (ADR-003), provenance (ADR-004)
```

**Tutor draait *direct* op de concepten-laag** — lage latency tussen wijziging in concept en wat de student ziet. **Leermateriaal gaat door een release-snapshot** — append-only, met changelog. Studieleerstof bewegt niet onder de student z'n voeten.

**Concepten zijn vakoverschrijdend** (één concept kan in meerdere programmaonderdelen voorkomen). Vakindeling leeft enkel in de programmaonderdeel-fiches op output-niveau.

**Examenpatronen lopen parallel aan concept-extractie**, niet erna. Beide gebruiken voorbeeldexamens als ground truth en voeden elkaar.

## Gevolgen

- Elke laag heeft eigen DoD, eigen regressietests en eigen stale-mechaniek (ADR-003).
- Volgorde van bouwen ≠ volgorde van afhankelijkheden: één POC-vertical-slice doorloopt alle lagen, daarna verbreding (zie [`docs/TODO.md`](../TODO.md) §Mindset).
- Beslissingen in deze ADR-stack zijn samen het architectuurkader; afwijken vereist een nieuwe ADR.
