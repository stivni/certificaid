---
title: "Integrale consolidatie"
concept_type: "verrichting"
schema_version: "2.2"
status: "concept"
categorieen:
  - regeling
  - gebeurtenis
ankers:
  - 1.4.I.D
  - 1.4.I.E
  - 1.4.II.C
tags:
  - concept
  - schema-2.2
  - type-verrichting
  - cat-regeling
  - cat-gebeurtenis
  - status-concept
gegenereerd_uit: "data/concepten/records/integrale-consolidatie.json"
---

# Integrale consolidatie

_Verrichting_

📋 Regeling · 📅 Gebeurtenis · Anchors: `1.4.I.D` · `1.4.I.E` · `1.4.II.C` · Wave: `skeleton-consolidatie-2026-05-28`

> [!info] 📝 **Concept** — content gevuld door cluster-extract; niet door mens-verify gegaan.

**Synoniemen**: volledige consolidatie · full consolidation

## Definitie

📖 Integrale consolidatie (volledige consolidatie, art. 3:131 KB WVV) is de consolidatiemethode waarbij de moedervennootschap 100 % van de activa, passiva, kosten en opbrengsten van de dochtervennootschap regel-per-regel opneemt in de geconsolideerde jaarrekening — onafhankelijk van haar effectieve deelnemingspercentage. Het aandeel dat niet aan de moeder toebehoort (minderheidsbelang of belang van derden) wordt afzonderlijk gepresenteerd binnen het eigen vermogen én binnen het resultaat. De methode wordt toegepast wanneer de moeder de exclusieve controle (art. 1:14 §1 WVV) over de dochter uitoefent.

<small>📚 KB WVV — art. 3:131 — _kb_ · KB WVV — art. 1:14 — _kb_ · CBN-advies — 2022/09 — _cbn_</small>

## Substantie

🔗 Het economisch idee: de geconsolideerde jaarrekening behandelt de groep als één economische eenheid. Omdat de moeder de dochter volledig controleert, neemt zij alle activa en passiva van de dochter op alsof het haar eigen activa en passiva waren — niet pro rata, maar volledig (100 %). De minderheidsaandeelhouders krijgen wel een afzonderlijke vermelding (rubriek IX 'Belangen van derden' in het geconsolideerde EV) zodat de lezer ziet welk deel van de groepsvermogensgroei en groepswinst toekomt aan partijen buiten de moeder. Intercompany-transacties (verkopen tussen groepsentiteiten, intercompany-vorderingen en -schulden, intercompany-winsten in voorraden of vaste activa) worden geëlimineerd — anders zou de groepsbalans transacties met zichzelf toonen.

<small>📚 KB WVV — art. 3:131 — _kb_ · CBN-advies — 2022/09 — _cbn_ · ISA 600 — Bijlage 2 — _norm_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Rationale

🔗 Ratio legis: bij exclusieve controle beschikt de moeder feitelijk over alle middelen van de dochter — voor de gebruikers van de jaarrekening (schuldeisers, investeerders) is het relevant om dat volledig zicht te krijgen, niet alleen het aandeel dat de moeder bezit. Het 'getrouw beeld' van de groep vereist dan ook integrale opname. De afzonderlijke aanduiding van minderheidsbelangen verzoent dit met de realiteit dat een deel van het vermogen niet aan de moeder-aandeelhouders toekomt.

<small>📚 KB WVV — art. 3:131 — _kb_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Gebruikscontext

**Status**: `in-voege` · basis: KB 29-04-2019 ter uitvoering WVV, Boek 3, Titel 2, Hoofdstuk II (art. 3:117 e.v.)

Belgische consolidatie-regeling sinds het KB van 30 januari 2001, hercodificeerd in het KB WVV 29-04-2019. Voor beursgenoteerde groepen: IFRS 10 (verplicht volgens Verordening 1606/2002).

**✅ Voor**
- 📖 Toepasselijk wanneer de moedervennootschap een exclusieve controle (art. 1:14 §1 WVV) uitoefent op de dochter. Dat is onweerlegbaar vermoed bij meerderheid van stemrechten, statutair benoemingsrecht, of stemmenmeerderheid op de laatste twee algemene vergaderingen (de-facto-controle, art. 1:14 §3 WVV).

**🚫 Niet voor**
- 📖 Niet toepasselijk bij gezamenlijke controle (twee partners delen controle) — dan evenredige consolidatie of vermogensmutatiemethode. Niet toepasselijk bij notabele invloed zonder controle (associates, typisch 20-50 % stemrechten) — dan vermogensmutatiemethode (art. 3:139 KB WVV).

## Bouwstenen

### 📜 100 %-opname regel-per-regel  
_`regel`_

📖 De activa, passiva, kosten en opbrengsten van de dochter worden volledig (100 %) opgenomen — ongeacht of de moeder 51 %, 80 % of 100 % bezit. De deelneming in de moederbalans (rubriek 28) wordt geëlimineerd tegen het aandeel van de moeder in het eigen vermogen van de dochter op de verkrijgingsdatum; het verschil wordt geboekt als consolidatieverschil (rubriek 9920 actief of 9910 passief).

<small>📚 KB WVV — art. 3:131 — _kb_ · KB WVV — art. 3:138 — _kb_</small>

### 📜 Eliminatie intercompany-transacties  
_`regel`_

📖 Vorderingen en schulden tussen groepsentiteiten worden volledig geëlimineerd (kruislings wegstrepen): een vordering van M op D wordt weggestreept tegen de schuld van D aan M. Intercompany-omzet (verkopen tussen groepsentiteiten) wordt eveneens volledig geëlimineerd. Niet-gerealiseerde winsten in voorraden of vaste activa (intercompany-winst op nog niet aan derden doorverkochte goederen) worden geëlimineerd uit voorraden/activa én uit het resultaat van de verkopende entiteit. Gerealiseerde winsten (door derden doorverkochte goederen) blijven staan.

<small>📚 KB WVV — art. 3:135 — _kb_ · ISA 600 — par. A23 + Bijlage 2 — _norm_</small>

### 📜 Detectie en presentatie van minderheidsbelangen  
_`regel`_

📖 Wanneer de moeder minder dan 100 % bezit, ontstaat een minderheidsbelang. Dat belang bestaat uit (1) het aandeel van derden in het EV van de dochter — gepresenteerd in rubriek IX 'Belangen van derden' van het geconsolideerde EV, apart van het groeps-EV (kapitaal, reserves moeder); en (2) het aandeel van derden in het resultaat van de dochter — gepresenteerd als afzonderlijke regel onder het geconsolideerde resultaat ('aandeel derden in het resultaat'). Zie verder het record minderheidsbelangen voor diepgang.

<small>📚 KB WVV — art. 3:132 — _kb_ · KB WVV — art. 3:145 — _kb_</small>

### 👣 Toepassing uniforme waarderingsregels  
_`stap`_

📖 Vóór de integrale opname moeten de waarderingsregels van de dochter aangepast worden aan de groepswaarderingsregels (art. 3:117 KB WVV). Verschillen in afschrijvingsmethoden, voorraadwaardering, voorzieningen-beleid, ... worden weggewerkt door pre-consolidatie-aanpassingen op de dochterbalans. Zonder uniformisering is de groepsbalans niet vergelijkbaar en geeft geen getrouw beeld.

<small>📚 KB WVV — art. 3:117 — _kb_</small>

## Voorbeelden

### 💡 Integrale consolidatie 80%-dochter (CBN 2022/09 — voorbeeld 10) 📖

_Vennootschap X bezit 80 % van X1, met aanschaffingswaarde 200. EV X1 = 250 + 200 = 450 (kapitaal + reserves). Aandeel X in EV X1 = 80 % × 450 = 360. Consolidatieverschil = 200 - 360 = -160 (negatief — passief)._

**Balans-snapshot**: ``

```json
{
  "titel": "Geconsolideerde balans X+X1 na integrale consolidatie",
  "tekst": "Immateriële vaste activa: 400 — Materiële vaste activa: 500 — Geldbeleggingen: 90 — Totaal activa: 990. Kapitaal: 100 — Reserves: 300 — Consolidatieverschil (passief): 160 — Belangen van derden (20% × 450 = 90): 90 — Schulden: 340 — Totaal passiva: 990."
}
```

<small>📚 CBN-advies — 2022/09 — voorbeeld 10 — _cbn_</small>

## Valkuilen

### ⚠️ Integraal opnemen ≠ 100% bezitten

**Verkeerde assumptie**: Studenten denken dat integrale consolidatie 100 % deelneming vereist.

**Kernpunt**: Integraal opnemen betekent 100 % van activa/passiva opnemen — niet 100 % bezitten. Een 51%-dochter wordt ook integraal geconsolideerd; het verschil komt tot uiting in de minderheidsbelangen-rubriek (49 % belang van derden), niet in een gewijzigde opname-graad.

<small>📚 KB WVV — art. 3:131 — _kb_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### ⚠️ Intercompany-vorderingen vergeten te elimineren

**Verkeerde assumptie**: Bij optellen van balans M + D blijft de vordering M op D + de schuld D aan M staan.

**Kernpunt**: Dat zou de groepsbalans 'opblazen' met een transactie van de groep met zichzelf. Verplichte eliminatie: vordering en schuld worden weggestreept (resultaat-neutraal). Idem voor intercompany-omzet — die wordt 100 % geëlimineerd uit omzet en aankopen.

<small>📚 KB WVV — art. 3:135 — _kb_</small>

### ⚠️ De-facto-controle missen

**Verkeerde assumptie**: Geen meerderheid stemrechten → geen integrale consolidatie.

**Kernpunt**: Art. 1:14 §3 WVV: ook zonder formele meerderheid kan controle bestaan (bv. dispersed shareholder base waar de moeder de facto stemmenmeerderheid haalt op de laatste twee AV's). Dan toch integrale consolidatie.

<small>📚 KB WVV — art. 1:14 §3 — _kb_</small>

## Accountant-perspectieven

### Groepsmoedervennootschap (consolidatieverantwoordelijke)

_De accountant of consolidatieverantwoordelijke die de geconsolideerde jaarrekening van de moeder opstelt._

#### 📒 Boekhouder

##### 👣 Mapping individueel naar groeps-rekeningenstelsel  
_`stap`_

🔗 Eerst alle dochter-balansen en -resultatenrekeningen converteren naar het groeps-rekeningenstelsel. Vervolgens uniforme waarderingsregels toepassen (art. 3:117 KB WVV). Daarna integraal optellen, deelneming elimineren tegen EV-aandeel, consolidatieverschil boeken, intercompany-eliminaties uitvoeren, minderheidsbelang berekenen.

<small>📚 KB WVV — art. 3:117 — _kb_ · KB WVV — art. 3:131 — _kb_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

#### 🔍 Auditor

##### 👣 ISA 600 — groepscontrole-bewijs  
_`stap`_

📖 De groepsauditor verkrijgt inzicht in het consolidatieproces (handmatige + geautomatiseerde stappen), de uniforme waarderingsregels en de matching/eliminatie van intercompany-transacties (ISA 600 Bijlage 2). Hij beoordeelt de werkzaamheden van auditors van significante groepsonderdelen en hercontroleert kritieke consolidatie-aanpassingen.

<small>📚 ISA 600 — par. A23 + Bijlage 2 — _norm_</small>

## Verder lezen (scope-out)

- → Consolidatiemethoden Σ-keuze-kader → [[consolidatiemethoden]] _(moet-verwijzen)_
- ↪ Minderheidsbelangen (alleen relevant bij integraal) → [[minderheidsbelangen]] _(mag-verwijzen)_

## Relaties

### `valt_onder`
- [[consolidatiemethoden]]
### `vereist`
- ⏳ controle-vennootschap — Vereist exclusieve controle (art. 1:14 §1 WVV) — onweerlegbaar bij meerderheid stemrechten of statutair benoemingsrecht; weerlegbaar bij de-facto-controle (art. 1:14 §3).
### `triggert`
- [[minderheidsbelangen]] — Bij <100 % belang ontstaat een minderheidsbelang dat afzonderlijk in EV en resultaat gepresenteerd wordt.
- [[consolidatieverschil]] — Verschil tussen aanschaffingsprijs deelneming en aandeel in EV op verkrijgingsdatum → goodwill (positief) of badwill (negatief).
### `vergelijkbaar_met`
- [[vermogensmutatiemethode]]
    - **Gelijkenissen**:
        - Beide consolideren een deelneming in de geconsolideerde jaarrekening
        - Beide elimineren de deelneming uit de moederbalans
    - **Verschillen**:
        - Integraal: 100 % van activa/passiva regel-per-regel + minderheidsbelang afzonderlijk
        - Vermogensmutatie: één balanslijn 'deelneming geconsolideerd via VMM', geen minderheidsbelang
        - Integraal bij exclusieve controle; vermogensmutatie bij notabele invloed (geen controle)
    - ⚠️ **Verwarringsrisico**: Studenten denken dat 'consolidatie' altijd integraal is — terwijl associates (notabele invloed zonder controle) verplicht vermogensmutatie krijgen (art. 3:139 KB WVV).
- [[evenredige-consolidatie]]
    - **Gelijkenissen**:
        - Beide nemen activa/passiva regel-per-regel op (geen één-regel-presentatie)
    - **Verschillen**:
        - Integraal: 100 % opname + minderheidsbelang voor derden
        - Evenredig: pro rata (aandeel in JV-vermogen) — typisch 50 % bij 50/50-JV
        - Integraal bij exclusieve controle; evenredig bij gezamenlijke controle (joint operation onder BE-GAAP)
