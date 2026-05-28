---
title: "Voorafgaande beslissing (DVB)"
concept_type: "procedure"
schema_version: "2.2"
status: "concept"
categorieen:
  - regeling
  - gebeurtenis
ankers:
  - 2.5.VIII
  - 2.1.IX
tags:
  - concept
  - schema-2.2
  - type-procedure
  - cat-regeling
  - cat-gebeurtenis
  - status-concept
gegenereerd_uit: "data/concepten/records/voorafgaande-beslissing-dvb.json"
---

# Voorafgaande beslissing (DVB)

_Procedure_

📋 Regeling · 📅 Gebeurtenis · Anchors: `2.5.VIII` · `2.1.IX` · Wave: `skeleton-fiscaliteit-klein-2026-05-28`

> [!info] 📝 **Concept** — content gevuld door cluster-extract; niet door mens-verify gegaan.

**Afk.**: DVB — **Synoniemen**: ruling · fiscale ruling · rulingcommissie — **Vertalingen**: fr: décision anticipée (SDA)

## Definitie

📖 Een voorafgaande beslissing (in de praktijk 'ruling' genoemd) is een schriftelijke beslissing van de federale Dienst Voorafgaande Beslissingen (DVB) waarin de fiscus zich bindt over de fiscale gevolgen van een door de belastingplichtige voorgenomen verrichting. Het systeem is geregeld in art. 20-28 van de Wet van 24 december 2002 (programmawet) en het KB van 17 januari 2003. De beslissing geldt typisch 5 jaar (verlengbaar) zolang de feitelijke en juridische context onveranderd blijft.

<small>📚 Wet 24 december 2002 — art. 20-28 — _wettekst_ · KB 17 januari 2003 — uitvoering rulingprocedure — _kb_</small>

## Substantie

🔗 Praktisch wordt een ruling aangevraagd vóór een transactie van enige omvang of complexiteit: herstructurering (fusie, splitsing, partiële inbreng), grensoverschrijdende holding, octrooi-inkomsten, tax shelter, beroepsmatige terbeschikkingstelling van vastgoed. De aanvraag start met een pre-filing (vrijblijvende verkenning, anoniem mogelijk) en mondt na onderhandeling uit in een gemotiveerde beslissing. Eens uitgereikt bindt de ruling de fiscus, op voorwaarde dat de verrichting reëel uitgevoerd wordt zoals beschreven.

<small>📚 Wet 24 december 2002 — art. 23 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Rationale

🔗 De DVB werd opgericht om rechtszekerheid te bieden in een steeds complexere fiscale wetgeving. Belastingplichtigen (en buitenlandse investeerders) willen vooraf weten welke fiscale gevolgen een transactie heeft. Voor de overheid is het ruling-systeem een instrument om grote investeringen aan te trekken (tax shelter, holding-regimes, ...) en om aggressieve fiscale planning vroeg te detecteren. Het verbod om over zuiver hypothetische gevallen te beslissen of voor reeds uitgevoerde verrichtingen voorkomt misbruik.

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Gebruikscontext

**Status**: `in-voege` · basis: Wet 24 december 2002 art. 20-28 + KB 17 januari 2003

Stabiel sinds 2003. Sinds 2017 strengere transparantie (publicatie geanonimiseerde rulings) onder druk van Europa (BEPS-context).

**✅ Voor**
- 🔗 Voorgenomen verrichting (vóór uitvoering) waarover er fiscale onzekerheid bestaat. Klassieke onderwerpen: fusie/splitsing (belastingneutraliteit), inbreng in natura, holding-structuren, vastgoed-belegging via vennootschap, tax shelter, octrooi-inkomsten, transfer pricing.

**🚫 Niet voor**
- 📖 Reeds uitgevoerde verrichtingen (de DVB beslist NIET retroactief); zaken die in een lopend bezwaar of geschil zitten; zuiver hypothetische vragen zonder concrete plannen; vragen die enkel een nationale wet interpreteren zonder feitelijke context (art. 22 Wet 24-12-2002).

**👍 Voordeel**
- 🔗 Rechtszekerheid vooraf — de fiscus kan later niet meer terugkomen op de beslissing zolang de feitelijke context klopt. Vermijden van langdurige procedures achteraf. Voor grensoverschrijdende structuren: een geldige Belgische ruling vergroot het comfort van buitenlandse partners.

## Bouwstenen

### 👣 Verloop van de procedure  
_`stap`_

📖 (1) Pre-filing — vrijblijvend (eventueel anoniem) verkennend gesprek met DVB-team. (2) Schriftelijke aanvraag met feiten + voorgenomen verrichting + fiscale vragen. (3) Behandeling door DVB-team van 3 leden (gespecialiseerd per materie). (4) Onderhandeling — bijsturing van de verrichting kan voorgesteld worden om binnen de wet te blijven. (5) Schriftelijke gemotiveerde beslissing binnen 3 maanden (verlengbaar). (6) Geanonimiseerde publicatie op fisconetplus.

<small>📚 Wet 24 december 2002 — art. 21-23 — _wettekst_</small>

### 📏 Geldigheidsduur (5 jaar)  
_`drempel`_

📖 Een voorafgaande beslissing geldt typisch 5 jaar (art. 23 Wet 24-12-2002), tenzij anders bepaald — verlengbaar op gemotiveerde aanvraag. De geldigheid eindigt vroeger indien (a) de feitelijke context wijzigt, (b) de wetgeving wijzigt, of (c) blijkt dat de beslissing op onvolledige/onjuiste informatie steunde.

<small>📚 Wet 24 december 2002 — art. 23 — _wettekst_</small>

### ✴️ Bindende werking  
_`principe`_

📖 Eens uitgereikt bindt de beslissing de fiscale administratie (art. 23 §1 Wet 24-12-2002): de aanslagdienst mag niet afwijken van de ruling-uitspraak. Voorwaarde: de feitelijke uitvoering komt overeen met wat in de aanvraag werd beschreven. De belastingplichtige is NIET gebonden: hij kan afzien van de verrichting of er anders mee omgaan.

<small>📚 Wet 24 december 2002 — art. 23 — _wettekst_</small>

### 🚧 Grenzen aan rulings  
_`beperking`_

🔗 DVB mag GEEN beslissing geven die strijdig is met de wet of die de strekking ervan ondermijnt. Sinds 2012-2017 is de DVB veel strenger geworden tegenover constructies die enkel een fiscaal voordeel beogen (anti-misbruik-bepaling art. 344 §1). Ruling-beslissingen die de wetgeving omzeilen kunnen later door de rechter naast zich neergelegd worden (cf. Cassatie-arresten 2015-2018).

<small>📚 WIB92 — art. 344 §1 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Valkuilen

### ⚠️ Geen ruling voor reeds uitgevoerde verrichtingen

**Verkeerde assumptie**: We kunnen achteraf nog een ruling vragen om de fiscale gevolgen vast te leggen.

**Kernpunt**: Art. 22 sluit dit expliciet uit. Ruling = vooraf. Voor reeds uitgevoerde verrichtingen ben je aangewezen op gewone aangifte + eventueel bezwaar.

<small>📚 Wet 24 december 2002 — art. 22 — _wettekst_</small>

### ⚠️ Ruling-bescherming valt weg bij feitelijke afwijking

**Verkeerde assumptie**: Met onze ruling in de hand mogen we de structuur licht aanpassen — de bescherming blijft.

**Kernpunt**: Zodra de werkelijke uitvoering wezenlijk afwijkt van wat in de aanvraag staat (andere bedragen, andere partijen, andere timing), valt de bindende werking weg. De aanslagdienst kan dan gewoon belasten zoals de wet voorschrijft. Bij twijfel: nieuwe ruling aanvragen.

<small>📚 Wet 24 december 2002 — art. 23 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Verder lezen (scope-out)

- ↪ AAMB als beperking van rulings → [[algemene-anti-misbruik-bepaling]] _(mag-verwijzen)_
- ↪ Fiscale beginselen (legaliteit · gelijkheid) → [[fiscale-beginselen]] _(mag-verwijzen)_

## Relaties

### `valt_onder`
- [[fiscale-procedure]]
