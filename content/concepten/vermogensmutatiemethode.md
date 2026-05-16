---
title: Vermogensmutatiemethode (equity method)
tags:
- concept
- methode
- po-1-4
linked_anchors:
- 1.4.I.E
- 1.4.I.D
- 1.4.I.G
- 1.4.II.C
- 1.4.taak.1
programmaonderdelen:
- '1.4'
confidence: grounded
node_type: methode
status: seed
schema_version: '1.4'
gegenereerd_uit: data/concepten/records/vermogensmutatiemethode.json
gegenereerd_op: '2026-05-16'
---
# Vermogensmutatiemethode (equity method) ⚖️

> [!summary] Korte inhoud
> Een deelneming verschijnt in de geconsolideerde jaarrekening niet activum-per-activum, maar als één samengevatte balanspost.

> [!info] Behoort tot: [[consolidatiemethodes-vergelijking]]

Een deelneming verschijnt in de geconsolideerde jaarrekening niet activum-per-activum, maar als één samengevatte balanspost. Bij de eerste opname waardeer je die post aan jouw pro-rata aandeel in het eigen vermogen van de andere onderneming op de datum van aankoop. Daarna pas je die boekwaarde elk boekjaar aan met jouw aandeel in het resultaat en in directe wijzigingen van het eigen vermogen. Je gebruikt deze methode voor (a) geassocieerde ondernemingen (invloed van betekenis, geen controle), (b) gemeenschappelijke dochters waarvan de activiteit niet nauw geïntegreerd is in die van de moeder, en (c) dochters die uit de consolidatie zijn gelaten op grond van KB WVV art. 3:98 of art. 3:99.

_Bron: KB WVV art. 3:142 jo. art. 3:141 — 3:145_


## Bouwstenen

### Eerste consolidatie — vervang aankoopwaarde door pro-rata EV ⚖️

Bij eerste opname vervang je de aankoopwaarde van de deelneming door jouw pro-rata aandeel in het eigen vermogen van de andere vennootschap (inclusief resultaat van het boekjaar). Een eventueel verschil reken je toe aan onder- of overgewaardeerde bezittingen of schulden; het residu boek je als 'Consolidatieverschillen' (positief of negatief) en je schrijft het positieve verschil af.

**Waarom?** Op de enkelvoudige balans van de moeder staat de deelneming aan historische kostprijs — een 'dood' getal. De vermogensmutatie maakt de deelneming levend door haar aan jouw effectieve aandeel in EV te koppelen, zodat de geconsolideerde jaarrekening een eerlijker beeld geeft.

**Voorbeeld**: Antwerpse Investments NV koopt 25 % van Drukkerij Dendermonde BV voor € 350.000; EV Drukkerij = € 1.250.000 → vervang € 350.000 (aankoopwaarde) door 25 % × € 1.250.000 = € 312.500 + € 37.500 consolidatieverschil. Boekwaarde 'Vennootschappen waarop vermogensmutatie is toegepast' = € 312.500; positief consolidatieverschil € 37.500 wordt apart bijgehouden en afgeschreven.

_Grondslag: CBN 2022/11 — Eerste consolidatie_

### Latere consolidaties — beweeg mee met EV-wijzigingen ⚖️

Elk volgend boekjaar pas je de boekwaarde van de deelneming aan met jouw pro-rata aandeel in: (a) het resultaat van de andere vennootschap, exclusief het deel dat als dividend wordt uitgekeerd (dat dividend boek je apart als financiële opbrengst); (b) directe wijzigingen binnen het eigen vermogen (herwaarderingsmeerwaarde, kapitaalsubsidie, omrekeningsverschillen).

**Waarom?** De deelneming-post moet meebewegen met wat economisch gebeurt in de andere vennootschap. Anders blijft de balanspost statisch en verdwijnt het didactische voordeel van de methode.

**Voorbeeld**: Drukkerij Dendermonde BV maakt in jaar 1 winst van € 200.000, keert geen dividend uit → Antwerpse boekt 25 % × € 200.000 = € 50.000 als 'Aandeel in het resultaat van vennootschappen waarop vermogensmutatie is toegepast'; 'Vennootschappen waarop vermogensmutatie is toegepast' stijgt met € 50.000 (€ 312.500 → € 362.500).

_Grondslag: KB WVV art. 3:143_

### Presentatie op de balans — één lijn ⚖️

De deelneming verschijnt in de geconsolideerde balans onder een afzonderlijke post van de financiële vaste activa met naam 'Vennootschappen waarop vermogensmutatie is toegepast'.

**Waarom?** Door één duidelijk gelabelde lijn weet de lezer dat het hier niet om een gewone deelneming gaat maar om een geassocieerde of niet-geïntegreerde gemeenschappelijke dochter — andere economische realiteit dan een 100 %-dochter.

**Voorbeeld**: Op de geconsolideerde balans van Antwerpse Investments NV staat 'Vennootschappen waarop vermogensmutatie is toegepast' 175 (voor Drukkerij Dendermonde) als aparte post bij de financiële vaste activa.

_Grondslag: KB WVV art. 3:141_

### Presentatie op de resultatenrekening — afzonderlijke post ⚖️

Jouw aandeel in het resultaat van de andere vennootschap komt in de geconsolideerde resultatenrekening als afzonderlijke post 'Aandeel in het resultaat van de vennootschappen waarop vermogensmutatie is toegepast'.

**Waarom?** Zo blijft het zichtbaar dat dit resultaat niet uit de eigen activiteit komt maar uit jouw aandeel in een andere vennootschap — anders zou het vermengd raken met de gewone bedrijfsresultaten en het beeld vertroebelen.

**Voorbeeld**: Aandeel Antwerpse Investments NV in het resultaat van Drukkerij Dendermonde BV in jaar 1: 25 → afzonderlijke regel op de geconsolideerde resultatenrekening (positief).

_Grondslag: KB WVV art. 3:145_


## Berekening

### Eerste consolidatie — herwaardering en consolidatieverschil

**Pro-rata aandeel in eigen vermogen (eerste consolidatie)** 
```
pro-rata aandeel EV = belangenpercentage × eigen vermogen geassocieerde op aankoopdatum
```

| Symbool | Betekenis | Eenheid |
|---|---|---|
| `belangenpercentage` | Aandeel van moeder in kapitaal geassocieerde (zie [[belangenpercentage]]) | % |
| `eigen vermogen geassocieerde op aankoopdatum` | Kapitaal + reserves + overgedragen resultaat + resultaat tot aankoopdatum | EUR |

**Voorbeeld-invulling**: belang Antwerpse Investments NV in Drukkerij Dendermonde BV = 25 %; EV Drukkerij = € 1.250.000

```
25 % × € 1.250.000 = € 312.500
```

_Resultaat in EUR_
**Consolidatieverschil (eerste consolidatie vermogensmutatie)** (volgt op: eerste-consolidatie-vm-pro-rata-ev)
```
consolidatieverschil = aankoopwaarde − pro-rata aandeel EV − toerekening aan stille meer-/minderwaarden
```

| Symbool | Betekenis | Eenheid |
|---|---|---|
| `aankoopwaarde` | Wat de moeder betaalde voor de aandelen | EUR |
| `pro-rata aandeel EV` | Resultaat van vorige formule | EUR |
| `toerekening aan stille meer-/minderwaarden` | Som van bedragen toegerekend aan onder-/overgewaardeerde posten van de geassocieerde | EUR |

**Voorbeeld-invulling**: aankoopwaarde = € 350.000; pro-rata aandeel EV = € 312.500; toerekening = € 0

```
€ 350.000 − € 312.500 − € 0 = € 37.500 (positief)
```

_Resultaat in EUR_
*Bij verwerving betaalt de moeder vaak een prijs die afwijkt van haar pro-rata aandeel in het netto-actief van de geassocieerde. Dat verschil reken je eerst toe aan onder- of overgewaardeerde posten van de geassocieerde; pas daarna boek je het residu als 'Consolidatieverschil'.*

### 1. Noteer de aankoopwaarde van de deelneming

Schrijf op wat de moeder effectief betaalde voor de aandelen in de geassocieerde of niet-geïntegreerde gemeenschappelijke dochter, inclusief eventueel geactiveerde aankoopkosten.

**Waarom?** Dit is je vertrekpunt: een fout cijfer hier vervalst het hele rekenwerk.

**📥 Input**:
- Aandelenkoopovereenkomst → **Prijs + bijkomende kosten** _(boekhoudkundig-bedrag)_

**📤 Output**:
- Werkblad vermogensmutatie → **Aanschaffingswaarde** _(boekhoudkundig-bedrag)_

**🛠️ Hoe**:

1. Open de aandelenkoopovereenkomst tussen Antwerpse Investments NV en Drukkerij Dendermonde BV.
2. Noteer de prijs voor 25 % van de aandelen: € 350.000.
3. Voeg eventuele aankoopkosten toe die volgens de waarderingsregels in de aanschaffingswaarde mogen.


**Grondslag**: KB WVV art. 3:142, § 1

### 2. Bereken jouw pro-rata aandeel in EV op aankoopdatum

Vermenigvuldig jouw belangenpercentage met het totaal eigen vermogen van de geassocieerde op de datum van aankoop (kapitaal + reserves + overgedragen resultaat + resultaat van het boekjaar tot die datum).

**Waarom?** Dit is de eerste 'echte' waarde van de deelneming volgens de vermogensmutatiemethode. Het verschil met de aankoopwaarde zal het consolidatieverschil opleveren.

**📥 Input**:
- Balans geassocieerde op aankoopdatum → **Eigen vermogen totaal** _(boekhoudkundig-bedrag)_
- Aandelenkoopovereenkomst → **Belangenpercentage** _(percentage)_

**📤 Output**:
- Werkblad vermogensmutatie → **Pro-rata EV** _(boekhoudkundig-bedrag)_

**🛠️ Hoe**:

1. Open de balans van Drukkerij Dendermonde BV op de aankoopdatum.
2. Tel kapitaal + reserves + overgedragen resultaat + resultaat tot die datum → eigen vermogen totaal (bv. € 1.250.000).
3. Vermenigvuldig met het belangenpercentage van Antwerpse: 25 % × € 1.250.000 = € 312.500.


**Grondslag**: KB WVV art. 3:142, § 1

### 3. Bereken het bruto-verschil

Trek het pro-rata EV (stap 2) af van de aankoopwaarde (stap 1).

**Waarom?** Het bruto-verschil is de tussenstap voor de toerekening; het is nog niet het uiteindelijke consolidatieverschil.

**📥 Input**:
- Werkblad vermogensmutatie → **Aanschaffingswaarde** _(boekhoudkundig-bedrag)_
- Werkblad vermogensmutatie → **Pro-rata EV** _(boekhoudkundig-bedrag)_

**📤 Output**:
- Werkblad vermogensmutatie → **Bruto-verschil** _(boekhoudkundig-bedrag)_

**🛠️ Hoe**:

1. Aanschaffingswaarde: € 350.000.
2. Pro-rata EV: € 312.500.
3. Bruto-verschil = € 350.000 − € 312.500 = € 37.500. Positief → mogelijk goodwill.


**Grondslag**: Synthese KB WVV art. 3:142 jo. art. 3:128

### 4. Reken het verschil toe aan stille meer-/minderwaarden

Reken het bruto-verschil zoveel mogelijk toe aan bezittingen of schulden van de geassocieerde waarvan de werkelijke waarde afwijkt van de boekwaarde (KB WVV art. 3:128).

**Waarom?** Zoals bij integrale consolidatie: de premie kan voor een deel reflecteren dat bepaalde posten ondergewaardeerd zijn. Door eerst die meer-/minderwaarden te erkennen verklein je het residu dat als goodwill (badwill) overblijft.

**📥 Input**:
- Werkblad vermogensmutatie → **Bruto-verschil** _(boekhoudkundig-bedrag)_
- Balans geassocieerde → **Posten met afwijkende werkelijke waarde** _(boekhoudkundig-bedrag)_

**📤 Output**:
- Werkblad vermogensmutatie → **Residu na toerekening** _(boekhoudkundig-bedrag)_

**🛠️ Hoe**:

1. Identificeer bij Drukkerij Dendermonde BV bezittingen of schulden waarvan de werkelijke waarde afwijkt.
2. Reken het bruto-verschil zoveel mogelijk daaraan toe; daarmee verlaag je het residu.
3. In dit cijfervoorbeeld: geen onder- of overwaarderingen geïdentificeerd → volledige bruto-verschil € 37.500 wordt residu.


**Grondslag**: KB WVV art. 3:128

### 5. Boek het residu als consolidatieverschil + start afschrijving

Het residu na stap 4 boek je als positief of negatief consolidatieverschil. Positief → afzonderlijk bijgehouden naast 'Vennootschappen waarop vermogensmutatie is toegepast', afgeschreven over de vermoedelijke gebruiksduur (>5 jaar: motivering in toelichting).

**Waarom?** Het residu vertegenwoordigt goodwill (of badwill) op de geassocieerde. Anders dan bij integrale consolidatie wordt het apart bijgehouden, niet vermengd met de hoofdpost van de deelneming.

**📥 Input**:
- Werkblad vermogensmutatie → **Residu na toerekening** _(boekhoudkundig-bedrag)_

**📤 Output**:
- Geconsolideerde balans → **Vennootschappen waarop vermogensmutatie is toegepast (= pro-rata EV)** _(nieuwe-balanspost)_
- Geconsolideerde balans → **Positief/negatief consolidatieverschil** _(nieuwe-balanspost)_

**🛠️ Hoe**:

1. Residu uit stap 4: € 37.500 (positief).
2. Boekingen: 'Vennootschappen waarop vermogensmutatie is toegepast' = € 312.500 (pro-rata EV); 'Positief consolidatieverschil' = € 37.500; tegenpost: 'Deelnemingen' op −€ 350.000 (de oorspronkelijke post wordt vervangen).
3. Som van de twee balansposten = € 312.500 + € 37.500 = € 350.000 = de aankoopwaarde.
4. Afschrijfplan voor het positief consolidatieverschil: bv. 5 jaar → € 37.500 / 5 = € 7.500 per jaar.


> [!example]- Voorbeeld: Antwerpse Investments NV koopt in 20X1 een belang van 25 % in Drukkerij Dendermonde BV voor € 350.000
> Antwerpse Investments NV koopt in 20X1 een belang van 25 % in Drukkerij Dendermonde BV voor € 350.000. EV Drukkerij op aankoopdatum: € 1.250.000; geen onder-/overwaarderingen.
>
> 1. **Werkblad eerste consolidatie** 🧮
>
>    | Stap                                          | Bedrag (€) |
>    |-----------------------------------------------|-----------:|
>    | (1) Aankoopwaarde                             |    350.000 |
>    | (2) Pro-rata EV (25 % × € 1.250.000)          |    312.500 |
>    | (3) Bruto-verschil                            |     37.500 |
>    | (4) Toerekening aan stille meerwaarden        |          0 |
>    | (5) **Residu = consolidatieverschil**         | **37.500** |
>
> 2. **Boeking eerste consolidatie** 📝
>
>    Schrap: Deelneming Drukkerij Dendermonde −€ 350.000
>    Nieuw: Vennootschappen waarop vermogensmutatie is toegepast +€ 312.500
>    Nieuw: Positief consolidatieverschil +€ 37.500
>    Saldo: € 312.500 + € 37.500 = € 350.000 (= aankoopwaarde, ongewijzigd op balansniveau)
>
> 3. **Afschrijvingsplan consolidatieverschil** 🧮
>
>    Vermoedelijke gebruiksduur: 5 jaar
>    Jaarlijkse afschrijving = € 37.500 / 5 = **€ 7.500**
>    Geboekt in afzonderlijke post van bedrijfs- of financiële kosten in de geconsolideerde resultatenrekening (RR).
>

**Grondslag**: KB WVV art. 3:130 jo. art. 3:131

**Voorbeeld**: Antwerpse Investments NV koopt in 20X1 een belang van 25 % in Drukkerij Dendermonde BV. Aankoopwaarde € 350.000. Eigen vermogen Drukkerij op aankoopdatum: € 1.250.000.

```
Pro-rata aandeel in EV op aankoopdatum = 25 % × € 1.250.000 = € 312.500.
Verschil = € 350.000 − € 312.500 = € 37.500 (positief).
Geen onder-/overwaarderingen aangewezen → het volledige verschil van € 37.500 wordt geboekt als positief consolidatieverschil.
Boeking: 'Vennootschappen waarop vermogensmutatie is toegepast' (balans) +€ 312.500; 'Positief consolidatieverschil' (balans) +€ 37.500; tegenpost: 'Deelnemingen' −€ 350.000.
```

Resultaat: Eerste consolidatie: deelneming wordt voorgesteld als 'Vennootschappen waarop vermogensmutatie is toegepast' voor € 312.500 + 'Positief consolidatieverschil' € 37.500 — som € 350.000 (gelijk aan aankoopwaarde). Positief consolidatieverschil wordt afgeschreven over bv. 5 jaar = € 7.500 per jaar in de geconsolideerde resultatenrekening (afzonderlijke post bij bedrijfs- of financiële kosten — KB WVV art. 3:131).
### Latere consolidatie — pro-rata aandeel in resultaat

**Pro-rata aandeel in resultaat (latere consolidatie)** 
```
Δ boekwaarde = belangenpercentage × (resultaat boekjaar − uitgekeerd dividend) + belangenpercentage × directe EV-mutaties
```

| Symbool | Betekenis | Eenheid |
|---|---|---|
| `belangenpercentage` | Aandeel van moeder in kapitaal geassocieerde | % |
| `resultaat boekjaar` | Winst of verlies van de geassocieerde in het lopende boekjaar | EUR |
| `uitgekeerd dividend` | Deel van het resultaat dat door de geassocieerde als dividend wordt uitgekeerd (wordt apart geboekt als financiële opbrengst) | EUR |
| `directe EV-mutaties` | Wijzigingen in eigen vermogen buiten het resultaat om (herwaarderingsmeerwaarde, kapitaalsubsidie, omrekeningsverschillen) | EUR |

**Voorbeeld-invulling**: belang Antwerpse = 25 %; resultaat Drukkerij = € 1.500.000; geen dividend; geen directe EV-mutaties

```
25 % × (€ 1.500.000 − € 0) + 25 % × € 0 = € 375.000
```

_Resultaat in EUR_
**Verliesgrens bij vermogensmutatie** 
```
doorgeboekt verlies = min(belangenpercentage × verlies geassocieerde, huidige boekwaarde deelneming)
```

| Symbool | Betekenis | Eenheid |
|---|---|---|
| `belangenpercentage × verlies geassocieerde` | Pro-rata aandeel in het verlies | EUR |
| `huidige boekwaarde deelneming` | Boekwaarde 'Vennootschappen waarop vermogensmutatie is toegepast' vóór deze verlies-verwerking | EUR |

**Voorbeeld-invulling**: verlies Drukkerij = 7.000; belang Antwerpse = 25 %; huidige boekwaarde = 150

```
min(25 % × 7.000 = 1.750; 150) = 150
```

_Resultaat in EUR_
*Het pro-rata aandeel in winst of verlies van de geassocieerde verandert direct de boekwaarde van de deelneming op de geconsolideerde balans, met een tegenpost als afzonderlijke regel 'Aandeel in het resultaat van vennootschappen waarop vermogensmutatie is toegepast' in de geconsolideerde resultatenrekening.*

### 1. Identificeer het resultaat van de geassocieerde voor het boekjaar

Neem de winst (of verlies) van de geassocieerde over het lopende boekjaar.

**Waarom?** Dit is de basis voor jouw pro-rata aandeel — een fout cijfer hier propageert door alle vervolgstappen.

**📥 Input**:
- Jaarrekening geassocieerde → **Resultaat van het boekjaar** _(boekhoudkundig-bedrag)_

**📤 Output**:
- Werkblad latere consolidatie → **Resultaat geassocieerde** _(boekhoudkundig-bedrag)_

**🛠️ Hoe**:

1. Open de jaarrekening van Drukkerij Dendermonde BV voor het boekjaar.
2. Noteer het resultaat (winst of verlies) over het boekjaar: bv. winst 1.500.
3. Let op: gebruik enkel het resultaat dat in het boekjaar is gerealiseerd, niet het cumulatieve overgedragen resultaat.


**Grondslag**: KB WVV art. 3:143

### 2. Bereken jouw pro-rata aandeel in dit resultaat

Vermenigvuldig het resultaat van de geassocieerde met jouw belangenpercentage. Sluit het deel uit dat als dividend wordt uitgekeerd; dat boek je apart.

**Waarom?** Anders zou je het dividend twee keer tellen — eenmaal via het pro-rata resultaat en eenmaal als financiële opbrengst bij de moeder.

**📥 Input**:
- Werkblad latere consolidatie → **Resultaat geassocieerde** _(boekhoudkundig-bedrag)_
- Aandeelhoudersstructuur → **Belangenpercentage moeder** _(percentage)_

**📤 Output**:
- Werkblad latere consolidatie → **Pro-rata resultaat-aandeel** _(boekhoudkundig-bedrag)_

**🛠️ Hoe**:

1. Resultaat Drukkerij in jaar 1: 1.500.
2. Belangenpercentage Antwerpse: 25 %.
3. Pro-rata resultaat-aandeel = 25 % × 1.500 = 375.
4. Als Drukkerij geen dividend uitkeert: alles via pro-rata. Anders: trek jouw deel van het dividend uit het pro-rata resultaat en boek het apart als financiële opbrengst.


**Grondslag**: KB WVV art. 3:143

### 3. Pas de balanswaarde van de deelneming aan

Verhoog (bij winst) of verlaag (bij verlies) de balanspost 'Vennootschappen waarop vermogensmutatie is toegepast' met jouw pro-rata aandeel.

**Waarom?** De methode bestaat juist daaruit dat de boekwaarde van de deelneming meebeweegt met het eigen vermogen van de geassocieerde — niet langer stuck op aankoopwaarde.

**📥 Input**:
- Werkblad latere consolidatie → **Pro-rata resultaat-aandeel** _(boekhoudkundig-bedrag)_
- Geconsolideerde balans (vorige jaar) → **Vennootschappen waarop vermogensmutatie is toegepast** _(boekhoudkundig-bedrag)_

**📤 Output**:
- Geconsolideerde balans → **Vennootschappen waarop vermogensmutatie is toegepast (geüpdatet)** _(nieuwe-balanspost)_

**🛠️ Hoe**:

1. Open de geconsolideerde balans van Antwerpse Investments NV — start-saldo 'Vennootschappen waarop vermogensmutatie is toegepast' (Drukkerij Dendermonde) = 150.
2. Verhoog met pro-rata winst van 375 (bij Hypothese 1) → nieuwe boekwaarde = 525.
3. Verlaag met pro-rata verlies bij verlies-scenario.
4. Belangrijke limiet: de boekwaarde kan niet onder nul gaan; verliezen boven die grens worden niet doorgeboekt zolang er geen aanvullende verplichting is.


**Grondslag**: KB WVV art. 3:143

### 4. Boek de tegenpost in de resultatenrekening

De tegenpost van de balansaanpassing komt in de geconsolideerde resultatenrekening als afzonderlijke post 'Aandeel in het resultaat van vennootschappen waarop vermogensmutatie is toegepast' — positief bij winst, negatief bij verlies.

**Waarom?** Deze afzonderlijke post houdt het resultaat uit vermogensmutatie zichtbaar gescheiden van het eigen bedrijfsresultaat van de groep.

**📥 Input**:
- Werkblad latere consolidatie → **Pro-rata resultaat-aandeel** _(boekhoudkundig-bedrag)_

**📤 Output**:
- Geconsolideerde resultatenrekening → **Aandeel in het resultaat van vennootschappen waarop vermogensmutatie is toegepast** _(nieuwe-balanspost)_

**🛠️ Hoe**:

1. Open de geconsolideerde resultatenrekening van Antwerpse.
2. Voeg een afzonderlijke regel toe: 'Aandeel in het resultaat van vennootschappen waarop vermogensmutatie is toegepast' = 375 (bij Hypothese 1).
3. Bij verlies: dezelfde regel, met negatief teken.


**Grondslag**: KB WVV art. 3:145

### 5. Behandel dividend apart (om dubbeltelling te vermijden)

Als de geassocieerde dividend uitkeert: het dividend wordt apart geboekt als financiële opbrengst bij de moeder, maar het deel van het resultaat dat als dividend werd toegekend mag niet ook nog via pro-rata bij de deelneming-waarde worden gerekend.

**Waarom?** Anders zou je hetzelfde stuk EV-stijging twee keer erkennen: via stijging boekwaarde én via dividend-inkomst. De vermogensmutatie corrigeert daarvoor.

**📥 Input**:
- Notulen AV geassocieerde → **Bestemming resultaat — dividend uitgekeerd** _(boekhoudkundig-bedrag)_
- Werkblad latere consolidatie → **Pro-rata resultaat** _(boekhoudkundig-bedrag)_

**📤 Output**:
- Geconsolideerde balans + resultatenrekening → **Correctie dividend-deel** _(geëlimineerde-post)_

**🛠️ Hoe**:

1. Bekijk of er dividend werd uitgekeerd door Drukkerij in dit boekjaar.
2. Bereken jouw deel: belangenpercentage × dividend.
3. Boek dat deel als financiële opbrengst bij Antwerpse (al via gewone enkelvoudige boekhouding).
4. Trek het pro-rata-dividend af van het pro-rata-resultaat zodat de boekwaarde van de deelneming alleen het ingehouden deel van het resultaat reflecteert.


**Grondslag**: KB WVV art. 3:143

**Voorbeeld**: Geassocieerde Drukkerij Dendermonde BV; belang van Antwerpse Investments NV = 25 %. Boekwaarde deelneming bij eerste consolidatie was € 312.500 + € 37.500 consolidatieverschil = totaal € 350.000. Hypothese 1: Drukkerij maakt in 20X2 winst van € 1.500.000. Hypothese 2: Drukkerij maakt verlies van € 1.500.000. Hypothese 3: Drukkerij maakt verlies van € 7.000.000 (groter dan boekwaarde € 312.500).

```
Hypothese 1: 25 % × € 1.500.000 = +€ 375.000 — verhoging boekwaarde 'Vennootschappen waarop vermogensmutatie is toegepast' (€ 312.500 → € 687.500) + opname 'Aandeel in het resultaat van vennootschappen waarop vermogensmutatie is toegepast' = € 375.000.
Hypothese 2: 25 % × (−€ 1.500.000) = −€ 375.000 — verlaging boekwaarde (€ 312.500 → niet onder € 0, dus reductie tot € 0 met € 312.500) + 'Aandeel in het verlies …' van −€ 312.500 (beperkt). De rest € 62.500 wordt niet doorgeboekt tenzij er een aanvullende verplichting is.
Hypothese 3: 25 % × (−€ 7.000.000) = −€ 1.750.000 — boekwaarde gaat naar € 0 (was € 312.500); verlies in resultatenrekening € 312.500 (niet € 1.750.000). Resterend € 1.437.500 niet doorgeboekt.
```

Resultaat: Hypothese 1: boekwaarde +€ 375.000 → € 687.500; resultaat verbetert met € 375.000. Hypothese 2 & 3: boekwaarde wordt afgeboekt tot nul; aandeel in verlies in resultatenrekening beperkt tot € 312.500 (oorspronkelijke boekwaarde) — overige verlies wordt niet doorgeboekt zolang geen verplichting bestaat (CBN 2022/11, hypothese 3).

## In de praktijk

<h3 id="eliminatie-van-intra-groepswinsten">Eliminatie van intra-groepswinsten</h3>

> [!tip]- Eliminatie van intra-groepswinsten
> Resultaten van verrichtingen tussen de moeder (of haar dochters) en de vennootschap waarop vermogensmutatie wordt toegepast, die nog in de waardering van een actief zitten, worden uit het 'Aandeel in het resultaat van vennootschappen waarop vermogensmutatie is toegepast' geweerd voor het pro-rata aandeel — zowel bij upstream als downstream sales. ⚖️

<h3 id="geen-vrijstelling-van-consolidatie">Geen vrijstelling van consolidatie</h3>

> [!tip]- Geen vrijstelling van consolidatie
> Het opnemen van een vennootschap via de vermogensmutatiemethode (in plaats van integraal of evenredig) geeft de groep géén vrijstelling van haar consolidatieplicht. De moeder blijft consolidatieplichtig zolang ze een dochter heeft. ⚖️

<h3 id="verkoop-van-de-deelneming">Verkoop van de deelneming</h3>

> [!tip]- Verkoop van de deelneming
> Bij verkoop boek je het verschil tussen verkoopprijs en boekwaarde (op vermogensmutatie-basis, inclusief mutaties tot verkoopdatum) als meer- of minderwaarde in de geconsolideerde resultatenrekening. Een resterend positief consolidatieverschil wordt mee afgeboekt. ⚖️


## Voorwaarden / uitzonderingen

- Geassocieerde onderneming: een deelneming waar je invloed van betekenis hebt, maar geen controle (WVV art. 1:22). Weerlegbaar vermoeden vanaf 20 % stemrechten. ⚖️
- Gemeenschappelijke dochter waarvan de activiteit niet nauw geïntegreerd is in die van de moeder — bij ontbrekende integratie kies je vermogensmutatie in plaats van evenredige consolidatie. ⚖️
- Dochter met enkel controle in feite die het getrouwe beeld zou verstoren bij integrale opname (KB WVV art. 3:98), of dochter waarvan de going-concern niet meer overeind staat (KB WVV art. 3:99) — wordt via vermogensmutatie opgenomen na uitsluiting uit de kring (KB WVV art. 3:100). ⚖️
> [!info]- Niet verwarren met [[integrale-consolidatie]]
> Vermogensmutatie behoudt de deelneming als één balanspost; integrale consolidatie neemt de bezittingen en schulden regel voor regel op (en zondert de derden af).
>
> _Trigger_: Soort relatie: controle → integraal; invloed van betekenis (of uitgesloten dochters / niet-geïntegreerde gemeenschappelijke dochters) → vermogensmutatie.

> [!info]- Niet verwarren met [[evenredige-consolidatie]]
> Evenredig neemt bezittingen en schulden pro-rata op (regel voor regel). Vermogensmutatie houdt de deelneming als één post 'Vennootschappen waarop vermogensmutatie is toegepast'. Evenredig is de regel voor gemeenschappelijke dochters; vermogensmutatie de uitzondering bij gebrek aan integratie.
>
> _Trigger_: Mate van integratie van de gemeenschappelijke dochter: nauw geïntegreerd → evenredig; los → vermogensmutatie.


## Valkuilen

> [!warning]- Het pro-rata aandeel in een verlies kan de boekwaarde van de deelneming nooit onder nul brengen
> ⚠️ Het pro-rata aandeel in een verlies kan de boekwaarde van de deelneming nooit onder nul brengen. Verdere verliezen worden niet doorgeboekt zolang er geen aanvullende verplichting (bv. borg, garantie) bestaat (CBN 2022/11, hypothese 3). ⚖️
>
> _Bron: CBN 2022/11_


> [!warning]- Een dividend dat de geassocieerde uitkeert vermindert haar eigen vermogen — maar wordt in de jaarrekening van de moeder geboekt als financië…
> ⚠️ Een dividend dat de geassocieerde uitkeert vermindert haar eigen vermogen — maar wordt in de jaarrekening van de moeder geboekt als financiële opbrengst (zonder voor een tweede maal als 'aandeel in resultaat' te worden geteld). De vermogensmutatie corrigeert dat: het resultaat-aandeel wordt berekend exclusief het deel dat als dividend wordt uitgekeerd. ⚖️
>
> _Bron: CBN 2022/11 — Latere consolidaties_


> [!warning]- Wijzigingen in het eigen vermogen van de geassocieerde buiten het resultaat om (herwaarderingsmeerwaarde, kapitaalsubsidie, omrekeningsversc…
> ⚠️ Wijzigingen in het eigen vermogen van de geassocieerde buiten het resultaat om (herwaarderingsmeerwaarde, kapitaalsubsidie, omrekeningsverschillen) moeten óók in de vermogensmutatie worden meegenomen — niet alleen het resultaat. Dit was vroeger een onderbelicht punt; CBN 2014/3 verduidelijkte het en CBN 2022/11 codificeerde de werkwijze. ⚖️
>
> _Bron: CBN 2014/3 + 2022/11_



## Zie ook

- **Getriggerd door**: [[invloed-van-betekenis]]

## Bronnen

[^1]: `CBN-2022-11-vermogensmutatiemethode__sec_toepassingsgebied`
[^2]: `CBN-2022-11-vermogensmutatiemethode__sec_eerste-consolidatie`
[^3]: `KB-WVV-2019__art_3_113`
[^4]: `KB-WVV-2019__art_3_115`
[^5]: `CBN-2013-03-de-boekhoudkundige-verwerking-van-step-acquisitions-update__sec_inleiding`
[^6]: `CBN-2013-03-de-boekhoudkundige-verwerking-van-step-acquisitions-update__sec_praktische-uitwerking`
[^7]: `KB-WVV-2019__art_3_78`
[^8]: `KB-WVV-2019__art_3_77`
[^9]: `CBN-2022-11-vermogensmutatiemethode__sec_voorbeeld`
[^10]: `CBN-2022-11-vermogensmutatiemethode__sec_latere-consolidaties`
[^11]: `CBN-2014-03-de-boekhoudkundige-verwerking-van-mutaties-binnen-het-eigen-vermogen-van-een-geassocieerde__sec_inleiding`
[^12]: `KB-WVV-2019__art_3_112`
[^13]: `CBN-2013-03-de-boekhoudkundige-verwerking-van-step-acquisitions-update__sec_voorbeeld-1`
[^14]: `CBN-2022-11-vermogensmutatiemethode__sec_herberekening-van-het-bedrag-van-de-deelneming-waarop-de-ver`
[^15]: `CBN-2022-11-vermogensmutatiemethode__sec_herberekening-van-het-bedrag-van-de-deelneming-waarop-de-ver_2`
[^16]: `CBN-2022-11-vermogensmutatiemethode__sec_herberekening-van-het-bedrag-van-de-deelneming-waarop-de-ver_3`
[^17]: `CBN-2022-11-vermogensmutatiemethode__sec_intra-groepsverkopen-upstream-downstream-sales`
[^18]: `CBN-2022-11-vermogensmutatiemethode__sec_toepassing-van-de-vermogensmutatiemethode`
[^19]: `CBN-2022-11-vermogensmutatiemethode__sec_voorbeeld-2-verkoop-van-de-deelnemingen-waarop-vermogensmuta`
[^20]: `CBN-2022-11-vermogensmutatiemethode__sec_directe-mutaties-binnen-het-eigen-vermogen-van-de-geassociee`
