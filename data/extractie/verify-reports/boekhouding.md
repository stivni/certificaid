# Verify-rapport: boekhouding

## Status
- Schema 2.2: ✓ (valide)
- Scope.in dekking: 4/4 topics gedekt (overzicht-discipline, organisatie, onderscheid handel/niet-handel/micro, interface andere disciplines)
- Voorbeelden: 3 (KMO-jaarcyclus, vereenvoudigd-vs-dubbel, interface-fiscaliteit) — concreet en didactisch
- Bron-discipline: OK met enkele kleine issues (zie below)
- Cross-relaties: OK — alle 8 targets bestaan (`belgisch-boekhoudrecht`, `boekhoudbeginselen`, `boekhoudplicht`, `dubbele-boekhouding`, `jaarrekening`, `eindejaarsverrichtingen`, `analytische-boekhouding`, `gecertificeerd-accountant`)

## Sterke punten
- Rijke kern (definitie + substantie + rationale) met goed onderscheid tussen wat/hoe/waarom
- Drie voorbeelden met concrete cijfers + boekingen + termijnen
- 3 valkuilen die typische student-misvattingen aanpakken (niet 'wat de wet zegt')
- Mermaid-diagram voor jaarcyclus
- Geldigheid expliciet uitgewerkt met wettelijke basis
- Goede balans tussen claims-met-bron en afgeleide synthese-tekst

## Issues
- [ ] **Schrijfstijl-smell — kruisreferentie in bouwsteen-tekst** (minor): bouwsteen `vormen-van-boekhouding` zegt "Mogelijk voor micro-eenmanszaken en kleine vzw's beneden de drempels van CBN 2019/12" — kan duidelijker dat dit een verwijs-relatie naar `boekhoudplicht` is (zit al in scope.out moet-verwijzen, maar in proza-tekst niet getagd).
- [ ] **Boeking 700 = klasse 7 (verkopen)** in adviseur-voorbeeld: rekening 70 / klasse 7-toelichting consistent (geen issue eigenlijk — wel correct).
- [ ] **Geen accountant_perspectief 'cliënt-zijde'** (minor): boekhouding-Σ presenteert alleen `eigen-kantoor-portefeuille` perspectief. Voor een Σ-cluster zou ook een 'cliënt-bestuursorgaan' perspectief logisch zijn (zoals jaarrekening dat wel heeft) — maar gegeven 'Σ-overzicht' karakter is dit niet kritiek.
- [ ] **Bron-context "ITAA-norm gedragslijnen relaties IBR"** (minor): naam van de norm is wat onvolledig — exacte norm-id zou bv. "ITAA-norm inzake gedragslijnen inzake de relaties van de leden van het ITAA met de Instituut van de Bedrijfsrevisoren" zijn. `ref` mag preciezer.
- [ ] **Speelruimte ontbreekt**: kader-record over hele discipline — een speelruimte rond "vereenvoudigd vs dubbele bij kleine eenmanszaak" zou nuttig zijn (de keuze die in valkuil 3 + voorbeeld 2 wordt aangeraakt). Nu impliciet in voorbeeld + valkuil verspreid.
- [ ] **Verworpen uitgaven autokosten 30%** in voorbeeld 3 (minor): vermenging — 30% is een willekeurig cijfer dat niet uit een algemene fiscale regel volgt. Werkelijk niet-aftrekbaar deel autokosten varieert per CO2-uitstoot (art. 198bis WIB92). Voorbeeld zegt "bv. 30%" wat oké is, maar kan verwarrend zijn voor stagiair. Suggestie: vervang door 50% expliciet als "didactisch versimpeld percentage".

## Verbeter-acties Pass 3
1. **Voeg cliënt-bestuursorgaan-perspectief toe** (parallel met `eigen-kantoor`): bestuursorgaan-verantwoordelijkheid + opdrachtbrief-tegenkant + WVV-aansprakelijkheid.
2. **Speelruimte toevoegen**: "Vereenvoudigde vs dubbele boekhouding bij kleine onderneming" met 2-3 opties + vuistregel.
3. **ITAA-norm bron-ref** verfijnen: exacte norm-naam + lid-nummer waar mogelijk.
4. **Autokosten-disclaimer** in voorbeeld 3: voeg explicietere flag toe dat 30% een didactisch versimpeld percentage is, met verwijzing naar `autokosten` of CO2-tabel.

## Severity-verdeling
- Critical: 0
- Major: 0
- Minor: 5
- Verdict: **OK — gepubliceerd-klaar met kleine cosmetische verbeteringen aanbevolen**
