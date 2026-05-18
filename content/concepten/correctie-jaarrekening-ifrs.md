---
title: Correctie van de jaarrekening — IAS 8 versus CBN 2020/12
tags:
- concept
- cluster
- po-1-5
linked_anchors:
- 1.5.IV.C
- 1.5.IV
programmaonderdelen:
- '1.5'
confidence: grounded
node_type: cluster
status: seed
schema_version: '1.5'
gegenereerd_uit: data/concepten/records/correctie-jaarrekening-ifrs.json
gegenereerd_op: '2026-05-18'
---
# Correctie van de jaarrekening — IAS 8 versus CBN 2020/12 ⚖️

> [!summary] Korte inhoud
> **Correctie van de jaarrekening** is het rechtzetten van een eerder gepubliceerde jaarrekening — door wijziging van een grondslag voor financiële verslaggeving, herziening van een schatting of correctie van een fout uit een vorige periode.

**Correctie van de jaarrekening** is het rechtzetten van een eerder gepubliceerde jaarrekening — door wijziging van een grondslag voor financiële verslaggeving, herziening van een schatting of correctie van een fout uit een vorige periode. Onder IFRS regelt **IAS 8** drie scherp onderscheiden categorieën met elk een eigen verwerking: retroactief (grondslag, fout) of prospectief (schatting). Onder Belgisch GAAP geldt **CBN 2020/12** voor de enkelvoudige jaarrekening; de principes lopen grotendeels gelijk maar publicatie-formaliteiten verschillen — onder BE-GAAP wordt een 'verbeterde jaarrekening' opnieuw bij de Nationale Bank gedeponeerd, terwijl IFRS de correctie in de **volgende** jaarrekening (vergelijkende cijfers) verwerkt.

_Bron: IAS 8 + CBN 2020/12_


## Bouwstenen

### Onderscheid schatting versus fout — soms moeilijk ⚖️

Een **fout** vereist dat de juiste informatie op publicatiedatum redelijkerwijze beschikbaar had moeten zijn. Een **schatting** is herziening op basis van nieuwe omstandigheden of betere techniek. Wanneer in twijfel: documenteer de redenering. Een keuze voor 'fout' (retroactief) heeft grote impact; een keuze voor 'schatting' (prospectief) ook — maar omgekeerd.

**Waarom?** Auditors testen deze classificatie streng — een 'cosmetische' herclassificatie van een fout als 'schattingswijziging' om retroactieve correctie te vermijden is een auditbevinding.


_Grondslag: IAS 8 alinea 5 (definities) + 41_

### Praktisch onhaalbaar — uitzondering ⚖️

Indien retroactieve toepassing voor een eerdere periode **praktisch onhaalbaar** is (alinea 23-25 voor grondslagwijzigingen, alinea 43 voor fouten): pas de wijziging toe vanaf de vroegste haalbare periode. Praktisch onhaalbaar = de entiteit kan ondanks redelijke inspanningen de informatie niet reconstrueren.

**Waarom?** Soms is hindsight nodig om retroactief de cijfers te bepalen — wat IFRS niet toelaat. Bv. een grondslagwissel voor IFRS 9 zou cashflowprognoses vereisen die er destijds niet waren. In zulke gevallen mag prospectief vanaf de eerste haalbare datum.


_Grondslag: IAS 8 alinea 23-25 + 43_


## Berekening

### Procedure correctie jaarrekening — classificatie en behandeling

### 1. Classificeer de aanpassing

Bepaal of de aanpassing een (a) wijziging in grondslag, (b) schattingswijziging of (c) fout is. Onderscheid is cruciaal: andere behandeling per categorie. Bij twijfel tussen schatting en fout: een fout bevat onjuiste informatie die op publicatiedatum redelijkerwijs beschikbaar was; een schatting hangt af van nieuwe informatie of betere techniek.

**Waarom?** Verkeerde classificatie leidt tot verkeerde behandeling — retroactief versus prospectief — met materiële impact op cijfers en op vertrouwen van gebruikers.

**📥 Input**:
- Beschrijving aanpassing → **Aard + oorzaak** _(informatie)_

**📤 Output**:
- Classificatiebeslissing → **Grondslag/schatting/fout** _(beslissing)_

**🛠️ Hoe**:

1. Zelena Bio ontdekt in 2026 dat ze in 2024 een voorraad van € 1.200.000 over het hoofd zag bij stocktelling (was wel fysiek aanwezig).
2. Test: Op publicatiedatum 2024-jaarrekening had Zelena dit kunnen weten met grondige controle? Ja → fout.
3. Conclusie: fout uit vorige periode → retroactieve correctie.

**Grondslag**: IAS 8 alinea 5 + 41

### 2. Pas retroactieve correctie toe (fouten + grondslagwijzigingen)

Bij retroactieve toepassing: pas de nieuwe grondslag of correctie aan alsof ze altijd had bestaan. Concreet: (a) pas vergelijkende cijfers van eerdere periodes aan; (b) als de fout/wijziging materieel effect heeft op een periode vóór de vergelijkende: pas het beginsaldo van ingehouden winsten van de vroegste gepresenteerde periode aan; (c) presenteer een **derde balans** als de impact op de openingsbalans van de vergelijkende periode materieel is (IAS 1 alinea 40A).

**Waarom?** Retroactieve aanpassing simuleert hoe de cijfers eruit zouden hebben gezien zonder de fout. Gebruikers zien een coherent beeld over periodes — anders zou een correctie van 5 jaar oude fouten de winst van het lopende jaar verstoren.

**📥 Input**:
- Originele cijfers vorige periode → **Foutieve cijfers** _(boekhoudkundig-bedrag)_
- Aanpassingsbedrag → **Correctie + ev. uitgestelde belasting** _(boekhoudkundig-bedrag)_

**📤 Output**:
- Aangepaste vergelijkende cijfers → **Correctie reflecteert** _(boekhoudkundig-bedrag)_
- Toelichting fout → **Aard + impact per regel** _(toelichtingsnoot)_

**🛠️ Hoe**:

1. Zelena Bio's fout: voorraad € 1.200.000 niet opgenomen in 2024.
2. Correctie: balans 31 december 2024 voorraad +€ 1.200.000; ingehouden winsten +€ 900.000 (na 25% uitgestelde belasting); uitgestelde belastingverplichting +€ 300.000.
3. Vergelijkende cijfers in 2025-jaarrekening (gepubliceerd in 2026 met correctie): aangepast voor de fout.
4. Derde balans (1 januari 2024) opnemen als materieel.
5. Toelichting noot 'Fout uit vorige periode' met aard + bedrag per regel.

**Grondslag**: IAS 8 alinea 42 + IAS 1 alinea 40A

### 3. Pas prospectieve toepassing toe (schattingswijziging)

Bij schattingswijziging: GEEN aanpassing van vergelijkende periodes. De wijziging wordt toegepast vanaf het moment van herziening — toekomstige effecten in winst of verlies. Toelichting van aard en bedrag van effect indien materieel.

**Waarom?** Schattingen evolueren met de tijd. Eerdere schattingen waren niet 'fout' — ze weerspiegelden de info op dat moment. Retroactief aanpassen zou hindsight-rapportering zijn.

**📥 Input**:
- Nieuwe schatting → **Bedrag + grondslag** _(boekhoudkundig-bedrag)_
- Resterende toekomst → **Periodes waar de schatting nog impact heeft** _(periode)_

**📤 Output**:
- Toekomstige boekingen → **Aangepaste afschrijving/voorziening/etc** _(boekhoudkundig-bedrag)_

**🛠️ Hoe**:

1. Zelena's productielijn (kostprijs € 13.800.000, gestart 1 januari 2026, oorspronkelijk 20 jaar): boekwaarde 31 december 2030 = € 13.800.000 − 5 × € 690.000 = € 10.350.000.
2. Eind 2030 herziet management gebruiksduur naar resterend 8 jaar (was 15).
3. Vanaf 2031: € 10.350.000 / 8 = € 1.293.750/jaar.
4. Geen aanpassing van afschrijvingen 2026-2030 — prospectieve toepassing.
5. Toelichting: aard schattingswijziging + effect (€ 603.750/jaar extra afschrijving in toekomst).

**Grondslag**: IAS 8 alinea 36-40


> [!info]- Niet verwarren met [[wijziging-boekhoudkundig-referentiestelsel]]
> Stelselwijziging (BE-GAAP ↔ IFRS, CBN 2022/08) is een fundamentele heropbouw van de cijferbasis. Grondslagwijziging binnen één stelsel (IAS 8 alinea 14) is een beperkte aanpassing — bv. binnen IFRS van kostprijs- naar herwaarderingsmodel voor MVA. Beide retroactief, maar de stelselwijziging is veel ingrijpender en gebruikt IFRS 1 voor eerste IFRS-toepassing.
>
> _Trigger_: Examen: 'Onderneming wijzigt afschrijvingsmethode' (lineair → degressief) — IAS 8 schattingswijziging (prospectief). 'Onderneming wijzigt waarderingsbasis vastgoed' (kostprijs → herwaardering) — IAS 8 grondslagwijziging (retroactief). 'Onderneming gaat over naar IFRS' — IFRS 1 + CBN 2022/08.


## Valkuilen

> [!warning]- Een wijziging in afschrijvingsmethode is een **schattingswijziging** (IAS 16 alinea 61 + IAS 8 alinea 38), GEEN grondslagwijziging — dus pro…
> ⚠️ Een wijziging in afschrijvingsmethode is een **schattingswijziging** (IAS 16 alinea 61 + IAS 8 alinea 38), GEEN grondslagwijziging — dus prospectief, niet retroactief. Stagiairs verwarren dit vaak met grondslagwijzigingen die wel retroactief zouden moeten. ⚖️
>
> _Bron: IAS 16 alinea 61 + IAS 8 alinea 38_


> [!warning]- Onder Belgisch GAAP geldt CBN 2020/12
> ⚠️ Onder Belgisch GAAP geldt CBN 2020/12. De principes zijn vergelijkbaar maar de **publicatie-vereisten** zijn anders: BE-GAAP vereist soms een aangepaste deponering bij de Nationale Bank, met expliciete vermelding 'verbeterde jaarrekening'. Onder IFRS gebeurt correctie in de **volgende** jaarrekening (vergelijkende cijfers), niet via een aparte 'verbeterde' jaarrekening. ⚖️
>
> _Bron: CBN 2020/12 vs. IAS 8_



## Zie ook

- **Vereist kennis van**: [[mutatieoverzicht-eigen-vermogen-ifrs]]

> [!todo] Voorbeeld ontbreekt voor dit concept
> Een latere ENRICH-pass voegt een synthese-voorbeeld toe.

## Bronnen

[^1]: `IAS-8-grondslagen-voor-financiele-verslaggeving-schattingswijzigingen-en-fouten__sec_definities`
[^2]: `CBN-2020-12-correctie-van-de-jaarrekening-0__sec_voorbeeld`
[^3]: `IAS-1-presentatie-van-de-jaarrekening__sec_jaarrekening`
