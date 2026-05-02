---
tags: ["1.2", "1.3", wip, materie]
niveau: integratie
status: draft
bronnen: []
bouwversie: 0
---

# Resultaatniveaus

De resultatenrekening beschrijft hoe de [[jaarrekening|jaarrekening]] de opbrengsten en kosten van een boekjaar in lagen ordent — van de ruwe omzet tot de nettowinst die overblijft na belastingen. Elk niveau heeft een eigen economische betekenis en is de basis voor specifieke [[financiele-ratios|financiële ratio's]].

De techniek om de resultatenrekening te herstructureren staat in [[jaarrekening-herwerken]]. Hoe de niveaus gebruikt worden in een analyse staat in [[financiele-positie-beoordelen]].

---

## 📌 Resultaatniveaus

| Niveau | Berekening | NBB-code |
|---|---|---|
| **Netto-omzet** | Omzet na kortingen en retourzendingen | 70 |
| **Toegevoegde waarde (TAW)** | Omzet + andere bedrijfsopbrengsten − aankopen − diensten en div. goederen ± voorraadwijzigingen | 9900 |
| **Bedrijfsresultaat (EBIT)** | TAW − personeelskosten − [[afschrijvingen\|afschrijvingen]] − [[waardeverminderingen\|waardeverminderingen]] − andere bedrijfskosten | 9901 |
| **Resultaat vóór belastingen (EBT)** | EBIT + financieel resultaat + uitzonderlijk resultaat | 9903 |
| **Nettowinst** | EBT − belastingen op het resultaat | 9905/9906 |
| **EBITDA** | EBIT + [[afschrijvingen\|afschrijvingen]] + [[waardeverminderingen\|waardeverminderingen]] | 9901 + 630/634 |

> [!info]- In de praktijk: resultatenrekening van boven naar beneden
>
> 🤖 *AI-aanvulling*
>
> Een productiebedrijf (volledig schema, in €):
>
> ```
> Netto-omzet (70)                              8.000.000
> + Andere bedrijfsopbrengsten (74)                80.000
> − Aankopen handelsgoederen (60)              -3.200.000
> − Diensten en diverse goederen (61)            -800.000
> ± Voorraadwijziging gereed product (+/-)       +120.000
> ─────────────────────────────────────────────────────────
> = Toegevoegde waarde (9900)                   4.200.000   (52,5% van omzet)
>
> − Personeelskosten (62)                      -2.500.000
> − Afschrijvingen MVA (630)                     -600.000
> − Waardeverminderingen vlottende activa (634)   -50.000
> − Andere bedrijfskosten (64)                   -150.000
> ─────────────────────────────────────────────────────────
> = Bedrijfsresultaat EBIT (9901)                 900.000   (11,25% van omzet)
>
> + Financiële opbrengsten (75)                    20.000
> − Financiële kosten (65)                        -80.000
> ─────────────────────────────────────────────────────────
> = Resultaat vóór belastingen EBT (9903)         840.000
>
> − Belastingen op het resultaat (67/77)          -210.000
> ─────────────────────────────────────────────────────────
> = Nettowinst (9905)                             630.000   (7,88% van omzet)
>
> EBITDA = EBIT + afschrijvingen + wverm.
>        = 900.000 + 600.000 + 50.000     =     1.550.000   (19,38% van omzet)
> ```
>
> **Wat valt op:** de kloof tussen EBITDA (€ 1.550.000) en EBIT (€ 900.000) is groot — dit bedrijf heeft zware afschrijvingen, typisch voor een kapitaalintensieve productieomgeving. De brutomarge (TAW) van 52,5% is hoog; na personeels- en overheadkosten resteert slechts 11,25% als bedrijfsresultaat. De financiële kosten (€ 80.000) zijn beperkt in verhouding tot de EBITDA — de schuldenlast is draagbaar.

**Brutomarge** = netto-omzet − kostprijs van de verkochte goederen. Dit niveau valt vóór EBIT en wordt niet apart als NBB-code gepubliceerd in het wettelijk schema, maar is afleidbaar als onderdeel van de toegevoegde waarde (TAW).

**EBITDA-toelichting**: [[afschrijvingen|afschrijvingen]] en [[waardeverminderingen|waardeverminderingen]] worden in EBIT als kost afgetrokken, maar zijn geen effectieve kasuitstroom. Ze worden terug opgeteld om een proxy te krijgen voor de operationele kascreatie vóór financiering en belastingen.

> [!warning]- EBIT en EBITDA zijn hetzelfde
> ❌ *"EBIT en EBITDA zijn twee namen voor hetzelfde — het bedrijfsresultaat voor belastingen."*
>
> EBIT is het bedrijfsresultaat ná [[afschrijvingen|afschrijvingen]] en [[waardeverminderingen|waardeverminderingen]]. EBITDA voegt die niet-kaskosten terug bij voor een proxy van de operationele kascreatie. Voor kapitaalintensieve sectoren (bouw, industrie, telecom) is EBITDA zinvoller voor vergelijking, omdat afschrijvingsbeleid sterk kan verschillen. EBIT en EBITDA kunnen voor dezelfde onderneming sterk van elkaar afwijken.
>
> 🤖 *AI-aanvulling*

---

## 🔢 Effect van boekhoudkundige keuzes op ratio's

Boekhoudkundige keuzes beïnvloeden de [[financiele-ratios|ratio's]] zonder de economische realiteit te veranderen. De [[financiele-ratios#-brutoverkoopmarge|brutoverkoopmarge]] is een veelgetoetst voorbeeld.

**[[financiele-ratios#-brutoverkoopmarge|Brutoverkoopmarge]] = Toegevoegde waarde / Netto-omzet**

[[afschrijvingen|Afschrijvingen]] maken deel uit van de **bedrijfskosten** — ze liggen **onder** de brutoverkoopmarge in de resultatenrekening. Een verhoging van [[afschrijvingen|afschrijvingen]] verlaagt het bedrijfsresultaat (EBIT) maar heeft **geen effect** op de brutoverkoopmarge.

| Keuze | Effect op [[financiele-ratios#-brutoverkoopmarge\|brutoverkoopmarge]] | Effect op EBIT |
|---|---|---|
| [[afschrijvingen\|Afschrijving]] verhogen | ❌ Geen | Daalt |
| Voorraadwaardering verlagen | ✓ Daalt | Daalt |
| Omzet verhogen | ✓ Stijgt (als marge > 0) | Stijgt |

📝 *Voorbeeldexamen 2024: "Verhoging van de afschrijving op gebouwen heeft het volgende effect op de bruto verkoopmarge → Geen"*

> [!warning]- Afschrijving verhogen verlaagt de brutoverkoopmarge
> ❌ *"Als de [[afschrijvingen|afschrijving]] verhoogt, zal de [[financiele-ratios#-brutoverkoopmarge|brutoverkoopmarge]] dalen."*
>
> [[afschrijvingen|Afschrijvingen]] liggen structureel **onder** het brutomargepeil in de resultatenrekening. De [[financiele-ratios#-brutoverkoopmarge|brutoverkoopmarge]] = toegevoegde waarde / netto-omzet. [[afschrijvingen|Afschrijvingen]] zijn bedrijfskosten die pas ná de brutomarge in mindering komen. Ze verlagen EBIT, niet de brutomarge.
>
> 📝 *Voorbeeldexamen 2024*

---

## ⚖️ Contextualisering

Cijfers krijgen pas betekenis wanneer ze worden vergeleken:

- **Sectorgemiddelden**: een [[financiele-ratios#-brutoverkoopmarge|brutomarge]] van 15% kan hoog zijn in de detailhandel maar laag in de industrie
- **Historische trend**: is de marge stijgend, stabiel of dalend over drie jaar?
- **Nationale en internationale context**: recessie, rentestijgingen, sectorspecifieke wetgeving
- **Bedrijfsdomein**: een kapitaalintensieve onderneming heeft hoge [[afschrijvingen|afschrijvingen]] die EBIT drukken — vergelijking via EBITDA is dan zinvoller

> [!warning]- Een hogere winst betekent altijd een betere financiële positie
> ❌ *"De onderneming boekt een stevige winst — de financiële situatie is dus gezond."*
>
> Winst en liquiditeit zijn twee verschillende dingen. Een winstgevende onderneming kan in betalingsmoeilijkheden verkeren als haar [[balansaggregaten#-werkkapitaalbehoefte-wkb|werkkapitaalbehoefte]] snel stijgt — bijvoorbeeld doordat klanten trager betalen of [[voorraden|voorraden]] oplopen. De [[balansaggregaten#-netto-bedrijfskapitaal-nbk|balansaggregaten]] (NBK, WKB) geven een completere gezondheidscheck dan winst alleen.
>
> 🤖 *AI-aanvulling*

---

## Relevant voor

**[[1.2-boekhoudrecht-en-jaarrekeningenrecht|1.2 Boekhoudrecht en jaarrekeningenrecht]]**

Kenniselementen:
- Herstructurering van de resultatenrekening
- Toegevoegde waarde (TAW), bedrijfsresultaat (EBIT), EBITDA, nettowinst

**[[1.3-analyse-en-kritische-beoordeling-jaarrekening|1.3 Analyse en kritische beoordeling van de jaarrekening]]**

Taken:
- *Analyse en beoordeling van de financiële situatie aan de hand van de jaarrekeningen, ratio's en kengetallen*
  - In staat zijn om de jaarrekeningen kritisch te bekijken

Kenniselementen:
- II.B — Jaarrekening: resultatenrekening
- II.C.1 — Herwerking van de resultatenrekening

### Voorbeeldvragen

> [!question]- EBIT vs. EBITDA
>
> Een onderneming heeft een EBIT van € 300.000 en jaarlijkse [[afschrijvingen|afschrijvingen]] van € 80.000. Haar EBITDA bedraagt € 220.000.
>
> Juist of fout?
>
> > [!success]- Antwoord
> >
> > **Fout.**
> >
> > EBITDA = EBIT + [[afschrijvingen|afschrijvingen]] + [[waardeverminderingen|waardeverminderingen]]. [[afschrijvingen|Afschrijvingen]] worden bij EBIT **opgeteld** (ze waren al als kost afgetrokken en worden terug bijgeteld voor de cashproxy). EBITDA = € 300.000 + € 80.000 = **€ 380.000**, niet € 220.000.
> >
> > *Zie: [[resultaatniveaus#-resultaatniveaus|Resultaatniveaus]]*
>
> 🤖 *AI-aanvulling*
