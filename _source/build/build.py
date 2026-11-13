# -*- coding: utf-8 -*-
import os, sys, shutil
sys.path.insert(0, os.path.dirname(__file__))
import common
from common import render, DOMAIN, UPDATED_ISO
from pages1 import HOME, MPP, IZ, BULK
from pages2 import XMLP, QRP, JDG, PRIV, ABOUT

OUT = os.path.join(os.path.dirname(__file__), "..", "site-v2")
OUT = os.path.abspath(OUT)
MPP["content"] = MPP["content"].replace("&amp;%%()", "&amp;%()")
import extras
IZ["content"] += extras.IZ_EXTRA; QRP["content"] += extras.QR_EXTRA; JDG["content"] += extras.JDG_EXTRA
MPP["content"] += extras.MPP_EXTRA; XMLP["content"] += extras.XML_EXTRA; BULK["content"] += extras.BULK_EXTRA
import v3_tools as V, v3_pages as VP
HOME["content"] += V.HOME_EXTRA; HOME["faq"] = HOME["faq"] + V.HOME_FAQ
MPP["content"] += V.MPP_EXTRA; MPP["faq"] = MPP["faq"] + V.MPP_FAQ
IZ["content"] += V.IZ_EXTRA; IZ["faq"] = IZ["faq"] + V.IZ_FAQ
BULK["content"] += V.BULK_EXTRA; BULK["faq"] = BULK["faq"] + V.BULK_FAQ
XMLP["content"] += V.XML_EXTRA; XMLP["faq"] = XMLP["faq"] + V.XML_FAQ
QRP["content"] += V.QR_EXTRA; QRP["faq"] = QRP["faq"] + V.QR_FAQ
JDG["content"] += V.JDG_EXTRA
JDG["faq"] = [V.JDG_FAQ_REPLACE.get(q, (q, a)) for q, a in JDG["faq"]] + V.JDG_FAQ
ABOUT["content"] += '<p>Zobacz też: <a href="/kontakt/">Kontakt</a> · <a href="/regulamin/">Regulamin</a> · <a href="/polityka-prywatnosci/">Polityka prywatności</a> · <a href="/blog/">Blog</a>.</p>'
ABOUT["desc"] = "NumerKSeF to niezależny serwis z darmowymi narzędziami do numerów KSeF, przelewów MPP i faktur XML. Niezwiązany z MF. Nie stanowi porady podatkowej."

# --- Zasoby: minifikacja JS (terser) i CSS (csso) z build/assets-src; CSS wstawiany inline
import subprocess
subprocess.run(["node", os.path.join(os.path.dirname(__file__), "tools", "minify.js")], check=True)
_cssf = os.path.join(OUT, "assets", ".style.min.css")
common.INLINE_CSS = open(_cssf, encoding="utf-8").read().replace("</", "<\\/")
os.remove(_cssf)
for _f in ("style.css",):
    if os.path.exists(os.path.join(OUT, "assets", _f)):
        os.remove(os.path.join(OUT, "assets", _f))

# --- SEO 2026-11-13: tytuły i H1 dopasowane do najmocniejszych fraz z Google Autocomplete (work/seo/keywords.md)
HOME["title"] = "Numer KSeF w przelewie – sprawdź numer i tytuł przelewu"
HOME["h1"] = "Sprawdź numer KSeF i przygotuj tytuł przelewu"
MPP["title"] = "Numer KSeF w przelewie MPP – generator komunikatu"
MPP["h1"] = "Numer KSeF w przelewie MPP – generator komunikatu split payment"
XMLP["title"] = "Faktura XML KSeF – otwórz plik i skopiuj dane do przelewu"
XMLP["h1"] = "Faktura XML KSeF – otwórz plik i przygotuj przelew z numerem KSeF"
QRP["title"] = "Kod QR KSeF – jak sprawdzić fakturę i wygenerować KOD I"
QRP["h1"] = "Kod QR KSeF – jak sprawdzić fakturę i czy nie jest podróbką"
JDG["title"] = "KSeF JDG od kiedy? Sprawdź, co zmienia się w 2027"
JDG["h1"] = "KSeF dla JDG – od kiedy i co zmienia się 1 stycznia 2027?"
BULK["title"] = "Sprawdź wiele numerów KSeF naraz – lista, CSV, wyciąg"
IZ["title"] = "Identyfikator zbiorczy KSeF – sprawdź poprawność online"

# Blok powiązanych narzędzi i artykułów na każdej stronie (także prawnych)
PRIV["related"] = True; VP.KONTAKT["related"] = True; VP.REGULAMIN["related"] = True
# Blok „Powiązane artykuły” na dole stron
common.ARTICLES[:] = [("/blog/%s/" % p["slug"], p["h1"], p["desc"]) for p in VP.POSTS]
_A1, _A2, _A3 = ["/blog/%s/" % p["slug"] for p in VP.POSTS]  # tytuł przelewu, gdzie znaleźć, identyfikator zbiorczy
common.ARTICLE_MAP.update({
    "/": [_A1, _A2, _A3], "/przelew-mpp-numer-ksef/": [_A1, _A3, _A2], "/identyfikator-zbiorczy-ksef/": [_A3, _A1, _A2],
    "/sprawdz-wiele-numerow-ksef/": [_A2, _A1, _A3], "/przelew-z-faktury-xml-ksef/": [_A2, _A1, _A3],
    "/kod-qr-ksef/": [_A2, _A1, _A3], "/ksef-od-2027-jdg/": [_A1, _A2, _A3],
})

PAGES = [
    ("/", HOME), ("/przelew-mpp-numer-ksef/", MPP), ("/identyfikator-zbiorczy-ksef/", IZ),
    ("/sprawdz-wiele-numerow-ksef/", BULK), ("/przelew-z-faktury-xml-ksef/", XMLP), ("/kod-qr-ksef/", QRP),
    ("/ksef-od-2027-jdg/", JDG), ("/polityka-prywatnosci/", PRIV), ("/o-serwisie/", ABOUT),
    ("/kontakt/", VP.KONTAKT), ("/regulamin/", VP.REGULAMIN), ("/blog/", VP.blog_index()),
]
for _p in VP.POSTS:
    _page, _url = VP.post_page(_p)
    PAGES.append((_url, _page))

def write(rel, content):
    p = os.path.join(OUT, rel.lstrip("/"))
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, "w", encoding="utf-8") as f:
        f.write(content)

for path, page in PAGES:
    write(path + "index.html" if path.endswith("/") else path, render(page, path))

NF = dict(
    title="Nie znaleziono strony (404) – NumerKSeF",
    desc="Ta strona nie istnieje. Przejdź do darmowych narzędzi KSeF: walidator numeru, przelew MPP, identyfikator zbiorczy i kod QR.",
    app=False, trust=False, noindex=True,
    h1="Nie znaleziono strony",
    intro="Adres mógł się zmienić albo zawiera literówkę. Wybierz jedno z narzędzi poniżej.",
    trail=[("Strona główna", "/"), ("Błąd 404", "/404.html")],
    content='<p><a class="btn" href="/">Przejdź do walidatora numeru KSeF</a></p>',
)
write("/404.html", render(NF, "/404.html"))

# lastmod: nowa data tylko dla stron, które zmieniły się względem wdrożonej kopii (repo/)
import re as _re, datetime as _dt
REPO = os.path.abspath(os.path.join(OUT, "..", "repo"))
_old = {}
try:
    for _loc, _lm in _re.findall(r"<loc>([^<]+)</loc><lastmod>([^<]+)</lastmod>", open(os.path.join(REPO, "sitemap.xml"), encoding="utf-8").read()):
        if re.match(r"^\d{4}-\d{2}-\d{2}", _lm or ""):
            _old[_loc.replace(DOMAIN, "")] = _lm
except OSError:
    pass
NOW = (os.environ.get("NUMERKSEF_LASTMOD") if re.match(r"^\d{4}-\d{2}-\d{2}", os.environ.get("NUMERKSEF_LASTMOD") or "") else None) or _dt.datetime.now(_dt.timezone(_dt.timedelta(hours=5))).replace(microsecond=0).isoformat()
def lastmod(u):
    newf = os.path.join(OUT, u.lstrip("/"), "index.html")
    oldf = os.path.join(REPO, u.lstrip("/"), "index.html")
    try:
        if u in _old and open(newf, encoding="utf-8").read() == open(oldf, encoding="utf-8").read():
            return _old[u]
    except OSError:
        pass
    return NOW

urls = [p for p, _ in PAGES]
sm = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
for u in urls:
    pr = "1.0" if u == "/" else ("0.3" if u in ("/polityka-prywatnosci/", "/o-serwisie/", "/kontakt/", "/regulamin/") else ("0.6" if u.startswith("/blog/") else "0.8"))
    sm.append("  <url><loc>%s%s</loc><lastmod>%s</lastmod><priority>%s</priority></url>" % (DOMAIN, u, lastmod(u), pr))
sm.append("</urlset>\n")
write("/sitemap.xml", "\n".join(sm))
write("/robots.txt", "User-agent: *\nAllow: /\nDisallow: /_source/\n\nSitemap: %s/sitemap.xml\n" % DOMAIN)

FAV = ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 32 32"><rect width="32" height="32" rx="8" fill="#1747c9"/>'
       '<path d="M9 9h3v6.2L17.6 9h3.7l-6 6.6L21.6 23h-3.8l-4.6-5.4-1.2 1.3V23H9z" fill="#fff"/>'
       '<circle cx="24.5" cy="24.5" r="4.5" fill="#22c55e" stroke="#fff" stroke-width="1.5"/>'
       '<path d="M22.4 24.6l1.4 1.4 2.7-2.8" fill="none" stroke="#fff" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg>\n')
write("/favicon.svg", FAV)
write("/site.webmanifest", """{
  "name": "Numer KSeF – darmowe narzędzia",
  "short_name": "NumerKSeF",
  "description": "Darmowe narzędzia KSeF: walidator numeru, przelew MPP, identyfikator zbiorczy, faktura XML, kod QR.",
  "lang": "pl",
  "start_url": "/",
  "scope": "/",
  "display": "standalone",
  "background_color": "#f6f8fb",
  "theme_color": "#1747c9",
  "icons": [{ "src": "/favicon.svg", "sizes": "any", "type": "image/svg+xml", "purpose": "any" },
            { "src": "/assets/logo-512.png", "sizes": "512x512", "type": "image/png", "purpose": "any" }]
}
""")
shutil.copy(os.path.join(OUT, "..", "repo", "CNAME"), os.path.join(OUT, "CNAME"))
write("/.nojekyll", "")
# IndexNow: plik klucza w katalogu głównym
write("/%s.txt" % common.INDEXNOW_KEY, common.INDEXNOW_KEY)
# Obraz OG 1200x630 i logo 512 – generowane lokalnie (PIL)
import og_image
og_image.og(os.path.join(OUT, "assets", "og-numerksef.png"))
og_image.logo(os.path.join(OUT, "assets", "logo-512.png"))
print("built", OUT)
