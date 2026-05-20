# EXTRACT v4 — PO 3.0.VI rapport

**Anchor**: 3.0.VI — *Aandeelhoudersovereenkomsten en methodes om de controle te verwerven*
**Run-id**: concept-extractie-v4-2026-05-20 (anchor-pilot, batch-pass)
**Model**: claude-opus-4-7 (subagent)
**Bundle**: `/tmp/po-3.0-pilot/bundle-3.0.VI-top180.json` (180 chunks) + `bundle-3.0.VI.json` (253 chunks)

---

## Records

**Nieuw aangemaakt: 12 records.**

| ID | node_type | Korte beschrijving |
|---|---|---|
| `aandeelhoudersovereenkomst` | cluster | Centrale SHA-cluster: contract tussen aandeelhouders, vertrouwelijk, vier categorieën clausules, tegenwerpelijkheid aan derden, duur |
| `stemovereenkomst` | regel | Art. 5:46 WVV — voorwaarden (tijdsbeperking, vennootschapsbelang) + drie absolute nietigheidsgronden |
| `overdrachtsbeperking-aandelen` | cluster | Statutair + contractueel: lock-up, goedkeuringsclausule, voorkooprecht, sanctie statutair (art. 7:78) |
| `voorkooprecht-aandelenoverdracht` | begrip | Right of first refusal bij **overdracht** — onderscheiden van voorkeurrecht bij **uitgifte** (vergelijkingspaar opgenomen) |
| `drag-along-tag-along` | synthese | Vergelijkingstabel meesleeprecht vs meekooprecht, kerninzichten, scenario JV-verkoop |
| `exit-mechanismen-sha` | cluster | Put/call, Russian roulette, Texas shoot-out, good/bad leaver, deadlock-resolutie |
| `certificering-aandelen` | cluster | Art. 7:61 / 5:48 — STAK-techniek, drie rollen, omwisselbaarheid, familiale opvolging |
| `meervoudig-stemrecht` | begrip | Art. 5:42 / 7:52 / 7:53 — niet-genoteerd vrij, genoteerd dubbel stemrecht (loyauteit) |
| `controleverwerving-methodes` | synthese | 9-rij vergelijkingstabel: directe meerderheid, bestuurdersaanstelling, stemafspraak, indirect, klasses, certificering, in feite, openbaar bod, squeeze-out |
| `verplicht-overnamebod` | regel | Wet 1 april 2007 — 30%-drempel, billijke prijs, FSMA, acting in concert |
| `uitkoopbod-squeeze-out` | regel | Art. 7:82 — 95%-drempel niet-genoteerde NV; effectenovergang van rechtswege met consignatie |
| `sell-out-minderheid` | regel | Spiegel-recht: minderheid kan na overnamebod (95% kapitaal + 90% verworven tijdens bod) eisen mee verkocht te worden |

**Bijgewerkt / hernoemd / verwijderd**: 0.

**Pre-EXTRACT centrale-ontbrekers-scan**: bundle-aggregatie wees IBA Guide + IBA Minority + WVV/MvT-WVV als dominante bronnen aan. Geen centrale begrippen waren reeds als dangling-ref aanwezig in de pijplijn (greenfield voor SHA-stof bevestigd).

## Edges-overzicht

Cross-PO edges (alle targets `resolved`):
- `vennoot-vs-aandeelhouder` ← 1 record (3.0.I)
- `naamloze-vennootschap-nv` ← 4 records (3.0.I)
- `besloten-vennootschap-bv` ← 1 record (3.0.I)
- `algemene-vergadering` ← 1 record (3.0.III)
- `stemrecht-aandeelhouder` ← 3 records (3.0.III)
- `voorkeurrecht-aandeelhouder` ← 2 records (3.0.IV, vergelijkings­paar)
- `controle`, `exclusieve-controle`, `gezamenlijke-controle` ← 4 records (3.0.II / II-overlap)
- `fsma` ← 2 records

Cross-record edges binnen 3.0.VI-batch (target_status: pending bij first save, opgelost door records-API edge-resolver bij volgende audit):
- `aandeelhoudersovereenkomst` is hub: 5 inkomende `onderdeel-van` (stemovereenkomst, overdrachtsbeperking-aandelen, drag-along-tag-along, exit-mechanismen-sha, controleverwerving-methodes(verwijst))
- `controleverwerving-methodes` is hub: 6 inkomende `onderdeel-van` van regels en clusters

Eén `vergelijkt-met`-paar buiten batch (target pending, gemarkeerd voor follow-up):
- `aandeelhoudersovereenkomst` ↔ `statuten-vennootschap` (target pending — gap geregistreerd)

## Gaps.json — toevoegingen

**7 nieuwe gap-entries**, alle status `open`:

| record_id | aspect | prio |
|---|---|---|
| `statuten-vennootschap` | records.ontbreekt | midden |
| `openbaar-overnamebod-procedure` | records.ontbreekt | midden |
| `onderling-overleg-acting-in-concert` | records.ontbreekt | midden |
| `gerechtelijke-uittreding` | records.ontbreekt | laag (doorschuif PO 3.0.VIII) |
| `toetredingsovereenkomst-sha` | dangling-reference | laag |
| `poison-pill-anti-overname` | records.ontbreekt | laag (doorschuif) |
| `burgerlijke-maatschap-aandelen` | dangling-reference | laag (bewust uit-scope) |

## Schema-migraties

- **Type-migraties (1.4 → 1.5/1.6)**: niet van toepassing — alle nieuwe records, geen oud-type aangetroffen
- **voorbeeld_inline → voorbeelden[]**: niet van toepassing — alle nieuwe records gebruiken direct schema 1.6
- **doel → situering**: alle 12 records hebben `situering`-veld (schema 1.6), geen `doel` aangemaakt

## Claims `inferred-from-aggregation`

- `aandeelhoudersovereenkomst` — in_praktijk: "Statuten of SHA — wat waar?" (synthese over IBA §2, §10, §3)
- `stemovereenkomst` — in_praktijk: "BV vs NV mutatis mutandis" (WVV art. 5:46 + MvT bij art. 449)
- `drag-along-tag-along` — kerninzicht: symbiotisch in private-equity (IBA §8 + §12)
- `controleverwerving-methodes` — top-level definitie (cross-bron synthese WVV + IBA's)
- `certificering-aandelen` — bouwsteen "Toepassingen — opvolging en werknemersparticipatie" (MvT + doctrine)

Alle aggregations hebben `_provenance.inputs` met de bijdragende chunk-ids.

## Open observaties (narratief)

1. **IBA als praktijkbron werkt goed voor concretiserings­velden** (`in_praktijk[]`, `voorbeelden[]`, cluster-bouwstenen-context). De prompt-instructie hield IBA-stof correct buiten `grounded`-claims op `regel`-records: alle regel-records (stemovereenkomst, verplicht-overnamebod, uitkoopbod, sell-out) hebben hun grondslag in WVV/Wet 1 april 2007/KB, met IBA als secundaire bron of cross-bron-aggregation. **Regime-cluster-heuristiek werd niet getriggerd** — SHA-stof is per definitie regime-overstijgend (geen IFRS/BE-GAAP-onderscheid).

2. **Anchor "stemafspraak in 7:56"** uit de scope-tekst klopt niet letterlijk: art. 7:56 ontbreekt in WVV.md tussen 7:55 en 7:57. De geldende regel zit in **art. 5:46 WVV** (BV-Boek) en geldt mutatis mutandis voor de NV via systematische verwijzing. Het record `stemovereenkomst` legt dit uit in een `in_praktijk[]`-blok zodat een stagiair de spanning niet ervaart.

3. **Sell-out vs squeeze-out**: beide bestaan parallel en zijn vaak verwarrend. Een expliciete `vergelijkt-met`-edge (facet: "minderheid vs meerderheid initieert") werd toegevoegd op beide records.

4. **Voorkeurrecht vs voorkooprecht**: terminologische verwarring is een echte stagiair-valkuil. Beide records (`voorkeurrecht-aandeelhouder`, `voorkooprecht-aandelenoverdracht`) hebben nu wederzijdse `vergelijkt-met`-edge + `vergelijkingsparen[]`-blok met `trigger`-uitleg.

5. **Bestuursmodel-link**: `aandeelhoudersovereenkomst` had logisch een edge naar `bestuursmodel-vennootschap` kunnen krijgen (SHA bevat doorgaans bestuurssamenstelling-clausules), maar dat is een eerder zwakke link — niet opgenomen. Bij latere VERIFY-pass valt te overwegen.

6. **Cijfer-zakboekje-drempels** (30%, 95%, 90%, 5%) zijn nauwgezet overgenomen uit primaire bronnen (Wet 1 april 2007, WVV art. 7:82, IBA Minority §4 met voetnoten 41-45) — geen verzonnen cijfers, geen afronding.

## Zelf-evaluatie

- **Anti-hallucinatie**: alle 12 records hebben `_provenance.inputs` met chunk-ids. Geen verzonnen artikelnummers (art. 7:56 NIET opgenomen omdat het feitelijk in de gebruikte WVV-md ontbreekt; in plaats daarvan verwijzing naar art. 5:46 + mutatis mutandis-uitleg).
- **Confidence-discipline**: IBA-stof als `grounded` alleen voor zuiver descriptieve definities; als `inferred-from-aggregation` bij synthese-over-bronnen.
- **Edge-vrije-tekst**: alle "zie ook", "niet verwarren met"-vermeldingen in tekst hebben corresponderende edges of vergelijkingsparen.
- **Cast-conventie**: cast-namen uit `casts/globaal.yaml` (Aurelia, Cardinal, Industria, Brugse Brouwerij, Constructies Cattoir, Energiehuis Evergem, Sofie Janssens, Pieter Vermeulen, Robert Vandenberghe, Marleen De Cock). Geen ad-hoc fictie. Bedragen met €-prefix + duizendpunten.
- **Slug-resolver**: alle "resolved" edges geverifieerd via concept-RAG/disk-check (`controle`, `exclusieve-controle`, `gezamenlijke-controle`, `naamloze-vennootschap-nv`, `besloten-vennootschap-bv`, `vennoot-vs-aandeelhouder`, `algemene-vergadering`, `stemrecht-aandeelhouder`, `voorkeurrecht-aandeelhouder`, `fsma`). Edges naar nog te creëren records (binnen batch + 7 gaps) als `target_status: pending`.

**Audit**: `python3 -m tools.lib.records_api audit` → groen, 586 records (574 → 586), disk + RAG + content in sync.

---

*Wave 1, anchor 3.0.VI — vervolg op 3.0.III/IV/VII/VIII/IX/X en pilot.*
