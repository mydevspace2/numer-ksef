// Testy jednostkowe logiki NumerKSeF (node test-core.js)
const assert = require("assert");
const fs = require("fs");
const path = require("path");
const K = require("../site-v2/assets/core.js");
const { DOMParser } = require("@xmldom/xmldom");
const TODAY = new Date(2026, 10, 13);
let pass = 0, fail = 0;
function t(name, fn) {
  try { fn(); pass++; console.log("  ✓ " + name); }
  catch (e) { fail++; console.log("  ✗ " + name + "\n      " + e.message); }
}
async function ta(name, fn) {
  try { await fn(); pass++; console.log("  ✓ " + name); }
  catch (e) { fail++; console.log("  ✗ " + name + "\n      " + e.message); }
}

(async () => {
console.log("CRC-8 / numer KSeF");
t("crc8 przykładu MF = AF", () => assert.strictEqual(K.crc8("5265877635-20250826-0100001AF629"), "AF"));
t("przykład MF 5265877635-20250826-0100001AF629-AF przechodzi", () => {
  const r = K.checkKsef("5265877635-20250826-0100001AF629-AF", TODAY);
  assert.strictEqual(r.valid, true); assert.strictEqual(r.status, "ok"); assert.strictEqual(r.parts.crcOk, true);
  assert.strictEqual(r.parts.nip, "5265877635"); assert.strictEqual(r.parts.date, "20250826");
});
t("zmieniona suma …-7C jest odrzucona", () => {
  const r = K.checkKsef("5265877635-20250826-0100001AF629-7C", TODAY);
  assert.strictEqual(r.valid, false); assert.strictEqual(r.parts.crcOk, false); assert.strictEqual(r.parts.calc, "AF");
  assert.ok(r.errors.some(e => /Suma kontrolna/.test(e)));
});
t("inne przykłady MF/przelewyksef przechodzą", () => {
  ["5265877635-20250709-0100E01D6840-3C", "9510001233-20261102-01A3F0C2B7D4-B8"].forEach(n => assert.strictEqual(K.checkKsef(n, TODAY).status, "ok", n));
});
t("przykład mBank (ilustracyjny) jest odrzucony – CRC 3A, zły NIP", () => {
  const r = K.checkKsef("3786417439-20260928-AB12CD34EF56-78", TODAY);
  assert.strictEqual(r.valid, false); assert.strictEqual(r.parts.calc, "3A"); assert.strictEqual(r.parts.nipOk, false);
});
t("normalizacja: spacje, małe litery, długi myślnik", () => {
  const r = K.checkKsef("  5265877635–20250826–0100001af629–af ", TODAY);
  assert.strictEqual(r.valid, true); assert.ok(r.fixes.length >= 2);
});
t("litera O zamiast zera – wskazówka z pozycją", () => {
  const r = K.checkKsef("5265877635-2025O826-0100001AF629-AF", TODAY);
  assert.strictEqual(r.valid, false); assert.ok(r.errors.some(e => /znak 16: „O” – „O” zamiast zera/.test(e)), r.errors.join("|"));
});
t("zła długość", () => { const r = K.checkKsef("5265877635-20250826-0100001AF629-A", TODAY); assert.ok(/Zła długość: 34/.test(r.errors[0])); });
t("36 znaków (KSeF 1.0) = ostrzeżenie, nie błąd", () => {
  const r = K.checkKsef("5265877635-20250826-010000-1AF629-AF", TODAY);
  assert.strictEqual(r.kind, "ksef1"); assert.strictEqual(r.status, "warn"); assert.strictEqual(r.valid, true);
});
t("prefiks inny niż NIP (M + 9 cyfr) = ostrzeżenie", () => {
  const base = "M123456789-20260310-0100001AF629-";
  const r = K.checkKsef(base + K.crc8(base.slice(0, 32)), TODAY);
  assert.strictEqual(r.status, "warn", JSON.stringify(r.errors)); assert.strictEqual(r.parts.nip, null);
});
t("data z przyszłości = błąd", () => {
  const base = "5265877635-20271231-0100001AF629-";
  const r = K.checkKsef(base + K.crc8(base.slice(0, 32)), TODAY);
  assert.strictEqual(r.valid, false); assert.ok(r.errors.some(e => /przyszłości/.test(e)));
});
t("nieistniejąca data (30 lutego) = błąd", () => {
  const base = "5265877635-20260230-0100001AF629-";
  assert.strictEqual(K.checkKsef(base + K.crc8(base.slice(0, 32)), TODAY).valid, false);
});

console.log("Identyfikator zbiorczy");
t("przykład MF 1111111111-IZ202607-65ED02180000-E7 przechodzi", () => {
  const r = K.checkIZ("1111111111-IZ202607-65ED02180000-E7", TODAY);
  assert.strictEqual(r.status, "ok"); assert.strictEqual(r.parts.calc, "E7"); assert.strictEqual(r.parts.month, 7); assert.strictEqual(r.parts.year, 2026);
});
t("checkKsef automatycznie rozpoznaje IZ", () => assert.strictEqual(K.checkKsef("1111111111-IZ202607-65ED02180000-E7", TODAY).kind, "iz"));
t("IZ ze zmienioną sumą jest odrzucony", () => assert.strictEqual(K.checkIZ("1111111111-IZ202607-65ED02180000-E8", TODAY).valid, false));
t("IZ z miesiącem 13 jest odrzucony", () => assert.strictEqual(K.checkIZ("1111111111-IZ202613-65ED02180000-E7", TODAY).valid, false));

console.log("NIP");
t("NIP 5265877635 poprawny", () => assert.strictEqual(K.nipValid("5265877635"), true));
t("NIP 1111111111 poprawny", () => assert.strictEqual(K.nipValid("1111111111"), true));
t("NIP 5265877636 błędny", () => assert.strictEqual(K.nipValid("5265877636"), false));
t("NIP z myślnikami i PL – checkNip", () => assert.strictEqual(K.checkNip("PL 526-587-76-35").valid, true));
t("NIP 3786417439 (mBank) błędny", () => assert.strictEqual(K.nipValid("3786417439"), false));

console.log("Tytuł przelewu");
t("3 numery + opis mieszczą się w 140", () => {
  const r = K.buildTitle(["5265877635-20250826-0100001AF629-AF", "5265877635-20250709-0100E01D6840-3C", "9510001233-20261102-01A3F0C2B7D4-B8"], "FV 1/2026");
  assert.strictEqual(r.length, 35 * 3 + 4 + 10); assert.strictEqual(r.ok, true);
});
t("4 numery = ostrzeżenie", () => {
  const n = "5265877635-20250826-0100001AF629-AF";
  const r = K.buildTitle([n, n, n, n], ""); assert.strictEqual(r.ok, false); assert.ok(r.warnings.length >= 1);
});

console.log("Komunikat MPP");
t("przykład: jedna faktura – dokładny wynik i długość", () => {
  const r = K.buildMpp({ vat: "230.00", gross: "1 230,00", nip: "526-587-76-35", inv: "5265877635-20250826-0100001AF629-AF", txt: "FV 12/11/2026" }, TODAY);
  assert.strictEqual(r.ok, true, r.errors.join("|"));
  assert.strictEqual(r.text, "/VAT/230,00/IDC/5265877635/INV/5265877635-20250826-0100001AF629-AF/TXT/FV 12/11/2026");
  assert.strictEqual(r.length, r.text.length); assert.strictEqual(r.length, 5 + 6 + 5 + 10 + 5 + 35 + 5 + 13); assert.strictEqual(r.length, 84);
  assert.deepStrictEqual(r.lines4, ["/VAT/230,00", "/IDC/5265877635", "/INV/5265877635-20250826-0100001AF629-AF", "/TXT/FV 12/11/2026"]);
  assert.strictEqual(r.lines35.join(""), r.text); assert.ok(r.lines35.every(l => l.length <= 35));
  assert.strictEqual(r.invKind, "ksef");
});
t("formuła długości 5+len(VAT)+5+len(NIP)+5+35(+5+len(TXT))", () => {
  const r = K.buildMpp({ vat: "23035,9", nip: "5265877635", inv: "5265877635-20250826-0100001AF629-AF", txt: "x".repeat(33) }, TODAY);
  assert.strictEqual(r.length, 5 + 8 + 5 + 10 + 5 + 35 + 5 + 33); assert.ok(r.length <= 140); assert.strictEqual(r.ok, true);
});
t("identyfikator zbiorczy w /INV/", () => {
  const r = K.buildMpp({ vat: "4600", gross: "24600", nip: "1111111111", inv: "1111111111-IZ202607-65ED02180000-E7" }, TODAY);
  assert.strictEqual(r.ok, true); assert.strictEqual(r.invKind, "iz"); assert.strictEqual(r.text, "/VAT/4600,00/IDC/1111111111/INV/1111111111-IZ202607-65ED02180000-E7");
});
t("VAT > brutto = błąd", () => assert.strictEqual(K.buildMpp({ vat: "300", gross: "200", nip: "5265877635", inv: "5265877635-20250826-0100001AF629-AF" }, TODAY).ok, false));
t("VAT 0,00 = błąd", () => assert.strictEqual(K.buildMpp({ vat: "0", nip: "5265877635", inv: "5265877635-20250826-0100001AF629-AF" }, TODAY).ok, false));
t("zabronione znaki w /TXT/", () => {
  const r = K.buildMpp({ vat: "1", nip: "5265877635", inv: "5265877635-20250826-0100001AF629-AF", txt: "zapłata #1!" }, TODAY);
  assert.strictEqual(r.ok, false); assert.ok(r.fieldErrors.txt.some(e => /#/.test(e) && /!/.test(e)));
});
t("/TXT/ dłuższy niż 33 = błąd", () => assert.strictEqual(K.buildMpp({ vat: "1", nip: "5265877635", inv: "5265877635-20250826-0100001AF629-AF", txt: "x".repeat(34) }, TODAY).ok, false));
t("błędny numer KSeF w /INV/ = błąd", () => assert.strictEqual(K.buildMpp({ vat: "1", nip: "5265877635", inv: "5265877635-20250826-0100001AF629-7C" }, TODAY).ok, false));
t("błędny NIP = błąd", () => assert.strictEqual(K.buildMpp({ vat: "1", nip: "5265877636", inv: "5265877635-20250826-0100001AF629-AF" }, TODAY).ok, false));
t("przekazanie własne", () => {
  const r = K.buildMpp({ vat: "100", gross: "100", nip: "5265877635", own: true }, TODAY);
  assert.strictEqual(r.text, "/VAT/100,00/IDC/5265877635/INV/PRZEKAZANIE WLASNE"); assert.strictEqual(r.ok, true);
});
t("numer faktury zamiast KSeF w 2027 = ostrzeżenie (ok)", () => {
  const r = K.buildMpp({ vat: "23", nip: "5265877635", inv: "FV/1/2027", date: "2027-01-05" }, TODAY);
  assert.strictEqual(r.ok, true); assert.ok(r.warnings.length >= 1);
});
t("parseAmount: formaty", () => {
  assert.strictEqual(K.parseAmount("1 234,5").text, "1234,50");
  assert.strictEqual(K.parseAmount("1.234,56").text, "1234,56");
  assert.strictEqual(K.parseAmount("1234.56").text, "1234,56");
  assert.strictEqual(K.parseAmount("12,345").ok, false);
});

console.log("FA(3) XML");
const sample = fs.readFileSync(path.join(__dirname, "../site-v2/assets/przyklad-fa3.xml"), "utf8");
t("parsowanie przykładowej faktury FA(3)", () => {
  const f = K.parseFa(sample, DOMParser);
  assert.strictEqual(f.ok, true, f.errors.join("|"));
  assert.strictEqual(f.schema, "FA(3)");
  assert.strictEqual(f.seller.nip, "5265877635"); assert.strictEqual(f.seller.nipOk, true);
  assert.strictEqual(f.seller.name, "Przykładowy Sprzedawca Sp. z o.o.");
  assert.strictEqual(f.buyer.nip, "1111111111");
  assert.strictEqual(f.number, "FV/123/11/2026"); assert.strictEqual(f.issueDate, "2026-11-12");
  assert.strictEqual(f.grossCents, 2000000); assert.strictEqual(f.vatCents, 373984); assert.strictEqual(f.amountToPayCents, 2000000);
  assert.strictEqual(f.splitPayment, true);
  assert.deepStrictEqual(f.payment.dueDates, ["2026-11-26"]); assert.strictEqual(f.payment.method, "Przelew");
  assert.strictEqual(f.payment.accounts[0].nrb, "60102010260000123456789012");
  assert.strictEqual(K.nrbValid(f.payment.accounts[0].nrb), true);
});
t("przykładowy XML z prefiksem przestrzeni nazw (ns:) też działa", () => {
  const pref = sample.replace('<Faktura xmlns="http://crd.gov.pl/wzor/2025/06/25/13775/"', '<tns:Faktura xmlns:tns="http://crd.gov.pl/wzor/2025/06/25/13775/"')
    .replace(/<(\/?)(?!tns:|\?|etd:)([A-Za-z_][\w]*)/g, "<$1tns:$2");
  const f = K.parseFa(pref, DOMParser);
  assert.strictEqual(f.ok, true, f.errors.join("|")); assert.strictEqual(f.seller.nip, "5265877635"); assert.strictEqual(f.splitPayment, true);
});
t("DoZaplaty ma pierwszeństwo przed P_15", () => {
  const x = sample.replace("<Platnosc>", "<Rozliczenie><Odliczenia><Kwota>500.00</Kwota><Powod>Zaliczka</Powod></Odliczenia><SumaOdliczen>500.00</SumaOdliczen><DoZaplaty>19500.00</DoZaplaty></Rozliczenie><Platnosc>");
  assert.strictEqual(K.parseFa(x, DOMParser).amountToPayCents, 1950000);
});
t("FA(2) – ostrzeżenie, dane odczytane", () => {
  const f = K.parseFa(sample.replace("http://crd.gov.pl/wzor/2025/06/25/13775/", K.FA2_NS), DOMParser);
  assert.strictEqual(f.schema, "FA(2)"); assert.strictEqual(f.seller.nip, "5265877635");
});
t("nie-faktura (UPO) – błąd", () => assert.strictEqual(K.parseFa('<?xml version="1.0"?><Potwierdzenie xmlns="x"><a/></Potwierdzenie>', DOMParser).ok, false));
t("numer KSeF z nazwy pliku", () => {
  const r = K.ksefFromFilename("5265877635-20250826-0100001AF629-AF.xml"); assert.ok(r && r.valid); assert.strictEqual(r.input, "5265877635-20250826-0100001AF629-AF");
  assert.strictEqual(K.ksefFromFilename("faktura_5265877635-20250826-0100001AF629-AF.xml").input, "5265877635-20250826-0100001AF629-AF");
  assert.strictEqual(K.ksefFromFilename("faktura.xml"), null);
});
t("komunikat MPP z faktury: VAT 3739,84, NIP, numer KSeF, P_2 w TXT", () => {
  const f = K.parseFa(sample, DOMParser);
  const m = K.buildMpp({ vat: K.formatAmountComma(f.vatPlnCents), gross: K.formatAmountComma(f.amountToPayCents), nip: f.seller.nip, inv: "5265877635-20250826-0100001AF629-AF", txt: "FV " + f.number }, TODAY);
  assert.strictEqual(m.ok, true, m.errors.join("|"));
  assert.strictEqual(m.text, "/VAT/3739,84/IDC/5265877635/INV/5265877635-20250826-0100001AF629-AF/TXT/FV FV/123/11/2026");
});

console.log("Wyszukiwanie w tekście");
t("findCandidates w tytułach i komunikacie MPP", () => {
  const s = "2026-11-05;BUDMAR;/VAT/4600,00/IDC/1111111111/INV/1111111111-IZ202607-65ED02180000-E7 oraz 5265877635-20250709-0100E01D6840-3C";
  assert.deepStrictEqual(K.findCandidates(s), ["1111111111-IZ202607-65ED02180000-E7", "5265877635-20250709-0100E01D6840-3C"]);
  assert.deepStrictEqual(K.findCandidates("Zapłata za fakturę 15/10/2026"), []);
});
t("CSV z BOM i średnikiem", () => {
  const c = K.toCsv([["a", "b;c"], ['x"y', "z"]]);
  assert.strictEqual(c, '\uFEFFa;"b;c"\r\n"x""y";z');
});

console.log("KOD I / linki QR");
t("przykład MF KOD I jest poprawny (TE, ostrzeżenie o braku skutków)", () => {
  const r = K.parseQrLink("https://qr-test.ksef.mf.gov.pl/invoice/1111111111/01-02-2026/UtQp9Gpc51y-u3xApZjIjgkpZ01js-J8KflSPW8WzIE", TODAY);
  assert.strictEqual(r.ok, true, r.errors.join("|")); assert.strictEqual(r.env, "TE"); assert.strictEqual(r.status, "warn"); assert.strictEqual(r.date, "01.02.2026");
});
t("skrót przykładu MF dekoduje się do 32 bajtów", () => assert.strictEqual(Buffer.from("UtQp9Gpc51y-u3xApZjIjgkpZ01js-J8KflSPW8WzIE", "base64url").length, 32));
t("fałszywa domena = phishing", () => {
  const r = K.parseQrLink("https://qr.ksef.mf.gov.pl.weryfikacja.example/invoice/1111111111/01-02-2026/UtQp9Gpc51y-u3xApZjIjgkpZ01js-J8KflSPW8WzIE", TODAY);
  assert.strictEqual(r.phishing, true); assert.strictEqual(r.ok, false); assert.ok(/udaje/.test(r.errors[0]));
});
t("http zamiast https = błąd", () => assert.strictEqual(K.parseQrLink("http://qr.ksef.mf.gov.pl/invoice/1111111111/01-02-2026/UtQp9Gpc51y-u3xApZjIjgkpZ01js-J8KflSPW8WzIE", TODAY).ok, false));
t("KOD II jest rozpoznawany", () => {
  const r = K.parseQrLink("https://qr-test.ksef.mf.gov.pl/certificate/Nip/1111111111/1111111111/01F20A5D352AE590/UtQp9Gpc51y-u3xApZjIjgkpZ01js-J8KflSPW8WzIE/c2lnbmF0dXJl", TODAY);
  assert.strictEqual(r.kind, "KOD II"); assert.strictEqual(r.ok, true, r.errors.join("|"));
});
await ta("KOD I z pliku: SHA-256 Base64URL (WebCrypto) + budowa linku", async () => {
  const buf = fs.readFileSync(path.join(__dirname, "../site-v2/assets/przyklad-fa3.xml"));
  const h = await K.sha256Base64Url(buf);
  const expect = require("crypto").createHash("sha256").update(buf).digest("base64url");
  assert.strictEqual(h, expect); assert.strictEqual(h.length, 43);
  const link = K.buildKod1("PROD", "5265877635", "2026-11-12", h);
  assert.strictEqual(link, "https://qr.ksef.mf.gov.pl/invoice/5265877635/12-11-2026/" + h);
  const back = K.parseQrLink(link, TODAY); assert.strictEqual(back.status, "ok", back.errors.concat(back.warnings).join("|"));
});

console.log("Ankieta JDG");
t("czynny VAT, B2B, limit, płaci, MPP – pełna lista + kary w toku", () => {
  const it = K.evaluateJdg({ b2b: "tak", vat: "czynny", small: "tak", cash: "tak", pays: "tak", mpp: "tak" });
  assert.ok(it.some(i => /10 000/.test(i.text))); assert.ok(it.some(i => /kasy fiskalnej/.test(i.text)));
  assert.ok(it.some(i => /numer KSeF/.test(i.text) && i.level === "must")); assert.ok(it.some(i => i.level === "pending" && /prac legislacyjnych/.test(i.text) && !/2028/.test(i.text + i.date)));
});
t("zwolniony z VAT – numer KSeF w przelewie dobrowolny", () => {
  const it = K.evaluateJdg({ b2b: "tak", vat: "zwolniony", pays: "tak" });
  assert.ok(it.some(i => /dobrowolnie/.test(i.text) && i.level === "info"));
});

console.log("\nWynik: " + pass + " zaliczonych, " + fail + " niezaliczonych");
process.exit(fail ? 1 : 0);
})();
