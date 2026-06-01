# Leerpad-skelet PO 2.7 — Regionale en lokale belastingen

**Status**: voorstel (2026-06-01). Sparring-document voor de bouw van het volledige leerpad-pakket (overzicht + leerstukken + samenvatting + oefening).
**Volgende stap**: na sparring → besluit over voorbeeldgroep + scripts per leerstuk via één Opus-run (ADR-037 amendement B) + samenvatting-migratie uit 3 themafiches.

---

## 1. Programma-analyse

### Officiële taken en doelstellingen

PO 2.7 heeft **drie taken** met **4 doelstellingen** in totaal. Niveau: **integratie** (`niveau: integratie` in PO-metadata — hoogste cognitieve laag in het programma).

| Code | Tekst (kort) | Rol |
|---|---|---|
| 2.7.taak.1 | Begeleiding bij oprichting van een onderneming | anchor |
| 2.7.taak.1.doel.1 | Autonoom werken in complexe fiscale omgeving — geïntegreerd advies waarin federale, gewestelijke en lokale fiscaliteit samenkomen | context |
| 2.7.taak.2 | Bijstaan van belastingplichtigen bij fiscale verplichtingen (aangiftes OV, verkeer, leegstand, …) | anchor — **hoofdtaak** |
| 2.7.taak.2.doel.1 | Geavanceerde concepten regionale + lokale belastingen toepassen op complexe gevallen | context |
| 2.7.taak.2.doel.2 | Relevante informatie verzamelen + juiste vragen stellen + fiscale risico's beheren | context |
| 2.7.taak.3 | Vertegenwoordigen bij gewestelijke (Vlabel, Bruxelles Fiscalité) en lokale (college B&S, deputatie) administraties | anchor |
| 2.7.taak.3.doel.1 | Adviseren over fasen van de belastingprocedure + gevolgen-afweging | context |

**Cruciale observaties**:

1. **Drie taken — adviseur · boekhouder · vertegenwoordiger** — exact het driehoeks-rolmodel uit de minicursus van het project. Geen enkele taak overweegt; het PO toetst integraal het accountantswerk over gewest + provincie + gemeente.
2. **"Geïntegreerd advies"** in 2.7.taak.1.doel.1 is sterk: de stagiair moet niet alleen weten welk gewest welke heffing oplegt, maar ook **samenloop met federale belastingen** kunnen doorrekenen — wat het PO een sterke cross-PO-component geeft (PO 2.1, 2.6, 2.5).
3. **De hoofdtaak is 2.7.taak.2** (bijstaan bij verplichtingen) — typische "compliance"-taak met aangiftes, termijnen, formaliteiten. De andere twee zijn omkaderend (oprichting → bredere context; vertegenwoordiging → na-het-feit-procedure).

### Kenniselementen-tree

Twee hoofdblokken, beide **gevorderd niveau + rechtspraak** — d.w.z. examenvraag mag een arrest van Grondwettelijk Hof, fiscale rechtbank of Cassatie inroepen.

- **2.7.I — GEWESTELIJKE FISCALITEIT**
  - 2.7.I.A — Algemene principes per type (4 sub-items): overgedragen belastingen · fiscale bevoegdheid gemeenschappen + gewesten · autonome belastingen · vestiging + invordering
  - 2.7.I.B — Types (4 sub-items): regeling BHG · regeling Vlaanderen · regeling Wallonië · gemeenschapsbelastingen
- **2.7.II — LOKALE BELASTINGEN**
  - 2.7.II.A — Algemene principes per type (4 sub-items): bevoegdheid om te heffen · belastingreglementering · vestiging + invordering + vervolging · regeling van geschillen
  - 2.7.II.B — Types (2 sub-items): gemeentebelastingen · provinciebelastingen

**Structuur-observatie**: 2.7.I.A en 2.7.II.A delen exact dezelfde vier-bouwstenen-kapstok (bevoegdheid · regulatie · vestiging+invordering · geschillen). Dat is een **pedagogisch geschenk**: één kapstok werkt voor alle niveaus. Tegelijk is 2.7.I.B (vier gewest-blokken) inhoudelijk gevarieerd — Vlaamse autonome heffingen (leegstand, planbaten) verschillen sterk van Brussel en Wallonië. De **horizontale as** (de vier bouwstenen) is daardoor stabieler dan de **verticale as** (per gewest of per niveau).

### Kern vs rakend

- **Kern (eigen aan 2.7)**:
  - **Bevoegdheidskaders** (gewestelijke + lokale fiscale autonomie) — art. 170 GW, BFW art. 1-7, art. 41/162 GW
  - **Reglementaire grondslag** voor lokale belastingen — Wet 24.12.1996, Decreet Lokaal Bestuur, wettigheidstoets aan gelijkheid/proportionaliteit/non-bis-in-idem ⚠️ te verifiëren (Wet 24.12.1996 niet in RAG-bronnen-corpus aangetroffen — bij bouw te checken via primaire bron)
  - **Typische gewestelijke autonome heffingen**: leegstandsheffing bedrijfsruimten (VCF Titel 2.6), planbatenheffing (VCRO 2.6.4 e.v.) ⚖️
  - **Aanvullende belastingen op gewest- + federale heffingen**: opcentiemen OV, aanvullende gemeentebelasting PB, provinciale opcentiemen ⚖️
  - **Gewest-eigen vestigings- en invorderingsprocedures** (Vlabel-procedure VCF Titel 3, Brusselse Codex Fiscale Procedure ord. 6.3.2019, Waals Decreet 6.5.1999, gemeentelijke procedure Wet 24.12.1996) — eigen termijnen, eigen administraties, eigen rechtsmiddelen ⚖️ (Vlabel + Waals decreet verifieerd via RAG)
- **Rakend met andere PO's**:
  - **PO 2.6 — Registratie- en successierechten**: de **materiële** gewest-tarieven, vrijstellingen, gunstregimes voor de gezinswoning of familiebedrijf zitten in 2.6. PO 2.7 zegt **waarom** die per gewest verschillen (bevoegdheidskader) — niet welk tarief. Risico op overlap: erfbelasting en registratie zijn dé schoolvoorbeelden van overgedragen gewestbelasting.
  - **PO 2.1 — Personenbelasting**: federale grondslag waarop de aanvullende gemeentebelasting en de gewestelijke belastingverminderingen (woonbonus, dienstencheques, ...) zitten. 2.7 raakt enkel de **opslag**, niet de federale aanslag zelf.
  - **PO 2.5 — Fiscale procedure**: algemene federale procedureleer (WIB92 art. 346, 354, 366, ...). PO 2.7 doet alleen de **gewestelijke + lokale eigenheden** (Vlabel-bezwaartermijn 3 mnd ≠ federale 6 mnd; bezwaar bij college B&S binnen 3 mnd). **Belangrijk om scherp af te bakenen** — anders dupliceren PO 2.5 en PO 2.7 elkaar.
  - **PO 3.0 — Vennootschaps- en verenigingsrecht**: keuze vestigingsplaats bij oprichting (taak 2.7.1) raakt de civielrechtelijke kant van zetel + statutaire zetel.
  - **PO 1.1/1.2 — Boekhouding**: aangifte onroerende voorheffing of leegstandsheffing wordt boekhoudkundig verwerkt — maar dit is een marginale raakvlak.

---

## 2. Voorbeeldexamen-patronen

### Gap: geen voorbeeldexamenvragen geclassificeerd onder PO 2.7

Zoek-resultaat in `data/programma/examen_vragen/_interpretaties/` op 2026-06-01 met filter `programmaonderdeel_ids` = `2.7`: **0 hits**. Het bestaande `content/studiemateriaal/2-7/voorbeeldexamenvragen.md` rendert correct de leeg-state.

De vijf vraag-eenheden die in `content/studiemateriaal/2-7/index.md` §5 worden opgesomd (bericht van wijziging, vraag om inlichtingen, bewaarplicht, fiscale procedure bij vertrek uit België) komen uit examen 2024-1 maar zijn — naar inhoud — **WIB92-procedurevragen** die thuishoren onder **PO 2.5 (Fiscale procedure)**. De huidige toekenning aan PO 2.7 in het index-bestand is een interpretatie-keuze uit de oude norm; bij vernieuwing zou ik die vragen niet als PO 2.7-canoniek behouden.

### Implicaties voor §4 minicursus "Examen-radar"

- Volg de PO 1.8-aanpak: **niet** een tabel met patronen, maar een **heuristische sectie** die expliciet markeert dat er geen voorbeeldexamens beschikbaar zijn voor PO 2.7 en die op basis van de twee gevorderde kenniselementen-blokken + integratie-niveau voorspelt welk type vragen waarschijnlijk is.
- Voorzichtig zijn met de bestaande tabel in `index.md` §5: die vragen leveren weinig houvast voor PO 2.7-specifieke voorbereiding. Bij re-render: expliciet vermelden dat ze materieel onder fiscale procedure (PO 2.5) vallen en hier alleen verschijnen omdat de gewestelijke procedure analoge mechanica heeft.

### Heuristische examenverwachting

Op basis van integratie-niveau + de "gevorderd niveau + rechtspraak"-clausule in beide hoofdblokken + de drie taken-rolverdeling:

| Vermoed type | Onderbouwing |
|---|---|
| **"Welke overheid is bevoegd?"** — vragen met multi-gewestelijk feitencomplex (vennootschap Vlaanderen + vastgoed Wallonië + overlijden in Brussel) | Klassieke fiscaal-federalistische puzzel; sluit aan bij 2.7.taak.1 + 2.7.I.A.2 |
| **Reglementstoets** — "is deze gemeentelijke belasting wettig?" J/N + motivering aan gelijkheid/proportionaliteit/non-bis-in-idem | 2.7.II.A.1 + 2.7.II.A.2 vragen letterlijk om die toets; rechtspraak-clausule wijst hierop |
| **Bezwaarroute** — "welke administratie? welke termijn?" voor concrete heffing | Praktijkrelevant; de termijnen verschillen sterk per route (Vlabel 3 mnd · federaal 1 jr PB · college 3 mnd · Raad van State 60 dgn) |
| **Mini-berekening OV** met opcentiemen | Cijferzakboekje-vraag: KI × gewest-tarief × (1 + opcentiemen/100) — sluit aan bij 2.7.taak.2 |
| **"Overgedragen of autonoom?"** — kwalificatie + gevolg voor tariefvrijheid van het gewest | 2.7.I.A.1 + 2.7.I.A.3 — kennistest met praktijkrelevantie |
| **Beslisboom samenloop** — gemeentelijke leegstandsheffing naast Vlaamse leegstandsheffing bedrijfsruimten, mag dat? | 2.7.II.A toetst non-bis-in-idem expliciet via rechtspraak (WIB92 art. 464 + RvS-rechtspraak) |

Verzin **geen** concrete vragen — dit is heuristiek. Bij latere vrijgave examenvragen: minicursus + leerstukken updaten.

---

## 3. Leerstuk-voorstel

**Voorstel: 5 leerstukken**. Granulariteits-stelregel toegepast: **eerder samen dan splitsen**. Niet één leerstuk per gewest (3×) en niet één leerstuk per heffing (12+×) — de stabiele as is de **vier-bouwstenen-kapstok** uit het programma (bevoegdheid · regulatie · vestiging+invordering · geschillen). Die wordt twee keer afgelopen — voor gewest en voor lokaal — plus één leerstuk voor de **bevoegdheidskaders bovenaan**, één voor de **procedure-laag** die de drie niveaus integreert, en één voor de typische **autonome heffingen** die anders versnipperen.

### Leerstuk 1 — `wat-zijn-regionale-en-lokale-belastingen` (entry + bevoegdheidskader)

- **Vraag**: Wat is de fiscale driehoek federaal — gewest — gemeente, en wie mag wat heffen op welke grondslag?
- **Type**: entry-fiche (kader, doorklik-zwaar)
- **Gedekte taken/doelstellingen**: 2.7.taak.1.doel.1 (geïntegreerd advies-kader) · 2.7.taak.2.doel.1 (gevorderde concepten — kennis-fundament)
- **Gedekte kenniselementen**: 2.7.I.A.2 (fiscale bevoegdheid gemeenschappen + gewesten) · 2.7.I.B.4 (gemeenschapsbelastingen — kort) · 2.7.II.A.1 (bevoegdheid om te heffen)
- **Gedekte concepten**: `lokale-en-regionale-belastingen` (koepel) · `gewestelijke-fiscale-autonomie` · `lokale-fiscale-autonomie`
- **Rationale**: Zonder begrip van **wie wat mag heffen** blijft elke heffing een losse anekdote. Drie kaders (BFW + art. 170 GW + art. 41/162 GW) horen pedagogisch in één beweging — het zijn drie zijden van hetzelfde grondwettelijke driehoeksbouwwerk. Hier komen ook de drie principes (legaliteit · gelijkheid · non-bis-in-idem) eenmalig aan bod als gemeenschappelijk fundament; de andere leerstukken roepen ze terug.

### Leerstuk 2 — `gewestelijke-heffingen-overgedragen-en-autonoom` (techniek 1)

- **Vraag**: Welke gewestelijke heffingen bestaan, wat is het verschil tussen overgedragen en autonoom, en wat zijn de typische voorbeelden + tarieven-structuur?
- **Type**: techniek + overzicht-fiche (zwaarste leerstuk in het pakket — analoog aan `ratios-en-kengetallen` in PO 1.3)
- **Gedekte taken/doelstellingen**: 2.7.taak.2 (bijstaan bij verplichtingen — aangiftes OV, BIV, verkeer, leegstand) · 2.7.taak.2.doel.2 (relevante informatie verzamelen — KI, akten, voertuig-gegevens)
- **Gedekte kenniselementen**: 2.7.I.A.1 (overgedragen belastingen) · 2.7.I.A.3 (autonome belastingen) · 2.7.I.B.1-3 (regeling per gewest, in een vergelijkende tabel — niet 3 sub-secties)
- **Gedekte concepten**: `onroerende-voorheffing` · `kadastraal-inkomen` · `verkeersbelasting` · `belasting-inverkeerstelling` · `leegstandsheffing-bedrijfsruimten` · `planbatenheffing` (6 concepten — de werkpaarden van het gewest-niveau)
- **Rationale**: De vier soorten gewestelijke heffingen (vier in 2.7.I.A) en hun toepassing op de drie gewesten (2.7.I.B.1-3) horen pedagogisch in één tabel-dominant leerstuk. **Splitsen per heffing of per gewest creëert versnippering**: de stagiair leert net door OV-Vl naast OV-Br te zetten, en leegstand-Vl naast leegstand-Br. De *categorische dichotomie* (overgedragen ↔ autonoom) is het belangrijkste begrip dat dit leerstuk moet vestigen, want het bepaalt **tarieven-vrijheid** van het gewest. Aanvullende belastingverminderingen op PB (woonbonus Vlaanderen, chèque habitat Wallonië) raken dit, maar leven materieel in PO 2.1 — hier alleen kort vermelden. Mag tot ~4000 woorden lopen (vergelijkbaar met `hoe-consolideren` in PO 1.4 — "hoe-uitzondering" in leerstuk-schrijfregels).

### Leerstuk 3 — `gemeente-en-provinciebelastingen` (techniek 2 + reglementstoets)

- **Vraag**: Hoe heffen gemeente en provincie eigen belastingen, hoe ziet een geldig belastingreglement eruit, en welke typische lokale heffingen bestaan?
- **Type**: techniek + reglements-fiche
- **Gedekte taken/doelstellingen**: 2.7.taak.2 (compliance — aangifte sui-generis-belastingen, controle aanslagbiljet) · 2.7.taak.2.doel.1 (gevorderd toepassen — reglements-toetsing)
- **Gedekte kenniselementen**: 2.7.II.A.1 (bevoegdheid heffen) · 2.7.II.A.2 (belastingreglementering — formele + materiële wettigheid) · 2.7.II.A.3 (vestiging + invordering + vervolging) · 2.7.II.B.1 (gemeentebelastingen) · 2.7.II.B.2 (provinciebelastingen)
- **Gedekte concepten**: `lokale-belasting-reglement` · `gemeentebelastingen-sui-generis` · `aanvullende-gemeentebelasting-pb` · `gemeentelijke-opcentiemen-onroerende-voorheffing` · `provinciale-belastingen`
- **Rationale**: Lokaal niveau heeft één centrale leervraag die niet bij gewest leeft: **hoe toets je de wettigheid van een reglement?** Vier criteria (raadsbeslissing · formele bekendmaking · materiële toets aan gelijkheid/proportionaliteit · non-bis-in-idem WIB92 art. 464) zijn een vaste examen-favoriet in administratief recht. Drie hefboomtypes (aanvullende belasting op PB, opcentiemen op OV, sui generis) horen samen want ze leveren samen de **gemeentelijke financieringsmix** — splitsen geeft een gefragmenteerd beeld. Provinciale belastingen leven in dezelfde mechanica (alleen met afnemende relevantie sinds 2018 in Vlaanderen) en passen pedagogisch als laatste subsectie. **Mag niet groeien tot 4000 woorden** — het is breder dan leerstuk 2 maar minder technisch.

### Leerstuk 4 — `procedure-gewest-en-gemeente` (proces-fiche)

- **Vraag**: Hoe verloopt een geschil over een gewestelijke of lokale belasting — wie behandelt het bezwaar, welke termijnen gelden, en hoe loopt het door naar de rechtbank?
- **Type**: proces-fiche (analoog aan `controle-werkzaamheden-uitvoeren` in audit-clusters)
- **Gedekte taken/doelstellingen**: 2.7.taak.3 (vertegenwoordigen) · 2.7.taak.3.doel.1 (procesrisico + termijnen + gevolgen-afweging)
- **Gedekte kenniselementen**: 2.7.I.A.4 (vestiging + invordering gewestelijk) · 2.7.II.A.3 (vestiging + invordering + vervolging gemeentelijk) · 2.7.II.A.4 (regeling van geschillen)
- **Gedekte concepten**: `gewestelijke-fiscale-procedure` (Vlabel · Bruxelles Fiscalité · Walfin) + sub-concepten "Bezwaar tegen individuele aanslag" en "Bezwaar tegen het reglement zelf" uit `lokale-belasting-reglement`
- **Rationale**: Vier procedure-routes (federaal · Vlabel · Brussel/Wallonië-FOD · College B&S) met elk eigen termijnen + administraties + rechtsmiddelen vragen om een **integrerende processfiche** met beslisboom + termijntabel. Niet samenvoegen met leerstuk 2 of 3, want het is een **andere denkactie**: de stagiair die net de heffing technisch beheerst, schakelt over naar geschilbeheer-modus (advocaten-perspectief). De PO 2.5-procedure (federale algemene) blijft daarbuiten — hier alleen de gewest- + lokale eigenheden. ⚠️ Bron-verificatie nodig bij scripts-fase: Wet 24.12.1996 + Brusselse Ord. 6.3.2019 niet in RAG aangetroffen.

### Leerstuk 5 — `geintegreerd-advies-bij-vestigingskeuze-en-vermogenstransfer` (synthese)

- **Vraag**: Hoe geef je een geïntegreerd advies waarin federale, gewestelijke en lokale heffingen samen worden afgewogen — bij vestigingskeuze, vastgoedaankoop, vermogensoverdracht?
- **Type**: synthese-fiche (analoog aan `kritische-beoordeling-en-diagnose` in PO 1.3)
- **Gedekte taken/doelstellingen**: 2.7.taak.1 + 2.7.taak.1.doel.1 (geïntegreerd advies bij oprichting + bij vermogenstransacties)
- **Gedekte kenniselementen**: integreert leerstuk 1-4 op concrete cases; geen nieuwe primaire kenniselementen
- **Gedekte concepten**: synthese van alle bovenstaande concepten + cross-PO doorklikken naar `registratierechten`, `erfbelasting` (PO 2.6) en `gewestelijke-belastingverminderingen-pb` (PO 2.1)
- **Rationale**: Doelstelling 2.7.taak.1.doel.1 vraagt **integratie-niveau** — niet langer "ken je deze heffing", maar "weeg de keuze tussen Vlaanderen of Brussel voor een nieuwe vennootschap". Dit kan geen sub-sectie zijn want het is een **andere denkmodus**: van kennis naar advies, met vooruit-redeneren, samenloop-detectie en proceskosten-afweging. Drie typische case-types: (a) oprichting vennootschap — vestigingsplaats; (b) aankoop tweede verblijf in andere gewest; (c) familiale vermogensoverdracht (link naar PO 2.6 erfbelasting). Het PO bestaat omdat zonder dit niveau de cliënt een onvolledig advies krijgt — daarom verdient het een eigen leerstuk, niet een sectie van iets anders.

### Waarom niet 4 of 7?

- **Niet 4** (door leerstuk 1 te integreren in 2+3): dan verdwijnt het bevoegdheidskader als losstaand verhaal en moet elke heffing zijn eigen grondwet-toets opnieuw uitleggen. Bevoegdheidskader is *het* fundament van dit PO.
- **Niet 6** (door per gewest te splitsen, of door leegstand+planbaten apart te leggen): drie gewest-leerstukken dupliceren steeds dezelfde vier-bouwstenen-kapstok; pedagogisch wint vergelijken het van scheiden. Leegstand+planbaten zijn dochtertoepassingen van "autonome heffing" — als sub-secties van leerstuk 2 sterker dan apart.
- **Niet 7** met aparte sui-generis-fiche: sui generis past pedagogisch onder reglementstoets (leerstuk 3) want de toets is identiek — de inhoud van de heffing is bijzaak.

---

## 4. Gap-check

Matrix kenniselement × leerstuk:

| Kenniselement | Leerstuk 1 entry | Leerstuk 2 gewest | Leerstuk 3 lokaal | Leerstuk 4 proc | Leerstuk 5 advies | Status |
|---|---|---|---|---|---|---|
| 2.7.I.A.1 overgedragen | doorklik | ✅ kern | – | – | ✅ toepassen | OK |
| 2.7.I.A.2 bevoegdheid gemeenschappen+gewesten | ✅ kern | doorklik | – | – | ✅ toepassen | OK |
| 2.7.I.A.3 autonome | doorklik | ✅ kern (subsecties leegstand+planbaten) | – | – | – | OK |
| 2.7.I.A.4 vestiging+invordering gewest | – | doorklik | – | ✅ kern | – | OK |
| 2.7.I.B.1 Brussel | – | ✅ tabel | – | doorklik (Bruxelles Fiscalité) | – | OK |
| 2.7.I.B.2 Vlaanderen | – | ✅ tabel | – | doorklik (Vlabel) | – | OK |
| 2.7.I.B.3 Wallonië | – | ✅ tabel | – | doorklik (Walfin) | – | OK |
| 2.7.I.B.4 gemeenschapsbelastingen | ✅ kort | – | – | – | – | ⚠️ dun — bewust (marginaal in praktijk) |
| 2.7.II.A.1 bevoegdheid lokaal | ✅ kort | – | ✅ kern | – | – | OK |
| 2.7.II.A.2 belastingreglementering | – | – | ✅ kern (wettigheidstoets) | – | – | OK |
| 2.7.II.A.3 vestiging+invordering+vervolging lokaal | – | – | ✅ kern | doorklik | – | OK |
| 2.7.II.A.4 geschillen lokaal | – | – | doorklik | ✅ kern | – | OK |
| 2.7.II.B.1 gemeentebelastingen | – | – | ✅ kern (3 typen) | – | ✅ toepassen | OK |
| 2.7.II.B.2 provinciebelastingen | – | – | ✅ subsectie | – | – | OK |
| Taak 2.7.1 begeleiding oprichting | – | – | – | – | ✅ kern | OK |
| Taak 2.7.2 bijstaan verplichtingen | – | ✅ aangiftes | ✅ aangiftes | – | – | OK |
| Taak 2.7.3 vertegenwoordigen | – | – | – | ✅ kern | – | OK |

**Geen kritieke gaten.** Eén zwakke dekking (gemeenschapsbelastingen 2.7.I.B.4) is bewust dun gehouden — die heffingen zijn praktisch marginaal (gemeenschappen hebben hoofdzakelijk dotaties uit federale begroting, weinig eigen belastingen).

**Twee aanwijzingen voor scripts-fase**:
- Leerstuk 2 moet *expliciet* het overgedragen-vs-autonoom-onderscheid als rode draad nemen, anders verkruimelt het tot losse heffing-sub-secties.
- Leerstuk 3 moet *de wettigheidstoets als examenpunt* uitwerken (4 criteria) — niet als bijzaak van "wat doen gemeenten?".

---

## 5. Overzicht-skelet (ADR-036 vijf-secties)

Bestand: `content/studiemateriaal/2-7/index.md`. Hergebruikt grote delen van het huidige bestand (verhaal-secties zijn pedagogisch sterk geschreven), maar §3 + §4 herstructureren naar leerstuk-leesroute en §5 examen-radar voorzichtiger framing.

### §1 — Waarom dit vak?

Hergebruiken uit huidige `index.md` §1. Sterke punten behouden:
- "Niet alle belastingen zijn federaal" — directe motivatie
- Tabel "Hoe past dit in het bredere programma?" — uitbreiden met **PO 2.5 fiscale procedure** als rakend (algemene procedure vs gewestelijke eigenheden)
- Cliënt-scenario (verhuizing Antwerpen → Wallonië + tweede verblijf + leegstand handelsfonds) als concrete inleidende casus

### §2 — Wat is dit vak?

Vijf compacte sub-secties, elk eindigend met wikilink naar het bijhorende leerstuk:

- "De fiscale driehoek federaal — gewest — gemeente" → [[wat-zijn-regionale-en-lokale-belastingen]]
- "Twee categorieën gewestelijke heffing — overgedragen vs autonoom" → [[gewestelijke-heffingen-overgedragen-en-autonoom]]
- "Drie hefbomen op gemeentelijk niveau — aanvullende PB, opcentiemen OV, sui generis" → [[gemeente-en-provinciebelastingen]]
- "Eigen procedure-routes — wanneer welk loket?" → [[procedure-gewest-en-gemeente]]
- "Eén cliënt, drie niveaus — geïntegreerd advies" → [[geintegreerd-advies-bij-vestigingskeuze-en-vermogenstransfer]]

### §3 — Wat moet je kunnen + hoe pak je het aan

Vervang de huidige rol-lijsten ("Als adviseur ...", "Als boekhouder ...", "Als vertegenwoordiger ...") — die zijn nu in de minicursus *en* leven beter in leerstukken zelf via accountant-perspectief-blokken.

Nieuwe leesroute in 5 stappen:
1. Bevoegdheidskader (leerstuk 1)
2. Gewestelijke heffingen — overgedragen + autonoom + 3 gewest-vergelijking (leerstuk 2)
3. Lokaal niveau + reglementstoets (leerstuk 3)
4. Procedure-route bij geschil (leerstuk 4)
5. Synthese — geïntegreerd advies (leerstuk 5)

+ Verwijzing naar **samenvatting** voor herhaling en **oefening** voor doorwerk.

### §4 — Examen-radar (heuristisch)

Vervang huidige tabel die procedure-vragen uit examen 2024-1 lijst (die zijn materieel PO 2.5). Expliciet markeren:

> Voor PO 2.7 zijn er nog geen voorbeeldexamenvragen geclassificeerd. De vijf vragen uit examen 2024-1 die voorheen onder PO 2.7 stonden, raken inhoudelijk de algemene federale fiscale procedure (WIB92 art. 346 e.v., 354) en horen materieel onder PO 2.5. Pas wanneer het examen gewestelijke of lokale heffingen expliciet vraagt, verschijnen die hier.

Daaronder de heuristische verwachtings-tabel (zie §2 hierboven in dit skelet-document).

### §5 — Concepten cross-PO

Tabel — kleine update t.o.v. huidige `index.md`:

| Concept | Cross-PO | Waarom relevant elders |
|---|---|---|
| `onroerende-voorheffing` | PO 2.6 (vastgoed-overdracht) · PO 2.1 (eigen woning, federale vrijstelling) | Vastgoedheffing |
| `kadastraal-inkomen` | PO 2.1 (onroerend inkomen) | Grondslag PB-vak III + OV |
| `gewestelijke-fiscale-autonomie` | PO 2.6 (gewest-tarieven erfbelasting/registratie) | Verklaart tarief-verschillen |
| `aanvullende-gemeentebelasting-pb` | PO 2.1 (gezamenlijk belaste inkomsten als grondslag) | Verhoogt federale aanslag |
| `gewestelijke-fiscale-procedure` | PO 2.5 (algemene fiscale procedure) · PO 2.6 (bezwaar Vlabel) | Procedure-eigenheden gewest |
| `gewestelijke-belastingverminderingen-pb` | PO 2.1 (cascade gewest-deel in PB-berekening) | Materiële inhoud gewest-verminderingen |

---

## 6. Voorbeeldgroep

### Voorstel: **GEEN centrale voorbeeldgroep — losse mini-cases per leerstuk**

Dit is de kern-vraag voor sparring. Mijn aanbeveling: **geen Aurelia-achtige mock-groep** voor PO 2.7.

**Waarom geen centrale mock-case zoals voor PO 1.4 (Aurelia) of 1.8 (productie-mock)?**

1. **Fiscale leerstukken werken anders dan boekhoudkundige**. Aurelia is een **groep van vier vennootschappen met balansen + intercompany-relaties** — dat materiaal wordt door alle 6 PO 1.4-leerstukken hergebruikt (wie consolideren · methode kiezen · goodwill · eliminaties). De cijfers zijn een doorgaande draad. Voor 2.7 is er geen analoge "doorgaande financiële realiteit" die over alle 5 leerstukken meebeweegt — elke heffing heeft zijn eigen feiten (KI voor OV, voertuig voor verkeer, leegstand-inventaris voor leegstandsheffing, reglement-tekst voor wettigheidstoets, ...).
2. **Een fiscaal scenario heeft een korte tijdsboog**. Een gemeentebelasting-bezwaar leeft op één aanslag. Een gewest-erfbelasting leeft op één overlijden. Forceer je één persoon "Wouter De Smedt" doorheen alle 5 leerstukken, dan moet hij toevallig én verhuizen én een tweede verblijf hebben én leegstandhebben én een Brussels successierecht én een gemeentelijk bezwaar — dat wordt karikaturaal.
3. **Vergelijken werkt beter dan doorgaan**. Leerstuk 2 (gewest-heffingen vergelijken) en leerstuk 3 (gemeente-vs-provincie) zijn intrinsiek **vergelijkende** leerstukken — je hebt méér voorbeelden nodig (Vlaanderen vs Brussel vs Wallonië; gemeente A vs gemeente B), niet één diepere case.
4. **Leerstuk 5 (synthese-advies) verdient wél een gerichte case** — maar dat is dan een case voor **één leerstuk**, niet voor het hele pakket. Daar past iets als "cliënt Vermeulen, vennootschap in Vlaanderen, tweede verblijf in Knokke, weduwe in Wallonië" als illustratie van geïntegreerd advies.

**Wat dan wel?**

- **Losse mini-cases per leerstuk**, ontworpen om het specifieke leerpunt scherp te stellen. Voorbeelden:
  - Leerstuk 2: één **OV-berekening** met KI 2.000 + 1.500 opcentiemen Vl (cijfer-cas) + één **autonomie-vraag** "mag Vlaanderen het tarief van de erfbelasting bepalen?" (begrip-cas)
  - Leerstuk 3: één **wettigheidstoets** op een mock-reglement (4 criteria) + één **opcentiemen-vergelijking** twee gemeenten
  - Leerstuk 4: één **bezwaar-flowchart** "klant ontvangt aanslag Vlabel erfbelasting — wat doe je?"
  - Leerstuk 5: één **vestigingsadvies** (vennootschap kiest tussen Antwerpen en Brussel) + één **vermogenstransfer** (schenking aan kind in Wallonië)
- Eventueel een **gedeelde mini-cliënt-galerij** in `data/voorbeeldgroepen/po-2-7-fiscale-mini-cases.yaml` — niet één groep, maar 5-8 onafhankelijke mini-personages of -bedrijven die in verschillende leerstukken opduiken, elk met hun eigen feitenset. Light-weight datastructuur. **Heroverweeg of dit in `data/voorbeeldgroepen/` past, of dat het beter binnen elke leerstuk-script-YAML als ingebed voorbeeld leeft** (zie open vraag 1).

**Alternatief om te overwegen**: één case-galerij "**De familie Vermeulen**" of een **kustgemeente "Stranddorp"** als rode draad voor leerstuk 3 (gemeente) + leerstuk 5 (synthese) — niet voor alle leerstukken. Dat geeft een dunne herkenning zonder de cases te dwingen.

### Cijferzakboekje-strategie

PO 2.7 leunt sterk op cijfers die jaar-na-jaar wijzigen (KI-indexering · gemeentelijke tarieven · leegstands-tariefschijven · planbaten-progressie). Alle concrete bedragen moeten via **MCP `certificaid-tarieven`** opgehaald worden in de scripts-fase. Geen training-only-cijfers.

---

## 7. Themafiche-mapping en samenvatting

Volgens [ADR-039](adr/ADR-039-samenvatting-vervangt-themafiche.md): één PO-samenvatting per programmaonderdeel vervangt de cluster-themafiches.

### Drie bestaande themafiches → één samenvatting

Bestand: `data/samenvattingen/2-7.yaml` + `content/studiemateriaal/2-7/samenvatting.md`.

**Migratie-strategie**:

| Themafiche | Inhoud | Migreert naar samenvatting als |
|---|---|---|
| `gewestelijke-fiscaliteit.md` | Drie types · bevoegdheidstabel · aanknopingspunten · 5-jaarsregel erfbelasting · Vlabel/Brussel/Wallonië-verschillen | **Blok 1**: tabel "Drie types gewestelijke fiscaliteit" + bevoegdheidstabel "wie heft welke belasting?" |
| `gemeentelijke-belastingen.md` | Wettigheidstoets 4 criteria · drie hefbomen · sui-generis-voorbeelden · opcentiemen vergelijking | **Blok 2**: tabel "Drie hefbomen gemeentelijk" + decision-list "Wettigheidstoets in 4 vragen" |
| `fiscale-procedure-gewest-gemeente.md` | Mermaid-beslisboom · 4 routes · termijnen · gerechtelijke fase | **Blok 3**: mermaid-beslisboom routes + termijntabel |

**Voorgestelde samenvatting-structuur** (2-4 A4 printbaar, visueel-dominant per ADR-039):

1. Intro-callout (no-print)
2. Take-away: 5 bullets (bevoegdheidskaders · 2 categorieën gewest · 3 hefbomen gemeente · 4 procedure-routes · wettigheidstoets 4 criteria)
3. **Bevoegdheidsdiagram** "Federaal — gewest — gemeente" (mermaid of tabel)
4. **Tabel-blok "Drie types gewestelijke fiscaliteit"** — type · voorbeelden · BFW-grond · tariefvrijheid (uit `gewestelijke-fiscaliteit.md`)
5. **Tabel-blok "Drie hefbomen gemeentelijk"** — type · grondslag · tarief-bandbreedte (uit `gemeentelijke-belastingen.md`)
6. **Mermaid-beslisboom routes** (uit `fiscale-procedure-gewest-gemeente.md`)
7. **Termijntabel** voor bezwaar per route
8. **Wettigheidstoets-tabel** (4 criteria + voorbeeldfalen)
9. Valkuilen (opcentiemen ≠ %; gewest-tarief ≠ federaal; non-bis-in-idem-grenzen)
10. Verdieping (no-print): doorklik naar 5 leerstukken

**De drie themafiches** worden bij voltooien van de samenvatting **gearchiveerd** (geen verwijdering — kunnen handig zijn als bron of als cross-PO-verwijzing). Locatie: te bepalen — `content/themafiches/archive/`? Open vraag.

---

## 8. Oefening

### Past een 60-75 min oefening bij dit PO?

**Voorzichtige aanbeveling: ja, maar in een ander format dan PO 1.4 (Nordica-consolideren) of PO 1.8 (kostprijscasus).**

**Verschilpunt**: een PO 1.4-oefening gaat door **één lange procedurele draad** (eliminaties, dochteropname, goodwill, presentatie). Voor PO 2.7 ontbreekt zo'n draad — fiscale leerstukken zijn meer **kennis-toepassen-op-feiten** dan **lange procedure**.

**Voorstel: oefening als "fiscaal multi-case-dossier"**

Format: één cliënt met **4-5 onafhankelijke fiscale vragen** die elk leerstuk activeren. Bijvoorbeeld:

- **Cliëntcontext**: BV Vlaamse landbouwer Vandenberghe, eigenaar van (a) eigen woning in Lier · (b) verhuurde studio in Knokke · (c) leegstaande bedrijfsruimte in Aalst · (d) waarvan grond herbestemd werd door RUP · (e) wagenpark met 3 voertuigen
- **Vraag 1** (leerstuk 1+2): welke gewestelijke heffingen treffen hem? Voor elk: bedrag-orde + bevoegde administratie.
- **Vraag 2** (leerstuk 2): hij overweegt verhuizing naar Brussel — vergelijk OV-tarief Vl vs Br op zijn studio. Mini-berekening.
- **Vraag 3** (leerstuk 3): de gemeente Lier heft een hondenbelasting met progressieve tariefschijf naar aantal honden, met vrijstelling voor blindengeleidehonden — wettigheidstoets in 4 criteria.
- **Vraag 4** (leerstuk 4): hij ontvangt aanslagbiljet planbatenheffing — hij betwist. Welke route, welke termijn, bij wie?
- **Vraag 5** (leerstuk 5): hij plant schenking van Knokke-studio aan dochter (woonachtig Wallonië) — geïntegreerd advies.

**Tijdbudget**: 75 minuten — 15 min per vraag. **Geen hints in opgave** (per oefening-procedure ADR). Modelantwoord apart in tweede markdown.

**Niet-doelstelling**: geen volledige reglements-tekst-schrijven, geen multi-jaars-vergelijking — die zouden in een tweede oefening kunnen leven.

**Alternatief**: oefening overslaan (zoals PO 1.8 momenteel doet?) en wachten tot een vrijgegeven examenvraag het format dicteert. Acceptabel maar geeft de stagiair minder doorwerk-materiaal — niet aanbevolen.

---

## 9. Open vragen voor sparring

1. **Voorbeeldgroep — bevestiging "geen centrale mock"?**
   - Voorstel: geen Aurelia-equivalent. Losse mini-cases per leerstuk, eventueel ingebed in leerstuk-script-YAML.
   - Alternatief: één "kustgemeente Stranddorp" of "familie Vermeulen" als rode draad door leerstuk 3 + 5. Dunne herkenning, niet alle leerstukken.
   - Beslissing nodig voor: aanmaak `data/voorbeeldgroepen/<naam>.yaml` of niet.

2. **Leerstuk-aantal — 5 of 4?**
   - 5 zoals voorgesteld (entry · gewest · lokaal · procedure · synthese-advies).
   - Alternatief 4: leerstuk 1 (entry) integreren in leerstuk 2 (gewest), startend met bevoegdheidskader. Risico: bevoegdheidskader = gemeenschappelijk fundament voor gewest **én** lokaal, hoort niet onder één van beide.
   - Alternatief 6: leerstuk 5 (synthese-advies) splitsen in "vestigingsadvies" + "vermogensadvies". Beide vragen om vooruit-redeneren, maar de denkmethode is identiek — splitsen levert dubbele bouwsteen-uitleg.

3. **Leerstuk 5 grens met PO 2.6**?
   - Vermogenstransfer raakt registratierechten + erfbelasting — die leven materieel in PO 2.6.
   - Voorstel: in PO 2.7 alleen de **bevoegdheidskeuze-component** (welk gewest? wat is gevolg van die keuze?), niet de inhoudelijke tarieven of vrijstellingen. Cross-PO doorklik naar 2.6 voor de techniek.
   - Risico: bij overdrachten zonder PO 2.6-kennis blijft de oefening kunstmatig.

4. **Bestaande huidige `content/studiemateriaal/2-7/index.md`** — gedeeltelijk hergebruiken (verhaal §1+§2) of opnieuw schrijven?
   - Voorstel: §1 + §2 grotendeels behouden (pedagogisch sterk), §3 herstructureren naar leerstuk-leesroute, §4 examen-radar opnieuw schrijven (voorzichtiger framing), §5 cross-PO uitbreiden met PO 2.5.

5. **Examen-vragen-tagging** — moeten de vijf "2024-1"-vragen onder PO 2.7 worden gewist of getagd naar PO 2.5?
   - Voorstel: re-classificeren naar PO 2.5 in `data/programma/examen_vragen/_interpretaties/`. Bij re-render verdwijnen ze automatisch uit `content/studiemateriaal/2-7/voorbeeldexamenvragen.md`.
   - Vereist beslissing van mens — niet door scripts-fase op te lossen.

6. **Themafiches archiveren — wanneer + waarheen?**
   - Voorstel: bij voltooien samenvatting → verplaatsen naar `content/themafiches/archive/po-2-7/`. Lokken niet meer via explorer, maar blijven leesbaar als historische bron.
   - Bij ADR-039 amendement-overleg expliciet bevestigen.

7. **Cijfer-discipline** — alle bedragen (KI-indexering, opcentiemen, BIV-tarieven, leegstands-tariefschijven, planbaten-schijven) via MCP `certificaid-tarieven` of Cijferzakboekje-doorklik. Bevestigen als beleid voor de scripts-fase.

8. **Rechtspraak-laag — verplichten in elk leerstuk?**
   - Het programma vraagt "gevorderd niveau + rechtspraak" voor beide hoofdblokken. Klassieke arresten (bv. GH-arrest gemeentebelasting × gelijkheidsbeginsel; Cassatie over Vlabel-procedure) kunnen examen-stof zijn.
   - Voorstel: scripts-fase moet per leerstuk **minstens 1 referentie-arrest** integreren in een "Klassieke rechtspraak"-blok. Bevestigen.

9. **Wet 24.12.1996 en Brusselse Codex Fiscale Procedure (Ord. 6.3.2019)** zijn **niet aangetroffen in de RAG-bronnen-corpus** (alleen via concept-records vermeld). Beleid: vóór scripts-fase ETL-pass om deze twee primaire bronnen in te lezen, óf werken met concept-records als enige bron + ⚠️ te verifiëren markering.

---

## Rapport

- **5 leerstukken voorgesteld**: entry+bevoegdheidskader · gewest-heffingen overgedragen+autonoom · gemeente+provincie+reglementstoets · procedure gewest+gemeente · geïntegreerd advies.
- **Hoofdtaak**: 2.7.taak.2 — bijstaan bij gewestelijke + lokale fiscale verplichtingen. Niveau **integratie** (hoogste).
- **Gaten t.o.v. programma**: geen kritieke. Eén bewust dunne dekking (2.7.I.B.4 gemeenschapsbelastingen — marginaal in praktijk).
- **Voorbeeldgroep**: aanbevolen **niet** te bouwen — losse mini-cases per leerstuk, eventueel een dunne "kustgemeente" of "familie" als bindweefsel voor leerstuk 3+5. Aurelia-model past slecht bij fiscale leerstof.
- **Themafiche-migratie**: drie bestaande themafiches (`gewestelijke-fiscaliteit` · `gemeentelijke-belastingen` · `fiscale-procedure-gewest-gemeente`) integreren in één samenvatting volgens ADR-039. Goede content-fit, geen herwerking nodig — wel her-arrangeren in printbaar 2-4 A4 format.
- **Oefening**: aanbevolen — fiscaal multi-case-dossier (één cliënt, 4-5 onafhankelijke vragen, ~75 min). Andere structuur dan PO 1.4/1.8 omdat fiscale leerstof geen lange procedurele draad biedt.
- **Belangrijkste onzekerheid**: (a) of "geen centrale voorbeeldgroep" pedagogisch echt beter werkt of dat een dunne case wel waarde toevoegt; (b) of de vijf "2024-1"-examenvragen blijven onder PO 2.7 of geherclassificeerd worden naar PO 2.5.
- **Volgende stap**: sparring met mens → beslissingen rond voorbeeldgroep-vorm + examen-vragen-classificatie → één Opus-run voor alle 5 leerstuk-scripts (ADR-037 amendement B) + samenvatting-YAML uit themafiche-inhoud + oefening-YAML.
