---
bron: https://www.cbn-cnc.be/nl/adviezen/overdracht-van-schuldvordering-nominale-waarde-waardevermindering
datum: 1988-01-01
gerelateerde_adviezen:
  - datum: '2025-07-14'
    titel: Waardeverminderingen op handelsvorderingen, gedekt door een kredietverzekering (update) [ONTWERP]
    url: https://www.cbn-cnc.be/nl/adviezen/waardeverminderingen-op-handelsvorderingen-gedekt-door-een-kredietverzekering-update
  - datum: '2021-07-05'
    titel: Boekhoudkundige verwerking van COVID-19-tegemoetkomingen en van kosten gemaakt ten gevolge van de gezondheidscrisis
    url: https://www.cbn-cnc.be/nl/adviezen/boekhoudkundige-verwerking-van-covid-19-tegemoetkomingen-en-van-kosten-gemaakt-ten-gevolge
  - datum: '2012-10-10'
    titel: De boekhoudkundige verwerking van immateriële vaste activa
    url: https://www.cbn-cnc.be/nl/adviezen/de-boekhoudkundige-verwerking-van-immateriele-vaste-activa
  - datum: '2011-10-05'
    titel: De boekhoudkundige verwerking van factoringovereenkomsten
    url: https://www.cbn-cnc.be/nl/adviezen/de-boekhoudkundige-verwerking-van-factoringovereenkomsten
nummer: CBN-advies 137/6
themas:
  - Waardevermindering
  - waardevermindering op vorderingen
  - nominale waarde
  - overdracht van schuldvordering
  - vordering
bron_rol: interpretatief
chunk:
  level: 2
  type: '##'
  sub_strategy:
provenance:
  inputs:
    - id: https://www.cbn-cnc.be/nl/adviezen/overdracht-van-schuldvordering-nominale-waarde-waardevermindering
      sha256:
      version:
  tooling:
    pipeline: tools/etl/convert.py
    pipeline_version: b4eac1f-dirty
    model:
    prompt_version:
  generated_at: '2026-05-12T23:37:44Z'
  stale: false
  stale_reason:
  trust:
    status: trusted
    confirmed_at: '2026-05-13T13:45:17Z'
    confirmed_by: subagent-sonnet-4-6
    rationale: Geen ETL-artefacten aangetroffen. Heading-structuur aanwezig (4 headings), inhoud volledig, voetnoten correct gerenderd, geen form-feeds of column-bleed.
    layer1:
      status: pass
      run_id: 20260512-233938
      run_at: '2026-05-12T23:39:40Z'
      heading_count: 3
      max_section_chars: 1158
      file_size_chars: 3513
      flags: []
    layer2:
      status: trusted
      agent: subagent-sonnet-4-6
      run_at: '2026-05-13T13:45:17Z'
      rationale: Geen ETL-artefacten aangetroffen. Heading-structuur aanwezig (4 headings), inhoud volledig, voetnoten correct gerenderd, geen form-feeds of column-bleed.
      concrete_problemen: []
---
# CBN-advies 137/6 - Overdracht van schuldvordering - Nominale waarde - Waardevermindering

Artikel 27*bis*, § 1 van het jaarrekeningbesluit bepaalt dat vorderingen in de balans worden opgenomen voor hun nominale waarde, onverminderd evenwel de verplichting om op de betrokken vorderingen waardeverminderingen toe te passen zo er voor het geheel of een gedeelte ervan onzekerheid bestaat over de betaling ervan op de vervaldag[^1].

Aan de Commissie werd volgend concreet toepassingsgeval van deze bepaling voorgelegd.

Onderneming Y draagt aan onderneming X een vordering op Z over. Nominaal bedraagt de vordering 100 doch de kans op realisatie van de vordering wordt gering geacht. De vordering in kwestie wordt aan X overgedragen tegen 40.

Naar het oordeel van de Commissie leidt de toepassing van artikel 27*bis*, § 1 voor X in casu tot de volgende boekhoudkundige verwerking.

## Bij de aankoop van de vordering
| | Rekening | Omschrijving | Debet | Credit |
|---|----------|--------------|-------|--------|
| | 2907 | Handelsvorderingen (op meer dan 1 jaar) dubieuze debiteuren | 100 | |
| aan | 2909 | Handelsvorderingen - geboekte waardeverminderingen | | 60 |
| | 55 | Kredietinstellingen | 40 | |

Deze boekingswijze heeft tot gevolg - en zulks acht de Commissie juridisch gezien essentieel - dat uit de boekhouding van schuldeiser X het nominaal bedrag van de van Y verworven vordering blijkt, wat overeenstemt met het bedrag ten belope waarvan schuldenaar Z door X op de vervaldag kan worden aangesproken. 

De sub 2909 geboekte "waardevermindering" stemt overeen met het bedrag waarvoor in de boekhouding van Y als gevolg van de overdracht van schuldvordering een minderwaarde op de realisatie van deze vordering werd geboekt. 

Deze "waardevermindering" werd niet ten laste genomen door de resultatenrekening van X, maar tesamen met de betrokken vordering van Y "verworven". 

## Ingeval van de verbetering van de solvabiliteit van Z : de vordering word op 60 geschat.
(toepassing van artikel 19, zesde lid K.B. van 8 oktober 1976) 

| | Rekening | Omschrijving | Debet | Credit |
|---|----------|--------------|-------|--------|
| | 2909 | Handelsvorderingen op meer dan 1 jaar - geboekte waardeverminderingen | 20 | |
| aan | 6331 | Handelsvorderingen op meer dan 1 jaar - terugneming van waardeverminderingen | | 20 |

## Op de vervandag
(Z betaalt uiteindelijk 70) 

| | Rekening | Omschrijving | Debet | Credit |
|---|----------|--------------|-------|--------|
| | 55 | Kredietinstellingen | 70 | |
| | 2909 | Handelsvorderingen op meer dan 1 jaar - geboekte waardeverminderingen | 40 | |
| aan | 2907 | Handelsvorderingen - dubieuze debiteuren | | 100 |
| | 6331 | Handelsvorderingen op meer dan 1 jaar -terugneming van waardeverminderingen 1 | 10 | |

Uit hetgeen voorafgaat blijkt tevens dat de Commissie van oordeel is dat artikel 27*bis*, § 2, b) in het betrokken geval niet mag worden toegepast daar het verschil tussen de nominale waarde van de betrokken vordering (100) en de waarde waartegen zij werd verkregen (40) in casu geenszins overeenstemt met een (impliciet berekende) interest, maar wel met een waardevermindering. De *ratio legis* van artikel 27*bis*, § 2, b) zoals deze blijkt uit het Verslag aan de Koning dat het besluit van 12 september 1983 tot wijziging van het jaarrekeningbesluit van 12 september 1983 tot wijziging van het jaarrekeningbesluit voorafgaat, is hier duidelijk niet voorhanden. 

[^1]: Cf. de verwijzing naar artikel 31 in fine van § 1, artikel 27bis.
