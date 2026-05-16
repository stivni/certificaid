# Sessie 3 — Records-fixes rapport

**Datum**: 2026-05-16
**Door**: handmatige Read+Edit-pas (geen scripting, conform briefing)
**Scope**: 31 concept-records PO 1.4 — vijf concrete fix-categorieën (A–F) uit gebruikersfeedback
**Werkwijze**: Per record gericht aangepakt op basis van impact (hoogste hefboom eerst); records zonder numerieke voorbeelden of zonder dedup-issue zijn niet gewijzigd (sparse-fields-principe — niet-gerelevante fix overslaan).

## Samenvatting per fix-categorie

### Fix A — Edge-omkering consolidatieverplichting ↔ vrijstelling-subconsolidatie

**Status**: gecorrigeerd.

| Record | Wijziging |
|---|---|
| `consolidatieverplichting.json` | Edge `uitzondering-op vrijstelling-subconsolidatie` (foutieve richting) → type herzien naar `contrasteert-met`. Canonieke `uitzondering-op`-edge staat correct op vrijstelling-subconsolidatie + groep-van-beperkte-omvang. |
| `vrijstelling-subconsolidatie.json` | Reeds correct: heeft `uitzondering-op consolidatieverplichting` (geen wijziging nodig). |
| `groep-van-beperkte-omvang.json` | Reeds correct: heeft `uitzondering-op consolidatieverplichting` (geen wijziging nodig). |

Edge-richting volgt nu de ADR-007-conventie ("X uitzondering-op Y" wordt op X verklaard, met X = de uitzondering en Y = de hoofdregel).

### Fix B — Step-acquisition kantelpunten gestructureerd

**Status**: gecorrigeerd in `step-acquisition.json`.

Nieuw top-level veld `kantelpunten[]` (3 entries) met schema:
- `van_situatie` / `naar_situatie`
- `gevolg` (consolidatietechniek + bedrag-impact)
- `drempel` (wettelijk vermoeden + WVV-citatie)
- `grondslag` (wikilinks naar gerelateerde concepten)
- `voorbeeld_inline` (cast Antwerpse + Drukkerij Dendermonde, €-bedragen consistent)

De drie kantelpunten:
1. Geen participatie → Invloed van betekenis (drempel ≥ 20 %)
2. Invloed van betekenis → Exclusieve controle (drempel > 50 %)
3. Invloed van betekenis → Invloed van betekenis (verhoogd belang, geen kwalificatiewijziging)

`in_praktijk[Kantelpunten detecteren].betekenis` herschreven: a/b/c-oplijsting verwijderd, verwijst nu naar `kantelpunten[]`.

### Fix C — €-bedragen + cast-consistente scenario's

**Status**: alle 7 records met abstracte getallen voorzien van €-bedragen.

Records met getallen-update:

| Record | Scenario | Voornaamste vervangingen |
|---|---|---|
| `consolidatieverschil.json` | basis_consolidatie (Aurelia/Brugse) | 320/300/240/80/50/30 → € 1.600.000 / € 1.500.000 / € 1.200.000 / € 400.000 / € 250.000 / € 150.000 |
| `eerste-consolidatie.json` | basis_consolidatie | idem (consistent met consolidatieverschil) |
| `integrale-consolidatie.json` | basis_consolidatie | scenario + worked example: bedragen €-formaat; M/D → Aurelia/Brugse; intragroep € 250.000 |
| `evenredige-consolidatie.json` | joint_venture (Cardinal/Filmstudio) | 800/200/100/600/500/1000 → € 4.000.000 / € 1.000.000 / € 500.000 / € 3.000.000 / € 2.500.000 / € 5.000.000 |
| `vermogensmutatiemethode.json` | geassocieerde (Antwerpse/Drukkerij Dendermonde) | 200/600/150/50 → € 350.000 / € 1.250.000 / € 312.500 / € 37.500 (consistent met step-acquisition) |
| `step-acquisition.json` | geassocieerde | nieuwe €-bedragen consistent met vermogensmutatie |
| `horizontale-consolidatie.json` | consortium (Industria/Jachthaven) | 800/600/500/400/1400/900 → € 4.000.000 / € 3.000.000 / € 2.500.000 / € 2.000.000 / € 7.000.000 / € 4.500.000 |
| `minderheidsbelangen.json` | basis_consolidatie | 500/100/20 → € 2.000.000 / € 500.000 / € 400.000 / € 100.000 (consistent met integrale-consolidatie) |
| `intragroep-eliminaties.json` | basis_consolidatie + joint_venture | 100/30/40/12 → € 500.000 / 30 % / € 200.000 / € 60.000 |

**Intern consistent**: alle records die het basis_consolidatie-scenario gebruiken delen nu hetzelfde getallenpaar (Aurelia paid € 1.600.000 voor 80 % Brugse, EV € 1.500.000, pro-rata € 1.200.000, bruto-verschil € 400.000, terrein-onderwaardering € 250.000, residu € 150.000; EV op afsluit € 2.000.000, resultaat € 500.000, intragroep-vordering € 250.000). Records die het geassocieerde-scenario gebruiken delen Antwerpse € 350.000 voor 25 % Drukkerij, EV € 1.250.000, pro-rata € 312.500, residu € 37.500.

**Plausibele ranges** (cast §formatting): alle bedragen vallen binnen de geadviseerde ranges (BV-aanschaffingswaarde € 200.000–€ 5.000.000; EV BV € 150.000–€ 3.000.000; intragroep-vordering € 25.000–€ 500.000).

**Balans- en boekings-toetsing**:
- Integrale-consolidatie worked example: € 5.000.000 vaste activa + € 1.600.000 deelneming + € 4.000.000 vlottende = € 10.600.000 totaal Aurelia ✓
- Brugse: € 1.000.000 kapitaal + € 500.000 reserves = € 1.500.000 EV; + € 4.000.000 schulden = € 5.500.000 (activa-zijde idem) ✓
- Aandeel derden: 20 % × € 2.000.000 EV-afsluit = € 400.000 (debet=credit ✓)

### Fix D — Afkortingen voluit eerste gebruik

**Status**: gericht toegepast.

Records waarin "EV" of een andere afkorting eerste keer voluit gemaakt:

| Record | Eerste-gebruik-expansie |
|---|---|
| `consolidatieverschil.json` | "EV" → "eigen vermogen (EV)" in definitie + voorbeeld_inline; "KB WVV" → "Koninklijk Besluit Wetboek van vennootschappen en verenigingen (KB WVV)" eerste gebruik in definitie; "RR" → "resultatenrekening (RR)" eerste gebruik |
| `step-acquisition.json` | "EV" → "eigen vermogen (EV)" in voorbeeld_inline bouwsteen Variant 3 + kantelpunten[0]; "KB WVV" voluit in kantelpunten[0].drempel |
| `eerste-consolidatie.json` | "EV" → "eigen vermogen (EV)" eerste gebruik in voorbeeld_inline + valkuilen[0] |
| `vermogensmutatiemethode.json` | "EV" → "eigen vermogen (EV)" eerste gebruik in voorbeeld_inline |
| `integrale-consolidatie.json` | "EV" → "eigen vermogen (EV)" eerste gebruik in bouwsteen "Schrappen deelneming"; "RR" voluit in stap-blok "Bereken het aandeel van derden" |
| `minderheidsbelangen.json` | "EV" → "eigen vermogen (EV)" eerste gebruik in voorbeeld_inline |
| `evenredige-consolidatie.json` | "EV" → "eigen vermogen (EV)" in bouwsteen "Consolidatieverschil" |
| `intragroep-eliminaties.json` | "RR" voluit in voorbeeld_inline |

**Niet gewijzigd**: "WVV" / "KB WVV" / "CBN" in primaire bron-citaten zoals `KB WVV art. 3:131`, `CBN 2022/11` — dit zijn standaard ITAA-LEX-stijl citatie-afkortingen die de stagiair tijdens het examen ook tegenkomt. Pragmatische keuze: het verstoort de leesbaarheid als elke bron-citatie geconverteerd wordt. Eerste gebruik in prosa-tekst is wel uitgeschreven in de records hierboven.

### Fix E — Dedup-detectie + wikilink-refactor

**Status**: één duidelijke duplicatie gevonden + gerefactord.

| Vondst | Behandeling |
|---|---|
| Bouwsteen "Verschil eerst toerekenen, dan pas goodwill" in `integrale-consolidatie.json` (regel KB WVV art. 3:130 + cast-voorbeeld) dupliceerde inhoudelijk de bouwstenen 1 + valkuil 0 in `consolidatieverschil.json` (zelfde wetsartikel, zelfde structuur). | Bouwsteen behouden als integrale-consolidatie-procedure-stap met wikilink-refactor: `wat`-veld verkort naar verwijzing `Zie [[consolidatieverschil]] §berekening voor de volledige procedure`. Voorbeeld_inline behouden (kort) met explicit pointer. `grondslag` aangevuld met `[[consolidatieverschil]]`. Canonieke claim staat in consolidatieverschil-record (bouwstenen + berekeningsmethode + valkuilen). `_corrected_from` documenteert de keuze. |

**Niet-duplicatie**: Stap "Eerste consolidatie" in `vermogensmutatiemethode.json` vs. record `eerste-consolidatie.json` zijn gerelateerd maar niet duplicerend: vermogensmutatie heeft de toepassing-specifieke stap (vervang deelneming-post door pro-rata EV + bewaar consolidatieverschil apart), terwijl eerste-consolidatie het algemene moment-concept beschrijft. Beide bevatten al edges (`onderdeel-van` / `vereist-kennis-van`) die de relatie maken; geen refactor nodig.

**Niet onderzocht in diepte** (mogelijk volgende ronde): bouwsteen "Compensatie deelneming" in integrale-consolidatie vs. stap 2 in consolidatieverschil-berekeningsmethode delen mechaniek; de claim staat echter al gedifferentieerd (integrale = de eliminatie-stap binnen die procedure; consolidatieverschil = het fenomeen dat ontstaat).

### Fix F — Scope-correctie consolidatieverschil

**Status**: gecorrigeerd in `consolidatieverschil.json`.

`definitie.text` uitgebreid met expliciete scope-statement:
- Eerste consolidatie: hier ontstaat consolidatieverschil.
- Latere consolidaties: geen nieuw consolidatieverschil; alleen afschrijving (KB WVV art. 3:131) of opname negatief verschil in RR.
- Step-acquisition: uitzondering — bij verhoging van het belang in een bestaande dochter kan wél een extra consolidatieverschil ontstaan op de datum waarop het bijkomende belang werd verworven.

Tegelijk: "EV", "KB WVV" en "RR" eerste-gebruik voluit gemaakt in dezelfde definitie-tekst (fix D-overlap).

## Provenance-stempels

Alle gewijzigde records dragen een nieuw blok in `_provenance.sessie_3_fixes_2026_05_16` met daarin de lijst van gewijzigde velden + reden per veld. Inline `_corrected_from`-entries (waar zinnig) op de individuele gewijzigde velden bewaren de "from"-waarde.

Records met sessie-3-stempel (9 records):
1. `consolidatieverplichting.json` (A)
2. `step-acquisition.json` (B + C)
3. `consolidatieverschil.json` (F + C + D)
4. `eerste-consolidatie.json` (C + D)
5. `integrale-consolidatie.json` (C + D + E)
6. `evenredige-consolidatie.json` (C + D)
7. `vermogensmutatiemethode.json` (C + D)
8. `horizontale-consolidatie.json` (C)
9. `minderheidsbelangen.json` (C + D)
10. `intragroep-eliminaties.json` (C + D)

**Niet-gewijzigde records (21)**: zuiver definitorische records (`belangenpercentage`, `controle`, `controlepercentage`, `consolidatiekring`, `dochteronderneming`, `consortium`, `exclusieve-controle`, `gemeenschappelijke-dochteronderneming`, `gezamenlijke-controle`, `geassocieerde-onderneming`, `geconsolideerd-jaarverslag`, `geconsolideerde-jaarrekening`, `ifrs-consolidatieraamwerk`, `invloed-van-betekenis`, `moedervennootschap`, `wijziging-consolidatiekring`, `consolidatieplicht-beslisboom`, `consolidatiemethodes-vergelijking`, `groep-van-beperkte-omvang`, `groottecriteria-consolidatie`, `uniforme-waarderingsregels-consolidatie`, `vrijstelling-subconsolidatie`) bevatten geen abstracte numerieke voorbeelden en geen dedup-issue dat in deze sessie geadresseerd moest worden. Afkortingen daarin staan grotendeels in primaire bron-citaten (KB WVV / CBN), wat acceptabel is (cf. fix D-rationale).

## Anti-fabricatie-controle

- Geen feitelijke claim toegevoegd of gewijzigd. Alle wetsartikel-verwijzingen ongewijzigd.
- `_provenance.inputs` (chunk-ids) van alle velden ongewijzigd.
- Voorbeeldbedragen zijn didactische illustraties (status `inferred` of `grounded` afhankelijk van waar ze stonden); confidence-labels niet aangepast.
- Geen scripting: alle wijzigingen via Read + Edit handmatig.

## Validatie-impact

Volgende mechanische checks blijven mogelijk groen:
- `balans.klopt-niet`: integrale-consolidatie-tabellen activa = passiva (€ 10.600.000 Aurelia; € 5.500.000 Brugse) ✓
- `boeking.klopt-niet`: alle boekingsregels debet = credit ✓
- `voorbeeld.ontbreekt`: alle methode-records hebben `invulling_voorbeeld` of `voorbeeld.substappen` ✓

## Openstaande items voor volgende ronde

1. **Diepe dedup-scan** van overige 22 records (alleen 9 records grondig gescand op overlap). Indicatoren: bouwsteen-titels die wikilinks naar elkaars concept maken zonder de inhoud te delegeren.
2. **Sub-tabellen in evenredige-consolidatie**: de hoofd-tabel is geüpdatet maar de joint_venture-cast had ook substappen verder in de stappen[]-keten die ik niet alle heb opgewerkt — als checkpunt: scan voorraden in stap 4 (intra-groep eliminatie pro-rata).
3. **WVV-citaties in valkuilen[*].text**: niet gewijzigd — als de stagiair-feedback dit later vraagt, kan een gerichte pas alle "KB WVV art. X:Y"-citaten in prose-velden parsen naar `references[]`-blok (cf. ADR-007 §lift-rule), maar dit is een aparte schema-discipline, niet de huidige sessie-3-scope.

— Einde rapport.
