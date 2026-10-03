"""Build index.html from nibble.py.  python build.py"""
from collections import Counter, OrderedDict
from html import escape as h
from pathlib import Path
import nibble as N

HERE = Path(__file__).parent


def pages(e8):
    w, r = divmod(e8, 8)
    return (f"{w} " if w else "") + (f"{r}/8" if r else "") if (w or r) else "0"


def kind(ie, tod):
    night = tod.lower() == "night"
    if not ie:
        return "pb", "Playback"
    return ({("INT", False): "di", ("EXT", False): "de", ("INT", True): "ni", ("EXT", True): "ne"}[(ie, night)],
            f"{'Night' if night else 'Day'} {ie.lower()}")


# ---------------------------------------------------------------- numbers
all_scenes = [s for d in N.DAYS for s in d[3]]
total8 = sum(s[4] for s in all_scenes)
cast_days = OrderedDict((c, [i for i, d in enumerate(N.DAYS) if any(c in s[5] for s in d[3])]) for c in N.CAST)
lines = [l for b in N.BUDGET for l in b[4]]


def cover(how):
    how = how.lower()
    if how.startswith("cash"):
        return "Cash"
    if "student" in how:
        return "Students"
    if "savage light" in how or "university" in how:
        return "Lent or provided"
    return "Pro bono"


cov = Counter(cover(l[2]) for l in lines)
prep_weeks = sum(1 for _, ph, _ in N.PREP if ph != 'Shoot')

# ---------------------------------------------------------------- prep timeline
weeks = [w for w, _, _ in N.PREP]
rows = ""
for ph in N.PHASES:
    cells = ""
    for wk, phase, tasks in N.PREP:
        on = phase == ph
        tip = h("; ".join(tasks)) if on else ""
        cells += f"<td class='g{' on' if on else ''}' title='{tip}'>{'<span>' + str(len(tasks)) + '</span>' if on else ''}</td>"
    rows += f"<tr><th scope='row'>{ph}</th>{cells}</tr>"
heads = "".join(f"<th scope='col'><span>{w}</span></th>" for w in weeks)
prep_list = "".join(f"<li><b>{w}</b> <span class='ph'>{p}</span><ul>" + "".join(f"<li>{h(t)}</li>" for t in ts) + "</ul></li>"
                    for w, p, ts in N.PREP)

# ---------------------------------------------------------------- stripboard
strips = ""
for di, (date, label, call, scenes) in enumerate(N.DAYS, 1):
    for sc, sset, ie, tod, e8, cast, note in scenes:
        k, klabel = kind(ie, tod)
        cl = " ".join(f"c{c}" for c in cast)
        strips += (f"<div class='strip {k} {cl}'><span class='sc'>{sc}</span><span class='set'>{h(sset)}</span>"
                   f"<span class='kd'>{klabel}{(' · ' + tod.lower()) if tod and tod.lower() not in ('night', 'day') else ''}</span>"
                   f"<span class='cast'>{', '.join(map(str, cast)) or '–'}</span><span class='pg'>{pages(e8)}</span>"
                   + (f"<span class='note'>Note: {h(note)}</span>" if note else "") + "</div>")
    d8 = sum(s[4] for s in scenes)
    strips += f"<div class='eod'><b>End of Day {di} of {len(N.DAYS)}</b> · {label} · {date} · call {call} · {pages(d8)} pages</div>"
chips = "".join(f"<button type='button' class='chip' data-c='{c}' aria-pressed='false'>{c} · {h(n.split(' (')[0])}</button>"
                for c, n in N.CAST.items() if c != 10)

# ---------------------------------------------------------------- day out of days
def code(days, i):
    if i not in days:
        return ""
    if len(days) == 1:
        return "SWF"
    return "SW" if i == days[0] else "WF" if i == days[-1] else "W"


dood_head = "".join(f"<th scope='col'>Day {i + 1}<br><span>{N.DAYS[i][1]}</span></th>" for i in range(len(N.DAYS)))
dood = ""
for c, days in cast_days.items():
    if not days or c == 10:
        continue
    dood += (f"<tr><th scope='row'>{c} · {h(N.CAST[c])}</th>" + "".join(f"<td class='{'w' if code(days, i) else ''}'>{code(days, i)}</td>" for i in range(len(N.DAYS)))
             + f"<td>{len(days)}</td></tr>")

# ---------------------------------------------------------------- budget
groups = OrderedDict([("ATL", "Above the line"), ("BTL", "Production"), ("POST", "Post-production"), ("OTHER", "Other")])
top = ""
for g, gname in groups.items():
    accts = [b for b in N.BUDGET if b[2] == g]
    top += f"<tr class='grp'><th colspan='3'>{gname}</th></tr>"
    for acct, name, _, cash, ls in accts:
        detail = "".join(f"<li>{h(l)}{(' · ' + h(q)) if q else ''} <span class='how {cover(how).split()[0].lower()}'>{h(how)}</span></li>" for l, q, how in ls)
        top += (f"<tr><td class='num'>{acct}</td><td><details><summary>{name}</summary><ul>{detail}</ul></details></td>"
                f"<td class='num'>${cash:,}</td></tr>")
    top += f"<tr class='sub'><td></td><td>Total {gname.lower()}</td><td class='num'>${sum(b[3] for b in accts):,}</td></tr>"
atl = sum(b[3] for b in N.BUDGET if b[2] == "ATL")
cash_bars = "".join(f"<div class='bar'><span class='lbl'>{name}</span><span class='track'><span class='fill' style='width:{cash / 1800 * 100:.1f}%'></span></span><span class='v'>${cash:,}</span></div>"
                    for acct, name, g, cash, ls in sorted(N.BUDGET, key=lambda b: -b[3]) if cash)
cov_tiles = "".join(f"<div class='tile'><b>{cov[k]}</b><span>{k.lower()} lines</span></div>" for k in ["Cash", "Pro bono", "Students", "Lent or provided"])

# ---------------------------------------------------------------- risks
risk_rows = "".join(f"<tr><td><span class='phase'>{p}</span>{h(w)}</td><td>{h(i)}</td><td>{h(r) if r else '<span class=dim>–</span>'}</td><td>{h(l) if l else '<span class=dim>–</span>'}</td></tr>"
                    for p, w, i, r, l in N.RISKS)

HTML = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>Nibble: Planning a Thesis Shoot</title>
<meta name="description" content="The real production paperwork for Nibble, an MFA thesis short: a 18-week preproduction plan, a four-day stripboard, a $4,750 budget and a risk log." />
<link rel="stylesheet" href="../assets/sls.css" />
<style>
  [hidden] {{ display: none !important; }}
  .js-only {{ display: none !important; }} html.js .js-only {{ display: flex !important; }}
  .tiles {{ display: grid; grid-template-columns: repeat(auto-fit, minmax(140px, 1fr)); gap: 0.7rem; margin: 1.2rem 0; }}
  .tile {{ background: var(--sls-panel); border: 1px solid var(--sls-line); border-radius: var(--sls-radius); padding: 0.8rem 1rem; }}
  .tile b {{ display: block; font-family: var(--sls-display); font-weight: 800; font-size: 1.6rem; color: var(--sls-cyan); line-height: 1.1; }}
  .tile span {{ font-size: 0.85rem; color: var(--sls-dim); }}
  section.part {{ border-top: 1px solid var(--sls-line); margin-top: 2.6rem; padding-top: 0.6rem; }}
  .scroll {{ overflow-x: auto; }}
  table.gantt {{ border-collapse: separate; border-spacing: 2px; font-size: 0.78rem; min-width: 760px; }}
  .gantt th {{ font-family: var(--sls-display); font-weight: 700; color: var(--sls-dim); text-align: left; white-space: nowrap; padding-right: 0.5rem; }}
  .gantt thead th span {{ display: inline-block; writing-mode: vertical-rl; transform: rotate(180deg); font-weight: 500; font-size: 0.72rem; }}
  .gantt td.g {{ width: 30px; height: 26px; background: #262626; border-radius: 3px; text-align: center; }}
  .gantt td.on {{ background: var(--sls-navy); border: 1px solid var(--sls-cyan); color: var(--sls-white); font-weight: 700; }}
  .gantt tr:last-child td.on {{ background: #3a2a20; border-color: var(--sls-ember); }}
  .preplist {{ columns: 2; column-gap: 2rem; font-size: 0.9rem; padding-left: 1rem; }}
  .preplist > li {{ break-inside: avoid; margin-bottom: 0.6rem; }}
  .preplist ul {{ padding-left: 1rem; color: var(--sls-dim); }}
  .ph {{ font-family: var(--sls-display); font-size: 0.68rem; letter-spacing: 0.1em; text-transform: uppercase; color: var(--sls-tan); margin-left: 0.4rem; }}
  @media (max-width: 640px) {{ .preplist {{ columns: 1; }} }}

  .legend {{ display: flex; flex-wrap: wrap; gap: 0.5rem 1rem; font-size: 0.85rem; margin: 0.8rem 0; }}
  .legend i {{ display: inline-block; width: 1.4rem; height: 0.9rem; border-radius: 2px; vertical-align: -2px; margin-right: 0.35rem; border: 1px solid #555; }}
  .board {{ border: 1px solid var(--sls-line); border-radius: var(--sls-radius); overflow: hidden; }}
  .strip {{ display: grid; grid-template-columns: 3rem 1fr 8.5rem 5rem 3.5rem; gap: 0 0.6rem; align-items: center; color: #111;
            padding: 0.32rem 0.7rem; border-bottom: 1px solid rgba(0,0,0,0.18); font-size: 0.9rem; }}
  .strip .sc {{ font-family: var(--sls-display); font-weight: 800; }}
  .strip .kd {{ font-size: 0.78rem; text-transform: uppercase; letter-spacing: 0.05em; }}
  .strip .pg {{ text-align: right; font-variant-numeric: tabular-nums; }}
  .strip .note {{ grid-column: 2 / -1; font-size: 0.82rem; font-style: italic; padding: 0.15rem 0 0.1rem; }}
  .di {{ background: #fbfbf8; }} .de {{ background: #f6e27a; }} .ni {{ background: #9cc3ee; }} .ne {{ background: #9fd8a8; }} .pb {{ background: #cfcfcf; }}
  .eod {{ background: #000; color: #fff; padding: 0.45rem 0.7rem; font-size: 0.85rem; }}
  .eod b {{ font-family: var(--sls-display); }}
  .chips {{ display: flex; flex-wrap: wrap; gap: 0.4rem; margin: 0.6rem 0; }}
  .chip {{ font: inherit; font-size: 0.82rem; background: var(--sls-panel); color: var(--sls-white); border: 1px solid var(--sls-line); border-radius: 999px; padding: 0.2rem 0.7rem; cursor: pointer; }}
  .chip[aria-pressed="true"] {{ border-color: var(--sls-cyan); background: var(--sls-navy); }}
  .board.filtering .strip:not(.hit) {{ opacity: 0.22; }}
  @media (max-width: 640px) {{ .strip {{ grid-template-columns: 2.4rem 1fr 3rem; }} .strip .kd, .strip .cast {{ display: none; }} }}

  table.t {{ width: 100%; border-collapse: collapse; font-size: 0.92rem; }}
  .t th, .t td {{ text-align: left; padding: 0.5rem 0.5rem; border-bottom: 1px solid var(--sls-line); vertical-align: top; }}
  .t thead th {{ font-family: var(--sls-display); font-size: 0.7rem; letter-spacing: 0.1em; text-transform: uppercase; color: var(--sls-dim); }}
  .t .num {{ text-align: right; font-variant-numeric: tabular-nums; white-space: nowrap; }}
  .t tr.grp th {{ font-family: var(--sls-display); color: var(--sls-cyan); padding-top: 1rem; }}
  .t tr.sub td {{ color: var(--sls-dim); font-style: italic; }}
  .t details summary {{ cursor: pointer; }}
  .t details ul {{ margin: 0.4rem 0 0.2rem; padding-left: 1.1rem; color: var(--sls-dim); font-size: 0.86rem; }}
  .how {{ font-size: 0.75rem; border: 1px solid var(--sls-line); border-radius: 999px; padding: 0 0.45rem; margin-left: 0.3rem; white-space: nowrap; }}
  .how.cash {{ border-color: var(--sls-ember); color: var(--sls-ember); }}
  .t tr.grand td {{ font-family: var(--sls-display); font-weight: 800; font-size: 1.05rem; border-top: 2px solid var(--sls-cyan); }}
  .dood td, .dood th {{ text-align: center; }} .dood th[scope=row] {{ text-align: left; }}
  .dood td.w {{ background: var(--sls-navy); color: var(--sls-white); font-family: var(--sls-display); font-weight: 700; }}
  .dood thead span {{ font-weight: 400; text-transform: none; letter-spacing: 0; }}
  .bars {{ display: grid; gap: 0.45rem; margin: 1rem 0; }}
  .bar {{ display: grid; grid-template-columns: 9rem 1fr 4.5rem; gap: 0.6rem; align-items: center; font-size: 0.9rem; }}
  .bar .track {{ height: 14px; background: #262626; border-radius: 4px; overflow: hidden; }}
  .bar .fill {{ display: block; height: 100%; background: var(--sls-cyan); border-radius: 4px; }}
  .bar .v {{ text-align: right; font-variant-numeric: tabular-nums; }}
  .phase {{ display: block; font-family: var(--sls-display); font-size: 0.68rem; letter-spacing: 0.1em; text-transform: uppercase; color: var(--sls-tan); }}
  .dim {{ color: var(--sls-dim); }}
  @media (max-width: 700px) {{ table.risk thead {{ display: none; }} table.risk tr {{ display: block; border-bottom: 1px solid var(--sls-line); padding: 0.4rem 0; }}
    table.risk td {{ display: block; border: 0; padding: 0.2rem 0; }} }}

  @media print {{
    @page {{ size: letter; margin: 0.45in; }}
    html {{ color-scheme: light; }} html, body {{ background: #fff !important; color: #111; font-size: 9.5pt; }}
    .sls-bar, .sls-hero .btn, .chips, .noprint {{ display: none !important; }}
    .sls-foot {{ background: none; color: #555; padding: 0; margin-top: 0.2in; }}
    main.sls {{ max-width: none; padding: 0; }} .sls-hero {{ background: #fff; padding: 0; }} .sls-hero::after {{ display: none; }}
    h2, .lede, .tile b, .t tr.grp th {{ color: #003b5b !important; }} .tile, .card {{ background: #f4f1ec; border-color: #d7d0c8; }}
    .tile span, .dim, .gantt th, .t thead th, .t details ul, .preplist ul {{ color: #444 !important; }}
    .gantt td.g {{ background: #eee; }} .gantt td.on {{ background: #003b5b; }}
    details > ul {{ display: block; }} details summary {{ list-style: none; }}
    section.part {{ break-before: page; border: 0; }}
    .strip, .eod, .gantt td, .dood td.w, .bar .fill {{ -webkit-print-color-adjust: exact; print-color-adjust: exact; }}
    .t th, .t td {{ border-bottom-color: #ccc; padding: 0.05in; }}
    html.js .chips {{ display: none !important; }}
    .scroll {{ overflow: visible; }} table.gantt {{ min-width: 0; width: 100%; font-size: 7pt; }} .gantt td.g {{ width: auto; height: 18px; }}
    .callout {{ background: #f4f1ec !important; color: #111; }} .callout b:first-child {{ color: #003b5b; }}
    .bar .track {{ background: #e6e6e6; }} .bar .fill {{ background: #2a8db8; }}
    #prep {{ break-before: auto; }} .callout, .t tr {{ break-inside: avoid; }}
  }}
</style>
</head>
<body>
<header class="sls-bar">
  <a class="sls-wordmark" href="../../">Savage Light Studios</a>
  <nav><a href="nibble-production-paperwork.pdf">PDF</a></nav>
</header>

<main class="sls">
  <section class="sls-hero">
    <span class="slate"><span>Production</span><span>Nibble</span><span>2024</span></span>
    <h1>Nibble: Planning a Thesis Shoot</h1>
    <p class="lede">The real paperwork from a short film I produced, from prospectus to picture wrap.</p>
    <p class="dim">{h(N.SUMMARY)} I was also its associate producer, unit production manager and location manager.</p>
  </section>

  <div class="tiles">
    <div class="tile"><b>{prep_weeks}</b><span>weeks of preproduction</span></div>
    <div class="tile"><b>{len(N.DAYS)}</b><span>shoot days, plus a pickup day</span></div>
    <div class="tile"><b>{len(all_scenes)}</b><span>scenes, {pages(total8)} pages</span></div>
    <div class="tile"><b>${N.GRAND_TOTAL:,}</b><span>cash budget, all in</span></div>
    <div class="tile"><b>{cov['Pro bono'] + cov['Students'] + cov['Lent or provided']}</b><span>of {len(lines)} budget lines covered without cash</span></div>
  </div>
  <p class="dim" style="font-size:0.88rem">Transcribed from my MFA thesis appendix (University of New Orleans, 2024). Names, the production address and phone numbers are removed; people are shown by role.</p>

  <section class="part" id="prep">
    <span class="slate"><span>1</span><span>Preproduction</span></span>
    <h2>Eighteen weeks, week by week</h2>
    <p>The plan I wrote in April and worked to. Each square is a week with work in that phase; the number is how many tasks. Hover a square for the tasks.</p>
    <div class="scroll"><table class="gantt"><thead><tr><th></th>{heads}</tr></thead><tbody>{rows}</tbody></table></div>
    <details class="card" style="margin-top:1rem"><summary><b>The full schedule, as written</b></summary><ol class="preplist" style="list-style:none;margin-top:0.8rem">{prep_list}</ol></details>
  </section>

  <section class="part" id="board">
    <span class="slate"><span>2</span><span>Shooting schedule</span></span>
    <h2>Four days, one actor per day</h2>
    <p>The stripboard in shooting order. Each lead's scenes are grouped into one day (a Nell day, a Suzie day, a Dani day), so each lead works once, and the child actor's limits fit a single day. The playback scenes shoot first though they come last in the script, and the notes are the ones I wrote on the board.</p>
    <div class="legend"><span><i class="di"></i>Day interior</span><span><i class="de"></i>Day exterior</span><span><i class="ni"></i>Night interior</span><span><i class="ne"></i>Night exterior</span><span><i class="pb"></i>TV playback</span></div>
    <div class="chips noprint js-only" role="group" aria-label="Highlight a cast member">{chips}</div>
    <div class="board" id="boardstrips">{strips}</div>
    <p class="dim" style="font-size:0.85rem">Columns: scene, set, type, cast numbers, pages in eighths. Cast: {"; ".join(f"{c} {h(n)}" for c, n in N.CAST.items())}.</p>
  </section>

  <section class="part" id="dood">
    <span class="slate"><span>3</span><span>Day Out of Days</span></span>
    <h2>Each lead on set once</h2>
    <p>Read from the board: every human lead is SWF, starting, working and finishing on the same day. With a volunteer cast and a child actor, that keeps each lead's time on set to a single day.</p>
    <div class="scroll"><table class="t dood"><thead><tr><th scope="col">Cast</th>{dood_head}<th scope="col">Days</th></tr></thead><tbody>{dood}</tbody></table></div>
  </section>

  <section class="part" id="budget">
    <span class="slate"><span>4</span><span>Budget</span></span>
    <h2>$4,750, and everything that didn't cost cash</h2>
    <p>Built in EP Budgeting (Movie Magic) and kept as delivered. Cash went only where nothing could be borrowed, donated or made: the location, meals, the script supervisor, wardrobe and props, drives, and festival entries.</p>
    <div class="tiles">{cov_tiles}</div>
    <div class="bars" aria-label="Where the cash went">{cash_bars}</div>
    <div class="scroll"><table class="t"><thead><tr><th scope="col">Acct</th><th scope="col">Category (open for the lines)</th><th scope="col" class="num">Cash</th></tr></thead>
      <tbody>{top}<tr class='sub'><td></td><td>Total above the line</td><td class='num'>${atl:,}</td></tr><tr class='sub'><td></td><td>Total below the line (production, post and other)</td><td class='num'>${N.GRAND_TOTAL - atl:,}</td></tr><tr class='grand'><td></td><td>Grand total (fringes $0)</td><td class="num">${N.GRAND_TOTAL:,}</td></tr></tfoot></table></div>
  </section>

  <section class="part" id="risks">
    <span class="slate"><span>5</span><span>Risk and change</span></span>
    <h2>What changed, and what it taught me</h2>
    <p>From my thesis reflection, with the lessons in my own words.</p>
    <div class="scroll"><table class="t risk"><thead><tr><th scope="col">What happened</th><th scope="col">Impact</th><th scope="col">Response</th><th scope="col">Lesson</th></tr></thead><tbody>{risk_rows}</tbody></table></div>
    <div class="callout" style="margin-top:1.4rem"><b>What I'd do differently</b>Put at least one lighting instrument on every shot. Shoot above the delivery resolution, to allow reframing. Tech-scout every location before booking it. Hire practical effects, and an animal trainer, rather than doing it all myself.</div>
  </section>
</main>

<footer class="sls-foot">© 2026 Savage Light Studios · Production paperwork by Feralucce Savage, from the MFA thesis film Nibble (University of New Orleans, 2024).</footer>
<script>
(function () {{
  document.documentElement.classList.add("js");
  var board = document.getElementById("boardstrips");
  document.querySelectorAll(".chip").forEach(function (b) {{
    b.addEventListener("click", function () {{
      var on = b.getAttribute("aria-pressed") !== "true";
      document.querySelectorAll(".chip").forEach(function (x) {{ x.setAttribute("aria-pressed", "false"); }});
      board.querySelectorAll(".strip").forEach(function (s) {{ s.classList.remove("hit"); }});
      board.classList.toggle("filtering", on);
      if (on) {{
        b.setAttribute("aria-pressed", "true");
        board.querySelectorAll(".strip.c" + b.dataset.c).forEach(function (s) {{ s.classList.add("hit"); }});
      }}
    }});
  }});
}})();
</script>
</body>
</html>
"""
(HERE / "index.html").write_text(HTML, encoding="utf-8")
print("index.html", len(HTML), "bytes;", len(all_scenes), "scenes;", pages(total8), "pages; coverage", dict(cov))
