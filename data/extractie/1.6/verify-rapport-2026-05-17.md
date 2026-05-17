# VERIFY-rapport PO 1.6 — Externe controle

**Datum**: 2026-05-17
**Run-id**: verify-run-po-1.6-2026-05-17T00:00Z
**Model**: claude-opus-4-7 (judge-rol)
**Scope**: 59 records met minstens één `linked_anchors` in 1.6.x
**Synthese-records aanwezig**: 2 (`opdrachttypes-zekerheidsniveaus-synthese`, `auditcyclus-fasen-synthese`)

## Samenvatting

```
Records beoordeeld : 59
Examenvragen getest: 0   (Check A geskipt — geen 1.6-vragen geclassificeerd)
Gaps geappend      : 19
  hoog  : 0
  midden: 2
  laag  : 17
Top-3 aandachtspunten:
  1. intern-beheersingsrisico: edges.target-ontbreekt — geen cross-PO-brug naar PO1.7 'interne-controle'/'coso-raamwerk'
  2. toetsing-interne-beheersing: edges.target-ontbreekt — methode mist edge naar PO1.7 'interne-controle' (het concept dat ze test)
  3. controleoordeel-types-overlap met aangepast-oordeel — niet als gap gelogd; één omvattend + één begrip is bewuste keuze, zie §C3
```

---

## Check A — Examenvraag-simulatie

**Geskipt** — er zijn geen examenvragen geclassificeerd onder 1.6.x in `data/programma/examen_vragen/`. Zodra examen-classificatie 1.6 oppakt, een tweede verify-pass uitvoeren.

---

## Check B — Minicursus-haalbaarheid

### B1. Uniforme rijkheid per node_type

**Methode-records (5 stuks)**:

| Record | formules | invulling_voorbeeld | bouwstenen | voorbeeld_inline | richness |
|---|---|---|---|---|---|
| `auditrisicomodel` | 1 (`berekeningsmethode[].formules`) | ja (Rotex 60% × 30% → 28%) | 2 | — | volledig |
| `cijferanalyses-audit` | — | — | 2 | ja | OK |
| `steekproef-audit` | — | — | — | ja | mager |
| `gegevensgerichte-werkzaamheden` | — | — | 2 | ja | OK |
| `toetsing-interne-beheersing` | — | — | 2 | ja | OK |

**Niet als gap gelogd**: alleen `auditrisicomodel` is rekenkundig. De vier andere methode-records zijn proceduraal-kwalitatief (geen formule vereist). `steekproef-audit` is iets dunner dan de rest (geen bouwstenen) maar heeft wel een voorbeeld_inline en duidelijke `doel.text` — niet voldoende reden voor expliciete gap. Wél een aandachtspunt voor enrich: een vergelijkingstabel statistische vs. niet-statistische steekproef zou rijkheid verhogen.

**Procedure-records (12 stuks)**: stap-blokken aanwezig in 7/12. De 5 zonder stappen (`beoordelingsverslag-elementen`, `ontbinding-vereffening-opdracht`, `kennis-van-onderneming-omgeving`, `kwaliteitsbeheersing-opdrachtniveau`, `werkprogramma-audit` — niet gechecked apart) zijn meer beschrijvend dan procedureel; geen harde gap, maar enrich kan ze tot echte stap-skelet verwerken. Niet als hoge prio gelogd.

**Begrip-records (25 stuks)**: bezitten alle minstens `definitie.text`. `materieel-belang-audit` heeft sterk numeriek `voorbeeld_inline` (€ 2 000 000 × 5 %). Geen rijkheid-gaps.

### B2. Minicursus-coherentie

Mentaal opgebouwd minicursus-skelet 1.6 = **haalbaar**:

1. **Wat is externe controle?** (begrip: `gecertificeerd-accountant-ga`, `bedrijfsrevisor`, `commissaris` (cross-PO 1.2), `opdrachttypes-zekerheidsniveaus-synthese`)
2. **Opdrachtenkader** (begrip: `wettelijke-controleopdracht-commissaris`, `contractuele-controleopdracht`, `contractuele-beoordelingsopdracht`, `samenstellingsopdracht-isrs4410`, `gedeelde-wettelijk-voorbehouden-opdracht`)
3. **Beroepskader** (beginsel: `onafhankelijkheid-externe-accountant`, `belangenconflict-accountant`, `beroepsgeheim-accountant`, `beroepsaansprakelijkheid-accountant`)
4. **Auditcyclus** (synthese: `auditcyclus-fasen-synthese`) → planning (`auditstrategie`, `auditplanning`, `werkprogramma-audit`, `opdrachtbrief-accountant`)
5. **Risicoanalyse** (methode: `auditrisicomodel` + componenten `inherent-risico`, `intern-beheersingsrisico`, `ontdekkingsrisico`; begrip: `materieel-belang-audit`, `significant-risico-audit`, `fraude-versus-fout`)
6. **Uitvoering** (methode: `gegevensgerichte-werkzaamheden`, `toetsing-interne-beheersing`, `cijferanalyses-audit`, `steekproef-audit`, `externe-bevestiging-audit`, `schriftelijke-bevestiging-management`)
7. **Oordeel + verslag** (begrip: `controleoordeel-types`, `aangepast-oordeel`, `paragraaf-ter-benadrukking`, `paragraaf-overige-aangelegenheden`, `getrouw-beeld-controle`, `regelmatigheid-jaarrekening-audit`, `controleverslag-elementen`, `beoordelingsverslag-elementen`)

Alle records zijn aanwezig, de auditcyclus-synthese geeft een proceduraal anker, en de opdrachttypes-synthese geeft een vergelijkingstabel die de drie zekerheidsniveaus uit elkaar trekt. **Minicursus-haalbaarheid: groen**.

---

## Check C — Semantische coherentie

### C1 — Mechanische checks

**Edges met ontbrekend target**: 15 — alle geappend in `gaps.json` (prio `laag`).

Patroon-analyse:
- **Typo's / niet-canonieke ids** (snelle fix in enrich): `regelmatig-jaarrekening` → `regelmatigheid-jaarrekening-audit`; `opdrachtbrief` → `opdrachtbrief-accountant`; `auditwerkschema` → `werkprogramma-audit`; `auditcyclus` → `auditcyclus-fasen-synthese`; `externe-bevestiging` → `externe-bevestiging-audit`. (5 stuks)
- **Niet-bestaande kapstok-targets**: `plichtenleer-accountant` (3 edges van `beroepsgeheim-`, `opvolging-voorganger-`, `onafhankelijkheid-externe-accountant`). Mogelijk nieuw kapstok-record te overwegen, OF de 3 edges vervangen door wikilinks naar specifieke KB-1998-bouwstenen die wel records hebben.
- **Assurance-opdracht** (2 edges) — niet-bestaande kapstok; vervang door edge naar `opdrachttypes-zekerheidsniveaus-synthese`.
- **Inhoudelijk-bedoelde maar niet-gemodelleerde concepten** (5 edges): `controlerisico` (zit in `auditrisicomodel`), `afwijking-van-materieel-belang` (zit in `controleoordeel-types`), `opdrachten-gecertificeerd-accountant`, `controle-inbreng-in-natura` (1.5-territorium), `antiwitwas-meldingsplicht` (1.10/1.11-territorium). Voor edge-resolutie: vervang door bestaand record OF verwijder.

**Vergelijkingsparen met ontbrekend target**: 2 — geappend.
- `fraude-versus-fout` → `afwijking-van-materieel-belang` (niet bestaand): vervang door `controleoordeel-types`.
- `beroepsaansprakelijkheid-accountant` → `tuchtrechtelijke-aansprakelijkheid-accountant` (niet bestaand): mogelijk apart record waardig (KB 1998 art. 18 + Wet ITAA 2019 art. 124 e.v.); voorlopig pair verwijderen.

### C2 — LLM-oordeel

**Cross-PO-bruggen ontbrekend** (2 midden-prio gaps geappend):

- `intern-beheersingsrisico` (component van auditrisicomodel) en `toetsing-interne-beheersing` (methode) verwijzen inhoudelijk naar interne beheersing — maar geen van beide heeft een edge naar het bestaande PO1.7-record `interne-controle` (of `coso-raamwerk`). Een minicursus 1.6 die "test of controls" introduceert, moet kunnen doorlinken naar de COSO/IC-uitwerking in 1.7.

**Cross-PO-bridges OK**:
- `getrouw-beeld-controle` (1.6) ↔ bestaande `controle.json` (1.4): de verschil-rationale uit het rapport is correct — `controle.json` (1.4) gaat over GROEP-controle (consolidatie), niet over audit-controle. Geen verwarringsrisico mits naam-consistent gebruik.
- `wettelijke-controleopdracht-commissaris` (1.6) ↔ `commissaris` (1.2): rapport flagt dit zelf voor enrich (PO 1.2-actor moet linked_anchors uitbreiden + edge naar de 1.6-opdracht). Niet apart in gaps.json toegevoegd omdat er reeds een open gap op `commissaris/edges.target-ontbreekt` bestaat (van eerdere verify-pass op 1.2, met ander target `accountant-itaa`); enrich kan beide tegelijk oppakken via de bestaande gap-entry. *Vermelding hier voor traceability.*

**Vrije-tekst-verwijzingen niet gespiegeld** (steekproef-scan, niet exhaustief):
- Geen "zie X"-patronen aangetroffen in steekproef-records. De extractor heeft consequent edges + wikilinks gebruikt in plaats van vrije-tekst-verwijzingen. Geen extra gaps.

### C3 — Overlap-controle (records.overlappend-fenomeen)

Onderzochte risico-paren:
- `controleoordeel-types` (omvattend record met 4 types in bouwstenen + vergelijkingstabel 2×2) versus `aangepast-oordeel` (apart begrip-record): **bewuste keuze rapport §Open obs pt 5**, geen overlap-gap. `aangepast-oordeel` is de paraplu voor de 3 niet-goedkeurende types; `controleoordeel-types` is de typologie. Acceptabel.
- `controleverslag-elementen` versus `beoordelingsverslag-elementen`: parallelle records voor twee opdrachttypes. Geen overlap (verschillende inhoud + verschillende NORM-bron). OK.
- `redelijke-mate-van-zekerheid` versus `beperkte-mate-van-zekerheid`: parallel begrip-paar; vergelijkingsparen aanwezig. OK.
- `professioneel-kritische-instelling` versus `professionele-oordeelsvorming`: dichtbij maar conceptueel onderscheiden (mindset vs. afweging). Beide nodig.

**Geen `records.overlappend-fenomeen` gaps gelogd**.

---

## Extra synthese-record voorstel: GEEN

Het mandaat is "maximaal 1 extra synthese-record IF clear-pedagogical-value". Onderzocht: een mogelijk `auditverklaring-typologie-tabel` of `controleoordeel-vergelijkingstabel`.

**Beslissing: niet nodig.** Het bestaande record `controleoordeel-types` bevat reeds:
- Alle 4 oordeel-types als bouwstenen (goedkeurend / met voorbehoud / afkeurend / onthouding) met `wat` + `waarom` + `voorbeeld_inline` (cast-namen Sofie/Rotex).
- Een **vergelijkingstabel 2×2** (aard probleem × diepgaand vs. niet-diepgaand) die de typologie cumulatief verklaart.

Een aparte synthese-record zou strikt dubbel zijn. Pedagogische meerwaarde is niet zichtbaar — minicursus kan rechtstreeks uit `controleoordeel-types` putten. **Geen synthese-record toegevoegd**.

---

## Vervolgacties voor enrich-pass

Concrete fix-list voor enrich-run op 1.6-scope, in volgorde van impact:

1. **Cross-PO-bruggen leggen** (midden):
   - `intern-beheersingsrisico` + edge → `interne-controle` (type: `vereist-kennis-van`) en/of → `coso-raamwerk`.
   - `toetsing-interne-beheersing` + edge → `interne-controle` (type: `getriggerd-door` of `vereist-kennis-van`).
   - `commissaris` (1.2): linked_anchors uitbreiden met `1.6.I.B` + edge naar `wettelijke-controleopdracht-commissaris` (type: `specialisatie-van` of `voert-uit`).

2. **Edge-target typo's renamen** (laag, 5 stuks):
   `regelmatig-jaarrekening` → `regelmatigheid-jaarrekening-audit`; `opdrachtbrief` → `opdrachtbrief-accountant`; `auditwerkschema` → `werkprogramma-audit`; `auditcyclus` → `auditcyclus-fasen-synthese`; `externe-bevestiging` → `externe-bevestiging-audit`.

3. **`plichtenleer-accountant` kapstok-beslissing** (laag, 3 edges): ofwel apart kapstok-record (KB 1998) ofwel edges vervangen door `beroepsgeheim-accountant`/`onafhankelijkheid-externe-accountant` als sub-deel-edges. Mens-beslissing aanbevolen.

4. **`assurance-opdracht` resolutie** (laag, 2 edges van `contractuele-*`): vervang door `opdrachttypes-zekerheidsniveaus-synthese`.

5. **Inhoudelijk-bedoelde maar niet-bestaande targets** (laag, 5 stuks): per geval beslissing in enrich. `controlerisico` → `auditrisicomodel`; `afwijking-van-materieel-belang` → `controleoordeel-types`; rest verwijderen of cross-PO-extern markeren.

6. **`tuberechtelijke-aansprakelijkheid-accountant`** (laag): overwegen apart begrip-record (KB 1998 art. 18 + Wet ITAA 2019 art. 124).

---

## Beperkingen die zijn nageleefd

- Geen records aangeraakt (judge-rol, read-only).
- Geen Python-scripts gemaakt in `tools/` — alleen ad-hoc JSON-IO heredoc.
- Geen examenvragen geraadpleegd (Check A geskipt).
- Strict dedup op (record_id, aspect, status=open) toegepast — bestaande `commissaris/edges.target-ontbreekt` gerespecteerd.
- Werkbudget ~25 min gerespecteerd.
