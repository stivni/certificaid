# ADR-041 — Rename leerpaden → studiemateriaal + minicursus → overzicht (UI)

**Status**: Accepted (2026-06-01)
**Gerelateerd**: ADR-036 (drie-lagen leermateriaal — definieert "minicursus") · ADR-037 (leerstuk-laag) · ADR-039 (samenvatting) · ADR-040 (voorbeeldexamenvragen-positie binnen leerpad-folder)

## Context

Twee onafhankelijke terminologie-knelpunten kwamen samen in één design-pass:

1. **Folder-naam `content/leerpaden/` was niet meer dekkend.** Sinds ADR-040 bevat elk PO-folder vijf soorten content: overzicht (was: minicursus), leerstukken, samenvatting, oefening, voorbeeldexamenvragen. "Leerpad" suggereert *één* lineair pad. "Studiemateriaal" dekt de hele inhoud van de folder.

2. **De UI-term "minicursus" was te lang en te specifiek.** In de Quartz-explorer sidebar leidde "minicursus" tot lange explorer-titels (`PO 1.4 — Geconsolideerde jaarrekening · minicursus`). De pagina is feitelijk een *overzicht* van het PO; de term "minicursus" voegt geen informatie toe voor de student.

## Beslissing

### 1. `content/leerpaden/` → `content/studiemateriaal/`

Volledige rename. Raakt:

- Directory (`git mv content/leerpaden content/studiemateriaal`)
- Alle wikilinks/markdown-paden in `content/`, `docs/`, `tools/`, `prompts/`, `quartz.layout.ts`, `CLAUDE.md` (129 files)
- Interne Python-symbolen (`LEERPADEN_DIR` → `STUDIEMATERIAAL_DIR` in `tools/examen/render_merged_v4.py`)
- ADRs en docs die paden noemen — geüpdatet in dezelfde commit

De Nederlandse term "leerpad" (singular, als concept) blijft toegestaan in prose waar het bedoeld is als "leerroute door de stof" — los van de directory-naam.

### 2. UI: "minicursus" → "overzicht" (alleen UI, interne term blijft)

**Aangepast (UI-laag)**:
- Page bodies: `# Minicursus PO 1.4 ...` → `# Overzicht PO 1.4 ...`
- Frontmatter `title:` waarden
- Frontmatter `tags: [minicursus, ...]` → `tags: [overzicht, ...]`
- `tags: [minicursus-mockup]` → `tags: [overzicht-mockup]`
- Render-template output (`tools/leermateriaal/lib/frontmatter.py` output-tag)
- Grammar-aanpassingen: "deze/elke/de minicursus" (vrouwelijk) → "dit/elk/het overzicht" (onzijdig)

**Behouden (interne laag)**:
- ADRs (ADR-036, ADR-037, ...) gebruiken "minicursus" als technische term
- `docs/minicursus-schrijfregels.md` — bestandsnaam en titel blijven
- `prompts/*-v1.md` — instructies aan agents blijven "minicursus" gebruiken
- Python function-names (bv. `minicursus_frontmatter`) en interne variabelen

Dit hybride pad voorkomt een wave van prompt-/ADR-/code-rename. De UI heeft prioriteit (de student ziet het); de interne term blijft stabiel voor agent-instructies.

### 3. Korte `explorer_title` op alle 19 PO-index-pagina's

Vóór ADR-041 had alleen PO 1-3/1-4/1-8/1-9 een korte `explorer_title` (bv. "1.4 Consolidatie"). De andere 15 PO's vielen terug op de lange `title` ("PO 2.4 — Belasting over de toegevoegde waarde · minicursus"), wat de Quartz-sidebar onleesbaar maakte.

Canonieke korte labels (alle 19):

| Slug | Label |
|---|---|
| 1-1 | `1.1 Boekhouding` |
| 1-2 | `1.2 Boekhoudrecht` |
| 1-3 | `1.3 Analyse jaarrekening` |
| 1-4 | `1.4 Consolidatie` |
| 1-5 | `1.5 IFRS & EU` |
| 1-6 | `1.6 Externe controle` |
| 1-7 | `1.7 Interne controle` |
| 1-8 | `1.8 Analytische boekhouding` |
| 1-9 | `1.9 Financiële analyse` |
| 2-1 | `2.1 Fiscaal recht` |
| 2-2 | `2.2 Personenbelasting` |
| 2-3 | `2.3 Vennootschapsbelasting` |
| 2-4 | `2.4 BTW` |
| 2-5 | `2.5 Fiscale procedure` |
| 2-6 | `2.6 Registratie & successie` |
| 2-7 | `2.7 Gewest & gemeente` |
| 2-8 | `2.8 Internationaal fiscaal` |
| 3-0 | `3.0 Vennootschapsrecht` |
| 4-0 | `4.0 Deontologie & AML` |

Pattern: `<po-code> <2-3 woord label>`. Officiële afkortingen (BTW, AML) zijn OK in explorer-context (CLAUDE.md regel 8 staat afkortingen toe in user-facing gesprek; explorer-sidebar telt mee).

## Gevolgen

**Pluspunten**:
- Quartz-sidebar wordt scanbaar (alle PO's op één regel met code + thema)
- Folder-naam dekt zijn inhoud
- "Overzicht" leest natuurlijk voor de student; "minicursus" suggereerde meer dan de pagina levert (geen cursus, wel een verhaal + routekaart)
- Interne stabiliteit voor agents (prompts blijven werken)

**Minpunten**:
- Tijdelijke inconsistentie: UI zegt "Overzicht", docs/prompts zeggen "minicursus". Documentatie maakt dit expliciet (CLAUDE.md wegwijzer + ADR-040/041).
- 240+ files aangeraakt in één commit — eenmalige migratie-cost.

## Migratie (uitgevoerd 2026-06-01)

1. `git mv content/leerpaden content/studiemateriaal`
2. Regex-sweep `\bleerpaden\b` → `studiemateriaal` over content/, docs/, tools/, prompts/, quartz.layout.ts, CLAUDE.md
3. Regex-sweep `[Mm]inicursus` → `[Oo]verzicht` over `content/` (UI only)
4. Plural-fix `overzichtsen` → `overzichten`
5. Grammar-fix `deze/elke/de overzicht` → `dit/elk/het overzicht` (onzijdig)
6. Python-script-injectie van `explorer_title` voor alle 19 PO-index-files (idempotent: replace bestaande of insert na `description:`)
7. `tools/examen/render_merged_v4.py` interne symbool-rename + path-update
8. `quartz.layout.ts` sortFn `order` array: `"leerpaden"` → `"studiemateriaal"`

Build verified groen (`npx quartz build`).

## Open punten

- **Page-title suffix** "· overzicht" in frontmatter (bv. `PO 1.4 — ... · overzicht`) is redundant nu we ADR-040 hebben (folder-context geeft het al). Mogelijk schrappen in volgende ronde; niet kritisch.
- **`docs/minicursus-schrijfregels.md`-rename** — bestandsnaam behoudt "minicursus" als interne identifier. Hernoemen vereist update van wegwijzer-links in CLAUDE.md + ADR-036; nu niet gedaan.
