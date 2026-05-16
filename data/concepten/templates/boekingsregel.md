# Boekingsregel (debet/credit)

Format voor één enkele boeking — debet/credit/bedrag/omschrijving. Gebruik wanneer een stap een concrete boeking demonstreert (bv. eerste opname van consolidatieverschil, eliminatie intragroep-vordering, dividend van geassocieerde).

## Markdown-skelet (enkele boeking)

```markdown
| Boeking — {{omschrijving_boeking}} | Debet | Credit |
|---|---:|---:|
| {{rekening_debet}} | {{bedrag}} | |
| {{rekening_credit}} | | {{bedrag}} |
```

## Markdown-skelet (samengestelde boeking)

```markdown
| Boeking — {{omschrijving_boeking}} | Debet | Credit |
|---|---:|---:|
| {{rekening_1}} | {{bedrag_1}} | |
| {{rekening_2}} | {{bedrag_2}} | |
| {{rekening_3}} | | {{bedrag_3}} |
| **Totaal** | **{{totaal_debet}}** | **{{totaal_credit}}** |
```

## Toetsing

- **Debet = Credit** (boekhoudkundige balans-regel)
- VERIFY-aspect `boeking.klopt-niet`: som debet ≠ som credit

## Cast-conventie

- Rekeningnamen volgens minimum algemeen rekeningstelsel (Belgisch MAR): "281 Deelnemingen in verbonden ondernemingen", "416 Vorderingen op verbonden ondernemingen", "5500 Bank", "70 Omzet", etc.
- Bedragen in € + duizendtallen
- Korte omschrijving in `omschrijving_boeking` (≤ 8 woorden)

## Voorbeelden

### Eerste opname consolidatieverschil (positief)

```markdown
| Boeking — Eerste consolidatie Brugse Brouwerij, consolidatieverschil 80.000 | Debet | Credit |
|---|---:|---:|
| 281 Deelnemingen in verbonden ondernemingen (eliminatie) |  | € 320.000 |
| Eigen vermogen Brugse Brouwerij (aandeel 80%, eliminatie) | € 240.000 |  |
| Consolidatieverschillen (positief, actief) | € 80.000 |  |
| **Totaal** | **€ 320.000** | **€ 320.000** |
```

### Eliminatie intragroep-vordering

```markdown
| Boeking — Eliminatie vordering Aurelia Holding op Brugse Brouwerij | Debet | Credit |
|---|---:|---:|
| 489 Schulden van Brugse Brouwerij aan Aurelia (passief) | € 50.000 |  |
| 416 Vorderingen Aurelia op Brugse (actief) |  | € 50.000 |
| **Totaal** | **€ 50.000** | **€ 50.000** |
```

## Wanneer dit template gebruiken

- Demonstratie van eerste consolidatie (boekhoudkundige verwerking)
- Intragroep-eliminatie (vorderingen, schulden, voorraadwinst)
- Dividend van geassocieerde via vermogensmutatie (financiële opbrengst + vermindering boekwaarde deelneming)
- Step acquisition (gedeeltelijke verwerving + correcties)
