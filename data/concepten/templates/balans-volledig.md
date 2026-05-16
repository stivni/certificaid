# Volledige balans (enkelvoudig, KB WVV-rubrieken)

Standaard enkelvoudige balans met alle hoofdrubrieken uit het KB WVV-schema. Gebruik wanneer rubriek-specifieke effecten belangrijk zijn (bv. herwaardering, deelnemingen, intragroep-vorderingen).

## Markdown-skelet

```markdown
| {{vennootschap_naam}} — Activa | EUR |
|---|---:|
| **Vaste activa** | {{vaste_activa_totaal}} |
| Oprichtingskosten | {{oprichtingskosten}} |
| Immateriële vaste activa | {{immateriele_va}} |
| Materiële vaste activa | {{materiele_va}} |
| Financiële vaste activa | {{financiele_va}} |
| └── Deelnemingen in verbonden ondernemingen | {{deelnemingen_verbonden}} |
| └── Andere financiële vaste activa | {{andere_financiele_va}} |
| **Vlottende activa** | {{vlottende_activa_totaal}} |
| Vorderingen op meer dan een jaar | {{vorderingen_lang}} |
| Voorraden en bestellingen in uitvoering | {{voorraden}} |
| Vorderingen op ten hoogste een jaar | {{vorderingen_kort}} |
| └── Vorderingen op verbonden ondernemingen | {{vorderingen_verbonden}} |
| Geldbeleggingen en liquide middelen | {{liquide_middelen}} |
| Overlopende rekeningen | {{overlopende_activa}} |
| **Totaal activa** | **{{totaal_activa}}** |

| {{vennootschap_naam}} — Passiva | EUR |
|---|---:|
| **Eigen vermogen** | {{eigen_vermogen_totaal}} |
| Kapitaal | {{kapitaal}} |
| Uitgiftepremies | {{uitgiftepremies}} |
| Herwaarderingsmeerwaarden | {{herwaarderingsmeerwaarden}} |
| Reserves | {{reserves}} |
| └── Wettelijke reserve | {{wettelijke_reserve}} |
| └── Onbeschikbare reserves | {{onbeschikbare_reserves}} |
| └── Beschikbare reserves | {{beschikbare_reserves}} |
| Overgedragen winst (verlies) | {{overgedragen_resultaat}} |
| **Voorzieningen en uitgestelde belastingen** | {{voorzieningen}} |
| **Schulden** | {{schulden_totaal}} |
| Schulden op meer dan een jaar | {{schulden_lang}} |
| Schulden op ten hoogste een jaar | {{schulden_kort}} |
| └── Schulden aan verbonden ondernemingen | {{schulden_verbonden}} |
| Overlopende rekeningen | {{overlopende_passiva}} |
| **Totaal passiva** | **{{totaal_passiva}}** |
```

## Toetsing

- `vaste_activa_totaal` = som van zijn subposten (oprichtingskosten + immateriële + materiële + financiële)
- `vlottende_activa_totaal` = som van zijn subposten
- `eigen_vermogen_totaal` = kapitaal + uitgiftepremies + herwaarderingsmeerwaarden + reserves + overgedragen_resultaat
- `schulden_totaal` = som van zijn subposten
- **`totaal_activa` = `totaal_passiva`** (VERIFY-aspect `balans.klopt-niet`)

## Cast-conventie

- Bedragen in € + duizendtal-formaat
- Plausibele verhoudingen: Eigen vermogen typisch 20-40% van totaal balans voor gezonde BV; schulden 60-80%
- Voor methode-demonstraties: vereenvoudig naar enkele subposten ingevuld (anderen op 0 of weggelaten)

## Wanneer dit template gebruiken

- Wanneer de bouwsteen/stap rubriek-specifieke informatie nodig heeft (bv. "schrap deelneming-post, voeg consolidatieverschillen toe")
- Wanneer intragroep-vorderingen/schulden gedemonstreerd moeten worden
- Voor uniforme-waarderingsregels-voorbeelden (rubriek X moet hercorrigeerd worden)
