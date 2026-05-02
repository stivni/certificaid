# Exploratory bevindingen

Post-build feedback uit `certificaid-exploratory`. Alle rollen door elkaar, chronologisch.

Obvious fixes worden autonoom verwerkt. Bevindingen gemarkeerd met `⚠️ WACHT OP GEBRUIKER` blijven staan tot de gebruiker beslist.

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
