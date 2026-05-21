---
title: Verbonden partijen
tags:
- concept
- po-1-1
- po-1-6
- po-2-3
- po-2-8
linked_anchors:
- 1.1.II.R
- 1.6.II.A
- 1.6.II.B
- '2.3'
- '2.8'
programmaonderdelen:
- '1.1'
- '1.6'
- '2.3'
- '2.8'
confidence: grounded
node_type: ''
status: draft
schema_version: '2.0'
gegenereerd_uit: data/concepten/records/verbonden-partijen.json
gegenereerd_op: '2026-05-21'
---
# Verbonden partijen ⚖️

> [!summary] Korte inhoud
> {'tekst': 'Een verbonden partij is een natuurlijke persoon of entiteit die door zeggenschap, gezamenlijke zeggenschap, invloed van betekenis of een andere band van wederzijdse afhankelijkheid een relatie heeft met de verslaggevende entiteit die de onafhankelijkheid van hun transa….

{'tekst': 'Een verbonden partij is een natuurlijke persoon of entiteit die door zeggenschap, gezamenlijke zeggenschap, invloed van betekenis of een andere band van wederzijdse afhankelijkheid een relatie heeft met de verslaggevende entiteit die de onafhankelijkheid van hun transacties beïnvloedt of kan beïnvloeden.', 'confidence': 'grounded', 'bron': {'type': 'wettekst', 'ref': 'IAS-24#art-9'}}




## Voorkennis & leespad

- **Lees eerst** (voorvereisten):
  [[jaarrekening]]
  [[toelichting-jaarrekening]]
  [[consolidatie-grondslagen]]
  [[groep-van-beperkte-omvang]]

- **Naast deze fiche relevant**:
  [[transfer-pricing]]
  [[abnormale-goedgunstige-voordelen]]
  [[intragroep-eliminaties]]
  [[risicoanalyse-audit]]
  [[fraude]]

- **Bij vervolgvragen**:
  [[verbonden-partijen-procedure-genoteerd]]
  [[deelnemingen]]




## Rol van de accountant

### 

#### boekhouder

##### Stap 1 — verbonden partijen inventariseren 🔗

Begin van het boekjaar: bestuursorgaan vraagt wie de verbonden partijen zijn (aandeelhouders ≥ 20 %, gecontroleerde vennootschappen, familieleden in key management). Bewaar de lijst als werkdocument.


##### Stap 2 — toelichting samenstellen (BGAAP verkort/volledig schema) ⚖️

Kleine vennootschappen (verkort schema): geen aparte VP-staat verplicht. Grote of genoteerde vennootschappen: staat met per-categorie-informatie verplicht.

_Bron: {'type': 'cbn', 'ref': 'CBN-advies-2010-1'}_

##### Rekening-courant met verbonden partij — boekhoudkundige verwerking ⚖️

Rekening-courant (RC) tussen aandeelhouder en vennootschap is een technisch instrument voor kasverkeer maar ook een potentieel VP-risico. Classificeer correct op balans: vorderingen op meer dan één jaar (rek. 28x) of op korte termijn (rek. 40x / 44x). Rente is verplicht te markeren als marktconform of niet-marktconform.

_Bron: {'type': 'wettekst', 'ref': 'WVV-KB#art-3-37'}_

| Rekening | Naam | Debet | Credit |
|---:|---|---:|---:|
| 550 | Bankrekening | 50000 | — |
| 4890 | Schulden aan verbonden partijen (< 1 jaar) | — | 50000 |



#### fiscaal-adviseur

##### Art. 26 WIB92 — abnormale of goedgunstige voordelen ⚖️

Wanneer een in België gevestigde onderneming een abnormaal of goedgunstig voordeel verleent aan een verbonden partij (band van wederzijdse afhankelijkheid), wordt dit voordeel bij haar eigen winst gevoegd — tenzij het voordeel al belastbaar is bij de ontvanger.

_Bron: {'type': 'wettekst', 'ref': 'WIB92#art-26'}_



##### Transfer pricing — arm's length-principe voor internationale groepen 🔗

Voor internationale groepen: intercompany-transacties (goederen, diensten, IP, financiering) moeten plaatsvinden tegen arm's length-prijzen. België past dit toe via WIB92 art. 185 §2 (correctie bij abnormale voordelen naar buitenlandse groepsleden) en de verplichting tot transfer-pricing-documentatie (CbCR, master file, local file) voor grote groepen.

_Bron: [{'type': 'wettekst', 'ref': 'WIB92#art-185-2'}]_



### 

#### boekhouder

##### Intragroep-transacties in consolidatie ⚖️

In de geconsolideerde jaarrekening worden intragroep-transacties en saldi geëlimineerd (IAS 24 par. 4 + IFRS 10). De geconsolideerde toelichting vermeldt nog wel transacties met buiten de consolidatiekring vallende verbonden partijen (geassocieerde deelnemingen, joint ventures, sleutelfunctionarissen).

_Bron: {'type': 'wettekst', 'ref': 'IAS-24#par-4'}_



#### externe-auditor

##### ISA 550 — doelstellingen van de auditor ⚖️

ISA 550 par. 9: de auditor moet (a) voldoende inzicht verwerven in relaties en transacties met verbonden partijen om frauderisicofactoren te herkennen en te beoordelen of de financiële overzichten een getrouw beeld geven; en (b) als het verslaggevingsstelsel VP-vereisten bevat: voldoende en geschikte controle-informatie verzamelen dat VP-relaties en -transacties correct zijn aangewezen, verwerkt en toegelicht.

_Bron: {'type': 'norm', 'ref': 'ISA-550#par-9'}_



##### Risico-inschattingswerkzaamheden VP (ISA 550 par. 11-17) ⚖️

De auditor voert specifieke procedures uit om inzicht te verwerven in VP-relaties.

_Bron: {'type': 'norm', 'ref': 'ISA-550#par-11-17'}_


##### VP-transacties als fraude-vehicle — rode vlaggen ⚖️

ISA 550 par. 5-7: verbonden partijen bieden meer gelegenheid tot samenspanning, verhulling of manipulatie. De auditor behandelt aangewezen significante transacties buiten de normale bedrijfsvoering als indicator voor een significant risico op fraude.

_Bron: {'type': 'norm', 'ref': 'ISA-550#par-5-7'}_

##### Evaluatie administratieve verwerking en toelichting (ISA 550 par. 25) ⚖️

De auditor evalueert of geïdentificeerde VP-relaties en -transacties correct zijn opgenomen in de financiële overzichten conform het van toepassing zijnde verslaggevingsstelsel (BGAAP of IFRS).

_Bron: {'type': 'norm', 'ref': 'ISA-550#par-25'}_



##### Communicatie met governance (ISA 550 par. 27) ⚖️

Significante bevindingen over VP-transacties (ontdekte niet-gemelde VP's, fraude-indicatoren, materiële toelichting-tekortkomingen) worden meegedeeld aan de met governance belaste personen.

_Bron: {'type': 'norm', 'ref': 'ISA-550#par-27'}_



### 

#### begeleider

##### Belangenconflict bestuurder NV (WVV art. 7:96) ⚖️

Wanneer een bestuurder van een NV een rechtstreeks of onrechtstreeks belang heeft dat strijdig is met het vennootschapsbelang bij een bestuursbeslissing: (1) melding aan andere bestuurders vóór besluit; (2) verklaring in notulen; (3) omschrijving in jaarverslag of bijlage bij neerlegging jaarrekening; (4) commissaris beoordeelt vermogensrechtelijke gevolgen in afzonderlijke sectie van zijn verslag; (5) bestuurder met conflict neemt niet deel aan beraadslagingen of stemming.

_Bron: {'type': 'wettekst', 'ref': 'WVV#art-7-96'}_





## Veelvoorkomende verwarringen

###  ⚖️



###  🔗



###  ⚖️



###  ⚖️





## Wat dit record dekt

### Behandelde competenties (chronologisch)

1. **Identificeren wie een verbonden partij is (BGAAP vs IFRS vs fiscaal)** — zie [Identificeren wie een verbonden partij is (BGAAP vs IFRS vs fiscaal)](#definitie-verbonden-partij-kaderschema)2. **VP-inventaris opstellen bij begin van een opdracht** — zie [VP-inventaris opstellen bij begin van een opdracht](#boekhouder-kmo-identificatie)3. **Toelichtingsstaat VP-transacties samenstellen (BGAAP, groot schema)** — zie [Toelichtingsstaat VP-transacties samenstellen (BGAAP, groot schema)](#toelichtings-eisen-bgaap)4. **RC-aandeelhouder correct boekhoudkundig en fiscaal kwalificeren** — zie [RC-aandeelhouder correct boekhoudkundig en fiscaal kwalificeren](#boekhouder-kmo-rc-verwerking)5. **Art. 26 WIB92 toepassen — abnormale voordelen toevoegen aan winst** — zie [Art. 26 WIB92 toepassen — abnormale voordelen toevoegen aan winst](#fiscaal-art26-wib92)6. **Risico-inschattingswerkzaamheden VP uitvoeren (ISA 550 par. 11-17)** — zie [Risico-inschattingswerkzaamheden VP uitvoeren (ISA 550 par. 11-17)](#auditor-isa550-risico-inschattingsprocedures)7. **Rode vlaggen bij VP-transacties herkennen en auditreactie bepalen** — zie [Rode vlaggen bij VP-transacties herkennen en auditreactie bepalen](#auditor-isa550-fraude-risico)8. **Evalueren of VP-toelichting volledig en correct is** — zie [Evalueren of VP-toelichting volledig en correct is](#auditor-isa550-evaluatie-toelichting)9. **Belangenconflict-procedure bestuurder NV begeleiden (WVV art. 7:96)** — zie [Belangenconflict-procedure bestuurder NV begeleiden (WVV art. 7:96)](#vennootschapsrecht-belangenconflict-nv)
### Behandelde termen (alfabetisch)

- **arm's length** — zie [↑](#toelichtings-eisen-bgaap)- **abnormale voordelen** — zie [↑](#fiscaal-art26-wib92)- **band van wederzijdse afhankelijkheid** — zie [↑](#fiscaal-art26-wib92)- **bestuurder-transactie** — zie [↑](#vennootschapsrecht-belangenconflict-nv)- **commissaris-verslag VP** — zie [↑](#auditor-isa550-governance-communicatie)- **consortium** — zie [↑](#definitie-verbonden-partij-kaderschema)- **controlebevoegdheid** — zie [↑](#definitie-verbonden-partij-kaderschema)- **fraude-vehicle VP** — zie [↑](#auditor-isa550-fraude-risico)- **geassocieerde deelneming** — zie [↑](#definitie-verbonden-partij-kaderschema)- **goedgunstige voordelen** — zie [↑](#fiscaal-art26-wib92)- **IAS 24** — zie [↑](#toelichtings-eisen-ifrs)- **ISA 550** — zie [↑](#auditor-isa550-doelstellingen)- **invloed van betekenis** — zie [↑](#definitie-verbonden-partij-kaderschema)- **joint venture** — zie [↑](#definitie-verbonden-partij-kaderschema)- **marktconformiteitstoets** — zie [↑](#verwarring-arm-length-bewering)- **rekening-courant aandeelhouder** — zie [↑](#boekhouder-kmo-rc-verwerking)- **significante transactie buiten normale bedrijfsvoering** — zie [↑](#auditor-isa550-risico-inschattingsprocedures)- **sleutelfunctionarissen (key management)** — zie [↑](#definitie-verbonden-partij-kaderschema)- **transfer pricing** — zie [↑](#fiscaal-transfer-pricing)- **verbonden vennootschap (WVV art. 1:20)** — zie [↑](#definitie-verbonden-partij-kaderschema)

