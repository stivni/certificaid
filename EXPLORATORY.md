# Exploratory — openstaande beslissingen

Post-build feedback uit `certificaid-exploratory`. Enkel items die nog een beslissing of actie vereisen.

Obvious fixes worden autonoom verwerkt en **hier verwijderd**. Bevindingen gemarkeerd met `⚠️ WACHT OP GEBRUIKER` blijven staan tot de gebruiker beslist.

---

## Architectuur

**[balansaggregaten — parent-sectie]**
⚠️ WACHT OP GEBRUIKER: `## 📌 Balansaggregaten` parent-sectie toevoegen die de drie aggregaten introduceert en de relatie `NBK = WKB + nettokaspositie` centraliseert? Of flat-structuur (drie aparte `##`-secties) behouden? Huidige kapotte externe links zijn al naar `[[balansaggregaten]]` (zonder anker) gezet als tijdelijke oplossing.

---

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

## [2026-05-03 10:28] Exploratieve ronde — fiscale-beginselen, fiscale-actoren, fiscale-norm-toetsen-aan-beginselen

**Obvious fixes verwerkt** (autonoom):

- [Bibliothecaris/Coherentie] **fiscale-actoren.md** r. 157: `Wet ITAA art. 3` (GBA) → `[[bronnen/wetteksten/XXI-wet-itaa#art-6|Wet ITAA art. 6]]` + activiteit-omschrijving aangevuld. *Coherentie-reviewer cross-checked met `beroep-van-accountant-en-belastingadviseur.md`: GBA-activiteiten staan in art. 6, niet art. 3.*
- [QA] **fiscale-actoren.md** r. 87: `bestendige deputatie` → `deputatie` (verouderde term sinds Provinciedecreet).
- [QA + Bibliothecaris] **fiscale-actoren.md** r. 284: bezwaartermijn "3 maanden... (of 6 maanden)" verwijderd uit voorbeeldvraag-antwoord; nu enkel verwijzing naar PO 2.5 met `⚠️ te verifiëren`. *Reden: WIB92 art. 371 stelt 6 maanden voor alle inkomstenbelastingen; "3 maanden" was feitelijk fout.*
- [Bibliothecaris] **fiscale-actoren.md** r. 78: `VCF` → wikilink naar `[[bronnen/wetteksten/IVA-vcf|VCF]]`.
- [Coherentie + Bibliothecaris] **fiscale-beginselen.md** r. 67: ruling-link `#-fod-financiën` → `#dienst-voorafgaande-beslissingen-dvb` (preciezer anker).
- [Bibliothecaris] **fiscale-beginselen.md** r. 225: EVRM en EU-Handvest gelinkt naar `bronnen-fiscaal-recht`-secties; Engel-criteria inline uitgelegd (3 criteria).
- [Bibliothecaris] **fiscale-norm-toetsen-aan-beginselen.md** r. 39: `[[bronnen-fiscaal-recht|zie hiërarchie]]` → `[[bronnen-fiscaal-recht#-normenhiërarchie|zie hiërarchie]]`.
- [Bibliothecaris + Coherentie] **fiscale-norm-toetsen-aan-beginselen.md** r. 174: "territorialiteit" → "territorialiteitsbeginsel" + EU-recht link toegevoegd.
- [Bibliothecaris] **fiscale-norm-toetsen-aan-beginselen.md** r. 197: Engel-criteria gelinkt naar fiscale-beginselen.
- [Stage-mentor] **fiscale-actoren.md**: `[!info]- In de praktijk: hoe een ruling-aanvraag verloopt` toegevoegd in DVB-sectie + `⚠️ te verifiëren` op "typisch 5 jaar" (Wet 24/12/2002 niet lokaal beschikbaar).
- [Stage-mentor] **fiscale-actoren.md**: `[!info]- In de praktijk: welke administratie botst mijn cliënt mee?` toegevoegd in §FOD Financiën (AAF/AAII/BBI/AAPD differentieel).
- [Examinator] **fiscale-norm-toetsen-aan-beginselen.md**: 2 nieuwe voorbeeldvragen toegevoegd door agent ("Eigenlijke vs. oneigenlijke retroactiviteit" weten + "Bewijslast bij fiscaal misbruik" toepassen).

---

**Bevindingen die wachten op gebruiker** (⚠️ WACHT OP GEBRUIKER):

[2026-05-03 10:28] [Coherentie] **fiscale-beginselen.md + fiscale-norm-toetsen-aan-beginselen.md**: art. 4 Zevende Protocol EVRM als grondslag voor non bis in idem.
→ ⚠️ WACHT OP GEBRUIKER: PO-fiche flagde al de twijfel over België's ratificatie van het 7e Protocol. Indien niet geratificeerd: grondslag in beide fiches corrigeren naar uitsluitend art. 50 EU-Handvest + interne una via (Wet 20 september 2012). Verifiëren via Belgisch Staatsblad / online.

[2026-05-03 10:28] [QA] **fiscale-beginselen.md** r. 119 (frontmatter) + r. 10: "Smeerkaas-arrest 1971" als bron voor realiteitsbeginsel.
→ ⚠️ WACHT OP GEBRUIKER: Smeerkaas (1971) gaat over voorrang van DBV op interne fiscale wet — niet over realiteitsbeginsel. Het realiteitsbeginsel rust op Brepols (1961). Smeerkaas hoort thematisch bij territorialiteit/internationaal kader. Verwijderen uit frontmatter-bronnen of verplaatsen?

[2026-05-03 10:28] [QA] **fiscale-beginselen.md** r. 279: "Europese ATAD-richtlijn (sinds 2019)".
→ ⚠️ WACHT OP GEBRUIKER: ATAD = richtlijn 2016/1164, in BE geïmplementeerd via Wet 25/12/2017 (datum 2019 onjuist); ATAD geldt voor Ven.B (GAAR), niet alle belastingen. Tekst nuanceren of weglaten.

[2026-05-03 10:28] [QA] **fiscale-beginselen.md**: art. 2 Oud BW als grondslag niet-retroactiviteit.
→ ⚠️ WACHT OP GEBRUIKER: Oud BW grotendeels opgeheven 01/01/2023. Primaire grondslag voor niet-retroactiviteit is nu het constitutioneel beginsel + GwH-rechtspraak; art. 2 NieuW BW als secundair. Tekst verduidelijken.

[2026-05-03 10:28] [QA] **fiscale-beginselen.md** r. 237: una via-wet "Wet 20 september 2012".
→ ⚠️ WACHT OP GEBRUIKER: Datum onverifieerbaar in lokale bronnen. De fiscale una via-regeling kreeg vorm via wijzigingen in WIB92 (art. 449bis e.v.) en het Sociaal Strafwetboek; de "Wet van 20 september 2012" verwijst in andere contexten naar mensenhandel. Wetsreferentie verifiëren of als ⚠️ markeren.

[2026-05-03 10:28] [Stagiair + Bibliothecaris] **fiscale-beginselen.md** r. 318: praktijk-callout vermeldt "in vak XVII (diverse inkomsten)".
→ ⚠️ WACHT OP GEBRUIKER: vak XVII in de PB-aangifte = "Winst uit nijverheids-, handels- of landbouwondernemingen", NIET diverse inkomsten. Diverse inkomsten zitten in een ander vak (verifiëren via aangifte-toelichting). Bovendien: "vak XVII" is ook ITAA-LEX sectie (Antiwitwaswet) — disambigueren in tekst.

[2026-05-03 10:28] [Stagiair] **fiscale-actoren.md** r. 64 (DVB-sectie): "typisch 5 jaar" en bindingsscope onduidelijk.
→ ⚠️ WACHT OP GEBRUIKER: bindt de ruling alleen de aanvrager of ook vergelijkbare gevallen? geldt 5 jaar als wettelijke standaard? Wettekst (Wet 24/12/2002, ITAA-LEX I) lokaal niet beschikbaar — markeer als `⚠️ te verifiëren` toegevoegd, maar de inhoudelijke verheldering wacht op de wettekst.

[2026-05-03 10:28] [QA] **fiscale-actoren.md** valkuil r. 162: "art. 728 Ger.W." voor familielid-bijstand in eerste aanleg.
→ ⚠️ WACHT OP GEBRUIKER: Ger.W. art. 728 lokaal niet beschikbaar; de "familielid"-uitzondering geldt mogelijk niet voor fiscale kamer. Verifiëren of conditional-formuleren.

[2026-05-03 10:28] [Stage-mentor] **fiscale-actoren.md**: Vlabel heeft eigen ruling-procedure (Voorafgaande beslissing) naast federale DVB voor VCF-materies.
→ ⚠️ WACHT OP GEBRUIKER: Vermelden in DVB-sectie of regionale-fisci-sectie? Belangrijk voor stagiairs: VCF-materies → Vlabel ruling, niet federale DVB.

[2026-05-03 10:28] [Examinator] **fiscale-actoren.md**: integratievraag voorgesteld (cliënt krijgt aanslag AAF + BBI-onderzoek tegelijk — 3-delige adviesvraag).
→ ⚠️ WACHT OP GEBRUIKER: Goed uitgewerkte vraag (zie agent-output) — doorvoeren? Vereist beslissing over scope: bevat termijn-claims die naar PO 2.5 verwijzen.

[2026-05-03 10:28] [Stagiair] **fiscale-norm-toetsen-aan-beginselen.md**: stappen 6 (territorialiteit) en 9 (conclusie opstellen) missen `[!info]- Concreet`-blok.
→ ⚠️ WACHT OP GEBRUIKER: stap 6 verdient een buitenlands-werknemer-voorbeeld; stap 9 verdient een mini-bezwaarschrift-skelet (5 zinnen). Inhoudelijke uitwerking nodig.

[2026-05-03 10:28] [QA] **fiscale-norm-toetsen-aan-beginselen.md** stap 7: una via-formulering "geen overleg geweest of geschonden".
→ ⚠️ WACHT OP GEBRUIKER: Suggereert dat ontbreken van una via-overleg op zich een schending van non bis in idem is — dit is misleidend. Una via is een instrument om dubbele bestraffing te voorkomen; het ontbreken ervan is geen zelfstandige schending. Herformuleren.

[2026-05-03 10:28] [Coherentie] **fiscale-norm-toetsen-aan-beginselen.md** stap 5b: "objectief criterium" zonder "redelijk verantwoord".
→ ⚠️ WACHT OP GEBRUIKER: Materie-fiche (Cassatie-toets) vermeldt "berust op een objectief criterium, redelijk verantwoord" als één gecombineerd criterium. Competentie-fiche heeft alleen "objectief criterium". Aanvullen of presentatieverschil aanvaarden?

[2026-05-03 10:28] [Stage-mentor] **fiscale-norm-toetsen-aan-beginselen.md** stap 8: misbruiktoets is in de praktijk vaak preventief (DVB-route) i.p.v. retroactief.
→ ⚠️ WACHT OP GEBRUIKER: Stap 8 als plannings-variant uitbreiden ("nog te realiseren verrichting → DVB-route") of scope competentie houden bij retroactieve betwisting? Raakt aan de definitie van de competentie.

---

## Bouwversie-debt (v0 → v2)

Fiches met `bouwversie: 0` die een volledig her-audit verdienen:
- `balansaggregaten.md`
- `financiele-ratios.md`
- `boekhoudkundige-beginselen.md`
- `jaarrekening.md`
- `jaarrekening-herwerken.md`
