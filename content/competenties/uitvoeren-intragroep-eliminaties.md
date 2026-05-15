---
title: Uitvoeren van intragroep-eliminaties en berekenen van het aandeel van derden
tags:
- competentie
- po-1-4
programmaonderdelen:
- '1.4'
status: voorgesteld
schema_version: '1.0'
gegenereerd_uit: data/concepten/competenties/uitvoeren-intragroep-eliminaties.yaml
gegenereerd_op: '2026-05-15'
---
# Uitvoeren van intragroep-eliminaties en berekenen van het aandeel van derden

**⚖️ 80% · 🤖 20%** · Status: `voorgesteld`

> De eliminatieplichten en de berekening van het aandeel van derden zijn wettelijk vastgelegd (KB WVV art. 3:134-3:140); de materialiteitsbeoordeling (verwaarloosbare bedragen, art. 3:139) is een praktijkoordeel.

## Aanbevolen werkwijze

### 1. Identificeren van onderlinge vorderingen en schulden

📥 **Input**: Geconsolideerde proefbalansen van moeder en dochters; intercompany-reconciliaties
📤 **Output**: Lijst van wederzijdse vorderingen en schulden tussen consoliderende vennootschap en in de consolidatie opgenomen dochters (en tussen die dochters onderling)
**Waarom**: Onderlinge posities moeten worden geschrapt om dubbeltelling in de geconsolideerde balans te vermijden.
**Grondslag**: [[intragroep-eliminaties]]
### 2. Elimineren van onderlinge vorderingen en schulden

📥 **Input**: De geïdentificeerde wederzijdse vorderingen en schulden
📤 **Output**: Geconsolideerde balans waarin enkel posities tegenover entiteiten buiten de consolidatiekring blijven staan; intercompany-saldi zijn naar nul gebracht
**Waarom**: Het beeld 'alsof het geheel één enkele onderneming was' vereist dat interne posities verdwijnen.
**Grondslag**: [[intragroep-eliminaties]]
### 3. Elimineren van in activa begrepen onderlinge winsten of verliezen

📥 **Input**: Voorraadbestanden bij elke groepsvennootschap; identificatie van voorraad of materiële vaste activa aangekocht binnen de groep met een marge; brutomarge% op intra-groepsverkopen
📤 **Output**: Eliminatie van niet-gerealiseerde winsten (brutomarge% × restvoorraad op balansdatum bij de kopende groepsvennootschap); het actief wordt teruggebracht tot zijn waarde voor de groep
**Waarom**: Winsten op interne transacties zijn economisch niet gerealiseerd zolang het actief de groep niet verlaten heeft.
**Grondslag**: [[intragroep-eliminaties]]
- ⚠️ **Alleen vorderingen/schulden moeten worden geëlimineerd; in voorraad begrepen intra-groepswinst hoeft niet.** → Activa moeten in de geconsolideerde balans verschijnen tegen hun waarde voor de groep; intra-groepswinst in voorraad of vaste activa wordt geëlimineerd. ([[intragroep-eliminaties]])
### 4. Elimineren van onderlinge opbrengsten en kosten

📥 **Input**: Resultatenrekeningen van groepsvennootschappen; lijst van interne verkopen, beheersvergoedingen, intresten, huur
📤 **Output**: Geconsolideerde resultatenrekening waarin onderlinge opbrengsten en kosten zijn geschrapt
**Waarom**: Dezelfde transactie mag niet dubbel verschijnen in de groepscijfers.
**Grondslag**: [[intragroep-eliminaties]]
### 5. Aanpassen van de eliminaties voor evenredig geconsolideerde gemeenschappelijke dochters

📥 **Input**: Lijst van gemeenschappelijke dochters die evenredig zijn geconsolideerd; belangenpercentage per gemeenschappelijke dochter
📤 **Output**: Eliminatie beperkt tot het pro-rata deel: niet 100 % van de intra-groepswinst, maar het belangenpercentage × intra-groepswinst (KB WVV art. 3:140, a)
**Waarom**: Bij evenredige consolidatie wordt slechts het pro-rata deel opgenomen; eliminatie moet daarbij aansluiten.
**Grondslag**: [[intragroep-eliminaties]]
### 6. Beoordelen van materialiteit

📥 **Input**: Bedragen van de geïdentificeerde eliminaties; geconsolideerd balanstotaal en resultaat
📤 **Output**: Beslissing of bepaalde eliminaties achterwege mogen blijven omdat ze van te verwaarlozen betekenis zijn (KB WVV art. 3:139, voor de eliminaties bedoeld in art. 3:134, 3:136 1°/2° en 3:138)
**Waarom**: De wet staat een proportionaliteitsoordeel toe; rituele eliminatie van triviale bedragen is niet vereist.
**Grondslag**: [[intragroep-eliminaties]]
### 7. Berekenen van het aandeel van derden (belangen van derden)

📥 **Input**: Eigen vermogen en resultaat van elke integraal geconsolideerde dochter op afsluitingsdatum; belangenpercentage per dochter
📤 **Output**: Belangen van derden (balans) = (1 − belang%) × eigen vermogen dochter op afsluitingsdatum; Aandeel van derden in resultaat = (1 − belang%) × resultaat dochter
**Waarom**: Bij integrale consolidatie wordt 100 % opgenomen; het deel toebehorend aan minderheidsaandeelhouders wordt afzonderlijk gepresenteerd.
**Grondslag**: [[minderheidsbelangen]]
- ⚠️ **Bij evenredige consolidatie moet ook een aandeel van derden worden geboekt.** → Minderheidsbelangen ontstaan uitsluitend bij integrale consolidatie waarbij de moeder < 100 % aanhoudt; bij evenredige consolidatie wordt het derden-deel niet opgenomen. ([[minderheidsbelangen]])
### 8. Aanpassen van de toelichtingsinformatie

📥 **Input**: Wettelijk vereiste inlichtingen over rechten en verplichtingen van de groep
📤 **Output**: Toelichting waarin de weggelaten wederzijdse rechten en verplichtingen niet meer voorkomen (KB WVV art. 3:138)
**Waarom**: Wat geëlimineerd is in cijfers moet ook in de toelichting consistent verdwijnen.
**Grondslag**: [[intragroep-eliminaties]]


## Voorbeelden

**Situatie**: Moeder M (90 % belang in dochter D) heeft aan D voorraad verkocht met een brutomarge van 25 %. Op balansdatum staat bij D nog 400 van die voorraad. D's eigen vermogen op afsluitingsdatum = 1.000; resultaat = 200.

**Conclusie**: Te elimineren intra-groepswinst in voorraad = 25 % × 400 = 100 (terug te brengen tot de waarde voor de groep). Belangen van derden op balans = (1 − 0,90) × 1.000 = 100; aandeel van derden in resultaat = (1 − 0,90) × 200 = 20.

**Grondslag**: [[intragroep-eliminaties]] §eliminatie voorraad; [[minderheidsbelangen]] §berekening

**Redenering**: Intra-groepswinst in voorraad wordt teruggedraaid omdat het actief de groep nog niet heeft verlaten; de complementaire 10 % belang wordt afgezonderd voor derden bij integrale consolidatie.

---

## Gebaseerd op concepten

[[intragroep-eliminaties]] · [[minderheidsbelangen]] · [[integrale-consolidatie]] · [[evenredige-consolidatie]] · [[belangenpercentage]] · 
## Voortkomend uit

- **Taken**: 1.4.taak.1
- **Kenniselementen**: 1.4.I.D, 1.4.I.B, 1.4.I.F
