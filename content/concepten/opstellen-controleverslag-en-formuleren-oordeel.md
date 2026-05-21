---
title: Opstellen van het controleverslag en formuleren van het oordeel
tags:
- concept
- competentie
- po-1-6
linked_anchors:
- 1.6.taak.1
- 1.6.IV.B
- 1.6.IV.C
- 1.6.IV
programmaonderdelen:
- '1.6'
confidence: inferred
node_type: competentie
status: voorgesteld
schema_version: '1.6'
gegenereerd_uit: data/concepten/records/opstellen-controleverslag-en-formuleren-oordeel.json
gegenereerd_op: '2026-05-21'
---
# Opstellen van het controleverslag en formuleren van het oordeel 🔗

Deze competentie omvat het formuleren van het controleoordeel (kiezen uit de vier types op basis van materialiteit + diepgaandheid + voldoende-en-geschikte assurance-informatie) én het redigeren van het controleverslag conform de ISA-700/705/706/701/720-structuur, aangevuld met Belgische ITAA-vereisten (scope-grenzen, andere prestaties, confraterneel afschrift). De stagiair leert het verslag als communicatie-instrument: paragraaf-volgorde en paragraaf-titels verschillen mee met het oordeels-type.



## Stappen

### 1. Slotsom maken over voldoende geschikt audit-bewijs

Beoordeel of de verzamelde bevindingen een redelijke mate van zekerheid (wettelijke controle) of beperkte mate (review) ondersteunen.

**Waarom?** Het type opdracht bepaalt het zekerheidsniveau; onvoldoende bewijs leidt tot scope-beperking → aangepast oordeel.

**📥 Input**:
- Volledig auditdossier → **Werkpapieren + cijferanalyses + bevestigingen** _(document)_
- Summary of Audit Differences → **Aggregaat ongereinigde afwijkingen** _(boekhoudkundig-bedrag)_

**📤 Output**:
- Werkpapier 'slotsom audit-bewijs' → **Voldoende / beperkt / onvoldoende** _(conclusie)_

**🛠️ Hoe**:

1. Controleer dat per significant risico en per materiële rubriek voldoende geschikt audit-bewijs is verzameld.
2. Identificeer eventuele scope-beperkingen (onmogelijkheid om te bevestigen, ontbrekende documenten).
3. Aggregeer de afwijkingen volgens [[beoordelen-getrouw-beeld-en-regelmatigheid]] §waarachtigheid.
4. Vergelijk met materialiteit + materialiteit voor het oordeel (lager dan algemene materialiteit) — zie [[materieel-belang-audit]] §oordeels-materialiteit.


**Grondslag**: [[assurance-informatie]] §slotsom, ITAA KMO-controlenorm §140

### 2. Type oordeel bepalen via een beslisboom

Pas een gestructureerde beslisboom toe: geen materiële afwijking → goedkeurend; materiële afwijking → voorbehoud / afkeurend / onthouding afhankelijk van pervasiviteit.

**Waarom?** Het oordeelstype is geen vrije keuze maar volgt uit twee dimensies: materialiteit én pervasiviteit (raakt het de jaarrekening als geheel?).

**📥 Input**:
- Slotsom audit-bewijs uit stap 1 → **Voldoende / beperkt / onvoldoende** _(conclusie)_
- Aggregaat afwijkingen + impact → **Bedrag + raakgebied** _(boekhoudkundig-bedrag)_

**📤 Output**:
- Werkpapier 'type oordeel' → **Goedkeurend / voorbehoud / afkeurend / onthouding** _(conclusie)_

**🛠️ Hoe**:

1. Pas de beslisboom uit [[controleoordeel-types]] §beslisboom toe.
2. Geen materiële afwijking + voldoende bewijs → **goedkeurend** (eventueel met paragraaf ter benadrukking).
3. Materiële afwijking, niet-pervasief OF scope-beperking, niet-pervasief → **oordeel met voorbehoud** ('except for').
4. Materiële + pervasieve afwijking → **afkeurend oordeel** ('adverse').
5. Materiële + pervasieve scope-beperking → **onthouding van oordeel** ('disclaimer').


> [!example]- Voorbeeld: Drie scenario-vergelijkingen voor Rotex Roeselare NV
> Drie scenario-vergelijkingen voor Rotex Roeselare NV.
>
> 1. **Beslisboom toegepast** 🌊
>
>    Scenario A: € 50.000 afwijking voorraad, materialiteit € 225.000
>      → niet materieel → goedkeurend, geen paragraaf
>    
>    Scenario B: € 300.000 afwijking voorraad, materialiteit € 225.000, niet-pervasief
>      → materieel + niet-pervasief → **oordeel met voorbehoud**
>      ("Behalve voor het effect van een overschatting van de voorraad
>      ten belope van € 300.000 ...")
>    
>    Scenario C: € 2.000.000 afwijking + structurele continuïteitstwijfel
>      → materieel + pervasief → **afkeurend oordeel**
>    
>
> 2. **Versus onthouding** 💬
>
>    Onthouding ≠ afkeurend. Onthouding bij scope-beperking
>    (kan niet beoordelen). Afkeurend bij gekende afwijking
>    (kan beoordelen en oordeel = negatief).
>    
>

**Grondslag**: [[controleoordeel-types]] §beslisboom, art. 3:75 §1 WVV

> [!warning]- Onderscheid scope-beperking (→ voorbehoud of onthouding) van vaststelling van afwijking (→ voorbehoud of afkeurend).
>
> _Vaak fout gedaan_: Een afkeurend oordeel uitspreken bij onvoldoende informatie; correct is dan een onthouding van oordeel.
>
> _Grondslag_: [[controleoordeel-types]] §scope-versus-afwijking

### 3. Verslag opstellen volgens verplichte structuur

Bouw het verslag op met de wettelijke rubrieken: titel, geadresseerde, oordeel, basis voor het oordeel, sleutelaangelegenheden, verantwoordelijkheden, ondertekening.

**Waarom?** Ontbrekende of foutief geformuleerde rubrieken maken het verslag aanvechtbaar; de structuur is strak gereglementeerd.

**📥 Input**:
- Type oordeel uit stap 2 → **Oordeelstype + redenen** _(conclusie)_
- Sjabloon verslag commissaris uit ITAA-bijlage → **Verplichte rubrieken** _(document)_

**📤 Output**:
- Concept-controleverslag → **Volledig + intern gereviewed** _(document)_

**🛠️ Hoe**:

1. Volg de structuur uit [[controleverslag-elementen]] §verplichte-rubrieken — twee delen voor commissaris: (1) verslag over jaarrekening + (2) verslag over overige door wetgeving gestelde eisen.
2. Schrijf het oordeel als eerste rubriek (post-2016 conventie) — bij aangepast oordeel staat de basis voor het aangepast oordeel onmiddellijk daaronder.
3. Voeg paragrafen toe waar relevant: [[paragraaf-ter-benadrukking]] (going-concern, post-balansdatum-gebeurtenis), [[paragraaf-overige-aangelegenheden]].
4. Vermeld sleutelaangelegenheden (Key Audit Matters) verplicht bij OOB's; aangemoedigd bij andere wettelijke opdrachten.
5. Tweede deel verslag: bestuursverslag-conformiteit, dividend-toelaatbaarheid, conformiteit boekhouding/WVV/statuten, antiwitwas, betalingen aan overheden.


**Grondslag**: [[controleverslag-elementen]] §verplichte-rubrieken, ITAA KMO-controlenorm §141, art. 3:75 §1 WVV

### 4. Verslag laten reviewen, ondertekenen en toezenden

Laat het verslag reviewen door tweede partner / Engagement Quality Reviewer, onderteken het persoonlijk en stuur het naar ITAA + cliënt.

**Waarom?** Persoonlijke ondertekening + vier-ogen-review + tijdige aflevering bij ITAA zijn wettelijke verplichtingen — niet-naleving = tuchtvergrijp.

**📥 Input**:
- Goedgekeurd concept-verslag → **Met alle reviewer-notes 'cleared'** _(document)_

**📤 Output**:
- Ondertekend verslag + bewijs van indiening → **Bij cliënt + ITAA + AV-dossier** _(document)_

**🛠️ Hoe**:

1. Laat het verslag finaal goedkeuren door de Engagement Quality Reviewer (indien aangewezen).
2. Sofie Janssens ondertekent persoonlijk — niet via volmacht. Vermeld haar naam + hoedanigheid + ITAA-nummer + naam Wolters & Partners CVBA.
3. Stuur het verslag binnen 30 dagen na ondertekening naar het ITAA (via online-platform).
4. Bezorg een origineel aan de cliënt, tijdig vóór de algemene vergadering (typisch 15 dagen).


**Grondslag**: [[controleverslag-elementen]] §ondertekening, ITAA KMO-controlenorm §149, Wet ITAA 2019 art. 32

> [!warning]- Persoonlijke handtekening van de aangeduide bedrijfsrevisor is verplicht — niet delegeerbaar.
>
> _Vaak fout gedaan_: Verslag laten ondertekenen door een collega bij afwezigheid; bij wettelijke opdracht is dit nietig.
>
> _Grondslag_: [[wettelijke-controleopdracht-commissaris]] §persoonlijke-ondertekening


## Zie ook

- **Vereist kennis van**: [[controleverslag-elementen]]
- **Vereist kennis van**: [[controleoordeel-types]]
- **Vereist kennis van**: [[aangepast-oordeel]]
- **Vereist kennis van**: [[paragraaf-ter-benadrukking]]
- **Vereist kennis van**: [[paragraaf-overige-aangelegenheden]]
- **Vereist kennis van**: [[materieel-belang-audit]]
- **Vereist kennis van**: [[getrouw-beeld-controle]]
- **Vereist kennis van**: [[wettelijke-controleopdracht-commissaris]]

## Voorbeelden





## Bronnen

[^1]: `ISA-700-herzien__sec_vereisten_2_part3`
[^2]: `ISA-705-herzien__sec_vereisten_2_part3`
[^3]: `ITAA-norm-algemene-controlenorm__sec_2-verslag`
