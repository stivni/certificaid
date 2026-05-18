---
title: Werkelijke kostencalculatie (vastgestelde kosten)
tags:
- concept
- cluster
- po-1-8
linked_anchors:
- 1.8.III.A
- 1.8.III.B
- 1.8.III.C
programmaonderdelen:
- '1.8'
confidence: inferred
node_type: cluster
status: seed
schema_version: '1.6'
gegenereerd_uit: data/concepten/records/werkelijke-kostencalculatie.json
gegenereerd_op: '2026-05-18'
---
# Werkelijke kostencalculatie (vastgestelde kosten) 🤖

Werkelijke kostencalculatie (synoniem: post-calculatie, vastgestelde kostencalculatie) berekent de kostprijs op basis van de werkelijk geboekte kosten, achteraf bekend uit de boekhouding. Tegenpool van voorbepaalde kostencalculatie (standaardkosten). Vereist een afgesloten boekhoudperiode vóór de kostprijs definitief is.

> [!summary] Korte inhoud
> Werkelijke kostencalculatie (post-calculatie, vastgestelde kostencalculatie) berekent de kostprijs op basis van de werkelijk geboekte kosten — achteraf bekend uit de algemene boekhouding van de afgesloten periode.

> [!info] Behoort tot: [[costing-methodes-vergelijking]]

Werkelijke kostencalculatie (post-calculatie, vastgestelde kostencalculatie) berekent de kostprijs op basis van de werkelijk geboekte kosten — achteraf bekend uit de algemene boekhouding van de afgesloten periode. Tegenpool van voorbepaalde kostencalculatie (standaardkosten, vóóraf bepaald). Werkelijke kostencalculatie kan zowel met full costing als met direct costing gebeuren; het label slaat op de tijdsdimensie (achteraf), niet op de scope.

_Bron: Management accounting — bron-gap_


## Bouwstenen

### Volledige of gedeeltelijke werkelijke kostprijs 🤖

Werkelijke kostencalculatie kan zowel met full costing (volledige werkelijke kost) als met direct costing (alleen variabele werkelijke kost) gebeuren. Het label 'werkelijk' slaat op de tijdsdimensie (achteraf), niet op de scope (volledig vs. gedeeltelijk).

**Waarom?** Verduidelijkt dat 'volledige kostencalculatie' (anchor 1.8.III.A) en 'werkelijke kostencalculatie' twee verschillende assen zijn — geen synoniemen.



Yperse Werkplaats BV berekent na afsluiting 20X1 dat een partij tapijten in werkelijkheid € 21.500 heeft gekost (€ 12.000 wol + € 4.800 directe arbeid + € 4.700 indirect). Een vergelijking met de standaardkostprijs van € 20.000 toont een verschil van € 1.500 ongunstig.



## Berekening

### Werkelijke-kost-berekening achteraf (post-calculatie)

*Stappenschema waarmee na periodeafsluiting de werkelijke kostprijs per kostendrager (product, order) wordt opgebouwd uit de werkelijk geregistreerde kosten in de algemene boekhouding.*

### 1. Wacht op periode-afsluiting

Werkelijke kostencalculatie veronderstelt afgesloten boekjaar of -periode waarin alle facturen, lonen en overhead geregistreerd zijn.

**🛠️ Hoe**:

Eindvoorraad opgenomen, debiteuren/crediteuren bijgewerkt, periodeafsluitingen geboekt (afschrijvingen, vakantiegeld, voorzieningen).

**Grondslag**: CBN 174/1 (regelmatige boekhouding)

### 2. Verzamel werkelijk direct verbruik per order

Materiaalbonnen en uurregistratie per order/product gekoppeld aan werkelijke prijzen (voorraadwaardering volgens gekozen methode, werkelijke uurkosten).

**🛠️ Hoe**:

Uit ERP/productie-systeem: per order materiaalafgifte × FIFO-/gewogen gemiddelde prijs; loonregistratie × werkelijk all-in uurtarief.

**Grondslag**: [[directe-kosten]] · CBN 132/7 §2.1

### 3. Verzamel werkelijke indirecte productiekosten per kostencentrum

Tel alle indirecte productiekosten van het kostencentrum (huur, energie, leiding, onderhoud, afschrijvingen) over de periode.

**🛠️ Hoe**:

Uit grootboek klasse 61-64 gesegmenteerd op kostencentrum; afschrijvingen via boekingen klasse 630.

**Grondslag**: KB 21.10.2018 — MAR klasse 61-64

### 4. Bereken werkelijke sleutel-tarieven en verdeel

Per kostencentrum: werkelijke indirecte kosten / werkelijke sleutel-eenheden (uren, machine-uren) = werkelijk tarief. Toegewezen overhead = werkelijk tarief × verbruikte eenheden per kostendrager.

**🛠️ Hoe**:

Verschil met voorbepaalde aanpak: tarief wordt achteraf herrekend met werkelijke cijfers, niet vooraf begroot. Geen verschillenboekhouding nodig.

**Grondslag**: [[verdeelsleutel]]

### 5. Som werkelijke kostprijs per kostendrager

Tel directe materiaal + directe arbeid + toegerekende werkelijke indirecte productiekosten op per kostendrager. Vergelijk met voorbepaalde kostprijs voor verschillenanalyse (indien beide systemen lopen).

**🛠️ Hoe**:

Output: vervaardigingsprijs werkelijk versus standaard. Gebruik werkelijk voor voorraadwaardering in jaarrekening (CBN 132/7) — tenzij verschillen klein, dan mag standaard ook.

**Grondslag**: CBN 132/7 §2.1


## In de praktijk

<h3 id="voor-de-jaarrekening">Voor de jaarrekening</h3>

> [!tip]- Voor de jaarrekening
> De wettelijke voorraadwaardering vraagt 'werkelijke' vervaardigingsprijs (CBN 132/7). Een onderneming die intern met standaardkosten werkt, moet bij jaarafsluiting de standaardprijs naar werkelijke prijs corrigeren — verschillenboekhouding herleidt eindvoorraad naar werkelijk niveau. ⚖️

<h3 id="tempo-nadeel">Tempo-nadeel</h3>

> [!tip]- Tempo-nadeel
> Werkelijke kostprijs is pas beschikbaar ná periodeafsluiting (week, maand, jaar). Voor snelle sturing tijdens de periode (offertes, korte termijn beslissingen) gebruikt men voorbepaalde kosten. Veel ondernemingen draaien beide systemen parallel. 🤖


> [!info]- Niet verwarren met [[voorbepaalde-kosten]]
> Werkelijke kostencalculatie: cijfers achteraf, traag maar exact. Voorbepaalde: vooraf, snel maar gemiddelde. Voor jaarrekening werkelijk; voor maandsturing voorbepaald.
>
> _Trigger_: Examen: welke kost gebruik je voor balans-voorraadwaarde?


## Bronnen

[^1]: `CBN-0132-07-boeking-en-waardering-van-voorraden__sec_vervaardigingsprijs`
