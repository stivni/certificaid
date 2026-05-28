---
title: "Bedrijfswaardering"
concept_type: "procedure"
schema_version: "2.2"
status: "concept"
categorieen:
  - kader
ankers:
  - 4.0.taak.6
  - 3.0.taak.2
tags:
  - concept
  - schema-2.2
  - type-procedure
  - cat-kader
  - status-concept
gegenereerd_uit: "data/concepten/records/bedrijfswaardering.json"
---

# Bedrijfswaardering

_Procedure_

🏛️ Kader · Anchors: `4.0.taak.6` · `3.0.taak.2` · Wave: `cluster-extract-bedrijfsadvies-2026-05-28`

> [!info] 📝 **Concept** — content gevuld door cluster-extract; niet door mens-verify gegaan.

**Synoniemen**: business valuation · ondernemingswaardering · vennootschapswaardering — **Vertalingen**: en: business valuation · fr: évaluation d'entreprise

## Definitie

🔗 Bedrijfswaardering is de discipline om een onderbouwde geldwaarde toe te kennen aan een onderneming — typisch ter ondersteuning van een transactie (overname, verkoop, kapitaalverhoging met externe partner), een familiale opvolging, een geschil of een fiscale waardering. Drie hoofdfamilies van methoden bestaan: (1) inkomsten-gebaseerd — Discounted Cash Flow (DCF) — toekomstige vrije kasstromen verdisconteerd; (2) markt-gebaseerd — multiples zoals P/E (price/earnings), EV/EBITDA, EV/sales — afgeleid uit vergelijkbare transacties of beursgenoteerde peers; (3) activa-gebaseerd — Net Asset Value (NAV) — gecorrigeerde substantiewaarde van het balansvermogen. In de Belgische KMO-praktijk wordt vaak een gewogen gemiddelde gebruikt van DCF + multiples + NAV.

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Substantie

🔗 Waardering is een schatting, niet een precieze meting. De vraag is niet 'wat is dit bedrijf objectief waard?' maar 'wat is een onderbouwde range waarbinnen koper en verkoper hun gesprek kunnen voeren?'. DCF kijkt vooruit (verwachte kasstromen) en is theoretisch de zuiverste methode — maar gevoelig voor input-assumpties. Multiples zijn markt-praktisch (wat betalen kopers echt voor vergelijkbare bedrijven?) maar minder precies voor unieke ondernemingen. NAV is een 'minimum-vloer' (substantiewaarde) — relevant voor activa-rijke vennootschappen (vastgoed, beleggingen). Goede waarderingen combineren methoden en stellen de range bij elkaar.

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Rationale

🔗 Waarom meerdere methoden? Omdat elk perspectief verschillende informatie vangt: DCF beloont toekomstige cash-genererings-capaciteit; multiples weerspiegelen markt-sentiment en sector-prijzen; NAV beschermt tegen liquidatie-scenarios. Bij familiale opvolging is een 'eerlijke' prijs bovendien fiscaal cruciaal — onder- of overprijzing kan kwalificatie als verdoken schenking, abnormaal-goedgunstig-voordeel of fiscale herziening uitlokken. De accountant in dit veld combineert technische methode met institutionele kennis (fiscaal, juridisch) — niet enkel cijferwerk.

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Gebruikscontext


**✅ Voor**
- 🔗 Verkoop/overname onderneming — koper en verkoper hebben elk een eigen waardering nodig als basis voor onderhandeling. Vaak prijs-range i.p.v. één punt-getal.
- 🔗 Familiale opvolging — overdracht via schenking of verkoop aan kinderen. Te lage prijs = fiscale herziening risico (verdoken schenking, art. 7 W.Succ.); te hoge prijs = liquiditeits-probleem bij koper.
- 🔗 Kapitaalverhoging met externe investeerder (private equity, business angel) — investeerder eist DCF + multiples ter onderbouwing.
- 🔗 Geschillen — vennootschapsgeschillen (uittreding aandeelhouder, art. 2:67 WVV), echtscheiding met onderneming, erfenis-discussies.

## Bouwstenen

### 🧮 DCF-methode (Discounted Cash Flow)  
_`formule`_

🔗 Enterprise Value (EV) = Σ FCFFt / (1 + WACC)^t (t=1 tot n) + eindwaarde / (1 + WACC)^n. Eindwaarde (terminal value) = FCFFn+1 / (WACC − g) met g = duurzame groei-voet (typisch 1-3 % BE-KMO). Equity-waarde = EV − netto schuld + niet-operationele activa. WACC reflecteert risico-gewogen kapitaalkost (zie investeringsevaluatie#wacc-formule).

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### 🧭 Multiples-methode (P/E · EV/EBITDA)  
_`vuistregel`_

🔗 Waarde = referentie-multiple × eigen winst/EBITDA. Twee bronnen voor de multiples: (1) Trading multiples — beursgenoteerde peer-groep (Bloomberg, Capital IQ); pas afslag toe voor illiquiditeit (typisch 20-30 % voor KMO). (2) Transaction multiples — historische M&A-transacties in dezelfde sector (Mergermarket, S&P, ITAA-rapporten). Typische Belgische KMO-ranges: EV/EBITDA 4-7× voor industriële KMO, 6-10× voor distributie, 8-15× voor software/IT, 5-9× voor diensten. Toepassen op genormaliseerde EBITDA (zonder uitzonderlijke items, eigenaars-overcompensatie gecorrigeerd).

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### 🧮 Net Asset Value (NAV)  
_`formule`_

🔗 NAV = boekwaarde eigen vermogen ± herwaarderings-correcties activa en passiva. Correcties: vastgoed naar marktwaarde, deelnemingen naar reële waarde, latente meerwaarden, niet-geboekte verplichtingen (pensioen, milieu), uitgestelde belastingen op de correcties. NAV is geschikt als 'vloer' bij activa-rijke vennootschappen (vastgoed-vennootschappen, holdings); minder relevant bij service-bedrijven of merknaam-gedreven ondernemingen waar de waarde vooral in immateriële niet-geboekte activa zit.

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### 🧭 Gemengde methode — gewogen gemiddelde  
_`vuistregel`_

🔗 Pragmatische Belgische KMO-aanpak: weeg DCF + multiples + NAV (bv. 40/40/20 voor mature KMO; 60/30/10 voor groei-bedrijf; 20/30/50 voor activa-zware holding). Geeft een verdedigbare range. ITAA-rapporten en notariële schattings-verslagen volgen vaak deze multi-methode-logica. Voor familiale-opvolgings-context: documenteer methodiek + assumpties grondig — fiscus toetst.

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Voorbeelden

### 💡 Bedrijfswaardering — Zelena Bio NV (overdracht aan zoon) 🔗

_Zelena Bio NV: omzet 5.700, EBITDA 770, FCFF jaar 1 = 350, verwachte groei 2 % p.j., eigen vermogen 2.000, marktwaarde vastgoed 500 boven boekwaarde (1.000 EUR). WACC 10 %._

**Berekening:**
- DCF — eindwaarde = 350 × 1,02 / (0,10 − 0,02) = 4.463
- 5-jarige expliciete kasstromen verdisconteerd ≈ 1.380 (vereenvoudigd)
- EV (DCF) ≈ 1.380 + 4.463 / 1,61 = 1.380 + 2.772 = 4.150
- Equity-waarde (DCF) = EV − netto schuld 0 = 4.150 (vereenvoudigd)
- Multiples — EV/EBITDA 5× × 770 = 3.850; equity ≈ 3.850
- NAV — eigen vermogen 2.000 + meerwaarde vastgoed 500 × (1 − 25 %) = 2.375
- Gemengd (50/30/20): 4.150 × 0,5 + 3.850 × 0,3 + 2.375 × 0,2 = 2.075 + 1.155 + 475 = 3.705

→ **Resultaat**: Geschatte waarderings-range: 3.700-4.200 KEUR (gewogen 3.705). DCF dominant want het bedrijf is groei-gericht; multiples bevestigen marktconforme prijs; NAV is veel lager (geen significante immateriële balans-waarde). Voor overdracht aan zoon: schenking-met-voorbehoud-vruchtgebruik op equity-waarde van ~3.700 KEUR met onderbouwing in waarderings-verslag aan fiscus.

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Valkuilen

### ⚠️ Eén methode als 'de' waarde presenteren

**Verkeerde assumptie**: DCF geeft 4,2 mio → dit is de waarde.

**Kernpunt**: Waarde is een range, geen punt-getal. Goede waarderingen tonen 3 methoden en spannen een range op (bv. 3,5-4,5 mio). Eén-methode-rapporten zijn academisch zwak en juridisch kwetsbaar — fiscus en tegenpartij kunnen ze betwisten met een eigen methode-keuze.

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### ⚠️ EBITDA niet normaliseren

**Verkeerde assumptie**: Pas multiple toe op laatste-jaar EBITDA.

**Kernpunt**: Genormaliseerde EBITDA = werkelijke EBITDA − uitzonderlijke items + correcties. Typische correcties voor KMO: marktconform loon voor eigenaar (vaak ondercompensatie of overcompensatie), één-malige verkoop activa, COVID-overheidssteun, familie-leden op payroll zonder reële bijdrage. Niet-normaliseren = systematische over- of onderwaardering.

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### ⚠️ Te lage WACC = waarderings-inflatie

**Verkeerde assumptie**: Gebruik OLO-rente + 3 % premie als WACC voor KMO.

**Kernpunt**: Belgische KMO-WACC is typisch 9-15 %, niet 5-7 %. Te lage WACC kan DCF-waarde met factor 2-3 opblazen. Werk met CAPM voor Ke (β van sector-peers × marktrisicopremie 5-7 %) + illiquiditeitspremie voor KMO (2-5 %) + size premium (2-3 %). Documenteer keuze in verslag.

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### ⚠️ Eindwaarde-overgewicht in DCF

**Verkeerde assumptie**: Lange horizon (10 jaar) lost het eindwaarde-probleem op.

**Kernpunt**: Bij DCF over 5 jaar maakt de eindwaarde typisch 70-80 % van EV uit. Zelfs over 10 jaar nog 60-70 %. Dit verhoogt gevoeligheid voor terminal growth rate g. Vuistregel: g ≤ 2-3 % (lange-termijn inflatie + reëel BBP-groei) — hogere g = onhoudbaar. Sensitiviteit op g: zichtbaar maken in verslag.

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### ⚠️ Fiscale impact negeren

**Verkeerde assumptie**: Waarde is bedrijfseconomisch onafhankelijk van transactie-vorm.

**Kernpunt**: Share-deal vs asset-deal heeft drastisch andere fiscale gevolgen voor koper én verkoper. Share-deal: meerwaarde aandelen vrijgesteld (DBI-meerwaarde voor vennootschap-verkoper); asset-deal: stopzettingsmeerwaarde belast bij verkoper, registratie + btw bij koper. Waarderings-conclusie moet de structuur-keuze meenemen.

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Verder lezen (scope-out)

- → Free cash flow (DCF-input) → [[free-cash-flow]] _(moet-verwijzen)_
- → Overdracht-onderneming (toepassings-context) → [[overdracht-onderneming]] _(moet-verwijzen)_
- → Investeringsevaluatie (verwante DCF-techniek) → [[investeringsevaluatie]] _(moet-verwijzen)_
- ↪ Bedrijfsstrategie-inzicht (context) → [[bedrijfsstrategie-inzicht]] _(mag-verwijzen)_

## Relaties

### `vereist`
- [[free-cash-flow]]
- [[jaarrekening]]
### `vergelijkbaar_met`
- [[investeringsevaluatie]]
    - **Gelijkenissen**:
        - Beide gebruiken DCF + WACC
    - **Verschillen**:
        - Bedrijfswaardering = hele onderneming; investeringsevaluatie = één project binnen onderneming
    - ⚠️ **Verwarringsrisico**: DCF-mechanica is identiek; toepassings-context anders.
### `triggert`
- [[overdracht-onderneming]] — Waardering is input voor overdracht-prijsbepaling.
### `beinvloed_door`
- [[bedrijfsstrategie-inzicht]] — Strategische context (markt-positie, concurrentie, businessmodel) voedt de DCF-kasstroom-projecties.
