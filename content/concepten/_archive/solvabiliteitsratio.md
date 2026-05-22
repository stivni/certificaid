---
title: Solvabiliteitsratio
tags:
- concept
- po-1-1
- po-1-3
- po-1-7
- po-1-9
linked_anchors:
- 1.3.II.C
- 1.3.I.A
- 1.3.taak.1
- 1.9.V.C
- 1.9.taak.1
- 1.1.III.C
- 1.7.III.A
programmaonderdelen:
- '1.1'
- '1.3'
- '1.7'
- '1.9'
confidence: inferred
node_type: ''
status: draft
schema_version: '2.0'
gegenereerd_uit: data/concepten/records/solvabiliteitsratio.json
gegenereerd_op: '2026-05-21'
---
# Solvabiliteitsratio 🔗

> [!summary] Korte inhoud
> De solvabiliteitsratio meet de financiële onafhankelijkheid van een onderneming: welk deel van haar totale vermogen door eigen middelen wordt gefinancierd in plaats van door schulden.

De solvabiliteitsratio meet de financiële onafhankelijkheid van een onderneming: welk deel van haar totale vermogen door eigen middelen wordt gefinancierd in plaats van door schulden. Een hogere ratio betekent meer eigen draagkracht en minder afhankelijkheid van schuldeisers.




## Voorkennis & leespad

- **Lees eerst** (voorvereisten):
  [[eigen-vermogen]]
  [[vreemd-vermogen]]
  [[jaarrekening]]

- **Past binnen kader**: [[jaarrekeninganalyse]]

- **Naast deze fiche relevant**:
  [[schuldgraad]]
  [[interest-coverage-ratio]]
  [[current-ratio]]
  [[quick-ratio]]
  [[rentabiliteit-eigen-vermogen]]

- **Bij vervolgvragen**:
  [[alarmbel]]
  [[kapitaalverhoging]]
  [[achtergestelde-lening]]



## Hoe het werkt

### Klassieke formule — EV / Totaal passief 🔗

De klassieke (Belgische, NBB-conforme) formule deelt het eigen vermogen door het balanstotaal en geeft een percentage tussen 0 % en 100 %. Dit is de variant die in financiële-analyse-rapporten standaard wordt gebruikt en die als alternatief in praktijkliteratuur 'equity ratio' heet.

Solvabiliteitsratio = Eigen vermogen / Totaal passief × 100 %

| Component | MAR-rubriek | Inhoud |
| --- | --- | --- |
| Eigen vermogen (teller) | 10–15 | Kapitaal + uitgiftepremies + herwaarderingsmeerwaarden + reserves + overgedragen resultaat + kapitaalsubsidies |
| Totaal passief (noemer) | 10–49 | Eigen vermogen + voorzieningen + schulden > 1 jaar + schulden ≤ 1 jaar + overlopende rekeningen passief |
| Resultaat | — | Percentage tussen 0 % (puur schuldgefinancierd) en 100 % (puur eigen) |

### Twee varianten — let op welke je leest 🔗

In de praktijk circuleren twee definities die beide 'solvabiliteit' heten. De klassieke (NBB) gebruikt het balanstotaal als noemer en geeft een percentage. De debt-to-equity-omgekeerde gebruikt het vreemd vermogen als noemer en geeft een ratio > 1 als sterk-signaal. Lees altijd de definitie die de bron gebruikt — een ratio van 1,5 is iets heel anders dan een ratio van 60 %.

| Variant | Formule | Schaal | Wanneer tegenkomen |
| --- | --- | --- | --- |
| Klassiek / NBB / Equity ratio | EV / Totaal passief | 0 – 100 % | NBB Centrale voor Balansen, ITAA-analyse, jaarverslagen |
| Omgekeerde schuldgraad | VV / Totaal passief | 0 – 100 % | Sectorrapporten — som van solvabiliteit + schuldgraad = 100 % |
| Debt-to-equity (inversie) | EV / VV | ratio (> 1 = sterk) | Angelsaksische literatuur, bankcovenants |
| Solvency II / Basel | Risico-gewogen kapitaalratio | — | Banken, verzekeraars — NIET gebruiken voor gewone vennootschappen |

### Voorbeeld — Rotex Roeselare NV 🔗

Geïllustreerde balans met berekening en interpretatie van het resultaat.



| Stap | Berekening | Resultaat |
| --- | --- | --- |
| 1. Teller | Eigen vermogen | € 12.000.000 |
| 2. Noemer | Balanstotaal | € 30.000.000 |
| 3. Ratio | 12.000.000 / 30.000.000 | 0,40 = 40 % |



### Interpretatie-drempels (vuistregels — geen wet) 🧭

De volgende drempels zijn beroepswijsheid uit de financiële-analyse-praktijk, GEEN wettelijke normen. Sectorgebonden: een industrieel bedrijf draagt typisch meer eigen vermogen dan een dienstverlener of een vastgoedvennootschap. Toepasselijke sectormediaan: zie NBB Centrale voor Balansen, sectorale statistieken.

| Ratio | Niveau | Algemene interpretatie |
| --- | --- | --- |
| > 50 % | Zeer gezond | Sterke eigen buffer; soms zelfs overgekapitaliseerd (kapitaal rendeert vaak slecht) |
| 33 – 50 % | Gezond | Comfortabele financieringsstructuur — typisch beeld solide KMO |
| 25 – 33 % | Aanvaardbaar | Mediaan voor veel Belgische KMO's volgens NBB-statistieken |
| 15 – 25 % | Zwak | Verhoogde gevoeligheid voor tegenslag; bancaire covenants vaak in zicht |
| < 15 % | Kritisch | Faillissementsrisico bij verlies-jaar; herstructurering urgent |
| Negatief | Insolvabel | Alarmbel-procedure WVV verplicht — netto-actief negatief |



### Wettelijke drempels — alarmbel-procedure WVV ⚖️

Het WVV koppelt geen drempel aan de solvabiliteitsratio zelf, maar wel aan het netto-actief — een directe verwante van de teller. Wanneer het netto-actief onder een wettelijke drempel zakt, moet het bestuursorgaan de algemene vergadering bijeenroepen binnen twee maanden (alarmbel-procedure). Het effect op de solvabiliteitsratio is mechanisch: bij negatief netto-actief wordt de ratio negatief.

| Rechtsvorm | Solvabiliteits-drempel | Wettelijk gevolg | Bron |
| --- | --- | --- | --- |
| BV / CV | Netto-actief negatief of dreigt negatief | AV bijeenroepen binnen 2 maanden; bijzonder verslag met herstelmaatregelen | WVV art. 5:153 §1 |
| BV / CV | Idem — bijkomend ook liquiditeitstest (12 maanden) | Idem — onafhankelijke tweede trigger | WVV art. 5:153 §2 |
| NV | Netto-actief < ½ geplaatst kapitaal (verlies-oorzaak vereist) | AV bijeenroepen binnen 2 maanden | WVV art. 7:228 §1 |
| NV | Netto-actief < ¼ geplaatst kapitaal | Minderheid van 25 % kan ontbinding stemmen | WVV art. 7:228 §1 |
| NV | Netto-actief < € 61.500 (minimumkapitaal) | Iedere belanghebbende kan gerechtelijke ontbinding vorderen | WVV art. 7:229 |



### Sectorgebondenheid — vuistregels per branche 🧭

Solvabiliteitsnormen verschillen sterk per sector omwille van structurele financieringspatronen. Een universele drempel toepassen op alle sectoren leidt tot foute conclusies.

| Sector | Typische solvabiliteit | Waarom |
| --- | --- | --- |
| Vastgoed / holding | 10 – 25 % | Vastgoed-onderpand maakt hoge schuld-financiering werkbaar; hefboom op rendement |
| Kapitaalintensieve industrie | 25 – 40 % | Investeringen in vaste activa worden deels via lange-termijn-schuld gefinancierd |
| Dienstverlening / consultancy | 40 – 60 % | Weinig vaste activa; eigen vermogen is hoofdfinanciering; hoge tolerantie voor cash-buffers |
| Retail / distributie | 20 – 35 % | Voorraad-financiering via leverancierskrediet drukt solvabiliteit; werkkapitaal-cyclus dominant |
| Bank / verzekeraar | Niet-vergelijkbaar | Eigen prudentiële kapitaal-ratio's (Basel III / Solvency II) — klassieke formule niet relevant |

### Interpretatie-valkuilen — balans-EV versus economisch EV 🔗

De boekhoudkundige solvabiliteitsratio kan systematisch afwijken van de economische realiteit door drie correctiepunten: herwaarderingsmeerwaarden, achtergestelde leningen en uitgestelde belastingen. Een analyst rapporteert vaak twee getallen: de bruto-ratio uit de balans en de gecorrigeerde 'economische' ratio.

| Post | Boekhoudkundige behandeling | Economische correctie | Effect op ratio |
| --- | --- | --- | --- |
| Herwaarderingsmeerwaarden (rubriek 12) | 100 % naar EV | Eventueel uitsluiten — geen cash, slechts boekhoudkundig | Bruto-ratio overschat solvabiliteit |
| Achtergestelde lening aandeelhouder | Vreemd vermogen (rubriek 17 of 42) | Behandel economisch als EV — niet opeisbaar bij faillissement vóór andere schulden | Bruto-ratio onderschat solvabiliteit |
| Uitgestelde belastingen (rubriek 168) | Voorziening — vreemd vermogen | Latente schuld — soms nooit feitelijk verschuldigd | Bruto-ratio onderschat solvabiliteit licht |
| Oprichtings- en O&O-kosten geactiveerd | Vaste activa — verhoogt balanstotaal | Aftrekken voor netto-actief-toets bij alarmbel | Wettelijke correctie verplicht — bruto-ratio overschat draagkracht |
| Overlopende rekeningen verkeerd toegewezen | Rubriek 49 (passief) vs 29 (actief) | Fout schuift het balanstotaal | Berekenings-fout — niet interpretatief |



### Wanneer NIET deze formule 🔗

Drie categorieën entiteiten waar de klassieke solvabiliteitsformule geen of beperkt zinvol resultaat oplevert.

1. Banken en verzekeraars — gebruik prudentiële Basel III- / Solvency II-ratio's (risicogewogen). De klassieke EV/balanstotaal-ratio negeert het risicoprofiel van de activa.
2. Verenigingen zonder winstoogmerk (vzw) — geen aandeelhouders en geen 'kapitaal'-concept; eigen vermogen-structuur is verschillend. Gebruik wel netto-actief-evolutie als signaal.
3. Eenmanszaken — geen scheiding tussen ondernemingsvermogen en privévermogen; ratio is niet zinvol. Gebruik kasstroomratio's en persoonlijke balans gecombineerd.


## Rol van de accountant

### Onderneming-met-ratio

#### 🎯 adviseur

##### Advies aan het bestuur — actie per drempel-niveau 🧭

De accountant koppelt aan het ratio-niveau een concrete handeling. De lange-termijn-richting van de balans is een bestuurs-beslissing die berust op deze analyse.

| Ratio-niveau | Aanbevolen actie | Confidence |
| --- | --- | --- |
| > 50 % | Overweeg uitkering of rendabel beleggen — overgekapitaliseerd EV rendeert slecht (link met nettoactieftest) | vuistregel |
| 33 – 50 % | Geen actie; bewaak jaarlijks | vuistregel |
| 25 – 33 % | Vermijd verdere schuldopbouw; bewaak schuldgraad | vuistregel |
| 15 – 25 % | Versterk EV — winstinhouding, kapitaalverhoging, achtergestelde lening aandeelhouder | vuistregel |
| < 15 % | Urgente actie — herstructurering of kapitaalinjectie; afstoten niet-strategische activa | vuistregel |
| Negatief | Bestuur wijzen op alarmbel-procedure (WVV art. 5:153 BV / 7:228 NV); AV binnen 2 maanden; bijzonder verslag opstellen | grounded |

##### Begeleiding bij financierings-keuze (EV vs VV) 🧭

Bij een investerings- of overname-vraagstuk weegt de accountant af welk financierings-instrument de solvabiliteit het meest belast versus welk het hefboomeffect ten voordele inzet. Trade-off tussen WACC, fiscale aftrek van rente, en de impact op covenanten.

| Instrument | Effect op solvabiliteit | Fiscaal | Wanneer kiezen |
| --- | --- | --- | --- |
| Bankkrediet LT | Daalt (VV stijgt) | Rente aftrekbaar (limiet thin-cap art. 198 §1 11°/1 WIB92) | Voldoende cashflow voor rentelast; covenants haalbaar |
| Obligatielening | Daalt (VV stijgt) | Idem | Voor grotere bedragen, lange looptijd |
| Kapitaalverhoging | Stijgt (EV stijgt) | Geen rente-aftrek; mogelijk impact NID (notionele intrestaftrek voor MKB) | Bij lage solvabiliteit + lange investerings-horizon |
| Achtergestelde lening aandeelhouder | Boekhoudkundig: daalt; economisch: neutraal | Rente aftrekbaar binnen marktconforme grens (art. 18 WIB92, transfer pricing) | Tussenvorm bij familie-vennootschappen |

#### fiscaal

##### Thin-capitalisation — fiscale schuld/EV-grens 5:1 ⚖️

Naast de boekhoudkundige solvabiliteitsanalyse bestaat een fiscale schuld/EV-grens: wanneer het totale bedrag van leningen binnen een groep van vennootschappen hoger is dan vijf maal de som van belaste reserves bij het begin van het belastbaar tijdperk en het gestort kapitaal bij het einde, is de interest op het overschrijdende deel fiscaal NIET aftrekbaar. Dit raakt vooral groep-interne financieringsstructuren.

_Bron: WIB92 art. 198 §1, 11°/1_

Grens groepslening = 5 × (belaste reserves bij begin BT + gestort kapitaal bij einde BT)



### Vennootschap-met-commissaris

#### controleur

##### Solvabiliteit als going-concern-indicator ⚖️

De commissaris weegt de solvabiliteitsratio (samen met liquiditeit en interest-coverage) in zijn beoordeling van de continuïteits-veronderstelling onder WVV art. 3:75 §3 en ISA 570 (going concern). Een kritisch niveau (< 15 %) of negatief netto-actief triggert verzwaarde audit-procedures: cashflow-projecties van 12 maanden, herfinancierings-plannen, brieven van aandeelhouders met financierings-toezeggingen, en analyse van de naleving van bank-covenants.

_Bron: WVV art. 3:75 §3; ISA 570 (Going Concern)_

1. Beoordeel ratio in evolutie (3-5 jaar) en versus sector
2. Bij ratio < 15 % of negatief: voer verzwaarde procedures uit (cashflow-projectie 12M, herfinancierings-plan)
3. Bij wettelijke alarmbel-overschrijding: controleer of het bestuur de procedure heeft gevolgd (AV binnen 2 maanden, bijzonder verslag, agenda)
4. Bij niet-naleving of materiële onzekerheid: vermelding in commissarisverslag (going-concern-paragraaf of toelichtende paragraaf)
5. Bij in gebreke blijven bestuur: aanmaning bestuur; bij uitblijven reactie zelf AV bijeenroepen (WVV art. 3:68)

##### Controle-aandachtspunten bij ratio-berekening 🔗

De commissaris controleert of de ratio in het beheersverslag of jaarverslag consistent is berekend met vorige boekjaren en met de eigen wettelijke definitie, en of materiële posten correct gerubriceerd zijn.

1. Berekeningsmethode consistent t.o.v. vorig boekjaar (geen 'best year' cherry-picking)
2. Correcte rubricering: achtergestelde leningen niet kunstmatig naar EV verplaatst
3. Herwaarderingsmeerwaarden conform rentabiliteitsvoorwaarde CBN-2011/14
4. Toelichting jaarrekening volledig bij overschrijden alarmbel-drempel
5. Geplaatst kapitaal correct opgenomen (passiefpost I.A.1) bij NV-drempel-toets

### Externe-kredietverstrekker-of-koper

#### 🎯 adviseur

##### Due diligence — solvabiliteit bij overname of kredietbeoordeling 🧭

Bij een overname-onderzoek of bij kredietbeoordeling becijfert de accountant de solvabiliteit met sector-gecorrigeerde drempels en past hij correcties toe voor goodwill, verborgen reserves en achtergestelde leningen. Hij vergelijkt de gevonden ratio met de bank-covenant-grens (vaak een minimum-solvabiliteit van 20 % – 25 % als trigger voor opeisbaarheid) en geeft bij overschrijding een waarschuwing aan de koper of de bank.




## Veelvoorkomende verwarringen

### Solvabiliteit verwarren met liquiditeit 🔗

Solvabiliteit = structurele balans-positie (lange termijn); liquiditeit = betalingscapaciteit binnen het jaar (korte termijn). Een onderneming met solvabiliteit 50 % maar quick ratio 0,3 staat op springen — twee dimensies, beide nodig. Voor korte-termijn-betaalcapaciteit gebruik je [[current-ratio]], [[quick-ratio]] of [[cash-ratio]].

### Solvabiliteit verwarren met rentabiliteit (ROE) 🔗

Solvabiliteit zegt niets over winstgevendheid. Een onderneming met EV 60 % maar verlieslatend boekjaar ziet de ratio dalen — solvabiliteit en rentabiliteit (ROE) meten verschillende dingen. ROE meet hoe efficiënt het EV rendeert; solvabiliteit meet de structurele aandeel-grootte van EV in de balans.

### Solvabiliteit verwarren met financial leverage / debt-to-equity 🔗

Klassieke solvabiliteit = EV / Totaal passief (schaal 0–100 %). Debt-to-equity = VV / EV (schaal > 0, > 1 betekent meer schuld dan EV). Ze meten dezelfde onderliggende structuur maar geven andere getallen. Bij Angelsaksische bronnen lees je vaak D/E; bij Belgische ITAA-praktijk meestal de klassieke ratio.

### Solvabiliteit-1 en solvabiliteit-2 als synoniem behandelen 🔗

Sommige bronnen onderscheiden 'solvabiliteit op lange termijn' (EV / totaal vermogen — klassiek) van 'solvabiliteit op korte termijn' (EV / kort-vreemd vermogen — zelden gebruikt). Niet verwarren met Solvency II — dat is een prudentieel kader voor verzekeraars en heeft niets te maken met deze klassieke ratio.

### Bank-Tier-1-ratio of Solvency II als 'solvabiliteit' lezen voor gewone vennootschap 🔗

Banken (Basel III) en verzekeraars (Solvency II) gebruiken risicogewogen kapitaalratio's met eigen drempels (8 % à 13 %). Die getallen mogen NOOIT als referentie dienen voor een gewone vennootschap — risicowegingen, kapitaalcomponenten en drempels zijn fundamenteel verschillend.



## Wat dit record dekt

### Behandelde competenties (chronologisch)

1. **Balans lezen — EV vs VV onderscheiden** — zie [Balans lezen — EV vs VV onderscheiden](#formule-klassiek)2. **Solvabiliteitsratio berekenen uit jaarrekening** — zie [Solvabiliteitsratio berekenen uit jaarrekening](#rekenvoorbeeld)3. **Interpretatie versus vuistregel-drempels** — zie [Interpretatie versus vuistregel-drempels](#interpretatie-vuistregels)4. **Sectorgecorrigeerde benchmarking** — zie [Sectorgecorrigeerde benchmarking](#sectorgebondenheid)5. **Achtergestelde-lening- en herwaarderings-correctie toepassen** — zie [Achtergestelde-lening- en herwaarderings-correctie toepassen](#interpretatie-valkuilen)6. **Wettelijke alarmbel-drempel herkennen** — zie [Wettelijke alarmbel-drempel herkennen](#wettelijke-drempels-alarmbel)7. **Going-concern-beoordeling als commissaris** — zie [Going-concern-beoordeling als commissaris](#going-concern-beoordeling)8. **Thin-cap-grens 5:1 op groepslening toepassen** — zie [Thin-cap-grens 5:1 op groepslening toepassen](#thin-cap-rule)9. **Bestuur adviseren over financierings-keuze (EV vs VV)** — zie [Bestuur adviseren over financierings-keuze (EV vs VV)](#advies-financierings-keuze)
### Behandelde termen (alfabetisch)

- **achtergestelde lening** — zie [↑](#interpretatie-valkuilen)- **alarmbel-drempel BV** — zie [↑](#wettelijke-drempels-alarmbel)- **alarmbel-drempel NV (½ en ¼ kapitaal)** — zie [↑](#wettelijke-drempels-alarmbel)- **balanstotaal** — zie [↑](#formule-klassiek)- **bank-covenant** — zie [↑](#due-diligence-rol)- **debt-to-equity** — zie [↑](#formule-varianten)- **eigen vermogen** — zie [↑](#formule-klassiek)- **financiële onafhankelijkheid** — zie [↑](#definitie)- **going concern** — zie [↑](#going-concern-beoordeling)- **herwaarderingsmeerwaarde** — zie [↑](#interpretatie-valkuilen)- **netto-actief** — zie [↑](#wettelijke-drempels-alarmbel)- **schuldgraad** — zie [↑](#formule-varianten)- **sectornorm** — zie [↑](#sectorgebondenheid)- **thin-capitalisation 5:1** — zie [↑](#thin-cap-rule)- **uitgestelde belastingen** — zie [↑](#interpretatie-valkuilen)- **vreemd vermogen** — zie [↑](#formule-klassiek)
### Behandelde formules

- {'naam': 'Solvabiliteitsratio (klassiek / NBB)', 'expressie': 'Eigen vermogen / Totaal passief × 100 %'}
- {'naam': 'Schuldgraad (omgekeerd)', 'expressie': '100 % − Solvabiliteitsratio'}
- {'naam': 'Debt-to-equity', 'expressie': 'Eigen vermogen / Vreemd vermogen'}
- {'naam': 'Thin-cap-grens groepslening (WIB92 art. 198 §1 11°/1)', 'expressie': '5 × (belaste reserves bij begin BT + gestort kapitaal bij einde BT)'}
- {'naam': 'Drempel BV alarmbel', 'expressie': 'Netto-actief < 0'}
- {'naam': 'Drempel NV alarmbel — eerste trigger', 'expressie': 'Netto-actief < ½ × geplaatst kapitaal'}
- {'naam': 'Drempel NV alarmbel — tweede trigger', 'expressie': 'Netto-actief < ¼ × geplaatst kapitaal'}


