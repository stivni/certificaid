# Leerpad-skelet PO 2.5 — Fiscale procedure

**Status**: voorstel (2026-06-01). Sparring-document voor de bouw van het volledige leerpad-pakket (overzicht + leerstukken + samenvatting + oefening).
**Volgende stap**: na sparring → besluit over voorbeeldgroep + scripts per leerstuk via één Opus-run (ADR-037 amendement B) + samenvatting-migratie uit 4 themafiches + oefening (procedure-multi-case-dossier).

---

## 1. Programma-analyse

### 1.1 Officiële taken en doelstellingen

PO 2.5 heeft **vier taken** met **vier doelstellingen** in totaal. Niveau: **integratie** (`niveau: integratie` — hoogste cognitieve laag).

| Code | Tekst (kort) | Rol |
|---|---|---|
| 2.5.taak.1 | Begeleiding bij oprichting van een onderneming | anchor — randtaak (oprichtings-fiscaliteit; deels in PO 2.1) |
| 2.5.taak.1.doel.1 | Autonoom werken in complexe fiscale omgeving — geïntegreerd advies | context |
| 2.5.taak.2 | De belastingplichtige in alle fiscale aangelegenheden advies verlenen | anchor — advies-taak |
| 2.5.taak.2.doel.1 | Zelfstandig en proactief in complexe fiscale omgeving werken | context |
| 2.5.taak.3 | Bijstaan bij vervullen fiscale verplichtingen (compliance) | anchor — **hoofdtaak** |
| 2.5.taak.3.doel.1 | Relevante informatie verzamelen + juiste vragen stellen + risico's beheren | context |
| 2.5.taak.3.doel.2 | Geavanceerde concepten fiscale procedure toepassen op complexe gevallen | context — **kern van het PO** |
| 2.5.taak.4 | Vertegenwoordigen bij fiscale administraties | anchor — vertegenwoordigings-taak |
| 2.5.taak.4.doel.1 | Adviseren over fasen belastingprocedure + gevolgen-afweging | context |

**Cruciale observaties**:

1. **Taken 1-3 zijn cross-PO** (formuleringen identiek aan PO 2.1, 2.6, 2.7) — vrijwel elke fiscale PO heeft deze drie. **De eigenheid van PO 2.5 zit in taak 4 (vertegenwoordigen) + in doel 3.2 (geavanceerde procedure-concepten toepassen)**. Daar moet de pedagogische klemtoon liggen.
2. **De hoofdtaak is 2.5.taak.3** in combinatie met 2.5.taak.4 — compliance (aangifte + termijnen + bewaarstukken) doorlopend, en vertegenwoordiging op kritieke procedure-momenten (controle, bezwaar, bemiddeling, gerechtelijke fase). Taak 2 (advies) is permanent-actief op de achtergrond.
3. **"Geavanceerde procedure-concepten op complexe gevallen"** (doel 3.2) is sterk: stuiting van termijnen, ambtshalve ontheffing, schorsing van invordering, omkering van bewijslast, samenloop administratieve-gerechtelijke fasen — niet de standaard-stappen, maar de tactische combinatie ervan.

### 1.2 Kenniselementen-tree (8 hoofdblokken, vlak — geen sub-items)

| Code | Tekst | Kern / rakend |
|---|---|---|
| 2.5.I | Taxatieprocedure | **Kern** — vestiging aanslag, BvW, ambtshalve aanslag |
| 2.5.II | Algemene beginselen van goed bestuur | **Kern** — rechtszekerheid, vertrouwen, zorgvuldigheid, redelijkheid, motivering |
| 2.5.III | Aangifte | **Kern + rakend** (PO 2.2/2.3/2.4 voor inhoud; hier proces) |
| 2.5.IV | Onderzoeksbevoegdheden | **Kern** — art. 315-326 WIB + WBTW art. 60-63 |
| 2.5.V | Bewijsmiddelen | **Kern** — art. 339-344 WIB + tekenen/indiciën + boekhouding als bewijs |
| 2.5.VI | Aanslagprocedure (= bezwaar) | **Kern** — bericht van wijziging, bezwaar, beslissing directeur, opent gerechtelijke fase |
| 2.5.VII | Bemiddelingsprocedure | **Kern** — FBD, schorsing beroepstermijn |
| 2.5.VIII | Invorderingsprocedure | **Kern** — dwangbevel, beslag, verzet |

**Structuur-observatie**: 8 vlak gepresenteerde blokken — maar pedagogisch lopen ze door een **chronologische as** (aangifte → controle → taxatie → bezwaar → bemiddeling → gerechtelijke fase → invordering) **plus** een **transversale laag** (beginselen van behoorlijk bestuur + bewijsmiddelen + termijnen). Het programma noemt termijnen niet expliciet als kenniselement — maar uit de voorbeeldexamens blijkt dat ze **dé** examenstof zijn (zie §2). De aanslagtermijnen worden afgeleid uit 2.5.IV (onderzoek), 2.5.VI (aanslag) en 2.5.VIII (verjaring invordering).

### 1.3 Kern vs rakend

**Kern (eigen aan 2.5)**:
- **Federale taxatie-procedure WIB92** — art. 305-393 (aangifte, controle, BvW, ambtshalve aanslag, vestiging) ⚖️ verifieerd
- **Onderzoeksbevoegdheden** — art. 315 (boeken/bescheiden), 316 (vraag om inlichtingen aan belastingplichtige), 319 (controle ter plaatse), 322 (vraag aan derden + bankgeheim doorbreking), 322bis (bankgegevens), 333 (kennisgeving fraude) ⚖️
- **Aanslagtermijnen** — art. 354 WIB (3/4/6/10 jaar sinds Wet 20-11-2022) + art. 358 (bijzondere termijnen, o.a. 24 maanden buitenlandse inlichtingen) ⚖️
- **Bewijsmiddelen** — art. 339-344 WIB: gemeen recht + tekenen en indiciën (341) + vergelijking (342) + AAMB als herkwalificatie (344 §1)
- **Beginselen behoorlijk bestuur** — ongeschreven + Wet 29-07-1991 (motivering) + Wet 11-04-1994 (openbaarheid) — vijf beginselen (rechtszekerheid, zorgvuldigheid, redelijkheid, vertrouwen, motivering)
- **Bezwaarprocedure** — art. 366 + 371 WIB: **1 jaar** vanaf 3e werkdag na verzending aanslagbiljet ⚖️ verifieerd via RAG ⚠️ concept-record `bezwaarprocedure` vermeldt "6 maanden" — stale en in tegenspraak met art. 371 WIB92 actuele tekst. Correctie nodig vóór scripts-fase.
- **Fiscale bemiddelingsprocedure** — Wet 25-04-2007 + sinds 2019 ook invorderingsgeschillen
- **Gerechtelijke fase** — rechtbank van eerste aanleg (fiscale kamer, Ger.W. art. 569 16°) → hof van beroep → Cassatie
- **Invorderingsprocedure** — Wetboek minnelijke en gedwongen invordering (sinds 2020) — federaal voor PB/VenB/btw; dwangbevel als uitvoerbare titel; verzet via vordering in rechte als enige stuiting van tenuitvoerlegging
- **WBTW-eigenheden** — art. 81bis WBTW (verjaring 3/4/7 jaar) + art. 60-63 WBTW (onderzoeksbevoegdheden parallel maar eigen)
- **Geheime commissielonen-aanslag** — art. 219 WIB als "examen-klassieker" voor sanctie-aanslagen ⚖️ ⚠️ pedagogisch raakt dit eerder VenB (PO 2.3) — in PO 2.5 alleen voor zover het de procedure raakt (welke aanslagtermijn? welk bezwaartraject?)

**Rakend met andere PO's**:
- **PO 2.1 — Algemene beginselen van fiscaal recht**: levert het denkkader (legaliteit, gelijkheid, non-bis-in-idem). PO 2.5 doet de **procedurele uitwerking** — beginselen behoorlijk bestuur (zorgvuldigheid, motivering) zijn hier de operationele variant. Afbakening helder.
- **PO 2.2 PB · 2.3 VenB · 2.4 btw**: leveren de **materiële** aangifte (vakken, bedragen, codes). PO 2.5 doet de **proces-mantel** rond elke aangifte: termijn, bewaarplicht, controle-respons, bezwaar. De voorbeeldexamen-vragen over PB-aangifte bij vertrek (art. 309 WIB) en VenB-aangifte (art. 310 WIB) leven in een grijze zone — proceduratief gaan ze over **2.5**, materieel over 2.2/2.3.
- **PO 2.7 — Regionale en lokale belastingen**: heeft **eigen procedure-eigenheden** (Vlabel-bezwaartermijn 3 mnd, college B&S 3 mnd, RvS 60 dgn). PO 2.5 doet alleen de **federale algemene** procedure; in 2.7 leven de afwijkingen. Belangrijke afbakening — anders dupliceren ze elkaar.
- **PO 2.6 — Registratie- en successierechten**: eigen procedure-regimes (Vlabel voor erfbelasting, federaal voor registratie buiten Vlaanderen). Aanstippen in cross-PO-tabel.
- **PO 1.2 — Boekhoudrecht**: bewaarplicht WER art. III.86 (7 jaar) overlapt met fiscale bewaarplicht WIB art. 315 (10 jaar sinds aj. 2023). Klassieke examen-strikvraag.
- **PO 1.6 — Externe controle**: onderzoeksbevoegdheden van de fiscus lijken op (maar verschillen van) bevoegdheden van de commissaris. Vermelden, niet uitwerken.

---

## 2. Voorbeeldexamen-patronen

PO 2.5 is een van de **goed bevraagde PO's**: 23 unieke vraag-eenheden (waarvan 2 clusters; totaal 25 voorkomens) uit 9 examens (2003-bibf, 2008-bibf, 2010-2, 2013-1, 2013-2, 2014-1, 2015-1, 2019-bibf, 2024-1) — alle met modelantwoord. Dit is **hét PO met examen-houvast** (in tegenstelling tot bv. PO 2.7 dat nog leeg is). De skelet-keuzes kunnen hier **rechtstreeks aan examenstof verankerd** worden.

### 2.1 Bevraagde patronen (uit `content/studiemateriaal/2-5/voorbeeldexamenvragen.md`)

| Patroon | Frequentie | Typische vraag | Kenniselement |
|---|---|---|---|
| **Bericht van wijziging — uiterlijke verzendingstermijn** | 1× (2024-1) | "Wanneer moet BvW verstuurd zijn?" — art. 354 WIB | 2.5.I + 2.5.VI |
| **Verlenging aanslagtermijn 6 maanden na BvW** | 1× (2024-1) | "Nakende verjaring — wat doet de administratie?" — art. 354 §1 lid 4 | 2.5.I |
| **Vraag om inlichtingen — antwoordtermijn 1 maand vanaf 3e werkdag** | 3× (2024-1, 2019-bibf, impliciet 2015-1) | "Termijn antwoord?" + "Wie kan ondertekenen?" — art. 316 WIB | 2.5.IV |
| **Vraag aan derden — geen wettelijke termijn, vrij door administratie** | 2× (2014-1, 2013-2 — duplicaat) | "Termijn van 10 dagen + onderbreking door staking — regelmatig?" — art. 323 WIB | 2.5.IV |
| **Onderzoekstermijn 5 jaar terug — voorafgaande kennisgeving fraude** | 1× (2015-1) | "Kan de administratie?" — art. 333 lid 3 WIB | 2.5.IV + 2.5.II |
| **Bijzondere aanslagtermijn 24 maanden — buitenlandse inlichtingen via DBV** | 1× (2015-1) | "Kan nog getaxeerd worden?" — art. 358 §1 2° + §2 WIB | 2.5.I |
| **Bewaarplicht — boekhoudkundig 7 jaar vs fiscaal 10 jaar + scope (bestelbonnen)** | 3× (2024-1, 2015-1, impliciet 2014/13) | "Welke stukken + welke termijn?" + "Moeten bestelbonnen voorgelegd worden?" — art. 315 WIB + WER art. III.86 | 2.5.IV |
| **Bijzondere aangifte PB bij vertrek uit België — 3 maanden** | 1× (2024-1) | "Welke verplichtingen bij emigratie?" — art. 309 WIB | 2.5.III (raakt PO 2.2) |
| **Aangifte VenB — termijn 1 maand na goedkeuring jaarrekening, max 6 mnd na boekjaar** | 1× (2019-bibf) | "Binnen welke termijn?" + "Uiterste indieningsdatum?" — art. 310 WIB + art. 53 Ger.W. | 2.5.III (raakt PO 2.3) |
| **Btw-onderzoekstermijn — geen "altijd 7 jaar", maar gedifferentieerd 3/4/7** | 1× (2015-1) | "Wat is de termijn?" — art. 81bis WBTW | 2.5.I + 2.5.IV (btw-eigenheid) |
| **Bezwaar — wie kan indienen + ondertekenen (volmacht)** | 2× (2014-1, 2013-2 — duplicaat) | "Wie kan bezwaar indienen?" — art. 366 WIB | 2.5.VI |
| **Tenuitvoerlegging dwangbevel — alleen vordering in rechte stuit** | 1× (2015-1) | "Welk middel?" — art. 221 W.Reg. + analoog WIB | 2.5.VIII |
| **Gevolgen van niet-antwoorden op vraag om inlichtingen** | 1× (2019-bibf) | "Wat kan er gebeuren?" — art. 346 + 351 + 444-445 WIB | 2.5.IV + 2.5.I |

### 2.2 Observaties

1. **Termijnen + vormvereisten domineren** — bijna elke vraag is "wat is de termijn?" of "is de vorm regelmatig?". Bijna nooit inhoudelijke fiscale kwesties. Het examen toetst **procedure als spel met klokken en stempels**, niet als interpretatie van materieel recht.
2. **Strikvragen op stale/oude regels** — "altijd 7 jaar btw" (fout), "termijn 12 maanden buitenlandse inlichtingen" (fout — 24 mnd), "bezwaartermijn 6 maanden" (fout — 1 jaar). Examen-favoriet: een onjuist getal in een MCQ-optie. Studiemateriaal moet **expliciet de juiste én de typische foute waarden** noemen.
3. **De aanslagtermijnen-hervorming Wet 20-11-2022** (3/4/6/10 jaar i.p.v. 3/7/7) is sinds aj. 2023 van toepassing — oudere examens (2013-2015) gebruiken nog de oude termijnen. Studiemateriaal moet de **nieuwe regels** als hoofdkader hanteren en de oude alleen vermelden als "voor aanslagjaren ≤ aj. 2022".
4. **Cross-PO-grijs gebied**: vragen over aangifte PB bij vertrek (art. 309 WIB) en aangifte VenB-termijn (art. 310 WIB) zijn formeel onder PO 2.5 getagd maar materieel deels PB/VenB. Hou ze in PO 2.5 — de **proceduratief-aangiftekant** is het examen-thema. Doorklik naar PO 2.2/2.3 voor vak-inhoud.
5. **Beginselen van behoorlijk bestuur** worden zelden expliciet bevraagd, maar duiken impliciet op (kennisgeving fraude art. 333 = uitwerking van zorgvuldigheid + motivering; redelijkheidsbeginsel bij belastingverhoging). Behandel ze als **transversale laag** in elk leerstuk i.p.v. één geïsoleerd leerstuk.

### 2.3 Implicatie voor de leerstuk-structuur

De examen-realiteit dwingt twee dingen af:
- Een **termijnen-tabel als rode draad** doorheen meerdere leerstukken (aanslag · onderzoek · BvW-antwoord · BvW-verlenging · bezwaar · gerechtelijk · invordering · btw-eigen + gewest-eigen).
- Een **leerstuk dat onderzoek+bewijs+vraag-om-inlichtingen samen behandelt** — examen-klassiekers (5-jaar-onderzoek, bestelbonnen-bewaring, vraag aan derden vs. aan belastingplichtige) leven hier.

---

## 3. Leerstuk-voorstel

**Voorstel: 5 leerstukken**. Granulariteits-stelregel toegepast: eerder samen dan splitsen. **De chronologische timeline (aangifte → controle → taxatie → bezwaar → bemiddeling → gerechtelijk → invordering) is de natuurlijke kapstok** — niet alle 7 stappen worden aparte leerstukken (dan zou de bemiddeling een dun leerstuk worden + zou de stagiair vergelijking missen).

### Leerstuk 1 — `wat-is-fiscale-procedure-en-aanslagcyclus` (entry + timeline)

- **Vraag**: Wat is fiscale procedure en wat is de timeline van aangifte tot definitieve aanslag — wat staat waar in welke wet, en op welke twee momenten heeft de cliënt dringend advies nodig?
- **Type**: entry-fiche (kader, doorklik-zwaar)
- **Gedekte taken/doelstellingen**: 2.5.taak.2 (advies kader) · 2.5.taak.3.doel.1 (info verzamelen + juiste vragen stellen)
- **Gedekte kenniselementen**: 2.5.I (taxatieprocedure als overzicht) · 2.5.III (aangifte als startpunt)
- **Gedekte concepten**: `fiscale-procedure` ⭐ · `aanslag-cyclus` ⭐ · `aangifteplicht` ⭐ · `aanslagbiljet-pb` (kort, voor inkohiering+aanslagbiljet als ontvankelijkheidsmoment) · `fiscale-actoren` (cross-PO, kort — wie heft wat)
- **Rationale**: Zonder een mentale timeline van aangifte → controle → taxatie → bezwaar → invordering blijft elk vervolg-leerstuk een losse anekdote. Dit leerstuk vestigt de **drie fases** (taxatie · betwisting · invordering) en de **twee scharnier-momenten** waar de cliënt advies nodig heeft: ontvangst BvW (1 maand antwoorden) en ontvangst aanslagbiljet (bezwaar of betalen). Het noemt de wetboeken (WIB92 art. 305-393 · WBTW art. 81bis · Wetboek Invordering · VCF) zodat de stagiair weet **waar opzoeken**. Geen technische diepte — alleen de kaart.

### Leerstuk 2 — `controle-onderzoek-en-bewijs` (techniek 1 — zwaarste leerstuk)

- **Vraag**: Hoe controleert de fiscus een aangifte — welke onderzoeksbevoegdheden heeft hij, welke termijnen gelden, welke bewijsmiddelen mag hij gebruiken, en welke rechten heeft de cliënt?
- **Type**: techniek + onderzoeks-fiche (zwaarste leerstuk in het pakket — analoog aan `hoe-consolideren` voor PO 1.4)
- **Gedekte taken/doelstellingen**: 2.5.taak.3 (bijstaan bij compliance) · 2.5.taak.3.doel.2 (geavanceerd toepassen op complexe gevallen) · 2.5.taak.4 (vertegenwoordigen tijdens controle)
- **Gedekte kenniselementen**: 2.5.IV (onderzoeksbevoegdheden — kern) · 2.5.V (bewijsmiddelen — kern) · 2.5.I (aanslagtermijnen als parallelle termijn van onderzoek) · raakt 2.5.II (beginselen — voorafgaande kennisgeving fraude als operationalisering)
- **Gedekte concepten**: `fiscale-controle` ⭐ · `fiscale-bewijsmiddelen` ⭐ · `aanslagtermijnen` ⭐ · `btw-controle` (subsectie btw-eigenheden) · raakt `beginselen-behoorlijk-bestuur`
- **Rationale**: Examen-favoriet bij uitstek: **6 van de 13 patroon-vragen** spelen zich hier af (vraag om inlichtingen, vraag aan derden, kennisgeving fraude, bewaarplicht, bestelbonnen, btw-controle). Dit leerstuk integreert vier draadjes: (a) wat **mag** de fiscus (art. 315-326 WIB + 60-63 WBTW); (b) welke **termijnen** gelden (aanslagtermijn = onderzoekstermijn, sinds Wet 20-11-2022 — 3/4/6/10 jaar; btw 3/4/7 jaar); (c) welke **bewijsmiddelen** mag de fiscus inzetten (art. 339-344 WIB — gemeen recht + tekenen-en-indiciën + vergelijking); (d) welke **rechten/grenzen** heeft de cliënt (1 maand antwoordtermijn art. 316; vrije termijn art. 323; voorafgaande kennisgeving art. 333; bankgeheim-grenzen art. 322; ambtshalve aanslag-risico). Mag tot ~4000 woorden lopen ("hoe-uitzondering" in leerstuk-schrijfregels). **Splitsen in twee leerstukken (onderzoek/bewijs) is af te raden**: de termijn-en-bewijs-as is **gekoppeld** — een laat onderzoek leidt tot omkering bewijslast, en een tekenen-en-indiciën-aanslag (bewijsmiddel) is alleen geldig binnen aanslagtermijn (termijn).

### Leerstuk 3 — `taxatie-bericht-van-wijziging-en-ambtshalve-aanslag` (proces 1 — scharniermoment)

- **Vraag**: Hoe vestigt de fiscus de aanslag — wat is een bericht van wijziging, wanneer een ambtshalve aanslag, en hoe reageert de cliënt binnen de wettelijke termijn?
- **Type**: proces-fiche (één scharniermoment uitgewerkt — analoog aan `hoe-omgaan-met-controlewerkzaamheden` in audit-clusters)
- **Gedekte taken/doelstellingen**: 2.5.taak.4 (vertegenwoordigen tijdens taxatie) · 2.5.taak.3.doel.2 (geavanceerde concepten — verlenging 6 maanden, stuiting termijnen)
- **Gedekte kenniselementen**: 2.5.I (taxatieprocedure — kern) · raakt 2.5.II (motiveringsplicht, zorgvuldigheid) · raakt 2.5.V (omkering bewijslast bij ambtshalve aanslag)
- **Gedekte concepten**: `taxatieprocedure` ⭐ · `beginselen-behoorlijk-bestuur` ⭐ (hier landt het — motiveringsplicht + zorgvuldigheid) · raakt `fiscale-sancties` (belastingverhoging + boete-cascade)
- **Rationale**: De vraag-om-inlichtingen-fase eindigt in een ⓐ aanvaarding, ⓑ bericht van wijziging (art. 346 — 1 maand antwoorden), of ⓒ ambtshalve aanslag (art. 351 — omkering bewijslast). Dit is dé **knip-moment** waar de cliënt advies nodig heeft. Examen-klassieker: BvW-verlenging 6 maanden (art. 354 §1 lid 4) — wordt expliciet getoetst in 2024-1. Dit verdient een **eigen leerstuk** omdat (a) de denkactie verschilt van leerstuk 2 (van "wat mag de fiscus" naar "hoe verdedig ik mijn cliënt"); (b) de **beginselen van behoorlijk bestuur** hier hun praktisch leven krijgen (een ongemotiveerde BvW = nietig); (c) de **fiscale sancties** (belastingverhoging art. 444 + boete art. 445) sluiten hier aan als gevolg. **Niet samenvoegen met leerstuk 2** — anders wordt het te lang en verliest de stagiair de focus op het scharniermoment.

### Leerstuk 4 — `bezwaar-bemiddeling-en-gerechtelijke-fase` (proces 2 — geschilbeslechting)

- **Vraag**: Hoe betwist de cliënt een gevestigde aanslag — wat is bezwaar (administratief), wanneer bemiddeling, wanneer rechtbank, en welke termijnen gelden in elke fase?
- **Type**: proces-fiche (geschil-route)
- **Gedekte taken/doelstellingen**: 2.5.taak.4 (vertegenwoordigen in bezwaar en gerechtelijke fase) · 2.5.taak.4.doel.1 (fasen + gevolgen-afweging)
- **Gedekte kenniselementen**: 2.5.VI (aanslagprocedure = bezwaar — kern) · 2.5.VII (bemiddeling — kern) · gerechtelijke fase (impliciet in 2.5.VI als beslissing-directeur opent rechtbankweg)
- **Gedekte concepten**: `bezwaarprocedure` ⭐ ⚠️ (correctie nodig: termijn 1 jaar i.p.v. 6 maanden) · `fiscale-bemiddelingsprocedure` ⭐ · `gerechtelijke-fase-belasting` ⭐ · raakt `beginselen-behoorlijk-bestuur` (reformatio in pejus verboden = redelijkheid)
- **Rationale**: Drie chronologische schakels (bezwaar bij directeur → eventueel FBD-bemiddeling → rechtbank van eerste aanleg → hof van beroep → Cassatie) horen pedagogisch in één leerstuk omdat ze **één keuzeboom** vormen: de cliënt staat na elke afwijzing voor de keuze "doorzetten of niet". De **termijnen** lopen daarbij door (1 jaar bezwaar art. 371 — 3 maanden naar rechtbank — 1 maand hoger beroep — 3 maanden cassatie). FBD heeft een **schorsende werking op de beroepstermijn naar de rechtbank** — examen-klassieker en raakvlak voor accountantsadvies. Vlabel-eigenheid (3 mnd bezwaartermijn) en btw (3 mnd) **vermelden** maar materieel in PO 2.7 / PO 2.4. **Verzet tegen dwangbevel** behoort NIET hier (dat is invordering, leerstuk 5 — andere denkactie). **Niet splitsen in bezwaar/gerecht-twee-leerstukken** — de bezwaarbeslissing is **toegangsvoorwaarde** tot de rechter; samen leren is sterker.

### Leerstuk 5 — `invordering-en-verzet-tegen-dwangbevel` (proces 3 — collectie-fase)

- **Vraag**: De aanslag is definitief en onbetaald — hoe vordert de fiscus in, welke beslagen kan hij leggen, en hoe verdedigt de cliënt zich tegen tenuitvoerlegging?
- **Type**: proces-fiche (invorderings-route)
- **Gedekte taken/doelstellingen**: 2.5.taak.4 (vertegenwoordigen in invordering) · 2.5.taak.4.doel.1 (gevolgen-afweging — bezwaar schorst invordering NIET)
- **Gedekte kenniselementen**: 2.5.VIII (invorderingsprocedure — kern)
- **Gedekte concepten**: `invorderingsprocedure` ⭐ · raakt `bestuurdersaansprakelijkheid` (hoofdelijkheid art. 442quater WIB voor BV en bedrijfsvoorheffing — cross-PO 3.0) · raakt `geheime-commissielonen` (alleen kort, als illustratie van een snel-eisbare sanctie-aanslag — eigenlijk PO 2.3)
- **Rationale**: Invordering verdient een **eigen leerstuk** omdat het een **andere logica** volgt dan vestiging/bezwaar: de aanslag is dan al definitief, het kohier is een uitvoerbare titel (art. 297-298 WIB), en de **enige stuiting** van tenuitvoerlegging is een **vordering in rechte** (verzet, niet administratief bezwaar). Dit onderscheid **bezwaar ≠ verzet** is een examen-klassieker (2015-1 vr44) en wordt door stagiairs vaak verward. Drie types beslag (bewarend · uitvoerend · onder derden), dwangbevel als uitvoerbare titel, verzet binnen 1 maand bij de beslagrechter — dit zijn allemaal aan elkaar geketende mechanismen die pedagogisch in één beweging horen. Hoofdelijkheid van de bestuurder voor bedrijfsvoorheffing/btw (art. 442quater WIB) sluit hier aan als compleetheid maar raakt PO 3.0 — kort houden.

### Waarom niet 4 of 6 of 7?

- **Niet 4** (door leerstuk 1 te integreren in leerstuk 2): dan verdwijnt de **kapstok-functie** van leerstuk 1 en moet leerstuk 2 zelf de hele timeline schetsen — wordt te zwaar. Leerstuk 1 dient als snelle-instap voor de stagiair die het PO voor het eerst opent.
- **Niet 6** (door bemiddeling apart te leggen): de bemiddelingsprocedure is **te dun** voor een eigen leerstuk (één kenniselement, beperkt examen-focus) en is bovendien **alleen relevant in samenhang met bezwaar** (schorsing beroepstermijn). Een sub-sectie in leerstuk 4 doet het werk.
- **Niet 7** (door alle 8 kenniselementen één-op-één te volgen): dit zou een leerstuk maken voor de algemene beginselen van behoorlijk bestuur (2.5.II) — maar die zijn pedagogisch **een transversale laag** die in elk leerstuk terugkomt (motivering BvW in leerstuk 3; zorgvuldigheid bij onderzoek in leerstuk 2; redelijkheid bij sanctie in leerstuk 3; rechtszekerheid in cross-PO 2.1). Een eigen leerstuk zou een **abstract verhaal zonder klant-scenario** worden. Beter: in elk leerstuk een blok "Beginselen-haakjes" waarin de stagiair leert herkennen waar het beginsel-argument speelt.
- **Niet 7** (door bewijsmiddelen apart te leggen): bewijsmiddelen leven **in dialoog met onderzoeksbevoegdheden** (de fiscus onderzoekt om bewijs te verzamelen; bewijsmiddel = uitkomst van onderzoek). Samen leren is pedagogisch sterker dan apart. Examen bevestigt: bestelbonnen-vragen (2015-1 vr43) toetsen tegelijk bewaarplicht (onderzoek) én voorleggingsplicht (bewijs).

---

## 4. Gap-check

Matrix kenniselement × leerstuk:

| Kenniselement | L1 entry | L2 controle+bewijs | L3 taxatie+BvW | L4 bezwaar+bemid+gerecht | L5 invordering | Status |
|---|---|---|---|---|---|---|
| 2.5.I Taxatieprocedure | ✅ timeline-overzicht | ✅ aanslag-/onderzoekstermijn | ✅ BvW + ambtshalve | – | – | OK |
| 2.5.II Beginselen behoorlijk bestuur | doorklik | ✅ zorgvuldigheid bij onderzoek | ✅ motivering BvW + redelijkheid sanctie | ✅ reformatio in pejus verboden | – | OK (transversaal) |
| 2.5.III Aangifte | ✅ kern | doorklik (bewaarplicht) | doorklik (laattijdig → ambtshalve) | – | – | OK |
| 2.5.IV Onderzoeksbevoegdheden | – | ✅ kern | – | – | – | OK |
| 2.5.V Bewijsmiddelen | – | ✅ kern | doorklik (omkering bij ambtshalve) | – | – | OK |
| 2.5.VI Aanslagprocedure (bezwaar) | doorklik | – | – | ✅ kern | – | OK |
| 2.5.VII Bemiddelingsprocedure | – | – | – | ✅ kern (sub-sectie) | – | OK |
| 2.5.VIII Invorderingsprocedure | doorklik | – | – | – | ✅ kern | OK |
| Taak 2.5.1 oprichting begeleiding | – | – | – | – | – | ⚠️ niet gedekt — bewust (zit in PO 2.1 + 2.3 — oprichting is geen procedure-thema) |
| Taak 2.5.2 advies in fiscale aangelegenheden | ✅ kader | ✅ controle-advies | ✅ BvW-advies | ✅ bezwaar-advies | ✅ invorderings-advies | OK |
| Taak 2.5.3 bijstaan bij verplichtingen | ✅ aangifte-mantel | ✅ bewaarplicht + voorleggen | – | – | – | OK |
| Taak 2.5.4 vertegenwoordigen | – | ✅ controle-respons | ✅ BvW-respons | ✅ bezwaar + bemiddeling + rechter | ✅ verzet | OK (kern-taak gedekt) |

**Geen kritieke gaten**. Eén bewust dunne dekking: taak 2.5.1 (oprichting begeleiding) is een cross-PO-formulering die elke fiscale PO bevat zonder eigen kenniselementen. Geen aparte aandacht nodig.

**Drie aanwijzingen voor scripts-fase**:
- Leerstuk 2 moet *expliciet* de **dialoog tussen onderzoek + termijn + bewijsmiddel** als rode draad nemen — anders verkruimelt het tot losse art.-nummers.
- Leerstuk 3 moet *de scharnier-functie* van het BvW-moment uitlichten (advies-call-to-action) — niet als technische uitleg verzanden.
- Leerstuk 4 moet expliciet **bezwaar ≠ verzet** uitleggen vóór leerstuk 5 — anders verwart de stagiair bezwaar (administratief, tegen aanslag, bij directeur) met verzet (gerechtelijk, tegen tenuitvoerlegging, bij beslagrechter).

**Een opmerking over `bezwaarprocedure` concept-record**: ⚠️ vermeldt "6 maanden bezwaartermijn" — dit is **stale**. RAG-verificatie via `mcp__certificaid-rag__zoek_bronnen` bevestigt: art. 371 WIB92 actuele tekst → **1 jaar** vanaf 3e werkdag na verzending aanslagbiljet. Bestaand `content/studiemateriaal/2-5/index.md` en de voorbeeldexamen-vragen 2024-1 vermelden correct 1 jaar. **Concept-record bezwaarprocedure moet voor scripts-fase gecorrigeerd worden** (operatie: `claims_checken` op `bezwaarprocedure`).

---

## 5. Overzicht-skelet (ADR-036 vijf-secties)

Bestand: `content/studiemateriaal/2-5/index.md`. Het huidige bestand is pedagogisch sterk — vooral §1 + §2 + §5 zijn behoudenswaardig. §3 herstructureren naar leerstuk-leesroute, §4 (studie-aanpak) wordt leesroute, §5 examen-radar behouden, §6 cross-PO uitbreiden.

### §1 — Waarom dit vak?

Hergebruiken uit huidige `index.md` §1 (uitstekend geschreven: "stille tweede leven van elke aanslag", "vak van de termijnen + rechten van verdediging"). Sterke punten behouden:
- "Stille tweede leven van elke aanslag" als opening
- "Federaal vs gewest vs btw"-uitleg (WIB / Wetboek Invordering / VCF / WBTW art. 81bis)
- Tabel "Hoe past dit in het bredere programma?" — actualiseren: PO 2.1 (denkkader) · PO 2.2 (aangifte PB) · PO 2.3 (aangifte VenB) · PO 2.4 (btw eigen verjaring) · PO 2.6 (registratie/successie) · PO 2.7 (regionale procedure-eigenheden) · PO 1.6 (externe controle — vergelijking onderzoeksbevoegdheden)

### §2 — Wat is dit vak?

Vijf compacte sub-secties, elk eindigend met wikilink naar het bijhorende leerstuk:

- "De fiscale procedure als timeline — drie fases, twee scharniermomenten" → [[wat-is-fiscale-procedure-en-aanslagcyclus]]
- "Wat mag de fiscus controleren — onderzoek, termijnen, bewijs" → [[controle-onderzoek-en-bewijs]]
- "Het bericht van wijziging — moment om te reageren" → [[taxatie-bericht-van-wijziging-en-ambtshalve-aanslag]]
- "Bezwaar, bemiddeling, rechter — drie schakels van de geschilroute" → [[bezwaar-bemiddeling-en-gerechtelijke-fase]]
- "Invordering en verzet — als de aanslag definitief is" → [[invordering-en-verzet-tegen-dwangbevel]]

### §3 — Wat moet je kunnen + hoe pak je het aan

Vervang de huidige (lange) "kern + rakend"-lijst door:

**Leesroute in 5 stappen**:
1. Begin met het stelsel-overzicht (leerstuk 1)
2. Onderzoek + termijnen + bewijsmiddelen (leerstuk 2) — **leer de termijntabel als hart**
3. Bericht van wijziging — wat is de antwoord-strategie? (leerstuk 3)
4. Bezwaar, bemiddeling, rechter (leerstuk 4)
5. Invordering + verzet (leerstuk 5)

+ Verwijzing naar **samenvatting** voor herhaling en **oefening** voor doorwerk.

### §4 — Examen-radar (behouden + actualiseren)

De huidige tabel (§5 van `index.md`) is **bruikbaar als is** — 19 vraag-eenheden uit 7 examens, met patroon-observaties. De daadwerkelijke aantallen vereisen lichte update (huidige render: 23 unieke vragen, 25 voorkomens, 9 examens — zie `content/studiemateriaal/2-5/voorbeeldexamenvragen.md` v2026-06-01). Voeg patroon-observatie toe: **strikvragen op stale waarden** (zie §2.2 hierboven) — examinator verstopt graag een fout getal in een MCQ-optie.

### §5 — Concepten cross-PO

Tabel — kleine update:

| Concept | Cross-PO | Waarom relevant elders |
|---|---|---|
| `aanslagtermijnen` | PO 2.2 · 2.3 · 2.4 | Verschillen per belasting (10 jaar WIB fraude vs 7 jaar btw) |
| `aangifteplicht` | PO 2.2 · 2.3 · 2.4 | Specifieke aangiften, gemeenschappelijke bewaarplicht |
| `voorafgaande-beslissing-dvb` | PO 2.1 · 2.3 | Rechtszekerheidsinstrument vóór de procedure begint |
| `fiscale-controle` | PO 2.4 | Btw eigen controle-regime art. 60-63 WBTW |
| `beginselen-behoorlijk-bestuur` | PO 2.1 | Algemene beginselen — hier processueel toegepast |
| `fiscale-bewijsmiddelen` | PO 2.2 · 2.3 | Tekenen en indiciën + AAMB als herkwalificatie |
| `fiscale-sancties` | PO 2.2 · 2.3 · 2.4 | Administratieve boetes + belastingverhogingen per wetboek |
| `geheime-commissielonen` | PO 2.3 | Bijzondere aanslag 100% — hier alleen procedureel raakvlak |
| `invorderingsprocedure` | PO 2.7 (Vlabel/lokaal) · PO 2.6 (registratie/successie) | Gewest-eigen invordering loopt parallel |

---

## 6. Voorbeeldgroep

### Voorstel: **één centrale procedure-cliënt + dossier-timeline** — analoog aan Aurelia voor PO 1.4, maar in procedure-vorm

PO 2.5 is **wel** een PO waar één doorlopende cliënt-case meerwaarde heeft (in tegenstelling tot PO 2.7 waar ik geen centrale mock aanbeval). **Reden**: fiscale procedure is een **timeline-vak** — dezelfde aanslag doorloopt fase na fase. Een gedeelde cliënt + één lopend fiscaal dossier laat de stagiair zien hoe de fases **aan elkaar geketend** zijn.

**Voorgestelde mock-case**: **BV De Vlieg & Partners** (een fictieve KMO-accountantsbeoefenaar of bouwbedrijf), eigenaar zaakvoerder Liesbeth Vandevoorde. Aanslagjaar 2024 (boekjaar 2023):
- Aangifte VenB tijdig ingediend in september 2024 (uiterste indieningsdatum)
- Februari 2025: vraag om inlichtingen art. 316 over een specifieke kostenpost (bv. een gebouw-bouw met privé-gebruik) — antwoord binnen 1 maand → leerstuk 2
- April 2025: bericht van wijziging art. 346 — voorgenomen verwerping van 80.000 EUR kosten → leerstuk 3 scharniermoment
- Mei 2025: gemotiveerd antwoord namens cliënt (gedeeltelijke aanvaarding)
- Juli 2025: aanslagbiljet vestigt 50.000 EUR rechtzetting + 50% belastingverhoging → leerstuk 4
- Augustus 2025: bezwaar bij gewestelijke directeur — termijn 1 jaar vanaf 3e werkdag na verzending
- November 2025: aanvraag fiscale bemiddeling FBD parallel — schorst beroepstermijn naar rechtbank
- Januari 2026: directeur-beslissing afwijzend → vordering bij rechtbank van eerste aanleg fiscale kamer binnen 3 maanden
- Parallel: ontvanger eist betaling onbetwist deel — bezwaar schorst NIET; bewarend beslag op rekening cliënt → leerstuk 5

**Voordelen** van deze case-vorm:
1. **Eén dossier-tijdlijn** waarin elke leerstuk zijn eigen episode krijgt — herkenningseffect doorheen het PO
2. **Realistisch** — past bij een gemiddeld accountantsdossier, geen extreme fraude-zaak
3. **Cijfer-arm** — focus op proces, niet op grote bedragen; de 80.000 EUR is grootteorde, niet de kern
4. **Geeft de stagiair een aanknopingspunt** voor de samenvatting (één timeline-diagram met De Vlieg als anker) en voor de oefening (verlenging van de timeline met een nieuwe wending — bv. een tweede aanslagjaar in fraude-traject)

**Alternatief om te overwegen**: twee parallel-cliënten (één PB-natuurlijke persoon met emigratie-thema; één VenB-vennootschap met controle-thema). Voordeel: dekt beide aangifte-vormen. Nadeel: dubbele bestandsovereenkomst nodig, en doorlopende-timeline-effect zwakker. **Mijn aanbeveling**: één centrale case (De Vlieg & Partners) + eventueel een korte secundaire mini-case voor de PB-emigratie-vraag (art. 309 WIB) in leerstuk 1 of de samenvatting.

**Locatie**: `data/voorbeeldgroepen/de-vlieg-en-partners.yaml`. **Datastructuur**: bedrijfs-identiteit + jaarrekening 2023 (samenvattend) + procedure-timeline (datum + handeling + correspondentie-stuk) + bedragen voor BvW-rechtzetting + bezwaar-grieven.

### Cijferzakboekje-strategie

Anders dan PO 2.7 leunt PO 2.5 **minder zwaar op cijfers** — termijnen (3/4/6/10 jaar; 1 maand; 1 jaar; 24 maanden) zijn de centrale getallen, en die staan **niet in het Cijferzakboekje** (zitten in WIB92 / WBTW zelf). Sancties (art. 444 + 445 WIB) hebben Cijferzakboekje-tarieven (KB 27 augustus 1993 voor belastingverhoging-schaal). Bij scripts-fase: alle sanctie-tarieven via MCP `certificaid-tarieven` opvragen. Termijn-cijfers rechtstreeks uit wetstekst.

---

## 7. Themafiche-mapping en samenvatting

Volgens [ADR-039](adr/ADR-039-samenvatting-vervangt-themafiche.md): één PO-samenvatting per programmaonderdeel vervangt de cluster-themafiches.

### Vier bestaande themafiches → één samenvatting

Bestand: `data/samenvattingen/2-5.yaml` + `content/studiemateriaal/2-5/samenvatting.md`.

**Migratie-strategie**:

| Themafiche | Inhoud | Migreert naar samenvatting als |
|---|---|---|
| `fiscale-termijnen.md` | Aanslagtermijnen (3/4/6/10 jaar) · onderzoekstermijn = aanslagtermijn · bezwaartermijn · btw 3/4/7 · invordering 5 jaar | **Blok 1**: termijnen-tabel (centraal — meest examen-relevant) |
| `taxatieprocedure.md` | Drie fasen flow · vraag om inlichtingen · BvW · ambtshalve aanslag · privéwoning vs beroepslokalen | **Blok 2**: mermaid-flow taxatie + tabel-blok voor de 3 onderzoeksinstrumenten |
| `bezwaar-en-gerechtelijke-fase.md` | Bezwaartermijn-vergelijking PB/btw/Vlabel · bezwaar-form · FBD · rechtbank-cascade | **Blok 3**: tabel bezwaartermijnen + mermaid-cascade administratief→gerechtelijk |
| `invordering-en-dwangbevel.md` | Invorderingscyclus · drie beslagtypes · verzet · hoofdelijkheid bestuurder · stuiting | **Blok 4**: mermaid-cyclus invordering + tabel beslagtypes + onderscheid bezwaar/verzet |

**Voorgestelde samenvatting-structuur** (2-4 A4 printbaar, visueel-dominant per ADR-039):

1. Intro-callout (no-print)
2. Take-away: 5 bullets (drie fases timeline · termijntabel als hart · BvW-scharniermoment · bezwaar ≠ verzet · onderzoeksgrenzen)
3. **Timeline-diagram** "Aangifte → controle → taxatie → bezwaar → rechter → invordering" (mermaid)
4. **Termijn-tabel** (groot blok) — direct vs btw vs invordering vs bezwaar
5. **Onderzoeksbevoegdheden-tabel** — art. 315/316/319/322/322bis/333 — wat, termijn, grens, gevolg bij weigering
6. **BvW-flow** (mermaid) — vraag → antwoord → akkoord/BvW/ambtshalve
7. **Bezwaar-cascade** (mermaid) — directeur → FBD (schorst beroepstermijn) → rechtbank → hoger beroep → cassatie
8. **Invorderings-cyclus** (mermaid) — minnelijk → dwangbevel → bewarend/uitvoerend/derden-beslag → verzet bij beslagrechter
9. Valkuilen (bezwaartermijn vanaf 3e werkdag, niet vanaf datum biljet · 1 maand antwoord BvW ≠ 1 jaar bezwaar · btw geen 10 jaar · vraag aan derden geen wettelijke termijn · privéwoning gerechtelijk machtiging)
10. Verdieping (no-print): doorklik naar 5 leerstukken

**De vier themafiches** worden bij voltooien van de samenvatting **gearchiveerd** (verplaatsen naar `content/themafiches/archive/po-2-5/` — open vraag, zie §9.6).

---

## 8. Oefening

### Past een 60-75 min oefening bij dit PO?

**Ja — sterk aanbevolen**, in het format van een **fiscaal procedure-dossier** met de De Vlieg-case als drager.

**Verschilpunt met PO 2.7**: waar PO 2.7 een multi-case-dossier nodig had (vier onafhankelijke fiscale puzzels), heeft PO 2.5 net **één lange procedurele draad** — en die past perfect bij het oefening-format van PO 1.4 (Nordica-consolideren). De stagiair doorloopt dezelfde aanslag stap voor stap.

**Voorstel: oefening als "fiscaal dossier De Vlieg & Partners — twaalf maanden in een aanslag"**

Format: één cliënt + één aanslagjaar + één lopend dossier; 5 deelvragen die parallel met de 5 leerstukken lopen. Elke vraag vertrekt vanuit een briefje, document of e-mail dat de stagiair ontvangt — geen hints in opgave.

- **Document 1** (leerstuk 1+2): Aangiftekopie + bevestiging tijdige indiening + 6 maanden later: vraag om inlichtingen ontvangen. **Vraag**: identificeer (a) welke termijn loopt voor antwoord, (b) wat de gevolgen zijn van niet-antwoorden, (c) of de vraag ook van toepassing is op de aankoopfacturen 2021 (5 jaar terug).
- **Document 2** (leerstuk 2): Antwoord van cliënt → bericht van wijziging ontvangen met motivering. **Vraag**: (a) is de motivering toereikend? (toets aan zorgvuldigheid + redelijkheid); (b) waar zou je een aanslag van ambtswege voor vrezen? (c) verlenging van 6 maanden — voor wie is die er, en wanneer?
- **Document 3** (leerstuk 3): Aanslagbiljet ontvangen met rechtzetting + 50% belastingverhoging. **Vraag**: (a) hoeveel tijd heb je voor bezwaar en wanneer start die termijn precies? (b) moet je betalen tijdens bezwaar?
- **Document 4** (leerstuk 4): Directeur-beslissing afwijzend ontvangen, en parallel een vraag van cliënt over fiscale bemiddeling. **Vraag**: (a) is bemiddeling nog nuttig?; (b) wat is de termijn naar de rechtbank en wat is het gevolg van een FBD-aanvraag?
- **Document 5** (leerstuk 5): Tijdens bezwaar krijgt cliënt brief van ontvanger met **dwangbevel**. **Vraag**: (a) is dat regelmatig?; (b) welk rechtsmiddel — bezwaar of verzet — en bij welke rechter?; (c) wat is het verschil in schorsende werking?

**Tijdbudget**: 75 minuten — 15 min per vraag. **Geen hints in opgave** (per oefening-procedure ADR-038). Modelantwoord apart in tweede markdown — per vraag de juiste termijn + de juiste artikelverwijzing + één veelvoorkomende valkuil.

**Niet-doelstelling**: geen volledige bezwaarschrift schrijven, geen rechtspraak-analyse, geen complexe AAMB-redenering — die horen bij PO 2.1 of bij de geavanceerde varianten.

---

## 9. Open vragen voor sparring

1. **Voorbeeldgroep — bevestiging "De Vlieg & Partners als centrale case"?**
   - Voorstel: één doorlopend KMO-procedure-dossier dat alle 5 leerstukken raakt + de oefening drijft.
   - Alternatief: één PB-natuurlijke persoon + één VenB-vennootschap, twee parallel-cases.
   - Beslissing nodig voor: aanmaak `data/voorbeeldgroepen/de-vlieg-en-partners.yaml` of een ander dossier-naam.

2. **Leerstuk-aantal — 5 of 4?**
   - 5 zoals voorgesteld (entry · controle+bewijs · taxatie+BvW · bezwaar+bemid+gerecht · invordering).
   - Alternatief 4: leerstuk 1 (entry) integreren in leerstuk 2 (controle+bewijs), startend met timeline-tabel. Risico: leerstuk 2 wordt nog zwaarder (al de zwaarste), en de stagiair mist een snelle-instap.
   - Alternatief 6: leerstuk 3 (taxatie+BvW) splitsen in "taxatie" + "bericht van wijziging". Risico: de BvW is precies hét scharniermoment waaraan de taxatieprocedure haar pedagogische waarde ontleent — splitsen zou een dun BvW-leerstuk maken.

3. **Beginselen van behoorlijk bestuur — transversaal of eigen leerstuk?**
   - Voorstel: **transversaal** — in elk leerstuk een blok "Beginselen-haakjes" waar relevant (motivering BvW in leerstuk 3, zorgvuldigheid + redelijkheid in leerstuk 2, redelijkheid bij sanctie in leerstuk 3, reformatio in pejus in leerstuk 4).
   - Alternatief: eigen leerstuk 6 "Beginselen van behoorlijk bestuur in de fiscale procedure". Risico: abstract verhaal zonder klant-scenario, en de beginselen worden net door **toepassing** in concrete situaties duidelijk.
   - Cross-PO: in PO 2.1 leven de **algemene** fiscale beginselen (legaliteit, gelijkheid, non-bis-in-idem) — niet dezelfde lijst als de beginselen behoorlijk bestuur. Helder afgrenzen.

4. **Examen-vragen-tagging** — moeten de aangifte-PB-bij-vertrek-vraag (art. 309) en de aangifte-VenB-termijn-vraag (art. 310) onder PO 2.5 blijven, of naar PO 2.2/2.3?
   - Voorstel: blijven onder PO 2.5 — examen-thema is **proceduratief** (termijn + uiterste datum), niet de PB/VenB-inhoud zelf. Cross-PO doorklik volstaat.
   - Alternatief: bij PO 2.5 + PO 2.2/2.3 tagging — verschijnt dan in beide voorbeeldexamen-paginas.

5. **Bezwaartermijn — concept-record `bezwaarprocedure` correctie**
   - ⚠️ huidige record vermeldt "6 maanden", maar art. 371 WIB92 zegt **1 jaar**. Bestaand `index.md` PO 2.5 + voorbeeldexamenvragen 2024-1 + RAG-verificatie bevestigen 1 jaar.
   - Voorstel: in scripts-fase eerst `claims_checken` operatie draaien op `bezwaarprocedure` om dit te corrigeren — vóór leerstuk 4 wordt geschreven.
   - Mogelijke verklaring stale: oude versie van art. 371 (vóór wetshervorming) vermeldde 6 maanden. Bij verificatie nakijken welke datum-versie.

6. **Themafiches archiveren — wanneer + waarheen?**
   - Voorstel: bij voltooien samenvatting → verplaatsen naar `content/themafiches/archive/po-2-5/`. Niet meer in explorer, maar leesbaar als historische bron.
   - 4 themafiches: `taxatieprocedure.md` · `bezwaar-en-gerechtelijke-fase.md` · `invordering-en-dwangbevel.md` · `fiscale-termijnen.md`.
   - Bij ADR-039 amendement-overleg expliciet bevestigen.

7. **Bewaarplicht — cross-PO afspraak met PO 1.2 (boekhoudrecht)**
   - WER art. III.86 (7 jaar boekhoudkundig) + WIB art. 315 (10 jaar fiscaal sinds aj. 2023) + W.Btw art. 60 (10 jaar) leven in verschillende PO's.
   - Voorstel: leerstuk 2 PO 2.5 noemt **alle drie de termijnen** in één tabel en linkt naar PO 1.2 voor boekhoudrechtelijke nuancering. Bij PO 1.2-leerpad: spiegelverwijzing.
   - Risico: dubbelwerk indien PO 1.2 ook een bewaarplicht-leerstuk heeft. Coördinatie nodig.

8. **Aanslagtermijnen — Wet 20-11-2022 als breekpunt**
   - Voorstel: studiemateriaal vertrekt vanuit de **nieuwe regels** (3/4/6/10 jaar sinds aj. 2023) en vermeldt oude regels (3/7/7) alleen als "voor aanslagjaren ≤ aj. 2022".
   - Examen 2024-1 toetst de nieuwe regels; 2013-2015 examens nog de oude. Bij modelantwoord op oudere vragen: oude regel correct toepassen, nieuwe regel vermelden als update-noot.

9. **Rechtspraak-laag — verplichten in elk leerstuk?**
   - Het programma noemt "rechtspraak" niet expliciet bij kenniselementen, anders dan in PO 2.7. Maar in praktijk: beginselen van behoorlijk bestuur leven grotendeels via Cassatie-rechtspraak; AAMB heeft sleutel-arresten; verjaring-discussies leiden tot rechterlijke uitspraken.
   - Voorstel: scripts-fase **mag** waar zinvol een klassiek arrest noemen (bv. Cassatie-arrest over voorafgaande kennisgeving fraude; Brepols als verre achtergrond bij AAMB-doorklik) — maar **niet verplichten**. Geen aparte rechtspraak-blok per leerstuk.

10. **Cross-PO termijnen-tabel — waar leeft "de" termijnen-tabel?**
    - Klassieke examen-stof: bezwaartermijn-verschillen tussen federaal (1 jaar PB/VenB), btw (3 maanden), Vlabel (3 maanden), gemeentebelasting (3 maanden, in reglement vastgelegd).
    - Voorstel: PO 2.5 samenvatting heeft een **federale termijnen-tabel** (PB/VenB + btw verjaring + invordering); PO 2.7 samenvatting heeft de **regionale/lokale termijnen-tabel**; beide samenvattingen hebben een korte cross-PO-doorklik. Risico: stagiair die alleen PO 2.5 ziet, mist het Vlabel-bezwaar (3 maanden). Compromis: PO 2.5 noemt **kort** de gewest-termijnen in een "Niet-federale variaties"-rij en linkt naar [[2.7]].

---

## 10. Rapport

- **5 leerstukken voorgesteld**: entry+timeline · controle+onderzoek+bewijs · taxatie+BvW+ambtshalve · bezwaar+bemiddeling+gerechtelijk · invordering+verzet.
- **Hoofdtaak**: 2.5.taak.3 (bijstaan bij fiscale verplichtingen) + 2.5.taak.4 (vertegenwoordigen) — niveau **integratie** (hoogste). De eigenheid van PO 2.5 ten opzichte van andere fiscale PO's zit in **taak 4 + doelstelling 3.2** (geavanceerde procedure-concepten op complexe gevallen).
- **Gaten t.o.v. programma**: geen kritieke. Eén bewust niet-uitgewerkte taak (2.5.1 oprichting-begeleiding — generieke cross-PO-formulering zonder eigen kenniselementen). Eén stale concept-record-claim te corrigeren vóór scripts-fase: `bezwaarprocedure` zegt "6 maanden" — moet "1 jaar" zijn (art. 371 WIB92).
- **Voorbeeldgroep**: **wel** aanbevolen — één doorlopende procedure-cliënt "BV De Vlieg & Partners" met aanslagjaar-timeline van aangifte tot dwangbevel. Past natuurlijk bij het timeline-karakter van het PO (in tegenstelling tot PO 2.7 waar losse mini-cases beter werkten).
- **Themafiche-migratie**: vier bestaande themafiches (`taxatieprocedure` · `bezwaar-en-gerechtelijke-fase` · `invordering-en-dwangbevel` · `fiscale-termijnen`) integreren in één samenvatting volgens ADR-039. Termijnen-tabel wordt centrale blok.
- **Oefening**: aanbevolen — fiscaal procedure-dossier "De Vlieg & Partners — twaalf maanden in een aanslag" met 5 documenten (één per leerstuk) en ~75 min tijdbudget.
- **Belangrijkste onzekerheid**: (a) of beginselen behoorlijk bestuur transversaal blijft of een eigen leerstuk verdient; (b) of de aangifte-cross-PO-vragen (art. 309 PB-emigratie, art. 310 VenB-termijn) onder PO 2.5 blijven of mede-getagd worden naar PO 2.2/2.3.
- **Volgende stap**: sparring met mens → beslissingen rond voorbeeldgroep-vorm + beginselen-laag + concept-record correctie `bezwaarprocedure` → één Opus-run voor alle 5 leerstuk-scripts (ADR-037 amendement B) + samenvatting-YAML uit themafiche-inhoud + oefening-YAML.
