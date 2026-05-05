---
tags: ["1.5", wip, materie]
niveau: integratie
status: draft
bouwversie: 2
bronnen:
  - IAS 18 (Revenue) — vervangen sinds 2018
  - IFRS 15 (Revenue from Contracts with Customers) — toepasbaar sinds 1 januari 2018
  - IAS 11 (Construction Contracts) — vervangen door IFRS 15
  - KB WVV 2019 art. 3:7, 3:11
---

# Opbrengsten onder IFRS

De opbrengsterkenning is sinds 2018 ingrijpend gewijzigd: **IAS 18** (verkoop van goederen, dienstprestaties, royalty's) en **IAS 11** (onderhanden bouwprojecten) zijn beide **vervangen door IFRS 15 — Revenue from Contracts with Customers**. IFRS 15 introduceert een uniform **5-stappenmodel** dat geldt voor alle opbrengsten uit contracten met klanten.

De ITAA-brochure verwijst naar IAS 18 (publicatiejaar 2022, kenniselement V.D). Voor het examen moet de student weten dat IAS 18 historisch is, en de logica van IFRS 15 begrijpen.

Voor het Belgische GAAP-equivalent zie [[bedrijfsresultaat-kosten-opbrengsten]] en [[boekhoudkundige-beginselen]].

---

## 📌 Definitie van opbrengsten

*Revenue*

**Opbrengsten** zijn de bruto instromen van economische voordelen tijdens de periode, voortvloeiend uit de **gewone activiteiten** van de entiteit, die het eigen vermogen verhogen zonder dat ze het gevolg zijn van een inbreng door eigenaars (IAS 18 §7, IFRS 15 §6).

Onderscheid:
- **Opbrengsten** = uit gewone activiteiten (verkoop, dienstverlening)
- **Winsten** (*gains*) = niet-gewone activiteiten (bv. verkoop van een gebouw bij stopzetting van een filiaal) — niet onder IFRS 15

**Niet-opbrengsten** (geïnde bedragen voor rekening van derden, bv. BTW, accijnzen): worden niet als opbrengst opgenomen — nettorapportering.

---

## 📋 Boeking van opbrengsten — 5-stappenmodel (IFRS 15)

IFRS 15 kent één uniform model dat in alle gevallen wordt toegepast:

### Stap 1: Identificeer het contract met de klant

Een contract bestaat onder IFRS 15 wanneer:
- Beide partijen instemmen
- De rechten en verplichtingen zijn identificeerbaar
- Er **commerciële substantie** is
- De vergoeding is bepaalbaar
- **Inning is waarschijnlijk**

### Stap 2: Identificeer de afzonderlijke prestatieverplichtingen

Een **prestatieverplichting** (*performance obligation*) is een belofte om een **te onderscheiden goed of dienst** te leveren. Een goed of dienst is "te onderscheiden" wanneer:
- De klant er voordeel uit haalt op zichzelf of in combinatie met andere beschikbare middelen
- De belofte afzonderlijk identificeerbaar is binnen het contract

> [!info]- Concreet: software + onderhoud
>
> Een softwareleverancier verkoopt een licentie voor €100.000 plus 3 jaar onderhoud voor €30.000. Onder IFRS 15: **twee afzonderlijke prestatieverplichtingen** — de licentie (eenmalig, op moment van levering) en het onderhoud (gespreid over 3 jaar). De €130.000 wordt verdeeld over beide volgens de relatieve standalone-prijzen.
>
> Onder IAS 18 (vóór 2018) gebeurde een vergelijkbare uitsplitsing, maar met andere terminologie en minder strenge criteria.
>
> 🤖 *AI-aanvulling*

### Stap 3: Bepaal de transactieprijs

De **transactieprijs** is het bedrag dat de entiteit verwacht te ontvangen in ruil voor de levering. Componenten:

- Vaste vergoeding
- **Variabele componenten** (kortingen, bonussen, gestaffelde prijzen) — opgenomen aan **verwachte waarde** of **meest waarschijnlijke waarde**, met **constraint**: enkel het bedrag dat zeer waarschijnlijk niet zal worden teruggedraaid mag worden opgenomen
- **Significant financieringscomponent** (bv. betaling > 12 maanden): aangepast naar contante waarde
- **Niet-contante vergoeding** (bv. ruilhandel): aan reële waarde
- **Vergoedingen aan klant** (bv. promotionele kortingen, slotting fees): in mindering, tenzij voor afzonderlijke prestatie van klant

### Stap 4: Verdeel de transactieprijs over de prestatieverplichtingen

Wanneer er meerdere prestatieverplichtingen zijn, wordt de transactieprijs verdeeld op basis van de **relatieve standalone-prijzen** (*standalone selling price*) van elk goed of elke dienst. Als de standalone-prijs niet observeerbaar is, wordt geschat (adjusted market assessment, expected cost plus margin, residual approach).

### Stap 5: Boek opbrengst wanneer (of naarmate) de prestatieverplichting is vervuld

**Twee modaliteiten**:

| Modaliteit | Opbrengst geboekt | Voorbeelden |
|---|---|---|
| **Op een tijdstip** *(point in time)* | Bij overdracht van controle | Verkoop van goederen aan klant, software-licentie eenmalig |
| **Naarmate de tijd verloopt** *(over time)* | Geleidelijk over de prestatieperiode | Dienstverlening, onderhoudscontracten, langlopende constructiecontracten |

**Over time** wordt toegepast wanneer **één** van de drie criteria vervuld is (IFRS 15 §35):
1. De klant ontvangt en gebruikt de voordelen tijdens de prestatie zelf (bv. schoonmaakdienst)
2. De prestatie creëert of verbetert een actief dat door de klant wordt gecontroleerd terwijl het wordt gecreëerd (bv. bouw op terrein van de klant)
3. De prestatie creëert geen actief met alternatief gebruik én er is een **enforceable right** op vergoeding voor het reeds afgewerkte deel

Voortgang wordt gemeten via een **input-methode** (kosten gemaakt vs. totaal verwachte kosten — vroegere "percentage-of-completion"-methode van IAS 11) of **output-methode** (afgeleverde eenheden, mijlpalen, surveys).

> [!info]- Concreet: bouwbedrijf met meerjarig contract
>
> Een aannemer bouwt een fabriek voor €10 miljoen. Bouwperiode: 3 jaar. Voorspelde totale kosten: €7 miljoen. In jaar 1 worden €2,1 miljoen kosten gemaakt.
>
> Onder IFRS 15 (criteria 2 — bouw op terrein klant, of criteria 3 — *enforceable right* indien klant moet betalen voor afgewerkt deel): **over time**.
>
> Voortgang via input-methode: 2,1 / 7,0 = **30%**.
> Op te nemen opbrengst jaar 1: 30% × €10M = **€3,0M**.
> Op te nemen kosten jaar 1: €2,1M.
> Marge jaar 1: €0,9M.
>
> Identieke logica als de oude IAS 11 percentage-of-completion-methode. Onder Belgisch GAAP wordt dit doorgaans verwerkt via KB WVV art. 3:48 (onderhanden werk) — meting aan vervaardigingsprijs, opbrengst gespreid via overlopende rekeningen of "geactiveerde kosten".
>
> 🤖 *AI-aanvulling*

---

## 📌 Verschil met IAS 18 (historisch)

IAS 18 (toegepast tot 2017) onderscheidde drie types opbrengsten met elk eigen criteria:

| Type | IAS 18-criteria |
|---|---|
| **Verkoop van goederen** | Risico's en voordelen overgedragen, geen voortgezette betrokkenheid bij beheer/eigendom, betrouwbare meting van opbrengst en kosten |
| **Dienstverlening** | Stage van voltooiing betrouwbaar meetbaar; opbrengst en kosten betrouwbaar meetbaar |
| **Royalty's, intresten, dividenden** | Specifieke regels (effectieve-rentemethode, recht op betaling) |

IFRS 15 vervangt deze drie modellen door één principe: **overdracht van controle** in plaats van overdracht van risico's en voordelen. In de meeste gevallen leidt dit tot dezelfde uitkomst, maar voor complexe contracten (multi-element arrangements, langlopende contracten, principal/agent) kan het tijdstip van opname verschillen.

---

## 📌 Onderhanden projecten (IAS 11 → IFRS 15)

IAS 11 (constructiecontracten) is per 2018 afgeschaft en geïntegreerd in IFRS 15. De methode blijft echter conceptueel hetzelfde:

- **Percentage-of-completion** wordt onder IFRS 15 hernoemd tot **input/output-methode** voor *over time* opbrengsterkenning
- **Voorspelde verlies**: zodra een totaal verlies op het contract wordt voorzien, moet dit **onmiddellijk** worden ten laste genomen — IAS 11 was hierin expliciet, IFRS 15 verwijst naar IAS 37 (voorzieningen voor verlieslatende contracten)

Onder Belgisch GAAP wordt onderhanden werk gewaardeerd aan **vervaardigingsprijs** (KB WVV art. 3:42 e.v.) tenzij gekozen wordt voor verwerking met progressieve winstopname — analoog aan percentage-of-completion. CBN-advies 2018/05 erkent beide methodes.

---

## 📌 Toelichtingsvereisten

IFRS 15 §110-129 vereist uitgebreide toelichting:

- **Disaggregatie van opbrengsten** in categorieën die de aard, het bedrag, het tijdstip en de onzekerheid weerspiegelen (bv. naar productlijn, geografische regio, type klant)
- **Saldo's** van contractuele activa en passiva, en wijzigingen daarin
- **Resterende prestatieverplichtingen** (*backlog*): bedrag dat aan toekomstige opbrengst zal worden toegerekend, met verwachte timing
- **Significant judgements**: wanneer is een prestatie vervuld, hoe is variabele vergoeding geschat

Onder Belgisch GAAP zijn de toelichtingsvereisten op opbrengsten **veel beperkter** — typisch alleen omzet per geografisch gebied of per activiteitsgroep voor grote vennootschappen (KB WVV-Boek 3 toelichting).

---

## ↔️ BE-GAAP vs. IFRS — opbrengsten

| Aspect | Belgisch GAAP | IFRS 15 |
|---|---|---|
| **Criterium** | Realisatie + zekerheid (voorzichtigheidsbeginsel) | **Overdracht van controle** |
| **Multi-element contracten** | Doorgaans als geheel verwerkt | Verplicht uitgesplitst in prestatieverplichtingen |
| **Variabele vergoeding** | Typisch pas erkend bij realisatie | Erkend op *expected value* of *most likely amount* met constraint |
| **Significant financieringscomponent** | Geen aparte regel | Verplichte verdiscontering bij > 12m |
| **Onderhanden werk** | Vervaardigingsprijs of progressieve winstopname (CBN 2018/05) | *Over time* met input/output-methode |
| **Onderhanden bouwcontract met verwacht verlies** | Voorziening voor verlieslatend contract | Idem — onmiddellijk ten laste |
| **Toelichting** | Beperkt | Zeer uitgebreid |

---

## Relevant voor

**[[1.5-europese-wetgeving-en-internationale-normen|1.5 Europese wetgeving en internationale boekhoudkundige normen]]**

Taken:
- *Opstellen van de individuele en geconsolideerde jaarrekening*
  - Een beginsel van boekhoudrecht of een wettelijke bepaling uit Belgische of Europese bron opzoeken, grondig analyseren en toepassen, met inachtneming van internationale normen

Kenniselementen:
- V.D — IAS 18 (vervangen door IFRS 15): definitie opbrengsten, boeking, toelichting
- V.E (deels) — IAS 11 (vervangen door IFRS 15): onderhanden projecten

### Voorbeeldvragen

> [!question]- Software + onderhoud — IFRS 15
>
> Een ERP-leverancier sluit een contract met een klant: software-licentie voor €600.000 (eenmalig, levering bij ondertekening) + jaarlijks onderhoud voor €100.000 gedurende 5 jaar. Hoe wordt de opbrengst onder IFRS 15 verwerkt?
>
> > [!success]- Antwoord
> >
> > **Twee prestatieverplichtingen, elk met eigen tijdstip van opname.**
> >
> > **Stap 1**: contract aanwezig (commerciële substantie, bepaalbare vergoeding, waarschijnlijke inning).
> >
> > **Stap 2**: identificatie van twee afzonderlijke prestatieverplichtingen — de software-licentie en het onderhoud zijn elk afzonderlijk te onderscheiden (de klant kan de licentie ook gebruiken zonder onderhoud).
> >
> > **Stap 3-4**: transactieprijs €1.100.000 (€600k + 5 × €100k), verdeeld op basis van standalone-prijzen — laten we aannemen €600k licentie en €500k onderhoud (samen €1.100k).
> >
> > **Stap 5**:
> > - Licentie: opbrengst geboekt **op tijdstip van levering** (= ondertekening) → €600k jaar 1
> > - Onderhoud: opbrengst geboekt **over time** lineair over 5 jaar → €100k per jaar
> >
> > Resultaat in jaar 1: €700k opbrengst. In jaar 2-5: €100k per jaar.
> >
> > Onder Belgisch GAAP zou hetzelfde resultaat ontstaan via overlopende rekeningen — €500k onderhoud verdeeld via *over te dragen opbrengsten* (rekening 493).
> >
> > *Zie: [[opbrengsten-ifrs#-boeking-van-opbrengsten--5-stappenmodel-ifrs-15|5-stappenmodel]]*
>
> 🤖 *AI-aanvulling*

> [!question]- Verlieslatend bouwcontract
>
> Een aannemer rapporteert eind jaar 1 voor een 3-jarig bouwcontract: contractprijs €5M, kosten gemaakt jaar 1 = €1,5M, totale verwachte kosten herzien naar €5,5M (was €4,5M bij start). Wat is de impact onder IFRS 15?
>
> > [!success]- Antwoord
> >
> > **Onmiddellijke verlieserkenning van het volledige verwachte verlies.**
> >
> > Verwacht totaalresultaat = €5M opbrengst − €5,5M kosten = **−€0,5M verlies**.
> >
> > Bij een verlieslatend contract verplicht IFRS 15 (via IAS 37) om het volledige verlies onmiddellijk in P&L te boeken — niet pas naarmate het ontstaat. Dus jaar 1: erkenning van het volledige verlies van €0,5M.
> >
> > Bovendien wordt de opbrengst nog steeds *over time* geboekt op basis van voortgang: voortgang = 1,5 / 5,5 = 27%, op te nemen opbrengst = 27% × €5M = €1,36M, kosten = €1,5M (effectief), netto-effect: −€0,14M door percentage-of-completion + extra voorziening om het totale voorspelde verlies van €0,5M onmiddellijk te dekken.
> >
> > Onder Belgisch GAAP zou een [[voorzieningen|voorziening voor verlieslatend contract]] worden gevormd voor het bedrag van het verwachte verlies. Het resultaatpatroon is conceptueel hetzelfde: verlies onmiddellijk, niet gespreid.
> >
> > *Zie: [[opbrengsten-ifrs#-onderhanden-projecten-ias-11--ifrs-15|Onderhanden projecten]]*
>
> 🤖 *AI-aanvulling*
