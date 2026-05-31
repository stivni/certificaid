---
title: "Themafiche — Bewaarplicht"
description: "Themafiche voor sub-cluster bewaarplicht (PO 2.5): 7j WER vs 10j WIB vs 10j WBTW + digitale bewaring + GDPR-interactie"
tags:
  - themafiche
  - po-2.5
  - cluster-fiscale-procedure
---

<div class="no-print">

> ⚠️ **Voorlopig — themafiche-laag wordt uitgefaseerd.** Per **ADR-039** vervangt één PO-samenvatting per programmaonderdeel de cluster-themafiches. Deze fiche blijft beschikbaar tot het relevante PO een leerpad krijgt — dan migreert de inhoud naar `content/leerpaden/<po-slug>/samenvatting.md`. Voor cross-PO themafiches (vergelijkingen tussen verschillende PO's) volgt een aparte beslissing per fiche: incorporeren in alle relevante samenvattingen, óf upgraden naar concept-fiche.

</div>

<div class="no-print">

> **Themafiche — kapstok voor herhaling.** Drie bewaarregimes naast elkaar — langste termijn primeert. Voor verhaal en routekaart: [[leerpaden/2.5|minicursus PO 2.5]].

</div>

---

## Take-away

- **In praktijk = 10 jaar** — langste van WER/WIB/WBTW primeert
- **Boekhoudrecht (WER) = 7 jaar minimum**; fiscale verplichting (10j) trekt door
- **Vorm-vrijheid**: papier OF digitaal toegelaten, mits leesbaarheid + integriteit + authenticiteit gewaarborgd
- **Origineelvereiste** vervalt indien digitalisering met certificering (EDI / e-facturering)
- **GDPR-spanning**: persoonsgegevens > bewaartermijn moeten geanonimiseerd/gewist (data-minimalisatie)
- **Termijn begint anders per documenttype** — boekjaar-einde voor jaarrekening, datum verrichting voor facturen

---

## Drie bewaarregimes naast elkaar

| Wet | Termijn | Wat? | Vertrekpunt termijn |
|---|---|---|---|
| **WER Boek III (boekhoudrecht)** | 7 jaar | Boeken (algemeen + hulp) · jaarrekening · verantwoordingsstukken | 1 januari volgend op boekjaar-einde |
| **WIB92 art. 315** | 10 jaar | Boeken + stukken nodig voor bepaling inkomstenbelasting | 1 januari volgend op AJ |
| **W.BTW art. 60** | 10 jaar | Facturen · BTW-aangiftes · IC-opgaves · BTW-boeken · jaaroverzichten | Datum opmaak document of laatste actie |

**Vuistregel**: voor élk fiscaal-relevant stuk → 10 jaar.

---

## Wat moet bewaard? Per documenttype

| Documenttype | WER | WIB | W.BTW | In praktijk |
|---|---|---|---|---|
| **Jaarrekening + dagboeken** | 7 j | 10 j | n.v.t. | 10 j |
| **Verantwoordingsstukken (contracten, facturen, bankafschriften)** | 7 j | 10 j | 10 j | 10 j |
| **Facturen ontvangen + verstuurd** | 7 j | 10 j | 10 j | 10 j |
| **Klantenlisting + IC-opgave** | n.v.t. | n.v.t. | 10 j | 10 j |
| **Loonadministratie** | 5 j (CAO 8 BIS) | 10 j | 10 j | 10 j |
| **Personeelsdossier** | 5 j na uitdiensttreding (sociaal recht) | n.v.t. | n.v.t. | 5 j na uittreding |
| **Bedrijfsmiddelen + investeringen** | 7 j | 10 j (+ herzieningstermijn BTW 5/15j) | 5 j roerend / 15 j onroerend | 15 j onroerend |

⚠️ Bedrijfsmiddel onroerend: bewaar tot **einde 15j herzieningstermijn** ná einde herzieningsperiode — anders herziening onbewijsbaar.

---

## Vorm-vereisten

| Vereiste | Papier | Digitaal | Toelichting |
|---|---|---|---|
| **Leesbaarheid** | Ja | Ja | Document leesbaar gedurende hele bewaarperiode |
| **Integriteit** | Originele staat | Hash/checksum-bewijs | Geen wijziging na opmaak |
| **Authenticiteit** | Handgeschreven / origineel | Digitale handtekening / EDI-protocol | Bewijs dat afkomstig is van benoemde partij |
| **Origineel** | Verplicht (papier) | Niet meer vereist mits EDI / e-facturering | KB nr. 1 art. 13 + EU 2010/45 |
| **Toegankelijkheid** | Op eerste verzoek fiscus | Idem + leesbaar op fiscus-systemen | "Binnen redelijke termijn" |

---

## Digitalisering — voorwaarden

| Methode | Voorwaarde | Toelating |
|---|---|---|
| **Inscannen papier (na 2014)** | Geadviseerde procedure FOD; checksum + onveranderlijke opslag | Papier mag vernietigd worden na conversie + bewaarbevestiging |
| **E-facturering EDI** | Akkoord beide partijen + integriteit + authenticiteit | Volwaardig elektronisch origineel |
| **PEPPOL (vanaf 1 jan 2026)** | Verplichte e-facturering B2B in BE | Standaard-protocol; verplicht inkomende + uitgaande |
| **Cloud-bewaring** | Toegankelijk + integriteit + recovery | Toegestaan mits FOD-toegang gegarandeerd |

⚠️ Bij digitalisering papier: **conversie-bewijs** bewaren (datum + verantwoordelijke + checksum). Anders riskeert fiscus de stukken te weigeren.

---

## GDPR-interactie — bewaartermijn vs data-minimalisatie

| Spanning | Oplossing |
|---|---|
| **Persoonsgegevens in boekhouding moeten 10 j bewaard** | Bewaarplicht primeert (juridische verplichting GDPR art. 6(1)(c)) |
| **Klantgegevens marketing < 10 j** | Marketing-doel kortere bewaring; boekhoud-doel 10 j → splitsing per doel |
| **Personeelsdossier na uitdiensttreding** | Loon-deel 10 j (fiscaal); rest 5 j (sociaal); recruitment-data ≤ 1 j |
| **Recht op vergetelheid** | Niet absoluut wanneer juridische verplichting bewaring bestaat |
| **Wat na 10 j?** | Anonimisering of vernietiging; bewaar-rationale doc |

---

## Sanctie bij niet-naleving

| Inbreuk | Sanctie |
|---|---|
| **Geen of onvolledige boekhouding** | Ambtshalve aanslag (omkering bewijslast) + boete BTW (1250 EUR per inbreuk) |
| **Vernietigde stukken vóór termijn-einde** | Idem + mogelijke fraudevermoeden |
| **Weigering inzage tijdens controle** | Boete WIB92 (50-1250 EUR) + ambtshalve aanslag |
| **Onleesbare digitale bewaring** | Behandeld als ontbrekende stukken |

---

## ⚠️ Valkuilen

| Valkuil | Wat klopt er niet | Wat klopt wél |
|---|---|---|
| 7 jaar WER volstaat | Boekhoudrecht-termijn als algemene regel | Langste primeert: 10 jaar WIB + BTW. Praktijk = 10 jaar voor alles |
| Termijn vanaf datum document | Factuur 2020 = vernietigen 2030 | Termijn vanaf 1 januari volgend op boekjaar / AJ — factuur 2020 → bewaren tot eind 2030 (WIB) of langer (BTW) |
| Papier vernietigen na scan = OK altijd | Inscannen + papier weg | Vereist conversie-bewijs + checksum; zonder bewijs riskeert fiscus weigering |
| Bedrijfsmiddel onroerend 10 jaar | Bewaartermijn algemeen | 15j BTW-herzieningstermijn vereist bewaring tot einde herzieningsperiode |
| GDPR overruled bewaarplicht | Vergetelheids-recht wist alles | Juridische verplichting bewaring (GDPR art. 6(1)(c)) primeert binnen bewaartermijn |
| E-facturen niet "echt" | Papier blijft origineel | E-factuur via EDI / PEPPOL = volwaardig origineel; geen papier vereist |

---

<div class="no-print">

## Doorklik — losse concept-fiches

**Bewaarplicht-grondslagen**
- [[boekhoudplicht]] — WER-kader
- [[boekhouding]] — algemene plicht + opzet
- [[fiscale-controle]] — bevoegdheden + inzage

**BTW-specifieke bewaring**
- [[factuur-btw]] — factuurvereisten + bewaring
- [[btw-aftrek]] — herziening 5/15j bedrijfsmiddel

**Verwante themafiches**
- [[themafiches/fiscale-termijnen|Themafiche — Fiscale termijnen]]
- [[themafiches/taxatieprocedure|Themafiche — Taxatieprocedure]]

</div>

---

*Themafiche afgeleid uit cluster fiscale-procedure (PO 2.5). Status: voorgesteld.*
