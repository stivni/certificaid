---
title: "Fiscale residentie"
concept_type: "kader"
schema_version: "2.2"
status: "concept"
categorieen:
  - regeling
  - kader
ankers:
  - 2.8.IV
tags:
  - concept
  - schema-2.2
  - type-kader
  - cat-regeling
  - cat-kader
  - status-concept
gegenereerd_uit: "data/concepten/records/fiscale-residentie.json"
---

# Fiscale residentie

_Kader_

📋 Regeling · 🏛️ Kader · Anchors: `2.8.IV` · Wave: `skeleton-btw-internationaal-2026-05-28`

> [!info] 📝 **Concept** — content gevuld door cluster-extract; niet door mens-verify gegaan.

**Synoniemen**: fiscale woonplaats · tax residence · rijksinwonerschap — **Vertalingen**: fr: résidence fiscale · en: tax residence

## Definitie

📖 Fiscale residentie is het kernaanknopingspunt dat bepaalt of een persoon of vennootschap in België onderworpen is aan de onbeperkte belastingplicht (= belasting op het wereldwijde inkomen via personenbelasting of vennootschapsbelasting) dan wel aan de beperkte belastingplicht voor niet-inwoners (BNI — enkel Belgische bron-inkomsten). Voor natuurlijke personen: rijksinwoner is wie zijn woonplaats OF de zetel van zijn fortuin in België heeft gevestigd (art. 2, 1° WIB92). Voor vennootschappen: Belgisch ingezetene is de vennootschap met maatschappelijke zetel, voornaamste inrichting of zetel van bestuur of beheer in België (art. 2, 5° WIB92). Bij conflicterende residentie in twee staten lossen de tie-breaker rules van het bilaterale dubbelbelastingverdrag (DBV) het conflict op (typisch art. 4 OESO-modelverdrag).

<small>📚 WIB92 — art. 2 — 1° — _wettekst_ · WIB92 — art. 2 — 5° — _wettekst_ · OESO-modelverdrag — art. 4 — _modelverdrag_</small>

## Substantie

🔗 Fiscale residentie is dé poortwachter van het internationaal fiscaal recht. Stel: een Belgisch ICT-consultant verhuist naar Dubai. Zolang hij Belgisch rijksinwoner blijft (vrouw + kinderen blijven in Gent, hij keert wekelijks terug, fortuin staat op Belgische bank), wordt hij in België belast op zijn wereldwijde loon — ook op het loon dat hij verdient in Dubai. Pas wanneer de zetel van zijn fortuin én zijn woonplaats effectief naar Dubai verhuizen, wordt hij niet-inwoner en betaalt hij in België enkel BNI op zijn eventuele Belgische bronnen (huurinkomsten uit Belgische woning, etc.). Voor vennootschappen werkt het identiek: een NV met statutaire zetel in Luxemburg maar werkelijke leiding (bestuursvergaderingen, dagelijks beleid) in Antwerpen wordt fiscaal als Belgische vennootschap behandeld — onderworpen aan VenB op het wereldwijde resultaat (art. 179 WIB92).

<small>📚 WIB92 — art. 2 — 1° — _wettekst_ · WIB92 — art. 2 — 5° — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Rationale

🔗 Het residentie-beginsel is de fundering van het 'wereldwijde-inkomen-beginsel': een staat heeft het recht om zijn inwoners op hun TOTALE inkomen te belasten, omdat ze de baten van de Belgische samenleving genieten (rechtsbescherming, infrastructuur, sociale zekerheid). Niet-inwoners worden enkel belast op inkomsten die effectief uit Belgische bron komen (BNI — bron-beginsel). Wanneer beide criteria leiden tot dubbele residentie (twee staten beschouwen dezelfde persoon als inwoner), zou dat tot dubbele belasting leiden. Daarom voorzien DBVs in tie-breaker-cascades (art. 4 OESO-MV voor natuurlijke personen: permanente woning → centrum vitale belangen → gewone verblijfplaats → nationaliteit → overleg tussen staten; voor vennootschappen: 'place of effective management' of mutual agreement). De residentie-vaststelling is fact-intensive — geen mechanische test maar een weging van objectieve omstandigheden.

<small>📚 OESO-modelverdrag — art. 4 — commentaar — _modelverdrag_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Gebruikscontext

**Status**: `in-voege` · basis: WIB92 art. 2 (definities rijksinwoner en vennootschap-residentie)

Stabiel regime sinds invoering WIB92. Aanpassing voor vennootschappen in 2020 (Wet 25 december 2017): de 'voornaamste inrichting' en 'zetel van bestuur of beheer' werden verduidelijkt in lijn met het WVV-statutaire-zetel-leerstuk.

**✅ Voor**
- 🔗 Elke vraag 'wie betaalt welke belasting in België?': natuurlijke persoon → personenbelasting (rijksinwoner) of BNI/nat (niet-rijksinwoner); vennootschap → vennootschapsbelasting (Belgisch ingezetene) of BNI/ven (buitenlandse vennootschap). De residentie-vaststelling is altijd de eerste stap.
- 🔗 Beoordelen of een verhuizing naar het buitenland (of vanuit het buitenland) fiscale gevolgen heeft (exit-tax, BNI-overgang, einde wereldwijd-inkomen-belasting).

**📋 Voorwaarden**
- 📖 Natuurlijke persoon — rijksinwoner indien aan minstens één van twee criteria voldaan: (1) WOONPLAATS in België = hoofdverblijf, plaats waar gezin is gevestigd, sociale en familiale binding; (2) ZETEL VAN FORTUIN = plaats van waaruit het vermogen wordt beheerd. Deze criteria worden 'naar de omstandigheden beoordeeld' (art. 2 — 1° in fine). Wettelijk vermoeden: wie ingeschreven is in het Rijksregister wordt geacht zijn woonplaats in België te hebben — behoudens tegenbewijs.
- 📖 Voor gehuwden / wettelijk samenwonenden (niet feitelijk gescheiden): de belastingwoonplaats wordt bepaald door de plaats waar HET GEZIN is gevestigd — niet individueel. Beide partners hebben dezelfde fiscale woonplaats zolang het gezin samenleeft (art. 2 — 1° laatste lid).
- 📖 Vennootschap — Belgisch ingezetene indien EEN VAN: (1) maatschappelijke zetel in België (statutair); (2) voornaamste inrichting in België; (3) zetel van bestuur of beheer in België. Het belangrijkste materiële criterium is de WERKELIJKE LEIDING (place of effective management): waar nemen de bestuurders de strategische beslissingen, waar vinden de raadsvergaderingen plaats. Een statutaire zetel in het buitenland weegt niet door als de leiding feitelijk vanuit België gebeurt.

**🟢 Indicaties**
- 🔗 Indicatoren voor Belgisch rijksinwonerschap natuurlijke persoon: inschrijving Rijksregister, gezinswoning in België, kinderen op Belgische school, hoofdbankrekening en kredieten in België, beroepsactiviteit hoofdzakelijk in België, sociale binding (clubs, vrienden, huisarts).
- 🔗 Indicatoren werkelijke leiding vennootschap in België: bestuursvergaderingen in België; voornaamste bestuurders wonen in België; strategische beslissingen worden in België genomen; centrale boekhouding en bankrekening in België; correspondentie en archieven in België.

**⚠️ Risico**
- 🔗 Niet-erkende residentie-overdracht: emigratie zonder voldoende substantie-verlies in België (cliënt houdt huis aan, gezin blijft, fortuin op Belgische bank) — fiscus weigert het verlies van rijksinwonerschap en blijft belasting heffen op het wereldwijde inkomen. Tegenbewijs van Rijksregister-vermoeden vergt sterke feitelijke onderbouwing.
- 🔗 Dubbele residentie zonder DBV: wanneer cliënt verhuist naar een land waar België geen dubbelbelastingverdrag mee heeft (bv. niet-EU + geen DBV), bestaat het risico van dubbele belasting op hetzelfde inkomen — beide staten passen onbeperkte belastingplicht toe en er is geen tie-breaker.

## Sub-concepten

### 📦 Rijksinwoner — natuurlijke personen (art. 2 — 1° WIB92)  
_`regime` (subconcept)_

#### Definitie

📖 Een natuurlijke persoon is Belgisch rijksinwoner wanneer hij OFWEL zijn woonplaats OFWEL de zetel van zijn fortuin in België heeft gevestigd. De twee criteria zijn alternatief, niet cumulatief — voldoen aan één criterium volstaat. Bijzondere categorieën worden eveneens als rijksinwoner aangemerkt: Belgische diplomaten in het buitenland, andere Belgische ambtenaren in het buitenland (mits niet duurzaam verblijfhoudend), en hun inwonende gezinsleden.

<small>📚 WIB92 — art. 2 — 1° a-d — _wettekst_</small>

#### Substantie

🔗 Woonplaats verwijst naar de plaats waar de persoon werkelijk leeft, waar zijn gezin gevestigd is, zijn sociale en persoonlijke bindingen liggen. Zetel van fortuin verwijst naar de plaats van waaruit hij zijn vermogen beheert — typisch waar hij zijn beleggingsbeslissingen neemt, zijn bankrekening houdt, zijn fiscale planning doet. Een Belgische gepensioneerde die in Frankrijk woont maar zijn vermogen volledig via een Belgische private banker beheert kan op grond van 'zetel van fortuin' toch rijksinwoner zijn — al wordt dit door een DBV (België-Frankrijk) typisch ten gunste van Frankrijk opgelost.

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

#### 📜 Wettelijk vermoeden Rijksregister-inschrijving  
_`regel`_

📖 Wie ingeschreven is in het Rijksregister wordt geacht zijn woonplaats in België te hebben gevestigd — behoudens tegenbewijs. Dit is een weerlegbaar vermoeden: de belastingplichtige moet aantonen dat zijn werkelijke woonplaats elders ligt. Tegenbewijs gebeurt door feitelijke elementen (huurcontract buitenland, schoolgaande kinderen elders, dagelijkse aanwezigheid op andere plaats, etc.).

<small>📚 WIB92 — art. 2 — 1° — _wettekst_</small>

#### 📜 Gezin bepaalt de woonplaats (gehuwden / samenwonenden)  
_`regel`_

📖 Voor gehuwden of wettelijk samenwonenden die een gemeenschappelijke aanslag krijgen, wordt de belastingwoonplaats bepaald door de plaats waar het gezin is gevestigd. Dit voorkomt dat partners afzonderlijke residenties kunnen hebben binnen één gezin. Uitzonderingen: feitelijke scheiding, jaar van huwelijk/scheiding/overlijden (art. 126 §2 WIB92 — geen gemeenschappelijke aanslag in die jaren).

<small>📚 WIB92 — art. 2 — 1° in fine — _wettekst_</small>

### 📦 Belgisch ingezetene — vennootschappen (art. 2 — 5° WIB92)  
_`regime` (subconcept)_

#### Definitie

📖 Een vennootschap is fiscaal Belgisch ingezetene wanneer zij rechtspersoonlijkheid bezit (Belgisch of buitenlands recht) en haar maatschappelijke zetel, voornaamste inrichting OF zetel van bestuur of beheer in België heeft. De drie criteria zijn alternatief. Het belangrijkste materiële criterium is de werkelijke leiding (place of effective management) — waar nemen de bestuurders de strategische beslissingen.

<small>📚 WIB92 — art. 2 — 5° — _wettekst_</small>

#### Substantie

🔗 Het criterium 'zetel van bestuur of beheer' is een feitelijke test. Een vennootschap die statutair in Cyprus is opgericht maar waarvan de twee Belgische bestuurders alle vergaderingen in Brussel houden, alle contracten in België tekenen en alle strategische beslissingen vanuit hun Belgische kantoor nemen, wordt fiscaal als Belgische vennootschap behandeld (onderworpen aan VenB op het wereldwijde resultaat). Dit blokkeert pure offshore-constructies waar de statutaire zetel artificieel naar een laagbelaste jurisdictie verschoven wordt.

<small>📚 WIB92 — art. 2 — 5° — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Bouwstenen

### 💡 Onbeperkte versus beperkte belastingplicht  
_`begrip`_

🔗 Residentie bepaalt de OMVANG van de belastingplicht. ONBEPERKT (wereldwijd inkomen): geldt voor Belgische rijksinwoners (PB op wereldwijd loon en vermogen) en Belgische vennootschappen (VenB op wereldwijde winst). BEPERKT (enkel Belgische bron): geldt voor niet-inwoners — natuurlijke personen (BNI/nat op art. 228 §2 WIB92-inkomsten) en buitenlandse vennootschappen (BNI/ven op art. 233 WIB92-inkomsten zoals Belgische vaste inrichting, Belgische onroerende inkomsten). DBVs verminderen de daadwerkelijke belasting maar wijzigen het residentie-aanknopingspunt zelf niet.

<small>📚 WIB92 — art. 5 + art. 227-248 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### 📏 183-dagen-indicatie (geen wettelijk criterium)  
_`drempel`_

🔗 Anders dan bv. in Nederland of Frankrijk, kent het WIB92 GÉÉN wettelijke 183-dagen-test voor rijksinwonerschap. De Belgische test is volledig FEITELIJK (woonplaats + zetel van fortuin). De 183-dagen-grens komt wél voor in DBV-tie-breaker-cascades (art. 4 OESO-MV — 'gewone verblijfplaats' wordt vaak feitelijk afgemeten aan dagen-aanwezigheid in een staat) en in sommige bronstaat-regels voor expats (art. 15 OESO-MV — bezoldigingen). Een Belgische rijksinwoner die minder dan 183 dagen in België verblijft maar wiens gezin in België blijft, BLIJFT rijksinwoner.

<small>📚 OESO-modelverdrag — art. 4 + art. 15 — _modelverdrag_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### ⚙️ Tie-breaker cascade natuurlijke personen (art. 4 OESO-MV)  
_`mechanisme`_

📖 Wanneer twee verdragstaten beide een persoon als inwoner kwalificeren (dubbele residentie), past het DBV de tie-breaker-cascade toe, in volgorde: (1) PERMANENTE WONING — de staat waar de persoon over een duurzaam beschikbare woning beschikt; (2) CENTRUM VAN VITALE BELANGEN — als beide staten een permanente woning bieden: waar liggen de persoonlijke en economische bindingen het sterkst (gezin, beroep, sociale relaties); (3) GEWONE VERBLIJFPLAATS — als de banden in beide staten gelijkwaardig zijn: waar verblijft de persoon gewoonlijk (feitelijke aanwezigheid); (4) NATIONALITEIT — als de gewone verblijfplaats in beide staten of in geen van beide ligt; (5) ONDERLING OVERLEG tussen bevoegde autoriteiten van de verdragstaten — als nationaliteit geen oplossing biedt.

<small>📚 OESO-modelverdrag — art. 4 lid 2 a-d — _modelverdrag_</small>

### ⚙️ Tie-breaker vennootschappen (art. 4 lid 3 OESO-MV)  
_`mechanisme`_

🔗 Voor vennootschappen met dubbele residentie hanteert het OESO-modelverdrag (versie 2017) een MAP-regel: de bevoegde autoriteiten van de verdragstaten lossen de residentie op in onderling overleg, met als criteria typisch de plaats van werkelijke leiding (place of effective management), de plaats van oprichting, en eventuele andere relevante factoren. Oudere versies van het MV (pre-2017) gebruikten 'place of effective management' als hoofdcriterium. Veel bestaande Belgische DBVs werken nog met de oude formulering.

<small>📚 OESO-modelverdrag — art. 4 lid 3 (versie 2017) — _modelverdrag_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Voorbeelden

### 💡 Belgische consultant verhuist naar Dubai 🔗

_Jonas Verdonck is consultant gespecialiseerd in IT-infrastructuur. Hij tekent in 2026 een 2-jarig contract met een Emirati-bedrijf in Dubai. Hij huurt daar een appartement, schrijft zich uit het Rijksregister uit. Zijn echtgenote en twee kinderen blijven in Gent (school, woonst). Hij keert om de zes weken een week terug naar Gent._

Analyse:

1. **Uitschrijving Rijksregister** — het wettelijke vermoeden van Belgische woonplaats valt weg. Maar de feitelijke beoordeling 'naar de omstandigheden' blijft.

2. **Gezin in België** — art. 2 §1 1° in fine: 'Voor gehuwden (...) wordt de belastingwoonplaats bepaald door de plaats waar het gezin is gevestigd.' Het gezin blijft in Gent → Jonas blijft Belgisch rijksinwoner ondanks zijn fysieke verhuis.

3. **Resultaat** — Jonas wordt in 2026 nog steeds in België belast op zijn wereldwijde loon, inclusief zijn Dubai-bezoldiging. Mogelijk verlaging via een dubbelbelastingverdrag België-VAE (indien van toepassing) of vrijstelling onder progressievoorbehoud.

4. **Wat moest er anders** — om effectief niet-inwoner te worden moet Jonas zijn gezin meenemen, of een feitelijke scheiding documenteren. Pure inschrijvingsverandering volstaat niet.

<small>📚 WIB92 — art. 2 — 1° — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### 💡 Cypriotische NV met werkelijke leiding in Brussel 🔗

_TechHolding Ltd is statutair gevestigd in Limassol (Cyprus). Twee bestuurders, beide Belgische rijksinwoners wonend in Brussel. Alle bestuursvergaderingen worden in een Brussels kantoor gehouden. De boekhouding wordt gevoerd in Antwerpen. Cypriotische 'directeur' is enkel een nominee._

Analyse: art. 2 — 5° WIB92 vereist één van drie criteria. Statutair: Cyprus (criterium 1 niet vervuld voor België). Voornaamste inrichting: te onderzoeken, maar boekhouding en kantoor in BE wijzen op BE. Zetel van bestuur of beheer: BE (alle besluiten genomen in Brussel). Conclusie: TechHolding Ltd is fiscaal Belgisch ingezetene → onderworpen aan Belgische VenB op het WERELDWIJDE resultaat, ondanks de Cypriotische rechtsvorm. DBV België-Cyprus past tie-breaker toe (typisch place of effective management → BE) → bevestiging Belgische residentie. Cypriotische winstbelasting eventueel verrekenbaar via DBV.

<small>📚 WIB92 — art. 2 — 5° — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Valkuilen

### ⚠️ Uitschrijving Rijksregister = einde rijksinwonerschap

**Verkeerde assumptie**: Studenten denken dat zich uitschrijven uit het Rijksregister automatisch leidt tot verlies van Belgisch rijksinwonerschap.

**Kernpunt**: Het Rijksregister-vermoeden valt weg, maar de feitelijke test ('beoordeling naar omstandigheden') blijft. Een persoon zonder Rijksregister-inschrijving kan nog steeds rijksinwoner zijn als zijn woonplaats of zetel van fortuin in België ligt. Uitschrijving is een NOODZAKELIJKE maar niet voldoende voorwaarde voor niet-rijksinwoner-status.

<small>📚 WIB92 — art. 2 — 1° — _wettekst_</small>

### ⚠️ 183-dagen-regel als residentie-test toepassen

**Verkeerde assumptie**: Een Belg die minder dan 183 dagen in België is, is geen rijksinwoner.

**Kernpunt**: België kent géén 183-dagen-test in zijn intern fiscaal recht. De residentie-test is volledig feitelijk (woonplaats + zetel van fortuin). De 183-dagen-grens komt enkel terug in DBVs (gewone verblijfplaats — tie-breaker stap 3) en in bron-staat-regels voor expats (art. 15 OESO-MV — bezoldigingen). Een Belgische CEO die het hele jaar zaken doet in het buitenland maar wiens gezin in België blijft, BLIJFT rijksinwoner.

<small>📚 WIB92 — art. 2 — 1° — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### ⚠️ Maatschappelijke zetel = vennootschap-residentie

**Verkeerde assumptie**: De maatschappelijke zetel (statutair) volstaat om de vennootschap-residentie vast te leggen.

**Kernpunt**: Art. 2 — 5° biedt drie ALTERNATIEVE criteria — voldoen aan één volstaat voor Belgische residentie. Een vennootschap met statutaire zetel in Cyprus maar werkelijke leiding in Brussel is Belgisch ingezetene (criterium 3). Statutaire zetel verplaatsen blokkeert het criterium maatschappelijke zetel, maar de feitelijke leiding-test blijft over en kan leiden tot dubbele residentie of Belgische residentie.

<small>📚 WIB92 — art. 2 — 5° — _wettekst_</small>

## Accountant-perspectieven

### Expat-cliënt of emigratie-planning

_De accountant die een natuurlijke persoon adviseert over een internationale carrière- of pensioenverhuizing._

#### 🧭 Adviseur

##### 👣 Checklist effectieve residentie-breuk  
_`stap`_

🔗 Om verlies van Belgisch rijksinwonerschap te bewerkstelligen: (1) gezin meeverhuizen (echtgenoot + minderjarige kinderen); (2) Belgische woning verkopen, schenken of leegtrek-verhuren met objectieve dossier-onderbouwing; (3) Belgische bankrekeningen herleiden tot minimum (eventueel afsluiten); (4) Belgische schoolinschrijvingen, clubs, abonnementen beëindigen; (5) hoofdvermogen verplaatsen naar nieuwe land; (6) uitschrijven Rijksregister; (7) inschrijven bevolkingsregister van het nieuwe land. Dossier opbouwen vóór de verhuizing voor het geval de fiscus de breuk betwist.

<small>📚 WIB92 — art. 2 — 1° — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### Internationale groepsstructuur — vennootschap-residentie-vraag

_De accountant die advies geeft bij een offshore- of internationale groepsstructuur._

#### 💰 Fiscaal adviseur

##### 👣 Bestuurssamenstelling en vergaderingen onderzoeken  
_`stap`_

🔗 Bij elke buitenlandse vennootschap met Belgische bestuurders: onderzoek waar de strategische beslissingen werkelijk genomen worden. Concreet: (1) waar wonen de bestuurders; (2) waar vinden de raden van bestuur plaats (notulen!); (3) wie tekent de contracten en waar; (4) waar wordt de boekhouding gevoerd; (5) waar zit de bank van de vennootschap. Een 'nominee director' in het buitenland zonder reële beslissingsmacht beschermt NIET tegen de Belgische werkelijke-leiding-test.

<small>📚 WIB92 — art. 2 — 5° — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Verder lezen (scope-out)

- → Belasting niet-inwoners (BNI) → [[belasting-niet-inwoners]] _(moet-verwijzen)_
- → Toepassingsgebied vennootschapsbelasting → [[toepassingsgebied-vennootschapsbelasting]] _(moet-verwijzen)_
- → DBV-tie-breaker rules → [[dubbelbelastingverdrag]] _(moet-verwijzen)_

## Relaties

### `valt_onder`
- [[internationaal-fiscaal]]
### `triggert`
- [[personenbelasting]] — Rijksinwonerschap (art. 2 — 1°) triggert onderwerping aan PB op het wereldwijde inkomen (art. 5 WIB92).
- [[toepassingsgebied-vennootschapsbelasting]] — Belgische vennootschap-residentie (art. 2 — 5°) triggert onderwerping aan VenB op het wereldwijde resultaat (art. 179 WIB92).
### `vergelijkbaar_met`
- [[belasting-niet-inwoners]]
    - **Gelijkenissen**:
        - Beide systemen samen vormen het complete toepassingsgebied van de Belgische inkomstenbelastingen
        - Beide bouwen op de residentie-vaststelling als trigger
    - **Verschillen**:
        - Rijksinwoner: onbeperkte belastingplicht (wereldwijd inkomen)
        - Niet-inwoner: beperkte belastingplicht (enkel Belgische bron-inkomsten)
        - Rijksinwoner: PB of VenB (art. 5 / 179 WIB92)
        - Niet-inwoner: BNI/nat of BNI/ven (art. 227-248 WIB92)
    - ⚠️ **Verwarringsrisico**: Studenten kwalificeren expats als 'niet-inwoners' op basis van het feit dat ze in het buitenland werken. De woonplaats- + gezin-criteria primeren: een expat met gezin in BE blijft rijksinwoner.
### `beinvloed_door`
- [[dubbelbelastingverdrag]] — Bij dubbele residentie lossen tie-breaker rules in het DBV (art. 4 OESO-MV) het conflict op — eerst permanente woning, dan centrum vitale belangen, dan gewone verblijfplaats, dan nationaliteit, dan MAP.
### `vereist`
- [[wereldwijd-inkomen-beginsel]] — Het wereldwijd-inkomen-beginsel is de logische gevolgtrekking uit residentie: een staat belast haar inwoners op hun globale inkomen.
