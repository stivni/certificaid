---
title: "Materiële vaste activa (IFRS — IAS 16)"
concept_type: "balanspost"
schema_version: "2.2"
status: "concept"
categorieen:
  - entiteit
ankers:
  - 1.5.V.A
  - 1.5.V.B
tags:
  - concept
  - schema-2.2
  - type-balanspost
  - cat-entiteit
  - status-concept
gegenereerd_uit: "data/concepten/records/materiele-vaste-activa.json"
---

# Materiële vaste activa (IFRS — IAS 16)

_Balanspost_

🏢 Entiteit · Anchors: `1.5.V.A` · `1.5.V.B` · Wave: `cluster-extract-balansposten-activa-2026-05-28`

> [!info] 📝 **Concept** — content gevuld door cluster-extract; niet door mens-verify gegaan.

**Synoniemen**: property, plant and equipment · PP&E — **Vertalingen**: en: property, plant and equipment · fr: immobilisations corporelles

## Definitie

📖 IAS 16 'Materiële vaste activa' definieert deze als materiële activa die (a) door een entiteit worden aangehouden voor gebruik in de productie of de levering van goederen of diensten, voor verhuur aan derden of voor administratieve doeleinden, én (b) naar verwachting langer dan één boekjaar zullen worden gebruikt. Opname bij eerste opname (alinea 15): tegen de kostprijs — aankoopprijs + invoerrechten + niet-restituurbare aankoopbelastingen, na aftrek handelskortingen, plus directly attributable costs (transport, installatie, testkosten, deconstructie-verplichting). Latere waardering (alinea 29): keuze tussen het kostprijsmodel (alinea 30) of het herwaarderingsmodel (alinea 31), gemaakt op het niveau van een 'klasse' van MVA.

<small>📚 Verordening (EU) 2023/1803 — IAS 16 — alinea 6, 15-16, 29-31 — _wettekst_</small>

## Substantie

📖 IAS 16 zit dichter bij Belgische Be-GAAP dan IFRS 16 (lease) of IAS 38 (IMA) — maar drie verschillen blijven cruciaal: (1) Component-aanpak (alinea 43-44): een MVA-onderdeel met afzonderlijke levensduur (vliegtuigmotor, dak gebouw) moet apart afgeschreven worden. Be-GAAP staat dit toe maar verplicht het niet. (2) Herwaarderingsmodel (alinea 31-42): periodieke fair-value-toets met meerwaarde naar OCI (herwaarderingsreserve in EV) of resultaat. Be-GAAP kent herwaardering ook maar met striktere voorwaarden (art. 57 KB WVV). (3) Impairment (kruisverwijzing IAS 36): jaarlijkse test indien indicatoren — afboeking direct naar resultaat. Be-GAAP gebruikt 'waardevermindering' (rubriek 631) bij duurzame waardedaling.

<small>📚 Verordening (EU) 2023/1803 — IAS 16 — alinea 31-44, IAS 36 — _wettekst_</small>

## Rationale

🔗 IAS 16 streeft naar economische realiteit: een gebouw van 100 jaar bestaat uit verschillende sub-componenten (structuur, dak, technische installaties, interieur) met verschillende slijtage-snelheden. Component-aanpak voorkomt dat een MVA met gemiddelde afschrijvingsduur de werkelijkheid maskeert. Het herwaarderingsmodel laat ondernemingen toe om aanzienlijke prijsstijging (gebouwen) te tonen — wat Be-GAAP nog steeds beperkt. Voor de stagiair die later in een IFRS-omgeving werkt (beursgenoteerd of dochter van internationale groep): leer de drie verschillen + de impact op de jaarrekening (hogere boekwaarde + hogere afschrijving onder herwaardering).

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Sub-concepten

### 📦 Initiële waardering — kostprijs + directly attributable costs  
_`procedure` (subconcept)_

#### Definitie

📖 IAS 16 alinea 16: kostprijs MVA omvat (a) aankoopprijs incl. invoerrechten + niet-restituurbare belastingen, na aftrek kortingen; (b) directly attributable costs om actief op de huidige locatie en in de huidige staat te brengen (transport, installatie, montage, testkosten); (c) initiële schatting van kosten voor ontmanteling/verwijdering/herstel locatie (asset retirement obligation — voorziening volgens IAS 37). Niet meeneembaar (alinea 19): training personeel, advertising-kosten voor lancering, administratie en algemene overhead.

<small>📚 Verordening (EU) 2023/1803 — IAS 16 — alinea 16-19 — _wettekst_</small>

### 📦 Kostprijsmodel vs herwaarderingsmodel  
_`procedure` (subconcept)_

#### Definitie

📖 IAS 16 alinea 29-42: per MVA-klasse kiezen. Kostprijsmodel (alinea 30): boekwaarde = kostprijs − geaccumuleerde afschrijvingen − geaccumuleerde impairment-verliezen. Herwaarderingsmodel (alinea 31): boekwaarde = reële waarde op herwaarderings-datum − latere afschrijvingen − latere impairment. Reële waarde kan worden bepaald via marktbenadering, kostprijsbenadering of inkomstenbenadering (IFRS 13). Herwaardering moet regelmatig genoeg gebeuren om afwijking van reële waarde materieel klein te houden — jaarlijks voor volatiele activa, om de 3-5 jaar voor andere.

<small>📚 Verordening (EU) 2023/1803 — IAS 16 — alinea 29-42 — _wettekst_</small>

### 📦 Afschrijving — systematic basis + component-aanpak  
_`procedure` (subconcept)_

#### Definitie

📖 IAS 16 alinea 43-62: afschrijfbaar bedrag (kostprijs − restwaarde) wordt systematisch toegewezen over de gebruiksduur. Methode (alinea 60-62): lineair OF degressief OF productie-eenhedenmethode — moet de wijze weerspiegelen waarop de toekomstige economische voordelen worden verbruikt. Component-aanpak (alinea 43): elk onderdeel van significante kostprijs ten opzichte van totaal MVA moet afzonderlijk worden afgeschreven (vliegtuigmotor 8 jaar, vliegtuigcasco 20 jaar). Restwaarde (alinea 50-53) jaarlijks herzien.

<small>📚 Verordening (EU) 2023/1803 — IAS 16 — alinea 43-62 — _wettekst_</small>

### 📦 De-recognition + meer-/minderwaarden  
_`procedure` (subconcept)_

#### Definitie

📖 IAS 16 alinea 67-72: actief uitboeken bij vervreemding of wanneer geen toekomstige economische voordelen meer verwacht. Meer-/minderwaarde = netto-opbrengst − boekwaarde, geboekt in resultaat (geen omclassificatie van herwaarderingsreserve via resultaat — alleen via OCI naar overgedragen resultaat).

<small>📚 Verordening (EU) 2023/1803 — IAS 16 — alinea 67-72 — _wettekst_</small>

## Valkuilen

### ⚠️ Component-aanpak negeren

**Verkeerde assumptie**: Een MVA met meerdere onderdelen kan altijd als één geheel afgeschreven worden.

**Kernpunt**: IAS 16 alinea 43-44 vereist component-aanpak voor onderdelen met significante kostprijs ten opzichte van totaal en afwijkende gebruiksduur. Klassieke voorbeelden: vliegtuig (motor vs casco), gebouw (structuur vs dak vs technische installaties), schip (romp vs motor vs interieur). Belangrijk voor groot-equipment audit-cliënten.

<small>📚 Verordening (EU) 2023/1803 — IAS 16 — alinea 43-44 — _wettekst_</small>

### ⚠️ Herwaardering-meerwaarde direct in resultaat

**Verkeerde assumptie**: Herwaarderings-meerwaarde gaat naar resultaat zoals reële-waarde-mutaties van financiële instrumenten.

**Kernpunt**: IAS 16 alinea 39-40: meerwaarde uit herwaardering MVA wordt rechtstreeks in OCI (other comprehensive income) opgenomen onder 'herwaarderingsreserve'. Pas bij desinvestering of via afschrijvings-allocatie kan dit naar de overgedragen resultaten verschuiven — NOOIT via P&L. Uitzondering: herstel van eerdere herwaardering-vermindering die in P&L was geboekt (alinea 39).

<small>📚 Verordening (EU) 2023/1803 — IAS 16 — alinea 39-40 — _wettekst_</small>

## Accountant-perspectieven

### IFRS-rapportering (beursgenoteerd of dochter van internationale groep)

#### 📒 Boekhouder

##### 👣 Mapping Be-GAAP MVA naar IAS 16-rapportering  
_`stap`_

🔗 Bij IFRS-conversie: (1) heridentificeer componenten — splits MVA-eenheden op basis van afwijkende levensduur; (2) controleer kostprijs-componenten (geactiveerde directly attributable costs in lijn met alinea 16); (3) kies model per klasse (kostprijs of herwaardering); (4) toets impairment-indicatoren (IAS 36); (5) journal-entry voor cumulatieve verschillen via 'retained earnings adjustment' (eerste IFRS-toepassing IFRS 1).

<small>📚 Verordening (EU) 2023/1803 — IFRS 1 — Eerste toepassing — _wettekst_</small>

#### 🔍 Auditor

##### 👣 Impairment-toets (IAS 36) op MVA  
_`stap`_

📖 Jaarlijks: identificeer impairment-indicatoren (extern: marktdaling, technologische obsoletie; intern: fysieke schade, plan tot afstoting). Bij indicator: bepaal recoverable amount = max(fair value − sale costs; value in use via DCF). Vergelijk met boekwaarde — verschil boeken in P&L (geen OCI behalve voor herwaardeerde activa, alinea 39 omkering). Cash Generating Unit (CGU) als geen losse cash flows.

<small>📚 Verordening (EU) 2023/1803 — IAS 36 — alinea 9-17, 22 — _wettekst_</small>

## Verder lezen (scope-out)

- → Vaste activa B-GAAP-perspectief → [[vaste-activa]] _(moet-verwijzen)_
- → IFRS Σ overkoepelend → [[ifrs]] _(moet-verwijzen)_
- ↪ Herwaardering vast actief (B-GAAP-revaluation) → [[herwaardering-vast-actief]] _(mag-verwijzen)_

## Relaties

### `valt_onder`
- [[ifrs]]
### `alternatief_referentiestelsel`
- [[vaste-activa]] — IAS 16 voor materiële vaste activa onder IFRS; klasse 22-27 Be-GAAP-equivalent.
### `vereist`
- [[vaste-activa]] — Be-GAAP-basis als prerequisite.
### `vergelijkbaar_met`
- [[immateriele-vaste-activa]]
    - **Gelijkenissen**:
        - Beide IFRS-MVA-/IMA-categorieën
        - Beide kennen kostprijs- en herwaarderingsmodel
    - **Verschillen**:
        - MVA = fysiek; IMA = niet-fysiek
        - IMA strenger op herwaardering (alleen actieve markt — zeldzaam)
### `beinvloed_door`
- [[bijzondere-waardevermindering-ias-36]] — IAS 36 levert recoverable amount + impairment-test.
