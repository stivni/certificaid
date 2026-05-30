# Leerstuk-scripts — v1 (één Opus-agent per PO)

**Doel**: alle leerstuk-scripts (`data/leerstukken/<slug>.yaml`) voor één PO schrijven in **één doorlopende Opus-run**, met zicht op de hand-offs tussen leerstukken.

**Voor**: Stap 3 van [`docs/leerstuk-procedure.md`](../docs/leerstuk-procedure.md). Canoniek sinds [ADR-037 §"Amendement 2026-05-31"](../docs/adr/ADR-037-leerstuk-vierde-leerlaag.md).

**Niet voor**: render-stap (YAML → markdown) — daarvoor `leerstuk-render-v1.md`. Render mag wél parallel per leerstuk.

---

## Waarom één agent

Leerpad + leerstukken vormen één pedagogisch verhaal. Bouwstenen worden in leerstuk N geïntroduceerd en in N+1 als referentie aangeroepen (bv. contributiemarge in leerstuk 2 → fundament van leerstuk 3). Parallelle agents zien elkaars werk niet → dubbele uitleg, broken hand-offs, gemiste cross-links.

Eén Opus-agent met volledige programma + concept + bron-kennis houdt het concept-vocabulair stabiel over de hele PO.

## Bron-discipline (verplicht)

Volgens [ADR-037 §"Amendement 2026-05-31"](../docs/adr/ADR-037-leerstuk-vierde-leerlaag.md), in deze volgorde:

1. **Programma** (`data/programma/programma.json`) — alle kenniselementen, niet de samenvatting
2. **Concept-records** — via MCP `mcp__certificaid-rag__zoek_concepten` + `lees_record`
3. **Primaire bronnen** (wetteksten, CBN-adviezen, ITAA-normen) — via MCP `mcp__certificaid-rag__zoek_bronnen`
4. **Het skelet** — leerstuk-voorstel is sparring-hypothese, mag herzien worden
5. **Voorbeeldgroep** + schrijfregels + schema + bestaande scripts als templates
6. **Themafiches** — secundair, sanity-check only, NIET als spiegel voor leerstuk-structuur

## Standaard prompt-template

Vul placeholders in en lance met `Agent` (`subagent_type: general-purpose`, `model: opus`):

```markdown
Je schrijft alle leerstuk-scripts voor PO <<PO_CODE>> "<<PO_TITEL>>" van het certificaid-project, in één doorlopende run.

## Output

Nieuwe bestanden in `data/leerstukken/`:
<<LIJST VAN SLUGS UIT SKELET, MET RUIMTE VOOR HERZIENING>>

## Stap A — Bron-inventaris (verplicht vóór je schrijft)

### A.1 Programma diep lezen
Lees in `data/programma/programma.json` het volledige blok voor PO <<PO_CODE>> — alle kenniselementen één niveau dieper dan de samenvatting. Maak een inventaris-tabel: per kenniselement, welk leerstuk dekt het primair.

### A.2 Concept-records inladen
Gebruik `mcp__certificaid-rag__zoek_concepten` met PO-zoektermen (zie skelet). Voor elk relevant record: `mcp__certificaid-rag__lees_record`. Noteer slug + definitie + relaties. Deze records zijn de definitorische basis voor wikilinks in `doorklik_concepten`.

### A.3 Primaire bronnen
Gebruik `mcp__certificaid-rag__zoek_bronnen` met wetstermen/CBN-thema's voor dit PO. Noteer welke wetsverwijzingen + CBN-nummers traceerbaar zijn. `wettelijk_fundament`-blokken mogen alleen geverifieerde refs noemen.

### A.4 Skelet-revalidatie
Lees `docs/leerpad-skelet-<<PO_SLUG>>.md`. Het leerstuk-voorstel is een hypothese — herevaluueer op basis van A.1-A.3:
- Dekt het voorstel alle kenniselementen?
- Zijn er kenniselementen die geen natuurlijke plek hebben?
- Is het aantal leerstukken juist gekozen (granulariteits-stelregel: eerder samen)?
- Bij significante afwijking: **rapporteer aan mens VOOR je scripts schrijft**.

### A.5 Secundaire context
- Voorbeeldgroep `data/voorbeeldgroepen/<naam>.yaml` (cijfer-bron)
- `docs/leerstuk-schrijfregels.md`
- `data/leerstukken/SCHEMA.md`
- Templates: `data/leerstukken/wie-moet-consolideren.yaml` (middelzwaar) + `hoe-consolideren.yaml` (zwaarste)
- Themafiches in `content/themafiches/` — **secundair**, alleen ter herkenning. Niet als spiegel-as.

## Stap B — Verhaal-architectuur

Plan voor jezelf:

1. **Concept-vocabulair-flow**: welk concept introduceer je in welk leerstuk, en in welke later aanroepen (zonder opnieuw uitleggen)?
2. **Wikilink-grafiek** tussen de leerstukken: wie verwijst naar wie?
3. **Hand-off-discipline**: aan einde van elk leerstuk een korte verwijzing naar wat het volgende oppakt.

## Stap C — Schrijven (in vaste volgorde, concepten cumulatief bekend)

Schrijf leerstuk 1, dan 2, dan 3, ... — telkens vol uit volgens onderstaande spec per leerstuk.

<<PER LEERSTUK: vraag · type · doelwoorden · programma-dekking · bouwstenen-in · bouwstenen-uit · voorbeeldgroep-blokken · wettelijk-fundament-richting · pedagogisch-kernpunt>>

## Schema + stijl-discipline (uniform)

- Volg `data/leerstukken/SCHEMA.md` strikt
- `meta.cluster`, `meta.po`, `meta.voorbeeldgroep` overal consistent
- Beats in mensentaal als instructies aan de renderer — geen prose-slots
- Concretiseringsregel (schrijfregels §10): abstracte stellingen krijgen mini-voorbeeld met getallen
- Wikilinks: `[[<andere-slug>]]` tussen leerstukken; `[[<concept-slug>]]` voor concept-fiches; `[[themafiches/<slug>]]` voor themafiches

## Sanity-check vóór elke save

1. Elke `visualisaties.ref` bestaat letterlijk in de voorbeeldgroep
2. Elke `wettelijk_fundament.ref` is via MCP `zoek_bronnen` traceerbaar — anders weglaten of `⚠️ te verifiëren`
3. Elke concept-slug in `doorklik_concepten` bestaat in `data/concepten/records/`
4. Elke wikilink naar een broer-leerstuk wijst naar een precies bestaande slug
5. Geen duplicatie van inhoud over leerstukken — één plek voor introductie, elders oproepen

## Rapport (aan einde, max 10 bullets)

- Regelaantal per script-bestand
- Bron-inventaris (concept-records gelezen + MCP-calls + verankerde wettelijke refs)
- Eventuele afwijking van skelet-keuze (welke leerstuk-grens herzien + waarom)
- Concept-flow per leerstuk-paar (één regel)
- Wikilink-grafiek: cross-leerstuk-links per script
- Visualisatie-refs gebruikt
- Doelstellingen-dekking — bevestig dat alle PO-doelstellingen ≥ 1× gedekt zijn
- Wettelijke claims NIET geverifieerd via MCP (vlag voor mens-review)
- Onzekerheden + open punten
- Volgende stap

Begin met Stap A.
```

## Hoe in te zetten

1. Vul placeholders in (PO-code, PO-titel, PO-slug, lijst slugs uit skelet, per-leerstuk-spec uit skelet §3)
2. Lance `Agent` met `subagent_type: general-purpose`, `model: opus`
3. Wacht op rapport. Bij gevlagde skelet-afwijking: sparring met mens vóór scripts goedkeuren
4. Pas dan Stap 4 (render YAML → markdown), kan parallel via Sonnet-agents

## Werkbasis

| Artefact | Locatie | Stap |
|---|---|---|
| Skelet | `docs/leerpad-skelet-<po-slug>.md` | 1 (input voor deze prompt) |
| Voorbeeldgroep | `data/voorbeeldgroepen/<naam>.yaml` | 2 (input voor deze prompt) |
| Scripts | `data/leerstukken/<slug>.yaml` | 3 (output van deze prompt) |
| Markdown | `content/leerpaden/<po-slug>/<slug>.md` | 4 (na render) |
