# Verify-rapport: resultaatverwerking

## Status
- Schema 2.2: ✓ (valide)
- Scope.in dekking: 5/5 topics gedekt (MAR klasse 79 · te bestemmen winst · reservevorming · dividend · cross winstuitkering)
- Voorbeelden: 1 (BV bestemmingsboeking in bouwsteen) — strikt 0 in `voorbeelden[]`-array
- Bron-discipline: OK — WVV art. 7:211, 5:153, 5:142, KB art. 3:3, MAR
- Cross-relaties: alle 2 targets bestaan (`boekhouding`, `winstuitkering`)

## Sterke punten
- Concept_type `procedure` correct
- Bestemmingsschema heel concreet uitgewerkt met klasse 79-sub-rubricering (791/792/793/794/795/796)
- Erkenning van WVV-onderscheid BV (art. 5:153) vs NV (art. 7:211) voor wettelijke reserve — belangrijk
- Verwijzing naar dubbele uitkeringstest (nettoactief + liquiditeit) voor BV/CV (art. 5:142-143)
- 2 valkuilen: wettelijke reserve dynamiek + dividend zonder uitkeringstest
- Heldere kern met 3 lagen (definitie + substantie + rationale)

## Issues
- [ ] **MAJOR — Geen voorbeelden in `voorbeelden[]`-array** (major): de boeking-illustratie zit IN een bouwsteen (`boeking-resultaat-naar-bestemming`). Geen aparte `voorbeelden[]` top-level. Cluster-verify-richtlijn: "≥2 voorbeelden" — record voldoet niet.
- [ ] **MAJOR — Voorbeeld in bouwsteen heeft tegenstrijdigheid** (major): Bouwsteen `boeking-resultaat-naar-bestemming` zegt "5 % naar wettelijke reserve (2.500 EUR — totaal wordt 10.500 EUR < 10.000 EUR... eigenlijk volledig 2.000 EUR want max bereikt bij 10.000 EUR, dan stoppen)". Berekening fout en verwarrend: 8.000 + 2.000 = 10.000 (= 10% van kapitaal 100.000), inderdaad correct cap op 2.000. Maar de tussenstap "2.500 EUR — totaal wordt 10.500" is een denkfout die NIET in een didactisch record hoort. Inline correctie maakt het rommelig. Pass 3: herschrijf cleaner.
- [ ] **GEEN `accountant_perspectieven`** (major): resultaatverwerking is bij uitstek adviseur-rol (uitkeringstest doen, advies aan AV over bestemming) en boekhouder-rol (klasse 79-boeking + roerende voorheffing). Geen rollen aanwezig.
- [ ] **GEEN `gebruikscontext`** (minor): geldigheid + trigger_start (boekjaareinde) + trigger_einde (AV-goedkeuring) zou natuurlijk passen.
- [ ] **GEEN `voorkennis_leespad`** (minor).
- [ ] **GEEN `speelruimte`** (minor): klassiek speelruimte-onderwerp (dividend vs reserve vs overgedragen) — substantiele afweging die NIET in valkuil 2 zit (die gaat over LEGITIMITEIT, niet over OPTIMALE bestemming). Pass 3-suggestie.
- [ ] **Schade-vermoeden RV-tarief 30%** (minor): NIET letterlijk in bron — moest 30% RV op gewoon dividend correct zijn (2026). VVPR-bis 15% wordt elders genoemd. Bron-ref: WIB92 art. 269 (tarief RV) zou bij dividend-RV-claim moeten staan. Nu impliciet.
- [ ] **Bouwsteen-tekst stap-1 "rekening 690 Te bestemmen winst"** (minor): standaard MAR is 691 (debet — beschikbaar) / 690 (Te bestemmen verlies — credit). Verifieer juiste rekening-codes voor "Te bestemmen winst" vs "Te bestemmen verlies".
- [ ] **Voorbeeld in bouwsteen — RV-boeking** (minor): "9.000 / 4530 Verschuldigde RV" — RV op dividend is fiscale schuld, ja. Maar het voorbeeld noemt dit niet expliciet. Verwijzing naar `aangifte-RV` of `voorheffingen-pb` zou logisch zijn.
- [ ] **Confidence/bronnen voorbeeld-bouwsteen** (minor): confidence `afgeleid` met bron MAR — past, maar de WIB92-ref voor RV (art. 269) ontbreekt.

## Verbeter-acties Pass 3
1. **CRITICAL — Voeg ≥2 `voorbeelden[]` top-level toe**: 
   - Voorbeeld 1: NV met te bestemmen winst (gebruik 7:211 wettelijke reserve 5/10-regel)
   - Voorbeeld 2: BV met dividend onder uitkeringstest (5:142 — netto-actief + liquiditeit testen)
2. **Herschrijf bouwsteen `boeking-resultaat-naar-bestemming`** — verwijder denkfout-tussenstap, maak berekening clean
3. **Voeg `accountant_perspectieven`** — adviseur (advies aan AV over bestemming + uitkeringstests) + boekhouder (klasse 79 + RV-boeking)
4. **Voeg `gebruikscontext`** met trigger_start (boekjaareinde) + trigger_einde (AV-goedkeuring)
5. **Voeg `voorkennis_leespad`** — kader=`jaarrekening`, voorvereisten=`eindejaarsverrichtingen`, volgkennis=`winstuitkering`
6. **Voeg `speelruimte`** "Bestemming winst: dividend vs reserve vs overgedragen" met fiscale + bedrijfseconomische voor/nadelen
7. **WIB92-ref toevoegen** voor RV-tarief in bouwsteen
8. **Rekeningnummering** 690/691 verifiëren

## Severity-verdeling
- Critical: 0
- Major: 3 (geen voorbeelden top-level, denkfout in bouwsteen-voorbeeld, geen perspectieven)
- Minor: 7
- Verdict: **Te dun — Pass 3 substantieel verbreden noodzakelijk; minst rijke record in sample**
