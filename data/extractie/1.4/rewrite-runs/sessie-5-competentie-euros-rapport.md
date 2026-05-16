# Sessie 5 — Competentie €-bedragen rapport

**Datum**: 2026-05-16
**Door**: handmatige Read+Edit-pas (geen scripting, conform briefing)
**Scope**: 9 competentie-yamls in `data/concepten/competenties/` — parallel aan Sessie 3 records-update (cast-consistente €-bedragen in Belgisch formaat)

## Gewijzigd (4 yamls)

| Yaml | Scenario('s) | Hoofdvervangingen |
|---|---|---|
| `uitvoeren-eerste-consolidatie.yaml` | basis_consolidatie (Aurelia/Brugse) + geassocieerde (Antwerpse/Drukkerij) | 320/300/240/80 → € 1.600.000 / € 1.500.000 / € 1.200.000 / € 400.000; toerekening terreinen € 250.000; residu € 150.000; EV-afsluit 400 → € 2.000.000; resultaat 100 → € 500.000; aandeel derden 80/20 → € 400.000/€ 100.000; goodwill-afschrijving € 150.000/5 = € 30.000/jaar. Voorbeelden[]-geassocieerde: 200/600/150/50 → € 350.000 / € 1.250.000 / € 312.500 / € 37.500; jaarafschrijving € 7.500. |
| `uitvoeren-intragroep-eliminaties.yaml` | basis_consolidatie (Aurelia/Brugse 90 %) + joint_venture (Cardinal/Filmstudio) | Intragroep-vordering 50 → € 250.000 (stap 2); voorraadwinst 25 %/400/100 → 25 %/€ 200.000/€ 50.000 (stap 3); joint_venture-pro-rata 100/50 → € 50.000/€ 25.000 (stap 5); EV-afsluit 1.000 → € 2.000.000, resultaat 200 → € 500.000, aandeel derden 100/20 → € 200.000/€ 50.000 (stap 7 + voorbeelden[]). |
| `verwerken-wijziging-consolidatiekring.yaml` | step-acquisition (Antwerpse → Drukkerij) + basis-realisatie (Aurelia → Brugse) | EV Drukkerij 800 → € 1.250.000; pro-rata 480 → € 750.000; aandeel derden 320 → € 500.000 (stap 4 + voorbeeld[0]). Brugse-realisatie: oorspronkelijk consolidatieverschil 80 → € 150.000 (residu); afboeking 24 → € 45.000; resterend 56 → € 105.000; nieuw aandeel derden 30 % × € 2.000.000 = € 600.000 (stap 5 + voorbeeld[1]). |
| `berekenen-controle-en-belangenpercentage.yaml` | basis-variant 90 % (voorbeelden[1]) | EV 1.000 → € 2.000.000; aandeel derden 100 → € 200.000. Ketenvoorbeeld (Aurelia 80 % → Brugse 60 % → Cardinal) ongewijzigd — toont rekenregel zonder €-bedragen. |

## Niet gewijzigd (5 yamls) — gemotiveerd

- **`kiezen-consolidatiemethode.yaml`**: bevat alleen kwalificaties + percentages, geen €-bedragen in scenario-context.
- **`kwalificeren-relatie-deelneming.yaml`**: alleen percentages (25 %, 20 %, 50/50). Geen scenario-bedragen.
- **`bepalen-consolidatieverplichting.yaml`**: bevat "20 mln EUR" en "8.000 EUR" als drempel-illustraties voor groottecriteria — geen scenario-context met abstracte 320/etc. (briefing: "als getal niet duidelijk scenario-deel is, niet vervangen").
- **`afbakenen-consolidatiekring.yaml`**: zelfde reden — "omzet 8.000 EUR" is drempel-illustratie.
- **`toepassen-uniforme-waarderingsregels.yaml`**: bedragen (100 LIFO / 130 FIFO / +30 / 200 / 50 / 150) horen bij waarderingsregel-cast Holsters Horst (afwijkende_afsluitingsdatum-scenario in `globaal.yaml`). Dit scenario komt niet voor in Sessie 3-records — er is geen canonieke €-set om mee af te stemmen. Aanpassing zou fabricatie zijn. Cast-naam blijft Holsters Horst, didactische getallen blijven; volgende sessie kan een waarderings-scenario in `globaal.yaml` toevoegen indien gewenst.

## Twijfelpunten

- **`berekenen-controle-en-belangenpercentage.yaml` voorbeelden[1]**: belang 90 % wijkt af van Sessie-3 basis-record `integrale-consolidatie` (80 %). Ik koos om EV € 2.000.000 (basis-canoniek) te behouden en aandeel derden 10 % × € 2.000.000 = € 200.000 te berekenen — dat is intern consistent en respecteert de variant-90 %-keuze van de oorspronkelijke voorbeeld-redactie.
- **`uitvoeren-intragroep-eliminaties.yaml` stap 7**: idem 90 %-variant; gekozen om € 2.000.000 / € 500.000 / € 200.000 / € 50.000 / € 450.000 toe te passen.
- **`verwerken-wijziging-consolidatiekring.yaml` stap 5 (realisatie)**: oorspronkelijk consolidatieverschil "80" interpretatie — Sessie 3 onderscheidt bruto (€ 400.000) en residu (€ 150.000). Ik kies residu (€ 150.000) omdat het op de geconsolideerde balans als "Consolidatieverschillen"-post staat; dat is wat een realisatie pro-rata afboekt.

## Mechanische check

- Alle vervangen bedragen in Belgisch €-formaat (€ 1.600.000, € 200.000 — punten als duizendtal-separator, geen komma-decimalen vereist binnen scenario's).
- Geen abstracte scenario-getallen meer in de 4 gewijzigde yamls (handmatige scan op 320/300/240/200/600/800 + spotchecks op 50/100 in scenario-velden).
- Cast-namen behouden waar reeds aanwezig (Aurelia/Brugse/Antwerpse/Drukkerij/Cardinal/Filmstudio).
- Confidence-labels ongewijzigd; geen nieuwe wetscitaten of stappen toegevoegd.
- `_provenance.sessie_5_competentie_euros_2026_05_16` toegevoegd aan de 4 gewijzigde yamls met `fields` + `reden`.

## Validatie

- `python3 -m tools.leermateriaal.render_competentie_fiche --alle`: 9/9 verwerkt, 0 overgeslagen.
- `python3 -m pytest tests/test_leermateriaal_render.py -q`: 56 passed.
- `npx quartz build`: 0 errors, 73 files emitted.

— Einde rapport.
