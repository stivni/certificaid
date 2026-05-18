---
title: Opstellen van het afschrijvingsplan voor materiële vaste activa
tags:
- concept
- competentie
- po-1-1
linked_anchors:
- 1.1.taak.1
- 1.1.II.B
programmaonderdelen:
- '1.1'
confidence: inferred
node_type: competentie
status: voorgesteld
schema_version: '1.5'
gegenereerd_uit: data/concepten/records/opstellen-afschrijvingsplan-vaste-activa.json
gegenereerd_op: '2026-05-18'
---
# Opstellen van het afschrijvingsplan voor materiële vaste activa 🤖


## Stappen

### 1. Bepaal de aanschaffingswaarde

Bereken de basis waarover wordt afgeschreven door alle bijkomende kosten van verwerving op te tellen.

**Waarom?** Een correcte basis is voorwaarde voor een correct afschrijvingsplan; bijkomende kosten worden niet vergeten en niet dubbel geboekt.

**📥 Input**:
- Aankoopfactuur + bijkomende facturen → **Aankoopprijs, transport, installatie, opstartkosten** _(document)_

**📤 Output**:
- Werkblad aanschaffingswaarde → **Som componenten + datum ingebruikneming** _(berekening)_

**🛠️ Hoe**:

1. Som de componenten volgens [[aanschaffingswaarde]] §componenten: aankoopprijs excl. btw + transport + installatie + niet-aftrekbare btw + andere kosten direct toerekenbaar tot ingebruikneming.
2. Trek af: kortingen, premies, investeringssteun (eventueel als overlopende rekening).
3. Bij Transport Tongeren BV — vrachtwagen MAN: aankoopprijs € 95.000 + douaneformaliteiten € 800 + opbouw laadbak € 7.500 + niet-aftrekbare btw 50% op personenautokost (n.v.t. vrachtwagen) = € 103.300.
4. Documenteer datum van ingebruikneming — afschrijving start vanaf die datum, niet vanaf aankoopdatum.


**Grondslag**: [[aanschaffingswaarde]] §componenten, KB-WVV art. 3:14

### 2. Bepaal economische levensduur en restwaarde

Schat hoe lang het activum economisch bruikbaar is en wat de waarde aan einde levensduur zal zijn.

**Waarom?** Levensduur bepaalt de periodes; restwaarde wordt afgetrokken van de basis om over-afschrijving te vermijden.

**📥 Input**:
- Sectorgegevens + technische specificaties → **Gangbare levensduur, terugkoopwaarde** _(berekening)_

**📤 Output**:
- Werknotitie → **Levensduur + restwaarde + motivering** _(conclusie)_

**🛠️ Hoe**:

1. Bepaal economische levensduur (kan korter zijn dan technische): voor gebouwen 33 jaar (3%), voor vrachtwagens 5 jaar (20%), voor IT-uitrusting 3-5 jaar, voor productiemachines 7-10 jaar — zie sectorgangbare normen.
2. Bepaal restwaarde — bij vrachtwagens vaak 10-20% van aanschaffingswaarde (tweedehandsmarkt); bij IT-uitrusting vaak € 0.
3. Voor Transport Tongeren BV — vrachtwagen 5 jaar levensduur, restwaarde € 10.000 (geschat tweedehandsverkoop).
4. Documenteer in waarderingsregels (KB-WVV art. 3:6).


**Grondslag**: [[afschrijvingen]] §levensduur, [[waarderingsregels-jaarrekening]] §vastlegging

> [!warning]- Houd rekening met restwaarde wanneer ze materieel is — voor vrachtwagens vaak 10-20% — anders schrijf je teveel af.
>
> _Vaak fout gedaan_: Restwaarde op € 0 zetten "voor de eenvoud", terwijl de tweedehandsmarkt een duidelijke prijs geeft.
>
> _Grondslag_: [[afschrijvingen]] §restwaarde

### 3. Kies afschrijvingsmethode (lineair of degressief)

Bepaal of de afschrijving even verdeeld of versneld in het begin moet worden.

**Waarom?** De methode beïnvloedt de jaarlijkse kost en het fiscale resultaat; ze moet aansluiten bij het werkelijk gebruikspatroon.

**📥 Input**:
- Werknotitie stap 1+2 → **Aanschaffingswaarde, levensduur, restwaarde** _(berekening)_

**📤 Output**:
- Methode-keuze + parameters → **Lineair of degressief + jaarlijks percentage** _(conclusie)_

**🛠️ Hoe**:

1. Toets de methodes uit [[afschrijvingen]] §methoden: lineair (constante dotatie) of degressief (versnelde dotatie eerste jaren).
2. Lineair: dotatie = (aanschaffingswaarde - restwaarde) / aantal jaren.
3. Degressief: dotatie = boekwaarde × degressief percentage; fiscaal max. tweemaal het lineair percentage; degressieve dotatie mag in geen geval lager zijn dan lineaire dotatie (dan terug naar lineair).
4. Voor Transport Tongeren BV — vrachtwagen 5 jaar: lineair 20% of degressief 40%. Bestuur kiest degressief omdat onderhoudskosten + brandstofverbruik in latere jaren stijgen → matching met opbrengsten.
5. Voor immateriële vaste activa zoals software: alleen lineair toegelaten (KB-WVV art. 3:42 §3).


**Grondslag**: [[afschrijvingen]] §methoden, KB-WVV art. 3:13

### 4. Bouw de afschrijvingstabel en boek jaarlijks

Stel een tabel op met dotatie, gecumuleerde afschrijving en netto-boekwaarde per boekjaar; boek op balansdatum.

**Waarom?** De tabel maakt de afschrijving voorspelbaar, ondersteunt de jaarrekening-toelichting en is bewijsstuk bij controle.

**📥 Input**:
- Methode-keuze stap 3 → **Parameters** _(berekening)_

**📤 Output**:
- Afschrijvingstabel + jaarlijkse boeking → **Multi-jaar overzicht + journaalpost** _(boekingsregel)_

**🛠️ Hoe**:

1. Bouw tabel: jaar | beginsaldo | dotatie | gecumuleerde afschrijving | netto-boekwaarde.
2. Bij ingebruikneming in de loop van het boekjaar — pro rata vanaf maand van ingebruikneming (bv. ingebruikneming 01/07 = 6/12 van jaarlijkse dotatie). Praktijk varieert (sommigen volledig jaar, sommigen pro rata) — leg vast in waarderingsregels.
3. Boek elke balansdatum: Debet 6302 Afschrijving materiële vaste activa; Credit 22X9 Gecumuleerde afschrijvingen (X is rubriek: 220 terreinen, 221 gebouwen, 230 installaties, 240 meubilair, 241 rollend materieel).
4. Bij verkoop of buitendienststelling — meerwaarde via 763, minderwaarde via 663 (zie [[niet-recurrente-verrichtingen]]).


> [!example]- Voorbeeld: Transport Tongeren BV koopt op 01/07/2026 een vrachtwagen MAN — aanschaffingswaarde € 103.300, restwaarde € 10.000, line…
> Transport Tongeren BV koopt op 01/07/2026 een vrachtwagen MAN — aanschaffingswaarde € 103.300, restwaarde € 10.000, lineair over 5 jaar. Basis af te schrijven: € 93.300.
>
> 1. **Afschrijvingstabel** 🧮
>
>    | Boekjaar | Beginsaldo (NBW) | Dotatie | Gecumuleerde afschrijving | NBW eind |
>    |---|---|---|---|---|
>    | 2026 | € 103.300 | € 9.330 (6/12) | € 9.330 | € 93.970 |
>    | 2027 | € 93.970 | € 18.660 | € 27.990 | € 75.310 |
>    | 2028 | € 75.310 | € 18.660 | € 46.650 | € 56.650 |
>    | 2029 | € 56.650 | € 18.660 | € 65.310 | € 37.990 |
>    | 2030 | € 37.990 | € 18.660 | € 83.970 | € 19.330 |
>    | 2031 | € 19.330 | € 9.330 (6/12) | € 93.300 | € 10.000 |
>    
>
> 2. **Jaarlijkse boeking eindejaar 2026** 📝
>
>    | Datum | Rekening | Omschrijving | Debet | Credit |
>    |---|---|---|---|---|
>    | 31/12/2026 | 6302 Afschrijving mat. vaste activa | dotatie vrachtwagen MAN (6 mnd) | € 9.330,00 | |
>    | 31/12/2026 | 2419 Gecumuleerde afschrijvingen rollend materieel | -- | | € 9.330,00 |
>    
>

**Grondslag**: [[afschrijvingen]] §dotatie, [[materiele-vaste-activa]] §boeking

### 5. Herzie het plan bij wijzigde gebruiksomstandigheden

Pas het afschrijvingsplan aan indien levensduur, restwaarde of gebruikspatroon materieel wijzigen.

**Waarom?** Een verouderd plan geeft geen getrouw beeld; wijzigingen moeten toekomstgericht doorwerken — verleden niet retroactief aanpassen.

**📥 Input**:
- Aanwijzing wijzigde omstandigheden → **Sneller verouderen, nieuwe technologie, gewijzigd gebruik** _(document)_

**📤 Output**:
- Herzien plan + toelichting → **Nieuwe parameters vanaf wijzigingsdatum** _(berekening)_

**🛠️ Hoe**:

1. Identificeer of wijziging materieel is (>10% impact op resultaat is gebruikelijke drempel).
2. Pas plan PROSPECTIEF aan — restwaarde van netto-boekwaarde uitsmeren over resterende levensduur (zie CBN 2017/16).
3. Indien de waardevermindering tot onder economische gebruikswaarde gaat: boek aanvullende waardevermindering — zie [[waardeverminderingen]] §vaste-activa.
4. Documenteer wijziging in toelichting bij jaarrekening + werkdocument met motivering.


**Grondslag**: [[afschrijvingen]] §planherziening, [[waardeverminderingen]] §vaste-activa, CBN 2017/16


