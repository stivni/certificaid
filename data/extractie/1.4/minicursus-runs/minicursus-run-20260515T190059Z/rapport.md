# Rapport — Minicursus-glue PO 1.4

**Run-id**: minicursus-run-20260515T190059Z
**Model**: claude-opus-4-7
**Datum**: 2026-05-15
**Skeleton**: `content/studiemateriaal/1.4-geconsolideerde-jaarrekening-en-wetgeving-betreffende-de-geconsolideerde-jaarrekening/minicursus.md`

## Samenvatting

Alle `<!-- TODO: Opus-glue ... -->` markers (totaal 16) zijn vervangen door narratieve glue-tekst. Geen markers meer aanwezig (geverifieerd via grep).

Verdeling: 1 leesgids + 1 waarom_po + 4 thematisch-intro + 9 competentie-intro + 1 synthese + 1 examenfocus = 16 markers. Opmerking: de gebruiker noemde "3 thematische intro's", maar het skeleton bevatte er 4 (fundamenteel begrippenkader, drie consolidatiemethoden, publicatie/rapportering, IFRS-context). Alle vier zijn ingevuld.

## Per glue-sectie

| Sectie | Marker | Woorden (~) | Gebruikte concepten/competenties |
|---|---|---|---|
| Leesgids | `leesgids` | 175 | Geen wikilinks (verwijst alleen naar structuur) |
| Waarom dit programmaonderdeel telt | `waarom_po` | 235 | `geconsolideerde-jaarrekening`, `consolidatieverplichting`, `intragroep-eliminaties`, `groep-van-beperkte-omvang`, `vrijstelling-subconsolidatie` |
| Thematisch — begrippenkader | `thematisch-intro #1` | 100 | Verwijst impliciet naar controle, exclusieve/gezamenlijke controle, invloed van betekenis (records-cluster) |
| Competentie — bepalen-consolidatieverplichting | `competentie-intro #1` | 75 | Procedure-grondslag van competentie `bepalen-consolidatieverplichting` (wettelijk 90%) |
| Competentie — afbakenen-consolidatiekring | `competentie-intro #2` | 80 | `afbakenen-consolidatiekring` (motivering "te verwaarlozen betekenis") |
| Competentie — kwalificeren-relatie-deelneming | `competentie-intro #3` | 80 | `kwalificeren-relatie-deelneming` (motivering controle-in-feite, 20%-weerlegging) |
| Competentie — berekenen-controle-en-belangenpercentage | `competentie-intro #4` | 85 | `berekenen-controle-en-belangenpercentage` (motivering: niet vermenigvuldigen vs. wel vermenigvuldigen) |
| Thematisch — drie consolidatiemethoden | `thematisch-intro #2` | 115 | Records: `integrale-consolidatie`, `evenredige-consolidatie`, `vermogensmutatiemethode`, `horizontale-consolidatie` |
| Competentie — kiezen-consolidatiemethode | `competentie-intro #5` | 85 | `kiezen-consolidatiemethode` (motivering: wettelijke koppeling kwalificatie → techniek) |
| Competentie — toepassen-uniforme-waarderingsregels | `competentie-intro #6` | 80 | `toepassen-uniforme-waarderingsregels` (uit definitie-snippet `uniforme-waarderingsregels-consolidatie`) |
| Competentie — uitvoeren-eerste-consolidatie | `competentie-intro #7` | 100 | `uitvoeren-eerste-consolidatie`, records `eerste-consolidatie`, `consolidatieverschil` |
| Competentie — uitvoeren-intragroep-eliminaties | `competentie-intro #8` | 105 | `uitvoeren-intragroep-eliminaties`, records `intragroep-eliminaties`, `minderheidsbelangen` |
| Competentie — verwerken-wijziging-consolidatiekring | `competentie-intro #9` | 90 | `verwerken-wijziging-consolidatiekring`, records `wijziging-consolidatiekring`, `step-acquisition` |
| Thematisch — publicatie en rapportering | `thematisch-intro #3` | 80 | Records `geconsolideerde-jaarrekening`, `geconsolideerd-jaarverslag` |
| Thematisch — IFRS-context | `thematisch-intro #4` | 90 | Record `ifrs-consolidatieraamwerk` |
| Synthese-stappenplan | `synthese` | 280 | Alle 9 competenties expliciet bij naam genoemd via wikilinks (alle die in het skeleton al voorkwamen) |
| Examenfocus | `examenfocus` | 145 | Beginselen-niveau; geen concrete records-feiten gekopieerd |

**Totaal glue-woorden**: ~1920 woorden (ruim onder de 2500-grens).

## Anti-fabricatie-check

- **Wikilinks**: enkel naar id's die al in het skeleton voorkomen (records én competenties). Geen nieuwe wikilinks verzonnen. Geverifieerd door alle gebruikte `[[...]]`-targets te kruisen met de skeleton-frontmatter en de bestaande wikilinks.
- **Feitenclaims**: geen wetsartikelnummers, geen drempelwaarden, geen tarieven in de glue-tekst. De cheatsheet bevat zulke cijfers, maar die zat al deterministisch in het skeleton.
- **Examenvragen**: niet geciteerd. Formuleringen zoals "komt klassiek terug in examen-cases" zijn meta-uitspraken zonder concrete vraag.
- **Beginselen-rationale**: in `waarom_po` en de oriëntatie-glue heb ik drie beginselen verbonden — substance over form, bescherming van de gebruiker, proportionaliteit. Deze drie verwijzen direct naar wat in de records-snippets en in de procedure-grondslagen impliciet aanwezig is (consolidatieplicht als rechtsfiguur, eliminaties tegen verborgen schuldgraad, vrijstellingen voor kleine groepen).

## Geen secties leeg gelaten

Alle 16 markers zijn ingevuld. De gebruiker liet "optionele" synthese en cheatsheet over aan oordeel:
- Synthese-stappenplan: **wel ingevuld** (de fasering volgt zuiver uit de volgorde van competenties en hun eerste-stap-vermelding — geen fabricatie).
- Cheatsheet: stond al deterministisch in het skeleton (drempelwaarden, formules, vergelijkingsmatrix). Geen extra cheatsheet toegevoegd — dat zou inhoudelijke claims vereisen die niet in de records expliciet staan.

## Mogelijke verbeteringen voor v2-glue-prompt

1. **Aantal thematische intro's vooraf documenteren in instructies.** De gebruikersopdracht zei "3 thematische clusters", maar het skeleton had er 4. Een count-mismatch leidt bijna tot een fout. Voorstel: laat de skeleton-generator het aantal hoofdstukken per type expliciet vermelden in de instructie-header.

2. **Definitie-snippets afgekapt op ~250 tekens.** Voor `consolidatieverplichting`, `consolidatieverschil` en `consolidatiekring` werden cruciale nuances afgekapt (consortium-regel, eerste-consolidatie-mechaniek, dochters in ruime zin). Dat dwingt tot voorzichtigheid maar werkt soms beperkend voor de oriëntatie-glue. Voorstel: snippets op 500 tekens of het volledige eerste alinea-veld meegeven.

3. **Procedure-grondslag geeft sterke handvat voor competentie-intro.** Het `wettelijk_pct`/`praktijk_pct`-onderscheid plus de motivering bleek goud waard om de juiste toon te kiezen (mechanisch vs. oordeel). Bewaar dit veld in toekomstige iteraties.

4. **JSON-output vs. in-place Edit.** De v1-prompt vraagt JSON op stdout, maar de werk-instructie vraagt in-place Edit van markers. Hier is gekozen voor in-place Edit (zoals de minicursus-instructies-md vraagt). Voor v2: laat de prompt consistent één van beide vragen.

5. **Wikilink-discipline binnen synthese.** De synthese-sectie heeft veel competentie-wikilinks. Het werkt, maar het herhaalt de competentie-titels uit het skeleton. Een lichtere variant (verwijzingen via "fase 2", "fase 3" zonder wikilinks) zou de tekst toegankelijker maken; nu is hij wat link-dicht. Open keuze voor v2.

6. **Eindbeoordeling van overlapping.** Er is enige conceptuele overlap tussen `waarom_po`, `thematisch-intro #1` en de oriëntatie-paragraaf van de synthese (alle drie noemen het beginsel "één economische entiteit"). Bewust gekozen om elke sectie zelfstandig leesbaar te houden, maar v2-prompt zou expliciet kunnen vragen "vermijd herhaling tussen secties X en Y".
