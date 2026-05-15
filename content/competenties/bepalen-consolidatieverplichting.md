---
title: Bepalen of een vennootschap een geconsolideerde jaarrekening moet opstellen
tags:
- competentie
- po-1-4
programmaonderdelen:
- '1.4'
status: voorgesteld
schema_version: '1.0'
gegenereerd_uit: data/concepten/competenties/bepalen-consolidatieverplichting.yaml
gegenereerd_op: '2026-05-15'
---
# Bepalen of een vennootschap een geconsolideerde jaarrekening moet opstellen

**⚖️ 90% · 🤖 10%** · Status: `voorgesteld`

> De plicht volgt rechtstreeks uit WVV art. 3:22 e.v. en de vrijstellingen uit WVV art. 1:26 en KB WVV; enkel de feitelijke beoordeling van controle in feite en de toetsing aan groottecriteria vergen oordeel.

## Aanbevolen werkwijze

### 1. Vaststellen of de entiteit rechtspersoonlijkheid heeft en als vennootschap kwalificeert

📥 **Input**: Statuten en juridische vorm van de potentieel consoliderende entiteit
📤 **Output**: Bevestiging dat de entiteit een vennootschap met rechtspersoonlijkheid is (geen natuurlijke persoon, geen maatschap zonder rechtspersoonlijkheid)
**Waarom**: Alleen vennootschappen met rechtspersoonlijkheid kunnen moedervennootschap zijn en consolidatieplichtig worden.
**Grondslag**: [[consolidatieverplichting]]
- ⚠️ **Een natuurlijke persoon met meerderheidsstemrechten in meerdere vennootschappen is zelf consolidatieplichtig.** → De natuurlijke persoon is geen moedervennootschap; meestal ontstaat een consortium en rust de plicht op de gezamenlijke leden. ([[consolidatieverplichting]])
- ⚠️ **Een maatschap zonder rechtspersoonlijkheid kan moedervennootschap zijn.** → Zonder rechtspersoonlijkheid kan de maatschap geen moedervennootschap zijn; de onderliggende vennootschappen moeten zelf consolideren tenzij ze als consortium kwalificeren. ([[consolidatieverplichting]])
### 2. Vaststellen of er controle bestaat over één of meer dochterondernemingen

📥 **Input**: Aandelenstructuur, statuten, aandeelhoudersovereenkomsten, samenstelling bestuursorgaan en historiek van algemene vergaderingen
📤 **Output**: Conclusie of controle (in rechte of in feite, exclusief of gezamenlijk) bestaat op balansdatum
**Waarom**: Zonder controle is de entiteit geen moedervennootschap en bestaat geen consolidatieplicht.
**Grondslag**: [[controle]]
- ⚠️ **Controle vereist altijd meer dan 50 % van de stemrechten.** → Controle in feite kan ook met minder dan 50 % bestaan (bv. wanneer de vennootschap op twee opeenvolgende AV's de meerderheid van bestuurders heeft aangesteld met haar effectieve stemrechten). ([[controle]])
### 3. Onderzoeken of er sprake is van een consortium (horizontale groep)

📥 **Input**: Vaststelling of er één rechtspersoon is die de andere(n) controleert dan wel of meerdere vennootschappen onder centrale leiding staan zonder onderlinge moeder-dochter-relatie
📤 **Output**: Conclusie: verticale groep met één moeder (stap 4) of horizontale groep / consortium (consolidatieplicht rust gezamenlijk bij de leden)
**Waarom**: Bij een consortium ontbreekt een moedervennootschap en moet de consolidatieplicht via WVV art. 3:24 op de leden samen gelegd worden.
**Grondslag**: [[consortium]]
### 4. Toetsen of de vrijstelling 'groep van beperkte omvang' van toepassing is

📥 **Input**: Geconsolideerde of geaggregeerde cijfers (jaaromzet, balanstotaal, jaargemiddelde werknemers) van de groep
📤 **Output**: Conclusie: overschrijdt de groep meer dan één van de drempels van WVV art. 1:26, § 1, dan vervalt deze vrijstelling
**Waarom**: Een moedervennootschap in een groep die op geconsolideerde of geaggregeerde basis niet meer dan één criterium overschrijdt, is in beginsel vrijgesteld.
**Grondslag**: [[groep-van-beperkte-omvang]]
- ⚠️ **Berekening 'op geconsolideerde basis' betekent dat er al een geconsolideerde jaarrekening moet bestaan.** → Het is enkel een berekeningswijze om de vrijstellingsdrempels te toetsen — geen verplichting tot effectieve consolidatie. ([[groottecriteria-consolidatie]])
### 5. Toetsen of de vrijstelling van subconsolidatie van toepassing is

📥 **Input**: Identiteit en consolidatiestatus van de hogere moedervennootschap; lijst van consortium-leden en dochters; notering op gereglementeerde markt
📤 **Output**: Conclusie of de submoeder is vrijgesteld omdat een hogere moeder al een gelijkwaardige geconsolideerde jaarrekening opstelt, laat controleren en openbaar maakt, en geen lid van haar consolidatiekring beursgenoteerd is
**Waarom**: Subconsolidatie wordt vermeden wanneer hogerop al een geconsolideerde jaarrekening wordt opgemaakt; bij notering vervalt de vrijstelling.
**Grondslag**: [[vrijstelling-subconsolidatie]]
- ⚠️ **De vrijstelling geldt ongeacht of een dochter in de subconsolidatiekring genoteerd is.** → Zodra de submoeder of één van haar dochters genoteerd is op een gereglementeerde markt, vervalt de vrijstelling van subconsolidatie. ([[vrijstelling-subconsolidatie]])
### 6. Formuleren van de eindconclusie

📥 **Input**: Resultaten van stappen 1-5
📤 **Output**: Eén van: (a) niet consolidatieplichtig (geen rechtspersoon, geen controle, beperkte omvang of subconsolidatie-vrijstelling); (b) consolidatieplichtig als moedervennootschap; (c) consolidatieplichtig samen met andere consortiumleden
**Waarom**: Een ondubbelzinnig antwoord op de cliëntvraag is het eindproduct van deze competentie.
**Grondslag**: 🤖 Beroepspraktijk — Synthese van de voorgaande wettelijke toetsen — vergt geen aparte regel.

## Beslisboom

**Heeft de entiteit rechtspersoonlijkheid en is zij een vennootschap?**
- Ja: Ga naar volgende vraag.
- Nee: Geen consolidatieplicht — meestal consortium of geen plicht.

**Bestaat controle (in rechte of in feite) over één of meer dochterondernemingen?**
- Ja: Ga naar volgende vraag (verticale moeder).
- Nee: Onderzoek of er een consortium is. Zo niet: geen consolidatieplicht.

**Overschrijdt de groep meer dan één van de groottecriteria (WVV art. 1:26, § 1) op geconsolideerde of geaggregeerde basis?**
- Ja: Vrijstelling 'groep van beperkte omvang' vervalt; ga naar volgende vraag.
- Nee: Vrijgesteld als groep van beperkte omvang (tenzij notering op gereglementeerde markt).

**Bestaat hogerop een moedervennootschap die al een gelijkwaardige geconsolideerde jaarrekening opstelt, laat controleren en openbaar maakt, en is geen lid van de subconsolidatiekring beursgenoteerd?**
- Ja: Vrijstelling van subconsolidatie van toepassing — geen plicht voor de submoeder.
- Nee: Consolidatieplichtig.


## Voorbeelden

**Situatie**: Vennootschap M bezit 90 % van de stemrechten van dochter D; D oefent een industriële activiteit uit; M heeft via haar stemrechten de bevoegdheid om de meerderheid van bestuurders aan te stellen.

**Conclusie**: M is consolidatieplichtig: zij is een moedervennootschap met exclusieve controle in rechte over D.

**Grondslag**: [[moedervennootschap]] §controlebevoegdheid; [[exclusieve-controle]] §onweerlegbaar vermoeden

**Redenering**: De stemrechtenmeerderheid (> 50 %) levert het onweerlegbaar vermoeden van controle in rechte op; M is moedervennootschap en moet D integraal opnemen, tenzij een vrijstelling van toepassing is.

---
**Situatie**: Een natuurlijke persoon bezit meerderheidsstemrechten in twee zustervennootschappen Y en Z die samen onder centrale leiding staan; er bestaat geen moeder-dochter-relatie tussen Y en Z.

**Conclusie**: Geen consolidatieplicht voor de natuurlijke persoon; Y en Z vormen vermoedelijk een consortium en zijn samen consolidatieplichtig.

**Grondslag**: [[consolidatieverplichting]] §natuurlijke personen; [[consortium]] §horizontale groep

**Redenering**: Een natuurlijke persoon kan geen moedervennootschap zijn. Bij centrale leiding zonder onderlinge controle ontstaat een consortium; WVV art. 3:24 legt de plicht op de leden samen.

---

## Gebaseerd op concepten

[[consolidatieverplichting]] · [[moedervennootschap]] · [[controle]] · [[consortium]] · [[vrijstelling-subconsolidatie]] · [[groottecriteria-consolidatie]] · [[groep-van-beperkte-omvang]] · 
## Voortkomend uit

- **Taken**: 1.4.taak.1
- **Kenniselementen**: 1.4.I.C, 1.4.I.B, 1.4.II.B
