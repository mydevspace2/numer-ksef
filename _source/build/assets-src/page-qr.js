/*! Kod QR KSeF: generator KOD I + dekoder linków */
(function () {
  "use strict";
  var K = window.KSEF, U = window.UI, $ = U.$, Q = window.QR;
  var state = { hash: "", nip: "", date: "", fileName: "" };
  function ksefLabel() {
    var v = $("g-ksef").value.trim();
    if (!v) return { label: "OFFLINE", ok: true };
    var r = K.checkKsef(v);
    return { label: r.valid ? r.input : "", ok: r.valid, err: r.errors[0] };
  }
  function gen() {
    var nip = K.cleanNip($("g-nip").value), date = $("g-date").value, env = $("g-env").value;
    var st = $("g-stat"), errs = [];
    if (!state.hash) errs.push("Wczytaj plik XML faktury – z niego liczony jest skrót SHA-256.");
    if (!K.nipValid(nip)) errs.push("Podaj poprawny NIP sprzedawcy.");
    if (!/^\d{4}-\d{2}-\d{2}$/.test(date)) errs.push("Podaj datę wystawienia faktury (pole P_1).");
    var lab = ksefLabel();
    if (!lab.ok) errs.push("Numer KSeF: " + lab.err);
    var box = $("g-out");
    if (errs.length) { box.hidden = true; if (state.hash || $("g-nip").value || $("g-ksef").value) U.statusBox(st, "bad", "Brakuje danych do KOD I", { errors: errs }); else U.statusBox(st, null); return; }
    var link = K.buildKod1(env, nip, date, state.hash);
    $("g-link").textContent = link; $("g-link").setAttribute("data-value", link);
    var svg = Q.toSvg(Q.encode(link, "M"), { label: "Kod QR KSeF: " + lab.label });
    $("g-qr").innerHTML = svg;
    $("g-label").textContent = lab.label;
    box.hidden = false;
    var w = [];
    if (env !== "PROD") w.push("Wybrano środowisko " + (env === "TE" ? "testowe" : "demo") + " – taki kod nie ma skutków podatkowych.");
    if (lab.label === "OFFLINE") w.push("Bez numeru KSeF pod kodem drukuje się napis OFFLINE (faktura offline). Dla faktury offline potrzebny jest też KOD II (CERTYFIKAT), którego to narzędzie nie generuje.");
    U.statusBox(st, w.length ? "warn" : "ok", "KOD I wygenerowany", { warnings: w });
    $("g-dl").onclick = function () { U.download("kod-qr-ksef.svg", svg.replace("<svg ", '<svg width="600" height="600" '), "image/svg+xml"); };
  }
  U.dropZone($("g-drop"), $("g-file"), function (files) {
    var f = files[0];
    U.readFile(f, false).then(function (buf) {
      state.fileName = f.name;
      return K.sha256Base64Url(buf).then(function (h) {
        state.hash = h;
        var text = new TextDecoder("utf-8").decode(buf), fa = K.parseFa(text);
        if (fa.ok) { if (fa.seller.nip) $("g-nip").value = fa.seller.nip; if (fa.issueDate) $("g-date").value = fa.issueDate; }
        var fromName = K.ksefFromFilename(f.name);
        if (fromName && fromName.valid && !$("g-ksef").value) $("g-ksef").value = fromName.input;
        $("g-hash").innerHTML = "Plik: <strong>" + K.esc(f.name) + "</strong> · SHA-256 (Base64URL): <span class=\"mono\">" + h + "</span>" + (fa.ok ? "" : '<br><span class="no">Plik nie wygląda na fakturę FA(3) – uzupełnij NIP i datę ręcznie.</span>');
        gen(); dec();
      });
    }).catch(function () { U.statusBox($("g-stat"), "bad", "Nie udało się odczytać pliku (przeglądarka bez WebCrypto?)"); });
  });
  ["g-nip", "g-date", "g-ksef", "g-env"].forEach(function (id) { $(id).addEventListener("input", gen); $(id).addEventListener("change", gen); });
  $("g-ex").addEventListener("click", function () {
    fetch("/assets/przyklad-fa3.xml").then(function (r) { return r.arrayBuffer(); }).then(function (buf) {
      var file = new File([buf], "przyklad-fa3.xml", { type: "application/xml" });
      var dt = new DataTransfer(); dt.items.add(file); $("g-file").files = dt.files;
      $("g-file").dispatchEvent(new Event("change"));
    }).catch(function () {});
  });

  // dekoder
  function dec() {
    var v = $("d-in").value.trim(), st = $("d-res");
    if (!v) { U.statusBox(st, null); return; }
    var r = K.parseQrLink(v), rows = [];
    if (r.env) rows.push(["Środowisko", K.esc(r.env + " (" + r.envLabel + ")")]);
    if (r.kind) rows.push(["Rodzaj kodu", r.kind]);
    if (r.nip) rows.push(["NIP sprzedawcy", '<span class="mono">' + K.formatNip(r.nip) + "</span>" + U.mark(r.nipOk)]);
    if (r.date) rows.push(["Data wystawienia", r.date]);
    if (r.ctxType) rows.push(["Kontekst", K.esc(r.ctxType + ": " + r.ctxValue)]);
    if (r.serial) rows.push(["Nr certyfikatu", '<span class="mono">' + K.esc(r.serial) + "</span>"]);
    if (r.hash) {
      var cmp = state.hash ? (state.hash === r.hash ? ' <span class="yes">✓ zgodny z wczytanym plikiem XML</span>' : ' <span class="no">✕ inny niż skrót wczytanego pliku XML – plik różni się od faktury z kodu</span>') : "";
      rows.push(["Skrót faktury (SHA-256)", '<span class="mono">' + K.esc(r.hash) + "</span>" + cmp]);
    }
    var head = r.phishing ? "Podejrzany link – to nie jest adres KSeF" : r.status === "ok" ? "Link ma poprawną budowę i prowadzi do domeny MF" : r.status === "warn" ? "Link poprawny, ale sprawdź uwagi" : "Link jest błędny";
    U.statusBox(st, r.status, head, { errors: r.errors, warnings: r.warnings, notes: r.notes, html: rows.length ? U.parts(rows) : "" });
    if (r.ok && !r.phishing) {
      st.insertAdjacentHTML("beforeend", '<p class="hint mt10">Ostateczne potwierdzenie: otwórz link – strona MF pokaże, czy faktura jest w KSeF. Adres musi zaczynać się dokładnie od <span class="mono">https://qr.ksef.mf.gov.pl/</span>.</p>');
    }
  }
  $("d-in").addEventListener("input", dec);
  function decShow() { dec(); U.reveal($("d-in"), $("d-res")); }
  $("d-check").addEventListener("click", decShow);
  U.onEnter($("d-in"), decShow);
  $("d-ex").addEventListener("click", function () { $("d-in").value = "https://qr-test.ksef.mf.gov.pl/invoice/1111111111/01-02-2026/UtQp9Gpc51y-u3xApZjIjgkpZ01js-J8KflSPW8WzIE"; dec(); });
  $("d-ex-bad").addEventListener("click", function () { $("d-in").value = "https://qr.ksef-mf-gov.pl.weryfikacja.example/invoice/1111111111/01-02-2026/UtQp9Gpc51y-u3xApZjIjgkpZ01js-J8KflSPW8WzIE"; dec(); });
  // skan obrazu / aparatu przez BarcodeDetector (jeśli przeglądarka wspiera)
  var hasBD = "BarcodeDetector" in window;
  var scanWrap = $("d-scan");
  if (hasBD && scanWrap) {
    scanWrap.hidden = false;
    var det;
    try { det = new window.BarcodeDetector({ formats: ["qr_code"] }); } catch (e) { scanWrap.hidden = true; }
    $("d-img").addEventListener("change", function () {
      var f = this.files[0]; if (!f || !det) return;
      createImageBitmap(f).then(function (bmp) { return det.detect(bmp); }).then(function (codes) {
        if (codes.length) { $("d-in").value = codes[0].rawValue; dec(); }
        else U.statusBox($("d-res"), "warn", "Nie znaleziono kodu QR na zdjęciu – spróbuj wyraźniejszego ujęcia.");
      }).catch(function () { U.statusBox($("d-res"), "warn", "Nie udało się odczytać obrazu."); });
    });
  }
})();
