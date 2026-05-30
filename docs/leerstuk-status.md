# Leerstuk-status — stand-van-zaken per PO

**Laatste update**: 2026-05-31
**Update-discipline**: elke sessie die een leerstuk-artefact wijzigt, update deze tabel in dezelfde commit.

---

## Stand per programmaonderdeel

| PO | Skelet | Scripts | Markdown gerendered | Minicursus aangepast | Themafiche tweelaags | Status |
|---|---|---|---|---|---|---|
| **1.1** Boekhouding | — | — | — | — | — | Openstaand |
| **1.2** Boekhoud- en jaarrekeningenrecht | — | — | — | — | — | Openstaand |
| **1.3** Analyse van de jaarrekening | — | — | — | — | — | Openstaand |
| **1.4** Geconsolideerde jaarrekening | ✅ retro [docs/leerpad-skelet-1-4.md](leerpad-skelet-1-4.md) | ✅ 6/6 ([data/leerstukken/](../data/leerstukken/)) | ✅ 6/6 (5 in `content/leerpaden/1-4/`, 1 cross-PO in `content/leerstukken/`) | ✅ [content/leerpaden/1-4/index.md](../content/leerpaden/1-4/index.md) (3+4 samengevoegd) | ✅ [content/themafiches/consolidatie.md](../content/themafiches/consolidatie.md) | **Voltooid** (POC voor schema-validatie) |
| **1.5** IFRS | — | — | — | — | — | Openstaand |
| **1.6** Externe controle | — | — | — | — | — | Openstaand |
| **1.7** Interne controle | — | — | — | — | — | Openstaand |
| **1.8** Analytische boekhouding | — | — | — | — | — | Openstaand |
| **1.9** Financiële analyse | — | — | — | — | — | Openstaand |
| **2.1** Beroepsethiek | — | — | — | — | — | Openstaand |
| **2.2** Personenbelasting | — | — | — | — | — | Openstaand |
| **2.3** Vennootschapsbelasting | — | — | — | — | — | Openstaand |
| **2.4** BTW | — | — | — | — | — | Openstaand |
| **2.5** Fiscale procedure | — | — | — | — | — | Openstaand |
| **2.6** Registratie- en successierechten | — | — | — | — | — | Openstaand |
| **2.7** Internationale fiscaliteit | — | — | — | — | — | Openstaand |
| **2.8** Btw-procedures | — | — | — | — | — | Openstaand |
| **3.0** Vennootschapsrecht | — | — | — | — | — | Openstaand |
| **4.0** Cabinet management | — | — | — | — | — | Openstaand |

**Legende**: ✅ = klaar · 🚧 = in uitvoering · — = nog niet gestart · ❌ = blocker / actie nodig

---

## Voorbeeldgroepen-inventaris

| Naam | Locatie | Gebruikt door | Beschrijving |
|---|---|---|---|
| `aurelia` | [data/voorbeeldgroepen/aurelia.yaml](../data/voorbeeldgroepen/aurelia.yaml) | PO 1.4 (alle leerstukken) | Mock Belgische groep met 4 deelnemingen — alle controle-niveaus en methodes |

Voor nieuwe PO's: overweeg eerst of een bestaande voorbeeldgroep hergebruikt kan worden. Anders maken in `data/voorbeeldgroepen/<naam>.yaml`.

---

## Open punten per PO

### PO 1.4 — Geconsolideerde jaarrekening

- **Cross-PO leerstuk**: `individuele-jaarrekening-opmaken` zit in `content/leerstukken/` (niet onder `leerpaden/1-4/`). Wanneer PO 1.1/1.2 leerstukken krijgen, beslis: dupliceren of via tag-gestuurde inclusie zichtbaar maken in beide PO's
- **Tarief-records**: drempels-* records bestaan en zijn trusted. Eventueel uitbreiden met PO-specifieke tarieven
- **Themafiche-revisie**: ADR-037 amendement zegt dat themafiche-schrijfregels zelf nog herzien moeten — visueel-dominanter en korter. Wacht tot 3+ PO's leerstukken hebben

---

## Procedure-referenties

- **Nieuwe PO starten**: [docs/leerstuk-procedure.md](leerstuk-procedure.md) Stap 0-7
- **Bestaand leerstuk bijwerken**: [docs/leerstuk-procedure.md](leerstuk-procedure.md) §"Feedback op een bestaand leerstuk"
- **Beleid**: [ADR-037](adr/ADR-037-leerstuk-vierde-leerlaag.md)
- **Schrijfregels**: [docs/leerstuk-schrijfregels.md](leerstuk-schrijfregels.md)
- **Script-schema**: [data/leerstukken/SCHEMA.md](../data/leerstukken/SCHEMA.md)
- **Render-prompt**: [prompts/leerstuk-render-v1.md](../prompts/leerstuk-render-v1.md)
- **Skelet-prompt**: [prompts/leerpad-skelet-v1.md](../prompts/leerpad-skelet-v1.md)

---

## Update-protocol voor deze tabel

Bij elke wijziging die de status van een PO raakt:

1. Update de relevante rij in de **Stand per programmaonderdeel**-tabel
2. Bij nieuwe voorbeeldgroep: voeg toe aan **Voorbeeldgroepen-inventaris**
3. Bij PO-specifieke open punten: voeg of update entry onder **Open punten per PO**
4. Bump **Laatste update** datum bovenaan
5. Commit deze update samen met de leerstuk-wijziging zelf (één commit per logische werkronde)
