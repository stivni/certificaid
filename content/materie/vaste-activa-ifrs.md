---
tags: ["1.5", wip, materie]
niveau: integratie
status: draft
bouwversie: 2
bronnen:
  - IAS 16 (Property, Plant and Equipment)
  - IAS 38 (Intangible Assets)
  - IAS 36 (Impairment of Assets)
  - KB WVV 2019 art. 3:32 e.v.
---

# Vaste activa onder IFRS

Onder IFRS regelt **IAS 16** de materiële vaste activa (*property, plant and equipment*) en **IAS 38** de immateriële activa (*intangible assets*). Beide standaarden bevatten gedeelde bepalingen voor opname, aanvankelijke waardering en afschrijving, maar verschillen op specifieke punten — vooral voor de behandeling van interne ontwikkeling en herwaardering.

Voor het Belgische GAAP-equivalent zie [[vaste-activa-waardering]] en [[afschrijvingen]].

---

## 📌 Gemeenschappelijke bepalingen voor materiële en immateriële activa

**Opnamevoorwaarden** (IAS 16 §7 en IAS 38 §21) — een actief wordt op de balans opgenomen wanneer:

1. Het **waarschijnlijk** is dat de toekomstige economische voordelen verbonden aan het actief naar de entiteit zullen toevloeien
2. De **kostprijs** van het actief **betrouwbaar** kan worden gemeten

**Aanvankelijke waardering** — beide standaarden waarderen de vaste activa initieel aan **kostprijs**, die omvat:

- Aankoopprijs (incl. niet-recupereerbare BTW en invoerrechten, na aftrek van handelskortingen)
- **Direct toerekenbare kosten** om het actief op zijn locatie en in zijn bedrijfsklare staat te brengen: voorbereiding terrein, transport, installatie, professionele honoraria, testen
- Geschatte **ontmantelingskosten** en herstel van het terrein, voor zover daarvoor een verplichting bestaat (IAS 16 §16)

Latere waardering: keuze tussen **kostprijsmodel** en **herwaarderingsmodel** — zie hieronder.

> [!info]- Concreet: aanvankelijke waardering machine
>
> Een productiebedrijf koopt een drukpers voor €500.000. Bijkomende kosten:
> - Transport: €15.000
> - Installatie en afregeling door leverancier: €25.000
> - Testreeks (ingebruikname): €10.000
> - Toekomstige verplichte ontmanteling, contant gemaakt: €20.000
>
> Initiële boekwaarde onder IAS 16: 500 + 15 + 25 + 10 + 20 = **€570.000**.
>
> Onder Belgisch GAAP zou de aanschaffingswaarde doorgaans 500 + 15 + 25 + 10 = €550.000 zijn — de ontmantelingsverplichting wordt traditioneel verwerkt via een [[voorzieningen|voorziening]] op het passief, niet via activatie. Het verschil is conceptueel: IFRS koppelt de toekomstige verplichting onmiddellijk aan het actief; Belgisch GAAP scheidt actief en voorziening.
>
> 🤖 *AI-aanvulling*

---

## 📌 Specifieke elementen immateriële activa (IAS 38)

IAS 38 stelt strengere voorwaarden voor de opname van immateriële activa dan IAS 16 voor materiële activa. Een immaterieel actief moet:

- **Identificeerbaar** zijn — te onderscheiden van goodwill, ofwel afsplitsbaar (verkoopbaar) ofwel voortvloeiend uit contractuele/wettelijke rechten
- **Gecontroleerd** worden door de entiteit (vermogen om de voordelen te beperken tot de entiteit)
- Toekomstige **economische voordelen** voortbrengen

**Intern gegenereerde immateriële activa** — IAS 38 §52-67:

| Fase | Belgisch GAAP (KB WVV) | IFRS (IAS 38) |
|---|---|---|
| **Onderzoek** *(research)* | Niet activeerbaar | **Niet activeerbaar** (§54) — direct ten laste |
| **Ontwikkeling** *(development)* | Activering toegestaan onder voorwaarden (KB WVV art. 3:34) | **Verplicht activeren** wanneer aan zes voorwaarden voldaan (§57): technische haalbaarheid, voornemen tot afwerking, vermogen om te gebruiken/verkopen, toekomstige economische voordelen aantoonbaar, beschikbaarheid middelen, betrouwbare meting kosten |

**Verboden activering** (IAS 38 §63 — niet erkend als immaterieel actief):
- Intern gegenereerde **goodwill**
- Intern gegenereerde **handelsmerken**, *publishing titles*, klantenlijsten
- **Opstart-, opleidings-, reclame- en promotiekosten**
- Verhuiskosten, herstructureringskosten

> [!warning]- Activeer ontwikkelingskosten verplicht onder IFRS — niet optioneel
> ❌ *"Onder IFRS mag je kiezen of je ontwikkelingskosten activeert of niet."*
>
> Onder IFRS is de activering **verplicht** zodra aan de zes voorwaarden van IAS 38 §57 is voldaan. De entiteit kan niet ervoor kiezen om die kosten ten laste te nemen. Onder Belgisch GAAP is activering een **optie**: KB WVV staat het toe wanneer de toekomstige rentabiliteit voldoende vaststaat, maar verplicht het niet.
>
> 🤖 *AI-aanvulling op basis van IAS 38 §57*

> [!warning]- Onderzoekskosten zijn nooit activeerbaar onder IFRS
> ❌ *"Een R&D-laboratorium kan al zijn onderzoeksuitgaven activeren als het project veelbelovend is."*
>
> IAS 38 maakt een hard onderscheid tussen onderzoek (zoeken naar nieuwe kennis, kennis evalueren, materialen testen) en ontwikkeling (concrete toepassing van de kennis in een product of proces). **Onderzoekskosten worden nooit geactiveerd**, ook niet wanneer het project later succesvol blijkt — IAS 38 §54 staat dat niet toe. Enkel ontwikkelingskosten ná de overgang naar de ontwikkelingsfase mogen geactiveerd worden, en dat onmiddellijk wanneer de voorwaarden vervuld zijn.
>
> 🤖 *AI-aanvulling*

---

## 📌 Gebruiksduur

*Useful life*

De **gebruiksduur** is de periode waarover de entiteit het actief verwacht te gebruiken, of het aantal eenheden dat de entiteit verwacht te produceren via het actief (IAS 16 §6, IAS 38 §8).

**Materiële activa** (IAS 16): hebben altijd een eindige gebruiksduur — terreinen vormen de uitzondering en worden niet afgeschreven (eindeloze gebruiksduur).

**Immateriële activa** (IAS 38) — twee categorieën:

| Categorie | Behandeling |
|---|---|
| **Eindige gebruiksduur** | Afschrijven over de gebruiksduur (§97-106) |
| **Onbepaalde gebruiksduur** | **Niet** afschrijven — jaarlijkse impairment-test verplicht (§107-110) |

**Goodwill** (geen aparte standaard, geregeld in IFRS 3 — bedrijfscombinaties): heeft altijd een **onbepaalde gebruiksduur** onder IFRS. Wordt **niet afgeschreven**, maar **jaarlijks getoetst op bijzondere waardevermindering** (impairment) volgens IAS 36.

> [!warning]- Goodwill wordt onder IFRS niet afgeschreven
> ❌ *"Goodwill wordt onder IFRS afgeschreven over 10 jaar zoals onder Belgisch GAAP."*
>
> Belgisch GAAP schrijft goodwill af (typisch over 5 of 10 jaar) — onder IFRS is dat **verboden** sinds IFRS 3 (2004). Goodwill blijft op de balans aan kostprijs, en jaarlijks (en bij indicatoren) wordt een impairment-test uitgevoerd. Wanneer de boekwaarde van de kasstroomgenererende eenheid de realiseerbare waarde overstijgt, wordt een waardevermindering geboekt — onomkeerbaar, ook als de waarde later herstelt.
>
> 🤖 *AI-aanvulling op basis van IFRS 3 / IAS 36*

---

## 📌 Afschrijvingsmethode

IAS 16 §60 en IAS 38 §97 schrijven voor dat de afschrijvingsmethode **het verwachte verbruikspatroon van de economische voordelen** weerspiegelt. Toegestane methodes:

- **Lineair** (*straight-line*) — meest gebruikt
- **Degressief** (*diminishing balance*) — toegestaan wanneer het verbruikspatroon afneemt
- **Eenheid van productie** (*units of production*) — toegestaan voor activa waar het verbruik gelinkt is aan output (mijnen, machines met meetbare output)

De methode moet **jaarlijks** worden herzien (zie verder). Onder Belgisch GAAP zijn dezelfde methodes toegestaan, maar de keuze wordt vaak gestuurd door fiscale optimalisatie (degressief in WIB92) eerder dan door economische realiteit. Onder IFRS prevaleert de economische realiteit.

> [!info]- Concreet: degressieve afschrijving onder IFRS
>
> Een rederij koopt een container voor €100.000 met een gebruiksduur van 5 jaar. De container wordt veel intensiever gebruikt in de eerste jaren (nieuw, betrouwbaar) dan op het einde (versleten, frequente reparaties). Een degressieve methode (bv. 2× lineair = 40% per jaar op de boekwaarde) weerspiegelt het verbruikspatroon beter dan lineair.
>
> Onder IAS 16 §60 is dat de juiste keuze. Onder Belgisch GAAP zou een onderneming meer geneigd zijn lineair toe te passen om consistent te blijven met de fiscale aangifte.
>
> 🤖 *AI-aanvulling*

---

## 📌 Restwaarde

*Residual value*

De **restwaarde** is het bedrag dat de entiteit verwacht te ontvangen bij desinvestering aan het einde van de gebruiksduur, na aftrek van de geschatte desinvesteringskosten (IAS 16 §6).

De **afschrijvingsbasis** is: kostprijs **min** restwaarde. Wanneer de restwaarde gelijk is aan of groter dan de boekwaarde, **stopt** de afschrijving — maar de impairment-test blijft van toepassing (IAS 16 §54-55).

> [!warning]- Reële waarde > boekwaarde stopt de afschrijving niet
> ❌ *"Als de marktwaarde van een gebouw boven de boekwaarde stijgt, mag je stoppen met afschrijven."*
>
> IAS 16 §55 stelt expliciet: zolang de boekwaarde van een actief boven de geschatte **restwaarde** ligt, blijft afschrijving doorlopen. De reële waarde of marktwaarde is niet relevant voor de stopzetting van afschrijving. Enkel wanneer de restwaarde wordt herzien en boven de boekwaarde uitkomt, of wanneer het actief geclassificeerd wordt als *held for sale* (IFRS 5), stopt de afschrijving. Een appreciatie van de reële waarde kan wel reden zijn om de afschrijvingsmethode of -periode te herzien.
>
> 🤖 *AI-aanvulling op basis van IAS 16 §55*

---

## 📌 Herziening van afschrijvingsperiode en -methode

*Reassessment*

IAS 16 §51 en §61 verplichten een **jaarlijkse herziening** van:

- De **gebruiksduur** — herzien wanneer initiële schatting niet meer accuraat is
- De **restwaarde** — herzien op basis van actuele marktverwachtingen
- De **afschrijvingsmethode** — herzien wanneer het verbruikspatroon van de economische voordelen significant wijzigt

Wijzigingen worden behandeld als **schattingswijzigingen** (IAS 8) — **prospectief** verwerkt over de resterende gebruiksduur. Geen retroactieve aanpassing.

Onder Belgisch GAAP is de herziening minder geformaliseerd — wijzigingen aan de afschrijvingsmethode worden vaak gemotiveerd via KB WVV art. 3:6 (consistentiebeginsel) en moeten in de toelichting worden vermeld als afwijking van de waarderingsregels.

---

## 📌 Herwaarderingsmodel

*Revaluation model*

IAS 16 §31 en IAS 38 §75 staan een **alternatief waarderingsmodel** toe na initiële opname:

- Het actief wordt aan **reële waarde** gewaardeerd, mits die betrouwbaar kan worden gemeten
- Herwaarderingen gebeuren met voldoende regelmaat zodat de boekwaarde niet materieel afwijkt van de reële waarde

**Behandeling van het verschil**:

- **Stijging** boven de oorspronkelijke kostprijs → via **OCI** geboekt op de **herwaarderingsreserve** in eigen vermogen (IAS 16 §39)
- **Daling** onder de oorspronkelijke kostprijs → eerst tegen de bestaande herwaarderingsreserve, daarna ten laste van P&L
- **Realisatie** (bij verkoop of stelselmatig over de gebruiksduur) → herwaarderingsreserve overgeboekt naar reserves of overgedragen resultaat (geen recycling naar P&L)

| Aspect | Belgisch GAAP | IFRS |
|---|---|---|
| **Toepassingsgebied** | Enkel materiële vaste activa met **duurzame** meerwaarde, niet voor terreinen die heffinggevoelig zijn | MVA (alle categorieën) en immateriële activa met **actieve markt** |
| **Frequentie** | Niet bepaald, in praktijk eenmalig of bij significante wijziging | Voldoende regelmatig om materiële afwijking te vermijden |
| **Selectie** | Per actief of per categorie | Per **categorie** (bv. alle gebouwen) — niet selectief |

Voor BE-GAAP zie [[herwaarderingsmeerwaarden]].

---

## 📌 Bijzondere waardevermindering (IAS 36)

*Impairment of Assets*

Wanneer aanwijzingen bestaan dat een actief in waarde is gedaald (interne of externe indicatoren), wordt een **impairment-test** uitgevoerd:

- **Realiseerbare waarde** = max(reële waarde min verkoopkosten ; bedrijfswaarde)
- **Bedrijfswaarde** (*value in use*) = contante waarde van toekomstige kasstromen die het actief genereert

Wanneer de boekwaarde de realiseerbare waarde overstijgt, wordt het verschil als **waardevermindering** ten laste genomen.

**Verplicht jaarlijks**, ongeacht indicatoren:
- Goodwill
- Immateriële activa met **onbepaalde** gebruiksduur
- Immateriële activa **nog niet in gebruik** (bv. afgewerkte ontwikkelingskosten waarvan de productie nog niet gestart is)

**Terugname van waardeverminderingen** (IAS 36 §117):
- **Toegelaten** voor MVA en immateriële activa wanneer de oorzaak verdwenen is — beperkt tot de boekwaarde die zou hebben bestaan zonder waardevermindering
- **Verboden** voor goodwill — onomkeerbaar

In Belgisch GAAP is een [[waardeverminderingen|waardevermindering]] eveneens verplicht maar de meting verloopt via een eenvoudiger criterium (duurzame minderwaarde) en wordt minder systematisch jaarlijks getoetst.

---

## ↔️ BE-GAAP vs. IFRS — vaste activa

Samenvatting van de belangrijkste afwijkingen:

| Aspect | Belgisch GAAP | IFRS |
|---|---|---|
| **Initiële kostprijs ontmanteling** | Activeren niet vereist; voorziening op passief | Verplicht activeren in kostprijs (IAS 16 §16c) |
| **Onderzoek** | Niet activeerbaar | Niet activeerbaar |
| **Ontwikkeling** | Activering optioneel | Activering **verplicht** bij voldoen voorwaarden (IAS 38 §57) |
| **Goodwill** | Afgeschreven, typisch 5-10j | **Niet** afgeschreven, jaarlijkse impairment |
| **Herwaardering MVA** | Toegelaten voor duurzame meerwaarde | Toegelaten — keuze model per categorie |
| **Herwaardering immaterieel** | Verboden | Toegelaten alleen bij actieve markt — zeldzaam |
| **Onbepaalde gebruiksduur immaterieel** | Bestaat niet | Mogelijk — geen afschrijving, jaarlijkse impairment |
| **Restwaarde** | Soms verwaarloosd | Verplicht jaarlijks herzien |
| **Afschrijvingsmethode** | Vaak gestuurd door fiscaliteit (WIB92) | Verbruikspatroon — herziening jaarlijks |
| **Terugname waardevermindering MVA** | Toegelaten bij verdwijnen oorzaak | Toegelaten — geplafonneerd op oorspronkelijke afschrijvingscurve |
| **Terugname waardevermindering goodwill** | Toegelaten in BE-GAAP (zeldzaam) | **Verboden** |

---

## Relevant voor

**[[1.5-europese-wetgeving-en-internationale-normen|1.5 Europese wetgeving en internationale boekhoudkundige normen]]**

Taken:
- *Opstellen van de individuele en geconsolideerde jaarrekening*
  - Een beginsel van boekhoudrecht of een wettelijke bepaling uit Belgische of Europese bron opzoeken, grondig analyseren en toepassen, met inachtneming van internationale normen

Kenniselementen:
- V.A — IAS 16 en IAS 38: gemeenschappelijke bepalingen, immateriële activa-specifiek
- V.B — Afschrijvingen volgens de normen (gebruiksduur, methode, restwaarde, herziening)

### Voorbeeldvragen

> [!question]- Ontwikkelingskosten activeren onder IFRS
>
> Een softwareontwikkelaar besteedt €2 miljoen aan een nieuw cloud-platform. Ze kunnen aantonen dat de technische haalbaarheid bewezen is, dat ze het platform commercialiseren, en dat de kosten betrouwbaar gemeten zijn. Mag/moet het bedrag geactiveerd worden?
>
> > [!success]- Antwoord
> >
> > **Onder IFRS: verplicht activeren. Onder Belgisch GAAP: optioneel.**
> >
> > IAS 38 §57 vereist activering zodra aan de zes ontwikkelingskosten-voorwaarden is voldaan: technische haalbaarheid, voornemen tot afwerking, vermogen om te gebruiken of verkopen, aantoonbare toekomstige economische voordelen, beschikbaarheid van middelen, en betrouwbare meting van de kosten. Dit is geen keuze.
> >
> > Onder Belgisch GAAP (KB WVV art. 3:34) is activering toegelaten maar niet verplicht — de onderneming mag de kosten ook ten laste nemen. Veel KMO's kiezen voor onmiddellijke kostneming wegens fiscale eenvoud.
> >
> > *Zie: [[vaste-activa-ifrs#-specifieke-elementen-immateriële-activa-ias-38|Immateriële activa]]*
>
> 🤖 *AI-aanvulling*

> [!question]- Restwaarde groter dan boekwaarde
>
> Een onderneming herziet de restwaarde van een gebouw. De nieuwe geschatte restwaarde overstijgt de huidige boekwaarde. Wat zijn de gevolgen onder IAS 16?
>
> > [!success]- Antwoord
> >
> > **Afschrijving wordt stopgezet zolang de restwaarde boven de boekwaarde blijft.**
> >
> > IAS 16 §54 bepaalt dat de afschrijvingsbasis = boekwaarde min restwaarde. Wanneer de restwaarde de boekwaarde overstijgt, is de afschrijvingsbasis nul, en wordt geen afschrijving meer geboekt. De impairment-test blijft echter van toepassing — als de realiseerbare waarde later daalt onder de boekwaarde, wordt een waardevermindering geboekt.
> >
> > *Zie: [[vaste-activa-ifrs#-restwaarde|Restwaarde]]*
>
> 🤖 *AI-aanvulling*
