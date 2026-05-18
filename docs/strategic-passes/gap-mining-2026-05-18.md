# Gap-mining rapport — strategische destillatie van `data/extractie/gaps.json`

**Datum**: 2026-05-18
**Scope**: 143 open gaps (status `open`) van VERIFY-runs 2026-05-15 t/m 2026-05-18, geclusterd op aspect, record-type en PO. Doel: zwaktes in EXTRACT v4-prompt en naam-cast detecteren, géén per-record verwerking.

## Executive summary

VERIFY-feedback wijst op vijf systemic patterns. Het meest urgente is **pattern 1 (referentiële drift in edges/vergelijkingsparen — 68 gaps, 48%)**: de prompt forceert geen slug-canonicalisatie, waardoor records vrolijk verwijzen naar niet-bestaande targets of varianten van hetzelfde slug (`dubbele-boekhouding` vs `dubbel-boekhouden`). Pattern 2 (in_praktijk-asymmetrie bij autoriteit-/begrip-records — 21 gaps) en pattern 3 (corpus-blindheid: records bestaan niet, maar worden wel gelinkt — 10 gaps + 6 vergelijkings-tegenhangers) zijn de tweede prioriteit. Pattern 4 (overlap-records, 10 gaps) en pattern 5 (procedurele-velden ongelijk gevuld binnen node_type, 9 stappen + 4 berekenings + 3 valkuilen = 16) tonen dat "uniforme rijkheid binnen type" (ADR-008 §13.1 regel 5) niet operationeel afgedwongen wordt. Aanbeveling: **archiveer de gaps.json als snapshot, en zet de vijf patronen om in concrete regels/prechecks in concept-extractie-v4 + een pre-write slug-resolver**.

---

## Pattern 1 — Referentiële drift in edges en vergelijkingsparen (68 gaps, 48%)

**Wat**: 54 `edges.target-ontbreekt` + 8 `vergelijkingsparen.target-ontbreekt` + 6 `vergelijkingsparen.ontbreekt` = 68 gaps. Drie sub-modi: (a) slug-variant (≈17 gaps: `dubbele-boekhouding` vs `dubbel-boekhouden`, `boekhoudkundige-beginselen` vs `aanvullende-boekhoudbeginselen`, `accountant-itaa` vs `itaa`), (b) doel-record bestaat helemaal niet (≈37 gaps: `resultatenrekening`, `jaarafsluiting`, `balans`, `werkkapitaalbehoefte`, `cash-ratio`, `vereffening`, `verantwoordingsstuk`), (c) vrije-tekst-verwijzing zonder gespiegelde edge (≈4 gaps).

**Vermoedelijke prompt/cast-oorzaak**: EXTRACT v4 vraagt edges op te nemen, maar krijgt geen slug-resolver of canonieke-slug-lijst geïnjecteerd in initial-ctx. Modus (a) toont dat de agent slugs ad-hoc construeert vanuit de tekst i.p.v. te lookuppen via concept-RAG. Modus (b) toont dat de prompt geen output-route heeft voor "ik wil hier linken maar het target ontbreekt" → een nieuwe `records.ontbreekt`-gap had bij EXTRACT-tijd zelf geschreven moeten worden.

**Suggestie**: (1) EXTRACT moet vóór elke edge een verplichte concept-RAG-lookup doen via records-API; gevonden → exacte slug, niet gevonden → automatisch een `records.ontbreekt`-gap-event creëren en de edge taggen als `target_status: "pending"` i.p.v. silently broken slug schrijven. (2) Bij vrije-tekst-verwijzing in `definitie`/`bouwstenen`/`in_praktijk` ("zie X", "vergelijk met Y"): post-write linter dwingt automatische spiegeling naar edges of vergelijkingsparen. (3) Concept-RAG levert canonieke-slug-rij bij elke retrieval (geen ad-hoc-slug-vorming).

---

## Pattern 2 — `in_praktijk` asymmetrisch leeg bij autoriteit-/begrip-records (21 gaps, 15%)

**Wat**: 21 records (FSMA, IBR, FOD Financiën, Griffies, PIE, kleine-vennootschap, ...) hebben node_type `begrip` of `autoriteit` met 0 `in_praktijk`-entries, terwijl peer-records van hetzelfde type 1-3 hebben. Klassieke "wanneer kom ik dit tegen in een dossier?"-blok.

**Vermoedelijke prompt/cast-oorzaak**: ADR-008 §13.1 regel 5 ("uniforme rijkheid binnen type") en ADR-008 §17 regel 13 ("voorbeeld-minimum per node_type") zijn in de prompt als principe geformuleerd, maar de prompt bevat geen **minimum-tabel per node_type** (autoriteit → ≥ 1 in_praktijk + ≥ 1 valkuil + ≥ 1 vergelijkingspaar; begrip → idem). Bij autoriteit-records ligt de wettelijke bron sterk op definitie/bevoegdheden, en de agent stopt zodra die rond is.

**Suggestie**: Voeg in EXTRACT v4 een **minimum-rijkheid-checklist per node_type** toe (autoriteit/begrip/regel/cluster/synthese/competentie) met expliciete getallen + één-zin-rationale. Voor autoriteit-records: verplicht in_praktijk met antwoord op "wanneer komt deze actor in een stagiair-dossier?". VERIFY-aspect `voorbeeld.ontbreekt` (ADR-008 §17) hoort bij EXTRACT al een self-check te zijn voor de agent disk schrijft.

---

## Pattern 3 — Corpus-blindheid: records die structureel gelinkt worden bestaan niet (10 gaps + spiegels)

**Wat**: 10 `records.ontbreekt` + 6 `vergelijkingsparen.target-ontbreekt` + overlap met pattern 1 modus (b). Voorbeelden: `resultatenrekening` (4 records linken via `onderdeel-van`), `jaarafsluiting` (4 records via `getriggerd-door`), `waarderingsregels` (3 records via `vereist-kennis-van`), `verantwoordingsstuk` (2), `balans`, `opbrengsten` (BE-GAAP-tegenhanger voor IFRS-15-vergelijking), `werkkapitaalbehoefte`, `cash-ratio`.

**Vermoedelijke prompt/cast-oorzaak**: Bij nieuwe-PO-event krijgt EXTRACT v4 anchor-bundles als initial-ctx, maar geen **gap-analyse vooraf** over welke centrale concepten in de bundles vóórkomen maar nog geen record hebben. De agent extraheert wat hij krijgt, niet wat hij collectief mist. Dit is een coverage-blindheid: de prompt vraagt records voor anchors, niet voor de **conceptuele aantrekkingspunten** die meerdere anchors delen.

**Suggestie**: Voor een PO-event: pre-EXTRACT script dat alle KB WVV-/wetsverwijzingen + termfrequenties in de anchor-bundles aggregeert en de top-N hoogfrequente termen die nog geen record hebben als verplichte "centrale ontbrekers" in initial-ctx zet. EXTRACT begint dan met die "anchor-concepten" voor hij naar specifieke anchors gaat. (Alternatief: gap-event-loop accepteren als normaal — VERIFY-feedback creëert het ontbrekende record automatisch in volgende cyclus.)

---

## Pattern 4 — Cross-PO overlap: hetzelfde fenomeen in twee records (10 gaps, 7%)

**Wat**: 10 `records.overlappend-fenomeen` — `getrouw-beeld` vs `getrouw-beeld-jaarrekening`, `jaarverslag` vs `bestuursverslag` (zelfs verschillende node_types!), `rechten-verplichtingen-buiten-balans` × 3 records, `bewaring-boekhoudstukken` vs `bewaartermijn-boekhouding`, `auditrisico-1-7-context` vs `auditrisicomodel`. Schema 1.4 regel "één fenomeen, één record" wordt geschonden.

**Vermoedelijke prompt/cast-oorzaak**: EXTRACT-events per PO werken geïsoleerd — de agent ziet wel concept-RAG bij retrieval, maar de prompt vraagt niet expliciet een **overlap-pre-check** vóór hij een nieuw record schrijft. Bovendien kan node_type tussen PO's verschillen (jaarverslag=begrip vs bestuursverslag=procedure), waardoor concept-RAG-matching op slug-similariteit faalt.

**Suggestie**: EXTRACT v4 verplicht een "near-duplicate"-check via concept-RAG voor élk nieuw record (semantische similarity op definitie + wettelijke grondslag, niet enkel slug). Bij hit > drempel → ofwel merge met bestaand (extra anchors toevoegen) ofwel `cross_po_overlap`-veld vullen + alleen het delta-perspectief opslaan. Synthese-records (node_type: synthese, ADR-008 §17) zijn de juiste pattern voor "overkoepelend overzicht" — de prompt moet die optie expliciet voorstellen i.p.v. een nieuw begrip-record te genereren.

---

## Pattern 5 — Procedurele/numerieke velden ongelijk gevuld binnen node_type (16 gaps, 11%)

**Wat**: 9 `stappen.onvolledig` + 4 `berekeningsmethode.*` (formule of voorbeeld) + 3 `valkuilen.ontbreekt`. Methode-records met 0 stappen terwijl peer-methodes 4-5 stappen hebben (herwaardering-component-benadering, afschrijvingsmethode-keuze, wisseling-procedure CBN 2022/08). Berekenbare concepten (prijsverschil-arbeid, vervaardigingskosten, flexibel budget) met definitie-only, geen formule, geen voorbeeld.

**Vermoedelijke prompt/cast-oorzaak**: Schema 1.4 voorziet stap-blok + formule-blok + bouwsteen-blok als toevoegingen, maar de prompt vraagt ze als optie i.p.v. als verplicht voor specifieke node_types. Dit is dezelfde "uniforme rijkheid"-leak als pattern 2, maar specifiek voor procedurele/numerieke velden i.p.v. illustratieve. Bovendien: ADR-008 §13.2 markeert zelf dat veld-gebonden VERIFY-checks falen zodra inhoud via een ander veld wordt geleverd (bv. stappen-met-rekenwerk i.p.v. formule-blok). Dat betekent ook dat de agent het ándere veld dán moet vullen — niet beide leeg laten.

**Suggestie**: (1) Per node_type een **verplichte content-pattern-tabel** in de prompt: cluster → minstens (stappen OF formules OF berekeningsmethode-met-voorbeeld); regel → minstens (definitie + valkuilen). (2) Self-check voor write: "heb ik voor dit node_type een procedure/formule/voorbeeld? Zo nee, fix dat eerst." (3) Content-pattern-based VERIFY-checks (ADR-008 §13.2 open punt) versnellen — niet veld-existence maar property-existence.

---

## Niet-systemische gaps die toch waardig zijn om te onthouden

- **`open-werk` × 3**: meta-flags voor lopende cursussen/handboek-uitbreidingen — geen prompt-issue, gewoon menselijke todo's.
- **`bron-corpus-uitbreiding` × 7**: corpus-gaten (IFRS 10/3/11/12 primaire tekst, Belgisch financial-analysis-handboek, doctrine-niveau enumeratie consolidatieverschil-oorzaken). Geen prompt-issue maar bron-pipeline-issue. Behoort thuis in Fase 1 (Bronnen-ETL) niet in EXTRACT-prompt-revisie.
- **`chunking-artefact` × 1**: één record met paragraaf-grens-ruis. Symptoom van ETL-issue (zie memory: tweetalige normen, structuurlabels als plain text).
- **`examenvragen.labels-ontbreken` × 1**: examen-pipeline-issue, niet concept-extractie.
- **`definitie.onvolledig` × 1** en **`edges.geen-types` × 1**: te weinig voorkomens om systemisch te noemen, maar worth een snelle scan in volgende VERIFY-pass.

## Aanbeveling

**Tussenoplossing**: Markeer alle 143 open gaps in `data/extractie/gaps.json` als `status: "archived-strategic-pass"` met `applied_door: "gap-mining-rapport-2026-05-18"`. Doel: behoud audit-trail, voorkom dat patronen-werk later als 1-op-1-todo herleeft.

**Niet weggooien.** De gaps.json is waardevol als snapshot van de pre-v4-staat; over 1-2 maand kan een diff tegen nieuwe VERIFY-runs aantonen of patronen 1-5 daadwerkelijk verminderd zijn na prompt-revisie.

**Concrete vervolgactie** (afzonderlijke design-sessie, Opus-werk): EXTRACT v4-prompt herzien op vijf concrete punten — (a) slug-resolver-regel + `target_status: pending`-tag, (b) minimum-rijkheid-tabel per node_type, (c) pre-EXTRACT centrale-ontbrekers-injectie voor PO-events, (d) verplichte near-duplicate-check + synthese-optie, (e) content-pattern-tabel per node_type voor procedurele/numerieke velden. Daarna pilot op één PO + nieuwe VERIFY-pass + meten of patronen 1-5 verzwakken.
