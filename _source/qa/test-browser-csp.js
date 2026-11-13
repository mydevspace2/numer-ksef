// Prawdziwa przeglądarka (Chromium/Playwright): CSP nie blokuje niczego, CSS inline działa, narzędzia działają.
// Uruchom: node qa/test-browser-csp.js  (wymaga playwright: NODE_PATH=/tmp/pw/node_modules)
const { chromium } = require("playwright");
const http = require("http"), fs = require("fs"), path = require("path");
const ROOT = path.join(__dirname, "../site-v2");
const TYPES = { ".html": "text/html; charset=utf-8", ".js": "application/javascript", ".css": "text/css", ".svg": "image/svg+xml", ".png": "image/png", ".xml": "application/xml", ".txt": "text/plain", ".webmanifest": "application/manifest+json" };
const srv = http.createServer((q, r) => {
  let p = decodeURIComponent(q.url.split("?")[0]); if (p.endsWith("/")) p += "index.html";
  const f = path.join(ROOT, p);
  if (!fs.existsSync(f)) { r.writeHead(404, { "content-type": TYPES[".html"] }); return r.end(fs.readFileSync(path.join(ROOT, "404.html"))); }
  r.writeHead(200, { "content-type": TYPES[path.extname(f)] || "application/octet-stream" }); r.end(fs.readFileSync(f));
}).listen(8767);
let pass = 0, fail = 0;
const ok = (c, m) => { if (c) { pass++; console.log("  ✓ " + m); } else { fail++; console.log("  ✗ " + m); } };
const PAGES = ["/", "/przelew-mpp-numer-ksef/", "/identyfikator-zbiorczy-ksef/", "/sprawdz-wiele-numerow-ksef/", "/przelew-z-faktury-xml-ksef/", "/kod-qr-ksef/", "/ksef-od-2027-jdg/", "/blog/", "/blog/jak-wpisac-numer-ksef-w-tytule-przelewu/", "/blog/gdzie-znalezc-numer-ksef-faktury/", "/blog/identyfikator-zbiorczy-ksef-co-to-jest/", "/kontakt/", "/regulamin/", "/polityka-prywatnosci/", "/o-serwisie/", "/nie-ma-takiej-strony/"];
const ACTIONS = {
  "/": async p => { await p.click("#k-ex"); await p.click("#t-ex"); return (await p.textContent("#k-res")).length > 10 && (await p.textContent("#t-out")).length > 10; },
  "/przelew-mpp-numer-ksef/": async p => { await p.click("#m-ex"); const a = await p.textContent("#m-out"); await p.click("#m-ex-iz"); return /\/VAT\//.test(a) && /\/INV\//.test(await p.textContent("#m-out")); },
  "/identyfikator-zbiorczy-ksef/": async p => { await p.click("#iz-ex"); await p.waitForTimeout(150); return /poprawn/i.test(await p.textContent("main")); },
  "/sprawdz-wiele-numerow-ksef/": async p => { await p.click("#b-ex"); await p.click("#b-check"); await p.waitForTimeout(200);
    const dl = p.waitForEvent("download", { timeout: 3000 }).then(() => true).catch(() => false); await p.click("#b-csv"); return (await p.$$("tbody tr")).length >= 2 && await dl; },
  "/przelew-z-faktury-xml-ksef/": async p => { await p.click("#x-ex"); await p.waitForTimeout(600); return /3739,84|3 ?739,84/.test(await p.textContent("main")); },
  "/kod-qr-ksef/": async p => { await p.click("#g-ex"); await p.waitForTimeout(800); const svg = await p.$("#g-qr svg"); await p.click("#d-ex-bad"); await p.waitForTimeout(200);
    const t = await p.textContent("#d-res"); return !!svg && /phishing|fałszyw|podrob|nie jest/i.test(t); },
  "/ksef-od-2027-jdg/": async p => {
    await p.evaluate(() => { const seen = {}; document.querySelectorAll('#tresc input[type=radio]').forEach(r => { if (!seen[r.name]) { seen[r.name] = 1; r.checked = true; r.dispatchEvent(new Event("change", { bubbles: true })); } }); });
    const btn = await p.$('#tresc form button[type=submit], #tresc form button:not([type=button])'); if (btn) await btn.click(); else await p.evaluate(() => document.querySelector("#tresc form").requestSubmit());
    await p.waitForTimeout(200); return (await p.textContent("#j-out")).length > 20; },
};
(async () => {
  const b = await chromium.launch();
  for (const u of PAGES) {
    const ctx = await b.newContext({ acceptDownloads: true }); const p = await ctx.newPage();
    const errs = [];
    p.on("console", m => { if (m.type() === "error" && !/404 \(Not Found\)/.test(m.text())) errs.push(m.text()); });
    p.on("pageerror", e => errs.push(String(e)));
    await p.addInitScript(() => document.addEventListener("securitypolicyviolation", e => console.error("CSP violation: " + e.violatedDirective + " " + e.blockedURI)));
    await p.goto("http://127.0.0.1:8767" + u, { waitUntil: "load" });
    const css = await p.evaluate(() => ({ bg: getComputedStyle(document.querySelector(".site-head")).position, theme: document.documentElement.getAttribute("data-theme"), wrap: getComputedStyle(document.querySelector(".wrap")).maxWidth }));
    ok(css.theme && css.wrap !== "none", u + " – CSS inline zastosowany, motyw ustawiony (" + css.theme + ", .wrap max-width " + css.wrap + ")");
    if (ACTIONS[u]) { let r = false; try { r = await ACTIONS[u](p); } catch (e) { errs.push("akcja: " + e.message); } ok(r, u + " – narzędzie działa w Chromium"); }
    const mt = await p.evaluate(() => { const el = document.querySelector(".mt14,.mt12,.mt10,.mt8"); return el ? getComputedStyle(el).marginTop : null; });
    if (mt) ok(/^(8|10|12|14)px$/.test(mt), u + " – klasy zamiast style= działają (margin-top " + mt + ")");
    await p.click("button.theme-toggle"); const t2 = await p.evaluate(() => document.documentElement.getAttribute("data-theme"));
    ok(t2 && t2 !== css.theme, u + " – przełącznik motywu działa");
    ok(errs.length === 0, u + " – brak błędów JS i naruszeń CSP" + (errs.length ? ": " + errs.join(" | ") : ""));
    await ctx.close();
  }
  await b.close(); srv.close();
  console.log("\nWynik: " + pass + " zaliczonych, " + fail + " niezaliczonych"); process.exit(fail ? 1 : 0);
})();
