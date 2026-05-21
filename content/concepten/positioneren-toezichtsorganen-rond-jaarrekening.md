---
title: Positioneren van de toezichtsorganen rond de jaarrekening
tags:
- concept
- competentie
- po-1-3
linked_anchors:
- 1.3.taak.1
- 1.3.I.D
- 1.3.I.D.1
- 1.3.I.D.2
- 1.3.I.D.3
- 1.3.I.D.4
- 1.3.I.D.5
programmaonderdelen:
- '1.3'
confidence: inferred
node_type: competentie
status: voorgesteld
schema_version: '1.6'
gegenereerd_uit: data/concepten/records/positioneren-toezichtsorganen-rond-jaarrekening.json
gegenereerd_op: '2026-05-21'
---
# Positioneren van de toezichtsorganen rond de jaarrekening 🔗

Competentie om de rolverdeling tussen bestuursorgaan, commissaris, algemene vergadering, ondernemingsraad en Kamer voor ondernemingen in moeilijkheden te kennen. De stagiair leert wie wat doet (opstelling vs. controle vs. goedkeuring vs. informatieverstrekking vs. signaaldetectie) en wanneer elk orgaan verplicht is op basis van omvang en vorm.



## Stappen

### 1. In kaart brengen van welke organen op de onderneming van toepassing zijn

Bepaal welke toezichtsorganen rond een specifieke onderneming actief zijn op basis van haar omvang, vorm en sector.

**Waarom?** Een KMO heeft een ander toezichtsecosysteem dan een grote NV — analyse en advies moeten dit reflecteren.

**📥 Input**:
- KBO-uittreksel + jaarrekening-schema → **Vennootschapsvorm, grootte (klein/groot), beursnotering** _(document)_
- Werknemerstal (jaargemiddelde) → **Aantal werknemers** _(boekhoudkundig-bedrag)_

**📤 Output**:
- Organengrafiek → **Per orgaan: van toepassing ja/nee + rol** _(document)_

**🛠️ Hoe**:

1. Toets vennootschapsvorm: alle vennootschappen hebben een algemene vergadering (AV).
2. Toets commissaris: verplicht voor grote vennootschappen of indien statutair voorzien ([[commissaris-toezicht-jaarrekening]] §benoeming).
3. Toets ondernemingsraad: verplicht bij gemiddeld > 100 werknemers ([[ondernemingsraad-sociaal-economische-info]] §toepassingsgebied).
4. Toets Kamer voor Ondernemingen in Moeilijkheden: van toepassing zodra signalen (zie [[kamer-ondernemingen-in-moeilijkheden]] §signalen) opduiken — passieve detectie.
5. Toets financiële instanties met covenants: van toepassing zodra er bancaire kredieten met financial covenants lopen ([[ratio-covenants]] §typische-covenants).
6. Schrijf een tabel "Toezichtsorganen aanwezig" op.


> [!example]- Voorbeeld: Rotex Roeselare NV (grote NV, 280 werknemers, bankkrediet met covenants)
> Rotex Roeselare NV (grote NV, 280 werknemers, bankkrediet met covenants).
>
> 1. **Organengrafiek** 🧮
>
>    | Orgaan                                  | Van toepassing? | Rol kort                            |
>    |-----------------------------------------|-----------------|-------------------------------------|
>    | Algemene vergadering                    | Ja              | Goedkeuring jaarrekening + kwijting |
>    | Commissaris                             | Ja (grote NV)   | Wettelijke controle jaarrekening    |
>    | Ondernemingsraad                        | Ja (> 100 wn)   | Sociaal-economische info werknemers |
>    | Kamer voor Ondernemingen in Moeilijkheden | Latent        | Detectie bij signalen               |
>    | Bank met covenants                      | Ja              | Periodieke ratio-toetsing           |
>    
>

**Grondslag**: [[commissaris-toezicht-jaarrekening]] §benoeming, [[ondernemingsraad-sociaal-economische-info]] §toepassingsgebied

### 2. Toelichten van de rol van de algemene vergadering bij de jaarrekening

Beschrijf welke beslissingen de AV neemt en welke documenten daarvoor moeten worden voorgelegd.

**Waarom?** De AV is het primaire orgaan dat de jaarrekening wettelijk goedkeurt — analyse moet die context kennen.

**📥 Input**:
- Statuten + WVV art. 9:19 → **Bevoegdheden AV** _(document)_

**📤 Output**:
- AV-rol-paragraaf → **Bevoegdheden, timing, documentenflow** _(document)_

**🛠️ Hoe**:

1. Beschrijf volgens [[algemene-vergadering-toezichtsfunctie]] §bevoegdheden: goedkeuring jaarrekening, kwijting aan bestuurders, benoeming commissaris.
2. Vermeld het toelichtingsrecht: bestuursorgaan moet vragen van aandeelhouders beantwoorden (WVV art. 9:19).
3. Vermeld bijzonder onderzoeksrecht: minderheidsaandeelhouder kan onderzoek vragen bij vermoeden van onregelmatigheden.
4. Bij entiteiten zonder commissaris: individueel onderzoeksrecht van elke vennoot.
5. Documenteer de jaarlijkse flow: jaarrekening voorleggen ≥ 15 dagen vóór AV; verslag goedkeuren; kwijting.


**Grondslag**: [[algemene-vergadering-toezichtsfunctie]] §bevoegdheden, WVV art. 9:19

### 3. Toelichten van de rol van de commissaris

Beschrijf wat de analist mag verwachten van het commissarisverslag.

**Waarom?** De analist gebruikt het commissarisverslag als extern signaal — moet de scope en grenzen ervan kennen.

**📥 Input**:
- ITAA-normen + WVV → **Wettelijke controleopdracht** _(document)_

**📤 Output**:
- Commissaris-rol-paragraaf → **Scope, onafhankelijkheid, rapportering** _(document)_

**🛠️ Hoe**:

1. Vermeld volgens [[commissaris-toezicht-jaarrekening]] §rol-onafhankelijk-oordeel: oordeel over getrouw beeld van de jaarrekening.
2. Vermeld dat de commissaris GEEN management-advies geeft — beperkt tot controle.
3. Wijs op de bijzondere meldingsplichten: AV, bestuursorgaan, ondernemingsraad, alarmprocedures bij continuïteitsbedreiging.
4. Vermeld de onafhankelijkheidsregels: een commissaris is geen accountant in dienst.
5. Geef aan dat bij kleine vennootschappen geen commissaris vereist is — dan vervalt deze externe controlebron.


**Grondslag**: [[commissaris-toezicht-jaarrekening]] §rol-onafhankelijk-oordeel, [[cijferanalyses-controle-norm]] §drie-momenten

### 4. Verhelderen van de informatieplichten richting ondernemingsraad

Beschrijf welke financiële informatie aan werknemers via de OR moet worden bezorgd.

**Waarom?** De OR is voor de analist een signaal: hoe transparant is het bestuur naar werknemers?

**📥 Input**:
- KB 27 november 1973 → **Basisinformatie, jaarinformatie, occasionele informatie** _(document)_

**📤 Output**:
- OR-flow-paragraaf → **Frequentie + inhoud** _(document)_

**🛠️ Hoe**:

1. Vermeld volgens [[ondernemingsraad-sociaal-economische-info]] §efi-procedure de drie informatie-types:
   - **Basisinformatie**: bij oprichting OR + bij wijzigingen — structuur, statuut, marktpositie.
   - **Jaarinformatie**: jaarlijks — jaarrekening + commentaar bestuur + sociaal balans.
   - **Occasionele informatie**: bij belangrijke wijzigingen (overnames, herstructureringen).
2. Bij twijfel kan de OR de commissaris om toelichting vragen — onafhankelijke controlebron.
3. Vermeld dat de bestuurder verplicht is de OR vóór de AV in te lichten over de financiële toestand.


**Grondslag**: [[ondernemingsraad-sociaal-economische-info]] §efi-procedure

### 5. Plaatsen van de Kamer voor Ondernemingen in Moeilijkheden in het signaleringskader

Beschrijf hoe en wanneer deze gerechtelijke kamer een rol speelt.

**Waarom?** De analist moet weten wanneer een cliënt waarschijnlijk een uitnodiging krijgt en welke gevolgen dat heeft.

**📥 Input**:
- Boek XX WER → **Detectieprocedure, vertrouwelijk gesprek** _(document)_
- Knipperlichten uit competentie [[formuleren-financiele-diagnose-en-adviezen]] stap 2 → **Going-concern-signalen** _(conclusie)_

**📤 Output**:
- KOM-paragraaf → **Werking + impact op cliënt** _(document)_

**🛠️ Hoe**:

1. Vermeld de werking volgens [[kamer-ondernemingen-in-moeilijkheden]] §detectie-en-preventie: NBB-signalen + commerciële signalen activeren de kamer.
2. Vermeld het vertrouwelijk gesprek: geen sanctie, doel is bewustwording en oriëntatie naar oplossingen (gerechtelijke reorganisatie, overdracht, vereffening).
3. Bij going-concern-signalen: adviseer cliënt over de mogelijkheid van vrijwillige melding — proactief beter dan op uitnodiging.
4. Documenteer dit in de adviezen-paragraaf van de analyse.


**Grondslag**: [[kamer-ondernemingen-in-moeilijkheden]] §detectie-en-preventie, Boek XX WER

### 6. Plaatsen van financiële tegenpartijen (banken) in het toezichtskader

Beschrijf de monitoring-rol van kredietverleners via ratio-covenants.

**Waarom?** Een bank is geen onafhankelijke controleur, maar haar covenants leggen wel reële beperkingen op aan de cliënt.

**📥 Input**:
- Kredietovereenkomsten met covenants → **Test-ratio's + drempels + testfrequentie** _(document)_

**📤 Output**:
- Bank-rol-paragraaf → **Werking + gevolgen breach** _(document)_

**🛠️ Hoe**:

1. Vermeld volgens [[ratio-covenants]] §typische-covenants: solvabiliteits-, leverage-, dekkings-covenants.
2. Vermeld testfrequentie: meestal kwartaal of jaarlijks.
3. Vermeld gevolgen breach: vervroegde opeisbaarheid, hogere marges, bijkomende zekerheden.
4. Wijs op de wisselwerking met analyse: een bank-monitoring-systeem versterkt of vervangt soms een commissaris-functie voor kredietverleners-doeleinden.


**Grondslag**: [[ratio-covenants]] §testdatum-en-testfrequentie


## Voorbeelden




## Bronnen

[^1]: `anchor-1.3.III`
