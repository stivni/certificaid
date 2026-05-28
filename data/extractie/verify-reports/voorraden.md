# Verify-rapport: voorraden

## Status
- Schema 2.2: ✓ (valide)
- Scope.in dekking: 5/5 topics gedekt (MAR 30-39 · FIFO/LIFO/GMP · waardeverminderingen · klasse 37 onderhanden · cross IAS 2)
- Voorbeelden: 1 (Zelena Bio FIFO) — voldoet net, beneden de "≥2 vereist"-richtlijn van cluster-verify
- Bron-discipline: OK — KB-art. 3:35-39 + MAR + IAS 2 expliciet
- Cross-relaties: alle 3 targets bestaan (`boekhouding`, `eindejaarsverrichtingen`, `ifrs`)

## Sterke punten
- Heldere kern met 3 lagen + concrete MAR-klasse-rubricering (30-37)
- 5 bouwstenen (FIFO/LIFO/GMP/waardevermindering/onderhanden) — alle vier waarderingsmethoden + onderhanden werk
- Valkuilen pakken twee belangrijke fouten aan: LIFO onder IFRS + bestendigheidsbeginsel-fout
- Speelruimte "Voorraadwaarderingsmethode" met 3 opties + vuistregel
- Concept_type `balanspost` past
- Cross IAS 2 (IFRS-verschil) goed uitgewerkt in valkuil 1 + relatie

## Issues
- [ ] **MAJOR — Slechts 1 voorbeeld** (major volgens richtlijn ≥2): cluster-verify-prompt zegt "Voorbeelden: N (≥2 vereist)". Slechts 1 voorbeeld (Zelena Bio FIFO). Onderhanden werk + waardevermindering klantgoed worden in bouwstenen aangeraakt, maar geen full-fledged voorbeeld met cijfers. Pass 3: voeg minstens 1 extra voorbeeld toe (bv. onderhanden bouwwerf percentage-of-completion).
- [ ] **GEEN `accountant_perspectieven`** (major voor een balanspost waarbij waarderingskeuze + voorraadtelling concrete accountant-acties zijn): valkuil-beschrijving en speelruimte raken handelings-aspecten aan maar er is geen perspectieven-blok met rollen (boekhouder voor inventaris-procedure; auditor voor voorraadtelling; fiscaal voor LIFO/FIFO-impact). Voor een balanspost met sterke audit-implicatie zou minstens 1 perspectief verwacht zijn.
- [ ] **GEEN `gebruikscontext`** (minor): geen voor/niet_voor/voorwaarden/voordeel/risico. Voor een balanspost is dit niet strict-verplicht maar `geldigheid` ontbreekt ook (default in-voege, ok). Voor consistentie met andere balanspost-records: minimaal `voorwaarden` (laagste-waarde-toets op balansdatum) of `risico` (manipulatie-risico) wenselijk.
- [ ] **GEEN `voorkennis_leespad`** (minor): kader + voorvereisten ontbreken. Voor pedagogische leespad-coherentie: kader=`boekhouding` of `jaarrekening`, voorvereiste=`dubbele-boekhouding` / `boekhoudbeginselen`.
- [ ] **Bron-ref `KB 29-04-2019 WVV — bijlage MAR`** (minor): de MAR is opgenomen in een ANDER KB (KB 21-10-2018) dan KB 29-04-2019 (waarderingsregels). Vermenging van twee KB's onder één naam in primary_bronnen + bron-refs ("KB 29-04-2019 WVV — bijlage MAR" — geen MAR-bijlage in KB 29-04-2019). Verifieer + corrigeer.
- [ ] **Bouwsteen `waardevermindering-voorraad` rekening 6310** (minor): wordt voor "terugneming" gebruikt. Volgens MAR: 631 Waardeverminderingen op voorraden — Toevoeging vs 6310 Terugneming op voorraden — verifieer juiste sub-codering. Subschema-conventie van CBN is dat tegen-rekeningen vaak 6X1 of een aparte 6XX-9 cijfer hebben.
- [ ] **Bouwsteen `waardering-lifo`** noemt "verboden onder IFRS" maar fiscaal heeft LIFO óók een uitdovend regime sinds bepaalde wetswijzigingen (controleer); zeker noemenswaardig in Belgische context.
- [ ] **Voorbeeld 1 — narratief vermengt twee scenarios** (minor): primaire scenario heeft marktwaarde 13 EUR (geen wv nodig), alternatief 11 EUR (wel wv). Beide in één voorbeeld — leesbaar maar didactisch beter als 2 aparte voorbeelden of subscenario's.

## Verbeter-acties Pass 3
1. **Voeg minstens 1 extra voorbeeld toe**: onderhanden werk (klasse 37) pro-rata met bouwwerf-cijfers, of definitieve oninvorderbare voorraad met BTW-correctie
2. **Voeg `accountant_perspectieven` toe** — minstens rol `boekhouder` (voorraad-inventarisatie + waardevermindering boeken) en `auditor` (voorraadtelling bijwonen)
3. **Voeg `gebruikscontext`** — minimaal `voorwaarden` (laagste-waarde-toets) + `risico` (manipulatie audit-risico)
4. **Voeg `voorkennis_leespad`** — voorvereisten + kader + naast_relevant + volgkennis
5. **MAR-bron-ref fix**: split KB 29-04-2019 (waardering art. 3:35-39) van KB 21-10-2018 (MAR-bijlage) in primary_bronnen + bron-velden
6. **Fiscaal LIFO-context** kort vermelden in bouwsteen of valkuil (BE-fiscaal-restrictions, indien relevant)

## Severity-verdeling
- Critical: 0
- Major: 2 (te weinig voorbeelden + geen perspectieven)
- Minor: 6
- Verdict: **Inhoudelijk goed maar OPMERKBAAR DUNNER dan andere records in sample — Pass 3 verbreden gewenst**
