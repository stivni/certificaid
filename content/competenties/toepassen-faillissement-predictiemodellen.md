---
title: Toepassen van kwantitatieve faillissement-predictiemodellen (Altman Z en Ohlson
  O)
tags:
- competentie
- po-1-9
programmaonderdelen:
- '1.9'
status: voorgesteld
schema_version: '1.5'
gegenereerd_uit: data/concepten/records/toepassen-faillissement-predictiemodellen.json
gegenereerd_op: '2026-05-18'
---
# Toepassen van kwantitatieve faillissement-predictiemodellen (Altman Z en Ohlson O)

**⚖️ 5% · 🤖 95%**

> Faillissement-predictiemodellen zijn internationale vakdoctrine (Altman 1968, Ohlson 1980). Belgisch recht (Boek XX WER, alarmbel-procedure WVV) levert wel het juridische kader voor falen, maar de modellen zelf zijn geen onderdeel van Belgisch wetgevend kader. Vereist mens-review wegens praktijk_pct > 70%.

## Aanbevolen werkwijze

### 1. Verzamelen van de input-ratio's voor Altman Z

Bereken de vijf ratio's die Altman vereist — NBK/TA, IW/TA, EBIT/TA, MVE/VV en O/TA.

**Waarom?** Het Altman-model is een gewogen lineaire combinatie van vijf ratio's. Eén ratio uit context plaatsen volstaat niet — alle vijf moeten samen worden berekend.

**📥 Input**:
- Balans + RR + (indien beursgenoteerd) beurskoers → **Werkkapitaal, totaal activa, ingehouden winst, EBIT, marktwaarde EV, totaal vreemd vermogen, omzet** _(boekhoudkundig-bedrag)_

**📤 Output**:
- Vijf ratio's → **NBK/TA, IW/TA, EBIT/TA, MVE/VV, O/TA — telkens als ratio** _(berekening)_

**🛠️ Hoe**:

1. Bereken werkkapitaal volgens [[werkkapitaal]] §absolute-tegenhanger. Deel door totaal activa.
2. Lees ingehouden winst (rubriek 14) en deel door totaal activa.
3. Bereken EBIT = bedrijfsresultaat + financiële opbrengsten (vóór financiële kosten en belastingen). Deel door totaal activa.
4. Voor MVE: beursgenoteerd = marktkapitalisatie; niet-beursgenoteerd = boekwaarde EV. Totaal vreemd vermogen = rubrieken 16 + 17 + 42-48. Deel.
5. Omzet uit RR (rubriek 70), deel door totaal activa.
6. Documenteer elke ratio met de bron-rubrieken voor traceerbaarheid.


> [!example]- Voorbeeld: Rotex Roeselare NV (niet-beursgenoteerd) — Altman input 20X3
> Rotex Roeselare NV (niet-beursgenoteerd) — Altman input 20X3.
>
> 1. **Vijf ratio's berekenen** 🧮
>
>    | Variabele | Formule | Waarde |
>    |---|---|---:|
>    | NBK/TA | € 8.000.000 / € 30.000.000 | 0,27 |
>    | IW/TA | € 2.100.000 / € 30.000.000 | 0,07 |
>    | EBIT/TA | € 6.000.000 / € 30.000.000 | 0,20 |
>    | MVE/VV | € 12.000.000 / € 18.000.000 | 0,67 |
>    | O/TA | € 50.000.000 / € 30.000.000 | 1,67 |
>    
>

**Grondslag**: [[altman-z-score]] §berekeningsmethode

### 2. Berekenen van de Altman Z-score en positioneren in de zones

Bereken Z via de gewogen som en plaats het resultaat in een van de drie zones — distress, grey of safe.

**Waarom?** De zones zijn de pedagogische tools die de student moet kennen — niet alleen het cijfer maar de interpretatie ervan.

**📥 Input**:
- Vijf ratio's (stap 1) → **NBK/TA, IW/TA, EBIT/TA, MVE/VV, O/TA** _(berekening)_

**📤 Output**:
- Z-score + zone-classificatie → **Z (dimensieloos) + label distress/grey/safe** _(conclusie)_

**🛠️ Hoe**:

1. Pas de Altman-formule toe uit [[altman-z-score]] §formules: Z = 1,2×(NBK/TA) + 1,4×(IW/TA) + 3,3×(EBIT/TA) + 0,6×(MVE/VV) + 1,0×(O/TA).
2. Classificeer volgens [[altman-z-score]] §drempelwaarden:
   - Z < 1,81 = distress zone (hoog faillissementsrisico binnen 2 jaar).
   - 1,81 ≤ Z < 2,99 = grey zone (onzeker, aanvullende analyse).
   - Z ≥ 2,99 = safe zone (gezond op basis van model).
3. Documenteer welke variant van het Altman-model je gebruikt: origineel (1968, productiebedrijven beursgenoteerd) of Z' (niet-beursgenoteerd) of Z'' (niet-productie). Voor Belgische KMO's is Z' of Z'' gepaster.


> [!example]- Voorbeeld: Rotex Roeselare NV — Altman Z berekening 20X3
> Rotex Roeselare NV — Altman Z berekening 20X3.
>
> 1. **Gewogen som** 🧮
>
>    Z = 1,2 × 0,27 + 1,4 × 0,07 + 3,3 × 0,20 + 0,6 × 0,67 + 1,0 × 1,67
>    Z = 0,32 + 0,10 + 0,66 + 0,40 + 1,67
>    Z = **3,15**
>    
>
> 2. **Zone-classificatie** 💬
>
>    Z = 3,15 ≥ 2,99 → **safe zone** = financieel gezond op basis van origineel Altman-model.
>    Bij gebruik Altman Z' (niet-beursgenoteerd, cut-offs 1,23 en 2,90): Z' wordt licht anders berekend; voor examen volstaat het origineel model met opmerking over toepassingsbeperking.
>    
>

**Grondslag**: [[altman-z-score]] §drempelwaarden

### 3. Berekenen van de Ohlson O-score voor probabiliteit

Bereken het Ohlson O-model voor de faillissement-kansprobabiliteit (logit-model, 9 variabelen).

**Waarom?** Ohlson levert een kans (0 tot 1) — een fundamenteel ander type output dan Altman's zone. Op bekwaamheid-niveau wordt verwacht dat de student deze techniek-verschillen begrijpt, niet dat hij de exacte coefficiënten uit het hoofd kent.

**📥 Input**:
- Balans + RR → **9 variabelen Ohlson (zie hoe-instructie)** _(berekening)_

**📤 Output**:
- O-score + kansprobabiliteit → **O (logit) + p (kans tussen 0 en 1)** _(conclusie)_

**🛠️ Hoe**:

1. Volg [[ohlson-o-score]] §formule: O = − 1,32 − 0,407×log(TA) + 6,03×(VV/TA) − 1,43×(NBK/TA) + 0,076×(KT-schulden/Vlottende activa) − 1,72×X1 − 2,37×(NI/TA) − 1,83×(CFO/VV) + 0,285×X2 − 0,521×Δ NI.
   Waar: X1 = 1 als VV > TA, anders 0; X2 = 1 als NI < 0 in zowel laatste 2 jaren, anders 0.
2. Bereken p = e^O / (1 + e^O) — kans tussen 0 en 1.
3. Interpretatie: p > 0,5 = voorspelling faillissement; p < 0,5 = voorspelling overleven. Een onderneming met p = 0,8 heeft volgens het model 80% kans op faillissement binnen 2 jaar — niet dat ze zeker failliet gaat.


> [!example]- Voorbeeld: Verffabriek Veurne BV in vereffening — Ohlson O 20X3
> Verffabriek Veurne BV in vereffening — Ohlson O 20X3.
>
> 1. **Variabelen** 🧮
>
>    TA = € 5.000.000, VV = € 6.000.000 (negatief EV: − € 1M)
>    log(TA) = 6,70
>    VV/TA = 1,20 (> 1 → X1 = 1)
>    NBK/TA = − 0,40 (negatief werkkapitaal)
>    KT-schulden / Vlottende activa = € 2.400.000 / € 2.000.000 = 1,20
>    NI/TA = − 0,15
>    CFO/VV = − 0,20 / 6,0 = − 0,03
>    NI < 0 in 20X2 én 20X3 → X2 = 1
>    Δ NI (genormaliseerd) = − 0,40
>    
>
> 2. **O-score** 🧮
>
>    O = − 1,32 − 0,407 × 6,70 + 6,03 × 1,20 − 1,43 × (− 0,40) + 0,076 × 1,20 − 1,72 × 1 − 2,37 × (− 0,15) − 1,83 × (− 0,03) + 0,285 × 1 − 0,521 × (− 0,40)
>    O ≈ + 4,2
>    p = e^4,2 / (1 + e^4,2) ≈ **0,99 (= 99% faillissement-kans)**
>    
>
> 3. **Interpretatie** 💬
>
>    Verffabriek Veurne BV scoort p ≈ 0,99 — bevestiging van diagnose 'in vereffening / manifest falen'. Vergelijk met Altman Z = 0,8 (distress zone): beide modellen wijzen in dezelfde richting → robuuste diagnose.
>    
>

**Grondslag**: [[ohlson-o-score]] §formule

### 4. Triangulair lezen — combineren met kwalitatieve signalen

Combineer de output van Altman én Ohlson met kwalitatieve signalen uit het bestuursverslag, risicoparagraaf en sector-context.

**Waarom?** Geen enkel kwantitatief model is op zichzelf voldoende. Een eensluidende slechte score van Altman én Ohlson + kwalitatieve signalen = robuste diagnose. Een tegenstrijdige score = vereist verdere analyse.

**📥 Input**:
- Altman Z + Ohlson p + bestuursverslag → **Drie outputs samen** _(conclusie)_

**📤 Output**:
- Diagnose-conclusie → **Eensluidende of tegenstrijdige bevindingen + aanbeveling** _(conclusie)_

**🛠️ Hoe**:

1. Plaats Altman-zone en Ohlson-probabiliteit naast elkaar volgens [[kwantitatieve-financiele-diagnose]] §in_praktijk.
2. Eensluidend slecht (Z < 1,81 + p > 0,5): bevestig met kwalitatieve signalen uit [[falen-van-de-onderneming]] §vroege-signalen (dalende rentabiliteit, opgevraagde leningen, methode-wijzigingen). Diagnose: 'falen in ontwikkeling' of 'manifest falen'.
3. Eensluidend gezond (Z ≥ 2,99 + p < 0,2): bevestig dat sector-evolutie geen plotse storingen voorspelt.
4. Tegenstrijdig: onderzoek de oorzaak — bv. EBIT/TA hoog (Altman gunstig) maar NI < 0 (Ohlson ongunstig) wijst op hoge afschrijvingen of belastingoptimalisatie. Verdere case-by-case analyse vereist.
5. Voor commissaris-mandaat: bij eensluidend slecht + bevestiging → signaleringsplicht naar bestuursorgaan + (bij verergerd risico) Kamer voor Ondernemingen in Moeilijkheden.


> [!example]- Voorbeeld: Rotex Roeselare NV vs Verffabriek Veurne BV — triangulair lezen
> Rotex Roeselare NV vs Verffabriek Veurne BV — triangulair lezen.
>
> 1. **Vergelijkingstabel** 🧮
>
>    | Onderneming | Altman Z | Ohlson p | Bestuursverslag | Diagnose |
>    |---|---:|---:|---|---|
>    | Rotex Roeselare NV | 3,15 (safe) | 0,05 | Geen distress-signalen | Gezond |
>    | Verffabriek Veurne BV | 0,80 (distress) | 0,99 | Vereffening aangekondigd | Manifest falen (stadium 2-3) |
>    
>
> 2. **Aanbeveling** 💬
>
>    Voor Rotex: geen verdere actie — modellen + kwalitatief eensluidend gezond.
>    Voor Verffabriek Veurne BV: documenteren in commissaris-verslag + signaleren aan KOM indien commissaris-mandaat aanwezig.
>    
>

**Grondslag**: [[kwantitatieve-financiele-diagnose]] §in_praktijk, [[falen-van-de-onderneming]] §vroege-signalen

> [!warning]- Pas het origineel Altman-model niet blind toe op Belgische KMO's — gebruik Z' (niet-beursgenoteerd) of Z'' (niet-productie) of vermeld de toepassingsbeperking.
>
> _Vaak fout gedaan_: Origineel Altman (1968, US productie-beursgenoteerd) gebruiken voor een Belgische dienstverlener-BV zonder kanttekening.
>
> _Grondslag_: [[altman-z-score]] §valkuilen

> [!warning]- Behandel Ohlson p > 0,5 als 'lijkt op gefailleerde bedrijven uit de steekproef' — niet als deterministische voorspelling.
>
> _Vaak fout gedaan_: 'p = 0,8 = onderneming gaat zeker failliet' — verkeerde interpretatie van probabilistische output.
>
> _Grondslag_: [[ohlson-o-score]] §valkuilen

> [!warning]- Combineer altijd met kwalitatieve analyse (bestuursverslag, marktcontext).
>
> _Vaak fout gedaan_: Enkel op modellen vertrouwen — modellen vangen niet alles op (eenmalige events, management-wijzigingen, sector-disrupties).
>
> _Grondslag_: [[kwantitatieve-financiele-diagnose]] §in_praktijk


## Voorbeelden

> [!example]- Een dienstverlenende KMO (consulting) heeft Altman Z = 2,5 (grey zone, origineel model)
> **Conclusie**: Sofie Janssens legt uit dat het origineel Altman-model geijkt is op productie-bedrijven. Voor consulting/diensten is het Z''-model passender (cut-offs 1,10 en 2,60). De Z van 2,5 in Z''-context ligt binnen de grey zone — niet alarmerend op zich, maar wel signaal voor diepere analyse. Aanbeveling: Ohlson berekenen + kwalitatieve check + 3-jaar evolutie.
>
> **Grondslag**: [[altman-z-score]] §valkuilen, [[kwantitatieve-financiele-diagnose]] §in_praktijk
>
> **Redenering**: De grey zone is per definitie 'onzeker' — de modellen kunnen geen diagnose stellen, alleen aangeven dat de student moet diepgaan. Bekwaamheid-niveau toetst dit redeneerwerk.


## Gebaseerd op concepten

[[altman-z-score]] · [[ohlson-o-score]] · [[kwantitatieve-financiele-diagnose]] · [[falen-van-de-onderneming]]
## Voortkomend uit

- **Taken**: 1.9.taak.1
- **Kenniselementen**: 1.9.VI, 1.9.VI.A, 1.9.VI.B
