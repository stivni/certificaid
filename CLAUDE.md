# Certificaid

Kennisbank voor het ITAA bekwaamheidsexamen (gecertificeerd accountant / gecertificeerd belastingadviseur).

## Doel
Gestructureerde conceptfiches die:
- Vakoverschrijdend zijn (één concept, meerdere vakken)
- Terugkoppelen naar kenniselementen uit de officiële ITAA-brochure
- Alleen verifieerbare informatie bevatten (bronvermelding verplicht)

## Structuur
```
certificaid/
├── CLAUDE.md
├── quartz.config.ts        # Quartz-configuratie (titel, plugins, baseUrl)
├── quartz.layout.ts        # Quartz-layout (sidebar, zoeken, backlinks)
├── quartz/                 # gitignored — symlink naar node_modules na `npm install`
├── package.json            # devDependency: @jackyzha0/quartz van GitHub
├── .gitignore
├── .github/
│   └── workflows/
│       └── deploy.yml      # Build & deploy naar GitHub Pages bij push op main
├── content/
│   ├── index.md
│   └── concepten/          # Één .md per concept, zie conventie hieronder
├── tools/
└── resources/              # Bronmateriaal (bv. ITAA-brochure PDF)
```

### Publicatie
- Site: https://stivni.github.io/certificaid
- Lokaal testen: `npm install && npm run dev` → http://localhost:8080
- Deploy triggert automatisch bij wijzigingen in `content/`, `quartz.config.ts` of `quartz.layout.ts`

## Absolute regel: geen hallucinaties
Dit is de belangrijkste regel van het hele project.

- Elk feit, elke definitie, elk wetsartikel moet traceerbaar zijn naar een
  concrete bron
- Schrijf NOOIT iets over wetsinhoud zonder een bronverwijzing
- Als je een concept niet met zekerheid kunt onderbouwen vanuit een bron:
  zeg dat expliciet, vul het veld NIET in, en markeer het als `⚠️ te verifiëren`
- Liever een leeg veld dan een onzeker feit

## Bronhiërarchie (van meest naar minst gezaghebbend)
1. Officiële wetteksten op [ejustice.just.fgov.be](http://ejustice.just.fgov.be) (geconsolideerde versies)
2. [Fisconet.be](http://Fisconet.be) (WIB92, WBTW, ...)
3. CBN-adviezen op [cnc-cbn.be](http://cnc-cbn.be)
4. ITAA-normen op [itaa.be](http://itaa.be)
5. NBB-documentatie op [nbb.be](http://nbb.be)
6. De ITAA-brochure zelf (resources/programma.pdf) — voor structuur en leerdoelen
7. Online resources, waarvan je dan de juistheid nog moet verifiëren met bovenstaande bronnen

## Conventie conceptfiche
Elk bestand in content/concepten/ volgt dit formaat:

```
---
tags: [1.2, 1.3, 2.3]
niveau: integratie
bronnen:
  - WVV art. 5:142
itaa-lex: p. ~
---

# Naam van het concept

Zie ook: [[concept-a]], [[concept-b]]

## Definitie
[letterlijk of nauw aansluitend bij de wettekst]

## Per vak
### [1.2] Boekhoudrecht
...
### [2.3] Vennootschapsbelasting
...
```

## Kenniselement-IDs
Komen uit de officiële brochure (april 2022):
1.1 t.e.m. 1.9 = accountancy
2.1 t.e.m. 2.8 = fiscaal
3.1, 3.2 = vennootschapsrecht
4.0 = deontologie
