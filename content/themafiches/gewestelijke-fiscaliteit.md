---
title: "Themafiche — Gewestelijke fiscaliteit"
description: "Themafiche voor sub-cluster gewestelijke fiscaliteit (PO 2.7): overgedragen vs autonoom + bevoegdheidstabel + inningsadministratie"
tags:
  - themafiche
  - po-2.7
  - cluster-regionale-en-lokale-belastingen
---

<div class="no-print">

> ⚠️ **Voorlopig — themafiche-laag wordt uitgefaseerd.** Per **ADR-039** vervangt één PO-samenvatting per programmaonderdeel de cluster-themafiches. Deze fiche blijft beschikbaar tot het relevante PO een leerpad krijgt — dan migreert de inhoud naar `content/studiemateriaal/<po-slug>/samenvatting.md`. Voor cross-PO themafiches (vergelijkingen tussen verschillende PO's) volgt een aparte beslissing per fiche: incorporeren in alle relevante samenvattingen, óf upgraden naar concept-fiche.

</div>

<div class="no-print">

> **Themafiche — kapstok voor herhaling.** Drie types gewestbelasting + bevoegdheidstabel per belasting + Vlabel/Brussel/Wallonië-verschillen. Voor verhaal en routekaart: [[studiemateriaal/2-7|overzicht PO 2.7]].

</div>

---

## Take-away

- **Drie soorten gewestelijke fiscaliteit**: (1) overgedragen federale belastingen (BFW art. 3) · (2) aanvullingen op federale PB (BFW art. 6 — aanvullende gewestbelasting) · (3) autonome eigen gewestbelastingen
- **Gewestelijke ≠ lokale autonomie**: gewestelijk (art. 170 §2 GW + BFW) vs gemeente/provincie (art. 170 §4 + art. 41/162 GW)
- **Inningsadministratie wisselt per belasting + per gewest**: Vlabel (Vlaanderen voor erfbelasting, registratie, OV, BIV/VKB sinds 2011/2015) · FOD Financiën (Brussel + Wallonië voor meeste overgedragen belastingen)
- **Aanknopingspunt = lokalisatie**: bepaalt welk gewest mag heffen — woonplaats / ligging onroerend goed / inschrijving voertuig
- **5-jaarsregel voor erfbelasting**: gewest waar fiscale woonplaats was tijdens **langste periode** in 5 jaar vóór overlijden

---

## Drie types gewestelijke fiscaliteit

| Type | Voorbeeld | BFW-grond | Tarief-vrijheid |
|---|---|---|---|
| **1. Overgedragen federale belasting** | Erfbelasting, registratierecht, OV, BIV, verkeersbelasting | BFW art. 3 + 4 | Gewest mag tarief + grondslag + vrijstellingen wijzigen |
| **2. Aanvullende gewestbelasting op PB** | Aanvullende belasting op PB (alle 3 gewesten heffen aan eigen tarief) | BFW art. 6 + 7 | Opcentiemen + verminderingen door gewest |
| **3. Autonome eigen gewestbelasting** | Leegstandheffing, ongebouwde percelen, verkeersbelasting Brussels Hoofdstedelijk Gewest | Restbevoegdheid art. 170 §2 GW | Volledig autonoom — eigen wetboek + tarief |

---

## Bevoegdheidstabel — wie heft welke belasting?

| Belasting | Federaal | Gewest (welke?) | Toelichting |
|---|---|---|---|
| **PB (basis)** | Ja (WIB92) | Aanvulling per gewest (art. 6 BFW) | Federaal grondslag; gewest heft opcentiemen + verminderingen |
| **VenB / BNI** | Ja (WIB92) | Geen gewestbevoegdheid | 100% federaal |
| **BTW** | Ja (federaal + EU) | Geen | Niet overdraagbaar (EU-harmonisatie) |
| **Erfbelasting** | Vroeger | Vlaanderen (Vlabel) · Brussel (FOD) · Wallonië (FOD) | Vlabel sinds 2015; tarief + vrijstellingen gewest-specifiek |
| **Registratierecht (verkoop, schenking)** | Vroeger | Vlaanderen (Vlabel) · Brussel (FOD) · Wallonië (FOD) | Idem |
| **Onroerende voorheffing (OV)** | Basis-grondslag federaal (KI) | Vlaanderen (Vlabel) · Brussel (FOD) · Wallonië (FOD) | Gewest bepaalt opcentiemen + verminderingen |
| **Verkeersbelasting + BIV** | Vroeger | Idem | Vlaamse BIV-hervorming 2025 (vergroeningstaks) |
| **Aanvullende gemeentebelasting PB** | Geïnd federaal | Federaal — doorgestort aan gemeenten | Tarief = gemeenteraad |

---

## Aanknopingspunten — welk gewest is bevoegd?

```mermaid
flowchart TD
    A["Belasting?"] --> B{Type aanknopingspunt}
    B -->|PB-basis| W["Fiscale woonplaats op 1 jan AJ<br/>(WIB92 art. 2)"]
    B -->|OV + registratierecht + verkooprecht onroerend| L["Ligging onroerend goed"]
    B -->|Schenkbelasting onroerend| L
    B -->|Schenkbelasting roerend| WS["Fiscale woonplaats schenker"]
    B -->|Erfbelasting (rijksinwoner)| R5["5-jaarsregel: gewest waar<br/>BP langst woonde in 5 jr vóór overlijden"]
    B -->|Verkeersbelasting / BIV| IV["Plaats inschrijving voertuig<br/>= fiscale woonplaats houder"]
    B -->|Niet-rijksinwoner (erfbelasting)| LR["Ligging Belgische goederen"]
```

---

## Vergelijking gewesten — kerntarieven

| Belasting | Vlaanderen | Brussel | Wallonië |
|---|---|---|---|
| **Verkooprecht algemeen** | 12% (sinds 2022) | 12,5% | 12,5% |
| **Verkooprecht gezinswoning** | 3% (vrijstelling tot drempel) | Abattement tot 200k | Verminderingen + abattementen |
| **Verdeelrecht** | 1% | 2,5% | 1% (familie) / 2,5% (overig) |
| **Schenkbelasting onroerend rechte lijn** | 3-27% (5 schijven) | 3-30% | 3-30% |
| **Schenkbelasting roerend rechte lijn** | 3% vlak | 3% vlak | 3,3% vlak |
| **Erfbelasting rechte lijn / partners** | 3-27% (5 schijven) | 3-30% | 3-30% |
| **Erfbelasting derden** | 25-55% | 40-80% | 40-80% |
| **Gunstregime familiale onderneming** | 0% schenking + 3-7% erfbelasting | 0-3% schenking | 0% schenking met houdperiode 5j |
| **Aanvullende belasting PB** | Tarief per gemeente (typisch 6-9%) | Idem | Idem |
| **OV-opcentiemen gemeente** | Per gemeente (300-3000) | Idem | Idem |

⚠️ Concrete tarieven + schijfgrenzen: **Cijferzakboekje bij examen** — gewest-specifiek raadplegen.

---

## Inningsadministratie per belasting

| Belasting | Vlaanderen | Brussel | Wallonië |
|---|---|---|---|
| **Erfbelasting** | Vlabel (sinds 2015) | FOD Financiën | FOD Financiën |
| **Registratie / verkooprecht** | Vlabel (sinds 2015) | FOD Financiën | FOD Financiën |
| **Onroerende voorheffing** | Vlabel | FOD Financiën | FOD Financiën |
| **Verkeersbelasting + BIV** | Vlabel (sinds 2011) | Vlabel (technisch) of FOD | Vlabel (technisch) of FOD |
| **Aanvullende gemeentebelasting PB** | FOD (doorstort) | FOD (doorstort) | FOD (doorstort) |
| **Leegstandheffing** | Vlabel + gemeente | Brussel Fiscaliteit | Wallonië-administratie |

---

## ⚠️ Valkuilen

| Valkuil | Wat klopt er niet | Wat klopt wél |
|---|---|---|
| Gewestelijke = lokale autonomie | "Gewest" en "lokaal" door elkaar gebruikt | Gewest (art. 170 §2 GW + BFW) = Vlaanderen/Brussel/Wallonië. Lokaal (art. 170 §4 + 41/162) = provincie/gemeente |
| Vlaamse cliënt = Vlaamse fiscaliteit voor alles | Eén gewest-regime voor hele dossier | Per belasting opnieuw lokaliseren: PB = woonplaats 1 jan · OV = ligging · BIV = inschrijving |
| Eigen gewestbelasting = gewest int altijd | Gewest int eigen belastingen | BFW art. 5 §3: gewest mag beheer overnemen of bij FOD laten. Vlabel int Vlaamse overgedragen belastingen; Brussel/Wallonië houden FOD-inning aan |
| Erfbelasting woonplaats overlijdens-moment | Plaats op datum overlijden | 5-jaarsregel: gewest waar BP **langste** in 5 jr vóór overlijden woonde |
| Aanvullende belasting PB = autonome gewestbelasting | Volledige gewestbevoegdheid | Aanvulling op federale PB-grondslag; gewest bepaalt tarief, federaal int + stort door |
| Tarieven uit het hoofd kennen | Specifieke tarieven memoriseren | Cijferzakboekje bij examen — onthoud bandbreedtes + structuur, niet specifieke schijfwaarden |

---

<div class="no-print">

## Doorklik — losse concept-fiches

**Gewestelijke autonomie**
- [[gewestelijke-fiscale-autonomie]] — BFW-kader + types
- [[lokale-en-regionale-belastingen]] — overkoepelend
- [[gewestelijke-belastingverminderingen-pb]] — opcentiemen + verminderingen PB

**Per gewest-belasting**
- [[verkooprecht]] — registratierecht overdracht
- [[schenkbelasting]] — schenkingsregime per gewest
- [[erfbelasting]] — successieregime per gewest
- [[onroerende-voorheffing]] — OV per gewest

**Verwante themafiches**
- [[themafiches/gemeentelijke-belastingen|Themafiche — Gemeentelijke belastingen]]
- [[themafiches/fiscale-procedure-gewest-gemeente|Themafiche — Procedure gewest/gemeente]]
- [[themafiches/registratierechten|Themafiche — Registratierechten]]
- [[themafiches/successierechten-en-erfrecht|Themafiche — Successierechten & erfrecht]]

</div>

---

*Themafiche afgeleid uit cluster regionale-en-lokale-belastingen (PO 2.7). Status: voorgesteld.*
