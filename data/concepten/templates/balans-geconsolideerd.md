# Geconsolideerde balans

Structuur van een geconsolideerde balans (KB WVV art. 3:104 e.v.). Sleutelverschillen met enkelvoudige balans:

- **Belangen van derden** als afzonderlijke passiefpost (KB WVV art. 3:137) — voor integrale consolidatie
- **Consolidatieverschillen** als afzonderlijke actief- of passiefpost (KB WVV art. 3:130-3:131)
- **Vennootschappen waarop vermogensmutatie is toegepast** als afzonderlijke post in financiële vaste activa (KB WVV art. 3:141) — voor geassocieerden
- Deelnemingen in volledig/evenredig opgenomen dochters: GEEN aparte post (zit verwerkt in de actief/passief-overname)
- Intragroep-vorderingen/schulden: geëlimineerd (KB WVV art. 3:134)

## Markdown-skelet

```markdown
| {{groep_naam}} — Geconsolideerde activa | EUR |
|---|---:|
| **Vaste activa** | {{vaste_activa_totaal}} |
| Immateriële vaste activa | {{immateriele_va}} |
| Materiële vaste activa | {{materiele_va}} |
| Financiële vaste activa | {{financiele_va_totaal}} |
| └── Vennootschappen waarop vermogensmutatie is toegepast | {{vermogensmutatie_post}} |
| └── Andere financiële vaste activa | {{andere_financiele_va}} |
| **Vlottende activa** | {{vlottende_activa_totaal}} |
| Voorraden | {{voorraden}} |
| Vorderingen op ten hoogste een jaar (na eliminatie intragroep) | {{vorderingen_na_eliminatie}} |
| Liquide middelen | {{liquide_middelen}} |
| **Consolidatieverschillen** (positief) | {{consolidatieverschil_positief}} |
| **Totaal activa** | **{{totaal_activa}}** |

| {{groep_naam}} — Geconsolideerde passiva | EUR |
|---|---:|
| **Eigen vermogen (groep)** | {{ev_groep_totaal}} |
| Kapitaal | {{kapitaal}} |
| Reserves | {{reserves}} |
| Overgedragen resultaat | {{overgedragen_resultaat}} |
| **Belangen van derden** | {{belangen_van_derden}} |
| **Consolidatieverschillen** (negatief) | {{consolidatieverschil_negatief}} |
| **Schulden** | {{schulden_totaal_na_eliminatie}} |
| Schulden op meer dan een jaar | {{schulden_lang}} |
| Schulden op ten hoogste een jaar (na eliminatie intragroep) | {{schulden_kort_na_eliminatie}} |
| **Totaal passiva** | **{{totaal_passiva}}** |
```

## Toetsing

- **`totaal_activa` = `totaal_passiva`** (VERIFY-aspect `balans.klopt-niet`)
- `belangen_van_derden` = (1 − belang%) × `eigen_vermogen_dochter` (per dochter)
- `consolidatieverschil_positief` − `consolidatieverschil_negatief` = aanschaffingswaarde deelneming − belang% × EV dochter (op acquisitiedatum, na toerekening aan onder/overgewaardeerde activa)
- Intragroep-vorderingen tussen moeder en dochters: niet in geconsolideerde balans

## Cast-conventie

- `groep_naam` typisch "Groep Aurelia Holding" of vergelijkbaar
- Bedragen in € + duizendtallen
- Voor demonstratie: vereenvoudig naar relevante rubrieken

## Wanneer dit template gebruiken

- Eindresultaat van een integrale of evenredige consolidatie (in substappen)
- Demonstratie van Belangen van derden
- Demonstratie van Consolidatieverschillen
- Voorbeeld voor vermogensmutatiemethode (alleen 1 post in financiële vaste activa)
