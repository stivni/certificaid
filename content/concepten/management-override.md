---
title: Doorbreking door management (management override)
tags:
- concept
- begrip
- po-1-7
linked_anchors:
- 1.7.III
- 1.7.III.B
programmaonderdelen:
- '1.7'
confidence: grounded
node_type: begrip
status: seed
schema_version: '1.6'
gegenereerd_uit: data/concepten/records/management-override.json
gegenereerd_op: '2026-05-18'
---
# Doorbreking door management (management override) ⚖️

Management override is een centrale inherente beperking van interne controle: zelfs het beste systeem kan door dagelijks bestuur worden omzeild — facturen buiten de procedure goedgekeurd, einde-jaars-boekingen zonder onderbouwing, ad-hoc-betalingen via privé-account. Voor de stagiair-auditor is dit een verplichte fraude-risicofactor bij elke audit (ISA 240): hij moet altijd alert zijn dat management de IC kan doorbreken, niet vermoeden dat het zonder bewijs is gebeurd. Examen-vragen testen vooral het herkennen van management override als oorzaak waarom IC nooit absoluut werkt.

> [!summary] Korte inhoud
> Management override is het bewust omzeilen van bestaande interne controle door personen met voldoende gezag (bestuurder, CFO, eigenaar-bestuurder), waarbij verplichte autorisaties, scheidingen of beoordelingen worden genegeerd.

> [!info] Behoort tot: [[interne-controle]]

Management override is het bewust omzeilen van bestaande interne controle door personen met voldoende gezag (bestuurder, CFO, eigenaar-bestuurder), waarbij verplichte autorisaties, scheidingen of beoordelingen worden genegeerd. Hierdoor verliest IC haar werking voor de specifieke transactie of beslissing — een inherente beperking die door geen enkel systeem volledig wegneembaar is.

_Bron: ITAA KMO-controlenorm Bijlage 1 — 'doorbreken van het systeem'_


## In de praktijk

- Bij audit van een KMO is management override extra waarschijnlijk wegens kleine teams en dominante eigenaar-bestuurder. Vaste fraud-procedure: random sample journal entries einde jaar.
- Bij IC-advies aan cliënt: bouw ALTIJD een compenserende control in waar één persoon te veel macht heeft (bv. tweede-handtekening RvB voor betalingen > drempel).

## Valkuilen

> [!warning]- Aannemen dat 'management is integer dus zal niet override doen'
> ⚠️ Aannemen dat 'management is integer dus zal niet override doen'. Audit-standaarden (ISA 240) vereisen dat je het risico AANNEEMT en compenserende procedures uitvoert — los van persoonlijke perceptie van integriteit. 🤖


> [!warning]- Management override verwarren met functiescheidingsfout
> ⚠️ Management override verwarren met functiescheidingsfout. Override = bestaande IC bewust omzeild door iemand met gezag; functiescheidingsfout = onvolledig ontworpen IC. Verschil is wie de oorzaak draagt — beleid versus ontwerp. 🤖



## Zie ook

- **Getriggerd door**: [[fraude]]

## Voorbeelden

Bij Yperse Werkplaats BV is de procedure dat alle aankoopfacturen > € 25.000 dubbel getekend worden. Eigenaar-bestuurder Wim Vermeulen tekent in december alleen een factuur van € 80.000 voor 'consultancy' van een vriend en boekt ze in 20X3. Klassiek management-override-rood-signaal: substantieve bedragen einde jaar, vriendschapsrelatie, ontbrekende dubbele paraaf, vage prestatie-omschrijving.

## Bronnen

[^1]: `ITAA-norm-kmo-controlenorm__sec_bijlage-1-definities_part3`
[^2]: `ISA-315-herzien-2019__sec_bijlage-3`
