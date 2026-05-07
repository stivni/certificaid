# Concept-schrijfregels

Content-conventie voor concept-records (`data/concept_records/*.json`). Wordt ingeladen in de extractor-prompt (ADR-008) en geldt ook voor menselijke review/aanvulling. Geen ADR — dit is content-stijl, geen architectuurbeslissing.

> **Doelpubliek**: stagiair gecertificeerd accountant, met boekhoudkundige en fiscale basiskennis. Géén jurist.

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
