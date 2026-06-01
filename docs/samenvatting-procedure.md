# Samenvatting-procedure — hoe maak je een PO-samenvatting?

**Voor**: Opus (design + delegatie) of een mens die voor een PO een **geheugen-kapstok** wil bouwen — printbaar op 2-4 A4, voor herhaling in de week vóór het examen.

**Canoniek**: [ADR-039](adr/ADR-039-samenvatting-vervangt-themafiche.md) (vervangt cluster-themafiches per ADR-036 door PO-samenvattingen). Schema POC-status; consolideren in ADR-040 of amendement na 2-3 PO's.

**Wanneer relevant**: nadat de leerstukken voor een PO klaar zijn. Eventueel parallel met of na de oefening (volgorde maakt niet uit; de twee zijn onafhankelijk).

**Gold-standard**: PO 1.4 ([`data/samenvattingen/1-4.yaml`](../data/samenvattingen/1-4.yaml) + [`content/studiemateriaal/1-4/samenvatting.md`](../content/studiemateriaal/1-4/samenvatting.md)).

---

## Waarom een samenvatting (vs themafiche)?

Tot ADR-039 leefden themafiches op **cluster-niveau** (één per concept-cluster). PO 1.8 bracht dat naar 4 themafiches voor één PO — versnipperd voor examen-voorbereiding. Een student wil **één** kapstok per examen-onderdeel.

De samenvatting bouwt voort op de themafiche-stijl (visueel-dominant, tabellen + beslisboom + formules + valkuilen) maar:
- Scope = PO, niet cluster (één samenvatting per PO)
- Locatie = `content/studiemateriaal/<po-slug>/samenvatting.md` (binnen het leerpad — self-contained PO-folder)
- Cap = **2-4 A4 printbaar** (was 1-2)
- Bron = YAML-script (was: handgeschreven markdown)

---

## Drie pijlers van een goede samenvatting

1. **Visueel-dominant.** Tabellen, beslisbomen, formules. Geen doorlopend proza. Wat niet in een tabel past, hoort waarschijnlijk in een leerstuk.
2. **Printbaar op 2-4 A4.** Wat niet past, hoort in een leerstuk of concept-fiche. Doel: in één avond herhalen, op de trein doorlopen.
3. **Wijst niet uit het PO.** Doorklik naar leerstukken (binnen PO) en concept-fiches mag; wikilinks naar leerstukken in *andere* PO's vermijden — die context heeft de student niet bij examen-voorbereiding.

---

## Stappen (bij PO N afgerond)

### Stap 1 — Ontwerp de blok-structuur

Vier verplichte blokken + optionele "select what fits":

| Blok | Verplicht? | Voor wat? |
|---|---|---|
| Intro-callout | ✅ | "kapstok voor herhaling, niet om voor het eerst te leren" |
| Take-away | ✅ | 3-6 scherpe insight-bullets (niet wat in tabellen terugkomt) |
| Vergelijkingsmatrix | optioneel | PO's met methode-/regime-keuze (1.4 consolidatie, 2.6 successie-stelsels, ...) |
| Beslisboom (mermaid) | optioneel | PO's met procedure / "welke X bij Y"-vraag |
| Drempels + formules | optioneel | PO's met wiskundig kerngeld (kostprijs, ratios, drempels) |
| Verbinding met examen | optioneel | Patroon-observatie + pointer naar voorbeeldexamen-pagina |
| Valkuilen | ✅ | 3-koloms tabel (Valkuil · Wat klopt niet · Wat klopt wel) of bullet-lijst |
| Verdieping (doorklik) | ✅ | Leerstukken (binnen PO) + concept-fiches gegroepeerd per functie |

Werk in pen-en-papier eerst de structuur uit: welke optionele blokken levert de PO-stof? Een goede samenvatting heeft 4-6 blokken in totaal (de 4 verplichte + 0-2 optionele).

### Stap 2 — YAML-script

**Hoe**: maak `data/samenvattingen/<po-slug>.yaml` (bv. `1-8.yaml`). Volg [`data/samenvattingen/SCHEMA.md`](../data/samenvattingen/SCHEMA.md). Gebruik `data/samenvattingen/1-4.yaml` als template.

**Sectie-structuur**:
- `meta` (slug = po-code-met-streepje, titel, po, beschrijving, explorer_title, print_a4)
- `intro.callout_beat`
- `take_away.bullets`
- `extra_blokken[]` (in render-volgorde — type bepaalt vorm)
- `valkuilen` (format: tabel of bullets)
- `doorklik` (leerstukken + concept_groepen)
- `footer`

**Voor PO's die uit themafiches gemigreerd worden**: pak alle bestaande cluster-themafiches voor dit PO + extracteer de scherpste tabellen/diagrammen/valkuilen. Wat dubbel staat → merge. Wat alleen kleine subgroep raakt → naar concept-fiche of leerstuk.

### Stap 3 — Render naar markdown

**Twee opties**:

- **Hand-rendered** (aanbevolen voor kleine wijzigingen + reverse-engineering uit bestaande themafiche): open de YAML, render manueel naar `content/studiemateriaal/<po-slug>/samenvatting.md`. Geen agent-overhead. Volg de regels in [`prompts/samenvatting-render-v1.md`](../prompts/samenvatting-render-v1.md).

- **Via Sonnet-agent**: gebruik [`prompts/samenvatting-render-v1.md`](../prompts/samenvatting-render-v1.md) als prompt-template. **Call-budget verplicht < 3 RAG-calls** (claims zijn al door leerstukken bevestigd). Voor kleine fixes (rij toevoegen, beat herformuleren): doe het via Edit op zowel YAML als markdown.

**Belangrijke render-regels** (volledig in `prompts/samenvatting-render-v1.md`):
- Automatische H2-nummering (1 Take-away, 2..N extra_blokken, N+1 Valkuilen, N+2 Verdieping)
- Mermaid horizontaal (LR) voor stappenplannen; TD voor beslisbomen
- `<div class="no-print">` voor intro-callout en Verdieping-sectie
- Wikilinks binnen PO: `[[<leerstuk-slug>]]`; minicursus: `[[studiemateriaal/<po-slug>|minicursus PO <po>]]`

### Stap 4 — Integratie

1. **Minicursus § "Voor de herhaling — samenvatting"** in `content/studiemateriaal/<po-slug>/index.md` — korte motivering + wikilink:
   ```markdown
   ### Voor de herhaling — samenvatting

   Wanneer je de stof grondig gezien hebt en het examen nadert: de **samenvatting** is een kapstok op enkele A4 (printbaar) met vergelijkingstabel, beslisboom, formules en klassieke valkuilen. Niet bedoeld om voor het eerst te leren.

   → [[studiemateriaal/<po-slug>/samenvatting|Samenvatting PO X.Y — <titel>]] (2-4 A4, printbaar)
   ```

2. **Frontmatter van `samenvatting.md`**:
   - `tags: [samenvatting, po-X.Y]`
   - `explorer_title: "7. Samenvatting"` (of welke positie volgt op de leerstukken + oefening)

3. **Update [`docs/leerstuk-status.md`](leerstuk-status.md)**: kolom "Samenvatting" voor de PO naar ✅ + pointers.

4. **Wikilinks van leerstukken**: in elk leerstuk-YAML/markdown `verder_lezen` → wikilink naar `[[studiemateriaal/<po-slug>/samenvatting|Samenvatting PO X.Y]]` i.p.v. `[[themafiches/<oude-slug>]]`.

5. **Bestaande cluster-themafiches voor dit PO**: verwijderen of redirect-noot toevoegen (afhankelijk van of ze cross-PO refs hebben). Per ADR-039.

---

## Wat NIET doen

- **Geen verhalende secties**. Geen "Inleiding tot consolidatie" — daarvoor zijn de leerstukken. Samenvatting = tabellen + bullets + formules.
- **Geen wetsartikelen letterlijk**. Pointers volstaan ("WVV art. 1:26"). De wettekst kennen is iets dat de stagiair via ITAA-LEX bij examen kan opzoeken.
- **Geen drempelbedragen hardcoded**. Verwijs naar Cijferzakboekje of tarief-record. Tarieven veranderen.
- **Geen losse cluster-themafiches meer maken**. Cross-cluster themafiches die meerdere PO's raken (zoals `boekhoudplicht-en-rechtsbronnen`) blijven voorlopig op cluster-niveau tot de PO's die ze raken een leerpad krijgen. Zie ADR-039 § "Cross-cluster themafiches".

---

## Open punten voor latere PO's

- **Print-CSS** voor samenvatting (`@media print` styles in Quartz) — al deels aanwezig via `.no-print` klassen
- **Cross-PO referentie-fiches** (gedeeld tussen 1.1 en 1.2, of tussen 1.4 en 1.5): per geval beslissen — incorpereren of behouden als uitzondering
- **Deterministische renderer** (Python script i.p.v. agent): kandidaat zodra het schema stabiel is over 3-5 PO's
- **Schema-versionering**: SCHEMA.md is v0.1 POC. Consolideren in ADR-040 of amendement ADR-039 na ervaring met 2-3 PO's
