---
title: "Faillissementspredictie-modellen"
concept_type: "kader"
schema_version: "2.2"
status: "concept"
categorieen:
  - kader
ankers:
  - 1.9.VI.B
tags:
  - concept
  - schema-2.2
  - type-kader
  - cat-kader
  - status-concept
gegenereerd_uit: "data/concepten/records/faillissementspredictie-modellen.json"
---

_Kader_ · ook: Z-score-modellen · bankruptcy prediction models · discontinuïteits-modellen

## Definitie

Faillissementspredictie-modellen zijn statistisch ontwikkelde formules die op basis van enkele ratio's een score berekenen die de kans op discontinuïteit binnen 1-2 jaar inschat. Het bekendste is Altman's Z-score (1968) — een lineaire combinatie van vijf ratio's met expliciete cut-off-zones (veilig, grijs, distressed). Voor de Belgische context bouwden Ooghe en Camerlynck (UGent) modellen op de NBB-balanscentrale-database — die nauwkeuriger zijn voor BE-KMO's. De modellen worden gebruikt als kwantitatieve check binnen een breder oordeel — nooit als enige basis.

<small>🔗 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Substantie

Z-scores en hun verwanten zijn snelle 'red flag'-tools die in 5 minuten een eerste indicatie geven of een bedrijf signalen van discontinuïteit toont. Banken gebruiken ze massaal in geautomatiseerde kredietbeoordeling; auditors gebruiken ze als risico-screening; financieel-analysten als triage in een grote dataset. De modellen vangen patronen die menselijke intuïtie soms mist: combinatie van zwakke liquiditeit + lage rentabiliteit + hoge schuldgraad. Maar ze zijn lagging — gebaseerd op historische jaarcijfers, geen voorspellers van plotse schokken (sluiting belangrijke klant, bestuurs-fraude). Vandaar: nooit als enig criterium; altijd combineren met kwalitatieve signalen.

<small>🔗 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Rationale

Waarom een eigen kader naast continuïteits-toets en financiële diagnose? Omdat de Z-score (en varianten) een specifieke methodologische bijdrage leveren: statistisch onderbouwde, gewogen combinatie van ratio's met empirische cut-off-niveaus. Een individuele ratio (current ratio 0,8, ROE -5 %) zegt 'mogelijk problemen'; een Z-score zegt 'in 80 % van vergelijkbare bedrijven met deze profielcombinatie volgde faillissement binnen 2 jaar'. Dat is een ander informatie-niveau — empirisch geijkt, niet vuistregel-gebaseerd. ISA 570 en CBN-advies 2010/14 stellen kwantitatieve predictie-modellen expliciet voor als één van de going-concern-indicatoren.

<small>📖 ISA 570 (herzien) — Going Concern — paragraaf A3 (financiële indicatoren) — _norm_</small>

## Gebruikscontext


**✅ Voor**
- 📖 Going-concern-toets in controleopdracht — Z-score als kwantitatieve screening (ISA 570 + CBN-advies 2010/14).
- 🔗 Bank-kredietbeoordeling — Belgische grootbanken bouwen Z-achtige scores in hun rating-modellen.
- 🔗 Kamers voor ondernemingen in moeilijkheden — bij signalering door RSZ/btw bouwt de Kamer een eerste-orde-beeld met financiële indicatoren.

## Bouwstenen

### 🧮 Altman Z-score (1968)

Origineel voor beursgenoteerde productie-ondernemingen (1968): Z = 1,2 × X₁ + 1,4 × X₂ + 3,3 × X₃ + 0,6 × X₄ + 1,0 × X₅. Waarbij X₁ = werkkapitaal / totaal activa (liquiditeit); X₂ = ingehouden winst / totaal activa (cumulatieve rentabiliteit); X₃ = EBIT / totaal activa (operationele rentabiliteit); X₄ = marktwaarde eigen vermogen / boekwaarde totaal schulden (solvabiliteit); X₅ = omzet / totaal activa (kapitaalefficiëntie). Interpretatie: Z > 2,99 = veilig; 1,81 < Z < 2,99 = grijze zone; Z < 1,81 = distressed (hoge faillissements-kans binnen 2 jaar).

<small>🔗 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### 🧮 Altman Z' en Z'' (niet-beursgenoteerd)

Z' (1983) voor niet-beursgenoteerde productie-ondernemingen — vervangt marktwaarde EV door boekwaarde EV: Z' = 0,717·X₁ + 0,847·X₂ + 3,107·X₃ + 0,420·X₄ + 0,998·X₅. Cut-offs: > 2,9 veilig; 1,23-2,9 grijs; < 1,23 distressed. Z'' (1995) voor niet-productie + emerging markets — laat X₅ weg: Z'' = 6,56·X₁ + 3,26·X₂ + 6,72·X₃ + 1,05·X₄. Cut-offs: > 2,6 veilig; 1,1-2,6 grijs; < 1,1 distressed. Meest gebruikt voor Belgische KMO en niet-industriële ondernemingen.

<small>🔗 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### 🧮 Ooghe-Camerlynck-model (Belgisch)

Ontwikkeld door Ooghe & Camerlynck (UGent) op basis van NBB-balanscentrale Belgische bedrijven. Logit-model met ratio's specifiek geijkt voor Belgische context: omzet/totaal activa, schuldgraad, brutomarge, achterstanden RSZ/btw als kwalitatieve indicator. Output: probabiliteit faillissement binnen 1 of 3 jaar. Vaak ingebed in commerciële tools (Belfius Companyweb, Graydon). Voordeel boven Altman: BE-specifieke ijking — minder vals-positief bij sectoren afwijkend van Amerikaanse productie-bedrijven.

<small>🔗 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### 🚧 Beperkingen + gebruiks-discipline

(1) Lagging — gebaseerd op jaarrekening 6-12 maanden oud; missen recente plotse schokken. (2) Sector-bias — productie-bedrijven anders dan diensten of vastgoed; algemene modellen falen daar systematisch. (3) Earnings management — bedrijven met faillissementsrisico manipuleren vaak balans (factoring, voorzieningen) → modellen onderschatten risico. (4) Vals-positieven — gezonde maar atypische bedrijven (start-ups, kapitaalintensieve sector) krijgen distressed score zonder werkelijk risico. Daarom: Z-score is EEN signaal, niet HET signaal. Combineer met kwalitatieve indicatoren + sector-context.

<small>🔗 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Voorbeelden

> [!example]- Altman Z''-score — Zelena Bio NV (20X4)
> _Zelena Bio NV (niet-beursgenoteerd, niet-pure-productie): werkkapitaal 1.600, totaal activa 5.000, ingehouden winsten 800, EBIT 450, boekwaarde EV 2.000, totaal schulden 3.000 (1.000 EUR)._
>
> **Berekening:**
>
> - X₁ = werkkapitaal / totaal activa = 1.600 / 5.000 = 0,32
> - X₂ = ingehouden winst / totaal activa = 800 / 5.000 = 0,16
> - X₃ = EBIT / totaal activa = 450 / 5.000 = 0,09
> - X₄ = boekwaarde EV / totaal schulden = 2.000 / 3.000 = 0,67
> - Z'' = 6,56 × 0,32 + 3,26 × 0,16 + 6,72 × 0,09 + 1,05 × 0,67 = 2,10 + 0,52 + 0,60 + 0,70 = 3,92
>
> → **Resultaat**: Z'' = 3,92 → boven 2,6-grens → veilige zone. Geen indicatie van faillissementsrisico volgens dit kwantitatieve kader. Combinatie van solide werkkapitaal-positie (X₁ = 0,32) en redelijke kapitaalopbouw (X₂ + X₄) compenseert de gematigde rentabiliteit (X₃ = 0,09). Conclusie: voorlopig geen Z-getriggerd going-concern-alarm — vol kwantitatieve diagnose nog uitvoeren met kwalitatieve indicatoren (klantverlies, sector-trends).
>
> <small>🔗 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Valkuilen

> [!warning]- Z-score als enig criterium gebruiken
> **Verkeerde assumptie**: Z-score zegt 'veilig' → het bedrijf is veilig.
>
> **Kernpunt**: Z-modellen vangen historische patronen van financiële discontinuïteit, maar missen kwalitatieve signalen (key-person-vertrek, klantverlies, sector-disruptie). Een 'veilige' Z-score betekent enkel afwezigheid van klassiek financieel-distress-patroon — niet absentie van risico.
>
> <small>🔗 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

> [!warning]- Foute Z-variant gebruiken
> **Verkeerde assumptie**: Pas Altman Z (origineel 1968) toe op Belgische KMO.
>
> **Kernpunt**: Origineel Altman Z is geijkt op Amerikaanse beursgenoteerde productie-bedrijven. Voor BE-KMO: gebruik Z'' (geen marktwaarde EV nodig) of liefst Belgisch geijkt model (Ooghe-Camerlynck). Foute variant geeft systematische vertekening.
>
> <small>🔗 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

> [!warning]- Distressed-score 'zelfvervullende profetie' negeren
> **Verkeerde assumptie**: Distressed Z-score → faillissement is onvermijdelijk.
>
> **Kernpunt**: Z-score is descriptief, niet deterministisch. Een distressed score = waarschuwingssignaal voor diepere diagnose + actie (herstructurering, kapitaalverhoging, kostbesparing, gerechtelijke reorganisatie). Veel distressed-score-bedrijven recupereren bij tijdige interventie.
>
> <small>🔗 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

> [!warning]- Sector-mismatch negeren
> **Verkeerde assumptie**: Z-model is sector-neutraal.
>
> **Kernpunt**: Vastgoed-vennootschappen (hoog balansvolume, lage omzetomloop) krijgen kunstmatig lage X₅ → systematische distressed score zonder werkelijk risico. Start-ups (negatieve cumulatieve winst) idem voor X₂. Banken passen sector-correcties toe; manuele toepassing moet expliciet kalibreren.
>
> <small>🔗 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Verder lezen (scope-out)

- → Continuiteit (CBN-advies 2010-14 + audit-NBE) → [[continuiteit]] _(moet-verwijzen)_
- → Financiële diagnose (geheel-oordeel) → [[financiele-diagnose]] _(moet-verwijzen)_

## Relaties

### `valt_onder`
- [[jaarrekeninganalyse]]
### `vereist`
- [[jaarrekening]]
### `triggert`
- [[continuiteit]] — Distressed Z-score is een ISA 570-trigger voor verdere going-concern-evaluatie.
### `beinvloed_door`
- [[financiele-diagnose]] — Z-score is één component binnen de bredere financiële diagnose.
