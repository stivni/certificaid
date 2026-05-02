---
tags: ["2.2", wip, materie]
niveau: integratie
status: draft
bouwversie: 2
bronnen:
  - WIB92 art. 126-178
  - Bijzondere wet financiering Gewesten en Gemeenschappen
---

# Belastingberekening personenbelasting

Van **belastbaar inkomen** naar **te betalen of te ontvangen bedrag** verloopt via een vaste keten van bewerkingen — federaal eerst, dan gewestelijk, dan gemeentelijk. Deze fiche geeft het volledige berekeningsschema en de kennis die nodig is om elke stap te begrijpen. Het uitvoeren van de berekening op een concreet dossier is de competentie [[belastingberekening-personenbelasting-uitvoeren|Belastingberekening personenbelasting uitvoeren]] *(⚠️ aan te maken)*.

Het schema is sinds de zesde staatshervorming (2014) **complexer** geworden door de splitsing tussen federale belasting en gewestelijke opcentiemen + gewestelijke verminderingen.

---

## 🔢 Berekeningsschema — overzicht

```
1. Belastbaar inkomen (gezamenlijk + afzonderlijk)
        ↓
2. Basisbelasting volgens federale progressieve tarieven
        ↓
3. − Belastingvrije som × federale schaal
        ↓
4. = Federaal verschuldigde belasting (vóór verminderingen)
        ↓
5. − Federale belastingverminderingen (pensioensparen, giften, ...)
        ↓
6. = Federaal te betalen belasting
        ↓
7. + Gewestelijke opcentiemen (Vlaanderen / Brussel / Wallonië)
8. − Gewestelijke belastingverminderingen (woonbonus, dienstencheques, ...)
        ↓
9. = Hoofdsom belasting
        ↓
10. + Gemeentelijke opcentiemen (% per gemeente — meestal 6 à 9%)
11. + Bijzondere bijdrage sociale zekerheid (BBSZ) - degressief
        ↓
12. = Eindbelasting vóór verrekening
        ↓
13. − Bedrijfsvoorheffing (al ingehouden door werkgever)
14. − Roerende voorheffing (verrekenbaar of bevrijdend)
15. − Voorafbetalingen
16. + Vermeerdering wegens onvoldoende voorafbetaling (zelfstandigen)
17. − Bonificatie wegens vroegtijdige voorafbetaling
        ↓
18. = Te betalen of te ontvangen
```

**Twee parallelle berekeningen** voor partners onder gezamenlijke aanslag — door de [[personenbelasting-basisbegrippen#-decumul|decumul]] worden stappen 1-9 voor elke partner afzonderlijk uitgevoerd, daarna samengevoegd voor de gemeenschappelijke aanslag.

---

## 🔢 Tarieven en belastingberekening

De **federale basisbelasting** wordt berekend volgens een **progressief schema** met vaste schijven en tarieven ([[bronnen/wetteksten/II-wib92|WIB92 art. 130]]):

| Schijf belastbaar inkomen (aj. 2026, indicatief — exacte bedragen via cijferzakboekje) | Tarief |
|---|---|
| € 0 – € 15 820 | 25% |
| € 15 820 – € 27 920 | 40% |
| € 27 920 – € 48 320 | 45% |
| Boven € 48 320 | 50% |

**Werking**: het tarief wordt **schijf per schijf** toegepast — geen sprong van het ene tarief naar het andere bij overschrijding van een drempel. De marginale en de gemiddelde aanslagvoet verschillen dus altijd.

**Voorbeeld** (vereenvoudigd, aj. 2026):

```
Belastbaar inkomen                  : € 50 000
   25% × € 15 820                   :  € 3 955
 + 40% × € 12 100                   :  € 4 840
 + 45% × € 20 400                   :  € 9 180
 + 50% × € 1 680                    :  €   840
                                   ──────────
Federale basisbelasting             : € 18 815
Marginale aanslagvoet               : 50%
Gemiddelde aanslagvoet              : 37,6%  (= 18 815 / 50 000)
```

> [!warning]- Marginale aanslagvoet en gemiddelde aanslagvoet zijn niet hetzelfde
> ❌ *"Een belastingplichtige die in de schijf van 50% belast wordt, betaalt 50% belasting op zijn inkomen."*
>
> Het tarief is **per schijf** — wie € 50 000 verdient, betaalt 25% op de eerste schijf (~ € 15 820), 40% op de tweede, enz. en pas 50% op het deel **boven € 48 320**. De **marginale aanslagvoet** is het tarief op de laatste euro inkomen (= 50% in het voorbeeld); de **gemiddelde aanslagvoet** is de totale belasting gedeeld door het inkomen (~ 37%). Wie de marginale aanslagvoet gebruikt om de totale belasting te schatten, overschat ze ruim.
>
> 🤖 *AI-aanvulling*

---

## 🔢 Belastingvrije som en toeslagen

De **belastingvrije som** is een schijf inkomen die **niet wordt belast** (= belast aan 0%) — geïmplementeerd als een vermindering van de belasting gelijk aan de belasting op die schijf ([[bronnen/wetteksten/II-wib92|WIB92 art. 131-145]]).

**Basisbedrag** (cijferzakboekje aj. 2026, indicatief): ~ € 10 570 per belastingplichtige. **Verhoogd** voor lage inkomens.

**Toeslagen voor [[gezinsfiscaliteit#-personen-ten-laste|personen ten laste]]** ([[bronnen/wetteksten/II-wib92|WIB92 art. 132]]):

| Aantal kinderen ten laste | Cumulatieve toeslag (cijferzakboekje aj. 2026, indicatief) |
|---|---|
| 1 kind | ~ € 1 920 |
| 2 kinderen | ~ € 4 950 |
| 3 kinderen | ~ € 11 090 |
| 4 kinderen | ~ € 17 940 |
| Per kind boven 4 | ~ € 6 850 |

De toeslagen zijn **niet-lineair** stijgend — een gezin met 4 kinderen krijgt aanzienlijk meer toeslag per kind dan een gezin met 1 kind. Reden: de marginale kost van extra kinderen relatief gezien lager is per kind, maar de fiscale tegemoetkoming wordt per kind hoger naarmate het gezin groeit.

**Bijkomende toeslagen**:
- Kind jonger dan 3 jaar zonder kinderoppasaftrek: extra toeslag (~ € 720)
- [[gezinsfiscaliteit#️-alleenstaande-ouder-toeslag|Alleenstaande ouder]] met kind ten laste: extra toeslag (~ € 1 920)
- Persoon met handicap (zelf, partner of ten laste): toeslag verdubbeld (telt als 2 personen ten laste)

**Mechanisme van de toepassing**:

```
Belastbare som = belastingvrije som + toeslagen
Vermindering belasting = belastbare som × tarief van laagste schijven (25% / 40% / 45% / 50%)
```

De vermindering wordt dus berekend op basis van de **laagste schijven** — dat maakt de belastingvrije som relatief méér waard voor lage inkomens (waar volledige som onder 25%-schijf valt) dan voor hoge inkomens (waar deels onder hogere schijven).

---

## 🔢 Federale belastingverminderingen

Verminderingen die op het **federale niveau** worden toegepast op de federale belasting. De belangrijkste ([[bronnen/wetteksten/II-wib92|WIB92 art. 145/1 e.v.]]):

| Vermindering | Tarief / formule |
|---|---|
| **Pensioensparen** | 30% van bestedingen, max. ~ € 1 020/jaar (aj. 2026) |
| **Langetermijnsparen** (premies levensverzekering, kapitaalaflossingen niet-eigen woning) | 30% van bestedingen, met geïndexeerde plafonds |
| **Giften** (≥ € 40 aan erkende instelling) | 45% van het bedrag |
| **Kinderoppas** (kinderen < 14 jaar) | 45% van betaald bedrag, max. € 16,80/dag/kind |
| **Werkgeverskredieten** (PWA-cheques, doelgroepvermindering) | Vaste tarieven |
| **Energiebesparende investeringen** (federaal — zonnepanelen vóór bepaalde datum) | In uitdoving |

**Vermindering vervangingsinkomsten** ([[bronnen/wetteksten/II-wib92|WIB92 art. 146-154]]): degressieve vermindering ten gunste van pensioenen, werkloosheidsuitkeringen, ziekte- en invaliditeitsuitkeringen — om de impact van de progressie op vervangingsinkomsten te verzachten.

**Voorrangsregel**: federale verminderingen worden **vóór** de gewestelijke verminderingen toegepast op de berekende belasting.

---

## 🔢 Gewestelijke opcentiemen en verminderingen

Sinds de **zesde staatshervorming** (2014) hebben de gewesten (Vlaanderen, Brussel, Wallonië) **autonome bevoegdheid** voor een deel van de PB op het beroeps- en onroerend inkomen van rijksinwoners van het gewest.

**Werking**:

1. Federale belasting wordt verminderd met een vast **% federale verminderingsfactor** (vermindering eigen aan elk gewest)
2. Daarop worden de **gewestelijke opcentiemen** toegepast (vast %, gewestelijk vastgesteld)
3. Vervolgens worden de **gewestelijke belastingverminderingen** toegepast

**Belangrijke gewestelijke verminderingen**:

| Vermindering | Vlaanderen | Brussel | Wallonië |
|---|---|---|---|
| **Eigen woning — geïntegreerde woonbonus** | In uitdoving (sinds 2020 stop voor nieuwe leningen) | Bestaat niet — vervangen door registratierechtenvermindering | "Chèque habitat" — afhankelijk van inkomen en kinderen |
| **Dienstencheques** | 20% (max. € 175/jaar/persoon) | 15% (max. € 174) | 10% (max. € 165) |
| **PWA-cheques / wijk-werken** | Vlaams-specifiek | — | — |
| **Monumentenzorg** | Specifieke regeling | — | — |
| **Renovatie / isolatie** | Verschilt per type werk | — | Specifieke "RénoPrêt" |

**Bevoegdheid wordt bepaald door fiscale woonplaats**: een Vlaamse rijksinwoner krijgt de Vlaamse opcentiemen en verminderingen, ook als hij elders werkt of investeert.

> [!warning]- Het gewest van toepassing is dat van de fiscale woonplaats, niet de werkplek
> ❌ *"Wie in Vlaanderen werkt en in Wallonië woont, krijgt de Vlaamse fiscale verminderingen."*
>
> De gewestelijke bevoegdheid in de PB wordt bepaald door het **gewest van de fiscale woonplaats op 1 januari van het aanslagjaar** — niet door de werkplek of de plaats waar het inkomen verdiend wordt. Een Waalse rijksinwoner die in Vlaanderen werkt, krijgt de Waalse opcentiemen en verminderingen. Bij een verhuizing tijdens het inkomstenjaar telt het gewest waar de belastingplichtige op 1 januari van het aanslagjaar gedomicilieerd is.
>
> 🤖 *AI-aanvulling*

---

## 🔢 Gemeentelijke en agglomeratiebelasting

**Aanvullende gemeentebelasting** ([[bronnen/wetteksten/II-wib92|WIB92 art. 466-470]]): elke gemeente bepaalt een **opcentiem** (% van de hoofdsom van de PB), meestal tussen **6% en 9%**.

```
Aanvullende gemeentebelasting = Hoofdsom PB × gemeentelijk opcentiem (%)
```

**Voorbeeld**:
- Hoofdsom PB: € 10 000
- Gemeente Antwerpen (8%): € 800 aanvullende gemeentebelasting
- Gemeente Knokke-Heist (0%): € 0

**Verschillen tussen gemeenten**: het gemeentelijk opcentiem is een fundamentele factor in de finale belastingdruk — een bedrijfsleider met hoog inkomen kan duizenden euro's per jaar besparen door verhuis naar een gemeente met laag opcentiem (Knokke-Heist 0%, De Panne 0%, Antwerpen 8%).

**Agglomeratiebelasting (Brussel)**: extra 1% in de Brusselse agglomeratie — bovenop het gemeentelijk opcentiem.

---

## 🔢 Bijzondere bijdrage sociale zekerheid (BBSZ)

Bijdrage geheven samen met de PB, **bestemd voor de sociale zekerheid** ([[bronnen/wetteksten/II-wib92|WIB92 art. 168 e.v.]] — wet van 30 maart 1994). Niet eigenlijk een belasting maar fiscaal verwerkt.

**Berekening**: degressief in functie van het belastbaar inkomen. Maximum ~ € 731/jaar/gezin (cijferzakboekje aj. 2026).

**Vrijstelling**: gezinnen met laag inkomen, bepaalde categorieën van vervangingsinkomsten.

---

## ⚖️ Bedrijfsvoorheffing en roerende voorheffing — verrekening

Voorheffingen zijn **voorschotten** op de uiteindelijke belasting. Ze worden ingehouden door de schuldenaar van het inkomen en betaald aan de FOD Financiën — en daarna verrekend met de aanslag.

**Bedrijfsvoorheffing (BV)** ([[bronnen/wetteksten/II-wib92|WIB92 art. 270-275]]):
- Schuldenaar: werkgever, vennootschap, debiteur van vervangingsinkomen
- Tarief: schalen volgens loonbarema's, gezinslast, voorafbetalingen
- **Volledig verrekenbaar** met de aanslag — eventueel teveel ingehouden BV wordt terugbetaald

**Roerende voorheffing (RV)** ([[bronnen/wetteksten/II-wib92|WIB92 art. 261-266]]):
- Schuldenaar: bank, vennootschap die dividenden uitkeert
- Tarief: 30% standaard (15% of 20% in specifieke gevallen — VVPRbis, gereglementeerde sparen)
- **Bevrijdend** voor de meeste roerende inkomsten — niet aangegeven, niet verrekend
- **Verrekenbaar** als de belastingplichtige de roerende inkomsten optioneel aangeeft (= globalisatie)

> [!warning]- Roerende voorheffing is in beginsel bevrijdend, niet verrekenbaar
> ❌ *"Een belastingplichtige met dividenden van € 5 000 met RV ingehouden, kan deze RV altijd verrekenen met zijn aanslag."*
>
> De RV op dividenden en interesten is **bevrijdend** — d.w.z. het inkomen wordt niet meer aangegeven en de RV wordt niet meer verrekend. De aanslag is volledig met de RV vereffend. Verrekening is enkel mogelijk als de belastingplichtige **vrijwillig globaliseert** (= aangeven in de PB) — meestal voordelig voor lage marginale tarieven (< 30%) of bij specifieke vrijstellingen (eerste schijf gereglementeerde spaarboekjes, vrijstelling eerste schijf dividenden ~ € 800).
>
> 🤖 *AI-aanvulling*

---

## 🔢 Voorafbetalingen en vermeerdering

**Voorafbetalingen (VA)** zijn **vrijwillige** vooruitbetalingen op de belasting — bedoeld om te vermijden dat de belastingplichtige op het einde van het jaar plots een groot bedrag moet betalen ([[bronnen/wetteksten/II-wib92|WIB92 art. 157 e.v.]]).

**Verplicht voor zelfstandigen, vrije beroepers en bedrijfsleiders** — voor werknemers in beginsel niet (BV is meestal voldoende).

**Vier kwartalen** (10 april, 10 juli, 10 oktober, 20 december van het inkomstenjaar) — elk met eigen percentage. Vroege betaling = grotere belastingvermindering.

**Vermeerdering wegens onvoldoende voorafbetaling**:

> Vermeerdering = (Hoofdsom × vermeerderingscoëfficiënt) − (∑ VA × bonificatiecoëfficiënt per kwartaal)

Als het saldo negatief is, valt de vermeerdering weg. **Doelstelling**: 90% van de belasting via voorheffing of voorafbetaling vóór het einde van het inkomstenjaar.

**Vermeerderingscoëfficiënt** voor aj. 2026: ~ 6,75% (afhankelijk van marktrente).

> [!info]- In de praktijk
>
> Een zelfstandige raamt zijn belasting voor inkomstenjaar 2025 op € 12 000.
>
> - Geen voorafbetalingen → vermeerdering = € 12 000 × 6,75% = € 810 te betalen bovenop de belasting
> - VA1 (10 april) = € 3 000 → bonificatie 9%, dekt 27% van de doelstelling
> - VA2 (10 juli) = € 3 000 → bonificatie 7,5%
> - VA3 (10 oktober) = € 3 000 → bonificatie 6%
> - VA4 (20 december) = € 3 000 → bonificatie 4,5%
>
> Voldoende voorafgebracht (90%-doelstelling gehaald) → geen vermeerdering. De vroegste VA hebben de hoogste fiscale waarde.
>
> 🤖 *AI-aanvulling*

**Bonificatie wegens vroegtijdige betaling** (voor wie meer dan nodig voorafbetaalt of als werknemer/loontrekkende vrijwillig voorafbetaalt): ~ 1,5% à 4,5% extra teruggave, afhankelijk van het kwartaal.

---

## 🔢 Eindbelasting en saldo

```
Eindbelasting vóór verrekening = hoofdsom + opcentiemen + BBSZ
                              − Bedrijfsvoorheffing
                              − Roerende voorheffing (indien verrekenbaar)
                              − Voorafbetalingen
                              + Vermeerdering wegens onvoldoende VA
                              − Bonificatie wegens vroegtijdige VA
                            = TE BETALEN of TE ONTVANGEN
```

Het aanslagbiljet dat de belastingplichtige ontvangt vermeldt het te betalen saldo (+ vervaldag) of het terug te ontvangen bedrag (rekeningnummer).

**Termijn van betaling**: doorgaans **2 maanden** na verzending van het aanslagbiljet, ook bij betwisting (tenzij vrijstelling van betaling werd toegestaan in het kader van [[fiscaal-bezwaar-voorbereiden|bezwaar]]).

---

## ⚖️ Globalisatie of afzonderlijke aanslagen

Bepaalde inkomsten worden niet aan de progressieve tarieven onderworpen, maar aan een **vast afzonderlijk tarief** ([[bronnen/wetteksten/II-wib92|WIB92 art. 171]]) — zie ook [[personenbelasting-basisbegrippen#️-globalisatie-en-afzonderlijke-aanslagen|Globalisatie en afzonderlijke aanslagen]] voor het algemeen overzicht.

| Inkomen | Tarief |
|---|---|
| Stopzettingsmeerwaarden materiële vaste activa (activiteit > 5 jaar) | 16,5% |
| Stopzettingsmeerwaarden cliënteel | 33% |
| Achterstallen van bezoldigingen | Gemiddelde aanslagvoet vorig jaar |
| Vakantiegeld vorig jaar uitgekeerd | Gemiddelde aanslagvoet vorig jaar |
| Pensioenkapitaal — vereffening op 60 jaar | 16,5% |
| Pensioenkapitaal — vereffening op 65 jaar | 10% |

**Vergelijkingsregel**: de wet legt op dat de **gunstigste oplossing** voor de belastingplichtige wordt toegepast. Als globalisatie voordeliger uitvalt dan de afzonderlijke aanslag, wordt globalisatie toegepast ([[bronnen/wetteksten/II-wib92|WIB92 art. 171]] in fine).

---

## Relevant voor

**[[2.2-personenbelasting|2.2 Personenbelasting]]**

Kenniselementen:
- XII — Uitgaven die recht geven op een gewestelijke belastingvermindering
- XIII — Uitgaven die recht geven op een federale belastingvermindering
- XIV — Inhoudingen aan de bron: aftrekbaarheid en terugbetaalbaarheid
- XV — Voorafbetalingen
- XVI — Vaststelling van het belastbaar inkomen en van de verschuldigde belasting
- XVII — Berekening van de belasting

### Voorbeeldvragen

> [!question]- Marginale vs. gemiddelde aanslagvoet
>
> Een belastingplichtige met een belastbaar inkomen van € 60 000 valt in de schijf van 50%. Hij beweert dat hij daarom 50% van zijn inkomen aan belasting betaalt — dus € 30 000.
>
> Juist of fout?
>
> > [!success]- Antwoord
> >
> > **Fout.**
> >
> > Het tarief is **per schijf** — wie € 60 000 verdient, betaalt enkel 50% op het deel **boven € 48 320** (~ € 11 680). De totale federale basisbelasting is ~ € 22 800 — d.w.z. een **gemiddelde** aanslagvoet van ~ 38%. Wie de marginale aanslagvoet (50%) gebruikt om de totale belasting te schatten, overschat aanzienlijk.
> >
> > *Zie: [[belastingberekening-personenbelasting#-tarieven-en-belastingberekening|Tarieven en belastingberekening]]*
>
> 🤖 *AI-aanvulling*

> [!question]- Gemeentebelasting bij verhuis
>
> Een belastingplichtige verhuist op 15 september 2025 van Antwerpen (8% opcentiem) naar Knokke-Heist (0%). Welke gemeentebelasting wordt voor aj. 2026 toegepast?
>
> > [!success]- Antwoord
> >
> > **De gemeentebelasting van de gemeente waar de belastingplichtige op 1 januari van het aanslagjaar gedomicilieerd is** — dus Knokke-Heist (0%).
> >
> > De aanvullende gemeentebelasting wordt bepaald op basis van het gemeentelijk opcentiem van de **fiscale woonplaats op 1 januari van het aanslagjaar** (1 januari 2026 voor aj. 2026). Wie tijdig verhuist, kan duizenden euro's besparen — een belangrijk fiscaal aandachtspunt voor hoge inkomens.
> >
> > *Zie: [[belastingberekening-personenbelasting#-gemeentelijke-en-agglomeratiebelasting|Gemeentelijke opcentiemen]]*
>
> 🤖 *AI-aanvulling*

> [!question]- Voorafbetaling kwartaal 1
>
> Een zelfstandige betaalt op 10 april 2025 een voorafbetaling van € 4 000 op zijn geraamde belasting van € 16 000 voor inkomstenjaar 2025. Welk percentage van de doelstelling is gedekt?
>
> > [!success]- Antwoord
> >
> > **Iets meer dan 30% van de doelstelling.**
> >
> > De doelstelling om vermeerdering te vermijden = 90% van de hoofdsom = € 14 400. De voorafbetaling van € 4 000 op kwartaal 1 wordt vermenigvuldigd met de bonificatie-coëfficiënt van kwartaal 1 (~ 9%, indicatief) — wat betekent dat de fiscale waarde van VA1 hoger is dan het nominale bedrag. Het resterende bedrag moet via VA2-VA4 of bedrijfsvoorheffing worden gedekt om de vermeerdering te vermijden. De vroegste VA dragen het meest bij — vandaar de aanbeveling om zo vroeg mogelijk te betalen.
> >
> > *Zie: [[belastingberekening-personenbelasting#-voorafbetalingen-en-vermeerdering|Voorafbetalingen en vermeerdering]]*
>
> 🤖 *AI-aanvulling*

> [!question]- Roerende voorheffing op spaarboekje
>
> Een belastingplichtige ontvangt € 1 200 interesten op een gereglementeerd spaarboekje. De bank heeft 0% RV ingehouden. Moet hij de interesten in zijn aangifte vermelden?
>
> > [!success]- Antwoord
> >
> > **Het deel boven de vrijgestelde schijf wel.**
> >
> > De **eerste schijf** van interesten op een gereglementeerd spaarboekje is **vrijgesteld** van RV en PB (~ € 1 020 voor aj. 2026, indicatief — cijferzakboekje raadplegen). Het deel **boven** de vrijgestelde schijf wordt belast aan **15% RV**. Bij niet-inhouding door de bank is de belastingplichtige verplicht het belastbare deel zelf aan te geven en de RV te betalen via de aangifte. Niet-aangifte is een fiscale inbreuk.
> >
> > *Zie: [[belastingberekening-personenbelasting#️-bedrijfsvoorheffing-en-roerende-voorheffing-verrekening|Roerende voorheffing]]*
>
> 🤖 *AI-aanvulling*
