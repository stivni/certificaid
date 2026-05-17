# Minicursus-glue-run minicursus-run-20260517T012458Z — Instructies voor Opus-subagent

**Programmaonderdeel**: 1.5
**Run-id**: minicursus-run-20260517T012458Z
**Gegenereerd op**: 2026-05-17T01:24:58+00:00

## Jouw taak

Vul de `<!-- TODO: Opus-glue ... -->` placeholders in de skeleton-Markdown in.
Schrijf de output als één JSON-object naar stdout met de velden beschreven in
`prompts/minicursus-glue-v1.md`.

## Input-bestanden

- **Skeleton**: `content/studiemateriaal/1-5-beginselen-van-de-europese-wetgeving.md`
- **Records-summaries** (27 stuks): zie §Records hieronder
- **Competentie-summaries** (7 stuks): zie §Competenties hieronder

## Anti-fabricatie-regels (verplicht)

- Geen feiten-claims in glue-tekst — alleen rationale, beginselen, transities
- Geen wikilinks bedenken — die staan al in de skeleton
- Verbind aan beginselen die in de records beschreven zijn
- Bij twijfel: korte neutrale tekst, geen uitvinding

## Records-summaries

```json
[
  {
    "id": "afschrijvingen-ifrs",
    "naam": "Afschrijvingen onder IFRS (IAS 16 + IAS 38)",
    "node_type": "methode",
    "definitie_snippet": "Onder IFRS is afschrijving (IAS 16 alinea 6, IAS 38 alinea 8) de **stelselmatige toerekening van het afschrijfbaar bedrag** van een actief **over zijn gebruiksduur**. Het afschrijfbaar bedrag = kostprijs (of geherwaardeerde waarde) − **restwaarde**. De gebruikte methode moet 'een afspiegeling zijn v",
    "rationale_snippet": ""
  },
  {
    "id": "be-gaap-vs-ifrs-overzicht",
    "naam": "Belgisch GAAP versus IFRS — overzicht van hoofdverschillen",
    "node_type": "synthese",
    "definitie_snippet": "",
    "rationale_snippet": ""
  },
  {
    "id": "bijzondere-waardevermindering-ias-36",
    "naam": "Bijzondere waardevermindering (impairment) onder IAS 36",
    "node_type": "methode",
    "definitie_snippet": "IAS 36 — Bijzondere waardevermindering van activa zorgt ervoor dat een entiteit haar activa niet boven hun **realiseerbare waarde** (recoverable amount) waardeert. Op elke balansdatum: beoordeel of er **aanwijzingen** zijn voor waardevermindering. Voor goodwill, immateriële activa met onbepaalde geb",
    "rationale_snippet": ""
  },
  {
    "id": "componentenbenadering-ias-16",
    "naam": "Componentenbenadering (IAS 16) — afschrijving per onderdeel",
    "node_type": "methode",
    "definitie_snippet": "De componentenbenadering (IAS 16 alinea 43-47) verplicht een entiteit om elk **bestanddeel** (component) van een materieel vast actief met een **substantiële kostprijs** in verhouding tot de totale kostprijs van het actief **afzonderlijk af te schrijven** wanneer dat bestanddeel een andere gebruiksd",
    "rationale_snippet": ""
  },
  {
    "id": "correctie-jaarrekening-ifrs",
    "naam": "Correctie van de jaarrekening — IAS 8 versus CBN 2020/12",
    "node_type": "procedure",
    "definitie_snippet": "Correcties van een eerdere jaarrekening — fouten, wijzigingen in grondslagen, schattingswijzigingen — worden onder IFRS geregeld door **IAS 8** (Grondslagen voor financiële verslaggeving, schattingswijzigingen en fouten). Drie scherpe categorieën met verschillende behandeling: (1) **wijziging in gro",
    "rationale_snippet": ""
  },
  {
    "id": "herwaarderingsmodel-ias-16",
    "naam": "Herwaarderingsmodel onder IAS 16",
    "node_type": "methode",
    "definitie_snippet": "Het herwaarderingsmodel (IAS 16 alinea 31) waardeert materiële vaste activa **na eerste opname tegen geherwaardeerde waarde**: de reële waarde op de datum van herwaardering, verminderd met latere geaccumuleerde afschrijvingen en bijzondere waardeverminderingsverliezen. Doel: gebruikers van de jaarre",
    "rationale_snippet": ""
  },
  {
    "id": "ias-1-balans-presentatie",
    "naam": "IFRS-balanspresentatie — vlottend versus niet-vlottend (IAS 1)",
    "node_type": "regel",
    "definitie_snippet": "Het overzicht van de financiële positie (IFRS-balans) moet activa en verplichtingen splitsen in **vlottend** en **niet-vlottend** (alinea 60). Vlottend = de entiteit verwacht het actief te realiseren, te verkopen of te verbruiken binnen de normale bedrijfscyclus OF binnen 12 maanden na de verslagper",
    "rationale_snippet": ""
  },
  {
    "id": "ias-1-jaarrekening-componenten",
    "naam": "Componenten van een IFRS-jaarrekening (IAS 1)",
    "node_type": "begrip",
    "definitie_snippet": "Onder IAS 1 — Presentatie van de jaarrekening bestaat een volledige IFRS-jaarrekening uit **vijf vaste componenten**: (1) een overzicht van de financiële positie aan het eind van de periode (de 'IFRS-balans'); (2) een overzicht van het totaalresultaat over de periode (winst of verlies + overige onde",
    "rationale_snippet": ""
  },
  {
    "id": "ias-1-mutatieoverzicht-eigen-vermogen",
    "naam": "Mutatieoverzicht eigen vermogen (IAS 1)",
    "node_type": "begrip",
    "definitie_snippet": "Het **mutatieoverzicht eigen vermogen** (Statement of Changes in Equity, SOCIE) is de derde verplichte component van een IFRS-jaarrekening (IAS 1 alinea 10c). Het toont de **verzoening tussen begin- en eindsaldo van elke component van het eigen vermogen** over de verslagperiode: geplaatst kapitaal, ",
    "rationale_snippet": ""
  },
  {
    "id": "ias-1-presentatie-beginselen",
    "naam": "Algemene presentatie-beginselen (IAS 1)",
    "node_type": "beginsel",
    "definitie_snippet": "IAS 1 legt zes algemene presentatie-beginselen op die altijd gelden bij het opstellen van een IFRS-jaarrekening: (1) **getrouw beeld + naleving van IFRSs** — een getrouw beeld wordt verkregen door naleving van de toepasselijke standaarden; (2) **continuïteit (going concern)** — de jaarrekening wordt",
    "rationale_snippet": ""
  },
  {
    "id": "ias-1-toelichtingsvereisten",
    "naam": "Toelichtingsvereisten onder IAS 1 — structuur en inhoud",
    "node_type": "regel",
    "definitie_snippet": "De toelichting bij de IFRS-jaarrekening (IAS 1 alinea 112-138) is geen optioneel addendum maar een **integraal deel** van de jaarrekening. Verplichte inhoud (alinea 112): (a) **verklaring van overeenstemming** met IFRS-en; (b) **samenvatting van significante grondslagen voor financiële verslaggeving",
    "rationale_snippet": ""
  },
  {
    "id": "ias-1-winst-en-totaalresultaat",
    "naam": "Winst of verlies en overige onderdelen van het totaalresultaat (IAS 1)",
    "node_type": "begrip",
    "definitie_snippet": "Onder IAS 1 omvat het **totaalresultaat** twee onderdelen: (1) **winst of verlies** (profit or loss) — de klassieke W&V-componenten zoals opbrengsten, kostprijs van omzet, financieringskosten, belastingen; en (2) **overige onderdelen van het totaalresultaat** (Other Comprehensive Income, OCI) — bate",
    "rationale_snippet": ""
  },
  {
    "id": "ifrs-16-lessee-vs-lessor-overzicht",
    "naam": "IFRS 16 — lessee versus lessor: overzicht en asymmetrie",
    "node_type": "synthese",
    "definitie_snippet": "",
    "rationale_snippet": ""
  },
  {
    "id": "ifrs-eerste-toepassing",
    "naam": "Eerste toepassing van IFRS (IFRS 1)",
    "node_type": "procedure",
    "definitie_snippet": "IFRS 1 — Eerste toepassing van International Financial Reporting Standards (IFRSs) bepaalt hoe een entiteit die voor het eerst een jaarrekening volledig conform IFRS uitbrengt, de overgang van haar oude grondslagen (typisch Belgisch GAAP / KB WVV) naar IFRS uitvoert. Het doel is dat de eerste IFRS-j",
    "rationale_snippet": ""
  },
  {
    "id": "ifrs-toepassingsgebied-belgie",
    "naam": "IFRS-toepassingsgebied in België — wie moet en wie mag?",
    "node_type": "regel",
    "definitie_snippet": "In België is IFRS-toepassing zeer beperkt. **Verplicht** is IFRS alleen voor de geconsolideerde jaarrekening van (1) op een gereglementeerde markt genoteerde Belgische ondernemingen, en (2) Belgische kredietinstellingen en verzekeringsondernemingen (op grond van sectorale toezichtsregels). **Toegest",
    "rationale_snippet": ""
  },
  {
    "id": "ifrs-verordening-1606-2002",
    "naam": "IFRS-verordening 1606/2002 — verplichte toepassing IFRS",
    "node_type": "regel",
    "definitie_snippet": "Verordening (EG) nr. 1606/2002 van het Europees Parlement en de Raad van 19 juli 2002 verplicht **beursgenoteerde EU-ondernemingen** om hun geconsolideerde jaarrekening op te stellen volgens de internationale standaarden (International Accounting Standards / International Financial Reporting Standar",
    "rationale_snippet": ""
  },
  {
    "id": "immateriele-vaste-activa-ifrs",
    "naam": "Immateriële activa onder IFRS (IAS 38)",
    "node_type": "regel",
    "definitie_snippet": "IAS 38 — Immateriële activa regelt de boekhoudkundige verwerking van **identificeerbare, niet-monetaire activa zonder fysieke vorm** (alinea 8). Drie cumulatieve definitie-eisen: (1) identificeerbaar — afscheidbaar OF voortkomend uit contractuele/juridische rechten; (2) entiteit heeft de zeggenschap",
    "rationale_snippet": ""
  },
  {
    "id": "leaseverplichting-ifrs",
    "naam": "Leaseverplichting onder IFRS 16",
    "node_type": "begrip",
    "definitie_snippet": "De **leaseverplichting** is de financiële verplichting die de lessee op de aanvangsdatum onder IFRS 16 op zijn balans opneemt: de **contante waarde van leasebetalingen die op aanvangsdatum nog niet zijn verricht** (alinea 26). Disconteringsvoet: **impliciete rentevoet van de leaseovereenkomst** indi",
    "rationale_snippet": ""
  },
  {
    "id": "leasing-ifrs",
    "naam": "Leasing onder IFRS (IFRS 16) — lessee-perspectief",
    "node_type": "regel",
    "definitie_snippet": "IFRS 16 — Leaseovereenkomsten vervangt sinds 1 januari 2019 de oude IAS 17 en hanteert voor de **lessee** een **single model**: ALLE leases (boven de vrijstellingsdrempels) worden on-balance gezet. Op de aanvangsdatum neemt de lessee twee posten op: (1) een **met een gebruiksrecht overeenstemmend ac",
    "rationale_snippet": ""
  },
  {
    "id": "materiele-vaste-activa-ifrs",
    "naam": "Materiële vaste activa onder IFRS (IAS 16)",
    "node_type": "regel",
    "definitie_snippet": "IAS 16 — Materiële vaste activa regelt de boekhoudkundige verwerking van **materiële vaste activa**: tastbare bezittingen aangehouden voor gebruik in productie/levering van goederen of diensten, verhuur of bestuurlijke doeleinden, met verwacht gebruik over **meer dan één periode**. Opnamecriteria (a",
    "rationale_snippet": ""
  },
  {
    "id": "onderhanden-projecten-ifrs",
    "naam": "Onderhanden projecten in opdracht van derden — onder IFRS 15",
    "node_type": "regel",
    "definitie_snippet": "Sinds de inwerkingtreding van IFRS 15 op 1 januari 2018 is IAS 11 — Construction Contracts ingetrokken. **Onderhanden projecten in opdracht van derden** (bouwprojecten, infrastructuurprojecten, specifiek-gemaakte goederen of diensten) vallen nu onder de algemene regel van IFRS 15. De kernvraag wordt",
    "rationale_snippet": ""
  },
  {
    "id": "opbrengsten-ifrs",
    "naam": "Opbrengsten onder IFRS (IFRS 15) — 5-stappen-model",
    "node_type": "methode",
    "definitie_snippet": "IFRS 15 — Opbrengsten van contracten met klanten vervangt sinds 1 januari 2018 IAS 18 (Opbrengsten uit gewone activiteiten) en IAS 11 (Onderhanden projecten in opdracht van derden). Het **kernprincipe** (alinea 2): een entiteit neemt opbrengsten op om de overdracht van beloofde goederen of diensten ",
    "rationale_snippet": ""
  },
  {
    "id": "prestatieverplichting-ifrs-15",
    "naam": "Prestatieverplichting (performance obligation) onder IFRS 15",
    "node_type": "begrip",
    "definitie_snippet": "Een **prestatieverplichting** (performance obligation, PO) is een belofte in een contract met een klant om aan die klant over te dragen: (a) een **onderscheiden** goed of dienst (of bundel van onderscheiden goederen of diensten); OF (b) een reeks van onderscheiden goederen of diensten die grotendeel",
    "rationale_snippet": ""
  },
  {
    "id": "richtlijn-2013-34-eu",
    "naam": "Richtlijn 2013/34/EU — Europese jaarrekeningenrichtlijn",
    "node_type": "regel",
    "definitie_snippet": "Richtlijn 2013/34/EU van het Europees Parlement en de Raad van 26 juni 2013 is het **Europese basiskader** voor de jaarlijkse financiële overzichten, geconsolideerde overzichten en aanverwante verslagen van bepaalde ondernemingsvormen. Zij vervangt de oude Vierde Richtlijn (78/660/EEG) en Zevende Ri",
    "rationale_snippet": ""
  },
  {
    "id": "right-of-use-actief",
    "naam": "Right-of-use-actief (gebruiksrecht-actief) onder IFRS 16",
    "node_type": "begrip",
    "definitie_snippet": "Het **met een gebruiksrecht overeenstemmende actief** (right-of-use asset, ROU) is het actief dat een lessee onder IFRS 16 op zijn balans opneemt: het **recht om gedurende de leaseperiode het onderliggende activum te gebruiken**. Niet de eigendom van het actief zelf, wel het exclusieve gebruiksrecht",
    "rationale_snippet": ""
  },
  {
    "id": "voorraden-ifrs",
    "naam": "Voorraden onder IFRS (IAS 2)",
    "node_type": "regel",
    "definitie_snippet": "IAS 2 — Voorraden regelt de boekhoudkundige verwerking van voorraden onder IFRS. **Voorraden** (alinea 6) zijn activa: (a) aangehouden voor verkoop in het kader van de normale bedrijfsvoering; (b) in het productieproces voor dergelijke verkoop; OF (c) grond-/hulpstoffen die tijdens het productieproc",
    "rationale_snippet": ""
  },
  {
    "id": "wijziging-boekhoudkundig-referentiestelsel",
    "naam": "Wijziging van boekhoudkundig referentiestelsel (CBN 2022/08)",
    "node_type": "procedure",
    "definitie_snippet": "CBN-advies 2022/08 regelt de **wijziging van het boekhoudkundig referentiestelsel** voor Belgische ondernemingen die overstappen tussen Belgisch GAAP en IFRS — of omgekeerd. Twee veelvoorkomende scenario's: (a) **van Belgisch GAAP naar IFRS** — typisch bij nieuwe beursnotering of vrijwillige keuze v",
    "rationale_snippet": ""
  }
]
```

## Competentie-summaries

```json
[
  {
    "id": "bepalen-toepasselijkheid-ifrs-belgie",
    "titel": "Bepalen of een onderneming IFRS moet of mag toepassen in België",
    "procedure_grondslag": {
      "wettelijk_pct": 90,
      "praktijk_pct": 10,
      "motivering": "De verplichte gevallen volgen rechtstreeks uit Verordening (EG) 1606/2002 art. 4 (beursgenoteerde geconsolideerde rekeningen) en sectorale regels (kredietinstellingen, verzekeraars). Vrijwillige IFRS-toepassing op statutair niveau is in België in beginsel niet toegestaan — alleen via uitzondering. Het praktijk-aandeel zit in het inschatten van de strategische gevolgen (toelichting, externe rapportering, vergelijkbaarheid)."
    },
    "gebaseerd_op_concepten": [
      "ifrs-verordening-1606-2002",
      "ifrs-toepassingsgebied-belgie",
      "richtlijn-2013-34-eu",
      "be-gaap-vs-ifrs-overzicht"
    ],
    "eerste_stap": "Identificeer het rapporteringsniveau"
  },
  {
    "id": "presenteren-ifrs-jaarrekening-volgens-ias-1",
    "titel": "Presenteren van een IFRS-jaarrekening volgens IAS 1 (5 componenten en presentatiebeginselen)",
    "procedure_grondslag": {
      "wettelijk_pct": 85,
      "praktijk_pct": 15,
      "motivering": "De 5 verplichte componenten, de presentatiebeginselen (going concern, accruals, materialiteit, consistentie, geen compensatie) en de minimale toelichtingsvereisten staan in IAS 1 (alinea's 9-138). Het praktijk-aandeel zit in het uitwerken van de minimum-categorieën in balans- en resultatenrekening tot een leesbare presentatie en in de samenstelling van de grondslagen-toelichting."
    },
    "gebaseerd_op_concepten": [
      "ias-1-jaarrekening-componenten",
      "ias-1-presentatie-beginselen",
      "ias-1-balans-presentatie",
      "ias-1-winst-en-totaalresultaat",
      "ias-1-mutatieoverzicht-eigen-vermogen",
      "ias-1-toelichtingsvereisten"
    ],
    "eerste_stap": "Stel de 5 verplichte componenten samen"
  },
  {
    "id": "toepassen-vijf-stappen-model-opbrengsten-ifrs",
    "titel": "Toepassen van het 5-stappen-model van IFRS 15 voor opbrengstenherkenning",
    "procedure_grondslag": {
      "wettelijk_pct": 80,
      "praktijk_pct": 20,
      "motivering": "Het 5-stappen-model en de criteria voor onderscheiden prestatieverplichtingen + tijdsbepaling (op tijdstip versus over periode) zijn volledig in IFRS 15 (alinea's 9-129) geregeld. Het praktijk-aandeel zit in het beoordelen van het 'onderscheiden'-criterium en in het kiezen van een geschikte voortgangsmeting (input- of outputmethode) bij over-periode-opname."
    },
    "gebaseerd_op_concepten": [
      "opbrengsten-ifrs",
      "prestatieverplichting-ifrs-15",
      "onderhanden-projecten-ifrs",
      "be-gaap-vs-ifrs-overzicht"
    ],
    "eerste_stap": "Identificeer het contract met de klant"
  },
  {
    "id": "toetsen-bijzondere-waardevermindering-ias-36",
    "titel": "Toetsen van een actief op bijzondere waardevermindering onder IAS 36",
    "procedure_grondslag": {
      "wettelijk_pct": 80,
      "praktijk_pct": 20,
      "motivering": "De impairment-procedure (aanwijzingen scannen, realiseerbare waarde berekenen als hoogste van reële waarde min verkoopkosten EN bedrijfswaarde, verschil boeken) is volledig in IAS 36 (alinea 8-99) geregeld. Het praktijk-aandeel zit in de schatting van toekomstige kasstromen, in de keuze van een passende disconteringsvoet (WACC) en in het identificeren van kasstroomgenererende eenheden (CGU's) wanneer een actief geen onafhankelijke kasstromen genereert."
    },
    "gebaseerd_op_concepten": [
      "bijzondere-waardevermindering-ias-36",
      "materiele-vaste-activa-ifrs",
      "immateriele-vaste-activa-ifrs",
      "afschrijvingen-ifrs"
    ],
    "eerste_stap": "Scan op aanwijzingen voor mogelijke waardevermindering"
  },
  {
    "id": "uitvoeren-eerste-toepassing-ifrs",
    "titel": "Uitvoeren van de eerste toepassing van IFRS overeenkomstig IFRS 1",
    "procedure_grondslag": {
      "wettelijk_pct": 70,
      "praktijk_pct": 30,
      "motivering": "De stappen volgen IFRS 1 alinea's 6-25 (openingsbalans, vier acties, verplichte uitzonderingen, optionele vrijstellingen, aansluiting in toelichting). Het praktijk-aandeel zit in het beoordelen van welke vrijstellingen (D1-D8) economisch en organisatorisch zinvol zijn, en in het opzetten van parallel-rapportering tijdens de vergelijkende periode."
    },
    "gebaseerd_op_concepten": [
      "ifrs-eerste-toepassing",
      "wijziging-boekhoudkundig-referentiestelsel",
      "ias-1-jaarrekening-componenten",
      "be-gaap-vs-ifrs-overzicht"
    ],
    "eerste_stap": "Stel de datum van overgang naar IFRS vast"
  },
  {
    "id": "verwerken-leasing-ifrs-lessee",
    "titel": "Verwerken van een leaseovereenkomst onder IFRS 16 als lessee (right-of-use + lease-verplichting)",
    "procedure_grondslag": {
      "wettelijk_pct": 80,
      "praktijk_pct": 20,
      "motivering": "De single-model-benadering, eerste waardering en afschrijvings-/rente-splitsing zijn volledig in IFRS 16 alinea's 22-45 geregeld. Het praktijk-aandeel zit in de keuze of de vrijstellingen (kortlopend, lage waarde) worden toegepast en in het bepalen van de marginale rentevoet wanneer de impliciete rentevoet niet bekend is."
    },
    "gebaseerd_op_concepten": [
      "leasing-ifrs",
      "right-of-use-actief",
      "leaseverplichting-ifrs",
      "ifrs-16-lessee-vs-lessor-overzicht",
      "leasing"
    ],
    "eerste_stap": "Identificeer of het contract een lease bevat"
  },
  {
    "id": "waarderen-materiele-vaste-activa-ifrs",
    "titel": "Waarderen van materiële vaste activa onder IAS 16 (kostprijs- of herwaarderingsmodel)",
    "procedure_grondslag": {
      "wettelijk_pct": 75,
      "praktijk_pct": 25,
      "motivering": "De keuze tussen kostprijs- en herwaarderingsmodel + de componentenbenadering + afschrijvingsregels zijn rechtstreeks in IAS 16 (alinea's 15-66) geregeld. Het praktijk-aandeel zit in het inschatten van de gebruiksduur per component, de restwaarde, en de frequentie van herwaardering (bij voldoende regelmaat zodat boekwaarde nooit substantieel afwijkt van reële waarde)."
    },
    "gebaseerd_op_concepten": [
      "materiele-vaste-activa-ifrs",
      "herwaarderingsmodel-ias-16",
      "componentenbenadering-ias-16",
      "afschrijvingen-ifrs",
      "bijzondere-waardevermindering-ias-36"
    ],
    "eerste_stap": "Bepaal de eerste waardering (kostprijs)"
  }
]
```

---

## Prompt-referentie (minicursus-glue-v1.md)

# Prompt: Minicursus-glue — Render-fase (v2)

**Doel**: Vul de `<!-- TODO: Opus-glue ... -->` placeholders in de minicursus-skeleton in.

**Model**: claude-opus-4-7 (Opus-subagent)

**Monotoon contract**: Geen feiten-claims, geen wikilinks bedenken, geen wettekst-citaties. **Compact**. Glue is verbindweefsel, geen leerstof.

---

## Jouw rol

Je schrijft minimale, verbindende, pedagogische tekst tussen de deterministisch gerenderde blokken. Je vult GEEN nieuwe feiten in. Je verbindt zonder uit te leggen wat al elders staat.

## Compactheidscontract

Mikt op compacte, dichte tekst zonder kaal te worden. Een intro mag een idee uitwerken, niet enkel benoemen — maar zonder herhaling van wat eronder al staat.

- **Sectie-intro's (oriëntatie / thematisch / competentie)**: typisch 2-3 zinnen. Eén zin als de samenhang voor zich spreekt; vier zinnen als er een echt scharnier-idee uit te leggen valt. Nooit meer dan vier.
- **Leesgids**: 3-4 zinnen — hoe lees je de minicursus, welke logica zit erin.
- **Waarom-po**: 4-6 zinnen — één tot twee beginselen + toepassings-implicaties. Mag ademen, geen wall-of-text.
- **Synthese-stappenplan**: 6-9 zinnen — werkschema-stijl, end-to-end-overzicht.
- **Examenfocus**: 4-6 zinnen — twee tot drie denkpatronen, met voldoende grond om bruikbaar te zijn.
- **Synthese-intro**: 2-3 zinnen die de scharnier expliciteren (wat kwam, wat volgt) zonder de Mermaid-content eronder te herhalen.
- **Bij twijfel**: liever kort en dicht dan opgeklopt — maar niet zo kaal dat de student de pedagogische verbinding moet zelf invullen.

## Anti-fabricatie-regels (hard)

1. **Geen feiten-claims**, geen wetsartikelnummers, geen specifieke percentages of bedragen die je niet in records-summaries ziet.
2. **Geen nieuwe wikilinks verzinnen.** De skeleton bevat ze al.
3. **Geen herhaling van de synthese-record-inhoud.** De Mermaid + kerninzichten staan eronder. Glue-intro voegt scharnier toe, geen overlap.
4. **Rationale = beginselen-inzicht, niet examen-truc.** "Waarom werkt dit zo" — niet "dit wordt vaak gevraagd".
5. **Bij gebrek aan grondslag: kort en neutraal.** Eerder "Dit hoofdstuk behandelt X." dan vrije uitvinding.
6. **Geen oude examen-vragen of percentages opnoemen.** Examenfocus is meta-niveau (welk denkpatroon), niet vraagspoilers.

## Workflow

Open `content/studiemateriaal/<X.Y>-<slug>/minicursus.md` met de Edit-tool. Vervang elke `<!-- TODO: Opus-glue X -->` regel door de bedoelde tekst, in volgorde. Geen JSON-output — direct editen.

## Stijl

- **Toon**: helder, direct, actief — zoals een ervaren collega
- **"Je"-aanspraak**, niet "men" of "de student"
- **Geen bullets in glue-tekst** (bullets staan al in skeleton)
- **Nederlands**
- **Geen euro-bedragen of cast-namen** in glue (die staan in records); generieke termen
- **Geen "hieronder zie je..." of "in de volgende sectie..."** — laat de structuur zelf spreken

## Verificatie

Na invullen:
1. `grep -c "<!-- TODO: Opus-glue" content/studiemateriaal/<X.Y>-*/minicursus.md` moet 0 teruggeven
2. Totale word-count zit doorgaans tussen 700 en 1100 woorden glue-tekst voor heel het document — minder dan de "uitgebreid"-stijl (1500+) maar voldoende ruimte voor pedagogische verbinding.
3. Geen overlap tussen synthese-intro en de synthese-record-inhoud die eronder rendert

Geen commit. De hoofdsessie commit.

