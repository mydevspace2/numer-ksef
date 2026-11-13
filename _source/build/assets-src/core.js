/*! NumerKSeF – wspólna logika (KSeF CRC-8, NIP, IZ, MPP, FA(3), KOD I). Działa w 100% w przeglądarce. */
(function (root, factory) {
  var api = factory();
  if (typeof module === "object" && module.exports) module.exports = api;
  else root.KSEF = api;
})(typeof self !== "undefined" ? self : this, function () {
  "use strict";

  var EXAMPLE_KSEF = "5265877635-20250826-0100001AF629-AF";
  var EXAMPLE_IZ = "1111111111-IZ202607-65ED02180000-E7";
  var EXAMPLE_NIP = "5265877635";
  var KSEF2_START = "20260201";
  var FA3_NS = "http://crd.gov.pl/wzor/2025/06/25/13775/";
  var FA2_NS = "http://crd.gov.pl/wzor/2023/06/29/12648/";
  var QR_HOSTS = {
    "qr.ksef.mf.gov.pl": { env: "PROD", label: "produkcyjne", tax: true },
    "qr-test.ksef.mf.gov.pl": { env: "TE", label: "testowe", tax: false },
    "qr-demo.ksef.mf.gov.pl": { env: "DEMO", label: "demo", tax: false }
  };

  /* ---------- helpers ---------- */
  function plural(n, one, few, many) {
    one = one || "znak"; few = few || "znaki"; many = many || "znaków";
    if (n === 1) return one;
    var d = n % 10, h = n % 100;
    return d >= 2 && d <= 4 && (h < 12 || h > 14) ? few : many;
  }
  function esc(t) {
    return String(t == null ? "" : t).replace(/[&<>"']/g, function (c) {
      return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c];
    });
  }
  function pad2(n) { return (n < 10 ? "0" : "") + n; }
  function todayYmd(today) {
    var t = today || new Date();
    return "" + t.getFullYear() + pad2(t.getMonth() + 1) + pad2(t.getDate());
  }

  /* ---------- CRC-8 (polinom 0x07, start 0x00) ---------- */
  function crc8(str) {
    var c = 0;
    for (var k = 0; k < str.length; k++) {
      c ^= str.charCodeAt(k) & 0xff;
      for (var i = 0; i < 8; i++) c = c & 0x80 ? ((c << 1) ^ 0x07) & 0xff : (c << 1) & 0xff;
    }
    return (c < 16 ? "0" : "") + c.toString(16).toUpperCase();
  }

  /* ---------- NIP ---------- */
  function cleanNip(raw) {
    return String(raw || "").replace(/^\s*PL/i, "").replace(/[\s\-\u2010-\u2015]/g, "");
  }
  function nipValid(nip) {
    if (!/^\d{10}$/.test(nip)) return false;
    var w = [6, 5, 7, 2, 3, 4, 5, 6, 7], s = 0;
    for (var i = 0; i < 9; i++) s += w[i] * +nip[i];
    var r = s % 11;
    return r !== 10 && r === +nip[9];
  }
  function checkNip(raw) {
    var n = cleanNip(raw);
    var res = { input: n, valid: false, errors: [] };
    if (!n) { res.errors.push("Wpisz NIP."); return res; }
    if (!/^\d+$/.test(n)) { res.errors.push("NIP może zawierać tylko cyfry."); return res; }
    if (n.length !== 10) { res.errors.push("NIP ma 10 cyfr, a wpisano " + n.length + "."); return res; }
    if (!nipValid(n)) { res.errors.push("Cyfra kontrolna NIP się nie zgadza – sprawdź, czy nie ma literówki."); return res; }
    res.valid = true;
    return res;
  }
  function formatNip(n) { return n.length === 10 ? n.slice(0, 3) + "-" + n.slice(3, 6) + "-" + n.slice(6, 8) + "-" + n.slice(8) : n; }

  /* ---------- normalizacja ---------- */
  function normalize(raw) {
    var s = String(raw == null ? "" : raw);
    var fixes = [];
    var t = s.trim();
    if (/[\u2010-\u2015\u2212]/.test(t)) { t = t.replace(/[\u2010-\u2015\u2212]/g, "-"); fixes.push("zamieniono długie myślniki na „-”"); }
    if (/\s/.test(t)) { t = t.replace(/\s+/g, ""); fixes.push("usunięto spacje"); }
    if (t !== t.toUpperCase()) { t = t.toUpperCase(); fixes.push("zamieniono małe litery na wielkie"); }
    return { value: t, fixes: fixes };
  }

  // wskazówki dla znaków spoza dozwolonego zbioru
  function charHints(s, template) {
    var hints = [];
    for (var i = 0; i < s.length && i < template.length && hints.length < 4; i++) {
      var ch = s[i], t = template[i], ok;
      if (t === "?") ok = /[0-9A-Z]/.test(ch);
      else if (t === "d") ok = /[0-9]/.test(ch);
      else if (t === "h") ok = /[0-9A-F]/.test(ch);
      else ok = ch === t;
      if (!ok) {
        var tip = "";
        if ((t === "d" || t === "h") && ch === "O") tip = " – „O” zamiast zera?";
        else if ((t === "d" || t === "h") && (ch === "I" || ch === "L")) tip = " – „" + ch + "” zamiast jedynki?";
        else if ((t === "d" || t === "h") && ch === "S") tip = " – „S” zamiast piątki?";
        else if (t === "-") tip = " – tu powinien być myślnik";
        else if (t === "d") tip = " – tu powinna być cyfra";
        else if (t === "h") tip = " – dozwolone są tylko 0–9 i A–F";
        else tip = " – oczekiwano „" + t + "”";
        hints.push("znak " + (i + 1) + ": „" + ch + "”" + tip);
      }
    }
    return hints;
  }
  var TPL_KSEF = "dddddddddd-dddddddd-hhhhhhhhhhhh-hh";
  var TPL_IZ = "dddddddddd-IZdddddd-hhhhhhhhhhhh-hh";

  function realDate(y, m, d) {
    var dt = new Date(Date.UTC(y, m - 1, d));
    return dt.getUTCFullYear() === y && dt.getUTCMonth() === m - 1 && dt.getUTCDate() === d;
  }

  /* ---------- numer KSeF ---------- */
  var KSEF_RE = /^(\d{10}|M\d{9}|[A-Z]{3}\d{7})-(\d{4})(\d{2})(\d{2})-([0-9A-F]{12})-([0-9A-F]{2})$/;
  var KSEF1_RE = /^(\d{10}|M\d{9}|[A-Z]{3}\d{7})-(\d{4})(\d{2})(\d{2})-([0-9A-F]{6})-([0-9A-F]{6})-([0-9A-F]{2})$/;
  var IZ_RE = /^(\d{10})-IZ(\d{4})(\d{2})-([0-9A-F]{12})-([0-9A-F]{2})$/;

  function result(input, fixes) {
    return { input: input, kind: "unknown", status: "bad", valid: false, errors: [], warnings: [], notes: [], fixes: fixes || [], parts: null };
  }
  function finish(r) {
    r.status = r.errors.length ? "bad" : r.warnings.length ? "warn" : "ok";
    r.valid = r.status !== "bad";
    return r;
  }

  function checkKsef(raw, today) {
    var n = normalize(raw), s = n.value;
    if (/^\d{10}-IZ/.test(s) || /-IZ\d/.test(s)) return checkIZ(raw, today);
    var r = result(s, n.fixes);
    r.kind = "ksef";
    if (!s) { r.errors.push("Wpisz numer KSeF."); return finish(r); }
    var t = todayYmd(today);
    var m1 = s.length === 36 && KSEF1_RE.exec(s);
    if (m1) {
      r.kind = "ksef1";
      r.parts = { prefix: m1[1], date: m1[2] + m1[3] + m1[4], tech: m1[5] + m1[6], given: m1[7] };
      r.warnings.push("36 znaków z dodatkowym myślnikiem – to stary format numeru z KSeF 1.0. Schemat FA(3) wciąż go akceptuje, ale nowe numery (KSeF 2.0) mają 35 znaków. Sumy kontrolnej tego formatu nie weryfikujemy.");
      prefixCheck(r, m1[1]);
      dateCheck(r, +m1[2], +m1[3], +m1[4], t);
      return finish(r);
    }
    if (s.length !== 35) {
      r.errors.push("Zła długość: " + s.length + " " + plural(s.length) + " zamiast 35.");
      if (s.length > 35 && s.length < 40) r.errors.push("Sprawdź, czy nie skopiowano dodatkowych znaków (np. kropki lub przecinka na końcu).");
      return finish(r);
    }
    var m = KSEF_RE.exec(s);
    if (!m) {
      var hints = charHints(s, /^(M\d{9}|[A-Z]{3}\d{7})-/.test(s) ? "??????????" + TPL_KSEF.slice(10) : TPL_KSEF);
      r.errors.push("Zły format. Wzór: 9999999999-RRRRMMDD-FFFFFFFFFFFF-FF.");
      hints.forEach(function (h) { r.errors.push(h); });
      return finish(r);
    }
    var data = s.slice(0, 32), given = s.slice(33), calc = crc8(data);
    r.parts = { prefix: m[1], date: m[2] + m[3] + m[4], tech: m[5], given: given, calc: calc, crcOk: given === calc };
    prefixCheck(r, m[1]);
    dateCheck(r, +m[2], +m[3], +m[4], t);
    if (!r.parts.crcOk) r.errors.push("Suma kontrolna się nie zgadza: jest " + given + ", powinno być " + calc + ". Najczęściej to literówka – skopiuj numer ponownie z UPO lub programu.");
    return finish(r);
  }

  function prefixCheck(r, prefix) {
    r.parts.nip = /^\d{10}$/.test(prefix) ? prefix : null;
    if (r.parts.nip) {
      r.parts.nipOk = nipValid(prefix);
      if (!r.parts.nipOk) r.errors.push("Pierwsze 10 cyfr to nie jest poprawny NIP (zła cyfra kontrolna).");
    } else {
      r.parts.nipOk = null;
      r.warnings.push("Początek „" + prefix + "” to nie NIP, tylko inny identyfikator dopuszczony przez schemat FA(3) (np. identyfikator wewnętrzny). Sprawdź go u wystawcy.");
    }
  }
  function dateCheck(r, y, mo, d, t) {
    var ymd = "" + y + pad2(mo) + pad2(d);
    r.parts.dateOk = false;
    if (!realDate(y, mo, d)) { r.errors.push("Data " + pad2(d) + "." + pad2(mo) + "." + y + " nie istnieje w kalendarzu."); return; }
    if (y < 2020) { r.errors.push("Data " + pad2(d) + "." + pad2(mo) + "." + y + " jest wcześniejsza niż start KSeF."); return; }
    if (ymd > t) { r.errors.push("Data przyjęcia do KSeF (" + pad2(d) + "." + pad2(mo) + "." + y + ") jest w przyszłości."); return; }
    r.parts.dateOk = true;
    if (ymd < "20220101") r.warnings.push("Data sprzed 2022 r. – to nietypowe dla numeru KSeF.");
    else if (ymd < KSEF2_START) r.notes.push("Data sprzed 1 lutego 2026 r. – to numer z KSeF 1.0 (okres dobrowolny) albo przykładowy/testowy.");
  }

  /* ---------- identyfikator zbiorczy ---------- */
  function checkIZ(raw, today) {
    var n = normalize(raw), s = n.value;
    var r = result(s, n.fixes);
    r.kind = "iz";
    if (!s) { r.errors.push("Wpisz identyfikator zbiorczy."); return finish(r); }
    if (s.length !== 35) {
      r.errors.push("Zła długość: " + s.length + " " + plural(s.length) + " zamiast 35.");
      return finish(r);
    }
    var m = IZ_RE.exec(s);
    if (!m) {
      r.errors.push("Zły format. Wzór: 9999999999-IZRRRRMM-FFFFFFFFFFFF-FF.");
      charHints(s, TPL_IZ).forEach(function (h) { r.errors.push(h); });
      return finish(r);
    }
    var y = +m[2], mo = +m[3], given = m[5], calc = crc8(s.slice(0, 32));
    r.parts = { nip: m[1], nipOk: nipValid(m[1]), year: y, month: mo, tech: m[4], given: given, calc: calc, crcOk: given === calc, dateOk: false };
    if (!r.parts.nipOk) r.errors.push("Pierwsze 10 cyfr to nie jest poprawny NIP (zła cyfra kontrolna).");
    var ym = "" + y + pad2(mo), tym = todayYmd(today).slice(0, 6);
    if (mo < 1 || mo > 12) r.errors.push("Miesiąc „" + pad2(mo) + "” nie istnieje.");
    else if (y < 2026) r.errors.push("Rok " + y + " jest wcześniejszy niż KSeF 2.0 – identyfikatory zbiorcze generuje się od 2026 r.");
    else if (ym > tym) r.errors.push("Miesiąc wygenerowania (" + pad2(mo) + "." + y + ") jest w przyszłości.");
    else r.parts.dateOk = true;
    if (!r.parts.crcOk) r.errors.push("Suma kontrolna się nie zgadza: jest " + given + ", powinno być " + calc + ". To prawdopodobnie literówka.");
    if (!r.errors.length) r.notes.push("Format i suma kontrolna są poprawne. Jakie faktury obejmuje ten identyfikator, wie tylko KSeF – sprawdzisz to w Aplikacji Podatnika KSeF lub w programie połączonym z KSeF.");
    return finish(r);
  }

  /* ---------- wyszukiwanie w dowolnym tekście ---------- */
  var FIND_LOOSE = /[0-9A-Z]{10}[-\u2010-\u2015\u2212](?:[0-9A-Z]{8}|IZ[0-9A-Z]{6})[-\u2010-\u2015\u2212][0-9A-Z]{6}[-\u2010-\u2015\u2212]?[0-9A-Z]{6}[-\u2010-\u2015\u2212][0-9A-Z]{2}/gi;
  function findCandidates(text) {
    var out = [], m, re = new RegExp(FIND_LOOSE.source, "gi");
    var s = String(text || "");
    while ((m = re.exec(s))) {
      var before = m.index > 0 ? s[m.index - 1] : "", after = s[m.index + m[0].length] || "";
      if (/[0-9A-Za-z]/.test(before) || /[0-9A-Za-z]/.test(after)) continue;
      out.push(m[0]);
    }
    return out;
  }

  /* ---------- tytuł przelewu (zwykły) ---------- */
  var TITLE_MAX = 140, TITLE_MAX_NUMBERS = 3;
  function buildTitle(nums, extra) {
    var list = (nums || []).filter(Boolean);
    var t = list.join(", ");
    var e = String(extra || "").trim();
    if (e) t = t ? t + " " + e : e;
    var warnings = [];
    if (list.length > TITLE_MAX_NUMBERS) warnings.push("Więcej niż " + TITLE_MAX_NUMBERS + " numery nie zmieszczą się w typowym polu tytułu – użyj identyfikatora zbiorczego.");
    if (t.length > TITLE_MAX) warnings.push("Tytuł ma " + t.length + " " + plural(t.length) + " – większość banków przyjmuje maks. 140. Skróć opis albo użyj identyfikatora zbiorczego.");
    return { text: t, length: t.length, ok: t.length > 0 && t.length <= TITLE_MAX && list.length <= TITLE_MAX_NUMBERS, warnings: warnings };
  }

  /* ---------- kwoty ---------- */
  function parseAmount(raw) {
    var s = String(raw == null ? "" : raw).replace(/[\s\u00a0\u202f]/g, "").replace(/zł$|PLN$/i, "");
    if (!s) return { ok: false, empty: true, error: "" };
    if (/^\d{1,3}(\.\d{3})+,\d{1,2}$/.test(s)) s = s.replace(/\./g, "");
    if (/^\d{1,3}(,\d{3})+\.\d{1,2}$/.test(s)) s = s.replace(/,/g, "");
    var m = /^(\d{1,10})(?:[.,](\d{1,2}))?$/.exec(s);
    if (!m) return { ok: false, error: "Nieprawidłowa kwota – wpisz np. 1230,00." };
    var cents = +m[1] * 100 + (m[2] ? +(m[2] + (m[2].length === 1 ? "0" : "")) : 0);
    return { ok: true, cents: cents, text: formatAmountComma(cents) };
  }
  function formatAmountComma(cents) {
    var zl = Math.floor(cents / 100), gr = cents % 100;
    return zl + "," + pad2(gr);
  }
  function decimalToCents(str) {
    if (str == null || str === "") return null;
    var s = String(str).trim();
    var m = /^(-?)(\d+)(?:\.(\d+))?$/.exec(s);
    if (!m) return null;
    var frac = (m[3] || "") + "00";
    var cents = +m[2] * 100 + +frac.slice(0, 2) + (+frac[2] >= 5 ? 1 : 0);
    return m[1] ? -cents : cents;
  }
  function formatPln(cents, currency) {
    if (cents == null) return "–";
    var v = cents / 100;
    try { return new Intl.NumberFormat("pl-PL", { style: "currency", currency: currency || "PLN" }).format(v); }
    catch (e) { return v.toFixed(2).replace(".", ",") + " " + (currency || "PLN"); }
  }

  /* ---------- komunikat MPP ---------- */
  var MPP_MAX = 140, MPP_TXT_MAX = 33, MPP_INV_MAX = 35, MPP_IDC_MAX = 14;
  var MPP_FORBIDDEN = /[:*;'"!+?|#\u2018\u2019\u201a\u201c\u201d\u201e`]/g;
  var MPP_ALLOWED_CHAR = /[0-9A-Za-z&%()\-{}\/,. ąćęłńóśźżĄĆĘŁŃÓŚŹŻ]/;
  function badChars(s) {
    var bad = {};
    for (var i = 0; i < s.length; i++) if (!MPP_ALLOWED_CHAR.test(s[i])) bad[s[i]] = 1;
    return Object.keys(bad);
  }
  function buildMpp(o, today) {
    o = o || {};
    var res = { ok: false, errors: [], warnings: [], fieldErrors: {}, fieldInfo: {}, text: "", lines4: [], lines35: [], length: 0 };
    function fe(f, msg) { (res.fieldErrors[f] = res.fieldErrors[f] || []).push(msg); res.errors.push(msg); }
    function fw(f, msg) { (res.fieldInfo[f] = res.fieldInfo[f] || []).push(msg); res.warnings.push(msg); }

    var own = !!o.own;
    // VAT
    var vat = parseAmount(o.vat);
    if (vat.empty) fe("vat", "Podaj kwotę VAT.");
    else if (!vat.ok) fe("vat", vat.error);
    else if (vat.cents <= 0) fe("vat", "Kwota VAT musi być większa od 0,00.");
    else if (vat.cents > 999999999999) fe("vat", "Kwota VAT może mieć maks. 10 cyfr przed przecinkiem.");
    // brutto
    var gross = parseAmount(o.gross);
    if (!gross.empty) {
      if (!gross.ok) fe("gross", gross.error);
      else if (vat.ok && vat.cents > gross.cents) fe("vat", "Kwota VAT nie może być wyższa niż kwota przelewu (brutto).");
      else if (own && vat.ok && gross.cents !== vat.cents) fw("gross", "Przy przekazaniu własnym kwota przelewu powinna być równa kwocie VAT.");
    }
    // IDC
    var idc = cleanNip(o.nip);
    if (!idc) fe("nip", own ? "Podaj swój NIP (przy przekazaniu własnym wpisujesz własny identyfikator)." : "Podaj NIP sprzedawcy (wystawcy faktury).");
    else if (/^\d{10}$/.test(idc)) { if (!nipValid(idc)) fe("nip", "Cyfra kontrolna NIP się nie zgadza."); }
    else if (/^[0-9A-Za-z]{1,14}$/.test(idc)) fw("nip", "To nie jest 10-cyfrowy NIP. Pole /IDC/ przyjmuje do 14 znaków – upewnij się, że to właściwy identyfikator dostawcy.");
    else fe("nip", "Identyfikator dostawcy: tylko cyfry i litery, maks. 14 znaków.");
    // INV
    var inv = "", invKind = "";
    if (own) { inv = "PRZEKAZANIE WLASNE"; invKind = "own"; }
    else {
      var invRaw = String(o.inv || "").trim();
      var nk = normalize(invRaw).value;
      if (!invRaw) fe("inv", "Podaj numer KSeF, identyfikator zbiorczy albo numer faktury.");
      else if (/^\d{10}-IZ/.test(nk)) {
        var iz = checkIZ(nk, today);
        if (!iz.valid) fe("inv", "Identyfikator zbiorczy jest błędny: " + iz.errors[0]);
        inv = nk; invKind = "iz";
      } else if (/^[0-9A-Z]{10}-\d{8}-/.test(nk) && (nk.length === 35 || nk.length === 36)) {
        var k = checkKsef(nk, today);
        if (!k.valid) fe("inv", "Numer KSeF jest błędny: " + k.errors[0]);
        else if (k.kind === "ksef1") fe("inv", "Numer w starym formacie (36 znaków) nie zmieści się w polu /INV/ (35 znaków).");
        inv = nk; invKind = "ksef";
      } else {
        inv = invRaw; invKind = "invoice";
        if (inv.length > MPP_INV_MAX) fe("inv", "Numer faktury może mieć maks. 35 znaków (ma " + inv.length + ").");
        var dt = String(o.date || "");
        if (!dt || dt >= "2027-01-01") fw("inv", "Od 1 stycznia 2027 r. za fakturę wystawioną w KSeF w polu /INV/ podajesz numer KSeF (albo identyfikator zbiorczy), a nie własny numer faktury.");
      }
      var bi = badChars(inv);
      if (bi.length) fe("inv", "Niedozwolone znaki w /INV/: " + bi.join(" "));
    }
    // TXT
    var txt = String(o.txt || "").trim();
    if (txt) {
      if (txt.length > MPP_TXT_MAX) fe("txt", "Tekst w /TXT/ może mieć maks. 33 znaki (ma " + txt.length + ").");
      var bt = badChars(txt);
      if (bt.length) fe("txt", "Niedozwolone znaki w /TXT/: " + bt.join(" ") + " (zabronione m.in. : * ; ‘ “ ! + ? | #).");
      if (/\/(VAT|IDC|INV|TXT)\//i.test("/" + txt + "/")) fe("txt", "Tekst nie może zawierać słów kodowych /VAT/, /IDC/, /INV/, /TXT/.");
    }
    res.invKind = invKind;
    var vatText = vat.ok ? vat.text : "";
    res.parts = { vat: vatText, idc: idc, inv: inv, txt: txt };
    if (vatText && idc && inv) {
      res.lines4 = ["/VAT/" + vatText, "/IDC/" + idc, "/INV/" + inv];
      if (txt) res.lines4.push("/TXT/" + txt);
      res.text = res.lines4.join("");
      res.length = res.text.length;
      for (var i = 0; i < res.text.length; i += 35) res.lines35.push(res.text.slice(i, i + 35));
      if (res.length > MPP_MAX) fe("txt", "Cały komunikat ma " + res.length + " znaków – limit to 140. Skróć /TXT/.");
    }
    res.ok = !res.errors.length && !!res.text;
    return res;
  }

  /* ---------- FA(3) XML ---------- */
  function parseFa(xmlText, DOMParserImpl) {
    var P = DOMParserImpl || (typeof DOMParser !== "undefined" ? DOMParser : null);
    var out = { ok: false, errors: [], warnings: [] };
    if (!P) { out.errors.push("Brak parsera XML."); return out; }
    var doc;
    try { doc = new P().parseFromString(String(xmlText).replace(/^\uFEFF/, ""), "application/xml"); }
    catch (e) { out.errors.push("Plik nie jest poprawnym XML."); return out; }
    var perr = doc.getElementsByTagName("parsererror");
    var rootEl = doc.documentElement;
    if (perr.length || !rootEl || (rootEl.localName || rootEl.nodeName) === "parsererror") { out.errors.push("Plik nie jest poprawnym XML (błąd składni)."); return out; }
    var ln = rootEl.localName || String(rootEl.nodeName).replace(/^.*:/, "");
    if (ln !== "Faktura") { out.errors.push("To nie jest e-faktura (brak elementu „Faktura”). Może to UPO albo inny dokument?"); return out; }
    var ns = rootEl.namespaceURI || "";
    out.namespace = ns;
    out.schema = ns === FA3_NS ? "FA(3)" : ns === FA2_NS ? "FA(2)" : "nieznana";
    if (out.schema === "FA(2)") out.warnings.push("To faktura w starszej strukturze FA(2). Odczytujemy dane, ale od 1 lutego 2026 r. obowiązuje FA(3).");
    else if (out.schema === "nieznana") out.warnings.push("Nieznana przestrzeń nazw – dane odczytane po nazwach elementów, sprawdź je ręcznie.");

    function kids(el, name) {
      var r = [];
      if (!el) return r;
      var all = el.getElementsByTagNameNS ? el.getElementsByTagNameNS(ns || "*", name) : [];
      for (var i = 0; i < all.length; i++) r.push(all[i]);
      if (!r.length) {
        var any = el.getElementsByTagName("*");
        for (var j = 0; j < any.length; j++) {
          var l = any[j].localName || String(any[j].nodeName).replace(/^.*:/, "");
          if (l === name) r.push(any[j]);
        }
      }
      return r;
    }
    function one(el, path) {
      var parts = path.split("/"), cur = el;
      for (var i = 0; i < parts.length; i++) { var k = kids(cur, parts[i]); if (!k.length) return null; cur = k[0]; }
      return cur;
    }
    function txt(el, path) { var n = path ? one(el, path) : el; return n ? String(n.textContent).trim() : ""; }

    var p1 = one(rootEl, "Podmiot1"), p2 = one(rootEl, "Podmiot2"), fa = one(rootEl, "Fa");
    if (!fa) { out.errors.push("Brak sekcji „Fa” z danymi faktury."); return out; }
    out.seller = {
      nip: txt(p1, "DaneIdentyfikacyjne/NIP"),
      name: txt(p1, "DaneIdentyfikacyjne/Nazwa"),
      address: [txt(p1, "Adres/AdresL1"), txt(p1, "Adres/AdresL2")].filter(Boolean).join(", "),
      country: txt(p1, "Adres/KodKraju")
    };
    out.seller.nipOk = nipValid(out.seller.nip);
    out.buyer = {
      nip: txt(p2, "DaneIdentyfikacyjne/NIP"),
      name: txt(p2, "DaneIdentyfikacyjne/Nazwa"),
      euVat: (txt(p2, "DaneIdentyfikacyjne/KodUE") + txt(p2, "DaneIdentyfikacyjne/NrVatUE")) || ""
    };
    out.buyer.nipOk = out.buyer.nip ? nipValid(out.buyer.nip) : null;
    out.currency = txt(fa, "KodWaluty") || "PLN";
    out.issueDate = txt(fa, "P_1");
    out.number = txt(fa, "P_2");
    out.kind = txt(fa, "RodzajFaktury");
    out.grossCents = decimalToCents(txt(fa, "P_15"));
    var vat = 0, vatPln = 0, anyVat = false, anyW = false;
    ["1", "2", "3", "4", "5"].forEach(function (k) {
      var directs = fa.childNodes, v = null, w = null;
      for (var i = 0; i < directs.length; i++) {
        var l = directs[i].localName || String(directs[i].nodeName || "").replace(/^.*:/, "");
        if (l === "P_14_" + k) v = decimalToCents(directs[i].textContent);
        if (l === "P_14_" + k + "W") w = decimalToCents(directs[i].textContent);
      }
      if (v != null) { vat += v; anyVat = true; }
      if (w != null) { vatPln += w; anyW = true; }
      else if (v != null) vatPln += v;
    });
    out.vatCents = anyVat ? vat : 0;
    out.vatPlnCents = anyW ? vatPln : (out.currency === "PLN" ? out.vatCents : null);
    out.splitPayment = txt(fa, "Adnotacje/P_18A") === "1";
    var roz = one(fa, "Rozliczenie");
    out.dueAmountCents = roz ? decimalToCents(txt(roz, "DoZaplaty")) : null;
    var pl = one(fa, "Platnosc");
    out.payment = { paid: false, dueDates: [], method: "", accounts: [], ipksef: "", link: "" };
    if (pl) {
      out.payment.paid = txt(pl, "Zaplacono") === "1";
      out.payment.paidDate = txt(pl, "DataZaplaty");
      kids(pl, "TerminPlatnosci").forEach(function (t) {
        var d = txt(t, "Termin");
        if (d) out.payment.dueDates.push(d);
        else {
          var il = txt(t, "TerminOpis/Ilosc"), j = txt(t, "TerminOpis/Jednostka"), z = txt(t, "TerminOpis/ZdarzeniePoczatkowe");
          if (il) out.payment.dueDates.push(il + " " + j + " od: " + z);
        }
      });
      var fp = "";
      for (var c = 0; c < pl.childNodes.length; c++) {
        var cl = pl.childNodes[c].localName || String(pl.childNodes[c].nodeName || "").replace(/^.*:/, "");
        if (cl === "FormaPlatnosci") fp = String(pl.childNodes[c].textContent).trim();
      }
      out.payment.methodCode = fp;
      out.payment.method = { "1": "Gotówka", "2": "Karta", "3": "Bon", "4": "Czek", "5": "Kredyt", "6": "Przelew", "7": "Mobilna" }[fp] || (txt(pl, "OpisPlatnosci") || "");
      kids(pl, "RachunekBankowy").forEach(function (rb) {
        var parent = rb.parentNode && (rb.parentNode.localName || String(rb.parentNode.nodeName).replace(/^.*:/, ""));
        if (parent !== "Platnosc") return;
        out.payment.accounts.push({ nrb: txt(rb, "NrRB").replace(/\s+/g, ""), swift: txt(rb, "SWIFT"), bank: txt(rb, "NazwaBanku"), desc: txt(rb, "OpisRachunku") });
      });
      kids(pl, "RachunekBankowyFaktora").forEach(function (rb) {
        out.payment.accounts.push({ nrb: txt(rb, "NrRB").replace(/\s+/g, ""), swift: txt(rb, "SWIFT"), bank: txt(rb, "NazwaBanku"), desc: "Rachunek faktora", factor: true });
      });
      out.payment.ipksef = txt(pl, "IPKSeF");
      out.payment.link = txt(pl, "LinkDoPlatnosci");
    }
    out.amountToPayCents = out.dueAmountCents != null ? out.dueAmountCents : out.grossCents;
    out.correctedKsef = txt(fa, "DaneFaKorygowanej/NrKSeFFaKorygowanej");
    if (!out.seller.nip) out.warnings.push("Brak NIP sprzedawcy.");
    else if (!out.seller.nipOk) out.warnings.push("NIP sprzedawcy ma złą cyfrę kontrolną.");
    if (!out.payment.accounts.length) out.warnings.push("Faktura nie zawiera numeru rachunku (NrRB) – zapytaj sprzedawcę o rachunek.");
    if (out.payment.paid) out.warnings.push("Faktura jest oznaczona jako zapłacona (Zaplacono = 1).");
    out.ok = true;
    return out;
  }
  function ksefFromFilename(name) {
    var c = findCandidates(String(name || "").replace(/_/g, " "));
    for (var i = 0; i < c.length; i++) { var r = checkKsef(c[i]); if (r.kind !== "iz") return r; }
    return null;
  }
  function formatNrb(nrb) {
    var s = String(nrb || "").replace(/\s+/g, "");
    if (/^\d{26}$/.test(s)) return s.slice(0, 2) + " " + s.slice(2).replace(/(\d{4})(?=\d)/g, "$1 ");
    return s.replace(/(.{4})(?=.)/g, "$1 ");
  }
  function nrbValid(nrb) {
    var s = String(nrb || "").replace(/\s+/g, "").toUpperCase();
    if (/^\d{26}$/.test(s)) s = "PL" + s;
    if (!/^[A-Z]{2}\d{2}[A-Z0-9]{10,30}$/.test(s)) return null;
    var r = s.slice(4) + s.slice(0, 4), num = "";
    for (var i = 0; i < r.length; i++) { var ch = r.charCodeAt(i); num += ch >= 65 ? (ch - 55) : r[i]; }
    var mod = 0;
    for (var j = 0; j < num.length; j++) mod = (mod * 10 + +num[j]) % 97;
    return mod === 1;
  }

  /* ---------- KOD I (link weryfikacyjny QR) ---------- */
  function bytesToBase64Url(bytes) {
    var bin = "";
    for (var i = 0; i < bytes.length; i++) bin += String.fromCharCode(bytes[i]);
    var b64 = typeof btoa === "function" ? btoa(bin) : Buffer.from(bin, "binary").toString("base64");
    return b64.replace(/\+/g, "-").replace(/\//g, "_").replace(/=+$/, "");
  }
  function sha256Base64Url(buf) {
    var c = (typeof crypto !== "undefined" && crypto.subtle) ? crypto : null;
    if (!c) return Promise.reject(new Error("Brak WebCrypto"));
    return c.subtle.digest("SHA-256", buf).then(function (h) { return bytesToBase64Url(new Uint8Array(h)); });
  }
  function buildKod1(env, nip, isoDate, hash) {
    var host = env === "TE" ? "qr-test.ksef.mf.gov.pl" : env === "DEMO" ? "qr-demo.ksef.mf.gov.pl" : "qr.ksef.mf.gov.pl";
    var p = String(isoDate || "").split("-");
    return "https://" + host + "/invoice/" + nip + "/" + p[2] + "-" + p[1] + "-" + p[0] + "/" + hash;
  }
  function lookalike(host) {
    return /ksef|mf-gov|mfgov|podatki/i.test(host);
  }
  function parseQrLink(raw, today) {
    var s = String(raw || "").trim();
    var r = { input: s, ok: false, status: "bad", errors: [], warnings: [], notes: [], kind: "", env: "", host: "", phishing: false };
    if (!s) { r.errors.push("Wklej link z kodu QR."); return r; }
    var u;
    try { u = new URL(s); } catch (e) { r.errors.push("To nie jest poprawny adres URL."); return r; }
    r.host = u.hostname.toLowerCase();
    var known = QR_HOSTS[r.host];
    if (!known) {
      r.phishing = true;
      r.errors.push(lookalike(r.host)
        ? "UWAGA: domena „" + r.host + "” udaje adres Ministerstwa Finansów, ale nim nie jest. Nie otwieraj linku i nie podawaj żadnych danych."
        : "Domena „" + r.host + "” nie należy do KSeF. Prawdziwe kody QR prowadzą tylko do qr.ksef.mf.gov.pl (oraz qr-test / qr-demo).");
      return r;
    }
    if (u.protocol !== "https:") r.errors.push("Link musi zaczynać się od https://.");
    if (u.username || u.password || u.port) r.errors.push("Link zawiera nietypowe elementy (login, port) – może być spreparowany.");
    if (u.search || u.hash) r.warnings.push("Link ma dodatkowe parametry (?/#), których prawdziwy kod nie zawiera.");
    r.env = known.env;
    r.envLabel = known.label;
    if (!known.tax) r.warnings.push("To środowisko " + known.label + " – faktura z takiego linku nie ma skutków podatkowych.");
    var segs = u.pathname.replace(/^\/+|\/+$/g, "").split("/");
    if (segs[0] === "invoice") {
      r.kind = "KOD I";
      if (segs.length !== 4) { r.errors.push("KOD I ma postać /invoice/{NIP}/{DD-MM-RRRR}/{skrót}."); return finishQr(r); }
      r.nip = segs[1]; r.nipOk = nipValid(segs[1]);
      if (!r.nipOk) r.errors.push("NIP sprzedawcy w linku jest niepoprawny.");
      var dm = /^(\d{2})-(\d{2})-(\d{4})$/.exec(segs[2]);
      if (!dm || !realDate(+dm[3], +dm[2], +dm[1])) r.errors.push("Data wystawienia w linku jest niepoprawna (format DD-MM-RRRR).");
      else { r.date = dm[1] + "." + dm[2] + "." + dm[3]; if (dm[3] + dm[2] + dm[1] > todayYmd(today)) r.warnings.push("Data wystawienia jest w przyszłości."); }
      r.hash = segs[3];
      if (!/^[A-Za-z0-9_-]{43}$/.test(segs[3])) r.errors.push("Skrót faktury powinien mieć 43 znaki Base64URL (SHA-256).");
    } else if (segs[0] === "certificate") {
      r.kind = "KOD II";
      if (segs.length !== 7) { r.errors.push("KOD II ma postać /certificate/{typ}/{identyfikator}/{NIP}/{nr certyfikatu}/{skrót}/{podpis}."); return finishQr(r); }
      r.ctxType = segs[1]; r.ctxValue = segs[2]; r.nip = segs[3]; r.serial = segs[4]; r.hash = segs[5]; r.signature = segs[6];
      if (["Nip", "InternalId", "NipVatUe", "PeppolId"].indexOf(r.ctxType) < 0) r.errors.push("Nieznany typ kontekstu: " + r.ctxType + ".");
      r.nipOk = nipValid(r.nip);
      if (!r.nipOk) r.errors.push("NIP sprzedawcy w linku jest niepoprawny.");
      if (!/^[A-Za-z0-9_-]{43}$/.test(r.hash)) r.errors.push("Skrót faktury powinien mieć 43 znaki Base64URL.");
      r.notes.push("KOD II (CERTYFIKAT) potwierdza wystawcę faktury offline. Podpis weryfikuje serwis MF po otwarciu linku – to narzędzie go nie sprawdza.");
    } else {
      r.errors.push("Nieznana ścieżka linku – oczekiwano /invoice/… (KOD I) lub /certificate/… (KOD II).");
    }
    return finishQr(r);
  }
  function finishQr(r) { r.status = r.errors.length ? "bad" : r.warnings.length ? "warn" : "ok"; r.ok = r.status !== "bad"; return r; }

  /* ---------- ankieta JDG ---------- */
  function evaluateJdg(a) {
    a = a || {};
    var items = [];
    var b2b = a.b2b === "tak", active = a.vat === "czynny";
    if (!b2b) {
      items.push({ level: "info", date: "—", text: "Wystawiasz faktury tylko konsumentom: faktury dla osób fizycznych nieprowadzących działalności możesz wystawiać w KSeF dobrowolnie." });
    } else {
      if (a.small === "tak") items.push({ level: "must", date: "1 stycznia 2027", text: "Kończy się zwolnienie dla firm ze sprzedażą fakturowaną do 10 000 zł miesięcznie. Od tego dnia faktury dla firm wystawiasz wyłącznie w KSeF." });
      else items.push({ level: "must", date: "już teraz", text: "Faktury dla firm wystawiasz w KSeF (obowiązek trwa od 2026 r.). Jeżeli dotąd korzystałeś ze zwolnienia do 10 000 zł miesięcznie, kończy się ono 31 grudnia 2026 r." });
      if (a.cash === "tak") items.push({ level: "must", date: "1 stycznia 2027", text: "Kończy się możliwość wystawiania faktur z kasy fiskalnej poza KSeF. Fakturę dla firmy trzeba będzie wystawić w KSeF." });
    }
    items.push({ level: "must", date: "już teraz", text: "Faktury zakupowe od innych firm otrzymujesz przez KSeF – potrzebujesz dostępu (Aplikacja Podatnika KSeF lub program księgowy)." });
    if (a.pays === "tak") {
      if (active) items.push({ level: "must", date: "1 stycznia 2027", text: "Płacąc przelewem za fakturę z KSeF innemu czynnemu podatnikowi VAT, podajesz w tytule numer KSeF (lub identyfikator zbiorczy przy kilku fakturach)." });
      else items.push({ level: "info", date: "1 stycznia 2027", text: "Jako podatnik zwolniony z VAT nie masz obowiązku podawania numeru KSeF w przelewach – możesz go podawać dobrowolnie." });
    }
    if (a.mpp === "tak" && active) items.push({ level: "must", date: "1 stycznia 2027", text: "W komunikacie przelewu MPP w polu /INV/ podajesz numer KSeF faktury albo identyfikator zbiorczy zamiast okresu." });
    if (b2b) items.push({ level: "pending", date: "w toku zmian", text: "Kary za niewystawienie faktury w KSeF (art. 106ni): przepisy są obecnie zmieniane w toku prac legislacyjnych – termin i zasady ich stosowania nie są jeszcze przesądzone. Same obowiązki od 1 stycznia 2027 r. pozostają." });
    return items;
  }

  /* ---------- CSV ---------- */
  function csvCell(v) {
    var s = String(v == null ? "" : v);
    return /[";\n\r]/.test(s) ? '"' + s.replace(/"/g, '""') + '"' : s;
  }
  function toCsv(rows) {
    return "\uFEFF" + rows.map(function (r) { return r.map(csvCell).join(";"); }).join("\r\n");
  }

  return {
    EXAMPLE_KSEF: EXAMPLE_KSEF, EXAMPLE_IZ: EXAMPLE_IZ, EXAMPLE_NIP: EXAMPLE_NIP, FA3_NS: FA3_NS, FA2_NS: FA2_NS, QR_HOSTS: QR_HOSTS,
    TITLE_MAX: TITLE_MAX, MPP_MAX: MPP_MAX,
    plural: plural, esc: esc, crc8: crc8, cleanNip: cleanNip, nipValid: nipValid, checkNip: checkNip, formatNip: formatNip,
    normalize: normalize, checkKsef: checkKsef, checkIZ: checkIZ, findCandidates: findCandidates, buildTitle: buildTitle,
    parseAmount: parseAmount, formatAmountComma: formatAmountComma, decimalToCents: decimalToCents, formatPln: formatPln,
    buildMpp: buildMpp, parseFa: parseFa, ksefFromFilename: ksefFromFilename, formatNrb: formatNrb, nrbValid: nrbValid,
    bytesToBase64Url: bytesToBase64Url, sha256Base64Url: sha256Base64Url, buildKod1: buildKod1, parseQrLink: parseQrLink,
    evaluateJdg: evaluateJdg, toCsv: toCsv
  };
});
