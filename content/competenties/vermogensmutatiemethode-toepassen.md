---
tags: ["1.4", wip, competentie]
niveau: toepassen
status: draft
programmaonderdelen: ["1.4"]
itaa-lex-secties:
  - XV (KB) (KB-WVV art. 3:141–3:148)
  - XV (WVV art. 1:21)
---

# Vermogensmutatiemethode toepassen

De boekhoudkundige verwerking van een deelneming in een **geassocieerde vennootschap** (of een uitgesloten dochteronderneming) in de geconsolideerde jaarrekening via de vermogensmutatiemethode (equity-methode). Vereist dat de [[consolidatiekring-bepalen|consolidatiekring reeds bepaald]] is en dat de deelneming als "equity-methode" is aangewezen.

## Aanbevolen werkwijze

### 1. 🔍 Initiële opname bepalen

> 📥 **Nodig**:
> - Aankoopprijs van de deelneming
> - Gecorrigeerd eigen vermogen van de geassocieerde vennootschap op de datum van verwerving
> - Percentage belang
>
> 📤 **Uitkomst**:
> - Beginwaarde van de deelneming in de geconsolideerde balans
> - Eventueel initieel [[consolidatieverschillen|consolidatieverschil]]

De deelneming wordt **initieel opgenomen** voor de aankoopprijs. Vervolgens wordt de aankoopprijs vergeleken met het aandeel van de consoliderende vennootschap in het gecorrigeerde eigen vermogen van de geassocieerde vennootschap op de overnamedatum:

```
Aankoopprijs deelneming
− % belang × gecorrigeerd EV geassocieerde vennootschap op overnamedatum
────────────────────────────────────────────────────────────────────
= Initieel consolidatieverschil (positief: actief; negatief: passief)
```

Het verschil wordt eerst toegerekend aan activa/passiva met stille reserves/lasten. Het saldo is het initiële [[consolidatieverschillen|consolidatieverschil]]. ([[wetteksten/XV-KB-wvv#art-3146|KB-WVV art. 3:146]])

*(Grondslag: [[wetteksten/XV-KB-wvv#art-3142|KB-WVV art. 3:141–3:142]], [[wetteksten/XV-KB-wvv#art-3146|art. 3:146]])*

### 2. 🔢 Jaarlijkse aanpassing boekwaarde deelneming

> 📥 **Nodig**:
> - Resultaat van de geassocieerde vennootschap over het boekjaar
> - Percentage belang
> - Dividenden uitgekeerd door de geassocieerde vennootschap aan de consoliderende vennootschap
>
> 📤 **Uitkomst**:
> - Gecorrigeerde boekwaarde deelneming in de geconsolideerde balans
> - Aandeel in het resultaat in de geconsolideerde resultatenrekening

De boekwaarde van de deelneming evolueert elk boekjaar als volgt:

```
Beginwaarde deelneming (begin boekjaar)
+ % belang × positief resultaat geassocieerde vennootschap
− % belang × negatief resultaat (verlies) geassocieerde vennootschap
− % belang × uitgekeerd dividend (ontvangen door consoliderende vennootschap)
────────────────────────────────────────────────────────────────────
= Eindwaarde deelneming (einde boekjaar)
```

In de geconsolideerde resultatenrekening verschijnt het aandeel in het resultaat als een afzonderlijke post. ([[wetteksten/XV-KB-wvv#art-3143|KB-WVV art. 3:143]])

*(Grondslag: [[wetteksten/XV-KB-wvv#art-3142|KB-WVV art. 3:142–3:143]])*

> [!warning]- Ontvangen dividend verlagen de boekwaarde — niet als opbrengst boeken
> ❌ *"Dividenden ontvangen van een geassocieerde vennootschap worden als financiële opbrengst geboekt in de geconsolideerde resultatenrekening."*
>
> In de geconsolideerde jaarrekening worden ontvangen dividenden van een geassocieerde vennootschap **niet** als opbrengst verwerkt. Ze verlagen de boekwaarde van de deelneming, omdat het dividend een uitkering is van eigen vermogen dat al via het "aandeel in het resultaat" was opgenomen.
>
> 🤖 *AI-aanvulling*

> [!info]- In de praktijk
>
> Moeder M bezit 30% van geassocieerde vennootschap G. Beginwaarde deelneming G: 600. Resultaat G dit jaar: 400. Dividend uitgekeerd aan M: 60.
>
> - Aandeel M in resultaat: 30% × 400 = 120 → bijschrijven op boekwaarde en in resultatenrekening
> - Ontvangen dividend: 60 → afschrijven van boekwaarde (EV daalt bij G door dividenduitkering)
> - Eindwaarde deelneming G: 600 + 120 − 60 = 660
>
> 🤖 *AI-aanvulling*

### 3. 🔢 Consolidatieverschil verwerken

> 📥 **Nodig**:
> - [[vermogensmutatiemethode-toepassen#1-🔍-initiële-opname-bepalen|Initieel consolidatieverschil]]
>
> 📤 **Uitkomst**:
> - Gecorrigeerde boekwaarde deelneming (inclusief consolidatieverschil na verwerking)

Behandel het initiële consolidatieverschil op dezelfde wijze als bij [[consolideren-integraal|integrale consolidatie]]:

- **Positief verschil**: afschrijven ten laste van de geconsolideerde resultatenrekening ([[wetteksten/XV-KB-wvv#art-3147|KB-WVV art. 3:147]]).
- **Negatief verschil**: niet meteen in resultaat; enkel vrijval wanneer verwachte verliezen of kosten van de geassocieerde vennootschap werkelijkheid worden.

*(Grondslag: [[wetteksten/XV-KB-wvv#art-3146|KB-WVV art. 3:146–3:147]])*

### 4. ✅ Presentatie in de geconsolideerde jaarrekening controleren

> 📥 **Nodig**:
> - Berekende eindwaarde deelneming
> - Aandeel in resultaat en afschrijving consolidatieverschil
>
> 📤 **Uitkomst**:
> - Correcte presentatie in balans en resultatenrekening

**Balans**: de deelneming verschijnt onder de financiële vaste activa in de afzonderlijke post **"Vennootschappen waarop vermogensmutatie is toegepast"**. ([[wetteksten/XV-KB-wvv#art-3141|KB-WVV art. 3:141]])

**Resultatenrekening**: het aandeel in het resultaat verschijnt als afzonderlijke post. Dividenden verschijnen **niet** als opbrengst.

**Toelichting**: geef per geassocieerde vennootschap informatie over de naam, zetel, percentage belang en de boekwaarde. ([[wetteksten/XV-KB-wvv#art-3148|KB-WVV art. 3:148]])

*(Grondslag: [[wetteksten/XV-KB-wvv#art-3141|KB-WVV art. 3:141]], [[wetteksten/XV-KB-wvv#art-3143|art. 3:143]], [[wetteksten/XV-KB-wvv#art-3148|art. 3:148]])*

## Voorbeelden

> [!example]- Geassocieerde vennootschap met verlies
>
> **Situatie**: M bezit 40% van G. Initiële aankoopprijs: 500, aandeel in gecorrigeerd EV op overnamedatum: 500 (geen consolidatieverschil). Vorig jaar eindwaarde: 500. Dit jaar verlies G: 300. Geen dividend.
>
> **Conclusie**:
> - Aandeel M in verlies: 40% × 300 = 120
> - Boekwaarde deelneming: 500 − 120 = 380
> - In de geconsolideerde resultatenrekening: "Aandeel in het resultaat van vennootschappen waarop de vermogensmutatiemethode wordt toegepast" = −120.
>
> **Grondslag**: KB-WVV art. 3:142–3:143
>
> **Redenering**: de vermogensmutatiemethode weerspiegelt het werkelijke aandeel van M in het eigen vermogen van G. Bij verlies daalt het EV van G → de boekwaarde van de deelneming daalt mee.
>
> 🤖 *AI-aanvulling*

## Motiveren op het examen

**Een volledig antwoord bevat:**
1. Vaststelling dat de deelneming via de vermogensmutatiemethode wordt verwerkt (grondslag: KB-WVV art. 3:124, 3°)
2. Berekening initiële boekwaarde en eventueel initieel consolidatieverschil
3. Jaarlijkse aanpassing: aandeel in resultaat opnemen, dividend aftrekken
4. Presentatie: aparte balanspost "Vennootschappen waarop vermogensmutatie is toegepast", aparte resultatenpost

**Typische vraagvormen**

> [!question]- Dividend van geassocieerde vennootschap
>
> M bezit 35% van geassocieerde vennootschap G. G maakt dit jaar een winst van 200 en keert een dividend uit van 40 aan M. Hoe verwerkt M dit in haar geconsolideerde jaarrekening?
>
> > [!success]- Antwoord
> >
> > - Aandeel in resultaat: 35% × 200 = 70 → opgenomen in de geconsolideerde resultatenrekening als positieve post "Aandeel in het resultaat van vennootschappen waarop de vermogensmutatiemethode wordt toegepast".
> > - Dividend ontvangen: 40 → verlaagt de boekwaarde van de deelneming (geen opbrengst in de resultatenrekening).
> > - Netto aanpassing boekwaarde: +70 − 40 = +30.
> >
> > *Zie: [[vermogensmutatiemethode-toepassen#2-🔢-jaarlijkse-aanpassing-boekwaarde-deelneming|Jaarlijkse aanpassing boekwaarde]]*
>
> 🤖 *AI-aanvulling*
