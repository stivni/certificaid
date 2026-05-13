---
bron: https://www.cbn-cnc.be/nl/adviezen/aansprakelijk-vertegenwoordiger-tov-het-belastingbestuur
datum: 1990-06-01
nummer: CBN-advies 161/1
themas:
  - aansprakelijk vertegenwoordiger
  - aansprakelijk vertegenwoordiger t.o.v. het belastingbestuur
  - lasthebber van de buitenlandse BTW-plichtige
  - medecontractant
bron_rol: interpretatief
chunk:
  level: 2
  type: '##'
  sub_strategy:
provenance:
  inputs:
    - id: https://www.cbn-cnc.be/nl/adviezen/aansprakelijk-vertegenwoordiger-tov-het-belastingbestuur
      sha256:
      version:
  tooling:
    pipeline: tools/etl/convert.py
    pipeline_version: b4eac1f-dirty
    model:
    prompt_version:
  generated_at: '2026-05-12T23:37:56Z'
  stale: false
  stale_reason:
  trust:
    status: trusted
    confirmed_at: '2026-05-13T13:25:00Z'
    confirmed_by: subagent-sonnet-4-6
    rationale: "Regel 65: 'Volgens boekingen geven een beeld van de relaties...' is grammaticaal incorrect ('Volgende' ontbreekt). Gezien de HTML-bron (geen PDF/OCR) is dit hoogstwaarschijnlijk een source-typo op de CBN-website zelf — per de source-typo-uitzondering geen grond voor needs-rework. De vier boekhoudschema's in markdown pipe-syntax zijn intact en structureel correct; lege Debet/Credit-kolommen zijn inhoudelijk intentioneel. Geen andere artefacten."
    layer1:
      status: pass
      run_id: 20260512-233938
      run_at: '2026-05-12T23:39:40Z'
      heading_count: 0
      max_section_chars: 3629
      file_size_chars: 3629
      flags: []
    layer2:
      status: trusted
      agent: subagent-sonnet-4-6
      run_at: '2026-05-13T13:25:00Z'
      rationale: "Regel 65: 'Volgens boekingen geven een beeld van de relaties...' is grammaticaal incorrect ('Volgende' ontbreekt). Gezien de HTML-bron (geen PDF/OCR) is dit hoogstwaarschijnlijk een source-typo op de CBN-website zelf — per de source-typo-uitzondering geen grond voor needs-rework. De vier boekhoudschema's in markdown pipe-syntax zijn intact en structureel correct; lege Debet/Credit-kolommen zijn inhoudelijk intentioneel. Geen andere artefacten."
      concrete_problemen:
        - regel: 65
          categorie: (source)
          type: source-typo
          voorbeeld: Volgens boekingen geven een beeld van de relaties die ten aanzien van...
---
# CBN-advies 161/1 - Aansprakelijk vertegenwoordiger t.o.v. het belastingbestuur

Aan de Commissie werd de vraag gesteld op welke wijze de onderneming die aansprakelijk vertegenwoordiger is t.a.v. het belastingbestuur zulks boekhoudkundig moet tot uiting brengen. 

Rekening houdend met de wettelijke voorschriften inzake de aansprakelijk vertegenwoordiger[^1] en met de administratieve circulaire nr. 30/1975 van 5 december 1975, moet de onderneming die aansprakelijk vertegenwoordiger is, worden beschouwd als lasthebber van de buitenlandse btw-plichtige.

Aangezien de aansprakelijk vertegenwoordiger een voor de aard van zijn bedrijf passende boekhouding moet voeren, moet hieruit blijken dat de B.T.W. verschuldigd is door de buitenlandse belastingplichtige en niet door hem. 

Volgens boekingen geven een beeld van de relaties die ten aanzien van deze aansprakelijk vertegenwoordiger ontstaan :

     a) De aansprakelijk vertegenwoordiger ontvangt van de buitenlandse belastingplichtige een factuur gericht aan zijn medecontractant. De aansprakelijk vertegenwoordiger maakt een stuk op waarop onder meer het bedrag van de verschuldigde belasting voorkomt en stuurt het origineel van dit stuk naar de medecontractant van de belastingplichtige na aanhechting van de factuur :

| | Rekening | Omschrijving | Debet | Credit |
|---|----------|--------------|-------|--------|
| | 416 | Diverse vorderingen - rekening-courant lastgever X | | |
| aan | 489 | Andere diverse schulden : voor rekening van derden te betalen B.T.W. | | |

     b) De aansprakelijk vertegenwoordiger ontvangt van de lastgever of diens Belgische medecontractant de nodige middelen om de B.T.W. te vereffenen : 

| | Rekening | Omschrijving | Debet | Credit |
|---|----------|--------------|-------|--------|
| | 55 | Bank | | |
| aan | 416 | Diverse vorderingen - Rekening-courant van lastgever X | | |

     c) De aansprakelijk vertegenwoordiger stort het B.T.W.-Bestuur de te betalen B.T.W. : 

| | Rekening | Omschrijving | Debet | Credit |
|---|----------|--------------|-------|--------|
| | 489 | Andere diverse schulden : voor rekening van derden te betalen B.T.W. | | |
| aan | 55 | Bank | | |

    d) De aansprakelijk vertegenwoordiger ontvangt van het B.T.W.-bestuur een terugbetaling van B.T.W. : 

| | Rekening | Omschrijving | Debet | Credit |
|---|----------|--------------|-------|--------|
| | 55 | Bank | | |
| aan | 489 | Andere diverse schulden : voor rekening van derden te betalen B.T.W. | | |

Er zij op gewezen dat om het even welke boeking in verband met de relaties tussen de buitenlandse belastingplichtige en het B.T.W.-Bestuur of de Belgische medecontractant, via de aansprakelijk vertegenwoordiger, geen enkele weerslag heeft op de resultatenrekening van laatstgenoemde, tenzij hij boetes zou moeten betalen.

Daarentegen moeten in de boekhouding van de aansprakelijk vertegenwoordiger ook de verrichtingen worden opgenomen die voor zijn rekening komen, zoals honoraria die aan de buitenlandse belastingplichtige zijn gefactureerd, salarissen, kantoorkosten, enz. 

Bovendien zij erop gewezen dat artikel 55 van het B.T.W.-wetboek stelt dat de aansprakelijk vertegenwoordiger "hoofdelijk verplicht is ... de belasting, intresten en boetes te betalen ...". 

De verplichtingen van de aansprakelijk vertegenwoordiger komen in de regel voor op de passiefzijde van de balans. De zekerheden die hij zou stellen als waarborg voor deze verplichtingen worden uitgedrukt via de passende rekeningen met betrekking tot rechten en verplichtingen.

[^1]: Artikel 55 van het Btw-wetboek en koninklijk besluit nr. 31 van 29 december 1970.
