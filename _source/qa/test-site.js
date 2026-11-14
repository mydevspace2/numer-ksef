// Testy strony: linki, JSON-LD, meta, treść, smoke-testy narzędzi w jsdom
const fs = require("fs"), path = require("path"), assert = require("assert");
const { JSDOM } = require("jsdom");
const ROOT = path.join(__dirname, "../site-v2");
let pass = 0, fail = 0;
function t(name, fn) { try { fn(); pass++; console.log("  ✓ " + name); } catch (e) { fail++; console.log("  ✗ " + name + "\n      " + e.message); } }
async function ta(name, fn) { try { await fn(); pass++; console.log("  ✓ " + name); } catch (e) { fail++; console.log("  ✗ " + name + "\n      " + e.message); } }

const pages = [];
(function walk(d) { for (const f of fs.readdirSync(d)) { const p = path.join(d, f); if (fs.statSync(p).isDirectory()) walk(p); else if (f.endsWith(".html")) pages.push(p); } })(ROOT);
function urlToFile(u) {
  u = u.split("#")[0].split("?")[0];
  if (!u) return null;
  let p = path.join(ROOT, decodeURIComponent(u));
  if (u.endsWith("/")) p = path.join(p, "index.html");
  return p;
}

console.log("Pliki i linki wewnętrzne (" + pages.length + " stron HTML)");
const titles = {}, descs = {}, faqQs = {};
const wordReport = [];
const sitemap = fs.readFileSync(path.join(ROOT, "sitemap.xml"), "utf8");
for (const file of pages) {
  const rel = "/" + path.relative(ROOT, file).replace(/index\.html$/, "");
  const html = fs.readFileSync(file, "utf8");
  const dom = new JSDOM(html);
  const doc = dom.window.document;
  t(rel + " – linki wewnętrzne istnieją", () => {
    const bad = [];
    doc.querySelectorAll("a[href], link[href], script[src]").forEach(el => {
      const u = el.getAttribute("href") || el.getAttribute("src");
      if (/^(https?:|mailto:|#)/.test(u)) return;
      if (!u.startsWith("/")) { bad.push(u + " (nie zaczyna się od /)"); return; }
      const f = urlToFile(u);
      if (!fs.existsSync(f)) bad.push(u);
    });
    assert.deepStrictEqual(bad, []);
  });
  t(rel + " – kotwice #id istnieją", () => {
    const bad = [];
    doc.querySelectorAll('a[href^="#"]').forEach(a => { const id = a.getAttribute("href").slice(1); if (id && !doc.getElementById(id)) bad.push(id); });
    assert.deepStrictEqual(bad, []);
  });
  t(rel + " – JSON-LD parsuje się (WebApplication/WebPage + BreadcrumbList)", () => {
    const blocks = [...doc.querySelectorAll('script[type="application/ld+json"]')];
    assert.ok(blocks.length >= 1);
    blocks.forEach(b => {
      const j = JSON.parse(b.textContent);
      const types = j["@graph"].map(x => x["@type"]);
      assert.ok(types.includes("BreadcrumbList"), types.join());
      assert.ok(types.includes("WebApplication") || types.includes("WebPage"));
      const faq = j["@graph"].find(x => x["@type"] === "FAQPage");
      if (faq) assert.strictEqual(faq.mainEntity.length, doc.querySelectorAll(".faq details").length, "FAQ w JSON-LD = FAQ na stronie");
    });
  });
  t(rel + " – meta: title, description, canonical, OG, jedno H1, lang=pl", () => {
    const title = doc.title, desc = doc.querySelector('meta[name="description"]').content;
    assert.ok(title.length > 10 && title.length <= 75, "title len " + title.length);
    assert.ok(desc.length >= 70 && desc.length < 160, "desc len " + desc.length);
    assert.ok(!titles[title], "powtórzony title"); titles[title] = 1;
    assert.ok(!descs[desc], "powtórzony description"); descs[desc] = 1;
    const can = doc.querySelector('link[rel="canonical"]').href;
    assert.ok(can.startsWith("https://numerksef.dpdns.org/"));
    if (!rel.includes("404")) assert.strictEqual(can, "https://numerksef.dpdns.org" + rel, "canonical = adres strony");
    ["og:title", "og:description", "og:url", "og:type", "og:locale"].forEach(p => assert.ok(doc.querySelector('meta[property="' + p + '"]'), p));
    assert.strictEqual(doc.querySelectorAll("h1").length, 1);
    assert.strictEqual(doc.documentElement.lang, "pl");
    if (!rel.includes("404")) assert.ok(sitemap.includes("<loc>" + can + "</loc>"), "w sitemap: " + can);
  });
  t(rel + " – dostępność: etykiety pól, alt/aria, brak zewnętrznych skryptów", () => {
    const unlabeled = [];
    doc.querySelectorAll("input:not([type=radio]):not([type=checkbox]):not([type=file]), textarea, select").forEach(i => {
      if (!doc.querySelector('label[for="' + i.id + '"]') && !i.getAttribute("aria-label")) unlabeled.push(i.id);
    });
    assert.deepStrictEqual(unlabeled, []);
    doc.querySelectorAll("script[src]").forEach(s => assert.ok(s.getAttribute("src").startsWith("/assets/"), "zewnętrzny skrypt"));
    assert.ok(!/googleapis|gstatic|cdn\.|unpkg|jsdelivr|analytics|gtag/i.test(html), "brak CDN/trackerów");
    const ids = [...doc.querySelectorAll("[id]")].map(e => e.id); const dup = ids.filter((x, i) => ids.indexOf(x) !== i);
    assert.deepStrictEqual(dup, [], "duplikaty id");
  });
  t(rel + " – v3: stopka (kontakt, regulamin, prywatność, o serwisie, blog), przełącznik motywu, brak dat kar", () => {
    ["/kontakt/", "/regulamin/", "/polityka-prywatnosci/", "/o-serwisie/", "/blog/"].forEach(u => assert.ok(doc.querySelector('.site-foot a[href="' + u + '"]'), "stopka: " + u));
    assert.ok(doc.querySelector("button.theme-toggle"), "przełącznik motywu");
    assert.ok(/localStorage\.getItem\("theme"\)/.test(html) && /prefers-color-scheme: dark/.test(html), "inicjalizacja motywu");
    assert.ok(!/2028/.test(html), "brak daty 2028");
    const gsv = html.includes('name="google-site-verification" content="elPNThwVdT6P4PDIZnIkvzQFaVe5GeQ3MDhBJpephcI"');
    if (rel === "/") assert.ok(gsv, "google-site-verification na stronie głównej");
    doc.querySelectorAll(".faq summary").forEach(q => { assert.ok(!faqQs[q.textContent], "powtórzone pytanie FAQ: " + q.textContent + " (" + faqQs[q.textContent] + ")"); faqQs[q.textContent] = rel; });
  });
  if (rel.startsWith("/blog/") && rel !== "/blog/") {
    t(rel + " – artykuł: Article JSON-LD, 900–1200 słów, link do narzędzia", () => {
      const j = JSON.parse(doc.querySelector('script[type="application/ld+json"]').textContent);
      const art = j["@graph"].find(x => x["@type"] === "Article"); assert.ok(art && art.headline && art.datePublished && art.author && art.publisher);
      const c = doc.querySelector("article.content").cloneNode(true);
      ["#zrodla", ".sources", "#inne-narzedzia", "#powiazane-artykuly", ".hub", ".updated"].forEach(s => c.querySelectorAll(s).forEach(x => x.remove()));
      const words = c.textContent.trim().split(/\s+/).filter(w => /[\p{L}\d]/u.test(w)).length;
      wordReport.push([rel, words]);
      assert.ok(words >= 900 && words <= 1200, "słów: " + words);
      const toolLinks = [...c.querySelectorAll("a")].filter(a => ["/", "/przelew-mpp-numer-ksef/", "/identyfikator-zbiorczy-ksef/", "/sprawdz-wiele-numerow-ksef/", "/przelew-z-faktury-xml-ksef/", "/kod-qr-ksef/"].includes(a.getAttribute("href")));
      assert.ok(toolLinks.length >= 2, "linki do narzędzi: " + toolLinks.length);
      console.log("      (artykuł: " + words + " słów)");
    });
  }
  if (doc.querySelector(".faq")) {
    t(rel + " – treść: 600–1000 słów, FAQ 5–8 (narzędzia), źródła, data aktualizacji, nota o prywatności", () => {
      const art = doc.querySelector("article.content").cloneNode(true);
      ["#faq", ".faq", "#zrodla", ".sources", "#inne-narzedzia", "#powiazane-artykuly", ".hub", ".updated"].forEach(s => art.querySelectorAll(s).forEach(x => x.remove()));
      const words = art.textContent.trim().split(/\s+/).filter(w => /[\p{L}\d]/u.test(w)).length;
      const isTool = !!doc.querySelector(".tool");
      wordReport.push([rel, words]);
      if (isTool) { assert.ok(words >= 1000 && words <= 1250, "słów w poradniku: " + words); assert.ok(art.querySelector("table"), "tabela"); assert.ok(/[Pp]rzykład/.test(art.textContent), "przykład"); assert.ok(doc.querySelectorAll(".faq details").length >= 5 && doc.querySelectorAll(".faq details").length <= 8); }
      console.log("      (poradnik: " + words + " słów, FAQ: " + doc.querySelectorAll(".faq details").length + ")");
      assert.ok(doc.querySelectorAll(".sources a").length >= 2);
      assert.ok(html.includes("13 listopada 2026"));
      assert.ok(html.includes("Dane nie opuszczają Twojej przeglądarki."));
    });
  }
}
const SEO_TOOLS = ["/", "/przelew-mpp-numer-ksef/", "/identyfikator-zbiorczy-ksef/", "/sprawdz-wiele-numerow-ksef/", "/przelew-z-faktury-xml-ksef/", "/kod-qr-ksef/", "/ksef-od-2027-jdg/"];
console.log("SEO (2026-11-13)");
for (const file of pages) {
  const rel = "/" + path.relative(ROOT, file).replace(/index\.html$/, "");
  if (rel.includes("404")) continue;
  const html = fs.readFileSync(file, "utf8");
  const doc = new JSDOM(html).window.document;
  const url = "https://numerksef.dpdns.org" + rel;
  t(rel + " – SEO: hreflang pl + x-default, OG image 1200x630, Twitter large card", () => {
    assert.strictEqual(doc.querySelector('link[rel="alternate"][hreflang="pl"]').href, url);
    assert.strictEqual(doc.querySelector('link[rel="alternate"][hreflang="x-default"]').href, url);
    assert.strictEqual(doc.querySelector('meta[property="og:image"]').content, "https://numerksef.dpdns.org/assets/og-numerksef.png");
    assert.strictEqual(doc.querySelector('meta[property="og:image:width"]').content, "1200");
    assert.strictEqual(doc.querySelector('meta[property="og:image:height"]').content, "630");
    assert.strictEqual(doc.querySelector('meta[name="twitter:card"]').content, "summary_large_image");
    ["twitter:title", "twitter:description", "twitter:image"].forEach(n => assert.ok(doc.querySelector('meta[name="' + n + '"]').content, n));
  });
  t(rel + " – SEO: JSON-LD typy (narzędzie → WebApplication, home → Organization+WebSite, podstrony → BreadcrumbList ≥2)", () => {
    const g = JSON.parse(doc.querySelector('script[type="application/ld+json"]').textContent)["@graph"];
    const types = g.map(x => x["@type"]);
    if (SEO_TOOLS.includes(rel)) { const app = g.find(x => x["@type"] === "WebApplication"); assert.ok(app && app.offers && app.offers.price === "0" && app.image, "WebApplication"); }
    if (rel === "/") { assert.ok(types.includes("Organization") && types.includes("WebSite"), types.join()); assert.ok(g.find(x => x["@type"] === "Organization").logo.url.endsWith("/assets/logo-512.png")); }
    else assert.ok(g.find(x => x["@type"] === "BreadcrumbList").itemListElement.length >= 2, "breadcrumb");
  });
  t(rel + " – SEO: blok powiązanych narzędzi i artykułów na dole, obrazki z wymiarami, brak blokujących skryptów", () => {
    assert.ok(doc.querySelector("#inne-narzedzia"), "powiązane narzędzia");
    const arts = doc.querySelectorAll("#powiazane-artykuly + .hub a");
    assert.ok(arts.length >= 2, "powiązane artykuły: " + arts.length);
    arts.forEach(a => assert.ok(a.getAttribute("href").startsWith("/blog/") && a.getAttribute("href") !== rel));
    doc.querySelectorAll("img").forEach(i => assert.ok(i.getAttribute("width") && i.getAttribute("height"), "img bez wymiarów"));
    doc.querySelectorAll("script[src]").forEach(s => assert.ok(s.hasAttribute("defer") || s.hasAttribute("async"), "blokujący skrypt " + s.src));
    assert.strictEqual(doc.querySelectorAll('link[rel="stylesheet"]').length, 0, "CSS inline – brak arkusza blokującego renderowanie");
    assert.strictEqual(doc.querySelectorAll("head style").length, 1, "jeden blok <style> w <head>");
  });
  t(rel + " – CSP (hash skryptu i stylu inline), referrer, brak atrybutów style", () => {
    const crypto = require("crypto"); const h = x => "'sha256-" + crypto.createHash("sha256").update(x, "utf8").digest("base64") + "'";
    const meta = doc.querySelector('meta[http-equiv="Content-Security-Policy"]'); assert.ok(meta, "CSP");
    const csp = meta.content;
    assert.ok(/default-src 'self'/.test(csp) && /img-src 'self' data:/.test(csp) && /object-src 'none'/.test(csp));
    assert.ok(!/unsafe-eval|unsafe-inline/.test(csp), "bez unsafe-*");
    const inl = [...doc.querySelectorAll("script:not([src])")].filter(s => s.type !== "application/ld+json");
    inl.forEach(s => assert.ok(csp.includes(h(s.textContent)), "hash skryptu inline"));
    assert.ok(csp.includes(h(doc.querySelector("head style").textContent)), "hash stylu inline");
    assert.ok([...doc.head.children].indexOf(meta) < [...doc.head.children].indexOf(doc.querySelector("head script")), "CSP przed skryptem");
    assert.strictEqual(doc.querySelector('meta[name="referrer"]').content, "strict-origin-when-cross-origin");
    assert.strictEqual(doc.querySelectorAll("[style]").length, 0, "atrybuty style zablokowałby CSP");
    assert.ok(!/ on[a-z]+="/i.test(html), "brak inline handlerów");
  });
}
t("zasoby: JS zminifikowany, bez eval/new Function/atrybutów style; czytelne źródła w build/assets-src", () => {
  const A = path.join(ROOT, "assets"), SRC = path.join(__dirname, "../build/assets-src");
  fs.readdirSync(A).filter(f => f.endsWith(".js")).forEach(f => {
    const min = fs.readFileSync(path.join(A, f), "utf8"), src = fs.readFileSync(path.join(SRC, f), "utf8");
    assert.ok(min.length < src.length * 0.9, f + " niezminifikowany");
    assert.ok(!/\beval\(|new Function\(|style=\\?"/.test(min), f + ": eval/Function/style=");
  });
  assert.ok(!fs.existsSync(path.join(A, "style.css")), "style.css inline");
});
t("SEO: obraz OG to PNG 1200x630 < 200 KB, logo 512x512; plik klucza IndexNow", () => {
  const b = fs.readFileSync(path.join(ROOT, "assets/og-numerksef.png"));
  assert.strictEqual(b.toString("ascii", 1, 4), "PNG"); assert.strictEqual(b.readUInt32BE(16), 1200); assert.strictEqual(b.readUInt32BE(20), 630); assert.ok(b.length < 200000);
  const l = fs.readFileSync(path.join(ROOT, "assets/logo-512.png")); assert.strictEqual(l.readUInt32BE(16), 512);
  const keyf = fs.readdirSync(ROOT).filter(f => /^[0-9a-f]{32}\.txt$/.test(f));
  assert.strictEqual(keyf.length, 1); assert.strictEqual(fs.readFileSync(path.join(ROOT, keyf[0]), "utf8"), keyf[0].replace(".txt", ""));
});
t("SEO: tytuły zawierają najmocniejsze frazy z autocomplete", () => {
  const T = r => new JSDOM(fs.readFileSync(urlToFile(r), "utf8")).window.document.title.toLowerCase();
  assert.ok(T("/").includes("numer ksef w przelewie"));
  assert.ok(T("/przelew-mpp-numer-ksef/").includes("numer ksef w przelewie mpp"));
  assert.ok(T("/identyfikator-zbiorczy-ksef/").includes("identyfikator zbiorczy ksef"));
  assert.ok(T("/kod-qr-ksef/").includes("kod qr ksef"));
  assert.ok(T("/ksef-od-2027-jdg/").includes("ksef jdg"));
  assert.ok(T("/przelew-z-faktury-xml-ksef/").includes("faktura xml ksef"));
  Object.keys(titles).forEach(x => assert.ok(x.length <= 60, "title > 60: " + x));
});
t("sitemap: wszystkie strony indeksowalne, lastmod w formacie daty; robots wskazuje sitemap; manifest JSON; CNAME", () => {
  const nUrl = (sitemap.match(/<url>/g) || []).length;
  const nIdx = pages.filter(f => !/404\.html$/.test(f) && !f.includes(path.sep + "_source" + path.sep)).length;
  assert.strictEqual(nUrl, nIdx, "URL w sitemap = strony HTML bez 404");
  assert.strictEqual((sitemap.match(/<lastmod>20\d\d-\d\d-\d\d(T\d\d:\d\d:\d\d\+05:00)?<\/lastmod>/g) || []).length, nUrl);
  sitemap.match(/<loc>([^<]+)<\/loc>/g).forEach(l => { const u = l.replace(/<\/?loc>/g, "").replace("https://numerksef.dpdns.org", ""); assert.ok(fs.existsSync(urlToFile(u)), u); });
  assert.ok(/Sitemap: https:\/\/numerksef\.dpdns\.org\/sitemap\.xml/.test(fs.readFileSync(path.join(ROOT, "robots.txt"), "utf8")));
  JSON.parse(fs.readFileSync(path.join(ROOT, "site.webmanifest"), "utf8"));
  assert.strictEqual(fs.readFileSync(path.join(ROOT, "CNAME"), "utf8").trim(), "numerksef.dpdns.org");
});

// ---------------- smoke tests w jsdom
function load(rel) {
  const html = fs.readFileSync(urlToFile(rel), "utf8");
  const dom = new JSDOM(html, { url: "https://numerksef.dpdns.org" + rel, pretendToBeVisual: true, runScripts: "outside-only" });
  const w = dom.window;
  w.fetch = (u) => Promise.resolve({ text: () => Promise.resolve(fs.readFileSync(path.join(ROOT, u), "utf8")), arrayBuffer: () => { const b = fs.readFileSync(path.join(ROOT, u)); return Promise.resolve(b.buffer.slice(b.byteOffset, b.byteOffset + b.byteLength)); } });
  Object.defineProperty(w, "crypto", { value: require("crypto").webcrypto });
  w.TextDecoder = TextDecoder; w.TextEncoder = TextEncoder;
  w.Element.prototype.scrollIntoView = function () {};
  const errors = [];
  w.addEventListener("error", e => errors.push(e.message));
  [...w.document.querySelectorAll("script[src]")].forEach(s => {
    const code = fs.readFileSync(urlToFile(s.getAttribute("src")), "utf8");
    try { w.eval(code); } catch (e) { errors.push(s.getAttribute("src") + ": " + e.message); }
  });
  return { w, d: w.document, errors };
}
const tick = (ms) => new Promise(r => setTimeout(r, ms || 30));
function click(d, id) { d.getElementById(id).dispatchEvent(new d.defaultView.MouseEvent("click", { bubbles: true })); }

(async () => {
  console.log("Smoke-testy interfejsu (jsdom)");
  await ta("/ – Przykład → zielony status, tytuł z 2 numerami", async () => {
    const { d, errors } = load("/");
    click(d, "k-ex"); assert.ok(d.getElementById("k-res").classList.contains("ok"), d.getElementById("k-res").textContent);
    d.getElementById("k-in").value = "5265877635-20250826-0100001AF629-7C"; d.getElementById("k-in").dispatchEvent(new d.defaultView.Event("input"));
    assert.ok(d.getElementById("k-res").classList.contains("bad")); assert.ok(/AF/.test(d.getElementById("k-res").textContent));
    click(d, "t-ex"); const out = d.getElementById("t-out").textContent;
    assert.strictEqual(out, "5265877635-20250826-0100001AF629-AF, 9510001233-20261102-01A3F0C2B7D4-B8 FV 12/11/2026");
    assert.ok(!d.getElementById("t-copy").disabled); assert.deepStrictEqual(errors, []);
  });
  await ta("/przelew-mpp-numer-ksef/ – przykłady i parametry z adresu", async () => {
    const { d, errors } = load("/przelew-mpp-numer-ksef/");
    click(d, "m-ex"); assert.strictEqual(d.getElementById("m-out").textContent, "/VAT/230,00/IDC/5265877635/INV/5265877635-20250826-0100001AF629-AF/TXT/FV 12/11/2026");
    assert.ok(d.getElementById("m-stat").classList.contains("ok"), d.getElementById("m-stat").textContent);
    assert.strictEqual(d.querySelectorAll("#m-lines4 > div").length, 4); assert.ok(d.querySelectorAll("#m-lines35 li").length >= 3);
    click(d, "m-ex-iz"); assert.ok(/INV\/1111111111-IZ202607-65ED02180000-E7/.test(d.getElementById("m-out").textContent));
    d.getElementById("m-txt").value = "zakaz: #"; d.getElementById("m-txt").dispatchEvent(new d.defaultView.Event("input"));
    assert.ok(d.getElementById("m-stat").classList.contains("bad")); assert.ok(d.getElementById("m-copy").disabled);
    assert.deepStrictEqual(errors, []);
    const q = load("/przelew-mpp-numer-ksef/?vat=10&nip=5265877635&inv=5265877635-20250826-0100001AF629-AF");
    assert.strictEqual(q.d.getElementById("m-out").textContent, "/VAT/10,00/IDC/5265877635/INV/5265877635-20250826-0100001AF629-AF");
  });
  await ta("/identyfikator-zbiorczy-ksef/ – przykład MF zielony, numer KSeF rozpoznany", async () => {
    const { d, errors } = load("/identyfikator-zbiorczy-ksef/");
    click(d, "iz-ex"); assert.ok(d.getElementById("iz-res").classList.contains("ok"), d.getElementById("iz-res").textContent);
    d.getElementById("iz-in").value = "5265877635-20250826-0100001AF629-AF"; click(d, "iz-check");
    assert.ok(/nie identyfikator zbiorczy/.test(d.getElementById("iz-res").textContent)); assert.deepStrictEqual(errors, []);
  });
  await ta("/sprawdz-wiele-numerow-ksef/ – lista, wyciąg, CSV", async () => {
    const { w, d, errors } = load("/sprawdz-wiele-numerow-ksef/");
    click(d, "b-ex"); const rows = d.querySelectorAll("#b-body tr"); assert.strictEqual(rows.length, 5);
    assert.ok(/2 błędnych|2 błędne/.test(d.getElementById("b-sum").textContent) || /błędnych/.test(d.getElementById("b-sum").textContent), d.getElementById("b-sum").textContent);
    click(d, "b-ex-statement"); const txt = d.getElementById("b-body").textContent; assert.ok(/Brak numeru/.test(txt)); assert.strictEqual(d.querySelectorAll("#b-body tr").length, 4);
    let csv = null; w.URL.createObjectURL = (b) => { csv = b; return "blob:x"; }; w.URL.revokeObjectURL = () => {};
    click(d, "b-csv"); assert.ok(csv); const bytes = new Uint8Array(await csv.arrayBuffer()); assert.deepStrictEqual([...bytes.slice(0, 3)], [0xEF, 0xBB, 0xBF], "BOM"); assert.ok(Buffer.from(bytes).toString("utf8").includes("Wiersz;Status;Numer"));
    assert.deepStrictEqual(errors, []);
  });
  await ta("/przelew-z-faktury-xml-ksef/ – przykład: karta płatności z MPP", async () => {
    const { d, errors } = load("/przelew-z-faktury-xml-ksef/");
    click(d, "x-ex"); await tick(80);
    const c = d.getElementById("x-cards").textContent;
    assert.ok(/Przykładowy Sprzedawca/.test(c)); assert.ok(/60 1020 1026 0000 1234 5678 9012/.test(c), "NRB");
    assert.ok(/\/VAT\/3739,84\/IDC\/5265877635\/INV\/5265877635-20250826-0100001AF629-AF\/TXT\/FV FV\/123\/11\/2026/.test(c), "MPP");
    assert.ok(/26\.11\.2026/.test(c)); assert.ok(/P_18A = 1/.test(c));
    assert.deepStrictEqual(errors, []);
  });
  await ta("/kod-qr-ksef/ – dekoder (MF, phishing) i generator z pliku", async () => {
    const { w, d, errors } = load("/kod-qr-ksef/");
    click(d, "d-ex"); assert.ok(d.getElementById("d-res").classList.contains("warn"), d.getElementById("d-res").className);
    click(d, "d-ex-bad"); assert.ok(d.getElementById("d-res").classList.contains("bad")); assert.ok(/Podejrzany/.test(d.getElementById("d-res").textContent));
    const buf = fs.readFileSync(path.join(ROOT, "assets/przyklad-fa3.xml"));
    const file = new w.File([buf], "5265877635-20250826-0100001AF629-AF.xml", { type: "application/xml" });
    const inp = d.getElementById("g-file"); Object.defineProperty(inp, "files", { value: [file] });
    inp.dispatchEvent(new w.Event("change")); await tick(200);
    const link = d.getElementById("g-link").textContent;
    const h = require("crypto").createHash("sha256").update(buf).digest("base64url");
    assert.strictEqual(link, "https://qr.ksef.mf.gov.pl/invoice/5265877635/12-11-2026/" + h);
    assert.ok(d.querySelector("#g-qr svg path")); assert.strictEqual(d.getElementById("g-label").textContent, "5265877635-20250826-0100001AF629-AF");
    d.getElementById("d-in").value = link; click(d, "d-check"); assert.ok(/zgodny z wczytanym plikiem/.test(d.getElementById("d-res").textContent));
    fs.writeFileSync(path.join(__dirname, "qr-generated.svg"), d.getElementById("g-qr").innerHTML);
    fs.writeFileSync(path.join(__dirname, "qr-generated.txt"), link);
    assert.deepStrictEqual(errors, []);
  });
  await ta("/ksef-od-2027-jdg/ – ankieta zwraca listę z karą w toku", async () => {
    const { w, d, errors } = load("/ksef-od-2027-jdg/");
    ["b2b=tak", "vat=czynny", "small=tak", "cash=nie", "pays=tak", "mpp=tak"].forEach(p => { const [n, v] = p.split("="); d.querySelector('input[name="' + n + '"][value="' + v + '"]').checked = true; });
    d.getElementById("j-form").dispatchEvent(new w.Event("submit", { cancelable: true }));
    const out = d.getElementById("j-out").textContent; assert.ok(/W toku legislacji/.test(out)); assert.ok(/1 stycznia 2027/.test(out));
    assert.deepStrictEqual(errors, []);
  });
    await ta("motyw: przełącznik zmienia data-theme, aria-pressed i zapisuje localStorage", async () => {
    const { w, d, errors } = load("/kontakt/");
    const btn = d.querySelector(".theme-toggle");
    const before = d.documentElement.getAttribute("data-theme");
    assert.ok(before === "light" || before === "dark", "start: " + before);
    btn.dispatchEvent(new w.MouseEvent("click", { bubbles: true }));
    const after = d.documentElement.getAttribute("data-theme");
    assert.notStrictEqual(after, before); assert.strictEqual(w.localStorage.getItem("theme"), after);
    assert.strictEqual(btn.getAttribute("aria-pressed"), after === "dark" ? "true" : "false");
    assert.deepStrictEqual(errors, []);
  });
  console.log("\nSłowa (poradnik bez FAQ/źródeł):"); wordReport.forEach(([r, n]) => console.log("  " + r + ": " + n));
  console.log("\nWynik: " + pass + " zaliczonych, " + fail + " niezaliczonych");
  process.exit(fail ? 1 : 0);
})();
