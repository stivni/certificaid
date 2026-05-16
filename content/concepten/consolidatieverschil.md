---
title: Consolidatieverschil
tags:
- concept
- fenomeen
- po-1-4
linked_anchors:
- 1.4.I.D
- 1.4.I.G
- 1.4.I.B
- 1.4.I.E
- 1.4.taak.1
programmaonderdelen:
- '1.4'
confidence: grounded
node_type: fenomeen
status: seed
schema_version: '1.4'
gegenereerd_uit: data/concepten/records/consolidatieverschil.json
gegenereerd_op: '2026-05-16'
---
# Consolidatieverschil ⚖️

> Het verschil dat bij de eerste consolidatie overblijft tussen (a) wat de moeder betaalde voor de aandelen van een dochter of geassocieerde onderneming en (b) haar pro-rata aandeel in het eigen vermogen van die onderneming op datum van aankoop — nadat je dat verschil zoveel mogelijk hebt toegerekend aan onder- of overgewaardeerde bezittingen en schulden. Wat dan nog overblijft, verschijnt in de geconsolideerde balans als 'Consolidatieverschillen': aan actiefzijde als het positief is, aan passiefzijde als het negatief is. Positieve consolidatieverschillen worden afgeschreven over hun vermoedelijke gebruiksduur.
>
> _Bron: KB WVV art. 3:130 jo. art. 3:131_


> [!summary] Korte definitie
> Het verschil dat bij de eerste consolidatie overblijft tussen (a) wat de moeder betaalde voor de aandelen van een dochter of geassocieerde onderneming en (b) haar pro-rata aandeel in het eigen vermogen van die onderneming op datum van aankoop — nadat je dat verschil zoveel mogelijk hebt toegerekend aan onder- of overgewaardeerde bezittingen en schulden.

> [!info] Behoort tot: [[integrale-consolidatie]]
## Bouwstenen

### Positief consolidatieverschil = goodwill ⚖️

Je betaalt meer voor de aandelen dan je pro-rata aandeel in het eigen vermogen van de dochter (na correctie voor stille meer- of minwaarden). Het positieve verschil komt aan actiefzijde van de geconsolideerde balans en wordt afgeschreven over de vermoedelijke gebruiksduur. Schrijf je af over meer dan vijf jaar? Dan moet je dat in de toelichting motiveren.

**Waarom?** De premie die de moeder boven op de boekwaarde betaalde, weerspiegelt economische waarde (klantenbestand, marktpositie, synergieën) die niet aan één concrete balanspost is toe te wijzen. Door dat residu op de balans te activeren en gespreid af te schrijven, vermijd je dat het hele bedrag de winst van het aankoopjaar onterecht zou drukken.

**Voorbeeld**: Aurelia betaalt 320 voor 80 % van Brugse; pro-rata EV = 240 en geen stille meerwaarden → positief consolidatieverschil = 80. Boeken aan actiefzijde, afschrijven over 5 jaar = 16 per jaar.

_Grondslag: KB WVV art. 3:131, § 1_

### Negatief consolidatieverschil = badwill ⚖️

Je betaalt minder dan je pro-rata aandeel in het eigen vermogen (na correctie). Het negatieve verschil komt aan passiefzijde. Het mag niet zomaar als winst worden geboekt. Uitzondering: als het negatieve verschil te verklaren is door een verwachte ongunstige resultaatsontwikkeling van de dochter, dan mag je het in resultaat opnemen naarmate die verwachte verliezen zich echt voordoen.

**Waarom?** Badwill wijst meestal op verborgen risico's (komende verliezen, schade-aansprakelijkheden) waar de koper rekening mee houdt. Het meteen als winst boeken zou een spookwinst opleveren; de wet koppelt de erkenning aan het effectief optreden van die verliezen.

**Voorbeeld**: Aurelia koopt 80 % van een verlieslatende Brugse voor 180; pro-rata EV = 240 → negatief consolidatieverschil = 60, geboekt aan passiefzijde. In jaar 1 boekt Brugse het verwachte verlies van 30; Aurelia mag 80 % × 30 = 24 uit het negatieve verschil in resultaat opnemen.

_Grondslag: KB WVV art. 3:131, § 2_

### Geen compensatie tussen verschillende dochters ⚖️

Positieve consolidatieverschillen bij dochter A en negatieve verschillen bij dochter B mag je niet tegen elkaar wegstrepen. Voor één en dezelfde dochter moeten positieve en negatieve verschillen wél worden gecompenseerd.

**Waarom?** Twee verschillende dochters zijn economisch los van elkaar; saldering zou een dochter met verborgen goodwill optisch laten verdwijnen achter de badwill van een andere dochter. Binnen één dochter daarentegen gaat het om hetzelfde economische geheel — daar is saldering juist verplicht.

**Voorbeeld**: Aurelia heeft een positief verschil van 80 bij Brugse en een negatief verschil van 40 bij Bouwwerf Beerse → beide afzonderlijk presenteren, niet salderen.

_Grondslag: KB WVV art. 3:130_

### Gedeeltelijke verkoop van aandelen ⚖️

Verkoopt de moeder een deel van haar aandelen in een dochter (buiten de consolidatiekring), dan boek je een evenredig stuk van het overblijvende consolidatieverschil af.

**Waarom?** Het consolidatieverschil hoort bij de aangehouden aandelen. Bij gedeeltelijke verkoop hoort dat verschil ook gedeeltelijk te verdwijnen, anders blijf je een goodwill aanhouden die niet meer correspondeert met je participatie.

**Voorbeeld**: Aurelia heeft een resterend positief consolidatieverschil van 60 op haar 80 %-belang in Brugse. Aurelia verkoopt de helft (40 %) aan een derde → 30 (= 60 × 40 %/80 %) van het consolidatieverschil wordt afgeboekt.

_Grondslag: KB WVV art. 3:132_


## Berekening

### Berekening van het consolidatieverschil bij eerste consolidatie

**Bruto-verschil (vóór toerekening)** 
```
bruto-verschil = aanschaffingswaarde aandelen − (belangenpercentage × eigen vermogen dochter op datum van aankoop)
```

| Symbool | Betekenis | Eenheid |
|---|---|---|
| `aanschaffingswaarde aandelen` | Wat de moeder betaalde voor de aandelen, inclusief eventueel meegerekende aankoopkosten | EUR |
| `belangenpercentage` | Aandeel van moeder in kapitaal dochter (zie [[belangenpercentage]]) | % |
| `eigen vermogen dochter op datum van aankoop` | Totaal eigen vermogen (kapitaal + reserves + overgedragen resultaat) van de dochter, op de aankoopdatum (niet op afsluitingsdatum) | EUR |

**Voorbeeld-invulling**: aanschaffingswaarde = 320; belangenpercentage Aurelia in Brugse = 80 %; EV Brugse op aankoopdatum = 300

```
320 − (80 % × 300) = 320 − 240 = 80
```

_Resultaat in EUR_
**Consolidatieverschil (residu na toerekening)** (volgt op: bruto-verschil)
```
consolidatieverschil = bruto-verschil − totaal toerekening aan stille meer-/minderwaarden
```

| Symbool | Betekenis | Eenheid |
|---|---|---|
| `bruto-verschil` | Resultaat van de eerste formule | EUR |
| `totaal toerekening` | Som van alle bedragen die toegerekend zijn aan onder- of overgewaardeerde bezittingen/schulden van de dochter (KB WVV art. 3:128 jo. art. 3:130, lid 1) | EUR |

**Voorbeeld-invulling**: bruto-verschil = 80; toerekening aan terreinen (onderwaardering) = 50

```
80 − 50 = 30 (positief → actiefzijde)
```

_Resultaat in EUR_
**Jaarlijkse afschrijving op positief consolidatieverschil** 
```
jaarlijkse afschrijving = positief consolidatieverschil / vermoedelijke gebruiksduur (in jaren)
```

| Symbool | Betekenis | Eenheid |
|---|---|---|
| `positief consolidatieverschil` | Het residu uit de vorige formule, wanneer positief | EUR |
| `vermoedelijke gebruiksduur` | Aantal jaren waarover de goodwill economisch nuttig blijft; >5 jaar vereist motivering in toelichting | jaar |

**Voorbeeld-invulling**: positief consolidatieverschil = 30; vermoedelijke gebruiksduur = 5 jaar

```
30 / 5 = 6 per jaar
```

_Resultaat in EUR_
*Je vergelijkt wat je betaalde met wat je economisch kreeg. Wat je betaalde is de aanschaffingswaarde van de aandelen; wat je kreeg is jouw aandeel in het eigen vermogen plus eventuele stille meer- of minderwaarden. Het residu is goodwill (of badwill).*

### . 

**Voorbeeld**: Aurelia Holding NV verwerft 100 % van Brugse Brouwerij BV voor 1.000. Eigen vermogen Brugse op datum van aankoop = 700. Aurelia stelt vast dat de terreinen van Brugse 150 ondergewaardeerd zijn t.o.v. werkelijke waarde.

```
Stap 1: aanschaffingswaarde = 1.000. Stap 2: pro-rata EV = 100 % × 700 = 700. Stap 3: bruto-verschil = 1.000 − 700 = 300. Stap 4: 150 wordt toegerekend aan de terreinen (geconsolideerde balans: terreinen +150). Stap 5: residu = 300 − 150 = 150. Geboekt als 'Consolidatieverschillen' (actiefzijde), afgeschreven volgens passend plan.
```

Resultaat: In de geconsolideerde balans wordt 150 als positief consolidatieverschil geboekt; de terreinen van Brugse Brouwerij BV worden voor 150 opgewaardeerd. Het positieve consolidatieverschil wordt bv. over 5 jaar afgeschreven (30 per jaar in de geconsolideerde resultatenrekening, afzonderlijke post bij bedrijfs- of financiële kosten — KB WVV art. 3:131).

## In de praktijk

### Consolidatieverschil bij vermogensmutatie {id="consolidatieverschil-bij-vermogensmutatie"}

Ook bij de vermogensmutatiemethode (geassocieerde onderneming) ontstaat een consolidatieverschil: het verschil tussen de boekwaarde van de deelneming en het pro-rata aandeel in het eigen vermogen — na toerekening aan onder-/overgewaardeerde posten — komt als positief of negatief consolidatieverschil. Dat verschil wordt apart bijgehouden (afzonderlijk van de hoofdpost 'Vennootschappen waarop vermogensmutatie is toegepast') en afgeschreven (CBN 2022/11). ⚖️

### Afzonderlijke post in de resultatenrekening {id="afzonderlijke-post-in-de-resultatenrekening"}

Afschrijvingen op positieve consolidatieverschillen verschijnen in de geconsolideerde resultatenrekening als afzonderlijke post (bedrijfs- of financiële kosten). Niet mengen met de gewone afschrijvingen op bestaande activa (KB WVV art. 3:131, § 1, lid 3). ⚖️


## Oorzaken

- Overpaid goodwill — de moeder betaalt een premie boven het pro-rata aandeel in het netto-actief van de dochter. Die premie reflecteert economische waarden die in de enkelvoudige jaarrekening van de dochter niet konden worden geactiveerd: verwachte synergieën, marktpositie, klantenbestand, merken, knowhow. Twee perspectieven van hetzelfde fenomeen: (a) prijsperspectief — wat de moeder bereid is te betalen bovenop de boekhoudkundige nettowaarde; (b) substantieperspectief — waarom die premie niet kan worden toegerekend aan specifieke activa of schulden (KB WVV art. 3:130, eerste lid: toerekening enkel 'voor zover mogelijk') en daarom in het residu blijft zitten. Het residu wordt aan actiefzijde geboekt als 'Consolidatieverschillen' en afgeschreven over de vermoedelijke gebruiksduur (KB WVV art. 3:131, § 1). De Europese Richtlijn 2013/34/EU art. 24, lid 3, c) duidt dit residu uitdrukkelijk als 'goodwill'. 🤖
- Activa van de dochter zijn boekhoudkundig ondergewaardeerd (bv. terreinen tegen historische kostprijs); de moeder betaalt de werkelijke waarde. Eerste stap (KB WVV art. 3:128): het verschil toerekenen aan die onder- of overgewaardeerde posten voor je het residu als consolidatieverschil boekt. ⚖️
- Verwachte ongunstige resultaatsontwikkeling — een aankoopprijs lager dan het netto-actief op aankoopdatum kan voortvloeien uit de verwachting van komende verliezen; dan ontstaat een negatief consolidatieverschil. ⚖️
- Schulden of voorzieningen van de dochter zijn boekhoudkundig overgewaardeerd (te hoge voorzieningen, te ruim ingeschatte schulden). KB WVV art. 3:130 bepaalt dat het verschil zoveel mogelijk wordt toegerekend aan bezittingen en schulden waarvan de waarde afwijkt van de boekwaarde. Een te hoog opgegeven schuld verlaagt na correctie het residu dat als consolidatieverschil overblijft. ⚖️

## Valkuilen

- ⚠️ Het verschil tussen aanschaffingswaarde en EV op aankoopdatum is niet meteen het consolidatieverschil. Eerst toerekenen aan onder-/overgewaardeerde bezittingen en schulden (KB WVV art. 3:128 jo. art. 3:130, lid 1); pas het residu na die toerekening wordt 'Consolidatieverschillen'. ⚖️
- ⚠️ Negatief consolidatieverschil mag niet 'gewoon' als winst worden geboekt. KB WVV art. 3:131, § 2 voorziet een resultaat-opname enkel als het negatief verschil te verklaren is door een verwachte ongunstige resultaatsontwikkeling — en dan slechts naarmate die ontwikkeling zich realiseert. ⚖️
- ⚠️ Aanvullende of uitzonderlijke afschrijvingen moeten worden geboekt zodra een gewijzigde economische context het niet langer rechtvaardigt het positieve consolidatieverschil tegen die waarde te behouden (KB WVV art. 3:131, § 1). ⚖️

## Zie ook

- **Getriggerd door**: [[eerste-consolidatie]]

## Bronnen

[^1]: `KB-WVV-2019__art_3_102`
[^2]: `KB-WVV-2019__art_3_103`
[^3]: `KB-WVV-2019__art_3_104`
[^4]: `CBN-2013-03-de-boekhoudkundige-verwerking-van-step-acquisitions-update__sec_voorbeeld-1`
[^5]: `Richtlijn-2013-34-EU__art_24__sub_lid1-lid14`
[^6]: `CBN-2022-11-vermogensmutatiemethode__sec_voorbeeld`
