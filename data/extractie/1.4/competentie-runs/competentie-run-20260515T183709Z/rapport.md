# Competentie-destillatie-run competentie-run-20260515T183709Z — rapport

**Programmaonderdeel**: 1.4 Geconsolideerde jaarrekening
**Model**: claude-opus-4-7
**Uitgevoerd op**: 2026-05-15T18:37:09Z

## Samenvatting

```
Competenties voorgesteld : 9
Bestanden geschreven     : 9
Stappen totaal           : 52
Praktijk-pct > 50%       : 0 (geen mens-review vereist op die grond)
```

| Competentie | Wettelijk % | Stappen | Concepten |
|---|---|---|---|
| `bepalen-consolidatieverplichting` | 90 | 6 | 7 |
| `afbakenen-consolidatiekring` | 80 | 5 | 6 |
| `kwalificeren-relatie-deelneming` | 75 | 5 | 7 |
| `kiezen-consolidatiemethode` | 80 | 5 | 8 |
| `berekenen-controle-en-belangenpercentage` | 60 | 5 | 4 |
| `uitvoeren-eerste-consolidatie` | 75 | 6 | 5 |
| `uitvoeren-intragroep-eliminaties` | 80 | 8 | 5 |
| `verwerken-wijziging-consolidatiekring` | 75 | 6 | 6 |
| `toepassen-uniforme-waarderingsregels` | 85 | 6 | 3 |

## Voorgestelde competenties

### 1. `bepalen-consolidatieverplichting`
Bepalen of een vennootschap een geconsolideerde jaarrekening moet opstellen — toetst rechtspersoonlijkheid, controle, consortium, groottecriteria en vrijstelling van subconsolidatie.

### 2. `afbakenen-consolidatiekring`
Afbakenen welke entiteiten in de kring zitten en beoordelen van de vier wettelijke weglatingsgronden + behandeling van weggelaten dochters via vermogensmutatie.

### 3. `kwalificeren-relatie-deelneming`
Kwalificeren van elke deelneming als dochter (exclusieve controle), gemeenschappelijke dochter (gezamenlijke controle), geassocieerde onderneming (invloed van betekenis) of gewone deelneming.

### 4. `kiezen-consolidatiemethode`
Mappen van de kwalificatie op de verplichte techniek: integraal / evenredig / vermogensmutatie / horizontaal. Bevat ook de regel dat KB WVV-uitgesloten dochters via vermogensmutatie alsnog worden opgenomen.

### 5. `berekenen-controle-en-belangenpercentage`
Rekenkundige vaardigheid in ketenstructuren — onderscheid tussen controlepercentage (niet vermenigvuldigen) en belangenpercentage (wél vermenigvuldigen). Onderbouwt het aandeel-van-derden en pro-rata opname.

### 6. `uitvoeren-eerste-consolidatie`
Procedure bij opname van een nieuw verworven dochter of geassocieerde: aanschaffingswaarde versus pro-rata EV, toerekening verschil aan onder-/overgewaardeerde activa/passiva, residueel consolidatieverschil, afschrijvingsplan.

### 7. `uitvoeren-intragroep-eliminaties`
Operationele procedure: vorderingen/schulden, intra-groepswinst in voorraad, opbrengsten/kosten, pro-rata aanpassing voor evenredig geconsolideerde dochters, materialiteitstoets en berekening aandeel van derden.

### 8. `verwerken-wijziging-consolidatiekring`
Behandeling van kantelpunten tussen technieken (step acquisition), gehele/gedeeltelijke realisatie en transacties onder gemeenschappelijke leiding.

### 9. `toepassen-uniforme-waarderingsregels`
Hercorrectie van afwijkende waarderingsregels en fiscale distorsies (KB WVV art. 3:116-3:118), met aandacht voor stelselmatigheid in de tijd.

## Afwegingen en design-keuzes

### Splitsing kwalificeren ↔ kiezen-methode
Ik heb bewust twee aparte competenties gemaakt: `kwalificeren-relatie-deelneming` (controle-toets) en `kiezen-consolidatiemethode` (mapping naar techniek). Reden: de twee vaardigheden worden zowel inhoudelijk als in examenvragen apart getoetst. Kwalificatie is een feitelijke toets (juridische verhoudingen, drempels); methode-keuze is een rechtsgevolg dat ook context-elementen meeneemt (nauwe integratie, consortium, KB WVV-uitsluitingen). Combineren zou een onleesbare "alles-fiche" geven.

### Berekenen-percentage als zelfstandige competentie
`berekenen-controle-en-belangenpercentage` is bewust uitgekapseld als losse fiche, ook al wordt zij gebruikt door verschillende andere competenties. Reden: het is de meest voorkomende valkuil bij examen-tabellen ("M x % van A, A y % van B") en verdient een eigen procedurele behandeling met de subtiele regel dat controle-% en belang-% verschillende rekenregels volgen. De wettelijk_pct ligt lager (60 %) omdat de rekenconvention vooral CBN-doctrinair is.

### Eerste consolidatie ↔ wijziging consolidatiekring
Ik heb `uitvoeren-eerste-consolidatie` (de eerste opname op zich) gescheiden van `verwerken-wijziging-consolidatiekring` (de bredere set van kantelpunten, realisaties en transacties onder gemeenschappelijke leiding). Eerste consolidatie wordt namelijk óók binnen wijzigingen toegepast (bij elke nieuwe opname), maar is breder bruikbaar (initiële kringopbouw). De wijziging-fiche linkt expliciet naar eerste-consolidatie.

### Niet als aparte competentie behandeld
- **Opstellen geconsolideerd jaarverslag**: voorlopig niet als procedurele competentie opgenomen. Het is sterk inhoudelijk ("toelichten van risico's, vooruitzichten, gebeurtenissen na balansdatum") en minder een mechanische procedure. Kan in een latere ronde toegevoegd worden als een rapporteringsfiche.
- **IFRS-consolidatieraamwerk**: het concept-record beschrijft het kader (IFRS 3/10/11/12) en wanneer het wettelijk verplicht is, maar geen geconsolideerde IFRS-procedure. Geen aparte competentie — wordt impliciet meegenomen in `bepalen-consolidatieverplichting` (keuze van raamwerk) en de andere competenties (waar verschillen tussen WVV en IFRS relevant worden, blijven die thema's op concept-niveau).
- **Horizontale consolidatie** kreeg geen eigen competentie maar zit als methode-keuze in `kiezen-consolidatiemethode`. Het concept beschrijft een afgeleide procedure (verticaal per lid, dan integraal samenvoegen) die niet veel meer toevoegt buiten het keuzemoment.

## Cross-PO observaties

- `bepalen-consolidatieverplichting`: de toetsing aan groottecriteria (WVV art. 1:26) raakt aan **PO 1.1** (jaarrekeningenrecht, groottecategorieën). De vrijstelling van subconsolidatie en consortium-regels zijn echter specifiek voor 1.4.
- `toepassen-uniforme-waarderingsregels`: de waarderingsbeginselen (KB WVV art. 3:116-3:118) liggen in het verlengde van de enkelvoudige waarderingsregels in **PO 1.1**. Een latere PO 1.1-versie kan hiernaar verwijzen.
- `kwalificeren-relatie-deelneming`: de drempelvermoedens (> 50 %, 20 %) en het concept "controle in feite" zijn cross-cutting; ze komen ook terug in **PO 1.2 (audit)** waar controle-relaties relevant zijn voor reikwijdte van de opdracht.

## Records die "los" blijven

Geen record blijft volledig zonder procedurele dekking. Alle 30 records worden door minstens één competentie gerefereerd. Onderstaande records komen voornamelijk als ondersteunend-conceptueel terug, niet als drager van een eigen competentie:

- `geconsolideerd-jaarverslag` — bewust niet uitgewerkt als procedurele competentie (zie afweging hierboven). Kan in een latere ronde een rapporteringsfiche worden.
- `ifrs-consolidatieraamwerk` — pure raamwerk-kennis, geen aparte procedure. Wordt impliciet meegenomen in `bepalen-consolidatieverplichting`.
- `geconsolideerde-jaarrekening` — uitgangsdefinitie (vermogen, financiële positie en resultaat van het geheel). Wordt door bijna alle competenties geraakt maar dekt geen eigen procedure.
- `controle` (basisbegrip) — zit in de DNA van `kwalificeren-relatie-deelneming`; geen separate fiche nodig.
- `moedervennootschap` — actor-record; ondersteunt `bepalen-consolidatieverplichting`.
- `dochteronderneming`, `geassocieerde-onderneming`, `gemeenschappelijke-dochteronderneming` — actor-records; ondersteunend voor kwalificatie + methode-keuze.

## Validatie

Alle 9 YAML-bestanden zijn gevalideerd via een lokaal Python-script:

- `gebaseerd_op_concepten` ≥ 2 voor elke fiche (range: 3-8).
- `wettelijk_pct + praktijk_pct == 100` exact voor elke fiche.
- Elke `stap` heeft een `grondslag` met geldige `type` en `ref`.
- Elke concept-id in `gebaseerd_op_concepten` en in `grondslag.ref` (type: concept) verwijst naar een bestaand record in `data/concepten/records/`.
- Cross-competence wikilinks (`[[competenties/<id>|alias]]`) gebruiken bestaande gegenereerde id's.
- Geen enkele competentie heeft `praktijk_pct > 50 %`; geen extra mens-review op die grond vereist.

## Volgende stap

Mens-curatie: review van elke fiche door een ervaren beoefenaar (vermoedelijke focus op stap-formulering en valkuilen). Na curatie: `status: voorgesteld` → `goedgekeurd` + invullen `_provenance.gecureerd_door/op`.
