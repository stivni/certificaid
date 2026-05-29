---
title: "Stopzetting BTW"
concept_type: "procedure"
schema_version: "2.2"
status: "concept"
categorieen:
  - gebeurtenis
  - regeling
ankers:
  - 2.4.II
  - 2.4.taak.1
tags:
  - concept
  - schema-2.2
  - type-procedure
  - cat-gebeurtenis
  - cat-regeling
  - status-concept
gegenereerd_uit: "data/concepten/records/stopzetting-btw.json"
---

_Procedure_ · ook: beëindiging btw-activiteit · 604C-procedure · deregistratie btw

## Definitie

Stopzetting BTW is de procedure waarbij een belastingplichtige zijn btw-activiteit beëindigt en zijn btw-identificatie laat doorhalen via de 604C-aangifte (binnen één maand na effectieve stopzetting, art. 53 §1 1° W.BTW). De procedure omvat drie luiken: (1) eindafrekening van lopende btw-positie (laatste aangifte met openstaande verschuldigde btw en aftrekken); (2) onttrekking van overblijvende activa — voorraad waarvoor recht op aftrek bestond wordt belastbaar onder art. 12 §1 5° (gelijkgesteld met levering tegen kostprijs); (3) herziening van btw-aftrek op nog-niet-uitgeputte bedrijfsmiddelen volgens art. 48 §2 + K.B. nr. 3 (resterende jaren in herzieningstermijn × 1/5 of 1/15 of 1/25). Bijzondere route: bij overdracht van een algemeenheid van goederen (art. 11) wordt geen btw aangerekend en geen herziening uitgevoerd — overnemer neemt over.

<small>📖 W.BTW — art. 53 §1 1° — _wettekst_ · W.BTW — art. 12 §1 5° — _wettekst_ · W.BTW — art. 48 §2 — _wettekst_ · W.BTW — art. 11 — _wettekst_</small>

## Substantie

Economisch is de stopzetting het btw-spiegelmoment: alle aftrek die de belastingplichtige tijdens zijn levensduur heeft genoten op activa die nog niet volledig zijn 'verbruikt' (verkocht aan eindconsument met btw-output), moet worden afgewikkeld. Voor voorraad: er was een aftrek bij aankoop, dus bij stopzetting moet er een output-btw worden gegenereerd — anders zit er btw-vrije voorraad in het systeem die mogelijk privé wordt geconsumeerd. Voor bedrijfsmiddelen (machines, gebouwen): de aftrek werd toegekend op basis van een verwacht btw-belast gebruik gedurende 5/15/25 jaar; stopzetting voor het einde van die termijn = niet alle jaren zijn 'verdiend', dus pro rata terugbetaling. De TOGC-route (art. 11) is een fiscaal-vriendelijke uitzondering: bij continuïteit (overname van een lopende business door een nieuwe btw-plichtige) wordt de keten niet onderbroken — geen output-btw bij stopper, geen herziening, overnemer neemt restant termijn over.

<small>🔗 W.BTW — art. 12 §1 5° — _wettekst_ · W.BTW — art. 11 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Rationale

Spiegelbeginsel + neutralisatie van privé-consumptie. De btw is een verbruiksbelasting die de aftrekketen sluit bij de eindconsument; wie ophoudt belastingplichtige te zijn met activa in handen die nog niet via de markt zijn verbruikt, moet die activa 'liquideren' onder btw — anders ontsnapt het verbruik. Het is ook een corrigerend mechanisme: aftrek tijdens activiteit is voorlopig in zoverre ze door btw-output moet worden gedekt — als die output niet komt (stopzetting voor einde van termijn), moet de oorspronkelijke aftrek herzien worden. BTW-richtlijn 2006/112/EG art. 18 c) (goederen behouden bij stopzetting = belastbare handeling) en art. 184-188 (herziening) zijn de juridische basis.

<small>🔗 BTW-richtlijn 2006/112/EG — art. 18 c + art. 184-188 — _richtlijn_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Gebruikscontext

**Status**: `in-voege` · basis: W.BTW art. 11, 12 §1 5°, 48 §2, 53 §1 1° + K.B. nr. 3 art. 10-11 + K.B. nr. 10

Stabiel regime sinds W.BTW 1969. Herzieningstermijn bedrijfsmiddelen verlengd in 1996 (5j → 5j roerend / 15j onroerend) en 2019 (25j voor opted-in vastgoed).

**✅ Voor**
- 📖 Elke btw-belastingplichtige die definitief stopt: vrijwillige stopzetting (pensioen, overstap loondienst, faillietverklaring), opheffing vennootschap, overdracht aan derde (al dan niet onder art. 11), overlijden zelfstandige zonder voortzetting door erfgenamen.

**🚫 Niet voor**
- 🔗 Tijdelijke onderbreking zonder definitieve stop (ziekte, sabbatical) — daar volstaat een 604B-wijzigingsaangifte met opschorting. Wijziging van rechtsvorm (eenmanszaak → BV) zonder activiteitswijziging — kan onder art. 11 verlopen.

**📋 Voorwaarden**
- 📖 Cumulatief: (1) definitieve beëindiging van alle btw-belastbare handelingen; (2) 604C-aangifte binnen één maand na stopzettingsdatum; (3) laatste periodieke btw-aangifte ingediend over de periode tot stopzetting; (4) eindafrekening voorraad + bedrijfsmiddelen + lopende vorderingen/schulden btw verwerkt; (5) klantenlisting + intracommunautaire opgave tot stopzettingsdatum ingediend.

**⏹ Trigger einde**
- 🔗 Stopzettingsdatum = datum laatste belastbare handeling (laatste factuur of laatste levering). Niet de datum van vrijwillige doorhaling — die kan later vallen, maar telt fiscaal alleen administratief.

**⚠️ Risico**
- 📖 Niet-aangeven onttrekking voorraad bij stopzetting → naheffing van btw op kostprijs voorraad + boete 10-200 % (art. 70 W.BTW). Bijkomende verzwarende factor: indien geen 604C is ingediend, blijft het btw-nummer 'actief' in de fiscale databank — boetes voor niet-ingediende aangiften kunnen jaren doorlopen.
- 📖 Vergeten herziening bedrijfsmiddelen: een gebouw 5 jaar geleden onder btw aangekocht (15-j termijn) → bij stopzetting moet 10/15 van afgetrokken btw worden terugbetaald aan de fiscus. Kan flink oplopen (honderdduizenden EUR voor onroerend bedrijfsmiddel).

## Bouwstenen

### 👣 Stap 1 — Laatste periodieke aangifte

De aangifte over de periode tot en met stopzettingsdatum (kwartaal of maand) wordt ingediend volgens de gewone termijn. Hierin worden alle uitgaande facturen + onttrekkingen (art. 12 §1 5°) + ontvangen facturen opgenomen. Eventuele btw-tegoed: aanvraag tot terugbetaling kan in deze laatste aangifte (vak 72).

<small>📖 W.BTW — art. 53 §1 2° — _wettekst_</small>

### 👣 Stap 2 — Onttrekking voorraad (art. 12 §1 5°)

Voor op de stopzettingsdatum nog aanwezige goederen waarvoor het recht op aftrek (geheel of gedeeltelijk) is uitgeoefend: gelijkgesteld met een levering onder bezwarende titel. Maatstaf = aankoopprijs of, bij gebrek daaraan, kostprijs op het tijdstip van onttrekking (art. 33 §1 1°). Btw wordt aangegeven in de laatste periodieke aangifte (vak 03 + 54). Uitzondering: handelsgoederen die in art. 11-overdracht meegaan.

<small>📖 W.BTW — art. 12 §1 5° — _wettekst_ · W.BTW — art. 33 §1 1° — _wettekst_</small>

### 👣 Stap 3 — Herziening bedrijfsmiddelen (art. 48 §2)

Voor bedrijfsmiddelen aangekocht binnen herzieningstermijn (5j roerend / 15j onroerend / 25j onroerend onder optie-verhuur): herziening van de oorspronkelijke aftrek pro rata resterende jaren. Formule: terug-te-betalen = oorspronkelijke aftrek × (resterende jaren / totale termijn). Toegepast in laatste aangifte (vak 61 negatief saldo). Geldt niet wanneer het bedrijfsmiddel onder art. 11-overdracht meegaat.

<small>📖 W.BTW — art. 48 §2 — _wettekst_ · K.B. nr. 3 — art. 10 — _kb_</small>

### 👣 Stap 4 — 604C indienen + nummerdoorhaling

604C-aangifte indienen elektronisch binnen één maand na stopzettingsdatum. Verplichte gegevens: stopzettingsdatum, reden (overlijden / pensioen / overdracht / faillissement / ander), eventueel overnemer-identificatie bij art. 11-overdracht. Btw-administratie haalt het identificatienummer door — vanaf doorhaling kan de gewezen belastingplichtige geen geldige btw-facturen meer uitschrijven. KBO-mutatie volgt automatisch via Crossroads Bank Enterprises.

<small>📖 W.BTW — art. 53 §1 1° — _wettekst_ · K.B. nr. 10 — art. 2 — _kb_</small>

### ↪️ Uitzondering art. 11 — overdracht algemeenheid

Bij overdracht van een 'algemeenheid van goederen of bedrijfstak' aan een nieuwe btw-belastingplichtige die de activiteit voortzet: geen btw op de overdracht (vrijgesteld art. 11), geen onttrekking voorraad (art. 12 §1 5° vervalt), geen herziening bedrijfsmiddelen (overnemer neemt resterende termijn over via K.B. nr. 3 art. 11 §1). Voorwaarde: overnemer is/wordt btw-plichtig en zet activiteit voort. Belangrijk: dit moet uitdrukkelijk worden vermeld in de overdrachtsakte + 604C; anders verliest de stopper de fiscale gunst.

<small>📖 W.BTW — art. 11 — _wettekst_ · K.B. nr. 3 — art. 11 §1 — _kb_</small>

## Voorbeelden

> [!example]- Stopzetting kleinhandel — voorraad + machine binnen herziening
> _Bakker Joris (eenmanszaak, kwartaalaangever) stopt op pensioen per 30 juni. Voorraad bij stop: meel, grondstoffen, bakmaterialen aankoopwaarde 8.000 EUR (excl. btw, btw 6 % = 480 EUR ooit afgetrokken). Bedrijfsmiddel: oven aangekocht 2 jaar geleden voor 25.000 EUR + 5.250 EUR btw (volledig afgetrokken; herzieningstermijn 5j)._
>
> **Berekening:**
>
> - Stap 1 — Onttrekking voorraad (art. 12 §1 5°): aankoopwaarde 8.000 × 6 % = 480 EUR btw aan te geven in laatste Q2-aangifte (vak 02 + 54).
> - Stap 2 — Herziening oven: oorspronkelijke aftrek 5.250 EUR; gebruikt 2 jaar van de 5-jarige termijn; resterende termijn 3/5; terug-te-betalen = 5.250 × 3/5 = 3.150 EUR (vak 61).
> - Stap 3 — Laatste Q2-aangifte saldo: + 480 (voorraad) + 3.150 (oven herziening) − eventuele input-btw juni = totaal te betalen.
> - Stap 4 — 604C indienen vóór 31 juli.
>
> → **Resultaat**: Totale btw-eindafrekening: 3.630 EUR te betalen aan Schatkist (naast normale Q2-saldo). Joris hield voorraad + oven privé — economisch heeft hij die btw nu op zijn balans als 'consumptie-kost'. Indien hij voorraad + oven aan een opvolger (art. 11) had overgedragen: 0 EUR extra te betalen.
>
> <small>🔗 W.BTW — art. 12 §1 5° — _wettekst_ · W.BTW — art. 48 §2 — _wettekst_ · K.B. nr. 3 — art. 10 — _kb_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

> [!example]- Art. 11-overdracht — verkoop handelszaak aan opvolger
> _Slager Vandekerckhove BV verkoopt zijn handelszaak (handelsfonds + voorraad + winkel-inrichting) aan opvolger Slager Mertens BV voor 200.000 EUR. Voorraad waarde 30.000 EUR, winkelinrichting (4 jaar oud, 5j-termijn) oorspronkelijk 50.000 EUR + 10.500 EUR btw afgetrokken. Beide partijen zijn btw-plichtig en Mertens zet de slagerij voort._
>
> 1. 1. Overdrachtsakte vermeldt uitdrukkelijk 'overdracht algemeenheid art. 11 W.BTW'.
> 2. 2. Geen btw op de 200.000 EUR overdrachtprijs.
> 3. 3. Geen onttrekking voorraad — Mertens neemt over met behoud van btw-aftrek-recht.
> 4. 4. Geen herziening winkelinrichting — Mertens neemt de resterende 1/5 termijn over.
> 5. 5. Vandekerckhove BV dient 604C in + vermeldt opvolger Mertens BV-btw-nummer.
>
> → **Resultaat**: Btw-neutraal voor beide partijen. Zonder art. 11: Vandekerckhove had voorraad-onttrekking 6.300 EUR + winkelinrichting-herziening 2.100 EUR = 8.400 EUR extra moeten betalen; Mertens had ook geen aftrek meer (want geen factuur met btw). Art. 11 maakt de overname economisch identiek aan een doorlopende activiteit.
>
> <small>🔗 W.BTW — art. 11 — _wettekst_ · K.B. nr. 3 — art. 11 §1 — _kb_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Valkuilen

> [!warning]- 604C 'wanneer ik tijd heb' indienen
> **Verkeerde assumptie**: Studenten denken dat er voldoende tijd is om de eindafrekening rustig te maken.
>
> **Kernpunt**: Termijn is ÉÉN maand na stopzettingsdatum (art. 53 §1 1° W.BTW). Laattijdig = boete + verlies van mogelijke art. 11-gunst (overnemer moet weten dat overdracht onder art. 11 valt — duidelijkheid vereist).
>
> <small>📖 W.BTW — art. 53 §1 1° — _wettekst_</small>

> [!warning]- Voorraad onttrekken aan 'aankoopwaarde' min slijtage
> **Verkeerde assumptie**: Studenten passen 'marktwaarde' of een afschrijving toe op de voorraad bij onttrekking.
>
> **Kernpunt**: Art. 33 §1 1° W.BTW: maatstaf = aankoopprijs of bij gebrek daaraan kostprijs op het ogenblik van de onttrekking. Bij voorraad in goede staat ≈ aankoopprijs. Lagere waardering enkel mogelijk bij bewezen waardevermindering (bv. bederfbare goederen).
>
> <small>📖 W.BTW — art. 33 §1 1° — _wettekst_</small>

> [!warning]- Vergeten dat art. 11 expliciet moet vermeld worden
> **Verkeerde assumptie**: Bij overdracht handelszaak past art. 11 automatisch toe.
>
> **Kernpunt**: De fiscus aanvaardt art. 11 enkel als (a) de overdracht inderdaad een algemeenheid of bedrijfstak betreft, niet enkel losse activa; (b) de overnemer een btw-plichtige is die voortzet; (c) dit uitdrukkelijk wordt gedocumenteerd in de akte. Zonder die elementen → gewone btw-handeling met onttrekking + herziening.
>
> <small>📖 W.BTW — art. 11 — _wettekst_</small>

## Accountant-perspectieven

### Stoppende zelfstandige (pensioen, overdracht)

_Accountant van een zelfstandige of vennootschap die de activiteit beëindigt._

#### 💰 Fiscaal adviseur

##### 👣 Scenario-analyse art. 11 vs gewone stopzetting

Bij overdracht aan opvolger: altijd eerst beoordelen of art. 11 haalbaar is (handelsfonds, voorraad, inventaris samen overgedragen + opvolger btw-plichtig). Berekening 'kostprijs vergeten art. 11' = onttrekking voorraad + herziening bedrijfsmiddelen; vaak veel hoger dan partijen verwachten. Documenteer beslissing en motivering in cliëntdossier.

<small>🔗 W.BTW — art. 11 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

#### 📒 Boekhouder

##### 👣 Inventarisatie + bedrijfsmiddelenlijst per stopzettingsdatum

Per stopzettingsdatum: fysieke voorraadtelling met aankoopwaarde + datum; bedrijfsmiddelenlijst met aankoopdatum + oorspronkelijke btw-aftrek + herzieningstermijn (5/15/25j) + resterende jaren. Dit is de basis voor de eindafrekening. Bewaartermijn 7 jaar voor btw-doeleinden + 10 jaar boekhouding.

<small>📖 W.BTW — art. 60 — _wettekst_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Verder lezen (scope-out)

- → BTW-herziening bij stopzetting → [[btw-herziening-bedrijfsmiddelen]] _(moet-verwijzen)_
- → Opstart-formaliteiten (spiegel) → [[opstart-btw-formaliteiten]] _(moet-verwijzen)_

## Relaties

### `valt_onder`
- [[btw]]
### `triggert`
- [[btw-herziening-bedrijfsmiddelen]] — Stopzetting binnen herzieningstermijn activeert pro-rata herziening.
### `vergelijkbaar_met`
- [[opstart-btw-formaliteiten]]
    - **Gelijkenissen**:
        - Spiegelprocedure — registratie/de-registratie via 604-formulieren
    - **Verschillen**:
        - 604A vóór aanvang; 604C binnen één maand na stopzetting
        - Opstart genereert aftrek; stopzetting kan herziening triggeren
    - ⚠️ **Verwarringsrisico**: Formulier 604A/B/C verwisselen — A = aanvang, B = wijziging, C = stopzetting.
