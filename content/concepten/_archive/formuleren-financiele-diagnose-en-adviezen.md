---
title: Formuleren van een financiële diagnose en concrete verbeteradviezen
tags:
- concept
- competentie
- po-1-3
linked_anchors:
- 1.3.taak.1
- 1.3.II.C
- 1.3.II.C.5
- 1.3.I.D.4
- 1.3.I.D.5
programmaonderdelen:
- '1.3'
confidence: inferred
node_type: competentie
status: voorgesteld
schema_version: '1.6'
gegenereerd_uit: data/concepten/records/formuleren-financiele-diagnose-en-adviezen.json
gegenereerd_op: '2026-05-21'
---
# Formuleren van een financiële diagnose en concrete verbeteradviezen 🔗

Sluitsteen-competentie: de losse cijferconclusies (liquiditeit, solvabiliteit, rentabiliteit, werkkapitaal, off-balance) samenballen in één diagnose en daaruit concrete verbeteradviezen formuleren. De stagiair leert dat een goede diagnose altijd gericht is op de specifieke gebruiker en zijn beslissing.



## Stappen

### 1. Synthetiseren van de bevindingen uit alle deelanalyses

Vat de conclusies van liquiditeit, solvabiliteit, rentabiliteit, werkkapitaal en off-balance samen in één matrix.

**Waarom?** Een diagnose is meer dan een lijst — het is de coherente lezing van wat alle ratio's samen zeggen.

**📥 Input**:
- Resultaten uit competentie [[berekenen-interpreteren-liquiditeitsratios]] → **Current ratio, quick ratio, trend** _(percentage)_
- Resultaten uit competentie [[berekenen-interpreteren-solvabiliteitsratios]] → **Solvabiliteit, debt-equity, covenant-marge** _(percentage)_
- Resultaten uit competentie [[berekenen-interpreteren-rentabiliteitsratios]] → **ROE netto+bruto, ROA netto+bruto, hefboom-marge** _(percentage)_
- Resultaten uit competentie [[beoordelen-werkkapitaal-en-kasstroom]] → **Werkkapitaal, vrije kasstroom** _(boekhoudkundig-bedrag)_

**📤 Output**:
- Diagnose-matrix → **Vier dimensies × signaal** _(conclusie)_

**🛠️ Hoe**:

1. Vul een matrix in met de vier hoofdperspectieven uit [[doelstellingen-financiele-analyse]] §liquiditeit/solvabiliteit/rendabiliteit/activiteit-groei.
2. Voor elk: noteer huidige waarde, sectormediaan, trendrichting, signaalkleur (groen/oranje/rood).
3. Identificeer dimensies waar twee of meer signalen rood zijn → systemisch zwakke plek.
4. Identificeer dimensies waar alle signalen groen zijn → bevestigde kracht.


> [!example]- Voorbeeld: Rotex Roeselare NV — synthese-matrix N
> Rotex Roeselare NV — synthese-matrix N.
>
> 1. **Diagnose-matrix** 🧮
>
>    | Dimensie       | Waarde N | Sectormed. | Trend | Signaal |
>    |----------------|---------:|-----------:|-------|---------|
>    | Liquiditeit (current)    | 1,63 | 1,40 | Stijgend | Groen   |
>    | Solvabiliteit            | 47,1% | 35%  | Stijgend | Groen   |
>    | Rentabiliteit (netto ROE)| 20,8% | 12%  | Stijgend | Groen   |
>    | Werkkapitaal-marge       | – € 0,2M tekort | n.v.t. | Stabiel | Oranje  |
>    
>
> 2. **Interpretatie** 💬
>
>    Drie groene signalen + één oranje. Financiële gezondheid bevestigd;
>    enige aandachtspunt is structureel werkkapitaaltekort van € 200.000
>    dat gefinancierd wordt via rekening-courant.
>    
>

**Grondslag**: [[doelstellingen-financiele-analyse]] §liquiditeit-solvabiliteit-rendabiliteit-activiteit

### 2. Detecteren van knipperlichten voor going concern

Toets aan de klassieke alarmsignalen voor financiële stress en continuïteits-twijfel.

**Waarom?** De accountant moet vroegtijdige signalen herkennen voordat ze tot insolventie leiden.

**📥 Input**:
- Diagnose-matrix uit stap 1 → **Signaalkleuren** _(conclusie)_
- Cashflow + dekkings-tabel → **Vrije kasstroom** _(boekhoudkundig-bedrag)_

**📤 Output**:
- Knipperlichten-lijst → **Per signaal: aanwezig/afwezig + ernst** _(conclusie)_

**🛠️ Hoe**:

1. Loop de klassieke alarmsignalen voor financiële moeilijkheden af volgens [[kamer-ondernemingen-in-moeilijkheden]] §signalen:
   - Aanhoudend negatief bedrijfsresultaat over meerdere boekjaren.
   - Erosie van het eigen vermogen (daling > 25% over twee boekjaren).
   - Negatieve vrije kasstroom recurrent.
   - Vervallen schulden — RSZ, fiscus, leveranciers.
   - Daling van de liquiditeit onder kritische drempels.
   - Schending of nakende schending van bankcovenanten ([[ratio-covenants]] §typische-covenants).
2. Markeer per signaal aanwezig/afwezig.
3. Bij twee of meer signalen aanwezig: going-concern-twijfel.
4. Bij going-concern-twijfel: documenteer expliciet en bespreek met cliënt.


> [!example]- Voorbeeld: Solaris Sint-Truiden BV — knipperlichten-toets
> Solaris Sint-Truiden BV — knipperlichten-toets.
>
> 1. **Knipperlichten-lijst** 🧮
>
>    | Signaal                                    | Aanwezig? |
>    |--------------------------------------------|-----------|
>    | Aanhoudend negatief bedrijfsresultaat      | Nee       |
>    | EV-erosie > 25% over 2 boekjaren           | Nee       |
>    | Recurrent negatieve vrije kasstroom        | Ja        |
>    | Vervallen RSZ-schuld € 180.000             | Ja        |
>    | Liquiditeit < 0,8                          | Nee       |
>    | Covenant-breach                            | Ja (debt-equity > 3) |
>    
>
> 2. **Conclusie** 💬
>
>    Drie signalen aanwezig: vervallen RSZ + negatieve vrije kasstroom +
>    covenant-breach. Going-concern-twijfel gerechtvaardigd. Solaris valt
>    binnen het detectie-bereik van de Kamer voor Ondernemingen in
>    Moeilijkheden — de zaakvoerder kan vrijwillig of op uitnodiging gehoord
>    worden.
>    
>

**Grondslag**: [[kamer-ondernemingen-in-moeilijkheden]] §signalen, Boek XX WER

> [!warning]- Documenteer going-concern-twijfel expliciet in een aparte paragraaf van het rapport.
>
> _Vaak fout gedaan_: Going-concern-signalen verwerken in een algemene zin "de onderneming heeft aandachtspunten" — onvoldoende voor een schuldeiser of bestuurder die op de analyse vertrouwt.
>
> _Grondslag_: [[cijferanalyses-controle-norm]] §drie-momenten

### 3. Formuleren van concrete verbeteradviezen

Vertaal de zwakke dimensies in actionable adviezen aan het bestuur of de vennoten.

**Waarom?** De doelstelling van een financiële analyse is niet alleen vaststellen, maar ook handvatten geven om bij te sturen (1.3.taak.1.doel.2).

**📥 Input**:
- Diagnose-matrix + knipperlichten-lijst → **Zwakke dimensies + alarmsignalen** _(conclusie)_

**📤 Output**:
- Adviezenparagraaf in rapport → **Per zwakte: concreet voorstel** _(document)_

**🛠️ Hoe**:

1. Voor elke "oranje" of "rood" gemarkeerde dimensie: formuleer een concreet advies.
2. Liquiditeitsprobleem: factoring, herfinanciering korte schulden naar lange, voorraadafbouw, klantbetaaltermijnen verkorten.
3. Solvabiliteitsprobleem: kapitaalinbreng, winstinhouding versterken, verkoop niet-strategische activa.
4. Rentabiliteitsprobleem: kostenstructuur herbekijken, prijszetting, productmix optimaliseren.
5. Werkkapitaalprobleem: cyclusduur verkorten (klanten, voorraad), leveranciersbetalingen optimaliseren.
6. Going-concern-twijfel: ga naar stap 4 — overwegen escalatie en formele procedures.
7. Elk advies krijgt een verwachte impact-indicatie (groot/middel/klein).


**Grondslag**: [[doelstellingen-financiele-analyse]] §rendabiliteit, vakdoctrine

### 4. Adviseren over escalatie en formele procedures

Bij going-concern-twijfel: bespreek met cliënt of vrijwillige melding aan Kamer voor Ondernemingen in Moeilijkheden, gerechtelijke reorganisatie of andere formele stappen aangewezen zijn.

**Waarom?** De accountant heeft een professionele plicht om in alarmsituaties op de juiste opvolgingsorganen te wijzen.

**📥 Input**:
- Knipperlichten-lijst → **Going-concern-signalen** _(conclusie)_

**📤 Output**:
- Escalatie-advies → **Aanbevolen formele stappen** _(document)_

**🛠️ Hoe**:

1. Bij twee of meer going-concern-signalen: documenteer dit en bespreek met de bestuurders.
2. Wijs op de bestaansreden van de [[kamer-ondernemingen-in-moeilijkheden]] §detectie-en-preventie: vroegtijdig bewustwording, mogelijke gerechtelijke reorganisatie.
3. Indien commissaris benoemd: stem af met commissaris (signaleringsplicht).
4. Indien er een ondernemingsraad is: bestuur moet de raad informeren over de financiële toestand.
5. Documenteer in dossier dat dit gesprek heeft plaatsgehad en welke beslissing de bestuurders namen.


**Grondslag**: [[kamer-ondernemingen-in-moeilijkheden]] §detectie-en-preventie, Boek XX WER

> [!warning]- Bespreek going-concern-signalen schriftelijk met het bestuur en documenteer in het dossier.
>
> _Vaak fout gedaan_: Alleen mondeling signaleren — bij latere insolventie is er geen spoor dat de accountant op tijd waarschuwde.
>
> _Grondslag_: [[cijferanalyses-controle-norm]] §drie-momenten

### 5. Structureren van het eindrapport

Schrijf een gestructureerd analyserapport dat de cliënt kan lezen zonder voorkennis.

**Waarom?** Een sterke diagnose is waardeloos als ze niet leesbaar is voor de eindgebruiker.

**📥 Input**:
- Alle deeloutputs (matrix, knipperlichten, adviezen) → **Per onderdeel** _(document)_

**📤 Output**:
- Eindrapport financiële analyse → **Volledig document** _(document)_

**🛠️ Hoe**:

1. Begin met executive summary: drie tot vijf zinnen — wat is de financiële toestand?
2. Daarna: profiel onderneming + sector + boekjaren.
3. Diagnose per dimensie (liquiditeit, solvabiliteit, rentabiliteit, werkkapitaal/cashflow).
4. Off-balance en kwalitatieve aspecten (bestuursverslag, commissarisverslag).
5. Knipperlichten en going-concern-beoordeling (indien van toepassing).
6. Adviezen — concreet en gerangschikt naar prioriteit.
7. Bijlagen: berekeningen + werkbladen.


**Grondslag**: [[doelstellingen-financiele-analyse]] §doel-stuurt-analyse, vakdoctrine rapportering


## Voorbeelden




## Bronnen

[^1]: `anchor-1.3.taak.4`
