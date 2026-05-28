# Verify-rapport: jaarrekening

## Status
- Schema 2.2: ✓ (valide)
- Scope.in dekking: 7/7 topics gedekt (synthesedocumenten · 3 schema's · waarderingsregels · jaarverslag · sociale balans · openbaarmaking · controle)
- Voorbeelden: 3 (BV TopSlot verkort, termijn-tijdslijn, NV MidCorp groot+commissaris) — concreet, met cijfers + tijdslijnen
- Bron-discipline: OK — gevarieerd (WVV/KB/CBN), CBN-S100 inhoudelijk wat dun
- Cross-relaties: 2 targets MISSING — zie issues

## Sterke punten
- Zeer rijke inhoud: 3-laag kern + 5 sub-concepten + 7 bouwstenen + 3 voorbeelden + 4 valkuilen + 2 speelruimtes
- 2 accountant_perspectieven (eigen-kantoor + cliënt-bestuursorgaan) met 5 rollen totaal — voorbeeldig dekking
- Speelruimte "Schema-keuze" en "Waarderingsregels-keuze" met heldere voor/nadelen + vuistregel
- Drie verschillende weergaven gebruikt (tabel, balans_snapshot, tijdslijn, proza)
- `vergelijkbaar_met geconsolideerde-jaarrekening` met rijke gelijkenissen/verschillen/verwarring_risico
- Geldigheid: status + sinds + wettelijke_basis + toelichting volledig
- Drempels per 28-03-2024 (verhoging) correct verwerkt (€11.250.000 / €6.000.000 / €900.000 / €450.000)

## Issues
- [ ] **MISSING TARGET: `groottecategorie-vennootschap`** (major): bestaat niet — wel `vennootschap-groottecategorieen.json`. Twee relaties verwijzen naar verkeerde id (relatie `beinvloed_door` + scope.out item). Moet **hernoemd** of het bestaande record moet hernoemd worden. Cross-record consistentie defect.
- [ ] **MISSING TARGET: `nationale-bank-van-belgie`** (major): relatie `gepubliceerd_via` verwijst naar niet-bestaand record. Moet ofwel record aangemaakt worden (autoriteit-type) ofwel relatie verwijderd. Mogelijk hoort dit bij `nbb`-id of moet aparte actor-record worden.
- [ ] **CBN-S100 bron-ref onverkort** (minor): twee citaten van "CBN-advies S100" zonder verdere context. CBN heeft S100 als sociale-balans-advies, maar ref-id "CBN-S100" is geen standaard format (anders dan "2024/07"). Verifieer + uniformeer.
- [ ] **NBB-toeslag bedragen** (minor): voorbeeld zegt "€120 na max. 8 maanden, oplopend tot €1.200 bij meer dan 9 maanden voor grote vennootschappen" — confidence `geciteerd` op art. 3:10 WVV. Bedragen zelf komen NIET uit art. 3:10 (alleen het schadevermoeden); bedragen staan in apart KB en cijferzakboekje. Bron-mix met ai_model voor bedragen is fair, maar het primaire art-citaat suggereert dat het uit WVV komt. Suggestie: split — schadevermoeden vs concrete tarieven.
- [ ] **Subconcept `jaarverslag-bestuursorgaan` is `concept_type: procedure`** (minor): semantisch is een jaarverslag een document/output (eerder `kader` of `instrument`), niet een procedure (= stappen-flow). Mogelijke type-mismatch.
- [ ] **Bouwsteen `consolidatie-verwijzing` met `bouwsteen_type: begrip`** (minor): inhoudelijk is dit eerder een verwijzing/cross-ref dan een begrip — vermeld dat verdere uitwerking elders staat. Past beter als content in scope.out (al gedekt) ipv volledige bouwsteen.
- [ ] **Voorbeeld 2 — termijn-berekening** noemt "WVV art. 3:1, § 1 + 3:10". De 6-maanden-termijn voor AV-bijeenroeping zit echter in art. 5:97 (BV) / 7:139 (NV) — `art 3:1, § 1` regelt het opmaken door bestuursorgaan, niet de AV-termijn op zich. Bronref enigszins onnauwkeurig.

## Verbeter-acties Pass 3
1. **CRITICAL — Fix MISSING TARGETS**: 
   - hernoem relatie-target `groottecategorie-vennootschap` → `vennootschap-groottecategorieen` (in 1 relatie + 1 scope.out item)
   - ofwel record `nationale-bank-van-belgie` aanmaken (autoriteit-type, lichtgewicht), ofwel relatie omzetten naar prozaverwijzing
2. **CBN-S100 bron-ref**: verifieer exacte CBN-advies-nummering voor sociale balans, hercodeer naar consistent format (bv. "S100" of "2014/8")
3. **NBB-toeslag claim split**: schadevermoeden (geciteerd, WVV art. 3:10) vs bedragen (afgeleid, cijferzakboekje)
4. **Subconcept-types**: heroverweeg jaarverslag-bestuursorgaan → `kader` of `instrument`; verwijder of vereenvoudig bouwsteen `consolidatie-verwijzing` (al gedekt door scope.out)
5. **AV-termijn-ref** in voorbeeld 2: voeg art. 5:97 BV / 7:139 NV expliciet toe voor 6-maandentermijn

## Severity-verdeling
- Critical: 0
- Major: 2 (missing targets)
- Minor: 5
- Verdict: **Substantieel goed maar BLOCKING op cross-relatie-consistentie** — fix MISSING TARGETS voor publicatie
