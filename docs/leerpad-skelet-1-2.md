# Leerpad-skelet PO 1.2 — Boekhoudrecht en jaarrekeningenrecht

**Status**: voorstel (2026-06-01).
**Volgende stap**: scripts in `data/leerstukken/<slug>.yaml` per leerstuk + voorbeeldgroep in `data/voorbeeldgroepen/bourdon-vermeer.yaml`.

---

## 1. Programma-analyse

### Officiële taak + doelstellingen

PO 1.2 heeft **één hoofdtaak** met **twee doelstellingen**:

> **Taak 1.2.1**: Opstellen van de individuele jaarrekening

| Code | Tekst | Anchor-rol |
|---|---|---|
| 1.2.taak.1.doel.1 | Een beginsel van boekhoudrecht of een wettelijke bepaling uit Belgische of Europese bron opzoeken, grondig analyseren en toepassen, in voorkomend geval met inachtneming van internationale normen | context |
| 1.2.taak.1.doel.2 | Verifiëren en waarborgen van de conformiteit van de boekhouding en documenten met de wettelijke vereisten | context |

**Vereist niveau**: *integratie* (volgens PO-metadata `niveau: integratie` — het hoogste niveau).

De **subtaken** (1.2.taak.1.a t/m e) lopen vooruit op analyse — balansherstructurering, balansaggregaten interpreteren, kasstromen, ratio's, sectorvergelijking. Die zijn formeel onder PO 1.2 gegroepeerd maar inhoudelijk **PO 1.3-stof** (analyse jaarrekening). Het examenprogramma plaatst ze hier omdat het opmaken en interpreteren één integratie-beweging vormt, maar de leerstof leeft elders.

### Kern vs rakend

- **Kern (uit doelstellingen)**: het **wettelijke kader rond de jaarrekening** — bronnen + autoriteiten, boekhoudplicht, grootte-toetsing, schema-keuze, toelichting/jaarverslag/sociale balans, neerlegging, sancties. De doelstellingen vragen *zelf wettelijke bepalingen opzoeken/toepassen* en *conformiteit waarborgen* — recht-eerst, techniek-tweede.
- **Rakend**: de **techniek van het opmaken** (eindejaarsverrichtingen, resultaatbestemming, proefbalans, waarderingsregels op detail-niveau) overlapt met PO 1.1 + 1.4. Het cross-PO leerstuk [[individuele-jaarrekening-opmaken]] (gehost onder PO 1.4) dekt die zijde — PO 1.2 verwijst er kort naar.
- **Rakend**: de **analyse** van wat opgemaakt is — herstructureren, ratio's, kasstroomanalyse — woont volledig in PO 1.3 ([[wat-is-jaarrekeninganalyse]], [[ratios-en-kengetallen]], [[kasstroom-en-financieringstabel]], [[jaarrekening-herwerken-en-functionele-balans]]).

---

## 2. Voorbeeldexamen-patronen

Uit `content/studiemateriaal/1-2/voorbeeldexamenvragen.md`: **11 vraag-eenheden** met PO 1.2 getagd (voorbeeldexamens 2003-2014). Alle met modelantwoord beschikbaar.

| Onderwerp | Hoe vaak | Type vraag | Centraal voor leerstuk |
|---|---|---|---|
| Schema-keuze (volledig/verkort) bij verbonden vennootschappen | 1× (2014-1) | Toepassings-case met aggregatie | `vennootschap-grootte-en-schema-keuze` |
| Schema-keuze moeder vs dochter (geconsolideerde toetsing) | 1× (2008-bibf) | Toetsing op geconsolideerde basis voor moeder | `vennootschap-grootte-en-schema-keuze` |
| Vermelding bestuurders eerste bladzijde jaarrekening | 1× (2013-2) | Wie staat waar? | `jaarrekening-publiceren-en-sancties` |
| Wijziging afschrijvingspercentage (prospectief) | 1× (2013-2) | Boekhoudkundig + juridisch | `wie-moet-boekhouden-en-hoe` (beginselen) + cross-PO 1.1 |
| Niet-neerlegging — sancties (tariefbijdrage, aansprakelijkheid, art. 2:74 WVV) | 1× (2013-2) | Adviezen aan cliënt | `jaarrekening-publiceren-en-sancties` |
| Verantwoording waarderingsregels (groot vs klein) | 1× (2013-1) | Onderscheid schema | `jaarrekening-publiceren-en-sancties` + `wie-moet-boekhouden-en-hoe` |
| Honoraria commissaris — boeking + toelichting | 1× (2008-bibf) | Rekeningkeuze + toelichting | `jaarrekening-publiceren-en-sancties` (toelichting-aspect) + cross-PO 1.1 |
| Sociale balans — opleidingskost | 1× (2008-bibf) | Berekeningsbestanddelen | `jaarrekening-publiceren-en-sancties` (sociale balans) |
| Vereenvoudigde boekhouding — toepassing + inhoud | 1× (2003-bibf) | Wie + wat | `wie-moet-boekhouden-en-hoe` |
| Centralisatieboek — inhoud + frequentie | 1× (2003-bibf) | Wetstekst-toepassing | `wie-moet-boekhouden-en-hoe` |
| Herwaardering activa — wat + voorwaarden | 1× (2003-bibf) | Cumulatieve voorwaarden | Cross-PO 1.1 (`herwaardering-vast-actief`) |

**Patroon**: het examen toetst de **scharnierregels** waar regime kantelt:
- Grootte-kanteling: micro → klein → groot, met **geconsolideerde toetsing voor moeders** en **micro-uitsluiting voor dochters** (vragen 2014-1 + 2008-bibf).
- Plicht-kanteling: wie mag vereenvoudigd (omzet-drempel, vennootschappen altijd dubbel — vraag 2003-bibf).
- Sanctie-kanteling: niet-neerlegging trekt tariefbijdrage + bestuurdersaansprakelijkheid + gerechtelijke ontbinding art. 2:74 WVV (vraag 2013-2).
- Toelichting/jaarverslag-vermeldingen: klein vrijgesteld, groot verplicht (vragen 2013-1, 2013-2, 2008-bibf).

Klassieke valkuilen: aggregatie verwarren met consolidatie; dochter erft grootte van moeder (onjuist); CBN-advies = wet (onjuist).

---

## 3. Leerstuk-voorstel

Vier leerstukken dekken de kern; één bestaand cross-PO leerstuk dekt de techniek.

### Leerstuk 1 — `wat-is-belgisch-boekhoudrecht`

- **Vraag**: Welke wettelijke bronnen regelen het Belgische boekhoud- en jaarrekeningenrecht, en wie zegt wat?
- **Type**: entry-fiche (bronnenoverzicht + autoriteiten — kort, hiërarchisch).
- **Gedekte doelstellingen**: 1.2.taak.1.doel.1 (wettelijke bron opzoeken en toepassen — bronnenkennis-voorwaarde).
- **Gedekte kenniselementen**: 1.2.I (Bronnen — EU, Grondwet, wet, KB, koninkl. besluiten, normen, adviezen) — alle subitems.
- **Gedekte concepten**: `belgisch-boekhoudrecht` (hoofdrecord) + `autoriteiten-boekhoudrecht`.
- **Rationale**: zonder bronnenkennis loopt elke andere doelstelling vast. Examen-typisch: "welke autoriteit geeft welke uitspraak?" + "is CBN-advies bindend?". Klein leerstuk (max ~2500 woorden) — voorbereiding op de zwaardere drie.

### Leerstuk 2 — `wie-moet-boekhouden-en-hoe`

- **Vraag**: Wie is boekhoudplichtig, op welke manier (dubbele vs vereenvoudigd), volgens welke beginselen, en hoe lang moet alles bewaard?
- **Type**: scope + plicht-fiche.
- **Gedekte doelstellingen**: 1.2.taak.1.doel.2 (conformiteit waarborgen) — de praktische kant van plicht-naleving.
- **Gedekte kenniselementen**: 1.2.II (Boekhoudwet/WER Boek III — boekhoudplicht + technische voorschriften), 1.2.III (waarheidsgetrouwheid + voorzichtigheid + bestendigheid + ...), 1.2.IV indirect (boekhoudkundige beginselen toegepast op de dagelijkse praktijk).
- **Gedekte concepten**: `boekhoudplicht` + `dubbele-boekhouding` + `boekhoudbeginselen` + `boekhouding` (Σ-record).
- **Rationale**: WER Boek III + KB 21-10-2018 + 8 beginselen vormen één pedagogische beweging — wie moet boekhouden + hoe + volgens welke regels. Examen-typisch: vereenvoudigde-boekhouding-toepassingsgebied (2003-bibf), centralisatie (2003-bibf), wijziging afschrijvingspercentage (2013-2 — bestendigheidsbeginsel). Bewaarplicht hoort hier ook bij (was apart themafiche). Hardste werkpaard, mogelijk tot ~4000 woorden.

### Leerstuk 3 — `vennootschap-grootte-en-schema-keuze`

- **Vraag**: Hoe bepaal je de groottecategorie van een vennootschap (micro/klein/groot), wat verandert daardoor, en wat is de bijzonderheid voor moeders, dochters en VZW's?
- **Type**: scharnier-fiche (één regel-systeem, twee toepassings-domeinen: vennootschap + vereniging).
- **Gedekte doelstellingen**: 1.2.taak.1.doel.1 (wettelijke bepaling — art. 1:24-25 WVV + WVV-VZW art. 3:47).
- **Gedekte kenniselementen**: 1.2.V (groottecategorieën vennootschappen — drempels + cascade + cijferzakboekje-cijfers).
- **Gedekte concepten**: `vennootschap-groottecategorieen` + `groottecategorie-vereniging`.
- **Rationale**: dit is het meest geëxamineerde stuk van PO 1.2 — de schema-keuze-vragen (2014-1, 2008-bibf) draaien rond geconsolideerde toetsing voor moeders + micro-uitsluiting voor dochters. Verdient eigen leerstuk omdat de regels één blok zijn: drempels → cascade → uitzonderingen (moeder, dochter, beurs-genoteerd, vereniging). Cijfers in toelichting komen uit Cijferzakboekje — examen-bron.

### Leerstuk 4 — `jaarrekening-publiceren-en-sancties`

- **Vraag**: Wat moet er in de jaarrekening + bijlagen, hoe wordt ze gepubliceerd, en wat als het niet gebeurt?
- **Type**: proces + sanctie-fiche.
- **Gedekte doelstellingen**: 1.2.taak.1.doel.2 (conformiteit van documenten waarborgen).
- **Gedekte kenniselementen**: 1.2.VI (jaarrekening — schema + toelichting + jaarverslag + sociale balans + waarderingsregels in toelichting), 1.2.VII (openbaarmaking + neerlegging + sancties).
- **Gedekte concepten**: `jaarrekening` (Σ-record) + `eindejaarsverrichtingen` (kort — voor cross-PO link).
- **Rationale**: dekt zes van de elf examenvragen — bestuurdersvermelding (2013-2), niet-neerlegging-sancties (2013-2), waarderingsregels-verantwoording (2013-1), honoraria commissaris-toelichting (2008-bibf), sociale balans (2008-bibf), en jaarverslag-inhoud. Verdient eigen leerstuk — toelichting + jaarverslag + neerlegging + sancties zijn één wettelijk proces. Tussen ~3500 en 4500 woorden mogelijk.

### Cross-PO leerstuk — `individuele-jaarrekening-opmaken`

Bestaand leerstuk onder `content/leerstukken/` (gehost via PO 1.4-scripts). Dekt de **techniek** — eindejaarsverrichtingen, resultaatbestemming, proefbalans, waarderingsregels detail. PO 1.2 verwijst er kort naar in §3 van het overzicht. Niet dupliceren — alleen linken.

---

## 4. Gap-check

| Doelstelling / kenniselement | Gedekt door | Notitie |
|---|---|---|
| 1.2.taak.1.doel.1 (wettelijke bron opzoeken + toepassen) | Alle vier leerstukken | Vol gedekt — elk leerstuk verankert in primaire bronnen via "Wettelijk fundament" |
| 1.2.taak.1.doel.2 (conformiteit waarborgen) | Leerstuk 2 (plicht + naleving) + Leerstuk 4 (jaarrekening-conformiteit) | Vol gedekt |
| 1.2.I (Bronnen + autoriteiten) | Leerstuk 1 | Vol |
| 1.2.II (WER Boek III + boekhoudplicht) | Leerstuk 2 | Vol |
| 1.2.III (Boekhoudbeginselen) | Leerstuk 2 | Vol |
| 1.2.IV (KB 29-04-2019 + waarderingsregels) | Leerstuk 2 (toepassing) + Leerstuk 4 (waarderingsregels in toelichting) | Vol — gespreid |
| 1.2.V (Groottecategorieën) | Leerstuk 3 | Vol |
| 1.2.VI (Jaarrekening — schema + toelichting + sociale balans) | Leerstuk 4 | Vol |
| 1.2.VII (Openbaarmaking + sancties) | Leerstuk 4 | Vol |
| Subtaken 1.2.taak.1.a-e (herstructureren, ratio's, kasstromen, sectorvergelijking) | **Niet hier** — verwijzing naar PO 1.3 leerstukken | Bewuste uitsluiting (zie §1 "Rakend") |

**Geen gaten.** Twee verwijzingen cross-PO (techniek → PO 1.4 `individuele-jaarrekening-opmaken`, analyse → PO 1.3).

---

## 5. Minicursus-skelet (overzicht / `index.md`)

Volgt de canonieke 5-secties-structuur van ADR-036 (na samenvoeging §3+§4):

### §1 — Waarom dit vak?

- Motivatie: PO 1.1 leert je *hoe* je boekt; dit PO leert je *binnen welke wettelijke spelregels*. Boekhoud- en jaarrekeningenrecht regelen wie boekhoudplichtig is, in welk schema de jaarrekening wordt opgesteld, welke beginselen gelden, en wat de gevolgen zijn van niet-naleving.
- Bredere-programma-tabel: relatie tot 1.1 (techniek), 1.3 (analyse — opvolger), 1.4 (consolidatie — eigen kader bovenop), 1.5 (IFRS — alternatief kader), 3.0 (WVV als gemeenschappelijke bron).

### §2 — Wat is dit vak?

Vier compacte sub-secties, elk eindigend met wikilink naar het leerstuk dat het uitwerkt:

- **Het probleem** → context voor [[wat-is-belgisch-boekhoudrecht]] (waarom uniforme regels)
- **Waar komt het recht vandaan** → [[wat-is-belgisch-boekhoudrecht]] (bronnen + autoriteiten)
- **Wie moet en hoe** → [[wie-moet-boekhouden-en-hoe]] (plicht + dubbele/vereenvoudigde + beginselen)
- **Grootte stuurt het regime** → [[vennootschap-grootte-en-schema-keuze]] (drempels + cascade)
- **De jaarrekening naar buiten** → [[jaarrekening-publiceren-en-sancties]] (publicatie + sancties)

### §3 — Wat moet je kunnen + hoe pak je het aan

Leerstukken-leesroute in vier stappen + cross-PO doorklik naar [[individuele-jaarrekening-opmaken]] voor wie de techniek wil zien. Plus verwijzing naar [[studiemateriaal/1-2/samenvatting|samenvatting]] voor herhaling. Geen rol-blokken (die zitten in de leerstukken).

### §4 — Examen-radar

Tabel met 11 voorbeeldexamen-eenheden + observatie ("toetst scharnierregels: grootte-kanteling, plicht-kanteling, sanctie-kanteling, vermelding-verschillen klein/groot").

### §5 — Concepten cross-PO

Tabel van concepten die ook in 1.1 / 1.3 / 1.4 / 1.6 / 3.0 leven (jaarrekening, vennootschap-groottecategorieen, boekhoudplicht, ...).

---

## 6. Voorbeeldgroep

**Naam**: `bourdon-vermeer` — dunne bindcase.
**Locatie**: `data/voorbeeldgroepen/bourdon-vermeer.yaml`.

### Keuze-rationale

PO 1.2 is — net als PO 2.1 en PO 2.7 — een **juridisch kader-vak**. Geen doorlopende financiële draad door alle leerstukken zoals Aurelia voor consolidatie. Wel: een **galerij van mini-personages** die scharnier-situaties illustreren. De voorbeeldgroep is *dun* — leerstukken kunnen er kort op leunen of inline-mini-cases gebruiken.

### Personages

- **Bourdon BV** — kleine vennootschap die net het kantelpunt klein → groot bereikt (drempel-test over twee jaar). Illustreert schema-keuze + (vanaf overschrijding) jaarverslag + commissarisplicht.
- **Vermeer NV** — moedervennootschap van Bourdon (60% controle). Illustreert geconsolideerde toetsing voor moeders + micro-uitsluiting voor dochters.
- **Jan De Smet — zelfstandig architect** — natuurlijke persoon onder/boven de omzet-drempel (€ 500 000). Illustreert vereenvoudigde vs dubbele boekhouding-vraag.
- **Buurthuis Linde VZW** — middelgrote VZW met betaald personeel + activiteiten. Illustreert WVV-VZW groottecategorieën + ander schema.

### Inhoud (één YAML-bestand)

- Personages-beschrijving + rolspel (welk leerstuk leunt waarop)
- Drempel-tabel voor klein/groot kanteling Bourdon (twee opeenvolgende boekjaren, gemarkeerd "twee van drie overschreden")
- Drempel-tabel voor VZW Buurthuis Linde
- Geconsolideerd-toets-tabel voor Vermeer + Bourdon
- Mini-case "Bourdon publiceert te laat" — sanctie-keten (tariefbijdrage + 2:74 WVV)
- Mini-case "Bourdon wijzigt afschrijvingspercentage" — bestendigheidsbeginsel + toelichting-verantwoording
- Bestuurdersvermelding eerste-bladzijde-mock voor Bourdon
- Sociale-balans-fragment voor Bourdon (verkort schema)

Geen kloppende balans-en-resultatenrekeningen-doorheen-alle-leerstukken — dat is overkill voor een recht-focus.

---

## 7. Themafiche-mapping

Bestaande cluster-themafiches die PO 1.2 raken:

- `content/themafiches/boekhoudplicht-en-rechtsbronnen.md` — dekt L1 + L2 grotendeels. Migreert naar `content/studiemateriaal/1-2/samenvatting.md` per ADR-039.
- `content/themafiches/jaarrekening-schema-en-publicatie.md` — dekt L3 + L4. Migreert naar samenvatting.
- Beide worden **verwijderd** in de samenvatting-commit (`git rm`).

Cross-cluster themafiches die blijven (raken meerdere PO's): `eindejaarsverrichtingen-en-waardering.md` (raakt 1.1/1.2/1.4), `be-gaap-vs-ifrs-vergelijking.md` (raakt 1.2/1.5), `bewaarplicht.md` (raakt 1.2/2.1) — niet aanraken in deze ronde.

Geen nieuwe themafiches nodig voor PO 1.2.

---

## 8. Oefening — beslismoment

PO 1.2 is recht-eerst. Een 60-75 min doorgewerkte case zoals Nordica (consolidatie) of Tessera (diagnose) past **minder natuurlijk**: de student moet vooral regels-opzoek + scharnier-redenering kunnen, niet een lange technische uitvoering doen.

**Voorstel**: een **korte gestructureerde oefening** (~30-40 min) met drie mini-deelopgaven rond de voorbeeldgroep:
1. Bourdon BV — bepaal de juiste groottecategorie voor boekjaar N (gegeven twee jaar cijfers + dochter-situatie) en kies het schema.
2. Wat verandert er voor Bourdon BV wanneer het op of net over de drempel kantelt (jaarverslag, commissaris, schema)?
3. Bourdon BV heeft jaarrekening N-1 niet binnen de termijn neergelegd — formuleer een advies aan de zaakvoerder (sancties + remediëring).

Geen lange JR-opmaak — die zit in PO 1.4 oefening. Beslismoment tijdens uitvoering: hou kort genoeg om geen lopende-tekst-case te worden.

---

## 9. Open punten

1. **Granulariteit L4** — leerstuk 4 is breed (jaarrekening-inhoud + publicatie + sancties). Bij uitvoering: kijk of opbouw-secties niet te veel sub-onderwerpen krijgen. Indien te zwaar: niet splitsen, maar bewust beats compact houden.
2. **Cijfers**: alle drempel-cijfers (€ 500 000 voor vereenvoudigd, art. 1:24 §6 WVV-drempels, tariefbijdrage-bedragen) moeten in scripts-fase via MCP `certificaid-tarieven` of Cijferzakboekje bevestigd worden. Bij twijfel: "⚠️ raadpleeg Cijferzakboekje bij examen".
3. **Bestaande index.md** — overzicht is geschreven in de OUDE stijl (concept-wikilinks ipv leerstuk-wikilinks). Wordt herschreven naar nieuwe norm in stap 5.
