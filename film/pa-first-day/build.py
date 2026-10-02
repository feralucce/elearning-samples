"""Build index.html from index.src.html by inlining the maps.

Each <!--map:name--> marker is replaced with maps/name.svg, with its ids
prefixed so several maps can share one page. Run after editing a map:

    python build.py
"""
import re
from pathlib import Path

here = Path(__file__).parent
src = (here / "index.src.html").read_text(encoding="utf-8")


def inline(match):
    name = match.group(1)
    svg = (here / "maps" / f"{name}.svg").read_text(encoding="utf-8")
    prefix = re.sub(r"\W", "", name) + "-"
    ids = re.findall(r'\bid="([^"]+)"', svg)
    for i in ids:
        svg = svg.replace(f'id="{i}"', f'id="{prefix}{i}"')
        svg = svg.replace(f"url(#{i})", f"url(#{prefix}{i})")
    svg = re.sub(r'aria-labelledby="([^"]+)"',
                 lambda m: 'aria-labelledby="' + " ".join(prefix + x for x in m.group(1).split()) + '"', svg)
    return svg


out = re.sub(r"<!--map:([\w-]+)-->", inline, src)
(here / "index.html").write_text(out, encoding="utf-8")
print("index.html built,", len(out), "bytes")
