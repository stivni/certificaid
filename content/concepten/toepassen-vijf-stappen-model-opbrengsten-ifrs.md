---
title: Toepassen van het 5-stappen-model van IFRS 15 voor opbrengstenherkenning
tags:
- concept
- competentie
- po-1-5
linked_anchors:
- 1.5.taak.1
- 1.5.V.D
- 1.5.V
- 1.5.IV.C
programmaonderdelen:
- '1.5'
confidence: inferred
node_type: competentie
status: voorgesteld
schema_version: '1.5'
gegenereerd_uit: data/concepten/records/toepassen-vijf-stappen-model-opbrengsten-ifrs.json
gegenereerd_op: '2026-05-18'
---
# Toepassen van het 5-stappen-model van IFRS 15 voor opbrengstenherkenning 🤖


## Stappen

### 1. Identificeer het contract met de klant

Toets of een afspraak een contract in de zin van IFRS 15 is — 5 cumulatieve criteria: partijen hebben akkoord gegeven; rechten en betalingsvoorwaarden zijn identificeerbaar; commerciële substantie; inning waarschijnlijk.

**Waarom?** Zonder kwalificerend contract geen opbrengstherkenning onder IFRS 15. De criteria voorkomen dat informele of dubieuze afspraken al opbrengsten genereren.

**📥 Input**:
- Schriftelijke of mondelinge overeenkomst met klant → **Partijen + commitments + betalingsvoorwaarden** _(document)_

**📤 Output**:
- Werkpapier IFRS 15-toepassing → **Kwalificatie: contract ja/nee** _(conclusie)_

**🛠️ Hoe**:

1. Volg [[opbrengsten-ifrs]] §stap-1 voor de 5 contractcriteria.
2. Voor Zelena Bio NV — verkoop softwarelicentie + implementatie + 2 jaar onderhoud aan klant Aurelia Holding NV: schriftelijk akkoord, prijzen vastgelegd, betaaltermijn 30 dagen, commerciële substantie aanwezig, kredietwaardigheid Aurelia gecheckt.
3. Alle 5 criteria voldaan → contract kwalificeert onder IFRS 15.
4. Documenteer in werkpapier met contractdatum en partijen.


**Grondslag**: [[opbrengsten-ifrs]] §stap-1, IFRS 15 alinea 9-16

### 2. Identificeer de afzonderlijke prestatieverplichtingen

Splits het contract in de afzonderlijke goederen of diensten die onderscheiden zijn: (a) de klant kan er afzonderlijk voordeel uit halen, EN (b) het is onderscheidbaar binnen de context van het contract (alinea 27).

**Waarom?** Elke prestatieverplichting krijgt haar eigen tijdsbepaling en haar eigen toegewezen transactieprijs. Verkeerde splitsing → opbrengst op verkeerd moment of in verkeerde fasen.

**📥 Input**:
- Contract-inhoud uit stap 1 → **Lijst van toegezegde goederen/diensten** _(document)_

**📤 Output**:
- Werkpapier → **Lijst onderscheiden prestatieverplichtingen** _(conclusie)_

**🛠️ Hoe**:

1. Volg [[prestatieverplichting-ifrs-15]] §onderscheiden-criteria voor de twee toetsen.
2. Inventariseer alle beloofde goederen/diensten: bv. Zelena's contract = (a) softwarelicentie € 600.000, (b) implementatieservice € 200.000, (c) onderhoud 2 jaar € 200.000.
3. Toets criterium (a) — afzonderlijk voordeel: licentie zonder implementatie kan klant elders laten doen → ja. Onderhoud is geen onderdeel van licentie zelf → ja.
4. Toets criterium (b) — onderscheidbaar binnen context: implementatie is hoog-gestandaardiseerd en niet specifiek geïntegreerd met de software → ja, onderscheiden.
5. Conclusie: 3 prestatieverplichtingen.


**Grondslag**: [[opbrengsten-ifrs]] §stap-2, [[prestatieverplichting-ifrs-15]] §criteria, IFRS 15 alinea 22-30

> [!warning]- Voer beide criteria (afzonderlijk voordeel + onderscheidbaar in context) uit — niet één van de twee.
>
> _Vaak fout gedaan_: Elke factuurregel automatisch als afzonderlijke prestatieverplichting beschouwen. Wanneer implementatie sterk geïntegreerd is met software (één combined output), is het één gecombineerde prestatieverplichting.
>
> _Grondslag_: [[prestatieverplichting-ifrs-15]] §onderscheiden-binnen-context

### 3. Bepaal de transactieprijs

Stel de vergoeding vast die de entiteit verwacht te ontvangen in ruil voor de overdracht van de goederen of diensten — exclusief btw en bedragen geïnd voor derden. Hou rekening met variabele componenten, financieringscomponenten en niet-cash-vergoedingen.

**Waarom?** Foutieve transactieprijs (te hoog door verwachte kortingen niet mee te tellen, te laag door bonus-clausule te negeren) leidt tot foutieve toegewezen prijzen in stap 4 en foutieve opbrengsten in stap 5.

**📥 Input**:
- Contract + bijlagen + scenario-analyse variabele componenten → **Vaste + variabele bedragen** _(boekhoudkundig-bedrag)_

**📤 Output**:
- Werkpapier → **Totale transactieprijs** _(boekhoudkundig-bedrag)_

**🛠️ Hoe**:

1. Volg [[opbrengsten-ifrs]] §stap-3 voor de componenten van transactieprijs.
2. Voor Zelena/Aurelia: vaste vergoeding € 1.000.000 (600 + 200 + 200). Variabele bonus € 50.000 bij implementatie binnen 3 maanden — beoordeel verwachting via 'most likely amount' of 'expected value' (alinea 53). Bij Zelena historisch 80 % kans → € 50.000 erbij of niet, afhankelijk van methode.
3. Korten/aftrekken: financiering > 1 jaar afsplitsen als rente; btw expliciet uitsluiten.
4. Conclusie Zelena: transactieprijs = **€ 1.050.000** (inclusief verwachte bonus, omzichtigheidsclausule alinea 56 toegepast).


**Grondslag**: [[opbrengsten-ifrs]] §stap-3, IFRS 15 alinea 47-72

### 4. Wijs de transactieprijs toe aan de prestatieverplichtingen

Verdeel de transactieprijs over de onderscheiden prestatieverplichtingen op basis van **relatieve standalone selling prices** (SSP) — de prijs die elke goed of dienst afzonderlijk zou hebben.

**Waarom?** Allocatie op basis van SSP voorkomt cherry-picking (bv. de licentie als 'gratis bonus' bij onderhoud presenteren om opbrengst uit te stellen). Allocatie weerspiegelt de economische substantie.

**📥 Input**:
- Lijst prestatieverplichtingen uit stap 2 → **Per onderscheiden goed/dienst** _(boekhoudkundig-bedrag)_
- Marktprijzen of geschatte SSP → **Per onderscheiden goed/dienst** _(boekhoudkundig-bedrag)_

**📤 Output**:
- Werkpapier → **Allocatietabel per prestatieverplichting** _(berekening)_

**🛠️ Hoe**:

1. Volg [[opbrengsten-ifrs]] §stap-4 voor de allocatiemethode.
2. Verzamel SSP per prestatieverplichting: licentie € 700.000 (lijstprijs Zelena), implementatie € 250.000 (uurtarieven × dagen), onderhoud € 150.000 (jaarlijks tarief × 2 jaar). Som SSP = € 1.100.000.
3. Allocatie pro rato: licentie € 1.050.000 × (700/1100) = € 668.182; implementatie € 1.050.000 × (250/1100) = € 238.636; onderhoud € 1.050.000 × (150/1100) = € 143.182.
4. Documenteer in allocatietabel + motivering keuze SSP-bron.


> [!example]- Voorbeeld: Allocatie transactieprijs € 1.050.000 over de drie prestatieverplichtingen Zelena/Aurelia
> Allocatie transactieprijs € 1.050.000 over de drie prestatieverplichtingen Zelena/Aurelia.
>
> 1. **Allocatietabel met SSP** 🧮
>
>    | Prestatieverplichting | SSP (€)      | Aandeel  | Toegewezen prijs (€) |
>    |-----------------------|-------------:|---------:|---------------------:|
>    | Softwarelicentie      |      700.000 |  63,64 % |              668.182 |
>    | Implementatie         |      250.000 |  22,73 % |              238.636 |
>    | Onderhoud 2 jaar      |      150.000 |  13,64 % |              143.182 |
>    | **Totaal**            |  **1.100.000** | **100 %** |          **1.050.000** |
>    
>

**Grondslag**: [[opbrengsten-ifrs]] §stap-4, IFRS 15 alinea 73-86

### 5. Neem opbrengst op bij vervulling — tijdstip of over periode

Bepaal per prestatieverplichting of opbrengst **op één tijdstip** (control-transfer-moment) of **over een periode** wordt opgenomen. Drie criteria voor over-periode-opname (alinea 35); bij geen voldoening → tijdstip-opname.

**Waarom?** De timing van opbrengstherkenning is de meest examen-getoetste IFRS 15-beslissing. Foute timing zet meerdere boekjaren in een verkeerde stand.

**📥 Input**:
- Lijst prestatieverplichtingen + toegewezen prijzen uit stap 4 → **Per prestatieverplichting** _(boekhoudkundig-bedrag)_

**📤 Output**:
- Boekingen opbrengsten + contractactiva/-passiva → **Per prestatieverplichting** _(boekingsregel)_

**🛠️ Hoe**:

1. Volg [[opbrengsten-ifrs]] §stap-5 voor de tijdstip-versus-periode-toets.
2. Voor elke prestatieverplichting van Zelena/Aurelia:
   - **Licentie € 668.182**: levering op tijdstip — control transfers bij activering licentiesleutel → opbrengst in één keer op die datum.
   - **Implementatie € 238.636**: voortbrengt iets met alternatief gebruik voor Zelena (gestandaardiseerd) → niet over-periode-criterium A. Maar klant ontvangt en verbruikt voordeel terwijl implementatie loopt → criterium A wel voldaan → opbrengst **over periode** via input-methode (gewerkte uren / verwachte uren).
   - **Onderhoud € 143.182**: klant verbruikt voordelen gelijktijdig → opbrengst **over periode** lineair over 24 maanden = € 5.966/maand.
3. Boek: bij control-transfer licentie → debet 'Vordering klanten' € 668.182 / credit 'Opbrengsten'. Bij implementatie over periode: maand 1 25 % voltooid → € 59.659 opbrengst + 'Contractactief'. Bij onderhoud: maand 1 → € 5.966 opbrengst.
4. Hou contractsaldo's bij: contractactief (opbrengst > factuur) of contractpassief (factuur > opbrengst).


**Grondslag**: [[opbrengsten-ifrs]] §stap-5, IFRS 15 alinea 31-45

> [!warning]- Splits het contract financieel naar de drie tijdsbepalingen — licentie tijdstip / implementatie over periode / onderhoud over periode.
>
> _Vaak fout gedaan_: Het volledige contractbedrag op factuurdatum als opbrengst boeken. Dit overschat omzet in de beginperiode en onderschat in latere periodes.
>
> _Grondslag_: [[opbrengsten-ifrs]] §tijdstip-versus-periode


