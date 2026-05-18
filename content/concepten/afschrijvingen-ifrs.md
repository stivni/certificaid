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
confidence: inferred
node_type: cluster
status: seed
schema_version: '1.5'
gegenereerd_uit: data/concepten/records/afschrijvingen-ifrs.json
gegenereerd_op: '2026-05-18'
---
# Afschrijvingen onder IFRS (IAS 16 + IAS 38) 🤖

> [!update] Bijgewerkt sinds `b2f4a4ad` — laatste wijziging 2026-05-18


Onder IFRS is afschrijving (IAS 16 alinea 6, IAS 38 alinea 8) de **stelselmatige toerekening van het afschrijfbaar bedrag** van een actief **over zijn gebruiksduur**. Het afschrijfbaar bedrag = kostprijs (of geherwaardeerde waarde) − **restwaarde**. De gebruikte methode moet 'een afspiegeling zijn van het patroon volgens welk de toekomstige economische voordelen van het actief naar verwachting zullen worden verbruikt' (IAS 16 alinea 60). Drie veelvoorkomende methoden: lineair, degressief, en op basis van verbruikte werkeenheden. De entiteit moet **jaarlijks** restwaarde, gebruiksduur en afschrijvingsmethode herzien (alinea 51 + 61); aanpassingen zijn schattingswijzigingen (IAS 8, prospectief). Een methode op basis van **opbrengsten** is voor materiële vaste activa NIET toegestaan (alinea 62A) — opbrengsten weerspiegelen prijs en volume, niet het verbruik van het actief.

> [!info] Behoort tot: [[materiele-vaste-activa-ifrs]] · Specialisatie van: [[afschrijvingen]]


## Bouwstenen

### Restwaarde — vaak nul, maar niet altijd ⚖️

De restwaarde is het bedrag dat de entiteit naar verwachting **vandaag** zou ontvangen bij vervreemding van een actief in de staat aan het eind van zijn gebruiksduur. In de praktijk is restwaarde vaak nihil (machines die volledig verbruikt zijn, software die obsoleet is). Maar voor activa met blijvende intrinsieke waarde (voertuigen, vastgoed-component 'gebouw') kan ze materieel zijn.

**Waarom?** Het afschrijfbaar bedrag = kostprijs − restwaarde. Een te lage restwaarde overschat de afschrijving; een te hoge restwaarde onderschat de afschrijving. Restwaarde moet realistisch zijn op basis van vandaag (alinea 53).



Zelena Bio NV koopt een vrachtwagen voor € 85.000, geschatte restwaarde bij 8 jaar gebruik = € 12.500 (verwachte verkoopprijs van vergelijkbare 8-jarige vrachtwagens vandaag). Afschrijfbaar bedrag = € 72.500. Lineair: € 9.063/jaar.

_Grondslag: IAS 16 alinea 6, 53_

### Start- en einddatum afschrijving ⚖️

Afschrijving **begint** wanneer het actief gereed is voor gebruik — d.w.z. op de locatie en in de staat is om te functioneren zoals door management beoogd. **Eindigt** op de vroegste van: classificatie als 'aangehouden voor verkoop' (IFRS 5), of niet langer opnemen (vervreemding, buitengebruikstelling) (alinea 55).

**Waarom?** Niet de aankoopdatum maar de gebruiksklare datum is bepalend. Een nieuwe productielijn die nog 4 maanden ingericht moet worden levert pas vanaf maand 5 economische voordelen — afschrijving begint dan ook pas op maand 5.



Zelena Bio's productielijn: aankoopfactuur 15 oktober 2025, installatie + tests afgerond 31 januari 2026. Afschrijving start op 1 februari 2026; voor boekjaar 2026 wordt 11/12 van de jaarafschrijving geboekt.

_Grondslag: IAS 16 alinea 55_

### Drie methoden — kies volgens verbruikspatroon ⚖️

**Lineair**: gelijk bedrag per periode (typisch voor gebouwen, kantoorinrichting). **Degressief**: dalend bedrag per periode (typisch voor voertuigen die in eerste jaren meer waarde verliezen). **Op basis van verbruikte werkeenheden**: per uitgevoerde productie-eenheid of werkuur (typisch voor mijnen, drukmachines). De entiteit kiest de methode die het verbruikspatroon van toekomstige economische voordelen het beste weerspiegelt.

**Waarom?** Een uniforme methode voor alle activa zou de afschrijving van werkelijkheid loskoppelen. De keuze hangt af van de aard van het actief en hoe het zijn waarde verliest.



Zelena Bio: productie-installatie (constante output) → lineair; vrachtwagen (snelle waardevermindering eerste jaren) → degressief; gietvorm voor productie van 500.000 doseflesjes → op basis van werkeenheden (€ 0,80 per geproduceerd flesje, kostprijs gietvorm € 400.000).

_Grondslag: IAS 16 alinea 60-62_

### Verbod op opbrengstenmethode ⚖️

Een afschrijvingsmethode op basis van **opbrengsten gegenereerd door de activiteit waarbij het actief wordt gebruikt** is voor materiële vaste activa **niet passend** (IAS 16 alinea 62A). Opbrengsten weerspiegelen veel factoren naast verbruik (prijs, volume, inflatie, marketing). Voor immateriële activa geldt een **weerlegbaar vermoeden** dat dezelfde methode niet passend is (IAS 38 alinea 98A). Het vermoeden kan in **twee beperkte gevallen** worden weerlegd: (a) wanneer het immaterieel actief is uitgedrukt als een **opbrengstenmaatstaf** (typisch contract met opbrengsten-cap, alinea 98C) — bv. een concessie 'tot € 2.000.000.000 cumulatieve goudverkoop'; of (b) wanneer kan worden aangetoond dat opbrengsten en het verbruik van economische voordelen **sterk gecorreleerd** zijn.

**Waarom?** Een entiteit die afschrijft op basis van omzet zou bij hoge omzet veel afschrijven (geeft optisch lage marge) en bij lage omzet weinig afschrijven (optisch hogere marge). Dat maakt resultaten manipuleerbaar en koppelt afschrijving los van werkelijk verbruik.



Zelena Bio mag NIET haar productielijn afschrijven op basis van '€ 0,02 per euro verkochte productieopbrengst'. Wel: per geproduceerd doseflesje (output-eenheden) of lineair over jaren.
Zelena Bio NV verwerft een **concessie** voor de winning van zeldzame celcultuur uit een bioreactor; het contract loopt tot € 12.000.000 cumulatieve opbrengsten zijn gerealiseerd. Het immaterieel actief is uitgedrukt als opbrengstenmaatstaf — IAS 38 alinea 98C laat hier wél een opbrengstengebaseerde afschrijving toe. Bij € 1.500.000 jaaromzet uit de concessie: afschrijving = 1.500.000/12.000.000 × kostprijs concessie.

_Grondslag: IAS 16 alinea 62A; IAS 38 alinea 98A + 98C_

### Onbepaalde gebruiksduur immateriële activa — geen afschrijving ⚖️

Onder IAS 38 wordt een immaterieel actief met **onbepaalde gebruiksduur** NIET afgeschreven (alinea 107). In plaats daarvan: jaarlijkse impairment-test onder IAS 36. Voorwaarde: er is geen voorzienbare beperking op de periode waarin het actief toekomstige economische voordelen genereert.

**Waarom?** Afschrijven over 'onbepaald' is conceptueel onmogelijk. De impairment-test waarborgt dat een verminderde economische realiteit wel zichtbaar wordt op het juiste moment.



Zelena Bio's productlicentie zonder vervaldatum (kostprijs € 4.500.000): geen afschrijving. Elke 31 december: impairment-test onder IAS 36 — vergelijk boekwaarde met realiseerbare waarde.

_Grondslag: IAS 38 alinea 107-108_

### Immateriële activa — default lineair bij onbetrouwbaar patroon ⚖️

Voor een immaterieel actief met beperkte gebruiksduur moet de afschrijvingsmethode het verwachte verbruikspatroon van toekomstige economische voordelen weergeven. **Kan dat patroon niet betrouwbaar worden bepaald, dan is de lineaire methode verplicht** (IAS 38 alinea 97). Dat is een belangrijk verschil met IAS 16: voor materiële vaste activa schrijft IAS 16 alinea 60 geen default-methode voor wanneer het patroon onzeker is.

**Waarom?** Voor immateriële activa is het verbruikspatroon vaak moeilijker objectief vast te stellen dan bij fysieke activa. Een dwingende default voorkomt willekeurige methodekeuzes en bevordert vergelijkbaarheid tussen entiteiten.



Zelena Bio koopt een softwarelicentie van € 240.000 met een gebruiksduur van 6 jaar. Het management kan niet betrouwbaar inschatten of het verbruik gelijkmatig of degressief verloopt — IAS 38 alinea 97 verplicht dan lineair: € 240.000 / 6 = € 40.000 per jaar.

_Grondslag: IAS 38 alinea 97_

### Restwaarde immateriële activa — verondersteld nul ⚖️

Voor een immaterieel vast actief met beperkte gebruiksduur wordt **de restwaarde verondersteld nul te zijn** (IAS 38 alinea 100), tenzij: (a) een derde zich ertoe verbonden heeft het actief aan het eind van zijn gebruiksduur aan te kopen; of (b) er een actieve markt is voor het actief én de restwaarde kan op die markt worden bepaald én het is waarschijnlijk dat die markt zal bestaan aan het einde van de gebruiksduur. Voor materiële vaste activa onder IAS 16 geldt geen vergelijkbaar default-vermoeden — daar moet de restwaarde steeds expliciet worden geschat (alinea 53).

**Waarom?** Voor de meeste immateriële activa (software, octrooien, ontwikkelingskosten) bestaat geen tweedehandsmarkt en is een verkoopbeding aan het eind van de gebruiksduur uitzonderlijk. Een default-nul vermijdt willekeurige inschattingen en houdt de afschrijfbare basis robuust.



Zelena Bio's intern ontwikkelde productiesoftware (geactiveerd voor € 720.000, gebruiksduur 6 jaar): geen verkoopovereenkomst, geen actieve markt → restwaarde = € 0. Afschrijfbaar bedrag = € 720.000; lineair = € 120.000/jaar.

_Grondslag: IAS 38 alinea 100_


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



## Zie ook

- **Wordt voorondersteld in** (1): [[materiele-vaste-activa-ifrs]]
## Bronnen

[^1]: `IAS-16-materiele-vaste-activa__sec_waardering-na-eerste-opname`
[^2]: `IAS-16-materiele-vaste-activa__sec_62a`
[^3]: `IAS-38-immateriele-activa__sec_gebruiksduur`
[^4]: `IAS-38-immateriele-activa__sec_immateri-le-activa-met-een-beperkte-gebruiksduur`
