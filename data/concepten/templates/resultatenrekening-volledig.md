# Volledige resultatenrekening (KB WVV-rubrieken)

Volledig schema met bedrijfs/financieel/uitzonderlijk onderscheid. Gebruik wanneer de bouwsteen/stap categorisering vereist (bv. waar zitten afschrijvingen op consolidatieverschil — bedrijfs- of financiële kosten).

## Markdown-skelet (enkelvoudig)

```markdown
| {{vennootschap_naam}} — Resultatenrekening {{boekjaar}} | EUR |
|---|---:|
| **I. Bedrijfsopbrengsten** | {{bedrijfsopbrengsten_totaal}} |
| A. Omzet | {{omzet}} |
| B. Wijziging voorraden | {{wijziging_voorraden}} |
| C. Geproduceerde vaste activa | {{geproduceerde_va}} |
| D. Andere bedrijfsopbrengsten | {{andere_bedrijfsopbrengsten}} |
| **II. Bedrijfskosten** | −{{bedrijfskosten_totaal}} |
| A. Handelsgoederen, grondstoffen en hulpstoffen | −{{kosten_handelsgoederen}} |
| B. Diensten en diverse goederen | −{{diensten}} |
| C. Personeelskosten | −{{personeelskosten}} |
| D. Afschrijvingen, waardeverminderingen, voorzieningen | −{{afschrijvingen_voorzieningen}} |
| E. Andere bedrijfskosten | −{{andere_bedrijfskosten}} |
| **III. Bedrijfsresultaat** | **{{bedrijfsresultaat}}** |
| **IV. Financiële opbrengsten** | {{financiele_opbrengsten}} |
| **V. Financiële kosten** | −{{financiele_kosten}} |
| **VI. Resultaat uit gewone bedrijfsuitoefening vóór belastingen** | **{{rgg_voor_belasting}}** |
| **VII. Uitzonderlijke opbrengsten** | {{uitzonderlijke_opbrengsten}} |
| **VIII. Uitzonderlijke kosten** | −{{uitzonderlijke_kosten}} |
| **IX. Resultaat vóór belastingen** | **{{resultaat_voor_belasting}}** |
| **X. Belastingen op het resultaat** | −{{belasting}} |
| **XI. Resultaat van het boekjaar** | **{{resultaat_boekjaar}}** |
```

## Markdown-skelet (geconsolideerd — KB WVV art. 3:144)

```markdown
| {{groep_naam}} — Geconsolideerde resultatenrekening {{boekjaar}} | EUR |
|---|---:|
| **I. Bedrijfsopbrengsten** (na eliminatie intragroep) | {{bedrijfsopbrengsten}} |
| **II. Bedrijfskosten** (na eliminatie intragroep) | −{{bedrijfskosten}} |
| **III. Bedrijfsresultaat** | **{{bedrijfsresultaat}}** |
| **IV. Financiële resultaten** (na eliminatie intragroep) | {{financiele_resultaten}} |
| **V. Aandeel in resultaat van vennootschappen waarop vermogensmutatie is toegepast** (KB WVV art. 3:145) | {{aandeel_vermogensmutatie}} |
| **VI. Afschrijving op positieve consolidatieverschillen** | −{{afschrijving_consolidatieverschil}} |
| **VII. Belastingen** | −{{belasting}} |
| **VIII. Resultaat van het boekjaar** | **{{resultaat_boekjaar}}** |
| Aandeel van derden in het resultaat (KB WVV art. 3:137) | {{aandeel_van_derden}} |
| **Aandeel van de groep** | **{{aandeel_groep}}** |
```

## Toetsing

- I − II = III (bedrijfsresultaat)
- III + IV − V = VI (resultaat uit gewone bedrijfsuitoefening) — enkelvoudig
- VI + VII − VIII = IX (resultaat vóór belastingen)
- IX − X = XI
- Geconsolideerd: VIII = aandeel_groep + aandeel_van_derden
- **VERIFY-aspect `resultatenrekening.klopt-niet`** voor alle sommen

## Cast-conventie

Identiek aan verkorte versie. Voor demonstraties: vul alleen relevante posten in, anderen op €0 of weglaten met dummy-aanduiding.

## Wanneer dit template gebruiken

- Voor het tonen waar precies een post verschijnt in de resultatenrekening (bv. afschrijving consolidatieverschil als afzonderlijke post — VI)
- Voor demonstratie van het verschil tussen bedrijfs- en financiële kosten bij intragroep-eliminaties
- Bij berekening van aandeel-van-derden in geconsolideerd resultaat
