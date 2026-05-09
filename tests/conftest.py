"""Pytest configuratie: zorg dat repo-root op sys.path staat zodat tests
absolute imports zoals `from tools.lib.headings import ...` kunnen doen.
"""
from __future__ import annotations

import sys
from pathlib import Path

_ROOT = Path(__file__).resolve().parent.parent
if str(_ROOT) not in sys.path:
    sys.path.insert(0, str(_ROOT))
