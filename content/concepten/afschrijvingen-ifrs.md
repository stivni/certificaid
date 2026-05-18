---
title: Afschrijvingen onder IFRS (IAS 16 + IAS 38)
tags:
- concept
- cluster
- po-1-5
linked_anchors:
- 1.5.V.B
- 1.5.V
programmaonderdelen:
- '1.5'
confidence: grounded
node_type: cluster
status: seed
schema_version: '1.5'
gegenereerd_uit: data/concepten/records/afschrijvingen-ifrs.json
gegenereerd_op: '2026-05-18'
---
# Afschrijvingen onder IFRS (IAS 16 + IAS 38) ⚖️

> [!summary] Korte inhoud
> Onder IFRS is afschrijving (IAS 16 alinea 6, IAS 38 alinea 8) de **stelselmatige toerekening van het afschrijfbaar bedrag** van een actief **over zijn gebruiksduur**.

> [!info] Behoort tot: [[materiele-vaste-activa-ifrs]]

Onder IFRS is afschrijving (IAS 16 alinea 6, IAS 38 alinea 8) de **stelselmatige toerekening van het afschrijfbaar bedrag** van een actief **over zijn gebruiksduur**. Het afschrijfbaar bedrag = kostprijs (of geherwaardeerde waarde) − **restwaarde**. De gebruikte methode moet 'een afspiegeling zijn van het patroon volgens welk de toekomstige economische voordelen van het actief naar verwachting zullen worden verbruikt' (IAS 16 alinea 60). Drie veelvoorkomende methoden: lineair, degressief, en op basis van verbruikte werkeenheden. De entiteit moet **jaarlijks** restwaarde, gebruiksduur en afschrijvingsmethode herzien (alinea 51 + 61); aanpassingen zijn schattingswijzigingen (IAS 8, prospectief). Een methode op basis van **opbrengsten** is voor materiële vaste activa NIET toegestaan (alinea 62A) — opbrengsten weerspiegelen prijs en volume, niet het verbruik van het actief.

_Bron: IAS 16 alinea 6, 50-62_


## Bouwstenen

### Restwaarde — vaak nul, maar niet altijd ⚖️

De restwaarde is het bedrag dat de entiteit naar verwachting **vandaag** zou ontvangen bij vervreemding van een actief in de staat aan het eind van zijn gebruiksduur. In de praktijk is restwaarde vaak nihil (machines die volledig verbruikt zijn, software die obsoleet is). Maar voor activa met blijvende intrinsieke waarde (voertuigen, vastgoed-component 'gebouw') kan ze materieel zijn.

**Waarom?** Het afschrijfbaar bedrag = kostprijs − restwaarde. Een te lage restwaarde overschat de afschrijving; een te hoge restwaarde onderschat de afschrijving. Restwaarde moet realistisch zijn op basis van vandaag (alinea 53).

**Voorbeeld**: Zelena Bio NV koopt een vrachtwagen voor € 85.000, geschatte restwaarde bij 8 jaar gebruik = € 12.500 (verwachte verkoopprijs van vergelijkbare 8-jarige vrachtwagens vandaag). Afschrijfbaar bedrag = € 72.500. Lineair: € 9.063/jaar.

_Grondslag: IAS 16 alinea 6, 53_

### Start- en einddatum afschrijving ⚖️

Afschrijving **begint** wanneer het actief gereed is voor gebruik — d.w.z. op de locatie en in de staat is om te functioneren zoals door management beoogd. **Eindigt** op de vroegste van: classificatie als 'aangehouden voor verkoop' (IFRS 5), of niet langer opnemen (vervreemding, buitengebruikstelling) (alinea 55).

**Waarom?** Niet de aankoopdatum maar de gebruiksklare datum is bepalend. Een nieuwe productielijn die nog 4 maanden ingericht moet worden levert pas vanaf maand 5 economische voordelen — afschrijving begint dan ook pas op maand 5.

**Voorbeeld**: Zelena Bio's productielijn: aankoopfactuur 15 oktober 2025, installatie + tests afgerond 31 januari 2026. Afschrijving start op 1 februari 2026; voor boekjaar 2026 wordt 11/12 van de jaarafschrijving geboekt.

_Grondslag: IAS 16 alinea 55_

### Drie methoden — kies volgens verbruikspatroon ⚖️

**Lineair**: gelijk bedrag per periode (typisch voor gebouwen, kantoorinrichting). **Degressief**: dalend bedrag per periode (typisch voor voertuigen die in eerste jaren meer waarde verliezen). **Op basis van verbruikte werkeenheden**: per uitgevoerde productie-eenheid of werkuur (typisch voor mijnen, drukmachines). De entiteit kiest de methode die het verbruikspatroon van toekomstige economische voordelen het beste weerspiegelt.

**Waarom?** Een uniforme methode voor alle activa zou de afschrijving van werkelijkheid loskoppelen. De keuze hangt af van de aard van het actief en hoe het zijn waarde verliest.

**Voorbeeld**: Zelena Bio: productie-installatie (constante output) → lineair; vrachtwagen (snelle waardevermindering eerste jaren) → degressief; gietvorm voor productie van 500.000 doseflesjes → op basis van werkeenheden (€ 0,80 per geproduceerd flesje, kostprijs gietvorm € 400.000).

_Grondslag: IAS 16 alinea 60-62_

### Verbod op opbrengstenmethode ⚖️

Een afschrijvingsmethode op basis van **opbrengsten gegenereerd door de activiteit waarbij het actief wordt gebruikt** is voor materiële vaste activa **niet passend** (alinea 62A). Opbrengsten weerspiegelen veel factoren naast verbruik (prijs, volume, inflatie, marketing). Voor immateriële activa is dezelfde regel met een (zeer beperkte) uitzondering bij IAS 38 alinea 98A.

**Waarom?** Een entiteit die afschrijft op basis van omzet zou bij hoge omzet veel afschrijven (geeft optisch lage marge) en bij lage omzet weinig afschrijven (optisch hogere marge). Dat maakt resultaten manipuleerbaar en koppelt afschrijving los van werkelijk verbruik.

**Voorbeeld**: Zelena Bio mag NIET haar productielijn afschrijven op basis van '€ 0,02 per euro verkochte productieopbrengst'. Wel: per geproduceerd doseflesje (output-eenheden) of lineair over jaren.

_Grondslag: IAS 16 alinea 62A_

### Onbepaalde gebruiksduur immateriële activa — geen afschrijving ⚖️

Onder IAS 38 wordt een immaterieel actief met **onbepaalde gebruiksduur** NIET afgeschreven (alinea 107). In plaats daarvan: jaarlijkse impairment-test onder IAS 36. Voorwaarde: er is geen voorzienbare beperking op de periode waarin het actief toekomstige economische voordelen genereert.

**Waarom?** Afschrijven over 'onbepaald' is conceptueel onmogelijk. De impairment-test waarborgt dat een verminderde economische realiteit wel zichtbaar wordt op het juiste moment.

**Voorbeeld**: Zelena Bio's productlicentie zonder vervaldatum (kostprijs € 4.500.000): geen afschrijving. Elke 31 december: impairment-test onder IAS 36 — vergelijk boekwaarde met realiseerbare waarde.

_Grondslag: IAS 38 alinea 107-108_


## Berekening

### Lineaire afschrijving

**Jaarlijkse lineaire afschrijving** 
```
jaarafschrijving = (kostprijs − restwaarde) / gebruiksduur in jaren
```

| Symbool | Betekenis | Eenheid |
|---|---|---|
| `kostprijs` | Kostprijs of geherwaardeerde waarde van het actief | EUR |
| `restwaarde` | Geschatte opbrengst bij vervreemding aan einde gebruiksduur (vandaag) | EUR |
| `gebruiksduur in jaren` | Periode waarin actief economisch nuttig is voor entiteit | jaar |

**Voorbeeld-invulling**: Zelena Bio vrachtwagen: kostprijs = € 85.000, restwaarde = € 12.500, gebruiksduur = 8 jaar

```
(€ 85.000 − € 12.500) / 8 = € 9.063 per jaar
```

_Resultaat in EUR_
### Afschrijving op basis van verbruikte werkeenheden

**Afschrijving per eenheid** 
```
afschrijving per eenheid = (kostprijs − restwaarde) / totale verwachte werkeenheden
```

| Symbool | Betekenis | Eenheid |
|---|---|---|
| `kostprijs` | Kostprijs van actief | EUR |
| `restwaarde` | Restwaarde aan einde gebruik | EUR |
| `totale verwachte werkeenheden` | Totaal aantal productie-eenheden, draaiuren, ton, ... over leven | eenheden |

**Voorbeeld-invulling**: Zelena Bio gietvorm: kostprijs = € 400.000, restwaarde = € 0, totale verwachte productie = 500.000 doseflesjes

```
(€ 400.000 − € 0) / 500.000 = € 0,80 per flesje. Bij jaarproductie 120.000 flesjes: € 96.000 afschrijving
```

_Resultaat in EUR_

## Valkuilen

> [!warning]- Restwaarde, gebruiksduur en afschrijvingsmethode worden **prospectief** aangepast bij wijziging (IAS 8)
> ⚠️ Restwaarde, gebruiksduur en afschrijvingsmethode worden **prospectief** aangepast bij wijziging (IAS 8). Geen retroactieve aanpassing van voorgaande boekjaren — alleen aanpassing van resterende afschrijfbaar bedrag over resterende gebruiksduur. ⚖️
>
> _Bron: IAS 16 alinea 51 + 61, verwijzing IAS 8_


> [!warning]- Terreinen worden NIET afgeschreven (alinea 58)
> ⚠️ Terreinen worden NIET afgeschreven (alinea 58). Bij aankoop van vastgoed: kostprijs splitsen in 'grond' (geen afschrijving) en 'gebouw' (wel afschrijving). Stagiairs vergeten deze splitsing. ⚖️
>
> _Bron: IAS 16 alinea 58_


> [!warning]- Een actief blijft afschrijven zolang het volledig afschrijfbaar bedrag niet bereikt is, ook als de reële waarde hoger is dan de boekwaarde (…
> ⚠️ Een actief blijft afschrijven zolang het volledig afschrijfbaar bedrag niet bereikt is, ook als de reële waarde hoger is dan de boekwaarde (alinea 52). Reële waarde stopt geen afschrijving — alleen de restwaarde doet dat indirect. ⚖️
>
> _Bron: IAS 16 alinea 52_



## Bronnen

[^1]: `IAS-16-materiele-vaste-activa__sec_waardering-na-eerste-opname`
[^2]: `IAS-16-materiele-vaste-activa__sec_62a`
[^3]: `IAS-38-immateriele-activa__sec_gebruiksduur`
