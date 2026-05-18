---
title: Groottecriteria (jaarrekening-context)
tags:
- concept
- regel
- po-1-2
- po-1-5
linked_anchors:
- 1.2.IV.B
- 1.2.IV
- 1.2.IV.C
- 1.5.I
programmaonderdelen:
- '1.2'
- '1.5'
confidence: grounded
node_type: regel
status: seed
schema_version: '1.5'
gegenereerd_uit: data/concepten/records/groottecriteria-jaarrekening.json
gegenereerd_op: '2026-05-18'
---
# Groottecriteria (jaarrekening-context) ⚖️

> [!summary] Korte inhoud
> Vennootschappen en verenigingen worden onderverdeeld in drie groottecategorieën — micro, klein en groot — op basis van drie criteria (jaargemiddelde personeelsbezetting, jaaromzet excl. BTW, balanstotaal).

Vennootschappen en verenigingen worden onderverdeeld in drie groottecategorieën — micro, klein en groot — op basis van drie criteria (jaargemiddelde personeelsbezetting, jaaromzet excl. BTW, balanstotaal). Een vennootschap is 'klein' als ze op balansdatum maximaal één criterium overschrijdt; 'micro' als ze daarenboven ook nog onder de strengere microdrempels blijft én geen 'moeder' of 'dochter' is. Overschrijdt ze meer dan één criterium → 'groot'.

_Bron: WVV art. 1:24 en 1:25_


## Bouwstenen

### Drie criteria, max één mag overschreden worden ⚖️

Eén criterium overschrijden = nog steeds 'klein'. Twee of drie criteria overschrijden = 'groot'. Het is dus geen som-formule; één 'fout' is OK, twee niet.

**Waarom?** Deze regel beschermt vennootschappen tegen statuswisseling bij toevallige uitschieter op één enkel criterium.



Brugse Brouwerij BV: 55 werknemers (te hoog), € 4M omzet (OK), € 3M balanstotaal (OK) → slechts 1 criterium overschreden → blijft klein.

_Grondslag: WVV art. 1:24 § 1_

### Twee opeenvolgende boekjaren ⚖️

De grootteklasse wijzigt pas als de overschrijding zich in twee opeenvolgende boekjaren voordoet ('lock-in regel'). Eénmalig overschrijden kantelt de status niet — pas bij herhaling.

**Waarom?** Voorkomt heen-en-weer-schommelen tussen klein en groot bij conjuncturele uitschieters.



Meubelzaak Mertens BV overschrijdt in 2024 zowel omzet als personeelsbezetting → moet wachten op 2025: blijft ze overschrijden? → vanaf 2026 'groot'.

_Grondslag: WVV art. 1:24, § 4_

### Verbondenheid trekt de telling op ⚖️

Een vennootschap die deel uitmaakt van een groep (moeder of dochter) telt de gegevens van de verbonden vennootschappen mee op geconsolideerde basis. Een 'kleine' vennootschap in een 'grote' groep wordt voor de jaarrekening behandeld als groot.

**Waarom?** Zo kan een grote groep niet zijn jaarrekening-verplichtingen ontwijken door zich op te splitsen in kleinere entiteiten.



Aurelia Holding NV (klein op zich) heeft 4 dochters → de groep heeft samen 60 werknemers en € 18M omzet → Aurelia wordt voor jaarrekening behandeld als groot.

_Grondslag: WVV art. 1:24, § 5; CBN-advies 2017/10_

### Microvennootschap: extra voorwaarde ⚖️

Naast de strengere drempels mag een microvennootschap géén moedervennootschap zijn en niet behoren tot een groep waarvan de moeder een geconsolideerde jaarrekening publiceert. Heeft ze één dochter → automatisch geen micro, maximaal klein.

**Waarom?** Microschema (kleinste schema) is bedoeld voor de allerkleinste, eenvoudigste vennootschappen — zonder groep-complexiteit.



Oprichtingen Oostende BV (omzet € 400K, 4 werknemers) → kan microschema gebruiken. Verwerft ze een 60%-deelneming → wordt moeder → schiet uit microschema, naar klein.

_Grondslag: WVV art. 1:25, § 2_


## In de praktijk

<h3 id="welk-schema-bij-welke-grootte">Welk schema bij welke grootte?</h3>

> [!tip]- Welk schema bij welke grootte?
> Microvennootschap → microschema (bijlage 3 KB-WVV). Kleine vennootschap → verkort schema (bijlage 2). Grote vennootschap → volledig schema (bijlage 1). Schema bepaalt detailniveau van balans, RR, toelichting + verplichting tot jaarverslag. ⚖️

> [!tip]- Herkennen op het examen
> Examenvraag begint met cijfers (omzet/personeel/balanstotaal) → eerst klasseren in micro/klein/groot, dan schema kiezen.


## Drempelwaarden

| Naam | Waarde | Eenheid | Gevolg |
|---|---|---|---|
| Drempels kleine vennootschap (na update 2024) | Personeelsbezetting ≤ 50; jaaromzet excl. BTW ≤ € 11.250.000; balanstotaal ≤ € 6.000.000 | drie criteria — max 1 mag overschreden worden | _zie toelichting hieronder_ |
| Drempels microvennootschap | Personeelsbezetting ≤ 10; jaaromzet excl. BTW ≤ € 900.000; balanstotaal ≤ € 450.000 | drie criteria — max 1 mag overschreden worden | Mag microschema gebruiken (kleinste schema). Bijkomende voorwaarde: geen moeder- of dochtervennootschap zijn. |

> [!info]- Drempels kleine vennootschap (na update 2024)
> Mag verkort schema gebruiken; geen jaarverslag verplicht; geen commissaris verplicht (tenzij ze deel uitmaakt van een groep die als geheel groot is).


> [!info]- Niet verwarren met [[groottecriteria-consolidatie]]
> Groottecriteria-jaarrekening (WVV art. 1:24-1:25) bepalen het schema van de enkelvoudige jaarrekening. Groottecriteria-consolidatie (WVV art. 1:26) bepalen de vrijstelling van consolidatieplicht voor 'groep van beperkte omvang'. Andere drempelwaarden, ander gevolg.
>
> _Trigger_: Examen 'welk schema moet X gebruiken?' → 1:24/1:25. 'Mag groep X afzien van consolideren?' → 1:26.


## Valkuilen

> [!warning]- Een 'kleine' dochter van een grote groep is voor de jaarrekening géén kleine vennootschap
> ⚠️ Een 'kleine' dochter van een grote groep is voor de jaarrekening géén kleine vennootschap. Test altijd verbondenheid (WVV art. 1:24, § 5) voor je 'verkort schema' adviseert. ⚖️
>
> _Bron: CBN-advies 2017/10_


> [!warning]- Drempels zijn periodiek geïndexeerd
> ⚠️ Drempels zijn periodiek geïndexeerd. Bij EU-richtlijn delegated act 2023 werden de bedragen met circa 25% verhoogd. In ITAA-LEX vind je de actuele bedragen — niet vertrouwen op cijfers uit oudere studiehandboeken. 🤖
>
> _Bron: Delegated Directive 2023/2775_



## Zie ook

- **Getriggerd door**: [[wetboek-vennootschappen-verenigingen]]
- **Vereist kennis van**: [[jaarrekening-schema]]

## Voorbeelden

Meubelzaak Mertens BV heeft op 31/12/2024: 12 werknemers, € 4.500.000 omzet, € 2.100.000 balanstotaal → onder kleine-vennootschap-drempels op alle 3 criteria → kleine vennootschap → mag verkort schema gebruiken.

## Bronnen

[^1]: `CBN-2022-03-beoordeling-van-de-groottecriteria-overeenkomstig-artikelen-124-en-125-van-het-wetboek-van__sec_definitie-van-kleine-vennootschappen-en-microvennootschappen`
[^2]: `CBN-2022-03-beoordeling-van-de-groottecriteria-overeenkomstig-artikelen-124-en-125-van-het-wetboek-van__sec_toepassingsgebied`
[^3]: `CBN-2018-22-groottecriteria-alternatieve-berekening-van-de-omzet-op__volledig_part1`
[^4]: `CBN-2017-10-groottecriteria-artikel-15-w-venn-verbonden__sec_wijziging-verbondenheid`
[^5]: `CBN-2017-10-groottecriteria-artikel-15-w-venn-verbonden__sec_algemeen`
