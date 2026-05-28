---
title: "Opeisbaarheid van de BTW"
concept_type: "principe"
schema_version: "2.2"
status: "concept"
categorieen:
  - regeling
ankers:
  - 2.4.I
tags:
  - concept
  - schema-2.2
  - type-principe
  - cat-regeling
  - status-concept
gegenereerd_uit: "data/concepten/records/opeisbaarheid-btw.json"
---

# Opeisbaarheid van de BTW

_Principe_

📋 Regeling · Anchors: `2.4.I` · Wave: `skeleton-btw-internationaal-2026-05-28`

> [!info] 📝 **Concept** — content gevuld door cluster-extract; niet door mens-verify gegaan.

**Synoniemen**: tijdstip btw verschuldigd · exigibilité TVA — **Vertalingen**: fr: exigibilité de la TVA

## Definitie

📖 Opeisbaarheid is het exacte tijdstip waarop de btw juridisch verschuldigd wordt aan de Schatkist en in de aangifte van het overeenstemmende tijdvak moet worden opgenomen. Het W.BTW onderscheidt twee begrippen die vaak samenvallen maar conceptueel verschillen: (a) het belastbaar feit — het moment waarop wettelijk de voorwaarden voor de heffing vervuld zijn (= levering, dienst, intracommunautaire verwerving, invoer); (b) de opeisbaarheid — het moment waarop de Schatkist de belasting daadwerkelijk mag innen. Hoofdregel (art. 17 W.BTW): de btw wordt opeisbaar op het tijdstip van de levering of dienst, MAAR indien er eerder een factuur wordt uitgereikt of een betaling wordt ontvangen, dan op dat eerdere tijdstip.

<small>📚 W.BTW — art. 17, §1 — _wettekst_ · Richtlijn 2006/112/EG — art. 62-66 — _richtlijn_</small>

## Substantie

🔗 Opeisbaarheid bepaalt in welke btw-aangifte (welke maand of welk kwartaal) de output-btw moet worden gemeld en de input-btw mag worden afgetrokken. Een fout van één dag rond een maand- of kwartaaleinde kan het verschil maken tussen tijdige en laattijdige aangifte — met proportionele boetes (art. 70 W.BTW) en nalatigheidsinteresten (art. 91) als gevolg. Sinds de hervorming van 2013 geldt het 'kasstelsel-light': de btw wordt opeisbaar bij factuur of bij betaling, naargelang welke gebeurtenis eerst plaatsvindt — niet meer zuiver bij het belastbaar feit. Voor doorlopende prestaties (huur, abonnement, leasing) bestaat een specifieke regeling (art. 22bis): opeisbaarheid op het einde van elke afrekenperiode (max 1 jaar).

<small>📚 W.BTW — art. 17 + art. 22bis + art. 70 + art. 91 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Rationale

🔗 De ratio van de opeisbaarheidsregels is tweeledig: (1) zorgen dat btw effectief wordt geïnd op het moment dat de transactie economisch is voltrokken (cashflow voor de Schatkist); (2) vermijden dat partijen door late facturatie de btw kunnen uitstellen. Het W.BTW koos bewust voor het vroegste van twee tijdstippen (levering OF factuur OF voorschot) om dergelijk uitstel te beletten. Voor doorlopende prestaties is een afgeleide regel nodig omdat er geen unieke 'leverdag' is — daarom de afrekenperiode-aanpak.

<small>📚 Richtlijn 2006/112/EG — art. 62-66 — _richtlijn_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Sub-concepten

### 📦 Hoofdregel — art. 17 W.BTW  
_`regime` (subconcept)_

#### Definitie

📖 Art. 17, §1 W.BTW: voor leveringen van goederen en dienstverrichtingen tussen belastingplichtigen wordt de btw opeisbaar op het tijdstip dat het belastbaar feit plaatsvindt (levering of voltooiing dienst — art. 16/22), MAAR de opeisbaarheid wordt vervroegd tot: (a) de datum van uitreiking van de factuur indien deze vóór het belastbaar feit wordt opgemaakt; (b) de datum van ontvangst van een betaling indien deze vóór het belastbaar feit en vóór de factuur wordt verricht. Voor B2C-handelingen geldt sinds 2016 een vereenvoudigde regel: opeisbaarheid bij het belastbaar feit of bij ontvangst van een betaling (geen automatische vervroeging via factuur, want B2C-facturen zijn vaak niet verplicht).

<small>📚 W.BTW — art. 17, §1 + §3 — _wettekst_</small>

#### 🧭 Opeisbaarheid — beslissende gebeurtenis per scenario  
_`vuistregel`_

**Substantie**: 📖 Voor het bepalen van het juiste aangifte-tijdvak: het VROEGSTE van de relevante gebeurtenissen telt.

<small>📚 W.BTW — art. 17 — _wettekst_</small>

### 📦 Doorlopende prestaties — art. 22bis W.BTW  
_`regime` (subconcept)_

#### Definitie

📖 Voor diensten en goederen die over een langere periode worden geleverd zonder afzonderlijke deelleveringen (huur, abonnement, leasing, doorlopende energie-levering, opslag) geldt art. 22bis: de btw wordt opeisbaar op het einde van elke afrekenperiode. De afrekenperiode mag niet langer zijn dan één jaar. Bij ontvangen voorschotten geldt de algemene regel (opeisbaarheid bij ontvangst voorschot).

<small>📚 W.BTW — art. 22bis — _wettekst_</small>

### 📦 Intracommunautaire handelingen — opeisbaarheid  
_`regime` (subconcept)_

#### Definitie

📖 Bij intracommunautaire leveringen (art. 39bis) is de btw aan 0 % opeisbaar op het tijdstip van uitreiking van de factuur of uiterlijk de 15e dag van de maand volgend op het belastbaar feit. Bij intracommunautaire verwervingen (art. 25sexies) geldt dezelfde regel voor de afnemer die de btw verlegd betaalt. De afstemming met de IC-listing is cruciaal — de Belgische uitgaande IC-levering moet in het kwartaal van opeisbaarheid worden gemeld.

<small>📚 W.BTW — art. 17, §2 + art. 25sexies — _wettekst_</small>

## Voorbeelden

### 💡 Concrete cases — bepaal het aangifte-tijdvak 🔗

_Maandaangifte. Bepaal voor elk geval in welk btw-tijdvak de output-btw moet worden gemeld._

| Casus | Opeisbaarheid | Aangifte |
| --- | --- | --- |
| Levering kantoormeubilair 28/2; factuur opgesteld 7/3; betaald 15/4 | 28/2 (levering = belastbaar feit) | Februari |
| Aannemingscontract: 30 % voorschot ontvangen 10/1, werk voltooid 20/4, eindfactuur 25/4 | Voorschot: 10/1 (op 30%) — Saldo: 20/4 (op 70%) | Januari (voorschot) + April (saldo) |
| Huur kantoor: maandhuur 1 000 EUR + 21 %, jaarlijkse vaste afrekening op 31/12 | Maandhuur per maandeinde (art. 22bis, korte afrekenperiode) | Maandelijks |
| Levering van computer 18/3; factuur opgesteld 8/3 (voor levering); betaling 25/4 | 8/3 (factuur vroegtijdig vóór belastbaar feit) | Maart |

<small>📚 W.BTW — art. 17 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Valkuilen

### ⚠️ Opeisbaarheid ≠ betalingstermijn

**Verkeerde assumptie**: Btw is verschuldigd wanneer de klant effectief betaalt.

**Kernpunt**: Opeisbaarheid heeft NIETS te maken met de feitelijke betaling door de klant. Btw is verschuldigd aan de Schatkist op het moment van levering, factuur of voorschot — wat ook het eerste is. Wanneer de klant pas drie maanden later betaalt, heeft de leverancier de btw al lang afgedragen. Dat creëert een liquiditeitsdruk: de leverancier moet btw voorfinancieren. Bij definitieve oninvorderbaarheid kan teruggave gevraagd worden (art. 77 W.BTW), maar dat is een aparte procedure.

<small>📚 W.BTW — art. 17 + art. 77 — _wettekst_</small>

### ⚠️ Voorschot triggert ook btw

**Verkeerde assumptie**: Een voorschot is een schuld — geen levering — dus geen btw.

**Kernpunt**: Bij ontvangst van een voorschot (vóór levering of voltooiing dienst) wordt de btw onmiddellijk opeisbaar op het ontvangen bedrag. Een proforma-factuur of voorschotnota moet worden opgemaakt en de btw moet in het aangifte-tijdvak van ontvangst worden opgenomen.

<small>📚 W.BTW — art. 17, §1 — _wettekst_</small>

### ⚠️ Eindejaar-grens: één dag telt

**Verkeerde assumptie**: Een factuur eind december valt automatisch in het volgende boekjaar/aangifte als ze pas in januari verstuurd wordt.

**Kernpunt**: De opeisbaarheid bepaalt het btw-aangifte-tijdvak, niet de verzendingsdatum van de factuur. Een levering op 30/12 valt — bij gebrek aan eerdere factuur of voorschot — in het aangifte-tijdvak december, ook al wordt de factuur pas op 5/1 opgemaakt en verstuurd. Dit is een typische bron van laattijdige aangiftes en boetes (art. 70, §1, 1° W.BTW: 10 % proportionele boete bij niet-aangifte).

<small>📚 W.BTW — art. 17 + art. 70 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Verder lezen (scope-out)

- → Factuurplicht + vermeldingen → [[factuur-btw]] _(moet-verwijzen)_
- → BTW-aangifte (welk tijdvak) → [[btw-aangifte]] _(moet-verwijzen)_

## Relaties

### `valt_onder`
- [[btw]]
### `vereist`
- [[btw-levering-goederen]]
- [[btw-dienstverlening]]
