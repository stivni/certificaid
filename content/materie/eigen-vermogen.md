---
tags: ["1.1", wip, materie]
niveau: integratie
status: draft
bouwversie: 2
bronnen:
  - WVV art. 5:1, 5:142, 5:143, 5:145, 5:148
  - WVV art. 7:211, 7:212, 7:215, 7:217
  - KB WVV art. 3:54 (definitie rubrieken passief)
  - CBN-advies 121/3 (mutaties eigen vermogen)
  - CBN-advies 2019/14 (BV: kapitaalloos)
---

# Eigen vermogen

Het eigen vermogen is het deel van het passief dat toebehoort aan de aandeelhouders of vennoten: de middelen die zij hebben ingebracht, verhoogd met de winsten die in de onderneming zijn gebleven. Het heeft geen terugbetalingsverplichting (tenzij bij liquidatie of dividendbeslissing) en vormt daarmee de financiële buffer van de vennootschap.

In het NBB-schema beslaat het eigen vermogen de [[balansaggregaten#passivazijde-volgorde-toenemende-eisbaarheid|rubrieken 10 tot en met 15]] van het passief. De samenstelling verschilt naargelang de vennootschapsvorm.

---

## 📌 Eigen vermogen

*Nettoactief, aandeelhouderswaarde*

Het eigen vermogen is de som van wat de aandeelhouders in de onderneming hebben gestoken (inbreng of kapitaal) en wat de onderneming in de loop van haar bestaan heeft opgebouwd of ontvangen (reserves, overgedragen winst, herwaarderingsmeerwaarden, kapitaalsubsidies), na aftrek van eventuele overgedragen verliezen.

Samenstelling (volledig schema NBB, rubriek 10/15):

```
I.   Inbreng (BV/CV) of Kapitaal (NV)               rubriek 10/11
     A. Geplaatst kapitaal / Inbreng (beschikbaar)   100 / 110
     B. Niet-opgevraagd kapitaal / inbreng            101 / onbeschikbaar
II.  Uitgiftepremies                                  11 (NV) / 110 (BV)
III. Herwaarderingsmeerwaarden                        12 (NV) / eigen rubriek
IV.  Reserves                                         13
     A. Wettelijke reserve                            130
     B. Onbeschikbare reserves                        131
     C. Belastingvrije reserves                       132
     D. Beschikbare reserves                          133
V.   Overgedragen winst (+) of verlies (-)            14
VI.  Kapitaalsubsidies                                15
```

> [!info]- In de praktijk
>
> Een NV wordt opgericht met € 200.000 geplaatst kapitaal, waarvan € 150.000 is volgestort. In jaar 1 maakt ze € 30.000 nettowinst, waarvan € 1.500 naar de wettelijke reserve gaat en € 28.500 wordt overgedragen. Het eigen vermogen op balansdatum:
>
> ```
> Geplaatst kapitaal          200.000
> Niet-opgevraagd kapitaal    −50.000
> ─────────────────────────────────────
> Gestort kapitaal            150.000
> Wettelijke reserve            1.500
> Overgedragen winst           28.500
> ─────────────────────────────────────
> Totaal eigen vermogen       180.000
> ```
>
> 🤖 *AI-aanvulling*

---

## 📌 Inbreng (BV en CV) en kapitaal (NV)

Vóór de inwerkingtreding van het WVV (1 mei 2019) hadden alle vennootschappen een maatschappelijk kapitaal. Het WVV heeft dat concept afgeschaft voor de besloten vennootschap (BV) en de coöperatieve vennootschap (CV) ([[bronnen/wetteksten/XV-wvv#art-51|ITAA-LEX XV · WVV art. 5:1]]). De naamloze vennootschap (NV) behoudt het kapitaalbegrip.

| | BV / CV | NV |
|---|---|---|
| Juridisch begrip | Inbreng (geen kapitaal) | Kapitaal |
| Minimumvereiste | Geen wettelijk minimumkapitaal | € 61.500 volgestort (⚠️ te verifiëren via cijferzakboekje voor huidig bedrag) |
| MAR-rekening | 11 *Inbreng buiten kapitaal* | 100 *Geplaatst kapitaal* |
| Wettelijke reserve | Niet wettelijk verplicht | Verplicht (art. 7:211 WVV) |
| Uitkeringstest | Nettoactief- + liquiditeitstest (dubbele test) | Netto-actieftest |

**Inbreng bij BV**: de bedongen waarde van alle door de aandeelhouders toegezegde inbrengen in geld of in natura, voor zover niet teruggestort ([[bronnen/wetteksten/XV-KB-wvv#art-354|ITAA-LEX XV (KB) · KB WVV art. 3:54, §2, 2°]]). Inbreng kan beschikbaar (rekening 110) of statutair onbeschikbaar (rekening 111) zijn.

**Inbreng bij NV**: het geplaatst kapitaal omvat de inbreng vanwege de aandeelhouders, de eventueel geïncorporeerde uitgiftepremies en geïncorporeerde reserves of herwaarderingsmeerwaarden ([[bronnen/wetteksten/XV-KB-wvv#art-354|ITAA-LEX XV (KB) · KB WVV art. 3:54, §2, 1°]]).

> [!warning]- BV heeft geen "kapitaal" — gebruik de term "inbreng"
> ❌ *"De BV heeft een maatschappelijk kapitaal van € 18.550."*
>
> Een BV heeft geen kapitaal. Het WVV heeft het kapitaalbegrip voor de BV afgeschaft. De correcte term is "inbreng". In de jaarrekening verschijnt rubriek I als "Inbreng" (niet "Kapitaal"). De NV en SE behouden wél het kapitaalbegrip.
>
> ([[bronnen/wetteksten/XV-wvv#art-51|WVV art. 5:1]]; CBN-advies 2019/14)
>
> 🤖 *AI-aanvulling*

---

## 📌 Geplaatst kapitaal en niet-opgevraagd kapitaal (NV)

Bij de NV onderscheidt het WVV:

- **Geplaatst kapitaal** (rubriek I.A, rekening 100): het totale bedrag waartoe de aandeelhouders zich hebben verbonden bij oprichting of kapitaalverhoging — ook al is het nog niet volgestort.
- **Niet-opgevraagd kapitaal** (rubriek I.B, rekening 101): het deel van het geplaatst kapitaal dat de aandeelhouders nog niet hebben gestort omdat het bestuursorgaan het nog niet heeft opgevraagd. Dit bedrag staat in mindering op het geplaatst kapitaal.

Het saldo (geplaatst kapitaal minus niet-opgevraagd kapitaal) is het **werkelijk volgestorte** deel. Aandeelhouders die hun inbreng nog niet volledig hebben volgestort, worden vermeld in de toelichting bij de jaarrekening ([[bronnen/wetteksten/XV-KB-wvv#art-354|KB WVV art. 3:54, §1]]).

> [!info]- In de praktijk
>
> Een NV wordt opgericht. Aandeelhouder A en B verbinden zich elk € 50.000 in te brengen (= geplaatst kapitaal € 100.000). Bij oprichting wordt slechts 25% opgevraagd (€ 25.000). Boeking:
>
> ```
> Oprichting:
> 416  Opgevraagd, niet gestort kapitaal    25.000
> 101  Niet-opgevraagd kapitaal             75.000
>         aan 100  Geplaatst kapitaal                  100.000
>
> Storting door aandeelhouders:
> 550  Bank                                25.000
>         aan 416  Opgevraagd, niet gestort kapitaal    25.000
> ```
>
> Balanspost na storting:
> ```
> I.A Geplaatst kapitaal      100.000
> I.B Niet-opgevraagd kapitaal −75.000
> ─────────────────────────────────────
> Gestort kapitaal             25.000
> ```
>
> 🤖 *AI-aanvulling*

---

## 📌 Onbeschikbare eigen vermogensrekening (BV/CV)

Bij de omvorming van een BVBA naar BV (vanaf 1 januari 2020) werden het gestort kapitaal en de wettelijke reserve **van rechtswege** omgezet in een statutair onbeschikbare eigen vermogensrekening (rekening 1119 *Andere onbeschikbare inbreng buiten kapitaal*) ([[bronnen/wetteksten/XV-wvv#art-51|WVV art. 5:1]]; CBN-advies 2019/14).

Deze onbeschikbare rekening kan later **beschikbaar** worden gesteld via een statutenwijziging. Ze mag dan worden uitgekeerd aan de aandeelhouders, mits de uitkeringstests zijn voldaan.

---

## 📌 Uitgiftepremies (rubriek II)

*Share premium, agio*

Een uitgiftepremie is het bedrag dat boven de fractiewaarde of boekhoudkundige pariteitswaarde van een aandeel wordt betaald bij de uitgifte van nieuwe aandelen. Ze vergoedt de bestaande aandeelhouders voor de waardedilutie die optreedt bij de uitgifte van nieuwe aandelen (CBN-advies 121/3).

Bij een **NV**: rubriek II, rekening 11 (beschikbaar of onbeschikbaar naargelang de statuten).
Bij een **BV**: onderdeel van rubriek I *Inbreng buiten kapitaal*, rekening 1100 (beschikbaar) of 1110 (onbeschikbaar) ([[bronnen/wetteksten/XV-KB-wvv#art-354|KB WVV art. 3:54]]; CBN-advies 2019/14).

Uitgiftepremies mogen worden geïncorporeerd in het kapitaal of de inbreng, of worden uitgekeerd als ze beschikbaar zijn.

---

## 📌 Herwaarderingsmeerwaarden (rubriek III)

De [[herwaarderingsmeerwaarden|herwaarderingsmeerwaarden]] zijn de boekhoudkundige uitdrukking van een vaststaande en duurzame waardestijging van materiële of financiële vaste activa. Ze worden niet via de resultatenrekening geboekt maar rechtstreeks in het eigen vermogen opgenomen ([[bronnen/wetteksten/XV-KB-wvv#art-335|KB WVV art. 3:35]]).

Volledige uitleg, voorwaarden en beperkingen: zie [[herwaarderingsmeerwaarden]].

**Belangrijk voor uitkeringen**: het niet-afgeschreven gedeelte van een herwaarderingsmeerwaarde geldt als **onbeschikbaar eigen vermogen**. Een uitkering die het nettoactief doet dalen tot onder dat bedrag is verboden — voor zowel BV ([[bronnen/wetteksten/XV-wvv#art-5142|WVV art. 5:142]]) als NV ([[bronnen/wetteksten/XV-wvv#art-7212|WVV art. 7:212]]).

---

## 📌 Reserves (rubriek IV)

Reserves zijn winsten die vroegere algemene vergaderingen hebben besloten niet uit te keren maar in de vennootschap te houden. Ze versterken het eigen vermogen en zijn (deels) beschikbaar voor uitkering in latere jaren.

Het KB WVV onderscheidt vier soorten ([[bronnen/wetteksten/XV-KB-wvv#art-354|KB WVV art. 3:54, §2]]):

### Wettelijke reserve (rubriek IV.A, rekening 130)

Verplicht bij de NV: jaarlijks wordt 5% van de nettowinst aan de wettelijke reserve toegevoegd, totdat die reserve 10% van het geplaatst kapitaal bedraagt ([[bronnen/wetteksten/XV-wvv#art-7211|WVV art. 7:211]]). De wettelijke reserve is onbeschikbaar — ze kan niet worden uitgekeerd aan de aandeelhouders.

Bij de BV bestaat geen wettelijk verplichte reserve. De wettelijke reserve van een voormalige BVBA werd bij de WVV-overgang omgezet in een onbeschikbare inbreng (CBN-advies 2019/14).

### Onbeschikbare reserves (rubriek IV.B, rekening 131)

Reserves die krachtens de wet of de statuten niet uitkeerbaar zijn. Drie categorieën ([[bronnen/wetteksten/XV-KB-wvv#art-354|KB WVV art. 3:54, §2]]):

- **Reserve voor eigen aandelen** (rekening 1312): verplicht aan te leggen zolang eigen aandelen op de balans staan — zie [[#-eigen-aandelen-rubriek-12-bij-nv-onbeschikbare-reserve|Eigen aandelen]].
- **Reserve voor financiële steunverlening** (rekening 1313): vereist wanneer de vennootschap financiële steun verleent voor de verkrijging van haar eigen aandelen.
- **Statutair onbeschikbare reserves** (rekening 1311): reserves die de statuten onbeschikbaar verklaren. Bij de voormalige BVBA: de geïncorporeerde kapitaal- en reservebestanddelen na WVV-overgang.

### Belastingvrije reserves (rubriek IV.C, rekening 132)

Reserves waarvan de belastingvrijstelling of het belastinguitstel afhankelijk is van het behoud in het vermogen van de vennootschap. Typische gevallen: gespreide belasting van meerwaarden op vaste activa, investeringsreserve ([[bronnen/wetteksten/XV-KB-wvv#art-354|KB WVV art. 3:54, §2]]). De betrokken bedragen omvatten de meerwaarden of winsten **na aftrek van de ermee samenhangende uitgestelde belastingen** (uitgestelde belasting staat in rubriek VII.B).

Mutaties in belastingvrije reserves verlopen via de **resultatenrekening** — geen rechtstreekse balansboekingen (CBN-advies 121/3; [[resultaatverwerking]]).

### Beschikbare reserves (rubriek IV.D, rekening 133)

Vrij uitkeerbare reserves — wat overblijft nadat de wet, de statuten en de uitkeringstests zijn voldaan.

---

## 📌 Overgedragen winst of verlies (rubriek V, rekening 14)

Het saldo van winsten en verliezen die de algemene vergadering niet heeft uitgekeerd, niet aan een reserve heeft toegevoegd, en niet heeft ingezet voor verliesaanzuivering. Bij een positief saldo: overgedragen winst; bij negatief saldo: overgedragen verlies (rubriek V). De verwerking gebeurt jaarlijks via de [[resultaatverwerking]].

---

## 📌 Kapitaalsubsidies (rubriek VI, rekening 15)

Kapitaalsubsidies zijn subsidies van de overheid voor investeringen in vaste activa. Ze worden niet als opbrengst geboekt op het moment van ontvangst, maar opgenomen in het eigen vermogen — **na aftrek van de ermee samenhangende uitgestelde belastingen** ([[bronnen/wetteksten/XV-KB-wvv#art-354|KB WVV art. 3:54, §2]]).

Ze worden **geleidelijk afgeboekt** via overboeking naar rubriek IV.C *Andere financiële opbrengsten*, evenredig met de afschrijvingen op de gesubsidieerde vaste activa ([[bronnen/wetteksten/XV-KB-wvv#art-354|KB WVV art. 3:54, §2]]). Bij realisatie of buitengebruikstelling van het actief vóór einde afschrijving: volledig resterende saldo vrijvalt.

> [!info]- In de praktijk
>
> Een vennootschap ontvangt een subsidie van € 50.000 voor een machine met een aanschaffingswaarde van € 200.000 en een levensduur van 5 jaar. De machine wordt lineair afgeschreven: € 40.000/jaar. De subsidie wordt evenredig met de afschrijvingen afgeboekt: € 10.000/jaar (= 50.000 / 5).
>
> **Ontvangst subsidie:**
> ```
> 550  Bank                                 50.000
>         aan 150  Ontvangen subsidies                  50.000
> ```
> (Uitgestelde belasting apart geboekt — rubriek VII.B — niet weergegeven in dit voorbeeld)
>
> **Jaarlijkse afboeking (overeenkomstig afschrijving):**
> ```
> 150  Kapitaalsubsidies                   10.000
>         aan 753  Onttrekking aan kapitaalsubsidies    10.000
> ```
>
> Na 5 jaar is de subsidie volledig afgeboekt en is rekening 150 nul.
>
> 🤖 *AI-aanvulling*

> [!warning]- Kapitaalsubsidies gaan niet onmiddellijk naar de resultatenrekening
> ❌ *"Een subsidie voor de aankoop van een machine wordt bij ontvangst volledig als opbrengst geboekt."*
>
> Een kapitaalsubsidie die verband houdt met een investering in een vast actief wordt geboekt in het **eigen vermogen** (rubriek 15), niet als opbrengst. Ze vloeit pas geleidelijk naar de resultatenrekening via "Onttrekking aan kapitaalsubsidies" (rekening 753), in hetzelfde ritme als de afschrijvingen op het gesubsidieerde actief.
>
> Uitzondering: subsidies die **niet** afhangen van een investering in een vast actief, worden wél meteen als opbrengst geboekt (onder D. Andere bedrijfsopbrengsten of IV.C Andere financiële opbrengsten).
>
> ([[bronnen/wetteksten/XV-KB-wvv#art-354|KB WVV art. 3:54, §2]])
>
> 🤖 *AI-aanvulling*

---

## ⚖️ WVV-overgang: van kapitaal naar inbreng

Vóór 2019 hadden alle Belgische handelsvennootschappen een maatschappelijk kapitaal — een vaste, onaantastbare buffer die schuldeisers beschermde. Het WVV (23 maart 2019) heeft dat concept afgeschaft voor de BV en de CV; alleen de NV (en SE) behoudt het verplichte kapitaal.

**Gevolg voor de jaarrekening**:

| | NV | BV / CV (post-WVV) |
|---|---|---|
| Rubriek I | Geplaatst kapitaal (100) | Inbreng (110/111) |
| Wettelijke reserve | Verplicht (art. 7:211) | Niet verplicht |
| Uitkeringstest | Netto-actieftest (art. 7:212) | Dubbele test: nettoactief + liquiditeit (art. 5:142–143) |
| Eigen aandelen: presentatie | Rubriek 50 activa + onbeschikbare reserve passiva | Rubriek 12 als aftrekpost van eigen vermogen |

**Bestaande BVBA's**: bij de WVV-overgang werd het gestort kapitaal en de wettelijke reserve van rechtswege omgezet in een onbeschikbare eigen vermogensrekening (rekening 1119). Deze kan via statutenwijziging beschikbaar worden gemaakt (CBN-advies 2019/14).

---

## 🔢 Wettelijke reserve — berekening (NV)

De wettelijke reserve wordt gevoed door een verplichte jaarlijkse dotatie van **ten minste 5% van de nettowinst** (= winst van het boekjaar vóór de resultaatverwerking), totdat de reserve gelijk is aan **10% van het geplaatst kapitaal** ([[bronnen/wetteksten/XV-wvv#art-7211|WVV art. 7:211]]).

**Formule**:

```
Dotatie = max(0,  min(5% × nettowinst,  10% × geplaatst kapitaal − bestaande wettelijke reserve))
```

**Voorbeeld**: Geplaatst kapitaal € 100.000. Bestaande wettelijke reserve: € 7.000. Nettowinst: € 40.000.

- Vereist plafond: 10% × 100.000 = € 10.000
- Ruimte tot plafond: 10.000 − 7.000 = € 3.000
- 5% van nettowinst: 5% × 40.000 = € 2.000
- Dotatie = min(2.000, 3.000) = **€ 2.000** (verplichting gestopt zodra plafond bereikt)

Zodra de wettelijke reserve de 10%-grens heeft bereikt, vervalt de dotatieverplichting. Na een kapitaalverhoging stijgt het plafond opnieuw en herleeft de verplichting.

---

## 📋 Boeking bij inbreng in geld (NV/BV)

### NV — oprichting met geplaatst kapitaal, gedeeltelijk volgestort

```
416  Opgevraagd, niet gestort kapitaal    25.000
101  Niet-opgevraagd kapitaal             75.000
     aan 100  Geplaatst kapitaal                  100.000

Bij storting:
550  Bank                                25.000
     aan 416  Opgevraagd, niet gestort kapitaal    25.000
```

### BV — oprichting (geen kapitaal, wel inbreng)

```
550  Bank                                50.000
     aan 110  Beschikbare inbreng buiten kapitaal   50.000
```

Als de statuten de inbreng onbeschikbaar verklaren:
```
     aan 111  Onbeschikbare inbreng buiten kapitaal 50.000
```

---

## 📋 Boeking bij inbreng in natura (NV)

Bij inbreng in natura stelt een aandeelhouder een niet-geldelijk goed ter beschikking (bv. een gebouw, een voertuig, een vordering). De waarde wordt vastgesteld door een bedrijfsrevisor. De boeking:

```
22   Terreinen en gebouwen            150.000   (of andere activarekening)
     aan 100  Geplaatst kapitaal               120.000
     aan 11   Uitgiftepremies                   30.000
```

De revisorskosten worden doorgaans geactiveerd als oprichtingskosten of ten laste van het boekjaar gebracht.

---

## 🔒 Uitkering aan aandeelhouders — uitkeringstests

### BV: dubbele test (art. 5:142–143 WVV)

Vóór elke uitkering (dividend, terugbetaling inbreng, inkoop eigen aandelen) moet aan **twee cumulatieve tests** zijn voldaan:

**1. Nettoactief-test** ([[bronnen/wetteksten/XV-wvv#art-5142|WVV art. 5:142]]):
Geen uitkering is toegelaten indien het [[nettoactief|nettoactief]] van de vennootschap negatief is of door de uitkering negatief zou worden. Evenmin als het nettoactief daalt tot onder het onbeschikbaar eigen vermogen (incl. niet-afgeschreven herwaarderingsmeerwaarden).

**2. Liquiditeitstest** ([[bronnen/wetteksten/XV-wvv#art-5143|WVV art. 5:143]]):
Het bestuursorgaan moet vaststellen — op basis van redelijkerwijs te verwachten ontwikkelingen — dat de vennootschap na de uitkering gedurende **ten minste twaalf maanden** haar schulden kan betalen naarmate ze opeisbaar worden. Het bestuursorgaan legt dit vast in een (niet neer te leggen) verslag.

Als leden van het bestuursorgaan bij de liquiditeitstest wisten of behoorden te weten dat de vennootschap na uitkering haar schulden niet meer kon betalen, zijn zij hoofdelijk aansprakelijk voor alle schade ([[bronnen/wetteksten/XV-wvv#art-5142|WVV art. 5:144]]).

### NV: netto-actieftest (art. 7:212 WVV)

Bij de NV geldt één test: geen uitkering als het [[nettoactief|nettoactief]] (blijkend uit de goedgekeurde jaarrekening) is gedaald of door de uitkering zou dalen tot onder het bedrag van het **gestort of opgevraagd kapitaal** (het hoogste van beide) vermeerderd met alle wettelijk of statutair onbeschikbare reserves ([[bronnen/wetteksten/XV-wvv#art-7212|WVV art. 7:212]]).

De NV heeft **geen liquiditeitstest**.

> [!warning]- BV heeft ook een liquiditeitstest — NV niet
> ❌ *"Als het nettoactief van de BV positief is na de uitkering, mag ze altijd een dividend uitkeren."*
>
> De BV heeft een **dubbele** test: (1) de netto-actieftest én (2) de liquiditeitstest. Een positief nettoactief na uitkering is noodzakelijk maar niet voldoende. Het bestuursorgaan moet ook positief oordelen over de liquiditeit voor de komende twaalf maanden. Beide tests zijn cumulatief.
>
> ([[bronnen/wetteksten/XV-wvv#art-5142|WVV art. 5:142–143]])
>
> 🤖 *AI-aanvulling*

---

## 📌 Eigen aandelen

Eigen aandelen zijn aandelen die de vennootschap in haar bezit heeft van zichzelf. De vennootschap mag ze inkopen, vernietigen of opnieuw vervreemden, maar aan strikte voorwaarden.

### Eigen aandelen bij de NV

**Presentatie**: eigen aandelen worden bij de NV opgenomen als **actief** (rubriek 50 *Eigen aandelen*), niet in mindering op het eigen vermogen. Tegelijkertijd vormt de vennootschap een **onbeschikbare reserve** (rekening 1312) gelijk aan de boekwaarde van de eigen aandelen. De totale omvang van het eigen vermogen blijft dus ongewijzigd — de liquiditeit vermindert, de onbeschikbare reserve stijgt ([[bronnen/wetteksten/XV-wvv#art-7217|WVV art. 7:217, §2]]; [[bronnen/wetteksten/XV-KB-wvv#art-354|KB WVV art. 3:54, §2]]).

**Voorwaarden voor verkrijging** ([[bronnen/wetteksten/XV-wvv#art-7215|WVV art. 7:215, §1]]):
1. Voorafgaand besluit van de algemene vergadering (met statutaire meerderheden)
2. Het uitgetrokken bedrag is voor uitkering vatbaar (netto-actieftest)
3. Het gaat om volgestorte aandelen
4. Het aanbod wordt gericht tot alle aandeelhouders onder gelijke voorwaarden (tenzij eenparige beslissing)

**Boeking bij inkoop (NV)**:
```
500  Eigen aandelen (actief)             30.000
     aan 550  Bank                                30.000

Gelijktijdig: vorming onbeschikbare reserve
14   Overgedragen winst                  30.000   (of beschikbare reserve 133)
     aan 1312  Reserve voor eigen aandelen         30.000
```

Stemrechten en dividendrechten van eigen aandelen zijn **geschorst** zolang de vennootschap ze aanhoudt.

### Eigen aandelen bij de BV

**Presentatie**: eigen aandelen worden bij de BV opgenomen als **aftrekpost van het eigen vermogen** (rubriek 12 *Eigen aandelen*) — niet als actief ([[bronnen/wetteksten/XV-KB-wvv#art-354|KB WVV art. 3:54, §2]]). Er is geen afzonderlijke onbeschikbare reservevorming nodig, want de inkoop vermindert het eigen vermogen rechtstreeks.

**Voorwaarden** ([[bronnen/wetteksten/XV-wvv#art-5145|WVV art. 5:145]]): vergelijkbaar met NV, maar de toelaatbare bedragen worden getoetst aan de **dubbele uitkeringstest** (nettoactief én liquiditeit).

**Boeking bij inkoop (BV)**:
```
12   Eigen aandelen (aftrekpost EV)      20.000
     aan 550  Bank                                20.000
```

> [!warning]- Eigen aandelen van een BV boeken als actief
> ❌ *"Een BV koopt eigen aandelen in. Boeking: debet 50 Eigen aandelen, credit Bank."*
>
> Bij de **BV** worden eigen aandelen niet als actief geboekt (rubriek 50) maar als **aftrekpost van het eigen vermogen** (rubriek 12). Dat is het wezenlijke verschil met de NV, waar eigen aandelen wél actief zijn (rubriek 50) en een compenserende onbeschikbare reserve in het passief verschijnt.
>
> ([KB WVV art. 3:54, §2]; [[bronnen/wetteksten/XV-wvv#art-5148|WVV art. 5:148, §2]])
>
> 🤖 *AI-aanvulling*

> [!warning]- Eigen aandelen behandelen als gewone financiële belegging
> ❌ *"Een vennootschap houdt eigen aandelen aan als kortetermijnbelegging en boekt ze in rubriek 51."*
>
> Eigen aandelen zijn geen belegging in de economische zin. Ze hebben een bijzonder juridisch statuut: stemrechten en dividendrechten zijn geschorst, en de presentatie in de balans verschilt fundamenteel van andere aandelen (actief bij NV, aftrekpost bij BV). Ze mogen nooit bij gewone geldbeleggingen worden geboekt.
>
> 🤖 *AI-aanvulling*

---

## ↔️ BV vs. NV — samenstelling en uitkeringsregels

| Aspect | BV | NV |
|---|---|---|
| Terminologie rubriek I | Inbreng | Kapitaal |
| Wettelijke reserve | Niet verplicht | Verplicht (5% nettowinst tot 10% kapitaal) |
| Uitkeringstest | Nettoactief + liquiditeitstest (dubbel) | Netto-actieftest (enkel) |
| Liquiditeitstest | Ja — bestuursorgaan beslist formeel | Nee |
| Eigen aandelen: balansrubriek | Aftrekpost EV (rubriek 12) | Actief (rubriek 50) |
| Eigen aandelen: onbeschikbare reserve | Niet — rubriek 12 verlaagt EV direct | Ja — rekening 1312 |

---

## 🚩 Kapitaalverhoging zonder volstorting als volledige inbreng boeken

Een vennootschap beslist om haar kapitaal te verhogen met € 100.000, maar de aandeelhouders storten slechts 25% (€ 25.000) onmiddellijk. Als de boeking het volledige bedrag onmiddellijk als gestort kapitaal behandelt, is de balans onjuist: de bankrekening stijgt met slechts € 25.000 maar het gestorte kapitaal lijkt € 100.000 te bedragen.

**Correcte boeking**:
```
416  Opgevraagd, niet gestort kapitaal    25.000
101  Niet-opgevraagd kapitaal             75.000
     aan 100  Geplaatst kapitaal                  100.000

550  Bank                                25.000
     aan 416  Opgevraagd, niet gestort kapitaal    25.000
```

Het geplaatst kapitaal (100) toont € 100.000, maar het niet-opgevraagde kapitaal (101 = −€ 75.000) corrigeert dit zodat het werkelijk volgestorte bedrag van € 25.000 zichtbaar is.

> [!warning]- Volgestort kapitaal en geplaatst kapitaal zijn niet hetzelfde
> ❌ *"Het geplaatst kapitaal van de vennootschap is € 100.000, dus heeft ze € 100.000 aan middelen ontvangen van haar aandeelhouders."*
>
> Het geplaatst kapitaal is het bedrag waartoe de aandeelhouders zich hebben verbonden — niet het bedrag dat al is gestort. Pas nadat het bestuursorgaan het niet-opgevraagde gedeelte opvraagt, en de aandeelhouders dit effectief storten, stijgt het beschikbare vermogen. De balans toont beide: geplaatst kapitaal (100) minus niet-opgevraagd kapitaal (101) = effectief volgestort deel.
>
> 🤖 *AI-aanvulling*

---

## Relevant voor

**[[1.1-algemene-boekhouding|1.1 Algemene boekhouding]]**

Taken:
- *Boeken van verrichtingen en opmaken van de jaarrekening*
  - Boeken van kapitaalwijzigingen en eigen vermogenstransacties

Kenniselementen:
- II.H — Eigen middelen: inbreng, herwaarderingsmeerwaarden, reserves, kapitaalsubsidies
- II.U — Beheer eigen aandelen

### Voorbeeldvragen

> [!question]- Wettelijke reserve NV — dotatieverplichting
>
> Een NV heeft een geplaatst kapitaal van € 200.000. De wettelijke reserve bedraagt momenteel € 16.000. De nettowinst van het boekjaar is € 60.000. Hoeveel moet ten minste worden toegevoegd aan de wettelijke reserve?
>
> > [!success]- Antwoord
> >
> > **€ 3.000.**
> >
> > Vereist plafond: 10% × 200.000 = € 20.000.
> > Ruimte tot plafond: 20.000 − 16.000 = € 4.000.
> > Minimale dotatie: 5% × 60.000 = € 3.000.
> > Dotatie = min(3.000, 4.000) = **€ 3.000**.
> >
> > *Zie: [[eigen-vermogen#-wettelijke-reserve--berekening-nv|Wettelijke reserve — berekening]]*
>
> 🤖 *AI-aanvulling*

> [!question]- Eigen aandelen BV — balansverwerking
>
> Een BV koopt voor € 15.000 eigen aandelen in. De aandeelhouders keurden dit goed; de dubbele uitkeringstest is voldaan.
>
> Hoe worden de eigen aandelen in de balans van de BV weergegeven?
>
> > [!success]- Antwoord
> >
> > **Als aftrekpost van het eigen vermogen (rubriek 12).**
> >
> > Bij een BV worden eigen aandelen niet als actief (rubriek 50) geboekt maar als aftrekpost in het eigen vermogen (rekening 12 *Eigen aandelen*). Het eigen vermogen daalt met € 15.000. Er wordt géén afzonderlijke onbeschikbare reserve gevormd — dat is het verschil met de NV, waar eigen aandelen als actief staan en een compenserende onbeschikbare reserve in het passief verschijnt.
> >
> > *Zie: [[eigen-vermogen#eigen-aandelen-bij-de-bv|Eigen aandelen bij de BV]]*
>
> 🤖 *AI-aanvulling*

> [!question]- Kapitaalsubsidie — timing van de opbrengstneming
>
> Een vennootschap ontvangt een subsidie van € 80.000 voor de aankoop van een productielijn met een levensduur van 8 jaar. In het jaar van ontvangst wordt € 80.000 als financiële opbrengst geboekt.
>
> Juist of fout?
>
> > [!success]- Antwoord
> >
> > **Fout.**
> >
> > Een kapitaalsubsidie voor een investering in vaste activa wordt opgenomen in het **eigen vermogen** (rekening 15 *Kapitaalsubsidies*), niet als onmiddellijke opbrengst. Ze vloeit pas geleidelijk naar de resultatenrekening — als "Onttrekking aan kapitaalsubsidies" (rekening 753) — in hetzelfde ritme als de afschrijvingen op de gesubsidieerde activa. Hier: € 10.000/jaar gedurende 8 jaar.
> >
> > *Zie: [[eigen-vermogen#-kapitaalsubsidies-rubriek-vi-rekening-15|Kapitaalsubsidies]]*
>
> 🤖 *AI-aanvulling*

> [!question]- BV versus NV — uitkeringstests vergelijken
>
> Zowel de BV als de NV passen een netto-actieftest toe voor uitkeringen aan aandeelhouders. Het verschil is dat de BV daarbovenop ook een liquiditeitstest heeft.
>
> Juist of fout?
>
> > [!success]- Antwoord
> >
> > **Juist.**
> >
> > De BV heeft een dubbele test: de netto-actieftest ([[bronnen/wetteksten/XV-wvv#art-5142|art. 5:142 WVV]]) én de liquiditeitstest ([[bronnen/wetteksten/XV-wvv#art-5143|art. 5:143 WVV]]). Het bestuursorgaan moet formeel vaststellen dat de vennootschap gedurende minstens twaalf maanden na de uitkering haar schulden kan betalen. De NV heeft enkel de netto-actieftest ([[bronnen/wetteksten/XV-wvv#art-7212|art. 7:212 WVV]]). Beide tests zijn cumulatief voor de BV.
> >
> > *Zie: [[eigen-vermogen#bv-dubbele-test-art-5142143-wvv|Uitkeringstests BV/NV]]*
>
> 🤖 *AI-aanvulling*
