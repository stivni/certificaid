---
title: "Verleggingsregeling (reverse charge)"
concept_type: "regime"
schema_version: "2.2"
status: "concept"
categorieen:
  - regeling
ankers:
  - 2.4.VI
tags:
  - concept
  - schema-2.2
  - type-regime
  - cat-regeling
  - status-concept
gegenereerd_uit: "data/concepten/records/verleggingsregeling.json"
---

_Regime_ · ook: reverse charge · cocontractant-regeling · BTW-verlegging · verlegging van heffing

## Definitie

De verleggingsregeling is een afwijking van het normale BTW-systeem waarbij de schuldenaar van de belasting niet de leverancier of dienstverrichter is, maar zijn medecontractant (de afnemer). De leverancier reikt een factuur uit zonder BTW met de vermelding 'BTW verlegd' (of 'Verlegging van heffing'); de afnemer berekent de verschuldigde BTW zelf, neemt ze op in zijn periodieke aangifte en mag ze in dezelfde aangifte aftrekken (voor zover hij recht op aftrek heeft).

<small>📖 WBTW — art. 51 §2 — _wettekst_ · KB nr. 1 — art. 20 §3 — _kb_</small>

## Substantie

Economisch effect: de fiscale operatie wordt cash-neutraal voor de afnemer-belastingplichtige met recht op aftrek. Hij boekt tegelijk verschuldigde BTW (bv. op rooster 56 'BTW verschuldigd op intracommunautaire verwervingen') én aftrekbare BTW (rooster 59) — netto effect = nul, geen kasstroom richting Schatkist. Voor de leverancier: geen BTW innen, geen voorfinanciering, geen wanbetalings-risico op het BTW-bedrag. Voor de fiscus: het BTW-bedrag wordt door één partij (de afnemer) verwerkt in plaats van twee — minder risico op BTW-carrousel-fraude in fraudegevoelige sectoren (bouw, goud, CO2-rechten, GSM/CPU).

<small>🔗 WBTW — art. 51 §2 — _wettekst_ · KB nr. 1 — art. 20bis — _kb_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Rationale

Drie ratio's combineren in één regeling: (1) fraude-bestrijding in carrouselfraude-gevoelige sectoren — door de inning bij de afnemer te leggen verdwijnt de gelegenheid voor de leverancier om geïnde BTW niet door te storten ('missing trader'); (2) administratieve vereenvoudiging voor grensoverschrijdende handelingen — een buitenlandse leverancier hoeft zich niet voor BTW in België te identificeren wanneer zijn Belgische afnemer de BTW verlegt; (3) cash-flow-neutraliteit voor B2B-handelingen waar de afnemer toch volledig aftrekgerechtigd is — de tussenkomst van de fiscus is louter administratief. EU-rechtelijke basis: art. 194-199 Richtlijn 2006/112/EG.

<small>🔗 Richtlijn 2006/112/EG (BTW) — art. 194-199 — _richtlijn_ · Richtlijn 2006/112/EG (BTW) — art. 208 — _richtlijn_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Gebruikscontext

**Status**: `in-voege` · basis: WBTW art. 51 §2 + KB nr. 1 art. 20, 20bis, 20ter, 20quater + Richtlijn 2006/112/EG art. 194-199

Stabiele kern (sinds invoering EU-BTW-systeem). Sector-uitbreidingen worden periodiek toegevoegd via KB (laatste belangrijke: KB 17-12-2023 met ingang 01-01-2024).

**✅ Voor**
- 📖 Drie hoofdfamilies van toepassingsgevallen: (1) grensoverschrijdend — B2B-dienst geleverd door een niet-Belgische dienstverrichter aan een Belgische belastingplichtige (art. 51 §2 1° WBTW), intracommunautaire verwervingen door een Belgische belastingplichtige; (2) binnenlandse cocontractant-regeling in de bouwsector — werk in onroerende staat tussen twee Belgische BTW-plichtigen met periodieke aangifte (art. 20 KB nr. 1); (3) sectorspecifieke verleggingen voor fraudegevoelige goederen/diensten: goud en halffabricaten ≥ 325/1000 (art. 20bis), broeikasgas-emissierechten (art. 20ter), GSM-toestellen/CPU's/spelconsoles (art. 20quater).

**🚫 Niet voor**
- 📖 Geen verlegging mogelijk wanneer de afnemer geen belastingplichtige is gehouden tot het indienen van een periodieke aangifte (bv. particulier, BTW-eenheidsmedebelastingplichtige zonder eigen aangifte, btw-vrijstellingsregeling). In dat geval blijft de leverancier schuldenaar van de BTW volgens art. 51 §1 1° WBTW.

**📋 Voorwaarden**
- 📖 Cumulatief: (a) de afnemer is een belastingplichtige gehouden tot het indienen van een periodieke BTW-aangifte (art. 53 §1 1° 2° WBTW); (b) de handeling valt onder een specifieke verleggingscategorie (art. 51 §2 WBTW + uitvoerings-KB); (c) de leverancier vermeldt op de factuur 'Verlegging van heffing' en geen BTW-tarief noch -bedrag; (d) bij ontstentenis van bezwaar binnen één maand wordt de afnemer geacht zijn hoedanigheid van periodieke aangever te bevestigen.

**👍 Voordeel**
- 🔗 Voor leverancier: geen BTW-voorfinanciering, geen wanbetalingsrisico op BTW-component, geen verplichte BTW-identificatie in andere lidstaten bij grensoverschrijdende dienstverlening. Voor afnemer met volledig recht op aftrek: cash-neutraal. Voor fiscus: minder fraudegevoelig (geen 'missing trader').

**⚠️ Risico**
- 📖 Voor afnemer met beperkt recht op aftrek (gemengde of vrijgestelde belastingplichtige, niet-aftrekbare kosten bv. autokost): de verlegde BTW wordt verschuldigd maar niet (volledig) aftrekbaar — uiteindelijk een kost in plaats van een nul-operatie. Voor leverancier: hoofdelijke aansprakelijkheid (art. 51bis WBTW) wanneer de factuur onjuiste vermeldingen bevat over identiteit van afnemer of BTW-nummer.

## Bouwstenen

### 📜 IC-verlegging — B2B-diensten en intracommunautaire verwervingen

Wanneer een Belgische belastingplichtige een dienst afneemt van een niet in België gevestigde belastingplichtige die volgens de plaats-van-handeling-regels (art. 21 §2 WBTW — B2B-hoofdregel) geacht wordt in België plaats te vinden, is de Belgische afnemer schuldenaar van de Belgische BTW (art. 51 §2 1° WBTW). Hij vermeldt de operatie in zijn aangifte op rooster 87 (maatstaf) + rooster 55 (BTW verschuldigd) + rooster 59 (BTW aftrekbaar). Idem voor intracommunautaire verwervingen van goederen (rooster 86 + 55/57 + 59).

<small>📖 WBTW — art. 51 §1 2° — _wettekst_ · WBTW — art. 51 §2 1° — _wettekst_</small>

### 📜 Binnenlandse verlegging — cocontractant-regeling bouwsector (art. 20 KB nr. 1)

Tussen twee Belgische belastingplichtigen die beide periodieke aangiften indienen, wordt de BTW op werk in onroerende staat (bouw, installatie, herstel, onderhoud) verlegd naar de medecontractant-bouwheer. De aannemer factureert zonder BTW met de vermelding 'Verlegging van heffing'; de bouwheer-belastingplichtige neemt de BTW op in zijn aangifte (rooster 87/56 + 59). Sinds 01-01-2023 (uitgebreid 01-01-2024) ook toepasselijk op installaties van centrale verwarming, sanitair, elektriciteit, alarm, en op de levering+plaatsing van wandbekleding, keukens, badkamermeubilair, gootstenen, buitenrolluiken. Niet toepasselijk wanneer de bouwheer particulier is of geen periodieke BTW-aangever — dan factureert de aannemer met BTW.

<small>📖 KB nr. 1 — art. 20 §1 — _kb_ · KB nr. 1 — art. 20 §2 — _kb_</small>

### 📜 Sectorspecifiek — beleggingsgoud en halffabricaten ≥ 325/1000 (art. 20bis KB nr. 1)

Verlegging op leveringen van goud of halffabricaten van goud met zuiverheid ≥ 325 duizendsten, en op beleggingsgoud waarvoor de leverancier op de belastingheffing heeft geopteerd (art. 44bis §1 WBTW). De leverancier vermeldt 'Verlegging van heffing' op de factuur zonder tarief of bedrag; bij gebrek aan schriftelijke betwisting binnen één maand wordt de afnemer geacht periodieke aangifteplichtig te zijn.

<small>📖 KB nr. 1 — art. 20bis — _kb_ · Richtlijn 2006/112/EG — art. 208 — _richtlijn_</small>

### 📜 Sectorspecifiek — broeikasgas-emissierechten (art. 20ter KB nr. 1)

Verlegging op overdrachten van broeikasgas-emissierechten en daarmee gelijkgestelde eenheden uit het EU ETS-systeem (Richtlijn 2003/87/EG). Ratio: deze rechten waren een speelveld voor BTW-carrouselfraude door grote bedragen, immateriële aard en internationale verhandelbaarheid. Verlegging maakt de fraude-mechanica onmogelijk.

<small>📖 KB nr. 1 — art. 20ter — _kb_</small>

### 📜 Factuurvermelding 'Verlegging van heffing'

De factuur vermeldt 'Verlegging van heffing' (FR: 'Autoliquidation') en geen BTW-tarief noch -bedrag. Een gestandaardiseerde clausule moet uitleggen dat bij gebrek aan schriftelijke betwisting binnen één maand na ontvangst de afnemer geacht wordt te erkennen dat hij periodieke aangifteplichtig is, en dat hij — indien dit niet correct is — aansprakelijk wordt voor de verschuldigde BTW, interesten en boetes. Behoudens samenspanning is de leverancier dan ontslagen van aansprakelijkheid.

<small>📖 KB nr. 1 — art. 20 §3 — _kb_ · KB nr. 1 — art. 20bis — _kb_</small>

### ⚙️ Aangifte-mechaniek — gelijktijdige voldoening en aftrek

De afnemer neemt in dezelfde periodieke aangifte op: (a) verschuldigde BTW (rooster 55 binnenlandse cocontractant, rooster 56 IC-verwervingen, rooster 57 importen-onder-verlegging); (b) aftrekbare BTW (rooster 59). Bij volledig aftrekrecht: netto-effect = 0. Bij gemengde belastingplichtige: aftrek beperkt volgens algemeen verhoudingsgetal of werkelijke bestemming → effectieve BTW-kost.

<small>🔗 KB nr. 1 — art. 20bis — _kb_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Valkuilen

> [!warning]- Verlegging toepassen wanneer afnemer particulier of niet-aangifteplichtig is
> **Verkeerde assumptie**: Bij elke B2B-bouwfactuur 'verlegging' op de factuur zetten zonder de hoedanigheid van de afnemer te controleren.
>
> **Kernpunt**: Verlegging vereist dat de afnemer een periodieke BTW-aangifte indient. Voor particulieren én voor BTW-plichtigen onder de vrijstellingsregeling of de bijzondere landbouwregeling moet de aannemer BTW factureren. De clausule 'bij gebrek aan betwisting binnen één maand' beschermt de aannemer alleen bij niet-samenspanning — een aannemer die wist of moest weten dat de cliënt particulier was, wordt aansprakelijk gehouden voor de verschuldigde BTW.
>
> <small>📖 KB nr. 1 — art. 20 §1 — _kb_ · KB nr. 1 — art. 20 §3 — _kb_</small>

> [!warning]- Verlegging = vrijstelling
> **Verkeerde assumptie**: Studenten denken dat een handeling 'zonder BTW gefactureerd' = vrijgesteld van BTW.
>
> **Kernpunt**: Verlegging is géén vrijstelling. De handeling is volledig BTW-plichtig — alleen de plicht om de BTW te voldoen verschuift van leverancier naar afnemer. De afnemer is wel schuldenaar; hij neemt de BTW op in zijn aangifte (rooster 55/56/57) en mag ze afhankelijk van zijn aftrekrecht voor (een deel van) terugkrijgen via rooster 59. Vrijstellingen (art. 39-44bis WBTW) staan los van de verleggingsregeling.
>
> <small>🔗 WBTW — art. 51 §2 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

> [!warning]- Verlegging = altijd cash-neutraal
> **Verkeerde assumptie**: Een verlegde IC-dienst is altijd nul-impact voor de afnemer.
>
> **Kernpunt**: Nul-impact geldt enkel bij volledig recht op aftrek. Voor gemengde belastingplichtigen (bv. een bank, een ziekenhuis, een immobiliënvennootschap met vrijgestelde verhuur) is de verlegde BTW slechts gedeeltelijk aftrekbaar — het niet-aftrekbare deel wordt een echte kost. Voor niet-aftrekbare kosten (autokost art. 45 §2 WBTW, restaurant- en receptie-kosten) blijft hetzelfde regime gelden: BTW verschuldigd in rooster 56, géén of beperkt aftrekrecht in rooster 59.
>
> <small>🔗 WBTW — art. 45 §2 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Accountant-perspectieven

### Accountant in BTW-aangifte voor B2B-cliënt

_Standaard-cliënt met gemengde inkoop (binnenlands + EU + sector-specifiek)._

#### 💰 Fiscaal adviseur

##### 👣 Kwalificatie inkomende factuur — verlegging ja/nee?

Bij elke inkomende factuur drie vragen: (1) Is de leverancier in België gevestigd? Zo nee + dienst geacht in BE → verlegging IC-dienst (art. 51 §2 1°). (2) Is dit een werk in onroerende staat tussen twee BE-aangifteplichtigen? → cocontractant-regeling (art. 20 KB nr. 1). (3) Valt het goed/de dienst onder een sectorspecifieke verlegging (goud, emissierechten, GSM/CPU)? Geen vermelding 'Verlegging' op factuur waar het wel verplicht is → de leverancier kan worden gecorrigeerd; geen aftrek van niet-verschuldigde BTW.

<small>🔗 WBTW — art. 51 §2 — _wettekst_ · KB nr. 1 — art. 20 — _kb_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

#### 📒 Boekhouder

##### 🧭 BTW-roosters 55 / 56 / 57 correct toewijzen

Verlegde BTW komt op verschillende roosters naargelang de bron: rooster 55 (binnenlandse cocontractant + bv. art. 20bis/20ter), rooster 56 (IC-verwerving van goederen en IC-dienst), rooster 57 (verleggingen bij invoer met BTW-vergunning ET 14.000). Verkeerde rooster-toewijzing leidt tot afwijkende controles bij de fiscus, ook al klopt het totaal — de roosters dienen ook als data-grondslag voor de SAF-T en BTW-listing.

<small>🔗 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Verder lezen (scope-out)

- → Σ-keuzekader grensoverschrijdend → [[btw-grensoverschrijdend]] _(moet-verwijzen)_
- → Plaats-van-handeling B2B diensten (welke lidstaat is heffingsbevoegd) → [[plaats-van-handeling-btw]] _(moet-verwijzen)_

## Relaties

### `valt_onder`
- [[btw]]
### `is_uitzondering_op`
- [[btw]] — Afwijking van het hoofdbeginsel 'leverancier is schuldenaar van de BTW' (art. 51 §1 1° WBTW).
### `vereist`
- [[plaats-van-handeling-btw]] — Voor IC-verlegging op B2B-diensten moet eerst worden bepaald of de dienst in België plaatsvindt volgens art. 21 §2 WBTW.
### `vergelijkbaar_met`
- [[fiscaal-vertegenwoordiger-btw]]
    - **Gelijkenissen**:
        - Beide regelen wie de BTW voldoet wanneer de leverancier niet in België gevestigd is
        - Beide vermijden dat de niet-EU-leverancier voor BTW in België moet worden geïdentificeerd
    - **Verschillen**:
        - Verlegging: afnemer wordt schuldenaar (geen tussenpartij)
        - Fiscaal vertegenwoordiger: aparte Belgische tussenpartij wordt schuldenaar (in plaats van afnemer); verplicht voor niet-EU-leveranciers wanneer verlegging niet greep heeft
    - ⚠️ **Verwarringsrisico**: Beide regelingen overlappen in de pre-fase 'hoe wordt BTW geïnd bij grensoverschrijdende handelingen'. Verschil: verlegging werkt wanneer de Belgische medecontractant aangifteplichtig is; fiscaal vertegenwoordiger is nodig voor de gevallen die niet door verlegging worden gevangen.
