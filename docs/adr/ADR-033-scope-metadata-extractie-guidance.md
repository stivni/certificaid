# ADR-033 — `scope.in` + `scope.out` in record-metadata als extractie-guidance

**Status**: Draft (2026-05-26)
**Gerelateerd**: ADR-029 (schema 2.1 v1.5) · ADR-030 (granulariteit-typologie) · `docs/granulariteit-skelet.md` (cluster-uitwerkingen + scope-formulering per record)

## Context

Tijdens granulariteit-skelet-sparring (PO 1.6 · PO 1.7 · PO 3.0.I, 2026-05-26) zijn rond elk uitgewerkt record twee soorten beslissingen genomen die de extractie-LLM straks moet respecteren:

1. **Wat behandelt dit record?** — bv. `controleopdracht` dekt de 4-fase-cyclus + basisattitude (skepticism) + team-organisatie.
2. **Wat behandelt dit record expliciet NIET?** — bv. `controleopdracht` behandelt geen planning-detail (zie `audit-planning`), geen bewijswerk-procedures (zie `audit-bewijs`), geen oordeel-vormen (zie `controleverklaring`).

Zonder deze afbakening krijgt de extractie-LLM bij operaties als `beschrijven` / `claims_checken` / `didactisch_verrijken` geen guidance om scope-creep en duplicatie te vermijden. Risico: hetzelfde topic landt in 2-3 fiches; cluster-sparring-werk verwatert in latere extractie.

Bestaande velden vangen dit niet af:
- `metadata.ankers[]` zegt welke PO-anchors het record raakt — niet wat het wel/niet inhoudelijk behandelt.
- `relaties[]` zegt welke andere records gerelateerd zijn — niet wat NIET in dit record komt.
- `inhoud.kern.definitie` beschrijft het concept — geen scope-uitspraak.

## Beslissing

Nieuwe velden in `metadata`:

```json
"metadata": {
  ...
  "scope": {
    "in":  ["topic 1", "topic 2", ...],
    "out": ["topic A (zie record-x)", "topic B (zie record-y)", ...]
  }
}
```

**Beide velden zijn optioneel** — niet elk record vereist scope-afbakening. Records waar versplintering risico is (Σ-records, K-techniek-records, bundel-records) hebben er meer baat bij dan zelfstandige fenomeen-records.

**Beide zijn `array<string>` met vrije tekst**. Bewust niet gestructureerd (geen `{topic, zie}`-objects, geen record-id-validatie). Reden:
- Eenvoudig in te vullen tijdens cluster-sparring + extractie
- Geen schema-evolutie nodig wanneer cross-references in records evolueren
- Render-laag heeft scope-velden niet nodig voor functionaliteit (cross-references staan ook in `inhoud`-tekst voor de student)

**Doel van de velden = LLM extractie-guidance**:
- Bij operatie `beschrijven`: LLM krijgt `scope.in` als positieve guidance ("dit moet je behandelen"), `scope.out` als negatieve guidance ("dit hoort hier niet — verwijs naar record X").
- Bij operatie `claims_checken`: LLM filtert RAG-hits — wat uit scope valt mag niet als claim binnen dit record landen.
- Bij operatie `didactisch_verrijken`: voorbeelden + valkuilen moeten binnen `scope.in` blijven.

**Cross-references in `inhoud` blijven legitiem** — student moet via in-tekst-links naar de juiste fiche worden gestuurd. `scope.out` voorkomt *duplicatie van inhoud*, niet *vermelding van afbakening*.

## Voorbeeld — `controleopdracht`-record (PO 1.6)

```json
{
  "id": "controleopdracht",
  "naam": {"primair": "Controleopdracht"},
  "concept_type": "kader",
  "metadata": {
    "schema_version": "2.1",
    "status": "seed",
    "ankers": ["1.6.taak.1", "1.6.II", "1.6.III", "1.6.IV"],
    "scope": {
      "in": [
        "4-fase-cyclus (aanvaarden → plannen → bewijswerk → afronden+oordeel) als overzichts-niveau",
        "basisattitude (skepticism, professionele oordeelsvorming) als doordringend principe",
        "team-organisatie (delegatie + supervisie) als sub-aspect"
      ],
      "out": [
        "planning-detail (kennis-entiteit, risicomodel, materialiteit, werkprogramma) — zie audit-planning",
        "bewijswerk per procedure (7 ISA-procedures, steekproef, LOR) — zie audit-bewijs",
        "afronding-mechaniek (subsequent events, misstatements-evaluatie) — zie audit-afronding",
        "oordeel-vormen + verslag-stijl — zie controleverklaring",
        "opdracht-type-keuze (controle/beoordeling/samenstelling/AUP) — zie opdracht-types",
        "commissaris-statuut + onafhankelijkheid — zie beroepsbeoefening-cluster"
      ]
    },
    "provenance": { ... }
  },
  "inhoud": { ... },
  "relaties": [ ... ]
}
```

## Wat NIET in scope van deze ADR

Bewuste uitsluitingen:

- **Geen link-integriteit-check** — `scope.out`-strings worden niet gevalideerd tegen record-ids (geen pre-commit-hook in `audit_parity`). Vrije tekst, mensen-leesbaar, LLM-leesbaar; broken references zijn een mapping-fase-aandachtspunt, geen schema-constraint.
- **Geen render-laag-functionaliteit** — `scope.out` is geen render-input. Eventuele "Niet hier, zie ginder"-blokken in fiches komen via cross-references in `inhoud`-tekst, niet via scope-metadata.
- **Geen schema-versie-bump** — dit is een additieve, niet-breaking uitbreiding aan schema 2.1 v1.5. Geen migratie nodig; bestaande records zonder `scope`-veld blijven valide.
- **Geen verplichte invul-discipline** — operatie-prompts (in `prompts/operaties/`) kunnen scope-velden lezen wanneer aanwezig, maar dwingen ze niet af. Wordt geleidelijk ingevuld tijdens mapping-fase + nieuwe records (kandidaten uit skelet-werk).

## Operationeel — invul-richtlijn

- **Tijdens cluster-sparring (skelet-werk)**: per record uit het cluster expliciet formuleren wat scope-in + scope-out is. Dit bestaat al in `docs/granulariteit-skelet.md` (cluster-secties met sub-secties + "schrappen-als-eigen-record"-lijsten + "cross-cluster"-lijsten); mapping-fase exporteert deze naar `metadata.scope.in`/`out`.
- **Nieuwe records (post-skelet)**: agent vult scope-velden in tijdens initiële `skeleton`/`beschrijven`-operatie, gebaseerd op cluster-context.
- **Bestaande records (mapping-fase)**: scope-velden worden toegevoegd wanneer record in scope komt voor herstructurering. Niet retroactief op alle 396 records ineens.

## Smell-detectie tijdens mapping

Tijdens mapping-fase scant agent op patronen die scope-violations signaleren:

- **"X-fiscaal" / "X-juridisch"-record-namen** = perspectief-vermomming (geformaliseerd in skelet-rationale-log 2026-05-26). Zelfde fenomeen × andere werk-as = `accountant_perspectieven[]`, niet apart record.
- **Suffix-naam-smells** (`-cluster`, `-rechtsvorm`, `-ic`, `-fiscaal`) = schema-categorie-marker in id (zie granulariteit-skelet rationale-log 2026-05-26).
- **`en`-naam-smell** = chapter-heading-overerving of 2 fenomenen geforceerd samen (zie granulariteit-skelet rationale-log 2026-05-24).

Records die deze smells dragen worden bij mapping-fase her-overwogen — scope-velden helpen scheiden wat bij elkaar hoort en wat niet.

## Wat dit oplost

| Probleem (pre-ADR) | Oplossing |
|---|---|
| Extractie-LLM dupliceert content tussen verwante records | `scope.out` als negatieve guidance — "dit hoort hier niet" |
| Versnipperde records waar één onderwerp in meerdere fiches landt | `scope.in` als afbakening tijdens cluster-sparring → consolidatie pre-extractie |
| Geen materiële brug tussen skelet-sparring en records-uitvoering | Cluster-sparring-tekst (in/out per record) wordt machine-leesbaar in metadata |
| Reviewer kan niet snel zien wat een record wel/niet behandelt | Eén veld om bij audit te checken |

## Niet-doelen voor toekomstige uitbreiding

Mogelijke uitbreidingen die NIET in deze ADR vastgelegd zijn:

- Render-laag rendert `scope.out`-blok onderaan fiche (kan later, maar geen vereiste)
- `audit_parity` valideert `scope.out`-referenties (kan later, maar geen vereiste)
- Aparte operatie `scope_invullen` (kan, maar `beschrijven` / `kandidaat_review` kunnen dit subsumeren)
- Strikt gestructureerde scope (`{topic, zie}` objects) — bewust afgewezen voor eenvoud
