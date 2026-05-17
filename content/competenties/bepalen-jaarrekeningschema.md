---
title: Bepalen welk jaarrekening-schema (volledig, verkort, micro) een vennootschap
  moet gebruiken
tags:
- competentie
- po-1-2
programmaonderdelen:
- '1.2'
status: voorgesteld
schema_version: '1.1'
gegenereerd_uit: data/concepten/competenties/bepalen-jaarrekeningschema.yaml
gegenereerd_op: '2026-05-17'
---
# Bepalen welk jaarrekening-schema (volledig, verkort, micro) een vennootschap moet gebruiken

**⚖️ 95% · 🤖 5%**

> De drie schema's en hun bijhorende grootteklassen zijn rechtstreeks geregeld in KB-WVV (bijlagen 1, 2 en 3) en in WVV art. 3:5-3:7. Praktijkoordeel beperkt zich tot het beoordelen van overgangsperiodes (vorig schema voortzetten of niet) en sectorspecifieke aanpassingen.

## Aanbevolen werkwijze

### 1. Haal de grootteklasse op

Bepaal of de vennootschap micro, klein of groot is voor het betrokken boekjaar.

**Waarom?** De grootteklasse stuurt rechtstreeks de schemakeuze.

**📥 Input**:
- Werknotitie groottecriteria-toets → **Definitieve grootteklasse** _(conclusie)_

**📤 Output**:
- Werknotitie → **Grootteklasse (micro / klein / groot)** _(conclusie)_

**🛠️ Hoe**:

1. Open het resultaat van de competentie [[klasseren-vennootschap-naar-groottecategorie]] voor het boekjaar.
2. Voer ontbrekend de toets uit volgens [[groottecriteria-jaarrekening]] §criteria.
3. Noteer expliciet welke grootteklasse geldt voor het rapporteringsjaar.


**Grondslag**: [[groottecriteria-jaarrekening]] §grootteklassen

### 2. Selecteer het bijhorende KB-WVV-schema

Wijs het schema toe volgens de regel groot → bijlage 1, klein → bijlage 2, micro → bijlage 3.

**Waarom?** Elk schema heeft een ander detailniveau in balans, resultatenrekening en toelichting.

**📥 Input**:
- Werknotitie stap 1 → **Grootteklasse** _(conclusie)_

**📤 Output**:
- Schemakeuze → **Volledig / verkort / micro** _(conclusie)_

**🛠️ Hoe**:

1. Groot → volledig schema, [[jaarrekening-schema]] §volledig-schema, KB-WVV bijlage 1.
2. Klein (niet micro) → verkort schema, [[jaarrekening-schema]] §verkort-schema, KB-WVV bijlage 2.
3. Micro → microschema, [[jaarrekening-schema]] §microschema, KB-WVV bijlage 3.
4. VZW / IVZW / stichting → apart vereenvoudigd of klein VZW-schema (KB-WVV art. 3:184 e.v.) — niet identiek aan vennootschapsschema's.


> [!example]- Voorbeeld: Drie cliënten op 31/12/2024: Rotex Roeselare NV (groot), Meubelzaak Mertens BV (klein, niet micro), Oprichtingen Oostend…
> Drie cliënten op 31/12/2024: Rotex Roeselare NV (groot), Meubelzaak Mertens BV (klein, niet micro), Oprichtingen Oostende BV (micro).
>
> 1. **Schema-toewijzing** 💬
>
>    | Cliënt | Grootteklasse | Schema | KB-WVV-bijlage |
>    |---|:---:|:---:|:---:|
>    | Rotex Roeselare NV | groot | volledig | bijlage 1 |
>    | Meubelzaak Mertens BV | klein | verkort | bijlage 2 |
>    | Oprichtingen Oostende BV | micro | micro | bijlage 3 |
>    
>

**Grondslag**: [[jaarrekening-schema]] §schema-per-grootte, KB-WVV art. 3:2 + bijlagen 1-3

### 3. Maak gevolgen voor sociale balans en toelichting expliciet

Bepaal of de sociale balans verplicht is en welk detail van toelichting van toepassing is.

**Waarom?** Schema bepaalt niet alleen presentatie maar ook welke bijlage-onderdelen wel of niet vereist zijn.

**📥 Input**:
- Schemakeuze stap 2 → **Schema** _(conclusie)_

**📤 Output**:
- Documentenlijst → **Balans + RR + toelichting (+ eventueel sociale balans + jaarverslag)** _(document)_

**🛠️ Hoe**:

1. Volledig schema en verkort schema → sociale balans verplicht ([[sociale-balans]] §verplichting). Microschema → géén sociale balans verplicht.
2. Toelichting: volledig schema → uitgebreid (kapitaalstaat, staat vaste activa, niet-balansrechten in detail). Verkort → beperkter. Micro → minimaal — zie [[toelichting-jaarrekening]] §detail-per-schema.
3. Jaarverslag: volledig schema → verplicht voor grote vennootschappen. Verkort en micro → niet verplicht (tenzij PIE of beursnotering).
4. Stel een documentenlijst op die je in de neerlegging zult opnemen.


**Grondslag**: [[jaarrekening-schema]] §componenten, [[toelichting-jaarrekening]] §detail-per-schema

> [!warning]- Sociale balans hoort bij verkort EN volledig schema, niet bij micro.
>
> _Vaak fout gedaan_: Een microvennootschap toch een sociale balans laten opmaken.
>
> _Grondslag_: [[sociale-balans]] §verplichting

### 4. Behandel een wijziging van schema bij grootteverandering

Stel de overgangsregels op als de vennootschap van grootteklasse verandert.

**Waarom?** Bij wisseling moet de vergelijkende kolom van het vorige boekjaar in het nieuwe schema worden gepresenteerd.

**📥 Input**:
- Schemakeuze huidig + vorig boekjaar → **Schema beide jaren** _(conclusie)_

**📤 Output**:
- Overgangs-werkblad → **Mapping rubrieken oud-nieuw + vergelijkende kolom** _(berekening)_

**🛠️ Hoe**:

1. Vergelijk schemakeuze huidig boekjaar met dat van vorig boekjaar.
2. Identiek? Geen overgangswerk — gebruik standaard vergelijkende kolom.
3. Verschillend (bv. klein → groot na lock-in)? Map elke rubriek van het verkort schema naar de uitgebreidere rubrieken van het volledig schema. Zie [[jaarrekening-schema]] §wijziging-bij-grootteverandering.
4. Documenteer in de toelichting de schemawissel en de impact op de vergelijkbaarheid.


**Grondslag**: [[jaarrekening-schema]] §wijziging-bij-grootteverandering, WVV art. 1:24 § 4


## Voorbeelden

> [!example]- Meubelzaak Mertens BV (klein, geen deelnemingen, geen beursnotering)
> **Conclusie**: Verkort schema (KB-WVV bijlage 2). Sociale balans verplicht. Jaarverslag niet verplicht.
>
> **Grondslag**: [[jaarrekening-schema]] §verkort-schema; [[kleine-vennootschap]] §gevolgen
>
> **Redenering**: Klein → verkort. Sociale balans hoort bij verkort schema. Jaarverslag valt weg.

> [!example]- Rotex Roeselare NV (groot, 550 werknemers, € 95M omzet)
> **Conclusie**: Volledig schema (KB-WVV bijlage 1). Sociale balans + uitgebreide toelichting + jaarverslag verplicht.
>
> **Grondslag**: [[jaarrekening-schema]] §volledig-schema
>
> **Redenering**: Grote vennootschap → alle componenten verplicht. Volledige toelichting bevat onder andere staat vaste activa, kapitaalstaat, ARO.

> [!example]- Oprichtingen Oostende BV in boekjaar 1 (4 werknemers, € 400.000 omzet, geen deelneming)
> **Conclusie**: Microschema (KB-WVV bijlage 3). Geen sociale balans, geen jaarverslag, minimale toelichting.
>
> **Grondslag**: [[jaarrekening-schema]] §microschema; [[microvennootschap]] §gevolgen
>
> **Redenering**: Onder alle micro-drempels + geen moeder/dochter → microschema. Laagste rapporteringslast.


## Gebaseerd op concepten

[[jaarrekening-schema]] · [[groottecriteria-jaarrekening]] · [[kleine-vennootschap]] · [[microvennootschap]] · [[kb-wvv-uitvoering]] · [[sociale-balans]] · [[toelichting-jaarrekening]]
## Voortkomend uit

- **Taken**: 1.2.taak.1
- **Kenniselementen**: 1.2.IV.C, 1.2.IV
