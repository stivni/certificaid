# ADR-013: Quartz als static site generator

**Status**: Draft  
**Datum**: 2026-05-06

## Context

De kennisbank moet publiceerbaar zijn als doorzoekbare website. De content is geschreven in Obsidian-flavored Markdown met wikilinks (`[[link]]`) — de site-generator moet die native begrijpen.

## Beslissing

**Quartz v4** (`@jackyzha0/quartz`, gebouwd op GitHub Actions → GitHub Pages).

Redenen:
- Native Obsidian-wikilink support — geen conversie nodig
- Statische HTML — geen server, geen kosten, geen onderhoud
- Backlinks, graafweergave, zoekfunctie ingebouwd
- `npm run dev` voor lokale preview

## Gevolgen

- Ankers in wikilinks volgen Quartz-slugging: speciale tekens (`:`, `.`, `/`) verdwijnen, spaties worden koppeltekens, emoji verdwijnen maar hun spatie blijft (→ leading dash in anker)
- Deploy triggert automatisch via `.github/workflows/deploy.yml` bij push naar `main`
- `quartz/` directory is gitignored (node_modules-equivalent)
- Site: `https://stivni.github.io/certificaid`
