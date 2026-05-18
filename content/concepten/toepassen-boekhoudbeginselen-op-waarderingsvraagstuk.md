---
title: Toepassen van de boekhoudbeginselen op een concreet waarderingsvraagstuk
tags:
- concept
- competentie
- po-1-2
linked_anchors:
- 1.2.taak.1
- 1.2.V
- 1.2.V.A
- 1.2.V.B
programmaonderdelen:
- '1.2'
confidence: inferred
node_type: competentie
status: voorgesteld
schema_version: '1.5'
gegenereerd_uit: data/concepten/records/toepassen-boekhoudbeginselen-op-waarderingsvraagstuk.json
gegenereerd_op: '2026-05-18'
---
# Toepassen van de boekhoudbeginselen op een concreet waarderingsvraagstuk 🤖


## Stappen

### 1. Identificeer het waarderingsvraagstuk

Beschrijf wat moet worden gewaardeerd of geboekt en op welk moment.

**Waarom?** Beginselen zijn pas operationeel zodra duidelijk is welk concreet vraagstuk men aanpakt.

**📥 Input**:
- Boekhoudverrichting of balanspost → **Korte beschrijving, bedrag, datum, partijen** _(document)_

**📤 Output**:
- Werknotitie → **Vraagstuk + balansdatum + waardering-keuzes** _(conclusie)_

**🛠️ Hoe**:

1. Lees de cliëntsituatie. Voorbeeld bij Meubelzaak Mertens BV: er hangt een lopende klantvordering van € 18.000 die volgens de bestuurder wellicht oninbaar wordt.
2. Bepaal het waarderingsobject: actief (welke balansrubriek?), passief (voorziening, schuld?), of een resultaat-element.
3. Bepaal het waarderingsmoment: op balansdatum, op verrichtingsdatum, of bij overdracht.
4. Noteer de keuze-alternatieven (bv. waardevermindering boeken of niet, voorziening boeken of niet).


**Grondslag**: [[waarderingsregels-jaarrekening]] §toepassingsgebied

### 2. Loop de boekhoudbeginselen systematisch af

Test elk beginsel op het waarderingsvraagstuk en formuleer wat het beginsel concreet voorschrijft.

**Waarom?** Beginselen kunnen tegen elkaar inwerken; pas door ze één voor één te toetsen weet je welke keuze juist is.

**📥 Input**:
- Werknotitie stap 1 → **Waarderingsvraagstuk** _(conclusie)_

**📤 Output**:
- Beginselen-tabel → **Per beginsel een gevolg + grondslag** _(berekening)_

**🛠️ Hoe**:

1. [[continuiteitsbeginsel]]: kan de onderneming verder? Zo nee → liquidatiewaardering, ander regime.
2. [[voorzichtigheidsbeginsel]]: opbrengsten pas boeken als zeker, kosten en risico's al boeken als waarschijnlijk. Welke waardering levert de meest voorzichtige uitkomst?
3. [[volledigheidsbeginsel]]: zijn alle relevante verrichtingen en rechten/verplichtingen opgenomen, ook buiten balans?
4. [[oprechtheidsbeginsel]]: weerspiegelt de boeking de werkelijke economische realiteit? Geen vorm boven inhoud, geen window-dressing.
5. [[consistentiebeginsel]]: pas dezelfde regel toe als vorig boekjaar, of motiveer en kwantificeer een wijziging.
6. Vul de beginselen-tabel met per beginsel een korte conclusie.


> [!example]- Voorbeeld: Meubelzaak Mertens BV heeft een vordering € 18.000 op cliënt X die sinds 9 maanden niet betaalt
> Meubelzaak Mertens BV heeft een vordering € 18.000 op cliënt X die sinds 9 maanden niet betaalt. Bestuurder schat 60% kans op definitief verlies.
>
> 1. **Toets per beginsel** 💬
>
>    | Beginsel | Toepassing op vordering Mertens |
>    |---|---|
>    | Continuïteit | Mertens BV is going concern → vordering blijft op activa-zijde, geen liquidatie-discount. |
>    | Voorzichtigheid | Waardevermindering boeken voor het waarschijnlijke verlies — 60% × € 18.000 = € 10.800. |
>    | Volledigheid | Indien de cliënt al een vonnis tegen zich heeft: ook eventuele aanmaningskosten en gerechtskosten boeken. |
>    | Oprechtheid | Niet wachten met boekingen tot na balansdatum om winstcijfer op te smukken. |
>    | Consistentie | Toepassen dezelfde grens als vorig jaar (bv. 9 maanden + risico-oordeel) of nieuwe regel motiveren. |
>    
>

**Grondslag**: [[aanvullende-boekhoudbeginselen]] §systematische-toepassing

### 3. Verifieer aan de getrouw-beeld-eis

Toets of de keuze die volgt uit de beginselen samen een getrouw beeld geeft.

**Waarom?** Indien strikte regeltoepassing geen getrouw beeld oplevert, moet afgeweken worden (en in de toelichting verantwoord).

**📥 Input**:
- Beginselen-tabel stap 2 → **Beginselen-conclusies** _(berekening)_

**📤 Output**:
- Gevolgschema → **Boeking + toelichting + eventuele afwijking** _(document)_

**🛠️ Hoe**:

1. Geeft de strikte regeltoepassing volgens stap 2 een getrouw beeld van het vermogen, de financiële positie en het resultaat? Zie [[getrouw-beeld-jaarrekening]] §toets.
2. Bij overeenstemming: voer de boeking uit volgens stap 2.
3. Bij onvoldoende getrouw beeld: pas KB-WVV art. 3:32 § 3 toe — wijk af van de standaardregel en motiveer in de toelichting.
4. Documenteer beslissing en grondslag.


**Grondslag**: [[getrouw-beeld-jaarrekening]] §toets, KB-WVV art. 3:32 § 3

> [!warning]- Een afwijking van een waarderingsregel is enkel toegelaten wanneer strikte toepassing geen getrouw beeld geeft — niet om resultaten te sturen.
>
> _Vaak fout gedaan_: De afwijkingsbepaling gebruiken om vrij te kiezen tussen alternatieve waarderingen.
>
> _Grondslag_: [[getrouw-beeld-jaarrekening]] §uitzondering

### 4. Boek en documenteer met grondslag-verwijzing

Voer de boeking uit en leg in een werkdocument vast welk beginsel doorslaggevend was.

**Waarom?** Bij latere controle (commissaris, fiscale audit) moet de redenering reproduceerbaar zijn.

**📥 Input**:
- Gevolgschema stap 3 → **Boekingsregel + toelichtingstekst** _(document)_

**📤 Output**:
- Boekhouddossier → **Boeking + werkdocument** _(document)_

**🛠️ Hoe**:

1. Boek de verrichting (bv. waardevermindering op handelsvorderingen):
   Debet 6340 Waardeverminderingen op handelsvorderingen — € 10.800
   Credit 4071 Waardeverminderingen op handelsvorderingen (correctief) — € 10.800
2. Voeg een toelichting-paragraaf toe over de toegepaste waarderingsregel.
3. Bewaar in cliëntdossier de motivering met grondslag-verwijzing naar het concept en het wetsartikel.


**Grondslag**: [[waarderingsregels-jaarrekening]] §documentatie (praktijk-discipline)


