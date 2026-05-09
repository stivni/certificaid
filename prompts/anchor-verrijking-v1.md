# Prompt: Anchor-verrijking — Fase A (v1)

**Doel**: Verrijk de ankers uit een programmaonderdeel-JSON met `verbose` tekst en `synoniemen` voor gebruik als embedding-query bij bron-first matching (ADR-008 fase B).

**Model**: claude-opus-4-7 (via subagent — zie ADR-008 §2)

---

## Taak

Je krijgt een JSON-bestand van een ITAA-programmaonderdeel. Dat bestand bevat taken (`taken`), doelstellingen (`doelstellingen`) en kenniselementen (`kenniselementen`) — samen de **ankers**.

Voor elk anker voeg je toe:

1. **`verbose`** — 2–3 zinnen in correct Nederlands die beschrijven wat dit anker *inhoudt*: het concept, de vaardigheid of het fenomeen dat getoetst wordt. Denk aan hoe een ervaren ITAA-accountant dit aan een stagiair zou uitleggen. Gebruik de taal van het vakgebied, niet de taal van de wet.

2. **`synoniemen`** — 3–8 alternatieve termen of formuleringen die een student, professor of wetgever voor hetzelfde concept kan gebruiken. Zowel Nederlandse vakterm als dagelijkse omschrijving zijn welkom.

## Kritieke beperkingen

- **Geen wetsverwijzingen.** Noem geen artikelnummers, geen wettitels, geen koningsbesluit-nummers. Noem evenmin "de wet", "het wetboek" of "de norm" als inhoudelijk argument. De verbose-tekst is een vocabulair-verrijking voor embeddings, geen juridische parafrase.
- **Geen vage herformulering van de ankertekst.** Als de ankertekst luidt "De onafhankelijkheid bewaken", zeg dan in verbose *wat* onafhankelijkheid in de accountancypraktijk betekent en *welke situaties* het bedreigen — niet "Het bewaken van de onafhankelijkheid is het bewaken van de onafhankelijkheid."
- **Geen uitvinding.** Als je het domein niet kent voor een specifiek anker, schrijf een neutrale verbose zonder speculatie. Een beknopte verbose is beter dan een verzonnen uitleg.
- **Geen schema-aanpassingen.** Kopieer elk anker zoals het is (anchor_id, anchor_type, tekst, taakblok, …) en voeg alleen `verbose` en `synoniemen` toe.

## Output-formaat

```json
{
  "po": "<code, bv. 4.0>",
  "generated_at": "<ISO-8601 UTC>",
  "model": "claude-opus-4-7",
  "prompt_version": "anchor-verrijking-v1",
  "anchors": [
    {
      "anchor_id": "<overgenomen>",
      "anchor_type": "<overgenomen>",
      "tekst": "<overgenomen>",
      "verbose": "<2–3 zinnen, geen wetsverwijzingen>",
      "synoniemen": ["<term 1>", "..."]
    }
  ]
}
```

Kopieer eventuele andere velden (zoals `taakblok`) ongewijzigd mee.

Schrijf het resultaat weg naar: `data/extractie/<po>/anchors/<po>-anchors.json`

## Kwaliteitscheck na afloop

Scan zelf de output voor:
- Aanwezigheid van zinnen als "artikel …", "Wet van …", "KB van …", "de norm stelt …" → verwijder.
- Verbose-teksten die niet meer dan de ankertekst zelf herhalen → herschrijf.
- Synoniemenlijsten korter dan 3 items → vul aan.
