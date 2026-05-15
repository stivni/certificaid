# Concept-schrijfregels

Content-conventie voor concept-records (`data/concepten/records/*.json`). Wordt ingeladen in de extractor-prompt (ADR-008) en geldt ook voor menselijke review/aanvulling. Geen ADR — dit is content-stijl + conceptkeuze, geen architectuurbeslissing.

> **Doelpubliek**: stagiair gecertificeerd accountant, met boekhoudkundige en fiscale basiskennis. Géén jurist.

## Wat IS een concept?

Een concept is een **tijdloos fenomeen** uit het beroep van de gecertificeerd accountant — iets dat een student moet *begrijpen* om als professional te kunnen handelen. Niet een wetsartikel, niet een vakindeling, niet een examenvraag.

Drie test-vragen om concept-status te valideren:

1. **Tijdloosheid**: zou dit concept nog gelden als de wet morgen veranderd wordt? Een concept beschrijft een **fenomeen** (bv. "Beroepsgeheim" als principe); de wettelijke uitvoering kan wijzigen, het concept blijft.
2. **Onderscheidbaarheid**: kan een student dit concept onderscheiden van zijn buren? Als concept A en concept B in elke voorbeeldvraag samen optreden en niet apart bevraagd kunnen worden → het is wellicht één concept.
3. **Praktijkbruikbaarheid**: kan een student het concept toepassen op een casus? Als het te abstract is om mee te redeneren ("Algemeen ethisch handelen") → te grof. Als het te specifiek is om buiten één voorbeeld toepasbaar te zijn ("Meldingsplicht bij vastgoedtransactie >€10.000") → te fijn.

### Voorbeelden van GOEDE concepten

| Naam | Type | Waarom goed |
|---|---|---|
| Beroepsgeheim van de gecertificeerd accountant | beginsel | Tijdloos, onderscheidbaar van discretieplicht, breed toepasbaar |
| Meldingsplicht aan de Cel voor Financiële Informatieverwerking (CFI) | regel | Concrete verplichting, bron in AWW, niet identiek aan beroepsgeheim |
| Cliëntenonderzoeksprocedure (Know Your Customer) | procedure | Stappen-gestructureerd, toepasbaar op elke nieuwe cliënt |
| Uiteindelijk begunstigde (UBO) | begrip | Tijdloos juridisch begrip, gekoppeld aan concrete identificatieregels |
| Risicogebaseerde aanpak (antiwitwas) | afwegingskader | Helpt bij keuzes tussen vereenvoudigd vs. verscherpt onderzoek |

### Voorbeelden van GEEN concepten

| Voorbeeld | Waarom niet | Wat dan wel? |
|---|---|---|
| "Artikel 47 AWW" | Een wetsartikel ≠ een concept | Concept = "Meldingsplicht aan CFI", waarvan Art. 47 AWW de bron is |
| "Hoofdstuk 3 Deontologie" | Een examenvak/programma-onderdeel ≠ een concept | Het programmaonderdeel is een container; concepten leven daarbinnen |
| "Wanneer is melding aan CFI verplicht voor een bouwopdracht?" | Een examenvraag ≠ een concept | Dit is een **toetsings-instantie** (examenfocus, ADR-009) van het concept "Meldingsplicht aan CFI" |
| "Algemeen handelen volgens de wet" | Te abstract — niet onderscheidbaar | Splits in concrete principes: "Beroepsgeheim", "Onafhankelijkheidsbeginsel", ... |
| "Meldingsplicht bij contante betaling boven €3.000 voor edelmetalen" | Te specifiek — niet generiek toepasbaar | Concept = "Beperking gebruik van contanten" met de drempel als veld |
| "De accountant in de digitale wereld" | Te vaag, niet substantief | Splits in specifieke skills/methoden waar nodig |

### Granulariteit — de "Goldilocks-zone"

Voor een programmaonderdeel als 4.0 Deontologie verwacht je grosso modo **15–40 concepten**. Veel meer en het is gepulveriseerd; veel minder en het is te grof.

**Schaal-signalen die je gebruikt om granulariteit te kalibreren**:
- `klein` (= "feature van een ander concept"): wordt waarschijnlijk een **veld of edge** op een groter concept ipv. een eigen record. Voorbeeld: "Specifieke analyse bij vermoeden" → veld `exceptions[]` op `Meldingsplicht aan CFI`.
- `middel` (= "kerndienstverlening"): krijgt zijn **eigen record**. Voorbeeld: "Verbod op doormelding (tipping-off)".
- `groot` (= "overkoepelend principe"): krijgt zijn eigen record met veel **edges naar onderliggende concepten**. Voorbeeld: "Beroepsgeheim van de gecertificeerd accountant" met edges naar uitzonderingen, doorbrekingsgronden, sancties.

### Smell tests bij twijfel

- **De "definitie" smell**: als je hoofd-veld begint met "X is..." en de definitie bevat geen voorbehoud, geen uitzondering, geen onderscheid van naburen → het is wellicht een **begrip-node** maar mogelijk te abstract. Check tegen de tijdloosheid-test.
- **De "stappenplan" smell**: als de hoofdtekst louter een nummering is van procedurele stappen → eerder `procedure`-type met `stappen[]`-veld dan losse concepten per stap.
- **De "alleen in deze wet" smell**: als het concept alleen bestaat omdat één specifiek artikel het beschrijft → controleer of het werkelijk een fenomeen is of een wettelijke specificiteit. Als artikel verdwijnt en concept verdwijnt → twijfelachtig.
- **De "casus" smell**: als de hoofdtekst gaat over "in het geval van..." met concrete feiten → het is een `casus`-node, geen begrip/regel.

## Taal

1. **Simpele Nederlands taal**. Korte zinnen, actieve vorm. Vermijd legalistische constructies ("doch", "alsmede", "hetwelk"). Het mag toegankelijk klinken — mits inhoudelijk correct.

2. **Boekhoudkundige terminologie mag**: "balans", "afschrijving", "btw-aangifte", "controlewerkzaamheden", "samenstellingsopdracht". De student kent deze termen al.

3. **Wetgeeftaal vermijden**, ook als de bron zo geschreven is. Paraphraseer in normaal Nederlands.
   - ❌ "De onderworpen entiteit is gehouden de waakzaamheidsverplichtingen na te leven onder voorbehoud van de bepalingen vervat in artikel 26."
   - ✅ "De accountant moet zijn cliënten controleren volgens de antiwitwaswet — behalve in de gevallen die artikel 26 opsomt."

4. **Verbatim wetstekst** mag wel — maar alleen in `source.citation`, niet in de hoofdtekst van een veld. Hoofdtekst is altijd herschreven.

## Afkortingen

5. **Eerste vermelding**: voluit, met afkorting tussen haakjes.
   - "Cel voor Financiële Informatieverwerking (CFI)"
   - "Antiwitwaswet (AWW)"
   - "Instituut van de Belastingadviseurs en Accountants (ITAA)"

6. **Vervolg in dezelfde tekst**: afkorting mag.

7. **Per veld opnieuw beginnen**. Een concept-record heeft meerdere tekstvelden (`main_rule`, `exceptions`, `voorbeeld_inline`, ...). Bij elk veld geldt regel 5 opnieuw — de student leest velden los.

## Confidence-labels

8. **Elke inhoudelijke claim** heeft een `confidence`-veld:
   - `"grounded"` — direct traceerbaar naar een bron in `source.ref`. Verplicht een bronverwijzing.
   - `"inferred"` — LLM-gegenereerde redenering of synthese. Mag, maar moet als zodanig herkenbaar zijn voor de student.

9. **Bij twijfel: leeg laten** is beter dan een verkeerd label. Lege velden zijn geldig (sparse fields zijn norm — ADR-007).

## Voorbeelden, valkuilen, cases

10. **Voorbeelden** in `voorbeeld_inline` (kort, illustratief). Pas in status `gevuld` (zie ADR-007).

11. **Valkuilen (`pitfalls`)** beschrijven typische redeneerfouten van studenten of fouten die in de praktijk regelmatig gebeuren. Niet "wat de wet zegt" maar "waar mensen struikelen".
    - ✅ "Veel stagiaires verwarren beroepsgeheim (ITAA-norm) met de discretieplicht (algemene burgerrechtelijke loyauteit). Beide gelden, maar hebben verschillende sancties."
    - ❌ "Schending van het beroepsgeheim is strafbaar volgens art. 458 SW." (= regel, geen valkuil)

12. **Casussen** zijn echte cases (jurisprudentie, voorbeeldexamenvraag, CBN-feitenset) — apart node-type `casus`, niet inline.

## Verwijzingen

13. **Verwijzingen tussen concepten** als getypeerde edges (ADR-007 §8), niet als hyperlink-prose in de hoofdtekst.
    - ❌ "Zie ook [doorbreking-beroepsgeheim] voor uitzonderingen."
    - ✅ Edge `uitzondering-op` met target-id, eventueel met `notitie` veld voor context.

14. **Verwijzingen naar bronnen** in `source.short` ("AWW art. 47 §1") en gestructureerd in `source.ref` — niet inline in prose.

## Lengte

15. **Hoofdtekstvelden ≤ 150 woorden** per veld. Langer betekent meestal: splits in subconcepten of beweeg detail naar aparte velden.

16. **`voorbeeld_inline` ≤ 80 woorden**. Eén concrete situatie, geen narratief.
