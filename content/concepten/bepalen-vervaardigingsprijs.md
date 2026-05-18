---
title: Bepalen van de vervaardigingsprijs
tags:
- concept
- competentie
- po-1-8
linked_anchors:
- 1.8.taak.1
- 1.8.II
- 1.8.II.A
- 1.8.II.B
- 1.8.III.A
programmaonderdelen:
- '1.8'
confidence: inferred
node_type: competentie
status: voorgesteld
schema_version: '1.6'
gegenereerd_uit: data/concepten/records/bepalen-vervaardigingsprijs.json
gegenereerd_op: '2026-05-18'
---
# Bepalen van de vervaardigingsprijs 🤖

Competentie waarmee de stagiair de wettelijke vervaardigingsprijs van zelf-vervaardigde voorraad bepaalt volgens KB 21.10.2018 art. 22 + CBN 132/7 §2.1: aanschaffingsprijs grondstoffen + directe productiekosten + evenredig deel indirecte productiekosten. Centrale toepassing in PO 1.8 — gevraagde uitkomst is een voorraadwaarde op de balans die juridisch verdedigbaar is. De stagiair moet expliciete keuzes maken over full vs. direct costing, behandeling van onderbezetting en uitsluiting van commerciële en administratieve kost.


## Stappen

### 1. Toetsen of het object onder de vervaardigingsprijs-regel valt

Bepaal of het te waarderen object goederen in voorraad of bestellingen in uitvoering zijn die door de onderneming zelf zijn vervaardigd.

**Waarom?** Vervaardigingsprijs geldt voor zelfvervaardigde voorraden en bestellingen in uitvoering; voor aangekochte voorraad geldt aanschaffingsprijs.

**📥 Input**:
- Aard van het voorraadobject → **Type goed (grondstof, halffabricaat, gereed product, BIU)** _(document)_

**📤 Output**:
- Toepasbaarheids-conclusie → **Vervaardigingsprijs vs. aanschaffingsprijs** _(conclusie)_

**🛠️ Hoe**:

1. Klasseer het voorraadobject volgens [[voorraadwaardering]] §rubrieken:
   30 grondstoffen, 31 hulpstoffen, 32 goederen in bewerking, 33 gereed product,
   34 handelsgoederen, 37 bestellingen in uitvoering.
2. Voor 32, 33 en 37 (zelfvervaardigd): vervaardigingsprijs.
3. Voor 30, 31, 34 (aangekocht): aanschaffingsprijs (= inkoopprijs + bijkomende kosten).
4. Documenteer keuze in toelichting jaarrekening (waarderingsregels).


**Grondslag**: [[voorraadwaardering]] §rubrieken, KB 21.10.2018 art. 22 + 23

### 2. Berekenen van de aanschaffingsprijs van grondstoffen

Bepaal de aanschaffingsprijs van de gebruikte grondstoffen en hulpstoffen die in het product zijn verwerkt.

**Waarom?** Dit is de eerste verplichte component van de vervaardigingsprijs (KB art. 22 + CBN 132/7 §2.1).

**📥 Input**:
- Materiaal-stuklijst + voorraad-bewegingen → **Kg/m² per eenheid product + waarderings-methode (FIFO, LIFO toegelaten, gewogen gemiddelde)** _(boekhoudkundig-bedrag)_

**📤 Output**:
- Grondstoffen-kost per eenheid en per serie → **€** _(boekhoudkundig-bedrag)_

**🛠️ Hoe**:

1. Pas [[materiaalkosten]] §aanschaffingsprijs toe: inkoopprijs + bijkomende
   kosten (transport, invoerrechten, niet-recupereerbare BTW) − kortingen.
2. Vermenigvuldig per eenheid product met het normverbruik (bv. 5 kg wol per
   tapijt).
3. Voor voorraadafloop: pas de waarderings-methode toe die in de waarderingsregels
   is vastgelegd (FIFO, gewogen gemiddelde — LIFO toegelaten maar zeldzaam).


**Grondslag**: [[materiaalkosten]] §aanschaffingsprijs, CBN 132/7 §2.1, KB 21.10.2018 art. 22

### 3. Optellen van direct toerekenbare productiekosten

Tel alle productiekosten op die rechtstreeks aan het product toe te wijzen zijn — arbeid, energie, machine-uren — en die als gevolg van de productie zijn ontstaan.

**Waarom?** KB art. 22 verplicht inclusie van direct toerekenbare productiekosten — anders is de vervaardigingsprijs onvolledig.

**📥 Input**:
- Tijdsregistratie directe arbeid + standaarduurtarief (€ 25/u bij Yperse) → **Werkelijke of standaard uren × tarief** _(boekhoudkundig-bedrag)_
- Direct toewijsbare overige productiekosten → **Energie productiemachine, hulpstoffen, uitval** _(boekhoudkundig-bedrag)_

**📤 Output**:
- Direct toewijsbare kost per eenheid → **€** _(boekhoudkundig-bedrag)_

**🛠️ Hoe**:

1. Volg [[arbeidskosten]] §directe-arbeid: brutoloon × (1 + sociale lasten +
   vakantiegeld) — typisch € 25/u inclusief bij Yperse Werkplaats BV.
2. Verwerk overige direct toerekenbare productiekosten via [[overige-kosten]]
   §direct-toerekenbaar.
3. Geen commerciële, administratieve of financiële kosten — die behoren NIET
   tot de vervaardigingsprijs (KB art. 22 al.2 expliciet).


**Grondslag**: [[arbeidskosten]] §directe-arbeid, [[overige-kosten]] §direct-toerekenbaar, KB 21.10.2018 art. 22, CBN 132/7 §2.1

### 4. Toerekenen van het 'evenredig deel' indirecte productiekosten

Bepaal welk deel van de indirecte productiekosten (productie-overhead) toe te rekenen valt aan het product, op een redelijke en consistente basis.

**Waarom?** KB art. 22 stelt dat 'een evenredig deel' van de productiekosten die slechts onrechtstreeks aan het product kunnen worden toegerekend, in de vervaardigingsprijs moet zitten — behalve als de onderneming opteert voor exclusie en dat motiveert in de toelichting.

**📥 Input**:
- Indirecte productiekosten per kostencentrum uit [[toepassen-volledige-kostencalculatie]] → **Bedrag + activiteit** _(boekhoudkundig-bedrag)_
- Bezettingsgraad → **Werkelijk versus normvolume** _(percentage)_

**📤 Output**:
- Toegerekend indirect deel per eenheid → **€** _(boekhoudkundig-bedrag)_

**🛠️ Hoe**:

1. Gebruik de verdeelsleutels van [[toepassen-volledige-kostencalculatie]] stap 4
   om indirecte productiekost aan de drager toe te wijzen.
2. CBN 132/7 §2.1 staat exclusie van indirecte productiekosten toe op
   voorwaarde van expliciete vermelding in toelichting + consistente toepassing.
3. Onderbezetting: kost van leegloop (vaste kosten × (norm-volume − werkelijk
   volume) / norm-volume) hoort NIET in de vervaardigingsprijs — die wordt als
   periodekost behandeld.
4. Het 'evenredig deel' verbiedt dat onderbezetting alle voorraad-eenheden
   belast met de niet-geproduceerde overhead.


> [!example]- Voorbeeld: Yperse Werkplaats BV — vervaardigingsprijs per tapijt-standaard (serie van 1.000)
> Yperse Werkplaats BV — vervaardigingsprijs per tapijt-standaard (serie van 1.000).
>
> 1. **Componenten vervaardigingsprijs** 🧮
>
>    | Component                                  | Bedrag        |
>    |--------------------------------------------|--------------:|
>    | Grondstoffen wol (5 kg × € 5,00)           | €  25,00      |
>    | Direct toerekenbare arbeid (0,68 u × € 25) | €  17,00      |
>    | Indirect toegerekend productie-deel (zie stap 4 van [[toepassen-volledige-kostencalculatie]]) | €  19,40 |
>    | **Vervaardigingsprijs per tapijt**          | **€  61,40**  |
>    
>
> 2. **Voor balans-voorraadwaardering** 💬
>
>    Geen commerciële of administratieve kost meegerekend (uit het scope-verbod
>    van KB art. 22 al.2). Onderbezetting van Confectie 5 % → € 14.000 jaar-kost
>    van leegloop blijft buiten de voorraadwaardering en wordt periodekost.
>    
>

**Grondslag**: [[vervaardigingsprijs]] §evenredig-deel-indirect, CBN 132/7 §2.1, KB 21.10.2018 art. 22

> [!warning]- Sluit commerciële, administratieve en financiële kosten expliciet uit van de vervaardigingsprijs.
>
> _Vaak fout gedaan_: Volledige bedrijfskostprijs op voorraad zetten — kunstmatig opgeblazen voorraad-waarde, schendt KB art. 22 al.2.
>
> _Grondslag_: [[vervaardigingsprijs]] §scope-verbod, KB 21.10.2018 art. 22 al.2

> [!warning]- Pas een 'evenredig' deel toe — corrigeer voor onderbezetting via norm-volume.
>
> _Vaak fout gedaan_: Werkelijke totale indirecte productiekost delen door werkelijk volume — onderbezetting wordt zo onterecht aan voorraad toegerekend.
>
> _Grondslag_: [[vervaardigingsprijs]] §evenredigheid, CBN 132/7 §2.1

### 5. Opnemen, toetsen en toelichten

Boek de voorraad in tegen vervaardigingsprijs, toets aan eventuele lagere realisatiewaarde, en vermeld de waarderings-methode in de toelichting.

**Waarom?** De jaarrekening vereist (i) opname tegen vervaardigingsprijs of lagere marktwaarde, (ii) consistente toepassing, en (iii) transparantie via de waarderingsregels.

**📥 Input**:
- Vervaardigingsprijs per eenheid uit stap 4 → **€ per eenheid + voorraadtelling** _(boekhoudkundig-bedrag)_
- Marktprijs of netto-realisatiewaarde → **Verkoopprijs − verkoopkosten** _(boekhoudkundig-bedrag)_

**📤 Output**:
- Voorraad-waardering op balans + toelichting waarderingsregels → **Saldo + methode-omschrijving** _(nieuwe-balanspost)_

**🛠️ Hoe**:

1. Bereken voorraad-saldo: aantal × vervaardigingsprijs per eenheid.
2. Toets aan netto-realisatiewaarde volgens [[voorraadwaardering]] §lagere-marktwaarde:
   waardeer aan vervaardigingsprijs OF lagere markt indien dat lager is.
3. Bij lagere markt: boek waardevermindering (klasse 631) — geen blijvende
   upgrading na herstel.
4. Documenteer in toelichting: gekozen methode (FIFO/LIFO/gewogen gemiddelde),
   behandeling indirecte productiekosten (inclusief of exclusief met motivering),
   behandeling onderbezetting.


**Grondslag**: [[voorraadwaardering]] §lagere-marktwaarde, KB 21.10.2018 art. 28 + 100, CBN 132/7


## Voorbeelden



## Bronnen

[^1]: `CBN-0132-07-boeking-en-waardering-van-voorraden__sec_vervaardigingsprijs`
