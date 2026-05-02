---
tags: ["2.2", wip, competentie]
niveau: integratie
status: draft
programmaonderdelen: ["2.2"]
itaa-lex-secties:
  - II (WIB92 — gehele wet)
  - XXI (Wet ITAA art. 3, 6 — beroepsactiviteiten)
procedure-grondslag: "Geen specifieke ITAA-norm voor het opmaken van een fiscaal advies in PB. De werkwijze is gebaseerd op de algemene beroepsdeontologie en de structuur conclusie → grondslag → redenering."
bouwversie: 2
---

# Fiscaal advies personenbelasting formuleren

Een fiscaal advies is **niet** een belastingberekening — het is het **antwoord op een vraag** van de cliënt, met een **conclusie** die hij begrijpt, een **grondslag** die het verantwoordt, en een **redenering** die de logica zichtbaar maakt. Het examen integratie-niveau toetst expliciet deze vaardigheid: niet of de student de wet kent, wel of hij ze in een concrete cliëntsituatie kan toepassen, alternatieven kan afwegen, en zijn aanbeveling kan motiveren.

Onderscheid met aangrenzende competenties:
- **[[aangifte-personenbelasting-invullen|Aangifte invullen]]**: uitvoerend werk na de keuzes; deze competentie maakt de keuzes
- **[[belastingberekening-personenbelasting-uitvoeren|Berekening uitvoeren]]**: cijfermatig werk om alternatieven te vergelijken; ondersteunt deze competentie
- **[[fiscale-optimalisatie-personenbelasting-beoordelen|Fiscale optimalisatie]]**: zoekt actief naar besparingen, eventueel grensgebied wettelijk; deze competentie beantwoordt vragen, niet noodzakelijk optimaliseert

> [!info]- Grondslag van deze werkwijze (🤖 80% · ⚖️ 20%)
> Geen specifieke **ITAA-norm** of **CBN-advies** beschrijft het opmaken van een fiscaal advies in de PB. De wettelijke grondslag is de **algemene aansprakelijkheid** van de beroepsbeoefenaar voor zijn advies ([[bronnen/wetteksten/XXI-wet-itaa|Wet ITAA art. 31, 32]]) en de **deontologische verplichting** tot vakbekwaamheid en zorgvuldigheid ([[deontologische-beginselen|7 deontologische beginselen]]). De **structuur conclusie → grondslag → redenering** is een [CLAUDE.md](file://CLAUDE.md)-stelregel die de leesbaarheid en evaluatie van het advies waarborgt.

## Aanbevolen werkwijze

### 1. 🎯 Vraag van de cliënt afbakenen

> 📥 **Nodig**:
> - Initiële vraag van de cliënt
>
> 📤 **Uitkomst**:
> - **Specifieke vraag** geherformuleerd in fiscale termen
> - Onderscheid: feitelijke vraag (interpretatie wet) of strategische vraag (keuze tussen alternatieven)?
> - Cliënt-doel achter de vraag

**Waarom**: cliënten formuleren hun vraag in **eigen woorden** ("kan ik mijn auto van de belasting trekken?", "wat is voordeliger?") — die formulering verbergt vaak de **werkelijke** fiscale vraag. Een advies op de letterlijke vraag mist het doel — een advies op de werkelijke vraag verschilt soms sterk.

**Twee vraagtypes**:

| Type | Voorbeeld cliëntvraag | Werkelijke fiscale vraag |
|---|---|---|
| **Feitelijk** | "Mag ik mijn vakliteratuur aftrekken?" | Hoe wordt vakliteratuur fiscaal behandeld voor mijn beroepscategorie? |
| **Strategisch** | "Wat is voordeliger: forfait of werkelijke kosten?" | Welke optie levert het laagste aanslagbiljet, gegeven mijn specifieke uitgaven en inkomensschijf? |

**Achterhaal het doel**:
- Cliënt wil belasting **minimaliseren** (optimaliseren)
- Cliënt wil belasting **vermijden** (kan illegaal worden)
- Cliënt wil **zekerheid** (geen risico op controle/herkwalificatie)
- Cliënt wil **inzicht** (begrijpen wat er gebeurt)

**Vraag-herformulering bij de cliënt**: "Begrijp ik goed dat u wilt weten of het voordeliger is om dit jaar uw bezoldiging te verhogen of dividend uit te keren?" Bevestiging vereist vóór het advies wordt gegeven.

> [!warning]- Een verkeerd begrepen cliëntvraag levert een correct maar nutteloos advies op
> ❌ *"Ik geef de cliënt een gedetailleerd advies over de aftrekbaarheid van zijn auto, terwijl hij eigenlijk wilde weten of hij beter een firmawagen krijgt of een mobiliteitsbudget."*
>
> Cliënten formuleren in vlug-en-vuil-bewoording. Een mandataris die de letterlijke vraag beantwoordt zonder eerst de **werkelijke vraag** te exploreren, levert technisch correct maar **strategisch verkeerd** advies. Eerste stap: parafraseer de vraag terug aan de cliënt in fiscale termen en bevestig vóór je begint te onderzoeken. Dit voorkomt latere correctie en verhoogt de waarde van het advies.
>
> 🤖 *AI-aanvulling*

---

### 2. 🔍 Feitelijke situatie volledig in kaart brengen

> 📥 **Nodig**:
> - Geherformuleerde vraag (stap 1)
> - Toegang tot cliëntdossier en MyMinfin

> 📤 **Uitkomst**:
> - Feitenrelaas: alle relevante feiten geïnventariseerd, gevalideerd en gedocumenteerd
> - Lijst ontbrekende informatie waarvoor cliënt-actie nodig is

**Waarom**: een fiscaal advies bouwt op feiten. Een verkeerd of incompleet feitenrelaas leidt tot fout advies. Wat **niet** wordt gevraagd, kan niet worden meegenomen — vandaar systematisch alle **relevante feiten** lijsten.

**Standaard feitenchecklist** (afhankelijk van vraag aan te vullen):

```
[ ] Burgerlijke staat (gehuwd, wettelijk samenwonend, alleenstaand, gescheiden)
[ ] Personen ten laste (kinderen + andere)
[ ] Belastingplichtigen-statuut (rijksinwoner, niet-rijksinwoner)
[ ] Inkomstencategorieën — alle bronnen
[ ] Beroepsstatuut (werknemer, zelfstandige, bedrijfsleider, vrij beroep)
[ ] Onroerend goed bezit (eigen woning, beleggingspand, buitenland)
[ ] Roerend bezit (aandelen, obligaties, spaarboekjes)
[ ] Lopende contracten (hypothecaire lening, levensverzekering, pensioensparen)
[ ] Recente of geplande verrichtingen (verkoop, aankoop, schenking)
[ ] Externe omstandigheden (gezondheid, leeftijd, pensioneringsplan)
```

**Documentatie**: bewaar de feitenlijst in het cliëntdossier als annex bij het advies — bewijst de zorgvuldigheid bij latere betwisting.

> [!info]- Concreet: vraag rond firmawagen
>
> Cliënt: zaakvoerder. Vraag: "Voordeliger firmawagen of mobiliteitsbudget?". Niet beperken tot deze vraag — vraag verder:
> - Aantal km/jaar (privé + beroep)?
> - Type wagen overwogen (cataloguswaarde, CO₂)?
> - Andere mobiliteitsbehoeften (trein, fiets, leasing)?
> - Eigen autogebruik nu (wagen of geen)?
> - Bedoeling op langere termijn (verkoop wagen, ander job)?
>
> Zonder deze feiten is het advies generiek. Mét deze feiten kan een gerichte berekening en aanbeveling worden gemaakt.
>
> 🤖 *AI-aanvulling*

---

### 3. 🔀 Toepasselijke fiscale regels identificeren

> 📥 **Nodig**:
> - Volledige feitenrelaas (stap 2)

> 📤 **Uitkomst**:
> - Lijst toepasselijke materie-fiches en wetsartikelen
> - Identificatie van complexe of betwiste regels (rechtspraak, rulings)

**Waarom**: een advies steunt op een **expliciete grondslag** — vermelding van wettelijke en jurisprudentiële basis is wat het van een mening onderscheidt. Cliënt en mandataris moeten beide kunnen verifiëren waar het advies vandaan komt.

**Werkwijze**:
1. Loop de feitenrelaas door en koppel elke fiscaal relevante feit aan de toepasselijke materie-fiche (bv. eigen woning → [[inkomsten-onroerende-goederen#-eigen-woning|inkomsten OG]], dividend → [[roerende-inkomsten-personenbelasting]], …)
2. Identificeer **bijzondere regels** of **uitzonderingen** die op de cliëntsituatie van toepassing zijn (herkwalificatie huur, normaal beheer, VVPRbis, …)
3. Onderzoek **onbetwiste vs. betwiste** materie — verifieer recente rechtspraak (Hof van Cassatie, Grondwettelijk Hof) of rulings van de Dienst Voorafgaande Beslissingen voor onzekerheid

**Tools**:
- Wetteksten: [[bronnen/wetteksten/II-wib92|WIB92]] (placeholder), [[bronnen/wetteksten/II-KB-wib92|KB/WIB92]]
- Rechtspraak: fisconetplus.belgium.be, juridat.be
- Rulings: ruling.be (publicaties Dienst Voorafgaande Beslissingen)
- Fiscale tijdschriften: Fiscoloog, Fiscale Actualiteit

---

### 4. 🔢 Alternatieven berekenen — minimum 2

> 📥 **Nodig**:
> - Toepasselijke regels (stap 3)
> - Tax-on-web simulator of eigen berekeningstool

> 📤 **Uitkomst**:
> - Per alternatief: berekende belasting + toelichting bij de cijfers
> - Tabel die alternatieven vergelijkt

**Waarom**: een advies zonder alternatieven is een mening. Een advies **met** vergelijkende cijfers is **fundamenteel** beter onderbouwd en laat de cliënt deelnemen aan de beslissing. De vergelijking maakt ook **risico's** zichtbaar.

**Standaardalternatieven om te overwegen**:

| Beslissing | Alternatieven |
|---|---|
| **Werkelijke vs. forfaitaire kosten** | Beide berekenen — kies hoogste |
| **Globaliseren of bevrijdend** | Met en zonder globalisatie van roerende inkomsten |
| **Voorafbetalingen** | Geen VA / spreiden / concentreren in VA1 |
| **Pensioensparen** | Standaard € 1 020 / verhoogd € 1 310 / niet doen |
| **Gezamenlijke aanslag of niet** (bij overlijden) | Vergelijken |
| **Herkwalificatie huur — toewijzing materieel/cliënteel** | Diverse toewijzingsverhoudingen testen |

Gebruik de [[belastingberekening-personenbelasting-uitvoeren|berekening-competentie]] om elk alternatief door te rekenen.

> [!info]- In de praktijk: Tax-on-web simulator is voor het lopende jaar
>
> De Tax-on-web simulator is betrouwbaar voor het lopende aanslagjaar maar biedt **geen multijaarscenario's** en geen vergelijking PB vs. Ven.B. Voor strategische adviezen met meerjarig perspectief (rechtsvormkeuze, stopzettingstiming) gebruiken kantoren eigen spreadsheets. Waarschuw ook cliënten die de simulator zelf gebruiken: een simulatie voor het lopende jaar zegt niets over de komende jaren.
>
> 🤖 *AI-aanvulling*

```
Vergelijkingstabel — alternatieven
                            Optie A          Optie B          Optie C
Belastbaar inkomen          € 65 000         € 65 000         € 65 000
Verminderingen              € 1 800          € 2 200          € 2 800
Eindbelasting               € 18 200         € 17 800         € 17 200
Δ tegenover Optie A         —                −€ 400           −€ 1 000
Risico                      Laag             Laag             Middel (controle-risico)
```

---

### 5. 🔀 Risico-afweging per alternatief

> 📥 **Nodig**:
> - Berekende alternatieven (stap 4)

> 📤 **Uitkomst**:
> - Per alternatief: risico-niveau (laag / middel / hoog) en aard
> - Aanbevolen alternatief, gemotiveerd

**Waarom**: het fiscaal voordeligste alternatief is **niet altijd** het beste advies. Risico's op controle, herkwalificatie of latere belastingverhoging kunnen het netto-voordeel ondermijnen. Cliënt moet expliciet geïnformeerd worden over de risico-component.

**Risico-categorieën**:

| Risico | Voorbeelden | Mitigatie |
|---|---|---|
| **Wettelijk** | Antimisbruikbepaling van toepassing? | Ruling vragen vooraf |
| **Feitelijk** | Bewijsstukken niet beschikbaar | Documentatie verzamelen vóór indiening |
| **Interpretatief** | Recente rechtspraak nog onzeker | Conservatieve uitleg toepassen |
| **Praktisch** | Termijnen of procedures missen | Checklist + reminders |

**Aanbeveling**: het advies eindigt met een **expliciete keuze** — niet "u kan kiezen voor A of B" maar "ik adviseer A, omwille van …". Dit toont **vakbekwaamheid** en **standpunt** — fundamenteel voor het examen.

> [!warning]- Cliëntcommunicatie: vermeld altijd het overige risico bij optimalisatie
> ❌ *"Optie C bespaart u € 1 000 — laten we daarvoor gaan."*
>
> Optie C had een **middelmatig risico** (bv. herkwalificatie huur als bezoldiging). Het advies moet **expliciet** vermelden: "Optie C bespaart € 1 000 maar brengt een controle-risico mee — bij herkwalificatie kan de besparing volledig verdwijnen plus belastingverhoging. Mijn aanbeveling: Optie B (€ 400 besparing zonder risico). Indien u Optie C verkiest, raad ik aan om documentatie van marktconforme huur op te bouwen (vergelijkbare panden, makelaarsrapport)." De cliënt moet **kennis hebben** van het risico — anders is de aansprakelijkheid bij de mandataris.
>
> 🤖 *AI-aanvulling*

---

### 6. 💬 Advies opstellen — conclusie / grondslag / redenering

> 📥 **Nodig**:
> - Aanbevolen alternatief met motivering (stap 5)

> 📤 **Uitkomst**:
> - Schriftelijk advies (e-mail, brief of nota) met de drie componenten

**Waarom**: de schriftelijke vorm waarborgt **traceerbaarheid** voor de mandataris (bewijs van zorgvuldig advies bij latere betwisting) en **verifieerbaarheid** voor de cliënt (kan het advies later raadplegen, doorgeven aan derden). De **structuur conclusie → grondslag → redenering** is examen-norm.

**Sjabloon**:

```
Advies inzake [vraag van de cliënt]

== CONCLUSIE ==
[Korte aanbeveling — 1 à 2 zinnen]

== GRONDSLAG ==
[Wettekst, ruling, rechtspraak, beroepspraktijk die het advies onderbouwen]
- WIB92 art. X
- Cassatie d.d. ../../....
- Ruling Voorafgaande Beslissingen nr. ....

== REDENERING ==
[De logische opbouw van het advies — feiten → regels → gevolgtrekking]
1. Feiten: [korte herhaling relevante feiten]
2. Toepasselijke regels: [wat zegt de wet]
3. Toepassing op uw situatie: [hoe past de regel hier]
4. Vergeleken alternatieven: [korte tabel]
5. Risico-overweging: [welk risico per alternatief]
6. Aanbeveling: [waarom net deze optie]
```

**Lengte**: zo kort als mogelijk, zo lang als nodig. Een eenvoudige vraag verdient een 1-pagina advies; een complex dossier (bv. herstructurering eenmanszaak naar bv) verdient een uitgewerkte nota van 5-10 pagina's.

**Toonzetting**: zakelijk, concreet, verifieerbaar — nooit informeel of oppervlakkig.

---

### 7. ✅ Cliëntvalidatie en archivering

> 📥 **Nodig**:
> - Schriftelijk advies (stap 6)

> 📤 **Uitkomst**:
> - Cliëntakkoord of vraag tot bijsturing
> - Advies gearchiveerd in cliëntdossier (digitaal + datum)

**Waarom**: zonder cliëntvalidatie loopt de mandataris het risico op betwisting later ("ik heb dat advies nooit gekregen"). Archivering met datumstempel (digitaal of papieren ontvangstbewijs) is de basis van **bewijslast** bij latere betwisting van **fiscale verantwoordelijkheid**.

**Cliëntcontact**:
- Verzending advies (e-mail of brief met ontvangstbewijs)
- Bevestiging ontvangst van de cliënt
- Bespreking (telefonisch of persoonlijk) bij complexe adviezen
- **Schriftelijke** keuze van de cliënt voor één van de alternatieven (e-mail volstaat)

**Archivering**:
- Bewaartermijn: **10 jaar** (langer dan fiscale 7 jaar — bewijslast professionele aansprakelijkheid)
- Bij elektronische archivering: timestamping voor authenticiteit
- Inclusief feitenrelaas (annex), berekeningen, alternatieven, cliëntcommunicatie

---

## Voorbeelden

> [!example]- Bedrijfsleider — bezoldiging vs. dividend
>
> **Situatie**: Zaakvoerder X (50 jaar) van een kleine bv (VVPRbis-aandelen sinds 2020). Vennootschap heeft € 50 000 winst beschikbaar voor uitkering. Cliëntvraag: "Wat is voordeliger, mezelf bezoldigen of dividend uitkeren?"
>
> **Conclusie**: Aanbeveling: combinatie van bezoldigingstop tot maximaal forfaitair voordelig + dividend voor de rest. Onder de feiten: hoog persoonlijk inkomen → marginale schijf 50% — dividend (15% RV op VVPRbis) is fiscaal voordeliger dan bezoldiging boven schijf 45%.
>
> **Grondslag**: [[bronnen/wetteksten/II-wib92|WIB92 art. 32 (bezoldigingen bedrijfsleiders), art. 130 (tarieven), art. 269 §2 (VVPRbis)]] + sociale bijdragen zelfstandige.
>
> **Redenering**:
> - Stap 1: Werkelijke vraag = "hoeveel bezoldiging en hoeveel dividend voor optimale netto?"
> - Stap 2: Feiten — bezoldiging huidige € 60 000, marginale 50% in PB; geen andere inkomsten; geen kinderen ten laste
> - Stap 3: Bezoldiging = beroepsinkomen progressief PB + sociale bijdragen ~ 22% + Ven.B aftrek (kost vennootschap). Dividend = Ven.B 25% + RV 15% (VVPRbis boekjaar 3+) op netto.
> - Stap 4: Berekening 3 scenario's:
>   - A: € 50 000 extra bezoldiging → marginale 50% PB + sociale bijdragen → netto cliënt ~ € 22 000
>   - B: € 50 000 dividend → Ven.B 25% (€ 12 500) + RV 15% op € 37 500 (€ 5 625) → netto cliënt ~ € 31 875
>   - C: € 30 000 bezoldiging + € 20 000 dividend → tussenresultaat ~ € 28 000 netto
> - Stap 5: Optie B levert grootste netto, geen specifiek risico (VVPRbis voldoet aan voorwaarden). Optie A houdt sociale dekking op (pensioenrechten, ziekteverzekering hoger) → kwalitatief argument
> - Stap 6: Advies: dividend voor het volledige bedrag (Optie B), met toelichting over verschil sociale dekking
>
> 🤖 *AI-aanvulling*

> [!example]- Werknemer met buitenlands huurpand
>
> **Situatie**: Werknemer A (Belgisch rijksinwoner) heeft sinds 2019 een appartement in Frankrijk (huur € 12 000/jaar, fiscaal in FR betaald: € 1 400). Tot vorig jaar gaf A dit niet aan in BE-aangifte. Vraag: "Moet ik dat aangeven?"
>
> **Conclusie**: Ja — verplicht aangifte, met vrijstelling met progressievoorbehoud onder DBV BE-FR. Aanbeveling: rechtzettingsaangifte voor de jaren 2019-2024 om belastingverhoging te beperken.
>
> **Grondslag**: [[bronnen/wetteksten/II-wib92|WIB92 art. 5 (wereldwijd inkomen rijksinwoner), art. 13/1 (buitenlands KI), art. 444 (belastingverhoging niet-aangifte)]]; DBV BE-FR art. 6 (onroerende inkomsten — heffingsbevoegdheid bronstaat) en art. 22 (vrijstelling met progressievoorbehoud).
>
> **Redenering**:
> - Stap 1: Werkelijke vraag = niet alleen "moet ik aangeven?" maar ook "wat zijn de gevolgen voor de vorige jaren?"
> - Stap 2: Feiten — pand in FR sinds 2019, € 12 000 huur/jaar, FR-belasting € 1 400/jaar betaald, geen aangifte in BE tot nu toe
> - Stap 3: Wereldwijd belastingbeginsel BE → moet aangegeven worden. DBV BE-FR → vrijstelling met progressievoorbehoud → geen extra BE-belasting op de huur, **maar** verhoging van marginaal tarief op overige BE-inkomsten
> - Stap 4: Vergelijking 2 alternatieven:
>   - A: Niets doen — risico op controle (uitwisseling fiscale info BE-FR via DAC) → belastingverhoging tot 200% bij ontdekking
>   - B: Rechtzettingsaangifte voor vorige jaren — beperkt de boete (kan tot 10% blijven bij vrijwillige rechtzetting); progressievoorbehoud verhoogt BE-belasting met ~ € 1 500-2 000/jaar (afhankelijk van marginale schijf) × 6 jaar = ~ € 12 000 bijbetaling, plus moratoire intresten
> - Stap 5: Optie B is de enige verantwoorde keuze — risico op detectie via DAC is reëel en zwaar
> - Stap 6: Advies: indienen rechtzettingsaangiftes voor 2019-2024 én voor 2025 onmiddellijk aangeven; documenteer feiten en bewaar bewijsstukken; budgetteer bijbetaling € 12-15 000
>
> 🤖 *AI-aanvulling*

## Motiveren op het examen

**Een volledig advies bevat:**
1. Geherformuleerde cliëntvraag in fiscale termen
2. Feitenrelaas (relevant voor de vraag)
3. Toepasselijke wetsartikelen / rulings / rechtspraak
4. Minimum 2 alternatieven berekend
5. Risico-afweging per alternatief
6. Conclusie / grondslag / redenering schriftelijk
7. Aanbeveling met motivering

### Voorbeeldvragen

> [!question]- Cliënt vraagt extra dividend in plaats van bezoldiging
>
> Een bedrijfsleider met marginale aanslagvoet 50% vraagt: "Mijn vennootschap heeft € 30 000 cash beschikbaar. Beter mezelf bezoldigen of dividend uitkeren?" Welke 4 elementen moet uw advies bevatten?
>
> > [!success]- Antwoord
> >
> > **(1) Vergelijking netto-bedrag bij beide opties** — bezoldiging (PB progressief + sociale bijdragen) vs. dividend (Ven.B + RV). **(2) Toepassing VVPRbis** indien beschikbaar (15% RV i.p.v. 30%). **(3) Sociale-dekking-impact** — bezoldiging verhoogt pensioenrechten, dividend niet. **(4) Cashflow-overweging vennootschap** — Ven.B is 25%, kostbaar voor de vennootschap; bezoldiging is aftrekbare kost.**
> >
> > Het advies moet expliciet alle 4 elementen bevatten — een louter cijfermatige vergelijking zonder de sociale-dekking en cashflow-overweging mist de strategische dimensie. Aanbevolen volgorde: cijfermatige vergelijking → kwalitatieve overwegingen → motivierde keuze.
> >
> > *Zie: [[fiscaal-advies-personenbelasting-formuleren#-4--alternatieven-berekenen-minimum-2|Alternatieven berekenen]]*
>
> 🤖 *AI-aanvulling*

> [!question]- Onverklaarbaar voordeel
>
> Een cliënt komt bij u: "Mijn vorige adviseur zei dat ik geen belasting moet betalen op mijn aandelenwinst van € 80 000 omdat het normaal beheer is." U twijfelt. Wat is uw advieshouding?
>
> > [!success]- Antwoord
> >
> > **Eerst feiten verzamelen, dan onafhankelijk oordelen — niet zomaar overnemen.**
> >
> > De [[diverse-inkomsten-personenbelasting#-normaal-beheer-van-het-privévermogen|normaal-beheer-kwalificatie]] is feitenkwestie — moet getoetst worden op concrete elementen: tijdsverloop, frequentie, geleende fondsen, professionele aanpak. Indien er **speculatieve elementen** aanwezig zijn (bv. day-trading, geleende fondsen), kwalificeert het als divers inkomen aan 33%. Een advies dat het standpunt van de vorige adviseur zonder eigen onderzoek overneemt, schendt de **deontologische zorgvuldigheidsplicht**. Stappen: (1) verzamel feiten over aankoop, verkoop, financiering; (2) toets aan de kwalificatiecriteria; (3) overweeg ruling bij twijfel; (4) eigen advies geven, eventueel afwijkend van vorige adviseur.
> >
> > *Zie: [[fiscaal-advies-personenbelasting-formuleren#-2--feitelijke-situatie-volledig-in-kaart-brengen|Feitelijke situatie in kaart brengen]] en [[diverse-inkomsten-personenbelasting#-normaal-beheer-van-het-privévermogen|Normaal beheer]]*
>
> 🤖 *AI-aanvulling*

> [!question]- Niet-aangegeven buitenlandse inkomsten
>
> Een cliënt onthult dat hij sinds 2018 een Spaans appartement verhuurt zonder dit ooit in BE aan te geven. Wat is uw advies?
>
> > [!success]- Antwoord
> >
> > **Rechtzettingsaangifte indienen voor de openstaande jaren — niet zwijgen.**
> >
> > Niet-aangifte van buitenlandse inkomsten is een **fiscale inbreuk** ([[bronnen/wetteksten/II-wib92|WIB92 art. 305, 444]]) — bestraft met belastingverhoging tot **200%**. Sinds DAC (uitwisseling fiscale informatie EU) is detectie via FR/SP-administratie waarschijnlijk. **Vrijwillige rechtzetting** beperkt de belastingverhoging vaak tot 10-50% (versus 100-200% bij ontdekking). Stappen: (1) feiten verzamelen (aankoop, huurinkomsten/jaar, FR-belastingbetaald); (2) berekening Belgische belasting per jaar met vrijstelling progressievoorbehoud; (3) rechtzettingsaangiftes indienen; (4) eventueel ruling vragen voor de boete-vermindering bij grote bedragen. **Niet aangeven** is geen optie — de mandataris heeft de **deontologische plicht** om de cliënt op de naleving te wijzen.
> >
> > *Zie: [[belastingplichtigen-personenbelasting#-dubbelbelastingverdragen|DBV]] en [[fiscaal-advies-personenbelasting-formuleren#-5--risico-afweging-per-alternatief|Risico-afweging]]*
>
> 🤖 *AI-aanvulling*
