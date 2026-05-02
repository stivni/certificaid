# Exploratory — openstaande beslissingen

Post-build feedback uit `certificaid-exploratory`. Enkel items die nog een beslissing of actie vereisen.

Obvious fixes worden autonoom verwerkt en **hier verwijderd**. Bevindingen gemarkeerd met `⚠️ WACHT OP GEBRUIKER` blijven staan tot de gebruiker beslist.

---

## Architectuur

**[balansaggregaten — parent-sectie]**
⚠️ WACHT OP GEBRUIKER: `## 📌 Balansaggregaten` parent-sectie toevoegen die de drie aggregaten introduceert en de relatie `NBK = WKB + nettokaspositie` centraliseert? Of flat-structuur (drie aparte `##`-secties) behouden? Huidige kapotte externe links zijn al naar `[[balansaggregaten]]` (zonder anker) gezet als tijdelijke oplossing.

---

## Sweeps (autonoom uitvoerbaar — wacht op go)

**[Project-brede emoji-in-URL sweep]**
Competentiefiches met genummerde emoji-stappen hebben kapotte zelf-links: `#2-🔍-type-relatie` ipv `#2--type-relatie`. Betroffen: `consolidatiekring-bepalen`, `consolideren-integraal`, `vermogensmutatiemethode-toepassen` en mogelijk anderen.
→ Kan autonoom worden opgelost met een gerichte grep + replace.


**[Project-brede accent-anker sweep]**
`#-clientenonderzoek` (zonder ë) vs `#-cliëntenonderzoek` (met ë). Grep-commando: `grep -rn "antiwitwaswetgeving#-clientenonderzoek\|financiele-info" content/`. Al deels opgelost in AWW en opdrachtaanvaarding; andere fiches mogelijk nog niet.
→ Kan autonoom worden opgelost.

---

## Bronverificatie (QA — WIB92 artikelnummers)

**[jaarrekening — art. 3:109 bestaat niet]**
⚠️ WACHT OP GEBRUIKER (aanpak): consolidatieplicht staat in Art. 3:23 (verplichting), Art. 3:25 + Art. 1:26 (vrijstelling groep van beperkte omvang). Alle `art. 3:109` verwijzingen in `jaarrekening.md` corrigeren — raakt de hele subsectie.

**[jaarrekening — consolidatiedrempels verouderd]**
⚠️ WACHT OP GEBRUIKER (aanpak): drempels €17.550.000 / €35.100.000 zijn oud. Nieuwe drempels (W 2024-03-28/60): €21.250.000 / €42.500.000 / 250 werknemers. Actualiseren met bronvermelding, of vervangen door "drempels in Art. 1:26"?

**[personenbelasting-basisbegrippen — pensioensparentarieven WIB92 subnummer]**
⚠️ WACHT OP GEBRUIKER: verificeer welk subnummer van WIB92 art. 171 de 10%/16,5%/20%-tarieven op pensioenkapitaal regelt.

**[personenbelasting-basisbegrippen — bewaarplicht art. 315 vs 315bis]**
⚠️ WACHT OP GEBRUIKER: art. 315 regelt bewaarplicht bij handelaars; voor particulieren mogelijk art. 315bis.

**[belastingplichtigen-PB — DBV-voorrang WIB92 art. 5 vs Grondwet]**
⚠️ WACHT OP GEBRUIKER: verdragsvoorrang vloeit eerder voort uit Grondwet art. 167-168 dan uit WIB92 art. 5. Verificeren.

**[gezinsfiscaliteit — wettelijke samenwoning BW artikelnummer]**
⚠️ WACHT OP GEBRUIKER: "BW art. 1475 e.v." is het oud BW; nieuw BW heeft andere nummering. Verificeren.

**[stopzettingsmeerwaarden — cliënteel zelf opgebouwd]**
⚠️ WACHT OP GEBRUIKER: "cliënteel opgebouwd door belastingplichtige zelf" als uitzondering op 33% — expliciete wettelijke basis in WIB92 art. 171 of enkel analytische afleiding?

**[belastingverminderingen-federaal — groepsverzekering mechanisme]**
⚠️ WACHT OP GEBRUIKER: formulering "80% wordt teruggegeven als belastingvermindering" mogelijk onjuist — mechanisme is via VAA bij werknemer + persoonlijke bijdragen art. 145/1, 2°. Herformulering nodig.

**[belastingverminderingen-gewestelijk — Vlaamse woonbonus 45%]**
⚠️ WACHT OP GEBRUIKER: bestaat er een verhoogde 45% woonbonus voor lagere inkomens (in uitdoving maar relevant voor bestaande leningen)?

**[belastingberekening-PB — BBSZ grondslag]**
⚠️ WACHT OP GEBRUIKER: BBSZ wordt geregeld door wet van 30 maart 1994, niet WIB92 art. 168 e.v. Bronverwijzing corrigeren.

**[stopzettings-en-overdrachtsmeerwaarden — definitieve invaliditeit 66%]**
⚠️ WACHT OP GEBRUIKER: is 66%-grens een fiscale WIB92-definitie of verwijst WIB92 naar het sociaal recht?

---

## Inhoud — praktijkblokken (stage-mentor)

**[beroepsgeheim — digitale realiteit]**
⚠️ WACHT OP GEBRUIKER: praktijkblok over cloud-opslag, AI-tools, gedeelde mailboxen en beroepsgeheim. Vereist input over ITAA-norm/circulaire over IT-security.

**[jaarrekening — GA-verificatie zonder commissaris]**
⚠️ WACHT OP GEBRUIKER: praktijkblok over GA-verificatie zonder commissaris-statuut (typische opdrachten, formaat verslag). Vereist beroepspraktijk-input.

**[continuiteit-beoordelen — GA vs GBA scope meldingsplicht]**
⚠️ WACHT OP GEBRUIKER: geldt WER art. XX.23 §3 meldingsplicht ook voor GBA, of enkel GA? Bron-check nodig.

---

## Inhoud — examenvragen (examinator-lacunes)

**[consolidatiekring-bepalen]** — extra vragen nodig per niveau (weten/toepassen/integratie). Voorbeeldexamens scannen op consolidatievragen.

**[boekhoudkundige-beginselen]** — ontbrekende vragen: Voorzichtigheid, Materialiteit, Munteenheid, Continuïteit, en integratievraag waarbij twee beginselen botsen.

**[belastingberekening-PB uitvoeren]** KRITIEK — geen doorlopende integratiecasus. Toe te voegen: echtpaar Vlaanderen, 2 kinderen, berekening tot saldo.

**[belastingplichtigen-PB]** — geen integratievraag over DBV-methodes (vrijstelling vs verrekening).

**[rechtsvorm-fiscaal-beoordelen]** — geen volledig integratieadvies (fiscaal + kwalitatief gecombineerd).

**[diverse-inkomsten-PB]** — geen integratievraag over "normaal beheer" met motivering (crypto-casus).

**[voorheffingen-PB]** — geen integratievraag waarbij mandataris diagnosticeert dat BV onvoldoende is.

**[stopzettingsmeerwaarden-PB]** — regime "vergoedingen na stopzetting" niet als examenvraag uitgewerkt.

---

## Bouwversie-debt (v0 → v2)

Fiches met `bouwversie: 0` die een volledig her-audit verdienen:
- `balansaggregaten.md`
- `financiele-ratios.md`
- `boekhoudkundige-beginselen.md`
- `jaarrekening.md`
- `jaarrekening-herwerken.md`
