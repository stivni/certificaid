---
title: "Fiscale bemiddelingsprocedure"
concept_type: "procedure"
schema_version: "2.2"
status: "concept"
categorieen:
  - gebeurtenis
ankers:
  - 2.5.VI
tags:
  - concept
  - schema-2.2
  - type-procedure
  - cat-gebeurtenis
  - status-concept
gegenereerd_uit: "data/concepten/records/fiscale-bemiddelingsprocedure.json"
---

_Procedure_ · afk: **FBD** · ook: fiscale bemiddeling · bemiddeling door FBD

## Definitie

De fiscale bemiddelingsprocedure is een vrijwillige, gratis en vertrouwelijke procedure waarbij de federale Fiscale Bemiddelingsdienst (FBD) — een onafhankelijke dienst opgericht bij wet van 25 april 2007 — probeert een akkoord tot stand te brengen tussen de belastingplichtige en de fiscus tijdens een lopend bezwaar (of geschil over een administratieve handeling). De FBD heeft geen beslissingsbevoegdheid: ze bemiddelt en formuleert een advies of voorstel. De aanvraag schorst de beroepstermijn naar de rechtbank.

<small>📖 WIB92 — art. 376quinquies — _wettekst_ · Wet 25 april 2007 houdende diverse bepalingen (IV) — art. 116 — _wettekst_</small>

## Substantie

Praktisch is de FBD een 'derde stem' tussen belastingplichtige en taxatiedienst, vooral nuttig bij feitelijke geschillen (waardering, kostenaftrek, gemengd privé/professioneel-gebruik) waar de standpunten vastliggen. De bemiddelaar is geen rechter — hij faciliteert. De FBD is ook bevoegd voor BTW, registratie- en successierechten, en sinds 2019 voor federale invorderingsgeschillen. Voor gewest-belastingen bestaan eigen bemiddelingsdiensten (Vlabel, ...).

<small>🔗 WIB92 — art. 376quinquies — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Rationale

De ratio is praktisch en menselijk: door een bemiddeling te organiseren kunnen procedures vermeden worden die voor beide partijen tijdrovend en duur zijn (vooral kosten voor de belastingplichtige). De vrijwilligheid + vertrouwelijkheid + schorsende werking maakt drempel laag. De FBD ontlast tegelijk de rechtbanken en de gewestelijke directies.

<small>🔗 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Gebruikscontext

**Status**: `in-voege` · basis: Wet 25 april 2007 art. 116 + WIB92 art. 376quinquies

FBD operationeel sinds 2010. Bevoegdheid uitgebreid in 2019 tot invorderingsgeschillen.

**✅ Voor**
- 🔗 Lopende bezwaarprocedure waar onderhandeling vastloopt of waar feitelijke discussie domineert (waardering, gemengd gebruik, ramingen).

**🚫 Niet voor**
- 📖 Wanneer de belastingplichtige reeds een vordering bij de rechtbank van eerste aanleg heeft ingesteld of wanneer de directeur al uitspraak heeft gedaan op het bezwaar — dan is de FBD onbevoegd (art. 376quinquies §2).

**👍 Voordeel**
- 📖 Vrijwillig, gratis, vertrouwelijk. Schorst de beroepstermijn naar de rechtbank — geen verlies van rechten. Vaak snellere oplossing dan een lange directeurs-procedure.

## Bouwstenen

### ✴️ Vrijwillig + vertrouwelijk + gratis

Drie kernkenmerken: (1) vrijwillig — beide partijen moeten meewerken, niemand kan gedwongen worden; (2) vertrouwelijk — wat gezegd wordt tijdens bemiddeling kan niet later tegen een partij gebruikt worden voor de rechter; (3) gratis — geen kosten voor de aanvrager.

<small>🔗 Wet 25 april 2007 — art. 116 §3 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### ⚙️ Schorsende werking op beroepstermijn

Indien een aanvraag tot bemiddeling wordt ingediend tijdens de bezwaarbehandeling, wordt de beroepstermijn naar de rechtbank van eerste aanleg geschorst tot de FBD haar bemiddelingsverslag heeft afgeleverd. Dit beschermt de belastingplichtige tegen termijnverlies tijdens de bemiddeling.

<small>📖 WIB92 — art. 376quinquies §2 — _wettekst_</small>

### 👣 Verloop van de bemiddeling

(1) Aanvraag bij de FBD (per brief, e-mail of via fiscaalbemiddelaar.be). (2) Onderzoek ontvankelijkheid. (3) Bemiddeling: gesprek of schriftelijke uitwisseling tussen FBD, belastingplichtige (of accountant) en taxatiedienst/directeur. (4) Bemiddelingsverslag met advies of voorstel. (5) Directeur beslist over het bezwaar — de FBD-bemiddeling bindt hem niet, maar zijn advies weegt meestal zwaar door.

<small>🔗 WIB92 — art. 376quinquies — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Valkuilen

> [!warning]- Bemiddeling vervangt geen bezwaar
> **Verkeerde assumptie**: Door de FBD in te schakelen, hoef ik geen bezwaar in te dienen.
>
> **Kernpunt**: De FBD-bemiddeling werkt enkel naast een lopend bezwaar (of administratieve geschil). Je moet dus eerst bezwaar indienen binnen de termijn van 6 maanden, en pas dan kun je bemiddeling vragen.
>
> <small>📖 WIB92 — art. 376quinquies §1 — _wettekst_</small>

> [!warning]- FBD = federaal, niet voor gewestbelastingen
> **Verkeerde assumptie**: De FBD bemiddelt voor élk fiscaal geschil, ook over erfbelasting of verkeersbelasting.
>
> **Kernpunt**: De FBD is federaal (PB, VenB, BTW, registratie- en successierechten federaal, douane, accijnzen). Voor Vlaamse heffingen (erfbelasting, registratie-Vlaams, onroerende voorheffing) is Vlabel-bemiddeling bevoegd. Brussel en Wallonië hebben eigen procedures.
>
> <small>🔗 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Verder lezen (scope-out)

- → Bezwaar als parallel pad → [[bezwaarprocedure]] _(moet-verwijzen)_
- → Gerechtelijke fase indien geen oplossing → [[gerechtelijke-fase-belasting]] _(moet-verwijzen)_

## Relaties

### `valt_onder`
- [[fiscale-procedure]]
### `vergelijkbaar_met`
- [[bezwaarprocedure]]
