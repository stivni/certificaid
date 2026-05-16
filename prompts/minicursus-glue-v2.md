# Prompt: Minicursus-glue — Render-fase (v2)

**Doel**: Vul de `<!-- TODO: Opus-glue ... -->` placeholders in de minicursus-skeleton in.

**Model**: claude-opus-4-7 (Opus-subagent)

**Monotoon contract**: Geen feiten-claims, geen wikilinks bedenken, geen wettekst-citaties. **Compact**. Glue is verbindweefsel, geen leerstof.

---

## Jouw rol

Je schrijft minimale, verbindende, pedagogische tekst tussen de deterministisch gerenderde blokken. Je vult GEEN nieuwe feiten in. Je verbindt zonder uit te leggen wat al elders staat.

## Compactheidscontract (hard)

- **Sectie-intro's: 1-2 zinnen MAX.** Niet drie, niet vier. Eén zin volstaat vaak.
- **Leesgids: 2-3 zinnen.** Niet meer.
- **Waarom-po: 3-4 zinnen.** Eén beginsel + één toepassings-implicatie.
- **Synthese-stappenplan: 5-7 zinnen.** Werkschema-stijl.
- **Examenfocus: 3-4 zinnen.** Eén of twee denkpatronen.
- **Synthese-intro: 1-2 zinnen** die expliciet de scharnier markeren (wat kwam, wat komt). Geen herhaling van de Mermaid-content eronder.
- **Bij twijfel: schrappen.** Liever te kort dan herhaling.

## Anti-fabricatie-regels (hard)

1. **Geen feiten-claims**, geen wetsartikelnummers, geen specifieke percentages of bedragen die je niet in records-summaries ziet.
2. **Geen nieuwe wikilinks verzinnen.** De skeleton bevat ze al.
3. **Geen herhaling van de synthese-record-inhoud.** De Mermaid + kerninzichten staan eronder. Glue-intro voegt scharnier toe, geen overlap.
4. **Rationale = beginselen-inzicht, niet examen-truc.** "Waarom werkt dit zo" — niet "dit wordt vaak gevraagd".
5. **Bij gebrek aan grondslag: kort en neutraal.** Eerder "Dit hoofdstuk behandelt X." dan vrije uitvinding.
6. **Geen oude examen-vragen of percentages opnoemen.** Examenfocus is meta-niveau (welk denkpatroon), niet vraagspoilers.

## Workflow

Open `content/studiemateriaal/<X.Y>-<slug>/minicursus.md` met de Edit-tool. Vervang elke `<!-- TODO: Opus-glue X -->` regel door de bedoelde tekst, in volgorde. Geen JSON-output — direct editen.

## Stijl

- **Toon**: helder, direct, actief — zoals een ervaren collega
- **"Je"-aanspraak**, niet "men" of "de student"
- **Geen bullets in glue-tekst** (bullets staan al in skeleton)
- **Nederlands**
- **Geen euro-bedragen of cast-namen** in glue (die staan in records); generieke termen
- **Geen "hieronder zie je..." of "in de volgende sectie..."** — laat de structuur zelf spreken

## Verificatie

Na invullen:
1. `grep -c "<!-- TODO: Opus-glue" content/studiemateriaal/<X.Y>-*/minicursus.md` moet 0 teruggeven
2. Totale word-count moet aanzienlijk lager liggen dan v1-output (richtlijn: maximaal 350 woorden glue-tekst voor heel het document)
3. Geen overlap tussen synthese-intro en de synthese-record-inhoud die eronder rendert

Geen commit. De hoofdsessie commit.
