# Verify-rapport: eindejaarsverrichtingen

## Status
- Schema 2.2: ✓ (valide)
- Scope.in dekking: 5/5 topics gedekt (inventaris · waarderings-correcties · overlopende rekeningen · resultaatverwerking · afsluit+heropening)
- Voorbeelden: 4 (afschrijving · waardevermindering klant · overlopende huur · resultaatverwerking) — alle met concrete cijfers en boekingen
- Bron-discipline: OK — WER/KB/CBN goed gestratificeerd
- Cross-relaties: 2 targets MISSING — zie issues

## Sterke punten
- Concept_type `procedure` correct gekozen (gestructureerde stappen-flow over tijd)
- Stap-bouwstenen 1-5 systematisch met wetbasis (WER art. III.89, KB art. 3:23, CBN 148/4, CBN 2018/25)
- Tijdslijn-synthese voor 31/12-afsluitcyclus met datums en acties (zeer praktisch)
- 4 valkuilen aan typische student-misvattingen (inventaris = voorraadtelling; voorzieningen = pot; klasse 49 = alleen huur; going-concern overslaan)
- 3 perspectieven-rollen (boekhouder · auditor · adviseur) met concrete check-lists
- WCO-context in voorbeeld 2 + BTW-handling-noot (correct: vermindering op exclusief BTW)
- Wisselkoers-bouwsteen specifiek toegevoegd (CBN 152/1)

## Issues
- [ ] **MISSING TARGET: `uitkering-aan-aandeelhouders`** (major): relatie `triggert` + scope.out item verwijzen naar niet-bestaand record. Wel aanwezig: `winstuitkering.json`. Moet hernoemd worden.
- [ ] **MISSING TARGET: `controle-opdracht`** (major): relatie `gecontroleerd_door` + scope.out item verwijzen naar niet-bestaand record. Mogelijk hoort dit bij `audit-opdracht` of `commissaris` — verifieer.
- [ ] **Voorbeeld 4 — wettelijke reserve onnauwkeurig** (minor): tekst zegt "Wettelijke reserve is statutair vastgelegd op 10% van kapitaal — momenteel reeds 5.000 EUR (volledig)". Voor BV onder WVV is de wettelijke reserve niet meer wettelijk verplicht (art. 5:142 vermeldt niet meer de oude 5%/10%-regel zoals dat voor NV — art. 7:211 — wel doet). Voor BV: alleen statutair indien voorzien. Het voorbeeld gebruikt BV ABC met "statutaire" reserve — dat klopt, maar de citatie `WVV art. 5:142` is niet de juiste basis (5:142 = uitkeringstest). Voor NV: art. 7:211 wel correct. Heroverweeg ref of vennootschapsvorm.
- [ ] **Voorbeeld 4 — Belasting niet meegenomen** (minor): stap 1 zegt "winst 100.000 EUR (na belastingen)" — maar dan: stap 4 boeking 14 / 133 + 471 + 14 — geen klasse 79 (resultaatverwerking) tussen. Verwacht: 691 D / 791+792+793+796 C. Te springachtige boeking-presentatie; legt didactisch klasse 79 niet uit (die WEL als kern wordt vermeld). Kan beter worden uitgewerkt richting record `resultaatverwerking` als verwijzing.
- [ ] **Stap 4-bouwsteen "BV niet meer wettelijk verplicht"** (minor): klopt voor wettelijke reserve onder WVV, maar de zin "verplicht voor NV's en BV's voorheen, voor BV niet meer wettelijk verplicht onder WVV" is correct. Wel: het scope.in vermeldt deze nuance niet. Ok.
- [ ] **Confidence 'afgeleid' op stap 1** (minor): stap-1 bouwsteen heeft confidence `geciteerd` op WER art. III.89 — perfect want letterlijk citaat. Goede praktijk.
- [ ] **Going-concern bouwsteen niet als bouwsteen** (minor): going-concern wordt aangeraakt in substantie + valkuil 4, maar niet als eigen bouwsteen (regel of stap). Voor een eindejaarsproof zou 'going-concern-toets' als specifieke bouwsteen passen (CBN 2018/18 is in primary_bronnen vermeld). Pass 3-suggestie.
- [ ] **Heropening klasse 89 — herhaling** (minor): stap 5-bouwsteen zegt "balansposten worden 'gesloten' en heropend voor jaar N+1 via klasse 89" — feitelijk worden klasse-6/7 saldi via 89 afgesloten + winst/verlies overgebracht naar klasse 14; balansposten worden technisch heropend via "openingsbalans" of via klasse 89 in sommige software. Formulering kan helderder.

## Verbeter-acties Pass 3
1. **CRITICAL — Fix MISSING TARGETS**:
   - Hernoem `uitkering-aan-aandeelhouders` → `winstuitkering` (1 relatie + 1 scope.out item)
   - Verifieer `controle-opdracht` — mogelijk `audit-opdracht` of nieuwe record nodig, ofwel verwijzing herstellen
2. **Voorbeeld 4 — wettelijke reserve**: schakel naar NV (art. 7:211) OF expliciteer statutaire BV-reserve (geen wetref); en koppel duidelijker aan klasse 79 mechaniek
3. **Voeg going-concern-toets** als expliciete bouwsteen met CBN 2018/18-ref toe
4. **Stap-5-bouwsteen** herformuleer klasse 89-mechaniek (klasse 6/7 saldi via 89 → klasse 14)

## Severity-verdeling
- Critical: 0
- Major: 2 (missing targets)
- Minor: 6
- Verdict: **Inhoudelijk uitstekend; BLOCKING op cross-relatie-consistentie**
