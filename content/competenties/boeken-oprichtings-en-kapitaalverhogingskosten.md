---
title: Boeken van oprichtings- en kapitaalverhogingskosten en hun afschrijving
tags:
- competentie
- po-1-1
programmaonderdelen:
- '1.1'
status: voorgesteld
schema_version: '1.1'
gegenereerd_uit: data/concepten/competenties/boeken-oprichtings-en-kapitaalverhogingskosten.yaml
gegenereerd_op: '2026-05-16'
---
# Boeken van oprichtings- en kapitaalverhogingskosten en hun afschrijving

**⚖️ 80% · 🤖 20%**

> Activering en afschrijving van oprichtingskosten (rubriek 20) zijn voorgeschreven in KB-WVV art. 3:39 en 3:42. Afschrijvingstermijn (maximaal 5 jaar) is wettelijk; de keuze tussen direct ten laste nemen of activeren is een professional judgment-keuze.

## Aanbevolen werkwijze

### 1. Onderscheid oprichtings- van eerste-werkings-kosten

Bepaal welke uitgaven kwalificeren als activeerbare oprichtingskosten en welke onmiddellijk als kost geboekt moeten worden.

**Waarom?** Alleen specifieke notaris- en administratieve oprichtingskosten mogen op rubriek 20; gewone werkingskosten (telefonie, kantoorhuur) horen op klasse 6.

**📥 Input**:
- Facturen oprichtingsperiode → **Notarisakte, RSZ-aansluitings-kosten, bankrekening-opening, software-licentie, eerste loon, kantoorinrichting** _(document)_

**📤 Output**:
- Werknotitie classificatie → **Lijst factuur → activeren of kost** _(conclusie)_

**🛠️ Hoe**:

1. Activeerbaar volgens [[oprichtingskosten]] §scope: oprichtingskosten in enge zin (notarisakte oprichting, neerlegging WVV-griffie, KBO-inschrijving, eerste statutenpublicatie BS), kapitaalverhogingskosten, kosten van uitgifte leningen en eigen vermogen, herstructureringskosten.
2. Niet activeerbaar: gewone werkingskosten zoals telefonie, eerste loon, kantoorhuur — direct op klasse 6.
3. Bij Oprichtingen Oostende BV — analyseer de facturen oprichtingsperiode jan-feb 2026.
4. Activering is een KEUZE, geen verplichting — bij beperkte bedragen kan ook direct ten laste worden geboekt om te voorkomen dat het uitkeerbare resultaat geblokkeerd wordt (KB-WVV art. 3:42 lid 2).


**Grondslag**: [[oprichtingskosten]] §classificatie, KB-WVV art. 3:39

> [!warning]- Activeer alleen kosten die noodzakelijk zijn voor de oprichting of kapitaalverhoging als rechtshandeling — niet de eerste maand kantoorhuur.
>
> _Vaak fout gedaan_: Alle uitgaven van de eerste twee maanden activeren als "oprichtings­kosten".
>
> _Grondslag_: [[oprichtingskosten]] §scope

### 2. Boek de geactiveerde oprichtingskosten op rubriek 20

Boek de geclassificeerde oprichtingskosten op de actief-rubriek 20 met btw-aftrek waar van toepassing.

**Waarom?** Activering op rubriek 20 spreidt de last over de afschrijvingstermijn en respecteert de matching tussen kost en gebruik.

**📥 Input**:
- Werknotitie classificatie stap 1 → **Activeerbare bedragen** _(berekening)_

**📤 Output**:
- Journaalpost activering → **Boeking 20 / 411 / 4400** _(boekingsregel)_

**🛠️ Hoe**:

1. Bepaal totaalbedrag activeerbare oprichtingskosten excl. btw.
2. Boek: Debet 200 Oprichtingskosten (of 2010 voor kapitaalverhogingskosten); Debet 411 Aftrekbare btw; Credit 4400 Leveranciers (notaris, drukker, ...).
3. Bij Oprichtingen Oostende BV: notarisakte € 2.800 + drukker statuten € 350 + Belgisch Staatsblad € 280 + KBO € 100 = € 3.530 excl. btw activeerbaar.
4. Indien deels al betaald via oprichters: gebruik tegenpost 4890 Oprichters of via kapitaal-storting.


> [!example]- Voorbeeld: Oprichtingen Oostende BV opgericht 15/01/2026 met kapitaal € 30.000
> Oprichtingen Oostende BV opgericht 15/01/2026 met kapitaal € 30.000. Oprichtingskosten: notaris € 2.800 + 21% btw, drukker statuten € 350 + 21% btw, Belgisch Staatsblad € 280 (geen btw), KBO inschrijving € 100 (geen btw). Totaal activeerbaar excl. btw: € 3.530.
>
> 1. **Activering oprichtingskosten** 📝
>
>    | Datum | Rekening | Omschrijving | Debet | Credit |
>    |---|---|---|---|---|
>    | 15/01/2026 | 200 Oprichtingskosten | notaris + drukker + BS + KBO | € 3.530,00 | |
>    | 15/01/2026 | 411 Aftrekbare btw 21% | btw notaris + drukker | € 661,50 | |
>    | 15/01/2026 | 4400 Leveranciers | te betalen aan notaris + drukker + BS + KBO | | € 4.191,50 |
>    
>

**Grondslag**: [[oprichtingskosten]] §activering, KB-WVV art. 3:39

### 3. Stel het afschrijvingsplan vast (max 5 jaar lineair)

Bepaal de afschrijvingstermijn en jaarlijkse afschrijving van de geactiveerde oprichtingskosten.

**Waarom?** Wettelijke maximumtermijn is 5 jaar; ondernemingen kiezen vaak een kortere periode om de balans sneller "schoon" te krijgen.

**📥 Input**:
- Saldo rubriek 200 stap 2 → **Aanschaffingswaarde oprichtingskosten** _(balans)_

**📤 Output**:
- Afschrijvingstabel → **Per boekjaar: dotatie, gecumuleerde afschrijvingen, netto-boekwaarde** _(berekening)_

**🛠️ Hoe**:

1. Toets de wettelijke maximumtermijn: 5 jaar volgens KB-WVV art. 3:42.
2. Kies methode — lineair is gebruikelijk; uitzonderlijk degressief (zelden gebruikt voor oprichtingskosten).
3. Bereken jaarlijkse dotatie = aanschaffingswaarde / aantal jaren. Bij € 3.530 / 5 = € 706 per jaar.
4. Toets aan beperking uitkeerbaar resultaat (KB-WVV art. 3:42 lid 2): zolang oprichtingskosten niet volledig afgeschreven zijn, mag geen winstuitkering plaatsvinden die het netto-actief onder kapitaal + niet-uitkeerbare reserves zou brengen.
5. Voor Oprichtingen Oostende BV: kies 5 jaar lineair = € 706 per jaar.


> [!example]- Voorbeeld: Oprichtingen Oostende BV — saldo rubriek 200 = € 3.530 op 15/01/2026
> Oprichtingen Oostende BV — saldo rubriek 200 = € 3.530 op 15/01/2026. Afschrijving lineair over 5 jaar = € 706/jaar.
>
> 1. **Afschrijvingstabel** 🧮
>
>    | Boekjaar | Beginsaldo | Dotatie | Gecumuleerde afschrijving | Netto-boekwaarde |
>    |---|---|---|---|---|
>    | 2026 | € 3.530 | € 706 | € 706 | € 2.824 |
>    | 2027 | € 3.530 | € 706 | € 1.412 | € 2.118 |
>    | 2028 | € 3.530 | € 706 | € 2.118 | € 1.412 |
>    | 2029 | € 3.530 | € 706 | € 2.824 | € 706 |
>    | 2030 | € 3.530 | € 706 | € 3.530 | € 0 |
>    
>

**Grondslag**: [[afschrijvingen]] §oprichtingskosten, [[oprichtingskosten]] §afschrijvingsplan, KB-WVV art. 3:42

### 4. Boek jaarlijkse afschrijvingsdotatie op balansdatum

Boek elk boekjaar de dotatie aan oprichtingskosten op rekening 6300 met tegenpost 2009.

**Waarom?** De jaarlijkse boeking erodeert de actief-waarde en voedt het bedrijfsresultaat tot de oprichtingskosten volledig zijn afgeschreven.

**📥 Input**:
- Afschrijvingstabel stap 3 → **Jaarlijkse dotatie** _(berekening)_

**📤 Output**:
- Eindejaars-boeking → **Dotatie + gecumuleerde afschrijvingen** _(boekingsregel)_

**🛠️ Hoe**:

1. Bepaal de dotatie volgens afschrijvingstabel.
2. Boek op balansdatum: Debet 6300 Afschrijving oprichtingskosten; Credit 2009 Gecumuleerde afschrijvingen oprichtingskosten.
3. Toets de bestemmingsbepaling: het uitkeerbaar resultaat blijft beperkt zolang netto-boekwaarde > 0.
4. Bij Oprichtingen Oostende BV per 31/12/2026: Debet 6300 € 706; Credit 2009 € 706.


> [!example]- Voorbeeld: Oprichtingen Oostende BV — eindejaarsboeking 31/12/2026, dotatie jaar 1
> Oprichtingen Oostende BV — eindejaarsboeking 31/12/2026, dotatie jaar 1.
>
> 1. **Boeking dotatie** 📝
>
>    | Datum | Rekening | Omschrijving | Debet | Credit |
>    |---|---|---|---|---|
>    | 31/12/2026 | 6300 Afschrijving oprichtingskosten | dotatie 2026 (1/5) | € 706,00 | |
>    | 31/12/2026 | 2009 Gecumuleerde afschrijvingen oprichtingskosten | -- | | € 706,00 |
>    
>

**Grondslag**: [[afschrijvingen]] §dotatie, [[oprichtingskosten]] §afschrijving


## Voorbeelden

> [!example]- Oprichtingen Oostende BV opgericht 15/01/2026
> **Conclusie**: Activeerbaar (rubriek 200) = € 3.530. Direct ten laste (klasse 6) = eerste loon € 2.500 op 6203 en huur € 1.200 op 6101. Btw apart op 411. Afschrijving over 5 jaar lineair → € 706/jaar.
>
> **Grondslag**: [[oprichtingskosten]] §scope; [[afschrijvingen]] §oprichtingskosten
>
> **Redenering**: Notaris + drukker + BS + KBO zijn juridisch noodzakelijk voor oprichting → rubriek 20. Loon en huur zijn werkingskosten, niet juridisch verbonden met de oprichtingshandeling → klasse 6.

> [!example]- Aurelia Holding NV verhoogt in 2026 het kapitaal met € 500.000
> **Conclusie**: Beide bedragen activeerbaar op 2010 Kapitaalverhogingskosten = € 6.300. Afschrijving lineair over 5 jaar → € 1.260/jaar. Tegenboeking schuld 4400.
>
> **Grondslag**: [[oprichtingskosten]] §kapitaalverhogingskosten; [[kapitaalwijziging]] §kosten
>
> **Redenering**: Kapitaalverhogingskosten kwalificeren expliciet onder rubriek 20. Bankkosten verbonden met emissie zijn opnamekosten — eveneens activeerbaar.


## Gebaseerd op concepten

[[oprichtingskosten]] · [[afschrijvingen]] · [[eigen-middelen]] · [[kapitaalwijziging]]
## Voortkomend uit

- **Taken**: 1.1.taak.1
- **Kenniselementen**: 1.1.II.A, 1.1.II.H
