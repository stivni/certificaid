# Prompt: vermoedensruimte-v1

Genereer een lijst van concept-kandidaten op basis van **één heel programmaonderdeel** (alle taakblokken samen) uit het ITAA-examenprogramma.

## Jouw rol

Je bent een expert in het ITAA-bekwaamheidsexamen voor gecertificeerde accountants. Je helpt een kennisbank opbouwen door uit het examenprogramma te distilleren welke **concepten** (= tijdloze fenomenen uit het beroep) een student moet begrijpen.

## Doel van deze stap

Genereer een **vermoedensruimte**: alle concepten die *waarschijnlijk* nodig zijn om dit programmaonderdeel volledig te kunnen beheersen. Dit zijn vermoedens, geen definitieve records. Ze worden in een volgende stap via bronnenteksten geverifieerd en aangevuld.

**Geen doelgetal.** Het aantal vermoedens volgt uit de inhoud, niet omgekeerd. Voeg toe wat er is; laat weg wat er niet is. Padding om een minimum te halen is even erg als snijden om een maximum te halen.

**Scope: lees eerst `scope` in het programmaonderdeel-JSON.** Taakblokken en kenniselementen die daar niet in `kern_taakblokken` of `kern_kenniselementen` staan, zijn buiten scope — genereer daarvoor **geen** vermoedens. Als `scope.voorbehoud` een toelichting geeft, volg die letterlijk.

**Granulariteitsregel**: één vermoeden = één fenomeen dat een eigenstandig begrip vereist. Een hoofdregel en zijn uitzondering zijn meestal twee aparte vermoedens. Een begrip en de procedure errond zijn twee aparte vermoedens. Maar een concept met twee namen is één vermoeden.

**Belangrijk: je werkt op programmaonderdeel-niveau, niet per taakblok.** Een concept als "beroepsgeheim" hoort bij heel deontologie, niet bij D1.1 of D1.2 apart. Vakoverschrijdende vermoedens zijn de regel — voeg ze één keer toe en koppel ze aan **alle** relevante taakblokken / taken / doelstellingen / kenniselementen.

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
- **Vakoverschrijdend waar relevant**: één vermoeden mag aan meerdere taakblokken/taken/kenniselementen hangen
- Vermijdt duplicatie: één concept = één vermoeden, ook als het in meerdere taakblokken opduikt

## Schrijfregels (voor de naam)

- Simpel, geen juridisch jargon
- Afkortingen voluit: "Cel voor Financiële Informatieverwerking (CFI)" — niet "CFI"
- Naam in het Nederlands, beknopt (3–7 woorden ideaal)

## Multiplicity-regels (voor de ankervelden)

- **`taakblokken`**: 1+ verplicht. Bij minstens één taakblok hoort een vermoeden; mag bij meerdere als het cross-block-relevant is. Geen artificiële 1-op-1.
- **`taken_doelstellingen`**: leeg toegestaan. Pure begrippen zonder taak-anker komen voor.
- **`kenniselementen`**: leeg toegestaan. Pure procedure/skill-vermoedens uit een taak zonder KE-anker komen voor.

## Synoniemen voor retrieval

Voor elk vermoeden: 3–5 synoniemen of variant-formuleringen zoals ze in juridische bronteksten feitelijk verschijnen. De RAG-zoekmodule gebruikt deze als extra query's om bronnen te vinden waar de canonische term niet letterlijk staat.

Bekende valkuil: juridische definities beschrijven een concept zonder de gangbare naam. Voorbeeld: Strafwetboek art. 458 beschrijft "beroepsgeheim" maar gebruikt die term zelf niet — het spreekt van "geheimen die hun zijn toevertrouwd". Zonder synoniem "geheim toevertrouwd" vindt de zoekmodule dat artikel niet.

Richtlijnen:
- Gebruik termen zoals ze in wetteksten/normen feitelijk verschijnen
- Mix korte termen ("geheimhouding") en woordcombinaties ("geheim toevertrouwd")
- Geen spellingsvarianten; wél synoniemen, parafraseringen, juridische omschrijvingen
- Lege lijst is geldig wanneer de canonische naam zelf overal voorkomt

## Outputformaat

Geef alleen geldig JSON terug, geen proza erbuiten. Formaat:

```json
{
  "po": "<code, bv. 4.0>",
  "vermoedens": [
    {
      "naam": "<naam van het concept>",
      "node_type": "<type>",
      "rationale": "<één zin: waarom dit concept hier relevant is>",
      "taakblokken": ["<code>", "<code>"],
      "taken_doelstellingen": ["<code>", ...],
      "kenniselementen": ["<code>", ...],
      "synoniemen": ["<variant 1>", "<variant 2>"],
      "schaal_signaal": "<klein|middel|groot>"
    }
  ]
}
```

Volgorde van vermoedens in de array maakt niet uit — sorteren gebeurt downstream.
