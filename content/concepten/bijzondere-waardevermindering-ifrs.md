---
title: Bijzondere waardevermindering onder IFRS (IAS 36)
tags:
- concept
- cluster
- po-1-5
linked_anchors:
- 1.5.V.A
- 1.5.V.B
- 1.5.IV.C
- 1.5.V
programmaonderdelen:
- '1.5'
confidence: grounded
node_type: cluster
status: seed
schema_version: '1.5'
gegenereerd_uit: data/concepten/records/bijzondere-waardevermindering-ifrs.json
gegenereerd_op: '2026-05-18'
---
# Bijzondere waardevermindering onder IFRS (IAS 36) ⚖️

> [!summary] Korte inhoud
> IAS 36 — Bijzondere waardevermindering van activa zorgt ervoor dat een entiteit haar activa niet boven hun **realiseerbare waarde** (recoverable amount) waardeert.

IAS 36 — Bijzondere waardevermindering van activa zorgt ervoor dat een entiteit haar activa niet boven hun **realiseerbare waarde** (recoverable amount) waardeert. Op elke balansdatum: beoordeel of er **aanwijzingen** zijn voor waardevermindering. Voor goodwill, immateriële activa met onbepaalde gebruiksduur en nog-niet-beschikbare-voor-gebruik immateriële activa: jaarlijkse test **verplicht**, ongeacht aanwijzingen. Een bijzondere waardevermindering (impairment) treedt op wanneer de **boekwaarde** de **realiseerbare waarde** overschrijdt. De realiseerbare waarde = de **hoogste** van: (a) **reële waarde minus verkoopkosten** (fair value less costs of disposal); of (b) **bedrijfswaarde** (value in use, contante waarde van toekomstige kasstromen uit voortgezet gebruik + vervreemding). Impairment-verlies in winst of verlies (tenzij activa onder herwaarderingsmodel — dan eerst herwaarderingsreserve aanspreken). Voor goodwill: nooit terugneembaar. Voor andere activa: terugneembaar bij verbeterde omstandigheden, maximum tot oorspronkelijke kostprijs minus normale afschrijvingen.

_Bron: IAS 36 algemeen_


## Bouwstenen

### Kasstroomgenererende eenheid (CGU) ⚖️

Als een individueel actief geen onafhankelijke kasstromen genereert, wordt het impairment-test uitgevoerd op het niveau van de **kasstroomgenererende eenheid** (cash-generating unit, CGU): de kleinste groep activa die onafhankelijke kasstromen genereert. Goodwill wordt toegewezen aan CGU's bij overname (alinea 80).

**Waarom?** Voor productielijnen, fabrieken, divisies kan een individuele machine geen aparte cashflows tonen. De CGU is het bedrijfseconomisch zinvolle niveau van impairment.



Zelena Bio's biofarmaceutische divisie genereert eigen kasstromen; de individuele machines binnen die divisie niet. Impairment-test op divisieniveau, niet per machine. Goodwill van vroegere acquisitie ad € 12.000.000 is toegewezen aan deze CGU.

_Grondslag: IAS 36 alinea 6, 66, 80_

### Terugneming impairment — behalve goodwill ⚖️

Bij latere verbetering van omstandigheden kan een impairment-verlies worden **teruggenomen** — maximum tot het bedrag dat de boekwaarde zou hebben gehad zonder de oorspronkelijke impairment (alinea 117). Uitzondering: een impairment op **goodwill mag NOOIT worden teruggenomen** (alinea 124) — goodwill is per definitie waarschijnlijk-vervangen-door-intern-gegenereerde-goodwill bij herstel, en die mag niet geactiveerd worden.

**Waarom?** Symmetrie: als de oorzaak van impairment verdwijnt, hoort de boekwaarde te herstellen. Maar goodwill is een uitzondering omdat herstel typisch via intern gegenereerde goodwill gebeurt — wat IFRS niet toestaat te activeren.



Zelena's productielijn Y in 2028 (twee jaar na impairment): nieuwe regelgeving versoepelt, marktwaarde herstelt. Boekwaarde 31 december 2028 (na 2 jaar herziene afschrijving € 1.440.000/jaar op € 7.200.000) = € 4.320.000. Hypothetische boekwaarde zonder oorspronkelijke impairment (€ 8.500.000 − 2 × € 2.000.000) = € 4.500.000. Realiseerbare waarde nu = € 5.500.000. Terugneming begrensd door hypothetische boekwaarde: € 4.500.000 − € 4.320.000 = € 180.000 in W&V (IAS 36 alinea 117-ceiling).

_Grondslag: IAS 36 alinea 114-117 + 124_

### BE-GAAP-tegenhanger: art. 3:42 KB WVV ⚖️

Onder Belgisch boekhoudrecht heet een vergelijkbare verlaging geen 'impairment' maar een **aanvullende of niet-recurrente afschrijving** (art. 3:42 § 1, tweede lid KB WVV) voor MVA met beperkte gebruiksduur, of een **waardevermindering wegens duurzame minderwaarde** (art. 3:42 § 2) voor MVA met onbeperkte gebruiksduur. De trigger lijkt op IAS 36: 'boekhoudkundige waarde hoger dan gebruikswaarde voor de vennootschap' wegens technische ontwaarding of gewijzigde economische/technologische omstandigheden.

**Waarom?** Belgisch boekhoudrecht kent geen formele realiseerbare-waarde-test met FVLCD/VIU-tweesporenbenadering en geen verplichte jaarlijkse goodwill-test. De afweging gebeurt 'naar redelijkheid' onder voorzichtigheidsbeginsel; documentatie-eisen zijn lichter dan onder IAS 36 (kein discounted cash flow-formule voorgeschreven).


**In de praktijk**: Praktisch verschil voor de stagiair: een IFRS-rapporteur moet jaarlijks scannen op aanwijzingen en het realiseerbare-waarde-onderzoek documenteren; een BE-GAAP-rapporteur boekt aanvullende afschrijving wanneer 'duidelijk' is dat de gebruiks- of marktwaarde lager is dan de boekwaarde. Bij dubbele rapportage (BE-GAAP + IFRS, bv. beursgenoteerde groep) ontstaan vaak tijdsverschillen omdat de IFRS-test eerder triggers oppikt.


_Grondslag: KB WVV art. 3:42 § 1 tweede lid + § 2_


## Berekening

### Vier-staps-procedure impairment-test IAS 36

*Voor elk actief (of CGU) met aanwijzing op waardevermindering: scan op aanwijzingen, bereken realiseerbare waarde, vergelijk met boekwaarde, boek het verschil als impairment-verlies, herzie het afschrijvingsplan.*

### 1. Scan op aanwijzingen voor waardevermindering

Aan het einde van elke verslagperiode toetst de entiteit of er aanwijzingen zijn voor waardevermindering. Externe aanwijzingen (alinea 12): significant daling marktwaarde, ongunstige technologische/markt-/economische veranderingen, gestegen marktrentes, boekwaarde nettoactiva > marktkapitalisatie. Interne aanwijzingen: bewijs van fysieke schade, plannen tot stopzetting/herstructurering, slechtere economische prestaties dan verwacht.

**Waarom?** Niet voor elk actief is een jaarlijkse impairment-test verplicht — alleen wanneer er aanwijzingen zijn. Voor goodwill en immaterieel-onbepaald geldt wel een verplichte jaarlijkse test, ongeacht aanwijzingen.

**📥 Input**:
- Externe + interne data → **Marktontwikkeling + operationele indicatoren** _(informatie)_

**📤 Output**:
- Impairment-aanwijzingenrapport → **Lijst getroffen activa/CGU's** _(rapport)_

**🛠️ Hoe**:

1. Zelena Bio NV scant in december 2026 op aanwijzingen. Externe aanwijzing: nieuwe Europese regelgeving 2027 beperkt productie van een product — marktwaarde van bijbehorende productielijn dalen.
2. Interne aanwijzing: divisie X heeft drie jaar onder budget gepresteerd.
3. Conclusie: impairment-test vereist voor productielijn Y en divisie X.

**Grondslag**: IAS 36 alinea 9-14

### 2. Bereken de realiseerbare waarde

Realiseerbare waarde = hoogste van (a) reële waarde minus verkoopkosten (FVLCD) of (b) bedrijfswaarde (VIU). VIU = contante waarde van toekomstige kasstromen uit voortgezet gebruik + vervreemdingswaarde aan einde gebruiksduur, gedisconteerd tegen risico-aangepaste rentevoet.

**Waarom?** De entiteit kiest de hoogste van twee — dat is wat ze 'redelijkerwijs zou kunnen realiseren'. Als verkoop meer opbrengt dan voortgezet gebruik, zou het management rationeel verkopen; als gebruik meer opbrengt, doorgaan.

**📥 Input**:
- Marktdata of taxatie → **Reële waarde - kosten** _(boekhoudkundig-bedrag)_
- Cashflow-prognoses + WACC → **Bedrijfswaarde** _(boekhoudkundig-bedrag)_

**📤 Output**:
- Realiseerbare waarde → **Bedrag** _(boekhoudkundig-bedrag)_

**🛠️ Hoe**:

1. Zelena's productielijn Y: boekwaarde € 8.500.000.
2. Reële waarde minus verkoopkosten: marktconforme tweedehandsprijs € 6.200.000 − verkoopkosten € 200.000 = € 6.000.000.
3. Bedrijfswaarde: verwachte kasstromen over resterende 5 jaar, gedisconteerd tegen 8% = € 7.200.000.
4. Realiseerbare waarde = hoogste van € 6.000.000 en € 7.200.000 = **€ 7.200.000**.

**Grondslag**: IAS 36 alinea 18-21

### 3. Vergelijk en boek impairment

Als boekwaarde > realiseerbare waarde: impairment-verlies = verschil. Boek het verlies in winst of verlies. Bij activa onder het herwaarderingsmodel (IAS 16 alinea 39): eerst openstaande herwaarderingsreserve aanspreken (impact in OCI), pas het excedent in winst of verlies.

**Waarom?** Impairment vermijdt dat activa met blijvende waardevermindering tegen overgewaardeerde boekwaarde op de balans blijven — het is een directe correctie van een onhoudbare positie.

**📥 Input**:
- Boekwaarde actief → **Huidige boekwaarde** _(boekhoudkundig-bedrag)_
- Realiseerbare waarde → **Bedrag berekend in stap 2** _(boekhoudkundig-bedrag)_

**📤 Output**:
- Boeking impairment → **Verlies in W&V + reductie boekwaarde** _(boekingsregel)_

**🛠️ Hoe**:

1. Boekwaarde Zelena's productielijn Y = € 8.500.000.
2. Realiseerbare waarde = € 7.200.000.
3. Impairment-verlies = € 8.500.000 − € 7.200.000 = € 1.300.000.
4. Boek: Debet 'Bijzondere waardevermindering' € 1.300.000 in W&V; Credit 'Geaccumuleerde waardevermindering productielijn Y' € 1.300.000.
5. Nieuwe boekwaarde = € 7.200.000; toekomstige afschrijvingen berekenen op deze gereduceerde basis.

> [!example]- Voorbeeld: Zelena Bio NV's productielijn Y op 31 december 2026: boekwaarde € 8.500.000, realiseerbare waarde € 7.200.000 (na stap 2…
> Zelena Bio NV's productielijn Y op 31 december 2026: boekwaarde € 8.500.000, realiseerbare waarde € 7.200.000 (na stap 2). Impairment-verlies te boeken in W&V.
>
> 1. **Bereken impairment-verlies** 🧮
>
>    Impairment = boekwaarde − realiseerbare waarde
>               = € 8.500.000 − € 7.200.000
>               = **€ 1.300.000**
>
> 2. **Boekingsregel impairment** 📝
>
>    | Rekening                                            |     Debet (€) |    Credit (€) |
>    |-----------------------------------------------------|--------------:|--------------:|
>    | 660 — Bijzondere waardevermindering productielijn Y |     1.300.000 |               |
>    | 2329 — Geaccumuleerde waardevermindering            |               |     1.300.000 |
>    
>    Debet-totaal = Credit-totaal = € 1.300.000 (balanseffect: actiefzijde daalt; W&V belast).
>
> 3. **Nieuwe boekwaarde** 📊
>
>    | Productielijn Y — balansweergave 31 december 2026 |        € |
>    |---------------------------------------------------|----------:|
>    | Bruto-aanschaffingswaarde                          |10.000.000 |
>    | − Geaccumuleerde afschrijvingen                    |−1.500.000 |
>    | − Geaccumuleerde waardevermindering (IAS 36)       |−1.300.000 |
>    | **Boekwaarde (netto)**                              | **7.200.000** |
>

**Grondslag**: IAS 36 alinea 59-60

### 4. Herzie afschrijvingsplan

Na een impairment moet het afschrijvingsplan voor het actief worden herzien: de nieuwe (lagere) boekwaarde wordt over de resterende gebruiksduur afgeschreven. Afschrijvingsbedrag per periode = nieuwe boekwaarde / resterende gebruiksduur (alinea 63).

**Waarom?** Het afschrijfbaar bedrag is nu lager; afschrijven over de oorspronkelijke kost zou inconsistent zijn. Het herziene plan zorgt voor coherente cijfers in toekomstige jaren.

**📥 Input**:
- Nieuwe boekwaarde na impairment → **Bedrag** _(boekhoudkundig-bedrag)_
- Vasteactivafile → **Resterende gebruiksduur** _(jaar)_

**📤 Output**:
- Aangepast afschrijvingsplan → **Nieuwe jaarlijkse afschrijving** _(boekhoudkundig-bedrag)_

**🛠️ Hoe**:

1. Zelena's productielijn Y nieuwe boekwaarde = € 7.200.000 na impairment.
2. Resterende gebruiksduur ook herzien wegens versnelde technologische veroudering: 5 jaar (i.p.v. 4,25 jaar die rekenkundig zou volgen uit een ongewijzigd plan).
3. Nieuwe jaarafschrijving = € 7.200.000 / 5 = € 1.440.000/jaar.
4. Oorspronkelijk afschrijvingsplan bedroeg € 10.000.000 / 5 = € 2.000.000/jaar; het herziene plan ligt € 560.000/jaar lager — de impairment heeft de jaarlijkse W&V-impact significant gereduceerd.

**Grondslag**: IAS 36 alinea 63


> [!info]- Niet verwarren met [[herwaarderingsmeerwaarden]]
> Impairment (IAS 36) is een **verlaging** van boekwaarde wanneer realiseerbare waarde gedaald is — een verlies. Herwaardering (IAS 16 alinea 31) is een **verhoging** naar marktwaarde — geen verlies maar reserve in OCI. Beide kunnen elkaar afwisselen voor hetzelfde actief: een herwaardering vergroten, dan impairment dat eerst de herwaarderingsreserve verbruikt voor het in W&V terechtkomt.
>
> _Trigger_: Examen: 'boekwaarde > marktwaarde' → impairment (verlaging, W&V); 'marktwaarde > boekwaarde + herwaarderingsmodel' → herwaardering (verhoging, OCI).

> [!info]- Niet verwarren met [[aanvullende-afschrijving-be-gaap]]
> IAS 36 vereist formele realiseerbare-waarde-test (hoogste van FVLCD en VIU) en jaarlijkse test voor goodwill + immaterieel-onbepaald. Art. 3:42 KB WVV vereist alleen dat aanvullende afschrijving wordt geboekt zodra de boekhoudkundige waarde 'hoger' is dan de gebruikswaarde voor de vennootschap — zonder voorgeschreven rekenmethode. Goodwill onder BE-GAAP wordt afgeschreven (art. 3:42 § 1), niet jaarlijks getest zoals onder IAS 36.
>
> _Trigger_: Examen: 'Onder welk regime werd deze waardevermindering geboekt?' → toets op aanwezigheid van DCF-onderbouwing en CGU-allocatie (= IFRS) versus eenvoudige verwijzing naar duurzame minderwaarde (= BE-GAAP).


## Valkuilen

> [!warning]- Impairment op goodwill is NOOIT terugneembaar (alinea 124)
> ⚠️ Impairment op goodwill is NOOIT terugneembaar (alinea 124). Een entiteit die € 5.000.000 goodwill-impairment boekt in jaar 1 en herstel ziet in jaar 3, mag de impairment niet ongedaan maken — de goodwill blijft op de verlaagde boekwaarde. ⚖️
>
> _Bron: IAS 36 alinea 124_


> [!warning]- Bedrijfswaarde (VIU) gebruikt 'reasonable and supportable assumptions' — geen optimistische scenario-planning
> ⚠️ Bedrijfswaarde (VIU) gebruikt 'reasonable and supportable assumptions' — geen optimistische scenario-planning. Te hoge cashflowprognoses zouden de impairment ondergraven. Externe inputs (markt, sectorrapport) zijn belangrijke checks. ⚖️
>
> _Bron: IAS 36 alinea 30-57_



## Zie ook

- **Vereist kennis van**: [[materiele-vaste-activa-ifrs]]
- **Vereist kennis van**: [[immateriele-vaste-activa-ifrs]]

## Voorbeelden

### Impairment + latere terugneming productielijn Y

_Personages: Zelena Bio NV_

Zelena Bio NV's productielijn Y in farma-divisie: aanschaffingswaarde € 10.000.000 op **1 april 2026**, gebruiksduur 5 jaar lineair (€ 2.000.000/jaar), restwaarde € 0. Op 31 december 2026 (9 maanden in gebruik, dus 0,75 jaar) geaccumuleerde afschrijving = 0,75 × € 2.000.000 = € 1.500.000 → boekwaarde vóór impairment = **€ 8.500.000**. In december 2026 kondigt de EU regelgeving aan die het product per 2030 verbiedt — interne aanwijzing voor impairment.

1. Identificeer aanwijzingen: regulatoire wijziging EU 2030 (extern) + jaarlijkse verkoop daalt 30% versus budget (intern).
2. Bereken realiseerbare waarde: FVLCD € 6.000.000 (markt voor tweedehands productielijnen); VIU € 7.200.000 (DCF over resterende 5 jaar, WACC 8%). Hoogste = € 7.200.000.
3. Vergelijk: boekwaarde € 8.500.000 > realiseerbare waarde € 7.200.000 → impairment € 1.300.000.
4. Boek het verlies (zie illustratie) en herzie het afschrijvingsplan. Wegens dezelfde gewijzigde technologische omstandigheden wordt ook de **resterende gebruiksduur** herijkt naar 5 jaar (versnelde veroudering, IAS 36 alinea 63). Nieuwe afschrijving = € 7.200.000 / 5 jaar = € 1.440.000/jaar.
5. Twee jaar later (31 december 2028): EU versoepelt regelgeving. Werkelijke boekwaarde = € 7.200.000 − 2 × € 1.440.000 = € 4.320.000. Hypothetische boekwaarde zonder oorspronkelijke impairment (gebruik blijft 2,75 jaar sinds 1 april 2026): € 10.000.000 − 2,75 × € 2.000.000 = **€ 4.500.000** (ceiling, IAS 36 alinea 117). Realiseerbare waarde nu € 5.500.000. Terugneming begrensd: min(€ 5.500.000 − € 4.320.000, € 4.500.000 − € 4.320.000) = min(€ 1.180.000, € 180.000) = **€ 180.000** in W&V.
#### Impairment-boeking 31 december 2026
_Debet- en credit-totaal beide € 1.300.000. De geaccumuleerde waardevermindering is een tegenpost op het brutoactief — boekwaarde valt naar € 7.200.000._

| Rekening | Debet | Credit |
|---|---:|---:|
| 660 — Bijzondere waardevermindering op productielijn Y _(Verlies in W&V)_ | 1300000 |  |
| 2329 — Geaccumuleerde waardevermindering productielijn Y _(Reductie boekwaarde op balans)_ |  | 1300000 |

#### Terugneming impairment 31 december 2028
_Symmetrische tegenboeking. Maximum begrensd door hypothetische-boekwaarde-zonder-impairment-regel (IAS 36 alinea 117)._

| Rekening | Debet | Credit |
|---|---:|---:|
| 2329 — Geaccumuleerde waardevermindering productielijn Y _(Terugneming impairment)_ | 180000 |  |
| 760 — Terugneming bijzondere waardevermindering _(Opbrengst in W&V (ceiling toegepast))_ |  | 180000 |

#### Boekwaarde-evolutie productielijn Y over tijd



## Bronnen

[^1]: `IAS-16-materiele-vaste-activa__sec_waardering-na-eerste-opname`
[^2]: `IAS-38-immateriele-activa__sec_realiseerbaarheid-van-de-boekwaarde-bijzondere-waardeverminderingsverliezen`
[^3]: `KB-WVV-2019__art_3_29`
