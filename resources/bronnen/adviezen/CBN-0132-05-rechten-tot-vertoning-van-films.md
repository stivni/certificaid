---
bron: https://www.cbn-cnc.be/nl/adviezen/rechten-tot-vertoning-van-films
datum: 1991-03-01
gerelateerde_adviezen:
  - datum: '2016-10-26'
    titel: Kilometerheffing
    url: https://www.cbn-cnc.be/nl/adviezen/kilometerheffing
  - datum: '1988-01-21'
    titel: Werkende vennoten
    url: https://www.cbn-cnc.be/nl/adviezen/werkende-vennoten
  - datum: '1988-12-01'
    titel: Boeking van commissies
    url: https://www.cbn-cnc.be/nl/adviezen/boeking-van-commissies
  - datum: '1986-01-01'
    titel: Materiële vaste activa - Onderscheid met voorraden
    url: https://www.cbn-cnc.be/nl/adviezen/materiele-vaste-activa-onderscheid-met-voorraden
nummer: CBN-advies 132/5
provenance:
  inputs:
    - id: https://www.cbn-cnc.be/nl/adviezen/rechten-tot-vertoning-van-films
      sha256: 01839fec25050d00ee08d40374ee0706fef1ac979531ff432708d211921e7e43
      version:
  tooling:
    pipeline: tools/etl/convert.py
    pipeline_version: 3b788cd
    model:
    prompt_version:
  generated_at: '2026-05-11T15:15:31Z'
  stale: false
  stale_reason:
  trust:
    status: needs-rework
    confirmed_at: '2026-05-11T15:15:33Z'
    confirmed_by: subagent-sonnet-4-6
    rationale: "A6 op L75: voetnootmarker [^1] gecombineerd met een leading-space line-break breekt de zin midden in ('...te worden gebruikt[^1] en derhalve niet...'). D4 op L89: 'onder* Diensten en diverse goederen*' — openende asterisk staat zonder spatie na 'onder', wat de italic-span slecht formatteert. Bevestiging van eerder layer2-verdict."
    layer1:
      file_size_chars: 3015
      flags: []
      heading_count: 0
      max_section_chars: 3015
      run_at: '2026-05-11T15:05:48Z'
      run_id: 20260511-150547
      status: pass
    layer2:
      status: needs-rework
      agent: subagent-sonnet-4-6
      run_at: '2026-05-11T15:15:33Z'
      rationale: "A6 op L75: voetnootmarker [^1] gecombineerd met een leading-space line-break breekt de zin midden in ('...te worden gebruikt[^1] en derhalve niet...'). D4 op L89: 'onder* Diensten en diverse goederen*' — openende asterisk staat zonder spatie na 'onder', wat de italic-span slecht formatteert. Bevestiging van eerder layer2-verdict."
      concrete_problemen:
        - regel: 75
          categorie: A6
          type: other
          voorbeeld: '...te worden gebruikt[^1] en derhalve niet als een vast actief...'
        - regel: 89
          categorie: D4
          type: other
          voorbeeld: '...wanneer de uitzendrechten onder* Diensten en diverse goederen* werden geboekt.'
themas:
  - diensten en diverse goederen
  - immateriële vaste activa
  - rechten tot vertoning van films
  - uitzendrechten
  - vertoningsrechten
  - voorraden
---

# CBN-advies 132/5 - Rechten tot vertoning van films

De Commissie werd om advies gevraagd over de boekhoudkundige verwerking van het bedrag dat een onderneming (bedoeld wordt een bioscoopuitbater of een televisieomroep) betaalt voor de verwerving van het recht tot vertoning van een film. 

De vraag of de sommen betaald voor dergelijke vertoningsrechten - die een beperkte draagwijdte hebben zowel in de tijd als in de ruimte - moeten worden geactiveerd als immateriële vaste activa en als dusdanig boekhoudkundig worden behandeld, is door de Commissie negatief beantwoord. Zij heeft geoordeeld dat deze verwerving van vertoningsrechten in casu niet kan worden gekwalificeerd als de verwerving van een vermogensbestanddeel bestemd om duurzaam voor de bedrijfsuitoefening van de bioscoopuitbater te worden gebruikt[^1] en derhalve niet als een vast actief kon worden geboekt. Zij heeft geadviseerd de betrokken sommen als courante bedrijfskosten hetzij als voorraadaankopen, hetzij als diensten en diverse goederen rechtstreeks ten laste te nemen in de resultatenrekening over de betrokken periode. 

Hier moeten inderdaad twee hypothesen worden onderscheiden. 

Wanneer voor een onderneming het uitzenden of vertonen van films het hoofdbedrijf uitmaakt, lijkt het naar het oordeel van de Commissie aangewezen de betrokken uitzendrechten boekhoudkundig te verwerken als voorraadaankopen (rekening 60 van het algemeen rekeningenstelsel). 

In de andere hypothese adviseert de Commissie de betrokken uitzendrechten te boeken onder *Diensten en diverse goederen* (rekening 61 van het algemeen rekeningenstelsel). 

Het spreekt echter vanzelf dat de Commissie in casu niet adviseert het beginsel van de kosten-en opbrengstentoerekening (matching principle) terzijde te schuiven. Vanuit die optiek is het niet toelaatbaar alle aankopen van uitzendrechten ten laste te nemen van een bepaald boekjaar, daar waar de vertoningen of uitzendingen later zullen plaatsvinden en de daaruit voortvloeiende opbrengsten[^2] ten gunste van een volgend boekjaar zullen worden geboekt. 

Het lijkt de Commissie derhalve noodzakelijk dat de betrokken kostenboekingen voor de opstelling van de jaarrekening worden gecorrigeerd teneinde de exacte periodekost te bepalen. 

Wanneer, overeenkomstig wat voorafgaat, de uitzendrechten als voorraadbestanddelen moeten worden beschouwd, wordt de periodekost aan actiefzijde van de balans gecorrigeerd via de rekening *Voorraadwijzigingen* voor de uitzendrechten die aan het einde van het boekjaar nog niet zijn verbruikt. Het zal vanzelfsprekend ook aangewezen zijn deze actiefpost een passende benaming te geven (cf. artikel 9, tweede lid K.B. 8 oktober 1976). 

De periodekost wordt gecorrigeerd via de overlopende rekeningen (actiefrekening 490 *Over te dragen kosten*) wanneer de uitzendrechten onder* Diensten en diverse goederen* werden geboekt.

[^1]: Cf. artikel 15, § 2, 4de E.E.G.-richtlijn.

[^2]: Ook al zijn deze slechts onrechtstreeks toerekenbaar aan de betrokken vertoningen.
