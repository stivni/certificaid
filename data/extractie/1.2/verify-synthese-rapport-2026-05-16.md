# PO 1.2 — VERIFY + Synthese-rapport (2026-05-16)

**Run-id**: `verify-run-po12-2026-05-16T16:00Z`
**Model**: claude-opus-4-7 (verify-pass + synthese-design)
**Scope**: 59 records met minstens één PO 1.2-anchor in `linked_anchors[]` (29 nieuw + 15 cross-PO + extra cascade-bewegingen sinds extractie-rapport)
**Budget**: ~30 min — gehaald

---

## Deel A — VERIFY

### Check A — Examenvraag-simulatie

**Status**: skipped per opdracht. Examenvragen voor PO 1.2 nog niet geclassificeerd in `data/examen_vragen/`. Eén open-werk-entry gelogd in `gaps.json` (record_id `PO-1.2`, aspect `open-werk`).

### Check B — Minicursus-haalbaarheid + uniforme rijkheid

Uniformiteits-sweep over de 59 records (`in_praktijk`-veld + `valkuilen`-veld):

| Cluster | Records met `in_praktijk` | Records met `valkuilen` | Diagnose |
|---|---|---|---|
| Beginselen (4) | 3/4 | 3/4 | `oprechtheidsbeginsel` is duidelijk te dun (0/0) |
| Autoriteiten (7) | 2/7 | 0/7 | **Systemisch dun** — alleen NBB + CBN hebben `in_praktijk`; geen enkele autoriteit heeft `valkuilen` |
| Grootte-cluster (3) | 2/3 | 1/3 | `kleine-vennootschap` heeft niets, `microvennootschap` heeft alleen `valkuilen` |
| Drie schema-records | 2/3 | 0/3 | `jaarrekening-schema` + `toelichting-jaarrekening` + `sociale-balans` missen `valkuilen` |
| PIE (1) | 0/1 | 0/1 | Centraal begrip, beide ontbreken |
| Hulpdagboeken (1) | 0/1 | 0/1 | Operationeel begrip |

Voor een minicursus over **Autoriteiten** is de huidige record-set ontoereikend zonder bijwerking — vandaar synthese-record (Deel B) als compenserende laag, maar individuele records moeten ook opgewaardeerd.

### Check C1 — Mechanische edges-/vergelijkingsparen-targets

Sweep over alle `edges[].target` en `vergelijkingsparen[].vergelijking_met` in de 59 records: **14 unieke targets bestaan niet als record** (mappen aan 21 verwijzende edges, gelogd in gaps.json). Belangrijkste:

| Missing target | Verwijzers | Resolutie |
|---|---|---|
| `dubbele-boekhouding` | wetboek-economisch-recht-boek-iii, boekhoudplichtige-onderneming | Vervang door canonieke slug `dubbel-boekhouden` (3 mismatches gelogd) |
| `boekhoudkundige-beginselen` | continuiteitsbeginsel, getrouw-beeld, onveranderlijkheid-boekingen, voorzichtigheidsbeginsel | Vervang door `aanvullende-boekhoudbeginselen` (4 mismatches gelogd) |
| `waarderingsregels` | continuiteitsbeginsel, inventaris, voorzichtigheidsbeginsel | Vervang door `waarderingsregels-jaarrekening` (3 mismatches gelogd) |
| `jaarafsluiting` | inventaris, overlopende-rekeningen | Vervang door `eindejaarsverrichtingen` |
| `accountant-itaa` | commissaris | Vervang door `itaa` |
| `verantwoordingsstuk` | dagboek, regelmatige-boekhouding | Nieuw record-kandidaat voor PO 1.1/1.2.III.D |
| `matching-principe`, `overeenstemmingsprincipe` | overlopende-rekeningen, voorzichtigheidsbeginsel | Mogelijk records.ontbreekt-gap, of bouwsteen in bestaand record |
| `ifrs-toepassingsgebied` | europees-boekhoudrecht | Nieuw record voor PO 1.3/1.4 |
| `materieel-belang-financiele-analyse` | getrouw-beeld-jaarrekening | Nieuw record voor PO 1.3 |
| `itaa-normen`, `obligatielening`, `vereffening`, `voorzieningen-voor-risicos-en-kosten` | Diverse | Optie: schrap edge, of records.ontbreekt-gap voor latere PO |

### Check C2 — Semantische coherentie + overlappende fenomenen

**Hoofdoverlap**: `jaarverslag` (PO 1.2-record, node_type begrip) ↔ `bestuursverslag` (PO 1.3-record, node_type procedure). Beide beschrijven hetzelfde wettelijke document (WVV art. 3:32 = Richtlijn 2013/34/EU art. 19). Beide records melden zelf de overlap in `cross_po_overlap`-veld. **Aanbeveling**: merge tot één canoniek record met behoud van procedure-stappen + bouwstenen, linked_anchors uit beide PO's. Gelogd als `records.overlappend-fenomeen` (twee spiegel-entries: prio midden).

**Synthese-kandidaat ontmaskerd**: `aanvullende-boekhoudbeginselen` (node_type begrip) aggregeert 4 bestaande beginselen-records zonder eigen extra inhoud — herclassificeer als `node_type: synthese`. Gelogd.

**Edge-types-zwakte**: alle 7 autoriteit-records gebruiken alleen edge-type `vereist-kennis-van`. Mist `vergelijkt-met` (FSMA ↔ NBB; ITAA ↔ IBR), `specialisatie-van` (PIE ↔ FSMA), `getriggerd-door` (lex specialis-wet). Niet als afzonderlijke gap gelogd maar geadresseerd via de FSMA `edges.geen-types`-gap.

### Aantallen gaps gelogd

| Prio | Aantal | Voorbeelden |
|---|---|---|
| hoog | 3 | fsma `vergelijkingsparen.ontbreekt`, public-interest-entity `in_praktijk.ontbreekt`, kleine-vennootschap `in_praktijk.ontbreekt` |
| midden | 19 | autoriteit-records uniforme rijkheid; jaarverslag↔bestuursverslag overlap; edges.target-ontbreekt voor dubbele-boekhouding/boekhoudkundige-beginselen/waarderingsregels/jaarafsluiting/matching-principe/accountant-itaa/ifrs-toepassingsgebied; aanvullende-boekhoudbeginselen herclassificatie |
| laag | 9 | Edge-target mismatches met laag-prio impact + 1 open-werk-entry |

Totaal **31 nieuwe gap-entries** in `data/extractie/gaps.json` (53 entries in totaal, alle valide JSON; dedup-check op record_id+aspect+status=open).

---

## Deel B — Synthese-records (drie clusters)

Drie synthese-records gemaakt onder `data/concepten/records/`, alle schema 1.4, status `seed`, `node_type: synthese`, confidence `inferred-from-aggregation` voor synthese-claims.

### 1. `autoriteiten-boekhoudrecht-landschap`

**Linked anchors**: 1.2.II + 1.2.I.E + 1.2.IV.E + 1.2.IV.F
**Gebaseerd op 9 concepten**: CBN, NBB, FSMA, ITAA, IBR, griffies, FOD Financiën, commissaris, PIE.
**Vergelijkingstabel**: 7 autoriteiten × 5 kolommen (wat doet ze · wettelijke basis · toepassingsgebied · wanneer raadplegen · bijzonderheden) met wikilinks naar elk autoriteit-record.
**Beslisboom**: `flowchart TD` — start vanuit dossiervraag → routeer naar juiste autoriteit. Mermaid-veilig (`&mdash;` in plaats van komma's in labels).
**5 kerninzichten**: ITAA vs IBR-onderscheid; Twin Peaks-model (NBB vs FSMA); twee neerleggingskanalen (NBB vs griffies); CBN-adviezen niet-bindend maar gezaghebbend; PIE-vennootschap triggert drie autoriteiten tegelijk.

**Pedagogische waarde**: compenseert de systemische dunte van individuele autoriteit-records. Stagiair krijgt in één klik antwoord op "naar wie met deze vraag?".

### 2. `vennootschapsgrootte-cascade`

**Linked anchors**: 1.2.IV.B + 1.2.IV.C + 1.2.IV.D + 1.2.IV.E + 1.2.IV.F + 1.2.IV
**Gebaseerd op 8 concepten**: groottecriteria-jaarrekening, kleine-vennootschap, microvennootschap, jaarrekening-schema, jaarverslag, commissaris, openbaarmaking-jaarrekening, sociale-balans.
**Vergelijkingstabel**: micro · klein · groot × 8 aspecten (drempels + schema + jaarverslag + commissaris + sociale balans + neerlegging + CSRD).
**Beslisboom**: van cijfers (VTE/omzet/balans) → klasse → cascade van zes verplichtingen. Inclusief verbondenheid-take (WVV art. 1:24 § 5).
**5 kerninzichten**: één klassering = zes verplichtingen (cascade); micro-extra-voorwaarde (geen moeder/dochter); twee-boekjaren-lock-in-regel; kleine dochter in grote groep wordt groot; onderscheid groottecriteria-jaarrekening vs groottecriteria-consolidatie.

**Pedagogische waarde**: directe examenvraag-beantwoording "welke verplichtingen voor mijn cliënt?". Verbindt 1.2.IV.B → de hele rest van 1.2.IV.

### 3. `rechtsbronnen-boekhoudrecht-piramide`

**Linked anchors**: 1.2.I + 1.2.I.A + 1.2.I.C + 1.2.I.D + 1.2.I.E + 1.2.I.F (dekt heel blok I)
**Gebaseerd op 7 concepten**: belgisch-boekhoudrecht, europees-boekhoudrecht, WER Boek III, WVV, KB-WVV, CBN-adviezen, rechtspraak.
**Vergelijkingstabel**: 5 lagen × 5 kolommen (bron · bindende kracht · voorbeeld · examen-tactiek).
**Beslisboom**: piramide-afdaling. Start bij wet → KB → CBN → rechtspraak afhankelijk van vraagtype; checkt EU-conformiteit bij twijfel.
**5 kerninzichten**: piramide is redeneer-as, geen mechanisch algoritme; directe werking van verordeningen (IAS) versus omzetting van richtlijnen; CBN-adviezen praktijk-gezag; geen precedenten-werking in België; Cijferzakboekje is hulpmiddel, geen primaire bron.

**Pedagogische waarde**: methodologisch — leert de stagiair *hoe* boekhoudrecht raadplegen, niet alleen *wat* erin staat.

---

## Mermaid-veiligheid

Alle drie de beslisbomen gebruiken:
- Geen `(n)`-haakjes in edge-labels.
- Geen komma's in edge-labels. Plaats van komma: `<br/>` voor regelafbreking, of `&mdash;` voor het-gedachten-streepje-effect.
- Wikilink-syntax `[[slug|Label]]` met backslash-escape in tabellen (`\\|`) voor JSON-string-encoding.

---

## Beperkingen + open werk

1. Examenvraag-classificatie voor PO 1.2 ontbreekt — Check A niet uitgevoerd. Open-werk-gap gelogd.
2. Wikilinks naar `groottecriteria-consolidatie`, `geconsolideerd-jaarverslag` (cross-PO 1.4) zijn aanwezig in synthese-records — die records bestaan al; gevalideerd.
3. Drie synthese-records overlappen onderling minimaal (autoriteit-rol bij grote vennootschap zit in beide cascade + autoriteiten-landschap), maar uit verschillend perspectief (verplichtingen-cascade vs autoriteit-keuze). Geen merge-aanbeveling.
4. `aanvullende-boekhoudbeginselen` is potentieel een vierde synthese-kandidaat (gelogd als gap met aspect `records.overlappend-fenomeen`). Niet gemaakt nu — twee Opus-cycles is voldoende voor één PO; ENRICH-pass kan deze ombouwen.

---

## Files-locatie

- Nieuwe synthese-records: 
  - `/Users/stivni/Documents/ITAA/certificaid/data/concepten/records/autoriteiten-boekhoudrecht-landschap.json`
  - `/Users/stivni/Documents/ITAA/certificaid/data/concepten/records/vennootschapsgrootte-cascade.json`
  - `/Users/stivni/Documents/ITAA/certificaid/data/concepten/records/rechtsbronnen-boekhoudrecht-piramide.json`
- Gaps-append: `/Users/stivni/Documents/ITAA/certificaid/data/extractie/gaps.json` (53 entries totaal, +31 nieuw)
- Dit rapport: `/Users/stivni/Documents/ITAA/certificaid/data/extractie/1.2/verify-synthese-rapport-2026-05-16.md`

Geen commit per opdracht. Geen Python-scripts gebruikt.
