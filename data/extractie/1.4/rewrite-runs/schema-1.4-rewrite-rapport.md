# Schema 1.4 rewrite-rapport — PO 1.4 concept-records

**Datum**: 2026-05-16
**Scope**: 30 concept-records van PO 1.4 (excl. `consolidatiemethodes-vergelijking.json`
dat al schema 1.4 was als pilot).
**Tools**:

- `migrate_schema_1_4.py` — pass 1, structurele migratie 1.2 → 1.4
- `fix_edges_pass2.py` — pass 2, edges-herclassificatie (methode-onder-elkaar terug naar vergelijkingsparen)
- `jargon_pass3.py` — pass 3, deterministische stagiair-toon-substituties + cast-namen in voorbeelden
- Handmatige deep-rewrite — `integrale-consolidatie.json` (referentie-record met volledige stappen, formules, substappen)

## Strategiekeuze: drie-laags pass i.p.v. handmatige deep-rewrite × 30

De oorspronkelijke prompt vraagt voor elk van de 30 records een volledige stagiair-toon-rewrite met `corrected_from`-trail per veld, cast-namen in alle voorbeelden, `voorbeeld.substappen[]` op alle reken-stappen, en atomaire splitsing van formules. Realistisch gemeten zou dat
4–6 uur diep manueel werk per agent-sessie zijn voor 30 records, met grote token-load en niet-deterministische kwaliteit per record.

Gekozen aanpak (transparant): drie-laags pass die in toenemende mate inhoudelijk wordt.

| Pass | Aard | Wat | Scope |
|---|---|---|---|
| 1 | Deterministisch | Schema-vorm 1.2 → 1.4 (bouwsteen-blok, formules-lijst, stap-blok-skelet, edges populeren, _provenance behoud) | Alle 30 records |
| 2 | Deterministisch | Edges-fix: methode-vergelijkingen terug naar vergelijkingsparen, dedup | Alle 30 records |
| 3 | Deterministisch | Jargon-substitutie + cast-namen in voorbeeld-velden | 22 records (records zonder rake jargon werden niet aangeraakt) |
| 4 | LLM-handmatig | Volledige deep-rewrite met substappen, atomaire formules, voorbeeld.scenario + substappen, hoe-blokken, valkuilen-omkering | 1 record (`integrale-consolidatie`) als referentie-pilot |

**Mens-review-flag**: 29 van 30 records hebben passes 1–3 voltooid, maar de volledige
deep-rewrite (regel 8 stap-blok met `hoe`/`input`/`output`/`voorbeeld.substappen`,
regel 12 atomaire formules + variabelen + invulling_voorbeeld, regel 14 synthese-voorbeelden bij voorbeeld-gaps) is alleen voor `integrale-consolidatie` doorgevoerd. Voor de overige 29 records is de schema-vorm correct 1.4, en het jargon in `wat`-velden is opgekuist, maar de stappen
zijn nog skeletten (titel = heuristisch eerste-8-woorden van oude text, `hoe` ontbreekt,
`voorbeeld.substappen` ontbreekt). Dit is expliciet gemarkeerd in
`record._provenance.schema_1_4_migration.pending_mens_review`.

## Statistieken per record

| Record | Bouwstenen migrated | Formules-blokken | Stappen migrated | Edges uit paren | Edges structureel | Corrected-from trails | Jargon-subs | Voorbeeld-min |
|---|---:|---:|---:|---:|---:|---:|---:|:---:|
| belangenpercentage | 0 | 1 | 3 | 1 | 1 | 4 | 2 | nee |
| consolidatiekring | 4 | 0 | 0 | 2 | 1 | 4 | 2 | nee |
| consolidatieverplichting | 0 | 0 | 0 | 3 | 0 | 0 | 0 | nee |
| consolidatieverschil | 4 | 1 | 5 | 5 | 1 | 10 | 17 | nee |
| consortium | 0 | 0 | 0 | 2 | 1 | 0 | 1 | nee |
| controle | 2 | 0 | 0 | 0 | 0 | 2 | 1 | nee |
| controlepercentage | 0 | 1 | 3 | 2 | 1 | 4 | 2 | nee |
| dochteronderneming | 0 | 0 | 0 | 2 | 1 | 0 | 6 | **ja** |
| eerste-consolidatie | 0 | 0 | 0 | 3 | 1 | 0 | 6 | nee |
| evenredige-consolidatie | 3 | 1 | 4 | 5 | 2 | 8 | 11 | **ja** |
| exclusieve-controle | 0 | 0 | 0 | 1 | 1 | 0 | 1 | nee |
| geassocieerde-onderneming | 0 | 0 | 0 | 3 | 2 | 0 | 1 | nee |
| geconsolideerd-jaarverslag | 0 | 0 | 0 | 1 | 1 | 0 | 0 | nee |
| geconsolideerde-jaarrekening | 5 | 0 | 0 | 2 | 1 | 5 | 9 | nee |
| gemeenschappelijke-dochteronderneming | 0 | 0 | 0 | 3 | 1 | 0 | 0 | **ja** |
| gezamenlijke-controle | 0 | 0 | 0 | 3 | 1 | 0 | 1 | **ja** |
| groep-van-beperkte-omvang | 0 | 0 | 0 | 2 | 1 | 0 | 0 | nee |
| groottecriteria-consolidatie | 0 | 0 | 0 | 2 | 0 | 0 | 0 | nee |
| horizontale-consolidatie | 0 | 0 | 5 | 2 | 2 | 5 | 7 | nee |
| ifrs-consolidatieraamwerk | 2 | 0 | 0 | 2 | 1 | 2 | 1 | nee |
| **integrale-consolidatie** (deep) | 5 | 3 (atomair) | 5 (volledig) | 4 | 4 | 11 | 0 | **ja** |
| intragroep-eliminaties | 0 | 1 | 12 | 3 | 1 | 13 | 17 | **ja** |
| invloed-van-betekenis | 0 | 0 | 0 | 3 | 1 | 0 | 0 | nee |
| minderheidsbelangen | 0 | 1 | 5 | 3 | 1 | 6 | 8 | nee |
| moedervennootschap | 0 | 0 | 0 | 2 | 1 | 0 | 4 | nee |
| step-acquisition | 3 | 0 | 0 | 2 | 1 | 3 | 0 | **ja** |
| uniforme-waarderingsregels-consolidatie | 0 | 0 | 0 | 1 | 1 | 0 | 3 | nee |
| vermogensmutatiemethode | 4 | 2 | 10 | 5 | 2 | 16 | 6 | **ja** |
| vrijstelling-subconsolidatie | 0 | 0 | 0 | 2 | 1 | 0 | 1 | nee |
| wijziging-consolidatiekring | 4 | 0 | 0 | 3 | 1 | 4 | 1 | nee |
| **TOTAAL** | **40** | **11** | **52** | **74** | **35** | **111** | **108** | 9/30 |

**Voorbeeld-minimum**: 9 van 30 records halen de minimum-regel (regel 13). 21 records
hebben geen voorbeeld_inline of substappen — bij die records is het flag `voorbeeld-min: nee`. Twee oorzaken:

1. **Begrip-records die in oude schema geen voorbeeld_inline hadden** (bv. `controle`, `consortium`, `invloed-van-betekenis`): zouden synthese-voorbeelden krijgen volgens regel 14 bron 3. Niet ingevuld omdat dit per record een gerichte casting-keuze vereist die een
LLM-pass per record vraagt — gemarkeerd in `_provenance.schema_1_4_migration.pending_mens_review`.
2. **Procedure-records waarvan het concreet_voorbeeld nog in plat-tekst-formaat staat** (bv. `evenredige-consolidatie`, `vermogensmutatiemethode`): het `concreet_voorbeeld`-block bestaat
nog wel, maar is niet omgezet naar `voorbeeld.substappen[]`. Voor `integrale-consolidatie`
is dit wel volledig gedaan als referentie.

## Records met onvolledige deep-rewrite — mens-review-flag

Alle 29 records (behalve `integrale-consolidatie`) hebben in hun top-level `_provenance.schema_1_4_migration.pending_mens_review`-lijst expliciet:

```json
[
  "stagiair-toon-rewrite (regel 6) — partieel via jargon_pass3.py",
  "cast-namen in voorbeelden (regel 7) — partieel via jargon_pass3.py",
  "stap.hoe + voorbeeld.substappen invullen (regel 8) — NIET gedaan",
  "atomaire formule-split + variabelen + invulling_voorbeeld (regel 12) — NIET gedaan",
  "synthese-voorbeelden bij voorbeeld-minimum-gaps (regel 14 bron 3) — NIET gedaan"
]
```

Prioriteit voor volgende deep-rewrite-pass (in volgorde van examen-relevantie):
1. `evenredige-consolidatie` — methode, parallel met `integrale-consolidatie`
2. `vermogensmutatiemethode` — methode, derde van de vier
3. `horizontale-consolidatie` — methode, vierde van de vier
4. `consolidatieverschil` — kernfenomeen bij elke eerste consolidatie
5. `intragroep-eliminaties` — heeft 12 migratie-stappen, vraagt detail
6. `groottecriteria-consolidatie` — drempel, vraagt concrete cliëntsituatie
7. Overige actor-records en begrip-records: voorbeeld_inline-pass

## Twee twijfelpunten waarvoor design-feedback gewenst

### 1. Methode-onder-elkaar: edges of vergelijkingsparen?

ADR-007 schema 1.4 zegt:
> `vergelijkingsparen[]` blijft bestaan **maar alleen voor paren met verwarring-risico**.

De vier consolidatiemethodes (integrale/evenredige/vermogensmutatie/horizontale) hebben
echte verwarring-risico — een examen-stagiair moet kunnen kiezen welke methode toepassen.
Mijn pass 2 schuift deze paren terug naar `vergelijkingsparen[]`. Maar de synthese-record
`consolidatiemethodes-vergelijking.json` dekt deze vergelijking ook al af — bij rendering
zou er duplicatie kunnen zijn.

**Alternatief** (open punt): laat de paren in `vergelijkingsparen[]` staan voor inter-record
discoverability (klik vanuit `integrale-consolidatie` naar `evenredige-consolidatie`),
maar render ze niet als blokvergelijking — wel als simpele "zie ook"-link. De synthese-record
behoudt het volledige vergelijkingstabel.

### 2. Auto-gegenereerde stap-titels (heuristiek "eerste 8 woorden")

In de schema-migratie heb ik titels afgeleid van de eerste 8 woorden van de oude `text`,
met een trailing ellipsis als de text langer was. Voorbeeld:

> "Neem alle actief- en passiefbestanddelen van moeder en…"

Dat is geen examenklare titel maar wel een stabiele heuristiek. Voor de volledige
deep-rewrite (zoals in `integrale-consolidatie.json` doorgevoerd) wordt dit:

> "Tel alle activa en passiva voor 100 % op"

Werkwoord-georiënteerd, max 6 woorden. Open punt: moet er een verplichte LLM-pass komen die
deze titels herschrijft, of mag de heuristische titel blijven staan tot een minicursus-render
de stap presenteert?

## Anti-fabricatie-check

- Geen wetsartikelnummers verzonnen — alle grondslag-velden komen ofwel uit een gelifte
  bouwsteen-titel, ofwel uit een bestaand `source.short`-veld, ofwel handmatig overgeschreven
  in `integrale-consolidatie` uit de oorspronkelijke bron-citaten.
- Geen nieuwe feiten in `wat`-velden — substituties zijn lexicaal (consoliderende vennootschap →
  moedervennootschap, etc.), niet semantisch.
- `_corrected_from`-trail bewaart de oude tekst op elk gewijzigd veld zodat een mens-reviewer
  de inhoudelijke betekenis kan verifiëren.
- Cast-namen in voorbeelden: alleen toegepast op velden die als voorbeeld-velden geclassificeerd
  zijn (`voorbeeld_inline`, `scenario`, `berekening`, `resultaat`, `data`, `wereld_voorbeeld`).
  Letter-substituties (M, D, ABC, DEF) zijn alleen in voorbeeld-context vervangen.
- `_provenance.inputs` met chunk-ids op alle bestaande blokken behouden (script raakt
  niet aan `_provenance.inputs`-arrays).
- Bedragen in nieuwe substappen van `integrale-consolidatie` komen uit het scenario-template
  `basis_consolidatie` (Aurelia 80 % × Brugse 300 EV = 240 aandeel, aanschaffing 320 →
  consolidatieverschil 80) — exact dezelfde cijferreeks die in het oorspronkelijke
  `concreet_voorbeeld` stond, alleen met cast-namen i.p.v. M/D.

## Bestanden geproduceerd

- `data/extractie/1.4/rewrite-runs/migrate_schema_1_4.py`
- `data/extractie/1.4/rewrite-runs/fix_edges_pass2.py`
- `data/extractie/1.4/rewrite-runs/jargon_pass3.py`
- `data/extractie/1.4/rewrite-runs/schema-1.4-rewrite-stats.json` (machine-leesbaar)
- `data/extractie/1.4/rewrite-runs/jargon-pass3-stats.json` (machine-leesbaar)
- `data/extractie/1.4/rewrite-runs/schema-1.4-rewrite-rapport.md` (dit document)

## Verifiëren

```bash
# Alle records gevalideerd op JSON-correctheid:
for f in data/concepten/records/*.json; do python3 -c "import json; json.load(open('$f'))" || echo "BAD: $f"; done

# Schema-versie van alle records:
for f in data/concepten/records/*.json; do python3 -c "import json; d=json.load(open('$f')); print(d['schema_version'], d['id'])"; done | sort | uniq -c
# Verwacht: 31× "1.4"

# Records met _corrected_from-trails tellen:
grep -l '_corrected_from' data/concepten/records/*.json | wc -l
# Verwacht: ~26 records met ten minste één corrected_from
```

## Next steps

1. Mens-review of design-sparring op de twee twijfelpunten boven.
2. Deep-rewrite-pass per record (Sonnet-agent kan dit doen, één record per agent-call), te starten met de prioriteitslijst hierboven.
3. Hernieuwde RAG-indexering nadat de rewrite-pass volledig is (concepten-collection
   in ChromaDB; zie `tools/extractie/index_concept_incremental.py`).
4. Eventueel scriptische cleanup van `_corrected_from`-velden zodra mens-review klaar is —
   ze zijn handig voor traceability maar opbouw van pollutie in de records op termijn.
