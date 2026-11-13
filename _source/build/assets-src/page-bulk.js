/*! Masowe sprawdzanie numerów KSeF */
(function () {
  "use strict";
  var K = window.KSEF, U = window.UI, $ = U.$;
  var ta = $("b-in"), tbody = $("b-body"), sum = $("b-sum"), rows = [];
  var LBL = { ok: "Poprawny", warn: "Do sprawdzenia", bad: "Błędny", none: "Brak numeru" };
  function analyse() {
    var statement = $("b-mode-statement").checked;
    var lines = ta.value.split(/\r?\n/);
    rows = [];
    lines.forEach(function (line, i) {
      if (!line.trim()) return;
      var found = K.findCandidates(line);
      if (!found.length) {
        // pojedynczy wpis bez separatorów – sprawdź całą linię (np. literówka w długości)
        var cells = line.split(/[;,\t]/).map(function (c) { return c.trim(); }).filter(Boolean);
        var guess = cells.filter(function (c) { return /^[0-9A-Z]{10}[-–—]/i.test(c) && c.length >= 30 && c.length <= 40; })[0];
        if (guess) found = [guess];
      }
      if (!found.length) {
        if (statement || line.split(/[;,\t]/).length > 1 || line.length > 40) rows.push({ line: i + 1, src: line.trim(), num: "", status: "none", type: "", nip: "", date: "", reason: "W tym wierszu nie znaleziono numeru KSeF ani identyfikatora zbiorczego." });
        else rows.push(mk(i + 1, line.trim(), K.checkKsef(line)));
        return;
      }
      found.forEach(function (f) { rows.push(mk(i + 1, line.trim(), K.checkKsef(f))); });
    });
    render();
  }
  function mk(n, src, r) {
    var p = r.parts || {};
    var date = r.kind === "iz" ? (p.month ? (p.month < 10 ? "0" : "") + p.month + "." + p.year : "") : (p.date ? U.ymdToPl(p.date) : "");
    return { line: n, src: src, num: r.input, status: r.status, type: r.kind === "iz" ? "Identyfikator zbiorczy" : r.kind === "ksef1" ? "KSeF 1.0 (36 zn.)" : "Numer KSeF",
      nip: p.nip || p.prefix || "", date: date, reason: (r.errors.concat(r.warnings).join(" ") || (r.notes[0] || "")) + (r.fixes.length ? " (Poprawiono zapis: " + r.fixes.join(", ") + ".)" : "") };
  }
  function render() {
    var c = { ok: 0, warn: 0, bad: 0, none: 0 };
    rows.forEach(function (r) { c[r.status]++; });
    var only = $("b-only-bad").checked;
    tbody.innerHTML = rows.filter(function (r) { return !only || r.status !== "ok"; }).map(function (r) {
      return "<tr><td>" + r.line + '</td><td><span class="badge ' + (r.status === "none" ? "info" : r.status) + '">' + LBL[r.status] + '</span></td><td class="mono">' + K.esc(r.num || "—") + "</td><td>" + K.esc(r.type) + '</td><td class="mono">' + K.esc(r.nip) + "</td><td>" + K.esc(r.date) + "</td><td>" + K.esc(r.reason) + "</td></tr>";
    }).join("");
    $("b-table").hidden = !rows.length;
    $("b-actions").hidden = !rows.length;
    if (!rows.length) { U.statusBox(sum, null); return; }
    var lvl = c.bad ? "bad" : (c.warn || c.none) ? "warn" : "ok";
    U.statusBox(sum, lvl, "Sprawdzono " + rows.length + " " + K.plural(rows.length, "pozycję", "pozycje", "pozycji") + ": " + c.ok + " poprawnych, " + c.warn + " do sprawdzenia, " + c.bad + " błędnych" + (c.none ? ", " + c.none + " bez numeru" : "") + ".");
  }
  function csv() {
    var data = [["Wiersz", "Status", "Numer", "Typ", "NIP", "Data", "Uwagi", "Tekst źródłowy"]];
    rows.forEach(function (r) { data.push([r.line, LBL[r.status], r.num, r.type, r.nip, r.date, r.reason, r.src]); });
    return K.toCsv(data);
  }
  ta.addEventListener("input", analyse);
  $("b-check").addEventListener("click", analyse);
  $("b-only-bad").addEventListener("change", render);
  $("b-mode-list").addEventListener("change", analyse);
  $("b-mode-statement").addEventListener("change", analyse);
  $("b-ex").addEventListener("click", function () {
    $("b-mode-list").checked = true;
    ta.value = ["5265877635-20250826-0100001AF629-AF", "5265877635-20250826-0100001AF629-7C", "1111111111-IZ202607-65ED02180000-E7", "9510001233-20261102-01A3F0C2B7D4-B8", "5265877635-2025O826-0100001AF629-AF"].join("\n");
    analyse();
  });
  $("b-ex-statement").addEventListener("click", function () {
    $("b-mode-statement").checked = true;
    ta.value = ["2026-11-02;ACME SP. Z O.O.;1230,00;5265877635-20250709-0100E01D6840-3C FV 7/2026", "2026-11-03;JAN KOWALSKI;450,00;Zapłata za fakturę 15/10/2026", "2026-11-05;BUDMAR;24600,00;/VAT/4600,00/IDC/1111111111/INV/1111111111-IZ202607-65ED02180000-E7", "2026-11-06;XYZ;99,00;9510001233-20261102-01A3F0C2B7D4-B9"].join("\n");
    analyse();
  });
  $("b-clear").addEventListener("click", function () { ta.value = ""; analyse(); });
  $("b-csv").addEventListener("click", function () { U.download("wyniki-numery-ksef.csv", csv()); });
  $("b-copy").addEventListener("click", function (e) {
    U.copyText(rows.map(function (r) { return [r.line, LBL[r.status], r.num, r.reason].join("\t"); }).join("\n"), e.currentTarget);
  });
  U.dropZone($("b-drop"), $("b-file"), function (files) {
    Promise.all(Array.prototype.map.call(files, function (f) { return U.readFile(f, true); })).then(function (texts) {
      ta.value = texts.join("\n"); analyse();
    });
  });
})();
