#!/usr/bin/env python3
"""Convert LLGA course index.html (paper shell) to Quarto index.qmd."""
from __future__ import annotations

import argparse
import html as htmlmod
import re
import subprocess
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

YAML_TEMPLATE = """\
---
title: "{title}"
subtitle: "{subtitle}"
lang: en
format:
  html:
    theme: none
    minimal: true
    toc: false
    anchor-sections: false
    html-math-method: katex
    highlight-style: github
    embed-resources: false
    css: ../../assets/paper.css
    include-in-header:
      - text: |
          <script>(function(){{try{{var t=localStorage.getItem("llga-theme");if(t==="dark"||t==="light")document.documentElement.setAttribute("data-theme",t);}}catch(e){{}}}})();</script>
          <style>
            /* Keep paper.css as visual source of truth; tame Quarto chrome */
            #title-block-header {{ margin: 0 0 0.5rem; }}
            #title-block-header .title {{ margin: 0 0 0.25rem; font-size: 1.85rem; font-weight: 700; }}
            #title-block-header .subtitle {{ color: var(--soft, #555); margin: 0 0 1rem; font-size: 1.05rem; }}
            div.sourceCode {{ background: var(--code-bg, #f7f7f7); border: 1px solid var(--hair, #e4e4e4); }}
            code {{ background: var(--code-inline-bg, #f4f4f4); }}

            /* Light (github) token colors — higher specificity beats paper.css */
            div.sourceCode pre.sourceCode code span.kw, div.sourceCode pre.sourceCode code span.cf, div.sourceCode pre.sourceCode code span.dt, div.sourceCode pre.sourceCode code span.at, div.sourceCode pre.sourceCode code span.bu, div.sourceCode pre.sourceCode code span.pp {{ color: #d73a49; }}
            div.sourceCode pre.sourceCode code span.im, div.sourceCode pre.sourceCode code span.st, div.sourceCode pre.sourceCode code span.ch, div.sourceCode pre.sourceCode code span.ss, div.sourceCode pre.sourceCode code span.vs {{ color: #032f62; }}
            div.sourceCode pre.sourceCode code span.co, div.sourceCode pre.sourceCode code span.an, div.sourceCode pre.sourceCode code span.cv, div.sourceCode pre.sourceCode code span.do, div.sourceCode pre.sourceCode code span.in {{ color: #6a737d; }}
            div.sourceCode pre.sourceCode code span.fu {{ color: #6f42c1; }}
            div.sourceCode pre.sourceCode code span.va {{ color: #e36209; }}
            div.sourceCode pre.sourceCode code span.cn, div.sourceCode pre.sourceCode code span.bn, div.sourceCode pre.sourceCode code span.dv, div.sourceCode pre.sourceCode code span.fl, div.sourceCode pre.sourceCode code span.sc {{ color: #005cc5; }}
            div.sourceCode pre.sourceCode code span.op {{ color: #24292e; }}
            /* Dark mode token colors (github highlight is light-oriented) */
            [data-theme="dark"] div.sourceCode pre.sourceCode code span.kw,
            [data-theme="dark"] div.sourceCode pre.sourceCode code span.cf,
            [data-theme="dark"] div.sourceCode pre.sourceCode code span.dt,
            [data-theme="dark"] div.sourceCode pre.sourceCode code span.at,
            [data-theme="dark"] div.sourceCode pre.sourceCode code span.bu,
            [data-theme="dark"] div.sourceCode pre.sourceCode code span.pp,
            [data-theme="dark"] div.sourceCode pre.sourceCode code span.op {{ color: #ff7b72; }}
            [data-theme="dark"] div.sourceCode pre.sourceCode code span.im {{ color: #ff7b72; }}
            [data-theme="dark"] div.sourceCode pre.sourceCode code span.st,
            [data-theme="dark"] div.sourceCode pre.sourceCode code span.ch,
            [data-theme="dark"] div.sourceCode pre.sourceCode code span.ss,
            [data-theme="dark"] div.sourceCode pre.sourceCode code span.vs {{ color: #a5d6ff; }}
            [data-theme="dark"] div.sourceCode pre.sourceCode code span.cn,
            [data-theme="dark"] div.sourceCode pre.sourceCode code span.bn,
            [data-theme="dark"] div.sourceCode pre.sourceCode code span.dv,
            [data-theme="dark"] div.sourceCode pre.sourceCode code span.fl,
            [data-theme="dark"] div.sourceCode pre.sourceCode code span.sc {{ color: #79c0ff; }}
            [data-theme="dark"] div.sourceCode pre.sourceCode code span.co,
            [data-theme="dark"] div.sourceCode pre.sourceCode code span.an,
            [data-theme="dark"] div.sourceCode pre.sourceCode code span.cv,
            [data-theme="dark"] div.sourceCode pre.sourceCode code span.do,
            [data-theme="dark"] div.sourceCode pre.sourceCode code span.in {{ color: #8b949e; }}
            [data-theme="dark"] div.sourceCode pre.sourceCode code span.va {{ color: #ffa657; }}
            [data-theme="dark"] div.sourceCode pre.sourceCode code span.fu {{ color: #d2a8ff; }}
            @media (prefers-color-scheme: dark) {{
              :root:not([data-theme="light"]) div.sourceCode pre.sourceCode code span.kw,
              :root:not([data-theme="light"]) div.sourceCode pre.sourceCode code span.cf,
              :root:not([data-theme="light"]) div.sourceCode pre.sourceCode code span.dt,
              :root:not([data-theme="light"]) div.sourceCode pre.sourceCode code span.at,
              :root:not([data-theme="light"]) div.sourceCode pre.sourceCode code span.bu,
              :root:not([data-theme="light"]) div.sourceCode pre.sourceCode code span.pp,
              :root:not([data-theme="light"]) div.sourceCode pre.sourceCode code span.op {{ color: #ff7b72; }}
              :root:not([data-theme="light"]) div.sourceCode pre.sourceCode code span.im {{ color: #ff7b72; }}
              :root:not([data-theme="light"]) div.sourceCode pre.sourceCode code span.st,
              :root:not([data-theme="light"]) div.sourceCode pre.sourceCode code span.ch,
              :root:not([data-theme="light"]) div.sourceCode pre.sourceCode code span.ss,
              :root:not([data-theme="light"]) div.sourceCode pre.sourceCode code span.vs {{ color: #a5d6ff; }}
              :root:not([data-theme="light"]) div.sourceCode pre.sourceCode code span.cn,
              :root:not([data-theme="light"]) div.sourceCode pre.sourceCode code span.bn,
              :root:not([data-theme="light"]) div.sourceCode pre.sourceCode code span.dv,
              :root:not([data-theme="light"]) div.sourceCode pre.sourceCode code span.fl,
              :root:not([data-theme="light"]) div.sourceCode pre.sourceCode code span.sc {{ color: #79c0ff; }}
              :root:not([data-theme="light"]) div.sourceCode pre.sourceCode code span.co,
              :root:not([data-theme="light"]) div.sourceCode pre.sourceCode code span.an,
              :root:not([data-theme="light"]) div.sourceCode pre.sourceCode code span.cv,
              :root:not([data-theme="light"]) div.sourceCode pre.sourceCode code span.do,
              :root:not([data-theme="light"]) div.sourceCode pre.sourceCode code span.in {{ color: #8b949e; }}
              :root:not([data-theme="light"]) div.sourceCode pre.sourceCode code span.va {{ color: #ffa657; }}
              :root:not([data-theme="light"]) div.sourceCode pre.sourceCode code span.fu {{ color: #d2a8ff; }}
            }}
          
          </style>
    include-before-body:
      - text: |
          <p class="crumb"><a href="../../index.html">MSc&amp;T LLGA · Course notes</a></p>
          <main class="paper">
    include-after-body:
      - text: |
          </main>
          <footer class="foot"><p><a href="../../index.html">← Master's program</a></p></footer>
          <script defer src="../../assets/theme.js"></script>
---

"""

FR_FIXES = [
    (
        "Materials in French, with English terminology systematically given",
        "Materials in English",
    ),
    (
        "Materials in French, code and terminology in English",
        "Materials in English; code and terminology in English",
    ),
]


def convert_inline_math(text: str) -> str:
    """Convert \\(...\\) to $...$ while leaving $$...$$ untouched."""
    out: list[str] = []
    i = 0
    n = len(text)
    while i < n:
        if text.startswith("$$", i):
            j = text.find("$$", i + 2)
            if j == -1:
                out.append(text[i:])
                break
            out.append(text[i : j + 2])
            i = j + 2
            continue
        if text.startswith("\\(", i):
            j = text.find("\\)", i + 2)
            if j == -1:
                out.append(text[i:])
                break
            out.append("$" + text[i + 2 : j] + "$")
            i = j + 2
            continue
        out.append(text[i])
        i += 1
    return "".join(out)


def unwrap_sections_html(main: str) -> str:
    """Turn <section class="chapter" id="x"> into flat content; put id on h2."""

    def repl(m: re.Match) -> str:
        attrs = m.group(1) or ""
        inner = m.group(2)
        idm = re.search(r'\bid="([^"]+)"', attrs)
        sid = idm.group(1) if idm else None
        if sid:

            def add_id(hm: re.Match) -> str:
                hattrs = hm.group(1) or ""
                body = hm.group(2)
                if "id=" in hattrs:
                    return hm.group(0)
                return f'<h2 id="{sid}">{body}</h2>'

            inner2, n = re.subn(
                r"<h2(\s[^>]*)?>(.*?)</h2>", add_id, inner, count=1, flags=re.S
            )
            if n:
                return inner2
            return f'<div id="{sid}"></div>\n' + inner
        return inner

    # Non-greedy section unwrap (chapters are siblings, not nested)
    return re.sub(
        r"<section(\s[^>]*)?>(.*?)</section>",
        repl,
        main,
        flags=re.S,
    )


def unwrap_nav_toc(main: str) -> str:
    """Replace HTML toc nav with a simple marker list pandoc will keep."""
    return re.sub(
        r'<nav class="toc">.*?</nav>',
        lambda m: m.group(0),  # keep — pandoc turns it into a list
        main,
        count=1,
        flags=re.S,
    )


def fix_math_escapes(md: str) -> str:
    """Inside $...$ / $$...$$, collapse pandoc double-backslashes to TeX singles."""

    def fix_span(tex: str) -> str:
        # pandoc escapes: \\ -> \, \^ -> ^, etc. inside math we want real TeX.
        tex = tex.replace("\\\\", "\0")  # temp for true backslash pairs
        # After replace, \0 stands for one intended backslash from \\
        # Also undo \^ \_
        tex = tex.replace("\\^", "^").replace("\\_", "_")
        tex = tex.replace("\0", "\\")
        return tex

    def sub_display(m: re.Match) -> str:
        return "$$" + fix_span(m.group(1)) + "$$"

    def sub_inline(m: re.Match) -> str:
        return "$" + fix_span(m.group(1)) + "$"

    md = re.sub(r"\$\$(.*?)\$\$", sub_display, md, flags=re.S)
    # inline: single $ not part of $$
    md = re.sub(r"(?<!\$)\$(?!\$)(.*?)(?<!\$)\$(?!\$)", sub_inline, md, flags=re.S)
    return md



def unescape_brackets_in_math(md: str) -> str:
    """Inside $...$ / $$...$$, replace \\[ → [ and \\] → ].

    Pandoc escapes literal brackets in math as \\[ \\], which KaTeX
    then misreads as display-math delimiters. These docs use $$ for display.
    Does not touch \\[...\\] outside dollar math.
    """

    def fix_span(tex: str) -> str:
        return tex.replace("\\[", "[").replace("\\]", "]")

    def sub_display(m: re.Match) -> str:
        return "$$" + fix_span(m.group(1)) + "$$"

    def sub_inline(m: re.Match) -> str:
        return "$" + fix_span(m.group(1)) + "$"

    md = re.sub(r"\$\$(.*?)\$\$", sub_display, md, flags=re.S)
    md = re.sub(r"(?<!\$)\$(?!\$)(.*?)(?<!\$)\$(?!\$)", sub_inline, md, flags=re.S)
    return md


def balance_check(md: str) -> None:
    depth = 0
    for i, line in enumerate(md.splitlines(), 1):
        if re.match(r"^:{3,}\s*$", line):
            depth -= 1
        elif re.match(r"^:{3,}\s+\S", line) or re.match(r"^:{3,}\s*\{", line):
            depth += 1
    if depth != 0:
        raise SystemExit(f"unbalanced fenced divs (depth={depth})")


def html_to_markdown(main_html: str) -> str:
    with tempfile.NamedTemporaryFile(
        "w", suffix=".html", delete=False, encoding="utf-8"
    ) as f:
        f.write("<article>\n" + main_html + "\n</article>\n")
        src = f.name
    out_md = Path(tempfile.mkstemp(suffix=".md")[1])
    subprocess.check_call(
        [
            "quarto",
            "pandoc",
            src,
            "-f",
            "html",
            "-t",
            "markdown-smart+raw_html+pipe_tables-tex_math_dollars",
            "--wrap=none",
            "-o",
            str(out_md),
        ]
    )
    return out_md.read_text(encoding="utf-8")


def convert_file(html_path: Path, qmd_path: Path | None = None) -> Path:
    html = html_path.read_text(encoding="utf-8")
    title = re.search(r"<h1>(.*?)</h1>", html, re.S).group(1).strip()
    subtitle_raw = re.search(r'<p class="subtitle">(.*?)</p>', html, re.S).group(1)
    subtitle = htmlmod.unescape(subtitle_raw.replace("&nbsp;", " ")).strip()
    main = re.search(r'<main class="paper">(.*?)</main>', html, re.S).group(1)

    # Drop h1/subtitle from main — they live in YAML
    main = re.sub(r"<h1>.*?</h1>\s*", "", main, count=1, flags=re.S)
    main = re.sub(r'<p class="subtitle">.*?</p>\s*', "", main, count=1, flags=re.S)

    main = unwrap_sections_html(main)
    main = convert_inline_math(main)
    for a, b in FR_FIXES:
        main = main.replace(a, b)

    md = html_to_markdown(main)
    md = re.sub(r"^Contents\n+", "## Contents\n\n", md, count=1)
    # Flatten any residual section-only div fences pandoc may emit
    md = re.sub(
        r"^:{3,}\s*\{#([a-zA-Z0-9_-]+)\s*\.section[^}]*\}\s*$",
        r"<!-- kept-id:\1 -->",
        md,
        flags=re.M,
    )
    # Do NOT strip bare ::: closers — they close note/def/thm/sol/…
    md = fix_math_escapes(md)
    md = unescape_brackets_in_math(md)
    md = re.sub(r"\n{3,}", "\n\n", md).strip() + "\n"
    balance_check(md)

    yaml = YAML_TEMPLATE.format(
        title=title.replace('"', '\\"'),
        subtitle=subtitle.replace('"', '\\"'),
    )
    qmd_path = qmd_path or html_path.with_name("index.qmd")
    qmd_path.write_text(yaml + md, encoding="utf-8")
    return qmd_path


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument(
        "courses",
        nargs="*",
        default=[
            "courses/m1p1-refresher-statistics",
            "courses/m1p1-refresher-cs",
        ],
    )
    args = ap.parse_args()
    for rel in args.courses:
        course = ROOT / rel
        html = course / "index.html"
        # Prefer original HTML backup if present (re-run safety)
        bak = Path("/tmp") / f"{course.name}-index.html.bak"
        src = bak if bak.exists() else html
        if not src.exists():
            raise SystemExit(f"missing {src}")
        # If we're reading backup, still write next to course dir
        out = convert_file(src, qmd_path=course / "index.qmd")
        print(f"wrote {out.relative_to(ROOT)} ({out.stat().st_size} bytes) from {src}")


if __name__ == "__main__":
    main()
