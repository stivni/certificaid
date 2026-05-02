---
tags: ["1.3", wip, competentie]
niveau: integratie
status: draft
programmaonderdelen: ["1.3"]
itaa-lex-secties:
  - XV (WVV art. 2:52, 5:153, 7:228–7:229 — alarmbelprocedure)
  - XIII (WER art. XX.23 — meldingsplicht bij continuïteitsrisico)
bouwversie: 0
---

# Continuiteit beoordelen

Aan de hand van de jaarrekening en andere beschikbare informatie het continuïteitsrisico vaststellen, beoordelen of de wettelijke drempelwaarden bereikt zijn, en de bijhorende verplichtingen van het bestuursorgaan en de beroepsbeoefenaar correct opvolgen.

> [!info]- Grondslag van deze werkwijze (🤖 60% · ⚖️ 40%)
> Er bestaat geen ITAA-norm die de volledige continuïteitsbeoordeling als taakprocedure beschrijft. De procedure combineert drie bronnen:
> - **Wettelijke verplichtingen** (stap 4–5): de [[continuiteitsrisico#-alarmbelprocedure|alarmbelprocedure]] en de [[continuiteitsrisico#-meldingsplicht-van-de-beroepsbeoefenaar|meldingsplicht bij continuïteitsrisico]] zijn volledig genormeerd in WVV en WER — de stappen en termijnen zijn niet vrij te kiezen.
> - **Analytisch referentiekader** (stap 1–3): signaalherkenning en weging van "gewichtige en overeenstemmende feiten" zijn niet genormeerd. **ISA 570** biedt een internationaal referentiekader, maar is voor GA/GBA niet bindend.
> - **Geconstrueerde stappen** (stap 2–3): beoordeling op misleidend karakter van signalen is analytische praktijk 🤖.

## Aanbevolen werkwijze

### 1. 🔎 Signalen inventariseren

> 📥 **Nodig**:
> - Jaarrekening (huidig jaar + vergelijkend vorig jaar indien beschikbaar)
> - Toelichting en bijkomende informatie in de opdracht (contracten, procedures, personeelswijzigingen)

> 📤 **Uitkomst**:
> - Overzicht van aanwezige financiële, operationele en juridische signalen

**Waarom**: zonder een volledig signalenoverzicht loop je het risico een gewichtig feit te missen dat stap 3 of 4 triggert — en daarmee een wettelijke verplichting.

Stel een overzicht op van alle signalen in drie categorieën (financieel, operationeel, juridisch). Volledig overzicht per categorie met voorbeelden: [[continuiteitsrisico#-signalen-van-continuïteitsrisico|Signalen van continuïteitsrisico]].

---

### 2. 🚩 Signalen beoordelen op misleidend karakter

> 📥 **Nodig**:
> - Lijst van signalen uit stap 1
> - Context: branche, leeftijd onderneming, recente investeringen, seizoenspatroon

> 📤 **Uitkomst**:
> - Beoordeling per signaal: reëel continuïteitsrisico of verklaarbaar door tijdelijke omstandigheid

**Waarom**: een verkeerde diagnose heeft twee gevaren: onterechte onrust bij het bestuursorgaan als een tijdelijk signaal als structureel wordt behandeld, of een gemiste alarmbelplicht als een misleidend signaal als onschuldig wordt afgedaan.

Beoordeel per signaal of er een aannemelijke tijdelijke verklaring is. [[continuiteitsrisico#-misleidende-continuïteitssignalen|Uitgewerkte patronen per type misleidend signaal]] (groeipijn, seizoenseffect, éénmalige capex).

> [!warning]- Eén negatief signaal gelijkstellen aan een continuïteitsrisico
> ❌ *"De current ratio is onder 1 — er is een continuïteitsrisico."*
>
> Continuïteitsrisico vereist "gewichtige **en** overeenstemmende feiten" ([[wetteksten/XV-wvv#art-252|WVV art. 2:52]]). Eén afwijkende ratio is geen continuïteitsrisico — het is een signaal dat nader onderzoek rechtvaardigt. Pas als meerdere signalen in dezelfde richting wijzen, én er geen aannemelijke tijdelijke verklaring is, is er een continuïteitsrisico.
>
> 🤖 *AI-aanvulling*

---

### 3. 🔀 Feiten wegen op gewichtigheid

> 📥 **Nodig**:
> - Gecorrigeerde lijst van reële signalen uit stap 2

> 📤 **Uitkomst**:
> - Oordeel: ja (ga naar stap 4) of nee (documenteer en monitor)

**Waarom**: de wet vereist "gewichtige én overeenstemmende feiten" ([[wetteksten/XV-wvv#art-252|WVV art. 2:52]]) als drempel — pas als aan beide criteria voldaan is, zijn de verplichtingen van stap 4 en 5 getriggerd.

"Gewichtig en overeenstemmend" betekent dat de signalen:
- Voldoende ernstig zijn om op zichzelf al bezorgdheid te rechtvaardigen (*gewichtig*)
- Consistent in dezelfde richting wijzen (*overeenstemmend*) — niet dat één signaal goed en één slecht is

Als de feiten gewichtig én overeenstemmend zijn → ga naar stap 4.

Als de feiten individueel of tegengesteld zijn → documenteer de bevindingen, formuleer aanbevelingen voor de cliënt, en plan een vervolgbeoordeling.

---

### 4. 🔀 Alarmbeldrempel controleren

> 📥 **Nodig**:
> - Vennootschapsvorm (BV, NV, of andere)
> - [[nettoactief|Nettoactief]] (= boekhoudkundig eigen vermogen)
> - Geplaatst kapitaal (enkel relevant bij NV)

> 📤 **Uitkomst**:
> - Ja/nee per drempel, met de toepasselijke wetsbepaling

**Waarom**: de wet verbindt dwingende proceduregevolgen aan het bereiken van specifieke drempels — dit is geen analytisch oordeel maar een wettelijke trigger die geen ruimte laat voor interpretatie.

De drempels verschillen per vennootschapsvorm:

**BV** ([[wetteksten/XV-wvv#art-5153|WVV art. 5:153]]):
- [[nettoactief|Nettoactief]] is negatief of dreigt negatief te worden, **of**
- Onzekerheid of schulden de komende 12 maanden betaald kunnen worden

**NV** ([[wetteksten/XV-wvv#art-7228|WVV art. 7:228–7:229]]):
- [[nettoactief|Nettoactief]] < **50%** van het geplaatst kapitaal → algemene vergadering bijeenroepen
- [[nettoactief|Nettoactief]] < **25%** van het geplaatst kapitaal → AV kan ontbinden met ¼ van de stemmen
- [[nettoactief|Nettoactief]] < **€ 61.500** → elke belanghebbende kan ontbinding vorderen

Als een drempel bereikt is → **alarmbelprocedure door het bestuursorgaan** (ga naar stap 5a).
Als geen drempel bereikt maar feiten zijn gewichtig en overeenstemmend → **[[continuiteitsrisico#-meldingsplicht-van-de-beroepsbeoefenaar|meldingsplicht bij continuïteitsrisico]]** kan al spelen (ga naar stap 5b).

> [!warning]- Alarmbelprocedure en meldingsplicht bij continuïteitsrisico verwarren
> ❌ *"Als het [[nettoactief|nettoactief]] negatief is, moet de accountant de rechtbank inlichten."*
>
> De alarmbelprocedure (bijeenroeping AV, bijzonder verslag) is een **verplichting van het bestuursorgaan** — niet van de beroepsbeoefenaar. De beroepsbeoefenaar heeft een eigen, aparte [[continuiteitsrisico#-meldingsplicht-van-de-beroepsbeoefenaar|meldingsplicht bij continuïteitsrisico]] ([[wetteksten/XIII-wer/boek-xx#art-xx23|WER art. XX.23]]). Die twee procedures zijn onderscheiden: het bestuursorgaan roept de AV bijeen; de GA stuurt bij onvoldoende reactie een aangetekende brief aan de bestuurders, en daarna eventueel een melding aan de rechtbank.
>
> 📝 *Terugkerende valkuil — zie ook [[continuiteitsrisico#-meldingsplicht-van-de-beroepsbeoefenaar|Meldingsplicht beroepsbeoefenaar]]*

> [!warning]- Alarmbelprocedure = faillissement
> ❌ *"Als de alarmbelprocedure loopt, gaat de vennootschap failliet."*
>
> De alarmbelprocedure is een wettelijke procedure om het bestuursorgaan te verplichten herstelmaatregelen te bespreken met de algemene vergadering. Ze triggert geen faillissement — ze is juist bedoeld om dat te voorkomen. Een negatief [[nettoactief|nettoactief]] = procedure starten, niet sluiting.
>
> 📝 *Terugkerende valkuil — zie ook [[continuiteitsrisico#-misleidende-continuïteitssignalen|Misleidende signalen]]*

---

### 5a. 📋 Alarmbelprocedure door het bestuursorgaan

> 📥 **Nodig**:
> - Vaststelling uit stap 4 dat de wettelijke drempel bereikt is

> 📤 **Uitkomst**:
> - Overzicht van de verplichte procedurestappen voor het bestuursorgaan

**Waarom**: de [[beroep-van-accountant-en-belastingadviseur|beroepsbeoefenaar]] heeft een controleplicht op de naleving van de wettelijke alarmbelprocedure — als die niet wordt nageleefd, zijn bestuurders aansprakelijk en kan de beroepsbeoefenaar zijn eigen meldingsplicht activeren.

Controleer als beroepsbeoefenaar of het bestuursorgaan de volgende stappen heeft uitgevoerd of uitvoert — het bestuursorgaan is de verantwoordelijke actor, **niet de beroepsbeoefenaar** zelf:

1. Bijeenroeping van de **algemene vergadering** binnen **2 maanden** na vaststelling ([[wetteksten/XV-wvv#art-5153|WVV art. 5:153]], [[wetteksten/XV-wvv#art-7228|WVV art. 7:228]])
2. Opstellen van een **bijzonder verslag** met herstelmaatregelen, tenzij ontbinding wordt voorgesteld
3. De AV beslist over de voorgestelde maatregelen of over ontbinding

Na naleving: geen nieuwe verplichting gedurende de volgende **12 maanden** voor dezelfde reden.

Bestuurders die de procedure niet naleven zijn aansprakelijk voor schade aan derden, tenzij ze het tegendeel bewijzen. ([[wetteksten/XV-wvv#art-5153|WVV art. 5:153 §3]])

De rol van de beroepsbeoefenaar hier is **adviseur**: hij informeert het bestuursorgaan over de toepasselijke procedure, maar voert ze niet zelf uit.

---

### 5b. 🔒 Meldingsplicht bij continuïteitsrisico

> 📥 **Nodig**:
> - Vaststelling van "gewichtige en overeenstemmende feiten" bij de normale uitoefening van de opdracht

> 📤 **Uitkomst**:
> - Aangetekende brief aan elk bestuurslid

**Waarom**: de meldingsplicht is een eigen wettelijke verplichting van de [[beroep-van-accountant-en-belastingadviseur|beroepsbeoefenaar]] — los van de alarmbelprocedure van het bestuursorgaan. Uitblijven ervan kan zijn persoonlijke aansprakelijkheid triggeren.

De [[continuiteitsrisico#-meldingsplicht-van-de-beroepsbeoefenaar|meldingsplicht]] van de gecertificeerd accountant (GA) is geregeld in WER art. XX.23 §3. Ze geldt bij vaststelling **in de normale uitoefening van de opdracht** — er is geen actieve onderzoeksplicht.

**Procedure**:
1. **Aangetekende brief** aan elk lid van het bestuursorgaan, met vermelding van de vastgestelde feiten en de gevraagde maatregelen (ook per gewone brief aan elk lid afzonderlijk)
2. **Responstermijn: 1 maand**

> [!warning]- ISA 570 als juridische grondslag vermelden
> ❌ *"Volgens ISA 570 moet de accountant de continuïteit beoordelen en eventueel de rechtbank inlichten."*
>
> ISA 570 is een IBR-auditstandaard (internationale standaard voor bedrijfsrevisoren). Ze is niet bindend voor gecertificeerde accountants (GA). De wettelijke grondslag voor de Belgische GA is **WER art. XX.23** en het WVV. ISA 570 kan als referentiekader voor de analysemethode dienen, maar mag nooit als juridische grondslag voor de [[continuiteitsrisico#-meldingsplicht-van-de-beroepsbeoefenaar|meldingsplicht bij continuïteitsrisico]] worden vermeld.
>
> 📝 *Terugkerende valkuil*

---

### 5c. 🔒 Melding aan de ondernemingsrechtbank (indien geen reactie)

> 📥 **Nodig**:
> - Verstuurde aangetekende brief uit stap 5b
> - Verstreken responstermijn van 1 maand zonder voldoende reactie, OF vaststelling dat faillissement op korte termijn onvermijdelijk lijkt

> 📤 **Uitkomst**:
> - Melding aan de voorzitter van de ondernemingsrechtbank

**Waarom**: de meldingsplicht bij continuïteitsrisico is tweefasig — de aangetekende brief is de eerste kans voor het bestuursorgaan om te reageren; pas bij uitblijven van reactie of bij imminente insolventie escaleert de verplichting naar de rechtbank.

De melding aan de voorzitter van de ondernemingsrechtbank is het sluitstuk van de [[continuiteitsrisico#-meldingsplicht-bij-continuïteitsrisico-wer-art-xx23|meldingsplicht bij continuïteitsrisico]] ([[wetteksten/XIII-wer/boek-xx#art-xx23|WER art. XX.23 §3]]).

---

## Voorbeelden

> [!example]- BV met negatief nettoactief — beoordeling en procedure
>
> **Situatie**: een kleine BV toont na herwerking: eigen vermogen = −€ 45.000 (negatief [[nettoactief|nettoactief]]). Current ratio = 0,65; dalende omzet over drie jaar; twee sleutelklanten verloren. Geen seizoenspatroon of grote investering.
>
> **Conclusie**: gewichtige en overeenstemmende feiten aanwezig; wettelijke alarmbeldrempel bereikt; alarmbelprocedure vereist; [[continuiteitsrisico#-meldingsplicht-van-de-beroepsbeoefenaar|meldingsplicht bij continuïteitsrisico]] (GA) geactiveerd.
>
> **Grondslag**: [[wetteksten/XV-wvv#art-5153|WVV art. 5:153]] (alarmbeldrempel BV: negatief [[nettoactief|nettoactief]]); [[wetteksten/XIII-wer/boek-xx#art-xx23|WER art. XX.23 §3]] (meldingsplicht bij continuïteitsrisico)
>
> **Redenering**: (1) Signalen: negatief EV, slechte liquiditeit, verlies klanten, dalende omzet — meerdere signalen, alle in dezelfde richting. (2) Geen misleidende verklaring: geen seizoenspatroon, geen recente capex, geen groeipijn. (3) Feiten zijn gewichtig én overeenstemmend. (4) Drempel BV bereikt: [[nettoactief|nettoactief]] is negatief. (5a) Bestuursorgaan moet AV bijeenroepen binnen 2 maanden. (5b) GA stuurt aangetekende brief aan elk bestuurslid; bij geen reactie binnen 1 maand → melding aan voorzitter ondernemingsrechtbank.
>
> 🤖 *AI-aanvulling*

> [!example]- NV met nettoactief net onder 50% — alleen procedure, geen meldingsplicht (nog)
>
> **Situatie**: een NV heeft geplaatst kapitaal van € 500.000 en een [[nettoactief|nettoactief]] van € 230.000 (= 46% van het kapitaal). Operationele kasstromen zijn positief. Eén moeilijk jaar door éénmalige reorganisatiekosten. Verwachting: terugkeer naar normaal in volgend boekjaar.
>
> **Conclusie**: alarmbeldrempel 50% bereikt (procedure bestuursorgaan vereist); maar feiten zijn nog niet "gewichtig en overeenstemmend" voor [[continuiteitsrisico#-meldingsplicht-van-de-beroepsbeoefenaar|meldingsplicht bij continuïteitsrisico]] (GA) — de situatie is verklaarbaar en tijdelijk.
>
> **Grondslag**: [[wetteksten/XV-wvv#art-7228|WVV art. 7:228]] (alarmbeldrempel NV 50%); [[wetteksten/XIII-wer/boek-xx#art-xx23|WER art. XX.23 §3]] (meldingsplicht bij continuïteitsrisico — nog niet getriggerd)
>
> **Redenering**: het [[nettoactief|nettoactief]] is onder 50% → bestuursorgaan moet de AV bijeenroepen. Maar de positieve operationele kasstroom en de eenmalige aard van de verliezen maken dat de feiten niet "gewichtig en overeenstemmend" zijn in de zin van WVV art. 2:52. De GA informeert het bestuursorgaan over de procedure maar heeft zijn eigen [[continuiteitsrisico#-meldingsplicht-van-de-beroepsbeoefenaar|meldingsplicht bij continuïteitsrisico]] nog niet geactiveerd — hij monitort de situatie.
>
> 🤖 *AI-aanvulling*

---

## Motiveren op het examen

**Een volledig antwoord bevat:**
1. **Identificatie** van de gewichtige en overeenstemmende feiten — welke signalen, uit welke bron
2. **Beoordeling** of er een aannemelijke niet-alarmerende verklaring is
3. **Bepaling** of de wettelijke drempel bereikt is (welke wetsbepaling, welke vennootschapsvorm)
4. **Procedure bestuursorgaan**: wie roept de AV bijeen, binnen welke termijn, wat staat in het bijzonder verslag
5. **[[continuiteitsrisico#-meldingsplicht-van-de-beroepsbeoefenaar|Meldingsplicht bij continuïteitsrisico]]** (GA): aangetekende brief, termijn 1 maand, dan rechtbank — of nog niet getriggerd (en waarom)

Bij integratievragen geldt de motiveringsstructuur: **conclusie → grondslag → redenering**.

**Voorbeeldvragen**

> [!question]- Welke verplichting heeft de GA bij going concern-signalen?
>
> Een gecertificeerd accountant stelt bij de opmaak van de jaarrekening van zijn cliënt (een BV) vast dat de vennootschap al drie jaar verlies maakt, dat het [[nettoactief|nettoactief]] negatief is en dat de leveranciers dreigen hun krediet in te trekken. Hij stelt het bestuursorgaan hiervan op de hoogte in een gewone e-mail. Is dit voldoende?
>
> Juist of fout?
>
> > [!success]- Antwoord
> >
> > **Fout — de [[continuiteitsrisico#-meldingsplicht-van-de-beroepsbeoefenaar|meldingsplicht bij continuïteitsrisico]] is niet correct nageleefd.**
> >
> > De GA heeft bij vaststelling van gewichtige en overeenstemmende feiten een wettelijke [[continuiteitsrisico#-meldingsplicht-van-de-beroepsbeoefenaar|meldingsplicht bij continuïteitsrisico]] ([[wetteksten/XIII-wer/boek-xx#art-xx23|WER art. XX.23 §3]]). Die vereist een **aangetekende brief** aan elk lid van het bestuursorgaan afzonderlijk — een gewone e-mail volstaat niet. Bovendien moet de brief de vastgestelde feiten vermelden en de gevraagde maatregelen. Na 1 maand zonder voldoende reactie moet de GA de voorzitter van de ondernemingsrechtbank inlichten — als hij dat nalaat, riskeer hij zijn eigen aansprakelijkheid.
> >
> > *Zie: [[continuiteitsrisico#-meldingsplicht-van-de-beroepsbeoefenaar|Meldingsplicht bij continuïteitsrisico]]*
>
> 🤖 *AI-aanvulling*

> [!question]- Alarmbelprocedure NV: welke drempel?
>
> Een NV heeft een geplaatst kapitaal van € 400.000. Na het boekjaar bedraagt het [[nettoactief|nettoactief]] € 95.000. Welke procedure is van toepassing en wie voert ze uit?
>
> > [!success]- Antwoord
> >
> > **De drempel van 25% is bereikt — de AV kan ontbinden met ¼ van de stemmen.**
> >
> > [[nettoactief|Nettoactief]] / geplaatst kapitaal = 95.000 / 400.000 = **23,75%** → onder de 25%-drempel (WVV art. 7:228–7:229). Het bestuursorgaan moet de AV bijeenroepen binnen 2 maanden. Op die AV kan met ¼ van de stemmen ontbinding besloten worden. Het is het **bestuursorgaan** dat de procedure voert — niet de accountant. De accountant adviseert en heeft zijn eigen [[continuiteitsrisico#-meldingsplicht-van-de-beroepsbeoefenaar|meldingsplicht bij continuïteitsrisico]] ([[wetteksten/XIII-wer/boek-xx#art-xx23|WER art. XX.23]]), maar is niet verantwoordelijk voor de uitvoering van de alarmbelprocedure zelf.
> >
> > *Zie: [[continuiteitsrisico#-alarmbelprocedure|Alarmbelprocedure]]*
>
> 🤖 *AI-aanvulling*

> [!question]- Groeipijn of continuïteitsrisico?
>
> Een startup heeft na drie jaar: current ratio 0,75; negatieve vrije kasstroom; eigen vermogen positief maar dalend. De omzet is verdrievoudigd in drie jaar. De investeerders hebben recent een kapitaalronde van € 500.000 afgerond. Is er een continuïteitsrisico?
>
> Juist of fout?
>
> > [!success]- Antwoord
> >
> > **Niet noodzakelijk — de signalen zijn verklaarbaar door groeipijn, mits de kapitaalronde voldoende dekking biedt.**
> >
> > Een startup met sterke omzetgroei en een recente kapitaalronde vertoont klassieke groeipijnkenmerken: de werkkapitaalbehoefte groeit sneller dan de liquiditeiten. De current ratio < 1 en negatieve vrije kasstroom zijn in deze context geen "gewichtige en overeenstemmende feiten" die continuïteit in gevaar brengen — tenzij de kapitaalronde onvoldoende is om de komende 12 maanden te overbruggen. De beoordeling vraagt contextanalyse, niet louter ratio's.
> >
> > *Zie: [[continuiteitsrisico#-misleidende-continuïteitssignalen|Misleidende signalen — groeipijn]]*
>
> 🤖 *AI-aanvulling*

---

## Relevant voor

**[[1.3-analyse-en-kritische-beoordeling-jaarrekening|1.3 Analyse en kritische beoordeling van de jaarrekening]]**

Taken:
- *Analyse en beoordeling van de financiële situatie*
  - Kritisch bekijken van de jaarrekening
  - Voorstellen kunnen doen om de situatie te verbeteren of te controleren

Kenniselementen:
- II.C.5 — Falingspredictie / going concern
