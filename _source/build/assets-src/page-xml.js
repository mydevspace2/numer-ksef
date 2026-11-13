/*! Faktura XML (FA3) -> dane do przelewu */
(function () {
  "use strict";
  var K = window.KSEF, U = window.UI, $ = U.$;
  var cards = $("x-cards"), manual = $("x-ksef"), loaded = [];
  function row(label, value, copy, id) {
    var v = value == null || value === "" ? "–" : value;
    return "<div><dt>" + label + '</dt><dd class="' + (copy ? "mono" : "") + '">' + v + "</dd><dd>" +
      (copy ? '<button type="button" class="btn ghost small" data-copy-text="' + K.esc(copy) + '">Kopiuj</button>' : "") + "</dd></div>";
  }
  function render() {
    var manualK = manual.value.trim() ? K.checkKsef(manual.value) : null;
    var mk = $("x-ksef-msg");
    if (manualK) { mk.innerHTML = manualK.valid ? '<span class="yes">✓ poprawny ' + (manualK.kind === "iz" ? "identyfikator zbiorczy" : "numer KSeF") + "</span>" : '<span class="no">✕ ' + K.esc(manualK.errors[0]) + "</span>"; manual.setAttribute("aria-invalid", manualK.valid ? "false" : "true"); }
    else { mk.textContent = ""; manual.removeAttribute("aria-invalid"); }
    cards.innerHTML = loaded.map(function (L, idx) { return card(L, manualK, idx); }).join("");
  }
  function card(L, manualK, idx) {
    var f = L.fa;
    if (!f.ok) return '<div class="status bad"><p class="status-head"><span class="ico" aria-hidden="true">✕</span>' + K.esc(L.name) + "</p><ul class=\"reasons-bad\">" + f.errors.map(function (e) { return "<li>" + K.esc(e) + "</li>"; }).join("") + "</ul></div>";
    var ks = (manualK && manualK.valid && manualK.kind !== "iz") ? manualK : L.fromName;
    var ksefNum = ks && ks.valid ? ks.input : "";
    var ksefSrc = ks && ks.valid ? (ks === manualK ? "wpisany ręcznie" : "z nazwy pliku") : "";
    var cur = f.currency, amount = f.amountToPayCents;
    var amountTxt = amount != null ? K.formatAmountComma(amount) : "";
    var acc = f.payment.accounts.filter(function (a) { return !a.factor; })[0] || f.payment.accounts[0];
    var h = '<article class="tool" aria-labelledby="xc' + idx + '"><h2 id="xc' + idx + '">Dane do przelewu – faktura ' + K.esc(f.number || "") + "</h2>";
    h += '<p class="hint">Plik: ' + K.esc(L.name) + " · struktura " + K.esc(f.schema) + (f.kind ? " · rodzaj " + K.esc(f.kind) : "") + "</p>";
    if (f.warnings.length) h += '<div class="status warn"><ul class="reasons-warn">' + f.warnings.map(function (w) { return "<li>" + K.esc(w) + "</li>"; }).join("") + "</ul></div>";
    if (f.splitPayment) h += '<div class="status info"><p class="status-head"><span class="ico" aria-hidden="true">i</span>Mechanizm podzielonej płatności (P_18A = 1)</p><p>Zapłać przelewem MPP – gotowy komunikat poniżej.</p></div>';
    h += '<dl class="kv">';
    h += row("Odbiorca (sprzedawca)", K.esc(f.seller.name), f.seller.name);
    h += row("NIP sprzedawcy", K.esc(K.formatNip(f.seller.nip)) + U.mark(f.seller.nipOk), f.seller.nip);
    if (f.seller.address) h += row("Adres", K.esc(f.seller.address), f.seller.address);
    if (acc) {
      var nv = K.nrbValid(acc.nrb);
      h += row("Numer rachunku" + (acc.factor ? " (faktor)" : ""), K.esc(K.formatNrb(acc.nrb)) + (nv === null ? "" : U.mark(nv)) + (acc.bank ? "<br><small>" + K.esc(acc.bank) + "</small>" : ""), acc.nrb);
      if (f.payment.accounts.length > 1) h += row("Inne rachunki", f.payment.accounts.slice(1).map(function (a) { return K.esc(K.formatNrb(a.nrb)); }).join("<br>"), "");
    } else h += row("Numer rachunku", '<span class="no">brak w fakturze</span>', "");
    h += row("Kwota do zapłaty", K.esc(K.formatPln(amount, cur)) + (f.dueAmountCents != null ? " <small>(DoZaplaty)</small>" : " <small>(P_15)</small>"), amountTxt);
    if (f.vatCents) h += row("w tym VAT", K.esc(K.formatPln(f.vatCents, cur)) + (cur !== "PLN" && f.vatPlnCents != null ? " = " + K.esc(K.formatPln(f.vatPlnCents, "PLN")) : ""), K.formatAmountComma(f.vatPlnCents != null ? f.vatPlnCents : f.vatCents));
    h += row("Termin płatności", K.esc(f.payment.dueDates.map(U.isoToPl).join(", ") || "–"), "");
    h += row("Forma płatności", K.esc(f.payment.method || "–"), "");
    h += row("Numer faktury (P_2)", K.esc(f.number), f.number);
    h += row("Data wystawienia (P_1)", K.esc(U.isoToPl(f.issueDate)), "");
    h += row("Numer KSeF", ksefNum ? '<span class="mono">' + ksefNum + "</span> <small>(" + ksefSrc + ")</small>" : '<span class="maybe">nie ma go w pliku XML – wpisz go powyżej (znajdziesz go w UPO lub w KSeF)</span>', ksefNum);
    if (f.payment.ipksef) h += row("IPKSeF (identyfikator płatności)", K.esc(f.payment.ipksef), f.payment.ipksef);
    h += "</dl>";
    // tytuł
    var tParts = ksefNum ? [ksefNum] : [];
    var t = K.buildTitle(tParts, ksefNum ? (f.number ? "FV " + f.number : "") : (f.number ? "Faktura " + f.number : ""));
    if (t.length > 140) t = K.buildTitle(tParts, "");
    h += '<h3>Tytuł zwykłego przelewu</h3><p class="out" id="xt' + idx + '" data-value="' + K.esc(t.text) + '">' + K.esc(t.text) + '</p><div class="out-row"><span>' + t.length + " / 140 " + K.plural(t.length) + '</span><button type="button" class="btn small" data-copy="xt' + idx + '">Kopiuj tytuł</button></div>';
    if (!ksefNum) h += '<p class="note">Od 1 stycznia 2027 r. płacąc czynnemu podatnikowi VAT podajesz numer KSeF. Wpisz go w polu powyżej, a tytuł uzupełni się sam.</p>';
    // MPP
    var vatForMpp = f.vatPlnCents != null ? K.formatAmountComma(f.vatPlnCents) : "";
    var m = K.buildMpp({ vat: vatForMpp, gross: cur === "PLN" ? amountTxt : "", nip: f.seller.nip, inv: ksefNum || f.number, txt: ksefNum && f.number ? ("FV " + f.number).slice(0, 33) : "" });
    var mppTitle = f.splitPayment ? "Komunikat przelewu MPP (split payment)" : "Komunikat MPP (gdybyś płacił w MPP dobrowolnie)";
    h += "<h3>" + mppTitle + "</h3>";
    if (m.text) {
      h += '<p class="out" id="xm' + idx + '" data-value="' + K.esc(m.text) + '">' + K.esc(m.text) + '</p><div class="out-row"><span>' + m.length + ' / 140 znaków</span><button type="button" class="btn small" data-copy="xm' + idx + '">Kopiuj komunikat</button>';
      var qs = "?vat=" + encodeURIComponent(vatForMpp) + "&gross=" + encodeURIComponent(cur === "PLN" ? amountTxt : "") + "&nip=" + encodeURIComponent(f.seller.nip) + "&inv=" + encodeURIComponent(ksefNum || f.number) + "&txt=" + encodeURIComponent(ksefNum && f.number ? ("FV " + f.number).slice(0, 33) : "");
      h += '<a class="btn ghost small" href="/przelew-mpp-numer-ksef/' + qs + '">Edytuj w generatorze MPP</a></div>';
      if (m.errors.length || m.warnings.length) h += '<div class="status ' + (m.errors.length ? "bad" : "warn") + '"><ul class="' + (m.errors.length ? "reasons-bad" : "reasons-warn") + '">' + m.errors.concat(m.warnings).map(function (e) { return "<li>" + K.esc(e) + "</li>"; }).join("") + "</ul></div>";
    } else h += '<p class="hint">Brak danych do komunikatu MPP (np. faktura bez VAT lub bez NIP sprzedawcy).</p>';
    if (cur !== "PLN") h += '<p class="note">Faktura w walucie ' + K.esc(cur) + ". W MPP kwotę VAT podaje się w złotych (pola P_14_xW).</p>";
    return h + "</article>";
  }
  function handle(files) {
    loaded = [];
    var arr = Array.prototype.slice.call(files).filter(function (f) { return /\.xml$/i.test(f.name) || /xml/.test(f.type); });
    if (!arr.length) { cards.innerHTML = '<div class="status bad"><p class="status-head"><span class="ico" aria-hidden="true">✕</span>Wybierz plik .xml faktury z KSeF.</p></div>'; return; }
    Promise.all(arr.map(function (f) { return U.readFile(f, true).then(function (t) { return { name: f.name, text: t }; }); })).then(function (list) {
      list.forEach(function (it) { loaded.push({ name: it.name, fa: K.parseFa(it.text), fromName: K.ksefFromFilename(it.name) }); });
      render();
      cards.querySelector("h2, .status") && cards.scrollIntoView({ block: "start" });
    });
  }
  U.dropZone($("x-drop"), $("x-file"), handle);
  manual.addEventListener("input", render);
  $("x-ex").addEventListener("click", function () {
    fetch("/assets/przyklad-fa3.xml").then(function (r) { return r.text(); }).then(function (t) {
      loaded = [{ name: "5265877635-20250826-0100001AF629-AF.xml", fa: K.parseFa(t), fromName: K.ksefFromFilename("5265877635-20250826-0100001AF629-AF.xml") }];
      render();
    }).catch(function () { cards.innerHTML = '<div class="status bad"><p>Nie udało się wczytać przykładu.</p></div>'; });
  });
})();
