---
title: "Vennootschap onder firma"
concept_type: "instrument"
schema_version: "2.2"
status: "concept"
categorieen:
  - entiteit
ankers:
  - 3.0.I
  - 3.0.I.A
  - 3.0.I.B
tags:
  - concept
  - schema-2.2
  - type-instrument
  - cat-entiteit
  - status-concept
gegenereerd_uit: "data/concepten/records/vennootschap-onder-firma.json"
---

# Vennootschap onder firma

_Instrument_

🏢 Entiteit · Anchors: `3.0.I` · `3.0.I.A` · `3.0.I.B` · Wave: `cluster-extract-vennootschapsvormen-2026-05-28`

> [!info] 📝 **Concept** — content gevuld door cluster-extract; niet door mens-verify gegaan.

**Afk.**: VOF — **Synoniemen**: société en nom collectif (SNC) · general partnership — **Vertalingen**: fr: société en nom collectif (SNC)

## Definitie

📖 De vennootschap onder firma (VOF) is een personenvennootschap mét rechtspersoonlijkheid (art. 1:5 §2 WVV) waarvan alle vennoten onbeperkt en hoofdelijk aansprakelijk zijn voor de verbintenissen van de vennootschap (art. 4:14 WVV). Geen minimumkapitaal vereist. Alle vennoten zijn van rechtswege bestuurder tenzij de statuten anders bepalen (art. 4:22 WVV). De VOF is geregeld in WVV boek 4 (gemeenschappelijke bepalingen voor maatschap, VOF en CommV). Vennoten brengen in (geld, natura of nijverheid); winst- en verlies-verdeling volgens statuten of pro rata inbreng. Onderscheid met maatschap: VOF heeft rechtspersoonlijkheid; onderscheid met CommV: alle VOF-vennoten zijn beherende vennoten met volle aansprakelijkheid.

<small>📚 WVV — art. 1:5 — _wettekst_ · WVV — art. 4:14 — _wettekst_ · WVV — art. 4:22 — _wettekst_</small>

## Substantie

🔗 Praktisch: VOF is vandaag eerder een nicheke vorm — gebruikt bij (a) familievennootschappen waar volle persoonlijke betrokkenheid van alle vennoten gewenst is (en aansprakelijkheid niet beperkend hoeft te zijn), (b) vrije beroepers die collectief en persoonlijk hoofdelijk willen optreden (advocatenkantoren, notaris-vennootschappen historisch), (c) als doorkijk-vennootschap in fiscale planning waar VenB-onderwerping gewenst is maar bestuursoverhead beperkt moet blijven. Sterke punten: geen kapitaalvereiste, vereenvoudigde boekhouding mogelijk (CBN-advies 2019/11 — mits omzet < 500.000 EUR), eenvoudige oprichting, statutaire vrijheid. Zwakke punten: onbeperkte hoofdelijke aansprakelijkheid privévermogen alle vennoten — typisch onaanvaardbaar voor commerciële activiteit met derden-risico.

<small>📚 WVV — art. 4:14 — _wettekst_ · CBN 2019/11 — Beoogde personen - rechtsvorm — _advies_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Rationale

🔗 De VOF behoudt haar plaats in het WVV-pallet als 'rechtspersoonlijkheid + volle aansprakelijkheid'-combinatie — beoogd voor situaties waar partners bewust een persoonlijke betrokkenheid signaal willen geven naar schuldeisers, of waar het fiscale doorkijk-voordeel weinig waard is maar de eenvoud van oprichting + boekhouding belangrijk is. Historisch wortelt zij in het 'firma'-begrip (vennoten die onder eigen naam handelen). Het WVV behield slechts één regime voor personenvennootschappen-met-rechtspersoonlijkheid (was vroeger gesplitst tussen 'vennootschap onder gemeenschappelijke naam' en 'vennootschap onder firma' — nu samengevoegd onder boek 4).

<small>📚 WVV — art. 4:1 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Gebruikscontext

**Status**: `in-voege` · sinds **2019-05-01** · basis: WVV boek 4

**✅ Voor**
- 🔗 Geschikt voor: family-business met persoonlijke betrokkenheid alle vennoten; vrije beroepers die historisch hoofdelijk optreden; doorkijk-structuren in fiscale planning; kleine ondernemingen waar eenvoud + lage drempel primeren boven aansprakelijkheidsbescherming.

**🚫 Niet voor**
- 🔗 Niet voor: commerciële activiteit met externe-klant-risico → BV verkiezen voor aansprakelijkheidsbescherming. Niet voor: louter beleggings-structuur → maatschap verkiezen voor fiscale transparantie + geen rechtspersoonlijkheid-overhead.

**📋 Voorwaarden**
- 📖 Oprichting: (1) minstens 2 vennoten (natuurlijke of rechtspersonen), (2) statuten (kan onderhands — geen notariële akte verplicht in tegenstelling tot BV/NV/CV), (3) inschrijving KBO, (4) publicatie in BS. Geen financieel plan verplicht (anders dan BV/NV/CV).

**👍 Voordeel**
- 📖 (a) Geen minimumkapitaal. (b) Geen notariële akte voor oprichting — kostenefficiënt. (c) Vereenvoudigde boekhouding toegelaten mits omzet < 500.000 EUR (CBN 2019/11). (d) Statutaire vrijheid winst-verdeling. (e) Rechtspersoonlijkheid (vermogensafscheiding van privévermogen vennoten voor 'maatschappelijk vermogen').

**⚠️ Risico**
- 📖 (a) HOOFDRISICO: onbeperkte hoofdelijke aansprakelijkheid alle vennoten op privévermogen (art. 4:14 WVV). Schuldeiser van VOF kan rechtstreeks privévermogen vennoot uitwinnen (subsidiair: eerst poging op vennootschapsvermogen, dan privé). (b) Bij overlijden vennoot: VOF wordt ontbonden tenzij statuten anders bepalen — administratieve impact. (c) Onenigheid tussen vennoten: blokkering omdat bestuur default unaniem is.

## Bouwstenen

### 📜 Hoofdelijke aansprakelijkheid alle vennoten  
_`regel`_

📖 Art. 4:14 WVV: 'De vennoten in een vennootschap onder firma zijn hoofdelijk gehouden tot alle verbintenissen van de vennootschap.' Concreet: een schuldeiser van de VOF kan na uitwinning op het vennootschapsvermogen (of bij gebrek aan succes daar) zich richten tegen elk van de vennoten persoonlijk voor het geheel van de schuld. De vennoot die meer betaalt dan zijn deel heeft regres op de andere vennoten.

<small>📚 WVV — art. 4:14 — _wettekst_</small>

### ⚙️ Vermogensafscheiding — verschil met maatschap  
_`mechanisme`_

📖 Door haar rechtspersoonlijkheid (in tegenstelling tot maatschap, art. 1:5 §2 WVV) heeft de VOF een afgescheiden vennootschapsvermogen. Schuldeisers van de VOF moeten zich in principe eerst tot dat vermogen wenden (subsidiariteits-beginsel — art. 4:14 in fine). Persoonlijke schuldeisers van een vennoot kunnen geen rechtstreeks verhaal nemen op het vennootschapsvermogen — enkel op het aandeel van de vennoot + zijn winstuitkering (art. 4:15 WVV).

<small>📚 WVV — art. 4:14 — _wettekst_ · WVV — art. 4:15 — _wettekst_</small>

### 📜 Bestuur — alle vennoten van rechtswege  
_`regel`_

📖 Art. 4:22 WVV: alle vennoten zijn van rechtswege bestuurder tenzij de statuten anders bepalen. Beslissingen worden default genomen bij eenparigheid; statuten kunnen meerderheidsregels of gedelegeerd bestuur voorzien. Elke vennoot-bestuurder kan de VOF binden tov derden voor handelingen die onder het maatschappelijk doel vallen.

<small>📚 WVV — art. 4:22 — _wettekst_</small>

### 📜 Fiscale aanknoping VOF — VenB  
_`regel`_

📖 VOF is een vennootschap met rechtspersoonlijkheid → in principe onderworpen aan vennootschapsbelasting (VenB, art. 179 WIB92). Hetzelfde tarief-regime als BV/NV: 25 % standaard, 20 % KMO-tarief op eerste 100.000 EUR voor kwalificerende kleine vennootschappen (art. 215 WIB92). Optie: VOF kan kiezen voor 'fiscale transparantie' (PB-aanknoping bij vennoten) in zeer beperkte gevallen voorzien door WIB92 — quasi nooit van toepassing in moderne praktijk.

<small>📚 WIB92 — art. 179 — _wettekst_ · WIB92 — art. 215 — _wettekst_</small>

### ↪️ Vereenvoudigde boekhouding toegelaten  
_`uitzondering`_

📖 Anders dan BV/NV/CV mag de VOF een vereenvoudigde boekhouding voeren (kasdagboek + aankoopdagboek + verkoopdagboek + inventarisboek) mits de omzet beneden 500.000 EUR excl. BTW blijft (CBN-advies 2019/11 + art. III.85 WER). Boven die drempel: dubbele boekhouding verplicht.

<small>📚 CBN 2019/11 — Beoogde personen - rechtsvorm — _advies_ · WER — art. III.85 — _wettekst_</small>

## Voorbeelden

### 💡 VOF familie-restaurant (3 broers) 🔗

_Drie broers willen een traditioneel familie-restaurant opstarten. Allen brengen 15.000 EUR cash in (totaal 45.000 EUR). Allen werken voltijds in de zaak. Aanvaarden persoonlijke betrokkenheid + aansprakelijkheid als 'familietraditie'._

**Berekening:**
- Stap 1 — oprichting: onderhandse statuten (geen notariële akte verplicht). Kosten beperkt tot publicatie BS + KBO-inschrijving (~150 EUR).
- Stap 2 — boekingen oprichting: D 550 Bank 45.000 / C 100 Inbreng 45.000. Aandelen: 45 aandelen (15 per broer).
- Stap 3 — boekhouding: omzet jaar 1 verwacht ca. 280.000 EUR → vereenvoudigde boekhouding toegelaten (CBN 2019/11). Kasboek dagelijks, aankoop-/verkoopdagboek wekelijks, inventarisboek einde jaar.
- Stap 4 — fiscaal: VenB op winst (na bezoldigingen). Bij 70.000 EUR winst (na 3 × 30.000 EUR bezoldiging): VenB op 70.000 = 14.000 EUR (KMO-tarief 20 % — voorwaarden art. 215 §3 WIB92 vervuld want bezoldiging > minimum aan bedrijfsleider).
- Stap 5 — risico-beheer: alle broers persoonlijk aansprakelijk voor de schulden van de VOF (bv. bij voedselveiligheid-claim, ontslagvergoedingen, fiscale schulden). Beroepsaansprakelijkheidsverzekering essentieel.

→ **Resultaat**: VOF actief; eenvoudige oprichting + boekhouding; gedeeld eigenaarschap + gedeelde aansprakelijkheid. Bij toekomstige groei: overweeg omzetting naar BV voor aansprakelijkheidsbescherming.

<small>📚 WVV — art. 4:1 — _wettekst_ · WVV — art. 4:14 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### 💡 Aansprakelijkheid bij faillissement VOF 🔗

_VOF 'Bouwco' (2 vennoten A en B, elk 50 %) gaat failliet. Maatschappelijk vermogen: 0 EUR. Schulden: 180.000 EUR (RSZ, leveranciers, klant-schadeclaim). Vennoot A heeft privévermogen 250.000 EUR; B heeft 30.000 EUR._

**Berekening:**
- Stap 1 — uitwinning vennootschapsvermogen: 0 EUR — geen middelen om schulden te dekken.
- Stap 2 — hoofdelijke aansprakelijkheid (art. 4:14): elke vennoot kan voor het GEHEEL aangesproken worden (niet pro rata). Schuldeisers richten zich tegen A (heeft geld) voor de hele 180.000 EUR.
- Stap 3 — gevolg vennoot A: A betaalt 180.000 EUR uit privévermogen; resteert 70.000 EUR privé.
- Stap 4 — regres: A heeft regres-vordering op B voor zijn pro-rata-deel (50 % = 90.000 EUR). Maar B heeft slechts 30.000 EUR privé → A kan 30.000 EUR recupereren en blijft met 60.000 EUR verlies steken (B's onvermogen is A's risico).
- Stap 5 — fiscaal: privé-betaling onmogelijk te recupereren = aftrekbare beroepsverliezen indien aandelen tot beroepsvermogen behoorden — anders niet aftrekbaar.

→ **Resultaat**: Vennoot A betaalt 180.000 EUR, recupereert slechts 30.000 EUR van B → netto-verlies 150.000 EUR uit privévermogen. Illustreert het kernrisico van een VOF tegenover een BV (waar A's blootstelling tot zijn 15.000 EUR inbreng beperkt zou zijn).

<small>📚 WVV — art. 4:14 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### 💡 Omzetting VOF → BV bij groei 🔗

_VOF met 4 vennoten, 8 jaar oud, omzet 850.000 EUR (boven 500.000 drempel → al verplicht dubbele boekhouding). Vennoten willen aansprakelijkheid beperken en externe investeerder binnenhalen._

**Berekening:**
- Stap 1 — voorstel omzetting + verslag bestuur + tussentijdse balans (max 3 m. oud) + verslag bedrijfsrevisor over de staat.
- Stap 2 — AV met eenparigheid (VOF default — statutair kan anders) beslist omzetting.
- Stap 3 — notariële akte BV: statuten boek 5 WVV, financieel plan, benoeming bestuurders.
- Stap 4 — boekingen: D 100 Inbreng VOF 60.000 / C 100 Inbreng BV 60.000. Reserves/overgedragen winst blijven; kapitaalbegrip vervangen door 'inbreng' in BV.
- Stap 5 — fiscaal: geen vereffening (art. 14:2) → geen meerwaardebelasting op de overgang. Aansprakelijkheid van vennoten voor pre-omzetting-schulden van de VOF blijft persoonlijk (zij waren aansprakelijk vóór omzetting), maar nieuwe schulden vanaf BV-vorm zijn beperkt tot inbreng.

→ **Resultaat**: VOF omgevormd tot BV met behoud rechtspersoonlijkheid; aansprakelijkheid voor toekomstige schulden beperkt; klaar voor externe investeerder.

<small>📚 WVV — art. 14:2 — _wettekst_ · WVV — art. 14:6 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Valkuilen

### ⚠️ VOF en maatschap door elkaar halen

**Verkeerde assumptie**: Student denkt dat VOF = maatschap of dat beide fiscaal-transparant zijn.

**Kernpunt**: VOF heeft rechtspersoonlijkheid (art. 1:5 §2 WVV); maatschap niet (art. 1:5 §1). Gevolg: VOF is VenB-plichtig; maatschap is fiscaal-transparant (PB bij vennoten). Beide hebben onbeperkte hoofdelijke aansprakelijkheid — dat is hun overeenkomst — maar fiscaal staan ze diametraal anders.

<small>📚 WVV — art. 1:5 — _wettekst_ · WIB92 — art. 179 — _wettekst_ · WIB92 — art. 29 — _wettekst_</small>

### ⚠️ VOF kiezen omdat 'geen kapitaal nodig'

**Verkeerde assumptie**: Student of cliënt kiest VOF omwille van laagdrempelige oprichting + geen minimumkapitaal — zonder rekening te houden met de aansprakelijkheid.

**Kernpunt**: BV biedt ook 'geen minimumkapitaal' (sinds WVV) en aansprakelijkheidsbescherming. Bij elke commerciële activiteit met derden-risico is BV vrijwel altijd te verkiezen boven VOF. VOF blijft uitzonderlijk gerechtvaardigd in family-business met sterk persoonlijk vertrouwen of in fiscale doorkijk-constructies.

<small>📚 WVV — art. 4:14 — _wettekst_ · WVV — art. 5:3 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### ⚠️ Subsidiariteit van vennootschapsvermogen overschatten

**Verkeerde assumptie**: Student denkt dat een schuldeiser eerst grondig moet proberen het vennootschapsvermogen uit te winnen vóór hij naar de vennoten kan gaan.

**Kernpunt**: Subsidiariteit is procedureel beperkt: schuldeiser moet wel eerst aankloppen bij het vennootschapsvermogen (bv. door een veroordeling tegen de VOF), maar zodra er onvoldoende middelen in de VOF zitten (vaak snel vast te stellen bij faillissement), kan onmiddellijk privévermogen vennoten worden aangesproken voor het VOLLEDIGE bedrag (art. 4:14 WVV).

<small>📚 WVV — art. 4:14 — _wettekst_</small>

## Accountant-perspectieven

### Adviseur — VOF-cliënt en risico-bewaking

_De accountant wijst de cliënt op de aansprakelijkheidsrisico's en begeleidt bij overstap naar BV indien gepast._

#### 🧭 Adviseur

##### 📜 Advies VOF behouden of omzetten naar BV  
_`regel`_

🔗 Bij elke jaarrekening-bespreking: evalueer het aansprakelijkheidsrisico. Triggers voor omzetting-advies: (a) groei omzet > 500.000 EUR (dubbele boekhouding al verplicht — verlies eenvoud-voordeel VOF), (b) externe investeerder gewenst (BV biedt aandelen-structuur), (c) gestegen derden-risico (claims, fiscaal, sociaal), (d) opvolging in beeld (BV-aandelen makkelijker overdraagbaar via schenking).

<small>📚 WVV — art. 4:14 — _wettekst_ · WVV — art. 14:2 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

#### 💰 Fiscaal adviseur

##### 👣 Aangifte VenB VOF  
_`stap`_

📖 VOF dient gewone VenB-aangifte (formulier 275.1) zoals BV/NV. Bezoldigingen aan vennoten worden geboekt als bedrijfsleidersbezoldigingen (rek. 618) en zijn aftrekbaar voor VenB; bij de vennoot belastbaar in PB (art. 32 WIB92). Indien VOF kwalificeert als 'kleine vennootschap' (art. 1:24 WVV): KMO-tarief 20 % op eerste 100.000 EUR mits voorwaarden (waaronder minimum-bezoldiging aan bedrijfsleider — art. 215 §3 WIB92).

<small>📚 WIB92 — art. 179 — _wettekst_ · WIB92 — art. 32 — _wettekst_ · WIB92 — art. 215 — _wettekst_</small>

## Verder lezen (scope-out)

- → Vergelijking met andere vormen → [[ondernemingsvormen]] _(moet-verwijzen)_
- → Verwante personenvennootschap met 2 vennoten-typen → [[commanditaire-vennootschap]] _(moet-verwijzen)_
- → Aansprakelijkheid bestuurders/vennoten → [[bestuurdersaansprakelijkheid]] _(moet-verwijzen)_

## Relaties

### `valt_onder`
- [[ondernemingsvormen]]
### `vergelijkbaar_met`
- [[commanditaire-vennootschap]]
    - **Gelijkenissen**:
        - Beide personenvennootschappen onder WVV boek 4
        - Beide met rechtspersoonlijkheid (art. 1:5 §2)
        - Beide geen minimumkapitaal
        - Beide VenB-plichtig
        - Beide mogen vereenvoudigde boekhouding voeren (mits omzet < 500.000 EUR)
    - **Verschillen**:
        - VOF: ALLE vennoten zijn hoofdelijk onbeperkt aansprakelijk (art. 4:14) · CommV: ALLEEN gecommanditeerde vennoten zijn onbeperkt aansprakelijk; commanditaire vennoten zijn beperkt tot inbreng
        - VOF: alle vennoten van rechtswege bestuurder · CommV: alleen gecommanditeerden mogen besturen (commanditaire vennoot die bestuurt verliest aansprakelijkheidsbescherming)
    - ⚠️ **Verwarringsrisico**: Beide vormen zijn personenvennootschappen onder boek 4; verschil zit in twee-trapse aansprakelijkheidsstructuur van CommV.
