---
title: Sale-and-leaseback onder IFRS (IFRS 16)
tags:
- concept
- cluster
- po-1-5
linked_anchors:
- 1.5.V.C
- 1.5.V
programmaonderdelen:
- '1.5'
confidence: grounded
node_type: cluster
status: seed
schema_version: '1.5'
gegenereerd_uit: data/concepten/records/sale-and-leaseback-ifrs.json
gegenereerd_op: '2026-05-18'
---
# Sale-and-leaseback onder IFRS (IFRS 16) ⚖️

> [!summary] Korte inhoud
> Een **sale-and-leaseback** (verkoop-en-terugleasing) is een samengestelde transactie waarbij één onderneming (de **verkoper-lessee**) een actief verkoopt aan een andere onderneming (de **koper-lessor**) en datzelfde actief onmiddellijk van de koper terugleaset (alinea 98).

> [!info] Behoort tot: [[leasing-ifrs]]

Een **sale-and-leaseback** (verkoop-en-terugleasing) is een samengestelde transactie waarbij één onderneming (de **verkoper-lessee**) een actief verkoopt aan een andere onderneming (de **koper-lessor**) en datzelfde actief onmiddellijk van de koper terugleaset (alinea 98). Economisch is het een financieringstechniek: de verkoper-lessee genereert liquiditeit door eigendom over te dragen, maar blijft het actief gebruiken via een lease. IFRS 16 verwerkt het in twee stappen: eerst beoordelen of de overdracht überhaupt **een verkoop is volgens IFRS 15-criteria** (alinea 99 — vooral het 'zeggenschap'-criterium), en dan op basis daarvan kiezen tussen twee verwerkingspaden. Onder BE-GAAP geldt artikel 63 KB W.Venn.: de meerwaarde uit de overdracht wordt **uitgesteld** via een overlopende rekening en jaarlijks in resultaat genomen naar verhouding van de afschrijving van het geleasde goed — de transactie wordt economisch als één geheel beschouwd.

_Bron: IFRS 16 alinea 98-103_


## Bouwstenen

### Tweestappentest — eerst is het een verkoop? ⚖️

IFRS 16 dwingt de entiteit eerst de IFRS 15-toets toe te passen (alinea 99): is de zeggenschap over het actief daadwerkelijk overgegaan naar de koper-lessor? Indicatoren uit IFRS 15: overdracht van wettelijke eigendom, fysieke bezit, risico's en voordelen, klant-aanvaarding, recht op betaling. Pas na een 'ja' op deze toets volgt de boekhoudkundige verwerking van een echte verkoop + leaseback (alinea 100). 'Nee' → de overdracht is geen verkoop → financieringsverwerking (alinea 103).

**Waarom?** Een sale-and-leaseback kan economisch een verkapte lening zijn. Als de verkoper-lessee de zeggenschap nooit echt overdroeg, zou meteen winstrealisatie en eigendomswijziging boeken een vertekend beeld geven. De IFRS 15-test filtert echte verkopen van pure financieringen.



Twee varianten op Zelena Bio's productiehal-deal: (a) Aurelia neemt fysiek bezit, draagt onderhouds- en eigendomsrisico's, kan de hal verkopen aan derden — verkoop geldig, alinea 100-verwerking. (b) Aurelia heeft een terugkoopverplichting tegen vaste prijs op einde lease — geen werkelijke zeggenschapsoverdracht, alinea 103-verwerking (financiering).

_Grondslag: IFRS 16 alinea 99 + IFRS 15-criteria_

### Pad A — overdracht is een verkoop (alinea 100) ⚖️

Bij een geldige verkoop boekt de verkoper-lessee: (a) het ROU-actief tegen **een evenredig deel van de oude boekwaarde** = oude boekwaarde × (contante waarde leasebetalingen / reële waarde actief). Het ROU vertegenwoordigt alleen het *behouden* gebruiksrecht. (b) Winst of verlies wordt alleen opgenomen voor het deel van de rechten dat **werkelijk is overgedragen** aan de koper-lessor — niet de volledige verkoopwinst. De koper-lessor verwerkt de aankoop volgens de geldende standaard (typisch IAS 16 voor het vastgoed) en de lease volgens de lessor-regels van IFRS 16.

**Waarom?** Als de verkoper-lessee het actief blijft gebruiken, heeft hij niet alle rechten verkocht. Volledige winstrealisatie zou economisch onjuist zijn. Het splitsingsprincipe ('overgedragen rechten' versus 'behouden rechten') zorgt voor symmetrie tussen wat is verkocht en wat als winst telt.



Zie record-niveau voorbeeld bij Zelena Bio: ROU = € 4.000.000 × (€ 3.894.000 / € 6.000.000) = € 2.596.000; opgenomen winst = € 2.000.000 × (€ 2.106.000 / € 6.000.000) ≈ € 702.000. De overige winst (€ 1.298.000) zit verwerkt in de relatief lagere ROU-waarde en kruist later via lagere afschrijving in het resultaat.

_Grondslag: IFRS 16 alinea 100_

### Pad B — overdracht is geen verkoop (alinea 103) ⚖️

Bij een ongeldige verkoop (IFRS 15-toets niet doorstaan) blijft het actief op de balans van de verkoper-lessee staan — er is geen activum-wegboeking en geen winstrealisatie. In plaats daarvan boekt de verkoper-lessee een **financiële verplichting** ten belope van de ontvangen overdrachtsprijs, te verwerken volgens IFRS 9 (rentekost op effectieve-rentevoetmethode, aflossing met de leasebetalingen). De koper-lessor neemt het actief NIET op de balans — die boekt een financieel actief (vordering) ten belope van de betaalde prijs.

**Waarom?** Als de zeggenschap niet werkelijk is overgegaan, is de transactie economisch een **gedekte lening** waarbij het actief enkel als zekerheid dient. Boekhoudkundig moet de balans dat reflecteren: actief blijft bij oorspronkelijke eigenaar; cash-instroom is een schuld, geen verkoop.



Variant op Zelena Bio's deal: Aurelia ontvangt € 6.000.000 maar Zelena heeft een vaste terugkoopverplichting in jaar 10 voor € 1.000.000 en blijft alle risico's dragen. Zeggenschap is niet overgegaan. Zelena boekt: hal blijft op balans voor € 4.000.000, schuld aan Aurelia € 6.000.000; jaarlijkse lease-betalingen worden gesplitst in rente (IFRS 9 effectieve methode) + hoofdsom-aflossing.

_Grondslag: IFRS 16 alinea 103 + IFRS 9_

### Aanpassing voor niet-marktconforme prijzen (alinea 101-102) ⚖️

Als de verkoopprijs of de lease-betalingen niet marktconform zijn, moet de entiteit eerst corrigeren naar reële waarde: **gunstiger** voorwaarden voor de verkoper-lessee → behandelen als **vooruitbetaling van lease**; **ongunstiger** voorwaarden → behandelen als **additionele financiering** door de koper-lessor. De aanpassing wordt bepaald op basis van het kleinste van twee bedragen: (a) verschil tussen reële vergoeding en reële waarde actief, of (b) verschil tussen contante waarde contractuele leasebetalingen en marktconforme leasebetalingen.

**Waarom?** Sale-and-leaseback-deals worden vaak gestructureerd om resultaten te manipuleren — door bv. een te hoge verkoopprijs te koppelen aan extra hoge huur. Alinea 101-102 voorkomt dit door substance over form te verzekeren: niet-marktconforme elementen worden uitgesplitst en correct toegewezen aan respectievelijk lease-voorschot of financiering.



Aurelia betaalt Zelena € 7.000.000 (reële waarde hal: € 6.000.000), in ruil voor verhoogde jaarlease € 580.000 (marktconform € 480.000). De extra € 1.000.000 verkoopprijs corrigeert tegen € 100.000 × annuïteit(10j;4%) = € 811.000 contante waarde extra lease. Aanpassing = min(€ 1.000.000; € 811.000) = € 811.000 wordt als additionele financiering (schuld) verwerkt; de eigenlijke verkoop is dan € 7.000.000 − € 811.000 = € 6.189.000 — dichter bij reële waarde.

_Grondslag: IFRS 16 alinea 101-102_

### Zeggenschap-criterium voor sale-and-leaseback (B46-B47) ⚖️

De technische definitie van 'sale-and-leaseback' draait om **zeggenschap vóór de overdracht**: een transactie geldt als sale-and-leaseback wanneer de lessee al zeggenschap had over het actief vóór het werd overgedragen aan de lessor (B46). Indien de lessee tijdelijk juridische eigendom verwerft (bv. via een fabrikant) maar nooit zeggenschap heeft gehad, dan is het GEEN sale-and-leaseback maar een gewone leaseovereenkomst (B47).

**Waarom?** Een onderneming die een nieuw actief via een lessor financiert (typisch bij autofinancieringen of equipment-leases waarbij de lessor van de fabrikant koopt) zou anders ten onrechte onder de strenge sale-and-leaseback-regels vallen. Het onderscheid 'al zeggenschap gehad' versus 'nooit zeggenschap gehad' filtert deze typische driehoekstransacties.



Zelena Bio bezat de productiehal al jaren en verkoopt die nu aan Aurelia met terugleasing → sale-and-leaseback (alinea 98-103). Zou Zelena een nieuwe machine bestellen die direct door Aurelia bij de fabrikant gekocht en aan Zelena geleased wordt zonder dat Zelena tussentijds zeggenschap had, dan is dat een gewone lease (B47).

_Grondslag: IFRS 16 B45-B47_


## In de praktijk

<h3 id="belgische-gaap-uitgestelde-meerwaarde-via-overlopende-rekening">Belgische GAAP — uitgestelde meerwaarde via overlopende rekening</h3>

> [!tip]- Belgische GAAP — uitgestelde meerwaarde via overlopende rekening
> Onder Belgisch GAAP (artikel 63 KB W.Venn., toegelicht in CBN-advies 2015/04 §III.C) is sale-and-leaseback één samengestelde verrichting. De bij overdracht vastgestelde **meerwaarde** wordt aan de passiefzijde geboekt op een overlopende rekening (rekening 49) en elk jaar in resultaat genomen **naar verhouding van de afschrijving** van het geleasde goed. Dezelfde behandeling geldt voor minderwaarden. Praktisch effect: geen onmiddellijke winstrealisatie, de winst smelt mee met de afschrijving van het terugleased goed. Onder IFRS 16 daarentegen wordt een evenredige winst onmiddellijk opgenomen voor het overgedragen deel (alinea 100) en draagt het ROU-actief de overige winst impliciet via een lagere boekwaarde. ⚖️

<h3 id="toelichting-en-informatieverschaffing">Toelichting en informatieverschaffing</h3>

> [!tip]- Toelichting en informatieverschaffing
> Een lessee moet onder IFRS 16 in de toelichting de winsten of verliezen uit sale-and-leasebacktransacties apart vermelden (alinea 53(i)). Voor materiële sale-and-leaseback-transacties verwacht IFRS 16 (B52) ook kwalitatieve toelichting over: de **redenen** voor de transactie, sleutelvoorwaarden, en de impact op kasstromen in de verslagperiode. Onder BE-GAAP is geen specifieke sale-and-leaseback-toelichtingsregel; de algemene leasing-toelichtingen van CBN 2015/04 gelden plus de boeking op overlopende rekening is herkenbaar in de balansposten. ⚖️


> [!info]- Niet verwarren met [[leasing]]
> BE-GAAP (art. 63 KB W.Venn. + CBN 2015/04) verwerkt sale-and-leaseback als één geheel met uitgestelde meerwaarde (overlopende rekening 49, vrijgegeven naar verhouding van afschrijving). IFRS 16 doet eerst een IFRS 15-zeggenschap-toets en kiest dan tussen evenredige onmiddellijke winstrealisatie (alinea 100) of financieringsverwerking (alinea 103). Verschillende winst-timing en balans-impact.
>
> _Trigger_: Examen: 'Onderneming X verkoopt gebouw aan financier en least het 10 jaar terug.' Onder BE-GAAP: meerwaarde naar overlopende rekening, jaarlijks vrijgegeven. Onder IFRS 16: eerst IFRS 15-toets; bij geldige verkoop direct gedeeltelijke winst + ROU + leaseverplichting.

> [!info]- Niet verwarren met [[leasing-ifrs]]
> Bij een gewone IFRS 16-lease boekt de lessee bij aanvang ROU + leaseverplichting (alinea 22). Bij sale-and-leaseback komt daar een verkoop-luik bij: het actief verlaat de balans, een evenredige winst kan worden opgenomen, en het ROU wordt op basis van de boekwaarde van het verkochte actief gewaardeerd — niet op basis van de contante waarde van leasebetalingen.
>
> _Trigger_: Examen: leasenemer vs verkoper-lessee onderscheid. Leasenemer-only → ROU = kostprijs (alinea 23-24). Verkoper-lessee → ROU = oude boekwaarde × verhouding behouden gebruiksrecht (alinea 100).


## Valkuilen

> [!warning]- Volledige winstrealisatie is een klassieke fout: een onderneming die een gebouw met € 2.000.000 boekmeerwaarde verkoopt en terugleaset zou o…
> ⚠️ Volledige winstrealisatie is een klassieke fout: een onderneming die een gebouw met € 2.000.000 boekmeerwaarde verkoopt en terugleaset zou onder oude IAS 17-regels (operationele leaseback) de volledige meerwaarde mogen boeken. Onder IFRS 16 alinea 100 mag enkel het deel van de meerwaarde dat overeenkomt met de **overgedragen rechten** worden opgenomen; de rest blijft impliciet in de ROU-waarde verwerkt. Zelena Bio's € 2.000.000 boekmeerwaarde leidt onder IFRS 16 maar tot ~€ 702.000 onmiddellijke winst. ⚖️
>
> _Bron: IFRS 16 alinea 100_


> [!warning]- Verwarring tussen 'tijdelijke eigendom' en 'sale-and-leaseback': een driehoekstransactie waarbij de lessee even juridische eigendom verwerft…
> ⚠️ Verwarring tussen 'tijdelijke eigendom' en 'sale-and-leaseback': een driehoekstransactie waarbij de lessee even juridische eigendom verwerft maar nooit zeggenschap had (B47), is GEEN sale-and-leaseback maar een gewone lease. Typische fout bij autofinancieringen waar de fabrikant kortstondig aan de lessee verkoopt en de leasemaatschappij de keten financiert. ⚖️
>
> _Bron: IFRS 16 B47_


> [!warning]- Niet-marktconforme prijzen ondoorzichtig: een verkoop boven reële waarde gekoppeld aan boven-marktlease wordt vaak benut om winsten naar vor…
> ⚠️ Niet-marktconforme prijzen ondoorzichtig: een verkoop boven reële waarde gekoppeld aan boven-marktlease wordt vaak benut om winsten naar voren te halen. Alinea 101-102 dwingt dat de extra niet-marktconforme component als vooruitbetaling van lease OF additionele financiering wordt verwerkt — niet als gewone verkoopprijs. Stagiairs vergeten deze test door te lopen. ⚖️
>
> _Bron: IFRS 16 alinea 101-102_



## Zie ook

- **Vereist kennis van**: [[right-of-use-actief]]
- **Vereist kennis van**: [[leaseverplichting-ifrs]]
- **Vereist kennis van**: [[prestatieverplichting]]

## Voorbeelden

Zelena Bio NV bezit haar productiehal in Antwerpen (boekwaarde € 4.000.000, reële waarde € 6.000.000). Op 1 januari 2026 verkoopt zij de hal aan Aurelia Holding NV voor € 6.000.000 én sluit gelijktijdig een 10-jarige lease aan € 480.000/jaar (marginale rentevoet 4%, contante waarde betalingen ≈ € 3.894.000). De overdracht voldoet aan IFRS 15: Aurelia heeft de zeggenschap verworven. Onder IFRS 16 alinea 100 boekt Zelena: (1) actief wegboeken voor boekwaarde € 4.000.000; (2) ROU opnemen voor het *behouden* gebruiksrecht = € 4.000.000 × (€ 3.894.000 / € 6.000.000) = € 2.596.000; (3) leaseverplichting € 3.894.000; (4) winst op verkoop alleen op het *overgedragen* deel = (€ 6.000.000 − € 4.000.000) × ((€ 6.000.000 − € 3.894.000) / € 6.000.000) = € 2.000.000 × 0,351 ≈ € 702.000. Geen volledige winstrealisatie van € 2.000.000.
### Sale-and-leaseback Pad A — Zelena Bio NV verkoopt productiehal aan Aurelia Holding NV

_Personages: Zelena Bio NV, Aurelia Holding NV_

Zelena Bio NV (verkoper-lessee) bezit een productiehal in Antwerpen — boekwaarde € 4.000.000, reële waarde € 6.000.000. Op 1 januari 2026 verkoopt zij de hal aan Aurelia Holding NV (koper-lessor) voor € 6.000.000 en sluit een 10-jarige lease aan € 480.000/jaar (marginale rentevoet 4%, contante waarde leasebetalingen ≈ € 3.894.000). Aurelia heeft volgens IFRS 15 de zeggenschap verworven, dus Pad A van IFRS 16 alinea 100 is van toepassing.

1. Bereken behouden gebruiksrecht in verhouding tot reële waarde: € 3.894.000 / € 6.000.000 = 0,649 → ROU = € 4.000.000 × 0,649 = € 2.596.000.
2. Bereken overgedragen rechten in verhouding tot reële waarde: (€ 6.000.000 − € 3.894.000) / € 6.000.000 = 0,351.
3. Bepaal winst op overgedragen deel: (€ 6.000.000 − € 4.000.000) × 0,351 = € 2.000.000 × 0,351 ≈ € 702.000.
4. Boek het wegboeken van de hal (€ 4.000.000), de opname ROU (€ 2.596.000) + leaseverplichting (€ 3.894.000), ontvangen cash (€ 6.000.000) en de winst op overgedragen deel (€ 702.000).
#### Boeking sale-and-leaseback Pad A bij Zelena Bio NV — 1 januari 2026
_Verkoop voldoet aan IFRS 15-zeggenschap-test → verwerking volgens IFRS 16 alinea 100 (Pad A). Debet-totaal € 8.596.000 = credit-totaal € 8.596.000 (= € 4.000.000 hal + € 3.894.000 leaseverplichting + € 702.000 meerwaarde op overgedragen deel)._

| Rekening | Debet | Credit |
|---|---:|---:|
| Bank | 6000000 |  |
| ROU-actief (gebouwen, behouden gebruiksrecht) | 2596000 |  |
| Materiële vaste activa — productiehal (uitboeken) |  | 4000000 |
| Leaseverplichting (langlopend) |  | 3894000 |
| Meerwaarde op verkoop activa (W&V, alleen overgedragen deel) |  | 702000 |

_Bron: IFRS 16 alinea 99-100_ ⚖️


## Bronnen

[^1]: `IFRS-16-leaseovereenkomsten__sec_informatieverschaffing_2`
[^2]: `CBN-2015-04-leasing__sec_sale-and-lease-back-overeenkomsten`
[^3]: `IFRS-16-leaseovereenkomsten__sec_identificatie-van-een-leaseovereenkomst-alinea-s-b9-tot-en-m`
[^4]: `IFRS-16-leaseovereenkomsten__sec_informatieverschaffing`
