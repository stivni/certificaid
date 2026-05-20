# EXTRACT v4 — PO 3.0.IV "Kapitaalbescherming en winstverdeling"

**Run-id**: `concept-extractie-v4-2026-05-20T08:00:00Z`
**Model**: claude-opus-4-7
**Wave**: 1 vervolg (na 3.0.I + 3.0.II pilot)
**Aantal records**: 12 nieuw, 0 bijgewerkt, 0 hernoemd, 0 verwijderd

---

## Records

### Begrip (1)
- **`voorkeurrecht-aandeelhouder`** — pro-rata-inschrijfrecht bij uitgifte; per soort + tweede rang; NV-/BV-modulatie.

### Regel (4)
- **`nettoactieftest`** — algemeen regime met regime-bouwstenen BV/CV en NV.
- **`liquiditeitstest-bv`** — 12-maanden-prospectie + bestuursverslag (BV/CV-specifiek, geen NV-tegenhanger).
- **`interimdividend`** — bevoegdheid bestuur bij statutaire delegatie; verschil interim vs tussentijds dividend.
- **`financiele-steunverlening`** — financial assistance art. 7:227/5:152 met onbeschikbare reserve.

### Cluster (6)
- **`kapitaalverhoging-nv`** — statutenwijziging, toegestaan kapitaal, voorkeurrecht, inbreng in natura, incorporatie reserves.
- **`kapitaalverhoging-bv`** — kapitaalloos equivalent: bijkomende inbreng + uitgifte aandelen; soepelere voorkeurrechtmodulatie.
- **`kapitaalvermindering-nv`** — twee-maanden-schuldeiserszekerheid, werkelijk vs boekhoudkundig, minimum € 61.500.
- **`uitkering-uit-eigen-vermogen-bv`** — BV-vermogensdistributie equivalent; statutenwijziging vereist bij vrijmaking onbeschikbaar verklaarde inbreng; **geen** twee-maanden-procedure.
- **`inkoop-eigen-aandelen-nv`** — 80 %-AV-meerderheid, onbeschikbare reserve, geschorst stemrecht, sanctie nietigheid.
- **`inkoop-eigen-aandelen-bv`** — dubbele uitkeringstest + statutenwijzigingsmeerderheid.

### Synthese (1)
- **`uitkeringstest-vergelijking-bv-nv`** — `vergelijkingstabel` met 8 dimensies + 4 kerninzichten.

---

## Edges-overzicht

**Inter-record-edges binnen 3.0.IV**: 23 edges (specialisatie-van, vereist-kennis-van, vergelijkt-met, onderdeel-van) verbinden de 12 records in een coherente kapitaalbeschermingsgraf:
- Centrale knoop: `nettoactieftest` ← specialisaties (interimdividend, financiele-steunverlening, uitkering-uit-eigen-vermogen-bv) + vergelijkt-met `liquiditeitstest-bv`
- Synthese `uitkeringstest-vergelijking-bv-nv` heeft 4 `vereist-kennis-van` edges naar de regels-records.

**Cross-PO-edges naar bestaande records**:
- `besloten-vennootschap-bv` ← onderdeel-van (5 records)
- `naamloze-vennootschap-nv` ← onderdeel-van (4 records)
- `kapitaalwijziging` (PO 1.1) ← specialisatie-van (4 records, regime-facet)
- `wettelijke-reserve` (PO 1.1) ← vereist-kennis-van/verwijst-naar (2 records)
- `inbreng-vennootschap` (3.0.I) ← vereist-kennis-van (2 records)
- `inbreng-in-natura-verslag` (1.7) ← vereist-kennis-van (2 records)
- `vennoot-vs-aandeelhouder`, `bestuursorgaan` ← vereist-kennis-van (sporadisch)

Geen cross-PO record bewerkt (scope-respect).

---

## Gaps.json — toevoegingen (10 entries)

Uitsplitsing per `aspect`:

| Aspect | Aantal |
|---|---|
| `records.ontbreekt` | 4 |
| `context-edge-ontbreekt` | 2 |
| `dangling-reference` | 2 |
| `bron-gap` | 1 |
| — andere | 1 |

Hoogtepunten:
- **`records.ontbreekt` — alarmbelprocedure** (midden) — verwante stof binnen kapitaalbescherming, valt onder 3.0.V; flag voor toekomstige wave.
- **`records.ontbreekt` — bestuurdersaansprakelijkheid bij ongeldige uitkering** (midden) — bewust uit scope (3.0.VII), kort vermeld in `liquiditeitstest-bv` en `uitkering-uit-eigen-vermogen-bv`.
- **`context-edge-ontbreekt` — kapitaalwijziging** (laag) — paraplu-cluster PO 1.1 mist outbound edges naar nieuwe specialisaties. Niet aangepast in deze pass (scope-respect).
- **`context-edge-ontbreekt` — wettelijke-reserve** (laag) — natuurlijke partner van nettoactieftest, niet aangepast.
- **`dangling-reference` — inschrijvingsrechten / converteerbare obligaties** (laag) — bewust voldoende-vermeld-geen-record-gemaakt.
- **`records.ontbreekt` — tantième** (laag), **reservevorming-cluster** (laag), **toegestaan kapitaal** (laag) — alle voldoende behandeld als bouwsteen.
- **`bron-gap` — CBN 2021/02 §tussentijds dividend jurisprudentie** (laag) — Cassatie-citaat in chunks beperkt.

---

## Migraties oud → nieuw schema

Geen migraties uitgevoerd — alle 12 records zijn nieuw aangemaakt in schema 1.6 (geen schema 1.4/1.5-records aangeraakt in deze pass).

Geen `voorbeeld_inline → voorbeelden[]`-conversies uitgevoerd (alle voorbeelden direct in schema 1.5/1.6 vorm geschreven).

---

## Claims `inferred-from-aggregation`

Twee expliciete `inferred-from-aggregation`-claims:

1. **`uitkeringstest-vergelijking-bv-nv` — kerninzicht "bedrag uitkeerbaar verschilt tussen regimes"** — synthese over WVV art. 5:142, 7:212 + CBN 2021/02.
2. **`uitkering-uit-eigen-vermogen-bv` — bouwsteen "geen wettelijke schuldeiserszekerheidstermijn"** — vaststelling over **afwezigheid** van een tegenhanger voor art. 7:209 in Boek 5, onderbouwd door WVV art. 5:143 + 7:209 + MvT bij art. 312.

Beide claims hebben volledige `_provenance.inputs` met chunk-ids uit ≥ 2 bronnen.

---

## Audit-resultaat

```
disk=512  rag=512  ghosts=0  missing=0  ok=True
```

Audit groen na de pass (was 500 voor de pass).

---

## Open observaties (narratief, niet in gaps.json)

### 1. Cluster-vs-regel-grens bij uitkeringstest

`nettoactieftest` is als **regel** gekozen (niet cluster), omdat de bouwstenen geen zelfstandige stappen zijn — ze zijn aspecten van **één wettelijke verplichting** in drie regimes. De regime-bouwstenen (BV/CV vs NV) zouden conceptueel ook specialisatie-clusters kunnen zijn (`nettoactieftest-bv`, `nettoactieftest-nv`). Gekozen voor één regel met regime-bouwstenen + één synthese voor de vergelijking — vermijdt de cluster-explosie en houdt de centrale regel-formulering bij elkaar. **VERIFY-pass kan dit overrulen** als wave 2 of feedback dit nodig vindt.

### 2. Inkoop-eigen-aandelen: twee specialisaties zonder algemene cluster

Conform de **regime-specialisatie**-richtlijn zou een algemene cluster `inkoop-eigen-aandelen` (regime-overstijgende kern) wenselijk zijn — niet aangemaakt omdat:
- De WVV-bronchunks behandelen het concept **uitsluitend** regime-specifiek (5:145 BV, 7:215 NV) — er is geen "algemene" wetstekst.
- De twee specialisaties dekken elkaar inhoudelijk reeds via `vergelijkt-met`-edge.
- Risico: corpus-blindheid voor de algemene definitie. Indien VERIFY of toekomstige wave dit signaleert: algemene cluster met `vergelijkings`-bouwsteen aanmaken.

### 3. BV-procedure benoemd in kapitaalbegrip-arme taal

`kapitaalverhoging-bv` en `uitkering-uit-eigen-vermogen-bv` zijn moeilijke titels omdat ze het kapitaalbegrip presupponeren dat juist is afgeschaft. Bewust voor "Bijkomende inbreng en uitgifte van aandelen" en "Uitkering uit eigen vermogen (vermogensdistributie)" gekozen als `naam`-velden, met de oude term in `naam_alternatief` / `situering`. Stagiairs zullen de oude term blijven gebruiken — record-id volgt de gangbare zoekterm.

### 4. Cijfer-consistentie tussen records

`nettoactieftest`-scenario (Brugse Brouwerij BV: nettoactief € 308.000, bodem € 88.000) wordt expliciet hergebruikt in `uitkering-uit-eigen-vermogen-bv`-scenario (zelfde Brugse Brouwerij BV, na vrijmaking € 40.000 onbeschikbaar: nettoactief € 308.000, bodem € 48.000, marge € 260.000). Rekenkundig consistent.

### 5. Cross-PO concretisering Aurelia Holding NV

`kapitaalverhoging-nv`, `kapitaalvermindering-nv`, `interimdividend`, `voorkeurrecht-aandeelhouder` gebruiken consistent Aurelia Holding NV als NV-cast (rol: moedervennootschap) met bedragen in plausibele range (kapitaal € 1.000.000-€ 1.500.000). Volgt cast/globaal.yaml-convention.

---

## Zelf-evaluatie

| Criterium | Score | Toelichting |
|---|---|---|
| Schema 1.6-conform | ✅ | Alle records `schema_version: "1.6"`, valide node_types, situering aanwezig, edges-types in canonieke set. |
| Cross-PO-strategie | ✅ | Geen dubbel-werk met `kapitaalwijziging`/`wettelijke-reserve` — wel cross-linked via edges. |
| Confidence-labeling | ✅ | Elke claim gelabeld; 2 `inferred-from-aggregation`-claims expliciet met `_provenance.inputs`. |
| Anti-hallucinatie | ✅ | Wetsartikelen letterlijk in chunks gecontroleerd; verbatim wetstekst niet in hoofdtekst; bestuurdersaansprakelijkheid bewust niet uitgebreid (scope). |
| Granulariteit | ⚠️ | 12 records over één anchor is rijk maar verdedigbaar — 3.0.IV is een dichte materie met BV/NV-parallel. Risico: regime-explosie bij wave 2 (CV-specifiek). |
| Concretisering | ✅ | Scenario's met cast-namen, illustraties (boekingen, balans-fragmenten), in_praktijk-vertalingen. |
| Edge-graf | ✅ | Synthese als centrale "ophanging", regime-specialisatie via `specialisatie-van` met facet. |
| Audit-status | ✅ | 0 ghosts, 0 missing, 512 records, audit groen. |

**Aanbevelingen voor wave 2 (3.0.V "Aandeelhoudersverhoudingen en alarmbelprocedure")**:
- `alarmbelprocedure-nv` en `alarmbelprocedure-bv` als spiegelbeeld van de uitkeringstest-records.
- Cross-link met `nettoactieftest` (zelfde balansconcept, andere drempel: helft of een vierde van kapitaal/inbreng).

**Aanbevelingen voor wave 2 (3.0.VII bestuurdersaansprakelijkheid)**:
- `bestuurdersaansprakelijkheid-uitkering-bv` (art. 5:144) — al kort geïntroduceerd in `liquiditeitstest-bv` en `uitkering-uit-eigen-vermogen-bv` als pointer.
- `terugvordering-uitkering` (art. 5:144, 7:214) — onderscheid goede-trouw-regime BV vs NV.
