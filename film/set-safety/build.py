"""Build index.html from index.src.html by inlining <!--map:name--> with name.svg.

    python build.py
"""
import re
from pathlib import Path

here = Path(__file__).parent
src = (here / "index.src.html").read_text(encoding="utf-8")
out = re.sub(r"<!--map:([\w-]+)-->",
             lambda m: (here / f"{m.group(1)}.svg").read_text(encoding="utf-8"), src)
(here / "index.html").write_text(out, encoding="utf-8")
print("index.html built,", len(out), "bytes")
