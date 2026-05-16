# PO 1.2 Competentie-destillatie — Rapport 2026-05-16

**Run**: competentie-destillatie-v2-po12-20260516
**Model**: claude-opus-4-7 (subagent)
**Scope**: PO 1.2 — Boekhoudrecht en jaarrekeningenrecht
**Prompt**: `prompts/competentie-destillatie-v2.md` (schema 1.1)
**Budget**: ~45 min

---

## Samenvatting

| Metriek | Aantal |
|---|---|
| Voorgestelde competenties | **9** |
| Bestanden geschreven | 9 |
| Stappen totaal | 36 (steeds 4 per competentie) |
| Competenties met `praktijk_pct` > 30% | 0 |
| Competenties met `praktijk_pct` 11-30% | 1 (`identificeren-administratieve-autoriteit`: 15%) |
| Competenties met `praktijk_pct` > 0% en ≤ 10% | 7 |
| Competenties met `praktijk_pct` > 30% in recht-context (flag voor mens-review) | 0 |

Negen competenties zit aan de bovenkant van het richtgetal (6-9). De keuze viel zo omdat PO 1.2 erg breed is: bronhiërarchie, autoriteiten, boekhoudplicht, groottecriteria, schema's, commissaris, openbaarmaking, beginselen-waardering én VZW. Smelt je twee samen, dan riskeer je verdunning; daarom liever apart en strak.

Alle 9 yamls valideren als geldig YAML met schema 1.1-skelet. Elke stap heeft `grondslag`. Alle competenties hebben `gebaseerd_op_concepten` ≥ 2. Alle `wettelijk_pct + praktijk_pct == 100`.

---

## Competenties — lijst + motivering

### 1. `identificeren-rechtsbron-boekhoudrecht`
**Anchors**: 1.2.I, 1.2.I.A, 1.2.I.C, 1.2.I.D, 1.2.I.E, 1.2.I.F
**Motivering**: Klassieke stagiair-vraag. Bij elk boekhoudrechtelijk dossier moet de juiste rechtsbron eerst worden bepaald — voorkomt fouten in latere stappen. Vier stappen: categoriseren → bronhiërarchie toepassen → adviezen/rechtspraak raadplegen → cliëntnota met grondslag.
**Praktijk-pct**: 10% — hoofdzakelijk juridisch maar het wegen van CBN-adviezen is praktijkoordeel.

### 2. `kwalificeren-boekhoudplichtige-onderneming`
**Anchors**: 1.2.III, 1.2.III.B, 1.2.III.C, 1.2.I.C
**Motivering**: Dekt de cruciale eerste vraag in een nieuw dossier — wie moet boekhouden, en hoe (dubbel of vereenvoudigd). Differentiatie tussen rechtspersoon en eenmanszaak gebeurt in stap 2.
**Praktijk-pct**: 10% — drempels en MAR strikt wettelijk, alleen omzet-inschatting is praktisch.

### 3. `klasseren-vennootschap-naar-groottecategorie`
**Anchors**: 1.2.IV.B, 1.2.IV
**Motivering**: Centrale procedure voor PO 1.2. Veel examenvragen gaan over micro/klein/groot-classificatie. Schema integreert de lock-in-regel én de verbondenheidsregel — vaak vergeten door studenten.
**Praktijk-pct**: 5% — hoogste wettelijkheid omdat criteria zelf strikt zijn.

### 4. `bepalen-jaarrekeningschema`
**Anchors**: 1.2.IV.C, 1.2.IV, 1.2.taak.1
**Motivering**: Vervolg op competentie 3. Bouwt brug van grootteklasse naar concrete schemakeuze (KB-WVV bijlagen 1/2/3) + sociale balans + jaarverslag-verplichting. Verklaart waarom drie schema's bestaan en welk effect schema-wisseling heeft.
**Praktijk-pct**: 5%.

### 5. `beoordelen-commissaris-verplichting`
**Anchors**: 1.2.IV.E, 1.2.IV
**Motivering**: Klassieke examenvraag — "moet deze BV een commissaris benoemen?". De competentie modelleert ook PIE-strengere regels en de verbondenheidstoets (kleine dochter van grote groep).
**Praktijk-pct**: 10% — wettelijke kern + praktische benoemingsweg.

### 6. `uitvoeren-openbaarmaking-jaarrekening`
**Anchors**: 1.2.IV.F, 1.2.IV
**Motivering**: Concrete procedure (dossier samenstellen → termijn → NBB-Filing → griffie-opvolging). Belangrijk voor stagiair die mogelijk de neerlegging zelf doet.
**Praktijk-pct**: 10%.

### 7. `toepassen-boekhoudbeginselen-op-waarderingsvraagstuk`
**Anchors**: 1.2.V, 1.2.V.A, 1.2.V.B
**Motivering**: De enige competentie die meerdere beginselen samen orchestreert. Geeft stagiair een werkbare procedure: per beginsel toetsen → getrouw-beeld-controle → boeken met grondslag.
**Praktijk-pct**: 20% (HOOGSTE) — beginselen leveren professional judgment, de keuze tussen waardevermindering vs voorziening vs afwijking is geen mechanische beslissing. Net onder de 30%-grens en daarom **geen mens-review flag**, maar wel het hoogste relevante praktijkgehalte in de set.

### 8. `kwalificeren-jaarrekeningregime-vzw-stichting`
**Anchors**: 1.2.IV.A, 1.2.IV, 1.2.III
**Motivering**: VZW-context wordt vaak vergeten. Apart traject met andere drempels (WVV art. 1:28-1:29) en aangepaste schema's. Belangrijk voor stagiair die voor non-profit cliënten werkt.
**Praktijk-pct**: 10%.

### 9. `identificeren-administratieve-autoriteit`
**Anchors**: 1.2.II
**Motivering**: Anker 1.2.II ("Belangrijkste administratieve autoriteiten") verdient een eigen competentie omdat de stagiair vragen vaak moet routeren naar één van CBN/NBB/FSMA/ITAA/IBR/griffie/FOD. Dekt cascade-vragen en routeringsadvies.
**Praktijk-pct**: 15% — bevoegdheden wettelijk vastgelegd; de routerings-keuze zelf is praktijk-oriëntatie. Net binnen de marge.

---

## `gebaseerd_op_concepten` per competentie

| Competentie | gebaseerd_op_concepten (count) |
|---|---|
| identificeren-rechtsbron-boekhoudrecht | 7: belgisch-boekhoudrecht, europees-boekhoudrecht, wetboek-economisch-recht-boek-iii, wetboek-vennootschappen-verenigingen, kb-wvv-uitvoering, cbn-adviezen, rechtspraak-boekhoudrecht |
| kwalificeren-boekhoudplichtige-onderneming | 7: boekhoudplichtige-onderneming, dubbel-boekhouden, vereenvoudigde-boekhouding, regelmatige-boekhouding, minimum-algemeen-rekeningenstelsel, bewaartermijn-boekhouding, wetboek-economisch-recht-boek-iii |
| klasseren-vennootschap-naar-groottecategorie | 4: groottecriteria-jaarrekening, kleine-vennootschap, microvennootschap, vennootschapsvormen-typologie |
| bepalen-jaarrekeningschema | 7: jaarrekening-schema, groottecriteria-jaarrekening, kleine-vennootschap, microvennootschap, kb-wvv-uitvoering, sociale-balans, toelichting-jaarrekening |
| beoordelen-commissaris-verplichting | 6: commissaris, groottecriteria-jaarrekening, kleine-vennootschap, public-interest-entity, ibr, vennootschapsvormen-typologie |
| uitvoeren-openbaarmaking-jaarrekening | 6: openbaarmaking-jaarrekening, nationale-bank-belgie, griffies-ondernemingsrechtbank, jaarrekening-schema, commissaris, jaarverslag |
| toepassen-boekhoudbeginselen-op-waarderingsvraagstuk | 8: voorzichtigheidsbeginsel, continuiteitsbeginsel, oprechtheidsbeginsel, consistentiebeginsel, volledigheidsbeginsel, getrouw-beeld-jaarrekening, waarderingsregels-jaarrekening, aanvullende-boekhoudbeginselen |
| kwalificeren-jaarrekeningregime-vzw-stichting | 6: jaarrekening-vzw-stichting, vennootschapsvormen-typologie, vereenvoudigde-boekhouding, dubbel-boekhouden, groottecriteria-jaarrekening, wetboek-vennootschappen-verenigingen |
| identificeren-administratieve-autoriteit | 9: commissie-boekhoudkundige-normen, nationale-bank-belgie, fsma, itaa, ibr, griffies-ondernemingsrechtbank, fod-financien-boekhoudrecht, public-interest-entity, commissaris |

Alle ≥ 2 — anti-fabricatie-grens gerespecteerd.

---

## `praktijk_pct` per competentie + flags

| Competentie | wettelijk_pct | praktijk_pct | Flag mens-review? |
|---|---:|---:|:---|
| klasseren-vennootschap-naar-groottecategorie | 95 | 5 | nee |
| bepalen-jaarrekeningschema | 95 | 5 | nee |
| identificeren-rechtsbron-boekhoudrecht | 90 | 10 | nee |
| kwalificeren-boekhoudplichtige-onderneming | 90 | 10 | nee |
| beoordelen-commissaris-verplichting | 90 | 10 | nee |
| uitvoeren-openbaarmaking-jaarrekening | 90 | 10 | nee |
| kwalificeren-jaarrekeningregime-vzw-stichting | 90 | 10 | nee |
| identificeren-administratieve-autoriteit | 85 | 15 | nee |
| toepassen-boekhoudbeginselen-op-waarderingsvraagstuk | 80 | 20 | nee |

**Geen flag voor mens-review.** Alle competenties zitten ruim boven 70% wettelijk (de drempel voor recht-context volgens de prompt). De competentie `toepassen-boekhoudbeginselen-op-waarderingsvraagstuk` heeft het hoogste praktijkgehalte (20%) — dat komt door de inherent oordeelmatige aard van beginselen-toepassing (voorzichtigheid, afwijkingsbepaling). Toch ruim binnen de 30%-marge.

Verdeling klopt met verwachting voor recht-context: PO 1.2 is sterk wettelijk verankerd (WER Boek III + WVV Boek 3 + KB-WVV + CBN-adviezen).

---

## Schema 1.1-naleving

| Regel | Status |
|---|---|
| Schema_version: 1.1 | ✓ |
| Status: voorgesteld | ✓ |
| Stap-blok-velden (nr, titel, wat, hoe, grondslag) per stap | ✓ — alle 36 stappen |
| Aanbevolen velden (waarom, input, output) | ✓ — opgenomen in alle stappen |
| `voorbeeld.substappen[]` op stappen die berekenen / klasseren | ✓ — opgenomen bij stappen met klassering-tabel (klasseren-grootte, bepalen-schema, kwalificeren-VZW, klasseren-boekhoudplicht) |
| `valkuilen[]` met `advies` als titel (niet `correctie`) | ✓ |
| Cast-namen uit globaal.yaml | ✓ (Meubelzaak Mertens BV, Rotex Roeselare NV, Oprichtingen Oostende BV, Praktijk Persenaire, Brugse Brouwerij BV, Naaiatelier Ninove BV, VZW Quelle de Vie, Sofie Janssens, Aurelia Holding NV, Transport Tongeren BV, Verffabriek Veurne BV) |
| Geen "M / D / X / Y" abstracte tags | ✓ |
| `gebaseerd_op_concepten` ≥ 2 | ✓ — gemiddeld 6,7 per competentie |
| `procedure_grondslag.wettelijk_pct + praktijk_pct == 100` | ✓ |
| Elke stap heeft `grondslag` | ✓ |
| Wikilinks verwijzen naar bestaande concepten | ✓ — gecheckt tegen records/-map |
| Geen examenvragen als input gebruikt | ✓ — alleen exam_patterns context |
| Stagiair-toon, korte zinnen | ✓ best effort — sommige beslisboom-vragen zijn lang door verwijsstructuur |

---

## Aandachtspunten voor curatie

1. **`toepassen-boekhoudbeginselen-op-waarderingsvraagstuk` — bedragen in voorbeelden zijn illustratief**. Het voorbeeld over de Mertens-vordering (60% × € 18.000 = € 10.800) is een didactische illustratie, geen bron-citaat. Bij curatie nakijken of CBN-advies een concretere casus aandraagt.

2. **Drempelwaarden in voorbeelden**. De cijfers € 11.250.000 / € 6.000.000 / € 900.000 / € 450.000 zijn de actuele 2024-cijfers uit de records — bij update via EU delegated act 2023/2775 zullen records én voorbeelden samen meebewegen. Geen hardcoded cijfers in stap-titels — alle drempelwaarden via wikilink naar [[groottecriteria-jaarrekening]] §drempels.

3. **VZW-drempels in `kwalificeren-jaarrekeningregime-vzw-stichting`**. De gebruikte zeer-klein-drempel (€ 391.000 ontvangsten / € 1.563.000 balanstotaal / 5 personeel) zijn de getallen die voortvloeien uit WVV art. 1:28-1:29 — bij curatie checken tegen het actuele cijferzakboekje, want VZW-drempels lopen achter op vennootschapsdrempels.

4. **Mogelijke 10de competentie** (NIET geschreven, maar te overwegen): `opstellen-statutaire-jaarrekening` als orchestratie van de hele taak 1.2.taak.1 (eindejaarsverrichtingen → schema kiezen → openbaarmaking). Dit zou een 'meta-competentie' worden die de andere oproept. Bewust niet opgenomen om verdunning te vermijden — taak 1.2.taak.1 is al goed gedekt via competenties 3+4+6+7.

5. **Cross-PO competenties**. Vier van de negen competenties hebben raakvlakken met andere POs:
   - `klasseren-vennootschap-naar-groottecategorie` raakt PO 1.4 (consolidatie-grootte) — maar gebruikt andere drempels (WVV art. 1:24 vs 1:26). Cross-link via vergelijkingsparen in records.
   - `beoordelen-commissaris-verplichting` raakt PO 2.x (auditrecht).
   - `toepassen-boekhoudbeginselen-op-waarderingsvraagstuk` raakt PO 1.1 (algemene boekhouding) en PO 1.3 (financiële analyse).
   - `uitvoeren-openbaarmaking-jaarrekening` zit volledig in 1.2.

   Bewust enkel `programmaonderdelen: [1.2]` gezet — als curator een cross-PO-relevantie wil, kan dat later toegevoegd.

---

## Files-locatie

Negen YAML-bestanden in `/Users/stivni/Documents/ITAA/certificaid/data/concepten/competenties/`:

- `identificeren-rechtsbron-boekhoudrecht.yaml`
- `kwalificeren-boekhoudplichtige-onderneming.yaml`
- `klasseren-vennootschap-naar-groottecategorie.yaml`
- `bepalen-jaarrekeningschema.yaml`
- `beoordelen-commissaris-verplichting.yaml`
- `uitvoeren-openbaarmaking-jaarrekening.yaml`
- `toepassen-boekhoudbeginselen-op-waarderingsvraagstuk.yaml`
- `kwalificeren-jaarrekeningregime-vzw-stichting.yaml`
- `identificeren-administratieve-autoriteit.yaml`

Dit rapport: `/Users/stivni/Documents/ITAA/certificaid/data/extractie/1.2/competentie-destillatie-rapport-2026-05-16.md`

Geen commit. Geen Python-scripts. Validatie via inline YAML-parse + structuurchecks (zie samenvatting hierboven).
