---
title: Berekenen van controle- en belangenpercentage in een ketenstructuur
tags:
- competentie
- po-1-4
programmaonderdelen:
- '1.4'
status: voorgesteld
schema_version: '1.1'
gegenereerd_uit: data/concepten/competenties/berekenen-controle-en-belangenpercentage.yaml
gegenereerd_op: '2026-05-17'
---
# Berekenen van controle- en belangenpercentage in een ketenstructuur

**⚖️ 60% · 🤖 40%**

> De definities en de drempel (> 50 %) zijn wettelijk. De rekenregels in ketens (controle-% niet vermenigvuldigen, belangen-% wél) zijn praktijkconventies die in de CBN-doctrine en KB WVV-toepassing worden gehanteerd.

## Aanbevolen werkwijze

### 1. Tekenen van de aandeelhoudersketen

Maak een visueel schema van wie wie controleert in de groep, met stemrechtpercentage per schakel.

**Waarom?** Zonder schema is een correcte ketenberekening niet mogelijk.

**📥 Input**:
- Aandeelhoudersregister per vennootschap → **Stemrechtpercentage per directe deelneming** _(percentage)_

**📤 Output**:
- Werkpapier ketenstructuur → **Schema van directe deelnemingen** _(document)_

**🛠️ Hoe**:

1. Lijst alle vennootschappen in de groep (bv. Aurelia Holding NV, Brugse Brouwerij BV, Cardinal Group NV).
2. Teken per vennootschap een blok. Trek pijlen van moeder naar dochter met het stemrechtpercentage erbij (bv. Aurelia → 80 % → Brugse → 60 % → Cardinal).
3. Verifieer of elke schakel volledig is: ontbreken er aandeelhouders, dan kun je geen sluitende berekening maken.
4. Hou het schema bij de hand voor stappen 2 en 3.


**Grondslag**: [[controlepercentage]] §voorbereiding (praktijk)

### 2. Berekenen van het controlepercentage in elke schakel

Bepaal per dochter het percentage stemrechten dat de moeder direct of indirect via gecontroleerde tussenschakels uitoefent.

**Waarom?** Het controlepercentage bepaalt of er exclusieve controle is en dus consolidatieplicht.

**📥 Input**:
- Werkpapier ketenstructuur → **Stemrechtpercentage per schakel** _(percentage)_

**📤 Output**:
- Werkpapier per dochter → **Controlepercentage moeder** _(percentage)_

**🛠️ Hoe**:

1. Voor de directe dochter (Brugse): controlepercentage = direct gehouden stemrechten Aurelia in Brugse (80 %).
2. Voor een kleindochter (Cardinal): toets eerst of Aurelia exclusieve controle heeft over Brugse (80 % > 50 % → ja).
3. Heeft elke tussenschakel exclusieve controle, dan telt het volledige stemrechtpercentage van de onderste schakel mee. Controle Aurelia in Cardinal = 60 % (NIET 80 % × 60 %).
4. Pas op: zodra één schakel geen exclusieve controle heeft, breekt de keten — zie [[exclusieve-controle]] §keten-breuk.


> [!example]- Voorbeeld: Aurelia Holding NV bezit 80 % stemrechten in Brugse Brouwerij BV. Brugse bezit 60 % stemrechten in Cardinal Group NV
> Aurelia Holding NV bezit 80 % stemrechten in Brugse Brouwerij BV. Brugse bezit 60 % stemrechten in Cardinal Group NV. In elke schakel: exclusieve controle in rechte.
>
> 1. **Schema van de keten** 🌊
>
>    Aurelia Holding NV — 80 % stemrechten → Brugse Brouwerij BV — 60 % stemrechten → Cardinal Group NV
>    
>
> 2. **Berekening controlepercentage Aurelia in Cardinal** 🧮
>
>    Stap a: heeft Aurelia exclusieve controle over Brugse? 80 % > 50 % → ja.
>    Stap b: Brugse bezit 60 % in Cardinal → exclusieve controle over Cardinal.
>    Stap c: controlepercentage Aurelia in Cardinal = 60 % (niet vermenigvuldigen — elke schakel heeft exclusieve controle, dus het volledige stemrechtpercentage van de onderste schakel telt mee).
>    
>

**Grondslag**: [[controlepercentage]] §berekening, WVV art. 1:14 e.v.

> [!warning]- Het controlepercentage wordt NIET vermenigvuldigd langs de keten.
>
> _Vaak fout gedaan_: Controlepercentage doorheen de keten vermenigvuldigen, zoals het belangenpercentage.
>
> _Grondslag_: [[controlepercentage]] §rekenregel-keten

### 3. Berekenen van het belangenpercentage in elke schakel

Bepaal het economische eigendomsaandeel van de moeder in elke vennootschap door de belangenpercentages langs de keten te vermenigvuldigen.

**Waarom?** Het belangenpercentage bepaalt het pro-rata aandeel in eigen vermogen, resultaat en consolidatieverschil.

**📥 Input**:
- Werkpapier ketenstructuur → **Belangenpercentage per directe deelneming** _(percentage)_

**📤 Output**:
- Werkpapier per dochter → **Belangenpercentage moeder** _(percentage)_

**🛠️ Hoe**:

1. Voor de directe dochter: belangenpercentage = direct gehouden aandeel (Aurelia in Brugse = 80 %).
2. Voor een kleindochter: vermenigvuldig de belangenpercentages doorheen de keten. Belangenpercentage Aurelia in Cardinal = 80 % × 60 % = 48 %.
3. Het economische eigendomsaandeel verdunt door tussenliggende derden. Cardinal hoort voor 48 % economisch toe aan Aurelia, voor 52 % aan derden.
4. Gebruik dit getal in de berekening van aandeel van derden bij integrale consolidatie (zie [[uitvoeren-intragroep-eliminaties]] stap 7).


> [!example]- Voorbeeld: Zelfde keten als stap 2: Aurelia 80 % → Brugse 60 % → Cardinal
> Zelfde keten als stap 2: Aurelia 80 % → Brugse 60 % → Cardinal.
>
> 1. **Berekening belangenpercentage Aurelia in Cardinal** 🧮
>
>    belangenpercentage Aurelia in Cardinal = belang Aurelia in Brugse × belang Brugse in Cardinal
>                                            = 80 % × 60 %
>                                            = **48 %**
>    Derden hebben dus 100 % − 48 % = **52 %** economisch belang in Cardinal.
>    
>

**Grondslag**: [[belangenpercentage]] §berekening-keten

> [!warning]- Belangenpercentage WEL vermenigvuldigen, controlepercentage NIET.
>
> _Vaak fout gedaan_: Aannemen dat belangenpercentage en controlepercentage altijd gelijk zijn.
>
> _Grondslag_: [[belangenpercentage]] §onderscheid-controle

### 4. Toetsen of er in elke schakel exclusieve controle bestaat

Ga schakel per schakel na of de tussenschakel exclusieve controle uitoefent.

**Waarom?** Bij een breuk in de controle-keten geldt het 'volledig meetellen' niet meer en moet je opnieuw kwalificeren.

**📥 Input**:
- Werkpapier ketenstructuur → **Stemrechtpercentage en kwalitatieve aanwijzingen per schakel** _(document)_

**📤 Output**:
- Werkpapier per schakel → **Ja/nee exclusieve controle + gevolg voor keten** _(conclusie)_

**🛠️ Hoe**:

1. Toets per schakel aan de criteria uit [[exclusieve-controle]] §controle-in-rechte en §controle-in-feite.
2. > 50 % stemrechten? → exclusieve controle in rechte.
3. ≤ 50 % stemrechten maar onweerlegbare vermoedens of controle-in-feite? → exclusieve controle toch.
4. Geen controle? → de keten breekt. Op die schakel begint een nieuwe kwalificatie (mogelijk gezamenlijke controle of invloed van betekenis).
5. Bij een breuk: stap 2 en 3 moeten opnieuw worden uitgevoerd vanaf het breukpunt.


**Grondslag**: [[exclusieve-controle]] §keten-breuk

### 5. Toepassen van het belangenpercentage in de consolidatieverwerking

Gebruik het belangenpercentage als rekenmaatstaf voor de bedragen in de geconsolideerde jaarrekening.

**Waarom?** Het belangenpercentage is de basis voor aandeel van derden, pro-rata aandeel in eigen vermogen en pro-rata-opname bij evenredige consolidatie.

**📥 Input**:
- Belangenpercentage per dochter (uit stap 3) → **Percentage** _(percentage)_
- Cijfers van de dochter → **Eigen vermogen, resultaat, balansposten** _(boekhoudkundig-bedrag)_

**📤 Output**:
- Geconsolideerde jaarrekening → **Aandeel van derden, pro-rata opname, pro-rata aandeel EV** _(nieuwe-balanspost)_

**🛠️ Hoe**:

1. Bij integrale consolidatie: bereken aandeel van derden = (1 − belangenpercentage) × eigen vermogen dochter. Zie [[uitvoeren-intragroep-eliminaties]] stap 7.
2. Bij evenredige consolidatie: neem activa en passiva op voor belangenpercentage × bedrag dochter. Geen aandeel van derden.
3. Bij vermogensmutatie: bereken pro-rata aandeel in EV = belangenpercentage × eigen vermogen geassocieerde op aankoopdatum.
4. Documenteer de toegepaste rekenmaatstaf in het werkpapier.


**Grondslag**: [[belangenpercentage]] §toepassing, KB WVV art. 3:137 en 3:141


## Voorbeelden

> [!example]- Aurelia Holding NV bezit 80 % van Brugse Brouwerij BV. Brugse bezit 60 % van Cardinal Group NV
> **Conclusie**: Controlepercentage Aurelia in Cardinal = 60 % (NIET vermenigvuldigen — elke schakel heeft exclusieve controle). Belangenpercentage Aurelia in Cardinal = 0,80 × 0,60 = 48 %.
>
> **Grondslag**: [[controlepercentage]] §keten; [[belangenpercentage]] §keten
>
> **Redenering**: Controlepercentage en belangenpercentage volgen verschillende rekenregels. Aurelia consolideert Cardinal integraal omdat zij via Brugse exclusieve controle uitoefent. Het aandeel van derden (52 %) wordt afgezonderd op basis van het belangenpercentage.

> [!example]- Aurelia Holding NV bezit 90 % van Brugse Brouwerij BV. Brugse heeft een industriële activiteit
> **Conclusie**: Belangenpercentage Aurelia in Brugse = 90 %. Aandeel van derden = (1 − 0,90) × € 2.000.000 = € 200.000 (op de balans), en (1 − 0,90) × resultaat Brugse (resultatenrekening).
>
> **Grondslag**: [[belangenpercentage]] §berekening-aandeel-van-derden; [[minderheidsbelangen]] §formule
>
> **Redenering**: Bij integrale consolidatie wordt 100 % van Brugse opgenomen. Het complement van het belangenpercentage bepaalt het deel dat als 'belangen van derden' wordt afgezonderd.


## Gebaseerd op concepten

[[controlepercentage]] · [[belangenpercentage]] · [[exclusieve-controle]] · [[controle]]
## Voortkomend uit

- **Taken**: 1.4.taak.1
- **Kenniselementen**: 1.4.I.C, 1.4.I.D, 1.4.I.E
