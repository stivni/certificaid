---
tags: ["2.8"]
itaa-lex-sectie: ""
wet: "Circulaire 2022/C/106 over de afzonderlijk belastbare inkomsten die bij verdrag zijn vrijgesteld — FOD Financiën AAFisc PB"
bron_rol: "interpretatief"
status: "beschikbaar"
bijgewerkt: "07.11.2022"
bron: "onbekend"
chunk:
  level: 2
  type: "Art."
  sub_strategy:
provenance:
  inputs:
    - id: resources/raw/handcrafted/Circ-2022-C-106-afzonderlijk-belastbaar-verdrag-vrijgesteld.md
      sha256: 8b769cd0418890fecffb6d57eff8d0b2ed26d6c67412cbbb050752700e20dfd0
      version: 07.11.2022
      pages:
  tooling:
    pipeline: tools/etl/convert.py
    pipeline_version: 0c77206e-dirty
    model:
    prompt_version:
  generated_at: '2026-05-19T18:26:10Z'
  stale: false
  stale_reason:
  trust:
    status: trusted
    confirmed_at: '2026-05-19T18:51:56Z'
    confirmed_by: subagent-sonnet-4-6
    rationale: Korte circulaire (116 regels) met heldere drieledige structuur (I/A-C, II, III). Alle paragrafen genummerd 1-9, doorlopende narratieve tekst, voetnoten correct als Markdown footnotes, blockquote correct voor geciteerde wetsartikelen, geen TOC-bleed of extractie-artefacten. Frontmatter matcht inhoud volledig.
    caveat:
    layer1:
      status: pass
      run_id: 20260519-182610
      run_at: '2026-05-19T18:26:10Z'
      heading_count: 8
      max_section_chars: 3607
      file_size_chars: 6329
      flags: []
    layer2:
      status: trusted
      agent: subagent-sonnet-4-6
      run_at: '2026-05-19T18:51:56Z'
      rationale: Korte circulaire (116 regels) met heldere drieledige structuur (I/A-C, II, III). Alle paragrafen genummerd 1-9, doorlopende narratieve tekst, voetnoten correct als Markdown footnotes, blockquote correct voor geciteerde wetsartikelen, geen TOC-bleed of extractie-artefacten. Frontmatter matcht inhoud volledig.
      concrete_problemen:
        - "Lijn 88: voetnoot 3 verwijst naar 'W 21.01.2021' (jaartal 2021 in plaats van 2022) — dit is een typo in de brontekst, niet een extractie-artefact; (source)-flag."
        - Inhoudstafel op lijn 48-56 is als plain-tekst-lijst bewaard (niet als headings), direct gevolgd door de echte headings — dit is correct gedrag maar de TOC-blokken zijn niet visueel afgescheiden (geen thematische scheidingsregel). Functioneel geen probleem voor de RAG-chunker.
---

# Circulaire 2022/C/106 over de afzonderlijk belastbare inkomsten die bij verdrag zijn vrijgesteld — FOD Financiën AAFisc PB

*Bijgewerkt tot en met 07.11.2022 — gecoördineerde versie.*

## Inhoudstafel

- I. Bespreking
  - A. Vrijstelling met progressievoorbehoud
  - B. Belasting tegen een afzonderlijke aanslagvoet
  - C. Aanvullende gemeentebelasting
- II. Inwerkingtreding
- III. Wetteksten

## I. BESPREKING

### A. Vrijstelling met progressievoorbehoud

1. Art. 155, eerste lid, van het Wetboek van de inkomstenbelastingen 1992 (WIB 92), bepaalt dat inkomsten die krachtens internationale overeenkomsten ter voorkoming van dubbele belasting (DBV) zijn vrijgesteld, in aanmerking komen voor het bepalen van het tarief van de belasting dat op de overige inkomsten van toepassing is, maar dat die belasting wordt verminderd naar de verhouding tussen de inkomsten die zijn vrijgesteld en het geheel van de inkomsten.

Dat principe wordt gewoonlijk 'vrijstelling met progressievoorbehoud' genoemd.

De nieuwe wettelijke bepaling wijzigt in dat verband de fiscale behandeling van de inkomsten die in beginsel afzonderlijk belastbaar zijn.

### B. Belasting tegen een afzonderlijke aanslagvoet

2. Vóór die nieuwe wettelijke bepaling werden ook inkomsten die in beginsel tegen een afzonderlijk tarief belastbaar zijn, in aanmerking genomen voor het progressievoorbehoud [^1]. Die toepassing van art. 155, WIB 92, werd voorheen ook in de rechtspraak gevolgd [^2].

[^1]: Nr. 171/3, Com.IB 92, parlementaire vraag nr. 215 van 27.05.1991 van de heer de Clippele, parlementaire vraag nr. 548 van 25.06.2009 van de heer Van Biesen.
[^2]: Arresten van het hof van beroep van Brussel van 08.05.1992 en 10.02.1994.

3. Het hof van beroep van Antwerpen heeft in twee arresten (van 22.10.2019 en 17.12.2019) echter geoordeeld dat inkomsten die, als ze niet waren vrijgesteld, in België aan een afzonderlijk tarief zouden worden belast, op basis van het Belgisch-Nederlands DBV moeten worden vrijgesteld zonder progressievoorbehoud.

Daarnaast heeft het Grondwettelijk Hof (arrest nr. 188/2021 van 23.12.2021) geoordeeld dat art. 155, eerste lid, WIB 92, de art. 10, 11 en 172 van de Grondwet schendt als het in die zin wordt geïnterpreteerd dat het onder de inkomsten die krachtens internationale overeenkomsten ter voorkoming van dubbele belasting zijn vrijgesteld en die in aanmerking worden genomen voor het bepalen van de belasting, de inkomsten beoogt die, als zij niet waren vrijgesteld, belastbaar zouden zijn tegen een afzonderlijke aanslagvoet overeenkomstig art. 171, 5°, a, WIB 92.

4. Ook in met andere landen afgesloten DBV's is de vrijstelling met progressievoorbehoud op dezelfde manier geformuleerd als in het Belgisch-Nederlands verdrag, waardoor inkomsten uit die landen die, als ze niet waren vrijgesteld, in België tegen een afzonderlijk tarief zouden worden belast, op basis van die verdragen dus ook zouden moeten worden vrijgesteld zonder progressievoorbehoud.

In de DBV's afgesloten met Algerije, Duitsland, Frankrijk, Luxemburg en Oostenrijk is het progressievoorbehoud op een andere manier geformuleerd en kunnen de voormelde inkomsten uit die landen verder in het progressievoorbehoud worden betrokken. Geen enkele van de voormelde verdragen verplicht België evenwel om een progressievoorbehoud toe te passen, noch om een eventueel progressievoorbehoud voor alle inkomsten op dezelfde manier toe te passen.

Om te vermijden dat de berekening van de personenbelasting nog complexer zou worden, is de wet aangepast zodat ook de inkomsten uit die landen die, als ze niet waren vrijgesteld, in België tegen een afzonderlijk tarief zouden worden belast, vrij te stellen zonder progressievoorbehoud. Hetzelfde geldt voor de inkomsten bedoeld in art. 155, tweede lid, WIB 92.

De vrijstelling zonder progressievoorbehoud van de betrokken inkomsten is internrechtelijk geregeld door in art. 171, WIB 92, te voorzien dat die inkomsten belastbaar zijn tegen een tarief van 0 %.

5. De wet van 21.01.2022 [^3] heeft het WIB 92, in die zin gewijzigd door in art. 171 een 8° toe te voegen, dat een belasting tegen de aanslagvoet van 0 % invoert voor de (in 1° tot 7° vermelde) afzonderlijk belastbare inkomsten waarvoor de belasting in toepassing van art. 155, WIB 92, zou worden verminderd als ze (volgens art. 130, WIB 92) gezamenlijk zouden worden belast.

[^3]: Art. 5 en 6 van de wet van 21.01.2022 houdende diverse fiscale bepalingen (hierna W 21.01.2021) (BS 28.01.2022).

6. De normale regels voor de toepassing van art. 171, WIB 92, blijven echter gelden.

Dat houdt in dat inkomsten die, als ze niet waren vrijgesteld, tegen de progressieve aanslagvoeten zouden worden belast omdat de volledige globalisatie voordeliger zou zijn, wel aan het progressievoorbehoud onderworpen blijven.

### C. Aanvullende gemeentebelasting

7. Beroepsinkomsten die krachtens een DBV in België vrijgesteld zijn van personenbelasting, kunnen overeenkomstig art. 466bis, WIB 92, voor de berekening van de aanvullende gemeentebelasting worden behandeld als inkomsten die uit bronnen in België zouden zijn verkregen, voor zover het DBV dat toelaat. Voor de inkomsten waarvoor bij de berekening van de personenbelasting de hierboven bedoelde aanslagvoet van 0 % wordt toegepast, zal in geval van toepassing van art. 466bis, WIB 92, voor de berekening van de gemeentelijke opcentiemen de belasting eveneens worden bepaald aan de hand van de aanslagvoet die van toepassing zou zijn als het inkomsten van een Belgische bron betrof.

## II. INWERKINGTREDING

8. Deze wijziging is van toepassing vanaf aanslagjaar 2021.

## III. WETTEKSTEN

9. W 21.01.2022

> '(…)
>
> **Art. 5**
>
> Artikel 171 van hetzelfde Wetboek, laatstelijk gewijzigd bij de wet van 24 december 2020 en bij het artikel 3 van deze wet, wordt aangevuld met een bepaling onder 8°, luidende: > > "8° tegen een aanslagvoet van 0 pct.: de in 1° tot 7° vermelde inkomsten waarvoor de belasting bij toepassing van artikel 155 zou worden verminderd indien ze overeenkomstig artikel 130 zouden worden belast.".
>
> **Art. 6**
>
> Artikel 5 is van toepassing vanaf aanslagjaar 2021.
>
> (…)'

## Verwante documenten

- 21.01.2022 — Wet houdende diverse fiscale bepalingen
- Artikel 155, WIB 92 (historisch)
- Artikel 171, WIB 92 (historisch)
- Artikel 466bis, WIB 92 (historisch)
