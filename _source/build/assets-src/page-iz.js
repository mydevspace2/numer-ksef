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
  }
  inp.addEventListener("input", check);
  $("iz-check").addEventListener("click", check);
  $("iz-ex").addEventListener("click", function () { inp.value = K.EXAMPLE_IZ; check(); inp.focus(); });
  $("iz-clear").addEventListener("click", function () { inp.value = ""; check(); inp.focus(); });
})();
