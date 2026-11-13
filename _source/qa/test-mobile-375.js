// Mobile 375x812 (touch): input + result above the fold, no sideways scroll after results, tap/badge/input sizes.
// Run: NODE_PATH=/tmp/pw/node_modules node qa/test-mobile-375.js
const { chromium } = require("playwright");
const http = require("http"), fs = require("fs"), path = require("path");
const ROOT = path.join(__dirname, "../site-v2");
const TYPES = { ".html": "text/html; charset=utf-8", ".js": "application/javascript", ".svg": "image/svg+xml", ".png": "image/png", ".xml": "application/xml", ".txt": "text/plain" };
const srv = http.createServer((q, r) => {
  let p = decodeURIComponent(q.url.split("?")[0]); if (p.endsWith("/")) p += "index.html";
  const f = path.join(ROOT, p);
  if (!fs.existsSync(f)) { r.writeHead(404); return r.end(); }
  r.writeHead(200, { "content-type": TYPES[path.extname(f)] || "application/octet-stream" }); r.end(fs.readFileSync(f));
}).listen(8768);
let pass = 0, fail = 0;
const ok = (c, m) => { if (c) { pass++; console.log("  ✓ " + m); } else { fail++; console.log("  ✗ " + m); } };
const B = "http://127.0.0.1:8768";
const EX = "5265877635-20250826-0100001AF629-AF";
async function widest(p) {
  return p.evaluate(() => { const W = document.documentElement.clientWidth; let worst = null;
    document.querySelectorAll("main *").forEach(el => { const r = el.getBoundingClientRect(); if (r.right > W + 1 && (!worst || r.right > worst.r)) { let a = el; let clipped = false; while ((a = a.parentElement)) { const s = getComputedStyle(a); if (/(auto|scroll|hidden)/.test(s.overflowX)) { clipped = true; break; } } if (!clipped) worst = { r: Math.round(r.right), tag: el.tagName + "." + el.className + "#" + el.id }; } });
    return { sw: document.documentElement.scrollWidth, W, worst }; });
}
const TOOLS = {
  "/": { inp: "#k-in", res: "#k-res", btn: "#k-check", after: async p => { await p.click("#k-ex"); await p.click("#t-ex"); } },
  "/identyfikator-zbiorczy-ksef/": { inp: "#iz-in", res: "#iz-res", btn: "#iz-check", val: "1111111111-IZ202607-65ED02180000-E7" },
  "/przelew-mpp-numer-ksef/": { after: async p => { await p.click("#m-ex"); await p.click("#m-ex-iz"); await p.click("#m-ex"); } },
  "/sprawdz-wiele-numerow-ksef/": { after: async p => { await p.click("#b-ex"); await p.click("#b-check"); } },
  "/przelew-z-faktury-xml-ksef/": { after: async p => { await p.click("#x-ex"); await p.waitForTimeout(600); } },
  "/kod-qr-ksef/": { after: async p => { await p.click("#d-ex"); await p.click("#g-ex"); await p.waitForTimeout(800); } },
  "/ksef-od-2027-jdg/": { after: async p => { await p.evaluate(() => { const seen = {}; document.querySelectorAll('#j-form input[type=radio]').forEach(r => { if (!seen[r.name]) { seen[r.name] = 1; r.click(); } }); }); } },
};
(async () => {
  const b = await chromium.launch();
  for (const [u, T] of Object.entries(TOOLS)) {
    const ctx = await b.newContext({ viewport: { width: 375, height: 812 }, isMobile: true, hasTouch: true, deviceScaleFactor: 2 });
    const p = await ctx.newPage(); const errs = [];
    p.on("pageerror", e => errs.push(String(e))); p.on("console", m => { if (m.type() === "error") errs.push(m.text()); });
    await p.goto(B + u, { waitUntil: "load" });
    const w0 = await widest(p); ok(w0.sw <= 375, u + " – no sideways scroll on load (scrollWidth " + w0.sw + ")");
    if (T.inp) {
      const ib = await p.$eval(T.inp, el => { const r = el.getBoundingClientRect(); return r.bottom + window.scrollY; });
      // paste a valid value, check the green result's top part fits above 812 without scrolling
      await p.fill(T.inp, T.val || EX);
      const rr = await p.$eval(T.res, el => { const h = el.querySelector(".status-head"); const r = (h || el).getBoundingClientRect(); return { top: r.top + window.scrollY, bottom: r.bottom + window.scrollY, ok: el.classList.contains("ok") }; });
      ok(ib <= 812, u + " – input bottom at " + Math.round(ib) + "px (≤ 812)");
      ok(rr.ok && rr.bottom <= 812, u + " – green ✓ result head at " + Math.round(rr.top) + "–" + Math.round(rr.bottom) + "px (≤ 812, live)");
      // Enter: blur + result into view
      await p.evaluate(() => window.scrollTo(0, 0));
      await p.focus(T.inp); await p.keyboard.press("Enter"); await p.waitForTimeout(700);
      const st = await p.evaluate(([i, r]) => { const el = document.querySelector(r); const b = el.getBoundingClientRect(); return { blurred: document.activeElement !== document.querySelector(i), inView: b.top >= 0 && b.top < innerHeight }; }, [T.inp, T.res]);
      ok(st.blurred && st.inView, u + " – Enter blurs input and result is in view");
      await p.fill(T.inp, ""); await p.focus(T.inp); await p.fill(T.inp, T.val || EX); await p.click(T.btn); await p.waitForTimeout(500);
      const st2 = await p.evaluate(([i, r]) => ({ blurred: document.activeElement !== document.querySelector(i), inView: document.querySelector(r).getBoundingClientRect().top < innerHeight }), [T.inp, T.res]);
      ok(st2.blurred && st2.inView, u + " – Sprawdź blurs input and result is in view");
    }
    if (T.after) await T.after(p);
    if (u === "/identyfikator-zbiorczy-ksef/") { await p.click("#iz-ex"); ok(await p.$eval("#iz-res", el => { const b = el.querySelector("#iz-copy"); return !!b && b.getAttribute("data-copy-text") === "1111111111-IZ202607-65ED02180000-E7"; }), u + " – result has a copy button with the identifier"); }
    if (u === "/ksef-od-2027-jdg/") { await p.waitForTimeout(400); ok(await p.$eval("#j-out", el => el.querySelectorAll(".checklist li").length > 0), u + " – result shows automatically once all questions are answered (no button click)"); ok(!!(await p.$("#j-form button[type=submit]")), u + " – submit button kept"); }
    await p.waitForTimeout(300);
    const w1 = await widest(p); ok(w1.sw <= 375, u + " – no sideways scroll after results (scrollWidth " + w1.sw + (w1.worst ? ", widest " + w1.worst.tag + " → " + w1.worst.r : "") + ")");
    const sizes = await p.evaluate(() => {
      const bad = [];
      document.querySelectorAll("main button, main .btn").forEach(el => { const r = el.getBoundingClientRect(); if (r.width && r.height < 44) bad.push("btn " + (el.id || el.textContent.trim().slice(0, 20)) + " " + Math.round(r.height)); });
      document.querySelectorAll("main input:not([type=radio]):not([type=checkbox]):not([type=file]), main textarea, main select").forEach(el => { const f = parseFloat(getComputedStyle(el).fontSize); if (el.getBoundingClientRect().width && f < 16) bad.push("input " + el.id + " " + f); });
      document.querySelectorAll(".trust li, .badge").forEach(el => { const f = parseFloat(getComputedStyle(el).fontSize); if (el.getBoundingClientRect().width && f < 13) bad.push("badge " + el.textContent.slice(0, 15) + " " + f); });
      return bad; });
    ok(sizes.length === 0, u + " – buttons ≥44px, inputs ≥16px, badges ≥13px" + (sizes.length ? ": " + sizes.join(", ") : ""));
    ok(errs.length === 0, u + " – no JS/CSP errors" + (errs.length ? ": " + errs.join(" | ") : ""));
    if (u === "/") await p.screenshot({ path: path.join(__dirname, "m375-home-after.png") });
    await ctx.close();
  }
  await b.close(); srv.close();
  console.log("\nWynik: " + pass + " zaliczonych, " + fail + " niezaliczonych"); process.exit(fail ? 1 : 0);
})();
