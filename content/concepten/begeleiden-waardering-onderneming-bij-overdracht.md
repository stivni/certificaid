---
title: Begeleiden van de waardering van een onderneming bij overdracht
tags:
- concept
- competentie
- po-3-0
linked_anchors:
- 3.0.taak.2
- 3.0.V
- 3.0.VI
programmaonderdelen:
- '3.0'
confidence: inferred
node_type: competentie
status: seed
schema_version: '1.6'
gegenereerd_uit: data/concepten/records/begeleiden-waardering-onderneming-bij-overdracht.json
gegenereerd_op: '2026-05-20'
---
# Begeleiden van de waardering van een onderneming bij overdracht 🤖

Adviesopdracht waarbij de gecertificeerd accountant — niet als expert-waarderingsspecialist maar als financiële adviseur — de cliënt begeleidt bij het opzetten of beoordelen van een waarderingsoefening voor een transactie. Hij selecteert passende methoden (DCF, multiples, NAV), toetst de inputs op redelijkheid, en vertaalt de waarderingsuitkomst naar onderhandelingstactiek. Diepe waarderingstheorie zit elders (PO 1.3, 2.5); hier ligt de focus op toepassing in een M&A-context.


## In de praktijk

- Vermeld altijd dat een waarderings-rapport geen prijs is — de prijs ontstaat uit onderhandeling waarin niet-financiële factoren (synergie, strategisch belang, persoonlijke voorkeur) mee meespelen.
- Voor wettelijke verslagen (inbreng in natura, fusie): hou je formelere methoden en zwaardere documentatie aan; voor onderhandelingsdoelen mag het lichter en flexibel.
- Onthoud dat sector-multiples sterk schommelen — gebruik liefst data van transacties in de laatste 18-24 maanden in dezelfde geografie.

## Stappen

### 1. Vaststellen van het waarderingsdoel en het perspectief

Verduidelijk of de waardering dient voor (a) een onderhandelingspositie van verkoper of koper, (b) een wettelijk voorbehouden verslag (inbreng in natura, fusie), (c) een familie-overdracht met fiscaal-juridische beslag, of (d) een ander doel (bv. echtscheiding, geschillen).

**Waarom?** Het doel stuurt zowel de methode-keuze als de toelaatbare assumptie-vrijheid. Een waardering voor onderhandeling kan ranges geven; een waardering voor een wettelijk verslag moet stelliger zijn en aan formele vereisten voldoen.

**📥 Input**:
- Mandaat cliënt → **Doel en bestemmeling van de waardering** _(vrije-tekst)_

**📤 Output**:
- Scope-memo waardering → **Doel + bestemmeling + waarderings-datum** _(tekst-document)_

**🛠️ Hoe**:

1. Identificeer bestemmeling (eigen cliënt, tegenpartij, notaris, rechter, fiscus).
2. Stel waarderings-datum vast (closing-datum, balans-datum, oprichtings-datum).
3. Stel formaat vast (rapport voor onderhandeling vs wettelijk verslag).
4. Bij wettelijke verslagen: kruis-link met [[opstellen-overname-verslaggeving-accountant]].

**Grondslag**: IBA M&A Guide Belgium 2022 §6

### 2. Selecteren waarderingsmethoden (minstens twee)

Kies typisch twee complementaire methoden: één income-based (DCF), één market-based (multiples). Bij vastgoed- of holdingvennootschappen: aanvullend asset-based (NAV).

**Waarom?** Een enkele methode geeft een schijnzekerheid; kruising van methoden geeft een vork waarin de meeste credibele waarde ligt. Voor wettelijke verslagen verlangt de ITAA-norm minstens twee methoden.

**📥 Input**:
- Aard van de onderneming → **Sector, kasstroom-profiel, asset-zwaarte** _(vrije-tekst)_

**📤 Output**:
- Methoden-keuze + motivering → **Welke + waarom** _(tekst-document)_

**🛠️ Hoe**:

1. DCF voor ondernemingen met voorspelbare kasstromen (dienstverlening, software, mature productiebedrijven).
2. Multiples (EBITDA-multiple of P/E) voor sectoren met goede peer-data (retail, IT-services, KMO-overnames).
3. NAV voor holdings, vastgoedvennootschappen, asset-zware bedrijven.
4. Substantiële waarde / liquidatiewaarde als ondergrens-check.
5. Bij twijfel: 2-3 methoden + vergelijking.

**Grondslag**: Vakdoctrine waardering; ITAA-norm-effectennorm §waarderingsmethoden

### 3. Toetsen van de inputs op redelijkheid

Onafhankelijk van wie de waardering uitvoert (cliënt, externe specialist): toets de kerninputs op redelijkheid — groeivoeten DCF, peer-selectie multiples, herwaarderingen NAV, normalisatie EBITDA.

**Waarom?** Inputs sturen de uitkomst meer dan de methode. Een DCF met overdreven groeivoet (10% perpetuiteit) levert een dubbele waardering tegenover redelijke 2%. Stagiair-rol: spot deze inputs vóór ze geconsacreerd raken in een rapport.

**📥 Input**:
- Waarderings-werkdocument → **Alle assumpties expliciet** _(tekst-document)_

**📤 Output**:
- Input-review-rapport → **Bevindingen per input + impact op uitkomst** _(tekst-document)_

**🛠️ Hoe**:

1. DCF-inputs: groeivoeten (vergelijk met sector + macro), WACC (vergelijk met peer-betas + risicovrije rente actueel + marktrisico-premie), terminal value (Gordon-formule check).
2. Multiples-inputs: peer-selectie (zelfde sector, zelfde grootte, zelfde geografie), uitgesloten outliers (ja/nee onderbouwd).
3. EBITDA-normalisatie: zie [[purchase-price-mechanismen]] §EBITDA-normalisatie.
4. NAV-inputs: actualiteit waarderingen (vastgoed: max 1 jaar oud), correcties latente belasting.
5. Sensitiviteit: ± 10% op kern-inputs, kijk hoe de waarde reageert.

> [!example]- Voorbeeld: Cliënt-koper wil bod uitbrengen op Tongerse Textielbedrijf NV (genormaliseerde EBITDA € 800.000, sector textiel-producti…
> Cliënt-koper wil bod uitbrengen op Tongerse Textielbedrijf NV (genormaliseerde EBITDA € 800.000, sector textiel-productie).
>
> 1. **Multiples-cross-check** 🧮
>
>    | Peer-multiple | Waarde |
>    |---|---:|
>    | Sector-mediaan EV/EBITDA 2024 | 5,5x |
>    | Toegepast op € 800.000 | € 4.400.000 |
>    | Premium 10% voor marktleiderschap | + € 440.000 |
>    | Indicatieve enterprise value | **€ 4.840.000** |
>    | − Netto financiële schuld | − € 320.000 |
>    | **Equity value** | **€ 4.520.000** |
>    
>

**Grondslag**: [[purchase-price-mechanismen]]; waarderings-vakdoctrine

### 4. Vertalen waardering naar onderhandelingstactiek

Help cliënt om de waarderings-vork te vertalen naar (a) een bod- of vraagprijs, (b) prijsformule (vast bedrag, EBITDA-multiple, locked-box, completion accounts), (c) earn-out of escrow indien er nog onzekerheden zijn.

**Waarom?** Waarderings-uitkomst is geen prijs. De prijs is wat partijen onderhandelen, gestructureerd in een formule die risico's alloceert. Earn-out en escrow vertalen onzekerheden in de waardering naar contractuele clausules.

**📥 Input**:
- Waarderings-vork → **Min – mediaan – max** _(boekhoudkundig-bedrag)_
- DD-bevindingen → **Risico's die de prijs beïnvloeden** _(tekst-document)_

**📤 Output**:
- Onderhandelings-strategie → **Openingsbod + onderbouwing + walk-away** _(tekst-document)_

**🛠️ Hoe**:

1. Cliënt-verkoper: openingsvraag in top van vork, walk-away rond mediaan.
2. Cliënt-koper: openingsbod onder mediaan, walk-away in top van vork.
3. Prijsformule: zie [[purchase-price-mechanismen]] voor locked-box vs completion accounts.
4. Earn-out (typisch 10-30% van prijs): koppel aan toekomstige EBITDA-realisatie als waardering een groeivoet veronderstelt die nog onzeker is.
5. Escrow (typisch 5-15% van prijs, 12-24 maanden): zekerheid voor R&W-claims.

**Grondslag**: [[purchase-price-mechanismen]]; IBA M&A Guide Belgium 2022 §5

### 5. Documenteren rapport en aanbevelingen

Lever een waarderings-rapport — voor onderhandelingsdoel meestal 5-10 pagina's, voor wettelijk verslag uitgebreider — met methoden, inputs, uitkomst-vork, gevoeligheids-analyse, conclusie.

**Waarom?** Het rapport is het document dat partijen en hun adviseurs gebruiken om over de prijs te onderhandelen. Bij latere geschillen (over waardering, R&W-claim, fiscale herziening) wordt het rapport teruggehaald — moet zelf-dragend en methodologisch defendable zijn.

**📥 Input**:
- Alle voorgaande analyses → **Methoden, inputs, uitkomsten** _(tekst-document)_

**📤 Output**:
- Waarderings-rapport → **Compleet document** _(tekst-document)_

**🛠️ Hoe**:

1. Structuur: management summary (vork in één tabel), beschrijving onderneming, gehanteerde methoden, inputs per methode, uitkomsten per methode, vergelijking + gewogen uitkomst, gevoeligheids-analyse, beperkingen.
2. Beperkingen expliciet: 'gebaseerd op door cliënt verstrekte cijfers, geen onafhankelijke audit' — anders sluipt ongewenste comfort.
3. Bij geschil-risico: voeg expliciete reasonable-care-clausule toe.
4. Bewaar werkversie + alle onderliggende berekeningen in dossier.

**Grondslag**: Vakdoctrine waardering; ITAA-deontologie


## Zie ook

- **Vereist kennis van**: [[purchase-price-mechanismen]]
- **Vereist kennis van**: [[overnameovereenkomst]]
- **Vereist kennis van**: [[controleverwerving-methodes]]
- **Vereist kennis van**: [[asset-deal-versus-share-deal]]

## Voorbeelden



