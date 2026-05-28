---
title: "Fiscaal vertegenwoordiger (BTW)"
concept_type: "actor"
schema_version: "2.2"
status: "concept"
categorieen:
  - entiteit
  - regeling
ankers:
  - 2.4.VI
tags:
  - concept
  - schema-2.2
  - type-actor
  - cat-entiteit
  - cat-regeling
  - status-concept
gegenereerd_uit: "data/concepten/records/fiscaal-vertegenwoordiger-btw.json"
---

# Fiscaal vertegenwoordiger (BTW)

_Actor_

🏢 Entiteit · 📋 Regeling · Anchors: `2.4.VI` · Wave: `skeleton-btw-internationaal-2026-05-28`

> [!info] 📝 **Concept** — content gevuld door cluster-extract; niet door mens-verify gegaan.

**Synoniemen**: aansprakelijk vertegenwoordiger · BTW-vertegenwoordiger — **Vertalingen**: fr: représentant responsable TVA

## Definitie

📖 De fiscaal vertegenwoordiger (in de wet 'aansprakelijk vertegenwoordiger') is een in België gevestigde persoon die door of vanwege de Minister van Financiën wordt erkend om een niet in de Gemeenschap gevestigde belastingplichtige te vertegenwoordigen voor zijn Belgische BTW-verplichtingen. Hij wordt in de plaats gesteld van zijn lastgever voor alle BTW-rechten en -verplichtingen en is met de lastgever hoofdelijk aansprakelijk voor de betaling van de BTW, nalatigheidsinteresten en geldboeten.

<small>📚 WBTW — art. 55 §1 — _wettekst_ · WBTW — art. 55 §4 — _wettekst_ · KB nr. 31 (2 april 2002) — art. 1 — _kb_</small>

## Substantie

🔗 Voor de Belgische fiscus is een belastingplichtige uit een derde land (buiten de EU) moeilijk te controleren en moeilijk in te vorderen. De aansprakelijk vertegenwoordiger lost dat op: een in België gevestigde 'voorpost' die fysiek aanspreekbaar is, de aangiftes indient, de BTW betaalt aan de Schatkist en — als de niet-EU-belastingplichtige in gebreke blijft — met zijn eigen vermogen mee aansprakelijk is. Voor de praktijk: gespecialiseerde fiscale kantoren, douane-expediteurs en logistieke dienstverleners treden vaak op als vertegenwoordiger. Bestaat in twee vormen: individueel (één vertegenwoordiger per niet-EU-cliënt, art. 55 §1) en globaal (één vooraf erkende persoon kan onder twee globale BTW-nummers meerdere niet-EU-belastingplichtigen vertegenwoordigen voor specifieke handelingen, KB nr. 31 art. 2).

<small>📚 WBTW — art. 55 §1 — _wettekst_ · KB nr. 31 (2 april 2002) — art. 2 — _kb_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Rationale

🔗 De ratio legis is invorderingszekerheid voor de Schatkist. Een belastingplichtige uit een derde land kan niet onder de EU-instrumenten voor wederzijdse bijstand (Richtlijn 2010/24/EU, Verordening 904/2010) worden ingevorderd. Door een Belgische vertegenwoordiger te eisen die hoofdelijk aansprakelijk is, beschikt de fiscus over een binnenlandse debiteur tegen wie ze rechtstreeks kan ageren. EU-belastingplichtigen vallen wél onder die wederzijdse bijstand — voor hen is een vertegenwoordiger niet verplicht, alleen mogelijk (art. 55 §2).

<small>📚 WBTW — art. 55 §1 — _wettekst_ · WBTW — art. 55 §2 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Gebruikscontext

**Status**: `in-voege` · basis: WBTW art. 55 + KB nr. 31 van 2 april 2002

Stabiel regime sinds invoering WBTW; KB nr. 31 van 2002 vervangt vroegere KB-versies. Wijzigingen sindsdien blijven op uitvoeringsmodaliteiten.

**✅ Voor**
- 📖 Een niet in de Gemeenschap gevestigde belastingplichtige die in België belastbare handelingen verricht die niet onder de verleggingsregeling vallen (art. 51 §2 1°, 2°, 5° en 6°) en geen gebruik maakt van de bijzondere regelingen van art. 58ter of 58quinquies (OSS/IOSS). Voorbeelden: invoer met opvolgende lokale levering · plaatsing onder entrepot ≠ douane-entrepot · intracommunautaire verwerving met opvolgende levering.

**🚫 Niet voor**
- 📖 Niet vereist wanneer de niet-EU-belastingplichtige in België uitsluitend handelingen verricht waarvoor de BTW via de verleggingsregeling door de medecontractant wordt voldaan (art. 51 §2 1°, 2°, 5° en 6° WBTW). In dat geval ontstaat er geen BTW-schuld in hoofde van de niet-residente belastingplichtige in België.
- 📖 Niet vereist voor belastingplichtigen gevestigd in een ander EU-land of in een derde land waarmee een rechtsinstrument inzake wederzijdse bijstand bestaat dat vergelijkbaar is met Richtlijn 2010/24/EU en Verordening 904/2010 (bv. Noorwegen). Erkenning is dan optioneel (art. 55 §2).

**📋 Voorwaarden**
- 📖 Verzoek tot erkenning aan het Centraal BTW-kantoor voor buitenlandse belastingplichtigen, ingediend door de niet-EU-belastingplichtige (individueel regime) of door de aspirant-vertegenwoordiger zelf (globaal regime). Aanvraag-formulier vooraf indienen, identiteit vertegenwoordiger volledig opgeven; bij globaal regime krijgt de erkende persoon twee globale BTW-identificatienummers (één voor invoer-handelingen, één voor andere handelingen van KB nr. 31 art. 2 §1).

**👍 Voordeel**
- 🔗 Voor de niet-EU-belastingplichtige: praktische toegang tot de Belgische BTW-markt zonder eigen vaste inrichting. Voor de vertegenwoordiger zelf: het is een betaalde dienstverlening (honoraria) — vooral interessant voor douane-expediteurs en logistieke spelers die het volume kunnen bundelen via het globale regime.

**⚠️ Risico**
- 🔗 Hoofdelijke aansprakelijkheid is onbeperkt en strekt zich uit tot belasting + nalatigheidsinteresten + geldboeten van de lastgever. Voor de vertegenwoordiger praktisch significant: als de niet-EU-cliënt verdwijnt of failliet gaat, kan de fiscus zich op het eigen vermogen van de vertegenwoordiger verhalen. Daarom: waarborg verplicht (KB nr. 31 voorziet zekerheidstelling) + voorzichtige cliëntacceptatie + boekhoudkundige scheiding van eigen middelen en middelen-voor-rekening-van-derden (rek. 489 vs. eigen-vermogen).

## Bouwstenen

### 📜 Individuele erkenning (art. 55 §1)  
_`regel`_

📖 Eén-op-één regime: per niet-EU-belastingplichtige wordt één Belgische vertegenwoordiger erkend en krijgt de lastgever zijn eigen Belgisch BTW-identificatienummer (BE-nummer). Die vertegenwoordiger doet de BTW-aangifte voor deze ene cliënt en is hoofdelijk aansprakelijk voor diens BTW-schulden. Vervanging of schrapping van de vertegenwoordiger vergt aangifte bij het Centraal BTW-kantoor; de oude vertegenwoordiger blijft aansprakelijk voor de handelingen tot de datum van aanvaarding van de vervanging.

<small>📚 WBTW — art. 55 §1 — _wettekst_ · KB nr. 31 — art. 1 §2 — _kb_ · KB nr. 31 — art. 1 §3 — _kb_</small>

### 📜 Globale erkenning (KB nr. 31 art. 2)  
_`regel`_

📖 Vooraf erkende persoon (typisch een gespecialiseerd kantoor of douane-expediteur) krijgt twee globale BTW-identificatienummers en mag onder die nummers meerdere niet-EU-belastingplichtigen vertegenwoordigen, voor zover die uitsluitend specifieke handelingen verrichten: invoer met opvolgende levering, intracommunautaire verwerving met opvolgende vrijgestelde levering, plaatsing onder/onttrekking aan entrepot ≠ douane-entrepot. De globale erkende persoon wordt in de plaats van zijn lastgever gesteld voor alle BTW-rechten en -verplichtingen onder het globale nummer.

<small>📚 KB nr. 31 — art. 2 §1 — _kb_ · KB nr. 31 — art. 2 §2 — _kb_ · KB nr. 31 — art. 2 §3 — _kb_</small>

### ⚙️ Hoofdelijke aansprakelijkheid vertegenwoordiger ↔ lastgever  
_`mechanisme`_

📖 De vertegenwoordiger is samen met zijn lastgever 'hoofdelijk gehouden tot voldoening van de belasting, nalatigheidsinteresten en geldboeten'. Dat betekent: de fiscus kan voor het volledige bedrag óf bij de niet-EU-belastingplichtige óf bij de Belgische vertegenwoordiger aankloppen, naar keuze. De vertegenwoordiger die betaalt, heeft een interne verhaal-vordering op zijn lastgever (rek. 416 'rekening-courant lastgever' volgens CBN 161/1) — maar het invorderingsrisico is volledig op hem afgewenteld als de lastgever onvermogend is.

<small>📚 WBTW — art. 55 §4, tweede lid — _wettekst_ · CBN-advies 161/1 — CBN-advies 161/1 — _cbn_</small>

### ⚙️ Boekhoudkundige verwerking (CBN 161/1)  
_`mechanisme`_

📖 De vertegenwoordiger wordt beschouwd als lasthebber van de buitenlandse BTW-plichtige. De BTW-bewegingen worden gevoerd via tussenrekeningen die duidelijk maken dat de BTW niet door de vertegenwoordiger zelf is verschuldigd: rek. 416 'Diverse vorderingen — rekening-courant lastgever X' tegenover rek. 489 'Andere diverse schulden: voor rekening van derden te betalen BTW'. Geen weerslag op de resultatenrekening van de vertegenwoordiger, behalve voor eigen honoraria, salarissen, kantoorkosten en eventuele boetes die hij zelf zou dragen. Hoofdelijke aansprakelijkheid wordt vermeld in de toelichting; bij reëel risico op aanspraak in klasse 0 'Niet in de balans opgenomen rechten en verplichtingen' boeken.

<small>📚 CBN-advies 161/1 — CBN-advies 161/1 — _cbn_</small>

### 📜 Vermeldings-plicht aan klanten en leveranciers  
_`regel`_

📖 De niet in België gevestigde belastingplichtige die hier een aansprakelijk vertegenwoordiger heeft laten erkennen, moet voor elke Belgische handeling de naam of benaming en het adres van die vertegenwoordiger meedelen aan zijn klanten en leveranciers. Praktisch komt dat op de factuur (vermelding 'BTW-vertegenwoordiger in België: X NV — BTW-nr. BEy').

<small>📚 WBTW — art. 53quater §5 — _wettekst_</small>

## Valkuilen

### ⚠️ Vertegenwoordiger verplicht voor élke buitenlandse belastingplichtige

**Verkeerde assumptie**: Stagiairs denken dat een buitenlandse belastingplichtige altijd een fiscaal vertegenwoordiger in België moet aanstellen.

**Kernpunt**: Alleen niet-EU-belastingplichtigen zijn verplicht, en zelfs zij niet wanneer al hun Belgische handelingen onder de verleggingsregeling vallen. EU-belastingplichtigen mogen kiezen — voor hen is een vertegenwoordiger optioneel (art. 55 §2). En sinds de OSS/IOSS-regelingen (art. 58ter/58quater/58quinquies) hoeft een belastingplichtige die alleen daarvoor handelingen verricht, evenmin een vertegenwoordiger te erkennen.

<small>📚 WBTW — art. 55 §1 — _wettekst_ · WBTW — art. 55 §2 — _wettekst_</small>

### ⚠️ Aansprakelijkheid beperkt tot eigen vergoeding

**Verkeerde assumptie**: De vertegenwoordiger denkt dat zijn aansprakelijkheid beperkt is tot de honoraria die hij voor zijn diensten ontvangt.

**Kernpunt**: De hoofdelijke aansprakelijkheid is onbeperkt en omvat belasting + interesten + boetes van de lastgever — geen plafond. Daarom: schermen via waarborg (KB nr. 31), zorgvuldige cliëntacceptatie, en — bij reëel risico — vermelding in klasse 0 + toelichting bij de jaarrekening.

<small>📚 WBTW — art. 55 §4 — _wettekst_ · CBN-advies 161/1 — CBN-advies 161/1 — _cbn_</small>

### ⚠️ BTW-bewegingen mengen met eigen resultatenrekening

**Verkeerde assumptie**: De BTW-stromen van de lastgever opnemen in de gewone omzet/aankoop-rekeningen van de vertegenwoordiger.

**Kernpunt**: De vertegenwoordiger handelt als lasthebber. BTW-bewegingen lopen via rek. 416 (vordering op lastgever) en rek. 489 (schuld aan Staat voor rekening van derden) — buiten de resultatenrekening van de vertegenwoordiger. Alleen eigen honoraria, kantoorkosten en eventuele zelf gedragen boetes raken het resultaat.

<small>📚 CBN-advies 161/1 — CBN-advies 161/1 — _cbn_</small>

## Accountant-perspectieven

### Accountantskantoor als fiscaal vertegenwoordiger

_Wanneer het kantoor zelf optreedt als aansprakelijk vertegenwoordiger voor een niet-EU-cliënt._

#### 💰 Fiscaal adviseur

##### 👣 BTW-aangifte indienen namens de lastgever  
_`stap`_

📖 Maandelijkse of kwartaalaangifte (art. 53 §1 1° 2° WBTW) indienen onder het toegekende BE-nummer van de lastgever (individueel regime) of onder het globale BE-nummer (globaal regime). Bewaar de onderliggende facturen + opgemaakte stukken (KB nr. 31 voorziet documentenbewaring). Betaling van de BTW gebeurt via rek. 489.

<small>📚 WBTW — art. 53 §1 — _wettekst_ · WBTW — art. 55 §4 eerste lid — _wettekst_ · CBN-advies 161/1 — CBN-advies 161/1 — _cbn_</small>

#### 📒 Boekhouder

##### 🧭 BTW voor rekening van derden (489) onderscheiden van eigen BTW (451)  
_`vuistregel`_

🔗 Elke euro BTW die het kantoor namens een lastgever int of betaalt, gaat via rek. 489 — nooit via rek. 451 'BTW-rekening-courant' van het kantoor zelf. Anders ontstaat boekhoudkundige verwarring tussen eigen BTW-positie en die van de vertegenwoordigde. Bij meerdere lastgevers: sub-rekeningen 489.X per lastgever om de mutaties traceerbaar te houden.

<small>📚 CBN-advies 161/1 — CBN-advies 161/1 — _cbn_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

#### 🧭 Adviseur

##### 🧭 Cliëntacceptatie: risico-analyse niet-EU-lastgever  
_`vuistregel`_

🔗 Vooraleer een opdracht als fiscaal vertegenwoordiger aan te nemen: due-diligence op de niet-EU-cliënt (KYC + sector + verwacht volume), waarborg eisen die de potentiële BTW-blootstelling dekt, contractuele recht-van-verhaal en opzeg-clausules opnemen, en bij verhoogd risico vermelding in de toelichting van de jaarrekening (rechten en verplichtingen niet in balans, klasse 0).

<small>📚 WBTW — art. 55 §4 — _wettekst_ · CBN-advies 161/1 — CBN-advies 161/1 — _cbn_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Verder lezen (scope-out)

- → Σ-keuzekader grensoverschrijdend (welk regime kiezen — eigen identificatie, vertegenwoordiger, OSS-systeem) → [[btw-grensoverschrijdend]] _(moet-verwijzen)_
- → BTW-belastingplichtige niet-resident (algemene status van niet-Belgische belastingplichtige) → [[btw-belastingplichtige]] _(moet-verwijzen)_

## Relaties

### `valt_onder`
- [[btw-grensoverschrijdend]]
### `vereist`
- [[btw-belastingplichtige]] — Veronderstelt het bestaan van een niet-EU-belastingplichtige die in België belastbare handelingen verricht.
### `is_uitzondering_op`
- [[verleggingsregeling]] — Wanneer de verleggingsregeling toepasselijk is (art. 51 §2 1°/2°/5°/6° WBTW), is geen fiscaal vertegenwoordiger vereist. De vertegenwoordiger is dus het 'andere pad' voor handelingen waar verlegging niet werkt.
