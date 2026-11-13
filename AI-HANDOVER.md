# AI handover: Numer KSeF (Polish KSeF tools)

Live site: https://numerksef.dpdns.org/
Owner: Yasir Ali (GitHub mydevspace2). Everything here belongs to the owner and runs free on GitHub Pages, with or without any AI subscription.

## What this site is
Free Polish tools for KSeF invoice numbers: validator, transfer-title/MPP builder, collective ID, bulk CSV check, XML→payment, QR codes, JDG 2027 guide, blog. Language: Polish.

Other sites by the same owner, built the same way: mydevspace2/numer-ksef, mydevspace2/herramientas-verifactu, mydevspace2/trade-charts.

## Rules (always follow)
- Zero budget. Never buy anything (domains, tools, ads) without the owner's explicit "yes".
- Never post anywhere outside this site (Facebook, forums, Reddit) without the owner's OK for that exact post. Drafts live in `_source/docs/` or `_source/seo/promo-drafts.md`.
- Never invent data: every figure, date, legal rule, chart value or rate must come from a cited official or published source. If it can't be verified, leave it out.
- Run every test in `_source/qa/` before pushing. Push only when all pass.
- Never put passwords or tokens in this repo. Logins belong to the owner.
- Keep the Google `google-site-verification` meta tag on the home page and the `CNAME` file (custom domain).

## How to continue with any AI (ChatGPT, Claude, Gemini, Cursor, Copilot)
1. Give the AI this file, `README.md`, and the notes in `_source/docs/` (start with `project-notes.md` if present, then `knowledge-base/README.md`).
2. Paste the daily routine below as your request.
3. The AI edits files in `_source/build/`, rebuilds, runs `_source/qa/`, and copies the output to the repo root. Then commit and push to `main`. GitHub Pages publishes in 1–2 minutes.
4. With no coding tool: open a file on github.com, tap the pencil, paste the AI's edited version, then commit.

## Daily routine (paste to the AI)
Publish 3 new Polish blog posts from `_source/seo/blog-calendar.md` (800–1,200 words, FAQ, link to the matching tool, official sources such as podatki.gov.pl / ksef.podatki.gov.pl / isap.sejm.gov.pl; no penalty dates or amounts unless quoted from law). Expand any tool or page under 1,000 words. Do one SEO fix (internal links, titles under 60 chars, descriptions under 160). Add each new URL to sitemap.xml with today's lastmod. Run the tests, then push.

## Weekly / yearly
- Mondays: Google Search Console (search.google.com/search-console, account topelitemindset1@gmail.com) and Bing Webmaster. Check coverage errors, sitemap status and top queries. Rewrite titles of pages with impressions but low CTR.
- After each new page: Search Console → URL Inspection → Request Indexing (a few a day; quota is limited).
- Every year before 12 Nov: renew the free domain numerksef.dpdns.org in the DigitalPlat dashboard (sign in with GitHub). The renewal window opens around 15 July.
- When the law changes (KSeF dates, 2028 penalties), update the guides.

## Where things are
- `_source/build/`: site generator (Python). `_source/qa/`: tests.
- `_source/docs/` (and `_source/seo/`): blog calendar, keywords, research, project notes, SEO knowledge base and playbook.
- Repo root: the published site (HTML, sitemap.xml, robots.txt).
