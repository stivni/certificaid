# EXTRACT v4 — rapport anchor 3.0.VIII "Conflicten in vennootschappen"

**Datum**: 2026-05-20  
**Run-id**: concept-extractie-v4-2026-05-20T10-00-00Z  
**Model**: claude-opus-4-7 (subagent)  
**Anchor**: 3.0.VIII (PO 3.0 Vennootschapsrecht)  
**State pre**: 599 records  
**State post**: 615 records (audit groen — disk/RAG/content in sync)

## Records aangemaakt (16 nieuwe, 0 bijgewerkt)

Geschreven in zes mini-batches om crash-risico te beperken na vorige stream-timeout.

### Hub (cluster)
1. **`vennootschapsconflict`** — overkoepelend cluster met 5 bouwstenen (intern-aandeelhouders, aandeelhouder-bestuur, inter-organen, wettelijke instrumenten, contractuele/alternatieve geschilbeslechting). Edges naar bv/nv/AV/bestuursorgaan + verwijzingen naar exit-mechanismen-sha en gerechtelijke-ontbinding.

### Vijf wettelijke vorderingen (cluster + regel + begrip)
2. **`minderheidsvordering`** (cluster) — BV 10% + NV 1%/€ 1,25M, subrogatoir karakter, kwijtingsvoorwaarde, dading-controle, kostenrisico.
3. **`uittredingsvordering`** (cluster) — art. 2:68; geen drempel; gegronde redenen bij verweerder; mede-aandeelhouders nemen over.
4. **`uitsluitingsvordering`** (cluster) — art. 2:63; drempel 30%; niet door vennootschap zelf; statutaire BV-uitsluiting als alternatief.
5. **`deskundigenonderzoek-vennootschap`** (regel) — 10%-drempel, onderzoek boeken + bestuurshandelingen, voorbereidende waarde voor zwaardere vorderingen.
6. **`vennootschapsvordering`** (begrip) — actio mandati door AV beslist; tegenhanger van minderheidsvordering.

### Specifieke figuren (regel + begrip + cluster)
7. **`nietigverklaring-algemene-vergaderingsbesluit`** (regel) — formele en inhoudelijke nietigheidsgronden inclusief misbruik van meerderheid; art. 2:143 verjaring.
8. **`misbruik-van-meerderheid`** (begrip) — doctrinaire figuur, drie cumulatieve elementen, drie klassieke types (uithongering / vermogenstransfer / verdunning).
9. **`misbruik-van-minderheid`** (begrip) — blokkering versterkte meerderheid zonder vennootschapsbelang.
10. **`statutaire-uittreding-bv`** (cluster) — art. 5:154–5:156: uittreding ten laste van vermogen, scheidingsaandeel, liquiditeitstest, statutaire uitsluiting, uittreding van rechtswege.
11. **`gegronde-redenen-vennootschapsgeschil`** (begrip) — gemeenschappelijk criterium uittreding/uitsluiting; locus bij verweerder.
12. **`deadlock-vennootschap`** (begrip) — 50/50, blokkering versterkte meerderheid, bestuursdeadlock; aanleiding voor SHA/uittreding/ontbinding.

### Syntheses (2)
13. **`vergelijking-vorderingen-vennootschapsconflict`** (synthese) — vergelijkingstabel van de 5 hoofdfiguren (drempel/eiser/verweerder/doel/uitkomst/wetsartikel).
14. **`beslisboom-remedie-vennootschapsconflict`** (synthese) — beslisboom-knopen: genoteerd? → doel? → drempel/SHA? → instrument.

### Cross-thema (2)
15. **`alternatieve-geschilbeslechting-vennootschap`** (cluster) — arbitrage, mediation, bindende expertise; getrapte clausules.
16. **`wettige-redenen-ontbinding`** (begrip) — art. 2:73 criterium, strenger dan gegronde redenen; ultimum-remedium-toets. Linked aan 3.0.VIII + 3.0.IX.

## Edges-overzicht

Hub-spoke-structuur: alle 15 niet-hub-records hebben een `onderdeel-van → vennootschapsconflict`-edge.

Sterke cross-PO edges (allemaal naar bestaande records):
- 3.0.I: `besloten-vennootschap-bv`, `naamloze-vennootschap-nv`
- 3.0.II: `bestuursorgaan`
- 3.0.III: `algemene-vergadering`, `quorum-en-meerderheid-statutenwijziging`
- 3.0.VI: `exit-mechanismen-sha`, `aandeelhoudersovereenkomst`
- 3.0.VII: `bestuurdersaansprakelijkheid`, `kwijting-bestuurder`
- 3.0.IX: `gerechtelijke-ontbinding` (en `wettige-redenen-ontbinding` is dual-anchored op 3.0.VIII + 3.0.IX)

Pending edges (target ontbreekt nog):
- `vereist-kennis-van → uitkeringstest-bv` op `statutaire-uittreding-bv` (gemarkeerd in gaps.json)
- Drie minderheidsvordering ↔ uittredingsvordering `vergelijkt-met` edges: één pending werd na save van target weer exists; zie gap-entry voor cleanup.

## Gaps.json-toevoegingen (5 nieuwe entries)

| record_id | aspect | prio | kern |
|---|---|---|---|
| minderheidsvordering | dangling-reference | laag | Edge pending → exists cleanup |
| statutaire-uittreding-bv | records.ontbreekt | midden | `uitkeringstest-bv` ontbreekt (hoort bij 3.0.IV) |
| — | records.ontbreekt | laag | NV statutair regime art 7:222 e.v. (out-of-scope) |
| — | bron-gap | laag | Cassatie-rechtspraak misbruik meerderheid ontbreekt in bundle |
| — | records.ontbreekt | midden | Verjaringstermijnen art. 2:143 verdient eigen record (cross-PO) |

## Claims `inferred-from-aggregation`

- `vennootschapsconflict` bouwsteen "Contractuele en alternatieve geschilbeslechting" — synthese over IBA-SHA-praktijkgids en algemeen vennootschapsrecht.
- `alternatieve-geschilbeslechting-vennootschap` arbitrage- en expertise-bouwstenen — gerede inhoud uit IBA-praktijkgids, aangevuld met algemene wetsverwijzingen.

Voorbeelden in `uittredingsvordering`, `deskundigenonderzoek-vennootschap`, `nietigverklaring-algemene-vergaderingsbesluit`, `misbruik-van-meerderheid`, `deadlock-vennootschap` zijn telkens gemarkeerd als `confidence: inferred` (cast-gebaseerde scenario's met plausibele bedragen).

## Schema-migraties

Geen — alle 16 records zijn nieuw aangemaakt; geen pre-existing schema-1.4-types of `voorbeeld_inline`-velden aangetroffen.

## Zelf-evaluatie

**Sterk**:
- Hub-spoke met expliciete `onderdeel-van`-edges van alle records naar `vennootschapsconflict` levert een zuivere graph-walk.
- Vergelijkingstabel en beslisboom-synthese maken de keuze tussen vorderingen examenklaar.
- Cross-PO-edges (twaalf onique target-records over zes PO-onderdelen) sluiten aan op bestaande kennisbank.

**Aanvaard zwak**:
- Geen eigen records voor art. 2:143 verjaring (gap-entry) of voor art. 2:74 ontbinding wegens niet-neerlegging jaarrekening (niet kern-conflict).
- Bronnen-RAG met directe term-query niet beschikbaar via daemon (enkel duplicate-check). Compensatie: directe disk-existence-check voor edge-targets via `data/concepten/records/`.
- Strafrechtelijke aansprakelijkheid bewust niet geraakt (out-of-scope-instructie).
- Sub-anchors 3.0.VIII.A-D niet apart bediend (instructie: komen later).

**Risico**:
- `wettige-redenen-ontbinding` is dual-anchored (3.0.VIII + 3.0.IX); bij latere extractie van 3.0.IX moet hier niet gedupliceerd worden.
- Misbruik-van-meerderheid is doctrine-gegrond (geen letterlijke WVV-tekst); rechtspraak-bron ontbreekt in bundle. Bij VERIFY mogelijk flagged als ondersteunend bewijs zwak.

## Open observaties (niet record-specifiek)

- De WVV.md heeft eigenaardige chunk-id-offsets (chunk-id `WVV__art_5_123` bevat tekst van Art. 5:152). Bron-attributie blijft consistent via `sectie`-veld, niet via chunk-id-parsing.
- Boek 2 Titel 7 "Geschillenregeling" centraliseert uittreding en uitsluiting voor BV/NV; vroegere boekspecifieke artikelen 5:152-5:156 betreffen het statutaire regime (uittreding **ten laste van vermogen**), niet de gerechtelijke geschillenregeling.
- De **CV (coöperatieve vennootschap)** valt buiten de geschillenregeling — opvallend gap dat in scope-text was vermeld maar bewust niet als eigen record werd opgenomen (de CV heeft een eigen uittredingsregime in Boek 6).
