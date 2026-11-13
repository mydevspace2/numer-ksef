# -*- coding: utf-8 -*-
"""Wspólne elementy szablonu NumerKSeF v2."""
import json, html, hashlib, base64

DOMAIN = "https://numerksef.dpdns.org"
SITE = "Numer KSeF – darmowe narzędzia"
BRAND = "NumerKSeF"
UPDATED_ISO = "2026-11-13"
UPDATED_PL = "13 listopada 2026"
ASSET_V = "4"
OG_IMAGE = "/assets/og-numerksef.png"
OG_W, OG_H = 1200, 630
LOGO_PNG = "/assets/logo-512.png"
INDEXNOW_KEY = "523ef9e7a671a55d7f695ae2f374abab"
# Artykuły bloga do bloku „Powiązane artykuły” (url, tytuł, opis) – wypełniane w build.py
ARTICLES = []
# Które artykuły pasują do której strony (kolejność = trafność); brak wpisu = wszystkie
ARTICLE_MAP = {}

TOOLS = [
    ("/", "Walidator numeru KSeF", "Walidator numeru", "Sprawdź numer KSeF (CRC-8, NIP, data) i ułóż tytuł przelewu."),
    ("/przelew-mpp-numer-ksef/", "Komunikat przelewu MPP", "Przelew MPP", "Generator /VAT/ /IDC/ /INV/ /TXT/ z numerem KSeF dla split payment."),
    ("/identyfikator-zbiorczy-ksef/", "Identyfikator zbiorczy", "Identyfikator zbiorczy", "Sprawdź identyfikator zbiorczy KSeF i rozłóż go na części."),
    ("/sprawdz-wiele-numerow-ksef/", "Wiele numerów naraz", "Wiele numerów", "Lista, plik CSV lub wyciąg bankowy – wyniki do pobrania w CSV."),
    ("/przelew-z-faktury-xml-ksef/", "Przelew z faktury XML", "Faktura XML", "Wczytaj fakturę FA(3) i skopiuj rachunek, kwotę, tytuł i komunikat MPP."),
    ("/kod-qr-ksef/", "Kod QR KSeF", "Kod QR", "Wygeneruj KOD I z pliku XML albo sprawdź link z kodu QR na fakturze."),
    ("/ksef-od-2027-jdg/", "KSeF dla JDG od 2027", "KSeF dla JDG", "Odpowiedz na kilka pytań i zobacz, co zmienia się 1 stycznia 2027 r."),
]
OTHER = [
    ("/blog/", "Blog – poradniki KSeF"),
    ("/o-serwisie/", "O serwisie"),
    ("/kontakt/", "Kontakt"),
    ("/regulamin/", "Regulamin"),
    ("/polityka-prywatnosci/", "Polityka prywatności"),
]
GSV = '<meta name="google-site-verification" content="elPNThwVdT6P4PDIZnIkvzQFaVe5GeQ3MDhBJpephcI" />'
THEME_INIT = ('<script>(function(){try{var t=localStorage.getItem("theme");if(t!=="light"&&t!=="dark")'
              '{t=window.matchMedia&&matchMedia("(prefers-color-scheme: dark)").matches?"dark":"light"}'
              'document.documentElement.setAttribute("data-theme",t)}catch(e){}})();</script>')
THEME_BTN = ('<button class="theme-toggle" type="button" aria-pressed="false" aria-label="Tryb ciemny" title="Przełącz tryb jasny / ciemny">'
             '<svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><circle cx="12" cy="12" r="9" fill="none" stroke="currentColor" stroke-width="2"/>'
             '<path d="M12 3a9 9 0 0 1 0 18z" fill="currentColor"/></svg></button>')

LOGO = ('<svg viewBox="0 0 32 32" aria-hidden="true" focusable="false"><rect width="32" height="32" rx="8" fill="#1747c9"/>'
        '<path d="M9 9h3v6.2L17.6 9h3.7l-6 6.6L21.6 23h-3.8l-4.6-5.4-1.2 1.3V23H9z" fill="#fff"/>'
        '<circle cx="24.5" cy="24.5" r="4.5" fill="#22c55e" stroke="#fff" stroke-width="1.5"/>'
        '<path d="M22.4 24.6l1.4 1.4 2.7-2.8" fill="none" stroke="#fff" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg>')

PRIVACY_NOTE = "Dane nie opuszczają Twojej przeglądarki."


INLINE_CSS = ""  # ustawiane w build.py (zminifikowany style.css wstawiany inline – brak żądania blokującego renderowanie)


def csp_hash(text):
    return "'sha256-%s'" % base64.b64encode(hashlib.sha256(text.encode("utf-8")).digest()).decode()


def csp_meta():
    theme_js = THEME_INIT[len("<script>"):-len("</script>")]
    pol = ("default-src 'self'; script-src 'self' %s; style-src 'self' %s; img-src 'self' data:; "
           "object-src 'none'; base-uri 'self'; form-action 'self'") % (csp_hash(theme_js), csp_hash(INLINE_CSS))
    return '<meta http-equiv="Content-Security-Policy" content="%s">' % pol


def e(s):
    return html.escape(s, quote=True)


def header(path):
    items = "".join(
        '<li><a href="%s"%s>%s</a></li>' % (u, ' aria-current="page"' if u == path else "", e(short))
        for (u, _l, short, _d) in TOOLS)
    items += '<li><a href="/blog/"%s>Blog</a></li>' % (' aria-current="page"' if path.startswith("/blog/") else "")
    return (
        '<a class="skip" href="#tresc">Przejdź do treści</a>'
        '<header class="site-head"><div class="wrap">'
        '<a class="brand" href="/" aria-label="%s – strona główna">%s<span>%s<small>darmowe narzędzia KSeF</small></span></a>'
        '<button class="nav-toggle" type="button" aria-expanded="false" aria-controls="site-nav">Menu</button>'
        '<nav id="site-nav" class="site-nav" aria-label="Narzędzia"><ul>%s</ul></nav>%s'
        '</div></header>') % (BRAND, LOGO, BRAND, items, THEME_BTN)


def footer():
    tools = "".join('<li><a href="%s">%s</a></li>' % (u, e(l)) for (u, l, _s, _d) in TOOLS)
    other = "".join('<li><a href="%s">%s</a></li>' % (u, e(l)) for (u, l) in OTHER)
    return (
        '<footer class="site-foot"><div class="wrap"><div class="foot-grid">'
        '<div><h2>%s</h2><p>Bezpłatne narzędzia do numerów KSeF, przelewów i faktur ustrukturyzowanych. '
        'Bez reklam, bez rejestracji. Wszystkie obliczenia wykonuje Twoja przeglądarka – %s</p>'
        '<p>Serwis niezależny, niezwiązany z Ministerstwem Finansów. Treści mają charakter informacyjny i nie stanowią porady podatkowej.</p></div>'
        '<div><h2>Narzędzia</h2><ul>%s</ul></div>'
        '<div><h2>Serwis i źródła</h2><ul>%s'
        '<li><a href="https://ksef.podatki.gov.pl/" rel="noopener" target="_blank">ksef.podatki.gov.pl (MF)</a></li>'
        '<li><a href="https://github.com/CIRFMF/ksef-docs" rel="noopener" target="_blank">Dokumentacja KSeF 2.0 (MF, GitHub)</a></li>'
        '<li><a href="/sitemap.xml">Mapa strony</a></li></ul></div>'
        '</div><p class="foot-note">© 2026 %s · Ostatnia aktualizacja: %s r. · Kod działa bez serwera, bez ciasteczek i bez śledzenia.</p></div></footer>'
        '<p id="live" class="sr-only" aria-live="polite"></p>'
    ) % (SITE, PRIVACY_NOTE, tools, other, BRAND, UPDATED_PL)


def crumbs_html(trail):
    lis = []
    for i, (name, url) in enumerate(trail):
        if i == len(trail) - 1:
            lis.append('<li aria-current="page">%s</li>' % e(name))
        else:
            lis.append('<li><a href="%s">%s</a></li>' % (url, e(name)))
    return '<nav class="crumbs" aria-label="Okruszki"><ol>%s</ol></nav>' % "".join(lis)


def faq_html(faq):
    return '<div class="faq">' + "".join(
        '<details><summary>%s</summary><p>%s</p></details>' % (e(q), a) for q, a in faq) + "</div>"


def strip_tags(s):
    import re
    return html.unescape(re.sub(r"<[^>]+>", "", s))


def org_ref():
    return {"@type": "Organization", "@id": DOMAIN + "/#organization", "name": BRAND, "url": DOMAIN + "/",
            "logo": {"@type": "ImageObject", "url": DOMAIN + LOGO_PNG, "width": 512, "height": 512}}


def jsonld(page, path):
    url = DOMAIN + path
    graph = []
    if page.get("app", True):
        graph.append({
            "@type": "WebApplication",
            "name": page["app_name"],
            "url": url,
            "description": page["desc"],
            "applicationCategory": "FinanceApplication",
            "operatingSystem": "Dowolny (przeglądarka internetowa)",
            "browserRequirements": "Wymaga JavaScript",
            "inLanguage": "pl-PL",
            "isAccessibleForFree": True,
            "offers": {"@type": "Offer", "price": "0", "priceCurrency": "PLN"},
            "dateModified": UPDATED_ISO,
            "image": DOMAIN + OG_IMAGE,
            "publisher": org_ref(),
        })
    else:
        graph.append({"@type": "WebPage", "name": page["title"], "url": url, "description": page["desc"],
                      "inLanguage": "pl-PL", "dateModified": UPDATED_ISO})
    if path == "/":
        graph.append({"@type": "Organization", "@id": DOMAIN + "/#organization", "name": BRAND,
                      "alternateName": SITE, "url": DOMAIN + "/",
                      "logo": {"@type": "ImageObject", "url": DOMAIN + LOGO_PNG, "width": 512, "height": 512},
                      "description": "Niezależny serwis z darmowymi narzędziami do numerów KSeF, przelewów i faktur ustrukturyzowanych. Niezwiązany z Ministerstwem Finansów."})
        graph.append({"@type": "WebSite", "@id": DOMAIN + "/#website", "name": SITE, "alternateName": BRAND,
                      "url": DOMAIN + "/", "inLanguage": "pl-PL", "publisher": {"@id": DOMAIN + "/#organization"}})
    if page.get("article"):
        org = org_ref()
        graph.append({"@type": "Article", "headline": page["h1"], "description": page["desc"], "url": url,
                      "mainEntityOfPage": url, "inLanguage": "pl-PL", "datePublished": UPDATED_ISO,
                      "dateModified": UPDATED_ISO, "author": org, "publisher": org,
                      "isAccessibleForFree": True, "image": DOMAIN + OG_IMAGE})
    if page.get("faq"):
        graph.append({"@type": "FAQPage", "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": strip_tags(a)}}
            for q, a in page["faq"]]})
    graph.append({"@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": i + 1, "name": n, "item": DOMAIN + u}
        for i, (n, u) in enumerate(page["trail"])]})
    return json.dumps({"@context": "https://schema.org", "@graph": graph}, ensure_ascii=False, indent=1)


def related(path):
    cards = "".join('<a href="%s"><strong>%s</strong><span>%s</span></a>' % (u, e(l), e(d))
                    for (u, l, _s, d) in TOOLS if u != path)
    return '<h2 id="inne-narzedzia">Inne darmowe narzędzia KSeF</h2><div class="hub">%s</div>' % cards


def related_articles(path):
    order = ARTICLE_MAP.get(path) or [u for (u, _t, _d) in ARTICLES]
    by = {u: (u, t, d) for (u, t, d) in ARTICLES}
    items = [by[u] for u in order if u in by and u != path][:3]
    if not items:
        return ""
    cards = "".join('<a href="%s"><strong>%s</strong><span>%s</span></a>' % (u, e(t), e(d)) for (u, t, d) in items)
    return '<h2 id="powiazane-artykuly">Powiązane artykuły</h2><div class="hub">%s</div>' % cards


def sources_html(src):
    return '<h2 id="zrodla">Źródła</h2><ul class="sources">' + "".join(
        '<li><a href="%s" rel="noopener" target="_blank">%s</a>%s</li>' % (u, e(t), (" – " + n) if n else "")
        for (t, u, n) in src) + "</ul>"


def render(page, path):
    title = page["title"]
    desc = page["desc"]
    url = DOMAIN + path
    scripts = "".join('<script src="/assets/%s?v=%s" defer></script>' % (s, ASSET_V) for s in page.get("scripts", []))
    robots = '<meta name="robots" content="noindex">' if page.get("noindex") else '<meta name="robots" content="index,follow,max-image-preview:large">'
    body_parts = []
    body_parts.append(crumbs_html(page["trail"]) if len(page["trail"]) > 1 else "")
    body_parts.append('<div class="hero"><h1>%s</h1><p class="lead">%s</p>' % (e(page["h1"]), page["intro"]))
    if page.get("trust", True):
        body_parts.append('<ul class="trust"><li>Za darmo, bez rejestracji</li><li>%s</li><li>Bez reklam i śledzenia</li></ul>' % PRIVACY_NOTE)
    body_parts.append("</div>")
    body_parts.append(page.get("tool", ""))
    content = page.get("content", "")
    if page.get("faq"):
        content += '<h2 id="faq">Najczęstsze pytania</h2>' + faq_html(page["faq"])
    if page.get("sources"):
        content += sources_html(page["sources"])
    if page.get("related", True):
        content += related(path)
        content += related_articles(path)
    content += '<p class="updated">Ostatnia aktualizacja: <time datetime="%s">%s r.</time> · %s</p>' % (UPDATED_ISO, UPDATED_PL, PRIVACY_NOTE)
    body_parts.append('<article class="content">%s</article>' % content)
    og_title = page.get("og_title", title)
    return """<!doctype html>
<html lang="pl">
<head>
<meta charset="utf-8">{gsv}
{csp}
<meta name="referrer" content="strict-origin-when-cross-origin">
<meta name="viewport" content="width=device-width, initial-scale=1">
{theme}
<title>{title}</title>
<meta name="description" content="{desc}">
{robots}
<link rel="canonical" href="{url}">
<link rel="alternate" hreflang="pl" href="{url}">
<link rel="alternate" hreflang="x-default" href="{url}">
<meta name="theme-color" content="#1747c9">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="{logo}">
<link rel="manifest" href="/site.webmanifest">
<meta property="og:type" content="{ogtype}">
<meta property="og:locale" content="pl_PL">
<meta property="og:site_name" content="{site}">
<meta property="og:title" content="{ogt}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{ogimg}">
<meta property="og:image:type" content="image/png">
<meta property="og:image:width" content="{ogw}">
<meta property="og:image:height" content="{ogh}">
<meta property="og:image:alt" content="NumerKSeF – sprawdź numer KSeF i przygotuj tytuł przelewu">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{ogt}">
<meta name="twitter:description" content="{desc}">
<meta name="twitter:image" content="{ogimg}">
<style>{css}</style>
<script type="application/ld+json">
{ld}
</script>
</head>
<body>
{header}
<main id="tresc" class="wrap" tabindex="-1">
{body}
</main>
{footer}
<script src="/assets/core.js?v={v}" defer></script>
<script src="/assets/ui.js?v={v}" defer></script>
{scripts}
</body>
</html>
""".format(gsv=("\n" + GSV) if path == "/" else "", theme=THEME_INIT, ogtype="article" if page.get("article") else "website", title=e(title), desc=e(desc), csp=csp_meta(), css=INLINE_CSS, ogimg=DOMAIN + OG_IMAGE, ogw=OG_W, ogh=OG_H, logo=LOGO_PNG, robots=robots, url=url, site=e(SITE), ogt=e(og_title), v=ASSET_V,
           ld=jsonld(page, path).replace("</", "<\\/"), header=header(path), body="\n".join(body_parts), footer=footer(),
           scripts=scripts)
