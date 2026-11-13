# QA NumerKSeF v2 – 2026-11-13

```
CRC-8 / numer KSeF
  ✓ crc8 przykładu MF = AF
  ✓ przykład MF 5265877635-20250826-0100001AF629-AF przechodzi
  ✓ zmieniona suma …-7C jest odrzucona
  ✓ inne przykłady MF/przelewyksef przechodzą
  ✓ przykład mBank (ilustracyjny) jest odrzucony – CRC 3A, zły NIP
  ✓ normalizacja: spacje, małe litery, długi myślnik
  ✓ litera O zamiast zera – wskazówka z pozycją
  ✓ zła długość
  ✓ 36 znaków (KSeF 1.0) = ostrzeżenie, nie błąd
  ✓ prefiks inny niż NIP (M + 9 cyfr) = ostrzeżenie
  ✓ data z przyszłości = błąd
  ✓ nieistniejąca data (30 lutego) = błąd
Identyfikator zbiorczy
  ✓ przykład MF 1111111111-IZ202607-65ED02180000-E7 przechodzi
  ✓ checkKsef automatycznie rozpoznaje IZ
  ✓ IZ ze zmienioną sumą jest odrzucony
  ✓ IZ z miesiącem 13 jest odrzucony
NIP
  ✓ NIP 5265877635 poprawny
  ✓ NIP 1111111111 poprawny
  ✓ NIP 5265877636 błędny
  ✓ NIP z myślnikami i PL – checkNip
  ✓ NIP 3786417439 (mBank) błędny
Tytuł przelewu
  ✓ 3 numery + opis mieszczą się w 140
  ✓ 4 numery = ostrzeżenie
Komunikat MPP
  ✓ przykład: jedna faktura – dokładny wynik i długość
  ✓ formuła długości 5+len(VAT)+5+len(NIP)+5+35(+5+len(TXT))
  ✓ identyfikator zbiorczy w /INV/
  ✓ VAT > brutto = błąd
  ✓ VAT 0,00 = błąd
  ✓ zabronione znaki w /TXT/
  ✓ /TXT/ dłuższy niż 33 = błąd
  ✓ błędny numer KSeF w /INV/ = błąd
  ✓ błędny NIP = błąd
  ✓ przekazanie własne
  ✓ numer faktury zamiast KSeF w 2027 = ostrzeżenie (ok)
  ✓ parseAmount: formaty
FA(3) XML
  ✓ parsowanie przykładowej faktury FA(3)
  ✓ przykładowy XML z prefiksem przestrzeni nazw (ns:) też działa
  ✓ DoZaplaty ma pierwszeństwo przed P_15
  ✓ FA(2) – ostrzeżenie, dane odczytane
  ✓ nie-faktura (UPO) – błąd
  ✓ numer KSeF z nazwy pliku
  ✓ komunikat MPP z faktury: VAT 3739,84, NIP, numer KSeF, P_2 w TXT
Wyszukiwanie w tekście
  ✓ findCandidates w tytułach i komunikacie MPP
  ✓ CSV z BOM i średnikiem
KOD I / linki QR
  ✓ przykład MF KOD I jest poprawny (TE, ostrzeżenie o braku skutków)
  ✓ skrót przykładu MF dekoduje się do 32 bajtów
  ✓ fałszywa domena = phishing
  ✓ http zamiast https = błąd
  ✓ KOD II jest rozpoznawany
  ✓ KOD I z pliku: SHA-256 Base64URL (WebCrypto) + budowa linku
Ankieta JDG
  ✓ czynny VAT, B2B, limit, płaci, MPP – pełna lista + kary w toku
  ✓ zwolniony z VAT – numer KSeF w przelewie dobrowolny

Wynik: 52 zaliczonych, 0 niezaliczonych
Pliki i linki wewnętrzne (10 stron HTML)
  ✓ /404.html – linki wewnętrzne istnieją
  ✓ /404.html – kotwice #id istnieją
  ✓ /404.html – JSON-LD parsuje się (WebApplication/WebPage + BreadcrumbList)
  ✓ /404.html – meta: title, description, canonical, OG, jedno H1, lang=pl
  ✓ /404.html – dostępność: etykiety pól, alt/aria, brak zewnętrznych skryptów
  ✓ /identyfikator-zbiorczy-ksef/ – linki wewnętrzne istnieją
  ✓ /identyfikator-zbiorczy-ksef/ – kotwice #id istnieją
  ✓ /identyfikator-zbiorczy-ksef/ – JSON-LD parsuje się (WebApplication/WebPage + BreadcrumbList)
  ✓ /identyfikator-zbiorczy-ksef/ – meta: title, description, canonical, OG, jedno H1, lang=pl
  ✓ /identyfikator-zbiorczy-ksef/ – dostępność: etykiety pól, alt/aria, brak zewnętrznych skryptów
      (poradnik: 621 słów, FAQ: 6)
  ✓ /identyfikator-zbiorczy-ksef/ – treść: 600–1000 słów, FAQ 5–8 (narzędzia), źródła, data aktualizacji, nota o prywatności
  ✓ / – linki wewnętrzne istnieją
  ✓ / – kotwice #id istnieją
  ✓ / – JSON-LD parsuje się (WebApplication/WebPage + BreadcrumbList)
  ✓ / – meta: title, description, canonical, OG, jedno H1, lang=pl
  ✓ / – dostępność: etykiety pól, alt/aria, brak zewnętrznych skryptów
      (poradnik: 630 słów, FAQ: 7)
  ✓ / – treść: 600–1000 słów, FAQ 5–8 (narzędzia), źródła, data aktualizacji, nota o prywatności
  ✓ /kod-qr-ksef/ – linki wewnętrzne istnieją
  ✓ /kod-qr-ksef/ – kotwice #id istnieją
  ✓ /kod-qr-ksef/ – JSON-LD parsuje się (WebApplication/WebPage + BreadcrumbList)
  ✓ /kod-qr-ksef/ – meta: title, description, canonical, OG, jedno H1, lang=pl
  ✓ /kod-qr-ksef/ – dostępność: etykiety pól, alt/aria, brak zewnętrznych skryptów
      (poradnik: 620 słów, FAQ: 6)
  ✓ /kod-qr-ksef/ – treść: 600–1000 słów, FAQ 5–8 (narzędzia), źródła, data aktualizacji, nota o prywatności
  ✓ /ksef-od-2027-jdg/ – linki wewnętrzne istnieją
  ✓ /ksef-od-2027-jdg/ – kotwice #id istnieją
  ✓ /ksef-od-2027-jdg/ – JSON-LD parsuje się (WebApplication/WebPage + BreadcrumbList)
  ✓ /ksef-od-2027-jdg/ – meta: title, description, canonical, OG, jedno H1, lang=pl
  ✓ /ksef-od-2027-jdg/ – dostępność: etykiety pól, alt/aria, brak zewnętrznych skryptów
      (poradnik: 615 słów, FAQ: 6)
  ✓ /ksef-od-2027-jdg/ – treść: 600–1000 słów, FAQ 5–8 (narzędzia), źródła, data aktualizacji, nota o prywatności
  ✓ /o-serwisie/ – linki wewnętrzne istnieją
  ✓ /o-serwisie/ – kotwice #id istnieją
  ✓ /o-serwisie/ – JSON-LD parsuje się (WebApplication/WebPage + BreadcrumbList)
  ✓ /o-serwisie/ – meta: title, description, canonical, OG, jedno H1, lang=pl
  ✓ /o-serwisie/ – dostępność: etykiety pól, alt/aria, brak zewnętrznych skryptów
      (poradnik: 211 słów, FAQ: 3)
  ✓ /o-serwisie/ – treść: 600–1000 słów, FAQ 5–8 (narzędzia), źródła, data aktualizacji, nota o prywatności
  ✓ /polityka-prywatnosci/ – linki wewnętrzne istnieją
  ✓ /polityka-prywatnosci/ – kotwice #id istnieją
  ✓ /polityka-prywatnosci/ – JSON-LD parsuje się (WebApplication/WebPage + BreadcrumbList)
  ✓ /polityka-prywatnosci/ – meta: title, description, canonical, OG, jedno H1, lang=pl
  ✓ /polityka-prywatnosci/ – dostępność: etykiety pól, alt/aria, brak zewnętrznych skryptów
  ✓ /przelew-mpp-numer-ksef/ – linki wewnętrzne istnieją
  ✓ /przelew-mpp-numer-ksef/ – kotwice #id istnieją
  ✓ /przelew-mpp-numer-ksef/ – JSON-LD parsuje się (WebApplication/WebPage + BreadcrumbList)
  ✓ /przelew-mpp-numer-ksef/ – meta: title, description, canonical, OG, jedno H1, lang=pl
  ✓ /przelew-mpp-numer-ksef/ – dostępność: etykiety pól, alt/aria, brak zewnętrznych skryptów
      (poradnik: 626 słów, FAQ: 7)
  ✓ /przelew-mpp-numer-ksef/ – treść: 600–1000 słów, FAQ 5–8 (narzędzia), źródła, data aktualizacji, nota o prywatności
  ✓ /przelew-z-faktury-xml-ksef/ – linki wewnętrzne istnieją
  ✓ /przelew-z-faktury-xml-ksef/ – kotwice #id istnieją
  ✓ /przelew-z-faktury-xml-ksef/ – JSON-LD parsuje się (WebApplication/WebPage + BreadcrumbList)
  ✓ /przelew-z-faktury-xml-ksef/ – meta: title, description, canonical, OG, jedno H1, lang=pl
  ✓ /przelew-z-faktury-xml-ksef/ – dostępność: etykiety pól, alt/aria, brak zewnętrznych skryptów
      (poradnik: 601 słów, FAQ: 6)
  ✓ /przelew-z-faktury-xml-ksef/ – treść: 600–1000 słów, FAQ 5–8 (narzędzia), źródła, data aktualizacji, nota o prywatności
  ✓ /sprawdz-wiele-numerow-ksef/ – linki wewnętrzne istnieją
  ✓ /sprawdz-wiele-numerow-ksef/ – kotwice #id istnieją
  ✓ /sprawdz-wiele-numerow-ksef/ – JSON-LD parsuje się (WebApplication/WebPage + BreadcrumbList)
  ✓ /sprawdz-wiele-numerow-ksef/ – meta: title, description, canonical, OG, jedno H1, lang=pl
  ✓ /sprawdz-wiele-numerow-ksef/ – dostępność: etykiety pól, alt/aria, brak zewnętrznych skryptów
      (poradnik: 622 słów, FAQ: 6)
  ✓ /sprawdz-wiele-numerow-ksef/ – treść: 600–1000 słów, FAQ 5–8 (narzędzia), źródła, data aktualizacji, nota o prywatności
  ✓ sitemap: 9 URL, lastmod 2026-11-13; robots wskazuje sitemap; manifest JSON; CNAME
Smoke-testy interfejsu (jsdom)
  ✓ / – Przykład → zielony status, tytuł z 2 numerami
  ✓ /przelew-mpp-numer-ksef/ – przykłady i parametry z adresu
  ✓ /identyfikator-zbiorczy-ksef/ – przykład MF zielony, numer KSeF rozpoznany
  ✓ /sprawdz-wiele-numerow-ksef/ – lista, wyciąg, CSV
  ✓ /przelew-z-faktury-xml-ksef/ – przykład: karta płatności z MPP
  ✓ /kod-qr-ksef/ – dekoder (MF, phishing) i generator z pliku
  ✓ /ksef-od-2027-jdg/ – ankieta zwraca listę z karą w toku

Wynik: 66 zaliczonych, 0 niezaliczonych
```

QR decode (zxing-cpp):
decoded OK https://qr.ksef.mf.gov.pl/invoice/5265877635/12-11-2026/RgmpPq84l8R6XG5wOujbz70mWfWPSO_KNdKUujPwMLI M

FA(3) sample vs official XSD:
../site-v2/assets/przyklad-fa3.xml VALID

# QA NumerKSeF v3 – 2026-11-13 (commit 3f6985c)
- test-site.js: 116 zaliczonych, 0 niezaliczonych (log: qa/test-site-v3.log)
- test-core.js: 52 zaliczonych, 0 niezaliczonych (log: qa/test-core-v3.log)
- Nowe sprawdzenia: canonical = adres strony, description < 160 znaków, stopka z Kontakt/Regulamin/Prywatność/O serwisie/Blog, przełącznik motywu, brak "2028", unikalne pytania FAQ w całym serwisie, Article JSON-LD + 900–1200 słów na wpisach blogu, poradniki narzędzi 1000–1250 słów z tabelą i przykładem.
- Live (curl po ~75 s): wszystkie nowe i zmienione strony 200, nieistniejący adres 404.

# QA SEO + wydajność + CSP – 2026-11-13
- test-core.js: 52/52 (na zminifikowanym core.js)
- test-site.js: 179/179 (nowe: hreflang, OG/Twitter, JSON-LD Organization/WebSite/WebApplication, powiązane artykuły, plik IndexNow, tytuły wg autocomplete, CSS inline, CSP z hashami, referrer, brak style=/eval, minifikacja)
- test-browser-csp.js (Chromium/Playwright, CSP egzekwowany): 61/61 – 16 stron bez błędów JS i naruszeń CSP; wszystkie 7 narzędzi działa (przykłady, fetch XML, generator QR SVG, eksport CSV przez blob), przełącznik motywu działa.
  Uruchomienie: NODE_PATH=/tmp/pw/node_modules LD_LIBRARY_PATH=/tmp/debs/x/usr/lib/aarch64-linux-gnu node qa/test-browser-csp.js
- Czytelne źródła JS/CSS: build/assets-src/; minifikacja: build/tools/minify.js (terser + csso), wywoływana przez build/build.py.
