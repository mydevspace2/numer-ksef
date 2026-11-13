/*! Ankieta: czy KSeF dotyczy mojej JDG */
(function () {
  "use strict";
  var K = window.KSEF, U = window.UI, $ = U.$;
  var form = $("j-form"), out = $("j-out");
  var LVL = { must: "Obowiązek", info: "Informacja", pending: "W toku legislacji" };
  function get(name) { var el = form.querySelector('input[name="' + name + '"]:checked'); return el ? el.value : ""; }
  function run(e) {
    if (e) e.preventDefault();
    var a = { b2b: get("b2b"), vat: get("vat"), small: get("small"), cash: get("cash"), pays: get("pays"), mpp: get("mpp") };
    var missing = ["b2b", "vat", "pays"].filter(function (k) { return !a[k]; });
    if (missing.length) { out.innerHTML = '<p class="status warn"><strong>Odpowiedz na pytania 1, 2 i 5</strong> – pozostałe są opcjonalne.</p>'; return; }
    var items = K.evaluateJdg(a);
    out.innerHTML = '<h3>Twoja lista zmian <small class="updated">(stan prawny na 13 listopada 2026 r.)</small></h3><ul class="checklist">' + items.map(function (it) {
      return '<li class="' + it.level + '"><span class="when">' + K.esc(it.date) + " · " + LVL[it.level] + "</span>" + K.esc(it.text) + "</li>";
    }).join("") + '</ul><p class="hint">To orientacyjna lista, nie porada podatkowa. W razie wątpliwości zapytaj księgową lub doradcę.</p>';
    out.querySelector("h3").setAttribute("tabindex", "-1");
    out.querySelector("h3").focus();
  }
  form.addEventListener("submit", run);
  $("j-reset").addEventListener("click", function () { form.reset(); out.innerHTML = ""; });
})();
