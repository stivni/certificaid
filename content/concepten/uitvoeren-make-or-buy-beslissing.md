---
title: Uitvoeren van een make-or-buy-beslissing op basis van kostenanalyse
tags:
- concept
- competentie
- po-1-8
linked_anchors:
- 1.8.taak.1
- 1.8.III.E
programmaonderdelen:
- '1.8'
confidence: inferred
node_type: competentie
status: voorgesteld
schema_version: '1.6'
gegenereerd_uit: data/concepten/records/uitvoeren-make-or-buy-beslissing.json
gegenereerd_op: '2026-05-21'
---
# Uitvoeren van een make-or-buy-beslissing op basis van kostenanalyse 🔗

Competentie waarmee de stagiair een make-or-buy-beslissing onderbouwt: relevante kosten isoleren (variabel + vermijdbare vaste + opportuniteitskost; geen sunk costs en geen gemeenschappelijke vaste kosten), make-kost en buy-kost vergelijken, strategische factoren (knowhow, leveringszekerheid, IP) wegen en een gevoeligheidsanalyse uitvoeren op volume en leveranciersprijs. Vereiste discipline: scheid relevante van niet-relevante kosten consequent — een full-cost-rapportage is misleidend voor deze beslissing.



## Stappen

### 1. Afbakenen van de beslissingshorizon en scope

Bepaal of de beslissing korte termijn (capaciteit vaststaat) of lange termijn (capaciteit kan wijzigen) is, en welke alternatieven realistisch zijn.

**Waarom?** Op korte termijn zijn vaste kosten meestal sunk; op lange termijn worden ze opnieuw relevant. Verkeerde horizon = verkeerde kost.

**📥 Input**:
- Productie-/inkoop-vraagstuk → **Welk onderdeel of welke fase, voor welk volume, welke termijn** _(document)_
- Capaciteitsstatus → **Vrije capaciteit of beperking** _(document)_

**📤 Output**:
- Beslissingskader → **Horizon + alternatieven + capaciteits-context** _(document)_

**🛠️ Hoe**:

1. Definieer alternatief A (zelf maken) tegen alternatief B (uitbesteden of inkopen).
2. Klasseer horizon: incidenteel (1-3 maanden) of structureel (> 1 jaar).
3. Toets capaciteit: heeft 'maken' nog vrije capaciteit of moet er geïnvesteerd worden?
4. Beslis welke kostendefinitie van toepassing is: marginaal (korte termijn) of
   volledig (lange termijn) volgens [[kostenanalyse-make-or-buy]] §horizon.


**Grondslag**: [[kostenanalyse-make-or-buy]] §horizon, [[marginale-kostprijs]] §korte-termijn

### 2. Identificeren van relevante kosten — sunk-cost-filter en opportuniteits-toets

Selecteer alleen kosten die door de beslissing wijzigen; elimineer sunk costs en breng eventuele opportuniteitskost in beeld.

**Waarom?** Beslissen op basis van niet-relevante kosten leidt tot foute conclusies — een klassieke examenval.

**📥 Input**:
- Volledige kostprijs-uitsplitsing alternatief A en B → **Per kostensoort + classificatie** _(boekhoudkundig-bedrag)_

**📤 Output**:
- Tabel relevante kosten per alternatief → **Inkrementele kosten + opportuniteit** _(boekhoudkundig-bedrag)_

**🛠️ Hoe**:

1. Pas [[sunk-cost]] §filter toe: schrap eerder gemaakte uitgaven (bv. al
   afgeschreven machine, al betaalde opleiding).
2. Pas [[opportuniteitskost]] §beslissingsregel toe: zou de capaciteit anders
   worden ingezet bij keuze 'kopen'? Tel die gederfde contributiemarge bij de
   kost van 'maken'.
3. Voor 'kopen': verwerk inkomende kost + ontvangstcontrole + transport in inkoopprijs.
4. Vermijd full-costing-allocaties van algemene overhead die toch blijft lopen.


**Grondslag**: [[sunk-cost]] §filter, [[opportuniteitskost]] §beslissingsregel, [[kostenanalyse-make-or-buy]] §relevant-kost

### 3. Berekenen en vergelijken van de twee alternatieven

Bereken de totale inkrementele kost (inclusief opportuniteit) per alternatief en vergelijk.

**Waarom?** De numerieke kern van make-or-buy is een directe vergelijking van relevante kosten — wat overblijft na de filter.

**📥 Input**:
- Tabel relevante kosten uit stap 2 → **Bedragen per alternatief** _(boekhoudkundig-bedrag)_

**📤 Output**:
- Voorkeurs-alternatief op kost-basis → **Verschil €** _(conclusie)_

**🛠️ Hoe**:

1. Totaal alternatief A (maken) = variabele kost zelf-productie + inkrementele
   vaste kost (alleen als die wijzigt) + opportuniteitskost capaciteit.
2. Totaal alternatief B (kopen) = inkoopprijs × volume + ontvangstkosten +
   eventuele resterende interne kost.
3. Kies het laagste totaal — maar zie stap 4 voor kwalitatieve factoren.


> [!example]- Voorbeeld: Yperse Werkplaats BV overweegt om de Spinnerij te outsourcen
> Yperse Werkplaats BV overweegt om de Spinnerij te outsourcen. Jaarvraag = 8.000 mach-uren spinwerk voor de productie. Externe spinnerij vraagt € 70/uur. Interne variabele kost = € 45/uur. Vaste kosten Spinnerij € 200.000 (bij outsourcing 60 % vermijdbaar). Vrijgekomen capaciteit kan extra weverij-werk doen met contributiemarge € 30.000/jaar.
>
> 1. **Relevante kosten zelf-spinnen (A)** 🧮
>
>    | Component                          | Bedrag       |
>    |------------------------------------|-------------:|
>    | Variabele kost (8.000 u × € 45)    | € 360.000    |
>    | Vermijdbare vaste kost             | € 120.000    |
>    | Opportuniteitskost (vrijgekomen)   | €  30.000    |
>    | **Totaal A**                       | **€ 510.000** |
>    
>
> 2. **Relevante kosten uitbesteden (B)** 🧮
>
>    | Component                          | Bedrag       |
>    |------------------------------------|-------------:|
>    | Inkoopprijs (8.000 u × € 70)       | € 560.000    |
>    | **Totaal B**                       | **€ 560.000** |
>    
>
> 3. **Conclusie** 💬
>
>    Zelf maken is € 50.000 goedkoper op jaarbasis. Zelf-maken behouden, tenzij
>    kwalitatieve factoren anders aangeven (zie stap 4).
>    
>

**Grondslag**: [[kostenanalyse-make-or-buy]] §vergelijking, [[opportuniteitskost]] §beslissingsregel

### 4. Toetsen aan kwalitatieve factoren en risico's

Weeg niet-financiële criteria mee: kwaliteitscontrole, leveringszekerheid, kennis-behoud, strategische afhankelijkheid, sociale gevolgen.

**Waarom?** Een 'goedkopere' uitbesteding kan operationeel duurder uitvallen door kwaliteitsproblemen, langere doorlooptijd of personeels-afvloeiing.

**📥 Input**:
- Voorkeur op kost-basis uit stap 3 → **A of B met verschil €** _(conclusie)_
- Lijst kwalitatieve factoren → **Risico's + opportuniteiten** _(document)_

**📤 Output**:
- Eindadvies → **Maken / kopen + voorwaarden** _(conclusie)_

**🛠️ Hoe**:

1. Inventariseer kwalitatieve factoren in een SWOT-stijl tabel:
   - Sterkte/Zwakte: kwaliteit, kennis, capaciteit, kostenstructuur.
   - Kans/Bedreiging: leverancier-marktmacht, afhankelijkheid, doorlooptijd.
2. Test het verschil uit stap 3 op gevoeligheid: bij welke prijsstijging van de
   leverancier kantelt de beslissing? Bij welke daling van interne efficiëntie?
3. Indien financieel verschil klein (< 10 %) én strategisch risico hoog
   (kennis-verlies, single source): meestal zelf-maken houden.
4. Documenteer eindadvies met expliciete voorwaarden (bv. heronderhandel
   leveranciersprijs binnen 6 maanden).


**Grondslag**: [[kostenanalyse-make-or-buy]] §kwalitatieve-toets

> [!warning]- Filter alle sunk costs (afgeschreven machines, vorige opleidingen) eruit vóór je gaat vergelijken.
>
> _Vaak fout gedaan_: Sunk costs meetellen in de make-zijde — leidt tot te dure 'maken' en onterechte voorkeur voor 'kopen'.
>
> _Grondslag_: [[sunk-cost]] §filter

> [!warning]- Voer altijd de opportuniteitskost-toets uit voor capaciteit die vrijkomt of die elders ingezet kan worden.
>
> _Vaak fout gedaan_: Vergeten dat vrijgekomen capaciteit alternatieve contributiemarge kan leveren — leidt tot verkeerde voorkeur.
>
> _Grondslag_: [[opportuniteitskost]] §beslissingsregel

> [!warning]- Onderzoek of vermeende 'vaste kosten' bij outsourcing werkelijk vermijdbaar zijn (afvloeiing, machine-verkoop, opzegtermijnen).
>
> _Vaak fout gedaan_: Vaste kosten 100 % als vermijdbaar inschatten terwijl ze deels blijven doorlopen.
>
> _Grondslag_: [[vaste-kosten]] §vermijdbaar-versus-doorlopend


## Voorbeelden



