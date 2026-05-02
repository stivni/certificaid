---
tags: ["1.3", wip, materie]
niveau: integratie
status: draft
bronnen:
  - WVV art. 2:52 (zorgplicht bestuursorgaan)
  - WVV art. 5:153 (alarmbelprocedure BV)
  - WVV art. 7:228–7:229 (alarmbelprocedure NV)
  - WVV art. 5:142, 7:212 (definitie nettoactief)
  - CBN-advies 2021/14 (jaarrekeningrechtelijke analyse alarmbelprocedure)
  - CBN-advies 2018/18 (going concern waardering bij discontinuïteit)
  - WER art. XX.23 (meldingsplicht beroepsbeoefenaar)
  - ISA 570 herzien (referentiekader indicatoren — IBR-auditstandaard, niet bindend voor GA)
---

# Continuiteitsrisico

## 📌 Continuïteitsveronderstelling
*Going concern*

De continuïteitsveronderstelling houdt in dat een entiteit haar activiteiten in de voorzienbare toekomst voortzet — activa en passiva worden gewaardeerd vanuit die veronderstelling. Bij twijfel moeten de waarderingsregels worden aangepast en moet de toelichting dit vermelden. ([[wetteksten/XV-wvv#art-252|WVV art. 2:52]], [[normen/ISA-570-herzien#par-2|ISA 570 herzien, par. 2]])

De beoordelingsperiode bedraagt minstens **12 maanden** na de balansdatum. ([[normen/ISA-570-herzien#par-13|ISA 570 herzien, par. 13]])

## 📌 Nettoactief

Het [[nettoactief|nettoactief]] is de centrale maatstaf voor de alarmbelprocedure. Definitie en berekening: [[nettoactief]].

## 📌 Alarmbelprocedure

De alarmbelprocedure verplicht het bestuursorgaan de algemene vergadering bijeen te roepen wanneer continuïteit in het gedrang komt. De triggers en drempels verschillen per vennootschapsvorm:

**BV** ([[wetteksten/XV-wvv#art-5153|WVV art. 5:153]]):
- Nettoactief is negatief of dreigt negatief te worden, **of**
- Onzekerheid of schulden betaald kunnen worden gedurende de komende 12 maanden

**NV** ([[wetteksten/XV-wvv#art-7228|WVV art. 7:228–7:229]]):
- Nettoactief gedaald onder **50%** van het geplaatst kapitaal, **of**
- Nettoactief gedaald onder **25%** van het geplaatst kapitaal (AV kan dan ontbinden met ¼ van de stemmen), **of**
- Nettoactief gedaald onder **€61.500** (ontbindingsvordering door elke belanghebbende)

**Procedure** (alle vennootschapsvormen): bijeenroeping binnen **2 maanden** na vaststelling. Het bestuursorgaan stelt een bijzonder verslag op met herstelmaatregelen, tenzij het ontbinding voorstelt. Na eerste naleving: geen nieuwe verplichting gedurende de volgende 12 maanden voor dezelfde reden. ([[wetteksten/XV-wvv#art-5153|WVV art. 5:153 §4]])

## 🔢 Altman Z-score (illustratief model)

De Altman Z-score is een kwantitatief model om falingskans in te schatten op basis van vijf ratio's. Er bestaat geen Belgische ITAA-specifieke versie — gebruik als aanvullend instrument, niet als primaire beoordeling.

**Formule** (originele versie, beursgenoteerde maatschappijen):

Z = 1,2 × (NBK/TA) + 1,4 × (IW/TA) + 3,3 × (EBIT/TA) + 0,6 × (MVE/VV) + 1,0 × (O/TA)

| Variabele | Naam | Berekening | Belgische code |
|---|---|---|---|
| NBK/TA | Werkkapitaal / Totaal activa | (29/58 − 42/48) / 20/58 | Rubriek 29/58, 42/48 |
| IW/TA | Ingehouden winst / Totaal activa | (14 − 141) / 20/58 | Rubriek 14 |
| EBIT/TA | Bedrijfsresultaat / Totaal activa | 9901 / 20/58 | Rubriek 9901 |
| MVE/VV | Marktwaarde EV / Boekwaarde schulden | 10 / (16+17+42/48) | Rubriek 10 |
| O/TA | Omzet / Totaal activa | 70 / 20/58 | Rubriek 70 |

**Zones (originele versie)**:
- Z > 2,99 → veilige zone
- 1,81 ≤ Z ≤ 2,99 → grijze zone
- Z < 1,81 → risicozone

**Beperkingen voor Belgische context**: de originele formule werd gekalibreerd op beursgenoteerde Amerikaanse productiebedrijven. Voor niet-beursgenoteerde KMO's bestaat een aangepaste Z'-versie (X₄ op basis van boekwaarde). Geen van beide versies is gevalideerd op een representatieve Belgische steekproef.

🤖 *AI-aanvulling — Belgische rekeningcodekoppelingen zijn indicatief; verifieer via het MAR*

> [!info]- In de praktijk: Altman Z-score berekenen
>
> 🤖 *AI-aanvulling*
>
> Een productie-nv heeft (in €): totaal activa 5.000.000; werkkapitaal (vlottende activa − schulden KT) 400.000; ingehouden winst (reserves) 600.000; EBIT 350.000; marktwaarde eigen vermogen 1.200.000; totale schulden 3.200.000; netto-omzet 7.000.000.
>
> | Variabele | Berekening | Waarde |
> |---|---|---|
> | NBK/TA = Werkkapitaal / Totaal activa | 400.000 / 5.000.000 | 0,080 |
> | IW/TA = Ingehouden winst / Totaal activa | 600.000 / 5.000.000 | 0,120 |
> | EBIT/TA = Bedrijfsresultaat / Totaal activa | 350.000 / 5.000.000 | 0,070 |
> | MVE/VV = Marktwaarde EV / Totale schulden | 1.200.000 / 3.200.000 | 0,375 |
> | O/TA = Omzet / Totaal activa | 7.000.000 / 5.000.000 | 1,400 |
>
> Z = 1,2 × 0,080 + 1,4 × 0,120 + 3,3 × 0,070 + 0,6 × 0,375 + 1,0 × 1,400
>   = 0,096 + 0,168 + 0,231 + 0,225 + 1,400 = **2,12**
>
> **Interpretatie**: Z = 2,12 → grijze zone (1,81–2,99). De onderneming is niet in de veilige zone maar ook niet acuut in gevaar. Dit is een signaal om de financiële positie verder te onderzoeken — het model geeft een indicatie, geen diagnose. Let op de beperkingen: het model is niet gevalideerd voor de Belgische context en is slechts één instrument naast ratio-analyse en kasstroomanalyse.

## 🔎 Signalen van continuïteitsrisico

Signalen zijn nooit op zichzelf conclusief — het is de combinatie ("gewichtige **en** overeenstemmende feiten") die de alarmbel triggert. ([[wetteksten/XV-wvv#art-252|WVV art. 2:52]])

De onderstaande indeling is gangbaar in financiële analyse. Ze is ook terug te vinden in de auditstandaard [[normen/ISA-570-herzien#par-a3|ISA 570 herzien, par. A3]] — die is niet bindend voor de gecertificeerd accountant (dat is een IBR-norm voor bedrijfsrevisoren), maar de signalen zelf zijn breed erkend analytisch referentiemateriaal.

**Financiële signalen**:
- Nettovlottende passiva of nettopasiva (meer schulden dan activa)
- Negatieve operationele kasstromen terwijl winst gerapporteerd wordt
- Ongunstige financiële ratio's (current ratio < 1, hoge schuldgraad, dalende interestdekking)
- Substantiële operationele verliezen of significante waardedaling activa
- Achterstanden of stopzetting van dividenden
- Onmogelijkheid om crediteuren op vervaldag te betalen
- Niet naleven van leningvoorwaarden (covenants)
- Leningen met vervaldatum zonder uitzicht op herfinanciering

**Operationele signalen**:
- Verlies van een cruciale klant, leverancier, markt of licentie
- Arbeidsconflicten, personeelstekort of vertrek van sleutelfiguren zonder vervanging
- Voorraadtekorten of productiestoornissen

**Juridische en externe signalen**:
- Lopende procedures met potentieel onoverzienbare claims
- Niet naleven van kapitaalvereisten of wettelijke solvabiliteitsvereisten
- Nadelige wetswijzigingen of intrekking van vergunningen

## 🚩 Misleidende continuïteitssignalen

Sommige situaties lijken op going concern-problemen maar zijn dat niet per definitie.

**Groeipijn**: een sterk groeiend bedrijf vertoont tijdelijk slechte liquiditeitsratio's doordat werkkapitaal de omzetgroei niet kan bijhouden. Alarmerend als structureel, maar normaal als tijdelijk en gefinancierd.

> Hoe onderscheiden: bekijk de trend over meerdere jaren. Bij gezonde groei verbetert de liquiditeit naarmate de groei afvlakt en het werkkapitaalbeheer volwassen wordt.

**Seizoenspatroon**: negatief werkkapitaal aan het einde van een laagseizoen (bv. retailer na de zomer) is normaal. Eén momentopname is onvoldoende.

> Hoe onderscheiden: vergelijk op hetzelfde punt in vorige seizoenen. Deterioreert het jaar-op-jaar? Dan is het structureel.

**Grote investering**: negatieve vrije kasstroom door een éénmalige capex-investering (gebouw, machine) ziet er alarmerend uit maar is geen going concern-probleem als de financiering gedekt is.

> Hoe onderscheiden: splits de kasstroom op in operationeel en investeringsactiviteiten. Een positieve operationele kasstroom naast een negatieve investeringskasstroom is geen continuïteitsrisico.

**NV met dalend kapitaal**: een NV waarvan het nettoactief de 50%-drempel nadert, is niet automatisch in gevaar. De drempel triggert een procedure — niet het faillissement.

> Hoe onderscheiden: het feit dat de alarmbelprocedure loopt, zegt niets over de werkelijke overlevingskansen. Kijk naar de kasstromen en het herstelplan.

🤖 *AI-aanvulling*

## 🔒 Verplichtingen van het bestuursorgaan

Wanneer het bestuursorgaan "gewichtige en overeenstemmende feiten" vaststelt die de continuïteit in het gedrang brengen:

1. Beraadslagen over herstelmaatregelen ([[wetteksten/XV-wvv#art-252|WVV art. 2:52]])
2. [[continuiteitsrisico#-alarmbelprocedure|Alarmbelprocedure uitvoeren]] als de wettelijke drempels bereikt zijn
3. Bij verdere verslechtering: overwegen om de voorzitter van de ondernemingsrechtbank in te lichten

Bestuursleden die de alarmbelprocedure niet naleven zijn aansprakelijk voor de schade die derden lijden, tenzij ze het tegendeel bewijzen. ([[wetteksten/XV-wvv#art-5153|WVV art. 5:153 §3]])

## 🔒 Meldingsplicht bij continuïteitsrisico (WER art. XX.23)

*Niet te verwarren met de [[antiwitwaswetgeving#-meldingsplicht-en-het-verbod-op-mededeling-tipping-off|meldingsplicht (AWW)]] — dit is een aparte wettelijke verplichting op grond van het WER.*

De gecertificeerd accountant (GA) en gecertificeerd belastingadviseur (GBA) hebben een meldingsplicht wanneer zij bij de uitoefening van hun opdracht "gewichtige en overeenstemmende feiten" vaststellen die de continuïteit in het gedrang kunnen brengen. ([[wetteksten/XIII-wer/boek-xx#art-xx23|WER art. XX.23 §3]])

**Procedure** (gecertificeerd accountant):
1. Aangetekende brief aan elk lid van het bestuursorgaan (ook per gewone brief aan elk lid afzonderlijk), met vermelding van de vastgestelde feiten en de gevraagde maatregelen
2. Responstermijn: **1 maand**
3. Geen of onvoldoende reactie, **of** faillissement lijkt op korte termijn onvermijdelijk → melding aan de **voorzitter van de ondernemingsrechtbank**

Geen actieve onderzoeksplicht — de plicht ontstaat bij vaststelling in de normale uitoefening van de opdracht.

## Relevant voor

**[[1.3-analyse-en-kritische-beoordeling-jaarrekening|1.3 Analyse en kritische beoordeling van de jaarrekening]]**

Taken:
- *Analyse en beoordeling van de financiële situatie*
  - Kritisch bekijken van de jaarrekening
  - Voorstellen kunnen doen om de situatie te verbeteren of te controleren

Kenniselementen:
- II.C.5 — Falingspredictie / going concern
