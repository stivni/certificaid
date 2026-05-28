# Verify-rapport: dubbele-boekhouding

## Status
- Schema 2.2: ✓ (valide)
- Scope.in dekking: 5/5 topics gedekt (dagboek→grootboek→proefbalans · MAR · debet/credit · periodiek · klasse-onderscheid)
- Voorbeelden: 4 (aankoop+BTW, verkoop+BTW, proefbalans, klasse-0 borg) — concreet met getallen, niet abstract
- Bron-discipline: OK — WVV/WER/KB/CBN-mix correct
- Cross-relaties: alle 4 targets bestaan (`boekhouding`, `boekhoudbeginselen`, `jaarrekening`, `boekhoudplicht`)

## Sterke punten
- 3-laag kern met historische context (Pacioli 1494) en functionele triple-doel (foutendetectie · volledigheid · gelijktijdig)
- 7 bouwstenen die MAR/dagboek/grootboek/proefbalans/afsluit/klasse-0 dekken
- Boekingen met exacte rekening-codes (604/411/4400 · 4000/70/451)
- MAR-tabel als weergave
- Tijdslijn-synthese 8-stappen brondocument → jaarrekening
- Valkuil 2 "proefbalans = correct" is een belangrijke didactische correctie

## Issues
- [ ] **MAR-tabel — klasse 4 actief vs passief** (minor): bouwsteen `mar-structuur` rij voor klasse 4 zegt "Vorderingen (D) + KT-schulden (C)". De technisch correctere formulering: klasse 4 bevat ZOWEL vorderingen (40, 41) ALS schulden (42-48); de plaats op balans hangt af van subrekening. De huidige tabel mengt "Plaats" en "Karakter" door elkaar. Minder belangrijk voor stagiair maar conceptueel onnauwkeurig.
- [ ] **MAR klasse 1 — formulering kunstig** (minor): substantie zegt "passief: 1-eigen vermogen + voorzieningen + LT-schulden; 4-KT-schulden+vorderingen-passief; actief: 2-vaste activa, 3-voorraden, 4-vorderingen-actief, 5-liquide middelen". Dit is moeilijk leesbaar — leestekens en structuur kan helderder. Klasse 1 = passief LT (eigen vermogen + voorzieningen + LT-schulden). 
- [ ] **Klasse 8/9 wat over-vereenvoudigd** (minor): rij in MAR-tabel zegt "Sluit- en analytische rekeningen". Klasse 89 is bestemming/sluitrekening; klasse 9 is analytisch (vrij gebruik). Beide hebben verschillende functies — kort split kan duidelijker.
- [ ] **Voorbeeld 1 — rekening 4400 'Leveranciers'** (minor): standaard MAR-rekening is 440 (leveranciers); 4400 is een sub-rekening op subniveau. Mogelijk inconsistent met algemeen gebruik. Soms wordt 4400 gebruikt voor leveranciers-handel (vs 4404 voor te ontvangen facturen). Verifieer convention.
- [ ] **Voorbeeld 4 klasse-0 — rekening 000/001** (minor): MAR Bijlage 1 klasse 0 gebruikt subklassen 00-09 voor verschillende soorten rechten/verplichtingen. "000" en "001" zijn placeholder; werkelijke MAR-rekening voor "Zekerheden persoonlijke borg ontvangen" zou 00 of een specifieke 00x-subrekening zijn. Didactisch geen probleem, maar streng-correct kan beter.
- [ ] **`vergelijkbaar_met boekhoudplicht`** (minor): relatie tussen "dubbele-boekhouding" en "boekhoudplicht" als vergelijkbaar is conceptueel scherper dan "vereist" — maar de gelijkenissen/verschillen die zijn opgegeven zijn meer aanvullend dan vergelijkend. Kan eventueel verschuiven naar `verwijst-naar` of `valt_onder` parent — minor.
- [ ] **Geen `accountant_perspectieven` cliënt-zijde** (minor): alleen `kantoor-bij-boekingsdiscipline` — voor een Σ-cluster is dit acceptabel maar kan worden uitgebreid met cliëntperspectief.

## Verbeter-acties Pass 3
1. **MAR-tabel klasse 4** herformuleren — actief (40,41) vs passief (42-48) duidelijk uit elkaar trekken, of bij elke subklasse expliciet
2. **Substantie-tekst** klassen 1-7 in proper Nederlandse zin herschrijven — leesbaarheid
3. **Klasse 8 vs 9** split in MAR-tabel — 89=sluitrekening, 9=analytisch (vrij)
4. **MAR-rekening-codes verifiëren** in voorbeelden (4400 vs 440, klasse-0 nummering) — desnoods sub-rekeningen documenteren in scope.in
5. **Relatie-type `vergelijkbaar_met boekhoudplicht`** heroverwegen → mogelijk gewoon `vereist` of `verwijst-naar`

## Severity-verdeling
- Critical: 0
- Major: 0
- Minor: 7
- Verdict: **OK — sterke didactische kern; verbeteringen vooral op MAR-detailprecisie**
