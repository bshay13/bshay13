"""Generate the profile README graphics in light and dark variants.

Run from the repo root: python3 assets/readme/build.py
Edit the content below, then re-run. Never hand-edit the generated SVGs.
"""

from pathlib import Path
from xml.sax.saxutils import escape

OUT = Path(__file__).parent

# One text color and one accent per theme. Bars use Apple's system blue, indigo, purple and pink, spread across the full
# scale so a longer bar reaches further into the spectrum.
THEMES = {
    "dark": {"fg": "#F5F5F7", "accent": "#2997FF",
             "ramp": ("#0A84FF", "#5E5CE6", "#BF5AF2", "#FF375F")},
    "light": {"fg": "#1D1D1F", "accent": "#0071E3",
              "ramp": ("#007AFF", "#5856D6", "#AF52DE", "#FF2D55")},
}

SANS = "-apple-system, BlinkMacSystemFont, SF Pro Display, Segoe UI, Helvetica Neue, Arial, sans-serif"
MONO = "ui-monospace, SFMono-Regular, SF Mono, Menlo, Consolas, monospace"

NAME = "Brandon Shay"
LINE = "AI systems I can stand behind."

# Test functions per repo: git grep -E '^\s*(async )?def test_' | wc -l
TESTS = [("margin_invest", 546), ("assay", 175), ("ai-jobs", 89), ("notionIQ", 50)]


def text(x, y, s, size, fill, *, font=SANS, weight=400, spacing=0, anchor="start"):
    return (
        f'<text x="{x}" y="{y}" font-family="{font}" font-size="{size}" font-weight="{weight}" '
        f'letter-spacing="{spacing}" fill="{fill}" text-anchor="{anchor}">{escape(s)}</text>'
    )


def svg(w, h, title, body):
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" '
        f'viewBox="0 0 {w} {h}" role="img" aria-labelledby="t">\n'
        f'<title id="t">{escape(title)}</title>\n' + "\n".join(body) + "\n</svg>\n"
    )


def build_hero(t):
    return svg(1200, 240, f"{NAME}. {LINE}", [
        text(2, 120, NAME, 96, t["fg"], weight=700, spacing=-3),
        text(4, 196, LINE, 44, t["fg"], spacing=-0.8),
    ])


def build_tests(t):
    total = sum(n for _, n in TESTS)
    top = max(n for _, n in TESTS)
    stops = "".join(
        f'<stop offset="{i / (len(t["ramp"]) - 1):.2f}" stop-color="{c}"/>'
        for i, c in enumerate(t["ramp"])
    )
    body = [
        f'<defs><linearGradient id="ramp" gradientUnits="userSpaceOnUse" '
        f'x1="644" y1="0" x2="1084" y2="0">{stops}</linearGradient></defs>',
        text(2, 140, f"{total}", 112, t["fg"], weight=700, spacing=-4),
        text(6, 190, "test functions across four projects", 26, t["fg"]),
    ]
    for i, (name, n) in enumerate(TESTS):
        y = 58 + i * 58
        width = round(440 * n / top)
        body.append(text(620, y + 8, name, 22, t["fg"], font=MONO, anchor="end"))
        body.append(f'<rect x="644" y="{y - 10}" width="{width}" height="24" rx="12" fill="url(#ramp)"/>')
        body.append(text(644 + width + 14, y + 8, str(n), 22, t["fg"], font=MONO))
    rows = ", ".join(f"{name} {n}" for name, n in TESTS)
    return svg(1200, 260, f"{total} test functions across four projects: {rows}.", body)


TOOLS = [
    {"slug": "notioniq", "name": "notionIQ",
     "lines": ["Reads a Notion workspace", "with Claude and suggests", "a cleanup."],
     "proof": "50 tests"},
    {"slug": "ai-jobs", "name": "ai-jobs",
     "lines": ["Runs my own job search", "from Claude Code: listings,", "fit scores, tailored CVs."],
     "proof": "89 tests"},
    {"slug": "it-automation-tools", "name": "it-automation-tools",
     "lines": ["Keeps Windows and Mac", "fleets in line through", "Intune and Kandji."],
     "proof": "PowerShell + Bash"},
]


def build_tool(c, t):
    body = [
        f'<rect x="4" y="16" width="48" height="3" rx="1.5" fill="{t["accent"]}"/>',
        text(4, 74, c["name"], 30, t["fg"], weight=700, spacing=-0.5),
    ]
    for i, line in enumerate(c["lines"]):
        body.append(text(4, 118 + i * 30, line, 22, t["fg"]))
    body.append(text(4, 228, c["proof"], 20, t["fg"], font=MONO))
    body.append(text(4, 270, "View on GitHub ›", 22, t["accent"]))
    return svg(400, 290, f'{c["name"]}. {" ".join(c["lines"])} {c["proof"]}.', body)


def main():
    for old in OUT.glob("*.svg"):
        old.unlink()
    for name, t in THEMES.items():
        (OUT / f"hero-{name}.svg").write_text(build_hero(t))
        (OUT / f"tests-{name}.svg").write_text(build_tests(t))
        for c in TOOLS:
            (OUT / f"tool-{c['slug']}-{name}.svg").write_text(build_tool(c, t))


if __name__ == "__main__":
    main()
