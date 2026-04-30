---
tags: ["1.2", wip, materie]
niveau: integratie
status: draft
bronnen: []
itaa-lex: ""
---

# Kasstroomanalyse

De jaarrekening toont winst en vermogen op een bepaald moment, maar niet de werkelijke geldstromen. Een onderneming kan winstgevend zijn en toch betalingsproblemen hebben — wanneer de winst vastzit in niet-geïnde vorderingen of voorraden. De kasstroomanalyse reconstrueert de werkelijke **bewegingen van geld** en maakt de kloof tussen boekhoudkundige winst en kasgeneratie zichtbaar.

---

## 📌 Kasstroom

Een kasstroom is een werkelijke in- of uitstroom van geld (of geldequivalenten). Kasstromen worden onderverdeeld in drie activiteiten:

| Type | Omschrijving | Voorbeelden |
|------|-------------|-------------|
| **Operationeel** | Geldstromen uit de gewone bedrijfsactiviteit | Ontvangen van klanten, betalen van leveranciers en personeel |
| **Investering** | Geldstromen uit aan- of verkoop van vaste activa | Aankoop machine, verkoop deelneming |
| **Financiering** | Geldstromen uit vermogenswijzigingen | Dividenduitkering, nieuwe lening, terugbetaling lening, kapitaalverhoging |

---

## 📌 Indirecte methode

De meest gebruikte manier om de operationele kasstroom te berekenen: vertrekken vanuit de **nettowinst** en corrigeren voor niet-kasboekingen en werkkapitaalmutaties.

**Stap 1 — Start met nettowinst**

**Stap 2 — Tel niet-kaskosten terug bij** (ze zijn als kost geboekt maar er is geen geld uitgestroomd):
- [[afschrijvingen|Afschrijvingen]]
- [[waardeverminderingen|Waardeverminderingen]]
- Voorzieningen (toename)

**Stap 3 — Trek niet-kasopbrengsten af** (ze zijn als opbrengst geboekt maar er is geen geld binnengestroomd):
- Terugname waardeverminderingen
- Terugname voorzieningen

**Stap 4 — Corrigeer voor werkkapitaalmutaties**:
- Stijging voorraden → geld uitgestroomd (−)
- Daling voorraden → geld vrijgekomen (+)
- Stijging handelsvorderingen → geld nog niet ontvangen (−)
- Daling handelsvorderingen → meer geld ontvangen (+)
- Stijging leveranciersschulden → betalingen uitgesteld (+)
- Daling leveranciersschulden → meer betaald (−)

**Resultaat** = Operationele kasstroom

> [!info]- In de praktijk
>
> Een onderneming boekt een winst van € 200.000. Ze heeft € 80.000 aan afschrijvingen (geen kasuitstroom). Maar haar handelsvorderingen zijn gestegen met € 150.000 (klanten betalen trager). Operationele kasstroom: € 200.000 + € 80.000 − € 150.000 = € 130.000. De winst is hoger dan de kasstroom — dat geld zit vast bij klanten.
>
> 🤖 *AI-aanvulling*

---

## ⚖️ Interpretatie van de drie kasstromen

**Operationele kasstroom** moet positief zijn voor een gezond bedrijf. Een negatieve operationele kasstroom betekent dat de kernactiviteit geld verbruikt in plaats van genereert.

**Investeringskasstroom** is doorgaans negatief voor groeiende ondernemingen (ze investeren). Een positieve investeringskasstroom kan wijzen op verkoop van activa — wat niet noodzakelijk slecht is, maar wel context vereist.

**Financieringskasstroom** is positief bij kapitaalverhogingen en nieuwe leningen; negatief bij aflossingen en dividenduitkeringen.

**Vrije kasstroom** (Free Cash Flow)
= Operationele kasstroom − Investeringen in vaste activa

De vrije kasstroom is de kasstroom die overblijft na de investeringen die nodig zijn om de activiteit te onderhouden. Ze geeft aan hoeveel cash beschikbaar is voor dividenden, schuldaflossing of groei-investeringen.

---

## ↔️ Kasstroom vs. winst

| | **Winst** | **Operationele kasstroom** |
|-|-----------|--------------------------|
| Basis | Boekhoudkundig resultaat | Werkelijke geldbewegingen |
| Bevat afschrijvingen | Ja (als kost) | Nee (niet-kascost, terug bijgeteld) |
| Bevat onbetaalde omzet | Ja (als opbrengst) | Nee (gecorrigeerd via werkkapitaal) |
| Manipulatiegevoelig | Meer (keuze waarderingsregels) | Minder (cash is objectief) |

---

> [!warning]- Een winstgevende onderneming heeft altijd positieve kasstromen
> ❌ *"De onderneming maakt winst, dus haar kasstromen zijn positief."*
>
> Winst en kasstromen lopen niet synchroon. Een sterk groeiende onderneming kan een hoge winst boeken maar negatieve operationele kasstromen hebben doordat ze steeds meer geld vastzet in hogere voorraden en uitstaande vorderingen. Dit fenomeen — snel groeien terwijl de kaspositie daalt — heet "overtrading" en is een van de meest voorkomende oorzaken van faillissement bij winstgevende bedrijven.
>
> 🤖 *AI-aanvulling*

> [!warning]- Een negatieve investeringskasstroom is altijd slecht
> ❌ *"De onderneming heeft een negatieve investeringskasstroom van € 2 miljoen — dat is zorgwekkend."*
>
> Een negatieve investeringskasstroom betekent dat de onderneming investeert — en dat is voor een groeiende onderneming **normaal en verwacht**. Zorgwekkend zou het pas zijn als ze meer investeert dan haar operationele kasstromen genereren zonder daarvoor financiering aan te trekken. Context is alles: bekijk de vrije kasstroom (operationeel − investeringen) en of de investeringen renderen.
>
> 🤖 *AI-aanvulling*

---

## Relevant voor

**[[1.2-boekhoudrecht-en-jaarrekeningenrecht|1.2 Boekhoudrecht en jaarrekeningenrecht]]**

Taken:
- *Opstellen van de individuele jaarrekening*
  - Berekenen van de elementen nodig voor een interpretatie van de kasstromen en ze interpreteren (doelstelling 3)
