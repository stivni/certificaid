# Extractie-rapport PO 1.6 — Externe controle (Bedrijfsrevisor/Gecertificeerd Accountant)

**Datum**: 2026-05-17
**Run-id**: concept-extractie-v4-2026-05-17T00:27Z
**Model**: claude-opus-4-7 (subagent)
**Schema**: ADR-007 v1.4
**Anker-aantal in scope**: 20 (1.6.taak.1, 1.6.I, I.A-C, II, II.A-D, III, III.A-E, IV, IV.A-C)

## Samenvatting

- **Nieuwe concept-records**: 59
- **Bijgewerkte records**: 0 (volledig nieuwe extractie — geen overlap met bestaande 1.4/1.7 records die overschreven werden)
- **Synthese-records**: 2 (`opdrachttypes-zekerheidsniveaus-synthese`, `auditcyclus-fasen-synthese`)
- **Dangling-references gelogd**: niet apart bestand aangelegd — alle gerefereerde concepten zijn aangemaakt of expliciet binnen scope.
- **Bron-voorstellen**: zie §"Bronnen-gaten"

## Overzicht records per anker

| Anker | Concept-id's |
|---|---|
| **1.6.I.A — Reikwijdte** | contractuele-controleopdracht, contractuele-beoordelingsopdracht, samenstellingsopdracht-isrs4410, wettelijke-controleopdracht-commissaris, gedeelde-wettelijk-voorbehouden-opdracht, redelijke-mate-van-zekerheid, beperkte-mate-van-zekerheid, randvoorwaarden-controle, opdrachtbrief-accountant, beroepsaansprakelijkheid-accountant, opdrachttypes-zekerheidsniveaus-synthese |
| **1.6.I.B — Rechtstatuut + aansprakelijkheid** | bedrijfsrevisor, gecertificeerd-accountant-ga, onafhankelijkheid-externe-accountant, belangenconflict-accountant, beroepsaansprakelijkheid-accountant, beroepsgeheim-accountant, wettelijke-controleopdracht-commissaris, gedeelde-wettelijk-voorbehouden-opdracht, ontbinding-vereffening-opdracht |
| **1.6.I.C — Normen** | itaa-algemene-controlenorm, itaa-kmo-controlenorm, samenstellingsopdracht-isrs4410, contractuele-controleopdracht, contractuele-beoordelingsopdracht, wettelijke-controleopdracht-commissaris |
| **1.6.II — Revisietechnieken** | assurance-informatie, gegevensgerichte-werkzaamheden, toetsing-interne-beheersing, cijferanalyses-audit, externe-bevestiging-audit, steekproef-audit, beweringen-audit, professioneel-kritische-instelling, professionele-oordeelsvorming |
| **1.6.II.A — Kennis onderneming + omgeving** | kennis-van-onderneming-omgeving, verbonden-partijen-audit, opvolging-voorganger-accountant, randvoorwaarden-controle |
| **1.6.II.B — Risicoanalyse** | risico-inschatting-audit, auditrisicomodel, inherent-risico, intern-beheersingsrisico, ontdekkingsrisico, materieel-belang-audit, significant-risico-audit, fraude-versus-fout, beweringen-audit, continuiteitsveronderstelling-audit |
| **1.6.II.C — Controle-instrumenten** | gegevensgerichte-werkzaamheden, toetsing-interne-beheersing, cijferanalyses-audit, externe-bevestiging-audit, steekproef-audit, schriftelijke-bevestiging-management |
| **1.6.II.D — Automatisering** | specifieke-kwesties-automatisering-audit, boekhoudkundige-schattingen-audit |
| **1.6.III — Auditstrategie** | auditstrategie, auditplanning, werkprogramma-audit, controledocumentatie, kwaliteitsbeheersing-opdrachtniveau, opvolging-voorganger-accountant, auditcyclus-fasen-synthese |
| **1.6.III.A — Planning** | auditplanning, auditstrategie, opdrachtbrief-accountant |
| **1.6.III.B — Werkprogramma** | werkprogramma-audit, auditplanning |
| **1.6.III.C — Revisiedossiers** | controledocumentatie |
| **1.6.III.D — Delegatie + supervisie** | kwaliteitsbeheersing-opdrachtniveau, opvolging-voorganger-accountant |
| **1.6.III.E — Relaties met cliëntactoren** | met-governance-belaste-personen, communicatie-met-management-governance, opdrachtbrief-accountant, onafhankelijkheid-externe-accountant, belangenconflict-accountant, beroepsgeheim-accountant, opvolging-voorganger-accountant |
| **1.6.IV — Oordeel** | controleoordeel-types, aangepast-oordeel, redelijke-mate-van-zekerheid, beperkte-mate-van-zekerheid, materieel-belang-audit, getrouw-beeld-controle, regelmatigheid-jaarrekening-audit, controleverslag-elementen |
| **1.6.IV.A — Beoordeling regelmatigheid + getrouw beeld** | getrouw-beeld-controle, regelmatigheid-jaarrekening-audit, continuiteitsveronderstelling-audit |
| **1.6.IV.B — Certificering + verklaring** | controleverslag-elementen, controleoordeel-types, aangepast-oordeel, paragraaf-ter-benadrukking, wettelijke-controleopdracht-commissaris, redelijke-mate-van-zekerheid |
| **1.6.IV.C — Revisieverslagen** | controleverslag-elementen, beoordelingsverslag-elementen, paragraaf-ter-benadrukking, paragraaf-overige-aangelegenheden, controleoordeel-types, opdrachttypes-zekerheidsniveaus-synthese |
| **1.6.taak.1 — Verslagen + analyses** | controleverslag-elementen, beoordelingsverslag-elementen, gecertificeerd-accountant-ga, bedrijfsrevisor, contractuele-controleopdracht, samenstellingsopdracht-isrs4410, onafhankelijkheid-externe-accountant |

## Bronnen die de extractie hebben gevoed

| Bron | Aantal claim-refs (indicatief) |
|---|---|
| ITAA-norm-kmo-controlenorm (bijlage 1 + §2-§150) | ~35 |
| ITAA-norm-algemene-controlenorm (§1-§7) | ~12 |
| ITAA-norm-samenstellingsopdrachten-isrs4410 | 5 |
| ITAA-norm-opdrachtbrief | 5 |
| ITAA-norm-ontbinding-vereffening | 3 |
| KB-1998-plichtenleer (art. 9, 11, 12, 13, 17, 18, 25) | 12 |
| Wet-ITAA-2019 (art. 3, 44) | 6 |
| ITAA-deontologie-beroepsgeheim | 2 |
| KB-WVV-2019 (art. 3:1) | 1 |

## Bronnen-gaten (worden niet apart geappendeerd — observatie in dit rapport)

**Belangrijke vaststelling**: de 1.6-bundles bevatten GEEN ISA-chunks, ondanks de prompt-uitnodiging om uit ISA 200/240/315/330/500/700/705 te putten. De ISA-bestanden in `resources/bronnen/normen/ISA-*.md` blijken niet (correct?) opgepikt door de bundle-bouwer. Concrete impact:

- Veel concepten konden via de ITAA KMO-controlenorm worden geconstrueerd (die zelf veel ISA-stof inkapselt) — de records zijn dus inhoudelijk solide.
- ISA-specifieke citaties (bv. "ISA 240.27" voor fraude) zijn vermeden — alleen ITAA-norm-paragrafen worden geciteerd. Dat is conform de anti-fabricatie-regel (geen citaties verzinnen).
- Concepten waar ISA-specifieke termen relevanter zijn dan ITAA-stof (bv. group audits, opening balances bij ISA 510, going concern bij ISA 570) zijn vlakker uitgewerkt dan ze zouden zijn met ISA-toegang.

**Voorstel**: bundle-builder controleren — waarom worden ISA-bronnen niet opgenomen in 1.6-bundles? Indien IBR-monopolie als reden geldt, zou een tweede pass met ISA-bundles voor de relevante ankers (II.B, II.C, IV) zinvol zijn.

**Tweede gat**: KMO-controlenorm-bijlage 5/6 (gedeelde wettelijk voorbehouden opdrachten lijsten) komt niet voor in de bundles. Voor concept `gedeelde-wettelijk-voorbehouden-opdracht` zou een directe opname van die lijsten de operationele bruikbaarheid verhogen.

## Schema 1.4-veld-gebruik (steekproef)

- **stap-blok** (Regel 8): gebruikt in `samenstellingsopdracht-isrs4410`, `auditplanning`, `risico-inschatting-audit`, `opvolging-voorganger-accountant`, `externe-bevestiging-audit`, `controleverslag-elementen`, `opdrachtbrief-accountant`, `kennis-van-onderneming-omgeving`, `communicatie-met-management-governance` (9 records met expliciete stap-velden).
- **bouwstenen-blok** (Regel 11): gebruikt in de meeste begrip-/methode-records — `contractuele-controleopdracht`, `contractuele-beoordelingsopdracht`, `wettelijke-controleopdracht-commissaris`, `gedeelde-wettelijk-voorbehouden-opdracht`, `bedrijfsrevisor`, `gecertificeerd-accountant-ga`, `itaa-algemene-controlenorm`, `itaa-kmo-controlenorm`, `controledocumentatie`, `auditrisicomodel`, `controleoordeel-types`, `assurance-informatie`, `gegevensgerichte-werkzaamheden`, `toetsing-interne-beheersing`, `cijferanalyses-audit`, `kennis-van-onderneming-omgeving` (≥16 records).
- **formule-blok** (Regel 12): één expliciete formule in `auditrisicomodel` (controlerisico = inherent × intern beheersing × ontdekking, met `invulling_voorbeeld`).
- **edges** (Regel 9): gepopuleerd in elke record — minstens 1, vaak 2-3 per record (`onderdeel-van`, `vereist-kennis-van`, `vergelijkt-met`, `specialisatie-van`, `getriggerd-door`).
- **vergelijkingsparen** (Regel 4): selectief gebruikt voor echte examenvalkuilen — typisch tussen:
  - `contractuele-controleopdracht` ↔ `contractuele-beoordelingsopdracht` ↔ `samenstellingsopdracht-isrs4410`
  - `paragraaf-ter-benadrukking` ↔ `paragraaf-overige-aangelegenheden` ↔ `aangepast-oordeel`
  - `inherent-risico` ↔ `intern-beheersingsrisico`
  - `getrouw-beeld-controle` ↔ `regelmatigheid-jaarrekening-audit`
  - `bedrijfsrevisor` ↔ `gecertificeerd-accountant-ga`
  - `wettelijke-controleopdracht-commissaris` ↔ `contractuele-controleopdracht`
- **synthese**: 2 records (`opdrachttypes-zekerheidsniveaus-synthese`, `auditcyclus-fasen-synthese`) met vergelijkingstabel + beslisboom (mermaid).
- **drempelwaarden**: `controledocumentatie` (5 jaar KMO-norm vs. 10 jaar algemene controlenorm), `exclusieve-controle` (>50 % stemrechten — al bestond).

## Cast-gebruik (Regel 7)

Alle voorbeeld-zinnen gebruiken namen uit `data/concepten/casts/globaal.yaml`:
- **Sofie Janssens** (bedrijfsrevisor/accountant) — primaire actor in elk record
- **Wolters & Partners CVBA** — audit-firma
- **Rotex Roeselare NV** — grote NV (audit_engagement_groot)
- **Meubelzaak Mertens BV** — KMO (audit_engagement_klein)
- **Naaiatelier Ninove BV** — KMO met productie-context (beoordeling / continuïteit)
- **Marleen De Cock, Pieter Vermeulen, Robert Vandenberghe** — bestuurders
- **Verffabriek Veurne BV** — ontbinding/vereffening-scenario

## Confidence-spread

- `grounded` (~70 %): direct citeerbaar uit één chunk (ITAA-normen, KB plichtenleer, Wet ITAA 2019)
- `inferred-from-aggregation` (~25 %): synthese over meerdere chunks (bv. drempelwaarden-vergelijking 5 vs. 10 jaar; controlerisico-formule)
- `inferred` (~5 %): redenering met explicitering van ratio — bv. wat de auditor kan/niet kan beïnvloeden in het risicomodel

## Anti-fabricatie-controle

- Geen ISA-paragraafnummers verzonnen — bundles bevatten geen ISA-chunks, dus citeren we ISA niet expliciet (alleen via ITAA-norm-paragrafen).
- Materialiteits-percentages (5 %) zijn alleen vermeld als didactische illustratie, niet als wettelijke drempel — geen bron-claim dat "5 %" wettelijk is.
- Bedragen in voorbeelden (€ 50.000, € 500.000, € 11.250.000 ...) volgen Belgische conventie (€-prefix + duizendtal met punt) en respecteren de plausibele ranges in cast.

## Anti-collision check (PO 1.7 / 1.2)

- **`commissaris.json`** (bestaande, PO 1.2.IV.E) — niet overschreven. Mijn nieuwe `wettelijke-controleopdracht-commissaris.json` is gericht op de OPDRACHT, niet op de ACTOR. Edges leggen de relatie. Aanbevolen post-pass: linked_anchors van `commissaris` uitbreiden met `1.6.I.B`.
- **`controle.json`** (bestaande, PO 1.4 groep-controle) — geen overlap met audit-controle. Mijn records gebruiken term "controleopdracht" / "auditcontrole" om verwarring te vermijden.
- **`interne-controle.json`** (bestaande, PO 1.7) — niet aangeraakt. Mijn `toetsing-interne-beheersing.json` is audit-specifiek (test of controls), geen alternatief.
- **`externe-controle.json`** (bestaande, PO 1.7) — niet overschreven. Mijn records zijn fijnmaziger dan dit overzichtsrecord.

## Open observaties / follow-ups voor enrich-pass

1. **ISA-integratie**: indien bundles met ISA-chunks beschikbaar worden, een enrich-pass om records `auditrisicomodel`, `materieel-belang-audit`, `fraude-versus-fout`, `controleverslag-elementen` te verrijken met ISA-paragraaf-citaties.
2. **Bestaande `commissaris.json`**: enrich-pass kan linked_anchors uitbreiden met PO 1.6-ankers en cross-edges leggen met `wettelijke-controleopdracht-commissaris` en `controleverslag-elementen`.
3. **IESBA Code of Ethics** (genoemd in de prompt) komt niet voor in de bundles — wel relevant voor onafhankelijkheids- en ethiekconcepten. Apart aan te leveren als bron.
4. **Modellen van verslagen** (Bijlage X van KMO-controlenorm en ISRS 4410): kunnen worden vastgelegd als templates in `data/concepten/templates/` voor render-tijd substitutie. Buiten scope van deze extractie.
5. **Granulariteit**: voor `aangepast-oordeel` en `oordeel-met-voorbehoud` heb ik bewust gekozen voor één omvattend `controleoordeel-types`-record + één begrip-record `aangepast-oordeel`. Drie aparte records (met-voorbehoud, afkeurend, onthouding) zou overlap geven. Beslissing-rationale opgenomen in `controleoordeel-types.bouwstenen`.

## Beperkingen die zijn nageleefd

- Geen examen-vragen geraadpleegd
- Bundle-JSON's onaangetast
- Records geschreven in het Nederlands
- `status: "seed"` op alle nieuwe records
- Werkbudget ~2u gerespecteerd (zonder Python-scripts, alleen JSON-IO)
