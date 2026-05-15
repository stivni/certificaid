---
title: Evenredige consolidatie (proportionele consolidatie)
tags:
- concept
- methode
- po-1-4
linked_anchors:
- 1.4.I.D
- 1.4.I.B
- 1.4.II.C
- 1.4.taak.1
programmaonderdelen:
- '1.4'
confidence: grounded
node_type: methode
status: seed
schema_version: '1.2'
gegenereerd_uit: data/concepten/records/evenredige-consolidatie.json
gegenereerd_op: '2026-05-15'
---
# Evenredige consolidatie (proportionele consolidatie) ⚖️

> Een gemeenschappelijke dochteronderneming (een vennootschap waarover een beperkt aantal vennoten gezamenlijke controle uitoefenen via overeenkomst) wordt in de geconsolideerde jaarrekening van elke gezamenlijk controlerende vennoot opgenomen naar rato van haar rechten in het kapitaal (of in de inbreng, voor kapitaalloze vennootschappen). Hiermee wordt enkel het pro-rata deel van de activa, passiva, opbrengsten en kosten meegenomen — zonder afzondering van 'aandeel van derden', want het derden-deel wordt eenvoudigweg niet opgenomen.
>
> _Bron: KB WVV art. 3:124, 2° jo. art. 3:140_


## Bouwstenen

- **Pro-rata opname (KB WVV art. 3:140, b)**: De actief- en passiefbestanddelen, rechten en verplichtingen, opbrengsten en kosten van de gemeenschappelijke dochter worden opgenomen naar rato van de rechten in het kapitaal (resp. in de inbreng) die door de consoliderende vennootschap en haar in de consolidatie opgenomen dochters worden gehouden. ⚖️
- **Toepassing van de integrale-consolidatie-regels op het pro-rata deel (KB WVV art. 3:140, a)**: Op de evenredig geconsolideerde gemeenschappelijke dochter zijn — voor het opgenomen pro-rata deel — de regels van toepassing inzake compensatie van de deelneming (KB WVV art. 3:127, a)), toerekening van het verschil aan onder-/overgewaardeerde activa (KB WVV art. 3:128), bepaling van de waarde op verwervingsdatum (KB WVV art. 3:129), boeking van het consolidatieverschil (KB WVV art. 3:130), afschrijving (KB WVV art. 3:131) en gedeeltelijke realisatie (KB WVV art. 3:132 en art. 3:133). Idem voor de eliminaties (KB WVV art. 3:134, 3:136, 3:138 en art. 3:139) op het pro-rata deel. ⚖️
- **Geen 'aandeel van derden'-post**: Anders dan bij integrale consolidatie kent de evenredige consolidatie geen post 'Belangen van derden' of 'Aandeel van derden in het resultaat' — het deel buiten de groep wordt niet opgenomen, zodat er geen derden-correctie nodig is. 🤖

## Berekening

### Evenredige consolidatie — pro-rata opname

**Formule**: `Geconsolideerde post = (post moeder) + (post gemeenschappelijke dochter × belang%) − intragroep-eliminaties op het pro-rata deel`

*Bij gezamenlijke controle wordt de macht over de dochter gedeeld; de geconsolideerde jaarrekening reflecteert die gedeelde macht door enkel het overeenstemmend deel van activa, passiva, opbrengsten en kosten te tonen. Het deel buiten de groep wordt niet 'gecorrigeerd' via een derden-post (zoals bij integrale consolidatie), maar simpelweg niet opgenomen.*

**Stappen**:

1. Bepaal het belangenpercentage (rechten in kapitaal / inbreng) van de consoliderende vennootschap in de gemeenschappelijke dochter.
2. Vermenigvuldig elke actief-, passief-, opbrengsten- en kostenpost van de dochter met dit percentage.
3. Voeg de pro-rata bedragen samen met de bedragen van de moeder en haar integraal geconsolideerde dochters.
4. Pas de compensatie- en eliminatieregels van KB WVV art. 3:127, 3:128, 3:130, 3:134, 3:136 toe op het pro-rata deel (KB WVV art. 3:140, a)).
**Voorbeeld**: Vennootschap A en vennootschap B oefenen gezamenlijke controle uit over vennootschap X via een aandeelhoudersovereenkomst — elk bezit 50 % van het kapitaal. Balans X: materiële vaste activa 800; voorraden 200; kas 100; eigen vermogen 600; schulden 500. Resultatenrekening X: omzet 1.000; kosten 800; resultaat 200. A koopt voor 60 goederen bij X (intra-groepsverkoop, in voorraad bij A; X realiseerde daarop een winst van 10).

```
Pro-rata deel van A in X = 50 %.
Geconsolideerde activa van X (vóór eliminatie): 50 % × (800 + 200 + 100) = 50 % × 1.100 = 550. Geconsolideerde schulden van X: 50 % × 500 = 250. Geconsolideerd eigen vermogen van X: 50 % × 600 = 300.
Geconsolideerde omzet uit X: 50 % × 1.000 = 500. Geconsolideerde kosten uit X: 50 % × 800 = 400. Geconsolideerd resultaat uit X (vóór eliminatie): 50 % × 200 = 100.
Intra-groepselimatie (KB WVV art. 3:140 jo. art. 3:134, op pro-rata deel): de winst op de intra-groepsverkoop wordt geëlimineerd voor 50 % × 10 = 5 (deel van A in het pro-rata aandeel). Geconsolideerde voorraden A worden met 5 verminderd; geconsolideerd resultaat met 5 verminderd.
```

Resultaat: In de geconsolideerde balans van A worden 550 activa en 250 schulden uit X opgenomen (na eliminatie 545 activa); 100 resultaat van X wordt voor 50 % meegenomen, verminderd met de intra-groepselimatie van 5 → 95. Er is géén post 'Aandeel van derden in resultaat' bij evenredige consolidatie — de overige 50 % van X verschijnt niet in de geconsolideerde jaarrekening van A (B doet dezelfde oefening voor haar 50 %).

## In de praktijk

### Wanneer toepassen {id="wanneer-toepassen"}

Standaard voor gemeenschappelijke dochters bij gezamenlijke controle. Uitzondering: bij gemeenschappelijke dochters die niet nauw geïntegreerd zijn in het bedrijf van de moeder, kan vermogensmutatie worden gebruikt (CBN 2013/3). ⚖️

**Herkenningspunt**: Gezamenlijke controle (overeenkomst, vetorecht) → evenredig.


## Vergelijkingsparen

| Verwarrend met | Verschil | Trigger |
|---|---|---|
| [[integrale-consolidatie]] | Integraal = 100 % opname met afzondering van derden-deel. Evenredig = pro-rata opname (% kapitaaldeelname), geen derden-post. Trigger: type controle (exclusief vs. gezamenlijk). | — |
| [[vermogensmutatiemethode]] | Evenredige consolidatie = activa/passiva regel voor regel pro-rata opgenomen (gedeelde controle). Vermogensmutatie = deelneming als één gesynthetiseerde post (invloed van betekenis, of niet-geïntegreerde gemeenschappelijke dochter). Bij gezamenlijke controle is evenredig de regel, vermogensmutatie de uitzondering. | — |
| [[gezamenlijke-controle]] | Gezamenlijke controle is het triggerend feitencomplex (overeenkomst dat beleidsbeslissingen alleen samen mogen worden genomen — CBN 2017/02), evenredige consolidatie is het boekhoudkundig gevolg dat KB WVV art. 3:124, 2° aan dat feitencomplex koppelt: de gemeenschappelijke dochter wordt naar evenredigheid in de consolidatie opgenomen. Zonder vastgestelde gezamenlijke controle is er geen wettelijke grondslag voor evenredige consolidatie. | — |
| [[gemeenschappelijke-dochteronderneming]] | De gemeenschappelijke dochteronderneming is het juridische object (de vennootschap waarover gezamenlijke controle wordt uitgeoefend door een beperkt aantal vennoten). Evenredige consolidatie is de boekhoudkundige techniek die wordt toegepast om dat object in de geconsolideerde jaarrekening op te nemen — naar rato van de rechten in het kapitaal of in de inbreng (KB WVV art. 3:140, b). Alternatief mag de vermogensmutatiemethode worden gebruikt wanneer het bedrijf van de gemeenschappelijke dochter niet nauw geïntegreerd is in dat van de gezamenlijk controlerende vennootschap. | — |
| [[belangen-van-derden]] | 'Belangen van derden' is een afzonderlijke balans- en resultatenpost die specifiek bij integrale consolidatie ontstaat omdat de actief- en passiefbestanddelen van de dochter voor 100 % worden opgenomen, ook al houdt de moeder geen 100 %. Bij evenredige consolidatie ontstaat geen 'belangen van derden'-post: het deel buiten de groep wordt eenvoudigweg niet opgenomen (KB WVV art. 3:140 verwijst niet naar de derden-bepaling van art. 3:137). Wanneer een examen 'belangen van derden' ziet figureren onder evenredige consolidatie, is dat dus een rode vlag voor een verkeerde methodekeuze. | — |

## Valkuilen

- ⚠️ Het opgenomen pro-rata deel volgt het belangenpercentage (rechten in kapitaal), niet het controlepercentage. Een 50/50 joint venture wordt aldus voor 50 % opgenomen, ook al heeft elke vennoot via de overeenkomst eigenlijk een gelijke beleidsmacht. ⚖️
- ⚠️ Intra-groepsverkopen tussen de moeder en de gemeenschappelijke dochter worden geëlimineerd op het pro-rata deel — niet voor 100 %. Andere bronnen (oudere W.Venn., IFRS 11) kennen andere regels; in WVV-context geldt de pro-rata eliminatie. 🤖

## Bronnen

[^1]: `KB-WVV-2019__art_3_111`
[^2]: `KB-WVV-2019__art_3_110`
[^3]: `CBN-2017-02-gezamenlijke-controle-over-een-vennootschap-groottecriteria-update__sec_algemeen`
[^4]: `CBN-2013-03-de-boekhoudkundige-verwerking-van-step-acquisitions-update__sec_praktische-uitwerking`
[^5]: `KB-WVV-2019__art_3_108`
[^6]: `KB-WVV-2019__art_3_106`
[^7]: `CBN-2017-02-gezamenlijke-controle-over-een-vennootschap-groottecriteria-update__sec_voorbeeld-2`
[^8]: `KB-WVV-2019__art_3_98`
