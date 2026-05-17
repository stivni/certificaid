"""Tests voor tools/lib/cbn_advies_html.py."""
from __future__ import annotations

from tools.lib.cbn_advies_html import select_title, _promote_implicit_headings, _cleanup_markdown


def test_select_title_strip_commissie_prefix():
    text = (
        "COMMISSIE VOOR BOEKHOUDKUNDIGE NORMEN "
        "CBN-advies 2022/15 - Bla bla "
        "Advies van 1 januari 2022"
    )
    result = select_title(text)
    assert "COMMISSIE" not in result
    assert "Advies van" not in result
    assert "CBN-advies 2022/15" in result or "Bla bla" in result


# ─── _promote_implicit_headings — italic standalone heading-promotie ──────────

def test_promote_italic_standalone_long():
    """REGRESSIE-FIX: een lange italic-standalone-regel tussen blank lines
    is een Q&A-titel die als ## heading geprommoveerd moet worden.

    Voorbeeld uit CBN-Q&A-adviezen:
        *Vragen in verband met de vaststelling van de aanschaffingswaarde*
    """
    md = (
        "Body voor.\n"
        "\n"
        "*Vragen in verband met de vaststelling van de aanschaffingswaarde*\n"
        "\n"
        "Body na.\n"
    )
    result = _promote_implicit_headings(md)
    assert "## Vragen in verband met de vaststelling van de aanschaffingswaarde" in result
    assert "*Vragen in verband" not in result  # italic-marker is weg


def test_promote_italic_short_not_promoted():
    """Korte italic (< 20 chars) blijft inline italic — niet promoveren."""
    md = "Body.\n\n*kort*\n\nMeer body.\n"
    result = _promote_implicit_headings(md)
    assert "## kort" not in result
    assert "*kort*" in result


def test_promote_italic_in_paragraph_not_promoted():
    """Italic die NIET tussen lege regels staat (inline emphasis) blijft."""
    md = (
        "Een zin met *emphasis op een woord langer dan twintig chars* in body.\n"
    )
    result = _promote_implicit_headings(md)
    assert "## " not in result


def test_promote_italic_with_trailing_period_not_promoted():
    """Italic met zin-einde-punt is geen heading."""
    md = "\n*Dit is een hele zin die eindigt met een punt.*\n\n"
    result = _promote_implicit_headings(md)
    # Mag niet als heading geprommoveerd worden (heeft zin-einde)
    assert "## Dit is een hele zin" not in result


def test_promote_italic_preserves_legitimate_bold():
    """Bestaande bold-promotie blijft werken (geen regressie)."""
    md = "\n**Boekhoudkundige verwerking**\n\nBody.\n"
    result = _promote_implicit_headings(md)
    assert "## Boekhoudkundige verwerking" in result


# ─── B4 ALL-CAPS heading-promotie ─────────────────────────────────────────────

def test_promote_allcaps_standalone_long():
    """REGRESSIE-FIX (CBN-0100, CBN-0152-01, CBN-2024-09): ALL-CAPS regel
    tussen blank lines met ≥2 woorden wordt ## heading.
    """
    md = "Body.\n\nDE ZIEKENHUIZEN DIE AFHANGEN VAN DE OCMW\n\nMeer body.\n"
    result = _promote_implicit_headings(md)
    assert "## DE ZIEKENHUIZEN DIE AFHANGEN VAN DE OCMW" in result


def test_promote_allcaps_short_acronym_not_promoted():
    """Korte ALL-CAPS afkortingen (VZW, OCMW, BV) blijven inline."""
    md = "Body.\n\nVZW\n\nMeer body.\n"
    result = _promote_implicit_headings(md)
    assert "## VZW" not in result


def test_promote_allcaps_inline_not_promoted():
    """ALL-CAPS midden in paragraph (geen blank lines rondom) blijft inline."""
    md = "Een paragraaf met DE OCMW vermelding\nin de tekst.\n"
    result = _promote_implicit_headings(md)
    assert "## " not in result


def test_promote_allcaps_single_word_not_promoted():
    """Single-word ALL-CAPS (zelfs lang) wordt niet als heading gepromoot."""
    md = "Body.\n\nNORMALISATIETERMIJN\n\nMeer body.\n"
    result = _promote_implicit_headings(md)
    # Single word → no heading (vermijdt false positives op term-definities)
    assert "## NORMALISATIETERMIJN" not in result


# ─── D3-SP3: standalone adjacent footnote refs strippen ─────────────────────

def test_cleanup_strips_four_adjacent_footnote_refs_on_standalone_line():
    """D3-SP3: een regel die enkel uit 4+ aaneengesloten [^N]-markers bestaat
    is een floating ETL-artefact (de refs zijn uit hun inline-context gerukt).
    De cleanup moet ze verwijderen — de definitie blijft onderaan in de
    footnotes-sectie.

    Voorbeeld: CBN-2012-13 r.198 ' [^13][^14][^15][^16]' (4 markers).
    """
    md = (
        "## Voorbeeld op het ogenblik van onderzoek\n"
        "\n"
        " [^13][^14][^15][^16]\n"
        "\n"
        "| | Rekening | Debet | Credit |\n"
        "|---|---------|-------|--------|\n"
        "| | 61 | 12.000 | |\n"
        "\n"
        "[^13]: Er wordt uitgegaan van een werkgeversbijdrage van 32%.\n"
        "[^14]: Het nettoloon is gelijk aan...\n"
        "[^15]: In dit voorbeeld wordt uitgegaan van 35% bedrijfsvoorheffing.\n"
        "[^16]: Werknemersbijdrage 13% van het brutoloon.\n"
    )
    result = _cleanup_markdown(md)
    # Standalone ref-regel moet verdwenen zijn
    assert " [^13][^14][^15][^16]" not in result
    # Footnote-definities onderaan moeten bewaard blijven
    assert "[^13]:" in result
    assert "[^14]:" in result


def test_cleanup_strips_two_adjacent_footnote_refs_on_standalone_line():
    """D3-SP3: ook 1-3 aangrenzende refs op een eigen regel worden gestript
    (bestaand gedrag; geen regressie door de uitbreiding).
    """
    md = "Heading.\n\n [^1][^2]\n\nBody.\n\n[^1]: Definitie een.\n[^2]: Definitie twee.\n"
    result = _cleanup_markdown(md)
    assert " [^1][^2]" not in result
    assert "[^1]:" in result


# ─── B4-SP2: bold Boeking-headings promotie ──────────────────────────────────

def test_promote_bold_boeking_short():
    """B4-SP2: '**Boeking eerste jaar**' (19 chars, onder 20-char drempel) moet
    als ## heading worden gepromoveerd — dit zijn subsectie-labels in CBN-adviezen
    die de ETL als bold uitlevert i.p.v. als heading.

    Voorbeeld: CBN-2013-06 r.66 '**Boeking eerste jaar**' staat naast
    '## Boeking in het jaar...' — inconsistente behandeling is ETL-artefact.
    """
    md = (
        "Body tekst.\n"
        "\n"
        "**Boeking eerste jaar**\n"
        "\n"
        "| | Rekening | Omschrijving | Debet | Credit |\n"
        "|---|----------|--------------|-------|--------|\n"
        "| | 640 | Bedrijfsbelastingen | 1,75 | |\n"
    )
    result = _promote_implicit_headings(md)
    assert "## Boeking eerste jaar" in result
    assert "**Boeking eerste jaar**" not in result


def test_promote_bold_boeking_with_footnote_in_text():
    """B4-SP2: 'Boeking op datum[^N]...' met ingebedde footnote-ref mag ook
    gepromoveerd worden — de footnote-marker maakt het geen zin.

    Voorbeeld: CBN-2016-13 r.102 '**Boeking op 31/03/2013 (...25[^10] procent)**'
    """
    md = (
        "Body.\n"
        "\n"
        "**Boeking op 31/03/2013 (tarief roerende voorheffing bedraagt 25[^10] procent)**\n"
        "\n"
        "| | col | Debet | Credit |\n"
        "|---|-----|-------|--------|\n"
        "| | 520 | 201 | |\n"
    )
    result = _promote_implicit_headings(md)
    assert "## Boeking op 31/03/2013" in result
    assert "**Boeking op 31/03/2013" not in result


def test_promote_bold_boeking_not_mid_paragraph():
    """B4-SP2: bold Boeking-tekst MIDDEN in een alinea (geen blank lines rondom)
    mag NIET gepromoveerd worden — het is inline emphasis.
    """
    md = "Zie **boeking eerste jaar** hieronder voor details.\n"
    result = _promote_implicit_headings(md)
    assert "## " not in result


# ─── E2: <br> binnen tabel-cel renders als spatie (CBN-0103/1 pattern) ────────

def test_br_inside_td_becomes_space():
    """REGRESSIE-FIX (CBN-0103/1): `<br>` binnen `<td>` is visuele wrapping,
    geen functionele line-break. Vervang met spatie zodat tabel-rij op één
    regel staat (markdown-tabel-parser werkt).
    """
    from tools.lib.cbn_advies_html import parse_html
    html = (
        '<html><body><main>'
        '<p>Lorem ipsum dolor sit amet consectetur adipiscing elit sed do eiusmod tempor incididunt '
        'ut labore et dolore magna aliqua ut enim ad minim veniam quis nostrud exercitation ullamco '
        'laboris nisi ut aliquip ex ea commodo consequat duis aute irure dolor.</p>'
        '<table><tbody><tr>'
        '<td>&lt; Verhoogde<br />criteria</td>'
        '<td>Tweede cel</td>'
        '</tr></tbody></table>'
        '</main></body></html>'
    )
    body = parse_html(html).get('body', '')
    # Tabel-rij moet op één regel staan
    for line in body.split('\n'):
        if '|' in line and 'Verhoogde' in line:
            # De rij met "Verhoogde" moet ook "criteria" bevatten — niet gesplitst
            assert 'criteria' in line, f"<br> in td brak rij: {line!r}"
            assert '\n' not in line  # by definition van split('\n')
            return
    raise AssertionError("Geen tabel-rij met 'Verhoogde' gevonden in body")


def test_br_outside_table_keeps_linebreak():
    """`<br>` BUITEN een tabel-cel blijft een markdown line-break (`  \\n`)."""
    from tools.lib.cbn_advies_html import parse_html
    html = (
        '<html><body><main>'
        '<p>Lijn 1<br/>Lijn 2 na br met genoeg tekst om de 200-char trigger te halen — '
        'lorem ipsum dolor sit amet consectetur adipiscing elit sed do eiusmod tempor incididunt '
        'ut labore et dolore magna aliqua ut enim ad minim veniam quis nostrud.</p>'
        '</main></body></html>'
    )
    body = parse_html(html).get('body', '')
    # Lijn 1 + line-break + Lijn 2 moet op verschillende regels staan
    assert 'Lijn 1' in body
    assert 'Lijn 2' in body
    # Tussen Lijn 1 en Lijn 2 moet een newline staan
    idx1 = body.find('Lijn 1')
    idx2 = body.find('Lijn 2')
    between = body[idx1:idx2]
    assert '\n' in between, f"Geen line-break na <br> buiten td: {between!r}"


def test_html_indentation_in_cell_not_extra_pipes():
    """HTML-indentatie (newlines+tabs tussen tags) BINNEN een cell mag geen
    extra pipes of broken rows opleveren.
    """
    from tools.lib.cbn_advies_html import parse_html
    html = (
        '<html><body><main>'
        '<p>Lorem ipsum dolor sit amet consectetur adipiscing elit sed do eiusmod tempor incididunt '
        'ut labore et dolore magna aliqua ut enim ad minim veniam quis nostrud exercitation.</p>'
        '<table><tbody>'
        '<tr>\n'
        '    <td>Eerste cel</td>\n'
        '    <td>Tweede cel</td>\n'
        '    <td>Derde cel</td>\n'
        '</tr>'
        '</tbody></table>'
        '</main></body></html>'
    )
    body = parse_html(html).get('body', '')
    # Tabel-rij telt 3 cellen → 4 pipes (open + 3 separators).
    for line in body.split('\n'):
        if 'Eerste cel' in line and '|' in line:
            n_pipes = line.count('|')
            assert n_pipes == 4, f"Verwacht 4 pipes voor 3 cellen, kreeg {n_pipes}: {line!r}"
            return
    raise AssertionError("Geen rij met 'Eerste cel' gevonden")


# ─── D4-SP2: aangrenzende `</em><em>` artefact (CBN-0007-02) ─────────────────

def test_cleanup_repairs_adjacent_em_tags_artefact():
    """REGRESSIE-FIX (CBN-0007-02 r.49): twee aaneengesloten `<em>` tags
    (`<em>Bull. </em><em>CBN</em>`) renderen naar `*Bull. **CBN*` —
    een nep-bold-marker (`**`) die de italic-span breekt. De cleanup moet
    dit herstellen naar twee aparte italic-spans (`*Bull.* *CBN*`).

    Detectie-criterium: `*<TEXT1> **<TEXT2>*` met TEXT2 zonder asterisk en
    geen sluitende `**` na TEXT2 in dezelfde alinea.
    """
    md = "cf. advies 110 in *Bull. **CBN* nr. 2).\n"
    result = _cleanup_markdown(md)
    # Het artefact `**CBN*` moet weg
    assert "**CBN*" not in result
    # En `*Bull. **` (italic gevolgd door bold-open zonder close) ook weg
    assert "*Bull. **" not in result
    # De content moet bewaard blijven
    assert "Bull." in result
    assert "CBN" in result
    assert "nr. 2)" in result


def test_cleanup_preserves_legitimate_nested_bold_in_italic():
    """Genuine `*X **Y***` (3 stars aan eind, italic met geneste bold) blijft
    bewaard — geen fix nodig.
    """
    md = "Een *citaat met **bold accent*** in italic.\n"
    result = _cleanup_markdown(md)
    # Drie sluitende stars moeten blijven (legitieme nested)
    assert "**bold accent***" in result


def test_cleanup_preserves_isolated_italic():
    """Plain italic (`*...*`) blijft bewaard — adjacent-em-fix
    mag isolated italic-spans niet aanraken.
    """
    md = "Een gewone zin met *italic accent* erin.\n"
    result = _cleanup_markdown(md)
    assert "*italic accent*" in result


def test_cleanup_preserves_isolated_bold():
    """Plain bold (`**...**`) blijft bewaard."""
    md = "Een gewone zin met **bold woorden** erin.\n"
    result = _cleanup_markdown(md)
    assert "**bold woorden**" in result


# ─── D4-SP3: stray onafgesloten `**` (CBN-2022-15 voetnoot 55) ───────────────

def test_cleanup_strips_unclosed_bold_before_closing_quote():
    """REGRESSIE-FIX (CBN-2022-15 voetnoot 55): de bron-HTML bevat een
    stray `**` direct vóór een sluitend aanhalingsteken (`Belgique **",`).
    Geen paired `**` elders in dezelfde regel/alinea → stray artefact.
    De cleanup moet het strippen.

    Patroon: `<woord> **<quote>` waar geen ander `**` in dezelfde
    paragraaf/regel sluit.
    """
    md = (
        'Zie ook J. GABRIEL, "Succursales de sociétés étrangères '
        'en Belgique **", Revue de droit, 1987.\n'
    )
    result = _cleanup_markdown(md)
    # De stray `**` voor de closing quote moet weg
    assert 'Belgique **"' not in result
    assert 'Belgique **”' not in result
    # Maar de content blijft
    assert "Belgique" in result
    assert "Revue de droit" in result


def test_cleanup_strips_unclosed_bold_before_curly_quote():
    """Idem als hierboven, maar met curly-quote `”` (CBN-2022-15 echte versie)."""
    md = 'titel "Succursales en Belgique **”, Revue, 1987.\n'
    result = _cleanup_markdown(md)
    assert 'Belgique **”' not in result
    assert "Belgique" in result


def test_cleanup_preserves_paired_bold_with_quote():
    """Genuine paired bold rond gequoteerde tekst blijft bewaard:
    `**"woord"**` is legitiem en mag niet aangetast worden.
    """
    md = 'De titel **"Het Boek"** is van Jan.\n'
    result = _cleanup_markdown(md)
    assert '**"Het Boek"**' in result
