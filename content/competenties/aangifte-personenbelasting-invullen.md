---
tags: ["2.2", wip, competentie]
niveau: integratie
status: draft
programmaonderdelen: ["2.2"]
itaa-lex-secties:
  - II (WIB92 art. 305-345)
  - II (KB/WIB92 — uitvoeringsbepalingen aangifte)
procedure-grondslag: "Wettelijke aangifteplicht (WIB92 art. 305) — het invulproces zelf is geen genormeerde procedure maar wordt gestructureerd door de aangifte als formulier en door beroepspraktijk."
bouwversie: 2
---

# Aangifte personenbelasting invullen

De aangifte is het **enige** formele instrument waarop de FOD Financiën de aanslag in de personenbelasting kan vestigen ([[bronnen/wetteksten/II-wib92|WIB92 art. 305]]). Een onvolledige of foute aangifte kost de cliënt geld (te hoge aanslag, niet-toegekende verminderingen) of stelt hem bloot aan controles, belastingverhogingen en strafsancties. Deze competentie beschrijft hoe je systematisch alle vakken doorloopt, de juiste informatie verzamelt en de aangifte tijdig en correct indient namens de cliënt.

Onderscheid met andere competenties:
- **[[belastingberekening-personenbelasting-uitvoeren|Belastingberekening personenbelasting uitvoeren]]**: rekent de belasting uit eens de aangifte volledig is — focus op het tarievenschema en de verminderingen
- **[[fiscaal-advies-personenbelasting-formuleren|Fiscaal advies personenbelasting formuleren]]**: adviesopdracht — keuzes vooraf (vóór de aangifte zelf), bv. werkelijke vs. forfaitaire kosten, voorafbetalingen, optimalisatie

> [!info]- Grondslag van deze werkwijze (🤖 70% · ⚖️ 30%)
> De aangifteplicht zelf is wettelijk geregeld ([[bronnen/wetteksten/II-wib92|WIB92 art. 305-315]]) en de structuur van de aangifte volgt de vakindeling van het uitvoeringsbesluit ([[bronnen/wetteksten/II-KB-wib92|KB/WIB92]]). Het **invulproces** als gestructureerde werkwijze is echter **geen genormeerde procedure** — er bestaat geen ITAA-norm of CBN-advies dat per vak voorschrijft hoe te werk te gaan. De stappen hieronder volgen de courante beroepspraktijk: verzamelen → kwalificeren → invullen → controleren → indienen → archiveren.

## Aanbevolen werkwijze

### 1. 🎯 Mandaatscope vaststellen

> 📥 **Nodig**:
> - Vraag van de cliënt
> - Bestaande relatie met de cliënt (eerste aangifte of recurring)
>
> 📤 **Uitkomst**:
> - Mandaatomvang: enkel aangifte, of ook bezwaar/voorafbetalingen/advies?
> - Tijdslijn: termijn waarbinnen aangifte moet ingediend zijn

**Waarom**: zonder duidelijke scope ontstaat onduidelijkheid over verantwoordelijkheid (cliënt vs. mandataris) en aansprakelijkheid bij fouten of vergetelheden.

Bepaal contractueel (in de [[relaties-met-clienten#-opdrachtbrief-verplicht-voor-iedere-opdracht|opdrachtbrief]]) of de opdracht beperkt is tot **enkel het invullen** van de aangifte op basis van wat de cliënt aanlevert, dan wel of het mandaat ruimer is en ook **proactief advies** over voorafbetalingen, optimalisatiekeuzes (forfait vs. werkelijke kosten) en eventueel **bezwaarschriften** omvat.

Informeer de cliënt over de **indieningstermijn** voor mandataris-aangiftes (~ eind oktober van het aanslagjaar — verlengde termijn t.o.v. burger zelf).

> [!info]- Concreet: terugkerend mandaat
>
> Een vaste cliënt sinds 5 jaar — opdrachtbrief vermeldt automatisch hernieuwing van de aangiftecompetentie. Geen noodzaak van nieuwe formele opdracht; wel jaarlijks updaten van de gegevens (loonfiches 281.10, attesten, …).
>
> 🤖 *AI-aanvulling*

> [!warning]- De mandataris is aansprakelijk voor wat hij invult op basis van de aangeleverde stukken
> ❌ *"Als de cliënt me een fiche niet bezorgt, ben ik er niet voor aansprakelijk."*
>
> De mandataris heeft een **inspanningsverbintenis** om de aangifte zo correct mogelijk in te vullen op basis van de **aangeleverde** stukken én op basis van de **gegevens die hij redelijkerwijze had moeten kennen** (bv. via de [[#-3--gegevens-elektronisch-verzamelen|MyMinfin-vooruitvulling]]). Als de cliënt een loonfiche vergeet en de mandataris vraagt er niet naar terwijl die in MyMinfin zichtbaar was, kan de aansprakelijkheid bij de mandataris liggen — vooral bij belastingverhoging wegens niet-aangifte.
>
> 🤖 *AI-aanvulling*

---

### 2. 🔍 Burgerlijke staat en aanslagregime bepalen

> 📥 **Nodig**:
> - Burgerlijke staat van de cliënt (gehuwd, wettelijk samenwonend, alleenstaand, …)
> - Eventuele wijziging tijdens het inkomstenjaar (huwelijk, echtscheiding, overlijden)
>
> 📤 **Uitkomst**:
> - Aanslagregime: gezamenlijke aanslag of afzonderlijke aanslag
> - Eén aangifte (alleenstaande) of één gemeenschappelijke aangifte voor partners

**Waarom**: het aanslagregime bepaalt of er één of twee aangiftes worden ingediend — een verkeerde indiening leidt tot een ambtshalve correctie of tot een verkeerde belasting (verlies van [[gezinsfiscaliteit#-huwelijksquotiënt|huwelijksquotiënt]], verkeerde toerekening van [[gezinsfiscaliteit#-personen-ten-laste|personen ten laste]]).

Bepaal het regime aan de hand van de [[gezinsfiscaliteit#-burgerlijke-staat-in-fiscalibus|burgerlijke staat]] op **31 december** van het inkomstenjaar (of speciaal regime bij wijziging tijdens het jaar — zie [[gezinsfiscaliteit#️-jaar-van-huwelijk-of-wettelijke-samenwoning|huwelijk]] / [[gezinsfiscaliteit#️-jaar-van-scheiding-van-tafel-en-bed-of-feitelijke-scheiding|scheiding]] / [[gezinsfiscaliteit#️-jaar-van-overlijden|overlijden]]).

```
Vak II — Persoonlijke gegevens
  - Burgerlijke staat: gehuwd ☐ / wettelijk samenwonend ☐ / weduwe-naar ☐ / gescheiden ☐ / alleenstaand ☐
  - Wijziging gedurende inkomstenjaar: ja ☐ datum: __/__/____
  - Personen ten laste: kinderen [aantal] / andere [aantal]
  - Persoon met handicap: zelf ☐ partner ☐ ten laste ☐
```

> [!info]- Concreet: feitelijk samenwonend
>
> Twee partners wonen al 8 jaar samen, hebben 2 kinderen, geen wettelijke samenwoningsverklaring → **afzonderlijke aanslagen**. De ouder bij wie de kinderen gedomicilieerd zijn, vermeldt ze als ten laste; de andere ouder geeft niets aan voor de kinderen tenzij er fiscaal co-ouderschap is. Twee aparte aangiftes, geen huwelijksquotiënt mogelijk.
>
> 🤖 *AI-aanvulling*

> [!warning]- Bij een wijziging tijdens het jaar gelden specifieke regimes
> ❌ *"Een echtpaar dat in juni huwt, doet onmiddellijk een gezamenlijke aangifte voor dat jaar."*
>
> Voor het **jaar van huwelijk of wettelijke samenwoning** worden de partners nog **afzonderlijk** belast als alleenstaanden ([[bronnen/wetteksten/II-wib92|WIB92 art. 126, §2, 1°]]) — de gezamenlijke aanslag begint pas vanaf het eerste **volledige** kalenderjaar. Wie deze regel mist, dient een verkeerde aangifte in en mist mogelijk de [[gezinsfiscaliteit#-huwelijksquotiënt|huwelijksquotiënt]]-berekening. Bij scheiding of overlijden gelden eigen regels — zie [[gezinsfiscaliteit#️-jaar-van-overlijden|jaar van overlijden]].
>
> 🤖 *AI-aanvulling*

---

### 3. 🔍 Gegevens elektronisch verzamelen

> 📥 **Nodig**:
> - Toegang tot **MyMinfin** (Tax-on-web mandataris)
> - Volmacht of mandaat van de cliënt
>
> 📤 **Uitkomst**:
> - Vooruitgevulde aangifte met automatisch beschikbare gegevens (loonfiches 281.10, 281.20, attesten verzekeringen, hypotheek, kinderoppas)
> - Lijst van ontbrekende gegevens die manueel ingewonnen moeten worden

**Waarom**: het overgrote deel van de gegevens wordt sinds enkele jaren **automatisch** aangeleverd door werkgevers, banken, verzekeringsmaatschappijen en kinderoppasinstellingen. Wie nog steeds enkel met papieren documenten van de cliënt werkt, riskeert dubbele invoerfouten of vergetelheden — én wordt beperkt door de cliëntcompliance.

Open **MyMinfin** (eservices.minfin.fgov.be) met je mandataris-toegang. Selecteer de cliënt en open Tax-on-web. De vooruitgevulde aangifte vermeldt:

- Loonfiches 281.10, 281.20, 281.18 (vervangingsinkomsten, pensioenen)
- Attesten levensverzekering, pensioensparen, hypothecaire lening (281.61, 281.62, 281.63, 281.71)
- Attesten kinderoppas
- KI's van geregistreerde onroerende goederen
- Onroerende voorheffing
- Eerder ingediende voorafbetalingen
- Belastingvermindering aandelen starter (Tax Shelter)

Maak een lijst van wat **niet** vooringevuld is en wat dus van de cliënt moet komen:
- Werkelijke beroepskosten met bewijsstukken
- Buitenlandse inkomsten (OG, beroep, kapitalen)
- Onderhoudsuitkeringen (gegeven of ontvangen)
- Giften aan erkende instellingen
- Energiebesparende investeringen (gewestelijk)

> [!tip]- Synchroniseer voor je begint
>
> Wacht na 1 mei van het aanslagjaar — de vooringevulde gegevens worden dan grotendeels door de FOD Financiën aangevuld. Vóór die datum is de aangifte vaak nog leeg en moet je alles manueel ingeven, waarna de automatische gegevens later overschrijven en je werk dubbel doen.

> [!info]- In de praktijk: import MyMinfin in aangiftesoftware
>
> Bij gebruik van aangiftesoftware (Biztax, Sofisk, Irix, …) is het importeren van de MyMinfin-vooruitvulling een **expliciete stap**, geen automatisme bij het openen van het dossier. Plan deze importstap in je workflow vóór het begin van elke aangifte — zo vermijd je dubbele invoer of vergeten vooringevulde gegevens die de FOD al voor jou heeft opgezocht.
>
> 🤖 *AI-aanvulling*

---

### 4. 🔀 Inkomsten kwalificeren per categorie

> 📥 **Nodig**:
> - Verzamelde gegevens uit [[#-3--gegevens-elektronisch-verzamelen|stap 3]]
> - Aanvullende stukken van de cliënt
>
> 📤 **Uitkomst**:
> - Elke ontvangen som correct gekwalificeerd in de juiste [[personenbelasting-basisbegrippen#-inkomstencategorieën|inkomstencategorie]]: OG, beroeps, roerend, divers
> - Bedrag en aangiftecode bepaald per som

**Waarom**: een verkeerde kwalificatie leidt tot toepassing van het verkeerde tarief en de verkeerde aftrekken. Een dividend dat als loon wordt aangegeven wordt aan progressieve tarieven belast in plaats van aan 30% RV; een meerwaarde op aandelen die als roerend inkomen wordt aangegeven blijft belastbaar terwijl ze als normaal beheer privévermogen vrijgesteld is.

Per ontvangen som: stel jezelf de vraag *"in welke inkomstencategorie hoort dit?"* — en vul in het juiste vak van de aangifte.

| Categorie | Vakken aangifte | Materie-fiche |
|---|---|---|
| **Onroerend** | III (Belgisch OG), XIII (buitenlands OG) | [[inkomsten-onroerende-goederen]] |
| **Beroeps** (loon, vervangingsinkomsten, pensioenen) | IV, V | [[beroepsinkomsten-personenbelasting]] |
| **Beroeps** (winsten, baten, bedrijfsleidersbezoldiging) | XV, XVI, XVII | [[beroepsinkomsten-personenbelasting]] |
| **Roerend** | VII | [[roerende-inkomsten-personenbelasting]] |
| **Divers** | XII | [[diverse-inkomsten-personenbelasting]] |
| **Aftrekbare uitgaven** | VIII (giften, onderhoudsuitkeringen) | [[onderhoudsuitkeringen-fiscaal]], [[belastingverminderingen-federaal#-giften\|Giften federaal]] |
| **Belastingverminderingen** (gewest + federaal) | IX, X | [[belastingverminderingen-gewestelijk]], [[belastingverminderingen-federaal]] |
| **Voorafbetalingen** | XI | [[voorafbetalingen-personenbelasting]] |

> [!warning]- Een zelfde geldsom kan verschillend gekwalificeerd worden naar gelang context
> ❌ *"Een meerwaarde op aandelen wordt altijd belast als roerend inkomen."*
>
> Een meerwaarde op aandelen is in beginsel **niet belastbaar** in de PB (kwalificeert als normaal beheer van het privévermogen — geen inkomstencategorie), tenzij:
> - **Speculatieve verrichting** (kort tijdsverloop, geleende fondsen) → diverse inkomsten 33% ([[bronnen/wetteksten/II-wib92|WIB92 art. 90, 1°]])
> - **Beroepsmatig** (zelfstandige effectenmakelaar) → beroepsinkomen
> - **Aanmerkelijke deelneming** (> 25%) verkocht aan buitenlandse vennootschap → 16,5% ([[bronnen/wetteksten/II-wib92|WIB92 art. 90, 9°]])
>
> De juiste kwalificatie hangt af van de feitelijke context. Verkeerde kwalificatie kan zowel een te hoge als een te lage aanslag opleveren.
>
> 🤖 *AI-aanvulling*

> [!info]- Concreet: huurinkomsten van bedrijfsleider
>
> Een zaakvoerder verhuurt zijn appartement aan zijn eigen bv voor € 24 000/jaar. Geïndexeerd KI = € 1 800. De [[inkomsten-onroerende-goederen#-herkwalificatie-van-huurinkomsten-van-bedrijfsleider|herkwalificatie van huurinkomsten van bedrijfsleider]] geldt: drempel = € 1 800 × 5/3 × 5,46 = € 16 380. Het deel boven de drempel (€ 24 000 − € 16 380 = € 7 620) wordt geherkwalificeerd als **bezoldiging bedrijfsleider** en aangegeven in vak XVII — niet in vak III als gewone huur.
>
> 🤖 *AI-aanvulling*

---

### 5. 🔢 Aftrekken en kosten optimaliseren

> 📥 **Nodig**:
> - [[#-4--inkomsten-kwalificeren-per-categorie|Gekwalificeerde brutoinkomsten]]
> - Bewijsstukken werkelijke kosten
>
> 📤 **Uitkomst**:
> - Optimale keuze tussen [[beroepsinkomsten-personenbelasting#-werkelijke-vs-forfaitaire-beroepskosten|forfaitaire vs. werkelijke beroepskosten]]
> - Alle aftrekken correct ingevuld

**Waarom**: dit is de belangrijkste optimalisatie-stap waarbij de mandataris **werkelijke meerwaarde** levert. Forfait of werkelijke kosten kiezen kan honderden tot duizenden euro's verschil maken; vergeten aftrek voor onderhoudsuitkeringen, giften of pensioensparen is direct verlies.

**Methodiek**:

1. **Werkelijke kosten verzamelen** (woon-werkverkeer, thuiskantoor, vakliteratuur, beroepskleding, vakbondsbijdragen)
2. **Berekenen vergelijking**: werkelijke kosten vs. forfait (cijferzakboekje aj. 2026: max ~ € 5 580 voor werknemers, ~ € 2 950 voor bedrijfsleiders)
3. **Keuze** maken — de hoogste van de twee. Eens gekozen → consistent voor alle beroepskosten van die persoon (niet per type)
4. **Aftrekken inzetten** voor onderhoudsuitkeringen, giften, pensioensparen, dienstencheques (onder de juiste vakken)

```
Vak IV — Bezoldigingen werknemers  ⚠️ codes te verifiëren via aangifte-PB-2025 FOD Financiën
  Code 1250  Brutoinkomen                     € 50 000,00
  Code 1258  Sociale bijdragen werknemer       € −6 535,00  (auto van 281.10)
  Code 1271  Werkelijke beroepskosten          € 8 350,00   (indien hoger dan forfait)
  Code 1289  Forfaitaire beroepskosten         (auto-berekend bij keuze forfait)
```

> [!warning]- Bij wettelijk samenwonende of gehuwde partners: kosten en aftrekken doorrekenen voor decumul
> ❌ *"De totale gezinsbeoefkosten worden op de hoogste verdiener toegerekend voor maximaal voordeel."*
>
> Door de [[personenbelasting-basisbegrippen#️-decumul|decumul]] worden beroepskosten **strikt persoonlijk** toegerekend aan de partner die ze gemaakt heeft. Werkelijke beroepskosten van partner A behoren tot het beroepsinkomen van A — ze kunnen niet naar B worden overgedragen. Voor onderhoudsuitkeringen, giften en pensioensparen geldt wel een specifieke verdelingsregel binnen de gezamenlijke aanslag.
>
> 🤖 *AI-aanvulling*

---

### 6. ✅ Aangifte controleren — kruislingse coherentiechecks

> 📥 **Nodig**:
> - Volledig ingevulde aangifte (alle vakken)
>
> 📤 **Uitkomst**:
> - Vastgestelde inconsistenties opgelost
> - Voorgestelde aanslag (Tax-on-web simulator) bekeken en geëvalueerd

**Waarom**: een aangifte zonder controle is een aangifte met fouten. De Tax-on-web simulator geeft direct de geraamde belasting terug — als die afwijkt van wat redelijk te verwachten is, is er ergens iets mis.

**Standaard checklist**:

```
[ ] Alle vakken doorlopen — geen leeg gelaten zonder reden?
[ ] Loonfiches 281.10/281.20: bedragen kloppen met cliëntinformatie?
[ ] Personen ten laste correct toegerekend? (1 januari aj. peildatum)
[ ] Onroerend goed eigen woning correct aangeduid (vrijgesteld)?
[ ] Buitenlandse inkomsten: aangegeven (vak XIII)?
[ ] Forfait of werkelijke kosten consistent gekozen per persoon?
[ ] Onderhoudsuitkeringen: 80%-regel toegepast, voorwaarden vervuld?
[ ] Federale + gewestelijke verminderingen ingevuld waar van toepassing?
[ ] Voorafbetalingen ingevuld vanuit MyMinfin?
[ ] Bedrijfsvoorheffing op loonfiche overeen met ingevulde RV?
[ ] Tax-on-web simulator: berekende belasting redelijk t.o.v. vorig jaar?
```

**Onverwacht hoge of lage aanslag**: zoek de oorzaak vóór indiening. Vaak: ten laste niet ingevuld, vermindering vervangingsinkomsten verkeerd, vergeten aftrek pensioensparen of giften.

> [!info]- Concreet: simulator-controle
>
> Vorig aanslagjaar: te betalen € 2 500. Dit jaar simulator: te betalen € 12 000 — vergelijkbaar inkomen. Onderzoek: vergeten huwelijksquotiënt toe te passen na huwelijk in jaar X-1; werkelijke kosten gekozen terwijl forfait voordeliger zou zijn; vergeten gewestelijke vermindering dienstencheques. Drie correcties later: te betalen € 2 800.
>
> 🤖 *AI-aanvulling*

---

### 7. 🔒 Tijdig indienen en bevestiging archiveren

> 📥 **Nodig**:
> - Goedgekeurde aangifte (door cliënt en mandataris)
>
> 📤 **Uitkomst**:
> - Aangifte ingediend via Tax-on-web
> - Bevestigingsattest opgeslagen in cliëntdossier
> - Aanslagbiljet binnen redelijke termijn opgevolgd

**Waarom**: niet-tijdige indiening leidt automatisch tot **belastingverhoging** (10% tot 200%) en mogelijk **ambtshalve aanslag** met omkering van de bewijslast ([[bronnen/wetteksten/II-wib92|WIB92 art. 351, 444]]).

Indien via mandataris: indieningstermijn is **eind oktober** van het aanslagjaar (voor aj. 2026 indicatief, te bevestigen via fiscale kalender). Indienen via Tax-on-web Mandataris.

**Na indiening**:
- Print of download het **PDF-bevestigingsattest** (Tax-on-web)
- Sla op in het cliëntdossier (digitaal, met datumstempel)
- Voorzie reminders voor het verwachte aanslagbiljet (~ september-december van het aanslagjaar; voor laattijdige aangiftes mogelijk later)

**Bewaarplicht**: de mandataris bewaart de stukken minstens **7 jaar** vanaf 1 januari van het aanslagjaar (gelijklopend met de fiscale bewaartermijn van de cliënt — [[bronnen/wetteksten/II-wib92|WIB92 art. 315]]).

> [!warning]- De aangifte is rechtsgeldig vanaf indiening, niet vanaf het ontvangen bevestigingsattest
> ❌ *"Ik moet wachten op het bevestigingsattest van Tax-on-web voor de aangifte officieel is."*
>
> De aangifte is **ingediend zodra de Tax-on-web sessie wordt afgesloten met "Indienen"**. Het bevestigingsattest is een handig bewijsstuk voor de mandataris/cliënt, maar de indiening zelf is rechtsgeldig vanaf druk op "Indienen". Bij een crash of verbroken verbinding: ALTIJD nakijken of de aangifte werkelijk is ingediend (status "ingediend" in de cliëntfiche).
>
> 🤖 *AI-aanvulling*

---

### 7c. 🔒 Voorstel van vereenvoudigde aangifte (VVA) — afwijkende stap (indien VVA ontvangen)

> 📥 **Nodig**:
> - Cliënt heeft een VVA ontvangen (papier of MyMinfin)
>
> 📤 **Uitkomst**:
> - VVA gecontroleerd, gewijzigd indien nodig — of stilzwijgend aanvaard

**Waarom**: een VVA is **automatisch** de aangifte — bij stilzwijgen wordt het voorstel aanvaard. Wie niet controleert riskeert een verkeerde aanslag (bv. vergeten aftrekken, onjuiste persoon ten laste).

Voor cliënten met enkel **eenvoudige** inkomsten (loon, pensioen, gekend OG) wordt door de FOD Financiën een **vooraf ingevuld voorstel van aangifte** verstuurd. De cliënt (of mandataris) controleert:

1. Alle inkomstencategorieën correct opgenomen?
2. Personen ten laste correct?
3. Geen ontbrekende aftrekken (giften, onderhoudsuitkeringen, pensioensparen)?

**Bij akkoord**: niets ondernemen — het VVA wordt automatisch de aangifte.

**Bij wijzigingen**: corrigeren via Tax-on-web binnen de geldige termijn (~ eind juni / mid-juli). Mandataris-termijn is hier niet automatisch van toepassing — controleer.

> [!info]- In de praktijk: systematische VVA-screening
>
> Tax-on-web Mandataris geeft een overzicht van alle cliënten met een VVA. Zorg dat je workflow een **systematische VVA-check** bevat: minstens screenen op ontbrekende giften-attesten, pensioensparen en gewestelijke verminderingen die de FOD niet automatisch oppikt. Veel kantoren missen hierdoor verminderingen van enkele honderden euro's per cliënt.
>
> 🤖 *AI-aanvulling*

---

## Voorbeelden

> [!example]- Standaardgezin met werknemerinkomen en hypotheek
>
> **Situatie**: Echtpaar (gehuwd 2018), beide werknemers, 2 kinderen ten laste (8 en 11 jaar), eigen woning met hypothecaire lening (sinds 2017, dus woonbonus van toepassing in Vlaanderen — in uitdoving), gewone gezinsuitgaven.
>
> - A: brutoloon € 65 000, BV ingehouden € 14 200, RSZ € 8 500
> - B: brutoloon € 38 000, BV ingehouden € 5 800, RSZ € 4 970
> - Hypotheekaflossingen 2025: kapitaal € 8 200 + interesten € 4 600
> - Pensioensparen A: € 1 020 (max)
> - Giften: € 200 aan Rode Kruis
>
> **Conclusie**: Gezamenlijke aanslag, decumul toegepast, geïntegreerde woonbonus toegepast (gewestelijk Vlaams), pensioensparen en giften als federale verminderingen. Geraamde aanslag: te ontvangen ~ € 1 800 (door gewestelijke woonbonus en federale verminderingen).
>
> **Grondslag**: [[bronnen/wetteksten/II-wib92|WIB92 art. 30, 1°, 126-128, 130, 145/3, 145/24, 145/33]]; [[gezinsfiscaliteit#-burgerlijke-staat-in-fiscalibus|Burgerlijke staat]]; [[beroepsinkomsten-personenbelasting]].
>
> **Redenering**:
> - Stap 1-2: Gezamenlijk gehuwd, 2 kinderen ten laste op 1 januari 2026 → één gemeenschappelijke aangifte
> - Stap 3: Loonfiches 281.10 vooringevuld via MyMinfin; hypotheekattest 281.61 vooringevuld
> - Stap 4: Beide bezoldigingen in vak IV; eigen woning vrijgesteld in vak III
> - Stap 5: Forfaitaire kosten gekozen voor beiden (geen significante werkelijke kosten); woonbonus, pensioensparen, giften ingevuld
> - Stap 6: Simulator Tax-on-web → te ontvangen € 1 800 (consistent met vorig jaar)
> - Stap 7: Indienen via Tax-on-web Mandataris vóór 31 oktober 2026
>
> 🤖 *AI-aanvulling*

> [!example]- Bedrijfsleider met verhuur aan eigen vennootschap
>
> **Situatie**: Zaakvoerder X van bv ABC, alleenstaand. Bezoldiging € 80 000, eigen woning, verhuurt zijn appartement aan zijn bv voor € 24 000/jaar (geïndexeerd KI = € 1 800, bedrijfsruimte voor administratie). Voorafbetalingen 2025: € 18 000 (€ 6 000 × VA1, € 6 000 × VA2, € 6 000 × VA3, niets in VA4).
>
> **Conclusie**: Bezoldiging bedrijfsleider in vak XVII; deel huur (€ 7 620) geherkwalificeerd als bezoldiging volgens herkwalificatieregel; rest huur (€ 16 380) in vak III als onroerend inkomen. Voorafbetalingen ingevuld in vak XI. Geraamde aanslag: te betalen ~ € 4 500 (VA en BV onvoldoende voor totale aanslag).
>
> **Grondslag**: [[bronnen/wetteksten/II-wib92|WIB92 art. 32 alinea 2, 3°, art. 7, 130, 157]]; [[inkomsten-onroerende-goederen#-herkwalificatie-van-huurinkomsten-van-bedrijfsleider|Herkwalificatie huur bedrijfsleider]].
>
> **Redenering**:
> - Stap 1: Mandataris-mandaat tot indienen aangifte, met advies over voorafbetalingen voor volgend jaar
> - Stap 2: Alleenstaand, geen wijziging tijdens jaar
> - Stap 3: Loonfiche 281.20 (bedrijfsleider) vooringevuld; KI van appartement vooringevuld
> - Stap 4: Cruciale kwalificatie — huur boven drempel = bezoldiging. Berekening drempel: € 1 800 × 5/3 × 5,46 = € 16 380. Excess € 7 620 → vak XVII. Rest € 16 380 → vak III met 40% forfaitaire kostenaftrek.
> - Stap 5: Forfaitaire kosten bedrijfsleider toegepast (3%, max ~ € 2 950); persoonlijke sociale bijdragen zelfstandige aftrekbaar
> - Stap 6: Simulator → te betalen € 4 500. Verklaring: VA4 ontbroken in december 2025 → vermeerdering toegepast (~ € 200 extra)
> - Stap 7: Indienen + advies aan cliënt: voor inkomstenjaar 2026 voorafbetalingen verhogen en VA4 inplannen om vermeerdering te vermijden
>
> 🤖 *AI-aanvulling*

## Motiveren op het examen

**Een volledig antwoord bevat:**
1. Aanslagregime: gezamenlijk of afzonderlijk (op basis van burgerlijke staat op 1 januari aanslagjaar)
2. Kwalificatie van elke som per inkomstencategorie (OG, beroeps, roerend, divers) met aangiftecode
3. Toepassing van specifieke regels (herkwalificatie huur, decumul, huwelijksquotiënt) waar relevant
4. Optimale keuze tussen forfait en werkelijke beroepskosten + bewijs
5. Toepassing van federale en gewestelijke verminderingen waar van toepassing
6. Conclusie: geraamde belasting + opvolgingen (voorafbetalingen volgend jaar, eventueel bezwaar)

### Voorbeeldvragen

> [!question]- Eigen woning vrijstelling
>
> Een rijksinwoner met eigen woning waarvan het geïndexeerd KI € 2 200 bedraagt: moet hij dit KI vermelden in zijn aangifte?
>
> > [!success]- Antwoord
> >
> > **Vermelden ja, maar het inkomen is vrijgesteld.**
> >
> > Het KI van de eigen woning wordt vermeld in vak III van de aangifte (informatieve verplichting), maar het inkomen zelf is **volledig vrijgesteld** ([[bronnen/wetteksten/II-wib92|WIB92 art. 12, §3]]). Het verhoogt de belastbare grondslag niet. Wel moet de eigen woning expliciet aangeduid worden om het onderscheid met andere niet-eigen woningen (waar geïndexeerd KI × 1,40 wel belastbaar is) te garanderen.
> >
> > *Zie: [[inkomsten-onroerende-goederen#️-eigen-woning|Eigen woning]]*
>
> 🤖 *AI-aanvulling*

> [!question]- Termijn aangifte mandataris
>
> Een belastingplichtige laat zijn aangifte invullen door een accountant. Tegen welke datum moet deze aangifte ingediend zijn voor inkomstenjaar 2025 (aj. 2026)?
>
> > [!success]- Antwoord
> >
> > **Eind oktober 2026 (indicatief — exacte datum jaarlijks bevestigd door FOD Financiën).**
> >
> > Voor aangiftes ingediend door een mandataris (accountant of belastingadviseur) gelden **verlengde** indieningstermijnen — typisch eind oktober of begin november van het aanslagjaar — om te compenseren voor de werklast van professionele kantoren. De cliënt zelf moet zijn aangifte vroeger indienen (mid-juli voor Tax-on-web zelf, eind juni voor papier). De mandataris-termijn wordt jaarlijks bevestigd door de FOD Financiën.
> >
> > *Zie: [[personenbelasting-basisbegrippen#-aangifteplicht|Aangifteplicht]]*
>
> 🤖 *AI-aanvulling*

> [!question]- Forfaitaire vs. werkelijke kosten
>
> Een werknemer heeft het volgende: brutoloon € 45 000, woon-werkverkeer 30 km/dag, vakliteratuur € 250, vakbondsbijdrage € 180. Forfait of werkelijke kosten?
>
> > [!success]- Antwoord
> >
> > **Bereken beide en kies de hoogste.**
> >
> > - **Forfait** (cijferzakboekje aj. 2026): ~ € 5 580 max
> > - **Werkelijke kosten**: woon-werk (30 × 220 dagen × 2 × € 0,15) ≈ € 1 980 + vakliteratuur € 250 + vakbond € 180 ≈ € 2 410
> >
> > → **Forfait wint** (€ 5 580 > € 2 410).
> >
> > Bij hogere woon-werkafstanden (bv. 80 km/dag) of bij specifieke beroepskosten (computer, beroepskleding, eigen kantoor thuis) kan het tij keren — altijd berekenen, niet veronderstellen. Eens gekozen → consistent voor alle kosten van die persoon.
> >
> > *Zie: [[beroepsinkomsten-personenbelasting#-werkelijke-vs-forfaitaire-beroepskosten|Werkelijke vs. forfaitaire beroepskosten]]*
>
> 🤖 *AI-aanvulling*

> [!question]- Ambtshalve aanslag bij niet-aangifte
>
> Wat zijn de gevolgen als een belastingplichtige geen aangifte indient binnen de termijn?
>
> > [!success]- Antwoord
> >
> > **Drie gevolgen**: (1) ambtshalve aanslag, (2) belastingverhoging 10-200%, (3) omkering van de bewijslast voor bezwaar.
> >
> > Bij niet-aangifte stuurt de FOD Financiën een **herinnering** met een laatste termijn. Bij blijvende stilte: **ambtshalve aanslag** ([[bronnen/wetteksten/II-wib92|WIB92 art. 351]]) — de administratie schat het inkomen op basis van beschikbare gegevens (vorige jaren, externe bronnen, geschatte tekens en indiciën). De belastingplichtige moet zelf bewijzen dat de schatting onjuist is (bewijslast omgekeerd). Bovendien: belastingverhoging van 10-200% afhankelijk van de aard van de inbreuk ([[bronnen/wetteksten/II-wib92|WIB92 art. 444]]). Vandaar het belang van een tijdige indiening, eventueel met onvolledige gegevens en latere correctie via een **rechtzettingsaangifte** binnen de bezwaartermijn.
> >
> > *Zie: [[personenbelasting-basisbegrippen#-aangifteplicht|Aangifteplicht]]*
>
> 🤖 *AI-aanvulling*
