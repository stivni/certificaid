# Verify-rapport: voorzieningen

## Status
- Schema 2.2: ✓ (valide)
- Scope.in dekking: 4/4 topics gedekt (MAR 160-163 · voorzichtigheidsbeginsel · waardering · onderscheid schulden/uitgestelde belastingen)
- Voorbeelden: 2 (waarborg-product + grote herstelling) — beide met cijfers en boekingen, voldoet aan ≥2
- Bron-discipline: OK — KB-art. 3:23, 3:33 + MAR 16
- Cross-relaties: alle 3 targets bestaan (`boekhouding`, `boekhoudbeginselen`, `schulden-op-korte-termijn`, `uitgestelde-belastingen`)

## Sterke punten
- Heldere kern met 3 lagen + concrete MAR-klasse 16 sub-rubricering
- Onderscheid met (a) schulden (b) uitgestelde belastingen (zelfde klasse 16 maar ander fenomeen) expliciet via 2 `vergelijkbaar_met`-relaties met gelijkenissen/verschillen/verwarring_risico
- Erkenningscriteria (3 cumulatieve voorwaarden) helder uitgewerkt — sluit aan bij IFRS IAS 37 zonder dat letterlijk te kopiëren
- Waardering inclusief actualisatie LT-voorzieningen (uitgewerkt)
- 2 valkuilen: voorziening vs reserve (klassieke fout) + voorziening zonder bestaande gebeurtenis (cookie-jar)
- Concept_type `balanspost` correct
- Boekingen met exacte rekeningen (637/163, 6370 voor terugneming)

## Issues
- [ ] **GEEN `accountant_perspectieven`** (major voor regelmatige verrichting met sterke audit-impact): voorzieningen zijn een typisch oordeels-gevoelig gebied waar de accountant/auditor expliciet positie inneemt (waardering best-estimate, terugneming-timing, fiscale aftrekbaarheid). Geen rollen-blok aanwezig. Voor risk-area is dit een tekort.
- [ ] **GEEN `gebruikscontext`** (minor): geen `voor/niet_voor/voorwaarden/voordeel/risico/geldigheid`. Voor balanspost niet strict-verplicht, maar `voorwaarden` (cumulatieve drie erkenningscriteria) zou ook hier kunnen herhaald worden.
- [ ] **GEEN `voorkennis_leespad`** (minor): pedagogische leespad ontbreekt.
- [ ] **Bouwsteen `criteria-voorziening-erkenning`** (minor): zegt "(juridisch of feitelijk, bv. publiek aangekondigde herstructurering)". Het "publiek aangekondigd" criterium komt uit IAS 37 (constructive obligation) — onder Belgisch boekhoudrecht is het niet strict zo geformuleerd. CBN spreekt eerder van "verplichting waarvan het waarschijnlijk is". Verifieer of deze IFRS-formulering correct is voor B-GAAP, of explicieer als IAS 37-parallel.
- [ ] **Bron-ref "Klasse 13 vs Klasse 16"** in valkuil 1 (minor): niet een echt bron-ref maar een interne verwijzing. KB-art voor reserves: art. 3:81 e.v. + WVV-art. Verifieer.
- [ ] **Categorie 168 Uitgestelde belastingen** als sub-rubricering van klasse 16 — wel correct, maar het record verwijst naar apart uitgestelde-belastingen-record (correct). Substantie-tekst zegt "168 Uitgestelde belastingen (zie apart record)" — perfect.
- [ ] **GEEN `speelruimte`** (minor): keuze tussen actualisatie of niet (voor LT-voorzieningen) is een typische keuze met afweging — kan als speelruimte. Ook: niveau van best-estimate (conservatief vs neutraal).
- [ ] **Voorbeeld 2 grote herstelling** (minor): zegt "elk jaar wordt 40.000 EUR geboekt" — zonder concrete boeking. Voorbeeld is wel didactisch helder maar zou nog konkreter zijn met expliciete jaarboeking 637/162 D/C 40.000.
- [ ] **Bron-confidence "geciteerd" bij "art. 3:33"** voor erkenningscriteria (minor): art. 3:33 KB heeft de algemene regel voor voorzieningen — de 3 cumulatieve criteria zoals geformuleerd (bestaande verplichting + waarschijnlijke uitstroom + betrouwbare schatting) zijn echter IAS-37-derived in formulering. Onder B-GAAP zelf is de wettekst minder expliciet. Confidence kan beter `afgeleid` zijn voor de 3-criteria-formulering, of toelichting "cf. internationale praktijk + CBN" toevoegen.

## Verbeter-acties Pass 3
1. **Voeg `accountant_perspectieven`** met minstens rol `boekhouder` (voorzieningen aanleggen + terugnemen) + `auditor` (waardering toetsen, dossier-onderbouwing)
2. **Voeg `gebruikscontext`** — voorwaarden (3 cumulatieve criteria) + risico (manipulatie-risico cookie-jar + audit-aandacht)
3. **Voeg `voorkennis_leespad`** — kader=`boekhouding` of `jaarrekening`, voorvereisten=`boekhoudbeginselen` + `dubbele-boekhouding`
4. **Confidence-fix** erkenningscriteria: ofwel `afgeleid` met IAS 37-context, ofwel CBN-advies-ref toevoegen die deze 3 criteria expliciet in B-GAAP-formulering noemt
5. **Voeg `speelruimte` actualisatie LT-voorziening** (al-actualiseren vs niet-actualiseren) met voor/nadeel
6. **Voorbeeld 2 — voeg expliciete boeking** voor jaarlijkse opbouw 637 D / 162 C 40.000 EUR
7. **IFRS-cross-relatie** met IAS 37 (parallel met voorraden-ifrs-relatie): nu in scope.out `mag-verwijzen` maar geen `vergelijkbaar_met`-relatie

## Severity-verdeling
- Critical: 0
- Major: 1 (geen perspectieven)
- Minor: 8
- Verdict: **Inhoudelijk goed kernrecord; mist contextlagen + perspectieven voor volledigheid**
