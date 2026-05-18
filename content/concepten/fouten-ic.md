---
title: Fouten in IC-context
tags:
- concept
- cluster
- po-1-7
linked_anchors:
- 1.7.VI.A
- 1.7.VI
programmaonderdelen:
- '1.7'
confidence: grounded
node_type: cluster
status: seed
schema_version: '1.6'
gegenereerd_uit: data/concepten/records/fouten-ic.json
gegenereerd_op: '2026-05-18'
---
# Fouten in IC-context ⚖️

Een 'fout' in IC- en audit-context is ISA 450 §4(a)'s niet-frauduleuze afwijking: een onopzettelijke discrepantie tussen registratie en realiteit. De interne controle moet fouten primair preventief vermijden (procedures, automatische plausibility-checks, vier-ogen-principe op kritische posten) en residueel detectief opvangen (afstemmingen, cijferanalyses, periodieke reviews). Voor de stagiair is dit het tegen-begrip van fraude — geen opzet → andere preventie + detectie + auditor-respons.

> [!summary] Korte inhoud
> Een fout is een onopzettelijke afwijking in de boekhouding, rapportering of bedrijfsvoering — door vergissing, onkunde, slordigheid of slecht ontworpen proces.

> [!info] Behoort tot: [[fraude-versus-fout]]

Een fout is een onopzettelijke afwijking in de boekhouding, rapportering of bedrijfsvoering — door vergissing, onkunde, slordigheid of slecht ontworpen proces. Onderscheidt zich van fraude door het ontbreken van opzet. ISA 450 §4(a) classificeert fouten als één van de twee oorzaken van een 'afwijking' tussen jaarrekening en stelsel. IC moet zoveel mogelijk fouten preventief vermijden (procedures, checks) en residuele fouten detecteren (afstemmingen, analyses).

_Bron: ISA 450 §4(a)_


## Bouwstenen

### Foutsoorten volgens ISA 450 §A1 ⚖️

ISA 450 onderscheidt vijf bronnen van fouten: (a) onnauwkeurigheid bij accumuleren of verwerken van gegevens, (b) weglating van een bedrag of toelichting, (c) incorrecte schatting doordat feiten over het hoofd zijn gezien of verkeerd geïnterpreteerd, (d) oordeelsvorming van het management bij schattingen of grondslagen die de auditor als onredelijk of niet passend beschouwt, en (e) onjuiste classificatie of presentatie.

**Waarom?** Deze indeling is bruikbaar bij de risico-inschatting: elke bron vraagt een ander type controlewerkzaamheid (cijferanalyse voor verwerkingsfouten, substantive tests voor weglating, schatting-review voor oordeels-fouten).


**In de praktijk**: In een audit-werkpapier wordt elke geïdentificeerde afwijking ingedeeld onder één van deze categorieën — dat helpt om patronen te herkennen (bv. systematische schatting-fouten wijzen op een diepere methode-tekortkoming).


_Grondslag: ISA 450 §A1_

### Accumulatie en duidelijk-triviaal-drempel (ISA 450 §A2-§A6) ⚖️

Alle geïdentificeerde fouten worden door de auditor geaccumuleerd, behalve fouten die 'duidelijk triviaal' zijn — een orde-van-grootte kleiner dan materialiteit én ongeacht aard of omstandigheden onbeduidend. De auditor mag een drempelbedrag vaststellen waaronder fouten niet hoeven te worden geaccumuleerd. Bij twijfel: niet als duidelijk triviaal beschouwen.

**Waarom?** Accumulatie maakt zichtbaar of gezamenlijke fouten de materialiteit naderen — het is geen bureaucratische oefening maar een mechanisme om verborgen risico's op materiële afwijking te detecteren (ISA 450 §A8).


**In de praktijk**: De auditor onderscheidt drie types geaccumuleerde fouten: feitelijke (geen twijfel), inschatting (oordeelsvormingen), en geprojecteerde (extrapolatie uit steekproef). Elk type wordt apart geëvalueerd voordat het totaal tegen materialiteit wordt gehouden.


_Grondslag: ISA 450 §5 + §A2-§A6_

### IC-respons — preventief versus detectief 🤖

Een goede IC voorkomt fouten primair door procedure-design (automatische plausibility checks, vereiste velden in ERP, drempelwaardes met manuele review, vier-ogen-principe op kritische posten). Wat preventief niet wordt afgevangen, moet detectief worden opgepikt: maandelijkse afstemmingen (bank ↔ grootboek), cijferanalyses (trends, ratio's), spotcheck-samples door een supervisor.

**Waarom?** Preventief is goedkoper dan detectief (geen correctie-werk nadien) maar nooit volledig: residuele fouten — door uitzonderingen, nieuwe transactietypes, software-bugs — moeten via detectieve controles worden gevangen. De combinatie van beide is wat ISA 315 'beheersactiviteiten' noemt.


**In de praktijk**: Examen-patroon: kies bij een gegeven foutsoort de juiste IC-laag. Invoerfout van bedrag → preventief (range-validatie in ERP). Verkeerde rekeningtoewijzing → detectief (maandelijkse review per kostencentrum). Foutieve schatting (afschrijvingstermijn) → detectief (jaarlijkse review door extern controle-orgaan).


_Grondslag: ISA 315 (herzien-2019) bijlage 3 + COSO 2013 component 3 (beheersactiviteiten)_


## In de praktijk

<h3 id="centrale-onderscheidsregel">Centrale onderscheidsregel</h3>

> [!tip]- Centrale onderscheidsregel
> Fout = onopzettelijk; fraude = opzettelijk + misleiding. Hetzelfde geldbedrag, zelfde balanspost — alleen het bewijs van opzet bepaalt welke regelset van toepassing is (ISA 240 voor fraude-respons, ISA 450 voor fout-accumulatie). Bij twijfel: documenteren en doorvragen, niet voorbarig kwalificeren. ⚖️


> [!info]- Niet verwarren met [[correctie-jaarrekening-ifrs]]
> Een 'fout' in ISA 450-zin (en in de IC-context van 1.7.VI.A) is per definitie ONOPZETTELIJK — fraude is een aparte categorie. Een 'fout' in IAS 8 §41-zin daarentegen omvat zowel onopzettelijke ALS opzettelijke afwijkingen in de jaarrekening (IAS 8 §41: 'fouten ... die opzettelijk zijn gemaakt teneinde de financiële positie ... te presenteren'). Dezelfde term, twee scopes — gevolg: een opzettelijke handeling die onder ISA 240 'fraude' heet, kan onder IAS 8 een 'materiële fout' heten die retrospectief moet worden gecorrigeerd in vergelijkende informatie.
>
> _Trigger_: Examen-zin met 'fout in een vorige periode' + 'IAS 8' → correctie-pad onder IAS 8. Zin met 'fout' + 'audit-respons' + 'ISA 450' → onopzettelijk, accumulatie en materialiteits-evaluatie.


## Valkuilen

> [!warning]- Een opzettelijke wijziging in de jaarrekening kan onder IAS 8 als 'fout' worden bestempeld (IAS 8 §41 noemt expliciet opzettelijke fouten) —…
> ⚠️ Een opzettelijke wijziging in de jaarrekening kan onder IAS 8 als 'fout' worden bestempeld (IAS 8 §41 noemt expliciet opzettelijke fouten) — terwijl dezelfde handeling onder ISA 240 'fraude' heet. De terminologie verschilt per stelsel; volg de scope van het standaard-document waarbinnen je redeneert. ⚖️


> [!warning]- Een geaccumuleerde lijst kleine fouten kan, gezamenlijk, de materialiteit overschrijden — zelfs als elk individueel duidelijk triviaal lijkt
> ⚠️ Een geaccumuleerde lijst kleine fouten kan, gezamenlijk, de materialiteit overschrijden — zelfs als elk individueel duidelijk triviaal lijkt. ISA 450 §A8 waarschuwt: gezamenlijke evaluatie is verplicht. Niet elke kleine fout 'wegstrepen' zonder eindcheck tegen totale materialiteit. ⚖️



## Zie ook

- **Vereist kennis van**: [[afwijking-van-materieel-belang]]
- **Vereist kennis van**: [[materieel-belang-audit]]

## Voorbeelden

Bij Yperse Werkplaats BV boekt een nieuwe boekhouder een factuur van € 12.000 onder verkeerd kostencentrum (Spinnerij i.p.v. Weverij). Geen opzet — gewoon vergissing. IC-respons: maandelijkse review per kostencentrum door afdelingschef pikt afwijking op; correctie + verduidelijking in instructie.

## Bronnen

[^1]: `ISA-450__sec_definities`
[^2]: `ISA-240__sec_definities`
[^3]: `ISA-450__sec_toepassingsgerichte-en-overige-verklarende-teksten_2_part2`
[^4]: `ISA-240__sec_toepassingsgerichte-en-overige-verklarende-teksten`
[^5]: `ISA-240__sec_toepassingsgerichte-en-overige-verklarende-teksten_2_part7`
[^6]: `IAS-8-grondslagen-voor-financiele-verslaggeving-schattingswijzigingen-en-fouten__sec_fouten`
[^7]: `ISA-450__sec_toepassingsgerichte-en-overige-verklarende-teksten`
