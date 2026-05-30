---
title: "Goodwill bij consolidatie"
description: "Leerstuk PO 1.4 — het consolidatieverschil-leerstuk: hoe ontstaat goodwill, hoe wordt ze nadien afgeschreven, wanneer is een impairment nodig, en hoe verschilt B-GAAP van IFRS?"
explorer_title: "4. Goodwill"
tags:
  - leerstuk
  - po-1.4
  - cluster-consolidatie
---

<div class="no-print">

> **Leerstuk — één vraag, helemaal doorgewerkt.** Goodwill is het verschil tussen wat je voor een dochter betaalt en het reële netto-vermogen dat je in ruil krijgt — en wat je daarna met dat verschil doet. Vereiste voorkennis: [[hoe-consolideren]], vooral het eerste-consolidatie-deel waar goodwill voor het eerst op de balans verschijnt. Voor verhaal en routekaart: [[leerpaden/1-4|minicursus PO 1.4]].

</div>

## Antwoord in één blik

Goodwill bij consolidatie is de **premie** die je betaalt boven het reëel-gewaardeerd aandeel in het netto-eigen vermogen van de dochter — formeel: aanschafprijs van de deelneming min het aandeel van de moeder in de na-herwaardering vastgestelde netto-activa. Onder B-GAAP schrijf je die premie systematisch af volgens een plan dat overeenstemt met de vermoedelijke gebruiksduur (met motiveringsplicht boven vijf jaar en een feitelijke maximumtermijn van tien jaar als die gebruiksduur niet betrouwbaar te schatten is), en boek je daarbovenop een niet-recurrente afschrijving zodra de economische omstandigheden niet meer rechtvaardigen dat goodwill aan zijn boekwaarde op de balans blijft. Onder IFRS wordt goodwill **niet** afgeschreven, maar jaarlijks getoetst op impairment per cash-generating unit. Een **negatief** consolidatieverschil (badwill) is de spiegel-situatie en heeft eigen, voorzichtige regels.

| Aspect | B-GAAP | IFRS |
|---|---|---|
| Lopende afschrijving goodwill | **Ja** — passend plan, gebruiksduur | **Nee** — geen afschrijving |
| Impairment | Niet-recurrente afschrijving bij ongunstige ontwikkeling | **Jaarlijkse** verplichte test per CGU |
| Terugneming impairment goodwill | Zelden mogelijk | **Verboden** (anders dan voor andere activa) |
| Negatief verschil (badwill) | Onder passiva; in resultaat bij ongunstige ontwikkeling | Direct in resultaat (*bargain purchase gain*) |

---

## Hoe ontstaat goodwill bij eerste consolidatie?

Goodwill is geen post die de moeder afzonderlijk boekt — ze ontstaat als *restpost* in de rekenformule van de eerste consolidatie. Het bredere mechaniek-verhaal staat in [[hoe-consolideren]] stap 2; hier pakken we enkel het verschil-stuk op.

Kort gerecapituleerd: op overnamedatum worden de activa en passiva van de dochter eerst geherwaardeerd naar reële waarde. Pas dán wordt de aanschafprijs van de deelneming vergeleken met het aandeel van de moeder in dat herwaardeerd netto-eigen vermogen. Het verschil dat overblijft, wordt op de geconsolideerde balans opgenomen in de post "Consolidatieverschillen" — aan de actiefzijde als het positief is, aan de passiefzijde als het negatief is.

In de Aurelia-case betaalt de moeder 6,0 mln voor 80 % van Bellator. Na herwaardering bedraagt het reëel netto-eigen vermogen van Bellator 5,5 mln; haar aandeel daarin is 80 % × 5,5 = 4,4 mln. Het verschil is goodwill.

| Component | Bedrag (mln) |
|---|---:|
| Aanschafprijs deelneming (80 % van Bellator) | **6,0** |
| Aandeel in reële NEV van Bellator (80 % × 5,5) | (4,4) |
| **Goodwill bij eerste consolidatie** | **1,6** |

> **De belangrijkste nuance.** Goodwill wordt berekend ten opzichte van het reëel netto-eigen vermogen, **niet** ten opzichte van de oorspronkelijke boekwaarde. Als je die stap overslaat, krijg je een goodwill die kunstmatig groot is — alles wat eigenlijk een herwaarderingsmeerwaarde op de gebouwen of een tot dan toe ongeboekt immaterieel actief (zoals klantenrelaties) zou zijn, schuif je dan in één hoop op de "goodwill"-lijn. Dat is niet wat de wet vraagt en niet wat de gebruiker van de geconsolideerde jaarrekening verwacht.

Conceptueel staat goodwill voor wat je niet onafhankelijk op de balans van de dochter kon vinden, maar wat blijkbaar wél waarde heeft: merknaam, geografische marktpositie, ingewerkt personeel, distributienetwerk, verwachte synergieën met de moeder. Allemaal economische realiteit, geen apart actief — en daarom samengevat als één rest-post.

---

## Afschrijving onder B-GAAP

Goodwill is een actief met beperkte levensduur — niet eeuwig. Onder B-GAAP volg je de hoofdregel: de positieve consolidatieverschillen worden afgeschreven ten laste van de geconsolideerde resultatenrekening volgens een passend afschrijvingsplan dat overeenstemt met de vermoedelijke gebruiksduur van het actief. Geen automatische tien jaar dus — je redeneert eerst over de vermoedelijke levensduur en kiest dán je termijn.

Twee belangrijke randvoorwaarden begeleiden die keuze. Eén: schrijf je goodwill af over meer dan **vijf jaar**, dan moet je dat motiveren in de toelichting. De wetgever wil voorkomen dat groepen routinematig zeer lange termijnen kiezen om de jaarlijkse afschrijvings-impact op het resultaat te drukken zonder rationale. Twee: als de gebruiksduur niet met zekerheid kan worden geraamd, geldt een **maximumtermijn van tien jaar**. Dat plafond stond in oud art. 61 KB W.Venn. en wordt in CBN-context bevestigd als basisprincipe dat onder het KB-WVV behouden blijft.

Voor Aurelia kiezen we de tienjaars-termijn: bij Bellator zijn klantenrelaties en synergieën moeilijk objectief af te bakenen, dus de vermoedelijke gebruiksduur is niet met zekerheid te ramen. Dat geeft een lineaire afschrijving van 1,60 ÷ 10 = 0,16 mln per jaar.

| Boekjaar | Goodwill begin | Afschrijving | Goodwill einde |
|---|---:|---:|---:|
| 2026 (jaar 1) | 1,60 | (0,16) | 1,44 |
| 2027 (jaar 2) | 1,44 | (0,16) | 1,28 |
| ... | ... | ... | ... |
| 2035 (jaar 10) | 0,16 | (0,16) | 0,00 |

De boeking elk jaar in de consolidatieregisters:

| Debet | mln | Credit | mln |
|---|---:|---|---:|
| Afschrijving op consolidatieverschil | 0,16 | Geboekte afschrijvingen op consolidatieverschil | 0,16 |
| **Totaal** | **0,16** | **Totaal** | **0,16** |

Die debet-post landt onder de bedrijfskosten of de financiële kosten in de geconsolideerde resultatenrekening — in een afzonderlijke post, zodat de gebruiker de impact van goodwill-afschrijving ziet zonder ze in een algemene post te moeten zoeken.

---

## Impairment onder B-GAAP — de niet-recurrente afschrijving

De lineaire afschrijving is het normale ritme, maar dat ritme volstaat niet altijd. Wanneer de economische omstandigheden zo verschuiven dat het *niet langer economisch verantwoord* is om goodwill aan zijn huidige waarde op de balans te handhaven, moet je een **aanvullende of niet-recurrente afschrijving** boeken. Dat is geen herwaardering in stijgende richting, maar een neerwaartse correctie bovenop het plan.

De trigger is open geformuleerd in de wet en in de praktijk afhankelijk van het oordeel van de groep over de waarde van de dochter: wegval van een grote klant, structurele marktverandering, technologie-shift, verlies van een patent. Wat ze gemeen hebben: de premie die je ooit betaalde, kan economisch niet langer hard gemaakt worden.

Stel dat Aurelia in 2028 vaststelt dat Bellators grootste klant het contract niet verlengt en wegvalt. De resterende waarde van de dochter — en dus van de goodwill — staat onder druk. Aurelia bepaalt dat een aanvullende niet-recurrente afschrijving van 0,5 mln nodig is, bovenop de gewone 0,16 mln voor dat jaar.

| Debet | mln | Credit | mln |
|---|---:|---|---:|
| Niet-recurrente afschrijving op consolidatieverschil | 0,5 | Geboekte afschrijvingen op consolidatieverschil | 0,5 |
| **Totaal** | **0,5** | **Totaal** | **0,5** |

Net als de gewone afschrijving wordt de niet-recurrente afschrijving in een afzonderlijke post van de bedrijfskosten of de financiële kosten geboekt, zodat ze in de toelichting traceerbaar blijft.

> **Geen terugneming.** Anders dan voor sommige andere activa wordt onder B-GAAP een eenmaal geboekte afschrijving op goodwill in de praktijk niet teruggenomen wanneer de omstandigheden weer verbeteren. Een correctie naar boven zou neerkomen op het opnieuw activeren van interne goodwill, en interne goodwill mag niet op de balans verschijnen. Wie 0,5 mln heeft afgeschreven, behoudt die afschrijving definitief.

---

## IFRS — geen afschrijving, alleen impairment

Onder IFRS draait het andere keer om. IFRS 3 *Business Combinations* regelt de eerste opname; IAS 36 *Impairment of Assets* regelt het vervolg. De combinatie: **geen** lopende afschrijving. Goodwill blijft op de balans staan zolang ze haar waarde kan rechtvaardigen, en wordt **jaarlijks** verplicht getoetst op impairment — en bovendien telkens wanneer indicatoren van waardeverlies opduiken.

De toets verloopt per *cash-generating unit*: de kleinste identificeerbare groep activa die onafhankelijke kasstromen genereert. Goodwill wordt bij eerste opname aan een of meer CGUs toegerekend. Per CGU vergelijk je vervolgens de **boekwaarde inclusief goodwill** met de **recoverable amount**, gedefinieerd als het maximum van (a) de reële waarde min verkoopkosten en (b) de gebruikswaarde, doorgaans bepaald via een verdiscontering van toekomstige kasstromen.

Is de boekwaarde van de CGU hoger dan haar recoverable amount, dan wordt het verschil als impairment-verlies in de resultatenrekening geboekt. Het verlies wordt eerst toegerekend aan de goodwill van die CGU; pas als die volledig is uitgewist, gaat eventuele rest naar de andere activa van de CGU.

Eén harde regel onderscheidt goodwill van bijna alle andere activa onder IFRS: een **terugneming** van een impairment op goodwill is **verboden**. Andere activa mogen onder voorwaarden hun impairment terugnemen wanneer omstandigheden verbeteren; goodwill niet. De achterliggende reden is identiek aan die onder B-GAAP: een terugneming zou interne goodwill activeren, en die mag niet op de balans.

Praktisch gevolg: onder IFRS leidt een impairment-vaststelling vaak tot één **grote, schokkende boeking** in plaats van een gespreide afschrijving over tien jaar. Het is een van de vaste examen-trappen — leerlingen verwarren de "geen afschrijving"-regel met "geen impact op het resultaat", terwijl impairment soms juist een veel grotere impact heeft dan jaarlijkse B-GAAP-afschrijvingen ooit zouden hebben.

---

## Badwill — het negatieve consolidatieverschil

De spiegel-situatie: je betaalt **minder** voor je deelneming dan het aandeel in het reëel netto-eigen vermogen waar je recht op hebt. Het verschil heet *badwill* of, in IFRS-jargon, *bargain purchase gain*. Op het eerste gezicht een meevaller — maar de boekhouder behandelt het met voorzichtigheid, want een echte koopje op de markt is zeldzaam en doorgaans heeft een lagere koopprijs een reden.

Typische scenario's waarin badwill ontstaat: een gedwongen verkoop door een verkoper in geldnood, een overname van een vennootschap met niet-erkende of slecht ingeschatte verplichtingen (pensioenen, herstelvergoedingen, milieuverplichtingen die nog niet als voorziening op de balans staan), of een dochter waarvan de verkoper grote toekomstige verliezen verwacht die de markt zwaarder inschat dan de boekwaarden suggereren.

**Onder B-GAAP** wordt het negatieve consolidatieverschil aan de **passiefzijde** van de geconsolideerde balans geboekt, in de post "Consolidatieverschillen". Het wordt pas naar de resultatenrekening overgebracht wanneer een ongunstige ontwikkeling die aan de basis lag van het negatieve verschil zich daadwerkelijk realiseert. In alle andere gevallen blijft het als component van het geconsolideerde eigen vermogen op de passiefzijde staan. De gedachte: een aanwezige badwill mag pas als opbrengst worden erkend wanneer de risico's die hem rechtvaardigden — een verwacht verlies, een verborgen verplichting — zich ook concretiseren.

**Onder IFRS** is de behandeling kortstondiger. IFRS 3 vraagt eerst een hermeting van de geïdentificeerde activa, verplichtingen en de koopprijs zelf — om zeker te zijn dat er geen meetfout in zit. Bevestigt die hermeting het negatieve verschil, dan wordt het **onmiddellijk** in de resultatenrekening geboekt als *bargain purchase gain*. Geen wachtperiode, geen passiva-opname.

> **Vaste examen-val.** Studenten verwarren badwill met een "gewone" winst. Onder B-GAAP volstaat de overname zelf níet — zonder gerealiseerde ongunstige ontwikkeling blijft badwill op de balans. Wie schrijft "negatief consolidatieverschil = onmiddellijke opbrengst onder B-GAAP" haalt het IFRS-mechaniek door elkaar met het Belgische.

---

## Waar staat goodwill in de geconsolideerde balans?

Onder B-GAAP verschijnt goodwill als afzonderlijke post **"Consolidatieverschillen"** binnen de immateriële vaste activa van de geconsolideerde balans. De toelichting moet drie zaken vermelden: het bedrag van het positief (en eventueel negatief) verschil, de gehanteerde afschrijvingstermijn, en — wanneer die termijn meer dan vijf jaar bedraagt — de motivering voor de gekozen termijn.

Onder IFRS verschijnt goodwill apart als **"Goodwill"** onder de non-current assets, met uitgebreide *disclosure*-vereisten over de CGUs waaraan ze is toegerekend, de gebruikte impairment-modellen, de belangrijkste veronderstellingen (groei-, discount- en margins-parameters) en de gevoeligheid van de testresultaten voor schommelingen in die veronderstellingen.

Het verschil in zichtbaarheid op de balans weerspiegelt het onderliggende verschil in benadering: onder B-GAAP is goodwill een te-verteren actief, onder IFRS een blijvende waarde die jaarlijks gerechtvaardigd moet worden.

---

<div class="no-print">

## Wanneer je dit snapt, ga dan naar

- [[hoe-consolideren]] — voor de bredere context: methodes, eerste-consolidatie en eliminaties waarin goodwill voor het eerst opduikt.
- [[rapportering-en-controle-geconsolideerde-jaarrekening]] — voor de toelichting-eisen en hoe goodwill in het jaarverslag wordt beschreven.
- [[themafiches/consolidatie|Themafiche Consolidatie]] — voor herhaling vlak vóór het examen.

## Doorklik naar concepten

Voor wie definitorisch detail wil opzoeken:

- [[consolidatieverschil]] · [[eerste-consolidatie]]

</div>

---

## Wettelijk fundament

- Positief consolidatieverschil — afschrijving: KB-WVV art. 3:131 § 1. Passend plan in functie van de vermoedelijke gebruiksduur; meer dan vijf jaar te motiveren in de toelichting; aanvullende of niet-recurrente afschrijvingen bij ongunstige economische ontwikkelingen, geboekt in een afzonderlijke post van de bedrijfskosten of de financiële kosten.
- Negatief consolidatieverschil (badwill): KB-WVV art. 3:131 § 2. Opname aan de passiefzijde; via resultaat enkel wanneer de ongunstige ontwikkeling die aan de basis lag zich realiseert.
- Maximumtermijn van tien jaar bij niet-betrouwbare schatting: CBN-advies 2016/7 (verwijzing naar oud art. 61 KB W.Venn.; principe behouden onder KB-WVV).
- Realisatie van de deelneming na overname — afboeking consolidatieverschil: KB-WVV art. 3:132.
- IFRS-pad: IFRS 3 *Business Combinations* (eerste meting van goodwill en bargain purchase gain) · IAS 36 *Impairment of Assets* (jaarlijkse impairment-test, geen lopende afschrijving, verbod op terugneming voor goodwill).

---

*Leerstuk PO 1.4. Status: nieuw — POC voor ADR-037, gerenderd uit script + Aurelia-voorbeeldgroep.*
