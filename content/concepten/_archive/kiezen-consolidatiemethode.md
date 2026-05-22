---
title: Kiezen van de toe te passen consolidatietechniek per entiteit
tags:
- concept
- competentie
- po-1-4
linked_anchors:
- 1.4.taak.1
- 1.4.I.D
- 1.4.I.E
- 1.4.I.B
- 1.4.II.C
programmaonderdelen:
- '1.4'
confidence: inferred
node_type: competentie
status: voorgesteld
schema_version: '1.6'
gegenereerd_uit: data/concepten/records/kiezen-consolidatiemethode.json
gegenereerd_op: '2026-05-21'
---
# Kiezen van de toe te passen consolidatietechniek per entiteit 🔗

Een beslis-competentie binnen het Belgische boekhoudrecht-consolidatieregime (KB WVV Boek 3, Titel 2). De stagiair koppelt elke deelneming aan de juiste consolidatietechniek — integraal, evenredig, equity of buiten de kring — op basis van de aard van de zeggenschap en de mate van integratie in de groep.



## Stappen

### 1. Vaststellen van de kwalificatie per entiteit

Neem voor elke entiteit in de kring de kwalificatie over uit [[kwalificeren-relatie-deelneming]].

**Waarom?** De kwalificatie bepaalt mechanisch welke techniek wettelijk vereist is.

**📥 Input**:
- Werkpapier kwalificatie (uit [[kwalificeren-relatie-deelneming]]) → **Kwalificatie per entiteit** _(conclusie)_

**📤 Output**:
- Werkpapier methode-keuze → **Eén kwalificatie per entiteit in de kring** _(document)_

**🛠️ Hoe**:

1. Open het werkpapier kwalificatie van [[kwalificeren-relatie-deelneming]].
2. Lijst per entiteit de kwalificatie op: dochter, gemeenschappelijke dochter, geassocieerde of gewone deelneming.
3. Voeg ook entiteiten toe die zijn weggelaten op grond van art. 3:98 of 3:99 (zie [[afbakenen-consolidatiekring]] stap 4).
4. Bij een consortium: noteer ook welke vennootschappen consortium-lid zijn.


**Grondslag**: [[controle]] §kwalificatie (pre-requisite)

### 2. Integrale consolidatie op exclusief gecontroleerde dochters

Wijs integrale consolidatie toe aan alle exclusief gecontroleerde dochters in de kring.

**Waarom?** Integrale consolidatie geeft het beeld 'alsof het geheel één onderneming was' en is de standaardtechniek voor exclusieve dochters.

**📥 Input**:
- Werkpapier methode-keuze → **Dochterondernemingen** _(document)_

**📤 Output**:
- Werkpapier methode-keuze → **Beslissing: integrale consolidatie + afzondering belangen van derden** _(conclusie)_

**🛠️ Hoe**:

1. Voor elke dochter waarover exclusieve controle bestaat (bv. Brugse Brouwerij BV onder Aurelia Holding NV): wijs integrale consolidatie toe.
2. Verifieer dat de dochter in de consolidatiekring zit (niet weggelaten op grond van KB WVV art. 3:97).
3. Stuur de dochter door naar [[uitvoeren-eerste-consolidatie]] en [[uitvoeren-intragroep-eliminaties]] voor de uitvoering.
4. Belangen van derden = (1 − belangenpercentage) × eigen vermogen dochter, apart presenteren in 'Belangen van derden' (balans) en 'Aandeel van derden in het resultaat' (resultatenrekening).


> [!example]- Voorbeeld: Aurelia Holding NV bezit 80 % stemrechten in Brugse Brouwerij BV (exclusieve controle in rechte)
> Aurelia Holding NV bezit 80 % stemrechten in Brugse Brouwerij BV (exclusieve controle in rechte).
>
> 1. **Toewijzing techniek** 💬
>
>    Kwalificatie: dochter → integrale consolidatie.
>    100 % van Brugse-activa en -passiva opnemen, 20 % afzonderen als belangen van derden.
>    
>

**Grondslag**: [[integrale-consolidatie]] §toepassingsgebied, KB WVV art. 3:124 lid 1

### 3. Evenredige consolidatie op gemeenschappelijke dochters

Wijs evenredige consolidatie toe aan gemeenschappelijke dochters die nauw geïntegreerd zijn in de groepsactiviteit, anders vermogensmutatie.

**Waarom?** Evenredige consolidatie weerspiegelt het gezamenlijke karakter van de controle. Bij gebrek aan integratie volstaat vermogensmutatie.

**📥 Input**:
- Werkpapier methode-keuze → **Gemeenschappelijke dochters** _(document)_
- Bedrijfsbeschrijving van de gemeenschappelijke dochter → **Mate van operationele integratie met moeder** _(document)_

**📤 Output**:
- Werkpapier methode-keuze → **Evenredige consolidatie OF vermogensmutatie per gemeenschappelijke dochter** _(conclusie)_

**🛠️ Hoe**:

1. Voor elke gemeenschappelijke dochter (bv. Filmstudio Florence BV, 50/50 tussen Cardinal Group NV en Energiehuis Evergem BV): beoordeel de mate van operationele integratie.
2. Nauwe integratie? → evenredige consolidatie: activa/passiva pro-rata (belangenpercentage × bedragen), geen afzondering van derden.
3. Geen nauwe integratie? → vermogensmutatie (zie stap 4).
4. Documenteer in werkpapier waarom integratie wel of niet 'nauw' is.


> [!example]- Voorbeeld: Cardinal Group NV en Energiehuis Evergem BV bezitten elk 50 % in Filmstudio Florence BV. Filmstudio levert exclusief pos…
> Cardinal Group NV en Energiehuis Evergem BV bezitten elk 50 % in Filmstudio Florence BV. Filmstudio levert exclusief postproductie aan beide partners en gebruikt hun gemeenschappelijke ICT-systemen.
>
> 1. **Toets nauwe integratie** 💬
>
>    Operationele indicatoren: exclusieve dienstverlening aan partners + gedeelde ICT → nauw geïntegreerd.
>    
>
> 2. **Toewijzing techniek** 💬
>
>    Evenredige consolidatie voor Cardinal én voor Energiehuis (elk 50 %).
>    Geen aandeel van derden geboekt (omdat het derden-deel niet wordt opgenomen).
>    
>

**Grondslag**: [[evenredige-consolidatie]] §toepassingsgebied, KB WVV art. 3:135

> [!warning]- Bij evenredige consolidatie nooit een aandeel van derden boeken.
>
> _Vaak fout gedaan_: Aannemen dat ook bij evenredige consolidatie een aandeel van derden moet worden geboekt voor het deel buiten de groep.
>
> _Grondslag_: [[evenredige-consolidatie]] §geen-aandeel-van-derden

### 4. Vermogensmutatiemethode op geassocieerden en specifieke dochters

Wijs vermogensmutatie toe aan geassocieerde ondernemingen, niet-nauw-geïntegreerde gemeenschappelijke dochters en dochters die zijn uitgesloten op grond van art. 3:98 of 3:99.

**Waarom?** Vermogensmutatie weerspiegelt invloed (niet controle) over het netto-actief en het resultaat van de geassocieerde.

**📥 Input**:
- Werkpapier methode-keuze → **Geassocieerden + uitgesloten dochters** _(document)_

**📤 Output**:
- Werkpapier methode-keuze → **Vermogensmutatie per geselecteerde entiteit** _(conclusie)_

**🛠️ Hoe**:

1. Voor elke geassocieerde (bv. Drukkerij Dendermonde BV onder Antwerpse Investments NV, 25 %): wijs vermogensmutatie toe.
2. Voor elke niet-nauw-geïntegreerde gemeenschappelijke dochter: idem.
3. Voor elke dochter uitgesloten op grond van art. 3:98 of 3:99: idem (KB WVV verplicht dit).
4. Initiële boeking: pro-rata aandeel in eigen vermogen op aankoopdatum + eventueel consolidatieverschil. Jaarlijkse aanpassing: pro-rata aandeel in wijzigingen van het eigen vermogen.
5. Volg [[vermogensmutatiemethode]] §boeking voor de uitvoering.


**Grondslag**: [[vermogensmutatiemethode]] §toepassingsgebied, KB WVV art. 3:141

### 5. Horizontale consolidatie bij een consortium

Bij een consortium: voer eerst per lid een verticale consolidatie uit, dan integraal horizontaal samenvoegen.

**Waarom?** Bij een consortium ontbreekt een verticale moeder; de geconsolideerde jaarrekening wordt gezamenlijk opgesteld.

**📥 Input**:
- Vaststelling consortium uit [[afbakenen-consolidatiekring]] → **Lijst van consortium-leden** _(conclusie)_

**📤 Output**:
- Werkpapier methode-keuze → **Plan voor verticale + horizontale consolidatie** _(document)_

**🛠️ Hoe**:

1. Voor elk consortium-lid (bv. Industria Antwerpen NV, Jachthaven Jezus-Eik NV): voer eerst een verticale consolidatie uit van zijn eigen dochters volgens de gebruikelijke technieken.
2. Voeg vervolgens de verticaal geconsolideerde cijfers van alle leden integraal samen via horizontale consolidatie.
3. Behoud het karakter van de eigen-vermogenposten per lid (geen samenvoeging van kapitaal van verschillende leden).
4. Volg [[horizontale-consolidatie]] §uitvoering voor de techniek.


**Grondslag**: [[horizontale-consolidatie]] §toepassingsgebied, WVV art. 3:24 + KB WVV art. 3:124 lid 1


## Voorbeelden




