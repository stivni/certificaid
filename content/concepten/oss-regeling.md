---
title: "One-Stop-Shop-regeling (OSS)"
concept_type: "regime"
schema_version: "2.2"
status: "concept"
categorieen:
  - regeling
ankers:
  - 2.4.VI
tags:
  - concept
  - schema-2.2
  - type-regime
  - cat-regeling
  - status-concept
gegenereerd_uit: "data/concepten/records/oss-regeling.json"
---

# One-Stop-Shop-regeling (OSS)

_Regime_

📋 Regeling · Anchors: `2.4.VI` · Wave: `skeleton-btw-internationaal-2026-05-28`

> [!info] 📝 **Concept** — content gevuld door cluster-extract; niet door mens-verify gegaan.

**Afk.**: OSS — **Synoniemen**: One-Stop-Shop · IOSS · Import One-Stop-Shop · Mini One Stop Shop · MOSS

## Definitie

📖 De One-Stop-Shop (OSS) is een vereenvoudigde aangifte- en betalingsregeling waarmee een btw-belastingplichtige zijn btw-verplichtingen voor B2C-verkopen aan EU-consumenten in andere lidstaten kan vervullen via één enkele aangifte ingediend in zijn lidstaat van identificatie — in plaats van zich in elke afzetlidstaat afzonderlijk te moeten registreren. De regeling bestaat sinds 1 juli 2021 (e-commerce-pakket EU 2017/2455) in drie varianten: de Union scheme (art. 58ter WBTW) voor binnen-EU-belastingplichtigen, de non-Union scheme (art. 58quater) voor buiten-EU-dienstverrichters die diensten leveren aan EU-consumenten, en de Import scheme (IOSS — art. 58quinquies) voor afstandsverkopen van uit derde landen ingevoerde goederen tot een intrinsieke waarde van 150 EUR.

<small>📚 WBTW — art. 58ter — _wettekst_ · WBTW — art. 58quater — _wettekst_ · WBTW — art. 58quinquies — _wettekst_ · Richtlijn EU 2017/2455 — e-commerce-pakket vanaf 1 juli 2021 — _richtlijn_</small>

## Substantie

🔗 Het probleem dat OSS oplost: zonder OSS moet een Belgische webshop die voor 50.000 EUR verkoopt aan Nederlandse consumenten zich in Nederland btw-registreren, een Nederlandse aangifte indienen en daar Nederlandse btw afdragen — en dat herhaalt zich voor elk van de 27 EU-lidstaten waarheen hij verkoopt. Met OSS doet de Belgische webshop één enkele kwartaalaangifte bij de Belgische administratie, vermeldt daarin per lidstaat van bestemming het verkoopvolume en het toepasselijk lokaal tarief, en betaalt het totaalbedrag op één Belgische rekening. De Belgische administratie verdeelt vervolgens de geïnde btw naar elke betrokken bestemmingslidstaat. Praktisch: één identificatie, één aangifte per kwartaal, één betaling — administratie 27-voudig vereenvoudigd.

<small>📚 WBTW — art. 58ter §5 — _wettekst_ · Richtlijn 2006/112/EG — art. 365 — _richtlijn_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Rationale

🔗 De ratio legis is operationele drempelverlaging voor grensoverschrijdende B2C-handel. Vóór 1 juli 2021 hadden lidstaten elk eigen drempels (35.000 of 100.000 EUR per lidstaat) — wie die per land overschreed, moest zich in elke lidstaat afzonderlijk registreren. Dat duwde webshops naar de keuze tussen ofwel groei beperken om de drempels niet te overschrijden ofwel een onevenredige administratieve last. De e-commerce-hervorming (Richtlijn EU 2017/2455) bracht de drempel terug tot één EU-wijd bedrag van 10.000 EUR én bood OSS aan als single-point-of-contact-aangifte. Doel: het bestemmingsland-principe sluitend maken voor B2C zonder kleine webshops uit de markt te duwen.

<small>📚 Richtlijn EU 2017/2455 — considerans + art. 1 — _richtlijn_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Gebruikscontext

**Status**: `in-voege` · sinds **2021-07-01** · basis: Richtlijn EU 2017/2455 (e-commerce-pakket) → WBTW art. 58ter-quinquies + KB 24

OSS is de uitbreiding van de Mini-One-Stop-Shop (MOSS), die sinds 1 januari 2015 al bestond voor telecommunicatie, omroep en elektronische diensten (TBE-diensten) aan EU-consumenten. Vanaf 1 juli 2021 werd het toepassingsgebied verbreed naar alle B2C-diensten en intra-communautaire afstandsverkopen, en werd IOSS toegevoegd voor invoer ≤ 150 EUR.

**✅ Voor**
- 📖 Belgische webshops en dienstverrichters die voor meer dan 10.000 EUR per kalenderjaar B2C-EU-omzet realiseren (afstandsverkopen + telecommunicatie/omroep/elektronische diensten samen). Buiten-EU-dienstverrichters die B2C-diensten verrichten voor EU-consumenten. E-commerce-platforms en dropshippers met kleine zendingen uit China / VS / VK aan EU-consumenten (IOSS).

**🚫 Niet voor**
- 🔗 B2B-handelingen (= afnemer is btw-belastingplichtige met geldig EU-btw-nummer) — die volgen de standaard verleggingsregels (art. 21 / 25ter WBTW), niet OSS. OSS is uitsluitend voor B2C-stromen.
- 📖 Afstandsverkopen van goederen met intrinsieke waarde > 150 EUR uit derde landen — die vallen niet onder IOSS maar onder de standaard-invoerregels (douaneformaliteit + btw bij invoer).

**📋 Voorwaarden**
- 📖 Voor Union scheme: belastingplichtige is in de EU gevestigd of heeft daar een vaste inrichting, en kiest één lidstaat van identificatie (België indien hier gevestigd). Voor non-Union scheme: belastingplichtige is niet in de EU gevestigd en kiest een EU-lidstaat van identificatie. Voor Import scheme (IOSS): zendingen met intrinsieke waarde ≤ 150 EUR, ingevoerd uit derde landen, naar EU-consumenten — niet-EU-belastingplichtige moet typisch een EU-tussenpersoon aanstellen.

**▶️ Trigger start**
- 📖 B2C-EU-omzet overschrijdt 10.000 EUR per kalenderjaar (Union scheme) — vanaf eerste levering die de drempel overschrijdt is OSS of lokale btw-registratie verplicht voor de verkochte goederen. Onder de drempel: optie mogelijk om vrijwillig OSS te kiezen.

**👍 Voordeel**
- 🔗 Eén btw-registratie en één kwartaalaangifte voor alle EU-lidstaten samen — vermijdt 27 afzonderlijke registraties, 27 lokale btw-aangiftes en 27 betaalstromen. Reductie van administratieve drempels voor KMO-e-commerce; mogelijkheid om snel naar nieuwe lidstaten uit te breiden zonder lokale fiscale-vertegenwoordigingskost.

**⚠️ Risico**
- 📖 OSS-aangifte is een aanvulling op de gewone Belgische btw-aangifte — geen vervanging. Wie OSS gebruikt mag in de OSS-aangifte géén btw aftrekken op de aankoop-kost (art. 58ter §8) — aftrek moet via de gewone Belgische periodieke aangifte of via teruggaafprocedure art. 76 §2. Fout: aftrekken in OSS-aangifte = afwijzing en boete. Bij niet-betaling binnen termijn: identificatielidstaat kan de belastingplichtige uitsluiten uit het OSS-systeem, met verplichte directe registratie in elke lidstaat als gevolg.

## Sub-concepten

### 📦 Union scheme (OSS — binnen-EU)  
_`regime` (subconcept)_

#### Definitie

📖 De Union scheme is de OSS-variant voor in de EU gevestigde belastingplichtigen. Toepassingsgebied: (1) intra-communautaire afstandsverkopen van goederen aan EU-consumenten en (2) alle B2C-diensten aan EU-consumenten waarbij plaats van handeling in een andere lidstaat ligt dan de lidstaat van vestiging. De Belgische webshop kiest België als lidstaat van identificatie, dient kwartaalaangifte in via INTERVAT-OSS, betaalt op één Belgische rekening (postrekening BE78 6792 0036 2186 — 'Mini One Stop Shop - VAT BE').

<small>📚 WBTW — art. 58ter — _wettekst_ · KB nr. 24 — art. 13bis — _kb_</small>

#### 📜 Aangifte- en betalingstermijn Union scheme  
_`regel`_

📖 Kwartaalaangifte: uiterlijk vóór het einde van de maand volgend op het einde van het kwartaal. Voor Q1 (januari-maart): uiterlijk 30 april. Aangifte gebeurt elektronisch via INTERVAT. Betaling in EUR op dezelfde deadline, op de speciale OSS-rekening. Bij niet-tijdige indiening of betaling kunnen herinneringen volgen door de lidstaat van identificatie (3 herinneringen → uitsluiting).

<small>📚 WBTW — art. 58ter §5 — _wettekst_</small>

### 📦 Non-Union scheme (OSS — buiten-EU dienstverrichter)  
_`regime` (subconcept)_

#### Definitie

📖 De non-Union scheme is OSS voor belastingplichtigen die niet in de EU zijn gevestigd en B2C-diensten verrichten voor EU-consumenten (typisch: Amerikaanse SaaS-aanbieder, Britse adviesbureau na Brexit). Niet-EU-belastingplichtige kiest één EU-lidstaat als lidstaat van identificatie (vrije keuze) en doet daar kwartaalaangifte voor zijn diensten naar alle EU-consumenten. Toepassingsgebied beperkt tot diensten (geen goederen).

<small>📚 WBTW — art. 58quater — _wettekst_</small>

### 📦 Import One-Stop-Shop (IOSS — Import scheme)  
_`regime` (subconcept)_

#### Definitie

📖 IOSS is de derde OSS-variant, specifiek voor afstandsverkopen van uit derdelandsgebieden of derde landen ingevoerde goederen met een intrinsieke waarde van ten hoogste 150 EUR per zending. Doelpubliek: dropshippers en e-commerce-platforms die rechtstreeks vanuit China / VK / VS verzenden naar EU-consumenten. Voordeel: de invoer wordt btw-vrijgesteld (art. 143, lid 1 ca) Richtlijn) en de btw wordt verschuldigd op het tijdstip van de verkoop, geheven in de lidstaat van de consument, en aangegeven in de IOSS-maandaangifte. Geen douane-vertraging meer voor de pakket-ontvanger. Niet-EU-belastingplichtige moet typisch een EU-tussenpersoon aanstellen die de IOSS-formaliteiten in zijn naam vervult.

<small>📚 WBTW — art. 58quinquies — _wettekst_ · Richtlijn 2006/112/EG — art. 143 lid 1 ca) — _richtlijn_</small>

#### 📜 IOSS-aangifte is maandelijks (niet per kwartaal)  
_`regel`_

📖 In tegenstelling tot Union/non-Union scheme (kwartaal) is de IOSS-aangifte maandelijks: uiterlijk vóór het einde van de maand volgend op het belastingtijdvak. Reden: invoer-stromen vereisen kortere afdrachttermijn. Aangifte bevat per lidstaat van verbruik het totaalbedrag exclusief btw + tarief + totale verschuldigde belasting. Boekhouding 10 jaar bewaren (art. 58quinquies §7 derde lid).

<small>📚 WBTW — art. 58quinquies §6 — _wettekst_</small>

## Bouwstenen

### 📏 EU-wijde drempel 10.000 EUR voor B2C-EU-handelingen  
_`drempel`_

📖 Sinds 1 juli 2021 geldt één EU-wijde drempel van 10.000 EUR (excl. btw) per kalenderjaar voor alle B2C-EU-afstandsverkopen + telecommunicatie/omroep/elektronische diensten aan EU-consumenten samen. Onder de drempel: btw van België blijft van toepassing, geen OSS nodig. Boven de drempel (of bij vrijwillige optie): btw van bestemmingsland → OSS of lokale registratie. De drempel is totaal (alle bestemmingslidstaten samen), niet per land.

<small>📚 WBTW — art. 15 §1 tweede lid 3° — _wettekst_ · WBTW — art. 21bis §2 9° tweede lid c) — _wettekst_</small>

### 🚧 Geen btw-aftrek in OSS-aangifte  
_`beperking`_

📖 OSS-aangifte is een aangifte van verschuldigde btw — géén netto-aangifte. De belastingplichtige die OSS gebruikt mag de btw geheven op zijn aankopen die met OSS-handelingen verband houden NIET aftrekken in de OSS-aangifte (art. 58ter §8). Hij recupereert ze ofwel via de gewone Belgische periodieke aangifte (als hij daar nog handelingen verricht), ofwel via de teruggaafprocedure art. 76 §2 (8e/13e-richtlijn-procedure voor buitenlandse btw). Dit is een vaak voorkomende stagiair-fout.

<small>📚 WBTW — art. 58ter §8 — _wettekst_ · WBTW — art. 58quinquies §8 — _wettekst_</small>

### 📜 Bewaartermijn OSS-boekhouding: 10 jaar  
_`regel`_

📖 Voor OSS- en IOSS-handelingen geldt een verlengde bewaartermijn van 10 jaar (versus de standaard 7 jaar voor Belgische btw-archief). De gegevens moeten op elk verzoek elektronisch beschikbaar zijn voor de Belgische administratie én voor de bevoegde administratie van elke lidstaat van verbruik.

<small>📚 WBTW — art. 58quinquies §7 — _wettekst_</small>

## Voorbeelden

### 💡 Belgische webshop met B2C-verkopen naar 3 EU-lidstaten 🔗

_Zelena Bio NV (Belgische webshop) verkoopt biologische voedingssupplementen aan EU-consumenten. Jaartotaal 2026: 4.500 EUR aan Nederlandse consumenten, 3.200 EUR aan Duitse consumenten, 2.800 EUR aan Franse consumenten. Drempel-toets: 4.500 + 3.200 + 2.800 = 10.500 EUR — boven 10.000 EUR-drempel._

**Berekening:**
- Stap 1 — drempelberekening: 4.500 + 3.200 + 2.800 = 10.500 EUR > 10.000 EUR. Drempel overschreden bij de levering die de cumulatieve 10.000 EUR overschrijdt.
- Stap 2 — Vanaf overschrijdings-levering: plaats van handeling = bestemmingsland (Nederland 21 %, Duitsland 7 % voor voedingssupplementen of 19 % standaard, Frankrijk 5,5 % voor sommige levensmiddelen of 20 % standaard). Zelena moet voor elke verkoop het juiste lokale btw-tarief aanrekenen volgens bestemmingsland.
- Stap 3 — Zelena registreert zich in INTERVAT-OSS (België = lidstaat van identificatie) en dient kwartaalaangifte in. Tabel-rij per lidstaat van verbruik met totaalbedrag excl. btw + tarief + verschuldigde btw.
- Stap 4 — Betaling: één bedrag op postrekening BE78 6792 0036 2186 'Mini One Stop Shop - VAT BE', uiterlijk einde van de maand volgend op het kwartaal.
- Stap 5 — De Belgische administratie verdeelt het bedrag naar de Nederlandse, Duitse en Franse administraties via het clearing-systeem.

→ **Resultaat**: Vermijdt 3 afzonderlijke btw-registraties in NL/DE/FR. Eén ENKELE aangifte + betaling in EUR via België. Nadeel: Zelena moet wel correcte tarieven per bestemmingsland kunnen toepassen — voor voedingssupplementen verschilt het tarief sterk per lidstaat.

<small>📚 WBTW — art. 15 §1 tweede lid 3° — _wettekst_ · WBTW — art. 58ter — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### 💡 IOSS — Belgische dropshipper met China-naar-EU-zendingen 🔗

_Aurelia Holding NV exploiteert een e-commerce-platform dat fashion-accessoires uit China rechtstreeks naar EU-consumenten verzendt. Gemiddelde zending: 35 EUR intrinsieke waarde. Volume: 800 zendingen/maand, geografisch verspreid over 12 lidstaten._

**Berekening:**
- Stap 1 — intrinsieke waarde per zending = 35 EUR < 150 EUR → IOSS toepasbaar.
- Stap 2 — Aurelia registreert zich voor IOSS in België (lidstaat van identificatie), krijgt IOSS-nummer (IM-xxx).
- Stap 3 — Bij elke verkoop berekent Aurelia het lokale btw-tarief van de eindbestemming (bv. NL 21 % op fashion = 7,35 EUR btw op 35 EUR), rekent dit aan op het ogenblik van de verkoop, en boekt 35 EUR omzet + 7,35 EUR btw.
- Stap 4 — Bij invoer in de EU: douane-aangifte vermeldt IOSS-nummer → vrijstelling van invoer-btw (art. 143 Richtlijn). Pakket gaat direct door zonder btw-betaling aan grens.
- Stap 5 — Maandaangifte via INTERVAT-IOSS: totaalbedrag per lidstaat van verbruik. Betaling op IOSS-rekening uiterlijk einde van de volgende maand.

→ **Resultaat**: Zonder IOSS: elk pakket zou douane-formaliteiten en btw-inning bij ontvangst doorlopen — wat het pakket vertraagt en de consument verrast met extra-betaling. Met IOSS: vlotte levering, btw transparant verwerkt in de verkoopprijs, eenvoudige IOSS-aangifte voor het platform.

<small>📚 WBTW — art. 58quinquies — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Valkuilen

### ⚠️ OSS verwarren met een btw-aftrek-mechanisme

**Verkeerde assumptie**: Studenten denken dat ze in de OSS-aangifte een 'aftrek-rooster' hebben zoals in de gewone aangifte — om bv. de Chinese inkoop-btw of de Belgische marketing-kosten te verrekenen.

**Kernpunt**: OSS-aangifte is uitsluitend verschuldigde-btw-aangifte. Aftrek/recuperatie loopt via de gewone Belgische periodieke aangifte (voor Belgische input-btw) of via de teruggaafprocedure art. 76 §2 (voor buitenlandse input-btw). Aftrek opnemen in OSS = automatische afwijzing.

<small>📚 WBTW — art. 58ter §8 — _wettekst_</small>

### ⚠️ Drempel 10.000 EUR per lidstaat in plaats van EU-totaal

**Verkeerde assumptie**: Studenten leren dat ze 'pas vanaf 10.000 EUR per lidstaat' OSS-plichtig zijn — een doorgetrokken pre-2021-redenering.

**Kernpunt**: De 10.000 EUR-drempel is een totaal voor alle bestemmingslidstaten samen, niet per land. 4.500 NL + 3.200 DE + 2.800 FR = 10.500 EUR cumulatief = drempel overschreden = OSS-plichtig voor elk van die landen vanaf de overschrijdings-levering.

<small>📚 WBTW — art. 15 §1 tweede lid 3° — _wettekst_</small>

### ⚠️ OSS toepassen op B2B-verkopen

**Verkeerde assumptie**: OSS lijkt op een 'one-stop-EU'-systeem en wordt door beginners gebruikt voor alle EU-verkopen, ook B2B.

**Kernpunt**: OSS is uitsluitend voor B2C-stromen — afnemer is consument of niet-belastingplichtige rechtspersoon zonder geldig EU-btw-nummer. B2B (afnemer met geldig EU-btw-nummer in VIES) = vrijgestelde IC-levering + IC-verwerving bij koper, géén OSS.

<small>📚 WBTW — art. 58ter §2 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### ⚠️ IOSS-drempel 150 EUR = factuurbedrag inclusief verzending

**Verkeerde assumptie**: De 150 EUR-grens van IOSS wordt vergeleken met het totaal-factuurbedrag inclusief verzendkosten.

**Kernpunt**: Het is de intrinsieke waarde van de goederen (zonder vervoer- en verzekeringskosten — die zijn pas in de maatstaf van heffing voor de OSS-aangifte zelf). Een zending van 145 EUR goederen + 20 EUR verzendkosten = intrinsieke waarde 145 EUR → IOSS toepasbaar. Een zending van 155 EUR goederen + 5 EUR verzendkosten = boven drempel → standaard-invoer-procedure.

<small>📚 WBTW — art. 58quinquies §1 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Speelruimtes

### 🎚️ OSS gebruiken hoewel onder 10.000 EUR-drempel

## Accountant-perspectieven

### E-commerce-onderneming met B2C-EU-verkopen

_De accountant die het btw-dossier voert voor een webshop of dienstverrichter met grensoverschrijdende B2C-omzet._

#### 📒 Boekhouder

##### 👣 Boeking OSS-omzet per bestemmingsland  
_`stap`_

🔗 Per bestemmingsland-verkoop een aparte sub-rekening van de verkoopomzet bijhouden, plus per bestemmingsland-tarief een aparte verschuldigde-btw-rekening. Op het einde van het kwartaal: somtarief × somomzet per land = OSS-aangifte-rij.

<small>📚 WBTW — art. 58ter §7 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

#### 💰 Fiscaal adviseur

##### 👣 Aansluitcontrole OSS-aangifte met boekhouding  
_`stap`_

🔗 Per kwartaal: voor elke bestemmingsland-rij in OSS-aangifte → omzet uit grootboek-rekening 700-LL = bedrag excl. btw op aangifte; verschuldigde btw uit rekening 451-LL = betaalde btw op aangifte. Tarieven uit Cijferzakboekje of EU-tarievendatabase (TEDB) verifiëren — tariefwijzigingen lidstaten gelden zonder Belgische omzetting.

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

##### 📜 Recuperatie input-btw los van OSS  
_`regel`_

📖 Belgische input-btw (Belgische leveranciers + Belgische marketing-kosten) = aftrek in gewone periodieke Belgische aangifte (rooster 59). Buitenlandse input-btw die verband houdt met OSS-handelingen = teruggaafprocedure art. 76 §2 → 8e/13e-richtlijn-aanvraag bij elke betrokken lidstaat (deadline jaarlijks 30 september). Nooit beide procedures op dezelfde EUR-btw stapelen.

<small>📚 WBTW — art. 58ter §8 — _wettekst_ · WBTW — art. 76 §2 — _wettekst_</small>

#### 🧭 Adviseur

##### 🧭 Advies: welke OSS-variant past?  
_`vuistregel`_

🔗 EU-gevestigde verkoper met goederen-stromen vanuit EU naar EU-consumenten plus diensten → Union scheme (OSS). EU-gevestigde dropshipper met goederen ≤ 150 EUR direct uit derde land naar EU-consument → IOSS bovenop Union scheme. Niet-EU dienstverrichter (US SaaS, UK consulting na Brexit) → non-Union scheme. Wie zowel EU-gevestigde goederen-verkoop als import-stromen heeft = beide schemes nodig (gescheiden registraties).

<small>📚 WBTW — art. 58ter — _wettekst_ · WBTW — art. 58quater — _wettekst_ · WBTW — art. 58quinquies — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Verder lezen (scope-out)

- → Σ-keuzekader grensoverschrijdend → [[btw-grensoverschrijdend]] _(moet-verwijzen)_
- → Plaats-van-handeling B2C → [[plaats-van-handeling-btw]] _(moet-verwijzen)_

## Relaties

### `valt_onder`
- [[btw-grensoverschrijdend]]
### `beinvloed_door`
- [[plaats-van-handeling-btw]] — OSS verschuift de plaats van handeling voor B2C-EU-stromen van vertrekland naar bestemmingsland — vereist correcte plaats-van-handeling-toepassing per transactie.
### `vergelijkbaar_met`
- [[fiscaal-vertegenwoordiger-btw]]
    - **Gelijkenissen**:
        - Beide vermijden dat een buitenlandse / niet-gevestigde belastingplichtige zich in elke lidstaat afzonderlijk moet registreren
    - **Verschillen**:
        - OSS = self-service single-point-of-contact aangifte voor B2C-stromen; werkt voor EU- en niet-EU-belastingplichtigen
        - Fiscaal vertegenwoordiger = professionele vertegenwoordiger die in België aansprakelijk is voor btw-verplichtingen van een niet-EU-belastingplichtige; werkt voor B2B én B2C; verplicht in bepaalde situaties (art. 55 WBTW)
        - OSS: één registratie globaal voor heel EU; fiscaal vertegenwoordiger: één registratie per lidstaat van vestiging-vertegenwoordiger
    - ⚠️ **Verwarringsrisico**: Beide regelingen lossen het 'niet-gevestigd in lidstaat van heffing'-probleem op maar voor verschillende doelgroepen en transactietypes.
### `uitgevoerd_door`
- [[btw-aangifte]] — OSS-aangifte is administratief gekoppeld aan de gewone btw-aangifte (input-btw-aftrek nooit in OSS) maar is een aparte aangifte met eigen periodiciteit en betalingsrekening.
