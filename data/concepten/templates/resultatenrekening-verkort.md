# Verkorte resultatenrekening

Eénstaps-resultatenrekening voor demonstraties waar enkel het netto-resultaat-niveau relevant is. Voor de geconsolideerde versie: zie de toevoeging van "Aandeel van derden in het resultaat" hieronder.

## Markdown-skelet (enkelvoudig)

```markdown
| {{vennootschap_naam}} — Resultatenrekening {{boekjaar}} | EUR |
|---|---:|
| Omzet | {{omzet}} |
| Andere bedrijfsopbrengsten | {{andere_opbrengsten}} |
| **Bedrijfsopbrengsten** | **{{bedrijfsopbrengsten_totaal}}** |
| Handelsgoederen, grondstoffen en hulpstoffen | −{{kosten_handelsgoederen}} |
| Diensten en diverse goederen | −{{diensten}} |
| Personeelskosten | −{{personeelskosten}} |
| Afschrijvingen | −{{afschrijvingen}} |
| **Bedrijfskosten** | **−{{bedrijfskosten_totaal}}** |
| **Bedrijfsresultaat** | **{{bedrijfsresultaat}}** |
| Financiële opbrengsten | {{financiele_opbrengsten}} |
| Financiële kosten | −{{financiele_kosten}} |
| **Resultaat vóór belasting** | **{{resultaat_voor_belasting}}** |
| Belasting op het resultaat | −{{belasting}} |
| **Netto-resultaat** | **{{netto_resultaat}}** |
```

## Markdown-skelet (geconsolideerd)

```markdown
| {{groep_naam}} — Geconsolideerde resultatenrekening {{boekjaar}} | EUR |
|---|---:|
| Bedrijfsopbrengsten (na eliminatie intragroep-omzet) | {{bedrijfsopbrengsten_na_eliminatie}} |
| Bedrijfskosten (na eliminatie intragroep-kosten) | −{{bedrijfskosten_na_eliminatie}} |
| **Bedrijfsresultaat** | **{{bedrijfsresultaat}}** |
| Aandeel in het resultaat van vennootschappen waarop vermogensmutatie is toegepast | {{aandeel_vermogensmutatie}} |
| Afschrijvingen op consolidatieverschillen | −{{afschrijvingen_consolidatieverschil}} |
| Financiële resultaten | {{financiele_resultaten}} |
| **Resultaat van het boekjaar** | **{{resultaat_boekjaar}}** |
| Belasting | −{{belasting}} |
| **Netto-resultaat** | **{{netto_resultaat}}** |
| Aandeel van de groep | {{aandeel_groep}} |
| **Aandeel van derden in het resultaat** | **{{aandeel_van_derden}}** |
```

## Toetsing

- `bedrijfsopbrengsten_totaal − bedrijfskosten_totaal = bedrijfsresultaat`
- `bedrijfsresultaat + financiële opbrengsten − financiële kosten = resultaat_voor_belasting`
- `resultaat_voor_belasting − belasting = netto_resultaat`
- **VERIFY-aspect `resultatenrekening.klopt-niet`**: opbrengsten − kosten ≠ resultaat
- Geconsolideerd: `netto_resultaat = aandeel_groep + aandeel_van_derden`
- `aandeel_van_derden = (1 − belang%) × resultaat_dochter` per integraal opgenomen dochter

## Cast-conventie

- Bedragen in €, duizendtallen
- Resultaten kunnen negatief (verlies — schrijf `−€ 50.000`)
- Verhoudingen plausibel: nettowinst typisch 3-15% van omzet voor gezonde BV

## Wanneer dit template gebruiken

- Demonstratie van intragroep-eliminaties op opbrengsten/kosten
- Aandeel-van-derden-berekening (geconsolideerd)
- Vermogensmutatie-resultaat-effect (één regel toegevoegd)
- Afschrijving consolidatieverschil-impact
