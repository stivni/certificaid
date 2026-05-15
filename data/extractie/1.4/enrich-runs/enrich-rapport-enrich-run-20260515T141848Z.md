# ENRICH-rapport — enrich-run-20260515T141848Z

**Programmaonderdeel**: 1.4
**Run-id**: enrich-run-20260515T141848Z
**Uitgevoerd door**: claude-opus-4-7 (subagent)
**Uitgevoerd op**: 2026-05-15T15:00:00+00:00
**Records verwerkt**: 7
**Gaps verwerkt**: 8 (2 hoog / 6 midden / 0 laag)
**Correcties aangebracht**: 1 (verplicht `corrected_from` aanwezig)
**Records-ontbreekt gaps overgeslagen (EXTRACT-taak)**: 0

## Samenvatting per record

| Record | Gaps | Status |
|---|---|---|
| `consolidatieverschil` | `definitie.onvolledig`, `vergelijkingsparen.vrije-tekst-niet-gespiegeld` | enriched-pending-verify |
| `geconsolideerde-jaarrekening` | `drempelwaarden.ontbreekt` | enriched-pending-verify |
| `evenredige-consolidatie` | `vergelijkingsparen.vrije-tekst-niet-gespiegeld` | enriched-pending-verify |
| `exclusieve-controle` | `in_praktijk.ontbreekt` | enriched-pending-verify |
| `geconsolideerd-jaarverslag` | `in_praktijk.ontbreekt` | enriched-pending-verify |
| `groep-van-beperkte-omvang` | `records.overlappend-fenomeen` | enriched-pending-verify (geen merge — zie caveat) |
| `vermogensmutatiemethode` | `vergelijkingsparen.vrije-tekst-niet-gespiegeld` | enriched-pending-verify |

---

## Per record — bron-chunks per veld + caveats

### `consolidatieverschil`

**Gap 1 — `definitie.onvolledig` (prio: hoog)**

Status: enriched-pending-verify.

De gap signaleerde dat de oorzaken-array slechts 3 entries telt waarvan één (verwachte ongunstige resultaatsontwikkeling) negatief betreft, terwijl examenvragen 2013-2 vr8 en 2015-1 vr11 vier voornaamste oorzaken van een **positief** consolidatieverschil vragen. Resolutie: ik liet de bestaande `definitie.text` en de bestaande drie `oorzaken[]`-items volledig ongewijzigd (append-only contract) en voegde twee nieuwe `oorzaken[]`-items toe.

Toegevoegde oorzaken:
- **"Overgewaardeerde passiva van de dochter (te hoge voorzieningen, te ruim ingeschatte schulden)"** — confidence: `grounded`. Bron: `KB-WVV-2019__art_3_102` (art. 3:130, eerste lid: "actief- EN passiefbestanddelen waarvan de waarde hoger of lager is dan hun boekwaarde"). Dit is geen redenering maar letterlijk wat de wettekst toelaat.
- **"Niet-geactiveerde immateriële waarden in de dochter (synergieverwachtingen, marktpositie, klantenbestand, merken, knowhow)"** — confidence: `inferred-from-aggregation`. Bronnen: `Richtlijn-2013-34-EU__art_24__sub_lid1-lid14` (residu = "goodwill"); `KB-WVV-2019__art_3_102` en `__art_3_103`. Bewust niet `grounded` omdat het label "niet-geactiveerde immateriële waarden" een synthese is over de Belgische en Europese wettekst; de bron noemt enkel het generieke "goodwill"-residu.

Caveat: de bestaande oorzaak "Overpaid goodwill" overlapt deels met de nieuwe "Niet-geactiveerde immateriële waarden". Bewust niet gemerged — append-only contract verbiedt verwijdering. VERIFY-agent kan in een latere ronde beoordelen of consolidatie nodig is.

**Gap 2 — `vergelijkingsparen.vrije-tekst-niet-gespiegeld` (prio: midden)**

Status: enriched-pending-verify.

Toegevoegde vergelijkingsparen:
- **`dochteronderneming`** — gebaseerd op `KB-WVV-2019__art_3_102` (art. 3:130) en `__art_3_103` (art. 3:131). Behandelt integrale consolidatie-context.
- **`geassocieerde-onderneming`** — gebaseerd op `CBN-2013-03-de-boekhoudkundige-verwerking-van-step-acquisitions-update__sec_praktische-uitwerking` (expliciete nuance art. 3:142, § 3 "slechts voor zover dit mogelijk is") en `CBN-2022-11-vermogensmutatiemethode__sec_eerste-consolidatie` (residu naast balanspost "Vennootschappen waarop vermogensmutatie is toegepast").

---

### `geconsolideerde-jaarrekening`

**Gap — `drempelwaarden.ontbreekt` (prio: hoog)**

Status: enriched-pending-verify.

Nieuwe `drempelwaarden[]`-array aangemaakt (veld bestond nog niet in het record) met één item:
- **"Maximale afwijking afsluitingsdatum dochter ↔ geconsolideerde jaarrekening"** — waarde: 3 maanden — confidence: `grounded`. Bron: `KB-WVV-2019__art_3_86` (art. 3:110, tweede lid: "Tussen beide data of de beschouwde periodes mag evenwel onder geen enkel beding meer dan drie maanden liggen.").

Caveat: de gap-reden verwees naar "KB WVV art. 3:109 tweede lid", maar de bundle-bron leverde dit criterium op via **art. 3:110, tweede lid** (over volledigheid + opname op andere datum). Art. 3:109 (afsluitingsdatum) bevat de regel dat een andere datum mag worden gebruikt om rekening te houden met de balansdatum van de meeste/belangrijkste dochters, maar zonder kwantitatieve drempel. De 3-maanden-grens staat in art. 3:110. Ik heb daarom de juiste bronvermelding gebruikt (art. 3:110); zo nodig kan VERIFY de gap-tekst rechtzetten.

---

### `evenredige-consolidatie`

**Gap — `vergelijkingsparen.vrije-tekst-niet-gespiegeld` (prio: midden)**

Status: enriched-pending-verify.

Toegevoegde vergelijkingsparen (drie items):
- **`gezamenlijke-controle`** — bronnen: `KB-WVV-2019__art_3_98` (art. 3:124, 2°) en `CBN-2017-02-gezamenlijke-controle-over-een-vennootschap-groottecriteria-update__sec_algemeen` (definitie + overeenkomstvereiste).
- **`gemeenschappelijke-dochteronderneming`** — bron: `KB-WVV-2019__art_3_111` (art. 3:140, b). Pro-rata-opname op niveau van kapitaalrechten.
- **`belangen-van-derden`** — bronnen: `KB-WVV-2019__art_3_111` (art. 3:140 verwijst niet naar art. 3:137) en `KB-WVV-2019__art_3_108`. Examenrelevant: bij evenredig géén derden-post.

---

### `exclusieve-controle`

**Gap — `in_praktijk.ontbreekt` (prio: midden)**

Status: enriched-pending-verify.

Drie nieuwe `in_praktijk[]`-items toegevoegd:
- **"Onderscheid controle in rechte vs. controle in feite"** — confidence: `inferred-from-aggregation`. Bronnen: `CBN-2022-09-consolidatie-bij-de-horizontale-groep-consortium-0__sec_horizontale-groep` (wettelijke vermoedens), `CBN-2017-02-gezamenlijke-controle-over-een-vennootschap-groottecriteria-update__sec_algemeen`, `KB-WVV-2019__art_3_77`.
- **"Uitsluiting uit consolidatie ondanks exclusieve controle"** — confidence: `grounded`. Bronnen: `KB-WVV-2019__art_3_77` (art. 3:98 uitsluiting bij getrouw beeld in gedrang) en `CBN-2013-03-de-boekhoudkundige-verwerking-van-step-acquisitions-update__sec_praktische-uitwerking` (vermogensmutatie als alternatief).
- **"Effect op de groottecriteria van de moedervennootschap"** — confidence: `grounded`. Bronnen: `CBN-2022-03-beoordeling-van-de-groottecriteria-overeenkomstig-artikelen-124-en-125-van-het-wetboek-van__sec_consolidatie-moedervennootschap` en `CBN-2017-02-…__sec_voorbeeld-2`.

Caveat: ik heb géén nieuw concreet voorbeeld toegevoegd voor de "twee opeenvolgende AVs"-test die de gap suggereerde. De bron-bundle bevat geen letterlijke vermelding van art. 1:14 WVV met die formulering; alleen het bestaande record verwijst er — al via een `inferred`-label — naar. Volgens de anti-hallucinatie-regels mag ik geen wetsartikelnummers of letterlijke testen toevoegen die niet in de bundle staan. De examen-toepasbaarheid wordt afgedekt door de drie nieuwe entries hierboven (vooral het onderscheid in rechte ↔ in feite + uitsluiting-bij-getrouw-beeld).

---

### `geconsolideerd-jaarverslag`

**Gap — `in_praktijk.ontbreekt` (prio: midden)**

Status: enriched-pending-verify.

Drie nieuwe `in_praktijk[]`-items toegevoegd:
- **"Inhoud — minimum-aanvullingen op het 'gewone' bestuursverslag"** — confidence: `grounded`. Bron: `Richtlijn-2013-34-EU__art_29__sub_lid1-lid5_part1` (art. 29, lid 1 en 2 met de twee aanpassingen: eigen aandelen op groepsniveau + groepsbrede interne controle/risicobeheer).
- **"Geconsolideerde duurzaamheidsrapportering"** — confidence: `grounded`. Zelfde chunk-bron (art. 29 CSRD-implementatie). Examenrelevant voor de actuele context (post-2024).
- **"Vrijstellingstrigger valt samen met de jaarrekening"** — confidence: `grounded`. Bron: `CBN-2022-11-vermogensmutatiemethode__sec_toepassingsgebied` (één gezamenlijke vrijstelling).

Caveat: WVV art. 3:32 en 3:35 (Belgische omzetting) zaten niet als losse chunks in de bundle; de Belgische details (risico's, onzekerheden, niet-financiële verklaring) zijn impliciet via de richtlijn-link gegrond, niet rechtstreeks via WVV-tekst. De bestaande `definitie`- en `references`-velden vermelden art. 3:32 reeds; ik heb daar niets aan veranderd.

---

### `groep-van-beperkte-omvang`

**Gap — `records.overlappend-fenomeen` (prio: midden)**

Status: enriched-pending-verify.

**Beslissing**: GEEN merge met `groottecriteria-consolidatie`. De bronnen tonen dat het twee verschillende fenomenen zijn:
- `groep van beperkte omvang` = juridische **kwalificatie/statuut** (uitkomst van de toets met als enig gevolg de vrijstelling van consolidatie en jaarverslag; WVV art. 1:26, § 1; CBN 2022/11 toepassingsgebied).
- `groottecriteria-consolidatie` = **meet-set en rekenmethoden** (omzet/balanstotaal/personeel, geconsolideerd vs. geaggregeerd +20 %; CBN 2022/03). Deze meet-set wordt ook in andere contexten gebruikt (bv. kwalificatie kleine/grote vennootschap onder art. 1:24).

Resolutie: ik heb de bestaande vergelijkingspaar-entry `vergelijking_met: "groottecriteria-consolidatie"` **gecorrigeerd** (met verplicht `corrected_from` + `correction_reason` + `correction_source`) door het `verschil`-veld te verrijken met een expliciete uiteenzetting van het onderscheid. De originele tekst staat bewaard in `corrected_from`.

Bronnen voor de correctie:
- `CBN-2022-11-vermogensmutatiemethode__sec_toepassingsgebied`
- `CBN-2022-03-beoordeling-van-de-groottecriteria-overeenkomstig-artikelen-124-en-125-van-het-wetboek-van__sec_vereenvoudigde-methode-berekening-van-het-balanstotaal-en-de`

Caveat: de andere record (`groottecriteria-consolidatie`) is **niet** door deze run aangeraakt — zoals de werkprompt vereist (één record per gap-entry). De gap-tekst impliceert dat beide records aangescherpt zouden moeten worden; in dit record is dat gebeurd. Voor het andere record kan een vervolg-gap door VERIFY worden aangemaakt.

---

### `vermogensmutatiemethode`

**Gap — `vergelijkingsparen.vrije-tekst-niet-gespiegeld` (prio: midden)**

Status: enriched-pending-verify.

Twee nieuwe `vergelijkingsparen[]`-items toegevoegd:
- **`invloed-van-betekenis`** — bronnen: `CBN-2013-03-de-boekhoudkundige-verwerking-van-step-acquisitions-update__sec_inleiding` (WVV art. 1:22 vermoeden vanaf 20 %) en `CBN-2022-11-vermogensmutatiemethode__sec_toepassingsgebied`. Inclusief nuance: vermogensmutatie wordt óók toegepast op uitgesloten dochters en niet-geïntegreerde gemeenschappelijke dochters.
- **`consolidatieverschil`** — bronnen: `CBN-2022-11-vermogensmutatiemethode__sec_eerste-consolidatie` (residu wordt geboekt onder 'Consolidatieverschillen' apart van 'Vennootschappen waarop vermogensmutatie is toegepast') en `CBN-2013-03-…__sec_praktische-uitwerking` (KB WVV art. 3:142, § 3 'slechts voor zover dit mogelijk is').

---

## Algemene caveats

1. **Geen records.ontbreekt-gaps** in deze run — geen EXTRACT-overdracht nodig.
2. **Enrich_runs in top-level _provenance**: bij elke van de 7 records is `_provenance.enrich_runs[]` aangemaakt met run-id, model, gaps_verwerkt, uitgevoerd_op.
3. **Schemavalidatie**: alle 7 records valideren als geldige JSON (gecheckt met `json.load`).
4. **Append-only contract gerespecteerd**: geen velden of array-items verwijderd. De enige correctie zit in `groep-van-beperkte-omvang.vergelijkingsparen[0]` en is volledig gedocumenteerd met `corrected_from` + `correction_reason` + `correction_source`.
5. **Bron-discipline**: elke nieuwe claim is voorzien van `_provenance.inputs` met thematisch relevante chunk-id's uit de meegeleverde bundles. Geen wetsartikelnummers verzonnen.
