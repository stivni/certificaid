---
title: NIS 2-richtlijn (cybersecurity-kader)
tags:
- concept
- regel
- po-1-7
linked_anchors:
- 1.7.X.A
- 1.7.X
programmaonderdelen:
- '1.7'
confidence: inferred
node_type: regel
status: seed
schema_version: '1.6'
gegenereerd_uit: data/concepten/records/nis-2-richtlijn.json
gegenereerd_op: '2026-05-18'
---
# NIS 2-richtlijn (cybersecurity-kader) 🤖

De NIS 2-richtlijn is het nieuwe Europese kader voor cybersecurity-verplichtingen van organisaties in kritieke en belangrijke sectoren. Voor stagiair-accountants is dit relevant in twee rollen: als adviseur van cliënten die onder NIS 2 vallen (toetsen of cyberbeheersing op orde is), en als externe auditor (cyberrisico's en IT-controles als onderdeel van risk assessment, ISA 315). De richtlijn vervangt NIS 1 (2016) en breidt het toepassingsgebied fors uit. In België is de richtlijn omgezet door de Wet van 26 april 2024.

> [!summary] Korte inhoud
> Richtlijn (EU) 2022/2555 ('NIS 2') verplicht organisaties die onder haar toepassingsgebied vallen om risicogebaseerde cybersecurity-maatregelen te treffen, ernstige incidenten te melden aan de bevoegde autoriteit, en hun bestuursorgaan persoonlijk verantwoordelijk te maken voor c….

> [!info] Behoort tot: [[cyberrisico-ic]]

Richtlijn (EU) 2022/2555 ('NIS 2') verplicht organisaties die onder haar toepassingsgebied vallen om risicogebaseerde cybersecurity-maatregelen te treffen, ernstige incidenten te melden aan de bevoegde autoriteit, en hun bestuursorgaan persoonlijk verantwoordelijk te maken voor cybersecurity-governance. In België is de richtlijn omgezet bij Wet van 26 april 2024; toezichthouder is het Centrum voor Cybersecurity België (CCB).

_Bron: Richtlijn (EU) 2022/2555 + Wet 26 april 2024 (BE-omzetting)_


## In de praktijk

<h3 id="kern-verplichtingen">Kern-verplichtingen</h3>

> [!tip]- Kern-verplichtingen
> (1) Risicogebaseerde cybersecurity-maatregelen: 10 minimaal vereiste domeinen (risicobeheer, incident handling, business continuity, supply chain security, encryptie, multi-factor authenticatie, training, ...). (2) Incidentmelding: 'vroege waarschuwing' aan CCB binnen 24 uur na bewustwording van een significant incident, gevolgd door incident-melding binnen 72 uur en eindrapport binnen 1 maand. (3) Bestuursorgaan-verantwoordelijkheid: persoonlijke aansprakelijkheid van bestuurders + verplichte cybersecurity-opleiding. (4) Sancties: tot 10 mln EUR of 2% van wereldwijde omzet voor essentiële entiteiten; tot 7 mln EUR of 1,4% voor belangrijke entiteiten. 🤖

<h3 id="link-met-interne-controle">Link met interne controle</h3>

> [!tip]- Link met interne controle
> NIS 2 is voor onderworpen entiteiten een 'compliance-driver' van de IT-controle-laag binnen het COSO-kader. Een externe auditor die de jaarrekening van een NIS 2-onderworpen cliënt controleert moet onder ISA 315 §A107 inschatten of cyberincidenten een materieel risico op de cijfers vormen, en onder ISA 250 de naleving van NIS 2-meldingsplichten meewegen. 🤖

<h3 id="wanneer-kom-je-dit-tegen-als-stagiair">Wanneer kom je dit tegen als stagiair</h3>

> [!tip]- Wanneer kom je dit tegen als stagiair
> Bij KMO-cliënten boven de 50 werknemers in sectoren als chemie, voedsel, productie of digitale diensten — adviesrol: helpen identificeren of cliënt onder NIS 2 valt en het cybersecurity-beleid documenteren. Bij grotere cliënten: NIS 2-compliance is onderdeel van governance-review en wordt in management letters opgenomen. 🤖


## Drempelwaarden

| Naam | Waarde | Eenheid | Gevolg |
|---|---|---|---|
|  |  | — |  |


## Voorwaarden / uitzonderingen

- Toepassingsgebied — essentiële versus belangrijke entiteiten 🤖
- Micro- en kleine ondernemingen (< 50 wn én jaaromzet ≤ 10 mln EUR) vallen in principe buiten NIS 2, tenzij ze als 'cruciale' aanbieder zijn aangewezen (bv. enige DNS-aanbieder voor een land). 🤖
> [!info]- Niet verwarren met [[dora-verordening]]
> DORA (EU 2022/2554) is sector-specifiek voor financiële diensten en ICT-derden; NIS 2 is sector-breed maar voor financiële sector treedt DORA terug als lex specialis. DORA legt operationele weerbaarheid bij banken, verzekeraars en ICT-leveranciers; NIS 2 dekt de bredere kritieke infrastructuur.
>
> _Trigger_: Vraagt examen welk regime voor een bank geldt? → DORA (lex specialis). Voor een chemiebedrijf? → NIS 2.

> [!info]- Niet verwarren met [[avg-interne-controle]]
> AVG (GDPR) beschermt persoonsgegevens-verwerking; NIS 2 beschermt de cyber-weerbaarheid van netwerk- en informatiesystemen ongeacht of er persoonsgegevens in zitten. Een datalek van klantgegevens raakt beide regimes; een ransomware-aanval op industriële procescontrolesystemen zonder persoonsgegevens raakt alleen NIS 2.


## Valkuilen

> [!warning]- Vaak fout: 'Klein bedrijf, dus geen NIS 2'
> ⚠️ Vaak fout: 'Klein bedrijf, dus geen NIS 2'. Sectorale drempel telt: een chemiebedrijf met 60 werknemers valt onder NIS 2 ondanks beperkte omvang. Test eerst sector, dan grootte. 🤖


> [!warning]- Meldingstermijnen worden gemakkelijk gemist: 24 uur is een 'vroege waarschuwing', geen volledig rapport — de meldingsplicht start vanaf 'bew…
> ⚠️ Meldingstermijnen worden gemakkelijk gemist: 24 uur is een 'vroege waarschuwing', geen volledig rapport — de meldingsplicht start vanaf 'bewustwording', niet vanaf vastgesteld incident. 🤖


> [!warning]- NIS 2 wordt vaak verward met DORA (Digital Operational Resilience Act, EU 2022/2554) — DORA geldt specifiek voor financiële sector + ICT-der…
> ⚠️ NIS 2 wordt vaak verward met DORA (Digital Operational Resilience Act, EU 2022/2554) — DORA geldt specifiek voor financiële sector + ICT-derden, NIS 2 voor de bredere economie. Financiële instellingen vallen primair onder DORA (lex specialis). 🤖



## Zie ook

- **Vereist kennis van**: [[it-general-controls]]

## Voorbeelden

### Yperse Werkplaats BV onder NIS 2

_Personages: Yperse Werkplaats BV, David Maes, Sofie Janssens_

Yperse Werkplaats BV (60 werknemers, productiesector, omzet € 12 mln) wordt door David Maes (financieel directeur) en Sofie Janssens (externe accountant) bekeken op NIS 2-toepasselijkheid.

1. Sectorale toets: 'productie' staat in Annex II → belangrijke entiteit-categorie.
2. Grootte-toets: 60 wn én omzet > 10 mln → boven middelgrote-drempel → valt onder NIS 2.
3. Gap-analyse: David documenteert de 10 verplichte domeinen — multi-factor authenticatie ontbreekt op het ERP, supply chain due diligence is informeel.
4. Roadmap: MFA uitrollen Q1, supply chain-vragenlijsten opzetten Q2, jaarlijkse bestuurder-training inplannen, incidentprocedure documenteren met CCB-meldingsstroom.
5. Sofie verwerkt dit als governance-bevinding in haar management letter.


