---
title: "Functiescheiding"
concept_type: "principe"
schema_version: "2.2"
status: "concept"
categorieen:
  - kader
ankers:
  - 1.7.VII
  - 1.7.VIII.B
  - 1.7.X.C
tags:
  - concept
  - schema-2.2
  - type-principe
  - cat-kader
  - status-concept
gegenereerd_uit: "data/concepten/records/functiescheiding.json"
---

_Principe_ · ook: segregation of duties · separation of duties · functie-onverenigbaarheid · rolscheiding · taakverdeling

## Definitie

Functiescheiding is het organisatorisch principe dat onverenigbare functies aan verschillende personen worden toegewezen, zodat geen enkele persoon alleen een volledige transactie kan initieren, uitvoeren, registreren en bewaren. Het doel is volgens ISA 315 (herzien-2019) Bijlage 3 om beperkingen aan te brengen in de mogelijkheden voor wie dan ook om bij de uitoefening van zijn normale taken fouten te maken en te verhullen of fraude te plegen en te verhullen. Klassiek voorbeeld: een manager die kredietverkopen autoriseert is niet verantwoordelijk voor het bijhouden van de vorderingenadministratie.

<small>📖 ISA 315 (herzien-2019) — Bijlage 3 - Functiescheiding — _norm_</small>

## Substantie

In de Belgische beroepspraktijk gebruikt men de zogenaamde ACR-IH-leer (Autoriseren, Uitvoeren, Registreren, Bewaren) - in het Engels ook Authorization, Custody, Record-keeping - waarbij de vuistregel is dat een persoon nooit meer dan twee niet-aangrenzende van deze vier functies mag combineren. Wie bijvoorbeeld een betaling autoriseert mag niet ook de boeking ervan registreren noch de bankrekening beheren. In de praktijk zit functiescheiding ingebed in autorisatie-instellingen in het ERP, in handtekenmandaten bij de bank en in de organisatie-structuur van de onderneming.

<small>🔗 ISA 315 (herzien-2019) — Bijlage 3 — _norm_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Rationale

Functiescheiding werkt op een dubbel principe: (1) preventie - het wordt fysiek moeilijker om fraude alleen uit te voeren omdat samenspanning met een collega nodig is, en collusie verhoogt het detectie-risico; (2) detectie - elke functie controleert impliciet de vorige, fouten worden eerder ontdekt. ISA 240 erkent collusie expliciet als een van de grondoorzaken die elke functiescheiding kan doorbreken - vandaar dat functiescheiding alleen onvoldoende is en altijd aangevuld moet worden met andere controles (autorisatie-limieten, monitoring, rotatie). Functiescheiding is ook expliciet voorzien voor accountantskantoren zelf in de antiwitwaswet (art. 9): twee functies per kantoor - hoogste verantwoordelijke en AMLCO.

<small>📖 ISA 240 — Toepassingsgerichte teksten A1 - kenmerken van fraude inclusief collusie — _norm_ · ITAA-Handleiding-interne-procedures-AWW-2019 — Art. 9 - twee functies per kantoor — _norm_</small>

## Gebruikscontext

**Status**: `in-voege`

Universeel principe, verankerd in ISA 315 Bijlage 3, in alle audit-handboeken, en wettelijk voor kantoren in antiwitwaswet 2017 art. 9.

**✅ Voor**
- 🔗 Bij het ontwerp van elke transactionele cyclus (aankoop, verkoop, voorraad, treasury, personeel) en bij het ontwerp van toegangsrechten in een informatica-systeem (Role-Based Access Control).

**🚫 Niet voor**
- 📖 In een kleine onderneming met een of twee werknemers is volledige functiescheiding onmogelijk. Daar geldt het compenserende-controles-principe: de eigenaar-zaakvoerder neemt persoonlijk de autorisatie- en monitoring-rol op zich; de externe accountant of boekhouder vervult een onafhankelijke detectie-rol via periodieke reviews.

**👍 Voordeel**
- 🔗 Sterke preventieve werking tegen interne fraude (vereist collusie) en tegen onopzettelijke fouten (volgende functie ontdekt). Erkende sleutelcontrole - externe auditors steunen graag op een goed werkende functiescheiding, wat de scope van gegevensgerichte werkzaamheden vermindert.

**⚠️ Risico**
- 📖 Pseudo-functiescheiding op papier maar niet in praktijk: een medewerker heeft formeel niet de bevoegdheid maar krijgt feitelijk het paswoord van een collega om snel iets te regelen. Collusie - twee of meer personen die samen frauderen - doorbreekt elke functiescheiding. Management override - de zaakvoerder die zijn eigen procedures negeert - is een specifiek risico in kmo's.

## Bouwstenen

### 💡 De vier onverenigbare functies (ACR-IH)

(A) Autoriseren - goedkeuring geven voor een transactie (bv. inkooporder goedkeuren, kredietverkoop autoriseren); (U) Uitvoeren - de feitelijke handeling stellen (bv. goederen bestellen, factuur betalen); (R) Registreren - de boeking in de administratie verwerken; (B) Bewaren - de fysieke of digitale activa beheren (bv. magazijnbeheer, kasbeheer, bankrekening). Een persoon mag maximaal twee niet-aangrenzende van deze vier functies cumuleren. ACR-IH staat voor de Engelse Authorization, Custody, Record-keeping waarbij in de Nederlandstalige opleiding Uitvoeren als vierde toegevoegd wordt.

<small>📖 ISA 315 (herzien-2019) — Bijlage 3 - autoriseren, registreren, bewaren — _norm_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### 🧭 Vuistregel: max twee niet-aangrenzende functies

Een persoon mag maximaal twee van de vier ACR-IH-functies cumuleren, en bij voorkeur twee die niet-aangrenzend zijn in de transactie-flow. Concreet onveilige combinaties: dezelfde persoon autoriseert + bewaart de activa (autorisatie zonder check op feitelijke output), of registreert + bewaart (kan eigen toe-eigening verbergen door wegmoffelen in administratie). Veilige combinatie: autoriseren + uitvoeren door dezelfde persoon (mits andere persoon de uitkomst registreert en bewaart).

<small>🔗 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### ⚙️ Toepassing aankoopcyclus

Klassieke functiescheiding in aankoop: aanvrager (behoefte uiten) <> goedkeurder (autorisatie) <> aankoper (bestellen) <> magazijnier (ontvangen) <> boekhouder (registreren) <> betaalverantwoordelijke (betalen). Bij een kmo worden deze rollen gegroepeerd maar de zaakvoerder houdt minstens de autorisatie- en betaalfunctie zelf. ERP-systemen zoals SAP, Microsoft Dynamics en Odoo implementeren dit via workflow-stappen waar elke stap door een andere user wordt afgevinkt.

<small>🔗 ISA 315 (herzien-2019) — Bijlage 3 — _norm_</small>

### ⚙️ Informatica-functiescheiding via Role-Based Access Control

In het informatica-domein wordt functiescheiding afgedwongen via Role-Based Access Control (RBAC): elke gebruiker krijgt een rol toegewezen (bv. inkoper, boekhouder, magazijnier) en die rol bepaalt welke schermen, transacties en bedragen hij mag gebruiken. Voor sleutelcontroles gelden twee fundamentele beginselen: (1) least privilege - elke gebruiker krijgt het minimum aan rechten dat hij voor zijn functie nodig heeft; (2) need-to-know - toegang tot gevoelige data alleen voor wie ze functioneel nodig heeft. Periodieke user-access-reviews controleren of de toegekende rechten nog passend zijn (cruciaal bij verloop, functiewissels, rolwijzigingen).

<small>🔗 ISA 315 (herzien-2019) — par. A172 general IT controls — _norm_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### 📜 Functiescheiding in het ITAA-kantoor (antiwitwaswet)

De antiwitwaswet (AWW 2017) verplicht elk ITAA-kantoor twee gescheiden functies te voorzien: (1) een verantwoordelijke op het hoogste niveau (typisch een vennoot of zaakvoerder) en (2) een Anti-Money Laundering Compliance Officer (AMLCO). In kantoren met minstens tien beroepsbeoefenaars moeten deze functies door verschillende personen worden uitgeoefend - een wettelijke toepassing van het functiescheiding-beginsel op het kantoor zelf.

<small>📖 ITAA-Handleiding-interne-procedures-AWW-2019 — Art. 9 — _norm_</small>

### 🚧 Grondbeperking: collusie

Functiescheiding faalt wanneer twee of meer personen samenspannen. Daarom altijd combineren met andere controles: rotatie van personeel in sleutelfuncties, verplichte vakantie (vervanger detecteert afwijkingen tijdens afwezigheid), management oversight, geautomatiseerde uitzonderingsrapporten, periodieke onafhankelijke reviews. Collusie is een van de vier inherente beperkingen van interne controle (zie record interne-controle).

<small>📖 ISA 240 — A1 - kenmerken van fraude inclusief samenspanning — _norm_</small>

## Voorbeelden

> [!example]- Functiescheiding aankoopcyclus bij Zelena Bio NV
> _Zelena Bio NV (kmo, 15 werknemers) heeft een eenvoudig ERP. De zaakvoerder wil weten welke functiescheiding-controles minimum nodig zijn voor de aankoopcyclus._
>
> | Stap | Door | ACR-IH |
>
> | --- | --- | --- |
>
> | Aanvraag | Magazijnier | Aanvragen (trigger, geen ACR-IH-functie) |
>
> | Goedkeuring inkooporder boven 1.000 EUR | Zaakvoerder | A |
>
> | Bestellen bij leverancier | Aankoper | U |
>
> | Ontvangst goederen en telling | Magazijnier | U + B |
>
> | Inboeking factuur en aansluiting met inkooporder | Boekhouder | R |
>
> | Betaling vrijgeven (tweehandtekeningsregel) | Zaakvoerder | A + U op treasury |
>
> <small>🔗 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Valkuilen

> [!warning]- Pseudo-functiescheiding via gedeelde paswoorden
> **Verkeerde assumptie**: Het volstaat dat de functies op papier gescheiden zijn.
>
> **Kernpunt**: Functiescheiding is alleen effectief als de toegangsrechten in de IT-systemen technisch afdwingen wat de papieren procedure voorschrijft. Gedeelde paswoorden, generieke accounts (admin, supervisor) of de gewoonte om elkaars sessie open te laten staan, vernietigen alle papieren scheiding. User-access-reviews en authenticatie-logs zijn daarom essentieel.
>
> <small>🔗 ISA 315 (herzien-2019) — par. A172 general IT controls — _norm_</small>

> [!warning]- Functiescheiding eisen in een te kleine entiteit
> **Verkeerde assumptie**: Een kmo met drie werknemers moet ook volledige ACR-IH toepassen.
>
> **Kernpunt**: Volledige functiescheiding is in een micro-onderneming feitelijk onmogelijk. De juiste vraag is dan welke compenserende controles aanwezig zijn: zaakvoerder-betrokkenheid bij autorisatie, externe accountant als onafhankelijke detectie-laag, jaarlijkse fysieke tellingen. Documenteer in het auditdossier waarom volledige functiescheiding ontbreekt en wat compenseert.
>
> <small>📖 ISA 265 — par. A3-A4 schaalbaarheid — _norm_</small>

> [!warning]- Functiescheiding als magic bullet zien
> **Verkeerde assumptie**: Met goede functiescheiding kan er geen fraude meer zijn.
>
> **Kernpunt**: Functiescheiding sluit collusie en management override niet uit. Het verlaagt het risico maar verwijdert het nooit volledig. Daarom altijd combineren met monitoring, verplichte vakantie, periodieke rotatie en management oversight. Functiescheiding is een sleutelcontrole, geen enige controle.
>
> <small>📖 ISA 240 — Bijlage 1 — _norm_</small>

## Accountant-perspectieven

### Externe auditor toetst functiescheiding bij cliente

_De auditor die functiescheiding wil identificeren als sleutelcontrole en operating effectiveness wil toetsen._

#### 🔍 Auditor

##### 👣 RBAC-extract opvragen uit ERP

Vraag aan de IT-afdeling een extract van de toegekende rollen per user in het ERP-systeem. Analyseer op SoD-conflicten: same-user-met-tegenstrijdige-rollen, niet-verwijderde inactieve users, generieke accounts. Tools zoals SAP GRC of ACL/IDEA detecteren SoD-conflicten automatisch.

<small>🔗 ISA 315 (herzien-2019) — par. A172 general IT controls — _norm_</small>

##### 👣 Walk-through fysieke functiescheiding

Volg een complete transactie van begin tot einde (aankoop, betaling, levering, boeking) en noteer wie elke stap effectief uitvoert. Vergelijk met de papieren procedure en de rolbeschrijvingen. Een gap tussen papier en praktijk is een design-deficiency die in het management letter moet (ISA 265).

<small>🔗 ISA 330 — par. 8 walk-through bij toetsing IC — _norm_</small>

### Eigen kantoor: AMLCO-functie inrichten

_De ITAA-beroepsbeoefenaar die zijn eigen kantoor conform antiwitwaswet moet inrichten._

#### 👥 Begeleider

##### 👣 AMLCO aanduiden (tweede functie)

Per kantoor twee functies aanduiden: (1) verantwoordelijke op het hoogste niveau - meestal een vennoot of zaakvoerder; (2) Anti-Money Laundering Compliance Officer - belast met de antiwitwas-procedures, kan een andere persoon of dezelfde zijn in kantoren met minder dan tien beroepsbeoefenaars. Vanaf tien beroepsbeoefenaars verplicht twee verschillende personen. Documenteer aanstelling in het kantoor-procedure-handboek en meld aan ITAA waar vereist.

<small>📖 ITAA-Handleiding-interne-procedures-AWW-2019 — Art. 9 — _norm_</small>

## Verder lezen (scope-out)

- → Interne controle als parent-kader → [[interne-controle]] _(moet-verwijzen)_
- → Ontwerp-aanpak → [[ontwerp-interne-controle]] _(moet-verwijzen)_
- → Concrete toepassing per cyclus → [[cyclus-analyse]] _(moet-verwijzen)_
- → Role-Based Access Control detail → [[it-controles]] _(moet-verwijzen)_
- ↪ Sleutelcontrole testen door auditor → [[audit-bewijs]] _(mag-verwijzen)_

## Relaties

### `valt_onder`
- [[interne-controle]]
### `vereist`
- [[it-controles]] — Functiescheiding wordt operationeel afgedwongen via Role-Based Access Control in informatica-systemen.
