---
title: 1.5 Beginselen van de Europese wetgeving en de IFRS-normen
tags:
- minicursus
- po-1-5
programmaonderdeel: '1.5'
gerelateerde_concepten:
- afschrijvingen-ifrs
- be-gaap-vs-ifrs-overzicht
- bijzondere-waardevermindering-ias-36
- componentenbenadering-ias-16
- correctie-jaarrekening-ifrs
- herwaarderingsmodel-ias-16
- ias-1-balans-presentatie
- ias-1-jaarrekening-componenten
- ias-1-mutatieoverzicht-eigen-vermogen
- ias-1-presentatie-beginselen
- ias-1-toelichtingsvereisten
- ias-1-winst-en-totaalresultaat
- ifrs-16-lessee-vs-lessor-overzicht
- ifrs-eerste-toepassing
- ifrs-toepassingsgebied-belgie
- ifrs-verordening-1606-2002
- immateriele-vaste-activa-ifrs
- leaseverplichting-ifrs
- leasing-ifrs
- materiele-vaste-activa-ifrs
- onderhanden-projecten-ifrs
- opbrengsten-ifrs
- prestatieverplichting-ifrs-15
- richtlijn-2013-34-eu
- right-of-use-actief
- voorraden-ifrs
- wijziging-boekhoudkundig-referentiestelsel
gegenereerd_op: '2026-05-17'
---
> [!warning]- Open beslissingen
> De volgende gaps zijn nog open voor dit programmaonderdeel — inhoud kan onvolledig zijn:
> - `edges.target-ontbreekt` op `onderhanden-projecten-ifrs`: Edge 'vervangt → ias-11-onderhanden-projecten' wijst naar niet-bestaand record. Historische IAS 11 i…
> - `edges.target-ontbreekt` op `opbrengsten-ifrs`: Edge 'vergelijkt-met → opbrengsten' wijst naar niet-bestaand BE-GAAP-record. PO 1.1 heeft (nog) geen…
> - `stappen.onvolledig` op `wijziging-boekhoudkundig-referentiestelsel`: node_type=procedure maar 0 stappen — terwijl andere PO 1.5-procedures (ifrs-eerste-toepassing 5 stap…
> - `stappen.onvolledig` op `afschrijvingen-ifrs`: node_type=methode maar 0 stappen; bijzondere-waardevermindering-ias-36 (ook methode) heeft 4 stappen…
> - `stappen.onvolledig` op `herwaarderingsmodel-ias-16`: node_type=methode met 0 stappen — terwijl bijzondere-waardevermindering-ias-36 (ook methode) wel 4 s…
> - `stappen.onvolledig` op `componentenbenadering-ias-16`: node_type=methode met 0 stappen; identificatie van significante componenten + apart afschrijvingspla…
> - `valkuilen.ontbreekt` op `leaseverplichting-ifrs`: 0 valkuilen terwijl andere begrippen (ias-1-jaarrekening-componenten 2, prestatieverplichting-ifrs-1…
> - `valkuilen.ontbreekt` op `right-of-use-actief`: 0 valkuilen; andere begrip-records hebben er 1-2. Typische fouten: vergeten initiële directe kosten …
> - `valkuilen.ontbreekt` op `ias-1-winst-en-totaalresultaat`: Slechts 2 valkuilen waarvan inhoudelijk weinig geld-impact. OCI-items reclassificatie versus geen re…
> - `vergelijkingsparen.vrije-tekst-niet-gespiegeld` op `be-gaap-vs-ifrs-overzicht`: Synthese-record vergelijkt 10 BE-GAAP/IFRS-paren maar `vergelijkingstabel` rijen verwijzen in vrije …
> - `records.ontbreekt` op `opbrengsten-ifrs`: BE-GAAP-tegenhanger record `opbrengsten` (realisatiebeginsel KB WVV art. 3:18 + 3:46) ontbreekt in c…
> - `records.ontbreekt` op `be-gaap-vs-ifrs-overzicht`: Voor PO 1.5.V.C bestaat geen aparte synthese over lessee-versus-lessor onder IFRS 16. Lessor-classif…

## Leesgids

Deze minicursus loopt van buiten naar binnen: eerst het Europese kader en wie IFRS moet toepassen, dan de presentatie-architectuur van IAS 1, daarna de waarderingsblokken. Elke thematische sectie groepeert begrippen rond één keuze; de competentie erna toont hoe je die keuze concreet maakt. Lees de twee synthese-fiches grondig — zij zijn de kaart waarop alle losse regels passen.

## Waarom dit programmaonderdeel telt

IFRS is geen alternatief Belgisch boekhoudrecht maar een andere kijk op wat een jaarrekening moet doen: niet fiscus of schuldeiser bedienen, maar de kapitaalmarkt informeren over economische realiteit. Dat verschil van doel verklaart bijna elke regel die je hier tegenkomt — van fair value tot componentenbenadering tot het verbod op LIFO. Als gecertificeerd accountant moet je IFRS-jaarrekeningen kunnen lezen, met BE-GAAP-cijfers vergelijken en cliënten adviseren bij keuze of overstap. Het examen toetst die transversale lezing: voor een gegeven feit het juiste stelsel herkennen en de twee tegen elkaar leggen.

## Waarom IFRS naast Belgisch GAAP? Twee referentiestelsels, één economische realiteit

BE-GAAP en IFRS verschillen niet in regelnummering maar in oriëntatie: BE-GAAP vertrekt vanuit voorzichtigheid, historische kostprijs en bescherming van schuldeiser en fiscus; IFRS vanuit getrouw beeld voor de kapitaalverstrekker, met meer ruimte voor fair value en economische substantie. Dezelfde transactie — een lease, een opbrengst, een herwaardering — krijgt onder elk stelsel een andere balans- en resultaatimpact, terwijl de onderliggende economie identiek blijft.

## Het Europese kader: richtlijn 2013/34/EU en verordening 1606/2002

Twee Europese instrumenten bepalen het speelveld: een richtlijn die in nationale wet wordt omgezet en de minimuminhoud van elke jaarrekening kadert, en een verordening die rechtstreeks geldt en IFRS oplegt aan specifieke ondernemingen. Het onderscheid juridisch instrument-rechtsbron is examenkritisch.

- [[richtlijn-2013-34-eu|Richtlijn 2013/34/EU — Europese jaarrekeningenrichtlijn]] · `regel`
- [[ifrs-verordening-1606-2002|IFRS-verordening 1606/2002 — verplichte toepassing IFRS]] · `regel`
- [[ifrs-toepassingsgebied-belgie|IFRS-toepassingsgebied in België — wie moet en wie mag?]] · `regel`

## Belgisch GAAP versus IFRS — overzicht van hoofdverschillen

Voor je in de IFRS-blokken duikt, geeft deze synthese de globale kaart: waar liggen de scharnieren waarop de twee stelsels uiteenlopen? Elke rij komt verderop in de cursus uitgewerkt terug — gebruik dit overzicht als ankerpunt om losse regels in hun geheel te plaatsen.

[[be-gaap-vs-ifrs-overzicht|→ Volledige synthese-fiche]]

## Bepalen of een onderneming IFRS moet of mag toepassen in België

De toepassingsvraag komt eerst: pas wanneer je weet welk stelsel geldt, weet je welke regels het dossier raakt. Deze procedure brengt verplichting, optie en uitsluiting samen tot één beslisboom.

[[competenties/bepalen-toepasselijkheid-ifrs-belgie|→ Volledige procedure]]

## IAS 1 — Presentatie van de jaarrekening: vijf componenten en presentatiebeginselen

IAS 1 levert de architectuur waarop alle andere IFRS-normen rusten: welke componenten een IFRS-jaarrekening bevat, welke beginselen de presentatie sturen en hoe balans, resultaat, eigenvermogen-mutaties en toelichtingen op elkaar aansluiten. Hier zit ook één van de zichtbaarste verschillen met BE-GAAP: mutatieoverzicht eigen vermogen en het onderscheid winst-versus-totaalresultaat bestaan onder de Belgische schema's niet.

- [[ias-1-jaarrekening-componenten|Componenten van een IFRS-jaarrekening (IAS 1)]] · `begrip`
- [[ias-1-presentatie-beginselen|Algemene presentatie-beginselen (IAS 1)]] · `beginsel`
- [[ias-1-balans-presentatie|IFRS-balanspresentatie — vlottend versus niet-vlottend (IAS 1)]] · `regel`
- [[ias-1-winst-en-totaalresultaat|Winst of verlies en overige onderdelen van het totaalresultaat (IAS 1)]] · `begrip`
- [[ias-1-mutatieoverzicht-eigen-vermogen|Mutatieoverzicht eigen vermogen (IAS 1)]] · `begrip`
- [[ias-1-toelichtingsvereisten|Toelichtingsvereisten onder IAS 1 — structuur en inhoud]] · `regel`

## Presenteren van een IFRS-jaarrekening volgens IAS 1 (5 componenten en presentatiebeginselen)

Deze procedure brengt de bouwstenen van IAS 1 samen tot één afleverbaar dossier: welk schema, welke beginselen toetsen, welke toelichtingen verplicht meegaan.

[[competenties/presenteren-ifrs-jaarrekening-volgens-ias-1|→ Volledige procedure]]

## Vaste activa onder IFRS: IAS 16 en IAS 38 — kostprijs, herwaardering en componenten

Vaste activa is het terrein waar fair value-denken het sterkst doorslaat: IFRS laat naast het kostprijsmodel ook een herwaarderingsmodel toe en verplicht een componentenbenadering bij substantieel afwijkende onderdelen. Het verschil met BE-GAAP zit niet alleen in toelating maar in presentatie — herwaarderingen lopen via OCI, niet via het resultaat.

- [[materiele-vaste-activa-ifrs|Materiële vaste activa onder IFRS (IAS 16)]] · `regel`
- [[immateriele-vaste-activa-ifrs|Immateriële activa onder IFRS (IAS 38)]] · `regel`
- [[herwaarderingsmodel-ias-16|Herwaarderingsmodel onder IAS 16]] · `methode`
- [[componentenbenadering-ias-16|Componentenbenadering (IAS 16) — afschrijving per onderdeel]] · `methode`
- [[afschrijvingen-ifrs|Afschrijvingen onder IFRS (IAS 16 + IAS 38)]] · `methode`

## Waarderen van materiële vaste activa onder IAS 16 (kostprijs- of herwaarderingsmodel)

De keuze tussen kostprijs- en herwaarderingsmodel geldt per activacategorie en raakt toelichting en eigen vermogen. Deze procedure structureert keuze, verwerking en bewaking.

[[competenties/waarderen-materiele-vaste-activa-ifrs|→ Volledige procedure]]

## Bijzondere waardevermindering onder IAS 36: indicaties, CGU en realiseerbare waarde

IAS 36 dwingt af dat een actief nooit boven zijn realiseerbare waarde op de balans blijft staan: bij indicaties van waardeverlies vergelijk je boekwaarde met het hoogste van fair value minus verkoopkosten en bedrijfswaarde. Genereert een actief niet zelfstandig kasstromen, dan toets je op het niveau van de kasstroomgenererende eenheid.

- [[bijzondere-waardevermindering-ias-36|Bijzondere waardevermindering (impairment) onder IAS 36]] · `methode`

## Toetsen van een actief op bijzondere waardevermindering onder IAS 36

De impairment-test verloopt in vaste stappen: indicatie detecteren, realiseerbare waarde meten, vergelijken met boekwaarde, boeken en toelichten — met aandacht voor het verschil tussen actief en kasstroomgenererende eenheid.

[[competenties/toetsen-bijzondere-waardevermindering-ias-36|→ Volledige procedure]]

## Opbrengsten onder IFRS 15: het vijf-stappen-model en prestatieverplichtingen

IFRS 15 vervangt het BE-GAAP-realisatiebeginsel door een gestructureerd vijf-stappen-model met de prestatieverplichting als spil: een opbrengst wordt erkend wanneer een afzonderlijke belofte aan de klant is overgedragen. Voor klant-specifieke projecten geldt erkenning over de periode wanneer aan welbepaalde criteria voldaan is — er is geen aparte norm meer voor onderhanden projecten.

- [[opbrengsten-ifrs|Opbrengsten onder IFRS (IFRS 15) — 5-stappen-model]] · `methode`
- [[prestatieverplichting-ifrs-15|Prestatieverplichting (performance obligation) onder IFRS 15]] · `begrip`
- [[onderhanden-projecten-ifrs|Onderhanden projecten in opdracht van derden — onder IFRS 15]] · `regel`

## Toepassen van het 5-stappen-model van IFRS 15 voor opbrengstenherkenning

Deze procedure loopt het vijf-stappen-model af op een concreet contract: contract identificeren, prestatieverplichtingen afzonderen, transactieprijs bepalen, toewijzen en erkennen naarmate verplichtingen worden vervuld. De kracht zit in het correct ontrafelen van bundels.

[[competenties/toepassen-vijf-stappen-model-opbrengsten-ifrs|→ Volledige procedure]]

## Voorraden onder IFRS: IAS 2 en het verbod op LIFO

Voorraadwaardering onder IFRS lijkt op BE-GAAP, met één scherp verschil: IAS 2 verbiedt LIFO. De andere kostprijsformules en de regel kostprijs versus opbrengstwaarde blijven herkenbaar.

- [[voorraden-ifrs|Voorraden onder IFRS (IAS 2)]] · `regel`

## IFRS 16 — lessee versus lessor: overzicht en asymmetrie

Voor je in de lessee-mechaniek duikt, expliciteert deze synthese de asymmetrie van IFRS 16: aan lessee-zijde verdween het oude onderscheid operationele-versus-financiële lease, aan lessor-zijde bleef het bestaan. Dat verschil is de sleutel om examenvragen over leasing onder IFRS correct te lezen.

[[ifrs-16-lessee-vs-lessor-overzicht|→ Volledige synthese-fiche]]

## Leasing onder IFRS 16: right-of-use-actief en leaseverplichting bij lessee

Onder IFRS 16 verschijnen quasi alle leases op de balans van de lessee: een gebruiksrecht-actief tegenover een verdisconteerde leaseverplichting. Wat onder BE-GAAP een huurlast was, wordt afschrijving plus rentelast — met directe gevolgen voor solvabiliteit en EBITDA.

- [[leasing-ifrs|Leasing onder IFRS (IFRS 16) — lessee-perspectief]] · `regel`
- [[right-of-use-actief|Right-of-use-actief (gebruiksrecht-actief) onder IFRS 16]] · `begrip`
- [[leaseverplichting-ifrs|Leaseverplichting onder IFRS 16]] · `begrip`

## Verwerken van een leaseovereenkomst onder IFRS 16 als lessee (right-of-use + lease-verplichting)

Deze procedure leidt je van lease-identificatie naar initiële opname, periodieke verwerking en toelichtingen. Let op de aansluiting tussen de afschrijving van het gebruiksrecht-actief en de rente-amortisatie van de verplichting.

[[competenties/verwerken-leasing-ifrs-lessee|→ Volledige procedure]]

## Correctie en wijziging van het boekhoudkundig referentiestelsel

Correctie binnen een stelsel en wisselen tussen stelsels zijn twee verschillende dingen: IAS 8 stuurt grondslag- en schattingswijzigingen binnen IFRS, terwijl de overstap tussen BE-GAAP en IFRS via afzonderlijke regels loopt. Verwar een schattingswijziging (prospectief) niet met een grondslagwijziging (retroactief).

- [[correctie-jaarrekening-ifrs|Correctie van de jaarrekening — IAS 8 versus CBN 2020/12]] · `procedure`
- [[wijziging-boekhoudkundig-referentiestelsel|Wijziging van boekhoudkundig referentiestelsel (CBN 2022/08)]] · `procedure`

## Uitvoeren van de eerste toepassing van IFRS overeenkomstig IFRS 1

De eerste toepassing is een eenmalige operatie met grote impact: openingsbalans op overgangsdatum, retroactieve toepassing met expliciete uitzonderingen, en een rijke toelichting die de overgang traceerbaar maakt.

[[competenties/uitvoeren-eerste-toepassing-ifrs|→ Volledige procedure]]

## Reflectie: IFRS als levend normenstelsel — IAS 17 → IFRS 16 en IAS 18 → IFRS 15

IFRS staat niet stil: opbrengsten verschoven van IAS 11 en IAS 18 naar IFRS 15, leasing van IAS 17 naar IFRS 16. Het ITAA-anker noemt nog de oude namen, maar de praktijk werkt al jaren met de nieuwe normen — en het examen kan beide kanten toetsen. Onthoud niet alleen de huidige regel maar ook de richting van de verschuiving: van off-balance naar on-balance bij lessees, van risico-en-beloning naar controle- en prestatieverplichting-criteria bij opbrengsten.


## Synthese-stappenplan

Bij elk IFRS-dossier doorloop je dezelfde keten. Begin met de toepassingsvraag: moet of mag de onderneming IFRS toepassen, en op welk niveau — enkelvoudig of geconsolideerd? Ga na of het om eerste toepassing gaat (IFRS 1) of om een going-concern-jaar. Stel de presentatie-architectuur volgens IAS 1 op en loop dan de waarderingsblokken af: vaste activa, impairment, opbrengsten, voorraden, leasing aan lessee-zijde. Bewaak per rubriek de aansluiting met BE-GAAP voor cliëntcommunicatie en consolidatie-input. Sluit af met toelichtingen en aansluitingstabellen die de overgang traceerbaar maken — IAS 1 vraagt expliciete verantwoording van elke keuze.

## Cheatsheet

### Kritische drempelwaarden

| Concept | Naam | Waarde | Eenheid | Gevolg |
|---|---|---|---|---|
| [[ifrs-verordening-1606-2002]] | Verplichting IFRS-toepassing | Beursnotering op een gereglementeerde markt van een EU-lidstaat op balansdatum + EU-rechtsvorm | kwalitatief criterium | Verplichte IFRS-toepassing op geconsolideerde jaarrekening voor boekjaren beginnend op of na 1 januari 2005 |

### Vergelijkingsparen-matrix

| Concept | Verwarrend met | Trigger |
|---|---|---|
| [[bijzondere-waardevermindering-ias-36]] | [[herwaarderingsmeerwaarden]] | Examen: 'boekwaarde > marktwaarde' → impairment (verlaging, W&V); 'marktwaarde > boekwaarde + herwaarderingsmodel' → herwaardering (verhoging, OCI). |
| [[correctie-jaarrekening-ifrs]] | [[wijziging-boekhoudkundig-referentiestelsel]] | Examen: 'Onderneming wijzigt afschrijvingsmethode' (lineair → degressief) — IAS 8 schattingswijziging (prospectief). 'Onderneming wijzigt waarderingsbasis vastgoed' (kostprijs → herwaardering) — IAS 8 grondslagwijziging (retroactief). 'Onderneming gaat over naar IFRS' — IFRS 1 + CBN 2022/08. |
| [[ias-1-balans-presentatie]] | [[jaarrekening-schema]] | Examenvraag over balansrubrieken: KB WVV gebruikt vaste-activa-rubrieken I (oprichtingskosten) tot IV (financiële vaste activa). IAS 1 gebruikt geen 'oprichtingskosten' — die mogen onder IFRS niet geactiveerd worden. |
| [[ias-1-jaarrekening-componenten]] | [[samenstelling-statutaire-jaarrekening]] | Bij vraag 'Welke vorm heeft de jaarrekening van een beursgenoteerde NV?': onderscheid maken tussen enkelvoudige (BE-GAAP-schema) en geconsolideerde (IAS 1). |
| [[ias-1-mutatieoverzicht-eigen-vermogen]] | [[samenstelling-statutaire-jaarrekening]] | Examen: 'Welke component bestaat WEL onder IFRS maar NIET onder BE-GAAP-jaarrekening?' → Mutatieoverzicht eigen vermogen. |
| [[ifrs-verordening-1606-2002]] | [[richtlijn-2013-34-eu]] | Bij vraag naar 'juridisch instrument' of 'rechtsbron': verordening = direct EU-recht, richtlijn = omgezet in nationaal recht. |
| [[immateriele-vaste-activa-ifrs]] | [[immateriele-vaste-activa]] | Examen: onderneming heeft € 2.500.000 onderzoekskosten op balans. Welk stelsel? → Als IFRS: schrappen, ingehouden winsten −€ 2.500.000. Als BE-GAAP: behouden mits voorwaarden vervuld. |
| [[leasing-ifrs]] | [[leasing]] | Examen: 'Bedrijf X heeft een huurcontract voor 5 jaar' — onder BE-GAAP: huurlast jaarlijks; onder IFRS 16: ROU + leaseverplichting op balans. Materiële impact bij vergelijking. |
| [[materiele-vaste-activa-ifrs]] | [[materiele-vaste-activa]] | Bij examenvraag over machine met componenten: KB WVV → één afschrijvingsplan mogelijk; IAS 16 → afzonderlijke afschrijving per component met substantiële kostprijs. |
| [[onderhanden-projecten-ifrs]] | [[voorraden-ifrs]] | Examen: 'Klant-specifiek project' → IFRS 15 over periode (mits criterium b of c vervuld); 'algemene voorraad voor verkoop' → IAS 2. |
| [[richtlijn-2013-34-eu]] | [[ifrs-verordening-1606-2002]] | Examenvraag: 'Welke EU-norm bepaalt of een onderneming IFRS moet toepassen?' → Verordening 1606/2002. 'Welke EU-norm bepaalt de minimuminhoud van een Belgische jaarrekening?' → Richtlijn 2013/34/EU. |
| [[voorraden-ifrs]] | [[voorraden]] | Examen: 'Onderneming gebruikt LIFO voor voorraadwaardering' — onder IFRS NIET toegelaten; onder BE-GAAP wel. |


## Examenfocus

Drie denkpatronen keren terug. Eerst de stelsel-herkenning: een casus geeft een feit (huurcontract, herwaardering, onderzoekskost, LIFO) en vraagt impliciet welk stelsel geldt — lees daarom altijd eerst de signalen over beursnotering en jaarrekeningniveau. Daarna de juridische-instrument-vraag: verordening tegenover richtlijn, grondslagwijziging tegenover schattingswijziging, impairment tegenover herwaardering — telkens een onderscheid dat met één criterium kantelt. Ten slotte de spiegelvraag: voor dezelfde economische gebeurtenis welke BE-GAAP- en welke IFRS-behandeling, en welk verschil ontstaat er in balanstotaal, eigen vermogen of resultaat?

<!-- TODO: examenvragen via classify_vragen_naar_programmaonderdelen.py -->

## Competentie-index

<div class="two-column-list">

- [[competenties/bepalen-toepasselijkheid-ifrs-belgie|Bepalen of een onderneming IFRS moet of mag toepassen in België]]
- [[competenties/presenteren-ifrs-jaarrekening-volgens-ias-1|Presenteren van een IFRS-jaarrekening volgens IAS 1 (5 componenten en presentatiebeginselen)]]
- [[competenties/toepassen-vijf-stappen-model-opbrengsten-ifrs|Toepassen van het 5-stappen-model van IFRS 15 voor opbrengstenherkenning]]
- [[competenties/toetsen-bijzondere-waardevermindering-ias-36|Toetsen van een actief op bijzondere waardevermindering onder IAS 36]]
- [[competenties/uitvoeren-eerste-toepassing-ifrs|Uitvoeren van de eerste toepassing van IFRS overeenkomstig IFRS 1]]
- [[competenties/verwerken-leasing-ifrs-lessee|Verwerken van een leaseovereenkomst onder IFRS 16 als lessee (right-of-use + lease-verplichting)]]
- [[competenties/waarderen-materiele-vaste-activa-ifrs|Waarderen van materiële vaste activa onder IAS 16 (kostprijs- of herwaarderingsmodel)]]

</div>

## Concept-index

<div class="two-column-list">

- [[afschrijvingen-ifrs|Afschrijvingen onder IFRS (IAS 16 + IAS 38)]] · `methode`
- [[ias-1-presentatie-beginselen|Algemene presentatie-beginselen (IAS 1)]] · `beginsel`
- [[be-gaap-vs-ifrs-overzicht|Belgisch GAAP versus IFRS — overzicht van hoofdverschillen]] · `synthese`
- [[bijzondere-waardevermindering-ias-36|Bijzondere waardevermindering (impairment) onder IAS 36]] · `methode`
- [[ias-1-jaarrekening-componenten|Componenten van een IFRS-jaarrekening (IAS 1)]] · `begrip`
- [[componentenbenadering-ias-16|Componentenbenadering (IAS 16) — afschrijving per onderdeel]] · `methode`
- [[correctie-jaarrekening-ifrs|Correctie van de jaarrekening — IAS 8 versus CBN 2020/12]] · `procedure`
- [[ifrs-eerste-toepassing|Eerste toepassing van IFRS (IFRS 1)]] · `procedure`
- [[herwaarderingsmodel-ias-16|Herwaarderingsmodel onder IAS 16]] · `methode`
- [[ifrs-16-lessee-vs-lessor-overzicht|IFRS 16 — lessee versus lessor: overzicht en asymmetrie]] · `synthese`
- [[ias-1-balans-presentatie|IFRS-balanspresentatie — vlottend versus niet-vlottend (IAS 1)]] · `regel`
- [[ifrs-toepassingsgebied-belgie|IFRS-toepassingsgebied in België — wie moet en wie mag?]] · `regel`
- [[ifrs-verordening-1606-2002|IFRS-verordening 1606/2002 — verplichte toepassing IFRS]] · `regel`
- [[immateriele-vaste-activa-ifrs|Immateriële activa onder IFRS (IAS 38)]] · `regel`
- [[leaseverplichting-ifrs|Leaseverplichting onder IFRS 16]] · `begrip`
- [[leasing-ifrs|Leasing onder IFRS (IFRS 16) — lessee-perspectief]] · `regel`
- [[materiele-vaste-activa-ifrs|Materiële vaste activa onder IFRS (IAS 16)]] · `regel`
- [[ias-1-mutatieoverzicht-eigen-vermogen|Mutatieoverzicht eigen vermogen (IAS 1)]] · `begrip`
- [[onderhanden-projecten-ifrs|Onderhanden projecten in opdracht van derden — onder IFRS 15]] · `regel`
- [[opbrengsten-ifrs|Opbrengsten onder IFRS (IFRS 15) — 5-stappen-model]] · `methode`
- [[prestatieverplichting-ifrs-15|Prestatieverplichting (performance obligation) onder IFRS 15]] · `begrip`
- [[richtlijn-2013-34-eu|Richtlijn 2013/34/EU — Europese jaarrekeningenrichtlijn]] · `regel`
- [[right-of-use-actief|Right-of-use-actief (gebruiksrecht-actief) onder IFRS 16]] · `begrip`
- [[ias-1-toelichtingsvereisten|Toelichtingsvereisten onder IAS 1 — structuur en inhoud]] · `regel`
- [[voorraden-ifrs|Voorraden onder IFRS (IAS 2)]] · `regel`
- [[wijziging-boekhoudkundig-referentiestelsel|Wijziging van boekhoudkundig referentiestelsel (CBN 2022/08)]] · `procedure`
- [[ias-1-winst-en-totaalresultaat|Winst of verlies en overige onderdelen van het totaalresultaat (IAS 1)]] · `begrip`

</div>
