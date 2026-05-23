# Schema 2.1 v1.5 — weergave-payload sub-schemas (TBD)

**Status**: open punt, doorgeschoven naar na wave-2.
**Context**: in `data/concepten/schema-2.1.schema.json` heeft `$defs/weergave` momenteel `additionalProperties: true`. Alleen het `type`-veld is enum-gevalideerd; de type-specifieke payload (e.g. een boekingstabel, een balans-snapshot) is structureel onbeperkt. Het besluit-doc (§"weergave_type enum") noemt dit expliciet als TBD.

## Waarom uitstellen

Bij v1.5-vaststelling was er onvoldoende corpus om payload-shapes per type te canoniseren. Wave-2 (`beschrijven` op 371 records) + de reverse-engineerde example-records (`data/concepten/examples/obligatielening-*-*.json`) leveren de eerste serieuze dataset. **Pas na wave-2 + render-pilot** kunnen we vaststellen welke payload-velden render-laag echt nodig heeft.

## De 11 weergave-types + voorgestelde payload-shape

Onderstaand is een eerste schets, NIET schema-bindend. Gebaseerd op patronen in `content/experiment/obligatielening-v7.md` + render-laag-overwegingen.

### `proza`
```json
{ "type": "proza", "tekst": "string" }
```
Eenvoudigste vorm — pure tekst als alternatief op het claim-`tekst`-veld zelf. Mogelijk redundant en kandidaat voor schrappen.

### `tabel`
```json
{
  "type": "tabel",
  "titel?": "string",
  "kolommen": ["string", ...],
  "rijen": [["string"|number, ...], ...],
  "voetnoot?": "string"
}
```

### `boeking`
```json
{
  "type": "boeking",
  "context?": "string",
  "datum?": "ISO-date | omschrijving",
  "rekeningen": [
    {
      "nummer": "string",                   // bv. "550 Kas"
      "omschrijving?": "string",
      "debet?": number,
      "credit?": number
    }
  ],
  "totaal_debet?": number,
  "totaal_credit?": number,
  "balanced?": boolean,
  "toelichting?": "string"
}
```
Validator-suggestie: `totaal_debet == totaal_credit` (anyOf-constraint).

### `balans_snapshot`
```json
{
  "type": "balans_snapshot",
  "context?": "string",
  "datum?": "ISO-date | balans-moment",
  "actief": [
    {
      "rubriek": "string",                  // bv. "Materiële vaste activa"
      "code?": "string",                    // MAR-code
      "bedrag": number
    }
  ],
  "passief": [/* zelfde shape */],
  "totaal_actief?": number,
  "totaal_passief?": number,
  "toelichting?": "string"
}
```

### `resultatenrekening_snapshot`
```json
{
  "type": "resultatenrekening_snapshot",
  "context?": "string",
  "periode?": "string",
  "posten": [
    {
      "rubriek": "string",
      "code?": "string",
      "bedrag": number,
      "teken?": "kost|opbrengst"            // optioneel; afleidbaar uit teken bedrag
    }
  ],
  "resultaat?": number,
  "toelichting?": "string"
}
```

### `stappenlijst`
```json
{
  "type": "stappenlijst",
  "titel?": "string",
  "stappen": [
    {
      "nummer?": integer,
      "titel?": "string",
      "beschrijving": "string"
    }
  ]
}
```

### `tijdslijn`
```json
{
  "type": "tijdslijn",
  "titel?": "string",
  "punten": [
    {
      "moment": "ISO-date | omschrijving",
      "gebeurtenis": "string",
      "actor?": "string"
    }
  ]
}
```

### `vergelijkingstabel`
```json
{
  "type": "vergelijkingstabel",
  "titel?": "string",
  "opties": ["string", ...],                // bv. ["Lineair", "Effective interest"]
  "criteria": [
    {
      "criterium": "string",                // bv. "Spreiding cashstroom"
      "waardes": ["string", ...]            // één per optie, zelfde volgorde
    }
  ]
}
```

### `formule_expressie`
```json
{
  "type": "formule_expressie",
  "expressie": "string",                    // bv. "JR = (Nominale × coupon%) + (Disagio / Looptijd)"
  "variabelen?": [
    { "symbool": "string", "betekenis": "string", "eenheid?": "string" }
  ]
}
```

### `berekening`
```json
{
  "type": "berekening",
  "context?": "string",
  "stappen": [
    { "label": "string", "berekening": "string", "resultaat": number | "string", "eenheid?": "string" }
  ],
  "eindresultaat?": { "label": "string", "waarde": number, "eenheid?": "string" }
}
```
Onderscheid met `formule_expressie`: berekening heeft concrete getallen; formule_expressie alleen symbolen.

### `beslisboom`
```json
{
  "type": "beslisboom",
  "wortel": {
    "vraag": "string",
    "opties": [
      {
        "antwoord": "string",
        "uitkomst?": "string",
        "volgende_vraag?": { /* recursie */ }
      }
    ]
  }
}
```

## Cross-cutting

- Alle types kunnen optioneel `grondslag` (`$ref: #/$defs/grondslag`) hebben.
- Geen verplicht `id`-veld op weergave-niveau (claim heeft al de identiteit).
- Geen `weergaven[]` binnen `weergave` — geen recursie.
- Validator-suggestie: `oneOf` over de 11 sub-schemas met `type`-discriminator.

## Migratie-plan zodra geïmplementeerd

1. Per type een sub-schema in `$defs/weergave_<type>`.
2. `$defs/weergave` wijzigen naar `oneOf: [...]` met `if/then` op `type`.
3. `additionalProperties: false` zetten.
4. Auto-fix-extensie in `multi_pass_extract.py`: detecteer veelvoorkomende payload-veld-fouten (e.g. `bedragen` i.p.v. `rijen`).
5. Re-validate alle records; rapporteer welke payloads geen schema-match hebben → manuele fix of schema bijschaven.

## Wanneer aanpakken

**Niet vóór wave-2** — eerst zien wat agents in de praktijk produceren. Realistisch:

- **Wave-2 klaar** (≈ 2026-05-24): inventariseer payload-shapes in alle 396 records.
- **Render-pilot start**: render-laag krijgt eerste shape-eisen; sub-schemas hierop afstemmen.
- **v1.6 schema-update**: sub-schemas voor 4-5 meest-gebruikte types (`boeking`, `balans_snapshot`, `tabel`, `vergelijkingstabel`, `berekening`).
- **v1.7**: resterende types.
