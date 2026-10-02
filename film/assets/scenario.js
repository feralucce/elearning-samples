/* Branching scenario player.
   Reads the page's markup: each .beat is one screen; .opt items carry
   data-m="trust,schedule,safety", data-best, data-next and data-lit.
   Nothing is saved: a refresh starts a new day. */
(function () {
  "use strict";
  var root = document.documentElement;
  root.classList.add("js");

  var NAMES = ["Crew trust", "Schedule", "Safety"];
  var start = [50, 50, 50];
  var meters, log, current;
  var beats = Array.prototype.slice.call(document.querySelectorAll(".beat"));
  var byId = {};
  beats.forEach(function (b) { byId[b.id] = b; });
  var live = document.getElementById("live");

  function $(sel, el) { return (el || document).querySelector(sel); }
  function $$(sel, el) { return Array.prototype.slice.call((el || document).querySelectorAll(sel)); }
  function clamp(v) { return Math.max(0, Math.min(100, v)); }
  function text(el) { return el ? el.textContent.replace(/\s+/g, " ").trim() : ""; }

  function drawMeters() {
    $$(".meterbar .meter").forEach(function (m, i) {
      var v = meters[i];
      m.querySelector(".fill").style.width = v + "%";
      m.querySelector(".v").textContent = v < 40 ? v + " · low" : v;
      m.classList.toggle("low", v < 40);
    });
  }

  function apply(delta) {
    var parts = [];
    delta.forEach(function (d, i) {
      if (!d) return;
      meters[i] = clamp(meters[i] + d);
      parts.push('<span class="' + (d > 0 ? "up" : "down") + '">' + NAMES[i] + " " + (d > 0 ? "+" : "−") + Math.abs(d) + "</span>");
    });
    drawMeters();
    var said = delta.map(function (d, i) { return d ? NAMES[i] + " " + (d > 0 ? "up " : "down ") + Math.abs(d) + ", now " + meters[i] : ""; }).filter(Boolean).join(". ");
    live.textContent = said || "No change to the meters.";
    return parts.join(" &nbsp;·&nbsp; ");
  }

  function parseM(s) { return (s || "0,0,0").split(",").map(Number); }

  function show(id) {
    beats.forEach(function (b) { b.classList.remove("on"); });
    var b = byId[id];
    current = b;
    b.classList.add("on");
    if (b.dataset.enter) enter[b.dataset.enter](b);
    var h = $("h2, h1", b);
    if (h) { h.setAttribute("tabindex", "-1"); h.focus({ preventScroll: true }); }
    window.scrollTo(0, 0);
  }

  function nextOf(b, opt) { return (opt && opt.dataset.next) || b.dataset.next; }

  function finishBeat(b, opt, resultHtml, isBest, chose, best) {
    var out = $(".outcome", b);
    out.className = "outcome on callout" + (isBest ? "" : " ember");
    out.innerHTML = "<b>" + (isBest ? "Nice" : "What happens") + "</b>" + resultHtml + '<div class="deltas">' + out.dataset.deltas + "</div>";
    var on = $(".onset", b); if (on) on.classList.add("on");
    if (b.dataset.title) log.push({ title: b.dataset.title, chose: chose, best: best, rule: text($(".onset", b)).replace(/^On set\s*/, ""), ok: isBest });
    var row = $(".next-row", b);
    row.classList.add("on");
    var btn = $("button", row);
    btn.onclick = function () { show(nextOf(b, opt)); };
    out.setAttribute("tabindex", "-1");
    out.focus();
  }

  // single-choice beats
  $$(".decision:not([data-type])").forEach(function (dec) {
    var b = dec.closest(".beat");
    var opts = $$(".opt", dec);
    var bestOpt = opts.filter(function (o) { return o.hasAttribute("data-best"); })[0];
    var map = $(".map", b);
    opts.forEach(function (o) {
      var btn = document.createElement("button");
      btn.type = "button";
      btn.className = "choice";
      btn.dataset.key = o.dataset.key;
      btn.setAttribute("aria-pressed", "false");
      btn.innerHTML = $(".say", o).innerHTML;
      o.insertBefore(btn, o.firstChild);
      $(".say", o).hidden = true;
      btn.addEventListener("click", function () { choose(o); });
    });
    function choose(o) {
      if (dec.dataset.done) return;
      dec.dataset.done = "1";
      opts.forEach(function (x) { var bt = $(".choice", x); bt.disabled = true; bt.setAttribute("aria-pressed", x === o ? "true" : "false"); });
      if (map) {
        $$(".spot", map).forEach(function (s) { s.classList.toggle("picked", s.dataset.key === o.dataset.key); s.setAttribute("tabindex", "-1"); });
        (o.dataset.lit || "").split(" ").filter(Boolean).forEach(function (l) { map.classList.add("lit-" + l); });
      }
      $(".outcome", b).dataset.deltas = apply(parseM(o.dataset.m));
      finishBeat(b, o, $(".result", o).innerHTML, o === bestOpt, text($(".say", o)), text($(".say", bestOpt)));
    }
    if (map) {
      $$(".spot", map).forEach(function (s) {
        s.setAttribute("tabindex", "0");
        s.setAttribute("role", "button");
        s.setAttribute("aria-label", "Stand at spot " + s.dataset.key);
        var o = opts.filter(function (x) { return x.dataset.key === s.dataset.key; })[0];
        s.addEventListener("click", function () { choose(o); });
        s.addEventListener("keydown", function (e) { if (e.key === "Enter" || e.key === " ") { e.preventDefault(); choose(o); } });
      });
    }
  });

  // multi-select beats (wrap checklist)
  $$('.decision[data-type="multi"]').forEach(function (dec) {
    var b = dec.closest(".beat");
    var opts = $$(".opt", dec);
    var ul = document.createElement("ul");
    ul.className = "checks";
    opts.forEach(function (o, i) {
      var li = document.createElement("li");
      li.innerHTML = '<label><input type="checkbox" data-i="' + i + '"> <span>' + $(".say", o).innerHTML + '</span><span class="tag"></span></label>';
      ul.appendChild(li);
    });
    $("ol.opts", dec).hidden = true;
    dec.appendChild(ul);
    var done = document.createElement("button");
    done.type = "button"; done.className = "btn"; done.textContent = "That's everything";
    dec.appendChild(done);
    done.addEventListener("click", function () {
      done.disabled = true;
      var allRight = true, missed = [];
      $$("input", ul).forEach(function (inp) {
        var o = opts[+inp.dataset.i], right = o.dataset.right === "1", lab = inp.closest("label");
        inp.disabled = true;
        if (inp.checked !== right) { allRight = false; if (right) missed.push(text($(".say", o))); }
        if (right) { lab.classList.add("right"); $(".tag", lab).textContent = inp.checked ? "✓ Done" : "Missed"; }
        else if (inp.checked) { lab.classList.add("wrong"); $(".tag", lab).textContent = "Not yet"; }
      });
      var d = parseM(allRight ? dec.dataset.pass : dec.dataset.fail);
      $(".outcome", b).dataset.deltas = apply(d);
      var res = allRight ? dec.dataset.passText : dec.dataset.failText + (missed.length ? " You missed: " + missed.join("; ") + "." : "");
      var best = opts.filter(function (o) { return o.dataset.right === "1"; }).map(function (o) { return text($(".say", o)); }).join("; ");
      finishBeat(b, null, res, allRight, allRight ? "All four" : "Left before finishing", best);
    });
  });

  var enter = {
    ending: function (b) {
      var t = meters[0], s = meters[2];
      var which = s < 40 ? "talk" : (s >= 60 && t >= 60 ? "back" : "day");
      $$(".end", b).forEach(function (e) { e.hidden = e.dataset.end !== which; });
      var reads = [
        t >= 60 ? "the crew would work with you again." : t >= 40 ? "the crew is still making up its mind." : "the crew has doubts.",
        meters[1] >= 60 ? "you helped the day run on time." : meters[1] >= 40 ? "you cost a few minutes here and there." : "you cost the day real time.",
        s >= 60 ? "you kept people safe." : s >= 40 ? "you got there, late." : "a near miss happened on your watch."
      ];
      $(".final-reads", b).innerHTML = NAMES.map(function (n, i) { return "<li><b>" + n + " " + meters[i] + ":</b> " + reads[i] + "</li>"; }).join("");
    },
    debrief: function (b) {
      var ok = log.filter(function (r) { return r.ok; }).length;
      $(".score", b).textContent = ok + " / " + log.length;
      $("tbody", b).innerHTML = log.map(function (r) {
        return "<tr><td data-h='Moment'>" + r.title + "</td><td data-h='You chose'><span class='mark " + (r.ok ? "ok'>✓" : "no'>✗") + "</span> " + r.chose +
          "</td><td data-h='Best'>" + (r.ok ? "Same" : r.best) + "</td><td data-h='The rule'>" + r.rule + "</td></tr>";
      }).join("");
    }
  };

  // reaction check (not recorded in this sample)
  $$(".rating button").forEach(function (btn) {
    btn.addEventListener("click", function () {
      $$(".rating button").forEach(function (x) { x.setAttribute("aria-pressed", x === btn ? "true" : "false"); });
      $(".rating-thanks").hidden = false;
    });
  });

  function reset() {
    meters = start.slice();
    log = [];
    drawMeters();
    $$(".decision").forEach(function (dec) {
      delete dec.dataset.done;
      $$(".choice", dec).forEach(function (bt) { bt.disabled = false; bt.setAttribute("aria-pressed", "false"); });
      $$(".checks input", dec).forEach(function (i) { i.checked = false; i.disabled = false; });
      $$(".checks label", dec).forEach(function (l) { l.className = ""; $(".tag", l).textContent = ""; });
      $$("button.btn", dec).forEach(function (bt) { bt.disabled = false; });
    });
    $$(".outcome").forEach(function (o) { o.className = "outcome"; o.innerHTML = ""; });
    $$(".onset, .next-row").forEach(function (x) { x.classList.remove("on"); });
    $$(".map").forEach(function (m) { m.classList.remove("lit-frame", "lit-eyeline"); $$(".spot", m).forEach(function (s) { s.classList.remove("picked"); s.setAttribute("tabindex", "0"); }); });
  }

  $$("[data-go]").forEach(function (btn) {
    btn.addEventListener("click", function () {
      if (btn.dataset.go === "restart") { reset(); show("title"); return; }
      show(btn.dataset.go);
    });
  });

  reset();
  show("title");
})();
