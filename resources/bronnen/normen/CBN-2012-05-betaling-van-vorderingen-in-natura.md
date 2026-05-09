---
nummer: "CBN-advies 2012/5"
datum: 2012-02-15
themas:
  - vordering
  - inbetalinggeving
bron: https://www.cbn-cnc.be/nl/adviezen/betaling-van-vorderingen-in-natura
gerelateerde_adviezen:
  - titel: Klassering van de vorderingen bij faillissement van de schuldenaar (update) [ONTWERP]
    url: https://www.cbn-cnc.be/nl/adviezen/klassering-van-de-vorderingen-bij-faillissement-van-de-schuldenaar-update-ontwerp
    datum: '2025-06-10'
  - titel: Waarderen en boeken van cryptomunten gebruikt als betaalmiddel
    url: https://www.cbn-cnc.be/nl/adviezen/waarderen-en-boeken-van-cryptomunten-gebruikt-als-betaalmiddel
    datum: '2021-12-06'
  - titel: 'Schulden en vorderingen: gevolgen van de wijzigingen aan artikel 67 KB W.Venn. door het koninklijk besluit van 18 december 2015'
    url: https://www.cbn-cnc.be/nl/adviezen/schulden-en-vorderingen-gevolgen-van-de-wijzigingen-aan-artikel-67-kb-wvenn-door-het
    datum: '2016-07-06'
  - titel: De boekhoudkundige verwerking van factoringovereenkomsten
    url: https://www.cbn-cnc.be/nl/adviezen/de-boekhoudkundige-verwerking-van-factoringovereenkomsten
    datum: '2011-10-05'
bron_rol: interpretatief
chunk:
  level: 2
  type: '##'
  sub_strategy:
provenance:
  inputs:
    - id: https://www.cbn-cnc.be/nl/adviezen/betaling-van-vorderingen-in-natura
      sha256:
      version:
  tooling:
    pipeline: tools/etl/convert.py
    pipeline_version: 3b788cd
    model:
    prompt_version:
  generated_at: '2026-05-09T20:20:40Z'
  stale: false
  stale_reason:
  trust:
    status: trusted
    qa_version: trust-rework-2
    confirmed_at: '2026-05-09T21:27:46Z'
    confirmed_by: subagent-sonnet-4-6
    rationale: L1=pass
    agent_verdict_at: '2026-05-09T21:27:46Z'
    sample_pick: false
    sample_reviewed_at:
    sample_reviewed_by:
    layer1:
      verdict: pass
      heading_count: 5
      max_section_chars: 2579
      file_size_chars: 6773
      flags: []
      run_id: 20260509-212552
---
# CBN-advies 2012/5 – Betaling van vorderingen in natura

CBN-advies 2012/5 – Betaling van vorderingen in natura 

1. Inbetalinggeving door levering van een goed 
  1. Het in betaling gegeven goed is een materieel vast actief 
  2. Het in betaling gegeven goed is een vlottend actief 

2. Inbetalinggeving door levering van een dienst 

### 
Inleiding

De Commissie wenst in dit advies de betaling van een vordering in natura te behandelen. De betaling kan omschreven worden als de rechtshandeling waardoor de schuldenaar zijn verbintenis uitvoert. Een bijzondere vorm van betaling is de zogenaamde *inbetalinggeving*: de schuldenaar kan er bijvoorbeeld voor opteren om een goed te leveren of een dienst te verstrekken ter betaling[^1].

Er is slechts sprake van inbetalinggeving indien er aan een aantal voorwaarden cumulatief wordt voldaan[^2]:

1. de prestatie of de zaak die geleverd wordt bij wijze van betaling moet vooreerst verschillen van de oorspronkelijk verschuldigde zaak of prestatie; 
2. de levering van de zaak of de prestatie moet bovendien gebeuren met het oog op betaling, m.a.w. met de bedoeling een bestaande verbintenis uit te voeren. Ze moet met andere woorden gebeuren met de bedoeling de schuldenaar te bevrijden; 
3. de inbetalinggeving betreft een overeenkomst en veronderstelt dus wederzijdse toestemming. 

Binnen de rechtsleer bestaat er geen duidelijkheid omtrent het feit of de inbetalinggeving al dan niet schuldvernieuwing tot gevolg heeft, dan wel een overeenkomst is over de wijze van betalen. Voor de verdere boekhoudkundige uitwerking van de inbetalinggeving zal dit onderscheid volgens de Commissie weinig gevolgen hebben.

## Inbetalinggeving door levering van een goed

Voor de uitwerking van de inbetalinggeving door levering van een goed dienen we een onderscheid te maken naar de aard van het onderliggend goed. Immers, de schuldenaar kan ervoor opteren om goederen in betaling te geven dewelke duurzaam door de schuldeiser zullen worden gebruikt, en dewelke dus kwalificeren als materiële vaste activa. Daarnaast kan de schuldenaar er tevens voor opteren om handelsgoederen of diensten in betaling te geven dewelke kwalificeren als vlottende activa.

De Commissie is de mening toegedaan dat de boekhoudkundige verwerking in hoofde van de schuldeiser de aard van het respectievelijk ontvangen goed dient te respecteren.

### Het in betaling gegeven goed is een materieel vast actief

*Voorbeeld*

Een onderneming levert onderhoudsdiensten aan een afnemer voor een bedrag van 1.000 EUR, exclusief BTW. Initieel werd er voorzien in een monetaire betaling. Na overleg tussen de schuldenaar en schuldeiser wordt er besloten dat de schuldenaar een schoonmaakmachine van 1.000 EUR exclusief BTW in betaling geeft voor de openstaande schuld. 

Gezien de aard van het onderliggende goed, wordt deze inbetalinggeving als volgt boekhoudkundig verwerkt in hoofde van de schuldeiser:

 [^3]

| | Rekening | Omschrijving | Debet | Credit |
|---|----------|--------------|-------|--------|
| | 23 | Installaties, machines en uitrusting | 1.000 | |
| | 411 | Terug te vorderen BTW | 210 | |
| aan | 400 | Handelsdebiteuren | | 1.210 |

### Het in betaling gegeven goed is een vlottend actief

*Voorbeeld*

Een onderneming levert onderhoudsdiensten aan een afnemer voor een bedrag van 100 EUR, exclusief BTW. Initieel werd er voorzien in een monetaire betaling. Na overleg tussen de schuldenaar en schuldeiser wordt er besloten dat de schuldenaar schoonmaakproducten voor 100 EUR exclusief BTW in betaling geeft voor de openstaande schuld. 

Gezien de aard van het onderliggende goed, wordt deze inbetalinggeving als volgt boekhoudkundig verwerkt in hoofde van de schuldeiser:

 [^4]

| | Rekening | Omschrijving | Debet | Credit |
|---|----------|--------------|-------|--------|
| | 601 | Aankopen van hulpstoffen | 100 | |
| | 411 | Terug te vorderen BTW | 21 | |
| aan | 400 | Handelsdebiteuren | | 121 |

Op het einde van het boekjaar wordt er vastgesteld dat er nog 4 liter schoonmaakproduct met een monetaire waarde van 10 EUR aanwezig is in de voorraad:

| | Rekening | Omschrijving | Debet | Credit |
|---|----------|--------------|-------|--------|
| | 310 | Voorraad hulpstoffen | 10 | |
| aan | 6091 | Voorraadwijzigingen van hulpstoffen | | 10 |

## Inbetalinggeving door levering van een dienst

Voor wat betreft de inbetalinggeving door levering van een dienst is de Commissie de mening toegedaan dat deze dienst in hoofde van de schuldeiser dient te worden verwerkt als periodekost binnen de *Diensten en diverse goederen* *(rekening 61).* Mocht de dienst door de schuldenaar over verschillende boekjaren worden verstrekt, dan dient de schuldeiser rekening te houden met een passende afgrenzing.

*Voorbeeld* 

Een onderneming levert in 20X1 een machine aan een afnemer voor een bedrag van 1.000 EUR, exclusief BTW. Initieel werd er voorzien in een monetaire betaling. Eind 20X1 wordt er, na overleg tussen de schuldenaar en schuldeiser, besloten dat de schuldenaar beveiligingsdiensten voor één jaar in betaling zal geven voor een waarde van 1.000 EUR exclusief BTW. Gezien het overleg pas in oktober 20X1 plaatsvond, worden er in 20X1 slechts 2 maanden diensten geleverd. 

*Boekingen per 31 december 20X1*

 [^5]

| | Rekening | Omschrijving | Debet | Credit |
|---|----------|--------------|-------|--------|
| | 61 | Diensten en diverse goederen | 1.000 | |
| | 411 | Terug te vorderen BTW | 210 | |
| aan | 400 | Handelsdebiteuren | | 1.210 |

| | Rekening | Omschrijving | Debet | Credit |
|---|----------|--------------|-------|--------|
| | 490 | Over te dragen kosten | 833,33 (1.000 x 10/12) | |
| aan | 61 | Diensten en diverse goederen | | 833,33 |

*Boekingen in 20X2*

| | Rekening | Omschrijving | Debet | Credit |
|---|----------|--------------|-------|--------|
| | 61 | Diensten en diverse goederen | 833,33 | |
| aan | 490 | Over te dragen kosten | | 833,33 |

[^1]: R. KRUITHOF, H. MOONS en C. PAULUS, “Overzicht van rechtspraak verbintenissenrecht (1965-1963)”, TPR 1975, 771 en de verwijzingen aldaar.

[^2]: P. VAN OMMESLAGHE, Droit des obligations, Brussel, Presses universitaires de Bruxelles , 1985/1004.

[^3]: De Commissie wenst te verduidelijken dat er ook voor geopteerd kan worden om eerst de rekening 440 Leveranciers te crediteren en deze nadien te compenseren met de openstaande handelsdebiteur.

[^4]: De Commissie wenst te verduidelijken dat er ook voor geopteerd kan worden om eerst de rekening 440 Leveranciers te crediteren en deze nadien te compenseren met de openstaande handelsdebiteur.

[^5]: De Commissie wenst te verduidelijken dat er ook voor geopteerd kan worden om eerst de rekening 440 Leveranciers te crediteren en deze nadien te compenseren met de openstaande handelsdebiteur.
