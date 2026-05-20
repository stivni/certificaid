# EXTRACT v4 — PO 3.0, parent 3.0.II, wave 2 (sub-anchors A+B+C)

**Run**: concept-extractie-v4-wave2-3.0.II
**Datum**: 2026-05-20
**Scope**: Sub-anchors 3.0.II.A (bestuurder alleen vs collegiaal), 3.0.II.B (vennootschap verbonden bij bevoegdheidsoverschrijding), 3.0.II.C (belangenconflict-regels detail)
**Schema**: ADR-007 v1.6 (records-API via ADR-019)

## Vertrekpunt

Wave 1 leverde 10 pilot-records voor parent anchor 3.0.II:
`bestuursorgaan`, `bestuursmodel-vennootschap`, `monistisch-bestuur`, `duaal-bestuur`,
`enige-bestuurder`, `dagelijks-bestuur`, `bevoegdheid-bestuursorgaan`,
`vertegenwoordiging-vennootschap-jegens-derden`, `belangenconflict-bestuurder`,
`verbonden-partijen-procedure-genoteerd`.

Wave 2 startte als gap-fill-modus over deze tien records voor de drie sub-anchors,
met als hypothese dat wave 1 het grootste deel van de scope al dekte.

## Resultaat in cijfers

| Categorie | Aantal |
|---|---|
| Nieuwe records | 4 |
| Bijgewerkte records (linked_anchors + edges) | 11 |
| Hernoemingen | 0 |
| Verwijderingen | 0 |
| Gaps.json-entries toegevoegd | 5 |
| Audit-parity | OK (647 disk = 647 RAG, 0 ghosts) |

## Nieuwe records

1. **`rechtspersoon-bestuurder-vaste-vertegenwoordiger`** (begrip) — art. 2:55 WVV.
   Vult een centrale lacune: rechtspersoon-bestuurder en zijn vaste vertegenwoordiger,
   inclusief hoofdelijke aansprakelijkheid, openbaarmaking en de niet-dubbele-rol-regel.
   Raakt sub-anchors A (alleen vs collegiaal — wie zit aan tafel) en B (binding van de
   vennootschap — door wie wordt ze verbonden).

2. **`bestuur-bv-cv-werkwijze`** (cluster, `specialisatie-van: bestuursorgaan`, regime BV/CV)
   — art. 5:73, 5:75 (BV) en 6:61, 6:63 (CV).
   Vult sub-anchor A: BV en CV gaan uit van "ieder alleen bevoegd" tenzij de statuten
   een collegiaal bestuursorgaan invoeren — fundamenteel tegenovergesteld aan de NV-regel.
   Vijf bouwstenen: standaardregel, statutaire beperking, keuze voor collegialiteit,
   notulen en schriftelijke besluitvorming, vertegenwoordiging jegens derden.

3. **`belangenconflict-bestuurder-bv-cv`** (cluster, `specialisatie-van: belangenconflict-bestuurder`,
   regime BV/CV) — art. 5:76-78 en 6:64-66.
   Vult sub-anchor C: BV/CV-specifieke procedure met onder meer het vangnet voor de
   enige-bestuurder-die-tevens-enige-aandeelhouder-is (art. 5:77 § 1), uitzondering bij
   uitkering met liquiditeitstoets (art. 5:143), en de bestuursaansprakelijkheid bij
   onrechtmatig financieel voordeel (art. 5:78).

4. **`belangenconflict-bestuurder-vzw-stichting`** (cluster, `specialisatie-van: belangenconflict-bestuurder`,
   regime vzw/stichting) — art. 9:8, 11:8, 11:9.
   Vult sub-anchor C: vzw met groottedrempel-afhankelijke verslagplicht (art. 3:47 §2),
   AV-vangnet bij meerderheid-in-conflict (vzw) versus eigen-besluit-vangnet bij stichting
   (geen AV). Zes bouwstenen, twee vangnetten naast elkaar.

## Bijgewerkte records

**Linked_anchors uitgebreid naar sub-anchor-coverage** (10 wave-1-records):

| Record | Nieuwe linked_anchors |
|---|---|
| bestuursorgaan | 3.0.II, 3.0.II.A, 3.0.II.B, 3.0.II.C |
| bestuursmodel-vennootschap | 3.0.II, 3.0.II.A |
| monistisch-bestuur | 3.0.II, 3.0.II.A |
| duaal-bestuur | 3.0.II, 3.0.II.A |
| enige-bestuurder | 3.0.II, 3.0.II.A, 3.0.II.B, 3.0.II.C |
| dagelijks-bestuur | 3.0.II, 3.0.II.A, 3.0.II.B |
| bevoegdheid-bestuursorgaan | 3.0.II, 3.0.II.A, 3.0.II.B |
| vertegenwoordiging-vennootschap-jegens-derden | 3.0.II, 3.0.II.B |
| belangenconflict-bestuurder | 3.0.II, 3.0.II.C |
| verbonden-partijen-procedure-genoteerd | 3.0.II, 3.0.II.C |

**Edges toegevoegd op bestaande records** (verbinding naar de 4 nieuwe records):

- `belangenconflict-bestuurder`:
  - `vergelijkt-met` → `belangenconflict-bestuurder-bv-cv` (aspect: NV vs BV/CV)
  - `vergelijkt-met` → `belangenconflict-bestuurder-vzw-stichting` (aspect: vennootschap vs vzw/stichting)
- `bestuursorgaan`:
  - `verwijst-naar` → `bestuur-bv-cv-werkwijze`
  - `verwijst-naar` → `rechtspersoon-bestuurder-vaste-vertegenwoordiger`
- `vertegenwoordiging-vennootschap-jegens-derden`:
  - `vereist-kennis-van` → `rechtspersoon-bestuurder-vaste-vertegenwoordiger`
- `bestuursmodel-vennootschap`:
  - `verwijst-naar` → `bestuur-bv-cv-werkwijze`

## Migraties (schema 1.4 → 1.5/1.6)

Geen. Alle aangeraakte wave-1-records waren al op schema 1.5/1.6.

## Confidence-distributie nieuwe records

- **grounded**: kernregels (procedurevereisten, sancties, drempels) — alle direct
  traceerbaar naar WVV-chunks via `_provenance.inputs`.
- **inferred-from-aggregation**: situering-blokken en vergelijkingsparen — combineren
  WVV-chunks uit 2+ bron-secties (art. 5:77 + 7:96 voor BV-NV-vergelijking;
  art. 9:8 + 11:8 voor vzw-stichting-vergelijking).
- **inferred**: enkele praktijk-voorbeelden met cast-namen (Aurelia/Brugse Brouwerij/etc),
  expliciet als zodanig gemarkeerd.

## Gaps.json — toegevoegde entries (5)

1. **`bron-gap`** — WVV.md (resources/bronnen/wetteksten/) mist artikelen 5:70, 5:76,
   6:64, 6:65, 7:101 en 7:115. Inhoud van die artikelen wordt impliciet via art. 5:77,
   7:117, 9:8, 11:8 gereconstrueerd; sommige nieuwe-record-content is daardoor
   inferred-from-aggregation in plaats van direct grounded. **Prio: midden** —
   vraagt ETL-aanpassing van de WVV-transformer.

2. **`records.ontbreekt`** — comité van drie onafhankelijke leden van de raad van
   toezicht (art. 7:116 §3, 7:117 §2) voor verbonden-partijen-verrichtingen in
   genoteerde duaal-NV's. **Prio: laag**.

3. **`dangling-reference`** op `belangenconflict-bestuurder-bv-cv` — uitkering met
   liquiditeitstoets (art. 5:143) als uitzondering. **Prio: laag** —
   bewust-uit-scope, suggestie voor PO 3.x-uitkeringswerk.

4. **`dangling-reference`** op `vertegenwoordiging-vennootschap-jegens-derden` —
   prokuratie/specifieke volmacht (lasthebber buiten bestuur). **Prio: laag** —
   onzeker of dit een eigen record nodig heeft.

5. **`context-edge-ontbreekt`** op `bevoegdheid-bestuursorgaan` — wave-1 record
   (`node_type=regel`) heeft géén `main_rule` of `definitie`-veld; structureel
   incompleet. **Prio: midden** — overweeg samenvoeging met `bestuursorgaan` of
   `main_rule` toevoegen in feedback-pass.

## Open observaties

- **Wave-1 hypothese bevestigd**: de tien wave-1-records dekken de hoofdkern van
  sub-anchors A/B/C. Gap-fill leverde 4 echte nieuwe records (geen volledige
  ankerlaag) en 11 anchor/edge-updates, zoals verwacht.

- **Patroon "specialisatie van algemene cluster naar regime"** werkt goed:
  `belangenconflict-bestuurder` (NV-default) krijgt twee parallel-specialisaties
  (BV/CV en vzw/stichting). De algemene record beschrijft het NV-regime expliciet —
  niet ideaal volgens ADR-007 §regime-specialisatie (algemene cluster zou
  regime-overstijgende kern moeten dekken). Voor wave 2 niet geherstructureerd om
  bestaande inhoud niet te dupliceren; aandachtspunt voor latere VERIFY-pass.

- **Granulariteits-keuze BV/CV gezamenlijk vs gesplitst**: art. 5:76-77 en 6:64-65
  zijn structureel identiek; één gezamenlijk record voor beide vennootschapsvormen
  is hier verantwoord (geen onnodige duplicatie, examenstof behandelt ze parallel).
  Hetzelfde geldt voor vzw/stichting (art. 9:8 en 11:8 hebben elk hun eigenheid
  rond AV-vangnet, maar dezelfde basisstructuur).

- **Cast-leemte stichting**: `data/concepten/casts/globaal.yaml` bevat geen
  stichting-naam. Voorbeelden in `belangenconflict-bestuurder-vzw-stichting`
  gebruiken alleen `VZW Quelle de Vie`; stichting-illustraties blijven abstract.
  Indien meer stichting-records komen in PO 3.x, cast aanvullen.

## Volgende stap

Geen automatische actie — wachtende op orchestrator om wave 3 (parent 3.0.III) of
feedback-pass over deze run te starten.
