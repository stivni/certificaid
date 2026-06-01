---
title: "Hoe scheidt men onverenigbare functies en welke taxonomieën classificeren controlemaatregelen?"
description: "Leerstuk PO 1.7 — techniek. Drie taxonomieën die elk examen toetst: 5 controletechnische functies (BURCB), 4-categorieën-typologie (Aut · Bew · Reg · Contr), karakter-driehoek preventief/detectief/correctief. Plus accountingcontrole vs administratieve controle en KMO-compensaties."
explorer_title: "2. Functiescheiding"
tags:
  - leerstuk
  - po-1.7
  - cluster-interne-controle
---

<div class="no-print">

> **Leerstuk — één vraag, helemaal doorgewerkt.** Dit is het denkmotor-leerstuk van PO 1.7 — de drie taxonomieën hier worden hergebruikt in [[cyclus-analyse-en-controlemiddelen]] (controle-architectuur per cyclus) en in [[fouten-fraude-en-risicobeheersing]] (functiescheidings-doorbraak als fraudemechanisme). Lees vooraf [[wat-is-interne-controle-en-coso]] dat het COSO-kader plaatst. Voor verhaal en routekaart: [[studiemateriaal/1-7|overzicht PO 1.7]].

</div>

## Antwoord in één blik

Functiescheiding is het organisatorisch principe dat **onverenigbare functies aan verschillende personen** worden toegewezen — zodat geen enkele persoon alleen een volledige transactie kan initiëren, uitvoeren, registreren en bewaren. Het doel is dubbel: voorkomen dat iemand fouten maakt **en** verhult, of fraude pleegt **en** verhult. Eén persoon mag mogelijk een fout maken (menselijk), maar moet die fout niet kunnen wegmoffelen zonder dat een ander het ziet.

Drie taxonomieën gebruikt het examen door elkaar — je moet ze alle drie beheersen. De eerste is de klassieke Belgische **vijf controletechnische functies** met het ezelsbruggetje BURCB: Beschikken · Uitvoeren · Registreren · Controleren · Bewaren. Vuistregel: één persoon mag maximaal twee niet-aangrenzende functies cumuleren. De tweede is de **4-categorieën-typologie** uit COSO/IIA-traditie: 1 Autorisatie · 2 Bewaring van activa · 3 Registratie en rapportering · 4 Controleprocedures — typisch gebruikt in de kruisjes-classificatievragen. De derde is de **karakter-driehoek**: preventief (vóór het feit), detectief of repressief (na het feit), correctief (herstel plus structurele aanpassing). Daarnaast onderscheid je nog accountingcontrole (output — de boekhouding zelf) van administratieve controle (proces — de weg ernaartoe).

In een KMO als Bracke is volledige functiescheiding zelden haalbaar — de staf is te beperkt. De juiste examen-reflex is **niet** "geen functiescheiding mogelijk", wel "beperkte functiescheiding moet worden gecompenseerd". Direct toezicht door de zaakvoerder, periodieke roulatie en steekproefcontroles vullen het gat. De internationale audit-standaarden erkennen die compensatie uitdrukkelijk voor minder complexe entiteiten.

### Vier taxonomieën in één tabel

| Taxonomie | Categorieën / functies | Examen-gebruik |
|---|---|---|
| **5 functies (BURCB)** | Beschikken · Uitvoeren · Registreren · Controleren · Bewaren | "Stel procedure op met minimaal 2 functiescheidingen" |
| **4 categorieën** | 1 Autorisatie · 2 Bewaring activa · 3 Registratie · 4 Controleprocedures | "Classificeer deze activiteiten" (kruisjes-vraag) |
| **Karakter-driehoek** | Preventief · Detectief (repressief) · Correctief | "Classificeer deze maatregelen" (kruisjes-vraag) |
| **Accounting vs administratief** | Accountingcontrole (boekhouding-output) · Administratieve controle (proces-input) | Begripsverklaring + voorbeelden |

We werken de drie hoofd-taxonomieën één voor één uit met voorbeelden uit de Bracke-aankoopcyclus. Daarna het bonus-onderscheid accountingcontrole versus administratieve controle (Starreveld-traditie). Tot slot: hoe een KMO als Bracke onvermijdelijke functiescheidings-gaten opvangt.

---

## Het principe — waarom functies scheiden?

De fundamentele logica is enkel: één persoon die alle stappen van een transactie alleen kan zetten, kan een fout **maken** én die fout **verhullen** — of bewust frauderen en zijn spoor uitwissen. Functiescheiding doorbreekt die single-point-of-failure door verschillende handen te dwingen langs dezelfde transactie te passeren. Wie iets fout doet, wordt vroeg of laat opgemerkt door de volgende schakel.

De internationale audit-standaarden formuleren het doel scherp: functiescheiding is bedoeld om beperkingen aan te brengen in de mogelijkheden voor wie dan ook om bij de uitoefening van zijn normale taken fouten te maken **en te verhullen**, of fraude te plegen **en te verhullen**. Twee werkwoorden zijn essentieel — maken én verhullen. De klassieke driedeling van onverenigbare verantwoordelijkheden volgt direct uit die formulering: het **autoriseren** van transacties, het **vastleggen** ervan en het **bewaren** van activa horen niet bij dezelfde persoon. Een manager die kredietverkopen autoriseert, mag niet ook debiteurenrekeningen bijhouden of contante betalingen afhandelen — anders kan hij een fictieve verkoop creëren die onopgemerkt blijft.

De Bracke-fraude-case maakt dit pijnlijk concreet. Bart Devlieger, werfleider sanitair, kon over veertien maanden 47.300 EUR via fictieve facturen wegsluizen omdat één gebundelde zwakte het mogelijk maakte. Hoofdboekhouder Eline had simultane rechten op **leveranciers-master** + **factuur-boeking** + **betaalbatch-aanmaak**. Bart vroeg haar een nieuwe leverancier aan te maken (de BV van zijn schoonbroer) "voor een eenmalige levering" — Eline deed dit zonder verificatie. Daarna leverde Bart valse bestelaanvragen onder de drempel van 5.000 EUR (geen Pieter-goedkeuring) en valse ontvangstbewijzen (geen onafhankelijke ontvangst-controle door magazijnier Davy, want werfleveringen passeren het magazijn niet). Resultaat: de 3-way match sloot formeel, Eline boekte, Eline gaf de betaalbatch vrij onder 10.000 EUR (geen tweede handtekening), de schoonbroer-BV ontving het geld en storteerde door. Eén persoon met de complete keten in handen is een fraude-vehikel par excellence.

Plaats dit in het COSO-kader uit het vorige leerstuk: functiescheiding valt onder de component **controleactiviteiten**, en haar karakter is **preventief** — ze plaatst zich vóór een mogelijk incident op het transactiepad. De drie taxonomieën hieronder zijn de drie lenzen waarmee je elke controle classificeert.

---

## Taxonomie 1 — de 5 controletechnische functies (BURCB)

De Belgische beroepsleer (Starreveld-traditie, ITAA-doctrine) bouwt op een vijfdeling. Elke volledige transactie omvat vijf onderscheiden functies, samen te vatten in het ezelsbruggetje **BURCB**: Beschikken · Uitvoeren · Registreren · Controleren · Bewaren. De vijf functies zijn niet stadia in de tijd maar **rollen** rond een transactie — sommige lopen parallel, sommige volgen elkaar op.

**Beschikken** is de beslissingsbevoegdheid: iemand met mandaat zegt "we kopen deze HVAC-units" of "we keuren deze bestelaanvraag goed". Strategisch-managerial. **Uitvoeren** is de feitelijke handeling stellen: de bestelling daadwerkelijk plaatsen bij de leverancier, de dienst verrichten, de levering uitvoeren. Operationeel. **Registreren** is de boeking in de administratie: factuur inboeken, magazijnbon ingeven, urenregistratie verwerken. Administratief. **Controleren** is een **onafhankelijke check** op één van de andere functies: een 3-way match-review, een kascontrole door iemand die zelf geen kasbeheerder is, een reconciliatie tussen bank en grootboek. Toezichtsfunctie. **Bewaren** ten slotte is het fysieke of digitale beheer van activa: wie heeft de magazijnsleutel, wie heeft de bank-toegang via Isabel, wie houdt de kassleutel? Custody.

De vuistregel die het examen verwacht: één persoon mag **maximaal twee niet-aangrenzende functies** cumuleren. "Niet-aangrenzend" betekent dat ze niet naast elkaar in de transactieflow zitten. Drie klassieke onveilige combinaties moet je kunnen herkennen. **Beschikken + Bewaren** geeft autorisatie zonder onafhankelijke check op de feitelijke output — wie zowel beslist als bewaart, kan zichzelf de activa toe-eigenen. **Registreren + Bewaren** maakt eigen toe-eigening verbergbaar in de eigen administratie — Davy die zowel het magazijn fysiek beheert als de voorraadboekingen doet (Bracke-zwakte Z7) is hier het schoolvoorbeeld. **Beschikken + Uitvoeren** laat dezelfde persoon beslissen én uitvoeren zonder onafhankelijke ontvangst-check — werfleider Bart die zelf bestelt én zelf de ontvangst tekent.

Een schone Bracke-aankoopflow zou er als volgt uitzien: de werfleider **beschikt** (stelt een bestelaanvraag op), Pieter **autoriseert** boven 5.000 EUR, Nora **voert uit** (plaatst de bestelling), Davy **bewaart** (ontvangt in magazijn), Eline **registreert** (boekt de factuur), Sofie **controleert** (3-way match review plus tweede handtekening boven 10.000 EUR). Vijf functies verdeeld over vijf personen — geen Bracke-realiteit (de staf is te klein), wel het ideaal waartegen je elke afwijking afmeet.

| Functie (BURCB) | Wat houdt ze in? | Bracke-aankoop voorbeeld |
|---|---|---|
| **B — Beschikken** | Beslissingsbevoegdheid: "we kopen dit" | Werfleider stelt bestelaanvraag op; Pieter keurt goed > 5.000 EUR |
| **U — Uitvoeren** | Feitelijke handeling stellen | Nora plaatst de bestelling bij leverancier |
| **R — Registreren** | Boeking in administratie | Eline boekt factuur in Odoo |
| **C — Controleren** | Onafhankelijke check op andere functie | 3-way match review; tweede handtekening betaling |
| **B — Bewaren** | Fysiek / digitaal beheer activa | Davy bewaart magazijn; Eline beheert Isabel-toegang |

Hoe pas je dit toe op een klassieke examenvraag — "stel een procedure op met minimaal twee functiescheidingen", bijvoorbeeld voor de kleine-kas-procedure? Vier stappen. **Eén**: doorloop de transactie van begin tot eind. **Twee**: duid bij elke stap aan welke van de 5 functies actief is. **Drie**: wijs verschillende personen toe aan onverenigbare functies. **Vier**: check dat geen persoon meer dan twee niet-aangrenzende functies krijgt. In KMO-context vermeld je expliciet welke compenserende direct-toezicht-controle de zaakvoerder uitoefent waar functiescheiding niet volstaat — anders blijft het antwoord onvolledig.

---

## Taxonomie 2 — de 4-categorieën-typologie (1 Aut · 2 Bew · 3 Reg · 4 Contr)

De 4-categorieën-typologie is een andere manier om dezelfde transactieflow te lezen — typisch gebruikt in COSO- en IIA-context en in een specifieke vraag-traditie van de ITAA-examens (de "categorie 1-4"-classificatievraag dook expliciet op in 2013-2 en 2014-1). De stagiair moet beide typologieën beheersen, want het examen kiest soms de ene en soms de andere — en wie BURCB-functies in een 1234-vraag stopt, verliest punten.

De vier categorieën. **Autorisatie (1)** is het geven van toestemming om een transactie te starten of een masterdata-record aan te maken — niet de feitelijke handeling, wel de poortwachter. Pieter die de bestelling boven 5.000 EUR goedkeurt, Eline die een nieuwe leverancier in het systeem zet: beide zijn autorisatie. **Bewaring van activa (2)** is de feitelijke custody: wie heeft de magazijnsleutel, wie heeft de Isabel-toegang, wie geeft fysiek af? **Registratie en rapportering (3)** is de boeking in systemen plus de opmaak van rapporten, lijsten en betaalvoorstellen — de administratieve verwerking. **Controleprocedures (4)** zijn de detecterende controles: 3-way match, reconciliatie, review van een voorstel door een tweede persoon.

De mapping op de 5-functies-leer is bruikbaar als geheugensteun. Autorisatie komt overeen met **Beschikken**. Bewaring valt samen met **Bewaren**. Registratie dekt **Registreren** plus deels **Uitvoeren** (de uitvoerende administratieve handeling). Controleprocedures vallen onder **Controleren**. De 4-categorieën-typologie heeft minder granulariteit dan BURCB — ze legt geen apart accent op het verschil tussen beslissen en uitvoeren — maar is praktischer voor de klassieke kruisjes-classificatie-vraag.

De Bracke-aankoopcyclus levert acht concrete activiteiten op die je één voor één kan toewijzen — dit is exact het type kruisjes-vraag dat het examen stelt. De tabel hieronder is geen opdracht (de oefening zit in `oefening.md`) maar een doorgewerkte referentie.

| Activiteit Bracke aankoopcyclus | Categorie |
|---|---|
| Goedkeuring bestelling > 5.000 EUR door Pieter | **1 — Autorisatie** |
| Ontvangst HVAC-units door Davy in magazijn | **2 — Bewaring activa** |
| Inboeken factuur Vaillant door Eline | **3 — Registratie en rapportering** |
| 3-way match controle door Eline (bestelbon ↔ ontvangstbon ↔ factuur) | **4 — Controleprocedures** |
| Aanmaak wekelijkse betaalbatch door Eline | **3 — Registratie en rapportering** |
| Goedkeuring betaalbatch > 10.000 EUR door Sofie | **4 — Controleprocedures** |
| Uitvoering bankbetaling via Isabel 6 | **2 — Bewaring activa** |
| Aanmaak nieuwe leverancier in Odoo door Eline | **1 — Autorisatie** |

De examen-formule voor classificatie-vragen is een korte zelf-test per activiteit: **wie geeft hier toestemming (1), wie houdt iets fysiek (2), wie schrijft iets op (3), wie kijkt na wat een ander deed (4)?** Eén-na-één-toepassing voorkomt dat je categorieën door elkaar haspelt. Let op de subtiliteiten: een betaalbatch *aanmaken* (selectie van te betalen facturen) is registratie — een betaalbatch *goedkeuren* is controleprocedure. Dezelfde persoon mag beide niet doen — daarom verdeel je het over Eline en Sofie.

---

## Taxonomie 3 — karakter-driehoek preventief · detectief · correctief

Controles kunnen niet alleen naar functie geclassificeerd worden, maar ook naar het **tijdstip waarop ze werken** ten opzichte van een mogelijk incident. Deze derde taxonomie keert systematisch terug op het examen.

**Preventief** voorkomt incidenten **vóór** ze gebeuren — de controle plaatst zich op het transactiepad als poortwachter. Functiescheiding zelf is preventief: ze verhindert dat één persoon alleen kan frauderen. Andere voorbeelden bij Bracke: de autorisatiedrempel van 5.000 EUR die elke bestelling boven dat bedrag blokkeert zonder Pieter, de Odoo-validatieregel die een factuur weigert wanneer ze meer dan 2 % afwijkt van de bestelbon, de toegangsbeveiliging op het magazijn (alleen Davy heeft sleutel en Odoo-rechten — al is dat juist daarom ook een Z7-zwakte).

**Detectief** of **repressief** signaleert incidenten **nadat** ze gebeurd zijn, zodat ze gecorrigeerd kunnen worden. De controle staat naast het transactiepad en kijkt periodiek wat er fout ging. Bracke-voorbeelden: de maandelijkse bank-reconciliatie door Eline (saldo grootboek versus uittreksel), de cyclische voorraadtelling twee keer per jaar (juni en december), het exceptie-rapport prijswijzigingen boven 3 %, de jaarlijkse externe samenstelling door de confrater-accountant. Detectieve controles ontdekken het incident — ze voorkomen het niet.

**Correctief** herstelt na een vastgesteld incident **én** past het systeem aan om herhaling te voorkomen. Het is geen passieve registratie van wat er fout ging maar een actieve interventie. Na het Bart-incident bij Bracke betekende dit: drempel-aanpassing (goedkeuring bestelling van 5.000 EUR naar 2.500 EUR, tweede handtekening van 10.000 EUR naar 5.000 EUR), Odoo-rolherinrichting (Eline verliest leveranciers-master-rechten — alleen Pieter of Sofie kan nog masterdata wijzigen), introductie van een periodieke spend-analyse top-20-leveranciers. De correctieve controle sluit de feedback-loop.

De drie karaktertypes zijn **complementair, niet alternatief**. Alleen preventief vertrouwen geeft een blinde vlek — wat als de control faalt of omzeild wordt? Alleen detectief vertrouwen betekent schade incasseren vóór correctie. Een sluitend IC-systeem heeft alle drie: preventief voorkomt, detectief vangt op wat er toch nog inglipt, correctief past het systeem aan op basis van wat detectief boven kwam. Bij Bracke werd de Bart-fraude pas na veertien maanden gedetecteerd — en dat alleen toevallig, omdat Eline tijdens de jaarafsluiting een leverancier opmerkte die niet in de offerte-database voorkwam. Sterkere preventieve **én** detectieve controles hadden de schade beperkt.

| Karakter | Tijdstip | Bracke-voorbeelden |
|---|---|---|
| **Preventief** | Vóór incident — blokkeert | Functiescheiding · 3-way match Odoo · autorisatie-drempels · toegangsbeveiliging magazijn |
| **Detectief (repressief)** | Na incident — signaleert | Bank-reconciliatie maandelijks · voorraadtelling 2× per jaar · externe samenstelling jaarlijks |
| **Correctief** | Na detectie — herstelt + past systeem aan | BTW-rechtzetting na klantenfiche-fout · drempelaanpassing en Odoo-rolherinrichting na Bart-incident |

> **Valkuil: telling versus correctieboeking.** Een fysieke voorraadtelling is **detectief** — ze stelt verschillen vast tussen het werkelijke en het geboekte aantal. De correctieboeking die op de telling volgt (boeken van het manco of het surplus) is **correctief** — ze herstelt het verschil in de boekhouding. Wie de telling en de boeking als één controle ziet, classificeert fout. Hetzelfde geldt voor een leverancier-saldoconfirmatie: de confirmatie zelf is detectief, de eventuele rechtzetting van de afwijking is correctief.

---

## Bonus-taxonomie — accountingcontrole versus administratieve controle

Een vierde examen-vraag-type onderscheidt **accountingcontrole** (boekhoudkundige controle) van **administratieve controle**. Het onderscheid komt uit de Starreveld-traditie en wordt in ITAA-context ondersteund door de internationale audit-standaarden over interne beheersing. Het is geen aparte taxonomie van controle-types in dezelfde zin als de drie hierboven — wel een onderscheid op basis van **wat** gecontroleerd wordt.

**Accountingcontrole** bewaakt de juistheid, volledigheid en tijdigheid van de boekhouding zelf — alle controles die zorgen dat transacties correct in de boeken belanden. Ze richt zich op de **output**: de boekhouding als eindproduct. Bracke-voorbeelden: de maandelijkse bank-grootboekreconciliatie (saldo 550 versus Isabel-uittreksel), de aansluitingscontrole klanten-grootboek met individuele klantfiches, de jaarlijkse voorraadtelling met aansluiting magazijnboek, de cut-off-controle bij jaareinde.

**Administratieve controle** bewaakt de rechtmatigheid, doelmatigheid en betrouwbaarheid van de administratieve **processen** — autorisaties, functiescheiding, procedure-naleving — **vóór** ze de boekhouding bereiken. Ze richt zich op de **weg naar de boekhouding toe**. Bracke-voorbeelden: de 3-way match in de aankoopcyclus vóór betaling, de autorisatiematrix met de drempel van 5.000 EUR door Pieter, de functiescheiding tussen leverancier-aanmaak en betalingsuitvoering, de vier-ogen op contracten met top-klanten.

De scherpe stelling: het onderscheid gaat over **wat** wordt gecontroleerd, niet **wanneer**. Accountingcontrole controleert de boeken (output); administratieve controle controleert het proces (de weg ernaartoe). Een goed IC-systeem heeft beide nodig — administratieve controle voorkomt dat fouten ontstaan, accountingcontrole detecteert wat toch nog inglipt. Wie alleen op administratieve controle vertrouwt, gaat ervan uit dat alle procedures perfect werken; wie alleen op accountingcontrole vertrouwt, accepteert dat fouten eerst de boekhouding moeten bereiken voor ze worden ontdekt. Beide blinde vlekken zijn onnodig.

---

## KMO-realiteit — compenseren als functiescheiding niet haalbaar is

Een Bracke met 32 medewerkers kan geen vijf personen op een aankoopflow zetten. Hoofdboekhouder Eline doet noodzakelijkerwijs meer dan alleen registreren — anders zou je vier extra functies-houders moeten aanwerven voor één cyclus. Bij beperkte staf moet je **andere** controles inzetten om hetzelfde doel (geen single-point-of-failure) te bereiken. De internationale audit-standaarden erkennen dit uitdrukkelijk: het is minder praktisch uitvoerbaar om functiescheiding in minder complexe entiteiten met minder medewerkers tot stand te brengen, maar in een door de eigenaar bestuurde entiteit kan de eigenaar-bestuurder via directe betrokkenheid effectief toezicht uitoefenen — wat de beperktere mogelijkheden voor functiescheiding kan compenseren.

Drie KMO-compensaties hoor je systematisch in te zetten. **Direct toezicht door de zaakvoerder** is de eerste — parafeer alle onkostennota's, doe zelf de periodieke kascontrole, valideer alle nieuwe leveranciers boven een bepaalde drempel, review de wekelijkse spend-rapporten. Pieter die zichtbaar aanwezig is op kantoor en de tone at the top zet. **Roulatie** is de tweede — laat verschillende personen periodiek elkaars taken doen (bijvoorbeeld wekelijks een andere persoon voor de bank-reconciliatie, of voor de kascontrole). Roulatie detecteert verbergende patronen: wie iets stelselmatig wil verhullen, slaagt minder makkelijk als de takenverdeling beweegt. **Steekproefcontroles** zijn de derde — de zaakvoerder controleert ad-hoc fraudegevoelige activiteiten: een periodieke spend-analyse top-20-leveranciers, een sample-check op nieuwe klantenfiches, een spot-check op manuele journaalposten.

> **Maar wie controleert de controleur?** Bij Bracke doet Pieter wel direct toezicht — hij is bedrijfsleider, zichtbaar aanwezig, parafeert. Tegelijk is hij **zelf uitvoerder** van bepaalde controles: alle cash-stortingen bij de bank gebeuren door hem alleen, één keer per twee weken, zonder tweede paar ogen op de samengetelde envelopinhoud (Bracke-zwakte Z11). Direct toezicht door iemand die zelf niet onder toezicht staat, opent een nieuw risico: **management-override**. Echte vier-ogen vereist dat de zaakvoerder zelf onder review staat — bijvoorbeeld door de externe accountant in een vrijwillige review-opdracht, of door de mede-zaakvoerder (Sofie tegenover Pieter en omgekeerd). Compenserende controles compenseren alleen als ze zelf gedekt zijn.

De klassieke examen-formule die je moet kunnen reproduceren: **beperkte functiescheiding ⇒ compenseren via direct toezicht plus roulatie plus steekproef**. Het antwoord "er is geen functiescheiding mogelijk in een KMO, dus geen interne controle" is altijd fout. Het juiste antwoord begint met de vaststelling dat de functiescheiding beperkt is — en sluit af met een concreet voorstel van compenserende controles, telkens benoemd met de naam van de verantwoordelijke (zaakvoerder, externe accountant, een tweede medewerker). Een verwijzing naar de erkenning in de internationale audit-standaard versterkt het antwoord, maar mag de concretisering niet vervangen.

---

## Drie valkuilen

> **Valkuil 1 — taxonomieën door elkaar gebruiken.** De 5-functies-leer (BURCB) en de 4-categorieën-typologie zijn twee aparte lenzen op dezelfde realiteit. Het examen specificeert welke taxonomie gevraagd wordt — lees de vraag zorgvuldig. "Stel een procedure op met minimaal twee functiescheidingen" vraagt BURCB. "Classificeer deze activiteiten naar categorie 1-4" vraagt de 4-categorieën-typologie. Wie BURCB-functies in een 1234-vraag stopt of omgekeerd, verliest punten — zelfs als de inhoudelijke redenering klopt.

> **Valkuil 2 — preventief en detectief verwarren.** Functiescheiding zelf is preventief: ze voorkomt dat één persoon alleen kan frauderen. Een fysieke inventarisatie is detectief: ze signaleert verschillen achteraf. Een leverancier-saldoconfirmatie is detectief: ze verifieert achteraf. ICT-toegangsbeveiliging is preventief: ze blokkeert ongeautoriseerde acties. De tijdslijn ten opzichte van het incident bepaalt de classificatie — niet of de controle "streng" of "soft" voelt.

> **Valkuil 3 — "geen functiescheiding mogelijk in KMO" als excuus.** Dit antwoord is altijd onvoldoende op het examen. Beperkte functiescheiding **moet** worden gecompenseerd door direct toezicht, roulatie of steekproef — en de stagiair moet die compensaties concreet kunnen benoemen, met aanduiding van wie ze uitvoert en op welke frequentie. Een KMO heeft minder formele functiescheiding, geen *geen* interne controle.

---

<div class="no-print">

## Wanneer je dit snapt, ga dan naar

- [[cyclus-analyse-en-controlemiddelen]] — De drie taxonomieën hier toegepast per transactiecyclus: aankoop, verkoop, voorraad, kas en lonen. Plus de IT-laag (algemene IT-controls, applicatie-controls, cloud) en het 8-stappen-ontwerp van een controle-architectuur.
- [[fouten-fraude-en-risicobeheersing]] — Hoe functiescheidings-gaten geëxploiteerd worden door fraudeurs: de fraudedriehoek (druk, gelegenheid, rationalisatie) plus de drie fraudecategorieën.
- [[wat-is-interne-controle-en-coso]] — Het COSO-kader, de vier doelen, redelijke zekerheid en de vijf inherente beperkingen — fundament dat hier wordt toegepast.
- [[interne-audit-evaluatie-en-aanbevelingen]] — Hoe de externe en interne auditor de functiescheiding evalueren: design effectiveness versus operating effectiveness.
- [[studiemateriaal/1-7/samenvatting|Samenvatting PO 1.7]] — Voor herhaling: de drie taxonomieën op één blad, het onderscheid accountingcontrole versus administratieve controle en de KMO-compensatie-formules.

## Doorklik naar concepten

Voor wie definitorisch detail wil opzoeken:

- [[functiescheiding]] · [[interne-controle]]

</div>

---

## Wettelijk fundament

- Functiescheiding als preventieve beheersingsmaatregel: ISA 315 (herzien-2019), Bijlage 3. Functiescheiding is bedoeld om beperkingen aan te brengen in de mogelijkheden om fouten te maken **en te verhullen** of fraude te plegen **en te verhullen** — door autoriseren, vastleggen en bewaren van activa aan verschillende personen toe te wijzen.
- KMO-compensatie via direct toezicht door eigenaar-bestuurder: ISA 315 (herzien-2019), §A157. In een door de eigenaar bestuurde entiteit kan de eigenaar-bestuurder via directe betrokkenheid effectief toezicht uitoefenen, wat de beperktere mogelijkheden voor functiescheiding kan compenseren.
- Schaalbaarheid van beheersingsmaatregelen voor minder complexe entiteiten: ISA 315 (herzien-2019), §A156. Interne beheersingsmaatregelen kunnen vergelijkbaar zijn met die in grotere entiteiten maar variëren in formaliteit; meer maatregelen kunnen direct door management worden toegepast.
- ITAA KMO-controlenorm — referentiekader voor vrijwillige en wettelijke controleopdrachten bij KMO's, met toetsing van functiescheiding en compenserende controles binnen de scope van de opdracht.
- 5 controletechnische functies (BURCB) en 4-categorieën-typologie: Starreveld-traditie plus COSO 2013 — internationale audit-doctrine, geen wettekst. Impliciet in ISA 315 (herzien-2019) waar de norm de driedeling autoriseren / vastleggen / bewaren benoemt als de kern van functiescheiding.

---

*Leerstuk PO 1.7 — techniek (2 van 5). Volgende stap: [[cyclus-analyse-en-controlemiddelen]].*
