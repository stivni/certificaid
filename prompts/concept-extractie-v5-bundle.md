# Prompt: Concept-extractie — EXTRACT v5 (BUNDLE-aware, compact)

**Status**: permanent prompt-artefact — bundle-aware variant (2-pass architectuur)
**Schema**: ADR-025 v2.0 + §4bis (rol-set + naming-regels)
**Vervangt**: `concept-extractie-v5.md` voor bulk-extract (volledige v5 blijft als referentie)

---

## 1. Wat is er anders

Je krijgt een **vooraf-gebouwde context-bundle** als initial-ctx: `data/extractie/_bundles/<fiche_id>.json`. Die bevat:
- `kandidaat` — skeleton-context (anchors, edges, motivatie, verwachte_onderdelen, v1_hints)
- `anchor_bundle` — alle TDKs van de primary_po
- `v1_inspiratie` — top-3 v1.x-records (content-inspiratie, NIET 1-op-1 overzetten)
- `bronnen_resultaten[].hits` — **echte bronnen-chunks** (al geprefetched via daemon, 3 kind-specifieke + 1 algemene query)

Controleer eerst `bundle.full_2pass`:
- **`true`** (normaal geval): hits staan al in `bronnen_resultaten[].hits`. **Skip de initiële retrieval volledig.**
- **`false`** (legacy / daemon offline): `bronnen_resultaten[].hits` bevat `_pending`-markers. Voer de queries alsnog uit via MCP.

Doe **geen herhaalcalls** voor deze data. Skip altijd:
- `mcp__certificaid-rag__lees_kandidaat` (al in bundle)
- `mcp__certificaid-rag__lees_anchor_bundle` (al in bundle)
- `mcp__certificaid-rag__lees_record` voor v1_hints in bundle (al gelezen)
- Exploratory Bash (`ls`, `curl`, `date`, `grep` op systeembestanden — alle paden staan hieronder)

---

## 2. Werkstroom (time-box 15 min)

### 2a. Full-2-pass (bundle.full_2pass == true — standaard)

1. **Lees de bundle** (`/path/to/data/extractie/_bundles/<fiche_id>.json`)
2. **Gebruik de bronnen-hits direct** uit `bronnen_resultaten[].hits` — **geen initiële zoek_bronnen-calls**
3. **Schrijf fiche** volgens schema 2.0 top-volgorde (zie §3)
4. **Max 1 extra `zoek_bronnen(rerank=true)`** alleen voor ÉÉN wettelijke ⚖️-claim waar bundle een concreet gap heeft
5. **Schrijf record naar `/tmp/<fiche_id>.json`** via Write-tool (clean JSON, geen Python-escape-issues)
6. **Save + markeer via CLI** (één Bash-call):
   ```bash
   python3 -m tools.lib.records_api save /tmp/<fiche_id>.json --wave-id <wave-tag>
   ```
   Dit combineert `save_record` (disk + RAG + markdown-render) **en** `markeer_kandidaat_gerealiseerd` in één call — **geen aparte MCP-call meer** voor markeer.

**NIET DOEN** — bekende anti-patterns die ~140s/fiche kosten:
- ❌ `python3 -c "from tools.lib import records_api; records_api.save_record({...})"` — faalt op SyntaxError bij records ≥ 5 KB (embedded quotes/special chars in long strings)
- ❌ `Write /tmp/<id>.py` met heredoc-script — werkt maar onnodig omslachtig
- ❌ Aparte `mcp__certificaid-rag__markeer_kandidaat_gerealiseerd`-call — niet meer nodig met `--wave-id` flag

**Harde caps (full-2-pass):**
- `zoek_bronnen` totaal: ≤ 3 (alleen eigen creatieve queries)
- `zoek_bronnen(rerank=true)` totaal: **≤ 1** (gebruik alleen voor ÉÉN cruciale wettelijke ⚖️-claim met onzekerheid)
- Bash: alleen voor save_record-uitvoering (geen exploration)
- v1-reads: 0 (al in bundle)

> **Rerank-discipline**: bundle bi-encoder is meestal voldoende — rerank alleen voor échte ambiguïteit-resolutie, niet als perfectie-streven. Elke extra `rerank=true`-call kost ~30-60s door cross-encoder overhead.

### 2b. Legacy (bundle.full_2pass == false — daemon was offline bij bundle-build)

1. **Lees de bundle**
2. **Voer de queries alsnog uit** via `mcp__certificaid-rag__zoek_bronnen(query=<bronnen_resultaten[i].query>, rerank=false, top_k=5)`
3. Ga verder als 2a stap 3-6 (incl. `Write /tmp/<id>.json` + CLI-save)

**Harde caps (legacy):**
- `zoek_bronnen` totaal: ≤ 7 (4 inhaal-queries + 3 eigen)
- `zoek_bronnen(rerank=true)` totaal: **≤ 1** (zie rerank-discipline hierboven)

---

## 3. Schema 2.0 top-volgorde

Schrijf records met deze structuur (zie ADR-025 voor details):

1. **Frontmatter** — `id`, `naam`, `node_type`, `schema_version: "2.0"`, `primary_po`, `linked_anchors[]`, `dekt_tdks[]`, `cross_po`, `edges_voorgesteld{}`, `_provenance{}`
2. **`definitie`** — 1-2 zinnen, ⚖️ direct uit bron met `source` (`source` als **string**, niet meer als dict)
3. **`wat_er_economisch_echt_gebeurt`** — gebruik veld `text` (niet `inhoud` of `tekst`). Didactische uitleg, rol-onafhankelijk.
4. **`wanneer_van_toepassing`** — `voor_wie.text` + `wanneer_wel[]` + `wanneer_niet[]` + optioneel `hoofdrisico.text` + `hoofdvoordeel.text` (kind-specifiek)
5. **`hoe_het_werkt`** — `intro` + `onderdelen[]` met geneste `weergaven[]`. Element-vocabulaire (`inhoud_type` + `weergaven[]`) hoort **GENEST binnen `hoe_het_werkt.onderdelen[].elementen[]`**, niet als top-level veld.
6. **`rol_van_de_accountant`** — gestructureerde matrix (zie §4 + §4bis voor canonieke structuur)
7. **`voorkennis_leespad`** — `voorvereisten`, `kader`, `naast_relevant`, `volgkennis`
8. **`veelvoorkomende_verwarringen`** *(verplicht waar relevant — bv. wanneer verschil met gelijkluidend concept didactisch belangrijk is)* — array van `{concept, verschil}` of beschrijvende paragrafen
9. **`familie_en_alternatieven`** *(verplicht voor instrument/operatie/regime/fiscale-regeling)* — leden van familie + alternatieve concepten die hetzelfde doel dienen
10. **`bronnen_en_verwijzingen`** *(verplicht)* — gestructureerd: `grounded[]` (lijst ⚖️-bronnen met `ref` + `art_of_par`), `te_verifieren[]` (lijst ⚠️-items), `edges[]` (cross-record `lid_van`/`heeft_lid`/`gerelateerd`/`verward_met`)
11. **`wat_dit_record_dekt`** — competenties_chronologisch + termen_alfabetisch

**Veld-namen strikt**:
- Gebruik `text` voor body-tekst (niet `inhoud`, niet `tekst`)
- Gebruik `source` als string voor bron-citation (niet als dict — daemon-fix 2026-05-21 ondersteunt beide vormen, maar **string is de canonical schema 2.0-vorm**)
- Gebruik `actor` voor perspectief-naam (niet `naam` of `klant` — render-template verwacht `actor`)
- Gebruik `emoji`-veld op perspectief en op rol (bv. `"emoji": "🏢"` voor uitgever-vennootschap, `"emoji": "📋"` voor boekhouder) — render-template gebruikt deze in headers

**Rol-emoji-conventies** (gebruik deze defaults):
- `adviseur` → 🎯
- `boekhouder` → 📋
- `externe auditor` → 🔍
- `interne-controle-adviseur` → 🛡️
- `fiscaal adviseur` → 💰

### 3bis. Vuistregels (🧭) — wanneer wél gebruiken

**Verplicht ⚠️ als signaal**: agents zijn vaak té conservatief en gebruiken 0 vuistregels — dat ondermijnt de didactische waarde. ADR-025 §confidence zegt expliciet dat **🧭 wel toegestaan** is voor:

- **"Wanneer kies je dit?"** — selectie-advies (wanneer wel/niet, voor wie)
- **"Hoofdrisico"** — waar de stagiair moet opletten
- **"Hoofdvoordeel"** — wat het concept écht oplost
- **Strategische signaal-zinnen** in `adviseur`-cellen — bv. "verlieslatende vennootschappen kunnen overwegen om vóór ontbinding eerst groepsbijdrage toe te passen indien…"
- **Speelruimte** — wanneer wet ruimte laat voor interpretatie
- **Sectoroverwegingen** — bv. "voor handelsondernemingen ligt de drempel typisch op…"
- **Empirische beroepswijsheid** zonder harde bron — als de wet niets zegt maar praktijk wel

**Niet toegestaan**: 🧭 voor procedures, cijfers, tarieven, drempels die uit wet/KB komen, wettelijke voorwaarden, rekening-codes. Daar geldt ⚖️ (met bron) of ⚠️ (te verifiëren).

**Streef-distributie** (voor kader/familie/fiscale-regeling-fiches met strategisch advies):
- 50-70% ⚖️ grounded
- 15-25% 🔗 inferred
- **10-25% 🧭 vuistregel** ← niet 0%!
- 0-10% ⚠️ te_verifieren

### 3ter. `weergaven[]` — concrete didactische blokken

Element-vocabulaire is **niet decoratief** — elke `inhoud_type` heeft één of meer `weergaven[]` met concrete didactische output. Voorbeelden per type:

| Concept-type | inhoud_type | weergave-types (gebruik!) |
|---|---|---|
| Boekhoudregel | `mechanisme` | `boeking` (rekening-codes, debet/credit), `t-rekening`, `balans-snapshot` |
| Formule | `formule` | `formule-expressie` (LaTeX-achtig), `berekening` (concreet getal) |
| Vergelijking | `vergelijking` | `vergelijkingstabel` (cols=alternatieven, rows=aspecten) |
| Stappen | `procedure` | `stappenlijst` (genummerd), `tijdslijn` |
| Beslissing | `keuze` | `beslisboom`, `vergelijkingstabel` |
| Voorbeeld | `casus` | `tabel` + `proza` (mini-case-study) |
| Drempel/regel | `drempel` | `tabel` (waarde + bron + sinds-wanneer) |

**Anti-pattern**: één lange tekstuele `proza`-weergave die alles uitlegt. **Patroon**: één concept-eenheid (= element) met meerdere weergaven (proza-uitleg + boeking + balans-snapshot) — render-template toont ze als zustertabbladen of geneste blokken.

**Voor `hoe_het_werkt.onderdelen[]`**: elk onderdeel HOORT `weergaven[]` te hebben (geen titel-only). Als je geen weergave hebt, is het onderdeel waarschijnlijk niet didactisch genoeg — overweeg om het in een ander onderdeel te integreren.

---

## 4. Rol × perspectief (ADR-025 §4 — 5-rol-set + eigen-kantoor)

Twee perspectief-soorten:
- **Klant-types**: KMO-handelsonderneming, familiale holding, uitgever, belegger NP, belegger venn., bestuur, vzw, …
- **`eigen-kantoor`**: voor AWW eigen-kantoor, ITAA-deontologie, GDPR — *niet* een klant

5 rollen (vaste set):
- **`adviseur`** — strategisch + operationeel advies + begeleiding (incl. faillissement-klant-begeleiding)
- **`boekhouder`** — boekings-uitvoering, MAR-toepassing
- **`externe auditor`** — commissaris, assurance, controleverklaring (incl. ISA 240 fraude-detectie)
- **`interne-controle-adviseur`** — IC-systemen ontwerpen/evalueren (NIET in-house IA-functie zelf)
- **`fiscaal adviseur`** — fiscaal advies + aangifte + procedure

**Geen aparte rollen voor**: compliance (= `adviseur` of `externe auditor` of `eigen-kantoor × interne-controle-adviseur`), curator (= externe actor; accountant-werk valt onder `adviseur`/`boekhouder`), forensisch (= `externe auditor` ISA 240).

**Toon geen lege rollen.** Dun-bezet matrix (~30-40% cellen vol) is normaal.

### 4bis. Canonieke JSON-structuur (verplicht — geen platte dict)

Render-template verwacht **`perspectieven[].rollen[]`-array**, NIET een platte dict zoals `{adviseur: {KMO: {...}}, boekhouder: {...}}`. Volg dit exacte schema:

```json
"rol_van_de_accountant": {
  "perspectieven": [
    {
      "actor": "KMO-handelsonderneming",
      "emoji": "🏪",
      "rollen": [
        {
          "rol": "adviseur",
          "emoji": "🎯",
          "taken": ["taak 1", "taak 2"],
          "elementen": [
            {
              "element_id": "kort-id",
              "inhoud_type": "vuistregel",
              "titel": "Titel",
              "beschrijving": "…",
              "confidence": "vuistregel",
              "weergaven": []
            }
          ]
        },
        { "rol": "boekhouder", "emoji": "📋", "taken": [...], "elementen": [...] }
      ]
    },
    {
      "actor": "eigen-kantoor",
      "emoji": "🏛️",
      "rollen": [...]
    }
  ]
}
```

**Wat NIET doen** (Sonnet-pitfall uit 2026-05-21 test):
```json
// ❌ FOUT — platte dict werkt niet met render-template:
"rol_van_de_accountant": {
  "adviseur": {
    "KMO-handelsonderneming": {"perspectief": "..."}
  }
}
```

Lege rollen of perspectieven NIET tonen — gewoon weglaten uit de array.

---

## 5. Confidence-discipline

| Token | Wanneer | Visueel |
|---|---|---|
| `grounded` | Direct uit wet/KB/CBN/norm met `source` | ⚖️ |
| `inferred` | Redenering uit combinatie bronnen | 🔗 |
| `vuistregel` | Beroepswijsheid zonder verifieerbare bron | 🧭 |
| `te_verifieren` | Bron ontbreekt of nog te checken | ⚠️ |
| `tegenstrijdig` | Bron is gevonden en spreekt claim tegen | ❌ |

**🧭 NIET toegestaan voor**: procedures, cijfers, tarieven, drempels, wettelijke voorwaarden, rekening-codes. Daar geldt ⚖️ of ⚠️.

**Per-claim**: zet `confidence` op elk element + waar zinvol op sub-claims.

---

## 6. Naming-discipline (ADR-025 §4bis)

Het record dat je schrijft heeft de `fiche_id` uit de kandidaat — die is al genormaliseerd. Voor edges en links naar andere fiches: gebruik concept-namen, geen kind-suffixes (`-kader`/`-familie`/`-procedure`) en geen bron-namen in naam (`ias-X`, `ifrs-X`, `isa-X` horen als bron-citation in body, niet als fiche-id).

---

## 7. Hard rules

- **GEEN examen-vragen** als extract-input (circulair)
- **GEEN schema-jargon in body** (`linked_anchors`, `node_type` alleen in frontmatter)
- **GEEN rekening-codes** in "Hoe het werkt" (alleen in Rol > Boekhouder cellen)
- **GEEN examen-context** in body ("in examen-context: …")
- **Confidence-history** bijhouden in `_provenance.confidence_history[]`

---

## 8. Bekende MCP-bug

`mcp__certificaid-rag__aanvul_kandidaat(veld='edge')` blokkeert. Workaround: edges direct in record-frontmatter zetten, niet via deze MCP-call.

---

## 9. Return-message (voor benchmark)

In je laatste message:
- Pad naar markdown + JSON
- Wall-clock vanaf start tot save_record
- MCP-call-breakdown (totaal + per tool + aantal `rerank=true`)
- ⚠️-percentage (aantal ⚠️/totaal-claims)
- Cell-fill rol×perspectief-matrix (gevulde cellen / totaal mogelijke)
- Eventuele errors of caps die je raakte
- (Alleen voor Sonnet) Specifieke moeilijkheden vs als Opus geweest was
