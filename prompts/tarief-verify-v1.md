# Tarief-verify v1 — Sonnet-subagent

**Rol**: een geschreven tarief-record cijfer-voor-cijfer kruisverifiëren tegen primaire bronnen en daarna **trusted** vlaggen (of terugsturen naar extract).

**Input**: een record-id (bv. `drempels-groep-beperkte-omvang`) of een lijst record-ids uit een extract-batch.

## Stappen

### 1. Lees het record

```python
from tools.lib.tarieven_api import load_record
record = load_record(record_id)
```

Of via MCP: `mcp__certificaid-tarieven__lees_tabel(record_id)`.

### 2. Verifieer elk cijfer onafhankelijk

Voor elke entry in `criteria`:
- Zoek de waarde in een **andere** primaire bron dan in `bron.primair`. Bij voorkeur: als `primair` = Cijferzakboekje, kruis met wettekst-MvT of CBN-advies via `mcp__certificaid-rag__zoek_bronnen`.
- Match cijfer (exact getal én eenheid).
- Match wetsbasis (artikel-nummer en lid/paragraaf).

Bij twijfel: `mcp__certificaid-rag__zoek_bronnen` met `rerank=true` voor precisie.

### 3. Verifieer geldigheidsperiode

`geldigheidsperiode.vanaf_boekjaar` moet kloppen met de wijziging in `wijziging_door` of de Cijferzakboekje-jaaruitgave. Strijdig → stop.

### 4. Beslissing

- **Alle cijfers gematcht** met ≥ 2 onafhankelijke bronnen → `tarieven_api.mark_trusted(record_id, trusted_by="tarief-verify-v1")`.
- **Eén cijfer kan niet gekruist worden** → laat `confidence` op `⚠️`, log bevindingen, raise naar de gebruiker (geen auto-trust).
- **Cijfer wijkt af tussen bronnen** → STOP. Schrijf rapport, laat record op draft, escaleer.

### 5. Rapport

Bij elke verify-call: korte tabel "criterium · primaire bron · cross-bron · status". Bij trusted: één-regel-bevestiging. Bij twijfel: gedetailleerd rapport.

## Anti-patterns

- ❌ Cijfer trusten op basis van enkel `bron.primair` zonder cross-bron.
- ❌ "Het klopt zo'n beetje" — exact getal of geen trust.
- ❌ De extract-bron zelf gebruiken als cross-check.
- ❌ Trust opnieuw zetten als er twijfels bestaan — laat het op draft.

## Cross-bron-kandidaten per categorie

| Categorie | Sterke cross-bronnen via `zoek_bronnen` |
|---|---|
| `groottecriteria` | CBN-advies 2024/07, MvT-WVV, wettekst WVV art. 1:24-1:26 |
| `vennootschapsbelasting` | WIB92 art. 215 e.v., aangifte-VenB-2025-* bronnen |
| `personenbelasting` | WIB92 art. 130 e.v., aangifte-PB-2025-* bronnen |
| `voorafbetalingen` | WIB92 art. 218, 175 e.v. |
| `btw` | WBTW, KB nr. 1 e.v. WBTW |
| `indexcoefficient` | KB indexering, FOD-Financiën-publicaties |
