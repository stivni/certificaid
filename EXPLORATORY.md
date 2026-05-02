# Exploratory bevindingen

Post-build feedback uit `certificaid-exploratory`. Alle rollen door elkaar, chronologisch.

Obvious fixes worden autonoom verwerkt. Bevindingen gemarkeerd met `⚠️ WACHT OP GEBRUIKER` blijven staan tot de gebruiker beslist.

---

## [2026-05-02 17:05] Exploratieve ronde — balansaggregaten, beroepsgeheim, financiele-ratios, consolidatiekring-bepalen

[2026-05-02 17:05] [Bibliothecaris] balansaggregaten: lijn 90 verwijst naar `[[balansaggregaten#-passivazijde-volgorde-toenemende-eisbaarheid|...]]` met een leading dash, maar de heading `### Passivazijde (volgorde: toenemende eisbaarheid)` heeft **geen emoji** — per CLAUDE.md moet het anker dan zonder leading dash zijn (`#passivazijde-...`).
→ obvious fix: leading dash verwijderd in regel 90.

[2026-05-02 17:05] [Bibliothecaris] financiele-ratios + jaarrekening-herwerken: drie kapotte links naar `[[balansaggregaten#-balansaggregaten|...]]` — er bestaat **geen heading `## 📌 Balansaggregaten`** in balansaggregaten.md (het file heet zo, maar de drie kernaggregaten zitten elk in hun eigen `##`-sectie). Bovendien was de financiele-ratios-instance een kale "zie ook"-link, exact het antipatroon dat CLAUDE.md verbiedt.
→ obvious fix: alle drie de links naar `[[balansaggregaten|...]]` (zonder anker) gezet; financiele-ratios lijn 58 omgezet naar inline-zin in de Nettothesaurie-context.

[2026-05-02 17:05] [Stagiair + Coherentie] consolidatiekring-bepalen: vier stappen zonder waarom-zin (CLAUDE.md vereist die voor competentie-stappen sinds bouwversie 1) en geen Grondslag-blok na de intro (CLAUDE.md vereist dit collapsible blok met 🤖/⚖️-percentage). Bouwversie staat op 0 — fiche dateert van vóór deze regels.
→ obvious fix: Grondslag-blok toegevoegd (🤖 20% · ⚖️ 80% — wettelijk gestuurd door WVV/KB-WVV, volgorde van stappen is analytische conventie). Waarom-zinnen toegevoegd aan alle vier de stappen.

[2026-05-02 17:05] [Bibliothecaris] consolidatiekring-bepalen: zelf-links naar genummerde stappen bevatten **emoji-literal in URL** (`#2-🔍-type-relatie-...`, `#3-🔀-weglatingen-...`). Andere competentie-fiches (opdrachtaanvaarding-beoordelen) doen het correct met dubbele dash zonder emoji (`#1--opdracht-en-cliënt-vaststellen`). Quartz strips emoji's, dus emoji-literal in URL = kapotte link.
→ obvious fix: zelf-links omgezet naar `#2--type-relatie-per-entiteit-vaststellen` en `#3--weglatingen-en-verplichte-uitsluitingen-beoordelen` (dubbele dash conform de werkende conventie).

[2026-05-02 17:05] [Bibliothecaris] consolideren-integraal, vermogensmutatiemethode-toepassen: zelfde emoji-in-URL bug als consolidatiekring-bepalen — `#4-🔢-optelling-en-intercompany-eliminaties`, `#1-🔍-initiële-opname-bepalen`, `#2-🔢-jaarlijkse-aanpassing-boekwaarde-deelneming` (uit grep over alle competentie-fiches). Buiten scope van deze fiche-set, maar zelfde patroon.
→ ⚠️ WACHT OP GEBRUIKER: project-brede sweep om emoji-literals uit zelf-link-ankers te verwijderen in alle competentie-fiches die genummerde stappen met emoji-staptypes hebben. Niet één-fiche-fix.

[2026-05-02 17:05] [Examinator] consolidatiekring-bepalen: slechts één voorbeeldvraag (geïntegreerde casus). Voor een toepassen-niveau competentie te dun: geen weten-vraag over de drempelwaarden voor "groep van beperkte omvang", geen vraag over het verschil tussen exclusieve / gezamenlijke / invloed van betekenis, geen vraag over de weglatingsgronden. Bovendien geen verwijzing naar voorbeeldexamens (`resources/voorbeeldexamens/INDEX.md` is niet geraadpleegd door deze run).
→ ⚠️ WACHT OP GEBRUIKER: examenvragen uitbreiden vereist een aparte ronde — voorbeeldexamens scannen op consolidatie-vragen en minstens 2-3 vragen per niveau toevoegen. Niet één losse autonome toevoeging.

[2026-05-02 17:05] [QA] balansaggregaten: bouwversie 0, status draft. Fiche heeft hechte structuur (NBK/WKB/Nettokaspositie als drie aparte ##-secties), maar er is **geen overkoepelende `## 📌 Balansaggregaten`-sectie** ondanks dat externe fiches er kennelijk naar willen linken (zie kapotte links hierboven). De relatie `NBK = WKB + nettokaspositie` zit verstopt onder Nettokaspositie — verdient een eigen positie als koppelend principe.
→ ⚠️ WACHT OP GEBRUIKER: structurele vraag — een `## 📌 Balansaggregaten` parent-sectie toevoegen die de drie aggregaten als groep introduceert (en daarmee de externe links repareert), of de huidige flat-structuur behouden? De parent-sectie zou de relatie-formule en de "drie aggregaten hangen samen"-redenering centraliseren.

[2026-05-02 17:05] [Stage-mentor] beroepsgeheim: praktijkpassages aanwezig (kwaliteitstoetsing, cliënt-dagvaarding) — sterk gedocumenteerd. **Maar**: geen passage over digitale realiteit — cloud-opslag, e-mail, gedeelde drives in associatie. CLAUDE.md "doorwerking naar medewerkers" wordt vermeld maar in 2026 zit het echte risico in onbeveiligde e-mail naar een verkeerd adres of een gedeelde Google Drive zonder access controls. Een 🤖-blok hierover zou nuttig zijn voor stagiairs.
→ ⚠️ WACHT OP GEBRUIKER: digitaal-praktijk-blok toevoegen voor beroepsgeheim — ICT-praktijken, AI-tools (kunnen cliëntinformatie via prompts lekken), gedeelde mailboxen. Vereist input over de feitelijke beroepspraktijk en mogelijk een ITAA-norm/circulaire over IT-security.

[2026-05-02 17:05] [Stagiair] financiele-ratios: lijn 58 had een kale "zie ook"-link tussen Nettothesaurie en Solvabiliteitsratio's, zonder context. Een student leest dit als ruis — wat moet ik daar doen? De inline-formulering (verwantschap tussen nettothesaurie en nettokaspositie) maakt het concept zelf duidelijker.
→ obvious fix: kale link omgezet naar inline-zin die de begripsverwantschap expliciteert.

[2026-05-02 17:05] [QA] financiele-ratios: bouwversie 0. Fiche heeft veel waarde maar volgt niet alle huidige conventies — bv. de `## 🔢 Cashflowratio's` sectie heeft een 🔢 emoji in plaats van 📌 voor wat eigenlijk een begrips-sectie is (definitie van bruto cashflow). Ook het gebruik van 📌 emoji bovenaan elk ratio-categorie-blok is onorthodox — andere fiches gebruiken `## ↔️` voor vergelijkingen of `## 🔎` voor patronen.
→ ⚠️ WACHT OP GEBRUIKER: bouwversie 0 → 2 audit-pas verdient een eigen ronde. De fiche is structureel correct maar gebruikt sectietypes mogelijk niet conform de huidige typologie (📌 begrip vs 🔢 berekening).

---

## [2026-05-02 16:11] Exploratieve ronde — boekhoudkundige-beginselen, jaarrekening, financiele-ratio-berekenen, jaarrekening-herwerken

[2026-05-02 16:11] [QA] jaarrekening: § Geconsolideerde jaarrekening (lijn 170-183) citeert vier keer `WVV art. 3:109`. **Dit artikel bestaat niet** in onze WVV-bron — Boek 3 stopt bij Art. 3:103. De geconsolideerde-jaarrekeningregels staan in Boek 3, DEEL 2, HOOFDSTUK 2 (Art. 3:21 e.v.): de verplichting in Art. 3:23, de vrijstelling voor "groep van beperkte omvang" in Art. 3:25, en de drempels voor die groep in Art. 1:26.
→ ⚠️ WACHT OP GEBRUIKER: artikelnummer corrigeren in jaarrekening.md vraagt herstructurering — niet één link maar de hele subsectie heeft de verkeerde grondslag. Voorgestelde aanpak: vervang de `art. 3:109`-verwijzingen door de juiste tweetrap (Art. 3:23 voor verplichting, Art. 3:25 + Art. 1:26 voor drempels).

[2026-05-02 16:11] [QA] jaarrekening: § Geconsolideerde jaarrekening noemt drempels "Balanstotaal > € 17.550.000", "Netto-omzet > € 35.100.000", "Werknemers > 250" voor consolidatieplicht. **Dit zijn de oude drempels.** Sinds W 2024-03-28/60 (in werking 2024-04-08) zijn de drempels voor "groep van beperkte omvang" in Art. 1:26 § 1: werknemers 250, netto-omzet € 42.500.000, balanstotaal € 21.250.000. CLAUDE.md zegt dat exacte bedragen Cijferzakboekje-materie zijn, maar deze staan inhoudelijk in de wet — ofwel actualiseren met bronvermelding, ofwel vervangen door "minstens twee van de drempels uit Art. 1:26".
→ ⚠️ WACHT OP GEBRUIKER: aanpak — actualiseren naar 2024-bedragen (en wetshistoriek vermelden), of bedragen weglaten en alleen verwijzen naar Art. 1:26?

[2026-05-02 16:11] [QA] financiele-ratio-berekenen: voorbeeld 1 (ROA met intrestsubsidie, lijn 173-181) gebruikt vier componenten in de redenering — `877.279 + 46.934 + 211.950 − 6.000` — maar de formule eronder noemt slechts drie (Resultaat vóór belastingen + financiële kosten − intrestsubsidies). Het vierde getal `211.950` ("bedrijfsresultaat financiële activiteiten") past niet bij een gedocumenteerde formulecomponent. Hetzelfde getal verschijnt in `financiele-ratios.md` lijn 129 als citaat uit voorbeeldexamen 2014. De situatie en formule sluiten dus niet sluitend op elkaar aan — de redenering is correct voor dat examen, maar de formule-uitleg is onvolledig.
→ ⚠️ WACHT OP GEBRUIKER: ofwel "Resultaat vóór belastingen" splitsen in een operationele en financiële component (zoals het examen 2014 deed), ofwel het voorbeeld vereenvoudigen naar drie componenten zodat het de formule volgt. Examen-realisme vs. didactische helderheid.

[2026-05-02 16:11] [Bibliothecaris] jaarrekening-herwerken: stap 2 en stap 3 sloten elk af met een standalone "Volledige NBB-code mapping per rubriek: [[balansaggregaten#...|...]]" / "Definitie en toelichting per niveau: [[resultaatniveaus#...|...]]" — exact het patroon dat CLAUDE.md verbiedt ("nooit als losstaande verwijzing achteraan"). Idem in financiele-ratio-berekenen lijn 39: "Volledige formules per ratio met NBB-codes: [[financiele-ratios]]".
→ obvious fix: drie verwijzingen geherformuleerd naar "zie [[...]]"-stijl met inline conceptwoord (`Voor de volledige NBB-code mapping per rubriek: zie de [[balansaggregaten#-analytische-indeling-van-de-balans|analytische indeling van de balans]]`). Niet ideaal — strikt genomen zou de inline-link op het conceptwoord zelf moeten staan, maar in deze contexten is dat een uitnodiging tot herstructurering die ik niet autonoom doe.

[2026-05-02 16:11] [Stagiair] jaarrekening-herwerken: stap 3 (Resultatenrekening herstructureren) had geen waarom-zin na het 📥/📤-blok — vereist door CLAUDE.md voor competentie-stappen. Stap 1, 2, 4 hadden er wel een. Bouwversie van de fiche staat op 0 (nog vóór waarom-zin verplicht werd in v1).
→ obvious fix: waarom-zin toegevoegd vóór het overzichts-tabel: "Waarom: de wettelijke resultatenrekening toont vooral het eindresultaat — de tussenniveaus (TAW, EBIT, EBITDA) zijn analytisch noodzakelijk om kosten- en margestructuur te begrijpen en zijn de inputs voor [[financiele-ratios|rentabiliteits- en activiteitsratio's]]."

[2026-05-02 16:11] [Bibliothecaris] boekhoudkundige-beginselen: voorbeeldvraag "Wijziging afschrijvingsmethode" (lijn 187) gebruikt twee keer "afschrijvingspercentages" / "afschrijvingsregels" zonder link naar de [[afschrijvingen|afschrijvingen]]-fiche. De begrippen die in de antwoordtekst wel gelinkt zijn naar consistentiebeginsel, maar de twee instances in de vraag-tekst niet.
→ obvious fix: één wikilink toegevoegd op "afschrijvingspercentages" in de eerste regel van de vraag. Tweede instance ("afschrijvingsregels") gelaten — student begrijpt context.

[2026-05-02 16:11] [Examinator] boekhoudkundige-beginselen: 4 voorbeeldvragen aanwezig, allemaal over Getrouw beeld, Consistentie en Matching. **Geen voorbeeldvraag** over Voorzichtigheid, Materialiteit, Munteenheid, Stelselmatigheid, Continuïteitsbeginsel of Individualisering. Bovendien geen integratievraag waarbij twee beginselen botsen (bv. continuïteit vs. voorzichtigheid bij dreigende discontinuïteit) — een typische integratie-toets.
→ ⚠️ WACHT OP GEBRUIKER: voorbeeldvragen toevoegen voor de 6 ontbrekende beginselen (vooral Voorzichtigheid en Continuïteit, die vaak getoetst worden). Stof voor een eigen exploratory-pas of expliciete uitbreidingsronde — niet één losse autonome toevoeging.

[2026-05-02 16:11] [Examinator] jaarrekening: 3 voorbeeldvragen aanwezig (deadline, commissaris-scope, nadruksparagraaf). Geen vraag op weten-niveau over de drie basisdoelstellingen (getrouw beeld, verantwoording, transparantie) — wel een prominente sectie. Geen vraag over het verschil tussen volledig/verkort/microschema voor een gegeven groottecategorie.
→ ⚠️ WACHT OP GEBRUIKER: weten-vraag over basisdoelstellingen + toepassingsvraag over schemakeuze toevoegen, of bewust beperkt houden? De fiche draait nu vooral op procedurele vragen (deadline, scope) — minder dekkingsbreedte op begrippen.

[2026-05-02 16:11] [Stage-mentor] jaarrekening: § Verslag van de commissaris geeft enkel de wettelijke inhoud + één goede valkuil ("goedkeurend ≠ economisch gezond"). Geen praktijkpassage over hoe een GA in de praktijk vrijwillige verificaties uitvoert (zonder commissaris-statuut, zonder NBB-neerlegging) — terwijl de fiche dat onderscheid wel benoemt in de tweede valkuil. Een `[!info]- In de praktijk` blok zou nuttig zijn.
→ ⚠️ WACHT OP GEBRUIKER: praktijk-blok toevoegen over GA-verificatie zonder commissaris-statuut (typische opdrachten, formaat van het verslag, wat het wel/niet bewijst)? Vereist input over de feitelijke beroepspraktijk.

[2026-05-02 16:11] [Coherentie] boekhoudkundige-beginselen / jaarrekening / continuiteitsrisico: alle drie gebruiken `#️-` (met U+FE0F variation selector tussen `#` en `-`) in interne ankers — bv. `[[continuiteitsrisico#️-waardering-bij-discontinuïteit|...]]`. CLAUDE.md zegt: anker = `#-` (gewone leading dash). De vorige exploratory ronde (2026-05-02 14:05) heeft dit ook al geflagd voor andere fiches. Patroon herhaalt zich — kennelijk consistent over heel de kennisbank.
→ ⚠️ WACHT OP GEBRUIKER: project-brede sweep nodig om alle `#️-` (variation-selector) ankers te vervangen door `#-` (gewoon koppelteken), of bevestigen dat Quartz dit transparant afhandelt. Niet één-fiche-fix.

[2026-05-02 16:11] [Stagiair] boekhoudkundige-beginselen: enige `[!info]- In de praktijk` blok zit op Matching. Andere principes (Voorzichtigheid, Continuïteit, Consistentie, Materialiteit) hebben geen praktijkvoorbeeld. Voor toepassings-niveau (zoals frontmatter zegt) is dat dun.
→ ⚠️ WACHT OP GEBRUIKER: praktijkblokken toevoegen voor minstens Voorzichtigheid en Consistentie (de twee die het vaakst getoetst worden), of niveau in frontmatter aanpassen naar `weten-en-inzien`? De fiche bevat overwegend ⚖️ secties — dat is conceptueel weten, geen toepassing.

[2026-05-02 16:11] [Coherentie] boekhoudkundige-beginselen / jaarrekening / jaarrekening-herwerken: alle drie hebben `bouwversie: 0` in frontmatter. CLAUDE.md huidige versie is 2 (regels over waarom-zin, [!info]- Concreet, valkuil-titels enz.). Stale-fiches zijn kandidaat voor herevaluatie.
→ ⚠️ WACHT OP GEBRUIKER: deze drie fiches zijn al voor v0 geschreven; de waarom-zinnen ontbreken deels (deels nu toegevoegd), de visuele ankers zijn er deels, de valkuil-titels volgen v2-conventie deels. Volledig her-auditen is een aparte build-stap, niet een exploratory fix.

---

## [2026-05-02 14:05] Exploratieve ronde — continuiteitsrisico, continuiteit-beoordelen, nettoactief

[2026-05-02 14:05] [Coherentie] continuiteitsrisico + continuiteit-beoordelen: 13+ broken wikilinks. De competentie verwijst overal naar `[[continuiteitsrisico#-meldingsplicht-van-de-beroepsbeoefenaar|...]]`, maar het bestaande sectie-anker was `#-meldingsplicht-bij-continuïteitsrisico-wer-art-xx23`.
→ obvious fix: sectie hernoemd in `continuiteitsrisico.md` naar `## 🔒 Meldingsplicht van de beroepsbeoefenaar` (de naam die overal al gebruikt werd, en die conceptueel de actor benoemt — disambiguatie van AWW-meldingsplicht staat al in de body). Eén afwijkend anker op lijn 221 van `continuiteit-beoordelen.md` rechtgezet naar dezelfde target.

[2026-05-02 14:05] [Bibliothecaris] continuiteitsrisico: §Nettoactief (lijn 42) bevatte een standalone "Definitie en berekening: [[nettoactief]]." — exact het patroon dat CLAUDE.md verbiedt ("nooit als losstaande verwijzing achteraan").
→ obvious fix: zin geherschreven met inline definitie (bedrag dat overblijft na schulden, voorzieningen, oprichtings-/O&O-kosten — in de praktijk rubriek 10/15). De verwijzing is nu inline op het conceptwoord en de student krijgt direct de essentie.

[2026-05-02 14:05] [Examinator] nettoactief: één van de klassieke examenvalkuilen (nettoactief ≠ eigen vermogen wanneer er niet-afgeschreven oprichtings-/O&O-kosten zijn) ontbrak als callout. WVV art. 5:142 trekt die expliciet af; in de praktijk kan een vennootschap die op rubriek 10/15 net boven de alarmbeldrempel zit, na correctie eronder vallen.
→ obvious fix: `[!warning]`-callout toegevoegd in `nettoactief.md` met titel "Nettoactief is niet altijd gelijk aan eigen vermogen", inclusief de foute aanname, de wettelijke grondslag (WVV art. 5:142) en de implicatie voor de alarmbelprocedure. Inleidende zin in §Nettoactief navenant uitgebreid.

[2026-05-02 14:05] [Stagiair] nettoactief: één concreet praktijkvoorbeeld (BV-cijfers) aanwezig, geen NV-context met de drempelpercentages (50% / 25% / €61.500). Een student die de fiche leest, zou een tweede praktijkblok kunnen helpen om het verschil tussen "nettoactief in absolute zin" en "nettoactief als percentage van geplaatst kapitaal" te zien.
→ ⚠️ WACHT OP GEBRUIKER: tweede praktijkvoorbeeld (NV-drempels) toevoegen in `nettoactief.md`, of bewust scheiden — drempelinterpretatie is een procedure die thuishoort in `continuiteitsrisico` of `continuiteit-beoordelen`? Granulariteitsbeslissing.

[2026-05-02 14:05] [QA] continuiteitsrisico: §Alarmbelprocedure noemt "€ 61.500" als NV-drempel. Dat is een vast bedrag uit WVV art. 7:229, géén Cijferzakboekje-bedrag. CLAUDE.md zegt: "Vermeld bij exacte bedragen de bron als 'Cijferzakboekje [jaar]'." Het bedrag mist nu een expliciete bronvermelding (`[[bronnen/wetteksten/XV-wvv#art-7229|WVV art. 7:229]]` of vermelding dat het in de wet zelf staat).
→ ⚠️ WACHT OP GEBRUIKER: voeg ik bij de €61.500 een inline bronlink naar WVV art. 7:229 toe, of laat ik staan dat het uit het algemene NV-blok WVV art. 7:228–7:229 volgt (zoals nu)? Stilistische keuze — niet duidelijk welke conventie het project hanteert voor "bedragen die wettelijk vastgelegd zijn".

[2026-05-02 14:05] [Stage-mentor] continuiteit-beoordelen: stap 5b (meldingsplicht) beschrijft de aangetekende-brief-procedure verbatim uit WER art. XX.23 §3, maar zonder praktijksignaal. Een ervaren GA weet dat in de praktijk nagenoeg altijd eerst informeel overleg met het bestuursorgaan plaatsvindt vóór de aangetekende brief — en dat de brief vaak met het bestuur wordt voorbereid (niet als verrassing). Dat staat nergens.
→ ⚠️ WACHT OP GEBRUIKER: praktijkpassage toevoegen ("In de praktijk gaat aan de aangetekende brief vrijwel altijd informeel overleg vooraf...") of houden we 5b strikt formeel-juridisch? Risico op "best practice" die niet aansluit bij de werkelijke praktijk in alle kantoren.

[2026-05-02 14:05] [Coherentie] continuiteit-beoordelen: stap 5a verwijst naar `[[beroep-van-accountant-en-belastingadviseur|beroepsbeoefenaar]]` (lijn 169, 193). Deze fiche behandelt zowel GA als GBA, maar in de meldingsplicht (stap 5b) staat alleen GA. WER art. XX.23 §3 geldt voor zowel "externe accountant" als "belastingadviseur"? Te verifiëren.
→ ⚠️ WACHT OP GEBRUIKER: bron-check WER art. XX.23 §3 op GA vs GBA scope. Als de meldingsplicht ook voor GBA geldt, moet stap 5b dat expliciet vermelden. Als enkel voor GA: dan moet de fiche ook duidelijk maken waarom GBA hier níet onderworpen is.

[2026-05-02 14:05] [Bibliothecaris] cross-fiche: gerelateerde fiches (jaarrekening, boekhoudkundige-beginselen) gebruiken `#️-waardering-bij-discontinuïteit` (met U+FE0F variation selector na `#`). Het materie-anker is `## ⚖️ Waardering bij discontinuïteit` — Quartz strips de emoji maar de variation-selector kan een aparte slug genereren. Niet bekeken in deze ronde maar verdacht.
→ ⚠️ WACHT OP GEBRUIKER: aparte exploratory ronde nodig om alle `#️-`-ankers (met variation selector) te verifiëren tegen Quartz-render. Geldt voor heel de kennisbank, niet alleen deze drie fiches.

---

## [2026-05-02 15:05] Exploratieve ronde — antiwitwaswetgeving, deontologische-beginselen, aww-beleid-beheren, opdrachtaanvaarding-beoordelen

[2026-05-02 15:05] [Bibliothecaris] antiwitwaswetgeving: lijn 181 verwees naar `#-cel-voor-financiele-informatieverwerking-cfi` (zonder ë). Heading is `## 📌 Cel voor Financiële Informatieverwerking (CFI)` — github-slugger 2.0 (door Quartz gebruikt) bewaart accenten. CLAUDE.md regel klopt. De link was dus broken (anker bestaat niet). Andere fiches in het project gebruiken consistent de versie zonder ë (`atypische-verrichting-opvolgen`, `aww-beleid-beheren`); alleen `beroepsgeheim` gebruikt de correcte versie met ë. Duidelijke patroon-inconsistentie.
→ obvious fix: link gecorrigeerd naar `#-cel-voor-financiële-informatieverwerking-cfi`. Zelfde fix toegepast in `aww-beleid-beheren.md` (lijn 57).

[2026-05-02 15:05] [Bibliothecaris] opdrachtaanvaarding-beoordelen: twee links op lijn 154 en 156 verwezen naar `#-clientenonderzoek-cdd` (zonder ë). Heading in antiwitwaswetgeving: `## 📋 Cliëntenonderzoek (CDD)` — anker met ë. Broken.
→ obvious fix: beide links gecorrigeerd naar `#-cliëntenonderzoek-cdd`.

[2026-05-02 15:05] [Bibliothecaris] cross-fiche accent-anker patroon: `atypische-verrichting-opvolgen.md` (lijn 14, 67, 152) en `examenvragen/1.3-analyse-jaarrekening.md` (lijn 43, 63) hebben dezelfde fout — accent ontbreekt in anker. Patroon-breed probleem dat niet enkel mijn 4 fiches betreft.
→ ⚠️ WACHT OP GEBRUIKER: aparte sweep gewenst om alle accent-stripped ankers in de kennisbank te corrigeren? Tip: `grep -rn "antiwitwaswetgeving#-clientenonderzoek\|continuiteits[^ï]\|financiele-info\|continuiteitsveronderstelling" content/` levert kandidaten op. Risico om dit niet te doen: stille broken links die de student bij het klikken niet doorsturen naar de juiste sectie.

[2026-05-02 15:05] [Stagiair] aww-beleid-beheren: stap 4 ("Intern AWW-reglement opstellen") had geen visueel anker en geen `[!info]- Concreet`-blok. Per CLAUDE.md is dit een oordeel/beslissingsstap die zonder visueel anker een Concreet-blok vereist. Stap 3 had wel een prachtig risicomatrix-codeblok; stap 4 hing daardoor abstract.
→ obvious fix: `[!info]- Concreet`-blok toegevoegd met een fragment uit een intern AWW-reglement (kantoor X) — code-block met Hoofdstuk 2 cliëntacceptatie, score-mapping, weiger-criteria. Zo ziet de student concreet hoe een reglement de art. 8-elementen invult.

[2026-05-02 15:05] [Stagiair] aww-beleid-beheren: stap 5 ("Medewerkers opleiden en sensibiliseren") heeft enkel een bulleted lijst van wat de opleiding dekt, geen concrete situatie. Ook hier geen visueel anker. Voor een eenmanspraktijk niet relevant; voor een groter kantoor wel een gat.
→ ⚠️ WACHT OP GEBRUIKER: een tweede `[!info]- Concreet` toevoegen met bv. "agenda van een tweejaarlijkse opleiding" of vermelden dat opleidingsdocumentatie deel uitmaakt van de naleving (bewijslast bij FOD Economie/ITAA-toezicht)? Meer praktijkkennis vereist dan ik autonoom kan invullen.

[2026-05-02 15:05] [QA] aww-beleid-beheren: meerdere stappen verwijzen naar "AWW-reglement ITAA punt 4.1, 4.3, 4.4" (in opdrachtaanvaarding-beoordelen ook). Het reglement zelf is volgens `resources/normen/INDEX.md` lokaal beschikbaar als `aww-reglement-iab.md` en in `content/bronnen/normen/` als `ITAA-norm-aww-reglement.md`. De citaten zijn niet wikilinks naar dat bestand — alleen losse mentions zonder klikbare bronverwijzing.
→ ⚠️ WACHT OP GEBRUIKER: omzetten naar wikilinks `[[bronnen/normen/ITAA-norm-aww-reglement|AWW-reglement ITAA punt 4.1]]`? Vereist verificatie van de exacte structuur (welke "punten" staan er waar). Geldt voor minstens 6 referenties in deze 2 competentiefiches.

[2026-05-02 15:05] [QA] deontologische-beginselen: 5+ inline mentions van "KMO-controlenorm (ITAA, 18 december 2018) — `resources/normen/kmo-controlenorm.md`". CLAUDE.md verbiedt links naar lokale paden ("Geen links naar lokale PDF's"). De norm bestaat als wikilinkable bron: `content/bronnen/normen/ITAA-norm-kmo-controlenorm.md`. De huidige patroon (`resources/...`-pad in italic na de bronnaam) is niet klikbaar en stoort het leespatroon.
→ ⚠️ WACHT OP GEBRUIKER: omzetten naar wikilink `[[bronnen/normen/ITAA-norm-kmo-controlenorm|KMO-controlenorm]]`? Stilistische keuze — als het project de "(KMO-controlenorm — bron-bestand)"-conventie aanhoudt (bv. om het als zichtbare bron in tekst te tonen), is wikilink toch een upgrade omdat hij klikbaar is.

[2026-05-02 15:05] [Examinator] aww-beleid-beheren: 2 voorbeeldvragen, beide weten-niveau, beide 🤖. Geen integratie-vraag die typische examensynthese vereist (bv. "kantoor X ontdekt na 6 maanden dat zijn risicoanalyse achterhaald is omdat een cliënt nu in een hoge-risicoland actief wordt — welke verplichtingen worden gewekt?").
→ ⚠️ WACHT OP GEBRUIKER: integratie-vraag toevoegen die intern beleid + cliëntherbeoordeling + AMLCO-rapportering combineert. Geen direct beschikbaar examensjabloon in `voorbeeldexamens/` voor dit type — vereist 🤖-constructie die pas zinvol is na akkoord op de scope.

[2026-05-02 15:05] [Stagiair] opdrachtaanvaarding-beoordelen: stap 6 ("Opdrachtbrief opstellen") somt de verplichte elementen op als doorlopende prozalist (lijn 195). Dit is dé stap waar een student concreet moet zien hoe zo'n brief eruitziet — zelfs een schematische opsomming met veld-koppen zou helpen.
→ ⚠️ WACHT OP GEBRUIKER: visueel anker toevoegen (codeblok met opdrachtbrief-skelet) of wachten tot `relaties-met-clienten#-opdrachtbrief-verplicht-voor-iedere-opdracht` zelf zo'n schema bevat? Logisch zou het skelet daar in de materie staan; de competentie linkt er enkel naar.

[2026-05-02 15:05] [Coherentie] opdrachtaanvaarding-beoordelen vs antiwitwaswetgeving: stap 5 ("Cliëntenonderzoek (CDD) uitvoeren") bevat een gedetailleerd codeblok met de drie CDD-niveaus (standaard/vereenvoudigd/verscherpt) inclusief checkpoints. Maar antiwitwaswetgeving §Cliëntenonderzoek (lijn 148-174) heeft die niveaudifferentiatie niet — alleen de algemene drie verplichtingen en de wanneer-vraag. CLAUDE.md zegt: "Een stap mag veronderstellen dat de student de gekoppelde materie heeft bestudeerd. De stap hoeft die materie niet te herhalen." Hier herhaalt de competentie materie die niet in de materie-fiche staat. Symptoom: kennis op verkeerde laag.
→ ⚠️ WACHT OP GEBRUIKER: standaard/vereenvoudigd/verscherpt CDD verplaatsen naar antiwitwaswetgeving (eigen `## 📋`-sectie of subsectie van bestaand CDD-blok), en de competentie-stap reduceren tot een ankerlink met 1-2 zinnen. Dit is een granulariteitsbeslissing met cross-fiche impact.

[2026-05-02 15:05] [Stage-mentor] aww-beleid-beheren + opdrachtaanvaarding-beoordelen: beide fiches beschrijven de norm (art. 8 verplichte elementen, drie CDD-niveaus) maar geven geen praktijk-input over hoe kantoren in praktijk hun AML-compliance organiseren — bv. AML-software (Themis, Compligo), wie in praktijk de UBO-check doet, hoe de FOD Economie controleert. Volledig norm-georiënteerd.
→ ⚠️ WACHT OP GEBRUIKER: praktijkblokken toevoegen vereist domeinkennis die ik niet zelfstandig kan verifiëren (welke softwareleveranciers? wat is "vaste" praktijk vs uitschieter?). Dit hoort bij een stage-mentor die het eigenlijk geleefd heeft. Beter geflagd dan zelf gefabriceerd.

[2026-05-02 15:05] [QA] opdrachtaanvaarding-beoordelen: lijn 30 vermeldt voorbehouden opdrachten "art. 3, 6°–8°"; lijn 215 redenering vermeldt "art. 3, 7°" voor omvorming. Ik heb dit niet inhoudelijk geverifieerd tegen Wet ITAA art. 3.
→ ⚠️ WACHT OP GEBRUIKER: bron-check Wet ITAA art. 3 — kloppen items 6°/7°/8° met inbreng/fusie/splitsing/vereffening/omzetting/expertise zoals beschreven? Lijkt plausibel maar niet door mij geverifieerd in dit run.
