/*! NumerKSeF – wspólne elementy interfejsu */
(function () {
  "use strict";
  var K = window.KSEF;
  function $(id) { return document.getElementById(id); }

  // menu mobilne
  var tg = document.querySelector(".nav-toggle"), nav = document.getElementById("site-nav");
  if (tg && nav) {
    tg.addEventListener("click", function () {
      var open = nav.classList.toggle("open");
      tg.setAttribute("aria-expanded", open ? "true" : "false");
    });
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape" && nav.classList.contains("open")) { nav.classList.remove("open"); tg.setAttribute("aria-expanded", "false"); tg.focus(); }
    });
  }

  // tryb jasny / ciemny: prefers-color-scheme + zapamiętany wybór (localStorage "theme")
  var root = document.documentElement, thBtn = document.querySelector(".theme-toggle");
  function stored() { try { var t = localStorage.getItem("theme"); return t === "dark" || t === "light" ? t : null; } catch (e) { return null; } }
  function sysDark() { return !!(window.matchMedia && window.matchMedia("(prefers-color-scheme: dark)").matches); }
  function applyTheme(t) {
    root.setAttribute("data-theme", t);
    if (thBtn) { thBtn.setAttribute("aria-pressed", t === "dark" ? "true" : "false"); thBtn.setAttribute("aria-label", t === "dark" ? "Tryb jasny" : "Tryb ciemny"); }
  }
  applyTheme(stored() || root.getAttribute("data-theme") || (sysDark() ? "dark" : "light"));
  if (thBtn) thBtn.addEventListener("click", function () {
    var t = root.getAttribute("data-theme") === "dark" ? "light" : "dark";
    applyTheme(t);
    try { localStorage.setItem("theme", t); } catch (e) {}
  });
  if (window.matchMedia) {
    var mq = window.matchMedia("(prefers-color-scheme: dark)");
    var onSys = function (ev) { if (!stored()) applyTheme(ev.matches ? "dark" : "light"); };
    if (mq.addEventListener) mq.addEventListener("change", onSys); else if (mq.addListener) mq.addListener(onSys);
  }

  function copyText(text, btn) {
    if (!text) return;
    function done(ok) {
      if (!btn) return;
      var old = btn.getAttribute("data-label") || btn.textContent;
      btn.setAttribute("data-label", old);
      btn.textContent = ok ? "Skopiowano ✓" : "Zaznacz i Ctrl+C";
      btn.classList.add("copied-btn");
      var live = $("live");
      if (live) live.textContent = ok ? "Skopiowano do schowka" : "Nie udało się skopiować";
      setTimeout(function () { btn.textContent = old; }, 1600);
    }
    function fallback() {
      var ta = document.createElement("textarea");
      ta.value = text; ta.setAttribute("readonly", ""); ta.style.position = "fixed"; ta.style.opacity = "0";
      document.body.appendChild(ta); ta.select();
      var ok = false;
      try { ok = document.execCommand("copy"); } catch (e) {}
      document.body.removeChild(ta);
      done(ok);
    }
    if (navigator.clipboard && window.isSecureContext) navigator.clipboard.writeText(text).then(function () { done(true); }, fallback);
    else fallback();
  }
  // przyciski z data-copy="id elementu" lub data-copy-text
  document.addEventListener("click", function (e) {
    var b = e.target.closest && e.target.closest("[data-copy],[data-copy-text]");
    if (!b) return;
    var t = b.getAttribute("data-copy-text");
    if (t == null) { var el = $(b.getAttribute("data-copy")); t = el ? (el.getAttribute("data-value") || el.value || el.textContent) : ""; }
    if (t) copyText(t, b);
  });

  var ICON = { ok: "✓", bad: "✕", warn: "!", info: "i" };
  function statusBox(el, level, head, opts) {
    opts = opts || {};
    if (!level) { el.className = "status"; el.innerHTML = ""; return; }
    var h = '<p class="status-head"><span class="ico" aria-hidden="true">' + ICON[level] + "</span>" + K.esc(head) + "</p>";
    if (opts.errors && opts.errors.length) h += '<ul class="reasons-bad">' + opts.errors.map(function (x) { return "<li>" + K.esc(x) + "</li>"; }).join("") + "</ul>";
    if (opts.warnings && opts.warnings.length) h += '<ul class="reasons-warn">' + opts.warnings.map(function (x) { return "<li>" + K.esc(x) + "</li>"; }).join("") + "</ul>";
    if (opts.notes && opts.notes.length) h += "<ul>" + opts.notes.map(function (x) { return "<li>" + K.esc(x) + "</li>"; }).join("") + "</ul>";
    if (opts.html) h += opts.html;
    el.className = "status " + level;
    el.innerHTML = h;
  }
  function mark(v) {
    if (v === true) return ' <span class="yes" aria-label="poprawne">✓</span>';
    if (v === false) return ' <span class="no" aria-label="błędne">✕</span>';
    return ' <span class="maybe" aria-label="do sprawdzenia">?</span>';
  }
  function parts(rows) {
    return '<dl class="parts">' + rows.map(function (r) { return "<div><dt>" + r[0] + "</dt><dd>" + r[1] + "</dd></div>"; }).join("") + "</dl>";
  }
  function ymdToPl(d) { return d && d.length === 8 ? d.slice(6, 8) + "." + d.slice(4, 6) + "." + d.slice(0, 4) : d; }
  function isoToPl(d) { var m = /^(\d{4})-(\d{2})-(\d{2})$/.exec(d || ""); return m ? m[3] + "." + m[2] + "." + m[1] : (d || "–"); }

  // szczegóły numeru KSeF / IZ
  function describe(r) {
    var p = r.parts, rows = [];
    if (!p) return "";
    if (r.kind === "iz") {
      rows.push(["NIP", '<span class="mono">' + K.formatNip(p.nip) + "</span>" + mark(p.nipOk)]);
      rows.push(["Oznaczenie i miesiąc", "IZ · " + (p.month < 10 ? "0" : "") + p.month + "." + p.year + mark(p.dateOk)]);
      rows.push(["Część techniczna", '<span class="mono">' + p.tech + "</span>"]);
      rows.push(["Suma kontrolna <small>(podana / obliczona)</small>", '<span class="mono">' + p.given + " / " + p.calc + "</span>" + mark(p.crcOk)]);
    } else {
      rows.push([p.nip ? "NIP sprzedawcy" : "Identyfikator", '<span class="mono">' + (p.nip ? K.formatNip(p.nip) : K.esc(p.prefix)) + "</span>" + mark(p.nip ? p.nipOk : null)]);
      rows.push(["Data przyjęcia do KSeF", ymdToPl(p.date) + mark(p.dateOk)]);
      rows.push(["Część techniczna", '<span class="mono">' + p.tech + "</span>"]);
      if (p.calc) rows.push(["Suma kontrolna CRC-8 <small>(podana / obliczona)</small>", '<span class="mono">' + p.given + " / " + p.calc + "</span>" + mark(p.crcOk)]);
      else rows.push(["Suma kontrolna", '<span class="mono">' + p.given + "</span> (nieweryfikowana)"]);
    }
    return parts(rows);
  }
  function showCheck(el, r) {
    var label = r.kind === "iz" ? "identyfikator zbiorczy" : "numer KSeF";
    var head = r.status === "ok" ? "Poprawny " + label : r.status === "warn" ? "Do sprawdzenia: " + label : "Błędny " + label;
    var notes = r.notes.slice();
    if (r.fixes.length) notes.unshift("Poprawiono zapis: " + r.fixes.join(", ") + ".");
    statusBox(el, r.status, head, { errors: r.errors, warnings: r.warnings, notes: notes, html: '<p class="mono mt8 mb0">' + K.esc(r.input) + "</p>" + describe(r) });
  }

  function readFile(file, asText) {
    return new Promise(function (res, rej) {
      var fr = new FileReader();
      fr.onload = function () { res(fr.result); };
      fr.onerror = function () { rej(fr.error); };
      if (asText) fr.readAsText(file, "utf-8"); else fr.readAsArrayBuffer(file);
    });
  }
  function dropZone(zone, input, onFiles) {
    if (!zone) return;
    ["dragenter", "dragover"].forEach(function (ev) { zone.addEventListener(ev, function (e) { e.preventDefault(); zone.classList.add("drag"); }); });
    ["dragleave", "drop"].forEach(function (ev) { zone.addEventListener(ev, function (e) { e.preventDefault(); zone.classList.remove("drag"); }); });
    zone.addEventListener("drop", function (e) { if (e.dataTransfer && e.dataTransfer.files.length) onFiles(e.dataTransfer.files); });
    input.addEventListener("change", function () { if (input.files.length) onFiles(input.files); });
  }
  function download(name, content, type) {
    var blob = new Blob([content], { type: type || "text/csv;charset=utf-8" });
    var a = document.createElement("a");
    a.href = URL.createObjectURL(blob); a.download = name;
    document.body.appendChild(a); a.click();
    setTimeout(function () { URL.revokeObjectURL(a.href); a.remove(); }, 500);
  }
  function counter(el, n, max) {
    el.textContent = n + " / " + max + " " + K.plural(n);
    el.classList.toggle("over", n > max);
  }

  window.UI = { $: $, copyText: copyText, statusBox: statusBox, mark: mark, parts: parts, describe: describe, showCheck: showCheck,
    readFile: readFile, dropZone: dropZone, download: download, counter: counter, ymdToPl: ymdToPl, isoToPl: isoToPl };
})();
