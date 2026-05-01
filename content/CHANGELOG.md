# Changelog

Elke inhoudelijke wijziging aan een eerder geverifieerde fiche wordt hier geregistreerd. Gebruik dit bestand om bij te houden welke fiches opnieuw bekeken moeten worden.

**Verificatiestatus**: nog niet geverifieerd — eerste gebruik.
*(Vervang deze regel na een verificatieronde: "Alle wijzigingen t.e.m. YYYY-MM-DD zijn geverifieerd.")*

---

## 2026-05-01 — Opstart vak 1.3

### Nieuw aangemaakt (nog nooit geverifieerd)

**Materie:**
- `continuiteitsrisico.md` — going concern, alarmbelprocedure BV/NV (WVV), meldingsplicht GA (WER XX.23), signalen, misleidende signalen, Altman Z-score (🤖)
- `vermogensstroomtabel.md` — begrip, structuur herkomst/besteding, interpretatie NBK-effect, vergelijking kasstroomoverzicht
- `hefboomwerking.md` — operationele hefboom (DOL), financiële hefboom (DFL), formules, sectorpatronen
- `betrokken-partijen-financiele-analyse.md` — externe gebruikers, toezichtsorganen, Balanscentrale NBB
- `niet-in-balans-opgenomen-elementen.md` — off-balance verplichtingen, zekerheden, toelichting-verplichting

**Competenties:**
- `financiele-ratio-berekenen.md` — stap-voor-stap ratio berekenen vanuit jaarrekening, schema-beperkingen, subsidie-correcties
- `jaarrekening-herwerken.md` — herstructurering balans en resultatenrekening, kernbalansaggregaten
- `continuiteit-beoordelen.md` — signalen → drempel → alarmbelprocedure (bestuursorgaan) → meldingsplicht (GA)

**Normen:**
- `normen/ISA-570-herzien.md` — sleutelpassages ISA 570 als analytisch referentiemateriaal (niet bindend voor GA)

### Uitgebreid (waren geverifieerd voor 1.2 — terug op draft)

- **`financiele-ratios.md`** — Belgische ratio-namen met NBB-codes toegevoegd (liquiditeit ruime/enge zin, nettorentabiliteit activa, brutoverkoopmarge), aandeelhoudersratio's (intrinsieke waarde, fractiewaarde), cashflowratio's (operationele cash flow), schema-beperkingen tabel. Tags uitgebreid met `"1.3"`.
  *Reden: fiche dekte enkel internationale terminologie (ROE, ROA), niet de Belgische examennamen.*

- **`jaarrekeninganalyse.md`** — (1) Inhoud uitgebreid voor 1.3: passief volgorde, EV kortmodel NBB, effect afschrijvingen op brutoverkoopmarge, NBK verhogen. (2) Architecturele herclassificatie: intro en sectiehoofden herschreven zodat de fiche duidelijk een begrippen-fiche is ("Analytische indeling van X" ipv "Herstructurering van X"). Procedurele stappen nu exclusief in `jaarrekening-herwerken`.
  *Reden: materie-fiches beschrijven geen werkwijze — dat is de rol van competentie-fiches.*

### Vakfiche bijgewerkt

- **`1.3-analyse-en-kritische-beoordeling-jaarrekening.md`** — Stap 2A/2B uitgevoerd: 4 competenties en 7 materie-fiches geïdentificeerd en gelinkt. Bestaande fiches (`jaarrekening.md`, `jaarrekeninganalyse.md`) hergebruikt ipv nieuwe aangemaakt.

### Verwijderd

- `content/itaa-lex/` (5 fiches) — vervangen door `content/wetteksten/` als primaire bron voor wetteksten

### Architecturele wijzigingen (CLAUDE.md + workflow)

- CLAUDE.md volledig herschreven: nieuwe structuur Context → Aanpak → Bronnen → PO-fiches → Competenties → Materie → Proces → Technisch
- Werkprincipe autonoom werken toegevoegd (geen tussenvragen)
- Reflecties geïntegreerd in workflow-stappen (niet meer apart)
- Bronintegriteit verplaatst naar Bronnen-sectie
- Wettekst lokaal toevoegen: nieuw proces toegevoegd
- Changelog-systeem ingevoerd (dit bestand)
- Feedback als verbeterimpuls: nieuw principe toegevoegd

## 2026-05-01 (vervolg) — Concretisering jaarrekeninganalyse en competenties

### Uitgebreid (waren al draft)

- **`jaarrekeninganalyse.md`** — NBB-code mapping tabel toegevoegd per analytische categorie (activazijde + passivazijde), met voor/na-voorbeeld in code block.
  *Reden: stagiair kon "vlottende activa" niet linken aan concrete rubrieken in de jaarrekening.*

- **`jaarrekening-herwerken.md`** — Stap 2 (balans): gedetailleerde NBB-tabel vervangen door verwijzing naar materie-fiche (canonieke thuisplaats), vuistregels voor snelle toepassing toegevoegd. Gebroken link naar resultatenrekening-sectie hersteld.
  *Reden: zelfde informatie stond op twee plaatsen; delegeer het "wat" naar materie, houd het "hoe" in de competentie.*

### Conventies bijgewerkt (CLAUDE.md)

- **Stapnamen competentie-fiches**: altijd in instructievorm (was: vragen by default). Alle bestaande fiches bijgewerkt.
