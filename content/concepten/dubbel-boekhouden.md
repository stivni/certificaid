---
title: Dubbel boekhouden
tags:
- concept
- cluster
- po-1-1
- po-1-2
linked_anchors:
- 1.1.I
- 1.1.I.A
- 1.1.taak.1
- 1.2.III
- 1.2.III.C
programmaonderdelen:
- '1.1'
- '1.2'
confidence: grounded
node_type: cluster
status: seed
schema_version: '1.5'
gegenereerd_uit: data/concepten/records/dubbel-boekhouden.json
gegenereerd_op: '2026-05-18'
---
# Dubbel boekhouden ⚖️

Elke economische verrichting in twee gelijke kanten registreren (debet = credit), zodat de boekhouding op elk moment in balans is en de oorsprong en bestemming van elke euro traceerbaar zijn.

> [!summary] Korte inhoud
> Een boekhoudtechniek waarin elke verrichting wordt geboekt in **minstens twee rekeningen**: een debet- en een creditzijde, voor exact hetzelfde totaalbedrag.

> [!info] Behoort tot: [[regelmatige-boekhouding]]

Een boekhoudtechniek waarin elke verrichting wordt geboekt in **minstens twee rekeningen**: een debet- en een creditzijde, voor exact hetzelfde totaalbedrag. De som van alle debetboekingen is altijd gelijk aan de som van alle creditboekingen. Hierdoor klopt de balans (Activa = Passief) per definitie en zijn rekenfouten meteen detecteerbaar. Voor boekhoudplichtige ondernemingen schrijft WER art. III.84 expliciet voor dat de boekhouding 'wordt gevoerd met inachtneming van de gebruikelijke regels van het dubbel boekhouden'.

_Bron: WER art. III.84_


## Bouwstenen

### Elke boeking heeft twee zijden ⚖️

Een verrichting raakt minstens twee rekeningen: één wordt gedebiteerd, één wordt gecrediteerd. Eén rekening alleen aanpassen kan niet — dat is geen boekhouden meer maar een aantekening.

**Waarom?** Een verrichting heeft altijd een oorsprong (waar komt het geld/de waarde vandaan?) en een bestemming (waar gaat het naartoe?). Beide zijden expliciteren is de essentie.



Klantbetaling van € 4.500 op de rekening van Naaiatelier Ninove BV: Debet 550 Bank € 4.500 / Credit 400 Klanten € 4.500.

_Grondslag: WER art. III.84_

### Som debet = som credit ⚖️

Per boeking is het totaal aan debet gelijk aan het totaal aan credit. Per hele boekhouding ook. Een uit balans staande proefbalans betekent: zoeken naar de fout.

**Waarom?** Deze identiteit is de wiskundige veiligheid: je kunt geen euro doen verschijnen of verdwijnen zonder dat het ergens anders zichtbaar wordt.



Verkoop van een meubel door Meubelzaak Mertens BV voor € 850 (BTW 21%): Debet 400 Klanten € 1.028,50 / Credit 700 Verkopen € 850 + Credit 451 BTW te betalen € 178,50. Debet € 1.028,50 = Credit (€ 850 + € 178,50) ✓.

_Grondslag: WER art. III.84_

### Methodische inschrijving in rekeningen ⚖️

Naast inschrijving in een dagboek (chronologisch) worden de boekingen 'methodisch' overgebracht naar de rekeningen waarop ze betrekking hebben (per onderwerp: klanten, voorraad, kassa, ...).

**Waarom?** Het dagboek geeft het verloop in de tijd; de rekeningen geven het saldo per onderwerp. Beide perspectieven zijn nodig om de balans en de resultatenrekening op te bouwen.



Naaiatelier Ninove BV: alle aankoopboekingen verschijnen chronologisch in het aankoopdagboek (15/3, 22/3, 28/3, ...) en parallel verzameld op rekening 600 Aankopen waar het totaal-saldo afleesbaar is.

_Grondslag: WER art. III.84, lid 1_


## Berekening

### Boekingsregel toepassen

**Boekhoudkundige identiteit** 
```
som van alle debetboekingen = som van alle creditboekingen, en activa = passief op elke balansdatum
```

| Symbool | Betekenis | Eenheid |
|---|---|---|
| `som debet` | Totaal van alle bedragen geboekt aan de debetzijde | EUR |
| `som credit` | Totaal van alle bedragen geboekt aan de creditzijde | EUR |

**Voorbeeld-invulling**: Voor de aankoopboeking van Meubelzaak Mertens: debet (600 + 411) = € 2.500 + € 525; credit (440) = € 3.025

```
€ 3.025 = € 3.025 ✓
```

_Resultaat in EUR_
*Voor elke verrichting bepaal je: welke rekeningen worden geraakt, in welke richting (debet/credit), en voor welk bedrag. Som debet moet gelijk zijn aan som credit.*

### 1. Identificeer de aard van de verrichting

Wat gebeurt er economisch? Aankoop, verkoop, betaling, ontvangst, lening, afschrijving, ...

**Waarom?** De aard bepaalt welke rekeningklassen worden geraakt (klasse 6 kosten, 7 opbrengsten, 4 vorderingen/schulden, 5 financieel, ...).

**📥 Input**:
- Verantwoordingsstuk → **Aard verrichting** _(tekst)_

**📤 Output**:
- Boekingsvoorstel → **Type verrichting** _(categorie)_

**🛠️ Hoe**:

1. Lees het verantwoordingsstuk (factuur, bankuittreksel, overeenkomst).
2. Stel vast: is dit een aankoop, verkoop, betaling, ...?
3. Identificeer eventuele BTW-component.

**Grondslag**: MAR (Minimum Algemeen Rekeningstelsel)

### 2. Kies de rekeningen (debet- en creditzijde)

Wijs voor elke kant van de boeking een specifieke rekening toe uit het rekeningstelsel.

**Waarom?** Het rekeningstelsel structureert de informatie zodat de jaarrekening automatisch uit de boekhouding te halen is.

**📥 Input**:
- Boekingsvoorstel → **Type verrichting** _(categorie)_

**📤 Output**:
- Boekingsvoorstel → **Rekeningen + zijde** _(rekening-set)_

**🛠️ Hoe**:

1. Bestemming/Bron-vraag: wat krijgt de onderneming (debet, activa stijgt of passief daalt)? wat geeft ze op (credit, passief stijgt of activa daalt)?
2. Voor kosten: debet klasse 6.
3. Voor opbrengsten: credit klasse 7.
4. Voor vorderingen klant: debet 400 'Handelsdebiteuren'.
5. Voor schuld leverancier: credit 440 'Leveranciers'.


**Grondslag**: KB 21 oktober 2018 op de jaarrekening; MAR

### 3. Boek de bedragen en controleer som-gelijkheid

Vul de bedragen in en controleer dat de debetzijde gelijk is aan de creditzijde.

**Waarom?** Een out-of-balance boeking wijst op een fout (rekenfout, vergeten BTW-component, of verkeerde rekeningkeuze).

**📥 Input**:
- Boekingsvoorstel → **Rekeningen + zijde** _(rekening-set)_

**📤 Output**:
- Boeking in dagboek → **Volledige boeking** _(boekingsregel)_

**🛠️ Hoe**:

1. Vul de bedragen in op elke rekening (debet of credit).
2. Tel debet-totaal op.
3. Tel credit-totaal op.
4. Indien ongelijk: zoek de fout (vaak: BTW vergeten, of verkeerde percentage).
5. Indien gelijk: boeking valideren, dagboeknummer toekennen.


> [!example]- Voorbeeld: Meubelzaak Mertens BV ontvangt een aankoopfactuur voor € 2.500 hout, BTW 21 % = € 525, totaal € 3.025
> Meubelzaak Mertens BV ontvangt een aankoopfactuur voor € 2.500 hout, BTW 21 % = € 525, totaal € 3.025.
>
> 1. **Aankoopboeking in het aankoopdagboek** 📝
>
>    | Rekening                          | Debet (€) | Credit (€) |
>    |-----------------------------------|----------:|-----------:|
>    | 600 Aankopen handelsgoederen      |  2.500,00 |            |
>    | 411 Terug te vorderen BTW         |    525,00 |            |
>    | 440 Leveranciers                  |           |   3.025,00 |
>    | **Totaal**                        |  **3.025,00** | **3.025,00** |
>
> 2. **Controle som-gelijkheid** 🧮
>
>    Debet  = € 2.500,00 + € 525,00 = **€ 3.025,00**
>    Credit = € 3.025,00                = **€ 3.025,00**
>    Debet = Credit ✓
>

**Grondslag**: WER art. III.84

**Voorbeeld**: Naaiatelier Ninove BV verkoopt op 12 juni een lot kleding aan een grootwarenhuis voor € 12.000 excl. BTW (21 % = € 2.520). Op 30 juni ontvangt zij de betaling van € 14.520 op de bankrekening.

```
Boeking 12/6 (verkoopdagboek): Debet 400 Handelsdebiteuren € 14.520 / Credit 700 Verkopen € 12.000 + Credit 451 BTW te betalen € 2.520. Controle: € 14.520 = € 12.000 + € 2.520 ✓. Boeking 30/6 (financieel dagboek): Debet 550 Bank € 14.520 / Credit 400 Handelsdebiteuren € 14.520.
```

Resultaat: De verkoop is volledig geregistreerd: omzet € 12.000 in de resultatenrekening, BTW-schuld € 2.520 op het passief tot aangifte, bank stijgt met € 14.520 en de vordering op de klant is voldaan.

## In de praktijk

<h3 id="proefbalans-als-controlewerktuig">Proefbalans als controlewerktuig</h3>

> [!tip]- Proefbalans als controlewerktuig
> Op elk moment kan een proefbalans worden opgemaakt: lijst van alle rekeningen met hun debet- en credittotalen. Het verschil moet altijd nul zijn. Bij afwijking: zoek de transcriptie- of berekenfout. 🤖

> [!tip]- Herkennen op het examen
> Examen: 'de proefbalans toont een debet-overschot van € 250 op X-rekening' — wijst op een eenzijdige boeking of telfout.


> [!info]- Niet verwarren met [[vereenvoudigde-boekhouding]]
> Dubbel boekhouden registreert elke verrichting in twee rekeningen (debet/credit) met balans + resultatenrekening als output. Vereenvoudigde boekhouding registreert verrichtingen in drie aparte dagboeken (financieel, aankopen, verkopen) zonder klassieke rekeningenstructuur; toegelaten voor kleine ondernemingen onder de drempelwaarden.
>
> _Trigger_: Examenvraag: kleine eenmanszaak met omzet onder € 500.000 (WER drempel) — mag vereenvoudigd, hoeft geen dubbel boekhouden.


## Valkuilen

> [!warning]- Een enkelvoudige boeking ('ik schrijf € 100 op de bankrekening en klaar') is geen dubbel boekhouden
> ⚠️ Een enkelvoudige boeking ('ik schrijf € 100 op de bankrekening en klaar') is geen dubbel boekhouden. De tegenpost moet expliciet zijn — wat is de andere kant van die € 100? (verkoop? lening? inbreng?). 🤖
>
> _Bron: WER art. III.84 — afgeleid_



## Zie ook

- **Vereist kennis van**: [[dagboek]]

## Voorbeelden

Meubelzaak Mertens BV koopt voor € 1.250 (incl. BTW € 217) hout op factuur. Boeking: Debet 600 Aankopen € 1.033 + Debet 411 Terug te vorderen BTW € 217 / Credit 440 Leveranciers € 1.250. Debet totaal € 1.250 = Credit totaal € 1.250 ✓.

## Bronnen

[^1]: `WER__art_III_71`
[^2]: `CBN-0174-01-beginselen-van-een-regelmatige-boekhouding__sec_regels-die-voor-elke-bedrijfsboekhouding-gelden`
[^3]: `CBN-0174-01-beginselen-van-een-regelmatige-boekhouding__sec_inhoud-van-de-boekingen`
[^4]: `CBN-2019-10-de-boekhoudkundige-en-jaarrekeningrechtelijke-verplichtingen__sec_dubbele-boekhouding-of-vereenvoudigde-boekhouding-optie`
