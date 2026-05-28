---
title: "Gewestelijke belastingverminderingen (PB)"
concept_type: "kader"
schema_version: "2.2"
status: "concept"
categorieen:
  - kader
  - regeling
ankers:
  - 2.2.XII
  - 2.2.XIII
tags:
  - concept
  - schema-2.2
  - type-kader
  - cat-kader
  - cat-regeling
  - status-concept
gegenereerd_uit: "data/concepten/records/gewestelijke-belastingverminderingen-pb.json"
---

# Gewestelijke belastingverminderingen (PB)

_Kader_

🏛️ Kader · 📋 Regeling · Anchors: `2.2.XII` · `2.2.XIII` · Wave: `skeleton-pb-venb-2026-05-28`

> [!info] 📝 **Concept** — content gevuld door cluster-extract; niet door mens-verify gegaan.

**Synoniemen**: gewest-belastingvermindering personenbelasting · réductions d'impôt régionales — **Vertalingen**: fr: réductions d'impôt régionales

## Definitie

📖 Gewestelijke belastingverminderingen zijn voordelen op de berekende personenbelasting die door de Vlaamse, Waalse of Brusselse wetgever zijn opgezet voor de aan dat gewest toegewezen bevoegdheden — voornamelijk woningfiscaliteit, energiebesparing, dienstencheques en specifieke gewestelijke gunstregimes. Sinds de zesde staatshervorming (Bijzondere Financieringswet, gewijzigd 2014) hebben de gewesten een eigen 'gewest-belasting' deel binnen de PB-cascade en bepalen ze autonoom welke bestedingen op dat deel recht geven op vermindering. Het federale WIB92 voorziet de structuur (bv. art. 14538/1 — leeg met 'Tekst: WIB 92 – Historische versie – Vlaams Gewest') en de gewest-decreten vullen de inhoud in.

<small>📚 WIB92 — art. 178/1 — _wettekst_ · WIB92 — art. 14538/1 — _wettekst_ · WIB92 — art. 14536bis — _wettekst_</small>

## Substantie

📖 Economisch effect: de belastingplichtige wordt voor zijn 'gewest-fiscale woonplaats' (= gemeente waar hij op 1 januari AJ gevestigd is) onder het regime van dat gewest gebracht voor de gewestelijke verminderingen. Een belastingplichtige in Antwerpen geniet Vlaamse regelingen (Vlaamse woonbonus voor lopende leningen, isolatie-vermindering); in Luik Waalse (chèque habitat); in Schaarbeek Brusselse. Verhuizing tussen gewesten in de loop van het jaar kan dus fiscaal impact hebben — wel altijd via de peildatum 1 januari AJ. Door art. 178/1 worden eerst de federale verminderingen op de gereduceerde belasting Staat aangerekend en daarna pas op de gewest-PB als saldo. Praktische impact: bij PB-aangifte twee parallelle codereeksen (federaal Vak X + gewestelijk Vak X-gewestelijk).

<small>📚 WIB92 — art. 178/1 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Rationale

🔗 Ratio legis: de gewesten kregen via de Bijzondere Financieringswet de bevoegdheid over fiscale aspecten die nauw verbonden zijn met hun materiële bevoegdheden (huisvesting, energie, sociaal beleid). De fiscale verminderingen vormen het instrument om gewestelijk beleid te ondersteunen zonder dat de basis-PB versplinterd wordt. De aanrekenings-volgorde (federaal eerst, gewestelijk pas voor het saldo) verzekert dat de federale verminderingen voorrang hebben op de schaarse fiscale capaciteit van middeninkomens — pas bij voldoende belasting komen gewestelijke regelingen tot hun volledig effect.

<small>📚 WIB92 — art. 178/1 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Gebruikscontext

**Status**: `in-voege` · sinds **AJ 2015** · basis: Bijzondere Financieringswet 16/01/1989 (gewijzigd door bijzondere wet 6/01/2014) + gewest-decreten

Sinds zesde staatshervorming. Gewesten hebben binnen hun bevoegdheden volledige autonomie inzake belastingverminderingen voor PB-rijksinwoners van het gewest. De woonbonus is in alle gewesten uitgedoofd voor nieuwe leningen (Vlaams Gewest 1/1/2020; Waals chèque habitat sinds 2016; Brussels woonbonus afgeschaft 1/1/2017).

**✅ Voor**
- 📖 Belastingplichtigen die op 1 januari AJ rijksinwoner zijn van het Vlaams, Waals of Brussels Gewest en die in het belastbaar tijdperk uitgaven hebben gedaan die door het gewest van hun fiscale woonplaats erkend zijn voor vermindering (woningfiscaliteit, energie, dienstencheques, specifieke domeinen).

**📋 Voorwaarden**
- 🔗 Cumulatief: (1) fiscale woonplaats in het gewest op 1 januari AJ; (2) werkelijke betaling van een in dat gewest erkende uitgave in het belastbaar tijdperk; (3) bewijsstuk (fiscaal attest of energie-attest of uittreksel gewest-erkende dienstenleverancier); (4) plafond per regeling; (5) anti-cumulatie met federale of andere gewest-regelingen vermijden.

**👍 Voordeel**
- 🔗 Naast federale verminderingen krijgen de inwoners van een gewest extra fiscale tegemoetkomingen voor gewest-prioritaire investeringen — vooral woningverwerving (woonbonus-overgang, chèque habitat), energiebesparing, en dienstencheques. Effect afhankelijk van gewest: een Vlaams overgangsdossier met grote woonbonus kan ettelijke duizenden EUR/jaar opleveren over de duur van de lening.

**⚠️ Risico**
- 🔗 Verkeerde gewest-toewijzing bij verhuizing tussen gewesten: peildatum is 1 januari AJ — verhuis naar ander gewest vóór 1 januari betekent volledige overgang naar regime nieuw gewest voor dat inkomstenjaar, ook voor lopende lening-verminderingen (die mogelijk minder voordelig zijn in nieuw gewest). · Federale en gewestelijke verminderingen op dezelfde uitgave laten cumuleren (bv. dakisolatie federaal + gewest = niet toegelaten). · Gewest-aangifte-codes verwarren met federale codes.

## Bouwstenen

### ⚙️ Aanrekenings-volgorde (art. 178/1 WIB92)  
_`mechanisme`_

📖 Federale belastingverminderingen (art. 1451-14516, 14526, 14527, 14533, 14535, 154bis) worden EERST aangerekend op de 'gereduceerde belasting Staat' met betrekking tot de art. 130-belaste inkomsten. Verminderingen die niet volledig kunnen worden aangerekend, gaan vervolgens naar de gewestelijke PB. Volgorde binnen verminderingen: (1) niet-omzetbaar in krediet en geen latere heffing; (2) niet-omzetbaar in krediet maar wél latere heffing; (3) omzetbaar in belastingkrediet. Doelstelling: voorkomen van fiscale capaciteit-verlies bij middeninkomens met meerdere parallel-regelingen.

<small>📚 WIB92 — art. 178/1 — _wettekst_</small>

### 📜 Vlaams Gewest — hoofdregelingen  
_`regel`_

📖 Voornaamste Vlaamse PB-verminderingen: (1) Geïntegreerde woonbonus (art. 14538/1 — Vlaamse versie): uitgedoofd voor leningen aangegaan vanaf 1/1/2020; overgangsregime voor lopende leningen (basis-vermindering 30%, plafond 2.280 EUR + verhoging eerste 10 jaar + per kind ten laste op moment lening). (2) Winwinlening / Vriendenaandeel: vermindering 2,5% × jaarbedrag van de lening, max bedragen per persoon (per gewestelijk decreet); 30% éénmalige vermindering bij faillissement-verlies. (3) Energiebesparende investeringen: dakisolatie (uitgefaseerd), warmtepomp, zonneboiler — gewestelijke premie + fiscale impact. (4) Dienstencheques: gewest-vermindering bovenop federaal residu (Vlaamse plafond per gezin per jaar). Concrete tarieven en plafonds: VCF + Vlaamse PB-Codex per AJ.

<small>📚 WIB92 — art. 14538/1 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### 📜 Waals Gewest — hoofdregelingen  
_`regel`_

🔗 Voornaamste Waalse PB-verminderingen: (1) Chèque habitat (sinds 2016): vervangt de woonbonus voor leningen aangegaan vanaf 1/1/2016. Forfaitair voordeel per jaar (gemiddeld 1.520 EUR de eerste 10 jaar, daarna degressief), gekoppeld aan inkomen + gezinslast; geldig 20 jaar. Niet cumuleerbaar met de oude woonbonus. (2) Dienstencheques (titres-services): gewest-vermindering op aankoop van cheques, plafond per gezin per jaar. (3) Energiebesparende investeringen: warmtepompen, energie-renovatie. (4) Vlaamse winwinlening-equivalent in Wallonië: 'Coup de Pouce' (lening tussen particulieren). Wettelijke basis: Décret du 06/05/1999 + opvolgende decreten Waalse fiscaliteit.

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### 📜 Brussels Hoofdstedelijk Gewest — hoofdregelingen  
_`regel`_

🔗 Voornaamste Brusselse PB-verminderingen: (1) Woonbonus volledig afgeschaft voor leningen vanaf 1/1/2017 — overgangsregime alleen voor oude leningen. Vervangen door overdrachtbelasting-vermindering (regio-belasting, niet PB). (2) Dienstencheques (titres-services): Brusselse gewest-vermindering bovenop federaal niveau (afnemend door reformes 2020+). (3) Energiebesparende investeringen via art. 14536bis. (4) Specifieke renovatie-stimuli (Renolution) en isolatie-premies (vooral via gewest-premie + gewest-vermindering combinatie).

<small>📚 WIB92 — art. 14536bis — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### 📜 Peildatum fiscale woonplaats (1 januari AJ)  
_`regel`_

🔗 Voor bepaling van het toepasselijke gewest-fiscaal regime telt de fiscale woonplaats op 1 januari van het aanslagjaar (= 1 januari ná het inkomstenjaar). Een belastingplichtige die op 15 december van inkomstenjaar N van Vlaanderen naar Wallonië verhuist: voor inkomstenjaar N (= AJ N+1) wordt het Waalse regime toegepast — ondanks dat 11,5 maanden uit het jaar in Vlaanderen werden gepresteerd. Praktisch gevolg: bij verhuizing vóór 1 januari moet de Vlaamse woonbonus-vermindering NIET meer worden geclaimd (lening valt onder Waals regime — chèque habitat in plaats van basisuitwerking).

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28) · Bijzondere Financieringswet 16/01/1989 — art. 5/1 — _wettekst_</small>

## Voorbeelden

### 💡 Vlaamse geïntegreerde woonbonus — overgangsregime lopende lening uit 2018 🔗

_Echtpaar A+B woont in Antwerpen (Vlaams Gewest), heeft op 1/3/2018 een hypothecaire lening van 200.000 EUR afgesloten voor enige eigen woning. Op 1 januari AJ 2025 zijn ze beide rijksinwoner van het Vlaams Gewest. 2 kinderen ten laste op moment lening aangegaan. Jaarlijkse kapitaalaflossingen + intresten: 11.500 EUR._

**Berekening:**
- Stap 1 — gewest-aanwijzing op 1/1 AJ 2025: Vlaams Gewest ✓.
- Stap 2 — lening aangegaan op 1/3/2018 < 1/1/2020 → onder overgangsregime Vlaamse geïntegreerde woonbonus.
- Stap 3 — basisbedrag in aanmerking (per echtgenoot): 2.280 EUR (niet-geïndexeerd). Voor jaar 7 van de lening (2024): basis + verhoging eerste 10 jaar +760 EUR + verhoging 2 kinderen op moment lening +80 EUR = 3.120 EUR per echtgenoot (niet-geïndexeerd).
- Stap 4 — totaal beide echtgenoten: 2 × 3.120 = 6.240 EUR. Hun jaarlijkse aflossingen + intresten van 11.500 EUR overschrijden plafond → enkel 6.240 EUR in aanmerking.
- Stap 5 — tarief vermindering: 30% (overgangsregime).
- Stap 6 — totale gewest-vermindering: 6.240 × 30% = 1.872 EUR.
- Stap 7 — die 1.872 EUR komt in mindering op het gewest-deel van de PB (art. 178/1, lid 2 — na federale verminderingen).

→ **Resultaat**: Vlaamse woonbonus levert dit gezin in AJ 2025 ca. 1.872 EUR PB-besparing (niet-geïndexeerd). Volledig opgebruikt aan beide echtgenoten — anders worden niet-benutte saldi niet overdraagbaar. Bij verhuizing naar Brussel of Wallonië vóór 1/1 zou het regime wijzigen.

<small>📚 WIB92 — art. 14538/1 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### 💡 Waalse chèque habitat — lening 2019 🔗

_Belastingplichtige C woont in Namen (Waals Gewest), heeft op 15/9/2019 een hypothecaire lening van 180.000 EUR aangegaan voor enige eigen woning. Belastbaar inkomen 2024 = 35.000 EUR. Gehuwd, 1 kind ten laste._

**Berekening:**
- Stap 1 — gewest-aanwijzing op 1/1 AJ 2025: Waals Gewest ✓.
- Stap 2 — lening 15/9/2019 → onder Waals chèque-habitat-regime.
- Stap 3 — chèque-bedrag is forfaitair op basis van inkomen + gezinslast (niet op werkelijke aflossingen): basis ca. 1.520 EUR + verhoging per kind ten laste ca. 125 EUR = 1.645 EUR voor jaren 1-10.
- Stap 4 — voor jaar 6 van de lening (2024) = nog volle bedrag; vanaf jaar 11 degressief.
- Stap 5 — totale chèque-vermindering AJ 2025: 1.645 EUR (op gewest-PB).
- Stap 6 — looptijd: 20 jaar — eerste 10 jaar vol, dan degressief naar 0.

→ **Resultaat**: De Waalse chèque habitat geeft een forfaitair voordeel van ~1.645 EUR/jaar over 10 vol-jaar + 10 degressieve jaren. Voor lagere inkomens kan het systeem voordeliger zijn dan de oude woonbonus; voor hoge inkomens minder.

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### 💡 Aanrekenings-volgorde art. 178/1 — federaal eerst 📖

_Belastingplichtige D, inwoner Vlaams Gewest, heeft federale vermindering pensioensparen 297 EUR + gewest-vermindering woonbonus-overgang 1.872 EUR. Gereduceerde belasting Staat (art. 130-deel) = 1.000 EUR, gewest-PB = 5.000 EUR._

**Berekening:**
- Stap 1 — federale vermindering pensioensparen 297 EUR wordt EERST aangerekend op gereduceerde belasting Staat 1.000 EUR. Resterend federaal: 1.000 − 297 = 703 EUR.
- Stap 2 — saldo aanrekening federale verminderingen op gewest-PB: 297 was volledig aanrekenbaar federaal → geen overschot, alles op federaal niveau.
- Stap 3 — gewest-vermindering woonbonus 1.872 EUR wordt aangerekend op gewest-PB 5.000 EUR. Resterend gewest: 5.000 − 1.872 = 3.128 EUR.
- Stap 4 — totaal PB na verminderingen: 703 (federaal) + 3.128 (gewest) = 3.831 EUR.
- Stap 5 — vervolgens wordt aanvullende gemeentebelasting (typisch 7%) berekend op deze 3.831 EUR.
- Stap 6 — alternative scenario: stel federale vermindering was 1.500 EUR > federale belasting 1.000 EUR. Surplus van 500 EUR zou dan worden aangerekend op gewest-PB (art. 178/1, §1, lid 2).

→ **Resultaat**: De aanrekenings-volgorde van art. 178/1 verzekert dat federale verminderingen voorrang krijgen op federale belasting; pas bij surplus gaan ze naar gewest-deel. Gewestelijke verminderingen blijven exclusief op gewest-PB.

<small>📚 WIB92 — art. 178/1 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Valkuilen

### ⚠️ Vergeten dat woonbonus is uitgedoofd voor nieuwe leningen

**Verkeerde assumptie**: Een lening voor eigen woning aangegaan in 2024 geeft nog Vlaamse woonbonus.

**Kernpunt**: Vlaamse geïntegreerde woonbonus is uitgedoofd voor leningen aangegaan vanaf 1/1/2020. Brussel: vanaf 1/1/2017. Wallonië: vervangen door chèque habitat sinds 1/1/2016. Voor nieuwe leningen vanaf die data: geen woonbonus meer — alleen overgangsregime voor lopende dossiers. Praktisch: nieuwe huizenkopers in Vlaanderen krijgen geen fiscaal voordeel meer voor de hypotheek zelf; in Wallonië wel chèque habitat; in Brussel niets PB-zijde (compensatie deels via lager registratierecht).

<small>📚 WIB92 — art. 14538/1 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### ⚠️ Verkeerde gewest-toewijzing bij verhuizing einde december

**Verkeerde assumptie**: Wie 11 maanden in Vlaanderen woonde en in december naar Brussel verhuist, valt voor dat inkomstenjaar nog onder Vlaams regime.

**Kernpunt**: Peildatum is 1 januari van het AANSLAGJAAR. Wie op 15/12/2024 naar Brussel verhuist: op 1/1/2025 is hij rijksinwoner Brussels Gewest → voor inkomstenjaar 2024 (AJ 2025) gelden de BRUSSELSE gewest-verminderingen, niet de Vlaamse. Vlaamse woonbonus van zijn lening kan dus NIET meer worden geclaimd voor AJ 2025; mogelijk geen Brusselse equivalent.

<small>📚 Bijzondere Financieringswet — art. 5/1 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### ⚠️ Federale en gewestelijke verminderingen voor zelfde uitgave cumuleren

**Verkeerde assumptie**: Dakisolatie-uitgave kan zowel federaal (art. 14542) als gewestelijk (Vlaamse regeling) afgetrokken worden.

**Kernpunt**: Anti-cumulatie: voor dezelfde uitgave kan slechts één vermindering worden geclaimd. Bij energiebesparende investeringen: gewest heeft prioriteit (federale uitfasering sinds 2014). Voor sommige uitgaven federaal residu nog beperkt mogelijk — Cijferzakboekje + gewest-FAQ per AJ raadplegen.

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Syntheses

### 🧩 Synthese  
_`matrix`_

Overzichtsmatrix gewestelijke woonbonus + chèque habitat (status en hoofdkenmerken)

## Accountant-perspectieven

### Particuliere cliënt (PB-aangifte gewest)

_De accountant die de PB-aangifte voorbereidt en gewest-specifieke verminderingen correct in kaart brengt._

#### 💰 Fiscaal adviseur

##### 👣 Gewest-toewijzing controleren  
_`stap`_

🔗 Bij elke aangifte: (1) gemeente op 1/1 AJ uit gemeente-attest verifiëren; (2) gewest-aanwijzing checken — Vlaams (incl. faciliteitengemeenten), Brussels (19 gemeenten), Waals; (3) voor klant die in loop van jaar verhuisde: NIEUWE gewest-regime toepassen voor AJ; (4) gewest-specifieke codereeksen invullen in PB-aangifte (Vlaams Vak X-gewestelijk; Waals attest 'logement'; Brussels eigen rubrieken); (5) federale + gewest-attesten apart bewaren (zelfde fysieke attest kan voor beide nodig zijn — bv. isolatie-werkmensen geven aan twee soorten attesten).

<small>📚 WIB92 — art. 178/1 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

#### 🧭 Adviseur

##### 🧭 Advies bij geplande gewest-grensoverschrijdende verhuizing  
_`vuistregel`_

🔗 Cliënt overweegt verhuizing van Vlaanderen naar Brussel of Wallonië (of vice versa). Concrete impact op fiscale planning: (1) verlies/winst van woonbonus-overgang voor lopende lening; (2) verschillende dienstencheques-plafonds per gewest; (3) verschillende energie-vermindering-regimes. ALTIJD per concrete situatie doorrekenen — verhuizen vóór 1 januari heeft volle impact voor het volledige inkomstenjaar; vermijd verhuizing eind december als de oude regime gunstiger is en de verhuizing administratief uitgesteld kan worden tot januari.

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Verder lezen (scope-out)

- → Federale belastingverminderingen (pensioensparen, langetermijnsparen, giften) → [[federale-belastingverminderingen-pb]] _(moet-verwijzen)_
- → Belastingberekening-procedure (volgorde in cascade) → [[belastingberekening-pb]] _(moet-verwijzen)_
- → Aftrekbare bestedingen (eerdere stap = aftrek inkomen) → [[aftrekbare-bestedingen-pb]] _(moet-verwijzen)_
- ↪ Aanvullende gemeentebelasting (volgt op saldo na gewestelijke verminderingen) → [[aanvullende-gemeentebelasting-pb]] _(mag-verwijzen)_
- ↪ Gewest-specifieke detailregelingen (woonbonus per gewest, chèque habitat) — eigen records aan te maken _(mag-verwijzen)_

## Relaties

### `valt_onder`
- [[personenbelasting]]
### `vergelijkbaar_met`
- [[federale-belastingverminderingen-pb]]
    - **Gelijkenissen**:
        - Beide werken op de berekende belasting (niet op grondslag)
        - Beide hanteren vast percentage of forfait
        - Beide vereisen werkelijke betaling + bewijsstuk
    - **Verschillen**:
        - Federaal: pensioensparen, langetermijnsparen, giften, monumentenzorg
        - Gewestelijk: woonfiscaliteit, energiebesparing, dienstencheques (gewest-deel)
        - Aanrekenings-volgorde art. 178/1: federaal eerst op gereduceerde belasting Staat, gewest pas op gewest-PB
        - Federaal uniform; gewest verschilt per Vlaanderen/Wallonië/Brussel
    - ⚠️ **Verwarringsrisico**: Studenten verwarren systematisch federaal en gewestelijk; let op aangifte-codes en peildatum 1 januari AJ.
### `triggert`
- [[belastingberekening-pb]] — Gewestelijke verminderingen komen na de federale verminderingen in de cascade (art. 178/1).
### `beinvloed_door`
- [[gezinssituatie]] — Gewest-toewijzing op 1/1 AJ wordt bepaald door de fiscale woonplaats, die afhankelijk is van gezinssituatie (gehuwden hebben gemeenschappelijke fiscale woonplaats).
