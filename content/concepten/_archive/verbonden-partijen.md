---
title: Verbonden partijen
tags:
- concept
- po-1-1
- po-1-4
- po-1-6
- po-2-3
- po-2-8
- po-3-0
linked_anchors:
- 1.1.II.R
- 1.1.III.I
- 1.4.I.I
- 1.6.II.A
- 1.6.II.B
- '2.3'
- '2.8'
- 3.0.II
- 3.0.II.C
programmaonderdelen:
- '1.1'
- '1.4'
- '1.6'
- '2.3'
- '2.8'
- '3.0'
confidence: grounded
node_type: ''
status: draft
schema_version: '2.0'
gegenereerd_uit: data/concepten/records/verbonden-partijen.json
gegenereerd_op: '2026-05-21'
---
# Verbonden partijen ⚖️

> [!summary] Korte inhoud
> {'tekst': "Een verbonden partij is een persoon of entiteit die door zeggenschap, gezamenlijke zeggenschap, invloed van betekenis of een band van wederzijdse afhankelijkheid de tegenpartij van een transactie kan beinvloeden — waardoor die transactie niet automatisch tegen marktcon….

{'tekst': "Een verbonden partij is een persoon of entiteit die door zeggenschap, gezamenlijke zeggenschap, invloed van betekenis of een band van wederzijdse afhankelijkheid de tegenpartij van een transactie kan beinvloeden — waardoor die transactie niet automatisch tegen marktconforme voorwaarden tot stand komt. 'Verbonden partijen' is een cluster begrippen — verbonden vennootschap, geassocieerde vennootschap, consortium, sleutelfunctionarissen — met een gedeelde rechtvaardiging: transparantie naar gebruikers van de jaarrekening, bescherming van minderheidsaandeelhouders en bewaking van de economische substantie achter de cijfers.", 'confidence': 'grounded', 'bron': [{'type': 'wettekst', 'ref': 'WVV#art-1-20'}, {'type': 'wettekst', 'ref': 'IAS-24#par-9'}, {'type': 'wettekst', 'ref': 'WIB92#art-26'}]}




## Voorkennis & leespad

- **Lees eerst** (voorvereisten):
  [[jaarrekening]]
  [[toelichting-jaarrekening]]
  [[controle]]
  [[gezamenlijke-controle]]
  [[consortium]]

- **Past binnen kader**: [[consolidatie]]

- **Naast deze fiche relevant**:
  [[transfer-pricing]]
  [[abnormale-goedgunstige-voordelen]]
  [[intragroep-eliminaties]]
  [[horizontale-consolidatie]]
  [[controleverwerving-methodes]]
  [[deelnemingen]]
  [[risicoanalyse-audit]]
  [[fraude]]

- **Bij vervolgvragen**:
  [[verbonden-partijen-procedure-genoteerd]]
  [[consolidatieverplichting]]




## Rol van de accountant

### Kmo / familievennootschap (bgaap)

#### 📋 boekhouder

##### Stap 1 — VP-inventaris opstellen bij begin boekjaar 🔗

Beginpunt van elke opdracht. Bewaar werkdocument als 'VP-register' — geactualiseerd per boekjaar.


##### Stap 2 — toelichting samenstellen per groottecategorie ⚖️

Inhoud verschilt sterk per categorie. Kleine vennootschap = minimum; grote/genoteerde = volledige staat.

_Bron: {'type': 'cbn', 'ref': 'CBN-advies-2010-1'}_

##### Rekening-courant aandeelhouder — boekhoudkundige verwerking ⚖️

RC is een technisch instrument voor kasverkeer maar ook een veel-voorkomend VP-instrument. Classificeer correct + bewaak marktconforme rente.

_Bron: {'type': 'kb', 'ref': 'KB-WVV#art-3-37'}_

| Rekening | Naam | Debet | Credit |
|---:|---|---:|---:|
| 550 | Bankrekening | 50000 | — |
| 4890 | Schulden aan verbonden ondernemingen <= 1 jaar | — | 50000 |



#### 💰 fiscaal-adviseur

##### Art. 26 WIB92 — toepassing in praktijk ⚖️

Documentatieplicht bij elke transactie met verbonden onderneming. Marktconformiteits-bewijs moet bij onderzoek tegenstelbaar zijn.

_Bron: {'type': 'wettekst', 'ref': 'WIB92#art-26'}_


##### Transfer pricing — arm's length voor internationale groepen 🔗

Voor internationale groepen: intercompany-transacties tegen arm's length-prijzen (OESO-richtlijnen). Belgie past dit toe via WIB92 art. 185 § 2 (correctie abnormale voordelen naar buitenlandse groepsleden) + verplichting CbCR / master file / local file boven drempel.

_Bron: {'type': 'wettekst', 'ref': 'WIB92#art-185-2'}_



### Grote vennootschap / groep (bgaap of ifrs)

#### 📋 boekhouder

##### Intragroep-transacties in consolidatie ⚖️

In de geconsolideerde JR worden intragroep-transacties en saldi geelimineerd. Wat overblijft als VP-toelichting: transacties met partijen buiten de consolidatiekring (geassocieerde deelnemingen, joint ventures, sleutelfunctionarissen, niet-geconsolideerde groepsdelen).

_Bron: [{'type': 'wettekst', 'ref': 'IAS-24#par-4'}, {'type': 'kb', 'ref': 'KB-WVV#art-3-124'}]_





#### 🔍 externe-auditor

##### ISA 550 — kernverantwoordelijkheid auditor ⚖️

ISA 550 par. 9 vereist dat de auditor (a) voldoende inzicht verwerft in relaties en transacties met verbonden partijen om frauderisicofactoren te herkennen en (b) wanneer het verslaggevingsstelsel VP-vereisten bevat: voldoende geschikte controle-informatie verzamelt dat VP-relaties en -transacties correct zijn aangewezen, verwerkt en toegelicht.

_Bron: {'type': 'norm', 'ref': 'ISA-550#par-9'}_



##### Risico-inschattingswerkzaamheden VP (ISA 550 par. 11-17) ⚖️

_Bron: {'type': 'norm', 'ref': 'ISA-550#par-11-17'}_


##### VP-transacties als fraude-vehicle — rode vlaggen ⚖️

ISA 550 par. 5-7: VP-relaties bieden meer gelegenheid tot samenspanning, verhulling of manipulatie. Aangewezen significante transacties buiten normale bedrijfsvoering = indicator significant fraude-risico.

_Bron: {'type': 'norm', 'ref': 'ISA-550#par-5-7'}_

##### Evaluatie verwerking en toelichting (ISA 550 par. 25) ⚖️

_Bron: {'type': 'norm', 'ref': 'ISA-550#par-25'}_



##### Communicatie met governance (ISA 550 par. 27) ⚖️

_Bron: {'type': 'norm', 'ref': 'ISA-550#par-27'}_



### Vennootschapsrechtelijk — nv / bv (corporate governance)

#### begeleider

##### Belangenconflict bestuurder NV (WVV art. 7:96) ⚖️

Bestuurder met rechtstreeks of onrechtstreeks strijdig vermogensbelang bij een bestuursbeslissing: (1) meldplicht aan andere bestuurders voor besluit; (2) verklaring in notulen; (3) omschrijving in jaarverslag of bijlage neerlegging JR; (4) commissaris beoordeelt vermogensrechtelijke gevolgen in afzonderlijke sectie verslag; (5) betrokken bestuurder neemt geen deel aan beraadslaging of stemming.

_Bron: {'type': 'wettekst', 'ref': 'WVV#art-7-96'}_







## Veelvoorkomende verwarringen

###  ⚖️



###  ⚖️



###  🔗



###  ⚖️



###  ⚖️



###  ⚖️





## Wat dit record dekt

### Behandelde competenties (chronologisch)

1. **VP-cluster begrijpen: vier relatietypes, drie kaders, één rationale** — zie [VP-cluster begrijpen: vier relatietypes, drie kaders, één rationale](#cluster-elementen-overzicht)2. **Controle in rechte vs. in feite herkennen (WVV 1:14)** — zie [Controle in rechte vs. in feite herkennen (WVV 1:14)](#controle-juridisch-feitelijk)3. **Geassocieerd ↔ verbonden ↔ deelneming ↔ minoritair onderscheiden** — zie [Geassocieerd ↔ verbonden ↔ deelneming ↔ minoritair onderscheiden](#geassocieerd-vs-verbonden-vs-deelneming)4. **Marktconformiteits-test uitvoeren op een VP-transactie** — zie [Marktconformiteits-test uitvoeren op een VP-transactie](#marktconformiteits-test)5. **VP-inventaris opstellen bij begin van opdracht** — zie [VP-inventaris opstellen bij begin van opdracht](#boekhouder-kmo-identificatie)6. **Toelichtingsstaat VP-transacties opmaken per groottecategorie** — zie [Toelichtingsstaat VP-transacties opmaken per groottecategorie](#toelichtings-eisen-bgaap)7. **IFRS-toelichting per categorie (IAS 24 par. 19) opbouwen** — zie [IFRS-toelichting per categorie (IAS 24 par. 19) opbouwen](#toelichtings-eisen-ifrs)8. **RC-aandeelhouder correct boekhoudkundig en fiscaal kwalificeren** — zie [RC-aandeelhouder correct boekhoudkundig en fiscaal kwalificeren](#boekhouder-kmo-rc-verwerking)9. **Art. 26 WIB92 toepassen — abnormaal voordeel bijvoegen** — zie [Art. 26 WIB92 toepassen — abnormaal voordeel bijvoegen](#wib92-art-26-mechanisme)10. **Intragroep-eliminaties uitvoeren in geconsolideerde JR** — zie [Intragroep-eliminaties uitvoeren in geconsolideerde JR](#boekhouder-groep-consolidatie)11. **Risico-inschattingswerkzaamheden VP uitvoeren (ISA 550 par. 11-17)** — zie [Risico-inschattingswerkzaamheden VP uitvoeren (ISA 550 par. 11-17)](#auditor-isa550-risico-inschattingsprocedures)12. **Rode vlaggen bij VP-transacties herkennen en auditreactie bepalen** — zie [Rode vlaggen bij VP-transacties herkennen en auditreactie bepalen](#auditor-isa550-fraude-risico)13. **Evalueren of VP-toelichting volledig en correct is** — zie [Evalueren of VP-toelichting volledig en correct is](#auditor-isa550-evaluatie-toelichting)14. **Belangenconflict-procedure NV (7:96) toepassen** — zie [Belangenconflict-procedure NV (7:96) toepassen](#vennootschapsrecht-belangenconflict-nv)15. **VP-procedure genoteerde NV (7:97) herkennen en triggers identificeren** — zie [VP-procedure genoteerde NV (7:97) herkennen en triggers identificeren](#wvv-7-97-procedure-genoteerd)
### Behandelde termen (alfabetisch)

- **abnormale voordelen** — zie [↑](#wib92-art-26-mechanisme)- **arm's length** — zie [↑](#marktconformiteits-test)- **band van wederzijdse afhankelijkheid** — zie [↑](#wib92-art-26-mechanisme)- **belangenconflict (WVV 7:96)** — zie [↑](#vennootschapsrecht-belangenconflict-nv)- **bestuurder-transactie** — zie [↑](#vennootschapsrecht-belangenconflict-nv)- **commissaris-verslag VP** — zie [↑](#auditor-isa550-governance-communicatie)- **consortium** — zie [↑](#cluster-elementen-overzicht)- **controle in rechte / in feite** — zie [↑](#controle-juridisch-feitelijk)- **controlebevoegdheid** — zie [↑](#controle-juridisch-feitelijk)- **deelneming** — zie [↑](#geassocieerd-vs-verbonden-vs-deelneming)- **fraude-vehicle VP** — zie [↑](#auditor-isa550-fraude-risico)- **geassocieerde vennootschap** — zie [↑](#geassocieerd-vs-verbonden-vs-deelneming)- **gemeenschappelijke dochter** — zie [↑](#cluster-elementen-overzicht)- **goedgunstige voordelen** — zie [↑](#wib92-art-26-mechanisme)- **horizontale groep** — zie [↑](#cluster-elementen-overzicht)- **IAS 24** — zie [↑](#toelichtings-eisen-ifrs)- **intragroep-eliminatie** — zie [↑](#boekhouder-groep-consolidatie)- **invloed van betekenis** — zie [↑](#geassocieerd-vs-verbonden-vs-deelneming)- **ISA 550** — zie [↑](#auditor-isa550-doelstellingen)- **joint venture** — zie [↑](#toelichtings-eisen-ifrs)- **marktconforme transactie** — zie [↑](#marktconformiteits-test)- **marktconformiteits-bewering** — zie [↑](#verwarring-arms-length-bewering)- **minoritair belang** — zie [↑](#verwarring-verbonden-vs-geassocieerd)- **rekening-courant aandeelhouder** — zie [↑](#boekhouder-kmo-rc-verwerking)- **significante transactie buiten normale bedrijfsvoering** — zie [↑](#auditor-isa550-risico-inschattingsprocedures)- **sleutelfunctionarissen (key management)** — zie [↑](#cluster-elementen-overzicht)- **transfer pricing** — zie [↑](#fiscaal-transfer-pricing)- **ultieme controleerder (UBO)** — zie [↑](#controle-juridisch-feitelijk)- **verbonden onderneming (fiscaal)** — zie [↑](#wib92-art-26-mechanisme)- **verbonden vennootschap (WVV 1:20)** — zie [↑](#cluster-elementen-overzicht)- **VP-inventaris / VP-register** — zie [↑](#boekhouder-kmo-identificatie)

