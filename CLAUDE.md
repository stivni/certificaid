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
