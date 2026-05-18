---
title: Voorbereiden van een financiële analyse van de jaarrekening
tags:
- concept
- competentie
- po-1-3
linked_anchors:
- 1.3.taak.1
- 1.3.I.A
- 1.3.I.B
- 1.3.II.A
programmaonderdelen:
- '1.3'
confidence: inferred
node_type: competentie
status: voorgesteld
schema_version: '1.5'
gegenereerd_uit: data/concepten/records/voorbereiden-financiele-analyse.json
gegenereerd_op: '2026-05-18'
---
# Voorbereiden van een financiële analyse van de jaarrekening 🤖


## Stappen

### 1. Definiëren van het doel en de gebruiker van de analyse

Stel vast wie de opdrachtgever is en welke beslissing of vraag de analyse moet ondersteunen.

**Waarom?** Hetzelfde cijfer wordt anders geïnterpreteerd door een bank (kredietrisico) dan door een aandeelhouder (rendement) of een fiscus (winstbasis).

**📥 Input**:
- Opdrachtbrief of e-mail van de cliënt → **Aard van de vraag** _(document)_
- Identificatie van de eindgebruiker → **Gebruikerstype** _(conclusie)_

**📤 Output**:
- Scoping-notitie → **Doel + gebruikersprofiel + diepgang** _(document)_

**🛠️ Hoe**:

1. Lees de opdrachtbrief en noteer de concrete vraag (kredietbeoordeling, overnameanalyse, going-concern, verbetervoorstellen, ...).
2. Kwalificeer de eindgebruiker volgens [[gebruikers-jaarrekening]] §categorieën (aandeelhouder, kredietverlener, fiscus, werknemers, klant/leverancier, publiek).
3. Koppel het doel aan één of meer hoofdperspectieven uit [[doelstellingen-financiele-analyse]] §liquiditeit/solvabiliteit/rendabiliteit/activiteit-groei.
4. Leg vast hoe diep je gaat: snelle review of grondige diagnose met sectorvergelijking en historiek.
5. Documenteer dit als scoping-notitie in het dossier.


> [!example]- Voorbeeld: Bank wil kredietlijn van € 2.000.000 verlengen aan Rotex Roeselare NV
> Bank wil kredietlijn van € 2.000.000 verlengen aan Rotex Roeselare NV. Vraagt aan accountant Sofie Janssens een ratio-analyse van de laatste drie boekjaren.
>
> 1. **Scoping** 💬
>
>    - **Gebruiker**: kredietverlener (bank).
>    - **Doel**: solvabiliteit + liquiditeit + dekking financiële lasten.
>    - **Perspectief**: terugbetalingscapaciteit op middellange termijn.
>    - **Diepgang**: drie boekjaren + sectorvergelijking + werkkapitaalevolutie.
>    
>

**Grondslag**: [[intake-financiele-analyse]] §stap-1, [[gebruikers-jaarrekening]] §categorieën

> [!warning]- Stel het doel expliciet op papier vóór je start.
>
> _Vaak fout gedaan_: Aannemen dat "even een analyse maken" volstaat — zonder doel kun je geen materialiteit bepalen.
>
> _Grondslag_: [[doelstellingen-financiele-analyse]] §doel-stuurt-analyse

### 2. Verzamelen van achtergrondinformatie over de onderneming en de sector

Bouw een beknopt profiel van de onderneming en haar sector vóór je in de cijfers duikt.

**Waarom?** Cijfers zonder context zijn betekenisloos — een schuldgraad van 60% is normaal in vastgoed maar alarmerend in dienstverlening.

**📥 Input**:
- KBO-uittreksel → **Activiteitencode (NACE), oprichtingsdatum, bestuurders** _(document)_
- Website + LinkedIn van de onderneming → **Markt, producten, omvang** _(document)_
- Sectorrapporten (NBB, Belfius, Graydon) → **Sectormediaan voor kernratio's** _(document)_

**📤 Output**:
- Onderneming-en-sectorprofiel → **Kerncijfers, markt, sector, recente gebeurtenissen** _(document)_

**🛠️ Hoe**:

1. Haal het KBO-uittreksel op en noteer NACE-code, oprichtingsdatum, juridische vorm.
2. Lees de website van Rotex Roeselare NV en bepaal het bedrijfsmodel (productie, distributie, dienst).
3. Zoek de sector op in NBB-statistieken of Belfius-sectoranalyse en noteer de sectormediaan voor de ratio's die je gaat berekenen.
4. Check op recente persberichten of overnames die de cijfers kunnen vertekenen.
5. Vat dit op één pagina samen in het dossier.


**Grondslag**: [[intake-financiele-analyse]] §stap-2, [[sectorvergelijking-financiele-analyse]] §sectorgrenzen

### 3. Verzamelen van de jaarrekeningen over drie tot vijf boekjaren

Haal de officiële jaarrekeningen op uit het Centraal Balanscentrum (CBSO) van de NBB.

**Waarom?** Eén boekjaar volstaat zelden — pas evolutie over meerdere jaren onthult trends en eenmalige effecten.

**📥 Input**:
- Centraal Balanscentrum (CBSO) — NBB → **Gedeponeerde jaarrekeningen N tot N-4** _(document)_

**📤 Output**:
- Werkmap met jaarrekeningen → **Drie tot vijf boekjaren, idealiter in Excel** _(document)_

**🛠️ Hoe**:

1. Ga naar nbb.be → Centraal Balanscentrum → zoek op KBO-nummer of naam.
2. Download minstens drie jaarrekeningen (boekjaren N, N-1, N-2); waar mogelijk vijf.
3. Open elk PDF-document en haal balans, resultatenrekening en toelichting in een werkbestand.
4. Noteer de schemavorm (verkort, micro, volledig) en de gebruikte waarderingsregels per boekjaar.
5. Controleer dat het boekjaar telkens dezelfde 12 maanden bestrijkt — anders moet je herrekenen.


**Grondslag**: [[intake-financiele-analyse]] §stap-3, [[historische-evolutie-financiele-analyse]] §3-5-boekjaren

> [!warning]- Check voor wijzigingen in waarderingsregels tussen de boekjaren.
>
> _Vaak fout gedaan_: Cijfers vergelijken zonder te merken dat de afschrijvingsmethode of voorraadwaardering veranderde.
>
> _Grondslag_: [[jaarrekening-als-studieobject]] §toelichting

### 4. Identificeren van bijzondere posten en aandachtspunten

Doorloop balans, resultatenrekening en toelichting en flag wat eruit springt.

**Waarom?** Een ratio is misleidend als één uitzonderlijke post de noemer of teller vertekent.

**📥 Input**:
- Werkmap met jaarrekeningen → **Balans + resultatenrekening + toelichting** _(document)_
- Commissarisverslag (indien aanwezig) → **Voorbehouden, melding aleatoire waardering** _(document)_

**📤 Output**:
- Lijst van aandachtspunten → **Per post een korte aantekening** _(document)_

**🛠️ Hoe**:

1. Loop de balans door en flag posten die plots verdubbelen of halveren tussen boekjaren.
2. Loop de resultatenrekening door en flag uitzonderlijke baten/lasten, herstructureringskosten, herwaarderingsmeerwaarden.
3. Lees de toelichting integraal: aleatoire waarderingen ([[getrouw-beeld-jaarrekening]] §toelichting-veiligheidsklep), verbonden partijen, gebeurtenissen na balansdatum, niet in de balans opgenomen rechten en verplichtingen.
4. Lees het commissarisverslag indien aanwezig — voorbehouden, paragrafen over going concern, kernpunten van de controle.
5. Pas de materialiteits-test toe volgens [[materieel-belang-jaarrekening]] §relatief: alles boven 5% van balanstotaal of 10% van bedrijfsresultaat is materieel.


**Grondslag**: [[intake-financiele-analyse]] §stap-4, [[materieel-belang-jaarrekening]] §context-bepaalt


## Voorbeelden




