# EXTRACT v4 — Rapport anchor 3.0.V "Aandachtspunten in overnameovereenkomsten"

**Run-ID**: `concept-extractie-v4-2026-05-20T08:56:28Z`
**Model**: claude-opus-4-7
**Schema**: 1.6
**Audit voor**: 586 records (groen)
**Audit na**: 599 records (groen, +13)

---

## 1. Aantal records

| Categorie | Aantal | IDs |
|---|---:|---|
| Nieuw | 13 | `overnameovereenkomst`, `asset-deal-versus-share-deal`, `due-diligence-overname`, `letter-of-intent-overname`, `confidentiality-overname`, `representations-and-warranties`, `indemnification-overname`, `purchase-price-mechanismen`, `escrow-en-zekerheidsmechanismen-overname`, `closing-condities-precedent`, `material-adverse-change-clausule`, `non-compete-overname`, `transfer-bedrijfstak-algemeenheid` |
| Bijgewerkt | 0 | — |
| Hernoemd | 0 | — |
| Verwijderd | 0 | — |

### Verdeling node_type

| node_type | Aantal | Records |
|---|---:|---|
| `cluster` | 8 | overnameovereenkomst, due-diligence-overname, representations-and-warranties, indemnification-overname, escrow-en-zekerheidsmechanismen-overname, closing-condities-precedent, transfer-bedrijfstak-algemeenheid, [+1 hieronder via synthese] |
| `synthese` | 2 | asset-deal-versus-share-deal, purchase-price-mechanismen |
| `begrip` | 2 | letter-of-intent-overname, confidentiality-overname, material-adverse-change-clausule (3, niet 2 — correctie: 3 begrip) |
| `regel` | 1 | non-compete-overname |

Correcte verdeling: 7 cluster + 2 synthese + 3 begrip + 1 regel = 13.

---

## 2. Cross-PO edges (anchor 3.0.V → buiten)

| Record | Edge | Target | Toelichting |
|---|---|---|---|
| `overnameovereenkomst` | `verwijst-naar` | `controleverwerving-methodes` | 3.0.VI cross-link |
| `overnameovereenkomst` | `verwijst-naar` | `aandeelhoudersovereenkomst` | 3.0.VI cross-link |
| `overnameovereenkomst` | `vergelijkt-met` | `verplicht-overnamebod` (`aspect: private vs genoteerd`) | 3.0.VI cross-link |
| `asset-deal-versus-share-deal` | `verwijst-naar` | `financiele-steunverlening` | 3.0.IV cross-link |
| `asset-deal-versus-share-deal` | `verwijst-naar` | `controleverwerving-methodes` | 3.0.VI cross-link |
| `transfer-bedrijfstak-algemeenheid` | `onderdeel-van` | `wetboek-vennootschappen-verenigingen` | 3.0.I cross-link |

Geen dangling-references (alle edge-targets bestaan op disk; gecontroleerd).

---

## 3. Gaps.json — toevoegingen

12 nieuwe entries (totaal 1003), uitgesplitst per aspect:

| Aspect | Aantal | Voorbeelden |
|---|---:|---|
| `dangling-reference` | 5 | W&I-insurance, data room, clean team agreement, B2B-wet, gun-jumping, CEPANI, culpa-in-contrahendo |
| `records.ontbreekt` | 4 | earn-out-overname, boekhoudkundige verwerking overname (IFRS 3), schadebeding/clause-pénale, ESG due diligence |
| `context-edge-ontbreekt` | 1 | `controleverwerving-methodes` → `asset-deal-versus-share-deal` |

(Optellen: 5 + 4 + 1 = 10; resterende 2 zijn dubbele dangling — feitelijke totaal: 12 → herzien per categorie: dangling-reference = 7, records.ontbreekt = 4, context-edge-ontbreekt = 1.)

---

## 4. Claims met `inferred-from-aggregation`

Twee synthese-records gebruiken expliciet `inferred-from-aggregation`:

1. **`asset-deal-versus-share-deal`** — vergelijkingstabel over 13 dimensies; aggregeert IBA-MA §2.1, §2.1.1, §2.1.2, §2.2, §2.4 in één synthese.
2. **`purchase-price-mechanismen`** — synthese closing-accounts / locked-box / earn-out; aggregeert IBA-MA §5.2.4, §1.1, §1.4.

Verder zijn alle bouwstenen op records met `grounded`-confidence rechtstreeks traceerbaar naar IBA-MA-Belgium-2022-EN-chunks (per bouwsteen `_provenance.inputs`).

---

## 5. Migraties (schema 1.5 → 1.6)

- Geen migraties: alle nieuwe records gebruiken `situering` direct (geen oude `doel`-velden).
- Geen `voorbeeld_inline` → `voorbeelden[]`-migratie nodig: bestaande records zijn niet getouched.

---

## 6. Open observaties (narratief, niet record-specifiek)

### 6.1 IBA-MA als monopolie-bron op contractuele M&A-stof
De anchor 3.0.V valt bijna volledig uit IBA-MA-Belgium-2022-EN. Het Belgisch wetboek vennootschappen, MvT-WVV en CBN-adviezen zwijgen grotendeels over deze stof — ze regelen wel **omgevingsregels** (vennootschapsbestaan, kapitaalbescherming, automatische bedrijfstak-overdracht) maar niet het **contractuele beschermingsbouwwerk**. Confidence-label `grounded` is volledig terecht omdat IBA-MA-bron expliciet getrusted is, met de bedenking dat IBA-MA een **praktijkgids** is — niet een wettekst. Eventuele heronderhandelingen van dat label naar `doctrine-grounded` voor R&W/indem-claims zijn een zinvolle VERIFY-vraag.

### 6.2 Cross-bron-validatie ontbreekt
Voor records zoals `non-compete-overname` zou een dwarsverwijzing naar Belgische rechtspraak of doctrine helpen — IBA-MA noemt de geldigheidsvoorwaarden (limited time/territory/scope) maar geen specifieke rechtspraak. In een latere VERIFY-pass kan dat worden aangevuld.

### 6.3 Spanning met bestaande PO 3.0.VI-records
`aandeelhoudersovereenkomst`, `drag-along-tag-along`, `verplicht-overnamebod` zitten op 3.0.VI. De overnameovereenkomst-anchor verwijst naar deze records voor private (SPA) ↔ genoteerde-markt (verplicht overnamebod) ↔ shareholder-relaties post-acquisition (SHA). Een wenselijke synthese — bv. `m-en-a-contracten-overzicht` — zou heel PO 3.0.V en 3.0.VI samenbrengen, maar valt buiten huidige scope.

### 6.4 PO 1.5 raakvlak (boekhoudkundige verwerking overname)
IFRS 3 (bedrijfscombinaties) en de fair-value-allocation van earn-outs en contingent consideration zijn op PO 1.5-territorium gemodelleerd via `consolidatieverschil`. Een specifiek M&A-accounting-record (zoals `earn-out-accounting-ifrs-3`) ontbreekt. Bewust uit scope gehouden voor 3.0.V — gap is genoteerd.

### 6.5 Pandemie-references blijven in tekst
IBA-MA-Belgium-2022-EN bevat veel 2020–2022-pandemie-context. Records gebruiken pandemie-impact zelden als kerninzicht maar wel als historische noot waar gepast (bv. MAC-clausule "1-in-5 SPAs heeft COVID-clausule"). Bij toekomstige update (IBA-MA 2024+) kan dit verfijnd worden.

### 6.6 Wave-planning observatie
De pre-pilot-verwachting "12-18 records" werd gehaald op 13. Tijdens schrijven was er één twijfel: `confidentiality-overname` versus opnemen-als-bouwsteen-in-LOI. Gekozen voor eigen record (begrip) omdat NDA's vaak vóór en buiten LOI bestaan; pre-existence-test in §6.1 EXTRACT v4 voldoet.

---

## 7. Zelf-evaluatie

| Criterium | Beoordeling |
|---|---|
| Scope-conformiteit | ✓ Binnen 3.0.V scope gebleven; cross-PO edges naar bestaande records, geen modificaties van andere PO's |
| Near-duplicate-check | ✓ Chroma-RAG-sweep op 14 query-varianten; geen overlap > 0.20 → 13 nieuwe records gerechtvaardigd |
| Slug-resolver | ✓ Alle 22 cross-record edges verwijzen naar bestaande records (geverifieerd op disk) |
| Bouwsteen-vs-record | ✓ W&I-insurance, data room, CTA → bouwsteen of gap; non-compete → eigen record (regel met geldigheids-voorwaarden) |
| Confidence-eerlijkheid | ✓ `grounded` voor IBA-MA-chunks; `inferred-from-aggregation` voor twee syntheses; `doctrine-grounded` voor één claim (MAC disproportionate-impact-test) |
| Cast-conventie | ✓ Aurelia Holding NV, Brugse Brouwerij BV, Logistics Lille SAS, Pieter Vermeulen, Sofie Janssens — alle uit `globaal.yaml`; bedragen in €-formaat |
| Drie concretiserings-velden | ✓ Records hebben mix van `in_praktijk[]`, `voorbeelden[]` (scenario en eenvoudig); geen `illustraties[]` toegevoegd (contracten-stof leent zich slecht voor boekingen/balansen) |
| Universeel `situering`-veld | ✓ Aanwezig op alle 13 records, 2-4 zinnen per record |
| Anti-hallucinatie | ✓ Provenance per bouwsteen + per top-level synthese; geen verzonnen wetsartikelen; bij asset/share-deal-fiscale-cijfers zijn de WIB92-percentages overgenomen uit IBA-MA (33 % speculatief, 16,5 % substantiële deelneming, 10 %/€ 2,5 mln DBI) |

---

## 8. Wave 1 voortgang

PO 3.0 anchors verwerkt in wave 1:
- 3.0.I (eerder)
- 3.0.III (eerder)
- 3.0.IV (eerder)
- 3.0.VI (eerder)
- 3.0.VII (eerder)
- 3.0.IX (eerder)
- 3.0.X (eerder)
- **3.0.V (deze pass) — 13 records, +13 t.o.v. baseline 586 → 599 records**

Audit groen op alle 599 records (disk = RAG = 599, content = 551 inclusief 48 synthese-records zonder fiche dat by design is).

---

*Rapport gegenereerd 2026-05-20T08:56:28Z*
