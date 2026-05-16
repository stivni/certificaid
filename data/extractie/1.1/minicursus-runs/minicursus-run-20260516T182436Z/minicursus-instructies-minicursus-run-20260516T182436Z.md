# Minicursus-glue-run minicursus-run-20260516T182436Z — Instructies voor Opus-subagent

**Programmaonderdeel**: 1.1
**Run-id**: minicursus-run-20260516T182436Z
**Gegenereerd op**: 2026-05-16T18:24:36+00:00

## Jouw taak

Vul de `<!-- TODO: Opus-glue ... -->` placeholders in de skeleton-Markdown in.
Schrijf de output als één JSON-object naar stdout met de velden beschreven in
`prompts/minicursus-glue-v1.md`.

## Input-bestanden

- **Skeleton**: `content/studiemateriaal/1-1-algemene-boekhouding/minicursus.md`
- **Records-summaries** (42 stuks): zie §Records hieronder
- **Competentie-summaries** (14 stuks): zie §Competenties hieronder

## Anti-fabricatie-regels (verplicht)

- Geen feiten-claims in glue-tekst — alleen rationale, beginselen, transities
- Geen wikilinks bedenken — die staan al in de skeleton
- Verbind aan beginselen die in de records beschreven zijn
- Bij twijfel: korte neutrale tekst, geen uitvinding

## Records-summaries

```json
[
  {
    "id": "aanschaffingswaarde",
    "naam": "Aanschaffingswaarde",
    "node_type": "begrip",
    "definitie_snippet": "De **basiswaarde** waartegen elk actiefbestanddeel bij verwerving in de boekhouding wordt opgenomen, vóór aftrek van afschrijvingen en waardeverminderingen. De aanschaffingswaarde kan **drie vormen** aannemen: (1) de **aanschaffingsprijs** bij aankoop van een derde (inclusief bijkomende kosten), (2)",
    "rationale_snippet": ""
  },
  {
    "id": "afschrijvingen",
    "naam": "Afschrijvingen",
    "node_type": "methode",
    "definitie_snippet": "Bedragen ten laste van de resultatenrekening genomen met betrekking tot **oprichtingskosten** en **immateriële en materiële vaste activa met beperkte gebruiksduur**, om hetzij de aanschaffingswaarde te spreiden over de waarschijnlijke gebruiksduur, hetzij de kost te nemen op het ogenblik waarop ze w",
    "rationale_snippet": ""
  },
  {
    "id": "bedrijfsresultaat",
    "naam": "Bedrijfsresultaat (bedrijfskosten en bedrijfsopbrengsten)",
    "node_type": "fenomeen",
    "definitie_snippet": "Het verschil tussen **bedrijfsopbrengsten** (klasse 7, hoofdzakelijk omzet en voorraadwijzigingen) en **bedrijfskosten** (klasse 6, hoofdzakelijk handelsgoederen/grond- en hulpstoffen, diensten en diverse goederen, bezoldigingen + sociale lasten, afschrijvingen, waardeverminderingen, voorzieningen, ",
    "rationale_snippet": ""
  },
  {
    "id": "bedrijfsvorderingen",
    "naam": "Bedrijfsvorderingen",
    "node_type": "begrip",
    "definitie_snippet": "**Vorderingen op derden** die voortkomen uit de gewone bedrijfsuitoefening (verkoop van goederen of diensten op krediet). Hoofdzakelijk **handelsdebiteuren** (rekening 400) plus te innen bedragen wegens leveringen of dienstprestaties. Op de balans gegroepeerd onder rubriek VII (vlottende activa, vor",
    "rationale_snippet": ""
  },
  {
    "id": "bewaring-boekhoudstukken",
    "naam": "Bewaring van boekhoudkundige stukken",
    "node_type": "regel",
    "definitie_snippet": "Boeken, rekeningen en verantwoordingsstukken moeten gedurende **7 jaar** worden bewaard, te rekenen vanaf 1 januari volgend op het boekjaar waarop ze betrekking hebben (WER art. III.86). Verantwoordingsstukken die geen verband houden met boekhoudkundige verrichtingen mogen 3 jaar worden bewaard. Bew",
    "rationale_snippet": ""
  },
  {
    "id": "boekhoudbeginselen-overzicht",
    "naam": "Boekhoudbeginselen &mdash; overzicht",
    "node_type": "synthese",
    "definitie_snippet": "",
    "rationale_snippet": ""
  },
  {
    "id": "boekjaar-eindprocedure-checklist",
    "naam": "Boekjaar afsluiten &mdash; van proefbalans tot neerlegging",
    "node_type": "synthese",
    "definitie_snippet": "",
    "rationale_snippet": ""
  },
  {
    "id": "continuiteitsbeginsel",
    "naam": "Boekhoudkundig continuïteitsbeginsel (going concern)",
    "node_type": "beginsel",
    "definitie_snippet": "De jaarrekening wordt opgemaakt in de **veronderstelling dat de onderneming haar bedrijf zal voortzetten** (going concern). Dat is de standaardpremisse voor alle waarderingen: vaste activa worden afgeschreven over hun gebruiksduur, voorraden tegen aanschaffingswaarde, vorderingen tegen verwachte rea",
    "rationale_snippet": ""
  },
  {
    "id": "dagboek",
    "naam": "Dagboek",
    "node_type": "begrip",
    "definitie_snippet": "Een **dagboek** is het chronologisch register waarin een onderneming al haar verrichtingen inschrijft op de dag dat ze gebeuren. Twee vormen: (1) een **ongesplitst dagboek** waarin alle verrichtingen achter elkaar staan, of (2) een set **hulpdagboeken** (aankoopdagboek, verkoopdagboek, financieel da",
    "rationale_snippet": ""
  },
  {
    "id": "dubbel-boekhouden",
    "naam": "Dubbel boekhouden",
    "node_type": "methode",
    "definitie_snippet": "Een boekhoudtechniek waarin elke verrichting wordt geboekt in **minstens twee rekeningen**: een debet- en een creditzijde, voor exact hetzelfde totaalbedrag. De som van alle debetboekingen is altijd gelijk aan de som van alle creditboekingen. Hierdoor klopt de balans (Activa = Passief) per definitie",
    "rationale_snippet": ""
  },
  {
    "id": "eigen-aandelen",
    "naam": "Beheer van eigen aandelen",
    "node_type": "fenomeen",
    "definitie_snippet": "Een vennootschap kan onder strikte voorwaarden **haar eigen aandelen inkopen** en aanhouden in haar portefeuille. Boekhoudkundig: opname op rekening **50 'Eigen aandelen'** onder de geldbeleggingen (rubriek IX activa). **Parallel** wordt een **'Reserve voor eigen aandelen'** (rekening 1310, **onbesc",
    "rationale_snippet": ""
  },
  {
    "id": "eigen-middelen",
    "naam": "Eigen middelen (eigen vermogen)",
    "node_type": "fenomeen",
    "definitie_snippet": "Het **netto-vermogen** van de onderneming dat toebehoort aan haar aandeelhouders/vennoten: activa minus schulden. In de balans onder rubriek I — VI: (10) kapitaal/eigen vermogensinbreng, (11) uitgiftepremies, (12) herwaarderingsmeerwaarden, (13) reserves (wettelijke, onbeschikbare, belastingvrije, b",
    "rationale_snippet": ""
  },
  {
    "id": "financiele-vaste-activa",
    "naam": "Financiële vaste activa",
    "node_type": "begrip",
    "definitie_snippet": "**Vorderingen en deelnemingen** die de onderneming aanhoudt **om duurzaam de bedrijfsuitoefening** van een andere onderneming **te ondersteunen** of om er duurzame band mee te onderhouden. Het MAR groepeert ze onder rubriek 28: (280) Deelnemingen in verbonden ondernemingen, (281) Vorderingen op verb",
    "rationale_snippet": ""
  },
  {
    "id": "financiele-verrichtingen",
    "naam": "Financiële verrichtingen (kosten + opbrengsten)",
    "node_type": "fenomeen",
    "definitie_snippet": "**Kosten en opbrengsten** uit de **financiële activiteit** van de onderneming: intresten op leningen en deposito's, kosten op leningen, opbrengsten/verliezen op effecten en deelnemingen, wisselkoersverschillen. Klasse 65 (financiële kosten) en 75 (financiële opbrengsten). Strikt gescheiden van het b",
    "rationale_snippet": ""
  },
  {
    "id": "geldbeleggingen",
    "naam": "Geldbeleggingen en liquide middelen",
    "node_type": "begrip",
    "definitie_snippet": "**Vlottende activa** (rubriek 5 MAR) waarin de onderneming tijdelijk haar overtollige middelen plaatst voor **korte-termijn-rendement** of voor **dagelijkse liquiditeit**. Twee hoofdgroepen: (1) **Geldbeleggingen** rubriek 50-53 (eigen aandelen 50, aandelen 51, vastrentende effecten 52, termijndepos",
    "rationale_snippet": ""
  },
  {
    "id": "getrouw-beeld",
    "naam": "Getrouw beeld",
    "node_type": "beginsel",
    "definitie_snippet": "De jaarrekening moet **een getrouw beeld** geven van het vermogen, de financiële positie en het resultaat van de onderneming (Richtlijn 2013/34/EU art. 4, lid 3; KB 21/10/2018 art. 3:1). Als de toepassing van de waarderingsregels in een uitzonderlijk geval geen getrouw beeld geeft, **moet** ervan wo",
    "rationale_snippet": ""
  },
  {
    "id": "herwaarderingsmeerwaarden",
    "naam": "Herwaarderingsmeerwaarden",
    "node_type": "fenomeen",
    "definitie_snippet": "Een **uitzonderlijke opwaardering** van een materieel of financieel vast actief boven zijn aanschaffingswaarde, geboekt als 'herwaarderingsmeerwaarde' aan de passiefzijde van de balans (rubriek III. binnen eigen middelen). Toegelaten enkel onder strikte voorwaarden (KB WVV art. 3:35): (a) zekere en ",
    "rationale_snippet": ""
  },
  {
    "id": "immateriele-vaste-activa",
    "naam": "Immateriële vaste activa",
    "node_type": "begrip",
    "definitie_snippet": "**Ondernemingsmiddelen van onlichamelijke aard** die duurzaam voor de bedrijfsactiviteit worden gebruikt en waaruit toekomstige economische voordelen zullen vloeien. Het MAR groepeert ze onder rubriek 21, opgesplitst in: (1) **kosten van onderzoek en ontwikkeling** (210), (2) **concessies, octrooien",
    "rationale_snippet": ""
  },
  {
    "id": "inventaris",
    "naam": "Inventaris",
    "node_type": "procedure",
    "definitie_snippet": "Het **gestructureerd overzicht** van alle bezittingen, vorderingen, schulden, verplichtingen en eigen middelen van een onderneming op één gekozen datum (typisch balansdatum), opgesteld door fysieke telling, contractverificatie en waardering. De inventaris is de feitelijke check op de boekhouding: vo",
    "rationale_snippet": ""
  },
  {
    "id": "jaarrekening",
    "naam": "Jaarrekening (synthesedocumenten)",
    "node_type": "fenomeen",
    "definitie_snippet": "Het **gestandaardiseerde overzicht** van de financiële toestand van een onderneming aan het einde van een boekjaar. Bestaat uit drie verplichte onderdelen: (1) de **balans** (vermogen op één moment), (2) de **resultatenrekening** (kosten en opbrengsten over het boekjaar), (3) de **toelichting** (uit",
    "rationale_snippet": ""
  },
  {
    "id": "kapitaalwijziging",
    "naam": "Kapitaalwijziging (verhoging en vermindering)",
    "node_type": "procedure",
    "definitie_snippet": "Een **wijziging van het maatschappelijk kapitaal** (NV) of de **eigen vermogensinbreng** (BV). Twee richtingen: (1) **kapitaalverhoging** — door inbreng in geld, in natura, of door incorporatie van reserves/uitgiftepremies, (2) **kapitaalvermindering** — door werkelijke terugbetaling aan aandeelhoud",
    "rationale_snippet": ""
  },
  {
    "id": "leasing",
    "naam": "Leasing (financieel en operationeel)",
    "node_type": "fenomeen",
    "definitie_snippet": "Een overeenkomst waarbij een **leasinggever** het gebruik van een goed (auto, machine, gebouw) afstaat aan een **leasingnemer** tegen periodieke vergoeding. Twee soorten met fundamenteel verschillende boekhoudkundige verwerking: (1) **Financiële leasing** — de leasingvergoedingen dekken de **integra",
    "rationale_snippet": ""
  },
  {
    "id": "materiele-vaste-activa",
    "naam": "Materiële vaste activa",
    "node_type": "begrip",
    "definitie_snippet": "**Lichamelijke** activa die de onderneming aanhoudt voor gebruik in de productie of levering van goederen of diensten, voor verhuur aan derden of voor bestuurlijke doeleinden. Het MAR groepeert ze onder rubrieken 22 — 26: (22) terreinen en gebouwen, (23) installaties, machines en uitrusting, (24) me",
    "rationale_snippet": ""
  },
  {
    "id": "niet-recurrente-verrichtingen",
    "naam": "Niet-recurrente verrichtingen",
    "node_type": "fenomeen",
    "definitie_snippet": "Kosten en opbrengsten die **niet voortvloeien uit de normale, herhalende bedrijfsuitoefening** van de onderneming en die op de resultatenrekening worden gepresenteerd in afzonderlijke rubrieken: **klasse 66** (niet-recurrente kosten) en **klasse 76** (niet-recurrente opbrengsten). Typisch: niet-recu",
    "rationale_snippet": ""
  },
  {
    "id": "obligatielening",
    "naam": "Obligatielening",
    "node_type": "fenomeen",
    "definitie_snippet": "Een **leningsovereenkomst** waarbij de vennootschap **obligaties** uitgeeft aan beleggers — verhandelbare schuldbewijzen met een vaste of variabele rente en een vooraf bepaalde looptijd (typisch 5 — 15 jaar). De vennootschap ontvangt het kapitaal en betaalt jaarlijkse coupons (rente) plus terugbetal",
    "rationale_snippet": ""
  },
  {
    "id": "onveranderlijkheid-boekingen",
    "naam": "Onveranderlijkheid van de boekingen",
    "node_type": "beginsel",
    "definitie_snippet": "Een boeking mag **na inschrijving niet onzichtbaar gewijzigd, weggelaten of toegevoegd** worden. Wijzigingen zijn wel toegelaten, maar moeten **duidelijk leesbaar blijven** — het oorspronkelijke geschrevene én de correctie moeten allebei zichtbaar zijn. Hetzelfde geldt voor jaarrekening- en inventar",
    "rationale_snippet": ""
  },
  {
    "id": "oprichtingskosten",
    "naam": "Oprichtingskosten",
    "node_type": "fenomeen",
    "definitie_snippet": "Kosten verbonden met de **oprichting, verdere ontwikkeling of herstructurering** van een vennootschap, in het bijzonder: (a) kosten van oprichting of kapitaalverhoging (notariskosten, registratierechten, advies), (b) kosten bij uitgifte van leningen (bankkosten, noteringskosten, publicatiekosten bij",
    "rationale_snippet": ""
  },
  {
    "id": "opsplitsing-eigendom",
    "naam": "Opsplitsing eigendom (vruchtgebruik, opstal, erfpacht)",
    "node_type": "fenomeen",
    "definitie_snippet": "**Zakelijke rechten op onroerende goederen** waarbij de **volle eigendom wordt opgesplitst** in twee tijdelijk gescheiden rechten: (1) het **vruchtgebruik** — recht om het goed te gebruiken en de vruchten te trekken, met onderhoudsplicht (BW art. 578), en (2) de **blote eigendom** — eigendomsrecht z",
    "rationale_snippet": ""
  },
  {
    "id": "overlopende-rekeningen",
    "naam": "Overlopende rekeningen",
    "node_type": "methode",
    "definitie_snippet": "**Balansrekeningen** die het verschil tussen kasstroom en economische toerekening zichtbaar maken aan het eind van het boekjaar. Twee paren: (1) **Over te dragen kosten** (490, actief): al betaalde kosten die op een volgend boekjaar betrekking hebben — vooruitbetaalde huur, premie verzekering 12 maa",
    "rationale_snippet": ""
  },
  {
    "id": "rechten-verplichtingen-buiten-balans",
    "naam": "Rechten en verplichtingen buiten balans",
    "node_type": "fenomeen",
    "definitie_snippet": "**Rechten en verplichtingen** die op balansdatum bestaan maar GEEN actief- of passiefbestanddeel vormen in de zin van het KB WVV (geen vermogensbestanddeel met onmiddellijke balansimpact). Bv. zekerheden gesteld door of voor derden, persoonlijke borgstellingen, ontvangen of gegeven garanties, termij",
    "rationale_snippet": ""
  },
  {
    "id": "regelmatige-boekhouding",
    "naam": "Regelmatige boekhouding",
    "node_type": "fenomeen",
    "definitie_snippet": "Een boekhouding is **regelmatig** als ze drie dingen samen waarmaakt: ze is **passend** voor de aard en omvang van het bedrijf, ze is **volledig** (omvat alle verrichtingen, bezittingen, vorderingen, schulden en verplichtingen) en ze is **onveranderlijk** (boekingen kun je niet zonder spoor wijzigen",
    "rationale_snippet": ""
  },
  {
    "id": "resultaat-categorisatie-beslisboom",
    "naam": "Bedrijfs- · financieel · niet-recurrent &mdash; in welke categorie hoort deze verrichting?",
    "node_type": "synthese",
    "definitie_snippet": "",
    "rationale_snippet": ""
  },
  {
    "id": "resultaatverwerking",
    "naam": "Resultaatverwerking (winst- of verliesbestemming)",
    "node_type": "procedure",
    "definitie_snippet": "Het proces waarbij het boekhoudkundige resultaat na winstbelasting wordt verdeeld over de verschillende bestemmingen: opname van wettelijke reserve, vrije bestemming aan beschikbare reserves, dividenduitkering, vergoeding bestuurders, overdracht naar volgend boekjaar. De resultaatverwerking gebeurt ",
    "rationale_snippet": ""
  },
  {
    "id": "schulden",
    "naam": "Schulden (LT en KT)",
    "node_type": "fenomeen",
    "definitie_snippet": "**Verplichtingen** van de onderneming tot betaling van een vastgesteld bedrag aan een derde, gewaardeerd tegen nominale **terugbetalingswaarde**. Onderscheid op de balans naar resterende looptijd op balansdatum: **schulden op meer dan één jaar** (rubriek VIII, MAR klasse 17 — financiële schulden, ha",
    "rationale_snippet": ""
  },
  {
    "id": "uitgiftepremie",
    "naam": "Uitgiftepremie",
    "node_type": "begrip",
    "definitie_snippet": "Het **verschil tussen de uitgifteprijs van nieuwe aandelen** bij een kapitaalverhoging en de **fractiewaarde** (of vroeger 'nominale waarde'). Geboekt op rekening 11 'Uitgiftepremies' onder eigen middelen. Een uitgiftepremie is GEEN reserve in de zin van de wet: ze wordt fiscaal en boekhoudkundig me",
    "rationale_snippet": ""
  },
  {
    "id": "vereenvoudigde-boekhouding",
    "naam": "Vereenvoudigde boekhouding",
    "node_type": "begrip",
    "definitie_snippet": "Een **alternatieve boekhoudvorm** voor kleine ondernemingen onder de wettelijke drempelwaarden (WER art. III.85), die GEEN dubbele boekhouding vereist. In plaats van een rekeningstelsel met debet/credit gebruikt de onderneming **drie aparte dagboeken**: een financieel dagboek (bank en kas), een aank",
    "rationale_snippet": ""
  },
  {
    "id": "vereffening",
    "naam": "Vereffening van een vennootschap",
    "node_type": "procedure",
    "definitie_snippet": "Het **wettelijk geregelde proces** waarbij een vennootschap haar bedrijfsactiviteit beëindigt: activa worden te gelde gemaakt, schulden worden betaald, het saldo wordt onder de aandeelhouders verdeeld in functie van hun rechten. De vennootschap blijft juridisch bestaan ('in vereffening') tot afsluit",
    "rationale_snippet": ""
  },
  {
    "id": "voorraden",
    "naam": "Voorraden",
    "node_type": "fenomeen",
    "definitie_snippet": "Activa die deel uitmaken van de bedrijfscyclus en die ofwel bij eerste gebruik worden geconsumeerd, ofwel worden verkocht — als zodanig of na een productieproces. Voorraden behoren tot de **vlottende activa** (rubriek 3 MAR). Subcategorieën: (30) grond- en hulpstoffen, (31) goederen in bewerking, (3",
    "rationale_snippet": ""
  },
  {
    "id": "voorzichtigheidsbeginsel",
    "naam": "Voorzichtigheidsbeginsel",
    "node_type": "beginsel",
    "definitie_snippet": "Bij waardering moet de onderneming **oprecht, voorzichtig en te goeder trouw** te werk gaan. Concreet: opbrengsten boek je pas als ze **zeker** zijn (realisatie); kosten en risico's boek je al wanneer ze **waarschijnlijk of zelfs alleen mogelijk** zijn (voorzichtigheid). Verliezen die op balansdatum",
    "rationale_snippet": ""
  },
  {
    "id": "voorzieningen",
    "naam": "Voorzieningen voor risico's en kosten",
    "node_type": "fenomeen",
    "definitie_snippet": "**Schattingen aan passiefzijde** die bestemd zijn om de kosten of verliezen te dekken die uit voorzienbare risico's en lasten **waarschijnlijk** zullen voortvloeien — zonder dat het bedrag of de exacte timing al vaststaat. Geboekt op rekening 16: (160) voorzieningen voor pensioenen en soortgelijke v",
    "rationale_snippet": ""
  },
  {
    "id": "waardeverminderingen",
    "naam": "Waardeverminderingen",
    "node_type": "methode",
    "definitie_snippet": "Onder **waardeverminderingen** verstaat men de correcties op de aanschaffingswaarde van actiefbestanddelen — andere dan die met beperkte gebruiksduur (waarvoor afschrijvingen gelden) — om rekening te houden met al dan niet als definitief aan te merken ontwaardingen bij het afsluiten van het boekjaar",
    "rationale_snippet": ""
  },
  {
    "id": "wettelijke-reserve",
    "naam": "Wettelijke reserve",
    "node_type": "regel",
    "definitie_snippet": "**Verplichte jaarlijkse afhouding** van **5 % van de nettowinst** voor de **wettelijke reserve**, totdat deze reserve **10 % van het maatschappelijk kapitaal** bereikt (NV) of **één tiende van de eigen vermogensinbreng** (BV). Geboekt op rekening 130 'Wettelijke reserve'. Niet uitkeerbaar zolang ze ",
    "rationale_snippet": ""
  }
]
```

## Competentie-summaries

```json
[
  {
    "id": "boeken-aankoop-verkoop-met-btw",
    "titel": "Boeken van een aankoop en verkoop met btw en betaling",
    "procedure_grondslag": {
      "wettelijk_pct": 70,
      "praktijk_pct": 30,
      "motivering": "De boekingsregels (MAR rekening 600 / 411 / 440 / 700 / 451 / 400) zijn voorgeschreven door het KB-MAR; btw-bepaling volgt uit het btw-wetboek. Praktijk komt kijken bij de keuze van sub-rekeningen, betalingsmethode (cash, bank, kruisposten) en gespreide betalingen."
    },
    "gebaseerd_op_concepten": [
      "dubbel-boekhouden",
      "dagboek",
      "bedrijfsvorderingen",
      "schulden",
      "minimum-algemeen-rekeningenstelsel"
    ],
    "eerste_stap": "Verifieer de factuur op vorm en inhoud"
  },
  {
    "id": "boeken-oprichtings-en-kapitaalverhogingskosten",
    "titel": "Boeken van oprichtings- en kapitaalverhogingskosten en hun afschrijving",
    "procedure_grondslag": {
      "wettelijk_pct": 80,
      "praktijk_pct": 20,
      "motivering": "Activering en afschrijving van oprichtingskosten (rubriek 20) zijn voorgeschreven in KB-WVV art. 3:39 en 3:42. Afschrijvingstermijn (maximaal 5 jaar) is wettelijk; de keuze tussen direct ten laste nemen of activeren is een professional judgment-keuze."
    },
    "gebaseerd_op_concepten": [
      "oprichtingskosten",
      "afschrijvingen",
      "eigen-middelen",
      "kapitaalwijziging"
    ],
    "eerste_stap": "Onderscheid oprichtings- van eerste-werkings-kosten"
  },
  {
    "id": "boeken-resultaatverwerking-en-bestemming",
    "titel": "Boeken van resultaatverwerking en bestemming (reserves, dividenden, belasting)",
    "procedure_grondslag": {
      "wettelijk_pct": 75,
      "praktijk_pct": 25,
      "motivering": "De volgorde (eerst vennootschapsbelasting, dan wettelijke reserve, dan beschikbare reserves, dan dividend) en de wettelijke reserve-plicht (WVV art. 5:114, 7:128) zijn wettelijk verankerd. De keuze tussen reserveren en dividend uitkeren is een bestuurs-/AV-beslissing — praktijk."
    },
    "gebaseerd_op_concepten": [
      "resultaatverwerking",
      "wettelijke-reserve",
      "eigen-middelen",
      "uitgiftepremie",
      "bedrijfsresultaat"
    ],
    "eerste_stap": "Bereken het te bestemmen resultaat van het boekjaar"
  },
  {
    "id": "boeken-uitgifte-en-aflossing-obligatielening",
    "titel": "Boeken van uitgifte en aflossing van een obligatielening",
    "procedure_grondslag": {
      "wettelijk_pct": 70,
      "praktijk_pct": 30,
      "motivering": "De boekhoudkundige verwerking (rubriek 170 obligatieleningen op meer dan 1 jaar, 420 obligatieleningen op ten hoogste 1 jaar) en de interestmatching volgen uit KB-WVV art. 3:42 en CBN 2019/07. De keuze tussen rente-spreiding methoden en boekhoudkundige verwerking van uitgiftedisagio is praktijkspecifiek."
    },
    "gebaseerd_op_concepten": [
      "obligatielening",
      "schulden",
      "overlopende-rekeningen",
      "financiele-verrichtingen"
    ],
    "eerste_stap": "Analyseer het emissieprospectus"
  },
  {
    "id": "boeken-voorzieningen-voor-risicos-en-kosten",
    "titel": "Boeken van een voorziening voor risico's en kosten",
    "procedure_grondslag": {
      "wettelijk_pct": 75,
      "praktijk_pct": 25,
      "motivering": "De boekhoudkundige verplichting (KB-WVV art. 3:11 en CBN 2018/25) is wettelijk; de inschatting van waarschijnlijkheid en bedrag vraagt professional judgment."
    },
    "gebaseerd_op_concepten": [
      "voorzieningen",
      "voorzichtigheidsbeginsel",
      "rechten-verplichtingen-buiten-balans",
      "bedrijfsresultaat"
    ],
    "eerste_stap": "Identificeer de potentiële last of risico"
  },
  {
    "id": "boeken-waardeverminderingen-op-vorderingen-en-voorraden",
    "titel": "Boeken van waardeverminderingen op vorderingen en voorraden",
    "procedure_grondslag": {
      "wettelijk_pct": 70,
      "praktijk_pct": 30,
      "motivering": "De boekingsregels (rubrieken 407/409 dubieuze klanten en 30X9 waardevermindering voorraden) zijn voorgeschreven in KB-WVV en KB-MAR; het voorzichtigheidsbeginsel verplicht boeking. Praktijk komt kijken bij de inschatting van het verlies-percentage en het criterium \"dubieus\" (al dan niet meer dan 6 maanden achterstand)."
    },
    "gebaseerd_op_concepten": [
      "waardeverminderingen",
      "voorzichtigheidsbeginsel",
      "bedrijfsvorderingen",
      "voorraden"
    ],
    "eerste_stap": "Identificeer dubieuze vorderingen"
  },
  {
    "id": "kwalificeren-en-boeken-leasing",
    "titel": "Kwalificeren en boeken van leasing (operationeel vs financieel)",
    "procedure_grondslag": {
      "wettelijk_pct": 65,
      "praktijk_pct": 35,
      "motivering": "De boekhoudkundige kwalificatie (KB-WVV art. 3:46 en 3:47, CBN 2015/04) is wettelijk; toepassing op een concreet contract vergt analyse van risico's en voordelen — dat is praktijkbeoordeling."
    },
    "gebaseerd_op_concepten": [
      "leasing",
      "materiele-vaste-activa",
      "afschrijvingen",
      "schulden"
    ],
    "eerste_stap": "Lees het leasingcontract en identificeer kerngegevens"
  },
  {
    "id": "opstellen-afschrijvingsplan-vaste-activa",
    "titel": "Opstellen van het afschrijvingsplan voor materiële vaste activa",
    "procedure_grondslag": {
      "wettelijk_pct": 65,
      "praktijk_pct": 35,
      "motivering": "De plicht tot afschrijving (KB-WVV art. 3:6), de keuze tussen lineair en degressief, en de definitie van afschrijvingsbasis (aanschaffingswaarde minus restwaarde) zijn wettelijk. Bepaling van de economische levensduur, restwaarde en gebruikspatroon vraagt sectorkennis en oordeel."
    },
    "gebaseerd_op_concepten": [
      "afschrijvingen",
      "aanschaffingswaarde",
      "materiele-vaste-activa",
      "waardeverminderingen",
      "waarderingsregels-jaarrekening"
    ],
    "eerste_stap": "Bepaal de aanschaffingswaarde"
  },
  {
    "id": "toepassen-fundamentele-boekhoudbeginselen",
    "titel": "Toepassen van de fundamentele boekhoudbeginselen op een concrete verrichting",
    "procedure_grondslag": {
      "wettelijk_pct": 85,
      "praktijk_pct": 15,
      "motivering": "De vier beginselen (continuïteit, voorzichtigheid, getrouw beeld, onveranderlijkheid) zijn rechtstreeks verankerd in WER art. III.84 en KB-WVV art. 3:1, 3:6 en 3:8. Praktijk komt enkel kijken bij de inschatting \"waarschijnlijk\" of \"zeker\" — die professional judgment vraagt."
    },
    "gebaseerd_op_concepten": [
      "continuiteitsbeginsel",
      "voorzichtigheidsbeginsel",
      "getrouw-beeld",
      "onveranderlijkheid-boekingen",
      "regelmatige-boekhouding"
    ],
    "eerste_stap": "Beschrijf het voorgelegde boekingsfeit"
  },
  {
    "id": "uitvoeren-eindejaarsverrichtingen-en-proefbalans",
    "titel": "Uitvoeren van eindejaarsverrichtingen en opmaken van proefbalans",
    "procedure_grondslag": {
      "wettelijk_pct": 70,
      "praktijk_pct": 30,
      "motivering": "De inventarisplicht (WER art. III.84) en de eindejaarsverrichtingen volgen uit het boekhoudrecht. Het opmaken van de proefbalans en de volgorde van verrichtingen zijn beroepspraktijk — best practices uit ITAA-normen."
    },
    "gebaseerd_op_concepten": [
      "inventaris",
      "afschrijvingen",
      "waardeverminderingen",
      "voorzieningen",
      "overlopende-rekeningen",
      "regelmatige-boekhouding",
      "jaarrekening"
    ],
    "eerste_stap": "Maak een eindejaars-checklist op"
  },
  {
    "id": "verwerken-overlopende-rekeningen-matching",
    "titel": "Verwerken van overlopende rekeningen volgens het matching-principe",
    "procedure_grondslag": {
      "wettelijk_pct": 80,
      "praktijk_pct": 20,
      "motivering": "Het matching-principe + de KB-WVV-rubrieken 490/491 (overlopende activa) en 492/493 (overlopende passiva) zijn wettelijk verplicht via KB-WVV art. 3:11 en art. 3:30. Inschatting van het pro-rata-deel en welke kosten/opbrengsten verschuiven vraagt analyse."
    },
    "gebaseerd_op_concepten": [
      "overlopende-rekeningen",
      "voorzichtigheidsbeginsel",
      "bedrijfsresultaat",
      "waarderingsregels-jaarrekening"
    ],
    "eerste_stap": "Identificeer kosten/opbrengsten die periode-overschrijdend zijn"
  },
  {
    "id": "voeren-boekhouding-vzw-met-economische-activiteit",
    "titel": "Voeren van de boekhouding van een VZW met economische activiteit",
    "procedure_grondslag": {
      "wettelijk_pct": 75,
      "praktijk_pct": 25,
      "motivering": "De groottecriteria voor VZW's (KB 21/10/2018, KB-WVV art. 3:47) zijn wettelijk; keuze regime volgt automatisch. Toepassing op subsidies, vrijwilligers en bijdragen vraagt sectorkennis — beperkte praktijk-marge."
    },
    "gebaseerd_op_concepten": [
      "regelmatige-boekhouding",
      "vereenvoudigde-boekhouding",
      "jaarrekening-vzw-stichting",
      "dubbel-boekhouden",
      "jaarrekening"
    ],
    "eerste_stap": "Bepaal het VZW-regime (microvereniging / klein / groot)"
  },
  {
    "id": "voeren-regelmatige-dubbele-boekhouding",
    "titel": "Voeren van een regelmatige dubbele boekhouding voor een onderneming",
    "procedure_grondslag": {
      "wettelijk_pct": 75,
      "praktijk_pct": 25,
      "motivering": "De plichten (dagboeken, centralisatie, inventaris, bewaring, MAR) staan in WER art. III.83-89 en het KB-MAR; de organisatie ervan (welk pakket, welke uitsplitsing, welke periodiciteit boven het wettelijk minimum) is beroepspraktijk."
    },
    "gebaseerd_op_concepten": [
      "regelmatige-boekhouding",
      "dubbel-boekhouden",
      "dagboek",
      "inventaris",
      "minimum-algemeen-rekeningenstelsel",
      "bewaring-boekhoudstukken"
    ],
    "eerste_stap": "Kwalificeer het boekhoudregime van de cliënt"
  },
  {
    "id": "waarderen-en-boeken-voorraden-fifo-ggp",
    "titel": "Waarderen en boeken van voorraden volgens FIFO of gewogen gemiddelde",
    "procedure_grondslag": {
      "wettelijk_pct": 70,
      "praktijk_pct": 30,
      "motivering": "KB-WVV art. 3:15 verplicht waardering aan aanschaffingswaarde of laagste van aanschaffings-/marktwaarde, en biedt vier methoden (individuele identificatie, FIFO, LIFO sinds 2018 verboden voor jaarrekening, gewogen gemiddelde). Keuze tussen FIFO en GGP is methodische keuze; bestendigheid is wettelijk vereist."
    },
    "gebaseerd_op_concepten": [
      "voorraden",
      "aanschaffingswaarde",
      "waarderingsregels-jaarrekening",
      "waardeverminderingen"
    ],
    "eerste_stap": "Bepaal de aanschaffingswaarde per voorraadbeweging"
  }
]
```

---

## Prompt-referentie (minicursus-glue-v1.md)

# Prompt: Minicursus-glue — Render-fase (v2)

**Doel**: Vul de `<!-- TODO: Opus-glue ... -->` placeholders in de minicursus-skeleton in.

**Model**: claude-opus-4-7 (Opus-subagent)

**Monotoon contract**: Geen feiten-claims, geen wikilinks bedenken, geen wettekst-citaties. **Compact**. Glue is verbindweefsel, geen leerstof.

---

## Jouw rol

Je schrijft minimale, verbindende, pedagogische tekst tussen de deterministisch gerenderde blokken. Je vult GEEN nieuwe feiten in. Je verbindt zonder uit te leggen wat al elders staat.

## Compactheidscontract

Mikt op compacte, dichte tekst zonder kaal te worden. Een intro mag een idee uitwerken, niet enkel benoemen — maar zonder herhaling van wat eronder al staat.

- **Sectie-intro's (oriëntatie / thematisch / competentie)**: typisch 2-3 zinnen. Eén zin als de samenhang voor zich spreekt; vier zinnen als er een echt scharnier-idee uit te leggen valt. Nooit meer dan vier.
- **Leesgids**: 3-4 zinnen — hoe lees je de minicursus, welke logica zit erin.
- **Waarom-po**: 4-6 zinnen — één tot twee beginselen + toepassings-implicaties. Mag ademen, geen wall-of-text.
- **Synthese-stappenplan**: 6-9 zinnen — werkschema-stijl, end-to-end-overzicht.
- **Examenfocus**: 4-6 zinnen — twee tot drie denkpatronen, met voldoende grond om bruikbaar te zijn.
- **Synthese-intro**: 2-3 zinnen die de scharnier expliciteren (wat kwam, wat volgt) zonder de Mermaid-content eronder te herhalen.
- **Bij twijfel**: liever kort en dicht dan opgeklopt — maar niet zo kaal dat de student de pedagogische verbinding moet zelf invullen.

## Anti-fabricatie-regels (hard)

1. **Geen feiten-claims**, geen wetsartikelnummers, geen specifieke percentages of bedragen die je niet in records-summaries ziet.
2. **Geen nieuwe wikilinks verzinnen.** De skeleton bevat ze al.
3. **Geen herhaling van de synthese-record-inhoud.** De Mermaid + kerninzichten staan eronder. Glue-intro voegt scharnier toe, geen overlap.
4. **Rationale = beginselen-inzicht, niet examen-truc.** "Waarom werkt dit zo" — niet "dit wordt vaak gevraagd".
5. **Bij gebrek aan grondslag: kort en neutraal.** Eerder "Dit hoofdstuk behandelt X." dan vrije uitvinding.
6. **Geen oude examen-vragen of percentages opnoemen.** Examenfocus is meta-niveau (welk denkpatroon), niet vraagspoilers.

## Workflow

Open `content/studiemateriaal/<X.Y>-<slug>/minicursus.md` met de Edit-tool. Vervang elke `<!-- TODO: Opus-glue X -->` regel door de bedoelde tekst, in volgorde. Geen JSON-output — direct editen.

## Stijl

- **Toon**: helder, direct, actief — zoals een ervaren collega
- **"Je"-aanspraak**, niet "men" of "de student"
- **Geen bullets in glue-tekst** (bullets staan al in skeleton)
- **Nederlands**
- **Geen euro-bedragen of cast-namen** in glue (die staan in records); generieke termen
- **Geen "hieronder zie je..." of "in de volgende sectie..."** — laat de structuur zelf spreken

## Verificatie

Na invullen:
1. `grep -c "<!-- TODO: Opus-glue" content/studiemateriaal/<X.Y>-*/minicursus.md` moet 0 teruggeven
2. Totale word-count zit doorgaans tussen 700 en 1100 woorden glue-tekst voor heel het document — minder dan de "uitgebreid"-stijl (1500+) maar voldoende ruimte voor pedagogische verbinding.
3. Geen overlap tussen synthese-intro en de synthese-record-inhoud die eronder rendert

Geen commit. De hoofdsessie commit.

