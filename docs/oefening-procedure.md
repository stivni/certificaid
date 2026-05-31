# Oefening-procedure — hoe maak je een oefening voor een PO?

**Voor**: Opus (design + delegatie) of een mens die voor een PO de 5e leerlaag wil toevoegen — een actieve oefencase waarin de student zelf het volledige pad loopt dat de leerstukken passief uitleggen.

**Canoniek**: POC-status (kandidaat voor amendement op [ADR-036](adr/ADR-036-drie-lagen-leermateriaal.md) of nieuw ADR-038 na 2-3 PO's). Gold-standard: **PO 1.4 Nordica Holdings** ([`data/oefeningen/nordica-consolideren.yaml`](../data/oefeningen/nordica-consolideren.yaml) + [`content/leerpaden/1-4/oefening.md`](../content/leerpaden/1-4/oefening.md)).

**Wanneer relevant**: nadat de leerstukken voor een PO klaar zijn (skelet → scripts → render → integratie afgerond). De oefening is een aanvullende laag, geen vervanging.

---

## Waarom een oefening?

De leerstukken **tonen** de techniek (passieve lezing). Het examen toetst fragmenten — kleine, scoped vragen. Maar die fragmenten landen alleen scherp als de student één keer het hele pad heeft afgelegd. De oefening is die actieve doorloop: opgave + werkpapier-data → student doet → modelantwoord in `<details>`-blok openen ter controle.

Verwacht **niet** dat de oefening lijkt op een echte examen-vraag — examen-vragen leven in `content/voorbeeldexamens/po-<code>.md`. De oefening is groter (60-75 min) en didactisch breder.

---

## Drie pijlers van een goede oefening

1. **Geen hints in de opgave.** Antwoorden op stap N mogen NIET zichtbaar zijn in de opgave-data van stap N. Eerste-versie-valkuil: een "Herwaardering"-kolom in de overname-tabel toont stap 2 voor de student begint. Verplaats die kolom naar de `uitwerking_visualisaties`. Idem voor EV-uitsplitsing, "(na herwaardering)"-labels, "boekw. X → reële Y"-tooltips.

2. **Realistische individuele jaarrekeningen.** ★-markers en "waarvan op verbonden onderneming"-uitsplitsingen op de balans zijn een didactische cheat — die staan niet op een echte KB-WVV-balans. Specifieke dochter-namen leven in de toelichting (Staat C), niet op de balans. Intra-groep data hoort in een aparte sectie **"Intra-groep mapping"** (consolidatie-werkpapier) die het centraal consolidatiebureau opbouwt uit specifieke grootboek-rekeningen voor verbonden vennootschappen (MAR 28/41/44/60/70-detail) + het rapporteringspakket dat dochters aanleveren.

3. **Instructies leidend, niet voorkauwend.** Een instructie als "(c) Intra-groep verkoop + nog-niet-gerealiseerde marge in voorraad — let op slechts 50% doorverkocht" is een verkapt antwoord. Vervang door: "Identificeer de intra-groep stromen. Wees alert bij de intra-groep verkoop — niet alles wat verkocht is, is voor de groep een echte transactie." Student moet zelf de drie families herkennen + de marge-correctie zelf zien.

---

## Stappen (bij PO N afgerond)

### Stap 1 — Ontwerp de mini-case

**Doel**: bedenk een kleinere mock dan de voorbeeldgroep van de PO-leerstukken (in 1.4 is Aurelia de leerstuk-groep; voor de oefening kwam Nordica — bewust kleiner, één moeder + één dochter, één intra-transactie).

**Granulariteits-stelregel**: één pad volledig doorlopen >> meerdere paden oppervlakkig. Een oefening dekt typisch:
- Eén methode in detail (bv. integrale consolidatie voor 1.4) — niet alle drie
- 4-6 stappen die samen één samenhangend doorgewerkt antwoord opleveren
- 60-75 min studietijd

**Cijfers fixeren**: kies *ronde* cijfers die mooi uitkomen. Eindbalansen moeten kloppen (Σ activa = Σ passiva). Tussenstappen moeten consistent zijn met eindresultaat. Werk de oplossing zelf eerst uit met pen en papier voor je de opgave schrijft.

### Stap 2 — YAML-script

**Hoe**: maak `data/oefeningen/<slug>.yaml`. Volg [`data/oefeningen/SCHEMA.md`](../data/oefeningen/SCHEMA.md) voor het schema. Gebruik `data/oefeningen/nordica-consolideren.yaml` als template.

**Sectie-structuur**:
- `meta` (slug, titel, po, cluster, beschrijving, studietijd, niveau)
- `intro.callout_beat` (verplichte "doe-eerst-zelf"-instructie)
- `opgave` (scenario_beats, groep, tabellen, balansen, resultatenrekening, intra_groep_mapping)
- `stappen` (per stap: instructie_beats, uitwerking_beats, uitwerking_visualisaties, valkuil_beat)
- `afsluiting` (reflectie_beats, doelstellingen_gedekt, valkuilen_geoefend)
- `verder_lezen`, `wettelijk_fundament`, `footer`

**Wat in de opgave hoort**: alleen data die een ECHTE consolidator/accountant zou krijgen (zonder antwoorden). Wat in de uitwerking hoort: de berekeningen, de tabellen-met-resultaten, de boekingen.

### Stap 3 — Render naar markdown

**Twee opties**:

- **Hand-rendered** (aanbevolen bij kleine wijzigingen): open de YAML, render manueel naar `content/leerpaden/<po-slug>/oefening.md`. Geen agent-overhead. Volg de regels in [`prompts/oefening-render-v1.md`](../prompts/oefening-render-v1.md) — opgave H2 + uitwerking H2 met `<details>`-blokken per stap.

- **Via Sonnet-agent**: gebruik [`prompts/oefening-render-v1.md`](../prompts/oefening-render-v1.md) als prompt-template. **Call-budget verplicht < 5 RAG-calls** (lessons learned uit leerstuk-render-batches — agenten kunnen ontsporen). Voor kleine fixes (titel-tweak, beat-herformulering): doe het via Edit, niet via agent.

**Belangrijke render-regels** (volledig in `prompts/oefening-render-v1.md`):
- Blank line vóór én na `<details>` en `</details>` (Quartz-quirk anders gaan tabellen erin stuk)
- `<details><summary><strong>Oplossing — klik om te tonen</strong></summary>` exact format
- Boekingen in 5-koloms CBN-stijl (kolom "aan" + MAR + Omschrijving + Debet + Credit) — zelfde template als leerstuk-render
- Wikilinks: `[[leerpaden/<po-slug>|minicursus PO <po>]]`, `[[<leerstuk-slug>]]`, `[[themafiches/<cluster>|Themafiche]]`

### Stap 4 — Integratie

1. **Minicursus § 6** in `content/leerpaden/<po-slug>/index.md` — korte motivering-paragraaf + wikilink met studietijd-indicatie:
   ```markdown
   ## 6. Oefening — actief testen

   Het examen zal nooit de volledige <onderwerp> laten doen — maar het toetst wel fragmenten die je alleen scherp herkent als je het hele pad één keer hebt afgelegd. Voor wie de leerstukken doorgenomen heeft en wil testen of het écht zit, is er een mini-case waar je zelf <onderwerp> uitvoert: van <eerste stap> tot <eindresultaat>.

   → [[oefening|Oefening: <Case-naam>]] (60-75 min)
   ```

2. **Frontmatter van `oefening.md`**:
   - `tags: [oefening, po-<po>, cluster-<cluster>, studietijd-<60-75min>]`
   - `explorer_title: "6. Oefening"`

3. **Update [`docs/leerstuk-status.md`](leerstuk-status.md)**: kolom "Oefening" voor de PO van — naar ✅.

---

## Wat NIET doen

- **Niet automatisch een oefening voor elke PO maken.** Sommige PO's lenen zich er minder voor (vooral pure begripsvakken zoals deontologie). Beoordeel per PO of een doorgewerkte case didactische meerwaarde heeft.
- **Niet meerdere oefeningen per PO stapelen.** Eén goede oefening per PO. Als de stof te breed is, knip de PO desnoods op (cross-PO leerstuk-strategie) — niet de oefeningen vermeerderen.
- **Niet de oefening verwarren met examen-format.** De oefening is groter en didactischer. Examen-vragen leven in `content/voorbeeldexamens/po-<code>.md`.
- **Niet hand-renderen vergeten te updaten als YAML wijzigt.** Markdown = output, YAML = source. Zelfde gouden regel als bij leerstukken.

---

## Open punten / volgende iteraties

- **Schema-versionering**: SCHEMA.md is v0.1 POC. Na 2-3 PO's: consolideren in ADR-038 of amendement ADR-036.
- **Hint-systeem**: tussenlaag tussen instructie en oplossing toevoegen (voor stagiairs die vastlopen maar nog niet de hele oplossing willen zien)?
- **Multiple-choice variant**: voor pure begrip-vragen zonder uitwerking-prose, alleen vier opties + correct antwoord — kandidaat 2e oefening-type.
- **Deterministische renderer**: Python-script dat YAML → markdown produceert zonder LLM, voor garantie-reproduceerbare re-renders bij script-wijzigingen.
