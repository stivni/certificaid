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


_Grondslag: IAS 36 alinea 6, 66, 80_

### Terugneming impairment — behalve goodwill ⚖️

Bij latere verbetering van omstandigheden kan een impairment-verlies worden **teruggenomen** — maximum tot het bedrag dat de boekwaarde zou hebben gehad zonder de oorspronkelijke impairment (alinea 117). Uitzondering: een impairment op **goodwill mag NOOIT worden teruggenomen** (alinea 124) — goodwill is per definitie waarschijnlijk-vervangen-door-intern-gegenereerde-goodwill bij herstel, en die mag niet geactiveerd worden.

**Waarom?** Symmetrie: als de oorzaak van impairment verdwijnt, hoort de boekwaarde te herstellen. Maar goodwill is een uitzondering omdat herstel typisch via intern gegenereerde goodwill gebeurt — wat IFRS niet toestaat te activeren.


_Grondslag: IAS 36 alinea 114-117 + 124_


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

1. Zelena's productielijn Y nieuwe boekwaarde = € 7.200.000; resterende gebruiksduur 5 jaar; restwaarde € 0.
2. Nieuwe jaarafschrijving = € 7.200.000 / 5 = € 1.440.000/jaar.
3. Oude afschrijving was € 8.500.000 / 5 = € 1.700.000/jaar; verschil − € 260.000/jaar minder afschrijving over toekomst.

**Grondslag**: IAS 36 alinea 63


> [!info]- Niet verwarren met [[herwaarderingsmeerwaarden]]
> Impairment (IAS 36) is een **verlaging** van boekwaarde wanneer realiseerbare waarde gedaald is — een verlies. Herwaardering (IAS 16 alinea 31) is een **verhoging** naar marktwaarde — geen verlies maar reserve in OCI. Beide kunnen elkaar afwisselen voor hetzelfde actief: een herwaardering vergroten, dan impairment dat eerst de herwaarderingsreserve verbruikt voor het in W&V terechtkomt.
>
> _Trigger_: Examen: 'boekwaarde > marktwaarde' → impairment (verlaging, W&V); 'marktwaarde > boekwaarde + herwaarderingsmodel' → herwaardering (verhoging, OCI).


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

> [!todo] Voorbeeld ontbreekt voor dit concept
> Een latere ENRICH-pass voegt een synthese-voorbeeld toe.

## Bronnen

[^1]: `IAS-16-materiele-vaste-activa__sec_waardering-na-eerste-opname`
[^2]: `IAS-38-immateriele-activa__sec_realiseerbaarheid-van-de-boekwaarde-bijzondere-waardeverminderingsverliezen`
