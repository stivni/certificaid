---
bron_categorie: isa
bron_rol: itaa_lex
chunk:
  level: 2
  sub_strategy: null
  type: Sectie
itaa-lex-sectie: ISA
norm: ''
provenance:
  generated_at: '2026-05-16T19:30:12Z'
  inputs: []
  stale: false
  stale_reason: null
  tooling:
    model: null
    pipeline: tools/download/scrape_ibr_isa.py (subagent a2fee1b5)
    pipeline_version: '1.0'
    prompt_version: null
  trust:
    status: needs-rework
    confirmed_at: '2026-05-16T20:31:37Z'
    confirmed_by: subagent-qa-2026-05-16
    rationale: >-
      QA-pass 2026-05-16: pymupdf-conversie via tools/download/scrape_ibr_isa.py extraheerde
      tekst lineair zonder structurele heading-injectie (0 ##-headings in body). Page-footers
      ('ALGEHELE DOELSTELLINGEN ... ISA 200 NBA-IBR 2022 N/M Originele bron: Handbook ... Versie
      2023') repeteren ~elke pagina inline. Paragraph-numbers ('1.', '2.') staan op aparte
      regels van hun body-tekst, en bullets ('• item') zijn losgekoppeld van hun bullet-marker.
      RAG-chunking faalt zonder heading-grenzen — ETL-fix nodig: inject_headings_isa +
      strip_isa_page_footers transformers.
    layer1: null
    layer2: null
status: beschikbaar
tags: []
title: ''
uitgever: IAASB / NBA-IBR
---

# ISA 570 (herzien) — Continuïteit

[Online raadplegen (IBR-IRE)](https://www.ibr-ire.be/docs/default-source/nl/documents/regelgeving-en-publicaties/rechtsleer/normen-en-aanbevelingen/isa-s/nieuwe-en-herziene-isa-s/new-and-revised-isas-2017-update-24062019/isa-570-(herzien)_nl_2023.pdf) · ibr-ire.be

## Overzicht sleutelpassages

| Paragraaf | Onderwerp |
|---|---|
| [Par. 2](#par-2) | Continuïteitsveronderstelling — definitie |
| [Par. 6](#par-6) | Verantwoordelijkheid auditor |
| [Par. 9](#par-9) | Doelstellingen auditor |
| [Par. 13](#par-13) | Beoordelingsperiode (12 maanden) |
| [Par. 16](#par-16) | Aanvullende werkzaamheden bij twijfel |
| [Par. 21–24](#par-21-24) | Implicaties voor de controleverklaring |
| [Par. A3](#par-a3) | Indicatoren van going concern-twijfel |

## Par. 2

**Continuïteitsveronderstelling**

Uitgaande van de continuïteitsveronderstelling worden de financiële overzichten opgesteld onder de veronderstelling dat de continuïteit van de entiteit gehandhaafd blijft en zij haar activiteiten in de voorzienbare toekomst zal voortzetten. Activa en passiva worden opgenomen vanuit de veronderstelling dat de entiteit in staat zal zijn haar activa te realiseren en haar verplichtingen na te komen in het kader van de normale bedrijfsvoering.

## Par. 6

**Verantwoordelijkheid van de auditor**

Het is de verantwoordelijkheid van de auditor om voldoende en geschikte controle-informatie te verkrijgen met betrekking tot de geschiktheid van het hanteren van de continuïteitsveronderstelling en om te concluderen of er sprake is van een onzekerheid van materieel belang met betrekking tot de mogelijkheid van de entiteit om haar continuïteit te handhaven.

## Par. 9

**Doelstellingen van de auditor**

a) Voldoende en geschikte controle-informatie verkrijgen over de geschiktheid van de continuïteitsveronderstelling;
b) Concluderen of er een onzekerheid van materieel belang bestaat;
c) Rapporteren overeenkomstig de ISA.

## Par. 13

**Beoordelingsperiode**

Bij de evaluatie van de beoordeling door het management dient de auditor dezelfde periode te hanteren als de periode waarop de beoordeling door het management betrekking heeft. Als de beoordeling van het management minder dan twaalf maanden na de balansdatum bestrijkt, verzoekt de auditor het management zijn beoordeling uit te breiden tot minimaal twaalf maanden na de balansdatum.

## Par. 16

**Aanvullende werkzaamheden bij geïdentificeerde twijfel**

Wanneer gebeurtenissen of omstandigheden worden geïdentificeerd die gerede twijfel kunnen doen ontstaan:

a) Management verzoeken zijn beoordeling te maken van de mogelijkheid om continuïteit te handhaven;
b) Plannen van het management evalueren op haalbaarheid en of ze de situatie verbeteren;
c) Kasstroomprognoses evalueren;
d) Aanvullende informatie of schriftelijke bevestigingen opvragen.

## Par. 21–24

**Implicaties voor de controleverklaring**

| Situatie | Gevolg voor controleverklaring |
|---|---|
| Continuïteitsveronderstelling niet passend | Afkeurend oordeel |
| Continuïteit passend + onzekerheid materieel belang + adequate toelichting | Goedkeurend oordeel + aparte sectie "Onzekerheid van materieel belang omtrent de continuïteit" |
| Continuïteit passend + onzekerheid materieel belang + geen adequate toelichting | Oordeel met beperking of afkeurend oordeel |

## Par. A3

**Indicatoren van going concern-twijfel (niet-limitatief)**

*Financieel:*
- Nettovlottende passiva of nettopasiva
- Leningen met vervaldatum zonder uitzicht op herfinanciering
- Aanwijzingen voor intrekking van financiering door verstrekkers
- Negatieve operationele kasstromen
- Ongunstige financiële verhoudingscijfers
- Substantiële operationele verliezen of significante waardedaling activa
- Achterstanden in dividenduitkeringen of stopzetting
- Onmogelijkheid om crediteuren op vervaldag te betalen
- Niet naleven van leningvoorwaarden (covenants)
- Overschakeling op levering onder rembours door leveranciers

*Operationeel:*
- Intentie tot liquidatie of beëindiging van activiteiten
- Vertrek van kernpersonen zonder vervanging
- Verlies van cruciale markt, klant, licentie of leverancier
- Arbeidsconflicten of tekorten aan grondstoffen/voorraden

*Overig:*
- Niet naleven van kapitaalvereisten of solvabiliteits-/liquiditeitsvereisten
- Lopende procedures met potentieel onoverzienbare claims
- Nadelige wetswijzigingen of overheidsbeleid
- Rampen zonder adequate verzekering

## Gebruikte concepten

[[continuiteitsrisico]]