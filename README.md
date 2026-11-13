# numerksef.dpdns.org – handover guide

Free Polish KSeF tools site. Owner: Yasir Ali. Everything here belongs to you and keeps running without Hark.

## Where everything lives
| What | Where | Login |
|---|---|---|
| Website files | This GitHub repo (`mydevspace2/numer-ksef`, branch `main`) | GitHub account mydevspace2 |
| Hosting | GitHub Pages (free): repo → Settings → Pages, deploys from `main` / root | same |
| Domain `numerksef.dpdns.org` | DigitalPlat dashboard (dash.domain.digitalplat.org), sign in with GitHub | same |
| Google Search Console | search.google.com/search-console, property `https://numerksef.dpdns.org/` | topelitemindset1@gmail.com |
| Bing Webmaster Tools | bing.com/webmasters (imported from Search Console) | topelitemindset1@gmail.com |

## Must do every year
- **Renew the free domain** in DigitalPlat before it expires (registered 2026-11-12). If it lapses, the site goes offline at that address.
- Keep the `CNAME` file in this repo. Deleting it disconnects the domain.
- Keep the `google-site-verification` meta tag in `index.html`.

## Quick edits (phone or PC, no tools needed)
1. Open the file on github.com (for example `index.html` or `blog/.../index.html`).
2. Tap the pencil icon, change the text, then "Commit changes".
3. The site updates in 1–2 minutes.

Tip: for bigger changes, paste the file into any free AI (ChatGPT, Gemini), ask for the change, and paste the result back.

## Adding a new blog post
1. Copy an existing post folder in `blog/` (e.g. `blog/<post>/index.html`) to a new folder with a short Polish slug.
2. Change the `<title>`, meta description, H1, canonical URL and text.
3. Add a link to it on `blog/index.html`.
4. Add the URL to `sitemap.xml`.
5. In Search Console, use URL Inspection → Request Indexing.
Post ideas: `_source/seo/blog-calendar.md` (30 planned posts) and `_source/seo/keywords.md`.

## Full rebuild (optional, for developers)
The generator that produced this site is in `_source/build/` (Python 3 + Node for minifying).
```
cd _source/build && python3 build.py        # writes ../site-v2/
cd tools && npm install && node minify.js    # minify JS
```
Then copy the output over the repo root (keep CNAME, the IndexNow key .txt and .nojekyll).
Tests: `_source/qa/` (`npm install`, then `node test-site.js`).
Small edits are easier straight in the HTML, as above.

## Rules worth keeping
- Don't state KSeF penalty dates (still unconfirmed).
- AdSense: apply only after ~3 months and real traffic; add `ads.txt` after approval.
