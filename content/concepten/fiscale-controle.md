---
title: "Fiscale controle"
concept_type: "procedure"
schema_version: "2.2"
status: "concept"
categorieen:
  - gebeurtenis
ankers:
  - 2.5.II
  - 2.5.III
tags:
  - concept
  - schema-2.2
  - type-procedure
  - cat-gebeurtenis
  - status-concept
gegenereerd_uit: "data/concepten/records/fiscale-controle.json"
---

_Procedure_ · ook: controle door de fiscus · fiscaal onderzoek

## Definitie

Fiscale controle is het onderzoek waarmee de fiscale administratie nagaat of de aangifte juist en volledig is. De controle gebeurt op grond van uitgebreide onderzoeksbevoegdheden in WIB92 art. 315-326: inzage in boekhouding (art. 315), vraag om inlichtingen aan belastingplichtige (art. 316) en derden (art. 322), controle ter plaatse (art. 319), en — onder voorwaarden — opvraging van bankgegevens (art. 322bis). De controle resulteert in aanvaarding van de aangifte, een bericht van wijziging, of een proces-verbaal bij fraude.

<small>📖 WIB92 — art. 315-326 — _wettekst_</small>

## Substantie

Soorten controles in de praktijk: (1) bureel-onderzoek (administratieve check op codes en plausibiliteit, vanuit het kantoor van de fiscus); (2) doelgerichte controle ter plaatse (boekenonderzoek bij de cliënt); (3) BBI-onderzoek (Bijzondere Belastinginspectie — voor fraude en grote dossiers); (4) zoeking (huiszoeking — alleen onder gerechtelijke machtiging). Voor de accountant is het cruciaal te weten welk type loopt: het bepaalt de toonzetting, de termijnen en de risico's.

<small>🔗 WIB92 — art. 315-323 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Rationale

De onderzoeksbevoegdheden van de fiscus zijn ruim — dat is nodig om het zelf-aangifte-systeem te laten werken (de fiscus kan niet alles vooraf zien, maar moet achteraf kunnen verifiëren). Tegenover die ruime bevoegdheid staan waarborgen: het bankgeheim (art. 322), de meldingsplicht bij doorbreking ervan, het verbod op fishing expeditions, en de proportionaliteit (beginsel van behoorlijk bestuur).

<small>🔗 WIB92 — art. 322 + art. 333 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Gebruikscontext

**Status**: `in-voege` · basis: WIB92 art. 315-333

**▶️ Trigger start**
- 📖 Brief van de fiscus met aankondiging van een controle, een vraag om inlichtingen, of een bericht dat boekhouding wordt opgevraagd. Bij BBI: bezoek van controleurs zonder voorafgaande aankondiging is wettelijk mogelijk (art. 319).

## Bouwstenen

### ⚙️ Vraag om inlichtingen (art. 316 WIB92)

Schriftelijke vraag van de fiscus aan de belastingplichtige (of via art. 322 aan derden). Antwoordtermijn: 1 maand (verlengbaar mits motivering). Antwoord moet schriftelijk + waarheidsgetrouw. Niet of foutief antwoorden → ambtshalve aanslag (art. 351) + administratieve boete (art. 445).

<small>📖 WIB92 — art. 316 — _wettekst_</small>

### ⚙️ Controle ter plaatse (art. 319 WIB92)

De fiscus heeft het recht om tijdens de openingsuren (of normale werkuren) zonder voorafgaande verwittiging beroepslokalen, kantoren, fabrieken en magazijnen te bezoeken om boekhouding en stukken te onderzoeken. NIET voor privéwoningen — daarvoor is gerechtelijke machtiging nodig (zoeking, art. 319 lid 2). De belastingplichtige moet meewerken; weigering = sanctie.

<small>📖 WIB92 — art. 319 — _wettekst_</small>

### ✴️ Bankgeheim (art. 322 WIB92)

Banken hoeven in beginsel geen klantengegevens vrij te geven aan de fiscus. Doorbreking is mogelijk: (1) bij vermoeden van fraude (concrete elementen, motivering), (2) bij ambtshalve aanslag, of (3) bij buitenlandse aanvragen via inlichtingenuitwisseling. De controleur moet vooraf een 'doorbreking bankgeheim' aanvragen en motiveren. Bankrekeningen worden centraal geregistreerd in het Centraal Aanspreekpunt (CAP) bij de NBB.

<small>📖 WIB92 — art. 322 + art. 322bis — _wettekst_</small>

### 📏 Onderzoekstermijn (art. 333)

Standaard 3 jaar vanaf 1 januari van het aanslagjaar; 6 jaar bij grensoverschrijdende dossiers; 10 jaar bij fraude (met voorafgaande kennisgeving aan de belastingplichtige). Buiten deze termijn mag de fiscus geen onderzoek meer doen — eventuele onderzoeksdaden buiten termijn zijn nietig.

<small>📖 WIB92 — art. 333 — _wettekst_</small>

### 📜 Rechten van de belastingplichtige

(1) Recht op bijstand door een accountant of advocaat tijdens controle; (2) recht op stilzwijgen voor strafbare feiten (nemo tenetur — art. 6 EVRM); (3) recht op gemotiveerde controle (geen 'fishing expedition'); (4) recht op afschrift van proces-verbaal; (5) recht om kopie te houden van overhandigde stukken.

<small>🔗 EVRM — art. 6 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Valkuilen

> [!warning]- Géén privéwoning zonder gerechtelijke machtiging
> **Verkeerde assumptie**: De fiscus kan zomaar bij u thuis binnenkomen om boekhouding op te vragen.
>
> **Kernpunt**: Art. 319 WIB92 laat alleen beroepslokalen toe. Voor privéwoningen is een huiszoekingsbevel van een onderzoeksrechter nodig. Vraag bij twijfel naar het bevel — een controle zonder bevel in privéruimte is onwettig.
>
> <small>📖 WIB92 — art. 319 — _wettekst_</small>

> [!warning]- Vraag om inlichtingen ≠ vrijblijvend
> **Verkeerde assumptie**: Een vraag om inlichtingen kun je negeren of laat beantwoorden, want het is 'maar een vraag'.
>
> **Kernpunt**: Niet of laattijdig antwoorden leidt tot ambtshalve aanslag (omkering bewijslast!) + administratieve boete. Behandel elke vraag om inlichtingen als een dwingende termijn van 1 maand.
>
> <small>📖 WIB92 — art. 316 + art. 351 — _wettekst_</small>

> [!warning]- Buiten onderzoekstermijn = nietig
> **Verkeerde assumptie**: Als de fiscus toch nog vraagt na 3 jaar, moet je toch antwoorden.
>
> **Kernpunt**: Onderzoeksdaden buiten de termijn van art. 333 zijn in beginsel nietig. Vraag naar de juridische grond (welk aanslagjaar? welke verlenging?). Bij onbevoegd onderzoek: weiger gemotiveerd via aangetekend antwoord.
>
> <small>🔗 WIB92 — art. 333 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Accountant-perspectieven

### Cliënt vertegenwoordigen bij fiscale controle

#### 💰 Fiscaal adviseur

##### 👣 Voorbereiding controle

Bij ontvangst aankondiging: dossier nakijken, mogelijke pijnpunten in kaart brengen (autokostenaftrek, gemengd privé, kostenforfaits, ...). Briefing met cliënt over wat er besproken wordt en wat NIET (alleen feiten, geen toegevingen vooraf).

<small>🔗 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

##### 👣 Tijdens de controle

Aanwezig zijn (recht op bijstand). Vragen formuleren waar ze toe leiden; geen documenten meegeven zonder kopie te houden; geen mondelinge toegevingen doen — alles schriftelijk. Notuleren wat gevraagd en gezegd wordt. Bij twijfel over een vraag: vraag tijd om schriftelijk te antwoorden (1 maand).

<small>🔗 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

##### 👣 Na de controle

Slotbespreking aandachtig volgen; vraag om afschrift van het proces-verbaal of een schriftelijke samenvatting. Bij voorgenomen rechtzetting: bericht van wijziging verwachten — bereid de respons voor (1 maand antwoordtermijn).

<small>📖 WIB92 — art. 346 — _wettekst_</small>

## Verder lezen (scope-out)

- → Bewijsmiddelen detail → [[fiscale-bewijsmiddelen]] _(moet-verwijzen)_
- → Bezwaar na controle-uitkomst → [[bezwaarprocedure]] _(moet-verwijzen)_
- ↪ Gewestelijke controle → [[gewestelijke-fiscale-procedure]] _(mag-verwijzen)_

## Relaties

### `valt_onder`
- [[fiscale-procedure]]
### `triggert`
- [[taxatieprocedure]]
### `vereist`
- [[fiscale-bewijsmiddelen]]
