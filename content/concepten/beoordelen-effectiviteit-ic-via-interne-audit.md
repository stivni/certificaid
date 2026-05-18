---
title: Beoordelen van de effectiviteit van een intern-controlesysteem (interne audit)
tags:
- concept
- competentie
- po-1-7
linked_anchors:
- 1.7.taak.1
- 1.7.I.D
- 1.7.V
- 1.7.V.A
- 1.7.V.B
- 1.7.VIII.F
- 1.7.XI
- 1.7.IV
programmaonderdelen:
- '1.7'
confidence: inferred
node_type: competentie
status: voorgesteld
schema_version: '1.5'
gegenereerd_uit: data/concepten/records/beoordelen-effectiviteit-ic-via-interne-audit.json
gegenereerd_op: '2026-05-18'
---
# Beoordelen van de effectiviteit van een intern-controlesysteem (interne audit) 🤖


## Stappen

### 1. Auditplan opstellen op basis van risico-prioriteiten

Stel een jaarlijks en meerjarig (3 jaar) auditplan op dat alle kritische processen dekt, met focus op hoogste risico's en risico-eigenaarschap.

**Waarom?** Een risk-based auditplan voorkomt verspilling van auditcapaciteit aan lage-risico-zones en zorgt voor systematische coverage.

**📥 Input**:
- Risico-register organisatie → **Risico's met kans × impact** _(document)_
- Audit-universe (lijst alle auditbare entiteiten) → **Processen, afdelingen, IT-systemen** _(document)_

**📤 Output**:
- Jaarlijks auditplan + meerjarenplan → **Auditopdrachten met scope, timing, dagen, auditor** _(document)_

**🛠️ Hoe**:

1. Volg [[interne-audit]] §risk-based: prioriteer auditeerbare entiteiten op (a) risico-niveau uit register, (b) tijd sinds laatste audit, (c) impact van controles op rapportering.
2. Wijs minstens jaarlijks een audit toe aan ELK hoog-risico-proces én aan kritische IT-systemen.
3. Reserveer 10-20% van capaciteit voor ad-hoc onderzoeken (klokkenluidermelding, fraude-vermoeden, dringende vraag bestuur).
4. Laat het auditplan goedkeuren door auditcomité ([[auditcomite]] §rol) — bestuursorgaan voor KMO zonder auditcomité.


**Grondslag**: [[interne-audit]] §risk-based-plan, [[auditcomite]] §goedkeuring-plan, IIA Standard 2010

### 2. Auditopdracht voorbereiden — scope, criteria en programma

Per auditopdracht: definieer expliciete scope, gebruik [[evaluatiecriteria-ic]] §design-operating als toetsingskader, en stel een werkprogramma op met testen en samplemethode.

**Waarom?** Onduidelijke scope leidt tot scope-creep en zwakke conclusies. Expliciete criteria beschermen tegen subjectieve oordelen.

**📥 Input**:
- Auditplan stap 1 → **Geplande auditopdracht** _(document)_
- Procesdocumentatie van auditee (IC-handboek, flowcharts) → **Bestaand IC-systeem** _(document)_

**📤 Output**:
- Auditplan-opdracht + werkprogramma → **Scope-statement, criteria, testen, samples** _(document)_

**🛠️ Hoe**:

1. Definieer scope SMART: welk proces, welke periode, welke entiteiten, wat uitgesloten. Bv. "aankoopcyclus van Yperse Werkplaats BV voor periode 2026, exclusief inter-company".
2. Identificeer toetsingscriteria via [[evaluatiecriteria-ic]] §design-operating: is de control adequaat ontworpen? wordt ze consistent uitgevoerd?
3. Stel werkprogramma op met combinatie van: walk-through (begrip), test of design (1 transactie per control), test of operating (sample 25-60 transacties afhankelijk van frequentie en risico).
4. Plan ook cijferanalyse op kritische rekeningen — verschillen versus verwachting zijn red flags.


**Grondslag**: [[evaluatiecriteria-ic]] §design-operating, [[interne-audit]] §werkprogramma, IIA Standard 2200

### 3. Audit uitvoeren — design én operating effectiveness testen

Voer eerst een walk-through (één transactie van begin tot einde) uit om design te begrijpen; voer dan operating tests uit op een sample om consistentie te bevestigen.

**Waarom?** Design én operating zijn cumulatief nodig. Design-OK alleen geeft schijnzekerheid; operating-tests zonder design-begrip toetsen iets dat misschien niet relevant is.

**📥 Input**:
- Werkprogramma stap 2 → **Test-instructies** _(document)_

**📤 Output**:
- Werkpapieren met bevindingen → **Per test: scope, resultaten, conclusie, evidence** _(document)_

**🛠️ Hoe**:

1. Walk-through (design test): selecteer één transactie en volg ze van initiatie tot eindboeking. Identificeer alle controls die ze passeert. Test of elke control aanwezig is en logisch het risico mitigeert.
2. Test of operating: selecteer een sample volgens [[monitoring-interne-controle]] §sample-grootte (typisch 25 voor dagelijkse, 12 voor wekelijkse, 5 voor maandelijkse, 2 voor kwartaal-controls).
3. Voor elke sample-transactie: verifieer dat de control daadwerkelijk werd uitgevoerd (paraaf, ERP-flag, formulier).
4. Bij uitzonderingen (control niet uitgevoerd): bepaal of dit een isolated incident is of systematic failure — afhankelijk verschilt de conclusie sterk.


**Grondslag**: [[evaluatiecriteria-ic]] §test-methoden, [[monitoring-interne-controle]] §samples, IIA Standard 2300

> [!warning]- Documenteer elk werkpapier met cliënt, periode, opsteller, datum, reviewer, conclusie + crossreference naar werkprogramma-cel.
>
> _Vaak fout gedaan_: Werkpapieren met enkel cijfers en tikteken-symbolen — externe reviewer of opvolgende auditor kan redenering niet reconstrueren.
>
> _Grondslag_: [[interne-audit]] §documentatie, IIA Standard 2330

### 4. Bevindingen klasseren — significantie en root cause

Klasseer elke bevinding op significantie (hoog/midden/laag) en identificeer de root cause (ontwerpgebrek, uitvoeringsgebrek, monitoring-gebrek, beleid-gebrek).

**Waarom?** Zonder root cause leidt remediation tot symptoom-bestrijding. Zonder significantie krijgen alle bevindingen evenveel aandacht, ook de triviale.

**📥 Input**:
- Werkpapieren stap 3 → **Uitzonderingen en afwijkingen** _(document)_

**📤 Output**:
- Bevindingenrapport intern → **Per bevinding: feit, criterium, oorzaak, impact, aanbeveling** _(document)_

**🛠️ Hoe**:

1. Volg het IIA-bevinding-format: Condition (wat is vastgesteld), Criteria (wat moest het zijn), Cause (waarom is dit gebeurd), Consequence (wat is de impact), Corrective action (wat te doen).
2. Significantie hoog: bedreigt accuratesse van financiële rapportering, of materiële operationele schade, of significant compliance-risico. Vereist directe rapportering aan auditcomité + remediation < 3 maand.
3. Significantie midden: lokaal IC-gebrek met beheersbare impact. Remediation binnen 6-12 maand.
4. Significantie laag: efficiëntie-suggesties of housekeeping. Opname in management letter.


**Grondslag**: [[interne-audit]] §root-cause, [[evaluatie-interne-controle]] §rapportering, IIA Standard 2410


> [!todo] Voorbeeld ontbreekt voor dit concept
> Een latere ENRICH-pass voegt een synthese-voorbeeld toe.

