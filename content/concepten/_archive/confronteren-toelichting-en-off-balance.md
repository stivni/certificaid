---
title: Confronteren van de financiële analyse met de toelichting en off-balance posten
tags:
- concept
- competentie
- po-1-3
linked_anchors:
- 1.3.taak.1
- 1.3.II.B.4
- 1.3.II.D
- 1.3.I.A
programmaonderdelen:
- '1.3'
confidence: inferred
node_type: competentie
status: voorgesteld
schema_version: '1.6'
gegenereerd_uit: data/concepten/records/confronteren-toelichting-en-off-balance.json
gegenereerd_op: '2026-05-21'
---
# Confronteren van de financiële analyse met de toelichting en off-balance posten 🔗

Competentie om financiële analyse op cijfers te confronteren met wat ernaast staat: de toelichting (waarderingsregels, off-balance-engagementen, lopende geschillen) en hors-balansposten. Zonder die confrontatie blijft de analyse oppervlakkig — een sterke solvabiliteit kan verbleken zodra borgstellingen en operationele leases meegenomen worden.



## Stappen

### 1. Doorlezen van de volledige toelichting

Lees de toelichting bij de jaarrekening integraal vóór je conclusies trekt.

**Waarom?** De echte risico's staan vaak in de toelichting, niet in de samengevatte balansposten.

**📥 Input**:
- Jaarrekening — toelichtingen → **Volledige toelichting (XBRL of PDF)** _(document)_

**📤 Output**:
- Notitielijst toelichting → **Per onderwerp een korte aantekening** _(document)_

**🛠️ Hoe**:

1. Open de toelichting bij de jaarrekening van Rotex Roeselare NV.
2. Lees in deze volgorde:
   - Waarderingsregels (wijzigingen tegenover N-1).
   - Staat van vaste activa (afschrijvingen, herwaarderingen).
   - Staat van vorderingen en schulden (vervaltermijnen, aard).
   - Niet in de balans opgenomen rechten en verplichtingen ([[niet-in-balans-opgenomen-rechten-verplichtingen]] §wat-hoort-eronder).
   - Persoonlijke en zakelijke zekerheden.
   - Verbonden partijen.
   - Gebeurtenissen na balansdatum.
3. Markeer elk element dat zou kunnen wijzigen welke conclusie je trekt uit de cijfers.


**Grondslag**: [[getrouw-beeld-jaarrekening]] §toelichting-veiligheidsklep

### 2. Inventariseren van niet in de balans opgenomen rechten en verplichtingen

Maak een lijst van alle off-balance items met bedrag en aard.

**Waarom?** Off-balance-verplichtingen kunnen de echte schuldgraad of risicopositie wezenlijk veranderen.

**📥 Input**:
- Sectie "Niet in de balans opgenomen rechten en verplichtingen" → **Borgstellingen, zekerheden, leasing, geschillen, contractuele commitments** _(document)_
- Klasse 0 — spiegelboekingen → **Buitenbalansrekeningen (00 tot 07)** _(boekhoudkundig-bedrag)_

**📤 Output**:
- Off-balance-inventaris → **Per item: aard, bedrag, duurtijd, partij** _(document)_

**🛠️ Hoe**:

1. Volg de zes categorieën uit [[niet-in-balans-opgenomen-rechten-verplichtingen]] §wat-hoort-eronder en [[klasse-0-niet-in-balans]] §categorieen-00-07:
   - Persoonlijke zekerheden (borgstellingen door en voor).
   - Zakelijke zekerheden (hypotheken, pand op handelszaak).
   - Andere verbintenissen (aankoop-, verkoop-verbintenissen).
   - Geschillen (lopende procedures).
   - Pensioenverplichtingen (defined benefit, indien niet voorzien).
   - Operationele leasing en huurverplichtingen — totaal toekomstige betalingen.
2. Per item: noteer aard, bedrag, eventuele duurtijd, tegenpartij.
3. Pas materialiteits-test toe ([[materieel-belang-jaarrekening]] §relatief): bedrag > 5% van balanstotaal = materieel.


> [!example]- Voorbeeld: Rotex Roeselare NV — off-balance items uit toelichting
> Rotex Roeselare NV — off-balance items uit toelichting.
>
> 1. **Off-balance-inventaris** 📊
>
>    | Item                                  | Bedrag       | Aard            | Materieel? (>5% balanstotaal € 25,8M) |
>    |---------------------------------------|-------------:|-----------------|:--------------------------------------|
>    | Hypotheek op bedrijfsgebouw           | € 8.000.000  | Zakelijke zekerheid | Ja (31%)                          |
>    | Borgstelling tgv. dochter             | € 1.500.000  | Persoonlijke zek. | Marginaal (5,8%)                    |
>    | Operationele leasing wagenpark (5 jaar)| € 600.000   | Huurverbintenis | Niet materieel                        |
>    | Lopend geschil met aannemer           | € 200.000    | Geschil         | Niet materieel                        |
>    
>

**Grondslag**: [[niet-in-balans-opgenomen-rechten-verplichtingen]] §subsidiariteit, KB W.Venn. art. 91-94

### 3. Confronteren met de berekende ratio's

Toets of off-balance posten de eerder berekende ratio's wezenlijk wijzigen.

**Waarom?** Een gezonde solvabiliteit kan misleidend zijn als er voor € 8M aan zekerheden gegeven is op bestaande schulden.

**📥 Input**:
- Off-balance-inventaris uit stap 2 → **Materiële items** _(boekhoudkundig-bedrag)_
- Berekende ratio's uit competentie [[berekenen-interpreteren-solvabiliteitsratios]] → **Solvabiliteit, debt-equity** _(percentage)_

**📤 Output**:
- Aangepaste solvabiliteits-beoordeling → **Ratio met en zonder off-balance impact** _(percentage)_

**🛠️ Hoe**:

1. Voor leasing-verplichtingen: bereken de "schaduw-solvabiliteit" door de te kapitaliseren verplichtingen virtueel als schuld op te tellen.
2. Voor borgstellingen ten voordele van derden: voeg dit niet toe als schuld, maar vermeld als contingent risico.
3. Voor zakelijke zekerheden op eigen schulden: deze verhogen niet de schuldgraad maar verlagen wel de financierings-flexibiliteit. Vermelden.
4. Voor materiële geschillen: schat best-case/worst-case impact op EV.
5. Documenteer twee scenario's: "boekhoudkundig" (zoals balans toont) en "economisch" (na integratie van off-balance).


> [!example]- Voorbeeld: Rotex Roeselare NV — leasing kapitaliseren en doorrekenen op solvabiliteit
> Rotex Roeselare NV — leasing kapitaliseren en doorrekenen op solvabiliteit.
>
> 1. **Twee scenario's** 🧮
>
>    | Scenario                            | EV          | Balanstotaal  | Solvabiliteit |
>    |-------------------------------------|------------:|--------------:|--------------:|
>    | Boekhoudkundig (balans)             | € 12.150.000 | € 25.800.000 | 47,1%         |
>    | Economisch (na kapitalisering leasing € 600k) | € 12.150.000 | € 26.400.000 | 46,0%        |
>    
>
> 2. **Interpretatie** 💬
>
>    Impact leasing-kapitalisering: 1,1 ppt lager. Niet materieel — Rotex
>    blijft sterk solvabel. Zou wel materieel zijn voor een vennootschap
>    met meer leasing (bv. Transport Tongeren BV).
>    
>

**Grondslag**: [[niet-in-balans-opgenomen-rechten-verplichtingen]] §wat-hoort-eronder

> [!warning]- Behandel borgstellingen ten voordele van derden als contingent risico, niet als schuld.
>
> _Vaak fout gedaan_: Een borgstelling van € 1.500.000 mechanisch optellen bij de schulden — overschat de schuldgraad.
>
> _Grondslag_: [[niet-in-balans-opgenomen-rechten-verplichtingen]] §subsidiariteit

### 4. Opnemen in het analyserapport

Schrijf één paragraaf over off-balance in je rapport.

**Waarom?** De gebruiker moet weten dat er materiële off-balance items zijn, ook al raken die de cijfers zelf niet.

**📥 Input**:
- Off-balance-inventaris + aangepaste solvabiliteit → **Materiële items + scenario-vergelijking** _(document)_

**📤 Output**:
- Off-balance-paragraaf in analyserapport → **Tekst met inventaris + impact-inschatting** _(document)_

**🛠️ Hoe**:

1. Schrijf een paragraaf met titel "Niet in de balans opgenomen verplichtingen en risico's".
2. Vermeld de materiële items met bedrag.
3. Geef de scenario-vergelijking (boekhoudkundig vs economisch).
4. Sluit af met concluderende zin: bevestiging of relativering van de ratio-conclusies.


**Grondslag**: [[getrouw-beeld-jaarrekening]] §toelichting-veiligheidsklep, vakdoctrine rapportering


## Voorbeelden




## Bronnen

[^1]: `anchor-1.3.taak.3`
