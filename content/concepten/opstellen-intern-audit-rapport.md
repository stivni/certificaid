---
title: Opstellen van een intern-audit-rapport
tags:
- concept
- competentie
- po-1-7
linked_anchors:
- 1.7.taak.1
- 1.7.V.A
- 1.7.V.B
- 1.7.V.D
- 1.7.VIII.F
- 1.7.XIII
programmaonderdelen:
- '1.7'
confidence: inferred
node_type: competentie
status: voorgesteld
schema_version: '1.5'
gegenereerd_uit: data/concepten/records/opstellen-intern-audit-rapport.json
gegenereerd_op: '2026-05-18'
---
# Opstellen van een intern-audit-rapport 🤖


## Stappen

### 1. Conceptrapport opstellen — feiten en aanbevelingen per bevinding

Werk elk bevindingenpaar uit volgens het IIA-5C-format: Condition, Criteria, Cause, Consequence, Corrective action. Werk per bevinding één paragraaf.

**Waarom?** Een goed gestructureerde bevinding kan door management direct gebruikt worden voor remediation. Onduidelijke bevindingen leiden tot weerwoord en uitstel.

**📥 Input**:
- Werkpapieren met bevindingen (uit auditopdracht) → **Geverifieerde feiten + analyses** _(document)_

**📤 Output**:
- Conceptrapport → **Voor elke bevinding 5C-uitwerking + significantie-klasse** _(document)_

**🛠️ Hoe**:

1. Volg [[interne-audit]] §5C-format.
   a. Condition: wat hebben we vastgesteld? Concreet, met cijfers waar mogelijk.
   b. Criteria: wat had het moeten zijn? Verwijs naar IC-handboek-sectie, wettekst, beleid.
   c. Cause: waarom is dit zo gegaan? Root cause uit de [[beoordelen-effectiviteit-ic-via-interne-audit]] §root-cause-analyse.
   d. Consequence: wat is de impact? Financieel (€), operationeel (kwaliteit, doorlooptijd), of reputationeel.
   e. Corrective action: wat moet er gebeuren? Specifiek, met deadline, met eigenaar.
2. Klasseer significantie (hoog/midden/laag) bovenaan elke bevinding.
3. Vermijd zachte woorden ("misschien", "lijkt") — feitelijke vaststellingen of nog niet vermelden.
4. Citeer evidence uit werkpapier (referentie-code) — niet de evidence zelf reproduceren.


**Grondslag**: [[interne-audit]] §5C-format, IIA Standard 2410

> [!warning]- Citeer voor elke bevinding het criterium expliciet ([[interne-controle]]-handboek sectie X, beleid Y, wet Z) — niet enkel 'best practice'.
>
> _Vaak fout gedaan_: Bevindingen zonder criterium — auditee discussieert dan terecht 'waar staat dit dan?'.
>
> _Grondslag_: [[interne-audit]] §criteria, IIA Standard 2410

### 2. Conceptrapport bespreken met auditee — recht op weerwoord

Stuur het conceptrapport naar het management van de geauditeerde afdeling, hou een formele exit-meeting, en verzamel hun reactie + remediation-commitments.

**Waarom?** Onaangekondigde rapporten zonder management-respons leiden tot weerstand en geen actie. Procesoreectheid vereist hoor + wederhoor.

**📥 Input**:
- Conceptrapport stap 1 → **Bevindingen + aanbevelingen** _(document)_

**📤 Output**:
- Conceptrapport + management-respons-paragraaf → **Per bevinding: management-respons + actiehouder + deadline** _(document)_

**🛠️ Hoe**:

1. Stuur conceptrapport minstens 2 weken voor exit-meeting naar auditee-management.
2. Vraag schriftelijke management-respons per bevinding: erkennen / niet-erkennen + reden, actie + eigenaar + deadline.
3. Houd een exit-meeting met auditee-management om resterende verschillen te bespreken. Documenteer eventuele blijvende verschillen ('management disagrees').
4. Bij blijvende disagreement: rapporteer beide standpunten in finaal rapport — auditcomité oordeelt.


**Grondslag**: [[interne-audit]] §wederhoor, IIA Standard 2440

### 3. Finaal rapport opmaken — executive summary + detailbevindingen

Werk het rapport in finale vorm uit: executive summary (max 1 pagina), context, scope, methodologie, geclassificeerde bevindingen, management-respons, conclusie en handtekening.

**Waarom?** Bestuursorgaan en auditcomité lezen vaak alleen de executive summary. Detailbevindingen voor remediation-eigenaars.

**📥 Input**:
- Conceptrapport + management-respons → **Volledige inhoud** _(document)_

**📤 Output**:
- Finaal auditrapport → **Definitief verslag voor distributie** _(document)_

**🛠️ Hoe**:

1. Bouw vaste structuur: (1) Executive summary, (2) Achtergrond en scope, (3) Methodologie, (4) Bevindingen per significantie, (5) Management-respons, (6) Conclusie + algemene opinie over IC.
2. Executive summary bevat de top-3-bevindingen + overall control rating (typisch satisfactory / needs improvement / unsatisfactory).
3. Identificeer waar bevindingen patronen vormen — bv. drie keer "ontoereikende monitoring" wijst op cultureel/systemisch probleem, niet drie aparte issues.
4. Onderteken door audit-leider + dateer. Voor vertrouwelijkheid: classificatie "Confidential — Internal Audit" en distributie-controle.


> [!example]- Voorbeeld: Sofie Janssens (interne auditor Rotex Roeselare NV) voltooit een audit van de aankoopcyclus voor Q3 2026
> Sofie Janssens (interne auditor Rotex Roeselare NV) voltooit een audit van de aankoopcyclus voor Q3 2026. Auditperiode 8 weken, scope drie business units.
>
> 1. **Executive summary (uittreksel)** 💬
>
>    Overall control rating: Needs Improvement
>    
>    Top-3 bevindingen:
>    1. (HOOG) 12% van leveranciers in masterdata zonder verificatie KBO + ondertekening (€ 4,2M cumulatieve aankoopwaarde) — risico fraudeleuze leveranciers.
>    2. (HOOG) SOD-conflict in business unit B: aankoopgoedkeurder Tom Lefèvre = factuurgoedkeurder. Geen compenserende control.
>    3. (MIDDEN) Drie-weg-match-paraaf ontbreekt op 8% sample (drempel 5%). Reden: ERP-veld optioneel, geen blokker.
>    
>
> 2. **Bevinding 1 detail (5C-format)** 💬
>
>    Condition: 47 van 392 actieve leveranciers (12%) in SAP-master zonder ondertekend leveranciersregistratieformulier of KBO-verificatie. Cumulatieve aankoopvolume 2026: € 4.200.000.
>    
>    Criteria: IC-handboek §A.3.2 vereist KBO-check + tweede goedkeuring CFO + ondertekend formulier vóór activering. ITAA-norm-kmo-controlenorm Bijlage 1 §96.
>    
>    Cause: Vóór SAP-migratie (juni 2025) bestaande leveranciers werden zonder review overgenomen.
>    
>    Consequence: Risico fictieve of vooraf gefraudeerde leveranciers; € 4,2M aan betalingen vatbaar voor fraudeel diversion.
>    
>    Corrective action: Alle 47 leveranciers retrospectief verifiëren tegen 31/12/2026; ERP-flag activeren die nieuwe boeking blokkeert zonder registratie-evidence; aanvragen status-update aan CFO per maand.
>    
>    Owner: Aankoopdirecteur + CFO. Deadline: 31/12/2026. Status follow-up: kwartaal.
>    
>
> 3. **Distributie + handtekening** 💬
>
>    Distributie: CEO Pieter Vermeulen; CFO; Aankoopdirecteur Tom Lefèvre; Auditcomité-voorzitter Robert Vandenberghe; externe commissaris (na auditcomité-vergadering).
>    Datum: 15/10/2026
>    Handtekening: Sofie Janssens, Head of Internal Audit
>    
>

**Grondslag**: [[interne-audit]] §rapportstructuur, IIA Standard 2410-2440

### 4. Rapport presenteren aan auditcomité en remediation opvolgen

Presenteer het rapport in de auditcomité-vergadering, bespreek significante bevindingen + management-respons, en plan kwartaal-status-update over remediation.

**Waarom?** Rapport zonder accountability-platform leidt tot niet-uitgevoerde acties. Auditcomité is de governance-laag die remediation afdwingt.

**📥 Input**:
- Finaal rapport stap 3 → **Definitief verslag** _(document)_

**📤 Output**:
- Auditcomité-notulen + remediation-tracking-spreadsheet → **Beslissingen + open acties** _(document)_

**🛠️ Hoe**:

1. Presenteer in auditcomité-vergadering (typisch kwartaal). Volg [[auditcomite]] §rol — comité oordeelt over significantie en pusht remediation.
2. Houd een remediation-tracker bij: per actie status (open / in progress / completed / overdue), eigenaar, deadline, evidence van completion.
3. Volg minstens per kwartaal alle openstaande acties op — overdue items rapporteren naar auditcomité en CEO.
4. Sluit een bevinding pas af ('closed') na retest door interne audit dat de remediation effectief werkt — niet enkel op verklaring van auditee.


**Grondslag**: [[auditcomite]] §rol, [[interne-audit]] §follow-up, IIA Standard 2500

> [!warning]- Sluit bevindingen enkel na retest die operating effectiveness bevestigt — niet op management-verklaring alleen.
>
> _Vaak fout gedaan_: Bevinding 'closed' verklaren omdat management zegt 'het is opgelost' — drie maanden later blijkt het niet zo.
>
> _Grondslag_: [[interne-audit]] §follow-up, IIA Standard 2500


