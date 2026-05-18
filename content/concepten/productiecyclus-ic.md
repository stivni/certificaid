---
title: Productiecyclus — interne controle
tags:
- concept
- procedure
- po-1-7
linked_anchors:
- 1.7.IX.B
- 1.7.IX
programmaonderdelen:
- '1.7'
confidence: inferred
node_type: procedure
status: seed
schema_version: '1.4'
gegenereerd_uit: data/concepten/records/productiecyclus-ic.json
gegenereerd_op: '2026-05-18'
---
# Productiecyclus — interne controle 🤖

> [!summary] Korte inhoud
> Boekhoudkundige verplichting tot juiste voorraadwaardering en cost-allocation.

> [!info] Behoort tot: [[interne-controle]]

Boekhoudkundige verplichting tot juiste voorraadwaardering en cost-allocation.


## Stappen

### 1. Productieplanning + uitgifte grondstoffen

Productieorder maken; grondstoffen uit magazijn uitgeven volgens stuklijst (BOM).

**Waarom?** Zonder formele uitgifte tracking: 'verdwijnen' van grondstoffen niet detecteerbaar.

**🛠️ Hoe**:

1. Productieorder met BOM in ERP.
2. Magazijnier geeft uit; ERP boekt voorraadafname.
3. Afwijking BOM ↔ werkelijk verbruik: opvolgen.

**Grondslag**: Productie-IC-doctrine

### 2. Productie-uitvoering + rapportering

Voltooide producten naar voorraad gereed product; afval/uitval boeken.

**Waarom?** Afval niet boeken = voorraad te hoog gewaardeerd; ook signaal voor proces-inefficiëntie of diefstal.

**🛠️ Hoe**:

1. Operator scant voltooide eenheid + uitval.
2. ERP boekt automatisch in voorraad gereed product.
3. Periodieke yield-analyse per machine + operator.

**Grondslag**: Productie-IC-doctrine

### 3. Kostprijsberekening + voorraadwaardering

Grondstoffenkost + directe arbeid + overhead toewijzen aan voltooide producten.

**Waarom?** Verkeerde kostprijs → verkeerde voorraadwaardering → verkeerd brutoresultaat.

**🛠️ Hoe**:

1. Maandelijks: actual cost rekenen op basis van werkelijke productie.
2. Vergelijk met standaardkost; analyseer variantie.
3. Adjustments boeken indien materiële afwijking.

**Grondslag**: KB WVV — voorraadwaardering


## Zie ook

- **Vereist kennis van**: [[functiescheiding]]

> [!todo] Voorbeeld ontbreekt voor dit concept
> Een latere ENRICH-pass voegt een synthese-voorbeeld toe.

