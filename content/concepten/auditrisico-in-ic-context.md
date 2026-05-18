---
title: Auditrisico in IC-context
tags:
- concept
- begrip
- po-1-7
linked_anchors:
- 1.7.V.E
- 1.7.V
programmaonderdelen:
- '1.7'
confidence: grounded
node_type: begrip
status: seed
schema_version: '1.6'
gegenereerd_uit: data/concepten/records/auditrisico-in-ic-context.json
gegenereerd_op: '2026-05-18'
---
# Auditrisico in IC-context ⚖️

Het auditrisicomodel (AR = IR × CR × DR) krijgt in IC-context een specifieke focus: het intern beheersingsrisico (CR) wordt rechtstreeks gemoduleerd door de kwaliteit van het IC-systeem van de cliënt. Een sterk IC verlaagt CR — daardoor mag de auditor minder gegevensgerichte werkzaamheden inplannen zonder dat het audit-risico stijgt. Dit verband is de hefboom waarop de hele IC-toetsing van de externe auditor gebouwd is.

> [!summary] Korte inhoud
> Auditrisico is het risico dat de auditor een verkeerde controleverklaring afgeeft over een jaarrekening die in werkelijkheid materieel afwijkend is.

> [!info] Specialisatie van: [[auditrisicomodel]]

Auditrisico is het risico dat de auditor een verkeerde controleverklaring afgeeft over een jaarrekening die in werkelijkheid materieel afwijkend is. Audit risico = Inherent risico × Intern beheersingsrisico × Detectierisico (zie [[auditrisicomodel]]). In de context van IC: hoe sterker het IC-systeem, hoe lager het intern beheersingsrisico, hoe minder substantief testwerk de auditor nodig heeft.

_Bron: ITAA-norm-kmo-controlenorm Bijlage 1 + §97-§98_


## Bouwstenen

### Sterk IC → lager CR → minder gegevensgericht werk ⚖️

Het intern beheersingsrisico (CR) is rechtstreeks afhankelijk van het IC-systeem van de cliënt. Wanneer de auditor inschat dat de IC effectief is opgezet én operationeel werkt, kan hij CR op 'laag' inschatten. Bij een gewenst totaal-auditrisico (bv. 5 %) kan het ontdekkingsrisico (DR) dan hoger zijn → minder substantieve werkzaamheden volstaan.

**Waarom?** Dit is de economische rationale van IC-evaluatie door de externe auditor: tijd besparen op gegevensgerichte tests die hoog overlappen met IC-werking. Zonder dat IC-CR-verband zou audit duur en weinig efficiënt zijn.


**In de praktijk**: Bij Rotex Roeselare NV met sterke aankoopcyclus-IC: enkele walkthroughs + 25 controle-tests + analytische review volstaan. Bij Transport Tongeren BV met zwakke verkoopcyclus-IC: volledige substantieve testen van vorderingen + bevestigingen + cut-off-tests.


_Grondslag: ITAA-norm-kmo-controlenorm §97-§98; ISA 330 §6-7_

### Verplichte test-of-controls bij CR-verlaging ⚖️

Als de auditor van plan is om CR lager dan 'maximum' in te schatten en daarop te steunen, moet hij dat onderbouwen met toetsingen van de werking van de interne beheersingsmaatregelen ('test of controls'). Inquiry en observatie alleen volstaan niet — er moet ook bewijs uit inspectie of heruitvoering komen.

**Waarom?** ISA 315 §34 verbiedt dat de auditor enkel op design-effectiviteit van IC steunt: hij moet de werking ook toetsen. Anders kan een mooi gedocumenteerd maar niet-uitgevoerd IC-stelsel onterecht tot CR-verlaging leiden.


**In de praktijk**: Examenval: 'mag de auditor CR op laag zetten enkel op basis van een walkthrough?' → Nee. Walkthrough toont design + bestaan; werking vereist samples van transacties + inspectie van het bewijs van uitvoering (handtekeningen, ERP-logs, checklists).


_Grondslag: ISA 315 (herzien-2019) §34; ISA 330 §8_

### Schaalbaarheid: minder geformaliseerde IC bij kleinere entiteiten ⚖️

In een minder complexe entiteit kan de auditor inzicht in IC verwerven via directe waarneming (bv. fysieke voorraadtelling, functiescheiding observeren) ook al is de IC niet schriftelijk gedocumenteerd. Schaal van toetsing volgt schaal en complexiteit van de entiteit, niet een vast minimum.

**Waarom?** ISA 315 (herzien-2019) erkent expliciet de schaalbaarheid: kmo-audits volgen dezelfde principes maar met een proportionele aanpak. Documentatie-gebrek alleen is geen ground voor CR=maximum, mits de auditor andere controle-informatie verkrijgt.


**In de praktijk**: Bij Yperse Werkplaats BV (15 VTE) is er geen IC-handboek. De commissaris observeert dat de zaakvoerder elke aankoopfactuur tekent vóór betaling én dat de boekhouder een tweede goedkeuring vraagt voor uitgaven > € 5.000. Dit volstaat als bewijs van IC-werking voor de aankoopcyclus.


_Grondslag: ISA 315 (herzien-2019) §A33 + Schaalbaarheid_


## Valkuilen

> [!warning]- CR ≠ IC
> ⚠️ CR ≠ IC. CR is de risico-inschatting van de auditor; IC is de objectieve realiteit bij de cliënt. Een sterk IC verlaagt CR, maar een lage CR-inschatting is geen vervanging voor IC-werking — als IC tijdens het boekjaar verandert, moet CR opnieuw worden ingeschat. 🤖


> [!warning]- Ontdekkingsrisico (DR) staat los van IC — het is een eigenschap van de werkzaamheden van de auditor zelf
> ⚠️ Ontdekkingsrisico (DR) staat los van IC — het is een eigenschap van de werkzaamheden van de auditor zelf. Een lager DR vergt méér en gerichtere substantieve werkzaamheden; IC kan DR niet beïnvloeden. 🤖



## Zie ook

- **Vereist kennis van**: [[toetsing-interne-beheersing]]
- **Vereist kennis van**: [[evaluatie-interne-controle]]

## Voorbeelden

Bij Yperse Werkplaats BV inschat Sofie Janssens het inherente risico op voorraadwaardering als 'middel-hoog' (productie-WIP, schatting nodig). Intern beheersingsrisico = 'laag' want maandelijkse stockcount + ERP met audit trail. Dus IR×CR = middel → detectierisico mag iets hoger → minder substantieve testwerk nodig.

## Bronnen

[^1]: `ITAA-norm-kmo-controlenorm__sec_bijlage-1-definities_part4`
[^2]: `ITAA-norm-kmo-controlenorm__sec_toetsingen-van-interne-beheersingsmaatregelen`
[^3]: `ISA-315-herzien-2019__sec_vereisten_2_part4`
[^4]: `ISA-315-herzien-2019__sec_schaalbaarheid_8_part3`
