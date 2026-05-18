---
title: Opstellen van een drie-segmenten-kasstroomoverzicht (CFO, CFI, CFF)
tags:
- concept
- competentie
- po-1-9
linked_anchors:
- 1.9.taak.1
- 1.9.IV
- 1.9.IV.B
- 1.9.IV.C
- 1.9.IV.G
- 1.9.IV.H
programmaonderdelen:
- '1.9'
confidence: inferred
node_type: competentie
status: voorgesteld
schema_version: '1.6'
gegenereerd_uit: data/concepten/records/opstellen-driesegmenten-kasstroomoverzicht.json
gegenereerd_op: '2026-05-18'
---
# Opstellen van een drie-segmenten-kasstroomoverzicht (CFO, CFI, CFF) 🤖

Operationele competentie: vanuit de balans, resultatenrekening en toelichtingsstaten (tabel van waardemutaties, mutatietabel eigen vermogen) een kasstroomoverzicht reconstrueren met de drie segmenten CFO, CFI, CFF. Sluitend met de mutatie van liquide middelen in de balans. Verplicht voor de stagiair bij verkort/microschema-jaarrekeningen waar de bedrijfscijfers het kasstroomoverzicht niet rechtstreeks meegeven.


## Stappen

### 1. Berekenen van de operationele kasstroom (CFO)

Bereken CFO via de indirecte methode — vertrek vanuit resultaat na belasting, corrigeer niet-kaskosten en wijziging in behoefte aan bedrijfskapitaal.

**Waarom?** CFO toont of de eigen activiteit voldoende kas genereert. Een negatieve of marginale CFO is het belangrijkste alarmsignaal voor continuïteit, ongeacht winst.

**📥 Input**:
- Resultatenrekening + balans (twee opeenvolgende boekjaren) → **Resultaat na belasting, afschrijvingen, waardeverminderingen, voorzieningen-mutatie, Δ voorraden + vorderingen + handelsschulden** _(boekhoudkundig-bedrag)_

**📤 Output**:
- CFO → **Eén bedrag + opbouw via indirecte methode** _(nieuwe-balanspost)_

**🛠️ Hoe**:

1. Start met resultaat na belasting (uit RR).
2. Tel niet-kaskosten op volgens [[cashflow-analyse]] §resultaat-plus-niet-kaskosten: afschrijvingen + waardeverminderingen + netto-dotatie voorzieningen.
3. Tussenresultaat = "cashflow" in enge zin (winst + niet-kaskosten).
4. Trek de wijziging in behoefte aan bedrijfskapitaal af (zie [[behoefte-aan-bedrijfskapitaal]] §formule): Δ voorraden + Δ handelsvorderingen − Δ handelsschulden.
5. Resultaat = CFO. Negatief CFO bij positieve winst = klassiek alarmsignaal (winst zit vast in werkkapitaal).


> [!example]- Voorbeeld: Rotex Roeselare NV — CFO boekjaar 20X3 via indirecte methode
> Rotex Roeselare NV — CFO boekjaar 20X3 via indirecte methode.
>
> 1. **Niet-kaskosten optellen** 🧮
>
>    Resultaat na belasting: + € 3.900.000
>    Afschrijvingen: + € 1.500.000
>    Waardeverminderingen: + € 100.000
>    Netto-dotatie voorzieningen: + € 300.000
>    Tussenresultaat (cashflow eng): + € 5.800.000
>    
>
> 2. **Δ BBK aftrekken** 🧮
>
>    Δ voorraden (20X3 − 20X2): + € 500.000
>    Δ handelsvorderingen: + € 800.000
>    Δ handelsschulden: + € 300.000
>    Δ BBK = € 500.000 + € 800.000 − € 300.000 = + € 1.000.000 (BBK groeide)
>    CFO = € 5.800.000 − € 1.000.000 = **+ € 4.800.000**
>    
>

**Grondslag**: [[kasstroomoverzicht-drie-segmenten]] §operationeel-cfo, [[cashflow-analyse]] §resultaat-plus-niet-kaskosten, [[behoefte-aan-bedrijfskapitaal]] §formule

### 2. Berekenen van de investeringskasstroom (CFI)

Bereken CFI via de tabel van waardemutaties — aanschaffingen vaste activa (kasuitstroom) min desinvesteringen (kasinstroom).

**Waarom?** CFI toont of de onderneming groeit (negatief CFI = uitbouw), stagneert (CFI ≈ 0) of leeft van afbouw (positief CFI = verkoop activa).

**📥 Input**:
- Tabel waardemutaties vaste activa (toelichting jaarrekening) → **Aanschaffingen + desinvesteringen per rubriek 20-28** _(boekhoudkundig-bedrag)_

**📤 Output**:
- CFI → **Eén bedrag + uitsplitsing per categorie vaste activa** _(nieuwe-balanspost)_

**🛠️ Hoe**:

1. Open de toelichting bij de jaarrekening, sectie "Tabel van waardemutaties van de vaste activa". Volg [[tabel-waardemutaties]] §vier-bewegingen.
2. Tel aanschaffingen op alle rubrieken vaste activa (immateriële, materiële, financiële). Dit is kasuitstroom (− teken).
3. Tel desinvesteringen op (verkoopsom, niet boekwaarde). Dit is kasinstroom (+ teken).
4. CFI = desinvesteringen − aanschaffingen. Bijna altijd negatief bij gezonde onderneming.
5. Let op financiële vaste activa: aankoop deelnemingen telt als CFI-uitstroom, niet als CFF.


> [!example]- Voorbeeld: Rotex Roeselare NV — CFI boekjaar 20X3
> Rotex Roeselare NV — CFI boekjaar 20X3.
>
> 1. **Bewegingen uit tabel waardemutaties** 🧮
>
>    | Categorie | Aanschaffingen | Desinvesteringen |
>    |---|---:|---:|
>    | Immateriële vaste activa | € 200.000 | € 0 |
>    | Materiële vaste activa | € 1.800.000 | € 100.000 |
>    | Financiële vaste activa | € 0 | € 50.000 |
>    | **Totaal** | **€ 2.000.000** | **€ 150.000** |
>    
>
> 2. **CFI berekening** 🧮
>
>    CFI = € 150.000 − € 2.000.000 = **− € 1.850.000**
>    Interpretatie: Rotex investeert netto € 1,85M — duidelijk groeitraject, geen afbouw.
>    
>

**Grondslag**: [[kasstroomoverzicht-drie-segmenten]] §investerings-cfi, [[tabel-waardemutaties]] §brug-naar-kasstroom

### 3. Berekenen van de financieringskasstroom (CFF)

Bereken CFF als netto-mutatie eigen vermogen + netto-mutatie vreemd vermogen − dividenden.

**Waarom?** CFF toont hoe het tekort tussen CFO en CFI overbrugd wordt. Een onderneming die structureel CFF > 0 nodig heeft om CFO + CFI dicht te houden, leeft op extern kapitaal.

**📥 Input**:
- Balans (twee boekjaren) + resultaatverwerking → **Δ kapitaal + reserves, Δ schulden > 1 jaar, Δ kortlopende financiële schulden, uitgekeerde dividenden** _(boekhoudkundig-bedrag)_

**📤 Output**:
- CFF → **Eén bedrag + uitsplitsing EV / VV / dividenden** _(nieuwe-balanspost)_

**🛠️ Hoe**:

1. Mutatie eigen vermogen (uit [[financiering-met-eigen-vermogen]] §inbreng-vs-zelffinanciering): kapitaalverhogingen + uitgiftepremies (cash-instroom).
2. Mutatie vreemd vermogen (uit [[financiering-met-derdenkapitaal]] §looptijd-kostprijs): nieuwe leningen − terugbetalingen.
3. Uitgekeerde dividenden (uit resultaatverwerking) — cash-uitstroom.
4. CFF = mutaties EV + mutaties VV − dividenden.
5. Combineer met CFO + CFI om Δ kas te verklaren (controle: CFO + CFI + CFF = Δ kasrubriek 50-58 op balans).


> [!example]- Voorbeeld: Rotex Roeselare NV — CFF boekjaar 20X3
> Rotex Roeselare NV — CFF boekjaar 20X3.
>
> 1. **Mutaties EV en VV** 🧮
>
>    Kapitaalverhogingen: + € 0 (geen)
>    Δ schulden > 1 jaar (rubriek 17): + € 500.000 (nieuwe banklening)
>    Δ schulden ≤ 1 jaar financieel (rubriek 43): − € 200.000 (aflossing)
>    Uitgekeerde dividenden: − € 600.000
>    
>
> 2. **CFF berekening** 🧮
>
>    CFF = € 0 + € 500.000 − € 200.000 − € 600.000 = **− € 300.000**
>    
>
> 3. **Δ kas controle** 🧮
>
>    Δ kas = CFO + CFI + CFF = € 4.800.000 + (− € 1.850.000) + (− € 300.000) = **+ € 2.650.000**
>    Controle: kas balans 20X3 − kas balans 20X2 = € 2.650.000 → klopt.
>    
>

**Grondslag**: [[kasstroomoverzicht-drie-segmenten]] §financierings-cff, [[financiering-met-eigen-vermogen]], [[financiering-met-derdenkapitaal]]

### 4. Diagnose stellen op basis van het CFO/CFI/CFF-patroon

Lees het teken-patroon van de drie segmenten samen — verschillende combinaties wijzen op verschillende fasen van het bedrijfsleven (groei, volwassen, distress, herstructurering).

**Waarom?** De drie segmenten samen vertellen een verhaal dat één CFO-cijfer of één winst-cijfer niet kan tonen. Op bekwaamheid-niveau wordt verwacht dat de student het patroon interpreteert.

**📥 Input**:
- CFO + CFI + CFF (stappen 1-3) → **Drie bedragen met tekens** _(boekhoudkundig-bedrag)_

**📤 Output**:
- Diagnose-conclusie → **Fase-classificatie + risico-signaal** _(conclusie)_

**🛠️ Hoe**:

1. Schrijf de drie tekens uit: (CFO, CFI, CFF) bv. (+, −, −).
2. Match het patroon met de typische cases uit [[kasstroomoverzicht-drie-segmenten]] §in_praktijk:
   - (+, −, −) = volwassen onderneming, financiert investeringen + dividenden uit operationele kas. Gezond.
   - (+, −, +) = groeiende onderneming, operations dragen deels, externe financiering brengt rest. Acceptabel als CFO+CFF dekken CFI.
   - (−, −, +) = onderneming overleeft op extern kapitaal. Alarmsignaal.
   - (+, +, −) = afbouw, verkoopt activa en betaalt schulden af. Vereffening-traject of strategische desinvestering.
3. Combineer met evolutie over 3 boekjaren — een eenmalig patroon kan strategisch zijn, een herhaling is structureel.


> [!example]- Voorbeeld: Rotex Roeselare NV — diagnose 20X3
> Rotex Roeselare NV — diagnose 20X3.
>
> 1. **Patroon-analyse** 💬
>
>    (CFO, CFI, CFF) = (+ € 4,8M, − € 1,85M, − € 0,3M) = (+, −, −)
>    Patroon: volwassen onderneming die uit eigen kas investeert en schulden afbouwt.
>    Gezond profiel. Vrije kasstroom (CFO − CFI) = + € 2,95M = ruimte voor extra dividend of schuldreductie.
>    
>

**Grondslag**: [[kasstroomoverzicht-drie-segmenten]] §in_praktijk

> [!warning]- Lees de drie segmenten als één verhaal — vermijd cherry-picking van de meest gunstige cijfer.
>
> _Vaak fout gedaan_: Conclusie 'gezond' trekken op basis van + € 4,8M CFO zonder rekening te houden dat investeringen + dividenden dit grotendeels opslokken.
>
> _Grondslag_: [[kasstroomoverzicht-drie-segmenten]] §in_praktijk

> [!warning]- Wijs altijd op het verschil tussen "cashflow" (één bedrag uit RR) en "kasstroomoverzicht" (drie segmenten, ook Δ BBK).
>
> _Vaak fout gedaan_: Cashflow uit stap 1 tussenresultaat (€ 5,8M) verwarren met CFO (€ 4,8M) — Δ BBK vergeten.
>
> _Grondslag_: [[kasstroomoverzicht-drie-segmenten]] §valkuilen


## Voorbeelden




## Bronnen

[^1]: `aggregate`
