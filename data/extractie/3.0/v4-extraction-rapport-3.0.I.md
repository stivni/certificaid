# EXTRACT v4 — rapport 3.0.I "De verschillende soorten vennootschappen"

**Run-id**: `concept-extractie-v4-3.0.I-2026-05-20`
**Anchor**: 3.0.I (kapstok PO 3.0)
**Model**: claude-opus-4-7 (subagent)
**Werkwijze**: research-and-draft-agent met initial-ctx bundle-3.0.I-top150.json (555 chunks volledig beschikbaar). Greenfield voor 3.0.I; cross-PO record `vennootschapsvormen-typologie` uitgebreid.

## Records-overzicht

**15 records geschreven**: 14 nieuw + 1 bijgewerkt.

### Nieuwe records (14)

| id | node_type | situeert |
|---|---|---|
| `vennootschap-begrip` | begrip | Constitutieve definitie WVV art. 1:1 — drie kenmerken (inbreng, vermogen, winstoogmerk). |
| `rechtspersoonlijkheid-vennootschap` | begrip | Eerste typologie-dimensie; vormen mét/zonder rechtspersoonlijkheid. |
| `inbreng-vennootschap` | begrip | Drie soorten inbreng (geld, natura, nijverheid) + fiscaal kapitaal-begrip. |
| `beperkte-aansprakelijkheid-vennoot` | begrip | "Slechts inbreng verbinden" — BV/NV/CV. Grenzen (bestuurder, oprichtersaansprakelijkheid). |
| `onbeperkte-aansprakelijkheid-vennoot` | begrip | Maatschap, VOF, CommV-gecommanditeerden, EESV. CBN-vermeldingsplicht. |
| `maatschap-rechtsvorm` | cluster | Boek 4 maatschap — geen rechtspersoonlijkheid, contract-basis, afgescheiden vermogen, stille/openbare variant. |
| `personenvennootschap-met-rechtspersoonlijkheid` | cluster | VOF + CommV als regime-cluster (pilot-bevinding 1 toegepast). |
| `besloten-vennootschap-bv` | cluster | Default-KMO-vorm. Afgeschaft kapitaal, financieel plan, dubbele uitkeringstest, statutaire flexibiliteit. |
| `naamloze-vennootschap-nv` | cluster | Kapitaalvennootschap voor grotere ondernemingen. € 61.500 minimum, drie bestuursmodellen, vrije overdraagbaarheid. |
| `cooperatieve-vennootschap-cv` | cluster | Hervormde CV — alleen voor échte coöperaties (post-2019). Variabel aandeelhouderschap, drie aandeelhouders min, sociale-onderneming-label. |
| `vereniging-en-stichting` | cluster | VZW, IVZW, stichting, feitelijke vereniging. Winstuitkeringsverbod als breuklijn met vennootschap. |
| `afgeschafte-vennootschapsvormen` | begrip | CVOA, Comm.VA, LV, ESV — historische noot voor examen-context. |
| `vennoot-vs-aandeelhouder` | begrip | Terminologie-onderscheid personen- vs kapitaalvennootschap. |
| `vennootschapsvormen-vergelijking` | synthese | Eén tabel met 11 vormen × 7 dimensies + 4 kerninzichten. |

### Bijgewerkte records (1)

| id | wijziging |
|---|---|
| `vennootschapsvormen-typologie` | `linked_anchors += 3.0.I`; `situering` bijgewerkt om beide PO's te dekken; 6 nieuwe `verwijst-naar`-edges naar 3.0.I-records; `_provenance.dekt_ook_anchors` aangevuld. Bestaande velden/bouwstenen behouden. |

### Hernoemd / verwijderd

Geen.

## Gaps.json-toevoegingen (6)

| aspect | aantal | prio | korte inhoud |
|---|---|---|---|
| `records.ontbreekt` | 3 | midden | (1) sub-anchor 3.0.I.A/B/C-detail uitgesteld; (2) financieel-plan-bij-oprichting eigen record kandidaat; (3) dubbele uitkeringstest eigen cluster kandidaat. |
| `bron-gap` | 2 | laag | (1) Boek 6 CV ondervertegenwoordigd in top-150; (2) Boek 10-11 (IVZW, stichting) niet rechtstreeks in bundle. |
| `granulariteit.beslissing-nodig` | 1 | laag | VOF + CommV als gecombineerde cluster of splitsen — voorlopig één cluster gehouden (regime-cluster-heuristiek). |

Geen `dangling-reference`-gaps: alle edge-targets bestaan al op disk.

## Edges-overzicht

- **`specialisatie-van`** → `vennootschap-begrip`: vanaf alle vormrecords (maatschap, VOF/CommV-cluster, BV, NV, CV). Patroon: 3.0.I-vormen als specialisaties van het generieke vennootschap-begrip.
- **`vergelijkt-met`**: BV ↔ NV (kapitaal-vs-flexibiliteit), maatschap ↔ VOF/CommV (rechtspersoonlijkheid), VOF/CommV ↔ BV (aansprakelijkheid), beperkte ↔ onbeperkte aansprakelijkheid, vennootschap ↔ vereniging (winstoogmerk).
- **`vereist-kennis-van`**: typologie-dimensies (rechtspersoonlijkheid, inbreng, aansprakelijkheid) zijn prereqs voor vormrecords; vergelijking-synthese vereist alle vormrecords.
- **Cross-PO `verwijst-naar`** naar pilot 3.0.II: `besloten-vennootschap-bv` en `naamloze-vennootschap-nv` linken naar `bestuursmodel-vennootschap`, `monistisch-bestuur`, `duaal-bestuur`. Dit cementeert de connectie tussen 3.0.I (typologie) en 3.0.II (governance per vorm).

Totaal aantal edges over de 14 nieuwe + 1 bijgewerkte record: ~55 (deduplicatie meegerekend).

## Migraties

Geen schema-1.4→1.5-migraties nodig — bestaande `vennootschapsvormen-typologie` was al schema 1.6.

Geen `voorbeeld_inline → voorbeelden[]`-migraties uitgevoerd op aangeraakt record.

## Claims met `inferred-from-aggregation`-confidence

5 plaatsen:
- `rechtspersoonlijkheid-vennootschap` — bouwsteen "Wat verandert door rechtspersoonlijkheid?" (aggregatie WVV + MvT).
- `maatschap-rechtsvorm` — in_praktijk "Wanneer kies je een maatschap?" (fiscale transparantie + voorbeelden uit advies-praktijk).
- `personenvennootschap-met-rechtspersoonlijkheid` — in_praktijk "Wanneer kies je VOF/CommV?" (combineert MvT + observatie BV-default).
- `cooperatieve-vennootschap-cv` — in_praktijk "Wanneer kies je voor een CV?" (MvT + sectorobservatie).
- `vennootschapsvormen-vergelijking` — twee kerninzichten over BV als default en drie beslissingsdimensies (synthese).

## Open observaties (narratief)

1. **Cross-PO-coherentie**: cross-link met PO 3.0.II-pilot voelt natuurlijk. De typologie (3.0.I) maakt expliciet welke bestuursmodellen aan welke vorm zijn voorbehouden (bv. duaal alleen NV). De pilot-records 3.0.II hebben geen `linked_anchors`-update gekregen vanuit deze run — eventueel later via dedicated edge-pass.

2. **Pilot-bevinding 1 (regime-cluster) toegepast**: `personenvennootschap-met-rechtspersoonlijkheid` bundelt VOF en CommV als één cluster met regime-bouwstenen ("Regime VOF" / "Regime CommV"). Voelt natuurlijk omdat Boek 4 zelf de twee vormen samen behandelt. Alternatief (twee aparte records) zou de smell-test `<concept>-<specialisatie>` opwerpen en zou redundante bouwstenen vereisen (vrijstelling-jaarrekening-publicatie geldt voor beide identiek).

3. **Anchor-tekst is leidend**: anchor 3.0.I verbose noemt expliciet "maatschappen zonder rechtspersoonlijkheid als kapitaalvennootschappen met beperkte aansprakelijkheid" en "wie is aansprakelijk, hoe wordt eigendom verdeeld, hoe wordt bestuurd — en niet om memoriseren van een lijst." Dit hebben we letterlijk gevolgd: de records leggen het *logica*-niveau bloot (3 typologie-dimensies + synthese), niet het *opsom*-niveau (lijst-met-namen-uit-hoofd).

4. **Cast-bias**: cast bevat geen expliciete VOF/CommV. We gebruikten natuurlijke personen (Pieter Vermeulen, Marleen De Cock) in maatschap-voorbeelden, en `Praktijk Persenaire` voor de eenmanszaak-maatschap-combinatie. Bij toekomstige aanvulling van de cast zou een "VOF-accountantskantoor" en een "CommV familiale holding" handig zijn — niet kritiek genoeg om nu de cast aan te passen (regel: ≥ 3 records die de rol nodig hebben).

5. **CBN-advies 2017/16 cross-link**: onbeperkte aansprakelijkheid bevat een belangrijke boekhoudkundige consequentie (vermeldingsplicht in jaarrekening van de vennoot). Dit linkt 3.0.I met PO 1.x. Het bestaande `vennootschapsvormen-typologie` heeft de link al; we hebben hem hergebruikt in `onbeperkte-aansprakelijkheid-vennoot`.

## Zelf-evaluatie

- **Vlot**: bundle-3.0.I-top150.json bevatte voldoende kerndefinities (art 1:1, 1:5, 1:6, 4:1, 4:13, 4:14, 4:22, 5:1, 6:1, 7:1, 9:1, 11) + MvT-toelichting om alle 14 nieuwe records grounded te schrijven zonder bron-MD-verificatie nodig te hebben. WVV is goed gechunkt.
- **Struikelpunt**: VOF/CommV-keuze (regime-cluster vs. twee records) — opgelost door regime-cluster te kiezen + gap-entry voor toekomstige splitsing-overweging. Pilot-bevinding 1 was direct toepasbaar.
- **Struikelpunt**: hoe diep gaan in BV/NV-kapitaal-procedures (financieel plan, uitkeringstest) — bewust beperkt tot bouwsteen-niveau in vormrecord. Eigen records voorgesteld in gaps.json voor sub-anchor 3.0.I.A/B/C of dedicated extract-pass. Volgde §6 anti-twijfel-regel maar woog "bestaansreden buiten BV-context" af: ja, dus eigen-record-kandidaat.
- **Signaal voor hoofdsessie**: pilot 3.0.II + 3.0.I geven samen een **hechte governance + typologie-basis** voor PO 3.0. Volgende anchors (3.0.III aandelen, 3.0.IV algemene vergadering, 3.0.V kapitaalveranderingen, 3.0.VII aansprakelijkheid) kunnen voortbouwen op deze 25 records. Pilot-bevinding 1 (regime-cluster) zal opnieuw relevant zijn bij 3.0.III (aandelensoorten BV/NV/CV) en 3.0.IV (algemene vergadering BV/NV/CV).
- **Wave-planning**: voor 3.0.I was top-150 voldoende. Geen second-pass naar volle 555 chunks nodig geweest (na initiële verkenning).

## Audit

```
[audit] disk: 500 records (34 synthese), RAG: 500 records, content: 466 fiches
[audit] OK — disk, RAG en content zijn in sync.
```

Begin-state: 485 records. End-state: 500. Delta: +15 (14 nieuw + 1 update zonder count-toename).
