---
title: Eerste toepassing van IFRS (IFRS 1)
tags:
- concept
- cluster
- po-1-5
linked_anchors:
- 1.5.IV.A
- 1.5.IV
programmaonderdelen:
- '1.5'
confidence: grounded
node_type: cluster
status: seed
schema_version: '1.5'
gegenereerd_uit: data/concepten/records/ifrs-eerste-toepassing.json
gegenereerd_op: '2026-05-21'
---
# Eerste toepassing van IFRS (IFRS 1) ⚖️

> [!summary] Korte inhoud
> De **eerste toepassing van IFRS** is de eenmalige overgang waarbij een onderneming voor het eerst een jaarrekening uitbrengt met expliciete en onvoorwaardelijke verklaring van overeenstemming met de IFRSs.

> [!info] Specialisatie van: [[stelselwissel-jaarrekening]]

De **eerste toepassing van IFRS** is de eenmalige overgang waarbij een onderneming voor het eerst een jaarrekening uitbrengt met expliciete en onvoorwaardelijke verklaring van overeenstemming met de IFRSs. Op een vooraf bepaalde **datum van overgang naar IFRS** — de begindatum van de vergelijkende periode — stelt de onderneming een volledig IFRS-conforme openingsbalans op. Alle activa en verplichtingen worden geherwaardeerd, geherclassificeerd of opgenomen alsof IFRS altijd al gold; het verschil met de oude grondslagen wordt rechtstreeks in de ingehouden winsten geboekt.

_Bron: IFRS 1 alinea's 1-7_



## Berekening

### Procedure eerste toepassing IFRS — vijf stappen

### 1. Bepaal de datum van overgang naar IFRS

Identificeer (a) de eerste verslagperiode waarin je een volledig IFRS-conforme jaarrekening uitbrengt — bv. boekjaar 31 december 2027 — en (b) de begindatum van de daarbij gepresenteerde vergelijkende periode. Die laatste datum is je **datum van overgang naar IFRS**.

**Waarom?** IFRS vereist minstens één vergelijkbare periode. De openingsbalans op de overgangsdatum moet al volledig IFRS-conform zijn, anders is de vergelijking onmogelijk.

**📥 Input**:
- Beslissing tot IFRS-toepassing → **Eerste IFRS-verslagperiode** _(datum)_

**📤 Output**:
- IFRS-overgangsdossier → **Datum van overgang** _(datum)_

**🛠️ Hoe**:

1. Zelena Bio NV beslist begin 2027 om voor boekjaar eindigend 31 december 2027 voor het eerst IFRS-jaarrekening uit te brengen.
2. Vergelijkende periode = boekjaar 2026.
3. Begindatum vergelijkende periode = 1 januari 2026.
4. Datum van overgang naar IFRS = **1 januari 2026**.

**Grondslag**: IFRS 1 alinea 3 + 6 + voorbeeld in 'Achtergrond'-sectie

### 2. Stel het IFRS-openingsoverzicht op

Maak een balans (overzicht van de financiële positie) op de overgangsdatum die volledig voldoet aan IFRS — alsof je altijd al IFRS had toegepast. Vier acties: (a) activa/verplichtingen opnemen die IFRS vereist maar BE-GAAP niet had; (b) activa/verplichtingen NIET opnemen die BE-GAAP wel had maar IFRS niet toestaat; (c) herclassificeren waar IFRS een andere categorie gebruikt; (d) volgens IFRS-grondslagen waarderen.

**Waarom?** Het openingsoverzicht is je IFRS-vertrekpunt. Foute openingsbalans → alle volgende IFRS-cijfers fout.

**📥 Input**:
- Belgisch-GAAP-balans op overgangsdatum → **Alle activa en passiva** _(boekhoudkundig-bedrag)_
- IFRS-grondslagenkeuze → **Per categorie kostprijs of reële waarde** _(beleidskeuze)_

**📤 Output**:
- IFRS-openingsoverzicht financiële positie → **Balans per overgangsdatum** _(jaarrekening-overzicht)_

**🛠️ Hoe**:

1. Neem de Belgisch-GAAP-balans van Zelena Bio NV per 1 januari 2026: activa € 200.000.000, passiva € 75.000.000, eigen vermogen € 125.000.000.
2. Check categorie per categorie:
   - Onderzoekskosten € 2.500.000 (geactiveerd onder BE-GAAP): IFRS staat geen activering toe (IAS 38, art. 54) → **schrappen**, ingehouden winsten −€ 2.500.000.
   - Operationele leasing wagenpark: BE-GAAP toonde alleen leasebedrag als kost. IFRS 16 vereist gebruiksrecht-actief + leaseverplichting. → Berekenen en **opnemen**.
   - Goodwill uit acquisitie 2020: BE-GAAP schreef gestaag af; IFRS 3 → niet langer afschrijven maar jaarlijks toetsen op bijzondere waardevermindering (impairment).
3. Resultaat: nieuwe balans met IFRS-cijfers per 1 januari 2026.

**Grondslag**: IFRS 1 alinea 10 (vier acties)

### 3. Pas verplichte uitzonderingen en optionele vrijstellingen toe

IFRS 1 voorziet **verplichte uitzonderingen** op retroactieve toepassing (waar het niet wenselijk is een IFRS volledig terug te draaien — bv. eerdere schattingen, hedging-aanwijzingen, niet-beheersbelangen). Daarnaast biedt het **optionele vrijstellingen** (in bijlagen C tot en met E): je mág kiezen om bv. de reële waarde op de overgangsdatum als 'veronderstelde kostprijs' te gebruiken voor materiële vaste activa.

**Waarom?** Volledige retroactieve toepassing is praktisch onhaalbaar of zou misleidende resultaten geven (bv. herzien van schattingen achteraf met kennis van vandaag). De uitzonderingen vermijden dat probleem; de vrijstellingen geven een redelijke kostengrens.

**📥 Input**:
- IFRS 1 bijlage B (verplichte uitzonderingen) → **Toepasselijke uitzonderingen** _(regelset)_
- IFRS 1 bijlage D (vrijstellingen) → **Optionele vrijstellingen** _(regelset)_

**📤 Output**:
- IFRS-overgangsdossier → **Keuzen en motivering per actief/passief-categorie** _(beleidskeuze)_

**🛠️ Hoe**:

1. Zelena Bio's terreinen (boekwaarde Belgisch GAAP € 12.000.000, marktwaarde 1 januari 2026 € 18.000.000): de stagiair gebruikt de vrijstelling 'reële waarde als veronderstelde kostprijs' (D5) → terreinen op € 18.000.000 in IFRS-openingsbalans, herwaarderingsverschil € 6.000.000 in ingehouden winsten.
2. Schattingen van uitgestelde belastingen die in 2020 onder BE-GAAP werden gemaakt: NIET herzien (verplichte uitzondering — IFRS 1 alinea 14).
3. Documentatie: per gebruikte vrijstelling vermelden in de toelichting.

**Grondslag**: IFRS 1 alinea's 13-17 + bijlagen B, C, D, E

### 4. Verwerk het aanpassingsverschil in ingehouden winsten

Het verschil tussen de oude (BE-GAAP) en nieuwe (IFRS) balans op de overgangsdatum komt **rechtstreeks** in de ingehouden winsten — niet in winst of verlies. Latere boekjaren gebruiken de IFRS-cijfers als vertrekpunt.

**Waarom?** De aanpassing weerspiegelt feiten van vóór de overgangsdatum. Ze hoort niet thuis in het resultaat van de overgangsperiode, anders zou één jaar de last/baat dragen van een correctie die over jaren is opgebouwd.

**📥 Input**:
- BE-GAAP-balans op overgangsdatum → **Eigen vermogen** _(boekhoudkundig-bedrag)_
- IFRS-openingsbalans → **Eigen vermogen** _(boekhoudkundig-bedrag)_

**📤 Output**:
- IFRS-openingsbalans → **Ingehouden winsten (aangepast)** _(boekhoudkundig-bedrag)_

**🛠️ Hoe**:

1. Zelena Bio: eigen vermogen onder BE-GAAP per 1 januari 2026 = € 125.000.000.
2. Aanpassingen: schrap onderzoek −€ 2.500.000; opname leaseverplichting netto-effect −€ 4.000.000; reële-waarde-uplift terreinen +€ 6.000.000; impairment-correctie goodwill +€ 1.500.000; saldo = +€ 1.000.000.
3. Eigen vermogen onder IFRS per 1 januari 2026 = € 126.000.000.
4. Het verschil van € 1.000.000 boek je in 'Ingehouden winsten' van de IFRS-openingsbalans.

**Grondslag**: IFRS 1 alinea 11

### 5. Stel aansluiting + toelichting op

Vermeld in de eerste IFRS-jaarrekening: (a) aansluiting tussen BE-GAAP- en IFRS-eigen vermogen op zowel de overgangsdatum als de einddatum van de laatste BE-GAAP-jaarrekening; (b) aansluiting tussen BE-GAAP- en IFRS-totaalresultaat over de laatste BE-GAAP-periode; (c) als impairment voor het eerst is opgenomen of teruggenomen: extra IAS 36-informatie.

**Waarom?** Gebruikers van de jaarrekening (beleggers, analisten) moeten **traceerbaar** kunnen zien hoe de cijfers veranderden. De aansluiting voorkomt dat de overgang lijkt op een 'cijfermachine' zonder verklaring.

**📥 Input**:
- BE-GAAP-cijfers vorige periode → **Eigen vermogen + totaalresultaat** _(boekhoudkundig-bedrag)_
- IFRS-cijfers vergelijkende periode → **Eigen vermogen + totaalresultaat** _(boekhoudkundig-bedrag)_

**📤 Output**:
- Toelichting eerste IFRS-jaarrekening → **Aansluitingstabellen** _(toelichtingsnoot)_

**🛠️ Hoe**:

1. Maak een tabel met als startpunt: 'EV onder BE-GAAP per 1 januari 2026 = € 125.000.000'.
2. Per aanpassing één regel: 'Schrappen onderzoekskosten (IAS 38) −€ 2.500.000', 'Opname leaseverplichting netto (IFRS 16) −€ 4.000.000', etc.
3. Eindlijn: 'EV onder IFRS per 1 januari 2026 = € 126.000.000'.
4. Herhaal dezelfde oefening voor 31 december 2026 (de einddatum van de vergelijkende periode).
5. Doe een vergelijkbare oefening voor het totaalresultaat 2026 (BE-GAAP → IFRS).

> [!example]- Voorbeeld: Aansluiting eigen vermogen Zelena Bio NV per 1 januari 2026 (datum van overgang naar IFRS)
> Aansluiting eigen vermogen Zelena Bio NV per 1 januari 2026 (datum van overgang naar IFRS)
>
> 1. **Aansluitingstabel EV op overgangsdatum** 🧮
>
>    | Post                                                            | Bedrag (€)       |
>    |-----------------------------------------------------------------|-----------------:|
>    | Eigen vermogen volgens Belgisch GAAP (1 januari 2026)           |   125.000.000    |
>    | Schrappen geactiveerde onderzoekskosten (IAS 38 art. 54)        |    −2.500.000    |
>    | Opname gebruiksrecht wagenpark (IFRS 16) — actief +20.000.000   |                  |
>    |   minus leaseverplichting −24.000.000 → netto                   |    −4.000.000    |
>    | Reële waarde terreinen als veronderstelde kostprijs (IFRS 1 D5) |    +6.000.000    |
>    | Terugname jaarlijkse goodwill-afschrijving 2020-2025            |    +1.500.000    |
>    | **Eigen vermogen volgens IFRS (1 januari 2026)**                |  **126.000.000** |
>

**Grondslag**: IFRS 1 alinea's 23-25 (toelichting en aansluitingen)


## In de praktijk

<h3 id="wanneer-kom-je-dit-tegen">Wanneer kom je dit tegen?</h3>

> [!tip]- Wanneer kom je dit tegen?
> Bij een Belgische beursgenoteerde groep die voor het eerst een IFRS-geconsolideerde jaarrekening publiceert, bij een dochter die overstapt omdat de buitenlandse moeder IFRS rapporteert, of bij een onderneming die uit een IFRS-stelsel terugkeert naar BE-GAAP en later opnieuw overstapt. 🔗

<h3 id="wat-is-de-drie-perioden-presentatie">Wat is de drie-perioden-presentatie?</h3>

> [!tip]- Wat is de drie-perioden-presentatie?
> De eerste IFRS-jaarrekening toont drie balansen: de IFRS-openingsbalans op de overgangsdatum, de balans op het einde van de vergelijkende periode, en de balans op het einde van de eerste IFRS-verslagperiode. Voor een onderneming met boekjaar dat eindigt op 31 december 2027 betekent dat: balans 1 januari 2026 + balans 31 december 2026 + balans 31 december 2027. ⚖️

<h3 id="waarom-rechtstreeks-in-ingehouden-winsten">Waarom rechtstreeks in ingehouden winsten?</h3>

> [!tip]- Waarom rechtstreeks in ingehouden winsten?
> Het aanpassingsverschil tussen BE-GAAP en IFRS weerspiegelt feiten van vóór de overgangsdatum — vaak meerdere boekjaren oud. Het opvoeren via de winst-en-verliesrekening van het overgangsjaar zou dat ene jaar onterecht belasten of bevoordelen met correcties die over verschillende voorgaande jaren slaan. ⚖️


## Tijdlijn

| Stap | Termijn | Actor | Actie |
|---|---|---|---|
| Datum van overgang naar IFRS — IFRS-openingsbalans opstellen | Begindatum vergelijkende periode (typisch 1 januari Y−1) | Onderneming + IFRS-team | Volledige IFRS-openingsbalans opstellen, aanpassingen in ingehouden winsten |
| Vergelijkende verslagperiode — registreer alle transacties parallel onder IFRS | Eerste vergelijkende boekjaar (Y−1) | Onderneming | Schaduw-rapportering onder IFRS naast de wettelijke BE-GAAP-rapportering |
| Eerste IFRS-verslagperiode — publicatie eerste IFRS-jaarrekening | Eerste IFRS-boekjaar (Y) | Onderneming + commissaris | Publicatie eerste IFRS-jaarrekening met aansluitingstabellen + IAS 1 minimum drie balansen (Y, Y−1, openingsbalans Y−1) |

## Valkuilen

> [!warning]- Het aanpassingsverschil bij eerste toepassing gaat **niet** via winst of verlies maar rechtstreeks naar ingehouden winsten
> ⚠️ Het aanpassingsverschil bij eerste toepassing gaat **niet** via winst of verlies maar rechtstreeks naar ingehouden winsten. Wie dat fout doet, vervuilt het IFRS-resultaat van de overgangsperiode met correcties die feitelijk over alle voorgaande jaren slaan. ⚖️
>
> _Bron: IFRS 1 alinea 11_


> [!warning]- Eenmalige vrijstelling 'reële waarde als veronderstelde kostprijs' (IFRS 1 D5) mag alleen bij **eerste** toepassing worden gebruikt — niet l…
> ⚠️ Eenmalige vrijstelling 'reële waarde als veronderstelde kostprijs' (IFRS 1 D5) mag alleen bij **eerste** toepassing worden gebruikt — niet later. Een onderneming die de overgang miste, kan dat voordeel niet meer benutten. ⚖️
>
> _Bron: IFRS 1 bijlage D_


> [!warning]- Schattingen die op de overgangsdatum onder BE-GAAP gemaakt waren, mogen alleen herzien worden als er objectieve aanwijzingen waren dat de ou…
> ⚠️ Schattingen die op de overgangsdatum onder BE-GAAP gemaakt waren, mogen alleen herzien worden als er objectieve aanwijzingen waren dat de oude schatting fout was. Nieuwe informatie die ná de overgangsdatum kwam, gebruik je niet om de openingsbalans aan te passen — dat zou hindsight zijn (IFRS 1 alinea 14-15). ⚖️
>
> _Bron: IFRS 1 alinea 14-15_



## Zie ook

- **Getriggerd door**: [[verplichte-ifrs-eu-beursgenoteerden]]
- **Vereist kennis van**: [[jaarrekening-componenten-ifrs]]
- **Wordt voorondersteld in** (2): [[bepalen-toepasselijkheid-ifrs-belgie]] · [[uitvoeren-eerste-toepassing-ifrs]]- **Triggert** (1): [[verplichte-ifrs-eu-beursgenoteerden]]
> [!todo] Voorbeeld ontbreekt voor dit concept
> Een latere ENRICH-pass voegt een synthese-voorbeeld toe.

## Bronnen

[^1]: `IFRS-1-eerste-toepassing-van-international-financial-reporting-standards__sec_opname-en-waardering`
[^2]: `IFRS-1-eerste-toepassing-van-international-financial-reporting-standards__sec_presentatie-en-informatieverschaffing`
[^3]: `IFRS-1-eerste-toepassing-van-international-financial-reporting-standards__sec_doel`
[^4]: `EU-IFRS-verordening-1606-2002__art_1`
[^5]: `IFRS-1-eerste-toepassing-van-international-financial-reporting-standards__sec_toepassingsgebied`
