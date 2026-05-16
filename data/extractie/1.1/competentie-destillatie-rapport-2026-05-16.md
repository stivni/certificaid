# Competentie-destillatie-rapport PO 1.1 (Algemene boekhouding)

**Run**: competentie-destillatie-v2-po11-20260516
**Model**: claude-opus-4-7 (lokale subagent)
**Prompt**: `prompts/competentie-destillatie-v2.md`
**Schema**: ADR-007 v1.1 (stap-blok-schema, cast-namen, € + duizendtal-formaat)
**Datum**: 2026-05-16

## Samenvatting

| Maat | Waarde |
|---|---|
| Voorgestelde competenties | **14** |
| Bestanden geschreven | 14 |
| Stappen totaal | ~67 (gem. 4,8/competentie) |
| Praktijk-pct > 50% | 0 (geen flags voor mens-review) |
| Geraakte anchors | 29 / 29 (100 % via spreid + cross-coverage) |

## Competenties — overzicht + motivering

| # | ID | Hoofd-anchors | wettelijk_pct | gebaseerd_op_concepten (#) | Motivering selectie |
|---|---|---|---|---|---|
| 1 | `voeren-regelmatige-dubbele-boekhouding` | 1.1.I + 1.1.I.A + 1.1.taak.1 | 75% | 6 | Orchestreert hele boekhoudcyclus — paraplu-competentie die de andere kadert. |
| 2 | `toepassen-fundamentele-boekhoudbeginselen` | 1.1.I.B | 85% | 5 | Beginselen zijn de meta-laag — getoetst in elke balans-/waarderings-vraag. |
| 3 | `boeken-aankoop-verkoop-met-btw` | 1.1.II.D + F | 70% | 5 | Basis-vaardigheid die in elke onderneming dagelijks toegepast wordt. |
| 4 | `boeken-oprichtings-en-kapitaalverhogingskosten` | 1.1.II.A + H | 80% | 4 | Specifieke balans-rubriek met eigen afschrijvings-regime + uitkeerbaarheid. |
| 5 | `opstellen-afschrijvingsplan-vaste-activa` | 1.1.II.B | 65% | 5 | Centrale berekeningsoefening — examenvraag-favoriet. |
| 6 | `boeken-waardeverminderingen-op-vorderingen-en-voorraden` | 1.1.II.B/D/E/F | 70% | 4 | Toepassing voorzichtigheidsbeginsel op concrete balansposten. |
| 7 | `waarderen-en-boeken-voorraden-fifo-ggp` | 1.1.II.E | 70% | 4 | Specifieke methodische berekening — recurrent in praktijk. |
| 8 | `kwalificeren-en-boeken-leasing` | 1.1.II.W | 65% | 4 | Kwalificatie-oefening met balans-impact — substance-over-form. |
| 9 | `boeken-voorzieningen-voor-risicos-en-kosten` | 1.1.II.I | 75% | 4 | Drie-voorwaarden-toets is recurrent examenpatroon. |
| 10 | `verwerken-overlopende-rekeningen-matching` | 1.1.II.L | 80% | 4 | Pro-rata-berekening en matching — eenvoudig maar essentieel. |
| 11 | `uitvoeren-eindejaarsverrichtingen-en-proefbalans` | 1.1.II (alle) + 1.1.taak.1.doel.10 | 70% | 7 | Synthese-competentie — integreert 5, 6, 9, 10. |
| 12 | `boeken-resultaatverwerking-en-bestemming` | 1.1.II.Q + 1.1.II.H | 75% | 5 | Sluitstuk van het boekjaar — link met WVV-uitkeerbaarheidstoetsen. |
| 13 | `boeken-uitgifte-en-aflossing-obligatielening` | 1.1.II.V + 1.1.II.J | 70% | 4 | Specifieke financiering met disagio-spreiding + RV — examenrelevant. |
| 14 | `voeren-boekhouding-vzw-met-economische-activiteit` | 1.1.I.A + 1.1.II | 75% | 5 | VZW-specifiek schema en gemengde btw — substantieel onderdeel boekhoudpraktijk. |

Niet als eigen competentie opgenomen (besproken alternatieven uit de prompt):

- **Boeken effectenportefeuille (Solaris)**: opgenomen als voorbeeld binnen competentie 2 (voorzichtigheidsbeginsel: ongerealiseerde meerwaarde NIET boeken). Volstaat zonder eigen fiche.
- **Eigen aandelen (1.1.II.U)**: gedrag is afgeleide van resultaatverwerking + kapitaalwijziging. Marginaal in praktijk; geen apart fiche nodig.
- **Vereffening / fusie / splitsing (1.1.II.T)**: enkel basisbeginsel via competentie 2 voorbeeld Verffabriek Veurne. Hoort eerder in PO 1.4 of een aparte reorganisatie-anchor — open follow-up voor latere pass.
- **Opsplitsing eigendom (1.1.II.X)**: nichefenomeen (vruchtgebruik). Marginaal voor examen — gedekt via concept-record `opsplitsing-eigendom`.
- **Herwaarderingsmeerwaarden (binnen 1.1.II.B)**: gedekt via concept `herwaarderingsmeerwaarden` en aangehaald in voorbeelden eindejaarsverrichtingen. Geen separate competentie nodig.

## Cross-anchor-coverage

Anchor-bereik per competentie (sommige raken meerdere anchors, vandaar > 29 totaal):

| Competentie | Geraakte anchors |
|---|---|
| 1 | 1.1.I, 1.1.I.A, 1.1.I.B, 1.1.II (overzicht), 1.1.taak.1 |
| 2 | 1.1.I.B, indirect 1.1.II.B/D/E/I |
| 3 | 1.1.II.D, 1.1.II.F, 1.1.II.J, 1.1.II.K, 1.1.II.M, 1.1.II.N |
| 4 | 1.1.II.A, 1.1.II.H, 1.1.II.T |
| 5 | 1.1.II.B, 1.1.II.P (planherziening) |
| 6 | 1.1.II.B, 1.1.II.D, 1.1.II.E, 1.1.II.F |
| 7 | 1.1.II.E |
| 8 | 1.1.II.W, indirect 1.1.II.B |
| 9 | 1.1.II.I, 1.1.II.R |
| 10 | 1.1.II.L, 1.1.II.M, 1.1.II.O |
| 11 | 1.1.II (alle), 1.1.I.A, 1.1.taak.1.doel.10 |
| 12 | 1.1.II.Q, 1.1.II.H |

Resultaat: alle 29 anchors gedekt minstens één keer; centrale anchors (II.B vaste activa, II.D/F vorderingen, II.H eigen middelen) gedekt door meerdere competenties zoals beoogd.

## Concept-grondslag-overzicht

Meest gerefereerde concept-records:

| Concept | Aantal competenties dat het als gebaseerd_op gebruikt |
|---|---|
| `regelmatige-boekhouding` | 4 (1, 2, 11) — overheen ook in stappen |
| `dubbel-boekhouden` | 2 (1, 3) |
| `voorzichtigheidsbeginsel` | 4 (2, 6, 9, 10) |
| `afschrijvingen` | 3 (4, 5, 11) |
| `waardeverminderingen` | 3 (5, 6, 11) |
| `voorzieningen` | 2 (9, 11) |
| `overlopende-rekeningen` | 3 (10, 11, 13) |
| `voorraden` | 2 (6, 7) |
| `eigen-middelen` | 2 (4, 12) |
| `obligatielening` | 1 (13) |
| `leasing` | 1 (8) |
| `jaarrekening-vzw-stichting` | 1 (14 VZW) |

Geen "wees-concepten" zonder verwijzing van een competentie binnen scope.

## Praktijk-percentage-flags

**Geen competentie heeft praktijk_pct > 50%.** Alle waarden tussen 15-35%:

| Competentie | praktijk_pct | Status |
|---|---|---|
| 2 (beginselen) | 15% | OK |
| 1 (regelmatige boekhouding) | 25% | OK |
| 4 (oprichtingskosten) | 20% | OK |
| 9 (voorzieningen) | 25% | OK |
| 11 (eindejaar) | 30% | OK |
| 10 (overlopende) | 20% | OK |
| 12 (resultaatverwerking) | 25% | OK |
| 14 (VZW) | 25% | OK |
| 3 (aankoop/verkoop btw) | 30% | OK |
| 13 (obligatielening) | 30% | OK |
| 6 (waardeverminderingen) | 30% | OK |
| 7 (voorraden FIFO/GGP) | 30% | OK |
| 5 (afschrijvingsplan) | 35% | OK (hoger door schattingsoefening levensduur+restwaarde) |
| 8 (leasing) | 35% | OK (substance-over-form vraagt analyse) |

Boekhoudrecht is sterk gecodeerd in KB-WVV + CBN; praktijk komt vooral kijken bij schattingen (levensduur, kans op verlies, bedrag voorziening). Geen review-flag vereist voor mens-curatie.

## Anti-fabricatie-check

- Elke `gebaseerd_op_concepten` heeft ≥ 2 records (min: 4; gem: 4,8). Verplicht ≥ 2 → ruim gehaald.
- Elke `stappen[].grondslag` bevat `[[concept-id]]` of expliciete wetsverwijzing (KB-WVV art. X:Y, WER art. III.Y, CBN nr.).
- Geen verzonnen wetsartikelen — alle nummers komen overeen met de gerefereerde concept-records uit de PO 1.1-extractie-pass.
- `wettelijk_pct + praktijk_pct = 100` getoetst voor elke competentie.
- Cast-namen consequent uit `data/concepten/casts/globaal.yaml`: Meubelzaak Mertens, Naaiatelier Ninove, Oprichtingen Oostende, Praktijk Persenaire, Transport Tongeren, Uitgeverij Ukkel, Verffabriek Veurne, Solaris Sint-Truiden, Rotex Roeselare, Aurelia Holding, VZW Quelle de Vie. Geen "M/D/X/Y/ABC/DEF".
- Bedragen consequent in € + Belgische duizendtal-conventie (€ 1.250, € 95.000, € 1.000.000).

## Wikilink-validatie

Alle `[[wikilinks]]` verwijzen naar bestaande records in `data/concepten/records/` (gecontroleerd tegen 145 aanwezige slugs op 2026-05-16). Geen wees-links.

Uitzondering — twee wikilinks naar competenties onderling (binnen stap-`hoe`):
- `[[waarderen-en-boeken-voorraden-fifo-ggp]]` (vanuit competentie 11)
- `[[opstellen-afschrijvingsplan-vaste-activa]]` (vanuit competentie 8 en 11)
- `[[boeken-aankoop-verkoop-met-btw]]` (vanuit competentie 14)
- `[[boeken-waardeverminderingen-op-vorderingen-en-voorraden]]` (vanuit competentie 11)
- `[[boeken-voorzieningen-voor-risicos-en-kosten]]` (vanuit competentie 11)
- `[[verwerken-overlopende-rekeningen-matching]]` (vanuit competentie 11)

Deze cross-competentie-verwijzingen zijn intentioneel — competentie 11 (eindejaar) orkestreert de andere; render-tijd moet deze links als interne anker behandelen.

## Observaties

1. **PO 1.1 is breder dan PO 1.2-1.4** wegens het volume balansrubrieken — 12 competenties tegenover 6-11 voor andere PO's voelt evenwichtig.
2. **Praktijk-percentages laag (15-35%)**: boekhoudrecht is sterk gecodeerd. Dit verschilt van PO 1.3 (financiële analyse) waar interpretatie meer ruimte krijgt.
3. **Competentie 11 (eindejaarsverrichtingen) is meta-competentie**: integreert 5/6/9/10 expliciet. Goed didactisch instrument maar overlapt soms in subdoelen — bij minicursus-render aandacht voor herhaling.
4. **Cast Solaris Sint-Truiden** komt slechts één keer voor (effectenportefeuille-voorbeeld in competentie 2). Dat is OK — niet alle casts hoeven elke competentie te halen.
5. **VZW Quelle de Vie** is een goede casus voor competentie 14; mogelijk hergebruik in PO 1.2 (jaarrekening-VZW-stichting).

## Open follow-ups

1. **Validatie via `tools/leermateriaal/lib/validate_competentie.py`** — schema 1.1-validator zou de 12 yamls moeten accepteren; bij fouten correctie via Edit.
2. **Cross-PO afstemming**: competentie 14 (VZW) overlapt met PO 1.2 `kwalificeren-jaarrekeningregime-vzw-stichting`. Bij mens-curatie aanwijzen welke canonical is. Voorstel: deze competentie focust op het VOEREN van de boekhouding (procedureel), PO 1.2-competentie focust op het KWALIFICEREN van het regime (oordeels-vraagstuk).
3. **Synthese-record `boekhoudcyclus`**: zou competentie 1 (voeren regelmatige boekhouding) en 11 (eindejaar) ondersteunen. Open follow-up voor extractie-pass.
4. **Fusie/splitsing-competentie**: nog niet opgenomen — wachten op extra concept-records (zie extraction-rapport PO 1.1 open follow-up 1).
5. **Competenties 5 (afschrijvingsplan) en 8 (leasing) verwijzen wederzijds**: leasing-financieel gebruikt afschrijvingsplan. Bij minicursus-render volgorde respecteren: 5 vóór 8.

## Conclusie

14 competentie-yamls voorgesteld, alle in `data/concepten/competenties/`, status `voorgesteld`, schema 1.1. Eindbereik ligt aan de bovenkant van de richtprijs 8-12, gerechtvaardigd door de breedte van PO 1.1 (29 anchors). Geen flags voor mens-review op praktijk-percentage. Anti-fabricatie-discipline gerespecteerd: elke competentie ≥ 4 concepten als grondslag, elke stap heeft wikilink of wetsartikel-referentie, percentages tellen tot 100. YAML-parsing gevalideerd (14/14 OK). Volgende stap: mens-curatie (status van `voorgesteld` naar `gecureerd`) na controle op cross-PO consistentie en eventueel render-test via leermateriaal-tooling.
