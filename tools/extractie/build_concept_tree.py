#!/usr/bin/env python3
"""Parse docs/granulariteit-skelet.md to a structured concept-tree JSON.

Output: data/concepten/concept-tree.json (canonical concept-tree).

Strategy:
1. Parse the compact top-level snapshot (lines 16-34 = discipline-stam + lines 38-297 = clusters).
2. Within each tree-snapshot, parse line-by-line using indentation depth.
3. Map cluster trees to their parent discipline based on a hand-curated cluster→discipline map.
4. Validate each node-id against data/concepten/records/<id>.json.
5. Report orphans (records on disk but not in tree) + virtual (in tree but no record).
"""
from __future__ import annotations

import json
import re
from pathlib import Path

ROOT = Path("/Users/stivni/Development/certificaid")
SKELET = ROOT / "docs/granulariteit-skelet.md"
RECORDS_DIR = ROOT / "data/concepten/records"
OUT = ROOT / "data/concepten/concept-tree.json"


# Cluster name (top-level entry in compact snapshot) → parent discipline
# Sub-disciplines under fiscaliteit are *not* in this map — they are sub-disciplines, not clusters.
# Sub-Kaders under controle are listed as clusters under controle.
CLUSTER_TO_DISCIPLINE = {
    # cross-cutting / multi-discipline clusters → primary discipline
    "mobiliteit": "fiscaliteit",  # primarily PB/VAA but cross-cutting; per skelet nav-table PO 2.1
    "kapitaalstructuur": "vennootschapsrecht",  # PO 3.0 + 1.1 + 2.3
    "werknemers-vergoedingen": "fiscaliteit",  # PO 2.1 + 2.3
    "overdracht-onderneming": "vennootschapsrecht",  # PO 3.0 + 2.3 + 2.7
    "schuldfinanciering": "boekhouding",  # PO 1.1 + 3.0 + 2.3
    "reorganisatie": "vennootschapsrecht",  # PO 3.0 + 2.3 + 2.8 + 1.4
    "fiscale-voordelen-vennootschap": "fiscaliteit",  # PO 2.3
    "anti-misbruik": "fiscaliteit",  # PO 2.1 + 2.8
    "controle-opdracht": "controle",  # sub-Kader
    "bestuur-en-aansprakelijkheid": "vennootschapsrecht",
    "vennootschapsgeschillen": "vennootschapsrecht",
    "insolventie": "vennootschapsrecht",
    "ondernemingsvormen": "vennootschapsrecht",
    "interne-controle": "controle",
    "bedrijfsadvies": "bedrijfseconomie-en-management",
    "management-accounting": "bedrijfseconomie-en-management",
    "consolidatie": "boekhouding",
    "ifrs-rapportering": "boekhouding",
    "financiele-analyse": "bedrijfseconomie-en-management",
    "boekhouding": "boekhouding",  # discipline-cluster (records under boekhouding-discipline)
    "btw": "fiscaliteit",  # sub-discipline cluster
    "vennootschapsbelasting": "fiscaliteit",
    "personenbelasting": "fiscaliteit",
    "beroepsbeoefening": "beroep-en-deontologie",
    "winstuitkering": "vennootschapsrecht",  # PO 3.0.IV.B + cross 2.3 + 2.1
    "loon-en-payroll": "fiscaliteit",  # K-techniek cross PO 2.1 + werknemers-vergoedingen
    "bijzondere-mandaten": "controle",
    "fiscale-procedure": "fiscaliteit",
    "internationaal-fiscaal": "fiscaliteit",
    "algemene-fiscale-beginselen": "fiscaliteit",
    "controle-shared": "controle",
    "beoordelings-opdracht": "controle",
    "isae-opdrachten": "controle",
    "overeengekomen-procedures": "controle",
    # Shared records — placed under controle as cross-cluster
    "Shared records (thema's `controle-opdracht` + `interne-controle` + `beroepsbeoefening`)": "controle",
}

# Sub-discipline clusters (live under fiscaliteit as subdiscipline entries)
FISCALITEIT_SUBDISCIPLINES = {
    "personenbelasting",
    "vennootschapsbelasting",
    "btw",
    "registratie-en-successierechten",
    "lokale-en-regionale-belastingen",
}

# Sub-Kaders of controle (live as clusters under controle discipline; but the discipline-stam lists them)
CONTROLE_SUBKADERS = {
    "controle-opdracht",
    "beoordelings-opdracht",
    "isae-opdrachten",
    "overeengekomen-procedures",
    "interne-controle",
    "bijzondere-mandaten",
}

DISCIPLINES = [
    "boekhouding",
    "fiscaliteit",
    "controle",
    "vennootschapsrecht",
    "beroep-en-deontologie",
    "bedrijfseconomie-en-management",
]


# ──────────────────────────────────────────────────────────────────────────────
# Tree-line parsing
# ──────────────────────────────────────────────────────────────────────────────

# match a line like:
#   ├── name                              [K]   *annotatie*
#   └── name                              [G+R]   └── sub-record (single-record inline)
#   │   └── sub-name                      [R]
# Or root-level lines:
#   name                                  [K]
TREE_PREFIX_RE = re.compile(
    r"""^
    (?P<indent>(?:[│ ]{1,4})*)        # vertical-bars/spaces for depth
    (?:(?P<connector>├──|└──)\s+)?    # optional connector
    (?P<rest>.*)$
    """,
    re.VERBOSE,
)

# Extract [tag] from rest of line
TAG_RE = re.compile(r"\[([^\]]+)\]")

# Slug pattern — record-name should be letters/digits/dashes, at least 2 chars,
# must contain at least one letter (rejects pure numbers like "3" or "5")
NAME_TOKEN_RE = re.compile(r"^([a-z][a-z0-9-]+|[a-z0-9]+-[a-z0-9-]+)(?=\s|$|\[|·|,)")

# Inline sub-record indicator: "└── sub-name [tag]" appearing later in the same line
INLINE_SUB_RE = re.compile(r"└──\s+([a-z0-9][a-z0-9-]+)\s*(?:\[([^\]]+)\])?")

# Skip lines that are pure section markers like "├── --- I. SECTION ---"
SECTION_MARKER_RE = re.compile(r"---\s*[IVX]+\.")

# Skip lines that contain only ▸ items (sub-sections, not records)
ARROW_PREFIX_RE = re.compile(r"^\s*▸")

# Lines like "(meerwaarde-aandelen-venb)" or "(loon-werknemer)" — parenthesised → cross-ref placeholder, skip
PARENTHESISED_RE = re.compile(r"^\s*\(.*\)\s*(?:TBD|⏳|→|$)")


def parse_indent(indent_str: str) -> int:
    """Return depth (0 = root) from indent prefix."""
    # Each level of indent is roughly 4 chars (│   ) or pure space. Normalize.
    # Count "│" + leading spaces in units of 4.
    if not indent_str:
        return 0
    # Strip trailing single space if present
    s = indent_str.rstrip()
    # Each "│   " or "    " is one indent level (4 chars in box-drawing)
    return len(s) // 4 + (1 if len(s) % 4 else 0)


def extract_tags(text: str) -> list[str]:
    """Extract category tags from `[X]` or `[X, Y]` patterns. Returns first bracket's contents split."""
    m = TAG_RE.search(text)
    if not m:
        return []
    inner = m.group(1)
    # Split on comma / "+" / spaces? Typically " [K]" or "[E+R]" or "[K, Σ]" or "[R, ⏳ NIEUW]"
    # We want categorieen as the canonical category-letters; everything else (Σ, ⏳ NIEUW, NIEUW) is flag.
    return [t.strip() for t in re.split(r"[,+]", inner) if t.strip()]


def parse_tags(tags: list[str]) -> tuple[list[str], dict]:
    """Separate canonical categories (K/E/G/R) from flags (Σ, ⏳, NIEUW, etc.)."""
    cats = []
    flags: dict = {"is_sigma": False, "is_kandidaat": False, "annotaties": []}
    for raw in tags:
        # Strip whitespace and common modifiers
        norm = raw.strip()
        if not norm:
            continue
        # Category letters: K, E, G, R (may have suffix like "K-techniek", "E-orgaan", "E-instrument")
        first_word = norm.split("-")[0].split()[0]
        if first_word in {"K", "E", "G", "R"}:
            cats.append(first_word)
        elif norm == "Σ" or "Σ" in norm:
            flags["is_sigma"] = True
            if norm != "Σ":
                flags["annotaties"].append(norm)
        elif "⏳" in norm:
            flags["is_kandidaat"] = True
            if norm.strip() not in {"⏳", "⏳ NIEUW", "NIEUW"}:
                flags["annotaties"].append(norm)
        else:
            flags["annotaties"].append(norm)
    return cats, flags


def parse_record_line(line: str) -> dict | None:
    """Parse a single tree-snapshot line.

    Returns:
        {
          'depth': int,
          'id': str,
          'categorieen': list[str],
          'flags': dict,
          'annotatie': str,
          'inline_sub': str | None,  # inline child id like "└── kapitaalverhoging-in-natura"
        }
        Or None if the line should be skipped.
    """
    line = line.rstrip()
    if not line.strip():
        return None
    # Skip section markers
    if SECTION_MARKER_RE.search(line):
        return None
    if ARROW_PREFIX_RE.match(line):
        return None
    if PARENTHESISED_RE.match(line):
        return None
    # Skip lines that don't contain a record-like slug
    m = TREE_PREFIX_RE.match(line)
    if not m:
        return None
    indent = m.group("indent") or ""
    connector = m.group("connector")
    rest = m.group("rest").strip()
    if not rest:
        return None

    # If there's indent but no connector, it's an annotation-continuation line, not a record line.
    if indent and not connector:
        return None

    # Depth: indent-depth + (1 if connector else 0)
    base_depth = parse_indent(indent)
    depth = base_depth + (1 if connector else 0)

    # Parse out name from rest
    name_m = NAME_TOKEN_RE.match(rest)
    if not name_m:
        return None
    rec_id = name_m.group(1)
    after_name = rest[name_m.end():]

    # Extract tags
    tags_raw = extract_tags(after_name)
    cats, flags = parse_tags(tags_raw)

    # Detect multiple records on same line separated by " · "
    # e.g. "kinderen-ten-laste · huwelijksquotient · belastingvrije-som   [R/R/R]"
    # Only treat as multi if the section BEFORE the first "[" tag is a *clean* slug list
    # (only slugs, spaces and ·). Otherwise the · separators are inside prose annotation.
    extra_ids: list[str] = []
    pre_tag = after_name
    tag_pos = pre_tag.find("[")
    if tag_pos >= 0:
        pre_tag = pre_tag[:tag_pos]
    # Check if pre_tag is a clean slug-only list separated by ·
    pre_tag_stripped = pre_tag.strip()
    if pre_tag_stripped and "·" in pre_tag_stripped:
        # Test: split on · and confirm every chunk is a clean slug (letters/digits/dashes only)
        chunks = [c.strip() for c in pre_tag_stripped.split("·")]
        slug_re = re.compile(r"^[a-z0-9][a-z0-9-]+$")
        if all(slug_re.match(c) for c in chunks):
            # First chunk is rec_id (already captured); the rest are extras
            extra_ids = chunks[1:]

    # Annotation: text after [tag] block(s), excluding inline-sub
    # Detect inline sub-record (└── sub-name [tag]) embedded in same line
    inline_sub = None
    inline_m = INLINE_SUB_RE.search(after_name)
    if inline_m:
        inline_sub = inline_m.group(1)

    # Annotation = the rest of the line after stripping tags + inline-sub patterns
    annotatie = after_name
    annotatie = TAG_RE.sub("", annotatie)
    annotatie = INLINE_SUB_RE.sub("", annotatie)
    # Remove leading "· slug" duplicates so annotation doesn't carry them
    if extra_ids:
        # Strip slug · slug · ... prefix from annotation
        annotatie = re.sub(r"^[\s·a-z0-9-]+(?=\[|$)", "", annotatie)
    annotatie = annotatie.strip(" \t*│")
    annotatie = re.sub(r"\s+", " ", annotatie).strip()

    return {
        "depth": depth,
        "id": rec_id,
        "categorieen": cats,
        "flags": flags,
        "annotatie": annotatie,
        "inline_sub": inline_sub,
        "extra_ids": extra_ids,
    }


def parse_tree_block(lines: list[str]) -> list[dict]:
    """Parse a code-block's lines into a flat list of parsed-line dicts (with depth).

    A line with extra_ids (slug-list separated by ' · ') is expanded into multiple
    sibling dicts at the same depth.
    """
    parsed = []
    for line in lines:
        p = parse_record_line(line)
        if p is None:
            continue
        parsed.append(p)
        # Emit extras as sibling entries
        for extra_id in p.get("extra_ids", []):
            extra = {
                "depth": p["depth"],
                "id": extra_id,
                "categorieen": p["categorieen"],  # share the line's tag set
                "flags": dict(p["flags"]),
                "annotatie": p["annotatie"],
                "inline_sub": None,
                "extra_ids": [],
            }
            parsed.append(extra)
    return parsed


def build_node_tree(parsed: list[dict]) -> list[dict]:
    """Convert flat depth-list to nested tree of nodes."""
    nodes: list[dict] = []
    # stack of (depth, node)
    stack: list[tuple[int, dict]] = []

    for p in parsed:
        node = {
            "id": p["id"],
            "categorieen": p["categorieen"],
            "is_sigma": p["flags"]["is_sigma"],
            "is_kandidaat": p["flags"]["is_kandidaat"],
            "annotatie": p["annotatie"],
            "extra_flags": p["flags"]["annotaties"],
            "children": [],
        }
        depth = p["depth"]
        # pop stack until parent depth < current depth
        while stack and stack[-1][0] >= depth:
            stack.pop()
        if not stack:
            nodes.append(node)
        else:
            stack[-1][1]["children"].append(node)
        stack.append((depth, node))

        # Inline-sub: add as child of current node
        if p["inline_sub"]:
            sub_node = {
                "id": p["inline_sub"],
                "categorieen": [],
                "is_sigma": False,
                "is_kandidaat": False,
                "annotatie": "(inline sub-record)",
                "extra_flags": [],
                "children": [],
            }
            node["children"].append(sub_node)
    return nodes


# ──────────────────────────────────────────────────────────────────────────────
# Skeleton-doc parsing
# ──────────────────────────────────────────────────────────────────────────────


def extract_code_blocks(md_text: str) -> list[tuple[str, int, str]]:
    """Extract `(block_content, start_line_number, preceding_header)` for every fenced code block.

    preceding_header = nearest `## ` or `### ` or `#### ` header above the block.
    """
    blocks = []
    lines = md_text.splitlines()
    in_block = False
    start = 0
    buf: list[str] = []
    current_header = ""
    for i, line in enumerate(lines, start=1):
        # Track latest header
        if line.startswith("#") and not in_block:
            stripped = line.lstrip("#").strip()
            current_header = stripped
        if line.strip() == "```":
            if in_block:
                blocks.append(("\n".join(buf), start, current_header))
                buf = []
                in_block = False
            else:
                in_block = True
                start = i + 1
        elif in_block:
            buf.append(line)
    return blocks


def parse_compact_snapshot(text: str) -> dict:
    """Parse the compact top-level snapshot (lines 16-34 disciplines + 38-297 clusters).

    Returns:
        {
          'discipline_stam': [...root nodes...],
          'clusters': [{'name': str, 'tree': [...nodes...]}, ...]
        }
    """
    lines = text.splitlines()
    # The compact snapshot at lines 16-34 is the first one we hit. We split blocks by blank lines.
    # Each cluster starts with a non-indented line and ends at a blank line.
    clusters = []
    current_block: list[str] = []

    for line in lines:
        if not line.strip():
            if current_block:
                clusters.append(current_block)
                current_block = []
        else:
            current_block.append(line)
    if current_block:
        clusters.append(current_block)

    return clusters  # list of cluster-line-groups


# ──────────────────────────────────────────────────────────────────────────────
# Main
# ──────────────────────────────────────────────────────────────────────────────


# Map detailed cluster header → cluster slug (must match compact snapshot cluster name)
HEADER_TO_CLUSTER = {
    "Overdracht-onderneming-cluster": "overdracht-onderneming",
    "Schuldfinanciering-cluster": "schuldfinanciering",
    "Werknemers-vergoedingen-cluster": "werknemers-vergoedingen",
    "Mobiliteit-cluster": "mobiliteit",
    "Kapitaalstructuur-cluster": "kapitaalstructuur",
    "Ondernemingsvormen-cluster": "ondernemingsvormen",
    "Bestuur-en-aansprakelijkheid-cluster": "bestuur-en-aansprakelijkheid",
    "Vennootschapsgeschillen-cluster": "vennootschapsgeschillen",
    "Insolventie-cluster": "insolventie",
    "Winstuitkering-cluster": "winstuitkering",
    "Reorganisatie-cluster": "reorganisatie",
    "Fiscale-voordelen-vennootschap-cluster": "fiscale-voordelen-vennootschap",
    "Anti-misbruik-cluster": "anti-misbruik",
    "Loon-en-payroll-cluster (K-techniek)": "loon-en-payroll",
    "Personenbelasting-cluster": "personenbelasting",
    "Vennootschapsbelasting-cluster": "vennootschapsbelasting",
    "BTW-cluster": "btw",
    "Boekhouding-cluster": "boekhouding",
    "Financiele-analyse-cluster": "financiele-analyse",
    "Consolidatie-cluster": "consolidatie",
    "IFRS-rapportering-cluster": "ifrs-rapportering",
    "Management-accounting-cluster": "management-accounting",
    "Bedrijfsadvies-cluster": "bedrijfsadvies",
    "Beroepsbeoefening-cluster": "beroepsbeoefening",
    "Bijzondere-mandaten-cluster": "bijzondere-mandaten",
    "Controle-opdracht-cluster": "controle-opdracht",
    "Interne-controle-cluster": "interne-controle",
    "Registratie-en-successierechten-cluster": "registratie-en-successierechten",
    "Lokale-en-regionale-belastingen-cluster": "lokale-en-regionale-belastingen",
    "Algemene-fiscale-beginselen-cluster": "algemene-fiscale-beginselen",
    "Internationaal-fiscaal-cluster": "internationaal-fiscaal",
    "Fiscale-procedure-cluster": "fiscale-procedure",
    "Shared records — controle-opdracht ↔ interne-controle": "controle-shared",
    "beoordelings-opdracht (sub-Kader, 1 record)": "beoordelings-opdracht",
    "isae-opdrachten (sub-Kader, 1 record)": "isae-opdrachten",
    "overeengekomen-procedures (sub-Kader, 1 record)": "overeengekomen-procedures",
}

# Additional sub-discipline clusters discovered via detail-headers
EXTRA_FISCALITEIT_CLUSTERS = {
    "algemene-fiscale-beginselen",
    "internationaal-fiscaal",
    "fiscale-procedure",
}


def main():
    md_text = SKELET.read_text(encoding="utf-8")
    blocks = extract_code_blocks(md_text)

    # Block #0 = discipline-stam (lines 16-34)
    # Block #1 = clusters compact snapshot (lines 38-297)
    discipline_block = blocks[0][0]
    cluster_compact_block = blocks[1][0]

    # Parse discipline-stam — it has fiscaliteit + sub-disciplines, controle + sub-Kaders, and other top-level disciplines
    discipline_parsed = parse_tree_block(discipline_block.splitlines())
    discipline_nodes = build_node_tree(discipline_parsed)

    # Build the discipline-skeleton: { discipline_id: { 'categorieen', 'subdisciplines': [], 'clusters': [] } }
    disciplines_skel: dict[str, dict] = {}
    for d in DISCIPLINES:
        disciplines_skel[d] = {
            "id": d,
            "categorieen": ["K"],
            "is_record": (RECORDS_DIR / f"{d}.json").exists(),
            "is_virtual": not (RECORDS_DIR / f"{d}.json").exists(),
            "subdisciplines": [],
            "clusters": [],
        }

    # Walk discipline-stam and find sub-disciplines
    for node in discipline_nodes:
        if node["id"] == "fiscaliteit":
            for child in node["children"]:
                subdisc_id = child["id"]
                if subdisc_id in FISCALITEIT_SUBDISCIPLINES:
                    has_record = (RECORDS_DIR / f"{subdisc_id}.json").exists()
                    disciplines_skel["fiscaliteit"]["subdisciplines"].append(
                        {
                            "id": subdisc_id,
                            "categorieen": child["categorieen"] or ["K"],
                            "is_record": has_record,
                            "is_virtual": not has_record,
                            "clusters": [],
                        }
                    )
        elif node["id"] == "controle":
            # children are sub-Kaders — treat as clusters under controle below
            pass
        # other disciplines don't have sub-discipline structure in the stam

    # Parse cluster-compact snapshot (one big block, but with blank-line separation between clusters)
    cluster_groups = parse_compact_snapshot(cluster_compact_block)

    # Each cluster_group is a list of lines starting with a root (depth=0) line.
    clusters_parsed = []
    for group in cluster_groups:
        parsed = parse_tree_block(group)
        if not parsed:
            continue
        # The first parsed line at depth=0 is the cluster root.
        # But sometimes the first parsed line has tag like [Σ-cluster, 4 records] and is the cluster-name.
        root = parsed[0]
        cluster_name = root["id"]
        # Build nodes within this cluster
        nodes = build_node_tree(parsed)
        clusters_parsed.append({"name": cluster_name, "root": root, "nodes": nodes})

    # Detect the "Shared records" pseudo-cluster in the compact snapshot.
    # It has no canonical root-line that parses; instead the first parsed-line is one of the shared records.
    SHARED_RECORDS_HINTS = {"coso-framework", "cyclus-analyse", "auditcomite", "onafhankelijkheid", "kwaliteitsmanagement-opdracht"}

    # Helper to find cluster by name (defined here so it's available below)
    def _find_cluster_by_name(name: str) -> dict | None:
        for d in disciplines_skel.values():
            for c in d["clusters"]:
                if c["naam"] == name:
                    return c
            for sub in d["subdisciplines"]:
                for c in sub["clusters"]:
                    if c["naam"] == name:
                        return c
        return None

    # Map each cluster to its discipline
    for cluster_data in clusters_parsed:
        cluster_name = cluster_data["name"]
        # If the cluster's first parsed line is a shared-record (no proper root), reframe as controle-shared
        if cluster_name in SHARED_RECORDS_HINTS:
            shared_cluster = _find_cluster_by_name("controle-shared")
            if shared_cluster is None:
                shared_cluster = {
                    "naam": "controle-shared",
                    "skelet_sectie": "shared-records",
                    "annotatie": "Shared records — controle-opdracht ↔ interne-controle ↔ beroepsbeoefening",
                    "nodes": [],
                }
                disciplines_skel["controle"]["clusters"].append(shared_cluster)
            for n in cluster_data["nodes"]:
                shared_cluster["nodes"].append(n)
            continue
        # Determine discipline:
        # 1. If cluster_name is a sub-discipline of fiscaliteit, its 'cluster-tree' becomes a sub-discipline-cluster
        # 2. If cluster_name is a sub-Kader of controle, becomes a cluster under controle
        # 3. Otherwise look up in CLUSTER_TO_DISCIPLINE
        discipline_id = CLUSTER_TO_DISCIPLINE.get(cluster_name)

        if cluster_name in FISCALITEIT_SUBDISCIPLINES:
            # Place this cluster under the matching subdiscipline within fiscaliteit
            target_subdiscs = disciplines_skel["fiscaliteit"]["subdisciplines"]
            sub = next((s for s in target_subdiscs if s["id"] == cluster_name), None)
            if sub is None:
                # Create on the fly if missing from discipline-stam
                has_record = (RECORDS_DIR / f"{cluster_name}.json").exists()
                sub = {
                    "id": cluster_name,
                    "categorieen": ["K"],
                    "is_record": has_record,
                    "is_virtual": not has_record,
                    "clusters": [],
                }
                target_subdiscs.append(sub)
            # The cluster's "nodes" tree — the root IS the sub-discipline; its children are the cluster members.
            cluster_root = cluster_data["nodes"][0]
            # If the cluster-root is itself a record (exists on disk), include it as first node.
            top_nodes = list(cluster_root["children"])
            if (RECORDS_DIR / f"{cluster_root['id']}.json").exists() and cluster_root["id"] not in {c["id"] for c in cluster_root["children"]}:
                # Strip children to avoid duplication: keep root-as-leaf-node
                root_only = {**cluster_root, "children": []}
                top_nodes = [root_only] + top_nodes
            sub["clusters"].append(
                {
                    "naam": cluster_name,
                    "skelet_sectie": f"{cluster_name}-cluster",
                    "annotatie": cluster_data["root"]["annotatie"],
                    "nodes": top_nodes,
                }
            )
        elif cluster_name in CONTROLE_SUBKADERS:
            target = disciplines_skel["controle"]
            cluster_root = cluster_data["nodes"][0]
            children = list(cluster_root["children"])
            top_nodes = children
            if (RECORDS_DIR / f"{cluster_root['id']}.json").exists() and cluster_root["id"] not in {c["id"] for c in children}:
                top_nodes = [{**cluster_root, "children": []}] + children
            target["clusters"].append(
                {
                    "naam": cluster_name,
                    "skelet_sectie": f"{cluster_name}-cluster",
                    "annotatie": cluster_data["root"]["annotatie"],
                    "nodes": top_nodes,
                }
            )
        elif discipline_id and discipline_id in disciplines_skel:
            target = disciplines_skel[discipline_id]
            cluster_root = cluster_data["nodes"][0]
            children = list(cluster_root["children"])
            top_nodes = children
            if (RECORDS_DIR / f"{cluster_root['id']}.json").exists() and cluster_root["id"] not in {c["id"] for c in children}:
                top_nodes = [{**cluster_root, "children": []}] + children
            target["clusters"].append(
                {
                    "naam": cluster_name,
                    "skelet_sectie": f"{cluster_name}-cluster",
                    "annotatie": cluster_data["root"]["annotatie"],
                    "nodes": top_nodes,
                }
            )
        else:
            # Shared records or unrecognized — print warning
            print(f"WARN: cluster '{cluster_name}' has no discipline mapping — skipping")

    # ── Augment with detail-cluster blocks (blocks 2..N) ──
    # Build cluster-lookup for augmentation
    def find_cluster_in_tree(cluster_name: str) -> dict | None:
        for d in disciplines_skel.values():
            for c in d["clusters"]:
                if c["naam"] == cluster_name:
                    return c
            for sub in d["subdisciplines"]:
                for c in sub["clusters"]:
                    if c["naam"] == cluster_name:
                        return c
        return None

    def all_ids_in_cluster(cluster: dict) -> set[str]:
        ids = set()

        def walk(node):
            ids.add(node["id"])
            for ch in node.get("children", []):
                walk(ch)

        for n in cluster["nodes"]:
            walk(n)
        return ids

    # Process every code block (after the first two)
    for block_text, _start, header in blocks[2:]:
        # Only treat as tree-snapshot if it has ├── or └── markers
        if "├──" not in block_text and "└──" not in block_text:
            continue
        cluster_slug = HEADER_TO_CLUSTER.get(header)
        if not cluster_slug:
            continue
        # Find or create cluster
        cluster = find_cluster_in_tree(cluster_slug)
        if cluster is None:
            # Create new cluster in the appropriate discipline
            if cluster_slug in FISCALITEIT_SUBDISCIPLINES:
                # Mount under sub-discipline; create a same-named cluster there
                target_subdiscs = disciplines_skel["fiscaliteit"]["subdisciplines"]
                sub = next((s for s in target_subdiscs if s["id"] == cluster_slug), None)
                if sub is None:
                    has_record = (RECORDS_DIR / f"{cluster_slug}.json").exists()
                    sub = {
                        "id": cluster_slug,
                        "categorieen": ["K"],
                        "is_record": has_record,
                        "is_virtual": not has_record,
                        "clusters": [],
                    }
                    target_subdiscs.append(sub)
                cluster = {
                    "naam": cluster_slug,
                    "skelet_sectie": f"{cluster_slug}-cluster",
                    "annotatie": "",
                    "nodes": [],
                }
                sub["clusters"].append(cluster)
            elif cluster_slug in EXTRA_FISCALITEIT_CLUSTERS:
                # add as cluster directly under fiscaliteit discipline
                cluster = {
                    "naam": cluster_slug,
                    "skelet_sectie": f"{cluster_slug}-cluster",
                    "annotatie": "",
                    "nodes": [],
                }
                disciplines_skel["fiscaliteit"]["clusters"].append(cluster)
            else:
                discipline_id = CLUSTER_TO_DISCIPLINE.get(cluster_slug)
                if not discipline_id:
                    print(f"WARN: detail-cluster '{cluster_slug}' (header '{header}') has no discipline mapping")
                    continue
                cluster = {
                    "naam": cluster_slug,
                    "skelet_sectie": f"{cluster_slug}-cluster",
                    "annotatie": "",
                    "nodes": [],
                }
                disciplines_skel[discipline_id]["clusters"].append(cluster)

        # Parse the detail-block
        parsed = parse_tree_block(block_text.splitlines())
        if not parsed:
            continue
        # Build tree from parsed lines
        detail_nodes = build_node_tree(parsed)
        # Root is the first node (cluster name itself) — its children are the actual records
        if not detail_nodes:
            continue
        # If the first root matches the cluster name, use its children; otherwise treat all as siblings
        root = detail_nodes[0]
        if root["id"] == cluster_slug:
            new_top_nodes = root["children"]
        else:
            new_top_nodes = detail_nodes

        # Merge: only add records (top-level + their children) that aren't already in cluster
        existing_ids = all_ids_in_cluster(cluster)

        def graft(nodes, parent_list):
            for n in nodes:
                if n["id"] in existing_ids:
                    # Recurse into existing node's children to merge sub-children
                    # Find that existing node and graft its missing children
                    for ex in parent_list:
                        if ex["id"] == n["id"]:
                            graft(n["children"], ex["children"])
                            break
                else:
                    parent_list.append(n)
                    existing_ids.add(n["id"])
                    # children added with parent already
                    for ch in n.get("children", []):
                        existing_ids.add(ch["id"])

        graft(new_top_nodes, cluster["nodes"])

    # ── Validate is_record / is_virtual for every node in the tree ──
    all_ids_in_tree: set[str] = set()

    def visit(node: dict):
        rec_path = RECORDS_DIR / f"{node['id']}.json"
        has = rec_path.exists()
        node["is_record"] = has
        node["is_virtual"] = not has
        all_ids_in_tree.add(node["id"])
        for child in node.get("children", []):
            visit(child)

    for disc in disciplines_skel.values():
        all_ids_in_tree.add(disc["id"])
        for sub in disc["subdisciplines"]:
            all_ids_in_tree.add(sub["id"])
            for cluster in sub["clusters"]:
                for node in cluster["nodes"]:
                    visit(node)
        for cluster in disc["clusters"]:
            for node in cluster["nodes"]:
                visit(node)

    # Compute orphan records (records on disk but not in tree)
    all_records_on_disk = {p.stem for p in RECORDS_DIR.glob("*.json")}
    orphans = sorted(all_records_on_disk - all_ids_in_tree)
    virtual_ids = sorted({i for i in all_ids_in_tree if not (RECORDS_DIR / f"{i}.json").exists()})

    # ── Compose output JSON ──
    output = {
        "$schema": "concept-tree-v1",
        "bron": "docs/granulariteit-skelet.md",
        "gegenereerd_op": "2026-05-28",
        "disciplines": [disciplines_skel[d] for d in DISCIPLINES],
    }

    OUT.write_text(json.dumps(output, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")

    # ── Report ──
    n_disc = len(DISCIPLINES)
    n_subdisc = sum(len(d["subdisciplines"]) for d in disciplines_skel.values())
    n_cluster = sum(len(d["clusters"]) for d in disciplines_skel.values()) + sum(
        len(s["clusters"]) for d in disciplines_skel.values() for s in d["subdisciplines"]
    )
    n_nodes = len(all_ids_in_tree)

    print(f"=== concept-tree.json gegenereerd ===")
    print(f"Disciplines:       {n_disc}")
    print(f"Sub-disciplines:   {n_subdisc}")
    print(f"Clusters:          {n_cluster}")
    print(f"Unieke nodes:      {n_nodes}")
    print(f"Virtual nodes:     {len(virtual_ids)}")
    print(f"Orphan records:    {len(orphans)} (= records op disk maar niet in tree)")
    print(f"Records op disk:   {len(all_records_on_disk)}")
    print()
    print(f"=== Sample virtual nodes (eerste 20) ===")
    for v in virtual_ids[:20]:
        print(f"  - {v}")
    print()
    print(f"=== Sample orphans (eerste 30) ===")
    for o in orphans[:30]:
        print(f"  - {o}")


if __name__ == "__main__":
    main()
