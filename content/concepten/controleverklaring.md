---
title: "Controleverklaring"
concept_type: "instrument"
schema_version: "2.2"
status: "concept"
categorieen:
  - entiteit
ankers:
  - 1.6.IV.A
  - 1.6.IV.B
  - 1.6.IV.C
tags:
  - concept
  - schema-2.2
  - type-instrument
  - cat-entiteit
  - status-concept
gegenereerd_uit: "data/concepten/records/controleverklaring.json"
---

# Controleverklaring

_Instrument_

🏢 Entiteit · Anchors: `1.6.IV.A` · `1.6.IV.B` · `1.6.IV.C` · Wave: `skeleton-controle-beroep-2026-05-28`

> [!info] 📝 **Concept** — content gevuld door cluster-extract; niet door mens-verify gegaan.

**Synoniemen**: auditverslag · controleverslag · audit report · audit opinion · commissarisverslag — **Vertalingen**: fr: rapport du commissaire · en: auditor's report

## Definitie

📖 De controleverklaring is het schriftelijke eindproduct van een controleopdracht: het document waarin de gecertificeerd accountant of bedrijfsrevisor zijn oordeel formuleert over de financiële overzichten. Voor wettelijke commissaris-opdrachten wordt het ‘commissarisverslag’ genoemd (WVV art. 3:75) en gepubliceerd samen met de jaarrekening bij de NBB. Vorm en inhoud zijn streng gestandaardiseerd door ISA 700 (herzien) — afwijkingen hiervan zijn alleen toegestaan via ISA 705 (aangepast oordeel) en ISA 706 (aanvullende paragrafen).

<small>📚 ISA 700 (herzien) — Doelstellingen + Vereisten — _norm_ · WVV — art. 3:75 — _wettekst_ · Richtlijn 2013/34/EU — art. 35 — _wettekst_</small>

## Substantie

📖 De verklaring oogt op het eerste gezicht administratief — een paar pagina's standaardtekst — maar elke zin is **doelbewust gewogen**. De ‘Oordeel’-sectie staat sinds ISA 700 (herzien, 2015) bovenaan zodat lezers meteen weten waar ze aan toe zijn. De vier oordeelsvormen vormen een hard signaal-systeem voor de markt:

- **Zonder voorbehoud** → groen licht: ‘naar ons oordeel geven de financiële overzichten een getrouw beeld’.
- **Met voorbehoud** → oranje: getrouw beeld op alles behalve het specifieke probleem dat in een ‘basis voor oordeel met voorbehoud’-paragraaf wordt beschreven.
- **Afkeurend** → rood: de jaarrekening geeft géén getrouw beeld door materieel én diepgaand falen.
- **Onthouding** → grijs: auditor kon niet voldoende bewijs verkrijgen om enige uitspraak te doen.

Elk afwijken van ‘zonder voorbehoud’ is een schokevent voor stakeholders en heeft praktische gevolgen (banken trekken faciliteiten in, aandeelhouders eisen verklaring, governance wordt onder druk gezet).

<small>📚 ISA 700 (herzien) — par. 24-26 — _norm_ · ISA 705 (herzien) — Vereisten — _norm_</small>

## Rationale

🔗 Waarom zo strakke standaardisatie? (1) **Vergelijkbaarheid**: een lezer in Antwerpen die ook Frankfurter rapporten leest, herkent direct de structuur en oordeelsformulering. (2) **Beschermt de auditor tegen druk**: standaardtaal voorkomt dat management onderhandelt over wollige formuleringen die de markt zouden misleiden. (3) **Maakt de schaal van afwijking leesbaar**: het verschil tussen ‘met voorbehoud’ en ‘afkeurend’ is geen woordkwestie maar een wezenlijke kalibratie (materieel vs materieel én diepgaand). (4) **Geeft auditor een laatste hefboom in onderhandeling met cliënt**: ‘als jullie deze fout niet corrigeren, wordt het een met-voorbehoud-verklaring’ is een concrete dreiging die management vaak doet bewegen.

<small>📚 ISA 700 (herzien) — _norm_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Gebruikscontext

**Status**: `in-voege` · basis: ISA 700 (herzien) · ISA 701 · ISA 705 (herzien) · ISA 706 (herzien) · ISA 710 · Richtlijn 2013/34/EU art. 35 · WVV art. 3:75

ISA 700 (herzien) ingangsdatum boekjaren afsluitend op of na 15/12/2016. Verplichting kernpunten van de controle (KAM, ISA 701) geldt voor beursgenoteerde entiteiten — andere entiteiten kunnen vrijwillig KAM toevoegen.

**✅ Voor**
- 🔗 Wordt uitgegeven bij elke controleopdracht (audit, reasonable assurance). Voor beoordelings-, samenstellings- en AUP-opdrachten gelden andere verslag-vormen (ISRE 2400/2410 review-rapport; ISRS 4410 samenstellingsverslag; ISRS 4400 rapport van feitelijke bevindingen).

## Sub-concepten

### 📦 Oordeel zonder voorbehoud (goedkeurend / unqualified)  
_`regime` (subconcept)_

#### Definitie

📖 De standaardvorm wanneer de auditor concludeert dat de financiële overzichten in alle van materieel belang zijnde opzichten een getrouw beeld geven (BE-GAAP/IFRS-EU). De formulering is volgens ISA 700 par. 25-26 voorgeschreven:

*‘Naar ons oordeel geven de bijgevoegde financiële overzichten een getrouw beeld van [de financiële positie van de entiteit per 31 december 20X1, alsmede van haar financiële prestaties en kasstromen over het op die datum afgesloten boekjaar] in overeenstemming met [het van toepassing zijnde stelsel inzake financiële verslaggeving].’*

Voor compliance-stelsels (waar conformiteit met regelgeving wordt geattesteerd, niet ‘getrouw beeld’): ‘zijn opgesteld in overeenstemming met...’.

<small>📚 ISA 700 (herzien) — par. 25-26 — _norm_</small>

### 📦 Oordeel met voorbehoud (qualified)  
_`regime` (subconcept)_

#### Definitie

📖 Wordt gebruikt wanneer (a) de auditor voldoende bewijs heeft van een afwijking van materieel belang die **wel materieel maar niet diepgaand** is, OF (b) hij voor een specifiek punt niet voldoende geschikt bewijs kon verkrijgen, met mogelijke effecten die wel materieel maar niet diepgaand zijn.

Formulering (ISA 705 par. 7): *‘Naar ons oordeel, behalve voor de gevolgen van de aangelegenheid beschreven in de sectie “Basis voor het oordeel met voorbehoud”, geven de bijgevoegde financiële overzichten een getrouw beeld...’*

Voorbeeld: voorraad ter waarde van X EUR die de auditor niet kon bijwonen bij opname omdat hij later werd aangesteld — wel materieel maar niet de hele jaarrekening verstorend.

<small>📚 ISA 705 (herzien) — par. 7-9 — _norm_</small>

### 📦 Afkeurend oordeel (adverse)  
_`regime` (subconcept)_

#### Definitie

📖 Wordt gebruikt wanneer de auditor voldoende bewijs heeft dat de afwijking **zowel materieel als diepgaand** is — de jaarrekening als geheel is misleidend.

Formulering (ISA 705 par. 8): *‘Naar ons oordeel geven de bijgevoegde financiële overzichten geen getrouw beeld van...’*

Gevolg is dramatisch: AV kan jaarrekening niet goedkeuren zonder ernstig gevolg, banken trekken financiering in, beursnotering kan opgeschort worden, bestuur staat onder druk om te zien wat de kwestie is. Komt zelden voor en is meestal de uitkomst van fundamenteel meningsverschil over waarderingen of consolidatieperimeter waar correctie niet meer mogelijk is.

<small>📚 ISA 705 (herzien) — par. 8 — _norm_</small>

### 📦 Oordeelonthouding (disclaimer)  
_`regime` (subconcept)_

#### Definitie

📖 Wordt gebruikt wanneer de auditor niet voldoende geschikt bewijs kon verkrijgen, met mogelijke effecten die **zowel materieel als diepgaand** zijn — hij kan geen oordeel vormen.

Formulering (ISA 705 par. 9): *‘Vanwege de significantie van de aangelegenheid beschreven in de sectie “Basis voor onthouding van een oordeel”, hebben wij geen oordeel kunnen vormen over de bijgevoegde financiële overzichten.’*

Voorbeelden: management verschaft fundamentele informatie niet, fraude waarvan de omvang niet kwantificeerbaar is, totale chaos in administratie. Geen ‘gemakzucht-optie’: onthouding signaleert massief probleem aan markt. ISA 705 par. 9 vereist dat *zowel* gebrek aan bewijs *als* diepgaande mogelijke effecten samen aanwezig zijn.

<small>📚 ISA 705 (herzien) — par. 9-10 — _norm_</small>

### 📦 Verslag-componenten (vaste structuur)  
_`kader` (subconcept)_

#### Definitie

📖 ISA 700 (herzien) par. 21-49 schrijft een vaste volgorde voor:

1. **Titel** — ‘Verslag van de commissaris’ / ‘Controleverklaring van de onafhankelijke auditor’
2. **Geadresseerde** — aandeelhouders (jaarrekening), governance (review)
3. **Oordeel** — eerst, niet verstopt achteraan
4. **Basis voor het oordeel** — verwijst naar ISA's, onafhankelijkheids-verklaring, voldoende-bewijs-bevestiging
5. **Materiële onzekerheid met betrekking tot continuïteit** (indien van toepassing — ISA 570)
6. **Kernpunten van de controle** (indien van toepassing — ISA 701)
7. **Andere informatie** (ISA 720) — toetsing bestuursverslag
8. **Verantwoordelijkheden van het bestuur** voor de financiële overzichten
9. **Verantwoordelijkheden van de auditor** voor de controle
10. **Andere wettelijke en regelgevende vereisten** (in BE: o.a. bestuurdersverslag, voorgesteld winstbestemming, art. 3:75 §2 WVV-checks)
11. **Naam, kantoor, datum, plaats, handtekening** opdrachtpartner

<small>📚 ISA 700 (herzien) — par. 21-49 — _norm_ · WVV — art. 3:75 §2 (BE-specifieke vereisten commissarisverslag) — _wettekst_</small>

### 📦 Kernpunten van de controle (Key Audit Matters)  
_`instrument` (subconcept)_

#### Definitie

📖 ISA 701 (sinds 2016) verplicht voor controles van **beursgenoteerde entiteiten** (en optioneel voor andere): een aparte sectie waarin de auditor de zaken bespreekt die volgens zijn professionele oordeelsvorming het meest significant waren voor de controle van het lopende boekjaar. Per kernpunt: (a) waarom de aangelegenheid een KAM is; (b) hoe de auditor het in zijn controle heeft behandeld. Doel: meer informatieve verklaring voor stakeholders; minder ‘pass/fail’-signaal en meer inzicht in wat moeilijk was. Veelvoorkomende KAMs: waardering goodwill, fair-value-schatting, going-concern, omzeterkenning (fraude-risico), waardering uitgestelde belastinglatenties.

<small>📚 ISA 701 — Vereisten — _norm_</small>

## Bouwstenen

### 📜 Paragraaf ter benadrukking van een aangelegenheid (Emphasis of Matter)  
_`regel`_

📖 ISA 706 (herzien): wanneer de auditor het belangrijk acht dat gebruikers de aandacht vestigen op een aangelegenheid die **al adequaat in de jaarrekening is toegelicht** — geen aanpassing van het oordeel maar wel een aparte paragraaf na de oordeelssectie. Voorbeelden: significante onzekerheid (going concern als adequaat toegelicht), early adoption van een verslaggevingsstandaard, ramp die de toekomst beïnvloedt. Géén Emphasis of Matter gebruiken om iets te zeggen dat aan een kernpunt of voorbehoud thuishoort.

<small>📚 ISA 706 (herzien) — Vereisten + Bijlage 3 — _norm_</small>

### 📜 Paragraaf inzake overige aangelegenheden (Other Matter)  
_`regel`_

📖 ISA 706 (herzien): voor zaken die *niet* in de jaarrekening toegelicht zijn maar volgens de auditor wel relevant voor gebruikers — typisch over de controle zelf. Voorbeeld: ‘Vergelijkende cijfers werden niet door een auditor onderzocht’ (ISA 710).

<small>📚 ISA 706 (herzien) — _norm_ · ISA 710 — vergelijkende informatie — _norm_</small>

### 📏 ‘Materieel’ vs ‘materieel én diepgaand’ — het kritische onderscheid  
_`drempel`_

📖 **Materieel** = boven materialiteitsdrempel. **Diepgaand** (pervasive) = het probleem is niet beperkt tot specifieke posten maar verstoort het beeld van de jaarrekening als geheel, of zou (indien beperkt tot specifieke posten) een substantieel deel van de jaarrekening uitmaken, of een fundamentele toelichting betreft.

Dit onderscheid is de scharnier tussen oordeel met voorbehoud (materieel maar niet diepgaand) en afkeurend/onthouding (zowel materieel als diepgaand). Examen-tip: bij elke oordeel-keuze: ‘is het probleem afgrensbaar in één hoek van de jaarrekening, of verstoort het het geheel?’

<small>📚 ISA 705 (herzien) — definities + Bijlage — _norm_</small>

## Valkuilen

### ⚠️ ‘Emphasis of Matter’ als compromis voor moeilijk oordeel

**Verkeerde assumptie**: Bij gevoelige zaken voeg je een Emphasis of Matter toe — dat is een diplomatiek compromis tussen schoon en met-voorbehoud-oordeel.

**Kernpunt**: ISA 706 par. 8(b): Emphasis of Matter mag *niet* worden gebruikt om een aangepast oordeel te vermijden. Als er een afwijking van materieel belang is → met-voorbehoud of afkeurend; als er gebrek aan bewijs is → met-voorbehoud of onthouding. Emphasis is voor zaken die wél correct toegelicht zijn maar bijzondere aandacht verdienen.

<small>📚 ISA 706 (herzien) — par. 8 — _norm_</small>

### ⚠️ Going-concern-onzekerheid = altijd voorbehoud

**Verkeerde assumptie**: Als er significant continuïteitstwijfel is, moet de auditor altijd een oordeel met voorbehoud geven.

**Kernpunt**: ISA 570 herzien: als (a) significant twijfel bestaat én (b) jaarrekening adequaat toelicht én (c) going-concern-basis nog passend is → oordeel **zonder voorbehoud** + aparte paragraaf ‘Material uncertainty related to going concern’. Pas als toelichting inadequaat is OF basis niet meer passend, wordt het voorbehoud of afkeurend.

<small>📚 ISA 570 (herzien) — par. 22-24 — _norm_</small>

### ⚠️ KAM beperkt zich tot wat er fout liep

**Verkeerde assumptie**: Kernpunten van de controle zijn de zaken waar de controle ‘op vastliep’ of waar problemen waren.

**Kernpunt**: KAM (ISA 701) zijn niet ‘problemen’ maar de **meest significante aandachtspunten voor de auditor** — vaak zaken waar veel werk in zat (waardering goodwill, fair values) zonder dat er noodzakelijk iets fout was. Het is een transparantie-tool, niet een waarschuwingssectie.

<small>📚 ISA 701 — Doelstellingen — _norm_</small>

## Syntheses

### 🧩 Synthese  
_`beslisboom`_

Welk oordeel? Beslisboom op basis van materialiteit en bewijs.

### 🧩 Synthese  
_`matrix`_

Vergelijking 4 oordelen — wanneer welk oordeel.

## Accountant-perspectieven

### De accountant als opsteller en ondertekenaar van de verklaring

#### 🔍 Auditor

##### 👣 Opbouw verklaring (BE-context)  
_`stap`_

📖 Voor commissaris-verslag (WVV art. 3:75) — twee delen: **Deel I — Verslag over de controle van de jaarrekening** (volgt ISA 700 herzien componenten); **Deel II — Vermeldingen en inlichtingen overeenkomstig art. 3:75 §1 2°-9° WVV** (bestuurdersverslag-toetsing, going-concern, niet-uitkeerbare overgedragen verliezen, sociaal balans, ...). Per discipline: standaardteksten ITAA + ICCI-modellen worden aangepast aan dossier. Datum verklaring ≥ datum bestuursbesluit goedkeuring jaarrekening. Twee originelen ondertekend door opdrachtpartner (één voor cliënt, één voor revisiedossier).

<small>📚 WVV — art. 3:75 — _wettekst_ · ISA 700 (herzien) — _norm_</small>

## Verder lezen (scope-out)

- → Cyclus-context (fase 4 output) → [[controleopdracht]] _(moet-verwijzen)_
- → Afronding als input → [[audit-afronding]] _(moet-verwijzen)_
- → Bijzondere-mandaat-verslagen → [[bijzondere-mandaten]] _(moet-verwijzen)_
- → Verslag-stijl per opdracht-type → [[opdracht-types]] _(moet-verwijzen)_
- → Uitvoerder bij wettelijke controle → [[commissaris]] _(moet-verwijzen)_

## Relaties

### `valt_onder`
- [[controleopdracht]]
### `beinvloed_door`
- [[audit-afronding]]
### `gedocumenteerd_in`
- [[bijzondere-mandaten]]
### `uitgevoerd_door`
- [[commissaris]]
