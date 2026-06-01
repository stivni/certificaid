---
title: "Themafiche — Art. 171 afzonderlijke aanslagvoeten"
description: "Themafiche voor sub-cluster afzonderlijke aanslagvoeten PB (PO 2.2): stopzettingsmeerwaarden, opzegvergoedingen, achterstallen, kapitaal aanvullend pensioen"
tags:
  - themafiche
  - po-2.2
  - cluster-personenbelasting
---

<div class="no-print">

> ⚠️ **Voorlopig — themafiche-laag wordt uitgefaseerd.** Per **ADR-039** vervangt één PO-samenvatting per programmaonderdeel de cluster-themafiches. Deze fiche blijft beschikbaar tot het relevante PO een leerpad krijgt — dan migreert de inhoud naar `content/studiemateriaal/<po-slug>/samenvatting.md`. Voor cross-PO themafiches (vergelijkingen tussen verschillende PO's) volgt een aparte beslissing per fiche: incorporeren in alle relevante samenvattingen, óf upgraden naar concept-fiche.

</div>

<div class="no-print">

> **Themafiche — kapstok voor herhaling.** Wanneer mag/moet PB afzonderlijk getarifeerd worden i.p.v. progressief? Art. 171 WIB lijst zes hoofdgroepen op met eigen percentages. Voor verhaal en routekaart: [[studiemateriaal/2-2|overzicht PO 2.2]].

</div>

---

## Take-away

- **Afzonderlijke aanslag = alternatief tarief, niet vrijstelling** — inkomen wordt belast aan vast percentage in plaats van progressieve schaal
- **Globalisatie-test altijd toepassen** — fiscus past het regime toe dat voor de belastingplichtige het **gunstigst** is (afzonderlijk vs progressief samen met andere inkomsten)
- **Stopzettingsmeerwaarde heeft DRIE tarieven** afhankelijk van type — 10% / 16,5% / 33% / progressief — keuze hangt af van leeftijd + omstandigheid
- **Opzegvergoeding > forfait**: gemiddeld tarief vorige 4 jaar gebruiken — kan fors lager liggen dan marginaal
- **Aanvullend pensioen-kapitaal**: 10% / 16,5% / 18% / 20% afhankelijk van leeftijd uitkering — uitstellen tot wettelijke pensioenleeftijd loont fiscaal

---

## Art. 171 — zes hoofdgroepen

| Categorie | Voorbeeld | Tarief (richting) | Voorwaarde |
|---|---|---|---|
| **Stopzettingsmeerwaarden** | Eenmanszaak verkoop bij pensioen | 10% / 16,5% / 33% / progressief | Cf. tabel hieronder |
| **Opzeg- en ontslagvergoedingen** | Wettelijke opzegvergoeding | Gemiddeld tarief vorige 4 inkomstenjaren | Werkgever-werknemer-relatie |
| **Kapitaal aanvullend pensioen** | Groepsverzekering uitkering | 10% / 16,5% / 18% / 20% | Leeftijd + uitkeringsmoment |
| **Achterstallen (laattijdige uitbetaling)** | Pensioen 2 jaar later uitbetaald | Tarief jaar waarop ze betrekking hebben | Vertraging > normaal |
| **Bepaalde diverse inkomsten** | Speculatieve meerwaarde aandelen | 33% | Buiten normaal beheer privévermogen |
| **Bepaalde meerwaarden gebouwen** | Verkoop gebouw ≤ 5 jaar | 16,5% | Buiten beroepsbestemming |

⚠️ Concrete percentages + leeftijdsdrempels: **Cijferzakboekje bij examen** verplicht raadplegen.

---

## Stopzettingsmeerwaarde — beslisboom

```mermaid
flowchart TD
    A["Stopzetting beroepsactiviteit"] --> B{"Materiele vaste activa<br/>of voorraden?"}
    B -->|materiele vaste activa| C{"Vrijwillig of gedwongen?"}
    C -->|vrijwillig + leeftijd 60+| D["10% tarief"]
    C -->|vrijwillig + jonger| E["16,5% tarief"]
    C -->|gedwongen<br/>(invaliditeit, overmacht, overlijden)| F["10% tarief"]
    B -->|voorraden/handelsgoederen| G["Progressief tarief<br/>(geen art. 171)"]
    B -->|immateriële vaste activa<br/>(klantenbestand)| H["33% tarief<br/>(of progressief indien gunstiger)"]
    A --> X["Globalisatie-test:<br/>afzonderlijk vs progressief"]
    X -.fiscus past gunstigste toe.-> SAM["Eindstand"]
```

---

## Opzegvergoeding — gemiddeld tarief vorige 4 jaar

| Stap | Berekening |
|---|---|
| 1 | Som van belastbare beroepsinkomsten van 4 vorige jaren |
| 2 | Som van PB op die 4 jaren (volgens hun toenmalige tariefschijven) |
| 3 | Gemiddeld tarief = som PB / som inkomen × 100 |
| 4 | Opzegvergoeding × gemiddeld tarief = belasting |
| 5 | Globalisatie-test: vergelijk met progressief samen met huidig jaar |

**Effect**: bij sterk gestegen inkomen leidt afzonderlijk tot lagere belasting; bij stabiel inkomen vaak vergelijkbaar.

---

## Aanvullend pensioen-kapitaal — leeftijdstabel (richting)

| Leeftijd uitkering | Tarief (richting) |
|---|---|
| Wettelijke pensioenleeftijd | 10% |
| 65 jaar | 16,5% |
| 62-64 jaar | 18% |
| 60-61 jaar | 20% |
| Vóór 60 jaar | Progressief (geen art. 171) |

**Voorwaarde 80%-regel** geldt aan opbouw-kant (groepsverzekering moet wettelijke + aanvullend pensioen onder 80% laatste brutoloon houden om aftrekbaarheid premies bij werkgever te behouden — cross VenB).

⚠️ Concrete percentages: **Cijferzakboekje bij examen**.

---

## Globalisatie-test — wie kiest?

| Wie? | Hoe? |
|---|---|
| **Fiscus past automatisch** het gunstigste regime toe (afzonderlijk vs samenvoeging met andere inkomsten) | Geen keuzevrijheid voor belastingplichtige |
| Berekening | Tax-on-web/aanslagprogrammatuur doet beide berekeningen + neemt laagste |
| Praktijk | Bij aangifte juist invullen in de juiste vakken; programma doet de rest |

---

## ⚠️ Valkuilen

| Valkuil | Wat klopt er niet | Wat klopt wél |
|---|---|---|
| Afzonderlijk = vrijstelling | Het inkomen blijft belastbaar | Alternatief tarief, geen vrijstelling |
| Gunstigste regime kiezen | Geen keuze — fiscus past gunstigste automatisch toe | Belastingplichtige vult correct in; programma berekent beide |
| Voorraden stopzettingsmeerwaarde aan 16,5% | Voorraden = progressief tarief | Alleen materiële + immateriële vaste activa krijgen art. 171 |
| Opzegvergoeding = laagste tarief automatisch | Gemiddeld vorige 4 jaar kan hoger zijn dan marginaal huidig jaar | Globalisatie-test kan progressief gunstiger maken |
| Aanvullend pensioen vóór 60 aan 20% | Vóór 60 = progressief tarief | Wachten tot pensioenleeftijd = 10% (groot voordeel) |
| Achterstallen aan huidig tarief | Tarief van jaar waarop ze betrekking hebben | Pensioen 2024 betaald in 2026 = tarief AJ 2025 (= IJ 2024) |
| Speculatieve meerwaarde aandelen vrijgesteld | Onder art. 90 + art. 171 = 33% | Buiten normaal beheer privévermogen → 33% afzonderlijk |

---

<div class="no-print">

## Doorklik — losse concept-fiches

**Per categorie**
- [[stopzettingsmeerwaarde]] — 10% / 16,5% / 33% / progressief tarieven
- [[diverse-inkomsten-pb]] — art. 90 + art. 171 koppeling
- [[meerwaarde-aandelen-venb]] — venn-kant (raakt PB via aandeelhouder)

**Pensioen + opzeg**
- [[werknemersbezoldiging]] — opzegvergoeding-kant
- [[bedrijfsleidersbezoldiging]] — pensioen + IPT-link

**Verwante themafiches**
- [[themafiches/pb-berekeningsschema|Themafiche — PB-berekeningsschema]]
- [[themafiches/inkomstencategorieen|Themafiche — Inkomstencategorieën PB]]

</div>

---

*Themafiche afgeleid uit cluster personenbelasting (PO 2.2). Status: voorgesteld.*
