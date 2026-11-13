/*! Strona główna: walidator numeru KSeF + generator tytułu przelewu */
(function () {
  "use strict";
  var K = window.KSEF, U = window.UI, $ = U.$;
  var inp = $("k-in"), res = $("k-res"), useBtn = $("k-use");
  var EXAMPLES = ["5265877635-20250826-0100001AF629-AF", "5265877635-20250709-0100E01D6840-3C", "9510001233-20261102-01A3F0C2B7D4-B8"];
  var last = null;
  function check() {
    var v = inp.value;
    if (!v.trim()) { U.statusBox(res, null); useBtn.hidden = true; inp.removeAttribute("aria-invalid"); return; }
    last = K.checkKsef(v);
    U.showCheck(res, last);
    inp.setAttribute("aria-invalid", last.status === "bad" ? "true" : "false");
    useBtn.hidden = !last.valid;
  }
  inp.addEventListener("input", check);
  function checkShow() { check(); U.reveal(inp, res); }
  $("k-check").addEventListener("click", checkShow);
  U.onEnter(inp, checkShow);
  $("k-ex").addEventListener("click", function () { inp.value = K.EXAMPLE_KSEF; check(); inp.focus(); });
  $("k-clear").addEventListener("click", function () { inp.value = ""; check(); inp.focus(); });
  useBtn.addEventListener("click", function () {
    if (!last || !last.valid) return;
    var slots = [$("t1"), $("t2"), $("t3")];
    var free = slots.filter(function (s) { return !s.value.trim(); })[0] || slots[0];
    free.value = last.input; title(); free.focus();
    $("tytul").scrollIntoView({ block: "start" });
  });

  // generator tytułu
  var tOut = $("t-out"), tCount = $("t-count"), tStat = $("t-stat"), tCopy = $("t-copy");
  function title() {
    var nums = [], errs = [];
    ["t1", "t2", "t3"].forEach(function (id, i) {
      var el = $(id), v = el.value.trim();
      if (!v) { el.removeAttribute("aria-invalid"); return; }
      var r = K.checkKsef(v);
      el.setAttribute("aria-invalid", r.valid ? "false" : "true");
      if (r.valid) nums.push(r.input);
      else errs.push("Numer " + (i + 1) + ": " + r.errors[0]);
    });
    var t = K.buildTitle(nums, $("t-extra").value);
    tOut.textContent = t.text || "Tu pojawi się tytuł przelewu.";
    tOut.classList.toggle("placeholder", !t.text);
    tOut.setAttribute("data-value", t.text);
    U.counter(tCount, t.length, K.TITLE_MAX);
    tCopy.disabled = !t.text;
    if (errs.length || t.warnings.length) U.statusBox(tStat, errs.length ? "bad" : "warn", errs.length ? "Popraw numery – błędne nie trafiają do tytułu" : "Uwaga", { errors: errs, warnings: t.warnings });
    else if (t.text) U.statusBox(tStat, "ok", "Tytuł gotowy do skopiowania (" + t.length + " " + K.plural(t.length) + ")");
    else U.statusBox(tStat, null);
  }
  ["t1", "t2", "t3", "t-extra"].forEach(function (id) { $(id).addEventListener("input", title); });
  $("t-ex").addEventListener("click", function () { $("t1").value = EXAMPLES[0]; $("t2").value = EXAMPLES[2]; $("t3").value = ""; $("t-extra").value = "FV 12/11/2026"; title(); });
  $("t-clear").addEventListener("click", function () { ["t1", "t2", "t3", "t-extra"].forEach(function (id) { $(id).value = ""; }); title(); });
  title();
})();
