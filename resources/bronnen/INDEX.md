# Bronnen-index

Auto-gegenereerd door `tools/lib/bronnen_index.py`. **Niet handmatig editen** — wijzigingen worden bij de eerstvolgende rebuild overschreven. Voor de machine-leesbare versie zie `data/bronnen-index.json`.

**Trust-statussen** (zie ADR-005 §5): `trusted` = klaar voor RAG-index; `unreviewed` = nog niet beoordeeld; `needs-rework` = ETL-fix vereist; `rejected` = bron afgekeurd.

## Overzicht

| Type | Totaal | Trusted | Unreviewed | Needs-rework | Rejected | Unknown |
|---|---|---|---|---|---|---|
| Wetteksten | 133 | 103 | — | 25 | 5 | — |
| Normen | 19 | 4 | — | 14 | 1 | — |
| Adviezen | 436 | 422 | — | 14 | — | — |
| **Totaal** | **588** | 529 | — | 53 | 6 | — |

## Wetteksten (133)

| Bestand | Trust | L1 | L2 | Confirmed-by | Titel |
|---|---|---|---|---|---|
| `BW-boek1-algemene-bepalingen.md` | ❌ rejected | — | rejected | subagent-sonnet-4-6 | Burgerlijk Wetboek — Boek 1 — Algemene bepalingen |
| `KB-21-10-2018.md` | ❌ rejected | — | rejected | subagent-sonnet-4-6 | Koninklijk besluit van 21 oktober 2018 houdende de boekhoudkundige verplichtingen van o… |
| `WBTW-KB22jun2020-e-notariaat.md` | ❌ rejected | — | rejected | subagent-sonnet-4-6 | K.B. 22 juni 2020 tot uitvoering van art. 93ter WBTW, art. 412bis en 433–435 WIB92 en a… |
| `WER-Boek-VIII-normalisatie.md` | ❌ rejected | — | rejected | subagent-sonnet-4-6 | WER Boek VIII — Kwaliteit van producten en diensten (boekhoudnormen) |
| `Wet-betalingsachterstand-2002.md` | ❌ rejected | — | rejected | subagent-sonnet-4-6 | Wet 2 augustus 2002 betreffende de bestrijding van de betalingsachterstand bij handelst… |
| `Almanak-BTW-2026.md` | ⚠️ needs-rework | — | needs-rework | subagent-sonnet-4-6 | Almanak BTW 2026 — ITAA / Larcier-Intersentia |
| `Almanak-VenB-2026.md` | ⚠️ needs-rework | — | needs-rework | subagent-sonnet-4-6 | Almanak Vennootschapsbelasting 2026 — ITAA / Larcier-Intersentia |
| `Belastingalmanak-2026.md` | ⚠️ needs-rework | — | needs-rework | subagent-sonnet-4-6 | Belastingalmanak 2026 — ITAA / Larcier-Intersentia |
| `belastinggids-aclvb-2025.md` | ⚠️ needs-rework | — | needs-rework | subagent-sonnet-4-6 | Belastinggids 2025 — ACLVB |
| `BTW-richtlijn-2006-112.md` | ⚠️ needs-rework | — | needs-rework | subagent-sonnet-4-6 | Richtlijn 2006/112/EG van de Raad betreffende het gemeenschappelijke stelsel van belast… |
| `Cijfers-Tarieven-2026.md` | ⚠️ needs-rework | — | needs-rework | subagent-sonnet-4-6 | Cijfers & tarieven 2026 — ITAA |
| `EU-Richtlijn-witwassen-2018-1673.md` | ⚠️ needs-rework | — | needs-rework | subagent-sonnet-4-6 | Richtlijn (EU) 2018/1673 van het Europees Parlement en de Raad van 23 oktober 2018 inza… |
| `fiscaal-memento-2025.md` | ⚠️ needs-rework | — | needs-rework | subagent-sonnet-4-6 | Fiscaal Memento 2025 — FOD Financiën (editie 12/2024) |
| `MAR-vzw.md` | ⚠️ needs-rework | — | needs-rework | subagent-sonnet-4-6 | Minimum Algemeen Rekeningstelsel voor verenigingen en stichtingen (MAR VZW) |
| `Registratierechten-federaal.md` | ⚠️ needs-rework | — | needs-rework | subagent-sonnet-4-6 | Wetboek der Registratie-, Hypotheek- en Griffierechten — federaal |
| `toelichting-PB-2025-deel1-VG.md` | ⚠️ needs-rework | — | needs-rework | subagent-sonnet-4-6 | Toelichting bij de aangifte in de personenbelasting — AJ 2025 — Vlaams Gewest |
| `toelichting-PB-2025-deel2.md` | ⚠️ needs-rework | — | needs-rework | subagent-sonnet-4-6 | Toelichting bij de aangifte in de personenbelasting — AJ 2025 — Deel 2 |
| `toelichting-VenB-2025.md` | ⚠️ needs-rework | — | needs-rework | subagent-sonnet-4-6 | Toelichting bij de aangifte in de vennootschapsbelasting — AJ 2025 |
| `VCF.md` | ⚠️ needs-rework | — | needs-rework | subagent-sonnet-4-6 | Decreet 13 december 2013 houdende de Vlaamse Codex Fiscaliteit (VCF) |
| `WBTW-KB10-uitoefening-keuzen.md` | ⚠️ needs-rework | — | needs-rework | subagent-sonnet-4-6 | K.B. nr. 10 van 29 december 1992, met betrekking tot de uitoefeningsmodaliteiten van de… |
| `WBTW-KB20-tarieven.md` | ⚠️ needs-rework | — | needs-rework | subagent-sonnet-4-6 | K.B. nr. 20 van 20 juli 1970, tot vaststelling van de tarieven van de belasting over de… |
| `WBTW-KB24-voldoening-bijzondere.md` | ⚠️ needs-rework | — | needs-rework | subagent-sonnet-4-6 | K.B. nr. 24 van 29 december 1992, met betrekking tot de voldoening van de belasting ove… |
| `WBTW-KB39-regeling-93duodecies.md` | ⚠️ needs-rework | — | needs-rework | subagent-sonnet-4-6 | K.B. nr. 39 van 17 oktober 1980, tot regeling van de toepassingsmodaliteiten van artike… |
| `WBTW-KB4-teruggaven.md` | ⚠️ needs-rework | — | needs-rework | subagent-sonnet-4-6 | K.B. nr. 4 van 29 december 1969, met betrekking tot de teruggaven inzake belasting over… |
| `WBTW-KB41-proportionele-geldboeten.md` | ⚠️ needs-rework | — | needs-rework | subagent-sonnet-4-6 | K.B. nr. 41 van 30 januari 1987, tot vaststelling van het bedrag van de proportionele f… |
| `WBTW-KB44-geldboeten.md` | ⚠️ needs-rework | — | needs-rework | subagent-sonnet-4-6 | K.B. nr. 44 van 9 juli 2012, tot vaststelling van het bedrag van de niet-proportionele … |
| `WBTW-KB50-intracommunautaire-opgave.md` | ⚠️ needs-rework | — | needs-rework | subagent-sonnet-4-6 | K.B. nr. 50 van 11 december 2019, met betrekking tot de btw-opgave van de intracommunau… |
| `WBTW-KB7-invoer.md` | ⚠️ needs-rework | — | needs-rework | subagent-sonnet-4-6 | K.B. nr. 7 van 29 december 1992, met betrekking tot de invoer van goederen voor de toep… |
| `WBTW-MB28okt2009-model-berichten-93ter.md` | ⚠️ needs-rework | — | needs-rework | subagent-sonnet-4-6 | M.B. van 28 oktober 2009, tot bepaling van het model der berichten en kennisgevingen al… |
| `WBTW-MB29apr2024-certificatie-kassasysteem.md` | ⚠️ needs-rework | — | needs-rework | subagent-sonnet-4-6 | M.B. van 29 april 2024, betreffende de technische aspecten ten aanzien van de certifica… |
| `aangifte-PB-2025-bezoldigingen.md` | ✅ trusted | — | trusted | subagent-sonnet-4-6 | aangifte-PB-2025-bezoldigingen |
| `aangifte-PB-2025-stopzetting.md` | ✅ trusted | — | trusted | subagent-sonnet-4-6 | aangifte-PB-2025-stopzetting |
| `Antiwitwaswet-2017.md` | ✅ trusted | — | trusted | subagent-sonnet-4-6 | Wet 18 september 2017 tot voorkoming van het witwassen van geld en de financiering van … |
| `AVG-wet-2018.md` | ✅ trusted | — | trusted | subagent-sonnet-4-6 | Wet 30 juli 2018 betreffende de bescherming van natuurlijke personen met betrekking tot… |
| `Brusselse-Codex-Fiscale-Procedure.md` | ✅ trusted | — | trusted | subagent-sonnet-4-6 | Ordonnantie 6 maart 2019 betreffende de Brusselse Codex Fiscale Procedure |
| `BTW-dertiende-richtlijn-1986.md` | ✅ trusted | — | trusted | subagent-sonnet-4-6 | Dertiende Richtlijn 86/560/EEG van de Raad inzake de teruggaaf van btw aan niet in de G… |
| `BTW-teruggaaf-richtlijn-2008-9.md` | ✅ trusted | — | trusted | subagent-sonnet-4-6 | Richtlijn 2008/9/EG van de Raad tot vaststelling van nadere voorschriften voor de in Ri… |
| `BTW-uitvoeringsverordening-282-2011.md` | ✅ trusted | — | trusted | subagent-sonnet-4-6 | Uitvoeringsverordening (EU) nr. 282/2011 van de Raad houdende maatregelen ter uitvoerin… |
| `BW-boek2-relatievermogensrecht.md` | ✅ trusted | — | trusted | subagent-sonnet-4-6 | Burgerlijk Wetboek — Boek 2 — Relatievermogensrecht |
| `BW-boek3-goederen.md` | ✅ trusted | — | trusted | subagent-sonnet-4-6 | Burgerlijk Wetboek — Boek 3 — Goederen |
| `BW-boek4-nalatenschappen.md` | ✅ trusted | — | trusted | subagent-sonnet-4-6 | Burgerlijk Wetboek — Boek 4 — Nalatenschappen, schenkingen en testamenten |
| `BW-boek5-verbintenissen.md` | ✅ trusted | — | trusted | subagent-sonnet-4-6 | Burgerlijk Wetboek — Boek 5 — Verbintenissen |
| `BW-boek8-bewijs.md` | ✅ trusted | — | trusted | subagent-sonnet-4-6 | Burgerlijk Wetboek — Boek 8 — Bewijs |
| `BW-boek9-zekerheden.md` | ✅ trusted | — | trusted | subagent-sonnet-4-6 | Burgerlijk Wetboek — Boek 9 — Zekerheden |
| `Decr-Waals-Directe-Belastingen.md` | ✅ trusted | — | trusted | subagent-sonnet-4-6 | Decreet 6 mei 1999 betreffende de vestiging, de invordering en de geschillen inzake de … |
| `EU-AVG-Verordening-2016-679.md` | ✅ trusted | — | trusted | subagent-sonnet-4-6 | Verordening (EU) 2016/679 van het Europees Parlement en de Raad van 27 april 2016 betre… |
| `EU-IFRS-verordening-1606-2002.md` | ✅ trusted | — | trusted | subagent-sonnet-4-6 | Verordening (EG) nr. 1606/2002 van het Europees Parlement en de Raad van 19 juli 2002 b… |
| `EU-Richtlijn-fusie-2009-133.md` | ✅ trusted | — | trusted | subagent-sonnet-4-6 | Richtlijn 2009/133/EG van de Raad van 19 oktober 2009 betreffende de gemeenschappelijke… |
| `EU-Richtlijn-interest-royalties-2003-49.md` | ✅ trusted | — | trusted | subagent-sonnet-4-6 | Richtlijn 2003/49/EG van de Raad van 3 juni 2003 betreffende een gemeenschappelijke bel… |
| `EU-Richtlijn-moeder-dochter-2011-96.md` | ✅ trusted | — | trusted | subagent-sonnet-4-6 | Richtlijn 2011/96/EU van de Raad van 30 november 2011 betreffende de gemeenschappelijke… |
| `KB-1998-plichtenleer.md` | ✅ trusted | — | trusted | subagent-sonnet-4-6 | Koninklijk besluit van 1 maart 1998 tot vaststelling van het reglement van plichtenleer… |
| `KB-voorafgaande-beslissingen-art22-2003.md` | ✅ trusted | — | trusted | subagent-sonnet-4-6 | K.B. 17 januari 2003 tot uitvoering van artikel 22, tweede lid, van de wet van 24 decem… |
| `KB-voorafgaande-beslissingen-art26-2003.md` | ✅ trusted | — | trusted | subagent-sonnet-4-6 | K.B. 30 januari 2003 tot uitvoering van artikel 26 van de wet van 24 december 2002 tot … |
| `KB-WIB92.md` | ✅ trusted | — | trusted | subagent-sonnet-4-6 | Koninklijk besluit tot uitvoering van het Wetboek van de Inkomstenbelastingen 1992 (KB/… |
| `KB-WVV-2019.md` | ✅ trusted | — | trusted | subagent-sonnet-4-6 | Koninklijk besluit van 29 april 2019 tot uitvoering van het Wetboek van vennootschappen… |
| `Klokkenluiderswet-2022.md` | ✅ trusted | — | trusted | subagent-sonnet-4-6 | Wet 28 november 2022 betreffende de bescherming van melders van inbreuken op het Unie- … |
| `MIGB-Brussel.md` | ✅ trusted | — | trusted | subagent-sonnet-4-6 | Wetboek van de met de inkomstenbelastingen gelijkgestelde belastingen — Brussels Hoofds… |
| `MIGB-Vlaanderen.md` | ✅ trusted | — | trusted | subagent-sonnet-4-6 | Wetboek van de met de inkomstenbelastingen gelijkgestelde belastingen — Vlaams Gewest |
| `MIGB-Wallonie.md` | ✅ trusted | — | trusted | subagent-sonnet-4-6 | Wetboek van de met de inkomstenbelastingen gelijkgestelde belastingen — Waals Gewest |
| `Oud-BW.md` | ✅ trusted | — | trusted | subagent-sonnet-4-6 | Burgerlijk Wetboek (oud, vóór hervormingen nieuwe Burgerlijk Wetboek 2019) |
| `Registratierechten-Brussel.md` | ✅ trusted | — | trusted | subagent-sonnet-4-6 | Wetboek der Registratie-, Hypotheek- en Griffierechten — Brussels Hoofdstedelijk Gewest |
| `Registratierechten-Waals.md` | ✅ trusted | — | trusted | subagent-sonnet-4-6 | Wetboek der Registratie-, Hypotheek- en Griffierechten — Waals Gewest |
| `Richtlijn-2013-34-EU.md` | ✅ trusted | — | trusted | subagent-sonnet-4-6 | Richtlijn 2013/34/EU van het Europees Parlement en de Raad van 26 juni 2013 betreffende… |
| `Strafwetboek-1867.md` | ✅ trusted | — | trusted | subagent-sonnet-4-6 | Strafwetboek 8 juni 1867 (Oud Strafwetboek) |
| `Strafwetboek2024-boek1.md` | ✅ trusted | — | trusted | subagent-sonnet-4-6 | Wetboek 29 februari 2024 Strafwetboek 2024 — Boek 1 |
| `Strafwetboek2024-boek2.md` | ✅ trusted | — | trusted | subagent-sonnet-4-6 | Wetboek 29 februari 2024 Strafwetboek 2024 — Boek 2 |
| `Successierechten-Brussel.md` | ✅ trusted | — | trusted | subagent-sonnet-4-6 | Wetboek der Successierechten — Brussels Hoofdstedelijk Gewest |
| `Successierechten-federaal.md` | ✅ trusted | — | trusted | subagent-sonnet-4-6 | Wetboek der Successierechten — federaal |
| `Successierechten-Waals.md` | ✅ trusted | — | trusted | subagent-sonnet-4-6 | Wetboek der Successierechten — Waals Gewest |
| `Verdrag-WABB.md` | ✅ trusted | — | trusted | subagent-sonnet-4-6 | Verdrag inzake wederzijdse administratieve bijstand in fiscale aangelegenheden (WABB/CM… |
| `WBTW-KB-GKS.md` | ✅ trusted | — | trusted | subagent-sonnet-4-6 | K.B. 30 december 2009 tot het bepalen van de definitie en de voorwaarden waaraan een ge… |
| `WBTW-KB01okt2013-certificatie-gks.md` | ✅ trusted | — | trusted | subagent-sonnet-4-6 | K.B. 1 oktober 2013 met betrekking tot de toepassingsmodaliteiten ten aanzien van de ce… |
| `WBTW-KB04apr2014-verificatie-vervoermiddelen.md` | ✅ trusted | — | trusted | subagent-sonnet-4-6 | K.B. van 4 april 2014, betreffende de verificatie van het regelmatig aanwezig zijn van … |
| `WBTW-KB07jun2007-uitvoering-84quinquies.md` | ✅ trusted | — | trusted | subagent-sonnet-4-6 | K.B. van 7 juni 2007, tot uitvoering van de artikelen 84quinquies tot 84decies van het … |
| `WBTW-KB1-voldoening.md` | ✅ trusted | — | trusted | subagent-sonnet-4-6 | K.B. nr. 1, 29 december 1992, met betrekking tot de regeling voor de voldoening van de … |
| `WBTW-KB11-verleggen-maatstaf.md` | ✅ trusted | — | trusted | subagent-sonnet-4-6 | K.B. nr. 11 van 29 december 1992, met betrekking tot de toepassing van de belasting ove… |
| `WBTW-KB13-tabaksfabricaten.md` | ✅ trusted | — | trusted | subagent-sonnet-4-6 | K.B. nr. 13 van 29 december 1992, met betrekking tot de regeling voor tabaksfabricaten … |
| `WBTW-KB14-vervreemdingen-gebouwen.md` | ✅ trusted | — | trusted | subagent-sonnet-4-6 | K.B. nr. 14 van 3 juni 1970, met betrekking tot de vervreemdingen van gebouwen, gedeelt… |
| `WBTW-KB15-schatting-onroerende.md` | ✅ trusted | — | trusted | subagent-sonnet-4-6 | K.B. nr. 15 van 3 juni 1970, tot regeling van de schattings- procedure waarin artikel 5… |
| `WBTW-KB16-vismijn.md` | ✅ trusted | — | trusted | subagent-sonnet-4-6 | K.B. nr. 16 van 3 juni 1970, met betrekking tot de toepassing van de belasting over de … |
| `WBTW-KB18-uitvoer-vrijstellingen.md` | ✅ trusted | — | trusted | subagent-sonnet-4-6 | K.B. nr. 18 van 29 december 1992, met betrekking tot de vrijstellingen ten aanzien van … |
| `WBTW-KB19-kleine-ondernemingen.md` | ✅ trusted | — | trusted | subagent-sonnet-4-6 | K.B. nr. 19, 15 december 2024, met betrekking tot de vrijstellingsregeling van belastin… |
| `WBTW-KB2-forfaitaire.md` | ✅ trusted | — | trusted | subagent-sonnet-4-6 | K.B. nr. 2, 19 december 2018, met betrekking tot de forfaitaire regeling inzake btw |
| `WBTW-KB22-landbouwondernemers.md` | ✅ trusted | — | trusted | subagent-sonnet-4-6 | K.B. nr. 22 van 15 september 1970, met betrekking tot de biezondere regeling voor landb… |
| `WBTW-KB23-jaarlijkse-lijst.md` | ✅ trusted | — | trusted | subagent-sonnet-4-6 | K.B. nr. 23 van 9 december 2009, met betrekking tot de jaarlijkse lijst van de BTW-bela… |
| `WBTW-KB27-vlees-slachtdieren.md` | ✅ trusted | — | trusted | subagent-sonnet-4-6 | K.B. nr. 27 van 26 juni 1973, met betrekking tot de regeling voor de voldoening van de … |
| `WBTW-KB29aug2019-registers.md` | ✅ trusted | — | trusted | subagent-sonnet-4-6 | K.B. van 29 augustus 2019, tot uitvoering van artikel 85, § 2, derde lid van het Wetboe… |
| `WBTW-KB2bis-cafehouders.md` | ✅ trusted | — | trusted | subagent-sonnet-4-6 | K.B. nr. 2bis, 15 mei 2022, tot vaststelling van de forfaitaire grondslagen van aanslag… |
| `WBTW-KB3-aftrekken.md` | ✅ trusted | — | trusted | subagent-sonnet-4-6 | K.B. nr. 3 van 10 december 1969, met betrekking tot de aftrekken voor de toepassing van… |
| `WBTW-KB30-financieringshuur.md` | ✅ trusted | — | trusted | subagent-sonnet-4-6 | K.B. nr. 30 van 29 december 1992, met betrekking tot de toepassing van de belasting ove… |
| `WBTW-KB31-niet-gevestigd.md` | ✅ trusted | — | trusted | subagent-sonnet-4-6 | K.B. nr. 31 van 2 april 2002, met betrekking tot de toepassings- modaliteiten van de be… |
| `WBTW-KB35-reisbureaus.md` | ✅ trusted | — | trusted | subagent-sonnet-4-6 | K.B. nr. 35 van 28 december 1999, tot invoering van een forfaitaire maatstaf van heffin… |
| `WBTW-KB45-vrijstelling-diplomaten.md` | ✅ trusted | — | trusted | subagent-sonnet-4-6 | K.B. nr. 45 van 14 april 1993, met betrekking tot de vrijstelling op het stuk van de be… |
| `WBTW-KB46-intracommunautaire-aangifte.md` | ✅ trusted | — | trusted | subagent-sonnet-4-6 | K.B. nr. 46 van 29 december 1992, tot regeling van de aangifte van de intracommunautair… |
| `WBTW-KB47-controle-vervoermiddelen-1996.md` | ✅ trusted | — | trusted | subagent-sonnet-4-6 | K.B. nr. 47 van 25 februari 1996, tot regeling van de controle van de voldoening van de… |
| `WBTW-KB48-levering-vervoermiddelen.md` | ✅ trusted | — | trusted | subagent-sonnet-4-6 | K.B. nr. 48 van 29 december 1992, met betrekking tot de levering van vervoermiddelen in… |
| `WBTW-KB51-accijnsproducten.md` | ✅ trusted | — | trusted | subagent-sonnet-4-6 | K.B. nr. 51 van 14 april 1993, met betrekking tot de vereenvoudigingsregeling voor intr… |
| `WBTW-KB52-intracommunautaire-vrijstellingen.md` | ✅ trusted | — | trusted | subagent-sonnet-4-6 | K.B. nr. 52 van 11 december 2019, met betrekking tot de bewijsregeling inzake de vrijst… |
| `WBTW-KB53-winstmarge-tweedehands.md` | ✅ trusted | — | trusted | subagent-sonnet-4-6 | K.B. nr. 53 van 23 december 1994, met betrekking tot de bijzondere regeling van belasti… |
| `WBTW-KB54-entrepot.md` | ✅ trusted | — | trusted | subagent-sonnet-4-6 | K.B. nr. 54, 21 december 2023, met betrekking tot de andere regeling van entrepot dan d… |
| `WBTW-KB55-btw-eenheid.md` | ✅ trusted | — | trusted | subagent-sonnet-4-6 | K.B. nr. 55 van 9 maart 2007, met betrekking tot de regeling voor belastingplichtingen … |
| `WBTW-KB56-teruggaaf.md` | ✅ trusted | — | trusted | subagent-sonnet-4-6 | K.B. nr. 56, 10 april 2022, met betrekking tot de teruggaaf inzake btw aan belastingpli… |
| `WBTW-KB57-plaats-diensten.md` | ✅ trusted | — | trusted | subagent-sonnet-4-6 | K.B. nr. 57, van 31.10.2017 met betrekking tot de plaats van diensten in functie van hu… |
| `WBTW-KB58-mededeling-pas-opgerichte.md` | ✅ trusted | — | trusted | subagent-sonnet-4-6 | K.B. nr. 58 van 28 mei 2019, met betrekking tot de mededeling van de inlichtingen inzak… |
| `WBTW-KB59-handelsgeschenken.md` | ✅ trusted | — | trusted | subagent-sonnet-4-6 | K.B. nr. 59, 18 mei 2020, met betrekking tot de onttrekking van handelsgeschenken van g… |
| `WBTW-KB6-internationaal-vervoer.md` | ✅ trusted | — | trusted | subagent-sonnet-4-6 | K.B. nr. 6 van 27 december 1977, met betrekking tot de vrijstellingen ten aanzien van i… |
| `WBTW-KB8-afronding.md` | ✅ trusted | — | trusted | subagent-sonnet-4-6 | K.B. nr. 8 van 12 maart 1970, tot vaststelling van de wijze van afronding van de versch… |
| `WBTW-KB9-ambtelijke-aanslag.md` | ✅ trusted | — | trusted | subagent-sonnet-4-6 | K.B. nr. 9 van 12 december 1970, met betrekking tot de ambtelijke aanslag inzake belast… |
| `WBTW-MB-compilatie.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | Ministeriële besluiten inzake belasting over de toegevoegde waarde (compilatie Fisconet… |
| `WBTW-MB-dagboek-ontvangsten-2023.md` | ✅ trusted | — | trusted | subagent-sonnet-4-6 | M.B. 17 maart 2023 betreffende de vaststelling van de modaliteiten voor het bijhouden v… |
| `WBTW-MB1-aftrekregeling.md` | ✅ trusted | — | trusted | subagent-sonnet-4-6 | M.B. nr. 1 van 2 september 1980, met betrekking tot de aftrekregeling voor de toepassin… |
| `WBTW-MB11-facturen-oprichting-gebouwen.md` | ✅ trusted | — | trusted | subagent-sonnet-4-6 | M.B. nr. 11 van 3 november 1972, met betrekking tot de controle op de toepassing van de… |
| `WBTW-MB12-weegtoestellen-slachthuizen.md` | ✅ trusted | — | trusted | subagent-sonnet-4-6 | M.B. nr. 12 van 28 augustus 1973, met betrekking tot de automatische weegtoestellen te … |
| `WBTW-MB13-hypotheek-verplichtingen.md` | ✅ trusted | — | trusted | subagent-sonnet-4-6 | M.B. nr. 13 van 4 maart 1993, met betrekking tot de verplichtingen waartoe een belastin… |
| `WBTW-MB16jul2019-beroepscommissie.md` | ✅ trusted | — | trusted | subagent-sonnet-4-6 | M.B. van 16 juli 2019, tot aanduiding van de ambtenaren die in de functie van adviseur-… |
| `WBTW-MB2-teruggaven.md` | ✅ trusted | — | trusted | subagent-sonnet-4-6 | M.B. nr. 2 van 21 december 2010, met betrekking tot de teruggaven inzake belasting over… |
| `WBTW-MB20dec2001-diensten-indiening-documenten.md` | ✅ trusted | — | trusted | subagent-sonnet-4-6 | M.B. van 20 december 2001, met betrekking tot de diensten waar de documenten bedoeld in… |
| `WBTW-MB23jun2005-delegatie-samenwerking.md` | ✅ trusted | — | trusted | subagent-sonnet-4-6 | M.B. van 23 juni 2005, met betrekking tot de delegatie van de bevoegde autoriteit inzak… |
| `WBTW-MB26feb2007-elektronische-notificaties.md` | ✅ trusted | — | trusted | subagent-sonnet-4-6 | M.B. van 26 februari 2007, met betrekking tot de aanduiding van de dienst bevoegd voor … |
| `WBTW-MB29aug2006-ambtenaar-62bis.md` | ✅ trusted | — | trusted | subagent-sonnet-4-6 | M.B. van 29 augustus 2006, tot aanduiding van de ambtenaar bedoeld in artikel 62bis van… |
| `WBTW-MB6-uitstel-invoer.md` | ✅ trusted | — | trusted | subagent-sonnet-4-6 | M.B. nr. 6 van 4 maart 1993, waarbij uitstel wordt verleend voor de voldoening van de t… |
| `WBTW.md` | ✅ trusted | — | trusted | subagent-sonnet-4-6 | Wet 3 juli 1969 tot invoering van het Wetboek van de belasting over de toegevoegde waar… |
| `WDRT.md` | ✅ trusted | — | trusted | subagent-sonnet-4-6 | Wetboek Diverse Rechten en Taksen |
| `WER.md` | ✅ trusted | — | trusted | subagent-sonnet-4-6 | Wetboek van Economisch Recht |
| `Wet-arbeidsovereenkomsten-1978.md` | ✅ trusted | — | trusted | subagent-sonnet-4-6 | Wet 3 juli 1978 betreffende de arbeidsovereenkomsten |
| `Wet-beroepskwalificaties-2008.md` | ✅ trusted | — | trusted | subagent-sonnet-4-6 | Wet 12 februari 2008 tot instelling van een nieuw algemeen kader voor de erkenning van … |
| `Wet-ITAA-2019.md` | ✅ trusted | — | trusted | subagent-sonnet-4-6 | Wet 17 maart 2019 tot oprichting van het Instituut van de Belastingadviseurs en de Acco… |
| `Wet-verzekeringen-2014.md` | ✅ trusted | — | trusted | subagent-sonnet-4-6 | Wet 4 april 2014 betreffende de verzekeringen |
| `Wet-voorafgaande-beslissingen-2002.md` | ✅ trusted | — | trusted | subagent-sonnet-4-6 | Wet 24 december 2002 tot wijziging van de vennootschapsregeling inzake inkomstenbelasti… |
| `Wetboek-Invordering.md` | ✅ trusted | — | trusted | subagent-sonnet-4-6 | Wetboek van de minnelijke en gedwongen invordering van fiscale en niet-fiscale schuldvo… |
| `WIB92.md` | ✅ trusted | — | trusted | subagent-sonnet-4-6 | WIB92 |
| `WVV.md` | ✅ trusted | — | trusted | subagent-sonnet-4-6 | Wetboek van vennootschappen en verenigingen 23/03/2019 |
| `X-oeso-model-verdrag.md` | ✅ trusted | — | trusted | subagent-sonnet-4-6 | X-oeso-model-verdrag |

## Normen (19)

| Bestand | Trust | L1 | L2 | Confirmed-by | Titel |
|---|---|---|---|---|---|
| `ITAA-deontologische-code.md` | ❌ rejected | warn | rejected | subagent-sonnet-4-6 | ITAA-deontologische-code |
| `IESBA-code-of-ethics-2024.md` | ⚠️ needs-rework | — | needs-rework | subagent-sonnet-4-6 | IESBA-code-of-ethics-2024 |
| `ITAA-norm-aww-geconsolideerd.md` | ⚠️ needs-rework | pass | needs-rework | subagent-sonnet-4-6 | ITAA-norm-aww-geconsolideerd |
| `ITAA-norm-aww-reglement.md` | ⚠️ needs-rework | pass | needs-rework | subagent-sonnet-4-6 | ITAA-norm-aww-reglement |
| `ITAA-norm-aww-richtlijn-bibf.md` | ⚠️ needs-rework | pass | needs-rework | subagent-sonnet-4-6 | ITAA-norm-aww-richtlijn-bibf |
| `ITAA-norm-domiciliering.md` | ⚠️ needs-rework | pass | needs-rework | subagent-sonnet-4-6 | ITAA-norm-domiciliering |
| `ITAA-norm-effectennorm.md` | ⚠️ needs-rework | pass | needs-rework | subagent-sonnet-4-6 | ITAA-norm-effectennorm |
| `ITAA-norm-gedragslijnen-relaties-IBR.md` | ⚠️ needs-rework | pass | needs-rework | subagent-sonnet-4-6 | ITAA-norm-gedragslijnen-relaties-IBR |
| `ITAA-norm-intern-kwaliteitsmanagement.md` | ⚠️ needs-rework | pass | needs-rework | subagent-sonnet-4-6 | ITAA-norm-intern-kwaliteitsmanagement |
| `ITAA-norm-kmo-controlenorm.md` | ⚠️ needs-rework | warn | needs-rework | subagent-sonnet-4-6 | ITAA-norm-kmo-controlenorm |
| `ITAA-norm-omzetting-vennootschap.md` | ⚠️ needs-rework | pass | needs-rework | subagent-sonnet-4-6 | ITAA-norm-omzetting-vennootschap |
| `ITAA-norm-ontbinding-vereffening.md` | ⚠️ needs-rework | pass | needs-rework | subagent-sonnet-4-6 | ITAA-norm-ontbinding-vereffening |
| `ITAA-norm-opdrachtbrief.md` | ⚠️ needs-rework | pass | needs-rework | subagent-sonnet-4-6 | ITAA-norm-opdrachtbrief |
| `ITAA-norm-permanente-vorming.md` | ⚠️ needs-rework | pass | needs-rework | subagent-sonnet-4-6 | ITAA-norm-permanente-vorming |
| `ITAA-norm-samenstellingsopdrachten-isrs4410.md` | ⚠️ needs-rework | pass | needs-rework | subagent-sonnet-4-6 | ITAA-norm-samenstellingsopdrachten-isrs4410 |
| `ITAA-deontologie-beroepsgeheim.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | ITAA-deontologie-beroepsgeheim |
| `ITAA-norm-algemene-controlenorm.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | ITAA-norm-algemene-controlenorm |
| `ITAA-norm-aww-procedurereglement.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | ITAA-norm-aww-procedurereglement |
| `ITAA-norm-fusie-splitsing.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | ITAA-norm-fusie-splitsing |

## Adviezen (436)

| Bestand | Trust | L1 | L2 | Confirmed-by | Titel |
|---|---|---|---|---|---|
| `CBN-0007-02-interne-en-externe-jaarrekening-begrippen.md` | ⚠️ needs-rework | pass | needs-rework | subagent-sonnet-4-6 | CBN-advies 7/2 |
| `CBN-0100-vragen-en-antwoorden-over-de-sociale-balans.md` | ⚠️ needs-rework | warn | needs-rework | subagent-sonnet-4-6 | CBN-advies S100 |
| `CBN-0126-05-vervaardigingsprijs.md` | ⚠️ needs-rework | pass | needs-rework | subagent-sonnet-4-6 | CBN-advies 126/5 |
| `CBN-0139-08-uitgifte-van-obligaties-met-inschrijvingsrechten-die-in-aandelen-converteerbaar-of.md` | ⚠️ needs-rework | pass | needs-rework | subagent-sonnet-4-6 | CBN-advies 139/8 |
| `CBN-0147-02-inresultaatneming-van-het-actuariele-rendement-van-vastrentende-effecten.md` | ⚠️ needs-rework | pass | needs-rework | subagent-sonnet-4-6 | CBN-advies 147/2 |
| `CBN-0152-01-boekingen-van-deviezenverrichtingen-en-verwerking-van-tegoeden-en-verplichtingen-in.md` | ⚠️ needs-rework | pass | needs-rework | subagent-sonnet-4-6 | CBN-advies 152/1 |
| `CBN-0166-02-verwerking-in-de-jaarrekening-van-bepaalde-verrichtingen-als-bedoeld-in-artikel-677-van.md` | ⚠️ needs-rework | pass | needs-rework | subagent-sonnet-4-6 | CBN-advies 166/2 |
| `CBN-0167-02-boekhoudkundige-verwerking-van-dekkingsverrichtingen-en-gedekte-posities-in-aandelen.md` | ⚠️ needs-rework | pass | needs-rework | subagent-sonnet-4-6 | CBN-advies 167/2 |
| `CBN-0173-05-toelichting-bij-de-boekhoudkundige-verwerking-van-termijnwisselverrichtingen-tussen-de.md` | ⚠️ needs-rework | pass | needs-rework | subagent-sonnet-4-6 | CBN-advies 173/5 |
| `CBN-2009-03-boekhoudkundige-verwerking-van-kapitaalsubsidies-waarvan-de-toekenning-enof-de-uitbetaling.md` | ⚠️ needs-rework | pass | needs-rework | subagent-sonnet-4-6 | CBN-advies 2009/3 |
| `CBN-2009-09-boekhoudkundige-gevolgen-van-de-aanvaardingsplicht-inzake-afgedankte-elektrische-en.md` | ⚠️ needs-rework | warn | needs-rework | subagent-sonnet-4-6 | CBN-advies 2009/9 |
| `CBN-2022-15-belgische-bijkantoren-van-buitenlandse-vennootschappen-eigen-boekhoudkundige.md` | ⚠️ needs-rework | pass | needs-rework | subagent-sonnet-4-6 | CBN-advies 2022/15 |
| `CBN-2024-03-gevolgen-van-niet-uitgedrukte-meerwaarden-bij-de-ontbinding.md` | ⚠️ needs-rework | pass | needs-rework | subagent-sonnet-4-6 | CBN-advies 2024/03 |
| `CBN-2024-09-verslaggeving-bij-de-heropening-van-de-vereffening-van-de-vennootschappen.md` | ⚠️ needs-rework | pass | needs-rework | subagent-sonnet-4-6 | CBN-advies 2024/09 |
| `CBN-0003-01-tijdstip-waarop-de-aan-of-verkoop-van-een-onroerend-goed-in-de-boekhouding-dient.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 3/1 |
| `CBN-0003-02-niet-in-de-balans-opgenomen-rechten-en-verplichtingen-0.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 3/2 |
| `CBN-0003-03-advies-inzake-de-boekhoudkundige-verwerking-van-verrichtingen-van-tijdelijk.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 3/3 |
| `CBN-0004-01-vermeldingen-in-het-centralisatieboek.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 4/1 |
| `CBN-0004-02-de-inschrijvingin-de-boeken-begrip.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 4/2 |
| `CBN-0004-03-over-het-centraal-boek.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 4/3 |
| `CBN-0004-04-beginsel-van-het-dubbel-boekhouden.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 4/4 |
| `CBN-0007-03-boek-waarin-de-jaarrekening-en-de-inventarisstukken-worden-opgenomen-opname-van-de.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 7/3 |
| `CBN-0007-04-opmaken-van-de-inventaris.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 7/4 |
| `CBN-0012-01-toepassingsgebied-van-de-uitvoeringsbesluiten-bedoelde-ondernemingen.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 12/1 |
| `CBN-0012-02-toepassingsgebied-van-de-uitvoeringsbesluiten-boekjaar-waarop-de-criteria-van-toepassing.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 12/2 |
| `CBN-0012-03-toepassingsgebied-van-de-uitvoeringsbesluiten-gemiddeld-aantal-jaarlijks-tewerkgestelde.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 12/3 |
| `CBN-0012-04-omvangcriteria-berekening-op-geconsolideerde-basis.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 12/4 |
| `CBN-0014-01-adviesbevoegdheid.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 14/1 |
| `CBN-0016-01-toepassing-van-de-wet-op-financiele-instellingen-kredietinstellingen-die-onder-de.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 16/1 |
| `CBN-0100-01-opening-van-bijkomende-rekeningen.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies R100-1 |
| `CBN-0100-02-aanpassing-van-het-rekeningstelsel-van-de-onderneming.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies R100/2 |
| `CBN-0100-omzet-begrip.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 100 |
| `CBN-0100-verwerking-in-de-geconsolideerde-jaarrekening-van-de-vermogensbestanddelen-en-de.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies C100 |
| `CBN-0101-01-zakelijke-waarborgen-gesteld-voor-rekening-van-derden.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies R101/1 |
| `CBN-0101-02-aandelen-als-waarborg-van-de-goede-uitoefening-van-een-mandaat-als-bestuurder-of.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies R101/2 |
| `CBN-0102-01-uitgegeven-cheques-werking-van-rekening-559.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies R102/1 |
| `CBN-0102-02-overschrijvingsorders.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies R102/2 |
| `CBN-0102-03-te-innen-cheques-rekening-53.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies R102/3 |
| `CBN-0102-omzet-verkopen-cif-cost-insurance-freight.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 102 |
| `CBN-0102-overschakeling-op-de-euro-aspecten-in-verband-met-de-geconsolideerde-jaarrekening.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies C102 |
| `CBN-0103-01-effect-in-de-tijd-van-de-verlaging-van-de-vrijstellingscriteria.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies C103/1 |
| `CBN-0103-03-omzet-van-lijnagenten.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 103/3 |
| `CBN-0103-gefactureerde-nog-niet-ontvangen-voorschotten-en-vooruitbetalingen-rekening-46.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies R103 |
| `CBN-0103-omzet-tussenpersonen.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 103 |
| `CBN-0103-omzet-van-expediteurs.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 103/2 |
| `CBN-0104-01-openbaarmaking-van-een-geconsolideerde-jaarrekening-op-vrijwillige-basis-of-op-basis-van.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies C104/1 |
| `CBN-0105-01-compensatie-tussen-debet-en-creditsaldi-bij-eenzelfde-bankinstelling.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 105/1 |
| `CBN-0105-01-uitgestelde-belastingvoordelen-wegens-overdraagbare-verliezen.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies C105/1 |
| `CBN-0105-02-kosten-afgewenteld-op-of-gedragen-door-derden.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 105/2 |
| `CBN-0105-04-vergoeding-van-kredieturen-door-de-rsz.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 105/4 |
| `CBN-0105-05-aanrekening-van-vergoedingen-van-beheerders-of-leden-van-het-personeel-toegekend-door-0.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 105-5 |
| `CBN-0105-06-schade-en-schadeverzekering-andere-dan-kredietverzekering.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 105/6 |
| `CBN-0106-01-advies-horizontale-consolidatie-in-combinatie-met-administratiekantoren.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies C106/1 |
| `CBN-0106-03-verbintenissen-van-een-moedervennootschap-met-betrekking-tot-de-solvabiliteit-van-haar.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 106/3 |
| `CBN-0106-04-beding-van-eigendomsvoorbehoud-uitdrukkelijk-ontbindend-beding-boekhoudkundige-verwerking.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 106/4 |
| `CBN-0107-01-voorzieningen-voor-grote-herstellings-of-onderhoudswerken.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 107/1 |
| `CBN-0107-02-voorzieningen-voor-prijsschommelingen-voorzieningen-met-een-algemeen-karakter.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 107/2 |
| `CBN-0107-03-verplichtingen-voortvloeiend-uit-brugpensioen-0.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 107/3 bis |
| `CBN-0107-03-verplichtingen-voortvloeiend-uit-brugpensioen.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 107/3 |
| `CBN-0107-04-voorzieningen-voor-de-schulden-ten-opzichte-van-het-personeel-bij-sluiting-van-de.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 107/4 |
| `CBN-0107-05-devaluatie-van-de-belgische-frank.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 107/5 |
| `CBN-0107-06-waarborgen-verbonden-aan-de-verkoop-van-goederen-of-het-leveren-van-diensten.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 107/6 |
| `CBN-0107-07-risicos-en-verliezen-waarvan-de-waardering-aleatoir-is.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 107/7 |
| `CBN-0107-08-boekhoudkundige-verwerking-van-de-voorzieningen-voor-risicos-en-kosten.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 107/8 |
| `CBN-0107-09-vaststelling-van-het-bedrag-van-een-voorziening-voor-pensioenen-of-brugpensioenen.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 107/9 |
| `CBN-0107-11-opbrengsten-waarover-betwisting-bestaat-update.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 107/11 |
| `CBN-0107-12-pensioenvoorzieningen.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 107/12 |
| `CBN-0107-13-voorzieningen-voor-geindexeerde-pensioenen-en-brugpensioenen.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 107/13 |
| `CBN-0107-14-voorzieningen-voor-bezoldigingen-bij-volledige-of-gedeeltelijke-vrijstelling-van-te.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 107/14 |
| `CBN-0108-01-afwijkingen-van-de-bepalingen-van-het-kb-van-8-oktober-1976-procedure.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 108/1 |
| `CBN-0108-02-aanvragen-tot-afwijking-overzicht.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 108/2 |
| `CBN-0108-03-adviesbeleid-van-de-commissie-voor-boekhoudkundige-normen-ten-aanzien-van-individuele.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 108/3 |
| `CBN-0108-04-vermelding-door-een-investeringsmaatschappij-van-het-aandelenbezit-in-andere.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 108/4 |
| `CBN-0110-01-openbaarmaking-van-de-jaarrekening-mogelijkheid-tot-publikatie-van-de-jaarrekening-in.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 110/1 |
| `CBN-0110-02-stukken-die-tegelijk-met-de-jaarrekening-dienen-neergelegd-te-worden-artikel-80-venn-w.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 110/2 |
| `CBN-0110-03-openbaarmaking-van-de-jaarrekening-van-vennootschappen-die-niet-aan-het-kb-van-8-oktober.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 110/3 |
| `CBN-0110-05-opstelling-goedkeuring-en-openbaarmaking-van-de-jaarrekening.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 110/5 |
| `CBN-0110-09-jaarrekening-schema-van-de-balanscentrale-omvang-van-de-bedrijven.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 110/9 |
| `CBN-0111-01-bezoldigingen-toegekend-aan-bestuurders-en-commissarissen-bedoelde-bezoldigingen.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 111/1 |
| `CBN-0111-02-toepassing-van-de-uitzondering-waarin-punt-17-van-de-toelichting-voorziet.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 111/2 |
| `CBN-0112-02-ontoereikendheid-van-de-afschrijvingen-geboekt-voor-de-inwerkingtreding-van-het-koninklijk.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 112/2 |
| `CBN-0112-08-waarderingsregels.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 112/8 |
| `CBN-0112-progressieve-afschrijvingsmethode.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 112/5 |
| `CBN-0113-02-herwaarderingen-verricht-met-toepassing-van-de-wet-van-20-augustus-1947.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 113/2 |
| `CBN-0113-05-herwaardering-van-vaste-activa-voor-het-begin-van-het-boekjaar-dat-aanvangt-na-31-december.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 113/5 |
| `CBN-0113-06-herwaardering-van-afschrijfbare-activa-intercommunale-verenigingen-en-gemeentebedrijven.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 113/6 |
| `CBN-0114-01-verbonden-ondernemingen-ondernemingen-met-deelnemingsverhouding.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 114/1 |
| `CBN-0114-02-bezit-van-maatschappelijke-rechten-in-verbonden-ondernemingen-of-in-ondernemingen-waarmee.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 114/2 |
| `CBN-0114-03-resultaten-uit-verrichtingen-met-dochterondernemingen.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 114/3 |
| `CBN-0114-04-verwerking-in-de-jaarrekening-van-een-onderneming-van-verrichtingen-met-verbonden.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 114/4 |
| `CBN-0114-06-uitdrukking-van-verrichtingen-tussen-ondernemingen-uit-eenzelfde-groep.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 114/6 |
| `CBN-0114-07-condominium.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 114/7 |
| `CBN-0116-financiele-kortingen.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 116 |
| `CBN-0117-01-jaarrekening-in-belgische-frank-munt-waarin-de-jaarrekening-moet-worden-opgesteld.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 117/1 |
| `CBN-0117-02-munt-waarin-de-boekhouding-moet-worden-gevoerd-en-de-jaarrekening-opgesteld-de-commissie.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 117/2 |
| `CBN-0117-03-voeren-van-de-boekhouding-en-opstellen-van-de-jaarrekening-in-een-andere-munt-dan-de-euro.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 117/3 |
| `CBN-0120-01-het-begrip-financiele-instelling.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 120/1 |
| `CBN-0120-02-in-aanmerking-te-nemen-termijn-contractuele-termijn-of-nog-te-lopen-termijn.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 120/2 |
| `CBN-0120-03-waardering-van-liquide-middelen-bij-de-jaarafsluiting-criterium-voor-de-toerekening-aan.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 120/3 |
| `CBN-0120-04-overheidsfondsen.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 120/4 |
| `CBN-0120-05-coordinatiecentrum-financiele-instelling.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 120/5 |
| `CBN-0120-06-boeking-van-het-financiele-bedrijf-van-een-coordinatiecentrum-binnen-een-groep.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 120/6 |
| `CBN-0121-01-afname-van-het-kapitaal-van-de-uitgiftepremies-van-de-reserves-van-de-overgedragen-winst.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 121/1 |
| `CBN-0121-02-verlies-gedragen-door-vennoten-of-derden.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 121/2 |
| `CBN-0121-02-verlies-gedragen-door-vennoten.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 121/2 bis |
| `CBN-0121-03-mutaties-binnen-het-eigen-vermogen.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 121/3 |
| `CBN-0121-04-voorstelling-van-een-tabel-met-de-wijzigingen-in-het-eigen-vermogen-en-de-bestemming-van.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 121/4 |
| `CBN-0124-01-fusie-inbreng-van-een-onderdeel-van-een-onderneming-splitsing.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 124/1 |
| `CBN-0126-01-aanschaffingsprijs-bijkomende-kosten.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 126/1 |
| `CBN-0126-02-inbrengprijs.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 126/2 |
| `CBN-0126-03-vervaardigingsprijs-toerekening-van-creditrente.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 126/3 |
| `CBN-0126-04-vervaardigingsprijs-correctie-van-de-nederlandse-tekst-van-artikel-22-van-het-koninklijk.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 126/4 |
| `CBN-0126-06-individualisering-van-de-aanschaffingsprijs.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 126/6 |
| `CBN-0126-07-waardering-van-de-aanschaffingsprijs-van-de-voorraden-op-grond-van-de-verkoopprijs.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 126/7 |
| `CBN-0126-08-financiele-vaste-activa-waardering-aanschaffingswaarde-met-prijstoeslag.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 126/8 |
| `CBN-0126-12-boeking-van-uitzettingsvergoedingen-betaald-door-de-eigenaar-en-van-de-kost-van-werken-ten.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 126/12 |
| `CBN-0126-13-boekhoudkundige-verwerking-van-de-aankoop-het-bezit-en-de-realisatie-van-vvpr-strips.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 126/13 |
| `CBN-0126-15-aanpassing-van-de-aan-verkoopprijs-van-een-deelneming.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 126/15 |
| `CBN-0126-16-aanschaffingswaarde-van-de-aandelen-ontvangen-naar-aanleiding-van-een-in-het-buitenland.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 126/16 |
| `CBN-0126-18-aanschaffingswaarde-bij-inbreng-in-natura.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 126/18 |
| `CBN-0127-01-forfaitaire-waardeverminderingen-op-vorderingen.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 127/1 |
| `CBN-0127-02-waardevermindering-op-aandelen-voorziening-voor-risicos-verbonden-aan-niet-opgevraagd.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 127/2 |
| `CBN-0128-02-betwiste-fiscale-aanslag-0.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 128/2 |
| `CBN-0128-05-vrijstelling-investeringsreserves-controle-op-de-toepassing-van-het-boekhoudrecht.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 128/5 |
| `CBN-0128-07-andere-taksen-en-lasten-ten-laste-van-derden.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 128/7 |
| `CBN-0128-08-boeking-van-voordelen-van-alle-aard.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 128/8 |
| `CBN-0129-01-boeking-van-bonusaandelen.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 129/1 |
| `CBN-0130-01-verzekering-tegen-de-burgerrechtelijke-aansprakelijkheid-van-de-werkgever.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 130/1 |
| `CBN-0131-02-toevoegingen-en-onttrekkingen-boekhoudkundige-verwerking.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 131/2 |
| `CBN-0132-01-lifo-methode.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 132/1 |
| `CBN-0132-02-voorraden-waarvan-de-verkoopprijs-door-de-overheid-gewaarborgd-is.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 132/2 |
| `CBN-0132-04-termijnovereenkomsten-op-handelsgoederen.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 132/4 |
| `CBN-0132-05-rechten-tot-vertoning-van-films.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 132/5 |
| `CBN-0132-06-vooruitbetalingen.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 132/6 |
| `CBN-0132-07-boeking-en-waardering-van-voorraden.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 132/7 |
| `CBN-0133-02-uitkering-van-een-dividend-aan-een-verbonden-onderneming.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 133/2 |
| `CBN-0133-03-schulden-voortvloeiend-uit-de-bestemming-van-het-resultaat.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 133/3 |
| `CBN-0133-04-schulden-uit-de-resultaatbestemming-dividenduitkering-aan-een-onderneming-die-ten-minste.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 133/4 |
| `CBN-0134-01-verwerking-in-de-boekhouding-en-de-jaarrekening-van-de-belastingbesparing-ingevoerd-door.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 134/1 |
| `CBN-0134-02-belastingvrije-provisie-voor-sociaal-passief.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 134/2 |
| `CBN-0134-03-investeringsaftrek.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 134/3 |
| `CBN-0135-01-kosten-die-worden-gemaakt-bij-de-vervreemding-van-activa.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 135/1 |
| `CBN-0136-01-voorwaardelijke-obligaties.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 136/1 |
| `CBN-0137-01-klassering-van-de-vorderingen-bij-faillissement-van-de-schuldenaar.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 137/1 |
| `CBN-0137-03-schulden-op-meer-dan-een-jaar-prefinanciering-van-langlopende-leningen.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 137/3 |
| `CBN-0137-04-renteloze-vorderingen-schulden-en-vorderingen-schulden-met-een-abnormaal-lage-rente-op.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 137/4 |
| `CBN-0137-06-overdracht-van-schuldvordering-nominale-waarde-waardevermindering.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 137/6 |
| `CBN-0137-actualisering-van-vorderingen-en-schulden-op-korte-termijn-update.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 137/9 |
| `CBN-0137-vordering-wegens-levering-van-goederen-en-diensten-omgevormd-tot-renteloze-leningen-op.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 137/8 |
| `CBN-0137-vorderingen-en-schulden-waarvan-de-rente-uitsluitend-bestaat-uit-het-verschil-tussen-de.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 137/5 |
| `CBN-0138-05-software.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 138/5 |
| `CBN-0139-02-obligaties-met-warrant.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 139/2 |
| `CBN-0139-03-aandelen-met-warrant.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 139/3 |
| `CBN-0139-04-afgezonderde-warranten.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 139/4 |
| `CBN-0139-05-obligaties-met-warrant-0.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 139/5 |
| `CBN-0139-06-aandelen-met-warrant-0.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 139/6 |
| `CBN-0139-07-verwerking-van-uitgegeven-inschrijvingsrechten-in-de-jaarrekening.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 139/7 |
| `CBN-0140-overeenstemming-tussen-de-boekhouding-en-de-jaarrekening.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 140 |
| `CBN-0146-01-belastingschulden-sociale-schulden-verwijlinteresten.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 146/1 |
| `CBN-0146-02-vooruitbetalingen-van-sociale-zekerheidsbijdragen.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 146/2 |
| `CBN-0147-01-vastrentende-effecten-financiele-vaste-activa-of-geldbeleggingen-criteria.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 147/1 |
| `CBN-0147-03-meerwaarden-op-overheidseffecten-bedoeld-door-artikel-513-van-het-nieuwe-wib.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 147/3 |
| `CBN-0148-01-overeenkomsten-waarin-gespreide-of-opeenvolgende-prestaties-worden-voorzien.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 148/1 |
| `CBN-0148-02-vakantiegeld.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 148/2 |
| `CBN-0148-03-toerekenen-van-kosten-als-gevolg-van-een-waarborgovereenkomst.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 148/3 |
| `CBN-0148-04-boeking-van-de-prorata-van-gelopen-interest-op-obligaties-en-kasbons.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 148/4 |
| `CBN-0148-05-actuarieel-rendement-op-vastrentende-effecten-aanpassing-van-de-adviezen-1375-en-1484.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 148/5 |
| `CBN-0148-06-boekhoudkundige-verwerking-van-verrichtingen-afgesloten-onder-opschortende-voorwaarde.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 148/6 |
| `CBN-0150-01-materiele-vaste-activa-onderscheid-met-voorraden.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 150/1 |
| `CBN-0150-02-aansluitingskosten-en-installatiekosten-waarbij-derden-de-eigendom-van-de-installatie.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 150/2 |
| `CBN-0150-04-investering-voor-een-rationeler-energieverbruik-geintegreerd-energiebeheerprogramma.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 150/4 |
| `CBN-0151-01-kapitaalvermindering-door-terugbetaling-aan-de-vennoten-of-vrijstelling-van-volstorting.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 151/1 |
| `CBN-0151-02-toerekening-door-de-aandeelhouder-van-een-terugbetaling-van-kapitaal-of-een-uitgiftepremie.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 151/2 |
| `CBN-0152-02-boekhoudkundige-verwerking-van-een-kapitaalverhoging-als-gevolg-van-de-conversie-in.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 152/2 |
| `CBN-0152-03-boekhoudkundige-verwerking-van-een-kapitaalverhoging-als-gevolg-van-de-inbreng-van-een.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 152/3 |
| `CBN-0152-04-niet-monetaire-financiele-activa-in-deviezen-deelnemingen-en-aandelen.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 152/4 |
| `CBN-0152-05-verwerking-van-omrekeningsverschillen.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 152/5 |
| `CBN-0152-06-risicos-verbonden-aan-bestellingen-van-vaste-activa.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 152/6 |
| `CBN-0153-02-loonmatiging-bezoldigingen-van-bestuurders.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 153/2 |
| `CBN-0154-01-wijziging-van-de-waarderingsregels-als-gevolg-van-gewijzigde-wetgeving.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 154/1 |
| `CBN-0155-01-boeking-van-commissies.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 155/1 |
| `CBN-0156-01-attribution-au-fonds-de-solidarite.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 156/1 |
| `CBN-0157-01-tijdstip-waarop-de-winst-is-gerealiseerd.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 157/1 |
| `CBN-0157-02-realisatiebeginsel-behalve-bij-fusie.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 157/2 |
| `CBN-0158-01-boekhoudkundige-verwerking-van-de-aankoop-afschrijving-en-ontginning-in-concessie-van.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 158/1 |
| `CBN-0159-01-schulden-op-meer-dan-een-jaar-waarvoor-geen-of-slechts-een-abnormaal-lage-rente.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 159/1 |
| `CBN-0159-02-specifiek-achtergestelde-leningen.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 159/2 |
| `CBN-0160-01-toepassing-van-artikel-40-van-het-koninklijk-besluit-van-8-oktober-1976-op-de-jaarrekening.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 160/1 |
| `CBN-0161-01-aansprakelijk-vertegenwoordiger-tov-het-belastingbestuur.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 161/1 |
| `CBN-0162-01-boekhoudkundige-verwerking-van-het-vruchtgebruik-van-aandelen-dat-onder-bezwarende-titel.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 162/1 |
| `CBN-0163-boekhoudkundige-verwerking-van-in-substance-defeasance.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 163 |
| `CBN-0164-passende-boekhoudkundige-verwerking-van-de-tegenwaarde-van-participatiecertificaten-cpcs.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 164 |
| `CBN-0168-01-boekhoudkundige-verwerking-van-deelnemingen-in-vennootschappen-naar-buitenlands-recht-die.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 168/1 |
| `CBN-0169-01-verwerking-van-leningen-en-ontleningen-van-effecten-in-de-jaarrekening-van-ondernemingen.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 169/1 |
| `CBN-0169-02-verwerking-van-cessie-retrocessieverrichtingen-in-de-jaarrekening-van-ondernemingen.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 169/2 |
| `CBN-0170-01-boekhoudkundige-verwerking-van-niet-betaalde-schulden-wegens-ontoereikend-actief-bij-het.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 170/1 |
| `CBN-0171-boekhoudkundige-verwerking-van-afvalstoffen.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 171 |
| `CBN-0172-01-opneming-van-de-rekeningen-van-een-buitenlands-bijkantoor.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 172/1 |
| `CBN-0173-01-overschakeling-op-de-euro-boekhoudrechtelijke-aspecten.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 173/1 |
| `CBN-0173-02-boekhoudkundige-verwerking-van-de-afrondingen-bij-conversie.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 173/2 |
| `CBN-0173-03-toelichting-bij-de-datum-vanaf-wanneer-ondernemingen-waarvan-het-boekjaar-niet-samenvalt.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 173/3 |
| `CBN-0173-04-vervroegde-vaststelling-van-de-bilaterale-wisselkoersen-in-mei-1998-gevolgen-voor-het.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 173/4 |
| `CBN-0173-06-verrekening-van-vorderingen-en-schulden-die-oorspronkelijk-zijn-uitgedrukt-in-munten-die.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 173/6 |
| `CBN-0173-07-afronding-van-de-bedragen-in-de-jaarrekeningen-die-in-euro-of-in-duizenden-euro-zijn.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 173/7 |
| `CBN-0173-08-aanvullende-aspecten-in-verband-met-de-boekhoudkundige-verwerking-van.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 173/8 |
| `CBN-0174-01-beginselen-van-een-regelmatige-boekhouding.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 174/1 |
| `CBN-0175-01-verwerking-in-de-jaarrekening-over-het-boekjaar-1996-en-de-daaropvolgende-boekjaren-van-de.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 175/1 |
| `CBN-0175-02-verwerking-in-de-jaarrekening-over-het-boekjaar-1999-van-de-maribel-bis-en-ter-steun.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 175/2 |
| `CBN-0176-01-boekhoudrechtelijke-aspecten-met-betrekking-tot-het-jaar-2000.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 176/1 |
| `CBN-0177-01-boekhoudkundige-verwerking-van-de-mini-bel-20.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 177/1 |
| `CBN-0178-01-advies-met-betrekking-tot-de-jaarrekeningrechtelijke-aspecten-van-de-certificatie-van.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 178/1 |
| `CBN-0179-01-boekhoudkundige-verwerking-van-broeikasgasemissierechten.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 179/1 |
| `CBN-0180-01-verwerking-in-de-jaarrekening-van-de-door-de-vlaamse-regering-gecreeerde-opleidingscheques.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 180/1 |
| `CBN-2009-04-model-van-ongesplitst-dagboek-zoals-bedoeld-in-artikel-2-van-het-koninklijk-besluit-van-26.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 2009/4 |
| `CBN-2009-07-de-boekhoudkundige-verwerking-van-grensoverschrijdende-fusies.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 2009/7 |
| `CBN-2009-10-bepaling-van-de-functionele-valuta-bij-financieringsvennootschappen.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 2009/10 |
| `CBN-2009-11-de-boekhoudkundige-verwerking-van-partiele-splitsingen.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 2009/11 |
| `CBN-2009-12-de-sociale-balans-en-de-statutaire-werknemers.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 2009/12 |
| `CBN-2009-13-de-boekhoudkundige-verwerking-van-het-stelsel-tot-gedeeltelijke-vrijstelling-van-0.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 2009/13 |
| `CBN-2009-14-boekhoudkundige-verwerking-van-groenestroom-en-warmtekrachtcertificaten.md` | ✅ trusted | warn | trusted | subagent-sonnet-4-6 | CBN-advies 2009/14 |
| `CBN-2009-15-de-boekhoudkundige-verwerking-van-de-inbreng-van-een-bedrijfstak-of-van-een-algemeenheid.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 2009/15 |
| `CBN-2009-16-omrekening-van-kapitaal-bij-grensoverschrijdende-fusies.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 2009/16 |
| `CBN-2010-01-de-interpretatie-van-de-openbaarmakingsverplichting-van-transacties-van-enige-betekenis.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 2010/1 |
| `CBN-2010-02-de-boekhoudkundige-verwerking-van-het-stelsel-tot-gedeeltelijke-vrijstelling-van-betaling.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 2010/2 |
| `CBN-2010-03-de-boekhoudkundige-verwerking-van-stockdividenden.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 2010/3 |
| `CBN-2010-04-omrekeningsverschillen-ontstaan-bij-omrekening-van-het-kapitaal-naar-aanleiding-van-het.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 2010/4 |
| `CBN-2010-08-financiele-steunverlening.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 2010/8 |
| `CBN-2010-09-toepassingsgebied-van-het-koninklijk-besluit-van-10-augustus-2009.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 2010/9 |
| `CBN-2010-10-duur-van-het-boekjaar.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 2010/10 |
| `CBN-2010-11-boekhoudkundige-verwerking-van-loontussenkomst-door-de-overheid-in-hoofde-van-de-werkgever.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 2010/11 |
| `CBN-2010-12-de-toepassing-van-de-algemene-boekhoudprincipes-op-afgeleide-financiele-instrumenten.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 2010/12 |
| `CBN-2010-13-boekhoudkundige-verwerking-van-de-belasting-over-de-toegevoegde-waarde-in-hoofde-van-de.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 2010/13 |
| `CBN-2010-14-bewaring-van-boeken-en-verantwoordingsstukken.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 2010/14 |
| `CBN-2010-15-afschrijvingsmethoden.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 2010/15 |
| `CBN-2010-16-boekhoudkundige-verwerking-van-subsidies-schenkingen-en-legaten-toegekend-in-contanten-in.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 2010/16 |
| `CBN-2010-17-boekhoudkundige-verwerking-van-subsidies-schenkingen-en-legaten-in-natura-in-de.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 2010/17 |
| `CBN-2010-18-subsidies-en-schenkingen-vanuit-het-oogpunt-van-de-verstrekkende-vereniging-of-stichting.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 2010/18 |
| `CBN-2010-20-gebruik-van-uniforme-boekhoudsoftware-door-internationale-ondernemingen.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 2010/20 |
| `CBN-2010-21-de-boekhoudkundige-verwerking-van-transfervergoedingen-betaald-bij-de-mutatie-van.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 2010/21 |
| `CBN-2010-22-boekingswijze-van-een-voorschot-op-de-verdeling-van-het-netto-actief.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 2010/22 |
| `CBN-2011-02-zetelverplaatsing-naar-belgie-van-een-vennootschap-opgericht-naar-buitenlands-recht.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 2011/2 |
| `CBN-2011-04-boekhoudkundige-verwerking-van-leveringontvangst-van-handelsgoederen-om-niet-update-0.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 2011/4 |
| `CBN-2011-05-consolidatiekring-interpretatie-van-de-uitsluitingsgrond-van-artikel-107-4deg-kb-wvenn.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 2011/5 |
| `CBN-2011-06-boekhoudkundige-verwerking-van-de-aankoop-van-goud-en-kunstwerken.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 2011/6 |
| `CBN-2011-07-bestemde-fondsen.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 2011/7 |
| `CBN-2011-10-de-boekhoudkundige-verwerking-van-grensoverschrijdende-splitsingen.md` | ✅ trusted | warn | trusted | subagent-sonnet-4-6 | CBN-advies 2011/10 |
| `CBN-2011-11-de-boekhoudkundige-verwerking-van-grensoverschrijdende-partiele-splitsingen.md` | ✅ trusted | warn | trusted | subagent-sonnet-4-6 | CBN-advies 2011/11 |
| `CBN-2011-12-afwijking-inzake-functionele-valuta-praktische-implicaties-en-procedure.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 2011/12 |
| `CBN-2011-13-overheidssubsidies.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 2011/13 |
| `CBN-2011-14-herwaarderingsmeerwaarden.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 2011/14 |
| `CBN-2011-15-waardeverminderingen-op-handelsvorderingen-gedekt-door-een-kredietverzekering.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 2011/15 |
| `CBN-2011-17-boekhoudkundige-verwerking-van-onderzoeksfondsen-in-de-jaarrekening-van-grote-en-zeer.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 2011/17 |
| `CBN-2011-18-de-boekhoudkundige-verwerking-van-de-renteswap-interest-rate-swap.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 2011/18 |
| `CBN-2011-19-de-boekhoudkundige-verwerking-van-interestopbrengsten-en-kosten-door-erkende.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 2011/19 |
| `CBN-2011-20-verbonden-ondernemingen.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 2011/20 |
| `CBN-2011-21-bewaring-van-de-boeken-en-verantwoordingsstukken.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 2011/21 |
| `CBN-2011-22-boekhoudkundige-verwerking-van-de-door-de-vlaamse-regering-gecreeerde-kmo-portefeuille.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 2011/22 |
| `CBN-2011-23-de-boekhoudkundige-verwerking-van-factoringovereenkomsten.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 2011/23 |
| `CBN-2011-24-herstructureringskosten-verwerking-in-de-jaarrekening.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 2011/24 |
| `CBN-2012-01-boekhoudkundige-verwerking-van-een-overschot-aan-broeikasgasemissierechten-door-een.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 2012/1 |
| `CBN-2012-02-de-boekhoudkundige-verwerking-van-toegekende-voordelen-bij-het-afsluiten-van-een.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 2012/2 |
| `CBN-2012-03-de-boekhoudkundige-verwerking-van-aandelenoptieplannen.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 2012/3 |
| `CBN-2012-04-de-boekhoudkundige-verwerking-van-de-inbeslagname-in-hoofde-van-de-beslagen-schuldenaar.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 2012/4 |
| `CBN-2012-05-betaling-van-vorderingen-in-natura.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 2012/5 |
| `CBN-2012-06-de-boekhoudkundige-verwerking-van-de-tax-shelter-in-hoofde-van-de-productievennootschap.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 2012/6 |
| `CBN-2012-07-de-boekhoudkundige-verwerking-van-de-tax-shelter-in-hoofde-van-de-investeerder.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 2012/7 |
| `CBN-2012-08-de-boekhoudkundige-verwerking-van-de-inbreng-in-eigendom-in-een-belgische-burgerlijke.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 2012/8 |
| `CBN-2012-09-de-boekhoudkundige-verwerking-van-de-verwerving-van-een-vast-actief-voor-een-variabele.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 2012/9 |
| `CBN-2012-10-te-verwaarlozen-betekenis.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 2012/10 |
| `CBN-2012-12-vrijstelling-van-subconsolidatie.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 2012/12 |
| `CBN-2012-13-de-boekhoudkundige-verwerking-van-immateriele-vaste-activa.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 2012/13 |
| `CBN-2012-15-bestellingen-in-uitvoering.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 2012/15 |
| `CBN-2012-16-de-boekhoudkundige-verwerking-van-wentelkredieten.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 2012/16 |
| `CBN-2012-17-erkenning-van-opbrengsten-en-kosten.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 2012/17 |
| `CBN-2012-19-goederen-verworven-tegen-betaling-van-een-lijfrente.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 2012/19 |
| `CBN-2012-20-de-boekhoudkundige-verwerking-van-de-betaling-van-een-schuld-van-de-vennootschap-door-een.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 2012/20 |
| `CBN-2012-de-boekhoudkundige-verwerking-van-aandelenopties-als-zodanig.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 2012/18 |
| `CBN-2013-01-de-boekhoudkundige-verwerking-van-pseudo-fusies-van-verenigingen-en-stichtingen.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 2013/1 |
| `CBN-2013-02-het-gebruik-van-de-rekening-15-kapitaalsubsidies-door-grote-en-zeer-grote-verenigingen-en.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 2013/2 |
| `CBN-2013-03-de-boekhoudkundige-verwerking-van-step-acquisitions-update.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 2013/3 |
| `CBN-2013-04-de-boekhoudkundige-verwerking-van-step-disposals.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 2013/4 |
| `CBN-2013-05-de-aandeelhoudersstructuur-van-ondernemingen-opname-in-de-toelichting-van-de-jaarrekening.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 2013/5 |
| `CBN-2013-06-de-boekhoudkundige-verwerking-van-de-afzonderlijke-aanslag-op-interne.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 2013/6 |
| `CBN-2013-08-de-boekhoudkundige-verwerking-van-de-door-de-waalse-regering-gecreeerde-opleidingscheques.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 2013/8 |
| `CBN-2013-09-de-boekhoudkundige-verwerking-van-een-herziening-van-de-btw-op-een-aangekocht.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 2013/9 |
| `CBN-2013-11-begrip-omzet-doorrekening-van-belastingen-en-accijnzen.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 2013/11 |
| `CBN-2013-12-erkenning-van-de-opbrengsten-en-kosten-die-overeenstemmen-met-interesten-en-royaltys.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 2013/12 |
| `CBN-2013-14-de-boekhoudkundige-verwerking-van-de-uitgestelde-belastingen-bij-gerealiseerde-0.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 2013/14 NT |
| `CBN-2013-14-de-boekhoudkundige-verwerking-van-de-uitgestelde-belastingen-bij-gerealiseerde-meerwaarden.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 2013/14 |
| `CBN-2013-16-toelichting-omtrent-het-niet-gebruik-van-de-waarderingsgregels-op-basis-van-de-waarde-in.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 2013/16 |
| `CBN-2013-17-de-boekhoudkundige-verwerking-met-betrekking-tot-de-toepassing-van-de-overgangsregeling.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 2013/17 |
| `CBN-2014-03-de-boekhoudkundige-verwerking-van-mutaties-binnen-het-eigen-vermogen-van-een-geassocieerde.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 2014/3 |
| `CBN-2014-05-afsluitingsdatum-van-het-boekjaar.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 2014/5 |
| `CBN-2014-06-de-boekhoudkundige-verwerking-van-effecten-aan-toonder-van-rechtswege-omgezet-in-effecten.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 2014/6 |
| `CBN-2014-07-de-boekhoudkundige-verwerking-van-subsidies-waarvan-de-toekenning-niet-gegarandeerd-is.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 2014/7 |
| `CBN-2014-08-de-boekhoudkundige-verwerking-van-de-fairness-tax.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 2014/8 |
| `CBN-2015-01-boekhoudkundige-verwerking-van-de-tax-shelter-in-hoofde-van-de-investeerder.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 2015/1 |
| `CBN-2015-02-boekhoudkundige-verwerking-van-de-liquidatiereserve-programmawet-van-19-december-2014-en.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 2015/2 |
| `CBN-2015-03-verplichting-tot-opstelling-en-publicatie-van-de-jaarrekening-door-de-inbrengende.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 2015/3 |
| `CBN-2015-04-leasing.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 2015/4 |
| `CBN-2015-05-zakelijke-rechten-op-onroerende-goederen-vruchtgebruik-opstalrecht-erfpachtrecht.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 2015/5 |
| `CBN-2015-06-boekhoudkundige-verwerking-van-de-liquidatiereserve-bedoeld-in-artikel-541-wib-92.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 2015/6 |
| `CBN-2015-07-boekhoudkundige-verwerking-van-de-tax-shelter-in-hoofde-van-de-productievennootschap.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 2015/7 |
| `CBN-2015-08-boekhoudkundige-verwerking-van-de-aankoop-van-een-onroerend-goed-bestemd-voor-verkoop.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 2015/8 |
| `CBN-2015-10-vrijstelling-van-subconsolidatie-de-maatschap.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 2015/10 |
| `CBN-2016-01-verrichtingen-met-betrekking-tot-inschrijvingsrechten.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 2016/1 |
| `CBN-2016-02-boekhoudkundige-verwerking-van-ontvangen-subsidies-voor-de-aankoop-van-activa-die-worden.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 2016/2 |
| `CBN-2016-04-verenigingen-en-stichtingen-boekhoudkundige-verwerking-van-meerjarige-toekenningen-bij.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 2016/4 |
| `CBN-2016-05-waardering-van-voorraden-gezamenlijke-aankoop-en-doorverkoop-per-stuk.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 2016/5 |
| `CBN-2016-06-verbeteringswerken-aan-gehuurde-gebouwen.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 2016/6 |
| `CBN-2016-07-verwerving-van-een-bedrijfstak-tegen-een-symbolische-euro.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 2016/7 |
| `CBN-2016-08-bepaling-van-de-omzet-van-een-franchisenemer.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 2016/8 |
| `CBN-2016-09-verwerving-van-een-bebost-terrein.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 2016/9 |
| `CBN-2016-10-schulden-en-vorderingen-gevolgen-van-de-wijzigingen-aan-artikel-67-kb-wvenn-door-het.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 2016/10 |
| `CBN-2016-11-boekhoudkundige-verwerking-van-de-cross-currency-swap.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 2016/11 |
| `CBN-2016-12-verjaarde-schulden.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 2016/12 |
| `CBN-2016-13-verenigingen-en-stichtingen-roerende-voorheffing.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 2016/13 |
| `CBN-2016-14-bestellingen-in-uitvoering-wijzigingen-door-het-koninklijk-besluit-van-18-december-2015.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 2016/14 |
| `CBN-2016-15-vergoedingen-aan-bestuurders-en-werkende-vennoten.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 2016/15 |
| `CBN-2016-16-kosten-van-onderzoek-en-ontwikkeling-wijzigingen-door-het-koninklijk-besluit-van-18.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 2016/16 |
| `CBN-2016-17-verenigingen-en-stichtingen-certificatie-van-aandelen-van-handelsvennootschappen.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 2016/17 |
| `CBN-2016-18-prestaties-geleverd-aan-overheid-verschuldigde-btw.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 2016/18 |
| `CBN-2016-19-consortium-toepasselijke-rapporteringsstandaard-vrijstelling-van-subconsolidatie-update-0.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 2016/19 |
| `CBN-2016-20-leveranciersschulden-en-schulden-aan-de-overheid-in-het-kader-van-boek-xx-insolventie-van.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 2016/20 – UPDATE |
| `CBN-2016-21-actualisatie-van-uitgestelde-belastingen-update.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 2016/21 |
| `CBN-2016-22-bewaring-van-boeken-en-verantwoordingsstukken-bij-een-geinformatiseerde-boekhouding.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 2016/22 |
| `CBN-2016-24-uitzonderlijke-resultaten-wijzigingen-door-het-koninklijk-besluit-van-18-december-2015.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 2016/24 |
| `CBN-2016-25-kapitaalvermindering-voor-vorming-van-een-reserve-voor-een-voorzienbaar-verlies.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 2016/25 |
| `CBN-2016-26-kilometerheffing.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 2016/26 |
| `CBN-2016-27-kosten-van-onderzoek-en-ontwikkeling-onderscheid-tussen-onderzoek-en-ontwikkeling.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 2016/27 |
| `CBN-2017-01-consortium-lidmaatschapsrechten-artikel-1401-5-bw.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 2017/01 |
| `CBN-2017-02-gezamenlijke-controle-over-een-vennootschap-groottecriteria-update.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 2017/02 |
| `CBN-2017-03-groottecriteria-boekjaar-korter-of-langer-dan-12-maanden-update.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 2017/03 |
| `CBN-2017-04-gegeven-borgtochten-in-contanten-en-effecten-update.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 2017/04 |
| `CBN-2017-07-niet-in-de-balans-opgenomen-rechten-en-verplichtingen.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 2017/07 |
| `CBN-2017-08-cijfers-van-het-vorig-boekjaar-bij-opmaak-jaarrekening-volgens-nieuw-model.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 2017/08 |
| `CBN-2017-10-groottecriteria-artikel-15-wvenn-verbonden-vennootschappen-verschillende-afsluitingsdata.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 2017/10 |
| `CBN-2017-11-opname-van-financiele-vaste-activa-geboekt-tegen-een-hoger-bedrag-dan-hun-reele-waarde-in.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 2017/11 |
| `CBN-2017-13-boekhoudkundige-verwerking-van-de-vergoeding-voor-een-borg-in-het-kader-van-de.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 2017/13 |
| `CBN-2017-14-verenigingen-en-stichtingen-verwerving-door-de-erfpacht-houder-van-het-met-een-erfpacht.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 2017/14 |
| `CBN-2017-15-transacties-onder-gemeenschappelijke-leiding-common-control-transactions-update.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 2017/15 |
| `CBN-2017-16-onbeperkt-aansprakelijke-vennoot-vermeldingen-in-de-jaarrekening.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 2017/16 |
| `CBN-2017-17-reverse-factoring.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 2017/17 |
| `CBN-2017-18-afschrijving-van-materiele-vaste-activa-in-aanbouw-en-vooruitbetalingen-inresultaatname.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 2017/18 |
| `CBN-2018-01-aftrek-voor-innovatie-inkomsten.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 2018/01 |
| `CBN-2018-02-belastingkrediet-voor-kosten-van-onderzoek-en-ontwikkeling.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 2018/02 |
| `CBN-2018-03-zetelverplaatsing-naar-belgie-inbound-verschil-in-waarderingsregels-ten-opzichte-van-het.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 2018/03 |
| `CBN-2018-04-de-boekhoudkundige-verwerking-van-derdenrekeningen-0.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 2018/04 |
| `CBN-2018-05-rekening-130-wettelijke-reserve.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 2018/05 |
| `CBN-2018-07-vereniging-van-aandelen-in-handen-van-een-enkele-rechtspersoon-vermeldingen-in-de.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 2018/07 |
| `CBN-2018-08-gebeurtenissen-na-afsluitingsdatum-van-het-boekjaar.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 2018/08 |
| `CBN-2018-09-tax-shelter-voor-podiumkunsten.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 2018/09 |
| `CBN-2018-11-verkoop-van-oplaadbare-betaalkaarten.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 2018/11 |
| `CBN-2018-12-interpretatie-van-code-99084-in-de-toelichting-514-van-de-geconsolideerde-jaarrekening.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 2018/12 |
| `CBN-2018-13-provisie-aanvullende-dagen-verlof-arbeidsduurvermindering.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 2018/13 |
| `CBN-2018-14-belastingen.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 2018/14 |
| `CBN-2018-15-boekhoudkundige-verwerking-van-onder-meer-de-rendementswaarborg-voor-werkgeversbijdragen.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 2018/15 |
| `CBN-2018-16-toekenning-van-gratis-aandelen-restricted-stock-units-als-bonus.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 2018/16 |
| `CBN-2018-17-schulden-gewaarborgd-door-een-zakelijke-zekerheid-niet-in-de-balans-opgenomen-rechten-en.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 2018/17 |
| `CBN-2018-18-going-concern-waarderingsregels-bij-de-stopzetting-of-gedeeltelijke-stopzetting-van-het.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 2018/18 |
| `CBN-2018-19-boekhoudkundige-verwerking-van-winstpremies.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 2018/19 |
| `CBN-2018-20-boekhoudkundig-niet-compensatiebeginsel.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 2018/20 |
| `CBN-2018-21-vrijstelling-mbt-het-sociaal-passief-ingevolge-het-eenheidsstatuut.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 2018/21 |
| `CBN-2018-22-groottecriteria-alternatieve-berekening-van-de-omzet-op-geconsolideerde-of-geaggregeerde.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 2018/22 |
| `CBN-2018-23-begin-van-het-boekjaar.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 2018/23 |
| `CBN-2018-24-duolegaat-vereniging-en-stichting.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 2018/24 |
| `CBN-2018-25-voorzieningen.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 2018/25 |
| `CBN-2019-01-dividenduitkering-en-kapitaalvermindering-in-natura-0.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 2019/01 |
| `CBN-2019-03-ziekenhuisfinanciering-de-boekhoudkundige-verwerking-van-het-instandhoudingsforfait-en-0.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 2019/03 |
| `CBN-2019-04-gevolgen-op-gebied-van-financiele-rapportering-als-gevolg-van-de-brexit-0.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 2019/04 |
| `CBN-2019-05-vergoedingen-vrijwilligerswerk-en-verenigingswerk.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 2019/05 |
| `CBN-2019-06-groepsbijdrage.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 2019/06 |
| `CBN-2019-07-boekhoudkundige-verwerking-van-de-uitgifte-van-een-obligatielening.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 2019/07 |
| `CBN-2019-08-boekhoudkundige-verwerking-van-crowdfunding-0.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 2019/08 |
| `CBN-2019-09-boekhoudplichtige-onderneming.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 2019/09 |
| `CBN-2019-10-de-boekhoudkundige-en-jaarrekeningrechtelijke-verplichtingen-van-een-beoefenaar-van-een-0.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 2019/10 |
| `CBN-2019-11-de-vereenvoudigde-boekhouding-van-een-natuurlijke-persoon-maatschap-vennootschap-onder.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 2019/11 |
| `CBN-2019-12-groottecriteria-verenigingen-en-stichtingen-schema-van-de-jaarrekening-begroting.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 2019/12 |
| `CBN-2019-13-pro-rata-regel-van-artikel-18-wib-92-bij-terugbetaling-van-inbreng-kapitaalvermindering.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 2019/13 |
| `CBN-2019-14-van-een-kapitaalhoudende-bvba-naar-een-kapitaalloze-bv.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 2019/14 |
| `CBN-2019-15-aanschaffingswaarde-van-een-actiefbestanddeel-verkregen-in-ruil-voor-een-tegenprestatie.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 2019/15 |
| `CBN-2020-01-neerlegging-van-de-enkelvoudige-jaarrekening-bij-de-nationale-bank-van-belgie-nieuwe.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 2020/01 |
| `CBN-2020-02-afronding-van-betalingen-in-euro-0.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 2020/02 |
| `CBN-2020-03-taal-van-de-jaarrekening-de-geconsolideerde-jaarrekening-en-de-andere-bij-de-nationale-0.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 2020/03 |
| `CBN-2020-05-verenigingen-en-stichtingen-vereenvoudigde-boekhouding-waarderingsregels.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 2020/05 |
| `CBN-2020-06-financieringskostensurplus-artikel-194sexies-en-artikel-1981-wib-92.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 2020/06 |
| `CBN-2020-07-mogelijkheid-tot-uitstel-van-de-goedkeuring-en-neerlegging-van-de-jaarrekening-vzws-0.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 2020/07 |
| `CBN-2020-08-mogelijkheid-tot-uitstel-van-de-gewone-algemene-vergadering-en-van-de-neerlegging-van-de.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 2020/08 |
| `CBN-2020-09-vermelding-in-de-jaarrekening-van-de-gegevens-van-de-bestuurders-en-de-commissaris.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 2020/09 |
| `CBN-2020-10-schenkingen-en-legaten-voor-vzws-ivzws-en-stichtingen-die-een-dubbele-boekhouding-voeren.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 2020/10 |
| `CBN-2020-11-vrijstelling-ter-versterking-van-de-solvabiliteit-en-het-eigen-vermogen-van-de-0.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 2020/11 |
| `CBN-2020-12-correctie-van-de-jaarrekening-0.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 2020/12 |
| `CBN-2020-13-overgang-van-een-kapitaalhoudende-cooperatieve-vennootschap-naar-een-kapitaalloze.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 2020/13 |
| `CBN-2020-14-boekhoudkundige-verwerking-van-de-aan-verkoop-van-een-actief-via-een-geblokkeerde-0.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 2020/14 |
| `CBN-2020-15-zetelverplaatsing-naar-belgie-model-van-staat-van-activa-en-passiva-bij-immigrerende.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 2020/15 |
| `CBN-2021-01-uitgiftepremie-0.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 2021/01 |
| `CBN-2021-02-winstverdeling-binnen-de-nv.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 2021/02 |
| `CBN-2021-03-de-boekhoudkundige-verwerking-van-het-vennootschapsvermogen-van-een-vof-en-een-commv.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 2021/03 |
| `CBN-2021-04-aanschaffingswaarde-bij-de-aankoop-van-een-goed-tegen-betaling-van-een-vaste-prijs-0.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 2021/04 |
| `CBN-2021-05-boekhoudrechtelijke-behandeling-van-kwijtschelding-van-huur-ten-gevolge-van-de-covid-19.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 2021/05 |
| `CBN-2021-07-invloed-van-het-buitengerechtelijk-minnelijk-akkoord-en-de-gerechtelijke-reorganisatie-1.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 2021/07 |
| `CBN-2021-08-verplichting-voor-bepaalde-vzws-ivzws-en-stichtingen-om-een-jaarverslag-op-te-stellen.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 2021/08 |
| `CBN-2021-09-rekening-26-overige-materiele-vaste-activa.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 2021/09 |
| `CBN-2021-10-boekhoudkundige-verwerking-van-fusies-tussen-vennootschappen.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 2021/10 |
| `CBN-2021-11-boekhoudkundige-verwerking-van-covid-19-tegemoetkomingen-en-van-kosten-gemaakt-ten-gevolge.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 2021/11 |
| `CBN-2021-12-boekhoudrechtelijke-verwerking-van-de-wederopbouwreserve.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 2021/12 |
| `CBN-2021-13-herwaarderingsmeerwaarden-bij-vennootschappen-gevolgen-van-de-wijzigingen-aangebracht-door.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 2021/13 |
| `CBN-2021-14-jaarrekeningrechtelijke-analyse-van-de-alarmbelprocedure-onder-het-wvv.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 2021/14 |
| `CBN-2021-15-verenigingen-en-stichtingen-compensatie-van-negatieve-fondsen.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 2021/15 |
| `CBN-2021-16-waarderen-en-boeken-van-cryptomunten-gebruikt-als-betaalmiddel.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 2021/16 |
| `CBN-2021-17-boekhoudkundige-verwerking-van-de-vergoeding-voor-de-groepsbijdrage-in-hoofde-van-de.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 2021/17 |
| `CBN-2022-01-boekhoudkundige-verwerking-van-splitsingen-van-vennootschappen-negatief-fiscaal.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 2025/01 |
| `CBN-2022-01-fusies-en-splitsingen-van-vennootschappen-met-een-negatief-nettoactief.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 2022/01 |
| `CBN-2022-02-uittreding-en-uitsluiting-lastens-het-vennootschapsvermogen-bij-de-bv-en-cv.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 2022/02 |
| `CBN-2022-03-beoordeling-van-de-groottecriteria-overeenkomstig-artikelen-124-en-125-van-het-wetboek-van.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 2022/03 |
| `CBN-2022-04-verslaggeving-bij-ontbinding-en-vereffening-van-bv-cv-nv-se-en-sce.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 2022/04 |
| `CBN-2022-05-verslaggeving-bij-ontbinding-en-vereffening-van-een-vzw-of-ivzw.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 2022/05 |
| `CBN-2022-06-verslaggeving-bij-onmiddellijke-sluiting-van-de-vereffening-van-een-vennootschap.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 2022/06 |
| `CBN-2022-07-verslaggeving-bij-onmiddellijke-sluiting-van-de-vereffening-van-een-vzw-of-ivzw.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 2022/07 |
| `CBN-2022-08-wijziging-van-het-boekhoudkundig-referentiestelsel.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 2022/08 |
| `CBN-2022-09-consolidatie-bij-de-horizontale-groep-consortium-0.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 2022/09 |
| `CBN-2022-10-boekhoudkundige-verwerking-van-interesten-en-andere-bedragen-verschuldigd-wegens.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 2022/10 |
| `CBN-2022-11-vermogensmutatiemethode.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 2022/11 |
| `CBN-2022-12-boekhoudkundige-verwerking-van-splitsingen-van-vennootschappen.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 2022/12 |
| `CBN-2022-13-boekhoudkundige-verwerking-van-fusies-tussen-verenigingen-en-stichtingen.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 2022/13 |
| `CBN-2022-14-belgische-bijkantoren-van-buitenlandse-vennootschappen-toepassing-van-het-belgisch.md` | ✅ trusted | warn | trusted | subagent-sonnet-4-6 | CBN-advies 2022/14 |
| `CBN-2022-16-omzetting-van-een-vennootschap-gevolgen-voor-de-jaarrekening.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 2022/16 |
| `CBN-2024-01-vermogensklem-bij-de-omzetting-van-een-vzw-in-een-cooperatieve-vennootschap-erkend-als-0.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 2024/01 |
| `CBN-2024-02-belgische-bijkantoren-van-buitenlandse-verenigingen-en-stichtingen-toepassing-van-het-0.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 2024/02 |
| `CBN-2024-04-terugbetaling-van-kapitaal-in-vreemde-valuta-aan-de-aandeelhouders.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 2024/04 |
| `CBN-2024-05-boekhoudkundige-verwerking-van-de-taks-tot-vergoeding-der-successierechten.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 2024/05 |
| `CBN-2024-06-openbaarmakingsverplichtingen-in-hoofde-van-de-vennootschap-onder-firma-en-de.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 2024/06 |
| `CBN-2024-07-gevolgen-verhoging-groottecriteria-voor-vennootschappen.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 2024/07 |
| `CBN-2024-08-gevolgen-verhoging-groottecriteria-voor-ivzws-en-stichtingen.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 2024/08 |
| `CBN-2024-10-verslaggeving-bij-de-heropening-van-de-vereffening-van-ivzws-die-een-dubbele-boekhouding.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies 2024/10 |
| `CBN-NFP-aanbevelingen-inzake-de-gelijkwaardigheid-van-boekhoud-en-jaarrekeningregels-opgelegd-door.md` | ✅ trusted | pass | trusted | subagent-sonnet-4-6 | CBN-advies NFP |
