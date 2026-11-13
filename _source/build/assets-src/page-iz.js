/*! Walidator identyfikatora zbiorczego */
(function () {
  "use strict";
  var K = window.KSEF, U = window.UI, $ = U.$;
  var inp = $("iz-in"), res = $("iz-res");
  function check() {
    var v = inp.value;
    if (!v.trim()) { U.statusBox(res, null); inp.removeAttribute("aria-invalid"); return; }
    var n = K.normalize(v).value, r;
    if (/^[0-9A-Z]{10}-\d{8}-/.test(n)) {
      r = K.checkKsef(v);
      U.showCheck(res, r);
      var extra = document.createElement("p");
      extra.className = "note";
      extra.textContent = "To jest numer KSeF pojedynczej faktury, a nie identyfikator zbiorczy (ten ma po NIP oznaczenie „IZ” i rok-miesiąc).";
      res.appendChild(extra);
    } else {
      r = K.checkIZ(v);
      U.showCheck(res, r);
    }
    inp.setAttribute("aria-invalid", r.status === "bad" ? "true" : "false");
    if (r.valid) {
      var row = document.createElement("div");
      row.className = "btns mt10 mb0";
      var cb = document.createElement("button");
      cb.type = "button"; cb.className = "btn ghost"; cb.id = "iz-copy";
      cb.setAttribute("data-copy-text", r.input);
      cb.textContent = r.kind === "iz" ? "Kopiuj identyfikator" : "Kopiuj numer";
      row.appendChild(cb); res.appendChild(row);
    }
  }
  function checkShow() { check(); U.reveal(inp, res); }
  inp.addEventListener("input", check);
  $("iz-check").addEventListener("click", checkShow);
  U.onEnter(inp, checkShow);
  $("iz-ex").addEventListener("click", function () { inp.value = K.EXAMPLE_IZ; check(); inp.focus(); });
  $("iz-clear").addEventListener("click", function () { inp.value = ""; check(); inp.focus(); });
})();
