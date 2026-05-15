# Examenvragen-classificatie naar programmaonderdelen — Subagent-instructies

**Gegenereerd op**: 2026-05-15T15:02:20+00:00
**Model**: claude-sonnet-4-6
**Nog te classificeren**: 183 vragen

## Jouw taak

Classificeer elke examenvraag hieronder naar het (de) juiste programmaonderdeel(en).

Een vraag kan meerdere programmaonderdelen raken (bv. een vraag over
'consolidatieverschil en fiscale behandeling' raakt PO 1.4 én een fiscaliteits-PO).

## Programmaonderdelen

- `1.1`: Algemene boekhouding
- `1.2`: Boekhoudrecht en jaarrekeningenrecht
- `1.3`: Analyse en kritische beoordeling van de jaarrekening
- `1.4`: Geconsolideerde jaarrekening en wetgeving betreffende de geconsolideerde jaarrekening
- `1.5`: Beginselen van de Europese wetgeving en internationale boekhoudkundige normen
- `1.6`: Externe controle
- `1.7`: Interne controle
- `1.8`: Analytische boekhouding en management accounting
- `1.9`: Financiële analyse en fundamentele principes van financieel bedrijfsbeheer
- `2.1`: Algemene beginselen van fiscaal recht
- `2.2`: Personenbelasting
- `2.3`: Vennootschapsbelasting
- `2.4`: Belasting over de toegevoegde waarde
- `2.5`: Fiscale procedure
- `2.6`: Registratie- en successierechten
- `2.7`: Regionale en lokale belastingen
- `2.8`: Europees en internationaal fiscaal recht
- `3.0`: Vennootschaps- en verenigingsrecht en insolventiewetgeving
- `4.0`: Deontologische beginselen in verband met het beroep en beginselen op het vlak van antiwitwaswetgeving

## Output-schema per vraag

```json
{
  "<vraag_id>": {
    "vraag_id": "...",
    "vak_code_in_pdf": "...",
    "vak_naam_in_pdf": "...",
    "programmaonderdelen": ["1.4", "..."],
    "confidence": "hoog | midden | laag",
    "rationale": "<1-2 zin uitleg>"
  }
}
```

## Output-locatie

Schrijf het resultaat als één JSON-object naar:
`data/examen_vragen/_programmaonderdeel_classificatie.json`

Gebruik de bestaande seed-entries als voorbeeld voor het formaat
(die staan al in het bestand als je dit leest).

**Merge met bestaande inhoud**: lees eerst het bestaande bestand,
voeg toe — overschrijf bestaande entries niet zonder reden.

## Richtlijnen

- Gebruik `vak_code_in_pdf` als eerste signaal (bv. "1.4" → PO 1.4).
- Maar: `vak_code_in_pdf` is de **oude nummering** uit de PDF.
  Koppel inhoudelijk: een vraag over 'geconsolideerde jaarrekening'
  of 'consolidatiemethode' hoort bij PO 1.4, ook als de code "1.2" zegt.
- Gebruik `themas[]` en `vraagtekst` voor twijfelgevallen.
- `confidence: "hoog"` als de koppeling duidelijk is uit de vraagtekst.
- `confidence: "midden"` bij redelijke afleiding maar niet 100 % zeker.
- `confidence: "laag"` bij gok of onduidelijke vraag.

## Vragen te classificeren

```json
[
  {
    "id": "2013-1-vr1",
    "vak_code_in_pdf": "1.1",
    "vak_naam_in_pdf": "Wetgeving inzake de jaarrekening",
    "vraagtekst": "Vraag 1 … / 4 punten\nDe besloten vennootschap met beperkte aansprakelijkheid XYZ heeft de volgende balans- en\nresultatenrekening.\nACTIEF JAAR JAAR PASSIEF JAAR JAAR\n2012 2011 2012 2011\nMateriële vaste activa 105.000 100.000 Kapitaal 65.000 65.000\nVorderingen < jaar 45.000 40.000 Reserves 15.000 15.0",
    "themas": [
      "fiscale-verliezen",
      "jaarverslag"
    ]
  },
  {
    "id": "2013-1-vr2",
    "vak_code_in_pdf": "1.1",
    "vak_naam_in_pdf": "Wetgeving inzake de jaarrekening",
    "vraagtekst": "Vraag 2 … / 6 punten\nGelieve voor de onderstaande gevallen het juiste antwoord aan te kruisen.\na) Onderneming A heeft een openstaande leveranciersschuld ten opzichte van\nonderneming X voor een bedrag van 100.000,00 euro. Er werd besloten om deze\nschuld in te brengen als kapitaal.\nZij dient de volgen",
    "themas": [
      "consolidatie",
      "internationaal-fiscaal-recht",
      "kapitaaloperaties",
      "sociale-bijdragen"
    ]
  },
  {
    "id": "2013-1-vr3",
    "vak_code_in_pdf": "1.1",
    "vak_naam_in_pdf": "Wetgeving inzake de jaarrekening",
    "vraagtekst": "Vraag 3 … / 5 punten\nEen onderneming heeft een nieuw prototype ontwikkeld van een transportmiddel dat gebruikt\nkan worden in ondermeer fabrieken voor de verplaatsing van zware goederen.\nZij heeft voor de ontwikkeling tot stand kwam een hele reeks van vooronderzoeken laten\ndoen. Dit heeft nadien gere",
    "themas": [
      "vennootschapsrecht"
    ]
  },
  {
    "id": "2013-1-vr4",
    "vak_code_in_pdf": "1.2",
    "vak_naam_in_pdf": "Analyse en kritische beoordeling van de jaarrekening",
    "vraagtekst": "Vraag 1 … / 9 punten\nIn bijlage vindt u de balans na winstverdeling en de resultatenrekening van een cliënt.\nBereken de gevraagde ratio’s telkens voor het BOEKJAAR.\nU dient de formules NIET uit te schrijven, maar WEL de gebruikte cijfers uit de jaarrekening\nals motivatie van uw antwoord.\nU dient uw ",
    "themas": [
      "jaarrekeninganalyse",
      "vennootschapsrecht",
      "kapitaalsubsidies"
    ]
  },
  {
    "id": "2013-1-vr5",
    "vak_code_in_pdf": "1.2",
    "vak_naam_in_pdf": "Analyse en kritische beoordeling van de jaarrekening",
    "vraagtekst": "Vraag 2 … / 10 punten\nOmschrijf de volgende begrippen :\na) Intrinsieke waarde\nAntwoord\nb) Fractiewaarde\nAntwoord\nc) Netto rendabiliteit van de bedrijfsactiva\nAntwoord\nd) Algemene schuldgraad\nAntwoord\ne) Operationele cash flow voor belastingen\nAntwoord",
    "themas": [
      "financiële-begrippen"
    ]
  },
  {
    "id": "2013-1-vr8",
    "vak_code_in_pdf": "1.3",
    "vak_naam_in_pdf": "Interne controle en accountantsonderzoek",
    "vraagtekst": "Vraag 1 … / 4 punten\nDe interne controle wordt gedefinieerd als:\n\"Het geheel van maatregelen en procedures om een redelijke mate van zekerheid te\nhebben over…”\nGeef vier elementen aan waarover het bestuursorgaan een redelijke zekerheid wil\nbereiken.\nAntwoord",
    "themas": []
  },
  {
    "id": "2013-1-vr9",
    "vak_code_in_pdf": "1.3",
    "vak_naam_in_pdf": "Interne controle en accountantsonderzoek",
    "vraagtekst": "Vraag 2 … / 4 punten\nHet secretariaat van de zaakvoerder van een familiale BVBA betaalt kleine kosten gemaakt\ndoor het personeel terug via een kas.\nStel een procedure op waarbij minimaal twee controletechnische\nfunctiescheidingen in voorkomen.\nAntwoord",
    "themas": [
      "interne-controle",
      "vennootschapsrecht"
    ]
  },
  {
    "id": "2013-1-vr10",
    "vak_code_in_pdf": "1.3",
    "vak_naam_in_pdf": "Interne controle en accountantsonderzoek",
    "vraagtekst": "Vraag 3 … / 4 punten\nGeef één voorbeeld van een analytische test welke op tussentijdse resultaten door de\ninterne controleafdeling (het bedrijf koopt/verkoopt werfkranen) kan uitgevoerd worden\nAntwoord",
    "themas": [
      "analytische-procedures"
    ]
  },
  {
    "id": "2013-1-vr11",
    "vak_code_in_pdf": "1.3",
    "vak_naam_in_pdf": "Interne controle en accountantsonderzoek",
    "vraagtekst": "Vraag 4 … / 4 punten\nWat is het belang van een budget voor de interne controleafdeling?\nAntwoord",
    "themas": []
  },
  {
    "id": "2013-1-vr12",
    "vak_code_in_pdf": "1.3",
    "vak_naam_in_pdf": "Interne controle en accountantsonderzoek",
    "vraagtekst": "Vraag 5 … / 4 punten\nWaarom zal de interne controleafdeling zich niet alleen steunen op de boekhouding maar\nook periodiek schriftelijk confirmatie vragen bij leveranciers?\nAntwoord",
    "themas": [
      "confirmatiebrieven"
    ]
  },
  {
    "id": "2013-1-vr13",
    "vak_code_in_pdf": "1.3",
    "vak_naam_in_pdf": "Interne controle en accountantsonderzoek",
    "vraagtekst": "Vraag 6 … / 30 punten\nOpgave :\nNV SLA-BAK is een kleine onderneming met goede resultaten.\nDe boekhouder valt vrij plots ziek en hij zal gedurende langere tijd afwezig zijn.\nDe bedrijfsleider wil tussentijdse cijfers en vraagt aan een extern accountant om een\ntussentijdse staat van activa en passiva ",
    "themas": [
      "vennootschapsrecht"
    ]
  },
  {
    "id": "2013-1-vr14",
    "vak_code_in_pdf": "3.1",
    "vak_naam_in_pdf": "Vennootschapsrecht",
    "vraagtekst": "Vraag 1 … / 14 punten\nHierna volgt de balans van de bvba Avenir, afgesloten op 31/12/2012:\nACTIVA PASSIVA\nMateriële vaste activa € 25.000 Geplaatst kapitaal € 20.460\nVoorraden € 7.500 Overgedragen winst € 44.540\nVorderingen op – 1 jaar € 75.500 Leveranciers € 28.500\nLiquide middelen € 12.500 Belasti",
    "themas": [
      "vennootschapsrecht"
    ]
  },
  {
    "id": "2013-1-vr15",
    "vak_code_in_pdf": "3.1",
    "vak_naam_in_pdf": "Vennootschapsrecht",
    "vraagtekst": "Vraag 2 … / 6 punten\nSinds 1 januari 2008 kunnen er geen nieuwe effecten aan toonder uitgegeven worden.\nDe wetgever heeft gesteld dat uiterlijk op 31 december 2013 de effecten aan toonder\nmoeten omgezet zijn.\na) De wetgever heeft om de omzetten te versnellen reeds een maatregel genomen,\neen maatrege",
    "themas": [
      "omzetting-vennootschap"
    ]
  },
  {
    "id": "2013-1-vr16",
    "vak_code_in_pdf": "3.2",
    "vak_naam_in_pdf": "Vennootschapsrecht (bijzondere mandaten)",
    "vraagtekst": "Vraag 1 …/ 7 punten\nHet Wetboek van Vennootschappen voorziet in een procedure van ontbinding.\na) Wat is het voorwerp en het doel van de opdracht van de externe accountant?\nAntwoord\nb) Wie stelt de staat van activa en passiva op?\nAntwoord\nc) Wanneer kan de staat van activa en passiva opgesteld worden",
    "themas": [
      "ontbinding-vereffening",
      "continuiteitsbeginsel"
    ]
  },
  {
    "id": "2013-1-vr17",
    "vak_code_in_pdf": "3.2",
    "vak_naam_in_pdf": "Vennootschapsrecht (bijzondere mandaten)",
    "vraagtekst": "Vraag 2 … / 7 punten\nOp de boekhoudkundige staat van de BVBA HOLDING RICH komen nog diverse machines A\nvoor. De zaakvoerders van de BVBA HOLDING RICH hebben een gemotiveerde, technisch en\nfinancieel onderbouwde waardering gemaakt van deze machines (totale waarde\n€ 600.000) op basis van de berekening",
    "themas": [
      "ontbinding-vereffening",
      "herwaarderingsmeerwaarden",
      "fiscale-verliezen",
      "vennootschapsrecht",
      "herwaarderingsmeerwaarden"
    ]
  },
  {
    "id": "2013-1-vr18",
    "vak_code_in_pdf": "3.2",
    "vak_naam_in_pdf": "Vennootschapsrecht (bijzondere mandaten)",
    "vraagtekst": "Vraag 3 … / 12 punten\nIn de BVBA GOFORT werd een staat van activa en passiva afgesloten per 31/01/2013\nopgesteld en ondertekend door de interne boekhouder, met het oog op de ontbinding van de\nvennootschap. De algemene vergadering wordt samengeroepen om te beslissen op\n15/04/2013 bij notaris. Het con",
    "themas": [
      "ontbinding-vereffening",
      "vennootschapsrecht"
    ]
  },
  {
    "id": "2013-1-vr19",
    "vak_code_in_pdf": "3.2",
    "vak_naam_in_pdf": "Vennootschapsrecht (bijzondere mandaten)",
    "vraagtekst": "Vraag 4 … / 4 punten\nDe normen inzake het verslag op te stellen bij de omzetting van een vennootschap stelt dat\nde beroepsbeoefenaar bij het aanvaarden van zijn opdracht over een behoorlijke\nopdrachtbrief dient te beschikken.\na) Wie ondertekent de opdrachtbrief ?\nAntwoord\nb) Geef 3 elementen die min",
    "themas": [
      "omzetting-vennootschap",
      "vennootschapsrecht"
    ]
  },
  {
    "id": "2013-1-vr20",
    "vak_code_in_pdf": "2.1",
    "vak_naam_in_pdf": "Personenbelasting",
    "vraagtekst": "Vraag 1 … / 12 punten\nDe heer André, een loodgieter van 58 jaar oud, zet in 2012 zijn beroepswerkzaamheid stop en\nverkoopt zijn volledige handelszaak aan de heer Bernard\n(NB: geen verwantschap tussen de overlater en de overnemer).\nBereken, op basis van de hierna verstrekte gegevens, het bedrag van d",
    "themas": [
      "stopzettingsmeerwaarden"
    ]
  },
  {
    "id": "2013-1-vr21",
    "vak_code_in_pdf": "2.1",
    "vak_naam_in_pdf": "Personenbelasting",
    "vraagtekst": "Vraag 2 … / 8 punten\nGeef aan of volgende uitspraken waar of onwaar zijn:\na) Wanneer een werknemer voorafbetalingen doet, zal hij een bonificatie genieten, maar\nenkel voor de belasting die betrekking heeft op zijn beroepsinkomsten.\nWaar\nNiet waar\nb) De interest van een spaarrekening geopend ten name",
    "themas": [
      "personenbelasting"
    ]
  },
  {
    "id": "2013-1-vr22",
    "vak_code_in_pdf": "2.2",
    "vak_naam_in_pdf": "Vennootschapsbelasting",
    "vraagtekst": "Vraag 1 … / 6 punten\nEen bvba verschaft volgende gegevens over de waardering van haar goederenvoorraad voor\nhet jaar 2012 (we beperken ons tot één bepaald type product) :\nDe bedragen zijn exclusief btw.\nBeginvoorraad = 265 stuks\nAantal aangekochte producten = 1 810 stuks\nAantal verkochte producten =",
    "themas": [
      "vennootschapsrecht"
    ]
  },
  {
    "id": "2013-1-vr23",
    "vak_code_in_pdf": "2.2",
    "vak_naam_in_pdf": "Vennootschapsbelasting",
    "vraagtekst": "Vraag 2 … / 6 punten\nEen bestaande Belgische NV (kleine vennootschap volgens art. 15 W.Venn.) die haar balans\nafsluit op 31.12.2012 beheert de volgende voorziening, door het vereiste formulier (204.3):\nEen voorziening van 23 000,00 euro voor grote herstellingen prijkte op de balans van het\nboekjaar ",
    "themas": [
      "voorzieningen",
      "vennootschapsrecht",
      "voorzieningen"
    ]
  },
  {
    "id": "2013-1-vr24",
    "vak_code_in_pdf": "2.2",
    "vak_naam_in_pdf": "Vennootschapsbelasting",
    "vraagtekst": "Vraag 3 … / 8 punten\nEen vennootschap heeft een boekjaar van 1 oktober 2011 tot en met 30 september 2012. In de\nperiode tussen 1 januari 2012 tot en met 30 september 2012 zijn de belastbare voordelen van\nalle aard uit firmawagens voor de personeelsleden en de bedrijfsleiders van de\nvennootschap geli",
    "themas": [
      "personenwagen-btw",
      "vennootschapsbelasting"
    ]
  },
  {
    "id": "2013-1-vr25",
    "vak_code_in_pdf": "2.3",
    "vak_naam_in_pdf": "Belasting over de toegevoegde waarde",
    "vraagtekst": "Vraag 1 … / 9 punten\nVermeld voor onderstaande handelingen het(de) rooster(s) van de btw-aangifte die moeten\ningevuld worden en eveneens het(de) overeenkomstig(e) bedrag(en).\nEen modelaangifte is in bijlage toegevoegd.\nU mag er van uit gaan dat de bedragen exclusief btw zijn.\na) Een gewone belasting",
    "themas": [
      "btw-aangifte"
    ]
  },
  {
    "id": "2013-1-vr26",
    "vak_code_in_pdf": "2.3",
    "vak_naam_in_pdf": "Belasting over de toegevoegde waarde",
    "vraagtekst": "Vraag 2 … / 6 punten\nWelke btw gevolgen zijn verbonden aan de onderstaande gegevens:\nGeef hierbij een woordje uitleg (geen verwijzing naar artikelnummers) en vermeld\novereenkomstig(e) bedrag(en). De nummers van de roosters van de btw-aangifte moet je niet\nvermelden.\na) A, een handelaar in computers ",
    "themas": [
      "personenwagen-btw",
      "vennootschapsrecht",
      "btw-aangifte"
    ]
  },
  {
    "id": "2013-1-vr27",
    "vak_code_in_pdf": "2.4",
    "vak_naam_in_pdf": "Beginselen van registratie- en successierechten",
    "vraagtekst": "Vraag 1 … / 8 punten\nDe heer Vandenbroucke, wonende in Nederland, verkoopt aan mevrouw Leroy, wonende in\nBelgië, een in Leuven gelegen gemeubileerd appartement (mevrouw Leroy is al eigenaar van\nhet bovenvermeld appartement: zij wil er een duplex van maken). De optredende notaris is\nmeester Vandewiel",
    "themas": [
      "registratierechten",
      "vennootschapsrecht"
    ]
  },
  {
    "id": "2013-1-vr28",
    "vak_code_in_pdf": "2.4",
    "vak_naam_in_pdf": "Beginselen van registratie- en successierechten",
    "vraagtekst": "Vraag 2 … / 2 punten\nDe heer André, sinds meer dan 10 jaar weduwnaar, is overleden en laat als enige wettige\nerfgename zijn dochter Anne na.\nKorte tijd vóór zijn overlijden heeft de heer André een authentiek testament opgesteld (dat bij\neen notaris werd neergelegd) waarin hij mevrouw Michèle, met wi",
    "themas": [
      "successierechten"
    ]
  },
  {
    "id": "2013-1-vr29",
    "vak_code_in_pdf": "2.6",
    "vak_naam_in_pdf": "Beginselen van Europees en internationaal fiscaal recht",
    "vraagtekst": "Vraag 1 … / 5 punten\nDe heer B. is een natuurlijke persoon van Belgische nationaliteit, vrijgezel en zonder\npersonen ten laste, en op fiscaal gebied inwoner van België. Hij is bediende bij een\nvennootschap naar Belgisch recht met een vaste inrichting in Frankrijk. Die Belgische\nvennootschap maakt de",
    "themas": [
      "internationaal-fiscaal-recht"
    ]
  },
  {
    "id": "2013-1-vr30",
    "vak_code_in_pdf": "2.6",
    "vak_naam_in_pdf": "Beginselen van Europees en internationaal fiscaal recht",
    "vraagtekst": "Vraag 2 … / 5 punten\nUw cliënt en zijn echtgenote zijn de enige aandeelhouders van een naamloze vennootschap\nnaar Belgisch recht.\nHun schoonbroer bezit 97% van de aandelen van een handelsvennootschap naar Hongaars\nrecht (rechtsvorm die overeenkomt met een naamloze vennootschap). De resterende 3% van",
    "themas": [
      "internationaal-fiscaal-recht"
    ]
  },
  {
    "id": "2013-1-vr31",
    "vak_code_in_pdf": "2.7",
    "vak_naam_in_pdf": "Fiscale procedure",
    "vraagtekst": "Vraag 1 … / 9 punten\nDe onderneming “Snack on the Road” exploiteert een foodservice langs de autosnelweg. De\nbediening ligt naast een tankstation en verschaft maaltijden en bereid voedsel aan\nautomobilisten die op de pleisterplaats of aan het tankstation stoppen. De producten zijn\nzowel verpakt voor",
    "themas": [
      "fiscale-procedure"
    ]
  },
  {
    "id": "2013-1-vr32",
    "vak_code_in_pdf": "2.7",
    "vak_naam_in_pdf": "Fiscale procedure",
    "vraagtekst": "Vraag 2 … / 6 punten\nOp 5 februari 2013 wordt het proces-verbaal van de administratie van de btw overgezonden\naan de controleur van de directe belastingen van de onderneming Snack on the Road.\nDie vennootschap sluit haar boekjaar af op 31 maart van het jaar.\nDe controleur geeft kennis van de aanwijz",
    "themas": [
      "fiscale-procedure"
    ]
  },
  {
    "id": "2013-1-vr33",
    "vak_code_in_pdf": "4.0",
    "vak_naam_in_pdf": "Juridische en beroepsnormen / deontologie",
    "vraagtekst": "Vraag 1 …. / 6 punten\nAntiwitwas-wetgeving\nIn het kader van de Antiwitwas-wetgeving wordt gesproken over een compliane officer of\nwitwasverantwoordelijke. Deze dient te worden aangesteld als er binnen hetzelfde kantoor\n“10” beroepsbeoefenaars werkzaam zijn.\na) Duid hieronder aan wie aanzien wordt al",
    "themas": [
      "antiwitwaswet"
    ]
  },
  {
    "id": "2013-1-vr34",
    "vak_code_in_pdf": "4.0",
    "vak_naam_in_pdf": "Juridische en beroepsnormen / deontologie",
    "vraagtekst": "Vraag 2 …. / 2 punten\nIn het kader van het beroepsgeheim zijn twee uitzonderingen ingeschreven in het\nstrafwetboek, en de externe accountant en/of belastingconsulent dus het beroepsgeheim\nnaast zich neer kan leggen.\nOm welke uitzonderingen gaat het hier?\nAntwoord",
    "themas": [
      "beroepsgeheim"
    ]
  },
  {
    "id": "2013-1-vr35",
    "vak_code_in_pdf": "4.0",
    "vak_naam_in_pdf": "Juridische en beroepsnormen / deontologie",
    "vraagtekst": "Vraag 3 …. / 5 punten\nIn het kader van de onafhankelijkheid zijn er een aantal activiteiten die expliciet werden\nuitgesloten als uit te voeren door een externe accountant en/of belastingconsulent of zijn er\nactiviteiten die mits te voldoen aan een aantal voorwaarden toch kunnen uitgevoerd worden\ndoo",
    "themas": [
      "onafhankelijkheid"
    ]
  },
  {
    "id": "2013-1-vr36",
    "vak_code_in_pdf": "4.0",
    "vak_naam_in_pdf": "Juridische en beroepsnormen / deontologie",
    "vraagtekst": "Vraag 4 …. / 2 punten\nDe externe accountant en/of belastingconsulent mag publiciteit voeren, doch dient zich te\nhouden aan een aantal regels. Welke van de onderstaande stellingen is juist of fout:\na) Een externe accountant en/of belastingconsulent mag geen vergelijkende studie\nmaken van de erelonen ",
    "themas": [
      "publiciteit-beroepsnormen"
    ]
  },
  {
    "id": "2013-1-vr37",
    "vak_code_in_pdf": "4.0",
    "vak_naam_in_pdf": "Juridische en beroepsnormen / deontologie",
    "vraagtekst": "Vraag 5 …. / 5 punten\nWanneer een externe accountant een door de vennootschappenwet opgelegd en openbaar te\nmaken controleverslag opstelt, dient hij hiervan een kopie over te maken aan het instituut.\nPreciseer vanaf welk moment en binnen welke termijn het verslag moet verstuurd worden in\nhet kader v",
    "themas": [
      "omzetting-vennootschap",
      "ontbinding-vereffening"
    ]
  },
  {
    "id": "2013-2-vr1",
    "vak_code_in_pdf": "1.1",
    "vak_naam_in_pdf": "Wetgeving inzake de jaarrekening",
    "vraagtekst": "Vraag 1 … / 3 punten\nOnderneming “Softy” BVBA is één maand actief. Zij ontwikkelt software. De onderneming wil\nde volgende transacties in haar boekhouding verwerken en vraagt u advies bij de verwerking\nhiervan. Kruis het juiste antwoord aan.\na) Aankoop van 10 laptops met software Windows 8\nAntwoord ",
    "themas": [
      "immateriële-vaste-activa",
      "vennootschapsrecht"
    ]
  },
  {
    "id": "2013-2-vr2",
    "vak_code_in_pdf": "1.1",
    "vak_naam_in_pdf": "Wetgeving inzake de jaarrekening",
    "vraagtekst": "Vraag 2 … / 4 punten\nGelieve voor de onderstaande gevallen het juiste antwoord aan te kruisen.\na) Tijdens het afgelopen boekjaar hebben een aantal bestuursleden ontslag genomen. Er\nwerden ter vervanging nieuwe bestuurders benoemd. In de jaarrekening over het\nafgelopen jaar neemt zij volgende bestuur",
    "themas": [
      "afschrijvingen"
    ]
  },
  {
    "id": "2013-2-vr3",
    "vak_code_in_pdf": "1.1",
    "vak_naam_in_pdf": "Wetgeving inzake de jaarrekening",
    "vraagtekst": "Vraag 3 … / 4 punten\nVennootschap “ Final” BVBA heeft van vennootschap “DEF” een aantal activa gekocht, zoals\nmachines en voorraad. Deze activa hadden de volgende marktwaarde:\nMachine A 15.000 euro\nMachine B 25.000 euro\nVoorraad 30.000 euro\nZij heeft in totaal 100.000 euro betaald. Het bedrag van 30",
    "themas": [
      "goodwill",
      "vennootschapsrecht"
    ]
  },
  {
    "id": "2013-2-vr4",
    "vak_code_in_pdf": "1.1",
    "vak_naam_in_pdf": "Wetgeving inzake de jaarrekening",
    "vraagtekst": "Vraag 4 … / 4 punten\nEen onderneming laat om de acht jaar haar gebouwen herschilderen. De schilderwerken\nworden geschat op 40.000 euro.\na) Kan zij in haar jaarrekening hiermee al rekening houden? Op welke manier en voor\nwelk bedrag zal zij dit doen?\nAntwoord … / 2 punten\nb) Wat indien na acht jaar d",
    "themas": [
      "voorzieningen"
    ]
  },
  {
    "id": "2013-2-vr5",
    "vak_code_in_pdf": "1.2",
    "vak_naam_in_pdf": "Analyse en kritische beoordeling van de jaarrekening",
    "vraagtekst": "Vraag 1 … / 6 punten\nIn bijlage vindt u de balans na winstverdeling en de resultatenrekening van een cliënt.\nBereken de gevraagde ratio’s telkens voor het BOEKJAAR.\nU dient de formules NIET uit te schrijven, maar WEL de gebruikte cijfers uit de jaarrekening\nals motivatie van uw antwoord.\nU dient uw ",
    "themas": [
      "jaarrekeninganalyse",
      "vennootschapsrecht"
    ]
  },
  {
    "id": "2013-2-vr6",
    "vak_code_in_pdf": "1.2",
    "vak_naam_in_pdf": "Analyse en kritische beoordeling van de jaarrekening",
    "vraagtekst": "Vraag 2 … / 3 punten\nBij de bespreking van de jaarrekening deelt U aan uw cliënt mede dat het netto\nbedrijfskapitaal van zijn vennootschap zeer laag is. Hij vraagt U hoe hij het netto\nbedrijfskapitaal kan verhogen.\nGeef drie voorbeelden.\nAntwoord",
    "themas": []
  },
  {
    "id": "2013-2-vr7",
    "vak_code_in_pdf": "1.2",
    "vak_naam_in_pdf": "Analyse en kritische beoordeling van de jaarrekening",
    "vraagtekst": "Vraag 3 … / 6 punten\na) Wat komt een bedrijfsleider te weten door de liquiditeitsratio’s te berekenen ?\nAntwoord … / 2 punten\nb) Met welke elementen houdt men geen rekening bij de berekening van de liquiditeit in\nenge zin en wel bij de berekening van de liquiditeit in ruime zin?\nAntwoord … / 2 punte",
    "themas": [
      "jaarrekeninganalyse"
    ]
  },
  {
    "id": "2013-2-vr8",
    "vak_code_in_pdf": "1.2",
    "vak_naam_in_pdf": "Analyse en kritische beoordeling van de jaarrekening",
    "vraagtekst": "Vraag 4 … / 10 punten\na) Wat is een positief consolidatieverschil ?\nAntwoord … / 2 punten\nb) Geef de vier voornaamste oorzaken van positieve consolidatieverschillen ?\nAntwoord … / 8 punten",
    "themas": [
      "consolidatie"
    ]
  },
  {
    "id": "2013-2-vr9",
    "vak_code_in_pdf": "1.3",
    "vak_naam_in_pdf": "Interne controle en accountantsonderzoek",
    "vraagtekst": "Vraag 1 … / 8 punten\nEen auditprocedure is een gedetailleerde instructie voor het verzamelen van een bepaald\nauditbewijsmiddel.\nGeef 4 soorten auditmethodes.\nAntwoord",
    "themas": [
      "auditopdracht"
    ]
  },
  {
    "id": "2013-2-vr10",
    "vak_code_in_pdf": "1.3",
    "vak_naam_in_pdf": "Interne controle en accountantsonderzoek",
    "vraagtekst": "Vraag 2 … / 12 punten\nIn het kader van scheiding van functies kunnen er 4 soorten taken worden onderkend :\nAutorisatie (1), bewaren van activa (2), registratie en rapportering (3) en controle procedures\n(4)\nDuid in onderstaande tabel aan welke soort taak bedoeld is.\nACTIVITEIT 1 2 3 4\nAkkoord bestel",
    "themas": []
  },
  {
    "id": "2013-2-vr11",
    "vak_code_in_pdf": "1.3",
    "vak_naam_in_pdf": "Interne controle en accountantsonderzoek",
    "vraagtekst": "Vraag 3 … / 8 punten\nWanneer dient een accountant een onthoudende verklaring af te geven?\nAntwoord",
    "themas": [
      "auditopdracht"
    ]
  },
  {
    "id": "2013-2-vr12",
    "vak_code_in_pdf": "1.3",
    "vak_naam_in_pdf": "Interne controle en accountantsonderzoek",
    "vraagtekst": "Vraag 4 … / 14 punten\nDe interne controle heeft een preventief, repressief en corrigerend karakter.\nKruis aan of deze voorbeelden een preventieve, repressieve of corrigerende maatregel zijn.\nAntwoord\nPreventief Repressief Corrigerend\nFunctiescheiding\nPeriodieke inventarisaties\nTussentijdse confirmat",
    "themas": [
      "interne-controle",
      "confirmatiebrieven",
      "vennootschapsrecht",
      "analytische-procedures"
    ]
  },
  {
    "id": "2013-2-vr13",
    "vak_code_in_pdf": "1.3",
    "vak_naam_in_pdf": "Interne controle en accountantsonderzoek",
    "vraagtekst": "Vraag 5 … / 8 punten\nJe wordt gevraagd om als extern accountant een controleopdracht uit te voeren bij de NV\nFortunato. De interne boekhouder van de onderneming bezorgt de cijfers per 30 november\n2013 ( = de afsluitdatum conform de statuten).\nOp 2 december 2013 heb je ter plaatse de voorraadtelling ",
    "themas": [
      "vennootschapsrecht"
    ]
  },
  {
    "id": "2013-2-vr14",
    "vak_code_in_pdf": "3.1",
    "vak_naam_in_pdf": "Vennootschapsrecht",
    "vraagtekst": "Vraag 1 … / 3 punten\nWat de bij de Nationale Bank van België neergelegde jaarrekeningen betreft, stelt u op 4 mei\n2013 vast dat uw nieuwe cliënt, de bvba “Mode Invest”, de jaarrekeningen van de vier laatste\nboekjaren niet meer heeft neergelegd.\na) Wat zult u uw cliënt adviseren?\nAntwoord … / 1 punt\n",
    "themas": [
      "vennootschapsrecht"
    ]
  },
  {
    "id": "2013-2-vr15",
    "vak_code_in_pdf": "3.1",
    "vak_naam_in_pdf": "Vennootschapsrecht",
    "vraagtekst": "Vraag 2 … / 4 punten\nIs, in de 2 onderstaande situaties de bijzondere procedure, de zogenaamde\nalarmbelprocedure, van toepassing voor de bvba “Zonder Zorgen”?\nKunt u voor elk geval en voor elk antwoord een bondige uitleg geven?\n1. Eerste situatie\nActiva Passiva\nOprichtingskosten 2.000,00 Geplaatst k",
    "themas": [
      "alarmbelprocedure",
      "fiscale-verliezen",
      "vennootschapsrecht"
    ]
  },
  {
    "id": "2013-2-vr16",
    "vak_code_in_pdf": "3.1",
    "vak_naam_in_pdf": "Vennootschapsrecht",
    "vraagtekst": "Vraag 3 … / 4 punten\nAls accountant en/of belastingconsulent van de in 2012 opgerichte nv “Vivant” wordt u\ngeraadpleegd door de drie aandeelhouders, tevens de bestuurders van de vennootschap, die\neen aantal vragen hebben omtrent hun toestand:\na) De statuten van de vennootschap voorzien in de procedu",
    "themas": [
      "vennootschapsrecht"
    ]
  },
  {
    "id": "2013-2-vr17",
    "vak_code_in_pdf": "3.1",
    "vak_naam_in_pdf": "Vennootschapsrecht",
    "vraagtekst": "Vraag 4 … / 6 punten\nKruis de juiste antwoorden aan in onderstaande tabel:\n1. Welke vennootschap kan opgericht worden met een onderhandse akte?\n2. Welke vennootschap kan winstbewijzen toekennen?\n3. Welke vennootschap is verplicht haar jaarrekening neer te leggen bij de Nationale Bank\nvan België?\n4. ",
    "themas": [
      "vennootschapsrecht"
    ]
  },
  {
    "id": "2013-2-vr18",
    "vak_code_in_pdf": "3.1",
    "vak_naam_in_pdf": "Vennootschapsrecht",
    "vraagtekst": "Vraag 5 … / 3 punten\nDe heer en mevrouw X bezitten aandelen in de bvba “Invest Plan”, die actief is in de\nvastgoedsector.\nHun aandeel in deze vennootschap bedraagt 11,3% van het totaal aantal aandelen.\nTijdens de laatste algemene vergadering hadden zij zich tegen de twee zaakvoerders van de\nbvba gek",
    "themas": [
      "vennootschapsrecht"
    ]
  },
  {
    "id": "2013-2-vr19",
    "vak_code_in_pdf": "3.2",
    "vak_naam_in_pdf": "Vennootschapsrecht (bijzondere mandaten)",
    "vraagtekst": "Vraag 1 …/ 22 punten\nEen collega accountant die je kent van uw beroepsvereniging vraagt om uw tussenkomst bij\nde omzetting van een vennootschap van één van zijn klanten. Het betreft de CVBA Fortunito\ndie wenst om te zetten naar de BVBA Roflexfort.\nOp vraag van uw collega zendt de interne boekhouder ",
    "themas": [
      "omzetting-vennootschap",
      "onafhankelijkheid",
      "afschrijvingen",
      "vennootschapsrecht"
    ]
  },
  {
    "id": "2013-2-vr20",
    "vak_code_in_pdf": "3.2",
    "vak_naam_in_pdf": "Vennootschapsrecht (bijzondere mandaten)",
    "vraagtekst": "Vraag 2 … / 8 punten\nEen Franse vennootschap is voor 15% aandeelhouder in een Belgische vennootschap BVBA\nSUPERTOC. De Franse vennootschap vraagt je om in het kader van het individueel\ncontrolerecht ter plaatse inzage te nemen in de stukken van de BVBA SUPERTOC.\nBeantwoord met FOUT / JUIST volgende ",
    "themas": [
      "individueel-controlerecht",
      "vennootschapsrecht"
    ]
  },
  {
    "id": "2013-2-vr21",
    "vak_code_in_pdf": "2.1",
    "vak_naam_in_pdf": "Personenbelasting",
    "vraagtekst": "Vraag 1 … / 6 punten\nDhr. en mevr. Martin zijn in de loop van 2012 gescheiden met onderlinge toestemming. Dhr.\nMartin is geboren op 15 juli 1963 en mevr. Martin op 10 juni 1975.\nEr werd overeengekomen dat dhr. Martin op 1 december 2012 een éénmalige\nonderhoudsuitkering onder de vorm van een kapitaal",
    "themas": [
      "onderhoudsuitkering"
    ]
  },
  {
    "id": "2013-2-vr22",
    "vak_code_in_pdf": "2.1",
    "vak_naam_in_pdf": "Personenbelasting",
    "vraagtekst": "Vraag 2 … / 10 punten\nEen osteopaat oefent zijn zelfstandige activiteit uit in 2 verschillende sectoren: bij\nprivépatiënten (op hun thuisadres en in zijn praktijk) en als verzorger van een rugbyploeg.\nZijn beroepsmatige verplaatsingen zijn de volgende:\na) van maandag tot vrijdag met zijn personenwag",
    "themas": [
      "personenwagen-btw"
    ]
  },
  {
    "id": "2013-2-vr23",
    "vak_code_in_pdf": "2.1",
    "vak_naam_in_pdf": "Personenbelasting",
    "vraagtekst": "Vraag 3 … / 4 punten\nGeef aan of volgende uitspraken waar of niet waar zijn. Zet een kruisje bij het juiste\nantwoord.\na) Anna is advocate. In 2012 heeft zij gedurende 6 maanden niet kunnen werken wegens\neen ernstige ziekte. Omdat zij een verzekering van het type “gewaarborgd inkomen”\nhad afgesloten,",
    "themas": []
  },
  {
    "id": "2013-2-vr24",
    "vak_code_in_pdf": "2.2",
    "vak_naam_in_pdf": "Vennootschapsbelasting",
    "vraagtekst": "Vraag 1 … / 10 punten\nEen vennootschap ABC heeft de volgende balans- en resultatenrekeningen per 31 december\n2012:\nACTIVA JAAR JAAR PASSIVA JAAR JAAR\n2012 2011 2012 2011\nMateriële vaste activa 15.000 20.000 Geplaatst 60.000 60.000\nkapitaal\nVorderingen < jaar 100.000 95.000 Wettelijke 6.000 6.000\nres",
    "themas": [
      "personenwagen-btw",
      "voorzieningen",
      "vennootschapsbelasting",
      "afschrijvingen",
      "vennootschapsrecht"
    ]
  },
  {
    "id": "2013-2-vr25",
    "vak_code_in_pdf": "2.2",
    "vak_naam_in_pdf": "Vennootschapsbelasting",
    "vraagtekst": "Vraag 2 … / 10 punten\nDe vennootschap GOODLUCK heeft een deel van haar middelen geïnvesteerd in een\naandelenportefeuille.\nIn het boekjaar 2012 zijn er de volgende wijzigingen geweest:\nDatum Omschrijving Bedrag Datum Verkoopprijs Kosten\naanschaf verkoop (bruto) verkoop\n01/02/2010 Colruyt 15.000\n01/03",
    "themas": [
      "beleggingsportefeuille",
      "vennootschapsrecht",
      "reserves",
      "beleggingsportefeuille"
    ]
  },
  {
    "id": "2013-2-vr26",
    "vak_code_in_pdf": "2.3",
    "vak_naam_in_pdf": "Belasting over de toegevoegde waarde",
    "vraagtekst": "Vraag 1 … / 7 punten\nMoet er in het onderstaande geval een herziening van het recht op aftrek gebeuren ? Zo ja,\nbereken het bedrag ervan. Zo neen, zeg waarom.\nAlle bedragen zijn exclusief btw. Motiveer bondig je antwoord.\nEen in België gevestigde kleinhandelaar in algemene levensmiddelen, onderworpe",
    "themas": []
  },
  {
    "id": "2013-2-vr27",
    "vak_code_in_pdf": "2.3",
    "vak_naam_in_pdf": "Belasting over de toegevoegde waarde",
    "vraagtekst": "Vraag 2 … / 8 punten\na) De BVBA ‘A’ (gewone belastingplichtige) stelt een nieuwe personenwagen ter\nbeschikking van de zaakvoerder. De aankoopprijs bedraagt 25 000,00 EUR exclusief\nbtw. De zaakvoerder gebruikt de wagen zowel voor privé- als voor beroepsdoeleinden.\nTijdens het jaar 2013 heeft de zaakv",
    "themas": [
      "personenwagen-btw",
      "vennootschapsrecht"
    ]
  },
  {
    "id": "2013-2-vr28",
    "vak_code_in_pdf": "2.4",
    "vak_naam_in_pdf": "Beginselen van registratie- en successierechten",
    "vraagtekst": "Vraag 1 … / 5 punten\nDhr. André, weduwnaar, is op 1 augustus 2012 tijdens de vakantie in Spanje overleden.\nHij heeft 2 kinderen als erfgenaam: dochter Hélène en zoon Johan.\nHij had zijn fiscale woonplaats in Luik.\nAangaande de elementen in het passief van de nalatenschap:\n- Kruis aan of de elementen",
    "themas": [
      "successierechten",
      "vennootschapsrecht"
    ]
  },
  {
    "id": "2013-2-vr29",
    "vak_code_in_pdf": "2.4",
    "vak_naam_in_pdf": "Beginselen van registratie- en successierechten",
    "vraagtekst": "Vraag 2 … / 5 punten\nAnne, Bernadette en Caroline zijn 3 zussen en in onverdeeldheid eigenaar (elk voor 1/3) van\neen appartementsgebouw in Brussel.\nZe zijn eigenaar geworden van dit gebouw na het overlijden van hun ouders (overleden in\n2007). Bij het overlijden werd het gebouw geschat op € 1.200.000",
    "themas": [
      "registratierechten",
      "vennootschapsrecht"
    ]
  },
  {
    "id": "2013-2-vr30",
    "vak_code_in_pdf": "2.6",
    "vak_naam_in_pdf": "Beginselen van Europees en internationaal fiscaal recht",
    "vraagtekst": "Vraag 1 … / 5 punten\nEen naamloze vennootschap naar Belgisch recht die haar boekjaar afsluit op 31 december, is\nin Italië actief via een bijkantoor dat goederen verkoopt aan in Italië gevestigde klanten. Het\nbijkantoor neemt bestellingen op, keurt ze goed, reikt facturen uit aan de klanten, levert d",
    "themas": [
      "internationaal-fiscaal-recht",
      "vennootschapsbelasting",
      "vennootschapsrecht"
    ]
  },
  {
    "id": "2013-2-vr31",
    "vak_code_in_pdf": "2.6",
    "vak_naam_in_pdf": "Beginselen van Europees en internationaal fiscaal recht",
    "vraagtekst": "Vraag 2 … / 5 punten\nEen natuurlijke persoon die als particulier handelt en fiscaal als een inwoner van België\nwordt beschouwd zet u de volgende toestand uiteen: hij houdt een bankrekening aan in het\nGroothertogdom Luxemburg en heeft in 2013 op die rekening in het Groothertogdom\ninteresten van oblig",
    "themas": [
      "roerende-voorheffing",
      "internationale-belasting"
    ]
  },
  {
    "id": "2013-2-vr32",
    "vak_code_in_pdf": "2.7",
    "vak_naam_in_pdf": "Fiscale procedure",
    "vraagtekst": "Vraag 1 … / 6 punten\nEén van uw cliënten – een verwarmingsinstallateur – ontvangt op 10 september 2013 een\nvraag om inlichtingen, luidende als volgt (nb: Het gaat hier over een aanvraag van\ninlichtingen betreffende een derde):\n“Gelieve mij de volgende inlichtingen mede te delen:\n- de volledige ident",
    "themas": [
      "fiscale-procedure",
      "vennootschapsrecht"
    ]
  },
  {
    "id": "2013-2-vr33",
    "vak_code_in_pdf": "2.7",
    "vak_naam_in_pdf": "Fiscale procedure",
    "vraagtekst": "Vraag 2 … / 4 punten\nGeef aan of onderstaande uitspraken waar of niet waar zijn:\na) Met betrekking tot de roerende voorheffing, kan enkel de schuldenaar van de\nvoorheffing (degene die de voorheffing moet inhouden) een bezwaarschrift indienen.\nDe verkrijger van de inkomsten waarop de voorheffing werd",
    "themas": [
      "roerende-voorheffing",
      "belastingprocedure"
    ]
  },
  {
    "id": "2013-2-vr34",
    "vak_code_in_pdf": "2.7",
    "vak_naam_in_pdf": "Fiscale procedure",
    "vraagtekst": "Vraag 3 … / 5 punten\nEen gewone btw-belastingplichtige gevestigd in België koopt goederen in Duitsland. De\ngoederen komen op 14/11/2012 aan bij de Belgische koper. Het vervoer werd verricht door\neen vervoeronderneming in opdracht van de Duitse verkoper. De factuur wordt toegestuurd\nen ontvangen door",
    "themas": [
      "fiscale-procedure"
    ]
  },
  {
    "id": "2013-2-vr35",
    "vak_code_in_pdf": "4.0",
    "vak_naam_in_pdf": "Juridische en beroepsnormen / deontologie",
    "vraagtekst": "Vraag 1 …. / 4 punten\nEen lid IAB heeft in 2013 volgende vormingsactiviteiten gevolgd:\n1) een seminarie georganiseerd door het IAB,\n2) een opleiding die werd verstrekt door het kantoor van accountants en\nbelastingconsulenten waar hij werkzaam is en die geen erkenning als\nvormingsoperator aanvroeg\n3)",
    "themas": [
      "beroepsnormen",
      "vennootschapsrecht"
    ]
  },
  {
    "id": "2013-2-vr36",
    "vak_code_in_pdf": "4.0",
    "vak_naam_in_pdf": "Juridische en beroepsnormen / deontologie",
    "vraagtekst": "Vraag 2 …. / 7 punten\nOp uw kantoor biedt zich de heer Silan aan die u vertelt dat hij zaakvoerder is van de bvba\nWitwassen en dat de activiteit van deze bvba een keten van wassalons is. Hij vraagt dat u in\nde toekomst de boekhouding en alle daaraan verbonden activiteiten zou overnemen van een\nander",
    "themas": [
      "antiwitwaswet",
      "vennootschapsrecht"
    ]
  },
  {
    "id": "2013-2-vr37",
    "vak_code_in_pdf": "4.0",
    "vak_naam_in_pdf": "Juridische en beroepsnormen / deontologie",
    "vraagtekst": "Vraag 3 …. / 4 punten\nIn de relatie met confraters wordt u soms geconfronteerd met het feit dat u een dossier\noverneemt of dat u zelf een dossier dient over te dragen.\nWelke van onderstaande stellingen zijn juist of fout?\na) Indien een cliënt al uw erelonen nog niet heeft betaald, bent u toch verpli",
    "themas": [
      "beroepsnormen",
      "jaarverslag"
    ]
  },
  {
    "id": "2013-2-vr38",
    "vak_code_in_pdf": "4.0",
    "vak_naam_in_pdf": "Juridische en beroepsnormen / deontologie",
    "vraagtekst": "Vraag 4 …. / 5 punten\nKan u in volgende situatie als externe accountant een monopolieopdracht aanvaarden?\na) U bent werkzaam in een accountantskantoor en één van uw collega accountants\nbinnen hetzelfde kantoor vraagt om een verslag op te maken in het kader van een\nomvorming van één van de dossiers d",
    "themas": [
      "omzetting-vennootschap",
      "onafhankelijkheid",
      "vennootschapsrecht"
    ]
  },
  {
    "id": "2014-1-vr1",
    "vak_code_in_pdf": "1.1",
    "vak_naam_in_pdf": "Wetgeving inzake de jaarrekening",
    "vraagtekst": "Vraag 1 … / 2 punten\nVennootschap PETRUS BVBA sluit haar jaarrekening af op 31 december. De vennootschap\nwou gebruik maken van de nieuwe maatregel rond het vastklikken van reserves.\nOp 20 december 2013 heeft een bijzondere algemene vergadering de beslissing genomen om\neen gedeelte van de reserves ui",
    "themas": [
      "kapitaaloperaties",
      "roerende-voorheffing",
      "vennootschapsrecht",
      "reserves"
    ]
  },
  {
    "id": "2014-1-vr2",
    "vak_code_in_pdf": "1.1",
    "vak_naam_in_pdf": "Wetgeving inzake de jaarrekening",
    "vraagtekst": "Vraag 2 … / 2 punten\nVoor de vennootschap ABC is er een authentieke akte verleden voor een kapitaalverhoging.\nDe kapitaalverhoging is doorgevoerd door enerzijds een incorporatie van bestaande reserves\nen anderzijds een inbreng in speciën. Voor dit laatste lag de uitgifteprijs van de nieuwe\naandelen ",
    "themas": [
      "kapitaaloperaties",
      "financiële-begrippen"
    ]
  },
  {
    "id": "2014-1-vr3",
    "vak_code_in_pdf": "1.1",
    "vak_naam_in_pdf": "Wetgeving inzake de jaarrekening",
    "vraagtekst": "Vraag 3 … / 8 punten\nVennootschap Immo-C had in 1980 een herwaardering toegepast op een octrooi. De\nherwaardering bedroeg 25.000 EUR en werd op rekening 120 van het passief van de balans\ngeboekt. Het octrooi werd oorspronkelijk verworven voor 75.000 EUR.\nHet octrooi is thans volledig afgeschreven.\nO",
    "themas": [
      "herwaarderingsmeerwaarden",
      "afschrijvingen",
      "herwaarderingsmeerwaarden"
    ]
  },
  {
    "id": "2014-1-vr4",
    "vak_code_in_pdf": "1.1",
    "vak_naam_in_pdf": "Wetgeving inzake de jaarrekening",
    "vraagtekst": "Vraag 4 … / 3 punten\nVennootschap Export heeft op 5 februari 2014 een goed verkocht tegen de prijs van\n5.000.000 EUR.\nHet contract voorziet in de betaling van dit bedrag in 5 jaarlijkse stortingen van 1.000.000\nEUR.\nWegens de toegestane betalingstermijn, werd de verkoopprijs van het goed verhoogd me",
    "themas": []
  },
  {
    "id": "2014-1-vr5",
    "vak_code_in_pdf": "1.2",
    "vak_naam_in_pdf": "Analyse en kritische beoordeling van de jaarrekening",
    "vraagtekst": "Vraag 1 … / 8 punten\nIn bijlage vindt U de balans na winstverdeling en de resultatenrekening van een cliënt. Kruis\nhet juiste antwoord aan voor de ratio’s van het BOEKJAAR.\nUit de toelichting tot de jaarrekening blijkt o.a. dat :\n1. Er tijdens het boekjaar investeringen in materiële vaste activa wer",
    "themas": [
      "jaarrekeninganalyse",
      "vennootschapsrecht"
    ]
  },
  {
    "id": "2014-1-vr6",
    "vak_code_in_pdf": "1.2",
    "vak_naam_in_pdf": "Analyse en kritische beoordeling van de jaarrekening",
    "vraagtekst": "Vraag 2 … / 5 punten\na) Omschrijf het begrip “nettothesaurie”.\nAntwoord\nb) Als u de nettothesaurie berekent en de uitkomst is positief, wat betekent dit dan ?\nAntwoord",
    "themas": [
      "werkkapitaalbehoefte"
    ]
  },
  {
    "id": "2014-1-vr9",
    "vak_code_in_pdf": "1.3 IC",
    "vak_naam_in_pdf": "Interne controle",
    "vraagtekst": "Vraag 1 … / 10 punten\nDuid met een kruis aan of de volgende omschrijvingen juist of fout zijn in het kader van de\nalgemene interne controle doelstellingen met betrekking tot de boekhoudkundige registratie.\nAntwoord\nOMSCHRIJVING JUIST FOUT\nTransacties worden uitgevoerd in overeenstemming met de\ndoor ",
    "themas": [
      "interne-controle",
      "vennootschapsrecht"
    ]
  },
  {
    "id": "2014-1-vr10",
    "vak_code_in_pdf": "1.3 IC",
    "vak_naam_in_pdf": "Interne controle",
    "vraagtekst": "Vraag 2 … / 9 punten\nDe verkoopafdeling maakt de nieuwe klantenfiches aan in het computersysteem op het\nmoment dat de verkoper een door een nieuwe klant getekende bestelbon binnenbrengt.\nDetecteer drie risico's.\nAntwoord",
    "themas": [
      "interne-controle"
    ]
  },
  {
    "id": "2014-1-vr11",
    "vak_code_in_pdf": "1.3 IC",
    "vak_naam_in_pdf": "Interne controle",
    "vraagtekst": "Vraag 3 … / 6 punten\nDe secretaresse van de zaakvoerder betaalt kleine kosten gemaakt door het personeel terug\nvia een kas.\nStel een procedure op waarbij minimaal twee controletechnische functiescheidingen in\nvoorkomen.\nAntwoord",
    "themas": [
      "interne-controle"
    ]
  },
  {
    "id": "2014-1-vr12",
    "vak_code_in_pdf": "1.3 AO",
    "vak_naam_in_pdf": "Accountantsonderzoek",
    "vraagtekst": "Vraag 1 … / 8 punten\nEr worden onvoldoende antwoorden ontvangen op de confirmatie- of bevestigingsbrieven\nwelke verzonden werden aan de klanten.\na) Moeten we daarvoor een voorbehoud in ons verslag maken ?\nAntwoord\nb) Welke acties kan men ondernemen om aan dit onvoldoende aantal antwoorden te\nremedië",
    "themas": [
      "confirmatiebrieven",
      "vennootschapsrecht"
    ]
  },
  {
    "id": "2014-1-vr13",
    "vak_code_in_pdf": "1.3 AO",
    "vak_naam_in_pdf": "Accountantsonderzoek",
    "vraagtekst": "Vraag 2 … / 3 punten\nBij nazicht van de resultatenrekening komen we op de kostenrekening “erelonen advocaat”\nten belope van 12.000,00 EUR.\nWaarom is dit van belang voor het controleverslag?\nWelke actie stel je voor ?\nAntwoord",
    "themas": [
      "auditopdracht"
    ]
  },
  {
    "id": "2014-1-vr14",
    "vak_code_in_pdf": "1.3 AO",
    "vak_naam_in_pdf": "Accountantsonderzoek",
    "vraagtekst": "Vraag 3 … / 14 punten\nIn het kader van een controleopdracht waarvoor een volkomen controle vereist is ontvangen\nwe tijdens onze audit ter plaatse op 20/02/2014 van de interne boekhouder de\nboekhoudkundige staat per 31/12/2013. Zoals je weet moeten er voor we op de cijfers\n“afstormen” een aantal voor",
    "themas": [
      "sociale-bijdragen"
    ]
  },
  {
    "id": "2014-1-vr15",
    "vak_code_in_pdf": "3.1",
    "vak_naam_in_pdf": "Vennootschapsrecht",
    "vraagtekst": "Vraag 1 … / 4 punten\nKruis de juiste antwoorden aan in onderstaande tabel:\n1. In welke vennootschap zijn de vennoten/aandeelhouders hoofdelijk aansprakelijk voor de\nschulden van hun vennootschap?\n2. Welke vennootschap kan winstbewijzen toekennen?\n3. Welke vennootschap is verplicht haar jaarrekening ",
    "themas": [
      "vennootschapsrecht"
    ]
  },
  {
    "id": "2014-1-vr16",
    "vak_code_in_pdf": "3.1",
    "vak_naam_in_pdf": "Vennootschapsrecht",
    "vraagtekst": "Vraag 2 … / 4 punten\nDe gedelegeerd bestuurder van de nv PILOTE (opgericht in 1992) raadpleegt u met volgende\ncijfers van de laatste balans (31/12/2013):\nPassiva\n100 Geplaatst kapitaal 1.000.000,00 EUR\n130 Wettelijke reserve 100.000,00 EUR\n133 Beschikbare reserves 5.000.000,00 EUR\n170 Verplichtingen",
    "themas": [
      "kapitaaloperaties",
      "vennootschapsrecht",
      "sociale-bijdragen",
      "reserves"
    ]
  },
  {
    "id": "2014-1-vr17",
    "vak_code_in_pdf": "3.1",
    "vak_naam_in_pdf": "Vennootschapsrecht",
    "vraagtekst": "Vraag 3 … / 4 punten\nDhr. LEVEQUE, enig vennoot en zaakvoerder van de bvba PETIT POIS (opgericht in 2009),\nraadpleegt u in verband met te verrichten investeringen.\nHij wil het gebouw, dat zijn persoonlijke eigendom is en door de bvba PETIT POIS wordt\ngebruikt om haar bedrijvigheid uit te oefenen, aa",
    "themas": [
      "vennootschapsrecht"
    ]
  },
  {
    "id": "2014-1-vr18",
    "vak_code_in_pdf": "3.1",
    "vak_naam_in_pdf": "Vennootschapsrecht",
    "vraagtekst": "Vraag 4 … / 4 punten\nDe heer KALO Ric gedelegeerd bestuurder van de nv MINCALOR, handel in dieetproducten,\nen hoofdaandeelhouder, raadpleegt u.\nDe heer KALO Ric heeft een aanzienlijk geldbedrag nodig voor een privé-vastgoed\nverrichting.\nHij toont u de statuten van de vennootschap die de raad van bes",
    "themas": [
      "dividend",
      "vennootschapsrecht",
      "sociale-bijdragen",
      "reserves"
    ]
  },
  {
    "id": "2014-1-vr19",
    "vak_code_in_pdf": "3.1",
    "vak_naam_in_pdf": "Vennootschapsrecht",
    "vraagtekst": "Vraag 5 … / 4 punten\nDe heer LEGRAND Alexandre is samen met zijn broer Luigi vennoot in de vennootschappen\n\"Mise en Trop\" bvba en \"Coté Pratique\" bvba in Brussel.\nVennootschap \"Mise en Trop\" bvba stelt 39 voltijdse personeelsleden tewerk in de\ninformaticasector. Vennootschap \"Coté Pratique\" bvba ste",
    "themas": [
      "vennootschapsrecht"
    ]
  },
  {
    "id": "2014-1-vr20",
    "vak_code_in_pdf": "3.2",
    "vak_naam_in_pdf": "Vennootschapsrecht (bijzondere mandaten)",
    "vraagtekst": "Vraag 1 …/ 10 punten\nDe heer FIXIT een externe accountant. De gedelegeerde bestuurder van die vennootschap\nwenst de vennootschap NV TRIAL om te zetten in een BVBA en geeft de heer FIXIT de\nopdracht dit te doen.\nOPMERKING: bij de vragen waar juist / fout moet geantwoord worden maak je bij voorkeur\nhe",
    "themas": [
      "omzetting-vennootschap",
      "afschrijvingen",
      "vennootschapsrecht",
      "continuiteitsbeginsel"
    ]
  },
  {
    "id": "2014-1-vr21",
    "vak_code_in_pdf": "3.2",
    "vak_naam_in_pdf": "Vennootschapsrecht (bijzondere mandaten)",
    "vraagtekst": "Vraag 2 …/ 20 punten\nTwee broers doen sedert een drietal jaar goede zaken met hun VOF STORE en wensen alvoor\nze verder investeren en personeel aanwerven de vennootschap om te zetten naar een BVBA.\nZe leggen volgende balans per 31/12/2013 voor.\nVOF STORE BALANS 31/12/2013\n23 Installaties en machines ",
    "themas": [
      "omzetting-vennootschap",
      "vennootschapsrecht",
      "reserves"
    ]
  },
  {
    "id": "2014-1-vr22",
    "vak_code_in_pdf": "2.1",
    "vak_naam_in_pdf": "Personenbelasting",
    "vraagtekst": "Vraag 1 … / 3 punten\nPersonen ten laste\nWelke personen, omschreven in onderstaande uitspraken, kunnen niet als persoon ten laste\nworden beschouwd?\nAntwoord\n\nDe afstammelingen van de belastingplichtige of zijn echtgenoot, met name de kinderen of\ngeadopteerde kinderen, kleinkinderen, achterkleinkinde",
    "themas": [
      "vennootschapsrecht"
    ]
  },
  {
    "id": "2014-1-vr23",
    "vak_code_in_pdf": "2.1",
    "vak_naam_in_pdf": "Personenbelasting",
    "vraagtekst": "Vraag 2 … / 3 punten\nHuwelijksquotiënt\nWelke van onderstaande uitspraken is niet juist?\nAntwoord\n\nHet huwelijksquotiënt is een regel die enkel de belastingplichtigen betreft die een\ngezamenlijke aangifte moeten indienen.\n\nWanneer één van beide echtgenoten geen beroepsinkomsten of onroerende inkoms",
    "themas": [
      "personenbelasting"
    ]
  },
  {
    "id": "2014-1-vr24",
    "vak_code_in_pdf": "2.1",
    "vak_naam_in_pdf": "Personenbelasting",
    "vraagtekst": "Vraag 3 … / 4 punten\nOnroerende inkomsten\nPaul en Jeanne, zonder kinderen, bezitten een in België gelegen gebouw met een niet-\ngeïndexeerd kadastraal inkomen (KI) van 5.000 EUR. Het gebouw werd in 2002 aangekocht\nmet een hypothecaire lening die een belastingvoordeel oplevert. De fiscale behandeling ",
    "themas": [
      "personenbelasting"
    ]
  },
  {
    "id": "2014-1-vr25",
    "vak_code_in_pdf": "2.1",
    "vak_naam_in_pdf": "Personenbelasting",
    "vraagtekst": "Vraag 4 … / 3 punten\nDiverse inkomsten\nWelke van de hierna omschreven inkomsten vallen onder de categorie van de diverse\ninkomsten bedoeld in 90, 1° WIB 1992?\nAntwoord\n\nerelonen voor advies verstrekt buiten het kader van een echt beroep;\n\nprijzen van tombola's en toegelaten loterijen, met inbegrip",
    "themas": [
      "personenbelasting"
    ]
  },
  {
    "id": "2014-1-vr26",
    "vak_code_in_pdf": "2.1",
    "vak_naam_in_pdf": "Personenbelasting",
    "vraagtekst": "Vraag 5 … / 3 punten\nWelke hieronder omschreven meerwaarden zijn belastbaar tegen de afzonderlijke\naanslagvoet van 33%, tenzij de samenvoeging voordeliger is?\nAntwoord\n\nMeerwaarden verwezenlijkt op activa die niet voor de uitoefening van de\nberoepswerkzaamheid werden gebruikt en betrekking hebben o",
    "themas": [
      "immateriële-vaste-activa",
      "vennootschapsrecht"
    ]
  },
  {
    "id": "2014-1-vr27",
    "vak_code_in_pdf": "2.1",
    "vak_naam_in_pdf": "Personenbelasting",
    "vraagtekst": "Vraag 6 … / 4 punten\nAftrekbare uitgaven\nWelke van onderstaande uitspraken is niet juist voor het aanslagjaar 2013?\nAntwoord\n\nDe uitgaven die recht geven op belastingverminderingen mogen nog niet afgetrokken zijn bij\nde vaststelling van de netto-inkomsten, zo niet kunnen ze niet in aanmerking worde",
    "themas": [
      "onderhoudsuitkering",
      "vennootschapsrecht"
    ]
  },
  {
    "id": "2014-1-vr28",
    "vak_code_in_pdf": "2.2",
    "vak_naam_in_pdf": "Vennootschapsbelasting",
    "vraagtekst": "Vraag 1 … / 12 punten\nEen kantoorgebouw was door de vennootschap ABC gekocht in het jaar 1985. Volgende\ngegevens zijn terug te vinden in de afschrijvingstabel:\nAanschaffingwaarde 1.000.000,00 EUR\nAfschrijvingen - 750.000,00 EUR\nBoekwaarde 250.000,00 EUR\nDe vennootschap probeerde, na schatting door e",
    "themas": [
      "gespreide-taxatie",
      "afschrijvingen",
      "vennootschapsrecht"
    ]
  },
  {
    "id": "2014-1-vr29",
    "vak_code_in_pdf": "2.2",
    "vak_naam_in_pdf": "Vennootschapsbelasting",
    "vraagtekst": "Vraag 2 … / 8 punten\nDe vennootschap ABC heeft het volgende eigen vermogen:\nJaar 2012 Jaar 2011\nGeplaatst kapitaal Oprichting 1989 in 20.000 20.000\nspeciën\nInbreng in natura 80.000 0\nop 14/03/2012\nIncorporatie 50.000 0\nbeschikbare\nreserves op\n14/03/2012\nWettelijke reserve 10.000 2.000\nBeschikbare 0 ",
    "themas": [
      "voorzieningen",
      "vennootschapsbelasting",
      "interne-pensioenbelofte",
      "inbreng-in-natura",
      "reserves"
    ]
  },
  {
    "id": "2014-1-vr30",
    "vak_code_in_pdf": "2.3",
    "vak_naam_in_pdf": "Belasting over de toegevoegde waarde",
    "vraagtekst": "Vraag 1 … / 3 punten\nEen in Welkenraedt gevestigde onderneming, gespecialiseerd in dakwerken, bouwt het\ndakgebinte en de dakbedekking van een zwembad in München (Duitsland), tegen de prijs van\n10.000 EUR. De eigenaar is een Oostenrijkse particulier.\nDuid de goede oplossing aan.\nAntwoord\n\nDe btw is ",
    "themas": [
      "btw-plaatsbepaling"
    ]
  },
  {
    "id": "2014-1-vr31",
    "vak_code_in_pdf": "2.3",
    "vak_naam_in_pdf": "Belasting over de toegevoegde waarde",
    "vraagtekst": "Vraag 2 … / 3 punten\nEen fabrikant van industriële aanhangwagens, een gewone belastingplichtige en gevestigd in\nVilvoorde, wordt failliet verklaard. De voorraad aanhangwagens en het exploitatiemateriaal\nvan de onderneming worden, op verzoek van de door de rechtbank van koophandel van\nBrussel aangest",
    "themas": [
      "btw-bijzondere-regelingen"
    ]
  },
  {
    "id": "2014-1-vr32",
    "vak_code_in_pdf": "2.3",
    "vak_naam_in_pdf": "Belasting over de toegevoegde waarde",
    "vraagtekst": "Vraag 3 … / 3 punten\nSophie, intern boekhoudster bij de firma ElectroStar, groothandel in huishoudtoestellen in\nBrussel, doet sinds een jaar, als zelfstandige in bijberoep (na haar dagtaak), de boekhouding\nvan de firma Libro, een ijzerwinkel in Brussel.\nIn 2013 ontvangt ze daarvoor 1.500 EUR per maa",
    "themas": [
      "personenbelasting"
    ]
  },
  {
    "id": "2014-1-vr33",
    "vak_code_in_pdf": "2.3",
    "vak_naam_in_pdf": "Belasting over de toegevoegde waarde",
    "vraagtekst": "Vraag 4 … / 3 punten\nJulien, bediende bij een bank in België, doet een beroep op een in Charleroi gevestigde\nzelfstandige accountant (gewone belastingplichtige) om zijn belastingaangifte op te stellen.\nDe accountant stelt die belastingaangifte op in de trein, op weg naar een conferentie in\nParijs, e",
    "themas": []
  },
  {
    "id": "2014-1-vr34",
    "vak_code_in_pdf": "2.3",
    "vak_naam_in_pdf": "Belasting over de toegevoegde waarde",
    "vraagtekst": "Vraag 5 … / 3 punten\nEen in Londen gevestigde hotelonderneming, die onder meer een hotel uitbaat in Coventry\n(Groot-Brittannië), bestelt bij het Brussels reclameblad Publi-Magazine een advertentie van\neen halve bladzijde om de prijzen van haar hotel in de Paasvakantie te promoten. De prijs die\nPubli",
    "themas": []
  },
  {
    "id": "2014-1-vr35",
    "vak_code_in_pdf": "2.4",
    "vak_naam_in_pdf": "Beginselen van registratie- en successierechten",
    "vraagtekst": "Vraag 1 … / 5 punten\nDe BVBA Mokka zou het aanpalende terrein, gelegen aan de achterzijde van haar\nbedrijfsgebouw, willen aankopen om er een opslagplaats te bouwen.\nAls de eigenaar te weten komt dat de BVBA geïnteresseerd is in de grond, is het zeer\nwaarschijnlijk dat hij daarvan zal profiteren om d",
    "themas": [
      "vennootschapsrecht"
    ]
  },
  {
    "id": "2014-1-vr36",
    "vak_code_in_pdf": "2.4",
    "vak_naam_in_pdf": "Beginselen van registratie- en successierechten",
    "vraagtekst": "Vraag 2 … / 5 punten\nDe heer Janssens is in België overleden op 12 augustus 2012.\nBij zijn overlijden was de heer Janssens gehuwd met Anne en had het echtpaar slechts één\ndochter die, op de dag van het overlijden, meerderjarig was.\nDe echtgenoten waren gehuwd onder het stelsel van de scheiding van g",
    "themas": [
      "successierechten"
    ]
  },
  {
    "id": "2014-1-vr37",
    "vak_code_in_pdf": "2.6",
    "vak_naam_in_pdf": "Beginselen van Europees en internationaal fiscaal recht",
    "vraagtekst": "Vraag 1 … / 6 punten\nEen Belgische verblijfhoudende vennootschap is in Italië actief via een vaste inrichting (VI).\nTussen Italië en België geldt een bilaterale overeenkomst tot het vermijden van dubbele\nbelasting.\nVI Italië Belg.verrichtingen Totaal Vennootschap\nJaar 1: Resultaat vóór belasting Ver",
    "themas": [
      "internationaal-fiscaal-recht"
    ]
  },
  {
    "id": "2014-1-vr38",
    "vak_code_in_pdf": "2.6",
    "vak_naam_in_pdf": "Beginselen van Europees en internationaal fiscaal recht",
    "vraagtekst": "Vraag 2 … / 4 punten\nEen vennootschap naar Belgisch recht, zonder bijkantoor noch vaste inrichting in het\nbuitenland, wordt overgenomen door een vennootschap naar Duits recht. De Belgische\nvennootschap had verrekenbare fiscale verliezen die zij nog niet van de latere winsten had\nkunnen aftrekken.\na)",
    "themas": [
      "internationaal-fiscaal-recht"
    ]
  },
  {
    "id": "2014-1-vr39",
    "vak_code_in_pdf": "2.7",
    "vak_naam_in_pdf": "Fiscale procedure",
    "vraagtekst": "Vraag 1 … / 6 punten\nEén van uw cliënten – de BVBA “Souris” die een winkel uitbaat van informaticamateriaal –\nontvangt op 2 februari 2014 een vraag om inlichtingen, luidende als volgt:\n“Gelieve mij de volgende inlichtingen mede te delen betreffende derden:\n- de volledige identiteit van al uw leveran",
    "themas": [
      "fiscale-procedure",
      "vennootschapsrecht"
    ]
  },
  {
    "id": "2014-1-vr40",
    "vak_code_in_pdf": "2.7",
    "vak_naam_in_pdf": "Fiscale procedure",
    "vraagtekst": "Vraag 2 … / 4 punten\nGeef aan of onderstaande uitspraken waar of niet waar zijn:\na) Met betrekking tot de roerende voorheffing, kan enkel de schuldenaar van de\nvoorheffing (degene die de voorheffing moet inhouden) een bezwaarschrift indienen.\nDe verkrijger van de inkomsten waarop de voorheffing werd",
    "themas": [
      "roerende-voorheffing",
      "belastingprocedure"
    ]
  },
  {
    "id": "2014-1-vr41",
    "vak_code_in_pdf": "2.7",
    "vak_naam_in_pdf": "Fiscale procedure",
    "vraagtekst": "Vraag 3 … / 5 punten\nDe btw controle stuurt aan een accountantskantoor een schriftelijke vraag om inlichtingen\nm.b.t. de btw-activiteiten van een van de klanten (vennootschap) van het kantoor. Moet het\nkantoor hierop antwoorden en binnen welke termijn? Duid het juiste antwoord aan.\n\nHet accountants",
    "themas": [
      "fiscale-procedure"
    ]
  },
  {
    "id": "2014-1-vr42",
    "vak_code_in_pdf": "4.0",
    "vak_naam_in_pdf": "Juridische en beroepsnormen / deontologie",
    "vraagtekst": "Vraag 1 …. / 3 punten\nHet principe van de kwaliteitstoetsing is dat iedere accountant om de zeven jaar op\nkantoorniveau zou gecontroleerd worden. Dit betreft de periodieke toetsing. Daarnaast zijn er\nnog drie andere soorten toetsing, namelijk “de vervolgtoetsing”, “de thematische toetsing”\nen “de In",
    "themas": [
      "antiwitwaswet",
      "beroepsnormen",
      "vennootschapsrecht"
    ]
  },
  {
    "id": "2014-1-vr43",
    "vak_code_in_pdf": "4.0",
    "vak_naam_in_pdf": "Juridische en beroepsnormen / deontologie",
    "vraagtekst": "Vraag 2 …. / 4 punten\nOp uw kantoor biedt zich een nieuwe klant aan die de opvolging van zijn vennootschap wil\nlaten overnemen door uw kantoor. Tijdens dit gesprek komen de volgende punten aan bod.\nGeef aan wanneer u zich niet akkoord kan verklaren met de besproken punten en licht kort\ntoe waarom u ",
    "themas": [
      "btw-aangifte"
    ]
  },
  {
    "id": "2014-1-vr44",
    "vak_code_in_pdf": "4.0",
    "vak_naam_in_pdf": "Juridische en beroepsnormen / deontologie",
    "vraagtekst": "Vraag 3 …. / 5 punten\nIn het kader van de samenwerkingsverbanden zijn er sinds 2010 een aantal nieuwe regels.\nZeg voor de onderstaande gevallen of deze situatie juist of fout is:\na) Een middelenvennootschappen kan enkel opgericht worden met confraters IAB.\nJuist\nFout\nb) De stemrechten van een profes",
    "themas": [
      "beroepsnormen",
      "vennootschapsrecht"
    ]
  },
  {
    "id": "2014-1-vr45",
    "vak_code_in_pdf": "4.0",
    "vak_naam_in_pdf": "Juridische en beroepsnormen / deontologie",
    "vraagtekst": "Vraag 4 …. / 3 punten\nIn het KB van 1 maart 1998 wordt eveneens de onafhankelijkheid van de externe\naccountant/belastingconsulent behandeld. In dat kader wordt er ook gesproken over\nmandaten en opdrachten die men niet mag aanvaarden. Geef hierna aan of de stellingen juist\nof fout zijn:\na) Mits voora",
    "themas": [
      "onafhankelijkheid",
      "vennootschapsrecht"
    ]
  },
  {
    "id": "2014-1-vr46",
    "vak_code_in_pdf": "4.0",
    "vak_naam_in_pdf": "Juridische en beroepsnormen / deontologie",
    "vraagtekst": "Vraag 5 …. / 5 punten\nEen confrater, die bij u in de gemeente is gevestigd, vraagt u als extern accountant, voor één\nvan zijn klanten een verslag van omvorming te willen opmaken. Geef aan of u met volgende\nstellingen akkoord kan gaan of niet:\na) U kan deze opdracht aanvaarden gezien er, buiten het f",
    "themas": [
      "omzetting-vennootschap",
      "beroepsnormen",
      "vennootschapsrecht"
    ]
  },
  {
    "id": "2015-1-vr1",
    "vak_code_in_pdf": "1.1",
    "vak_naam_in_pdf": "Wetgeving inzake de jaarrekening",
    "vraagtekst": "Vraag 1 … / 3 punten\nEen onderneming XYZ verkoopt producten voor klein meubilair. Volgens haar\nwaarderingsregels gebruikt zij de FIFO methode.\nZij heeft volgende aankopen en verkopen op één bepaald voorraadartikel verricht tijdens\n2013:\n aankoop op 15 januari 2013 van 1.000 stuks aan 350,00 EUR\n a",
    "themas": []
  },
  {
    "id": "2015-1-vr2",
    "vak_code_in_pdf": "1.1",
    "vak_naam_in_pdf": "Wetgeving inzake de jaarrekening",
    "vraagtekst": "Vraag 2 … / 2 punten\nEen werknemer, de heer Janssens van de vennootschap XYZ, heeft zijn ontslag gekregen\nvan de vennootschap op 5 december 2013, zodat hij op 1 maart 2014 van het stelsel\nwerkloosheid met bedrijfstoeslag (oude brugpensioenstelsel) kan genieten.\nVanaf 1 maart 2014 betaalt de vennoots",
    "themas": [
      "voorzieningen"
    ]
  },
  {
    "id": "2015-1-vr3",
    "vak_code_in_pdf": "1.1",
    "vak_naam_in_pdf": "Wetgeving inzake de jaarrekening",
    "vraagtekst": "Vraag 3 … / 2 punten\nEen vennootschap XYZ heeft een machine verkocht aan een klant voor een bedrag van\n121.000,00 EUR inclusief 21% BTW op 1 juli 2012. De betaling hiervan diende slechts na drie\njaar te gebeuren. Er werd hiervoor een rente gevraagd van 8%, zesmaandelijks te betalen. In\nde boekhoudin",
    "themas": []
  },
  {
    "id": "2015-1-vr4",
    "vak_code_in_pdf": "1.1",
    "vak_naam_in_pdf": "Wetgeving inzake de jaarrekening",
    "vraagtekst": "Vraag 4 … / 2 punten\nIn de boekhouding van de vennootschap van uw cliënt werd onder de rubriek “499 –\nwachtrekening” een bedrag van 125.000,00 EUR opgenomen, met de vermelding “intercalaire\ninteresten per 31/08/2014 op het investeringskrediet 15-237584-22”.\nWelke van onderstaande instructies moet u ",
    "themas": [
      "vennootschapsrecht",
      "intercalaire-intresten"
    ]
  },
  {
    "id": "2015-1-vr5",
    "vak_code_in_pdf": "1.1",
    "vak_naam_in_pdf": "Wetgeving inzake de jaarrekening",
    "vraagtekst": "Vraag 5 … / 2 punten\nEen vennootschap consulteert u omdat zij van plan is te investeren in een nieuw\nproductieapparaat.\nDe kosten van de investering bedragen 80.000 EUR. De vennootschap zou een subsidie van\n12.800 EUR kunnen verkrijgen.\nDie subsidie zou betaald worden in twee stortingen van respecti",
    "themas": [
      "afschrijvingen",
      "vennootschapsrecht",
      "kapitaalsubsidies"
    ]
  },
  {
    "id": "2015-1-vr6",
    "vak_code_in_pdf": "1.1",
    "vak_naam_in_pdf": "Wetgeving inzake de jaarrekening",
    "vraagtekst": "Vraag 6 … / 2 punten\nDe vennootschap “Koffie van het Noorden” heeft beslist om haar afdeling “Fabricatie van\nKoffiemolens” te herstructureren.\nDe gemaakte kosten zijn de volgende:\n Ontmanteling van de bestaande productielijn: 150.000 EUR\n Elektronische automatisatie van de nieuwe productielijn: 30",
    "themas": []
  },
  {
    "id": "2015-1-vr7",
    "vak_code_in_pdf": "1.1",
    "vak_naam_in_pdf": "Wetgeving inzake de jaarrekening",
    "vraagtekst": "Vraag 7 … / 2 punten\nBij de vereffening van een bvba wordt een voorschot op het uiteindelijk te verdelen bedrag\nuitgekeerd. Welke van de onderstaande voorstellen geeft de juiste boekhoudkundige\nverwerking weer?\nA. Het voorschot wordt geboekt op het debet van rekening 100.\nB. Het voorschot wordt gebo",
    "themas": [
      "ontbinding-vereffening",
      "vennootschapsrecht"
    ]
  },
  {
    "id": "2015-1-vr8",
    "vak_code_in_pdf": "1.2",
    "vak_naam_in_pdf": "Analyse en kritische beoordeling van de jaarrekening",
    "vraagtekst": "Vraag 1 … / 8 punten\nIn bijlage vindt U de balans na winstverdeling en de resultatenrekening van een cliënt. Kruis\nhet juiste antwoord aan voor de ratio’s van het BOEKJAAR.\nUit de toelichting tot de jaarrekening blijkt o.a. dat :\n1. Er tijdens het boekjaar investeringen in materiële vaste activa wer",
    "themas": [
      "voorzieningen",
      "jaarrekeninganalyse",
      "vennootschapsrecht"
    ]
  },
  {
    "id": "2015-1-vr9",
    "vak_code_in_pdf": "1.2",
    "vak_naam_in_pdf": "Analyse en kritische beoordeling van de jaarrekening",
    "vraagtekst": "Vraag 2 … / 5 punten\nOmschrijf de volgende begrippen :\na) Intrinsieke waarde\nAntwoord … / 1 punt\nb) Fractiewaarde\nAntwoord … / 1 punt\nc) Netto rendabiliteit van de bedrijfsactiva\nAntwoord … / 1 punt\nd) Algemene schuldgraad\nAntwoord … / 1 punt\ne) Operationele cash flow voor belastingen\nAntwoord … / 1",
    "themas": [
      "financiële-begrippen"
    ]
  },
  {
    "id": "2015-1-vr10",
    "vak_code_in_pdf": "1.2",
    "vak_naam_in_pdf": "Analyse en kritische beoordeling van de jaarrekening",
    "vraagtekst": "Vraag 3 … / 6 punten\nWelke van de onderstaande elementen neemt U op in de berekening “behoefte aan\nwerkkapitaal (of bedrijfskapitaal)”?\nDuid bij elke code “ja of nee” aan. Bij elk foutief antwoord of ontbrekend antwoord, wordt er\néén punt afgetrokken.\nAntwoord … / punten\nCode Ja Neen\nMateriële vaste",
    "themas": [
      "voorzieningen"
    ]
  },
  {
    "id": "2015-1-vr12",
    "vak_code_in_pdf": "1.3 IC",
    "vak_naam_in_pdf": "Interne controle",
    "vraagtekst": "Vraag 1 … / 12 punten\nDe controleactiviteiten kunnen op verschillende wijzen worden ingedeeld.\nVerklaar de volgende begrippen en geef van iedere controleactiviteit een voorbeeld.\na) Accountingcontrole en administratieve contrôle.\nAntwoord … / 6 punten\nb) Preventieve en repressieve controle.\nAntwoord",
    "themas": []
  },
  {
    "id": "2015-1-vr13",
    "vak_code_in_pdf": "1.3 IC",
    "vak_naam_in_pdf": "Interne controle",
    "vraagtekst": "Vraag 2 … / 8 punten\nDe verantwoordelijke van de interne audit zal een aantal controletechnieken aanwenden om\nvoldoende bewijsmateriaal te verzamelen over de toepassing en effectiviteit van de interne\ncontrole maatregelen.\nGeef vier controletechnieken die door de interne controleur kunnen toegepast ",
    "themas": []
  },
  {
    "id": "2015-1-vr14",
    "vak_code_in_pdf": "1.3 IC",
    "vak_naam_in_pdf": "Interne controle",
    "vraagtekst": "Vraag 3 … / 5 punten\nIn onderstaand schema worden een aantal doelstellingen weergegeven die bij de\noperationele audit van de verkoopcyclus van belang zijn.\nDuid bij elke doelstelling aan of het gaat om een financieel, en/of operationeel en/of\nconformiteitsaspect .\nAntwoord\nDoelstelling Financieel Op",
    "themas": [
      "interne-controle"
    ]
  },
  {
    "id": "2015-1-vr15",
    "vak_code_in_pdf": "1.3 AO",
    "vak_naam_in_pdf": "Accountantsonderzoek",
    "vraagtekst": "Vraag 1 … / 2 punten\nTijdens een controleopdracht bij een middelgrote onderneming, zonder commissaris en in\nhet kader van een contractueel beperkt nazicht stelt de externe accountant een aantal\nverbeteringen (adjustments) voor.\na) Wanneer deze adjustments talrijk en substantieel zijn in bedrag, zou ",
    "themas": [
      "auditopdracht"
    ]
  },
  {
    "id": "2015-1-vr16",
    "vak_code_in_pdf": "1.3 AO",
    "vak_naam_in_pdf": "Accountantsonderzoek",
    "vraagtekst": "Vraag 2 … / 4 punten\nEen eerste stap bij het auditwerk is de aanvaardingsprocedure van de opdracht.\nGeef twee voorbeelden van situaties bij deze procedure, waarbij we het dossier mogelijks\nniet kunnen aanvaarden.\nAntwoord",
    "themas": [
      "vennootschapsrecht"
    ]
  },
  {
    "id": "2015-1-vr17",
    "vak_code_in_pdf": "1.3 AO",
    "vak_naam_in_pdf": "Accountantsonderzoek",
    "vraagtekst": "Vraag 3 … / 6 punten\nTijdens de werkzaamheden aan een controleverslag ivm een omzetting stelt de aangestelde\naccountant vast dat op het actief een debet lopende rekening op naam van de overleden\nvader van de zaakvoerders-aandeelhouders voorkomt.\na) Geef twee (2) controledoelstellingen die op dergeli",
    "themas": [
      "omzetting-vennootschap"
    ]
  },
  {
    "id": "2015-1-vr18",
    "vak_code_in_pdf": "1.3 AO",
    "vak_naam_in_pdf": "Accountantsonderzoek",
    "vraagtekst": "Vraag 4 … / 8 punten\nHet is 23 januari 2015 en de onderneming heeft haar boekhouding afgesloten op\n30 september 2014 conform haar statuten. Op 1 oktober 2014 heeft u als controlerende\naccountant de voorraadtelling gevolgd en u ermee akkoord verklaard. Het betreft hier een\nBelgisch bedrijf dat in han",
    "themas": [
      "confirmatiebrieven"
    ]
  },
  {
    "id": "2015-1-vr19",
    "vak_code_in_pdf": "1.3 AO",
    "vak_naam_in_pdf": "Accountantsonderzoek",
    "vraagtekst": "Vraag 5 … / 5 punten\nGeef de werkwijze tijdens een externe controle om tot de confirmatie van een representatief\naantal leverancierssaldi te komen.\na) Wat is representatief?\nAntwoord … / 1 punt\nb) Hoe doe je de steekproef?\nAntwoord … / 1 punt\nc) Hoe gebeurt de verzending van de confirmatiebrieven?\nA",
    "themas": [
      "confirmatiebrieven"
    ]
  },
  {
    "id": "2015-1-vr20",
    "vak_code_in_pdf": "3.1",
    "vak_naam_in_pdf": "Vennootschapsrecht",
    "vraagtekst": "Vraag 1 … / 4 punten\nDe heer DUPONT, zaakvoerder en hoofdaandeelhouder van de S-bvba “LA POINTE” komt u\nop zaterdag 11 april 2015 om advies vragen. De vennootschap werd opgericht in december\n2009.\nHij legt u de jaarrekening per 31 december 2014 voor.\nDie ziet er als volgt uit:\nActiva Passiva\nMaterië",
    "themas": [
      "ontbinding-vereffening",
      "fiscale-verliezen",
      "afschrijvingen",
      "vennootschapsrecht"
    ]
  },
  {
    "id": "2015-1-vr21",
    "vak_code_in_pdf": "3.1",
    "vak_naam_in_pdf": "Vennootschapsrecht",
    "vraagtekst": "Vraag 2 … / 4 punten\nU hebt de balans opgemaakt voor uw cliënt waarbij het eigen vermogen van de bvba als volgt\nis samengesteld:\nGeplaatst Kapitaal: 18.550,00 EUR\nWettelijke reserve: 1.855,00 EUR\nOvergedragen winst: 15.000,00 EUR\nDe zaakvoerder van de bvba wenst de vennootschap om te zetten in een n",
    "themas": [
      "omzetting-vennootschap",
      "kapitaaloperaties",
      "vennootschapsrecht",
      "reserves"
    ]
  },
  {
    "id": "2015-1-vr22",
    "vak_code_in_pdf": "3.1",
    "vak_naam_in_pdf": "Vennootschapsrecht",
    "vraagtekst": "Vraag 3 … / 4 punten\nMet het oog op de voorbereiding van de Algemene Vergadering van 15 mei biedt de\nzaakvoerder van de bvba De Toekomst (die tevens 55% van de aandelen bezit) zich op 25\njanuari 2014 in uw kantoor aan en overhandigt u de financiële staten van de bvba per\n31/12/2013.\nBij nazicht van ",
    "themas": [
      "ontbinding-vereffening",
      "fiscale-verliezen",
      "vennootschapsrecht",
      "reserves"
    ]
  },
  {
    "id": "2015-1-vr23",
    "vak_code_in_pdf": "3.1",
    "vak_naam_in_pdf": "Vennootschapsrecht",
    "vraagtekst": "Vraag 4 … / 4 punten\nHet bestuursorgaan moet jaarlijks de jaarrekening opstellen.\nDe raad van bestuur van uw cliënt, de nv “Option for the Future”, die haar rekeningen afsluit\nop 31/12 van elk jaar, roept de gewone algemene vergadering te laat bijeen en stelt de datum\nvast op 20/07/2014.\nDe redenen ",
    "themas": [
      "vennootschapsrecht"
    ]
  },
  {
    "id": "2015-1-vr24",
    "vak_code_in_pdf": "3.1",
    "vak_naam_in_pdf": "Vennootschapsrecht",
    "vraagtekst": "Vraag 5 … / 4 punten\nDe heer POULAIN, enig vennoot, zaakvoerder en oprichter van de vennootschap “bvba LE\nBON” komt u advies vragen in verband met een kapitaalverhoging. De bvba LE BON werd\nopgericht op 16 november 2013.\nDe vennootschap heeft een kapitaal van 20.000 EUR en hij wenst het met 10.000 E",
    "themas": [
      "kapitaaloperaties",
      "vennootschapsrecht",
      "herwaarderingsmeerwaarden"
    ]
  },
  {
    "id": "2015-1-vr25",
    "vak_code_in_pdf": "3.2",
    "vak_naam_in_pdf": "Vennootschapsrecht (bijzondere mandaten)",
    "vraagtekst": "Vraag 1 … / 3 punten\nWat is of zijn de doelstelling(en) van de specifieke opdracht van de externe accountant bij de\nomzetting van een vennootschap ?\nAntwoord",
    "themas": [
      "omzetting-vennootschap"
    ]
  },
  {
    "id": "2015-1-vr26",
    "vak_code_in_pdf": "3.2",
    "vak_naam_in_pdf": "Vennootschapsrecht (bijzondere mandaten)",
    "vraagtekst": "Vraag 2 … / 18 punten\nIn de norm inzake de controle bij het voorstel tot ontbinding van vennootschappen met\nbeperkte aansprakelijkheid zoals goedgekeurd door de raad van het IAB staan een aantal uit\nte voeren werkzaamheden. Geef in de onderstaande gevallen weer wat de norm voorziet in\nvolgende geval",
    "themas": [
      "alarmbelprocedure",
      "ontbinding-vereffening",
      "continuiteitsbeginsel"
    ]
  },
  {
    "id": "2015-1-vr27",
    "vak_code_in_pdf": "3.2",
    "vak_naam_in_pdf": "Vennootschapsrecht (bijzondere mandaten)",
    "vraagtekst": "Vraag 3 … / 9 punten\nEen externe accountant krijgt als opdracht het opmaken van een verslag over een\nboekhoudkundige staat van activa en passiva in het kader van de omzetting van een\nvennootschap van NV Salami in BVBA Salami. De vennootschap valt onder het Wetboek van\nVennootschappen. Het betreft hi",
    "themas": [
      "omzetting-vennootschap",
      "confirmatiebrieven",
      "vennootschapsrecht"
    ]
  },
  {
    "id": "2015-1-vr28",
    "vak_code_in_pdf": "2.1",
    "vak_naam_in_pdf": "Personenbelasting",
    "vraagtekst": "Vraag 1 … / 4 punten\nBeroepsverliezen\nGeef aan welke van onderstaande uitspraken ONJUIST is:\nA. Wanneer in een welbepaalde beroepswerkzaamheid, na aftrek van de beroepskosten, een\nverlies overblijft, wordt dat eerst afgetrokken van de beroepsinkomsten die dezelfde\nbelastingplichtige tijdens hetzelfd",
    "themas": [
      "personenbelasting"
    ]
  },
  {
    "id": "2015-1-vr29",
    "vak_code_in_pdf": "2.1",
    "vak_naam_in_pdf": "Personenbelasting",
    "vraagtekst": "Vraag 2 … / 4 punten\nEen belastingplichtige is eigenaar van een in het buitenland gelegen onroerend goed. (NB:\nhet betreft geen onroerend goed dat kan beschouwd worden als de enige eigen woning van\nde belastingplichtige en er bestaat in desbetreffend land geen theoretische huurwaarde).\nWelke van ond",
    "themas": [
      "internationaal-fiscaal-recht"
    ]
  },
  {
    "id": "2015-1-vr30",
    "vak_code_in_pdf": "2.1",
    "vak_naam_in_pdf": "Personenbelasting",
    "vraagtekst": "Vraag 3 … / 4 punten\nGeef aan welke uitspraak ONJUIST is, met betrekking tot de aftrekbare bestedingen en de\nuitgaven die recht geven op een belastingvermindering :\nA. De kosten voor kinderoppas zijn sinds het aanslagjaar 2013 geen aftrekbare bestedingen\nmeer. Die kosten geven sinds het aanslagjaar ",
    "themas": [
      "onderhoudsuitkering"
    ]
  },
  {
    "id": "2015-1-vr31",
    "vak_code_in_pdf": "2.1",
    "vak_naam_in_pdf": "Personenbelasting",
    "vraagtekst": "Vraag 4 … / 4 punten\nVrijstellingen van economische aard\n aftrek voor bijkomend personeel tewerkgesteld in de uitvoer en de integrale\nkwaliteitszorg\n aftrek voor ander bijkomend personeel\n aftrek voor stage in de onderneming\n investeringsaftrek\nWelke van onderstaande uitspraken is ONJUIST:\nA. De",
    "themas": [
      "afschrijvingen",
      "vennootschapsrecht"
    ]
  },
  {
    "id": "2015-1-vr32",
    "vak_code_in_pdf": "2.1",
    "vak_naam_in_pdf": "Personenbelasting",
    "vraagtekst": "Vraag 5 … / 4 punten\nGeef aan welke van onderstaande uitspraken \"ONJUIST\" is, met betrekking tot de belasting\nvan de roerende inkomsten:\nA. Bij een niet-gereglementeerde spaarrekening moet op de volledige interestopbrengst een\nroerende voorheffing van 25% worden betaald.\nB. De eerste schijf (tot 56.",
    "themas": [
      "roerende-voorheffing",
      "internationale-belasting"
    ]
  },
  {
    "id": "2015-1-vr33",
    "vak_code_in_pdf": "2.2",
    "vak_naam_in_pdf": "Vennootschapsbelasting",
    "vraagtekst": "Vraag 1 … / 8 punten\nDe vennootschap ABC heeft een beleggingsportefeuille.\nDeze portefeuille was per 31 december 2013 als volgt samengesteld:\nBenaming Datum Aanschaffings- Kosten Datum Verkoop Kosten\naanschaf waarde aankoop verkoop -prijs verkoop\nAandelen 15/02/2011 10.000 200 30/06/2013 13.000 250\n",
    "themas": [
      "vennootschapsbelasting",
      "fiscale-verliezen"
    ]
  },
  {
    "id": "2015-1-vr34",
    "vak_code_in_pdf": "2.2",
    "vak_naam_in_pdf": "Vennootschapsbelasting",
    "vraagtekst": "Vraag 2 … / 6 punten\nTer info: De vraag heeft betrekking op het aanslagjaar 2014 – inkomsten 2013.\nDe vennootschap ‘ABC’ realiseert tijdens het belastbaar tijdperk 2013 een in principe fiscale\nwinst (= resultaat in de 1ste bewerking) van 500 000,00 EUR. Volgens de berekeningen zou de\nvennootschap re",
    "themas": [
      "vennootschapsbelasting",
      "dbi-aftrek",
      "vennootschapsrecht"
    ]
  },
  {
    "id": "2015-1-vr35",
    "vak_code_in_pdf": "2.2",
    "vak_naam_in_pdf": "Vennootschapsbelasting",
    "vraagtekst": "Vraag 3 … / 6 punten\nKan BVBA ‘ABC’ aan de hand van onderstaande gegevens met betrekking tot de\nbedrijfsleider aanspraak maken op het verminderd basistarief, in de veronderstelling dat alle\nandere voorwaarden zijn voldaan en het belastbaar resultaat meer bedraagt dan 36 000,00\nEUR ?\nDoe de nodige be",
    "themas": [
      "personenwagen-btw",
      "vennootschapsrecht"
    ]
  },
  {
    "id": "2015-1-vr36",
    "vak_code_in_pdf": "2.3",
    "vak_naam_in_pdf": "Belasting over de toegevoegde waarde",
    "vraagtekst": "Vraag 1 … / 4 punten\nUw cliënt is eigenaar van een woning gelegen in het Brussels Hoofdstedelijk Gewest. Uw\ncliënt wenst het appartement te verkopen en vraagt u om hem daarin te adviseren en de\nmeest voordelige formule voor hem aan te raden.\nUw cliënt heeft in 2006 de grond aangekocht voor 200.000 E",
    "themas": [
      "registratierechten"
    ]
  },
  {
    "id": "2015-1-vr37",
    "vak_code_in_pdf": "2.3",
    "vak_naam_in_pdf": "Belasting over de toegevoegde waarde",
    "vraagtekst": "Vraag 2 … / 2 punten\nEen nieuwe klant komt bij u aankloppen en vraagt om begeleiding bij de opstart, onder meer\nover zijn btw-statuut.\nHet gaat om een nieuw op te richten vzw die volgende activiteiten zal ontwikkelen:\n Het geven van yogalessen en relaxatieoefeningen voor mensen die kampen met een\nb",
    "themas": [
      "btw-aangifte",
      "btw"
    ]
  },
  {
    "id": "2015-1-vr38",
    "vak_code_in_pdf": "2.3",
    "vak_naam_in_pdf": "Belasting over de toegevoegde waarde",
    "vraagtekst": "Vraag 3 … / 3 punten\nDe uitbater van een lokale supermarkt heeft in de rekken regelmatig etenswaren die nog\nmoeilijk verkoopbaar zijn omdat bijvoorbeeld de verpakking licht beschadigd is, of omdat de\nvervaldatum dichtbij is. In plaats van de producten te verkopen met afslag of te vernietigen\ngaat hi",
    "themas": []
  },
  {
    "id": "2015-1-vr39",
    "vak_code_in_pdf": "2.3",
    "vak_naam_in_pdf": "Belasting over de toegevoegde waarde",
    "vraagtekst": "Vraag 4 … / 3 punten\nDe interne accountant van een Belgische onderneming rijdt met zijn bedrijfswagen elke\nmaand 2 dagen naar hun filiaal in Parijs om daar de boekhouding van de Franse\nonderneming af te sluiten en de Franse btw-aangifte te doen.\nDe accountant beschikt over een laptop, een gsm en een",
    "themas": [
      "btw-aangifte",
      "btw"
    ]
  },
  {
    "id": "2015-1-vr40",
    "vak_code_in_pdf": "2.3",
    "vak_naam_in_pdf": "Belasting over de toegevoegde waarde",
    "vraagtekst": "Vraag 5 … / 3 punten\nEen Belgische onderneming fabrikant van badkameraccessoires verkoopt goederen aan een\nNederlandse groothandel (met geldig NL btw-nummer) met leveringsvoorwaarden franco\nDuitsland. De Nederlandse groothandel heeft de goederen doorverkocht aan een Duitse\ngroothandel (met geldig DE",
    "themas": [
      "vennootschapsrecht",
      "btw-aangifte",
      "btw-intracommunautair"
    ]
  },
  {
    "id": "2015-1-vr41",
    "vak_code_in_pdf": "2.7",
    "vak_naam_in_pdf": "Fiscale procedure",
    "vraagtekst": "Vraag 1 … / 3 punten\nIn een aanslagjaar in de personenbelasting, 5 jaar vóór het huidige aanslagjaar wenst de\nadministratie onderzoekshandelingen te stellen bij uw cliënt.\nU analyseert :\nA. dat kan de administratie zonder beperking.\nB. dat kan de administratie sowieso niet meer.\nC. dat kan de admini",
    "themas": []
  },
  {
    "id": "2015-1-vr42",
    "vak_code_in_pdf": "2.7",
    "vak_naam_in_pdf": "Fiscale procedure",
    "vraagtekst": "Vraag 2 … / 3 punten\nUw cliënt wordt ingelicht dat de administratie 18 maanden geleden van een buitenlandse\nbelastingadministratie, waarmee België een dubbelbelastingverdrag heeft gesloten,\ninlichtingen kreeg die uitwijzen dat uw cliënt in een aanslagjaar vier jaar voor het huidige\ngeen correcte aan",
    "themas": [
      "internationaal-fiscaal-recht"
    ]
  },
  {
    "id": "2015-1-vr43",
    "vak_code_in_pdf": "2.7",
    "vak_naam_in_pdf": "Fiscale procedure",
    "vraagtekst": "Vraag 3 … / 3 punten\nDe administratie vraagt inzage in de bestelbonnen van uw cliënt die een onderneming voert\nonder vennootschapsvorm.\nU analyseert :\nA. de administratie kan deze niet opvragen omdat de bewaringsplicht van de boeken en\nbescheiden enkel beperkt is tot de wettelijk verplichte boeken e",
    "themas": [
      "fiscale-procedure"
    ]
  },
  {
    "id": "2015-1-vr44",
    "vak_code_in_pdf": "2.7",
    "vak_naam_in_pdf": "Fiscale procedure",
    "vraagtekst": "Vraag 4 … / 3 punten\nDe tenuitvoerlegging van een dwangbevel kan slechts worden gestuit door :\nA. een bezwaarschrift bij de gewestelijke directie.\nB. een verzoekschrift, verzet voor de rechtbank van eerste aanleg, fiscale kamer.\nC. een beroep bij de bevoegde controledienst.\nD. een voorziening bij de",
    "themas": [
      "voorzieningen",
      "belastingprocedure"
    ]
  },
  {
    "id": "2015-1-vr45",
    "vak_code_in_pdf": "2.7",
    "vak_naam_in_pdf": "Fiscale procedure",
    "vraagtekst": "Vraag 5 … / 3 punten\nDe vraag peilt naar de onderzoekstermijn inzake BTW.\nU analyseert :\nA. Dusdanig bestaan er geen specifieke bepalingen inzake controletermijnen, inzake BTW,\ndaar die gelijklopen met de specifieke verjaringstermijnen.\nB. het voorgaande antwoord is fout, want de onderzoekstermijn i",
    "themas": [
      "fiscale-procedure"
    ]
  },
  {
    "id": "2015-1-vr46",
    "vak_code_in_pdf": "2.4",
    "vak_naam_in_pdf": "Beginselen van registratie- en successierechten",
    "vraagtekst": "Vraag 1 … / 3 punten\nEen echtpaar koopt in september 2014 een huis in het Brussels Hoofdstedelijk Gewest tegen\nde prijs van 255.000 EUR.\nKies uit onderstaande lijst welke uitspraak de kopers geen recht geeft op een vermindering\nvan de registratierechten:\nA. Het echtpaar verkrijgt de blote (naakte) e",
    "themas": [
      "registratierechten",
      "vennootschapsrecht"
    ]
  },
  {
    "id": "2015-1-vr47",
    "vak_code_in_pdf": "2.4",
    "vak_naam_in_pdf": "Beginselen van registratie- en successierechten",
    "vraagtekst": "Vraag 2 … / 3 punten\nMevrouw Martin is overleden op 20 februari 2014. Op de datum van haar overlijden was ze\nweduwe en haar enige erfgenamen zijn haar 3 kinderen. Mevrouw Martin is overleden in het\nWaals Gewest, maar haar woonplaats heeft ze steeds in het Vlaams Gewest gehad.\nIn december 2013 had me",
    "themas": [
      "successierechten"
    ]
  },
  {
    "id": "2015-1-vr48",
    "vak_code_in_pdf": "2.4",
    "vak_naam_in_pdf": "Beginselen van registratie- en successierechten",
    "vraagtekst": "Vraag 3 … / 4 punten\nEen echtpaar wil de blote (naakte) eigendom van een onroerend goed aankopen waarvan het\nvruchtgebruik door de verkoper wordt voorbehouden.\nDe blote eigendom wordt verkregen tegen een prijs van 186.000 EUR.\nDe vruchtgebruiker is 63 jaar oud.\nDe blote eigenaar is 31 jaar oud.\nDe v",
    "themas": [
      "registratierechten"
    ]
  },
  {
    "id": "2015-1-vr49",
    "vak_code_in_pdf": "2.6",
    "vak_naam_in_pdf": "Beginselen van Europees en internationaal fiscaal recht",
    "vraagtekst": "Vraag 1 … / 6 punten\nBeantwoord de vragen met “waar” of “niet waar” op basis van de beginselen ingeschreven in\nde “door de OESO ontwikkelde modelovereenkomst naar het inkomen en naar het\nvermogen”.\na) Een natuurlijke persoon die geen dubbele nationaliteit bezit en die door beide\novereenkomstsluitend",
    "themas": [
      "successierechten",
      "internationaal-fiscaal-recht",
      "vennootschapsrecht",
      "internationaal-fiscaal-recht"
    ]
  },
  {
    "id": "2015-1-vr50",
    "vak_code_in_pdf": "2.6",
    "vak_naam_in_pdf": "Beginselen van Europees en internationaal fiscaal recht",
    "vraagtekst": "Vraag 2 … / 4 punten\nDe financieel verantwoordelijke van een internationale vereniging zonder winstoogmerk\n(ivzw) met maatschappelijke zetel in België raadpleegt u, omdat deze ivzw haar activiteiten\nwil uitbreiden tot andere landen van de Europese Unie. In het kader van deze expansie wil de\nivzw naa",
    "themas": []
  },
  {
    "id": "2015-1-vr51",
    "vak_code_in_pdf": "4.0",
    "vak_naam_in_pdf": "Juridische en beroepsnormen / deontologie",
    "vraagtekst": "Vraag 1 …. / 3 punten\nDe accountant en/of belastingconsulent is onderworpen aan de discretieplicht en het\nberoepsgeheim.\nGeef hieronder aan of de stellingen juist of fout zijn.\na) In tegenstelling tot het beroepsgeheim is de discretieplicht ook van toepassing op de\ninterne accountants en/of belastin",
    "themas": [
      "beroepsgeheim"
    ]
  },
  {
    "id": "2015-1-vr52",
    "vak_code_in_pdf": "4.0",
    "vak_naam_in_pdf": "Juridische en beroepsnormen / deontologie",
    "vraagtekst": "Vraag 2 …. / 3 punten\nIn de artikelen 27 tot en met 29 van het KB van 1 maart 1998 worden de erelonen van de\naccountant en/of belastingconsulent behandeld.\nGeef aan of volgende stellingen juist of fout zijn:\na) De accountant en/of belastingconsulent dient met een vast uurloon te werken en mag zijn\ne",
    "themas": []
  },
  {
    "id": "2015-1-vr53",
    "vak_code_in_pdf": "4.0",
    "vak_naam_in_pdf": "Juridische en beroepsnormen / deontologie",
    "vraagtekst": "Vraag 3 …. / 3 punten\na) Uw klant, een meubelhandel, stelt u de volgende vraag:\nHoeveel mag de klant van de meubelhandel in contanten betalen in de volgende\ngevallen?\nAntwoord … / 2 punten\n- Een klant koopt een meubel van 2.800 EUR: …………………………………………………..\n- Een klant koopt een meubel van 5.800 EUR: …",
    "themas": [
      "antiwitwaswet"
    ]
  },
  {
    "id": "2015-1-vr54",
    "vak_code_in_pdf": "4.0",
    "vak_naam_in_pdf": "Juridische en beroepsnormen / deontologie",
    "vraagtekst": "Vraag 4 …. / 3 punten\nDe heer FIXIT is reeds jaren de externe accountant van de NV TRIAL. De gedelegeerde\nbestuurder van die vennootschap wenst de vennootschap NV TRIAL te vereffenen en geeft\nde heer FIXIT de opdracht dit te doen.\nGeef in onderstaande situaties weer of de stelling of situatie juist ",
    "themas": [
      "onafhankelijkheid",
      "vennootschapsrecht"
    ]
  },
  {
    "id": "2015-1-vr55",
    "vak_code_in_pdf": "4.0",
    "vak_naam_in_pdf": "Juridische en beroepsnormen / deontologie",
    "vraagtekst": "Vraag 5 …. / 3 punten\nU bent belastingconsulent, lid van het IAB en ingeschreven op de deellijst van de externe\nleden van het Instituut.\nTwee personen uit de streek van Aarlen, die u al jaren kent, associëren zich en richten een\nvennootschap naar Luxemburgs recht op, die belastingadvies verstrekt in",
    "themas": []
  },
  {
    "id": "2015-1-vr56",
    "vak_code_in_pdf": "4.0",
    "vak_naam_in_pdf": "Juridische en beroepsnormen / deontologie",
    "vraagtekst": "Vraag 6 …. / 5 punten\nIn de norm inzake de controle van fusie- en splitsingsverrichtingen van vennootschappen\nzoals goedgekeurd door de raad van het IAB zijn er drie verplichtingen voor de\nberoepsbeoefenaar wanneer de door de wet vereiste verslagen in de bij de fusie of splitsing\nbetrokken vennootsc",
    "themas": []
  },
  {
    "id": "2024-1-vr1",
    "vak_code_in_pdf": "3.1",
    "vak_naam_in_pdf": "Vennootschapsrecht",
    "vraagtekst": "1 Vennootschapsrecht\nA. BVBA naar BV volgens nieuw WVV. Aandeelhouder vrij van volstorting van het niet\nvolstort kapitaal. Liquidatietest nodig?\nB. Quasi inbreng in NV. Wie kan dit doen?\nC. Vennootschap verliest rechtspersoonlijkheid:\nA. a. Bij ontbinding\nB. b. Bij publicatie van de ontbinding\nC. c.",
    "themas": [
      "ontbinding-vereffening",
      "wvv",
      "liquidatietest",
      "quasi-inbreng",
      "vennootschapsrecht"
    ]
  },
  {
    "id": "2024-1-vr2",
    "vak_code_in_pdf": "1.3 Externe controle",
    "vak_naam_in_pdf": "Externe controle / accountantsonderzoek",
    "vraagtekst": "2 Externe controle\nA. Stellingen juist of fout ivm onafhankelijkheid bij controle opdracht\nB. Na acceptatie van de opdracht -> voldoende kennis verwerven, op welke wijze?\nC. Volkomen controle volgens revisienormen\nD. 4 algemene stellingen juist of fout\nE. Bij een accountantsonderzoek wordt de materi",
    "themas": [
      "onafhankelijkheid"
    ]
  },
  {
    "id": "2024-1-vr3",
    "vak_code_in_pdf": "1.3 Interne controle",
    "vak_naam_in_pdf": "Interne controle",
    "vraagtekst": "3 Interne controle\nA. Wat zijn goede adviezen aan de bedrijfsleider in verband met de verkoopcyclus\nB. Wat is de hoofddoelstelling van de invoering van een interne controle in een KMO\nC. Over welke soort risico gaat het? ( COSO model)\n● Strategisch\n● Informatie\n● Operationeel\n● Financieel\nD. Verkoop",
    "themas": [
      "vennootschapsrecht",
      "interne-controle"
    ]
  },
  {
    "id": "2024-1-vr4",
    "vak_code_in_pdf": "3.2",
    "vak_naam_in_pdf": "Bijzondere mandaten — ontbinding/omzetting",
    "vraagtekst": "4 Bijzonder mandaten\nA. Stellingen Juist of fout:\nA. CV ontbonden door AV bij gewone meerderheid\nB. Vrijwillige ontbinding BV is verslag externe accountant verplicht als de\nmeerderheid van de aandeelhouders hierom vraagt.\nC. AV voor de vereffening van BV moet bij authentieke akte\nD. AV voor het slui",
    "themas": [
      "omzetting-vennootschap",
      "ontbinding-vereffening"
    ]
  },
  {
    "id": "2024-1-vr5",
    "vak_code_in_pdf": "2.1",
    "vak_naam_in_pdf": "Personenbelasting",
    "vraagtekst": "5 Personenbelasting\nA. Juist/ Fout: Van de toekenning aan de meewerkend echtgenoot, aangesloten\nministatuut, wordt er een forfaitaire kostenaftrek van 5% in mindering gebracht.\nB. Ik bezit een niet gemeubeld onroerend goed om te verhuren aan privépersoon als\nbewoning. Woning is door overstroming 6 m",
    "themas": [
      "roerende-voorheffing"
    ]
  },
  {
    "id": "2024-1-vr6",
    "vak_code_in_pdf": "4.0",
    "vak_naam_in_pdf": "Deontologie en AWW",
    "vraagtekst": "6 Deontologie en AWW\nA. Ereloon accountant: (Welke stelling is juist)?\nA. Barema ITAA\nB. Zelf vaststellen\nC. Provisie/voorschotten zijn verboden\nD. Kan bestaan uit commissielonen\nB. Welke stelling is fout?\nA. Dienstverstrekkers, zoals accountants en belastingadviseurs mogen 2.500 EUR\ncontante betali",
    "themas": [
      "antiwitwaswet",
      "contantengrens"
    ]
  },
  {
    "id": "2024-1-vr7",
    "vak_code_in_pdf": "1.1/IFRS",
    "vak_naam_in_pdf": "Wetgeving jaarrekening + IFRS",
    "vraagtekst": "7 IFRS\nA. Onder IAS/ IFRS zijn volgende methoden mogelijk: ( Juist/ fout)\nA. Fifo, Lifo, gewogen gemiddelde, individueel.\nB. Fifi, gewogen gemiddelde, individueel\nC. Lifo, gewogen gemiddelde individueel\nD. Fifo en gewogen gemiddelde\nB. Richtlijn 2013/34/EU 26/06/2013, opname waardering volgens voorz",
    "themas": [
      "ifrs",
      "afschrijvingen"
    ]
  },
  {
    "id": "2024-1-vr8",
    "vak_code_in_pdf": "2.2",
    "vak_naam_in_pdf": "Vennootschapsbelasting",
    "vraagtekst": "8 Vennootschapsbelasting\nA. Stellingen ivm overdraagbare fiscale verliezen\nB. Moeder A fuseert (neutraal) met Dochter B, waarin ze 100% bezit.\nNetto Actief van B = 100.\nFiscale waarde van de participatie in B in de boekhouding van A = 20\nOvergedragen fiscale verliezen van B = 30\nOverdraagbare aftrek",
    "themas": [
      "vennootschapsbelasting",
      "vennootschapsrecht"
    ]
  },
  {
    "id": "2024-1-vr9",
    "vak_code_in_pdf": "2.7",
    "vak_naam_in_pdf": "Fiscale procedure",
    "vraagtekst": "9 Fiscale procedure\nA. Bericht van wijziging aangetekend, uiterlijke termijn?\nB. Belastingplichtige verlaat België, wat te doen?\nC. Bericht van wijziging, verjaringstermijn is nakende, wat te doen?\nD. Vraag om inlichtingen, termijn?\nE. Bewaarplicht, welke stukken + termijn",
    "themas": [
      "fiscale-procedure"
    ]
  },
  {
    "id": "2024-1-vr10",
    "vak_code_in_pdf": "1.2",
    "vak_naam_in_pdf": "Analyse en kritische beoordeling jaarrekening",
    "vraagtekst": "10 Analyse en kritische beoordeling van de\njaarrekening\nA. Stellingen ivm financiële onafhankelijkheid\nB. Welke ratio kan je niet berekenen op basis van een verkort schema\nn- dagen klanten krediet\nC. In welke volgorde zijn rubrieken op Passief van de Balans gerangschikt?\nToenemende eisbaarheid\nD. JR",
    "themas": [
      "onafhankelijkheid",
      "afschrijvingen"
    ]
  },
  {
    "id": "2024-1-vr11",
    "vak_code_in_pdf": "2.3",
    "vak_naam_in_pdf": "BTW",
    "vraagtekst": "11 BTW\nA. Situatie: Rentenier liet hybride dieselwagen onderhouden door Porsche-garage\nAntwerpen (maandaangever)\nOnderhoud op 27/4/N\nKlant betaald op 3/5/N\nOp 30/4/N uitreiking factuur van 1.210 euro incl BTW:\na. Niet verplicht van factuur uit te reiken: BTW opeisbaar 3/5/N\nb. Niet verplicht van fac",
    "themas": [
      "btw-margeregeling"
    ]
  }
]
```
