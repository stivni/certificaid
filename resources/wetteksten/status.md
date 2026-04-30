# Wetteksten — status

Download als PDF → drop in `resources/wetteksten/` → `pdftotext -layout x.pdf x.txt`.
Geconsolideerde versies via ejustice: open de wet in de browser, linkerpaneel → "PDF geconsolideerde versie".

## Truc: geconsolideerde PDF vinden op ejustice

Elke wet op ejustice heeft (als die beschikbaar is) een **"PDF geconsolideerde versie"**-link
in het rechterpaneel van de `change_lg.pl`-pagina. URL-patroon:

```
https://www.ejustice.just.fgov.be/cgi_loi/change_lg.pl?language=nl&la=N&table_name=wet&cn=XXXXXXXXXX
```

De PDF-link heeft het formaat: `/img_l/pdf/YYYY/MM/DD/XXXXXXXXXX_N.pdf`

Wetboeken staan ook op: https://www.ejustice.just.fgov.be/cgi_loi/codex.pl?language=nl

## Nog manueel te downloaden

- [ ] `WIB92.pdf` — Wetboek Inkomstenbelastingen 1992 — ⚠️ Justel-versie niet bijgewerkt sinds 2002. Actuele versie enkel op myminfin.fgov.be (authenticatie vereist). Alternatief: vraag PDF via ITAA.
- [ ] `BTW-Wetboek.pdf` — WBTW (wet 3/7/1969) — geen gecoördineerde PDF beschikbaar op ejustice. Zelfde probleem als WIB92.
- [ ] `BW-2019.pdf` — Nieuw Burgerlijk Wetboek (wet 13/4/2019) — type "BURGERLIJK WETBOEK" in ejustice, CN nog niet gevonden. Probeer zoekinterface op ejustice.
- [ ] `VCF-UVB.pdf` — B.Vl.Reg. 20/12/2013 uitvoering VCF — via codex.vlaanderen.be
- [ ] `Ord-Brussel-Fiscale-Procedure.pdf` — Ord. 06/03/2019 Brusselse Codex Fiscale Procedure — via ejustice (CN onbekend, publicatie B.S. 19/03/2019)
- [ ] `Decr-Waals-Invordering.pdf` — Decr. W.R. 06/05/1999 directe gewestelijke belastingen — via ejustice

## Reeds aanwezig (PDF + txt + md)

| Bestand | Wet | Bron |
|---------|-----|------|
| `VCF.md` | Vlaamse Codex Fiscaliteit (gecoördineerd t.e.m. 31/12/2025) | ejustice img_l |
| `Wetboek-Invordering.md` | Wetboek Minnelijke en Gedwongen Invordering 2019 | ejustice img_l |
| `WDRT.md` | Wetboek Diverse Rechten en Taksen | ejustice img_l |
| `Oud-BW.md` | Oud Burgerlijk Wetboek (1804, gecoördineerd) | ejustice img_l |
| `KB-WIB92.md` | KB 27/08/1993 uitvoering WIB92 (107 p., gecoördineerd) | ejustice img_l |
| `WER.md` + `WER-Boek-VIII-normalisatie.md` | Wetboek Economisch Recht | PDF manueel |
| `WVV.md` + `KB-WVV-2019.md` | WVV + uitvoeringsbesluit | PDF manueel |
| `Wet-ITAA-2019.md` | Wet beroepen accountant en belastingadviseur | PDF manueel |
| `Antiwitwaswet-2017.md` | Antiwitwaswet 2017 (gecoördineerd t.e.m. 24/12/2025) | PDF manueel |
| `KB-21-10-2018.md` | KB 21/10/2018 uitvoering WER art. III.82–III.95 | PDF manueel |
| `KB-WER-boekhouding-2018.md` | KB 21/10/2018 (manueel verwerkte MD-versie) | manueel |
| `Richtlijn-2013-34-EU.md` | EU-Richtlijn 2013/34/EU jaarrekeningen | PDF manueel |
