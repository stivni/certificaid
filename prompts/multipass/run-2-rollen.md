# Operatie: `accountant_perspectief` (run-2)

Schema-versie: 2.1 v1.5 (zie `data/concepten/schema-2.1.schema.json` — `$comment`/`description` per `$def` is bron-van-zelfsturing).

**Doel**: vul `inhoud.accountant_perspectieven[]` van het record. Bouw didactische rol × perspectief-matrix.

**Input**: `/tmp/<fiche-id>.json` (na `beschrijven`; bevat al `inhoud.kern` + `elementen`).

**Output**: overschrijf met aangevuld `accountant_perspectieven`.

---

## Confidence-tokens (overzicht)

| Token | Symbool | Wanneer toegestaan in deze operatie |
|---|---|---|
| `geciteerd` | 📖 | ❌ — alleen `claims_checken` |
| `afgeleid` | 🔗 | ❌ — alleen `claims_checken` |
| `verondersteld` | 🤖 | ✅ |
| `betwijfeld` | ❓ | ✅ |
| `weerlegd` | ❌ | ❌ |

Alle claims = `verondersteld` met `ai_model`-bron (en/of `mens`-bron). `claims_checken` upgradet later.

---

## Conceptuele scheiding van mechanisme

Deze sectie gaat over **wat doet de accountant**, niet over het concept zelf. Voorkom dubbel-schrijven met `inhoud.elementen` (= "hoe werkt het").

| `inhoud.elementen` | `inhoud.accountant_perspectieven` |
|---|---|
| Mechanisme · principe · stappen · formule · drempel · regel | Wat doet **accountant** voor klant-perspectief X als rol Y |
| Bv. "Disagio = uitgiftekost gespreid via matching" | Bv. "Als boekhouder: boek bij uitgifte rekening 4901 over te dragen disagio" |

Kruisverwijzen via `relaties[]` op het element (niet via verouderde `verwijst_naar`).

---

## v1.5-structuur (één nesting-laag minder dan v1.4)

```json
"inhoud": {
  "accountant_perspectieven": [
    {
      "id": "uitgever-vennootschap",
      "naam": {"primair": "Voor de uitgever-vennootschap"},
      "rollen": [
        {
          "rol": "adviseur",
          "elementen": [
            {
              "id": "advies-keuze-financieringsvorm",
              "naam": {"primair": "Klant adviseren over keuze"},
              "inhoud_type": "vuistregel",
              "kern": {
                "rationale": {
                  "tekst": "...",
                  "grondslag": {"confidence": "verondersteld", "bronnen": [{"type": "ai_model", "naam": "claude-sonnet-4-6", "datum": "<vandaag>"}]}
                }
              }
            }
          ]
        }
      ]
    }
  ]
}
```

**Verschillen met v1.4**:
- Hernoemd: `rollen_per_perspectief` → `accountant_perspectieven`.
- Top-level wrapper `perspectieven[]` is weg (lijst-items zijn direct de perspectieven).
- Elementen volgen v1.5-element-shape met `kern.{definitie,substantie,rationale}` — gebruik `kern.rationale` voor de rol-instructie.
- Veld `tekst` (was `text`).

---

## Vijf-rol-set (cf. ADR-025 §4)

- `adviseur` — strategische keuze + planning
- `boekhouder` — boekingen + balans-impact
- `begeleider` — procedurele afhandeling
- `fiscaal` — aangifte + optimalisatie
- `auditor` — controle-perspectief

Geen verdere rollen-uitbreidingen: `bestuurder`/`curator`/`forensisch` zijn personae binnen perspectief, niet accountant-rollen (gedropt in v1.5).

---

## Plaatsingsregel (vastgelegd 2026-05-23)

**Hier (`accountant_perspectieven`) hoort álle handelings-kennis** — wat doet de accountant. Dat is **harde grens** met `inhoud.elementen` (= concept-intrinsiek, wat-is-het).

**Litmus**: "gebeurt dit ongeacht of er een accountant bij betrokken is?" → ja → element; → nee → rol.

| Inhoud | Plek |
|---|---|
| Boekhoudkundige verwerking · rekening-codes · boekingsmoment | rol=`boekhouder` |
| Audit-procedures · risico-drempels · controle-aandachtspunten | rol=`auditor` |
| Aangifte-codes · fiscale optimalisatie-stappen | rol=`fiscaal` |
| Advies-checklist · alternatieven-afweging · vuistregels | rol=`adviseur` |
| Begeleidings-stappen · formaliteiten · termijn-bewaking | rol=`begeleider` |

Concept-intrinsieke procedures (wettelijke termijn, schuldeisersbeschermings­procedure als dwingend onderdeel van een verrichting, ...) blijven bij `inhoud.elementen`. Bij dubbeling: kruisverwijs via `relaties[]` op de claim, **niet dupliceren**.

---

## Per-rol-instructies (vastgelegd; waar van toepassing)

- **adviseur**: keuze + alternatieven + vuistregels
- **auditor**: risico + drempels + controle-procedures
- **boekhouder**: boekingen + balans-impact + timing
- **begeleider**: formaliteiten + termijnen + publicaties
- **fiscaal**: aangifte-codes + aftrek + optimalisatie

(Diepere data-driven per-rol-element-typering wordt na wave-2 (≥ 50 ingevulde records) geëvalueerd — cf. ADR-029 §E3.)

---

## Discipline

- **Toon geen lege rollen.** Cell-fill matrix per perspectief: alleen rollen die echt iets te zeggen hebben.
- **Cross-PO-completeness**: als concept zowel PO 1.1 (boekhouden) als PO 2.x (fiscaal) raakt, vul beide rol-perspectieven.
- **Geen overlap** met `inhoud.elementen` — kruisverwijs via `relaties[]` op het element.
- **Element-shape** = identiek aan top-level `element` (zie `beschrijven`-prompt + schema `$defs/element`).
- **Migratie-check** voor bestaande records: als `inhoud.elementen[]` items bevat die volgens de plaatsingsregel onder een rol horen (bv. een `procedure_stap` "Boekhoudkundige verwerking"), verplaats die — verwijder uit `elementen`, voeg toe onder de juiste rol, log in changelog.

---

## Werkwijze

1. Lees `/tmp/<fiche-id>.json` (na `beschrijven`).
2. Identificeer klant-perspectieven uit `inhoud.elementen` + `concept_type`:
   - **instrument / regime**: uitgever vs ontvanger vs belegger vs bestuur
   - **verrichting**: initiator vs ontvanger vs toezichthouder
   - **procedure**: actor-per-fase
   - **ratio**: analist vs onderwerp-bedrijf
   - **balanspost / methode**: opsteller vs gebruiker
3. Voor elke perspectief: welke rollen heeft de accountant?
4. Per rol: 1-3 elementen (kerntaak, niet alles).
5. Schrijf record terug naar `/tmp/<fiche-id>.json`.
6. Update `metadata.changelog`:
   ```json
   {"operatie": "accountant_perspectief", "timestamp": "<ISO>", "model": "<jouw-model>"}
   ```

**Tempo**: 1-2 min. Geen RAG.

---

## Eindrapport

- Aantal perspectieven · aantal cellen (rol × perspectief).
- Confidence-mix.
- Open vragen voor `claims_checken`.
