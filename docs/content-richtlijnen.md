# Content-richtlijnen: fiches schrijven voor Certificaid

Gedetailleerde regels voor het schrijven van materie-fiches, competentie-fiches en programmaonderdeel-fiches. Van toepassing bij elke PO-build en bij manuele ficheaanpassingen.

**Verwante docs**: [`docs/po-builder.md`](po-builder.md) — procesflow · [`docs/adr/INDEX.md`](adr/INDEX.md) — architectuurbeslissingen

---

## Drie lagen studiemateriaal

Het bekwaamheidsexamen toetst bekwaamheid = het vermogen om technieken correct toe te passen in onbekende situaties. Daarvoor zijn drie soorten studiemateriaal nodig:

| Laag | Vraag | Content | Bron van waarheid |
|------|-------|---------|-------------------|
| **Kennis** (materie) | Wat is X? Hoe werkt X? | Één concept per fiche in `content/materie/` | Wetteksten, CBN-adviezen |
| **Competentie** | Hoe pak ik dit type taak aan? | Één techniek per fiche in `content/competenties/` | ITAA-normen, CBN, beroepspraktijk |
| **Synthese** | Hoe combineer ik competenties over domeinen? | Voorbeeldexamenvragen bij programmaonderdelen | Voorbeeldexamens |

Materie = de blokjes. Competenties = de bouwtechnieken. Synthese = oefenen met beide tegelijk.

**Motiveringsstructuur**: elk antwoord op integratieniveau volgt **conclusie → grondslag → redenering**.

## Materie vs. competentie

**Canonieke thuisplaats**: elk stuk inhoud heeft één vaste plek — materie of competentie, nooit beide.

| Hoort in materie | Hoort in competentie |
|---|---|
| Definitie van een begrip | Hoe je een begrip gebruikt in een taakcontext |
| Drempelwaarden en criteria | Wanneer je welk criterium toepast |
| Formule van een ratio | Welke ratio's relevant zijn voor welk analysedoel |
| Wettelijke verplichting | Hoe je de naleving ervan verifieert |

**Naamgeving competenties**: altijd werkwoord + object, actiegericht. ✓ `continuiteit-beoordelen` — ✗ `falingspredictie-beoordelen`.

**Naam verifiëren na schrijven**: de naam is een hypothese. Na schrijven: dekt de naam het volledige bereik? Zo niet: hernoem vóór commit. Prioriteit: (1) gezaghebbende bron (ITAA-norm, wettekst) geeft een naam → gebruik die; (2) anders: draft-naam aanpassen.

**Concrete ankerpunten bij links**: geef altijd 1–3 voorbeelden of sleutelwoorden bij een link, niet alleen de link zelf.

**Gebruik van `→`**: alleen voor logische flow in tekst (`oorzaak → gevolg`) en voor PO-fiche takenbullets (`- → [[competentie|Naam]]`). Nooit als vervanging voor een gewone link.

## Terminologie

| Term | Betekenis |
|------|-----------|
| **TDKs** | Taken, Doelstellingen en Kenniselementen — de inhoud van een programmaonderdeel-fiche |
| **Materie** | Kennisfiches: één concept per fiche in `content/materie/` |
| **Competentie** | Techniekefiches in `content/competenties/` |
| **Concept / fenomeen** | Één coherent studieonderwerp met een eigen fiche |

Kenniselement-IDs uit de brochure (april 2022): 1.1–1.9 = accountancy · 2.1–2.8 = fiscaal · 3.1–3.2 = vennootschapsrecht · 4.0 = deontologie

## Status en tags

| Tags | Betekenis | Zichtbaar in Explorer |
|------|-----------|----------------------|
| `[wip]` | Actief in behandeling | Ja |
| `[wip, verborgen]` | Nog niet behandeld | Nee |
| *(geen wip-tag)* | Voltooid en geverifieerd | Ja |

**Nieuwe inzichten op geverifieerde fiches**: zet status terug naar `draft`, voeg `wip`-tag toe, noteer in CHANGELOG.md.

---

## Bronnen

### Primaire werkreferentie

| Index | Gebruik voor |
|---|---|
| `resources/bronnen/normen/INDEX.md` | Welke norm regelt procedure X? |
| `resources/bronnen/adviezen/INDEX.md` | Welk advies is relevant voor onderwerp X? |
| `resources/bronnen/wetteksten/WETTEKSTEN-INDEX.md` | Welke wet/KB behandelt onderwerp X? |
| `resources/voorbeeldexamens/INDEX.md` | Welk examen bevraagt PO X / concept Y? |

> **⚠️ Nummerverschuiving oude examens**: examens vóór 2022 gebruiken oude PO-nummering. Vertaaltabel: oud 2.1 PB = nieuw 2.2 · oud 2.2 VennB = nieuw 2.3 · oud 2.3 BTW = nieuw 2.4 · oud 2.4 Registratie = nieuw 2.5 · oud 2.6 Europees = nieuw 2.8.

**Werkwijze bronopzoeking**:
1. Lees de relevante INDEX.md — identificeer kandidaat-bronnen semantisch
2. Grep op thema via `  - [thema]` in frontmatter, of op vrije tekst in body
3. Lees de volledige gevonden passages voor citaat en verificatie
4. Ga enkel online als de bron niet lokaal beschikbaar is

### Bronhiërarchie

**Voor materie (kennis):**
1. Wetteksten in `content/bronnen/wetteksten/` (gecoördineerde versies)
2. Officiële wetteksten op ejustice.just.fgov.be
3. Fisconet.be (WIB92, WBTW)
4. CBN-adviezen in `resources/bronnen/adviezen/`
5. NBB-documentatie

**Voor competenties (technieken):**
1. ITAA-normen in `resources/bronnen/normen/`
2. CBN-adviezen
3. Administratieve circulaires FOD Financiën
4. Erkende handboeken — secundair, niet bindend
5. Geconstrueerde kennis — altijd 🤖 labelen

### Bronvermelding in fiches

**Inline bronnen** — elke feitelijke bewering over wetsinhoud:
- `([[wetteksten/XXI-wet-itaa#art-37|Wet ITAA art. 37]])`
- `([[wetteksten/XVII-antiwitwaswet#art-47|ITAA-LEX XVII · AWW art. 47]])`

**Ankers in wetteksten** — Quartz strips speciale tekens (`:`, `.`, `/`), spaties worden koppeltekens:
- `## Art. 47` → `#art-47`
- `## Art. 1:24` (WVV) → `#art-124`
- `## Art. III.82` (WER) → `#art-iii82`

**Ankers in materie-fiches** — emoji verdwijnt maar spatie erna blijft (→ leading dash):
- `## 📌 Witwassen van geld` → `#-witwassen-van-geld`
- `## 🔒 Meldingsplicht` → `#-meldingsplicht`

Geaccentueerde tekens worden behouden: `#-cel-voor-financiële-informatieverwerking-cfi` ✓

**Geen aparte "Bronnen en artikelen"-sectie** — bronverwijzingen inline in de tekst.

### Bronintegriteit en AI-labeling

- Elk feit in materie-secties moet traceerbaar zijn naar een concrete bron
- Schrijf NOOIT iets over wetsinhoud zonder bronverwijzing
- Onzeker: markeer als `⚠️ te verifiëren`
- Valkuilen, voorbeeldvragen en competentie-heuristieken mogen 🤖-gelabeld zijn

Confidence-labeling (zie ADR-007):
- ⚖️ `grounded` — direct traceerbaar naar bron met hoge autoriteit
- 🤖 `inferred` — redenering, constructie of analogie zonder directe bron

### Tegenstrijdige bronnen

- Vermeld beide standpunten expliciet
- Geef aan welke bron hogere rang heeft
- Markeer als `⚠️ te verifiëren`

---

## Programmaonderdeel-fiches

### Structuur

- Officiële tekst verbatim uit de brochure — geen parafrases
- AI-aanvulling (geïdentificeerde competenties) in aparte `#### Geïdentificeerde competenties` subsectie
- Competenties op taakniveau, niet op doelstellingniveau (N-N koppeling)
- Kenniselementen zonder materie-link: `*(⚠️ materie aan te maken)*`
- "TDK" is intern begrip — gebruik in fiches: "Kenniselement", "Taak", "Doelstelling"

### Template

```
---
explorer_title: "X.X Korte naam"
tags: ["X.X", wip, programmaonderdeel]
bouwversie: 1
---

# X.X Volledige naam van het programmaonderdeel

## Taken en doelstellingen

### Taak: [omschrijving verbatim uit brochure]

- [doelstelling 1 verbatim]

#### Geïdentificeerde competenties

- → [[competentie-fiche-a|Naam competentie A]]

## Kenniselementen

**I. Groepsnaam**
- I.A — [[materie-fiche|Naam kenniselement]]: omschrijving

## Relevante competenties

- [[competentie-fiche-a|Naam competentie A]]

## Relevante materie

- [[materie-fiche-a|Naam concept A]]
```

### Verificatiestap

1. Elke TDK → link naar juiste sectie in conceptfiche?
2. Elke fiche in "Relevante materie" → dekt alle TDKs die ernaar linken?
3. TDKs zonder materie-link? → maak aan of voeg toe als sectie
4. Laagcheck (bij `niveau: integratie`): Weten (📌⚖️🔒), Toepassen (📋🔢✅👤), Integreren (🔎🚩↔️)

**"Relevante materie" volledigheidseis**: een student die alleen deze lijst doorloopt, moet alle examenstof gezien hebben — geen subset.

---

## Competentie-fiches

### Granulariteit en compositie

- Één competentie per zelfstandig toetsbaar examenvaardigheidtype
- Compositie: competentie kan andere competentie aanroepen als sub-stap — nooit herhalen

### Staptypes

| Icoon | Type | Vraag die het beantwoordt |
|---|---|---|
| 🎯 | Doel | Wat wil ik bereiken? |
| 🔍 | Vaststelling | Wat is dit? Welke categorie? |
| 🔀 | Beslissing | Welke optie is van toepassing? |
| 🔢 | Berekening | Wat is de waarde? |
| 📊 | Diagnose | Wat betekenen de signalen in context? |
| 💬 | Synthese | Wat is het totaalplaatje? |

💬 Synthese en 📊 Diagnose bestaan **uitsluitend** als competentie-staptype — niet in materie.

### Regels voor stappen

**Elke stap heeft een `📥/📤`-blok**:
```markdown
> 📥 **Nodig**:
> - [[andere-competentie#stap-x|Output van stap X]]
>
> 📤 **Uitkomst**:
> - Resultaat A
```

**Elke stap begint met een "waarom"-zin** — niet wat je doet maar waarom. Zonder die zin is de stap een instructie zonder grond.

**Stapnamen**: instructievorm, actief, zonder vraagteken. ✓ "Balans herstructureren" — ✗ "Welk schema is van toepassing?"

**Visueel anker** (code-blok): verplicht bij stappen die inwerken op een financieel document.

**`[!info]- Concreet`**: verplicht bij stappen die een oordeel of beslissing vereisen zonder visueel anker.

**Stap vanuit perspectief van de beroepsbeoefenaar**: de beroepsbeoefenaar (GA/GBA) is steeds de actor. Niet "het bestuursorgaan doet X" maar "controleer of het bestuursorgaan X heeft gedaan."

**Optionele/conditionele stap = aparte genummerde stap**: `### 5c. 🔒 [Naam] (indien [conditie])`.

**Grondslag-blok** (altijd collapsible):
```markdown
> [!info]- Grondslag van deze werkwijze (🤖 60% · ⚖️ 40%)
> [Beschrijf de grondslag van de procedure als geheel]
```

**Voorbeelden verplicht**: minstens één uitgewerkt voorbeeld (Situatie / Conclusie / Grondslag / Redenering).

### Template

```markdown
---
tags: ["X.X", wip, competentie]
niveau: integratie
status: draft
bouwversie: 1
programmaonderdelen: ["X.X"]
itaa-lex-secties:
  - [sectie] ([wet] art. X–Y)
procedure-grondslag: "[ITAA-norm X / CBN-advies YYYY/NN / analytische praktijk 🤖]"
---

# Naam van de competentie

> [!info]- Grondslag van deze werkwijze (🤖 X% · ⚖️ Y%)
> ...

## Aanbevolen werkwijze

### 1. 🔍 [Stap]

> 📥 **Nodig**: ...
> 📤 **Uitkomst**: ...

**Waarom**: ...

## Voorbeelden

> [!example]- [Naam situatie]
> **Situatie**: ... **Conclusie**: ... **Grondslag**: ... **Redenering**: ...

## Motiveren op het examen

> [!question]- [Vraagnaam]
> > [!success]- Antwoord
> > **Verdict**
```

---

## Materie-fiches

### Wat is een concept?

Een concept is de **kleinste coherente eenheid die een student als één geheel moet begrijpen**.

- Concepten worden gedefinieerd door het **reële fenomeen**, niet door de juridische structuur: ✓ "antiwitwaswetgeving" — ✗ "AWW art. 47"
- **Vakoverschrijdend is gewenst**: één fiche voor alle contexten (vakken zijn examen-organisatielaag)
- **Secties volgen topics, niet vakken**: `↔️ Boekhoudkundig vs. fiscaal` geeft meer inzicht dan twee vak-secties

### Sectietypes (10)

| Emoji | Type | Vraag |
|---|---|---|
| 📌 | Begrip | Wat is X? |
| ⚖️ | Principe | Hoe werkt X als algemene regel? |
| 📋 | Procedure | Welke stappen volg je? |
| 🔢 | Berekening | Hoe reken je X uit? |
| ↔️ | Vergelijking | Wat is het verschil tussen X en Y? |
| ✅ | Checklist | Wat controleer je? |
| 🔒 | Verplichting | Wat moet verplicht gebeuren? |
| 👤 | Rol | Wie doet wat? |
| 🔎 | Patroon | Hoe herken je dat iets normaal is? |
| 🚩 | Antipatroon | Hoe herken je dat iets fout gaat? |

**Kennislagen**:
- Weten: 📌⚖️🔒
- Toepassen: 📋🔢✅👤
- Integreren: 🔎🚩↔️

### Schrijfstijl

- **Menselijke, heldere taal** — geen legalese, wel precies
- **Hoofdregel eerst, uitzondering daarna** — nooit omgekeerd
- **Oorzaak → gevolg** — "X leidt tot Y", niet "Y wordt opgelegd wanneer X"
- **Actieve zin boven passieve** — de actor is wat de student moet onthouden
- **Parallelstructuur in opsommingen** — alle items volgen dezelfde grammaticale structuur
- **Niet herhalen — wel verwijzen** — zelfde info nooit twee keer
- **Geen hyperlinks in titels van callouts** — niet gerenderd door Quartz
- **Wikilinks** — elk concept dat een fiche heeft, krijgt een link bij elke vermelding
- **"(zie § X)" → klikbare wikilink** — `[[fiche#anker|sectienaam]]`, nooit plain text
- **Formule-variabelen**: gebruik betekenisvolle afkortingen (NBK, TA, EBIT, MVE, VV, O)
- **Wetsartikelnamen horen in voetnoten** — niet inline in zinnen (uitzonderingen: artikel is zelf het onderwerp; tabelcellen)

**Structuurvolgorde binnen een fiche**:
1. Begrippen — van hoog naar detail
2. Principes/regels — gebruiken alleen al uitlegde begrippen
3. Procedures — sanctie direct bij de verplichting
4. Vergelijkingen — pas nadat alle betrokken begrippen uitgelegd zijn
5. Rollen — wie doet wat

### Hoe een nieuwe conceptfiche starten

1. Controleer op duplicaten — ook onder andere naam
2. Verifieer de bronnen — voldoende bronmateriaal?
3. Begin met begrippen
4. Markeer onzekerheden als `⚠️ te verifiëren`
5. Zet status op `draft` — alleen de gebruiker zet `geverifieerd`

**Zoek eerst, schrijf daarna**: altijd zoeken naar de meest logische bestaande plek voor nieuwe info.

### Template

```markdown
---
tags: ["4.0", wip, materie]
niveau: integratie
status: draft
bouwversie: 1
bronnen:
  - Wet ITAA art. 37
---

# Naam van het concept

## 📌 Term A
Definitie. ([[wetteksten/XXI-wet-itaa#art-2|ITAA-LEX XXI · Wet ITAA art. 2]])

## ⚖️ Naam van het principe
Inhoud.

> [!warning]- Correcte bewering als titel
> ❌ *"De verkeerde aanname."*
> Correcte uitleg.
> 🤖 *AI-aanvulling*

> [!info]- In de praktijk
> Concrete situatie.
> 🤖 *AI-aanvulling*

## Relevant voor

**[[X.X-naam|X.X Naam van het programmaonderdeel]]**

Taken:
- *Naam van de taak*

### Voorbeeldvragen

> [!question]- Korte vraagnaam
>
> Vraag volledig geformuleerd.
>
> Juist of fout?
>
> > [!success]- Antwoord
> >
> > **Fout.**
> > Uitleg.
>
> 🤖 *AI-aanvulling*
```

### Callout-conventies

**Valkuil** (`[!warning]-`):
- Titel vermeldt **altijd de correcte bewering** — declaratief voor feiten ("CBN-adviezen zijn niet juridisch bindend") of imperatief voor handelingen ("Gebruik EV vóór winstverdeling bij ROE")
- Body: foutieve aanname cursief + aanhalingstekens als eerste regel, dan correcte uitleg

**Voorbeeldvraag** (`[!question]-` genest met `[!success]-`):
- Lege regel na elke callout-opening (Quartz nesting)
- "Juist of fout?" op aparte regel
- Verdict vetgedrukt op eerste regel van antwoord

**In de praktijk** (`[!info]-`):
- 🤖 staat onderaan, na de tekst
- Altijd 🤖 tenzij situatie rechtstreeks uit een bron komt

---

## Bouwversie

Elke fiche bevat `bouwversie: N`. Fiches met lagere versie dan de huidige zijn kandidaat voor heraudit.

**Huidige versie: 2**

| Versie | Datum | Wijzigingen |
|---|---|---|
| 0 | vóór 2026-05-02 | Pre-versioning |
| 1 | 2026-05-02 | Waarom-zin verplicht; grondslag-blok collapsible; synoniemen als cursieve subtitel; fiche-titel = kernfenomeen; formule-variabelen betekenisvol; "(zie § X)" → wikilink; geen hyperlinks in callout-titels |
| 2 | 2026-05-02 | Valkuil-titels = correcte bewering; visueel anker verplicht; [!info]- Concreet verplicht; topic-secties i.p.v. vak-secties; scope-vernauwing detectiestap |

**Versie ophogen**: bij elke wijziging aan content-richtlijnen die bestaande fiches suboptimaal maakt.

**Stale fiches vinden**:
```bash
grep -rL "bouwversie" content/materie content/competenties content/programmaonderdelen
grep -r "bouwversie: 0" content/
```

---

## Kwaliteitschecks

### Semantische hyperlinkdoorlezing

Lees elke zin opnieuw: **"heeft deze passage betrekking op iets dat ergens een anker heeft?"**

| Type passage | Actie |
|---|---|
| Begrip wordt gebruikt | Link naar `##`-sectie in de juiste fiche |
| Verplichting wordt beschreven | Link naar sectie met die verplichting |
| Uitzondering verwijst impliciet naar ander concept | Link naar dat concept |
| Opsomming met termen die elk een sectie hebben | Elk item afzonderlijk linken |
| Callout-tekst verwijst naar begrippen | Ook in callouts links verwacht |

**Polyseme termen altijd kwalificeren**: "meldingsplicht [[continuiteitsrisico#...|bij continuïteitsrisico]]" vs. "[[antiwitwaswetgeving#...|meldingsplicht]] (AWW)".

**Links inline op het conceptwoord** — nooit als losstaande verwijzing achteraan.

### Kritische lezing

Stelregel: **als een student een vraag heeft die de tekst niet beantwoordt, is de zin onvolledig.**

Signaalzinnen om te vermijden: "in bepaalde gevallen", "de bevoegde autoriteit", "er zijn bepaalde voorwaarden", "dit is verboden" (zonder precisering).

**Structuurproblemen**:

| Probleem | Correctie |
|---|---|
| Gevolg vóór oorzaak | "X leidt tot Y", niet "Y wordt opgelegd wanneer X" |
| Passieve zin verbergt actor | Herschrijf actief |
| Vergelijking vóór begrippen | Tabel pas na introductie alle betrokken concepten |
| Abstract principe instrument-specifiek geframed | Scope intro naar algemeen niveau; applicatie naar instrumentfiche |

### Feedback als verbeterimpuls

Bij inhoudelijke feedback: stel jezelf de vraag **"Hoe had ik dit zelf kunnen detecteren?"** en voeg een concrete verificatiestap toe aan de meest relevante sectie van dit document.
