# ENRICH-run enrich-run-20260515T144255Z — Rapport

**Programmaonderdeel**: 1.4
**Uitgevoerd op**: 2026-05-15T16:50:00+00:00 (UTC)
**Subagent-model**: claude-opus-4-7
**Records verwerkt**: 2
**Gaps verwerkt**: 2 (2 hoog / 0 midden / 0 laag)
**Correcties aangebracht**: 1 (verplicht `corrected_from` aanwezig)
**Records-ontbreekt gaps overgeslagen (taak voor EXTRACT)**: 0

---

## Samenvatting per record

### `consolidatieverschil` — gap `oorzaken.dedup`

- **Resultaat**: `oorzaken[]` teruggebracht van 5 naar 4 items.
- **Consolidatie**: items 1 ("Overpaid goodwill") en 5 ("Niet-geactiveerde immateriële waarden") samengevoegd tot één item op positie 1. Beide oorspronkelijke teksten zijn integraal bewaard in `corrected_from` (array met twee strings). `correction_reason` legt uit dat beide items hetzelfde fenomeen vanuit twee invalshoeken (prijsperspectief vs. substantieperspectief) beschreven.
- **Behouden**: alle vier chunk-id's uit de oorspronkelijke twee items zijn opgenomen in `_provenance.inputs` van het samengevoegde item (`CBN-2013-03-…__sec_voorbeeld-1`, `Richtlijn-2013-34-EU__art_24__sub_lid1-lid14`, `KB-WVV-2019__art_3_102`, `KB-WVV-2019__art_3_103`).
- **Confidence**: `inferred-from-aggregation` (synthese van 4 chunks over 2 bronnen, incl. Europese richtlijn).
- **Andere oorzaken-items**: ondergewaardeerde activa, verwachte ongunstige resultaatsontwikkeling, overgewaardeerde passieven — ongewijzigd behouden.
- **enrich_runs**: nieuw object toegevoegd aan de bestaande `enrich_runs[]`-array (run 20260515T141848Z blijft staan).

### `intragroep-eliminaties` — gap `berekeningsmethode.concreet_voorbeeld`

- **Resultaat**: nieuw `berekeningsmethode[]`-blok toegevoegd (1 methode, schema 1.2) met:
  - `naam`: "Eliminatie van niet-gerealiseerde winst in voorraad (intra-groepsverkoop)"
  - `formule`: combineert KB WVV art. 3:134, 2° (balans) en art. 3:136, 1° (P&L)
  - `ratio`: verklaart waarom de marge op het deel dat nog in de groep zit niet gerealiseerd is
  - `stappen`: 6 stappen, incl. pro-rata bij evenredige consolidatie (art. 3:140, a)
  - `concreet_voorbeeld`: scenario uit de gap-tekst — M verkoopt 100 aan D, marge 30 %, restvoorraad 40 → niet-gerealiseerde winst = 12; balans-eliminatie −12 op voorraden/reserves; P&L-eliminatie −100 op zowel omzet als kostprijs verkochte goederen.
- **Confidence**: `inferred-from-aggregation`. Het veld `inferred_motivation` is toegevoegd om expliciet te documenteren dat de bundle geen letterlijk cijfervoorbeeld voor voorraadwinst-eliminatie bevat (de relevante chunks `KB-WVV-2019__art_3_106` (art. 3:134) en `KB-WVV-2019__art_3_107` (art. 3:136) bevatten enkel de eliminatieregel, geen werkvoorbeeld; CBN 2022/11 §upstream/downstream geeft alleen de algemene regel). De cijfers (100/30 %/40) zijn een minimaal, conventioneel voorbeeld en geen overname. De boekhoudkundige logica volgt strikt uit de wettekst.
- **Provenance**: 3 chunk-id's (`KB-WVV-2019__art_3_106`, `KB-WVV-2019__art_3_107`, `CBN-2022-11-vermogensmutatiemethode__sec_intra-groepsverkopen-upstream-downstream-sales`).
- **Bestaande velden**: `verplichting`, `stappen[6]`, `in_praktijk[2]`, `vergelijkingsparen[3]`, `valkuilen[2]` ongewijzigd behouden.
- **enrich_runs**: nieuw `enrich_runs[]`-array aangemaakt onder top-level `_provenance` (was er nog niet).

---

## Bronnen geraadpleegd

- `bundle-consolidatieverschil-enrich-run-20260515T144255Z.json` — 458 chunks; relevante chunks gevonden:
  - `KB-WVV-2019__art_3_102` (art. 3:130 — boeking)
  - `KB-WVV-2019__art_3_103` (art. 3:131 — afschrijving)
  - `Richtlijn-2013-34-EU__art_24__sub_lid1-lid14` (residu = goodwill)
  - `CBN-2013-03-…__sec_voorbeeld-1` (positief consolidatieverschil-voorbeeld)
- `bundle-intragroep-eliminaties-enrich-run-20260515T144255Z.json` — 440 chunks; relevante chunks gevonden:
  - `KB-WVV-2019__art_3_106` (art. 3:134 — balans-eliminatie)
  - `KB-WVV-2019__art_3_107` (art. 3:136 — P&L-eliminatie)
  - `CBN-2022-11-…__sec_intra-groepsverkopen-upstream-downstream-sales` (algemene regel)
- Het bundle bevat **geen** gewerkt cijfervoorbeeld voor niet-gerealiseerde voorraadwinst — vandaar `inferred-from-aggregation` + expliciete `inferred_motivation` op de berekeningsmethode.

---

## Bewaakte hard-contract-regels

- [x] Geen velden of array-items verwijderd zonder motivering.
- [x] Correctie (`consolidatieverschil.oorzaken` dedup) heeft `corrected_from` (volledige teksten van beide samengevoegde items), `correction_reason` en `correction_source`.
- [x] Geen niet-gevraagde velden toegevoegd buiten de gap-aspecten.
- [x] Elke nieuwe claim heeft chunk-id provenance.
- [x] Geen verzonnen wetsartikelnummers (alle vermelde art. 3:127–3:142, art. 3:105, art. 24 Richtlijn 2013/34/EU komen letterlijk voor in de bundle of het bestaande record).
- [x] Confidence-discipline: `inferred-from-aggregation` waar synthese over meerdere bronnen/chunks plaatsvindt; geen `grounded` zonder directe chunk-dekking.

---

## Vervolg

Gaps gemarkeerd in `data/extractie/gaps.json`:
- `consolidatieverschil` / `oorzaken.dedup` → `status: "enriched-pending-verify"`, `applied_door: "enrich-run-20260515T144255Z"`.
- `intragroep-eliminaties` / `berekeningsmethode.concreet_voorbeeld` → `status: "enriched-pending-verify"`, `applied_door: "enrich-run-20260515T144255Z"`.

Volgende stap: VERIFY-pass (blok 4) op beide records om te bevestigen dat:
1. Het samengevoegde oorzaken-item dekkend is voor klassieke examenvragen "vier voornaamste oorzaken" en geen blinde vlek introduceert.
2. Het cijfervoorbeeld bij `intragroep-eliminaties.berekeningsmethode` consistent is met de regelgeving en didactisch bruikbaar.
