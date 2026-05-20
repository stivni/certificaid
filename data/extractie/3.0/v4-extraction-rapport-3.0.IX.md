# EXTRACT v4 — rapport PO 3.0.IX "Ontbinding en vereffening"

**Run**: 2026-05-20  
**Anchor**: 3.0.IX  
**Wave**: Wave 1 vervolg (na pilot 3.0.II + 3.0.I + 3.0.IV)  
**Bundle**: `/tmp/po-3.0-pilot/bundle-3.0.IX.json` (191 chunks, geen truncatie)

---

## Records

### Nieuw (14)

| ID | node_type | Hoofd-grondslag |
|---|---|---|
| `ontbinding-vennootschap` | cluster | WVV art. 2:70 — 2:76 |
| `vrijwillige-ontbinding` | regel | WVV art. 2:67 + 2:71 |
| `gerechtelijke-ontbinding` | regel | WVV art. 2:73 + 2:81 |
| `ontbinding-van-rechtswege` | regel | WVV art. 2:68 + 2:35 |
| `vereffeningsprocedure-klassiek` | cluster | WVV art. 2:75 — 2:102 (5 fasen) |
| `vereffening-in-een-akte` | regel | WVV art. 2:80 |
| `vereffenaar` | begrip | WVV art. 2:75 — 2:98 |
| `staat-van-activa-en-passiva-ontbinding` | begrip | WVV art. 2:71 § 2 + ITAA-norm bijlage 3 |
| `omstandige-staat-vereffening` | begrip | WVV art. 2:86 + 2:99 |
| `sluiting-vereffening` | cluster | WVV art. 2:90 — 2:104 |
| `heropening-vereffening` | regel | WVV art. 2:95 + 2:105 + CBN 2024/09 |
| `liquidatiebonus` | begrip | WIB92 art. 18, 2°ter + CBN 2019/01 |
| `klassieke-versus-een-akte-vereffening` | synthese | vergelijkingstabel — art. 2:71 vs 2:80 |
| `vrijwillige-versus-gerechtelijke-ontbinding` | synthese | vergelijkingstabel — art. 2:70 e.v. |

### Bijgewerkt (1)

- `vereffening` — `linked_anchors` uitgebreid met `3.0.IX`; 5 nieuwe edges toegevoegd richting de nieuwe juridische records (`ontbinding-vennootschap`, `vereffeningsprocedure-klassiek`, `vereffenaar`, `sluiting-vereffening`, `vereffening-in-een-akte`). Cross-PO link tussen PO 1.1-boekhoudkundige perspectief en PO 3.0.IX-juridische uitwerking.

### Verwijderd / hernoemd

Geen.

---

## Audit

```
[audit] disk: 526 records (37 synthese), RAG: 526 records, content: 489 fiches
[audit] OK — disk, RAG en content zijn in sync.
```

Stijging: 512 → 526 records (+14, exact het aantal nieuwe records).

---

## Cross-PO edges

Bestaande PO 1.x/3.0-records waarheen edges gelegd zijn:

- `continuiteitsbeginsel` (PO 1.1) — `getriggerd-door` vanuit `ontbinding-vennootschap`
- `vereffening` (PO 1.1) — uitgebreid met cross-link, gewerkt als boekhoudkundige tegenhanger
- `ontbinding-vereffening-opdracht` (PO 1.6) — `verwijst-naar` vanuit `vereffenaar` en `staat-van-activa-en-passiva-ontbinding`
- `bestuursorgaan` (PO 3.0 pilot) — `vereist-kennis-van` vanuit `ontbinding-vennootschap` en `vereffenaar`
- `uitkering-uit-eigen-vermogen-bv` (PO 3.0.IV) — `verwijst-naar` vanuit `liquidatiebonus`

---

## Migraties

Geen — alle nieuwe records zijn schema 1.6 direct. `vereffening`-update bevat geen oude type-migratie (was al cluster sinds PO 1.1-touchup 2026-05-18); enkel veld-uitbreiding.

---

## `inferred-from-aggregation`-claims

- `ontbinding-vennootschap.situering` — aggregatie WVV art. 2:70 + MvT
- `vereffeningsprocedure-klassiek.situering` — aggregatie CBN 2022/04 + ITAA-norm § I.4
- `gerechtelijke-ontbinding.voorwaarden[sluimerende vennootschappen]` — aggregatie MvT art. 1:27 (rechtstreekse WVV-chunks ontbraken voor art. 2:74 e.v., zie gap)
- `vereffenaar.situering` — aggregatie WVV art. 2:88 + 2:96 + ITAA-norm
- `liquidatiebonus.situering` — aggregatie CBN 2019/01 + WIB92
- Beide syntheses (`klassieke-versus-een-akte-vereffening`, `vrijwillige-versus-gerechtelijke-ontbinding`) — kerninzichten vrijwel volledig aggregatief

---

## Regime-cluster-heuristiek (pilot-bevinding)

Toegepast op `vrijwillige-ontbinding`: één regel met **regime-bouwstenen** voor BV/CV/NV (4/5-meerderheid via art. 5:84 / 6:70 § 2 / 7:132) en uitzondering voor VOF/CommV — **niet** N parallelle records per vennootschapsvorm. Zelfde principe in `vereffeningsprocedure-klassiek` (vijf fasen WVV-overstijgend gemaakt, met fase 4 die alleen voor BV/CV/NV de jaarrekening-in-vereffening cite).

VZW/IVZW-parallel-regime (art. 2:107 — 2:140) bewust **niet** verwerkt als parallel-records — gap-entry geplaatst.

---

## Gaps.json — toevoegingen (7)

| Aspect | Record / Onderwerp | Prio |
|---|---|---|
| `records.ontbreekt` | Alarmbel-procedure NV (art. 7:228) + BV (art. 5:153) | hoog |
| `records.ontbreekt` | Vereffenaarsaansprakelijkheid (art. 2:96 + 2:106) — PO 3.0.VII | midden |
| `records.ontbreekt` | Vereffening VZW/IVZW/stichting (art. 2:107 — 2:140 + CBN 2022/05) | laag |
| `dangling-reference` | `fiscaal-gestort-kapitaal` (op `liquidatiebonus`) | midden |
| `dangling-reference` | `VVPR-bis-regime` (op `liquidatiebonus`) | laag |
| `bron-gap` | Sluimerende-vennootschap-art. 2:74 e.v. niet in WVV-chunks | midden |
| `granulariteit.beslissing-nodig` | `vereffenaar`-keuze begrip vs autoriteit | laag |

Totale `gaps.json`: 951 → 958 entries.

---

## Open observaties (niet record-specifiek)

- **Alarmbelprocedure bewust niet diepgaand uitgewerkt** in deze pass. Hoort bij PO 3.0.V/VI (eigen vermogen / kapitaal-issues). Bundle bevatte weinig dekking; primaire bron is art. 5:153/7:228. Hier alleen vermeld in `vereffening`-valkuilen die al bestonden en in `ontbinding-vennootschap`-bouwsteen waar relevant.
- **Vereffenaarsaansprakelijkheid op art. 2:96 + 2:106**: alleen aangestipt als valkuil in `vereffenaar`. Diep uitwerken wacht op PO 3.0.VII-wave conform scope-instructie.
- **Sub-anchors 3.0.IX.A / B**: niet gedekt — wachten op latere sub-wave.
- **CBN-advies 2022/04 §accountant-rol** geeft rijke beschrijving van het verschil in opdrachten voor commissaris vs niet-commissaris. Verwerkt in `sluiting-vereffening`-bouwsteen en synthese; mogelijk waardevol om bij PO 1.6-opdrachtenfiche te cross-linken (`ontbinding-vereffening-opdracht` bestaat).
- **CBN 2018/18-record** (going concern bij stopzetting): zou eigen record verdienen, maar valt onder PO 1.1 — niet hier gemaakt om scope te respecteren.
- **WVV-extractie van afdelingen-titels onvoldoende**: enkele WVV-chunks tonen `Art. 2:67` met paragraaf-§ 1 maar de bredere onderafdeling-context (bv. "Onderafdeling 3 — Ontbinding van rechtswege") wordt alleen via MvT-chunks aangeleverd. Goed nieuws: combinatie WVV+MvT+CBN gaf voldoende dekking; geen blocker.

---

## Zelf-evaluatie

**Volledigheid scope**: alle kernthema's uit de instructie zijn gedekt — ontbindingsgronden (vrijwillig/rechtswege/gerechtelijk), alarmbel als trigger (kort), vereffening klassiek + één-akte, bevoegdheden en aansprakelijkheid vereffenaar (afgeschermd), sluiting, heropening. Insolventie strikt uit scope gebleven.

**Granulariteit**: 14 records ligt aan het bovenscheidende van de instructie-range (10-15). Twee syntheses passen in de cast; cluster `vereffeningsprocedure-klassiek` met 5-fasen-bouwstenen vermijdt 5 mini-records.

**Cross-PO-integratie**: `vereffening` (PO 1.1) en `ontbinding-vereffening-opdracht` (PO 1.6) cross-linked zonder dubbelmaak. De boekhoudkundige laag in `vereffening` complementeert nu de juridische laag in `vereffeningsprocedure-klassiek`.

**Bron-stevigheid**: gemiddeld 2-3 chunk-IDs per claim; mix WVV (primaire bron), MvT (situering), ITAA-norm (opdracht-conventies), CBN-adviezen (boekhoudkundige verwerking). Vrijwel alle main-rules `grounded`; situerings en syntheses correct gelabeld `inferred-from-aggregation`.

**Risico's**: 
- Sluimerende-vennootschap-procedure deels op MvT gebaseerd zonder directe art. 2:74-chunk. Gap geflagd.
- Liquidatiebonus-record snijdt fiscaal werkterrein dat eigenlijk PO 4.x is — bewust kort gehouden, twee danglings geflagd.
