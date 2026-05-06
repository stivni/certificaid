# Bronnen-pipeline: importeren en verwerken

## Overzicht

Nieuwe bronnen toevoegen verloopt in drie stappen:

```
resources/raw/wetteksten/NAAM.pdf   (of Justel HTML via curl)
    ↓  python3 tools/convert.py --source NAAM
resources/bronnen/wetteksten/NAAM.md
    ↓  python3 tools/rag_index.py --collection wetteksten --reset
data/chroma_db/  (bijgewerkt)
```

Alle bronnen zijn geregistreerd in `resources/source_config.yaml` — de enige bron van waarheid voor wat er bestaat, hoe het geconverteerd wordt en welk gewicht het heeft.

## Stap 1 — Bron toevoegen aan source_config.yaml

```yaml
MijnWet:
  type: ejustice_nl          # zie Types hieronder
  bron_rol: itaa_lex         # zie Bronrollen hieronder
  raw: resources/raw/wetteksten/MijnWet.pdf
  output: resources/bronnen/wetteksten/MijnWet.md
  content: content/bronnen/wetteksten/XX-mijnwet.md  # optioneel: Quartz site-versie
  itaa_sectie: "XX"          # leeg ("") als niet in ITAA-LEX
  tags: ["XX", "2.x"]
  bijgewerkt: "DD.MM.JJJJ"
  wet: "Volledige wetsnaam"
  cleanup: [remove_toc_ejustice, ensure_article_headings]
  status: nieuw
```

Na conversie: update `status` naar `volledig` en voeg toe aan `content/bronnen/ITAA-LEX.md`.

## Types

| Type | Beschrijving | Gebruik voor |
|---|---|---|
| `wib92` | Delegeert naar `convert-wib92.py` | WIB92 (Fisconet tweetalig, eigen script) |
| `wetboek` | Delegeert naar `convert-wetboek.py` via `wetboek_key` | Bronnen met config in dat script |
| `ejustice_nl` | pdftotext -layout + cleanup | ejustice NL-only PDFs |
| `ejustice_bilingual` | pdftotext met kolom-extractie | ejustice NL/FR tweetalig |
| `skip` | Geen (her)conversie via convert.py | Al manueel verwerkt, HTML-extractie, formulieren |

**`simple_mode: true`** toevoegen bij `ejustice_nl` voor EU-publicatieblad CELEX-documenten (tweekoloms — zonder `-layout` betere output).

### Bronnen zonder PDF (Justel HTML)

Sommige wetten hebben geen gecoördineerde PDF op ejustice (bv. Wet verzekeringen 2014). Aanpak:

```bash
curl -s -L "https://www.ejustice.just.fgov.be/cgi_loi/change_lg.pl?language=nl&la=N&cn=...&table_name=wet" \
  -o /tmp/wet.html
# Extraheer tekst en verwerk naar MD met Python (zie convert.py van Wet-verzekeringen-2014 als voorbeeld)
# Voeg toe aan source_config als type: skip
```

### Praktijkgidsen en toelichtingen (FOD Financiën)

```bash
# Toelichting PB (jaarlijks — vervang 2025 door het actuele aanslagjaar):
curl -L "https://fin.belgium.be/sites/default/files/media/documents/toelichting-deel-1-vg-JJJJ.pdf" \
  -o resources/raw/wetteksten/toelichting-PB-JJJJ-deel1-VG.pdf
# Toelichting VenB:
curl -L "https://financien.belgium.be/sites/default/files/121-aangifte-venb-toelichting-JJJJ.pdf" \
  -o resources/raw/wetteksten/toelichting-VenB-JJJJ.pdf
# Verwerk met pdftotext (geen -layout) en voeg toe als type: skip, bron_rol: praktijkgids
```

## Bronrollen (`bron_rol`)

Geeft aan welk gewicht een bron heeft bij conceptextractie en studie:

| `bron_rol` | Autoriteit | Bij examen? | Gebruik |
|---|---|---|---|
| `itaa_lex` | Hoogste — wettekst | ✅ Ja, in ITAA-LEX | Primaire bron voor feitelijke beweringen |
| `normatief` | Hoog — wettekst | ❌ Niet in ITAA-LEX | Juridische grondslag, maar niet citeerbaar bij examen |
| `interpretatief` | Middel — CBN/ITAA | ❌ | Boekhoudkundige/professionele interpretatie |
| `praktijkgids` | Laag — gids | ❌ | Uitleg van HOE iets werkt; niet als rechtsbron citeren |
| `formulier` | Referentie | ❌ | Code-referentie; geen conceptinhoud |

**Regel voor conceptextractie**: chunks met `bron_rol: itaa_lex` of `interpretatief` krijgen `confidence: grounded`; chunks met `praktijkgids` geven aanleiding tot `confidence: inferred` tenzij ze verwijzen naar een wetsartikel.

## Cleanup-stappen

Standaard-stappen (altijd, in vaste volgorde — volgorde is kritisch):
1. `remove_page_artifacts` — paginanummers, URL-fragmenten, form feeds ← **moet vóór remove_toc**
2. `remove_toc` — inhoudsopgave verwijderen (generiek)
3. `fix_broken_words` — afgebroken woorden aan regeleindes herstellen
4. `normalize_whitespace` — meerdere spaties → één
5. `collapse_blank_lines` — max 2 lege regels na elkaar

Extra stappen (via `cleanup:` in config):

| Stap | Gebruik voor |
|---|---|
| `remove_toc_ejustice` | ejustice-format TOC (Art. X-Y ranges) vóór echte artikels |
| `remove_french_lines` | Losse Franse regels in NL-documenten |
| `remove_french_blocks` | Aaneengesloten Franse paragrafen (tweetalige ejustice) |
| `remove_inline_metadata` | Staatsblad-referenties, datumregels in body |
| `ensure_article_headings` | Artikels omzetten naar `## Art. X` markdown-headings |

## Stap 2 — Converteren

```bash
# Eén bron
python3 tools/convert.py --source MijnWet

# Alle bronnen van een type
python3 tools/convert.py --type ejustice_nl

# Alle toc-only bronnen
python3 tools/convert.py --type toc_only

# Overzicht van alle bronnen en hun status
python3 tools/convert.py --list

# Cleanup-only met diff (geen herconversie)
python3 tools/convert.py --source WIB92 --cleanup-only --diff --dry-run
```

## Stap 3 — RAG-index bijwerken

```bash
# Volledige herbouw wetteksten-collection
python3 tools/rag_index.py --collection wetteksten --reset

# Alle collections herbouwen
python3 tools/rag_index.py --reset

# Verificatie
python3 tools/rag_query.py "btw belastingplicht toepassingsgebied" --collections wetteksten --n 3
```

## Stap 4 — ITAA-LEX.md bijwerken

Na elke nieuwe bron: voeg een regel toe aan `content/bronnen/ITAA-LEX.md`:
- **ITAA-LEX bronnen** → in de juiste sectie (I t/m XXI)
- **Andere bronnen** → in de "Andere bronnen" sectie met `bron_rol`-annotatie

## Artikel-formats per bron-familie

| Familie | Artikel-format in PDF | Oplossing |
|---|---|---|
| Fisconet (WIB92, WBTW) | `## Art. X` (al markdown) | Geen extra stap |
| ejustice NL-only | `  Art. X. tekst...` (inline, 1-4 spaties) | `ensure_article_headings` |
| ejustice tweetalig | `  Art. X. tekst...` in NL-kolom | Kolom-extractie + `ensure_article_headings` |
| EU Publicatieblad (CELEX) | `Artikel X` (gecentreerd, aparte regel) | `simple_mode: true` + `ensure_article_headings` |
| Word-PDF (MIGB) | `Art. X. tekst...` (geen inspringing) | `ensure_article_headings` |
| WABB-verdrag | `Artikel X` (aparte regel) | `ensure_article_headings` |
| Justel HTML | HTML met `Art. X` — geen PDF | curl + Python HTML-extractie → `type: skip` |
| FOD-toelichting | Lopende tekst per vak/code | pdftotext (geen -layout) → `type: skip`, `bron_rol: praktijkgids` |

## Statuswaarden

| Status | Betekenis |
|---|---|
| `volledig` | Geconverteerd, artikeltekst aanwezig |
| `toc_only` | Markdown bestaat maar bevat enkel inhoudsopgave — conversie nodig |
| `nieuw` | Net toegevoegd aan config, nog te converteren |
| `skip` | Niet (opnieuw) verwerken via convert.py |

## Jaarlijks te vervangen bronnen

Sommige bronnen zijn aanslagjaar-gebonden en moeten jaarlijks bijgewerkt worden:

| Bron | URL-patroon | Wanneer |
|---|---|---|
| Toelichting PB deel 1 VG | `fin.belgium.be/.../toelichting-deel-1-vg-JJJJ.pdf` | Mei–juni elk jaar |
| Toelichting PB deel 2 | `fin.belgium.be/.../toelichting-deel-2-JJJJ.pdf` | Mei–juni elk jaar |
| Toelichting VenB | `financien.belgium.be/.../121-aangifte-venb-toelichting-JJJJ.pdf` | Najaar elk jaar |
| Belastinggids ACLVB | `aclvb.be/.../belastinggids-JJJJ.pdf` | Mei elk jaar |
