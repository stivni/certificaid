---
title: Bijzondere waardevermindering (regime-overstijgend)
tags:
- concept
- cluster
- po-1-1
- po-1-5
linked_anchors:
- 1.5.V.A
- 1.1.II.G
programmaonderdelen:
- '1.1'
- '1.5'
confidence: inferred-from-aggregation
node_type: cluster
status: seed
schema_version: '1.6'
gegenereerd_uit: data/concepten/records/bijzondere-waardevermindering.json
gegenereerd_op: '2026-05-18'
---
# Bijzondere waardevermindering (regime-overstijgend) 🤖

Het examenprogramma toetst onder PO 1.5.V.A de IFRS-mechaniek (impairment-test, CGU, omkering) naast PO 1.1 de BE-GAAP-mechaniek (aanvullende afschrijving, waardevermindering). De stagiair moet beide regimes kennen én weten hoe ze functioneel hetzelfde economische probleem (boekwaarde > realiseerbare waarde) op verschillende manieren oplossen.

> [!summary] Korte inhoud
> Bijzondere waardevermindering is de boekhoudkundige erkenning van een waardeverlies op een actief wanneer de realiseerbare of gebruikswaarde van dat actief lager ligt dan zijn boekhoudkundige restwaarde.

> [!info] Behoort tot: [[waarderingsregels-jaarrekening]]

Bijzondere waardevermindering is de boekhoudkundige erkenning van een waardeverlies op een actief wanneer de realiseerbare of gebruikswaarde van dat actief lager ligt dan zijn boekhoudkundige restwaarde. Onder elk boekhoudregime is de logica gelijk: detecteer indicatoren, vergelijk boekwaarde met realiseerbare/gebruikswaarde, registreer het verschil als verlies of als aanvullende afschrijving. De rekenmethode en rapportering verschillen wezenlijk tussen IFRS (IAS 36 — formele test, expliciete CGU) en BE GAAP (KB WVV art. 3:42 — gebruikswaarde voor de vennootschap, principe-gebaseerd).

_Bron: Aggregatie IAS 36 + KB WVV art. 3:42-3:43_


## Bouwstenen

### Trigger: waarde-indicatoren ⚖️

Bij elke afsluiting beoordeelt het bestuur of er indicatoren zijn dat een actief waarde verloren heeft: externe (marktwaarde, technologische obsolescentie, sectoriële krimp) en interne (fysieke beschadiging, verminderd gebruik, ondermaatse prestatie). Onder IFRS verplichte jaarlijkse test voor goodwill en immaterieel-onbepaald.

**Waarom?** De trigger is regime-onafhankelijk: de boekhouding moet getrouw beeld bewaren. Verschil zit in hoe formeel de test is (IFRS-protocol versus BE-GAAP-oordeel).




_Grondslag: IAS 36 alinea 9-17; KB WVV art. 3:42 § 1 lid 2_

### Vergelijking boekwaarde met waarde-maatstaf ⚖️

Het verlies = boekwaarde − realiseerbare/gebruikswaarde. Onder IFRS is realiseerbare waarde = hoogste van fair value less costs of disposal (FVLCD) en value in use (VIU). Onder BE GAAP is de maatstaf 'gebruikswaarde voor de vennootschap' — meestal beoordeeld door het bestuur zonder voorgeschreven rekenmodel.

**Waarom?** Beide regimes vertrekken van een 'wat is dit actief economisch nog waard?'-vraag. IFRS formaliseert die vraag (FVLCD, VIU, discontering). BE GAAP geeft het oordeel aan het bestuur, met principle-based onderbouwing.




_Grondslag: IAS 36 alinea 18-57 (realiseerbare waarde); KB WVV art. 3:42 § 1 (gebruikswaarde voor de vennootschap)_

### Boeking: verlies versus aanvullende afschrijving ⚖️

Onder IFRS wordt het verlies onmiddellijk in W&V geboekt (tenzij herwaarderingsreserve aanwezig — dan eerst tegenover OCI tot de reserve op is). Onder BE GAAP onderscheid: voor materiële vaste activa **met** beperkte gebruiksduur = aanvullende of niet-recurrente afschrijving (art. 3:42 § 1 lid 2); voor materiële vaste activa **zonder** beperkte gebruiksduur (terreinen, kunstwerken) = waardevermindering (art. 3:42 § 2).

**Waarom?** Het BE-GAAP-onderscheid 'aanvullende afschrijving' versus 'waardevermindering' is een examen-klassieker. Stagiair moet de gebruiksduur-vraag herkennen om de juiste rekening te kiezen.




_Grondslag: IAS 36 alinea 60-64 (impairment loss); KB WVV art. 3:42 § 1 lid 2 (beperkte gebruiksduur) + art. 3:42 § 2 (onbeperkte gebruiksduur)_

### Omkering van eerder verlies ⚖️

Onder IFRS is omkering verplicht zodra de indicatoren omgekeerd zijn — behalve voor goodwill (verbod op terugneming, IAS 36 alinea 124). Onder BE GAAP is terugneming verplicht zodra de verminderwaarde wegvalt (KB WVV art. 3:39 — terugneming waardeverminderingen).

**Waarom?** Goodwill-asymmetrie onder IFRS (afgeschreven verlies blijft permanent) is een sleutelverschil met BE-GAAP-praktijk en wordt regelmatig getoetst.




_Grondslag: IAS 36 alinea 109-125 (omkering); KB WVV art. 3:39 (terugneming)_


> [!info]- Niet verwarren met [[bijzondere-waardevermindering-ifrs]]
> Algemeen cluster dekt regime-overstijgende kern (indicatoren, boekwaarde-vergelijking, boekingslogica). IFRS-specialisatie dekt IAS 36-mechaniek: realiseerbare waarde = hoogste van FVLCD en VIU, expliciete CGU-allocatie, jaarlijkse test goodwill en immaterieel-onbepaald.
>
> _Trigger_: Algemeen → 'wat is het mechanisme van bijzondere waardevermindering?'; IFRS → 'hoe bereken ik VIU?' / 'wat is CGU-allocatie?'

> [!info]- Niet verwarren met [[bijzondere-waardevermindering-be-gaap]]
> Algemeen cluster dekt regime-overstijgende kern. BE-GAAP-specialisatie dekt het onderscheid aanvullende afschrijving versus waardevermindering en de art. 3:42-redactie 'gebruikswaarde voor de vennootschap'.
>
> _Trigger_: Algemeen → 'wat is het mechanisme?'; BE GAAP → 'aanvullende afschrijving of waardevermindering — welk artikel?'


> [!todo] Voorbeeld ontbreekt voor dit concept
> Een latere ENRICH-pass voegt een synthese-voorbeeld toe.

## Bronnen

[^1]: `IAS-36-bijzondere-waardevermindering__sec_indicatoren`
[^2]: `IAS-36-bijzondere-waardevermindering__sec_realiseerbare-waarde`
[^3]: `KB-WVV-uitvoering__sec_waardeverminderingen`
[^4]: `IAS-36-bijzondere-waardevermindering__sec_omkering`
