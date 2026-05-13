---
tags: ["VI.C", "2.4"]
itaa-lex-sectie: "VI.C"
wet: "M.B. 17 maart 2023 betreffende de vaststelling van de modaliteiten voor het bijhouden van een elektronisch dagboek van ontvangsten en de bewaring van elektronische kastickets"
bron_rol: "itaa_lex"
status: "beschikbaar"
bijgewerkt: "2023"
bron: "Fisconetplus.be (officieuze gecoördineerde versie)"
chunk:
  level: 2
  type: "Art."
  sub_strategy:
provenance:
  inputs:
    - id: resources/raw/wetteksten/btw-kbs/WBTW-MB-dagboek-ontvangsten-2023.pdf
      sha256: cd61a57a107e3959efafea39d3a999979703da0be22e70f146d17fdce3c0d927
      version: '2023'
  tooling:
    pipeline: tools/etl/convert.py
    pipeline_version: 8add68e
    model:
    prompt_version:
  generated_at: '2026-05-12T19:14:19Z'
  stale: false
  stale_reason:
  trust:
    status: trusted
    confirmed_at: '2026-05-12T19:27:16Z'
    confirmed_by: subagent-sonnet-4-6
    rationale: 'L1 pass: 3 headings, max sectie 3942 chars. Kleine MB correct verwerkt. Inhoud volledig (art. 1-9).'
    layer1:
      status: pass
      run_id: 20260513-104838
      run_at: '2026-05-13T10:48:42Z'
      heading_count: 3
      max_section_chars: 3942
      file_size_chars: 4943
      flags: []
    layer2:
      status: trusted
      agent: subagent-sonnet-4-6
      run_at: '2026-05-12T19:27:16Z'
      rationale: 'L1 pass: 3 headings, max sectie 3942 chars. Kleine MB correct verwerkt. Inhoud volledig (art. 1-9).'
      concrete_problemen: []
---

# BTW MB 17/03/2023 — Elektronisch dagboek ontvangsten en kastickets

*Bijgewerkt tot en met 2023 — gecoördineerde versie.*

17 MAART 2023. - Ministerieel besluit met betrekking tot de vaststelling van de modaliteiten voor het bijhouden van een elektronisch dagboek van ontvangsten en van een centralisatiedagboek enerzijds en de bewaring en de integriteit van de inhoud van de elektronische kastickets anderzijds, alsmede de modaliteiten voor de bewaring van de financiële rapporten

derde lid, van het koninklijk besluit nr. 1 van 29 december 1992 met betrekking tot de regeling voor de voldoening van de belasting over de toegevoegde waarde worden digitaal bewaard.

## Art. 7

De integriteit van de inhoud van de kastickets wordt verzekerd door het gebruik van een beveiligingssysteem toegepast op ononderbroken wijze door een reeks van volgnummers toegekend conform artikel 14, § 2, 3°, vierde lid, b), van het koninklijk besluit nr. 1 van 29 december 1992 met betrekking tot de regeling voor de voldoening van de belasting over de toegevoegde waarde. Dit beveiligingssysteem:
a) registreert elke volledige lijn van een kasticket van zodra zij wordt uitgewerkt door het informaticasysteem en verhindert elke wijziging of verwijdering van deze registratie;
b) genereert een digitale handtekening van de registratie met inbegrip van de totalen van een kasticket bedoeld in punt c) bij de behandeling door het informaticasysteem.
De digitale handtekening moet worden toegepast op de volgende gegevens/velden van het kasticket met uitsluiting van elke andere:

- les huit derniers caractères de la                           - de acht laatste karakters van de signature digitale de l'enregistrement        (alphanumérique) digitale handtekening van de       (alfanumeriek) précédent                                                      vorige registratie - la date                                     YYYYMMDD               - de datum                            YYYYMMDD - het nummer van de vestiging - le numéro de l'établissement (si utilisé)   (numérique)                                                  (numeriek) (indien gebruikt) - l'identification de la caisse               (numérique)            - de identificatie van de kassa       (numeriek) - le numéro d'ordre du ticket                 (numérique)            - het volgnummer van het ticket       (numeriek) - de som van de totaalbedragen - la somme des montants totaux par article                           per artikel bedoeld in het artikel visés à l'article 14, § 2, 3°, alinéa 4, d), de                      14, § 2, 3°, vierde lid, d) van het l'arrêté royal n° 1 du 29 décembre 1992         (numérique)          koninklijk besluit nr. 1 van 29       (numeriek) relatif aux mesures tendant à assurer le                             december 1992 met betrekking paiement de la taxe sur la valeur ajoutée                            tot de regeling voor de voldoening van de belasting - het totaalbedrag van het ticket * - le montant total du ticket * 100            (numérique)                                                (numeriek)

Iedere registratie van de totalen van een kasticket wordt verbonden met het voorgaande door het opnemen van de acht laatste karakters van de digitale handtekening van de vorige registratie in de berekening van de betrokken registratie. Alsook, geen enkele registratie zal later nog kunnen geplaatst of verwijderd worden zonder de digitale handtekening zelf te wijzigen.
c) voorziet dat de registratie die de totalen van het kasticket bevat minimaal de volgende gegevens bevat: - de laatste acht karakters van de digitale handtekening van de vorige registratie;
- de datum van afgifte van het kasticket aan de klant;
- het volgnummer (minimum 4 en maximum 8 posities);
- de identificatie van de kassa en, indien er meerdere vestigingen zijn, de identificatie van de vestiging;
- de som van de totaalbedragen bedoeld in het artikel 7, b), tweede lid, zesde streepje, hiervoor. Deze som moet worden weergegeven als een veld met twee decimale plaatsen;
- het totaalbedrag, BTW inbegrepen, te betalen door de klant of, in voorkomend geval, het saldo te betalen aan de klant. Dit bedrag moet worden weergegeven als een veld met twee decimale plaatsen;
- de laatste acht karakters van de digitale handtekening;
d) registreert onmiddellijk alle beveiligde registraties in een afzonderlijk bestand dat de volgende eigenschappen bezit: opeenvolgend (flat file), ongecomprimeerd en niet geëncrypteerd;
e) drukt de laatste acht karakters van de digitale handtekening af op het originele kasticket dat is afgeleverd aan de klant.

## Art. 8

De financiële rapporten, bedoeld in artikel 14, § 2, 3°, vijfde lid, van het koninklijk besluit van 29 december 1992 nr. 1 met betrekking tot de regeling voor de voldoening van de belasting over de toegevoegde waarde, worden bewaard op digitale wijze.

## Art. 9

Dit besluit treedt in werking op 1 april 2023.