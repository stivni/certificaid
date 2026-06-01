# PO-uitbouw-procedure — hoe pak je een nieuw PO aan?

**Voor**: Opus (design + delegatie) of een mens die een nieuwe PO wil uitbouwen tot een volledig studiemateriaal-pakket — overzicht + leerstukken + samenvatting + oefening + voorbeeldexamenvragen.

**Canoniek**: [ADR-036](adr/ADR-036-drie-lagen-leermateriaal.md) (drie-lagen model — overzicht/themafiche/concept) · [ADR-037](adr/ADR-037-leerstuk-vierde-leerlaag.md) (leerstuk-laag tussen overzicht en concept) · [ADR-039](adr/ADR-039-samenvatting-vervangt-themafiche.md) (samenvatting vervangt themafiche) · [ADR-040](adr/ADR-040-voorbeeldexamenvragen-in-leerpadstructuur.md) (voorbeeldexamenvragen in leerpad-folder).

**Resulterende folder** (canoniek, per ADR-040): `content/studiemateriaal/<po-slug>/` met als kinderen:
1. `index.md` — overzicht (was: minicursus, naam in UI sinds rename)
2. `<leerstuk-slug>.md` × N — één per didactische vraag
3. `samenvatting.md` — geheugen-kapstok printbaar
4. `oefening.md` — actieve doorwerk-case
5. `voorbeeldexamenvragen.md` — auto-gegenereerd uit examen-pijplijn

**Terminologie**: in de UI heet `index.md` "overzicht" (per rename 2026-06-01). In docs/prompts/ADRs blijft de interne term **minicursus**. Bij verwijzing in deze procedure gebruik ik de interne term — page-bodies en headers schrijf je met "Overzicht".

---

## Stap 0 — Voorkennis

Alvorens te starten, zorg dat je:
- ADR-037 + leerstuk-schrijfregels gelezen hebt
- De gold-standard van PO 1.4 hebt bekeken (`content/studiemateriaal/1-4/index.md` + de 5 leerstukken)
- Toegang hebt tot de drie MCP-servers (`certificaid-rag`, `certificaid-tarieven`) — anders mis je bron-verificatie

---

## Stap 1 — Skelet (één Opus-pass)

**Doel**: voorstel voor minicursus + leerstukken in één gedachtegang, op basis van het officiële examenprogramma.

**Hoe**: gebruik [`prompts/leerpad-skelet-v1.md`](../prompts/leerpad-skelet-v1.md). Vul `<<PO_CODE>>`, `<<PO_SLUG>>`, `<<PO_TITEL>>` in en lance een Opus-sessie.

**Output**: `docs/leerpad-skelet-<po-slug>.md` met:
- Programma-analyse (taken, doelstellingen, kern vs rakend)
- Voorbeeldexamen-patronen
- Voorgestelde leerstukken (slug, vraag, type, dekking, concepten, rationale)
- Gap-check (matrix taak/doelstelling × leerstuk)
- Minicursus-skelet (5 secties)
- Voorbeeldgroep-voorstel
- Themafiche-mapping
- Open vragen voor sparring

**Beslismoment (sparring met gebruiker)**:
- Aantal leerstukken (granulariteits-stelregel: eerder samen dan splitsen)
- Welke voorbeeldgroep — nieuwe of hergebruiken bestaande
- Welke wikilink-grafiek tussen leerstukken (wie verwijst naar wie?)
- Welke gaten zijn echte gaten en welke "raken andere PO's" — beslis welke later in een ander PO landen

---

## Stap 2 — Voorbeeldgroep-data

**Doel**: één centrale data-bron die door alle leerstukken in dit PO wordt geconsumeerd.

**Hoe**: maak `data/voorbeeldgroepen/<naam>.yaml`. Gebruik `data/voorbeeldgroepen/aurelia.yaml` als template — het patroon is gevalideerd voor PO 1.4.

**Inhoud (variabel per PO-type)**:
- Beschrijving + balansdatum + boekjaar
- Groepsstructuur (indien relevant: rechtspersoon, %-en, controle-niveaus)
- Mermaid-diagrammen
- Balansen (voor en na bewerking, indien relevant)
- Resultatenrekening
- Boekingen (T-rekening-stijl, één per relevante verrichting)
- Mock geconsolideerd / mock-eindresultaat
- Drempel-tabellen / vergelijking-tabellen voor PO-specifieke regels
- Mini-cases voor sub-onderwerpen

**Belangrijk**: cijfers moeten intern consistent zijn (totaal activa = totaal passiva, Σ debet = Σ credit). Mock is fictief maar moet kloppen.

---

## Stap 3 — Scripts per leerstuk

**Doel**: voor elke voorgestelde leerstuk een YAML-script schrijven dat de didactische structuur vastlegt.

**Hoe**: gebruik [`prompts/leerstuk-scripts-v1.md`](../prompts/leerstuk-scripts-v1.md) — canonical prompt sinds [ADR-037 §"Amendement 2026-05-31"](adr/ADR-037-leerstuk-vierde-leerlaag.md). **Eén Opus-agent** schrijft alle scripts van het PO in één run (verhaal-cohesie + hand-offs). Bron-discipline: programma + concept-records + wettekst (via MCP) primair; skelet is hypothese die ge-revalideerd mag worden; themafiches zijn secundair. Schrijf één YAML per leerstuk in `data/leerstukken/<slug>.yaml` volgens [`data/leerstukken/SCHEMA.md`](../data/leerstukken/SCHEMA.md).

**Inhoud**:
- `meta` (slug, titel, po, cluster, voorbeeldgroep-ref, beschrijving)
- `intro.callout_beat` (instructie voor de intro-paragraaf)
- `antwoord_in_een_blik` (beats + optioneel visualisaties)
- `opbouw` (lijst secties met niveau + beats + visualisaties + optioneel `kinderen`)
- `verder_lezen` (leerstukken + themafiches + concepten doorklik)
- `wettelijk_fundament` (per claim: onderwerp + ref + optioneel noot)
- `footer`

**Schrijf-discipline**:
- Beats in mensentaal als instructies aan de renderer, niet als prose-slots
- Sectie-types: `sectie` (default, krijgt heading) · `blockquote-aside` (intro vet + prose, geen heading) · `intro-callout` (no-print)
- Visualisatie-refs naar `voorbeeldgroep.<categorie>.<key>` of inline kolommen+rijen
- **Concretiseringsregel** (schrijfregels #10): abstracte stellingen krijgen een mini-voorbeeld in de beats zelf

**Sanity-check vóór render**: alle visualisatie-refs bestaan in de voorbeeldgroep, alle wikilinks wijzen naar bestaande targets (of zijn bewust voorlopig — markeer dan).

---

## Stap 4 — Render per leerstuk (Sonnet-agent)

**Doel**: van YAML-script naar markdown-leerstuk via een Sonnet-uitvoeringsagent met verplichte RAG-bron-verificatie.

**Hoe**: gebruik [`prompts/leerstuk-render-v1.md`](../prompts/leerstuk-render-v1.md). Vul placeholders in:
- `<<OUTPUT_PATH>>` — `content/studiemateriaal/<po-slug>/<slug>.md` (PO-specifiek) of `content/leerstukken/<slug>.md` (cross-PO)
- `<<SLUG>>`, `<<VOORBEELDGROEP>>`, `<<SPECIFIEKE_CLAIMS_OM_TE_VERIFIËREN>>`

Lance met `Agent` (`subagent_type: general-purpose`). Parallel-rendering van meerdere leerstukken kan: meerdere `Agent`-calls in één bericht (run_in_background voor latere collection).

**Wat je krijgt terug**:
- Gegenereerde markdown op het output-pad
- Rapport (~10 bullets): word count, RAG-calls, bevestigde claims, weerleggingen, visualisaties, beats-samenvoegingen, pedagogische gaps

**Wat te doen met weerleggingen**:
- Update het script-YAML met de bevestigde wetsverwijzing
- Eventueel: noteer voor concept-laag-opkuis indien een concept-record fout zat

**Wat te doen met pedagogische gaps**:
- Beoordeel of het script uitbreiding nodig heeft (extra beats of secties)
- Bij meerdere gaps over leerstukken heen: schrijfregels-update of beats-vocabularium-uitbreiding

---

## Stap 5 — Minicursus (`index.md`)

**Doel**: de minicursus schrijven die naar de leerstukken verwijst, vertrekkend uit het skelet.

**Hoe**: handmatig schrijven of via een Sonnet-agent (analoog aan leerstuk-render, maar zonder script — wel met skelet-document als input).

**Structuur** (canoniek, sinds 1.4 samenvoeging §3+§4):

1. **Waarom dit vak?** — Motivatie + bredere-programma-tabel
2. **Wat is dit vak?** — Verhaal in compacte sub-secties, elk eindigend met wikilink naar het relevante leerstuk
3. **Wat moet je kunnen + hoe pak je het aan** — Leerstukken-leesroute (4-7 stappen) + themafiche-noot
4. **Examen-radar** — Voorbeeldexamen-tabel + patroon-observatie
5. **Concepten cross-PO** — Tabel met concepten die ook elders relevant zijn

**Wat NIET in de minicursus**:
- Rol-uitwerking per beroep (boekhouder/commissaris/adviseur) — die leeft in de leerstukken zelf via accountant-perspectieven
- Directe concept-wikilinks in §3 — alleen leerstuk-wikilinks
- Wettelijke kaders apart — die zitten in "Wettelijk fundament" van elk leerstuk

**Locatie**: `content/studiemateriaal/<po-slug>/index.md`. Quartz rendert dat als `/studiemateriaal/<po-slug>/` (folder-index).

---

## Stap 6 — Samenvatting (geheugen-kapstok per PO)

**Doel**: één PO-brede samenvatting bouwen — printbaar op 2-4 A4, voor herhaling vlak vóór het examen. Vervangt de oude cluster-themafiches per [ADR-039](adr/ADR-039-samenvatting-vervangt-themafiche.md).

**Hoe**: volg [`docs/samenvatting-procedure.md`](samenvatting-procedure.md):
- YAML-bron in `data/samenvattingen/<po-slug>.yaml` (zie [`data/samenvattingen/SCHEMA.md`](../data/samenvattingen/SCHEMA.md))
- Markdown op `content/studiemateriaal/<po-slug>/samenvatting.md` (hand-rendered of via [`prompts/samenvatting-render-v1.md`](../prompts/samenvatting-render-v1.md))
- Schrijfregels: [`docs/samenvatting-schrijfregels.md`](samenvatting-schrijfregels.md) — telegram-stijl, tabellen/diagrammen/formules dominant

**Indien er voor dit PO al cluster-themafiches bestaan**: merge ze tot één samenvatting volgens § "Migratie uit themafiches" in de schrijfregels. Verwijder de oude `content/themafiches/<cluster>.md`-bestanden in dezelfde commit. Cross-cluster themafiches die meerdere PO's raken blijven voorlopig staan (zie ADR-039 § "Cross-cluster themafiches").

**Gold-standard**: PO 1.4 ([`content/studiemateriaal/1-4/samenvatting.md`](../content/studiemateriaal/1-4/samenvatting.md) + [`data/samenvattingen/1-4.yaml`](../data/samenvattingen/1-4.yaml) — in opbouw).

---

## Stap 7 — Oefening (5e leerlaag)

**Doel**: één PO-brede oefening waarin de student zelf het volledige pad loopt dat de leerstukken passief uitleggen. POC-status (kandidaat ADR-038).

**Hoe**: volg [`docs/oefening-procedure.md`](oefening-procedure.md):
- YAML-bron in `data/oefeningen/<slug>.yaml` (zie [`data/oefeningen/SCHEMA.md`](../data/oefeningen/SCHEMA.md))
- Markdown op `content/studiemateriaal/<po-slug>/oefening.md` via [`prompts/oefening-render-v1.md`](../prompts/oefening-render-v1.md)
- Schrijfregels: 3 pijlers — geen hints in opgave · realistische individuele JR met aparte intra-groep mapping · niet-voorkauwende instructies

**Gold-standard**: PO 1.4 Nordica Holdings ([`data/oefeningen/nordica-consolideren.yaml`](../data/oefeningen/nordica-consolideren.yaml) + [`content/studiemateriaal/1-4/oefening.md`](../content/studiemateriaal/1-4/oefening.md)).

**Optioneel**: oefening kan worden overgeslagen voor PO's waar een 60-75 min doorgewerkte case minder waarde toevoegt dan tijd kost (sommige fiscale PO's). Beslissing per PO; samenvatting is wel verplicht.

---

## Stap 8 — Voorbeeldexamenvragen (auto)

**Doel**: laatste sibling in de leerpad-folder met de geclassificeerde examen-vragen voor dit PO.

**Hoe**: **geen handmatige actie**. Per [ADR-040](adr/ADR-040-voorbeeldexamenvragen-in-leerpadstructuur.md) genereert `python3 -m tools.examen.render_merged_v4` automatisch `content/studiemateriaal/<po-slug>/voorbeeldexamenvragen.md`:
- Gevulde pagina wanneer er vragen geclassificeerd zijn in `data/programma/examen_vragen/_interpretaties/` onder dit PO
- Stub-pagina met `[!info]`-callout "geen vragen geclassificeerd" wanneer leeg (bv. PO 1.8)
- `explorer_title` krijgt automatisch het juiste vervolgnummer (N+1 op basis van bestaande siblings)

**Waar het hand-werk wél zit**: het classificeren van voorbeeldexamen-vragen onder de juiste PO-codes — zie `data/programma/examen_vragen/_interpretaties/` + de prompts in `prompts/examen-*`. Dat is een aparte werklijn (ADR-022/023/024), niet gekoppeld aan PO-uitbouw.

---

## Stap 9 — Integratie + verifieer

**Checks na afloop**:

| Check | Hoe |
|---|---|
| Wikilink-resolution | Open `/studiemateriaal/<po-slug>/` in browser, klik door naar elk leerstuk, klik door naar themafiche en concepten |
| Quartz explorer-sidebar | Toont de hiërarchie minicursus → leerstukken? Korte titels via `explorer_title` frontmatter (vereist Quartz custom plugin — zie `quartz-custom/plugins/emitters/contentIndex.tsx`) |
| RAG-validatie | Alle wetsverwijzingen geverifieerd door render-agent (zie rapport-bullets) |
| Voorbeeldgroep-consistentie | Cijfers kloppen over alle leerstukken heen (geconsolideerd activa = geconsolideerd passiva, etc.) |
| Pre-publicatie-checklist per leerstuk | Volg [docs/leerstuk-schrijfregels.md](leerstuk-schrijfregels.md) §Pre-publicatie-checklist |

---

## Wat NIET in deze procedure

- **Themafiche-creatie of -herziening** wanneer de PO geen bestaande themafiche heeft: aparte werkronde
- **Concept-laag-opkuis** (records dedupliceren, feitelijke correcties): aparte ronde, behandel weerleggingen uit render-rapporten in batch
- **Cross-PO leerstukken** (zoals `individuele-jaarrekening-opmaken` voor 1.1/1.2/1.4): bespreek expliciet in skelet-stap of het cross-PO is. Locatie wordt dan `content/leerstukken/<slug>.md` i.p.v. `content/studiemateriaal/<po>/<slug>.md`

---

## Tijdsindicatie (PO 1.4 als referentie)

| Stap | Tijd | Wie |
|---|---|---|
| 1. Skelet | 30-60 min | Opus (sparring met mens) |
| 2. Voorbeeldgroep-data | 1-2 uur | Mens (creatieve mock met kloppende cijfers) |
| 3. Scripts per leerstuk | ~5-15 min per stuk (Opus-agent) | Eén Opus-agent voor alle scripts van het PO; ~1-2 uur totaal voor 4-7 leerstukken |
| 4. Render per leerstuk | ~3-5 min per stuk; parallel 4 tegelijk via subagenten | Sonnet-agenten |
| 5. Overzicht (`index.md`, intern: minicursus) | 30-60 min | Mens of Sonnet |
| 6. Samenvatting | 1-2 uur (YAML) + ~15 min (render-prompt) | Mens (YAML) + Sonnet-agent (render) |
| 7. Oefening *(optioneel)* | 2-4 uur (YAML met kloppende cijfers) + ~15 min (render) | Mens + Sonnet-agent |
| 8. Voorbeeldexamenvragen | 0 min (auto-render) | Geen — `render_merged_v4.py` produceert de pagina |
| 9. Integratie + verifieer | 30 min | Mens |

**Totaal per PO**: ongeveer 1-2 werkdagen voor een volledig 5-lagen-pakket, afhankelijk van complexiteit + nieuwe vs hergebruikte voorbeeldgroep + of oefening wordt gemaakt.

---

---

## Feedback op een bestaand leerstuk

Wanneer een PO al gerenderd is en je iets wil verbeteren — een beat herformuleren, een visualisatie toevoegen, een wetsfout corrigeren — werk **altijd via het script**, niet rechtstreeks in de markdown.

### Gouden regel

> **Bewerk nooit rechtstreeks de gegenereerde markdown.** Bij de volgende re-render gaat je wijziging verloren. Markdown = output, script = source.

Enige uitzondering: typografische micro-fixes (komma, paragraaf-breek, evidente typo) die je tegelijk in zowel de markdown als het script toevoegt. Bij twijfel: script.

### Workflow per type wijziging

| Type wijziging | Wat doe je in script-YAML | Re-render nodig? |
|---|---|---|
| Pedagogische bijstelling (beat herformuleren, sectie-volgorde) | Edit `opbouw[].beats` of `opbouw[].kinderen[].beats` in `data/leerstukken/<slug>.yaml` | Ja |
| Wetsclaim corrigeren | Edit `wettelijk_fundament` + relevante beats die de claim noemen | Ja |
| Drempel/getal bijwerken | Edit in `data/voorbeeldgroepen/<naam>.yaml` (gedeelde data) | Ja, voor alle leerstukken die de voorbeeldgroep raken |
| Nieuwe visualisatie toevoegen | Edit `opbouw[].visualisaties` + indien nodig nieuwe data in voorbeeldgroep | Ja |
| Sectie toevoegen of structuur wijzigen | Edit `opbouw` (nieuwe entry, niveau, kinderen) | Ja |
| Wikilink-fix (tikfout in slug) | Edit `verder_lezen` of relevante beat met wikilink | Ja |
| Frontmatter veld (title, description, tags) | Edit `meta` in script | Ja |

### Stappen

1. **Identificeer**: welk leerstuk + welk veld? Open `data/leerstukken/<slug>.yaml` en `data/voorbeeldgroepen/<naam>.yaml`
2. **Edit het script**: maak je wijziging in de YAML
3. **Re-render** via [`prompts/leerstuk-render-v1.md`](../prompts/leerstuk-render-v1.md) — Sonnet-agent verwerkt het script + voorbeeldgroep + schrijfregels naar markdown
4. **Verifieer**: bekijk de gerendere markdown op het canonical pad (`content/studiemateriaal/<po-slug>/<slug>.md`). Plus rapport van de agent voor RAG-bevestiging.
5. **Commit beide**: script-YAML + gerendere markdown in één commit. Zo blijft de source-output-sync zichtbaar in git-history.

### Multi-leerstuk feedback

Soms raakt een wijziging meerdere leerstukken (bv. de voorbeeldgroep wijzigen of een terugkerende valkuil herformuleren). Re-render dan **alle geraakte leerstukken** in één werkronde:

```
# 4 subagenten parallel in één bericht (run_in_background)
Agent 1: render wat-is-...
Agent 2: render wie-moet-...
Agent 3: render hoe-...
Agent 4: render goodwill-bij-...
```

Wacht alle vier af, controleer, commit als één pakket.

### Schema- of schrijfregels-wijziging

Verandering aan `data/leerstukken/SCHEMA.md` of `docs/leerstuk-schrijfregels.md` raakt **alle** bestaande leerstukken. Twee paden:

- **Achterwaarts compatibel**: nieuwe field of regel die optioneel is. Geen re-render verplicht; nieuwe leerstukken volgen het patroon.
- **Breekt**: bestaande leerstukken moeten opnieuw. Plan een batch-rerender (alle scripts via 1 ronde Agent-calls). Test met één leerstuk eerst.

### Wijziging aan voorbeeldgroep

Verandering aan `data/voorbeeldgroepen/<naam>.yaml` (bv. nieuwe cijfers, extra mermaid-diagram) raakt elk leerstuk dat de voorbeeldgroep gebruikt. Controleer welke via:

```bash
grep -l "voorbeeldgroep: <naam>" data/leerstukken/*.yaml
```

Re-render die set.

---

## Open punten / nog te verfijnen na meerdere PO's

- **Beats-vocabularium**: formaliseren (introduceer · concretiseer · valkuil · achtergrond-aside · ...) — kandidaat voor appendix in [leerstuk-schrijfregels.md](leerstuk-schrijfregels.md)
- **Render-tool als pre-processor**: Python-script dat YAML-script + voorbeeldgroep → markdown produceert zonder LLM, voor deterministische re-render bij script-wijzigingen. ADR-038 kandidaat.
- **Skelet → script automatisch**: een tweede prompt die het skelet-document leest en concept-scripts genereert (per leerstuk een YAML-skelet met lege beats). Bespaart Stap 3-tijd.
- **Themafiche-schrijfregels-revisie**: zodra ≥3 PO's leerstukken hebben en het overlap-gebied empirisch zichtbaar is.
