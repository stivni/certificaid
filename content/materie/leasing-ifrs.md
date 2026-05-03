---
tags: ["1.5", wip, materie]
niveau: integratie
status: draft
bouwversie: 2
bronnen:
  - IAS 17 (Leases) — vervangen sinds 2019
  - IFRS 16 (Leases) — toepasbaar sinds 1 januari 2019
  - KB WVV 2019 art. 3:40-3:41
  - CBN-advies 2015/4
---

# Leasing onder IFRS

De leaseboekhouding heeft onder IFRS een ingrijpende verandering doorgemaakt. Tot 2018 gold **IAS 17** — een classificatiemodel dat sterk leek op het Belgische GAAP-model met financiële versus operationele leasing. Sinds **1 januari 2019** is **IFRS 16** van toepassing — het schrapt de onderscheid voor de **lessee** (huurder) en verplicht haar om bijna alle leases op de balans te brengen.

De ITAA-brochure verwijst expliciet naar IAS 17 (publicatiejaar 2022, kenniselement V.C). Voor het examen is het cruciaal om **beide standaarden** te kennen: IAS 17 (historisch en lessor-zijde) én IFRS 16 (huidige norm voor lessee).

Voor het Belgische GAAP-equivalent zie [[leasing-boekhoudkundig]].

---

## ↔️ Financiële vs. operationele leasing (IAS 17)

*Operating lease vs. Finance lease — historische standaard*

Onder IAS 17 (toegepast tot 2018) werd elke lease eerst geclassificeerd als financiële of operationele leasing. De classificatie bepaalde de boekhoudkundige verwerking.

**Classificatiecriterium**: een leasing is **financieel** wanneer de **risico's en voordelen** verbonden aan de eigendom **substantieel** zijn overgedragen aan de lessee. IAS 17 §10-11 lijstte indicatoren op:

1. Eigendom gaat over aan het einde van de leaseperiode
2. Lessee heeft een **bargain purchase option** (koopoptie tegen substantieel lagere prijs dan reële waarde)
3. Leaseperiode beslaat het **grootste deel** van de economische levensduur (typisch ≥ 75%)
4. Contante waarde van de leasebetalingen ≥ **substantieel alle** reële waarde van het actief (typisch ≥ 90%)
5. Het actief is zo gespecialiseerd dat enkel deze lessee het zonder substantiële wijziging kan gebruiken

Bij minstens één indicator: financiële leasing. Anders: operationele leasing.

> [!warning]- IAS 17-criteria zijn principle-based, geen harde drempels
> ❌ *"Een lease is financieel zodra de leaseperiode 75% van de levensduur bedraagt."*
>
> De percentages 75% / 90% zijn **indicaties** uit US GAAP-traditie, niet absolute IAS 17-drempels. IAS 17 is principle-based: de **substantie** van de overdracht van risico's en voordelen telt, niet een mechanische test. Een leaseperiode van 70% kan financieel zijn als andere indicatoren wijzen op overdracht van risico's. Onder Belgisch GAAP is het criterium daarentegen specifiek meetbaar: integrale wedersamenstelling van het kapitaal via de termijnen — zie [[leasing-boekhoudkundig#-financiële-leasing|Financiële leasing BE-GAAP]].
>
> 🤖 *AI-aanvulling*

---

## 📌 Boekhouding door lessee en lessor

### Onder IAS 17 (vóór 2019) — bestaat nog voor lessor

**Lessee bij financiële leasing**:
- Actief geboekt als materieel actief, gewaardeerd aan **laagste van**: reële waarde van het actief, of contante waarde van de leasebetalingen
- Tegenboeking als **financiële schuld** (verdeeld in kort/lang)
- Periodiek: afschrijving van het actief + interest op de schuld + aflossing van de schuld

**Lessee bij operationele leasing**:
- Geen actief, geen schuld
- **Periodieke leasebetalingen ten laste** van P&L (typisch op een **lineaire basis**)

**Lessor bij financiële leasing**:
- Actief afgevoerd, **vordering op de lessee** opgenomen aan netto-investering in de lease
- Periodiek: ontvangsten verdeeld in interest (resultatenrekening) en aflossing van de vordering
- IFRS 16 behield deze classificatie voor de **lessor-zijde** — IFRS 16 §61-97

**Lessor bij operationele leasing**:
- Actief blijft op de balans, wordt afgeschreven volgens IAS 16
- Periodieke leasebetalingen als **opbrengst** in P&L, lineair over de leaseperiode

### Onder IFRS 16 (vanaf 2019) — voor lessee

IFRS 16 schrapt het onderscheid voor de lessee. **Elke** lease (behalve enkele uitzonderingen) wordt op de balans gebracht volgens een **single recognition model**:

**Lessee — IFRS 16 §22-60**:

1. Bij ingang van de lease wordt een **recht-van-gebruik-actief** (*right-of-use asset*) opgenomen, gewaardeerd aan:
   - de aanvankelijke leaseschuld
   - plus eventuele initiële betalingen vóór ingangsdatum
   - plus initiële directe kosten
   - plus geschatte ontmantelingskosten
   - min eventuele incentives (bv. eerste-maand-gratis)

2. Tegenboeking: **leaseschuld** (*lease liability*) gewaardeerd aan contante waarde van de toekomstige leasebetalingen, verdisconteerd aan de impliciete rentevoet of — bij gebrek — aan de **incrementele leningsvoet** van de lessee

3. Periodiek:
   - Afschrijving van het recht-van-gebruik-actief volgens IAS 16 (typisch lineair over de leaseperiode)
   - **Interestlast** op de leaseschuld via de effectieve-rentemethode
   - Aflossing van de leaseschuld

```
IFRS 16-balans bij ingangsdatum kantoorhuur 5 jaar, €100.000/jaar:

Activa
  Right-of-use asset (kantoor)        +€430.000  (= contante waarde 5×100k @ 5%)

Verplichtingen
  Leaseschuld (kortlopend deel)       +€85.000
  Leaseschuld (langlopend deel)       +€345.000
                                       ────────
                                       +€430.000

Resultatenrekening jaar 1:
  Afschrijving right-of-use asset     -€86.000  (lineair 5j)
  Interestlast                        -€21.500  (5% van €430k)
                                       ────────
  Totale impact                       -€107.500
```

**Uitzonderingen IFRS 16**: een lessee mag de op-balans-verwerking **niet** toepassen voor:
- **Korte-termijnleases** (< 12 maanden, zonder koopoptie)
- **Leases van activa met geringe waarde** (< $5.000 nieuw — bv. laptop, klein kantoorbureau)

In dat geval: lineair ten laste over de leaseperiode (zoals IAS 17 operationeel).

> [!warning]- IFRS 16 verandert de balansstructuur ingrijpend voor lessees
> ❌ *"IFRS 16 heeft alleen impact op de toelichting, niet op de balans."*
>
> IFRS 16 brengt **alle** leases (op uitzonderingen na) op de balans van de lessee. Voor een onderneming met veel operationele leases (bv. retailer met gehuurde winkels, luchtvaartmaatschappij met geleasde vliegtuigen) kan dit het balanstotaal en de **schuldgraad** dramatisch verhogen — een operationele leaseverbintenis van €500M wordt €500M extra schuld én €500M extra activa.
>
> Dit beïnvloedt **financiële ratio's** (zie [[financiele-ratios]]):
> - Schuldgraad ↑
> - Solvabiliteitsratio (EV/TA) ↓
> - EBITDA ↑ (huurkost wordt afschrijving + interest, beide *under the line* van EBITDA)
> - ROCE wijzigt door grotere kapitaalbasis
>
> Voor analyse over een vergelijkende periode 2018→2019 moet de analist de bruisende impact corrigeren of expliciet bespreken.
>
> 🤖 *AI-aanvulling op basis van IFRS 16*

---

## 📌 Overdracht van de eigendom aan het einde van de leaseperiode

Wanneer de lease eindigt:

- **Geen overdracht** (lessee geeft het actief terug): IFRS 16 vereist dat het recht-van-gebruik-actief volledig is afgeschreven en de leaseschuld nul is op einddatum. Eventuele *make-good obligations* (herstel in oorspronkelijke staat) zijn al opgenomen in de initiële kostprijs.

- **Overdracht via een koopoptie** die de lessee zal uitoefenen (*reasonably certain*): de leaseperiode loopt door tot het einde van de **economische levensduur** van het actief in plaats van tot de contractuele einddatum. Bij uitoefening verandert er niets — het recht-van-gebruik wordt herclassificeerd als gewone MVA.

- **Lessor-zijde** onder IFRS 16: de classificatie in financiële vs. operationele leases blijft bestaan, met verwerking conform de oude IAS 17-regels.

---

## ↔️ BE-GAAP vs. IFRS — leasing

| Aspect | Belgisch GAAP (KB WVV) | IFRS 16 (lessee) |
|---|---|---|
| **Classificatie** | Financieel of operationeel | **Geen** classificatie — alle leases on-balance (uitzondering: < 12m of low value) |
| **Criterium financieel BE** | Integrale wedersamenstelling kapitaal via termijnen | n.v.t. |
| **Criterium IFRS** | n.v.t. | Recht om gebruik te controleren over een periode |
| **Operationele lease lessee** | Off-balance, periodieke huurkost | **On-balance** — recht-van-gebruik-actief + leaseschuld |
| **Resultatenrekening** | Huurkost lineair | Afschrijving + interest (front-loaded effect) |
| **EBITDA-impact** | Huurkost in EBITDA → lager | Afschrijving en interest onder EBITDA → hoger |
| **Initiële kostprijs** | Geen activatie niet-betaalde verplichtingen | Activatie van toekomstige verplichtingen incl. ontmanteling |
| **Lessor** | Boeking volgt het volledige BE-GAAP-classificatiemodel | Behoudt classificatie financieel/operationeel zoals IAS 17 |

In **Belgisch GAAP** kan dezelfde feitelijke situatie tot een totaal andere balanspresentatie leiden:
- **Financiële leasing**: lessee boekt actief én financiële schuld (zoals IFRS 16)
- **Operationele leasing**: niets op de balans van de lessee — enkel huur in resultatenrekening

Het verschil komt in beeld wanneer een ITAA-LEX-bedrijf zowel een Belgische statutaire jaarrekening als een IFRS-geconsolideerde rekening publiceert: dezelfde lease verschijnt anders in beide.

> [!info]- In de praktijk
>
> Een Belgische dochter van een beursgenoteerde groep huurt haar kantoor (operationeel onder BE-GAAP). In:
>
> - **Statutaire jaarrekening (BE-GAAP, NBB-neerlegging)**: enkel huurkost in P&L, geen recht-van-gebruik
> - **IFRS-consolidatie van de moedergroep**: recht-van-gebruik op balans, leaseschuld op balans
>
> Bij consolidatie worden dus **consolidatieboekingen** toegevoegd om de IFRS 16-effecten op te nemen — die staan niet in de statutaire boekhouding van de dochter zelf. Voor de consolidatie-accountant is dit standaard werk.
>
> 🤖 *AI-aanvulling*

---

## Relevant voor

**[[1.5-europese-wetgeving-en-internationale-normen|1.5 Europese wetgeving en internationale boekhoudkundige normen]]**

Taken:
- *Opstellen van de individuele en geconsolideerde jaarrekening*
  - Een beginsel van boekhoudrecht of een wettelijke bepaling uit Belgische of Europese bron opzoeken, grondig analyseren en toepassen, met inachtneming van internationale normen

Kenniselementen:
- V.C — IAS 17 / IFRS 16: financiële vs. operationele leasing, lessee/lessor, einde leaseperiode

### Voorbeeldvragen

> [!question]- Operationele vs. financiële leasing — IFRS-behandeling
>
> Een onderneming huurt een kantoor voor 10 jaar voor €120.000 per jaar. De huurovereenkomst eindigt zonder koopoptie. Hoe moet zij dit behandelen onder IAS 17 (vóór 2019) en onder IFRS 16 (vanaf 2019)?
>
> > [!success]- Antwoord
> >
> > **Twee fundamenteel verschillende behandelingen.**
> >
> > **Onder IAS 17**: classificatie als **operationele leasing** (geen koopoptie, geen overdracht eigendom, kantoor is geen specifiek gespecialiseerd actief) → **off-balance**. De huurkost van €120.000/jaar wordt lineair ten laste in de P&L. Geen actief, geen schuld.
> >
> > **Onder IFRS 16**: **geen classificatieoefening** — bij aanvang wordt een **right-of-use asset** opgenomen ter waarde van de contante waarde van de toekomstige huurbetalingen (bv. €920.000 bij 5% disconteringsvoet over 10 jaar), met als tegenboeking een **leaseschuld** voor hetzelfde bedrag. In de P&L verschijnt jaarlijks een afschrijving (typisch lineair, €92.000) plus een interestlast (afnemend). Het is dus niet meer "huur" in P&L, maar afschrijving + interest.
> >
> > Dit verklaart waarom EBITDA na de IFRS 16-overgang in 2019 voor veel ondernemingen kunstmatig steeg: de huur viel uit EBITDA en werd afschrijving + interest, beide onder EBITDA.
> >
> > *Zie: [[leasing-ifrs#-boekhouding-door-lessee-en-lessor|Boekhouding lessee en lessor]]*
>
> 📝 *Geïnspireerd door voorbeeldexamen 2024 (vraag 7D) — formulering aangevuld 🤖*

> [!question]- BE-GAAP vs. IFRS leasing — dezelfde vrachtwagen
>
> Een transportbedrijf least een vrachtwagen voor 5 jaar. De maandelijkse termijnen wedersamenstellen het volledige geïnvesteerde kapitaal van de lessor. Hoe wordt dit verwerkt in de Belgische statutaire jaarrekening en in de IFRS-geconsolideerde rekening van een hypothetische moedergroep?
>
> > [!success]- Antwoord
> >
> > **In beide kaders staat de vrachtwagen op de balans van de lessee — maar via een andere logica.**
> >
> > **Belgisch GAAP** ([[leasing-boekhoudkundig#-financiële-leasing|Financiële leasing BE-GAAP]]): de termijnen wedersamenstellen integraal het kapitaal → **financiële leasing**. Vrachtwagen wordt geactiveerd onder rubriek III.D, met tegenboeking financiële schuld. Termijnen worden gesplitst in interest (P&L) en aflossing.
> >
> > **IFRS 16**: de classificatieoefening wordt overgeslagen voor de lessee. Aangezien er een leaseovereenkomst is met een identificeerbaar actief, wordt automatisch een **right-of-use asset** geboekt met tegenboeking leaseschuld. Verwerking is identiek aan een BE-GAAP financiële leasing.
> >
> > Voor een operationele leasing (zoals huur kantoor) zou het verhaal verschillen — daar staat onder BE-GAAP niets op de balans, onder IFRS wél.
> >
> > *Zie: [[leasing-ifrs#-be-gaap-vs-ifrs|BE-GAAP vs. IFRS leasing]]*
>
> 🤖 *AI-aanvulling*
