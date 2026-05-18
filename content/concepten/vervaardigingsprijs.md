---
title: Vervaardigingsprijs
tags:
- concept
- regel
- po-1-8
linked_anchors:
- 1.8.III.A
- 1.8.II.B
programmaonderdelen:
- '1.8'
confidence: grounded
node_type: regel
status: seed
schema_version: '1.5'
gegenereerd_uit: data/concepten/records/vervaardigingsprijs.json
gegenereerd_op: '2026-05-18'
---
# Vervaardigingsprijs ⚖️

> [!summary] Korte inhoud
> De vervaardigingsprijs van producten omvat (a) de aanschaffingsprijs van de gebruikte grondstoffen, verbruiksgoederen en hulpstoffen, (b) de productiekosten die rechtstreeks aan het individuele product kunnen worden toegerekend (directe productiekosten), en (c) het evenredig deel….

> [!info] Behoort tot: [[volledige-kostencalculatie]]

De vervaardigingsprijs van producten omvat (a) de aanschaffingsprijs van de gebruikte grondstoffen, verbruiksgoederen en hulpstoffen, (b) de productiekosten die rechtstreeks aan het individuele product kunnen worden toegerekend (directe productiekosten), en (c) het evenredig deel van de productiekosten die slechts onrechtstreeks aan het individuele product kunnen worden toegerekend (indirecte productiekosten). De opname van (c) is een keuze die in de waarderingsregels wordt vastgelegd: 'full costing' (alle (c) opnemen) of 'direct costing' (enkel het variabele deel of niets opnemen).

_Bron: CBN 132/7 §2.1 jo. CBN 2012/15 jo. KB 21.10.2018 art. 22_


## Bouwstenen

### Drie verplichte bestanddelen ⚖️

(a) Aanschaffingsprijs van het in het product verwerkte materiaal. (b) Directe productiekosten: alles wat met productie te maken heeft en aan dat product toewijsbaar is (directe arbeid, machine-uren rechtstreeks toegerekend). (c) Indirecte productiekosten: het evenredig deel van de gemeenschappelijke productiekosten.

**Waarom?** Wettelijke ondergrens voor voorraadwaardering; mag niet onder de werkelijke (a)+(b) liggen.


_Grondslag: KB 21.10.2018 art. 22 · CBN 132/7 §2.1_

### Full costing vs. direct costing ⚖️

Full costing = alle indirecte productiekosten opnemen in (c). Direct costing = (c) weglaten of beperken tot het variabele deel; vaste indirecte kosten worden direct als periode-last geboekt in de RR.

**Waarom?** Keuze met grote impact op voorraadwaardering, periodieke winst en stuurinformatie. Belastingadministratie aanvaardt direct costing mits consistent toegepast en in waarderingsregels opgenomen.


_Grondslag: CBN 2012/15_

### Niet inbegrepen: commercieel en administratief ⚖️

Algemene administratie-, financiële, commerciële en distributiekosten worden NIET in de vervaardigingsprijs opgenomen — ook niet bij full costing. Enkel productie-gerelateerde overhead telt mee.

**Waarom?** Voorkomt dat de voorraad onterecht opgeblazen wordt met kosten die niet aan het maken-van-het-product gelinkt zijn.


_Grondslag: CBN 132/7 §2.1_


## Berekening

### Vervaardigingsprijs full-costing-berekening

**Vervaardigingsprijs (full costing)** 
```
vervaardigingsprijs = direct materiaal + directe productiekosten + toegerekende indirecte productiekosten
```

| Symbool | Betekenis | Eenheid |
|---|---|---|
| `direct materiaal` | Verbruikt materiaal aan voorraadprijs | EUR |
| `directe productiekosten` | Arbeid en andere rechtstreeks toewijsbare kosten | EUR |
| `toegerekende indirecte productiekosten` | Sleutel-tarief × eenheden van het product | EUR |

**Voorbeeld-invulling**: Yperse partij tapijten: materiaal € 12.000, directe arbeid € 4.500, toegerekend overhead € 3.600

```
€ 12.000 + € 4.500 + € 3.600 = € 20.100
```

_Resultaat in EUR_
*Tel materiaal, directe productiekosten en het toegerekende deel van de indirecte productiekosten op, voor de hoeveelheid effectief geproduceerde eenheden.*

### 1. Tel direct materiaalverbruik

Bereken hoeveel grondstof/halffabrikaat in de productie is opgegaan, gewaardeerd volgens de gekozen voorraadmethode (gewogen gemiddelde, FIFO).

**Waarom?** Eerste verplichte bestanddeel.

**🛠️ Hoe**:

1. Bepaal verbruikte hoeveelheid via beginvoorraad + aankopen − eindvoorraad.
2. Waardeer aan eenheidsprijs volgens voorraadmethode.
3. Tel aanvullende aanschaffingskosten mee (transport, douane) als die aan de aanschaffing toewijsbaar zijn.


**Grondslag**: CBN 132/7 §2.1 · KB 21.10.2018 art. 22

### 2. Tel directe productiekosten

Voeg directe arbeidskost en andere rechtstreeks toewijsbare productiekosten toe.

**Waarom?** Tweede verplichte bestanddeel.

**🛠️ Hoe**:

1. Vermenigvuldig de directe arbeidsuren met het uurtarief inclusief werkgeverslasten.
2. Voeg eventuele rechtstreeks aan order gefactureerde onderaanneming, machine-uren-tarieven, of speciaal gereedschap toe.


**Grondslag**: CBN 132/7 §2.1

### 3. Verdeel indirecte productiekosten

Bereken een verdeelsleutel-tarief per kostencentrum en pas dat toe op de productie-eenheid. Enkel productie-gerelateerde overhead — geen administratie of commercieel.

**Waarom?** Derde bestanddeel; full costing kiest opname.

**🛠️ Hoe**:

1. Verzamel alle indirecte productiekosten per kostencentrum (huur, energie, afschrijving productiemachines, indirect personeel).
2. Bepaal een causale sleutel (directe arbeidsuren, machine-uren).
3. Tarief = totale indirecte productiekost / totale sleutel-eenheden.
4. Vermenigvuldig met de sleutel-eenheden van het concrete product.


> [!example]- Voorbeeld: Yperse Werkplaats BV: weverij heeft € 1.200.000 jaarlijkse indirecte productiekosten en 30.000 directe arbeidsuren
> Yperse Werkplaats BV: weverij heeft € 1.200.000 jaarlijkse indirecte productiekosten en 30.000 directe arbeidsuren. Partij tapijten verbruikt 90 directe arbeidsuren.
>
> 1. **Bereken sleutel-tarief** 🧮
>
>    tarief = € 1.200.000 / 30.000 uur = **€ 40 per directe arbeidsuur**
>
> 2. **Toerekening aan partij** 🧮
>
>    toegerekend overhead partij = 90 uur × € 40 = **€ 3.600**
>
> 3. **Vervaardigingsprijs van de partij** 🧮
>
>    Materiaal (wol)            = € 12.000
>    Directe arbeid (90 u × € 50) = €  4.500
>    Indirect overhead           = €  3.600
>    **Vervaardigingsprijs**     = **€ 20.100**
>

**Grondslag**: CBN 132/7 §2.1


## Valkuilen

> [!warning]- De aanschaffingsprijs van het materiaal is niet de factuurprijs, maar de factuurprijs inclusief aanverwante kosten (transport, niet-aftrekba…
> ⚠️ De aanschaffingsprijs van het materiaal is niet de factuurprijs, maar de factuurprijs inclusief aanverwante kosten (transport, niet-aftrekbare BTW, douane) en na korting. Examen-valkuil: studenten gebruiken de bruto factuurprijs. 🤖


> [!warning]- Direct costing kiezen voor voorraadwaardering is wettelijk toegelaten (mits consistent en gemeld in waarderingsregels), maar leidt tot lager…
> ⚠️ Direct costing kiezen voor voorraadwaardering is wettelijk toegelaten (mits consistent en gemeld in waarderingsregels), maar leidt tot lagere voorraad en lagere periode-winst in groeijaren. De toelichting moet de methodekeuze vermelden. ⚖️
>
> _Bron: CBN 2012/15_


> [!warning]- Bij abnormaal lage productie (onderbenutting van capaciteit) mag de werkgever niet 'extra' overhead op de geproduceerde eenheden gooien om d…
> ⚠️ Bij abnormaal lage productie (onderbenutting van capaciteit) mag de werkgever niet 'extra' overhead op de geproduceerde eenheden gooien om de voorraadwaarde op te krikken — onbenutte capaciteit blijft periode-kost. Internationale norm IAS 2 expliciet; Belgisch niet wetstekstmatig vastgelegd maar gangbare interpretatie. 🤖



## Bronnen

[^1]: `CBN-0132-07-boeking-en-waardering-van-voorraden__sec_vervaardigingsprijs`
[^2]: `CBN-2012-15-bestellingen-in-uitvoering__sec_defini-ring-van-de-vervaardigingprijs-bij-bestellingen-in-ui`
[^3]: `CBN-2012-15-bestellingen-in-uitvoering__sec_waarderingsaspecten-n-a-v-de-toepassing-van-full-costing`
[^4]: `CBN-2012-15-bestellingen-in-uitvoering__sec_waarderingsaspecten-n-a-v-de-toepassing-van-direct-costing`
