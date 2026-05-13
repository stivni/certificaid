r"""Transformer: reorder cluster van headings die achter hun body verschijnen.

Pdftotext-extractie van 2-koloms PDFs (zoals EU-Richtlijn-witwassen) kan
een rij van artikel-headings concentreren ACHTER de bijbehorende body:

  ... [Art. 4 body paragraaf] ...

  1. ... [Art. 5 body lid 1] ...
  2. ... [Art. 5 body lid 2] ...
  3. ... [Art. 5 body lid 3] ...

  1. ... [Art. 6 body lid 1] ...
  ...

  1. ... [Art. 7 body lid 1] ...
  a) ... [Art. 7 body letter a] ...

  ###### Artikel 4
  Medeplichtigheid, uitlokking en poging
  ###### Artikel 5
  Sancties voor natuurlijke personen
  ###### Artikel 6
  Verzwarende omstandigheden
  ###### Artikel 7
  Aansprakelijkheid van rechtspersonen

Heuristiek:
1. Detecteer cluster van ≥3 consecutive `###### Artikel N` headings (alleen blanco's
   en eventuele 'subtitle' regels tussen — geen body-content).
2. Walk back to find N paragraph-blocks (door blanco-regels gescheiden).
3. Voor elk blok: prepend het bijbehorende heading.
4. Strip de oorspronkelijke cluster.

Conservatief: alleen wanneer
- Cluster heeft ≥3 headings, allemaal op zelfde level
- Headings zijn sequentieel genummerd (Art. N, N+1, N+2, ...)
- N paragraph-blocks voor cluster zijn vindbaar

Conform ADR-005 §1: format-agnostische tekst-transformatie.
"""
from __future__ import annotations

import re

_HEADING_RE = re.compile(r"^(?P<prefix>#{2,6})\s+(?:Artikel|Art\.)\s+(?P<num>\d+)\s*$")


def reorder_heading_cluster(body: str, frontmatter: dict) -> tuple[str, dict]:
    """Reorder cluster van artikel-headings achter hun body naar voren."""
    lines = body.split("\n")
    n = len(lines)
    out_lines = lines[:]

    # Vind clusters: ≥3 consecutive headings (met blanco's of korte subtitle-lines
    # tussen — max 2 non-heading non-blank regels tussen).
    i = 0
    while i < n:
        line = out_lines[i]
        m = _HEADING_RE.match(line)
        if m:
            cluster_start = i
            cluster_headings: list[tuple[int, str, int]] = [(i, m.group("prefix"), int(m.group("num")))]
            j = i + 1
            same_level = m.group("prefix")
            while j < n:
                nxt = out_lines[j]
                nm = _HEADING_RE.match(nxt)
                if nm and nm.group("prefix") == same_level:
                    cluster_headings.append((j, nm.group("prefix"), int(nm.group("num"))))
                    j += 1
                elif not nxt.strip():
                    j += 1
                elif len(cluster_headings) >= 1 and j - cluster_headings[-1][0] <= 2:
                    # Korte subtitle-regel direct na een heading — accepteer.
                    j += 1
                else:
                    break

            # Eindigt cluster met ≥3 headings + sequentiele nummering?
            if len(cluster_headings) >= 3:
                nums = [h[2] for h in cluster_headings]
                if all(nums[k + 1] == nums[k] + 1 for k in range(len(nums) - 1)):
                    cluster_end = cluster_headings[-1][0]
                    # Subtitle: tussen heading-idx en volgende heading-idx, eventuele
                    # non-blank regel die de heading-titel beschrijft.
                    subtitles: dict[int, str] = {}
                    for k, (hidx, _, _) in enumerate(cluster_headings):
                        # Vind eerste non-blank regel na deze heading (binnen cluster).
                        # Voor de laatste heading: zoek vooruit max 3 regels.
                        if k + 1 < len(cluster_headings):
                            search_end = cluster_headings[k + 1][0]
                        else:
                            search_end = min(hidx + 4, len(out_lines))
                        for q in range(hidx + 1, search_end):
                            s = out_lines[q].strip()
                            if s:
                                # Subtitle moet kort genoeg zijn (<100 chars) en geen heading
                                if len(s) < 100 and not s.startswith("#") and not s.startswith(("1.", "a)", "b)", "2.", "3.")):
                                    subtitles[hidx] = s
                                break

                    # Walk back N paragraph-blocks vanaf cluster_start
                    # Een paragraph-block: groep non-blanke regels gescheiden door blank-lines.
                    block_starts: list[int] = []
                    k = cluster_start - 1
                    # Skip leading blanks
                    while k >= 0 and not out_lines[k].strip():
                        k -= 1
                    needed = len(cluster_headings)
                    current_block_end = k
                    while k >= 0 and len(block_starts) < needed:
                        if not out_lines[k].strip():
                            # Begin van blok is k+1
                            block_starts.append(k + 1)
                            # Skip dit blank, search verder
                            kk = k
                            while kk >= 0 and not out_lines[kk].strip():
                                kk -= 1
                            # Now kk is end of previous block
                            k = kk
                        else:
                            k -= 1
                    if len(block_starts) >= needed:
                        block_starts.append(k + 1)  # eerste blok-start (oudste)
                        # block_starts is in reverse: youngest first
                        block_starts.reverse()
                        block_starts = block_starts[-needed:]
                        # Insert headings at block_starts (reverse order to keep indices)
                        new_lines: list[str] = []
                        skip_range_start = cluster_start
                        # Skip ook subtitle van de laatste heading (komt na cluster_end)
                        last_heading_idx = cluster_headings[-1][0]
                        last_subtitle = subtitles.get(last_heading_idx, "")
                        skip_range_end = cluster_end + 1
                        if last_subtitle:
                            # Vind de exacte line-index van de laatste subtitle
                            for q in range(cluster_end + 1, min(cluster_end + 4, len(out_lines))):
                                if out_lines[q].strip() == last_subtitle:
                                    skip_range_end = q + 1
                                    break
                        # Build new body: replicate originele lines, met heading-injectie
                        # bij elk block_start en skipping van [skip_range_start..skip_range_end).
                        # Bouw ook reverse-lookup voor block-start.
                        block_to_heading = {
                            block_starts[k]: cluster_headings[k]
                            for k in range(needed)
                        }
                        idx = 0
                        while idx < n:
                            if idx in block_to_heading:
                                hidx_info = block_to_heading[idx]
                                prefix = hidx_info[1]
                                num = hidx_info[2]
                                subtitle = subtitles.get(hidx_info[0], "")
                                if subtitle:
                                    new_lines.append(f"{prefix} Artikel {num} — {subtitle}")
                                else:
                                    new_lines.append(f"{prefix} Artikel {num}")
                                new_lines.append("")
                            if skip_range_start <= idx < skip_range_end:
                                idx += 1
                                continue
                            new_lines.append(out_lines[idx])
                            idx += 1
                        out_lines = new_lines
                        # Restart scanning from a safe point after the changes
                        n = len(out_lines)
                        i = cluster_end + 1
                        continue
        i += 1

    new_body = "\n".join(out_lines)
    new_body = re.sub(r"\n{3,}", "\n\n", new_body)
    return new_body, frontmatter
