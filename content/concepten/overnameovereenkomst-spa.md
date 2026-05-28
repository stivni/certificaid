---
title: "Overnameovereenkomst (SPA)"
concept_type: "instrument"
schema_version: "2.2"
status: "concept"
categorieen:
  - entiteit
ankers:
  - 3.0.taak.2
  - 3.0.taak.3
  - 2.3.III.B
tags:
  - concept
  - schema-2.2
  - type-instrument
  - cat-entiteit
  - status-concept
gegenereerd_uit: "data/concepten/records/overnameovereenkomst-spa.json"
---

# Overnameovereenkomst (SPA)

_Instrument_

🏢 Entiteit · Anchors: `3.0.taak.2` · `3.0.taak.3` · `2.3.III.B` · Wave: `skeleton-vennootschapsrecht-2026-05-28`

> [!info] 📝 **Concept** — content gevuld door cluster-extract; niet door mens-verify gegaan.

**Afk.**: SPA — **Synoniemen**: Share Purchase Agreement · Asset Purchase Agreement (APA) · overnamecontract — **Vertalingen**: en: Share Purchase Agreement

## Definitie

🔗 De overnameovereenkomst (Engels Share Purchase Agreement bij aandelenovername, Asset Purchase Agreement bij handelsfonds-overname) is het contractueel kerninstrument dat een overdracht van onderneming regelt. Ze legt vast wie wat aan wie verkoopt, voor welke prijs, onder welke voorwaarden, met welke garanties en wat er gebeurt als de garanties niet kloppen. Het is een gewone koop-verkoop-overeenkomst in burgerlijk recht (oud BW art. 1582 e.v.), maar contractueel sterk uitgebreid omdat het voorwerp — een levende onderneming — veel verborgen risico's draagt die in de basis-koopregels niet zijn voorzien.

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28) · CBN-advies 126/15 — aanpassing aan-/verkoopprijs — _advies_</small>

## Substantie

🤖 De SPA is in praktijk vaak 50 tot 150 paginas lang, met meer dan de helft besteed aan R&W (representations & warranties) en vrijwaring (indemnification). Reden: bij overdracht van een onderneming weet de koper nooit volledig wat hij koopt — er kunnen latente fiscale claims, lopende geschillen, milieuverplichtingen of foutieve cijfers schuilgaan. Het R&W-pakket is de manier waarop de verkoper bevestigt dat 'wat hij toont, klopt' en zich verbindt om schade te dragen indien iets uit zijn waarborgen achteraf onjuist blijkt. De prijsaanpassings-mechanismen (closing accounts of locked-box) zorgen ervoor dat de uiteindelijke prijs overeenstemt met de waarde van de onderneming op closing-datum.

<small>📚 CBN-advies 126/15 — waarborgen + prijsherziening — _advies_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Rationale

🔗 Waarom zo'n lange overeenkomst voor een 'gewone' koop-verkoop? Omdat het algemene koop-recht (oud BW) onvoldoende beschermt tegen overdracht-specifieke risico's. Het oud-BW kent vrijwaring voor verborgen gebreken (art. 1641), maar binnen heel beperkte tijdsspanne en alleen voor 'materiele' gebreken. Een latente belastingschuld of een onbestaande klant kwalificeert niet als materieel gebrek in burgerlijk-rechtelijke zin. Vandaar dat partijen alles contractueel inkleden: wat ik garandeer, hoe lang ik daar voor opdraai, tot welke maximumbedrag, en hoe geschillen worden opgelost.

<small>📚 Burgerlijk Wetboek — art. 1641 e.v. (verborgen gebreken) — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Gebruikscontext

**Status**: `in-voege` · basis: Burgerlijk recht (koop-verkoop, contractsvrijheid art. 5.14 nieuw BW, oud-BW art. 1134 e.v.)

**✅ Voor**
- 🤖 Elke private M&A-transactie waarbij een onderneming of een deelneming overgaat van de ene partij naar de andere — share-deal, asset-deal, secondary-deal.

**🚫 Niet voor**
- 🤖 Beursgenoteerde overnames met openbaar bod — daar gelden specifieke regels van de wet op de openbare overnamebiedingen.

## Sub-concepten

### 📦 Voorwerp en prijs  
_`kader` (subconcept)_

#### Definitie

🤖 Het voorwerp wordt exact omschreven: het aantal aandelen of de lijst van activa, met identificatie van de doelvennootschap of het over te dragen handelsfonds. De prijs wordt geuit als een bedrag (of een berekenings-formule op closing-datum) plus een aanpassingsmechanisme om te corrigeren voor wijzigingen tussen signing en closing.

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

#### Substantie

🤖 Twee gebruikelijke prijsmechanismen: (1) Closing accounts (Anglo-Saksisch model): de prijs wordt voorlopig vastgesteld bij signing, daarna gecorrigeerd op basis van een effectieve balans op closing-datum (vooral werkkapitaal en netto-schuld). (2) Locked-box (Europees model): de prijs is definitief op basis van een eerdere balans (de 'locked box date'), gekoppeld aan een verbod voor de verkoper om waarde uit de onderneming te halen ('leakage') tussen die datum en closing.

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### 📦 Representations & warranties (R&W)  
_`instrument` (subconcept)_

#### Definitie

🤖 Een catalogus van uitspraken die de verkoper bevestigt als juist op signing en typisch herhaalt op closing. Voorbeelden: 'De jaarrekeningen zijn opgesteld in overeenstemming met BE-GAAP en geven een getrouw beeld', 'Er zijn geen lopende belangrijke geschillen', 'Alle vergunningen zijn geldig en in regel', 'Er bestaat geen change-of-control-clausule die door deze transactie wordt getriggerd'. Indien een R&W achteraf onjuist blijkt, kan de koper de verkoper aansprakelijk stellen voor de geleden schade.

<small>📚 CBN-advies 126/15 — waarborgen werkelijkheid waarderingen — _advies_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### 📦 Vrijwaring en beperkingen (caps, baskets, survival)  
_`instrument` (subconcept)_

#### Definitie

🤖 De aansprakelijkheid van de verkoper voor R&W-schendingen wordt typisch beperkt door: (a) Cap — maximum bedrag waarvoor de verkoper kan worden aangesproken (vaak 10-30% van de aankoopprijs); (b) Basket — drempel waaronder geen claim mogelijk is (de minimis-drempel) en/of de claim slechts geldt boven een bepaalde aggregate threshold; (c) Survival — tijdslimiet binnen welke een claim moet worden gemeld (typisch 12-24 maanden voor business reps, langer voor fiscale en titel-reps); (d) Knowledge qualifiers ('to the knowledge of seller') — beperking tot wat de verkoper wist of redelijkerwijs moest weten.

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### 📦 Opschortende voorwaarden (conditions precedent)  
_`kader` (subconcept)_

#### Definitie

🤖 Voorwaarden die vervuld moeten zijn vooraleer closing kan plaatsvinden. Klassieke voorbeelden: (a) regelgevende goedkeuringen (mededingingsautoriteit, FSMA bij beursgenoteerde context); (b) instemming van bepaalde tegenpartijen bij change-of-control-clausules; (c) afwezigheid van een MAC (material adverse change) tussen signing en closing; (d) bevestiging dat R&W op closing nog steeds juist zijn ('bring-down').

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### 📦 MAC-clausule (material adverse change)  
_`instrument` (subconcept)_

#### Definitie

🤖 Een opschortende voorwaarde of ontbindingsgrond die de koper toelaat de transactie af te blazen of de prijs te heronderhandelen als zich tussen signing en closing een materieel nadelige verandering voordoet in de business, financiele positie, vooruitzichten of regelgevende omgeving van de doel. De definitie 'materieel' is sterk onderhandeld — meestal worden externe gebeurtenissen (macroeconomische schokken, oorlogen, pandemie) uitgesloten.

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### 📦 Post-closing-verplichtingen  
_`kader` (subconcept)_

#### Definitie

🤖 Verbintenissen die na closing nog gelden. Typisch: (a) Non-compete — de verkoper verbindt zich om gedurende N jaar (vaak 2-3 jaar) niet te concurreren met de overgedragen activiteit; (b) Non-solicit — geen actief benaderen van werknemers of klanten; (c) Transitie-assistentie — de verkoper helpt de koper met overdracht van kennis en relaties; (d) Escrow-arrangement — een deel van de prijs wordt geblokkeerd op een rekening om eventuele claims onder R&W te dekken (vrijgave na N maanden).

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Bouwstenen

### 👣 Typische structuur van een SPA  
_`stap`_

**Substantie**: 🤖 De SPA volgt doorgaans een vaste structuur.

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

**Weergave** `stappenlijst`:

```json
{
  "stappen": [
    "1. Partijen en achtergrond (whereas-clauses)",
    "2. Definities (lange lijst — bepaalt betekenis in heel het contract)",
    "3. Voorwerp en prijs (incl. prijsmechanisme)",
    "4. Opschortende voorwaarden voor closing",
    "5. Verplichtingen tussen signing en closing (interim covenants)",
    "6. Closing-procedure (wat wordt op closing-dag uitgewisseld)",
    "7. Representations & warranties (verkoper + koper)",
    "8. Vrijwaring en beperkingen (caps, baskets, survival)",
    "9. Post-closing-verplichtingen (non-compete, transitie, escrow)",
    "10. Geschillenbeslechting + toepasselijk recht + diversen"
  ]
}
```

### 📜 Boekhoudkundige verwerking van prijsherziening  
_`regel`_

📖 Indien R&W-claims leiden tot een prijsherziening: bij de koper wordt de aanschaffingswaarde van de deelneming overeenkomstig aangepast; bij de verkoper wordt de gerealiseerde meerwaarde of minderwaarde aangepast (verhogen of verlagen). Indien de claim leidt tot een vergoeding (niet tot prijsaanpassing), wordt dit als opbrengst of last verwerkt afhankelijk van de afspraak in de overeenkomst.

<small>📚 CBN-advies 126/15 — boekhoudkundige verwerking prijsherziening — _advies_</small>

## Valkuilen

### ⚠️ R&W lezen als 'algemene goedheid' in plaats van als precieze juridische uitspraken

**Verkeerde assumptie**: R&W zijn standaardformuleringen die je gewoon copy-paste vanuit een precedent.

**Kernpunt**: Elke R&W is een precieze juridische verbintenis. 'Knowledge qualifiers' ('to the seller's knowledge') versus 'absolute reps' veranderen de aansprakelijkheid drastisch. Een 'wide' representation ('de jaarrekening is correct in alle materiele opzichten') geeft meer claimruimte dan een 'narrow' rep ('de jaarrekening is opgesteld in overeenstemming met BE-GAAP'). Lees elke woord.

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### ⚠️ Escrow vergeten te koppelen aan vrijgave-trigger

**Verkeerde assumptie**: Geld in escrow wordt automatisch na X maanden vrijgegeven aan de verkoper.

**Kernpunt**: Escrow-vrijgave wordt typisch gekoppeld aan (a) afwezigheid van pendings claims, (b) afwezigheid van bekendgemaakte schendingen, of (c) eindbalans tussen koper en verkoper. Het mechanisme moet contractueel exact zijn — wie geeft instructie aan de escrow-agent? Wat als beide partijen het oneens zijn?

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### ⚠️ Disclosure letter niet correct gebruiken

**Verkeerde assumptie**: De disclosure letter is een formaliteit waarin men 'voor de zekerheid' alles vermeldt.

**Kernpunt**: De disclosure letter beperkt de R&W: alles dat in de disclosure letter wordt vermeld, vormt geen schending van een R&W. Een te ruime disclosure letter ondergraaft de bescherming van de koper. Een te beperkte disclosure letter legt de verkoper open voor onnodige claims. Onderhandel met dezelfde zorg als de R&W zelf.

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Accountant-perspectieven

### Accountant als adviseur bij SPA-onderhandeling

_De gecertificeerd accountant heeft een rol bij het cijfermatige luik van de SPA: prijsmechanisme, closing accounts, definities van EBITDA en netto-schuld._

#### 🧭 Adviseur

##### 👣 Advies over prijsmechanisme  
_`stap`_

**Substantie**: 🤖 Stap 1: definieer EBITDA voor de doelvennootschap (normalisaties — eigenaar-bezoldiging, niet-recurrente posten). Stap 2: definieer 'net debt' en 'working capital' (welke items tellen mee, welke niet). Stap 3: stel een referentiebalans op (locked-box) of beschrijf de closing accounts-procedure. Stap 4: definieer 'leakage' bij locked-box (welke uitstromen zijn verboden tussen locked-box-datum en closing). Stap 5: review het R&W-pakket op cijfermatige uitspraken (jaarrekening juist, voorraden gewaardeerd, voorzieningen adequaat).

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Verder lezen (scope-out)

- → Overdracht-onderneming als Sigma-context → [[overdracht-onderneming]] _(moet-verwijzen)_
- → Aandeelhoudersovereenkomsten — raakvlak (na overdracht in joint-venture-structuur) → [[aandeelhoudersovereenkomsten]] _(moet-verwijzen)_

## Relaties

### `valt_onder`
- [[overdracht-onderneming]]
### `vergelijkbaar_met`
- [[aandeelhoudersovereenkomsten]] — Beide regelen rechten tussen aandeelhouders, maar SPA regelt de eenmalige overdracht, aandeelhoudersovereenkomst regelt het lopende samenleven.
    - **Gelijkenissen**:
        - Beide zijn contracten tussen aandeelhouders
        - Beide bevatten clausules over aandelen, governance en exit
    - **Verschillen**:
        - SPA = transactie-document (one-shot, signing → closing); aandeelhoudersovereenkomst = duurzaam document (loopt zolang partijen aandeelhouder zijn)
        - SPA focust op overdracht en R&W; aandeelhoudersovereenkomst focust op governance, blokkeringen, exit-rechten
