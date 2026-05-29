---
title: "Aftrekbare bestedingen (PB)"
concept_type: "regime"
schema_version: "2.2"
status: "concept"
categorieen:
  - regeling
ankers:
  - 2.2.XI
tags:
  - concept
  - schema-2.2
  - type-regime
  - cat-regeling
  - status-concept
gegenereerd_uit: "data/concepten/records/aftrekbare-bestedingen-pb.json"
---

_Regime_ · ook: aftrek van het totale netto-inkomen · art. 104 WIB-aftrek

> [!warning] **Uitdovend regime** — wordt afgebouwd; check sinds-/tot-data.

## Definitie

Aftrekbare bestedingen (PB) zijn welbepaalde uitgaven die de belastingplichtige in het belastbaar tijdperk daadwerkelijk heeft betaald en die volgens art. 104 WIB92 mogen worden afgetrokken van zijn TOTAAL NETTO-INKOMEN — vóór de tariefberekening van art. 130. Dat onderscheidt ze van belastingverminderingen, die pas later in de cascade op de berekende belasting in mindering komen. De wet zelf bevat slechts één hoofdcategorie: onderhoudsuitkeringen (en gelijkgestelde kapitalen) betaald aan EER/Zwitserse-inwoners die niet tot het gezin behoren, aftrekbaar tot 70% (AJ 2025) — met geleidelijke afbouw naar 60% (vanaf 1/1/2026) en 50% (vanaf 1/1/2027).

<small>📖 WIB92 — art. 104 — _wettekst_</small>

## Substantie

Economisch effect: aftrek van het netto-inkomen vermindert de belastbare grondslag. De effectieve belastingbesparing is dus AFTREK × MARGINAAL TARIEF van de belastingplichtige (typisch 40-50% in de top-schijven van de PB). Dit is een belangrijk verschil met belastingverminderingen die werken aan vast tarief (bv. 30-45% afhankelijk van de regeling) of via belastingvrije som (25-50% volgens schijven van art. 134). De aftrek van 70% van een betaalde onderhoudsuitkering levert dus iemand met marginaal tarief 50% een netto-belastingbesparing op van 0,70 × 0,50 = 35% van het uitgekeerde bedrag. Symmetrisch zijde: bij de ontvanger is dat zelfde percentage van het bruto-bedrag belastbaar (art. 99 — referentie naar art. 90, 3°/4°).

<small>📖 WIB92 — art. 104 — _wettekst_ · WIB92 — art. 99 — _wettekst_</small>

## Rationale

Ratio legis: de aftrek voor onderhoudsuitkeringen erkent de feitelijke draagkracht-vermindering door de wettelijke onderhoudsplicht naar derden (kinderen, ex-partner, ouders) die niet meer tot het fiscaal gezin behoren. De 70%-coefficient (geen 100%) reflecteert een gemiddelde verhouding tussen het 'echt-noodzakelijke' onderhoud en de werkelijk-betaalde uitkering, en dient als forfaitaire correctie. De wetgever heeft echter beslist om dat percentage geleidelijk af te bouwen (70 → 60 → 50%) tussen 2025 en 2027, vermoedelijk als budgettaire maatregel én om consistent te zijn met de afbouw van fiscale gunstregimes. Symmetrie met art. 99 (zelfde percentage belastbaar bij ontvanger) verzekert dat de overheid niet 'tweemaal' belast.

<small>🔗 WIB92 — art. 104 — _wettekst_ · WIB92 — art. 99 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Gebruikscontext

**Status**: `uitdovend` · sinds **AJ 2026** · basis: WIB92 art. 104 — gewijzigd; afbouw 70% → 60% (1/1/2026) → 50% (1/1/2027)

Het regime zelf (aftrek onderhoudsuitkeringen) blijft bestaan, maar het aftrekbaar percentage daalt geleidelijk. Studenten moeten letten op het toepasselijke AJ: AJ 2025 → 70%; AJ 2026 → 60%; AJ 2027 → 50%. Mogelijk verdere wetgeving.

**✅ Voor**
- 📖 Belastingplichtigen die regelmatig onderhoudsuitkeringen betalen aan een inwoner van de EER of Zwitserland die niet tot hun gezin behoort, ter uitvoering van een verplichting op grond van het Burgerlijk Wetboek of Gerechtelijk Wetboek (of gelijkaardige buitenlandse wet).

**📋 Voorwaarden**
- 📖 Cumulatief: (1) regelmatige betaling — niet eenmalig of vrijwillig; (2) werkelijke betaling in het belastbaar tijdperk; (3) ontvanger is inwoner van EER-lidstaat of Zwitserland; (4) ontvanger maakt geen deel uit van het gezin van de belastingplichtige op 1 januari AJ; (5) wettelijke grondslag in BW/Gerechtelijk Wetboek of gelijkaardige buitenlandse wet (vrijwillige uitkering buiten wettelijke onderhoudsplicht = niet aftrekbaar); (6) geen kind waarvoor in een vorig AJ art. 132bis (co-ouderschap-toeslag) werd toegepast (art. 104, 2° in fine — anti-cumulatie); (7) bewijsstukken bewaren (rekeninguittreksels, vonnis, alimentatie-overeenkomst).

**⛔ Uitsluitingen**
- 📖 Niet aftrekbaar: (a) onderhoudsuitkeringen aan personen die deel uitmaken van het eigen gezin (kinderen ten laste, ouders ten laste in gezin); (b) onderhoudsuitkeringen aan inwoners buiten EER+Zwitserland; (c) vrijwillige geldelijke steun zonder wettelijke onderhoudsplicht; (d) onderhoudsuitkeringen voor kinderen waarvoor art. 132bis (co-ouderschap-deling) in een vorig AJ werd toegepast.

**👍 Voordeel**
- 🔗 Verlaging belastbare grondslag → besparing aan marginaal tarief van de belastingplichtige (typisch 40-50% voor hogere inkomens). Voor iemand in 50%-schijf: aftrek van 12.000 EUR onderhoudsuitkering × 70% × 50% = netto belastingbesparing 4.200 EUR.

**⚠️ Risico**
- 📖 Anti-cumulatie met art. 132bis: belastingplichtige die in vorig AJ co-ouderschap-deling claimde voor een kind, kan voor datzelfde kind geen onderhoudsuitkering aftrekken in een later AJ. Risico van retro-actief verwerping. · Vergeten dat de regelmatigheids-voorwaarde wordt geschonden bij gemiste/laat betaalde alimentatie. · Vergeten dat aftrek alleen geldt voor EER+CH-inwoners (uitkering aan kind dat in VS studeert valt erbuiten).

## Bouwstenen

### 💡 Onderhoudsuitkering — afbakening

Onderhoudsuitkering = periodieke betaling ter uitvoering van een wettelijke onderhoudsplicht (BW/Gerechtelijk Wetboek of gelijkaardige buitenlandse wetgeving) aan een persoon buiten het gezin. Typische gevallen: alimentatie aan ex-echtgenoot na scheiding; alimentatie voor kinderen die niet meer ten laste zijn (bv. studerend kind dat zelfstandig woont >21 jaar); levensonderhoud aan ouders/grootouders. Kapitalen die zulke uitkeringen vervangen, worden gelijkgesteld (art. 104, 1° in fine + art. 169).

<small>📖 WIB92 — art. 104 — _wettekst_</small>

### 📏 Aftrekbaar percentage (afbouwregime)

Aftrekbaar percentage van de betaalde onderhoudsuitkering (en symmetrisch belastbaar bij de ontvanger via art. 99):
• AJ 2025 en eerder: 70%
• Vanaf 1/1/2026 (AJ 2027): 60%
• Vanaf 1/1/2027 (AJ 2028): 50%

Noot: vóór recente hervorming was het 80% — die historische waarde komt voor in oude cursussen maar is niet meer actueel. Voor elk concreet examen: het percentage van het toepasselijke AJ gebruiken.

<small>📖 WIB92 — art. 104 — _wettekst_ · WIB92 — art. 99 — _wettekst_</small>

### 📜 'Regelmatige betaling'-voorwaarde

De wet vereist dat de uitkering REGELMATIG werd betaald. Strikte interpretatie: maandelijks/trimestrieel volgens vastgestelde frequentie in vonnis of overeenkomst. Onregelmatige of laat-betaalde uitkeringen verliezen in principe de aftrek — tenzij art. 104, 2°-mechanisme geldt: bedragen betaald na het belastbaar tijdperk waarop ze betrekking hebben, ter uitvoering van een gerechtelijke beslissing met terugwerkende kracht, blijven aftrekbaar (alsnog) aan zelfde percentage. Praktijk: ontvanger moet ook 'als-geheel' worden meegenomen in zijn aangifte voor het juiste belastbaar tijdperk.

<small>📖 WIB92 — art. 104 — _wettekst_</small>

### ⚙️ Uitsplitsing bij gemeenschappelijke aanslag (art. 127 + art. 105)

Bij gemeenschappelijke aanslag wordt de aftrek aangerekend op het netto-inkomen van DE ECHTGENOOT DIE DE BESTEDING HEEFT GEDAAN. Wanneer de uitkering verband houdt met inkomsten die volgens art. 127 deels aan elk van beide echtgenoten worden toegekend (50/50-regel voor 'andere inkomsten'), kan een evenredige verdeling van de aftrek nodig zijn. In de praktijk: alimentatie betaald door één echtgenoot uit zijn eigen beroepsinkomen → aftrek volledig bij hem.

<small>📖 WIB92 — art. 127 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### ↪️ Anti-cumulatie met co-ouderschap (art. 132bis)

Uitkeringen betaald voor kinderen waarvoor in een vorig AJ art. 132bis (co-ouderschap-toeslag-deling) werd toegepast, zijn NIET aftrekbaar (art. 104, 2° in fine). Keuze per kind, niet per gezin: voor één kind kan men kiezen voor 132bis-deling (en geen aftrek alimentatie); voor een ander kind voor aftrek (en geen 132bis-deling). Logica: voorkomt dubbel-voordeel — co-ouderschap-deling én aftrek van wat overgemaakt wordt.

<small>📖 WIB92 — art. 104 — _wettekst_ · WIB92 — art. 132bis — _wettekst_</small>

### ↪️ Aftrek bij niet-inwoners (art. 242)

Voor niet-inwoners van België (BNI/nat. personen) geldt de aftrek van art. 104 alleen als minstens 75% van hun beroepsinkomsten in België belastbaar is (art. 242 §1) — proportionaliteits-eis EU-recht. Alternatief (art. 242 §1/1): aftrek geldt ook in evenredigheid als de niet-inwoner via inkomensverklaring aantoont dat hij in zijn woonstaat de aftrek niet kan genieten (Schumacker-doctrine, EER-context). Strikte voorwaarden: woonstaat = EER-lidstaat; nettoinkomen omvat beroepsinkomsten; geen sluitend belang in andere EER-lidstaat.

<small>📖 WIB92 — art. 242 — _wettekst_</small>

## Voorbeelden

> [!example]- Aftrek 70%-alimentatie aan ex-echtgenoot — AJ 2025
> _Belastingplichtige A betaalt in 2024 (= inkomstenjaar AJ 2025) maandelijks 1.000 EUR alimentatie aan zijn ex-echtgenote B, ter uitvoering van een vonnis. B woont in België. Marginaal tarief A = 50%. Geen co-ouderschap-deling in vorig AJ._
>
> **Berekening:**
>
> - Stap 1 — totaal betaald in 2024: 12 × 1.000 = 12.000 EUR.
> - Stap 2 — aftrekbaar (AJ 2025): 70% × 12.000 = 8.400 EUR (art. 104, 1°).
> - Stap 3 — aftrek van totaal netto-inkomen van A: belastbare grondslag van A daalt met 8.400 EUR.
> - Stap 4 — netto belastingbesparing voor A: 8.400 × 50% (marginaal tarief) = 4.200 EUR.
> - Stap 5 — gemeentebelasting (typisch 7%): besparing × 1,07 = 4.494 EUR bruto-effect.
> - Stap 6 — bij ontvanger B (art. 99): 70% × 12.000 = 8.400 EUR belastbaar als divers inkomen (art. 90, 3°). B betaalt PB op die 8.400 EUR aan haar marginale tarief — typisch lager dan A's tarief, wat het symmetrisch netto-fiscaal-voordeel voor het gezin verklaart.
> - Stap 7 — bewijsstukken: vonnis + 12 rekeninguittreksels.
>
> → **Resultaat**: Voor 12.000 EUR overgedragen alimentatie: A bespaart 4.494 EUR; B betaalt PB op 8.400 EUR. Voor een gezin met fiscaal-tarief-asymmetrie (A in 50%-schijf, B in 25%-schijf) is dit netto-positief voor het gezin.
>
> <small>🔗 WIB92 — art. 104 — _wettekst_ · WIB92 — art. 99 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

> [!example]- Zelfde casus AJ 2028 (vanaf 1/1/2027) — afbouw naar 50%
> _Identiek aan vorige casus, maar voor inkomstenjaar 2027 (AJ 2028). Aftrekpercentage onder de nieuwe wet: 50%._
>
> **Berekening:**
>
> - Stap 1 — totaal betaald in 2027: 12.000 EUR (zelfde alimentatie).
> - Stap 2 — aftrekbaar (AJ 2028): 50% × 12.000 = 6.000 EUR.
> - Stap 3 — netto belastingbesparing A: 6.000 × 50% = 3.000 EUR (vs 4.200 in AJ 2025 = verlies van 1.200 EUR).
> - Stap 4 — belastbaar bij B: 50% × 12.000 = 6.000 EUR (vs 8.400 EUR — vermindering van haar PB).
>
> → **Resultaat**: Vergeleken met AJ 2025: A verliest 1.200 EUR aftrek-voordeel; B's belastbare deel daalt symmetrisch met 2.400 EUR. Voor het gezin als geheel: netto-negatief effect, want A's voordeel daalt sneller dan B's last (asymmetrische tariefs-progressie). Dit illustreert waarom de afbouw 70 → 50% een budgettair instrument is.
>
> <small>📖 WIB92 — art. 104 — _wettekst_ · WIB92 — art. 99 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

> [!example]- Co-ouderschap → aftrek alimentatie keuze-cascade
> _Gescheiden ouders A en B met 2 kinderen, co-ouderschap met gelijke huisvesting. A betaalt 300 EUR/maand alimentatie aan B voor het oudste kind (16 jaar, studerend) — gehomologeerd in vonnis. Jongste kind (10 jaar): zuiver gelijke huisvesting, geen alimentatie._
>
> **Berekening:**
>
> - Stap 1 — voor het jongste kind (10 jaar): geen alimentatie betaald → automatisch art. 132bis (co-ouderschap-deling). Beide ouders krijgen halve toeslag belastingvrije som (1.120 EUR niet-geïndexeerd elk).
> - Stap 2 — voor het oudste kind (16 jaar): keuze tussen art. 132bis-deling OF aftrek alimentatie.
> - Stap 3a — Optie A: art. 132bis voor 16-jarige: helft toeslag = 1.120 EUR voor elke ouder. Belastingbesparing voor A ≈ 1.120 × 25% = 280 EUR. Geen aftrek alimentatie mogelijk.
> - Stap 3b — Optie B: aftrek alimentatie. 12 × 300 = 3.600 EUR betaald. Aftrekbaar 70% = 2.520 EUR. Bij marginaal tarief 50%: belastingbesparing A = 1.260 EUR. B's belastbare basis stijgt met 2.520 EUR (belastbaar aan haar tarief, typisch 40-45%): zij betaalt extra PB ≈ 1.008-1.134 EUR. Geen co-ouderschap-toeslag voor dit kind voor beide ouders.
> - Stap 4 — Netto-vergelijking voor A: Optie A = +280 EUR; Optie B = +1.260 EUR (eigen voordeel) − verlies van halve toeslag voor de andere ouder is buiten A's controle. Maar de aftrek doet B 1.000+ EUR EXTRA betalen.
> - Stap 5 — Gezin-perspectief: Optie A (132bis) = +280 + +280 = 560 EUR voor het gezin. Optie B (aftrek) = +1.260 EUR (A) − 1.080 EUR (B, gemiddeld) − verlies 2 × 280 EUR co-ouder-toeslag = netto ca. -380 EUR voor het gezin.
> - Stap 6 — Conclusie: voor lage alimentaties is co-ouderschap voordeliger; aftrek wordt voordeliger naarmate alimentatie >5.000 EUR/jaar.
>
> → **Resultaat**: Anti-cumulatie dwingt tot een rationele keuze per kind. Hier optimaal: 132bis voor beide kinderen, geen aftrek. Voor een studerend kind 21+ met alimentatie van 10.000 EUR/jaar zou aftrek wellicht voordeliger zijn.
>
> <small>🔗 WIB92 — art. 104 — _wettekst_ · WIB92 — art. 132bis — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Valkuilen

> [!warning]- 80%-percentage uit oude cursussen klakkeloos gebruiken
> **Verkeerde assumptie**: Aftrek onderhoudsuitkering = 80% — een 'eeuwig getal' uit oudere fiscale handboeken.
>
> **Kernpunt**: De huidige percentages zijn 70% (AJ 2025), 60% (vanaf 1/1/2026) en 50% (vanaf 1/1/2027). 80% was de historische waarde maar is hervormd. Bij elk examen: het percentage van het toepasselijke aanslagjaar in WIB92 art. 104 raadplegen.
>
> <small>📖 WIB92 — art. 104 — _wettekst_</small>

> [!warning]- Aftrek verwarren met belastingvermindering
> **Verkeerde assumptie**: Aftrek en belastingvermindering hebben hetzelfde fiscaal effect.
>
> **Kernpunt**: Aftrek (art. 104) werkt op de belastbare grondslag → besparing = bedrag × marginaal tarief van de belastingplichtige (15-50%). Belastingvermindering werkt op de berekende belasting → besparing = bedrag × vastgesteld tarief (typisch 30 of 45%, of conform BVS-schijven). Voor hoge inkomens (50%-schijf) is aftrek dus meestal voordeliger; voor lage inkomens (≤30%) is een vermindering aan vast tarief 30% gunstiger.
>
> <small>🔗 WIB92 — art. 104 — _wettekst_ · WIB92 — art. 1451 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

> [!warning]- Onderhoudsuitkering aan persoon BUITEN EER aftrekken
> **Verkeerde assumptie**: Alimentatie aan bv. kind dat in Verenigde Staten studeert is aftrekbaar.
>
> **Kernpunt**: Art. 104, 1° beperkt expliciet tot 'inwoners van een lidstaat van de Europese Economische Ruimte of van Zwitserland'. Onderhoudsuitkering aan een persoon in VS, Canada, Marokko etc. is NIET aftrekbaar onder art. 104. Geen wettelijke uitzondering ondanks reële kost.
>
> <small>📖 WIB92 — art. 104 — _wettekst_</small>

> [!warning]- Vrijwillige geldelijke steun zonder wettelijke onderhoudsplicht aftrekken
> **Verkeerde assumptie**: Maandelijkse steun aan een hulpbehoevende vriend of niet-juridisch-erkende partner is aftrekbaar.
>
> **Kernpunt**: Art. 104, 1° vereist 'verplichting op grond van het Burgerlijk of Gerechtelijk Wetboek of van een gelijkaardige wettelijke verplichting in een buitenlandse wetgeving'. Vrijwillige uitkeringen, schenkingen of steun zonder vonnis/wettelijke onderhoudsplicht zijn niet aftrekbaar. De rechter heeft die kwalificatie reeds meermaals bevestigd.
>
> <small>📖 WIB92 — art. 104 — _wettekst_</small>

## Speelruimtes

### 🎚️ Aftrek alimentatie (art. 104) vs co-ouderschap-deling (art. 132bis)

## Accountant-perspectieven

### Particuliere cliënt (PB-aangifte met aftrekbare bestedingen)

_De accountant die de PB-aangifte van een cliënt met onderhoudsuitkeringen voorbereidt of nakijkt._

#### 💰 Fiscaal adviseur

##### 👣 Controle bewijsstukken onderhoudsuitkering

Bij aftrek van onderhoudsuitkeringen verzamelen: (1) vonnis of gehomologeerde overeenkomst (basis voor wettelijke onderhoudsplicht); (2) rekeninguittreksels die regelmatigheid van betaling bewijzen; (3) verklaring/bewijs van EER-residentie van ontvanger; (4) verklaring dat ontvanger geen deel uitmaakt van gezin op 1/1 AJ; (5) check anti-cumulatie art. 132bis: zijn voor dit kind in voorgaande AJ'en co-ouderschap-toeslagen geclaimd? Vakje in PB-aangifte: Vak VIII (federaal — aftrekbare bestedingen), code 1390/2390 (alimentatie aan binnen-België) of 1392/2392 (aan EER-buitenland).

<small>🔗 WIB92 — art. 104 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

##### 📜 Optimalisatie-afweging aftrek vs co-ouderschap

Bij gescheiden cliënt: per kind apart bekijken welk regime voordeliger is. Bereken (a) aftrek × marginaal tarief MINUS bijkomende belasting bij ontvanger versus (b) helft toeslag art. 132 × BVS-schijf-tarief. Houd rekening met de geleidelijke afbouw 70 → 60 → 50% — voor jonge kinderen met meerjarige alimentatie kan dit een verschuiving van advies impliceren over de tijd. Documenteer adviezen aan cliënt — keuze van AJ N bepaalt anti-cumulatie voor AJ N+1.

<small>🔗 WIB92 — art. 104 — _wettekst_ · WIB92 — art. 132bis — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Verder lezen (scope-out)

- → Onderhoudsuitkering symmetrisch — belastbaarheid bij ontvanger (art. 90, 3°-4° + art. 99) → [[onderhoudsuitkering]] _(moet-verwijzen)_
- → Gewest-belastingverminderingen (eigen woning, energiebesparing — latere stap in berekening) → [[gewestelijke-belastingverminderingen-pb]] _(moet-verwijzen)_
- → Federale belastingverminderingen (pensioensparen, dienstencheques) → [[federale-belastingverminderingen-pb]] _(moet-verwijzen)_
- → Belastingberekening-procedure (cascade: aftrekken → tarief → verminderingen → BVS) → [[belastingberekening-pb]] _(moet-verwijzen)_
- → Co-ouderschap-anti-cumulatie → [[kinderen-ten-laste]] _(moet-verwijzen)_

## Relaties

### `valt_onder`
- [[personenbelasting]]
### `bevat`
- [[onderhoudsuitkering]] — Hoofdcategorie van aftrekbare bestedingen onder art. 104 is de onderhoudsuitkering aan een persoon buiten het gezin.
### `triggert`
- [[belastingberekening-pb]] — Aftrek vermindert het totaal netto-inkomen vóór tariefberekening — eerste stap in de berekenings-cascade.
### `niet_combineerbaar_met`
- [[kinderen-ten-laste]] — Voor een kind waarvoor in een vorig AJ art. 132bis (co-ouderschap-deling) werd toegepast, is geen aftrek alimentatie meer mogelijk (art. 104, 2° in fine).
### `vergelijkbaar_met`
- [[federale-belastingverminderingen-pb]]
    - **Gelijkenissen**:
        - Beide verminderen netto de PB van de belastingplichtige
        - Beide vereisen specifieke bewijsstukken en aangifte-rubrieken
        - Beide kennen percentage- of plafond-beperkingen
    - **Verschillen**:
        - Aftrek (art. 104) grijpt op belastbare grondslag → effect = bedrag × marginaal tarief
        - Belastingvermindering grijpt op berekende belasting → effect = bedrag × vast tarief (30% of 45%)
        - Aftrek werkt voordeliger voor hoge inkomens (50%-schijf); vermindering voordeliger voor middeninkomens (≤30%-schijf)
    - ⚠️ **Verwarringsrisico**: Studenten verwisselen 'aftrek' en 'vermindering' systematisch — de eerste werkt vóór, de tweede ná de tariefberekening.
