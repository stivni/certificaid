---
title: "Buitenlandse winst en verlies"
concept_type: "procedure"
schema_version: "2.2"
status: "concept"
categorieen:
  - regeling
ankers:
  - 2.8.V
tags:
  - concept
  - schema-2.2
  - type-procedure
  - cat-regeling
  - status-concept
gegenereerd_uit: "data/concepten/records/buitenlandse-winst-en-verlies.json"
---

# Buitenlandse winst en verlies

_Procedure_

📋 Regeling · Anchors: `2.8.V` · Wave: `skeleton-btw-internationaal-2026-05-28`

> [!info] 📝 **Concept** — content gevuld door cluster-extract; niet door mens-verify gegaan.

**Synoniemen**: cross-border winst-en-verlies · verrekening buitenlands resultaat · buitenlandse VI-winst aangifte

## Definitie

📖 Buitenlandse winst en verlies omvat de regels voor de behandeling in de Belgische VenB van het resultaat dat een Belgische binnenlandse vennootschap behaalt via buitenlandse activiteiten (typisch via een vaste inrichting of buitenlands onroerend goed). De kernregel: art. 206/4 WIB92 verdeelt het resterend resultaat in drie kolommen (Belgisch / niet-bij-verdrag-vrijgesteld / bij-verdrag-vrijgesteld). Voor buitenlandse verliezen geleden in een verdragsland gelden bijzondere aanrekenings-volgorde en recapture-regels (art. 185 §3) — verliezen die ooit in BE werden afgetrokken moeten worden 'teruggenomen' wanneer ze later in de buitenstaat aftrekbaar worden.

<small>📚 WIB92 — art. 206/4 — _wettekst_ · WIB92 — art. 185 §3 — _wettekst_</small>

## Substantie

📖 Voor de accountant van een internationaal actieve groep is dit dé jaarlijkse exercise: hoe verwerken we VI-winsten en -verliezen in de Belgische aangifte? Vier scenario's: (1) winst uit verdragsland-VI — vrijgesteld in BE (kolom 'bij verdrag vrijgesteld'); (2) winst uit niet-verdragsland-VI — belast in BE (kolom 'niet bij verdrag vrijgesteld'), eventueel met FBB-verrekening voor bronheffing; (3) verlies uit verdragsland-VI — kan aanrekenen op BE-winst MITS onherroepelijke keuze + recapture-risico; (4) verlies uit niet-verdragsland-VI — vrij aanrekenbaar tegen Belgische winst. De Marks & Spencer-doctrine (HvJ C-446/03, 2005) heeft 'finale verliezen' uit EU-dochters in beperkte mate aftrekbaar gemaakt.

<small>📚 WIB92 — art. 206/4 + 185 §3 — _wettekst_ · HvJ Marks & Spencer C-446/03 — 13 december 2005 — _rechtspraak_</small>

## Rationale

🔗 De ratio achter de complexe regels: (1) DBV's verzaken België vaak aan heffingsrecht op VI-winst (vrijstellingsmethode), maar dat creëert een asymmetrie — kan België ook geen verliezen aftrekken die uit dezelfde activiteit komen? Symmetrie is het doel: vrijgestelde winsten komen NIET in BE-belasting; vrijgestelde verliezen WORDEN NIET aftrekbaar in BE. Maar voor finale verliezen (waar het buitenland definitief geen aftrek meer toelaat — bv. liquidatie van de VI) heeft HvJ Marks & Spencer geoordeeld dat EU-vrijheid van vestiging vereist dat de woonstaat toch aftrek toelaat — symmetrie wijkt voor proportionaliteit. (2) Recapture (art. 185 §3): wanneer België een verlies aftrok en het buitenland later wel aftrek toelaat, moet BE die aftrek 'terugnemen' om dubbele aftrek te vermijden.

<small>📚 HvJ Marks & Spencer C-446/03 — punten 55-59 — _rechtspraak_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Gebruikscontext

**Status**: `in-voege` · basis: WIB92 art. 206/4 + 185 §3; OESO-MV art. 7 + 23A; M&S-doctrine voor EU-finale verliezen

Sinds AJ 2020 verstrengd door beperking van verliesaftrek (art. 207-208 hervormingswet 2017). Marks & Spencer-doctrine blijft beperkt tot 'finale' verliezen — recente HvJ-arresten (Bevola C-650/16, 2018; Memira C-607/17, 2019; A Oy C-123/11) verfijnen de finaal-test.

**✅ Voor**
- 📖 Belgische binnenlandse vennootschap met VI in EU- of niet-EU-land: jaarlijkse verwerking van VI-resultaat in de driedeling van art. 206/4.

## Bouwstenen

### 📜 Drie kolommen in de aangifte VenB  
_`regel`_

📖 Code 1431 PN (aangifte VenB 2025): verdeling van het resterend resultaat in drie categorieën. (1) Belgisch resterend resultaat — in BE behaald; (2) Niet-bij-verdrag-vrijgesteld — in het buitenland behaald, niet vrijgesteld door DBV (typisch: land zonder DBV, of art. 185/2 CFC-doorrekening); (3) Bij-verdrag-vrijgesteld — VI-winst uit verdragsland onder vrijstellingsmethode (art. 23A DBV). Splitsing gebeurt na alle correcties art. 206/1-206/3.

<small>📚 WIB92 — art. 206/4 — _wettekst_ · Aangifte VenB 2025 — code 1431 PN — _aangifte_</small>

### 👣 Verlies-aanrekenings-volgorde (art. 206/4, tweede lid)  
_`stap`_

📖 Vóór de driedeling worden verliezen aangerekend in deze volgorde: (a) verlies uit verdragsland-VI → eerst op bij-verdrag-vrijgestelde winst, dan niet-bij-verdrag-winst, dan BE-winst; (b) verlies uit niet-verdragsland → eerst op niet-bij-verdrag-winst, dan BE-winst; (c) BE-verlies → eerst op BE-winst, dan niet-bij-verdrag-winst. Volgorde a is gunstig wanneer de bij-verdrag-categorie weinig winst heeft (laat verlies door naar belastbare categorieën).

<small>📚 WIB92 — art. 206/4, tweede lid — _wettekst_</small>

### 📜 Onherroepelijke keuze voor verdragsverlies-aanrekening  
_`regel`_

📖 Verdragsverliezen mogen enkel tegen Belgische of niet-bij-verdrag-winst worden aangerekend indien de belastingplichtige op onherroepelijke wijze een bijlage indient bij de aangifte met (a) het land waarin het verlies werd geleden, (b) het bedrag, en (c) het belastbare tijdperk. Deze keuze triggert ook de recapture-verplichting van art. 185 §3.

<small>📚 WIB92 — art. 206/4, laatste lid — _wettekst_</small>

### ⚙️ Recapture-mechanisme (art. 185 §3)  
_`mechanisme`_

📖 Wanneer een Belgische vennootschap een verlies van haar buitenlandse VI heeft afgetrokken op haar Belgische resultaat (art. 206/4-keuze), en latere winst van diezelfde VI in het buitenland aftrekbaar wordt (de buitenlandse staat laat de verliezen-overdracht toe), moet die VI-winst — voor het bedrag van de eerder afgetrokken verliezen — alsnog in de Belgische belastbare grondslag worden opgenomen. Anders dubbele aftrek. De recapture is onbeperkt in de tijd.

<small>📚 WIB92 — art. 185 §3 — _wettekst_</small>

### ✴️ Marks & Spencer finale verliezen (HvJ C-446/03)  
_`principe`_

📖 Het arrest M&S (2005) en latere arresten (Bevola, Memira) erkennen dat de EU-vrijheid van vestiging vereist dat de moedervennootschap onder uitzonderlijke omstandigheden buitenlandse verliezen kan aftrekken — namelijk wanneer die verliezen 'finaal' zijn (geen mogelijkheid meer voor aftrek of overdracht in de buitenstaat — typisch na liquidatie van de buitenlandse vennootschap of VI). De Belgische rechtspraak past dit toe maar restrictief: M&S-aftrek vereist hard bewijs van finaal karakter + uitputting van alle buitenlandse aftrekmogelijkheden.

<small>📚 HvJ Marks & Spencer C-446/03 — 13 december 2005, punten 55-59 — _rechtspraak_ · HvJ Bevola C-650/16 — 12 juni 2018 — _rechtspraak_</small>

### 📜 CFC-winst toegerekend (art. 185/2) = niet-bij-verdrag-vrijgesteld  
_`regel`_

📖 Wanneer een Belgische moeder CFC-winsten van een buitenlandse vennootschap moet opnemen (art. 185/2 anti-CFC-regel), worden deze winsten in de categorie 'niet-bij-verdrag-vrijgesteld' opgenomen — ze zijn dus Belgisch belastbaar (art. 206/4, vierde lid). Logisch: CFC-regel is anti-misbruik en mag niet door DBV-vrijstelling worden uitgehold.

<small>📚 WIB92 — art. 206/4, vierde lid — _wettekst_ · WIB92 — art. 185/2 — _wettekst_</small>

## Valkuilen

### ⚠️ Buitenlands verlies automatisch aanrekenen zonder onherroepelijke keuze

**Verkeerde assumptie**: Verlies van een Franse VI aftrekken van Belgische winst zonder de aanvullende bijlage in de aangifte.

**Kernpunt**: Art. 206/4 vereist onherroepelijke vermelding van land + bedrag + tijdperk in een bijlage. Zonder die formaliteit: aanrekening enkel binnen vrijgestelde-kolom (= verlies wordt feitelijk niet benut). Plus: keuze brengt recapture mee — afweging vooraf.

<small>📚 WIB92 — art. 206/4, laatste lid — _wettekst_</small>

### ⚠️ Recapture vergeten bij latere VI-winst

**Verkeerde assumptie**: Als de VI later weer winstgevend wordt, gewoon onder de bij-verdrag-vrijgesteld-kolom plaatsen.

**Kernpunt**: Art. 185 §3: voor het bedrag van eerder afgetrokken verliezen moet de latere winst aan BE-belasting worden onderworpen. Recapture is onbeperkt in tijd; vereist een chronologische opvolging van de VI-resultaten per land.

<small>📚 WIB92 — art. 185 §3 — _wettekst_</small>

### ⚠️ M&S-aftrek aannemen zonder finaal bewijs

**Verkeerde assumptie**: Bij liquidatie van een EU-dochter de geaccumuleerde verliezen aftrekken van de BE-moeder.

**Kernpunt**: M&S-doctrine vereist hard bewijs van finaal karakter — alle overdrachts- en aftrekmogelijkheden in de buitenstaat moeten zijn uitgeput. Belgische fiscus is restrictief. Documentatie van buitenlandse aangiften + bevestiging van fiscale autoriteiten daar is doorgaans vereist.

<small>📚 HvJ Bevola C-650/16 — 12 juni 2018 — _rechtspraak_</small>

## Verder lezen (scope-out)

- → Vaste inrichting (basis-concept) → [[vaste-inrichting]] _(moet-verwijzen)_
- → Winst-naar-herkomst (toerekenings-procedure) → [[winst-naar-herkomst]] _(moet-verwijzen)_
- ↪ Vrijstelling met progressievoorbehoud (mechaniek vrijstellen) → [[vrijstelling-met-progressievoorbehoud]] _(mag-verwijzen)_

## Relaties

### `valt_onder`
- [[internationaal-fiscaal]]
### `vereist`
- [[vaste-inrichting]] — Toepassing van de driedeling vereist dat de buitenlandse activiteit kwalificeert als VI met daaraan toerekenbare winst.
- [[winst-naar-herkomst]] — Eerst toerekenen volgens art. 7 OESO-MV, dan opnemen in de juiste kolom van art. 206/4.
### `triggert`
- [[vrijstelling-met-progressievoorbehoud]] — Bij-verdrag-vrijgestelde winst valt in de progressievoorbehoud-categorie.
### `beinvloed_door`
- [[atad-richtlijn]] — ATAD CFC-rules zorgen dat sommige buitenlandse winsten alsnog in de niet-bij-verdrag-categorie belanden (art. 206/4 vierde lid).
