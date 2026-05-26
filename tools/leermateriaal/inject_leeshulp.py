"""
Leeshulp-injectie: bron + leeshulp → publicatie-versie in content/.

Drie-laag-architectuur (zie ADR-034):
- `resources/bronnen/<type>/X.md` = canonieke bron (onaangeroerd)
- `resources/leeshulp/<type>/X.md` = handgeschreven didactische callouts (optioneel)
- `content/bronnen/<type>/X.md` = build-output (bron + callouts geïnjecteerd)

CLI:
    python3 -m tools.leermateriaal.inject_leeshulp inject-all
        → regenereert alle `content/bronnen/normen/*.md` uit bron + (optionele) leeshulp.
        Bronnen zonder bijbehorende leeshulp worden 1-op-1 gekopieerd.

    python3 -m tools.leermateriaal.inject_leeshulp check
        → exit-code 1 als ten minste één `content/`-versie out-of-sync is met
        `inject(bron, leeshulp)`. Bedoeld als pre-commit / CI-gate.

Leeshulp-anchor-syntax (in `resources/leeshulp/...`):
    ## @intro                      — callout vóór de eerste H1 (na frontmatter)
    ## @na "## 2. Verslag"         — callout NA de sectie gestart door deze heading,
                                     d.w.z. vóór de volgende heading van gelijk/hoger niveau
                                     (of aan EOF als er geen volgende heading meer is).

Bij meerdere occurrences van dezelfde heading: eerste match wordt gebruikt. Bij
conflict: leeshulp-auteur moet uniciteit afdwingen (bv. heading hernoemen in
bron is geen optie — heading-arg vervolledigen tot uniek prefix).

Scope v1: enkel `normen/`. Wetteksten (kb's, codices) zijn ordes van grootte
groter en hebben mogelijk een ander callout-patroon nodig — niet in v1.
"""

from __future__ import annotations

import argparse
import difflib
import re
import sys
from dataclasses import dataclass
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
BRONNEN_ROOT = REPO_ROOT / "resources" / "bronnen"
LEESHULP_ROOT = REPO_ROOT / "resources" / "leeshulp"
CONTENT_ROOT = REPO_ROOT / "content" / "bronnen"

# Welke bron-types worden geïnjecteerd (v1: enkel normen)
SUPPORTED_TYPES = ("normen",)

ANCHOR_RE = re.compile(r'^##\s+@(\w+)(?:\s+"([^"]+)")?\s*$')


# ────────────────────────────────────────────────────────────────────────────
# Markdown utilities
# ────────────────────────────────────────────────────────────────────────────


def split_frontmatter(text: str) -> tuple[str, str]:
    """Splits markdown text in (frontmatter_block_incl_delimiters, body).

    Frontmatter wordt herkend als `---\\n...\\n---\\n` aan het begin van het
    bestand. Het delimiter-blok blijft inclusief de afsluitende `---\\n`.
    """
    if not text.startswith("---\n"):
        return "", text
    lines = text.split("\n")
    if lines[0] != "---":
        return "", text
    for i in range(1, len(lines)):
        if lines[i] == "---":
            fm = "\n".join(lines[: i + 1]) + "\n"
            body = "\n".join(lines[i + 1 :])
            return fm, body
    return "", text


def _heading_level(line: str) -> int:
    """Geeft het ATX-heading-niveau (1-6) of 0 als geen heading."""
    if not line.startswith("#"):
        return 0
    stripped = line.lstrip("#")
    level = len(line) - len(stripped)
    if level > 6:
        return 0
    if stripped and not stripped.startswith(" "):
        return 0
    return level


# ────────────────────────────────────────────────────────────────────────────
# Leeshulp-parser
# ────────────────────────────────────────────────────────────────────────────


@dataclass(frozen=True)
class Callout:
    directive: str           # "intro" of "na"
    arg: str | None          # bv. '## 2. Verslag' bij @na; None bij @intro
    body: str                # de callout-tekst zelf (zonder de `## @`-heading)


def parse_leeshulp(text: str) -> list[Callout]:
    """Parse een leeshulp-bestand naar een geordende lijst Callout-records.

    Alles vóór de eerste `## @<directive>`-heading wordt genegeerd (intro-prose
    van het leeshulp-bestand zelf).
    """
    _, body = split_frontmatter(text)
    sections: list[tuple[str, str | None, list[str]]] = []
    current: tuple[str, str | None, list[str]] | None = None

    for line in body.split("\n"):
        m = ANCHOR_RE.match(line)
        if m:
            if current is not None:
                sections.append(current)
            current = (m.group(1), m.group(2), [])
        elif current is not None:
            current[2].append(line)

    if current is not None:
        sections.append(current)

    return [
        Callout(directive=d, arg=a, body="\n".join(lines).strip())
        for d, a, lines in sections
    ]


# ────────────────────────────────────────────────────────────────────────────
# Injectie
# ────────────────────────────────────────────────────────────────────────────


def _inject_intro(body: str, callout: str, leeshulp_rel_path: str) -> str:
    """Voegt een intro-callout in vóór de eerste H1, met HTML-marker."""
    marker = f"<!-- LEESHULP-INJECT: bron={leeshulp_rel_path} (ADR-034) -->"
    return f"{marker}\n\n{callout}\n\n{body}"


def _inject_after_section(body: str, heading: str, callout: str) -> str:
    """Voegt een callout in NA de sectie gestart door `heading`.

    Sectie-einde = eerste volgende heading van gelijk/hoger niveau, of EOF.
    """
    target_level = _heading_level(heading)
    if target_level == 0:
        raise ValueError(f"@na-arg moet een ATX-heading zijn: {heading!r}")

    lines = body.split("\n")

    heading_idx: int | None = None
    for i, line in enumerate(lines):
        if line.strip() == heading.strip():
            heading_idx = i
            break
    if heading_idx is None:
        raise ValueError(f"@na-heading niet gevonden in bron: {heading!r}")

    for j in range(heading_idx + 1, len(lines)):
        lvl = _heading_level(lines[j])
        if 0 < lvl <= target_level:
            # Insert vóór deze volgende heading: blank + callout + blank
            return "\n".join(lines[:j] + ["", callout, ""] + lines[j:])

    # EOF-geval: geen volgende heading → callout aan het einde, met één
    # blank line ervoor en één afsluitende newline. Strip eerst trailing blanks.
    while lines and lines[-1] == "":
        lines.pop()
    return "\n".join(lines) + "\n\n" + callout + "\n"


def inject(
    bron_text: str,
    leeshulp_text: str | None,
    leeshulp_rel_path: str | None = None,
) -> str:
    """Combineer bron + leeshulp tot publicatie-versie.

    Als `leeshulp_text` None is, wordt de bron 1-op-1 teruggegeven.
    """
    if leeshulp_text is None:
        return bron_text

    callouts = parse_leeshulp(leeshulp_text)
    if not callouts:
        return bron_text

    fm, body = split_frontmatter(bron_text)

    # @intro wordt altijd eerst toegepast (vóór de heading-zoektocht van @na,
    # zodat @na-headings in de oorspronkelijke bron-sectie zoeken).
    intro = next((c for c in callouts if c.directive == "intro"), None)
    if intro is not None:
        if leeshulp_rel_path is None:
            raise ValueError("@intro vereist een leeshulp_rel_path voor de HTML-marker")
        body = _inject_intro(body, intro.body, leeshulp_rel_path)

    for callout in callouts:
        if callout.directive == "intro":
            continue
        if callout.directive == "na":
            if callout.arg is None:
                raise ValueError("@na-directive vereist een heading-argument")
            body = _inject_after_section(body, callout.arg, callout.body)
            continue
        raise ValueError(f"Onbekend leeshulp-directive: @{callout.directive}")

    return fm + body


# ────────────────────────────────────────────────────────────────────────────
# Filesystem-driver
# ────────────────────────────────────────────────────────────────────────────


def _read(path: Path) -> str | None:
    if not path.exists():
        return None
    return path.read_text(encoding="utf-8")


def _bronnen_paden(bron_type: str, only_with_leeshulp: bool = True) -> list[Path]:
    """Lijst bron-paden voor een type.

    Default scope (v1): alleen bronnen waarvoor een `resources/leeshulp/<type>/X.md`
    bestaat. Reden: de tool is in POC-fase voor leeshulp-functionaliteit. Bestaande
    drift tussen `resources/bronnen/` en `content/bronnen/` voor bronnen zónder
    leeshulp wordt apart aangepakt (zie ADR-034 §Open punten — "drift-opkuis
    bronnen zonder leeshulp").

    Met `only_with_leeshulp=False` werkt de tool op álle bronnen — bron-only
    bestanden worden 1-op-1 gekopieerd, leeshulp-bestanden worden geïnjecteerd.
    """
    root = BRONNEN_ROOT / bron_type
    if not root.exists():
        return []
    # Sluit INDEX.md + keywords/ uit — die zijn geen bronnen-content
    bronnen = [
        p for p in root.glob("*.md")
        if p.name != "INDEX.md" and not p.name.startswith("WETTEKSTEN-")
    ]
    if only_with_leeshulp:
        bronnen = [
            p for p in bronnen
            if (LEESHULP_ROOT / bron_type / p.name).exists()
        ]
    return sorted(bronnen)


def _expected_content(bron_path: Path) -> str:
    bron_type = bron_path.parent.name
    rel = bron_path.relative_to(BRONNEN_ROOT)
    leeshulp_path = LEESHULP_ROOT / rel
    bron_text = bron_path.read_text(encoding="utf-8")
    leeshulp_text = _read(leeshulp_path)
    leeshulp_rel = (
        str(leeshulp_path.relative_to(REPO_ROOT)) if leeshulp_text is not None else None
    )
    return inject(bron_text, leeshulp_text, leeshulp_rel)


def cmd_inject_all(only_with_leeshulp: bool = True) -> int:
    written = 0
    skipped = 0
    for bron_type in SUPPORTED_TYPES:
        for bron_path in _bronnen_paden(bron_type, only_with_leeshulp=only_with_leeshulp):
            expected = _expected_content(bron_path)
            content_path = CONTENT_ROOT / bron_path.relative_to(BRONNEN_ROOT)
            content_path.parent.mkdir(parents=True, exist_ok=True)
            current = _read(content_path)
            if current == expected:
                skipped += 1
                continue
            content_path.write_text(expected, encoding="utf-8")
            print(f"  geschreven: {content_path.relative_to(REPO_ROOT)}")
            written += 1
    print(f"\nKlaar — {written} geschreven, {skipped} ongewijzigd.")
    return 0


def cmd_check(only_with_leeshulp: bool = True) -> int:
    """Exit 1 als ten minste één content/-versie out-of-sync is."""
    stale: list[tuple[Path, str, str]] = []
    for bron_type in SUPPORTED_TYPES:
        for bron_path in _bronnen_paden(bron_type, only_with_leeshulp=only_with_leeshulp):
            expected = _expected_content(bron_path)
            content_path = CONTENT_ROOT / bron_path.relative_to(BRONNEN_ROOT)
            current = _read(content_path)
            if current != expected:
                stale.append((content_path, current or "", expected))

    if not stale:
        return 0

    print(
        f"\n⚠️  {len(stale)} content/-versie(s) out-of-sync met inject(bron, leeshulp):\n",
        file=sys.stderr,
    )
    for path, current, expected in stale:
        print(f"  ✗ {path.relative_to(REPO_ROOT)}", file=sys.stderr)
        # Eerste paar regels diff voor diagnose
        diff = list(
            difflib.unified_diff(
                current.splitlines(keepends=True),
                expected.splitlines(keepends=True),
                fromfile="on-disk",
                tofile="expected",
                n=1,
            )
        )
        for line in diff[:12]:
            print(f"    {line}", end="", file=sys.stderr)
        if len(diff) > 12:
            print(f"    ... ({len(diff) - 12} regels diff niet getoond)", file=sys.stderr)
        print(file=sys.stderr)

    print(
        "\nFix: python3 -m tools.leermateriaal.inject_leeshulp inject-all",
        file=sys.stderr,
    )
    return 1


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Leeshulp-injectie voor bron-publicaties (ADR-034)."
    )
    sub = parser.add_subparsers(dest="cmd", required=True)
    p_inject = sub.add_parser("inject-all", help="Regenereer content/bronnen/-versies.")
    p_check = sub.add_parser("check", help="Exit 1 als out-of-sync.")
    for p in (p_inject, p_check):
        p.add_argument(
            "--all",
            action="store_true",
            help="Ook bronnen ZONDER leeshulp meenemen (1-op-1 kopie). "
                 "Default: alleen bronnen met leeshulp.",
        )

    args = parser.parse_args(argv)
    only_with_leeshulp = not args.all

    if args.cmd == "inject-all":
        return cmd_inject_all(only_with_leeshulp=only_with_leeshulp)
    if args.cmd == "check":
        return cmd_check(only_with_leeshulp=only_with_leeshulp)
    return 2


if __name__ == "__main__":
    sys.exit(main())
