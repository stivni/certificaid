---
tags: ["1.4", wip, competentie]
niveau: toepassen
status: draft
programmaonderdelen: ["1.4"]
itaa-lex-secties:
  - XV (KB) (KB-WVV art. 3:126–3:139)
  - XV (KB) (KB-WVV art. 3:123–3:125)
bouwversie: 0
---

# Integraal consolideren

De technische uitvoering van integrale consolidatie: van de enkelvoudige jaarrekeningen van de consoliderende vennootschap en haar volledig geconsolideerde dochterondernemingen naar een geconsolideerde balans en resultatenrekening. Deze competentie veronderstelt dat de [[consolidatiekring-bepalen|consolidatiekring reeds bepaald]] is en dat de juiste entiteiten als "integraal te consolideren" zijn aangewezen.

## Aanbevolen werkwijze

### 1. 🔍 Waarderingsaanpassingen doorvoeren

> 📥 **Nodig**:
> - Enkelvoudige jaarrekeningen van alle integraal te consolideren entiteiten
>
> 📤 **Uitkomst**:
> - Gecorrigeerde jaarrekeningen op basis van uniforme waarderingsregels

Alle activa en passiva moeten gewaardeerd zijn volgens **uniforme regels** vóór de optelling. Dit vereist:

1. **Herwaardering** van activa/passiva van dochterondernemingen die andere waarderingsregels hanteren dan de moeder (bv. andere afschrijvingspercentages, andere voorraadbepaling). ([[wetteksten/XV-KB-wvv#art-3115|KB-WVV art. 3:115]])
2. **Eliminatie van fiscale distorsies**: grotere afschrijvingen of grotere passiva dan economisch verantwoord, aangebracht omwille van fiscale redenen, worden ongedaan gemaakt. ([[wetteksten/XV-KB-wvv#art-3118|KB-WVV art. 3:118]])
3. **Belastinglatenties** boeken voor tijdelijke belastingverschillen die ontstaan door de herwaarderingen en distorsie-eliminaties (post IX.B "Uitgestelde belastingen en belastinglatenties"). ([[wetteksten/XV-KB-wvv#art-3119|KB-WVV art. 3:119]])

*(Grondslag: [[wetteksten/XV-KB-wvv#art-3115|KB-WVV art. 3:115–3:119]])*

### 2. 🔢 Kapitaaleliminatie berekenen

> 📥 **Nodig**:
> - Gecorrigeerde eigen vermogen van elke dochteronderneming op de datum van verwerving
> - Boekwaarde van de aandelen in elke dochteronderneming (bij de moeder)
> - Aankooppercentage per dochteronderneming
>
> 📤 **Uitkomst**:
> - Bedrag toegerekend aan individuele activa/passiva (stille reserves)
> - [[consolidatieverschillen|Consolidatieverschil]] (positief of negatief) per dochteronderneming

Voer de kapitaaleliminatie uit per dochteronderneming:

```
Boekwaarde aandelen bij moeder (te elimineren)
− Aandeel moeder in gecorrigeerd EV van dochter op overnamedatum
─────────────────────────────────────────────
= Verschil vóór toerekening

Toerekening aan individuele activa/passiva:
  - Herwaarder activa tot reële waarde (stille reserves → positief verschil)
  - Herwaarder passiva tot reële waarde (stille lasten → negatief verschil)
  - Verwante belastinglatentie op toerekening
─────────────────────────────────────────────
= Resterend consolidatieverschil (post "Consolidatieverschillen")
```

*(Grondslag: [[wetteksten/XV-KB-wvv#art-3127|KB-WVV art. 3:127–3:130]])*

### 3. 🔢 Belangen van derden bepalen

> 📥 **Nodig**:
> - Gecorrigeerd eigen vermogen van elke dochteronderneming na herwaardering
> - Percentage aandelen in handen van derden (niet de consoliderende vennootschap)
>
> 📤 **Uitkomst**:
> - Bedrag "Belangen van derden" aan passiefzijde van de geconsolideerde balans
> - Bedrag "Aandeel van derden in het resultaat" in de geconsolideerde resultatenrekening

Voor dochterondernemingen waarbij de consoliderende vennootschap minder dan 100% bezit:

```
Belangen van derden (balans) = % aandelen derden × gecorrigeerd EV dochter
Aandeel derden in resultaat  = % aandelen derden × resultaat boekjaar dochter
```

*(Grondslag: [[wetteksten/XV-KB-wvv#art-3127|KB-WVV art. 3:127, b]], [[wetteksten/XV-KB-wvv#art-3137|art. 3:137]])*

> [!info]- In de praktijk
>
> Moeder M bezit 70% van dochter D. Na waarderingsaanpassingen heeft D een gecorrigeerd EV van 1.000 en een resultaat van 200.
> - Belangen van derden (balans): 30% × 1.000 = 300
> - Aandeel derden in resultaat: 30% × 200 = 60
> - Na de kapitaaleliminatie van M's aandelenparticipatie blijft het aandeel van M in het EV van D in de consolidatie aanwezig via de individuele activa en passiva.
>
> 🤖 *AI-aanvulling*

### 4. 🔢 Optelling en intercompany-eliminaties

> 📥 **Nodig**:
> - Gecorrigeerde balansen en resultatenrekeningen van alle entiteiten
> - Overzicht van intercompany-transacties (vorderingen/schulden, verkopen, dividenden)
>
> 📤 **Uitkomst**:
> - Geconsolideerde balans en resultatenrekening na eliminaties

**Stap 4a — Optelling**: tel alle activa, passiva, opbrengsten en kosten van de consoliderende vennootschap en de dochterondernemingen samen (100% voor elk).

**Stap 4b — Eliminaties** ([[wetteksten/XV-KB-wvv#art-3134|KB-WVV art. 3:134, 3:136]]):

*Balans:*
- Elimineer onderlinge vorderingen en schulden (bv. vordering moeder op dochter = schuld dochter aan moeder).
- Elimineer niet-gerealiseerde intercompany-winsten in voorraden of activa (bv. dochter heeft goederen gekocht van moeder met marge → die marge is ongerealiseerd op groepsniveau).

*Resultatenrekening:*
- Elimineer intragroepsleveringen en -diensten (omzet bij verkoper = kost bij koper).
- Elimineer dividenden ontvangen van groepsvennootschappen.
- Elimineer waardeverminderingen op deelnemingen in groepsvennootschappen.
- Elimineer meer/minderwaarden op overdracht van deelnemingen binnen de groep.

*(Grondslag: [[wetteksten/XV-KB-wvv#art-3134|KB-WVV art. 3:134, 3:136, 3:139]])*

> [!warning]- Intercompany-winst in voorraden vergeten
> ❌ *"Intragroepsleveringen zijn geëlimineerd door de omzet te schrappen — klaar."*
>
> Naast de eliminatie van omzet/kost moet ook de **niet-gerealiseerde winst in de eindvoorraad** worden geëlimineerd. Als moeder een product met 30% marge verkoopt aan dochter en dochter heeft nog 40% in voorraad, dan zit er nog een intercompany-winst van 30% × 40% in de eindvoorraad van de dochter. Die winst is pas gerealiseerd wanneer dochter het aan een externe partij verkoopt.
>
> 🤖 *AI-aanvulling*

### 5. 🔢 Afschrijving consolidatieverschillen verwerken

> 📥 **Nodig**:
> - Positieve [[consolidatieverschillen|consolidatieverschillen]] en hun afschrijvingsplan
>
> 📤 **Uitkomst**:
> - Boekwaarde consolidatieverschillen na afschrijving in de geconsolideerde balans
> - Afschrijvingskost in de geconsolideerde resultatenrekening

Positieve consolidatieverschillen (goodwill bij consolidatie) worden **afgeschreven** ten laste van de geconsolideerde resultatenrekening. ([[wetteksten/XV-KB-wvv#art-3131|KB-WVV art. 3:131]])

Wanneer de afschrijving over meer dan vijf jaar wordt gespreid, moet dit worden gemotiveerd in de toelichting.

*(Grondslag: [[wetteksten/XV-KB-wvv#art-3131|KB-WVV art. 3:131]])*

## Voorbeelden

> [!example]- Eenvoudige consolidatie met 80%-dochter
>
> **Situatie**: Moeder M bezit 80% van dochter D. M heeft D twee jaar geleden gekocht voor 900. Op overnamedatum bedroeg het gecorrigeerde EV van D 1.000. In D zijn geen stille reserves aanwezig. Dit boekjaar heeft D een resultaat van 200.
>
> **Kapitaaleliminatie**:
> - Boekwaarde aandelen bij M: 900
> - Aandeel M in gecorrigeerd EV: 80% × 1.000 = 800
> - Verschil: 900 − 800 = 100 → positief consolidatieverschil
> - Toerekening aan individuele activa/passiva: 0 (geen stille reserves)
> - Consolidatieverschil op actief: 100
>
> **Belangen van derden** (balans): 20% × 1.000 = 200
>
> **Aandeel derden in resultaat**: 20% × 200 = 40
>
> **Afschrijving consolidatieverschil (jaar 2)**: stel 5 jaar lineair = 100/5 = 20 per jaar → na 2 jaar: boekwaarde 60, reeds afgeschreven 40.
>
> **Conclusie**: geconsolideerde resultatenrekening vermeldt 20 afschrijving op het consolidatieverschil; "Belangen van derden" staat op de passiva voor 200 + evolutie EV D.
>
> **Grondslag**: KB-WVV art. 3:127, 3:130, 3:131, 3:137
>
> 🤖 *AI-aanvulling*

## Motiveren op het examen

**Een volledig antwoord bevat:**
1. Waarderingsuniformiteit en fiscale distorsie-eliminatie vermelden
2. Kapitaaleliminatieberekening: aankoopprijs − aandeel in gecorrigeerd EV = verschil → toerekening → consolidatieverschil
3. Belangen van derden: percentage × gecorrigeerd EV (balans) en × resultaat (resultatenrekening)
4. Eliminaties: welke intercompany-posten worden geëlimineerd en waarom
5. Afschrijving positief consolidatieverschil: bedrag, periode, motivering indien >5 jaar

**Typische vraagvormen**

> [!question]- Intercompany-levering elimineren
>
> Moeder M verkoopt goederen aan Dochter D voor 1.000 (kostprijs 700, marge 300). Einde boekjaar heeft D nog 50% van de goederen in voorraad. Welk bedrag moet uit de geconsolideerde resultatenrekening worden geëlimineerd en hoeveel niet-gerealiseerde winst zit er in de geconsolideerde balans?
>
> > [!success]- Antwoord
> >
> > **Resultatenrekening**: de volledige intragroepsomzet van 1.000 (bij M) en de bijhorende kost van 1.000 (bij D) worden geëlimineerd.
> >
> > **Balans**: de 50% voorraad bij D bevat een niet-gerealiseerde intercompany-winst van 50% × 300 = 150. Deze wordt uit de voorraad geëlimineerd.
> >
> > Resultaat: geconsolideerde balans toont de goederen voor de kostprijs van M = 700 × 50% = 350. De winst van 150 is pas gerealiseerd wanneer D de goederen aan een externe klant verkoopt.
> >
> > *Zie: [[consolideren-integraal#4-🔢-optelling-en-intercompany-eliminaties|Intercompany-eliminaties]]*
>
> 🤖 *AI-aanvulling*
