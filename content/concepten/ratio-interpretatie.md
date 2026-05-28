---
title: "Ratio-interpretatie"
concept_type: "procedure"
schema_version: "2.2"
status: "concept"
categorieen:
  - kader
ankers:
  - 1.9.V.E
tags:
  - concept
  - schema-2.2
  - type-procedure
  - cat-kader
  - status-concept
gegenereerd_uit: "data/concepten/records/ratio-interpretatie.json"
---

# Ratio-interpretatie

_Procedure_

🏛️ Kader · Anchors: `1.9.V.E` · Wave: `cluster-extract-financiele-analyse-2026-05-28`

> [!info] 📝 **Concept** — content gevuld door cluster-extract; niet door mens-verify gegaan.

**Synoniemen**: ratio-analyse-methodologie · kruisverbanden ratio's — **Vertalingen**: en: ratio interpretation methodology · fr: interprétation des ratios

## Definitie

🔗 Ratio-interpretatie is de methodologische laag boven de losse ratio-categorieën — de discipline om uit een tabel ratio's een betekenisvol oordeel te halen. Vier interpretatie-assen werken samen: (1) trend-analyse over 3-5 jaar (welke kant gaan we op?), (2) sector-benchmark (hoe verhouden we ons tot vergelijkbare bedrijven?), (3) cross-categorie verbanden (DuPont-decomposition, cash-conversion-cycle), (4) kwalitatieve duiding (wat verklaart de cijfers? eenmalig of structureel?). Zonder deze methodologie blijven ratio's geïsoleerde getallen zonder betekenis.

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Substantie

🔗 Eén ratio op één moment is een snapshot zonder context — als naar één foto kijken van een wedstrijd zonder de eindstand te kennen. De vakkundige analist combineert daarom altijd minstens drie dimensies: (a) hoe is het geëvolueerd? (b) hoe doen de concurrenten het? (c) wat verklaart het via DuPont of cash-conversion-cycle? Een ROE van 12 % is bij voorbeeld 'matig' in software (sector-norm 20 %) maar 'uitstekend' in retail-food (sector-norm 8 %). De cijfers fluisteren — de analist moet het verhaal eruit halen.

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Gebruikscontext


**✅ Voor**
- 🔗 Bouwen van financieel diagnose-rapport — methodologische backbone van het hoofdstuk 'analyse en interpretatie'.
- 🔗 Kredietverlening + bancair onderhoud — banken vragen jaarlijks ratio-analyse met jaar-op-jaar evolutie en sector-vergelijking.

## Bouwstenen

### 👣 Tijd-as: trend over 3-5 jaar  
_`stap`_

🔗 Bouw een tijdreeks van 3-5 boekjaren voor elke ratio. Bereken jaar-op-jaar veranderingen en gemiddelde + standaarddeviatie. Patronen herkennen: (a) stabiel — predictiebaar, lage risico-premie; (b) trend op of neer — extrapoleer voor toekomst; (c) volatiel zonder trend — cyclisch of risicovol; (d) trend-omslag — recente structurele wijziging onderzoeken. Trend-analyse is bijna altijd informatiever dan absolute-niveau-analyse.

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### 👣 Sector-as: benchmark tegen peers  
_`stap`_

🔗 Identificeer 3-10 sector-vergelijkbare bedrijven (zelfde NACE-code, vergelijkbare omzet-grootte). Bronnen: (1) NBB-balanscentrale — sectoraggregaten gratis online; (2) Belfius Companyweb — betaalde benchmark-rapporten; (3) Trends Top — top-200 per sector; (4) Graydon — kredietrapporten; (5) jaarlijkse sector-rapporten van federaties (Agoria, Comeos, ...). Positioneer per ratio: top kwartiel — boven gemiddelde — onder gemiddelde — bottom kwartiel.

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### 👣 Cross-as: verbanden tussen ratio's  
_`stap`_

🔗 Ratio's hangen samen — DuPont-decomposition + cash-conversion-cycle leggen de mechanismen bloot. (1) DuPont 3-factor: ROE = nettomarge × omloopsnelheid activa × hefboom — verklaart waarom een ROE laag of hoog is. (2) Cash-conversion-cycle: CCC = DIO + DSO − DPO — verbindt activiteits- met liquiditeits-ratios. (3) Werkkapitaalbehoefte vs netto-bedrijfskapitaal — toetst structurele financiering. (4) EBITDA / interestlasten — interest coverage, brug rentabiliteit ↔ solvabiliteit. Cross-verbanden tonen waar pijnpunten clusteren.

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### 🧮 DuPont-decomposition  
_`formule`_

🔗 ROE = (nettowinst / omzet) × (omzet / totaal activa) × (totaal activa / eigen vermogen) = nettomarge × kapitaalomloop × financiële hefboom. Diagnose-tool: stel je ROE-A 18 % en ROE-B 12 %. DuPont laat zien of A's voordeel komt uit (1) margekracht (premium-positionering), (2) kapitaalefficiëntie (light asset model), of (3) hefboomgebruik (meer schuld — meer risico). Strategische implicaties verschillen totaal.

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### ⚙️ Cash-conversion-cycle als brug  
_`mechanisme`_

🔗 CCC = DIO + DSO − DPO (in dagen) verbindt activiteits-ratio's met liquiditeit. Een stijgende CCC → meer werkkapitaal-behoefte → minder cash voor andere doeleinden → druk op liquiditeit. Daling van current ratio gecombineerd met stijging van CCC = klassiek alarm-patroon. Omgekeerd: bedrijven met negatieve CCC (supermarkten) gebruiken hun werkkapitaal als financieringsbron en kunnen lage current ratio combineren met sterke liquiditeit.

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### 🧭 Sector-benchmark-bronnen  
_`vuistregel`_

🔗 Belgische bronnen: (1) NBB-balanscentrale — gratis sectorrapporten op nbb.be → aggregaten op NACE-niveau; (2) Belfius Companyweb / Trends Top — abonnement, individuele en peer-vergelijking; (3) Graydon — kredietrapporten met peer-positionering; (4) federatie-rapporten (Agoria voor industrie, Comeos voor handel, BCC voor bouw). Internationaal: Bloomberg, S&P Capital IQ. Voor KMO-analyse: combineer NBB-aggregaten (sector) met Companyweb-individuele rapporten (peer-vergelijking).

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Voorbeelden

### 💡 DuPont-vergelijking — twee retailers met identieke ROE 🔗

_Twee retailers, beide ROE 18 %, totaal andere strategie._

**Weergave** `vergelijkingstabel`:

```json
{
  "kolommen": [
    "Maatstaf",
    "Retailer A (premium)",
    "Retailer B (discount)"
  ],
  "rijen": [
    [
      "Nettomarge",
      "12 %",
      "3 %"
    ],
    [
      "Omloopsnelheid activa",
      "1,5×",
      "4,0×"
    ],
    [
      "Financiële hefboom",
      "1,0×",
      "1,5×"
    ],
    [
      "ROE = product",
      "18 %",
      "18 %"
    ]
  ],
  "interpretatie": "Identieke ROE, totaal andere businessmodel: A verdient via marge (luxe, kleine volumes, weinig schuld); B verdient via omloop (kleine marge, hoge volumes, beetje hefboom). Strategische implicaties: A kwetsbaar voor consumenten-trend-shift; B kwetsbaar voor prijsdruk en logistieke kostenstijging. Zonder DuPont zou je twee identieke bedrijven zien — met DuPont zie je twee totaal verschillende risicoprofielen."
}
```

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Valkuilen

### ⚠️ Ratio's zonder context citeren

**Verkeerde assumptie**: Current ratio 1,2 betekent automatisch 'matig liquide'.

**Kernpunt**: Eén ratio op één moment in één bedrijf zegt niets zonder (1) historische trend, (2) sector-benchmark, (3) cross-verbanden. Een current ratio van 1,2 kan uitstekend zijn voor een supermarkt en alarmerend voor een bouwbedrijf.

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### ⚠️ Window-dressing niet opmerken

**Verkeerde assumptie**: Balansdatum-ratio's reflecteren de normale situatie.

**Kernpunt**: Bedrijven manipuleren balanspresentatie rond jaareinde: schulden tijdelijk aflossen (en januari heropnemen), factoring (vorderingen verdwijnen), late afschrijvings-aanpassingen. Vergelijk met tussentijdse staten waar beschikbaar, of bekijk mediaan over jaar uit Companyweb/Belfius.

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### ⚠️ Niet-recurrente items als duurzaam interpreteren

**Verkeerde assumptie**: Winststijging dit jaar zet zich door.

**Kernpunt**: Eenmalige effecten (verkoop activa, fiscale tax credits, vrijgevallen voorzieningen, sale-lease-back winsten) bekijken in detail. Zuiverder vergelijking: bedrijfsresultaat (rubriek 9901) i.p.v. nettowinst (9904). Lees rubrieken 76/66 in de toelichting voor uitzonderlijk resultaat.

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### ⚠️ Seizoenseffecten als trend lezen

**Verkeerde assumptie**: Voorraad steeg 30 % t.o.v. vorig jaar — slecht teken.

**Kernpunt**: Seizoens-gevoelige sectoren (kerstartikelen, ijsproducenten, tuincenters) hebben sterk variabele balans-snapshots. Vergelijk altijd dezelfde balansdatum jaar-op-jaar; gebruik gemiddelde balans-stand (begin + einde) / 2 voor ratio's met balans-component en stroom-component.

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### ⚠️ Kwantitatief overschatten, kwalitatief onderschatten

**Verkeerde assumptie**: Alle ratio's groen = bedrijf gezond.

**Kernpunt**: Ratio's zijn lagging indicators uit het verleden — ze missen toekomstige bedreigingen (technologische verstoring, klantverlies, key-person dependency, regulatoire wijzigingen). Combineer altijd met kwalitatieve signalen: leiderschapswissel, klantconcentratie, sector-trends, jaarverslag-toelichting over risico's.

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Verder lezen (scope-out)

- → Specifieke ratio-categorieën → [[liquiditeits-ratios]] _(moet-verwijzen)_
- → Financiële diagnose (geheel-oordeel inclusief kwalitatief) → [[financiele-diagnose]] _(moet-verwijzen)_

## Relaties

### `valt_onder`
- [[jaarrekeninganalyse]]
### `vereist`
- [[liquiditeits-ratios]]
- [[solvabiliteits-ratios]]
- [[rentabiliteits-ratios]]
- [[activiteits-ratios]]
### `triggert`
- [[financiele-diagnose]] — Goede ratio-interpretatie voedt de integrale financiële diagnose.
