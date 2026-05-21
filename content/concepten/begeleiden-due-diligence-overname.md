---
title: Begeleiden van due diligence bij overname (verkoper- of koperszijde)
tags:
- concept
- competentie
- po-3-0
linked_anchors:
- 3.0.taak.2
- 3.0.V
programmaonderdelen:
- '3.0'
confidence: inferred
node_type: competentie
status: seed
schema_version: '1.6'
gegenereerd_uit: data/concepten/records/begeleiden-due-diligence-overname.json
gegenereerd_op: '2026-05-21'
---
# Begeleiden van due diligence bij overname (verkoper- of koperszijde) 🔗

Operationele competentie waarbij de gecertificeerd accountant het due-diligence-proces organiseert en uitvoert: vendor due diligence aan verkoperszijde (rapport voorbereiden voor potentiële kopers) of buy-side due diligence aan koperszijde (financial-tax-legal-HR-checks). Het DD-resultaat bepaalt de prijsformule, de R&W en eventuele earn-out- of escrow-clausules in de overnameovereenkomst.



## In de praktijk

- Een vendor DD versnelt de verkoop met 4-8 weken en geeft de verkoper controle over de narratief — risico's worden gestructureerd gepresenteerd in plaats van defensief beantwoord.
- Buy-side DD met multipele kandidaat-targets: standaardiseer de werkmethode en het rapport-format zodat de cliënt kandidaten kan vergelijken op identieke assen.
- DD-rapporten zijn vertrouwelijk en worden in het cliëntendossier bewaard met striktere toegang dan reguliere accountantsdossiers — typisch named-access in plaats van team-access.

## Stappen

### 1. Vaststellen perspectief, scope en team

Bevestig met de cliënt of het mandaat verkoper- (vendor DD) of koperszijde (buy-side DD) is, welke DD-werkstromen meegaan (financial, tax, legal, HR, IT, milieu, commercial) en wie de teamleden zijn per werkstroom.

**Waarom?** Vendor DD heeft een andere oriëntatie (kwetsbaarheden vooraf identificeren en remediëren of disclosen) dan buy-side DD (risico's vinden die de prijs of de R&W beïnvloeden). De scope-keuze bepaalt budget, tijdslijn en welke externe specialisten (fiscalist, M&A-jurist) je betrekt.

**📥 Input**:
- Mandaat cliënt → **Verkoper of koper, gewenste DD-scope** _(vrije-tekst)_
- Profiel doelvennootschap → **Sector, omvang, hoofdrisico-categorieën** _(vrije-tekst)_

**📤 Output**:
- DD-plan-document → **Scope, werkstromen, team, tijdslijn, budget** _(tekst-document)_

**🛠️ Hoe**:

1. Definieer perspectief: vendor DD vs buy-side DD.
2. Lijst de werkstromen: financial (boekhouding + analyses), tax (vennootschapsbelasting + btw + lokale belastingen), legal (contracten, geschillen, vergunningen), HR (CAO's, personeelsdossiers, pensioenverplichtingen), IT (systemen, licenties, cyber), milieu/CSR (vergunningen, claims), commercial (klanten, leveranciers, marktpositie).
3. Per werkstroom: één lead-persoon (zelf, collega, externe specialist).
4. Schat tijdslijn (typisch 4-8 weken voor KMO, 8-16 weken voor middelgroot).
5. Confidentiality vooraf via NDA — zie [[confidentiality-overname]].

**Grondslag**: [[due-diligence-overname]]; [[confidentiality-overname]]

### 2. Opzetten dataroom en information request list

Bij vendor DD: bouw en cureer een (virtuele) dataroom met georganiseerde documentatie. Bij buy-side DD: lever een gestructureerde information request list aan de verkoper en monitor uploads.

**Waarom?** Een goed georganiseerde dataroom versnelt de DD met factor 2-3 en vermindert vragen-iteraties. Bij buy-side DD: ontbrekende documenten zijn een signaal — soms van onordelijke administratie, soms van bewust verzwijgen.

**📥 Input**:
- DD-werkstromen (stap 1) → **Lijst van documenten per werkstroom** _(tekst-document)_

**📤 Output**:
- Dataroom-index of information request list → **Hoofdstukken per werkstroom + checklist per item** _(structuur)_

**🛠️ Hoe**:

1. Gebruik een standaard-template (financial: 5 jaar jaarrekeningen, hulpboekhouding, audit-files, fiscale aangiften; legal: aandeelhoudersregister, statuten, materiële contracten, geschillen-lijst; HR: arbeidsovereenkomsten directie, CAO's, pensioenfondsbeloften).
2. Vendor DD: cureer documenten — verwijder of redact GDPR-gevoelige content vóór externe toegang.
3. Buy-side DD: maak een gating-volgorde — basisdocumenten eerst, gevoelige (klantcontracten) pas na binding LOI.
4. Tracking: log per document datum-upload, datum-review, vragen-status.

**Grondslag**: [[due-diligence-overname]] §dataroom

> [!warning]- Plaats nooit ongeredigeerde personeelsdossiers in de dataroom — GDPR overtreding en bovendien onevenredig voor de koper-fase.
>
> _Vaak fout gedaan_: Vendor uploadt 'alles' uit angst voor niet-disclosure, leverend in GDPR-risico.

### 3. Uitvoeren financial due diligence

Analyseer de gerapporteerde resultaten, de kwaliteit van de winst (quality of earnings), de werkkapitaal-positie, de netto financiële schuld en de kasstromen.

**Waarom?** Kopers betalen op basis van een prijsformule die typisch start van EBITDA (× multiple) of van enterprise value − netto financiële schuld − minimum werkkapitaal. Alle drie de componenten moeten zuiver gerapporteerd zijn. Niet-recurrente baten, eigenaar-vergoedingen boven markt, of activerings-correcties kunnen de werkelijke EBITDA wezenlijk verlagen.

**📥 Input**:
- Jaarrekeningen 3-5 jaar → **Resultatenrekening + balans + toelichting** _(boekhoudkundig-overzicht)_
- Hulpboekhouding → **Klanten, leveranciers, voorraad-detail** _(boekhoudkundig-overzicht)_

**📤 Output**:
- Quality-of-earnings-rapport → **Genormaliseerde EBITDA + commentaar + risico-lijst** _(tekst-document)_

**🛠️ Hoe**:

1. Normalisaties EBITDA: schrap niet-recurrente baten/kosten (verzekeringsuitkeringen, eenmalige verkoop activum), corrigeer voor boven-markt vergoedingen van familie-eigenaars, herclassificeer activeringen die in feite operationele kosten zijn.
2. Netto financiële schuld: financiële schulden − cash, plus debt-like items (achterstallige sociale schulden, hangende fiscale geschillen, pensioenverplichtingen).
3. Normaal werkkapitaal: 12-maand-gemiddelde van (klanten + voorraad) − leveranciers (zonder cash en zonder financiële schulden).
4. Kasstromen: bouw cash-conversie ratio (cashflow uit operaties / EBITDA) — onder 80% = inefficiënt werkkapitaal of materiële niet-cash baten.

> [!example]- Voorbeeld: Buy-side financial DD op Tongerse Textielbedrijf NV — gerapporteerde EBITDA jaar N: € 850.000
> Buy-side financial DD op Tongerse Textielbedrijf NV — gerapporteerde EBITDA jaar N: € 850.000.
>
> 1. **Normalisatie EBITDA** 🧮
>
>    | Post | Bedrag |
>    |---|---:|
>    | Gerapporteerde EBITDA | € 850.000 |
>    | − Eenmalige verzekeringsuitkering | − € 75.000 |
>    | + Boven-markt loon bestuurder-eigenaar | + € 60.000 |
>    | − Eenmalige verkoop machine | − € 35.000 |
>    | **Genormaliseerde EBITDA** | **€ 800.000** |
>    
>

**Grondslag**: [[due-diligence-overname]] §financial; [[purchase-price-mechanismen]] §EBITDA-normalisatie

### 4. Uitvoeren tax due diligence

Onderzoek vennootschapsbelasting (laatste 5 jaar), btw (laatste 3 jaar), bedrijfsvoorheffing, lokale belastingen, fiscale ruling en mogelijke fiscale claims (correcties, lopende discussies).

**Waarom?** Onontdekte fiscale schulden gaan bij een share deal automatisch mee — daarom is tax DD bij share deals een 'must'. De geschatte fiscale aansprakelijkheid stuurt direct de R&W-formulering, indemnification-cap en mogelijk een specifieke fiscale escrow.

**📥 Input**:
- Vennootschapsbelasting-aangiften 5 jaar → **Aangifte + bijlagen** _(wettelijk-document)_
- Btw-aangiften 3 jaar → **Periodieke aangiften + klant-/leveranciersluisters** _(wettelijk-document)_
- Correspondentie fiscus → **Vraag om inlichtingen, taxatie-bericht, bezwaarschriften** _(wettelijk-document)_

**📤 Output**:
- Tax DD-rapport → **Identificeerde risico's + ingeschatte impact + remediatie-voorstellen** _(tekst-document)_

**🛠️ Hoe**:

1. Vennootschapsbelasting: check de bijgehouden boekhoudkundige reserves, de DBI-claims, de aftrek innovatie-inkomsten, de afschrijvings-methoden. Hoge afschrijvings-verschillen → fiscale latentie.
2. Btw: controleer cohérence aangiften vs jaarrekening-omzet, gemengd-btw-statuut, intracommunautaire diensten.
3. Verjaringstermijnen: 3 jaar normaal, 7 jaar bij fraude — risico-fenster.
4. Lopende geschillen: vraag specifiek naar bezwaarschriften, rulings-aanvragen, fiscale audits.
5. Bij ontdekte risico's: bedrag inschatten + suggestie (R&W-clausule, specifieke indemnification, escrow).

**Grondslag**: [[due-diligence-overname]] §tax; [[indemnification-overname]]

### 5. Synthetiseren bevindingen in DD-rapport

Lever een gesynthetiseerd rapport dat de hoofdbevindingen per werkstroom, hun impact op prijs en R&W, en de aanbevolen vervolgstappen voor de cliënt bevat.

**Waarom?** Het DD-rapport is het inputs-document voor de transactiedocumentatie (R&W, indemnification, escrow, eventuele earn-out). Cliënt en M&A-jurist gebruiken het direct om in onderhandeling met de tegenpartij te treden.

**📥 Input**:
- Werkstroom-rapporten (financial, tax, legal, HR) → **Bevindingen + risico's per werkstroom** _(tekst-document)_

**📤 Output**:
- Geconsolideerd DD-rapport → **Executive summary + werkstroom-secties + risico-matrix + impact-tabel** _(tekst-document)_

**🛠️ Hoe**:

1. Schrijf een executive summary van maximaal 1 pagina: 5-7 belangrijkste bevindingen + impact-kleurcode (rood/oranje/groen).
2. Per werkstroom: 2-3 pagina's met bevindingen, gevolg, aanbeveling.
3. Risico-matrix: lijst alle 'red items' met kwantificering en aanbevolen mitigatie (R&W, indemnification, prijsaanpassing, walk-away).
4. Impact-tabel: geef voor elk top-risico het effect op prijs (€), op closing (vertraging), of op R&W (specifieke clausule).
5. Vendor DD: lever het rapport vóór bookrunner-fase aan investment-banker; buy-side DD: lever vóór final LOI of SPA-onderhandeling.

**Grondslag**: [[due-diligence-overname]]; ITAA-deontologie

> [!warning]- Houd het rapport feitelijk — geen aanbevelingen over of de transactie 'goed' is. Dat is een commerciële beslissing van cliënt.
>
> _Vaak fout gedaan_: Accountant adviseert 'koop niet' of 'verkoop wel'; gaat buiten zijn rol.


## Zie ook

- **Vereist kennis van**: [[due-diligence-overname]]
- **Vereist kennis van**: [[representations-and-warranties]]
- **Vereist kennis van**: [[indemnification-overname]]
- **Vereist kennis van**: [[purchase-price-mechanismen]]
- **Vereist kennis van**: [[closing-condities-precedent]]
- **Vereist kennis van**: [[confidentiality-overname]]

## Voorbeelden



