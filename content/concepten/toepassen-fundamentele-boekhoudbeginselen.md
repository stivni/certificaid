---
title: Toepassen van de fundamentele boekhoudbeginselen op een concrete verrichting
tags:
- concept
- competentie
- po-1-1
linked_anchors:
- 1.1.taak.1
- 1.1.I.B
programmaonderdelen:
- '1.1'
confidence: inferred
node_type: competentie
status: voorgesteld
schema_version: '1.6'
gegenereerd_uit: data/concepten/records/toepassen-fundamentele-boekhoudbeginselen.json
gegenereerd_op: '2026-05-21'
---
# Toepassen van de fundamentele boekhoudbeginselen op een concrete verrichting 🔗

De competentie die de losse beginselen (regelmatigheid, voorzichtigheid, getrouw beeld, continuïteit, onveranderlijkheid, matching) verbindt tot één **professioneel oordeel** over een concrete verrichting. Voor een stagiair-GA: typisch examenscenario waarbij meerdere beginselen tegelijk getoetst worden en de juiste hiërarchie + uitkomst moet worden onderbouwd.



## Stappen

### 1. Beschrijf het voorgelegde boekingsfeit

Vat de verrichting samen in een feiten-zin met datum, bedragen en partijen.

**Waarom?** Beginselen krijgen pas grip als duidelijk is wat de bestuurder of accountant moet boeken.

**📥 Input**:
- Cliëntdossier → **Beschrijving van de verrichting** _(document)_

**📤 Output**:
- Werknotitie → **Feiten + tijdstip** _(conclusie)_

**🛠️ Hoe**:

1. Lees de cliëntsituatie. Voorbeeld: Naaiatelier Ninove BV ontvangt op 27/12/2026 een dagvaarding voor schade aan een leveringsmachine — schade-claim € 22.000.
2. Bepaal het tijdstip: vóór, op of na balansdatum?
3. Noteer de partijen en bedragen.
4. Bewaar als startpunt voor stap 2-4.


**Grondslag**: [[regelmatige-boekhouding]] §boekingsbeginsel

### 2. Toets aan het continuïteitsbeginsel

Stel vast of de onderneming als going concern verder bestaat — dat bepaalt of de standaardwaardering nog geldt.

**Waarom?** Bij wegvallen van continuïteit verandert het volledige waarderingsregime (liquidatiewaarde) — alle latere stappen werken anders.

**📥 Input**:
- Werknotitie stap 1 → **Feiten** _(conclusie)_
- Balans + financieringsplan → **Eigen vermogen, liquide middelen, lopende verliezen** _(balans)_

**📤 Output**:
- Continuïteits-conclusie → **Going concern Ja/Nee + onderbouwing** _(conclusie)_

**🛠️ Hoe**:

1. Toets de drie indicatoren uit [[continuiteitsbeginsel]] §indicatoren: blijvende verliezen, ontoereikende eigen middelen, gebrek aan financiering.
2. Bij Naaiatelier Ninove BV: ondanks de schade-claim blijven omzet en eigen middelen positief → going concern blijft gelden.
3. Bij wegvallen continuïteit (zie Verffabriek Veurne BV in vereffening): overschakelen op liquidatiewaardering — vaste activa tegen realisatiewaarde, voorzieningen voor opzegvergoedingen.
4. Documenteer in werknotitie.


**Grondslag**: [[continuiteitsbeginsel]] §toets, KB-WVV art. 3:6

### 3. Pas het voorzichtigheidsbeginsel toe op kosten en opbrengsten

Boek waarschijnlijke kosten/verliezen vóór balansdatum; boek opbrengsten pas wanneer zeker.

**Waarom?** Asymmetrische behandeling van risico's beschermt schuldeisers en geeft een prudent beeld van het resultaat.

**📥 Input**:
- Continuïteits-conclusie stap 2 → **Going concern Ja/Nee** _(conclusie)_

**📤 Output**:
- Boekingsvoorstel + redenering → **Voorziening, waardevermindering of geen actie** _(boekingsregel)_

**🛠️ Hoe**:

1. Identificeer kosten/verliezen die wáárschijnlijk zijn op balansdatum — zie [[voorzichtigheidsbeginsel]] §regel.
2. Bij Naaiatelier Ninove BV: schade-claim € 22.000 met juridisch advies "waarschijnlijke veroordeling" → voorziening boeken (rubriek 163).
3. Identificeer opbrengsten — boek alleen wat reeds gerealiseerd of contractueel zeker is.
4. Bij Solaris Sint-Truiden BV: niet-gerealiseerde meerwaarde op aandelen (€ 5.000 koerstoename) → NIET boeken (voorzichtigheid weegt boven oprechtheid bij ongerealiseerde winst).
5. Documenteer de keuze met bedrag en grondslag.


> [!example]- Voorbeeld: Naaiatelier Ninove BV, balansdatum 31/12/2026
> Naaiatelier Ninove BV, balansdatum 31/12/2026. Schade-claim € 22.000 met advies advocaat 'veroordeling waarschijnlijk' + ongerealiseerde meerwaarde € 5.000 op effecten.
>
> 1. **Voorziening voor schade-claim** 📝
>
>    | Datum | Rekening | Omschrijving | Debet | Credit |
>    |---|---|---|---|---|
>    | 31/12/2026 | 6370 Voorzieningen — toevoeging | dotatie | € 22.000 | |
>    | 31/12/2026 | 163 Andere voorzieningen voor risico's | claim Ninove | | € 22.000 |
>    
>
> 2. **Behandeling ongerealiseerde meerwaarde** 💬
>
>    Geen boeking. Voorzichtigheidsbeginsel verbiedt het boeken van niet-gerealiseerde winsten.
>    Bij verkoop in 2027 → meerwaarde dan boeken op rubriek 751.
>    
>

**Grondslag**: [[voorzichtigheidsbeginsel]] §regel, KB-WVV art. 3:11

> [!warning]- Voorzichtigheid geldt asymmetrisch — verliezen ja vóór realisatie, winsten nee tot na realisatie.
>
> _Vaak fout gedaan_: Niet-gerealiseerde meerwaarden meteen als opbrengst boeken om winst te verbeteren.
>
> _Grondslag_: [[voorzichtigheidsbeginsel]] §asymmetrie

### 4. Verifieer aan getrouw beeld + onveranderlijkheid

Toets of de boeking samen met de toelichting een getrouw beeld geeft, en verzeker dat eerder geboekte stukken niet worden uitgewist.

**Waarom?** De jaarrekening moet "een getrouw beeld" geven (KB-WVV art. 3:1) — dat is de overkoepelende toets. Onveranderlijkheid waarborgt de bewijsfunctie.

**📥 Input**:
- Boekingsvoorstel stap 3 → **Voorgestelde boeking** _(boekingsregel)_

**📤 Output**:
- Definitieve boeking + correctieboeking-regel → **Doorgevoerde journaalpost + toelichting** _(boekingsregel)_

**🛠️ Hoe**:

1. Toets aan [[getrouw-beeld]] §toets: geeft het samenspel van balans, resultatenrekening en toelichting een getrouw beeld?
2. Indien strikte regeltoepassing geen getrouw beeld geeft → afwijken én motiveren in de toelichting (KB-WVV art. 3:1 §3).
3. Onveranderlijkheid: indien een eerdere boeking foutief blijkt, NOOIT doorhalen of overschrijven — boek een correctieboeking met datum en verwijzing. Zie [[onveranderlijkheid-boekingen]] §correctie.
4. Bij materiële fout in een afgesloten boekjaar: vermeld in de toelichting bij de eerstvolgende jaarrekening (CBN 2014/01).
5. Documenteer de afwijking of correctie in cliëntdossier.


**Grondslag**: [[getrouw-beeld]] §toets, [[onveranderlijkheid-boekingen]] §correctie, KB-WVV art. 3:1


## Voorbeelden





