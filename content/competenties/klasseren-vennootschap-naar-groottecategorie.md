---
title: Klasseren van een vennootschap als micro, klein of groot volgens de groottecriteria
tags:
- competentie
- po-1-2
programmaonderdelen:
- '1.2'
status: voorgesteld
schema_version: '1.1'
gegenereerd_uit: data/concepten/competenties/klasseren-vennootschap-naar-groottecategorie.yaml
gegenereerd_op: '2026-05-16'
---
# Klasseren van een vennootschap als micro, klein of groot volgens de groottecriteria

**⚖️ 95% · 🤖 5%**

> De criteria, drempels, lock-in-regel en verbondenheidsregel staan letterlijk in WVV art. 1:24-1:25 en in CBN-advies 2022/03. Praktijkoordeel beperkt zich tot het correct berekenen van de jaargemiddelde personeelsbezetting en de omzet op alternatieve basis bij omzetschommelingen.

## Aanbevolen werkwijze

### 1. Verzamel de drie criteria-waarden op balansdatum

Bereken jaargemiddelde personeelsbezetting, jaaromzet excl. BTW en balanstotaal van het afgesloten boekjaar.

**Waarom?** Zonder de drie cijfers is geen toets mogelijk.

**📥 Input**:
- Loonadministratie en sociale balans → **Jaargemiddelde personeel (VTE)** _(getal)_
- Resultatenrekening + BTW-aangiftes → **Jaaromzet excl. BTW (rubriek 70)** _(boekhoudkundig-bedrag)_
- Voorlopige balans → **Balanstotaal (totaal activa)** _(boekhoudkundig-bedrag)_

**📤 Output**:
- Toets-werkblad → **Drie cijfers + boekjaar-eind** _(berekening)_

**🛠️ Hoe**:

1. Lees de jaargemiddelde personeelsbezetting uit de sociale balans (totaal uurtellingen ÷ normuren, in VTE).
2. Lees de jaaromzet excl. BTW uit rubriek 70 van de resultatenrekening van Meubelzaak Mertens BV.
3. Lees het balanstotaal uit het voorlopige balans-totaal van de activa-zijde.
4. Bij verbonden vennootschappen: bereken de cijfers op geconsolideerde of geaggregeerde basis — zie stap 3.


**Grondslag**: [[groottecriteria-jaarrekening]] §criteria, WVV art. 1:24 § 1

### 2. Toets aan de drie drempels voor 'kleine vennootschap'

Vergelijk de drie cijfers met de WVV-drempels en pas de regel 'maximaal één criterium overschreden' toe.

**Waarom?** Slechts één criterium mag worden overschreden; twee of drie maken de vennootschap groot.

**📥 Input**:
- Toets-werkblad stap 1 → **Drie cijfers** _(berekening)_

**📤 Output**:
- Tussenstand → **Klein OF (potentieel) groot** _(conclusie)_

**🛠️ Hoe**:

1. Lees de actuele drempels uit [[groottecriteria-jaarrekening]] §drempels (cijferzakboekje): personeel ≤ 50, omzet ≤ € 11.250.000, balanstotaal ≤ € 6.000.000.
2. Tel het aantal overschreden criteria.
3. Eén overschrijding (of geen) → klein. Twee of drie → potentieel groot, maar eerst stap 4 (lock-in).


> [!example]- Voorbeeld: Meubelzaak Mertens BV op 31/12/2024: 12 werknemers (VTE), € 4.500.000 omzet, € 2.100.000 balanstotaal
> Meubelzaak Mertens BV op 31/12/2024: 12 werknemers (VTE), € 4.500.000 omzet, € 2.100.000 balanstotaal.
>
> 1. **Toets per criterium** 🧮
>
>    | Criterium | Waarde Mertens | Drempel klein | Overschreden? |
>    |---|---:|---:|:---|
>    | Personeel (VTE) | 12 | 50 | Nee |
>    | Omzet excl. BTW | € 4.500.000 | € 11.250.000 | Nee |
>    | Balanstotaal | € 2.100.000 | € 6.000.000 | Nee |
>    
>
> 2. **Tussenstand** 💬
>
>    Geen enkele drempel overschreden → klein. Ga door naar microtoets (stap 3).
>    
>

**Grondslag**: [[kleine-vennootschap]] §criteria, [[groottecriteria-jaarrekening]] §drempels

### 3. Toets aan de micro-drempels en bijkomende voorwaarde

Als de vennootschap klein is, ga na of ze ook microvennootschap is.

**Waarom?** Een micro-vennootschap mag het microschema gebruiken — kleinste schema met laagste rapporteringslast.

**📥 Input**:
- Tussenstand stap 2 → **Klein OF (potentieel) groot** _(conclusie)_
- Aandeelhoudersregister + KBO van eventuele deelnemingen → **Bestaat moeder- of dochter-relatie?** _(document)_

**📤 Output**:
- Werknotitie → **Micro / klein / groot** _(conclusie)_

**🛠️ Hoe**:

1. Was de vennootschap in stap 2 al groot? → micro-toets niet relevant; stop hier.
2. Lees de strengere micro-drempels uit [[microvennootschap]] §drempels: personeel ≤ 10, omzet ≤ € 900.000, balanstotaal ≤ € 450.000.
3. Tel ook hier maximum één overschrijding toelaten.
4. Kruistoets: is de vennootschap moeder of dochter? Zo ja → géén micro, maximaal klein ([[microvennootschap]] §bijkomende-voorwaarde).
5. Beide voorwaarden vervuld → micro. Anders → klein.


> [!example]- Voorbeeld: Oprichtingen Oostende BV in jaar 1: 4 werknemers, € 400.000 omzet, € 380.000 balanstotaal, geen deelnemingen
> Oprichtingen Oostende BV in jaar 1: 4 werknemers, € 400.000 omzet, € 380.000 balanstotaal, geen deelnemingen.
>
> 1. **Toets micro-drempels** 🧮
>
>    | Criterium | Waarde Oostende | Drempel micro | Overschreden? |
>    |---|---:|---:|:---|
>    | Personeel | 4 | 10 | Nee |
>    | Omzet | € 400.000 | € 900.000 | Nee |
>    | Balanstotaal | € 380.000 | € 450.000 | Nee |
>    
>
> 2. **Bijkomende voorwaarde** 💬
>
>    Geen moeder, geen dochter → bijkomende voorwaarde vervuld.
>    → Microvennootschap.
>    
>

**Grondslag**: [[microvennootschap]] §criteria, WVV art. 1:25

> [!warning]- Een dochter in een groep is nooit microvennootschap, ook al blijft ze onder de drempels.
>
> _Vaak fout gedaan_: Een 100%-dochter van Aurelia Holding NV als micro aanmerken op grond van haar lage cijfers.
>
> _Grondslag_: [[microvennootschap]] §bijkomende-voorwaarde

### 4. Pas de lock-in-regel en de verbondenheidsregel toe

Toets of de overschrijding twee opeenvolgende boekjaren standhoudt en of verbonden vennootschappen meegerekend moeten worden.

**Waarom?** Eénmalig overschrijden kantelt de status niet; een 'kleine' dochter van een grote groep wordt voor de jaarrekening als groot behandeld.

**📥 Input**:
- Tussenstand stap 2 of 3 → **Status van het huidige jaar** _(conclusie)_
- Cijfers vorig boekjaar + groepsstructuur → **Drie criteria + lijst verbonden vennootschappen** _(berekening)_

**📤 Output**:
- Definitieve grootteklasse → **Micro / klein / groot** _(conclusie)_

**🛠️ Hoe**:

1. Als de overschrijding nieuw is in het huidige jaar: kijk naar het vorige boekjaar. Twee jaar overschrijding op rij? → grootteklasse kantelt vanaf het volgende boekjaar (zie [[groottecriteria-jaarrekening]] §lock-in).
2. Maakt de vennootschap deel uit van een groep? Bereken de drie criteria op geconsolideerde of geaggregeerde basis (som van de groepscijfers) — zie [[groottecriteria-jaarrekening]] §verbondenheid.
3. Als de groep groot is, wordt de individuele vennootschap voor jaarrekening behandeld als groot, zelfs als ze op zich klein is.
4. Documenteer de definitieve grootteklasse in het dossier.


> [!example]- Voorbeeld: Naaiatelier Ninove BV is op zich klein (€ 3M omzet, 25 werknemers, € 2M balans), maar dochter van Aurelia Holding NV
> Naaiatelier Ninove BV is op zich klein (€ 3M omzet, 25 werknemers, € 2M balans), maar dochter van Aurelia Holding NV. De Aurelia-groep heeft samen 280 werknemers en € 60M omzet.
>
> 1. **Verbondenheidstoets** 🧮
>
>    | Niveau | Personeel | Omzet | Balans | Status |
>    |---|---:|---:|---:|:---|
>    | Naaiatelier individueel | 25 | € 3M | € 2M | klein |
>    | Aurelia-groep | 280 | € 60M | € 22M | groot |
>    
>
> 2. **Conclusie** 💬
>
>    Naaiatelier behoort tot een grote groep → voor jaarrekening behandeld als groot
>    → volledig schema, jaarverslag, mogelijk commissaris (afhankelijk van eigen toets).
>    
>

**Grondslag**: [[groottecriteria-jaarrekening]] §lock-in, [[groottecriteria-jaarrekening]] §verbondenheid

> [!warning]- Pas de lock-in-regel toe vóór je een schemawissel adviseert.
>
> _Vaak fout gedaan_: Een vennootschap onmiddellijk van klein naar groot kantelen na één jaar overschrijding.
>
> _Grondslag_: [[groottecriteria-jaarrekening]] §lock-in


## Voorbeelden

> [!example]- Oprichtingen Oostende BV in haar eerste boekjaar: 4 werknemers, € 400.000 omzet, € 380.000 balanstotaal, geen deelneming…
> **Conclusie**: Microvennootschap — onder alle micro-drempels, geen moeder/dochter.
>
> **Grondslag**: [[microvennootschap]] §criteria
>
> **Redenering**: Drie criteria onder de micro-drempels + bijkomende voorwaarde vervuld. Mag microschema gebruiken vanaf eerste jaarrekening.

> [!example]- Rotex Roeselare NV: 550 werknemers, € 95.000.000 omzet, € 42.000.000 balanstotaal
> **Conclusie**: Grote vennootschap — alle drie criteria ver boven kleine-drempels.
>
> **Grondslag**: [[groottecriteria-jaarrekening]] §drempels
>
> **Redenering**: Geen twijfel — drie van de drie overschreden. Verplicht: volledig schema, jaarverslag, commissaris.

> [!example]- Brugse Brouwerij BV: 55 werknemers (te hoog), € 4M omzet (OK), € 3M balanstotaal (OK)
> **Conclusie**: Klein — slechts één criterium overschreden, dus 'max één overschrijding' is gerespecteerd.
>
> **Grondslag**: [[groottecriteria-jaarrekening]] §één-criterium-regel
>
> **Redenering**: De regel is geen som; één overschrijding is toegelaten. Brugse blijft klein, mag verkort schema.


## Gebaseerd op concepten

[[groottecriteria-jaarrekening]] · [[kleine-vennootschap]] · [[microvennootschap]] · [[vennootschapsvormen-typologie]]
## Voortkomend uit

- **Kenniselementen**: 1.2.IV.B, 1.2.IV
