---
title: "Evaluatie van interne controle"
concept_type: "procedure"
schema_version: "2.2"
status: "concept"
categorieen:
  - kader
ankers:
  - 1.7.VIII.F
  - 1.7.XI
  - 1.7.XIII
tags:
  - concept
  - schema-2.2
  - type-procedure
  - cat-kader
  - status-concept
gegenereerd_uit: "data/concepten/records/evaluatie-interne-controle.json"
---

# Evaluatie van interne controle

_Procedure_

🏛️ Kader · Anchors: `1.7.VIII.F` · `1.7.XI` · `1.7.XIII` · Wave: `cluster-extract-controle-2026-05-28`

> [!info] 📝 **Concept** — content gevuld door cluster-extract; niet door mens-verify gegaan.

**Synoniemen**: internal control evaluation · control assessment · control self-assessment · operating effectiveness testing · design effectiveness review · doeltreffendheidstoets interne controle — **Vertalingen**: fr: évaluation du contrôle interne

## Definitie

📖 Evaluatie van interne controle is de gestructureerde activiteit waarbij de werking van een interne-controle-systeem wordt getoetst aan twee criteria: (1) design effectiveness - is de controle theoretisch geschikt om het beoogde risico af te dekken; (2) operating effectiveness - werkt de controle ook in de praktijk zoals ontworpen. Wordt uitgevoerd door verschillende actoren met verschillende doelen: door management zelf (continue monitoring, COSO-vijfde-component), door interne audit (onafhankelijke derde lijn), of door de externe auditor (in de planningsfase als basis voor zijn risico-inschatting en zijn beslissing om te steunen op interne controle).

<small>📚 ISA 330 — par. 8 - toetsing design effectiveness en operating effectiveness — _norm_ · ITAA-norm-kmo-controlenorm — par. 97-98 - toetsingen van interne beheersingsmaatregelen — _norm_</small>

## Substantie

🔗 Praktisch bestaat een evaluatie van interne controle uit drie soorten werkzaamheden, in oplopende mate van zekerheid: (1) inquiry - vraag aan de uitvoerder hoe hij de controle uitvoert; geeft enkel design-zekerheid; (2) walk-through - volg een transactie van begin tot einde om te zien dat de controle echt loopt; combineert design en eerste indicator van operating; (3) test of controls - selecteer een steekproef van transacties over de hele periode en toets de uitvoering; geeft operating effectiveness over de tijd. Voor sleutelcontroles waarop wordt gesteund: minstens een test of controls verplicht (ISA 330 par. 8). Voor controles waarop niet wordt gesteund: walk-through volstaat als bevestiging van design.

<small>📚 ISA 330 — par. 9 - aard en omvang toetsing — _norm_ · cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Rationale

📖 Een interne controle die niet wordt geevalueerd verliest na verloop van tijd zijn werking - personen worden anders ingezet, IT-systemen wijzigen, procedures verwateren. ISA 315 zet evaluatie expliciet in als vijfde COSO-component (monitoring activities). Voor het management: vroegtijdige detectie van degradatie en input voor remediering. Voor de externe auditor: een gefundeerde basis om al dan niet te steunen op interne controle, met directe impact op de scope en kost van de externe audit.

<small>📚 ISA 315 (herzien-2019) — par. 24 - monitoring-activities-component — _norm_</small>

## Gebruikscontext

**Status**: `in-voege`

Verplichte stap in elke externe controle (ISA 315/330) en in elke interne audit. Voor management: vrijwillig maar onderdeel van zorgvuldigheidsplicht.

**✅ Voor**
- 📖 Bij elke externe controleopdracht (planningsfase ISA 315). Bij elke interne audit volgens jaarplan. Periodiek door management als COSO-monitoring-component. Bij wijzigingen in processen, IT, organisatie of regelgeving als impact-assessment.

## Sub-concepten

### 📦 Design effectiveness  
_`procedure` (subconcept)_

#### Definitie

📖 Design effectiveness toetst of een controle, indien correct uitgevoerd, het beoogde risico zou afdekken. Typisch via inquiry en observatie. Een controle kan design-ineffectief zijn als (1) de procedure niet adressheert wat het zegt te doen (bv. 'goedkeuring' zonder echte beoordeling van inhoud); (2) de uitvoerder geen toegang heeft tot de informatie nodig om de controle uit te voeren; (3) de controle te laat in de flow zit om effect te hebben.

<small>📚 ISA 330 — par. 8 - design effectiveness — _norm_</small>

### 📦 Operating effectiveness  
_`procedure` (subconcept)_

#### Definitie

📖 Operating effectiveness toetst of een als design-effectief beoordeelde controle ook in de praktijk wordt uitgevoerd over de hele relevante periode. Vereist een test of controls op een steekproef van transacties. Bij geautomatiseerde controles volstaat vaak een kleinere steekproef (mits gekoppeld aan ITGC-toets); bij manuele controles is een ruimere steekproef nodig die de hele periode bestrijkt. Bij significante risico's: toetsing in de lopende controleperiode verplicht (ISA 330 par. 15).

<small>📚 ISA 330 — par. 8-15 — _norm_</small>

## Bouwstenen

### 👣 Inquiry (verzoek om inlichtingen)  
_`stap`_

📖 Vraag aan de procesverantwoordelijke hoe hij een controle uitvoert: welke stappen, welke documenten gebruikt hij, wanneer voert hij hem uit, wat doet hij bij een uitzondering. Inquiry alleen geeft beperkte zekerheid - de uitvoerder kan beschrijven wat hij zou moeten doen zonder het effectief te doen. Combineer altijd met observatie of test of controls voor sleutelcontroles.

<small>📚 ISA 500 — par. A14 - inquiries als type van bewijs — _norm_</small>

### 👣 Walk-through  
_`stap`_

🔗 Volg een complete transactie van begin tot einde door de cyclus. Bij elke processtap: bevraag de uitvoerder, inspecteer de gebruikte documenten en systeemschermen, observeer de uitvoering. Doel: bevestigen dat de gedocumenteerde procedure correspondeert met de werkelijke uitvoering. Eindigt met een korte bevestiging dat de geidentificeerde controles bestaan en lijken te werken. Een walk-through alleen volstaat niet voor operating effectiveness over de hele periode.

<small>📚 ISA 330 — par. 8 — _norm_</small>

### 👣 Test of controls (toetsing interne beheersingsmaatregel)  
_`stap`_

📖 Selecteer een steekproef van transacties die de hele controleperiode bestrijkt (of voor handmatige controles minstens een representatief deel). Toets per transactie of de sleutelcontrole effectief is uitgevoerd zoals voorgeschreven. Aanvaardbaar afwijkingspercentage hangt af van de gewenste mate van zekerheid - in audit-context vaak nul-tolerantie voor kritieke controles (bv. autorisatie boven 100.000 EUR). Eventuele afwijkingen analyseren: oorzaak, mogelijke gevolgen, aanpassing van risico-inschatting.

<small>📚 ISA 330 — par. 16-17 evalueren effectieve werking — _norm_ · ISA 530 — Gebruik van steekproeven bij een controle — _norm_</small>

### ⚙️ Control self-assessment door process owners  
_`mechanisme`_

🔗 Process owners (managers van een afdeling of cyclus) beoordelen periodiek zelf hun eigen controles via vragenlijsten, scorecards of workshops. Voordeel: hoge betrokkenheid, snelle detectie van issues. Nadeel: gebrek aan onafhankelijkheid, optimisme-bias. Typisch combinatie: self-assessment kwartaalbasis + onafhankelijke interne audit jaarlijks-basis + externe audit jaarlijks-basis voor financiele rapportering.

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

### 📜 Tekortkomingen categoriseren (ISA 265)  
_`regel`_

📖 Gevonden tekortkomingen worden gecategoriseerd op basis van significantie: (1) significante tekortkoming - moet schriftelijk aan met governance belaste personen worden gerapporteerd (auditcomite of bestuursorgaan); (2) andere tekortkoming - rapporteren aan management. ISA 265 par. A6-A7 geeft criteria: waarschijnlijkheid van afwijkingen van materieel belang in financiele overzichten, vatbaarheid voor verlies of fraude, complexiteit van schattingen, omvang van de blootgestelde transactiestromen.

<small>📚 ISA 265 — par. 6-9 + A6-A7 — _norm_</small>

### 📜 Frequentie en rotatie van toetsing  
_`regel`_

📖 Voor controles waarop de externe auditor steunt zonder significant risico: minstens een keer per drie controleperiodes toetsen, met een deel van de controles elke periode (ISA 330 par. 14). Voor significante risico's: elk jaar toetsen verplicht (par. 15). Bij wijzigingen in de controle sinds de vorige toetsing: opnieuw toetsen in de lopende periode (par. 14(a)).

<small>📚 ISA 330 — par. 14-15 — _norm_</small>

## Voorbeelden

### 💡 Evaluatie van aankoopautorisatie-controle bij Zelena Bio NV 🔗

_Externe auditor wil steunen op de tweehandtekeningsregel boven 5.000 EUR in de aankoopcyclus bij Zelena Bio NV._

**Weergave** `stappenlijst`:

```json
{
  "stappen": [
    "Stap 1 - Inquiry: vraag aan de aankoopverantwoordelijke en de zaakvoerder hoe de tweehandtekeningsregel werkt en aan welk bewijs het wordt gedocumenteerd",
    "Stap 2 - Design assessment: bevestig dat de procedure voorziet in formele goedkeuring door twee gemachtigden boven 5.000 EUR en dat deze in het ERP wordt afgedwongen (system-blokkering zonder beide handtekeningen)",
    "Stap 3 - Walk-through: volg een specifieke aankoop boven 5.000 EUR door de cyclus en bevestig dat beide handtekeningen aanwezig zijn",
    "Stap 4 - Test of controls: trek een steekproef van 25 inkoopfacturen boven 5.000 EUR verspreid over het boekjaar; toets per factuur de aanwezigheid en authenticiteit van beide handtekeningen",
    "Stap 5 - Evaluatie: nul afwijkingen → operating effectiveness bevestigd, auditor kan steunen en zijn gegevensgerichte werkzaamheden inperken; afwijkingen → oorzaakanalyse + uitbreiding gegevensgerichte controles"
  ]
}
```

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Valkuilen

### ⚠️ Design effectiveness verwarren met operating effectiveness

**Verkeerde assumptie**: Een goed gedocumenteerde procedure betekent dat de controle ook effectief werkt.

**Kernpunt**: Design effectiveness en operating effectiveness zijn twee aparte tests. Een procedure kan perfect ontworpen zijn maar in de praktijk niet uitgevoerd (medewerkers volgen de procedure niet, slaan stappen over, geven elkaar paswoorden). Beide moeten apart getoetst worden vooraleer wordt gesteund op de controle.

<small>📚 ISA 330 — par. 8 — _norm_</small>

### ⚠️ Steekproef van een transactie laten doorgaan voor een toetsing

**Verkeerde assumptie**: Met een walk-through op een transactie heb ik de controle voldoende getoetst.

**Kernpunt**: Een walk-through geeft enkel een momentopname; operating effectiveness over de hele periode vergt een steekproef die de hele periode bestrijkt. Voor sleutelcontroles is dat een verplichting (ISA 330 par. 8 + 14).

<small>📚 ISA 330 — par. 8 — _norm_</small>

### ⚠️ Geen onderzoek doen naar afwijkingen

**Verkeerde assumptie**: Een paar afwijkingen in een steekproef zijn normaal en mogen genegeerd worden.

**Kernpunt**: ISA 330 par. 17 vereist dat de auditor bij gedetecteerde deviaties specifiek onderzoek doet naar oorzaken en gevolgen, en bepaalt of (a) de toetsingen een passende basis blijven voor steunen, (b) aanvullende toetsingen nodig zijn, of (c) terugvallen op gegevensgerichte controles. Een afwijking kan symptomatisch zijn voor een veel grotere onderliggende controle-zwakte.

<small>📚 ISA 330 — par. 17 — _norm_</small>

## Accountant-perspectieven

### Externe auditor evalueert interne controle cliente

_De externe auditor in de planning- en uitvoeringsfase die de werking van interne controle moet toetsen._

#### 🔍 Auditor

##### 👣 Sleutelcontroles selecteren voor toetsing  
_`stap`_

📖 Niet alle controles toetsen: focus op de sleutelcontroles per significant risico. Selecteer per bewering en per significant rekeningsaldo de controles die voldoende zekerheid kunnen geven indien effectief werkend. Documenteer de selectie in het audit-dossier met motivering.

<small>📚 ISA 330 — par. 6-7 — _norm_</small>

##### 👣 Rapportering via management letter  
_`stap`_

📖 Significante tekortkomingen worden in een management letter aan het auditcomite (of bestuursorgaan) gerapporteerd. Per tekortkoming: beschrijving, mogelijke gevolgen voor de financiele overzichten, aanbeveling voor remediering, management response (wat gaat het management eraan doen en wanneer). Andere tekortkomingen apart aan operationeel management.

<small>📚 ISA 265 — par. 9-11 — _norm_</small>

### Interne auditor evalueert eigen IC-systeem

_De interne auditor in een geplande audit-opdracht van een specifiek cyclus of process._

#### 🔍 Auditor

##### 👣 Audit-rapport met bevindingen en aanbevelingen  
_`stap`_

🔗 Resultaat is een audit-rapport met per bevinding: feitenvaststelling (wat is gevonden), risico (welk financieel/operationeel/compliance-risico), aanbeveling (wat zou anders moeten), management response (commitment van proceseigenaar), deadline. Status: open, in progress, closed. Follow-up bij volgende cyclus.

<small>📚 cluster-extract-agent (opus-4.7-1M) — _ai_model_ — (2026-05-28)</small>

## Verder lezen (scope-out)

- → Interne controle als object van evaluatie → [[interne-controle]] _(moet-verwijzen)_
- → Externe auditor doet zelfde activiteit (cross) → [[audit-planning]] _(moet-verwijzen)_
- → Interne audit als uitvoerder → [[interne-audit]] _(moet-verwijzen)_
- → Auditcomite-rapportering → [[auditcomite]] _(moet-verwijzen)_
- ↪ COSO-monitoring-component → [[coso-framework]] _(mag-verwijzen)_

## Relaties

### `valt_onder`
- [[interne-controle]]
### `uitgevoerd_door`
- [[interne-audit]]
### `gedocumenteerd_in`
- [[auditcomite]] — Rapportering van significante tekortkomingen gebeurt schriftelijk aan auditcomite (ISA 265).
