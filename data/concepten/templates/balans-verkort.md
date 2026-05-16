# Verkorte balans (enkelvoudig)

Structuur voor een verkorte enkelvoudige balans — twee hoofdrubrieken per kant. Gebruik dit format wanneer detail niet relevant is voor het didactische punt (bv. demonstratie van controle-percentage zonder volledige rubricering).

## Markdown-skelet

```markdown
| {{vennootschap_naam}} — Activa | EUR |
|---|---:|
| Vaste activa | {{vaste_activa}} |
| Vlottende activa | {{vlottende_activa}} |
| **Totaal activa** | **{{totaal_activa}}** |

| {{vennootschap_naam}} — Passiva | EUR |
|---|---:|
| Eigen vermogen | {{eigen_vermogen}} |
| Schulden | {{schulden}} |
| **Totaal passiva** | **{{totaal_passiva}}** |
```

## Toetsing

- `totaal_activa` = `vaste_activa` + `vlottende_activa`
- `totaal_passiva` = `eigen_vermogen` + `schulden`
- **`totaal_activa` = `totaal_passiva`** (balans-evenwicht; VERIFY-aspect `balans.klopt-niet`)

## Cast-conventie

- `vennootschap_naam` = één van de cast-namen (Aurelia Holding NV, Brugse Brouwerij BV, ...)
- Bedragen in € + duizendtal-formaat: `€ 1.250.000` (niet `1250000` of `1.25M`)
- Plausibel voor accounting-praktijk: BV's hebben typisch balans-totaal tussen € 500.000 en € 50.000.000

## Voorbeeld

```markdown
| Brugse Brouwerij BV — Activa | EUR |
|---|---:|
| Vaste activa | € 800.000 |
| Vlottende activa | € 450.000 |
| **Totaal activa** | **€ 1.250.000** |

| Brugse Brouwerij BV — Passiva | EUR |
|---|---:|
| Eigen vermogen | € 350.000 |
| Schulden | € 900.000 |
| **Totaal passiva** | **€ 1.250.000** |
```
