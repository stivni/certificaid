"""Tail een agent-JSONL en toon last-N events leesbaar.

Usage:
    python3 -m tools.extractie.tail_agent <agent_id>
    python3 -m tools.extractie.tail_agent <agent_id> --watch    # refresh elke 5s
    python3 -m tools.extractie.tail_agent <agent_id> --tail 10  # toon laatste 10
"""

import argparse
import json
import sys
import time
from pathlib import Path

PROJECT_DIR = Path.home() / ".claude" / "projects" / "-Users-stivni-Documents-ITAA-certificaid"


def find_session_dir() -> Path:
    """Zoek de meest recente sessie-dir."""
    if not PROJECT_DIR.exists():
        raise SystemExit(f"PROJECT_DIR niet gevonden: {PROJECT_DIR}")
    sessions = sorted([d for d in PROJECT_DIR.iterdir() if d.is_dir() and (d / "subagents").exists()],
                      key=lambda p: p.stat().st_mtime, reverse=True)
    if not sessions:
        raise SystemExit("Geen sessie-dirs gevonden")
    return sessions[0]


def find_agent_jsonl(agent_id: str) -> Path:
    """Zoek de JSONL van een agent — fuzzy match op prefix."""
    session_dir = find_session_dir()
    subagents_dir = session_dir / "subagents"
    for f in subagents_dir.glob(f"agent-{agent_id}*.jsonl"):
        return f
    raise SystemExit(f"Agent JSONL niet gevonden voor id-prefix '{agent_id}' in {subagents_dir}")


def summarize_event(i: int, obj: dict) -> str:
    """Maak een 1-line samenvatting van een JSONL-event."""
    msg = obj.get("message", {})
    content = msg.get("content", [])
    lines = []
    if isinstance(content, list):
        for c in content:
            if not isinstance(c, dict):
                continue
            t = c.get("type")
            if t == "tool_use":
                name = c.get("name", "?")
                inp = c.get("input", {})
                detail = ""
                if name == "mcp__certificaid-rag__zoek_bronnen":
                    detail = f"rerank={inp.get('rerank', False)} q='{inp.get('query','')[:50]}'"
                elif name == "Bash":
                    detail = inp.get("command", "")[:70]
                elif name in ("Read", "Write", "Edit"):
                    detail = inp.get("file_path", "")[:70]
                elif name.startswith("mcp__"):
                    detail = " ".join(f"{k}={str(v)[:20]}" for k, v in inp.items() if k not in ("query",))[:80]
                else:
                    detail = str(list(inp.keys()))[:60]
                lines.append(f"[{i}] TOOL: {name} | {detail}")
            elif t == "tool_result":
                txt = str(c.get("content", ""))[:90]
                err = "ERR " if c.get("is_error") else ""
                lines.append(f"[{i}] {err}RESULT: {txt}")
            elif t == "text":
                text = c.get("text", "")[:90]
                lines.append(f"[{i}] TEXT[{len(c.get('text',''))}]: {text}")
            elif t == "thinking":
                lines.append(f"[{i}] THINKING[{len(c.get('thinking',''))}c]")
    return "\n  ".join(lines) if lines else f"[{i}] (empty)"


def show_tail(path: Path, n: int):
    events = []
    with open(path) as fh:
        for line in fh:
            try:
                events.append(json.loads(line))
            except json.JSONDecodeError:
                continue
    total = len(events)
    print(f"━━━ {path.name} — {total} events, mtime {time.strftime('%H:%M:%S', time.localtime(path.stat().st_mtime))} ━━━")
    for i, obj in enumerate(events[-n:], start=total - n):
        print("  " + summarize_event(i, obj))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("agent_id", help="Agent-id of prefix (bv. 'ac2ad' voor agent-ac2ad95f2...)")
    ap.add_argument("--watch", action="store_true", help="Refresh elke 5s")
    ap.add_argument("--tail", type=int, default=5, help="Aantal laatste events (default 5)")
    ap.add_argument("--interval", type=int, default=5, help="Watch-interval in seconden (default 5)")
    args = ap.parse_args()

    path = find_agent_jsonl(args.agent_id)
    if args.watch:
        try:
            while True:
                # Clear screen + show
                print("\033[2J\033[H", end="")
                show_tail(path, args.tail)
                print(f"\n  (Ctrl+C om te stoppen, refresh elke {args.interval}s)")
                time.sleep(args.interval)
        except KeyboardInterrupt:
            print("\n  Gestopt.")
    else:
        show_tail(path, args.tail)


if __name__ == "__main__":
    main()
