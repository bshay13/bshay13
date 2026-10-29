"""Generate the profile README SVGs in light and dark variants.

Run from the repo root: python3 assets/readme/build.py
Edit the content dicts below, then re-run. Never hand-edit the generated SVGs.
"""

from pathlib import Path
from xml.sax.saxutils import escape

OUT = Path(__file__).parent

THEMES = {
    "dark": {
        "bg": "#0F141B", "surface": "#161C25", "border": "#263040",
        "fg": "#E6EDF3", "muted": "#8B98A9", "me": "#B794F6", "agent": "#4FD1C5",
    },
    "light": {
        "bg": "#FFFFFF", "surface": "#F6F8FA", "border": "#D8DEE6",
        "fg": "#1F2328", "muted": "#59636E", "me": "#6D28D9", "agent": "#0F766E",
    },
}

SANS = "-apple-system, BlinkMacSystemFont, Segoe UI, Helvetica, Arial, sans-serif"
MONO = "ui-monospace, SFMono-Regular, Menlo, Consolas, monospace"

HERO = {
    "eyebrow": "AI ENGINEER  ·  ORANGE COUNTY, CA",
    "name": "Brandon Shay",
    "lines": [
        "I design AI systems end to end:",
        "the spec, the evals and the gates.",
        "I build with coding agents and",
        "own what ships.",
    ],
    "loop": [
        ("SPEC + SLICES", "me"),
        ("BUILD WITH TDD", "agent"),
        ("TESTS + JUDGES", "agent"),
        ("EVAL GATE", "me"),
        ("APPROVE + COMMIT", "me"),
    ],
}

FLAGSHIP = {
    "slug": "margin-invest",
    "eyebrow": "FLAGSHIP  ·  SHIPPED, THEN RETIRED MAY 2026",
    "title": "Margin Invest",
    "desc": [
        "Deterministic equity research. Filters,",
        "scores and sizes 3,056 tickers. Claude",
        "flags what changed in 10-K risk factors.",
    ],
    "call": "No score reached a user without my approval.",
    "pipeline": [
        ("3,056 TICKERS", None),
        ("7 ELIMINATION FILTERS", None),
        ("4 SCORING PILLARS", None),
        ("10-K RISK DIFF  ·  CLAUDE", "agent"),
        ("HUMAN APPROVAL", "me"),
    ],
    "chips": ["546 tests", "95% coverage gate", "106-case eval set", "2,038 commits"],
}

CARDS = [
    {
        "slug": "assay",
        "eyebrow": "CLAUDE CODE PLUGIN  ·  v0.1.1",
        "title": "assay",
        "desc": ["Assays AI-written code before it", "merges: spec, TDD, judges, gates."],
        "call": "A test that never failed proves nothing.",
        "chips": ["29 judges", "175 tests", "MIT"],
    },
    {
        "slug": "notioniq",
        "eyebrow": "CLAUDE API  ·  CLI",
        "title": "notionIQ",
        "desc": ["Classifies a Notion workspace with", "Claude and recommends a cleanup."],
        "call": "Cost controls ship with the features.",
        "chips": ["50 tests", "mypy + pytest CI", "3 LLM providers"],
    },
    {
        "slug": "ai-jobs",
        "eyebrow": "CLAUDE CODE WORKSPACE",
        "title": "ai-jobs",
        "desc": ["Searches US job boards, scores fit,", "tailors the CV and preps interviews."],
        "call": "Your profile never leaves your machine.",
        "chips": ["89 tests", "BLS salary data", "Typer + httpx"],
    },
    {
        "slug": "it-automation-tools",
        "eyebrow": "ENTERPRISE  ·  2024-2025",
        "title": "it-automation-tools",
        "desc": ["Endpoint automation for Windows and", "macOS fleets: Intune, SCCM, Kandji."],
        "call": "Native OS tools, minimal dependencies.",
        "chips": ["PowerShell", "Bash", "Python + Polars"],
    },
]


def text(x, y, s, size, fill, *, mono=False, weight=400, spacing=0, anchor="start"):
    family = MONO if mono else SANS
    ls = f' letter-spacing="{spacing}"' if spacing else ""
    return (
        f'<text x="{x}" y="{y}" font-family="{family}" font-size="{size}" '
        f'font-weight="{weight}" fill="{fill}" text-anchor="{anchor}"{ls}>{escape(s)}</text>'
    )


def svg(w, h, title, desc, body, t):
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" '
        f'viewBox="0 0 {w} {h}" role="img" aria-labelledby="t d">\n'
        f'<title id="t">{escape(title)}</title>\n<desc id="d">{escape(desc)}</desc>\n'
        f'<rect x="5" y="5" width="{w - 10}" height="{h - 10}" rx="20" '
        f'fill="{t["bg"]}" stroke="{t["border"]}" stroke-width="2"/>\n'
        + "\n".join(body)
        + "\n</svg>\n"
    )


def chips(x, y, labels, t, size=17):
    out = []
    for label in labels:
        w = round(len(label) * size * 0.61 + 28)
        out.append(
            f'<rect x="{x}" y="{y}" width="{w}" height="34" rx="17" '
            f'fill="{t["surface"]}" stroke="{t["border"]}" stroke-width="1.5"/>'
        )
        out.append(text(x + 14, y + 23, label, size, t["fg"], mono=True))
        x += w + 10
    return out


def call_box(x, y, w, s, t):
    return [
        f'<rect x="{x}" y="{y}" width="{w}" height="46" rx="10" fill="{t["surface"]}"/>',
        f'<rect x="{x}" y="{y}" width="5" height="46" rx="2.5" fill="{t["me"]}"/>',
        text(x + 20, y + 30, "My call:", 19, t["me"], weight=600),
        text(x + 102, y + 30, s, 19, t["fg"]),
    ]


def node(x, y, w, h, label, role, t, size=19):
    stroke = t[role] if role else t["border"]
    out = [
        f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{h / 2}" '
        f'fill="{t["surface"]}" stroke="{stroke}" stroke-width="2"/>',
        f'<circle cx="{x + 22}" cy="{y + h / 2}" r="6" fill="{stroke}"/>',
        text(x + 40, y + h / 2 + size * 0.36, label, size, t["fg"], mono=True),
    ]
    if role:
        out.append(
            text(x + w - 20, y + h / 2 + 6, role, 16, t[role], mono=True, anchor="end")
        )
    return out


def connector(x, y1, y2, t):
    return (
        f'<line x1="{x}" y1="{y1}" x2="{x}" y2="{y2}" stroke="{t["muted"]}" '
        f'stroke-width="2" stroke-dasharray="3 4"/>'
    )


def legend(x, y, t):
    return [
        f'<circle cx="{x + 7}" cy="{y - 6}" r="7" fill="{t["me"]}"/>',
        text(x + 22, y, "me", 18, t["muted"], mono=True),
        f'<circle cx="{x + 82}" cy="{y - 6}" r="7" fill="{t["agent"]}"/>',
        text(x + 97, y, "agent", 18, t["muted"], mono=True),
    ]


def build_hero(t):
    body = [
        text(64, 86, HERO["eyebrow"], 18, t["muted"], mono=True, spacing=2),
        text(64, 154, HERO["name"], 60, t["fg"], weight=700, spacing=-1),
    ]
    for i, line in enumerate(HERO["lines"]):
        body.append(text(64, 212 + i * 37, line, 27, t["fg"]))
    body += legend(64, 374, t)

    x, w, h, gap, y = 730, 330, 46, 18, 56
    for i, (label, role) in enumerate(HERO["loop"]):
        top = y + i * (h + gap)
        if i:
            body.append(connector(x + 165, top - gap, top, t))
        body += node(x, top, w, h, label, role, t)
    last = y + 4 * (h + gap) + h / 2
    first = y + h / 2
    body.append(
        f'<path d="M {x + w} {last} C {x + w + 60} {last}, {x + w + 60} {first}, '
        f'{x + w} {first}" fill="none" stroke="{t["me"]}" stroke-width="2" '
        f'stroke-dasharray="3 4"/>'
    )
    body.append(
        f'<path d="M {x + w + 10} {first - 6} L {x + w} {first} L {x + w + 10} {first + 6}" '
        f'fill="none" stroke="{t["me"]}" stroke-width="2"/>'
    )
    body.append(
        f'<text x="{x + w + 66}" y="{(first + last) / 2}" font-family="{MONO}" '
        f'font-size="16" fill="{t["muted"]}" text-anchor="middle" '
        f'transform="rotate(90 {x + w + 66} {(first + last) / 2})">lessons feed the next spec</text>'
    )
    return svg(
        1200, 420, "Brandon Shay, AI Engineer",
        "AI Engineer in Orange County, CA. I design AI systems end to end: the spec, the evals "
        "and the gates. I build with coding agents and own what ships. Loop: spec and slices (me), build with TDD "
        "(agent), tests and judges (agent), eval gate (me), approve and commit (me), with "
        "lessons feeding the next spec.",
        body, t,
    )


def build_flagship(t):
    f = FLAGSHIP
    body = [
        text(48, 70, f["eyebrow"], 18, t["muted"], mono=True, spacing=1.5),
        text(48, 128, f["title"], 48, t["fg"], weight=700, spacing=-0.5),
    ]
    for i, line in enumerate(f["desc"]):
        body.append(text(48, 172 + i * 32, line, 24, t["fg"]))
    body += call_box(48, 254, 560, f["call"], t)
    body += chips(48, 330, f["chips"], t, size=18)

    x, w, h, gap, y = 680, 470, 40, 12, 44
    for i, (label, role) in enumerate(f["pipeline"]):
        top = y + i * (h + gap)
        if i:
            body.append(connector(x + 235, top - gap, top, t))
        body += node(x, top, w, h, label, role, t, size=18)
    return svg(
        1200, 392, "Margin Invest",
        "Margin Invest: deterministic equity research platform, shipped then retired "
        "in May 2026. Pipeline: 3,056 tickers, 7 elimination filters, 4 scoring pillars, a "
        "10-K risk factor diff judged by Claude, then human approval before publishing. "
        "546 tests, 95% engine coverage gate, a 106-case eval set, 2,038 commits.",
        body, t,
    )


def build_card(c, t):
    body = [
        text(40, 64, c["eyebrow"], 18, t["muted"], mono=True, spacing=1.5),
        text(40, 116, c["title"], 40, t["fg"], weight=700, spacing=-0.5),
    ]
    for i, line in enumerate(c["desc"]):
        body.append(text(40, 158 + i * 30, line, 22, t["fg"]))
    body += call_box(40, 210, 520, c["call"], t)
    body += chips(40, 280, c["chips"], t)
    return svg(
        600, 340, c["title"],
        f'{c["title"]}: {" ".join(c["desc"])} My call: {c["call"]} {", ".join(c["chips"])}.',
        body, t,
    )


def main():
    for name, t in THEMES.items():
        (OUT / f"hero-{name}.svg").write_text(build_hero(t))
        (OUT / f"card-{FLAGSHIP['slug']}-{name}.svg").write_text(build_flagship(t))
        for c in CARDS:
            (OUT / f"card-{c['slug']}-{name}.svg").write_text(build_card(c, t))


if __name__ == "__main__":
    main()
