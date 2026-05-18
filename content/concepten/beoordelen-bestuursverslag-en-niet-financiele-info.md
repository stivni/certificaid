---
title: Beoordelen van het bestuursverslag en de niet-financiële informatie
tags:
- concept
- competentie
- po-1-3
linked_anchors:
- 1.3.taak.1
- 1.3.I.E
- 1.3.I.C.1
- 1.3.I.D.2
programmaonderdelen:
- '1.3'
confidence: inferred
node_type: competentie
status: voorgesteld
schema_version: '1.5'
gegenereerd_uit: data/concepten/records/beoordelen-bestuursverslag-en-niet-financiele-info.json
gegenereerd_op: '2026-05-18'
---
# Beoordelen van het bestuursverslag en de niet-financiële informatie 🤖


## Stappen

### 1. Verzamelen van het bestuursverslag en het commissarisverslag

Haal de narratieve documenten op die bij de jaarrekening horen.

**Waarom?** Zonder de tekst kun je niet beoordelen of de cijfers correct geduid zijn.

**📥 Input**:
- Centraal Balanscentrum (CBSO) — NBB → **Volledige neerlegging, inclusief bestuursverslag en commissarisverslag** _(document)_

**📤 Output**:
- Document-werkbestand → **PDF's of platte tekst van de verslagen** _(document)_

**🛠️ Hoe**:

1. Open de NBB-depositie van Rotex Roeselare NV en controleer of het bestuursverslag aanwezig is — verkort of micro-schema mogen het soms weglaten.
2. Indien afwezig en de vennootschap is verplicht een verslag op te stellen: flag als hiaat in het dossier.
3. Indien een commissaris is benoemd: haal ook het commissarisverslag op.
4. Bewaar in werkmap met dezelfde naamconventie als jaarrekeningen (vennootschap-N-bestuursverslag.pdf).


**Grondslag**: [[bestuursverslag]] §verplichte-rubrieken (Richtlijn 2013/34/EU art. 19)

### 2. Toetsen van de verplichte rubrieken

Loop de wettelijk verplichte rubrieken af en controleer dat elk aanwezig is.

**Waarom?** Een onvolledig bestuursverslag is een wettelijke tekortkoming en zegt iets over de kwaliteit van de governance.

**📥 Input**:
- Bestuursverslag → **Volledige tekst** _(document)_

**📤 Output**:
- Compliance-checklist → **Per rubriek aanwezig of ontbrekend** _(conclusie)_

**🛠️ Hoe**:

1. Toets aanwezigheid volgens [[bestuursverslag]] §stap-1, §stap-2 en §stap-3:
   - Ontwikkeling van het boekjaar en resultaat.
   - Voornaamste risico's en onzekerheden ([[risicoparagraaf-bestuursverslag]] §vier-verplichte-risicos).
   - Gebeurtenissen na balansdatum.
   - Onderzoek en ontwikkeling.
   - Eigen aandelen + bijkantoren.
   - Gebruik van financiële instrumenten (indien materieel).
2. Voor beursgenoteerde vennootschappen ook: corporate-governance-verklaring ([[corporate-governance-verklaring]] §comply-or-explain).
3. Voor grote vennootschappen ook: niet-financiële verklaring (NFRD/CSRD waar van toepassing).
4. Markeer per rubriek: aanwezig / ontbrekend / oppervlakkig.


> [!example]- Voorbeeld: Rotex Roeselare NV (grote NV) — checklist bestuursverslag
> Rotex Roeselare NV (grote NV) — checklist bestuursverslag.
>
> 1. **Compliance-checklist** 🧮
>
>    | Rubriek                                    | Aanwezig? | Diepgang        |
>    |--------------------------------------------|-----------|-----------------|
>    | Ontwikkeling boekjaar + resultaat          | Ja        | Volledig        |
>    | Risico's en onzekerheden                   | Ja        | Vier categorieën ontbreken |
>    | Hedging-beleid                             | Nee       | Materieel — flag |
>    | Gebeurtenissen na balansdatum              | Ja        | Volledig        |
>    | Onderzoek en ontwikkeling                  | Ja        | Beknopt         |
>    | Eigen aandelen                             | n.v.t.    | —               |
>    | Corporate governance (niet beursgenoteerd) | n.v.t.    | —               |
>    
>

**Grondslag**: [[bestuursverslag]] §verplichte-rubrieken, [[risicoparagraaf-bestuursverslag]] §vier-categorieen

> [!warning]- Onderscheid tussen "niet vermeld" en "niet van toepassing".
>
> _Vaak fout gedaan_: Een rubriek als ontbrekend flaggen terwijl ze terecht niet van toepassing is (bv. onderzoek-en-ontwikkeling bij een handelszaak).
>
> _Grondslag_: [[bestuursverslag]] §materialiteit

### 3. Kritisch lezen van de risicoparagraaf

Beoordeel of de risicoparagraaf concrete risico's beschrijft of slechts boilerplate is.

**Waarom?** Een goede risicoparagraaf is een vroege waarschuwing voor problemen die niet uit de cijfers blijken.

**📥 Input**:
- Risicoparagraaf uit bestuursverslag → **Tekst over financiële risico's en onzekerheden** _(document)_

**📤 Output**:
- Risico-evaluatie → **Per risico: concreet/oppervlakkig + impact-inschatting** _(conclusie)_

**🛠️ Hoe**:

1. Identificeer de vier verplichte financiële risicocategorieën uit [[risicoparagraaf-bestuursverslag]] §vier-verplichte-risicos: prijsrisico, kredietrisico, liquiditeitsrisico, kasstroomrisico.
2. Voor elk: vraag of het concreet beschreven is met bedragen of percentages, of louter algemene zinnen ("wij volgen de markten op").
3. Toets aan de cijfers: een risicoparagraaf die "geen kredietrisico" claimt terwijl 60% van de omzet bij één klant zit, is niet betrouwbaar.
4. Controleer hedging-beleid: gebruikt de onderneming derivaten? Welke? Tegen welke risico's?
5. Documenteer bevindingen — een zwakke risicoparagraaf is op zich een rood vlaggetje voor governance-kwaliteit.


**Grondslag**: [[risicoparagraaf-bestuursverslag]] §hedging-beleid-expliciet

### 4. Confronteren van het narratief met de cijfers

Toets of de positieve toonzetting strookt met de cijfers — en omgekeerd.

**Waarom?** Bestuurders hebben belang bij positieve framing — een analist moet narratief en cijfers naast elkaar lezen.

**📥 Input**:
- Bestuursverslag (volledige tekst) → **Trefwoorden, framing, claims** _(document)_
- Berekende ratio's + evolutie-tabellen → **Liquiditeit, solvabiliteit, rentabiliteit** _(percentage)_

**📤 Output**:
- Consistentie-paragraaf → **Bevestiging of tegenspraak narratief-cijfers** _(document)_

**🛠️ Hoe**:

1. Markeer in het bestuursverslag passages over "groei", "marges", "marktaandeel", "uitdagingen", "going concern".
2. Toets aan de cijfers: claimt het bestuursverslag "stevige marges" terwijl bedrijfsresultaat daalt? Markeer als inconsistentie.
3. Lees op aanwijzingen voor going-concern-twijfel — soms tussen de regels.
4. Bij significante inconsistentie: vraag toelichting aan het bestuur of vermeld dit expliciet in je analyserapport.


> [!example]- Voorbeeld: Bestuursverslag Rotex Roeselare NV stelt: 'onze marges blijven robuust ondanks energieprijsstijgingen'
> Bestuursverslag Rotex Roeselare NV stelt: 'onze marges blijven robuust ondanks energieprijsstijgingen'. Bedrijfsmarge N daalde van 5,7% naar 5,0%.
>
> 1. **Toetsing narratief** 💬
>
>    Daling marge van 5,7% naar 5,0% (= – 70 basispunten) is matig — niet
>    dramatisch maar wel een daling. "Robuust" is verdedigbaar in sectorcontext
>    (concurrenten hadden steilere dalingen). Analyseparagraaf: "narratief
>    klopt mits sectorvergelijking, expliciet vermelden."
>    
>

**Grondslag**: [[getrouw-beeld-jaarrekening]] §getrouw-beeld, vakdoctrine

> [!warning]- Documenteer afwijkingen tussen narratief en cijfers expliciet in je rapport.
>
> _Vaak fout gedaan_: Het bestuursverslag overnemen zonder toetsing aan de cijfers — geeft een vals beeld door aan de gebruiker.
>
> _Grondslag_: [[getrouw-beeld-jaarrekening]] §toelichting-veiligheidsklep

### 5. Integreren van het commissarisverslag

Lees het commissarisverslag op voorbehouden, paragrafen ter benadrukking en kernpunten van de controle.

**Waarom?** Het commissarisverslag is het meest betrouwbare extern-onafhankelijke signaal over de jaarrekening.

**📥 Input**:
- Commissarisverslag → **Oordeel, voorbehouden, going-concern-paragraaf, kernpunten** _(document)_

**📤 Output**:
- Commissaris-bevindingen → **Per element: implicatie voor analyse** _(conclusie)_

**🛠️ Hoe**:

1. Lees het oordeel: goedkeurend zonder voorbehoud, met voorbehoud, onthouding, of afkeurend.
2. Bij een paragraaf "going concern": neem dit altijd over in je analyserapport — kritiek signaal.
3. Lees de "kernpunten van de controle" (key audit matters bij grote vennootschappen): aspecten die de commissaris het hardst toetste.
4. Vergelijk de kernpunten met je eigen aandachtspunten uit competentie [[voorbereiden-financiele-analyse]] stap 4 — overlap bevestigt; niet-overlap = mogelijk gemist aspect aan jouw kant.
5. Documenteer dit naast je eigen analyse.


**Grondslag**: [[commissaris-toezicht-jaarrekening]] §rol-onafhankelijk-oordeel


## Voorbeelden




