# PO-builder: procesflow voor programmaonderdeel-builds

> ⚠️ **Pre-redesign-document** (vóór 2026-05-07). PO-build-procesflow onder het oude drie-lagenmodel. PO-output gaat in de nieuwe architectuur via release-snapshots gegenereerd uit de concepten-laag — zie [ADR-010](adr/ADR-010-leermateriaal-tutor.md) en [`roadmap.md`](roadmap.md) Fase 5. De `po-builder` scheduled agent draait niet meer; document blijft staan als referentie tot Fase 5 een nieuwe builder definieert.

Volledige procesflow voor het bouwen van een programmaonderdeel (PO). Wordt geladen door de po-builder scheduled agent via `resources/po-builder-prompt.md`.

**Verwante docs**: [`docs/content-richtlijnen.md`](content-richtlijnen.md) — schrijfregels · [`docs/adr/INDEX.md`](adr/INDEX.md) — architectuurbeslissingen

---

## Werkprincipe

Een PO-build is een gestructureerde doorloop van alle TDKs van één programmaonderdeel:
1. Structuur bepalen (welke concepten en competenties zijn nodig?)
2. Materie schrijven (brongebonden conceptfiches)
3. Competenties schrijven (procedure-fiches)
4. PO-fiche bijwerken (catalogus + links)
5. Reviewronde (factcheck + leesbaarheid)

**Branch**: alle werk op `rag-tutor` (later `main` na validatie).

**Modelkeuze**:
- Stap 2B Taakdecompositie: Claude Opus (complexe redenering)
- Alle andere stappen en subagenten: Claude Sonnet 4.6

---

## Stap 0 — Voorbereiding

**Acties**:
1. Maak `.po-voortgang-[PO].md` aan in de projectroot als eerste actie
2. Schrijf het PO-nummer in `.po-target`
3. Lees de PO-fiche in `content/programmaonderdelen/[PO]-*.md`
4. Verwijder de `verborgen`-tag als die er nog op staat

**Voortgangsbestand** (`.po-voortgang-[PO].md`):
```markdown
# Voortgang PO [X.X] — [Datum]

## Status
- [ ] Stap 0: Voorbereiding
- [ ] Stap 1: Bronnen
- [ ] Stap 2A: Concepten identificeren
- [ ] Stap 2B: Taakdecompositie
- [ ] Stap 3A: Materie schrijven
- [ ] Stap 3B: Competenties schrijven
- [ ] Stap 4: PO-fiche bijwerken
- [ ] Stap 5: Reviewronde

## Beslissingen
[Architectuurbeslissingen en afwijkingen van de standaardprocedure]

## Verdicts reviewronde
[Per fiche: factcheck-verdict + leesbaarheid-verdict]
```

---

## Stap 1 — Bronnen laden

Laad de relevante bronnen voor dit PO:

```bash
# Welke wetteksten zijn relevant?
cat resources/bronnen/wetteksten/WETTEKSTEN-INDEX.md

# Welke normen?
grep -l "[thema]" resources/bronnen/normen/

# Welke CBN-adviezen?
grep -l "  - [thema]" resources/bronnen/adviezen/
```

Controleer beschikbaarheid via `content/bronnen/ITAA-LEX.md`.

---

## Stap 2A — Concepten identificeren

Lees de TDKs van het PO en identificeer alle concepten die nodig zijn:

1. Lees taken en doelstellingen: welk fenomeen moet de student beheersen?
2. Lees kenniselementen: welke begrippen worden expliciet genoemd?
3. Identificeer impliciete concepten (verondersteld maar niet vermeld)
4. Check of concepten al bestaan (andere POs)

Output: lijst van te bouwen concepten met geschatte scope.

---

## Stap 2B — Taakdecompositie (Opus)

Voor elk concept: bepaal welke materie-secties nodig zijn op basis van het niveau:
- `weten-en-inzien` → 📌⚖️🔒 secties
- `toepassen` → 📋🔢✅👤 secties
- `integratie` → 🔎🚩↔️ secties + minstens één ↔️ vergelijking

Output per concept: overzicht van te schrijven secties + bronverwijzingen.

---

## Stap 3A — Materie schrijven

Per concept-fiche:

1. Open bestaande fiche of maak nieuwe aan met `wip`-tag en `status: draft`
2. Schrijf secties in volgorde: begrippen → principes → procedures → vergelijkingen → rollen
3. Elke bewering krijgt een inline bronverwijzing
4. Valkuilen en voorbeeldvragen mogen 🤖 zijn (gelabeld)
5. Semantische hyperlinkdoorlezing: elk conceptwoord dat een fiche heeft, krijgt een link
6. Kritische lezing: elke zin beantwoording vanuit studentperspectief

**Kwaliteitschecks** (zie `docs/content-richtlijnen.md` §Kwaliteitschecks):
- Hoofdregel vóór uitzondering
- Oorzaak → gevolg
- Actieve zinnen
- Geen "in bepaalde gevallen" zonder precisering

---

## Stap 3B — Competenties schrijven

Per competentie-fiche:

1. Zoek eerst of een ITAA-norm of CBN-advies de procedure beschrijft
2. Open of maak fiche aan met `wip`-tag
3. Schrijf grondslag-blok met 🤖/⚖️-indicator
4. Schrijf stappen: elk met `📥/📤`-blok + waarom-zin + instructie
5. Visueel anker verplicht bij stappen die inwerken op financiële documenten
6. `[!info]- Concreet` verplicht bij oordeel/beslissingstappen
7. Minstens één uitgewerkt voorbeeld (Situatie/Conclusie/Grondslag/Redenering)

**Kwaliteitscheck**: stel jezelf na elke competentie de vraag: klopt de naam nog met de scope?

---

## Stap 4 — PO-fiche bijwerken

1. Voeg links toe van kenniselementen → materie-secties
2. Voeg links toe van taken → competentie-fiches
3. Vul "Relevante materie" en "Relevante competenties" volledig aan
4. Voer de verificatiestap uit (zie `docs/content-richtlijnen.md` §Programmaonderdeel-fiches)

---

## Stap 5 — Reviewronde

Twee subagenten draaien in parallel:

### Factchecker-agent

Prompt:
```
Je bent een juridisch-boekhoudkundige factchecker voor het ITAA-bekwaamheidsexamen.
Controleer elke fiche van PO [X.X] op:
1. Elke feitelijke bewering heeft een bronverwijzing
2. Bronverwijzingen zijn traceerbaar (bestand + artikelnummer)
3. Geen tegenstrijdige uitspraken binnen de fiche
4. Uitzonderingen zijn volledig en correct
5. Geen circulaire definities

Rapporteer per fiche: AKKOORD / CORRIGEER [beschrijving] / ESCALEER [detail]
```

### Leesbaarheid-agent

Prompt:
```
Je bent een leesbaarheidsreviewer voor ITAA-studiemateriaal.
Controleer elke fiche van PO [X.X] op:
1. Hoofdregel staat vóór uitzondering
2. Oorzaak → gevolg (niet omgekeerd)
3. Actieve zinnen (actor is zichtbaar)
4. Geen vage formuleringen ("in bepaalde gevallen", "de bevoegde autoriteit")
5. Parallelstructuur in opsommingen
6. Wikilinks aanwezig op alle conceptwoorden

Rapporteer per fiche: AKKOORD / AANPASSEN [beschrijving]
```

**Verdicts bijhouden** in `.po-voortgang-[PO].md`.

---

## Subagenten

| Subagent | Model | Taak |
|---|---|---|
| Taakdecompositor | Opus | Stap 2B — complexe structuuranalyse |
| Materie-schrijver | Sonnet | Stap 3A — conceptfiches |
| Competentie-schrijver | Sonnet | Stap 3B — competentiefiches |
| Factchecker | Sonnet | Stap 5 — bronverificatie |
| Leesbaarheidsreviewer | Sonnet | Stap 5 — stijl en structuur |

Elke subagent laadt `docs/content-richtlijnen.md` als context vóór zijn taak.
