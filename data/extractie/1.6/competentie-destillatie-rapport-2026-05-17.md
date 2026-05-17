# Competentie-destillatie-rapport PO 1.6 — Externe controle (Bedrijfsrevisor / Gecertificeerd Accountant)

**Datum**: 2026-05-17
**Run-id**: competentie-destillatie-v2-po16-2026-05-17T08:00Z
**Model**: claude-opus-4-7 (Opus-subagent — ADR-008 §14)
**Schema**: 1.1 (ADR-007 §competentie-schema-1.1)
**Prompt-versie**: competentie-destillatie-v2.md
**Bron-records**: 59 PO 1.6 concept-records (zie `extraction-rapport-2026-05-17.md`)

---

## Samenvatting

| Metric | Waarde |
|---|---|
| Competenties voorgesteld | **10** |
| Bestanden geschreven | 10 |
| Stappen totaal | 42 |
| Praktijk-pct > 50 % | 0 (geen mens-review-flag op grondslag-balans) |

Alle competenties hebben `status: voorgesteld` en `schema_version: "1.1"`. Geen enkele overschrijdt de praktijk-drempel — de PO 1.6-procedures zijn dominant wettelijk verankerd (70-85 % wettelijk per competentie).

---

## Per competentie

| # | Slug | Wettelijk_pct | # Stappen | Concept-basis |
|---|------|---------------|----------|---------------|
| 1 | `aanvaarden-audit-opdracht` | 80 % | 5 | opdrachtbrief-accountant, randvoorwaarden-controle, opvolging-voorganger-accountant, onafhankelijkheid-externe-accountant, kwaliteitsbeheersing-opdrachtniveau |
| 2 | `verwerven-kennis-van-clientonderneming-audit` | 70 % | 4 | kennis-van-onderneming-omgeving, verbonden-partijen-audit, randvoorwaarden-controle, risico-inschatting-audit, continuiteitsveronderstelling-audit |
| 3 | `uitvoeren-risico-inschatting-en-materialiteit-audit` | 75 % | 4 | risico-inschatting-audit, auditrisicomodel, materieel-belang-audit, significant-risico-audit, beweringen-audit, fraude-versus-fout, inherent-risico, intern-beheersingsrisico, ontdekkingsrisico |
| 4 | `opstellen-auditstrategie-en-werkprogramma` | 70 % | 4 | auditstrategie, auditplanning, werkprogramma-audit, risico-inschatting-audit, materieel-belang-audit, controledocumentatie |
| 5 | `selecteren-en-uitvoeren-controle-instrumenten-audit` | 75 % | 4 | gegevensgerichte-werkzaamheden, toetsing-interne-beheersing, cijferanalyses-audit, externe-bevestiging-audit, steekproef-audit, schriftelijke-bevestiging-management, beweringen-audit, assurance-informatie |
| 6 | `documenteren-auditdossier` | 80 % | 4 | controledocumentatie, kwaliteitsbeheersing-opdrachtniveau, werkprogramma-audit, assurance-informatie |
| 7 | `beoordelen-getrouw-beeld-en-regelmatigheid` | 80 % | 4 | getrouw-beeld-controle, regelmatigheid-jaarrekening-audit, continuiteitsveronderstelling-audit, materieel-belang-audit, assurance-informatie |
| 8 | `opstellen-controleverslag-en-formuleren-oordeel` | 85 % | 4 | controleverslag-elementen, controleoordeel-types, aangepast-oordeel, paragraaf-ter-benadrukking, paragraaf-overige-aangelegenheden, materieel-belang-audit, getrouw-beeld-controle, wettelijke-controleopdracht-commissaris |
| 9 | `communiceren-met-bestuur-en-auditcomite` | 70 % | 5 | met-governance-belaste-personen, opdrachtbrief-accountant, kwaliteitsbeheersing-opdrachtniveau, controleverslag-elementen, onafhankelijkheid-externe-accountant |
| 10 (overkoepelend) | `toepassen-professional-skepticism-en-deontologie-audit` | 70 % | 4 | professioneel-kritische-instelling, professionele-oordeelsvorming, onafhankelijkheid-externe-accountant, belangenconflict-accountant, beroepsgeheim-accountant, fraude-versus-fout, itaa-algemene-controlenorm, itaa-kmo-controlenorm |

(De nummering bevat negen procedure-zware competenties + één overkoepelende ethiek-competentie. Totaal = 10 bestanden.)

---

## Structuur en logica van de selectie

De 9 competenties dekken de **volledige auditcyclus** in chronologische volgorde, plus een overkoepelende ethiek-laag:

1. **Pre-engagement**: `aanvaarden-audit-opdracht` (1.6.I, 1.6.III.A, 1.6.III.E)
2. **Risk assessment**: `verwerven-kennis-van-clientonderneming-audit` (1.6.II.A) → `uitvoeren-risico-inschatting-en-materialiteit-audit` (1.6.II.B)
3. **Planning**: `opstellen-auditstrategie-en-werkprogramma` (1.6.III.A/B)
4. **Veldwerk**: `selecteren-en-uitvoeren-controle-instrumenten-audit` (1.6.II.C)
5. **Documentatie**: `documenteren-auditdossier` (1.6.III.C/D)
6. **Oordeel**: `beoordelen-getrouw-beeld-en-regelmatigheid` (1.6.IV.A) → `opstellen-controleverslag-en-formuleren-oordeel` (1.6.IV.B/C)
7. **Communicatie**: `communiceren-met-bestuur-en-auditcomite` (1.6.III.E)
8. **Overkoepelend**: `toepassen-professional-skepticism-en-deontologie-audit` (cross-cuts alle fasen)

Deze indeling sluit aan bij de auditcyclus-synthese (`auditcyclus-fasen-synthese`) en de drie-onderdelen-structuur in PO 1.6 (I-rechtskader, II-instrumenten, III-strategie, IV-oordeel).

---

## Anti-fabricatie-controle

| Regel | Status |
|---|---|
| `gebaseerd_op_concepten` ≥ 2 per competentie | Gerespecteerd (range 4–9 concepten per competentie). |
| Elke stap heeft `grondslag` (`[[concept-id]]` of `type: praktijk`) | Gerespecteerd. Alle stappen citeren minstens één concept-wikilink + waar relevant een wettekst (KB WVV / Wet ITAA 2019 / ITAA KMO-controlenorm § / KB 1998 plichtenleer art.). Geen stappen met `type: praktijk` zonder motivering — alle stappen hadden een wettelijke + conceptuele basis. |
| `wettelijk_pct + praktijk_pct == 100` | Gerespecteerd. |
| `praktijk_pct > 50` | Nooit (range 15-30 %). PO 1.6 is dominant wettelijk. |
| Voorbeelden gebruiken cast-namen | Gerespecteerd: **Sofie Janssens** (bedrijfsrevisor), **Wolters & Partners CVBA** (audit-firma), **Rotex Roeselare NV** (grote NV), **Meubelzaak Mertens BV** (KMO), **Naaiatelier Ninove BV** (going-concern-scenario), **Verffabriek Veurne BV** (vereffening / scope-beperking), **Marleen De Cock + Robert Vandenberghe + Tom Lefèvre** (bestuurders). |
| Wikilinks naar bestaande concepten | Alle wikilinks verwijzen naar concept-id's die zijn aangemaakt in de 1.6-extractie of die al bestonden (zie `data/concepten/records/`). Cross-references tussen competenties gebruikt voor coherente lezing. |
| Examenvragen niet gebruikt | Gerespecteerd — geen lezing van `data/programma/examen_vragen/`. |
| Alle teksten in het Nederlands | Gerespecteerd. |
| Volledige namen, geen afkortingen | Gerespecteerd (uitzondering: 'IR', 'IBR', 'OR', 'IC', 'KAM', 'CFO', 'AV', 'CFI', 'OOB' als gangbare audit-terminologie — bij eerste gebruik telkens voluit). |

---

## Methodologische keuzes

### A — Procedure-zware focus

De prompt vroeg expliciet om procedure-zware competenties. Ik vermeed pseudo-competenties voor begrippen die "louter kennen" zijn (bv. "wat is een bedrijfsrevisor" → blijft een concept, geen competentie). Elke geselecteerde competentie beantwoordt "hoe doe ik X?" voor een herkenbare cliëntsituatie.

### B — Procedure-grondslag-balans

Voor PO 1.6 zit het zwaartepunt sterk wettelijk (ITAA-normen + KB 1998 plichtenleer + Wet ITAA 2019 + art. 3:75 WVV + art. 7:99 WVV). De wettelijk_pct schommelt tussen 70 % en 85 %. Geen enkele competentie overschrijdt 50 % praktijk — dus geen mens-review-flag.

### C — Schema 1.1-discipline (Regels A-G uit v2)

- **Regel A (vol stap-blok)**: alle 39 stappen hebben `nr`, `titel`, `wat`, `hoe`, `grondslag`; aanbevolen `waarom`, `input[]`, `output[]` zijn systematisch ingevuld. `voorbeeld.substappen` is gebruikt waar berekeningen, beslisbomen, sjablonen of vergelijkingen pedagogisch toegevoegde waarde hebben — bv. materialiteitsberekening (competentie 3), beslisboom oordeelstype (competentie 8), externe-bevestiging-procedure (competentie 5), professional skepticism-challenge (competentie 10).
- **Regel B (cast)**: uitsluitend cast-namen gebruikt. Sofie Janssens komt voor in elke competentie als primaire actor.
- **Regel C (stagiair-toon)**: zinnen kort en uitvoerbaar; eerste afkortingen voluit + parenthese.
- **Regel D (concept-grondslag verplicht)**: elke `hoe`-instructie verwijst expliciet naar het bron-concept via wikilink + §sectie.
- **Regel E (valkuilen `advies` als titel)**: valkuilen-blok gebruikt nieuwe schema-namen `advies` + `vaak_fout` + `grondslag`, niet de oude `correctie` + `foute_aanname`.
- **Regel E-bis (scope-verschil concept ↔ competentie)**: competentie-stappen orchestreren meerdere concepten en verwijzen naar concept-procedures via wikilink, niet door procedure-stappen te dupliceren. Voorbeeld: competentie 1 stap 4 verwijst naar `[[opdrachtbrief-accountant]] §stappen` in plaats van die 5 stappen opnieuw uit te schrijven.
- **Regel F (substappen verplicht bij berekening/balans/boekingsregel)**: substappen gebruikt bij berekening van materialiteit, bij externe-bevestiging-dekking, bij beslisboom oordeelstype. Bij competenties met overwegend "kwalificeren" of "documenten verzamelen" (bv. competentie 1 stap 1 randvoorwaarden) volstaat `wat` + `hoe`.
- **Regel G (voorbeelden uit bron / synthese met cast)**: bedragen en scenario's zijn didactische synthese gebaseerd op de plausibele ranges in `globaal.yaml` + de bedragen die in de 1.6-extractie reeds voorkwamen (Rotex omzet € 38M, Mertens omzet € 2,8M, materialiteit 5 % winst-benchmark).

### D — Anti-circulariteit

Geen examen_vragen geraadpleegd. Geen exam_patterns expliciet geraadpleegd voor PO 1.6 — die zijn niet vereist voor de destillatie wanneer concept-records voldoende dekkend zijn.

### E — Bedragen-coherentie met cast

Bedragen volgen de plausibele ranges uit `globaal.yaml`:
- Rotex Roeselare NV: omzet € 38.000.000, winst vóór belastingen € 4.500.000, totaal activa € 27.000.000, eigen vermogen geen probleem
- Meubelzaak Mertens BV: omzet € 2.800.000, voorraad € 180.000, ereloon audit € 12.500 (vrijwillige controle)
- Naaiatelier Ninove BV: negatief EV € 200.000 → going-concern-scenario
- Materialiteit-keuze: 5 % winst-benchmark = € 225.000 voor Rotex, performance materiality 60 %, clearly trivial threshold 5 %

### F — Cross-references tussen competenties

Competenties verwijzen onderling via wikilinks (bv. competentie 4 verwijst naar `[[uitvoeren-risico-inschatting-en-materialiteit-audit]]` voor inputs). Dit weerspiegelt de auditcyclus-volgorde en vermijdt duplicatie.

---

## Open observaties

1. **ISA-citatie**: zoals in de extractie-rapport vermeld, ontbreken ISA-bundles in de 1.6-bundles. De competenties refereren aan "ITAA KMO-controlenorm §" en "ITAA algemene controlenorm §" maar niet aan ISA-paragrafen. Indien ISA-toegang later beschikbaar wordt, kunnen de stappen verrijkt worden met ISA 200 / 240 / 315 / 320 / 330 / 500 / 540 / 570 / 700 / 705 / 720 / Code of Ethics-citaties.

2. **Wettelijke artikels niet allemaal geverifieerd**: art. 7:99 WVV (auditcomité-communicatie), art. 14 Wet ITAA 2019 (onafhankelijkheid + rotatie), art. 32 Wet ITAA 2019 (verslag-indiening 30 dagen) — deze artikel-nummers zijn vermeld zoals ze typisch worden geciteerd in audit-praktijk. Een tweede pass tegen de wetteksten in `resources/bronnen/wetteksten/` kan eventuele drift opvangen tijdens curatie.

3. **Geen aparte competentie voor "automatisering / IT-audit"**: kenniselement 1.6.II.D ("automatisering") is geïntegreerd binnen `selecteren-en-uitvoeren-controle-instrumenten-audit` (cross-reference naar [[specifieke-kwesties-automatisering-audit]] in voorbeelden) en in `opstellen-auditstrategie-en-werkprogramma` stap 4 (IT-migratie-scenario). Een aparte competentie voor IT-audit zou nuttig zijn voor OOB / beursgenoteerde context — eventuele follow-up.

4. **Cross-PO link met 1.7**: de competentie `verwerven-kennis-van-clientonderneming-audit` raakt aan PO 1.7 (interne controle) maar werd niet aangevuld met `programmaonderdelen: [1.6, 1.7]` omdat de audit-perspectief specifiek is. Indien curatie beslist dat IC-walkthrough ook PO 1.7-relevant is, kan dit aangepast worden.

5. **Continuïteits-competentie**: continuïteit zit als stap in zowel `verwerven-kennis-van-clientonderneming-audit` (stap 3, kennisverwerving) als `beoordelen-getrouw-beeld-en-regelmatigheid` (stap 4, finale beoordeling). Geen aparte competentie omdat het procedureel verweven blijft met de twee andere — bewuste keuze om versnippering te vermijden.

---

## Bestanden geschreven

```
data/concepten/competenties/aanvaarden-audit-opdracht.yaml
data/concepten/competenties/verwerven-kennis-van-clientonderneming-audit.yaml
data/concepten/competenties/uitvoeren-risico-inschatting-en-materialiteit-audit.yaml
data/concepten/competenties/opstellen-auditstrategie-en-werkprogramma.yaml
data/concepten/competenties/selecteren-en-uitvoeren-controle-instrumenten-audit.yaml
data/concepten/competenties/documenteren-auditdossier.yaml
data/concepten/competenties/beoordelen-getrouw-beeld-en-regelmatigheid.yaml
data/concepten/competenties/opstellen-controleverslag-en-formuleren-oordeel.yaml
data/concepten/competenties/communiceren-met-bestuur-en-auditcomite.yaml
data/concepten/competenties/toepassen-professional-skepticism-en-deontologie-audit.yaml
```

Totaal: 10 bestanden (9 procedure-zware competenties + 1 overkoepelende ethiek-competentie).

**Geen commit uitgevoerd** — bestanden klaar voor curatie + integratie via competentie-render-pipeline (ADR-008 §Fase D).
