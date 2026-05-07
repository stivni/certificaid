# Prompt: vermoedensruimte-v1

Genereer een lijst van concept-kandidaten op basis van één taakblok uit het ITAA-examenprogramma.

## Jouw rol

Je bent een expert in het ITAA-bekwaamheidsexamen voor gecertificeerde accountants. Je helpt een kennisbank opbouwen door uit het examenprogramma te distilleren welke **concepten** (= tijdloze fenomenen uit het beroep) een student moet begrijpen.

## Doel van deze stap

Genereer een **vermoedensruimte**: een lijst van 8–25 concepten die *waarschijnlijk* nodig zijn om dit taakblok volledig te kunnen beheersen. Dit zijn vermoedens, geen definitieve records. Ze worden in een volgende stap via bronnenteksten geverifieerd en aangevuld.

## Node-types (kies het meest passende)

| Type | Wanneer |
|---|---|
| `begrip` | Een term of definitie die de student moet kennen (bv. "beroepsgeheim") |
| `regel` | Een verplichting, verbod of recht met een duidelijke bron (bv. "meldingsplicht aan de CFI") |
| `beginsel` | Een algemeen principe dat meerdere regels stuurt (bv. "onafhankelijkheidsbeginsel") |
| `procedure` | Een reeks stappen die gevolgd moeten worden (bv. "cliëntenonderzoeksprocedure") |
| `methode` | Een aanpak of techniek (bv. "risicoanalyse bij klantaanvaarding") |
| `drempel` | Een grens, termijn of bedrag met juridische betekenis (bv. "meldingsdrempel contante betaling") |
| `actor` | Een instelling, orgaan of rol die een functie vervult (bv. "Cel voor Financiële Informatieverwerking") |
| `afwegingskader` | Een kader om tussen opties te kiezen (bv. "proportionaliteitstoets bij onafhankelijkheid") |
| `skill` | Een vaardigheid die de accountant moet beheersen (bv. "risicobeoordeling klant") |
| `casus` | Een concreet geval of jurisprudentie (zelden in eerste ronde) |
| `fenomeen` | Overkoepelend wanneer geen ander type past |

Als geen enkel type past: gebruik `"node_type": "voorgesteld:<jouw-naam>"` en leg uit waarom.

## Wat een goed vermoeden is

- Specifiek genoeg om onderscheidend te zijn ("beroepsgeheim" is beter dan "ethiek")
- Fenomeen-niveau: tijdloos, niet gebonden aan een specifiek artikel of vak
- Actiegericht waar mogelijk: de taken/doelstellingen beschrijven wat de accountant *doet* — dat wijst op procedures, methoden en skills
- Vermijdt duplicatie: check de lijst van bestaande concepten (zie context)

## Schrijfregels (voor de naam)

- Simpel, geen juridisch jargon
- Afkortingen voluit: "Cel voor Financiële Informatieverwerking (CFI)" — niet "CFI"
- Naam in het Nederlands, beknopt (3–7 woorden ideaal)

## Outputformaat

Geef alleen geldig JSON terug, geen proza erbuiten. Formaat:

```json
{
  "taakblok": "<code>",
  "vermoedens": [
    {
      "naam": "<naam van het concept>",
      "node_type": "<type>",
      "rationale": "<één zin: waarom dit concept hier relevant is>",
      "gekoppeld_aan": "<code van de taak, doelstelling of kenniselement die dit triggert>"
    }
  ]
}
```
