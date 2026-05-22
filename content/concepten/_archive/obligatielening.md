---
title: Obligatielening
tags:
- concept
- concept
- po-1-1
- po-1-4
- po-1-7
- po-2-1
- po-2-3
- po-3-0
linked_anchors:
- 1.1.II.V
- 1.1.II.J
- 1.4.III.B
- 1.7.II.B
- 2.1.III.E
- 2.3.IV.C
- 3.0.II.A
programmaonderdelen:
- '1.1'
- '1.4'
- '1.7'
- '2.1'
- '2.3'
- '3.0'
confidence: grounded
node_type: concept
status: active
schema_version: '2.0'
gegenereerd_uit: data/concepten/records/obligatielening.json
gegenereerd_op: '2026-05-21'
---
# Obligatielening ⚖️

> [!summary] Korte inhoud
> Een **obligatielening** is een schuldfinanciering waarbij een vennootschap verhandelbare schuldbewijzen (obligaties) uitgeeft aan meerdere beleggers — in plaats van te lenen bij één bank.

Een **obligatielening** is een schuldfinanciering waarbij een vennootschap verhandelbare schuldbewijzen (obligaties) uitgeeft aan meerdere beleggers — in plaats van te lenen bij één bank. De vennootschap ontvangt het kapitaal bij uitgifte, betaalt jaarlijkse coupons (rente) tijdens de looptijd en betaalt het nominale bedrag terug op vervaldag.




## Voorkennis & leespad

- **Lees eerst** (voorvereisten):
  [[matching-beginsel]]
  [[oprichtingskosten]]
  [[jaarrekening-structuur]]

- **Past binnen kader**: [[lange-termijn-financiering]]

- **Naast deze fiche relevant**:
  [[banklening]]
  [[converteerbare-obligatie]]

- **Bij vervolgvragen**:
  [[winstdelende-lening]]
  [[achtergestelde-lening]]
  [[ebitda-regel-198-1]]



## Hoe het werkt


## Rol van de accountant

### Uitgever-vennootschap

#### 🎯 adviseur

##### Instrument-keuze vs alternatieven 🧭

Vergelijk obligatielening met banklening · achtergestelde lening · kapitaalverhoging op basis van looptijd-behoefte, cashflow-stabiliteit, schuldgraad. Stuur op werkelijke kost (YTM-niveau), niet op coupon alleen. Stress-test op coupon-verplichting over hele looptijd.

##### Structuur-advies 🧭

Vast vs variabele coupon · looptijd · agio/disagio of pari · call/put-clausules · sinking fund. Timing van uitgifte i.f.v. marktrente.

#### 📋 boekhouder

##### Bij uitgifte (T₀) — variant pari ⚖️

Cash ontvangen = nominale schuld. Eén boeking voor de hoofdsom, een aparte voor de uitgiftekosten (op rekening 201 — oprichtingskosten — onder de uitzondering van art. 3:37 KB-WVV).

_Bron: [{'type': 'advies', 'ref': 'CBN-2019-07'}]_

| Rekening | Naam | Debet | Credit |
|---:|---|---:|---:|
| 5500 | Kredietinstellingen — R/C | 1000000 | — |
| 1711 | Niet-achtergestelde, niet-converteerbare obligatieleningen | — | 1000000 |

| Rekening | Naam | Debet | Credit |
|---:|---|---:|---:|
| 201 | Kosten bij uitgifte van leningen | 12000 | — |
| 5500 | Kredietinstellingen — R/C | — | 12000 |

##### Bij uitgifte (T₀) — variant disagio ⚖️

Schuld wordt op balans tegen nominale (terugbetalings-)waarde geboekt; het verschil tussen ontvangen cash en nominale waarde wordt geactiveerd als over te dragen kost en *prorata temporis* in resultaat genomen (art. 3:51 KB-WVV).

_Bron: [{'type': 'kb', 'ref': 'KB-WVV#art-3-51'}, {'type': 'advies', 'ref': 'CBN-2019-07'}]_

| Rekening | Naam | Debet | Credit |
|---:|---|---:|---:|
| 5500 | Kredietinstellingen — R/C | 950000 | — |
| 4901 | Over te dragen kosten — disagio | 50000 | — |
| 1711 | Niet-achtergestelde, niet-converteerbare obligatieleningen | — | 1000000 |

##### Bij uitgifte (T₀) — variant agio ⚖️

Schuld blijft tegen nominale waarde op balans; het verschil (premium) wordt over de looptijd opgenomen als opbrengst die de werkelijke couponlast verlaagt.

_Bron: [{'type': 'kb', 'ref': 'KB-WVV#art-3-51'}, {'type': 'advies', 'ref': 'CBN-2019-07'}]_

| Rekening | Naam | Debet | Credit |
|---:|---|---:|---:|
| 5500 | Kredietinstellingen — R/C | 1050000 | — |
| 1711 | Niet-achtergestelde, niet-converteerbare obligatieleningen | — | 1000000 |
| 4902 | Over te dragen opbrengsten — agio | — | 50000 |

##### Balans-snapshot — direct na uitgifte (variant disagio) 🔗

_Bron: [{'type': 'advies', 'ref': 'CBN-2019-07'}]_



##### Jaarlijks — coupon · prorata · spreiding · afschrijving uitgiftekosten ⚖️

Vier boekingen per jaar (variant disagio): cash coupon op coupondatum, prorata op balansdatum, disagio-amortisatie (lineair) en afschrijving uitgiftekosten over de looptijd.

_Bron: [{'type': 'advies', 'ref': 'CBN-2019-07'}, {'type': 'kb', 'ref': 'KB-WVV#art-3-51'}]_

| Rekening | Naam | Debet | Credit |
|---:|---|---:|---:|
| 6500 | Rente, commissies en kosten verbonden aan schulden | 30000 | — |
| 5500 | Kredietinstellingen — R/C | — | 30000 |

| Rekening | Naam | Debet | Credit |
|---:|---|---:|---:|
| 6500 | Rente, commissies en kosten verbonden aan schulden | 15000 | — |
| 492 | Toe te rekenen kosten | — | 15000 |

| Rekening | Naam | Debet | Credit |
|---:|---|---:|---:|
| 6500 | Rente, commissies en kosten verbonden aan schulden — disagio | 10000 | — |
| 4901 | Over te dragen kosten — disagio | — | 10000 |

| Rekening | Naam | Debet | Credit |
|---:|---|---:|---:|
| 6501 | Afschrijving van kosten bij uitgifte van leningen | 2400 | — |
| 201 | Kosten bij uitgifte van leningen | — | 2400 |

##### Op vervaldag (T₅) — terugbetaling nominaal ⚖️

_Bron: [{'type': 'advies', 'ref': 'CBN-2019-07'}]_

| Rekening | Naam | Debet | Credit |
|---:|---|---:|---:|
| 1711 | Niet-achtergestelde, niet-converteerbare obligatieleningen | 1000000 | — |
| 5500 | Kredietinstellingen — R/C | — | 1000000 |

##### Uitvoerings-valkuilen voor de boekhouder ⚖️

**Uitgiftekosten niet of niet correct spreiden** bij looptijd > 5 j → resultaat van jaar 1 vertekend; spreidingskeuze niet vermeld in toelichting (verplicht). **Agio/disagio niet spreiden** → resultaat van jaar 1 vertekend, art. 3:51 KB-WVV geschonden. **Prorata vergeten** → matching-beginsel gebroken. Bij **variabele coupon**: prorata herrekenen op basis van geldende rentevoet op balansdatum, niet op vorige coupon. Bij **call-clausule activering**: premie boven pari is een kapitaalverlies, geen rentekost.

_Bron: [{'type': 'kb', 'ref': 'KB-WVV#art-3-37'}, {'type': 'kb', 'ref': 'KB-WVV#art-3-51'}]_

#### begeleider

##### Stappenplan bij uitgifte 🔗

De accountant begeleidt typisch de boekhoudkundige en fiscale aspecten; notaris en bank verzorgen de juridische uitgifte. Het is nuttig de volledige sequentie te kennen.

_Bron: [{'type': 'wettekst', 'ref': 'WVV#art-7-63'}, {'type': 'wettekst', 'ref': 'WVV#art-7-161'}]_

1. Voorbereiding — bestuur analyseert financieringsbehoefte; prospectus of informatienota opgesteld door bank/advocaat; accountant levert financiële paragrafen.
2. Besluit bestuursorgaan — formeel goedgekeurd voorstel met nominaal, coupon, looptijd, agio/disagio en aflossingsmodaliteiten.
3. Publicatie en plaatsing — bekendmaking in Belgisch Staatsblad bij publieke uitgifte; plaatsing bij beleggers via bank-syndicaat.
4. Ontvangst kapitaal en uitgifteboeking — zie Boekhouder > Bij uitgifte (T₀).
5. Opzet spreidingstabel agio/disagio en uitgiftekosten; opzet prorata-aanslag in jaarafsluiting.
6. Eerste boekjaar: toelichting jaarrekening vermeldt spreidings- en waarderingskeuzes.
7. Jaarlijkse routine — coupon · prorata · spreiding · afschrijving.
8. Vervaldag — aflossing nominaal.

##### Formaliteiten — vergadering van obligatiehouders ⚖️

Bij **wijziging van voorwaarden** (uitstel, herstructurering, conversie) is een vergadering van obligatiehouders verplicht. De uitgiftevoorwaarden mogen niet afwijken van art. 7:175 en 7:176 WVV (dwingende beschermingsregels). Individuele renegotiatie per houder is niet mogelijk.

_Bron: [{'type': 'wettekst', 'ref': 'WVV#art-7-161'}]_

#### fiscaal

##### Aftrekbaarheid rentelasten (coupon + disagio-spreiding) ⚖️

Coupon + disagio-spreiding zijn aftrekbare beroepskosten in vennootschapsbelasting (art. 49 WIB92). Agio-opname vermindert symmetrisch de aftrekbare last (verschijnt als financiële opbrengst).

_Bron: [{'type': 'wettekst', 'ref': 'WIB92#art-49'}]_

##### Financieringskostensaldoregel (EBITDA-cap, art. 198/1 WIB92) ⚖️

Het **financieringskostensurplus** (netto-rentelasten − netto-renteopbrengsten) is niet aftrekbaar voor zover het het **grensbedrag** overschrijdt = max(30 % × fiscale EBITDA; € 3.000.000). Niet-aftrekbaar surplus is **overdraagbaar naar volgende boekjaren** (vrijgesteld via art. 194sexies WIB92, mits opgave bij de aangifte). Groepen kunnen via een **interestaftrekovereenkomst** ongebruikte aftrekcapaciteit overdragen tussen groepsvennootschappen.

_Bron: [{'type': 'wettekst', 'ref': 'WIB92#art-198-1'}, {'type': 'wettekst', 'ref': 'WIB92#art-194sexies'}, {'type': 'advies', 'ref': 'CBN-2020-06'}]_

grensbedrag = max(0,30 × fiscale EBITDA; € 3.000.000)

##### Roerende voorheffing bij uitbetaling coupon ⚖️

De vennootschap-uitgever is **schuldenaar van de roerende voorheffing** op de betaalde rente (art. 261, 1° WIB92). RV moet ingehouden en doorgestort worden, tenzij vrijstelling van toepassing is (art. 265 e.v. WIB92).

_Bron: [{'type': 'wettekst', 'ref': 'WIB92#art-261'}, {'type': 'wettekst', 'ref': 'WIB92#art-265'}]_

##### Toelichting jaarrekening — verplichte vermeldingen ⚖️

Vermelding obligatielening in toelichting bij rubriek 17; spreidingsmethode agio/disagio + uitgiftekosten in waarderingsregels; vervalkalender van de schuld; eventuele aftrek-beperking door art. 198/1 WIB92 met opgave bij aangifte.

_Bron: [{'type': 'kb', 'ref': 'KB-WVV#art-3-37'}, {'type': 'wettekst', 'ref': 'WIB92#art-194sexies'}]_

### Belegger-natuurlijke-persoon

#### 🎯 adviseur

##### Obligatie als beleggingscomponent 🧭

Risico/return-positie tussen liquide spaardeposito en aandelen; looptijd-matching met cashbehoefte; diversificatie t.o.v. aandelen.

#### fiscaal

##### Coupon = roerend inkomen (art. 17, §1, 2° en art. 19, 1° WIB92) ⚖️

De jaarlijkse coupon is **rente uit een schuldvordering** en kwalificeert als roerend inkomen voor de natuurlijke persoon. Belastbaar in PB; roerende voorheffing in principe **bevrijdend** wanneer correct ingehouden (art. 313 WIB92) — geen aangifteplicht in PB.

_Bron: [{'type': 'wettekst', 'ref': 'WIB92#art-17'}, {'type': 'wettekst', 'ref': 'WIB92#art-19'}, {'type': 'wettekst', 'ref': 'WIB92#art-313'}]_

##### Aangifteplicht — Vak VII PB (zonder of met onvolledige RV) ⚖️

**Verplicht aan te geven** in Vak VII rubriek A.2 van de aangifte PB: rente uit obligaties **zonder** ingehouden Belgische RV (typisch buitenlandse obligaties) of waarop een vrijstelling werd toegepast die de aangifte niet vervangt. Geen aangifte vereist als RV bevrijdend werkt.

_Bron: [{'type': 'wettekst', 'ref': 'WIB92#art-313'}, {'type': 'wettekst', 'ref': 'aangifte-PB-2025-roerende-inkomsten'}]_

##### Behandeling meerwaarde bij vervaldag (disagio-belegger) ⚠️

Verschil tussen aankoopprijs (bv. € 950) en terugbetaling op vervaldag (€ 1.000) — kwalificatie als belastbaar roerend inkomen of (vrijgestelde) meerwaarde hangt af van de houderschapsregeling en het onderscheid in art. 19 WIB92. **Te verifiëren** bij concrete dossiers.

### Belegger-vennootschap

#### 📋 boekhouder

##### Boeking belegging — rekening 51 'Vastrentende effecten' ⚖️

De belegger-vennootschap boekt de obligatie als vastrentend effect (rubriek 51). Let op: de MAR-benaming impliceert niet dat de coupon vast is — ook obligaties met variabele coupon staan op rubriek 51. Bij aankoop met disagio: schuld geboekt aan nominaal, verschil als over te dragen opbrengst, prorata in financiële opbrengsten genomen (spiegel van uitgever-zijde, art. 3:45 + 3:55 KB-WVV).

_Bron: [{'type': 'kb', 'ref': 'KB-WVV#art-3-45'}, {'type': 'kb', 'ref': 'KB-WVV#art-3-55'}]_

| Rekening | Naam | Debet | Credit |
|---:|---|---:|---:|
| 51 | Vastrentende effecten — nominaal | 1000 | — |
| 5500 | Kredietinstellingen — R/C | — | 950 |
| 4902 | Over te dragen opbrengsten (op belegging) | — | 50 |

| Rekening | Naam | Debet | Credit |
|---:|---|---:|---:|
| 4902 | Over te dragen opbrengsten (op belegging) | 10 | — |
| 750 | Opbrengsten uit vlottende activa | — | 10 |

#### fiscaal

##### Belastbaarheid coupon + spreiding in VenB 🔗

Coupons + amortisatie van disagio worden opgenomen als financiële opbrengsten in de winst, volledig belastbaar in vennootschapsbelasting (geen specifieke aftrek voor rente-opbrengsten).

_Bron: [{'type': 'wettekst', 'ref': 'WIB92#art-24'}]_

##### Geen DBI op rente (art. 202 WIB92) ⚖️

De DBI-aftrek (Definitief Belaste Inkomsten — uitsluiting van dubbele belasting) geldt **uitsluitend voor dividenden** en bepaalde gelijkgestelde inkomsten (art. 202, §1 WIB92 — uitputtende opsomming). Rente uit obligaties valt **niet** onder DBI en is gewoon belastbaar bij de ontvangende vennootschap, ongeacht wie de schuldenaar is.

_Bron: [{'type': 'wettekst', 'ref': 'WIB92#art-202'}]_

##### Symmetrische cap voor de belegger-venn. (art. 198/1, §2 WIB92) ⚖️

Voor het financieringskostensurplus wordt **ook rente-opbrengst** in mindering gebracht (netto-financieringskostensurplus = rentelasten − renteopbrengsten). Een belegger-vennootschap met overwegend rente-opbrengsten heeft typisch geen surplus.

_Bron: [{'type': 'wettekst', 'ref': 'WIB92#art-198-1'}]_

### Auditor

#### controleur

##### Controle-aandachtspunten bij obligatielening ⚖️

**Spreidingsmethode** agio/disagio consistent toegepast over de jaren (wisselen tussen lineair en effective interest breekt consistency-beginsel). **Prorata-intrest** correct berekend op balansdatum. **Toelichting jaarrekening** volledig: spreidingskeuze + waarderingsregels + vervalkalender. **Financieringskostensaldoregel** correct toegepast (eventuele aftrek-beperking gerapporteerd met opgave). Bij **call-clausule activering**: premie correct als kapitaalverlies behandeld, niet als rentekost.

_Bron: [{'type': 'kb', 'ref': 'KB-WVV#art-3-37'}, {'type': 'kb', 'ref': 'KB-WVV#art-3-51'}, {'type': 'wettekst', 'ref': 'WIB92#art-198-1'}]_

##### Specifiek bij converteerbare obligaties (commissaris/bedrijfsrevisor-rol) ⚖️

Bij uitgifte van **converteerbare obligaties** vereist art. 7:180 WVV een verslag van de commissaris, bedrijfsrevisor of gecertificeerd accountant over de getrouwheid van de financiële en boekhoudkundige gegevens in het bestuursverslag. Voor *niet*-converteerbare obligaties is dit verslag niet vereist.

_Bron: [{'type': 'wettekst', 'ref': 'WVV#art-7-180'}]_


## Veelvoorkomende verwarringen

###  ⚖️



###  🔗



###  🔗



###  🔗



###  🔗



###  ⚖️





## Wat dit record dekt

### Behandelde competenties (chronologisch)

1. **Klant adviseren over keuze obligatielening vs alternatieven** — zie [Klant adviseren over keuze obligatielening vs alternatieven](#adviseur)2. **Stappen begeleiden bij uitgifte (besluit · prospectus · plaatsing · publicatie)** — zie [Stappen begeleiden bij uitgifte (besluit · prospectus · plaatsing · publicatie)](#begeleider)3. **Uitgifte boekhoudkundig verwerken (drie varianten + uitgiftekosten)** — zie [Uitgifte boekhoudkundig verwerken (drie varianten + uitgiftekosten)](#bij-uitgifte-t0)4. **Werkelijk rendement (YTM) berekenen bij agio/disagio** — zie [Werkelijk rendement (YTM) berekenen bij agio/disagio](#uitgifteprijs-pari-agio-disagio)5. **Jaarlijkse routine boekhoudkundig verwerken (coupon · prorata · spreiding · afschrijving)** — zie [Jaarlijkse routine boekhoudkundig verwerken (coupon · prorata · spreiding · afschrijving)](#jaarlijkse-routine)6. **Toelichting jaarrekening opstellen (spreidingskeuze + waarderingsregels)** — zie [Toelichting jaarrekening opstellen (spreidingskeuze + waarderingsregels)](#fiscaal-uitgever)7. **Fiscale gevolgen inschatten — uitgever (aftrekbaarheid + EBITDA-cap)** — zie [Fiscale gevolgen inschatten — uitgever (aftrekbaarheid + EBITDA-cap)](#fiscaal-uitgever)8. **Fiscale gevolgen inschatten — belegger NP (PB Vak VII, RV bevrijdend)** — zie [Fiscale gevolgen inschatten — belegger NP (PB Vak VII, RV bevrijdend)](#fiscaal-np)9. **Fiscale gevolgen inschatten — belegger-venn. (VenB belastbaar, geen DBI)** — zie [Fiscale gevolgen inschatten — belegger-venn. (VenB belastbaar, geen DBI)](#fiscaal-venn)10. **Terugbetaling op vervaldag boekhoudkundig verwerken** — zie [Terugbetaling op vervaldag boekhoudkundig verwerken](#terugbetaling-vervaldag)11. **Auditor-controle op spreidingsmethode + prorata + toelichting + EBITDA-cap** — zie [Auditor-controle op spreidingsmethode + prorata + toelichting + EBITDA-cap](#auditor)
### Behandelde termen (alfabetisch)

- **agio**- **bevrijdende roerende voorheffing**- **call-clausule**- **coupon**- **coupondatum**- **disagio**- **emissieprospectus**- **financieringskostensurplus**- **interestaftrekovereenkomst**- **nominale waarde (pari)**- **nulcoupon**- **prorata-intrest**- **put-clausule**- **sinking fund**- **stapcoupon**- **uitgiftekosten**- **vergadering van obligatiehouders**- **vervaldag**- **wanbetaling**- **werkelijk rendement (YTM)**
### Behandelde formules

- {'naam': 'Prorata-intrest', 'expressie': 'coupon × (dagen sinds laatste betaling / 365)'}
- {'naam': 'Werkelijke financieringskost bij disagio', 'expressie': '(coupon + lineaire amortisatie disagio) / ontvangen kapitaal'}
- {'naam': 'Werkelijke financieringskost bij agio', 'expressie': '(coupon − lineaire afname agio) / ontvangen kapitaal'}
- {'naam': 'Grensbedrag financieringskostensurplus (art. 198/1 WIB92)', 'expressie': 'max(0,30 × fiscale EBITDA; € 3.000.000)'}


