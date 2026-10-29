"""Generate the profile README graphics in light and dark variants.

Run from the repo root: python3 assets/readme/build.py
Edit the content below, then re-run. Never hand-edit the generated SVGs.
"""

from pathlib import Path
from xml.sax.saxutils import escape

OUT = Path(__file__).parent

# Light mode is sampled from a white Bronco with heritage-red trim: warm
# off-white paint, the stripe red (#A72530) and the near-black trim. The dark
# canvas matches GitHub's dark code blocks so the hero sits with them, and
# the accent approximates Bronco's Area 51 dusty blue.
THEMES = {
    "light": {"canvas": "#F1EEE9", "ink": "#1C1716", "accent": "#A72530"},
    "dark": {"canvas": "#151B23", "ink": "#F2F5FA", "accent": "#7FA3B3"},
}

SANS = "-apple-system, BlinkMacSystemFont, SF Pro Display, Segoe UI, Helvetica Neue, Arial, sans-serif"
MONO = "ui-monospace, SFMono-Regular, SF Mono, Menlo, Consolas, monospace"

HEADLINE = ["I build AI systems", "and the evals that measure them."]
META = "Orange County, CA  ·  Open to AI Engineer roles"

TOOLS = [
    {"slug": "notioniq", "name": "notionIQ",
     "lines": ["Claude reads a Notion", "workspace and proposes", "a cleanup."],
     "proof": "50 tests"},
    {"slug": "ai-jobs", "name": "ai-jobs",
     "lines": ["My job search, run from", "Claude Code. Listings, fit", "scores, tailored CVs."],
     "proof": "89 tests"},
    {"slug": "it-automation-tools", "name": "it-automation-tools",
     "lines": ["Zscaler cert trust, weekly", "restarts and Edge repair", "for Windows and Mac."],
     "proof": "5 scripts"},
]


def text(x, y, s, size, fill, *, font=SANS, weight=400, spacing=0):
    return (
        f'<text x="{x}" y="{y}" font-family="{font}" font-size="{size}" font-weight="{weight}" '
        f'letter-spacing="{spacing}" fill="{fill}">{escape(s)}</text>'
    )


def svg(w, h, title, body):
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" '
        f'viewBox="0 0 {w} {h}" role="img" aria-labelledby="t">\n'
        f'<title id="t">{escape(title)}</title>\n' + "\n".join(body) + "\n</svg>\n"
    )


def reveal(element, begin):
    """Fade an element in while it rises 10 units, then hold (plays once)."""
    return (
        f'<g opacity="0">'
        f'<animate attributeName="opacity" from="0" to="1" begin="{begin}s" dur="0.6s" fill="freeze"/>'
        f'<animateTransform attributeName="transform" type="translate" from="0 10" to="0 0" '
        f'begin="{begin}s" dur="0.6s" calcMode="spline" keySplines="0.2 0.8 0.2 1" fill="freeze"/>'
        f"{element}</g>"
    )


def build_hero(t):
    # A shell prompt types `whoami`, then the headline arrives as its output.
    # SMIL animation plays once on load and freezes on the final frame.
    steps = ";".join(str(round(i * 13.6)) for i in range(7))
    typing = 'begin="0.5s" dur="0.6s" calcMode="discrete" fill="freeze"'
    return svg(1200, 360, f'whoami: {" ".join(HEADLINE)} {META}', [
        '<defs><clipPath id="typed"><rect x="118" y="60" width="0" height="44">'
        f'<animate attributeName="width" values="{steps};84" {typing}/></rect></clipPath></defs>',
        f'<rect width="1200" height="324" rx="14" fill="{t["canvas"]}"/>',
        text(66, 92, "~ $", 22, t["accent"], font=MONO, weight=700),
        f'<g clip-path="url(#typed)">{text(120, 92, "whoami", 22, t["ink"], font=MONO)}</g>',
        f'<rect x="121" y="73" width="12" height="24" fill="{t["accent"]}">'
        '<animate attributeName="opacity" values="1;0;1" dur="0.5s" repeatCount="1"/>'
        f'<animateTransform attributeName="transform" type="translate" '
        f'values="{";".join(f"{v} 0" for v in steps.split(";"))};84 0" {typing}/>'
        '<set attributeName="opacity" to="0" begin="1.35s" fill="freeze"/></rect>',
        reveal(text(64, 164, HEADLINE[0], 52, t["ink"], weight=700, spacing=-1.4), 1.4),
        reveal(text(64, 226, HEADLINE[1], 52, t["ink"], weight=700, spacing=-1.4), 1.6),
        reveal(text(66, 282, META, 21, t["ink"]), 1.9),
    ])


def build_tool(c, t):
    # The name takes the accent: the whole column links to the repo.
    body = [text(4, 40, c["name"], 28, t["accent"], weight=700, spacing=-0.5)]
    for j, line in enumerate(c["lines"]):
        body.append(text(4, 84 + j * 30, line, 21, t["ink"]))
    body.append(text(4, 192, c["proof"], 19, t["ink"], font=MONO))
    return svg(400, 212, f'{c["name"]}. {" ".join(c["lines"])} {c["proof"]}.', body)


# GitHub forces its own blue on markdown links, so links that should carry the
# palette are drawn as text images instead.
LINKS = {"margin-invest": ("Margin Invest", 36), "assay": ("assay", 36),
         "linkedin": ("Say hello on LinkedIn ›", 26)}


def build_link(label, size, t):
    return svg(1200, round(size * 1.6), label, [
        text(2, round(size * 1.15), label, size, t["accent"], weight=700 if size > 30 else 500,
             spacing=-0.6 if size > 30 else 0),
    ])


def main():
    for old in OUT.glob("*.svg"):
        old.unlink()
    for name, t in THEMES.items():
        (OUT / f"hero-{name}.svg").write_text(build_hero(t))
        for c in TOOLS:
            (OUT / f"tool-{c['slug']}-{name}.svg").write_text(build_tool(c, t))
        for slug, (label, size) in LINKS.items():
            (OUT / f"link-{slug}-{name}.svg").write_text(build_link(label, size, t))


if __name__ == "__main__":
    main()
