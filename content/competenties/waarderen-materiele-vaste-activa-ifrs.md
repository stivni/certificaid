---
title: Waarderen van materiële vaste activa onder IAS 16 (kostprijs- of herwaarderingsmodel)
tags:
- competentie
- po-1-5
programmaonderdelen:
- '1.5'
status: voorgesteld
schema_version: '1.1'
gegenereerd_uit: data/concepten/competenties/waarderen-materiele-vaste-activa-ifrs.yaml
gegenereerd_op: '2026-05-17'
---
# Waarderen van materiële vaste activa onder IAS 16 (kostprijs- of herwaarderingsmodel)

**⚖️ 75% · 🤖 25%**

> De keuze tussen kostprijs- en herwaarderingsmodel + de componentenbenadering + afschrijvingsregels zijn rechtstreeks in IAS 16 (alinea's 15-66) geregeld. Het praktijk-aandeel zit in het inschatten van de gebruiksduur per component, de restwaarde, en de frequentie van herwaardering (bij voldoende regelmaat zodat boekwaarde nooit substantieel afwijkt van reële waarde).

## Aanbevolen werkwijze

### 1. Bepaal de eerste waardering (kostprijs)

Stel de kostprijs vast bij eerste opname: aankoopprijs (netto van kortingen) + alle direct toerekenbare kosten om het actief gebruiksklaar te maken + geraamde ontmantelings- en herstelverplichting.

**Waarom?** IAS 16 alinea 15 bepaalt dat de eerste waardering uit drie componenten bestaat. Onvolledig opnemen (bv. ontmantelingsverplichting vergeten) leidt tot een te lage activum-waarde en een latere voorzieningsboeking met cumulatieve impact.

**📥 Input**:
- Aankoopfactuur + transportkosten + installatiekosten → **Per kostenpost: bedrag** _(boekhoudkundig-bedrag)_
- Inschatting ontmantelings- en herstelverplichting → **Contante waarde verwachte kosten** _(boekhoudkundig-bedrag)_

**📤 Output**:
- Investeringsdossier → **Initiële kostprijs van het actief** _(boekhoudkundig-bedrag)_

**🛠️ Hoe**:

1. Volg [[materiele-vaste-activa-ifrs]] §eerste-waardering voor de drie componenten.
2. Zelena Bio NV koopt een productie-installatie: aankoopprijs € 8.000.000 + transport en installatie € 250.000 + initiële tests € 150.000 + contante waarde ontmantelingsverplichting € 600.000 = **initiële kostprijs € 9.000.000**.
3. Documenteer per component met factuur-referentie of berekenings-werkpapier.
4. Belangrijk: lopende exploitatiekosten en opleidings-kosten zijn GEEN onderdeel van de kostprijs (alinea 19).


**Grondslag**: [[materiele-vaste-activa-ifrs]] §eerste-waardering, IAS 16 alinea 15-22

### 2. Identificeer significante componenten en stel afschrijvingsplan per component op

Splits het actief in delen waarvan de kostprijs significant is t.o.v. het totaal én die een verschillende gebruiksduur of afschrijvingspatroon hebben. Schrijf elke component apart af.

**Waarom?** IAS 16 alinea 43-45 (componentenbenadering) is verplicht — een gebouw heeft niet één gebruiksduur maar bv. structuur (50 jaar), dakbedekking (20 jaar) en HVAC (15 jaar).

**📥 Input**:
- Investeringsdossier uit stap 1 → **Totaalkostprijs + technische beschrijving** _(boekhoudkundig-bedrag)_
- Technische expertise → **Gebruiksduren per component** _(document)_

**📤 Output**:
- Afschrijvingsplan IFRS → **Per component: kostprijs + duur + methode + jaarlijkse afschrijving** _(document)_

**🛠️ Hoe**:

1. Volg [[componentenbenadering-ias-16]] §identificatie voor het detecteren van significante componenten.
2. Voor de Zelena-productie-installatie van € 9.000.000: identificeer (a) machine-kern € 6.500.000 / 20 jaar, (b) regelsysteem € 1.500.000 / 8 jaar, (c) bekabeling € 800.000 / 10 jaar, (d) ontmantelingsdeel € 200.000 / 20 jaar.
3. Kies per component een afschrijvingsmethode die het verbruikspatroon van de economische voordelen weerspiegelt: lineair, degressief of units-of-production (alinea 62). Geen 'opbrengstenmethode' (alinea 62A — verboden).
4. Reken de jaarlijkse afschrijving per component uit en sommeer.


> [!example]- Voorbeeld: Componentenbenadering productie-installatie Zelena Bio NV: € 9.000.000 verdeeld over 4 componenten met verschillende geb…
> Componentenbenadering productie-installatie Zelena Bio NV: € 9.000.000 verdeeld over 4 componenten met verschillende gebruiksduren.
>
> 1. **Afschrijvingsplan per component** 🧮
>
>    | Component        | Kostprijs (€) | Gebruiksduur | Jaarlijkse afschrijving (€) |
>    |------------------|--------------:|-------------:|----------------------------:|
>    | Machine-kern     |     6.500.000 |      20 jaar |                     325.000 |
>    | Regelsysteem     |     1.500.000 |       8 jaar |                     187.500 |
>    | Bekabeling       |       800.000 |      10 jaar |                      80.000 |
>    | Ontmantelingsdeel|       200.000 |      20 jaar |                      10.000 |
>    | **Totaal**       | **9.000.000** |              |                 **602.500** |
>    
>

**Grondslag**: [[componentenbenadering-ias-16]] §identificatie, [[afschrijvingen-ifrs]] §methodekeuze, IAS 16 alinea 43-62A

### 3. Kies tussen kostprijs- en herwaarderingsmodel per klasse

Beslis per klasse van materiële vaste activa (terreinen, gebouwen, machines, voertuigen, ...) of na eerste opname het kostprijsmodel (alinea 30) of het herwaarderingsmodel (alinea 31) wordt toegepast. De keuze geldt voor de hele klasse.

**Waarom?** IAS 16 vereist consistentie binnen één klasse om cherry-picking van enkel waardevolle activa te voorkomen. De keuze is geen vrije omkering — wel een doordachte beleidskeuze.

**📥 Input**:
- Klasse-indeling materiële vaste activa → **Lijst van klassen + activa per klasse** _(document)_
- Inschatting frequentie en kosten reële-waarde-bepaling → **Per klasse: haalbaar of niet** _(document)_

**📤 Output**:
- Grondslagen-toelichting IFRS → **Per klasse: gekozen model + motivering** _(beleidskeuze)_

**🛠️ Hoe**:

1. Volg [[herwaarderingsmodel-ias-16]] §toepassingsvoorwaarden voor het herwaarderingsmodel.
2. Voor Zelena Bio: terreinen → herwaarderingsmodel (reële waarde betrouwbaar te bepalen via externe taxateur jaarlijks); gebouwen → kostprijsmodel (eenvoudiger, geen volatiele markt); machines → kostprijsmodel.
3. Bij keuze herwaarderingsmodel: herwaarderingen moeten frequent genoeg gebeuren zodat boekwaarde nooit substantieel afwijkt van reële waarde (alinea 31 + 34).
4. Vermelding in toelichting: gekozen model + (bij herwaarderingsmodel) datum laatste herwaardering + onafhankelijke taxateur + grondslagen voor reële-waarde-bepaling (alinea 77).


**Grondslag**: [[herwaarderingsmodel-ias-16]] §toepassingsvoorwaarden, IAS 16 alinea 29-31

> [!warning]- Bij keuze voor herwaarderingsmodel: ga deze keuze pas aan als reële waarde betrouwbaar én regelmatig kan worden vastgesteld — niet voor uniek of moeilijk meetbaar actief.
>
> _Vaak fout gedaan_: Het herwaarderingsmodel kiezen om de balans op te poetsen, zonder structurele frequentie van herwaarderen. Dit produceert misleidende stille meerwaarden.
>
> _Grondslag_: [[herwaarderingsmodel-ias-16]] §frequentie

### 4. Pas het gekozen model toe (kostprijs OF herwaardering)

Voor kostprijsmodel: kostprijs − cumulatieve afschrijving − cumulatieve bijzondere waardevermindering. Voor herwaarderingsmodel: reële waarde op herwaarderingsdatum − sindsdien cumulatieve afschrijving − cumulatieve bijzondere waardevermindering.

**Waarom?** Het toepassen vereist concrete boekingen: bij kostprijsmodel jaarlijkse afschrijving + impairment-test bij triggers; bij herwaarderingsmodel herwaarderingen via OCI of W&V naargelang dezelfde klasse eerder anders bewogen heeft.

**📥 Input**:
- Boekwaarde op begin boekjaar → **Per actief** _(boekhoudkundig-bedrag)_
- Externe taxatie (bij herwaarderingsmodel) → **Reële waarde op herwaarderingsdatum** _(boekhoudkundig-bedrag)_

**📤 Output**:
- Boekingen in IFRS-resultaat en OCI → **Afschrijving / herwaardering / impairment** _(boekingsregel)_

**🛠️ Hoe**:

1. Bij kostprijsmodel: boek jaarlijkse afschrijving per component conform plan stap 2 → debet 'Afschrijvingskosten', credit 'Cumulatieve afschrijving'.
2. Bij herwaarderingsmodel: vergelijk reële waarde met boekwaarde op herwaarderingsdatum. Eerste opwaardering → boek het verschil in **OCI** als 'Herwaarderingsreserve' (alinea 39). Latere afwaardering → eerst tegen de bestaande herwaarderingsreserve van hetzelfde actief in OCI, dan pas in W&V (alinea 40).
3. Toets op elke balansdatum of er aanwijzingen zijn voor bijzondere waardevermindering — zo ja, volg [[toetsen-bijzondere-waardevermindering-ias-36]].
4. Bij realisatie (verkoop): herwaarderingsreserve mag overgeboekt worden naar ingehouden winsten — NIET via W&V (alinea 41).


> [!example]- Voorbeeld: Zelena Bio NV: herwaardering terreinen Antwerpse site op 31 december 2027
> Zelena Bio NV: herwaardering terreinen Antwerpse site op 31 december 2027. Boekwaarde (BE-GAAP-kostprijs op overgangsdatum 1 januari 2026 = veronderstelde kostprijs onder IFRS 1 D5) € 18.000.000; nieuwe reële waarde € 22.000.000.
>
> 1. **Berekening herwaarderingsverschil** 🧮
>
>    reële waarde op 31 december 2027 = € 22.000.000
>    boekwaarde vóór herwaardering    = € 18.000.000
>    **opwaardering**                  = **€ 4.000.000**
>    
>
> 2. **Boeking in OCI** 📝
>
>    Debiteer:  Terreinen                                  € 4.000.000
>    Crediteer: Herwaarderingsreserve (OCI, eigen vermogen) € 4.000.000
>    
>    (Geen impact op W&V — eerste opwaardering van deze klasse.)
>    
>

**Grondslag**: [[materiele-vaste-activa-ifrs]] §waardering-na-opname, IAS 16 alinea 29-42

> [!warning]- Bij herwaarderingsmodel altijd eerst de bestaande herwaarderingsreserve van datzelfde actief opzoeken vóór een afwaardering in W&V te boeken.
>
> _Vaak fout gedaan_: Een afwaardering meteen in W&V boeken terwijl er nog een eerdere opwaardering in OCI staat. IAS 16 alinea 40 vereist die eerst terug te draaien.
>
> _Grondslag_: [[herwaarderingsmodel-ias-16]] §symmetrische-verwerking


## Voorbeelden

> [!example]- Rotex Roeselare NV (BE-GAAP, niet IFRS-plichtig) en Zelena Bio NV (IFRS-plichtig) kopen elk dezelfde productie-installat…
> **Conclusie**: Rotex onder BE-GAAP: één afschrijvingsplan over een gewogen gemiddelde gebruiksduur van bv. 15 jaar → jaarlijkse afschrijving € 600.000. Zelena Bio onder IFRS: vier componenten met verschillende duren → jaarlijkse afschrijving € 602.500 maar met afnemend patroon (regelsysteem volledig afgeschreven na 8 jaar; bekabeling na 10 jaar). De IFRS-componentenbenadering toont sneller dat verlengingen of vervangingen nodig zijn — pedagogisch verschil illustreert de hogere granulariteit.
>
> **Grondslag**: [[componentenbenadering-ias-16]] §pedagogisch-verschil; [[afschrijvingen-ifrs]] §verbruikspatroon; [[be-gaap-vs-ifrs-overzicht]] §materiele-vaste-activa
>
> **Redenering**: Onder BE-GAAP volstaat één afschrijvingsplan op activum-niveau (KB WVV staat dit toe). IFRS vereist componenten met significante verschillen in gebruiksduur apart te behandelen. De som van componenten-afschrijvingen wijkt slechts marginaal af, maar de tijdsspreiding is verschillend.


## Gebaseerd op concepten

[[materiele-vaste-activa-ifrs]] · [[herwaarderingsmodel-ias-16]] · [[componentenbenadering-ias-16]] · [[afschrijvingen-ifrs]] · [[bijzondere-waardevermindering-ias-36]]
## Voortkomend uit

- **Taken**: 1.5.taak.1
- **Kenniselementen**: 1.5.V.A, 1.5.V.B, 1.5.IV.C
