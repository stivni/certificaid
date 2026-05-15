---
title: Verwerken van een wijziging in de consolidatiekring (inclusief step acquisition)
tags:
- competentie
- po-1-4
programmaonderdelen:
- '1.4'
status: voorgesteld
schema_version: '1.0'
gegenereerd_uit: data/concepten/competenties/verwerken-wijziging-consolidatiekring.yaml
gegenereerd_op: '2026-05-15'
---
# Verwerken van een wijziging in de consolidatiekring (inclusief step acquisition)

**⚖️ 75% · 🤖 25%** · Status: `voorgesteld`

> De verwerking is grotendeels wettelijk (KB WVV art. 3:127-3:132 voor eerste consolidatie en realisaties), maar de behandeling van kantelpunten tussen technieken (vermogensmutatie ↔ integrale/evenredige consolidatie) en transacties onder gemeenschappelijke leiding vergt doctrinair inzicht (CBN-adviezen).

## Aanbevolen werkwijze

### 1. Identificeren van de aard van de wijziging

📥 **Input**: Wijzigingen in de groep tussen twee opeenvolgende boekjaren: verwerving, vervreemding, liquidatie, verhoging/verlaging van belang, wijziging in mate van controle, kringintegratie van voorheen uitgesloten dochter
📤 **Output**: Eén van de typen: (a) opname nieuwe dochter (eerste consolidatie); (b) uittrede dochter (de-consolidatie); (c) step acquisition met kwalificatiewijziging; (d) wijziging tussen gezamenlijke en exclusieve controle; (e) transactie onder gemeenschappelijke leiding
**Waarom**: De aard van de wijziging bepaalt welk specifiek verwerkingsregime van toepassing is.
**Grondslag**: [[wijziging-consolidatiekring]]
### 2. Toetsen van kwalificatiewijziging bij belangsverhoging

📥 **Input**: Belangenpercentage en controlepercentage voor en na de transactie; aandeelhoudersovereenkomsten
📤 **Output**: Per trap: bevestiging of de kwalificatie wijzigt — (a) van geen invloed naar invloed van betekenis; (b) van invloed van betekenis naar controle; (c) verhoging binnen dezelfde categorie
**Waarom**: Een kwalificatiewijziging triggert een wijziging van consolidatietechniek met bijhorende waarderingsgevolgen.
**Grondslag**: [[step-acquisition]]
### 3. Verwerken van een eerste consolidatie bij opname van een nieuwe dochter of geassocieerde

📥 **Input**: Aanschaffingswaarde, eigen vermogen op verwervingsdatum, stille meer-/minderwaarden
📤 **Output**: Toepassing van de procedure voor eerste consolidatie (zie [[competenties/uitvoeren-eerste-consolidatie|uitvoeren eerste consolidatie]]): compensatie, toerekening verschil, boeking consolidatieverschil, afschrijvingsplan
**Waarom**: Elke nieuwe opname in de kring vereist een eerste consolidatie met berekening van het consolidatieverschil.
**Grondslag**: [[eerste-consolidatie]]
### 4. Verwerken van een kantelpunt vermogensmutatie → integrale/evenredige consolidatie

📥 **Input**: Bestaande boekwaarde van de deelneming (post 'Vennootschappen waarop vermogensmutatie is toegepast' + bestaand consolidatieverschil); aanvullende aanschaffingswaarde; eigen vermogen op datum van de nieuwe trap
📤 **Output**: Verlaten van vermogensmutatie; start integrale (of evenredige) consolidatie; herwaardering bestaande boekwaarde en herberekening consolidatieverschil; activa en passiva van de nieuwe dochter worden voortaan volledig (of pro-rata) opgenomen
**Waarom**: Bij overschrijding van de controlegrens (of overgang naar gezamenlijke controle) volstaat vermogensmutatie niet meer; de techniek kantelt.
**Grondslag**: [[step-acquisition]]
- ⚠️ **Bij overgang van vermogensmutatie naar integrale consolidatie blijft het bestaande consolidatieverschil ongewijzigd.** → Het bestaande consolidatieverschil wordt geherwaardeerd en de activa/passiva van de nieuwe dochter worden volledig opgenomen — er ontstaat een nieuwe eerste consolidatie. ([[step-acquisition]])
### 5. Verwerken van een gehele of gedeeltelijke realisatie van aandelen

📥 **Input**: Aandelenverkoop; oorspronkelijk consolidatieverschil; deel van de aandelen dat is vervreemd
📤 **Output**: Afboeking van het overblijvende consolidatieverschil naar verhouding van de gerealiseerde aandelen (KB WVV art. 3:132); eventueel volledige de-consolidatie van de dochter
**Waarom**: Bij realisatie verdwijnt de economische binding (geheel of gedeeltelijk) en moet het consolidatieverschil pro-rata worden afgeboekt.
**Grondslag**: [[wijziging-consolidatiekring]]
### 6. Verwerken van transacties onder gemeenschappelijke leiding

📥 **Input**: Overdracht van een dochter binnen dezelfde groep waarbij de uiteindelijke economische controle ongewijzigd blijft
📤 **Output**: Toepassing van de bijzondere regels: in beginsel geen nieuwe goodwill genereren; historische cijfers behouden — het economische karakter van de groep is niet gewijzigd
**Waarom**: Interne herstructureringen mogen het groepsbeeld niet kunstmatig wijzigen.
**Grondslag**: [[wijziging-consolidatiekring]]


## Voorbeelden

**Situatie**: Onderneming ABC bezit 20 % in DEF (geassocieerde onderneming, vermogensmutatie). In een latere stap koopt ABC er aandelen bij tot 60 %. Op de datum van trap 2 bedroeg DEF's eigen vermogen 800.

**Conclusie**: Kantelpunt: DEF wordt voortaan integraal geconsolideerd. ABC verlaat de vermogensmutatie; het bestaande consolidatieverschil wordt geherwaardeerd en de activa/passiva van DEF worden volledig opgenomen, met afzondering van het aandeel van derden (1 − 0,60) × DEF's eigen vermogen.

**Grondslag**: [[step-acquisition]] §kantelpunt invloed → controle; [[integrale-consolidatie]] §opname 100 %

**Redenering**: De controlegrens (> 50 %) wordt overschreden; de wijziging van consolidatietechniek triggert een nieuwe eerste consolidatie waarbij de bestaande post wordt herwaardeerd.

---
**Situatie**: Onderneming X verkoopt 30 % van haar 100 %-dochter D buiten de groep; D blijft een dochter (70 % belang).

**Conclusie**: Pro-rata afboeking van het oorspronkelijke consolidatieverschil naar verhouding van de gerealiseerde aandelen (30 %); D blijft in de consolidatiekring; voortaan wordt 30 % als belangen van derden opgenomen.

**Grondslag**: [[wijziging-consolidatiekring]] §realisatie aandelen; [[consolidatieverschil]] §afboeking pro-rata

**Redenering**: Gedeeltelijke realisatie zonder verlies van controle: D blijft integraal geconsolideerd, maar het verkochte deel triggert pro-rata afboeking van consolidatieverschil en een nieuw aandeel van derden van 30 %.

---

## Gebaseerd op concepten

[[wijziging-consolidatiekring]] · [[eerste-consolidatie]] · [[step-acquisition]] · [[consolidatieverschil]] · [[vermogensmutatiemethode]] · [[integrale-consolidatie]] · 
## Voortkomend uit

- **Taken**: 1.4.taak.1
- **Kenniselementen**: 1.4.I.G, 1.4.II.D
