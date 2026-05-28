---
title: "Toegevoegde waarde"
concept_type: "ratio"
schema_version: "2.2"
status: "concept"
categorieen:
  - kader
ankers:
  - 1.3.I.B
  - 1.3.II.B
tags:
  - concept
  - schema-2.2
  - type-ratio
  - cat-kader
  - status-concept
gegenereerd_uit: "data/concepten/records/toegevoegde-waarde.json"
---

# Toegevoegde waarde

_Ratio_

🏛️ Kader · Anchors: `1.3.I.B` · `1.3.II.B` · Wave: `cluster-extract-financiele-analyse-2026-05-28`

> [!info] 📝 **Concept** — content gevuld door cluster-extract; niet door mens-verify gegaan.

**Afk.**: TW — **Synoniemen**: TW · value added · valeur ajoutée — **Vertalingen**: en: value added · fr: valeur ajoutée

## Definitie

🔗 De toegevoegde waarde (TW) is het verschil tussen de waarde van wat een onderneming produceert (output) en de waarde van wat ze daarvoor extern aankoopt (input). Concreet in BE-GAAP-cascade: TW = bedrijfsopbrengsten (rubriek 70-74) − handelsgoederen, grond- en hulpstoffen (rubriek 60) − diensten en diverse goederen (rubriek 61). Het is de waarde die door de eigen activiteit van de onderneming wordt 'toegevoegd' aan de aangekochte input — vóór ze verdeeld wordt over de productiefactoren arbeid (personeelskosten), kapitaal (financiële kosten + dividend), overheid (belastingen) en zelf-financiering (reserves + afschrijvingen).

<small>📚 KB W.Venn. — minimum algemeen rekeningenstelsel — klasse 60-61 (handelsgoederen + diensten en diverse goederen) — _wettekst_ · Richtlijn 2013/34/EU — bijlage V (winst-en-verliesrekening naar aard) — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Substantie

🔗 TW is dé centrale economische indicator van een onderneming — méér nog dan omzet. Omzet zegt 'hoeveel verkocht'; TW zegt 'hoeveel waarde gecreëerd'. Een handelsonderneming met 10 mio EUR omzet die zes-zevende doorboekt aan handelsgoederen genereert misschien 1,5 mio TW; een advieskantoor met 2 mio omzet en weinig aankopen genereert misschien 1,8 mio TW. De optelsom van de TW van alle ondernemingen in een economie = bruto binnenlands product (BBP) — dezelfde logica. Op micro-niveau wordt TW dé maatstaf van productiviteit (TW/personeelskost, TW/VTE), van marge-structuur (TW/omzet) en van waardestroom naar stakeholders.

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Rationale

🔗 Waarom een aparte indicator naast omzet en winst? Omzet zegt niets over het deel dat in het bedrijf 'blijft hangen' — twee bedrijven met dezelfde omzet kunnen totaal verschillende toegevoegde waarde hebben. Winst zegt niets over de ruimte voor loonbeleid of investeringspolitiek (winst = wat overschiet na alle stakeholders). TW staat tussen omzet en winst in: het is de waarde voor het bedrijf vooraleer ze verdeeld is. Daarom is TW het natuurlijke vertrekpunt voor (a) productiviteits-analyse, (b) loonruimte-onderhandelingen (vakbonden eisen 'aandeel in TW'), (c) sectorvergelijking (TW per VTE neutraliseert grootte-effecten), (d) waardestroom-analyse naar stakeholders.

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Gebruikscontext


**✅ Voor**
- 🔗 Productiviteits-analyse — TW per VTE benchmarken tegen sector om personeelsefficiëntie te beoordelen.
- 🔗 Stakeholder-verdeling — bepalen welk deel van de TW naar personeel, fiscus, kapitaal en zelf-financiering gaat.
- 🔗 Macro-economische rapportering (NBB Balanscentrale) — TW per sector als input voor BBP-statistieken.

## Bouwstenen

### 🧮 Formule toegevoegde waarde  
_`formule`_

🔗 TW = (70 Omzet + 71 Wijziging voorraden gereed product/bestellingen + 72 Geactiveerde productie + 74 Andere bedrijfsopbrengsten) − (60 Handelsgoederen, grond- en hulpstoffen + 61 Diensten en diverse goederen). Subsidies (740) worden meegenomen in bedrijfsopbrengsten. Voorraadwijzigingen op handelsgoederen (609) zitten in rubriek 60.

<small>📚 KB W.Venn. — MAR — klasse 60-74 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### ⚙️ Verdeling TW over productiefactoren  
_`mechanisme`_

🔗 TW wordt verdeeld over vier stakeholders: (1) arbeid → personeelskosten (rubriek 62); (2) kapitaal → financiële kosten (rubriek 65) + dividenden uit winstverdeling; (3) overheid → belastingen (rubriek 67); (4) zelf-financiering → afschrijvingen (rubriek 63) + voorzieningen + niet-uitgekeerde winst (reserves). Som van die vier verdeelposten ≈ TW. Het is een didactisch krachtig schema: 'aan wie ging de waarde die dit bedrijf creëerde?'

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### 🧮 TW per voltijds equivalent (TW/VTE)  
_`formule`_

🔗 TW/VTE = toegevoegde waarde / gemiddeld aantal voltijdse equivalenten. Productiviteits-indicator die schaalverschillen tussen ondernemingen neutraliseert. Benchmark: NBB-sectoraggregaten + Belfius-sectoranalyses. Industrieel KMO: typisch 60.000-100.000 EUR/VTE; dienstverlening hoog-waarde (consultancy, IT): 100.000-200.000 EUR/VTE; arbeidsintensieve sectoren (horeca, schoonmaak): 30.000-50.000 EUR/VTE.

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### 🧮 TW-marge (TW/omzet)  
_`formule`_

🔗 TW-marge = TW / omzet × 100 %. Structurele maatstaf van hoeveel waarde de onderneming zelf toevoegt aan haar omzet. Lage TW-marge (< 20 %): doorverkoop-bedrijf (handelaars, distributeurs); middelhoge marge (20-40 %): industriële productie; hoge marge (> 40 %): dienstverlening, hoog-waarde-industrie.

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

**Rationale**: 🔗 TW-marge zegt iets over de positie in de waardeketen: lage marge betekent dat de onderneming vooral 'doorgeefluik' is en haar marge maakt op volume; hoge marge betekent dat ze veel waarde toevoegt en haar marge maakt op kennis, merken of unieke processen. Strategische gevolgen voor pricing, schaalstrategie en arbeidsintensiteit.

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Voorbeelden

### 💡 Berekening TW + verdeling — Zelena Bio NV 🔗

_Zelena Bio NV, productie en verkoop bio-voedingsmiddelen, 35 VTE. Resultatenrekening 20X4 (in 1.000 EUR)._

**Berekening:**
- Bedrijfsopbrengsten: 70 Omzet 5.700 + 71 Voorraadwijziging +200 + 74 Andere bedrijfsopbrengsten 100 = 6.000
- Bedrijfskosten input: 60 Handelsgoederen + grond/hulpstoffen 2.500 + 61 Diensten en diverse goederen 1.100 = 3.600
- TW = 6.000 − 3.600 = 2.400

→ **Resultaat**: TW = 2.400.000 EUR. TW/omzet = 2.400/5.700 = 42 % → middel-hoge marge, consistent met productie + eigen merk. TW/VTE = 2.400/35 = 68.570 EUR — net onder sectorgemiddelde voedingsindustrie.

| Stakeholder | Bedrag | % van TW |
| --- | --- | --- |
| Personeel (62) | 1.560 | 65 % |
| Zelf-financiering (63 afschrijvingen + ingehouden winst) | 528 | 22 % |
| Overheid (67 belastingen) | 192 | 8 % |
| Kapitaal (65 + dividend) | 120 | 5 % |
| TOTAAL | 2.400 | 100 % |

Lezing: Zelena Bio besteedt het leeuwendeel van haar TW (65 %) aan personeel — typisch voor een arbeidsintensieve KMO. Het zelf-financierings-aandeel van 22 % is gezond (genoeg voor herinvestering). Het kapitaal-aandeel van 5 % is laag (weinig schuld + matige dividenduitkering). Trend over 3 jaar: personeels-aandeel stijgt van 60 % → 63 % → 65 % → drukt op winstcapaciteit. Vraag voor het management: TW per VTE verhogen via productiviteits-investering, of personeelskosten beperken?

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Valkuilen

### ⚠️ TW verwarren met omzet of brutomarge

**Verkeerde assumptie**: Studenten gebruiken TW en brutomarge door elkaar.

**Kernpunt**: Brutomarge = omzet − kostprijs verkochte goederen (alleen rubriek 60). TW gaat verder: TW = bedrijfsopbrengsten − rubriek 60 − rubriek 61 (diensten en diverse goederen). De diensten-en-diverse-goederen (huur, energie, verzekeringen, advies, IT, ...) zijn dus al afgetrokken. TW < brutomarge per definitie.

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### ⚠️ TW verwarren met BTW (belasting toegevoegde waarde)

**Verkeerde assumptie**: Bij zoekqueries leveren BTW-bronnen voor 'toegevoegde waarde' — studenten denken aan BTW als ze TW zien.

**Kernpunt**: Belasting op de Toegevoegde Waarde (btw) is een verbruiksbelasting; toegevoegde waarde (TW) als economische indicator in financiële analyse is iets totaal anders. De btw-aangifte zit niet in de TW-berekening (btw is een doorstroompost). Verwarring is alleen lexicaal — de concepten staan in heel verschillende werkvelden.

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### ⚠️ Subsidies vergeten in TW-berekening

**Verkeerde assumptie**: Subsidies (740) buiten beschouwing laten.

**Kernpunt**: Subsidies die het exploitatie-resultaat ondersteunen (740 Andere bedrijfsopbrengsten — bedrijfssubsidies en compenserende bedragen) maken deel uit van de bedrijfsopbrengsten en horen dus in de TW. Vergeten leidt tot onderschatting. Wel: kapitaalsubsidies (15) niet — die zitten op de passiva-zijde en worden via 753 (in resultaat genomen kapitaalsubsidies) in de financiële opbrengsten geboekt, buiten de TW-cascade.

<small>📚 KB W.Venn. — MAR — rubriek 740 / 753 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Verder lezen (scope-out)

- → Jaarrekening-analyse Σ → [[jaarrekeninganalyse]] _(moet-verwijzen)_
- ↪ Rentabiliteits-ratios (winstgevendheid) → [[rentabiliteits-ratios]] _(mag-verwijzen)_

## Relaties

### `valt_onder`
- [[jaarrekeninganalyse]] — Centrale indicator in de cascade-resultatenrekening.
### `vereist`
- [[jaarrekening]] — TW wordt afgeleid uit rubrieken 60-74 van de resultatenrekening.
### `vergelijkbaar_met`
- [[rentabiliteits-ratios]]
    - **Gelijkenissen**:
        - Beide meten winstgevendheid-aspecten via de resultatenrekening
    - **Verschillen**:
        - TW = bruto-indicator vóór verdeling stakeholders; rentabiliteits-ratios = na verdeling, in verhouding tot ingezet kapitaal of eigen vermogen
    - ⚠️ **Verwarringsrisico**: TW-marge ≠ EBIT-marge ≠ netto-marge — vier verschillende lagen in de cascade.
