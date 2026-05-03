---
tags: ["1.5", wip, materie]
niveau: integratie
status: draft
bouwversie: 2
bronnen:
  - IAS 1 (Presentation of Financial Statements)
  - IAS 7 (Statement of Cash Flows)
  - IFRS 1 (First-time Adoption of IFRS)
  - Richtlijn 2013/34/EU art. 4, 6
  - KB WVV 2019 art. 3:1, 3:7
---

# Presentatie van de jaarrekening (IFRS)

Onder IFRS is **IAS 1 — Presentation of Financial Statements** de centrale standaard voor de structuur, naamgeving en kwalitatieve kenmerken van de jaarrekening. Ze regelt het algemene kader. **IAS 7** vult dit aan met de kasstroomtabel; **IFRS 1** regelt de eerste toepassing wanneer een vennootschap voor het eerst IFRS toepast.

Deze fiche behandelt: bestanddelen, kwalitatieve kenmerken, schema's en de afwijkingen tegenover Belgisch GAAP. Voor het bredere rechtskader (verordening, richtlijn, toepassingsgebied) zie [[ifrs-rechtskader]].

---

## 📌 Bestanddelen van de jaarrekening (IAS 1)

*Statement of Financial Statements*

Een **complete IFRS-jaarrekening** bestaat uit vijf primaire overzichten plus toelichting (IAS 1 §10):

1. **Balans** — *Statement of Financial Position*
2. **Resultatenrekening en niet-gerealiseerde resultaten** — *Statement of Profit or Loss and Other Comprehensive Income* (eventueel als één gecombineerd of als twee aparte overzichten)
3. **Mutatieoverzicht eigen vermogen** — *Statement of Changes in Equity*
4. **Kasstroomtabel** — *Statement of Cash Flows* (geregeld door IAS 7)
5. **Toelichting** — *Notes*, met grondslagen voor financiële verslaglegging en aanvullende informatie
6. **Vergelijkende informatie** voor de voorgaande periode (verplicht)
7. Bij retroactieve aanpassing of herclassificatie: ook een **derde balans** per begin van de vorigste periode

Onder Belgisch GAAP daarentegen bestaat de jaarrekening uit drie bestanddelen: **balans**, **resultatenrekening** en **toelichting** ([[bronnen/wetteksten/XV-wvv#art-31|WVV art. 3:1]]). Een mutatieoverzicht eigen vermogen en een kasstroomtabel zijn er **geen verplichte onderdelen** van — zie [[jaarrekening#-jaarrekening|Jaarrekening (BE-GAAP)]].

---

## 📌 Identificatie van de jaarrekening

IAS 1 §49-53 vereist dat elk overzicht en de toelichting **duidelijk identificeerbaar** zijn:

- Naam van de rapporterende entiteit
- Of het de jaarrekening van een individuele entiteit of een groep betreft
- Datum van afsluiting van de verslagperiode (of de periode waarop het overzicht betrekking heeft)
- Presentatievaluta (bv. EUR, USD)
- Niveau van afronding (in eenheden, duizenden, miljoenen)

Onder Belgisch GAAP wordt deze identificatie afgehandeld via het XBRL-schema van de NBB (gestandaardiseerd) — IFRS laat meer vrijheid in vormgeving, maar legt strengere informatieplicht over de gebruikte conventies.

---

## 📌 Verslagperiode

De jaarrekening wordt **minstens jaarlijks** opgesteld (IAS 1 §36). Wanneer een entiteit de verslagperiode wijzigt en de jaarrekening over een **langere of kortere periode** dan twaalf maanden wordt opgesteld, moet ze:

- de reden vermelden waarom een afwijkende periode wordt gebruikt
- vermelden dat de bedragen niet volledig vergelijkbaar zijn met de vorige periode

Vergelijkbaar met [[bronnen/wetteksten/XV-wvv#art-31|WVV art. 3:1]] (Belgisch boekjaar = twaalf maanden, behoudens uitzondering bij oprichting/wijziging).

---

## ⚖️ Kwalitatieve kenmerken

IAS 1 §15-46 (in samenhang met het IFRS Conceptual Framework) verlangt dat de jaarrekening:

- een **getrouw beeld** geeft (*fair presentation*) — vertaalt zich in: relevant, betrouwbaar, vergelijkbaar, begrijpelijk
- de continuïteitsveronderstelling expliciet beoordeelt — bij twijfel: motiveren in toelichting (zie [[continuiteitsrisico]])
- het **toerekeningsbeginsel** (*accrual basis*) toepast op alle overzichten behalve de kasstroomtabel
- **consistent** is in presentatie en classificatie van jaar tot jaar
- **materiële** posten apart presenteert en niet-materiële mag aggregeren
- **geen verrekening** tussen activa en passiva of tussen baten en lasten toepast (behoudens uitdrukkelijk toegestaan)
- **vergelijkende informatie** verstrekt over de voorgaande periode

Deze kenmerken zijn nagenoeg identiek aan de algemene beginselen in [[ifrs-rechtskader#-richtlijn-201334eu|Richtlijn 2013/34/EU art. 6]] en aan de [[boekhoudkundige-beginselen|Belgische boekhoudkundige beginselen]] — het verschil zit in de uitwerking en in de **substance over form**-doctrine die IFRS systematischer toepast dan Belgisch GAAP.

> [!info]- In de praktijk
>
> De IFRS-doctrine *substance over form* leidt tot andere resultaten dan Belgisch GAAP voor:
>
> - **Leasing**: economische realiteit (gebruik van het actief) prevaleert → recht-van-gebruik op de balans van de lessee — zie [[leasing-ifrs]]
> - **Verkoop met terugkoopbeding**: blijft op balans van de verkoper als de risico's niet zijn overgedragen
> - **Factoring**: enkel echte derecognition als de risico's zijn overgegaan
>
> Belgisch GAAP volgt veel vaker de **juridische vorm** — zoals duidelijk blijkt bij operationele leasing waarvan het actief niet op de balans staat van de huurder.
>
> 🤖 *AI-aanvulling*

---

## 📌 Balans (Statement of Financial Position)

IAS 1 §54 schrijft voor welke posten **minimaal** in de balans moeten verschijnen, maar laat vrijheid in volgorde en gedetailleerde indeling. De entiteit kiest een classificatie:

**Optie 1 — Vlottend / niet-vlottend** (*current / non-current* — meest gebruikt, default)
- Activa en passiva worden in twee groepen gesplitst op basis van een **realisatiehorizon van 12 maanden**
- *Niet-vlottende activa* eerst, dan *vlottende activa*; idem voor passiva

**Optie 2 — Liquiditeitsvolgorde** (*by liquidity*)
- Toegestaan wanneer dat een betrouwbaarder en relevanter overzicht geeft (typisch voor banken en verzekeraars)
- Activa en passiva van meest naar minst liquide

```
IFRS-balans (current / non-current, vereenvoudigd):

Niet-vlottende activa:
  Materiële vaste activa (IAS 16)
  Immateriële activa (IAS 38)
  Vastgoedbeleggingen (IAS 40)
  Investeringen verwerkt via vermogensmutatiemethode
  Financiële activa (lange termijn)
  Uitgestelde belastingvorderingen

Vlottende activa:
  Voorraden (IAS 2)
  Handels- en overige vorderingen
  Belastingvorderingen
  Financiële activa (korte termijn)
  Geldmiddelen en kasequivalenten

Eigen vermogen:
  Geplaatst kapitaal
  Reserves (incl. herwaarderingsreserve, andere OCI-reserves)
  Overgedragen resultaat
  Belang van derden (Non-controlling interests)

Niet-vlottende verplichtingen:
  Langlopende financiële schulden
  Voorzieningen op lange termijn
  Uitgestelde belastingverplichtingen

Vlottende verplichtingen:
  Kortlopende financiële schulden
  Handelsschulden
  Belastingverplichtingen
  Voorzieningen op korte termijn
```

**Belgisch GAAP-balans** kent geen current/non-current uitsplitsing als zodanig — de structuur is vast (rubrieken I-IX in vaste volgorde). Wel zijn de NBB-codes mappable op IFRS-classificaties — zie [[balansaggregaten]].

---

## 📌 Resultatenrekening (Statement of Profit or Loss and OCI)

De IFRS-resultatenrekening kent twee delen:

1. **Profit or Loss** — winst of verlies van de periode
2. **Other Comprehensive Income (OCI)** — niet via P&L gerealiseerde resultaatcomponenten:
   - Herwaarderingsreserve op MVA en immateriële activa (IAS 16 / IAS 38)
   - Niet-gerealiseerde resultaten op financiële activa *fair value through OCI* (IFRS 9)
   - Actuariële winsten/verliezen op personeelsvoordelen (IAS 19)
   - Wisselkoersverschillen op buitenlandse activiteiten (IAS 21)
   - Resultaten op kasstroomafdekkingsinstrumenten

De entiteit mag IAS 1 §99 toepassen op één van twee manieren voor de classificatie van kosten:

| Methode | Indeling van kosten |
|---|---|
| **By nature** | Naar aard: grondstoffen, personeelskosten, afschrijvingen, andere bedrijfskosten |
| **By function** | Naar functie: cost of sales, distribution, administration, R&D |

Belgisch GAAP-RR is altijd "by nature" — de NBB-rekeningen volgen de aard. Een IFRS-rapporterende vennootschap die "by function" kiest, moet wel aanvullende informatie geven over de aard van de kosten in de toelichting.

> [!warning]- OCI is geen winst die uitgekeerd kan worden
> ❌ *"Een IFRS-OCI-resultaat van €10M kan als dividend worden uitgekeerd."*
>
> OCI-componenten zijn niet-gerealiseerde resultaten. Ze gaan naar reserves binnen het eigen vermogen, niet naar de uitkeerbare winst. Sommige worden later "gerecycleerd" naar de P&L (bv. wisselkoersverschillen bij verkoop van een buitenlandse dochter), andere blijven definitief in reserve (bv. herwaarderingsreserve op MVA). Voor uitkering moet enerzijds de Belgische statutaire jaarrekening voldoende uitkeerbaar resultaat tonen — IFRS bepaalt het uitkeringsmaximum nooit.
>
> 🤖 *AI-aanvulling*

---

## 📌 Wijzigingen in het eigen vermogen

Het *Statement of Changes in Equity* (IAS 1 §106) toont per categorie eigen vermogen (kapitaal, reserves, overgedragen resultaat, OCI-componenten, belang van derden) de bewegingen tussen begin- en eindtoestand:

- Resultaat van het boekjaar (P&L + OCI)
- Kapitaalverhogingen, kapitaalverminderingen en eigen aandelen
- Dividenden
- Effect van wijzigingen in grondslagen (retroactief)

In Belgisch GAAP wordt deze informatie verspreid over de toelichting (rubriek "Staat van het kapitaal", "Mutaties van de reserves") — geen apart primair overzicht.

---

## 📌 Kasstroomtabel (IAS 7)

*Statement of Cash Flows*

IAS 7 verplicht een kasstroomtabel die de bewegingen van **geldmiddelen en kasequivalenten** opdeelt in drie categorieën:

| Categorie | Inhoud |
|---|---|
| **Operationele activiteiten** | Kasstromen uit de hoofdactiviteit: ontvangsten van klanten, betalingen aan leveranciers en personeel, betaalde belastingen |
| **Investeringsactiviteiten** | Aankoop/verkoop van vaste activa, deelnemingen, langetermijnbeleggingen |
| **Financieringsactiviteiten** | Kapitaalverhoging, uitgifte/aflossing van leningen, dividendbetalingen |

**Twee toegestane methodes** voor operationele kasstroom (IAS 7 §18):
- **Directe methode**: rechtstreekse opname van bruto kasontvangsten en -uitgaven (aanbevolen door IASB, maar zelden toegepast)
- **Indirecte methode**: vertrek vanuit nettoresultaat, gecorrigeerd voor niet-kasposten (afschrijvingen, voorzieningen, mutatie werkkapitaal) — meest gebruikte methode in praktijk

In Belgisch GAAP is een kasstroomtabel **geen verplicht onderdeel** van de jaarrekening, hoewel ze in het jaarverslag mag worden opgenomen en in de praktijk vaak via de toelichting wordt gepresenteerd. Voor analysedoeleinden wordt ze opgesteld via [[kasstroomanalyse]].

---

## 📌 Toelichting

IAS 1 §112-117 vereist dat de toelichting:

- de gebruikte **grondslagen voor financiële verslaglegging** (*accounting policies*) toelicht
- de **belangrijke oordeelsvormingen en schattingen** beschrijft (judgements en estimation uncertainty)
- voldoende informatie geeft om elke positie in de primaire overzichten te begrijpen
- aanvullende informatie verstrekt die de getrouwheid van het beeld bevordert

De omvang van een IFRS-toelichting is daardoor doorgaans **drie tot tien keer groter** dan de Belgische toelichting bij KB WVV-jaarrekeningen — dit is een van de meest opvallende verschillen voor de gebruiker.

---

## 📋 Eerste toepassing van IFRS (IFRS 1)

*First-time adoption of IFRS*

IFRS 1 regelt hoe een entiteit overstapt van een ander kader (bv. Belgisch GAAP) naar IFRS. De kern: bij eerste toepassing wordt een **opening IFRS-balans** opgesteld op de **transitiedatum** — dat is het begin van de vroegste vergelijkende periode in de eerste IFRS-jaarrekening.

Stappen voor eerste toepassing:

1. **Bepaal de transitiedatum** — als een entiteit voor boekjaar 2026 voor het eerst IFRS rapporteert en één jaar vergelijkende informatie geeft, is de transitiedatum 1 januari 2025
2. **Stel een IFRS-balans op transitiedatum op** — toepassing IFRS-grondslagen alsof die altijd van toepassing waren geweest
3. **Pas IFRS retroactief toe** voor alle posten — met enkele uitzonderingen (verplicht of optioneel) die IFRS 1 toelaat om de transitielast te verlichten
4. **Verwerk de aanpassingen rechtstreeks in eigen vermogen** op de transitiedatum (overgedragen resultaat of een specifieke transitiereserve)
5. **Reconciliatietabellen** opstellen tussen Belgisch GAAP en IFRS voor: eigen vermogen op transitiedatum, eigen vermogen op afsluitingsdatum vergelijkende periode, totaalresultaat vergelijkende periode

> [!info]- Concreet: KBC overgang
>
> Toen Belgische banken vanaf 2005 verplicht naar IFRS overstapten voor hun geconsolideerde rekeningen, was de transitiedatum 1 januari 2004. Op die datum werd een opening IFRS-balans opgesteld waarbij bv. financiële activa volgens IAS 39 (toen) werden geherclassificeerd, leasing volgens IAS 17 werd herbekeken, en goodwill niet meer werd afgeschreven maar getoetst op bijzondere waardevermindering. Het verschil met de bestaande Belgisch GAAP-balans werd via een transitiepost in het eigen vermogen geboekt.
>
> 🤖 *AI-aanvulling*

---

## ↔️ Afwijkingen ten opzichte van de Belgische wetgeving

Op niveau van presentatie zijn de belangrijkste afwijkingen tussen IFRS en Belgisch GAAP (KB WVV):

| Aspect | Belgisch GAAP | IFRS |
|---|---|---|
| **Bestanddelen** | Balans, resultatenrekening, toelichting | Balans, P&L+OCI, mutatieoverzicht EV, kasstroomtabel, toelichting |
| **Schema** | Vast schema (volledig/verkort/microschema), gecodeerd via NBB-rubrieken | Vrije presentatie binnen IAS 1 minimumvereisten |
| **Balansindeling** | Vaste indeling I-IX | Current/non-current of liquiditeitsvolgorde |
| **Kostenclassificatie RR** | Naar aard verplicht | By nature OF by function |
| **Kasstroomtabel** | Niet verplicht | Verplicht (IAS 7) |
| **Eigen vermogen mutatie** | Verspreid in toelichting | Apart primair overzicht |
| **OCI** | Bestaat niet als concept | Aparte sectie in resultatenrekening |
| **Toelichting** | Beperkt, gestandaardiseerd via XBRL | Uitgebreid, principle-based |
| **Vergelijkende periode** | Vorig boekjaar | Vorig boekjaar (3e balans bij retroactieve aanpassing) |
| **Herwaardering** | Optioneel, alleen MVA met duurzame meerwaarde | Optioneel voor MVA (IAS 16) en immateriële (IAS 38, beperkt) |

Voor specifieke posten zie:
- [[vaste-activa-ifrs]] — IAS 16 / IAS 38
- [[leasing-ifrs]] — IFRS 16
- [[opbrengsten-ifrs]] — IFRS 15
- [[voorraden-ifrs]] — IAS 2

---

## Relevant voor

**[[1.5-europese-wetgeving-en-internationale-normen|1.5 Europese wetgeving en internationale boekhoudkundige normen]]**

Taken:
- *Opstellen van de individuele en geconsolideerde jaarrekening*
  - Herstructureren van de balans en de resultatenrekening
  - Identificeren en interpreteren van de balansaggregaten
  - Berekenen van de elementen die nodig zijn voor een interpretatie van de kasstromen en die interpreteren

Kenniselementen:
- IV.A — Eerste toepassing van IFRS (IFRS 1)
- IV.B — IAS 1 De jaarrekening (1-9)
- IV.C — Afwijkingen ten opzichte van de Belgische wetgeving

### Voorbeeldvragen

> [!question]- Bestanddelen IFRS-jaarrekening
>
> Welke onderdelen behoren tot een complete IFRS-jaarrekening die niet verplicht zijn onder Belgisch GAAP?
>
> > [!success]- Antwoord
> >
> > **Twee bestanddelen.**
> >
> > 1. **Mutatieoverzicht eigen vermogen** (*Statement of Changes in Equity*) — onder Belgisch GAAP versnipperd over toelichtingsrubrieken; onder IFRS een apart primair overzicht.
> > 2. **Kasstroomtabel** (*Statement of Cash Flows*) volgens IAS 7 — onder Belgisch GAAP geen verplicht bestanddeel.
> >
> > Daarnaast bevat de IFRS-resultatenrekening een aparte **OCI-sectie** voor niet-gerealiseerde resultaten — een conceptueel verschil meer dan een nieuw bestanddeel.
> >
> > *Zie: [[presentatie-jaarrekening-ifrs#-bestanddelen-van-de-jaarrekening-ias-1|Bestanddelen]]*
>
> 🤖 *AI-aanvulling*

> [!question]- Stellingen over IAS/IFRS
>
> Welke stellingen over IAS/IFRS-presentatie zijn juist of fout?
>
> A. Degressieve afschrijvingen zijn toegestaan.
> B. Afschrijving op materiële vaste activa mag stopgezet worden wanneer de reële waarde van het actief groter is dan de boekwaarde.
> C. Uitzonderlijke opbrengsten (extraordinary items) mogen onder IFRS worden gepresenteerd.
>
> > [!success]- Antwoord
> >
> > **A juist · B fout · C fout.**
> >
> > **A juist** — IAS 16 §62 laat verschillende afschrijvingsmethodes toe (lineair, degressief, eenheid van productie), zolang ze het verbruikspatroon van de economische voordelen weerspiegelen. Onder Belgisch GAAP is degressieve afschrijving fiscaal beperkt; onder IFRS gaat het over economische realiteit. Zie [[vaste-activa-ifrs#-afschrijvingsmethode|Afschrijvingsmethode]].
> >
> > **B fout** — IAS 16 §55 bepaalt dat een actief blijft afgeschreven worden zelfs als de reële waarde groter is dan de boekwaarde. Afschrijving stopt enkel wanneer het actief is geclassificeerd als *held for sale* (IFRS 5) of wanneer de boekwaarde de restwaarde bereikt. Een impairment-test (IAS 36) is iets anders.
> >
> > **C fout** — Sinds de herziening van IAS 1 in 2003 zijn **extraordinary items** verboden. Posten worden geclassificeerd binnen P&L of OCI, met materialiteitsdiscipline en — indien nodig — apart vermeld in de toelichting.
> >
> > *Zie: [[presentatie-jaarrekening-ifrs#-resultatenrekening-statement-of-profit-or-loss-and-oci|Resultatenrekening]] · [[vaste-activa-ifrs]]*
>
> 📝 *Geïnspireerd door voorbeeldexamen 2024 (vraag 7C) — gedeeltelijk uit examen, aangevuld 🤖*
