---
title: Bepalen of een onderneming IFRS moet of mag toepassen in België
tags:
- competentie
- po-1-5
programmaonderdelen:
- '1.5'
status: voorgesteld
schema_version: '1.5'
gegenereerd_uit: data/concepten/records/bepalen-toepasselijkheid-ifrs-belgie.json
gegenereerd_op: '2026-05-18'
---
# Bepalen of een onderneming IFRS moet of mag toepassen in België

**⚖️ 90% · 🤖 10%**

> De verplichte gevallen volgen rechtstreeks uit Verordening (EG) 1606/2002 art. 4 (beursgenoteerde geconsolideerde rekeningen) en sectorale regels (kredietinstellingen, verzekeraars). Vrijwillige IFRS-toepassing op statutair niveau is in België in beginsel niet toegestaan — alleen via uitzondering. Het praktijk-aandeel zit in het inschatten van de strategische gevolgen (toelichting, externe rapportering, vergelijkbaarheid).

## Aanbevolen werkwijze

### 1. Identificeer het rapporteringsniveau

Stel vast of de vraag gaat over de statutaire (enkelvoudige) jaarrekening of over de geconsolideerde jaarrekening van de onderneming.

**Waarom?** Het Europese en Belgische kader behandelt beide niveaus verschillend: IFRS-verplichting geldt onder Verordening 1606/2002 voor geconsolideerde rekeningen van beursgenoteerden, niet voor statutaire.

**📥 Input**:
- Vennootschapsdocumenten → **Vraag van de cliënt — over welke jaarrekening?** _(document)_

**📤 Output**:
- Werkpapier IFRS-toepasselijkheid → **Niveau (statutair / geconsolideerd)** _(conclusie)_

**🛠️ Hoe**:

1. Vraag bij Zelena Bio NV expliciet op: betreft het de jaarrekening van Zelena alléén of de geconsolideerde jaarrekening van de Zelena-groep (Zelena Bio NV + dochters)?
2. Noteer 'statutaire' of 'geconsolideerde' rapportering — dit stuurt de hele verdere beslisboom.
3. Bij twijfel: vraag of de cliënt een raadpleegbare set aandeelhouders heeft en of er dochters zijn — alleen dan kan geconsolideerd relevant zijn.


**Grondslag**: [[ifrs-verordening-1606-2002]] §toepassingsgebied

### 2. Toets of de onderneming beursgenoteerd is op een gereglementeerde EU-markt

Verifieer of de aandelen of obligaties van de onderneming op een gereglementeerde markt binnen de Europese Unie (Euronext Brussel, andere lidstaten) worden verhandeld op balansdatum.

**Waarom?** Verordening (EG) 1606/2002 art. 4 verplicht alle beursgenoteerde EU-vennootschappen om hun geconsolideerde jaarrekening volgens IFRS op te stellen — rechtstreeks van toepassing zonder nationale omzetting.

**📥 Input**:
- Statuten + aandelenregister → **Notering aandelen of obligaties** _(document)_
- FSMA-register → **Notering op gereglementeerde markt** _(document)_

**📤 Output**:
- Werkpapier IFRS-toepasselijkheid → **Beursgenoteerd ja/nee + welke markt** _(conclusie)_

**🛠️ Hoe**:

1. Open de FSMA-website of EBA-register en zoek op de naam Zelena Bio NV.
2. Verifieer of effecten genoteerd zijn op Euronext Brussel of een andere gereglementeerde EU-markt.
3. Belangrijk: 'gereglementeerde markt' is enger dan 'beurs' — MTF's zoals Euronext Growth tellen NIET voor de Verordening.
4. Bij Zelena Bio: noteer 'Beursgenoteerd op Euronext Brussel (gereglementeerde markt EU) sinds 2022'.


**Grondslag**: [[ifrs-verordening-1606-2002]] §artikel-4, Verordening (EG) 1606/2002 art. 4

### 3. Pas de beslisboom toe en formuleer conclusie

Combineer rapporteringsniveau (stap 1) + notering (stap 2) + sectorale status om vast te stellen of IFRS verplicht, toegestaan of verboden is.

**Waarom?** De combinatie van factoren bepaalt het regime; één enkele factor volstaat zelden voor een sluitende conclusie.

**📥 Input**:
- Werkpapier uit stappen 1 + 2 → **Niveau, notering, sector** _(conclusie)_

**📤 Output**:
- Advies-nota aan cliënt → **Toepasselijk referentiestelsel** _(conclusie)_

**🛠️ Hoe**:

1. Pas de beslisboom uit [[be-gaap-vs-ifrs-overzicht]] §beslisboom toe.
2. Geconsolideerd + beursgenoteerd EU = IFRS **verplicht** (Verordening art. 4).
3. Geconsolideerd + kredietinstelling/verzekeraar = IFRS **verplicht** (sectorregelgeving — KB).
4. Geconsolideerd + niet-beursgenoteerd, niet-financieel = Belgisch GAAP (KB WVV consolidatie) standaard; IFRS niet toegestaan op statutair maar wel op geconsolideerd indien vrijwillige keuze toegestaan door bestuur.
5. Statutair (enkelvoudig) = Belgisch GAAP (KB WVV) **verplicht** — IFRS niet toegestaan tenzij specifieke uitzondering.
6. Voor Zelena Bio NV (beursgenoteerd Euronext Brussel, geconsolideerd): conclusie = **IFRS verplicht voor geconsolideerd; Belgisch GAAP verplicht voor statutair**.


> [!example]- Voorbeeld: Cliënt Zelena Bio NV (beursgenoteerd Euronext Brussel, omzet € 250M, 3 dochters) vraagt of de groepscijfers in 2026 in I…
> Cliënt Zelena Bio NV (beursgenoteerd Euronext Brussel, omzet € 250M, 3 dochters) vraagt of de groepscijfers in 2026 in IFRS moeten worden gepresenteerd.
>
> 1. **Beslismatrix** 💬
>
>    | Vraag                                       | Antwoord                           |
>    |---------------------------------------------|------------------------------------|
>    | Geconsolideerd of statutair?                | Geconsolideerd                     |
>    | Beursgenoteerd op gereglementeerde EU-markt?| Ja (Euronext Brussel)              |
>    | Kredietinstelling/verzekeraar?              | Nee                                |
>    | → Toepasselijk stelsel?                     | **IFRS verplicht** — Verord. art. 4|
>    
>
> 2. **Conclusie voor stagiair** 💬
>
>    Zelena Bio NV moet de geconsolideerde jaarrekening 2026 volgens IFRS opstellen. Voor de statutaire jaarrekening van Zelena Bio NV blijft het Belgisch boekhoudrecht (KB WVV) van toepassing. Bij eerste IFRS-toepassing geldt [[ifrs-eerste-toepassing]] (zie aparte competentie [[uitvoeren-eerste-toepassing-ifrs]]).
>    
>

**Grondslag**: [[ifrs-toepassingsgebied-belgie]] §beslisboom, [[be-gaap-vs-ifrs-overzicht]] §beslisboom

> [!warning]- Toets expliciet of de markt 'gereglementeerd' is in de zin van MiFID — niet elke verhandelingsmarkt valt onder Verordening 1606/2002.
>
> _Vaak fout gedaan_: Aannemen dat elke notering op een handelsplatform IFRS-verplichting triggert. Multilateral Trading Facilities (MTF's) zoals Euronext Growth zijn geen gereglementeerde markt.
>
> _Grondslag_: [[ifrs-verordening-1606-2002]] §toepassingsgebied

> [!warning]- Hou statutair (enkelvoudig) en geconsolideerd strikt gescheiden bij IFRS-vraagstukken.
>
> _Vaak fout gedaan_: Concluderen dat een beursgenoteerde Belgische NV haar statutaire jaarrekening in IFRS opmaakt — dat blijft KB WVV-Belgisch GAAP.
>
> _Grondslag_: [[ifrs-toepassingsgebied-belgie]] §statutair-niveau


## Voorbeelden

> [!example]- Meubelzaak Mertens BV (niet-beursgenoteerd, kleine groep met 1 dochter, omzet € 8M) overweegt vrijwillig IFRS toe te pas…
> **Conclusie**: IFRS-toepassing op geconsolideerd niveau is niet uitdrukkelijk verboden voor niet-beursgenoteerde groepen, maar in België ongebruikelijk en niet als verplichting opgelegd. De geconsolideerde jaarrekening volgens Belgisch GAAP (KB WVV consolidatie) blijft het wettelijk vereiste; vrijwillige IFRS-rapportering kan parallel gebeuren als aanvullende informatie aan de stakeholders. Statutair blijft Belgisch GAAP verplicht.
>
> **Grondslag**: [[ifrs-toepassingsgebied-belgie]] §vrijwillige-keuze; [[ifrs-verordening-1606-2002]] §lidstaat-opties
>
> **Redenering**: Verordening 1606/2002 art. 5 laat lidstaten toe om IFRS toe te staan of te verplichten voor niet-beursgenoteerde groepen of voor statutaire jaarrekeningen. België heeft op statutair niveau Belgisch GAAP behouden en stelt vrijwillige IFRS-rapportering parallel toe maar niet ter vervanging van de KB WVV-verplichting.


## Gebaseerd op concepten

[[ifrs-verordening-1606-2002]] · [[ifrs-toepassingsgebied-belgie]] · [[richtlijn-2013-34-eu]] · [[be-gaap-vs-ifrs-overzicht]]
## Voortkomend uit

- **Taken**: 1.5.taak.1
- **Kenniselementen**: 1.5.II, 1.5.III, 1.5.I
