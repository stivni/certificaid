---
title: Evenredige consolidatie (proportionele consolidatie)
tags:
- concept
- cluster
- po-1-4
linked_anchors:
- 1.4.I.D
- 1.4.I.B
- 1.4.II.C
- 1.4.taak.1
programmaonderdelen:
- '1.4'
confidence: grounded
node_type: cluster
status: seed
schema_version: '1.5'
gegenereerd_uit: data/concepten/records/evenredige-consolidatie.json
gegenereerd_op: '2026-05-18'
---
# Evenredige consolidatie (proportionele consolidatie) ⚖️

> [!summary] Korte inhoud
> Een gemeenschappelijke dochter (een vennootschap die door een beperkt aantal vennoten samen wordt gecontroleerd, op grond van een overeenkomst) neem je in de geconsolideerde jaarrekening van elke gezamenlijk controlerende moeder op naar rato van haar aandeel in het kapitaal (of i….

> [!info] Behoort tot: [[consolidatiemethodes-vergelijking]]

Een gemeenschappelijke dochter (een vennootschap die door een beperkt aantal vennoten samen wordt gecontroleerd, op grond van een overeenkomst) neem je in de geconsolideerde jaarrekening van elke gezamenlijk controlerende moeder op naar rato van haar aandeel in het kapitaal (of in de inbreng bij vennootschappen zonder kapitaal). Alleen jouw pro-rata stuk van de bezittingen, schulden, opbrengsten en kosten komt erin — geen afzonderlijke 'belangen van derden' nodig, want het deel buiten de groep wordt simpelweg niet opgenomen.

_Bron: KB WVV art. 3:124, 2° jo. art. 3:140_


## Bouwstenen

### Pro-rata opname ⚖️

Neem elke bezitting, schuld, opbrengst en kost van de gemeenschappelijke dochter op naar rato van jouw aandeel in het kapitaal (of in de inbreng bij vennootschappen zonder kapitaal).

**Waarom?** Je deelt de macht over deze dochter met andere vennoten; je hebt geen 100 %-zeggenschap. De geconsolideerde jaarrekening reflecteert die gedeelde macht door alleen jouw stuk te tonen.



Cardinal Group NV bezit 50 % van Filmstudio Florence BV (gezamenlijke controle). Filmstudio Florence heeft € 4.000.000 vaste activa → Cardinal neemt 50 % × € 4.000.000 = € 2.000.000 op in haar geconsolideerde balans.

_Grondslag: KB WVV art. 3:140, b_

### Integrale-consolidatie-regels gelden, maar op het pro-rata stuk ⚖️

Op het opgenomen pro-rata deel pas je alle technieken van integrale consolidatie toe: schrappen van de deelneming (KB WVV art. 3:127, a), toerekening van verschillen (art. 3:128 jo. 3:130), boeken van consolidatieverschil (art. 3:130) met afschrijving (art. 3:131), gedeeltelijke realisatie (art. 3:132–3:133) en eliminatie van onderlinge posten (art. 3:134, 3:136, 3:139). Het verschil: alles wat 100 % was bij integrale consolidatie, gebeurt nu pro-rata.

**Waarom?** Door dezelfde technieken op een kleinere schaal toe te passen behoud je consistentie binnen de geconsolideerde jaarrekening — een goodwill bij een gemeenschappelijke dochter werkt boekhoudkundig op dezelfde manier als bij een gewone dochter, alleen voor jouw deel.



Cardinal koopt haar 50 %-belang in Filmstudio Florence voor € 1.500.000; pro-rata eigen vermogen (EV) Filmstudio op aankoopdatum = € 1.250.000 → bruto-verschil € 250.000 op pro-rata basis, eventueel toe te rekenen aan stille meerwaarden in Filmstudio's apparatuur.

_Grondslag: KB WVV art. 3:140, a_

### Geen 'Belangen van derden'-post 🤖

Bij evenredige consolidatie verschijnt er geen post 'Belangen van derden' of 'Aandeel van derden in het resultaat'. Het deel buiten je groep neem je gewoon niet op — er valt dus niets af te zonderen.

**Waarom?** Bij integrale consolidatie zit 100 % van de dochter in de geconsolideerde balans, en moet de niet-moeder-fractie zichtbaar worden gemaakt. Bij evenredige consolidatie zit alleen jouw stuk er al in — het deel van de andere vennoten verschijnt nooit; daarom geen derden-correctie nodig.



Cardinal neemt 50 % van Filmstudio Florence op; Energiehuis Evergem neemt de andere 50 % op in haar eigen geconsolideerde jaarrekening. Geen 'Belangen van derden' aan beide zijden.

_Grondslag: KB WVV art. 3:140 (geen verwijzing naar KB WVV art. 3:137)_


## Berekening

### Evenredige consolidatie — pro-rata opname

**Pro-rata opname van een post** 
```
geconsolideerde post = post moeder + (post gemeenschappelijke dochter × belangenpercentage) − pro-rata intragroep-eliminaties
```

| Symbool | Betekenis | Eenheid |
|---|---|---|
| `post moeder` | Bedrag van de post bij de moeder (en eventueel integraal geconsolideerde dochters) | EUR |
| `post gemeenschappelijke dochter` | 100 %-bedrag van dezelfde post bij de gemeenschappelijke dochter | EUR |
| `belangenpercentage` | Aandeel van moeder en haar groep in het kapitaal van de gemeenschappelijke dochter | % |
| `pro-rata intragroep-eliminaties` | Onderlinge transacties × belangenpercentage | EUR |

**Voorbeeld-invulling**: Cardinal-vaste activa = € 2.500.000; Filmstudio Florence-vaste activa = € 4.000.000; belang Cardinal in Filmstudio = 50 %; geen intragroep op deze post

```
€ 2.500.000 + (€ 4.000.000 × 50 %) − € 0 = € 2.500.000 + € 2.000.000 = € 4.500.000
```

_Resultaat in EUR_
**Eliminatie intra-groepsverkoop (op pro-rata basis)** 
```
te elimineren winst = nog-niet-gerealiseerde winst op intra-groepsverkoop × belangenpercentage
```

| Symbool | Betekenis | Eenheid |
|---|---|---|
| `nog-niet-gerealiseerde winst op intra-groepsverkoop` | Winstmarge die de dochter op een interne verkoop heeft gerealiseerd, voor zover de goederen nog in voorraad zitten bij de koper binnen de groep | EUR |
| `belangenpercentage` | Aandeel van moeder in kapitaal gemeenschappelijke dochter | % |

**Voorbeeld-invulling**: winst op intra-groepsverkoop Filmstudio aan Cardinal = € 50.000 (nog in voorraad); belang Cardinal = 50 %

```
€ 50.000 × 50 % = € 25.000
```

_Resultaat in EUR_
*Bij gezamenlijke controle deel je de zeggenschap met andere vennoten. De geconsolideerde jaarrekening laat dat zien door alleen jouw deel van bezittingen, schulden, opbrengsten en kosten op te nemen. Het deel buiten de groep verschijnt niet — er is dus geen derden-post zoals bij integrale consolidatie.*

### 1. Bepaal jouw belangenpercentage in de gemeenschappelijke dochter

Bereken welk percentage van het kapitaal (of de inbreng) jouw moeder en haar dochters in de consolidatiekring samen in de gemeenschappelijke dochter aanhouden.

**Waarom?** Dit percentage is jouw 'pro-rata-factor'. Een verkeerd percentage hier zorgt voor verkeerde bedragen in elke post van de geconsolideerde balans en resultatenrekening.

**📥 Input**:
- Aandeelhoudersregister gemeenschappelijke dochter → **Aandeel in kapitaal van moeder + groepsleden** _(percentage)_

**📤 Output**:
- Werkblad evenredige consolidatie → **Pro-rata-percentage** _(percentage)_

**🛠️ Hoe**:

1. Open het aandeelhoudersregister van Filmstudio Florence BV.
2. Tel het aandeel van Cardinal Group NV (50 %) bij het aandeel van eventuele Cardinal-dochters (bv. 0 %) — totaal 50 %.
3. Dit is jouw pro-rata-percentage.
4. Let op: dit is het belangenpercentage (kapitaal), niet het controlepercentage. Bij 50/50 met overeenkomst is de controle gedeeld maar het belang exact 50 %.


**Grondslag**: KB WVV art. 3:140, b

### 2. Vermenigvuldig elke post van de dochter met het percentage

Pas het pro-rata-percentage toe op elke afzonderlijke balanspost en elke afzonderlijke post van de resultatenrekening van de gemeenschappelijke dochter.

**Waarom?** Pro-rata opname werkt regel voor regel, niet als één samengevatte deelneming. Daardoor blijft de groepsstructuur transparant per post (vaste activa, voorraden, schulden, …).

**📥 Input**:
- Balans + resultatenrekening gemeenschappelijke dochter → **Alle posten** _(boekhoudkundig-bedrag)_
- Werkblad evenredige consolidatie → **Pro-rata-percentage** _(percentage)_

**📤 Output**:
- Werkblad evenredige consolidatie → **Pro-rata bedragen per post** _(boekhoudkundig-bedrag)_

**🛠️ Hoe**:

1. Voor elke balanspost van Filmstudio Florence: vermenigvuldig met 50 %. Vaste activa € 4.000.000 → € 2.000.000; voorraden € 1.000.000 → € 500.000; kas € 500.000 → € 250.000; eigen vermogen € 3.000.000 → € 1.500.000; schulden € 2.500.000 → € 1.250.000.
2. Voor elke resultatenpost: idem. Omzet € 5.000.000 → € 2.500.000; kosten € 4.000.000 → € 2.000.000; resultaat € 1.000.000 → € 500.000.
3. Schrijf elke pro-rata-uitkomst in je werkblad.


**Grondslag**: KB WVV art. 3:140, b

### 3. Tel de pro-rata bedragen op bij de moeder + integraal geconsolideerde dochters

Voeg de pro-rata bedragen samen met de overeenkomstige posten van de moeder en van alle dochters die je integraal consolideert.

**Waarom?** De gemeenschappelijke dochter komt zo, voor haar pro-rata deel, gewoon mee in de groepsbalans en -resultatenrekening — naast de volledig opgenomen integrale dochters.

**📥 Input**:
- Werkblad evenredige consolidatie → **Pro-rata bedragen** _(boekhoudkundig-bedrag)_
- Geconsolideerde balans/resultatenrekening (tussentijds) → **Bedragen moeder + integrale dochters** _(boekhoudkundig-bedrag)_

**📤 Output**:
- Geconsolideerde balans + resultatenrekening → **Bijgewerkte posten** _(nieuwe-balanspost)_

**🛠️ Hoe**:

1. Open de tussentijdse geconsolideerde balans (moeder + integrale dochters).
2. Tel post per post de pro-rata bedragen van Filmstudio Florence erbij.
3. Idem voor de resultatenrekening.
4. Belangrijke uitzondering: nog niet met intra-groepselimaties — die volgen in stap 4.


> [!example]- Voorbeeld: Cardinal Group NV en Energiehuis Evergem BV bezitten elk 50 % van Filmstudio Florence BV. Balans Filmstudio: vaste activ…
> Cardinal Group NV en Energiehuis Evergem BV bezitten elk 50 % van Filmstudio Florence BV. Balans Filmstudio: vaste activa € 4.000.000, voorraden € 1.000.000, kas € 500.000; eigen vermogen € 3.000.000, schulden € 2.500.000. Resultaat: omzet € 5.000.000, kosten € 4.000.000, resultaat € 1.000.000.
>
> 1. **Pro-rata-percentage voor Cardinal** 🧮
>
>    Cardinal in Filmstudio = **50 %**
>
> 2. **Pro-rata balansposten (Filmstudio → 50 %)** 📊
>
>    | Post                       | Filmstudio (€) | × 50 % (€) |
>    |----------------------------|---------------:|-----------:|
>    | Vaste activa               |      4.000.000 |  2.000.000 |
>    | Voorraden                  |      1.000.000 |    500.000 |
>    | Kas                        |        500.000 |    250.000 |
>    | **Totaal activa**          |  **5.500.000** | **2.750.000** |
>    | Eigen vermogen             |      3.000.000 |  1.500.000 |
>    | Schulden aan derden        |      2.500.000 |  1.250.000 |
>    | **Totaal passiva**         |  **5.500.000** | **2.750.000** |
>
> 3. **Pro-rata resultatenrekening** 🧮
>
>    Omzet: 50 % × € 5.000.000 = **€ 2.500.000**
>    Kosten: 50 % × € 4.000.000 = **€ 2.000.000**
>    Resultaat: 50 % × € 1.000.000 = **€ 500.000**
>

**Grondslag**: KB WVV art. 3:140, b

### 4. Schrap intragroep-posten — op het pro-rata deel

Pas de compensatie- en eliminatieregels (KB WVV art. 3:127, 3:128, 3:130, 3:134, 3:136) toe — maar enkel op het pro-rata deel.

**Waarom?** Een joint venture is voor de groep geen volledige interne speler maar voor jouw stuk wel. Je elimineert dus pro-rata: een intra-groepsverkoop wordt niet voor 100 % weggeboekt, maar voor jouw belang × bedrag.

**📥 Input**:
- Lijst transacties tussen moedergroep en gemeenschappelijke dochter → **Bedragen + winstmarge** _(boekhoudkundig-bedrag)_
- Werkblad evenredige consolidatie → **Pro-rata-percentage** _(percentage)_

**📤 Output**:
- Geconsolideerde balans + resultatenrekening → **Geëlimineerde posten** _(geëlimineerde-post)_

**🛠️ Hoe**:

1. Maak een lijst van alle vorderingen, schulden, verkopen en aankopen tussen Cardinal (of haar dochters) en Filmstudio Florence.
2. Elimineer pro-rata: bedrag × 50 %.
3. Voorbeeld: intra-groepsverkoop van Filmstudio aan Cardinal voor 60, met winstmarge 10 nog in voorraad bij Cardinal → schrap 50 % × 10 = 5 winst uit de geconsolideerde voorraad én uit het geconsolideerd resultaat.
4. Compensatie van Cardinal's deelneming Filmstudio met haar pro-rata aandeel in Filmstudio's EV: idem, op pro-rata basis.


**Grondslag**: KB WVV art. 3:140, a) jo. art. 3:127–3:136

**Voorbeeld**: Cardinal Group NV en Energiehuis Evergem BV oefenen gezamenlijke controle uit over Filmstudio Florence BV via een aandeelhoudersovereenkomst — elk bezit 50 % van het kapitaal. Balans Filmstudio Florence: vaste activa € 4.000.000, voorraden € 1.000.000, kas € 500.000; eigen vermogen € 3.000.000, schulden € 2.500.000. Resultatenrekening: omzet € 5.000.000, kosten € 4.000.000, resultaat € 1.000.000. Cardinal koopt voor € 300.000 goederen bij Filmstudio (intra-groepsverkoop, nog in voorraad bij Cardinal; Filmstudio realiseerde daarop € 50.000 winst).

```
Pro-rata deel van Cardinal in Filmstudio = 50 %.
Geconsolideerde activa van Filmstudio (vóór eliminatie): 50 % × (€ 4.000.000 + € 1.000.000 + € 500.000) = 50 % × € 5.500.000 = € 2.750.000. Geconsolideerde schulden van Filmstudio: 50 % × € 2.500.000 = € 1.250.000. Geconsolideerd eigen vermogen van Filmstudio: 50 % × € 3.000.000 = € 1.500.000.
Geconsolideerde omzet uit Filmstudio: 50 % × € 5.000.000 = € 2.500.000. Geconsolideerde kosten uit Filmstudio: 50 % × € 4.000.000 = € 2.000.000. Geconsolideerd resultaat uit Filmstudio (vóór eliminatie): 50 % × € 1.000.000 = € 500.000.
Intragroep-eliminatie (KB WVV art. 3:140 jo. art. 3:134, op pro-rata deel): de winst op de intragroep-verkoop wordt geëlimineerd voor 50 % × € 50.000 = € 25.000. Geconsolideerde voorraden Cardinal verminderen met € 25.000; geconsolideerd resultaat vermindert met € 25.000.
```

Resultaat: In de geconsolideerde balans van Cardinal verschijnen € 2.750.000 activa en € 1.250.000 schulden uit Filmstudio (na intragroep-eliminatie € 2.725.000 activa); van het resultaat € 1.000.000 wordt € 500.000 meegenomen, verminderd met € 25.000 → € 475.000 in het geconsolideerd resultaat. Er is géén post 'Aandeel van derden in resultaat' — de andere 50 % van Filmstudio komt niet voor in Cardinal's geconsolideerde jaarrekening (Energiehuis Evergem BV doet dezelfde oefening met haar eigen 50 %).

## In de praktijk

<h3 id="wanneer-toepassen">Wanneer toepassen</h3>

> [!tip]- Wanneer toepassen
> Standaard voor gemeenschappelijke dochters bij gezamenlijke controle. Uitzondering: gemeenschappelijke dochters die niet nauw geïntegreerd zijn in de activiteit van de moeder mogen via vermogensmutatie worden verwerkt (CBN 2013/3). ⚖️

> [!tip]- Herkennen op het examen
> Gezamenlijke controle (overeenkomst, vetorecht) + integratie → evenredige consolidatie.


## Voorwaarden / uitzonderingen

- Er moet gezamenlijke controle bestaan over de gemeenschappelijke dochter: een overeenkomst dat beleidsbeslissingen alleen met gemeenschappelijke instemming kunnen worden genomen. ⚖️
- De activiteit van de gemeenschappelijke dochter moet voldoende geïntegreerd zijn in die van de gezamenlijk controlerende moeder. Is de activiteit niet nauw geïntegreerd, dan kun je in plaats van evenredige consolidatie de vermogensmutatiemethode gebruiken (CBN 2013/3). ⚖️
> [!info]- Niet verwarren met [[integrale-consolidatie]]
> Integraal = 100 % opname met afzondering van derden-deel via 'Belangen van derden'. Evenredig = pro-rata opname (% kapitaaldeelname), geen derden-post.
>
> _Trigger_: Soort controle bepaalt de methode: exclusieve controle → integraal; gezamenlijke controle → evenredig (of vermogensmutatie als niet-geïntegreerd).

> [!info]- Niet verwarren met [[vermogensmutatiemethode]]
> Evenredige consolidatie neemt bezittingen/schulden regel voor regel pro-rata op. Vermogensmutatie houdt de deelneming als één gesynthetiseerde post ('Vennootschappen waarop vermogensmutatie is toegepast'). Bij gezamenlijke controle van een niet-geïntegreerde dochter mag je kiezen voor vermogensmutatie.
>
> _Trigger_: Mate van integratie van de gemeenschappelijke dochter in de groep — nauw geïntegreerd → evenredig; los → vermogensmutatie.


## Valkuilen

> [!warning]- Het opgenomen pro-rata deel volgt het belangenpercentage (kapitaal), niet het controlepercentage
> ⚠️ Het opgenomen pro-rata deel volgt het belangenpercentage (kapitaal), niet het controlepercentage. Een 50/50-joint venture wordt voor 50 % opgenomen, ook al heeft elke vennoot via de overeenkomst eigenlijk een gelijke beleidsmacht (gedeelde 100 % controle). ⚖️
>
> _Bron: KB WVV art. 3:140, b_


> [!warning]- Intra-groepsverkopen tussen moeder en gemeenschappelijke dochter worden geëlimineerd op het pro-rata deel — niet voor 100 %
> ⚠️ Intra-groepsverkopen tussen moeder en gemeenschappelijke dochter worden geëlimineerd op het pro-rata deel — niet voor 100 %. Andere bronnen (oudere W.Venn., IFRS 11) kennen andere regels; in WVV-context geldt de pro-rata-eliminatie. 🤖
>
> _Bron: KB WVV art. 3:140, a_



## Zie ook

- **Getriggerd door**: [[gezamenlijke-controle]]

## Voorbeelden

Cardinal Group NV en Energiehuis Evergem BV bezitten elk 50 % van Filmstudio Florence BV (gezamenlijke controle via aandeelhoudersovereenkomst). Cardinal neemt 50 % van elke balanspost en elke opbrengst/kost van Filmstudio Florence op in haar geconsolideerde jaarrekening. Geen post 'Belangen van derden'.

## Bronnen

[^1]: `KB-WVV-2019__art_3_111`
[^2]: `KB-WVV-2019__art_3_110`
[^3]: `CBN-2017-02-gezamenlijke-controle-over-een-vennootschap-groottecriteria-update__sec_algemeen`
[^4]: `CBN-2013-03-de-boekhoudkundige-verwerking-van-step-acquisitions-update__sec_praktische-uitwerking`
[^5]: `KB-WVV-2019__art_3_108`
[^6]: `KB-WVV-2019__art_3_106`
[^7]: `CBN-2017-02-gezamenlijke-controle-over-een-vennootschap-groottecriteria-update__sec_voorbeeld-2`
[^8]: `KB-WVV-2019__art_3_98`
