---
title: Voorraad — fysieke controle en veiligheid
tags:
- concept
- procedure
- po-1-7
linked_anchors:
- 1.7.IX.E
- 1.7.IX
programmaonderdelen:
- '1.7'
confidence: inferred
node_type: procedure
status: seed
schema_version: '1.5'
gegenereerd_uit: data/concepten/records/voorraadcyclus-ic.json
gegenereerd_op: '2026-05-18'
---
# Voorraad — fysieke controle en veiligheid 🤖

> [!summary] Korte inhoud
> Jaarlijkse inventaris (KB 21.10.2018 boekhoudkundige verplichtingen).

> [!info] Behoort tot: [[interne-controle]]

Jaarlijkse inventaris (KB 21.10.2018 boekhoudkundige verplichtingen).


## Stappen

### 1. Fysieke bewaking + toegangscontrole

Magazijn op slot; toegang beperkt tot magazijnpersoneel via badge; camerabewaking bij waardevolle voorraad.

**Waarom?** Open magazijn = directe diefstal-mogelijkheid voor élke medewerker.

**🛠️ Hoe**:

1. Badge-toegang met log per persoon per uur.
2. Camerabewaking ingang en hoge-waarde-zones.
3. Verzegeling buiten kantooruren.

**Grondslag**: Fysieke-beveiliging-doctrine

### 2. Permanente voorraad in ERP

Elke ingang en uitgang van voorraad direct boeken; saldo zichtbaar in real-time.

**Waarom?** Zonder permanente voorraad ontdekken verschillen pas bij jaarlijkse telling — te laat.

**🛠️ Hoe**:

1. Magazijnier scant elke beweging.
2. ERP houdt saldo per artikel + locatie.
3. Discrepantie tussen sticker en saldo: direct opvolgen.

**Grondslag**: Voorraadbeheer-doctrine

### 3. Periodieke + jaarlijkse inventaris

Cycle counts (steekproef) maandelijks + volledige inventaris jaarlijks; telling door iemand anders dan magazijnier.

**Waarom?** Tellen door magazijnier = niemand kan zijn fouten of diefstal ontdekken.

**🛠️ Hoe**:

1. Maandelijks: 10% van artikelen wisselend tellen.
2. Jaarlijks (typisch eind december): volledige telling met externe persoon (bv. medewerker boekhouding).
3. Verschillen ≥ drempel: onderzoeken + boeking + actieplan.

**Grondslag**: KB 21.10.2018 + ITAA-norm voorraadcontrole


## Valkuilen

> [!warning]- Magazijnier die zelf telt is geen onafhankelijke controle
> ⚠️ Magazijnier die zelf telt is geen onafhankelijke controle. Vereiste: 2e persoon, idealiter uit andere afdeling. 🤖


> [!warning]- Bestellingen in uitvoering (rekening 37) hebben een eigen waarderingsproblematiek (CBN 2012/15, 2016/14) — niet zomaar als voorraad behandel…
> ⚠️ Bestellingen in uitvoering (rekening 37) hebben een eigen waarderingsproblematiek (CBN 2012/15, 2016/14) — niet zomaar als voorraad behandelen. ⚖️
>
> _Bron: CBN 2012/15, 2016/14_



## Zie ook

- **Vereist kennis van**: [[functiescheiding]]

> [!todo] Voorbeeld ontbreekt voor dit concept
> Een latere ENRICH-pass voegt een synthese-voorbeeld toe.

## Bronnen

[^1]: `CBN-2012-15-bestellingen-in-uitvoering__sec_inleiding`
