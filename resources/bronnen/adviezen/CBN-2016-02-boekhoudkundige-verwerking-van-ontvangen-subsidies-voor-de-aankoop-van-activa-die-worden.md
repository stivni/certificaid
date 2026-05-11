---
bron: https://www.cbn-cnc.be/nl/adviezen/boekhoudkundige-verwerking-van-ontvangen-subsidies-voor-de-aankoop-van-activa-die-worden
datum: 2016-03-09
gerelateerde_adviezen:
  - datum: '2022-07-20'
    titel: Wijziging van het boekhoudkundig referentiestelsel
    url: https://www.cbn-cnc.be/nl/adviezen/wijziging-van-het-boekhoudkundig-referentiestelsel
  - datum: '2011-07-06'
    titel: Herwaarderingsmeerwaarden
    url: https://www.cbn-cnc.be/nl/adviezen/herwaarderingsmeerwaarden
  - datum: '1991-03-01'
    titel: Verwerking van verrichtingen voor de verwerving of verkoop van een recht op vruchtgebruik of van naakte eigendom op materiële vaste activa in de boekhouding van de vruchtgebruiker (de erfpachter, de opstalhouder) en van de naakte eigenaar (de grondeigenaa
    url: https://www.cbn-cnc.be/nl/adviezen/verwerking-van-verrichtingen-voor-de-verwerving-of-verkoop-van-een-recht-op-vruchtgebruik
  - datum: '1986-07-01'
    titel: Bouwwerken op andermans grond
    url: https://www.cbn-cnc.be/nl/adviezen/bouwwerken-op-andermans-grond
nummer: CBN-advies 2016/2
provenance:
  inputs:
    - id: https://www.cbn-cnc.be/nl/adviezen/boekhoudkundige-verwerking-van-ontvangen-subsidies-voor-de-aankoop-van-activa-die-worden
      sha256: 074350628fb9f6a0648fb610e585e68c7bac08b5f35a1156be111a403d2c830a
      version:
  tooling:
    pipeline: tools/etl/convert.py
    pipeline_version: 3b788cd
    model:
    prompt_version:
  generated_at: '2026-05-11T13:15:12Z'
  stale: false
  stale_reason:
  trust:
    status: needs-rework
    confirmed_at: '2026-05-11T13:30:32Z'
    confirmed_by: subagent-sonnet-4-6
    rationale: 'Regels 59–65: de drie titels zijn gemarkeerd als `# **COMMISSIE...` en `# **CBN-advies...` zonder sluitende `**`, en `## **Inleiding****` bevat overtollige asterisken — malformed bold/italic (D4). Regel 72: lege heading `## ` zonder tekst (B3). Inhoud zelf is correct en voetnoten [^1] en [^2] zijn aanwezig.'
    layer1:
      status: pass
      run_id: 20260511-131513
      run_at: '2026-05-11T13:15:17Z'
      heading_count: 2
      max_section_chars: 2264
      file_size_chars: 3169
      flags: []
    layer2:
      status: needs-rework
      agent: subagent-sonnet-4-6
      run_at: '2026-05-11T13:30:32Z'
      rationale: 'Regels 59–65: de drie titels zijn gemarkeerd als `# **COMMISSIE...` en `# **CBN-advies...` zonder sluitende `**`, en `## **Inleiding****` bevat overtollige asterisken — malformed bold/italic (D4). Regel 72: lege heading `## ` zonder tekst (B3). Inhoud zelf is correct en voetnoten [^1] en [^2] zijn aanwezig.'
      concrete_problemen:
        - regel: 59
          categorie: D4
          type: other
          voorbeeld: '# **COMMISSIE VOOR BOEKHOUDKUNDIGE NORMEN (geen sluitende **)'
        - regel: 61
          categorie: D4
          type: other
          voorbeeld: '# **CBN-advies 2016/2 – Boekhoudkundige verwerking... (geen sluitende **)'
        - regel: 63
          categorie: D4
          type: other
          voorbeeld: '# **Advies van 9 maart 2016** (sluit wel, maar titelbold in heading is onnatuurlijk)'
        - regel: 65
          categorie: D4
          type: other
          voorbeeld: '## **Inleiding**** (dubbele afsluitende asterisken)'
        - regel: 72
          categorie: B3
          type: other
          voorbeeld: '## (lege heading zonder tekst)'
themas:
  - materiële vaste activa
  - overige materiële vaste activa
  - subsidies
  - terbeschikkingstelling vaste activa
  - vereniging zonder winstoogmerk
  - vzw
---

# **COMMISSIE VOOR BOEKHOUDKUNDIGE NORMEN

# **CBN-advies 2016/2 – Boekhoudkundige verwerking van ontvangen subsidies voor de aankoop van activa die worden ter beschikking gesteld

# **Advies van 9 maart 2016**

## **Inleiding****

Aan de Commissie werd de vraag gesteld hoe een VZW (VZW ABC) materiële vaste activa boekhoudkundig dient te verwerken die ter beschikking worden gesteld aan een andere VZW (VZW XYZ). Deze materiële vaste activa worden fysiek overgedragen door VZW ABC aan VZW XYZ; op het einde van de economische levensduur worden deze materiële vaste activa terug overgedragen door VZW XYZ aan VZW ABC. Gedurende de terbeschikkingstelling kan VZW ABC deze materiële vaste activa niet vervreemden.

Daarnaast worden er aan VZW XYZ tevens subsidies toegekend die worden uitbetaald aan VZW ABC ter financiering van de investeringen in de betrokken materiële vaste activa.

## 

**Analyse****

In hetgeen volgt gaan we ervan uit dat het Koninklijk Besluit van 19 december 2003 (hierna: KB 19.12.2003) van toepassing is op VZW ABC.

Op het ogenblik van de toekenning van de subsidies zal VZW ABC deze als volgt boekhoudkundig verwerken:

| | Rekening | Omschrijving | Debet | Credit |
|---|----------|--------------|-------|--------|
| | 413 | Te ontvangen subsidies | | |
| aan | 151 | Kapitaalsubsidies ontvangen in contanten | | |

Op het ogenblik van de ontvangst van de subsidies zal VZW ABC deze als volgt boekhoudkundig verwerken: 

| | Rekening | Omschrijving | Debet | Credit |
|---|----------|--------------|-------|--------|
| | 550 | Kredietinstellingen: rekening-courant | | |
| aan | 413 | Te ontvangen subsidies | | |

Vervolgens worden de desbetreffende materiële vaste activa aangekocht. Aangezien de VZW ABC deze materiële vaste activa niet voor eigen gebruik zal hanteren, dienen deze activa te worden geboekt op de rekening 232 *Overige installaties, machines en uitrusting**[^1]** *.

Artikel 19, § 1, 2° KB 19.12.2003 specifieert immers dat hieronder de materiële vaste activa worden opgenomen waarvan de vereniging de volle eigendom heeft, maar die ze niet vrij mag gebruiken of waarover zij niet vrij kan beschikken omwille van bepaalde eisen.

Na aankoop zal de VZW ABC de materiële vaste activa fysiek overdragen aan VZW XYZ. Gedurende de periode van de terbeschikkingstelling zal VZW ABC deze activa afschrijven over haar economische levensduur en wordt de ontvangen kapitaalsubsidie gespreid in resultaat erkend.

Op het ogenblik dat VZW XYZ deze materiële vaste activa terug fysiek overdraagt aan de VZW ABC zal laatstgenoemde een eventuele aanvullende afschrijving op deze materiële vaste activa erkennen wanneer ingevolge hun technische ontwaarding of wegens wijziging van economische of technologische omstandigheden, hun boekwaarde hoger is dan hun gebruikswaarde[^2] voor de VZW ABC.

[^1]: Afhankelijk van de aard van de activa zal de vereniging rekening 2202 Overige terreinen, 2212 Overige gebouwen, 2222 Overige bebouwde terreinen, 232 Overige installaties, machines en uitrusting, 242 Overig meubilair en rollend materieel of 262 Overige materiële vaste activa hanteren.

[^2]: Art. 64 § 1, tweede lid, KB 19.12.2003.
