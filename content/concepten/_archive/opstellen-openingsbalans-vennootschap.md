---
title: Opstellen van de openingsbalans van een nieuwe vennootschap
tags:
- concept
- competentie
- po-1-1
- po-3-0
linked_anchors:
- 3.0.taak.1
- 1.1.taak.1
programmaonderdelen:
- '1.1'
- '3.0'
confidence: inferred
node_type: competentie
status: seed
schema_version: '1.6'
gegenereerd_uit: data/concepten/records/opstellen-openingsbalans-vennootschap.json
gegenereerd_op: '2026-05-21'
---
# Opstellen van de openingsbalans van een nieuwe vennootschap 🔗

Operationele boekhoudkundige competentie: vanuit de oprichtingsakte de eerste boekingen (openingsbalans + boeken van inbrengen + boeken van oprichtingskosten) verrichten zodat de vennootschap met een conforme balans haar eerste boekjaar start. Doel: vertrekpositie correct vastleggen volgens BOK/KB WVV en consistent met het financieel plan.



## In de praktijk

- De openingsbalans gebeurt vaak een paar dagen na de akte — niet direct, omdat oprichtingskosten-facturen pas dan binnenkomen.
- Voor BV's (kapitaalloos): boek inbreng op 11 — Inbreng buiten kapitaal beschikbaar, niet op 100 — Kapitaal (dat is NV-rekening).
- Sluitstuk: verifieer voorts dat de boekhoudpakket-startdatum = datum oprichtingsakte — vermijd 'gat' tussen oprichting en eerste boeking.

## Stappen

### 1. Inventariseren oprichtingstransacties

Lijst alle financiële handelingen die de vennootschap raken tussen oprichtingsdatum en effectieve startdatum: inbrengen, notariskosten, oprichtingskosten, eerste investeringen.

**Waarom?** De openingsbalans is geen gemiddelde maar een momentopname — alles wat gebeurd is moet erin.

**📥 Input**:
- Oprichtingsakte → **Inbrengen, kapitaal/aanvangsvermogen** _(wettelijk-document)_
- Facturen notaris, registratie, advies → **Oprichtingskosten** _(wettelijk-document)_

**📤 Output**:
- Transactielijst → **Per transactie: datum, bedrag, tegenrekening** _(tabel)_

**🛠️ Hoe**:

1. Verzamel: oprichtingsakte (totaal inbreng + aandelen-onderschrijving), bankafschriften vennootschap-in-oprichting-rekening, facturen notaris/advocaten/accountant voor oprichtingsfase, facturen eerste investeringen.
2. Klassificeer: inbreng vs kost vs investering.
3. Datum bij elk: pre-oprichting (op vennootschap-in-oprichting-rekening) of post-oprichting (na vrijgave geblokkeerde rekening).

**Grondslag**: [[boeken-oprichtings-en-kapitaalverhogingskosten]]

### 2. Boeken van de inbrengen

Boek de inbreng in geld en in natura: kapitaal-rekening of inbreng-rekening (passief) tegenover bank of het ingebrachte goed (actief).

**Waarom?** De openingsbalans-passiefzijde start met eigen vermogen. Onjuiste boeking (bv. inbreng als opbrengst) vertekent het eerste resultaat en de balans-presentatie.

**📥 Input**:
- Oprichtingsakte met inbreng-details → **Bedragen per oprichter + aard** _(wettelijk-document)_

**📤 Output**:
- Openingsboeking inbrengen → **Journaalboeking** _(boekingsregel)_

**🛠️ Hoe**:

1. Inbreng in geld (BV): debet 5500 — Bank, credit 11 — Inbreng buiten kapitaal beschikbaar (BV — kapitaalloos) of credit 100 — Kapitaal (NV — kapitaal).
2. Inbreng in natura (bv. bestelwagen): debet 240 — Rollend materieel tegenover credit 11/100 — afhankelijk van vorm.
3. Bedrag = waarde uit revisorenverslag.
4. Boek op datum van de notariële akte (datum verkrijging rechtspersoonlijkheid).

> [!example]- Voorbeeld: Oprichtingen Oostende BV — boeking inbreng € 25.000 cash + bestelwagen € 17.500
> Oprichtingen Oostende BV — boeking inbreng € 25.000 cash + bestelwagen € 17.500.
>
> 1. **Journaalboeking** 📝
>
>    | Rekening | Debet | Credit |
>    |---|---:|---:|
>    | 5500 Bank | € 25.000 |  |
>    | 240 Rollend materieel |  € 17.500 |  |
>    | 11 Inbreng buiten kapitaal beschikbaar |  | € 42.500 |
>    
>    *Datum: 18/03 (verlijden akte)*
>    
>

**Grondslag**: MAR; [[inbreng-vennootschap]]

### 3. Boeken van de oprichtingskosten

Boek de kosten die direct verbonden zijn aan de oprichting (notaris, eerste publicatie, accountant-advies, advocaat-statuten, eventueel registratie) — keuze tussen activeren onder rubriek 20 of in resultaat boeken.

**Waarom?** Oprichtingskosten zijn een uitzondering op het kost-of-actief-criterium: ze mogen worden geactiveerd onder strikte voorwaarden (afschrijving over max 5 jaar). De keuze beïnvloedt het resultaat van het eerste boekjaar.

**📥 Input**:
- Facturen oprichtingsfase → **Notaris, advocaat, accountant, publicatiekosten** _(wettelijk-document)_

**📤 Output**:
- Boeking oprichtingskosten + afschrijvingsplan → **Activering of kost** _(boekingsregel)_

**🛠️ Hoe**:

1. Inventariseer: alle facturen met oprichtingskarakter (notariskosten, publicatie Belgisch Staatsblad, advies fee accountant en advocaat statutenwerk, registratierechten).
2. Beslis activering of niet — zie [[boeken-oprichtings-en-kapitaalverhogingskosten]] voor de keuze-criteria. Activering aangewezen wanneer het bedrag materieel is en de cliënt het resultaat van jaar 1 niet wil vertekenen.
3. Bij activering: debet 200 — Kosten van oprichting tegenover credit 5500 — Bank of credit 440 — Leveranciers.
4. Afschrijvingsplan opstellen: lineair over 5 jaar of korter — verplicht een afschrijving vóór winstverdeling tot volledig afgeschreven.
5. Bij niet-activering: boek direct op 61 — Diensten en diverse goederen.

**Grondslag**: [[boeken-oprichtings-en-kapitaalverhogingskosten]]; KB WVV art. 3:42; [[oprichtingskosten]]

### 4. Samenstellen van de openingsbalans op formele wijze

Stel de openingsbalans op volgens het schema art. 3:3 KB WVV (volledig of verkort), met actief- en passiefzijde sluitend, en gebruik dit als startpunt van het boekhoudsysteem.

**Waarom?** Een formeel-conforme openingsbalans is voorwaarde voor latere jaarrekeningoplevering (de openingsbalans van jaar 1 = sluitbalans-1 voor jaar 2-vergelijking).

**📥 Input**:
- Boekingen inbreng (stap 2) + oprichtingskosten (stap 3) → **Alle openingsposten** _(boekingsregel)_

**📤 Output**:
- Openingsbalans WVV-schema → **Actief en passief gesloten** _(balans)_

**🛠️ Hoe**:

1. Bouw volgens KB WVV art. 3:3 schema: vaste activa (20-28), vlottende activa (29-58); eigen vermogen (10-15), voorzieningen (16), schulden > 1 jaar (17), schulden ≤ 1 jaar (42-49).
2. Vul met de cijfers uit de openingsboekingen.
3. Verifieer actief = passief.
4. Vergelijk met de geprojecteerde openingsbalans in het financieel plan — afwijking analyseren en documenteren.
5. Voer in het boekhoudpakket als startbalans op datum oprichting.

> [!example]- Voorbeeld: Oprichtingen Oostende BV — openingsbalans op 18/03
> Oprichtingen Oostende BV — openingsbalans op 18/03.
>
> 1. **Balans** 📊
>
>    | ACTIEF | Bedrag | PASSIEF | Bedrag |
>    |---|---:|---|---:|
>    | 200 Kosten van oprichting | € 4.500 | 11 Inbreng buiten kapitaal | € 42.500 |
>    | 240 Rollend materieel | € 17.500 |  |  |
>    | 5500 Bank | € 20.500 |  |  |
>    | **Totaal actief** | **€ 42.500** | **Totaal passief** | **€ 42.500** |
>    
>    *Cash € 20.500 = € 25.000 inbreng − € 4.500 oprichtingskosten direct betaald.*
>    
>

**Grondslag**: KB WVV art. 3:3 jaarrekeningenschema

### 5. Reconciliëren met financieel plan en documentatie

Vergelijk de werkelijke openingsbalans met de geprojecteerde openingsbalans uit het financieel plan; documenteer afwijkingen voor latere transparantie.

**Waarom?** Materiële afwijkingen tussen plan en realiteit zijn een vroeg-signaal voor afwijkende bedrijfsuitvoering en zijn relevant bij latere aansprakelijkheidsdiscussies.

**📥 Input**:
- Geprojecteerde openingsbalans uit financieel plan → **Sectie 3 plan** _(balans)_
- Werkelijke openingsbalans (stap 4) → **Conform jaarrekeningenschema** _(balans)_

**📤 Output**:
- Reconciliatie-nota → **Afwijkingen + reden** _(tekst-document)_

**🛠️ Hoe**:

1. Plaats de twee balansen naast elkaar.
2. Voor elke regel waar afwijking > 10% of > € 5.000: noteer reden (bv. krediet nog niet opgenomen, ingebrachte machine duurder dan verwacht).
3. Documenteer in cliëntdossier.
4. Indien materieel: signaleer aan cliënt — kan invloed hebben op haalbaarheid jaar 1.

**Grondslag**: Vakpraktijk + [[financieel-plan-oprichting]]


## Voorbeelden



