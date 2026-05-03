---
tags: ["1.5", wip, competentie]
niveau: integratie
status: draft
bouwversie: 2
programmaonderdelen: ["1.5"]
itaa-lex-secties:
  - EU (Richtlijn 2013/34/EU als interpretatieve bron)
procedure-grondslag: "🤖 analytische praktijk — IFRS-standaarden zelf prescribeert geen werkwijze, alleen criteria per onderwerp"
---

# Transactie onder IFRS verwerken

Voor een specifieke transactie of post: identificeren welke IFRS-standaard van toepassing is, hoe de transactie wordt opgenomen en gemeten, en — bij vergelijking met Belgisch GAAP — welke afwijkingen materieel zijn. Deze competentie wordt typisch ingeroepen bij:

- de eerste IFRS-toepassing van een entiteit (welke posten verschillen materieel?)
- een nieuwe transactie binnen een bestaande IFRS-rapporterende entiteit
- de **consolidatieboeking** in de moedergroep wanneer de Belgische dochter onder Belgisch GAAP boekt
- **due diligence** bij overname van een IFRS-rapporterend bedrijf

Voor de bepaling of IFRS überhaupt van toepassing is, zie [[ifrs-toepassingskader-bepalen]].

> [!info]- Grondslag van deze werkwijze (🤖 70% · ⚖️ 30%)
>
> De individuele IFRS-standaarden zijn wettelijk bindend (via [[ifrs-rechtskader#-verordening-eg-nr-16062002|Verordening 1606/2002]] en endorsement-verordeningen) — de **criteria** zijn dus genormeerd. De **werkwijze** om systematisch een transactie tegen die criteria te toetsen is een analytische praktijk: er is geen IFRS-norm die voorschrijft "zo identificeer je welke standaard van toepassing is op een transactie".

## Aanbevolen werkwijze

### 1. 🔍 Aard van de transactie kwalificeren

> 📥 **Nodig**:
> - Beschrijving van de transactie of post (contract, document, gebeurtenis)
> - Bedrag en timing
>
> 📤 **Uitkomst**:
> - Onderwerp gekwalificeerd in IFRS-categorieën: vaste activa / financieel / lease / opbrengst / voorraad / personeel / consolidatie / etc.

**Waarom**: zonder een correcte kwalificatie van de transactie is geen enkele standaard juist toepasbaar. De typering "huur" kan onder IFRS bv. als lease (IFRS 16), als dienst (IFRS 15) of als financieel instrument (IFRS 9) doorgaan, met radicaal andere gevolgen.

Vraagstelling per categorie:

| Categorie | Vraag |
|---|---|
| Materieel actief | Tastbaar, > 1 jaar gebruik, eigen gebruik? → IAS 16 |
| Immaterieel | Identificeerbaar, geen fysieke vorm? → IAS 38 / IFRS 3 (goodwill) |
| Lease | Recht om gebruik van een actief te controleren over een periode tegen vergoeding? → IFRS 16 |
| Opbrengst | Contract met klant tegen vergoeding? → IFRS 15 |
| Voorraad | Aangehouden voor verkoop, productie of grondstof? → IAS 2 |
| Financieel actief | Recht op cash of een ander financieel actief? → IFRS 9 |
| Voorziening | Bestaande verplichting met onzeker bedrag of timing? → IAS 37 |
| Personeel | Beloning of pensioen voor personeel? → IAS 19 |

### 2. 🔀 Toepasselijke IFRS-standaard identificeren

> 📥 **Nodig**:
> - Categorie van de transactie (stap 1)
>
> 📤 **Uitkomst**:
> - Eén of meerdere toepasselijke standaarden geïdentificeerd, in volgorde van specificiteit

**Waarom**: een transactie kan onder meerdere standaarden vallen — het kiezen van de **meest specifieke** standaard is een principle van IFRS-toepassing. Een verkeerde keuze leidt tot een verkeerd boekingsmodel.

**Hiërarchie van toepasselijkheid**:
1. **Meest specifieke standaard** wint (bv. IAS 17/IFRS 16 voor leases, niet IAS 16 voor het onderliggende actief op de balans van de lessor)
2. Bij overlap: **scope-bepaling** in elke standaard (de scope-paragraaf van een IFRS bepaalt expliciet wat erbuiten valt)
3. Geen specifieke standaard: gebruik **IAS 8 §10-12** — analoge regels uit andere IFRS, dan IFRS Conceptual Framework, dan andere normgevers (US GAAP) als secundaire bron

> [!info]- Concreet: vastgoed
>
> Een onderneming bezit een gebouw dat ze gedeeltelijk zelf gebruikt en gedeeltelijk verhuurt. Welke standaard?
>
> - Eigen gebruik → **IAS 16** (Materiële vaste activa)
> - Verhuurd voor huurinkomsten of waardestijging → **IAS 40** (Vastgoedbeleggingen)
> - Beide gebruikt: scheiden indien afzonderlijk verhandelbaar (IAS 40 §10), anders volledig onder IAS 16 als het verhuurde deel niet apart verhandelbaar is
>
> 🤖 *AI-aanvulling*

### 3. 🔍 Opnamevoorwaarden toetsen

> 📥 **Nodig**:
> - Toepasselijke standaard (stap 2)
> - Feiten van de transactie
>
> 📤 **Uitkomst**:
> - Beslissing: wel/niet opnemen
> - Indien wel: tijdstip van opname

**Waarom**: niet alles wat een entiteit "heeft" of "zal hebben" is een actief of verplichting onder IFRS. De opnamecriteria filteren wat op de balans terechtkomt versus wat in de toelichting blijft of buiten-balans.

Standaardcriterium per categorie:

- **Actief** (algemeen): toekomstige economische voordelen waarschijnlijk + betrouwbare meting van de kostprijs
- **Verplichting**: bestaande verplichting (juridisch of constructief) + waarschijnlijke uitstroom + betrouwbare meting
- **Opbrengst** (IFRS 15): contract bestaat + prestatieverplichting vervuld of gaande
- **Voorziening** (IAS 37): bestaande verplichting + waarschijnlijke uitstroom + betrouwbare schatting

> [!info]- Concreet: garantieverplichting
>
> Een fabrikant verkoopt apparaten met 2 jaar standaardgarantie. Verleden leert dat 3% van de verkochte apparaten een gemiddelde herstelkost van €200 oplevert.
>
> Onder IAS 37: er is een **constructieve verplichting** ontstaan bij verkoop, met **waarschijnlijke uitstroom** en **betrouwbare schatting** (3% × €200 = €6 per apparaat). Een **voorziening** wordt opgenomen op moment van verkoop, niet bij effectieve herstelling.
>
> Onder Belgisch GAAP: idem — voorziening wordt gevormd via [[voorzieningen]] op het passief van de balans.
>
> 🤖 *AI-aanvulling*

### 4. 🔢 Initiële waardering bepalen

> 📥 **Nodig**:
> - Toepasselijke standaard (stap 2)
> - Concrete cijfers van de transactie
>
> 📤 **Uitkomst**:
> - Initieel geboekt bedrag (kostprijs, reële waarde, of contante waarde)

**Waarom**: de initiële waardering is het anker voor alle latere boekingen. Een fout hier propageert door alle boekjaren tot afvoer van het actief.

Veelvoorkomende waarderingsbasis per categorie:

| Categorie | Initiële waardering |
|---|---|
| Materieel actief (IAS 16) | Kostprijs incl. directe kosten en ontmanteling |
| Immaterieel (IAS 38) | Kostprijs (niet activeerbaar voor goodwill intern) |
| Lease lessee (IFRS 16) | Contante waarde toekomstige leasebetalingen + initiële kosten |
| Opbrengst (IFRS 15) | Transactieprijs verdeeld over prestatieverplichtingen |
| Voorraad (IAS 2) | Kostprijs (aankoopprijs + conversiekosten + andere kosten om in huidige staat te brengen) |
| Financieel actief (IFRS 9) | Reële waarde + transactiekosten (behalve FVTPL) |
| Voorziening (IAS 37) | Beste schatting van uitgaven nodig om verplichting af te wikkelen |

### 5. 🔀 Latere waardering bepalen

> 📥 **Nodig**:
> - Initiële waardering (stap 4)
> - Beleidskeuze van de entiteit (waar opties bestaan)
>
> 📤 **Uitkomst**:
> - Latere waardering (kostprijsmodel of herwaarderingsmodel of reële waarde)
> - Periodieke verwerking (afschrijving, herwaardering, impairment)

**Waarom**: voor veel posten biedt IFRS twee modellen: **kostprijsmodel** en **herwaarderingsmodel** (of reële-waardemodel). De keuze wordt op niveau van **categorie** gemaakt en moet consistent worden toegepast — zie de individuele standaarden ([[vaste-activa-ifrs|IAS 16/38]], IAS 40, IFRS 9).

**Periodieke verwerking** omvat:
- Afschrijving (IAS 16, IAS 38, IFRS 16)
- Herwaardering naar reële waarde (IAS 16 als gekozen, IAS 40, IFRS 9 FVTPL/FVTOCI)
- Impairment-test (IAS 36, IFRS 9 verwachte kredietverliezen)
- Aanpassingen voor schattingswijzigingen (IAS 8)

### 6. 🔍 Belgisch GAAP-vergelijking opstellen (indien dual reporting)

> 📥 **Nodig**:
> - IFRS-verwerking (stappen 4-5)
> - De Belgische statutaire boeking voor dezelfde transactie
>
> 📤 **Uitkomst**:
> - Verschillen genoteerd: timing, waardering, classificatie, OCI vs. P&L
> - Consolidatie-aanpassingen geformuleerd indien IFRS-rapportering op groep- of segmentniveau

**Waarom**: bij Belgische entiteiten met IFRS-rapportering op groepniveau bestaat altijd een **dubbele set boekingen** — Belgisch GAAP statutair en IFRS in consolidatie. De analist moet de verschillen identificeren en als consolidatieboekingen overzetten.

| Frequente verschilpunten | Belgisch GAAP | IFRS |
|---|---|---|
| Operationele lease | Off-balance | On-balance (IFRS 16) — zie [[leasing-ifrs]] |
| Goodwill | Afgeschreven 5-10 jaar | Niet afgeschreven, jaarlijks impairment |
| Ontwikkelingskosten | Activering optioneel | Verplicht bij voldoen voorwaarden |
| Voorraad LIFO | Toegelaten | Verboden — zie [[voorraden-ifrs]] |
| Herwaardering MVA | Beperkt tot duurzame meerwaarde | Vrijer model voor categorie |
| Toelichting | Beperkt | Uitgebreid |

### 7. 💬 Beslissing en toelichting opstellen

> 📥 **Nodig**:
> - Volledige IFRS-verwerking (stappen 1-6)
>
> 📤 **Uitkomst**:
> - Schriftelijke memo: standaard toegepast, opname, waardering, presentatie, toelichting
> - Toelichtingstekst voor de jaarrekening

**Waarom**: IFRS verlangt veel meer toelichting dan Belgisch GAAP — een correcte boeking volstaat niet. De redenering moet schriftelijk worden vastgelegd zodat de auditor en latere accountants kunnen reconstrueren waarom een specifieke verwerking gekozen werd.

De memo bevat:
- Aard van de transactie en gekozen kwalificatie (stap 1)
- Toepasselijke standaard met paragraafverwijzing (stap 2)
- Opname-redenering (stap 3)
- Initiële en latere waardering (stappen 4-5)
- Vergelijking met Belgisch GAAP indien relevant (stap 6)
- Bedragen voor de jaarrekening, classificatie, en concept van de toelichting

## Voorbeelden

> [!example]- Vastgoedbelegger koopt kantoorgebouw voor verhuur
>
> **Situatie**: een investeringsmaatschappij koopt een kantoorgebouw voor €20M om volledig te verhuren aan een derde. Initiële waardering en latere behandeling onder IFRS?
>
> **Conclusie**:
> - **Toepasselijke standaard**: IAS 40 (Vastgoedbeleggingen) — het gebouw wordt gehouden voor huurinkomsten en/of waardestijging
> - **Initiële waardering**: kostprijs = €20M + transactiekosten (advocaat, registratie)
> - **Latere waardering** — keuze tussen:
>   - **Kostprijsmodel** (IAS 16-equivalent): afschrijven over economische gebruiksduur
>   - **Reële-waardemodel**: herwaarderen naar reële waarde, **wijzigingen via P&L** (niet OCI)
>
> Veel beleggingsmaatschappijen kiezen reële-waardemodel om de waardestijging in P&L te tonen.
>
> **Grondslag**: IAS 40 §30, §35
>
> **Redenering**: het gebouw is geen eigen-gebruik-actief (IAS 16), maar wordt gehouden voor inkomstgenerering. Onder Belgisch GAAP zou het gebouw onder rubriek III (gebouwen) staan en aan aanschaffingswaarde min afschrijvingen worden gewaardeerd. IFRS-keuze voor reële waarde brengt volatiliteit in de P&L maar reflecteert de economische realiteit beter — typisch voor REIT's en vastgoedfondsen.
>
> 🤖 *AI-aanvulling*

> [!example]- Belgische dochter van IFRS-groep huurt kantoor
>
> **Situatie**: een Belgische dochter van een IFRS-genoteerde moedergroep tekent een operationele leaseovereenkomst voor 7 jaar voor haar nieuwe kantoor (€150.000 per jaar). Hoe wordt dit verwerkt in (a) de Belgische statutaire jaarrekening en (b) de IFRS-consolidatie?
>
> **Conclusie**:
> - **Belgisch statutair**: operationele lease → off-balance, jaarlijkse huurkost €150.000 in P&L (geen actief, geen schuld)
> - **IFRS-consolidatie**: IFRS 16 → right-of-use asset + leaseschuld voor contante waarde van toekomstige betalingen (~€870.000 bij 5%)
>
> **Grondslag**:
> - Belgisch GAAP: [[bronnen/wetteksten/XV-KB-wvv|KB WVV art. 3:40]] — operationele leasing blijft off-balance
> - IFRS: [[leasing-ifrs|IFRS 16]] — single recognition model voor lessee
>
> **Redenering**: de Belgische statutaire jaarrekening blijft Belgisch GAAP — geen IFRS 16. In de **consolidatieboekingen** wordt een aanpassing toegevoegd: het right-of-use-actief en de leaseschuld worden geboekt, en de huurkost in de Belgische P&L wordt geherclassificeerd als afschrijving + interest. Bij elke afsluiting moeten deze consolidatieboekingen geactualiseerd worden (aflossing leaseschuld, afschrijving right-of-use). Een typische consolidatieboeking — werkpapieren onderhouden door het consolidatieteam.
>
> 🤖 *AI-aanvulling*

## Motiveren op het examen

**Een volledig antwoord bevat:**
1. **Kwalificatie** van de transactie in IFRS-termen
2. **Toepasselijke standaard** met expliciete naamgeving (IAS 16, IFRS 15, etc.)
3. **Opname**, **initiële waardering**, en **latere waardering** met cijfers waar mogelijk
4. **Vergelijking met Belgisch GAAP** — leg uit waar het verschil zit en waarom
5. **Concrete impact** op balansposten en resultatenrekening

**Voorbeeldvragen**

> [!question]- Operationele lease — hoe behandelen?
>
> Een onderneming gaat een 5-jarige operationele leasing aan voor een vrachtwagen, €30.000 per jaar. Hoe verwerk je dit onder IAS 17 (vóór 2019) en onder IFRS 16 (vanaf 2019)?
>
> > [!success]- Antwoord
> >
> > **Twee verschillende behandelingen.**
> >
> > Stap 1 — kwalificatie: leaseovereenkomst, recht om gebruik te controleren over 5 jaar.
> >
> > Stap 2 — toepasselijke standaard: IAS 17 vóór 2019, IFRS 16 vanaf 2019.
> >
> > **IAS 17 (operationeel)**: niet financieel → off-balance. Periodieke huur €30.000 lineair in P&L. Geen actief, geen schuld op de balans.
> >
> > **IFRS 16**: classificatie wordt overgeslagen voor lessee. Recognition op transitiedatum:
> > - Right-of-use-actief = contante waarde 5 × €30.000 (bv. €130.000 bij 5%)
> > - Leaseschuld = €130.000
> > - Periodiek: afschrijving (€26.000 lineair) + interest (afnemend)
> >
> > Dit wijzigt EBITDA, schuldgraad en solvabiliteitsratio's bij eerste toepassing materieel.
> >
> > *Zie: [[leasing-ifrs#-boekhouding-door-lessee-en-lessor|Boekhouding lessee onder IFRS]]*
>
> 📝 *Geïnspireerd door voorbeeldexamen 2024 (vraag 7D) — uitwerking 🤖*
