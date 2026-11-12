/*! Generator komunikatu MPP */
(function () {
  "use strict";
  var K = window.KSEF, U = window.UI, $ = U.$;
  var F = ["vat", "gross", "nip", "inv", "txt"];
  function val(id) { return $("m-" + id).value; }
  function run() {
    var own = $("m-own").checked;
    $("m-inv").disabled = own;
    $("m-inv-wrap").style.opacity = own ? ".55" : "1";
    var r = K.buildMpp({ vat: val("vat"), gross: val("gross"), nip: val("nip"), inv: own ? "" : val("inv"), txt: val("txt"), own: own, date: val("date") });
    var touched = F.some(function (f) { return val(f).trim(); });
    F.forEach(function (f) {
      var el = $("m-" + f), msg = $("m-" + f + "-msg");
      var errs = (r.fieldErrors[f] || []), info = (r.fieldInfo[f] || []);
      var show = el.value.trim() || (touched && f !== "gross" && f !== "txt");
      if (f === "inv" && own) show = false;
      el.setAttribute("aria-invalid", show && errs.length ? "true" : "false");
      msg.innerHTML = show ? errs.map(function (x) { return '<span class="no">✕ ' + K.esc(x) + "</span>"; }).concat(info.map(function (x) { return '<span class="maybe">! ' + K.esc(x) + "</span>"; })).join("<br>") : "";
    });
    var kindLbl = { ksef: "numer KSeF ✓", iz: "identyfikator zbiorczy ✓", invoice: "numer faktury (spoza KSeF)", own: "przekazanie własne" }[r.invKind] || "";
    $("m-inv-kind").textContent = kindLbl && !(r.fieldErrors.inv || []).length ? "Rozpoznano: " + kindLbl : "";
    var out = $("m-out");
    out.textContent = r.text || "Uzupełnij kwotę VAT, NIP i numer KSeF – komunikat pojawi się tutaj.";
    out.classList.toggle("placeholder", !r.text);
    out.setAttribute("data-value", r.text);
    U.counter($("m-count"), r.length, K.MPP_MAX);
    $("m-copy").disabled = !r.ok;
    var l4 = $("m-lines4");
    l4.innerHTML = r.lines4.map(function (l, i) {
      var sep = l.indexOf("/", 1) + 1, code = l.slice(0, sep), v = l.slice(sep);
      return '<div><dt>Linia ' + (i + 1) + " " + code + '</dt><dd class="mono" id="m-l' + i + '">' + K.esc(l) + '</dd><dd><button type="button" class="btn ghost small" data-copy-text="' + K.esc(l) + '">Kopiuj linię</button> <button type="button" class="btn ghost small" data-copy-text="' + K.esc(v) + '">Tylko wartość</button></dd></div>';
    }).join("");
    $("m-lines35").innerHTML = r.lines35.map(function (l) { return "<li>" + K.esc(l) + "</li>"; }).join("");
    $("m-split").hidden = !r.text;
    var st = $("m-stat");
    if (!touched) U.statusBox(st, null);
    else if (r.ok) U.statusBox(st, r.warnings.length ? "warn" : "ok", r.warnings.length ? "Komunikat poprawny – sprawdź uwagi" : "Komunikat MPP poprawny (" + r.length + " / 140 znaków)", { warnings: r.warnings });
    else U.statusBox(st, "bad", "Komunikat wymaga poprawek", { errors: r.errors, warnings: r.warnings });
  }
  F.concat(["date"]).forEach(function (f) { $("m-" + f).addEventListener("input", run); });
  $("m-own").addEventListener("change", run);
  $("m-ex").addEventListener("click", function () {
    $("m-own").checked = false;
    $("m-vat").value = "230,00"; $("m-gross").value = "1230,00"; $("m-nip").value = K.EXAMPLE_NIP;
    $("m-inv").value = K.EXAMPLE_KSEF; $("m-txt").value = "FV 12/11/2026"; run();
  });
  $("m-ex-iz").addEventListener("click", function () {
    $("m-own").checked = false;
    $("m-vat").value = "4600,00"; $("m-gross").value = "24600,00"; $("m-nip").value = "1111111111";
    $("m-inv").value = K.EXAMPLE_IZ; $("m-txt").value = "faktury lipiec 2026"; run();
  });
  $("m-clear").addEventListener("click", function () { F.forEach(function (f) { $("m-" + f).value = ""; }); $("m-own").checked = false; run(); });
  // dane z adresu (np. z generatora XML)
  try {
    var q = new URLSearchParams(location.search);
    F.forEach(function (f) { if (q.get(f)) $("m-" + f).value = q.get(f); });
  } catch (e) {}
  run();
})();
