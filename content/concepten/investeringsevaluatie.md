---
title: "Investeringsevaluatie"
concept_type: "procedure"
schema_version: "2.2"
status: "concept"
categorieen:
  - kader
ankers:
  - 4.0.taak.6
tags:
  - concept
  - schema-2.2
  - type-procedure
  - cat-kader
  - status-concept
gegenereerd_uit: "data/concepten/records/investeringsevaluatie.json"
---

# Investeringsevaluatie

_Procedure_

🏛️ Kader · Anchors: `4.0.taak.6` · Wave: `cluster-extract-financiele-analyse-2026-05-28`

> [!info] 📝 **Concept** — content gevuld door cluster-extract; niet door mens-verify gegaan.

**Synoniemen**: capital budgeting · investerings-beslissing · investeringsanalyse — **Vertalingen**: en: investment appraisal · fr: évaluation d'investissement

## Definitie

🔗 Investeringsevaluatie is de discipline om te beslissen of een capitaalinvestering (nieuwe machine, gebouw, IT-systeem, overname) economisch verantwoord is. Vier complementaire methoden: (1) Netto Contante Waarde (NCW of NPV) — som van toekomstige kasstromen verdisconteerd tegen kapitaalkost; (2) Interne Rentevoet (IRR) — disconteringsvoet die NPV op nul brengt; (3) terugverdientijd (payback) — hoeveel jaar tot de investering terugverdiend is; (4) winst-index (profitability index, PI) — verhouding NPV / initiële investering. Disconteringsvoet is typisch de WACC (gewogen kapitaalkost). Een investering is theoretisch aanvaardbaar bij NPV > 0, IRR > WACC, en past binnen de risico-bereidheid van het bedrijf.

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Substantie

🔗 Investeringsevaluatie verzoent twee tijdstippen: cash uit vandaag, kasstromen morgen. Het centrale inzicht: een euro nu is meer waard dan een euro over 5 jaar (tijdwaarde van geld). NPV maakt die vergelijking expliciet door alle toekomstige kasstromen terug te brengen naar 'vandaag-euros'. Voor de accountant die KMO's adviseert is investeringsevaluatie typisch nodig bij: machine-vervanging, capaciteits-uitbreiding, overname, make-or-buy-beslissing, IT-projecten met meerjarige horizon. Vuistregel: investering aanvaarden indien NPV > 0; bij keuze tussen alternatieven, neem hoogste NPV (NIET hoogste IRR — IRR vertekent bij verschillende project-omvang).

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Rationale

🔗 Waarom niet gewoon 'investering goedkeuren als ze winst oplevert'? Omdat winst niet rekening houdt met (a) timing — eerder cash = meer waard; (b) kapitaalkost — geld kost iets (rente schuld, vereist rendement aandeelhouder); (c) risico — onzekere kasstromen zijn minder waard dan zekere. NPV-methode integreert al die elementen via de disconteringsvoet. IRR is intuïtiever (geeft een rendement-percentage) maar heeft problemen met (i) project-schaal (kleine IRR-winnaar kan grote NPV-verliezer zijn) en (ii) onconventionele kasstromen (meerdere oplossingen mogelijk). Daarom: NPV als hoofdcriterium, IRR + payback als aanvullende perspectieven.

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Gebruikscontext


**✅ Voor**
- 🔗 Investerings-advies aan KMO-cliënt — nieuwe machine, capaciteits-uitbreiding, IT-investering met meerjarige horizon.
- 🔗 Make-or-buy-beslissingen — outsourcing van productie of administratie versus interne capaciteit. NPV-vergelijking over horizon van 5-10 jaar.
- 🔗 Subsidie-aanvraag — investeringssteun-dossiers (Vlaio, regionale agentschappen) vragen vaak een investerings-evaluatie met aangetoonde rentabiliteit.

**⚠️ Risico**
- 🔗 Over-optimistische kasstroom-projecties — typische bias bij projectinitiator. Bouw scenario-analyse (base / pessimistisch / optimistisch) en sensitiviteitstest van kritische parameters (omzet-groei, kostprijs-evolutie).

## Bouwstenen

### 🧮 Net Present Value-formule  
_`formule`_

🔗 NPV = −I₀ + Σ (CFt / (1 + r)^t) voor t = 1 tot n, waarbij I₀ = initiële investering, CFt = nettokasstroom in jaar t, r = disconteringsvoet (typisch WACC), n = looptijd. Beslisregel: NPV > 0 → aanvaard (waarde-creatie); NPV < 0 → verwerp (waarde-vernietiging); NPV = 0 → break-even tegen kapitaalkost.

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### 🧮 Internal Rate of Return  
_`formule`_

🔗 IRR is de disconteringsvoet r waarvoor NPV = 0. Iteratief op te lossen (Excel: =IRR(); financiële rekenmachine). Beslisregel: IRR > WACC → aanvaard (project rendeert meer dan kapitaalkost); IRR < WACC → verwerp. Beperking: IRR-vergelijking tussen projecten kan misleidend zijn — een klein project met IRR 25 % kan minder NPV opleveren dan groot project met IRR 15 %. Bij scale-verschillen: NPV is leidend.

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### 🧮 Payback-periode  
_`formule`_

🔗 Payback (terugverdientijd) = aantal jaren tot cumulatieve nettokasstroom = initiële investering. Eenvoudige vorm: I₀ / jaarlijkse kasstroom. Bij ongelijke kasstromen: cumulatief tellen tot terugverdiend. Gediscontineerde payback corrigeert voor tijdwaarde door verdisconteerde kasstromen te gebruiken. Vuistregel: < 3 jaar = aantrekkelijk; > 7 jaar = riskant voor KMO. Beperking: negeert kasstromen na payback-punt — dus geen volledig rentabiliteitsbeeld.

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### 🧮 WACC-formule  
_`formule`_

🔗 WACC = (E / V) × Ke + (D / V) × Kd × (1 − T) waarbij E = marktwaarde eigen vermogen, D = marktwaarde schuld, V = E + D, Ke = vereist rendement eigen vermogen (Capital Asset Pricing Model: Ke = Rf + β × marktrisicopremie), Kd = rente op schuld, T = belastingsvoet. T-factor reflecteert tax shield op rente. Typisch WACC voor Belgische KMO: 7-12 %. Vuistregel: hogere risico-perceptie → hogere β → hogere Ke → hogere WACC.

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### 🧮 Profitability Index (PI)  
_`formule`_

🔗 PI = (NPV + I₀) / I₀ = present value van toekomstige kasstromen / initiële investering. Beslisregel: PI > 1 → aanvaard; PI < 1 → verwerp. Voordeel boven NPV: schaal-onafhankelijk — geschikt voor rangordening van projecten bij kapitaalrantsoenering (vast budget, meerdere kandidaten).

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Voorbeelden

### 💡 Investerings-evaluatie nieuwe productielijn — Zelena Bio NV 🔗

_Zelena overweegt investering in nieuwe productielijn: initiële investering 1.000 KEUR, verwachte netto-jaarkasstroom 280 KEUR gedurende 5 jaar, geen restwaarde. WACC = 10 %._

**Berekening:**
- PV jaar 1: 280 / 1,10 = 254,5
- PV jaar 2: 280 / 1,21 = 231,4
- PV jaar 3: 280 / 1,331 = 210,4
- PV jaar 4: 280 / 1,464 = 191,3
- PV jaar 5: 280 / 1,611 = 173,9
- Σ PV = 1.061,5
- NPV = −1.000 + 1.061,5 = +61,5 KEUR
- IRR (op te lossen): r ≈ 12,4 % > WACC 10 % → aanvaard
- Payback (ongediscontineerd): 1.000 / 280 = 3,57 jaar
- Gediscontineerde payback: tussen jaar 4 en 5 (cum. PV jaar 4 = 887,6 < 1.000)
- PI = 1.061,5 / 1.000 = 1,06

→ **Resultaat**: NPV +61,5 KEUR → marginaal positief: investering creëert waarde tegen WACC 10 %. IRR 12,4 % bevestigt. Payback 3,6 jaar = aanvaardbaar. PI 1,06 = elke euro investering levert 6 cent NPV. Aanbeveling: aanvaarden, maar met sensitiviteit-test — een 10 %-daling kasstroom (260 i.p.v. 280) brengt NPV naar 0. Sensitive op omzet-volume. Stel scenario-analyse op.

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Valkuilen

### ⚠️ Gemiddelde i.p.v. marginale kasstromen

**Verkeerde assumptie**: Kasstroom-projectie = totale omzet × marge.

**Kernpunt**: Gebruik UITSLUITEND marginale kasstromen — wat verandert er bij wel/niet investeren? Sunk costs (al uitgegeven studie-kosten) NIET meenemen. Allocaties van bestaande overhead NIET meenemen tenzij deze werkelijk toenemen. Opportunity costs (gemiste alternatieve aanwending) WEL meenemen.

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### ⚠️ Te lage disconteringsvoet kiezen

**Verkeerde assumptie**: Gebruik de bankrente of een 'redelijke' 5 % als disconteringsvoet.

**Kernpunt**: De disconteringsvoet moet de WACC of project-specifieke risicogewogen vereist rendement zijn — typisch 7-15 % voor Belgische KMO afhankelijk van risico. Te lage voet maakt alle projecten kunstmatig 'rendabel' en leidt tot waarde-vernietigende investeringen.

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### ⚠️ Werkkapitaal-impact vergeten

**Verkeerde assumptie**: Investeringskasstroom = enkel CAPEX-uitgaaf + jaarlijkse winst.

**Kernpunt**: Een productie-uitbreiding vergroot ook werkkapitaal-behoefte: meer voorraad, meer klantenkrediet → Δ WKB. Deze cash-uitgave moet meegeteld worden in jaar van uitbreiding, en wordt teruggewonnen op project-einde (werkkapitaal vrijkomt). Vergeten = systematische NPV-overschatting.

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### ⚠️ Optimistische projecties zonder sensitiviteit

**Verkeerde assumptie**: Eén projectie volstaat, met de 'meest waarschijnlijke' cijfers.

**Kernpunt**: Bouw altijd 3 scenario's (pessimistisch / base / optimistisch) + sensitiviteit op kritische variabelen (omzet, kostprijs, levensduur). Een investering met positieve NPV alleen in optimistisch scenario is geen veilige investering. Risk-adjusted NPV = gewogen gemiddelde van scenario-NPV's.

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### ⚠️ IRR als rangschikkings-criterium gebruiken

**Verkeerde assumptie**: Hoogste IRR = beste project.

**Kernpunt**: IRR vertekent bij scale-verschillen — een klein project met IRR 30 % kan minder NPV genereren dan groot project met IRR 12 %. Bij wederzijds uitsluitende projecten: NPV is leidend. IRR is wel nuttig als snelle filter en als communicatie-tool naar niet-financiële stakeholders.

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Verder lezen (scope-out)

- → Marginale analyse (make-or-buy-input) → [[marginale-analyse]] _(moet-verwijzen)_
- → Kasstroomanalyse (kasstroom-input) → [[kasstroom-analyse]] _(moet-verwijzen)_
- ↪ Bedrijfswaardering (DCF-verwante techniek) → [[bedrijfswaardering]] _(mag-verwijzen)_

## Relaties

### `vereist`
- [[kasstroom-analyse]]
### `vergelijkbaar_met`
- [[bedrijfswaardering]]
    - **Gelijkenissen**:
        - Beide gebruiken DCF-techniek met disconteringsvoet
    - **Verschillen**:
        - Investeringsevaluatie = micro (één project); bedrijfswaardering = macro (hele onderneming)
    - ⚠️ **Verwarringsrisico**: Studenten gebruiken WACC inconsequent — bij projectinvestering soms een aangepaste project-specifieke risicovoet.
### `beinvloed_door`
- [[marginale-analyse]] — Make-or-buy-beslissingen vereisen marginale-kosten-analyse als input voor kasstroom-projectie.
