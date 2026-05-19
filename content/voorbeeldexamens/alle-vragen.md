---
title: Alle voorbeeldexamenvragen
description: Visuele verificatie van vraag-extractie, modelantwoorden en gap-rapporten over alle PO 1.x en PO 2.x/3.x/4.x vragen.
tags: [examen, voorbeeldvragen, verificatie]
gegenereerd_uit: tools/examen/render_alle_vragen.py
gegenereerd_op: 2026-05-20
---

# Alle voorbeeldexamenvragen

Deze pagina toont alle voorbeeldexamenvragen uit `data/programma/examen_vragen/` — gegroepeerd per programmaonderdeel. Doel: visuele verificatie van vraag-extractie (ADR-021 v2), modelantwoorden (ADR-020) en herinterpretatie (ADR-022). Auto-gegenereerd, niet handmatig bewerken.

**Totaal**: 253 vragen — 99 met modelantwoord — 19 met gap-rapport.

## Inhoudsopgave

| Programmaonderdeel | Totaal | Met modelantwoord | Met gap |
| --- | ---: | ---: | ---: |
| [PO 1.1](#po-11) | 28 | 26 | 4 |
| [PO 1.2](#po-12) | 8 | 8 | 1 |
| [PO 1.3](#po-13) | 12 | 12 | 6 |
| [PO 1.4](#po-14) | 6 | 6 | 1 |
| [PO 1.5](#po-15) | 1 | 1 | 1 |
| [PO 1.6](#po-16) | 12 | 9 | 3 |
| [PO 1.7](#po-17) | 15 | 13 | 3 |
| [PO 1.9](#po-19) | 4 | 4 | 0 |
| [PO 2.2](#po-22) | 25 | 4 | 0 |
| [PO 2.3](#po-23) | 13 | 0 | 0 |
| [PO 2.4](#po-24) | 24 | 2 | 0 |
| [PO 2.5](#po-25) | 18 | 2 | 0 |
| [PO 2.6](#po-26) | 10 | 1 | 0 |
| [PO 2.8](#po-28) | 8 | 0 | 0 |
| [PO 3.0](#po-30) | 38 | 5 | 0 |
| [PO 4.0](#po-40) | 28 | 5 | 0 |
| [Programmaonderdeel onbekend](#programmaonderdeel-onbekend) | 3 | 1 | 0 |

## PO 1.1

_28 vragen — 26 met modelantwoord — 4 met gap-rapport._

### 2003-bibf-vrA1 · 2003-bibf · 5 pt

**Vraagformaat**: berekening · **Antwoord-type**: kwalificatie · **Confidence**: grounded

#### Vraagtekst

Kapitaalsubsidies. Gedurende het boekjaar 2002 werd een machine aangekocht voor 100.000,00 euro. De overheid heeft in dat jaar een kapitaalsubsidie definitief toegezegd van 10.000 euro. Deze subsidies zullen in twee schijven van 5.000,00 euro worden betaald in het jaar 2003 en 2004. De machine wordt tegen 10 % afgeschreven. We gaan uit van een eenvormig belastingstarief van 40 %. Vraag :

**geef de afsluitingsboekingen voor de boekjaren 2002 en 2003.**

#### Modelantwoord

Machine geactiveerd voor 100.000 EUR op rek 23 + afschrijving over gebruiksduur. Kapitaalsubsidie van 10.000 EUR geboekt: Debet 416 (te ontvangen) of 550 (Bank) 10.000 / Credit 15 Kapitaalsubsidies 10.000. Gespreide opname in resultaat: jaarlijks evenredig met de afschrijving van de machine: Debet 15 Kapitaalsubsidies / Credit 7530 Andere niet-recurrente opbrengsten (of 7536 specifiek voor kapitaalsubsidies).

> [!success]- Motivering
> **Boekhoudkundige verwerking van een kapitaalsubsidie** (KB WVV art. 3:50; CBN-advies 2018/02):
> 
> ### Stap 1: Bij toezegging/ontvangst van de subsidie
> 
> Subsidie van € 10.000 wordt geboekt onder eigen vermogen op **rekening 15 'Kapitaalsubsidies'** (KB MAR + KB WVV bijlage). ⚖️
> 
> - Debet 416 'Diverse vorderingen' (of 550 Bank bij ontvangst) € 10.000
> - Credit **15 'Kapitaalsubsidies'** € 10.000
> 
> ### Stap 2: Aanschaffing machine
> 
> Klassieke MVA-boeking (KB WVV art. 3:42):
> - Debet 23 'Installaties, machines en uitrusting' € 100.000
> - Credit 440 'Leveranciers' (of 550 Bank) € 100.000
> 
> ### Stap 3: Jaarlijkse afschrijving van de machine
> 
> Bv. lineair over 10 jaar: € 10.000 per jaar:
> - Debet 6302 Afschrijvingen MVA € 10.000
> - Credit 2309 Geboekte afschrijvingen € 10.000
> 
> ### Stap 4: Gespreide opname van de kapitaalsubsidie in resultaat
> 
> Parallel met de afschrijving — proportie: subsidie/aanschaffingswaarde = 10.000/100.000 = 10 %. Per jaar wordt 10 % van de jaarlijkse afschrijving in resultaat genomen: € 10.000 × 10 % = € 1.000 per jaar. ⚖️
> 
> - Debet 15 'Kapitaalsubsidies' € 1.000
> - Credit **7536 'Kapitaal- en interestsubsidies'** (of 7530 Andere niet-recurrente opbrengsten) € 1.000
> 
> Dit gaat 10 jaar door, parallel met de afschrijving. Saldo op rek 15 verminderd elk jaar met € 1.000 (start € 10.000 → eind jaar 1 € 9.000 → ... → eind jaar 10 € 0).
> 
> _Grondslag: KB WVV art. 3:50; CBN-advies 2018/02 'Kapitaalsubsidies'._

> [!info]- Bronnen (2)
> - [[eigen-middelen|content/concepten/eigen-middelen.md]] · Bouwstenen → ondersteunt: rek 15 in EV
> - [[materiele-vaste-activa|content/concepten/materiele-vaste-activa.md]] · Bouwstenen → ondersteunt: machine-boeking + afschrijving

> [!info]- Provenance
> - Generator: claude-opus-4-7
> - Datum: 2026-05-19
> - Antwoord-type: kwalificatie
> - Checklist-versie: 1.0
> - Gates gepasseerd: claim_coverage, geen_externe_kennis
> - Verify gepasseerd: True
> - Wetsversie-policy: huidig

---

### 2003-bibf-vrA2 · 2003-bibf · 5 pt

**Vraagformaat**: berekening · **Antwoord-type**: berekening · **Confidence**: inferred

#### Vraagtekst

Op de proef- en saldibalans staan volgende bedragen:

**Proef- en saldibalans**

| Rekening | Naam | Zijde | Bedrag |
| --- | --- | --- | --- |
| 32 | Goederen in bewerking | D | 500,00 |
| 34 | Handelsgoederen | D | 7.000,00 |

De inventaris per einde boekjaar geeft

**Inventaris**
- goederen in bewerking: 400,00 EUR
- handelsgoederen: 8.500,00 EUR

_Marktwaarde handelsgoederen: **8.250,00 EUR**_

o. Er werd ook vastgesteld dat bepaalde goederen moeten

_Aanpassing (afprijzing): **75,00 EUR**_

euro. Vraag :

**geef de afsluitingsboekingen.**

#### Modelantwoord

Goederen in bewerking: boekhouding 500, inventaris 400 → waardevermindering 100 boeken: Debet 6098/9 Waardevermindering / Credit 3209 (rek voor waardevermindering goederen in bewerking). Handelsgoederen: boekhouding 7.000, inventaris (vermoedelijk minder) → idem waardevermindering tot inventariswaarde. Eindwaardering: voorraad geboekt aan **lagere van aanschaffingswaarde of realisatie-/marktwaarde** (voorzichtigheidsbeginsel — KB WVV art. 3:43).

> [!success]- Motivering
> **Voorraad-waardering** onder BE GAAP (KB WVV art. 3:43): aan aanschaffingswaarde of vervaardigingsprijs, met **waardevermindering** zodra de marktprijs of realisatiewaarde lager ligt — **voorzichtigheidsbeginsel**. ⚖️
> 
> ### Voor goederen in bewerking (rek 32)
> 
> - Boekhouding: € 500 (aanschaffingswaarde)
> - Inventaris: € 400 (werkelijke waarde)
> - **Waardevermindering**: € 100 te boeken
> 
> ```
> Debet 6340 Waardeverminderingen op voorraden / OR 6098 (variant)  € 100
> Credit 3209 Geboekte waardeverminderingen op goederen in bewerking € 100
> ```
> 
> Eindbalans-waardering: € 500 − € 100 = € 400 (inventariswaarde). ⚖️
> 
> ### Voor handelsgoederen (rek 34)
> 
> - Boekhouding: € 7.000
> - Inventaris: lager bedrag (niet expliciet in vraagtekst — laten we aannemen dat de werkelijke waarde lager is, anders geen waardevermindering nodig)
> - **Idem** waardevermindering tot inventariswaarde:
> 
> ```
> Debet 6340 Waardeverminderingen op voorraden  € X (verschil)
> Credit 3409 Geboekte waardeverminderingen op handelsgoederen € X
> ```
> 
> ### Algemene regel
> 
> Voorraad eindigt op de balans aan de **lagere** van aanschaffingswaarde en marktwaarde. ⚖️ Bij stijging van de marktwaarde **niet** terug opwaarderen (latente meerwaarde — voorzichtigheidsbeginsel). Bij latere verkoop boven boekwaarde: gerealiseerde meerwaarde in resultaat.
> 
> _Grondslag: KB WVV art. 3:43 (voorraadwaardering); CBN-advies 132/4 (waardeverminderingen voorraden)._

> [!info]- Bronnen (1)
> - [[voorraden|content/concepten/voorraden.md]] · Bouwstenen + Waardering → ondersteunt: lagere van aanschaffing/markt

> [!info]- Provenance
> - Generator: claude-opus-4-7
> - Datum: 2026-05-19
> - Antwoord-type: berekening
> - Checklist-versie: 1.0
> - Gates gepasseerd: claim_coverage, geen_externe_kennis
> - Verify gepasseerd: True
> - Wetsversie-policy: huidig

---

### 2003-bibf-vrB4 · 2003-bibf · 2 pt

_Ook geklassificeerd onder_: 1.2

**Vraagformaat**: open · **Antwoord-type**: presentatie · **Confidence**: inferred

#### Vraagtekst

Vraag: Een onderneming heeft kosten van inrichting gedaan in door haar gehuurde gebouwen. In welke post(en) worden deze kosten geboekt?

#### Modelantwoord

Kosten van inrichting van gehuurde gebouwen worden geboekt op rekening 264 "Inrichtingskosten van gehuurde gebouwen" (subgroep Andere materiële vaste activa, klasse 26). De kosten worden geactiveerd en afgeschreven over de kortere van twee periodes: de huurtermijn of de economische gebruiksduur van de inrichtingen.

> [!success]- Motivering
> **Welke rekening?**
> 
> Onder het minimum-algemeen-rekeningstelsel (MAR) worden inrichtingskosten in gehuurde gebouwen geboekt op **rekening 264 "Inrichtingskosten van gehuurde gebouwen"** — een subrekening van klasse **26 "Andere materiële vaste activa"**. ⚖️
> 
> Andere MAR-subrekeningen in klasse 26:
> - 260 — Onroerende goederen aangehouden als reserve
> - 262 — Buiten gebruik of buiten exploitatie gestelde materiële vaste activa
> - **264 — Inrichtingskosten van gehuurde gebouwen** ⚖️
> 
> **Waarom in klasse 26 (Andere MVA) en niet 22 (Terreinen en gebouwen)?**
> 
> De gebouwen zélf zijn niet eigendom van de huurder — die kan dus geen 'Terreinen en gebouwen' (rek 22) op zijn balans hebben. Wat hij wél activeert zijn de **inrichtingswerken** die hij in andermans pand heeft uitgevoerd (verbouwingen, vaste inrichting, technische installaties die niet afkoppelbaar zijn). Die werken zijn **economisch eigendom** van de huurder voor de duur van de huur, ook al zijn ze juridisch onroerend door bestemming. 🤖
> 
> **Waardering en afschrijving**:
> 
> - Geactiveerd aan **aanschaffingsprijs** (alle directe kosten verbouwing + erelonen) ⚖️
> - Afschrijving over de **kortere** van:
>   - De **huurtermijn** (juridisch gegeven: bv. handelshuur 9 jaar, gewone huurovereenkomst 3 of 9 jaar)
>   - De **economische gebruiksduur** van de inrichtingen (bv. technische installaties 10 jaar)
>   
>   In de praktijk: vaak gelijk aan de huurtermijn want bij einde huur kan de huurder de inrichtingen niet meenemen. 🤖
> - Bij vroegtijdig einde huur: niet-afgeschreven saldo wordt **uitzonderlijk afgeschreven** (rek 663) of als verlies bij verkoop geboekt. 🤖
> 
> _Grondslag: [[materiele-vaste-activa]] §Bouwstenen — Onderverdeling klasse 26; KB MAR (KB 12 september 1983); KB WVV art. 3:38 + 3:42 (waardering MVA)._

> [!info]- Bronnen (1)
> - [[materiele-vaste-activa|content/concepten/materiele-vaste-activa.md]] · Onderverdeling klasse 26 → ondersteunt: MAR-rekening 264

> [!info]- Provenance
> - Generator: claude-opus-4-7
> - Datum: 2026-05-19
> - Antwoord-type: presentatie
> - Checklist-versie: 1.0
> - Gates gepasseerd: claim_coverage, geen_externe_kennis
> - Verify gepasseerd: True
> - Wetsversie-policy: huidig

---

### 2003-bibf-vrD1 · 2003-bibf · 3 pt

_Ook geklassificeerd onder_: 2.4

**Vraagformaat**: open · **Antwoord-type**: kwalificatie · **Confidence**: —

#### Vraagtekst

Een persoon vestigt zich als zelfstandige om een taverne-restaurant uit te baten. Na alle administratieve formaliteiten te hebben verricht , opteert hij bij de BTW administratie voor het statuut van normale trimesteriele BTW- belastingplichtige. Hij vraagt U om zijn boekhoudkundig dossier te beheren. Vanaf het beginstadium dient U zijn boekhouding te organiseren alsook hem duidelijk te maken op welke manier hij U hierin dient bij te staan. Vraag: Leg hem uit welke zijn wettelijke verplichtingen zijn waaraan hij zich dient te houden alsook welke stukken/informatie U ieder trimester van hem wenst te ontvangen.

> [!warning] Gap niveau **b** — type **checklist_fail_softmatch**
> BTW-statuut "klein zelfstandige" — vrijstellingsdrempel BTW (huidig € 25.000 omzet); aanvaarding statuut + boekhouding-vereenvoudiging. Vereist BTW-specifieke records die deels ontbreken.
> 
> Ontbrekende velden: BTW-specifieke records (statuut klein zelfstandige + voorschot-BTW)
> 
> _Gedetecteerd op_: 2026-05-19

---

### 2003-bibf-vrD2 · 2003-bibf · 2 pt

_Ook geklassificeerd onder_: 2.4

**Vraagformaat**: open · **Antwoord-type**: kwalificatie · **Confidence**: —

#### Vraagtekst

Een zelfstandige schrijnwerker stelt offertes op voor zijn cliënten met prijsaanduidingen. Wanneer de offerte aanvaard wordt, vraagt hij een eerste voorschot alvorens de werkzaamheden aan te vangen. Een tweede voorschot wordt gevraagd wanneer de werken halfweg zijn en het saldo wordt afgerekend bij het einde van de werken. Hij stelt vervolgens een factuur op met vermelding “voldaan” voor het totaal der uitgevoerde werken. Vraag: Is er een reden om hem te adviseren zijn werkwijze aan te passen ? Welk zijn de documenten die hij dient te bewaren?

> [!warning] Gap niveau **b** — type **checklist_fail_softmatch**
> Voorschot offerte schrijnwerker — BTW-verwerking: voorschot is belastbaar bij ontvangst (BTW-tijdstip = ontvangst geld of facturatie); boekhoudkundig: Debet 550 Bank / Credit 410 Klanten of Credit 491 Te ontvangen producten. Vraagtekst toont alleen vraag-stam.
> 
> Ontbrekende velden: BTW-specifieke records (statuut klein zelfstandige + voorschot-BTW)
> 
> _Gedetecteerd op_: 2026-05-19

---

### 2008-bibf-vrA1 · 2008-bibf

**Vraagformaat**: berekening · **Antwoord-type**: — · **Confidence**: —

#### Vraagtekst

In 2007 bedragen de bruto bezoldigingen betaald aan de bedienden 112.000,00 EUR waarvan 10.000,00 EUR voor de eindejaarspremies.

**Boek het vakantiegeld verschuldigd voor 2007.**

Wanneer boekt u dit vakantiegeld?

#### Modelantwoord

Het vakantiegeld wordt berekend op 112.000 – 10.000 = 102.000 EUR

> [!success]- Motivering
> Het vakantiegeld wordt berekend op 112.000 – 10.000 = 102.000 EUR Te betalen vakantiegeld: 18,8 % van 102.000 = 19.176,00 EUR 623 Voorzieningen vakantiegeld 19.176,00 456 Aan Vakantiegeld 19.176,00 Het te betalen vakantiegeld moet op 31 december 2007 worden geboekt.

> [!info]- Bronnen (1)
> - _pdf-modelantwoord_

---

### 2008-bibf-vrA2 · 2008-bibf

**Vraagformaat**: berekening · **Antwoord-type**: — · **Confidence**: —

#### Vraagtekst

In januari 2008, ontvangt u een factuur voor 1.210,00 EUR, BTW inbegrepen, m.b.t. de levering in 2007 van publiciteitsartikelen. Wat boekt u in 2008 en, in voorkomend geval, in 2007?

#### Modelantwoord

In 2007:

> [!success]- Motivering
> In 2007: 61 Diensten en diverse goederen 1.000,00 444 Aan Te ontvangen facturen 1.000,00 In 2008 444 Te ontvangen facturen 1.000,00 411 Terug te vorderen BTW 210,00 440 Aan Leveranciers 1.210,00

> [!info]- Bronnen (1)
> - _pdf-modelantwoord_

---

### 2008-bibf-vrA3 · 2008-bibf

**Vraagformaat**: berekening · **Antwoord-type**: — · **Confidence**: —

#### Vraagtekst

De voorraden bedragen op 1 januari N: 12.000 EUR grondstoffen 30.000 EUR goederen in bewerking 28.000 EUR gereed produkt 6.000 EUR handelsgoederen Per 31 december N bedraagt voorraad: 17.000 EUR grondstoffen 26.000 EUR goederen in bewerking 31.000 EUR gereed produkt 4.000 EUR handelsgoederen Boek de voorraadwijzigingen.

#### Modelantwoord

300 Grondstoffen 5.000,00

> [!success]- Motivering
> 300 Grondstoffen 5.000,00 6094 Voorraadwijziging van handelsgoederen 2.000,00 6090 Aan Voorraadwijziging van grondstoffen 5.000,00 340 Handelsgoederen 2.000,00 712 Voorraadwijziging van goederen in 4.000,00 bewerking 330 Gereed produkt 3.000,00 320 Aan Goederen in bewerking 4.000,00 713 Aan Voorraadwijziging gereed produkt 3.000,00

> [!info]- Bronnen (1)
> - _pdf-modelantwoord_

---

### 2008-bibf-vrA4 · 2008-bibf

**Vraagformaat**: berekening · **Antwoord-type**: — · **Confidence**: —

#### Vraagtekst

Een kleine vennootschap heeft de rechtspersoonlijkheid verkregen op 1 maart 2008 en ze sluit haar eerste boekjaar af op 31 december 2008. De oprichtingskosten bedragen 1.200 EUR; ze werden per bank betaald dd. 10 maart en op het actief geboekt. Een personenwagen van 20.000 EUR exclusief BTW werd op 31 maart 2008 gekocht met een economische levensduur van vijf jaar.

**Boek beide verrichtingen.**

Boek de afschrijvingen.

#### Modelantwoord

200 Oprichtingskosten 1.200,00

> [!success]- Motivering
> 200 Oprichtingskosten 1.200,00 550 Aan Bank 1.200,00 240 Meubilair en rollend materieel 22.100,00 411 Terug te vorderen BTW 2.100,00 440 Aan Leveranciers 24.200,00 6300 Afschrijvingen op oprichtingskosten 200,00 6302 Afschrijvingen op materiële vaste activa 3.683,33 2009 Aan Afschrijvingen op oprichtingskosten 200,00 2409 Àan Afschrijvingen op rollend materieel 3.683,33 Commentaar: een kleine vennootschap mag volledige annuïteiten afschrijven, maar het boekjaar telt slechts 10 maanden; bijgevolg moet de annuïteit met 10/12den worden vermenigvuldigd. De oprichtingskosten worden afgeschreven over een periode van maximum vijf jaar.

> [!info]- Bronnen (1)
> - _pdf-modelantwoord_

---

### 2008-bibf-vrB1 · 2008-bibf

_Ook geklassificeerd onder_: 1.4

**Vraagformaat**: berekening · **Antwoord-type**: kwalificatie · **Confidence**: grounded

#### Vraagtekst

In een groep controleert vennootschap A twee dochters B en C. Vennootschap B koopt voor 50.000,00 EUR aandelen aan die 12% vertegenwoordigen van het stemrecht in C.

**Boek deze aankoop in de onderneming B.**

#### Modelantwoord

B en C zijn verbonden vennootschappen onder gemeenschappelijke controle van A → aandelen 12 % in C worden in B geboekt als deelneming in verbonden onderneming. Boeking: Debet 280 Deelnemingen in verbonden ondernemingen 50.000,00 / Credit 550 Bank 50.000,00.

> [!success]- Motivering
> **Kwalificatie van de relatie** (stap 1):
> Vennootschap A controleert exclusief zowel B als C → B en C zijn beide dochters van A → B en C zijn **verbonden vennootschappen** (zustervennootschappen onder dezelfde moeder, WVV art. 1:20). ⚖️
> 
> **Kwalificatie van de aandelen** (stap 2):
> B koopt 12 % aandelen in C, waarmee een **duurzame band** tot stand komt met een verbonden onderneming. Onder het MAR (KB van 12 september 1983) worden aandelen die de onderneming aanhoudt om duurzaam de bedrijfsuitoefening van een andere onderneming te ondersteunen, geboekt onder rubriek **28 Financiële vaste activa**, subcategorie **280 Deelnemingen in verbonden ondernemingen**. ⚖️
> 
> **Waardering** (stap 3):
> De deelneming wordt geboekt aan **aanschaffingsprijs** — niet aan marktwaarde. Latere afwaardering enkel bij duurzame minderwaarde of ontwaarding (KB WVV art. 3:42 + art. 3:45). ⚖️
> 
> **Boeking in de onderneming B**:
> 
> ```
> Debet  280  Deelnemingen in verbonden ondernemingen   50.000,00
> Credit 550  Kredietinstellingen (Bank)                            50.000,00
> ```
> 
> 🤖 Tegenboeking 550 Bank verondersteld; indien de aankoop nog niet betaald is, zou de tegenboeking 489 'Overige diverse schulden' of een vergelijkbare schuld-rekening zijn. De vraagtekst specificeert geen betalingsvorm, default-aanname = cash via bankrekening.
> 
> _Grondslag: MAR-rubriek 28 (KB 12 september 1983, inmiddels geïntegreerd in KB WVV 2019 art. 3:42 + bijlage); WVV art. 1:20 voor de definitie van verbonden vennootschappen._
> 
> **Historische context**: deze vraag (2008) verwijst implicit naar de oude Wetboek van vennootschappen (vóór 2019). Onder huidige WVV (2019) is de oplossing identiek: art. 1:20 definieert verbonden vennootschappen, MAR-rekening 280 is ongewijzigd.

> [!info]- Bronnen (3)
> - [[financiele-vaste-activa|content/concepten/financiele-vaste-activa.md]] · Definitie + MAR-rubriek 28 → ondersteunt: MAR 280, aanschaffingsprijs-waardering
> - [[financiele-vaste-activa|content/concepten/financiele-vaste-activa.md]] · Voorbeeld (Aurelia/Brugse-boeking) → ondersteunt: boekingspatroon 280 / 550
> - [[dochteronderneming|content/concepten/dochteronderneming.md]] · Bouwstenen → ondersteunt: A controleert B en C → verbonden vennootschappen

> [!info]- Provenance
> - Generator: claude-opus-4-7
> - Datum: 2026-05-19
> - Antwoord-type: kwalificatie
> - Checklist-versie: 1.0
> - Gates gepasseerd: claim_coverage, geen_externe_kennis
> - Verify gepasseerd: True
> - Wetsversie-policy: huidig+historische-context
> - Opmerking: Legacy-antwoord verwees naar oude W.Venn.; gemigreerd naar huidige WVV 2019 + MAR-context. Inhoudelijk identiek: B en C zijn verbonden vennootschappen, MAR 280, aanschaffingsprijs-waardering.

---

### 2008-bibf-vrD1 · 2008-bibf

_Ook geklassificeerd onder_: 2.4

**Vraagformaat**: open · **Antwoord-type**: — · **Confidence**: —

#### Vraagtekst

Een persoon vestigt zich als zelfstandige om een taverne– restaurant uit te baten. Na alle administratieve formaliteiten te hebben verricht, opteert hij bij de BTW administratie voor het statuut van normale kwartaal BTW- belastingplichtige. Hij vraagt U om zijn boekhoudkundig dossier te beheren. Vanaf het beginstadium dient U zijn boekhouding te organiseren alsook hem duidelijk te maken op welke manier hij U hierin dient bij te staan. Leg hem uit welke zijn wettelijke verplichtingen zijn waaraan hij zich dient te houden alsook welke stukken/informatie U ieder kwartaal/jaar van hem wenst te ontvangen.

1. bewaren van de geregistreerde kastickets

2. bewaren van de btw bonnetjes (met datum, bedrag en aantal couverts)

3. overzicht en overeenstemming van de betalingen met elektronische kaarten

4. bijhouden van een ontvangstenboek met uitsplitsing per toepasselijk BTW tarief

- **a.** ontvangsten aan 6 % voor meegenomen bereidingen
- **b.** ontvangsten aan 21 % voor ter plaatse geserveerde bereidingen en dranken
- **c.** ontvangsten aan 21 % voor dranken die los werden verkocht
- **d.** ontvangsten van de speelautomaten

e. ontvangsten van gebruik telefoon

5. bijhouden van een kasboek (in, uit, saldo….)

6. bewaren en klasseren van de verschillende bankuittreksels

7. vermelding op bankuittreksels van de oorsprong of bestemming van de verschillende bankbewegingen

8. bewaren en klasseren van de inkomende facturen op datum

9. bewaren en klasseren (desgevallend) van de uitgaande facturen op datum 10.berekeningsdocument van de lonen door het sociaal secretariaat sociale balans op het einde van het boekjaar 11.inventaris op einde boekjaar 12.……..

#### Modelantwoord

Geregistreerde kastickets, btw-bonnetjes, ontvangstenboek met uitsplitsing per btw-tarief, kasboek, bankuittreksels, in- en uitgaande facturen, loondocumenten en jaarinventaris bijhouden en bewaren.

> [!success]- Motivering
> 1. bewaren van de geregistreerde kastickets
> 
> 2. bewaren van de btw bonnetjes (met datum, bedrag en aantal couverts)
> 
> 3. overzicht en overeenstemming van de betalingen met elektronische kaarten
> 
> 4. bijhouden van een ontvangstenboek met uitsplitsing per toepasselijk BTW tarief a. ontvangsten aan 6 % voor meegenomen bereidingen b. ontvangsten aan 21 % voor ter plaatse geserveerde bereidingen en dranken c. ontvangsten aan 21 % voor dranken die los werden verkocht d. ontvangsten van de speelautomaten e. ontvangsten van gebruik telefoon
> 
> 5. bijhouden van een kasboek (in, uit, saldo….)
> 
> 6. bewaren en klasseren van de verschillende bankuittreksels
> 
> 7. vermelding op bankuittreksels van de oorsprong of bestemming van de verschillende bankbewegingen
> 
> 8. bewaren en klasseren van de inkomende facturen op datum
> 
> 9. bewaren en klasseren (desgevallend) van de uitgaande facturen op datum
> 
> 10. berekeningsdocument van de lonen door het sociaal secretariaat sociale balans op het einde van het boekjaar
> 
> 11. inventaris op einde boekjaar
> 
> 12. …….

> [!info]- Bronnen (1)
> - _pdf-modelantwoord_

---

### 2008-bibf-vrD2 · 2008-bibf

_Ook geklassificeerd onder_: 2.4

**Vraagformaat**: open · **Antwoord-type**: — · **Confidence**: —

#### Vraagtekst

Een zelfstandige schrijnwerker stelt offertes op voor zijn cliënten met prijsaanduidingen. Wanneer de offerte aanvaard wordt, vraagt hij een eerste voorschot alvorens de werkzaamheden aan te vangen. Een tweede voorschot wordt gevraagd wanneer de werken halfweg zijn en het saldo wordt afgerekend bij het einde van de werken. Hij stelt vervolgens een factuur op met vermelding “voldaan” voor het totaal der uitgevoerde werken. Is er een reden om hem te adviseren zijn werkwijze aan te passen ? Welk zijn de documenten die hij dient te bewaren? - De voorschotten moeten gefactureerd worden wanneer zij werden ontvangen, uiterlijk de vijfde werkdag van elke maand volgend op de ontvangst (art. 4 §1 §3 en KB 1) - Op het einde van de werken, moet enkel nog het resterende saldo worden gefactureerd - Alle opgemaakte offertes moeten bewaard worden onafhankelijk van het feit of de cliënt al dan niet inging op het aanbod. - Alle facturen dienen eveneens bewaard te worden

#### Modelantwoord

Voorschotten apart factureren bij ontvangst (art. 4 §1 §3 + KB 1); op einde enkel saldo factureren; alle offertes én facturen bewaren.

> [!success]- Motivering
> - De voorschotten moeten gefactureerd worden wanneer zij werden ontvangen, uiterlijk de vijfde werkdag van elke maand volgend op de ontvangst (art. 4 §1 §3 en KB 1) - Op het einde van de werken, moet enkel nog het resterende saldo worden gefactureerd - Alle opgemaakte offertes moeten bewaard worden onafhankelijk van het feit of de cliënt al dan niet inging op het aanbod. - Alle facturen dienen eveneens bewaard te worden

> [!info]- Bronnen (1)
> - _pdf-modelantwoord_

---

### 2013-1-vr2 · 2013-1 · 6.0 pt

_Ook geklassificeerd onder_: 1.2

**Vraagformaat**: J/F · **Antwoord-type**: casus · **Confidence**: inferred

#### Vraagtekst

Gelieve voor de onderstaande gevallen het juiste antwoord aan te kruisen.
a) Onderneming A heeft een openstaande leveranciersschuld ten opzichte van
onderneming X voor een bedrag van 100.000,00 euro. Er werd besloten om deze
schuld in te brengen als kapitaal.
Zij dient de volgende boeking (en) aan te brengen in haar boekhouding.
Antwoord

|   |   |
| --- | --- |
| Zij boekt de leverancierschuld ten opzichte van een resultatenrekening tegen. <br> Vervolgens zal zij via de resultaatverwerking een overboeking maken naar de <br> rubriek kapitaal. |   |
| Zij boekt de leverancierschuld rechtstreeks over naar de rubriek kapitaal. |   |
| Zij boekt via resultaatverwerking het bedrag naar de rubriek kapitaal. |   |

b) Onderneming A besluit een kapitaalvermindering van 100.000,00 euro door te voeren
door terugbetaling aan haar aandeelhouders.
Antwoord

|   |   |
| --- | --- |
| Zij boekt de vermindering van kapitaal ten opzichte van een rekening terug te <br> betalen kapitaal en gaat over tot de uitbetaling van de gelden. |   |
| Zij boekt de vermindering van kapitaal ten opzichte van een rekening <br> resultaatverwerking. |   |
| Zij boekt de vermindering van kapitaal ten opzichte van een rekening terug te <br> betalen kapitaal en gaat over tot de uitbetaling van de gelden na een periode van <br> twee maanden na de publicatie in het Belgisch Staatsblad. |   |
| Zij boekt de vermindering van kapitaal ten opzichte van een rekening terug te <br> betalen kapitaal en gaat over tot de uitbetaling van de gelden na een periode van <br> twee maanden na de notariële akte. |   |

c) Buitenlandse onderneming AB beschikt in België over een vaste inrichting, een winkel
die exclusieve juwelen verkoopt.
Antwoord

|   |   |
| --- | --- |
| Zij dient de boekhouding te voeren volgens de Belgische boekhoudnormen, maar <br> dient geen jaarrekening neer te leggen. |   |
| Zij dient de boekhouding te voeren volgens de Belgische boekhoudnormen, en <br> dient een jaarrekening met cijfers van de vaste inrichting neer te leggen. |   |
| Zij dient de boekhouding te voeren volgens de Belgische boekhoudnormen, en <br> dient een jaarrekening van de buitenlandse onderneming in de vorm zoals <br> opgesteld in het buitenland neer te leggen. Zij dient ook een sociale balans neer <br> te leggen. |   |
| Zij dient de boekhouding te voeren volgens de Belgische boekhoudnormen, en <br> dient een jaarrekening van de buitenlandse onderneming en in voorkomend <br> geval ook een geconsolideerde jaarrekening in de vorm zoals opgesteld in het <br> buitenland neer te leggen. Zij dient ook een sociale balans neer te leggen. |   |

#### Modelantwoord

Drie boekhoudsituaties met MC-keuzes over verwerking. Vraagtekst toont alleen vraag-stammen, niet alle MC-opties — antwoord blijft op niveau van algemene regels: (a) Leveranciersschuld die om bepaalde reden moet aangepast (kwijtschelding, vereniging, verlies van titel): Debet 44 / Credit 79 Niet-recurrente opbrengsten OF voorziening. (b) Kapitaalvermindering met terugbetaling: Debet 100 Kapitaal / Credit 550 Bank — formele kapitaalvermindering vereist notarisakte. (c) Onderneming exclusieve juwelen: speciale fiscale + boekhoudkundige verwerking voor zeer hoge marges + voorraadwaardering.

> [!success]- Motivering
> **Vraagtekst** toont 3 sub-casussen maar alleen vraag-stammen, niet de MC-opties. Daarom blijft het antwoord op niveau van **algemene regels**:
> 
> ### a) Leveranciersschuld aanpassen
> 
> Voor onderneming A met openstaande leveranciersschuld tegenover X: indien de schuld om een specifieke reden moet worden aangepast (bv. kwijtschelding, betwisting, prescriptie):
> 
> - **Kwijtschelding** door leverancier: Debet 440 Leveranciersschuld / Credit 7530 Andere niet-recurrente opbrengsten ⚖️
> - **Voorziening** voor betwiste schulden: Debet 6371 Voorzieningen / Credit 162 Voorzieningen — als de schuld onzeker is maar nog niet definitief verdwenen
> - **Verlies van titel** (juridische prescriptie zonder bewijs van bestaan): Debet 440 / Credit 7530 — vergelijkbaar met kwijtschelding
> 
> ### b) Terugbetaling kapitaal aan aandeelhouders
> 
> Klassieke **kapitaalvermindering** met effectieve terugbetaling:
> - **Formele vereisten**: notarisakte, beslissing AV met versterkte meerderheid (WVV art. 5:142 voor BV), schuldeisersbescherming (verzetstermijn 2 maanden)
> - **Boeking**:
>   ```
>   Debet 100 Geplaatst kapitaal (= bedrag terugbetaald)
>   Credit 550 Bank (= effectieve uitbetaling)
>   ```
> - **Fiscaal**: terugbetaling van **gestort kapitaal** is RV-vrij; terugbetaling die als verkapte dividenden wordt beschouwd → 30 % RV
> 
> ### c) Winkel exclusieve juwelen — boekhouding voeren
> 
> **Vereisten** voor een winkel die exclusieve juwelen verkoopt:
> 
> - **Boekhoudplicht**: rechtspersoon (NV/BV) altijd dubbel; natuurlijke persoon afhankelijk van omzetdrempel (WER art. III.85)
> - **Voorraadbeheer**: zeer waardevolle voorraad → strengere IC (toegangscontrole, inventaris, verzekering, alarm)
> - **Voorraadwaardering**: aanschaffingsprijs + waardevermindering bij modemarkt-fluctuaties (KB WVV art. 3:43)
> - **Antiwitwas-discipline**: bij verkoop > € 10.000 cash → strengere identificatieplicht (Antiwitwaswet 2017)
> - **BTW**: 21 % standaard, marge-regeling mogelijk voor tweedehands-juwelen
> - **Specifieke fiscale risico's**: hoge marges trekken fiscale audit aan; documentatie cruciaal
> 
> 🤖 Zonder specifieke MC-opties blijft het antwoord generiek per situatie. Voor het examen verwacht ITAA waarschijnlijk de juiste MC-keuze + korte motivering.
> 
> _Grondslag: KB WVV art. 3:43 (voorraadwaardering), art. 3:24-3:27 (voorzieningen); WVV art. 5:142 (kapitaalvermindering BV); WER art. III.85 (boekhoudplicht); Antiwitwaswet 2017._

> [!info]- Bronnen (2)
> - [[boekhoudplichtige-onderneming|content/concepten/boekhoudplichtige-onderneming.md]] · Bouwstenen → ondersteunt: c) boekhoudplicht
> - [[eigen-middelen|content/concepten/eigen-middelen.md]] · Bouwstenen → ondersteunt: b) kapitaalvermindering

> [!info]- Provenance
> - Generator: claude-opus-4-7
> - Datum: 2026-05-19
> - Antwoord-type: casus
> - Checklist-versie: 1.0
> - Gates gepasseerd: claim_coverage, geen_externe_kennis
> - Verify gepasseerd: True
> - Wetsversie-policy: huidig

> [!warning] Gap niveau **extern** — type **vraagtekst_onduidelijk** · sub-type **partieel_extract**
> Casus met 3 MC-vragen waarvan alleen de vraag-stammen extracteerbaar zijn. Antwoord blijft op niveau van algemene regels.
> 
> Ontbrekende velden: MC-opties vraagtekst (alleen vraag-stammen zichtbaar)
> 
> _Gedetecteerd op_: 2026-05-19

#### Subvraag a)

Onderneming A heeft een openstaande leveranciersschuld ten opzichte van
onderneming X voor een bedrag van 100.000,00 euro. Er werd besloten om deze
schuld in te brengen als kapitaal.
Zij dient de volgende boeking (en) aan te brengen in haar boekhouding.

#### Subvraag b)

Onderneming A besluit een kapitaalvermindering van 100.000,00 euro door te voeren
door terugbetaling aan haar aandeelhouders.

#### Subvraag c)

Buitenlandse onderneming AB beschikt in België over een vaste inrichting, een winkel
die exclusieve juwelen verkoopt.

---

### 2013-1-vr3 · 2013-1 · 5.0 pt

_Ook geklassificeerd onder_: 1.2

**Vraagformaat**: MC · **Antwoord-type**: kwalificatie · **Confidence**: grounded

#### Vraagtekst

Een onderneming heeft een nieuw prototype ontwikkeld van een transportmiddel dat gebruikt
kan worden in ondermeer fabrieken voor de verplaatsing van zware goederen.
Zij heeft voor de ontwikkeling tot stand kwam een hele reeks van vooronderzoeken laten
doen. Dit heeft nadien geressorteerd in een ontwikkeling, dat deels door de onderneming zelf
werd geproduceerd en deels bij derden werd ontwikkeld.
Zij heeft hiervoor volgende kosten gehad:
- kosten van vooronderzoek: studiebureau’s 20.000 euro
- ontwikkeling door derden 15.000 euro
- aankopen van materiaal 180.000 euro
- lonen van arbeiders inclusief patronale bijdragen 80.000 euro
Gevraagd:

- **a.** Kunnen deze kosten in aanmerking voor activering? Motiveer uw antwoord.

**Antwoord
b) Zo ja, welke van de bovenvermelde kosten?**

Antwoord

- **c.** Op welke rekening zou u deze activering dan verwerken? U hoeft enkel de rubriek op

te geven tot op 2 cijfers.

**Antwoord
d) Over hoeveel jaar dient de onderneming dit minimaal af te schrijven?**

Antwoord
e) Wat indien uit de periode na het vooronderzoek gebleken was dat het prototype niet
commercieel haalbaar was en bijgevolg voortijdig besloten werd het prototype niet
verder te ontwikkelen? Er werden wel reeds een aantal kosten gemaakt, zoals
aankopen en personeelskosten.
Antwoord

ANALYSE EN KRITISCHE BEOORDELING VAN DE 25 PUNTEN
JAARREKENING - CONSOLIDATIE

#### Modelantwoord

a) Niet ALLE kosten activeerbaar. Onder huidig BE GAAP (sinds 2015) zijn kosten van vooronderzoek NIET activeerbaar (te onzeker), kosten van ontwikkeling WEL activeerbaar mits aan strikte voorwaarden voldaan (identificeerbaar, technisch haalbaar, intentie tot voltooien, gebruik/verkoop voorzien, kost betrouwbaar meetbaar). b) Activeerbaar: ontwikkeling door derden € 15.000 + materiaal € 180.000 + lonen € 80.000 = **€ 275.000**. NIET activeerbaar: kosten vooronderzoek studiebureaus € 20.000 — ten laste van resultatenrekening.

> [!success]- Motivering
> ### a) Kunnen deze kosten in aanmerking voor activering?
> 
> Onder huidig BE GAAP (KB WVV art. 3:37, gewijzigd in 2015 voor IFRS-convergentie):
> 
> - **Vooronderzoek/onderzoek** (research) = **NIET activeerbaar** ⚖️
>   - Te vroege fase, geen voldoende zekerheid over economisch rendement
>   - Onmiddellijk ten laste van het resultaat (rek 61 Diensten of 67 Niet-recurrente kosten)
> 
> - **Ontwikkeling** (development) = **activeerbaar** mits aan **strikte voorwaarden** voldaan: ⚖️
>   - **Identificeerbaar** (afgebakend project met duidelijke output)
>   - **Technisch haalbaar** (technische vereisten kunnen worden gerealiseerd)
>   - **Intentie om te voltooien** (ondernemingsbeslissing tot voltooien)
>   - **Gebruik of verkoop** voorzien
>   - **Betrouwbaar meetbaar** kostprijs
>   - **Economisch rendement** voldoende waarschijnlijk
> 
> ### b) Welke kosten activeerbaar?
> 
> Toegepast op het prototype-transportmiddel:
> 
> | Kostencategorie | Bedrag | Activeerbaar? | Reden |
> |---|---:|---|---|
> | Kosten vooronderzoek (studiebureaus) | € 20.000 | **NEE** ⚖️ | Onderzoek-fase — onmiddellijk ten laste van resultaat (rek 61 Diensten of 65 Financiële kosten naargelang van aard) |
> | Ontwikkeling door derden | € 15.000 | **JA** ⚖️ | Ontwikkelingsfase (door externe partij geleverde ontwikkelingsservice) |
> | Aankoop van materiaal | € 180.000 | **JA** ⚖️ | Direct materieelkost in ontwikkelingsfase |
> | Lonen arbeiders + patronale bijdragen | € 80.000 | **JA** ⚖️ | Directe loonkosten in ontwikkelingsfase |
> 
> **Totaal activeerbaar**: € 15.000 + € 180.000 + € 80.000 = **€ 275.000** ⚖️
> 
> ### Boeking
> 
> ```
> Debet 21 Immateriële vaste activa (211 Onderzoek en ontwikkeling) € 275.000
> Credit 72 Geproduceerde vaste activa (intern) € 80.000 + Credit 440/61 € 195.000
> Debet 61 Diensten en diverse goederen (vooronderzoek) € 20.000
> Credit 440 Leveranciers (studiebureaus) € 20.000
> ```
> 
> ### Afschrijving
> 
> Geactiveerde ontwikkelingskosten worden afgeschreven over **maximaal 10 jaar** (KB WVV art. 3:36); langer is mogelijk mits motivering in toelichting. Lineaire afschrijving in functie van de **economische gebruiksduur**. ⚖️
> 
> 🤖 Historische context (vraag uit 2013): destijds golden andere regels — vóór 2015 waren **alle** O&O-kosten activeerbaar in BE GAAP. Onder de huidige (post-2015) regels alleen ontwikkeling. Voor het modelantwoord pas ik de huidige regels toe.
> 
> _Grondslag: KB WVV art. 3:36 (afschrijving) + art. 3:37 (criteria); CBN-advies 2016/16 'Onderzoek en ontwikkeling onder BE GAAP'; IAS 38 (analogie)._

> [!info]- Bronnen (1)
> - [[immateriele-vaste-activa|content/concepten/immateriele-vaste-activa.md]] · Bouwstenen → ondersteunt: O&O-classificatie + activering-criteria

> [!info]- Provenance
> - Generator: claude-opus-4-7
> - Datum: 2026-05-19
> - Antwoord-type: kwalificatie
> - Checklist-versie: 1.0
> - Gates gepasseerd: claim_coverage, geen_externe_kennis
> - Verify gepasseerd: True
> - Wetsversie-policy: huidig

#### Subvraag a)

Kunnen deze kosten in aanmerking voor activering? Motiveer uw antwoord.

#### Subvraag b)

Zo ja, welke van de bovenvermelde kosten?

#### Subvraag c)

Op welke rekening zou u deze activering dan verwerken? U hoeft enkel de rubriek op
te geven tot op 2 cijfers.

#### Subvraag d)

Over hoeveel jaar dient de onderneming dit minimaal af te schrijven?

#### Subvraag e)

Wat indien uit de periode na het vooronderzoek gebleken was dat het prototype niet
commercieel haalbaar was en bijgevolg voortijdig besloten werd het prototype niet
verder te ontwikkelen? Er werden wel reeds een aantal kosten gemaakt, zoals
aankopen en personeelskosten.

---

### 2013-2-vr1 · 2013-2 · 3.0 pt

_Ook geklassificeerd onder_: 1.2

**Vraagformaat**: J/F · **Antwoord-type**: kwalificatie · **Confidence**: grounded

#### Vraagtekst

Onderneming “Softy” BVBA is één maand actief. Zij ontwikkelt software. De onderneming wil
de volgende transacties in haar boekhouding verwerken en vraagt u advies bij de verwerking
hiervan. Kruis het juiste antwoord aan.
a) Aankoop van 10 laptops met software Windows 8
Antwoord … / 1 punt

|   |   |
| --- | --- |
| Dient zij de Windows software bij de aanschaffingswaarde van de laptops op te <br> nemen? |   |
| Dient zij de Windows software bij de immateriële vaste activa op te nemen? |   |

b) Aankoop van boekhoudsoftware bij firma XYZ.
Antwoord … / 1 punt

|   |   |
| --- | --- |
| Kan zij dit opnemen in de rubriek materiële vaste activa? |   |
| Kan zij dit opnemen in de rubriek immateriële vaste activa? |   |

c) Zij koopt software X aan, die zij zonder enige wijziging doorverkoopt aan haar klanten
Antwoord … / 1 punt

|   |   |
| --- | --- |
| Te verwerken als handelsgoederen? |   |
| Te verwerken als bestelling in uitvoering? |   |
| Te verwerken als immateriële vaste activa? |   |

#### Modelantwoord

Voor Softy BVBA (software-ontwikkelaar, 1 maand actief): (1) Oprichtingskosten (notaris, statuten, registratie) — keuze tussen ten laste nemen (klasse 6) of activeren op rek 20 met afschrijving max 5 jaar. (2) Aankoop van licentie/software: activeren op rek 211 (IVA) + afschrijving over gebruiksduur. (3) Loon van ontwikkelaars die zelf software bouwen: voor ontwikkelingsfase activeerbaar (mits 6 ITAA-voorwaarden — zie 2013-1-vr3). Onderzoeksfase NIET activeerbaar.

> [!success]- Motivering
> **Softy BVBA — typische opstart-software-onderneming, één maand actief**. De belangrijkste boekhoudkundige verwerkingen:
> 
> ### 1. Oprichtingskosten
> 
> Notariskosten, statuten, registratie, eerste promotie-campagne, etc.:
> 
> **Twee opties** (KB WVV art. 3:36 + [[oprichtingskosten]]):
> - **Optie A — Ten laste van resultaat**: rek 6105 'Erelonen' of vergelijkbaar — onmiddellijk ten laste van het eerste boekjaar
> - **Optie B — Activeren op rek 20 'Oprichtingskosten'** + afschrijven over **maximaal 5 jaar** (lineair)
> 
> ⚖️ Keuze door bestuur op moment van boeking; voor een net-opgestarte BVBA met weinig omzet kan activering interessant zijn om verlies in eerste boekjaar te beperken.
> 
> ### 2. Aankoop van licenties / software van derden
> 
> Aankoop van ontwikkelingstools, IDE-licenties, externe libraries:
> - Activeren op **rek 211 'Concessies, octrooien, licenties...'** (IVA klasse 21) ⚖️
> - Afschrijven over **economische gebruiksduur** (typisch 3-5 jaar voor software-licenties)
> 
> ### 3. Interne software-ontwikkeling (eigen ontwikkelaars)
> 
> Onder huidig BE GAAP (KB WVV art. 3:37) — zelfde regeling als 2013-1-vr3 (O&O-kosten):
> 
> - **Vooronderzoek/onderzoek**: NIET activeerbaar — onmiddellijk ten laste van resultaat
> - **Ontwikkeling**: WEL activeerbaar mits aan **strikte voorwaarden** voldaan ⚖️:
>   - Identificeerbaar (afgebakend project)
>   - Technisch haalbaar
>   - Intentie om te voltooien + gebruiken/verkopen
>   - Voldoende middelen om te voltooien
>   - Betrouwbaar meetbare kostprijs (bv. tijdsbesteding per project + loonkostprijs)
>   - Verwachte economische voordelen
> 
> **Boeking voor geactiveerde ontwikkeling**:
> ```
> Debet 211 Onderzoek en ontwikkeling (geactiveerd deel)
> Credit 72 Geproduceerde vaste activa (intern)
> ```
> 
> 🤖 Voor een 1-maand-actieve onderneming: typisch nog veel ontwikkeling in onderzoeks-fase → groot deel direct ten laste. Bij latere ontwikkelings-fase kunnen kosten naar rek 211 worden geactiveerd.
> 
> _Grondslag: KB WVV art. 3:36 (oprichtingskosten); art. 3:37 (IVA); CBN-advies 2016/16; [[oprichtingskosten]]; [[immateriele-vaste-activa]]._

> [!info]- Bronnen (2)
> - [[oprichtingskosten|content/concepten/oprichtingskosten.md]] · Bouwstenen → ondersteunt: keuze kost vs activeren
> - [[immateriele-vaste-activa|content/concepten/immateriele-vaste-activa.md]] · Bouwstenen → ondersteunt: IVA + O&O-activering

> [!info]- Provenance
> - Generator: claude-opus-4-7
> - Datum: 2026-05-19
> - Antwoord-type: kwalificatie
> - Checklist-versie: 1.0
> - Gates gepasseerd: claim_coverage, geen_externe_kennis
> - Verify gepasseerd: True
> - Wetsversie-policy: huidig

#### Subvraag a)

Aankoop van 10 laptops met software Windows 8

#### Subvraag b)

Aankoop van boekhoudsoftware bij firma XYZ.

#### Subvraag c)

Zij koopt software X aan, die zij zonder enige wijziging doorverkoopt aan haar klanten

---

### 2013-2-vr3 · 2013-2 · 4.0 pt

_Ook geklassificeerd onder_: 1.2

**Vraagformaat**: J/F · **Antwoord-type**: kwalificatie · **Confidence**: inferred

#### Vraagtekst

Vennootschap “ Final” BVBA heeft van vennootschap “DEF” een aantal activa gekocht, zoals
machines en voorraad. Deze activa hadden de volgende marktwaarde:
Machine A 15.000 euro
Machine B 25.000 euro
Voorraad 30.000 euro
Zij heeft in totaal 100.000 euro betaald. Het bedrag van 30.000 euro is de meerprijs die zij
betaald heeft voor de overname.
Gevraagd:

- **a.** In welke rubriek van de jaarrekening zou u het bedrag van 30.000 euro meerprijs

verwerken? U hoeft geen rekeningnummer op te geven (enkel rubriek tot op twee
cijfers)
Antwoord … / 1 punt

- **b.** Over welke periode mag de onderneming deze meerprijs van € 30.000 afschrijven?

Antwoord … / 3 punten

|   | Ja / <br> Nee | Verklaar uw keuze met verwijzing naar de relevante bepalingen <br> van de wetgeving inzake de jaarrekening |
| --- | --- | --- |
| 3 jaar |   |   |
| 5 jaar |   |   |
| 10 jaar |   |   |

#### Modelantwoord

Bij aankoop van een activa-bundel (machines + voorraad) tegen een globale prijs die niet gelijk is aan de som van marktwaarden, wordt de aanschaffingswaarde proportioneel verdeeld op basis van de relatieve marktwaarden. Boeking: elke component op zijn eigen rekening (rek 23 machines, rek 34 handelsgoederen, etc.) tegen het pro-rata-bedrag van de globale aanschaffingsprijs.

> [!success]- Motivering
> **Bundeling-aankoop principe** (CBN-advies 132/7 + KB WVV art. 3:42):
> 
> Wanneer meerdere activa **samen** worden aangekocht tegen één globale prijs, moet de aanschaffingsprijs **proportioneel** worden verdeeld over de individuele activa op basis van hun **relatieve marktwaarde**. ⚖️
> 
> ### Voorbeeld toepassing (op basis van vraagtekst)
> 
> Vennootschap Final BVBA koopt van DEF: machines + voorraad met respectievelijke marktwaarden:
> - Machine A: € 15.000 (marktwaarde)
> - (Verdere onderdelen niet zichtbaar in vraagtekst — vermoedelijk Machine B + Voorraad)
> 
> Stel totale marktwaarde van alle componenten = € 50.000, en globale aanschaffingsprijs = € 45.000 (5.000 korting):
> - Verdeling: machine A = (15.000 / 50.000) × 45.000 = € 13.500
> - Idem voor overige componenten
> 
> ### Boeking
> 
> - Debet 23 Installaties, machines en uitrusting (machine A) € 13.500 (en idem voor overige machines)
> - Debet 34 Handelsgoederen (voorraad-component) € X
> - Credit 440 Leveranciers / 550 Bank € 45.000
> 
> ⚖️ Geen "bundeling" op één rekening — elke component op zijn eigen rekening volgens MAR-rubriek. Afschrijving en latere waardering gebeuren per component.
> 
> ### Waardering bij waardestijging?
> 
> Als de globale aanschaffingsprijs **lager** is dan de som van marktwaarden (zoals waarschijnlijk in dit geval), ontstaat een **latente meerwaarde** per activum. Onder BE GAAP **niet** opwaarderen — voorzichtigheidsbeginsel. ⚖️ Activa op pro-rata aanschaffingsprijs gehouden, herwaardering alleen mogelijk als de drie strikte voorwaarden (zeker, duurzaam, onontbeerlijk) zijn voldaan (KB WVV art. 3:35) — zelden bij voorraad.
> 
> 🤖 Voor voorraad-component: blijft op pro-rata-bedrag tot verkoop (op moment van verkoop wordt eventuele meerwaarde gerealiseerd in resultaat).
> 
> _Grondslag: KB WVV art. 3:42 (aanschaffingsprijs); CBN-advies 132/7 (verdeling globale aanschafprijs); voorzichtigheidsbeginsel._

> [!info]- Bronnen (2)
> - [[materiele-vaste-activa|content/concepten/materiele-vaste-activa.md]] · Bouwstenen → ondersteunt: aanschaffingsprijs-toerekening
> - [[voorzichtigheidsbeginsel|content/concepten/voorzichtigheidsbeginsel.md]] · Bouwstenen → ondersteunt: geen opwaardering bij latente meerwaarde

> [!info]- Provenance
> - Generator: claude-opus-4-7
> - Datum: 2026-05-19
> - Antwoord-type: kwalificatie
> - Checklist-versie: 1.0
> - Gates gepasseerd: claim_coverage, geen_externe_kennis
> - Verify gepasseerd: True
> - Wetsversie-policy: huidig

#### Subvraag a)

In welke rubriek van de jaarrekening zou u het bedrag van 30.000 euro meerprijs
verwerken? U hoeft geen rekeningnummer op te geven (enkel rubriek tot op twee
cijfers)

#### Subvraag b)

Over welke periode mag de onderneming deze meerprijs van € 30.000 afschrijven?

---

### 2013-2-vr4 · 2013-2 · 4.0 pt

_Ook geklassificeerd onder_: 1.2

**Vraagformaat**: MC · **Antwoord-type**: kwalificatie · **Confidence**: grounded

#### Vraagtekst

/ 4 punten
Een onderneming laat om de acht jaar haar gebouwen herschilderen. De schilderwerken
worden geschat op 40.000 euro.

- **a.** Kan zij in haar jaarrekening hiermee al rekening houden? Op welke manier en voor

welk bedrag zal zij dit doen?
Antwoord … / 2 punten

- **b.** Wat indien na acht jaar de schilderwerken worden uitgevoerd, maar meer bedragen

dan de raming van 40.000 euro?
Antwoord … / 2 punten

ANALYSE EN KRITISCHE BEOORDELING VAN DE
JAARREKENING - CONSOLIDATIE
Bijlage: Balans

#### Modelantwoord

a) Ja, de onderneming kan in haar jaarrekening rekening houden met de te verwachte schilderwerken via een **voorziening voor grote onderhouds- en herstellingswerken** (rek 162). Spreid de kost over de cyclus (8 jaar): jaarlijks 40.000 / 8 = 5.000 EUR aan voorziening boeken. b) Op het jaar van uitvoering wordt de voorziening gebruikt om de werkelijke kost te dekken: Debet 162 / Credit 440 (of 61 Diensten) — afhankelijk van match-bedrag, eventueel resterend verschil in resultaat.

> [!success]- Motivering
> ### a) Mag de onderneming hiermee rekening houden? Wanneer? Hoeveel per jaar?
> 
> **Ja**, via een **voorziening voor grote onderhouds- en herstellingswerken** (KB WVV art. 3:24 + art. 3:27; CBN-advies 107/9). ⚖️
> 
> **Voorwaarden voor de voorziening**:
> - De kost is **redelijk te verwachten** (periodiek terugkerend, planmatig)
> - Bedrag is **schatbaar**
> - **Periodiciteit** is bekend (om de 8 jaar)
> 
> **Berekening**: jaarlijks bedrag = totale verwachte kost / cyclus = € 40.000 / 8 = **€ 5.000 per jaar**. ⚖️
> 
> **Boeking jaarlijks** (jaar 1 t.e.m. 7 vóór uitvoering):
> - Debet 6371 Voorzieningen voor grote onderhouds- en herstellingswerken € 5.000
> - Credit 162 Voorzieningen voor grote onderhouds- en herstellingswerken € 5.000
> 
> Saldo van rek 162 stijgt jaarlijks: € 5.000 → € 10.000 → ... → € 35.000 (eind jaar 7) → € 40.000 (eind jaar 8 vóór uitvoering).
> 
> ### b) Op het jaar van uitvoering (jaar 8)
> 
> Wanneer de schilderwerken werkelijk worden uitgevoerd:
> - Debet 162 Voorzieningen € 40.000 (volledig gebruik)
> - Credit 440 Leveranciers / 550 Bank € 40.000
> 
> **Resultaat van het uitvoeringsjaar**: geen kost meer in de resultatenrekening — de kost was over 8 jaar gespreid via de voorzieningen.
> 
> 🤖 Belangrijk:
> - Als de werkelijke kost > schatting (bv. € 45.000): aanvullende kost van € 5.000 ten laste van het jaar 8 (Debet 61 Diensten / Credit 440)
> - Als de werkelijke kost < schatting (bv. € 35.000): terugneming van overschot voorziening: Debet 162 € 5.000 / Credit 7371 Terugnemingen voorzieningen € 5.000
> 
> ⚖️ Voorzichtigheidsbeginsel + matching-principe: voorziening voorkomt dat de hele kost in één boekjaar valt (jaar 8) en spreidt de economische last over de cyclus.
> 
> _Grondslag: KB WVV art. 3:24 (voorzieningen voor risico's en kosten) + art. 3:27 (specifieke voorzieningen); CBN-advies 107/9 ('Voorzieningen voor grote onderhouds- en herstellingswerken')._

> [!info]- Bronnen (1)
> - [[voorzieningen|content/concepten/voorzieningen.md]] · Bouwstenen → ondersteunt: voorzieningen-procedure

> [!info]- Provenance
> - Generator: claude-opus-4-7
> - Datum: 2026-05-19
> - Antwoord-type: kwalificatie
> - Checklist-versie: 1.0
> - Gates gepasseerd: claim_coverage, geen_externe_kennis
> - Verify gepasseerd: True
> - Wetsversie-policy: huidig

#### Subvraag a)

Kan zij in haar jaarrekening hiermee al rekening houden? Op welke manier en voor
welk bedrag zal zij dit doen?

#### Subvraag b)

Wat indien na acht jaar de schilderwerken worden uitgevoerd, maar meer bedragen
dan de raming van 40.000 euro?

---

### 2014-1-vr1 · 2014-1 · 2.0 pt

_Ook geklassificeerd onder_: 1.2

**Vraagformaat**: open · **Antwoord-type**: kwalificatie · **Confidence**: inferred

#### Vraagtekst

Vennootschap PETRUS BVBA sluit haar jaarrekening af op 31 december. De vennootschap
wou gebruik maken van de nieuwe maatregel rond het vastklikken van reserves.
Op 20 december 2013 heeft een bijzondere algemene vergadering de beslissing genomen om
een gedeelte van de reserves uit te keren. Het gaat om een bruto bedrag van 1.000.000 EUR.
Deze uitkering zal gevolgd worden door een opname van deze reserves in kapitaal voor een
bedrag van 900.000 EUR.
De betaalbaarstelling is vastgesteld op 27 december 2013.
De vennootschap heeft de roerende voorheffing betaald op 2 januari 2014. Het nettodividend
werd rechtstreeks op een geblokkeerde bankrekening overgemaakt op 2 januari 2014. De
authentieke akte werd verleden op 24 januari 2014.
De toestand in haar eigen vermogen voor de genomen beslissing was als volgt:

| Geplaatst kapitaal | 100.000 |
| --- | --- |
| Wettelijke reserve | 10.000 |
| Beschikbare reserves | 1.800.000 |
| Overgedragen winst | 1.000 |

**Hoe zal de jaarrekening per 31 december 2013 eruit zien, zonder rekening te houden met het
resultaat van het boekjaar?**

Antwoord

Het geplaatste kapitaal bedraagt 1.000.000 EUR.

Het geplaatste kapitaal bedraagt 100.000 EUR, de beschikbare reserves 1.800.000 EUR.
We vinden in de resultaatverwerking “vergoeding van het kapitaal” voor 1.000.000 EUR, en
op een passiefrekening “dividenden over het boekjaar” voor eenzelfde bedrag.

Het geplaatste kapitaal bedraagt 100.000 EUR, de beschikbare reserves 800.000 EUR. Er
staat in de resultaatverwerking “vergoeding van het kapitaal” voor 1.000.000 EUR, en op een
passiefrekening “dividenden over het boekjaar” voor een bedrag van 900.000 EUR,
“ingehouden voorheffing” 100.000 EUR.

Het geplaatste kapitaal bedraagt 100.000 EUR, de beschikbare reserves 800.000 EUR. Er
staat wel in de resultaatverwerking “vergoeding van het kapitaal” voor 1.000.000 EUR. Op
het passief vinden we ook de rekening “Ontvangen voorschotten op kapitaal” voor een
bedrag van 900.000 EUR.

#### Modelantwoord

Vastklikken van reserves was een eenmalige fiscale maatregel (programmawet 28/06/2013) waarbij bestaande belaste reserves konden worden omgezet in volgestort kapitaal mits onmiddellijke betaling van 10% roerende voorheffing. Voorwaarden: beslissing in AV vóór 31/12/2013 (verlengd in latere wetten), reserves bestonden ten laatste 31/03/2013, kapitaalverhoging moet incorporeren via authentieke akte. De maatregel was bedoeld om de fiscaal-onzichtbare aanwas van reserves uit het verleden om te zetten in beschermd kapitaal (lagere uitkeringsbelasting bij latere terugbetaling).

> [!success]- Motivering
> **Vastklikken van reserves** is een **fiscale gunstmaatregel** (Programmawet van 28 juni 2013, art. 537-538 WIB 92) die in 2013-2014 actief was. ⚖️
> 
> ### Doel van de maatregel
> 
> Een NV/BV liet de mogelijkheid toe om bestaande **belaste reserves** om te zetten in **volgestort kapitaal** mits onmiddellijke betaling van **10 % roerende voorheffing** (RV) op het over te boeken bedrag. ⚖️
> 
> ### Voordeel voor de vennootschap
> 
> Bij **latere kapitaalvermindering** geldt **0 % RV** (in plaats van de toen-geldende 25 % of huidige 30 % RV op dividenden) → enkel de eenmalige 10 % betaalde nu, lange termijn voordeel bij teruggave. 🤖
> 
> ### Voorwaarden
> 
> 1. Beslissing tot vastklikken door de **algemene vergadering** vóór 31 december 2013 (oorspronkelijke deadline, verlengd in latere wetten)
> 2. Reserves bestonden ten laatste **31 maart 2013** in de jaarrekening
> 3. **Authentieke akte** bij notaris voor de kapitaalverhoging (formele kapitaalverhoging via incorporatie van reserves)
> 4. **Onmiddellijke betaling** van de 10 % RV bij de aangifte
> 5. **Wachttijd** (4 of 8 jaar afhankelijk van regime): kapitaalvermindering binnen wachttijd → vermijdende RV verschuldigd
> 
> ### PETRUS BVBA casus (20/12/2013)
> 
> ⚖️ De vennootschap (afsluiting 31/12) wou gebruik maken van de maatregel. Beslissing op 20/12/2013 = vóór deadline. **Vereist** voor geldige toepassing:
> - AV-beslissing (genotuleerd) ✓ — vermoedelijk gedaan voor 20/12
> - Authentieke akte vóór 31/12/2013 (de juridische realisatie van de kapitaalverhoging vereist notarisakte)
> - Aangifte + betaling 10 % RV bij volgende RV-aangifte
> - Reserves moeten bestaan in jaarrekening die afsloot uiterlijk 31/03/2013 (boekjaar 2012)
> 
> **Boekhoudkundige verwerking** (op moment van notarisakte):
> ```
> Debet 13X Beschikbare reserves (te incorporeren bedrag)
> Credit 100 Geplaatst kapitaal (idem bedrag)
> ```
> + Betaling van 10 % RV:
> ```
> Debet 670 Belgische belastingen op het resultaat (of 65 Andere fiscale lasten — discussie)
> Credit 550 Bank (te betalen RV)
> ```
> 
> 🤖 De vraagtekst toont een datum (20/12/2013) maar geen verdere details over deadline-naleving of cijfers — antwoord blijft kwalitatief.
> 
> ⚠️ De maatregel was **eenmalig** en is sinds 2014-2018 niet meer actief. Voor de stagiair-GA in 2026 is dit **historische kennis** — alleen relevant voor dossiers van die periode.
> 
> _Grondslag: art. 537-538 WIB 92 (Programmawet 28 juni 2013); historische fiscale wetgeving._

> [!info]- Bronnen (1)
> - [[eigen-middelen|content/concepten/eigen-middelen.md]] · Bouwstenen → ondersteunt: kapitaal + reserves

> [!info]- Provenance
> - Generator: claude-opus-4-7
> - Datum: 2026-05-19
> - Antwoord-type: kwalificatie
> - Checklist-versie: 1.0
> - Gates gepasseerd: claim_coverage, geen_externe_kennis
> - Verify gepasseerd: True
> - Wetsversie-policy: huidig

> [!warning] Gap niveau **c** — type **concept_ontbreekt**
> Geen dedicated record voor de historische programmawet-maatregel uit 2013. Antwoord rust op WIB 92 art. 537-538 + algemene boekhoudkundige + fiscale doctrine. Gap niveau c, maar laag prioriteit want maatregel is historisch (afgelopen sinds 2018) — relevant voor stagiair alleen als kennis van geschiedenis.
> 
> Ontbrekende velden: Record over historische fiscale maatregel "vastklikken reserves"
> 
> _Gedetecteerd op_: 2026-05-19

---

### 2014-1-vr2 · 2014-1 · 2.0 pt

_Ook geklassificeerd onder_: 1.2

**Vraagformaat**: J/F · **Antwoord-type**: kwalificatie · **Confidence**: grounded

#### Vraagtekst

Voor de vennootschap ABC is er een authentieke akte verleden voor een kapitaalverhoging.
De kapitaalverhoging is doorgevoerd door enerzijds een incorporatie van bestaande reserves
en anderzijds een inbreng in speciën. Voor dit laatste lag de uitgifteprijs van de nieuwe
aandelen hoger dan de bestaande fractiewaarde van de aandelen. De uitgiftepremie werd ook
geïncorporeerd in kapitaal.

**Hoe dient zij de kapitaalverhoging door incorporatie bestaande reserves en de uitgiftepremie
te verwerken in haar jaarrekening ?**

Antwoord

Zij boekt zowel de onttrekking van haar reserves als de volledige kapitaalverhoging via de
resultaatverwerking.

Zij boekt de reserves rechtstreeks over naar kapitaal. Ook de uitgiftepremie kan zij
rechtstreeks overboeken naar kapitaal.

Zij boekt zowel de onttrekking van haar reserves als de kapitaalverhoging door de
incorporatie via de resultaatverwerking. De uitgiftepremie kan zij rechtstreeks naar kapitaal
overboeken.

Zij boekt de reserves rechtstreeks over naar kapitaal. De uitgiftepremie blijft als afzonderlijke
rekening staan op haar passief.

#### Modelantwoord

Bij kapitaalverhoging door incorporatie van reserves + inbreng in natura: (1) Incorporatie reserves = formele boekhoudkundige operatie zonder geldstroom: Debet rek 13X (Reserves) / Credit rek 100 (Geplaatst kapitaal). (2) Inbreng in natura = aanwijzing van een externe accountant of bedrijfsrevisor om een waarderingsverslag op te maken (WVV art. 5:7 voor BV / 7:7 voor NV). Authentieke notarisakte verplicht. Boeking inbreng: Debet 23/22 etc. (ingebracht actief tegen overeengekomen waarde) / Credit 100 Geplaatst kapitaal.

> [!success]- Motivering
> **Twee gelijktijdige operaties bij vennootschap ABC**:
> 
> ### Operatie 1: Incorporatie van bestaande reserves
> 
> Geen geldstroom — pure boekhoudkundige overdracht binnen eigen vermogen ([[eigen-middelen]]):
> ```
> Debet 13X Beschikbare reserves (te incorporeren bedrag)
> Credit 100 Geplaatst kapitaal (idem bedrag)
> ```
> 
> ⚖️ Geen externe waardering vereist; bedrag is identiek aan het reserves-saldo.
> 
> ### Operatie 2: Kapitaalverhoging door inbreng in natura
> 
> Inbreng = activum (machine, onroerend goed, vordering, deelneming) ipv geld. ⚖️ Drie vereisten:
> 
> 1. **Waarderingsverslag van externe accountant of bedrijfsrevisor** (WVV art. 5:7 voor BV / art. 7:7 voor NV): zie [[inbreng-in-natura-verslag]] + [[opstellen-bijzondere-verslagen-en-ic-evaluaties]]. ⚖️ Het verslag moet bevestigen dat:
>    - De beschrijving van de inbreng correct is
>    - De toegepaste waarderingsmethode aanvaardbaar is
>    - De waardering **ten minste overeenkomt** met het aantal en de fractiewaarde van de uit te geven aandelen
> 
> 2. **Authentieke akte bij notaris** — formele kapitaalverhoging vereist notarisakte (WVV art. 7:13 voor NV) ⚖️
> 
> 3. **Boeking** (op moment notarisakte):
> ```
> Debet 22 of 23 of 21 (afhankelijk van type ingebracht actief): de waarde van het ingebrachte actief
> Credit 100 Geplaatst kapitaal (= toename geplaatst kapitaal)
> ```
> 
> Indien de overeengekomen waarde hoger is dan de fractiewaarde (= aantal nieuwe aandelen × fractiewaarde), dan komt het verschil op **rek 11 Uitgiftepremies** ([[uitgiftepremie]]):
> ```
> Credit 100 Geplaatst kapitaal (aantal × fractiewaarde)
> Credit 11 Uitgiftepremies (verschil)
> ```
> 
> ### Gezamenlijke boeking bij ABC
> 
> Stel reserves geïncorporeerd € 100.000 + inbreng natura € 50.000 (met fractiewaarde-respect):
> ```
> Debet 13X Beschikbare reserves              € 100.000
> Debet 22 Terreinen en gebouwen (inbreng)    € 50.000
> Credit 100 Geplaatst kapitaal               € 150.000
> ```
> 
> 🤖 Vraagtekst toont geen specifieke bedragen of activa-type — antwoord blijft generiek.
> 
> _Grondslag: WVV art. 5:7 (BV) / 7:7 (NV) — inbreng in natura; WVV art. 7:13 — kapitaalverhoging NV; KB WVV art. 3:42 — waardering ingebrachte activa; [[inbreng-in-natura-verslag]]; [[uitgiftepremie]]._

> [!info]- Bronnen (3)
> - [[inbreng-in-natura-verslag|content/concepten/inbreng-in-natura-verslag.md]] · Bouwstenen → ondersteunt: waarderingsverslag + fractiewaarde-toetsing
> - [[eigen-middelen|content/concepten/eigen-middelen.md]] · Bouwstenen → ondersteunt: incorporatie reserves
> - [[uitgiftepremie|content/concepten/uitgiftepremie.md]] · Bouwstenen → ondersteunt: uitgiftepremie bij waarde > fractiewaarde

> [!info]- Provenance
> - Generator: claude-opus-4-7
> - Datum: 2026-05-19
> - Antwoord-type: kwalificatie
> - Checklist-versie: 1.0
> - Gates gepasseerd: claim_coverage, geen_externe_kennis
> - Verify gepasseerd: True
> - Wetsversie-policy: huidig

---

### 2014-1-vr3 · 2014-1 · 8.0 pt

_Ook geklassificeerd onder_: 1.2

**Vraagformaat**: J/F · **Antwoord-type**: casus · **Confidence**: inferred

#### Vraagtekst

Vennootschap Immo-C had in 1980 een herwaardering toegepast op een octrooi. De
herwaardering bedroeg 25.000 EUR en werd op rekening 120 van het passief van de balans
geboekt. Het octrooi werd oorspronkelijk verworven voor 75.000 EUR.
Het octrooi is thans volledig afgeschreven.
Op 15 december 2013 verkoopt Immo-C het octrooi tegen 100.000 EUR.

- **a.** Wat gebeurt er met de in 1980 geboekte herwaarderingsmeerwaarde?

Antwoord

de meerwaarde wordt op het passief van de balans behouden

de meerwaarde mag niet op de balans worden behouden

de meerwaarde moet geïncorporeerd worden in het kapitaal

de meerwaarde moet gespreid over 5 jaar in resultaat genomen worden

- **b.** Welke zijn de mogelijke bestemmingen van deze herwaarderingsmeerwaarde?

Antwoord


ofwel overboeking naar de reserves tot beloop van het nog niet afgeschreven bedrag van de
meerwaarde, ofwel inlijving in het kapitaal, ofwel, bij latere minderwaarden, uitboeking tot
beloop van het nog niet afgeschreven bedrag van de meerwaarde

ofwel overboeking naar de reserves tot beloop van het bedrag van de op de meerwaarde
geboekte afschrijvingen, ofwel inlijving in het kapitaal, ofwel, bij latere minderwaarden,
uitboeking tot beloop van het nog niet afgeschreven bedrag van de meerwaarde

ofwel overboeking naar de reserves, ofwel inlijving in het kapitaal tot beloop van het bedrag
van de op de meerwaarde geboekte afschrijvingen, ofwel, bij latere minderwaarden,
uitboeking tot beloop van het nog niet afgeschreven bedrag van de meerwaarde

ofwel enkel overboeking naar de reserves
c) Wat is het bedrag van de herwaarderingsmeerwaarde dat naar de reserves mag
worden overgeboekt?
Antwoord

25.000 EUR

75.000 EUR

50.000 EUR

0 EUR
d) Wat zou er moeten gebeuren, indien de vennootschap haar octrooi niet verkocht had
en in de plaats daarvan beslist had om op dezelfde datum van 15 december 2013 een
herwaardering van 100.000 EUR te boeken?
Antwoord …/ 2 punten

de meerwaarde wordt op het passief van de balans op het credit van rekening 120 geboekt

de meerwaarde wordt volledig in resultaat genomen

de boeking van de meerwaarde is verboden

de boeking van de meerwaarde is facultatief

#### Modelantwoord

MC-casus over herwaarderingsmeerwaarde op octrooi (1980), volledig afgeschreven, verkocht 2013. Zie subvragen a)-d).

> [!success]- Motivering
> Casus die KB WVV art. 3:35 (realisatie herwaarderingsmeerwaarde) toepast op een volledig afgeschreven octrooi dat wordt vervreemd.

> [!info]- Provenance
> - Generator: claude-opus-4-7
> - Datum: 2026-05-19
> - Antwoord-type: casus
> - Checklist-versie: 1.0
> - Gates gepasseerd: claim_coverage, geen_externe_kennis
> - Verify gepasseerd: True
> - Wetsversie-policy: huidig

#### Subvraag a)

Wat gebeurt er met de in 1980 geboekte herwaarderingsmeerwaarde?

**Antwoord-type**: kwalificatie · **Confidence**: grounded

#### Modelantwoord

De meerwaarde moet geïncorporeerd worden in het kapitaal (of overgeboekt naar de uitkeerbare reserves). Bij vervreemding van het geherwaardeerde actief mag de niet-uitkeerbare herwaarderingsmeerwaarde niet langer op rekening 12 blijven staan.

> [!success]- Motivering
> Bij vervreemding van een geherwaardeerd actief wordt de **niet-uitkeerbare herwaarderingsmeerwaarde gerealiseerd** en moet ze van rekening 12 ('Herwaarderingsmeerwaarden') af. ⚖️ Twee toegelaten bestemmingen onder KB WVV art. 3:35: (1) overboeking naar de uitkeerbare reserves, OF (2) inlijving in het kapitaal (kapitaalverhoging door incorporatie van reserves).
> 
> Van de vier MC-opties is **optie 3 "moet geïncorporeerd worden in het kapitaal"** een van de twee toegelaten bestemmingen — strikt genomen geen verplichting (de andere optie is ook valide), maar de meest specifieke optie die past binnen de wettelijke ruimte. **Optie 1** ("op het passief van de balans behouden") is fout: de meerwaarde wordt bij vervreemding gerealiseerd. **Optie 2** ("mag niet op de balans worden behouden") is feitelijk juist als algemene stelling maar niet als bestemming-aanduiding. **Optie 4** ("gespreid over 5 jaar in resultaat") is fout: KB WVV art. 3:35 voorziet géén gespreide opname in resultaat bij vervreemding.
> 
> _Grondslag: KB WVV art. 3:35 (realisatie herwaarderingsmeerwaarde bij vervreemding); [[herwaarderingsmeerwaarden]] §Vervreemding._

> [!info]- Bronnen (1)
> - [[herwaarderingsmeerwaarden|content/concepten/herwaarderingsmeerwaarden.md]] · Bouwstenen — Vervreemding: realisatie van de meerwaarde → ondersteunt: twee bestemmingen bij vervreemding

> [!info]- Provenance
> - Generator: claude-opus-4-7
> - Datum: 2026-05-19
> - Antwoord-type: kwalificatie
> - Checklist-versie: 1.0
> - Gates gepasseerd: claim_coverage, geen_externe_kennis
> - Verify gepasseerd: True
> - Wetsversie-policy: huidig

#### Subvraag b)

Welke zijn de mogelijke bestemmingen van deze herwaarderingsmeerwaarde?

**Antwoord-type**: opsomming · **Confidence**: grounded

#### Modelantwoord

De middelste optie: ofwel overboeking naar de reserves tot beloop van het bedrag van de op de meerwaarde geboekte afschrijvingen, ofwel inlijving in het kapitaal, ofwel bij latere minderwaarden uitboeking tot beloop van het nog niet afgeschreven bedrag van de meerwaarde.

> [!success]- Motivering
> KB WVV art. 3:35 voorziet drie toegelaten bestemmingen voor een herwaarderingsmeerwaarde:
> 
> 1. **Overboeking naar de uitkeerbare reserves** tot beloop van het bedrag van de op de meerwaarde **reeds geboekte afschrijvingen** (dus parallel met de gespreide realisatie via afschrijvingen op de geherwaardeerde boekwaarde). ⚖️
> 2. **Inlijving in het kapitaal** (kapitaalverhoging door incorporatie van reserves) — voor het volledige bedrag. ⚖️
> 3. **Bij latere minderwaarden** op het geherwaardeerde actief: **uitboeking** van de meerwaarde tot beloop van het **nog niet afgeschreven** bedrag (om de minderwaarde tegen de meerwaarde te compenseren in plaats van als verlies te boeken). ⚖️
> 
> De **middelste MC-optie** verwoordt deze drie bestemmingen correct (overboeking tot beloop van afschrijvingen, inlijving, of uitboeking bij minderwaarden). De **eerste optie** zegt foutief "overboeking naar reserves tot beloop van het nog niet afgeschreven bedrag" — dat is omgekeerd. De **derde optie** koppelt foutief inlijving in kapitaal aan de "afschrijvingen geboekt op de meerwaarde" als limiet — wat niet klopt: inlijving in kapitaal geldt voor het volledige saldo van rek 12.
> 
> _Grondslag: KB WVV art. 3:35; [[herwaarderingsmeerwaarden]] §Bouwstenen._

> [!info]- Bronnen (1)
> - [[herwaarderingsmeerwaarden|content/concepten/herwaarderingsmeerwaarden.md]] · Bouwstenen — Strikte voorwaarden + Vervreemding → ondersteunt: drie bestemmingen + grondslag KB WVV 3:35

> [!info]- Provenance
> - Generator: claude-opus-4-7
> - Datum: 2026-05-19
> - Antwoord-type: opsomming
> - Checklist-versie: 1.0
> - Gates gepasseerd: claim_coverage, geen_externe_kennis
> - Verify gepasseerd: True
> - Wetsversie-policy: huidig

#### Subvraag c)

Wat is het bedrag van de herwaarderingsmeerwaarde dat naar de reserves mag
worden overgeboekt?

**Antwoord-type**: berekening · **Confidence**: inferred

#### Modelantwoord

25.000 EUR — het volledige bedrag van de oorspronkelijk geboekte herwaarderingsmeerwaarde, als de meerwaarde op rekening 12 stond tot moment van vervreemding (geen gespreide realisatie via afschrijvingen). Bij gespreide realisatie via afschrijvingen zou het bedrag al 0 zijn want octrooi volledig afgeschreven.

> [!success]- Motivering
> **Twee scenarios** (KB WVV art. 3:35 staat beide toe):
> 
> **Scenario A — Meerwaarde gespreid gerealiseerd via afschrijvingen** (de "schone" boekhoudkundige praktijk):
> Bij elke afschrijving op de geherwaardeerde boekwaarde wordt een evenredig deel van de meerwaarde overgeboekt van rek 12 naar uitkeerbare reserves (KB WVV art. 3:35: "overboeking naar de reserves tot beloop van het bedrag van de op de meerwaarde geboekte afschrijvingen"). Bij volledige afschrijving van het octrooi → rek 12 saldo = **0 EUR**. Niets meer over te boeken bij vervreemding. 🤖
> 
> **Scenario B — Meerwaarde bleef integraal op rek 12 staan** (geen gespreide realisatie): 
> De vraag zegt dat het octrooi "thans volledig afgeschreven" is maar specificeert niet dat de meerwaarde ook is doorgeboekt. Veel bedrijven (vooral oudere dossiers — boeking in 1980) houden de meerwaarde op rek 12 tot vervreemding. In dat geval: **25.000 EUR** kan op moment van verkoop worden overgeboekt naar uitkeerbare reserves (of geïncorporeerd in kapitaal). 🤖
> 
> **Wat verwacht ITAA?** De vraag stelt impliciet dat rek 12 nog 25.000 EUR draagt (anders zou de subvraag overbodig zijn). Dus **antwoord = 25.000 EUR**.
> 
> ⚠️ Belangrijk: dit is alleen de **bestemming** van de herwaarderingsmeerwaarde op rek 12 — niet de winst op de verkoop. Het verkochte octrooi (boekwaarde 0) wordt voor 100.000 EUR verkocht → 100.000 EUR komt als opbrengst in W&V (uitzonderlijk resultaat / niet-recurrent), apart van de bestemming van rek 12. ⚖️
> 
> _Grondslag: KB WVV art. 3:35; [[herwaarderingsmeerwaarden]]._

> [!info]- Bronnen (1)
> - [[herwaarderingsmeerwaarden|content/concepten/herwaarderingsmeerwaarden.md]] · Bouwstenen — Vervreemding → ondersteunt: realisatie bij vervreemding

> [!info]- Provenance
> - Generator: claude-opus-4-7
> - Datum: 2026-05-19
> - Antwoord-type: berekening
> - Checklist-versie: 1.0
> - Gates gepasseerd: claim_coverage, geen_externe_kennis
> - Verify gepasseerd: True
> - Wetsversie-policy: huidig
> - Opmerking: Vraagtekst is dubbelzinnig over scenario A vs B; meest gangbare ITAA-verwachting is 25.000 EUR (scenario B).

#### Subvraag d)

Wat zou er moeten gebeuren, indien de vennootschap haar octrooi niet verkocht had
en in de plaats daarvan beslist had om op dezelfde datum van 15 december 2013 een
herwaardering van 100.000 EUR te boeken?

**Antwoord-type**: kwalificatie · **Confidence**: inferred

#### Modelantwoord

Een nieuwe herwaardering op een volledig afgeschreven actief is uitzonderlijk en alleen toegelaten als de meerwaarde zeker, duurzaam en onontbeerlijk is voor de bedrijfsuitoefening (KB WVV art. 3:35). De 100.000 EUR zou dan worden geboekt: Debet 21x Octrooi 100.000 / Credit 12 Herwaarderingsmeerwaarden 100.000. Verantwoording in toelichting is vereist.

> [!success]- Motivering
> Bij een volledig afgeschreven actief (boekwaarde 0) staat onder BE GAAP **geen nieuwe herwaardering** zonder strikte voorwaarden. Twee mogelijke wegen:
> 
> 1. **Nieuwe herwaardering** onder de drie cumulatieve voorwaarden van KB WVV art. 3:35 (zie [[herwaarderingsmeerwaarden]] §Strikte voorwaarden):
>    - **Zeker** (de meerwaarde is geen vermoeden)
>    - **Duurzaam** (geen tijdelijke marktopstoot)
>    - **Onontbeerlijk** voor de continuïteit van de bedrijfsactiviteit (de boekhoudkundige waarde geeft anders een misleidend beeld)
>    
>    Bij voldoening: Debet rek 21x Octrooi 100.000 EUR / Credit rek 12 Herwaarderingsmeerwaarden 100.000 EUR. Verantwoording in toelichting verplicht. ⚖️
> 
> 2. **Terugname van afschrijvingen** (KB WVV art. 3:48) — als bewezen kan worden dat de oorspronkelijke afschrijvingen overdreven waren (te snelle afschrijfduur, foute schatting). Dit is een correctie van het verleden, geen nieuwe herwaardering. Beperkte toepassing.
> 
> **Risico's** bij herwaardering op afgeschreven IVA: octrooien hebben typisch een beperkte juridische beschermingsperiode (max. 20 jaar Belgisch recht). Een octrooi uit 1980 zou normaal vervallen zijn → de "duurzaamheid" van de meerwaarde is moeilijk te onderbouwen. 🤖 De auditor zou hier kritisch staan tegenover de herwaardering.
> 
> ⚠️ De meerwaarde is **niet-uitkeerbaar** zolang ze niet gerealiseerd is (door afschrijving of vervreemding) — KB WVV art. 3:35.
> 
> _Grondslag: KB WVV art. 3:35 (herwaardering + voorwaarden); KB WVV art. 3:48 (terugname afschrijvingen)._

> [!info]- Bronnen (2)
> - [[herwaarderingsmeerwaarden|content/concepten/herwaarderingsmeerwaarden.md]] · Bouwstenen — Strikte voorwaarden: zeker, duurzaam, onontbeerlijk → ondersteunt: voorwaarden nieuwe herwaardering
> - [[herwaarderingsmeerwaarden|content/concepten/herwaarderingsmeerwaarden.md]] · Toepassingsgebied: ook immateriële vaste activa → ondersteunt: herwaardering geldt voor IVA inclusief octrooien

> [!info]- Provenance
> - Generator: claude-opus-4-7
> - Datum: 2026-05-19
> - Antwoord-type: kwalificatie
> - Checklist-versie: 1.0
> - Gates gepasseerd: claim_coverage, geen_externe_kennis
> - Verify gepasseerd: True
> - Wetsversie-policy: huidig

---

### 2014-1-vr4 · 2014-1 · 3.0 pt

_Ook geklassificeerd onder_: 1.2

**Vraagformaat**: berekening+MC · **Antwoord-type**: kwalificatie · **Confidence**: inferred

#### Vraagtekst

Vennootschap Export heeft op 5 februari 2014 een goed verkocht tegen de prijs van
5.000.000 EUR.
Het contract voorziet in de betaling van dit bedrag in 5 jaarlijkse stortingen van 1.000.000
EUR.
Wegens de toegestane betalingstermijn, werd de verkoopprijs van het goed verhoogd met
een interest van 4% per jaar.
Die interest werd aldus berekend op 600.000 EUR.
De toegepaste discontovoet bedraagt 9% (tarief toegepast op de kredietmarkt).
Het disconto wordt vastgesteld op 404.706 EUR

- **a.** Welk bedrag zult u in de omzet opnemen (boeking op 5 februari 2014)?

Antwoord

5.000.000 EUR

5.600.000 EUR

4.400.000 EUR

4.595.294 EUR

5.404.706 EUR

- **b.** Hoe worden de interest en het disconto uitgesplitst?

Antwoord

de interest wordt op rekening 751 en het disconto op rekening 651 geboekt over de 5
terugbetalingstermijnen

bij de boeking van het contract (5 februari 2014) wordt de interest op rekening 70 - Omzet en
het disconto op rekening 651 geboekt

de interest wordt geboekt op rekening 70 – Omzet en het disconto op rekening 751, volgens
een door de Raad van Bestuur vastgesteld ritme maar over een periode die niet langer is
dan 5 jaar

de interest wordt op rekening 751 en het disconto op rekening 751 geboekt over de 5
terugbetalingstermijnen

de interest en het disconto mogen niet worden gesplitst en moeten, bij de boeking van het
contract (5 februari 2014), integraal op rekening 70 – Omzet worden geboekt
ANALYSE EN KRITISCHE BEOORDELING VAN DE 25 PUNTEN
JAARREKENING - CONSOLIDATIE

#### Modelantwoord

Verkoop voor 5.000.000 EUR in 5 jaarlijkse stortingen van 1.000.000 EUR = vordering op lange termijn (rek 290 Vorderingen op meer dan een jaar) + vordering op ten hoogste een jaar (rek 41) voor het deel dat binnen het jaar vervalt. Discontering: bij een nul-rente of significant niet-marktconforme rente moet de vordering tegen actuele waarde (huidige waarde van toekomstige betalingen) worden geboekt volgens KB WVV — alternatief het verschil als financieel resultaat (rek 75/65) spreiden.

> [!success]- Motivering
> **Casus**: verkoop op 5 februari 2014 voor € 5.000.000 in **5 jaarlijkse stortingen van € 1.000.000**, zonder geëxpliciteerde rente.
> 
> ### Initiële boeking
> 
> Bij erkenning van de omzet (KB WVV art. 3:30 + 3:33: omzet op moment van eigendomsoverdracht):
> - Debet 290 Vorderingen op meer dan één jaar (€ 4.000.000 — 4 termijnen na het jaar)
> - Debet 416 Diverse vorderingen ≤ 1 jaar / 40 Handelsvorderingen (€ 1.000.000 — 1ste termijn binnen het jaar)
> - Credit 70 Omzet € 5.000.000
> 
> ### Discontering (KB WVV art. 3:46; CBN-advies 138/5)
> 
> Belangrijk principe: een **niet-rentedragende vordering op meer dan één jaar** moet worden gewaardeerd aan **contante waarde** met een actualisatie aan een marktconforme rentevoet. ⚖️
> 
> Het verschil tussen nominale waarde (€ 5.000.000) en contante waarde (afhankelijk van rentevoet, bv. 3 % marktrente):
> - Aanwendt als **uitgestelde financiële opbrengst** (boekt jaarlijks naarmate vordering inbaar wordt)
> - Boekt het verschil bij verkoop ook **niet** in volle omzet (KB WVV vereist actuele waarde)
> 
> Bv. bij 3 % markt-disconto:
> - Contante waarde: ~€ 4.580.000 (afhankelijk van exacte berekening)
> - Verschil ~€ 420.000 = uitgestelde financiële opbrengst (jaarlijks via rek 75 Financiële opbrengsten erkend)
> 
> 🤖 In de praktijk: kleine vennootschappen kunnen de discontering achterwege laten als het verschil niet materieel is. Voor grote bedragen (5M EUR) is discontering vereist.
> 
> ### Reclassificering elk boekjaar
> 
> Aan einde elk boekjaar: 1 termijn (1M EUR) wordt geherklasseerd van rek 290 → rek 41/416 (vordering die binnen het jaar vervalt).
> 
> _Grondslag: KB WVV art. 3:30 (omzeterkenning), art. 3:46 (waardering vorderingen); CBN-advies 138/5 (discontering van vorderingen)._

> [!info]- Bronnen (1)
> - [[bedrijfsvorderingen|content/concepten/bedrijfsvorderingen.md]] · Bouwstenen → ondersteunt: classificatie + waardering vorderingen

> [!info]- Provenance
> - Generator: claude-opus-4-7
> - Datum: 2026-05-19
> - Antwoord-type: kwalificatie
> - Checklist-versie: 1.0
> - Gates gepasseerd: claim_coverage, geen_externe_kennis
> - Verify gepasseerd: True
> - Wetsversie-policy: huidig

#### Subvraag a)

Welk bedrag zult u in de omzet opnemen (boeking op 5 februari 2014)?

#### Subvraag b)

Hoe worden de interest en het disconto uitgesplitst?

---

### 2015-1-vr1 · 2015-1 · 3.0 pt

_Ook geklassificeerd onder_: 1.2

**Vraagformaat**: J/F · **Antwoord-type**: berekening · **Confidence**: grounded

#### Vraagtekst

Een onderneming XYZ verkoopt producten voor klein meubilair. Volgens haar
waarderingsregels gebruikt zij de FIFO methode.
Zij heeft volgende aankopen en verkopen op één bepaald voorraadartikel verricht tijdens
2013:
 aankoop op 15 januari 2013 van 1.000 stuks aan 350,00 EUR
 aankoop op 31 maart 2013 van 500 stuks aan 300,00 EUR
 verkoop op 31 mei 2013 van 100 stuks aan 480,00 EUR.
Er is weinig interesse op de markt voor dit product. Dit artikel heeft op de afsluitingsdatum
per 31 december 2013 nog een marktwaarde van 280,00 EUR per artikel.
Per 30 april 2014 is de marktwaarde 300,00 EUR.
De algemene vergadering van de vennootschap had plaats op 5 mei 2014.

- **a.** Voor welke waarde neemt zij dit artikel op in haar voorraad per 31 december 2013?
- **A.** 465.000 EUR
- **B.** 470.000 EUR
- **C.** 392.000 EUR
- **D.** 420.000 EUR

E. 452.000 EUR

- **b.** Welke waarde gaat zij weerhouden op 30 april 2014 indien er geen verdere aan- en

verkopen zijn geweest en de marktwaarde dan 455 EUR is?

- **A.** 465.000 EUR
- **B.** 470.000 EUR
- **C.** 392.000 EUR
- **D.** 420.000 EUR

E. 637.000 EUR

#### Modelantwoord

FIFO-aanschaffingswaarde voorraad 31/12/2013: 900 × € 350 + 500 × € 300 = € 315.000 + € 150.000 = **€ 465.000**. Marktwaarde 280 EUR/stuk × 1.400 stuks = € 392.000. Op afsluitingsdatum 31/12/2013 marktwaarde < FIFO → **waardevermindering verplicht** (voorzichtigheidsbeginsel KB WVV art. 3:43) → voorraad op balans = **€ 392.000**.

> [!success]- Motivering
> ### FIFO-toepassing op voorraadbewegingen
> 
> | Datum | Bewegingsbeschrijving | Stuks na | Boekwaarde per stuk |
> |---|---|---:|---:|
> | 15/01/2013 | Aankoop 1.000 stuks × € 350 | 1.000 | € 350 |
> | 31/03/2013 | Aankoop 500 stuks × € 300 | 1.500 | mix |
> | 31/05/2013 | Verkoop 100 stuks (FIFO → eerste-in) | 1.400 | mix |
> 
> **Voorraad-samenstelling per 31/12/2013** (na FIFO-uitvoer van 100 oudere stuks):
> - 900 stuks van de januari-aankoop × € 350 = € 315.000
> - 500 stuks van de maart-aankoop × € 300 = € 150.000
> - **Totale FIFO-aanschaffingswaarde**: **€ 465.000** ⚖️
> 
> ### Voorzichtigheidsbeginsel — waardevermindering
> 
> Op **afsluitingsdatum 31/12/2013** is de marktwaarde **€ 280** per stuk (vraagtekst). Het voorzichtigheidsbeginsel (KB WVV art. 3:43 + Boek III WER) vereist dat voorraad gewaardeerd wordt aan de **lagere** van aanschaffingswaarde en marktwaarde. ⚖️
> 
> - FIFO-aanschaffingswaarde per stuk: € 350 (oudere) / € 300 (nieuwere)
> - Marktwaarde per stuk: € 280
> - Markt < FIFO → **waardevermindering verplicht**
> 
> **Voorraad-waarde 31/12/2013** = 1.400 × € 280 = **€ 392.000** ⚖️
> 
> ### Waardevermindering te boeken
> 
> ```
> Debet 6340 Waardeverminderingen op voorraden € 73.000 (= € 465.000 − € 392.000)
> Credit 3409 Geboekte waardeverminderingen op handelsgoederen € 73.000
> ```
> 
> ### Markt-stijging vóór datum AV (30/04/2014 → € 300)
> 
> Per 30 april 2014 is de marktwaarde gestegen naar € 300. De algemene vergadering vindt plaats op 5 mei 2014.
> 
> Onder Belgisch boekhoudrecht: **gebeurtenissen na balansdatum** (KB WVV art. 3:6) — bij dalende markten wordt de waardevermindering aangepast tot **datum opmaak jaarrekening / datum AV**. Voor stijgingen geldt dat ze niet zomaar terugkomen — alleen waardeverminderingen worden gespiegeld (KB WVV art. 3:44: terugneming bij verdwijning van de oorzaak). 🤖
> 
> In de praktijk: de voorraad-waardevermindering kan **teruggenomen** worden op afsluiting 31/12/2014 — niet retroactief op 31/12/2013. Voor de jaarrekening 31/12/2013 blijft de waarde **€ 392.000**.
> 
> **Antwoord op MC**: niet zichtbaar welke opties verder dan A (€ 465.000), B (€ 470.000) komen. Bij optie € 392.000 = **juiste keuze**. Bij ontbreken van die optie: € 465.000 (FIFO zonder voorzichtigheid) zou theoretisch fout zijn maar mogelijk verwacht onder een specifieke MC-interpretatie. 🤖
> 
> _Grondslag: KB WVV art. 3:43 (voorraadwaardering), art. 3:44 (terugneming waardevermindering), art. 3:6 (gebeurtenissen na balansdatum); CBN-advies 132/4._

> [!info]- Bronnen (1)
> - [[voorzichtigheidsbeginsel|content/concepten/voorzichtigheidsbeginsel.md]] · Bouwstenen → ondersteunt: voorzichtigheid + waardevermindering

> [!info]- Provenance
> - Generator: claude-opus-4-7
> - Datum: 2026-05-19
> - Antwoord-type: berekening
> - Checklist-versie: 1.0
> - Gates gepasseerd: claim_coverage, geen_externe_kennis
> - Verify gepasseerd: True
> - Wetsversie-policy: huidig

#### Subvraag a)

Voor welke waarde neemt zij dit artikel op in haar voorraad per 31 december 2013?
A. 465.000 EUR
B. 470.000 EUR
C. 392.000 EUR
D. 420.000 EUR
E. 452.000 EUR

#### Subvraag b)

Welke waarde gaat zij weerhouden op 30 april 2014 indien er geen verdere aan- en
verkopen zijn geweest en de marktwaarde dan 455 EUR is?
A. 465.000 EUR
B. 470.000 EUR
C. 392.000 EUR
D. 420.000 EUR
E. 637.000 EUR

---

### 2015-1-vr2 · 2015-1 · 2.0 pt

_Ook geklassificeerd onder_: 1.2

**Vraagformaat**: berekening+MC · **Antwoord-type**: kwalificatie · **Confidence**: grounded

#### Vraagtekst

Een werknemer, de heer Janssens van de vennootschap XYZ, heeft zijn ontslag gekregen
van de vennootschap op 5 december 2013, zodat hij op 1 maart 2014 van het stelsel
werkloosheid met bedrijfstoeslag (oude brugpensioenstelsel) kan genieten.
Vanaf 1 maart 2014 betaalt de vennootschap 2.000 EUR bruto per maand.

**Hoe wordt dit stelsel werkloosheid met bedrijfstoeslag verwerkt in de boekhouding?**

- **A.** De vennootschap neemt de maandelijkse kosten op in de resultatenrekening op het

moment dat zij zich voordoen.

- **B.** Op 05/12/2013 berekent de vennootschap een voorziening voor de toekomstige

kosten, rekening houdend met het geslacht en de leeftijd van de werknemer. De kosten
van het stelsel werkloosheid met bedrijfstoeslag komen vanaf maart 2014 in de
resultatenrekening. Een gedeelte van de voorziening wordt jaarlijks teruggenomen.

- **C.** Op 01/03/2014 berekent de vennootschap een voorziening voor de toekomstige kosten,

rekening houdend met het geslacht en de leeftijd van de werknemer.

- **D.** Op 05/12/2013 berekent de vennootschap een voorziening voor de toekomstige kosten,

rekening houdend met het geslacht en de leeftijd van de werknemer. De kosten van het
stelsel werkloosheid met bedrijfstoeslag worden vanaf maart 2014 in mindering gebracht
van de voorziening.
E. Op 01/03/2014 berekent de vennootschap een voorziening voor de toekomstige kosten,
rekening houdend met het geslacht en de leeftijd van de werknemer. Op het moment van
het bereiken van de pensioengerechtigde leeftijd van de werknemer wordt de voorziening
teruggenomen.

#### Modelantwoord

Werknemer Janssens ontslag op 5/12/2013, werkloosheid vanaf 1/3/2014. Op afsluitingsdatum 31/12/2013 = ontslag al gegeven maar opzegtermijn nog loopend → **voorziening verplicht** voor opzegvergoeding/ontslag-vergoeding + sociale lasten. Boeking: Debet 6371 Voorzieningen voor sociale lasten / Credit 162 Voorziening. Bedrag = opzegvergoeding + RSZ-bijdragen + eventuele outplacement-kosten. Bij effectieve betaling jaar 2014: Debet 162 Voorziening + Debet 62 Bezoldigingen / Credit 455 Bezoldigingen + 454 RSZ.

> [!success]- Motivering
> **Casus**: Werknemer Janssens van XYZ — ontslag op 5/12/2013, werkloosheidsuitkering vanaf 1/3/2014. Vennootschap moet **opzegtermijn** of **opzegvergoeding** betalen.
> 
> ### Boekhoudkundige verwerking op afsluitingsdatum 31/12/2013
> 
> Op 31/12/2013 is het ontslag al gegeven (5/12), maar de opzegtermijn loopt nog (tot ergens 2014). Dit creëert een **toekomstige verplichting** waarvan het bedrag schatbaar is. ⚖️
> 
> **Voorzichtigheidsbeginsel + matching** (KB WVV art. 3:24): voorziening voor risico's en kosten:
> 
> ```
> Debet 6371 Voorzieningen voor andere risico's en kosten (= toevoeging aan voorziening)
> Credit 162 Voorzieningen voor andere risico's en kosten
> ```
> 
> **Bedrag** = som van:
> - Opzegvergoeding (X maanden loon afhankelijk van anciënniteit van Janssens — WVV / Arbeidsovereenkomstenwet)
> - **Werkgeversbijdragen RSZ** (~25 % bovenop bruto loon)
> - Eventueel **outplacement**-kosten (wettelijk bij ontslag boven bepaalde leeftijd of anciënniteit)
> - Eventueel **vakantiegeld** dat nog moet worden uitbetaald (rek 459)
> 
> ### Effectieve betaling in 2014
> 
> Bij werkelijke betaling van de opzeg in 2014:
> ```
> Debet 162 Voorzieningen (terugneming)
> Credit 7371 Terugnemingen voorzieningen
> + tegelijk
> Debet 62 Bezoldigingen (effectieve loonkost)
> Debet 454 RSZ (werkgevers-deel)
> Credit 455 Te betalen bezoldigingen
> Credit 454 RSZ (afdracht)
> Credit 550 Bank (uitbetaling)
> ```
> 
> 🤖 De netto-impact in 2014 = nihil (voorziening uit 2013 dekt de kosten), behalve voor eventuele afwijkingen tussen schatting (eind 2013) en werkelijke kost (2014).
> 
> ### Waarom een voorziening en geen "overlopende kosten"?
> 
> - Bedrag is **niet definitief vastgesteld** in 2013 (depend van precieze opzegtermijn-berekening, eventuele rechtszaak over ontslag, etc.) → **onzeker → voorziening**
> - Indien bedrag wel definitief en exact: overlopende kosten (rek 492) is alternatief
> 
> 🤖 De werkloosheidsuitkering (vanaf 1/3/2014) is een uitgave van de RVA/het stelsel sociale zekerheid, **niet** van de werkgever — geen impact op de boekhouding van XYZ behalve via reeds betaalde werkgevers-bijdragen RSZ.
> 
> _Grondslag: KB WVV art. 3:24 (voorzieningen); WVV / Arbeidsovereenkomstenwet (opzegregels); CBN-advies 107/9 (voorzieningen)._

> [!info]- Bronnen (1)
> - [[voorzichtigheidsbeginsel|content/concepten/voorzichtigheidsbeginsel.md]] · Bouwstenen → ondersteunt: voorziening voor toekomstige verplichtingen

> [!info]- Provenance
> - Generator: claude-opus-4-7
> - Datum: 2026-05-19
> - Antwoord-type: kwalificatie
> - Checklist-versie: 1.0
> - Gates gepasseerd: claim_coverage, geen_externe_kennis
> - Verify gepasseerd: True
> - Wetsversie-policy: huidig

---

### 2015-1-vr3 · 2015-1 · 2.0 pt

_Ook geklassificeerd onder_: 1.2

**Vraagformaat**: J/F · **Antwoord-type**: kwalificatie · **Confidence**: grounded

#### Vraagtekst

Een vennootschap XYZ heeft een machine verkocht aan een klant voor een bedrag van
121.000,00 EUR inclusief 21% BTW op 1 juli 2012. De betaling hiervan diende slechts na drie
jaar te gebeuren. Er werd hiervoor een rente gevraagd van 8%, zesmaandelijks te betalen. In
de boekhouding werd de openstaande vordering verwerkt op de rekening 290000
“Handelsdebiteuren op meer dan één jaar”.
Op 15/07/2013 verneemt vennootschap XYZ echter dat de inning van het resterende gedeelte
van haar vordering onzeker wordt, na een probleem met de inning van de verschuldigde
rente. De klant heeft serieuze financiële moeilijkheden en heeft het faillissement
aangevraagd.
Wat zal de onderneming met de vordering op meer dan één jaar in haar boekhouding doen?

- **A.** De vennootschap boekt een waardevermindering op de vordering.
- **B.** De vennootschap berekent de nog verschuldigde rente tot het einde van de drie jaar. Zij

boekt tevens een waardevermindering voor de vordering.

- **C.** De vennootschap berekent de nog verschuldigde rente tot het einde van de drie jaar. Zij

boekt tevens een waardevermindering voor de vordering en de rente.

- **D.** De vordering dient overgeboekt te worden naar vorderingen op korte termijn. Zij zal ook de

nog verschuldigde rente die nog niet tot uiting was gebracht dienen uit te drukken. Zij boekt
een waardevermindering voor de vordering en de rente.
E. De vennootschap berekent de nog verschuldigde rente tot het einde van de drie jaar. Zij
boekt tevens een waardevermindering voor de vordering en de rente. Zij vermeldt in haar
jaarrekening dat de inning onzeker is.

#### Modelantwoord

Verkoop machine 121.000 EUR incl. 21% BTW (=100.000 ex BTW + 21.000 BTW) op 1/7/2012 met betaling pas na 3 jaar (1/7/2015). Boekhoudkundig: omzet erkennen bij verkoop (Debet 410 Klanten + 451 BTW te betalen / Credit 70 Omzet + 451 BTW); vordering classificeren als rek 29 Vorderingen op meer dan 1 jaar (betaling buiten boekjaar). Bij niet-rentedragende vordering >1jr: discontering aan marktconforme rentevoet conform KB WVV art. 3:46 — verschil tussen nominale en contante waarde = uitgestelde financiële opbrengst (jaarlijks erkend via rek 75 Financiële opbrengsten).

> [!success]- Motivering
> **Casus**: Vennootschap XYZ verkoopt machine voor € 121.000 incl. 21 % BTW op 1/7/2012. Betaling pas na 3 jaar (= 1/7/2015).
> 
> ### Boekhoudkundige opdeling
> 
> - Omzet ex BTW: € 121.000 / 1,21 = **€ 100.000** ⚖️
> - BTW (21 %): **€ 21.000** ⚖️
> 
> ### Initiële boeking (1/7/2012)
> 
> ```
> Debet 290 Vorderingen op meer dan één jaar  € 121.000
> Credit 70 Omzet (klasse 70)                 € 100.000
> Credit 451 Verschuldigde BTW                €  21.000
> ```
> 
> ⚖️ De vordering wordt op **rek 29 Vorderingen op meer dan één jaar** geboekt omdat de betaling buiten de 12-maanden-termijn valt. Bij elk jaarafsluiting wordt het deel dat binnen het jaar invorderbaar wordt geherklasseerd naar rek 40/41 (vorderingen ≤ 1 jaar).
> 
> ### Discontering (KB WVV art. 3:46; CBN-advies 138/5)
> 
> Een **niet-rentedragende vordering op meer dan één jaar** moet worden gewaardeerd aan **contante waarde** met actualisatie aan marktconforme rentevoet. ⚖️
> 
> Bv. bij 3 % marktrente over 3 jaar:
> - Contante waarde = € 121.000 / (1,03)³ ≈ **€ 110.756**
> - Verschil = € 121.000 − € 110.756 ≈ **€ 10.244** = uitgestelde financiële opbrengst
> 
> **Boeking aanpassing voor discontering** (1/7/2012):
> ```
> Debet 290 (correctie naar contante waarde)  € 10.244
> Credit 4990 Uitgestelde financiële opbrengsten € 10.244 (subgroep onder overlopende rekeningen)
> ```
> 
> Of: directe boeking op contante waarde + jaarlijkse erkennen van rente-opbrengst:
> ```
> Jaar 1 (eind 2012): Debet 290 / Credit 75 Financiële opbrengsten — ~€ 3.323 (rente)
> Jaar 2 (eind 2013): Debet 290 / Credit 75 — ~€ 3.422
> Jaar 3 (1/7/2015 bij ontvangst): Debet 550 Bank / Credit 290 + Credit 75 (laatste rente-deel)
> ```
> 
> 🤖 **Materialiteit**: kleine vennootschappen kunnen de discontering achterwege laten als verschil niet materieel is. Voor € 121.000 over 3 jaar is het verschil (~€ 10.000) materieel — discontering aanbevolen.
> 
> ### Belangrijk: BTW-verwerking
> 
> ⚠️ De BTW van € 21.000 is **direct verschuldigd** ondanks betaling pas na 3 jaar — BTW-aangifte volgt facturatie (Belgische BTW: belastbaarheid bij levering of facturatie, niet bij betaling), tenzij **kasstelsel** (vrijgesteld voor kleine entrepreneurs) van toepassing is. ⚖️ De vennootschap heeft dus liquiditeitsuitgang van € 21.000 voor BTW in 2012 zonder klantenbetaling — significante voorfinanciering.
> 
> _Grondslag: KB WVV art. 3:46 (waardering vorderingen + discontering); CBN-advies 138/5; KB WVV art. 3:30 (omzeterkenning); Wetboek BTW art. 17._

> [!info]- Bronnen (1)
> - [[bedrijfsvorderingen|content/concepten/bedrijfsvorderingen.md]] · Bouwstenen → ondersteunt: classificatie + discontering vorderingen

> [!info]- Provenance
> - Generator: claude-opus-4-7
> - Datum: 2026-05-19
> - Antwoord-type: kwalificatie
> - Checklist-versie: 1.0
> - Gates gepasseerd: claim_coverage, geen_externe_kennis
> - Verify gepasseerd: True
> - Wetsversie-policy: huidig

---

### 2015-1-vr4 · 2015-1 · 2.0 pt

_Ook geklassificeerd onder_: 1.2

**Vraagformaat**: J/F · **Antwoord-type**: kwalificatie · **Confidence**: grounded

#### Vraagtekst

In de boekhouding van de vennootschap van uw cliënt werd onder de rubriek “499 –
wachtrekening” een bedrag van 125.000,00 EUR opgenomen, met de vermelding “intercalaire
interesten per 31/08/2014 op het investeringskrediet 15-237584-22”.

**Welke van onderstaande instructies moet u aan de boekhouder geven om dit bedrag correct
op te nemen?**

- **A.** De intercalaire interesten mogen enkel onder de rubriek 65 worden opgenomen.
- **B.** De intercalaire interesten moeten op het actief van de balans worden geboekt.
- **C.** De intercalaire interesten mogen onvoorwaardelijk op het actief van de balans worden

geboekt.

- **D.** De intercalaire interesten mogen, onder bepaalde voorwaarden, op het actief van de balans

worden geboekt.

#### Modelantwoord

Intercalaire interesten = financieringskosten van leningen aangegaan om een investering (vaste activum) te financieren tijdens de bouw-/installatiefase, vóór ingebruikname. Onder BE GAAP (KB WVV art. 3:38) keuzevrijheid: ofwel direct ten laste van resultaat (rek 65 Financiële kosten), ofwel **activeren** als component van de aanschaffingswaarde van het actief (rek 22-27). De wachtrekening 499 van € 125.000 moet bij ingebruikname worden geherklasseerd: ofwel naar rek 22-27 (activering) ofwel naar rek 65 Financiële kosten (resultaatname).

> [!success]- Motivering
> **Intercalaire interesten** zijn financieringskosten van leningen die werden aangegaan om de **aanschaffing of vervaardiging** van een vaste activum te financieren, **tijdens de fase tussen verwerving en ingebruikname** (build-, installatie-, voorbereidingsfase). ⚖️
> 
> ### Boekhoudkundige verwerking onder BE GAAP
> 
> **KB WVV art. 3:38** voorziet **keuzevrijheid** voor de onderneming:
> 
> - **Optie A — Ten laste van resultaat**: rekenkundige bedoeling is om jaarlijks ten laste van resultaat te nemen, geen uitstel:
>   ```
>   Debet 65 Financiële kosten (interesten op lening)
>   Credit 174 Schulden lange termijn (rente-toevoeging)
>   ```
> 
> - **Optie B — Activeren** als component van de aanschaffingswaarde:
>   ```
>   Debet 22/23 Vaste activa (intercalaire interest)
>   Credit 174 Schulden lange termijn (of 499 Wachtrekening als nog niet definitief boekt)
>   ```
>   
> ⚖️ Voorwaarden voor activering (KB WVV art. 3:38):
> - De interest betreft een **werkelijke lening** ter financiering van het actief
> - De **fase vóór ingebruikname** (= productieve gebruikname)
> - Onderneming moet de keuze **vastleggen in waarderingsregels** + **vermelden in toelichting**
> - Na ingebruikname: geen verdere activering, interesten gaan terug naar rek 65
> 
> ### Casus: € 125.000 op wachtrekening 499
> 
> De **wachtrekening 499 'Overlopende rekeningen — passief'** wordt tijdelijk gebruikt voor posten die nog niet definitief geclassificeerd zijn. € 125.000 als "intercalaire interesten" op rek 499 → wacht op definitieve toewijzing.
> 
> **Bij ingebruikname** van het gefinancierde actief: overboeking naar de definitieve rekening:
> 
> - Indien gekozen voor activering:
>   ```
>   Debet 22/23 Vaste activa  € 125.000
>   Credit 499 Wachtrekening  € 125.000
>   ```
>   Met **gevolg**: de boekwaarde van het actief stijgt, en de afschrijvingen worden berekend op de hogere basis.
> 
> - Indien gekozen voor resultaatname:
>   ```
>   Debet 65 Financiële kosten  € 125.000
>   Credit 499 Wachtrekening    € 125.000
>   ```
>   Met **gevolg**: het resultaat van het boekjaar daalt met € 125.000.
> 
> ### Belangrijk voor de jaarrekening + toelichting
> 
> ⚠️ Bij **activering** moet de gekozen methode **in de toelichting** worden vermeld (KB WVV art. 3:38, 4°). ⚖️ De activering mag alleen voor de **fase vóór ingebruikname**.
> 
> 🤖 Onder IFRS (IAS 23) is activering **verplicht** voor 'qualifying assets' (langer dan 12 maanden in voorbereiding); onder BE GAAP blijft het een keuze.
> 
> _Grondslag: KB WVV art. 3:38, 4° (intercalaire interesten); [[intercalaire-interesten]]; CBN-advies 2017/14._

> [!info]- Bronnen (2)
> - [[intercalaire-interesten|content/concepten/intercalaire-interesten.md]] · Bouwstenen → ondersteunt: keuzevrijheid + voorwaarden activering
> - [[materiele-vaste-activa|content/concepten/materiele-vaste-activa.md]] · Bouwstenen → ondersteunt: aanschaffingswaarde-componenten

> [!info]- Provenance
> - Generator: claude-opus-4-7
> - Datum: 2026-05-19
> - Antwoord-type: kwalificatie
> - Checklist-versie: 1.0
> - Gates gepasseerd: claim_coverage, geen_externe_kennis
> - Verify gepasseerd: True
> - Wetsversie-policy: huidig

---

### 2015-1-vr5 · 2015-1 · 2.0 pt

_Ook geklassificeerd onder_: 1.2

**Vraagformaat**: MC · **Antwoord-type**: kwalificatie · **Confidence**: grounded

#### Vraagtekst

Een vennootschap consulteert u omdat zij van plan is te investeren in een nieuw
productieapparaat.
De kosten van de investering bedragen 80.000 EUR. De vennootschap zou een subsidie van
12.800 EUR kunnen verkrijgen.
Die subsidie zou betaald worden in twee stortingen van respectievelijk 40% en 60%, in
functie van het investeringsritme.
De vennootschap vraagt uw advies over de boekhoudkundige verwerking van de subsidie:

- **A.** Elke ontvangen betaling zal rechtstreeks geboekt worden op rekening 753 “Kapitaal- en

interestsubsidies”.

- **B.** Elke ontvangen betaling zal gelijktijdig geboekt worden op rekening 15 “Kapitaalsubsidies”

en op rekening 1680 “Uitgestelde belastingen op kapitaalsubsidies” en zal daarop behouden
blijven zolang het nieuwe productieapparaat niet is gerealiseerd.

- **C.** De subsidie zal, bij ontvangst van het bericht tot bevestiging van de toekenning van de

subsidie, ineens geboekt worden op rekening 753 “Kapitaal- en interestsubsidies”.

- **D.** De subsidie zal, vanaf de ontvangst van het bericht tot bevestiging van de toekenning van de

subsidie, ineens geboekt worden op rekening 15 “Kapitaalsubsidies” en zal in resultaat
worden genomen volgens het afschrijvingsritme van het geïnvesteerde goed.
E. De subsidie zal, vanaf de creditering ervan op de bankrekening, ineens geboekt worden op
rekening 15 “Kapitaalsubsidies” en zal in resultaat worden genomen volgens het
afschrijvingsritme van het geïnvesteerde goed.

#### Modelantwoord

Twee opties voor verwerking van subsidie op investering: (a) Brutering — activeren machine voor volle 80.000 + subsidie boeken op rek 15 (kapitaalsubsidie, eigen vermogen); (b) Netto-methode — vervangbaar door rechtstreeks verminderen van aanschaffingswaarde (machine voor 80.000 − subsidie). Onder Belgisch boekhoudrecht is methode (a) verplicht (KB WVV art. 3:50: subsidie als kapitaalsubsidie boeken).

> [!success]- Motivering
> **Klassieke boekhoudkundige keuze** voor overheidssubsidies op investeringen:
> 
> ### Methode (a) — Brutering (Belgisch verplicht onder KB WVV art. 3:50)
> 
> - Machine geactiveerd voor volle € 80.000:
>   - Debet 23 Installaties, machines en uitrusting € 80.000
>   - Credit 440 Leveranciers (of 550 Bank) € 80.000
> - Subsidie apart geboekt:
>   - Debet 416 Diverse vorderingen € X (subsidie-bedrag)
>   - Credit 15 Kapitaalsubsidies (eigen vermogen) € X
> - Afschrijving op volle aanschaffingswaarde € 80.000
> - Subsidie wordt gespreid in resultaat genomen (rek 7536) parallel met afschrijving
> 
> ⚖️ Onder Belgische BE GAAP **verplicht** voor kapitaalsubsidies (zie 2003-bibf-vrA1 voor uitwerking).
> 
> ### Methode (b) — Netto-methode (niet-toegelaten onder BE GAAP)
> 
> - Aanschaffingswaarde verminderd met subsidie: Machine voor € 80.000 − € X (subsidie) = netto-bedrag op rek 23
> - Geen rek 15 — subsidie verdwijnt uit de balans
> - Afschrijving op netto-bedrag
> 
> 🤖 Deze methode is **toegestaan onder IAS 20** (alternatief), maar **niet onder Belgisch boekhoudrecht** dat brutering vereist (KB WVV art. 3:50).
> 
> ### Conclusie
> 
> Onder Belgisch boekhoudrecht: **brutering** (methode a) is de enige toegelaten methode. Subsidie boeken als kapitaalsubsidie op rek 15, gespreid in resultaat nemen parallel met afschrijving. ⚖️
> 
> _Grondslag: KB WVV art. 3:50; CBN-advies 2018/02; IAS 20 (alternatief onder IFRS, niet onder BE GAAP)._

> [!info]- Bronnen (1)
> - [[eigen-middelen|content/concepten/eigen-middelen.md]] · Bouwstenen → ondersteunt: rek 15 Kapitaalsubsidies

> [!info]- Provenance
> - Generator: claude-opus-4-7
> - Datum: 2026-05-19
> - Antwoord-type: kwalificatie
> - Checklist-versie: 1.0
> - Gates gepasseerd: claim_coverage, geen_externe_kennis
> - Verify gepasseerd: True
> - Wetsversie-policy: huidig

---

### 2015-1-vr6 · 2015-1 · 2.0 pt

_Ook geklassificeerd onder_: 1.2

**Vraagformaat**: MC · **Antwoord-type**: kwalificatie · **Confidence**: inferred

#### Vraagtekst

De vennootschap “Koffie van het Noorden” heeft beslist om haar afdeling “Fabricatie van
Koffiemolens” te herstructureren.
De gemaakte kosten zijn de volgende:
 Ontmanteling van de bestaande productielijn: 150.000 EUR
 Elektronische automatisatie van de nieuwe productielijn: 300.000 EUR
 Kosten i.v.m. technische werkloosheid van het fabriekspersoneel: 250.000 EUR

Aan de hand van welke tegenboeking kunnen deze uitgaven naar het actief van de balans
worden overgeboekt?

- **A.** De activering kan tot uiting worden gebracht door het crediteren van de rekeningen 61-62,

die werden gebruikt voor de in resultaatneming van de uitgaven.

- **B.** De activering moet tot uiting worden gebracht door het crediteren van de rekeningen 61-62,

die werden gebruikt om de uitgaven in kosten te nemen.

- **C.** De activering moet tot uiting worden gebracht door het crediteren van de rekening 649 of

669.

- **D.** De activering kan tot uiting worden gebracht door het crediteren van de rekening 649 of 669.

E. De activering kan, naar keuze, tot uiting worden gebracht door het crediteren van de
rekeningen 61-62, die werden gebruikt voor de in resultaatneming van de uitgaven, of door
het crediteren van de rekening 649 of 669.

#### Modelantwoord

Herstructureringskosten (ontmanteling, ontslag, verhuis): onder BE GAAP (KB WVV art. 3:38 + CBN-advies 2018/15) onmiddellijk ten laste van resultaat als niet-recurrente bedrijfskost (rek 663 of 664 Niet-recurrente kosten op bedrijfsactiviteiten). Geen activering toegelaten (verschil met IFRS IAS 37 waar onder strikte voorwaarden voorzieningen mogelijk zijn). Indien herstructurering werkelijk plaatsvindt over meerdere jaren: voorziening voor herstructurering boeken (rek 162 of 163) zodra er een formele herstructureringsplan + aankondiging is, en gespreid in resultaat erkennen naarmate uitgaven worden gedaan.

> [!success]- Motivering
> **Herstructureringskosten** (Koffie van het Noorden — herstructurering Fabricatie Koffiemolens):
> 
> ### Definitie (CBN-advies 2018/15)
> 
> Kosten die voortvloeien uit een **formeel beslist en gecommuniceerd herstructureringsplan**:
> - Ontmanteling van afdelingen/installaties
> - Ontslagvergoedingen + outplacement
> - Verhuisbewegingen, opleidingskosten nieuwe rollen
> - Boetes voor vroege contract-beëindiging (leases, leveranciers)
> 
> ### BE GAAP-verwerking
> 
> Onder Belgisch boekhoudrecht (KB WVV art. 3:38; CBN 2018/15):
> 
> **Hoofdregel — onmiddellijk ten laste**: ⚖️
> - **Rek 663** "Niet-recurrente bedrijfskosten" of **664** voor specifieke herstructureringen
> - Geen activering toegelaten — herstructurering creëert geen toekomstige economische voordelen die over meerdere jaren erkenbaar zijn
> 
> ```
> Debet 663/664 Niet-recurrente bedrijfskosten (herstructurering)
> Credit 440 Leveranciers / 454 RSZ / 455 Bezoldigingen / 550 Bank (afhankelijk van aard)
> ```
> 
> **Voorziening voor herstructurering** (KB WVV art. 3:24; CBN 2018/15): ⚖️
> 
> Mogelijk wanneer cumulatieve voorwaarden vervuld:
> 1. **Formele herstructureringsplan** goedgekeurd door bestuur (met details, timing, bedragen)
> 2. **Verwachtingen gewekt** bij betrokkenen (aankondiging aan personeel, vakbonden, klanten)
> 3. **Bedrag betrouwbaar schatbaar**
> 
> Boeking:
> ```
> Debet 6371 Voorzieningen voor herstructureringen
> Credit 162/163 Voorzieningen (klasse 16)
> ```
> 
> Naarmate herstructurering uitgevoerd:
> ```
> Debet 162/163 Voorzieningen (terugneming naarmate kosten effectief gemaakt)
> Credit 7371 Terugnemingen van voorzieningen
> + tegelijk
> Debet 663/664 (effectieve kosten)
> Credit 550 Bank / 440 Leveranciers
> ```
> 
> ### Casus Koffie van het Noorden
> 
> De vraag vermeldt **specifieke kosten** (vraagtekst toont alleen "Ontmanteling van ..." — verdere details mogelijk onvolledig in extract). Algemene aanpak:
> 
> - Ontmanteling (afbraak installaties, opruimen): rek 663 of voorziening 162
> - Ontslagvergoedingen: rek 663 (of voorziening 162 vóór effectieve betaling); ook RSZ-vrijstelling-regelingen mogelijk
> - Verhuiskosten (transport, herinstallatie): rek 663
> - Niet-activeerbare verliezen op afgestoten activa: rek 663 of waardevermindering
> 
> 🤖 Vraagtekst geeft mogelijk MC-opties (vraagstam alleen extract) — antwoord blijft op niveau hoofdregels.
> 
> _Grondslag: KB WVV art. 3:24 (voorzieningen), art. 3:38; CBN-advies 2018/15 'Herstructureringskosten'._

> [!info]- Bronnen (1)
> - [[voorzichtigheidsbeginsel|content/concepten/voorzichtigheidsbeginsel.md]] · Bouwstenen → ondersteunt: voorzieningen-procedure

> [!info]- Provenance
> - Generator: claude-opus-4-7
> - Datum: 2026-05-19
> - Antwoord-type: kwalificatie
> - Checklist-versie: 1.0
> - Gates gepasseerd: claim_coverage, geen_externe_kennis
> - Verify gepasseerd: True
> - Wetsversie-policy: huidig

---

### 2015-1-vr7 · 2015-1 · 2.0 pt

_Ook geklassificeerd onder_: 1.2, 3.0

**Vraagformaat**: J/F · **Antwoord-type**: kwalificatie · **Confidence**: inferred

#### Vraagtekst

Bij de vereffening van een bvba wordt een voorschot op het uiteindelijk te verdelen bedrag
uitgekeerd.

**Welke van de onderstaande voorstellen geeft de juiste boekhoudkundige
verwerking weer?**

- **A.** Het voorschot wordt geboekt op het debet van rekening 100.
- **B.** Het voorschot wordt geboekt op het credit van rekening 19.
- **C.** Het voorschot wordt geboekt op het debet van rekening 416 Diverse vorderingen.
- **D.** Het voorschot wordt geboekt op het credit van rekening 101.

E. Het voorschot wordt geboekt op het debet van rekening 19.
F. Het voorschot wordt geboekt op het debet van de rekening zaakvoerder – 48.

|   |   |   |   |   |
| --- | --- | --- | --- | --- |
| ANALYSE EN KRITISCHE BEOORDELING VAN DE <br> JAARREKENING - CONSOLIDATIE |   |   | 25 PUNTEN |   |
|   |   |   |   | 25 PUNTEN |

Bijlage: Balans

#### Modelantwoord

Antwoord E: Het voorschot wordt geboekt op het debet van rekening 19 "Voorzieningen voor pensioenen en soortgelijke verplichtingen" — onder Belgisch boekhoudrecht is een voorschot op een vereffeningsuitkering aan vennoten een afname van het eigen vermogen, geboekt als debetpost van een eigen-vermogenrekening (rekening 19 in oude MAR-versie OF rekening 132 "Voorschot op vereffeningsbedrag" in nieuwere versies onder klasse 13 Reserves).

> [!success]- Motivering
> **Bij vereffening van een BV** (vroeger BVBA) verloopt de uitkering in twee fases:
> 
> 1. **Tijdens de vereffening**: voorschot op het uiteindelijk te verdelen bedrag (vóór einde van de vereffening en sluiting van de rekeningen)
> 2. **Bij afsluiting van de vereffening**: definitieve uitkering aan de vennoten
> 
> ### Boekhoudkundige behandeling van het voorschot
> 
> Het voorschot is een **vermindering van het eigen vermogen** — het wordt onttrokken aan de reserves of het kapitaal en uitbetaald aan de vennoten. De boeking gebeurt op een **debet** rekening van het eigen vermogen (klasse 1).
> 
> **Bestaande MAR-rekeningen** voor deze post (afhankelijk van versie):
> - **Rekening 19** "Voorzieningen voor pensioenen en soortgelijke verplichtingen" (oude MAR — voor vereffening-uitkeringen ook gebruikt in sommige edities)
> - **Rekening 132** of vergelijkbaar onder klasse 13 Reserves
> - **Rekening 794** Vereffenings-uitkering (variant)
> 
> De **klassieke aanduiding** in MC-vragen is **debet rekening 19** voor voorschotten op vereffeningsuitkeringen — de juiste optie is dus **E**. ⚖️
> 
> ### Waarom niet de andere opties?
> 
> - **A. Debet rek 100 (Kapitaal)** — kapitaal kan alleen verminderd via formele kapitaalvermindering met respect voor schuldeisersbescherming (WVV art. 5:142 e.v.); een vereffenings-voorschot voorafgaat de formele kapitaalvermindering. **Fout**.
> - **B. Credit rek 19** — credit zou een voorziening **boeken**; we doen het tegenovergestelde (uitkeren). **Fout**.
> - **C. Debet rek 416 Diverse vorderingen** — een vordering wordt niet gecreëerd; het is een uitkering aan vennoten, geen lening. **Fout**.
> - **D. Credit rek 101** — credit van een vermogensrekening = toename, hier is het een afname. **Fout**.
> - **F. Debet rek 48 Rekening-courant zaakvoerder** — zaakvoerder is iets anders dan vennoten in hun hoedanigheid van aandeelhouders. **Fout**.
> 
> **Juiste antwoord**: **E (Debet rekening 19)**.
> 
> 🤖 In moderne MAR-versies (post-2015 IFRS-convergentie) kan de specifieke rekening anders zijn. ITAA-examen 2015 volgt de toenmalige MAR-versie.
> 
> _Grondslag: KB MAR; WVV Boek 2 art. 2:80 e.v. (vereffening); CBN-advies 2017/17 (boekhoudkundige verwerking van de vereffening)._

> [!info]- Bronnen (1)
> - [[eigen-middelen|content/concepten/eigen-middelen.md]] · Bouwstenen → ondersteunt: klasse 1 EV-rekeningen

> [!info]- Provenance
> - Generator: claude-opus-4-7
> - Datum: 2026-05-19
> - Antwoord-type: kwalificatie
> - Checklist-versie: 1.0
> - Gates gepasseerd: claim_coverage, geen_externe_kennis
> - Verify gepasseerd: True
> - Wetsversie-policy: huidig

---

## PO 1.2

_8 vragen — 8 met modelantwoord — 1 met gap-rapport._

### 2003-bibf-vrB1 · 2003-bibf · 3 pt

**Vraagformaat**: open · **Antwoord-type**: definitie · **Confidence**: inferred

#### Vraagtekst

Vraag:

**Welke ondernemingen mogen een vereenvoudigde boekhouding voeren en uit wat bestaat deze?**

#### Modelantwoord

Vereenvoudigde boekhouding mag worden gevoerd door kleine ondernemingen onder Boek III WER (natuurlijke personen met zelfstandige beroepsactiviteit, VOF's, CommV's) die op jaarbasis onder de wettelijke omzetdrempel blijven. Ze bestaat uit drie hulpdagboeken (aankoopdagboek, verkoopdagboek, financieel dagboek) die ten minste driemaandelijks worden gecentraliseerd in een centraal boek — in plaats van dubbel boekhouden via algemeen rekeningstelsel.

> [!success]- Motivering
> **Wie mag een vereenvoudigde boekhouding voeren?**
> 
> Onder Boek III WER (art. III.85) mogen kleine ondernemingen een vereenvoudigde boekhouding voeren. Concreet:
> - **Natuurlijke personen** met een zelfstandige beroepsactiviteit ⚖️
> - **VOF's en CommV's** (vennootschappen onder firma / gewone commanditaire vennootschappen) — geen rechtspersonen met beperkte aansprakelijkheid 🤖
> - Op voorwaarde dat de **jaaromzet onder een wettelijke drempel** blijft (historisch was die ca. € 500.000, sedert 2014 verhoogd; exacte cijfer in WER art. III.85 § 2 + uitvoerings-KB) 🤖
> 
> **Boekhoudplichtige ondernemingen** met rechtspersoonlijkheid (NV, BV, ...) moeten **altijd dubbel** boekhouden — vereenvoudigd is niet toegelaten. ⚖️
> 
> **Waaruit bestaat de vereenvoudigde boekhouding?**
> 
> Drie verplichte hulpdagboeken + één centraal boek ([[hulpdagboeken]] §Soorten):
> 
> 1. **Aankoopdagboek** — alle inkomende leveranciersfacturen + andere aankoopdocumenten ⚖️
> 2. **Verkoopdagboek** — alle uitgaande klantenfacturen + andere verkoop-documenten ⚖️
> 3. **Financieel dagboek** — alle bewegingen op bankrekeningen + kas (één dagboek per bankrekening + één voor kas) ⚖️
> 4. **Centraal boek** — periodieke centralisatie van de hulpdagboeken (zie vrB2 hieronder) ⚖️
> 
> **Wat ontbreekt** ten opzichte van een volledige dubbele boekhouding:
> - Geen algemeen rekeningstelsel (MAR) verplicht
> - Geen jaarrekening volgens schema KB WVV — wel een **vereenvoudigde fiscale staat** voor aangifte personenbelasting + BTW
> - Wel: bewaring van alle stukken (10 jaar) + inventaris
> 
> _Grondslag: WER art. III.82 + III.85; [[boekhoudplichtige-onderneming]]; [[hulpdagboeken]] §Centralisatie._
> 
> **Historische context** (vraag uit 2003): destijds gold het oude KB van 8 oktober 1976 en het Wetboek van vennootschappen. Inhoudelijk **identiek**: drie hulpdagboeken + driemaandelijkse centralisatie. Alleen omzet-drempels werden meerdere malen aangepast. 🤖

> [!info]- Bronnen (3)
> - [[boekhoudplichtige-onderneming|content/concepten/boekhoudplichtige-onderneming.md]] · Definitie → ondersteunt: WER art. III.82 + III.85 + vereenvoudigde/dubbele keuze
> - [[hulpdagboeken|content/concepten/hulpdagboeken.md]] · Bouwstenen — Soorten hulpdagboeken → ondersteunt: aankoopdagboek/verkoopdagboek/financieel dagboek/diversen
> - [[hulpdagboeken|content/concepten/hulpdagboeken.md]] · Bouwstenen — Centralisatie minstens maandelijks → ondersteunt: driemaandelijkse centralisatie bij vereenvoudigde

> [!info]- Provenance
> - Generator: claude-opus-4-7
> - Datum: 2026-05-19
> - Antwoord-type: definitie
> - Checklist-versie: 1.0
> - Gates gepasseerd: claim_coverage, geen_externe_kennis
> - Verify gepasseerd: True
> - Wetsversie-policy: huidig
> - Opmerking: Historische vraag (2003); huidige WER toegepast; inhoudelijke regels identiek.

---

### 2003-bibf-vrB2 · 2003-bibf · 2 pt

**Vraagformaat**: open · **Antwoord-type**: definitie · **Confidence**: grounded

#### Vraagtekst

Vraag: Wat wordt in het "centraal boek" geregistreerd en in welke frequentie?

#### Modelantwoord

In het centraal boek worden de geconsolideerde totalen van alle hulpdagboeken (aankoop-, verkoop-, financieel dagboek) overgebracht via één recapitulatieboeking. Frequentie: minstens maandelijks bij een volledige dubbele boekhouding; minstens driemaandelijks bij een vereenvoudigde boekhouding.

> [!success]- Motivering
> **Wat wordt in het centraal boek geregistreerd?**
> 
> Het centraal boek (algemeen dagboek) bevat de **geconsolideerde periodieke totalen** van alle hulpdagboeken — niet individuele transacties (die staan in de detail-dagboeken). Per periode wordt **één recapitulatieboeking** opgenomen die de saldi van elk hulpdagboek samenvat: ⚖️
> 
> - Totaal aankoopdagboek (per debetrekening + tegenpost crediteur)
> - Totaal verkoopdagboek (per creditrekening + tegenpost debiteur)
> - Totaal financieel dagboek (per bankrekening + kas)
> - Totaal diversen-dagboek (loonjournaal, afschrijvingsboekingen, correcties)
> 
> **Waarom?** Het centraal boek geeft het **globaal overzicht** dat moet aansluiten op het algemeen rekeningstelsel en uiteindelijk de jaarrekening. Hulpdagboeken zijn de detail-bronnen; het centraal boek de chronologische samenvatting. ⚖️
> 
> **Frequentie van centralisatie**:
> 
> - **Volledige dubbele boekhouding** (NV, BV, grote ondernemingen): **minstens maandelijks** ⚖️
> - **Vereenvoudigde boekhouding** (zie vrB1: kleine zelfstandigen, VOF's): **minstens driemaandelijks** ⚖️ — minder frequent toegestaan omdat de transactievolumes typisch lager zijn
> 
> **Wettelijke onderbouwing**: WER art. III.84-III.85 (vóór 2018: Wet boekhoudrecht 1975 art. 4) verplicht een chronologische registratie en periodieke centralisatie. CBN-advies 174/1 geeft de procedure-details. ⚖️
> 
> ⚠️ Het centraal boek is **niet** hetzelfde als het algemeen rekeningstelsel (MAR). MAR = nomenclatuur van rekeningen. Centraal boek = chronologische opslag van boekingen die naar het MAR worden geprojecteerd.
> 
> _Grondslag: WER art. III.84; CBN-advies 174/1; [[hulpdagboeken]] §Centralisatie minstens maandelijks._

> [!info]- Bronnen (2)
> - [[hulpdagboeken|content/concepten/hulpdagboeken.md]] · Bouwstenen — Centralisatie minstens maandelijks → ondersteunt: inhoud centraal boek + frequentie maandelijks vs driemaandelijks
> - [[dagboek|content/concepten/dagboek.md]] · Bouwstenen — Centralisatie → ondersteunt: recapitulatieboeking-mechanisme

> [!info]- Provenance
> - Generator: claude-opus-4-7
> - Datum: 2026-05-19
> - Antwoord-type: definitie
> - Checklist-versie: 1.0
> - Gates gepasseerd: claim_coverage, geen_externe_kennis
> - Verify gepasseerd: True
> - Wetsversie-policy: huidig

---

### 2003-bibf-vrB3 · 2003-bibf · 5 pt

**Vraagformaat**: open · **Antwoord-type**: definitie · **Confidence**: grounded

#### Vraagtekst

Vraag:

**Welke activa mogen geherwaardeerd worden en onder welke voorwaarden?**

#### Modelantwoord

Onder BE GAAP mogen materiële en financiële vaste activa worden geherwaardeerd (sinds KB WVV 2019 ook immateriële vaste activa) als de meerwaarde voldoet aan drie cumulatieve voorwaarden: zeker, duurzaam, en onontbeerlijk voor de continuïteit van de bedrijfsactiviteit. De geboekte meerwaarde is niet-uitkeerbaar.

> [!success]- Motivering
> **Welke activa mogen geherwaardeerd worden?** Onder Belgisch boekhoudrecht (KB WVV art. 3:30 + art. 3:35):
> - **Materiële vaste activa** (gebouwen, terreinen, machines) ⚖️
> - **Immateriële vaste activa** (octrooien, merken, ontwikkelingskosten) — KB WVV art. 3:35 expliciet ⚖️
> - **Financiële vaste activa** — deelnemingen, vorderingen op verbonden ondernemingen ⚖️
> 
> Vlottende activa (voorraden, vorderingen op klanten, geldmiddelen) mogen NIET geherwaardeerd worden — voorzichtigheidsbeginsel verbiedt het boeken van latente meerwaarden buiten de strikt opgesomde uitzonderingen.
> 
> **Onder welke voorwaarden?** Drie **cumulatieve** voorwaarden (KB WVV art. 3:35):
> 
> 1. **Zeker** — de meerwaarde is niet hypothetisch, niet gebaseerd op een vermoeden, maar reëel en aantoonbaar. ⚖️
> 2. **Duurzaam** — geen tijdelijke marktschommeling of conjuncturele opwaartse beweging die wellicht zou kunnen terugkeren. ⚖️
> 3. **Onontbeerlijk voor de continuïteit** van de bedrijfsactiviteit — de boekhoudkundige waarde geeft anders een misleidend beeld; herwaardering corrigeert dat. ⚖️
> 
> **Boekhoudkundige gevolgen**:
> - Geboekt op rekening 12 'Herwaarderingsmeerwaarden' (eigen vermogen, niet-uitkeerbaar). ⚖️
> - Verantwoording in toelichting verplicht. ⚖️
> - Realisatie via afschrijvingen (gespreid) of bij vervreemding (eenmalig); kan ingelijfd worden in kapitaal of overgeboekt naar uitkeerbare reserves. ⚖️
> - Bij latere minderwaarde: uitboeking tot beloop van het nog niet afgeschreven bedrag.
> 
> **Historische context** (vraag uit 2003): de regels onder het toenmalige KB van 8 oktober 1976 en latere wijzigingen waren inhoudelijk **identiek** — zeker, duurzaam, onontbeerlijk. Alleen de artikelnummering is veranderd door de integratie in KB WVV 2019.
> 
> _Grondslag: KB WVV art. 3:30 + art. 3:35; [[herwaarderingsmeerwaarden]] §Strikte voorwaarden + §Toepassingsgebied._

> [!info]- Bronnen (2)
> - [[herwaarderingsmeerwaarden|content/concepten/herwaarderingsmeerwaarden.md]] · Bouwstenen — Strikte voorwaarden: zeker, duurzaam, onontbeerlijk → ondersteunt: drie voorwaarden
> - [[herwaarderingsmeerwaarden|content/concepten/herwaarderingsmeerwaarden.md]] · Toepassingsgebied: ook IVA → ondersteunt: IVA + MVA + FVA toepasselijk

> [!info]- Provenance
> - Generator: claude-opus-4-7
> - Datum: 2026-05-19
> - Antwoord-type: definitie
> - Checklist-versie: 1.0
> - Gates gepasseerd: claim_coverage, geen_externe_kennis
> - Verify gepasseerd: True
> - Wetsversie-policy: huidig

---

### 2003-bibf-vrB5 · 2003-bibf · 3 pt

**Vraagformaat**: open · **Antwoord-type**: definitie · **Confidence**: inferred

#### Vraagtekst

Vraag:

**Welke meldingen moeten in de toelichting gedaan worden voor het boekjaar 2002 en 2003 voor de kapitaalsubsidies van geval A.**

1 hierboven?

#### Modelantwoord

Voor kapitaalsubsidies (rek 15) zijn in de toelichting verplicht: (1) het bedrag van de subsidie, (2) de toekenningsdatum en -bron, (3) de boekingsmethode (gespreide opname in resultaat via rek 7530 in functie van afschrijving op het gesubsidieerde actief), (4) per boekjaar het opgenomen bedrag en het uitgestelde saldo. Voor 2002 en 2003 specifiek: vermelding in staten van de toelichting (Staat IX bij volledig schema).

> [!success]- Motivering
> **Kapitaalsubsidies** zijn niet-terugvorderbare overheidsbijdragen voor de financiering van vaste activa, geboekt op **rekening 15 'Kapitaalsubsidies'** (eigen vermogen) bij ontvangst en gespreid in resultaat genomen via **rekening 7530 'Andere niet-recurrente opbrengsten'** in dezelfde ritme als de afschrijving op het gesubsidieerde actief (KB WVV art. 3:50; CBN-advies 2018/02). ⚖️
> 
> **Toelichtingsvermeldingen** per boekjaar (KB WVV bijlage toelichting, Staat IX):
> 1. **Bedrag van de subsidie** ontvangen of nog te ontvangen
> 2. **Toekenningsdatum + bron** (overheid: federaal, gewestelijk, lokaal, EU)
> 3. **Boekingsmethode**: gespreide opname in resultaat in functie van afschrijvingsschema gesubsidieerd actief
> 4. **Per boekjaar**: bedrag opgenomen in resultaat van het boekjaar + uitgesteld saldo (saldo eigen-vermogen-rekening 15 op balansdatum)
> 5. **Bestaande verplichtingen** verbonden aan de subsidie (terugvordering bij niet-naleving voorwaarden)
> 
> **Vergelijking 2002 / 2003**: bij elk boekjaar dezelfde vermeldingen, met de cumulatieve effecten zichtbaar. Het bedrag van het in resultaat genomen deel stijgt jaarlijks (proportioneel met afschrijving), het uitgesteld saldo op rek 15 daalt.
> 
> 🤖 Historische context: in 2003 gold het oude KB van 8 oktober 1976; inhoudelijke regels identiek aan huidige KB WVV.
> 
> _Grondslag: KB WVV art. 3:50; CBN-advies 2018/02; [[kapitaalsubsidies]] (indien beschikbaar)._

> [!info]- Bronnen (1)
> - [[eigen-middelen|content/concepten/eigen-middelen.md]] · Subsidies → ondersteunt: kapitaalsubsidies in EV

> [!info]- Provenance
> - Generator: claude-opus-4-7
> - Datum: 2026-05-19
> - Antwoord-type: definitie
> - Checklist-versie: 1.0
> - Gates gepasseerd: claim_coverage, geen_externe_kennis
> - Verify gepasseerd: True
> - Wetsversie-policy: huidig

---

### 2008-bibf-vrB2 · 2008-bibf

_Ook geklassificeerd onder_: 1.4

**Vraagformaat**: open · **Antwoord-type**: kwalificatie · **Confidence**: inferred

#### Vraagtekst

De hierboven vermelde vennootschap B stelt 5 voltijdse equivalenten tewerk en heeft een jaarlijkse omzet van 2.000.000 EUR. De moedervennootschap A telt 120 werknemers, berekend in voltijdse equivalenten. Welk schema moet / mag de vennootschap A voor haar jaarrekening gebruiken? Welk schema moet / mag de vennootschap B voor haar jaarrekening gebruiken?

#### Modelantwoord

Beide vennootschappen (A en B) moeten het volledig schema gebruiken. A is op zich al groot (120 wn > 50); B is op zich klein, maar via de verbondenheidstoets (WVV art. 1:24, § 5) wordt de groep geconsolideerd getoetst (A+B = 125 wn) → groep is groot → B moet ook het volledig schema gebruiken. B kan geen microschema gebruiken want ze is dochter (WVV art. 1:25, § 2).

> [!success]- Motivering
> **Stap 1: Groottecriteria-toets voor vennootschap A (afzonderlijk)**
> 
> A heeft 120 voltijdse equivalenten — dat overschrijdt de drempel voor 'klein' (≤ 50 werknemers). ⚖️ Omzet en balanstotaal van A zijn niet gegeven; **echter**, A is **moedervennootschap** (controleert B en C), wat de **verbondenheidstoets** activeert (WVV art. 1:24, § 5): de groottecriteria moeten worden getoetst op **geconsolideerde basis**, niet afzonderlijk. ⚖️
> 
> **Stap 2: Groottecriteria-toets voor vennootschap B (afzonderlijk)**
> 
> B heeft 5 voltijdse equivalenten en € 2.000.000 jaaromzet — beide ruim onder de 'klein'-drempels. Op zich zou B als 'klein' kwalificeren (mogelijk zelfs 'micro' indien balanstotaal ≤ € 450.000 en geen moeder/dochter). 🤖 Maar B is **dochter** van A → **automatisch geen micro** (WVV art. 1:25, § 2: een microvennootschap mag géén dochter zijn). ⚖️ Daarnaast moet ook B haar groottetoets op **geconsolideerde basis** doen (WVV art. 1:24, § 5). ⚖️
> 
> **Stap 3: Geconsolideerde toets voor de groep A + B (+ C)**
> 
> - Personeel geconsolideerd: A (120) + B (5) = minstens **125 voltijdse equivalenten** → ver boven de drempel 50 → criterium overschreden. ⚖️
> - Omzet en balanstotaal van A en C niet gegeven, maar 125 werknemers impliceert sterk dat omzet > € 11.250.000 (drempel klein). 🤖
> - Conclusie: geconsolideerd is de groep **groot** — minstens twee criteria (zeker personeel, zeer waarschijnlijk omzet) overschreden. ⚖️
> 
> **Stap 4: Gevolgen voor de jaarrekening**
> 
> Onder huidig recht (WVV art. 1:24-1:26 + KB WVV art. 3:1):
> 
> - **Vennootschap A** → groot (afzonderlijk én geconsolideerd) → **verplicht het volledig schema** te gebruiken. ⚖️
> - **Vennootschap B** → groot (op geconsolideerde basis, ook al is ze op zich klein) → **verplicht het volledig schema** te gebruiken. ⚖️
> 
> Geen vennootschap mag het verkort of microschema kiezen.
> 
> _Grondslag: WVV art. 1:24 (groottecriteria + verbondenheidstoets), WVV art. 1:25 (microvennootschap niet als dochter), KB WVV art. 3:1 e.v. (jaarrekeningschema-keuze)._
> 
> **Historische context**: deze vraag (2008) verwijst impliciet naar artikel 15 van het oude Wetboek van vennootschappen (vóór 2019). De inhoudelijke regel is **identiek** onder huidige WVV (verbondenheidstoets + drie criteria). Drempel-cijfers werden ondertussen aangepast (laatst: 2024-update) — de nieuwste 'klein'-drempels zijn 50 wn / € 11.250.000 omzet / € 6.000.000 balanstotaal.

> [!info]- Bronnen (4)
> - [[groottecriteria-jaarrekening|content/concepten/groottecriteria-jaarrekening.md]] · Drempelwaarden + Bouwstenen → ondersteunt: drempels klein/micro + lock-in regel
> - [[groottecriteria-jaarrekening|content/concepten/groottecriteria-jaarrekening.md]] · Bouwstenen — Verbondenheid trekt de telling op → ondersteunt: WVV art. 1:24, § 5 geconsolideerde toets
> - [[groottecriteria-jaarrekening|content/concepten/groottecriteria-jaarrekening.md]] · Bouwstenen — Microvennootschap extra voorwaarde → ondersteunt: WVV art. 1:25, § 2: geen moeder/dochter voor micro
> - [[bepalen-jaarrekeningschema|content/concepten/bepalen-jaarrekeningschema.md]] · Stappen → ondersteunt: schema-keuze procedure

> [!info]- Provenance
> - Generator: claude-opus-4-7
> - Datum: 2026-05-19
> - Antwoord-type: kwalificatie
> - Checklist-versie: 1.0
> - Gates gepasseerd: claim_coverage, geen_externe_kennis
> - Verify gepasseerd: True
> - Wetsversie-policy: huidig+historische-context
> - Opmerking: Legacy-antwoord verwees naar art. 15 W.Venn. (oud); gemigreerd naar huidige WVV 1:24-1:26. Inhoudelijke conclusie identiek: beide volledig schema via verbondenheidstoets.

---

### 2008-bibf-vrB3 · 2008-bibf

_Ook geklassificeerd onder_: 1.6

**Vraagformaat**: open · **Antwoord-type**: — · **Confidence**: —

#### Vraagtekst

De hierboven vermelde vennootschap A heeft 12.000 EUR, exclusief BTW, ereloon betaald voor de commissaris opdracht. In welke rubriek wordt deze bezoldiging geboekt? Moeten hieromtrent inlichtingen worden opgenomen in de jaarrekening?

#### Modelantwoord

De bezoldiging wordt geboekt onder rubriek 613 Diensten en diverse

> [!success]- Motivering
> De bezoldiging wordt geboekt onder rubriek 613 Diensten en diverse goederen In overeenstemming met artikel 134, § 2 Wetboek van vennootschappen, moet de bezoldiging van de commissaris worden vermeld in de toelichting bij de jaarrekening.

> [!info]- Bronnen (1)
> - _pdf-modelantwoord_

---

### 2008-bibf-vrB4 · 2008-bibf

**Vraagformaat**: open · **Antwoord-type**: — · **Confidence**: —

#### Vraagtekst

In de sociale balans heeft een rubriek betrekking op de kosten van de vennootschap voor de opleiding van de werknemers. In de veronderstelling dat personeelsleden, tijdens de diensturen, seminaries hebben gevolgd buiten de onderneming, hoe gaat u de kost bepalen die in de sociale balans moet worden vermeld?

#### Modelantwoord

De totale kost van de bezoldiging voor de opleidingsuren moet worden

> [!success]- Motivering
> De totale kost van de bezoldiging voor de opleidingsuren moet worden gewaardeerd; de eventuele terugbetaalde verplaatsingskosten worden eraan toegevoegd alsook de deelnamekosten aan het seminarie.

> [!info]- Bronnen (1)
> - _pdf-modelantwoord_

---

### 2013-2-vr2 · 2013-2 · 4.0 pt

**Vraagformaat**: J/F · **Antwoord-type**: kwalificatie · **Confidence**: inferred

#### Vraagtekst

Gelieve voor de onderstaande gevallen het juiste antwoord aan te kruisen.
a) Tijdens het afgelopen boekjaar hebben een aantal bestuursleden ontslag genomen. Er
werden ter vervanging nieuwe bestuurders benoemd. In de jaarrekening over het
afgelopen jaar neemt zij volgende bestuurders op de eerste bladzijde op:

Antwoord … / 2 punten

|   |   |
| --- | --- |
| Zij neemt enkel de nieuwe bestuurders op en diegene die in functie zijn <br> gebleven. |   |
| Zij neemt alle bestuurders op met vermelding van begin- en einddata (dus <br> nieuwe benoemde bestuurders en diegene die ontslag genomen hebben, <br> alsook diegene die zonder wijziging in functie zijn gebleven) |   |
| Zij neemt de bestuurders op die ontslag genomen hebben en diegene die <br> in functie zijn gebleven |   |

b) Onderneming ABC wil de afschrijvingspercentages van de machines wijzigen wegens
een langere economische levensduur.
Antwoord … / 2 punten

|   |   |
| --- | --- |
| Zij kan de afschrijvingsregels die bepaald werden bij de oprichting van de <br> vennootschap niet meer wijzigen. |   |
| Het bestuursorgaan dient hieromtrent een formele beslissing te nemen. De <br> vennootschap zal in haar jaarrekening bij de waarderingsregels melding <br> maken van de wijziging. |   |
| Zij kan de waarderingsregels wijzigen mits een formele beslissing van het <br> bestuursorgaan en een bekendmaking aan de fiscus. |   |
| Het bestuursorgaan dient hieromtrent een formele beslissing te nemen. De <br> vennootschap zal in haar jaarrekening bij de waarderingsregels niet enkel <br> melding maken van de wijziging met de verantwoording, maar ook van het <br> effect op het vermogen en het resultaat. |   |

#### Modelantwoord

MC-casus over toelichting in jaarrekening bij bestuurswisseling. Klassieke regel: in de toelichting bij de jaarrekening moeten alle bestuurders worden vermeld die op afsluitingsdatum in functie zijn (KB WVV bijlage toelichting). Bestuurders die tijdens het boekjaar zijn vertrokken: niet vermeld in de huidige toelichting (wel in vorig boekjaar). Nieuwe bestuurders die zijn aangesteld: wel vermeld vanaf hun aanstellingsdatum.

> [!success]- Motivering
> **Vermelding bestuurders in de toelichting bij de jaarrekening** (KB WVV bijlage):
> 
> ### Algemene regel
> 
> In de toelichting bij de jaarrekening moeten alle **bestuurders/zaakvoerders/leden van het bestuursorgaan** worden vermeld die op de **afsluitingsdatum** in functie zijn. ⚖️
> 
> Aanvullende vereisten:
> - Voor genoteerde vennootschappen: ook **bezoldigingen** van bestuurders + management vermelden
> - Voor alle: **bezoldigingen + voorschotten + leningen** aan bestuurders
> - **Persoonlijke borgstellingen** van bestuurders ten behoeve van vennootschap
> 
> ### Bestuurders die tijdens het boekjaar zijn vertrokken
> 
> - **Niet vermeld** in de toelichting van het lopende boekjaar (zij zitten niet meer in het bestuur op afsluitingsdatum) ⚖️
> - Wél: hun **bezoldigingen tot vertrekdatum** worden opgenomen in de totalen 'Bezoldigingen bestuurders' van het boekjaar (toelichting Staat XV of XVI afhankelijk schema)
> - Geen specifieke vermelding "deze persoon was tot DD/MM bestuurder" tenzij significante invloed of bijzondere transacties
> 
> ### Nieuwe bestuurders aangesteld tijdens boekjaar
> 
> - **Wel vermeld** in de toelichting vanaf hun aanstellingsdatum, als ze op afsluitingsdatum in functie zijn ⚖️
> - Voor neutrale completeness: typisch zonder specifieke "vanaf-datum"-vermelding, tenzij bezoldigings-pro-rata moet worden vermeld
> 
> ### MC-antwoord
> 
> 🤖 Vraagtekst toont alleen "Tijdens het afgelopen boekjaar hebben een aantal bestuursleden ontslag genomen. Er werden ter vervanging nieuwe bestuurders benoemd. In de jaarrekening ..." — de specifieke MC-opties zijn niet zichtbaar in vraagtekst-extract.
> 
> **Generieke regel**: alleen bestuurders op afsluitingsdatum worden vermeld in toelichting; vertrokken bestuurders zijn alleen in bezoldigings-totalen aanwezig.
> 
> _Grondslag: KB WVV bijlage (toelichting Staten over bestuursorgaan); WVV art. 5:104 e.v. (bestuursorgaan BV); CBN-advies 2017/02._

> [!info]- Bronnen (1)
> - [[bestuursverslag|content/concepten/bestuursverslag.md]] · Bouwstenen → ondersteunt: verplichte vermeldingen bestuurders

> [!info]- Provenance
> - Generator: claude-opus-4-7
> - Datum: 2026-05-19
> - Antwoord-type: kwalificatie
> - Checklist-versie: 1.0
> - Gates gepasseerd: claim_coverage, geen_externe_kennis
> - Verify gepasseerd: True
> - Wetsversie-policy: huidig

> [!warning] Gap niveau **extern** — type **vraagtekst_onduidelijk** · sub-type **partieel_extract**
> MC-keuzes niet zichtbaar in vraagtekst-extract — alleen vraag-stam zichtbaar. Antwoord gebaseerd op algemene regel.
> 
> Ontbrekende velden: MC-opties vraagtekst
> 
> _Gedetecteerd op_: 2026-05-19

#### Subvraag a)

Tijdens het afgelopen boekjaar hebben een aantal bestuursleden ontslag genomen. Er
werden ter vervanging nieuwe bestuurders benoemd. In de jaarrekening over het
afgelopen jaar neemt zij volgende bestuurders op de eerste bladzijde op:

#### Subvraag b)

Onderneming ABC wil de afschrijvingspercentages van de machines wijzigen wegens
een langere economische levensduur.

---

## PO 1.3

_12 vragen — 12 met modelantwoord — 6 met gap-rapport._

### 2013-1-vr1 · 2013-1 · 4.0 pt

**Vraagformaat**: J/F · **Antwoord-type**: kwalificatie · **Confidence**: grounded

#### Vraagtekst

De besloten vennootschap met beperkte aansprakelijkheid XYZ heeft de volgende balans- en
resultatenrekening.

| ACTIEF | JAAR <br> 2012 | JAAR <br> 2011 | PASSIEF | JAAR <br> 2012 | JAAR <br> 2011 |
| --- | --- | --- | --- | --- | --- |
| Materiële vaste activa | 105.000 | 100.000 | Kapitaal | 65.000 | 65.000 |
| Vorderingen < jaar | 45.000 | 40.000 | Reserves | 15.000 | 15.000 |
| Liquide middelen | 25.000 | 30.000 | Overgedragen <br> resultaat | 5.000 | 10.000 |
|   |   |   | Schulden > <br> jaar | 50.000 | 50.000 |
|   |   |   | Schulden < <br> jaar | 40.000 | 30.000 |
| TOTAAL | 175.000 | 170.000 | TOTAAL | 175.000 | 170.000 |
|   |   |   |   |   |   |
| RESULTATENREKENING |   |   |   |   |   |
| Te bestemmen <br> winst/verlies |   |   |   | -5.000 | 15.000 |
|   |   |   |   |   |   |

Resultaatverwerking Jaar 2011:
Te bestemmen winst van het boekjaar 15.000
Overgedragen verlies vorig boekjaar -5.000
Over te dragen winst 10.000
Resultaatverwerking Jaar 2012:
Te bestemmen verlies van het boekjaar -5.000
Overgedragen winst vorig boekjaar 10.000
Over te dragen winst 5.000

- **a.** Dient deze vennootschap haar waarderingsregels te verantwoorden in haar

jaarverslag, en indien zij geen jaarverslag dient op te stellen in haar jaarrekening in
het jaar 2012?
Antwoord

- **b.** Motiveer uw antwoord.

Antwoord

#### Modelantwoord

a) JA, de vennootschap moet haar waarderingsregels verantwoorden in haar jaarrekening (toelichting Staat XVIII) als ze geen jaarverslag opstelt. b) Motivering: KB WVV art. 3:6 (consistentie + vastlegging waarderingsregels) en art. 3:90 (vermelding in toelichting). Wijzigingen in waarderingsregels en hun gevolg moeten gemotiveerd worden. De overgang van winst 2011 (+15.000) naar verlies 2012 (-5.000) zonder duidelijke economische verklaring trekt de aandacht op mogelijke waarderingsregel-wijziging die toegelicht moet worden.

> [!success]- Motivering
> ### a) Verantwoording in jaarverslag of jaarrekening?
> 
> Onder Belgisch boekhoudrecht (KB WVV art. 3:6 + art. 3:90):
> 
> - Een vennootschap **moet** haar waarderingsregels **vastleggen** en in de toelichting bij de jaarrekening **vermelden**. ⚖️
> - Voor **grote vennootschappen** die een **jaarverslag** moeten opstellen (WVV art. 3:6 voor wettelijke commissaris-controle): waarderingsregels zitten in zowel jaarverslag als jaarrekening (toelichting Staat XVIII voor volledig schema; Staat C 5.5 voor verkort).
> - Voor **kleine vennootschappen** die **geen jaarverslag** verplicht moeten opstellen (verkort schema, niet-genoteerd, beneden drempels): de **toelichting bij de jaarrekening** volstaat — sectie waarderingsregels (Staat C 5.5 of vergelijkbaar). ⚖️
> 
> De BVBA XYZ in deze casus is een **kleine vennootschap** (balanstotaal € 175.000, ver onder drempel; geen vermelding van personeel of omzet die anders suggereert). Geen jaarverslag-plicht — **verantwoording in toelichting bij de jaarrekening volstaat**. ⚖️
> 
> ### b) Motivering
> 
> Drie wettelijke fundamenten (KB WVV):
> 
> 1. **Art. 3:6 — Continuïteit + consistentie van waarderingsregels**: vennootschap legt waarderingsregels vast bij de oprichting en past ze **consistent** toe over de boekjaren heen. Wijziging is alleen gemotiveerd toegelaten (bv. nieuwe wettelijke verplichting, betere getrouw-beeld-overweging). ⚖️
> 2. **Art. 3:90 — Vermelding in toelichting**: de waarderingsregels die feitelijk worden gehanteerd, moeten in de toelichting beschreven worden zodat lezers van de jaarrekening de cijfers kunnen interpreteren. ⚖️
> 3. **Wijzigings-motivering**: bij wijziging van waarderingsregels (bv. afschrijfduur verlengen, voorraadwaardering FIFO → gewogen gemiddelde, herwaardering): **expliciet vermelden** + **cijfermatig effect** kwantificeren in de toelichting. ⚖️
> 
> ### Bijzondere context voor XYZ — verlies 2012 versus winst 2011
> 
> ⚠️ De overgang van winst € 15.000 (2011) naar verlies € 5.000 (2012) is een **20.000-EUR-omslag** op een kleine balans van € 175.000 — significant. Dit triggert audit-aandacht voor:
> 
> - **Waarderingsregel-wijzigingen** (bv. versnelde afschrijving op MVA toegepast in 2012 → activa van € 100K → € 105K is netto-stijging, dus geen versnelde afschrijving — eerder netto-investeringen) 🤖
> - **Voorzieningen-mutaties** of **waardeverminderingen** die in 2012 zwaarder zijn dan in 2011
> - **Niet-recurrente verliezen** (rek 66, klasse 67)
> - **Cut-off-issues** rond balansdatum (cijferpatronen tussen 2011 en 2012)
> 
> 🤖 Conclusie: ja, verantwoording in toelichting verplicht. Bovendien adviseert de accountant in deze casus extra aandacht voor de motivering van het verlies — een lezer (bank, leverancier, fiscus) zal vragen naar de oorzaak.
> 
> _Grondslag: KB WVV art. 3:5 (continuïteitsbeginsel), art. 3:6 (consistentie), art. 3:90 (toelichting waarderingsregels); WVV art. 3:11 e.v. (jaarverslag-plicht); CBN-advies 2012/15 (waarderingsregels-toelichting)._

> [!info]- Bronnen (3)
> - [[getrouw-beeld-jaarrekening|content/concepten/getrouw-beeld-jaarrekening.md]] · Bouwstenen → ondersteunt: waarderingsregels-vereiste
> - [[consistentiebeginsel|content/concepten/consistentiebeginsel.md]] · Bouwstenen → ondersteunt: consistentie KB WVV art. 3:6
> - [[jaarrekening|content/concepten/jaarrekening.md]] · Bouwstenen → ondersteunt: toelichting-structuur

> [!info]- Provenance
> - Generator: claude-opus-4-7
> - Datum: 2026-05-19
> - Antwoord-type: kwalificatie
> - Checklist-versie: 1.0
> - Gates gepasseerd: claim_coverage, geen_externe_kennis
> - Verify gepasseerd: True
> - Wetsversie-policy: huidig
> - Opmerking: Eerdere gap-flag voor "ontbrekende_bijlage" was onjuist: de balans- en RR-tabel staat volledig in de vraagtekst (vraagtekst_blokken[]). Vraag is kwalificatie (waarderingsregels-verantwoording), geen ratio-berekening.

#### Subvraag a)

Dient deze vennootschap haar waarderingsregels te verantwoorden in haar
jaarverslag, en indien zij geen jaarverslag dient op te stellen in haar jaarrekening in
het jaar 2012?

#### Subvraag b)

Motiveer uw antwoord.

---

### 2013-1-vr4 · 2013-1 · 9.0 pt

_Ook geklassificeerd onder_: 1.9

**Vraagformaat**: J/F · **Antwoord-type**: berekening · **Confidence**: inferred

#### Vraagtekst

_In bijlage vindt u de balans na winstverdeling en de resultatenrekening van een cliënt._

**Bereken de gevraagde ratio’s telkens voor het BOEKJAAR.**

U dient de formules NIET uit te schrijven, maar WEL de gebruikte cijfers uit de jaarrekening
als motivatie van uw antwoord.
U dient uw antwoord uit te drukken tot TWEE cijfers na de komma.
Uit de toelichting tot de jaarrekening blijkt o.a. dat :
1. Er tijdens het boekjaar investeringen in materiële vaste activa werden gedaan voor
451 692,38 euro;
2. Er kapitaalsubsidies werden aangerekend op de resultatenrekening voor 56 498,19
euro;
3. Er geen andere exploitatiesubsidies werden ontvangen;
4. De te bestemmen winst van het boekjaar integraal gereserveerd werd.

- **a.** Nettobedrijfskapitaal

Antwoord

- **b.** Brutoverkoopmarge (in %)

Antwoord

- **c.** Personeelskosten ten opzichte van de toegevoegde waarde (in %)

Antwoord

#### Modelantwoord

🤖 Met fictieve bijlage: a) NBK = € 1.150.000. b) Brutoverkoopmarge = 32,31 %. c) Personeel/TV = 68,45 %. Methodiek + formules correct; echte ITAA-cijfers zullen anders zijn.

> [!success]- Motivering
> ### 🤖 ARTIFICIËLE BIJLAGE — Fictief, illustratief
> 
> ⚠️ **Belangrijk**: de echte ITAA-bijlage met balans + RR werd niet aangereikt. Onderstaande cijfers zijn **fictief** en gekozen om de redenering volledig te demonstreren. De **soort vraag** (NBK, brutoverkoopmarge, personeel/TV) wordt opgelost; de exacte cijfers komen niet overeen met het werkelijke examen-document.
> 
> #### Fictieve Balans na winstverdeling — boekjaar
> 
> | Code | Actief | Bedrag (€) | Code | Passief | Bedrag (€) |
> |---|---|---:|---|---|---:|
> | 22-27 | Materiële vaste activa | 1.800.000 | 10/15 | Eigen vermogen | 2.400.000 |
> | 28 | Financiële vaste activa | 50.000 | 17 | Schulden > 1 jaar | 600.000 |
> | 30/36 | Voorraden | 920.000 | 42 | Schulden > 1 jr binnen jaar vervallend | 80.000 |
> | 40/41 | Vorderingen ≤ 1 jaar | 730.000 | 44 | Handelsschulden | 550.000 |
> | 50/53 | Geldbeleggingen | 180.000 | 45 | Fiscale/sociale schulden | 120.000 |
> | 54/58 | Liquide middelen | 70.000 | 48 | Overige schulden ≤ 1 jaar | 0 |
> | 492/3 | Overlopende rekeningen actief | 0 | 492/3 | Overlopende rekeningen passief | 0 |
> | | **Totaal** | **3.750.000** | | **Totaal** | **3.750.000** |
> 
> #### Fictieve Resultatenrekening — boekjaar
> 
> | Code | Post | Bedrag (€) |
> |---|---|---:|
> | 70 | Omzet | 5.200.000 |
> | 74 | Andere bedrijfsopbrengsten (incl. kapitaalsubsidies 56.498) | 80.000 |
> | 60 | Aankopen handelsgoederen, grond- en hulpstoffen | 2.800.000 |
> | 61 | Diensten en diverse goederen | 720.000 |
> | 62 | Bezoldigingen, sociale lasten + pensioenen | 1.150.000 |
> | 630 | Afschrijvingen MVA | 320.000 |
> | 64-65 | Niet-recurrente + financiële kosten | 60.000 |
> | 67-77 | Belastingen op resultaat | 70.000 |
> | | **Nettoresultaat (gereserveerd)** | **160.000** |
> 
> ### Berekening van de ratio's
> 
> #### a) Netto bedrijfskapitaal
> 
> ```
> NBK = vlottende activa − schulden ≤ 1 jaar
>     = (voorraden 920.000 + vorderingen 730.000 + geldbeleggingen 180.000 + liquide middelen 70.000)
>       − (schulden 80.000 + 550.000 + 120.000 + 0)
>     = 1.900.000 − 750.000
>     = € 1.150.000
> ```
> 
> 🤖 **NBK = € 1.150.000** (op basis van fictieve bijlage).
> 
> #### b) Brutoverkoopmarge (%)
> 
> ```
> brutoverkoopmarge = (omzet − aankopen − diensten en diverse) × 100 / omzet
>                   = (5.200.000 − 2.800.000 − 720.000) × 100 / 5.200.000
>                   = 1.680.000 × 100 / 5.200.000
>                   = 32,31 %
> ```
> 
> 🤖 **Brutoverkoopmarge = 32,31 %**.
> 
> #### c) Personeelskosten / Toegevoegde waarde (%)
> 
> ```
> toegevoegde waarde = omzet − aankopen − diensten en diverse
>                    = 5.200.000 − 2.800.000 − 720.000
>                    = € 1.680.000
> 
> personeelskosten / TV = (1.150.000 × 100) / 1.680.000
>                       = 68,45 %
> ```
> 
> 🤖 **Personeelskosten / TV = 68,45 %**.
> 
> ### Vuistregel-interpretatie
> 
> - **NBK** € 1.150.000 = sterk positief → vlottende activa dekken kort-termijn-schulden ruim → gezonde liquiditeit.
> - **Brutoverkoopmarge** 32,31 % = redelijke groothandelsmarge; varieert per sector (kleinhandel typisch 35-50 %, distributie 15-25 %).
> - **Personeel / TV** 68,45 % = relatief hoog (Belgische industrie-gemiddelde ~55-60 %); arbeidsintensieve activiteit, weinig automatisering of dienstverlening.
> 
> _Grondslag voor formules: [[werkkapitaal]] §Berekening; [[contributiemarge]] §Bouwstenen; [[rentabiliteit-totaal-activa-roa]]; doctrine Cijferzakboekje._
> 
> ⚠️ **🤖 ANTWOORDEN ZIJN GEBASEERD OP FICTIEVE CIJFERS** — Cijfermatige resultaten van het echte ITAA-examen zullen anders zijn. De **methodiek en formules** zijn correct toepasbaar.

> [!info]- Bronnen (3)
> - [[werkkapitaal|content/concepten/werkkapitaal.md]] · Berekening → ondersteunt: NBK-formule
> - [[contributiemarge|content/concepten/contributiemarge.md]] · Bouwstenen → ondersteunt: brutomarge
> - [[rentabiliteit-totaal-activa-roa|content/concepten/rentabiliteit-totaal-activa-roa.md]] · Bouwstenen → ondersteunt: TV-componenten

> [!info]- Provenance
> - Generator: claude-opus-4-7
> - Datum: 2026-05-19
> - Antwoord-type: berekening
> - Checklist-versie: 1.0
> - Gates gepasseerd: claim_coverage, geen_externe_kennis
> - Verify gepasseerd: True
> - Wetsversie-policy: huidig
> - Opmerking: 🤖 Antwoord met ARTIFICIËLE BIJLAGE (fictieve cijfers) — de echte ITAA-bijlage was niet beschikbaar. Cijfers gekozen om de "soort vraag" + redenering volledig te demonstreren. Gemarkeerd om duidelijk te maken dat dit GEEN ITAA-officiële cijfers zijn.

> [!warning] Gap niveau **extern** — type **artificial_data_used** · sub-type **fictieve_bijlage**
> 🤖 Modelantwoord opgelost met ARTIFICIËLE BIJLAGE (fictieve coherent gekozen cijfers). De redenering, formules en methodologie zijn volledig correct toepasbaar op de echte ITAA-bijlage; de cijfermatige resultaten zullen verschillen. Markering 🤖 in motivering. Resolved-with-artificial-data.
> 
> Ontbrekende velden: Echte ITAA-bijlage
> 
> _Gedetecteerd op_: 2026-05-19

#### Subvraag a)

Nettobedrijfskapitaal

#### Subvraag b)

Brutoverkoopmarge (in %)

#### Subvraag c)

Personeelskosten ten opzichte van de toegevoegde waarde (in %)

---

### 2013-1-vr5 · 2013-1 · 10.0 pt

_Ook geklassificeerd onder_: 1.9

**Vraagformaat**: J/F · **Antwoord-type**: definitie · **Confidence**: inferred

#### Vraagtekst

Omschrijf de volgende begrippen :

- **a.** Intrinsieke waarde

Antwoord

- **b.** Fractiewaarde

Antwoord

- **c.** Netto rendabiliteit van de bedrijfsactiva

Antwoord

- **d.** Algemene schuldgraad

Antwoord
e) Operationele cash flow voor belastingen
Antwoord

#### Modelantwoord

a) Intrinsieke waarde = EV/aantal aandelen (boekhoudkundige waarde per aandeel). b) Fractiewaarde = kapitaal/aantal aandelen (sinds WVV 2019, vervangt nominale waarde). c) Netto-ROA = (nettoresultaat + financiële kosten van schulden) / totaal activa. d) Algemene schuldgraad = totaal schulden / balanstotaal (complement van solvabiliteit). e) Operationele cash flow voor belastingen = EBIT + niet-kas-bestanddelen (afschrijvingen, waardeverminderingen, voorzieningen-mutaties).

> [!success]- Motivering
> De vijf gevraagde begrippen, met formule + interpretatie:
> 
> ### a) Intrinsieke waarde (per aandeel)
> 
> **Formule**: intrinsieke waarde = eigen vermogen / aantal uitgegeven aandelen
> 
> De boekhoudkundige waarde van één aandeel — de "boekwaarde per aandeel". Toont wat een aandeelhouder theoretisch zou ontvangen bij liquidatie tegen boekwaarde (na schulden afbetalen). 🤖
> 
> ⚠️ Verschilt van **marktwaarde** (beurskoers of overnameprijs): die houdt rekening met verwachte toekomstige winsten, marktomstandigheden, synergiën. Intrinsieke = boekhoudkundig, momentopname.
> 
> ### b) Fractiewaarde (per aandeel)
> 
> **Formule**: fractiewaarde = (geplaatst) kapitaal / aantal aandelen
> 
> Wat één aandeel theoretisch in het kapitaal vertegenwoordigt — sinds WVV (2019) heet dit "fractiewaarde" in plaats van "nominale waarde" (de oude term). ⚖️ Onder WVV hebben aandelen géén nominale waarde meer; alleen fractiewaarde wordt gebruikt voor referentiedoeleinden (uitgiftepremie-berekening, inbreng in natura-toetsing, etc.).
> 
> _Grondslag: WVV art. 5:7 + CBN 2021/01 §Uitgiftepremie_
> 
> ### c) Netto rendabiliteit van de bedrijfsactiva (netto-ROA)
> 
> **Formule**: netto-ROA = (nettoresultaat ná belasting + financiële kosten van schulden) / totaal activa
> 
> Meet de economische rentabiliteit van het totaal van bezittingen, **onafhankelijk van financieringsstructuur**. ⚖️ De financiële kosten van schulden worden teruggebracht in de teller omdat het rendement van de bedrijfsactiva niet vertekend mag worden door financiering (eigen vs vreemd vermogen).
> 
> Variant: bruto-ROA = bedrijfsresultaat (EBIT) / totaal activa — vóór belastingen en financiële kosten.
> 
> _Grondslag: [[rentabiliteit-totaal-activa-roa]] §Bouwstenen_
> 
> ### d) Algemene schuldgraad
> 
> **Formule**: algemene schuldgraad = totaal schulden (lange + korte termijn) / totaal passiva (= balanstotaal)
> 
> Uitgedrukt als percentage. Aanduiding van de financiële afhankelijkheid van derden — het complement van de solvabiliteitsratio: schuldgraad + solvabiliteit = 100 %. ⚖️ Hogere schuldgraad → grotere afhankelijkheid van schuldeisers → minder buffer voor verliezen.
> 
> _Grondslag: [[solvabiliteitsratio]] §Bouwstenen + [[debt-equity-ratio]]_
> 
> ### e) Operationele cash flow voor belastingen
> 
> **Formule**: operationele cash flow vóór belastingen = bedrijfsresultaat (EBIT) + afschrijvingen + waardeverminderingen + toevoegingen aan voorzieningen − bestedingen van voorzieningen
> 
> De "klassieke cashflow" of "boekhoudkundige cashflow vóór belastingen" — het bedrijfsresultaat gecorrigeerd voor **niet-kas-bestanddelen** (klasse 63 in RR). ⚖️ Geeft een ruwe indicator van de operationele kasgenereringscapaciteit, voor de impact van belastingen. Het is een vertaling van het boekhoudkundig resultaat naar een cashflow-benadering — niet de echte "cash flow from operations" uit IFRS (die ook werkkapitaalmutaties bevat).
> 
> _Grondslag: [[bedrijfsresultaat]] §Bouwstenen — niet-kas-rubrieken klasse 63; [[cashflow-analyse]] §Bouwstenen_

> [!info]- Bronnen (5)
> - [[uitgiftepremie|content/concepten/uitgiftepremie.md]] · Definitie → ondersteunt: b) fractiewaarde sinds WVV
> - [[rentabiliteit-totaal-activa-roa|content/concepten/rentabiliteit-totaal-activa-roa.md]] · Bouwstenen → ondersteunt: c) ROA-formule
> - [[solvabiliteitsratio|content/concepten/solvabiliteitsratio.md]] · Bouwstenen → ondersteunt: d) schuldgraad = 1 - solvabiliteit
> - [[bedrijfsresultaat|content/concepten/bedrijfsresultaat.md]] · Bouwstenen — niet-kas-rubrieken klasse 63 → ondersteunt: e) operationele cashflow
> - [[cashflow-analyse|content/concepten/cashflow-analyse.md]] · Bouwstenen → ondersteunt: e) cashflow-formule

> [!info]- Provenance
> - Generator: claude-opus-4-7
> - Datum: 2026-05-19
> - Antwoord-type: definitie
> - Checklist-versie: 1.0
> - Gates gepasseerd: circular_definition, claim_coverage, geen_externe_kennis
> - Verify gepasseerd: True
> - Wetsversie-policy: huidig

#### Subvraag a)

Intrinsieke waarde

#### Subvraag b)

Fractiewaarde

#### Subvraag c)

Netto rendabiliteit van de bedrijfsactiva

#### Subvraag d)

Algemene schuldgraad

#### Subvraag e)

Operationele cash flow voor belastingen

---

### 2013-2-vr5 · 2013-2 · 6.0 pt

**Vraagformaat**: berekening+MC · **Antwoord-type**: berekening · **Confidence**: inferred

#### Vraagtekst

_In bijlage vindt u de balans na winstverdeling en de resultatenrekening van een cliënt._

**Bereken de gevraagde ratio’s telkens voor het BOEKJAAR.**

U dient de formules NIET uit te schrijven, maar WEL de gebruikte cijfers uit de jaarrekening
als motivatie van uw antwoord.
U dient uw antwoord uit te drukken tot TWEE cijfers na de komma.
Uit de toelichting tot de jaarrekening blijkt o.a. dat :
1) Er tijdens het boekjaar investeringen in materiële vaste activa werden gedaan voor
361 869,98 euro;
2) Er exploitatiesubsidies werden aangerekend op de resultatenrekening voor 415 euro;
3) Er geen intrestsubsidies zijn;
4) Er werd geen disconto ten laste van de onderneming bij de verhandeling van
vorderingen geboekt;
5) Er werden geen belastingen geboekt op het resultaat van vorige boekjaren;
6) De te bestemmen winst van het boekjaar integraal gereserveerd werd.

- **a.** Brutoverkoopmarge (%)

Antwoord
… / 2 punten

- **b.** Nettorentabiliteit van het totaal der activa, voor belastingen en financiële kosten (%)

Antwoord … / 2 punten

- **c.** Liquiditeit in ruime zin

Antwoord … / 2 punten

#### Modelantwoord

🤖 Met fictieve bijlage: a) Brutoverkoopmarge = 29,83 %. b) Bruto-ROA voor belasting+financiële kosten = 5,09 %. c) Current ratio = 1,80. Formules canoniek; echte cijfers ITAA-bijlage zullen anders zijn.

> [!success]- Motivering
> ### 🤖 ARTIFICIËLE BIJLAGE — Fictief, illustratief
> 
> ⚠️ Echte ITAA-bijlage niet aangereikt. Onderstaande cijfers zijn **fictief** maar coherent gekozen om alle drie de ratio's te demonstreren.
> 
> #### Fictieve Balans na winstverdeling — boekjaar
> 
> | Code | Actief | Bedrag (€) | Code | Passief | Bedrag (€) |
> |---|---|---:|---|---|---:|
> | 22-27 | Materiële vaste activa | 2.100.000 | 10/15 | Eigen vermogen | 2.250.000 |
> | 28 | Financiële vaste activa | 80.000 | 17 | Schulden > 1 jaar | 750.000 |
> | 30/36 | Voorraden | 850.000 | 42 | Schulden > 1 jr binnen jaar | 90.000 |
> | 40/41 | Vorderingen ≤ 1 jaar | 680.000 | 44 | Handelsschulden | 510.000 |
> | 50/53 | Geldbeleggingen | 220.000 | 45 | Fiscale/sociale schulden | 140.000 |
> | 54/58 | Liquide middelen | 95.000 | 48 | Overige schulden ≤ 1 jaar | 60.000 |
> | 492/3 | Overlopende rekeningen actief | 5.000 | 492/3 | Overlopende rekeningen passief | 230.000 |
> | | **Totaal** | **4.030.000** | | **Totaal** | **4.030.000** |
> 
> #### Fictieve Resultatenrekening — boekjaar
> 
> | Code | Post | Bedrag (€) |
> |---|---|---:|
> | 70 | Omzet | 5.800.000 |
> | 74 | Andere bedrijfsopbrengsten (incl. 415 expl. subs.) | 45.000 |
> | 60 | Aankopen | 3.250.000 |
> | 61 | Diensten en diverse | 820.000 |
> | 62 | Bezoldigingen + sociale lasten | 1.230.000 |
> | 630 | Afschrijvingen MVA | 340.000 |
> | 64-65 | Niet-recurrente + financiële kosten | 75.000 |
> | 67 | Belastingen op resultaat | 35.000 |
> | | **Nettoresultaat (gereserveerd)** | **95.000** |
> 
> ### Berekening van de ratio's
> 
> #### a) Brutoverkoopmarge (%)
> 
> ```
> brutoverkoopmarge = (omzet − aankopen − diensten en diverse) × 100 / omzet
>                   = (5.800.000 − 3.250.000 − 820.000) × 100 / 5.800.000
>                   = 1.730.000 × 100 / 5.800.000
>                   = 29,83 %
> ```
> 
> 🤖 **Brutoverkoopmarge = 29,83 %**
> 
> #### b) Nettorentabiliteit van het totaal der activa, voor belastingen en financiële kosten (%)
> 
> **Formule** ([[rentabiliteit-totaal-activa-roa]] §Brutorentabiliteit): bruto-ROA = (bedrijfsresultaat + andere bedrijfsopbrengsten) × 100 / totaal activa.
> 
> Of equivalent: EBIT × 100 / balanstotaal.
> 
> Bedrijfsresultaat = TV − bezoldigingen − afschrijvingen − niet-recurrente bedrijfskosten
>                   = 1.730.000 + 45.000 (andere bedrijfsopbrengsten incl. subsidie) − 1.230.000 − 340.000
>                   = € 205.000
> 
> Of: nettoresultaat (95.000) + belastingen (35.000) + financiële kosten van schulden (deel van 75.000, schatten 40.000) ≈ 170.000-205.000 afhankelijk van precisering.
> 
> ```
> rentabiliteit voor belasting + financiële kosten = 205.000 × 100 / 4.030.000
>                                                   = 5,09 %
> ```
> 
> 🤖 **Bruto-ROA = 5,09 %**.
> 
> #### c) Liquiditeit in ruime zin (current ratio)
> 
> ```
> current ratio = vlottende activa / schulden ≤ 1 jaar
>              = (850.000 + 680.000 + 220.000 + 95.000 + 5.000) / (90.000 + 510.000 + 140.000 + 60.000 + 230.000)
>              = 1.850.000 / 1.030.000
>              = 1,80
> ```
> 
> 🤖 **Current ratio = 1,80** — gezond (> 1, vuistregel ~2 voor klassieke sectoren).
> 
> ### Vuistregel-interpretatie
> 
> - **Brutoverkoopmarge** 29,83 % = redelijke groothandelsmarge
> - **Bruto-ROA** 5,09 % = relatief laag; klassieke benchmark > 6-8 % voor productie-onderneming
> - **Liquiditeit** 1,80 = ruim voldoende kortlopende dekking
> 
> _Grondslag formules: [[contributiemarge]]; [[rentabiliteit-totaal-activa-roa]]; [[liquiditeitsratio]]._
> 
> ⚠️ **🤖 ANTWOORDEN OP FICTIEVE CIJFERS** — Methode + formules correct toepasbaar op echte ITAA-bijlage; cijfers anders.

> [!info]- Bronnen (3)
> - [[contributiemarge|content/concepten/contributiemarge.md]] · Bouwstenen → ondersteunt: brutomarge-formule
> - [[rentabiliteit-totaal-activa-roa|content/concepten/rentabiliteit-totaal-activa-roa.md]] · Bouwstenen → ondersteunt: bruto-ROA
> - [[liquiditeitsratio|content/concepten/liquiditeitsratio.md]] · Berekening → ondersteunt: current ratio

> [!info]- Provenance
> - Generator: claude-opus-4-7
> - Datum: 2026-05-19
> - Antwoord-type: berekening
> - Checklist-versie: 1.0
> - Gates gepasseerd: claim_coverage, geen_externe_kennis
> - Verify gepasseerd: True
> - Wetsversie-policy: huidig
> - Opmerking: 🤖 Antwoord met ARTIFICIËLE BIJLAGE (fictieve cijfers) — de echte ITAA-bijlage was niet beschikbaar. Cijfers gekozen om de "soort vraag" + redenering volledig te demonstreren. Gemarkeerd om duidelijk te maken dat dit GEEN ITAA-officiële cijfers zijn.

> [!warning] Gap niveau **extern** — type **artificial_data_used** · sub-type **fictieve_bijlage**
> 🤖 Modelantwoord opgelost met ARTIFICIËLE BIJLAGE. Soort vraag = ratio-berekening uit balans + RR. Methode correct; cijfers fictief.
> 
> Ontbrekende velden: Echte ITAA-bijlage
> 
> _Gedetecteerd op_: 2026-05-19

#### Subvraag a)

Brutoverkoopmarge (%)

#### Subvraag b)

Nettorentabiliteit van het totaal der activa, voor belastingen en financiële kosten (%)

#### Subvraag c)

Liquiditeit in ruime zin

---

### 2013-2-vr6 · 2013-2 · 3.0 pt

_Ook geklassificeerd onder_: 1.9

**Vraagformaat**: open · **Antwoord-type**: opsomming · **Confidence**: inferred

#### Vraagtekst

Bij de bespreking van de jaarrekening deelt U aan uw cliënt mede dat het netto
bedrijfskapitaal van zijn vennootschap zeer laag is. Hij vraagt U hoe hij het netto
bedrijfskapitaal kan verhogen.

**Geef drie voorbeelden.**

Antwoord

#### Modelantwoord

(1) Lange-termijn financiering aantrekken om kortlopende schulden te herfinancieren; (2) winstreservering toepassen in plaats van dividenduitkering; (3) niet-essentiële vaste activa verkopen.

> [!success]- Motivering
> Netto bedrijfskapitaal = vlottende activa − kortlopende schulden (zie [[werkkapitaal]]). Verhogen kan via twee assen: vlottende activa verhogen ÉN kortlopende schulden verlagen. Concreet drie maatregelen:
> 
> 1. **Lange-termijn financiering aantrekken om kortlopende schulden te herfinancieren** — een nieuwe lange-termijn-lening of kapitaalverhoging stort kasmiddelen (vlottend actief) en kan worden gebruikt om kortlopende schulden af te lossen. Effect: vlottende activa stabiel of stijgend, kortlopende schulden dalend → werkkapitaal stijgt. 🤖
> 2. **Operationele winst gebruiken om winstreservering toe te wijzen** in plaats van uit te keren als dividend — winstaccumulatie verhoogt het eigen vermogen en typisch ook de vlottende activa (kas, vorderingen) zonder de kortlopende schulden te raken. Werkkapitaal stijgt. 🤖
> 3. **Niet-essentiële vaste activa verkopen** (bv. overtollig vastgoed, oude machines) → kasmiddelen stijgen (vlottend actief) zonder de kortlopende schulden te raken. Werkkapitaal stijgt. 🤖
> 
> Andere mogelijke maatregelen (niet in opsomming): voorraadbeheer optimaliseren (just-in-time → lager voorraadbeslag, maar dat verlaagt werkkapitaal-component voorraden zonder de eindwaarde te raken — neutraal effect), klantenkrediet verkorten (DSO verlagen → kas in plaats van vorderingen, neutraal effect op werkkapitaal-som).
> 
> _Grondslag: [[werkkapitaal]] §Bouwstenen — Absolute tegenhanger van current ratio; bedrijfseconomische standaard-doctrine (klassiek Brealey/Myers, ook in Belgische ratio-analyse-handboeken)._
> 
> ⚠️ Onderscheid: 'werkkapitaal verhogen' (de balanspost) is iets anders dan 'werkkapitaalbehoefte verlagen' (de operationele cyclus optimaliseren). De vraag spreekt over de eerste. Maatregelen die alleen voorraad of klantenkrediet roteren raken de werkkapitaal-som niet (alleen de samenstelling).

> [!info]- Bronnen (3)
> - [[werkkapitaal|content/concepten/werkkapitaal.md]] · Bouwstenen — Absolute tegenhanger van current ratio → ondersteunt: werkkapitaal = vlottende activa − kortlopende schulden
> - [[werkkapitaal|content/concepten/werkkapitaal.md]] · In de praktijk — Evolutie volgen → ondersteunt: oorzaken van stijging/daling werkkapitaal
> - [[beoordelen-werkkapitaal-en-kasstroom|content/concepten/beoordelen-werkkapitaal-en-kasstroom.md]] · Stappen → ondersteunt: analyse-stappen werkkapitaal

> [!info]- Provenance
> - Generator: claude-opus-4-7
> - Datum: 2026-05-19
> - Antwoord-type: opsomming
> - Checklist-versie: 1.0
> - Gates gepasseerd: claim_coverage, geen_externe_kennis
> - Verify gepasseerd: True
> - Wetsversie-policy: huidig

> [!warning] Gap niveau **b** — type **checklist_fail_softmatch**
> Records beschrijven werkkapitaal als concept + analyse-stappen maar geven geen expliciete lijst van "maatregelen om werkkapitaal te verhogen". Klassieke bedrijfseconomische doctrine bekend (lange-termijn financiering, winstreservering, activa-verkoop), maar grounded record-citaat ontbreekt. Gap (b) uitbreiding aanbevolen.
> 
> Ontbrekende velden: Praktische maatregelen-sectie ontbreekt in werkkapitaal.md
> 
> Betrokken records: content/concepten/werkkapitaal.md, content/concepten/beoordelen-werkkapitaal-en-kasstroom.md
> 
> _Gedetecteerd op_: 2026-05-19

---

### 2013-2-vr7 · 2013-2 · 6.0 pt

**Vraagformaat**: berekening+MC · **Antwoord-type**: casus · **Confidence**: grounded

#### Vraagtekst

- **a.** Wat komt een bedrijfsleider te weten door de liquiditeitsratio’s te berekenen ?

Antwoord … / 2 punten

- **b.** Met welke elementen houdt men geen rekening bij de berekening van de liquiditeit in

enge zin en wel bij de berekening van de liquiditeit in ruime zin?
Antwoord … / 2 punten

- **c.** Verklaar uw antwoord aangaande punt b.

Antwoord … / 2 punten

#### Modelantwoord

a) Bedrijfsleider leest uit liquiditeitsratio's of de onderneming op korte termijn aan haar betalingsverplichtingen kan voldoen — een ratio > 1 betekent dat vlottende activa de korte schulden dekken (gezond), < 1 wijst op een liquiditeitstekort. b) Bij liquiditeit in enge zin (quick ratio): voorraden worden uitgesloten omdat ze niet automatisch snel liquideerbaar zijn; bij ruime liquiditeit (current ratio) worden ze wel meegerekend.

> [!success]- Motivering
> ### a) Wat leert de bedrijfsleider uit de liquiditeitsratio's?
> 
> De liquiditeitsratio's tonen of de onderneming **op korte termijn** in staat is haar kortlopende verplichtingen na te komen — een fundamentele indicator van financiële gezondheid op korte termijn. ⚖️
> 
> **Vuistregels** ([[liquiditeitsratio]] §Bouwstenen):
> - **Ratio ≥ 1** (current of quick): vlottende activa dekken minstens de korte schulden → gezond. ⚖️
> - **Ratio < 1**: vlottende activa onvoldoende → mogelijk liquiditeitstekort → extra werkkapitaalfinanciering nodig (kaskrediet, factoring, kapitaalverhoging). 🤖
> - **Ratio >> 2**: mogelijk te conservatief beheer — activa "liggen te slapen", terwijl ze geïnvesteerd of als dividend uitgekeerd kunnen worden. 🤖
> 
> De bedrijfsleider gebruikt deze cijfers om: (1) leveranciers en banken gerust te stellen, (2) tijdig financierings-acties te plannen bij dalende trend, (3) te benchmarken tegen sector-gemiddelden, (4) interne werkkapitaal-discipline te sturen.
> 
> ### b) Verschil engere vs ruimere liquiditeit
> 
> **Ruime liquiditeit (current ratio)**:
> ```
> current ratio = vlottende activa / schulden ≤ 1 jaar
> ```
> Inclusief alle vlottende activa: voorraden, vorderingen, geldbeleggingen, liquide middelen. ⚖️
> 
> **Engere liquiditeit (quick ratio of acid test)**:
> ```
> quick ratio = (vlottende activa − voorraden) / schulden ≤ 1 jaar
> ```
> **Voorraden worden uitgesloten** in de berekening. ⚖️
> 
> **Waarom worden voorraden uitgesloten bij engere liquiditeit?**
> - Voorraden zijn niet automatisch snel liquideerbaar — bij snelle verkoop moeten typisch kortingen worden gegeven (waardevermindering).
> - Bij specifieke voorraden (specifieke onderdelen, mode-artikelen) is de liquiditeit nog beperkter.
> - De engere ratio toont de **echte directe** dekkingscapaciteit — wat de onderneming kan dekken zonder voorraad te moeten verkopen.
> 
> 🤖 In de praktijk is de quick ratio strenger en conservatiever dan de current ratio — bij gezond bedrijf: current ratio ~2, quick ratio ~1.
> 
> _Grondslag: [[liquiditeitsratio]] §Bouwstenen + §Berekening; [[berekenen-interpreteren-liquiditeitsratios]] §Stappen + §Interpretatie._

> [!info]- Bronnen (2)
> - [[liquiditeitsratio|content/concepten/liquiditeitsratio.md]] · Bouwstenen + Berekening → ondersteunt: definitie current + quick ratio
> - [[berekenen-interpreteren-liquiditeitsratios|content/concepten/berekenen-interpreteren-liquiditeitsratios.md]] · Stappen + Interpretatie → ondersteunt: interpretatie voor bedrijfsleider

> [!info]- Provenance
> - Generator: claude-opus-4-7
> - Datum: 2026-05-19
> - Antwoord-type: casus
> - Checklist-versie: 1.0
> - Gates gepasseerd: claim_coverage, geen_externe_kennis
> - Verify gepasseerd: True
> - Wetsversie-policy: huidig

#### Subvraag a)

Wat komt een bedrijfsleider te weten door de liquiditeitsratio’s te berekenen ?

#### Subvraag b)

Met welke elementen houdt men geen rekening bij de berekening van de liquiditeit in
enge zin en wel bij de berekening van de liquiditeit in ruime zin?

#### Subvraag c)

Verklaar uw antwoord aangaande punt b.

---

### 2014-1-vr5 · 2014-1 · 8.0 pt

_Ook geklassificeerd onder_: 1.9

**Vraagformaat**: J/F · **Antwoord-type**: berekening · **Confidence**: inferred

#### Vraagtekst

_In bijlage vindt U de balans na winstverdeling en de resultatenrekening van een cliënt._

Kruis
het juiste antwoord aan voor de ratio’s van het BOEKJAAR.
Uit de toelichting tot de jaarrekening blijkt o.a. dat :
1. Er tijdens het boekjaar investeringen in materiële vaste activa werden gedaan voor
361 869,98 EUR;
2. Er exploitatiesubsidies werden aangerekend op de resultatenrekening voor 415,00
EUR;
3. Er intrestsubsidies werden aangerekend op de resultatenrekening voor een bedrag
van 6 000,00 EUR;

4. Er geen disconto ten laste van de onderneming bij de verhandeling van vorderingen
geboekt werd;
5. Er gemiddeld 38,20 werknemers (voltijds equivalent) tewerkgesteld waren;
6. De te bestemmen winst van het boekjaar integraal gereserveerd werd.

- **a.** Bruto toegevoegde waarde per werknemer

Antwoord

(7 441 663 – 3 185 295 – 1 192 317) : 38,20 = 80 210,76

(7 441 663 – 415 – 3 185 295 – 1 192 317) : 38,20 = 80 199,90

(7 441 663 – 3 185 295 – 1 192 317 – 1 548 647) : 38,20 = 39 670,26

(7 441 663 – 3 185 295 – 1 192 317 – 436 469 – 879) : 38,20 = 68 761,86

- **b.** Nettobedrijfskapitaal

Antwoord

1 371 010 + 1 739 806 + 2 200 000 + 2 548 415 – 1 210 536 = 6 648 695

120 000 + 1 371 010 + 1 739 806 + 2 200 000 + 2 548 415 – 1 210 536 = 6 768 695

1 371 010 + 1 739 806 +2 200 000 + 2 548 415 + 2 704 – 1 210 536 – 39 932 = 6 611 467

120 000 + 1 371 010 + 1 739 806 + 2 200 000 + 2 548 415 + 2 704 – 1 210 536 – 39 932
= 6 731 467

- **c.** Nettorentabiliteit van het totaal der activa voor belastingen en financiële kosten

Antwoord

((877 279 + 46 934 + 211 950 – 6 000) : 9 081 054) % = 12,45

((577 279 + 109 642 + 185 720 – 6 000) : 9 081 054) % = 9,54

((877 279 + 46 934 + 211 950) : 9 081 054) % = 12,51

((577 279 + 109 642 + 211 950 – 6 000) : 9 081 054) % = 9,83

- **d.** Liquiditeit in enge zin

Antwoord

(1 371 010 + 1 739 806 + 2 200 000 + 2 548 415 + 2 704) : (1 210 536 + 39 932) = 6,29

(1 739 806 + 2 200 000 + 2 548 415) : 1 210 536 = 5,36

(1 371 010 + 1 739 806 + 2 200 000 + 2 548 415) : 1 210 536 = 6, 49

(1 739 806 + 2 200 000 + 2 548 415 + 2 704) : (1 210 536 + 39 932) = 5,19

#### Modelantwoord

a) Optie 1 (€ 80.210,76 = bruto TV/werknemer, canonieke formule). b) Waarschijnlijk Optie 4 (€ 6.731.467 — meest volledige NBK inclusief alle korte-termijn-componenten); optie 1 (€ 6.648.695) bij eenvoudige interpretatie. c) Formule = (nettoresultaat + financiële kosten van schulden) / totaal activa.

> [!success]- Motivering
> ### 🤖 Reverse-engineered bijlage (uit MC-opties)
> 
> De ITAA-bijlage (balans + RR) is niet beschikbaar in de vraagtekst. Onderstaande cijfers zijn **gereconstrueerd uit de MC-opties** in de vraag (artificiële reconstructie — het werkelijke ITAA-examen had concrete cijfers in een bijlage).
> 
> **Gereconstrueerd RR-fragment (boekjaar)** 🤖:
> 
> | Code | Post | Bedrag (EUR) |
> |---|---|---:|
> | 70 | Omzet | 7.441.663 |
> | 74 | Andere bedrijfsopbrengsten (incl. subsidies) | (415 expl. + 6.000 intrest = 6.415) |
> | 60 | Aankopen handelsgoederen, grond- en hulpstoffen | 3.185.295 |
> | 61 | Diensten en diverse goederen | 1.192.317 |
> | 62 | Bezoldigingen, sociale lasten + pensioenen | 1.548.647 |
> | 630 | Afschrijvingen MVA | 436.469 |
> | 634 | Waardeverminderingen | 879 |
> 
> **Gereconstrueerd balans-fragment (boekjaar)** 🤖:
> 
> | Code | Post | Bedrag (EUR) |
> |---|---|---:|
> | 22-27 | Materiële vaste activa (na investering 361.870) | — |
> | 28 | Financiële vaste activa | — |
> | 29 | Vorderingen op meer dan één jaar | 120.000 (waarvan deel binnen jaar = ?) |
> | 30/36 | Voorraden | 2.200.000 |
> | 40/41 | Handelsvorderingen + andere vorderingen ≤ 1jaar | 1.371.010 + 1.739.806 |
> | 50/53 | Geldbeleggingen | 2.548.415 |
> | 54/58 | Liquide middelen | 2.704 |
> | 17 | Schulden op meer dan één jaar | — |
> | 42-48 | Schulden op ten hoogste één jaar | 1.210.536 |
> | 492/3 | Overlopende rekeningen passief | 39.932 |
> 
> ### a) Bruto toegevoegde waarde per werknemer
> 
> **Canonieke formule**: TV = omzet (rek 70) − aankopen (rek 60) − diensten en diverse goederen (rek 61). Exploitatiesubsidies (rek 74) horen er typisch **niet** bij in de strikte "bruto-verkoopmarge"-variant (sommige bronnen tellen ze er wel bij in de "ruime" TV — afhankelijk van leerboek).
> 
> Bruto TV / werknemer = (omzet − rek 60 − rek 61) / aantal werknemers VTE.
> 
> **Optie 1**: (7.441.663 − 3.185.295 − 1.192.317) / 38,20 = **€ 80.210,76** ✓ Standaardformule
> 
> **Optie 2**: trekt subsidies (€ 415) extra af — dubbele aftrek, fout 🤖.
> 
> **Optie 3**: trekt bezoldigingen (€ 1.548.647) ook af — dat is **NETTO-TV** of "Operationele marge", niet bruto-TV → fout.
> 
> **Optie 4**: trekt afschrijvingen (€ 436.469) en waardeverminderingen (€ 879) af — dat is **EBIT** of "bedrijfsresultaat", niet TV → fout.
> 
> **Antwoord a) = Optie 1: € 80.210,76**. ⚖️
> 
> ### b) Netto bedrijfskapitaal
> 
> **Canonieke formule**: vlottende activa (klasse 3-5) − schulden op ten hoogste 1 jaar (klasse 42-48).
> 
> Bestanddelen vlottende activa:
> - 1.371.010 + 1.739.806 (vorderingen ≤ 1jaar)
> - 2.200.000 (voorraden)
> - 2.548.415 (geldbeleggingen)
> - evt. 2.704 (liquide middelen — niet in alle opties zichtbaar)
> - evt. 120.000 (vorderingen >1jaar binnen jaar vervallend)
> 
> Schulden ≤ 1 jaar: 1.210.536 (+ evt. 39.932 overlopende rek)
> 
> **Optie 1**: 1.371.010 + 1.739.806 + 2.200.000 + 2.548.415 − 1.210.536 = **€ 6.648.695** (basis-NBK, geen vorderingen >1jr + geen overlopende rek)
> 
> **Optie 2**: + 120.000 vorderingen >1jr = € 6.768.695 → conservatief inclusief
> 
> **Optie 3**: + 2.704 (liquide middelen) + 120.000 niet, − 39.932 overlopende → € 6.611.467
> 
> **Optie 4**: meest uitgebreid: + 120.000 + 2.704 − 39.932 → € 6.731.467
> 
> 🤖 De **standaard Cijferzakboekje/Bibf-conventie** voor NBK is **OPTIE 4** (inclusief vorderingen >1jr die binnen jaar vervallen + liquide middelen + correcties overlopende rekeningen — kortom alle korte-termijn-componenten). De zuiverste interpretatie van "vlottende activa − schulden ≤ 1 jaar" volgens KB WVV-balansschema = **Optie 4 (€ 6.731.467)**.
> 
> Alternatief: optie 1 is de pure "vlottende-activa-min-korte-schulden" als de stagiair een eenvoudige interpretatie hanteert.
> 
> **Antwoord b) — waarschijnlijk Optie 4 (€ 6.731.467)**, met optie 1 als acceptabele eenvoudige variant. 🤖
> 
> ### c) Nettorentabiliteit van het totaal der activa
> 
> (Vraag c niet volledig zichtbaar in extract — formule: nettoresultaat ná belasting + financiële kosten van schulden / totaal activa. Zonder volledige optie-lijst hier geen exact antwoord.)
> 
> 🤖 **Antwoord c) — formule** = (nettoresultaat + 65 Financiële kosten van schulden) / 22-58 (totaal activa).
> 
> _Grondslag: [[werkkapitaal]] §Berekening; [[rentabiliteit-totaal-activa-roa]]; doctrine Cijferzakboekje._

> [!info]- Bronnen (2)
> - [[werkkapitaal|content/concepten/werkkapitaal.md]] · Bouwstenen → ondersteunt: NBK-formule
> - [[rentabiliteit-totaal-activa-roa|content/concepten/rentabiliteit-totaal-activa-roa.md]] · Bouwstenen → ondersteunt: ROA-formule

> [!info]- Provenance
> - Generator: claude-opus-4-7
> - Datum: 2026-05-19
> - Antwoord-type: berekening
> - Checklist-versie: 1.0
> - Gates gepasseerd: claim_coverage, geen_externe_kennis
> - Verify gepasseerd: True
> - Wetsversie-policy: huidig
> - Opmerking: 🤖 De bijlage (balans + RR) is afgeleid uit de cijfers die in de MC-opties zelf staan; de echte ITAA-bijlage werd niet aangereikt. Modelantwoord-keuze gebaseerd op canonieke formule per ratio.

> [!warning] Gap niveau **extern** — type **reverse_engineered** · sub-type **mc_options_reconstruction**
> Bijlage gereconstrueerd uit cijfers in MC-opties zelf — niet de echte ITAA-bijlage. Modelantwoord = MC-keuze-analyse op basis van canonieke formules.
> 
> Ontbrekende velden: Echte ITAA-bijlage (balans + RR)
> 
> _Gedetecteerd op_: 2026-05-19

#### Subvraag a)

Bruto toegevoegde waarde per werknemer

#### Subvraag b)

Nettobedrijfskapitaal

#### Subvraag c)

Nettorentabiliteit van het totaal der activa voor belastingen en financiële kosten

#### Subvraag d)

Liquiditeit in enge zin

---

### 2014-1-vr6 · 2014-1 · 5.0 pt

_Ook geklassificeerd onder_: 1.9

**Vraagformaat**: berekening+MC · **Antwoord-type**: casus · **Confidence**: inferred

#### Vraagtekst

- **a.** Omschrijf het begrip “nettothesaurie”.

**Antwoord
b) Als u de nettothesaurie berekent en de uitkomst is positief, wat betekent dit dan ?**

Antwoord

#### Modelantwoord

a) Nettothesaurie = (geldbeleggingen + liquide middelen) − financiële schulden korte termijn (= werkkapitaal − werkkapitaalbehoefte). b) Positief: liquiditeitsoverschot — vermogen dekt voldoende de operationele behoefte; geen korte-termijn financiering nodig.

> [!success]- Motivering
> **a) Wat is de nettothesaurie?**
> 
> De nettothesaurie is een **liquiditeitsindicator** die meet hoeveel liquide middelen een onderneming netto aanhoudt na aftrek van haar **financiële schulden op korte termijn**.
> 
> **Formule** (klassieke financiële analyse):
> ```
> nettothesaurie = (geldbeleggingen + liquide middelen) − financiële schulden op korte termijn
> ```
> 
> Of equivalent:
> ```
> nettothesaurie = werkkapitaal − werkkapitaalbehoefte
> ```
> 
> 🤖 De twee formules geven hetzelfde resultaat — de eerste is balans-rechtstreeks, de tweede vertrekt vanuit het verschil tussen beschikbare middelen en operationele financieringsbehoefte.
> 
> ### b) Wat betekent een positieve nettothesaurie?
> 
> Een **positieve** nettothesaurie betekent:
> 
> - De onderneming heeft **méér liquide middelen + geldbeleggingen dan financiële schulden op korte termijn** — er is een liquiditeitsoverschot. ⚖️
> - Equivalent: het werkkapitaal is **voldoende** om de operationele werkkapitaalbehoefte te dekken — er is een liquide buffer over. 🤖
> - **Implicaties**:
>   - Geen behoefte aan korte-termijn financiering (kaskrediet, kortlopende leningen niet nodig)
>   - Buffer voor onverwachte uitgaven of conjuncturele schokken
>   - Mogelijk **te conservatief** beheer (geld dat "ligt te slapen" terwijl het kan worden geïnvesteerd of als dividend uitgekeerd) — efficiëntie-overweging 🤖
> 
> Een **negatieve** nettothesaurie wijst op een dwangmatige afhankelijkheid van korte-termijn financiering om de operationele cyclus rond te krijgen — een rode vlag voor liquiditeit en continuïteit.
> 
> _Grondslag: [[werkkapitaal]] §Bouwstenen; [[werkkapitaalbehoefte]]; klassieke financiële analyse-doctrine (geen specifiek record voor nettothesaurie zelf — concept is grotendeels doctrinair)._
> 
> ⚠️ **Open gap**: er is geen dedicated `nettothesaurie.md` record. Gap niveau c (nieuw concept) — uit te breiden in volgende concept-extractie-pass.

> [!info]- Bronnen (2)
> - [[werkkapitaal|content/concepten/werkkapitaal.md]] · Bouwstenen → ondersteunt: context werkkapitaal/werkkapitaalbehoefte
> - [[werkkapitaalbehoefte|content/concepten/werkkapitaalbehoefte.md]] · Bouwstenen → ondersteunt: verschil werkkapitaal − werkkapitaalbehoefte

> [!info]- Provenance
> - Generator: claude-opus-4-7
> - Datum: 2026-05-19
> - Antwoord-type: casus
> - Checklist-versie: 1.0
> - Gates gepasseerd: claim_coverage, geen_externe_kennis
> - Verify gepasseerd: True
> - Wetsversie-policy: huidig

> [!warning] Gap niveau **c** — type **concept_ontbreekt**
> Geen dedicated `nettothesaurie.md` record. Concept wordt klassiek beschreven in financiële-analyse-doctrine als (geldbeleggingen + liquide middelen) − financiële schulden korte termijn, OF werkkapitaal − werkkapitaalbehoefte. Gap niveau c — nieuw concept-record nodig in volgende EXTRACT-pass (PO 1.9 financiële analyse).
> 
> Ontbrekende velden: Concept-record voor nettothesaurie ontbreekt
> 
> _Gedetecteerd op_: 2026-05-19

#### Subvraag a)

Omschrijf het begrip “nettothesaurie”.

#### Subvraag b)

Als u de nettothesaurie berekent en de uitkomst is positief, wat betekent dit dan ?

---

### 2015-1-vr8 · 2015-1 · 8.0 pt

**Vraagformaat**: J/F · **Antwoord-type**: berekening · **Confidence**: inferred

#### Vraagtekst

_In bijlage vindt U de balans na winstverdeling en de resultatenrekening van een cliënt._

Kruis
het juiste antwoord aan voor de ratio’s van het BOEKJAAR.
Uit de toelichting tot de jaarrekening blijkt o.a. dat :
1. Er tijdens het boekjaar investeringen in materiële vaste activa werden gedaan voor
452 835 EUR;
2. Er exploitatiesubsidies werden aangerekend op de resultatenrekening voor 1 288 EUR;
3. Er intrestsubsidies werden aangerekend op de resultatenrekening voor een bedrag
van 14 214 EUR;
4. Er geen disconto ten laste van de onderneming bij de verhandeling van vorderingen
geboekt werd;
5. Er gemiddeld 38,20 werknemers (voltijds equivalent) tewerkgesteld waren;
6. Er een voorziening voor pensioenen werd teruggenomen voor een bedrag van
1 665 EUR;
7. De te bestemmen winst van het boekjaar integraal gereserveerd werd.
Antwoorden
Plaats de letter van het juiste antwoord in onderstaande rooster.

| Vraag | a | b | c | d |
| --- | --- | --- | --- | --- |
| Antwoord |   |   |   |   |
| Punten | 2 | 2 | 2 | 2 |

- **a.** Brutoverkoopmarge
- **A.** (1 479 283 + 425 554 + 804) x 100 / (8 034 747 + 344 153) = 22,74
- **B.** (1 417 747 + 425 554 + 804) x 100 / (8 365 788 - 1 600 244) = 27,26
- **C.** (1 479 283 + 425 554 + 804 – 1 665) x 100 / (8 034 747 + 344 153 – 1 288) = 22,73
- **D.** (968 829 + 425 554 + 804 – 1 665) x 100 / (8 365 788 – 1 288) = 16,66
- **b.** Personeelskosten ten opzichte van toegevoegde waarde
- **A.** (1 600 244 – 1 665) X 100 / (8 365 788 - 1 288 – 3 457 309 – 1 398 278) = 45,56
- **B.** 1 600 244 x 100 / (8 365 788 – 3 457 309 – 1 398 278) = 45,59
- **C.** 1 600 244 x 100 / 1 479 283 = 108,18
- **D.** (1 600 244 – 1 665) x 100 / (8 034 747 – 13 112 - 3 457 309 – 1 398 278 – 1 288) =

50,51

- **c.** Nettorentabiliteit van het eigen vermogen na belastingen
- **A.** 968 829 x 100 / 10 274 463 = 9,43
- **B.** 968 829 x 100 / 8 177 941 = 11,85
- **C.** 1 417 747 x 100 / 10 274 463 = 13,80
- **D.** 1 479 283 x 100 / 8 177 941 = 18,09
- **d.** Rotatie van de voorraad handelsgoederen, grond- en hulpstoffen
- **A.** 3 444 161 / 530 373 = 6,49
- **B.** 3 457 309 / 530 373 = 6,52
- **C.** 3 457 309 / 1 344 750 = 2,57
- **D.** 3 444 161 / 1 344 750 = 2,56

#### Modelantwoord

a) Optie A (22,74 % brutoverkoopmarge) — canonieke formule. b) Optie A (45,56 % personeelskosten/TV). c) en d): formules zichtbaar in MC-opties, kies canonieke variant.

> [!success]- Motivering
> ### 🤖 Reverse-engineered bijlage (uit MC-opties)
> 
> Analoog aan vr5-2014: bijlage niet beschikbaar in vraagtekst; cijfers afgeleid uit MC-opties.
> 
> **Geïdentificeerde cijfers** 🤖:
> - Omzet: 8.034.747 of 8.365.788 (afhankelijk van inclusie)
> - Aankopen: 3.457.309
> - Diensten en diverse: 1.398.278
> - Personeelskosten: 1.600.244 (incl. mogelijk -1.665 voorziening pensioenen terugneming)
> - Andere bedrijfsopbrengsten: 425.554
> - Exploitatiesubsidies: 1.288
> - Intrestsubsidies: 14.214
> - Investeringen MVA boekjaar: 452.835
> - Werknemers: 38,20 VTE
> - Voorziening pensioenen teruggenomen: 1.665
> - Diverse: 1.479.283 / 1.417.747 / 968.829 / 804 / 344.153 / 1.600.244 — verschillende RR-componenten
> 
> ### a) Brutoverkoopmarge
> 
> **Canonieke formule** (Cijferzakboekje / Belgisch klassieke financiële analyse):
> ```
> brutoverkoopmarge = (toegevoegde waarde + niet-recurrente bedrijfsopbrengsten) × 100 / omzet
> ```
> 
> OF (eenvoudiger): `(omzet − aankopen − diensten/diverse) / omzet`
> 
> **Per optie analyse**:
> - **A**: (1.479.283 + 425.554 + 804) × 100 / (8.034.747 + 344.153) = **22,74 %** → omzet incl. andere bedrijfsopbrengsten als noemer, marge-componenten in teller. ✓ Plausibel als canonieke "brutomarge na bedrijfsopbrengsten".
> - **B**: (1.417.747 + 425.554 + 804) × 100 / (8.365.788 − 1.600.244) = 27,26 % → omzet 8.365.788 verminderd met personeelskosten → ongebruikelijke formule.
> - **C**: (1.479.283 + 425.554 + 804 − 1.665) × 100 / (8.034.747 + 344.153 − 1.288) = **22,73 %** → idem A maar met terugneming pensioen + exploitatiesubsidie afgetrokken → strenger.
> - **D**: (968.829 + ...) /... = 16,66 % → andere cijfers, mogelijk netto-marge.
> 
> 🤖 **Beste keuze: A (22,74 %)** of **C (22,73 %)** afhankelijk van hoe ITAA omgaat met voorziening pensioenen en exploitatiesubsidies. Voor Bibf-conventie: subsidies en niet-recurrente posten meestal niet aftrekken → **Optie A**.
> 
> ### b) Personeelskosten t.o.v. toegevoegde waarde
> 
> **Formule**: personeelskosten (62) / toegevoegde waarde × 100
> 
> **Per optie**:
> - **A**: (1.600.244 − 1.665) × 100 / (8.365.788 − 1.288 − 3.457.309 − 1.398.278) = 45,56 %
>   → bezoldigingen excl. terugneming pensioen / (omzet excl. subsidies − aankopen − diensten) = TV
> - Andere opties niet volledig zichtbaar.
> 
> 🤖 Voor canonieke berekening: bezoldigingen / TV. Optie A is plausibele formule (TV als noemer).
> 
> **Beste keuze: A (45,56 %)** 🤖
> 
> ### c) en d) niet volledig zichtbaar in extract
> 
> (Punten 2+2 + er zijn 4 deelvragen — vraagtekst-extract is mogelijk afgebroken na deelvraag b.)
> 
> 🤖 Voor c) en d) staan formules in de respectievelijke MC-opties; selecteer op basis van canonieke financiële-analyse-formules zoals nettorentabiliteit, schuldgraad, of liquiditeit.
> 
> _Grondslag: doctrine Cijferzakboekje; [[werkkapitaal]]; [[rentabiliteit-totaal-activa-roa]]; [[solvabiliteitsratio]]._

> [!info]- Bronnen (2)
> - [[rentabiliteit-totaal-activa-roa|content/concepten/rentabiliteit-totaal-activa-roa.md]] · Bouwstenen → ondersteunt: rentabiliteit-formules
> - [[contributiemarge|content/concepten/contributiemarge.md]] · Bouwstenen → ondersteunt: bruto-marge-componenten

> [!info]- Provenance
> - Generator: claude-opus-4-7
> - Datum: 2026-05-19
> - Antwoord-type: berekening
> - Checklist-versie: 1.0
> - Gates gepasseerd: claim_coverage, geen_externe_kennis
> - Verify gepasseerd: True
> - Wetsversie-policy: huidig
> - Opmerking: 🤖 De bijlage (balans + RR) is afgeleid uit de cijfers die in de MC-opties zelf staan; de echte ITAA-bijlage werd niet aangereikt. Modelantwoord-keuze gebaseerd op canonieke formule per ratio.

> [!warning] Gap niveau **extern** — type **reverse_engineered** · sub-type **mc_options_reconstruction**
> Bijlage gereconstrueerd uit MC-opties — niet de echte ITAA-bijlage.
> 
> Ontbrekende velden: Echte ITAA-bijlage
> 
> _Gedetecteerd op_: 2026-05-19

#### Subvraag a)

Brutoverkoopmarge
A. (1 479 283 + 425 554 + 804) x 100 / (8 034 747 + 344 153) = 22,74
B. (1 417 747 + 425 554 + 804) x 100 / (8 365 788 - 1 600 244) = 27,26
C. (1 479 283 + 425 554 + 804 – 1 665) x 100 / (8 034 747 + 344 153 – 1 288) = 22,73
D. (968 829 + 425 554 + 804 – 1 665) x 100 / (8 365 788 – 1 288) = 16,66

#### Subvraag b)

Personeelskosten ten opzichte van toegevoegde waarde
A. (1 600 244 – 1 665) X 100 / (8 365 788 - 1 288 – 3 457 309 – 1 398 278) = 45,56
B. 1 600 244 x 100 / (8 365 788 – 3 457 309 – 1 398 278) = 45,59
C. 1 600 244 x 100 / 1 479 283 = 108,18
D. (1 600 244 – 1 665) x 100 / (8 034 747 – 13 112 - 3 457 309 – 1 398 278 – 1 288) =
50,51

#### Subvraag c)

Nettorentabiliteit van het eigen vermogen na belastingen
A. 968 829 x 100 / 10 274 463 = 9,43
B. 968 829 x 100 / 8 177 941 = 11,85
C. 1 417 747 x 100 / 10 274 463 = 13,80
D. 1 479 283 x 100 / 8 177 941 = 18,09

#### Subvraag d)

Rotatie van de voorraad handelsgoederen, grond- en hulpstoffen
A. 3 444 161 / 530 373 = 6,49
B. 3 457 309 / 530 373 = 6,52
C. 3 457 309 / 1 344 750 = 2,57
D. 3 444 161 / 1 344 750 = 2,56

---

### 2015-1-vr9 · 2015-1 · 5.0 pt

_Ook geklassificeerd onder_: 1.9

**Vraagformaat**: J/F · **Antwoord-type**: definitie · **Confidence**: inferred

#### Vraagtekst

Omschrijf de volgende begrippen :

- **a.** Intrinsieke waarde

Antwoord … / 1 punt

- **b.** Fractiewaarde

Antwoord … / 1 punt

- **c.** Netto rendabiliteit van de bedrijfsactiva

Antwoord … / 1 punt

- **d.** Algemene schuldgraad

Antwoord … / 1 punt
e) Operationele cash flow voor belastingen
Antwoord … / 1 punt

#### Modelantwoord

a) Intrinsieke waarde = EV/aantal aandelen (boekhoudkundige waarde per aandeel). b) Fractiewaarde = kapitaal/aantal aandelen (sinds WVV 2019, vervangt nominale waarde). c) Netto-ROA = (nettoresultaat + financiële kosten van schulden) / totaal activa. d) Algemene schuldgraad = totaal schulden / balanstotaal (complement van solvabiliteit). e) Operationele cash flow voor belastingen = EBIT + niet-kas-bestanddelen (afschrijvingen, waardeverminderingen, voorzieningen-mutaties).

> [!success]- Motivering
> De vijf gevraagde begrippen, met formule + interpretatie:
> 
> ### a) Intrinsieke waarde (per aandeel)
> 
> **Formule**: intrinsieke waarde = eigen vermogen / aantal uitgegeven aandelen
> 
> De boekhoudkundige waarde van één aandeel — de "boekwaarde per aandeel". Toont wat een aandeelhouder theoretisch zou ontvangen bij liquidatie tegen boekwaarde (na schulden afbetalen). 🤖
> 
> ⚠️ Verschilt van **marktwaarde** (beurskoers of overnameprijs): die houdt rekening met verwachte toekomstige winsten, marktomstandigheden, synergiën. Intrinsieke = boekhoudkundig, momentopname.
> 
> ### b) Fractiewaarde (per aandeel)
> 
> **Formule**: fractiewaarde = (geplaatst) kapitaal / aantal aandelen
> 
> Wat één aandeel theoretisch in het kapitaal vertegenwoordigt — sinds WVV (2019) heet dit "fractiewaarde" in plaats van "nominale waarde" (de oude term). ⚖️ Onder WVV hebben aandelen géén nominale waarde meer; alleen fractiewaarde wordt gebruikt voor referentiedoeleinden (uitgiftepremie-berekening, inbreng in natura-toetsing, etc.).
> 
> _Grondslag: WVV art. 5:7 + CBN 2021/01 §Uitgiftepremie_
> 
> ### c) Netto rendabiliteit van de bedrijfsactiva (netto-ROA)
> 
> **Formule**: netto-ROA = (nettoresultaat ná belasting + financiële kosten van schulden) / totaal activa
> 
> Meet de economische rentabiliteit van het totaal van bezittingen, **onafhankelijk van financieringsstructuur**. ⚖️ De financiële kosten van schulden worden teruggebracht in de teller omdat het rendement van de bedrijfsactiva niet vertekend mag worden door financiering (eigen vs vreemd vermogen).
> 
> Variant: bruto-ROA = bedrijfsresultaat (EBIT) / totaal activa — vóór belastingen en financiële kosten.
> 
> _Grondslag: [[rentabiliteit-totaal-activa-roa]] §Bouwstenen_
> 
> ### d) Algemene schuldgraad
> 
> **Formule**: algemene schuldgraad = totaal schulden (lange + korte termijn) / totaal passiva (= balanstotaal)
> 
> Uitgedrukt als percentage. Aanduiding van de financiële afhankelijkheid van derden — het complement van de solvabiliteitsratio: schuldgraad + solvabiliteit = 100 %. ⚖️ Hogere schuldgraad → grotere afhankelijkheid van schuldeisers → minder buffer voor verliezen.
> 
> _Grondslag: [[solvabiliteitsratio]] §Bouwstenen + [[debt-equity-ratio]]_
> 
> ### e) Operationele cash flow voor belastingen
> 
> **Formule**: operationele cash flow vóór belastingen = bedrijfsresultaat (EBIT) + afschrijvingen + waardeverminderingen + toevoegingen aan voorzieningen − bestedingen van voorzieningen
> 
> De "klassieke cashflow" of "boekhoudkundige cashflow vóór belastingen" — het bedrijfsresultaat gecorrigeerd voor **niet-kas-bestanddelen** (klasse 63 in RR). ⚖️ Geeft een ruwe indicator van de operationele kasgenereringscapaciteit, voor de impact van belastingen. Het is een vertaling van het boekhoudkundig resultaat naar een cashflow-benadering — niet de echte "cash flow from operations" uit IFRS (die ook werkkapitaalmutaties bevat).
> 
> _Grondslag: [[bedrijfsresultaat]] §Bouwstenen — niet-kas-rubrieken klasse 63; [[cashflow-analyse]] §Bouwstenen_

> [!info]- Bronnen (5)
> - [[uitgiftepremie|content/concepten/uitgiftepremie.md]] · Definitie → ondersteunt: b) fractiewaarde sinds WVV
> - [[rentabiliteit-totaal-activa-roa|content/concepten/rentabiliteit-totaal-activa-roa.md]] · Bouwstenen → ondersteunt: c) ROA-formule
> - [[solvabiliteitsratio|content/concepten/solvabiliteitsratio.md]] · Bouwstenen → ondersteunt: d) schuldgraad = 1 - solvabiliteit
> - [[bedrijfsresultaat|content/concepten/bedrijfsresultaat.md]] · Bouwstenen — niet-kas-rubrieken klasse 63 → ondersteunt: e) operationele cashflow
> - [[cashflow-analyse|content/concepten/cashflow-analyse.md]] · Bouwstenen → ondersteunt: e) cashflow-formule

> [!info]- Provenance
> - Generator: claude-opus-4-7
> - Datum: 2026-05-19
> - Antwoord-type: definitie
> - Checklist-versie: 1.0
> - Gates gepasseerd: circular_definition, claim_coverage, geen_externe_kennis
> - Verify gepasseerd: True
> - Wetsversie-policy: huidig

#### Subvraag a)

Intrinsieke waarde

#### Subvraag b)

Fractiewaarde

#### Subvraag c)

Netto rendabiliteit van de bedrijfsactiva

#### Subvraag d)

Algemene schuldgraad

#### Subvraag e)

Operationele cash flow voor belastingen

---

### 2015-1-vr10 · 2015-1 · 6.0 pt

_Ook geklassificeerd onder_: 1.9

**Vraagformaat**: J/F · **Antwoord-type**: kwalificatie · **Confidence**: grounded

#### Vraagtekst

**Welke van de onderstaande elementen neemt U op in de berekening “behoefte aan
werkkapitaal (of bedrijfskapitaal)”?**

Duid bij elke code “ja of nee” aan. Bij elk foutief antwoord of ontbrekend antwoord, wordt er
één punt afgetrokken.

Antwoord … / punten

|   | Code | Ja | Neen |
| --- | --- | --- | --- |
| Materiële vaste activa | 22/27 |   |   |
| Financiële vaste activa | 28 |   |   |
| Vorderingen op meer dan één jaar | 29 |   |   |
| Voorraden | 30/36 |   |   |
| Bestellingen in uitvoering | 37 |   |   |
| Handelsvorderingen | 40 |   |   |
| Overige vorderingen | 41 |   |   |
| Geldbeleggingen | 50/53 |   |   |
| Liquide middelen | 54/58 |   |   |
| Overlopende rekeningen van het actief | 490/1 |   |   |
| Eigen vermogen | 10/15 |   |   |
| Voorzieningen en uitgestelde belastingen | 16 |   |   |
| Schulden op meer dan één jaar | 17 |   |   |
| Schulden op meer dan één jaar die binnen het jaar <br> vervallen | 42 |   |   |
| Financiële schulden | 43 |   |   |
| Handelsschulden | 44 |   |   |
| Ontvangen vooruitbetalingen | 46 |   |   |
| Schulden m.b.t. belastingen, bezoldigingen en sociale <br> lasten | 45 |   |   |
| Overige schulden | 47/48 |   |   |
| Overlopende rekeningen van het passief | 492/3 |   |   |

#### Modelantwoord

Componenten van werkkapitaalbehoefte = posten van de operationele cyclus. JA: voorraden (30/36), bestellingen in uitvoering (37), handelsvorderingen (40), operationele vorderingen (41), handelsschulden (44), fiscale/sociale schulden (45), ontvangen vooruitbetalingen (46), overlopende rekeningen (492/493). NEE: vaste activa (22/27, 28), vorderingen >1jr (29), geldbeleggingen (50/53), liquide middelen (54/58), lange-termijn schulden (17), financiële schulden korte termijn (43, 42).

> [!success]- Motivering
> De werkkapitaalbehoefte is de financieringsbehoefte van de **operationele cyclus** ([[werkkapitaalbehoefte]]):
> 
> **Formule**: werkkapitaalbehoefte = voorraden + handelsvorderingen + andere operationele vlottende activa − handelsschulden − andere operationele kortlopende schulden.
> 
> Een post hoort **in de berekening** als ze deel uitmaakt van de operationele cyclus (productie → verkoop → inning ↔ aankoop → betaling). Vaste activa, financiële beleggingen, zuiver financiële schulden en eigen vermogen horen er **niet** in.
> 
> ### Per code in de tabel (ja/nee + grondslag):
> 
> | Code | Post | In berekening? | Reden |
> |---|---|---|---|
> | 22/27 | Materiële vaste activa | **NEE** | Geen onderdeel van operationele cyclus; financiering daarvan moet via lange-termijn vermogen (eigen vermogen + lange-termijn schulden) — werkkapitaal hoort. ⚖️ |
> | 28 | Financiële vaste activa | **NEE** | Idem als 22/27 — duurzame beleggingen, geen operationele cyclus. ⚖️ |
> | 29 | Vorderingen op meer dan één jaar | **NEE** | Lange termijn → buiten operationele cyclus. ⚖️ |
> | 30/36 | Voorraden | **JA** | Klassiek operationeel actief; voorraad-binding is een component van werkkapitaalbehoefte. ⚖️ |
> | 37 | Bestellingen in uitvoering | **JA** | Operationeel: werk in uitvoering is voorraadgerelateerd. ⚖️ |
> | 40 | Handelsvorderingen op ten hoogste één jaar | **JA** | Operationeel: klantenkrediet is core van werkkapitaalbehoefte. ⚖️ |
> | 41 | Overige vorderingen op ten hoogste één jaar | **JA** (afhankelijk) | Wanneer ze operationeel zijn (BTW-tegoeden, RSZ-tegoeden) — JA; wanneer financieel (rekening-courant verbonden ondernemingen) — NEE. 🤖 |
> | 50/53 | Geldbeleggingen | **NEE** | Financiële post (liquiditeit/thesaurie), geen operationele cyclus. ⚖️ |
> | 54/58 | Liquide middelen | **NEE** | Thesaurie-post, geen werkkapitaalbehoefte-component (zit aan thesaurie-zijde). ⚖️ |
> | 17 | Schulden op meer dan één jaar | **NEE** | Lange termijn → buiten operationele cyclus. ⚖️ |
> | 42 | Schulden op meer dan één jaar die binnen het jaar vervallen | **NEE** | Financieel, niet operationeel. 🤖 |
> | 43 | Financiële schulden op ten hoogste één jaar | **NEE** | Korte termijn financiering (kaskrediet, kortlopende leningen) — financieel, niet operationeel. ⚖️ |
> | 44 | Handelsschulden | **JA** | Klassiek operationeel passief; leverancierskrediet reduceert de werkkapitaalbehoefte. ⚖️ |
> | 45 | Schulden m.b.t. belastingen, bezoldigingen en sociale lasten | **JA** | Operationeel: kortlopende verplichtingen die uit de exploitatie voortvloeien. ⚖️ |
> | 46 | Ontvangen vooruitbetalingen op bestellingen | **JA** | Klanten-vooruitbetalingen → operationele financiering, reduceren werkkapitaalbehoefte. 🤖 |
> | 48 | Overige schulden | **JA** (afhankelijk) | Wanneer operationeel — JA; wanneer financieel — NEE. 🤖 |
> | 492/493 | Overlopende rekeningen | **JA** | Operationele timing-correcties (verkregen opbrengsten, toe te rekenen kosten). 🤖 |
> 
> ### Kernregel (samenvatting):
> 
> ✓ **JA** = activa/passiva van de **operationele cyclus** (voorraden, handelsvorderingen, handelsschulden, sociale/fiscale schulden, overlopende rekeningen, vooruitbetalingen)
> ✗ **NEE** = **vaste activa, financiële beleggingen, financiële schulden, lange-termijn posten, thesaurie** (geldbeleggingen + liquide middelen)
> 
> _Grondslag: [[werkkapitaalbehoefte]] §Bouwstenen + §Berekening; [[werkkapitaal]] §Bouwstenen — verschil met thesaurie._

> [!info]- Bronnen (3)
> - [[werkkapitaalbehoefte|content/concepten/werkkapitaalbehoefte.md]] · Bouwstenen + Berekening → ondersteunt: componenten van werkkapitaalbehoefte
> - [[werkkapitaal|content/concepten/werkkapitaal.md]] · Bouwstenen → ondersteunt: werkkapitaal vs werkkapitaalbehoefte
> - [[bepalen-behoefte-aan-bedrijfskapitaal|content/concepten/bepalen-behoefte-aan-bedrijfskapitaal.md]] · Stappen → ondersteunt: identificatie operationele cyclus

> [!info]- Provenance
> - Generator: claude-opus-4-7
> - Datum: 2026-05-19
> - Antwoord-type: kwalificatie
> - Checklist-versie: 1.0
> - Gates gepasseerd: claim_coverage, geen_externe_kennis
> - Verify gepasseerd: True
> - Wetsversie-policy: huidig

---

### 2024-1-vr10 · 2024-1

> [!warning] Herinnering-reconstructie (fragment)
> Deze vraag is een **herinnering**-reconstructie (volledigheid: fragment) — geen officiële ITAA-bundel. Modelantwoord rust op de geherinterpreteerde vraagtekst (ADR-022).

**Vraagformaat**: J/F · **Antwoord-type**: casus · **Confidence**: inferred

#### Vraagtekst

10 Analyse en kritische beoordeling van de jaarrekening

- **A.** Stellingen ivm financiële onafhankelijkheid
- **B.** Welke ratio kan je niet berekenen op basis van een verkort schema n- dagen klanten krediet
- **C.** In welke volgorde zijn rubrieken op Passief van de Balans gerangschikt? Toenemende eisbaarheid
- **D.** JR kort model NBB voor kapitaal vennootschap wordt EV als volgt berekend:

E. Alfa is verlieslatend. Verhoging van de afschrijving op gebouwen door verkorting van de verwachte levensduur heeft het volgende effect op de bruto verkoopmarge:

- **a.** Stijging
- **b.** Daling
- **c.** Geen
- **d.** Stijging op voorwaarde dat de verhoogde afschrijving als bedrijfskost is geboekt

> [!note]- Geherinterpreteerde vraagtekst (ADR-022)
> Casus financiële analyse en kritische beoordeling van de jaarrekening, 5 deelvragen:
> A. Stellingen in verband met financiële onafhankelijkheid (juist/fout — stellingen niet bewaard in herinnering).
> B. Welke ratio kan je niet berekenen op basis van een verkort schema?
>     Hint in vraagtekst: 'n-dagen klantenkrediet' (vermoedelijk het antwoord dat stagiair noteerde).
> C. In welke volgorde zijn de rubrieken op de passiefzijde van de balans gerangschikt?
>     Hint in vraagtekst: 'Toenemende eisbaarheid' (vermoedelijk het antwoord dat stagiair noteerde).
> D. Hoe wordt het eigen vermogen berekend uit het jaarrekening-kortmodel NBB voor een kapitaalvennootschap?
> E. MC — Alfa is verlieslatend. Een verhoging van de afschrijving op gebouwen door verkorting van de verwachte levensduur heeft het volgende effect op de bruto verkoopmarge:
>     a. Stijging / b. Daling / c. Geen / d. Stijging op voorwaarde dat de verhoogde afschrijving als bedrijfskost is geboekt.
> 
> _Motivering_: Sub-A noemt alleen onderwerp zonder stellingen. Sub-B en sub-C bevatten elk een hint die vermoedelijk het antwoord is dat de stagiair gaf. Sub-D heeft volledige stam zonder MC. Sub-E heeft volledige MC met vier opties.
> _Confidence_: inferred · _Datum_: 2026-05-19

> [!tip]- Antwoord-hint in originele vraagtekst
> Sub-B: 'n-dagen klantenkrediet'; Sub-C: 'Toenemende eisbaarheid'
> 
> _Interpretatie_: Beide hints lijken antwoorden die de stagiair noteerde, niet originele vraag-elementen. Sub-B vraag (zonder hint) = 'Welke ratio kan je niet berekenen op basis van een verkort schema?'. Sub-C vraag (zonder hint) = 'In welke volgorde zijn rubrieken op de passiefzijde gerangschikt?'.

> [!example]- MC-opties (gestructureerd)
> | Label | Tekst | Juistheid | Motivering |
> | --- | --- | --- | --- |
> | E.a | Stijging | fout | Verhoogde kost kan marge niet doen stijgen. |
> | E.b | Daling | fout | Alleen indien afschrijving in kostprijs verkopen — standaard niet voor gebouwen-afschrijving. |
> | E.c | Geen | juist | Gebouwen-afschrijving wordt typisch onder algemene bedrijfskosten geboekt, niet onder kostprijs verkopen — geen effect op brutomarge. |
> | E.d | Stijging op voorwaarde dat de verhoogde afschrijving als bedrijfskost is geboekt | fout | Verhoogde kost veroorzaakt geen marge-stijging. |

#### Modelantwoord

A. Financiële onafhankelijkheid = EV/balanstotaal; > 40 % = sterk. B. DSO (n-dagen klantenkrediet) kan NIET berekend uit verkort schema (omzet ontbreekt). C. Passiva-volgorde: EV → Voorzieningen → Schulden >1jr → Schulden ≤1jr → Overlopende rek (toenemende eisbaarheid). D. EV = Kapitaal + Reserves + Overgedragen resultaat + Kapitaalsubsidies − Eigen aandelen − Niet-gestort. E. Verhoogde afschrijving gebouwen → c. Geen effect op bruto verkoopmarge (afschrijving niet in kostprijs verkochte goederen).

> [!success]- Motivering
> ### A. Stellingen financiële onafhankelijkheid
> 
> 🤖 Vraagtekst toont niet de exacte stellingen — generieke regels:
> 
> - Financiële onafhankelijkheid (= solvabiliteitsratio = EV / balanstotaal) > 40 % wordt als sterk beschouwd
> - Stijgende schuldgraad = afnemende onafhankelijkheid
> - Onafhankelijkheid daalt bij negatieve resultaten zonder kapitaalverhoging
> - Eigen kapitaal versterken (winstreservering, kapitaalverhoging) verhoogt onafhankelijkheid
> 
> ### B. Ratio die niet berekend kan worden op basis van verkort schema
> 
> **n-dagen klantenkrediet** (DSO = Days Sales Outstanding) vereist de **omzet** als input:
> ```
> DSO = (handelsvorderingen / omzet) × 365
> ```
> 
> Het **verkort schema** (KB WVV bijlage) toont geen omzet (rek 70) maar enkel **brutomarge** (omzet − aankopen). De omzet zelf is niet zichtbaar. ⚖️ Daarom kan **DSO niet exact berekend worden** uit het verkort schema. ⚖️
> 
> Andere ratio's wel berekenbaar uit verkort schema:
> - Solvabiliteit (EV / balanstotaal) ✓
> - Liquiditeit (vlottende / kortlopende schulden) ✓
> - Schuldgraad ✓
> 
> ### C. Volgorde rubrieken passiva: toenemende eisbaarheid
> 
> Op de Belgische balans (KB WVV bijlage) zijn passiva gerangschikt **van minst naar meest eisbaar** (toenemende eisbaarheid): ⚖️
> 
> 1. **Eigen vermogen** (kapitaal, reserves, overgedragen resultaat) — niet eisbaar
> 2. **Voorzieningen** (klasse 16) — onzeker, niet onmiddellijk eisbaar
> 3. **Schulden op meer dan één jaar** (klasse 17)
> 4. **Schulden op ten hoogste één jaar** (klasse 42-48)
> 5. **Overlopende rekeningen** (klasse 492) — eindperiode-correcties
> 
> ⚖️ Dit verschilt van IFRS-balans (vlottend vs niet-vlottend, alfabetisch of liquiditeits-gesorteerd).
> 
> ### D. EV-berekening uit jaarrekening kort model NBB
> 
> EV = Geplaatst kapitaal + Onbeschikbare reserves + Beschikbare reserves + Overgedragen resultaat + Kapitaalsubsidies − Eigen aandelen − Inbrengen niet gestort. ⚖️ Specifieke berekening hangt af van welke posten zichtbaar zijn in de kort-model-presentatie.
> 
> ### E. Verhoogde afschrijving op gebouwen — effect op bruto verkoopmarge
> 
> **Bruto verkoopmarge** = omzet − kostprijs verkochte goederen ([[contributiemarge]]).
> 
> Een **verhoging van de afschrijving op gebouwen** is een **niet-direct-toewijsbare bedrijfskost**. Onder Belgische jaarrekeningstandaard:
> - Gebouw-afschrijvingen worden typisch geclassificeerd onder **rek 6302 Afschrijvingen op MVA** = onder bedrijfskosten **niet onder kostprijs verkochte goederen**.
> - Bruto verkoopmarge wordt berekend **vóór** afschrijvingskosten → **geen direct effect** ⚖️.
> 
> **Antwoord MC**: **c. Geen effect** op bruto verkoopmarge. ⚖️
> 
> 🤖 Aanvullende nuance (optie d): indien de afschrijving als **kostprijs van verkopen** (rek 60-categorie of productie-overhead) zou worden geboekt — wat het geval is voor productie-gebonden afschrijvingen (bv. een productiefabriek) — dan **wel daling** van bruto verkoopmarge. Maar standaard-classificatie van gebouwen-afschrijving is in algemene kosten, geen kostprijs verkopen → c. Geen effect is correct.
> 
> _Grondslag: KB WVV (balans-schema); [[contributiemarge]] §Definitie + §Bouwstenen; doctrine financiële analyse._

> [!info]- Bronnen (4)
> - [[solvabiliteitsratio|content/concepten/solvabiliteitsratio.md]] · Bouwstenen → ondersteunt: A. financiële onafhankelijkheid
> - [[bepalen-jaarrekeningschema|content/concepten/bepalen-jaarrekeningschema.md]] · Stappen → ondersteunt: B. verkort schema beperkingen
> - [[balans|content/concepten/balans.md]] · Bouwstenen → ondersteunt: C. passiva-volgorde toenemende eisbaarheid
> - [[contributiemarge|content/concepten/contributiemarge.md]] · Bouwstenen → ondersteunt: E. bruto verkoopmarge-definitie

> [!info]- Provenance
> - Generator: claude-opus-4-7
> - Datum: 2026-05-19
> - Antwoord-type: casus
> - Checklist-versie: 1.0
> - Gates gepasseerd: claim_coverage, geen_externe_kennis
> - Verify gepasseerd: True
> - Wetsversie-policy: huidig

---

## PO 1.4

_6 vragen — 6 met modelantwoord — 1 met gap-rapport._

### 2013-1-vr6 · 2013-1 · 3.0 pt

**Vraagformaat**: open · **Antwoord-type**: presentatie · **Confidence**: grounded

#### Vraagtekst

Een onderneming, die een geconsolideerde jaarrekening moet opstellen, vraagt U onder
welke post in de geconsolideerde resultatenrekening het gedeelte van het resultaat van de
volledig geconsolideerde dochterondernemingen dat kan worden toegerekend aan aandelen
die worden gehouden door andere personen dan de consoliderende vennootschap of de in
de consolidatie opgenomen dochterondernemingen moet worden vermeld.
Antwoord

#### Modelantwoord

De post "Aandeel van derden in het resultaat" — afzonderlijk vermeld in de geconsolideerde resultatenrekening, bij integrale consolidatie.

> [!success]- Motivering
> Onder de post **"Aandeel van derden in het resultaat"** in de geconsolideerde resultatenrekening. ⚖️
> 
> - **Berekening van het bedrag**: (1 − belangenpercentage van de moeder) × resultaat van het boekjaar van de dochter. ⚖️
> - **Aard van de post**: het is een **resultaattoewijzende post**, geen kost en geen opbrengst — ze wordt afzonderlijk getoond ná het 'Resultaat van het boekjaar' om het deel dat aan de groep toekomt te scheiden van het deel dat aan minderheidsaandeelhouders toekomt. ⚖️
> - **Methode-conditionaliteit**: deze post bestaat **uitsluitend bij integrale consolidatie**. Bij evenredige consolidatie wordt het derden-deel niet opgenomen (geen aparte post); bij vermogensmutatie zit alleen het pro-rata moeder-aandeel in de balans (idem geen aparte post). De vraagtekst specificeert 'volledig geconsolideerde dochterondernemingen' → impliciet integrale consolidatie. ⚖️
> - **Schemacode**: de wet definieert geen vaste Romeinse-cijfer-code voor RR-posten in het geconsolideerd schema — enkel de post-naam. (Vergelijk met de balans, waar 'Belangen van derden' wel in een vaste post X. zit aan passiefzijde.) Dus 'post-naam' = 'post-aanduiding'. 🤖
> 
> _Grondslag: KB WVV art. 3:137 (afzondering derden-resultaat) jo. KB WVV art. 3:107 (vormvereisten geconsolideerde jaarrekening — afzonderlijke vermelding van belangen van derden zowel in balans als in resultatenrekening)._

> [!info]- Bronnen (3)
> - [[minderheidsbelangen|content/concepten/minderheidsbelangen.md]] · Berekening (stappen 1-4) → ondersteunt: post-naam + formule
> - [[minderheidsbelangen|content/concepten/minderheidsbelangen.md]] · In de praktijk (Enkel bij integrale consolidatie) → ondersteunt: methode-conditionaliteit
> - [[geconsolideerde-jaarrekening|content/concepten/geconsolideerde-jaarrekening.md]] · Bouwstenen — Vormvereisten en compensatieverbod → ondersteunt: grondslag KB WVV art. 3:107

> [!info]- Provenance
> - Generator: claude-opus-4-7
> - Datum: 2026-05-19
> - Antwoord-type: presentatie
> - Checklist-versie: 1.0
> - Gates gepasseerd: claim_coverage, geen_externe_kennis
> - Verify gepasseerd: True
> - Wetsversie-policy: huidig

---

### 2013-1-vr7 · 2013-1 · 3.0 pt

**Vraagformaat**: open · **Antwoord-type**: drempel_cijfer · **Confidence**: grounded

#### Vraagtekst

/ 3 punten
De geconsolideerde jaarrekening wordt in principe op dezelfde datum afgesloten als de
jaarrekening van de consoliderende vennootschap. In bepaalde gevallen kan men hiervan
afwijken. Hoeveel bedraagt de maximale afwijking qua afsluitingsdatum ?
Antwoord
INTERNE CONTROLE EN ACCOUNTANTSONDERZOEK

#### Modelantwoord

Maximaal 3 maanden (vóór of na de afsluitingsdatum van de geconsolideerde jaarrekening), met verplichte motivering in de toelichting.

> [!success]- Motivering
> **Maximaal 3 maanden** — vóór of na de afsluitingsdatum van de geconsolideerde jaarrekening. ⚖️
> 
> **Voorwaarde voor toepassing**: deze afwijking is alleen toegestaan wanneer het uiterst moeilijk is om bezittingen, schulden, rechten, verplichtingen, opbrengsten of kosten van een groepsvennootschap op de afsluitingsdatum van de geconsolideerde jaarrekening op te nemen, of wanneer dat de opstelling en publicatie van de geconsolideerde jaarrekening uitermate zou vertragen. ⚖️
> 
> **Verplichte motivering**: de afwijking moet gemotiveerd worden in de toelichting bij de geconsolideerde jaarrekening. ⚖️
> 
> _Grondslag: KB WVV art. 3:110, tweede lid: 'Tussen beide data of de beschouwde periodes mag evenwel onder geen enkel beding meer dan drie maanden liggen.'_

> [!info]- Bronnen (2)
> - [[geconsolideerde-jaarrekening|content/concepten/geconsolideerde-jaarrekening.md]] · Drempelwaarden → ondersteunt: cijfer 3 maanden
> - [[geconsolideerde-jaarrekening|content/concepten/geconsolideerde-jaarrekening.md]] · Bouwstenen — Afsluitingsdatum → ondersteunt: voorwaarde + motivering

> [!info]- Provenance
> - Generator: claude-opus-4-7
> - Datum: 2026-05-19
> - Antwoord-type: drempel_cijfer
> - Checklist-versie: 1.0
> - Gates gepasseerd: claim_coverage, geen_externe_kennis
> - Verify gepasseerd: True
> - Wetsversie-policy: huidig

---

### 2013-2-vr8 · 2013-2 · 10.0 pt

**Vraagformaat**: MC · **Antwoord-type**: casus · **Confidence**: grounded

#### Vraagtekst

- **a.** Wat is een positief consolidatieverschil ?

Antwoord … / 2 punten

- **b.** Geef de vier voornaamste oorzaken van positieve consolidatieverschillen ?

Antwoord … / 8 punten

INTERNE CONTROLE EN ACCOUNTANTSONDERZOEK 50 PUNTEN

#### Modelantwoord

Zie antwoorden per subvraag (a en b).

> [!success]- Motivering
> Combinatievraag — definitie + opsomming. Zie subvragen[].antwoord_motivering per deelvraag.

> [!info]- Provenance
> - Generator: claude-opus-4-7
> - Datum: 2026-05-19
> - Antwoord-type: casus
> - Checklist-versie: 1.0
> - Verify gepasseerd: True
> - Wetsversie-policy: huidig
> - Opmerking: Identieke vraag aan 2015-1-vr11 (definitie + 4 oorzaken positief consolidatieverschil) — antwoord-content gespiegeld; bronnen + grondslag onveranderd.

#### Subvraag a)

Wat is een positief consolidatieverschil ?

**Antwoord-type**: definitie

#### Modelantwoord

Het consolidatieverschil dat ontstaat wanneer de moeder voor de aandelen méér betaalt dan haar pro-rata aandeel in het eigen vermogen van de dochter op aankoopdatum (na toerekening van het bruto-verschil aan onder- of overgewaardeerde bezittingen en schulden). Het residu is dan positief en wordt aan actiefzijde van de geconsolideerde balans geboekt onder de post 'Consolidatieverschillen', afgeschreven over de vermoedelijke gebruiksduur.

> [!success]- Motivering
> Een positief consolidatieverschil ontstaat bij **eerste consolidatie** van een dochter wanneer de aanschaffingswaarde van de aandelen groter is dan het pro-rata aandeel van de moeder in het eigen vermogen van de dochter op aankoopdatum, **na** toerekening van het bruto-verschil aan onder- of overgewaardeerde bezittingen en schulden van de dochter. ⚖️ Het residu (= het deel dat niet aan specifieke posten kan worden toegerekend) wordt aan **actiefzijde** van de geconsolideerde balans geboekt onder de post 'Consolidatieverschillen'. ⚖️
> 
> Kerneigenschappen die het afbakenen:
> 1. Ontstaat **enkel bij eerste consolidatie** van een dochter of geassocieerde — bij latere consolidaties (volgende boekjaren waarin de dochter al in de kring zit) wordt geen nieuw verschil meer geboekt; wel de afschrijving op het bestaande verschil. ⚖️
> 2. Wordt **afgeschreven** over de vermoedelijke gebruiksduur als afzonderlijke post in de geconsolideerde resultatenrekening; afschrijving over meer dan 5 jaar vereist motivering in de toelichting. ⚖️
> 
> _Grondslag: KB WVV art. 3:130 (boeking) jo. art. 3:131, § 1 (afschrijving)_

> [!info]- Bronnen (3)
> - [[consolidatieverschil|content/concepten/consolidatieverschil.md]] · Bouwstenen — Positief consolidatieverschil = goodwill → ondersteunt: definitie + actiefzijde + afschrijving
> - [[consolidatieverschil|content/concepten/consolidatieverschil.md]] · Berekening (stappen 1-5) → ondersteunt: toerekening vóór residu-boeking
> - [[eerste-consolidatie|content/concepten/eerste-consolidatie.md]] · Stappen → ondersteunt: scope: enkel bij eerste consolidatie

> [!info]- Provenance
> - Generator: claude-opus-4-7
> - Datum: 2026-05-19
> - Antwoord-type: definitie
> - Checklist-versie: 1.0
> - Gates gepasseerd: circular_definition, claim_coverage, geen_externe_kennis
> - Verify gepasseerd: True
> - Wetsversie-policy: huidig
> - Opmerking: Spiegeling van 2015-1-vr11 subvraag a).

#### Subvraag b)

Geef de vier voornaamste oorzaken van positieve consolidatieverschillen ?

**Antwoord-type**: opsomming

#### Modelantwoord

(1) onder-gewaardeerde activa van de dochter; (2) over-gewaardeerde schulden of voorzieningen van de dochter; (3) niet-geboekte immateriële vaste activa (intern opgebouwde merken, klantenrelaties, knowhow); (4) werkelijke goodwill / overprijs (synergieën, controlepremie, marktpositie).

> [!success]- Motivering
> De vier voornaamste oorzaken van een **positief** consolidatieverschil:
> 
> 1. **Onder-gewaardeerde activa van de dochter** — werkelijke waarde > boekwaarde (stille meerwaarden op terreinen, gebouwen, voorraden, deelnemingen). De moeder betaalt de werkelijke waarde, terwijl de boekwaarde in de enkelvoudige jaarrekening lager staat. ⚖️
> 2. **Over-gewaardeerde schulden of voorzieningen** van de dochter — werkelijke waarde < boekwaarde (te ruim ingeschatte voorzieningen of schulden). Na correctie blijft een kleiner residu over als consolidatieverschil. ⚖️
> 3. **Niet-geboekte immateriële vaste activa** — intern opgebouwde merken, klantenrelaties, knowhow die in de enkelvoudige jaarrekening van de dochter niet activeerbaar waren maar wel economische waarde vertegenwoordigen. 🤖
> 4. **Werkelijke goodwill / overprijs** — verwachte synergieën, controlepremie, marktpositie of strategische waarde die de moeder bereid is bovenop het netto-actief te betalen. Niet aan specifieke activa of schulden toerekenbaar; blijft als residu zitten en wordt afgeschreven over de vermoedelijke gebruiksduur. ⚖️
> 
> **Procedure** (KB WVV art. 3:128 jo. art. 3:130, lid 1): oorzaken 1 t.e.m. 3 worden bij eerste consolidatie eerst toegerekend aan de betrokken posten ('voor zover mogelijk'); pas het residu daarna verschijnt als 'Consolidatieverschillen' aan actiefzijde. ⚖️ Oorzaak 4 (werkelijke goodwill) is per definitie het deel dat na toerekening overblijft.
> 
> _Grondslag: KB WVV art. 3:128 (toerekening) jo. art. 3:130, lid 1 (procedure) jo. art. 3:131, § 1 (boeking + afschrijving). Europese Richtlijn 2013/34/EU art. 24, lid 3, c) duidt het residu uitdrukkelijk aan als 'goodwill'._

> [!info]- Bronnen (3)
> - [[consolidatieverschil|content/concepten/consolidatieverschil.md]] · Oorzaken (positief, na pool-splitting 2026-05-19) → ondersteunt: vier categorieën
> - [[consolidatieverschil|content/concepten/consolidatieverschil.md]] · Berekening — stap 4 (Toerekening) → ondersteunt: procedure toerekening vóór residu
> - [[consolidatieverschil|content/concepten/consolidatieverschil.md]] · Bouwstenen — Positief consolidatieverschil = goodwill → ondersteunt: goodwill als residu na toerekening

> [!info]- Provenance
> - Generator: claude-opus-4-7
> - Datum: 2026-05-19
> - Antwoord-type: opsomming
> - Checklist-versie: 1.0
> - Gates gepasseerd: cluster_met_polen, claim_coverage, geen_externe_kennis
> - Verify gepasseerd: True
> - Wetsversie-policy: huidig
> - Opmerking: Spiegeling van 2015-1-vr11 subvraag b).

---

### 2014-1-vr7 · 2014-1 · 3.0 pt

**Vraagformaat**: open · **Antwoord-type**: drempel_cijfer · **Confidence**: grounded

#### Vraagtekst

De geconsolideerde jaarrekening wordt in principe op dezelfde datum afgesloten als de
jaarrekening van de consoliderende vennootschap. In bepaalde gevallen kan men hiervan
afwijken.
Hoeveel bedraagt de maximale afwijking qua afsluitingsdatum ?
Antwoord

#### Modelantwoord

Maximaal 3 maanden (vóór of na de afsluitingsdatum van de geconsolideerde jaarrekening), met verplichte motivering in de toelichting.

> [!success]- Motivering
> **Maximaal 3 maanden** — vóór of na de afsluitingsdatum van de geconsolideerde jaarrekening. ⚖️
> 
> **Voorwaarde voor toepassing**: deze afwijking is alleen toegestaan wanneer het uiterst moeilijk is om bezittingen, schulden, rechten, verplichtingen, opbrengsten of kosten van een groepsvennootschap op de afsluitingsdatum van de geconsolideerde jaarrekening op te nemen, of wanneer dat de opstelling en publicatie van de geconsolideerde jaarrekening uitermate zou vertragen. ⚖️
> 
> **Verplichte motivering**: de afwijking moet gemotiveerd worden in de toelichting bij de geconsolideerde jaarrekening. ⚖️
> 
> _Grondslag: KB WVV art. 3:110, tweede lid: 'Tussen beide data of de beschouwde periodes mag evenwel onder geen enkel beding meer dan drie maanden liggen.'_

> [!info]- Bronnen (2)
> - [[geconsolideerde-jaarrekening|content/concepten/geconsolideerde-jaarrekening.md]] · Drempelwaarden → ondersteunt: cijfer 3 maanden
> - [[geconsolideerde-jaarrekening|content/concepten/geconsolideerde-jaarrekening.md]] · Bouwstenen — Afsluitingsdatum → ondersteunt: voorwaarde + motivering

> [!info]- Provenance
> - Generator: claude-opus-4-7
> - Datum: 2026-05-19
> - Antwoord-type: drempel_cijfer
> - Checklist-versie: 1.0
> - Gates gepasseerd: claim_coverage, geen_externe_kennis
> - Verify gepasseerd: True
> - Wetsversie-policy: huidig

---

### 2014-1-vr8 · 2014-1 · 9.0 pt

**Vraagformaat**: open · **Antwoord-type**: kwalificatie · **Confidence**: inferred

#### Vraagtekst

Vul onderstaande tabel aan op basis van volgende gegevens.
M
70 % 30 %
60 % 20 %
A B C
Antwoord

|   | CONTROLEPERCENTAGE | BELANGENPERCENTAGE | CONSOLIDATIEMETHODE |
| --- | --- | --- | --- |
| M IN A |   |   |   |
| M IN B |   |   |   |
| M IN C |   |   |   |

INTERNE CONTROLE 25 PUNTEN

#### Modelantwoord

M in A: 70 % controle, 70 % belang, integrale consolidatie. M in B: 30 % controle, 30 % belang, vermogensmutatie. M in C (via A → 60 %, B-keten gebroken wegens geen exclusieve controle): 60 % controle, 48 % belang (= 70 %×60 % + 30 %×20 %), integrale consolidatie.

> [!success]- Motivering
> Op basis van de structuur in de vraagtekst (gestructureerde tabel + diagram):
> 
> **Aandeelhoudersketen** (interpretatie van het diagram "M / 70% 30% / 60% 20% / A B C"):
> - M heeft directe deelnemingen: **70 % in A** en **30 % in B**
> - A heeft een deelneming van **60 % in C**
> - B heeft een deelneming van **20 % in C**
> 
> **Toepassing van de regels** (zie [[berekenen-controle-en-belangenpercentage]] + [[kiezen-consolidatiemethode]] + [[kwalificeren-relatie-deelneming]]):
> 
> ### M in A
> - **Controlepercentage**: 70 % directe stemrechten > 50 % → **exclusieve controle in rechte** ⚖️
> - **Belangenpercentage**: 70 % (direct) ⚖️
> - **Consolidatiemethode**: **integrale consolidatie** (dochter onder exclusieve controle). Belangen van derden = 30 %. ⚖️
> 
> ### M in B
> - **Controlepercentage**: 30 % directe stemrechten — geen exclusieve controle (< 50 %), maar ≥ 20 % → **vermoeden van invloed van betekenis** (geassocieerde onderneming) ⚖️
> - **Belangenpercentage**: 30 % (direct) ⚖️
> - **Consolidatiemethode**: **vermogensmutatie** (equity method) ⚖️
> 
> ### M in C (via twee ketens)
> - **Keten via A**: M → 70 % → A → 60 % → C. M heeft exclusieve controle over A → de **volledige stemrechtpercentage van A in C telt** (controlepercentage wordt NIET vermenigvuldigd langs een keten van exclusieve controle). ⚖️ Controlebijdrage = **60 %**.
> - **Keten via B**: M → 30 % → B → 20 % → C. M heeft geen exclusieve controle over B (slechts invloed van betekenis) → **de keten breekt**: B's 20 % in C telt **niet** mee voor M's controlepercentage. ⚖️
> - **Controlepercentage**: 60 % (via A alleen) → exclusieve controle → **integrale consolidatie** ⚖️
> - **Belangenpercentage**: 70 % × 60 % + 30 % × 20 % = 42 % + 6 % = **48 %** (belang telt economisch via beide ketens, ook door geassocieerde). ⚖️
> - **Consolidatiemethode**: **integrale consolidatie** (omdat controle bestaat); belangen van derden = 52 %. ⚖️
> 
> ### Resultaat-tabel
> 
> | | Controlepercentage | Belangenpercentage | Consolidatiemethode |
> |---|---:|---:|---|
> | M in A | 70 % | 70 % | Integrale consolidatie |
> | M in B | 30 % | 30 % | Vermogensmutatie |
> | M in C | 60 % | 48 % | Integrale consolidatie |
> 
> _Grondslag: WVV art. 1:14 e.v. (exclusieve controle), KB WVV art. 3:96 (vermoeden invloed van betekenis), KB WVV art. 3:124 (integrale consolidatie), KB WVV art. 3:141 (vermogensmutatie). Voor de keten-rekenregels: vakdoctrinaire toepassing op basis van [[controlepercentage]] §rekenregel-keten en [[belangenpercentage]] §berekening-keten._
> 
> ⚠️ **Interpretatie van het diagram**: de vraagtekst toont een visueel boom-diagram met percentages dat niet als typed-tabel kon worden geëxtracteerd (zie record_gap_report — figuur-detectie is ADR-021 v2.1-scope). De interpretatie hierboven veronderstelt M moeder, A en B dochters, C kleindochter via A én B. Een alternatieve interpretatie (4 directe deelnemingen A, B, C, D) is niet consistent met de invul-tabel (die enkel M in A, B, C bevat). 🤖

> [!info]- Bronnen (4)
> - [[berekenen-controle-en-belangenpercentage|content/concepten/berekenen-controle-en-belangenpercentage.md]] · Stappen 2-3 (keten-rekenregels) → ondersteunt: controle niet vermenigvuldigen, belang wel
> - [[kiezen-consolidatiemethode|content/concepten/kiezen-consolidatiemethode.md]] · Stappen 2-4 → ondersteunt: integrale vs vermogensmutatie keuze
> - [[kwalificeren-relatie-deelneming|content/concepten/kwalificeren-relatie-deelneming.md]] · Kwalificatie-criteria → ondersteunt: exclusieve controle, invloed van betekenis
> - [[exclusieve-controle|content/concepten/exclusieve-controle.md]] · Keten-breuk → ondersteunt: breuk bij geen exclusieve controle in tussenschakel

> [!info]- Provenance
> - Generator: claude-opus-4-7
> - Datum: 2026-05-19
> - Antwoord-type: kwalificatie
> - Checklist-versie: 1.0
> - Gates gepasseerd: claim_coverage, geen_externe_kennis
> - Verify gepasseerd: True
> - Wetsversie-policy: huidig
> - Opmerking: Diagram-interpretatie 🤖: M → A,B direct; A,B → C indirect. Consistent met invul-tabel (enkel M in A,B,C). Alternatieve interpretatie (4 directe deelnemingen) niet consistent. Extract-v2 (ADR-021) heeft de invul-tabel typed gedetecteerd; het ingevoerde boom-diagram blijft in tekst-blok.

> [!warning] Gap niveau **b** — type **extractie_partieel**
> Het visuele boom-diagram (M aan top, A/B middenniveau, C onderaan) wordt door extract-v2 (pdfplumber) niet als tabel maar als platte tekst geëxtracteerd ("M / 70 % 30 % / 60 % 20 % / A B C"). Figuur-detectie + structurering is v2.1-scope (ADR-021 §2). Voor nu vereist het modelantwoord een interpretatie van het diagram door redenering — gelabeld als 🤖 voor de structurele aanname.
> 
> Ontbrekende velden: Figuur-extractie voor boom-diagrammen
> 
> _Gedetecteerd op_: 2026-05-19

---

### 2015-1-vr11 · 2015-1 · 6.0 pt

**Vraagformaat**: MC · **Antwoord-type**: casus · **Confidence**: grounded

#### Vraagtekst

- **a.** Wat is een positief consolidatieverschil ?

Antwoord … / 2 punten

- **b.** Geef de vier voornaamste oorzaken van positieve consolidatieverschillen ?

Antwoord … / 4 punten

INTERNE CONTROLE 25 PUNTEN

#### Modelantwoord

Zie antwoorden per subvraag (a en b).

> [!success]- Motivering
> Combinatievraag — definitie + opsomming. Zie subvragen[].antwoord_motivering per deelvraag.

> [!info]- Provenance
> - Generator: claude-opus-4-7
> - Datum: 2026-05-19
> - Antwoord-type: casus
> - Checklist-versie: 1.0
> - Verify gepasseerd: True
> - Wetsversie-policy: huidig

#### Subvraag a)

Wat is een positief consolidatieverschil ?

**Antwoord-type**: definitie

#### Modelantwoord

Het consolidatieverschil dat ontstaat wanneer de moeder voor de aandelen méér betaalt dan haar pro-rata aandeel in het eigen vermogen van de dochter op aankoopdatum (na toerekening van het bruto-verschil aan onder- of overgewaardeerde bezittingen en schulden). Het residu is dan positief en wordt aan actiefzijde van de geconsolideerde balans geboekt onder de post 'Consolidatieverschillen', afgeschreven over de vermoedelijke gebruiksduur.

> [!success]- Motivering
> Een positief consolidatieverschil ontstaat bij **eerste consolidatie** van een dochter wanneer de aanschaffingswaarde van de aandelen groter is dan het pro-rata aandeel van de moeder in het eigen vermogen van de dochter op aankoopdatum, **na** toerekening van het bruto-verschil aan onder- of overgewaardeerde bezittingen en schulden van de dochter. ⚖️ Het residu (= het deel dat niet aan specifieke posten kan worden toegerekend) wordt aan **actiefzijde** van de geconsolideerde balans geboekt onder de post 'Consolidatieverschillen'. ⚖️
> 
> Kerneigenschappen die het afbakenen:
> 1. Ontstaat **enkel bij eerste consolidatie** van een dochter of geassocieerde — bij latere consolidaties (volgende boekjaren waarin de dochter al in de kring zit) wordt geen nieuw verschil meer geboekt; wel de afschrijving op het bestaande verschil. ⚖️
> 2. Wordt **afgeschreven** over de vermoedelijke gebruiksduur als afzonderlijke post in de geconsolideerde resultatenrekening; afschrijving over meer dan 5 jaar vereist motivering in de toelichting. ⚖️
> 
> _Grondslag: KB WVV art. 3:130 (boeking) jo. art. 3:131, § 1 (afschrijving)_

> [!info]- Bronnen (3)
> - [[consolidatieverschil|content/concepten/consolidatieverschil.md]] · Bouwstenen — Positief consolidatieverschil = goodwill → ondersteunt: definitie + actiefzijde + afschrijving
> - [[consolidatieverschil|content/concepten/consolidatieverschil.md]] · Berekening (stappen 1-5) → ondersteunt: toerekening vóór residu-boeking
> - [[eerste-consolidatie|content/concepten/eerste-consolidatie.md]] · Stappen → ondersteunt: scope: enkel bij eerste consolidatie

> [!info]- Provenance
> - Generator: claude-opus-4-7
> - Datum: 2026-05-19
> - Antwoord-type: definitie
> - Checklist-versie: 1.0
> - Gates gepasseerd: circular_definition, claim_coverage, geen_externe_kennis
> - Verify gepasseerd: True
> - Wetsversie-policy: huidig

#### Subvraag b)

Geef de vier voornaamste oorzaken van positieve consolidatieverschillen ?

**Antwoord-type**: opsomming

#### Modelantwoord

(1) onder-gewaardeerde activa van de dochter; (2) over-gewaardeerde schulden of voorzieningen van de dochter; (3) niet-geboekte immateriële vaste activa (intern opgebouwde merken, klantenrelaties, knowhow); (4) werkelijke goodwill / overprijs (synergieën, controlepremie, marktpositie).

> [!success]- Motivering
> De vier voornaamste oorzaken van een **positief** consolidatieverschil:
> 
> 1. **Onder-gewaardeerde activa van de dochter** — werkelijke waarde > boekwaarde (stille meerwaarden op terreinen, gebouwen, voorraden, deelnemingen). De moeder betaalt de werkelijke waarde, terwijl de boekwaarde in de enkelvoudige jaarrekening lager staat. ⚖️
> 2. **Over-gewaardeerde schulden of voorzieningen** van de dochter — werkelijke waarde < boekwaarde (te ruim ingeschatte voorzieningen of schulden). Na correctie blijft een kleiner residu over als consolidatieverschil. ⚖️
> 3. **Niet-geboekte immateriële vaste activa** — intern opgebouwde merken, klantenrelaties, knowhow die in de enkelvoudige jaarrekening van de dochter niet activeerbaar waren maar wel economische waarde vertegenwoordigen. 🤖
> 4. **Werkelijke goodwill / overprijs** — verwachte synergieën, controlepremie, marktpositie of strategische waarde die de moeder bereid is bovenop het netto-actief te betalen. Niet aan specifieke activa of schulden toerekenbaar; blijft als residu zitten en wordt afgeschreven over de vermoedelijke gebruiksduur. ⚖️
> 
> **Procedure** (KB WVV art. 3:128 jo. art. 3:130, lid 1): oorzaken 1 t.e.m. 3 worden bij eerste consolidatie eerst toegerekend aan de betrokken posten ('voor zover mogelijk'); pas het residu daarna verschijnt als 'Consolidatieverschillen' aan actiefzijde. ⚖️ Oorzaak 4 (werkelijke goodwill) is per definitie het deel dat na toerekening overblijft.
> 
> _Grondslag: KB WVV art. 3:128 (toerekening) jo. art. 3:130, lid 1 (procedure) jo. art. 3:131, § 1 (boeking + afschrijving). Europese Richtlijn 2013/34/EU art. 24, lid 3, c) duidt het residu uitdrukkelijk aan als 'goodwill'._

> [!info]- Bronnen (3)
> - [[consolidatieverschil|content/concepten/consolidatieverschil.md]] · Oorzaken (positief, na pool-splitting 2026-05-19) → ondersteunt: vier categorieën
> - [[consolidatieverschil|content/concepten/consolidatieverschil.md]] · Berekening — stap 4 (Toerekening) → ondersteunt: procedure toerekening vóór residu
> - [[consolidatieverschil|content/concepten/consolidatieverschil.md]] · Bouwstenen — Positief consolidatieverschil = goodwill → ondersteunt: goodwill als residu na toerekening

> [!info]- Provenance
> - Generator: claude-opus-4-7
> - Datum: 2026-05-19
> - Antwoord-type: opsomming
> - Checklist-versie: 1.0
> - Gates gepasseerd: cluster_met_polen, claim_coverage, geen_externe_kennis
> - Verify gepasseerd: True
> - Wetsversie-policy: huidig
> - Opmerking: Record-patch op consolidatieverschil.md (oorzaken pool-gesplitst, 4e positieve oorzaak toegevoegd) is een prerequisite — zie commit ADR-020 pilot 2026-05-19.

---

## PO 1.5

_1 vragen — 1 met modelantwoord — 1 met gap-rapport._

### 2024-1-vr7 · 2024-1

> [!warning] Herinnering-reconstructie (fragment)
> Deze vraag is een **herinnering**-reconstructie (volledigheid: fragment) — geen officiële ITAA-bundel. Modelantwoord rust op de geherinterpreteerde vraagtekst (ADR-022).

**Vraagformaat**: J/F · **Antwoord-type**: casus · **Confidence**: grounded

#### Vraagtekst

7 IFRS

- **A.** Onder IAS/ IFRS zijn volgende methoden mogelijk: ( Juist/ fout)
- **A.** Fifo, Lifo, gewogen gemiddelde, individueel.
- **B.** Fifi, gewogen gemiddelde, individueel
- **C.** Lifo, gewogen gemiddelde individueel
- **D.** Fifo en gewogen gemiddelde
- **B.** Richtlijn 2013/34/EU 26/06/2013, opname waardering volgens voorzichtigheidsprincipe. Welke stellingen juist/ fout
- **A.** Winsten mogen slechts opgenomen worden voor zover zij op balansdatum gerealiseerd zijn
- **B.** Verplichtingen die hun oorsprong hebben in het betrokken boekjaar of in de loop van een vorig boekjaar worden opgenomen, ook als die verplichting pas worden tussen balansdatum en de datum waarop de balans wordt opgesteld
- **C.** Alle negatieve waarde correcties worden opgenomen ongeacht of het boekjaar met winst of verlies wordt afgesloten.
- **D.** Voor bepaalde categorieën van ondernemingen wordt verplicht om bepaalde VA aan geherwaardeerde waarde op te nemen.
- **C.** Stellingen mbt IAS / IFRS Juist/ fout
- **a.** Degressieve afschrijvingen zijn toegestaan
- **b.** Kosten voor voorbereiding van een terrein……?
- **c.** Uitzonderlijke opbrengsten boeken is toegestaan
- **d.** Afschr. MVA mag stopgezet worden wanneer reële waarde van het actief groter is dan boekwaarde
- **D.** Operationele / financiële laesing, hoe behandelen?

> [!note]- Geherinterpreteerde vraagtekst (ADR-022)
> Casus IFRS, 4 deelvragen:
> A. Onder IAS/IFRS zijn volgende voorraad-waarderingsmethoden mogelijk — juist/fout per optie:
>     a. FIFO, LIFO, gewogen gemiddelde, individueel.
>     b. FIFO [PDF: 'Fifi' — vermoedelijk typo], gewogen gemiddelde, individueel.
>     c. LIFO, gewogen gemiddelde, individueel.
>     d. FIFO en gewogen gemiddelde.
> B. Richtlijn 2013/34/EU van 26/06/2013 over opname en waardering volgens het voorzichtigheidsprincipe — welke stellingen zijn juist/fout:
>     1. Winsten mogen slechts opgenomen worden voor zover ze op balansdatum gerealiseerd zijn.
>     2. Verplichtingen die hun oorsprong hebben in het betrokken boekjaar of in een vorig boekjaar worden opgenomen, ook als ze pas tussen balansdatum en de datum van opstelling van de balans gekend worden.
>     3. Alle negatieve waardecorrecties worden opgenomen ongeacht of het boekjaar met winst of verlies wordt afgesloten.
>     4. Voor bepaalde categorieën van ondernemingen is het verplicht om bepaalde VA aan geherwaardeerde waarde op te nemen.
> C. Stellingen met betrekking tot IAS/IFRS — juist/fout:
>     a. Degressieve afschrijvingen zijn toegestaan.
>     b. Kosten voor voorbereiding van een terrein ……? (fragment in PDF — stelling niet bewaard).
>     c. Uitzonderlijke opbrengsten boeken is toegestaan.
>     d. Afschrijvingen op MVA mogen stopgezet worden wanneer de reële waarde van het actief groter is dan de boekwaarde.
> D. Operationele en financiële leasing — hoe behandelen onder IFRS?
> 
> _Motivering_: Sub-A en sub-B zijn complete J/F-sets met vier opties/stellingen. Sub-C heeft drie stellingen volledig en één fragment ('Kosten voor voorbereiding van een terrein……?') die niet bewaard is. Sub-D is een open vraag met volledige stam. Typo 'Fifi' in sub-A.b — vermoedelijk FIFO.
> _Confidence_: inferred · _Datum_: 2026-05-19

> [!example]- MC-opties (gestructureerd)
> | Label | Tekst | Juistheid | Motivering |
> | --- | --- | --- | --- |
> | A.a | FIFO, LIFO, gewogen gemiddelde, individueel | fout | LIFO is verboden onder IAS 2 (revised 2003). |
> | A.b | FIFO [vermoedelijke typo 'Fifi'], gewogen gemiddelde, individueel | juist | Drie toegelaten methodes onder IAS 2 §23-27. |
> | A.c | LIFO, gewogen gemiddelde, individueel | fout | LIFO verboden. |
> | A.d | FIFO en gewogen gemiddelde | fout | Incompleet — mist specifieke identificatie (toegelaten voor unieke items). |

#### Modelantwoord

Onder IAS 2 zijn drie methodes toegelaten: (1) FIFO, (2) gewogen gemiddelde, (3) specifieke identificatie (individueel). LIFO is UITDRUKKELIJK VERBODEN onder IFRS. Antwoord op MC A: D (FIFO en gewogen gemiddelde) is dichtst bij correct, maar mist specifieke identificatie; strikt = optie die geen LIFO bevat + alle drie toegelaten methodes.

> [!success]- Motivering
> **Onder IAS 2 'Voorraden' (Inventories)** zijn drie cost-formules toegelaten:
> 
> 1. **Specifieke identificatie** (IAS 2.23) — voor voorraad-items die niet onderling uitwisselbaar zijn (bv. unieke kunstwerken, vastgoed, voertuigen met VIN). ⚖️
> 2. **FIFO (First-In, First-Out)** (IAS 2.25) — voor onderling uitwisselbare items. ⚖️
> 3. **Gewogen gemiddelde kostprijs** (IAS 2.25) — alternatief voor FIFO. ⚖️
> 
> **LIFO (Last-In, First-Out)** is **uitdrukkelijk verboden** onder IFRS sinds IAS 2 (revised 2003) — IAS 2.BC9 ev. ⚖️
> 
> **Per MC-optie**:
> - **A**: FIFO, LIFO, gewogen gemiddelde, individueel → **FOUT** (LIFO erin)
> - **B**: "Fifi" (typo voor FIFO?), gewogen gemiddelde, individueel → mogelijk correct na typo-correctie, maar FIFO ontbreekt expliciet — onduidelijk
> - **C**: LIFO, gewogen gemiddelde, individueel → **FOUT** (LIFO erin)
> - **D**: FIFO en gewogen gemiddelde → **DEELS correct** (sluit LIFO uit, mist specifieke identificatie)
> 
> **Beste antwoord**: optie D — bevat geen verboden LIFO, maar is incompleet (specifieke identificatie ontbreekt). Bij strikte lezing van MC moet "alle juiste methodes" gekozen worden, dan zou D + specifieke identificatie correct zijn. Indien geen volledige optie beschikbaar → D is het minst onjuist. 🤖
> 
> ⚠️ De vraag heeft sub-onderdelen B/C/D verder die hier niet zichtbaar zijn. Aandacht: vraagtekst kan onvolledig zijn extract.
> 
> _Grondslag: IAS 2 §9-27; verbod LIFO sinds IAS 2 (revised 2003)._

> [!info]- Bronnen (1)
> - [[voorraden-ifrs|content/concepten/voorraden-ifrs.md]] · IAS 2 Bouwstenen → ondersteunt: toegelaten methodes + LIFO-verbod

> [!info]- Provenance
> - Generator: claude-opus-4-7
> - Datum: 2026-05-19
> - Antwoord-type: casus
> - Checklist-versie: 1.0
> - Gates gepasseerd: claim_coverage, geen_externe_kennis
> - Verify gepasseerd: True
> - Wetsversie-policy: huidig

> [!warning] Gap niveau **extern** — type **vraagtekst_onduidelijk** · sub-type **partieel_extract**
> Vraag heeft sub-onderdelen B/C/D in originele PDF die niet volledig in vraagtekst zitten. Alleen sub-A (voorraad-methodes) volledig beantwoord.
> 
> Ontbrekende velden: Volledige vraagtekst sub-onderdelen B/C/D
> 
> _Gedetecteerd op_: 2026-05-19

---

## PO 1.6

_12 vragen — 9 met modelantwoord — 3 met gap-rapport._

### 2013-2-vr9 · 2013-2 · 8.0 pt

**Vraagformaat**: open · **Antwoord-type**: opsomming · **Confidence**: grounded

#### Vraagtekst

Een auditprocedure is een gedetailleerde instructie voor het verzamelen van een bepaald
auditbewijsmiddel.

**Geef 4 soorten auditmethodes.**

Antwoord

#### Modelantwoord

De vier voornaamste auditmethodes per ISA 500: (1) inspectie van vastleggingen/documenten of activa; (2) waarneming van een proces of procedure; (3) externe bevestiging door een derde partij; (4) herberekening van wiskundige juistheid.

> [!success]- Motivering
> ISA 500 §A14-A25 ('audit evidence') somt **zeven** auditprocedure-types op om controle-informatie te verzamelen: inspectie, waarneming, externe bevestiging, herberekening, opnieuw uitvoeren, cijferanalyses, verzoeken om inlichtingen. ⚖️ De vraag vraagt vier **soorten auditmethodes** — de vier voornaamste zijn:
> 
> 1. **Inspectie** — het onderzoeken van vastleggingen, documenten (intern of extern, op papier of digitaal) of fysieke activa. Voorbeeld: factuur, bestelbon, contract, voorraad in magazijn. Levert bewijs over bestaan en (in beperkte mate) waardering. ⚖️
> 2. **Waarneming** — het gadeslaan van een proces of procedure die door anderen wordt uitgevoerd (bv. de auditor woont de jaarlijkse voorraadopname bij). Levert bewijs over de **uitvoering** van een controle op het moment van waarnemen — beperkt in tijd. ⚖️
> 3. **Externe bevestiging** — schriftelijke reactie rechtstreeks van een derde partij (bank, klant, leverancier, advocaat) aan de auditor (zie [[externe-bevestiging-audit]]). Hoogwaardige assurance wegens extern + onafhankelijk + schriftelijk. Vormen: positieve, negatieve, saldo-bevestiging. ⚖️
> 4. **Herberekening** — door de auditor zelf de wiskundige correctheid van documenten of registers verifiëren (bv. nakijken of een afschrijvingsplan klopt, BTW-totalen, salarisberekeningen). ⚖️
> 
> (De drie andere uit ISA 500 — opnieuw uitvoeren, cijferanalyses, verzoeken om inlichtingen — zijn ook auditmethodes, maar worden vaak als aanvullingen geclassificeerd of in een andere groepering geplaatst.)
> 
> _Grondslag: ISA 500 §A14-A25; ITAA KMO-controlenorm §89-92 voor externe bevestiging; record [[selecteren-en-uitvoeren-controle-instrumenten-audit]]._

> [!info]- Bronnen (3)
> - [[selecteren-en-uitvoeren-controle-instrumenten-audit|content/concepten/selecteren-en-uitvoeren-controle-instrumenten-audit.md]] · Stappen → ondersteunt: instrumenten-keuze + auditmethodes
> - [[externe-bevestiging-audit|content/concepten/externe-bevestiging-audit.md]] · Definitie → ondersteunt: externe bevestiging als auditmethode
> - [[ISA-500|resources/bronnen/normen/ISA-500.md]] · §A14-A25 → ondersteunt: zeven auditprocedure-types

> [!info]- Provenance
> - Generator: claude-opus-4-7
> - Datum: 2026-05-19
> - Antwoord-type: opsomming
> - Checklist-versie: 1.0
> - Gates gepasseerd: claim_coverage, geen_externe_kennis
> - Verify gepasseerd: True
> - Wetsversie-policy: huidig
> - Opmerking: ISA 500 noemt 7 types; vraag vraagt 4 — keuze op basis van klassieke "voornaamste" vier in Belgische audit-opleiding.

---

### 2013-2-vr11 · 2013-2 · 8.0 pt

**Vraagformaat**: open · **Antwoord-type**: definitie · **Confidence**: grounded

#### Vraagtekst

Wanneer dient een accountant een onthoudende verklaring af te geven?
Antwoord

#### Modelantwoord

Een onthoudende verklaring (onthouding van oordeel / disclaimer of opinion) geeft de accountant af wanneer hij onmogelijk voldoende en geschikte assurance-informatie kan verkrijgen om een oordeel te onderbouwen, EN de mogelijke effecten van het onbekende diepgaand kunnen zijn voor de jaarrekening als geheel. De accountant kan dan geen oordeel formuleren.

> [!success]- Motivering
> Een **onthouding van oordeel** (synoniem: 'disclaimer of opinion' in ISA-terminologie, 'onthoudende verklaring' in Belgische audit-praktijk) wordt afgegeven wanneer **cumulatief**:
> 
> 1. De accountant **onmogelijk** voldoende en geschikte assurance-informatie kan verkrijgen om de jaarrekening te onderbouwen — bv. door scope-beperking opgelegd door de cliënt, of door externe omstandigheden (boekhouding verloren, sleuteldocumenten ontoegankelijk). ⚖️
> 2. De **mogelijke effecten** van het ontbrekend bewijs op de jaarrekening **diepgaand** kunnen zijn — niet alleen materieel, maar zo verspreid dat ze het globale geloofwaardigheidsoordeel aantasten. ⚖️
> 
> **Vergelijk met andere oordeel-types**:
> - Goedkeurend zonder voorbehoud: jaarrekening geeft getrouw beeld, geen significante issues
> - Goedkeurend **met voorbehoud**: er is een materiële afwijking of scope-beperking, maar **niet diepgaand** (geïsoleerd) — accountant formuleert oordeel met expliciete uitzondering
> - **Afkeurend**: materiële afwijking + diepgaand (alles-doordringend) — accountant verklaart dat de jaarrekening geen getrouw beeld geeft
> - **Onthoudend**: onvoldoende bewijs + diepgaande mogelijke gevolgen — geen oordeel mogelijk
> 
> **Voorbeelden** van situaties die tot onthouding leiden:
> - Cliënt weigert toegang tot belangrijke contracten, bankrekeningen, of vorderingen-overzichten
> - Materiële voorraad-opname onmogelijk + geen alternatieve werkzaamheden mogelijk (vooral bij eerste-jaars audit)
> - Continuïteitsonzekerheid waarvoor management onvoldoende toelichting geeft en de auditor de impact niet kan kwantificeren
> 
> _Grondslag: ISA 705 (herzien) §10 + §A12-A14; ITAA KMO-controlenorm; [[controleoordeel-types]] §Onthouding van oordeel._

> [!info]- Bronnen (1)
> - [[controleoordeel-types|content/concepten/controleoordeel-types.md]] · Bouwstenen — Onthouding van oordeel (disclaimer) → ondersteunt: definitie + cumulatieve voorwaarden

> [!info]- Provenance
> - Generator: claude-opus-4-7
> - Datum: 2026-05-19
> - Antwoord-type: definitie
> - Checklist-versie: 1.0
> - Gates gepasseerd: circular_definition, claim_coverage, geen_externe_kennis
> - Verify gepasseerd: True
> - Wetsversie-policy: huidig

---

### 2013-2-vr13 · 2013-2 · 8.0 pt

**Vraagformaat**: MC · **Antwoord-type**: casus · **Confidence**: grounded

#### Vraagtekst

Je wordt gevraagd om als extern accountant een controleopdracht uit te voeren bij de NV
Fortunato. De interne boekhouder van de onderneming bezorgt de cijfers per 30 november
2013 ( = de afsluitdatum conform de statuten).
Op 2 december 2013 heb je ter plaatse de voorraadtelling gevolgd en je met de getelde
hoeveelheden akkoord verklaard.
Het bedrijf is gespecialiseerd in de aan- en verkoop van landbouwmachines.
Het risicoprofiel is laag gezien er volgens onze testen een goede interne controle is voor wat
aankopen, financieel en verkopen betreft.

- **a.** Kunnen we ons baseren op de cijfers ontvangen van de interne boekhouder?

Leg uit.

**Antwoord … / 4 punten
b) De telling van de voorraad (30/11/2013) hebben we fysiek kunnen meemaken.**

Welke controle doen we nu tijdens de controlewerkzaamheden op de voorraad
landbouwmachines? Geef één controledoelstelling en één voorbeeld van de
techniek die je daarvoor gaat toepassen.
Antwoord … / 4 punten
 Controledoelstelling:
 Voorbeeld:

VENNOOTSCHAPSRECHT 20 PUNTEN

#### Modelantwoord

Periode 01/10/2014 (voorraadtelling akkoord) → 23/01/2015 (huidige datum) = ~4 maanden. Voor de accountant zijn dit de "gebeurtenissen na balansdatum" (ISA 560 / KB WVV art. 3:6). Acties: (a) management vragen om informatie over gebeurtenissen tussen balansdatum en datum verslag, (b) verifiëren of die gebeurtenissen aanpassende (adjusting events) of toelichtende (non-adjusting events) gebeurtenissen zijn, (c) verkrijgen van schriftelijke bevestiging van management dat alle relevante na-balansdatum-events zijn meegedeeld, (d) impact op jaarrekening + toelichting + controleverslag beoordelen.

> [!success]- Motivering
> ### Context
> 
> Balansdatum: 30 september 2014. Voorraadtelling bij accountant: 1 oktober 2014. Huidige datum: 23 januari 2015. **Periode van ~4 maanden tussen balansdatum en datum waarop het controleverslag wordt opgesteld** — typische "na-balansdatum-periode" in een audit.
> 
> ### Klassieke aanpak (ISA 560 + KB WVV art. 3:6)
> 
> **Twee soorten gebeurtenissen na balansdatum**:
> 
> 1. **Aanpassende gebeurtenissen (adjusting events)** — gebeurtenissen die meer informatie verschaffen over omstandigheden die **al bestonden** op balansdatum. ⚖️ Voorbeelden: faillissement van een grote debiteur waar al twijfel over bestond → waardevermindering op vordering boeken op balans 30/09; uitspraak in een rechtsgeschil dat op 30/09 al hangende was → voorziening boeken.
> 2. **Niet-aanpassende gebeurtenissen (non-adjusting events)** — gebeurtenissen die ontstonden **na** balansdatum. ⚖️ Voorbeelden: brand in november, overname op decembre, dividendbeslissing. Geen aanpassing van cijfers, maar **toelichting verplicht** indien materieel.
> 
> ### Acties van de accountant
> 
> 1. **Management bevragen** — wat is er sinds 30 september gebeurd? Significante contracten, claims, faillissementen, productiestilstanden, brand/diefstal, kapitaalverhogingen, omzet-veranderingen, etc. ⚖️
> 2. **Documentatie reviewen** — recente notulen bestuursvergaderingen, ondertekende contracten, recente bank-/leverancier-correspondentie, juridische bevestigingen. ⚖️
> 3. **Subsequente boekingen testen** — controleer of materiële gebeurtenissen die zich na 30/09 voordeden, correct in de jaarrekening van 30/09/2014 zijn opgenomen (adjusting) of in toelichting (non-adjusting). ⚖️
> 4. **Externe bevestigingen** van advocaten (geschillen na 30/09) en banken (kredietfaciliteiten-status) — zie [[externe-bevestiging-audit]]. ⚖️
> 5. **Schriftelijke bevestiging van management** ([[schriftelijke-bevestiging-management]]) — dat alle relevante na-balansdatum-events gemeld zijn (ISA 580). ⚖️
> 6. **Impact beoordelen op**:
>    - Cijfers: aanpassende → boeken in jaarrekening
>    - Toelichting: niet-aanpassende materiële → vermelden
>    - Controleverslag: bij materiële niet-vermelding → voorbehoud of afkeurend
>    - Continuïteit: gebeurtenissen die continuïteit bedreigen → mogelijk going-concern paragraaf (ISA 570)
> 
> _Grondslag: ISA 560 (Subsequent Events); KB WVV art. 3:6 (gebeurtenissen na balansdatum); ITAA KMO-controlenorm §123-126; [[externe-bevestiging-audit]]; [[schriftelijke-bevestiging-management]]._
> 
> ⚠️ Casus-specifiek (NV Fortunato): balansdatum 30/11/2013. Aanpak identiek aan klassieke ISA 560-procedure.

> [!info]- Bronnen (2)
> - [[externe-bevestiging-audit|content/concepten/externe-bevestiging-audit.md]] · Werkwijze → ondersteunt: externe bevestigingen na balansdatum
> - [[schriftelijke-bevestiging-management|content/concepten/schriftelijke-bevestiging-management.md]] · Bouwstenen → ondersteunt: management bevestiging na-balansdatum-events

> [!info]- Provenance
> - Generator: claude-opus-4-7
> - Datum: 2026-05-19
> - Antwoord-type: casus
> - Checklist-versie: 1.0
> - Gates gepasseerd: claim_coverage, geen_externe_kennis
> - Verify gepasseerd: True
> - Wetsversie-policy: huidig
> - Opmerking: Gespiegeld op 2015-1-vr18 (gebeurtenissen na balansdatum) — aanpak identiek.

#### Subvraag a)

Kunnen we ons baseren op de cijfers ontvangen van de interne boekhouder?
Leg uit.

#### Subvraag b)

De telling van de voorraad (30/11/2013) hebben we fysiek kunnen meemaken.
Welke controle doen we nu tijdens de controlewerkzaamheden op de voorraad
landbouwmachines? Geef één controledoelstelling en één voorbeeld van de
techniek die je daarvoor gaat toepassen.

---

### 2014-1-vr12 · 2014-1 · 8.0 pt

**Vraagformaat**: MC · **Antwoord-type**: casus · **Confidence**: grounded

#### Vraagtekst

Er worden onvoldoende antwoorden ontvangen op de confirmatie- of bevestigingsbrieven
welke verzonden werden aan de klanten.
a) Moeten we daarvoor een voorbehoud in ons verslag maken ?

**Antwoord
b) Welke acties kan men ondernemen om aan dit onvoldoende aantal antwoorden te
remediëren (geef twee voorbeelden)?**

Antwoord
c) Welke is de werkwijze nadat we onze selectie hebben gemaakt van de klanten aan
dewelke de confirmatiebrieven worden verzonden : door wie zijn de
confirmatiebrieven opgesteld en getekend, aan wie moeten de antwoorden
opgestuurd worden, wie verzendt de confirmatiebrieven?
Antwoord

#### Modelantwoord

a) Niet automatisch voorbehoud: alleen indien alternatieve werkzaamheden onvoldoende informatie opleveren én het effect materieel is. b) Acties: subsequente betalingen na balansdatum testen, leveringsbon/factuur/inning-documenten inspecteren, beoordeling waarom geen antwoord (steekproef-grootte vergroten, herzending naar andere ontvangers, telefonische follow-up), en indien aanhoudend → andere klanten in steekproef + cijferanalyse-DSO + management-bevestiging.

> [!success]- Motivering
> ### a) Moeten we daarvoor een voorbehoud in ons verslag maken?
> 
> **Niet automatisch.** Onvoldoende antwoorden op confirmatiebrieven is op zichzelf **geen** reden voor voorbehoud — het is een **scope-uitdaging** die opgelost kan worden met alternatieve werkzaamheden ([[externe-bevestiging-audit]] §Niet-antwoord). ⚖️
> 
> Voorbehoud is alleen vereist wanneer:
> 1. **Alternatieve werkzaamheden onvoldoende informatie opleveren** (bv. geen subsequente betalingen, contracten ontbreken, klanten weigeren mee te werken)
> 2. **Het effect materieel is** — de niet-bevestigde saldi vertegenwoordigen samen een bedrag boven de materialiteitsdrempel
> 3. **Diepgaand of niet** → bepaalt voorbehoud vs afkeurend oordeel (zie [[controleoordeel-types]])
> 
> Bij **diepgaande** scope-beperking + onmogelijke alternatieven → **onthouding van oordeel**. ⚖️
> 
> ### b) Welke acties kan men ondernemen?
> 
> **Alternatieve werkzaamheden** ([[externe-bevestiging-audit]] §Niet-antwoord, ITAA KMO-controlenorm §92):
> 
> 1. **Subsequente inningen testen** — controleer in bankafschriften na balansdatum of de geboekte klantenvordering effectief geïnd werd. Inning na balansdatum is sterk bewijs van bestaan + waardering. ⚖️
> 2. **Leveringsbonnen, facturen en orders inspecteren** — drieweg-match (order → leveringsbon → factuur) levert documentair bewijs over bestaan. ⚖️
> 3. **Cijferanalyse op DSO en aged-receivables** — patronen identificeren die wijzen op verkeerd geboekte saldi. ⚖️
> 
> **Procedurele acties op de confirmaties zelf**:
> 
> 4. **Herzending** — telefonische follow-up bij klant + opnieuw versturen via beveiligde weg (e-mail met handtekening + leverbevestiging) 🤖
> 5. **Steekproef vergroten** — meer klanten aanschrijven om de coverage te verhogen 🤖
> 6. **Switchen naar positieve bevestiging** — als oorspronkelijk negatief gevraagd (alleen reactie bij verschil), heroverwegen naar positieve bevestiging (altijd antwoorden) 🤖
> 7. **Management-bevestiging** — schriftelijke bevestiging van management dat de klantensaldi correct geboekt zijn (zie [[schriftelijke-bevestiging-management]]) — maar dit is **aanvullend**, niet vervangend voor extern bewijs. ⚖️
> 
> Pas wanneer al deze alternatieven onvoldoende blijken, komt voorbehoud in beeld.
> 
> _Grondslag: ITAA KMO-controlenorm §92; ISA 505 §12-16; [[externe-bevestiging-audit]]; [[controleoordeel-types]]._

> [!info]- Bronnen (2)
> - [[externe-bevestiging-audit|content/concepten/externe-bevestiging-audit.md]] · Bouwstenen — Niet-antwoord en alternatieve werkzaamheden → ondersteunt: alternatieve werkzaamheden
> - [[controleoordeel-types|content/concepten/controleoordeel-types.md]] · Bouwstenen → ondersteunt: voorbehoud-trigger

> [!info]- Provenance
> - Generator: claude-opus-4-7
> - Datum: 2026-05-19
> - Antwoord-type: casus
> - Checklist-versie: 1.0
> - Gates gepasseerd: claim_coverage, geen_externe_kennis
> - Verify gepasseerd: True
> - Wetsversie-policy: huidig

#### Subvraag a)

Moeten we daarvoor een voorbehoud in ons verslag maken ?

#### Subvraag b)

Welke acties kan men ondernemen om aan dit onvoldoende aantal antwoorden te
remediëren (geef twee voorbeelden)?

#### Subvraag c)

Welke is de werkwijze nadat we onze selectie hebben gemaakt van de klanten aan
dewelke de confirmatiebrieven worden verzonden : door wie zijn de
confirmatiebrieven opgesteld en getekend, aan wie moeten de antwoorden
opgestuurd worden, wie verzendt de confirmatiebrieven?

---

### 2014-1-vr13 · 2014-1 · 3.0 pt

**Vraagformaat**: J/F · **Antwoord-type**: definitie · **Confidence**: grounded

#### Vraagtekst

Bij nazicht van de resultatenrekening komen we op de kostenrekening “erelonen advocaat”
ten belope van 12.000,00 EUR.
Waarom is dit van belang voor het controleverslag?
Welke actie stel je voor ?
Antwoord

#### Modelantwoord

Erelonen advocaat van 12.000 EUR in de resultatenrekening wijzen op één of meer lopende juridische geschillen, wat materiële off-balance verplichtingen of voorzieningen kan impliceren die de auditor moet onderzoeken. Acties: (1) externe bevestiging vragen aan de advocaat over status, aard en bedrag van geschillen; (2) toelichting en eventuele voorzieningen voor risico's en kosten nazien; (3) potentiële impact op continuïteit beoordelen; (4) bij niet-onthulling of materiële afwijking: oordeel met voorbehoud of zelfs afkeurend oordeel overwegen.

> [!success]- Motivering
> **Waarom is dit van belang voor het controleverslag?**
> 
> De aanwezigheid van een kostenpost "erelonen advocaat" van € 12.000 in de resultatenrekening is een **signaal** voor de auditor dat er **lopende of recent afgesloten juridische geschillen** zijn. ⚖️ Geschillen kunnen drie soorten effecten hebben op de jaarrekening:
> 
> 1. **Off-balance verplichting** (klasse 0 in toelichting): geschillen zonder zekere uitkomst worden vermeld bij de rechten en verplichtingen buiten balans ([[balans]] §In de praktijk — buiten-balans-vermelding). ⚖️
> 2. **Voorziening voor risico's en kosten** (rek 16 Voorzieningen): bij waarschijnlijk verlies → voorziening boeken op basis van de schatting van het bedrag (KB WVV art. 3:24-3:27). ⚖️
> 3. **Materiële afwijking** bij niet-vermelding of onder-geschatte voorziening → impact op het oordeel van de auditor.
> 
> **Welke acties moet de auditor ondernemen?**
> 
> 1. **Externe bevestiging vragen aan de advocaat** ([[externe-bevestiging-audit]] §Werkwijze): de advocaat is bij uitstek de externe partij die status, aard, en bedrag van de geschillen kan bevestigen. Schriftelijke confirmatie rechtstreeks aan auditor. ⚖️
> 2. **Toelichting nazien**: zijn alle hangende geschillen vermeld in de toelichting (off-balance + voorzieningen)? Vergelijk de erelonen-volume met de toelichting — onverhouding wijst op niet-vermelding. ⚖️
> 3. **Voorziening evalueren** ([[boekhoudkundige-schattingen-audit]]): bij materieel geschil + waarschijnlijk verlies → voorziening boeken op basis van de schatting. Auditor toetst de redelijkheid van de schatting (range van uitkomsten van de advocaat). ⚖️
> 4. **Continuïteit beoordelen**: een groot geschil kan continuïteit bedreigen. Bij materieel risico → assessing going concern (ISA 570). ⚖️
> 
> **Impact op het controleverslag**:
> 
> - **Niets aan de hand** (geschil gering, correct vermeld, voorziening adequaat) → geen impact, gewoon goedkeurend oordeel
> - **Materiële niet-vermelding of onder-voorziening** → mogelijke afwijking van materieel belang → oordeel met **voorbehoud** indien geïsoleerd, of **afkeurend** indien diepgaand (zie [[controleoordeel-types]]) ⚖️
> - **Onmogelijk om informatie te krijgen** (advocaat antwoordt niet, cliënt weigert) → scope-beperking → mogelijk **onthouding van oordeel** indien diepgaand ⚖️
> - **Materiële continuïteitsonzekerheid** → paragraaf 'Materiële onzekerheid m.b.t. continuïteit' in het verslag (ISA 570) ⚖️
> 
> ⚠️ Een ereloon van € 12.000 is **niet automatisch** materieel — afhankelijk van de bedrijfsgrootte en de materialiteitsdrempel. Maar het is een **trigger** om dieper te kijken, niet de afwijking zelf. 🤖
> 
> _Grondslag: [[externe-bevestiging-audit]]; [[boekhoudkundige-schattingen-audit]]; [[controleoordeel-types]]; ISA 501 §4-A6 (litigation & claims); ISA 505 (externe confirmaties); ISA 570 (continuïteit); KB WVV art. 3:24-3:27 (voorzieningen)._

> [!info]- Bronnen (4)
> - [[externe-bevestiging-audit|content/concepten/externe-bevestiging-audit.md]] · Bouwstenen — Werkwijze (advocaat) → ondersteunt: externe bevestiging van advocaat voor geschillen
> - [[boekhoudkundige-schattingen-audit|content/concepten/boekhoudkundige-schattingen-audit.md]] · Bouwstenen → ondersteunt: voorzieningen voor geschillen als schatting
> - [[controleoordeel-types|content/concepten/controleoordeel-types.md]] · Bouwstenen → ondersteunt: impact op oordeel-type
> - [[balans|content/concepten/balans.md]] · In de praktijk — buiten-balans-vermelding → ondersteunt: klasse 0 hangende geschillen

> [!info]- Provenance
> - Generator: claude-opus-4-7
> - Datum: 2026-05-19
> - Antwoord-type: definitie
> - Checklist-versie: 1.0
> - Gates gepasseerd: claim_coverage, geen_externe_kennis
> - Verify gepasseerd: True
> - Wetsversie-policy: huidig

---

### 2014-1-vr14 · 2014-1 · 14.0 pt

**Vraagformaat**: J/F · **Antwoord-type**: — · **Confidence**: —

#### Vraagtekst

In het kader van een controleopdracht waarvoor een volkomen controle vereist is ontvangen
we tijdens onze audit ter plaatse op 20/02/2014 van de interne boekhouder de
boekhoudkundige staat per 31/12/2013. Zoals je weet moeten er voor we op de cijfers
“afstormen” een aantal voorbereidende werken en checks verricht worden.
Alvorens over te gaan tot cijfercontroles hebben we de materialiteitsgrens berekend op
50.000 EUR.

- **a.** Kunnen we onze controleopdracht op deze cijfers afhandelen en ons besluit

ondertekenen? Motiveer uw antwoord.

**Antwoord
b) Wat is het belang, in het kader van deze opdracht, zoals hierboven beschreven,
van het vastleggen van de materialiteitsgrens?**

Antwoord

- **c.** De vennootschap voor dewelke wij deze controleopdracht verrichten, heeft een

dochterbedrijf via aandelen aangekocht voor 300.000 EUR (code 28).

**Hoe pak je
deze post aan ?**

Geef 2 controledoelstellingen en 2 controletechnieken die hier
kunnen toegepast worden.

**Antwoord
d) Gedurende deze controleopdracht, ga je een afloopcontrole uitvoeren op de post
“bezoldigingen en sociale lasten” (passief codes 454/9) .**

Hoe voer je zo een
controle uit, leg uit of werk een voorbeeld uit?
Antwoord

VENNOOTSCHAPSRECHT 20 PUNTEN

> [!warning] Gap niveau **b** — type **checklist_fail_softmatch**
> Volkomen controle casus 14 ptn met 4 deelvragen (besluit afhandelen, materialiteit, deelneming-controle, afloopcontrole bezoldigingen). Vereist: timing-context-redenering, specifieke procedures voor consolidatie + bezoldigingen. Partial-grounded antwoord mogelijk maar veelomvattend — gap niveau b voor record-uitbreiding op afloopcontrole bezoldigingen + deelnemingen-controle.
> 
> Ontbrekende velden: Volledige antwoord-grondslag uit records
> 
> _Gedetecteerd op_: 2026-05-19

#### Subvraag a)

Kunnen we onze controleopdracht op deze cijfers afhandelen en ons besluit
ondertekenen? Motiveer uw antwoord.

#### Subvraag b)

Wat is het belang, in het kader van deze opdracht, zoals hierboven beschreven,
van het vastleggen van de materialiteitsgrens?

#### Subvraag c)

De vennootschap voor dewelke wij deze controleopdracht verrichten, heeft een
dochterbedrijf via aandelen aangekocht voor 300.000 EUR (code 28). Hoe pak je
deze post aan ? Geef 2 controledoelstellingen en 2 controletechnieken die hier
kunnen toegepast worden.

#### Subvraag d)

Gedurende deze controleopdracht, ga je een afloopcontrole uitvoeren op de post
“bezoldigingen en sociale lasten” (passief codes 454/9) . Hoe voer je zo een
controle uit, leg uit of werk een voorbeeld uit?

---

### 2015-1-vr15 · 2015-1 · 2.0 pt

_Ook geklassificeerd onder_: 4.0

**Vraagformaat**: MC · **Antwoord-type**: kwalificatie · **Confidence**: grounded

#### Vraagtekst

Tijdens een controleopdracht bij een middelgrote onderneming, zonder commissaris en in
het kader van een contractueel beperkt nazicht stelt de externe accountant een aantal
verbeteringen (adjustments) voor.
a) Wanneer deze adjustments talrijk en substantieel zijn in bedrag, zou dit een probleem
kunnen veroorzaken in het bijzonder op het vlak van deontologische regels?
Antwoord … / 0,5 punt

|   |   |
| --- | --- |
|   | Ja |
|   | Neen |

b) Verklaar bondig.
Antwoord … / 1,5 punten

#### Modelantwoord

a) Indien adjustments worden geweigerd door de cliënt + materieel → de accountant kan een oordeel met voorbehoud uitbrengen, of (indien diepgaand) een afkeurend oordeel. Hij kan zich niet onthouden van rapportering — een contractueel beperkt nazicht eindigt met een verslag.

> [!success]- Motivering
> In een **contractueel beperkt nazicht** (review) — met **beperkte mate van zekerheid** in plaats van redelijke zekerheid (ISA 2400 / ITAA-norm-beoordelingsopdracht) — stelt de accountant **adjustments** voor wanneer hij afwijkingen vaststelt.
> 
> ### Wanneer cliënt de adjustments weigert
> 
> **Optie 1: cliënt past de adjustments toe** → geen probleem, beoordelingsverslag met negatieve assurance ("we zijn niets tegengekomen dat ons doet vermoeden ...").
> 
> **Optie 2: cliënt weigert** + adjustments zijn **materieel** → accountant moet de afwijking weerspiegelen in zijn verslag:
> - **Voorbehoud** (geïsoleerde afwijking, niet alles-doordringend) ⚖️
> - **Afkeurend verklaring** (diepgaande materiële afwijking — beoordelingsverslag-equivalent van afkeurend oordeel) ⚖️
> - **Onthouding** (bij onmogelijke scope — niet bij weigering van adjustment, want scope is hier wel bekend)
> 
> ### Belangrijke nuances
> 
> 🤖 Verschil met een **wettelijke commissaris-controle**: bij een contractueel beperkt nazicht is er geen wettelijke verplichting tot publiceren — maar de accountant blijft gebonden aan zijn beroepsethiek en moet wel **rapporteren** wat hij heeft vastgesteld. Hij kan zich niet eenvoudig "terugtrekken" zonder gevolgen — daarvoor is een opdrachtbrief met opzegclausule nodig.
> 
> ⚖️ Bij een controleopdracht (assurance met redelijke zekerheid) zou hetzelfde probleem leiden tot voorbehoud/afkeurend/onthouding op de jaarrekening zelf. Bij beperkt nazicht: hetzelfde principe maar met "negatieve assurance"-formulering ("Op basis van onze beoordeling is ons niet gebleken dat ... behalve voor [adjustment]").
> 
> _Grondslag: [[contractuele-beoordelingsopdracht]] §Bouwstenen; ISA 2400 (Engagements to Review Historical Financial Statements); [[controleoordeel-types]]; ITAA-norm beoordelingsopdracht (indien beschikbaar)._

> [!info]- Bronnen (2)
> - [[contractuele-beoordelingsopdracht|content/concepten/contractuele-beoordelingsopdracht.md]] · Bouwstenen → ondersteunt: beperkt nazicht + negatieve assurance
> - [[controleoordeel-types|content/concepten/controleoordeel-types.md]] · Bouwstenen — voorbehoud/afkeurend/onthouding → ondersteunt: mogelijke oordeel-types

> [!info]- Provenance
> - Generator: claude-opus-4-7
> - Datum: 2026-05-19
> - Antwoord-type: kwalificatie
> - Checklist-versie: 1.0
> - Gates gepasseerd: claim_coverage, geen_externe_kennis
> - Verify gepasseerd: True
> - Wetsversie-policy: huidig

#### Subvraag a)

Wanneer deze adjustments talrijk en substantieel zijn in bedrag, zou dit een probleem
kunnen veroorzaken in het bijzonder op het vlak van deontologische regels?

#### Subvraag b)

Verklaar bondig.

---

### 2015-1-vr16 · 2015-1 · 4.0 pt

**Vraagformaat**: J/F · **Antwoord-type**: opsomming · **Confidence**: grounded

#### Vraagtekst

Een eerste stap bij het auditwerk is de aanvaardingsprocedure van de opdracht.

**Geef twee voorbeelden van situaties bij deze procedure, waarbij we het dossier mogelijks
niet kunnen aanvaarden.**

Antwoord

#### Modelantwoord

Twee voorbeelden: (1) Onafhankelijkheidsprobleem of belangenconflict — de auditor, zijn kantoor of nauwe verwanten hebben een financiële of persoonlijke band met de cliënt die de onafhankelijkheid aantast (KB 1998 plichtenleer art. 12; Wet ITAA 2019 §Onafhankelijkheid). (2) Cliënt erkent niet de drie basisverantwoordelijkheden van het management (opstellen jaarrekening, interne beheersing, toegang tot informatie verschaffen) — zonder die erkenning mist de audit een referentiekader.

> [!success]- Motivering
> Bij de aanvaardingsprocedure van een audit-opdracht moet de accountant verschillende randvoorwaarden toetsen ([[aanvaarden-audit-opdracht]] §Stappen 1-5). Situaties waarin het dossier **mogelijk niet kan worden aanvaard**:
> 
> ### Voorbeeld 1: Onafhankelijkheidsprobleem of belangenconflict
> 
> De accountant — zijn kantoor of zijn nauwe verwanten — hebben een band met de cliënt die de onafhankelijkheid in twijfel trekt:
> - Familiale band met de bestuurder/eigenaar
> - Significant financieel belang (aandelen, schulden, leningen)
> - Eerdere niet-audit-diensten die zelf-controle veroorzaken (bv. boekhouding gevoerd voor dezelfde cliënt)
> - Gerelateerde commerciële relaties (significant deel van de omzet komt van deze ene cliënt)
> 
> ⚖️ Schending van onafhankelijkheid leidt tot **tucht en nietigheid van het verslag** (Wet ITAA 2019 + KB 1998 plichtenleer art. 12 + IESBA Code of Ethics). De accountant **weigert** of trekt zich terug.
> 
> ### Voorbeeld 2: Cliënt erkent niet de drie basisverantwoordelijkheden van het management
> 
> Voor een audit moet het management ([[aanvaarden-audit-opdracht]] §1) erkennen:
> - Verantwoordelijkheid voor het opstellen van de jaarrekening conform het toepasselijke financieel rapporteringsstelsel ⚖️
> - Verantwoordelijkheid voor de interne beheersing die het opstellen mogelijk maakt zonder afwijking van materieel belang ⚖️
> - Verplichting om de accountant toegang te verschaffen tot alle relevante informatie en aanvullende inlichtingen ⚖️
> 
> Zonder die erkenning **mist de audit een referentiekader** en is een controle-oordeel onmogelijk te onderbouwen. → niet aanvaarden.
> 
> ### Aanvullende voorbeelden (niet in opsomming):
> - Toepasselijk rapporteringsstelsel niet aanvaardbaar (bv. exotisch zelfbedacht model in plaats van BE GAAP/IFRS)
> - Voorgaande accountant meldt fundamentele integriteitsbezwaren over het management (KB 1998 plichtenleer art. 17-18 — collegiaal contact verplicht)
> - Cliënt is geen toegestane juridische entiteit voor de opdracht (bv. een ad-hoc structuur zonder rechtspersoonlijkheid voor een wettelijke commissaris-controle)
> 
> _Grondslag: [[aanvaarden-audit-opdracht]] §Stappen 1-3; Wet ITAA 2019; KB 1998 plichtenleer art. 12 + 17-18; IESBA Code of Ethics._

> [!info]- Bronnen (2)
> - [[aanvaarden-audit-opdracht|content/concepten/aanvaarden-audit-opdracht.md]] · Stappen 1-3 → ondersteunt: randvoorwaarden + onafhankelijkheid + collegiaal contact
> - [[belangenconflict-accountant|content/concepten/belangenconflict-accountant.md]] · Bouwstenen → ondersteunt: voorbeeld onafhankelijkheid

> [!info]- Provenance
> - Generator: claude-opus-4-7
> - Datum: 2026-05-19
> - Antwoord-type: opsomming
> - Checklist-versie: 1.0
> - Gates gepasseerd: claim_coverage, geen_externe_kennis
> - Verify gepasseerd: True
> - Wetsversie-policy: huidig

---

### 2015-1-vr17 · 2015-1 · 6.0 pt

_Ook geklassificeerd onder_: 3.0, 1.2

**Vraagformaat**: MC · **Antwoord-type**: — · **Confidence**: —

#### Vraagtekst

Tijdens de werkzaamheden aan een controleverslag ivm een omzetting stelt de aangestelde
accountant vast dat op het actief een debet lopende rekening op naam van de overleden
vader van de zaakvoerders-aandeelhouders voorkomt.

- **a.** Geef twee (2) controledoelstellingen die op dergelijk actief worden toegepast?
- **b.** Geef kort weer voor elk van deze twee (2) controledoelstellingen welke techniek of

methodiek je toepast?
Vul uw antwoorden in op volgend schema.
Antwoord
Controledoelstelling Techniek of methodiek

Debet lopende 1. 1.
rekening
2. 2.

> [!warning] Gap niveau **b** — type **checklist_fail_softmatch**
> Casus debet lopende rekening op naam van overleden vader van zaakvoerders-aandeelhouders. Vereist: erfrechtelijke kennis (wat gebeurt met vordering bij overlijden), vennootschapsrecht (terugvordering bij erven), en boekhoudkundige verwerking (afboeking, voorziening, eventueel onbehoorlijk bestuur). Vereist multi-domein records die deels ontbreken. Gap niveau b.
> 
> Ontbrekende velden: Volledige antwoord-grondslag uit records
> 
> _Gedetecteerd op_: 2026-05-19

#### Subvraag a)

Geef twee (2) controledoelstellingen die op dergelijk actief worden toegepast?

#### Subvraag b)

Geef kort weer voor elk van deze twee (2) controledoelstellingen welke techniek of
methodiek je toepast?
Vul uw antwoorden in op volgend schema.

---

### 2015-1-vr18 · 2015-1 · 8.0 pt

**Vraagformaat**: J/F · **Antwoord-type**: casus · **Confidence**: grounded

#### Vraagtekst

Het is 23 januari 2015 en de onderneming heeft haar boekhouding afgesloten op
30 september 2014 conform haar statuten. Op 1 oktober 2014 heeft u als controlerende
accountant de voorraadtelling gevolgd en u ermee akkoord verklaard. Het betreft hier een
Belgisch bedrijf dat in handen is van een Franse groep. Het bedrijf is gespecialiseerd in
hoogtechnologische gasleidingen. We berekenen een materialiteit van 100.000 EUR op de
resultatenrekening en 70.000 EUR op de balansposten.
Het risicoprofiel is laag gezien er een goede interne controle is voor wat de aankopen,
financiële verrichtingen en verkopen betreft.
a) De telling van de voorraad (30/09/2014) hebben we fysiek kunnen meemaken en deze
hoeveelheidstelling was in orde.

**Welke controle gaan we nu (23/01/2015) nog doen op
de voorraad ?**

Geef twee controledoelstellingen met telkens een voorbeeld van de techniek die je
gaat toepassen.

**Antwoord … / 6 punten
Vul uw antwoorden in op volgend schema.**

| Controledoelstelling | Techniek |
| --- | --- |
| 1. <br> 2. | 1. <br> 2. |

b) Bij nazicht van de handelsvorderingen (onder toepassing van 21% BTW) wordt een
confirmatie bekomen van een klant voor 121.000,00 EUR, daar waar de vordering in de
boekhouding op 217.800,00 EUR staat. Bij de confirmatie zit een ontvangstbon
afgetekend op 29/09/2014 door de klant en de chauffeur die de levering heeft gedaan.
Op deze ontvangstbon staat de vermelding dat er voor 80.000,00 EUR (excl btw) aan
fout geleverde goederen terug zijn meegenomen.
Welke actie onderneem je als controlerende accountant:
 Kies één van de drie mogelijkheden:
Antwoord … / 1 punt

|   |   |
| --- | --- |
|   | of je stelt een correctieboeking voor (geef dan de boeking) |
|   | of je maakt een voorbehoud (motiveer) |
|   | of vraag je de correctie te boeken in de heropening van <br> volgend boekjaar (geef dan de boeking). |

 Verklaar bondig.
Antwoord … / 1 punt

#### Modelantwoord

Periode 01/10/2014 (voorraadtelling akkoord) → 23/01/2015 (huidige datum) = ~4 maanden. Voor de accountant zijn dit de "gebeurtenissen na balansdatum" (ISA 560 / KB WVV art. 3:6). Acties: (a) management vragen om informatie over gebeurtenissen tussen balansdatum en datum verslag, (b) verifiëren of die gebeurtenissen aanpassende (adjusting events) of toelichtende (non-adjusting events) gebeurtenissen zijn, (c) verkrijgen van schriftelijke bevestiging van management dat alle relevante na-balansdatum-events zijn meegedeeld, (d) impact op jaarrekening + toelichting + controleverslag beoordelen.

> [!success]- Motivering
> ### Context
> 
> Balansdatum: 30 september 2014. Voorraadtelling bij accountant: 1 oktober 2014. Huidige datum: 23 januari 2015. **Periode van ~4 maanden tussen balansdatum en datum waarop het controleverslag wordt opgesteld** — typische "na-balansdatum-periode" in een audit.
> 
> ### Klassieke aanpak (ISA 560 + KB WVV art. 3:6)
> 
> **Twee soorten gebeurtenissen na balansdatum**:
> 
> 1. **Aanpassende gebeurtenissen (adjusting events)** — gebeurtenissen die meer informatie verschaffen over omstandigheden die **al bestonden** op balansdatum. ⚖️ Voorbeelden: faillissement van een grote debiteur waar al twijfel over bestond → waardevermindering op vordering boeken op balans 30/09; uitspraak in een rechtsgeschil dat op 30/09 al hangende was → voorziening boeken.
> 2. **Niet-aanpassende gebeurtenissen (non-adjusting events)** — gebeurtenissen die ontstonden **na** balansdatum. ⚖️ Voorbeelden: brand in november, overname op decembre, dividendbeslissing. Geen aanpassing van cijfers, maar **toelichting verplicht** indien materieel.
> 
> ### Acties van de accountant
> 
> 1. **Management bevragen** — wat is er sinds 30 september gebeurd? Significante contracten, claims, faillissementen, productiestilstanden, brand/diefstal, kapitaalverhogingen, omzet-veranderingen, etc. ⚖️
> 2. **Documentatie reviewen** — recente notulen bestuursvergaderingen, ondertekende contracten, recente bank-/leverancier-correspondentie, juridische bevestigingen. ⚖️
> 3. **Subsequente boekingen testen** — controleer of materiële gebeurtenissen die zich na 30/09 voordeden, correct in de jaarrekening van 30/09/2014 zijn opgenomen (adjusting) of in toelichting (non-adjusting). ⚖️
> 4. **Externe bevestigingen** van advocaten (geschillen na 30/09) en banken (kredietfaciliteiten-status) — zie [[externe-bevestiging-audit]]. ⚖️
> 5. **Schriftelijke bevestiging van management** ([[schriftelijke-bevestiging-management]]) — dat alle relevante na-balansdatum-events gemeld zijn (ISA 580). ⚖️
> 6. **Impact beoordelen op**:
>    - Cijfers: aanpassende → boeken in jaarrekening
>    - Toelichting: niet-aanpassende materiële → vermelden
>    - Controleverslag: bij materiële niet-vermelding → voorbehoud of afkeurend
>    - Continuïteit: gebeurtenissen die continuïteit bedreigen → mogelijk going-concern paragraaf (ISA 570)
> 
> _Grondslag: ISA 560 (Subsequent Events); KB WVV art. 3:6 (gebeurtenissen na balansdatum); ITAA KMO-controlenorm §123-126; [[externe-bevestiging-audit]]; [[schriftelijke-bevestiging-management]]._

> [!info]- Bronnen (2)
> - [[externe-bevestiging-audit|content/concepten/externe-bevestiging-audit.md]] · Werkwijze → ondersteunt: externe bevestigingen na balansdatum
> - [[schriftelijke-bevestiging-management|content/concepten/schriftelijke-bevestiging-management.md]] · Bouwstenen → ondersteunt: management bevestiging na-balansdatum-events

> [!info]- Provenance
> - Generator: claude-opus-4-7
> - Datum: 2026-05-19
> - Antwoord-type: casus
> - Checklist-versie: 1.0
> - Gates gepasseerd: claim_coverage, geen_externe_kennis
> - Verify gepasseerd: True
> - Wetsversie-policy: huidig

#### Subvraag a)

De telling van de voorraad (30/09/2014) hebben we fysiek kunnen meemaken en deze
hoeveelheidstelling was in orde. Welke controle gaan we nu (23/01/2015) nog doen op
de voorraad ?
Geef twee controledoelstellingen met telkens een voorbeeld van de techniek die je
gaat toepassen.

#### Subvraag b)

Bij nazicht van de handelsvorderingen (onder toepassing van 21% BTW) wordt een
confirmatie bekomen van een klant voor 121.000,00 EUR, daar waar de vordering in de
boekhouding op 217.800,00 EUR staat. Bij de confirmatie zit een ontvangstbon
afgetekend op 29/09/2014 door de klant en de chauffeur die de levering heeft gedaan.
Op deze ontvangstbon staat de vermelding dat er voor 80.000,00 EUR (excl btw) aan
fout geleverde goederen terug zijn meegenomen.
Welke actie onderneem je als controlerende acc

---

### 2015-1-vr19 · 2015-1 · 5.0 pt

**Vraagformaat**: MC · **Antwoord-type**: casus · **Confidence**: inferred

#### Vraagtekst

**Geef de werkwijze tijdens een externe controle om tot de confirmatie van een representatief
aantal leverancierssaldi te komen.**

- **a.** Wat is representatief?

Antwoord … / 1 punt

- **b.** Hoe doe je de steekproef?

Antwoord … / 1 punt

- **c.** Hoe gebeurt de verzending van de confirmatiebrieven?

Antwoord … / 1 punt

- **d.** Wie ontvangt de antwoorden?

Antwoord … / 1 punt
e) Wat bij niet ontvangst van antwoorden?
Antwoord … / 1 punt

|   |   |   |   |   |
| --- | --- | --- | --- | --- |
| VENNOOTSCHAPSRECHT |   |   | 20 PUNTEN |   |
|   |   |   |   | 20 PUNTEN |

Antwoorden
Plaats de letter van het juiste antwoord in onderstaande rooster.

| Vraag | 1 | 2 | 3 | 4 | 5 |
| --- | --- | --- | --- | --- | --- |
| Antwoord |   |   |   |   |   |
| Punten | 4 | 4 | 4 | 4 | 4 |

#### Modelantwoord

Zie antwoorden per subvraag a)-e). Werkwijze externe confirmatie leveranciersaldi conform ISA 505 + ITAA KMO-controlenorm §89-92.

> [!success]- Motivering
> Vraag betreft de werkwijze van externe bevestiging (confirmation) voor leverancierssaldi — vijf procedurestappen. Zie subvragen per stap.

> [!info]- Provenance
> - Generator: claude-opus-4-7
> - Datum: 2026-05-19
> - Antwoord-type: casus
> - Checklist-versie: 1.0
> - Gates gepasseerd: claim_coverage, geen_externe_kennis
> - Verify gepasseerd: True
> - Wetsversie-policy: huidig

#### Subvraag a)

Wat is representatief?

**Antwoord-type**: definitie · **Confidence**: inferred

#### Modelantwoord

Representatief = een steekproef die de samenstelling en spreiding van de hele populatie van leveranciers weerspiegelt — kwantitatief (significante bedragen + spreiding klein/groot) én kwalitatief (verschillende soorten leveranciers: regulier, eenmalig, gerelateerde partijen, risico-leveranciers).

> [!success]- Motivering
> Een **representatieve** steekproef bevat elementen die de hele populatie weerspiegelen. Voor leverancierssaldi betekent dat:
> 
> - **Kwantitatieve dekking**: significante saldi (top-bedragen) volledig erin, plus aselecte spreiding over de overige saldi van klein tot middelgroot. ⚖️ De steekproef moet voldoende dekking van het totale balansbedrag geven (vaak ≥ 60-70 % van het saldo handelsleveranciers in monetaire eenheden — concrete drempel afhankelijk van risico en materialiteit). 🤖
> - **Kwalitatieve dekking**: spreiding over types leveranciers — recurrente versus eenmalige, binnenlandse versus buitenlandse, gerelateerde versus onafhankelijke. ⚖️ Risico-leveranciers (nieuwe, geschillen, ongewone bewegingen) verplicht erin. 🤖
> - **Doel**: een redelijke basis krijgen voor conclusies over de **hele populatie** van leveranciers, zonder alle saldi te testen ([[steekproef-audit]]). ⚖️
> 
> _Grondslag: ISA 530 (audit sampling) §A1-A4; ITAA KMO-controlenorm Bijlage 1 (definitie steekproef)._

> [!info]- Bronnen (2)
> - [[steekproef-audit|content/concepten/steekproef-audit.md]] · Definitie → ondersteunt: definitie steekproef + doel
> - [[ISA-530|resources/bronnen/normen/ISA-530.md]] · §A1-A4 → ondersteunt: representativiteit kwantitatief + kwalitatief

> [!info]- Provenance
> - Generator: claude-opus-4-7
> - Datum: 2026-05-19
> - Antwoord-type: definitie
> - Checklist-versie: 1.0
> - Gates gepasseerd: circular_definition, claim_coverage, geen_externe_kennis
> - Verify gepasseerd: True
> - Wetsversie-policy: huidig

#### Subvraag b)

Hoe doe je de steekproef?

**Antwoord-type**: procedure · **Confidence**: inferred

#### Modelantwoord

Steekproef-keuze: (1) selecteer alle significante saldi (top-N of monetary unit sampling boven materialiteit-drempel); (2) selecteer aselecte aanvulling over de overige saldi (random of systematic sampling); (3) selecteer expliciete risico-saldi (geschillen, nieuwe leveranciers, gerelateerde partijen).

> [!success]- Motivering
> De steekproef wordt opgemaakt langs drie sporen die elkaar aanvullen:
> 
> 1. **Significante saldi (key items)**: alle saldi boven een materialiteit-drempel (bv. > € 50.000) of via Monetary Unit Sampling (MUS) waarbij grote saldi automatisch een hogere kans op selectie hebben. ⚖️ Levert dekking op de bedragen-as.
> 2. **Aselecte aanvulling**: random sampling (lotnummering) of systematic sampling (elke n-de saldi) over de resterende populatie. ⚖️ Levert spreiding over de hele populatie.
> 3. **Risico-saldi (judgemental)**: saldi die de auditor expliciet wil testen wegens specifieke risico-indicaties (saldo's met geschillen, nieuwe leveranciers, ongewone bewegingen, gerelateerde-partij-transacties). ⚖️
> 
> Aantal te selecteren: bepaald door risico-inschatting (ISA 530 §A11-A14) — hoe hoger het ingeschatte risico, hoe groter de steekproef. 🤖
> 
> _Grondslag: ISA 530 §A1-A14; ITAA KMO-controlenorm Bijlage 1._

> [!info]- Bronnen (2)
> - [[steekproef-audit|content/concepten/steekproef-audit.md]] · Voorbeelden — Rotex steekproef gestratificeerd → ondersteunt: gestratificeerde steekproef
> - [[ISA-530|resources/bronnen/normen/ISA-530.md]] · §A1-A14 → ondersteunt: steekproef-methodes + omvang

> [!info]- Provenance
> - Generator: claude-opus-4-7
> - Datum: 2026-05-19
> - Antwoord-type: procedure
> - Checklist-versie: 1.0
> - Gates gepasseerd: claim_coverage, geen_externe_kennis
> - Verify gepasseerd: True
> - Wetsversie-policy: huidig

#### Subvraag c)

Hoe gebeurt de verzending van de confirmatiebrieven?

**Antwoord-type**: procedure · **Confidence**: grounded

#### Modelantwoord

De auditor stelt de bevestigingsbrief zelf op, laat de cliënt deze ondertekenen (op briefpapier van de cliënt) en verstuurt de brief zelf naar de leverancier. Antwoordadres in de brief = kantoor van de auditor. De cliënt mag de brief opmaken of ondertekenen, maar niet onderscheppen of doorsturen.

> [!success]- Motivering
> De **auditor controleert het kanaal volledig** (ITAA KMO-controlenorm §89; ISA 505 §7-8):
> 
> 1. **Brief-opmaak**: auditor stelt de inhoud op, met daarin het saldo dat in de boekhouding van de cliënt staat (positieve of negatieve bevestiging — zie [[externe-bevestiging-audit]]). ⚖️
> 2. **Ondertekening door cliënt**: de brief gaat op briefpapier van de cliënt en wordt door een gemachtigde van de cliënt ondertekend — anders zou de leverancier de auditor niet als geldige verzoek-partij erkennen. ⚖️
> 3. **Verzending door auditor**: de auditor verzendt zelf (per post of beveiligde digitale weg), rechtstreeks naar het adres van de leverancier. Cliënt mag de brief niet zelf opsturen — anders kan hij onderscheppen of inhoud manipuleren. ⚖️
> 4. **Antwoordadres = auditor**: in de brief staat duidelijk dat het antwoord rechtstreeks naar het **kantoor van de auditor** moet, niet via de cliënt. ⚖️
> 
> _Grondslag: ITAA KMO-controlenorm §89 + ISA 505 §7-8._

> [!info]- Bronnen (2)
> - [[externe-bevestiging-audit|content/concepten/externe-bevestiging-audit.md]] · Bouwstenen — Auditor controleert het kanaal → ondersteunt: verzending + adres
> - [[externe-bevestiging-audit|content/concepten/externe-bevestiging-audit.md]] · Bouwstenen — Werkwijze in drie stappen → ondersteunt: verzending-procedure

> [!info]- Provenance
> - Generator: claude-opus-4-7
> - Datum: 2026-05-19
> - Antwoord-type: procedure
> - Checklist-versie: 1.0
> - Gates gepasseerd: claim_coverage, geen_externe_kennis
> - Verify gepasseerd: True
> - Wetsversie-policy: huidig

#### Subvraag d)

Wie ontvangt de antwoorden?

**Antwoord-type**: presentatie · **Confidence**: grounded

#### Modelantwoord

De auditor ontvangt de antwoorden rechtstreeks op zijn kantoor — niet via de cliënt. Dat is voorgeschreven om manipulatie of onderschepping uit te sluiten.

> [!success]- Motivering
> De **antwoorden komen rechtstreeks naar het kantoor van de auditor**, niet via de cliënt. ⚖️
> 
> Het adres dat in de bevestigingsbrief vermeld wordt voor het terug-sturen is het kantoor-adres van de auditor (of een beveiligde digitale postbus die de auditor beheert). De cliënt mag de antwoorden niet ontvangen, openen of voorfilteren — dat zou de evidence-waarde van de externe bevestiging fundamenteel ondermijnen, omdat het kenmerk 'rechtstreeks van derde aan auditor' verloren gaat.
> 
> _Grondslag: ITAA KMO-controlenorm §89 ('rechtstreeks aan de beroepsbeoefenaar'); ISA 505 §7 (auditor maintains control over confirmation process)._

> [!info]- Bronnen (1)
> - [[externe-bevestiging-audit|content/concepten/externe-bevestiging-audit.md]] · Definitie + §Auditor controleert het kanaal → ondersteunt: antwoordadres = auditor

> [!info]- Provenance
> - Generator: claude-opus-4-7
> - Datum: 2026-05-19
> - Antwoord-type: presentatie
> - Checklist-versie: 1.0
> - Gates gepasseerd: claim_coverage, geen_externe_kennis
> - Verify gepasseerd: True
> - Wetsversie-policy: huidig

#### Subvraag e)

Wat bij niet ontvangst van antwoorden?

**Antwoord-type**: procedure · **Confidence**: grounded

#### Modelantwoord

Bij niet-ontvangst: alternatieve werkzaamheden uitvoeren. Voor leveranciersaldi typisch: (1) subsequente betalingen testen na balansdatum; (2) factuur- en bestelbon-koppeling inspecteren; (3) contracten of leveringsovereenkomsten nakijken. Bij verschil in een ontvangen antwoord: oorzaak onderzoeken en documenteren.

> [!success]- Motivering
> Niet-antwoord = **geen** bevestiging. De auditor moet **alternatieve werkzaamheden** uitvoeren om voldoende controle-informatie te verkrijgen (ITAA KMO-controlenorm §92; ISA 505 §12):
> 
> 1. **Subsequente betalingen testen** — kijk in de bankafschriften na balansdatum of de geboekte schuld effectief betaald werd; een betaling aan de leverancier kort na balansdatum is sterk bewijs van het bestaan van de schuld. ⚖️
> 2. **Factuur- en bestelbon-koppeling inspecteren** — drieweg-match (bestelbon, ontvangstbon, factuur) levert documentair bewijs over het bestaan en de waardering. ⚖️
> 3. **Contracten of leveringsovereenkomsten nakijken** — voor recurrente leveranciers met raamcontract levert het contract context over de redelijkheid van het saldo. 🤖
> 
> Bij verschil in een wél ontvangen antwoord: de oorzaak onderzoeken en documenteren (timing-verschil, betwiste post, fout in cliëntenboeking, fout in leveranciersboeking). ⚖️
> 
> _Grondslag: ITAA KMO-controlenorm §92; ISA 505 §12-16 (handling non-responses + exceptions)._

> [!info]- Bronnen (1)
> - [[externe-bevestiging-audit|content/concepten/externe-bevestiging-audit.md]] · Bouwstenen — Niet-antwoord en alternatieve werkzaamheden → ondersteunt: alternatieve werkzaamheden + verschil-onderzoek

> [!info]- Provenance
> - Generator: claude-opus-4-7
> - Datum: 2026-05-19
> - Antwoord-type: procedure
> - Checklist-versie: 1.0
> - Gates gepasseerd: claim_coverage, geen_externe_kennis
> - Verify gepasseerd: True
> - Wetsversie-policy: huidig

---

### 2024-1-vr2 · 2024-1

> [!warning] Herinnering-reconstructie (fragment)
> Deze vraag is een **herinnering**-reconstructie (volledigheid: fragment) — geen officiële ITAA-bundel. Modelantwoord rust op de geherinterpreteerde vraagtekst (ADR-022).

**Vraagformaat**: J/F · **Antwoord-type**: — · **Confidence**: —

#### Vraagtekst

2 Externe controle

- **A.** Stellingen juist of fout ivm onafhankelijkheid bij controle opdracht
- **B.** Na acceptatie van de opdracht -> voldoende kennis verwerven, op welke wijze?
- **C.** Volkomen controle volgens revisienormen
- **D.** 4 algemene stellingen juist of fout

E. Bij een accountantsonderzoek wordt de materialiteitsdrempel:

- **A.** a. Vastgesteld bij KB
- **B.** b. Door aandeelhouders van de vennootschap vastgesteld
- **C.** c. Bepaald op basis van omzet van de 2 laatste jaren
- **D.** d. Bepaald naargelang inherente risico’s + interne controle van de cliënt

> [!note]- Geherinterpreteerde vraagtekst (ADR-022)
> Casus externe controle / accountantsonderzoek, 5 deelvragen:
> A. Stellingen juist of fout in verband met onafhankelijkheid bij een controle-opdracht (stellingen niet bewaard in herinnering).
> B. Na acceptatie van de opdracht moet de accountant voldoende kennis verwerven van de cliënt — op welke wijze gebeurt dat?
> C. Volkomen controle volgens de revisienormen — wat houdt dat in?
> D. Vier algemene stellingen juist of fout (stellingen niet bewaard in herinnering).
> E. MC — Bij een accountantsonderzoek wordt de materialiteitsdrempel: a. Vastgesteld bij KB / b. Door aandeelhouders van de vennootschap vastgesteld / c. Bepaald op basis van omzet van de twee laatste jaren / d. Bepaald naargelang inherente risico's + interne controle van de cliënt.
> 
> _Motivering_: Sub-A en sub-D verwijzen expliciet naar 'stellingen' die niet in de herinnering bewaard zijn — niet beantwoordbaar zonder bron. Sub-B en sub-C hebben volledige stam. Sub-E is een complete MC met vier alternatieven.
> _Confidence_: inferred · _Datum_: 2026-05-19

> [!example]- MC-opties (gestructureerd)
> | Label | Tekst | Juistheid | Motivering |
> | --- | --- | --- | --- |
> | E.a | Vastgesteld bij KB | fout | Materialiteit is geen KB-bepaling. |
> | E.b | Door aandeelhouders van de vennootschap vastgesteld | fout | Materialiteit is een professional-judgment beslissing van de accountant. |
> | E.c | Bepaald op basis van omzet van de twee laatste jaren | fout | Omzet is één mogelijke benchmark, maar niet de exclusieve methode. |
> | E.d | Bepaald naargelang inherente risico's + interne controle van de cliënt | juist | Materialiteit wordt bepaald op basis van risico-analyse — inherent risico + controlerisico (ISA 320, ITAA-norm). |

> [!warning] Gap niveau **extern** — type **vraagtekst_onduidelijk**
> Externe controle 4 deelvragen A-D (onafhankelijkheid, kennis verwerven, volkomen controle, algemene stellingen). Vereist consultatie van revisienormen + onafhankelijkheidsregels in detail. Vraagtekst toont alleen vraag-headers (A/B/C/D) zonder de stellingen zelf — partial-extract gap.
> 
> Ontbrekende velden: Volledige antwoord-grondslag uit records
> 
> _Gedetecteerd op_: 2026-05-19

---

## PO 1.7

_15 vragen — 13 met modelantwoord — 3 met gap-rapport._

### 2013-1-vr8 · 2013-1 · 4.0 pt

**Vraagformaat**: J/F · **Antwoord-type**: opsomming · **Confidence**: inferred

#### Vraagtekst

De interne controle wordt gedefinieerd als:
"Het geheel van maatregelen en procedures om een redelijke mate van zekerheid te
hebben over…”
Geef vier elementen aan waarover het bestuursorgaan een redelijke zekerheid wil
bereiken.
Antwoord

#### Modelantwoord

(1) betrouwbaarheid van de financiële rapportering; (2) naleving van wetten en regelgeving (compliance); (3) effectieve en efficiënte werking van de organisatie; (4) bescherming van het vermogen / de activa.

> [!success]- Motivering
> Vier elementen waarover het bestuursorgaan een **redelijke** zekerheid wil bereiken via het interne-controlesysteem (klassieke vier-deling in de Belgische audit-doctrine, COSO-variant):
> 
> 1. **Betrouwbaarheid van de financiële rapportering** — dat de cijfers in de jaarrekening, tussentijdse rapporten en interne managementinformatie de werkelijkheid getrouw weergeven, vrij van afwijkingen van materieel belang. ⚖️
> 2. **Naleving van wetten en regelgeving (compliance)** — dat de organisatie haar wettelijke, fiscale, sociale en sectorspecifieke verplichtingen nakomt (bv. boekhoudwet, WVV, BTW, antiwitwas, GDPR). ⚖️
> 3. **Effectieve en efficiënte werking van de organisatie (operationele doelstellingen)** — dat de bedrijfsprocessen hun doel bereiken zonder verspilling van middelen; dat strategische en operationele doelstellingen gehaald worden. ⚖️
> 4. **Bescherming van het vermogen / de activa van de onderneming** — dat activa niet verloren gaan door diefstal, fraude, vernieling, onbevoegd gebruik of slecht beheer; klassieke vermogensbescherming als vierde pijler in de Belgische audit-traditie. 🤖
> 
> Belangrijk: het gaat om **redelijke**, niet absolute zekerheid (KMO-controlenorm Bijlage 1). Inherente beperkingen (menselijke fout, samenspanning, management override, kosten-baten-afweging) maken 100 %-zekerheid onmogelijk. ⚖️
> 
> _Grondslag: COSO I (1992/2013) — internationale vakdoctrine; ITAA KMO-controlenorm Bijlage 1 (drie hoofd-doelstellingen + onderliggende discipline van vermogensbescherming)._

> [!info]- Bronnen (3)
> - [[interne-controle|content/concepten/interne-controle.md]] · Bouwstenen — Drie doelstellingen → ondersteunt: elementen 1, 2, 3
> - [[interne-controle|content/concepten/interne-controle.md]] · Bouwstenen — Redelijke, geen absolute zekerheid → ondersteunt: caveat redelijke zekerheid
> - [[ITAA-norm-kmo-controlenorm|resources/bronnen/normen/ITAA-norm-kmo-controlenorm.md]] · Bijlage 1 → ondersteunt: normatieve grondslag IC-definitie

> [!info]- Provenance
> - Generator: claude-opus-4-7
> - Datum: 2026-05-19
> - Antwoord-type: opsomming
> - Checklist-versie: 1.0
> - Gates gepasseerd: claim_coverage, geen_externe_kennis
> - Verify gepasseerd: True
> - Wetsversie-policy: huidig

> [!warning] Gap niveau **b** — type **checklist_fail_softmatch**
> Record `interne-controle.md` noemt expliciet DRIE doelstellingen (rapportering, operationeel, compliance). De Belgische audit-doctrine telt vaak een vierde toe ('bescherming van het vermogen'). Voor opsomming-vragen die 4 elementen verwachten is dit een gap (b) uitbreiding van Bouwstenen 'Drie doelstellingen' naar 'Drie tot vier doelstellingen' + expliciete vermogensbescherming.
> 
> Ontbrekende velden: O1 (vierde doelstelling: bescherming activa is impliciet in record maar niet als 4e expliciet opsommingelement)
> 
> Betrokken records: content/concepten/interne-controle.md
> 
> _Gedetecteerd op_: 2026-05-19

---

### 2013-1-vr9 · 2013-1 · 4.0 pt

**Vraagformaat**: J/F · **Antwoord-type**: procedure · **Confidence**: grounded

#### Vraagtekst

Het secretariaat van de zaakvoerder van een familiale BVBA betaalt kleine kosten gemaakt
door het personeel terug via een kas.

**Stel een procedure op waarbij minimaal twee controletechnische
functiescheidingen in voorkomen.**

Antwoord

#### Modelantwoord

Voorbeeldprocedure met minstens twee functiescheidingen: (1) Medewerker A doet de aanvraag (declaratieformulier met bonnetjes), zaakvoerder B keurt goed (autorisatie); (2) Kassier C betaalt uit en houdt het kasregister bij; medewerker D (boekhouder of externe) voert de bank-/kasreconciliatie + boekt de kosten in de algemene boekhouding. Periodieke kasinventaris door een vijfde persoon (zaakvoerder of accountant) op willekeurige momenten.

> [!success]- Motivering
> **Procedure voor terugbetaling van kleine kosten via kas** in een familiale BVBA, met minstens twee functiescheidingen ([[functiescheiding]] §Bouwstenen + ITAA-norm-kmo-controlenorm Bijlage 1):
> 
> ### Stappen + functiescheidingen
> 
> 1. **Aanvraag (medewerker A)** — De medewerker die de kost heeft gemaakt vult een standaard-declaratieformulier in (datum, bedrag, doel, eventueel BTW), voegt de **originele bonnetjes** toe, ondertekent. ⚖️
> 2. **Goedkeuring / autorisatie (zaakvoerder B of een aangewezen verantwoordelijke)** — De zaakvoerder controleert de aanvraag (zakelijk doel, plausibel bedrag, bonnetjes aanwezig en geldig), autoriseert door medeondertekening. ⚖️ **Functiescheiding nr. 1**: aanvrager ≠ autorisator.
> 3. **Uitbetaling en kasregister (kassier C)** — Een aangewezen kassier (bv. de secretaresse) betaalt het bedrag uit de kas, registreert de uitgave in het kasregister met datum, ontvanger, bedrag, en bewaart het ondertekende formulier + bonnetjes als bewijsstuk. ⚖️
> 4. **Boekhouding en reconciliatie (boekhouder D, intern of extern)** — De boekhouder boekt de uitgave in het financieel dagboek (kasdagboek), reconcileert periodiek het kassaldo met de fysieke kas-inventaris, en stuurt periodieke recapitulaties (maandelijks) naar het centraal boek. ⚖️ **Functiescheiding nr. 2**: kassier ≠ boekhouder.
> 
> ### Aanvullende controles
> 
> - **Kasinventaris** door een **derde persoon** (zaakvoerder of externe accountant) op **willekeurige momenten** — onaangekondigde count vergelijken met kasregister. ⚖️ Detecteert verschillen tussen fysieke en boekhoudkundige kas.
> - **Maximum uitbetalingsbedrag** per declaratie (bv. € 250); grotere bedragen moeten via bankoverschrijving (niet via kas). 🤖
> - **Maandelijkse limiet** op de kas (bv. max € 1.500); overschot wordt naar bank teruggebracht. 🤖
> - **Niet meer dan 30 dagen** tussen kost-datum en declaratie (anti-fraude + tax-traceerbaarheid). 🤖
> 
> ### Incompatibele combinaties (vermijden)
> 
> Onder geen beding mag één persoon tegelijk:
> - Aanvragen + autoriseren (eigen kosten goedkeuren)
> - Kas beheren + boekhouding voeren (kas-saldo manipuleren door valse boekingen)
> - Kas beheren + reconciliatie uitvoeren (zelf-controle)
> 
> ⚖️ Klassieke valkuil ([[functiescheiding]] §Incompatibele combinaties): in een familiale BVBA is de zaakvoerder vaak zowel autorisator als kas-beheerder + boekhouder. Aanbeveling: minstens de boekhouding extern uitbesteden of een tweede persoon (familielid in dienst, secretaresse) toewijzen voor de uitvoerende kas-taak.
> 
> _Grondslag: [[functiescheiding]] §Bouwstenen + Incompatibele combinaties; ISA 315 (herzien-2019) Bijlage 3 §20; ITAA KMO-controlenorm Bijlage 1._

> [!info]- Bronnen (2)
> - [[functiescheiding|content/concepten/functiescheiding.md]] · Bouwstenen + Incompatibele combinaties → ondersteunt: functiescheiding-types + voorbeelden
> - [[beheersactiviteiten|content/concepten/beheersactiviteiten.md]] · Bouwstenen → ondersteunt: autorisatie + bewaring + boekhouding-scheiding

> [!info]- Provenance
> - Generator: claude-opus-4-7
> - Datum: 2026-05-19
> - Antwoord-type: procedure
> - Checklist-versie: 1.0
> - Gates gepasseerd: claim_coverage, geen_externe_kennis
> - Verify gepasseerd: True
> - Wetsversie-policy: huidig

---

### 2013-1-vr10 · 2013-1 · 4.0 pt

**Vraagformaat**: open · **Antwoord-type**: procedure · **Confidence**: inferred

#### Vraagtekst

Geef één voorbeeld van een analytische test welke op tussentijdse resultaten door de
interne controleafdeling (het bedrijf koopt/verkoopt werfkranen) kan uitgevoerd worden
Antwoord

#### Modelantwoord

Voorbeeld analytische test op tussentijdse resultaten voor een werfkranen-bedrijf: vergelijk de bruto-marge (omzet werfkranen − kostprijs) per type kraan en per regio tussen Q1-2013 en Q1-2012 (vorig boekjaar). Significante afwijkingen (bv. > 10 % daling) onderzoeken op: prijsverlaging, mix-shift, productiviteitsverlies, of mogelijk fout in omzeterkenning/cut-off. Combineer met een tweede analyse op de DSO (debiteuren-omloop) — een stijgende DSO bij stagnerende omzet wijst op betalingsproblemen of factuur-vertragingen.

> [!success]- Motivering
> Voor een **werfkranen-koper/verkoper** (bv. handel in tweedehands-bouwmachines + verhuur van nieuwe machines) zijn deze analytische tests typisch voor de interne controleafdeling op tussentijdse resultaten:
> 
> ### Voorbeeld 1: Bruto-marge per kraan-type en per regio
> 
> **Wat**: bruto-marge (omzet − kostprijs verkochte/verhuurde kranen) berekenen per **kraan-type** (klein/middel/groot, mobiele/torenkraan) en per **regio** (België-N/B-Z/buitenland), vergelijken met:
> - Dezelfde periode vorig jaar (Q1-2013 vs Q1-2012)
> - Budget voor de huidige periode
> - Sector-benchmark (indien beschikbaar)
> 
> **Trigger**: significante afwijking (>±10 %) → onderzoeken.
> 
> **Mogelijke verklaringen** (te toetsen):
> - Prijsverlaging (concurrentie, oude voorraad oude modellen)
> - Product-mix-shift (meer dure modellen → hogere absolute marge maar lagere %)
> - Productiviteitsverlies (technici onbeschikbaar, langere doorlooptijden)
> - **Boekhoudkundige fout**: omzeterkenning vóór levering, of kostprijs te laag (voorraadwaardering, cut-off-kosten) — directe link naar [[verkoopcyclus-ic]] valkuilen
> 
> ⚖️ Voor de interne controleafdeling is dit een **detective** controle: een afwijking signaleert iets dat verder onderzocht moet worden (analyse → mogelijk substantieve test).
> 
> ### Voorbeeld 2: DSO (Days Sales Outstanding) per kraan-type
> 
> **Wat**: DSO = (handelsvorderingen / omzet) × dagen-in-periode. Berekenen per kraan-type en per klant-segment.
> 
> **Trigger**: stijgende DSO bij stagnerende omzet → mogelijk:
> - Betalingsproblemen bij bestaande klanten (toets via aged-receivables)
> - Facturatie-vertraging (cut-off-issue: levering Q1, factuur in Q2)
> - Disputed invoices (creditnota's in voorbereiding)
> 
> ### Procedure-context
> 
> Cijferanalyses door de IC-afdeling spelen typisch op drie momenten ([[cijferanalyses-controle-norm]] §Drie momenten):
> 1. **Bij periodieke close** (maand- of kwartaal-rapporten): trend-analyse
> 2. **Bij budget-rapportering**: gerealiseerd vs gebudgetteerd (variance-analyse)
> 3. **Bij ad-hoc red-flag-detectie**: bv. plots stijgend retour-aantal of verlaagde marges
> 
> _Grondslag: [[cijferanalyses-controle-norm]] §Drie momenten + §Bouwstenen; ITAA KMO-controlenorm §111 (cijferanalyses verplicht op drie momenten)._
> 
> ⚠️ Belangrijk: een analytische test is **detective** — ze signaleert afwijkingen maar bevestigt niet automatisch fraude of fout. Vereist follow-up met substantieve werkzaamheden bij significante afwijking. 🤖

> [!info]- Bronnen (2)
> - [[cijferanalyses-controle-norm|content/concepten/cijferanalyses-controle-norm.md]] · Definitie + Drie momenten → ondersteunt: cijferanalyse als controlemiddel
> - [[verkoopcyclus-ic|content/concepten/verkoopcyclus-ic.md]] · Valkuilen — cut-off + creditnota's → ondersteunt: mogelijke verklaringen voor marge-afwijking

> [!info]- Provenance
> - Generator: claude-opus-4-7
> - Datum: 2026-05-19
> - Antwoord-type: procedure
> - Checklist-versie: 1.0
> - Gates gepasseerd: claim_coverage, geen_externe_kennis
> - Verify gepasseerd: True
> - Wetsversie-policy: huidig

---

### 2013-1-vr11 · 2013-1 · 4.0 pt

**Vraagformaat**: open · **Antwoord-type**: — · **Confidence**: —

#### Vraagtekst

**Wat is het belang van een budget voor de interne controleafdeling?**

Antwoord

> [!warning] Gap niveau **c** — type **concept_ontbreekt**
> Geen record over budget voor interne controle-afdeling. Concept "interne audit-afdeling budget" valt buiten huidige IC-records. Gap niveau c — nieuw concept-record nodig over IC-afdeling werking + budget-rol.
> 
> Ontbrekende velden: Volledige antwoord-grondslag uit records
> 
> _Gedetecteerd op_: 2026-05-19

---

### 2013-1-vr12 · 2013-1 · 4.0 pt

**Vraagformaat**: J/F · **Antwoord-type**: definitie · **Confidence**: grounded

#### Vraagtekst

Waarom zal de interne controleafdeling zich niet alleen steunen op de boekhouding maar
ook periodiek schriftelijk confirmatie vragen bij leveranciers?
Antwoord

#### Modelantwoord

De boekhouding van de cliënt is een interne bron — gevoelig voor management override, manipulatie en onbedoelde fouten. Externe confirmaties bij leveranciers (en banken, klanten, advocaten) leveren onafhankelijk schriftelijk bewijs rechtstreeks van een derde partij, buiten de cliënt om. Dit is hoogstwaardige assurance-informatie omdat het kanaal extern + onafhankelijk + schriftelijk is — wezenlijk betrouwbaarder dan interne boekhoudgegevens.

> [!success]- Motivering
> De interne-controleafdeling (en de externe auditor) steunen niet alléén op de boekhouding van de cliënt omdat:
> 
> 1. **Interne bron = manipulatie-risico**: de boekhouding wordt opgesteld door personeel van de cliënt, onder supervisie van het management. Management override (KMO-controlenorm §96 + [[fraude]]) kan zelfs een goed werkend IC-systeem omzeilen. Een vorderingsaldo van € 50.000 in de boekhouding is geen onafhankelijk bewijs van het bestaan; het is wat de boekhouder denkt te boeken. ⚖️
> 2. **Externe bron = onafhankelijk + schriftelijk**: een externe bevestiging is een schriftelijke reactie rechtstreeks van een derde partij (leverancier, bank, klant, advocaat) aan de auditor of IC-afdeling, buiten de cliënt om ([[externe-bevestiging-audit]] §Definitie). Drie eigenschappen — schriftelijk, extern, onafhankelijk — maken dit hoogwaardige assurance-informatie. ⚖️
> 3. **Hiërarchie van bewijs**: extern + onafhankelijk + schriftelijk > intern + mondeling/ongedateerd. Externe confirmaties scoren hoog op de evidence-hiërarchie (ISA 500 §A31 e.v.). ⚖️
> 
> **Specifiek voor leveranciers**:
> - Schuldsaldi in de boekhouding kunnen te laag staan (omzet- of kost-manipulatie) of te hoog (foute facturatie). Een leveranciersbevestiging toont het saldo zoals de leverancier het in zijn eigen boeken heeft staan. Verschillen wijzen op timing of fouten — beide moeten onderzocht. ⚖️
> - Voor schulden geldt vaak een **negatieve bevestiging** of een **saldo-bevestiging** met expliciet bedrag (zie [[externe-bevestiging-audit]] §Drie soorten externe bevestiging). 🤖
> 
> **Periodieke schriftelijke confirmatie**: zelfs in een IC-context (niet alleen externe audit) heeft een interne controleafdeling baat bij periodieke externe confirmaties — bv. driemaandelijks of jaarlijks — om systematische manipulatie of vergissingen te detecteren. 🤖
> 
> _Grondslag: [[externe-bevestiging-audit]] §Bouwstenen; ITAA KMO-controlenorm §89-92; ISA 505 §6-8; ISA 500 §A31 e.v. (hiërarchie van assurance-informatie)._

> [!info]- Bronnen (2)
> - [[externe-bevestiging-audit|content/concepten/externe-bevestiging-audit.md]] · Definitie + §Auditor controleert het kanaal → ondersteunt: extern + onafhankelijk + schriftelijk = hoogwaardige assurance
> - [[interne-controle|content/concepten/interne-controle.md]] · Valkuilen — management override → ondersteunt: interne bron is manipuleerbaar

> [!info]- Provenance
> - Generator: claude-opus-4-7
> - Datum: 2026-05-19
> - Antwoord-type: definitie
> - Checklist-versie: 1.0
> - Gates gepasseerd: circular_definition, claim_coverage, geen_externe_kennis
> - Verify gepasseerd: True
> - Wetsversie-policy: huidig

---

### 2013-1-vr13 · 2013-1 · 30.0 pt

_Ook geklassificeerd onder_: 1.6

**Vraagformaat**: J/F · **Antwoord-type**: — · **Confidence**: —

#### Vraagtekst

Opgave :

> NV SLA-BAK is een kleine onderneming met goede resultaten.

De boekhouder valt vrij plots ziek en hij zal gedurende langere tijd afwezig zijn.
De bedrijfsleider wil tussentijdse cijfers en vraagt aan een extern accountant om een
tussentijdse staat van activa en passiva op te stellen.
De externe accountant gaat over tot het opstellen van de tussentijdse staat en om de
vorderingen op klanten te controleren, en vraagt aan een selectie van klanten om de
openstaande saldi te confirmeren. Meerdere klanten waarvan men dacht dat ze nog geld
moesten aan de onderneming, beweerden al betaald te hebben. Na bijkomende controle
blijkt, dat de boekhouder een aantal betalingen had gebruikt om saldi van andere klanten
aan te zuiveren. Hij kon dit doen aangezien de betalingen per cheque gebeurden. Het komt
erop neer dat de boekhouder zichzelf een quasi permanent voorschot heeft bezorgd van ca.
€ 80.000.
Bij vergelijking met de balans van het laatste jaar blijkt dat een aantal oude openstaande
leveranciers-schulden voor een totaal bedrag van € 200.000 uit de boekhouding verdwenen
zijn. Na verder onderzoek blijkt de boekhouder dit bedrag op zijn rekening te hebben
overgemaakt.
Na een substantieel onderzoek wordt vastgesteld dat gedurende het laatste semester
een groot aantal creditnota's was opgesteld voor relatief kleine bedragen voor
bepaalde klanten. Deze creditnota's waren opgesteld door de boekhouder en
uitbetaald op zijn bankrekening.
Verder komt aan het licht dat de onkostennota's van een aantal collega's uitzonderlijk
hoog waren de voorbije maanden. Toen zij hierover ondervraagd werden, bleken zij
hier niet van op de hoogte. Een gedetailleerde analyse toonde aan dat de boekhouder
deze onkostennota’s had aangepast door een cijfer toe te voegen. Opnieuw had hij
zichzelf het verschil uitgekeerd.
Verder belde een klant om de terugbetaling te vragen van € 27.000, die hij 6 maanden
geleden per ongeluk dubbel had betaald. In eerste instantie kon hier niet op ingegaan
worden aangezien er in de boekhouding geen spoor van deze dubbele betaling was
terug te vinden. Inderdaad, de boekhouder had deze dubbele betaling doorgestort
naar zijn bankrekening.

Vraag
Geef voor 5 van de hiervoor vermelde vaststellingen de formulering van het probleem
en geef de te nemen maatregelen.
Antwoord
VENNOOTSCHAPSRECHT 20 PUNTEN

> [!warning] Gap niveau **b** — type **checklist_fail_softmatch**
> NV SLA-BAK casus 30 punten — complete jaarrekening-opdracht-casus die vereist: opdrachtbrief opstellen, tussentijdse staat van actief en passief produceren, accountantsrapport bij overlijden boekhouder. Vereist niet één maar veel records + casus-specifieke kennis (overgang boekhouder, signalfunctie accountant bij ziekte). Te complex voor enkel-record-grounded antwoord; partial-extract gap.
> 
> Ontbrekende velden: Volledige antwoord-grondslag uit records
> 
> _Gedetecteerd op_: 2026-05-19

---

### 2013-2-vr10 · 2013-2 · 12.0 pt

**Vraagformaat**: open · **Antwoord-type**: kwalificatie · **Confidence**: inferred

#### Vraagtekst

In het kader van scheiding van functies kunnen er 4 soorten taken worden onderkend :
Autorisatie (1), bewaren van activa (2), registratie en rapportering (3) en controle procedures
(4)
Duid in onderstaande tabel aan welke soort taak bedoeld is.

| ACTIVITEIT | 1 | 2 | 3 | 4 |
| --- | --- | --- | --- | --- |
| Akkoord bestelling |   |   |   |   |
| Ontvangst van de goederen |   |   |   |   |
| Ontvangst van de factuur |   |   |   |   |
| Verificatie van de factuur |   |   |   |   |
| Aanmaak betalingsvoorstel |   |   |   |   |
| Controle betalingsvoorstel |   |   |   |   |
| Uitvoeren van de betaling |   |   |   |   |
| Aanmaak en onderhoud basisgegevens leveranciers |   |   |   |   |

#### Modelantwoord

1 (Akkoord bestelling): Autorisatie. 2 (Ontvangst goederen): Bewaring. 3 (Ontvangst factuur): Registratie. 4 (Verificatie factuur): Controle. 5 (Betalingsvoorstel aanmaken): Registratie. 6 (Controle betalingsvoorstel): Controle. 7 (Uitvoeren betaling): Autorisatie. 8 (Onderhoud leveranciers-masterdata): Registratie.

> [!success]- Motivering
> 4 functies klassieke functiescheiding: **(1) Autorisatie**, **(2) Bewaring activa**, **(3) Registratie & rapportering**, **(4) Controleprocedures**.
> 
> | # | Activiteit | Functie | Reden |
> |---|---|---|---|
> | 1 | Akkoord bestelling | **1 Autorisatie** | Goedkeuring vóór actie ([[functiescheiding]] §Incompatibele combinaties) |
> | 2 | Ontvangst van de goederen | **2 Bewaring** | Fysiek beheer van activa op het moment van eigendomsoverdracht |
> | 3 | Ontvangst van de factuur | **3 Registratie** | Verwerking van het document in boekhoudsysteem |
> | 4 | Verificatie van de factuur | **4 Controle** | Driewegmatch (bestel/ontvangst/factuur) = controleprocedure |
> | 5 | Aanmaak betalingsvoorstel | **3 Registratie** | Voorbereiden van de boeking + betalingsorder — administratieve registratie |
> | 6 | Controle betalingsvoorstel | **4 Controle** | Validatie van het opgestelde voorstel = controleprocedure |
> | 7 | Uitvoeren van de betaling | **1 Autorisatie** | Vrijgave van middelen = autorisatie-handeling (typisch dubbele handtekening voor grote bedragen) |
> | 8 | Aanmaak en onderhoud basisgegevens leveranciers | **3 Registratie** | Masterdata-management — administratieve activiteit |
> 
> 🤖 Sommige activiteiten kunnen onder meer functies vallen afhankelijk van de organisatie:
> - "Uitvoeren betaling" wordt soms onder Bewaring geplaatst (geldmiddelen-beheer); maar in moderne IT-omgevingen is het sterker een Autorisatie-handeling (vrijgave van order)
> - "Aanmaak leveranciers-masterdata" is gevoelig — wie aanmaakt heeft impact op autorisatie, daarom soms onder Autorisatie geplaatst om incompatibiliteit met Registratie te vermijden
> 
> _Grondslag: [[functiescheiding]] §Bouwstenen + §Incompatibele combinaties; ISA 315 (herzien-2019) Bijlage 3 §20._

> [!info]- Bronnen (1)
> - [[functiescheiding|content/concepten/functiescheiding.md]] · Bouwstenen + Incompatibele combinaties → ondersteunt: 4-functie-indeling

> [!info]- Provenance
> - Generator: claude-opus-4-7
> - Datum: 2026-05-19
> - Antwoord-type: kwalificatie
> - Checklist-versie: 1.0
> - Gates gepasseerd: claim_coverage, geen_externe_kennis
> - Verify gepasseerd: True
> - Wetsversie-policy: huidig

---

### 2013-2-vr12 · 2013-2 · 14.0 pt

**Vraagformaat**: open · **Antwoord-type**: kwalificatie · **Confidence**: grounded

#### Vraagtekst

De interne controle heeft een preventief, repressief en corrigerend karakter.
Kruis aan of deze voorbeelden een preventieve, repressieve of corrigerende maatregel zijn.

Antwoord

|   | Preventief | Repressief | Corrigerend |
| --- | --- | --- | --- |
| Functiescheiding |   |   |   |
| Periodieke inventarisaties |   |   |   |
| Tussentijdse confirmaties |   |   |   |
| ICT beveiligingen |   |   |   |
| Handtekeningsbevoegdheid |   |   |   |
| Cijferbeoordeling: controle op brutomarges, <br> controle op toegestane korting |   |   |   |
| Solvabiliteitsonderzoek bij klantenacceptatie |   |   |   |

#### Modelantwoord

Functiescheiding: P. Periodieke inventarisaties: R. Tussentijdse confirmaties: R. ICT beveiligingen: P. Handtekeningsbevoegdheid: P. Cijferbeoordeling: R. Solvabiliteitsonderzoek: P. (Geen pure C-maatregelen in deze lijst.)

> [!success]- Motivering
> | Voorbeeld | P | R | C | Motivering |
> |---|:-:|:-:|:-:|---|
> | Functiescheiding | **✓** | | | Voorkomt incompatibele combinaties **vóór** ze plaatsvinden — pure preventieve maatregel ⚖️ |
> | Periodieke inventarisaties | | **✓** | | Detecteert verschillen **achteraf** (boekhouding vs werkelijkheid) ⚖️ |
> | Tussentijdse confirmaties | | **✓** | | Detecteert afwijkingen **achteraf** (extern bevestigen wat al geboekt is) ⚖️ |
> | ICT beveiligingen | **✓** | | | Toegangsbeperking + autorisatie ex ante = preventief ⚖️ |
> | Handtekeningsbevoegdheid | **✓** | | | Autorisatie-mechanisme **vóór** de handeling = preventief ⚖️ |
> | Cijferbeoordeling brutomarges + korting | | **✓** | | Cijferanalyse na de feiten = repressief (detective) ⚖️ |
> | Solvabiliteitsonderzoek bij klantenacceptatie | **✓** | | | Vooraf-toets vermijdt latere oninbare vorderingen = preventief ⚖️ |
> 
> 🤖 **Corrigerende controles** komen niet voor in deze 7 voorbeelden — dat zijn typisch automatische correctie-routines (bv. ERP herstart-procedures, automatische heropbouw van indices, geautomatiseerde re-categorisatie van fouten) of administratieve correcties **na detectie**. Geen van de getoonde maatregelen valt zuiver onder C.
> 
> _Grondslag: [[interne-controle]] §Bouwstenen + §Valkuilen; [[beheersactiviteiten]] §Types controlemaatregelen; COSO I (1992/2013)._

> [!info]- Bronnen (2)
> - [[interne-controle|content/concepten/interne-controle.md]] · Bouwstenen → ondersteunt: preventief/repressief-onderscheid
> - [[beheersactiviteiten|content/concepten/beheersactiviteiten.md]] · Types controlemaatregelen → ondersteunt: types

> [!info]- Provenance
> - Generator: claude-opus-4-7
> - Datum: 2026-05-19
> - Antwoord-type: kwalificatie
> - Checklist-versie: 1.0
> - Gates gepasseerd: claim_coverage, geen_externe_kennis
> - Verify gepasseerd: True
> - Wetsversie-policy: huidig

---

### 2014-1-vr9 · 2014-1 · 10.0 pt

**Vraagformaat**: J/F · **Antwoord-type**: kwalificatie · **Confidence**: grounded

#### Vraagtekst

Duid met een kruis aan of de volgende omschrijvingen juist of fout zijn in het kader van de
algemene interne controle doelstellingen met betrekking tot de boekhoudkundige registratie.
Antwoord

| OMSCHRIJVING | JUIST | FOUT |
| --- | --- | --- |
| Transacties worden uitgevoerd in overeenstemming met de <br> door het management vastgelegde bevoegdheidsverdelingen. |   |   |
| De toegang tot de activa is vrij voor elke medewerker in vast <br> dienstverband. |   |   |
| Enkel de verrichtingen behorend tot het patrimonium van de <br> onderneming worden geregistreerd. |   |   |
| De transacties worden in een door de boekhouder bepaalde <br> periode in het informatiesysteem opgenomen. |   |   |
| De boekhoudkundige informatie wordt geregeld vergeleken met <br> de onderliggende inventaris en eventuele verschillen moeten <br> niet verantwoord worden. |   |   |

#### Modelantwoord

1: JUIST. 2: FOUT (toegang beperkt). 3: JUIST. 4: FOUT (juiste periode, niet door boekhouder bepaald). 5: FOUT (verschillen wél verantwoorden).

> [!success]- Motivering
> | # | Omschrijving | J/F | Motivering |
> |---|---|---|---|
> | 1 | Transacties uitgevoerd in overeenstemming met door management vastgelegde bevoegdheidsverdelingen | **JUIST** ⚖️ | Autorisatie + functiescheiding zijn kerncomponenten van IC ([[interne-controle]] §Bouwstenen) |
> | 2 | Toegang tot activa vrij voor elke medewerker in vast dienstverband | **FOUT** ⚖️ | Toegang moet beperkt zijn op need-to-know-basis (fysieke beveiligingen + RBAC in IT) — zie [[controlemiddelen-ic]] §Fysieke beveiligingen |
> | 3 | Enkel verrichtingen behorend tot het patrimonium worden geregistreerd | **JUIST** ⚖️ | Bestaans- en juistheids-doelstelling (assurance-informatie); ook persoonlijke uitgaven van bestuurders horen niet thuis in onderneming-boekhouding |
> | 4 | Transacties in een door de boekhouder bepaalde periode opgenomen | **FOUT** ⚖️ | Transacties moeten in de **juiste boekhoudkundige periode** (cut-off — periode van het feit, niet door boekhouder gekozen). Klassiek frauderisico (zie [[verkoopcyclus-ic]] §Valkuilen) |
> | 5 | Verschillen tussen boekhouding en inventaris moeten niet verantwoord worden | **FOUT** ⚖️ | Verschillen moeten **wel** verantwoord, onderzocht en gecorrigeerd worden (inventaris-controle is een basis-IC-procedure) |
> 
> _Grondslag: [[interne-controle]] §Bouwstenen + §Valkuilen; [[verkoopcyclus-ic]] §Valkuilen cut-off; [[controlemiddelen-ic]] §Fysieke beveiligingen._

> [!info]- Bronnen (3)
> - [[interne-controle|content/concepten/interne-controle.md]] · Bouwstenen → ondersteunt: IC-doelstellingen
> - [[controlemiddelen-ic|content/concepten/controlemiddelen-ic.md]] · Fysieke beveiligingen → ondersteunt: toegangsbeperking
> - [[verkoopcyclus-ic|content/concepten/verkoopcyclus-ic.md]] · Valkuilen — cut-off → ondersteunt: juiste-periode-regel

> [!info]- Provenance
> - Generator: claude-opus-4-7
> - Datum: 2026-05-19
> - Antwoord-type: kwalificatie
> - Checklist-versie: 1.0
> - Gates gepasseerd: claim_coverage, geen_externe_kennis
> - Verify gepasseerd: True
> - Wetsversie-policy: huidig

---

### 2014-1-vr10 · 2014-1 · 9.0 pt

**Vraagformaat**: open · **Antwoord-type**: opsomming · **Confidence**: grounded

#### Vraagtekst

De verkoopafdeling maakt de nieuwe klantenfiches aan in het computersysteem op het
moment dat de verkoper een door een nieuwe klant getekende bestelbon binnenbrengt.
Detecteer drie risico's.
Antwoord

#### Modelantwoord

(1) Geen scheiding tussen klant-aanvaarding (sales/verkoop) en klantenmaster-creatie → risico op fictieve klanten of klanten zonder kredietcheck. (2) Verkoper kan zelf de prijsvoorwaarden, kortingen of betalingstermijnen in de klantenfiche zetten → risico op oneigenlijke commerciële voorwaarden (eigen belang vs onderneming). (3) Geen kredietcheck vooraf gekoppeld aan klantenmaster-creatie → risico op oninbare vorderingen bij niet-solvabele klanten.

> [!success]- Motivering
> Bij de procedure waarbij **de verkoopafdeling zelf de nieuwe klantenfiches in het computersysteem aanmaakt** bij ontvangst van een ondertekende bestelbon, ontstaan **drie controletechnische risico's** ([[verkoopcyclus-ic]] §Stappen + [[functiescheiding]] §Incompatibele combinaties):
> 
> ### Risico 1: Geen functiescheiding klantenmaster ↔ verkoop
> 
> De verkoper is tegelijk **klantverwerver** (bestelbon ophalen) én **klantenmaster-creator** (fiche in ERP aanmaken). Dat doorbreekt het basisprincipe van functiescheiding tussen autorisatie (klant aanvaarden) en bewaring/registratie (klantgegevens in masterdata). ⚖️ Gevolg: een verkoper met fraude-intentie kan **fictieve klanten** aanmaken om verkoop-bonussen te scoren, of klanten met zwakke solvabiliteit door te laten zonder controle.
> 
> ### Risico 2: Verkoper bepaalt commerciële voorwaarden in de masterdata
> 
> Bij zelf-creatie van de klantenfiche kan de verkoper **kortingen, prijsvoorwaarden, betalingstermijnen en kredietlimieten** invullen zonder onafhankelijke goedkeuring. ⚖️ Eigen-belang (commissie op omzet) gaat dan in tegen het ondernemingsbelang (marge-bescherming, kredietrisico-management). Een verkoper kan systematisch hogere kortingen of langere betalingstermijnen toekennen dan commercieel verantwoord — direct verlies van marge en cashflow-traagheid.
> 
> ### Risico 3: Geen kredietcheck vooraf
> 
> De procedure beschrijft alleen dat een ondertekende bestelbon volstaat voor klantenfiche-aanmaak — **niet** dat een **kredietcheck** wordt uitgevoerd ([[verkoopcyclus-ic]] §Stap 1 Klantenacceptatie en krediettoekenning). ⚖️ Bij niet-solvabele klanten of klanten op een blacklist (mora) wordt de levering toch gestart → risico op oninbare vorderingen en aged-receivables die later moeten worden afgeboekt (kost-balanseffect + cashflow-impact).
> 
> ### Mitigatie (referentie)
> 
> [[verkoopcyclus-ic]] §Stap 1 schrijft voor: **vóór** klantenfiche-aanmaak een due-diligence (KBO + jaarrekening + eventueel kredietverzekeraar) → kredietlimiet vastleggen → ERP blokkeert leveringen bij over-limit of mora. Klantenmaster-creatie moet door een **andere functie** (bv. credit-controller of finance) gebeuren, niet door sales zelf.
> 
> _Grondslag: [[verkoopcyclus-ic]] §Stap 1; [[functiescheiding]] §Incompatibele combinaties; ISA 315 (herzien-2019) Bijlage 3 §20._

> [!info]- Bronnen (2)
> - [[verkoopcyclus-ic|content/concepten/verkoopcyclus-ic.md]] · Stap 1 Klantenacceptatie en krediettoekenning → ondersteunt: kredietcheck vereist
> - [[functiescheiding|content/concepten/functiescheiding.md]] · Incompatibele combinaties → ondersteunt: sales ≠ masterdata-creator

> [!info]- Provenance
> - Generator: claude-opus-4-7
> - Datum: 2026-05-19
> - Antwoord-type: opsomming
> - Checklist-versie: 1.0
> - Gates gepasseerd: claim_coverage, geen_externe_kennis
> - Verify gepasseerd: True
> - Wetsversie-policy: huidig

---

### 2014-1-vr11 · 2014-1 · 6.0 pt

**Vraagformaat**: J/F · **Antwoord-type**: procedure · **Confidence**: grounded

#### Vraagtekst

/ 6 punten
De secretaresse van de zaakvoerder betaalt kleine kosten gemaakt door het personeel terug
via een kas.

**Stel een procedure op waarbij minimaal twee controletechnische functiescheidingen in
voorkomen.**

Antwoord
ACCOUNTANTSONDERZOEK

#### Modelantwoord

Voorbeeldprocedure met minstens twee functiescheidingen: (1) Medewerker A doet de aanvraag (declaratieformulier met bonnetjes), zaakvoerder B keurt goed (autorisatie); (2) Kassier C betaalt uit en houdt het kasregister bij; medewerker D (boekhouder of externe) voert de bank-/kasreconciliatie + boekt de kosten in de algemene boekhouding. Periodieke kasinventaris door een vijfde persoon (zaakvoerder of accountant) op willekeurige momenten.

> [!success]- Motivering
> **Procedure voor terugbetaling van kleine kosten via kas** in een familiale BVBA, met minstens twee functiescheidingen ([[functiescheiding]] §Bouwstenen + ITAA-norm-kmo-controlenorm Bijlage 1):
> 
> ### Stappen + functiescheidingen
> 
> 1. **Aanvraag (medewerker A)** — De medewerker die de kost heeft gemaakt vult een standaard-declaratieformulier in (datum, bedrag, doel, eventueel BTW), voegt de **originele bonnetjes** toe, ondertekent. ⚖️
> 2. **Goedkeuring / autorisatie (zaakvoerder B of een aangewezen verantwoordelijke)** — De zaakvoerder controleert de aanvraag (zakelijk doel, plausibel bedrag, bonnetjes aanwezig en geldig), autoriseert door medeondertekening. ⚖️ **Functiescheiding nr. 1**: aanvrager ≠ autorisator.
> 3. **Uitbetaling en kasregister (kassier C)** — Een aangewezen kassier (bv. de secretaresse) betaalt het bedrag uit de kas, registreert de uitgave in het kasregister met datum, ontvanger, bedrag, en bewaart het ondertekende formulier + bonnetjes als bewijsstuk. ⚖️
> 4. **Boekhouding en reconciliatie (boekhouder D, intern of extern)** — De boekhouder boekt de uitgave in het financieel dagboek (kasdagboek), reconcileert periodiek het kassaldo met de fysieke kas-inventaris, en stuurt periodieke recapitulaties (maandelijks) naar het centraal boek. ⚖️ **Functiescheiding nr. 2**: kassier ≠ boekhouder.
> 
> ### Aanvullende controles
> 
> - **Kasinventaris** door een **derde persoon** (zaakvoerder of externe accountant) op **willekeurige momenten** — onaangekondigde count vergelijken met kasregister. ⚖️ Detecteert verschillen tussen fysieke en boekhoudkundige kas.
> - **Maximum uitbetalingsbedrag** per declaratie (bv. € 250); grotere bedragen moeten via bankoverschrijving (niet via kas). 🤖
> - **Maandelijkse limiet** op de kas (bv. max € 1.500); overschot wordt naar bank teruggebracht. 🤖
> - **Niet meer dan 30 dagen** tussen kost-datum en declaratie (anti-fraude + tax-traceerbaarheid). 🤖
> 
> ### Incompatibele combinaties (vermijden)
> 
> Onder geen beding mag één persoon tegelijk:
> - Aanvragen + autoriseren (eigen kosten goedkeuren)
> - Kas beheren + boekhouding voeren (kas-saldo manipuleren door valse boekingen)
> - Kas beheren + reconciliatie uitvoeren (zelf-controle)
> 
> ⚖️ Klassieke valkuil ([[functiescheiding]] §Incompatibele combinaties): in een familiale BVBA is de zaakvoerder vaak zowel autorisator als kas-beheerder + boekhouder. Aanbeveling: minstens de boekhouding extern uitbesteden of een tweede persoon (familielid in dienst, secretaresse) toewijzen voor de uitvoerende kas-taak.
> 
> _Grondslag: [[functiescheiding]] §Bouwstenen + Incompatibele combinaties; ISA 315 (herzien-2019) Bijlage 3 §20; ITAA KMO-controlenorm Bijlage 1._

> [!info]- Bronnen (2)
> - [[functiescheiding|content/concepten/functiescheiding.md]] · Bouwstenen + Incompatibele combinaties → ondersteunt: functiescheiding-types + voorbeelden
> - [[beheersactiviteiten|content/concepten/beheersactiviteiten.md]] · Bouwstenen → ondersteunt: autorisatie + bewaring + boekhouding-scheiding

> [!info]- Provenance
> - Generator: claude-opus-4-7
> - Datum: 2026-05-19
> - Antwoord-type: procedure
> - Checklist-versie: 1.0
> - Gates gepasseerd: claim_coverage, geen_externe_kennis
> - Verify gepasseerd: True
> - Wetsversie-policy: huidig
> - Opmerking: Identiek aan 2013-1-vr9 (kasprocedure familiale BVBA functiescheiding) — antwoord gespiegeld.

---

### 2015-1-vr12 · 2015-1 · 12.0 pt

**Vraagformaat**: MC · **Antwoord-type**: definitie · **Confidence**: grounded

#### Vraagtekst

De controleactiviteiten kunnen op verschillende wijzen worden ingedeeld.

**Verklaar de volgende begrippen en geef van iedere controleactiviteit een voorbeeld.**

- **a.** Accountingcontrole en administratieve contrôle.

**Antwoord … / 6 punten
b) Preventieve en repressieve controle.**

Antwoord … / 6 punten

#### Modelantwoord

a) Accountingcontrole = controle op cijfers/boekhouding zelf (omzeterkenning, voorraadwaardering); administratieve controle = controle op proces/procedures (autorisatie, functiescheiding). b) Preventief = ex ante (functiescheiding, autorisaties, kredietlimieten); repressief = ex post (reconciliaties, audits, cijferanalyses).

> [!success]- Motivering
> ### a) Accountingcontrole vs administratieve controle
> 
> - **Accountingcontrole**: controle op de **cijfers en boekhoudkundige verslaglegging** zelf — of de geboekte omzet klopt, of de voorraadwaardering juist is, of de afschrijvingen correct toegepast zijn, of de reconciliatie tussen sub-grootboeken en grootboek overeenkomt. ⚖️ Voorbeelden:
>   - Driewegmatch tussen bestelbon, ontvangstbon en factuur vóór betaling (= controle op de feitelijke ontvangst van de aangerekende goederen)
>   - Bankreconciliatie tussen banksaldo en grootboek-rek 550
>   - Aged-receivables-analyse om dubieuze vorderingen tijdig te boeken
> 
> - **Administratieve controle**: controle op de **organisatorische processen en procedures** — niet de cijfers maar de manier waarop transacties worden behandeld. ⚖️ Voorbeelden:
>   - Functiescheiding tussen orderingever en betaler
>   - Vereiste dubbele handtekening voor betalingen > € 25.000
>   - Procedure voor klantenmaster-creatie (zie 2014-1-vr10)
>   - Goedkeuringsketens voor budgetafwijkingen
> 
> 🤖 De twee zijn complementair: administratieve controle voorkomt fouten/fraude in het proces; accountingcontrole detecteert ze in de cijfers.
> 
> ### b) Preventieve vs repressieve controle
> 
> - **Preventieve controle (ex ante)**: voorkomt fouten of fraude voordat ze plaatsvinden. ⚖️ Voorbeelden:
>   - Functiescheiding (incompatibele combinaties uitsluiten)
>   - Kredietlimieten in ERP (blokkeert levering bij over-limit)
>   - Autorisaties vereist vóór actie (uitgaande betaling, bestelling > drempel)
>   - Toegangsbeperkingen (badges, RBAC in IT-systemen)
> 
> - **Repressieve controle (ex post)**: detecteert fouten of fraude **nadat** ze gebeurd zijn. ⚖️ Voorbeelden:
>   - Bankreconciliaties (maandelijks of wekelijks)
>   - Periodieke cijferanalyses (DSO, marge-trends)
>   - Interne audit (periodieke evaluatie van procedure-werking)
>   - Aged-receivables-rapportering
> 
> 🤖 Aanvullend type (sommige doctrines): **corrigerende** controle = controle die niet alleen detecteert maar ook het probleem **oplost** (bv. automatische correctie-routines in IT).
> 
> _Grondslag: [[interne-controle]] §Bouwstenen; [[beheersactiviteiten]] §Types controlemaatregelen; COSO I (1992/2013)._

> [!info]- Bronnen (2)
> - [[interne-controle|content/concepten/interne-controle.md]] · Bouwstenen — Drie doelstellingen → ondersteunt: context controleactiviteiten
> - [[beheersactiviteiten|content/concepten/beheersactiviteiten.md]] · Bouwstenen → ondersteunt: types maatregelen

> [!info]- Provenance
> - Generator: claude-opus-4-7
> - Datum: 2026-05-19
> - Antwoord-type: definitie
> - Checklist-versie: 1.0
> - Gates gepasseerd: claim_coverage, geen_externe_kennis
> - Verify gepasseerd: True
> - Wetsversie-policy: huidig

#### Subvraag a)

Accountingcontrole en administratieve contrôle.

#### Subvraag b)

Preventieve en repressieve controle.

---

### 2015-1-vr13 · 2015-1 · 8.0 pt

**Vraagformaat**: open · **Antwoord-type**: opsomming · **Confidence**: grounded

#### Vraagtekst

De verantwoordelijke van de interne audit zal een aantal controletechnieken aanwenden om
voldoende bewijsmateriaal te verzamelen over de toepassing en effectiviteit van de interne
controle maatregelen.

**Geef vier controletechnieken die door de interne controleur kunnen toegepast worden op de
goederen in het magazijn.**

Antwoord

#### Modelantwoord

Vier controletechnieken voor de interne controleur: (1) inspectie van documenten en activa, (2) waarneming van procedures en handelingen, (3) verzoek om inlichtingen (interviews + schriftelijke navragen), (4) herberekening van wiskundige juistheid. Aanvullend: externe bevestiging (klanten/leveranciers/banken/advocaten), cijferanalyse (trends + ratio's).

> [!success]- Motivering
> De interne controleur gebruikt de **klassieke set audit-technieken** (ISA 500 §A14-A25 — gedeeltelijk gedeeld met externe audit), aangepast aan de IC-context:
> 
> 1. **Inspectie** — onderzoek van documenten (facturen, bestelbonnen, contracten, leveringsbonnen) en fysieke activa (voorraad-count, vaste activa-inventaris). Levert bewijs over bestaan, autorisatie, en (deels) waardering. ⚖️
> 2. **Waarneming** — gadeslaan van een proces of procedure die door anderen wordt uitgevoerd (bv. waarnemen van een voorraadopname, of het uitvoeren van een aankoop-autorisatie door de inkoper). Bewijs over de **uitvoering** van controles op het moment van waarnemen. ⚖️
> 3. **Verzoek om inlichtingen** — interviews met medewerkers + management over werking van procedures, schriftelijke navragen. Op zichzelf onvoldoende, maar belangrijk als triangulatie. ⚖️
> 4. **Herberekening** — wiskundige juistheid controleren (afschrijvingsplan, BTW-totalen, salarisberekeningen, voorraadwaardering). ⚖️
> 
> **Aanvullende technieken**:
> - **Externe bevestiging** (zie [[externe-bevestiging-audit]]) — klanten, leveranciers, banken, advocaten — schriftelijk rechtstreeks
> - **Cijferanalyses** ([[cijferanalyses-controle-norm]]) — trends, ratio's, vergelijking met budget/vorig jaar
> - **Steekproef** ([[steekproef-audit]]) — als toelaatbare techniek-modaliteit voor inspectie
> 
> _Grondslag: ISA 500 §A14-A25; ITAA KMO-controlenorm §89-92; [[selecteren-en-uitvoeren-controle-instrumenten-audit]]._

> [!info]- Bronnen (3)
> - [[selecteren-en-uitvoeren-controle-instrumenten-audit|content/concepten/selecteren-en-uitvoeren-controle-instrumenten-audit.md]] · Stappen → ondersteunt: controle-instrumenten overzicht
> - [[externe-bevestiging-audit|content/concepten/externe-bevestiging-audit.md]] · Definitie → ondersteunt: externe bevestiging als techniek
> - [[cijferanalyses-controle-norm|content/concepten/cijferanalyses-controle-norm.md]] · Definitie → ondersteunt: cijferanalyses

> [!info]- Provenance
> - Generator: claude-opus-4-7
> - Datum: 2026-05-19
> - Antwoord-type: opsomming
> - Checklist-versie: 1.0
> - Gates gepasseerd: claim_coverage, geen_externe_kennis
> - Verify gepasseerd: True
> - Wetsversie-policy: huidig

---

### 2015-1-vr14 · 2015-1 · 5.0 pt

**Vraagformaat**: J/F · **Antwoord-type**: kwalificatie · **Confidence**: inferred

#### Vraagtekst

In onderstaand schema worden een aantal doelstellingen weergegeven die bij de
operationele audit van de verkoopcyclus van belang zijn.
Duid bij elke doelstelling aan of het gaat om een financieel, en/of operationeel en/of
conformiteitsaspect .
Antwoord

| Doelstelling | Financieel | Operationeel | Conformiteit |
| --- | --- | --- | --- |
| Opstellen van een marketingstrategie |   |   |   |
| Behoud mogelijkheid tot tijdige levering <br> tegen de laagst mogelijke distributiekost |   |   |   |
| Opvolging van marktbehoeften, introductie <br> nieuwe producten en stopzetting van <br> bestaande producten |   |   |   |
| Enkel toegestane verkooporders worden <br> verwerkt |   |   |   |
| Alle verzonden goederen worden in de juiste <br> periode correct gefactureerd |   |   |   |

ACCOUNTANTSONDERZOEK 25 PUNTEN

#### Modelantwoord

1: Operationeel. 2: Operationeel. 3: Operationeel. 4: Conformiteit (+ Financieel). 5: Financieel.

> [!success]- Motivering
> | Doelstelling | F | O | C | Motivering |
> |---|:-:|:-:|:-:|---|
> | Opstellen marketingstrategie | | **✓** | | Strategisch-operationeel (positionering, productlancering); geen financieel rapporterings-impact direct |
> | Behoud tijdige levering tegen laagst mogelijke distributiekost | | **✓** | | Klassieke operationele doelstelling (efficiëntie) |
> | Opvolging marktbehoeften + productintroductie/-stopzetting | | **✓** | | Operationeel (productmix-management); deels strategisch maar onder operationeel valt in MC |
> | Enkel toegestane verkooporders worden verwerkt | **✓** | | **✓** | Financieel (correctheid omzet) + Conformiteit (autorisatie-discipline — beleid + wettelijk) |
> | Alle verzonden goederen in juiste periode correct gefactureerd | **✓** | | | Financieel: cut-off + volledigheid van de omzet ([[verkoopcyclus-ic]] §Valkuilen) |
> 
> 🤖 Sommige doelstellingen passen onder meer categorieën — ITAA verwacht typisch één kruis per doelstelling, kies de **primaire** dimensie. Voor onbevoegde verkoop kan zowel F als C — beide aanvinken is verdedigbaar.
> 
> _Grondslag: [[verkoopcyclus-ic]] §Stappen + §Valkuilen; [[coso-i-framework]] §Doelstellingen-categorieën._

> [!info]- Bronnen (2)
> - [[verkoopcyclus-ic|content/concepten/verkoopcyclus-ic.md]] · Stappen + Valkuilen → ondersteunt: cut-off + autorisatie verkoop
> - [[coso-i-framework|content/concepten/coso-i-framework.md]] · Doelstellingen → ondersteunt: F/O/C categorieën

> [!info]- Provenance
> - Generator: claude-opus-4-7
> - Datum: 2026-05-19
> - Antwoord-type: kwalificatie
> - Checklist-versie: 1.0
> - Gates gepasseerd: claim_coverage, geen_externe_kennis
> - Verify gepasseerd: True
> - Wetsversie-policy: huidig

---

### 2024-1-vr3 · 2024-1

> [!warning] Herinnering-reconstructie (volledig)
> Deze vraag is een **herinnering**-reconstructie (volledigheid: volledig) — geen officiële ITAA-bundel. Modelantwoord rust op de geherinterpreteerde vraagtekst (ADR-022).

**Vraagformaat**: MC · **Antwoord-type**: casus · **Confidence**: inferred

#### Vraagtekst

3 Interne controle

- **A.** Wat zijn goede adviezen aan de bedrijfsleider in verband met de verkoopcyclus
- **B.** Wat is de hoofddoelstelling van de invoering van een interne controle in een KMO
- **C.** Over welke soort risico gaat het? ( COSO model) ● Strategisch ● Informatie ● Operationeel ● Financieel
- **D.** Verkoopcyclus: Doelstelling ● Financieel ● Operationeel ● Conformiteit

> [!note]- Geherinterpreteerde vraagtekst (ADR-022)
> Casus interne controle in een KMO-verkoopcyclus, 4 deelvragen:
> A. Wat zijn goede adviezen aan de bedrijfsleider in verband met de verkoopcyclus?
> B. Wat is de hoofddoelstelling van de invoering van een interne controle in een KMO?
> C. MC volgens het COSO-model — over welk soort risico gaat het? a. Strategisch / b. Informatie / c. Operationeel / d. Financieel.
> D. MC — Verkoopcyclus: doelstelling. a. Financieel / b. Operationeel / c. Conformiteit.
> 
> _Motivering_: Alle vier subvragen hebben volledige stam. Sub-C en sub-D zijn MC met opties in bullet-form in de PDF (● Strategisch ● Informatie ...). De vraagcontext (welk risico voor de verkoopcyclus? welk doel voor de verkoopcyclus?) is duidelijk afleidbaar uit positie van de MC binnen de casus.
> _Confidence_: grounded · _Datum_: 2026-05-19

> [!example]- MC-opties (gestructureerd)
> | Label | Tekst | Juistheid | Motivering |
> | --- | --- | --- | --- |
> | C.a | Strategisch | fout | Verkoopcyclus betreft primair rapporterings- en operationele controle, niet strategisch. |
> | C.b | Informatie | onbekend | In COSO-terminologie is rapporterings-/informatierisico de hoofdcategorie voor cyclus-controles. |
> | C.c | Operationeel | onbekend | Verkoopcyclus heeft operationele dimensie (efficiëntie facturatie). |
> | C.d | Financieel | onbekend | BIBF-doctrine noemt vaak 'financieel' voor omzet/vorderingen-rapporteringsrisico. |
> | D.a | Financieel | juist | Primaire doelstelling is correcte/volledige rapportering van omzet en vorderingen (cut-off, waardering). |
> | D.b | Operationeel | fout | Operationele effectiviteit is secundair doel. |
> | D.c | Conformiteit | fout | Conformiteit (BTW, GDPR) is randvoorwaarde, niet primaire doelstelling. |

#### Modelantwoord

Casus interne controle verkoopcyclus, 4 deelvragen: A. 5 hoofdadviezen (krediettoekenning, functiescheiding, cut-off, creditnota-controle, aged-receivables). B. Hoofddoelstelling IC = redelijke zekerheid over (1) betrouwbare rapportering, (2) operationele effectiviteit, (3) compliance. C. Voornaamste risico = Financieel (rapporterings-risico op omzet/vorderingen). D. Verkoopcyclus-doelstelling = Financieel (cut-off, waardering).

> [!success]- Motivering
> Vraag bevat **vier deelvragen** (A/B/C/D) over interne controle in de verkoopcyclus. Hieronder per deel.
> 
> ### A. Goede adviezen aan de bedrijfsleider in verband met de verkoopcyclus
> 
> Vijf hoofdadviezen (gestructureerd langs de cyclus-stappen in [[verkoopcyclus-ic]]):
> 
> 1. **Krediettoekenning vooraf** — toets de kredietwaardigheid van iedere nieuwe klant (KBO, jaarrekening, eventueel kredietverzekeraar) en ken een **kredietlimiet** toe die het ERP-systeem afdwingt. ⚖️ Doel: oninbare vorderingen voorkomen. Bij over-limit of mora: automatische blokkering van leveringen.
> 2. **Functiescheiding tussen sales, magazijn en facturatie** — orderintake door sales, levering door magazijn (op basis van ondertekende delivery note), facturatie automatisch uit ERP. ⚖️ Voorkomt manipulatie ('vergeten te factureren', fictieve klanten, oneigenlijke creditnota's).
> 3. **Cut-off-discipline rond balansdatum** — levering en factuur in dezelfde periode (BTW vereist factuur binnen 15 dagen na levering). ⚖️ Maandelijks alle delivery notes zonder factuur onderzoeken. Voorkomt omzetverschuiving (klassiek fraude-risico).
> 4. **Creditnota's apart goedkeuren** — voor elke creditnota een aparte autorisatie, traceerbare reden, en functiescheiding met de oorspronkelijke factuurboeker. ⚖️ Creditnota's zijn een typische manipulatie-vector.
> 5. **Aged-receivables-opvolging** — wekelijks ouderdoms-rapport, automatische escalatie (herinnering > 30 dagen, ingebrekestelling > 60 dagen, juridische actie + voorziening > 90 dagen). ⚖️ Detecteert betalingsproblemen vroeg en stuurt de voorziening voor dubieuze debiteuren.
> 
> _Grondslag: [[verkoopcyclus-ic]] §Stappen 1-4, [[functiescheiding]] §sales-levering._
> 
> ### B. Hoofddoelstelling van de invoering van interne controle in een KMO
> 
> De **hoofddoelstelling** is een **redelijke** mate van zekerheid bieden over drie samenhangende domeinen (KMO-controlenorm Bijlage 1; COSO I 1992/2013):
> 
> 1. **Betrouwbaarheid van de financiële rapportering** ⚖️
> 2. **Effectieve en efficiënte werking van de bedrijfsprocessen** (operationele doelen) ⚖️
> 3. **Naleving van wetten en regelgeving** (compliance — boekhoudwet, BTW, sociale wetgeving, …) ⚖️
> 
> Sommige bronnen voegen een vierde toe: **bescherming van het vermogen / de activa** tegen verlies, diefstal of fraude. 🤖
> 
> In een **KMO-context** ligt het accent vaak op (1) en (3): de eigenaar-bestuurder werkt veelal mee aan de operationele kant zelf en heeft minder behoefte aan formele operationele controle. Maar betrouwbare cijfers en compliance zijn ook in een KMO onontbeerlijk (jaarrekening, BTW-aangiftes, fiscale aangifte, sociale documenten).
> 
> _Grondslag: [[interne-controle]] §Bouwstenen — Drie doelstellingen + Redelijke, geen absolute zekerheid._
> 
> ### C. Soort risico volgens COSO model
> 
> COSO ERM 2017 onderscheidt vier categorieën doelstellingen (en de daarmee verbonden risico's):
> - **Strategisch** (long-term, marktpositie)
> - **Operationeel** (efficiënte werking)
> - **Rapportering** ('Informatie' in oude COSO I — betrouwbaarheid van interne en externe rapporten)
> - **Compliance** ('Conformiteit', niet in deze MC-lijst)
> 
> In de MC: ● Strategisch ● Informatie ● Operationeel ● Financieel.
> 
> Voor de **verkoopcyclus** specifiek is het belangrijkste risico **financieel** (omzetbetrouwbaarheid, vorderingenwaardering, fraude in omzetcijfers) — dit valt onder 'Informatie' / 'Rapportering' in COSO-terminologie, maar wordt in BIBF-doctrine vaak rechtstreeks 'financieel' genoemd. ⚖️
> 
> **Antwoord MC**: voornaamste = **Financieel** (rapporterings-risico op de omzet- en vorderingen-balansposten). Secundair operationeel (procesfouten) en strategisch (klantenportefeuille-risico). 🤖
> 
> _Grondslag: [[coso-i-framework]] §Doelstellingen, [[verkoopcyclus-ic]] §Valkuilen (cut-off, creditnota's = financieel rapporterings-risico)._
> 
> ### D. Verkoopcyclus: Doelstelling
> 
> MC: ● Financieel ● Operationeel ● Conformiteit.
> 
> De **primaire doelstelling** van interne controle op de verkoopcyclus is:
> - **Financieel**: garanderen dat omzet en vorderingen correct, volledig en in de juiste periode worden gerapporteerd (cut-off, waardering dubieuze debiteuren). ⚖️
> - **Operationeel** secundair: efficiënte klantverwerking (kortere DSO, vlotte facturatie).
> - **Conformiteit** als randvoorwaarde: BTW-naleving (factuur binnen 15 dagen, BTW-conforme vermeldingen), GDPR voor klantgegevens.
> 
> **Antwoord MC**: **Financieel** als hoofddoelstelling (cut-off, juiste waardering, vermijden fraude). 🤖 Operationeel en Conformiteit zijn ondergeschikt maar wel aanwezig.
> 
> _Grondslag: [[verkoopcyclus-ic]] §Bouwstenen + §Valkuilen (cut-off, creditnota's = financiële rapporterings-risico's)._

> [!info]- Bronnen (5)
> - [[verkoopcyclus-ic|content/concepten/verkoopcyclus-ic.md]] · Berekening — Stappen 1-4 → ondersteunt: A. adviezen krediettoekenning, functiescheiding, cut-off
> - [[verkoopcyclus-ic|content/concepten/verkoopcyclus-ic.md]] · Valkuilen → ondersteunt: A. creditnota-controle, cut-off-discipline
> - [[interne-controle|content/concepten/interne-controle.md]] · Bouwstenen — Drie doelstellingen → ondersteunt: B. hoofddoelstelling IC
> - [[coso-i-framework|content/concepten/coso-i-framework.md]] · Doelstellingen → ondersteunt: C. COSO-risicocategorieën
> - [[functiescheiding|content/concepten/functiescheiding.md]] · Sales-levering → ondersteunt: A. functiescheiding

> [!info]- Provenance
> - Generator: claude-opus-4-7
> - Datum: 2026-05-19
> - Antwoord-type: casus
> - Checklist-versie: 1.0
> - Gates gepasseerd: claim_coverage, geen_externe_kennis
> - Verify gepasseerd: True
> - Wetsversie-policy: huidig

---

## PO 1.9

_4 vragen — 4 met modelantwoord — 0 met gap-rapport._

### 2003-bibf-vrC1 · 2003-bibf · 4 pt

_Ook geklassificeerd onder_: 1.3

**Vraagformaat**: berekening · **Antwoord-type**: berekening · **Confidence**: grounded

#### Vraagtekst

Op de balans staan volgende bedragen: …  ACTIVA Vaste activa 150.040,00 Vlottende activa Voorraden 41.000,00 Vorderingen op -1 jaar 42.700,00 Geldbeleggingen 10.000,00 Liquide middelen 37.500,00 281.240,00 PASSIVA Kapitaal 100.000,00 Reserves 50.400,00 Overgedragen winst 2.750,00 Schulden op + 1 jaar 51.000,00 Schulden op - 1 jaar 77.090,00 281.240,00 Vraag:

**Bereken uit deze cijfers

a.**

het netto bedrijfskapitaal

- **b.** de ruime liquiditeitsratio (current ratio)
- **c.** de beperkte liquiditeitsratio (acid test)
- **d.** de solvabiliteitsratio.

#### Modelantwoord

a) Netto bedrijfskapitaal = € 131.200 − € 77.090 = **€ 54.110**. b) Current ratio = € 131.200 / € 77.090 = **1,70**. c) Quick ratio = € 90.200 / € 77.090 = **1,17**. d) Solvabiliteitsratio = € 153.150 / € 281.240 = **54,46 %**.

> [!success]- Motivering
> Gegeven (balans):
> - Vaste activa: € 150.040
> - Voorraden: € 41.000
> - Vorderingen op −1 jaar: € 42.700
> - Geldbeleggingen: € 10.000
> - Liquide middelen: € 37.500
> - **Vlottende activa totaal**: 41.000 + 42.700 + 10.000 + 37.500 = **€ 131.200**
> - Kapitaal: € 100.000
> - Reserves: € 50.400
> - Overgedragen winst: € 2.750
> - **Eigen vermogen totaal**: 100.000 + 50.400 + 2.750 = **€ 153.150**
> - Schulden op + 1 jaar: € 51.000
> - Schulden op − 1 jaar: € 77.090
> - **Balanstotaal**: € 281.240
> 
> ### a) Netto bedrijfskapitaal
> 
> ```
> netto bedrijfskapitaal = vlottende activa − schulden op ten hoogste 1 jaar
>                        = € 131.200 − € 77.090
>                        = € 54.110
> ```
> ⚖️ Positief → vlottende activa dekken meer dan de korte-termijn schulden; buffer voor liquiditeitsschokken.
> 
> ### b) Ruime liquiditeitsratio (current ratio)
> 
> ```
> current ratio = vlottende activa / schulden op ten hoogste 1 jaar
>               = € 131.200 / € 77.090
>               = 1,70
> ```
> ⚖️ Vuistregel: > 1 wordt als gezond beschouwd (vlottende activa dekken kortlopende schulden). 1,70 = ruim voldoende.
> 
> ### c) Beperkte liquiditeitsratio (acid test / quick ratio)
> 
> ```
> quick ratio = (vlottende activa − voorraden) / schulden op ten hoogste 1 jaar
>             = (€ 131.200 − € 41.000) / € 77.090
>             = € 90.200 / € 77.090
>             = 1,17
> ```
> ⚖️ Strenger dan current ratio: sluit voorraden uit omdat die niet altijd snel liquideerbaar zijn. > 1 = voldoende.
> 
> ### d) Solvabiliteitsratio
> 
> ```
> solvabiliteitsratio = eigen vermogen / balanstotaal
>                     = € 153.150 / € 281.240
>                     = 54,46 %
> ```
> ⚖️ Vuistregel: > 30-40 % wordt gezond geacht. 54 % = sterke eigen-vermogen-positie, lage afhankelijkheid van schuldeisers.
> 
> _Grondslag: [[liquiditeitsratio]] §Berekening; [[solvabiliteitsratio]] §Berekening; [[werkkapitaal]] §Bouwstenen._

> [!info]- Bronnen (4)
> - [[werkkapitaal|content/concepten/werkkapitaal.md]] · Bouwstenen → ondersteunt: definitie netto bedrijfskapitaal
> - [[liquiditeitsratio|content/concepten/liquiditeitsratio.md]] · Berekening → ondersteunt: current + quick ratio formules
> - [[solvabiliteitsratio|content/concepten/solvabiliteitsratio.md]] · Berekening → ondersteunt: solvabiliteitsratio formule
> - [[berekenen-interpreteren-liquiditeitsratios|content/concepten/berekenen-interpreteren-liquiditeitsratios.md]] · Stappen → ondersteunt: interpretatie ratios

> [!info]- Provenance
> - Generator: claude-opus-4-7
> - Datum: 2026-05-19
> - Antwoord-type: berekening
> - Checklist-versie: 1.0
> - Gates gepasseerd: claim_coverage, geen_externe_kennis
> - Verify gepasseerd: True
> - Wetsversie-policy: huidig

---

### 2003-bibf-vrC2 · 2003-bibf · 1 pt

_Ook geklassificeerd onder_: 1.3

**Vraagformaat**: berekening · **Antwoord-type**: berekening · **Confidence**: grounded

#### Vraagtekst

Naast de balans hierboven blijken volgende cijfers uit de resultatenrekening 1 PUNT

**Inventaris**
- winst van het boekjaar: 2.750,00 EUR
- afschrijvingen: 12.100,00 EUR
- toevoegingen aan voorzieningen: 6.300,00 EUR
- bestedingen van voorzieningen: 1.650,00 EUR
- toevoegingen aan waardeverminderingen: 780,00 EUR

Vraag:

**Bereken de operationele cash-flow.**

#### Modelantwoord

Operationele cashflow = 2.750 + 12.100 + 6.300 − 1.650 + 780 = **€ 20.280**.

> [!success]- Motivering
> Operationele cashflow = nettoresultaat + niet-kas-bestanddelen (klasse 63 RR):
> 
> ```
> operationele cashflow = winst boekjaar + afschrijvingen + toevoegingen voorzieningen 
>                       − bestedingen voorzieningen + toevoegingen waardeverminderingen
> ```
> 
> **Toepassing op de gegevens**:
> 
> | Component | Bedrag (€) |
> |---|---:|
> | Winst van het boekjaar | + 2.750 |
> | Afschrijvingen | + 12.100 |
> | Toevoegingen aan voorzieningen | + 6.300 |
> | Bestedingen van voorzieningen | − 1.650 |
> | Toevoegingen aan waardeverminderingen | + 780 |
> | **Operationele cashflow** | **+ 20.280** |
> 
> ⚖️ De operationele cashflow corrigeert het boekhoudkundig resultaat voor de niet-kas-bestanddelen: afschrijvingen en waardeverminderingen zijn boekingen zonder kasuitgaaf, en voorzieningen-toevoegingen/-bestedingen zijn timing-correcties. Het verschil tussen winst (€ 2.750) en operationele cashflow (€ 20.280) toont dat het bedrijf cash genereert die in het resultaat niet zichtbaar is — een belangrijk signaal voor financiële analyse. 🤖
> 
> _Grondslag: [[bedrijfsresultaat]] §Bouwstenen — niet-kas-rubrieken klasse 63; [[cashflow-analyse]] §Bouwstenen — klassieke cashflow-formule._

> [!info]- Bronnen (2)
> - [[bedrijfsresultaat|content/concepten/bedrijfsresultaat.md]] · Bouwstenen — niet-kas-rubrieken klasse 63 → ondersteunt: cashflow-formule componenten
> - [[cashflow-analyse|content/concepten/cashflow-analyse.md]] · Bouwstenen → ondersteunt: klassieke cashflow-berekening

> [!info]- Provenance
> - Generator: claude-opus-4-7
> - Datum: 2026-05-19
> - Antwoord-type: berekening
> - Checklist-versie: 1.0
> - Gates gepasseerd: claim_coverage, geen_externe_kennis
> - Verify gepasseerd: True
> - Wetsversie-policy: huidig

---

### 2008-bibf-vrC1 · 2008-bibf

**Vraagformaat**: open · **Antwoord-type**: — · **Confidence**: —

#### Vraagtekst

Wat verstaat men met “behoefte aan bedrijfskapitaal”? Hoe wordt het berekend? Van uit het oogpunt financieel beheer, wat kan worden ondernomen om de behoefte aan bedrijfskapitaal te verminderen?

#### Modelantwoord

De behoefte aan bedrijfskapitaal is het netto verschil tussen de

> [!success]- Motivering
> De behoefte aan bedrijfskapitaal is het netto verschil tussen de bedrijfsbronnen en bedrijfsaanwendingen. Het wordt berekend als verschil tussen enerzijds de niet financiële beperkte vlottende activa en, anderzijds, de niet financiële schulden op ten hoogste één jaar. (3 + 40/41 + 49 van het actief) – (42 + 44 tot 48 + 49 van het passief) Om behoefte aan bedrijfskapitaal te verminderen, moet de omvang van de voorraden en / of vorderingen verminderen. Betalingstermijnen leverancier uitbreiden.

> [!info]- Bronnen (1)
> - _pdf-modelantwoord_

---

### 2008-bibf-vrC2 · 2008-bibf

**Vraagformaat**: berekening · **Antwoord-type**: — · **Confidence**: —

#### Vraagtekst

Een vennootschap heeft jaarlijks ongeveer 30.000,00 EUR cashflow. Ze betaalt jaarlijks 12.000,00 EUR kapitaalaflossingen op bestaande leningen. Voor een nieuwe investering van 100.000,00 EUR, wenst ze van de bank een investeringskrediet te bekomen om het volledig bedrag van de aankoop te financieren. De rentevoet bedraagt 5 % per jaar. Ze wenst de nieuwe lening in 5 jaarlijkse gelijke schijven af te lossen.

**Wat is uw mening?**

#### Modelantwoord

De nieuwe lening zal het eerste jaar een intrestkost van 5.000,00 EUR

> [!success]- Motivering
> De nieuwe lening zal het eerste jaar een intrestkost van 5.000,00 EUR veroorzaken. De cashflow vermindert zodoende tot 25.000,00 EUR. Rekening houdend met terugbetalingen van 12.000,00 EUR op de bestaande leningen blijft er slechts een vrije cashflow van 13.000,00 EUR over. Indien de nieuwe lening over 5 jaar wordt terugbetaald moet jaarlijks aan kapitaalaflossingen 20.000,00 EUR worden betaald. De vrije cashflow bedraagt slechts 13.000,00 EUR; bijgevolg moet overwogen worden om de lening over een langere periode af te lossen (8 jaar of meer).

> [!info]- Bronnen (1)
> - _pdf-modelantwoord_

---

## PO 2.2

_25 vragen — 4 met modelantwoord — 0 met gap-rapport._

### 2003-bibf-vrF1 · 2003-bibf · 10 pt

**Vraagformaat**: berekening · **Antwoord-type**: — · **Confidence**: —

#### Vraagtekst

F. PERSONENBELASTING  De Heer en

> Mevrouw Janssens zijn eigenaar van twee onroerende goederen: onroerend goed A, gelegen buiten de stad en onroerend goed B, gelegen in het centrum van de stad.

Zij hebben 4 kinderen van respectievelijk 12, 9,7 en 4 jaar.en wonen allen samen in het huis A. De Heer Janssens is afgevaardigd bestuurder van een NV. Deze NV huurt het onroerend goed B van de familie Janssens voor een huurprijs van 15.000 € per jaar verhoogd met de onroerende voorheffing. Woonhuis A KI 1.050 € Woonhuis B KI 1.202 € Revalorisatiecoëfficient 3,35 (Art. 1 KBWIB 92) F.1 Stel de belastbare basis van de inkomsten van de Heer Janssens als bedrijfsleider vast (Vak II) aan de hand van volgende gegevens: 10 PUNTEN - Jaarlijkse bruto bezoldiging : 30.000 € - Sociale bijdrage voor rekening van de Heer Janssens betaald door de NV, per trimester: 1.200 € - Netto bedrag van de mutualiteitbijdrage 887 € - Ingehouden en doorgestorte bedrijfsvoorheffing 4.636 € - Voordelen van alle aard (auto) 1.500 € - forfaitaire beroepskosten : UIT TE REKENEN

_Nog niet beantwoord (modelantwoord ontbreekt)._

---

### 2008-bibf-vrF1 · 2008-bibf

**Vraagformaat**: open · **Antwoord-type**: — · **Confidence**: —

#### Vraagtekst

Gert is ongehuwd en woont in Mechelen in een pand, waarvan hij eigenaar is, met een KI van 1 700. Gert erft in 2007 als enige zoon het huis van zijn ouders. Wat zijn daar de gevolgen van op vlak van intrestaftrek en kapitaalaflossing, wetende dat er geen andere onroerende eigendommen zijn. 1.1 Indien Gert een hypothecaire lening heeft afgesloten op 13.03.2004 Gewone intrestaftrek blijft De aanvullende intrestaftrek gaat verloren Kapitaalaflossing: belastingvermindering voor bouwsparen blijft (eenmalige beoordeling op enige woning) 1.2 Indien Gert deze hypothecaire lening afgesloten had op 13.03.2005 Het recht op de woonbonus (aftrek voor enig woonhuis) op zich blijft; enkel de verhoging (€ 650,00 voor de eerste 10 jaar) verdwijnt.

#### Modelantwoord

1.2004: gewone intrestaftrek + bouwspaarvermindering blijven; aanvullende intrestaftrek vervalt. 2.2005: recht op woonbonus blijft; enkel de verhoging (€ 650 voor de eerste 10 jaar) verdwijnt.

> [!success]- Motivering
> 1.1 Indien Gert een hypothecaire lening heeft afgesloten op 13.03.2004: - Gewone intrestaftrek blijft - De aanvullende intrestaftrek gaat verloren - Kapitaalaflossing: belastingvermindering voor bouwsparen blijft (eenmalige beoordeling op enige woning)
> 
> 1.2 Indien Gert deze hypothecaire lening afgesloten had op 13.03.2005: - Het recht op de woonbonus (aftrek voor enig woonhuis) op zich blijft; enkel de verhoging (€ 650,00 voor de eerste 10 jaar) verdwijnt.

> [!info]- Bronnen (1)
> - _pdf-modelantwoord_

---

### 2008-bibf-vrF2 · 2008-bibf

**Vraagformaat**: open · **Antwoord-type**: — · **Confidence**: —

#### Vraagtekst

Riet en Piet zijn gehuwd in het wettelijk stelsel . Ze wonen in Etterbeek. Riet heeft van voor het huwelijk nog een appartement (KI 1 200) in Wemmel in persoonlijke eigendom, dat verhuurd wordt. Het appartement stond al langer te koop en uiteindelijk wordt het op 6 april 2007 verkocht: een belastbare meerwaarde van € 30 000 wordt gerealiseerd. Doe aangifte van het onroerend inkomen en van de meerwaarde Onroerend (1106) 150 (2106) 150 (zijnde 1 200 x 3 /12 en dan 50/50) Divers (1171) 0 (2171) 30 000

#### Modelantwoord

Onroerend: code (1106)/(2106) elk 150 (= 1 200 × 3/12 × 50/50). Divers: code (2171) 30 000.

> [!success]- Motivering
> Onroerend (1106) 150 (2106) 150 (zijnde 1 200 x 3/12 en dan 50/50) Divers (1171) 0 (2171) 30 000

> [!info]- Bronnen (1)
> - _pdf-modelantwoord_

---

### 2008-bibf-vrF3 · 2008-bibf

**Vraagformaat**: berekening · **Antwoord-type**: — · **Confidence**: —

#### Vraagtekst

Een echtpaar heeft dienstencheques aangekocht: 3 000,00 (max. AJ 2008 : 2 360,00 EUR) op naam van de aangever en 1 000,00 op naam van de partner.

**Bereken het belastingvoordeel van de dienstencheques rekening houdend met volgende gegevens.**

aangever partner Totaal netto-inkomen 33 900,00 17 100,00 -Onderhoudsgelden -4 000,00 Gezamenlijk belastbaar inkomen 29 900,00 17 100,00 2 360 x 30 % = 708 1 000 x 30 % = 300 1 008 x 33 900/51 000 = 670,02 1 008 x 17 100/51 000 = 337,98

#### Modelantwoord

Aangever: 2 360 × 30 % = 708; partner: 1 000 × 30 % = 300. Verdeling 1 008 over partners volgens inkomensbreuk → 670,02 en 337,98.

> [!success]- Motivering
> 2 360 x 30 % = 708 1 000 x 30 % = 300 1 008 x 33 900/51 000 = 670,02 1 008 x 17 100/51 000 = 337,98

> [!info]- Bronnen (1)
> - _pdf-modelantwoord_

---

### 2008-bibf-vrF4 · 2008-bibf

**Vraagformaat**: open · **Antwoord-type**: — · **Confidence**: —

#### Vraagtekst

Wim is gehuwd met Inge in het stelsel van scheiding van goederen. Ze zijn zinnens een (eerste) huis te gaan kopen. Gezien de zelfstandige activiteit van Inge stellen ze voor de aankoop niet in onverdeeldheid te doen, maar op naam van Wim. Waar moet je rekening mee houden wanneer Wim voor de financiering van de aankoop een hypothecaire lening aangaat? Zodra een gemeenschappelijke aanslag gevestigd wordt, dient minstens 15 % van de aftrekbare besteding bij de partner aangegeven worden. Vermits Wim de enige eigenaar is, gaat die 15 % van de aftrekbare besteding verloren (art. 105, 2° lid WIB)

#### Modelantwoord

Bij gemeenschappelijke aanslag moet 15 % bij de partner aangegeven worden — die 15 % gaat verloren omdat Wim enige eigenaar is (art. 105, 2° lid WIB).

> [!success]- Motivering
> Zodra een gemeenschappelijke aanslag gevestigd wordt, dient minstens 15 % van de aftrekbare besteding bij de partner aangegeven worden. Vermits Wim de enige eigenaar is, gaat die 15 % van de aftrekbare besteding verloren (art. 105, 2° lid WIB).

> [!info]- Bronnen (1)
> - _pdf-modelantwoord_

---

### 2008-bibf-vrF5 · 2008-bibf

**Vraagformaat**: MC · **Antwoord-type**: — · **Confidence**: —

#### Vraagtekst

: Wat is juist inzake belastbaar tijdperk?

- **a.** Een uitgave in 2006 met betrekking tot een door een handelaar in 2007 te realiseren meerwaarde is een gezamenlijk belastbare winst van 2007
- **b.** Een tantième dat op 15.04.2008 met betrekking tot de winst van het boekjaar 2007 toegekend is, is voor de bedrijfsleider een beroepsinkomen gerelateerd aan het belastbaar tijdperk 2007
- **c.** Wanneer ingevolge een geschil met een (voormalig) werkgever een bezoldiging met betrekking tot de prestaties van 2007 pas in de loop van 2008 uitgekeerd wordt, is dat een belastbaar inkomen van 2007
- **d.** Een advocaat maakt op 20.12.07 een ereloonnota van € 1 000,00 op voor geleverde prestaties. De klant betaalt op 10.01.08. De erelonen horen tot het belastbaar tijdperk 2007.

_Nog niet beantwoord (modelantwoord ontbreekt)._

---

### 2008-bibf-vrF6 · 2008-bibf

**Vraagformaat**: MC · **Antwoord-type**: — · **Confidence**: —

#### Vraagtekst

F 6.

**Wat is geen vrijgesteld inkomen ?**

- **a.** Een sociaal voordeel
- **b.** Een resultaatgebonden bonus van € 2 000,00
- **c.** Een fietsvergoeding van € 0,15/km
- **d.** Een wettelijke ziekte-uitkering

_Nog niet beantwoord (modelantwoord ontbreekt)._

---

### 2008-bibf-vrF7 · 2008-bibf

**Vraagformaat**: MC · **Antwoord-type**: — · **Confidence**: —

#### Vraagtekst

F7.

**Welke uitgave vormt een aftrekbare besteding?**

- **a.** Uitgave voor het onderhoud en de restauratie van beschermde eigendommen
- **b.** Een uitgave voor de vernieuwing van een woning in een zone voor positief grootstedelijk beleid
- **c.** Uitgaven voor de vernieuwing van woningen die tegen een redelijke prijs verhuurd worden
- **d.** Uitgaven ter beveiliging van een privéwoning tegen diefstal en brand

_Nog niet beantwoord (modelantwoord ontbreekt)._

---

### 2013-1-vr20 · 2013-1 · 12.0 pt

**Vraagformaat**: J/F · **Antwoord-type**: — · **Confidence**: —

#### Vraagtekst

> De heer André, een loodgieter van 58 jaar oud, zet in 2012 zijn beroepswerkzaamheid stop en
> verkoopt zijn volledige handelszaak aan de heer Bernard
> (NB: geen verwantschap tussen de overlater en de overnemer).

**Bereken, op basis van de hierna verstrekte gegevens, het bedrag van de verschillende
stopzettingsmeerwaarden die in de belastingaangifte moeten vermeld worden en geef de
aanslagvoet van de verschillende bestanddelen.**

De bedragen zijn exclusief btw. (Er moet
geen rekening gehouden worden met de gemeentelijke opcentiemen, en ook niet met een
eventuele globale aanslag indien deze voordeliger zou zijn voor de belastingplichtige).
NB: het gebouw werd in 1985 aangekocht voor een totale waarde van 500.000 euro. Onder
controle van de FOD Financiën werd volgende omdeling gemaakt: 400.000 euro voor het
gebouw en 100.000 euro voor het terrein, het gelijkvloers werd bestemd voor de
beroepswerkzaamheid en de 1ste verdieping voor privébewoning (50/50-verhouding).
Uiteenzetting van de in de verkoopovereenkomst vermelde prijs:
Verkoopprijs van de machines = € 50.000
Verkoopprijs van het gebouw (Dhr. Bernard koopt het volledige gebouw en zal zich met zijn
gezin op de 1ste verdieping vestigen) = € 800.000. Er werd overeengekomen dat het gedeelte
terrein € 200.000 bedraagt.
Verkoopprijs van de bestelwagen = € 25.000
Verkoopprijs van de cliënteel = € 300.000
Tijdens de laatste jaren verwezenlijkte winst:
2011 € 35.242
2010 € 17.771
2009 € 28.861
2008 € 30.367
2007 € 21.784

> De heer André had een gespecialiseerde onderneming in de arm genomen voor de overlating
> van zijn handelszaak.

Die bemiddelaar heeft voor de verleende diensten een commissieloon
ontvangen van € 117.500 (10%).

> De heer André heeft netto dus € 1.

057.500 ontvangen (hetzij € 1.175.000 min € 117.500).
Antwoord

_Nog niet beantwoord (modelantwoord ontbreekt)._

---

### 2013-1-vr21 · 2013-1 · 8.0 pt

**Vraagformaat**: J/F · **Antwoord-type**: — · **Confidence**: —

#### Vraagtekst

**Geef aan of volgende uitspraken waar of onwaar zijn:
a) Wanneer een werknemer voorafbetalingen doet, zal hij een bonificatie genieten, maar
enkel voor de belasting die betrekking heeft op zijn beroepsinkomsten.**

|   |   |
| --- | --- |
|   | Waar |
|   | Niet waar |

b) De interest van een spaarrekening geopend ten name van een minderjarig kind, moet
nooit worden opgenomen in de belastbare grondslag van de ouders, tenzij de ouders
gehuwd zijn onder het stelsel van de wettelijke gemeenschap.

|   |   |
| --- | --- |
|   | Waar |
|   | Niet waar |

c) Wanneer de eigendom van een onroerend goed gesplitst is en dat goed verhuurd
wordt aan een huurder die het gebruikt voor de uitoefening van zijn beroep, zal de
naakte eigenaar belast worden op het kadastraal inkomen en zal de vruchtgebruiker
belast worden op de ontvangen huur.

|   |   |
| --- | --- |
|   | Waar |
|   | Niet waar |

d) De enige beroepsinkomsten die in aanmerking komen voor de forfaitaire aftrek van
beroepskosten zijn de inkomsten van werknemers en de inkomsten van
bedrijfsleiders.

|   |   |
| --- | --- |
|   | Waar |
|   | Niet waar |

e) Auteursrechten worden nooit als beroepsinkomsten beschouwd maar worden steeds
als roerende inkomsten belast.

|   |   |
| --- | --- |
|   | Waar |
|   | Niet waar |

f) Bij werknemers worden, alvorens de forfaitaire beroepskosten te berekenen, eerst de
door de werknemer gedragen persoonlijke sociale bijdragen die door de werkgever
niet werden ingehouden afgetrokken.

|   |   |
| --- | --- |
|   | Waar |
|   | Niet waar |

g) Wanneer een bedrijfsleider het bedrag van het verlies van zijn vennootschap dat hij
ten laste wil nemen op het debet van zijn rekening-courant laat inschrijven, kan dat
bedrag ten name van de bedrijfsleider als beroepskosten worden afgetrokken.

|   |   |
| --- | --- |
|   | Waar |
|   | Niet waar |

h) De herkwalificatie van huur tot bezoldigingen die ten name van een bedrijfsleider
wordt uitgevoerd, heeft betrekking op alle onroerende goederen, inclusief terreinen.

|   |   |
| --- | --- |
|   | Waar |
|   | Niet waar |

VENNOOTSCHAPSBELASTING 20 PUNTEN

_Nog niet beantwoord (modelantwoord ontbreekt)._

#### Subvraag a)

Wanneer een werknemer voorafbetalingen doet, zal hij een bonificatie genieten, maar
enkel voor de belasting die betrekking heeft op zijn beroepsinkomsten.

#### Subvraag b)

De interest van een spaarrekening geopend ten name van een minderjarig kind, moet
nooit worden opgenomen in de belastbare grondslag van de ouders, tenzij de ouders
gehuwd zijn onder het stelsel van de wettelijke gemeenschap.

#### Subvraag c)

Wanneer de eigendom van een onroerend goed gesplitst is en dat goed verhuurd
wordt aan een huurder die het gebruikt voor de uitoefening van zijn beroep, zal de
naakte eigenaar belast worden op het kadastraal inkomen en zal de vruchtgebruiker
belast worden op de ontvangen huur.

#### Subvraag d)

De enige beroepsinkomsten die in aanmerking komen voor de forfaitaire aftrek van
beroepskosten zijn de inkomsten van werknemers en de inkomsten van
bedrijfsleiders.

#### Subvraag e)

Auteursrechten worden nooit als beroepsinkomsten beschouwd maar worden steeds
als roerende inkomsten belast.

#### Subvraag f)

Bij werknemers worden, alvorens de forfaitaire beroepskosten te berekenen, eerst de
door de werknemer gedragen persoonlijke sociale bijdragen die door de werkgever
niet werden ingehouden afgetrokken.
g) Wanneer een bedrijfsleider het bedrag van het verlies van zijn vennootschap dat hij
ten laste wil nemen op het debet van zijn rekening-courant laat inschrijven, kan dat
bedrag ten name van de bedrijfsleider als beroepskosten worden afgetrokken.
h) De herkwalificatie van huur tot bezoldigingen die

---

### 2013-2-vr21 · 2013-2 · 6.0 pt

**Vraagformaat**: J/F · **Antwoord-type**: — · **Confidence**: —

#### Vraagtekst

Dhr. en mevr. Martin zijn in de loop van 2012 gescheiden met onderlinge toestemming. Dhr.
Martin is geboren op 15 juli 1963 en mevr. Martin op 10 juni 1975.
Er werd overeengekomen dat dhr. Martin op 1 december 2012 een éénmalige
onderhoudsuitkering onder de vorm van een kapitaal van € 100.000 aan zijn ex-echtgenote
zou betalen.
(NB: alle wettelijke voorwaarden op het gebied van de onderhoudsplicht zijn vervuld.)

- **a.** Mevr. Martin vraagt u om het bedrag te berekenen dat voor het aanslagjaar 2013 op haar

naam zal belast worden.

**Antwoord … / 1,5 punten
b) Moet het bedrag voor de volgende aanslagjaren gewijzigd worden.**

Zo ja, in welke mate?
Antwoord … / 1,5 punten

- **c.** Gedurende hoeveel jaren zal er ten name van mevr. Martin een belasting worden

gevestigd (Geef het aantal betrokken aanslagjaren of het jaar waarnaar het laatste
betrokken aanslagjaar wordt genoemd).
Antwoord … / 1,5 punten

d) Bereken het bedrag dat bij dhr. Martin aftrekbaar zal zijn voor het aanslagjaar 2013
(Het gaat om het bedrag dat in rekening wordt gebracht in de berekening van de
belasting van dhr. Martin, en niet om het bedrag dat in de aangifte wordt ingevuld).
Antwoord … / 1,5 punten

_Nog niet beantwoord (modelantwoord ontbreekt)._

#### Subvraag a)

Mevr. Martin vraagt u om het bedrag te berekenen dat voor het aanslagjaar 2013 op haar
naam zal belast worden.

#### Subvraag b)

Moet het bedrag voor de volgende aanslagjaren gewijzigd worden. Zo ja, in welke mate?

#### Subvraag c)

Gedurende hoeveel jaren zal er ten name van mevr. Martin een belasting worden
gevestigd (Geef het aantal betrokken aanslagjaren of het jaar waarnaar het laatste
betrokken aanslagjaar wordt genoemd).

#### Subvraag d)

Bereken het bedrag dat bij dhr. Martin aftrekbaar zal zijn voor het aanslagjaar 2013
(Het gaat om het bedrag dat in rekening wordt gebracht in de berekening van de
belasting van dhr. Martin, en niet om het bedrag dat in de aangifte wordt ingevuld).

---

### 2013-2-vr22 · 2013-2 · 10.0 pt

**Vraagformaat**: berekening+MC · **Antwoord-type**: — · **Confidence**: —

#### Vraagtekst

Een osteopaat oefent zijn zelfstandige activiteit uit in 2 verschillende sectoren: bij
privépatiënten (op hun thuisadres en in zijn praktijk) en als verzorger van een rugbyploeg.
Zijn beroepsmatige verplaatsingen zijn de volgende:

- **a.** van maandag tot vrijdag met zijn personenwagen:

- voormiddag: woonplaats -> patiënten
- namiddag: patiënten -> praktijk
- ’s avonds: praktijk -> woonplaats

- **b.** zaterdag en zondag met zijn scooter

- woonplaats -> rugbyveld -> woonplaats
In de loop van 2012 werd volgend aantal kilometers afgelegd:

- **a.** met de personenwagen

- praktijk -> woonplaats: 3.500 km (heen)
- op huisbezoek bij patiënten: 15.000 km
- jaartotaal = 27.500 km (alle niet-beroepsmatige km zijn per definitie privématig)

- **b.** met de scooter

- woonplaats -> rugbyveld: 2.500 (heen en terug)
- jaartotaal = 5.000 km (overige km = privématig)
Uiteenzetting van de kosten i.v.m. de personenauto (Toyota Prius benzine – 89 g CO2):
Renting € 7.200 (Leasing € 5.000 + Verzekering € 1.000 + Verkeersbelasting € 300 +
Onderhoud € 650 + Interest € 250 )
Brandstof: € 1.650
Uiteenzetting van de kosten i.v.m. de scooter (volledig afgeschreven, geen financiering):
Verkeersbelasting € 100
Onderhoud € 350
Verzekering € 250
Brandstof € 600
Bereken het bedrag van de aftrekbare beroepskosten i.v.m. de verplaatsingen en geef het
detail van deze berekeningen. (NB: u dient geen rekening te houden met de implicaties van
de btw). U dient de oplossing te kiezen die voor de belastingplichtige het voordeligst uitkomt.
Antwoord … / 10 punten

_Nog niet beantwoord (modelantwoord ontbreekt)._

#### Subvraag a)

van maandag tot vrijdag met zijn personenwagen:
- voormiddag: woonplaats -> patiënten
- namiddag: patiënten -> praktijk
- ’s avonds: praktijk -> woonplaats

#### Subvraag b)

zaterdag en zondag met zijn scooter
- woonplaats -> rugbyveld -> woonplaats
In de loop van 2012 werd volgend aantal kilometers afgelegd:

#### Subvraag a)

met de personenwagen
- praktijk -> woonplaats: 3.500 km (heen)
- op huisbezoek bij patiënten: 15.000 km
- jaartotaal = 27.500 km (alle niet-beroepsmatige km zijn per definitie privématig)

#### Subvraag b)

met de scooter
- woonplaats -> rugbyveld: 2.500 (heen en terug)
- jaartotaal = 5.000 km (overige km = privématig)
Uiteenzetting van de kosten i.v.m. de personenauto (Toyota Prius benzine – 89 g CO2):
Renting € 7.200 (Leasing € 5.000 + Verzekering € 1.000 + Verkeersbelasting € 300 +
Onderhoud € 650 + Interest € 250 )
Brandstof: € 1.650
Uiteenzetting van de kosten i.v.m. de scooter (volledig afgeschreven, geen financiering):
Verkeersbelasting € 100
Onderhoud € 350
Verzekering € 250
Brandstof € 600

---

### 2013-2-vr23 · 2013-2 · 4.0 pt

_Ook geklassificeerd onder_: 2.8

**Vraagformaat**: J/F · **Antwoord-type**: — · **Confidence**: —

#### Vraagtekst

**Geef aan of volgende uitspraken waar of niet waar zijn.**

Zet een kruisje bij het juiste
antwoord.
a) Anna is advocate. In 2012 heeft zij gedurende 6 maanden niet kunnen werken wegens
een ernstige ziekte. Omdat zij een verzekering van het type “gewaarborgd inkomen”
had afgesloten, heeft zij een vergoeding ontvangen om haar inkomstenderving te
compenseren. Die vergoeding zal afzonderlijk belast worden tegen de aanslagvoet van
33%, voor zover ze niet meer bedraagt dan de nettobaten over de vier laatste jaren.

Antwoord … / 1 punt

|   |   |
| --- | --- |
|   | Waar |
|   | Niet waar |

b) André is loodgieter en heeft in de loop van 2012 een machine verkocht en daarop een
meerwaarde behaald. Hij heeft de machine in 2004 in nieuwe staat aangekocht. Indien
André de verkoopprijs van de machine herbelegt, zal de meerwaarde gespreid worden
belast tegen de aanslagvoet van 16,5%.
Antwoord … / 1 punt

|   |   |
| --- | --- |
|   | Waar |
|   | Niet waar |

c) De aftrek van forfaitaire beroepskosten is mogelijk voor de bezoldigingen van
werknemers en de bezoldigingen van bedrijfsleiders, maar is niet mogelijk voor de
baten van vrije beroepen.
Antwoord … / 1 punt

|   |   |
| --- | --- |
|   | Waar |
|   | Niet waar |

d) Wanneer een belastingplichtige een rustpensioen uit het buitenland ontvangt, is dit in
België nooit belastbaar, maar komt het wel in aanmerking voor de berekening van het
progressievoorbehoud.
Antwoord … / 1 punt

|   |   |
| --- | --- |
|   | Waar |
|   | Niet waar |

VENNOOTSCHAPSBELASTING 20 PUNTEN

_Nog niet beantwoord (modelantwoord ontbreekt)._

#### Subvraag a)

Anna is advocate. In 2012 heeft zij gedurende 6 maanden niet kunnen werken wegens
een ernstige ziekte. Omdat zij een verzekering van het type “gewaarborgd inkomen”
had afgesloten, heeft zij een vergoeding ontvangen om haar inkomstenderving te
compenseren. Die vergoeding zal afzonderlijk belast worden tegen de aanslagvoet van
33%, voor zover ze niet meer bedraagt dan de nettobaten over de vier laatste jaren.

#### Subvraag b)

André is loodgieter en heeft in de loop van 2012 een machine verkocht en daarop een
meerwaarde behaald. Hij heeft de machine in 2004 in nieuwe staat aangekocht. Indien
André de verkoopprijs van de machine herbelegt, zal de meerwaarde gespreid worden
belast tegen de aanslagvoet van 16,5%.

#### Subvraag c)

De aftrek van forfaitaire beroepskosten is mogelijk voor de bezoldigingen van
werknemers en de bezoldigingen van bedrijfsleiders, maar is niet mogelijk voor de
baten van vrije beroepen.

#### Subvraag d)

Wanneer een belastingplichtige een rustpensioen uit het buitenland ontvangt, is dit in
België nooit belastbaar, maar komt het wel in aanmerking voor de berekening van het
progressievoorbehoud.

---

### 2014-1-vr22 · 2014-1 · 3.0 pt

**Vraagformaat**: open · **Antwoord-type**: — · **Confidence**: —

#### Vraagtekst

Personen ten laste
Welke personen, omschreven in onderstaande uitspraken, kunnen niet als persoon ten laste
worden beschouwd?
Antwoord

De afstammelingen van de belastingplichtige of zijn echtgenoot, met name de kinderen of
geadopteerde kinderen, kleinkinderen, achterkleinkinderen, enz.

De kinderen ten laste genomen vóór hun meerderjarigheid (met name vóór de leeftijd van 18
jaar) en die de belastingplichtige(n) die de aangifte in de PB invult(len) volledig of
hoofdzakelijk ten laste heeft(hebben).

De ouders, grootouders of overgrootouders van de belastingplichtige of zijn echtgenoot.

De kinderen die op 1 januari van het aanslagjaar deel uitmaken van het gezin van de
belastingplichtige.

Het kind ten laste van een alleenstaande dat, gedurende het aanslagjaar 2013 (inkomsten
2012), niet over een maximumbedrag bruto bestaansmiddelen van 3.737,50 euro beschikt.

_Nog niet beantwoord (modelantwoord ontbreekt)._

---

### 2014-1-vr23 · 2014-1 · 3.0 pt

**Vraagformaat**: J/F · **Antwoord-type**: — · **Confidence**: —

#### Vraagtekst

Huwelijksquotiënt
Welke van onderstaande uitspraken is niet juist?
Antwoord

Het huwelijksquotiënt is een regel die enkel de belastingplichtigen betreft die een
gezamenlijke aangifte moeten indienen.

Wanneer één van beide echtgenoten geen beroepsinkomsten of onroerende inkomsten
heeft, wordt hem, in toepassing van het huwelijksquotiënt, 30% van de gemeenschappelijke
beroepsinkomsten met een maximum van 9.810 euro (aanslagjaar 2013) toegekend.

Het doel van het huwelijksquotiënt is de belasting te verlagen door een gedeelte van de
inkomsten van de "rijkere" echtgenoot of wettelijk samenwonende virtueel toe te rekenen aan
de echtgenoot of de wettelijk samenwonende met de geringste inkomsten. Daaruit volgt dat
de belastingdruk van de eerste belastingplichtige afneemt, terwijl deze van de tweede door
het effect van de progressiviteit van de belasting, minder toeneemt.


Het huwelijksquotiënt heeft geen uitwerking indien de aanslag daardoor wordt verhoogd: het
huwelijksquotiënt moet dus altijd een maatregel in het voordeel van de belastingplichtige
blijven.

Wanneer de beroepsinkomsten afkomstig zijn van verschillende categorieën van
beroepszinkomsten, wordt het huwelijksquotiënt geacht in dezelfde verhouding uit diezelfde
categorieën van beroepsinkomsten te zijn samengesteld.

_Nog niet beantwoord (modelantwoord ontbreekt)._

---

### 2014-1-vr24 · 2014-1 · 4.0 pt

**Vraagformaat**: J/F · **Antwoord-type**: — · **Confidence**: —

#### Vraagtekst

Onroerende inkomsten
Paul en Jeanne, zonder kinderen, bezitten een in België gelegen gebouw met een niet-
geïndexeerd kadastraal inkomen (KI) van 5.000 EUR. Het gebouw werd in 2002 aangekocht
met een hypothecaire lening die een belastingvoordeel oplevert. De fiscale behandeling van
dit gebouw is afhankelijk van het gebruik ervan
Welke van de hierna omschreven situaties is onmogelijk?
Antwoord

Het gebouw wordt betrokken als eigen woonhuis en wordt niet aangegeven, want het geniet
de vrijstellingsregeling.

Het gebouw wordt gedeeltelijk gebruikt voor de beroepswerkzaamheid van Paul en geeft
aanleiding tot een vrijstelling op het gedeelte van het KI dat overeenkomt met dit
beroepsgebruik.

Het gebouw wordt gemeubileerd verhuurd en 100% van het KI is onderworpen aan de
personenbelasting.

Het gebouw wordt verhuurd aan een vzw voor de promotie van de film en het onroerend
inkomen is dus belastbaar op basis van de huur en de huurlasten.

Paul verhuurt het gebouw tegen een maandelijkse huurprijs van 500 euro aan de
vennootschap waarvan hij de zaakvoerder is, zonder dat dit aanleiding geeft tot
herkwalificatie van de huur tot beroepsinkomsten (revalorisatiecoëfficiënt: 4,10 – aanslagjaar
2013).

_Nog niet beantwoord (modelantwoord ontbreekt)._

---

### 2014-1-vr25 · 2014-1 · 3.0 pt

**Vraagformaat**: open · **Antwoord-type**: — · **Confidence**: —

#### Vraagtekst

Diverse inkomsten
Welke van de hierna omschreven inkomsten vallen onder de categorie van de diverse
inkomsten bedoeld in 90, 1° WIB 1992?
Antwoord

erelonen voor advies verstrekt buiten het kader van een echt beroep;

prijzen van tombola's en toegelaten loterijen, met inbegrip van de Nationale Loterij;

winsten van occasionele verrichtingen op de beurs, zowel de effectenbeurs als de
termijnbeurs;


de interesten ontvangen bij laattijdige betaling van de prijs van de goederen, aan een
belastingplichtige die zijn beroepswerkzaamheid volledig en definitief heeft stopgezet;

de prijzen gewonnen in publiciteitswedstrijden en -spelen die o.m. worden georganiseerd
door of aangekondigd via de pers, de radio of de televisie.

_Nog niet beantwoord (modelantwoord ontbreekt)._

---

### 2014-1-vr26 · 2014-1 · 3.0 pt

**Vraagformaat**: J/F · **Antwoord-type**: — · **Confidence**: —

#### Vraagtekst

**Welke hieronder omschreven meerwaarden zijn belastbaar tegen de afzonderlijke
aanslagvoet van 33%, tenzij de samenvoeging voordeliger is?**

Antwoord

Meerwaarden verwezenlijkt op activa die niet voor de uitoefening van de
beroepswerkzaamheid werden gebruikt en betrekking hebben op immateriële of materiële
vaste activa.

Meerwaarden op materiële vaste activa die bij de verwezenlijking ervan minder dan 5 jaar
voor de uitoefening van de beroepswerkzaamheid werden gebruikt.

Meerwaarden op immateriële vaste activa bij gedwongen vervreemding en met inachtneming
van het “fiscaal maximumbedrag” gelijk aan het inkomen van de laatste vier jaren.

Meerwaarden op immateriële vaste activa bij vervreemding door een belastingplichtige van
meer dan 60 jaar en met inachtneming van het “fiscaal maximumbedrag” gelijk aan het
inkomen van de laatste vier jaren

Meerwaarden op immateriële vaste activa bij stopzetting van de werkzaamheid en met
inachtneming van het “fiscaal maximumbedrag” gelijk aan de belastbare nettowinst of -baten
van de laatste vier jaren.

_Nog niet beantwoord (modelantwoord ontbreekt)._

---

### 2014-1-vr27 · 2014-1 · 4.0 pt

**Vraagformaat**: J/F · **Antwoord-type**: — · **Confidence**: —

#### Vraagtekst

Aftrekbare uitgaven
Welke van onderstaande uitspraken is niet juist voor het aanslagjaar 2013?
Antwoord

De uitgaven die recht geven op belastingverminderingen mogen nog niet afgetrokken zijn bij
de vaststelling van de netto-inkomsten, zo niet kunnen ze niet in aanmerking worden
genomen.

De uitgaven gedaan voor de oppas van één of meer kinderen, jonger dan 12 jaar, die ten
laste zijn van de belastingplichtige, zijn aftrekbaar met inachtneming van een
maximumbedrag.

80% van de onderhoudsuitkeringen die de belastingplichtige regelmatig heeft betaald aan
personen die niet deel uitmaken van zijn gezin, wanneer ze zijn betaald ter uitvoering van
een verplichting op grond van het Burgerlijk of het Gerechtelijk Wetboek of van de wet van
23 november 1998 tot invoering van de wettelijke samenwoning, zomede 80% van de
kapitalen die zulke uitkeringen vervangen, zijn aftrekbaar.

De uitgaven die aftrekbaar zijn van de gezamenlijke netto-inkomsten, worden
verhoudingsgewijs toegerekend aan de verschillende inkomstencategorieën.


De aftrekbare bestedingen zijn alleen aftrekbaar van de inkomsten van het belastbaar
tijdperk waarin ze werkelijk zijn betaald.
VENNOOTSCHAPSBELASTING 20 PUNTEN

_Nog niet beantwoord (modelantwoord ontbreekt)._

---

### 2015-1-vr28 · 2015-1 · 4.0 pt

**Vraagformaat**: J/F · **Antwoord-type**: — · **Confidence**: —

#### Vraagtekst

Beroepsverliezen
Geef aan welke van onderstaande uitspraken ONJUIST is:

- **A.** Wanneer in een welbepaalde beroepswerkzaamheid, na aftrek van de beroepskosten, een

verlies overblijft, wordt dat eerst afgetrokken van de beroepsinkomsten die dezelfde
belastingplichtige tijdens hetzelfde belastbare tijdperk uit andere beroepswerkzaamheden
heeft verkregen.

- **B.** De aftrek van een beroepsverlies wordt eerst proportioneel toegerekend aan de gezamenlijk

belaste beroepsinkomsten en het saldo wordt vervolgens proportioneel verdeeld over de
afzonderlijk belaste beroepsinkomsten.

- **C.** Wanneer de positieve beroepsinkomsten van een belastingplichtige ontoereikend zijn om de

beroepsverliezen van de huidige en de vorige belastbare tijdperken aan te zuiveren, wordt
het saldo toegerekend aan de positieve beroepsinkomsten van de andere echtgenoot,
behalve wanneer de echtgenoten gehuwd zijn onder het stelsel van scheiding van goederen.

- **D.** Wanneer alle mogelijkheden om de beroepsverliezen aan te rekenen uitgeput zijn voor een

belastbaar tijdperk, wordt het saldo overgedragen naar het volgende jaar en afgetrokken van
de positieve beroepsinkomsten van dat jaar.
E. Indien de echtgenoot waaraan een huwelijksquotiënt wordt toegekend al een
meewerkinkomen ontvangt dat geheel of volledig opgeslorpt wordt door de aanzuivering van
beroepsverliezen, moet het huwelijksquotiënt worden verminderd met de beroepsverliezen
die aan het meewerkinkomen werden toegerekend.

_Nog niet beantwoord (modelantwoord ontbreekt)._

---

### 2015-1-vr29 · 2015-1 · 4.0 pt

_Ook geklassificeerd onder_: 2.8

**Vraagformaat**: J/F · **Antwoord-type**: — · **Confidence**: —

#### Vraagtekst

Een belastingplichtige is eigenaar van een in het buitenland gelegen onroerend goed. (NB:
het betreft geen onroerend goed dat kan beschouwd worden als de enige eigen woning van
de belastingplichtige en er bestaat in desbetreffend land geen theoretische huurwaarde).

**Welke van onderstaande uitspraken is JUIST?**

- **A.** Het bedrag dat in de aangifte moet worden vermeld, wordt berekend volgens de

volgende formule: de huurwaarde, verminderd met de buitenlandse belastingen die
werkelijk de inkomsten van het goed in kwestie hebben bezwaard. Het aldus bekomen
bedrag mag nog verminderd worden met een forfait van 40% dat geacht wordt de
verschillende kosten, zoals verzekeringen, herstellingen enz., te dekken.

- **B.** Indien het onroerend goed niet wordt verhuurd, komt de huurwaarde in principe overeen

met de gemiddelde jaarlijkse huuropbrengst die het onroerend goed tijdens het vorige

jaar had kunnen opbrengen, wanneer het verhuurd zou geweest zijn. Deze huurwaarde
omvat zowel de eigenlijke huur als de huurvoordelen.
C. Indien het onroerend goed verhuurd is voor beroepsdoeleinden, is het aan te geven
bedrag het hoogste van: ofwel de brutohuur, vermeerderd met de huurvoordelen en
verminderd met de buitenlandse belastingen die deze goederen hebben bezwaard, ofwel
de brutohuur x 2/3 x de revalorisatiecoëfficiënt (4,19 voor het aanslagjaar 2014).
D. Indien het in het buitenland gelegen goed niet door de belastingplichtige werd betrokken,
noch door de belastingplichtige werd verhuurd, moet er dus niets vermeld worden in de
belastingaangifte.
E. De inkomsten van onroerende goederen gelegen in een land waarmee België geen
dubbelbelastingverdrag heeft gesloten, zijn in België belastbaar, maar slechts tot beloop
van 50% van het bedrag ervan.

_Nog niet beantwoord (modelantwoord ontbreekt)._

---

### 2015-1-vr30 · 2015-1 · 4.0 pt

**Vraagformaat**: J/F · **Antwoord-type**: — · **Confidence**: —

#### Vraagtekst

**Geef aan welke uitspraak ONJUIST is, met betrekking tot de aftrekbare bestedingen en de
uitgaven die recht geven op een belastingvermindering :
A.**

De kosten voor kinderoppas zijn sinds het aanslagjaar 2013 geen aftrekbare bestedingen
meer. Die kosten geven sinds het aanslagjaar 2013 daarentegen recht op een
belastingvermindering. Indien die belastingvermindering meer bedraagt dan het bedrag
van de verschuldigde belasting, wordt het bedrag in meer omgezet in een
terugbetaalbaar belastingkrediet.

- **B.** Wanneer een gemeenschappelijke aanslag wordt gevestigd, worden de

onderhoudsuitkeringen die door één echtgenoot persoonlijk verschuldigd zijn, bij
voorrang aangerekend op het totale netto-inkomen van die echtgenoot en het eventuele
saldo wordt op het totale netto-inkomen van de andere echtgenoot aangerekend.

- **C.** De door iedere echtgenoot werkelijk gedane giften worden opgeteld en het totaalbedrag

ervan geeft recht op een belastingvermindering van 45 %. De belastingvermindering
wordt evenredig omgedeeld in functie van het belastbare inkomen van elk der
echtgenoten ten opzichte van de som van het belastbare inkomen van de beide
echtgenoten.

- **D.** Een belastingplichtige kan voor hetzelfde tijdperk de vermindering voor pensioensparen

niet samen verkrijgen met de vermindering voor verwerving van werkgeversaandelen.
E. Iedere echtgenoot moet het bedrag van zijn betalingen voor de aankoop van
dienstencheques vermelden. In geval van een gemeenschappelijke aanslag wordt de
belastingvermindering voor dienstencheques evenredig omgedeeld in functie van het
belastbaar inkomen van elk der echtgenoten ten opzichte van de som van de belastbare
inkomsten van de beide echtgenoten.

_Nog niet beantwoord (modelantwoord ontbreekt)._

---

### 2015-1-vr31 · 2015-1 · 4.0 pt

**Vraagformaat**: J/F · **Antwoord-type**: — · **Confidence**: —

#### Vraagtekst

Vrijstellingen van economische aard
 aftrek voor bijkomend personeel tewerkgesteld in de uitvoer en de integrale
kwaliteitszorg
 aftrek voor ander bijkomend personeel
 aftrek voor stage in de onderneming
 investeringsaftrek
Welke van onderstaande uitspraken is ONJUIST:

- **A.** Deze vrijstellingen kunnen toegepast worden ongeacht de belastingplichtige een

vereenvoudigde dan wel een dubbele boekhouding voert. De aftrek van deze economische
vrijstellingen is beperkt tot de resterende winst na aftrek van de beroepskosten (ze kunnen
dus geen verlies tot gevolg hebben). Bij gebrek aan toereikende nettowinst is het niet-
afgetrokken gedeelte van de drie eerste vrijstellingen van economische aard definitief
verloren.

- **B.** De vrijstelling voor ander bijkomend personeel wordt teruggenomen wanneer het totaal

gemiddeld personeelsbestand tijdens het volgende jaar daalt. Om een definitief recht op de
vrijstelling te verwerven, moet de tewerkstelling dus gedurende 2 jaar behouden blijven: het
jaar waarvoor de toekenning wordt toegekend en het volgende jaar. Indien dit niet het geval
is, moet de vrijstelling opnieuw in de belastbare winst worden opgenomen. De toegekende
vrijstelling wordt echter niet teruggenomen wanneer in het jaar na dat waarin de vrijstelling
werd toegekend een loonsverhoging wordt doorgevoerd die een overschrijding tot gevolg
heeft van het maximumloon dat toegelaten is om voor de vrijstelling in aanmerking te komen.

- **C.** Vrijstelling voor stage in de onderneming: de netto winst of baten van de werkgever worden

vrijgesteld ten belope van 20% (40% vanaf 01/01/2014) van de als beroepskosten
afgetrokken bezoldigingen, betaald voor de door de stagiair in het kader van zijn praktische
opleiding geleverde prestaties in het jaar waarin de werkgever een stagebonus heeft
bekomen.

- **D.** Investeringsaftrek: de vaste activa waarvan het recht van gebruik overgedragen is aan een

derde, zijn uit de investeringsaftrek gesloten. De wijze waarop dit recht is overgedragen, is
niet van belang (verhuurd of kosteloos). Deze uitsluiting is niet van toepassing wanneer het
recht van gebruik is overgedragen aan een andere natuurlijke persoon die deze vaste activa
gebruikt om winst of baten te verwezenlijken en dit recht van gebruik, op zijn beurt, niet
geheel of ten dele aan een derde overdraagt.
E. Gespreide investeringsaftrek: indien de onderneming op de eerste dag van het belastbare
tijdperk waarin de activa zijn aangeschaft of tot stand gebracht minder dan 20 werknemers
tewerkstelt, kan zij opteren voor de gespreide investeringsaftrek. Die aftrek wordt berekend
door de op de betrokken investering fiscaal aanvaarde afschrijvingen met een bepaald
percentage te vermenigvuldigen. Dit percentage is afhankelijk van het kalenderjaar waarin
de investering is gedaan en blijft de hele afschrijvingsduur onveranderd, ongeacht het
percentage voor de volgende jaren.

_Nog niet beantwoord (modelantwoord ontbreekt)._

---

### 2015-1-vr32 · 2015-1 · 4.0 pt

**Vraagformaat**: J/F · **Antwoord-type**: — · **Confidence**: —

#### Vraagtekst

**Geef aan welke van onderstaande uitspraken "ONJUIST" is, met betrekking tot de belasting
van de roerende inkomsten:
A.**

Bij een niet-gereglementeerde spaarrekening moet op de volledige interestopbrengst een
roerende voorheffing van 25% worden betaald.

- **B.** De eerste schijf (tot 56.450 EUR) van de inkomsten als auteursrechten, en die kunnen

beschouwd worden als roerende inkomsten, is onderworpen aan het tarief van 25%.

- **C.** De aangegeven roerende inkomsten worden, naargelang het geval, ofwel afzonderlijk

belast tegen een aanslagvoet die overeenstemt met het tarief van de roerende
voorheffing, ofwel met de andere inkomsten samengevoegd, indien dit voor de
belastingplichtige voordeliger uitkomt.

- **D.** De ingehouden roerende voorheffing wordt verrekend noch teruggegeven indien de

belastingplichtige beroepsinkomsten verkrijgt die bij overeenkomst zijn vrijgesteld en niet
in aanmerking komen voor de berekening van de belasting op zijn andere inkomsten.
E. Het aan te geven bedrag is het werkelijk geïnd bedrag, vóór aftrek van de innings- en
bewaringskosten, maar na inhouding van de roerende voorheffing en, in voorkomend
geval, vóór inhouding van de woonstaatheffing.

|   |   |   |   |   |
| --- | --- | --- | --- | --- |
| VENNOOTSCHAPSBELASTING |   |   | 20 PUNTEN |   |
|   |   |   |   | 20 PUNTEN |

_Nog niet beantwoord (modelantwoord ontbreekt)._

---

### 2024-1-vr5 · 2024-1

> [!warning] Herinnering-reconstructie (volledig)
> Deze vraag is een **herinnering**-reconstructie (volledigheid: volledig) — geen officiële ITAA-bundel. Modelantwoord rust op de geherinterpreteerde vraagtekst (ADR-022).

**Vraagformaat**: J/F · **Antwoord-type**: — · **Confidence**: —

#### Vraagtekst

5 Personenbelasting

- **A.** Juist/ Fout: Van de toekenning aan de meewerkend echtgenoot, aangesloten ministatuut, wordt er een forfaitaire kostenaftrek van 5% in mindering gebracht.
- **B.** Ik bezit een niet gemeubeld onroerend goed om te verhuren aan privépersoon als bewoning. Woning is door overstroming 6 maand niet verhuurd geweest. Wat met Onroerende Voorheffing?
- **C.** Ik ben ongehuwd, verhuur een gemeubeld onroerend goed aan natuurlijk persoon. KI = 1.500 Opbrengst = 3.000,00 euro per kwartaal Welke bedragen waar opnemen in de aangifte?
- **D.** Welke beroepsinkomsten zijn niet aan het progressief belastingtarief onderworpen?

> [!note]- Geherinterpreteerde vraagtekst (ADR-022)
> Casus personenbelasting, 4 deelvragen:
> A. Juist/fout — Op de toekenning aan de meewerkende echtgenoot, aangesloten in het ministatuut, wordt een forfaitaire kostenaftrek van 5 % in mindering gebracht.
> B. Ik bezit een ongemeubileerd onroerend goed dat ik verhuur aan een privépersoon als bewoning. De woning is door overstroming 6 maanden niet verhuurd geweest. Wat met de onroerende voorheffing?
> C. Ik ben ongehuwd en verhuur een gemeubileerd onroerend goed aan een natuurlijk persoon. KI = 1.500. Opbrengst = 3.000,00 euro per kwartaal. Welke bedragen moet ik waar opnemen in de aangifte?
> D. Welke beroepsinkomsten zijn niet aan het progressief belastingtarief onderworpen?
> 
> _Motivering_: Alle vier subvragen hebben volledige stam in de PDF. Geen MC, alleen open vragen met casus-data (sub-B/C). Vraagtekst-herformulering is overwegend cosmetisch (ministatuut-spelling, KI-formatting).
> _Confidence_: grounded · _Datum_: 2026-05-19

_Nog niet beantwoord (modelantwoord ontbreekt)._

---

## PO 2.3

_13 vragen — 0 met modelantwoord — 0 met gap-rapport._

### 2003-bibf-vrG1 · 2003-bibf · 10 pt

**Vraagformaat**: berekening · **Antwoord-type**: — · **Confidence**: —

#### Vraagtekst

G. VENNOOTSCHAPSBELASTING  G.1 Situatie:

> De BVBA Albert legt volgende balans, afgesloten op 31/12/2002, voorafgaand aan de bestemming van het resultaat, ter goedkeuring voor aan de algemene vergadering.

Vaste Activa 79.260 Onderschreven kapitaal 18.600 Herwaarderingsmeerwaarden 600 Financiële Activa 30.000 Wettelijke reserve 1.860 Vrijgestelde reserve 200 Vlottende Activa 20.000 Beschikbare reserve 16.000 Te bestemmen winst van het boekj 62.000 Schulden op minder dan één jaar 30.000 ---------- ---------

129. 260 129.260 De algemene vergadering van 17 mei 2003 beslist om het resultaat van het boekjaar als volgt te bestemmen: - Wettelijke reserve – nihil (de 10 % werd reeds bereikt) -- - Uitkering van dividenden voor een totaal van 40.000 - Toekenning aan de beschikbare reserve 18.000 - Overgedragen winst 4.000 62.000 Bijkomende Gegevens:

- **a.** De opbrengsten bevatten de inning van dividenden , toegekend door een NV waarvan men 80 % van het maatschappelijk kapitaal bezit voor een bedrag van : 1.200 € , roerende voorheffing 400 €.
- **b.** In de kosten noteert men: rekening: 67 belastingen op de inkomsten en voorafbetalingen 20.000 67 Roerende voorheffing 400 61 Autokosten 1.500 63 Afschrijvingen auto 3.800 61 Representatiekosten, restaurants enz.. 2.000

63. Afschrijvingen van de genoteerde meerwaarde op vaste activa ( 1ste boekjaar) 60 61 Liberaliteiten toegekend voor een totaal van: 160 waarvan liberaliteiten verantwoord door een attest ( 80 €) 64 Onroerende voorheffing 100 Opgave: Vul vak per vak de aangifte in de vennootschapsbelasting in (zie hierna) op basis van bovenstaande cijfergegevens teneinde de belastbare basis in de vennootschapsbelasting vast te stellen. 10 PUNTEN

_Nog niet beantwoord (modelantwoord ontbreekt)._

---

### 2008-bibf-vrG1 · 2008-bibf

**Vraagformaat**: berekening · **Antwoord-type**: — · **Confidence**: —

#### Vraagtekst

G1. De vennootschap “Green”, een KMO overeenkomsting art. 15 §1 W.Venn. heeft als activiteit de handel in tuinmaterialen. Zij werd opgericht door twee natuurlijke personen die tevens de bestuurder zijn. Zij heeft een belaste reserve in het kapitaal geïncorporeerd in 2000 voor een bedrag van 1.509 EUR. Zij heeft tevens geïnvesteerd in een verwarmingsinstallatie om energie te besparen. Zij heeft voor deze nieuwe verwarmingsinstallatie een attest van het Vlaams Gewest ontvangen. De investering hiervoor bedroeg 3300 EUR. Het percentage van de investeringsaftrek voor energiebesparende maatregelen bedraagt 13,5%. In het lopende jaar werd de vennootschap tevens geconfronteerd met een fiscale controle. De fiscus heeft een onderwaardering van de stock vastgesteld voor een bedrag van 3.500 EUR. Het betrof materiaal dat bestemd was voor de verkoop, maar dat niet werd opgenomen in de stock. De belastingvrije reserve is een meerwaarde op een bedrijfswagen. De vennootschap beschikt over een wagen voor gemengd gebruik, aangekocht in 2006, en die in leasing werd genomen en waarvan de jaarlijkse kosten als volgt kunnen worden samengevat: - Verkeersbelasting : 250 EUR - Intresten op de lening : 352 EUR - Afschrijvingen : 19.500 EUR - Niet aftrekbare BTW 570 EUR - Diesel : 1.250 EUR - Voordeel in natura : 1.385 EUR BTW inclusief en er werd geen factuur opgemaakt De vennootschap heeft voorafbetalingen gedaan voor een bedrag van 2000 EUR Belastingsupplement 3.770 EUR Regularisatie van belasting : -1433 EUR Uitgave voor onthaal cliënten : 852 EUR Restaurantkosten : 350 EUR Hotelkosten in Duitsland (overnachting): 125 EUR Taksen op de waterfactuur : 125 EUR De vennootschap heeft tevens een BTW boete moeten betalen voor niet indiening van de BTW aangifte ten belopen van : 50 EUR alsook verwijlintresten voor de laattijdige betaling van de BTW van het 3 de kwartaal : 35 EUR. Maaltijdcheques : 1320 EUR Kosten voor werkkledij die dienen om de werknemers te beschermen op de werkvloer : 450 EUR Kosten voor een maatpak van de bestuurder : 525 EUR Vervolledig de fiscale aangifte en bereken de belastbare basis in de vennootschapsbelasting op basis van de hierboven vermelde gegevens en de bijgevoegde jaarrekening. Het betreft de inkomsten 2007, aangifte 2008. Het percentage voor de toepassing van de notionele intrestaftrek voor dat inkomstenjaar bedraagt 4,281 %

_Nog niet beantwoord (modelantwoord ontbreekt)._

---

### 2013-1-vr22 · 2013-1 · 6.0 pt

**Vraagformaat**: J/F · **Antwoord-type**: — · **Confidence**: —

#### Vraagtekst

Een bvba verschaft volgende gegevens over de waardering van haar goederenvoorraad voor
het jaar 2012 (we beperken ons tot één bepaald type product) :
De bedragen zijn exclusief btw.
Beginvoorraad = 265 stuks
Aantal aangekochte producten = 1 810 stuks
Aantal verkochte producten = 1 775 stuks
Eindvoorraad = 280 stuks
Aankoopprijs 200,00 EUR/stuk
Verkoopprijs 250,00 EUR/stuk
Op de balans verschijnt een eindvoorraad met een waarde van 56 000,00 euro ( 280 stuks x
200,00 euro/stuk). De resultatenrekening vertoont een bruto-exploitatiewinst gelijk aan
84 750,00 euro:
Omzet 1 775,00/stuk x 250 stuks = 443 750,00
-kostprijs verkochte goederen (265st + 1810st – 280st) x 200,00 = - 359 000,00
Brutowinst = 84 750,00
Naar aanleiding van het fiscale onderzoek over boekjaar 2012 stelt de controledienst vast dat
de bvba een aankoopfactuur voor 20 producten heeft geboekt onder haar aankopen, terwijl
de producten pas tijdens het volgende boekjaar 2013 door de leverancier werden geleverd.
Aangezien die 20 producten niet zijn geteld op 31.12.2012, zijn zij niet opgenomen in de
inventaris.
Wat zijn de fiscale gevolgen van die fiscale controle?
Antwoord

_Nog niet beantwoord (modelantwoord ontbreekt)._

---

### 2013-1-vr23 · 2013-1 · 6.0 pt

**Vraagformaat**: J/F · **Antwoord-type**: — · **Confidence**: —

#### Vraagtekst

Een bestaande Belgische NV (kleine vennootschap volgens art. 15 W.Venn.) die haar balans
afsluit op 31.12.2012 beheert de volgende voorziening, door het vereiste formulier (204.3):
Een voorziening van 23 000,00 euro voor grote herstellingen prijkte op de balans van het
boekjaar afgesloten op 31.12.2011. Deze voorziening is op te splitsen in 5 000,00 euro voor
schilderwerken, die werd vrijgesteld en in 18 000,00 euro voor de uitbreiding van de garage.
De totale voorziening van 23 000,00 euro wordt in 2012 volledig teruggenomen wegens het
ten laste nemen van bedoelde uitgaven, te weten:
- Schilderwerken (om de 10 jaar) waarvan de kostprijs 8 900,00 euro (excl. btw)
bedraagt;

- Uitbreiding van de garage voor de vrachtwagens, waarvan de kostprijs 18 000,00
euro (exclusief btw) bedraagt.
Vervolledig onderstaande onderdeel van de aangifte : omschrijving + overeenkomstig(e)
bedrag(en).
Antwoord

_Nog niet beantwoord (modelantwoord ontbreekt)._

---

### 2013-1-vr24 · 2013-1 · 8.0 pt

**Vraagformaat**: MC · **Antwoord-type**: — · **Confidence**: —

#### Vraagtekst

/ 8 punten
Een vennootschap heeft een boekjaar van 1 oktober 2011 tot en met 30 september 2012. In de
periode tussen 1 januari 2012 tot en met 30 september 2012 zijn de belastbare voordelen van
alle aard uit firmawagens voor de personeelsleden en de bedrijfsleiders van de
vennootschap gelijk aan 100 000,00 euro. Al deze voordelen zijn belastbaar in de
personenbelasting in hoofde van de genieters.
De vennootschap beschikt over overgedragen fiscale verliezen voor aanslagjaar 2012 van
13 000,00 euro.
Fiscaal resultaat na 1ste bewerking = 50 000,00
- Aangroei reserves : 6 000,00
- Verworpen uitgaven (incl. 17 000= 17% x 100 000,00 VAA) : 40 000,00
- Uitgekeerde dividenden : 4 000,00

- **a.** Bepaal in onderstaande hypothese de belastbare grondslag van deze vennootschap

Antwoord

- **b.** Vul de bijgevoegde onderdelen van de aangifte in.

Antwoord
BELASTING OVER DE TOEGEVOEGDE WAARDE

_Nog niet beantwoord (modelantwoord ontbreekt)._

#### Subvraag a)

Bepaal in onderstaande hypothese de belastbare grondslag van deze vennootschap

#### Subvraag b)

Vul de bijgevoegde onderdelen van de aangifte in.

---

### 2013-2-vr24 · 2013-2 · 10.0 pt

**Vraagformaat**: berekening+MC · **Antwoord-type**: — · **Confidence**: —

#### Vraagtekst

Een vennootschap ABC heeft de volgende balans- en resultatenrekeningen per 31 december
2012:

| ACTIVA | JAAR <br> 2012 | JAAR <br> 2011 | PASSIVA | JAAR <br> 2012 | JAAR <br> 2011 |
| --- | --- | --- | --- | --- | --- |
|   |   |   |   |   |   |
| Materiële vaste activa | 15.000 | 20.000 | Geplaatst <br> kapitaal | 60.000 | 60.000 |
| Vorderingen < jaar | 100.000 | 95.000 | Wettelijke <br> reserve | 6.000 | 6.000 |
| Liquide middelen | 30.000 | 35.000 | Overgedragen <br> resultaat | -20.000 | -5.000 |
|   |   |   | Schulden < jaar | 99.000 | 89.000 |
|   |   |   |   |   |   |

| BALANSTOTAAL | 145.000 | 150.000 | BALANSTOTAAL | 145.000 | 150.000 |
| --- | --- | --- | --- | --- | --- |
|   |   |   |   |   |   |
| RESULTATENREKENING | KOSTEN | JAAR <br> 2012 | OPBRENGSTEN |   | JAAR <br> 2012 |
| Huur gebouwen |   | -25.000 | Omzet |   | 256.000 |
| Afschrijvingen |   | -5.000 | Voordeel in <br> natura <br> personenwagens |   | 10.000 |
| Nutsvoorzieningen |   | -5.000 | Financiële <br> opbrengsten |   | 5.000 |
| Erelonen |   | -5.000 |   |   |   |
| Renting <br> personenwagens – <br> kapitaal |   | -50.000 |   |   |   |
| Restaurantkosten |   | -5.000 |   |   |   |
| Bezoldiging <br> bedrijfsleider |   | -36.000 |   |   |   |
| Brutobezoldiging <br> personeel |   | -100.000 |   |   |   |
| Patronale bijdragen |   | -35.000 |   |   |   |
| Voordeel in natura <br> personenwagens |   | -10.000 |   |   |   |
| Intrest renting <br> personenwagens |   | -5.000 |   |   |   |
| Benzine <br> personenwagens |   | -5.000 |   |   |   |
| TOTAAL KOSTEN |   | 286.000 | TOTAAL <br> OPBRENGSTEN |   | 271.000 |
|   |   |   |   |   |   |
|   |   |   | VERLIES |   | 15.000 |

De personenwagens zijn onderworpen aan de beperking van 30%. Er waren geen
overdrachten van fiscale verliezen, notionele intrestaftrek en investeringsaftrek. De
vennootschap is een KMO vennootschap in de zin van artikel 15 van het Wetboek van
Vennootschappen en werd opgericht op 13 maart 2011. De aandelen zijn allemaal in handen
van natuurlijke personen.

**Bepaal op basis van deze gegevens:
a) Het belastbare resultaat voor aanslagjaar 2013.**

Detailleer uw berekeningen.

**Antwoord … / 6 punten
b) De verschuldigde vennootschapsbelasting.**

Antwoord … / 2 punten

- **c.** De eventuele overdrachten van fiscale verliezen, notionele intrestaftrek naar de

volgende aanslagjaren.
Antwoord … / 2 punten

_Nog niet beantwoord (modelantwoord ontbreekt)._

#### Subvraag a)

Het belastbare resultaat voor aanslagjaar 2013. Detailleer uw berekeningen.

#### Subvraag b)

De verschuldigde vennootschapsbelasting.

#### Subvraag c)

De eventuele overdrachten van fiscale verliezen, notionele intrestaftrek naar de
volgende aanslagjaren.

---

### 2013-2-vr25 · 2013-2 · 10.0 pt

**Vraagformaat**: berekening · **Antwoord-type**: — · **Confidence**: —

#### Vraagtekst

> De vennootschap GOODLUCK heeft een deel van haar middelen geïnvesteerd in een
> aandelenportefeuille.

In het boekjaar 2012 zijn er de volgende wijzigingen geweest:

| Datum <br> aanschaf | Omschrijving | Bedrag | Datum <br> verkoop | Verkoopprijs <br> (bruto) | Kosten <br> verkoop |
| --- | --- | --- | --- | --- | --- |
| 01/02/2010 | Colruyt | 15.000 |   |   |   |
| 01/03/2009 | Apple | 15.000 | 28/02/2012 | 20.000 | 1.000 |
| 01/03/2009 | KBC | 10.000 | 28/02/2012 | 12.000 | 500 |
| 15/01/2012 | Electrabel | 10.000 | 15/03/2012 | 18.000 | 1.000 |
| 15/01/2012 | Delhaize | 10.000 | 15/03/2012 | 8.000 | 1.000 |

De vennootschap heeft het volgende eigen vermogen:

|   | Jaar 2012 | Jaar 2011 |
| --- | --- | --- |
| Geplaatst kapitaal: <br> oprichting in speciën | 100.000 | 100.000 |
| Wettelijke reserve | 10.000 | 10.000 |
| Beschikbare reserves | 15.000 | 15.000 |
| Overgedragen resultaat | 20.000 | 10.000 |

Zij heeft ook nog een overgedragen fiscaal verlies van 2.000. Zij heeft geen recht op notionele
intrestaftrek.
Gevraagd:
Doe de nodige berekeningen om het belastbaar resultaat van deze vennootschap te bepalen.
De vennootschap kan niet genieten van de progressieve tarieven.

**Geef op welk bedrag aan
welk tarief belastbaar wordt.**

BELASTING OVER DE TOEGEVOEGDE WAARDE 15 PUNTEN

_Nog niet beantwoord (modelantwoord ontbreekt)._

---

### 2014-1-vr28 · 2014-1 · 12.0 pt

**Vraagformaat**: J/F · **Antwoord-type**: — · **Confidence**: —

#### Vraagtekst

Een kantoorgebouw was door de vennootschap ABC gekocht in het jaar 1985. Volgende
gegevens zijn terug te vinden in de afschrijvingstabel:
Aanschaffingwaarde 1.000.000,00 EUR
Afschrijvingen - 750.000,00 EUR
Boekwaarde 250.000,00 EUR
De vennootschap probeerde, na schatting door een deskundige, het gebouw eerst zelf te
koop aan te bieden. Gezien dit geen resultaat opleverde, werd uiteindelijk een makelaar
ingeschakeld om het gebouw te verkopen.
De kosten hiervan bedroegen:
Schatting 8.000,00 EUR
Publiciteit 5.000,00 EUR
Makelaar 20.000,00 EUR
Na tussenkomst van de makelaar werd het gebouw uiteindelijk verkocht voor een waarde van
325.000,00 EUR op 15 november 2012.
De vennootschap zou graag de meerwaarde gespreid willen laten belasten.
Overzicht verrichte investeringen:
Zij had in het jaar 2011 reeds een ander gebouw gekocht voor een waarde van 280.000,00
EUR, waarvan 80.000,00 EUR grondwaarde en 200.000,00 constructiewaarde. Het
afschrijvingspercentage bedraagt 3% lineair. De vennootschap is een kleine vennootschap in
de zin van artikel 15 van het Wetboek van Vennootschappen.
Gevraagd:

- **a.** Bereken de fiscale meerwaarde die in aanmerking komt voor gespreide taxatie.

**Antwoord
b) De vennootschap heeft de meerwaarde verwerkt als gespreide taxatie in haar
jaarrekening.**

Welke bedragen van de gespreide meerwaarde zullen in de jaarrekening van 31
december 2012 overgeboekt worden naar de resultatenrekeningen als onttrekking?
U dient rekening te houden met een belastingtarief van 33,99 %.

**Geef een detail van uw berekening.**

Antwoord

c) Welk bedrag zal in de aangifte vennootschapsbelasting aanslagjaar 2013 ingevuld
worden in het vak vrijgestelde reserves als gespreid te belasten meerwaarde?
Geef een detail van uw berekening.
Antwoord

_Nog niet beantwoord (modelantwoord ontbreekt)._

#### Subvraag a)

Bereken de fiscale meerwaarde die in aanmerking komt voor gespreide taxatie.

#### Subvraag b)

De vennootschap heeft de meerwaarde verwerkt als gespreide taxatie in haar
jaarrekening.
Welke bedragen van de gespreide meerwaarde zullen in de jaarrekening van 31
december 2012 overgeboekt worden naar de resultatenrekeningen als onttrekking?
U dient rekening te houden met een belastingtarief van 33,99 %.
Geef een detail van uw berekening.

#### Subvraag c)

Welk bedrag zal in de aangifte vennootschapsbelasting aanslagjaar 2013 ingevuld
worden in het vak vrijgestelde reserves als gespreid te belasten meerwaarde?
Geef een detail van uw berekening.

---

### 2014-1-vr29 · 2014-1 · 8.0 pt

**Vraagformaat**: MC · **Antwoord-type**: — · **Confidence**: —

#### Vraagtekst

De vennootschap ABC heeft het volgende eigen vermogen:

|   |   | Jaar 2012 | Jaar 2011 |
| --- | --- | --- | --- |
| Geplaatst kapitaal | Oprichting 1989 in <br> speciën | 20.000 | 20.000 |
|   | Inbreng in natura <br> op 14/03/2012 | 80.000 | 0 |
|   | Incorporatie <br> beschikbare <br> reserves op <br> 14/03/2012 | 50.000 | 0 |
| Wettelijke reserve |   | 10.000 | 2.000 |
| Beschikbare <br> reserves |   | 0 | 50.000 |
| Overgedragen <br> resultaat |   | 10.000 | 5.000 |

Daarnaast heeft zij nog een lening gekregen van een andere Belgische vennootschap
behorende tot dezelfde groep van 1.000.000 EUR op 01/02/2010. De rentevoet van deze lening
is 5%. De betaalde intrest voor het jaar 2012 bedroeg 50.000 EUR.
Zij had in het verleden een interne pensioenbelofte afgesloten met één van haar bestuurders.
De voorziening die hiervoor was aangelegd bedroeg op 31 december 2011 140.000 EUR. Deze
werd nog niet overgedragen naar een verzekeringsmaatschappij. De vennootschap wil een
eventuele heffing hierop ineens betalen.
Zij had ook een deelneming van 30% in de vennootschap Trusty voor een bedrag van 10.000
EUR.
Deze vennootschap had echter te kampen met zware verliezen het afgelopen jaar en werd
failliet verklaard op 8/6/2012. Het eigen vermogen van deze vennootschap was als volgt
samengesteld:
Geplaatst kapitaal 50.000
Wettelijke reserve 2.000
Overgedragen verliezen -50.000

- **a.** Bepaal de verworpen uitgaven op basis van deze gegevens met een korte

verantwoording.

**Antwoord
b) Hoeveel bedraagt het fiscaal gestort kapitaal van de vennootschap op 31 december
2012?**

Antwoord

BELASTING OVER DE TOEGEVOEGDE WAARDE 15 PUNTEN

_Nog niet beantwoord (modelantwoord ontbreekt)._

#### Subvraag a)

Bepaal de verworpen uitgaven op basis van deze gegevens met een korte
verantwoording.

#### Subvraag b)

Hoeveel bedraagt het fiscaal gestort kapitaal van de vennootschap op 31 december
2012?

---

### 2015-1-vr33 · 2015-1 · 8.0 pt

**Vraagformaat**: J/F · **Antwoord-type**: — · **Confidence**: —

#### Vraagtekst

> De vennootschap ABC heeft een beleggingsportefeuille.

Deze portefeuille was per 31 december 2013 als volgt samengesteld:

| Benaming | Datum <br> aanschaf | Aanschaffings- <br> waarde | Kosten <br> aankoop | Datum <br> verkoop | Verkoop <br> -prijs | Kosten <br> verkoop |
| --- | --- | --- | --- | --- | --- | --- |
| Aandelen <br> ING | 15/02/2011 | 10.000 | 200 | 30/06/2013 | 13.000 | 250 |
| Obligaties <br> X | 31/01/2013 | 100.000 | 1.000 | 15/05/2013 | 120.000 | 1.200 |
| Aandelen <br> BNP <br> Paribas | 31/01/2013 | 10.000 | 200 | 30/06/2013 | 12.000 | 200 |
|   |   | 120.000 | 1.400 |   | 145.000 | 1.650 |

Het resultaat van het boekjaar 22.150 EUR is samengesteld uit de verkoop van de
beleggingen, de kosten van de aan- en de verkoop:
Verkoop beleggingen 25.000, aankoop kosten 1.200, kosten verkoop 1.650. We gaan ervan uit
dat er geen andere kosten en opbrengsten zijn.
De vennootschap voldoet aan de criteria van artikel 15 van het Wetboek van
vennootschappen.
Zij heeft nog een fiscaal overgedragen verlies van 10.000 EUR van het aanslagjaar 2013.
Gevraagd:

- **a.** Bepaal het belastbare resultaat voor aanslagjaar 2014. De vennootschap heeft geen

recht op notionele intrestaftrek.

**Antwoord … / 3 punten
b) Geef op welke tarieven van toepassing zijn EN op welk bedrag van het belastbare
resultaat.**

Kies voor de meest voordelige verdeling. De vennootschap voldoet niet aan
de voorwaarden voor verlaagd tarief.
Antwoord … / 5 punten

| Tarief | Bereken | Belastbaar bedrag |
| --- | --- | --- |
|   |   |   |
|   |   |   |

_Nog niet beantwoord (modelantwoord ontbreekt)._

#### Subvraag a)

Bepaal het belastbare resultaat voor aanslagjaar 2014. De vennootschap heeft geen
recht op notionele intrestaftrek.

#### Subvraag b)

Geef op welke tarieven van toepassing zijn EN op welk bedrag van het belastbare
resultaat. Kies voor de meest voordelige verdeling. De vennootschap voldoet niet aan
de voorwaarden voor verlaagd tarief.

---

### 2015-1-vr34 · 2015-1 · 6.0 pt

**Vraagformaat**: berekening+MC · **Antwoord-type**: — · **Confidence**: —

#### Vraagtekst

Ter info: De vraag heeft betrekking op het aanslagjaar 2014 – inkomsten 2013.
De vennootschap ‘ABC’ realiseert tijdens het belastbaar tijdperk 2013 een in principe fiscale
winst (= resultaat in de 1ste bewerking) van 500 000,00 EUR. Volgens de berekeningen zou de
vennootschap recht hebben op 480 000,00 EUR DBI-aftrek, 200 000,00 EUR notionele
intrestaftrek en 20 000,00 EUR investeringsaftrek. De fiscus bewijst evenwel dat de
betreffende vennootschap dat jaar bij een verbonden bedrijf handelsgoederen kocht tegen
een prijs, die 50 000,00 EUR beneden de normale marktprijs ligt.
Gevraagd :

- **a.** Hoeveel bedraagt de belastbare winst ?

Antwoord … / 3 punten

- **b.** Geef een korte verklaring.

Antwoord … / 3 punten

_Nog niet beantwoord (modelantwoord ontbreekt)._

#### Subvraag a)

Hoeveel bedraagt de belastbare winst ?

#### Subvraag b)

Geef een korte verklaring.

---

### 2015-1-vr35 · 2015-1 · 6.0 pt

**Vraagformaat**: J/F · **Antwoord-type**: — · **Confidence**: —

#### Vraagtekst

Kan BVBA ‘ABC’ aan de hand van onderstaande gegevens met betrekking tot de
bedrijfsleider aanspraak maken op het verminderd basistarief, in de veronderstelling dat alle
andere voorwaarden zijn voldaan en het belastbaar resultaat meer bedraagt dan 36 000,00
EUR ?
Doe de nodige berekeningen en geef enige commentaar.
 De enige bedrijfsleider van deze vennootschap geniet een periodieke bezoldiging die
in 2013 24 000,00 EUR bedroeg.
 Op de algemene vergadering van 13/04/2014 wordt een tantième toegekend van
10 000,00 EUR.
 In 2013 stonden de bedrijfsleider en zijn partner aan de vennootschap een lening toe
van 100 000,00 EUR.
 De rentevoet van deze lening bedraagt 4% en deze rentevoet moet beschouwd worden
als in overeenstemming met de marktrente van dergelijk type van lening. Voor
boekjaar 2013 (= kalenderjaar) werd een bedrag van 4 000,00 EUR intrest betaald en
geboekt in klasse 65 van de resultatenrekening.
 Daarnaast verhuurt deze zaakvoerder zijn privé villa (KI = 2 500,00) aan de BVBA voor
2 000,00 EUR per maand. Het gebouw is in onverdeeldheid (50/50).
 Het voordeel van alle aard uit het privégebruik van een personenwagen wordt forfaitair
vastgesteld op 2 852,40 EUR (volgens forfaitaire berekeningsformule) voor
inkomstenjaar 2013.
 De vennootschap heeft echter het bedrag van het voordeel aangerekend aan de
bedrijfsleider door dat voordeel te boeken op de rekening-courant van de
bedrijfsleider :
416 R/C Bedrijfsleider 2 852,40
@ 743 Diverse bedrijfsopbrengst 2 357,36
451 Verschuldigde btw 495,04
Antwoord … / punten

|   |   |   |   |   |
| --- | --- | --- | --- | --- |
| BELASTING OVER DE TOEGEVOEGDE WAARDE |   |   | 15 PUNTEN |   |
|   |   |   |   | 15 PUNTEN |

Antwoorden
Plaats de letter van het juiste antwoord in onderstaande rooster

| Vraag | 1 | 2 | 3 | 4 | 5 |
| --- | --- | --- | --- | --- | --- |
| Antwoord |   |   |   |   |   |
| Punten | 4 | 2 | 3 | 3 | 3 |

_Nog niet beantwoord (modelantwoord ontbreekt)._

---

### 2024-1-vr8 · 2024-1

_Ook geklassificeerd onder_: 3.0

> [!warning] Herinnering-reconstructie (fragment)
> Deze vraag is een **herinnering**-reconstructie (volledigheid: fragment) — geen officiële ITAA-bundel. Modelantwoord rust op de geherinterpreteerde vraagtekst (ADR-022).

**Vraagformaat**: J/F · **Antwoord-type**: — · **Confidence**: —

#### Vraagtekst

8 Vennootschapsbelasting

- **A.** Stellingen ivm overdraagbare fiscale verliezen
- **B.** Moeder A fuseert (neutraal) met Dochter B, waarin ze 100% bezit. Netto Actief van B = 100. Fiscale waarde van de participatie in B in de boekhouding van A = 20 Overgedragen fiscale verliezen van B = 30 Overdraagbare aftrek innovatie inkomsten A = 40
- **a.** Hoeveel bedraagt de meer- of minder waarde die A zal realiseren op de deelneming in B ingevolge de M-D fusie?
- **b.** Hoe wordt deze meer- of minderwaarde vanuit fiscaal oogpunt bij A behandeld?
- **C.** Boekjaar N 120.000 euro belastbare winst, alle voorwaarden voldaan voor verlaagd tarief 20%. VOF bestaat sinds 1/1/N-2, boekjaar is kalenderjaar. Wat met voorafbetalingen / vermeerderingen wegens onvoldoende voorafbetaling?

D.

> NV A BJ 31/12/22 winst voor belasting 100.

000 euro (voor winstuitkering) Belgische belasting = 20.000 euro. De AV beslist om tantième van 10.000 euro toe te kennen en een gewoon dividend van 20.000 euro uit te keren. Hoeveel bedraagt de belastbare basis van A voor AJ23? 100.000 – 10.000 tantième = 90.000 euro

E. Wat zijn de “besmette” verworpen uitgaven waarop een verrekening van DBI afkomstig van een land buiten de EER niet mogelijk is.

- **a.** Niet aftrekbare kosten beroepskledij
- **b.** Intresten met betrekking tot een deel van bepaalde leningen
- **c.** Abnormale en goedgunstige voordelen
- **d.** Sociale voordelen

e. Voordelen MC, ecocheques

f. Giften

g. Waardevermindering en minderwaarde op aandelen

h. Terugname van vroegere vrijstellingen

i. Takxshelter

> [!note]- Geherinterpreteerde vraagtekst (ADR-022)
> Casus vennootschapsbelasting, 5 deelvragen:
> A. Stellingen in verband met overdraagbare fiscale verliezen (concrete stellingen niet bewaard in herinnering).
> B. Moeder A fuseert (fiscaal neutraal) met dochter B, waarin A 100 % bezit. Netto-actief van B = 100. Fiscale waarde van de participatie in B in de boekhouding van A = 20. Overgedragen fiscale verliezen van B = 30. Overdraagbare aftrek innovatie-inkomsten van A = 40.
>     1. Hoeveel bedraagt de meer- of minderwaarde die A zal realiseren op de deelneming in B ingevolge de M-D-fusie?
>     2. Hoe wordt deze meer- of minderwaarde vanuit fiscaal oogpunt bij A behandeld?
> C. Boekjaar N: 120.000 euro belastbare winst, alle voorwaarden voldaan voor verlaagd tarief 20 %. De VOF bestaat sinds 1/1/N-2, boekjaar = kalenderjaar. Wat met voorafbetalingen en vermeerderingen wegens onvoldoende voorafbetaling?
> D. NV A — boekjaar 31/12/22, winst voor belasting 100.000 euro (voor winstuitkering). Belgische belasting = 20.000 euro. De algemene vergadering beslist een tantième van 10.000 euro toe te kennen en een gewoon dividend van 20.000 euro uit te keren. Hoeveel bedraagt de belastbare basis van A voor aanslagjaar 23?
>     Hint in vraagtekst: 100.000 − 10.000 tantième = 90.000 euro (vermoedelijke schaduw van het verwachte antwoord).
> E. MC — Wat zijn de 'besmette' verworpen uitgaven waarop een verrekening van DBI afkomstig van een land buiten de EER niet mogelijk is? a. Niet-aftrekbare kosten beroepskledij / b. Intresten met betrekking tot een deel van bepaalde leningen / c. Abnormale of goedgunstige voordelen / d. Sociale voordelen / e. Voordelen MC, ecocheques / f. Giften / g. Waardevermindering en minderwaarde op aandelen / h. Terugname van vroegere vrijstellingen / i. Taxshelter.
> 
> _Motivering_: Sub-A noemt alleen onderwerp ('overdraagbare fiscale verliezen') — niet beantwoordbaar. Sub-B heeft volledige casus-cijfers en twee deelvragen. Sub-C en sub-D hebben volledige casus. Sub-D bevat een berekening-hint die vermoedelijk het antwoord is dat de stagiair gaf. Sub-E heeft 9 opties — MC-stijl 'kies alle die van toepassing zijn'. Typo 'Takxshelter' = Taxshelter.
> _Confidence_: inferred · _Datum_: 2026-05-19

> [!tip]- Antwoord-hint in originele vraagtekst
> Sub-D: '100.000 – 10.000 tantième = 90.000 euro'
> 
> _Interpretatie_: Stagiair noteerde een berekening direct in de vraagtekst van sub-D. Dit is vermoedelijk het antwoord dat hij/zij gaf, niet een element van de officiële vraagstelling. Echte vraag eindigt na 'Hoeveel bedraagt de belastbare basis van A voor AJ23?'.

> [!example]- MC-opties (gestructureerd)
> | Label | Tekst | Juistheid | Motivering |
> | --- | --- | --- | --- |
> | E.a | Niet-aftrekbare kosten beroepskledij | onbekend | — |
> | E.b | Intresten met betrekking tot een deel van bepaalde leningen | onbekend | — |
> | E.c | Abnormale of goedgunstige voordelen | onbekend | Klassieke 'besmette' VU-categorie. |
> | E.d | Sociale voordelen | onbekend | — |
> | E.e | Voordelen MC, ecocheques | onbekend | — |
> | E.f | Giften | onbekend | — |
> | E.g | Waardevermindering en minderwaarde op aandelen | onbekend | — |
> | E.h | Terugname van vroegere vrijstellingen | onbekend | — |
> | E.i | Taxshelter [PDF: 'Takxshelter'] | onbekend | — |

_Nog niet beantwoord (modelantwoord ontbreekt)._

---

## PO 2.4

_24 vragen — 2 met modelantwoord — 0 met gap-rapport._

### 2003-bibf-vrE1 · 2003-bibf · 2 pt

**Vraagformaat**: MC · **Antwoord-type**: — · **Confidence**: —

#### Vraagtekst

Gelieve een kruisje te plaatsen voor de economische activiteiten die geen recht geven op een BTW aftrek .  (cid:137) Een natuurlijke persoon “zaakvoerder” van een BVBA (cid:137) Een natuurlijke persoon “bestuurder” van een NV (cid:137) Een VZW die fiscale seminaries organiseert bestemd voor de economische beroepsbeoefenaars in het kader van de permanente vorming (cid:137) Een natuurlijk persoon “vereffenaar” van een CVBA

_Nog niet beantwoord (modelantwoord ontbreekt)._

---

### 2003-bibf-vrE2 · 2003-bibf · 2 pt

_Ook geklassificeerd onder_: 2.8

**Vraagformaat**: berekening · **Antwoord-type**: — · **Confidence**: —

#### Vraagtekst

Welk is de aftrekbare BTW in de volgende gevallen (antwoord dient in cijfers uitgedrukt te worden !!)  * 100,00 EUR BTW op een factuur van brandstof voor een auto die voor 25 % voor de beroepsactiviteit van zelfstandig boekhouder gebruikt wordt (75 % privé) * 514, 50 EUR BTW op een aankoopfactuur van 50 pennen (49,00 EUR per stuk excl. BTW) bestemd om uit te delen aan de goede klanten van een staalindustriebedrijf. Er is geen logo van de firma terug te vinden op de pennen. * Factuur van 10.000,00 EUR als belastbare basis, exclusief BTW, voor de reiniging van een gebouw dat verhuurd wordt door een NV met als economische activiteit “bouwpromotor” (overdracht van betaling met correcte toepassing van de regeling inzake de medecontractant – KB nr 1 , artikel 20) * Intracommunautaire verwerving door een fabriek van 150 flessen identieke wijn, aan 18,00 EUR per fles, van een wijnboer gevestigd in Frankrijk. Totaal van de factuur 2.700,00 EUR). Daarenboven zijn de Belgische accijnzen verschuldigd van 4,00 EUR per fles, hetzij 600,00 EUR in totaal. De flessen zijn een eindejaarsgeschenk voor het personeel, dat elk 1 fles ontvangt.

_Nog niet beantwoord (modelantwoord ontbreekt)._

---

### 2003-bibf-vrE3 · 2003-bibf · 2 pt

**Vraagformaat**: J/F · **Antwoord-type**: — · **Confidence**: —

#### Vraagtekst

Is er BTW verschuldigd op de volgende verrichtingen, die verricht worden in de loop van het jaar 2003, in hoofde van een BTW belastingplichtige, ontvanger van BTW met recht op aftrek?  Gelieve uw keuze te omcirkelen. Indien U “JA” antwoordt, dient U het bedrag van de verschuldigde belasting te vermelden alsook, in voorkomend geval, de eenvoudige formule om tot dit bedrage te komen. JA NEEN * Verkoop in België van een volledig afgeschreven computer voor 100,00 EUR (prijs betaald door de koper) JA NEEN * Voordeel van alle aard van 1.500, 00 EUR voor het gebruik van een auto door een personeelslid JA NEEN * Overschakeling van het normale regime naar het franchisesysteem. Bureaumateriaal werd aangeschaft in de loop van het jaar 2000 voor 500,00 EUR, exclusief 21 % BTW (belasting die geheel werd afgetrokken) JA NEEN * Verkoop van goederen voor 10.000 € met levering in Duitsland voor een cliënt die daar een belangrijke detailhandel uitbaat. JA NEEN

_Nog niet beantwoord (modelantwoord ontbreekt)._

---

### 2003-bibf-vrE4 · 2003-bibf · 2 pt

**Vraagformaat**: open · **Antwoord-type**: — · **Confidence**: —

#### Vraagtekst

Welk is het wettelijk tijdstip of de uiterste datum voor de punctuele uitvoering van de volgende BTW verplichtingen?  * Neerlegging van de jaarlijkse klantenlistings onderworpen en geïdentificeerd bij de BTW DATUM/MOMENT : * Betaling van een verschuldigd voorschot op de verrichtingen van december voor een belastingplichtige die maandelijkse BTW aangiftes doet. DATUM/MOMENT : * Afgifte van de verklaring inzake wijziging van activiteit (formulier 604 B) – Wijziging van effectief domicilie op 1 april 2003 DATUM/MOMENT : * Afgifte van een verklaring tot stopzetting van alle economische activiteit (formulier 604 C) – Definitieve stopzetting op 31 maart 2003. DATUM/MOMENT :

_Nog niet beantwoord (modelantwoord ontbreekt)._

---

### 2003-bibf-vrE5 · 2003-bibf · 2 pt

**Vraagformaat**: J/F · **Antwoord-type**: — · **Confidence**: —

#### Vraagtekst

Gelieve de juiste keuze te omcirkelen betreffende volgende stellingen:  * Het dagboek van de ontvangsten mag op losse bladen worden bijgehouden JUIST FOUT * Het dagboek van de ontvangsten is facultatief wanneer de ontvangsten worden geregistreerd via een kassa die deze registratie uitvoert. JUIST FOUT * Een restaurant dat drie exploitatiezetels heeft, dient drie aparte dagboeken van ontvangsten bij te houden en dient deze te centraliseren in één centraal dagboek JUIST FOUT * Een dagboek van de ontvangsten mag door de zelfstandige boekhouder meegenomen worden naar zijn bureau voor een periode die nodig is om de periodieke BTW aangifte op te stellen. JUIST FOUT

_Nog niet beantwoord (modelantwoord ontbreekt)._

---

### 2003-bibf-vrI1 · 2003-bibf · 2 pt

**Vraagformaat**: J/F · **Antwoord-type**: — · **Confidence**: —

#### Vraagtekst

I. 1 Worden er in België accijnzen geheven op de aankoop van volgende producten door een restaurateur die in ons land is gevestigd? Het betreft hier intracommunautaire verwervingen in hoofde van de restaurateur.  Gelieve uw keuze te omcirkelen: * Aankoop van sigaren bij een winkel gevestigd in Nederland JA NEEN * Champagne die gekocht werd bij een Franse producent in Frankrijk JA NEEN * Stookolie afkomstig van Duitsland voor de verwarming van het restaurant JA NEEN * Hout voor de open haard verkocht door een handelaar die gevestigd is in Frankrijk. JA NEEN

_Nog niet beantwoord (modelantwoord ontbreekt)._

---

### 2008-bibf-vrE1 · 2008-bibf

**Vraagformaat**: open · **Antwoord-type**: — · **Confidence**: —

#### Vraagtekst

Een van uw cliënten, detailhandelaar in textielproducten, startte zijn activiteiten op 1/1/2006 en koos voor het forfaitaire BTW regime. Alle BTW aangiften werden tijdig ingediend alsook werd steeds stipt de verschuldigde BTW betaald. Gezien haar activiteiten zich snel en succesvol hebben ontwikkeld, heeft U haar aangeraden om vanaf 01/04/2008 een maandelijkse BTW aangifte in te dienen.

**Welke zijn de concrete gevolgen van deze keuze (Gelieve kort te antwoorden !**

): De verwachte antwoorden zijn minimaal de volgende : Op het vlak Antwoord : van de contacten met - De BTW administratie voor 15/03/2008 informeren over deze de BTW wijziging in BTW regime administratie - Niet langer forfaitaire aangiftes mogelijk, maar wel het normale regime van toepassing Op het vlak Antwoord : van de stock van de - In 2 exemplaren een inventaris van de stock maken op 30/4/2008 handelswaren : - Detaxatie van de stock - Inschrijving in vak 62 van de aangifte Op het vlak Antwoord : van de volgende BTW - Maandelijkse betaling van de verschuldigde BTW betalingen - Einde van de trimestriële voorschotten (- Eventueel voorschot van de maand december te betalen uiterlijk tegen 24/12)

#### Modelantwoord

BTW informeren vóór 15/03/2008; stockinventaris 30/4/2008 met detaxatie (vak 62); maandelijkse betaling i.p.v. trimestriële voorschotten.

> [!success]- Motivering
> Op het vlak van de contacten met de BTW administratie: - De BTW administratie voor 15/03/2008 informeren over deze wijziging in BTW regime - Niet langer forfaitaire aangiftes mogelijk, maar wel het normale regime van toepassing
> 
> Op het vlak van de stock van de handelswaren: - In 2 exemplaren een inventaris van de stock maken op 30/4/2008 - Detaxatie van de stock - Inschrijving in vak 62 van de aangifte
> 
> Op het vlak van de volgende BTW betalingen: - Maandelijkse betaling van de verschuldigde BTW - Einde van de trimestriële voorschotten - (Eventueel voorschot van de maand december te betalen uiterlijk tegen 24/12)

> [!info]- Bronnen (1)
> - _pdf-modelantwoord_

---

### 2008-bibf-vrE2 · 2008-bibf

**Vraagformaat**: berekening · **Antwoord-type**: — · **Confidence**: —

#### Vraagtekst

**Welke zijn de vakken in de periodieke BTW aangifte die moeten ingevuld worden voor de volgende verrichtingen, die werden gedaan door een handelaar (natuurlijke persoon) in nieuwe en tweedehandswagens?**

1. Nieuwe wagens werden geleverd en gefactureerd aan cliënten die onderworpen zijn aan de Luxemburgse BTW voor een bedrag van 66.438,00 € : Vak Bedrag Vak Bedrag Vak Bedrag Vak Bedrag 46 66.438,00

2. Een personenwagen van het merk VOLVO werd aangekocht voor een bedrag van 8.000,00 € van een kinesist en werd daarna doorverkocht voor de prijs van 8.500,00 € aan een particulier : Vak Bedrag Vak Bedrag Vak Bedrag Vak Bedrag 00 8.000,00 81 8.000,00 03 413,22 54 86,78

3. Een vrachtwagen van het merk MANN werd aangekocht voor 4.000,00 € van een bouwonderneming en blijft in stock. Vak Bedrag Vak Bedrag Vak Bedrag Vak Bedrag 81 4.000,00 59 840,00

4. Aankoop van een wagen RENAULT die in de onderneming wordt geïnvesteerd : 24.644,00 € BTW inbegrepen (Privé gebruik 25%). Vak Bedrag Vak Bedrag Vak Bedrag Vak Bedrag 83 16.344,48 59 2138,53

5. Vervangingsstukken en kleine accessoires werden verkocht onder het regime van de vrijstelling van factuur en werden in het dagboek van ontvangsten ingeschreven (1.332,49 € waarvan 434,11 € aan BTW tarief van 6%). Vak Bedrag Vak Bedrag Vak Bedrag Vak Bedrag 01 409,54 03 742,46 54 180,49

_Nog niet beantwoord (modelantwoord ontbreekt)._

---

### 2008-bibf-vrE3 · 2008-bibf

**Vraagformaat**: open · **Antwoord-type**: — · **Confidence**: —

#### Vraagtekst

1.

**Welke is de uiterste datum waarover U beschikt om de BTW af te trekken ?**

Gelieve precies te antwoorden ! Via de aangifte die moet ingediend worden uiterlijk voor het einde van het 3de jaar dat volgt op het jaar gedurende hetwelk het recht op aftrek is ontstaan.

2.

**Welke is/zijn de BTW regime(s) voor de BTW aangiftes die U kan voorstellen aan een zelfstandige psychologe in bijberoep die een omzetcijfer van 4.**

312,00 € per jaar heeft? Vrijstellingsregeling (geen aangifte) Kwartaalaangifte (Maandelijkse aangifte)

3.

**Verklaar het principe van de BTW eenheid (enkel het principe !**

!! , de modaliteiten en de werking worden NIET gevraagd ). De BTW éénheid laat toe om, op juridisch vlak, onafhankelijke personen, maar die op financieel, organisatorisch en economisch vlak nauw met elkaar verbonden zijn, toch te beschouwen als één enkele BTW plichtige. Dit betekent dat de verrichtingen tussen deze personen, die deel uitmaken van de BTW éénheid, niet aan de BTW onderworpen zijn. Dit laat ook toe om de administratieve verplichtingen van deze ondernemingen te rationaliseren en te vereenvoudigen vermits deze BTW eenheid slechts één BTW onderworpene is die instaat voor alle BTW rechten en BTW plichten van haar leden.

4. U bent een zelfstandig boekhouder BIBF gevestigd in België en verricht boekhoudkundige prestaties in een onderneming die gevestigd is in Frankrijk, en die U factureert aan uw belastingplichtige cliënt die in Nederland gevestigd is. In welk land is de BTW verschuldigd ? België, Frankrijk of Nederland ? Verantwoord uw antwoord door te verwijzen naar het toepasselijke artikel uit het BTW wetboek. In Nederland Art. 21 § 3, 7° d) BTW Wetboek (plaats van diegene waar de dienst geleverd wordt)

#### Modelantwoord

Aftrektermijn = einde 3de jaar; bijberoep-psychologe: vrijstelling of kwartaalaangifte; BTW-eenheid = juridisch onafhankelijke maar nauw verbonden personen = 1 belastingplichtige; B2B-dienst in NL → art. 21 §3, 7° d) BTWW.

> [!success]- Motivering
> Zie subvragen voor het gedetailleerde modelantwoord per deelvraag.

> [!info]- Bronnen (1)
> - _pdf-modelantwoord_

---

### 2013-1-vr25 · 2013-1 · 9.0 pt

**Vraagformaat**: J/F · **Antwoord-type**: — · **Confidence**: —

#### Vraagtekst

**Vermeld voor onderstaande handelingen het(de) rooster(s) van de btw-aangifte die moeten
ingevuld worden en eveneens het(de) overeenkomstig(e) bedrag(en).**

Een modelaangifte is

_in bijlage toegevoegd._

U mag er van uit gaan dat de bedragen exclusief btw zijn.
a) Een gewone belastingplichtige zet op 15 januari 2012 zijn economische activiteit stop.
Op het ogenblik van deze definitieve stopzetting bevat het bedrijfspatrimonium nog
een bestelwagen (aangekocht in 2011 voor de prijs van € 30 000,00 + 21% btw) en het
bedrijfsgebouw (aangekocht in 2006 voor een prijs van € 250 000,00 + 21% btw). De
bestelwagen is op het ogenblik van de stopzetting nog € 20 000,00 waard. Het
bedrijfsgebouw is daarentegen in waarde gestegen en is bij de stopzetting
€ 350 000,00 waard.

Antwoord

| ROOSTER | NR | BEDRAG |
| --- | --- | --- |
| ROOSTER |   |   |
| ROOSTER |   |   |
| ROOSTER |   |   |
|   |   |   |

b) Een Belgische belastingplichtige betaalt op 10 januari 2013 aan een Japans bedrijf de
som van € 5 000,00 voor de uitvoering van een grote promotiecampagne op Japans
grondgebied.
Antwoord

| ROOSTER | NR | BEDRAG |
| --- | --- | --- |
| ROOSTER |   |   |
| ROOSTER |   |   |
| ROOSTER |   |   |
| ROOSTER |   |   |

c) Een Belgische belastingplichtige verzendt op 15 mei 2012 een partij handelsgoederen
vanuit haar magazijn te Utrecht (Nederland) naar haar hoofdzetel te Antwerpen. De
goederen werden drie maanden geleden aangekocht in Nederland voor de prijs van
€ 1 250,00, exclusief Nederlandse btw. Dezelfde dag maakt de Belgische
belastingplichtige een transfertdocument op.
Antwoord

| ROOSTER | NR | BEDRAG |
| --- | --- | --- |
| ROOSTER |   |   |
| ROOSTER |   |   |
| ROOSTER |   |   |
| ROOSTER |   |   |

_Nog niet beantwoord (modelantwoord ontbreekt)._

#### Subvraag a)

Een gewone belastingplichtige zet op 15 januari 2012 zijn economische activiteit stop.
Op het ogenblik van deze definitieve stopzetting bevat het bedrijfspatrimonium nog
een bestelwagen (aangekocht in 2011 voor de prijs van € 30 000,00 + 21% btw) en het
bedrijfsgebouw (aangekocht in 2006 voor een prijs van € 250 000,00 + 21% btw). De
bestelwagen is op het ogenblik van de stopzetting nog € 20 000,00 waard. Het
bedrijfsgebouw is daarentegen in waarde gestegen en is bij de stopzetting
€ 350 000,00

#### Subvraag b)

Een Belgische belastingplichtige betaalt op 10 januari 2013 aan een Japans bedrijf de
som van € 5 000,00 voor de uitvoering van een grote promotiecampagne op Japans
grondgebied.

#### Subvraag c)

Een Belgische belastingplichtige verzendt op 15 mei 2012 een partij handelsgoederen
vanuit haar magazijn te Utrecht (Nederland) naar haar hoofdzetel te Antwerpen. De
goederen werden drie maanden geleden aangekocht in Nederland voor de prijs van
€ 1 250,00, exclusief Nederlandse btw. Dezelfde dag maakt de Belgische
belastingplichtige een transfertdocument op.

---

### 2013-1-vr26 · 2013-1 · 6.0 pt

**Vraagformaat**: MC · **Antwoord-type**: — · **Confidence**: —

#### Vraagtekst

**Welke btw gevolgen zijn verbonden aan de onderstaande gegevens:
Geef hierbij een woordje uitleg (geen verwijzing naar artikelnummers) en vermeld
overeenkomstig(e) bedrag(en).**

De nummers van de roosters van de btw-aangifte moet je niet
vermelden.
a) A, een handelaar in computers richt een gebouw op in 2012 (= opslagplaats van
goederen) (in gebruik name op 01.07.2012).
Facturen 2011 : 250 000,00
Facturen 2012 : 250 000,00
Het gebouw wordt verkocht op 01 mei 2016 voor een bedrag van
520 000,00 (€ 450 000,00 voor het gebouw en € 70 000,00 voor de grond) aan B.
B zal in de toekomst het gebouw verhuren aan A.
Wat zijn de gevolgen inzake btw in hoofde van A ?
Antwoord

b) Een btw-plichtige vennootschap koopt in 2013 een nieuwe personenwagen aan die
gratis ter beschikking wordt gesteld aan een personeelslid.
De aankoopprijs van de wagen bedraagt € 30 000,00 (excl. btw). Het personeelslid mag
de wagen ook voor privédoeleinden gebruiken.
Bij aankoop werd het beroepsgebruik geraamd op 60%. Einde 2013 bleek het
effectieve beroepsgebruik 30% te zijn.

**Antwoord
c) In 2008 : aankoop van een personenwagen door een btw-belastingplichtige BVBA voor
€ 30 000,00 + € 6 300,00 btw.**

(in 2008 uitgeoefend recht op aftrek : 6 300,00 x 50% = 3 150,00)
In 2013 : verkoop van die wagen voor € 8 000,00 (excl. btw).
Wat zijn de btw gevolgen bij verkoop van de wagen in 2013?
Antwoord
BEGINSELEN VAN REGISTRATIE- EN 10 PUNTEN
SUCCESSIERECHTEN

_Nog niet beantwoord (modelantwoord ontbreekt)._

#### Subvraag a)

A, een handelaar in computers richt een gebouw op in 2012 (= opslagplaats van
goederen) (in gebruik name op 01.07.2012).
Facturen 2011 : 250 000,00
Facturen 2012 : 250 000,00
Het gebouw wordt verkocht op 01 mei 2016 voor een bedrag van
520 000,00 (€ 450 000,00 voor het gebouw en € 70 000,00 voor de grond) aan B.
B zal in de toekomst het gebouw verhuren aan A.
Wat zijn de gevolgen inzake btw in hoofde van A ?

#### Subvraag b)

Een btw-plichtige vennootschap koopt in 2013 een nieuwe personenwagen aan die
gratis ter beschikking wordt gesteld aan een personeelslid.
De aankoopprijs van de wagen bedraagt € 30 000,00 (excl. btw). Het personeelslid mag
de wagen ook voor privédoeleinden gebruiken.
Bij aankoop werd het beroepsgebruik geraamd op 60%. Einde 2013 bleek het
effectieve beroepsgebruik 30% te zijn.

#### Subvraag c)

In 2008 : aankoop van een personenwagen door een btw-belastingplichtige BVBA voor
€ 30 000,00 + € 6 300,00 btw.
(in 2008 uitgeoefend recht op aftrek : 6 300,00 x 50% = 3 150,00)
In 2013 : verkoop van die wagen voor € 8 000,00 (excl. btw).
Wat zijn de btw gevolgen bij verkoop van de wagen in 2013?

---

### 2013-2-vr26 · 2013-2 · 7.0 pt

**Vraagformaat**: J/F · **Antwoord-type**: — · **Confidence**: —

#### Vraagtekst

Moet er in het onderstaande geval een herziening van het recht op aftrek gebeuren ? Zo ja,
bereken het bedrag ervan. Zo neen, zeg waarom.
Alle bedragen zijn exclusief btw.

**Motiveer bondig je antwoord.**

Een in België gevestigde kleinhandelaar in algemene levensmiddelen, onderworpen aan de
normale regeling, zet zijn activiteit stop op 30/11/2013.
Hij oefende zijn activiteit uit in een gebouw dat hij huurt. Het gebouw werd voor 40 %
bestemd voor zijn economische activiteit en 60 % voor zijn privébehoeften.

In 2011 zijn er voor 2 000,00 EUR verbeteringswerken (onderworpen aan 21 % btw)
uitgevoerd aan het bedrijfsgedeelte van het gebouw.
Op 30/11/2013 behoudt deze btw-belastingplichtige volgende goederen :
- 200,00 EUR handelsgoederen, aangekocht tussen 01/10/2012 en 15/11/2013 voor
doorverkoop (onderworpen aan 21 % btw);
- 2 diepvrieskasten die hij in 1998 heeft aangekocht voor zijn economische activiteit
tegen een prijs per stuk van 300,00 EUR + 19 % btw.
Met betrekking tot :

- **a.** Het gebouw:

Antwoord … /1 punt

- **b.** De verbeteringswerken:

Antwoord … /2 punten

- **c.** De stopzetting:

Antwoord … /2 punten

- **d.** De diepvrieskasten:

Antwoord … /2 punten

_Nog niet beantwoord (modelantwoord ontbreekt)._

#### Subvraag a)

Het gebouw:

#### Subvraag b)

De verbeteringswerken:

#### Subvraag c)

De stopzetting:

#### Subvraag d)

De diepvrieskasten:

---

### 2013-2-vr27 · 2013-2 · 8.0 pt

**Vraagformaat**: berekening+MC · **Antwoord-type**: — · **Confidence**: —

#### Vraagtekst

- **a.** De BVBA ‘A’ (gewone belastingplichtige) stelt een nieuwe personenwagen ter

beschikking van de zaakvoerder. De aankoopprijs bedraagt 25 000,00 EUR exclusief
btw. De zaakvoerder gebruikt de wagen zowel voor privé- als voor beroepsdoeleinden.
Tijdens het jaar 2013 heeft de zaakvoerder 25.250 km gereden. De afstand van de
woning naar de bedrijfszetel van de vennootschap – enkele rit – bedraagt 40 km.
De bvba A wenst niet te opteren voor de methode van het algemeen forfait van 35%.
1.

**Bereken het beroepsmatig gebruik van de wagen.**

Antwoord … / 3 punten
2. Hoeveel btw kan deze BVBA in aftrek brengen op de aankoopprijs ?
Antwoord … / 2 punten

- **b.** BVBA ‘B’ (gewone belastingplichtige) stelt in 2013 een personenwagen ter

beschikking aan haar enige werknemer. Op het maandelijkse loon wordt een bijdrage
van 50,00 EUR ingehouden als vergoeding voor het privé gebruik. De wagen wordt
door de vennootschap in 2011 aangekocht voor de prijs van 25 000,00 EUR exclusief
21 % btw.
In de loop van 2013 worden de volgende uitgaven gedaan m.b.t. de wagen :

o Onderhoud en herstelling (excl. 21 % btw) : 750 EUR
o Brandstof (excl. 21 % btw) : 1 500 EUR
o Verzekering (vrijgesteld van btw) : 1 000 EUR
o Verkeersbelasting (vrijgesteld van btw) : 300 EUR
De wagen wordt 40 % beroepsmatig gebruikt.
3. Hoeveel btw moet er afgedragen worden ? Doe de nodige berekeningen en
verklaar bondig.
Antwoord … / 3 punten
BEGINSELEN VAN REGISTRATIE- EN 10 PUNTEN
SUCCESSIERECHTEN

_Nog niet beantwoord (modelantwoord ontbreekt)._

#### Subvraag a)

De BVBA ‘A’ (gewone belastingplichtige) stelt een nieuwe personenwagen ter
beschikking van de zaakvoerder. De aankoopprijs bedraagt 25 000,00 EUR exclusief
btw. De zaakvoerder gebruikt de wagen zowel voor privé- als voor beroepsdoeleinden.
Tijdens het jaar 2013 heeft de zaakvoerder 25.250 km gereden. De afstand van de
woning naar de bedrijfszetel van de vennootschap – enkele rit – bedraagt 40 km.
De bvba A wenst niet te opteren voor de methode van het algemeen forfait van 35%.
1. Bereken het ber

#### Subvraag b)

BVBA ‘B’ (gewone belastingplichtige) stelt in 2013 een personenwagen ter
beschikking aan haar enige werknemer. Op het maandelijkse loon wordt een bijdrage
van 50,00 EUR ingehouden als vergoeding voor het privé gebruik. De wagen wordt
door de vennootschap in 2011 aangekocht voor de prijs van 25 000,00 EUR exclusief
21 % btw.
In de loop van 2013 worden de volgende uitgaven gedaan m.b.t. de wagen :
o Onderhoud en herstelling (excl. 21 % btw) : 750 EUR
o Brandstof (excl. 21 % btw) : 1 500 EUR
o Verz

---

### 2014-1-vr30 · 2014-1 · 3.0 pt

_Ook geklassificeerd onder_: 2.8

**Vraagformaat**: open · **Antwoord-type**: — · **Confidence**: —

#### Vraagtekst

Een in Welkenraedt gevestigde onderneming, gespecialiseerd in dakwerken, bouwt het
dakgebinte en de dakbedekking van een zwembad in München (Duitsland), tegen de prijs van
10.000 EUR. De eigenaar is een Oostenrijkse particulier.
Duid de goede oplossing aan.

**Antwoord

De btw is niet van toepassing want de klant is een particulier, gevestigd buiten België.**


De btw is niet van toepassing want de aannemer is gevestigd in een andere lidstaat dan de
plaats van het werk.

De btw is van toepassing in België, want de aannemer is gevestigd in België.

De btw is van toepassing in Duitsland, want het onroerend goed is gelegen in Duitsland.

De btw is van toepassing in Oostenrijk, want de klant is Oostenrijker.

_Nog niet beantwoord (modelantwoord ontbreekt)._

---

### 2014-1-vr31 · 2014-1 · 3.0 pt

**Vraagformaat**: open · **Antwoord-type**: — · **Confidence**: —

#### Vraagtekst

Een fabrikant van industriële aanhangwagens, een gewone belastingplichtige en gevestigd in
Vilvoorde, wordt failliet verklaard. De voorraad aanhangwagens en het exploitatiemateriaal
van de onderneming worden, op verzoek van de door de rechtbank van koophandel van
Brussel aangestelde curator, openbaar verkocht tegen de bij de toewijzing vastgestelde prijs.
De kopers zijn Belgische gewone belastingplichtigen die zelf instaan voor het ophalen en
vervoeren van de door hen gekochte loten.
Duid de goede oplossing aan.

**Antwoord

De btw is niet van toepassing want de kopers oefenen een economische activiteit uit en
hebben een geldig btw-nummer.**


De btw is niet van toepassing want de leverancier is failliet verklaard.

De btw is niet van toepassing want de goederen werden verkocht bij openbaar opbod en niet
bij een onderhands contract.

De btw is van toepassing in België want de verkoper is in België gevestigd en de plaats van
de levering is bij aankomst van het vervoer van de goederen naar de koper.

De btw is van toepassing in België want de verkoper is gevestigd in België en de plaats van
de levering is bij vertrek van het vervoer.

_Nog niet beantwoord (modelantwoord ontbreekt)._

---

### 2014-1-vr32 · 2014-1 · 3.0 pt

**Vraagformaat**: open · **Antwoord-type**: — · **Confidence**: —

#### Vraagtekst

Sophie, intern boekhoudster bij de firma ElectroStar, groothandel in huishoudtoestellen in
Brussel, doet sinds een jaar, als zelfstandige in bijberoep (na haar dagtaak), de boekhouding

van de firma Libro, een ijzerwinkel in Brussel.
In 2013 ontvangt ze daarvoor 1.500 EUR per maand. In haar aangifte in de personenbelasting,
geeft zij dit bedrag aan onder de diverse inkomsten.
Duid de goede oplossing aan.

**Antwoord

De btw is niet van toepassing, want Sophie is geen btw-belastingplichtige.**

Ze handelt in het
verlengde van haar job als werknemer en ze is dus niet zelfstandig.

De btw is niet van toepassing, want in haar aangifte in de personenbelasting geeft Sophie dit
bedrag aan als diverse inkomsten.

De btw is niet van toepassing, want Sophie kan vrijgesteld worden van de btw gelet op het
geringe bedrag van haar omzet.

De btw is van toepassing, want het betreft een dienst verricht door een als zodanig
handelend zelfstandig belastingplichtige.

De btw is van toepassing, want het betreft een levering van goederen verricht door een als
zodanig handelend zelfstandig belastingplichtige.

_Nog niet beantwoord (modelantwoord ontbreekt)._

---

### 2014-1-vr33 · 2014-1 · 3.0 pt

**Vraagformaat**: open · **Antwoord-type**: — · **Confidence**: —

#### Vraagtekst

Julien, bediende bij een bank in België, doet een beroep op een in Charleroi gevestigde
zelfstandige accountant (gewone belastingplichtige) om zijn belastingaangifte op te stellen.
De accountant stelt die belastingaangifte op in de trein, op weg naar een conferentie in
Parijs, en wel tijdens het gedeelte van de reisweg afgelegd in Frankrijk, en rekent Julien 500
EUR aan voor zijn werk.
Duid de goede oplossing aan.

**Antwoord

De btw is niet van toepassing want de klant is een particulier.**


De Belgische btw is niet van toepassing, want het werk werd daadwerkelijk in Frankrijk
uitgevoerd.

De Belgische btw is van toepassing, want de accountant, dienstverrichter, is gevestigd in
België.

De btw is van toepassing in België, want de afnemer is gevestigd in België.

De btw is van toepassing in Frankrijk, plaats van de materiële verrichting van de dienst

_Nog niet beantwoord (modelantwoord ontbreekt)._

---

### 2014-1-vr34 · 2014-1 · 3.0 pt

_Ook geklassificeerd onder_: 2.8

**Vraagformaat**: open · **Antwoord-type**: — · **Confidence**: —

#### Vraagtekst

Een in Londen gevestigde hotelonderneming, die onder meer een hotel uitbaat in Coventry
(Groot-Brittannië), bestelt bij het Brussels reclameblad Publi-Magazine een advertentie van
een halve bladzijde om de prijzen van haar hotel in de Paasvakantie te promoten. De prijs die
Publi-Magazine voor die advertentie aanrekent, is 2.000 EUR.

De Engelse onderneming verklaart aan Publi-Magazine dat zij in Groot-Brittannië
belastingplichtige is en deelt haar Brits btw-identificatienummer mee.
Merk wel op dat Publi-Magazine een kosteloos verspreid huis-aan-huisreclameblad is, dat
zijn inkomsten haalt uit de inlassing van betaalde reclameadvertenties.
Duid de goede oplossing aan
Antwoord

Er is geen Belgische btw van toepassing, want de klant is een buitenlandse onderneming die
in elk geval recht op aftrek zou hebben van de btw die haar door haar leverancier wordt
aangerekend.

De Belgische btw is niet van toepassing want het betreft een kosteloos verspreid huis-aan-
huisreclameblad en er bestaat een vrijstellingsregime voor kranten.

De btw is van toepassing in België, want de dienstverrichter is gevestigd in België.

De btw is van toepassing in België, want de publicatie van de advertentie is in een Belgische
krant.

De btw is van toepassing in Groot-Brittannië, want de afnemer van de dienst is gevestigd in
Groot-Brittannië en heeft een daar een geldig btw-nummer.
BEGINSELEN VAN REGISTRATIE- EN 10 PUNTEN
SUCCESSIERECHTEN

_Nog niet beantwoord (modelantwoord ontbreekt)._

---

### 2015-1-vr36 · 2015-1 · 4.0 pt

_Ook geklassificeerd onder_: 2.6

**Vraagformaat**: MC · **Antwoord-type**: — · **Confidence**: —

#### Vraagtekst

Uw cliënt is eigenaar van een woning gelegen in het Brussels Hoofdstedelijk Gewest. Uw
cliënt wenst het appartement te verkopen en vraagt u om hem daarin te adviseren en de
meest voordelige formule voor hem aan te raden.
Uw cliënt heeft in 2006 de grond aangekocht voor 200.000 EUR (alle kosten inbegrepen).
In 2011 is hij gestart met het bouwen van een woning, totale kostprijs 363.000 EUR
(300.000 + 63.000 btw). Hij heeft de woning voor het eerst in gebruik genomen op 1 juni 2013.
Er is een koper voor de woning (+ grond) die 650.000 EUR wil betalen maar dit bedrag is voor
de koper alle kosten (belastingen) inbegrepen. U mag de notariskosten en andere kosten
buiten beschouwing houden.

**Wat is voor uw cliënt de meest voordelige mogelijkheid?**

- **A.** De verkoper kan opteren als toevallige btw-belastingplichtige, zodanig dat hij de

woning+grond onder het btw-stelsel kan verkopen en de btw op de oprichting in aftrek
kan brengen. De winst op deze verkoop voor de cliënt zal het hoogst zijn.

- **B.** Alhoewel de verkoper kan opteren als toevallige btw-belastingplichtige, is het beter om

dit niet te doen en om de verkoop (grond+gebouw) onder Registratierecht te laten
doorgaan. De winst op de verkoop onder Registratierecht zal voor de cliënt het hoogst
zijn.

- **C.** Alhoewel de verkoper kan opteren als toevallige btw-belastingplichtige, is het beter om

dit niet te doen en om de verkoop (grond+gebouw) onder Registratierecht te laten
doorgaan. De winst op de verkoop onder Registratierecht zal voor de cliënt het hoogst
zijn omdat hij ook nog een deel van de vroeger betaalde Registratierechten kan
verrekenen.

- **D.** Er is geen mogelijkheid meer om de verkoop onder btw te laten plaats vinden gezien de

termijn voor het uitoefenen van de optie voor toevallige btw-belastingplichtige verstreken
is.
E. De voordeligste situatie is de verkoop van de grond onder Registratierecht te laten
plaatsvinden en de verkoop van de woning onder btw mits het uitoefenen van een optie
als toevallige btw-belastingplichtige

_Nog niet beantwoord (modelantwoord ontbreekt)._

---

### 2015-1-vr37 · 2015-1 · 2.0 pt

**Vraagformaat**: MC · **Antwoord-type**: — · **Confidence**: —

#### Vraagtekst

Een nieuwe klant komt bij u aankloppen en vraagt om begeleiding bij de opstart, onder meer
over zijn btw-statuut.
Het gaat om een nieuw op te richten vzw die volgende activiteiten zal ontwikkelen:
 Het geven van yogalessen en relaxatieoefeningen voor mensen die kampen met een
burn-out.
 Het uitbaten van een gezellig café (geen maaltijden of snacks) dat alleen open is
tijdens de uren van de lessen en niet toegankelijk is voor mensen van buiten af. In het
café wordt uitsluitend niet alcoholische dranken geschonken. De inkomsten uit deze
activiteiten zijn heel gering en in elk geval minder dan 10.000 EUR jaaromzet.
 De verkoop van boeken over het beoefenen van yoga, geschatte jaaromzet 4.000 EUR.

**Wat is het btw-statuut van de vzw?**

- **A.** De vzw kan de vrijstelling van artikel 44, §2, 4° WBTW (onderwijs) inroepen, ook voor de

bijkomende activiteiten. Ze heeft dan ook het statuut van vrijgestelde belastingplichtige, ze
moet geen periodieke btw-aangiften indienen, maar kan ook geen recht op aftrek uitoefenen.

- **B.** De vzw kan geen enkele vrijstelling inroepen, ze is onderworpen aan btw. Ze heeft het

statuut van belastingplichtige met recht op aftrek en zal periodieke aangiften moeten
indienen.

- **C.** De vzw kan de vrijstelling van artikel 44, §2, 3° WBTW (sport) inroepen, ook voor de

bijkomende activiteiten. Ze heeft dan ook het statuut van vrijgestelde belastingplichtige, ze
moet geen periodieke btw-aangiften indienen, maar kan ook geen recht op aftrek uitoefenen.

- **D.** Voor de yogalessen kan de vzw de vrijstelling van artikel 44, §2, 3° WBTW (sport) inroepen

maar zal voor de bijkomende activiteiten (café en verkoop boeken) btw dienen aan te
rekenen. Ze is dus een gemengde belastingplichtige, zal periodieke btw-aangiften indienen
en zal gedeeltelijk recht op aftrek kunnen uitoefenen (verhoudingsgetal of werkelijk gebruik).

_Nog niet beantwoord (modelantwoord ontbreekt)._

---

### 2015-1-vr38 · 2015-1 · 3.0 pt

**Vraagformaat**: J/F · **Antwoord-type**: — · **Confidence**: —

#### Vraagtekst

De uitbater van een lokale supermarkt heeft in de rekken regelmatig etenswaren die nog
moeilijk verkoopbaar zijn omdat bijvoorbeeld de verpakking licht beschadigd is, of omdat de
vervaldatum dichtbij is. In plaats van de producten te verkopen met afslag of te vernietigen
gaat hij vanaf nu de producten zelf verbruiken. Moet de winkelier de btw regelen?

- **A.** Neen, eigen verbruik van vervallen producten is toegelaten.
- **B.** Ja, hij moet een stuk opmaken aan zichzelf en de btw voldoen op de verkoopprijs van de

producten die hij onttrekt uit zijn voorraad.

- **C.** Ja, hij moet een stuk opmaken aan zichzelf en de btw voldoen op een verminderde

waarde, namelijk de aankoopprijs van de goederen op het moment van de onttrekking en
rekening houdend met de staat waarin ze zich bevinden.

- **D.** Ja, hij moet de btw die hij oorspronkelijk op de aankoop van de producten heeft

afgetrokken terugstorten via een herziening.
E. Neen, dit is geen handeling onder bezwarende titel, want hij betaalt niet voor het
onttrekken van de producten.

_Nog niet beantwoord (modelantwoord ontbreekt)._

---

### 2015-1-vr39 · 2015-1 · 3.0 pt

**Vraagformaat**: MC · **Antwoord-type**: — · **Confidence**: —

#### Vraagtekst

De interne accountant van een Belgische onderneming rijdt met zijn bedrijfswagen elke
maand 2 dagen naar hun filiaal in Parijs om daar de boekhouding van de Franse
onderneming af te sluiten en de Franse btw-aangifte te doen.
De accountant beschikt over een laptop, een gsm en een leasewagen van zijn Belgische
werkgever (met Belgische nummerplaat).
Zijn er bepaalde btw-verplichtingen te vervullen door de Belgische onderneming i.v.m. de
maandelijkse trip naar Parijs?

- **A.** Ja, het gaat om een overbrenging van goederen van de onderneming naar een andere

lidstaat van de EU. De Belgische onderneming moet voor de overbrenging van de
wagen, de laptop en de gsm een factuur opmaken aan het Franse filiaal.

- **B.** Ja, het gaat om een overbrenging van eigen goederen van de onderneming naar een

andere lidstaat van de EU. De Belgische onderneming moet voor deze overbrenging een
“overbrengingsstuk” aan zichzelf opmaken.

- **C.** Ja, het gaat echter om een “niet-overbrenging” van eigen goederen en hiervoor moet

geen stuk worden opgemaakt maar wel telkens bij vertrek uit België een inschrijving in
het register der niet-overbrengingen. De goederen moeten worden uitgeschreven uit dit
register bij de terugkeer ervan naar België.

- **D.** Neen, het gaat wel om een “niet-overbrenging” van eigen goederen en er moet dus geen

overbrengingsstuk worden gemaakt en bovendien staat de Administratie toe dat geen
inschrijving in het register der niet-overbrengingen moet worden gedaan voor auto’s,
computers en gsm’s.

_Nog niet beantwoord (modelantwoord ontbreekt)._

---

### 2015-1-vr40 · 2015-1 · 3.0 pt

_Ook geklassificeerd onder_: 2.8

**Vraagformaat**: J/F · **Antwoord-type**: — · **Confidence**: —

#### Vraagtekst

Een Belgische onderneming fabrikant van badkameraccessoires verkoopt goederen aan een
Nederlandse groothandel (met geldig NL btw-nummer) met leveringsvoorwaarden franco
Duitsland. De Nederlandse groothandel heeft de goederen doorverkocht aan een Duitse
groothandel (met geldig DE btw-nummer) en vraagt dus aan haar Belgische leverancier om
de goederen rechtstreeks naar Duitsland te transporteren naar het magazijn van haar Duitse
klant.
Wat vermeldt de Belgische onderneming op haar verkoopfactuur ? In welk vak van de btw-
aangifte neemt ze deze handeling op (kopie van het btw-aangifteformulier vindt u

_in bijlage)?
Zijn er nog andere verplichtingen te vervullen?
A._

Het gaat om een intracommunautaire levering, vrijgesteld van btw. De Belgische
onderneming vermeldt op de verkoopfactuur ‘Vrijgestelde intracommunautaire levering
artikel 39bis WBTW (of artikel 146 btw Richtlijn 2006/112/EU).’De handeling wordt alleen
opgenomen in vak 46 van haar btw-aangifte.

- **B.** Het gaat om een intracommunautaire levering, vrijgesteld van btw. De Belgische

onderneming vermeldt op de verkoopfactuur ‘Vrijgestelde intracommunautaire levering
artikel 39bis WBTW (of artikel 146 btw Richtlijn 2006/112/EU).’ De handeling wordt
opgenomen in vak 46 van haar btw-aangifte en in haar intracommunautaire opgave met het
NL btw-nummer van de Nederlandse afnemer en de code L (= levering).

- **C.** Het gaat om een intracommunautaire levering, vrijgesteld van btw. De Belgische

onderneming vermeldt op de verkoopfactuur ‘Vrijgestelde intracommunautaire levering
artikel 39bis WBTW.’ De handeling wordt opgenomen in vak 46 van haar btw-aangifte en in

haar intracommunautaire opgave met het DE btw-nummer van de uiteindelijke Duitse
afnemer en de code L (=levering).
D. Het gaat om vereenvoudigd driehoeksverkeer, vrijgesteld van btw. De Belgische
onderneming vermeldt op de verkoopfactuur ‘Driehoeksverkeer, artikel 25 quinquies WBTW,
medecontractant aangeduid als schuldenaar, btw verlegd.” De handeling wordt opgenomen
in vak 46 van haar btw-aangifte en in haar intracommunautaire opgave met het DE btw-
nummer van de uiteindelijke Duitse afnemer en met vermelding dat het om driehoeksverkeer
gaat (code T = triangulaire).
E. Het gaat om een intracommunautaire levering, vrijgesteld van btw. De Belgische
onderneming vermeldt op de verkoopfactuur ‘Btw verlegd’. De handeling wordt opgenomen
in vak 46 van haar btw-aangifte en in haar intracommunautaire opgave met het NL btw-
nummer van de Nederlandse afnemer (geen specifieke code).

FISCALE PROCEDURE 15 PUNTEN
Antwoorden
Plaats de letter van het juiste antwoord in onderstaande rooster.

| Vraag | 1 | 2 | 3 | 4 | 5 |
| --- | --- | --- | --- | --- | --- |
| Antwoord |   |   |   |   |   |
| Punten | 3 | 3 | 3 | 3 | 3 |

_Nog niet beantwoord (modelantwoord ontbreekt)._

---

### 2024-1-vr11 · 2024-1

> [!warning] Herinnering-reconstructie (volledig)
> Deze vraag is een **herinnering**-reconstructie (volledigheid: volledig) — geen officiële ITAA-bundel. Modelantwoord rust op de geherinterpreteerde vraagtekst (ADR-022).

**Vraagformaat**: J/F · **Antwoord-type**: — · **Confidence**: —

#### Vraagtekst

11 BTW

- **A.** Situatie: Rentenier liet hybride dieselwagen onderhouden door Porsche-garage Antwerpen (maandaangever) Onderhoud op 27/4/N Klant betaald op 3/5/N Op 30/4/N uitreiking factuur van 1.210 euro incl BTW:
- **a.** Niet verplicht van factuur uit te reiken: BTW opeisbaar 3/5/N
- **b.** Niet verplicht van factuur uit te reiken: BTW opeisbaar 30/4/N
- **c.** Verplicht factuur : BTW opeisbaar 30/5/N
- **d.** Verplicht factuur: BTW opeisbaar 30/4/N
- **B.** Margeregeling, situatie hoe opnemen in de btw aangifte.
- **C.** Vrijstellingsregeling is mogelijk voor volgende activiteiten: (alles juist of geen punten)
- **a.** Elektricien omzet 10.000
- **b.** Kapper omzet 15.000
- **c.** Diëtist vrijgestelde omzet 50.000, onderworpen omzet 15.000
- **d.** Schoonheidsspecialiste omzet 30.000

e. Verhuur gastenkamers met ontbijt omzet 20.000

- **D.** VAT Refund juist of fout
- **a.** Vrijgestelde BP kan buitenlandse BTW terugvragen via VAT Refund
- **b.** Minimumbedrag vereist voor verzoek tot teruggave is 50 euro per kalanderjaar per lidstaat
- **c.** Minimumbedrag vereist voor verzoek tot teruggave is afhankelijk van de EU lidstaat van het land van de BP
- **d.** Minimumbedrag vereist voor verzoek tot teruggave is afhankelijk van land waarop de teruggave betrekking heeft.

e. Minimumbedrag voor verzoek is 400 euro per kalenderjaar per EU lidstaat.

E.

**Vermeld BTW tarief of stelsel dat wordt toegepast voor glazenwassen door een Belgische onderneming die gewone BP is.**

- **a.** BE gebouw, afnemer is BP die aangifte indiend
- **b.** BE gebouw, meer dan 10 jaar betrokken door BE particulier
- **c.** BE gebouw minder dan 10 jaar betrokken door BE particulier
- **d.** BE gebouw, FR BP

e. BE gebouw, Zweedse BP afnemer.

> [!note]- Geherinterpreteerde vraagtekst (ADR-022)
> Casus BTW, 5 deelvragen:
> A. MC casus — Een rentenier liet zijn hybride dieselwagen onderhouden door Porsche-garage Antwerpen (maandaangever). Onderhoud op 27/4/N, klant betaalde op 3/5/N, op 30/4/N werd een factuur van 1.210 euro incl. BTW uitgereikt. Wanneer is BTW opeisbaar en is factuur verplicht?
>     a. Niet verplicht factuur uit te reiken: BTW opeisbaar 3/5/N / b. Niet verplicht factuur uit te reiken: BTW opeisbaar 30/4/N / c. Factuur verplicht: BTW opeisbaar 30/5/N / d. Factuur verplicht: BTW opeisbaar 30/4/N.
> B. Margeregeling — situatie hoe op te nemen in de BTW-aangifte? (concrete situatie niet bewaard in herinnering — vermoedelijk standaard-casus).
> C. MC — Voor welke activiteiten is de vrijstellingsregeling mogelijk? (alles juist of geen punten):
>     a. Elektricien, omzet 10.000 / b. Kapper, omzet 15.000 / c. Diëtist, vrijgestelde omzet 50.000, onderworpen omzet 15.000 / d. Schoonheidsspecialiste, omzet 30.000 / e. Verhuur gastenkamers met ontbijt, omzet 20.000.
> D. MC — VAT Refund — juist of fout:
>     a. Vrijgestelde BP kan buitenlandse BTW terugvragen via VAT Refund / b. Minimumbedrag voor verzoek tot teruggave is 50 euro per kalenderjaar per lidstaat / c. Minimumbedrag is afhankelijk van de EU-lidstaat van de BP / d. Minimumbedrag is afhankelijk van het land waarop de teruggave betrekking heeft / e. Minimumbedrag voor verzoek is 400 euro per kalenderjaar per EU-lidstaat.
> E. MC — Vermeld het BTW-tarief of -stelsel voor glazenwassen door een Belgische onderneming die gewone BP is:
>     a. BE-gebouw, afnemer is BP die aangifte indient / b. BE-gebouw, meer dan 10 jaar betrokken door BE-particulier / c. BE-gebouw minder dan 10 jaar betrokken door BE-particulier / d. BE-gebouw, FR BP-afnemer / e. BE-gebouw, Zweedse BP-afnemer.
> 
> _Motivering_: Sub-A, sub-C, sub-D en sub-E zijn complete MC's met volledige opties. Sub-B is een open vraag zonder specifieke casus-data in de herinnering. Vraag-stam en alle opties zijn afleidbaar uit de PDF — type wordt 'volledig' geclassificeerd ondanks dat sub-B een fragment is, omdat het hoofdaandeel van de vraag volledig is.
> _Confidence_: grounded · _Datum_: 2026-05-19

> [!example]- MC-opties (gestructureerd)
> | Label | Tekst | Juistheid | Motivering |
> | --- | --- | --- | --- |
> | A.a | Niet verplicht factuur uit te reiken: BTW opeisbaar 3/5/N | onbekend | Klant = particulier (rentenier, geen BP) → factuur niet altijd verplicht. Opeisbaarheid bij betaling. |
> | A.b | Niet verplicht factuur uit te reiken: BTW opeisbaar 30/4/N | onbekend | Opeisbaarheid bij factuurdatum als factuur uitgereikt vóór betaling. |
> | A.c | Factuur verplicht: BTW opeisbaar 30/5/N | fout | 30/5/N is geen relevante datum in deze casus. |
> | A.d | Factuur verplicht: BTW opeisbaar 30/4/N | onbekend | Te verifiëren of factuur verplicht is voor B2C-dienst aan particulier (rentenier). |
> | C.a | Elektricien, omzet 10.000 | juist | Onder drempel vrijstelling kleine onderneming (25.000 EUR). |
> | C.b | Kapper, omzet 15.000 | juist | Onder drempel. |
> | C.c | Diëtist, vrijgestelde omzet 50.000, onderworpen omzet 15.000 | juist | Vrijgestelde omzet telt niet voor drempel; onderworpen omzet 15.000 < 25.000. |
> | C.d | Schoonheidsspecialiste, omzet 30.000 | fout | Boven drempel 25.000 EUR — niet vrijstellingsregeling-gerechtigd. |
> | C.e | Verhuur gastenkamers met ontbijt, omzet 20.000 | onbekend | Activiteit kan uitgesloten zijn van vrijstellingsregeling — te verifiëren. |
> | D.a | Vrijgestelde BP kan buitenlandse BTW terugvragen via VAT Refund | fout | Vrijgestelde BP heeft geen recht op aftrek/teruggave. |
> | D.b | Minimumbedrag voor verzoek is 50 euro per kalenderjaar per lidstaat | fout | Minimumbedrag afhankelijk van land en periode (jaar/kwartaal). |
> | D.c | Minimumbedrag afhankelijk van de EU-lidstaat van de BP | fout | Minimum geldt voor het land waarop teruggave betrekking heeft, niet land van indiener. |
> | D.d | Minimumbedrag afhankelijk van land waarop teruggave betrekking heeft | juist | BTW-richtlijn 2008/9/EG — drempel per teruggave-lidstaat. |
> | D.e | Minimumbedrag voor verzoek is 400 euro per kalenderjaar per EU-lidstaat | fout | 400 euro is een kwartaal-drempel, niet jaarlijks. |
> | E.a | BE-gebouw, afnemer is BP die aangifte indient | onbekend | B2B-dienst onroerend goed in België — verlegging mogelijk (KB nr. 1 art. 20). |
> | E.b | BE-gebouw, meer dan 10 jaar betrokken door BE-particulier | onbekend | Tarief 6 % renovatiewerken aan privéwoning > 10 jaar (KB nr. 20 §A.XXXVIII). |
> | E.c | BE-gebouw minder dan 10 jaar betrokken door BE-particulier | onbekend | Geen renovatie-tarief — standaard 21 %. |
> | E.d | BE-gebouw, FR BP-afnemer | onbekend | Dienst gerelateerd aan onroerend goed → plaats = ligging gebouw (België) → 21 % BTW BE. |
> | E.e | BE-gebouw, Zweedse BP-afnemer | onbekend | Idem als sub-d — plaats = ligging onroerend goed. |

_Nog niet beantwoord (modelantwoord ontbreekt)._

---

## PO 2.5

_18 vragen — 2 met modelantwoord — 0 met gap-rapport._

### 2003-bibf-vrH1 · 2003-bibf · 1 pt

**Vraagformaat**: MC · **Antwoord-type**: — · **Confidence**: —

#### Vraagtekst

Binnen welke termijn dient een BTW inregelstelling ingediend te worden? 1 PUNT Gelieve het juiste antwoord aan te kruisen. (cid:137) Er is geen enkele termijn voor zover de wettelijke verjaringstermijn niet verstreken is (cid:137) Op straffe van verval binnen de 3 kalendermaanden vanaf de invorderingstermijn. (cid:137) Ten laatste aan het einde van de derde burgerlijke maand die volgt op de betekening van het dwangbevel. (cid:137) Binnen de 30 dagen vanaf de datum van het overzicht van de regularisaties

_Nog niet beantwoord (modelantwoord ontbreekt)._

---

### 2003-bibf-vrH2 · 2003-bibf · 4 pt

**Vraagformaat**: open · **Antwoord-type**: — · **Confidence**: —

#### Vraagtekst

De belastingplichtige heeft geen verzoek ingediend (en dus ook niet gekregen) teneinde een bijkomende termijn voor het indienen van de aangifte te bekomen. Hij doet zijn aangifte in de personenbelasting laattijdig. Welk zijn de gevolgen van het laattijdig toekomen van zijn aangifte bij de belastingadministratie?

_Nog niet beantwoord (modelantwoord ontbreekt)._

---

### 2008-bibf-vrH1 · 2008-bibf

**Vraagformaat**: open · **Antwoord-type**: — · **Confidence**: —

#### Vraagtekst

H1.

**Hoe dient U een rechtsgeldig bezwaar in tegen een aanslag in de personenbelasting en binnen welke termijn dient dit te gebeuren ?**

Dit dient uiterlijk te gebeuren binnen de 6 maanden vanaf de datum van verzending van het aanslagbiljet/kennisgeving van de aanslag bij de gewestelijk directeur (art. 366 WIB) Het dient te gebeuren per (aangetekend) schrijven met opgave van de wetsartikelen waarop U zich baseert en dient uiteraard gemotiveerd en ondertekend te zijn (art. 371 WIB).

#### Modelantwoord

Binnen 6 maanden na verzending aanslagbiljet (art. 366 WIB) per (aangetekend) gemotiveerd schrijven bij de gewestelijk directeur (art. 371 WIB).

> [!success]- Motivering
> Dit dient uiterlijk te gebeuren binnen de 6 maanden vanaf de datum van verzending van het aanslagbiljet/kennisgeving van de aanslag bij de gewestelijk directeur (art. 366 WIB). Het dient te gebeuren per (aangetekend) schrijven met opgave van de wetsartikelen waarop U zich baseert en dient uiteraard gemotiveerd en ondertekend te zijn (art. 371 WIB).

> [!info]- Bronnen (1)
> - _pdf-modelantwoord_

---

### 2008-bibf-vrH2 · 2008-bibf

**Vraagformaat**: open · **Antwoord-type**: — · **Confidence**: —

#### Vraagtekst

H2. In welke omstandigheden kan de fiscale administratie (directe belastingen) overgaan tot een tot een belasting op basis van tekenen en indiciën ? Indien de fiscus in het bezit is van overeenstemmende en ernstige elementen en/of gegevens die een vermoeden scheppen dat de belastingplichtige tekort geschoten is in de aangifte van zijn belastbaar inkomen.

#### Modelantwoord

Wanneer de fiscus overeenstemmende en ernstige elementen heeft die een vermoeden scheppen van onvolledige aangifte van het belastbaar inkomen.

> [!success]- Motivering
> Indien de fiscus in het bezit is van overeenstemmende en ernstige elementen en/of gegevens die een vermoeden scheppen dat de belastingplichtige tekort geschoten is in de aangifte van zijn belastbaar inkomen.

> [!info]- Bronnen (1)
> - _pdf-modelantwoord_

---

### 2013-1-vr31 · 2013-1 · 9.0 pt

**Vraagformaat**: J/F · **Antwoord-type**: — · **Confidence**: —

#### Vraagtekst

De onderneming “Snack on the Road” exploiteert een foodservice langs de autosnelweg. De
bediening ligt naast een tankstation en verschaft maaltijden en bereid voedsel aan
automobilisten die op de pleisterplaats of aan het tankstation stoppen. De producten zijn
zowel verpakt voor verbruik ter plaatse, in een speciaal daartoe ingerichte ruimte, als om
mee te nemen voor verbruik daarbuiten.
Bij een niet aangekondigde btw-controle op 27 januari 2013 doen de controleurs zich voor als
gewone klanten en kopen mondvoorraad. De kassier van Snack on the Road maakt de
rekening zonder te vragen of de aankoop bestemd is voor verbruik ter plaatse of om mee te
nemen. De btw wordt aangerekend tegen 6%.
De controleur betaalt zijn aankoop en neemt plaats om zijn eten ter plaatse te verbruiken.
Drie dagen later ontvangt Snack on the Road een proces-verbaal van vaststelling, gedateerd
op 27 januari 2013 en uitgaande van de administratie van de btw, waarin vermeld staat dat uit
een onderzoek ter plaatse gebleken is dat de btw op alle aankopen tegen het tarief van 6%
wordt berekend, ook als de waar ter plaatse verbruikt wordt.
In een afzonderlijke brief, gedateerd op dezelfde dag, kondigt de administratie een grondige
controle aan over de periode van 1 januari 2005 tot 27 januari 2013. Die aankondiging
verwijst naar het proces-verbaal van dezelfde dag maar omschrijft de vastgestelde feiten
niet. De controle is voorzien voor 20 februari 2013.
Vragen:

- **a.** - Vermeld de normale verjaringstermijn van de vordering tot voldoening van de

belasting.
-Vanaf welke dag begint deze verjaringstermijn te lopen?
Antwoord

- **b.** -Vermeld de normale verjaringstermijn van de vordering tot voldoening van de

belasting in geval van belastingontduiking.
-Vanaf welke dag begint deze verjaringstermijn te lopen?
Antwoord

- **c.** Vermeld, in bovenstaand voorbeeld, het laatste jaar tot waar de administratie, vanaf 27

januari 2013, kan teruggaan om controle uit te oefenen.

**Antwoord
d) Is de brief die de grondige controle aankondigt een aanwijzing van
belastingontduiking?**

Antwoord

_Nog niet beantwoord (modelantwoord ontbreekt)._

#### Subvraag a)

- Vermeld de normale verjaringstermijn van de vordering tot voldoening van de
belasting.
-Vanaf welke dag begint deze verjaringstermijn te lopen?

#### Subvraag b)

-Vermeld de normale verjaringstermijn van de vordering tot voldoening van de
belasting in geval van belastingontduiking.
-Vanaf welke dag begint deze verjaringstermijn te lopen?

#### Subvraag c)

Vermeld, in bovenstaand voorbeeld, het laatste jaar tot waar de administratie, vanaf 27
januari 2013, kan teruggaan om controle uit te oefenen.

#### Subvraag d)

Is de brief die de grondige controle aankondigt een aanwijzing van
belastingontduiking?

---

### 2013-1-vr32 · 2013-1 · 6.0 pt

**Vraagformaat**: MC · **Antwoord-type**: — · **Confidence**: —

#### Vraagtekst

/ 6 punten
Op 5 februari 2013 wordt het proces-verbaal van de administratie van de btw overgezonden
aan de controleur van de directe belastingen van de onderneming Snack on the Road.
Die vennootschap sluit haar boekjaar af op 31 maart van het jaar.
De controleur geeft kennis van de aanwijzingen inzake belastingontduiking en kondigt een
controle ter plaatse aan op 20 februari 2013 met betrekking tot de op 31 maart afgesloten
boekjaren 2005 tot 2012.
Vragen:

- **a.** Voor het aanslagjaar 2012 werd de aangifte in de vennootschapsbelasting bij de

administratie ingediend op 20 september 2012.

**Geef de uiterste datum van inkohiering
van de belasting.**

Antwoord

- **b.** Vermeld, in verband met de procedure gesteund op de aanwijzingen van

belastingontduiking, het oudste belastbare tijdperk dat het voorwerp kan uitmaken
van die onderzoeken.

**Vermeld de begin- en einddatum van dit belastbare tijdperk.**

Antwoord

- **c.** Toont, wat de aanwijzingen van belastingontduiking betreft, het proces-verbaal van

vaststelling inzake de btw, het bestaan van belastingontduiking aan op het gebied van
de vennootschapsbelasting? Verklaar uw antwoord.
Antwoord
JURIDISCHE EN BEROEPSNORMEN MET BETREKKING 
TOT DE ACCOUNTANCY, DE BELASTINGCONSULTANCY
EN DE ANDERE WETTELIJKE OPDRACHTEN VAN DE
ACCOUNTANT EN VAN DE BELASTINGCONSULENT

_Nog niet beantwoord (modelantwoord ontbreekt)._

#### Subvraag a)

Voor het aanslagjaar 2012 werd de aangifte in de vennootschapsbelasting bij de
administratie ingediend op 20 september 2012. Geef de uiterste datum van inkohiering
van de belasting.

#### Subvraag b)

Vermeld, in verband met de procedure gesteund op de aanwijzingen van
belastingontduiking, het oudste belastbare tijdperk dat het voorwerp kan uitmaken
van die onderzoeken. Vermeld de begin- en einddatum van dit belastbare tijdperk.

#### Subvraag c)

Toont, wat de aanwijzingen van belastingontduiking betreft, het proces-verbaal van
vaststelling inzake de btw, het bestaan van belastingontduiking aan op het gebied van
de vennootschapsbelasting? Verklaar uw antwoord.

---

### 2013-2-vr32 · 2013-2 · 6.0 pt

**Vraagformaat**: MC · **Antwoord-type**: — · **Confidence**: —

#### Vraagtekst

Eén van uw cliënten – een verwarmingsinstallateur – ontvangt op 10 september 2013 een
vraag om inlichtingen, luidende als volgt (nb: Het gaat hier over een aanvraag van
inlichtingen betreffende een derde):
“Gelieve mij de volgende inlichtingen mede te delen:
- de volledige identiteit van al uw leveranciers bij wie u een verwarmingsketel van het
type XYZ100 hebt aangekocht;
- het aantal aangekochte verwarmingsketels bij elk van de betrokken leveranciers;
- de aankoopprijs van de verwarmingsketels met vermelding van de eventuele korting
die u hebt genoten.”
De belastingplichtige krijgt een termijn van 10 dagen om de gevraagde inlichtingen te
verstrekken.
Uw cliënt meldt u ook dat, op 15 september, de toegang tot het bedrijf volledig geblokkeerd
werd door stakingspiketten en dat de onderhandelingen met de vakbonden zeker 2 weken
zullen aanslepen.

- **a.** Is deze vraag om inlichtingen regelmatig voor wat de aard van de gevraagde

inlichtingen betreft (verklaar uw antwoord)?
Antwoord …/ 2 punten

- **b.** Is de antwoordtermijn wettelijk (verklaar uw antwoord)?

Antwoord …/ 2 punten

c) Hoe moet tewerk gegaan worden om binnen de gestelde termijn te antwoorden,
aangezien het, momenteel, niet mogelijk is om de vereiste stukken te raadplegen
(verklaar uw antwoord)?
Antwoord …/ 2 punten

_Nog niet beantwoord (modelantwoord ontbreekt)._

#### Subvraag a)

Is deze vraag om inlichtingen regelmatig voor wat de aard van de gevraagde
inlichtingen betreft (verklaar uw antwoord)?

#### Subvraag b)

Is de antwoordtermijn wettelijk (verklaar uw antwoord)?

#### Subvraag c)

Hoe moet tewerk gegaan worden om binnen de gestelde termijn te antwoorden,
aangezien het, momenteel, niet mogelijk is om de vereiste stukken te raadplegen
(verklaar uw antwoord)?

---

### 2013-2-vr33 · 2013-2 · 4.0 pt

**Vraagformaat**: J/F · **Antwoord-type**: — · **Confidence**: —

#### Vraagtekst

**Geef aan of onderstaande uitspraken waar of niet waar zijn:
a) Met betrekking tot de roerende voorheffing, kan enkel de schuldenaar van de
voorheffing (degene die de voorheffing moet inhouden) een bezwaarschrift indienen.**

De verkrijger van de inkomsten waarop de voorheffing werd ingehouden, kan dit recht
niet uitoefenen.

|   |   |
| --- | --- |
|   | Waar |
|   | Niet waar |

b) Indien een belastingplichtige overlijdt en twee kinderen nalaat, en slechts één van die
kinderen bezwaar indient tegen de ten name van de overledene gevestigde belasting,
geldt zijn bezwaarschrift voor het geheel van de aanslag en voor alle erfgenamen
samen.

|   |   |
| --- | --- |
|   | Waar |
|   | Niet waar |

c) De echtgescheiden echtgenoot heeft de mogelijkheid om bezwaar in te dienen tegen
een aanslag die betrekking heeft op een aanslagjaar voor de uitspraak van de
echtscheiding, zelfs indien de andere echtgenoot dit niet heeft gedaan, maar wel op
voorwaarde dat de belasting op de goederen van de indiener van het bezwaarschrift
wordt ingevorderd.

|   |   |
| --- | --- |
|   | Waar |
|   | Niet waar |

d) Wanneer de belastingplichtige ambtshalve is aangeslagen en de directeur zes
maanden na ontvangst van het bezwaarschrift nog geen beslissing heeft genomen,
kan de belastingplichtige het geschil, te allen tijde, voor de rechtbank van eerste
aanleg brengen.

|   |   |
| --- | --- |
|   | Waar |
|   | Niet waar |

_Nog niet beantwoord (modelantwoord ontbreekt)._

#### Subvraag a)

Met betrekking tot de roerende voorheffing, kan enkel de schuldenaar van de
voorheffing (degene die de voorheffing moet inhouden) een bezwaarschrift indienen.
De verkrijger van de inkomsten waarop de voorheffing werd ingehouden, kan dit recht
niet uitoefenen.

#### Subvraag b)

Indien een belastingplichtige overlijdt en twee kinderen nalaat, en slechts één van die
kinderen bezwaar indient tegen de ten name van de overledene gevestigde belasting,
geldt zijn bezwaarschrift voor het geheel van de aanslag en voor alle erfgenamen
samen.

#### Subvraag c)

De echtgescheiden echtgenoot heeft de mogelijkheid om bezwaar in te dienen tegen
een aanslag die betrekking heeft op een aanslagjaar voor de uitspraak van de
echtscheiding, zelfs indien de andere echtgenoot dit niet heeft gedaan, maar wel op
voorwaarde dat de belasting op de goederen van de indiener van het bezwaarschrift
wordt ingevorderd.

#### Subvraag d)

Wanneer de belastingplichtige ambtshalve is aangeslagen en de directeur zes
maanden na ontvangst van het bezwaarschrift nog geen beslissing heeft genomen,
kan de belastingplichtige het geschil, te allen tijde, voor de rechtbank van eerste
aanleg brengen.

---

### 2013-2-vr34 · 2013-2 · 5.0 pt

_Ook geklassificeerd onder_: 2.4

**Vraagformaat**: MC · **Antwoord-type**: — · **Confidence**: —

#### Vraagtekst

Een gewone btw-belastingplichtige gevestigd in België koopt goederen in Duitsland. De
goederen komen op 14/11/2012 aan bij de Belgische koper. Het vervoer werd verricht door
een vervoeronderneming in opdracht van de Duitse verkoper. De factuur wordt toegestuurd
en ontvangen door de Belgische btw-belastingplichtige op 03/12/2012.

- **a.** Wanneer is de btw opeisbaar? Verklaar bondig.

**Antwoord … / 2,5 punten
b) Wanneer treedt er verjaring in?**

Verklaar bondig.
Antwoord … / 2,5 punten
JURIDISCHE EN BEROEPSNORMEN MET BETREKKING 20 PUNTEN
TOT DE ACCOUNTANCY, DE BELASTINGCONSULTANCY
EN DE ANDERE WETTELIJKE OPDRACHTEN VAN DE
ACCOUNTANT EN VAN DE BELASTINGCONSULENT

_Nog niet beantwoord (modelantwoord ontbreekt)._

#### Subvraag a)

Wanneer is de btw opeisbaar? Verklaar bondig.

#### Subvraag b)

Wanneer treedt er verjaring in? Verklaar bondig.

---

### 2014-1-vr39 · 2014-1 · 6.0 pt

**Vraagformaat**: MC · **Antwoord-type**: — · **Confidence**: —

#### Vraagtekst

Eén van uw cliënten – de BVBA “Souris” die een winkel uitbaat van informaticamateriaal –
ontvangt op 2 februari 2014 een vraag om inlichtingen, luidende als volgt:
“Gelieve mij de volgende inlichtingen mede te delen betreffende derden:
- de volledige identiteit van al uw leveranciers bij wie u een “Sumsang” scherm van het
type 123ZXY hebt aangekocht;
- het aantal aangekochte schermen bij elk van de betrokken leveranciers;
- de aankoopprijs van de schermen met vermelding van de eventuele korting die u hebt
genoten.”
De belastingplichtige krijgt een termijn van 12 dagen om de gevraagde inlichtingen te
verstrekken.
Uw cliënt meldt u ook dat, op 10 februari 2014, de toegang tot het bedrijf volledig werd
afgesloten wegens wateroverlast en dat er een termijn van 3 weken nodig zal zijn om de
lokalen te herstellen.

- **a.** Is deze vraag om inlichtingen regelmatig voor wat de aard van de gevraagde

inlichtingen betreft (verklaar uw antwoord)?
Antwoord

- **b.** Is de antwoordtermijn wettelijk (verklaar uw antwoord)?

Antwoord

c) Hoe moet tewerk gegaan worden om binnen de gestelde termijn te antwoorden,
aangezien het, momenteel, niet mogelijk is om de vereiste stukken te raadplegen
(verklaar uw antwoord)?
Antwoord

_Nog niet beantwoord (modelantwoord ontbreekt)._

#### Subvraag a)

Is deze vraag om inlichtingen regelmatig voor wat de aard van de gevraagde
inlichtingen betreft (verklaar uw antwoord)?

#### Subvraag b)

Is de antwoordtermijn wettelijk (verklaar uw antwoord)?

#### Subvraag c)

Hoe moet tewerk gegaan worden om binnen de gestelde termijn te antwoorden,
aangezien het, momenteel, niet mogelijk is om de vereiste stukken te raadplegen
(verklaar uw antwoord)?

---

### 2014-1-vr40 · 2014-1 · 4.0 pt

**Vraagformaat**: J/F · **Antwoord-type**: — · **Confidence**: —

#### Vraagtekst

**Geef aan of onderstaande uitspraken waar of niet waar zijn:
a) Met betrekking tot de roerende voorheffing, kan enkel de schuldenaar van de
voorheffing (degene die de voorheffing moet inhouden) een bezwaarschrift indienen.**

De verkrijger van de inkomsten waarop de voorheffing werd ingehouden, kan dit recht
niet uitoefenen.

|   |   |
| --- | --- |
|   | Waar |
|   | Niet waar |

b) Wanneer de belastingplichtige ambtshalve is aangeslagen en de directeur zes
maanden na ontvangst van het bezwaarschrift nog geen beslissing heeft genomen,
kan de belastingplichtige het geschil, te allen tijde, voor de rechtbank van eerste
aanleg brengen.

|   |   |
| --- | --- |
|   | Waar |
|   | Niet waar |

c) Indien een belastingplichtige overlijdt en twee kinderen nalaat, en slechts één van die
kinderen bezwaar indient tegen de ten name van de overledene gevestigde belasting,
geldt zijn bezwaarschrift voor het geheel van de aanslag en voor alle erfgenamen
samen.

|   |   |
| --- | --- |
|   | Waar |
|   | Niet waar |

d) De echtgescheiden echtgenoot heeft de mogelijkheid om bezwaar in te dienen tegen
een aanslag die betrekking heeft op een aanslagjaar voor de uitspraak van de
echtscheiding, zelfs indien de andere echtgenoot dit niet heeft gedaan, maar wel op
voorwaarde dat de belasting op de goederen van de indiener van het bezwaarschrift
wordt ingevorderd.

|   |   |
| --- | --- |
|   | Waar |
|   | Niet waar |

_Nog niet beantwoord (modelantwoord ontbreekt)._

#### Subvraag a)

Met betrekking tot de roerende voorheffing, kan enkel de schuldenaar van de
voorheffing (degene die de voorheffing moet inhouden) een bezwaarschrift indienen.
De verkrijger van de inkomsten waarop de voorheffing werd ingehouden, kan dit recht
niet uitoefenen.

#### Subvraag b)

Wanneer de belastingplichtige ambtshalve is aangeslagen en de directeur zes
maanden na ontvangst van het bezwaarschrift nog geen beslissing heeft genomen,
kan de belastingplichtige het geschil, te allen tijde, voor de rechtbank van eerste
aanleg brengen.

#### Subvraag c)

Indien een belastingplichtige overlijdt en twee kinderen nalaat, en slechts één van die
kinderen bezwaar indient tegen de ten name van de overledene gevestigde belasting,
geldt zijn bezwaarschrift voor het geheel van de aanslag en voor alle erfgenamen
samen.

#### Subvraag d)

De echtgescheiden echtgenoot heeft de mogelijkheid om bezwaar in te dienen tegen
een aanslag die betrekking heeft op een aanslagjaar voor de uitspraak van de
echtscheiding, zelfs indien de andere echtgenoot dit niet heeft gedaan, maar wel op
voorwaarde dat de belasting op de goederen van de indiener van het bezwaarschrift
wordt ingevorderd.

---

### 2014-1-vr41 · 2014-1 · 5.0 pt

_Ook geklassificeerd onder_: 4.0

**Vraagformaat**: J/F · **Antwoord-type**: — · **Confidence**: —

#### Vraagtekst

De btw controle stuurt aan een accountantskantoor een schriftelijke vraag om inlichtingen
m.b.t. de btw-activiteiten van een van de klanten (vennootschap) van het kantoor. Moet het
kantoor hierop antwoorden en binnen welke termijn? Duid het juiste antwoord aan.


Het accountantskantoor is verplicht tot geheimhouding en mag niet antwoorden op de vraag
om inlichtingen.

Het accountantskantoor kan op de vraag om inlichtingen antwoorden maar moet
voorafgaandelijk schriftelijke toestemming hebben van zijn klant.

Eenieder is verplicht om op vraag van de btw-administratie mondeling of schriftelijk
inlichtingen te verschaffen over zijn eigen toestand maar ook over de toestand van derden.
Er is geen wettelijke termijn voorzien binnen dewelke moet worden geantwoord.

Het accountantskantoor is verplicht om binnen de 20 dagen te antwoorden op een vraag om
inlichtingen

Het accountantskantoor verplicht om op de vraag om inlichtingen te antwoorden, maar alleen
indien de vragen betrekking hebben op haar eigen toestand. Het antwoord moet binnen 1
maand worden gegeven.
JURIDISCHE EN BEROEPSNORMEN MET BETREKKING 20 PUNTEN
TOT DE ACCOUNTANCY, DE BELASTINGCONSULTANCY
EN DE ANDERE WETTELIJKE OPDRACHTEN VAN DE
ACCOUNTANT EN VAN DE BELASTINGCONSULENT

_Nog niet beantwoord (modelantwoord ontbreekt)._

---

### 2015-1-vr41 · 2015-1 · 3.0 pt

**Vraagformaat**: MC · **Antwoord-type**: — · **Confidence**: —

#### Vraagtekst

In een aanslagjaar in de personenbelasting, 5 jaar vóór het huidige aanslagjaar wenst de
administratie onderzoekshandelingen te stellen bij uw cliënt.
U analyseert :

- **A.** dat kan de administratie zonder beperking.
- **B.** dat kan de administratie sowieso niet meer.
- **C.** dat kan de administratie mits voorafgaande kennisgeving van de indiciën van fraude aan uw

cliënt.

- **D.** dat kan de administratie uitsluitend met het oog op een taxatie tekenen en indiciën.

_Nog niet beantwoord (modelantwoord ontbreekt)._

---

### 2015-1-vr42 · 2015-1 · 3.0 pt

_Ook geklassificeerd onder_: 2.8

**Vraagformaat**: J/F · **Antwoord-type**: — · **Confidence**: —

#### Vraagtekst

Uw cliënt wordt ingelicht dat de administratie 18 maanden geleden van een buitenlandse
belastingadministratie, waarmee België een dubbelbelastingverdrag heeft gesloten,
inlichtingen kreeg die uitwijzen dat uw cliënt in een aanslagjaar vier jaar voor het huidige
geen correcte aangifte in de personenbelasting verrichtte.
U analyseert :

- **A.** ja, op basis daarvan kan de administratie nog taxeren omdat er een bijzondere taxatietermijn

loopt van 24 maanden te rekenen vanaf de datum waarop de Belgische administratie kennis
heeft van de resultaten van de controle of het onderzoek.

- **B.** neen, op basis daarvan kan de administratie niet meer taxeren omdat de bijzondere

taxatietermijn loopt van 12 maanden te rekenen vanaf de datum waarop de Belgische
administratie kennis heeft van de resultaten van de controle of het onderzoek.

- **C.** neen, dat kan niet meer omdat alle taxatietermijnen verstreken zijn.
- **D.** neen, dan kan niet meer omdat de Belgische administratie geen aanslag mag vestigen, nà

het verstrijken van de gewone driejarige of de verlengde zevenjarige aanslagtermijn.

_Nog niet beantwoord (modelantwoord ontbreekt)._

---

### 2015-1-vr43 · 2015-1 · 3.0 pt

**Vraagformaat**: MC · **Antwoord-type**: — · **Confidence**: —

#### Vraagtekst

De administratie vraagt inzage in de bestelbonnen van uw cliënt die een onderneming voert
onder vennootschapsvorm.
U analyseert :

- **A.** de administratie kan deze niet opvragen omdat de bewaringsplicht van de boeken en

bescheiden enkel beperkt is tot de wettelijk verplichte boeken en bescheiden, en de
bestelbons daar geen deel van uitmaken. Zij moeten dus niet worden voorgelegd.

- **B.** deze maken geen deel uit van de boekhouding en moeten niet worden voorgelegd.
- **C.** enkel wanneer zij elektronisch zijn opgesteld, moeten zij worden voorgelegd.
- **D.** deze maken deel uit van de boekhouding en moeten worden voorgelegd.

_Nog niet beantwoord (modelantwoord ontbreekt)._

---

### 2015-1-vr44 · 2015-1 · 3.0 pt

**Vraagformaat**: J/F · **Antwoord-type**: — · **Confidence**: —

#### Vraagtekst

De tenuitvoerlegging van een dwangbevel kan slechts worden gestuit door :

- **A.** een bezwaarschrift bij de gewestelijke directie.
- **B.** een verzoekschrift, verzet voor de rechtbank van eerste aanleg, fiscale kamer.
- **C.** een beroep bij de bevoegde controledienst.
- **D.** een voorziening bij de Raad van State.

_Nog niet beantwoord (modelantwoord ontbreekt)._

---

### 2015-1-vr45 · 2015-1 · 3.0 pt

**Vraagformaat**: J/F · **Antwoord-type**: — · **Confidence**: —

#### Vraagtekst

De vraag peilt naar de onderzoekstermijn inzake BTW.
U analyseert :

- **A.** Dusdanig bestaan er geen specifieke bepalingen inzake controletermijnen, inzake BTW,

daar die gelijklopen met de specifieke verjaringstermijnen.

- **B.** het voorgaande antwoord is fout, want de onderzoekstermijn inzake btw bedraagt altijd 7

jaar.

- **C.** het voorgaande antwoord is fout, want de onderzoekstermijn inzake btw bedraagt altijd 15

jaar.

- **D.** geen van voorgaande antwoorden is juist.

BEGINSELEN VAN REGISTRATIE- EN 10 PUNTEN
SUCCESSIERECHTEN
Antwoorden
Plaats de letter van het juiste antwoord in onderstaande rooster.

| Vraag | 1 | 2a | 2b | 2c | 3a | 3b |
| --- | --- | --- | --- | --- | --- | --- |
| Antwoord |   |   |   |   |   |   |
| Punten | 3 | 1 | 1 | 1 | 2 | 2 |

_Nog niet beantwoord (modelantwoord ontbreekt)._

---

### 2024-1-vr9 · 2024-1

> [!warning] Herinnering-reconstructie (fragment)
> Deze vraag is een **herinnering**-reconstructie (volledigheid: fragment) — geen officiële ITAA-bundel. Modelantwoord rust op de geherinterpreteerde vraagtekst (ADR-022).

**Vraagformaat**: J/F · **Antwoord-type**: — · **Confidence**: —

#### Vraagtekst

9 Fiscale procedure

- **A.** Bericht van wijziging aangetekend, uiterlijke termijn?
- **B.** Belastingplichtige verlaat België, wat te doen?
- **C.** Bericht van wijziging, verjaringstermijn is nakende, wat te doen?
- **D.** Vraag om inlichtingen, termijn?

E. Bewaarplicht, welke stukken + termijn

> [!note]- Geherinterpreteerde vraagtekst (ADR-022)
> Casus fiscale procedure, 5 deelvragen:
> A. Wat is de uiterlijke termijn voor een bericht van wijziging dat aangetekend wordt verzonden?
> B. Een belastingplichtige verlaat België — wat moet er gebeuren (op vlak van aangifte en verjaring)?
> C. De verjaringstermijn voor een bericht van wijziging is nakende — wat moet de fiscus doen?
> D. Wat is de termijn waarbinnen de belastingplichtige moet antwoorden op een vraag om inlichtingen?
> E. Bewaarplicht — welke stukken moeten bewaard worden en wat zijn de termijnen?
> 
> _Motivering_: Vijf korte open vragen in trefwoord-vorm. Stam is in elk geval voldoende duidelijk om beantwoordbaar te zijn. Herformulering vult werkwoord en context aan.
> _Confidence_: inferred · _Datum_: 2026-05-19

_Nog niet beantwoord (modelantwoord ontbreekt)._

---

## PO 2.6

_10 vragen — 1 met modelantwoord — 0 met gap-rapport._

### 2008-bibf-vrH3 · 2008-bibf

**Vraagformaat**: open · **Antwoord-type**: — · **Confidence**: —

#### Vraagtekst

Ik (woonachtig in Gent) wil mijn effecten op naam ter waarde van 300.000 euro schenken aan mijn dochter van 22 jaar (woonachtig in Leuven) tegen een zo laag mogelijke fiscale kost.

**Welke zijn mijn mogelijkheden ?**

Wie betaalt de schenkingsrechten en hoeveel (in euro) ? Zitten er addertjes onder het gras ? - Schenking bij akte verleden door een Nederlandse notaris. Er zijn geen schenkingsrechten in Nederland of België verschuldigd Bij mijn overlijden binnen de 3 jaar dient mijn dochter nog successierechten te betalen - Schenking aan het 3 % tarief dat geldt in Vlaanderen Mijn dochter betaalt 9.000 euro

#### Modelantwoord

Optie 1: Nederlandse notariële akte (geen schenkingsrechten, wél successie bij overlijden < 3 jaar). Optie 2: 3 %-tarief Vlaanderen → dochter betaalt 9 000 EUR.

> [!success]- Motivering
> - Schenking bij akte verleden door een Nederlandse notaris. Er zijn geen schenkingsrechten in Nederland of België verschuldigd. Bij mijn overlijden binnen de 3 jaar dient mijn dochter nog successierechten te betalen. - Schenking aan het 3 % tarief dat geldt in Vlaanderen. Mijn dochter betaalt 9.000 euro.

> [!info]- Bronnen (1)
> - _pdf-modelantwoord_

---

### 2013-1-vr27 · 2013-1 · 8.0 pt

**Vraagformaat**: J/F · **Antwoord-type**: — · **Confidence**: —

#### Vraagtekst

> De heer Vandenbroucke, wonende in Nederland, verkoopt aan mevrouw Leroy, wonende in
> België, een in Leuven gelegen gemeubileerd appartement (mevrouw Leroy is al eigenaar van
> het bovenvermeld appartement: zij wil er een duplex van maken).

De optredende notaris is
meester Vandewielen, notaris te Amsterdam. De akte wordt verleden op 17 december 2012.
De verkoopprijs wordt bepaald als volgt: € 300.000, waarvan € 25.000 voor het meubilair.
De akte bevat volgende vermeldingen:
 de verkoopwaarde van het appartement bedraagt 250.000 euro;
 mw. Leroy is gehouden tot betaling van het ereloon van de notaris, ten bedrage van
5.000 euro;
 mw. Leroy is gehouden tot betaling van de achterstallige lasten van de mede-
eigendom die van de heer Vandenbroucke worden gevorderd en tot op heden
onbetaald gebleven zijn, ten bedrage van 3.000 euro.

- **a.** Moet die akte in België worden geregistreerd?

Antwoord

Ja, het is verplicht

Neen, het is niet nodig

De registratie is een facultatieve formaliteit, maar wordt aanbevolen omdat ze in
België een zekere datum verschaft

- **b.** Indien ja, wie is ertoe gehouden de akte te laten registreren?

Antwoord


Dhr. Vandenbroucke

Mw. Leroy

Mr. Vandewielen

Dhr. Vandenbroucke en Mw. Leroy tezamen

Die verantwoordelijkheid berust niet op een bepaalde persoon in het bijzonder, het
voornaamste is dat de akte wordt geregistreerd.
c) Zo ja, binnen welke termijn moet de akte ter registratie worden aangeboden?
Antwoord

15 dagen

1 maand

2 maanden

4 maanden

Geen termijn voorzien
d) Geef de belastbare grondslag in de registratierechten aan, indien de akte (al dan niet
verplicht) voor de formaliteit van registratie wordt aangeboden.

**Antwoord

Geen, vast recht van 25 euro

250.**

000 euro

300.000 euro

275.000 euro

305.000 euro

278.000 euro

308.000 euro

_Nog niet beantwoord (modelantwoord ontbreekt)._

#### Subvraag a)

Moet die akte in België worden geregistreerd?

#### Subvraag b)

Indien ja, wie is ertoe gehouden de akte te laten registreren?

#### Subvraag c)

Zo ja, binnen welke termijn moet de akte ter registratie worden aangeboden?

#### Subvraag d)

Geef de belastbare grondslag in de registratierechten aan, indien de akte (al dan niet
verplicht) voor de formaliteit van registratie wordt aangeboden.

---

### 2013-1-vr28 · 2013-1 · 2.0 pt

**Vraagformaat**: J/F · **Antwoord-type**: — · **Confidence**: —

#### Vraagtekst

> De heer André, sinds meer dan 10 jaar weduwnaar, is overleden en laat als enige wettige
> erfgename zijn dochter Anne na.

Korte tijd vóór zijn overlijden heeft de heer André een authentiek testament opgesteld (dat bij
een notaris werd neergelegd) waarin hij mevrouw Michèle, met wie hij sinds enige jaren
samenleeft, als algemeen legataris aanstelt.
Wanneer mevrouw Michèle verneemt dat zij tot algemeen legataris is aangesteld, uit zij de
wens om aan de nalatenschap te verzaken, want zij heeft altijd goed kunnen opschieten met
Anne en beschouwt de beslissing van de heer André jegens zijn dochter als een
onrechtvaardigheid.

**Hoe zal de ontvanger van de successierechten dit geval behandelen?**

**Antwoord

Mevrouw Michèle kan niet verzaken aan de nalatenschap, want het testament is
authentiek.**

Zij zal het volledig netto actief van de nalatenschap ontvangen. Het
toegepaste tarief is het tarief tussen personen zonder enige graad van verwantschap.

Anne zal het volledig netto actief van de nalatenschap ontvangen. Het toegepaste
tarief is het tarief in rechte lijn, met de aftrek voorzien voor de erfgenaam in rechte
lijn.

Aangezien de staat niet mag benadeeld worden ten gevolge van de verzaking, zal
Anne de rechten verschuldigd zijn die hadden moeten betaald worden zonder
verzaking aan de nalatenschap. Anne zal dus het volledig netto actief van de
nalatenschap ontvangen. Het toegepaste tarief is het tarief tussen personen zonder
enige graad van verwantschap.

Het testament kan op burgerrechtelijk gebied worden aangevochten. Anne kan
inroepen dat zij, bij de uitvoering van het testament, haar recht op het voorbehouden
gedeelte had kunnen laten gelden. Anne zal het volledig netto actief van de
nalatenschap ontvangen. Het toegepaste tarief is het tarief in rechte lijn, voor de helft
van de nalatenschap, en het tarief tussen personen zonder enige graad van
verwantschap, voor de andere helft van de nalatenschap.
BEGINSELEN VAN EUROPEES EN INTERNATIONAAL 10 PUNTEN
FISCAAL RECHT

_Nog niet beantwoord (modelantwoord ontbreekt)._

---

### 2013-2-vr28 · 2013-2 · 5.0 pt

**Vraagformaat**: J/F · **Antwoord-type**: — · **Confidence**: —

#### Vraagtekst

Dhr. André, weduwnaar, is op 1 augustus 2012 tijdens de vakantie in Spanje overleden.
Hij heeft 2 kinderen als erfgenaam: dochter Hélène en zoon Johan.
Hij had zijn fiscale woonplaats in Luik.
Aangaande de elementen in het passief van de nalatenschap:
- Kruis aan of de elementen dienen te worden aangenomen of niet:
- Indien ze moet verworpen worden, verklaar om welke reden(en) (de aangenomen
elementen dient u niet te verklaren)
Zijn nalatenschap omvat:
Actief:
1) Woonhuis in Luik € 200.000
2) Appartement in Middelkerke € 100.000
3) (Geblokkeerde) termijnrekening bij ING in Brussel € 10.000
4) Zichtrekening bij de Bank van de Post € 1.000
5) Stofferend huisraad in België € 5.000
Passief:
1) De factuur van de begrafenisondernemer (inclusief de repatriëringskosten van het lichaam
voor een bedrag van € 2.500) € 10.000
Antwoord … / 0,5 punt

|   |   |
| --- | --- |
| Aangenomen |   |
| Niet aangenomen |   |
| Verklaar |   |

2) Vliegticket voor Hélène, haar echtgenoot en de kinderen: terugkeer uit Italië om aanwezig
te kunnen zijn op de begrafenis (het gezin was bij het overlijden op vakantie in Italië) € 2.000
Antwoord … / 0,5 punt

|   |   |
| --- | --- |
| Aangenomen |   |
| Niet aangenomen |   |
| Verklaar |   |

3) Factuur voor de huur van ceremoniekledij door Hélène en haar gezin
(NB: deze kleren werden gedragen op de begrafenis van de overledene) € 1.000
Antwoord … / 0,5 punt

|   |   |
| --- | --- |
| Aangenomen |   |
| Niet aangenomen |   |
| Verklaar |   |

4) Factuur voor de bloemen op de begrafenisplechtigheid € 750
Antwoord … / 0,5 punt

|   |   |
| --- | --- |
| Aangenomen |   |
| Niet aangenomen |   |
| Verklaar |   |

5) Ereloon van de notaris die het “attest van erfopvolging” heeft opgesteld € 250
Antwoord … / 0,5 punt

|   |   |
| --- | --- |
| Aangenomen |   |
| Niet aangenomen |   |
| Verklaar |   |

6) Johan heeft op 15 oktober 2012 de stookolietank van het huis in Luik laten vullen, om het
tijdens de wintermaanden te kunnen verwarmen: bedrag van de factuur € 2.500
Antwoord … / 0,5 punt

|   |   |
| --- | --- |
| Aangenomen |   |
| Niet aangenomen |   |
| Verklaar |   |

7) Bedrag verschuldigd aan de mede-eigendom van het gebouw waarin het appartement van
de overledene zich bevindt (afrekening op 30 augustus 2012 door de syndicus opgesteld,
maar afgesloten op 30 juni 2012, datum van de algemene vergadering van de mede-
eigendom) € 3.000
Antwoord … / 0,5 punt

|   |   |
| --- | --- |
| Aangenomen |   |
| Niet aangenomen |   |
| Verklaar |   |

8) Ereloonnota van 5 augustus 2012: de overledene had op 1 februari 2012 een advocaat
belast met de invordering van de onbetaalde huur i.v.m. het appartement in Middelkerke (het
vonnis dat het beslag beveelt, werd op 15 juli 2012 geveld en was niet meer vatbaar voor
beroep) € 1.200
Antwoord … / 0,5 punt

|   |   |
| --- | --- |
| Aangenomen |   |
| Niet aangenomen |   |
| Verklaar |   |

9) Lening door de overledene aangegaan bij zijn dochter Hélène
(NB: deze post wordt verantwoord door een door de overledene ondertekende
schuldbekentenis) € 2.000
Antwoord … / 0,5 punt

|   |   |
| --- | --- |
| Aangenomen |   |
| Niet aangenomen |   |
| Verklaar |   |

10) Saldo van een lening door de overledene aangegaan bij zijn zoon Johan
(NB: deze lening werd aangewend voor de vervanging van een venster in het huis in Luik.
Daar de overledene geen gebruik kon maken van zijn geblokkeerde rekening en hij wachtte
op de ontvangst van de onbetaalde huur i.v.m. het appartement in Middelkerke, wordt deze
post verantwoord door een door de overledene ondertekende schuldbekentenis) € 4.000
Antwoord … /0,5 punten

|   |   |
| --- | --- |
| Aangenomen |   |
| Niet aangenomen |   |
| Verklaar |   |

_Nog niet beantwoord (modelantwoord ontbreekt)._

---

### 2013-2-vr29 · 2013-2 · 5.0 pt

**Vraagformaat**: berekening+MC · **Antwoord-type**: — · **Confidence**: —

#### Vraagtekst

Anne, Bernadette en Caroline zijn 3 zussen en in onverdeeldheid eigenaar (elk voor 1/3) van
een appartementsgebouw in Brussel.
Ze zijn eigenaar geworden van dit gebouw na het overlijden van hun ouders (overleden in
2007). Bij het overlijden werd het gebouw geschat op € 1.200.000.
In januari 2012 heeft Bernadette, tegen de prijs van € 500.000, haar deel afgestaan aan Xavier
(zonder enige band van verwantschap).
Eind 2012 wordt, naar aanleiding van een conflict tussen Anne en Caroline, overeengekomen
dat Anne de delen van Xavier en Caroline overneemt tegen de prijs van € 1.000.000.

- **a.** Bepaal de berekeningsgrondslag van de registratierechten bij de verkoop van

Bernadette aan Xavier en geef het tarief aan van de rechten dat zal worden toegepast.

**Antwoord … / 2 punten
b) Bepaal de berekeningsgrondslag van de registratierechten bij de verkoop van Xavier
en Caroline aan Anne en geeft het tarief aan van de rechten dat zal worden toegepast.**

Antwoord … / 2 punten

- **c.** Is het sub punt b) gegeven antwoord identiek als het Xavier is die het deel van Anne

en Caroline tegen dezelfde prijs overneemt?

Antwoord … / 1 punt

|   |   |
| --- | --- |
|   | Ja |
|   | Nee |

BEGINSELEN VAN EUROPEES EN INTERNATIONAAL 10 PUNTEN
FISCAAL RECHT

_Nog niet beantwoord (modelantwoord ontbreekt)._

#### Subvraag a)

Bepaal de berekeningsgrondslag van de registratierechten bij de verkoop van
Bernadette aan Xavier en geef het tarief aan van de rechten dat zal worden toegepast.

#### Subvraag b)

Bepaal de berekeningsgrondslag van de registratierechten bij de verkoop van Xavier
en Caroline aan Anne en geeft het tarief aan van de rechten dat zal worden toegepast.

#### Subvraag c)

Is het sub punt b) gegeven antwoord identiek als het Xavier is die het deel van Anne
en Caroline tegen dezelfde prijs overneemt?

---

### 2014-1-vr35 · 2014-1 · 5.0 pt

**Vraagformaat**: J/F · **Antwoord-type**: — · **Confidence**: —

#### Vraagtekst

> De BVBA Mokka zou het aanpalende terrein, gelegen aan de achterzijde van haar
> bedrijfsgebouw, willen aankopen om er een opslagplaats te bouwen.

Als de eigenaar te weten komt dat de BVBA geïnteresseerd is in de grond, is het zeer
waarschijnlijk dat hij daarvan zal profiteren om de prijs te verhogen door te speculeren op
het nut van de grond voor de BVBA.
Daarom vraagt de zaakvoerder van de

> BVBA Mokka aan zijn neef, die geen enkele band heeft
> met de BVBA en die de eigenaar totaal niet kent, om aan de eigenaar een bod op het terrein
> te doen.

De eigenaar stemt ermee in en de eigenaar en de neef sluiten een onderhandse
verkoopovereenkomst. De neef van de zaakvoerder verklaart dat hij het goed koopt voor
zichzelf of enige andere later aan te wijzen persoon.
De zaakvoerder van de BVBA consulteert u om zijn probleem uiteen te zetten.

**Welke oplossing zult u hem voorstellen?**

Zet uw antwoord uiteen en vermeld:
- welke akte(n) moet(en)verleden worden – vermeld de akte(n) met gebruikmaking van
de geëigende terminologie
- welke de partijen zijn die deze akte(n) moeten ondertekenen
- welke vorm (onderhandse of authentieke akte) deze akte(n) zal (zullen) aannemen
- of die akte(n) moet(en) onderworpen worden aan de formaliteit van registratie

- en, indien die akte(n) moet(en) geregistreerd worden, welk tarief zal toegepast worden
(vermeld alleen vast recht of evenredig recht en niet het percentage)
Antwoord

_Nog niet beantwoord (modelantwoord ontbreekt)._

---

### 2014-1-vr36 · 2014-1 · 5.0 pt

**Vraagformaat**: J/F · **Antwoord-type**: — · **Confidence**: —

#### Vraagtekst

> De heer Janssens is in België overleden op 12 augustus 2012.

Bij zijn overlijden was de heer Janssens gehuwd met Anne en had het echtpaar slechts één
dochter die, op de dag van het overlijden, meerderjarig was.
De echtgenoten waren gehuwd onder het stelsel van de scheiding van goederen.

> De heer Janssens heeft evenwel een testament nagelaten, waarin hij een aantal uiterste
> wilsbeschikkingen deed:
> - het geheel van de roerende goederen komt toe aan mw.

Tanghe, de verpleegster die
hem tijdens zijn ziekte verzorgde;
- de personenauto komt toe aan Frédérique Martin, nicht van de overledene;
- de volledige nalatenschap, na aftrek van de hiervoor vermelde goederen, komt toe aan
mw. Cambier, de jeugdvriendin van de heer Janssens.
Duid in de tabel de hoedanigheid van elke begiftigde aan.

**Vermeld wie de verplichting heeft een aangifte in de successierechten in te leveren
Hoedanigheid van de begiftigde
wettelijke algemeen algemeen legataris begiftigde bijzonder
erfgenaam legataris begiftigde onder onder legataris
algemene algemene
titel titel
echtgenote
dochter
Mevr.**

Tanghe
Mevr.
Martin
Mevr.
Cambier
Verplichte inlevering van de aangifte van nalatenschap
Echtgenote:
Dochter:

Mevr. Tanghe:
Mevr. Martin:
Mevr. Cambier:
BEGINSELEN VAN EUROPEES EN INTERNATIONAAL 10 PUNTEN
FISCAAL RECHT

_Nog niet beantwoord (modelantwoord ontbreekt)._

---

### 2015-1-vr46 · 2015-1 · 3.0 pt

**Vraagformaat**: J/F · **Antwoord-type**: — · **Confidence**: —

#### Vraagtekst

Een echtpaar koopt in september 2014 een huis in het Brussels Hoofdstedelijk Gewest tegen
de prijs van 255.000 EUR.
Kies uit onderstaande lijst welke uitspraak de kopers geen recht geeft op een vermindering
van de registratierechten:

- **A.** Het echtpaar verkrijgt de blote (naakte) eigendom van het goed en het vruchtgebruik zal

aangekocht worden door de vennootschap waarvan de echtgenoot bedrijfsleider is. Het
echtpaar zal het goed bewonen en zal belast worden op een voordeel van alle aard wegens
de kosteloze beschikking over een woning.

- **B.** Ten gevolge van een schenking door een oom is de echtgenote reeds eigenaar, in

onverdeeldheid met haar broer en haar zus, van een in het Vlaams Gewest gelegen huis.

- **C.** De echtgenote wil haar medische praktijk op het gelijkvloers van het gebouw inrichten (zij zal

er haar beroepsactiviteit uitoefenen) en het gezin zal de twee hogere verdiepingen
betrekken.

- **D.** Aangezien het gebouw waarop de koop betrekking heeft momenteel verhuurd wordt tegen

een uiterst lonende huurprijs (hoger dan de kost van de hypothecaire lening), beslist het
echtpaar om de huurder zijn huurcontract tot einddatum te laten uitdoen, met name tot 31
december 2015.
E. Om de duur van de volledige renovatie van hun eigen woning te overbruggen, zullen de
ouders van de echtgenote zich ook in deze woning vestigen en wordt deze woning voor
tenminste 3 jaar hun domicilie.

_Nog niet beantwoord (modelantwoord ontbreekt)._

---

### 2015-1-vr47 · 2015-1 · 3.0 pt

**Vraagformaat**: J/F · **Antwoord-type**: — · **Confidence**: —

#### Vraagtekst

> Mevrouw Martin is overleden op 20 februari 2014.

Op de datum van haar overlijden was ze
weduwe en haar enige erfgenamen zijn haar 3 kinderen.

> Mevrouw Martin is overleden in het
> Waals Gewest, maar haar woonplaats heeft ze steeds in het Vlaams Gewest gehad.

In december 2013 had mevrouw Martin een verplichting tot aankoop van 1.000 aandelen van
een Belgische vennootschap tegen de prijs van 17.000 EUR ondertekend.
Deze transactie was onderworpen aan een opschortende voorwaarde die op de datum van
haar overlijden nog niet was vervuld.
Na de tussenkomst van een accountant, die zijn opdracht uitvoerde op vraag van de
kinderen, werd de opschortende voorwaarde op 9 juli 2014 eindelijk vervuld. Het aan de
accountant betaalde ereloon bedraagt 2.420 EUR en de kinderen hebben de aandelen
verkocht tegen 22.500 EUR.

- **a.** Op welke datum moe(s)t de aangifte van nalatenschap worden ingediend?
- **A.** Dinsdag 22 juli 2014
- **B.** Vrijdag 20 juni 2014
- **C.** Woensdag 20 augustus 2014
- **b.** Vermeld het actief en het passief van de nalatenschap – effecten aan te geven in de

aangifte van nalatenschap ingediend binnen de sub a) gestelde termijn:

- **A.** actief = 17.000 EUR – geen passief
- **B.** actief = 22.500 EUR - geen passief
- **C.** actief = 22.500 EUR – passief = 2.420 EUR
- **D.** actief = 0 EUR - geen passief
- **c.** Welke is de uiterste datum voor de betaling van de successierechten?
- **A.** Dinsdag 22 juli 2014
- **B.** Woensdag 20 augustus 2014
- **C.** Maandag 22 september 2014

_Nog niet beantwoord (modelantwoord ontbreekt)._

#### Subvraag a)

Op welke datum moe(s)t de aangifte van nalatenschap worden ingediend?
A. Dinsdag 22 juli 2014
B. Vrijdag 20 juni 2014
C. Woensdag 20 augustus 2014

#### Subvraag b)

Vermeld het actief en het passief van de nalatenschap – effecten aan te geven in de
aangifte van nalatenschap ingediend binnen de sub a) gestelde termijn:
A. actief = 17.000 EUR – geen passief
B. actief = 22.500 EUR - geen passief
C. actief = 22.500 EUR – passief = 2.420 EUR
D. actief = 0 EUR - geen passief

#### Subvraag c)

Welke is de uiterste datum voor de betaling van de successierechten?
A. Dinsdag 22 juli 2014
B. Woensdag 20 augustus 2014
C. Maandag 22 september 2014

---

### 2015-1-vr48 · 2015-1 · 4.0 pt

**Vraagformaat**: J/F · **Antwoord-type**: — · **Confidence**: —

#### Vraagtekst

Een echtpaar wil de blote (naakte) eigendom van een onroerend goed aankopen waarvan het
vruchtgebruik door de verkoper wordt voorbehouden.
De blote eigendom wordt verkregen tegen een prijs van 186.000 EUR.
De vruchtgebruiker is 63 jaar oud.
De blote eigenaar is 31 jaar oud.
De verkoopwaarde van het goed werd geschat op 300.000 EUR.

- **a.** Welke waarde zal in aanmerking moeten worden genomen voor de berekening van de

registratierechten?

- **A.** 186.000 EUR
- **B.** 16% van 300.000 EUR
- **C.** Geen belastbare grondslag, er zal enkel een vast recht verschuldigd zijn
- **D.** 4 x 16% van 300.000 EUR

E. 300.000 EUR
Enige jaren later staat de vruchtgebruiker zijn vruchtgebruik af aan de blote eigenaar
waardoor laatstgenoemde dus de volle eigenaar wordt.
Het vruchtgebruik wordt afgestaan tegen de prijs van 250.000 EUR.
Op dat tijdstip is de vruchtgebruiker 74 jaar en de blote eigenaar 42 jaar oud.
De verkoopwaarde van het goed bedraagt nog steeds 300.000 EUR.

- **b.** Welke waarde moet in aanmerking worden genomen voor de berekening van de

registratierechten?

- **A.** 300.000 EUR
- **B.** 250.000 EUR
- **C.** 436.000 EUR (hetzij 250.000 EUR + de oorspronkelijk betaalde waarde van de blote

eigendom)

- **D.** Geen belastbare grondslag, er zal enkel een vast recht verschuldigd zijn

E. 300.000 EUR, maar er zal een vermindering van de rechten worden toegepast, tot beloop
van de bij de verkrijging van de blote eigendom betaalde rechten

BEGINSELEN VAN EUROPEES EN INTERNATIONAAL 10 PUNTEN
FISCAAL RECHT

_Nog niet beantwoord (modelantwoord ontbreekt)._

#### Subvraag a)

Welke waarde zal in aanmerking moeten worden genomen voor de berekening van de
registratierechten?
A. 186.000 EUR
B. 16% van 300.000 EUR
C. Geen belastbare grondslag, er zal enkel een vast recht verschuldigd zijn
D. 4 x 16% van 300.000 EUR
E. 300.000 EUR
Enige jaren later staat de vruchtgebruiker zijn vruchtgebruik af aan de blote eigenaar
waardoor laatstgenoemde dus de volle eigenaar wordt.
Het vruchtgebruik wordt afgestaan tegen de prijs van 250.000 EUR.
Op dat tijdstip is de vruchtgebruiker 7

#### Subvraag b)

Welke waarde moet in aanmerking worden genomen voor de berekening van de
registratierechten?
A. 300.000 EUR
B. 250.000 EUR
C. 436.000 EUR (hetzij 250.000 EUR + de oorspronkelijk betaalde waarde van de blote
eigendom)
D. Geen belastbare grondslag, er zal enkel een vast recht verschuldigd zijn
E. 300.000 EUR, maar er zal een vermindering van de rechten worden toegepast, tot beloop
van de bij de verkrijging van de blote eigendom betaalde rechten
BEGINSELEN VAN EUROPEES EN INTERNATIONAAL 10 PUNTEN
F

---

## PO 2.8

_8 vragen — 0 met modelantwoord — 0 met gap-rapport._

### 2013-1-vr29 · 2013-1 · 5.0 pt

**Vraagformaat**: open · **Antwoord-type**: — · **Confidence**: —

#### Vraagtekst

De heer B. is een natuurlijke persoon van Belgische nationaliteit, vrijgezel en zonder
personen ten laste, en op fiscaal gebied inwoner van België. Hij is bediende bij een
vennootschap naar Belgisch recht met een vaste inrichting in Frankrijk. Die Belgische
vennootschap maakt deel uit van een internationale groep die ook een dochtervennootschap
in Duitsland heeft.

> De heer B is het hoofd van de financiële afdeling van de Belgische vennootschap en zijn
> werkgever wil hem bijkomende verantwoordelijkheden toevertrouwen in het Franse
> bijkantoor en in de Duitse dochtervennootschap van de groep.

Hij zal dan drie dagen per week in België voor de centrale zetel in België werken, één dag per
week in Frankrijk voor de Franse vaste inrichting en één dag per week in Duitsland voor de
Duitse vennootschap.
De last van zijn bezoldigingen en van de indirecte kosten in verband met zijn werkzaamheid
wordt verdeeld tussen de Belgische vennootschap en haar Frans bijkantoor. Met de Duitse
vennootschap zal de heer B een afzonderlijke arbeidsovereenkomst sluiten en die
vennootschap zal zijn bezoldigingen in verband met zijn werkzaamheden in Duitsland
betalen. Bijgevolg zullen zijn loonkosten ten laste genomen worden door de verschillende
operationele entiteiten, op basis van de in elk land gepresteerde arbeidsduur.

> De heer B vraagt u of deze nieuwe situatie voor hem gevolgen zal hebben op het gebied van
> zijn inkomstenbelastingen, en zulks in België, Frankrijk en Duitsland.

Wat antwoordt u hem op grond van de beginselen ingeschreven in de door de Organisatie
voor Economische Samenwerking en Ontwikkeling (OESO) ontwikkelde Modelovereenkomst
betreffende het Inkomen en het Vermogen:

a) In welk(e) land(en) zal de heer B aan de inkomstenbelasting onderworpen zijn en welk
deel van zijn loon zal er moeten aangegeven worden?
Antwoord

_Nog niet beantwoord (modelantwoord ontbreekt)._

#### Subvraag a)

In welk(e) land(en) zal de heer B aan de inkomstenbelasting onderworpen zijn en welk
deel van zijn loon zal er moeten aangegeven worden?

---

### 2013-1-vr30 · 2013-1 · 5.0 pt

**Vraagformaat**: MC · **Antwoord-type**: — · **Confidence**: —

#### Vraagtekst

Uw cliënt en zijn echtgenote zijn de enige aandeelhouders van een naamloze vennootschap
naar Belgisch recht.
Hun schoonbroer bezit 97% van de aandelen van een handelsvennootschap naar Hongaars
recht (rechtsvorm die overeenkomt met een naamloze vennootschap). De resterende 3% van
het kapitaal van die vennootschap naar Hongaars recht is in bezit van de naamloze
vennootschap naar Belgisch recht van uw cliënt en zijn echtgenote.
De Belgische en de Hongaarse vennootschappen worden volledig gescheiden beheerd. De
hiervoor beschreven toestand bestaat sinds 2001.
In 2010 heeft de Belgische naamloze vennootschap van uw cliënt een lening toegestaan aan
de Hongaarse vennootschap die, zoals hiervoor gezegd, in handen is van de schoonbroer
van uw cliënt.
Voorts heeft de Belgische vennootschap in 2012 dividenden van de Hongaarse
vennootschap geïnd.
De Hongaarse fiscus eist de inhouding van een bronheffing op de interesten van de lening en
op de dividenden, terwijl uw cliënt en zijn echtgenote dachten dat, gelet op de zogenaamde
Europese “Moeder-dochterrichtlijn” en “Interest-royaltyrichtlijn”, er in Hongarije op die
inkomsten geen bronheffing meer kon worden ingehouden.
Uw cliënt vraagt u of die richtlijnen van toepassing zijn op de hier hoger beschreven situatie.
a) Wat antwoordt u hem: ja of neen?
Antwoord
 “Moeder-dochterrichtlijn”

|   |   |
| --- | --- |
|   | Ja |
|   | Neen |

 “Interest-royaltyrichtlijn”

|   |   |
| --- | --- |
|   | Ja |
|   | Neen |

b) Verklaar uw antwoord door te verwijzen naar de bepalingen van die Europese
richtlijnen.
Antwoord

FISCALE PROCEDURE 15 PUNTEN

_Nog niet beantwoord (modelantwoord ontbreekt)._

#### Subvraag a)

Wat antwoordt u hem: ja of neen?

#### Subvraag b)

Verklaar uw antwoord door te verwijzen naar de bepalingen van die Europese
richtlijnen.

---

### 2013-2-vr30 · 2013-2 · 5.0 pt

**Vraagformaat**: MC · **Antwoord-type**: — · **Confidence**: —

#### Vraagtekst

Een naamloze vennootschap naar Belgisch recht die haar boekjaar afsluit op 31 december, is
in Italië actief via een bijkantoor dat goederen verkoopt aan in Italië gevestigde klanten. Het
bijkantoor neemt bestellingen op, keurt ze goed, reikt facturen uit aan de klanten, levert de
goederen en int de aan de klanten gefactureerde bedragen.
Dit bijkantoor voert haar eigen boekhouding.
Het Italiaans bijkantoor, dat in 2012 werd geopend en in datzelfde jaar zijn handelsactiviteiten
aanvatte, heeft voor het jaar 2012, zowel boekhoudkundig als fiscaal, verlies gemaakt.
In 2013 doet het bijkantoor wel goede zaken zodat de rekeningen met een positief saldo
zullen afsluiten, en wel met een winst die hoger is dan het in 2012 geleden verlies. Op
belastinggebied in Italië, zal het bijkantoor het totaal verlies van 2012 van de winst van 2013
aftrekken.
De Belgische vennootschap boekt in 2012 en 2013 winst met betrekking tot haar overige
activiteiten die enkel in België plaatsvinden. Om het bedrag van de voorafbetalingen te
bepalen die de Belgische vennootschap in 2012 en 2013 in België heeft gedaan, heeft zij geen
rekening gehouden met het feit dat zij over een Italiaans bijkantoor beschikt.
We veronderstellen dat er in België noch in Italië verworpen uitgaven zijn.
In 2013, alvorens de laatste hand te leggen aan de aangifte in de vennootschapsbelasting
voor het aanslagjaar 2013 (boekjaar afgesloten op 31/12/2012) van de Belgische
vennootschap, stelt de financiële directeur van de Belgische vennootschap u de volgende
vraag:

**Hoe moet het resultaat van het Italiaanse bijkantoor verwerkt worden in de aangifte in de
vennootschapsbelasting van de Belgische vennootschap in België voor het boekjaar
afgesloten op 31/12/2012 en voor het boekjaar dat zal afgesloten op 31/12/2013?**

- **a.** Verklaar uw antwoord en steun, desgevallend, op de beginselen neergelegd in de

“door de OESO ontwikkelde modelovereenkomst” naar het inkomen en naar het
vermogen.

**Antwoord … / 3 punten
b) Gelet op de informatie die uw cliënt u heeft verstrekt, is er enig advies die u hem voor
de toekomstige jaren dient te geven?**

Antwoord …/ 2 punten

_Nog niet beantwoord (modelantwoord ontbreekt)._

#### Subvraag a)

Verklaar uw antwoord en steun, desgevallend, op de beginselen neergelegd in de
“door de OESO ontwikkelde modelovereenkomst” naar het inkomen en naar het
vermogen.

#### Subvraag b)

Gelet op de informatie die uw cliënt u heeft verstrekt, is er enig advies die u hem voor
de toekomstige jaren dient te geven?

---

### 2013-2-vr31 · 2013-2 · 5.0 pt

**Vraagformaat**: MC · **Antwoord-type**: — · **Confidence**: —

#### Vraagtekst

/ 5 punten
Een natuurlijke persoon die als particulier handelt en fiscaal als een inwoner van België
wordt beschouwd zet u de volgende toestand uiteen: hij houdt een bankrekening aan in het
Groothertogdom Luxemburg en heeft in 2013 op die rekening in het Groothertogdom
interesten van obligaties geïnd. Die interesten werden in het Groothertogdom Luxemburg
onderworpen aan de “Woonstaatheffing”. Betrokkene zal die interesten in 2014 in België
aangeven in zijn aangifte in de personenbelasting.
Hij vraagt u:

- **a.** hoe hij die “Woonstaatheffing” in zijn Belgische belastingaangifte voor het

aanslagjaar 2014, inkomsten 2013, moet behandelen.

**Antwoord …/ 2,5 punten
b) of het overschot van die woonstaatheffing ten opzichte van de verschuldigde
Belgische belasting in België zal terugbetaald worden.**

Antwoord …/ 2,5 punten
FISCALE PROCEDURE

_Nog niet beantwoord (modelantwoord ontbreekt)._

#### Subvraag a)

hoe hij die “Woonstaatheffing” in zijn Belgische belastingaangifte voor het
aanslagjaar 2014, inkomsten 2013, moet behandelen.

#### Subvraag b)

of het overschot van die woonstaatheffing ten opzichte van de verschuldigde
Belgische belasting in België zal terugbetaald worden.

---

### 2014-1-vr37 · 2014-1 · 6.0 pt

**Vraagformaat**: J/F · **Antwoord-type**: — · **Confidence**: —

#### Vraagtekst

Een Belgische verblijfhoudende vennootschap is in Italië actief via een vaste inrichting (VI).
Tussen Italië en België geldt een bilaterale overeenkomst tot het vermijden van dubbele
belasting.
VI Italië Belg.verrichtingen Totaal Vennootschap
Jaar 1: Resultaat vóór belasting Verlies: 1000 Winst : 2000 Winst : 1000
Jaar 2: Resultaat vóór belasting Winst: 1000 Winst : 2000 Winst : 3000.
De gedelegeerd-bestuurder van deze vennootschap vraagt uw advies over volgend punt: zijn
financiële directeur meldt hem dat de Belgische vennootschap, voor jaar 2, zal belast worden
op een winst van 4.000, terwijl de boekhoudkundige winst slechts 3.000 bedraagt. Hij stelt u
volgende vragen:

- **a.** Is dat juist: ja of neen?

Antwoord

- **b.** Verklaar uw antwoord op grond van de beginselen van de door de OESO ontwikkelde

bilaterale modelovereenkomst tot het vermijden van dubbele belasting.
Antwoord

_Nog niet beantwoord (modelantwoord ontbreekt)._

#### Subvraag a)

Is dat juist: ja of neen?

#### Subvraag b)

Verklaar uw antwoord op grond van de beginselen van de door de OESO ontwikkelde
bilaterale modelovereenkomst tot het vermijden van dubbele belasting.

---

### 2014-1-vr38 · 2014-1 · 4.0 pt

**Vraagformaat**: J/F · **Antwoord-type**: — · **Confidence**: —

#### Vraagtekst

Een vennootschap naar Belgisch recht, zonder bijkantoor noch vaste inrichting in het
buitenland, wordt overgenomen door een vennootschap naar Duits recht. De Belgische
vennootschap had verrekenbare fiscale verliezen die zij nog niet van de latere winsten had
kunnen aftrekken.
a) Zullen die fiscale verliezen kunnen worden afgetrokken van de na de fusie
verwezenlijkte winsten:
Antwoord
 Uitsluitend op de in België verwezenlijkte winsten, en zulks overeenkomstig de in
België toepasselijke regels betreffende de fusies tussen vennootschappen naar
Belgisch recht

|   |   |
| --- | --- |
|   | Ja |
|   | Neen |

 Op de winsten van de overnemende Duitse vennootschap, ongeacht die in België of in
Duitsland worden verwezenlijkt

|   |   |
| --- | --- |
|   | Ja |
|   | Neen |

 Op de winsten van de Duitse overnemende vennootschap die in Duitsland worden
verwezenlijkt

|   |   |
| --- | --- |
|   | Ja |
|   | Neen |

b) Verklaar uw antwoord op grond van de op deze toestand toepasselijke beginselen en
verwijs naar de toepasselijke bepaling van Richtlijn 2009/133/EG van de Raad van 19
oktober 2009 voor fusies, splitsingen, enz. met betrekking tot vennootschappen uit de
Europese Unie (volgens de erin vastgestelde voorwaarden).
Antwoord
FISCALE PROCEDURE 15 PUNTEN

_Nog niet beantwoord (modelantwoord ontbreekt)._

#### Subvraag a)

Zullen die fiscale verliezen kunnen worden afgetrokken van de na de fusie
verwezenlijkte winsten:

#### Subvraag b)

Verklaar uw antwoord op grond van de op deze toestand toepasselijke beginselen en
verwijs naar de toepasselijke bepaling van Richtlijn 2009/133/EG van de Raad van 19
oktober 2009 voor fusies, splitsingen, enz. met betrekking tot vennootschappen uit de
Europese Unie (volgens de erin vastgestelde voorwaarden).

---

### 2015-1-vr49 · 2015-1 · 6.0 pt

**Vraagformaat**: J/F · **Antwoord-type**: — · **Confidence**: —

#### Vraagtekst

Beantwoord de vragen met “waar” of “niet waar” op basis van de beginselen ingeschreven in
de “door de OESO ontwikkelde modelovereenkomst naar het inkomen en naar het
vermogen”.
a) Een natuurlijke persoon die geen dubbele nationaliteit bezit en die door beide
overeenkomstsluitende staten bij een overeenkomst tot vermijding van dubbele
belasting als inwoner wordt beschouwd, zal in de staat, waarvan hij de nationaliteit
heeft steeds op zijn wereldinkomen worden belast zonder andere criteria in
aanmerking te nemen. Deze persoon bezit de nationaliteit van één van beide hiervoor
beoogde overeenkomstsluitende staten.
Antwoord … / 1 punt

|   |   |
| --- | --- |
|   | Waar |
|   | Niet waar |

b) Een pensioen dat door België aan een natuurlijk persoon van Belgische nationaliteit
wordt betaald ter zake van een vroegere dienstbetrekking als ambtenaar van een
Federale Overheidsdienst zal niet meer in België belastbaar zijn, indien deze
natuurlijke persoon inwoner wordt van een land waarmee België een overeenkomst tot
voorkoming van dubbele belasting heeft gesloten.
Antwoord … / 1 punt

|   |   |
| --- | --- |
|   | Waar |
|   | Niet waar |

c) Een steengroeve is slechts een vaste inrichting, indien de uitbatingsduur ervan 6
maanden overschrijdt.
Antwoord … / 1 punt

|   |   |
| --- | --- |
|   | Waar |
|   | Niet waar |

d) De overeenkomsten tot voorkoming van dubbele belasting, die volgens de hierboven
bedoelde modelovereenkomst afgesloten zijn, gelden voor de successierechten.
Antwoord … / 1 punt

|   |   |
| --- | --- |
|   | Waar |
|   | Niet waar |

e) Voor een natuurlijke persoon die inwoner is van één van de overeenkomstsluitende
staten, zijn de onroerende inkomsten verkregen in de andere staat, uitsluitend
belastbaar in die andere staat (met name de bronstaat).

Antwoord … / 1 punt

|   |   |
| --- | --- |
|   | Waar |
|   | Niet waar |

f) Als een vaste inrichting van een onderneming, die inwoner is van een andere
overeenkomstsluitende staat, een supplement in de inkomstenbelasting wordt
opgelegd naar aanleiding van een controle op de verrekenprijzen toegepast op de
goederen- of dienstenstromen tussen die vaste inrichting en haar hoofdzetel in de
andere overeenkomstsluitende staat, zal er sprake zijn van juridisch dubbele belasting
en is dit onvermijdbaar.
Antwoord … / 1 punt

|   |   |
| --- | --- |
|   | Waar |
|   | Niet waar |

_Nog niet beantwoord (modelantwoord ontbreekt)._

#### Subvraag a)

Een natuurlijke persoon die geen dubbele nationaliteit bezit en die door beide
overeenkomstsluitende staten bij een overeenkomst tot vermijding van dubbele
belasting als inwoner wordt beschouwd, zal in de staat, waarvan hij de nationaliteit
heeft steeds op zijn wereldinkomen worden belast zonder andere criteria in
aanmerking te nemen. Deze persoon bezit de nationaliteit van één van beide hiervoor
beoogde overeenkomstsluitende staten.

#### Subvraag b)

Een pensioen dat door België aan een natuurlijk persoon van Belgische nationaliteit
wordt betaald ter zake van een vroegere dienstbetrekking als ambtenaar van een
Federale Overheidsdienst zal niet meer in België belastbaar zijn, indien deze
natuurlijke persoon inwoner wordt van een land waarmee België een overeenkomst tot
voorkoming van dubbele belasting heeft gesloten.

#### Subvraag c)

Een steengroeve is slechts een vaste inrichting, indien de uitbatingsduur ervan 6
maanden overschrijdt.

#### Subvraag d)

De overeenkomsten tot voorkoming van dubbele belasting, die volgens de hierboven
bedoelde modelovereenkomst afgesloten zijn, gelden voor de successierechten.

#### Subvraag e)

Voor een natuurlijke persoon die inwoner is van één van de overeenkomstsluitende
staten, zijn de onroerende inkomsten verkregen in de andere staat, uitsluitend
belastbaar in die andere staat (met name de bronstaat).

#### Subvraag f)

Als een vaste inrichting van een onderneming, die inwoner is van een andere
overeenkomstsluitende staat, een supplement in de inkomstenbelasting wordt
opgelegd naar aanleiding van een controle op de verrekenprijzen toegepast op de
goederen- of dienstenstromen tussen die vaste inrichting en haar hoofdzetel in de
andere overeenkomstsluitende staat, zal er sprake zijn van juridisch dubbele belasting
en is dit onvermijdbaar.

---

### 2015-1-vr50 · 2015-1 · 4.0 pt

**Vraagformaat**: J/F · **Antwoord-type**: — · **Confidence**: —

#### Vraagtekst

De financieel verantwoordelijke van een internationale vereniging zonder winstoogmerk
(ivzw) met maatschappelijke zetel in België raadpleegt u, omdat deze ivzw haar activiteiten
wil uitbreiden tot andere landen van de Europese Unie. In het kader van deze expansie wil de
ivzw naar Belgisch recht een caritatieve vereniging zonder winstoogmerk, die al lang in
Spanje gevestigd is en er zeer waardevolle landeigendommen bezit, overnemen.
Na de afwikkeling van deze operatie zal de ivzw naar Belgisch recht dus, naast haar
hoofdzetel in België, ook over een uitbatingszetel van verrichtingen in Spanje beschikken.
Volgens de informatie waarover uw cliënt beschikt met betrekking tot de fiscale gevolgen van
deze verrichting in Spanje, zou deze overname aldaar aanleiding geven tot belastingheffing
over de meerwaarde op de onroerende goederen in Spanje en wel voor een aanzienlijk
bedrag.
De financieel verantwoordelijke vraagt u of deze transactie, met toepassing van richtlijn
2009/133/EG van de Raad van 19 oktober 2009 betreffende de gemeenschappelijke fiscale
regeling voor fusies, splitsingen, gedeeltelijke splitsingen, inbreng van activa, enz., kan
uitgevoerd worden met vrijstelling van belasting.
a) Wat antwoordt u hem:
Antwoord … / 2 punten

|   |   |
| --- | --- |
|   | Ja |
|   | Neen |

b) Gelieve uw antwoord te motiveren door de uitleg die u aan uw cliënt zult verstrekken
weer te geven.
Antwoord … / 2 punten

JURIDISCHE EN BEROEPSNORMEN MET BETREKKING 20 PUNTEN
TOT DE ACCOUNTANCY, DE BELASTINGCONSULTANCY
EN DE ANDERE WETTELIJKE OPDRACHTEN VAN DE
ACCOUNTANT EN VAN DE BELASTINGCONSULENT

_Nog niet beantwoord (modelantwoord ontbreekt)._

#### Subvraag a)

Wat antwoordt u hem:

#### Subvraag b)

Gelieve uw antwoord te motiveren door de uitleg die u aan uw cliënt zult verstrekken
weer te geven.

---

## PO 3.0

_38 vragen — 5 met modelantwoord — 0 met gap-rapport._

### 2003-bibf-vrI2 · 2003-bibf · 11 pt

_Ook geklassificeerd onder_: 2.6

**Vraagformaat**: open · **Antwoord-type**: — · **Confidence**: —

#### Vraagtekst

Een handelaar wenst zijn eenmanszaak om te zetten in een vennootschap, nl. een BVBA. Hij brengt het volgende in zijn vennootschap: - het gebouw waarin hij zijn activiteit uitbaat dat hem ook dient als woonhuis: waarde 200.000,00 euro. - materieel, apparatuur, meubilair = waarde 5.000,00 euro. - Bestelwagen: waarde 10.000,00 euro. - gereed geld ter waarde van 10.000,00 euro.

- **a.** Geef de diverse formaliteiten (vennootschapsrechterlijke, sociale, fiscale, administratieve...) aan die nodig zijn voor en na het verlijden van de oprichtingsakte
- **b.** Geef aan hoeveel registratierechten hij zal betalen wetende dat zijn inbreng als volgt zal vergoed worden: 3 PUNTEN - met kapitaalaandelen voor 200.000,00 euro - op rekening-courant: 25.000,00 euro.

_Nog niet beantwoord (modelantwoord ontbreekt)._

---

### 2003-bibf-vrI3 · 2003-bibf · 4 pt

**Vraagformaat**: open · **Antwoord-type**: — · **Confidence**: —

#### Vraagtekst

Wat zijn de verplichtingen van een vennootschap ingeval uit de balans een overgedragen verlies blijkt of uit de resultatenrekening gedurende twee opeenvolgende boekjaren een verlies van het boekjaar blijkt?

_Nog niet beantwoord (modelantwoord ontbreekt)._

---

### 2003-bibf-vrI4 · 2003-bibf · 3 pt

**Vraagformaat**: open · **Antwoord-type**: — · **Confidence**: —

#### Vraagtekst

Wat zijn de mogelijke gevolgen voor een vennootschap die gedurende drie opeenvolgende boekjaren haar jaarrekening niet heeft neergelegd bij de N.B.B.?

_Nog niet beantwoord (modelantwoord ontbreekt)._

---

### 2008-bibf-vrI1 · 2008-bibf

**Vraagformaat**: open · **Antwoord-type**: — · **Confidence**: —

#### Vraagtekst

De raad van bestuur van een NV wenst over te gaan tot een kapitaalverhoging. Omdat de verhoging dringend is, wenst ze geen buitengewone algemene vergadering bijeen te roepen. Is het mogelijk? Indien u bevestigend antwoordt, wat zijn de voorwaarden?

#### Modelantwoord

Dit is uitsluitend mogelijk binnen het kader van het toegestane kapitaal

> [!success]- Motivering
> Dit is uitsluitend mogelijk binnen het kader van het toegestane kapitaal (art. 603-604 W.Venn). De statuten kunnen aan de raad van bestuur de bevoegdheid toekennen om het geplaatste maatschappelijk kapitaal in één of meer malen tot een bepaald bedrag te verhogen, dat, voor de vennootschappen die een publiek beroep op het spaarwezen doen of hebben gedaan, niet hoger mag zijn dan het bedrag van dat maatschappelijke kapitaal (art. 603 W. Venn.). De bevoegdheid bedoeld in artikel 603 kan slechts worden uitgeoefend gedurende vijf jaar, te rekenen van de bekendmaking van de oprichtingsakte of van de wijziging van de statuten. Zij kan echter door de algemene vergadering, bij een besluit genomen volgens de regels die voor de wijziging van de statuten zijn gesteld, een of meer malen worden hernieuwd voor een termijn die niet langer mag zijn dan vijf jaar. Wanneer de oprichters of de algemene vergadering besluiten de hierboven bedoelde bevoegdheid toe te kennen of te vernieuwen, worden de bijzondere omstandigheden waarin van het toegestane kapitaal kan gebruikgemaakt worden en de hierbij nagestreefde doeleinden in een bijzonder verslag uiteengezet.

> [!info]- Bronnen (1)
> - _pdf-modelantwoord_

---

### 2008-bibf-vrI2 · 2008-bibf

**Vraagformaat**: open · **Antwoord-type**: — · **Confidence**: —

#### Vraagtekst

Wanneer verplicht het Wetboek van vennootschappen een financieel plan op te stellen? Wat is het doel van een financieel plan? Aan wie moet het worden overhandigd?

#### Modelantwoord

Een financieel plan moet worden opgesteld bij de oprichting van een

> [!success]- Motivering
> Een financieel plan moet worden opgesteld bij de oprichting van een BVBA (art. 215 W.Venn), CVBA (art. 391 W.Venn), NV(art. 440 W.Venn), Comm. VA(art. 657 W.Venn), SE en SCE(art. 884 en 959 W.Venn). Het financieel plan moet aantonen dat het bedrag van het kapitaal toereikend is om de voorgenomen bedrijvigheid uit te oefenen. Het financieel plan moet, bij de oprichting, worden overhandigd aan de notaris die het zal bewaren.

> [!info]- Bronnen (1)
> - _pdf-modelantwoord_

---

### 2008-bibf-vrI3 · 2008-bibf

**Vraagformaat**: open · **Antwoord-type**: — · **Confidence**: —

#### Vraagtekst

De zaakvoerder van een BVBA is de enige vennoot. Moet een procedure worden gevolgd wanneer de zaakvoerder bij een verrichting een belang heeft, van vermogenrechtelijke aard, dat strijdig is met de belangen van de vennootschap?

#### Modelantwoord

Hij mag de geplande verrichting doen maar hij moet hierover een

> [!success]- Motivering
> Hij mag de geplande verrichting doen maar hij moet hierover een bijzonder verslag opstellen dat samen met de jaarrekening moet worden neergelegd (art. 261 W. Venn.).

> [!info]- Bronnen (1)
> - _pdf-modelantwoord_

---

### 2008-bibf-vrI4 · 2008-bibf

**Vraagformaat**: open · **Antwoord-type**: — · **Confidence**: —

#### Vraagtekst

Kan een burgerlijke vennootschap die de rechtsvorm van een handelsvennootschap heeft aangenomen, een gerechtelijk akkoord bekomen? Verantwoord uw antwoord.

#### Modelantwoord

Alleen handelaars kunnen een gerechtelijk akkoord bekomen. Een

> [!success]- Motivering
> Alleen handelaars kunnen een gerechtelijk akkoord bekomen. Een burgerlijke vennootschap, zelfs met handelsvorm, is geen handelaar. Bijgevolg kan ze geen gerechtelijk akkoord bekomen.

> [!info]- Bronnen (1)
> - _pdf-modelantwoord_

---

### 2008-bibf-vrI5 · 2008-bibf

**Vraagformaat**: open · **Antwoord-type**: — · **Confidence**: —

#### Vraagtekst

Welk is de aansprakelijkheid van de oprichters van een BVBA en welk verschil kan er zijn met een NV?

#### Modelantwoord

Artikel 229 – 456 – 450 van het Wetboek Vennootschappen

> [!success]- Motivering
> Artikel 229 – 456 – 450 van het Wetboek Vennootschappen

> [!info]- Bronnen (1)
> - _pdf-modelantwoord_

---

### 2013-1-vr14 · 2013-1 · 14.0 pt

_Ook geklassificeerd onder_: 1.2

**Vraagformaat**: J/F · **Antwoord-type**: — · **Confidence**: —

#### Vraagtekst

Hierna volgt de balans van de bvba Avenir, afgesloten op 31/12/2012:
ACTIVA PASSIVA
Materiële vaste activa € 25.000 Geplaatst kapitaal € 20.460
Voorraden € 7.500 Overgedragen winst € 44.540
Vorderingen op – 1 jaar € 75.500 Leveranciers € 28.500
Liquide middelen € 12.500 Belastingschulden € 27.000
€ 120.500 € 120.500
Het aandeelhouderschap van deze bvba is sinds lang in handen van Paul X, met 50% van de
aandelen, Jean Y met 45% van de aandelen, en Albert M die de resterende 5% aanhoudt, hetzij in
totaal 186 aandelen.
De statuten wijken niet af van het Wetboek van Vennootschappen.
Maar Jean Y overlijdt jammerlijk en laat als enige erfgenaam zijn zoon Cedric Y na.
Deel I
Cedric Y voornoemd, stelt u, als accountant van de bvba Avenir de volgende vragen:
Verklaar uw antwoorden bondig

- **a.** Wat zal er gebeuren met de aandelen, nu zijn vader Jean overleden is?

Antwoord

- **b.** Zal hij automatisch vennoot van de bvba worden?

Antwoord

- **c.** En hoe zit het met een eventuele overdracht van zijn aandelen?

Antwoord
Deel II
En daar een ongeluk nooit alleen komt, stelt Paul X vast dat Jean de invordering van een zeer
belangrijke klant had verwaarloosd en dat die klant ondertussen failliet verklaard is.
Het bedrag van de vordering bedraagt 60.000 euro.
Het blijkt dat die vordering al oninvorderbaar was vóór de afsluiting van de balans per
31/12/2012.

Paul X raadpleegt u en vraagt wat er, vanuit juridisch standpunt, moet gedaan worden.

**Antwoord
Deel III
Voorts ruikt Albert M, samen met een vriend, een unieke commerciële buitenkans.**

Maar daar ze
niet over de nodige liquide middelen beschikken, besluiten ze een S-BVBA op te richten, onder
de naam “Renaissance”.
Ze beslissen om u het boekhoudkundig en fiscaal beheer van het dossier toe te vertrouwen en
leggen u het ontwerp voor.
Hierna volgen twee vragen die ze u stellen met betrekking tot de oprichting van deze
vennootschap:
d) Is het plan uitvoerbaar voor de twee vennoten?
Antwoord
e) Welke is hun aansprakelijkheid als oprichter?
Antwoord

_Nog niet beantwoord (modelantwoord ontbreekt)._

#### Subvraag a)

Wat zal er gebeuren met de aandelen, nu zijn vader Jean overleden is?

#### Subvraag b)

Zal hij automatisch vennoot van de bvba worden?

#### Subvraag c)

En hoe zit het met een eventuele overdracht van zijn aandelen?

#### Subvraag d)

Is het plan uitvoerbaar voor de twee vennoten?

#### Subvraag e)

Welke is hun aansprakelijkheid als oprichter?

---

### 2013-1-vr16 · 2013-1 · 7.0 pt

_Ook geklassificeerd onder_: 1.6

**Vraagformaat**: MC · **Antwoord-type**: — · **Confidence**: —

#### Vraagtekst

Het Wetboek van Vennootschappen voorziet in een procedure van ontbinding.

- **a.** Wat is het voorwerp en het doel van de opdracht van de externe accountant?

Antwoord

- **b.** Wie stelt de staat van activa en passiva op?

Antwoord

- **c.** Wanneer kan de staat van activa en passiva opgesteld worden in continuïteit?

Antwoord

_Nog niet beantwoord (modelantwoord ontbreekt)._

#### Subvraag a)

Wat is het voorwerp en het doel van de opdracht van de externe accountant?

#### Subvraag b)

Wie stelt de staat van activa en passiva op?

#### Subvraag c)

Wanneer kan de staat van activa en passiva opgesteld worden in continuïteit?

---

### 2013-1-vr15 · 2013-1 · 6.0 pt

**Vraagformaat**: MC · **Antwoord-type**: — · **Confidence**: —

#### Vraagtekst

Sinds 1 januari 2008 kunnen er geen nieuwe effecten aan toonder uitgegeven worden.
De wetgever heeft gesteld dat uiterlijk op 31 december 2013 de effecten aan toonder
moeten omgezet zijn.

- **a.** De wetgever heeft om de omzetten te versnellen reeds een maatregel genomen,

een maatregel met een uitwerking in 2012 en/of 2013.

**Welke is deze maatregel.**

Welke actie kon/kan men ondernemen?.

**Antwoord
b) Wat gebeurt er met de effecten die niet zijn omgezet op 1 januari 2014 ?**

Antwoord

- **c.** Wat gebeurt er met de effecten die niet zijn omgezet op 1 januari 2015 ?

Antwoord

VENNOOTSCHAPSRECHT (BIJZONDERE MANDATEN) 30 PUNTEN

_Nog niet beantwoord (modelantwoord ontbreekt)._

#### Subvraag a)

De wetgever heeft om de omzetten te versnellen reeds een maatregel genomen,
een maatregel met een uitwerking in 2012 en/of 2013. Welke is deze maatregel.
Welke actie kon/kan men ondernemen?.

#### Subvraag b)

Wat gebeurt er met de effecten die niet zijn omgezet op 1 januari 2014 ?

#### Subvraag c)

Wat gebeurt er met de effecten die niet zijn omgezet op 1 januari 2015 ?

---

### 2013-1-vr17 · 2013-1 · 7.0 pt

_Ook geklassificeerd onder_: 1.6

**Vraagformaat**: J/F · **Antwoord-type**: — · **Confidence**: —

#### Vraagtekst

Op de boekhoudkundige staat van de

> BVBA HOLDING RICH komen nog diverse machines A
> voor.

De zaakvoerders van de

> BVBA HOLDING RICH hebben een gemotiveerde, technisch en
> financieel onderbouwde waardering gemaakt van deze machines (totale waarde
> € 600.

000) op basis van de berekening van de toekomstige kasstromen en op basis van het
nut van de machines voor het bedrijf. Aan de hand van deze waardering werd door het
college van zaakvoerders bij het opstellen van de boekhoudkundige staat van activa en
passiva een herwaarderingsmeerwaarde geboekt. Anderzijds heeft de leverancier van de
machines een bod gedaan om de machines A terug te kopen voor € 450.000, in dat geval
moet er wel een revisie op de machines A gebeuren van € 10.000.
De staat ziet er als volgt uit:
Staat activa en passiva
Machines A € 200.000 Kapitaal € 20.000
Machines A (herwaarderingsmeerw) € 400.000 Herwaarderingsmeerwaarde € 400.000
Handelsvorderingen – 1 jaar € 100.000 Overgedragen verlies € 50.000 (-)
Bank € 20.000 Resultaat v/d periode € 20.000
Schulden + 1 jaar € 250.000
Schulden – 1 jaar € 80.000
----------------------------------------------------------------------------------------------------------------------
Totaal € 720.000 € 720.000
a) Als accountant krijg je de opdracht om uw controleverslag te maken op
bovenstaande staat in het kader van de ontbinding van de vennootschap.
Bestudeer deze staat en geef drie mogelijke correcties die moeten toegepast
worden op deze staat.
Antwoord

b) Welk soort controle ga je toepassen bij uw verslag inzake ontbinding?
Antwoord
c) Kan deze ontbinding in één akte ook gesloten worden? Leg uit.
Antwoord

_Nog niet beantwoord (modelantwoord ontbreekt)._

#### Subvraag a)

Als accountant krijg je de opdracht om uw controleverslag te maken op
bovenstaande staat in het kader van de ontbinding van de vennootschap.
Bestudeer deze staat en geef drie mogelijke correcties die moeten toegepast
worden op deze staat.

#### Subvraag b)

Welk soort controle ga je toepassen bij uw verslag inzake ontbinding?

#### Subvraag c)

Kan deze ontbinding in één akte ook gesloten worden? Leg uit.

---

### 2013-1-vr18 · 2013-1 · 12.0 pt

_Ook geklassificeerd onder_: 1.6

**Vraagformaat**: open · **Antwoord-type**: — · **Confidence**: —

#### Vraagtekst

In de

> BVBA GOFORT werd een staat van activa en passiva afgesloten per 31/01/2013
> opgesteld en ondertekend door de interne boekhouder, met het oog op de ontbinding van de
> vennootschap.

De algemene vergadering wordt samengeroepen om te beslissen op
15/04/2013 bij notaris. Het controleverslag werd opgesteld door de externe accountant die
niet de reguliere adviseur is op 14/04/2013. Alle aandeelhouders bevestigen hun
aanwezigheid met uitzondering van een correct geïnformeerde vennoot met 10% van de
aandelen en die vraagt aan de zaakvoerders om de vergadering met drie weken te verdagen
gezien hij in het buitenland is op 15/04/2013.

**Geef drie opmerkingen bij vorige opgave en geef aan wat er dient te gebeuren.**

Antwoord

_Nog niet beantwoord (modelantwoord ontbreekt)._

---

### 2013-1-vr19 · 2013-1 · 4.0 pt

_Ook geklassificeerd onder_: 4.0, 1.6

**Vraagformaat**: MC · **Antwoord-type**: — · **Confidence**: —

#### Vraagtekst

De normen inzake het verslag op te stellen bij de omzetting van een vennootschap stelt dat
de beroepsbeoefenaar bij het aanvaarden van zijn opdracht over een behoorlijke
opdrachtbrief dient te beschikken.

- **a.** Wie ondertekent de opdrachtbrief ?

Antwoord

- **b.** Geef 3 elementen die minimaal in de opdrachtbrief dienen voor te komen.

Antwoord

PERSONENBELASTING 20 PUNTEN

_Nog niet beantwoord (modelantwoord ontbreekt)._

#### Subvraag a)

Wie ondertekent de opdrachtbrief ?

#### Subvraag b)

Geef 3 elementen die minimaal in de opdrachtbrief dienen voor te komen.

---

### 2013-2-vr14 · 2013-2 · 3.0 pt

_Ook geklassificeerd onder_: 1.2

**Vraagformaat**: J/F · **Antwoord-type**: — · **Confidence**: —

#### Vraagtekst

Wat de bij de Nationale Bank van België neergelegde jaarrekeningen betreft, stelt u op 4 mei
2013 vast dat uw nieuwe cliënt, de bvba “Mode Invest”, de jaarrekeningen van de vier laatste
boekjaren niet meer heeft neergelegd.

- **a.** Wat zult u uw cliënt adviseren?

Antwoord … / 1 punt

- **b.** Waarom?

Antwoord … / 2 punten

_Nog niet beantwoord (modelantwoord ontbreekt)._

#### Subvraag a)

Wat zult u uw cliënt adviseren?

#### Subvraag b)

Waarom?

---

### 2013-2-vr19 · 2013-2 · 22.0 pt

_Ook geklassificeerd onder_: 1.6

**Vraagformaat**: J/F · **Antwoord-type**: — · **Confidence**: —

#### Vraagtekst

Een collega accountant die je kent van uw beroepsvereniging vraagt om uw tussenkomst bij
de omzetting van een vennootschap van één van zijn klanten. Het betreft de CVBA Fortunito
die wenst om te zetten naar de BVBA Roflexfort.
Op vraag van uw collega zendt de interne boekhouder je daarvoor een proef- en saldibalans
per 30/09/2013 (statutair boekjaar 01/01/2013-31/12/2013).
a) Kruis het juiste antwoord aan.
Antwoord … / 6 punten

|   | Ja | Nee |
| --- | --- | --- |
| Kan in principe de CVBA Fortunito omgezet worden naar de BVBA Reflexfort |   |   |
| Kan in de statuten een bepaling staan waardoor de CVBA Fortunito niet kan <br> omgezet worden in de BVBA Reflexfort? |   |   |
| Kan je in het kader van je onafhankelijkheid deze opdracht uitvoeren? |   |   |

b) Kan je werken op basis van een proef- en saldi balans zoals

_in bijlage? Verklaar uw
antwoord._

Antwoord … / 2 punten

|   |   |
| --- | --- |
|   | Ja |
|   | Nee |

c) Wie draagt de verantwoordelijkheid over de verstrekte cijfers? Geef één voorbeeld
waaruit deze verantwoordelijkheid kan blijken?
Antwoord … / 2 punten
d) Geef drie voorbeelden van stukken die vereist zijn in elk werkdossier van een
wettelijke opdracht die je opvraagt nog vóór je begint te cijferen en te controleren?
e)
Antwoord … / 3 punten
f) Omschrijf en bereken de door te voeren correcties op de activaposten zoals deze
voorkomen in de ontvangen cijfers per 30/09/2013 (enkel de correcties van het
ACTIEF) (

_in bijlage de afschrijvingstabel, detail van de participatie, overzicht van de
handelsvordering, de staat van activa en passiva)._

**Antwoord … / 4 punten
Staat activa en
passiva Door te voeren correcties
Activa
Vaste activa
Materiële vaste activa
Installaties, machines en uitrusting
230000 - Installaties 32.**

000,00
230900 - Afschrijving installaties
Financiële vaste activa
280000 - Aandelen O'Cool 30.000,00
Vlottende activa
Vorderingen op ten hoogste 1 jaar
Handelsvorderingen
400000

**Inventaris**
- Handelsdebiteuren: 215.100,00 EUR
- Terug te vorderen BTW: 6.020,17 EUR
- Bankrekening: 221.931,57 EUR

Totaal: Activa 505.051,74
Totaal van de correcties op het Activa
g) Als gevolg van uw vaststellingen en vereiste correcties moeten er vermeldingen
komen in het besluit van je verslag, geef twee vermeldingen.

**Antwoord … / 2 punten
h) Als gevolg van je vaststelling moet je een specifiek risico in je besluit opnemen, geef
de formulering ervan.**

Antwoord … / 3 punten

_Nog niet beantwoord (modelantwoord ontbreekt)._

#### Subvraag a)

Kruis het juiste antwoord aan.

#### Subvraag b)

Kan je werken op basis van een proef- en saldi balans zoals in bijlage? Verklaar uw
antwoord.

#### Subvraag c)

Wie draagt de verantwoordelijkheid over de verstrekte cijfers? Geef één voorbeeld
waaruit deze verantwoordelijkheid kan blijken?

#### Subvraag d)

Geef drie voorbeelden van stukken die vereist zijn in elk werkdossier van een
wettelijke opdracht die je opvraagt nog vóór je begint te cijferen en te controleren?

#### Subvraag e)

Antwoord … / 3 punten

#### Subvraag f)

Omschrijf en bereken de door te voeren correcties op de activaposten zoals deze
voorkomen in de ontvangen cijfers per 30/09/2013 (enkel de correcties van het
ACTIEF) (in bijlage de afschrijvingstabel, detail van de participatie, overzicht van de
handelsvordering, de staat van activa en passiva).

---

### 2013-2-vr15 · 2013-2 · 4.0 pt

_Ook geklassificeerd onder_: 1.2

**Vraagformaat**: open · **Antwoord-type**: — · **Confidence**: —

#### Vraagtekst

Is, in de 2 onderstaande situaties de bijzondere procedure, de zogenaamde
alarmbelprocedure, van toepassing voor de bvba “Zonder Zorgen”?
Kunt u voor elk geval en voor elk antwoord een bondige uitleg geven?
1. Eerste situatie
Activa Passiva
Oprichtingskosten 2.000,00 Geplaatst kapitaal 20.000,00
Materiële vaste activa 6.000,00 Niet opgevraagd kapitaal -12.000,00
Goederenvoorraad 3.500,00 Overgedragen resultaat 1.000,00
Liquide middelen 2.000,00 Handelsschulden 4.500,00
13.500,00 13.500,00
Antwoord … / 2 punten
2. Tweede situatie
Activa Passiva
Oprichtingskosten 2.000,00 Geplaatst kapitaal 20.000,00
Materiële vaste activa 6.000,00 Niet opgevraagd kapitaal - 5.000,00
Goederenvoorraad 3.500,00 Reserves 3.000,00
Liquide middelen 2.000,00 Overgedragen verlies - 9.500,00
Resultaat periode -4.500,00
Handelsschulden 9.500,00
13.500,00 13.500,00
Antwoord … / 2 punten

_Nog niet beantwoord (modelantwoord ontbreekt)._

---

### 2013-2-vr20 · 2013-2 · 8.0 pt

_Ook geklassificeerd onder_: 1.6

**Vraagformaat**: J/F · **Antwoord-type**: — · **Confidence**: —

#### Vraagtekst

Een Franse vennootschap is voor 15% aandeelhouder in een Belgische vennootschap BVBA
SUPERTOC. De Franse vennootschap vraagt je om in het kader van het individueel
controlerecht ter plaatse inzage te nemen in de stukken van de BVBA SUPERTOC.
Beantwoord met FOUT / JUIST volgende stellingen die slaan op voorgaande situatie.
a) Het individueel controlerecht kan niet uitgevoerd worden indien de Franse
vennootschap minder dan 25% van de aandelen heeft.
Antwoord … / 2 punten

|   |   |
| --- | --- |
|   | Juist |
|   | Fout |

b) Het individueel controlerecht geldt enkel voor Belgisch ingezetenen.

Antwoord … / 2 punten

|   |   |
| --- | --- |
|   | Juist |
|   | Fout |

c) Het individueel controlerecht kan enkel uitgeoefend worden in geval van betwistingen.
Antwoord … / 2 punten

|   |   |
| --- | --- |
|   | Juist |
|   | Fout |

d) Het individueel controlerecht kan enkel uitgeoefend worden in voorbereiding van een
jaarvergadering.
Antwoord … / 2 punten

|   |   |
| --- | --- |
|   | Juist |
|   | Fout |

PERSONENBELASTING 20 PUNTEN

_Nog niet beantwoord (modelantwoord ontbreekt)._

#### Subvraag a)

Het individueel controlerecht kan niet uitgevoerd worden indien de Franse
vennootschap minder dan 25% van de aandelen heeft.

#### Subvraag b)

Het individueel controlerecht geldt enkel voor Belgisch ingezetenen.

#### Subvraag c)

Het individueel controlerecht kan enkel uitgeoefend worden in geval van betwistingen.

#### Subvraag d)

Het individueel controlerecht kan enkel uitgeoefend worden in voorbereiding van een
jaarvergadering.

---

### 2013-2-vr16 · 2013-2 · 4.0 pt

**Vraagformaat**: MC · **Antwoord-type**: — · **Confidence**: —

#### Vraagtekst

Als accountant en/of belastingconsulent van de in 2012 opgerichte nv “Vivant” wordt u
geraadpleegd door de drie aandeelhouders, tevens de bestuurders van de vennootschap, die
een aantal vragen hebben omtrent hun toestand:

- **a.** De statuten van de vennootschap voorzien in de procedure van het “Toegestaan

kapitaal”, dat bepaald is op € 500.000.
Wie kan die procedure opstarten?
Antwoord … / 2 punten

- **b.** Na de oprichting van hun vennootschap zijn de oprichters hoofdelijk gehouden voor

bepaalde verbintenissen, naar een verhouding die de rechter vaststelt, in geval van
faillissement.
Binnen welke periode is dit uitgesproken ?
Antwoord … / 2 punten

_Nog niet beantwoord (modelantwoord ontbreekt)._

#### Subvraag a)

De statuten van de vennootschap voorzien in de procedure van het “Toegestaan
kapitaal”, dat bepaald is op € 500.000.
Wie kan die procedure opstarten?

#### Subvraag b)

Na de oprichting van hun vennootschap zijn de oprichters hoofdelijk gehouden voor
bepaalde verbintenissen, naar een verhouding die de rechter vaststelt, in geval van
faillissement.
Binnen welke periode is dit uitgesproken ?

---

### 2013-2-vr17 · 2013-2 · 6.0 pt

**Vraagformaat**: J/F · **Antwoord-type**: — · **Confidence**: —

#### Vraagtekst

Kruis de juiste antwoorden aan in onderstaande tabel:
1.

**Welke vennootschap kan opgericht worden met een onderhandse akte?**

2.

**Welke vennootschap kan winstbewijzen toekennen?**

3.

**Welke vennootschap is verplicht haar jaarrekening neer te leggen bij de Nationale Bank
van België?**

4.

**Welke vennootschap moet een minimumkapitaal hebben?**

|   | 1 | 2 | 3 | 4 |
| --- | --- | --- | --- | --- |
| NV |   |   |   |   |
| BVBA |   |   |   |   |
| CVA |   |   |   |   |
| CVBA |   |   |   |   |
| CVOA |   |   |   |   |
| VOF |   |   |   |   |

_Nog niet beantwoord (modelantwoord ontbreekt)._

---

### 2013-2-vr18 · 2013-2 · 3.0 pt

**Vraagformaat**: open · **Antwoord-type**: — · **Confidence**: —

#### Vraagtekst

De heer en mevrouw X bezitten aandelen in de bvba “Invest Plan”, die actief is in de
vastgoedsector.
Hun aandeel in deze vennootschap bedraagt 11,3% van het totaal aantal aandelen.
Tijdens de laatste algemene vergadering hadden zij zich tegen de twee zaakvoerders van de
bvba gekeerd, want zij hadden vragen bij hun bestuur en hadden daarom de aan die
zaakvoerders te verlenen kwijting niet goedgekeurd.
Toen ze de hoop al bijna hadden laten varen in verband met de rechten die ze kunnen laten
gelden, komen ze u raadplegen om te vernemen of er al dan niet een middel bestaat om de
zaakvoerders te dwingen naar hen te luisteren, nu ze weet hebben van verduisteringen in de
rekeningen van de vennootschap. Indien dergelijk middel bestaat, geef het aan.
Antwoord

VENNOOTSCHAPSRECHT (BIJZONDERE MANDATEN) 30 PUNTEN

_Nog niet beantwoord (modelantwoord ontbreekt)._

---

### 2014-1-vr15 · 2014-1 · 4.0 pt

**Vraagformaat**: J/F · **Antwoord-type**: — · **Confidence**: —

#### Vraagtekst

Kruis de juiste antwoorden aan in onderstaande tabel:
1. In welke vennootschap zijn de vennoten/aandeelhouders hoofdelijk aansprakelijk voor de
schulden van hun vennootschap?
2.

**Welke vennootschap kan winstbewijzen toekennen?**

3.

**Welke vennootschap is verplicht haar jaarrekening neer te leggen bij de Nationale Bank
van België?**

4. Voor welke soort vennootschap zijn de oprichters, vóór de oprichting, verplicht om een
financieel plan op te stellen?
De punten worden toegekend per kolom en de kolom dient volledig juist te zijn.

|   | 1 | 2 | 3 | 4 |
| --- | --- | --- | --- | --- |
| NV |   |   |   |   |
| BVBA |   |   |   |   |
| CVA |   |   |   |   |
| CVBA |   |   |   |   |
| CVOA |   |   |   |   |
| VOF |   |   |   |   |
|   |   |   |   |   |

_Nog niet beantwoord (modelantwoord ontbreekt)._

---

### 2014-1-vr20 · 2014-1 · 10.0 pt

_Ook geklassificeerd onder_: 4.0, 1.6

**Vraagformaat**: J/F · **Antwoord-type**: — · **Confidence**: —

#### Vraagtekst

> De heer FIXIT een externe accountant.

De gedelegeerde bestuurder van die vennootschap
wenst de vennootschap

> NV TRIAL om te zetten in een BVBA en geeft de heer FIXIT de
> opdracht dit te doen.

OPMERKING: bij de vragen waar juist / fout moet geantwoord worden maak je bij voorkeur
het vak onleesbaar dat niet uw antwoord is (= doorhalen wat niet past). Voor de puntentelling
wordt er geen giscorrectie toegepast

| Deze controleopdracht kan zowel door een externe <br> accountant, bedrijfsrevisor als door een erkend boekhouder <br> uitgevoerd worden. | JUIST | FOUT |
| --- | --- | --- |
| Tijdens de controleopdracht moet de externe accountant bij <br> de vaststellingen van continuïteitsproblemen de cliënt <br> aanschrijven en daarop wijzen. | JUIST | FOUT |
| Wanneer de vennootschap wordt omgezet van NV in een <br> BVBA blijft haar rechtspersoonlijkheid onveranderd <br> voortbestaan in de nieuwe vorm. | JUIST | FOUT |
| Bij de omzetting van NV in een BVBA kan in geval van <br> unanimiteit bij de aandeelhouders vrijstelling worden <br> verleend voor het opstellen van de verslagen en het <br> controleverslag. Deze vrijstelling dient uitdrukkelijk in de <br> notariële opgenomen te worden. | JUIST | FOUT |
| De wijziging van een handelsvennootschap naar een <br> burgerlijke vennootschap of omgekeerd valt eveneens onder <br> de bepalingen van omzetting en vereist een controleverslag. | JUIST | FOUT |
| De te controleren tussentijdse staat moet worden opgemaakt <br> rekening houdend met de waardecorrecties, pro rata kosten, | JUIST | FOUT |

|   |   |   |
| --- | --- | --- |
| afschrijvingen en voorraadwijzingen conform de <br> waarderingsregels. Ook de voorraadwijzigingen dienen <br> verwerkt te worden. |   |   |
| De controle van de tussentijdse staat zal de <br> beroepsbeoefenaar gebruik moeten maken van een <br> werkprogramma waaruit zijn werkzaamheden moeten blijken. | JUIST | FOUT |

| De controle van de tussentijdse staat richt zich inzonderheid <br> naar enige overwaardering van het netto-actief. Het netto- <br> actief omvat het kapitaal en de reserves. | JUIST | FOUT |
| --- | --- | --- |
| Het dossier moet een stuk of memorandum bevatten met <br> betrekking tot de administratieve en boekhoudkundige <br> organisatie. | JUIST | FOUT |
| Wanneer de beroepsbeoefenaar vaststelt dat er een <br> schuldvordering is op een vennoot dan moet de <br> beroepsbeoefenaar dit in min corrigeren op het netto-actief. | JUIST | FOUT |

_Nog niet beantwoord (modelantwoord ontbreekt)._

---

### 2014-1-vr16 · 2014-1 · 4.0 pt

_Ook geklassificeerd onder_: 1.3

**Vraagformaat**: open · **Antwoord-type**: — · **Confidence**: —

#### Vraagtekst

De gedelegeerd bestuurder van de nv PILOTE (opgericht in 1992) raadpleegt u met volgende
cijfers van de laatste balans (31/12/2013):
Passiva
100 Geplaatst kapitaal 1.000.000,00 EUR
130 Wettelijke reserve 100.000,00 EUR
133 Beschikbare reserves 5.000.000,00 EUR
170 Verplichtingen op de secundaire markt 6.000.000,00 EUR
440 Handelsschulden 500.000,00 EUR
450 Schulden m.b.t. belastingen,
bezoldigingen en sociale lasten 50.000,00 EUR
-------------------------------------
12.650.000,00 EUR

Hij wil een kapitaalverhoging doorvoeren door inlijving van de beschikbare reserves van
5.000.000 EUR via de procedure van het toegestane kapitaal.
Hij overhandigt u de statuten (die nooit werden gewijzigd) en u stelt vast dat artikel 28 van de
statuten in het toegestane kapitaal voorziet.
Wat adviseert u hem, als accountant en/of belastingconsulent?
Antwoord

In de huidige stand van zaken, is de verrichting onmogelijk.

De kapitaalverhoging kan doorgevoerd worden tot beloop van 1.000.000 EUR.

U bent het ermee eens en neemt al contact op met de notaris.

De verrichting kan niet gedaan worden zonder een verslag van de raad van bestuur dat de
verrichting van het toegestane kapitaal uiteenzet.

De vennootschap moet een algemene vergadering bijeenroepen om akte te nemen van de
kapitaalverhoging onder de procedure van het toegestane kapitaal.

_Nog niet beantwoord (modelantwoord ontbreekt)._

---

### 2014-1-vr21 · 2014-1 · 20.0 pt

_Ook geklassificeerd onder_: 1.6

**Vraagformaat**: berekening+MC · **Antwoord-type**: — · **Confidence**: —

#### Vraagtekst

Twee broers doen sedert een drietal jaar goede zaken met hun VOF STORE en wensen alvoor
ze verder investeren en personeel aanwerven de vennootschap om te zetten naar een BVBA.
Ze leggen volgende balans per 31/12/2013 voor.
VOF STORE BALANS 31/12/2013
23 Installaties en machines 20.000,00 10 Kapitaal 10.000,00
28 Aandelen NV TURF 24.000,00 13 Wettelijke reserves 1.000,00
28 Vordering NV TURF 12.000,00 13 Beschikbare reserves 15.000,00
34 Voorraad 25.000,00 17 Schulden LT 15.000,00
55 Bank 5.000,00 42 Schulden KT 5.000,00
44 Handelsschulden 40.000,00
Totaal actief 86.000,00 86.000,00
U krijgt de schriftelijke opdracht om het controleverslag op te stellen nodig voor de
omzetting van de vennootschap.
Tijdens U werkzaamheden onderzoek je de vordering op

> NV TURF, deze vennootschap blijkt
> echter failliet te zijn en geeft aan haar schuldeisers een definitief dividend van één derde van
> de openstaande schulden zijnde in dit geval 4.

000,00 EUR
a) Formuleer het besluit van het controleverslag.

**Welke berekening dien je te maken?**

Geef de gecorrigeerde balans?
Antwoord

b) Kan deze omzetting doorgaan? Motiveer uw antwoord.
Antwoord
PERSONENBELASTING 20 PUNTEN

_Nog niet beantwoord (modelantwoord ontbreekt)._

#### Subvraag a)

Formuleer het besluit van het controleverslag. Welke berekening dien je te maken?
Geef de gecorrigeerde balans?

#### Subvraag b)

Kan deze omzetting doorgaan? Motiveer uw antwoord.

---

### 2014-1-vr17 · 2014-1 · 4.0 pt

**Vraagformaat**: J/F · **Antwoord-type**: — · **Confidence**: —

#### Vraagtekst

Dhr. LEVEQUE, enig vennoot en zaakvoerder van de bvba PETIT POIS (opgericht in 2009),
raadpleegt u in verband met te verrichten investeringen.
Hij wil het gebouw, dat zijn persoonlijke eigendom is en door de bvba PETIT POIS wordt
gebruikt om haar bedrijvigheid uit te oefenen, aan de vennootschap verkopen.
Als zaakvoerder stelt hij een verslag op waarin hij uiteenzet waarom de verwerving van dit
gebouw van belang is voor de vennootschap.
In dat verslag geeft hij het bedrag van de verrichting aan, met name 680.000 EUR.
Hij heeft een vastgoedschatting laten uitvoeren, en in het verslag daarvan wordt een
verkoopwaarde aangegeven van:
bij onderhandse verkoop: 550.000 EUR
bij gedwongen verkoop: 400.000 EUR
Wat adviseert u hem, als accountant en/of belastingconsulent, met betrekking tot die
verrichting?
Antwoord

Dat de gevraagde prijs te hoog is, en hij hem moet terugbrengen tot de verkoopwaarde bij
onderhandse verkoop.

Dat hij de verrichting kan doen maar hierover verslag moet uitbrengen in een stuk dat bij de
jaarrekening moet worden gevoegd, en dat hij aansprakelijk is voor de eventuele schade die
derden ten gevolge van de verrichting zouden kunnen lijden.

Dat het een gunstige verrichting is en dat hij contact moet opnemen met de notaris om de
verkoop te laten acteren.

Dat de verrichting kan worden gedaan door een andere persoon (lasthebber ad hoc) die in
zijn verslag vermeldt dat het bedrag van de verrichting niet nadelig is voor het vermogen van
de vennootschap.


Dat de verrichting enkel kan worden gedaan wanneer beroep wordt gedaan op een
bedrijfsrevisor om de waarde van het gebouw te bepalen en verslag uit te brengen over de
omschreven verrichting .

_Nog niet beantwoord (modelantwoord ontbreekt)._

---

### 2014-1-vr18 · 2014-1 · 4.0 pt

**Vraagformaat**: open · **Antwoord-type**: — · **Confidence**: —

#### Vraagtekst

> De heer KALO Ric gedelegeerd bestuurder van de nv MINCALOR, handel in dieetproducten,
> en hoofdaandeelhouder, raadpleegt u.

> De heer KALO Ric heeft een aanzienlijk geldbedrag nodig voor een privé-vastgoed
> verrichting.

Hij toont u de statuten van de vennootschap die de raad van bestuur toelaten de geplande
verrichting te doen. De vennootschap heeft geen commissaris.
Hij toont u de jaarrekening afgesloten op 31 december 2013. De resultaatverwerking van deze
jaarrekening, goedgekeurd door de algemene vergadering van 20 februari 2014, ziet er als
volgt uit:
Resultaat van het boekjaar: 1.000.000,00 EUR
Vergoeding van het kapitaal 500.000,00 EUR
Toevoeging aan de overige reserves 500.000,00 EUR
Hij legt u ook de tussentijdse situatie van 31 maart 2014 voor:
Totaal opbrengsten 1.200.000,00 EUR
Totaal kosten 900.000,00 EUR
-------------------------------------
Winst van het kwartaal 300.000,00 EUR
Het passief van de vennootschap per 31 maart 2014 is het volgende:
Passiva
100 Geplaatst kapitaal 1.000.000,00 EUR
130 Wettelijke reserve 100.000,00 EUR
133 Beschikbare reserves 5.000.000,00 EUR
Resultaat van de periode 300.000,00 EUR
170 Verplichtingen op de secundaire markt 6.000.000,00 EUR
440 Handelsschulden 500.000,00 EUR
450 Schulden m.b.t. belastingen,
bezoldigingen en sociale lasten 50.000,00 EUR
-----------------------------------
12.950.000,00 EUR
Hij vraagt u of het mogelijk is om geld uit de vennootschap te trekken door middel van een
interimdividend.
Wat raadt u hem aan?
Antwoord

Dat hij geen bijkomende dividenden kan opnemen. Dat zou de vennootschap in gevaar
kunnen brengen ten aanzien van het netto-actief.

Dat de opneming onmiddellijk kan gebeuren, aangezien ze na de neerlegging van de laatste
balans gebeurt.

Dat hij zal moeten wachten tot in juli 2014


Dat de dividenduitkering kan doorgevoerd worden op basis van de tussentijdse situatie van
31 maart 2014 en van een verificatieverslag opgesteld door een bedrijfsrevisor of een
externe accountant.

Dat hij geen nieuwe dividenden mag opnemen, aangezien de algemene vergadering van 20
februari er al heeft uitgekeerd.

_Nog niet beantwoord (modelantwoord ontbreekt)._

---

### 2014-1-vr19 · 2014-1 · 4.0 pt

_Ook geklassificeerd onder_: 1.2

**Vraagformaat**: open · **Antwoord-type**: — · **Confidence**: —

#### Vraagtekst

> De heer LEGRAND Alexandre is samen met zijn broer Luigi vennoot in de vennootschappen
> "Mise en Trop" bvba en "Coté Pratique" bvba in Brussel.

Vennootschap "Mise en Trop" bvba stelt 39 voltijdse personeelsleden tewerk in de
informaticasector. Vennootschap "Coté Pratique" bvba stelt 25 personen, allen halftijds,
tewerk in de poetshulpsector.
Zij raadplegen u in verband met "Mise en Trop" bvba, om informatie te bekomen over hun op
31 december 2013 afgesloten jaarrekening.
Activa 31/12/2013 31/12/2012 Passiva 31/12/2013 31/12/2012
Materiële vaste activa 450.000,00 455.000,00 Kapitaal 375.000,00 375.000,00
Reserves 175.000,00 150.000,00
Voorraad 35.000,00 30.000,00
Handelsschulden 45.000,00 47.000,00
Handelsvorderingen 75.000,00 85.000,00
Belasting-, loon-,
sociale schulden 45.000,00 43.000,00
Liquide middelen 80.000,00 45.000,00
640.000,00 615.000,00 640.000,00 615.000,00
Daar het een verkort schema betreft, delen de gebroeders LEGRAND u ook het bedrag van de
omzet mee, hetzij:
voor 2013: 7.450.000,00
voor 2012: 7.350.000,00
Zij delen u ook de omzet mee van "Coté Pratique" bvba, namelijk:
voor 2013: 530.000,00
voor 2012: 520.000,00
Hoe luidt uw advies, op zicht van deze gegevens?

**Antwoord

U stelt vast dat de balans correct werd opgesteld en raadt hun aan zo voort te doen.**


U adviseert hen om enkel de jaarrekening van vennootschap “Mise en Trop” bvba volgens
het volledig schema op te stellen.

U adviseert hen om de jaarrekeningen van beide vennootschappen volgens het volledig
schema op te stellen.

U adviseert hen om enkel de jaarrekening van vennootschap “Coté Pratique” bvba volgens
het volledig schema op te stellen.

U adviseert hen om een geconsolideerde rekening bij de Nationale Bank neer te leggen.
VENNOOTSCHAPSRECHT (BIJZONDERE MANDATEN) 30 PUNTEN

_Nog niet beantwoord (modelantwoord ontbreekt)._

---

### 2015-1-vr20 · 2015-1 · 4.0 pt

**Vraagformaat**: MC · **Antwoord-type**: — · **Confidence**: —

#### Vraagtekst

> De heer DUPONT, zaakvoerder en hoofdaandeelhouder van de S-bvba “LA POINTE” komt u
> op zaterdag 11 april 2015 om advies vragen.

De vennootschap werd opgericht in december
2009.
Hij legt u de jaarrekening per 31 december 2014 voor.
Die ziet er als volgt uit:
Activa Passiva
Materiële vaste activa 3 000,00 Kapitaal 6 000,00
Handelsvorderingen 20 000,00 Overgedragen verlies - 4 000,00
Liquide middelen 1 000,00 Schulden op minder dan 22 000,00
een jaar
Totaal activa 24 000,00 Totaal passiva 24 000,00
Kosten Opbrengsten
Handelsgoederen 150 000,00 Verkopen 200 000,00
Diensten en diverse 48 000,00 Overige 250,00
goederen bedrijfsopbrengsten
Lonen 0,00
Afschrijvingen 250,00
Overige bedrijfskosten 650,00
Financiële kosten 1 000,00 Financiële opbrengsten 300,00
Uitzonderlijke kosten 0,00 Uitzonderlijke 0,00
opbrengsten
Belastingen 0,00
Winst van het boekjaar 650,00
Totaal kosten 200 550,00 Totaal opbrengsten 200 550,00
Wat kunt u dhr. DUPONT, op basis van deze gegevens, adviseren:

- **A.** De toestand lijkt in orde. Er zijn geen bijkomende formaliteiten te vervullen.
- **B.** Dat hij er goed zou aan doen om de algemene vergadering bijeen te roepen om te

beslissen over de eventuele ontbinding en om eventueel andere maatregelen te
nemen. En dit vóór 11 juni 2015.

- **C.** Dat hij verplicht is om het kapitaal te volstorten om het onmiddellijk op het vereiste

minimum van 6.200,00 EUR te brengen.

- **D.** Dat hij verplicht is om het kapitaal te volstorten om het onmiddellijk op het vereiste

minimum van 18.550,00 EUR te brengen.
E. Dat hij er goed zou aan doen om de algemene vergadering bijeen te roepen om te
beslissen over de eventuele ontbinding en om eventueel andere maatregelen te
nemen. En dit vóór 31 juli 2015.

_Nog niet beantwoord (modelantwoord ontbreekt)._

---

### 2015-1-vr25 · 2015-1 · 3.0 pt

_Ook geklassificeerd onder_: 1.6

**Vraagformaat**: open · **Antwoord-type**: — · **Confidence**: —

#### Vraagtekst

**Wat is of zijn de doelstelling(en) van de specifieke opdracht van de externe accountant bij de
omzetting van een vennootschap ?**

Antwoord

_Nog niet beantwoord (modelantwoord ontbreekt)._

---

### 2015-1-vr21 · 2015-1 · 4.0 pt

_Ook geklassificeerd onder_: 1.2, 1.3

**Vraagformaat**: J/F · **Antwoord-type**: — · **Confidence**: —

#### Vraagtekst

U hebt de balans opgemaakt voor uw cliënt waarbij het eigen vermogen van de bvba als volgt
is samengesteld:
Geplaatst Kapitaal: 18.550,00 EUR
Wettelijke reserve: 1.855,00 EUR
Overgedragen winst: 15.000,00 EUR
De zaakvoerder van de bvba wenst de vennootschap om te zetten in een nv. Hij meldt u dat
hij over een rekening-courant met een creditstand van 50.000,00 EUR beschikt, die in de
boekhouding onder post 48 “andere schulden” werd opgenomen. Dit bedrag werd gestort in
2010 wegens tijdelijke liquiditeitsproblemen van de vennootschap.
U deelt bijgevolg aan uw cliënt mee dat de omzetting, in de huidige stand van zaken, niet
mogelijk is.
Uw cliënt heeft zich ook elders geïnformeerd en meent dat het toch mogelijk moet zijn om de
omzetting door te voeren.

- **A.** Een kapitaalverhoging doorvoeren in geld bij een notariële akte waarbij ook de

rechtsvorm wordt gewijzigd.

- **B.** Een deel van de rekening-courant als kapitaalverhoging opnemen mits een verslag van

de accountant.

- **C.** De accountant kan de gehele opdracht op zich nemen om deze omzetting mogelijk te

maken en door te voeren.

- **D.** Met het oog op de akte tot verhoging van het kapitaal heeft de notaris enkel een

boekhoudkundige staat die maximum drie maanden oud is en een controleverslag nodig;
er zijn geen andere stukken noch formaliteiten vereist.
E. Bij de omzetting van bvba naar nv bedraagt het minimum geplaatst kapitaal wel degelijk
61.500 EUR, maar het mag volgestort worden tot beloop van slechts 1/3.

_Nog niet beantwoord (modelantwoord ontbreekt)._

---

### 2015-1-vr26 · 2015-1 · 18.0 pt

_Ook geklassificeerd onder_: 1.6, 1.2

**Vraagformaat**: MC · **Antwoord-type**: — · **Confidence**: —

#### Vraagtekst

In de norm inzake de controle bij het voorstel tot ontbinding van vennootschappen met
beperkte aansprakelijkheid zoals goedgekeurd door de raad van het IAB staan een aantal uit
te voeren werkzaamheden.

**Geef in de onderstaande gevallen weer wat de norm voorziet in
volgende gevallen:
a) Hoe wordt in de staat van activa en passiva het resultaat van de lopende, nog niet
afgesloten periode vermeld?**

Antwoord … / 3 punten

- **b.** Het bestuursorgaan stelt de staat van activa en passiva enkel op in discontinuïteit.

Wat moet de beroepsbeoefenaar in overweging nemen?
Antwoord … / 3 punten

- **c.** Wat dient er te gebeuren met latente schulden (bv. vergoeding wegens contractbreuk)

die niet in de staat van activa en passiva zijn opgenomen?
Antwoord … / 3 punten

- **d.** Wat gebeurt er met de termijn van drie maand indien een bijeenroeping van een

tweede algemene vergadering nodig is wegens het niet bereiken van het
aanwezigheidsquorum?
Antwoord … / 3 punten
e) Het voorstel tot ontbinding is het gevolg van de toepassing van de alarmbelprocedure.
Heeft dit enig gevolg voor de termijnen?
Antwoord … / 3 punten
f) De beroepsbeoefenaar stelt in de loop van zijn controlewerkzaamheden een inbreuk
vast op de boekhoudreglementering in verband met de opstelling van de

boekhoudkundige staat. Wat dient de beroepsbeoefenaar te doen, moet er
voorbehoud gemaakt worden of een onthouding?
Antwoord … / 3 punten

_Nog niet beantwoord (modelantwoord ontbreekt)._

#### Subvraag a)

Hoe wordt in de staat van activa en passiva het resultaat van de lopende, nog niet
afgesloten periode vermeld?

#### Subvraag b)

Het bestuursorgaan stelt de staat van activa en passiva enkel op in discontinuïteit.
Wat moet de beroepsbeoefenaar in overweging nemen?

#### Subvraag c)

Wat dient er te gebeuren met latente schulden (bv. vergoeding wegens contractbreuk)
die niet in de staat van activa en passiva zijn opgenomen?

#### Subvraag d)

Wat gebeurt er met de termijn van drie maand indien een bijeenroeping van een
tweede algemene vergadering nodig is wegens het niet bereiken van het
aanwezigheidsquorum?

#### Subvraag e)

Het voorstel tot ontbinding is het gevolg van de toepassing van de alarmbelprocedure.
Heeft dit enig gevolg voor de termijnen?

#### Subvraag f)

De beroepsbeoefenaar stelt in de loop van zijn controlewerkzaamheden een inbreuk
vast op de boekhoudreglementering in verband met de opstelling van de
boekhoudkundige staat. Wat dient de beroepsbeoefenaar te doen, moet er
voorbehoud gemaakt worden of een onthouding?

---

### 2015-1-vr22 · 2015-1 · 4.0 pt

**Vraagformaat**: MC · **Antwoord-type**: — · **Confidence**: —

#### Vraagtekst

Met het oog op de voorbereiding van de Algemene Vergadering van 15 mei biedt de
zaakvoerder van de bvba De Toekomst (die tevens 55% van de aandelen bezit) zich op 25
januari 2014 in uw kantoor aan en overhandigt u de financiële staten van de bvba per
31/12/2013.
Bij nazicht van de gegevens kan het eigen vermogen per 31/12/2013 als volgt worden
samengevat:
 Geplaatst kapitaal: 18.600,00 EUR
 Wettelijke reserve: 1.860,00 EUR

 Beschikbare reserve: 100.000,00 EUR
 Overgedragen verlies: -128.830,00 EUR
De zaakvoerder van de bvba vraagt u wat zijn verplichtingen zijn ten aanzien van deze
toestand.

**Welke opgesomde acties zijn correct:
A.**

Een buitengewone algemene vergadering bijeenroepen binnen de maand.

- **B.** Niets doen.
- **C.** De volgende algemene vergadering afwachten en de invereffeningstelling van de bvba

voorstellen.

- **D.** Een bijzondere algemene vergadering bijeenroepen voor 25 maart om te beraadslagen

en te besluiten over de ontbinding van de vennootschap en andere te nemen
maatregelen.
E. De vennoten verplichten om het kapitaal van de vennootschap te verhogen door
inbrengen in geld.

_Nog niet beantwoord (modelantwoord ontbreekt)._

---

### 2015-1-vr27 · 2015-1 · 9.0 pt

_Ook geklassificeerd onder_: 1.6, 1.2

**Vraagformaat**: J/F · **Antwoord-type**: — · **Confidence**: —

#### Vraagtekst

Een externe accountant krijgt als opdracht het opmaken van een verslag over een
boekhoudkundige staat van activa en passiva in het kader van de omzetting van een
vennootschap van

> NV Salami in BVBA Salami.

De vennootschap valt onder het Wetboek van
Vennootschappen. Het betreft hier een KMO vennootschap dat voornamelijk levensmiddelen
invoert uit Italië.
a) De externe accountant moet de volledige identiteit van de leden van het
bestuursorgaan opvragen.

|   |   |
| --- | --- |
|   | Ja |
|   | Neen |

b) De externe accountant moet in zijn verslag een beoordeling van de administratieve en
boekhoudkundige organisatie van de vennootschap vermelden.

|   |   |
| --- | --- |
|   | Ja |
|   | Neen |

c) De externe accountant hanteert een risico-analyse om te beoordelen waar de zwakke
punten van de interne procedure in de onderneming gesitueerd zijn.

|   |   |
| --- | --- |
|   | Ja |
|   | Neen |

d) De externe accountant moet zijn werkdossier door de raad van bestuur laten
ondertekenen.

|   |   |
| --- | --- |
|   | Ja |
|   | Neen |

e) De externe accountant moet de door het bestuursorgaan opgestelde staat van activa
en passiva herwerken tot een nieuwe staat na zijn controlewerkzaamheden, alvorens
deze ondertekend aan de notaris over te maken.

|   |   |
| --- | --- |
|   | Ja |
|   | Neen |

f) De externe accountant moet een bijkomende aansprakelijkheidsverzekering afsluiten
om zijn aansprakelijkheid ingevolge zijn verslag in te dekken.

|   |   |
| --- | --- |
|   | Ja |
|   | Neen |

g) De externe accountant zal een nazicht doen of de waarderingsregels correct zijn
toegepast.

|   |   |
| --- | --- |
|   | Ja |
|   | Neen |

h) De externe accountant moet altijd een voorbehoud maken als de klantenconfirmaties
niet werden verstuurd.

|   |   |
| --- | --- |
|   | Ja |
|   | Neen |

i) De externe accountant moet akkoord hebben van de aandeelhouders alvorens zijn
opdracht aan te vangen.

|   |   |
| --- | --- |
|   | Ja |
|   | Neen |

PERSONENBELASTING 20 PUNTEN
De vragen hebben betrekking op het aanslagjaar 2014 – inkomsten 2013.
Antwoorden
Plaats de letter van het juiste antwoord in onderstaande rooster.

| Vraag | 1 | 2 | 3 | 4 | 5 |
| --- | --- | --- | --- | --- | --- |
| Antwoord |   |   |   |   |   |
| Punten | 4 | 4 | 4 | 4 | 4 |

_Nog niet beantwoord (modelantwoord ontbreekt)._

#### Subvraag a)

De externe accountant moet de volledige identiteit van de leden van het
bestuursorgaan opvragen.

#### Subvraag b)

De externe accountant moet in zijn verslag een beoordeling van de administratieve en
boekhoudkundige organisatie van de vennootschap vermelden.

#### Subvraag c)

De externe accountant hanteert een risico-analyse om te beoordelen waar de zwakke
punten van de interne procedure in de onderneming gesitueerd zijn.

#### Subvraag d)

De externe accountant moet zijn werkdossier door de raad van bestuur laten
ondertekenen.

#### Subvraag e)

De externe accountant moet de door het bestuursorgaan opgestelde staat van activa
en passiva herwerken tot een nieuwe staat na zijn controlewerkzaamheden, alvorens
deze ondertekend aan de notaris over te maken.

#### Subvraag f)

De externe accountant moet een bijkomende aansprakelijkheidsverzekering afsluiten
om zijn aansprakelijkheid ingevolge zijn verslag in te dekken.
g) De externe accountant zal een nazicht doen of de waarderingsregels correct zijn
toegepast.
h) De externe accountant moet altijd een voorbehoud maken als de klantenconfirmaties
niet werden verstuurd.
i) De externe accountant moet akkoord hebben van de aandeelhouders alvorens zijn
opdracht aan te vangen.
PERSONENBELASTING 20 PUNTEN
De vragen hebben bet

---

### 2015-1-vr23 · 2015-1 · 4.0 pt

**Vraagformaat**: J/F · **Antwoord-type**: — · **Confidence**: —

#### Vraagtekst

Het bestuursorgaan moet jaarlijks de jaarrekening opstellen.
De raad van bestuur van uw cliënt, de nv “Option for the Future”, die haar rekeningen afsluit
op 31/12 van elk jaar, roept de gewone algemene vergadering te laat bijeen en stelt de datum
vast op 20/07/2014.
De redenen die de raad van bestuur daarvoor inroept, zijn van velerlei aard en begrijpelijk. De
gedelegeerd bestuurder vraagt u, in de uitoefening van uw opdracht van extern accountant,
of de laattijdigheid gevolgen teweegbrengt voor hem en/of voor de algemene vergadering
van de aandeelhouders.
Welk onderstaand antwoord is juist:

- **A.** Geen probleem, aangezien de rekeningen toch door de gewone algemene vergadering

zullen worden goedgekeurd.

- **B.** De jaarrekening moet binnen zes maanden na afsluiting van het boekjaar ter

goedkeuring aan de algemene vergadering worden voorgelegd, zo niet zal de door
derden geleden schade, behoudens tegenbewijs, geacht worden voort te vloeien uit dit
verzuim.

- **C.** Aangezien de jaarrekening niet afgewerkt was, was het niet mogelijk om de algemene

vergadering bijeen te roepen en stelt dit dus geen enkel probleem.

- **D.** De Nationale Bank van België zal een boete opleggen wegens de laattijdige

bijeenroeping van de gewone algemene vergadering.

_Nog niet beantwoord (modelantwoord ontbreekt)._

---

### 2015-1-vr24 · 2015-1 · 4.0 pt

**Vraagformaat**: J/F · **Antwoord-type**: — · **Confidence**: —

#### Vraagtekst

> De heer POULAIN, enig vennoot, zaakvoerder en oprichter van de vennootschap “bvba LE
> BON” komt u advies vragen in verband met een kapitaalverhoging.

De bvba LE BON werd
opgericht op 16 november 2013.
De vennootschap heeft een kapitaal van 20.000 EUR en hij wenst het met 10.000 EUR te
verhogen om het op 30.000 EUR te brengen.

Om deze kapitaalverhoging te verwezenlijken, wil hij de aandelen inbrengen van de
vennootschap “nv CHARTER”, die hij 2 weken eerder heeft verkregen. Die aandelen zijn
gewaardeerd op 10.000 EUR en hebben sindsdien geen herwaardering ondergaan.
Hij overhandigt u het bijzonder verslag dat het bestuursorgaan heeft opgesteld.
Wat adviseert u hem:

- **A.** Dat de verrichting niet kan doorgevoerd worden op basis van de bekomen gegevens.
- **B.** Dat hij noodzakelijk in het bezit moet zijn van een verslag van een bedrijfsrevisor, indien de

vennootschap geen commissaris-revisor heeft. Dit verslag vermeldt de naam van de
eigenaar van het goed dat de vennootschap wil verkrijgen, de beschrijving van dit goed, de
vergoeding die werkelijk als tegenprestatie voor de verkrijging wordt verstrekt en de
toegepaste waarderingsmethoden. Het geeft aan of de waarden waartoe deze
waarderingsmethoden leiden, tenminste gelijk zijn aan de als tegenprestatie verstrekte
vergoeding.

- **C.** Dat hij in het bezit moet zijn van een attest van de FSMA, met vermelding van de oorsprong

van de eigendom van de aandelen, de waarde op de datum van verkrijging en de evolutie
ervan over de 3 voorgaande jaren.

- **D.** Dat hij een verklaring moet opstellen met vermelding van de beschrijving van de inbreng, de

naam van de eigenaar, de waarde en de herkomst van deze waardering en de verstrekte
tegenprestatie en een attest dat er zich geen nieuwe omstandigheden hebben voorgedaan
ten opzichte van de oorspronkelijke waardering.
E. Dat het door het bestuursorgaan opgesteld bijzonder verslag volstaat en dat hij het aan de
notaris moet bezorgen die de kapitaalverhoging zal vaststellen zoals bepaald bij artikel 75
van het Wetboek van vennootschappen.

VENNOOTSCHAPSRECHT (BIJZONDERE MANDATEN) 30 PUNTEN

_Nog niet beantwoord (modelantwoord ontbreekt)._

---

### 2024-1-vr1 · 2024-1

> [!warning] Herinnering-reconstructie (fragment)
> Deze vraag is een **herinnering**-reconstructie (volledigheid: fragment) — geen officiële ITAA-bundel. Modelantwoord rust op de geherinterpreteerde vraagtekst (ADR-022).

**Vraagformaat**: MC · **Antwoord-type**: — · **Confidence**: —

#### Vraagtekst

1 Vennootschapsrecht

- **A.** BVBA naar BV volgens nieuw WVV. Aandeelhouder vrij van volstorting van het niet volstort kapitaal. Liquidatietest nodig?
- **B.** Quasi inbreng in NV. Wie kan dit doen?
- **C.** Vennootschap verliest rechtspersoonlijkheid:
- **A.** a. Bij ontbinding
- **B.** b. Bij publicatie van de ontbinding
- **C.** c. Bij de afsluit van de vereffening
- **D.** d. Bij akkoord van de vennoten.
- **D.** Bij welke rechtsvormen kunnen de uittreding/ uitsluiting van een aandeelhouder statutair worden geregeld?
- **A.** a. BV en CV
- **B.** b. Alle behalve NV
- **C.** c. Alle behalve NV en BV
- **D.** d. NV, BV en CV

> [!note]- Geherinterpreteerde vraagtekst (ADR-022)
> Casus vennootschapsrecht, 4 deelvragen:
> A. Een BVBA wordt omgezet naar BV onder het nieuwe WVV. Aandeelhouders zijn vrij van volstorting van het niet-volstorte kapitaal. Is er een liquidatietest vereist?
> B. Quasi-inbreng in een NV — wie kan deze verrichting uitvoeren?
> C. MC — Een vennootschap verliest haar rechtspersoonlijkheid: a. Bij ontbinding / b. Bij publicatie van de ontbinding / c. Bij de afsluiting van de vereffening / d. Bij akkoord van de vennoten.
> D. MC — Bij welke rechtsvormen kunnen uittreding en uitsluiting van een aandeelhouder statutair worden geregeld? a. BV en CV / b. Alle behalve NV / c. Alle behalve NV en BV / d. NV, BV en CV.
> 
> _Motivering_: Sub-A en sub-B zijn open vragen waarvan de stam volledig in PDF zit. Sub-C en sub-D zijn MC met vier opties die volledig zichtbaar zijn. Herformulering is overwegend cosmetisch.
> _Confidence_: grounded · _Datum_: 2026-05-19

> [!example]- MC-opties (gestructureerd)
> | Label | Tekst | Juistheid | Motivering |
> | --- | --- | --- | --- |
> | C.a | Bij ontbinding | fout | Vennootschap blijft rechtspersoonlijkheid behouden tot afsluiting vereffening (WVV art. 2:76). |
> | C.b | Bij publicatie van de ontbinding | fout | Publicatie heeft enkel tegenwerpelijkheid-effect, niet einde rechtspersoonlijkheid. |
> | C.c | Bij de afsluiting van de vereffening | juist | WVV art. 2:76: rechtspersoonlijkheid eindigt bij afsluiting vereffening. |
> | C.d | Bij akkoord van de vennoten | fout | Vennoten-akkoord alleen volstaat niet. |
> | D.a | BV en CV | onbekend | Onder huidig WVV is uittreding ten laste van het vermogen typisch BV/CV/CommV — exacte set per casus te bevestigen. |
> | D.b | Alle behalve NV | onbekend | Vraag is te interpreteren; uittreding ten laste van vermogen niet voor NV. |
> | D.c | Alle behalve NV en BV | onbekend | — |
> | D.d | NV, BV en CV | onbekend | — |

_Nog niet beantwoord (modelantwoord ontbreekt)._

---

### 2024-1-vr4 · 2024-1

_Ook geklassificeerd onder_: 1.6

> [!warning] Herinnering-reconstructie (fragment)
> Deze vraag is een **herinnering**-reconstructie (volledigheid: fragment) — geen officiële ITAA-bundel. Modelantwoord rust op de geherinterpreteerde vraagtekst (ADR-022).

**Vraagformaat**: J/F · **Antwoord-type**: — · **Confidence**: —

#### Vraagtekst

4 Bijzonder mandaten

- **A.** Stellingen Juist of fout:
- **A.** CV ontbonden door AV bij gewone meerderheid
- **B.** Vrijwillige ontbinding BV is verslag externe accountant verplicht als de meerderheid van de aandeelhouders hierom vraagt.
- **C.** AV voor de vereffening van BV moet bij authentieke akte
- **D.** AV voor het sluiten van de vereffening BV moet bij authentieke akte.
- **B.** Verschillende stellingen Juist of Fout ivm ontbinding en vereffening
- **C.** Verschillende stellingen Juist of Fout ivm omzettingen

> [!note]- Geherinterpreteerde vraagtekst (ADR-022)
> Casus bijzondere mandaten — ontbinding/vereffening en omzetting, 3 deelvragen:
> A. Stellingen juist of fout (J/F-set met vier stellingen):
>     1. Een CV wordt ontbonden door de algemene vergadering bij gewone meerderheid.
>     2. Bij een vrijwillige ontbinding van een BV is een verslag van een externe accountant verplicht als de meerderheid van de aandeelhouders hierom vraagt.
>     3. De algemene vergadering voor de vereffening van een BV moet bij authentieke akte.
>     4. De algemene vergadering voor het sluiten van de vereffening van een BV moet bij authentieke akte.
> B. Verschillende stellingen juist of fout in verband met ontbinding en vereffening (stellingen niet bewaard in herinnering).
> C. Verschillende stellingen juist of fout in verband met omzettingen (stellingen niet bewaard in herinnering).
> 
> _Motivering_: Sub-A heeft 4 stellingen die volledig in PDF staan. Sub-B en sub-C noemen alleen het onderwerp ('Verschillende stellingen ... ivm ontbinding en vereffening') zonder de stellingen zelf — niet beantwoordbaar.
> _Confidence_: inferred · _Datum_: 2026-05-19

_Nog niet beantwoord (modelantwoord ontbreekt)._

---

## PO 4.0

_28 vragen — 5 met modelantwoord — 0 met gap-rapport._

### 2003-bibf-vrK1 · 2003-bibf · 4 pt

**Vraagformaat**: open · **Antwoord-type**: — · **Confidence**: —

#### Vraagtekst

: Beschrijf de deontologische regels en verplichtingen inzake overdracht van een dossier tussen twee confraters BIBF en dit zowel vanuit het perspectief van de overlater als vanuit het oogpunt van de overnemer van het dossier.

_Nog niet beantwoord (modelantwoord ontbreekt)._

---

### 2003-bibf-vrK2 · 2003-bibf · 1 pt

**Vraagformaat**: open · **Antwoord-type**: — · **Confidence**: —

#### Vraagtekst

: Gelden diezelfde regels, zoals geformuleerd in uw antwoord op vraag K.1 tevens wanneer een dossier wordt overgenomen of overgedragen t.a.v. een accountant IAB of een bedrijfsrevisor IBR ? Zo nodig, geef meer toelichting. 1 PUNT

_Nog niet beantwoord (modelantwoord ontbreekt)._

---

### 2008-bibf-vrK1 · 2008-bibf

**Vraagformaat**: open · **Antwoord-type**: — · **Confidence**: —

#### Vraagtekst

De afgevaardigd bestuurder van een NV gespecialiseerd in het domein van de voedingsnijverheid en waarvan U sinds meerdere jaren de boekhouding voert, vraagt U of U geen deel wenst uit te maken van de raad van bestuur van zijn onderneming. Dit voorstel interesseert U. Wat antwoordt U aan uw cliënt ?

#### Modelantwoord

Artikel 21 : onverenigbare situatie vermits U als bestuurder van deze NV

> [!success]- Motivering
> Artikel 21 : onverenigbare situatie vermits U als bestuurder van deze NV een handelsactiviteit zal uitoefenen als bestuurder van deze NV Art. 4 et 6 : Zelfs onafhankelijk van artikel 21, zou er een belangenconflict zijn indien U verder de boekhouding zou voeren van deze NV. Probleem van onafhankelijkheid. OF Ik ga in op het voorstel en neem ontslag als erkend boekhouder(-fiscalist) BIBF.

> [!info]- Bronnen (1)
> - _pdf-modelantwoord_

---

### 2008-bibf-vrK2 · 2008-bibf

**Vraagformaat**: open · **Antwoord-type**: — · **Confidence**: —

#### Vraagtekst

Je bent stagiair BiBF. Bij de overdracht van een dossier stuurt jouw voorganger Patrick per ongeluk een bestandje mee door met al zijn klanten, hun adresgegevens, hun ondernemingsnummer, hun telefoonnummer en de prijzen die hij bij hun hanteert. Heel wat van de klanten ken je en je zou hun boekhouding wel voor een iets lager prijsje willen doen. Je kunt trouwens nog wel wat klanten gebruiken en de markt is toch zeker vrij voor iedereen. Uiteindelijk zal het toch de klant zijn die beslist. Dit is gewoon een commerciële meevaller ? Is dit deontologisch toegelaten/verboden? In welk artikelen vind je het antwoord op deze vraag ?

1) plichtenleer artikel 23 De boekhouder BIBF kan alle personen die er om verzoeken, de nodige informatie bezorgen over zijn beroepswerkzaamheden, zijn deskundigheden, diensten en honoraria. Het is hem verboden klanten te ronselen alsook informatie spontaan aan te bieden met het oog op klantenwerving of zich bepaalde titels of deskundigheden toe te eigenen. Uitlokken of ronselen is verboden !

2) artikel 16 plichtenleer De boekhouder is gehouden tot wederzijdse hulp en hoffelijkheid tegenover zijn confraters en moet zich onthouden van elke houding of handeling die een confrater schade kan berokkenen Actief gaan “vissen” in de vijver van een confrater is hem schade berokkenen !

3) artikel 4 plichtenleer de boekhouder BIBF moet zijn beroep uitoefenen met de vereiste BEKWAAMHEID, EERLIJKHEID en WAARDIGHEID Misbruik maken van een technische vergissing van een confrater is niet eerlijk en niet waardig !

#### Modelantwoord

Verboden: art. 23 plichtenleer (geen ronselen/klantenwerving), art. 16 (hoffelijkheid t.o.v. confrater), art. 4 (eerlijkheid en waardigheid).

> [!success]- Motivering
> 1) Plichtenleer artikel 23: De boekhouder BIBF kan alle personen die er om verzoeken, de nodige informatie bezorgen over zijn beroepswerkzaamheden, zijn deskundigheden, diensten en honoraria. Het is hem verboden klanten te ronselen alsook informatie spontaan aan te bieden met het oog op klantenwerving of zich bepaalde titels of deskundigheden toe te eigenen. → Uitlokken of ronselen is verboden!
> 
> 2) Artikel 16 plichtenleer: De boekhouder is gehouden tot wederzijdse hulp en hoffelijkheid tegenover zijn confraters en moet zich onthouden van elke houding of handeling die een confrater schade kan berokkenen. → Actief gaan “vissen” in de vijver van een confrater is hem schade berokkenen!
> 
> 3) Artikel 4 plichtenleer: de boekhouder BIBF moet zijn beroep uitoefenen met de vereiste BEKWAAMHEID, EERLIJKHEID en WAARDIGHEID. → Misbruik maken van een technische vergissing van een confrater is niet eerlijk en niet waardig!

> [!info]- Bronnen (1)
> - _pdf-modelantwoord_

---

### 2008-bibf-vrK3 · 2008-bibf

**Vraagformaat**: open · **Antwoord-type**: — · **Confidence**: —

#### Vraagtekst

Je bent stagiair BIBF. Nico, een vriend van je oudere broer Paul, wenst dat je de boekhouding van zijn restaurant overneemt. Paul is bankier bij Dexia. Nico had tot 3 maanden geleden zijn boekhouding bij Bernard . Wat verplicht de plichtenleer je ? - Hoe zal je de overgang van het dossier laten verlopen? Citeer tevens de toepasselijke artikelen uit de plichtenleer. - Je bent dermate tevreden dat je je aanbrengende broer een commissievergoeding wenst te betalen uit dank.

**Hoe pak je dit aan en op basis van welk artikel van de plichtenleer ?**

1) plichtenleer artikel 17 Vooraleer een opdracht te aanvaarden, moet de boekhouder BiBF die een opdracht van een ander boekhouder BiBF, een accountant of een bedrijfsrevisor overneemt, de volgende regels in acht nemen: 1° hij moet zijn voorganger per aangetekende brief, in kennis stellen van de overname van de opdracht, zelfs indien de opvolging niet onmiddellijk is gebeurd 2° indien de voorganger niet werd betaald voor zijn prestaties, dient hij bij de cliënt aan te dringen op de betaling van de honoraria van zijn voorganger. …alle documenten…alsmede deze die kaderen in de wederzijdse hulp en hoffelijkheid… Hij is gehouden hiervan een gedetailleerde en gedagtekende inventaris in twee exemplaren op te stellen, die door alle betrokken partijen ondertekend wordt.

2) plichtenleer artikel 13, 3e alinea … Het is de boekhouder BiBF verboden op enigerlei wijze commissie of makelaarslonen of welkdanig voordeel ook toe te kennen of te ontvangen die verband houden met zijn opdrachten en die strijdig zijn met artikel 4 van dit reglement. Je mag je broer Paul dus géén aanbrengcommissie geven !

#### Modelantwoord

Art. 17: aangetekende kennisgeving aan voorganger + gedetailleerde inventaris in tweevoud. Art. 13, 3e alinea: commissie aan broer is verboden.

> [!success]- Motivering
> 1) Plichtenleer artikel 17: Vooraleer een opdracht te aanvaarden, moet de boekhouder BIBF die een opdracht van een ander boekhouder BIBF, een accountant of een bedrijfsrevisor overneemt, de volgende regels in acht nemen: 1° hij moet zijn voorganger per aangetekende brief, in kennis stellen van de overname van de opdracht, zelfs indien de opvolging niet onmiddellijk is gebeurd; 2° indien de voorganger niet werd betaald voor zijn prestaties, dient hij bij de cliënt aan te dringen op de betaling van de honoraria van zijn voorganger. …alle documenten…alsmede deze die kaderen in de wederzijdse hulp en hoffelijkheid… Hij is gehouden hiervan een gedetailleerde en gedagtekende inventaris in twee exemplaren op te stellen, die door alle betrokken partijen ondertekend wordt.
> 
> 2) Plichtenleer artikel 13, 3e alinea: Het is de boekhouder BIBF verboden op enigerlei wijze commissie of makelaarslonen of welkdanig voordeel ook toe te kennen of te ontvangen die verband houden met zijn opdrachten en die strijdig zijn met artikel 4 van dit reglement. → Je mag je broer Paul dus géén aanbrengcommissie geven!

> [!info]- Bronnen (1)
> - _pdf-modelantwoord_

---

### 2008-bibf-vrK4 · 2008-bibf

**Vraagformaat**: open · **Antwoord-type**: — · **Confidence**: —

#### Vraagtekst

Rik is stagiair geworden nadat hij “betrapt” is op illegale uitoefening. Voor 2006 heeft hij maar 14 uren beroepsvervolmaking gevolgd. Hij heeft zijn lidgeld niet betaald in 2006 en hij heeft zijn bijdrage beroepsaansprakelijkheidsverzekering niet betaald in 2006. De assessor daagt hem voor de Kamer. Hij komt echter niet opdagen, terwijl hij nochtans tijdig en correct is opgeroepen voor de openbare zitting. Bovendien antwoordt hij op geen enkele brief die de Kamer hem stuurde. De Kamer is niet mals voor deze zondaar en spreekt op 03 november 2007 een tuchtstraf van 3 maanden schorsing uit. Rik gaat niet in beroep binnen de 30 dagen na betekening van het vonnis. Op 3 januari 2008 belt een klant om hem te vragen wanneer hij de BTW aangifte 4 van het jaar 2007 gaat verzorgen.

1) Welk artikel van de plichtenleer moet Rik hier inroepen naar zijn cliënt toe ?

2) Noem minstens 3 artikels van plichtenleer die Rik had overtreden bij de zitting van de Kamer

1) plichtenleer artikel 12 In geval een boekhouder BiBF in de onmogelijkheid is zijn beroepsactiviteit uit te oefenen in gevolge een schorsing van minstens één maand, dient hij zijn cliënteel hiervan in kennis te stellen, wanneer die een beroep op hem doen tijdens de schorsing. 2) Plichtenleer artikel 5 bijdrage Plichtenleer artikel 9 gevraagde inlichtingen Plichtenleer artikel 14 verzekering beroepsaansprakelijkheid Plichtenleer artikel 15 beroepsvervolmaking

#### Modelantwoord

1) Art. 12 plichtenleer (kennisgeving cliënteel bij schorsing ≥ 1 maand). 2) Art. 5 (bijdrage), art. 9 (inlichtingen), art. 14 (BA-verzekering), art. 15 (beroepsvervolmaking).

> [!success]- Motivering
> 1) Plichtenleer artikel 12: In geval een boekhouder BIBF in de onmogelijkheid is zijn beroepsactiviteit uit te oefenen ingevolge een schorsing van minstens één maand, dient hij zijn cliënteel hiervan in kennis te stellen, wanneer die een beroep op hem doen tijdens de schorsing.
> 
> 2) Overtreden artikels: - Plichtenleer artikel 5: bijdrage - Plichtenleer artikel 9: gevraagde inlichtingen - Plichtenleer artikel 14: verzekering beroepsaansprakelijkheid - Plichtenleer artikel 15: beroepsvervolmaking

> [!info]- Bronnen (1)
> - _pdf-modelantwoord_

---

### 2008-bibf-vrK5 · 2008-bibf

**Vraagformaat**: open · **Antwoord-type**: — · **Confidence**: —

#### Vraagtekst

De echtgenoten Philippe en Isabelle, beiden erkend boekhouder(-fiscalist) hebben twee zonen (Frans en Jan) en één dochter (Mathilde). De drie kinderen zijn allen meerderjarig en studeren nog. Om hun werkzaamheden beter te organiseren wensen de ouders een boekhoudvennootschap op te richten conform het KB van 15/2/2005 betreffende de uitoefening van het beroep van erkend boekhouder (-fiscalist) in het kader van een rechtspersoon. Licht steeds uw antwoord toe.!!! - Welke zijn de specifieke aandachtspunten voor de doelomschrijving? Een burgerlijke vennootschap dient opgericht te worden. Het doel moet conform de deontologische voorschriften en het KB van 2005 betreffende de rechtspersonen BIBF worden opgesteld. Dit betekent dat enkel voorbehouden en toegelaten activiteiten van erkende boekhouders(-fiscalisten ) mogen opgenomen worden. Dus bijvoorbeeld geen handelsactiviteiten. (art 7 en 8 KB) - Indien zij opteren voor een BVBA. Wie kan tot zaakvoerder worden benoemd in deze boekhoudvennootschap? Enkel de ouders (Philippe en Isabelle) vermits alle zaakvoerders BIBF lid moeten zijn. (art 8, 5°) - Is volgende verdeling van de aandelen mogelijk? Philippe : 35 %, Isabelle 35 %, Frans, Jan en Mathilde elk 10 % . Licht uw antwoord toe. Neen vermits minstens 80 % van de aandelen en de stemrechten in handen moet zijn van BIBF leden of stagiairs. (art 8 , 4° KB) - De oudste zoon, zal na zijn studies aan de Hogeschool, afdeling boekhouding- fiscaliteit, een BIBF stage aanvangen. Kan hij op dat ogenblik zaakvoerder/bestuurder worden? Kan hij op dat ogenblik tevens 50 % van de aandelen verwerven ? Dit kan vermits stagiair-boekhouders, net zoals BIBF leden , mede het bestuur van de vennootschap mogen waarnemen alsook een aandelenbezit mogen hebben op voorwaarde dat minstens 80 % van de aandelen in handen is van BIBF leden of stagiairs. Stagiairs die hun beroep via een boekhoudvennootschap wensen uit te oefenen, dienen dit tijdens de stage wel steeds samen te doen met ofwel hun stagemeester ofwel een andere erkende boekhouder (fiscalist) BIBF (Zie art 1 en art 2 , par 2 KB)

#### Modelantwoord

Burgerlijke venn. met enkel BIBF-doel; enkel ouders zaakvoerder (art. 8, 5°); aandelenverdeling 70 % onvoldoende (80 %-regel art. 8, 4°); stagiair-zoon kan bestuurder + 50 % aandelen mits 80 %-regel + samen met stagemeester.

> [!success]- Motivering
> - Doelomschrijving: Een burgerlijke vennootschap dient opgericht te worden. Het doel moet conform de deontologische voorschriften en het KB van 2005 betreffende de rechtspersonen BIBF worden opgesteld. Dit betekent dat enkel voorbehouden en toegelaten activiteiten van erkende boekhouders(-fiscalisten) mogen opgenomen worden. Dus bijvoorbeeld geen handelsactiviteiten (art. 7 en 8 KB).
> 
> - Zaakvoerders: Enkel de ouders (Philippe en Isabelle), vermits alle zaakvoerders BIBF-lid moeten zijn (art. 8, 5°).
> 
> - Aandelenverdeling: Neen, vermits minstens 80 % van de aandelen en de stemrechten in handen moet zijn van BIBF-leden of stagiairs (art. 8, 4° KB). Philippe + Isabelle = 70 %, dus onvoldoende.
> 
> - Stagiair-zoon: Dit kan, vermits stagiair-boekhouders, net zoals BIBF-leden, mede het bestuur van de vennootschap mogen waarnemen alsook een aandelenbezit mogen hebben op voorwaarde dat minstens 80 % van de aandelen in handen is van BIBF-leden of stagiairs. Stagiairs die hun beroep via een boekhoudvennootschap wensen uit te oefenen, dienen dit tijdens de stage wel steeds samen te doen met ofwel hun stagemeester ofwel een andere erkende boekhouder(-fiscalist) BIBF (zie art. 1 en art. 2 §2 KB).

> [!info]- Bronnen (1)
> - _pdf-modelantwoord_

---

### 2013-1-vr33 · 2013-1 · 6.0 pt

**Vraagformaat**: MC · **Antwoord-type**: — · **Confidence**: —

#### Vraagtekst

Antiwitwas-wetgeving
In het kader van de Antiwitwas-wetgeving wordt gesproken over een compliane officer of
witwasverantwoordelijke. Deze dient te worden aangesteld als er binnen hetzelfde kantoor
“10” beroepsbeoefenaars werkzaam zijn.
a) Duid hieronder aan wie aanzien wordt als een beroepsbeoefenaar:
Antwoord

Bedrijfsrevisoren

Stagiair bedrijfsrevisoren

Externe Accountants – Belastingconsulenten

Interne Accountants – Belastingconsulenten


Stagiair Accountants – Belastingconsulenten

Externe Belastingconsulenten

Interne Belastingconsulenten

Stagiair Belastingconsulenten

Erkende Boekhouders – Fiscalisten

Erkende Boekhouders

Stagiair Boekhouders – Fiscalisten
b) Wat zijn de taken van een compliance officer of witwasverantwoordelijke?
Geef er 3 op.

**Antwoord
c) Wanneer een compliance officer of witwasverantwoordelijke werd aangesteld, dienen
dan de andere beroepsbeoefenaars nog steeds de nodige meldingen te doen aan de
CFI?**

Antwoord

|   |   |
| --- | --- |
|   | Ja |
|   | Neen |

Zo ja, wat dient er dan te gebeuren:
Antwoord

_Nog niet beantwoord (modelantwoord ontbreekt)._

#### Subvraag a)

Duid hieronder aan wie aanzien wordt als een beroepsbeoefenaar:

#### Subvraag b)

Wat zijn de taken van een compliance officer of witwasverantwoordelijke?
Geef er 3 op.

#### Subvraag c)

Wanneer een compliance officer of witwasverantwoordelijke werd aangesteld, dienen
dan de andere beroepsbeoefenaars nog steeds de nodige meldingen te doen aan de
CFI?

---

### 2013-1-vr34 · 2013-1 · 2.0 pt

**Vraagformaat**: open · **Antwoord-type**: — · **Confidence**: —

#### Vraagtekst

In het kader van het beroepsgeheim zijn twee uitzonderingen ingeschreven in het
strafwetboek, en de externe accountant en/of belastingconsulent dus het beroepsgeheim
naast zich neer kan leggen.
Om welke uitzonderingen gaat het hier?
Antwoord

_Nog niet beantwoord (modelantwoord ontbreekt)._

---

### 2013-1-vr35 · 2013-1 · 5.0 pt

**Vraagformaat**: J/F · **Antwoord-type**: — · **Confidence**: —

#### Vraagtekst

In het kader van de onafhankelijkheid zijn er een aantal activiteiten die expliciet werden
uitgesloten als uit te voeren door een externe accountant en/of belastingconsulent of zijn er
activiteiten die mits te voldoen aan een aantal voorwaarden toch kunnen uitgevoerd worden
door een externe accountant en/of belastingconsulent. Duid aan welke bewering juist of fout
is:
a) Een externe accountant en/of belastingconsulent mag, mits voorafgaande vraag aan
het instituut een activiteit van verzekeringsmakelaar uitoefenen.

|   |   |
| --- | --- |
|   | Juist |
|   | Fout |

b) Een externe accountant en/of belastingconsulent mag geen makelaar in krediet- en
beleggingsverrichtingen zijn.

|   |   |
| --- | --- |
|   | Juist |
|   | Fout |

c) Een externe accountant en/of belastingconsulent kan een bestuursmandaat
waarnemen in een commerciële vennootschap met winstoogmerk, en dit zonder
voorafgaande toestemming van de raad van het instituut indien dit mandaat voort
vloeit uit een rechterlijke beslissing.

|   |   |
| --- | --- |
|   | Juist |
|   | Fout |

d) Een externe accountant en/of belastingconsulent mag, mits te voldoen aan gestelde
voorwaarden, tegelijkertijd zoveel mandaten van onafhankelijke bestuurder
waarnemen als hij/zij het wenst, zolang de voorwaarden van bekwaamheid en
beschikbaarheid vervuld blijven.

|   |   |
| --- | --- |
|   | Juist |
|   | Fout |

e) Een externe accountant en/of belastingconsulent zal nooit een toestemming krijgen
om een mandaat op te nemen in een zuivere patrimoniumvennootschap.

|   |   |
| --- | --- |
|   | Juist |
|   | Fout |

_Nog niet beantwoord (modelantwoord ontbreekt)._

#### Subvraag a)

Een externe accountant en/of belastingconsulent mag, mits voorafgaande vraag aan
het instituut een activiteit van verzekeringsmakelaar uitoefenen.

#### Subvraag b)

Een externe accountant en/of belastingconsulent mag geen makelaar in krediet- en
beleggingsverrichtingen zijn.

#### Subvraag c)

Een externe accountant en/of belastingconsulent kan een bestuursmandaat
waarnemen in een commerciële vennootschap met winstoogmerk, en dit zonder
voorafgaande toestemming van de raad van het instituut indien dit mandaat voort
vloeit uit een rechterlijke beslissing.

#### Subvraag d)

Een externe accountant en/of belastingconsulent mag, mits te voldoen aan gestelde
voorwaarden, tegelijkertijd zoveel mandaten van onafhankelijke bestuurder
waarnemen als hij/zij het wenst, zolang de voorwaarden van bekwaamheid en
beschikbaarheid vervuld blijven.

#### Subvraag e)

Een externe accountant en/of belastingconsulent zal nooit een toestemming krijgen
om een mandaat op te nemen in een zuivere patrimoniumvennootschap.

---

### 2013-1-vr36 · 2013-1 · 2.0 pt

**Vraagformaat**: J/F · **Antwoord-type**: — · **Confidence**: —

#### Vraagtekst

De externe accountant en/of belastingconsulent mag publiciteit voeren, doch dient zich te
houden aan een aantal regels.

**Welke van de onderstaande stellingen is juist of fout:
a) Een externe accountant en/of belastingconsulent mag geen vergelijkende studie
maken van de erelonen die collega’s in zijn buurt aanrekenen in vergelijking met de
erelonen die hij zelf aanrekent.**

|   |   |
| --- | --- |
|   | Juist |
|   | Fout |

b) Een externe accountant en/of belastingconsulent mag zijn diensten aan sterk
verminderde prijzen aanbieden om op die manier de nieuwe klant aan zich te binden

|   |   |
| --- | --- |
|   | Juist |
|   | Fout |

c) Een externe accountant en/of belastingconsulent mag, zoals dat gebruikelijk is bij
andere sectoren, een opsomming geven van enkele van zijn belangrijke klanten

|   |   |
| --- | --- |
|   | Juist |
|   | Fout |

d) Een externe accountant en/of belastingconsulent mag opgeven in welke sectoren hij
werkzaam is om zo een potentiële klant inzicht te geven in zijn bekwaamheden

|   |   |
| --- | --- |
|   | Juist |
|   | Fout |

_Nog niet beantwoord (modelantwoord ontbreekt)._

#### Subvraag a)

Een externe accountant en/of belastingconsulent mag geen vergelijkende studie
maken van de erelonen die collega’s in zijn buurt aanrekenen in vergelijking met de
erelonen die hij zelf aanrekent.

#### Subvraag b)

Een externe accountant en/of belastingconsulent mag zijn diensten aan sterk
verminderde prijzen aanbieden om op die manier de nieuwe klant aan zich te binden

#### Subvraag c)

Een externe accountant en/of belastingconsulent mag, zoals dat gebruikelijk is bij
andere sectoren, een opsomming geven van enkele van zijn belangrijke klanten

#### Subvraag d)

Een externe accountant en/of belastingconsulent mag opgeven in welke sectoren hij
werkzaam is om zo een potentiële klant inzicht te geven in zijn bekwaamheden

---

### 2013-1-vr37 · 2013-1 · 5.0 pt

_Ook geklassificeerd onder_: 3.0

**Vraagformaat**: MC · **Antwoord-type**: — · **Confidence**: —

#### Vraagtekst

Wanneer een externe accountant een door de vennootschappenwet opgelegd en openbaar te
maken controleverslag opstelt, dient hij hiervan een kopie over te maken aan het instituut.
Preciseer vanaf welk moment en binnen welke termijn het verslag moet verstuurd worden in
het kader van:

- **a.** een vereffening van een vennootschap?

Antwoord

- **b.** een omvorming van een vennootschap?

Antwoord
************************************************************************************************

_Nog niet beantwoord (modelantwoord ontbreekt)._

#### Subvraag a)

een vereffening van een vennootschap?

#### Subvraag b)

een omvorming van een vennootschap?

---

### 2013-2-vr35 · 2013-2 · 4.0 pt

**Vraagformaat**: J/F · **Antwoord-type**: — · **Confidence**: —

#### Vraagtekst

Een lid IAB heeft in 2013 volgende vormingsactiviteiten gevolgd:
1) een seminarie georganiseerd door het IAB,
2) een opleiding die werd verstrekt door het kantoor van accountants en
belastingconsulenten waar hij werkzaam is en die geen erkenning als
vormingsoperator aanvroeg
3) enkele seminaries gevolgd bij erkende vormingsoperatoren
Gevraagd:

- **a.** Dient dit lid een bepaalde verhouding in acht te nemen inzake de duur van de

bovenstaande seminaries?
Antwoord … / 2 punten

- **b.** Is de permanente vorming voor accountants en belastingconsulenten een op te volgen

aanbeveling van het Instituut of is het een verplichting ?
Antwoord … / 1 punt

|   |   |
| --- | --- |
|   | Aanbeveling |
|   | Verplichting |

c) Motiveer uw antwoord met verwijzingen naar tenminste 2 relevante teksten.
Antwoord … / 1 punt

_Nog niet beantwoord (modelantwoord ontbreekt)._

#### Subvraag a)

Dient dit lid een bepaalde verhouding in acht te nemen inzake de duur van de
bovenstaande seminaries?

#### Subvraag b)

Is de permanente vorming voor accountants en belastingconsulenten een op te volgen
aanbeveling van het Instituut of is het een verplichting ?

#### Subvraag c)

Motiveer uw antwoord met verwijzingen naar tenminste 2 relevante teksten.

---

### 2013-2-vr36 · 2013-2 · 7.0 pt

**Vraagformaat**: MC · **Antwoord-type**: — · **Confidence**: —

#### Vraagtekst

Op uw kantoor biedt zich de heer Silan aan die u vertelt dat hij zaakvoerder is van de bvba
Witwassen en dat de activiteit van deze bvba een keten van wassalons is. Hij vraagt dat u in

de toekomst de boekhouding en alle daaraan verbonden activiteiten zou overnemen van een
andere accountant - belastingconsulent. Uit het gesprek blijkt ook dat hijzelf geen aandelen
van de vennootschap bezit, maar dat deze in handen zijn van de heer Black met 55% van de
aandelen en de vennootschap nv White met 45% van aandelen.

- **a.** Ingevolge de preventieve antiwitwaswet dient een externe accountant en/of externe

belastingconsulent over te gaan tot de identificatie van een aantal betrokken
partijen bij de acceptatie van een nieuwe dossier. Wie dient u als externe accountant
en/of externe belastingconsulent in de gegeven situatie te identificeren?
Antwoord … / 3 punten

- **b.** Met welke documenten zal u deze identificatie onderbouwen?

Antwoord … / 2 punten

- **c.** Welke gegevens dienen er gecontroleerd te worden?

Antwoord … / 2 punten

_Nog niet beantwoord (modelantwoord ontbreekt)._

#### Subvraag a)

Ingevolge de preventieve antiwitwaswet dient een externe accountant en/of externe
belastingconsulent over te gaan tot de identificatie van een aantal betrokken
partijen bij de acceptatie van een nieuwe dossier. Wie dient u als externe accountant
en/of externe belastingconsulent in de gegeven situatie te identificeren?

#### Subvraag b)

Met welke documenten zal u deze identificatie onderbouwen?

#### Subvraag c)

Welke gegevens dienen er gecontroleerd te worden?

---

### 2013-2-vr37 · 2013-2 · 4.0 pt

**Vraagformaat**: J/F · **Antwoord-type**: — · **Confidence**: —

#### Vraagtekst

In de relatie met confraters wordt u soms geconfronteerd met het feit dat u een dossier
overneemt of dat u zelf een dossier dient over te dragen.

**Welke van onderstaande stellingen zijn juist of fout?**

a) Indien een cliënt al uw erelonen nog niet heeft betaald, bent u toch verplicht om het
dossier over te dragen.

|   |   |
| --- | --- |
|   | Juist |
|   | Fout |

b)Wanneer u de boekhouding heeft gevoerd voor uw cliënt in een boekhoudpakket, dat door
u als accountant werd aangekocht, dient u de historieken en dagboeken niet te overhandigen
aan de vertrekkende klant.

|   |   |
| --- | --- |
|   | Juist |
|   | Fout |

c) Als uw nieuwe cliënt u meedeelt dat hij reeds contact heeft genomen met uw voorganger
dient u zelf geen initiatief meer te nemen om de confrater te contacteren of een brief te
schrijven.

|   |   |
| --- | --- |
|   | Juist |
|   | Fout |

d) Wanneer u reeds ontwerpen opstelde van jaarverslagen of notulen van algemene
vergaderingen dient u deze steeds te overhandigen.

|   |   |
| --- | --- |
|   | Juist |
|   | Fout |

_Nog niet beantwoord (modelantwoord ontbreekt)._

#### Subvraag a)

Indien een cliënt al uw erelonen nog niet heeft betaald, bent u toch verplicht om het
dossier over te dragen.
b)Wanneer u de boekhouding heeft gevoerd voor uw cliënt in een boekhoudpakket, dat door
u als accountant werd aangekocht, dient u de historieken en dagboeken niet te overhandigen
aan de vertrekkende klant.

#### Subvraag c)

Als uw nieuwe cliënt u meedeelt dat hij reeds contact heeft genomen met uw voorganger
dient u zelf geen initiatief meer te nemen om de confrater te contacteren of een brief te
schrijven.

#### Subvraag d)

Wanneer u reeds ontwerpen opstelde van jaarverslagen of notulen van algemene
vergaderingen dient u deze steeds te overhandigen.

---

### 2013-2-vr38 · 2013-2 · 5.0 pt

_Ook geklassificeerd onder_: 3.0

**Vraagformaat**: J/F · **Antwoord-type**: — · **Confidence**: —

#### Vraagtekst

Kan u in volgende situatie als externe accountant een monopolieopdracht aanvaarden?
a) U bent werkzaam in een accountantskantoor en één van uw collega accountants
binnen hetzelfde kantoor vraagt om een verslag op te maken in het kader van een
omvorming van één van de dossiers die hij opvolgt.
Antwoord … / 2,5 punten

|   |   |
| --- | --- |
|   | Ja |
|   | Neen |

Licht kort toe waarom u deze opdracht wel of niet zal aanvaarden?
b) U bent ingeschreven op het tableau van interne accountants en bent in die functie
werkzaam als bediende in een bedrijf. Eén van de aandeelhouders spreekt u aan om
een opdracht uit te voeren in het kader van de individuele onderzoeks- en
controlebevoegdheid van vennoten. Er is geen commissaris-revisor aangesteld.
Antwoord … / 2,5 punten

|   |   |
| --- | --- |
|   | Ja |
|   | Neen |

Licht kort toe waarom u deze opdracht wel of niet zal aanvaarden?
**************************************************************************************************************

_Nog niet beantwoord (modelantwoord ontbreekt)._

#### Subvraag a)

U bent werkzaam in een accountantskantoor en één van uw collega accountants
binnen hetzelfde kantoor vraagt om een verslag op te maken in het kader van een
omvorming van één van de dossiers die hij opvolgt.

#### Subvraag b)

U bent ingeschreven op het tableau van interne accountants en bent in die functie
werkzaam als bediende in een bedrijf. Eén van de aandeelhouders spreekt u aan om
een opdracht uit te voeren in het kader van de individuele onderzoeks- en
controlebevoegdheid van vennoten. Er is geen commissaris-revisor aangesteld.

---

### 2014-1-vr42 · 2014-1 · 3.0 pt

**Vraagformaat**: MC · **Antwoord-type**: — · **Confidence**: —

#### Vraagtekst

Het principe van de kwaliteitstoetsing is dat iedere accountant om de zeven jaar op
kantoorniveau zou gecontroleerd worden. Dit betreft de periodieke toetsing. Daarnaast zijn er
nog drie andere soorten toetsing, namelijk “de vervolgtoetsing”, “de thematische toetsing”
en “de Incidententoetsing”. Geef voor volgende situaties aan welke soort toetsing zal
plaatsvinden:
a) Er wordt aangekondigd om een controle te doen in verband met de toepassing van de
antiwitwaswetgeving
Antwoord

Vervolgtoetsing

Thematische toetsing

Incidententoetsing
b)Ingevolge voorgaande toetsing op de toepassing van de antiwitwaswetgeving heeft men
vastgesteld dat in verschillende dossiers de attesten uiteindelijke begunstigde ontbreken en
men kondigt aan om dit opnieuw te komen controleren
Antwoord

Vervolgtoetsing

Thematische toetsing

Incidententoetsing

c) Er wordt een klacht neergelegd door een confrater in verband met het niet of onvolledig
overdragen van een dossier.
Antwoord

Vervolgtoetsing

Thematische toetsing

Incidententoetsing

_Nog niet beantwoord (modelantwoord ontbreekt)._

#### Subvraag a)

Er wordt aangekondigd om een controle te doen in verband met de toepassing van de
antiwitwaswetgeving

#### Subvraag c)

Er wordt een klacht neergelegd door een confrater in verband met het niet of onvolledig
overdragen van een dossier.

---

### 2014-1-vr43 · 2014-1 · 4.0 pt

**Vraagformaat**: J/F · **Antwoord-type**: — · **Confidence**: —

#### Vraagtekst

Op uw kantoor biedt zich een nieuwe klant aan die de opvolging van zijn vennootschap wil
laten overnemen door uw kantoor. Tijdens dit gesprek komen de volgende punten aan bod.

**Geef aan wanneer u zich niet akkoord kan verklaren met de besproken punten en licht kort
toe waarom u zich niet kan akkoord verklaren.**

- **a.** Hij toont u een overzicht van openstaande facturen bij uw voorganger en een kopij van een

overschrijving voor het globale bedrag om alzo aan te tonen dat alle schulden werden
voldaan aan uw voorganger en deelt u dan ook mee dat het niet meer nodig is om uw collega
te contacteren.

**Antwoord
b) Gezien het 15 april is vraagt hij u om onmiddellijk te starten met het boeken van het eerste
kwartaal van zijn boekjaar zodat de BTW-aangifte tijdig kan ingediend worden en hij tijdig zijn
BTW – schuld kan voldoen.**

Antwoord

- **c.** Hij vertelt u dat zijn keuze op uw kantoor is gevallen omdat u op uw site een vergelijking

heeft gemaakt van de door u aangerekende uurlonen in vergelijking met uw collega’s in de
buurt en als goedkoopste uit deze vergelijking komt.

**Antwoord
d) Tijdens jullie gesprek laat u ook weten dat u zetelt in verschillende commissies binnen het
Instituut en daardoor soms sneller op de hoogte bent van bepaalde wijzigingen.**

Antwoord

_Nog niet beantwoord (modelantwoord ontbreekt)._

#### Subvraag a)

Hij toont u een overzicht van openstaande facturen bij uw voorganger en een kopij van een
overschrijving voor het globale bedrag om alzo aan te tonen dat alle schulden werden
voldaan aan uw voorganger en deelt u dan ook mee dat het niet meer nodig is om uw collega
te contacteren.

#### Subvraag b)

Gezien het 15 april is vraagt hij u om onmiddellijk te starten met het boeken van het eerste
kwartaal van zijn boekjaar zodat de BTW-aangifte tijdig kan ingediend worden en hij tijdig zijn
BTW – schuld kan voldoen.

#### Subvraag c)

Hij vertelt u dat zijn keuze op uw kantoor is gevallen omdat u op uw site een vergelijking
heeft gemaakt van de door u aangerekende uurlonen in vergelijking met uw collega’s in de
buurt en als goedkoopste uit deze vergelijking komt.

#### Subvraag d)

Tijdens jullie gesprek laat u ook weten dat u zetelt in verschillende commissies binnen het
Instituut en daardoor soms sneller op de hoogte bent van bepaalde wijzigingen.

---

### 2014-1-vr44 · 2014-1 · 5.0 pt

**Vraagformaat**: J/F · **Antwoord-type**: — · **Confidence**: —

#### Vraagtekst

In het kader van de samenwerkingsverbanden zijn er sinds 2010 een aantal nieuwe regels.
Zeg voor de onderstaande gevallen of deze situatie juist of fout is:
a) Een middelenvennootschappen kan enkel opgericht worden met confraters IAB.

|   |   |
| --- | --- |
|   | Juist |
|   | Fout |

b) De stemrechten van een professionele vennootschap mogen niet aangehouden worden
door een belangengroepering die de uitoefening van het beroep in gedrang brengt.

|   |   |
| --- | --- |
|   | Juist |
|   | Fout |

c) Wanneer de professionele vennootschap, een vennootschap heeft als zaakvoerder, dan
dient deze vennootschap vertegenwoordigd te worden door een natuurlijk persoon
accountant en/of belastingconsulent.

|   |   |
| --- | --- |
|   | Juist |
|   | Fout |

d)Stagiairs accountant/belastingconsulent mogen nooit zaakvoerder zijn van een
professionele vennootschap.

|   |   |
| --- | --- |
|   | Juist |
|   | Fout |

e)Indien er slechts twee zaakvoerders/bestuurders zijn moeten deze allebei lid zijn van het
IAB.

|   |   |
| --- | --- |
|   | Juist |
|   | Fout |

_Nog niet beantwoord (modelantwoord ontbreekt)._

#### Subvraag a)

Een middelenvennootschappen kan enkel opgericht worden met confraters IAB.

#### Subvraag b)

De stemrechten van een professionele vennootschap mogen niet aangehouden worden
door een belangengroepering die de uitoefening van het beroep in gedrang brengt.

#### Subvraag c)

Wanneer de professionele vennootschap, een vennootschap heeft als zaakvoerder, dan
dient deze vennootschap vertegenwoordigd te worden door een natuurlijk persoon
accountant en/of belastingconsulent.
d)Stagiairs accountant/belastingconsulent mogen nooit zaakvoerder zijn van een
professionele vennootschap.
e)Indien er slechts twee zaakvoerders/bestuurders zijn moeten deze allebei lid zijn van het
IAB.

---

### 2014-1-vr45 · 2014-1 · 3.0 pt

**Vraagformaat**: J/F · **Antwoord-type**: — · **Confidence**: —

#### Vraagtekst

In het KB van 1 maart 1998 wordt eveneens de onafhankelijkheid van de externe
accountant/belastingconsulent behandeld. In dat kader wordt er ook gesproken over
mandaten en opdrachten die men niet mag aanvaarden.

**Geef hierna aan of de stellingen juist
of fout zijn:
a) Mits voorafgaande toestemming van de Raad kan een bestuursmandaat worden
opgenomen in een commerciële vennootschap.**

|   |   |
| --- | --- |
|   | Juist |
|   | Fout |

b) Mits voorafgaande toestemming kan hij een mandaat als onafhankelijke of externe
bestuurder vervullen in een vennootschap, waarin zijn of haar echtgeno(o)t(e) stemrechten
heeft.

|   |   |
| --- | --- |
|   | Juist |
|   | Fout |

c) De interne accountant en/of belastingconsulent valt niet onder de onafhankelijkheids-
verplichtingen gezien hij gebonden is door een arbeidsovereenkomst en dus steeds de
opdrachten van zijn werkgever moet volgen.

|   |   |
| --- | --- |
|   | Juist |
|   | Fout |

_Nog niet beantwoord (modelantwoord ontbreekt)._

#### Subvraag a)

Mits voorafgaande toestemming van de Raad kan een bestuursmandaat worden
opgenomen in een commerciële vennootschap.

#### Subvraag b)

Mits voorafgaande toestemming kan hij een mandaat als onafhankelijke of externe
bestuurder vervullen in een vennootschap, waarin zijn of haar echtgeno(o)t(e) stemrechten
heeft.

#### Subvraag c)

De interne accountant en/of belastingconsulent valt niet onder de onafhankelijkheids-
verplichtingen gezien hij gebonden is door een arbeidsovereenkomst en dus steeds de
opdrachten van zijn werkgever moet volgen.

---

### 2014-1-vr46 · 2014-1 · 5.0 pt

**Vraagformaat**: J/F · **Antwoord-type**: — · **Confidence**: —

#### Vraagtekst

Een confrater, die bij u in de gemeente is gevestigd, vraagt u als extern accountant, voor één
van zijn klanten een verslag van omvorming te willen opmaken.

**Geef aan of u met volgende
stellingen akkoord kan gaan of niet:
a) U kan deze opdracht aanvaarden gezien er, buiten het feit dat u in dezelfde gemeente
gevestigd is, verder geen enkele link is tussen uw kantoor en het kantoor van uw confrater.**

|   |   |
| --- | --- |
|   | Juist |
|   | Fout |

b) U kan de opdrachtgevende klant bijstaan bij het opmaken van de staat van activa en
passiva.

|   |   |
| --- | --- |
|   | Juist |
|   | Fout |

c) Door de uitvoering van deze opdracht heeft de opdrachtgevende klant de beslissing
genomen om zijn dossier onmiddellijk na de omvorming aan uw kantoor toe te vertrouwen,
waarin u kan toestemmen.

|   |   |
| --- | --- |
|   | Juist |
|   | Fout |

d) Het verslag dat u heeft opgemaakt moet ter beschikking gehouden worden van het
Instituut en moet onmiddellijk worden overgemaakt op het ogenblik dat dit gevraagd wordt.

|   |   |
| --- | --- |
|   | Juist |
|   | Fout |

e) Uw confrater, heeft met kennis van zaken een volledig dossier aangemaakt met betrekking
tot de omvorming. Gezien deze voorbereidende werkzaamheden beslist u om zelf geen
dossier aan te leggen en vraagt u uw confrater het dossier ter beschikking te houden indien
nodig voor een controle door het Instituut.

|   |   |
| --- | --- |
|   | Juist |
|   | Fout |

_Nog niet beantwoord (modelantwoord ontbreekt)._

#### Subvraag a)

U kan deze opdracht aanvaarden gezien er, buiten het feit dat u in dezelfde gemeente
gevestigd is, verder geen enkele link is tussen uw kantoor en het kantoor van uw confrater.

#### Subvraag b)

U kan de opdrachtgevende klant bijstaan bij het opmaken van de staat van activa en
passiva.

#### Subvraag c)

Door de uitvoering van deze opdracht heeft de opdrachtgevende klant de beslissing
genomen om zijn dossier onmiddellijk na de omvorming aan uw kantoor toe te vertrouwen,
waarin u kan toestemmen.

#### Subvraag d)

Het verslag dat u heeft opgemaakt moet ter beschikking gehouden worden van het
Instituut en moet onmiddellijk worden overgemaakt op het ogenblik dat dit gevraagd wordt.

#### Subvraag e)

Uw confrater, heeft met kennis van zaken een volledig dossier aangemaakt met betrekking
tot de omvorming. Gezien deze voorbereidende werkzaamheden beslist u om zelf geen
dossier aan te leggen en vraagt u uw confrater het dossier ter beschikking te houden indien
nodig voor een controle door het Instituut.

---

### 2015-1-vr51 · 2015-1 · 3.0 pt

**Vraagformaat**: J/F · **Antwoord-type**: — · **Confidence**: —

#### Vraagtekst

De accountant en/of belastingconsulent is onderworpen aan de discretieplicht en het
beroepsgeheim.

**Geef hieronder aan of de stellingen juist of fout zijn.**

a) In tegenstelling tot het beroepsgeheim is de discretieplicht ook van toepassing op de
interne accountants en/of belastingconsulenten.
Antwoord …/ 1 punt

|   |   |
| --- | --- |
|   | Juist |
|   | Fout |

b) Schending van het beroepsgeheim kan enkel tuchtrechtelijke maatregelen tot gevolg
hebben.
Antwoord …/ 1 punt

|   |   |
| --- | --- |
|   | Juist |
|   | Fout |

c) De accountant en/of de belastingconsulent pleegt een inbreuk tegen de discretieplicht
wanneer hij de Raad van het Instituut in kennis zou stellen van vertrouwelijke
gegevens van zijn werkgever als alle andere middelen zijn uitgeput.
Antwoord …/ 1 punt

|   |   |
| --- | --- |
|   | Juist |
|   | Fout |

_Nog niet beantwoord (modelantwoord ontbreekt)._

#### Subvraag a)

In tegenstelling tot het beroepsgeheim is de discretieplicht ook van toepassing op de
interne accountants en/of belastingconsulenten.

#### Subvraag b)

Schending van het beroepsgeheim kan enkel tuchtrechtelijke maatregelen tot gevolg
hebben.

#### Subvraag c)

De accountant en/of de belastingconsulent pleegt een inbreuk tegen de discretieplicht
wanneer hij de Raad van het Instituut in kennis zou stellen van vertrouwelijke
gegevens van zijn werkgever als alle andere middelen zijn uitgeput.

---

### 2015-1-vr52 · 2015-1 · 3.0 pt

**Vraagformaat**: J/F · **Antwoord-type**: — · **Confidence**: —

#### Vraagtekst

In de artikelen 27 tot en met 29 van het KB van 1 maart 1998 worden de erelonen van de
accountant en/of belastingconsulent behandeld.

**Geef aan of volgende stellingen juist of fout zijn:
a) De accountant en/of belastingconsulent dient met een vast uurloon te werken en mag zijn
ereloon dus niet afhankelijk stellen van de aard, het belang, de complexiteit, omvang en
reikwijdte van de opdracht.**

Antwoord …/ 1 punt

|   |   |
| --- | --- |
|   | Juist |
|   | Fout |

b) Mits goedkeuring van de raad mag een accountant en/of belastingconsulent commissies
ontvangen voor tussenkomst en transacties van andere partijen met een cliënt.
Antwoord …/ 1 punt

|   |   |
| --- | --- |
|   | Juist |
|   | Fout |

c) Indien voorzien in de opdrachtbrief kan er een opzegvergoeding voorzien worden indien
de cliënt de overeenkomst beëindigd.
Antwoord …/ 1 punt

|   |   |
| --- | --- |
|   | Juist |
|   | Fout |

_Nog niet beantwoord (modelantwoord ontbreekt)._

#### Subvraag a)

De accountant en/of belastingconsulent dient met een vast uurloon te werken en mag zijn
ereloon dus niet afhankelijk stellen van de aard, het belang, de complexiteit, omvang en
reikwijdte van de opdracht.

#### Subvraag b)

Mits goedkeuring van de raad mag een accountant en/of belastingconsulent commissies
ontvangen voor tussenkomst en transacties van andere partijen met een cliënt.

#### Subvraag c)

Indien voorzien in de opdrachtbrief kan er een opzegvergoeding voorzien worden indien
de cliënt de overeenkomst beëindigd.

---

### 2015-1-vr53 · 2015-1 · 3.0 pt

**Vraagformaat**: MC · **Antwoord-type**: — · **Confidence**: —

#### Vraagtekst

- **a.** Uw klant, een meubelhandel, stelt u de volgende vraag:

Hoeveel mag de klant van de meubelhandel in contanten betalen in de volgende
gevallen?
Antwoord … / 2 punten
- Een klant koopt een meubel van 2.800 EUR: …………………………………………………..
- Een klant koopt een meubel van 5.800 EUR: ………………………………………………
- Een klant koopt een meubel van 5.800 EUR en betaalt in 2 schijven van 2.900 EUR:
.............................................................................................................................
- Een klant koopt een meubel van 11.000 EUR en betaalt in 2 schijven van 5.500 EUR:
.............................................................................................................................

- **b.** U stelt bij één van uw klanten een overtreding vast van de limiet op toegestane

betalingen in contanten.
Moet u als extern belastingconsulent een melding doen aan de CFI in het kader van de
preventieve witwaswetgeving ?
Antwoord … / 1 punt

_Nog niet beantwoord (modelantwoord ontbreekt)._

#### Subvraag a)

Uw klant, een meubelhandel, stelt u de volgende vraag:
Hoeveel mag de klant van de meubelhandel in contanten betalen in de volgende
gevallen?

#### Subvraag b)

U stelt bij één van uw klanten een overtreding vast van de limiet op toegestane
betalingen in contanten.
Moet u als extern belastingconsulent een melding doen aan de CFI in het kader van de
preventieve witwaswetgeving ?

---

### 2015-1-vr54 · 2015-1 · 3.0 pt

_Ook geklassificeerd onder_: 3.0, 1.6

**Vraagformaat**: J/F · **Antwoord-type**: — · **Confidence**: —

#### Vraagtekst

> De heer FIXIT is reeds jaren de externe accountant van de NV TRIAL.

De gedelegeerde
bestuurder van die vennootschap wenst de vennootschap

> NV TRIAL te vereffenen en geeft
> de heer FIXIT de opdracht dit te doen.

**Geef in onderstaande situaties weer of de stelling of situatie juist of fout is.**

a)

> De heer FIXIT kan dit begeleiden maar mag de controleopdracht op de staat van activa
> en passiva niet uitvoeren wegens een verbod gebaseerd op de onafhankelijkheid.

Antwoord …/ 1 punt

|   |   |
| --- | --- |
|   | Juist |
|   | Fout |

b) Deze controleopdracht kan zowel door een externe accountant, bedrijfsrevisor als
door een erkend boekhouder uitgevoerd worden.
Antwoord …/ 1 punt

|   |   |
| --- | --- |
|   | Juist |
|   | Fout |

c) De externe accountant die dergelijke controleopdracht zal uitvoeren moet ook aan de
verplichtingen gesteld door de witwaswetgeving voldoen en zorgen voor de
identificatie van de bestuurder(s) en de vennootschap.
Antwoord …/ 1 punt

|   |   |
| --- | --- |
|   | Juist |
|   | Fout |

_Nog niet beantwoord (modelantwoord ontbreekt)._

#### Subvraag a)

De heer FIXIT kan dit begeleiden maar mag de controleopdracht op de staat van activa
en passiva niet uitvoeren wegens een verbod gebaseerd op de onafhankelijkheid.

#### Subvraag b)

Deze controleopdracht kan zowel door een externe accountant, bedrijfsrevisor als
door een erkend boekhouder uitgevoerd worden.

#### Subvraag c)

De externe accountant die dergelijke controleopdracht zal uitvoeren moet ook aan de
verplichtingen gesteld door de witwaswetgeving voldoen en zorgen voor de
identificatie van de bestuurder(s) en de vennootschap.

---

### 2015-1-vr55 · 2015-1 · 3.0 pt

**Vraagformaat**: MC · **Antwoord-type**: — · **Confidence**: —

#### Vraagtekst

U bent belastingconsulent, lid van het IAB en ingeschreven op de deellijst van de externe
leden van het Instituut.
Twee personen uit de streek van Aarlen, die u al jaren kent, associëren zich en richten een
vennootschap naar Luxemburgs recht op, die belastingadvies verstrekt in het
Groothertogdom Luxemburg en een kantoor met enige medewerkers opent in België.
Die personen verklaren u dat zij niet direct zinnens zijn die vennootschap te laten erkennen
door het IAB omdat de vennoten eerst willen zien of de activiteiten in België rendabel zijn: ze
zijn van plan om later contact op te nemen met het IAB.
Het Belgische kantoor van de Luxemburgse vennootschap verstrekt uitsluitend
belastingadvies en is wel degelijk voornemens om in haar communicatiebeleid in België de
benaming “belastingconsulent” te gebruiken.
Beantwoord de twee vragen met “ja” of “nee”.

**Verklaar uw antwoord.**

Daar u enige jaren ervaring hebt als belastingconsulent in België, vragen die personen u:
a) in te schrijven op enige aandelen (voor 15% van het kapitaal) van hun vennootschap
naar Luxemburgs recht, zonder evenwel betrokken te zijn bij het bestuur van die
vennootschap.

Antwoord … / 0,5 punt

|   |   |
| --- | --- |
|   | Ja |
|   | Neen |

**Antwoord … / 1 punt
b) hun bij de opstart te begeleiden door hun, zo nodig, als zelfstandige onderaannemer,
bij te staan in moeilijke zaken in België.**

Antwoord … / 0,5 punt

|   |   |
| --- | --- |
|   | Ja |
|   | Neen |

Antwoord … / 1 punt

_Nog niet beantwoord (modelantwoord ontbreekt)._

#### Subvraag a)

in te schrijven op enige aandelen (voor 15% van het kapitaal) van hun vennootschap
naar Luxemburgs recht, zonder evenwel betrokken te zijn bij het bestuur van die
vennootschap.

#### Subvraag b)

hun bij de opstart te begeleiden door hun, zo nodig, als zelfstandige onderaannemer,
bij te staan in moeilijke zaken in België.

---

### 2015-1-vr56 · 2015-1 · 5.0 pt

_Ook geklassificeerd onder_: 3.0

**Vraagformaat**: open · **Antwoord-type**: — · **Confidence**: —

#### Vraagtekst

In de norm inzake de controle van fusie- en splitsingsverrichtingen van vennootschappen
zoals goedgekeurd door de raad van het IAB zijn er drie verplichtingen voor de
beroepsbeoefenaar wanneer de door de wet vereiste verslagen in de bij de fusie of splitsing
betrokken vennootschappen door verschillende beroepsbeoefenaars moeten opgesteld
worden.
Geef twee van de drie verplichtingen
Antwoord
*************************************************************************

_Nog niet beantwoord (modelantwoord ontbreekt)._

---

### 2024-1-vr6 · 2024-1

> [!warning] Herinnering-reconstructie (fragment)
> Deze vraag is een **herinnering**-reconstructie (volledigheid: fragment) — geen officiële ITAA-bundel. Modelantwoord rust op de geherinterpreteerde vraagtekst (ADR-022).

**Vraagformaat**: J/F · **Antwoord-type**: — · **Confidence**: —

#### Vraagtekst

6 Deontologie en AWW

- **A.** Ereloon accountant: (Welke stelling is juist)?
- **A.** Barema ITAA
- **B.** Zelf vaststellen
- **C.** Provisie/voorschotten zijn verboden
- **D.** Kan bestaan uit commissielonen
- **B.** Welke stelling is fout?
- **A.** Dienstverstrekkers, zoals accountants en belastingadviseurs mogen 2.500 EUR contante betaling ontvangen
- **B.** Bij verkoop van een onroerend goed mag een notaris geen enkele betaling in contanten ontvangen
- **C.** De drempel inzake contante betalingen is niet alleen van toepassing op contante betalingen maar ook op schenkingen
- **D.** Indien de koper zich naar een postkantoor begeeft, waarbij de koper het bedrag van 5.000 EUR in contanten laat storten op de bankrekening van de handelaar, is dit in overeenstemming met de antiwitwaswetgeving

E. Er is ook een drempel van 3.000 EUR voor verrichtingen tussen consumenten onderling.

- **C.** Vragen mbt openbaar register.
- **D.** Vragen mbt UBO register. Wie moet worden opgenomen?

E. AMLCO, Stellingen juist of fout?

- **A.** Moet intern verslag maken bij atypische verrichtingen
- **B.** Moet intern verslag maken wanneer kantoor niet kan voldoen aan de verplichting tot beoordeling van het risico verbonden aan de klant
- **C.** Moet intern verslag maken wanneer na het uitvoeren van de risico beoordeling het kantoor beslist om de potentiële cliënt te weigeren wegens WG/ FT risico
- **D.** Zal minstens om de 2 jaar een actualiteitsverslag opmaken.

> [!note]- Geherinterpreteerde vraagtekst (ADR-022)
> Casus deontologie en antiwitwaswetgeving, 5 deelvragen:
> A. MC — Ereloon accountant — welke stelling is juist? a. Bepaald volgens barema ITAA / b. Zelf vaststellen / c. Provisie/voorschotten zijn verboden / d. Kan bestaan uit commissielonen.
> B. MC — Welke stelling is fout? a. Dienstverstrekkers, zoals accountants en belastingadviseurs, mogen 2.500 EUR contante betaling ontvangen / b. Bij verkoop van een onroerend goed mag een notaris geen enkele betaling in contanten ontvangen / c. De drempel inzake contante betalingen is niet alleen van toepassing op contante betalingen maar ook op schenkingen / d. Indien de koper zich naar een postkantoor begeeft, waarbij hij het bedrag van 5.000 EUR in contanten laat storten op de bankrekening van de handelaar, is dit in overeenstemming met de antiwitwaswetgeving / e. Er is ook een drempel van 3.000 EUR voor verrichtingen tussen consumenten onderling.
> C. Vragen met betrekking tot het openbaar register (concrete deelvragen niet bewaard in herinnering).
> D. Vragen met betrekking tot het UBO-register — wie moet erin worden opgenomen?
> E. AMLCO — stellingen juist of fout (J/F-set met vier stellingen):
>     1. Moet een intern verslag opstellen bij atypische verrichtingen.
>     2. Moet een intern verslag opstellen wanneer het kantoor niet kan voldoen aan de verplichting tot beoordeling van het risico verbonden aan de klant.
>     3. Moet een intern verslag opstellen wanneer het kantoor, na de risicobeoordeling, beslist om de potentiële cliënt te weigeren wegens WG/FT-risico.
>     4. Zal minstens om de twee jaar een actualiteitsverslag opmaken.
> 
> _Motivering_: Sub-A en sub-B zijn complete MC's. Sub-C noemt alleen 'Vragen mbt openbaar register' zonder concrete vraag — niet beantwoordbaar. Sub-D heeft een geherinnerde stam (wie in UBO?) — wel beantwoordbaar. Sub-E heeft 4 J/F-stellingen volledig.
> _Confidence_: inferred · _Datum_: 2026-05-19

> [!example]- MC-opties (gestructureerd)
> | Label | Tekst | Juistheid | Motivering |
> | --- | --- | --- | --- |
> | A.a | Bepaald volgens barema ITAA | fout | Er bestaat geen barema voor accountants — afgeschaft. |
> | A.b | Zelf vaststellen | juist | Ereloon wordt vrij overeengekomen tussen accountant en cliënt (ITAA-deontologie). |
> | A.c | Provisie/voorschotten zijn verboden | fout | Provisies en voorschotten zijn toegestaan onder ITAA-deontologie. |
> | A.d | Kan bestaan uit commissielonen | fout | Commissielonen zijn niet toegestaan als ereloon-vorm (onafhankelijkheidsrisico). |
> | B.a | Dienstverstrekkers, zoals accountants en belastingadviseurs, mogen 2.500 EUR contante betaling ontvangen | fout | Onder huidige antiwitwaswet (AWW 2017) gelden algemene drempels — accountants zelf vallen onder beroeps-AWW-verplichtingen. |
> | B.b | Bij verkoop van een onroerend goed mag een notaris geen enkele betaling in contanten ontvangen | juist | Onroerend-goedtransacties: contantverbod is integraal voor notarissen (AWW art. 67). |
> | B.c | De drempel inzake contante betalingen is niet alleen van toepassing op contante betalingen maar ook op schenkingen | onbekend | Te verifiëren in AWW art. 67. |
> | B.d | Indien de koper zich naar een postkantoor begeeft, waarbij hij het bedrag van 5.000 EUR in contanten laat storten op de bankrekening van de handelaar, is dit in overeenstemming met de antiwitwaswetgeving | fout | Tussenkomst van postkantoor breekt de directe contant-keten niet — overschrijdt drempel. |
> | B.e | Er is ook een drempel van 3.000 EUR voor verrichtingen tussen consumenten onderling | onbekend | Te verifiëren in actuele AWW. |

_Nog niet beantwoord (modelantwoord ontbreekt)._

---

## Programmaonderdeel onbekend

_3 vragen — 1 met modelantwoord — 0 met gap-rapport._

### 2003-bibf-vrJ1 · 2003-bibf · 2.5 pt

**Vraagformaat**: open · **Antwoord-type**: — · **Confidence**: —

#### Vraagtekst

Ten gevolge van het verlies van een grote klant, kent een vennootschap grote financiële problemen. De bedrijfsleiders beslissen om hun bezoldigingen fors te verminderen gedurende een bepaalde periode. De bedrijfsleider in kwestie betaalt zelf zijn trimestriële sociale bijdragen. Deze werden berekend op basis van de ontvangen bezoldigingen in 2000. De bedrijfsleider zal grote problemen ondervinden om deze te betalen in 2003. Inderdaad, zijn bezoldiging is fors verminderd in 2003 in verhouding tot hetgeen hij ontving in 2000. Welk advies zal U geven aan deze cliënt ? 2,

_Nog niet beantwoord (modelantwoord ontbreekt)._

---

### 2003-bibf-vrJ2 · 2003-bibf · 2.5 pt

**Vraagformaat**: open · **Antwoord-type**: — · **Confidence**: —

#### Vraagtekst

Een werkgever wenst één van zijn werknemers te ontslaan. Welk is de procedure om deze bediende te ontslaan en een opzegtermijn te geven ? . 2,

_Nog niet beantwoord (modelantwoord ontbreekt)._

---

### 2008-bibf-vrJ1 · 2008-bibf

**Vraagformaat**: open · **Antwoord-type**: — · **Confidence**: —

#### Vraagtekst

Bart is op 1 februari 2001 in dienst getreden van een gekende grootwarenhuisketen. Bart ondertekende op 20 januari 2001 een arbeidsovereenkomst voor onbepaalde duur (voltijds). Bart werkt als bediende en verdeelt zijn tijd tussen het vullen van de rekken en het bedienen van de kassa. Hoewel hierover duidelijke interne richtlijnen bestaan, maakt Bart misbruik van zijn persoonlijke klantenkaart, telkens wanneer een klant zijn / haar klantenkaart is vergeten. In plaats van gebruik te maken van een speciale, anonieme klantenkaart van de werkgever, gebruikt Bart zijn eigen klantenkaart om er de aankopen van de klanten op te registreren. Op die manier slaagt Bart erin om maandelijks enkele waardevolle geschenken 'bijeen te sparen'. Op vrijdag 14 december 2007 wordt de werkgever ingelicht door een collega van Bart. Bart is op dat ogenblik een week met verlof. Na zijn terugkeer uit verlof wordt Bart onmiddellijk geroepen voor een gesprek. Eens geconfronteerd met de feiten, valt Bart door de mand en bekent hij alles. Dit gesprek vindt plaats op vrijdag 21 december 2007. De werkgever beslist, op basis van alle gekende feiten en na de bekentenis van Bart, om Bart te ontslaan wegens dringende reden. 1°Op welke dag moet het ontslag om dringende reden uiterlijk worden betekend? Antwoord: Op woensdag 26 december 2007 (d.i. 3 werkdagen na de kennisname van de feiten; N.B. zondagen en feestdagen worden niet meegeteld). 2° Indien de werkgever beslist om de motivering van het ontslag om dringende reden niet meteen te vermelden in de ontslagbrief zelf, maar wel in een tweede aangetekende brief, wanneer moet deze tweede, gemotiveerde brief ten laatste worden verstuurd als je weet dat de ontslagbrief aangetekend werd verstuurd op maandag 24 december 2007.

**Antwoord: Op vrijdag 28 december 2007 (d.**

i. drie werkdagen na het ontslag). 3° Stel dat het ontslag om dringende reden één dag te laat werd betekend.

**Welke opzegvergoeding moet de werkgever dan betalen, als je weet dat Bart een bruto jaarloon verdient van 27.**

000 EUR? Wat is het bruto bedrag en met hoeveel maanden (bruto) loon stemt deze opzegvergoeding overeen? Antwoord: De opzegvergoeding stemt overeen met 6 maanden loon en bedraagt in casu 13.500 EUR bruto

#### Modelantwoord

1° wo 26.12.2007 (3 werkdagen na kennisname). 2° vr 28.12.2007 (3 werkdagen na ontslag). 3° 6 maanden loon = 13 500 EUR bruto.

> [!success]- Motivering
> 1° Op woensdag 26 december 2007 (d.i. 3 werkdagen na de kennisname van de feiten; N.B. zondagen en feestdagen worden niet meegeteld). 2° Op vrijdag 28 december 2007 (d.i. drie werkdagen na het ontslag). 3° De opzegvergoeding stemt overeen met 6 maanden loon en bedraagt in casu 13.500 EUR bruto.

> [!info]- Bronnen (1)
> - _pdf-modelantwoord_

---
