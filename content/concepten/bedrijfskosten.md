---
title: "Bedrijfskosten"
concept_type: "balanspost"
schema_version: "2.2"
status: "concept"
categorieen:
  - entiteit
ankers:
  - 1.1.II.M
tags:
  - concept
  - schema-2.2
  - type-balanspost
  - cat-entiteit
  - status-concept
gegenereerd_uit: "data/concepten/records/bedrijfskosten.json"
---

_Balanspost_ · ook: operationele kosten · operating expenses

## Definitie

Bedrijfskosten zijn alle kosten die voortvloeien uit de gewone bedrijfsuitoefening van de onderneming — dat wil zeggen kosten verbonden aan haar operationele activiteit (productie, handel, dienstverlening). In het Belgische Minimum Algemeen Rekeningenstelsel (MAR-KB 21.10.2018) zitten ze in klasse 60-65: 60 (handelsgoederen, grond- en hulpstoffen), 61 (diensten en diverse goederen), 62 (personeelskosten), 630/631 (afschrijvingen en waardeverminderingen op oprichtingskosten en vaste activa), 634 (waardeverminderingen op voorraden, bestellingen en vorderingen), 635-637 (voorzieningen), 640-649 (andere bedrijfskosten zoals bedrijfsbelastingen, minderwaarden). Bedrijfskosten vormen samen met bedrijfsopbrengsten (klasse 70-74) het bedrijfsresultaat — de kern van de operationele winstgevendheid.

<small>📖 Minimum Algemeen Rekeningstelsel voor boekhoudplichtige ondernemingen — KB 21.10.2018 Bijlage 1 — Klasse 6 — _kb_</small>

## Substantie

Bedrijfskosten meten 'wat het kost om te ondernemen' — los van financiering (klasse 65) en uitzonderlijke verrichtingen (klasse 66). De stagiair moet drie dingen scherp houden: (1) het onderscheid kosten- vs uitgaven — een kost is een verbruik in het boekjaar (matching-principe), een uitgave is een betaling; cash flow ≠ winst. (2) De MAR is geen vrije lijst maar een verplichte minimumstructuur (KB 2018) — elke onderneming moet rubriek 60-65 herkenbaar gebruiken. (3) Resultatenrekening kent twee voorstellingen: per natuur (60+61+62+630+634+...) of per functie (kostprijs verkopen + distributiekosten + administratiekosten — IAS 1 §103). België: naturenindeling dominant, IFRS-rapporteurs kunnen ook functioneel.

<small>🔗 KB 29.04.2019 (uitvoering WVV) — art. 3:84 (vorm jaarrekening) — _kb_ · Verordening (EU) 2023/1803 — IAS 1 — §103 — _wettekst_</small>

## Rationale

Het MAR-onderscheid bedrijfs- vs financieel vs uitzonderlijk dient analyse en vergelijkbaarheid. Het bedrijfsresultaat (REBITDA-achtige logica) toont of de kernactiviteit rendabel is, los van financieringskeuzes (te veel schuld? → klasse 65) of eenmalige gebeurtenissen (herstructurering, desinvestering — klasse 66 vóór 2020, sinds reform 2020 deels heringedeeld). Voor de stagiair: leer de klasse-codes uit het hoofd — examen bevat steeds rubricerings-vragen.

<small>🔗 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Gebruikscontext


**✅ Voor**
- 📖 Boeken van facturen, lonen, afschrijvingen tijdens het boekjaar — elke aankoop, dienst, salaris belandt op een klasse 60-65 rekening.
- 📖 Opstellen van de resultatenrekening per einde boekjaar — bedrijfskosten worden gesaldeerd tegen bedrijfsopbrengsten (klasse 70-74) om bedrijfsresultaat te bekomen.

## Sub-concepten

### 📦 60 — Handelsgoederen, grond- en hulpstoffen

#### Definitie

Klasse 60 dekt aankopen van goederen die de onderneming verbruikt of doorverkoopt: 600 grondstoffen · 601 hulpstoffen · 602 diensten/werk/studies · 603 algemene onderaannemingen · 604 handelsgoederen · 605 onroerende goederen bestemd voor verkoop · 608 ontvangen kortingen (creditrekening) · 609 voorraadwijzigingen. Boekingsmoment: bij ontvangst factuur. Voorraadwijziging (609) corrigeert kosten naar verbruik (matching).

<small>📖 MAR-KB — Bijlage 1 — klasse 60 — _kb_</small>

> [!example]- Aankoop handelsgoederen 1.000 EUR + 21% btw
> _Zelena Bio NV koopt voor 1.000 EUR handelsgoederen (factuur leverancier ARGENTA Bio NV)._
>
> **📒 Boeking factuur leverancier**
>
> | Rekening | Debet | Credit |
> | --- | --- | --- |
> | 604 — Aankopen handelsgoederen | 1.000 |  |
> | 411 — Terug te vorderen btw | 210 |  |
> | 440 — Leveranciers |  | 1.210 |
>
> <small>🔗 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### 📦 61 — Diensten en diverse goederen

#### Definitie

Klasse 61 omvat kosten van diensten geleverd door derden + diverse goederen niet bestemd voor wederverkoop. Typisch: huur, energie, onderhoud, verzekeringen, erelonen advocaten/accountants, marketing, telecom, kantoorbenodigdheden. Boeking netto btw (voor aftrekbare btw); voor 100% beroepskosten wagen blijft 50% btw niet aftrekbaar — naar 6405.

<small>📖 CBN-advies 2016/26 — Diensten en diverse goederen — boekhoudkundige verwerking — _cbn_</small>

> [!example]- Ereloon accountant 2.500 EUR + 21% btw
> **📒 Boeking ereloon**
>
> | Rekening | Debet | Credit |
> | --- | --- | --- |
> | 613 — Ereloon en kosten van derden | 2.500 |  |
> | 411 — Terug te vorderen btw | 525 |  |
> | 440 — Leveranciers |  | 3.025 |
>
> <small>🔗 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### 📦 62 — Personeelskosten

#### Definitie

Klasse 62 omvat totale loonkost: 620 bezoldigingen + 621 werkgeversbijdragen RSZ + 622 werkgeverspremies extra-wettelijke verzekeringen + 623 andere personeelskosten + 624 pensioenen + 625 voorzieningen sociale verplichtingen. Detail in apart record personeelskosten — hier alleen positie binnen MAR.

<small>📖 MAR-KB — Bijlage 1 — klasse 62 — _kb_</small>

### 📦 630/631 — Afschrijvingen en waardeverminderingen op vaste activa

#### Definitie

630 afschrijvingen op oprichtingskosten + immateriële + materiële vaste activa (kosten van de spreiding-in-tijd van de aanschaffingswaarde). 631 waardeverminderingen op vaste activa (bijzondere waardeverlies — niet de jaarlijkse afschrijving). Tegenpost in actief: 20-28 met negatief teken (rubriek ...9 afschrijvingen).

<small>📖 MAR-KB — Bijlage 1 — klasse 630/631 — _kb_</small>

> [!example]- Jaarlijkse afschrijving machine 10.000 EUR / 10 jaar = 1.000 EUR
> _Zelena Bio bezit een productiemachine (aanschaffingswaarde 10.000 EUR, lineair over 10 jaar)._
>
> **📒 Boeking jaarafschrijving**
>
> | Rekening | Debet | Credit |
> | --- | --- | --- |
> | 6302 — Afschrijvingen op materiële vaste activa | 1.000 |  |
> | 2309 — Geboekte afschrijvingen op installaties/machines (-) |  | 1.000 |
>
> <small>🔗 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### 📦 634 — Waardeverminderingen op voorraden, bestellingen en handelsvorderingen

#### Definitie

Waardevermindering ≠ afschrijving: afschrijving is systematisch (over levensduur), waardevermindering is bijzonder (concreet waardeverlies vastgesteld). Op voorraad: onverkoopbaar, technisch verouderd. Op handelsvorderingen: dubieuze debiteur (faillissement, lange betalingsachterstand). Boekingsregel CBN: documenteer per debiteur de risico-inschatting.

<small>🔗 MAR-KB — Bijlage 1 — klasse 634 — _kb_</small>

### 📦 640-649 — Andere bedrijfskosten

#### Definitie

Bedrijfsbelastingen + minderwaarden op courante realisatie + diverse. Sub-rubrieken: 640 bedrijfsbelastingen (verkeersbelasting, onroerende voorheffing, registratierechten, niet-aftrekbare btw, gemeente- en provinciebelastingen, milieuheffingen) · 641 minderwaarden op realisatie courante vaste activa · 642 minderwaarden op realisatie handelsvorderingen · 643/648 andere · 649 als bedrijfskosten op te nemen herstructureringskosten (zie CBN 2011/24).

<small>📖 MAR-KB — Bijlage 1 — klasse 640-649 — _kb_ · CBN-advies 2011/24 — Herstructureringskosten — _cbn_</small>

## Valkuilen

> [!warning]- Klasse 6 ≠ uitgave
> **Verkeerde assumptie**: Een kost in klasse 6 betekent dat er deze maand cash is betaald.
>
> **Kernpunt**: Kost ≠ uitgave. Bij ontvangst factuur boek je 60-65 (kost) tegenover 440 (leveranciers, schuld) — pas bij betaling beweegt 55 bank. Bij afschrijving: enkel boekhoudkundige spreiding, geen cash-beweging. Voor liquiditeitsanalyse: kijk naar bewegingen klasse 55 + werkkapitaal, niet naar klasse 6.
>
> <small>🔗 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

> [!warning]- Niet-aftrekbare btw vergeten
> **Verkeerde assumptie**: Btw is altijd terug te vorderen (klasse 411) — kost is netto.
>
> **Kernpunt**: Niet-aftrekbare btw (bv. 50% wagenkosten, gemengd privé/zakelijk, vrijgestelde activiteit) wordt onderdeel van de kost en geboekt op 6405 (niet-aftrekbare btw) of opgenomen in de hoofdkostrekening. Aandacht bij wagens, restaurantkosten, relatiegeschenken.
>
> <small>📖 MAR-KB — rubriek 6405 — _kb_</small>

> [!warning]- Herstructureringskosten = uitzonderlijk?
> **Verkeerde assumptie**: Herstructureringskosten horen automatisch onder klasse 66 (uitzonderlijke kosten) of 76 (uitzonderlijke opbrengsten).
>
> **Kernpunt**: CBN 2011/24: herstructureringskosten kunnen als bedrijfskosten (649) OF als uitzonderlijk worden geboekt, afhankelijk van aard en omvang. Sinds reform 2020 (KB 29.04.2019) is klasse 66/76 deels heringedeeld — veel posten verschoven naar bedrijfs- of financieel resultaat. Documenteer keuze in toelichting.
>
> <small>📖 CBN-advies 2011/24 — Herstructureringskosten — verwerking in de jaarrekening — _cbn_</small>

## Syntheses

### 🧩 Matrix

Naturenindeling (Belgische MAR standaard) vs functionele indeling (IAS 1 §103, optioneel).

| MAR-rubriek (naturen) | IAS 1 functionele rubriek (typisch) |
| --- | --- |
| 60 + 609 voorraadwijziging | Kostprijs verkopen (deels) |
| 61 (huur, energie productiehal) | Kostprijs verkopen of distributiekosten |
| 61 (marketing, commerciële agenten) | Distributiekosten |
| 62 productie-personeel | Kostprijs verkopen |
| 62 administratie-personeel | Beheerskosten |
| 630 afschrijving machine productie | Kostprijs verkopen |
| 630 afschrijving kantoor | Beheerskosten |
| 640 bedrijfsbelastingen | Andere lasten |

## Accountant-perspectieven

### Onderneming zelf — operationele boekhouding

_Het accountantskantoor voert de boekhouding van de cliënt-onderneming._

#### 📒 Boekhouder

##### 👣 Juiste klasse-6-rubriek kiezen

Per inkomende factuur: (1) is dit een handelsgoed/grondstof voor doorverkoop/productie → klasse 60 (sub 600-605). (2) Is dit een dienst van een derde of een diverse-goed (energie, huur, papier) → klasse 61 (sub 610-619). (3) Is dit personeelsgerelateerd → klasse 62. (4) Is dit een bedrijfsbelasting → 640. (5) Is dit een minderwaarde of herstructureringskost → 641-649. Documenteer beleidsregel voor gemende posten (bv. erelonen accountant = 613, leasing wagens = 612, brandstofkosten = 6112).

<small>🔗 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

##### 👣 Afschrijvingen + waardeverminderingen op jaarafsluit boeken

Per einde boekjaar: afschrijvingsbatch boeken (630.xxxx debet, 2xxx9 credit) volgens afschrijvingstabel. Waardeverminderingen op voorraad (633) en op dubieuze handelsvorderingen (634) na inventaris-toets. Documenteer per dossier de afschrijvingsgrondslag (lineair / degressief / aanschaffingswaarde / restwaarde) — vereist door art. 3:42 KB WVV.

<small>🔗 KB 29.04.2019 — art. 3:42 — _kb_</small>

#### 🔍 Auditor

##### 👣 Existentie en volledigheid bedrijfskosten

Existentie: steekproef facturen (klasse 60-61), check werkelijk geleverd. Volledigheid: cut-off test eind boekjaar — facturen die in januari binnenkomen voor diensten geleverd in december → te boeken via 492 (overlopende rekening passief). Analytisch: vergelijk huidige bedrijfskosten met vorig boekjaar + budget; abnormale schommelingen onderzoeken (kostprijs-marge ratio).

<small>🔗 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

##### 👣 Classificatie bedrijfskosten vs financieel/uitzonderlijk

Toets dat klasse-65 kosten effectief financieringskosten zijn (rente, koersverschil, financiële schulden — geen bedrijfsmatige kosten verstopt om bedrijfsresultaat te flatteren). Herstructureringskosten: keuze 649 of (post-reform 2020) bedrijfsmatig — vraag rationale + CBN 2011/24-conformiteit. Boekhoudkundige fraude-indicator: plotse stijging klasse 66 net vóór desinvestering = verschuiving operationele kosten.

<small>🔗 CBN-advies 2011/24 — Herstructureringskosten — _cbn_</small>

#### 💰 Fiscaal adviseur

##### 📜 Aftrekbaarheid bedrijfskosten — art. 49 WIB92

Algemene regel: bedrijfskosten zijn aftrekbaar mits gemaakt om belastbare inkomsten te verwerven of te behouden (art. 49 WIB92) + werkelijkheidsvoorwaarde + bewijsstukken. Beperkingen WIB92 art. 53-66bis: 50% aftrek restaurantkosten (al sinds AJ 2005), beperkte aftrek wagenkosten volgens CO2-formule, 0% relatiegeschenken > 50 EUR, etc. Aangifte: VenB-vak ZZ 'verworpen uitgaven' voor het niet-aftrekbare deel. Documenteer scheiding boekhoudkundige kost (volledig in klasse 6) vs fiscaal aftrekbaar deel.

<small>📖 WIB92 — art. 49 + 53-66bis — _wettekst_</small>

## Verder lezen (scope-out)

- → Bedrijfsopbrengsten (klasse 70-74) → [[bedrijfsopbrengsten]] _(moet-verwijzen)_
- → Personeelskosten — detail klasse 62 → [[personeelskosten]] _(moet-verwijzen)_
- ↪ Resultaatverwerking (jaarafsluit) → [[resultaatverwerking]] _(mag-verwijzen)_
- ↪ Financiële kosten (klasse 65) → ⏳ financiele-kosten _(mag-verwijzen)_

## Relaties

### `valt_onder`
- ⏳ resultatenrekening — Bedrijfskosten = debetzijde bedrijfsresultaat-deel van de resultatenrekening.
### `vergelijkbaar_met`
- [[bedrijfsopbrengsten]]
    - **Gelijkenissen**:
        - Beide vormen het bedrijfsresultaat
        - Beide MAR-klassen 6 vs 7
    - **Verschillen**:
        - Bedrijfskosten = klasse 60-65 (debet)
        - Bedrijfsopbrengsten = klasse 70-74 (credit)
### `bevat`
- [[personeelskosten]] — Klasse 62 is sub-rubriek van bedrijfskosten.
### `vereist`
- ⏳ rekeningstelsel-mar — Klasse-6-rubricering veronderstelt kennis van het MAR.
