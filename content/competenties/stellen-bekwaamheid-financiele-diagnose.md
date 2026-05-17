---
title: Stellen van een complete bekwaamheid-financiële diagnose met aanbevelingen
  aan het management
tags:
- competentie
- po-1-9
programmaonderdelen:
- '1.9'
status: voorgesteld
schema_version: '1.1'
gegenereerd_uit: data/concepten/competenties/stellen-bekwaamheid-financiele-diagnose.yaml
gegenereerd_op: '2026-05-17'
---
# Stellen van een complete bekwaamheid-financiële diagnose met aanbevelingen aan het management

**⚖️ 30% · 🤖 70%**

> De alarmbel-procedure (WVV art. 7:228 en 2:52) en de signaleringsplicht naar Kamer voor Ondernemingen in Moeilijkheden (Boek XX WER) zijn wettelijk verankerd. De bestuursverslag-risicoparagraaf is KB WVV-verplichting. De synthese-methode en interpretatie zijn vakdoctrine. Vereist mens-review (praktijk_pct = 70%, op de grenslijn).

## Aanbevolen werkwijze

### 1. Plaatsen van elke ratio in zijn doel-categorie

Verdeel alle berekende ratio's over de vier doelen — liquiditeit, solvabiliteit, rentabiliteit, productiviteit — en toets per ratio of de teller en noemer correct geclassificeerd zijn.

**Waarom?** Bekwaamheid-niveau eist dat de student niet 'is 1,45 goed of slecht?' beantwoordt maar 'welk doel meet deze ratio en welk benchmark hoort daarbij?'. Verkeerde doel-toewijzing leidt tot verkeerde benchmark en verkeerde conclusie.

**📥 Input**:
- Ratio-set uit tool of handmatige berekening → **Per ratio: naam, teller, noemer, waarde** _(berekening)_

**📤 Output**:
- Gegroepeerde ratio-tabel → **Per doel-categorie: ratio's met waarde** _(nieuwe-balanspost)_

**🛠️ Hoe**:

1. Pas de classificatie toe uit [[ratio-vier-doelen-vergelijking]] §vier-doelen.
2. Liquiditeit: current ratio, quick ratio, werkkapitaal/omzet.
3. Solvabiliteit: solvabiliteitsratio (EV/TA), debt-equity-ratio (VV/EV), interest coverage.
4. Rentabiliteit: ROE, ROA, brutoresultaat-marge.
5. Productiviteit/groei: omzetgroei, TW per VTE, omzet/totaal-activa.
6. Plaats elke ratio in de juiste cel. Bij twijfel: welke beslissingsvraag beantwoordt de ratio?


**Grondslag**: [[ratio-vier-doelen-vergelijking]] §vier-doelen

### 2. Lezen in evolutie en sectorvergelijking

Voor elke ratio: bereken de evolutie over minstens 3 boekjaren en vergelijk met de sector-mediaan via NACE-code.

**Waarom?** Eén ratio = momentopname. Drie boekjaren = trend. Trend versus sector-evolutie = relatieve positie. Op bekwaamheid-niveau is de combinatie van deze drie lezingen verplicht.

**📥 Input**:
- Ratio-tabel (stap 1) + sector-data (Bel-First/NBB) → **Drie boekjaren + NACE-sector-mediaan + kwartielen** _(boekhoudkundig-bedrag)_

**📤 Output**:
- Tabel met drie-boekjaar-evolutie + sector-positie → **Per ratio: trend (↑/→/↓) + positie in sector (Q1-Q4)** _(nieuwe-balanspost)_

**🛠️ Hoe**:

1. Bereken Δ per ratio over 3 boekjaren volgens [[horizontale-analyse-jaarrekening]] §index-cijfers.
2. Klassificeer evolutie: stijgend, stabiel, dalend.
3. Vergelijk niveau met sector-mediaan volgens [[sectorvergelijking-financiele-analyse]] §NACE-classificatie.
4. Vergelijk EVOLUTIE met sector-evolutie — niet alleen niveau. Een onderneming die sneller daalt dan haar sector is alarmerend, ook al ligt ze nog boven sector-mediaan.
5. Documenteer in tabel met drie kolommen: niveau, eigen evolutie, sector-evolutie.


> [!example]- Voorbeeld: Rotex Roeselare NV — drie-boekjaar-evolutie 20X1-20X3
> Rotex Roeselare NV — drie-boekjaar-evolutie 20X1-20X3.
>
> 1. **Evolutie-tabel** 🧮
>
>    | Ratio | 20X1 | 20X2 | 20X3 | Trend Rotex | Sector 20X3 | Positie |
>    |---|---:|---:|---:|---|---:|---|
>    | Current ratio | 1,80 | 1,60 | 1,45 | ↓ | 1,80 | Onder, in Q1 |
>    | Solvabiliteit | 38% | 39% | 40% | ↑ | 32,5% | Boven, in Q3 |
>    | ROE | 28% | 30% | 32,5% | ↑ | 18,7% | Ver boven, in Q4 |
>    | TW per VTE | € 140K | € 145K | € 150K | ↑ | € 130K | Boven |
>    
>

**Grondslag**: [[interpretatie-financiele-ratios]] §evolutie-lezen, [[horizontale-analyse-jaarrekening]], [[sectorvergelijking-financiele-analyse]]

### 3. Triangulair lezen — combineren van de vier doelen

Lees rentabiliteit, solvabiliteit, liquiditeit en productiviteit samen — identificeer patronen die alleen zichtbaar zijn in de combinatie.

**Waarom?** Falen ontstaat zelden uit één doel-categorie maar uit interactie. Een winstgevende, solvabele onderneming kan toch in een liquiditeitscrisis komen via groeiende BBK. Op bekwaamheid-niveau wordt deze triangulaire lezing verwacht.

**📥 Input**:
- Evolutie-tabel (stap 2) → **Vier doelen met trends + sector-positie** _(berekening)_

**📤 Output**:
- Patroon-diagnose → **Identificatie van type ondernemings-profiel** _(conclusie)_

**🛠️ Hoe**:

1. Stel per doel-categorie de status vast: boven/onder benchmark, evolutie stijgend/dalend.
2. Match het patroon met typische cases uit [[interpretatie-financiele-ratios]] §triangulair-lezen en [[falen-van-de-onderneming]] §vroege-signalen:
   - Rentabel + solvabel + dalende liquiditeit + groeiende omzet = "groei verbrand werkkapitaal" → niet alarm maar wel monitor.
   - Dalende rentabiliteit + dalende solvabiliteit + stabiele liquiditeit = "geleidelijk falen" → diepere analyse vereist.
   - Hoge ROE + lage solvabiliteit + dalende current ratio = "leverage-piek" → kwetsbaar bij cyclus-omslag.
   - Hoge rentabiliteit + hoge solvabiliteit + alle ratio's boven sector = "premium-positie" → bevestiging gezond.
3. Documenteer het patroon in één zin: 'Onderneming X vertoont profiel Y omdat ratio's A, B en C samen op Z wijzen.'


> [!example]- Voorbeeld: Rotex Roeselare NV — triangulair lezen 20X3
> Rotex Roeselare NV — triangulair lezen 20X3.
>
> 1. **Patroon-identificatie** 💬
>
>    Patroon: hoge rentabiliteit (ROE 32,5%) + hoge solvabiliteit (40%) + dalende current ratio (1,45)
>    + boven-sector-productiviteit (TW/VTE € 150K).
>    Diagnose: 'premium-positie met efficient werkkapitaalbeheer'. De dalende current ratio is geen
>    zwakte maar het resultaat van een verkortte cyclus en groeiende activiteit — bevestigd door
>    de positieve trend in solvabiliteit en rentabiliteit.
>    
>

**Grondslag**: [[interpretatie-financiele-ratios]] §triangulair-lezen, [[falen-van-de-onderneming]] §vroege-signalen

### 4. Bevestigen via kwantitatieve modellen en kwalitatieve signalen

Bereken Altman Z en/of Ohlson O, lees de risicoparagraaf van het bestuursverslag, en bevestig of weerleg de triangulaire diagnose.

**Waarom?** Modellen + kwalitatieve signalen + ratio-analyse moeten convergeren naar dezelfde diagnose. Divergentie = onderzoek welke component klopt.

**📥 Input**:
- Triangulaire diagnose (stap 3) + bestuursverslag → **Patroon + risicoparagraaf + Altman/Ohlson outputs** _(conclusie)_

**📤 Output**:
- Bevestigde diagnose → **Eensluidende of tegenstrijdige bevindingen** _(conclusie)_

**🛠️ Hoe**:

1. Bereken Altman Z en/of Ohlson O volgens [[kwantitatieve-financiele-diagnose]] §vergelijkingstabel. Voor Belgische KMO's: gebruik Z' of Z'' of vermeld toepassings-beperking.
2. Lees de risicoparagraaf in het bestuursverslag volgens [[risicoparagraaf-bestuursverslag]] §inhoud — welke risico's signaleert het management zelf?
3. Vergelijk:
   - Patroon (stap 3) ↔ Altman/Ohlson zone ↔ risicoparagraaf-bevindingen.
   - Eensluidend gezond: alle drie wijzen op gezond profiel.
   - Eensluidend distress: alle drie wijzen op falen.
   - Tegenstrijdig: onderzoek welke component een eenmalig event of strategische keuze representeert.
4. Formuleer de eindconclusie in één paragraaf met expliciete vermelding van de drie informatiebronnen.


> [!example]- Voorbeeld: Rotex Roeselare NV — bevestiging diagnose 20X3
> Rotex Roeselare NV — bevestiging diagnose 20X3.
>
> 1. **Convergentie-check** 🧮
>
>    | Bron | Output | Verdict |
>    |---|---|---|
>    | Triangulair lezen (stap 3) | Premium-positie | Gezond |
>    | Altman Z | 3,15 (safe zone) | Gezond |
>    | Ohlson p | 0,05 | Gezond |
>    | Bestuursverslag-risicoparagraaf | Vermeldt energieprijs-volatiliteit als enig risico | Beheersbaar |
>    
>
> 2. **Conclusie** 💬
>
>    Eensluidend gezond op vier informatiebronnen. Eindconclusie: 'Rotex Roeselare NV is financieel
>    gezond in 20X3. Ratio's wijzen op premium-positie binnen sector; kwantitatieve modellen plaatsen
>    de onderneming in de safe zone; het bestuursverslag signaleert enkel een beheersbaar
>    energieprijs-risico.'
>    
>

**Grondslag**: [[kwantitatieve-financiele-diagnose]], [[risicoparagraaf-bestuursverslag]], [[falen-van-de-onderneming]]

### 5. Formuleren van aanbevelingen aan het management

Vertaal de diagnose naar 3-5 concrete aanbevelingen voor het bestuursorgaan — actiegerichte adviezen met meetbare deelpunten.

**Waarom?** Een diagnose zonder aanbevelingen is een onafgewerkt rapport. Bekwaamheid-examen verwacht dat de student het bedrijfsmodel begrijpt en advies kan geven, niet alleen ratio's oplezen.

**📥 Input**:
- Bevestigde diagnose (stap 4) → **Patroon + ondersteunend bewijs** _(conclusie)_

**📤 Output**:
- Lijst aanbevelingen → **3-5 actiegerichte adviezen met onderbouwing per advies** _(document)_

**🛠️ Hoe**:

1. Per zwakte uit de diagnose: formuleer een actiegerichte aanbeveling met meetbaar effect.
2. Voor risico-signalen: stel monitor-indicatoren voor (welke ratio onder welke drempel triggert wat?).
3. Bij wettelijke verplichting (Boek XX WER signaleringsplicht, alarmbel-procedure WVV): documenteer dit expliciet als de drempels overschreden zijn.
4. Volgorde: prioriteit hoog naar laag. Een liquiditeitsrisico komt voor een rentabiliteits-optimalisatie.
5. Sluit af met een review-tijdstip (bv. 'volgende balansanalyse over 12 maanden').


> [!example]- Voorbeeld: Verffabriek Veurne BV (falen-in-ontwikkeling) — aanbevelingen aan bestuursorgaan
> Verffabriek Veurne BV (falen-in-ontwikkeling) — aanbevelingen aan bestuursorgaan.
>
> 1. **Aanbevelingen-lijst** 💬
>
>    1. **DRINGEND** (binnen 30 dagen): Aanmelding bij Kamer voor Ondernemingen in Moeilijkheden
>       (KOM) conform Boek XX WER — alarmbel-criteria bereikt (EV < 50% kapitaal, en negatieve
>       CFO over 2 boekjaren).
>    2. **HOOG** (binnen 3 maanden): Herstructureringsplan opstellen met cash-projectie 12 maanden
>       — externe begeleiding aanbevolen.
>    3. **MIDDEN** (binnen 6 maanden): Verkoop niet-strategische activa overwegen om
>       werkkapitaal vrij te maken.
>    4. **MONITOR**: Maandelijkse cash-projectie + wekelijkse opvolging openstaande
>       handelsvorderingen.
>    5. **REVIEW**: Volgende formele financiële analyse na publicatie tussentijdse cijfers
>       (kwartaal-bemerking).
>    
>

**Grondslag**: [[falen-van-de-onderneming]] §drie-stadia, WVV art. 7:228 + Boek XX WER

> [!warning]- Maak aanbevelingen actiegericht en meetbaar — vermijd algemeenheden zoals 'verbeter de rentabiliteit'.
>
> _Vaak fout gedaan_: Vage aanbevelingen die niet uitvoerbaar zijn op managementsniveau.
>
> _Grondslag_: Beroepspraktijk financiële diagnose

> [!warning]- Vermeld wettelijke signaleringsplicht expliciet bij overschrijding van drempels.
>
> _Vaak fout gedaan_: Alarmbel-procedure (WVV art. 7:228) of KOM-signalering verzwijgen uit voorzichtigheid — dat is geen voorzichtigheid maar nalatigheid.
>
> _Grondslag_: WVV art. 7:228 + Boek XX WER

> [!warning]- Lijst aanbevelingen in prioriteits-volgorde, niet thematisch.
>
> _Vaak fout gedaan_: Aanbevelingen thematisch ordenen (eerst alle liquiditeits-adviezen, dan alle rentabiliteits-adviezen) zonder rekening te houden met dringendheid.
>
> _Grondslag_: Beroepspraktijk diagnose-rapportering


## Voorbeelden

> [!example]- Meubelzaak Mertens BV: ROE 12% (sector 15%), solvabiliteit 22% (sector 30%), current ratio 1,1 (sector 1,5), groei omzet…
> **Conclusie**: Sofie Janssens identificeert het patroon 'geleidelijke verslechtering in alle vier doelen + onder-sector + onder-trend'. Altman Z' = 1,75 (distress zone bij Z'-cutoff 1,23-2,90 → grey-distress). Diagnose: 'falen in ontwikkeling, stadium 1-2'. Aanbevelingen: (1) jaarbalans-projectie opmaken; (2) overleg bestuursorgaan over strategische heroriëntering; (3) cash-projectie 6 maanden; (4) voorbereiding alarmbel-toets indien EV verder zakt onder 50% kapitaal.
>
> **Grondslag**: [[interpretatie-financiele-ratios]], [[falen-van-de-onderneming]], [[kwantitatieve-financiele-diagnose]]
>
> **Redenering**: De combinatie van vier dalende doelen + sector-onderperformance + falen-modellen in distress-richting is een robuuste basis voor 'falen-in-ontwikkeling'-diagnose. Aanbevelingen zijn proportioneel met stadium 1-2 — nog geen formele signaleringsplicht, maar wel voorbereiden.

> [!example]- Zelena Bio NV (groeibedrijf IFRS): hoge ROE 25%, lage solvabiliteit 18% (sector 25%), current ratio 1,3 (sector 1,5), om…
> **Conclusie**: Patroon: 'high-growth, leverage-piek'. Lage solvabiliteit + hoge ROE = leverage-effect; lage current ratio + sterke omzetgroei = werkkapitaal verbrand door groei. Altman Z = 2,2 (grey zone) — typisch voor groeibedrijven. Diagnose: 'gezond profiel maar leverage-kwetsbaar bij cyclus-omslag'. Aanbevelingen: (1) monitor schulden-aflossings-schema versus CFO; (2) overweeg kapitaalverhoging om solvabiliteit boven 25% te brengen; (3) stress-test 20% omzetkrimp-scenario.
>
> **Grondslag**: [[interpretatie-financiele-ratios]] §triangulair-lezen, [[kwantitatieve-financiele-diagnose]]
>
> **Redenering**: Hoge groei + lage solvabiliteit is geen distress-signaal als CFO meegroeit. Maar de kwetsbaarheid bij cyclus-omslag moet expliciet in de aanbevelingen — bekwaamheid-niveau toetst dit vooruit denken.


## Gebaseerd op concepten

[[interpretatie-financiele-ratios]] · [[falen-van-de-onderneming]] · [[kwantitatieve-financiele-diagnose]] · [[ratio-vier-doelen-vergelijking]] · [[sectorvergelijking-financiele-analyse]] · [[horizontale-analyse-jaarrekening]] · [[risicoparagraaf-bestuursverslag]]
## Voortkomend uit

- **Taken**: 1.9.taak.1
- **Kenniselementen**: 1.9.I, 1.9.V, 1.9.V.E, 1.9.VI, 1.9.VI.A
