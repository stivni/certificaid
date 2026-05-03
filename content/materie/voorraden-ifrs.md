---
tags: ["1.5", wip, materie]
niveau: integratie
status: draft
bouwversie: 2
bronnen:
  - IAS 2 (Inventories)
  - IAS 11 (Construction Contracts) — vervangen door IFRS 15
  - IFRS 15 (vanaf 2018)
  - KB WVV 2019 art. 3:42 e.v.
---

# Voorraden onder IFRS

**IAS 2 — Inventories** regelt de waardering en boeking van voorraden onder IFRS. Onderhanden projecten in opdracht van derden, vroeger gedekt door **IAS 11**, vallen sinds 2018 onder **IFRS 15** (zie [[opbrengsten-ifrs#-onderhanden-projecten-ias-11--ifrs-15|Onderhanden projecten]]). De ITAA-brochure (april 2022) verwijst nog naar IAS 11; de student moet weten dat dit historisch is.

Voor het Belgische GAAP-equivalent zie [[vlottende-activa-waardering]].

---

## 📌 Voorraad

*Inventories*

Voorraden zijn activa (IAS 2 §6):
- aangehouden om te worden **verkocht** in de normale bedrijfsvoering (handelsgoederen, gereed product)
- in **productie** voor latere verkoop (onderhanden werk)
- aangehouden als **grondstoffen of hulpmaterialen** die in het productieproces worden verbruikt

---

## 📌 Waardering en boeking van voorraden

IAS 2 §9 schrijft voor: voorraden worden gewaardeerd aan **het laagste van**:

- **Kostprijs** (*cost*)
- **Netto realiseerbare waarde** (*net realisable value, NRV*) — geschatte verkoopprijs in normale bedrijfsvoering, min de geschatte kosten van voltooiing en de geschatte verkoopkosten

### Kostprijsbepaling

De **kostprijs** omvat (IAS 2 §10-22):

- Aankoopkosten (aankoopprijs + invoerrechten + niet-recupereerbare BTW + transport- en behandelkosten, na aftrek van handelskortingen)
- **Conversiekosten** voor producten in eigen productie:
  - Directe arbeid en directe materialen
  - **Vaste productieoverhead** toegerekend op basis van de **normale productiecapaciteit** — vaste overhead per eenheid stijgt niet bij ondercapaciteit
  - Variabele productieoverhead toegerekend per geproduceerde eenheid
- Andere kosten die nodig zijn om de voorraad in haar huidige locatie en staat te brengen

**Niet activeerbaar in de voorraadkostprijs** (rechtstreeks ten laste):
- Abnormale verspilling
- Opslagkosten (tenzij noodzakelijk in het productieproces)
- Administratieve overhead die niet bijdraagt aan productie
- Verkoopkosten

### Toegestane formules voor de toerekening van kostprijs

IAS 2 §23-27 bepaalt welke methodes mogen worden gebruikt:

| Methode | Toepassing |
|---|---|
| **Specifieke identificatie** | Verplicht voor goederen die niet onderling uitwisselbaar zijn (bv. unieke kunstwerken, op maat gebouwde machines) |
| **First-In-First-Out (FIFO)** | Voor onderling uitwisselbare voorraden: oudste aankopen eerst verkocht |
| **Gewogen gemiddelde** *(weighted average cost)* | Voor onderling uitwisselbare voorraden: gemiddelde herberekend bij elke aankoop of periodiek |

**Last-In-First-Out (LIFO)** is sinds 2005 **uitdrukkelijk verboden** onder IAS 2. Dit is een belangrijk verschil met US GAAP, waar LIFO wel is toegestaan om fiscale redenen.

> [!warning]- LIFO is verboden onder IFRS — niet onder Belgisch GAAP
> ❌ *"Onder IAS/IFRS zijn FIFO, LIFO, gewogen gemiddelde en individuele identificatie alle vier toegestaan."*
>
> IAS 2 schrapte de LIFO-optie in 2003 (toepasbaar vanaf 2005). Sindsdien zijn enkel **specifieke identificatie**, **FIFO** en **gewogen gemiddelde** toegestaan.
>
> Onder **Belgisch GAAP** ([[bronnen/wetteksten/XV-KB-wvv|KB WVV art. 3:42]]) zijn FIFO, gewogen gemiddelde, LIFO én individuele identificatie alle vier toegestaan. LIFO is daar legitiem, maar zelden gebruikt — bij stijgende prijzen geeft het de laagste winst (interessant fiscaal, oncomfortabel commercieel).
>
> 🤖 *AI-aanvulling op basis van IAS 2 §25*

> [!info]- Concreet: kies tussen FIFO en gewogen gemiddelde
>
> Een groothandelaar in computeronderdelen koopt in januari 1.000 chips à €50, in februari 1.000 chips à €60, en verkoopt in maart 1.500 chips. Welke kostprijs zit in de COGS?
>
> **FIFO**: 1.000 × €50 + 500 × €60 = €50.000 + €30.000 = **€80.000**.
> Resterende voorraad: 500 × €60 = **€30.000**.
>
> **Gewogen gemiddelde**: gemiddelde kostprijs = (1.000 × 50 + 1.000 × 60) / 2.000 = **€55**.
> COGS = 1.500 × €55 = **€82.500**.
> Resterende voorraad: 500 × €55 = **€27.500**.
>
> Bij stijgende prijzen geeft FIFO een hogere voorraad en lagere COGS dan gewogen gemiddelde. Bij dalende prijzen omgekeerd.
>
> 🤖 *AI-aanvulling*

### Netto realiseerbare waarde (NRV)

Wanneer:
- voorraden beschadigd, verouderd of slecht verkoopbaar zijn
- de verkoopprijs gedaald is
- de geraamde kosten van voltooiing of verkoop gestegen zijn

worden ze afgewaardeerd tot de NRV. De afwaardering wordt ten laste van de P&L geboekt, in de **periode van afwaardering**.

**Terugname**: wanneer de oorzaak verdwijnt en de NRV opnieuw stijgt, wordt de afwaardering teruggenomen — beperkt tot de oorspronkelijke kostprijs (IAS 2 §33). Onder Belgisch GAAP geldt eenzelfde principe via [[waardeverminderingen]].

---

## 📌 Onderhanden projecten (IAS 11 → IFRS 15)

IAS 11 regelde tot 2017 de **constructiecontracten** (gebouwen, schepen, complexe machines op bestelling). Sinds 2018 vallen deze onder **IFRS 15**:

- Voortgangsmeting via input/output-methode (oude *percentage-of-completion*)
- Verwacht verlies → onmiddellijk volledig ten laste (via IAS 37, voorzieningen)
- Opbrengst en kosten gespreid over de contractperiode wanneer **over time**-criteria voldaan

Volledige uitwerking: zie [[opbrengsten-ifrs#-onderhanden-projecten-ias-11--ifrs-15|Onderhanden projecten onder IFRS 15]].

In Belgisch GAAP wordt onderhanden werk gewaardeerd aan **vervaardigingsprijs** ([[bronnen/wetteksten/XV-KB-wvv|KB WVV art. 3:48]]). De entiteit **mag** kiezen voor opname met progressieve winstopname conform CBN-advies 2018/05 — vergelijkbaar met IFRS *over time*-erkenning.

---

## ↔️ BE-GAAP vs. IFRS — voorraden

| Aspect | Belgisch GAAP (KB WVV) | IFRS (IAS 2) |
|---|---|---|
| **Waardering** | Laagste van aanschaffingswaarde of marktwaarde | Laagste van kostprijs of NRV |
| **Toegestane methodes** | FIFO, LIFO, gewogen gemiddelde, individueel | FIFO, gewogen gemiddelde, individueel — **geen LIFO** |
| **Vaste overhead** | Mag (niet verplicht) opgenomen worden | Verplicht opgenomen op basis van normale capaciteit |
| **Onderhanden werk** | Vervaardigingsprijs of progressief (CBN 2018/05) | Verplicht *over time* indien criteria vervuld (IFRS 15) |
| **Terugname afwaardering** | Toegelaten | Toegelaten — geplafonneerd op oorspronkelijke kostprijs |

---

## Relevant voor

**[[1.5-europese-wetgeving-en-internationale-normen|1.5 Europese wetgeving en internationale boekhoudkundige normen]]**

Taken:
- *Opstellen van de individuele en geconsolideerde jaarrekening*
  - Een beginsel van boekhoudrecht of een wettelijke bepaling uit Belgische of Europese bron opzoeken, grondig analyseren en toepassen, met inachtneming van internationale normen

Kenniselementen:
- V.E — IAS 2 en IAS 11/IFRS 15: waardering en boeking voorraden, onderhanden projecten

### Voorbeeldvragen

> [!question]- Toegestane voorraadwaarderingsmethodes onder IAS/IFRS
>
> Welke methodes voor de toerekening van kostprijs zijn onder IAS/IFRS toegestaan?
>
> A. FIFO, LIFO, gewogen gemiddelde, individueel
> B. FIFO, gewogen gemiddelde, individueel
> C. LIFO, gewogen gemiddelde, individueel
> D. FIFO en gewogen gemiddelde
>
> > [!success]- Antwoord
> >
> > **B is correct.**
> >
> > IAS 2 §23-27 staat drie methodes toe:
> > - **Specifieke identificatie** (verplicht voor niet-uitwisselbare goederen)
> > - **FIFO**
> > - **Gewogen gemiddelde**
> >
> > **LIFO is sinds 2005 verboden** (IAS 2 schrapte de optie in 2003). Onder Belgisch GAAP is LIFO daarentegen wél toegestaan ([[bronnen/wetteksten/XV-KB-wvv|KB WVV art. 3:42]]) — een typisch verschilpunt tussen kaders.
> >
> > Optie D mist de specifieke identificatie, dus is onvolledig.
> >
> > *Zie: [[voorraden-ifrs#-waardering-en-boeking-van-voorraden|Toegestane formules]]*
>
> 📝 *Uit voorbeeldexamen 2024 (vraag 7A)*

> [!question]- Vaste overhead op productie onder ondercapaciteit
>
> Een fabrikant heeft een normale productiecapaciteit van 100.000 eenheden per jaar, maar produceerde slechts 70.000 eenheden in jaar X. De vaste productieoverhead bedraagt €1.000.000. Hoeveel vaste overhead per eenheid mag in de voorraadkostprijs worden opgenomen onder IAS 2?
>
> > [!success]- Antwoord
> >
> > **€10 per eenheid (op basis van normale capaciteit).**
> >
> > IAS 2 §13 bepaalt dat de vaste productieoverhead wordt toegerekend aan de geproduceerde eenheden op basis van de **normale capaciteit**. Daarmee:
> >
> > - Vaste overhead per eenheid = €1.000.000 / 100.000 = **€10**
> > - Totaal geactiveerd in voorraad: 70.000 × €10 = €700.000
> > - **Restant van €300.000** = ondercapaciteitskost → **direct ten laste** in P&L
> >
> > Onder Belgisch GAAP zou deze allocatie minder strikt zijn: de onderneming kan kiezen om de volledige vaste overhead aan de gereduceerde productie toe te rekenen (€1.000.000 / 70.000 = €14,29 per eenheid), of niet — beide methodes zijn aanvaardbaar mits consistent toegepast en toegelicht. IFRS dwingt dus tot een specifieke economische realiteit.
> >
> > *Zie: [[voorraden-ifrs#-waardering-en-boeking-van-voorraden|Conversiekosten]]*
>
> 🤖 *AI-aanvulling*
