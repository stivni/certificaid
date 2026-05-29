---
title: "Groottecategorieën van vennootschappen"
concept_type: "kader"
schema_version: "2.2"
status: "concept"
categorieen:
  - kader
  - regeling
ankers:
  - 3.0.III
  - 3.0.III.A
tags:
  - concept
  - schema-2.2
  - type-kader
  - cat-kader
  - cat-regeling
  - status-concept
gegenereerd_uit: "data/concepten/records/vennootschap-groottecategorieen.json"
---

_Kader_ · ook: groottecriteria · size categories companies

## Definitie

Het Wetboek van vennootschappen en verenigingen (WVV) deelt vennootschappen in op basis van hun grootte. Voor jaarrekeningrechtelijke en controlerechtelijke doeleinden onderscheidt art. 1:24-1:27 drie hoofdcategorieën: **microvennootschap** (art. 1:25), **kleine vennootschap** (art. 1:24) en — impliciet, als restcategorie — de **grote vennootschap**. Naast deze WVV-categorieën gebruikt de fiscale wet eigen criteria (WIB92 art. 2 + art. 15) voor het KMO-tarief vennootschapsbelasting. De grootte wordt bepaald aan de hand van drie criteria — balanstotaal, jaaromzet (excl. btw) en gemiddelde aantal werknemers — telkens beoordeeld op balansdatum van het laatst afgesloten boekjaar.

<small>📖 WVV — art. 1:24 (klein) + art. 1:25 (micro) — _wettekst_ · CBN-advies 2022/03 — Definitie van kleine vennootschappen en microvennootschappen — _cbn_</small>

## Substantie

Voor de accountant is de groottecategorie hét vertrekpunt van bijna elk dossier: ze bepaalt welk jaarrekening-schema (micro · verkort · volledig) wordt gebruikt, of een commissaris moet worden aangesteld, of er moet worden geconsolideerd, welke publicatieverplichtingen gelden, en welke controlenormen (ISA versus ITAA-KMO-norm) van toepassing zijn. De categorie wordt jaarlijks her-getoetst — en wijzigt pas (omhoog of omlaag) na een **twee-jaar-overschrijdingsregel** (twee opeenvolgende boekjaren boven of onder de drempels). Bij de allereerste boekjaren van een nieuwe vennootschap geldt: schatten op basis van te goeder trouw schattingen (de eerste boekjaar-cijfers zijn nog niet 'historiek').

<small>🔗 WVV — art. 1:24 § 2 (twee-jaarsregel) — _wettekst_ · CBN-advies 2022/03 — Voorbeeld 1-2 (toepassings-cascade) — _cbn_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Rationale

De groottecategorieën vertalen het EU-principe 'think small first' (richtlijn 2013/34/EU): kleinere ondernemingen moeten verlost worden van administratieve overlast die voor grote bedrijven gerechtvaardigd is. Hoe kleiner de vennootschap, hoe lichter de informatieplicht (kleinere schema's), hoe minder controle (geen commissaris), en hoe minder publicatie (alleen verkort schema bij NBB). Dit beleid balanceert tussen transparantie naar derden (schuldeisers, fiscus, beleggers) en redelijke kosten voor de onderneming.

<small>🔗 EU-richtlijn 2013/34/EU (Accounting Directive) — Considerans + art. 3 (grootteklassen) — _richtlijn_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Gebruikscontext

**Status**: `in-voege` · sinds **2024-01-01** · basis: WVV art. 1:24-1:27 (W 23-03-2019); drempels herzien door KB 21 maart 2024 (substantiële verhoging na EU-aanpassing voor inflatie)

De drempelwaarden werden bij KB van 21 maart 2024 substantieel verhoogd om EU-richtlijn 2023/2775 om te zetten. Boekjaren startend vanaf 1 januari 2024 vallen onder de nieuwe drempels. Voor boekjaren daarvóór gelden de oude drempels — CBN-advies 2024/08 bespreekt de overgangs-perikelen voor v(z)w's.

## Sub-concepten

### 📦 Microvennootschap (art. 1:25 WVV)

#### Definitie

Microvennootschap is een **kleine vennootschap** die geen dochter- of moedervennootschap is en die op balansdatum **niet meer dan één** van de volgende criteria overschrijdt (drempels vanaf BJ 2024, na verhoging KB 21-03-2024):
• Balanstotaal: 450.000 EUR
• Jaaromzet (excl. btw): 900.000 EUR
• Gemiddeld aantal werknemers (jaargemiddelde): 10

Gevolg: mag de **micro-schema-jaarrekening** gebruiken (kortste schema), met sterk vereenvoudigde toelichting. Geen commissaris vereist. Lichte publicatieplicht (alleen micro-schema bij NBB).

<small>📖 WVV — art. 1:25 — _wettekst_ · CBN-advies 2022/03 — Definitie microvennootschappen — _cbn_</small>

### 📦 Kleine vennootschap (art. 1:24 WVV)

#### Definitie

Een vennootschap is **klein** als ze op balansdatum **niet meer dan één** van de volgende criteria overschrijdt (drempels vanaf BJ 2024):
• Balanstotaal: 6.000.000 EUR (vroeger 4.500.000)
• Jaaromzet (excl. btw): 11.250.000 EUR (vroeger 9.000.000)
• Gemiddeld aantal werknemers: 50

Dochters en moedervennootschappen worden voor deze test beoordeeld op **geconsolideerd niveau**. Een vennootschap die deel uitmaakt van een groep én meer dan 50 werknemers heeft, kan nooit klein zijn — ongeacht balans en omzet (art. 1:24 § 3).

<small>📖 WVV — art. 1:24 § 1 + § 3 — _wettekst_ · Aangifte VenB 2025 — Blz. 14 — Vak grootte van de vennootschap — _aangifte_ · KB 21 maart 2024 — art. 1 (drempel-verhoging) — _kb_</small>

#### Substantie

Een kleine vennootschap mag het **verkort schema** gebruiken (of micro-schema indien zij ook micro is). Geen commissaris vereist. Geen geconsolideerde jaarrekening (vrijstelling). Genieten van fiscale gunstregimes (KMO-tarief VenB 20% op eerste 100.000 EUR, investeringsaftrek, taxshelter, ...).

<small>🔗 WVV — art. 3:4-3:23 — _wettekst_ · WIB92 — art. 215 (KMO-tarief) — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### 📦 Grote vennootschap

#### Definitie

Een vennootschap is **groot** zodra ze niet klein is — d.w.z. ze overschrijdt meer dan één van de kleine-drempels, of ze hoort tot een groep met >50 werknemers. Verplichtingen voor grote vennootschappen: **volledig jaarrekening-schema**, **aanstelling commissaris** (art. 3:72 WVV) tenzij uitzonderingen, **geconsolideerde jaarrekening** indien moedervennootschap (art. 3:22 e.v.), **volledige publicatie** bij NBB. De ISA-controlenormen (Internationale Standaarden voor Audit) zijn integraal van toepassing bij wettelijke controle.

<small>📖 WVV — art. 3:22 (consolidatie) — _wettekst_ · WVV — art. 3:62 + 3:72 (commissaris) — _wettekst_</small>

### 📦 Twee-jaar-overschrijdingsregel

#### Definitie

Een vennootschap wisselt van categorie pas wanneer de drempels gedurende **twee opeenvolgende boekjaren** worden overschreden — niet bij een eenmalige piek (art. 1:24 § 2). Dit voorkomt jojo-effect bij conjuncturele schommelingen. Bijgevolg: een vennootschap die in BJ 2024 voor het eerst de kleine-drempels overschrijdt blijft 'klein' tot het einde van BJ 2025; pas vanaf BJ 2026 wordt zij 'groot' (mits ook BJ 2025 boven drempel was).

<small>📖 WVV — art. 1:24 § 2 (mutatis mutandis art. 1:25 § 2) — _wettekst_ · CBN-advies 2022/03 — Voorbeelden van toepassing tweejaars-regel — _cbn_</small>

#### Substantie

Belangrijke uitzondering: **bij eerste boekjaar** van een nieuwe vennootschap geldt de tweejaars-regel niet — daar werkt men met te goeder trouw schattingen op basis van budget en plan. Bij **wijziging boekjaar-duur** worden de drempels pro rata aangepast (omzet en personeel worden geannualiseerd).

<small>📖 CBN-advies 2022/03 — Eerste boekjaar + wijziging boekjaar-duur — _cbn_</small>

### 📦 Groepsniveau-beoordeling (geconsolideerde drempels)

#### Definitie

Een vennootschap die een dochteronderneming of moedermaatschappij is, of die deel uitmaakt van een **consortium**, moet de groottedrempels **op geconsolideerd niveau** beoordelen (art. 1:24 § 3 + § 6 + art. 1:26). Met andere woorden: de jaaromzet, het balanstotaal en het personeelsbestand van alle groepsvennootschappen worden samen geteld, na eliminatie van interne stromen, en daarop wordt de drempel-toets gedaan. Doel: voorkomen dat een grote groep zich verkleed in kleine dochtervennootschappen om aan controle-en consolidatieplicht te ontsnappen.

<small>📖 WVV — art. 1:24 § 3 + § 6 — _wettekst_ · CBN-advies 2022/03 — Voorbeeld 1 — consortium — _cbn_ · WIB92 — art. 2 — 5°/1 (definitie groep) — _wettekst_</small>

### 📦 Cascade van gevolgen per categorie

#### Definitie

De groottecategorie triggert vijf wezenlijke gevolgen: (1) **Jaarrekening-schema** — micro/verkort/volledig (art. 3:4-3:6); (2) **Wettelijke controle** — commissaris verplicht bij grote (art. 3:72) — bij kleine niet (uitzonderingen: openbaar belang, beursgenoteerd); (3) **Consolidatieplicht** — alleen grote moederv. moeten geconsolideerde jaarrekening opmaken (art. 3:22) — kleine zijn vrijgesteld als 'kleine groep'; (4) **Publicatieformaliteiten** — micro publiceert micro-schema, klein publiceert verkort, groot volledig + jaarverslag + commissarisverslag; (5) **Controlenorm-toepasselijkheid** — voor wettelijke controle op grote: ISA (volledige internationale standaarden); voor vrijwillige opdrachten KMO: ITAA-KMO-controlenorm (lichter).

<small>📖 WVV — art. 3:4 (schemakeuze) — _wettekst_ · WVV — art. 3:22 (consolidatie) — _wettekst_ · WVV — art. 3:72 (commissaris) — _wettekst_</small>

### 📦 Verschil met fiscale KMO-criteria (WIB92)

#### Definitie

Voor het KMO-tarief vennootschapsbelasting (20% op eerste 100.000 EUR) hanteert de fiscale wet **eigen criteria** (WIB92 art. 2 + art. 15). Niet alle WVV-kleine vennootschappen kwalificeren fiscaal. Bijkomende fiscale voorwaarden o.a.: bedrijfsleidersbezoldiging ≥ 45.000 EUR (of ≥ belastbaar resultaat indien lager), geen 'financiële vennootschap', niet meer dan 50% beleggingen, geen onderdeel van groep met grote venn. Verwarring tussen WVV-klein en fiscaal-KMO is een klassieke val.

<small>📖 WIB92 — art. 215 (KMO-tarief) — _wettekst_ · WIB92 — art. 1:24-1:25 — _wettekst_</small>

## Bouwstenen

### 📏 Drempels kleine vennootschap (vanaf BJ 2024)

Drempels art. 1:24 § 1 WVV (geldig vanaf boekjaren startend vanaf 1-1-2024 ingevolge KB 21-03-2024):
• Balanstotaal: **6.000.000 EUR** (was 4.500.000)
• Jaaromzet excl. btw: **11.250.000 EUR** (was 9.000.000)
• Gemiddelde aantal werknemers (jaargemiddelde): **50**

Eén overschrijden is OK; twee of drie overschrijden = niet meer klein (na tweejaars-regel).

<small>📖 WVV — art. 1:24 § 1 — _wettekst_ · KB 21 maart 2024 — art. 1 — _kb_</small>

### 📏 Drempels microvennootschap (vanaf BJ 2024)

Drempels art. 1:25 § 1 WVV (geldig vanaf BJ 2024):
• Balanstotaal: **450.000 EUR** (was 350.000)
• Jaaromzet excl. btw: **900.000 EUR** (was 700.000)
• Gemiddelde aantal werknemers: **10**

Bijkomende voorwaarde: GEEN dochter- of moedervennootschap zijn — micro = strikt 'stand-alone' kleine venn.

<small>📖 WVV — art. 1:25 § 1 — _wettekst_ · KB 21 maart 2024 — art. 2 — _kb_</small>

### 📜 'Niet meer dan één'-regel

Een vennootschap is klein/micro als ze **niet meer dan één** van de drie drempels overschrijdt. Dat betekent: overschrijden van twee of drie drempels = niet meer klein. Het is dus geen 'alle drie'-test maar een 'maximum één'-test. Verwarring hierover is wijdverbreid bij studenten.

<small>📖 WVV — art. 1:24 § 1 — _wettekst_ · Aangifte VenB 2025 — Didactische opmerkingen — _aangifte_</small>

## Voorbeelden

> [!example]- Categorisering Aurelia Industrie BV — BJ 2024
> _Aurelia Industrie BV behaalt in BJ 2024: balanstotaal 5.500.000 EUR · jaaromzet excl. btw 12.000.000 EUR · 45 werknemers gemiddeld. Geen dochter, geen moeder. In BJ 2023: balans 4.200.000 · omzet 10.500.000 · 42 werknemers._
>
> **📋 Toets aan kleine-drempels BJ 2024**
>
> Criterium | Drempel | Aurelia BJ 2024 | Aurelia BJ 2023 | Overschreden?
> ---|---|---|---|---
> Balanstotaal | 6.000.000 | 5.500.000 | 4.200.000 | Nee
> Jaaromzet | 11.250.000 | 12.000.000 | 10.500.000 | **2024 ja, 2023 nee**
> Werknemers | 50 | 45 | 42 | Nee
>
> Besluit BJ 2024: 1 drempel overschreden → nog klein.
> Maar in BJ 2025 indien omzet opnieuw > 11.250.000: dan twee opeenvolgende jaren overschrijding van één drempel — alsnog klein (slechts één criterium). Pas wanneer twee criteria gedurende twee jaar overschreden zijn, kantelt de categorie naar groot.
>
> <small>🔗 CBN-advies 2022/03 — Voorbeeld 1 — _cbn_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Valkuilen

> [!warning]- 'Alle drie de drempels' vs 'meer dan één'
> **Verkeerde assumptie**: Een vennootschap is klein zolang ze niet alle drie de drempels overschrijdt.
>
> **Kernpunt**: Onjuist. De test is **'meer dan één'** — twee drempels overschrijden is al genoeg om uit de 'klein'-categorie te vallen. Een vennootschap met 60 werknemers en 13 miljoen omzet is dus groot, ook al is haar balans nog onder de 6 miljoen.
>
> <small>📖 WVV — art. 1:24 § 1 — _wettekst_</small>

> [!warning]- WVV-klein = fiscaal-KMO
> **Verkeerde assumptie**: Een vennootschap die WVV-klein is, geniet automatisch het KMO-tarief vennootschapsbelasting.
>
> **Kernpunt**: De fiscale wet heeft extra voorwaarden (WIB92 art. 215 § 2-3): bedrijfsleidersbezoldiging-minimum, geen 'financiële vennootschap', geen groepsdochter. Een WVV-kleine venn kan dus alsnog buiten het KMO-tarief vallen. Cijferzakboekje raadplegen voor de actuele bedragen.
>
> <small>📖 WIB92 — art. 215 § 2-3 — _wettekst_</small>

> [!warning]- Eenmalige overschrijding = onmiddellijke wijziging
> **Verkeerde assumptie**: Zodra de drempels in één boekjaar worden overschreden, wisselt de categorie van klein naar groot.
>
> **Kernpunt**: Toepassing van de twee-jaarsregel (art. 1:24 § 2): pas wanneer twee opeenvolgende boekjaren de drempels worden overschreden, wijzigt de categorie. Een eenmalige conjuncturele piek heeft geen onmiddellijk gevolg.
>
> <small>📖 WVV — art. 1:24 § 2 — _wettekst_</small>

> [!warning]- Groottedrempels op stand-alone-basis voor groep-venn
> **Verkeerde assumptie**: Bij een dochtervennootschap kijken we naar de eigen cijfers, niet naar de groep.
>
> **Kernpunt**: Voor moeder- en dochtervennootschappen worden de drempels **geconsolideerd** beoordeeld (art. 1:24 § 3). Een kleine dochter binnen een grote groep is voor jaarrekeningrechtelijke doeleinden dus 'groot'. Dit voorkomt fragmentatie van een grote groep in kleine dochters om aan administratieve verplichtingen te ontsnappen.
>
> <small>📖 WVV — art. 1:24 § 3 + § 6 — _wettekst_</small>

## Accountant-perspectieven

### Bij jaarafsluiting: bepaal de groottecategorie

#### 📒 Boekhouder

##### 👣 Drempels toetsen aan einde boekjaar

Stap 1: Verzamel cijfers boekjaar — balanstotaal (na waardering), jaaromzet excl. btw, jaargemiddelde werknemers (via DmfA-aangiftes). Stap 2: Toets aan kleine-drempels (1:24) — meer dan één overschreden? Stap 3: Indien klein, toets ook aan micro-drempels (1:25) + check 'geen dochter/moeder'. Stap 4: Apply twee-jaarsregel (kijk ook BJ-1). Stap 5: Bij groep — herhaal op geconsolideerd niveau.

<small>🔗 WVV — art. 1:24-1:25 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

##### 👣 Jaarrekening-schema kiezen

Micro → micro-schema (bijlage 8 KB WVV); klein → verkort schema (bijlage 7); groot → volledig schema (bijlage 6) + jaarverslag + (in voorkomend geval) commissarisverslag. Schema-keuze beïnvloedt sterk de complexiteit en bijgevolg de kosten van de jaarrekening-opdracht.

<small>📖 WVV — art. 3:4-3:6 — _wettekst_ · KB WVV — Bijlage 6-7-8 — _wettekst_</small>

#### 💰 Fiscaal adviseur

##### 👣 Fiscaal-KMO-check apart uitvoeren

Doe een aparte test op de fiscale KMO-voorwaarden (WIB92 art. 215 § 2-3): bedrijfsleidersbezoldiging, financiële-vennootschap-test, groepsverbod. Een WVV-klein die niet fiscaal-KMO is, mist het 20%-tarief — een aanzienlijk fiscaal nadeel. Documenteer de toets in het belastingsdossier.

<small>📖 WIB92 — art. 215 § 2-3 — _wettekst_</small>

## Verder lezen (scope-out)

- → Parent — ondernemingsvormen → [[ondernemingsvormen]] _(moet-verwijzen)_
- → Jaarrekening-schema-keuze (volledig · verkort · micro) → [[jaarrekening]] _(moet-verwijzen)_
- → KMO-tarief vennootschapsbelasting — aparte fiscale criteria → ⏳ kmo-tarief-vennootschapsbelasting _(moet-verwijzen)_
- → Wettelijke controle door commissaris (trigger via grootte) → [[controleopdracht]] _(moet-verwijzen)_

## Relaties

### `valt_onder`
- [[ondernemingsvormen]]
### `triggert`
- [[jaarrekening]]
- [[controleopdracht]]
