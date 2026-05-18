---
title: Integreren van AVG-compliance in het intern-controlesysteem
tags:
- competentie
- po-1-7
programmaonderdelen:
- '1.7'
status: voorgesteld
schema_version: '1.5'
gegenereerd_uit: data/concepten/records/integreren-avg-compliance-in-ic.json
gegenereerd_op: '2026-05-18'
---
# Integreren van AVG-compliance in het intern-controlesysteem

**⚖️ 80% · 🤖 20%**

> AVG (EU-Verordening 2016/679) + Wet 30 juli 2018 leggen wettelijk strikte verplichtingen op: rechtmatige verwerking, AVG-register (art. 30), DPIA bij hoog risico (art. 35), datalekmelding aan GBA binnen 72u (art. 33), rechten betrokkenen (art. 12-22), aanstelling DPO bij verplichte categorieën (art. 37). De vertaling naar IC-procedures, retentie-schema's en awareness-training is praktijkmatig.

## Aanbevolen werkwijze

### 1. AVG-register opstellen — alle verwerkingen van persoonsgegevens

Inventariseer alle verwerkingen van persoonsgegevens binnen de organisatie en documenteer per verwerking de rechtsgrondslag, doel, categorieën, bewaartermijn en ontvangers.

**Waarom?** AVG-register (art. 30) is wettelijke verplichting voor organisaties met ≥ 250 werknemers + voor risicovolle verwerkingen ongeacht omvang. Zonder register is geen demonstratie van compliance mogelijk.

**📥 Input**:
- Procesinventaris IC-handboek → **Alle bedrijfsprocessen** _(document)_
- HR-data, klantendata, leveranciersdata, marketing-data → **Bestaande databronnen** _(document)_

**📤 Output**:
- AVG-verwerkingsregister → **Per verwerking: identificatie, doel, rechtsgrondslag, categorieën, ontvangers, bewaartermijn, beveiliging** _(document)_

**🛠️ Hoe**:

1. Volg [[avg-interne-controle]] §register-art-30: doorloop elke bedrijfsproces en identificeer waar persoonsgegevens worden verwerkt — HR (loonadministratie, sollicitaties), verkoop (klantgegevens), marketing (mailing-lijsten), inkoop (contactpersonen).
2. Documenteer per verwerking de zes verplichte velden uit art. 30: doel, categorieën betrokkenen, categorieën gegevens, ontvangers, internationale doorgifte, bewaartermijn.
3. Voeg rechtsgrondslag toe (art. 6): toestemming, contract, wettelijke verplichting, vitale belangen, openbaar belang, gerechtvaardigd belang.
4. Voor bijzondere categorieën (gezondheid, biometrie, lidmaatschap) — strengere grondslag uit art. 9 vereist.


**Grondslag**: [[avg-interne-controle]] §register, AVG art. 30 + art. 5

> [!warning]- Documenteer bewaartermijnen expliciet per categorie — niet enkel 'zolang noodzakelijk'.
>
> _Vaak fout gedaan_: Bewaartermijn 'voor onbepaalde duur' invullen — schending van data-minimisatie-beginsel (art. 5).
>
> _Grondslag_: [[avg-interne-controle]] §bewaartermijn

### 2. DPIA uitvoeren bij hoog risico — privacy-impactbeoordeling

Voor verwerkingen die waarschijnlijk een hoog risico inhouden voor rechten en vrijheden (grootschalige profilering, bijzondere categorieën, systematische monitoring): voer een Data Protection Impact Assessment uit.

**Waarom?** DPIA (art. 35) is wettelijk verplicht bij hoog risico. Geen DPIA = directe sanctiegrond + GBA-handhaving.

**📥 Input**:
- AVG-register stap 1 → **Hoog-risico-verwerkingen** _(document)_

**📤 Output**:
- DPIA-rapporten per verwerking → **Risico-analyse + waarborgen + residueel risico** _(document)_

**🛠️ Hoe**:

1. Pas [[avg-interne-controle]] §DPIA-trigger toe: gebruik GBA-lijst van verplichte DPIA-verwerkingen (bv. camerabewaking op werkplek, biometrie, grootschalige gezondheidsdata).
2. Beschrijf systematisch de verwerking + noodzakelijkheid en proportionaliteit.
3. Analyseer risico's voor rechten betrokkenen: discriminatie, identiteitsdiefstal, financieel verlies, reputatieschade.
4. Definieer waarborgen: technische (encryptie, pseudonimisering) + organisatorische (toegangsbeleid, training). Bij rest-hoog-risico: voorafgaande raadpleging GBA verplicht (art. 36).


**Grondslag**: [[avg-interne-controle]] §DPIA, AVG art. 35-36

### 3. Procedures voor rechten betrokkenen en datalekken inbouwen

Bouw IC-procedures voor (a) afhandeling van verzoeken van betrokkenen (inzage, rectificatie, wissing, beperking, overdraagbaarheid, bezwaar) en (b) detectie + 72u-melding van datalekken.

**Waarom?** Termijnen zijn hard: 1 maand voor verzoeken (art. 12), 72u voor datalekmelding aan GBA (art. 33). Vroeger gemist = sanctie.

**📥 Input**:
- AVG-register + DPIA-rapporten → **Volledig beeld verwerkingen** _(document)_

**📤 Output**:
- Procedures + meldformulieren rechten + datalekken → **Met deadlines + verantwoordelijken + meldroutes** _(document)_

**🛠️ Hoe**:

1. Verzoeken-procedure: één centraal kanaal (DPO of dataverantwoordelijke), template voor identificatie betrokkene, beslissingsmatrix per recht, tracker voor doorlooptijd. Vervaltermijn 1 maand (verlengbaar tot 3 met motivatie).
2. Datalek-detectie via IT-monitoring + medewerker-meldingen. Definieer 'datalek' duidelijk (vernietiging, verlies, ongeoorloofde toegang).
3. 72u-protocol: meldformulier GBA voorbereid; juridisch en IT pre-geïdentificeerd. Bij hoog risico voor betrokkenen: ook melding aan betrokkenen (art. 34).
4. Train alle medewerkers minstens jaarlijks: hoe een datalek herkennen en wie te informeren. Documenteer training-evidence (Yperse Werkplaats BV: jaarlijkse 30-min e-learning + handtekening).


**Grondslag**: [[avg-interne-controle]] §rechten + datalek, AVG art. 12-22 + art. 33-34

> [!warning]- Behandel datalek-melding aan GBA proactief — ook bij twijfel melden. GBA waardeert transparantie; verzwijgen leidt tot zwaardere sancties.
>
> _Vaak fout gedaan_: Wachten met datalekmelding 'tot we de impact begrepen hebben' — vervaltermijn 72u wordt overschreden.
>
> _Grondslag_: [[avg-interne-controle]] §datalek-72u, AVG art. 33

### 4. AVG koppelen aan cyberbeveiliging en IT-controls

Integreer AVG-beveiligingsverplichtingen (art. 32) met algemene cyberbeveiliging: toegangsbeheer, encryptie, back-up, incident response.

**Waarom?** AVG en cyberbeveiliging overlappen sterk — een aanpak die beide combineert vermijdt duplicatie en versterkt zekerheid.

**📥 Input**:
- IT-beleid Yperse Werkplaats BV → **Bestaand cyberbeleid** _(document)_

**📤 Output**:
- Geïntegreerd security + AVG-beleid → **Eén document met cross-references** _(document)_

**🛠️ Hoe**:

1. Pas [[geinformatiseerde-omgeving-ic]] §IT-controls toe met AVG-bril: toegangsbeheer op basis van need-to-know, MFA voor persoonsgegevens-systemen, encryptie van back-ups, periodieke toegangsreview.
2. Volg [[cyberrisico-ic]] §typologie: malware, phishing, insider threat, supply chain attack — elk heeft AVG-impact.
3. Aanstelling DPO (Data Protection Officer) verplicht bij art. 37-triggers: overheid, grootschalige systematische monitoring, grootschalige verwerking bijzondere gegevens. DPO rapporteert direct aan hoogste bestuursniveau.
4. Awareness-programma: phishing-simulaties, cybersafe-day, AVG-quiz voor nieuwe medewerkers in onboarding.


> [!example]- Voorbeeld: Yperse Werkplaats BV (45 werknemers, productie-KMO, geen verplichte DPO) integreert AVG met begeleiding van Xenon Expert…
> Yperse Werkplaats BV (45 werknemers, productie-KMO, geen verplichte DPO) integreert AVG met begeleiding van Xenon Expertise BV. Marleen De Cock fungeert als data-coördinator (geen DPO-functietitel).
>
> 1. **AVG-register-overzicht** 💬
>
>    8 verwerkingen geïdentificeerd:
>    - HR: loonadmin + ziekteverlof (rechtsgrond: contract + wet)
>    - Klanten-CRM (contact + facturatie — rechtsgrond: contract)
>    - Sollicitaties (rechtsgrond: gerechtvaardigd belang; bewaartermijn 2 jaar)
>    - Marketing-nieuwsbrief (rechtsgrond: toestemming)
>    - Camerabewaking magazijn (rechtsgrond: gerechtvaardigd belang; DPIA uitgevoerd)
>    - Bezoekersregister receptie
>    - Telefooncentrale (call recording: alleen voor klachten, retentie 1 maand)
>    - Wearables veiligheid (productie): rechtsgrondslag = wet arbeidsbescherming; retentie 6 maand.
>    
>
> 2. **DPIA-trigger** 💬
>
>    Camerabewaking en wearables = hoog-risico (systematische monitoring werknemers).
>    DPIA's opgemaakt: identificatie waarborgen (gerichte camera-zones, geen continue beeldopname werknemers; wearables: alleen veiligheidsdata, geen biometrische identificatie). Vakbond ingelicht.
>    
>
> 3. **Datalek-procedure (72u)** 💬
>
>    Stap 1: medewerker meldt aan Marleen (telefoon + e-mail).
>    Stap 2: Marleen + IT classificeren binnen 24u (datalek of niet; impact).
>    Stap 3: bij datalek = melding GBA via portal binnen 72u (Marleen ondertekent).
>    Stap 4: bij hoog risico betrokkenen = e-mail naar betrokkenen binnen 5 dagen.
>    Stap 5: lessons-learned-review na 30 dagen.
>    
>

**Grondslag**: [[geinformatiseerde-omgeving-ic]] §IT-controls, [[cyberrisico-ic]] §typologie, AVG art. 32 + art. 37


## Voorbeelden

> [!example]- Meubelzaak Mertens BV (8 werknemers, kleine BV) heeft AVG-vragen
> **Conclusie**: Ja, AVG geldt voor elke organisatie die persoonsgegevens verwerkt — geen drempel. Wel proportioneel: verwerkingsregister verplicht alleen bij ≥ 250 werknemers OF bij risicovolle verwerkingen — kleine BV's met enkel basale HR + klantenadministratie kunnen vereenvoudigde tracking gebruiken (cliëntenkaartje met bewaartermijn). Datalekmelding 72u + rechten betrokkenen 1 maand gelden zonder drempel.
>
> **Grondslag**: [[avg-interne-controle]] §toepassingsgebied, AVG art. 30 lid 5
>
> **Redenering**: Drempels gelden voor formaliteiten (register, DPO), niet voor materiële verplichtingen. Kleine onderneming moet kernverplichtingen alsnog naleven.

> [!example]- Bij Rotex Roeselare NV verzoekt een ex-werknemer om verwijdering van zijn HR-dossier op basis van 'recht op vergetelheid…
> **Conclusie**: Recht op wissing (art. 17) heeft uitzonderingen — onder andere wettelijke bewaarplicht. HR-dossiers moeten 5 jaar bewaard worden (sociale wetgeving + arbeidsrechtelijke verjaring), loonfiches 10 jaar (sociale zekerheid). Antwoord aan betrokkene binnen 1 maand: gedeeltelijke wissing waar mogelijk + motivering waarom andere data wettelijk bewaard moet blijven. Documenteer beslissing in AVG-tracking-tool.
>
> **Grondslag**: [[avg-interne-controle]] §rechten-uitzonderingen, AVG art. 17 lid 3
>
> **Redenering**: AVG-rechten zijn niet absoluut. Wettelijke bewaarplichten hebben voorrang. Correct antwoorden binnen termijn beschermt tegen sanctie.


## Gebaseerd op concepten

[[avg-interne-controle]] · [[geinformatiseerde-omgeving-ic]] · [[cyberrisico-ic]] · [[beheersactiviteiten]] · [[hr-cyclus-ic]]
## Voortkomend uit

- **Taken**: 1.7.taak.1
- **Kenniselementen**: 1.7.XII.A, 1.7.XII.H, 1.7.X, 1.7.X.A, 1.7.IX.D
