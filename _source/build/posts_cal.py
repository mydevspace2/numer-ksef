# -*- coding: utf-8 -*-
# Posty z kalendarza (work/seo/blog-calendar.md). Każdy: slug, title (<=60), desc (70–159), h1, intro, lead_tool,
# date (ISO, PL), content (HTML), faq [(q, a)], sources. Dopisuj nowe na końcu listy CAL_POSTS.
from sources import MF_NUM, MF_TERM, DOC_NUM, XSD, MF_QR, APP, MF_FA3
from sources import MF_NUM, MF_TERM, DOC_NUM, XSD, MF_QR, APP, MF_FA3, MBANK_SPEC, MBANK_IMPORT, MBANK_NEWS, DB, IZ_PDF, IZ_PDF2
# ---------------------------------------------------------------- #1 (2026-11-14)
C01 = dict(
    slug="jak-wyglada-numer-ksef-przyklad",
    title="Jak wygląda numer KSeF? Przykład i budowa numeru",
    desc="Jak wygląda numer KSeF: oficjalny przykład MF, wzór 35 znaków, gdzie go zobaczysz na PDF, w UPO i w nazwie pliku oraz czym różni się od podobnych numerów.",
    h1="Jak wygląda numer KSeF – przykład, wzór i podobne numery",
    intro="Numer KSeF łatwo pomylić z numerem faktury, NIP-em albo identyfikatorem zbiorczym. Pokazujemy, jak wygląda prawdziwy numer i po czym go rozpoznać w kilka sekund.",
    lead_tool=("/", "walidator numeru KSeF"),
    date=("2026-11-14", "14 listopada 2026"),
    content="""
<h2 id="przyklad">Oficjalny przykład numeru KSeF</h2>
<p>Ministerstwo Finansów w dokumentacji KSeF 2.0 podaje taki przykład numeru:</p>
<p class="mono">5265877635-20250826-0100001AF629-AF</p>
<p>Według dokumentacji numer KSeF <q>zawsze ma długość 35 znaków</q> i jest nadawany przez system – wystawca nie wybiera go sam. Ogólny wzór wygląda tak: <code>9999999999-RRRRMMDD-FFFFFFFFFFFF-FF</code>. Widać w nim cztery bloki rozdzielone trzema myślnikami:</p>
<div class="table-wrap"><table>
<thead><tr><th scope="col">Blok</th><th scope="col">Przykład</th><th scope="col">Co oznacza</th><th scope="col">Znaki</th></tr></thead>
<tbody>
<tr><th scope="row">1</th><td class="mono">5265877635</td><td>NIP sprzedawcy</td><td>10 cyfr</td></tr>
<tr><th scope="row">2</th><td class="mono">20250826</td><td>data przyjęcia faktury do KSeF (RRRRMMDD)</td><td>8 cyfr</td></tr>
<tr><th scope="row">3</th><td class="mono">0100001AF629</td><td>część techniczna (zapis szesnastkowy)</td><td>12 znaków 0–9, A–F</td></tr>
<tr><th scope="row">4</th><td class="mono">AF</td><td>suma kontrolna CRC-8</td><td>2 znaki 0–9, A–F</td></tr>
</tbody></table></div>
<p>Szczegółowy rozkład znak po znaku opisujemy w artykule <a href="/blog/z-czego-sklada-sie-numer-ksef/">z czego składa się numer KSeF</a>. Tutaj skupiamy się na tym, jak numer rozpoznać w praktyce.</p>

<h2 id="cechy">Pięć cech, po których rozpoznasz numer KSeF</h2>
<ol class="steps">
<li><strong>35 znaków razem z myślnikami.</strong> Ani więcej, ani mniej. Jeśli ciąg ma 36 znaków i dodatkowy myślnik w części technicznej, to stary format z KSeF 1.0.</li>
<li><strong>Na początku 10 cyfr.</strong> Zwykle to NIP sprzedawcy, więc zgadza się z NIP-em z nagłówka faktury.</li>
<li><strong>Potem 8 cyfr daty.</strong> Rok zaczyna się od 20, miesiąc ma wartość 01–12. To data przyjęcia przez KSeF, nie data wystawienia.</li>
<li><strong>Tylko wielkie litery A–F.</strong> Część techniczna i suma kontrolna to zapis szesnastkowy. Litera G, O czy Z oznacza literówkę.</li>
<li><strong>Brak spacji i ukośników.</strong> Numer faktury nadany przez sprzedawcę często ma ukośniki (FV/12/2026); numer KSeF – nigdy.</li>
</ol>
<p>Wszystkie te cechy, a do tego sumę kontrolną, sprawdza automatycznie nasz <a href="/">walidator numeru KSeF</a>. Wystarczy wkleić numer.</p>

<h2 id="podobne">Numery, które wyglądają podobnie</h2>
<p>Na fakturze, w KSeF i w przelewie pojawia się kilka różnych identyfikatorów. Tak je odróżnisz:</p>
<div class="table-wrap"><table>
<thead><tr><th scope="col">Identyfikator</th><th scope="col">Przykład</th><th scope="col">Jak odróżnić</th></tr></thead>
<tbody>
<tr><th scope="row">Numer KSeF</th><td class="mono">5265877635-20250826-0100001AF629-AF</td><td>35 znaków, środkowa część to pełna data</td></tr>
<tr><th scope="row">Identyfikator zbiorczy</th><td class="mono">1111111111-IZ202607-65ED02180000-E7</td><td>35 znaków, ale w środku litery IZ i tylko rok z miesiącem</td></tr>
<tr><th scope="row">Numer KSeF 1.0</th><td>36 znaków</td><td>dodatkowy myślnik dzielący część techniczną na dwie po 6 znaków</td></tr>
<tr><th scope="row">Numer faktury</th><td class="mono">FV/12/11/2026</td><td>nadaje sprzedawca, dowolny format, pole P_2 w XML</td></tr>
<tr><th scope="row">NIP</th><td class="mono">5265877635</td><td>tylko 10 cyfr – to dopiero początek numeru KSeF</td></tr>
</tbody></table></div>
<p>Identyfikator zbiorczy omawiamy osobno w artykule <a href="/blog/identyfikator-zbiorczy-ksef-co-to-jest/">identyfikator zbiorczy KSeF – co to jest</a>.</p>

<h2 id="gdzie-widac">Jak numer KSeF wygląda na dokumentach</h2>
<h3>W UPO</h3>
<p>Wystawca po wysłaniu faktury dostaje urzędowe poświadczenie odbioru. MF podaje, że numer KSeF jest zwracany w UPO – zobaczysz tam dokładnie ten 35-znakowy ciąg.</p>
<h3>Na wizualizacji PDF</h3>
<p>Faktura przekazana poza KSeF, np. mailem jako PDF, ma kod QR (KOD I). Pod kodem umieszcza się numer KSeF. Jeśli faktura w chwili tworzenia PDF-u nie miała jeszcze numeru, pod kodem widnieje napis OFFLINE. Sam link w kodzie QR to inny ciąg – możesz go sprawdzić w narzędziu <a href="/kod-qr-ksef/">kod QR KSeF</a>.</p>
<h3>W nazwie pliku XML</h3>
<p>W treści pliku XML faktury numeru KSeF nie ma – według MF nie jest on elementem pliku. Pliki pobierane z KSeF i z programów księgowych często mają go jednak w nazwie, np. <code>5265877635-20250826-0100001AF629-AF.xml</code>.</p>
<h3>W tytule przelewu</h3>
<p>Od 1 stycznia 2027 r. numer KSeF trafi też do tytułów przelewów między czynnymi podatnikami VAT. Najlepiej, gdy stoi na samym początku tytułu – wtedy nie zostanie obcięty.</p>

<h2 id="przyklad-praktyczny">Przykład: który ciąg na fakturze to numer KSeF?</h2>
<p>Pani Ewa dostała PDF faktury, na której widzi trzy ciągi znaków: <code>FV/0457/11/2026</code> w nagłówku, <code>9510001233</code> przy danych sprzedawcy i <code>9510001233-20261102-01A3F0C2B7D4-B8</code> pod kodem QR w rogu strony.</p>
<ul>
<li>Pierwszy ma ukośniki i dowolny format – to numer faktury nadany przez sprzedawcę.</li>
<li>Drugi ma 10 cyfr – to NIP sprzedawcy.</li>
<li>Trzeci ma 35 znaków, zaczyna się od tego samego NIP-u, ma datę 2 listopada 2026 r. i kończy się sumą kontrolną B8 – to numer KSeF.</li>
</ul>
<p>Pani Ewa wkleja trzeci ciąg do walidatora. Ten potwierdza długość, NIP, datę i sumę kontrolną, a potem od razu układa tytuł przelewu. Jak go poprawnie zapisać, opisujemy w poradniku <a href="/blog/jak-wpisac-numer-ksef-w-tytule-przelewu/">jak wpisać numer KSeF w tytule przelewu</a>.</p>

<h2 id="mpp">Jak numer KSeF wygląda w przelewie MPP</h2>
<p>W mechanizmie podzielonej płatności numer KSeF nie stoi na początku tytułu, tylko w polu <code>/INV/</code> komunikatu. Pole to ma dokładnie 35 znaków, czyli tyle, ile numer KSeF albo identyfikator zbiorczy. Przykładowy komunikat wygląda tak:</p>
<p class="mono">/VAT/230,00/IDC/5265877635/INV/5265877635-20250826-0100001AF629-AF</p>
<p>Widać tu ten sam NIP dwa razy: raz w polu <code>/IDC/</code> (NIP sprzedawcy), raz jako początek numeru KSeF. Gotowy komunikat ułożysz w <a href="/przelew-mpp-numer-ksef/">generatorze komunikatu przelewu MPP</a>, który pilnuje formatu każdego pola.</p>

<h2 id="pulapki">Na co uważać</h2>
<ul>
<li><strong>Przykłady z instrukcji banków i programów</strong> bywają ilustracyjne i nie mają poprawnej sumy kontrolnej. Nie traktuj ich jako wzoru do kopiowania.</li>
<li><strong>Zero i litera O</strong> wyglądają w wielu czcionkach podobnie. W numerze KSeF litery O nie ma nigdy, więc zawsze chodzi o zero.</li>
<li><strong>Kopiowanie z PDF-u</strong> czasem dokleja spację lub zamienia myślnik na półpauzę. Walidator naprawia takie drobiazgi i informuje o tym.</li>
<li><strong>Numer na fakturze zakupowej</strong> zaczyna się od NIP-u sprzedawcy, a nie Twojego.</li>
</ul>

<h2 id="podsumowanie">Podsumowanie</h2>
<p>Numer KSeF to zawsze 35 znaków w czterech blokach: NIP, data przyjęcia, 12 znaków technicznych i 2 znaki sumy kontrolnej. Znajdziesz go w UPO, pod kodem QR na PDF-ie i w nazwie pliku XML, ale nie w samej treści XML. Masz wątpliwość, czy dany ciąg to numer KSeF? Wklej go do <a href="/">walidatora numeru KSeF</a> – odpowiedź dostaniesz od razu, a dane nie opuszczą Twojej przeglądarki.</p>
""",
    faq=[
        ("Czy numer KSeF może zawierać małe litery?", "Nie. Według dokumentacji MF część techniczna i suma kontrolna zawierają tylko cyfry 0–9 i wielkie litery A–F. Walidator zamieni małe litery na wielkie i poinformuje o tym."),
        ("Gdzie na fakturze PDF jest numer KSeF?", "Pod kodem QR (KOD I), zwykle w rogu wizualizacji. Gdy faktura nie miała jeszcze numeru w chwili tworzenia PDF-u, w tym miejscu jest napis OFFLINE."),
        ("Czy numer KSeF zawsze zaczyna się od NIP-u sprzedawcy?", "Zwykle tak. Schemat FA(3) dopuszcza też inne identyfikatory na początku numeru (np. litera M i 9 cyfr albo 3 litery i 7 cyfr), a przy samofakturowaniu może to być NIP nabywcy."),
        ("Jak na pierwszy rzut oka odróżnić numer KSeF od identyfikatora zbiorczego?", "Oba mają 35 znaków, ale identyfikator zbiorczy ma w drugim bloku litery IZ i tylko rok z miesiącem, np. IZ202607. Numer KSeF ma tam pełną datę RRRRMMDD."),
    ],
    sources=[DOC_NUM, MF_NUM, MF_QR, XSD],
)

# ---------------------------------------------------------------- #2 (2026-11-14)
C02 = dict(
    slug="z-czego-sklada-sie-numer-ksef",
    title="Z czego składa się numer KSeF? 35 znaków krok po kroku",
    desc="Z czego składa się numer KSeF: NIP, data przyjęcia, 12 znaków technicznych i suma CRC-8. Rozkład 35 znaków pozycja po pozycji, z przykładem MF i tabelą.",
    h1="Z czego składa się numer KSeF – 35 znaków pozycja po pozycji",
    intro="Każdy z 35 znaków numeru KSeF ma swoje miejsce i znaczenie. Rozkładamy oficjalny przykład MF na części i pokazujemy, co z nich można odczytać, a czego nie.",
    lead_tool=("/", "rozłóż numer KSeF na części"),
    date=("2026-11-14", "14 listopada 2026"),
    content="""
<h2 id="wzor">Wzór numeru według MF</h2>
<p>Dokumentacja KSeF 2.0 Ministerstwa Finansów opisuje numer jako <code>9999999999-RRRRMMDD-FFFFFFFFFFFF-FF</code>. Ma on zawsze 35 znaków: 32 znaki danych, myślnik i 2 znaki sumy kontrolnej. Weźmy oficjalny przykład <code>5265877635-20250826-0100001AF629-AF</code> i rozłóżmy go na pozycje.</p>

<h2 id="pozycje">Rozkład pozycja po pozycji</h2>
<div class="table-wrap"><table>
<thead><tr><th scope="col">Pozycje</th><th scope="col">Przykład</th><th scope="col">Element</th><th scope="col">Dozwolone znaki</th></tr></thead>
<tbody>
<tr><th scope="row">1–10</th><td class="mono">5265877635</td><td>NIP sprzedawcy</td><td>cyfry 0–9</td></tr>
<tr><th scope="row">11</th><td class="mono">-</td><td>separator</td><td>myślnik</td></tr>
<tr><th scope="row">12–15</th><td class="mono">2025</td><td>rok przyjęcia</td><td>cyfry</td></tr>
<tr><th scope="row">16–17</th><td class="mono">08</td><td>miesiąc przyjęcia</td><td>01–12</td></tr>
<tr><th scope="row">18–19</th><td class="mono">26</td><td>dzień przyjęcia</td><td>01–31 (zgodnie z kalendarzem)</td></tr>
<tr><th scope="row">20</th><td class="mono">-</td><td>separator</td><td>myślnik</td></tr>
<tr><th scope="row">21–32</th><td class="mono">0100001AF629</td><td>część techniczna</td><td>0–9 i wielkie A–F</td></tr>
<tr><th scope="row">33</th><td class="mono">-</td><td>separator</td><td>myślnik</td></tr>
<tr><th scope="row">34–35</th><td class="mono">AF</td><td>suma kontrolna CRC-8</td><td>0–9 i wielkie A–F</td></tr>
</tbody></table></div>
<p>Pozycje warto znać, bo nasz <a href="/">walidator numeru KSeF</a> przy błędzie formatu wskazuje numer znaku, który nie pasuje do wzoru. Dzięki tabeli od razu wiesz, w którym bloku szukać pomyłki.</p>

<h2 id="nip">Pozycje 1–10: NIP sprzedawcy</h2>
<p>Pierwsze 10 cyfr to zazwyczaj NIP podmiotu, który wystawił fakturę. NIP ma własną cyfrę kontrolną – dziesiątą – liczoną z dziewięciu poprzednich. Dlatego walidator sprawdza ten blok dwa razy: czy to 10 cyfr i czy cyfra kontrolna NIP się zgadza.</p>
<p>Są wyjątki. Schemat FA(3) dopuszcza na początku numeru także identyfikatory w postaci litery M i 9 cyfr albo 3 liter i 7 cyfr. Przy samofakturowaniu numer może zaczynać się od NIP-u nabywcy, a przy przedstawicielu podatkowym – od NIP-u przedstawiciela. Gdy początek nie jest NIP-em, walidator nie zgłasza błędu, tylko ostrzeżenie.</p>

<h2 id="data">Pozycje 12–19: data przyjęcia do KSeF</h2>
<p>Osiem cyfr w formacie RRRRMMDD to – według MF – data przyjęcia faktury do dalszego przetwarzania. To ważne rozróżnienie:</p>
<ul>
<li>data w numerze KSeF <strong>nie musi</strong> być równa dacie wystawienia z pola P_1,</li>
<li>przy fakturach offline data w numerze jest datą przesłania do KSeF, która może być późniejsza niż data wystawienia,</li>
<li>data nie może być z przyszłości – numer z jutrzejszą datą to na pewno literówka.</li>
</ul>
<p>KSeF 2.0 działa produkcyjnie od 1 lutego 2026 r., więc numery z wcześniejszymi datami pochodzą z okresu dobrowolnego (KSeF 1.0) albo są przykładowe. Oficjalny przykład MF ma datę 26 sierpnia 2025 r. – walidator oznaczy to jako uwagę, nie błąd.</p>

<h2 id="techniczna">Pozycje 21–32: część techniczna</h2>
<p>Dwanaście znaków szesnastkowych (0–9, A–F) generuje system. MF nie publikuje ich znaczenia, dlatego nie da się z nich nic odczytać – i nie ma takiej potrzeby. W praktyce liczy się jedno: to w tym bloku najczęściej zdarzają się literówki, bo ciąg cyfr i liter jest trudny do przepisania. Litera O zamiast zera albo I zamiast jedynki od razu łamie format, bo O i I nie należą do zapisu szesnastkowego.</p>
<p>W starych numerach z KSeF 1.0 ten blok był podzielony dodatkowym myślnikiem na dwie części po 6 znaków. Stąd 36 znaków zamiast 35. Schemat FA(3) wciąż akceptuje taki zapis, np. w polu numeru faktury korygowanej.</p>

<h2 id="crc">Pozycje 34–35: suma kontrolna CRC-8</h2>
<p>Ostatnie dwa znaki to suma kontrolna liczona algorytmem CRC-8 z 32 pierwszych znaków (razem z myślnikami). MF podaje parametry: wielomian <code>0x07</code>, wartość początkowa <code>0x00</code>, wynik zapisany jako dwa znaki szesnastkowe wielkimi literami. Dla przykładu MF wynik to <code>AF</code>.</p>
<p>Suma kontrolna wychwytuje praktycznie każdą pojedynczą pomyłkę. Przykład: gdyby ktoś przepisał datę jako <code>20250827</code> zamiast <code>20250826</code>, poprawna suma dla takich danych wyniosłaby <code>4A</code>, a nie <code>AF</code> – walidator od razu pokaże niezgodność. Więcej o samej weryfikacji przeczytasz w artykule <a href="/blog/jak-sprawdzic-czy-numer-ksef-jest-poprawny/">jak sprawdzić, czy numer KSeF jest poprawny</a>.</p>

<h2 id="przyklad-zakup">Przykład: odczytujemy numer z faktury zakupowej</h2>
<p>Księgowa biura rachunkowego dostaje od klienta numer <code>9510001233-20261102-01A3F0C2B7D4-B8</code> i chce szybko ocenić, czego dotyczy. Rozkłada go według tabeli:</p>
<ul>
<li><strong>9510001233</strong> – NIP sprzedawcy; porównuje go z kartoteką kontrahentów i od razu wie, od kogo jest faktura,</li>
<li><strong>20261102</strong> – faktura trafiła do KSeF 2 listopada 2026 r., więc powinna być w zestawieniu zakupów za listopad, jeśli data wystawienia też przypada w tym miesiącu,</li>
<li><strong>01A3F0C2B7D4</strong> – część techniczna, której nie interpretuje,</li>
<li><strong>B8</strong> – suma kontrolna; walidator potwierdza, że zgadza się z danymi.</li>
</ul>
<p>Dzięki temu bez otwierania KSeF wie, od którego dostawcy pochodzi faktura i kiedy została przyjęta. Szczegóły – kwotę, rachunek i termin – i tak sprawdzi w samej fakturze. Jeśli takich numerów ma kilkadziesiąt, wkleja całą listę do narzędzia <a href="/sprawdz-wiele-numerow-ksef/">sprawdź wiele numerów KSeF</a>, które pokazuje NIP i datę z każdego numeru w osobnych kolumnach.</p>

<p>Ta sama wiedza przydaje się sprzedawcy: gdy w tytule wpłaty pojawi się numer KSeF, pierwsze 10 cyfr powinno być jego własnym NIP-em. Jeśli jest inaczej, klient prawdopodobnie wkleił numer faktury od innego dostawcy i warto to wyjaśnić, zanim wpłata zostanie rozliczona.</p>

<h2 id="co-odczytasz">Co możesz odczytać z numeru, a czego nie</h2>
<div class="table-wrap"><table>
<thead><tr><th scope="col">Odczytasz</th><th scope="col">Nie odczytasz</th></tr></thead>
<tbody>
<tr><td>NIP wystawcy (zwykle)</td><td>numeru faktury nadanego przez sprzedawcę</td></tr>
<tr><td>dzień przyjęcia faktury do KSeF</td><td>daty wystawienia i terminu płatności</td></tr>
<tr><td>czy numer nie ma literówki (CRC-8)</td><td>kwoty faktury i danych nabywcy</td></tr>
<tr><td>czy to stary format 36 znaków</td><td>czy faktura faktycznie istnieje w KSeF</td></tr>
</tbody></table></div>
<p>Kwotę, rachunek i termin płatności odczytasz dopiero z samej faktury. Jeśli masz jej plik XML, skorzystaj z narzędzia <a href="/przelew-z-faktury-xml-ksef/">przelew z faktury XML KSeF</a>.</p>

<h2 id="podsumowanie">Podsumowanie</h2>
<p>Numer KSeF składa się z czterech bloków: NIP (10 cyfr), daty przyjęcia (8 cyfr), części technicznej (12 znaków szesnastkowych) i sumy kontrolnej CRC-8 (2 znaki), rozdzielonych myślnikami. Znając pozycje, szybko znajdziesz literówkę. A najszybciej zrobi to za Ciebie <a href="/">walidator numeru KSeF</a>, który rozkłada numer na części i sprawdza każdą z nich.</p>
""",
    faq=[
        ("Co oznacza data w numerze KSeF?", "To data przyjęcia faktury przez KSeF do dalszego przetwarzania. Może różnić się od daty wystawienia, zwłaszcza przy fakturach wystawionych offline."),
        ("Czy część techniczna numeru KSeF coś oznacza?", "MF opisuje ją tylko jako 12 znaków technicznych w zapisie szesnastkowym. Jej wewnętrzne znaczenie nie jest publikowane i nie jest potrzebne do płatności ani weryfikacji."),
        ("Czy myślniki są częścią numeru KSeF?", "Tak. Trzy myślniki wliczają się do 35 znaków i do danych, z których liczy się suma kontrolna. Numer bez myślników jest niepoprawny."),
        ("Dlaczego numer KSeF może zaczynać się od litery?", "Schemat FA(3) dopuszcza na początku numeru identyfikatory inne niż NIP: literę M i 9 cyfr albo 3 litery i 7 cyfr. To rzadkie przypadki – w typowej fakturze krajowej jest tam NIP."),
    ],
    sources=[DOC_NUM, MF_NUM, XSD, MF_TERM],
)

# ---------------------------------------------------------------- #3 (2026-11-14)
C03 = dict(
    slug="jak-sprawdzic-czy-numer-ksef-jest-poprawny",
    title="Jak sprawdzić, czy numer KSeF jest poprawny?",
    desc="Jak sprawdzić, czy numer KSeF jest poprawny: 4 kroki walidacji wg MF, suma kontrolna CRC-8, typowe błędy z przykładami i różnica: poprawny a istniejący.",
    h1="Jak sprawdzić, czy numer KSeF jest poprawny – 4 kroki i przykłady",
    intro="Pomyłka w jednym z 35 znaków sprawi, że sprzedawca nie dopasuje przelewu do faktury. Pokazujemy, jak sprawdzić numer KSeF według dokumentacji MF – ręcznie i automatycznie.",
    lead_tool=("/", "sprawdź numer KSeF online"),
    date=("2026-11-14", "14 listopada 2026"),
    content="""
<h2 id="kroki">Cztery kroki walidacji według MF</h2>
<p>Dokumentacja KSeF 2.0 Ministerstwa Finansów opisuje walidację numeru w czterech krokach:</p>
<ol class="steps">
<li>sprawdzenie, czy numer ma <strong>dokładnie 35 znaków</strong>,</li>
<li>rozdzielenie <strong>części danych (32 znaki)</strong> i <strong>sumy kontrolnej (2 znaki)</strong>,</li>
<li>obliczenie sumy kontrolnej z części danych <strong>algorytmem CRC-8</strong>,</li>
<li>porównanie obliczonej sumy z dwoma ostatnimi znakami numeru.</li>
</ol>
<p>Nasz <a href="/">walidator numeru KSeF</a> wykonuje te kroki, a dodatkowo sprawdza cyfrę kontrolną NIP-u na początku numeru i to, czy data jest prawdziwą datą kalendarzową, która nie leży w przyszłości. Wszystko dzieje się w przeglądarce – numer nie jest nigdzie wysyłany.</p>

<h2 id="crc8">Jak działa suma kontrolna CRC-8</h2>
<p>CRC-8 to krótki algorytm, który z 32 znaków danych (razem z myślnikami) wylicza jedną liczbę od 0 do 255, zapisaną jako dwa znaki szesnastkowe. MF podaje parametry: wielomian <code>0x07</code>, wartość początkowa <code>0x00</code>, wynik wielkimi literami. Obliczenie ręczne jest żmudne, ale dla programu to ułamek sekundy. Twórcy oprogramowania znajdą gotowe walidatory w oficjalnych bibliotekach MF dla C# i Javy.</p>
<p>Najważniejsza właściwość: zmiana nawet jednego znaku w danych prawie zawsze zmienia sumę kontrolną. Dlatego literówka w numerze zwykle kończy się komunikatem „suma kontrolna się nie zgadza”.</p>

<h2 id="przyklady">Przykłady: numer poprawny i z błędami</h2>
<p>Wszystkie przykłady bazują na oficjalnym numerze z dokumentacji MF. Sumy kontrolne policzyliśmy algorytmem opisanym przez MF.</p>
<div class="table-wrap"><table>
<thead><tr><th scope="col">Numer</th><th scope="col">Wynik</th><th scope="col">Dlaczego</th></tr></thead>
<tbody>
<tr><td class="mono">5265877635-20250826-0100001AF629-AF</td><td>poprawny</td><td>35 znaków, obliczona suma AF = podana AF</td></tr>
<tr><td class="mono">5265877635-20250827-0100001AF629-AF</td><td>błąd sumy</td><td>zmieniony dzień daty; dla tych danych suma wynosi 4A</td></tr>
<tr><td class="mono">5265877635-20250826-0100001AF629-FA</td><td>błąd sumy</td><td>zamienione dwa ostatnie znaki</td></tr>
<tr><td class="mono">5265877635-20250826-01000O1AF629-AF</td><td>błąd formatu</td><td>litera O na pozycji 26 – w zapisie szesnastkowym jej nie ma</td></tr>
<tr><td class="mono">5265877635-20250826-0100001AF629</td><td>zła długość</td><td>brak sumy kontrolnej – tylko 32 znaki</td></tr>
<tr><td class="mono">5265877636-20250826-0100001AF629-AF</td><td>błąd NIP i sumy</td><td>zmieniona ostatnia cyfra NIP-u</td></tr>
</tbody></table></div>
<p>Zwróć uwagę na drugi i trzeci wiersz: na oko wyglądają poprawnie. Bez sprawdzenia sumy kontrolnej takiej pomyłki nie zauważysz.</p>

<h2 id="krok-po-kroku">Jak sprawdzić numer w walidatorze</h2>
<ol class="steps">
<li>Skopiuj numer z UPO, programu księgowego albo spod kodu QR na fakturze. Nie przepisuj go ręcznie.</li>
<li>Wklej go do pola na stronie <a href="/">walidatora numeru KSeF</a>. Wynik pojawi się od razu.</li>
<li>Przeczytaj komunikat. Zielony wynik oznacza poprawny format, NIP, datę i sumę. Przy błędzie narzędzie wskazuje pozycję znaku i podpowiada najczęstszą przyczynę.</li>
<li>Porównaj NIP z początku numeru z NIP-em sprzedawcy na fakturze.</li>
<li>Skopiuj gotowy tytuł przelewu przyciskiem „Kopiuj”.</li>
</ol>
<p>Masz wiele numerów, np. z listy faktur do zapłaty albo z wyciągu bankowego? Użyj narzędzia <a href="/sprawdz-wiele-numerow-ksef/">sprawdź wiele numerów KSeF</a> – wklejasz listę lub plik CSV, a dostajesz wynik dla każdego wiersza i plik do pobrania.</p>

<h2 id="reczne">Czy da się sprawdzić numer bez narzędzia?</h2>
<p>Część kontroli zrobisz wzrokiem: policz znaki (35), sprawdź trzy myślniki, porównaj pierwsze 10 cyfr z NIP-em sprzedawcy i upewnij się, że data ma sens. W części technicznej i sumie kontrolnej szukaj liter spoza zakresu A–F. Tego, czy zgadza się suma kontrolna, ręcznie praktycznie nie sprawdzisz – do tego potrzebny jest program. Dlatego kontrola wzrokowa wyłapie tylko część błędów, a walidator wszystkie, które da się wykryć bez dostępu do KSeF.</p>

<h2 id="poprawny-a-istniejacy">Poprawny to nie to samo co istniejący</h2>
<p>Walidator potwierdza, że numer jest <strong>zbudowany poprawnie</strong>. Nie potwierdza, że faktura o takim numerze istnieje w KSeF ani że to właśnie ta faktura, którą płacisz. To dwie różne rzeczy:</p>
<div class="table-wrap"><table>
<thead><tr><th scope="col">Pytanie</th><th scope="col">Gdzie sprawdzisz</th></tr></thead>
<tbody>
<tr><td>Czy w numerze nie ma literówki?</td><td>walidator (format, NIP, data, CRC-8)</td></tr>
<tr><td>Czy faktura jest w KSeF?</td><td>KSeF, np. Aplikacja Podatnika, albo link z kodu QR na wizualizacji</td></tr>
<tr><td>Czy numer należy do tej faktury?</td><td>porównanie z UPO, programem księgowym lub danymi z KSeF</td></tr>
</tbody></table></div>
<p>Jeśli masz PDF z kodem QR, sprawdź link w narzędziu <a href="/kod-qr-ksef/">kod QR KSeF</a>: pokaże, czy prowadzi do oficjalnej domeny MF, i ostrzeże przed podróbką.</p>

<h2 id="kiedy">Kiedy warto sprawdzać numer KSeF</h2>
<p>Sprawdzenie zajmuje sekundę, więc warto je robić w kilku typowych momentach:</p>
<div class="table-wrap"><table>
<thead><tr><th scope="col">Moment</th><th scope="col">Kto</th><th scope="col">Po co</th></tr></thead>
<tbody>
<tr><td>przed wysłaniem przelewu</td><td>nabywca</td><td>żeby sprzedawca mógł dopasować wpłatę do faktury</td></tr>
<tr><td>przy imporcie listy płatności do banku</td><td>księgowość</td><td>żeby jeden błędny numer nie trafił do kilkudziesięciu przelewów</td></tr>
<tr><td>przy rozliczaniu wpłat z wyciągu</td><td>sprzedawca</td><td>żeby odróżnić literówkę klienta od wpłaty za inną fakturę</td></tr>
<tr><td>przy korekcie lub fakturze końcowej</td><td>wystawca</td><td>bo w XML podaje się numer KSeF faktury pierwotnej lub zaliczkowej</td></tr>
</tbody></table></div>
<p>Ostatni przypadek łatwo przeoczyć: schemat FA(3) ma osobne pola na numer KSeF faktury korygowanej i faktury zaliczkowej. Pomyłka w takim polu nie zablokuje płatności, ale utrudni powiązanie dokumentów w KSeF. Sprzedawca, który dostaje wiele wpłat dziennie, najszybciej sprawdzi tytuły z wyciągu w trybie „wyciąg” narzędzia do wielu numerów – narzędzie samo wyszuka numer KSeF w środku dłuższego tytułu.</p>

<h2 id="najczestsze">Najczęstsze przyczyny błędów</h2>
<ul>
<li><strong>Przepisywanie zamiast kopiowania</strong> – O zamiast 0, I zamiast 1, B zamiast 8.</li>
<li><strong>Ucięty numer</strong> – przy kopiowaniu z wąskiej kolumny Excela lub PDF-u gubi się suma kontrolna.</li>
<li><strong>Dodatkowe znaki</strong> – kropka lub przecinek na końcu, spacja w środku, półpauza zamiast myślnika. Walidator usuwa je i informuje o poprawce.</li>
<li><strong>Numer z instrukcji</strong> – przykłady w materiałach banków i programów bywają zmyślone i nie przechodzą kontroli.</li>
<li><strong>Stary format</strong> – 36 znaków to numer z KSeF 1.0; walidator rozpozna go i oznaczy ostrzeżeniem.</li>
</ul>

<h2 id="podsumowanie">Podsumowanie</h2>
<p>Poprawność numeru KSeF sprawdzisz w czterech krokach opisanych przez MF: długość, podział, obliczenie CRC-8 i porównanie sumy. Ręcznie to żmudne, automatycznie trwa sekundę. Wklej numer do <a href="/">walidatora numeru KSeF</a>, zanim wyślesz przelew – a istnienie faktury potwierdź w KSeF.</p>
""",
    faq=[
        ("Czy poprawna suma kontrolna oznacza, że faktura istnieje w KSeF?", "Nie. Suma kontrolna potwierdza tylko, że numer jest zbudowany poprawnie. Istnienie faktury sprawdzisz w KSeF, np. w Aplikacji Podatnika, albo przez link z kodu QR na wizualizacji."),
        ("Jak sprawdzić naraz numery KSeF z listy faktur w Excelu?", "Skopiuj kolumnę z numerami albo zapisz arkusz jako CSV i wklej go do narzędzia „Sprawdź wiele numerów KSeF”. Każdy wiersz dostanie osobny wynik, który pobierzesz jako CSV."),
        ("Co zrobić, gdy walidator pokazuje błąd daty?", "Sprawdź, czy data w drugim bloku istnieje w kalendarzu i nie jest z przyszłości. Taki błąd to prawie zawsze literówka – skopiuj numer ponownie ze źródła, np. z UPO."),
        ("Czy walidator numeru KSeF działa bez internetu?", "Po wczytaniu strony obliczenia wykonuje przeglądarka, więc numer nie jest wysyłany na żaden serwer. Do samego otwarcia strony potrzebne jest połączenie."),
    ],
    sources=[DOC_NUM, MF_NUM, MF_QR, APP],
)


# ---------------------------------------------------------------- #4 (2026-11-15)
C04 = dict(
    slug="numer-ksef-w-przelewie-mpp",
    title="Numer KSeF w przelewie MPP – gdzie go wpisać?",
    desc="Numer KSeF w przelewie MPP (split payment): gdzie go wpisać, jak wygląda komunikat /VAT/ /IDC/ /INV/ /TXT/, limity znaków i przykład z dokumentacji banku.",
    h1="Numer KSeF w przelewie MPP – gdzie go wpisać i jak wygląda komunikat",
    intro="W przelewie podzielonym numer KSeF trafia do komunikatu MPP, a nie do zwykłego tytułu. Pokazujemy układ pól, limity znaków i przykład, który możesz porównać ze swoim przelewem.",
    lead_tool=("/przelew-mpp-numer-ksef/", "generator komunikatu MPP z numerem KSeF"),
    date=("2026-11-15", "15 listopada 2026"),
    content="""
<h2 id="zasada">Co mówi Ministerstwo Finansów</h2>
<p>Według strony MF o numerze KSeF i identyfikatorze zbiorczym w komunikacie przelewu MPP podaje się między innymi numer KSeF faktury. Jeśli płacisz za kilka faktur, zamiast okresu wpisuje się identyfikator zbiorczy. Szczegóły techniczne – kolejność i długość pól – zależą od banku, bo komunikat MPP ma ściśle określony format.</p>
<p>Najprościej złożysz go w <a href="/przelew-mpp-numer-ksef/">generatorze komunikatu MPP</a>: wpisujesz numer KSeF, NIP sprzedawcy i kwotę VAT, a narzędzie sprawdza długości i znaki. Poniżej wyjaśniamy, co dokładnie dostajesz.</p>

<h2 id="slowa-kodowe">Słowa kodowe komunikatu MPP</h2>
<p>Specyfikacja mBank dla importu płatności (pain.001) opisuje komunikat MPP jako ciąg słów kodowych w ustalonej kolejności. Każde może wystąpić tylko raz, a między słowem kodowym a znakiem nie ma spacji.</p>
<div class="table-wrap"><table>
<thead><tr><th scope="col">Słowo</th><th scope="col">Co zawiera</th><th scope="col">Limit</th><th scope="col">Wymagane</th></tr></thead>
<tbody>
<tr><td>/VAT/</td><td>kwota VAT z przecinkiem, np. 23,00</td><td>większa od 0 i nie większa niż kwota płatności</td><td>tak</td></tr>
<tr><td>/IDC/</td><td>identyfikator dostawcy (NIP sprzedawcy)</td><td>14 znaków</td><td>tak</td></tr>
<tr><td>/INV/</td><td>numer faktury lub numer KSeF</td><td>35 znaków</td><td>tak</td></tr>
<tr><td>/TXT/</td><td>dowolny opis płatności</td><td>33 znaki</td><td>nie</td></tr>
</tbody></table></div>
<p>Całość mieści się w polu o długości 140 znaków. Numer KSeF ma dokładnie 35 znaków, więc wypełnia pole /INV/ w całości. Własny numer faktury sprzedawcy zmieścisz co najwyżej w opcjonalnym /TXT/.</p>

<h2 id="przyklad">Przykład komunikatu krok po kroku</h2>
<p>Przykład z dokumentacji mBank (numery w specyfikacji są przykładowe):</p>
<p><code>/VAT/23035,90/IDC/3786417439/INV/3786417439-20260928-AB12CD34EF56-78/TXT/dowolny tekst</code></p>
<div class="table-wrap"><table>
<thead><tr><th scope="col">Fragment</th><th scope="col">Znaczenie</th><th scope="col">Znaków</th></tr></thead>
<tbody>
<tr><td>/VAT/23035,90</td><td>VAT 23 035,90 zł</td><td>13</td></tr>
<tr><td>/IDC/3786417439</td><td>NIP sprzedawcy</td><td>15</td></tr>
<tr><td>/INV/ + numer KSeF</td><td>35 znaków numeru</td><td>40</td></tr>
<tr><td>/TXT/dowolny tekst</td><td>opcjonalny opis</td><td>18</td></tr>
</tbody></table></div>
<p>Razem 86 znaków, czyli mieści się w limicie 140. Liczenie jest proste: 5 znaków na każde słowo kodowe plus długość wartości. Przy dłuższej kwocie VAT i opisie 33 znaki w /TXT/ nadal się zmieszczą.</p>

<h2 id="formularz">Jak to wygląda w formularzu banku</h2>
<p>Banki wdrażają zmiany w różnym tempie. Deutsche Bank opisuje formularz z czterema liniami: /VAT/, /IDC/, /INV/ i opcjonalnie /TXT/ jako ostatnią. mBank zapowiedział w komunikacie dla klientów firmowych zmiany w przelewach podzielonych, m.in. możliwość wpisania numeru faktury KSeF w polu numeru faktury. Zanim wyślesz pierwszą większą płatność, sprawdź w swoim banku, jak wygląda formularz, i zrób jeden przelew testowy.</p>
<ol class="steps">
<li>Otwórz fakturę i odczytaj numer KSeF (patrz <a href="/blog/jak-wyglada-numer-ksef-przyklad/">jak wygląda numer KSeF</a>).</li>
<li>Sprawdź numer w <a href="/">walidatorze numeru KSeF</a>, żeby wykluczyć literówkę.</li>
<li>Wpisz kwotę VAT z faktury, z przecinkiem jako separatorem.</li>
<li>Jako /IDC/ podaj NIP sprzedawcy, czyli pierwsze 10 cyfr numeru KSeF.</li>
<li>Wklej numer KSeF do pola /INV/ i zapisz przelew.</li>
</ol>

<h2 id="znaki">Dozwolone i zakazane znaki</h2>
<p>Specyfikacja mBank dopuszcza w szczegółach płatności cyfry, litery, polskie znaki oraz znaki &amp; % ( ) - { } / , . Niedozwolone są m.in. dwukropek, gwiazdka, średnik, apostrof, cudzysłów, wykrzyknik, plus, znak zapytania, pionowa kreska i hash. Numer KSeF zawiera tylko cyfry, litery i myślniki, więc nie sprawia problemu. Kłopot pojawia się w polu /TXT/, jeśli skopiujesz do niego opis z faktury ze znakami specjalnymi.</p>

<h2 id="kilka-faktur">Kilka faktur w jednym przelewie MPP</h2>
<p>Gdy płacisz za wiele faktur tego samego sprzedawcy, w /INV/ może stać identyfikator zbiorczy zamiast pojedynczego numeru. Specyfikacja mBank podaje taki przykład: <code>/INV/3786417439-IZ202708-AB12CD34EF56-78</code>. Jak go wygenerować, opisuje strona o <a href="/identyfikator-zbiorczy-ksef/">identyfikatorze zbiorczym KSeF</a>.</p>

<h2 id="bledy">Najczęstsze błędy w komunikacie MPP</h2>
<p>Komunikat MPP jest bardziej restrykcyjny niż zwykły tytuł przelewu. Bank może odrzucić przelew albo nie zaksięgować go jako płatności podzielnej, jeśli format się nie zgadza. Poniżej błędy, które najłatwiej popełnić przy ręcznym wpisywaniu.</p>
<div class="table-wrap"><table>
<thead><tr><th scope="col">Błąd</th><th scope="col">Dlaczego to problem</th><th scope="col">Jak poprawić</th></tr></thead>
<tbody>
<tr><td>kropka zamiast przecinka w kwocie VAT</td><td>specyfikacja wymaga przecinka jako separatora</td><td>wpisz 230,00, nie 230.00</td></tr>
<tr><td>VAT większy niż kwota płatności</td><td>pole /VAT/ musi być większe od 0 i nie większe niż kwota</td><td>sprawdź kwotę VAT na fakturze</td></tr>
<tr><td>spacja po słowie kodowym</td><td>spacje między słowem kodowym a znakiem są niedozwolone</td><td>pisz /INV/numer bez spacji</td></tr>
<tr><td>zmiana kolejności słów</td><td>kolejność VAT, IDC, INV, TXT jest obowiązkowa</td><td>trzymaj się układu z przykładu</td></tr>
<tr><td>dwukropek lub średnik w opisie</td><td>to znaki niedozwolone w szczegółach płatności</td><td>usuń je albo zastąp myślnikiem</td></tr>
<tr><td>obcięty numer KSeF</td><td>pole /INV/ przyjmuje do 35 znaków, numer ma dokładnie 35</td><td>kopiuj cały numer, nie przepisuj</td></tr>
</tbody></table></div>
<p>Nie ma jednej gwarancji, że każdy bank przyjmie komunikat tak samo. Specyfikacje opisują konkretne produkty (np. import płatności w mBank), a formularze w bankowości internetowej mogą mieć osobne pola zamiast jednego ciągu. Jeśli formularz ma osobne pola, wpisz w nie te same wartości, które widzisz w komunikacie: kwotę VAT, NIP i numer KSeF.</p>
<h2 id="przekazanie-wlasne">Przekazanie własne między rachunkami VAT</h2>
<p>Specyfikacja mBank przewiduje też wariant dla przelewów między rachunkami VAT tego samego klienta. W polu /INV/ wpisuje się wtedy tekst PRZEKAZANIE WLASNE, a w polu /IDC/ własny identyfikator klienta. Kwota VAT jest wtedy równa kwocie płatności. Ten wariant nie dotyczy płatności za fakturę sprzedawcy, więc numeru KSeF w nim nie ma. Jeśli rozliczasz fakturę sprzedawcy, zawsze używaj pełnego komunikatu z numerem KSeF albo identyfikatorem zbiorczym.</p>
<p>Przed wysłaniem policz długość całego komunikatu i upewnij się, że nie przekracza 140 znaków. Generator robi to automatycznie.</p>
<p>Pamiętaj też, że kwota VAT w komunikacie to kwota z faktury, a nie wyliczona z głowy. Gdy faktura ma kilka stawek, sumujesz VAT ze wszystkich pozycji, które opłacasz tym przelewem. Dla pewności porównaj sumę z polem P_15 i podatkiem na wizualizacji faktury.</p>
<h2 id="podsumowanie">Podsumowanie</h2>
<p>W przelewie MPP numer KSeF wpisujesz w pole /INV/, NIP sprzedawcy w /IDC/, a kwotę VAT w /VAT/. Pilnuj przecinka, limitu 140 znaków i zakazanych znaków. Gotowy komunikat złożysz w <a href="/przelew-mpp-numer-ksef/">generatorze komunikatu MPP</a>, a przed wysłaniem sprawdź w swoim banku aktualny formularz.</p>
""",
    faq=[
        ("Czy w przelewie MPP numer KSeF zastępuje numer faktury?", "Według specyfikacji mBank pole /INV/ przyjmuje numer faktury albo numer (identyfikator) KSeF. Przy fakturze z KSeF wpisujesz więc numer KSeF."),
        ("Ile znaków może mieć komunikat przelewu MPP?", "Według specyfikacji mBank komunikat mieści się w polu o długości 140 znaków, z czego /TXT/ ma maksymalnie 33 znaki, a /INV/ 35."),
        ("Co wpisać w /IDC/ przy płatności za fakturę z KSeF?", "Identyfikator dostawcy, czyli NIP sprzedawcy. To te same 10 cyfr, od których zaczyna się numer KSeF faktury."),
        ("Czy mogę wpisać własny numer faktury razem z numerem KSeF?", "Pole /INV/ jest w całości zajęte przez 35 znaków numeru KSeF. Własny numer faktury możesz dopisać w opcjonalnym polu /TXT/, jeśli zmieści się w 33 znakach."),
    ],
    sources=[MF_NUM, MF_TERM, MBANK_SPEC, MBANK_IMPORT, MBANK_NEWS, DB],
)

# ---------------------------------------------------------------- #5 (2026-11-15)
C05 = dict(
    slug="czy-numer-ksef-to-numer-faktury",
    title="Czy numer KSeF to numer faktury? Różnice",
    desc="Czy numer KSeF to numer faktury? Nie – to dwa różne numery. Sprawdź, kto je nadaje, gdzie występują w XML i PDF oraz który wpisać w tytule przelewu.",
    h1="Czy numer KSeF to numer faktury? Wyjaśniamy różnice",
    intro="Na fakturze z KSeF możesz zobaczyć dwa numery i łatwo je pomylić. Wyjaśniamy, który jest który, kto go nadaje i który podać w przelewie.",
    lead_tool=("/", "walidator numeru KSeF"),
    date=("2026-11-15", "15 listopada 2026"),
    content="""
<h2 id="krotko">Krótka odpowiedź</h2>
<p>Nie. <strong>Numer faktury</strong> nadaje wystawca według własnego schematu, np. FV/11/2026/15. <strong>Numer KSeF</strong> nadaje system KSeF po przyjęciu faktury. Ma stałą budowę i 35 znaków. Poprawność drugiego sprawdzisz w <a href="/">walidatorze numeru KSeF</a>.</p>

<h2 id="porownanie">Porównanie obu numerów</h2>
<div class="table-wrap"><table>
<thead><tr><th scope="col">Cecha</th><th scope="col">Numer faktury</th><th scope="col">Numer KSeF</th></tr></thead>
<tbody>
<tr><td>Kto nadaje</td><td>wystawca faktury</td><td>system KSeF</td></tr>
<tr><td>Kiedy powstaje</td><td>przy wystawianiu faktury</td><td>po przyjęciu faktury przez KSeF</td></tr>
<tr><td>Format</td><td>dowolny, ustalony przez wystawcę</td><td>35 znaków: NIP, data, część techniczna, suma kontrolna</td></tr>
<tr><td>Pole w XML FA(3)</td><td>P_2</td><td>nie jest w pliku faktury (nadawany po przyjęciu)</td></tr>
<tr><td>Unikalność</td><td>w obrębie wystawcy</td><td>w całym systemie</td></tr>
</tbody></table></div>
<p>Plik XML faktury zawiera numer P_2, ale nie zawiera numeru KSeF, bo ten powstaje dopiero po wysłaniu pliku do systemu. Dlatego numer KSeF znajdziesz w UPO, w Aplikacji Podatnika, na wizualizacji PDF oraz w danych pobranych z KSeF. Więcej o miejscach, w których go zobaczysz, jest w poście <a href="/blog/gdzie-znalezc-numer-ksef-faktury/">gdzie znaleźć numer KSeF faktury</a>.</p>

<h2 id="przyklad">Przykład: jedna faktura, dwa numery</h2>
<p>Sprzedawca z NIP 1234567890 wystawia fakturę o numerze FV/11/2026/15. Po przyjęciu jej system nadaje numer w rodzaju 1234567890-20261115-XXXXXXXXXXXX-YY, gdzie litery zastępują część techniczną i sumę kontrolną. Na PDF obok siebie pojawią się:</p>
<div class="table-wrap"><table>
<thead><tr><th scope="col">Pozycja na PDF</th><th scope="col">Wartość</th></tr></thead>
<tbody>
<tr><td>Numer faktury</td><td>FV/11/2026/15</td></tr>
<tr><td>Numer KSeF</td><td>1234567890-20261115-… (35 znaków)</td></tr>
</tbody></table></div>
<p>To przykład ilustracyjny – nie jest prawdziwym numerem. Pierwsze 10 cyfr numeru KSeF to NIP sprzedawcy, a kolejne 8 to data w formacie RRRRMMDD. Budowę opisujemy w poście <a href="/blog/z-czego-sklada-sie-numer-ksef/">z czego składa się numer KSeF</a>.</p>

<h2 id="przelew">Który numer wpisać w przelewie</h2>
<p>MF wskazuje, że przy płatności za pojedynczą fakturę podaje się numer KSeF faktury, a przy płatności za więcej faktur – identyfikator zbiorczy albo kilka numerów KSeF, z uwzględnieniem ograniczeń pola tytułu. Własny numer faktury możesz dopisać obok, jeśli starczy miejsca. Pole tytułu ma zwykle 140 znaków, więc numer KSeF (35) i numer faktury zwykle się zmieszczą. Gotowy tytuł zbudujesz w <a href="/">walidatorze</a>.</p>
<p>Obowiązek podawania numeru KSeF w płatnościach między czynnymi podatnikami VAT, według MF, jest odroczony do końca 2026 roku. Sprawdzaj aktualne zasady na stronie ksef.podatki.gov.pl.</p>

<h2 id="pomylki">Typowe pomyłki</h2>
<ul>
<li>Wpisanie w przelewie tylko numeru P_2 – sprzedawcy trudniej dopasować wpłatę, gdy wymagany jest numer KSeF.</li>
<li>Szukanie numeru KSeF w pliku XML – tam go nie ma.</li>
<li>Skracanie numeru KSeF do NIP-u i daty – numer musi mieć wszystkie 35 znaków.</li>
<li>Użycie numeru faktury jako identyfikatora w komunikacie MPP – tam wpisuje się numer KSeF (zob. <a href="/blog/numer-ksef-w-przelewie-mpp/">numer KSeF w przelewie MPP</a>).</li>
</ul>

<h2 id="gdzie">Gdzie zobaczysz oba numery w praktyce</h2>
<p>W codziennej pracy z fakturami najczęściej spotkasz oba numery w tych miejscach. Warto wiedzieć, które z nich pokazuje który, żeby nie przepisywać złego.</p>
<div class="table-wrap"><table>
<thead><tr><th scope="col">Miejsce</th><th scope="col">Numer faktury (P_2)</th><th scope="col">Numer KSeF</th></tr></thead>
<tbody>
<tr><td>plik XML FA(3) od wystawcy</td><td>tak</td><td>nie</td></tr>
<tr><td>wizualizacja PDF z KSeF</td><td>tak</td><td>tak, zwykle razem z kodem QR</td></tr>
<tr><td>UPO (urzędowe poświadczenie odbioru)</td><td>tak</td><td>tak</td></tr>
<tr><td>Aplikacja Podatnika</td><td>tak</td><td>tak</td></tr>
<tr><td>program księgowy</td><td>tak</td><td>zwykle tak, jeśli pobiera dane z KSeF</td></tr>
</tbody></table></div>
<p>Jeśli dostałeś fakturę w PDF-ie, który wygenerował program sprzedawcy, a nie system KSeF, numeru KSeF może na nim nie być. Wtedy poproś o numer albo pobierz fakturę z KSeF. Gdy PDF ma kod QR, możesz sprawdzić jego link w narzędziu <a href="/kod-qr-ksef/">kod QR KSeF</a>.</p>
<h2 id="ksiegowosc">Po co księgowości oba numery</h2>
<p>Numer wystawcy porządkuje dokumenty w jego własnej numeracji: według niego sprzedawca układa rejestr i szuka faktury w swoim programie. Numer KSeF jednoznacznie wskazuje dokument w centralnym systemie, więc pozwala dopasować płatność do właściwej faktury, nawet jeśli dwóch sprzedawców ma podobną numerację, np. FV/1/2026. Dlatego MF wprowadza numer KSeF do przelewów, a nie zastępuje nim numeracji wystawcy. W praktyce zatrzymaj oba: numer P_2 do własnej ewidencji, numer KSeF do płatności i uzgodnień.</p>
<h2 id="przypadki">Trzy sytuacje z życia firmy</h2>
<p><strong>Kupujesz od stałego dostawcy.</strong> Dostawca ma prostą numerację FV/1/2026, FV/2/2026 i tak dalej, a ty płacisz kilka faktur w miesiącu. Samo FV/2/2026 niewiele mówi bankowi i księgowemu, a numer KSeF wskazuje dokładnie jeden dokument. W tytule wpisz numer KSeF, a numer dostawcy dopisz na końcu.</p>
<p><strong>Rozliczasz wpłaty od klientów.</strong> Klient wpisał w tytule numer KSeF, a twój program księgowy szuka numeru P_2. Dopasowanie wymaga tabeli, w której obok siebie masz oba numery. Warto ją tworzyć od razu, gdy faktura trafia do KSeF, a przy większej liczbie wpłat sprawdzać tytuły z wyciągu w <a href="/sprawdz-wiele-numerow-ksef/">narzędziu do wielu numerów KSeF</a>.</p>
<p><strong>Dostajesz fakturę spoza KSeF.</strong> Faktura bez numeru KSeF, np. wystawiona w trybie awaryjnym, ma tylko numer wystawcy. MF zaznacza, że w takich przypadkach nie podaje się numeru KSeF w płatności. W tytule przelewu wpisz wtedy zwykły numer faktury.</p>
<p>We wszystkich trzech przypadkach zasada jest ta sama: numer KSeF identyfikuje dokument w systemie, a numer wystawcy pomaga ludziom. Żaden nie zastępuje drugiego.</p>
<p>Jeśli nie jesteś pewien, który numer ma na myśli sprzedawca, zapytaj go wprost. Krótka wiadomość z pytaniem, jakiego numeru oczekuje w tytule, oszczędza czasu obu stronom i zmniejsza ryzyko, że płatność trafi na niewłaściwą fakturę.</p>
<p>Dobrym nawykiem jest też opisanie w ewidencji, który numer jest którym, na przykład w osobnych kolumnach arkusza. Dzięki temu po miesiącu nie zgadujesz, co oznacza dany ciąg znaków.</p>
<p>Numeru KSeF nie znajdziesz w pliku faktury, bo nadaje go system. Wyjaśnia to artykuł <a href="/blog/dlaczego-numeru-ksef-nie-ma-w-xml/">dlaczego numeru KSeF nie ma w pliku XML</a>.</p>
<h2 id="podsumowanie">Podsumowanie</h2>
<p>Numer faktury to numer od wystawcy, numer KSeF to numer z systemu. W przelewie podaj numer KSeF, a własny numer dopisz, jeśli starczy miejsca. Skopiowany numer sprawdź w <a href="/">walidatorze numeru KSeF</a>.</p>
""",
    faq=[
        ("Czy numer KSeF zastępuje numer faktury?", "Nie. Wystawca nadal nadaje własny numer faktury, widoczny w polu P_2. Numer KSeF jest dodatkowym numerem nadawanym przez system po przyjęciu faktury."),
        ("Czy numer KSeF jest w pliku XML faktury?", "Nie. Numer powstaje po przyjęciu faktury przez system, więc plik wysyłany przez wystawcę go nie zawiera. Znajdziesz go w UPO, Aplikacji Podatnika lub na wizualizacji."),
        ("Ile znaków ma numer KSeF, a ile numer faktury?", "Numer KSeF ma 35 znaków, w tym NIP, datę, część techniczną i sumę kontrolną. Długość numeru faktury ustala wystawca."),
        ("Czy mogę wpisać oba numery w tytule przelewu?", "Tak, jeśli mieszczą się w limicie pola. Numer KSeF ma 35 znaków, a pole tytułu zwykle 140, więc zwykle starczy miejsca na oba."),
    ],
    sources=[MF_NUM, DOC_NUM, MF_FA3, XSD, APP],
)

# ---------------------------------------------------------------- #6 (2026-11-15)
C06 = dict(
    slug="numer-ksef-faktury-korygujacej",
    title="Numer KSeF faktury korygującej – co wpisać?",
    desc="Numer KSeF faktury korygującej: czym różni się od numeru faktury korygowanej, które pole XML FA(3) go wskazuje i jaki numer podać przy płatności.",
    h1="Numer KSeF faktury korygującej – co wpisać w XML i w przelewie",
    intro="Przy korekcie pojawiają się dwa numery KSeF: faktury korygowanej i samej korekty. Pokazujemy, gdzie który występuje i jak ich nie pomylić.",
    lead_tool=("/", "walidator numeru KSeF"),
    date=("2026-11-15", "15 listopada 2026"),
    content="""
<h2 id="dwa-numery">Dwie faktury, dwa numery KSeF</h2>
<p>Faktura korygująca jest osobnym dokumentem, więc po przyjęciu przez KSeF dostaje własny numer KSeF, tak jak każda faktura. Jednocześnie wskazuje fakturę, którą poprawia, a ta ma inny numer KSeF. Oba możesz sprawdzić w <a href="/">walidatorze numeru KSeF</a>.</p>
<div class="table-wrap"><table>
<thead><tr><th scope="col">Dokument</th><th scope="col">Numer KSeF</th><th scope="col">Gdzie go znajdziesz</th></tr></thead>
<tbody>
<tr><td>Faktura pierwotna (korygowana)</td><td>nadany przy jej przyjęciu</td><td>UPO, Aplikacja Podatnika, wizualizacja</td></tr>
<tr><td>Faktura korygująca</td><td>nowy, nadany przy przyjęciu korekty</td><td>UPO korekty, Aplikacja Podatnika</td></tr>
</tbody></table></div>

<h2 id="xml">Które pole XML wskazuje fakturę korygowaną</h2>
<p>W schemacie FA(3) dane faktury korygowanej znajdują się w sekcji DaneFaKorygowanej. Jest tam pole NrKSeFFaKorygowanej typu numeru KSeF, a obok znacznik NrKSeF, który informuje, że faktura korygowana była w KSeF. Jest też odrębny znacznik NrKSeFN dla faktury, która w KSeF nie została wystawiona. Wystawca wybiera jedną z tych dwóch możliwości.</p>
<p>Pole NrKSeFFaKorygowanej wymaga numeru zgodnego z formatem TNumerKSeF, czyli 35 znaków. Literówka w tym polu nie zablokuje płatności, ale utrudni powiązanie korekty z fakturą pierwotną. Dlatego przed wysłaniem skopiuj numer ze źródła i sprawdź go w <a href="/">walidatorze</a>.</p>

<h2 id="przyklad">Przykład: korekta zmniejszająca kwotę</h2>
<p>Przykład ilustracyjny, bez prawdziwych numerów. Faktura pierwotna na 1 230,00 zł brutto została skorygowana do 984,00 zł brutto.</p>
<div class="table-wrap"><table>
<thead><tr><th scope="col">Element</th><th scope="col">Wartość</th></tr></thead>
<tbody>
<tr><td>Faktura pierwotna</td><td>1 230,00 zł brutto (1 000,00 netto + 230,00 VAT)</td></tr>
<tr><td>Po korekcie</td><td>984,00 zł brutto (800,00 netto + 184,00 VAT)</td></tr>
<tr><td>Różnica</td><td>–246,00 zł brutto (–200,00 netto, –46,00 VAT)</td></tr>
<tr><td>Numer w polu NrKSeFFaKorygowanej</td><td>numer KSeF faktury pierwotnej</td></tr>
</tbody></table></div>
<p>Po korekcie in minus sprzedawca nie pobiera dopłaty, więc przelewu może nie być albo będzie to zwrot nadpłaty. Przy korekcie in plus (np. zmiana ceny z 1 000 na 1 200 zł netto) kupujący płaci różnicę.</p>

<h2 id="przelew">Co wpisać w tytule przelewu</h2>
<p>MF wskazuje, że przy płatności za fakturę podaje się numer KSeF faktury. Zasada nie opisuje osobno korekt, więc najbezpieczniej wpisać numer KSeF dokumentu, którego dotyczy płatność, a w razie wątpliwości ustalić ze sprzedawcą, jak dopasowuje wpłaty. Dopisz własny numer korekty z pola P_2, jeśli starczy miejsca w tytule. Gotowy tytuł zbudujesz w <a href="/">walidatorze</a>, a zasady pola tytułu opisuje post <a href="/blog/jak-wpisac-numer-ksef-w-tytule-przelewu/">jak wpisać numer KSeF w tytule przelewu</a>.</p>

<h2 id="porady">Praktyczne wskazówki</h2>
<ul>
<li>Zapisz oba numery w arkuszu: pierwotnej faktury i korekty.</li>
<li>Przy wielu korektach sprawdź listę w <a href="/sprawdz-wiele-numerow-ksef/">narzędziu do wielu numerów KSeF</a>.</li>
<li>Nie myl numeru KSeF z numerem P_2 – różnice opisuje post <a href="/blog/czy-numer-ksef-to-numer-faktury/">czy numer KSeF to numer faktury</a>.</li>
<li>Jeśli płacisz w MPP, pamiętaj o limicie 35 znaków w polu /INV/.</li>
</ul>

<h2 id="rodzaje">Rodzaje korekt a numery</h2>
<p>Nie każda korekta wygląda tak samo. Liczba numerów, które musisz zebrać, zależy od tego, co poprawiasz.</p>
<div class="table-wrap"><table>
<thead><tr><th scope="col">Sytuacja</th><th scope="col">Co jest do zebrania</th><th scope="col">Uwagi</th></tr></thead>
<tbody>
<tr><td>korekta jednej faktury z KSeF</td><td>numer KSeF faktury pierwotnej</td><td>trafia do pola NrKSeFFaKorygowanej</td></tr>
<tr><td>korekta faktury wystawionej poza KSeF</td><td>numer faktury pierwotnej z jej własnej numeracji</td><td>w XML używa się znacznika NrKSeFN</td></tr>
<tr><td>kilka korekt do tej samej faktury</td><td>numer faktury pierwotnej plus numery wcześniejszych korekt</td><td>każda korekta ma własny numer KSeF</td></tr>
<tr><td>płatność różnicy po korekcie in plus</td><td>numer KSeF dokumentu, którego dotyczy płatność</td><td>ustal ze sprzedawcą, jak dopasowuje wpłaty</td></tr>
</tbody></table></div>
<p>Schemat FA(3) pozwala wskazać fakturę korygowaną na dwa sposoby: przez numer KSeF albo, gdy faktury nie było w KSeF, przez jej dane wskazane znacznikiem NrKSeFN. To wygodne w okresie przejściowym, gdy część dokumentów powstała jeszcze poza systemem.</p>
<h2 id="kontrola">Jak sprawdzić korektę przed płatnością</h2>
<p>Zanim zapłacisz różnicę po korekcie, przejdź krótką listę kontrolną. Zajmie ci to minutę, a oszczędzi wyjaśnień ze sprzedawcą.</p>
<ol class="steps">
<li>Otwórz korektę w Aplikacji Podatnika albo na wizualizacji i odczytaj jej numer KSeF.</li>
<li>Porównaj numer faktury korygowanej z dokumentem, który masz w księgach.</li>
<li>Sprawdź, czy kwota różnicy zgadza się z różnicą między fakturą pierwotną a stanem po korekcie.</li>
<li>Skopiuj numer do walidatora i zbuduj tytuł przelewu.</li>
<li>Zapisz w ewidencji oba numery KSeF razem z numerami P_2.</li>
</ol>
<p>Ta sama lista sprawdza się przy płatnościach w MPP, gdzie w polu /INV/ wpisujesz numer KSeF dokumentu, który rozliczasz.</p>
<h2 id="blady">Typowe błędy przy korektach</h2>
<ul>
<li><strong>Wpisanie numeru korekty zamiast numeru faktury pierwotnej w polu NrKSeFFaKorygowanej.</strong> Pole ma wskazywać dokument poprawiany, a nie dokument poprawiający.</li>
<li><strong>Użycie numeru z poprzedniej wersji faktury.</strong> Jeśli korekta dotyczy faktury, która sama była już korygowana, sprawdź, co dokładnie wskazuje twój program księgowy.</li>
<li><strong>Brak numeru w ewidencji.</strong> Przy kilku korektach do jednej faktury łatwo zgubić, która jest która. Zapisuj numery od razu.</li>
<li><strong>Przepisywanie zamiast kopiowania.</strong> W numerze są cyfry i litery A–F, więc pomyłka O i 0 lub B i 8 psuje sumę kontrolną.</li>
</ul>
<p>Przy wątpliwościach co do wystawiania korekt i ich skutków podatkowych zajrzyj do materiałów MF na ksef.podatki.gov.pl albo zapytaj księgową. Ten wpis opisuje wyłącznie numery i pola, nie rozstrzyga, kiedy i jak wystawić korektę.</p>
<p>Jeśli korekta dotyczy faktury sprzed wdrożenia KSeF, numeru KSeF faktury pierwotnej może nie być. W takim przypadku schemat przewiduje wskazanie jej innymi danymi, zamiast numeru KSeF. Szczegóły podaje dokumentacja schematu FA(3) na stronie MF.</p>
<p>Dobrym nawykiem jest prowadzenie osobnej kolumny „numer KSeF korekty” w arkuszu rozliczeń. Dzięki temu po miesiącu od razu widzisz, które dokumenty są poprawione, a które czekają na płatność lub zwrot.</p>
<h2 id="podsumowanie">Podsumowanie</h2>
<p>Korekta ma własny numer KSeF, a numer faktury korygowanej wskazuje w XML pole NrKSeFFaKorygowanej. W przelewie podaj numer dokumentu, którego dotyczy płatność, i w razie wątpliwości potwierdź to ze sprzedawcą. Każdy numer sprawdź w <a href="/">walidatorze numeru KSeF</a>.</p>
""",
    faq=[
        ("Czy faktura korygująca ma własny numer KSeF?", "Tak. Korekta jest osobną fakturą, więc po przyjęciu przez KSeF dostaje własny numer, inny niż numer faktury korygowanej."),
        ("Które pole XML zawiera numer KSeF faktury korygowanej?", "W schemacie FA(3) jest to pole NrKSeFFaKorygowanej w sekcji DaneFaKorygowanej. Dla faktury spoza KSeF służy znacznik NrKSeFN."),
        ("Czy przy korekcie in minus trzeba robić przelew?", "Jeśli korekta zmniejsza kwotę, kupujący nie dopłaca. Ewentualny zwrot nadpłaty zależy od ustaleń ze sprzedawcą, a nie od numeru KSeF."),
        ("Jak sprawdzić, czy numer faktury korygowanej jest poprawny?", "Wklej go do walidatora numeru KSeF. Narzędzie sprawdzi długość, NIP, datę i sumę kontrolną, ale nie potwierdzi, że faktura istnieje w KSeF."),
    ],
    sources=[DOC_NUM, MF_NUM, MF_FA3, XSD, APP],
)


# ---------------------------------------------------------------- #7-9 (2026-11-16)
C07 = dict(
    slug="numer-ksef-faktury-zaliczkowej",
    title="Numer KSeF faktury zaliczkowej i przelew zaliczki",
    desc="Numer KSeF faktury zaliczkowej: jak nadawany jest numer, które pole FA(3) wskazuje zaliczkę na fakturze końcowej i jaki numer wpisać w tytule przelewu.",
    h1="Numer KSeF faktury zaliczkowej – gdzie go wpisać i co z przelewem zaliczki",
    intro="Faktura zaliczkowa to zwykła faktura w KSeF, więc dostaje własny numer. Pokazujemy, gdzie ten numer wraca na fakturze końcowej i jak go użyć przy płatności.",
    lead_tool=("/", "walidator numeru KSeF"),
    date=("2026-11-16", "16 listopada 2026"),
    content="""
<h2 id="zaliczka">Faktura zaliczkowa w KSeF – własny numer</h2>
<p>Faktura dokumentująca otrzymanie zapłaty przed wykonaniem czynności ma w schemacie FA(3) osobny rodzaj. W pliku XSD udostępnionym przez Ministerstwo Finansów w polu RodzajFaktury występuje wartość <code>ZAL</code>, opisana jako faktura dokumentująca otrzymanie zapłaty lub jej części przed dokonaniem czynności. Dla KSeF to po prostu kolejna faktura: po przyjęciu przez system dostaje numer KSeF o tej samej budowie co każdy inny, czyli 35 znaków (NIP sprzedawcy, data przyjęcia, część techniczna i suma kontrolna).</p>
<p>Oznacza to, że przy zaliczce nie ma żadnego specjalnego formatu numeru. Zanim go użyjesz w przelewie, możesz sprawdzić go w <a href="/">walidatorze numeru KSeF</a>: narzędzie zweryfikuje długość, NIP, datę i sumę kontrolną.</p>
<div class="table-wrap"><table>
<thead><tr><th scope="col">Dokument</th><th scope="col">Rodzaj w FA(3)</th><th scope="col">Numer KSeF</th></tr></thead>
<tbody>
<tr><td>Faktura zaliczkowa</td><td class="mono">ZAL</td><td>własny, nadany przy przyjęciu</td></tr>
<tr><td>Faktura końcowa (rozliczająca)</td><td class="mono">ROZ</td><td>własny, nadany przy przyjęciu</td></tr>
<tr><td>Korekta faktury zaliczkowej</td><td class="mono">KOR_ZAL</td><td>własny, nadany przy przyjęciu</td></tr>
</tbody></table></div>
<p>Skróty rodzajów pochodzą z wyliczenia w schemacie FA(3): ZAL dotyczy faktur zaliczkowych, ROZ faktury wystawianej w związku z art. 106f ust. 3 ustawy o VAT, a KOR_ZAL korekty faktury zaliczkowej.</p>

<h2 id="koncowa">Gdzie numer zaliczki trafia na fakturze końcowej</h2>
<p>Faktura końcowa musi wskazywać wcześniejsze zaliczki. Schemat FA(3) przewiduje na to element FakturaZaliczkowa, który może wystąpić do 100 razy. Opis pola w XSD brzmi: numery faktur zaliczkowych lub ich numery KSeF, jeśli zostały wystawione z użyciem KSeF. Wybór zależy od tego, jak powstała zaliczka:</p>
<ul>
<li><strong>NrKSeFFaZaliczkowej</strong> – numer identyfikujący fakturę zaliczkową w KSeF. Pole obowiązkowe, gdy zaliczka była wystawiona za pomocą KSeF.</li>
<li><strong>NrKSeFZN</strong> razem z <strong>NrFaZaliczkowej</strong> – znacznik zaliczki wystawionej poza KSeF i jej zwykły numer nadany przez sprzedawcę.</li>
</ul>
<p>Dokumentacja schematu zaznacza, że numer faktury zaliczkowej jest obowiązkowy na fakturze wystawianej po wydaniu towaru lub wykonaniu usługi, o której mowa w art. 106f ust. 3 ustawy. Praktyczny wniosek: przy rozliczaniu zaliczek trzymaj numery KSeF wszystkich zaliczek pod ręką, bo program fakturujący będzie ich potrzebował.</p>

<h2 id="przyklad">Przykład: dwie zaliczki i faktura końcowa</h2>
<p>Załóżmy zlecenie za 30 000 zł netto rozliczane w trzech etapach. Numery poniżej są wymyślone na potrzeby przykładu i mają tylko pokazać układ:</p>
<div class="table-wrap"><table>
<thead><tr><th scope="col">Etap</th><th scope="col">Dokument</th><th scope="col">Co zawiera pole FakturaZaliczkowa</th></tr></thead>
<tbody>
<tr><td>1</td><td>Zaliczka 30%</td><td>nic, to pierwsza faktura w serii</td></tr>
<tr><td>2</td><td>Zaliczka 30%</td><td>nic (zależnie od układu dokumentów)</td></tr>
<tr><td>3</td><td>Faktura końcowa</td><td>numery KSeF obu zaliczek</td></tr>
</tbody></table></div>
<p>Na fakturze końcowej program wypełni dwa elementy FakturaZaliczkowa, każdy z numerem KSeF jednej zaliczki. Jeśli któraś zaliczka została wystawiona poza KSeF, dla niej zostanie użyty znacznik NrKSeFZN i zwykły numer faktury. Kwoty i podatek rozlicza się według ustawy o VAT, a ten wpis opisuje tylko numery.</p>

<h2 id="przelew">Jaki numer wpisać w przelewie zaliczki</h2>
<p>Ministerstwo Finansów opisuje zasadę ogólnie: przy płatności za pojedynczą fakturę podawany jest numer KSeF tej faktury. Zaliczka jest fakturą, więc przelew zaliczki dotyczy numeru KSeF faktury zaliczkowej, a przelew reszty należności dotyczy numeru faktury końcowej. Obowiązek podawania numeru w płatnościach między czynnymi podatnikami VAT zaczyna się 1 stycznia 2027 r. (art. 108g ustawy o VAT), a do końca 2026 r. jest odroczony.</p>
<p>Jeśli płacisz zaliczkę jeszcze przed wystawieniem faktury (np. na podstawie proformy), numeru KSeF po prostu jeszcze nie ma. W takiej sytuacji uzgodnij ze sprzedawcą, jak oznaczyć płatność, i zapytaj księgową, czy w twoim przypadku obowiązek w ogóle dotyczy takiej płatności. Gotowy tytuł zbudujesz w <a href="/przelew-mpp-numer-ksef/">kreatorze przelewu MPP</a> lub w walidatorze.</p>
<p>Przykład tytułu zaliczki, gdy numer KSeF faktury zaliczkowej to oficjalny przykład MF:</p>
<p class="mono">5265877635-20250826-0100001AF629-AF</p>
<p>W polu tytułu wpisujesz sam numer, ewentualnie z krótkim opisem, pamiętając o limicie 140 znaków.</p>

<h2 id="bledy">Typowe pomyłki</h2>
<ul>
<li><strong>Podanie numeru faktury końcowej w przelewie zaliczki.</strong> Faktura końcowa jeszcze nie istnieje, kiedy płacisz zaliczkę.</li>
<li><strong>Pominięcie zaliczki w fakturze końcowej.</strong> Każda zaliczka rozliczana w KSeF powinna mieć swój element z numerem.</li>
<li><strong>Ręczne przepisywanie numeru.</strong> W numerze są litery A–F i cyfry, a pomyłka psuje sumę kontrolną. Kopiuj i wklejaj.</li>
<li><strong>Mylenie korekty zaliczki z zaliczką.</strong> Korekta (KOR_ZAL) ma własny numer, tak samo jak opisujemy w tekście o <a href="/blog/numer-ksef-faktury-korygujacej/">numerze KSeF faktury korygującej</a>.</li>
</ul>
<h2 id="kontrola">Jak sprawdzić zaliczki przed wystawieniem faktury końcowej</h2>
<p>Przy dłuższych zleceniach, gdzie zaliczek jest kilka, łatwo o pomyłkę w numerach. Prosta kontrola zajmuje kilka minut i oszczędza poprawiania dokumentów.</p>
<ol class="steps">
<li>Wypisz wszystkie wystawione zaliczki ze zleceniem, którego dotyczą, wraz z numerami KSeF.</li>
<li>Wklej każdy numer do <a href="/sprawdz-wiele-numerow-ksef/">sprawdzarki wielu numerów KSeF</a>. Narzędzie przetworzy całą listę naraz i wskaże numery z błędem formatu.</li>
<li>Porównaj liczbę zaliczek na liście z liczbą elementów FakturaZaliczkowa w projekcie faktury końcowej.</li>
<li>Upewnij się, że zaliczki wystawione poza KSeF są oznaczone znacznikiem NrKSeFZN i mają zwykły numer.</li>
<li>Dopiero potem wyślij fakturę końcową do KSeF.</li>
</ol>
<p>Warto wiedzieć, że zaliczki wystawione jeszcze przed wdrożeniem KSeF u danego sprzedawcy nie mają numeru KSeF w ogóle. Dla nich schemat przewiduje właśnie wariant z numerem zwykłym. Jeśli masz wątpliwości, który wariant dotyczy konkretnej zaliczki, sprawdź, czy dokument figuruje w Aplikacji Podatnika.</p>
<h2 id="program">Co robi za ciebie program fakturujący</h2>
<p>Większość programów do fakturowania sama wypełnia element FakturaZaliczkowa, jeśli faktura końcowa jest powiązana z wcześniejszymi zaliczkami. Wiedza o polach XML przydaje się jednak wtedy, gdy trzeba zweryfikować wynik. Gdy odbierasz fakturę końcową jako nabywca, możesz otworzyć plik XML i zobaczyć, jakie numery KSeF zaliczek na niej wskazano, a następnie porównać je ze swoimi zapisami. Pomaga w tym <a href="/przelew-z-faktury-xml-ksef/">narzędzie do wczytywania faktury XML</a>, które pokazuje dane płatności z pliku.</p>
<p>Nabywca powinien też pilnować, żeby kwota przelewu końcowego odpowiadała kwocie do zapłaty z faktury końcowej, a nie jej pełnej wartości brutto. Zaliczki już zapłacone pomniejszają należność. Numer KSeF w przelewie nie zastępuje tej kontroli, jest tylko identyfikatorem dokumentu, którego dotyczy płatność. Dlatego dobrze jest zapisywać w ewidencji osobno: numer KSeF zaliczki, kwotę wpłaty i datę przelewu, a przy fakturze końcowej dopisać, które zaliczki zostały rozliczone.</p>
<h2 id="podsumowanie">Podsumowanie</h2>
<p>Zaliczka ma własny, standardowy numer KSeF, a faktura końcowa wskazuje go w polu NrKSeFFaZaliczkowej. W przelewie zaliczki podajesz numer faktury zaliczkowej, o ile już istnieje. Każdy numer sprawdź w <a href="/">walidatorze numeru KSeF</a> przed zapłatą. Szczegóły rozliczeń podatkowych zostaw księgowej i przepisom, bo ten tekst wyjaśnia tylko numerację.</p>
""",
    faq=[
        ("Czy faktura zaliczkowa ma numer KSeF?", "Tak. Jeśli została wystawiona w KSeF, po przyjęciu dostaje numer o standardowej budowie, 35 znaków, taki sam jak każda inna faktura."),
        ("Które pole FA(3) wskazuje zaliczkę na fakturze końcowej?", "Element FakturaZaliczkowa, a w nim NrKSeFFaZaliczkowej dla zaliczki z KSeF albo NrKSeFZN z NrFaZaliczkowej dla zaliczki wystawionej poza KSeF."),
        ("Ile zaliczek można wskazać na jednej fakturze końcowej?", "Schemat FA(3) pozwala powtórzyć element FakturaZaliczkowa maksymalnie 100 razy."),
        ("Co wpisać w tytule przelewu, gdy faktury zaliczkowej jeszcze nie ma?", "Numeru KSeF nie da się podać, bo nie został nadany. Ustal ze sprzedawcą sposób oznaczenia płatności i potwierdź z księgową, czy obowiązek obejmuje taką płatność."),
    ],
    sources=[DOC_NUM, MF_NUM, MF_FA3, XSD, MF_TERM],
)

C08 = dict(
    slug="czy-numer-ksef-musi-byc-w-tytule-przelewu",
    title="Czy numer KSeF musi być w tytule przelewu?",
    desc="Czy numer KSeF musi być w tytule przelewu: od kiedy obowiązuje art. 108g, kogo dotyczy, co z kilkoma fakturami i MPP oraz ile numerów mieści się w 140 znakach.",
    h1="Czy numer KSeF musi być w tytule przelewu? Zasady od 1 stycznia 2027",
    intro="Krótko: od 1 stycznia 2027 r. tak, ale nie w każdej sytuacji. Sprawdź, kogo dotyczy obowiązek, jak wygląda tytuł przy jednej i wielu fakturach i co z płatnością w MPP.",
    lead_tool=("/", "walidator numeru KSeF i generator tytułu przelewu"),
    date=("2026-11-16", "16 listopada 2026"),
    content="""
<h2 id="odpowiedz">Krótka odpowiedź</h2>
<p>Ministerstwo Finansów w zestawieniu kluczowych terminów KSeF pisze, że do końca 2026 r. odroczony jest obowiązek podawania numeru KSeF faktury podczas płatności pomiędzy podatnikami czynnymi (art. 108g ustawy o VAT) oraz w ramach MPP. Z tego wynika, że obowiązek zaczyna się 1 stycznia 2027 r. Dotyczy płatności za faktury wystawione w KSeF, a nie każdego przelewu w ogóle.</p>
<p>Zanim zbudujesz tytuł, wklej numer do <a href="/">generatora tytułu przelewu</a>. Sprawdzi on poprawność numeru i ułoży gotowy tekst.</p>
<div class="table-wrap"><table>
<thead><tr><th scope="col">Sytuacja</th><th scope="col">Co podajesz w płatności (wg MF)</th></tr></thead>
<tbody>
<tr><td>Jedna faktura</td><td>numer KSeF tej faktury</td></tr>
<tr><td>Kilka faktur</td><td>identyfikator zbiorczy albo kilka numerów KSeF albo kilka identyfikatorów zbiorczych</td></tr>
<tr><td>Płatność w MPP</td><td>numer KSeF w komunikacie przelewu; zamiast okresu można podać identyfikator zbiorczy</td></tr>
<tr><td>Faktura w trybie awaryjnym lub offline niewprowadzona do systemu z powodu awarii</td><td>wyjątek opisany przez MF, numeru KSeF nie ma</td></tr>
</tbody></table></div>

<h2 id="kogo">Kogo dotyczy obowiązek</h2>
<p>Przepis, na który powołuje się MF, mówi o płatnościach pomiędzy podatnikami czynnymi. Czynny podatnik VAT to firma zarejestrowana jako czynna, a nie podatnik zwolniony. Jeśli nie jesteś pewien statusu swojego lub kontrahenta, sprawdź go na stronach podatki.gov.pl albo zapytaj księgową. Ten tekst nie rozstrzyga indywidualnych przypadków, tylko streszcza stanowisko MF.</p>
<p>Obowiązek nie dotyczy też faktur wystawionych poza KSeF, bo takie faktury nie mają numeru KSeF. W ich przypadku podaje się zwykły numer faktury, tak jak dotychczas.</p>

<h2 id="jedna">Jedna faktura – najprostszy przypadek</h2>
<p>W tytule wpisujesz numer KSeF faktury, którą płacisz. Używając oficjalnego przykładu MF:</p>
<p class="mono">5265877635-20250826-0100001AF629-AF</p>
<p>Numer ma 35 znaków, więc zostaje jeszcze 105 znaków z limitu 140 na ewentualny dodatkowy opis. Jak zapisać numer w różnych bankach, opisujemy w poradniku <a href="/blog/jak-wpisac-numer-ksef-w-tytule-przelewu/">jak wpisać numer KSeF w tytule przelewu</a>.</p>

<h2 id="wiele">Kilka faktur i limit znaków</h2>
<p>MF wskazuje trzy możliwości dla płatności za więcej niż jedną fakturę, z zastrzeżeniem ograniczeń technicznych pola tytułu. Prosty rachunek pokazuje, skąd wynikają: przy limicie 140 znaków zmieszczą się trzy numery po 35 znaków oddzielone dwoma separatorami, czyli 107 znaków. Czwarty numer wymaga kolejnych 36 znaków (separator plus numer), co daje 143, a więc przekracza limit. Dlatego przy większej liczbie faktur sensownym wyjściem jest identyfikator zbiorczy, który omawiamy w tekście <a href="/identyfikator-zbiorczy-ksef/">o identyfikatorze zbiorczym KSeF</a>.</p>
<div class="table-wrap"><table>
<thead><tr><th scope="col">Liczba numerów</th><th scope="col">Długość (35 znaków + separatory)</th><th scope="col">Mieści się w 140?</th></tr></thead>
<tbody>
<tr><td>1</td><td>35</td><td>tak</td></tr>
<tr><td>2</td><td>71</td><td>tak</td></tr>
<tr><td>3</td><td>107</td><td>tak</td></tr>
<tr><td>4</td><td>143</td><td>nie</td></tr>
</tbody></table></div>
<p>To obliczenia na podstawie długości numeru. Limit pola w twoim banku może być inny, więc sprawdź go w formularzu przelewu.</p>

<h2 id="mpp">Płatność w MPP</h2>
<p>MF pisze, że w komunikacie przelewu MPP podaje się między innymi numer KSeF faktury. Szczegółowy zapis słów kodowych /VAT/, /IDC/, /INV/ i /TXT/ znajdziesz w <a href="/przelew-mpp-numer-ksef/">kreatorze przelewu MPP</a>. Pole /INV/ może zawierać numer KSeF albo identyfikator zbiorczy.</p>

<h2 id="co-robic">Co zrobić przed 1 stycznia 2027</h2>
<ol class="steps">
<li>Ustal, którzy kontrahenci wystawiają faktury w KSeF i czy są czynnymi podatnikami.</li>
<li>Zdecyduj, kto w firmie pobiera numery KSeF z faktur i jak trafiają do przelewów.</li>
<li>Przetestuj zapis numeru w swoim banku, szczególnie przy MPP.</li>
<li>Przy wielu fakturach do jednego kontrahenta rozważ identyfikator zbiorczy.</li>
</ol>
<h2 id="przyklady">Trzy przykłady z życia firmy</h2>
<p>Poniższe sytuacje są uproszczone i mają pokazać sposób myślenia, a nie zastąpić interpretacji przepisów. Numery KSeF w przykładach to oficjalny wzór z dokumentacji MF.</p>
<div class="table-wrap"><table>
<thead><tr><th scope="col">Przykład</th><th scope="col">Co robisz przy płatności</th></tr></thead>
<tbody>
<tr><td>Firma A (czynny VAT) płaci firmie B (czynny VAT) za jedną fakturę z KSeF</td><td>wpisuje numer KSeF tej faktury w tytule</td></tr>
<tr><td>Firma A płaci za pięć faktur tego samego sprzedawcy jednym przelewem</td><td>używa identyfikatora zbiorczego lub grupuje płatności tak, by numery mieściły się w polu</td></tr>
<tr><td>Firma A płaci za fakturę wystawioną poza KSeF</td><td>wpisuje zwykły numer faktury, bo numeru KSeF nie ma</td></tr>
</tbody></table></div>
<p>Najczęściej kłopot sprawia drugi przypadek, bo wielu księgowych płaci hurtowo raz w tygodniu. Tu przydaje się tekst o tym, <a href="/blog/identyfikator-zbiorczy-ksef-co-to-jest/">czym jest identyfikator zbiorczy</a>. Według MF jeden identyfikator może obejmować maksymalnie 500 numerów KSeF, a wszystkie faktury w nim muszą pochodzić od tego samego sprzedawcy.</p>
<h2 id="bank">Czy bank sprawdzi numer w tytule</h2>
<p>Banki przyjmują tytuł przelewu jako zwykły tekst i same nie weryfikują, czy numer KSeF jest prawdziwy. Pomyłka w numerze zostanie więc wykryta dopiero przez odbiorcę, który nie będzie mógł dopasować wpłaty do faktury. Dlatego sprawdzenie sumy kontrolnej przed wysłaniem przelewu ma sens: wyłapuje literówki, zanim pieniądze wyjdą z konta. W płatnościach MPP formularz banku jest bardziej wymagający, bo wymaga słów kodowych w ściśle określonej kolejności, co opisujemy w specyfikacji mBanku cytowanej w naszym kreatorze.</p>
<p>Warto też pamiętać o dopuszczalnych znakach. W specyfikacji mBanku dla pola szczegółów płatności wymienione są litery, cyfry oraz znaki &amp;%()-{}/,. oraz polskie znaki, a niedozwolone są między innymi dwukropek, gwiazdka, średnik, wykrzyknik, plus, znak zapytania i kreska pionowa. Numer KSeF składa się tylko z cyfr, wielkich liter A–F i myślników, więc mieści się w dozwolonym zestawie, ale dodatkowy opis dopisany obok może już go naruszyć.</p>
<h2 id="podsumowanie">Podsumowanie</h2>
<p>Od 1 stycznia 2027 r. numer KSeF w tytule jest wymagany w płatnościach między czynnymi podatnikami VAT za faktury z KSeF. Jedna faktura to jeden numer, wiele faktur to numery lub identyfikator zbiorczy. Sprawdź numer w <a href="/">walidatorze</a> przed wysłaniem przelewu.</p>
""",
    faq=[
        ("Od kiedy numer KSeF musi być w przelewie?", "Według Ministerstwa Finansów obowiązek podawania numeru KSeF w płatnościach między podatnikami czynnymi był odroczony do końca 2026 r., więc zaczyna się 1 stycznia 2027 r."),
        ("Czy przelew do kontrahenta bez faktury z KSeF też wymaga numeru?", "Nie ma wtedy numeru KSeF do podania. Faktura wystawiona poza KSeF ma tylko zwykły numer."),
        ("Ile numerów KSeF zmieści się w tytule przelewu?", "Przy limicie 140 znaków trzy numery po 35 znaków z separatorami to 107 znaków, a cztery to 143, więc nie zmieszczą się. Limit w twoim banku sprawdź w formularzu."),
        ("Co zamiast kilku numerów KSeF?", "MF wskazuje identyfikator zbiorczy, który obejmuje wiele faktur jednego sprzedawcy."),
    ],
    sources=[MF_TERM, MF_NUM, DOC_NUM, MBANK_SPEC, APP],
)

C09 = dict(
    slug="numer-ksef-ile-znakow",
    title="Numer KSeF – ile ma znaków i dlaczego 35?",
    desc="Numer KSeF ma 35 znaków: 10 cyfr NIP, 8 cyfr daty, 12 znaków części technicznej i 2 sumy kontrolnej plus 3 myślniki. Wyjaśniamy też stary format 36 znaków.",
    h1="Numer KSeF – ile ma znaków i dlaczego dokładnie 35",
    intro="Numer KSeF ma zawsze 35 znaków razem z myślnikami. Rozbijamy tę liczbę na części i pokazujemy, co zrobić, gdy ktoś podaje numer o innej długości.",
    lead_tool=("/", "walidator numeru KSeF"),
    date=("2026-11-16", "16 listopada 2026"),
    content="""
<h2 id="35">35 znaków – skąd ta liczba</h2>
<p>Dokumentacja KSeF 2.0 opublikowana przez Ministerstwo Finansów mówi wprost, że numer KSeF zawsze ma długość 35 znaków. Ogólny wzór to <code>9999999999-RRRRMMDD-FFFFFFFFFFFF-FF</code>. Liczba 35 to po prostu suma czterech bloków i trzech myślników:</p>
<div class="table-wrap"><table>
<thead><tr><th scope="col">Część</th><th scope="col">Przykład</th><th scope="col">Znaki</th></tr></thead>
<tbody>
<tr><td>NIP sprzedawcy</td><td class="mono">5265877635</td><td>10</td></tr>
<tr><td>Myślnik</td><td class="mono">-</td><td>1</td></tr>
<tr><td>Data przyjęcia (RRRRMMDD)</td><td class="mono">20250826</td><td>8</td></tr>
<tr><td>Myślnik</td><td class="mono">-</td><td>1</td></tr>
<tr><td>Część techniczna</td><td class="mono">0100001AF629</td><td>12</td></tr>
<tr><td>Myślnik</td><td class="mono">-</td><td>1</td></tr>
<tr><td>Suma kontrolna CRC-8</td><td class="mono">AF</td><td>2</td></tr>
<tr><td colspan="2"><strong>Razem</strong></td><td><strong>35</strong></td></tr>
</tbody></table></div>
<p>Rachunek: 10 + 8 + 12 + 2 = 32 znaki danych, do tego 3 myślniki, razem 35. To dokładnie te 32 znaki (razem z dwoma myślnikami między blokami) są podstawą do obliczenia sumy kontrolnej, o czym piszemy w tekście <a href="/blog/z-czego-sklada-sie-numer-ksef/">z czego składa się numer KSeF</a>.</p>

<h2 id="bez-myslnikow">A bez myślników?</h2>
<p>Bez trzech myślników zostaje 32 znaki. Taki zapis bywa spotykany w nazwach plików i arkuszach, ale oficjalny numer zawiera myślniki, więc w tytule przelewu i w XML podajesz go w pełnej postaci 35-znakowej. Walidator zaczyna od sprawdzenia długości, więc numer bez myślników zostanie zgłoszony jako błędny.</p>

<h2 id="36">Stary format 36 znaków</h2>
<p>W starszej wersji KSeF (1.0) numer miał jeden dodatkowy myślnik w części technicznej i długość 36 znaków. Schemat FA(3) w polu typu TNumerKSeF nadal dopuszcza ten starszy zapis, żeby można było odwołać się do faktur wystawionych w poprzednim systemie. Nowo nadawane numery w KSeF 2.0 mają 35 znaków. Jeśli widzisz numer 36-znakowy, to najpewniej pochodzi on z poprzedniej wersji systemu, a nie jest zwykłą literówką.</p>

<h2 id="sprawdz">Jak szybko policzyć długość</h2>
<ol class="steps">
<li>Skopiuj numer z faktury lub UPO – nie przepisuj go ręcznie.</li>
<li>Policz bloki: 10, 8, 12 i 2 znaki, rozdzielone trzema myślnikami.</li>
<li>Upewnij się, że na końcu nie ma spacji ani znaku nowej linii, które wydłużają ciąg.</li>
<li>Wklej numer do <a href="/">walidatora</a>, który sprawdzi też NIP, datę i sumę kontrolną.</li>
</ol>

<h2 id="inne">Co z innymi długościami</h2>
<div class="table-wrap"><table>
<thead><tr><th scope="col">Długość</th><th scope="col">Najczęstsza przyczyna</th></tr></thead>
<tbody>
<tr><td>32</td><td>numer bez myślników</td></tr>
<tr><td>34 lub mniej</td><td>ucięty końcowy fragment przy kopiowaniu</td></tr>
<tr><td>35</td><td>poprawna długość, sprawdź jeszcze sumę kontrolną</td></tr>
<tr><td>36</td><td>stary format KSeF 1.0 albo dodatkowy znak (np. spacja)</td></tr>
<tr><td>powyżej 36</td><td>numer z dopisanym tekstem lub dwa numery sklejone razem</td></tr>
</tbody></table></div>
<p>Dobra długość nie gwarantuje, że numer jest prawdziwy: mówi tylko, że ma właściwy format. Czy faktura istnieje w KSeF, potwierdzisz w Aplikacji Podatnika lub w systemie, z którego korzystasz. Identyfikator zbiorczy ma podobną długość i budowę, ale zamiast daty zawiera oznaczenie IZ oraz rok i miesiąc, jak opisujemy w tekście o <a href="/identyfikator-zbiorczy-ksef/">identyfikatorze zbiorczym</a>.</p>
<h2 id="walidacja">Jak liczy to walidator</h2>
<p>Kolejność sprawdzania w naszym narzędziu odpowiada budowie numeru. Najpierw liczona jest długość, bo błąd długości zwykle oznacza ucięcie lub dopisanie znaków przy kopiowaniu. Potem sprawdzany jest NIP w pierwszym bloku (wagi 6, 5, 7, 2, 3, 4, 5, 6, 7, suma modulo 11 musi być równa dziesiątej cyfrze), następnie data z drugiego bloku oraz dopuszczalne znaki w trzecim. Na końcu liczona jest suma kontrolna CRC-8 z wielomianem 0x07 i wartością początkową 0 z pierwszych 32 znaków i porównywana z dwoma ostatnimi znakami numeru.</p>
<p>Taki porządek ma sens, bo każdy kolejny krok jest bardziej kosztowny i mniej oczywisty dla człowieka. Długość policzysz wzrokiem, NIP kalkulatorem, a CRC-8 w praktyce tylko programem. Jeśli wynik pokazuje błąd już na długości, nie ma sensu szukać dalej, najpierw skopiuj numer jeszcze raz.</p>
<h2 id="przyklad-bledu">Przykład: ten sam numer z błędami długości</h2>
<p>Weźmy oficjalny przykład i zobaczmy, jak zmienia się wynik po typowych pomyłkach:</p>
<div class="table-wrap"><table>
<thead><tr><th scope="col">Wariant</th><th scope="col">Zapis</th><th scope="col">Znaki</th></tr></thead>
<tbody>
<tr><td>poprawny</td><td class="mono">5265877635-20250826-0100001AF629-AF</td><td>35</td></tr>
<tr><td>bez myślników</td><td class="mono">5265877635202508260100001AF629AF</td><td>32</td></tr>
<tr><td>bez ostatniego znaku</td><td class="mono">5265877635-20250826-0100001AF629-A</td><td>34</td></tr>
<tr><td>ze spacją na końcu</td><td class="mono">5265877635-20250826-0100001AF629-AF&nbsp;</td><td>36</td></tr>
</tbody></table></div>
<p>Każdy z trzech błędnych wariantów ma długość inną niż 35, więc walidator odrzuci go na pierwszym kroku. Ostatni jest podstępny: spacja na końcu jest niewidoczna, a zwiększa długość do 36, czyli do liczby znanej ze starego formatu. Jeśli więc dostajesz numer 36-znakowy i nie jesteś pewien jego pochodzenia, usuń końcowe białe znaki i policz jeszcze raz.</p>
<h2 id="po-co">Po co w ogóle ta stała długość</h2>
<p>Stała długość ułatwia programom księgowym i bankom rozpoznanie numeru w tekście. Dzięki niej można automatycznie wyszukać numer KSeF w tytule przelewu i dopasować płatność do faktury. Pole <code>/INV/</code> w komunikacie MPP ma w specyfikacji mBanku długość do 35 znaków, co dokładnie mieści jeden numer KSeF. Tytuł zwykłego przelewu może mieć 140 znaków, więc zmieści jeden numer z dodatkowym opisem albo kilka numerów, o czym piszemy w tekście <a href="/blog/czy-numer-ksef-musi-byc-w-tytule-przelewu/">czy numer KSeF musi być w tytule przelewu</a>.</p>
<p>Warto zwrócić uwagę, że kody QR do płatności w standardzie ZBP ograniczają tytuł do 32 znaków, więc numer 35-znakowy się w nim nie zmieści. To jeden z powodów, dla których numer KSeF występuje w kodach weryfikacyjnych w innej formie, o czym piszemy na stronie o <a href="/kod-qr-ksef/">kodzie QR KSeF</a>.</p>
<h2 id="ksiegowosc">Długość numeru w arkuszu i programie księgowym</h2>
<p>Jeśli prowadzisz ewidencję faktur w arkuszu kalkulacyjnym, ustaw dla kolumny z numerem KSeF format tekstowy i dodaj prostą kontrolę długości. W większości arkuszy wystarczy formuła zliczająca znaki w komórce i podświetlająca wynik różny od 35. Dzięki temu błędnie wklejony numer od razu rzuci się w oczy, jeszcze przed przygotowaniem przelewu. Ten sam warunek warto ustawić w eksportach z programu księgowego, bo część systemów przy eksporcie do CSV obcina lub zmienia zapis długich ciągów znaków. Jeśli masz wiele numerów naraz, użyj <a href="/sprawdz-wiele-numerow-ksef/">sprawdzarki wielu numerów KSeF</a>, która wskaże wszystkie błędne wiersze.</p>
<h2 id="podsumowanie">Podsumowanie</h2>
<p>Numer KSeF ma 35 znaków: 32 znaki danych i 3 myślniki. Wszystko inne to błąd, brak myślników albo stary format 36-znakowy. Zawsze kopiuj numer i sprawdzaj go w <a href="/">walidatorze numeru KSeF</a>.</p>
""",
    faq=[
        ("Ile znaków liczy numer KSeF?", "35 znaków razem z trzema myślnikami: 10 cyfr NIP, 8 cyfr daty, 12 znaków części technicznej i 2 znaki sumy kontrolnej."),
        ("Ile znaków ma numer KSeF bez myślników?", "32 znaki. W tytule przelewu i w XML używa się jednak pełnej postaci 35-znakowej."),
        ("Dlaczego widzę numer KSeF z 36 znakami?", "To format znany z KSeF 1.0, z dodatkowym myślnikiem w części technicznej. Schemat FA(3) nadal go dopuszcza, ale nowe numery mają 35 znaków."),
        ("Czy 35 znaków oznacza, że numer jest prawidłowy?", "Nie. To tylko poprawna długość. Trzeba jeszcze sprawdzić NIP, datę i sumę kontrolną CRC-8, co robi walidator."),
    ],
    sources=[DOC_NUM, MF_NUM, XSD, MF_FA3],
)

C10 = dict(
    slug="przelew-za-kilka-faktur-ksef",
    title="Przelew za kilka faktur KSeF jednym przelewem",
    desc="Jak zapłacić za kilka faktur jednym przelewem z numerem KSeF w tytule: kilka numerów w polu 140 znaków albo jeden identyfikator zbiorczy. Przykłady.",
    h1="Przelew za kilka faktur KSeF jednym przelewem – jak opisać tytuł",
    intro="Płacisz kontrahentowi za kilka faktur naraz i nie wiesz, czy trzeba robić osobne przelewy? Pokazujemy dwie drogi: kilka numerów KSeF w tytule albo jeden identyfikator zbiorczy.",
    lead_tool=("/identyfikator-zbiorczy-ksef/", "walidator identyfikatora zbiorczego"),
    date=("2026-11-17", "17 listopada 2026"),
    content="""
<h2 id="zasada">Co mówi Ministerstwo Finansów</h2>
<p>Na stronie o numerze KSeF i zbiorczym identyfikatorze Ministerstwo Finansów opisuje, że przy płatności za więcej niż jedną fakturę można podać zbiorczy identyfikator albo kilka numerów KSeF albo kilka zbiorczych identyfikatorów, przy uwzględnieniu ograniczeń technicznych pola z tytułem płatności. Jeśli chcesz od razu sprawdzić zapis, użyj <a href="/identyfikator-zbiorczy-ksef/">walidatora identyfikatora zbiorczego</a> albo <a href="/">walidatora numeru KSeF</a>.</p>
<p>Zgodnie z informacją MF obowiązek podawania numeru KSeF w płatnościach między podatnikami czynnymi został odroczony do końca 2026 roku, więc zasady zaczynają działać od 1 stycznia 2027. Szczegóły terminów sprawdzaj zawsze na stronie ksef.podatki.gov.pl.</p>

<h2 id="dwie-drogi">Dwie drogi do jednego przelewu</h2>
<div class="table-wrap"><table>
<thead><tr><th scope="col">Sposób</th><th scope="col">Co wpisujesz</th><th scope="col">Zaleta</th><th scope="col">Ograniczenie</th></tr></thead>
<tbody>
<tr><td>Kilka numerów KSeF</td><td>numery oddzielone separatorem</td><td>nic nie trzeba generować</td><td>pole tytułu ma zwykle 140 znaków</td></tr>
<tr><td>Identyfikator zbiorczy</td><td>jeden ciąg 35 znaków</td><td>mieści wiele faktur</td><td>trzeba go wygenerować w KSeF</td></tr>
</tbody></table></div>

<h2 id="kilka-numerow">Kilka numerów w tytule – ile się zmieści</h2>
<p>Numer KSeF ma 35 znaków. Zwykłe pole tytułu przelewu w wielu bankach ma 140 znaków, na przykład w specyfikacji mBanku pole Ustrd ma 140 znaków. Policzmy: trzy numery to 105 znaków, dwa separatory (przecinek i spacja zajmują po 2 znaki, razem 4, jeśli używasz „, ”) dają 109. Czwarty numer nie zmieści się już razem z separatorami, bo dodałby kolejne 37 znaków i przekroczyłby 140. W praktyce więc jednym zwykłym przelewem opiszesz do trzech faktur. Ile dokładnie mieści Twój bank, sprawdź w formularzu, bo część banków skraca lub dzieli tytuł inaczej.</p>
<div class="table-wrap"><table>
<thead><tr><th scope="col">Liczba numerów</th><th scope="col">Znaki numerów</th><th scope="col">Separatory „, ”</th><th scope="col">Razem</th></tr></thead>
<tbody>
<tr><td>1</td><td>35</td><td>0</td><td>35</td></tr>
<tr><td>2</td><td>70</td><td>2</td><td>72</td></tr>
<tr><td>3</td><td>105</td><td>4</td><td>109</td></tr>
<tr><td>4</td><td>140</td><td>6</td><td>146</td></tr>
</tbody></table></div>
<p>Cztery numery dają 146 znaków, czyli więcej niż 140. Bez żadnego dodatkowego tekstu limit przekracza więc już czwarta faktura, nawet gdy zrezygnujesz ze spacji i użyjesz samych przecinków, bo 140 + 3 = 143.</p>

<h2 id="zbiorczy">Identyfikator zbiorczy – rozwiązanie dla większej liczby faktur</h2>
<p>Identyfikator zbiorczy ma budowę podobną do numeru KSeF: <code>9999999999-IZRRRRMM-FFFFFFFFFFFF-FF</code>, czyli NIP, oznaczenie IZ z rokiem i miesiącem, 12 znaków części technicznej i dwie cyfry sumy kontrolnej. Oficjalny przykład z dokumentacji to <code>1111111111-IZ202607-65ED02180000-E7</code>. Według informacji MF jeden identyfikator może obejmować do 500 numerów KSeF (w Aplikacji Podatnika do 50), a wszystkie faktury w nim muszą mieć tego samego sprzedawcę. Jedna faktura może znaleźć się w co najwyżej 132 identyfikatorach zbiorczych w danym kontekście.</p>
<p>Ważne: identyfikator generuje się w systemie KSeF. Strona nie ma więc możliwości sama go „wymyślić” – nasz walidator sprawdza tylko format i sumę kontrolną, a nie to, jakie faktury identyfikator obejmuje. Szerzej opisujemy to w tekście <a href="/blog/jak-wygenerowac-identyfikator-zbiorczy-ksef/">jak wygenerować identyfikator zbiorczy KSeF</a>.</p>

<h2 id="przyklad">Przykład: trzy faktury od jednego dostawcy</h2>
<ol class="steps">
<li>Masz trzy faktury od tego samego sprzedawcy i chcesz zapłacić jednym przelewem.</li>
<li>Skopiuj z każdej numer KSeF (nie przepisuj ręcznie).</li>
<li>Sprawdź każdy numer w walidatorze lub wklej wszystkie naraz w <a href="/sprawdz-wiele-numerow-ksef/">sprawdzarce wielu numerów</a>.</li>
<li>Jeśli numery mieszczą się w 140 znakach, wpisz je w tytule, oddzielone przecinkami.</li>
<li>Jeśli faktur jest więcej, poproś o identyfikator zbiorczy albo wygeneruj go samodzielnie w KSeF i wpisz jego jeden ciąg.</li>
</ol>

<h2 id="kiedy">Kiedy osobne przelewy są prostsze</h2>
<p>Jeśli faktury mają różnych sprzedawców, jeden identyfikator zbiorczy ich nie obejmie, bo wymaga wspólnego sprzedawcy. Wtedy robisz osobne przelewy albo, gdy płacisz jednemu odbiorcy, kilka numerów w tytule. Przy płatności w mechanizmie podzielonej płatności obowiązuje osobny format komunikatu, który opisujemy w tekście o <a href="/blog/numer-ksef-w-przelewie-mpp/">numerze KSeF w przelewie MPP</a>.</p>
<h2 id="uwagi">Praktyczne uwagi</h2>
<p>Przed wysłaniem przelewu porównaj kwotę z sumą faktur i upewnij się, że rachunek odbiorcy jest na białej liście. Numer KSeF w tytule nie zastępuje tych kontroli. Dobrym nawykiem jest zapisanie w arkuszu, które numery trafiły do którego przelewu, bo ułatwi to późniejsze uzgadnianie wyciągu. Pamiętaj, że przy zapłacie kilku faktur jednym przelewem część programów księgowych dopasowuje płatności po numerze, więc kolejność i separator warto utrzymać zawsze taki sam.</p>
<h2 id="przyklad-liczb">Przykład z kwotami</h2>
<p>Załóżmy, że od jednego dostawcy masz trzy faktury: na 1 230,00 zł, 2 460,00 zł i 615,00 zł brutto. Suma to 4 305,00 zł. Robisz jeden przelew na 4 305,00 zł, a w tytule wpisujesz trzy numery KSeF oddzielone przecinkami. Dostawca widzi jedną wpłatę i trzy numery, więc bez trudu przypisze ją do właściwych dokumentów. Gdyby faktur było dziesięć, w polu 140 znaków zmieściłyby się tylko trzy numery, więc lepszy będzie identyfikator zbiorczy obejmujący wszystkie dziesięć.</p>
<div class="table-wrap"><table>
<thead><tr><th scope="col">Faktura</th><th scope="col">Kwota brutto</th><th scope="col">W tytule</th></tr></thead>
<tbody>
<tr><td>Pierwsza</td><td>1 230,00 zł</td><td>numer KSeF 1</td></tr>
<tr><td>Druga</td><td>2 460,00 zł</td><td>numer KSeF 2</td></tr>
<tr><td>Trzecia</td><td>615,00 zł</td><td>numer KSeF 3</td></tr>
<tr><td><strong>Razem</strong></td><td><strong>4 305,00 zł</strong></td><td>109 znaków tytułu</td></tr>
</tbody></table></div>
<h2 id="niezaplacone">Częściowa zapłata i korekty</h2>
<p>Jeśli płacisz tylko część należności, przelew z kilkoma numerami nie pokaże, którą fakturę opłacasz w całości. W takiej sytuacji zwykle prościej jest zapłacić oddzielnie za każdą fakturę albo uzgodnić z kontrahentem sposób opisu. Gdy do faktury wystawiono korektę, sprawdź, który numer KSeF należy podać, o czym piszemy w tekście o <a href="/blog/numer-ksef-faktury-korygujacej/">numerze KSeF faktury korygującej</a>. Pamiętaj też o fakturach zaliczkowych, które mają własne numery, jak w tekście o <a href="/blog/numer-ksef-faktury-zaliczkowej/">numerze KSeF faktury zaliczkowej</a>.</p>
<h2 id="program">Przelewy zbiorcze z programu księgowego</h2>
<p>Wiele programów księgowych potrafi przygotować paczkę przelewów do importu do banku. Zanim zaczniesz z niej korzystać po 1 stycznia 2027, sprawdź, czy program wstawia numer KSeF do tytułu każdego przelewu i czy nie ucina tytułu po 140 znakach. Dobrym testem jest wygenerowanie jednego przelewu na małą kwotę i obejrzenie tytułu w banku przed wysłaniem całej paczki.</p>
<p>Numery KSeF trafiają też do ewidencji VAT. Zobacz <a href="/blog/czy-numer-ksef-musi-byc-w-jpk/">czy numer KSeF musi być w JPK_VAT</a>.</p>
<h2 id="podsumowanie">Podsumowanie</h2>
<p>Do trzech faktur zwykle zmieszczą się w tytule jako osobne numery KSeF, a przy większej liczbie zostaje identyfikator zbiorczy. Każdy ciąg sprawdzisz w <a href="/identyfikator-zbiorczy-ksef/">walidatorze identyfikatora zbiorczego</a>.</p>
""",
    faq=[
        ("Czy za kilka faktur KSeF można zrobić jeden przelew?", "Tak. Według Ministerstwa Finansów w tytule można podać zbiorczy identyfikator albo kilka numerów KSeF, z uwzględnieniem limitu pola tytułu."),
        ("Ile faktur opłacisz jednym przelewem w polu 140 znaków?", "Przy polu 140 znaków zwykle trzy: 3 × 35 znaków plus separatory dają około 109 znaków. Czwarty przekroczyłby limit."),
        ("Czy identyfikator zbiorczy obejmie faktury od różnych sprzedawców?", "Nie. Według informacji MF wszystkie faktury w jednym identyfikatorze zbiorczym muszą mieć tego samego sprzedawcę."),
        ("Ile faktur obejmie identyfikator zbiorczy?", "Do 500 numerów KSeF, a w Aplikacji Podatnika do 50, według informacji Ministerstwa Finansów."),
    ],
    sources=[MF_NUM, MF_TERM, IZ_PDF, MBANK_SPEC],
)

C11 = dict(
    slug="jak-wygenerowac-identyfikator-zbiorczy-ksef",
    title="Jak wygenerować identyfikator zbiorczy KSeF?",
    desc="Identyfikator zbiorczy KSeF – czym jest, jak wygląda, limity (500 numerów, 132 identyfikatory) i dlaczego generuje się go w systemie KSeF. Przykład i FAQ.",
    h1="Jak wygenerować identyfikator zbiorczy KSeF – krok po kroku",
    intro="Identyfikator zbiorczy pozwala opisać jednym ciągiem znaków płatność za wiele faktur. Wyjaśniamy, kto go tworzy, jak jest zbudowany i co możesz sprawdzić samodzielnie.",
    lead_tool=("/identyfikator-zbiorczy-ksef/", "walidator identyfikatora zbiorczego"),
    date=("2026-11-17", "17 listopada 2026"),
    content="""
<h2 id="co-to">Czym jest identyfikator zbiorczy</h2>
<p>To ciąg znaków generowany przez KSeF, który reprezentuje zestaw numerów KSeF faktur. Zamiast wpisywać w tytule przelewu każdy numer osobno, wpisujesz jeden identyfikator. Po stronie sprzedawcy system wie, które faktury za nim stoją. Jeżeli masz już identyfikator, sprawdzisz jego zapis w <a href="/identyfikator-zbiorczy-ksef/">walidatorze identyfikatora zbiorczego</a>.</p>

<h2 id="budowa">Budowa identyfikatora</h2>
<p>Według grafiki Ministerstwa Finansów wzór to <code>9999999999-IZRRRRMM-FFFFFFFFFFFF-FF</code>. Oficjalny przykład z dokumentacji API to <code>1111111111-IZ202607-65ED02180000-E7</code>.</p>
<div class="table-wrap"><table>
<thead><tr><th scope="col">Część</th><th scope="col">Przykład</th><th scope="col">Znaczenie</th></tr></thead>
<tbody>
<tr><td>NIP</td><td class="mono">1111111111</td><td>10 cyfr</td></tr>
<tr><td>IZ + rok i miesiąc</td><td class="mono">IZ202607</td><td>oznaczenie IZ, rok 2026, miesiąc 07</td></tr>
<tr><td>Część techniczna</td><td class="mono">65ED02180000</td><td>12 znaków</td></tr>
<tr><td>Suma kontrolna</td><td class="mono">E7</td><td>2 znaki, liczone automatycznie</td></tr>
</tbody></table></div>
<p>Zwróć uwagę, że zamiast daty (8 cyfr) jest oznaczenie IZ i rok z miesiącem (razem też 8 znaków), więc długość całości to znów 35 znaków. Suma kontrolna jest liczona tym samym algorytmem CRC-8 co w numerze KSeF, o którym piszemy w tekście <a href="/blog/z-czego-sklada-sie-numer-ksef/">z czego składa się numer KSeF</a>.</p>

<h2 id="generowanie">Kto i jak go generuje</h2>
<p>Identyfikatora nie da się obliczyć samodzielnie, bo część techniczna jest nadawana przez system. Generuje się go przez KSeF: w Aplikacji Podatnika albo przez interfejs API w programie księgowym czy bankowym. Dokładne kroki w Twoim programie zależą od jego producenta, dlatego w instrukcji programu szukaj funkcji dotyczącej płatności lub identyfikatora zbiorczego. Ministerstwo Finansów podaje przy tym limity:</p>
<div class="table-wrap"><table>
<thead><tr><th scope="col">Limit</th><th scope="col">Wartość</th></tr></thead>
<tbody>
<tr><td>Numerów KSeF w jednym identyfikatorze</td><td>do 500</td></tr>
<tr><td>Numerów w Aplikacji Podatnika</td><td>do 50</td></tr>
<tr><td>Identyfikatorów, w których może być jedna faktura</td><td>do 132 w danym kontekście</td></tr>
<tr><td>Sprzedawcy faktur w jednym identyfikatorze</td><td>ten sam</td></tr>
</tbody></table></div>

<h2 id="co-sprawdzisz">Co możesz sprawdzić sam</h2>
<ol class="steps">
<li>Skopiuj identyfikator otrzymany od sprzedawcy lub wygenerowany w systemie.</li>
<li>Wklej go do <a href="/identyfikator-zbiorczy-ksef/">walidatora</a>: sprawdzi długość, NIP, oznaczenie IZ, rok i miesiąc oraz sumę kontrolną.</li>
<li>Porównaj NIP w identyfikatorze z NIP sprzedawcy z faktur.</li>
<li>Wpisz identyfikator w tytule przelewu w całości, bez spacji w środku.</li>
</ol>
<p>Walidator nie sprawdzi, jakie faktury obejmuje identyfikator, bo ta informacja jest dostępna tylko w KSeF. Dobry wynik oznacza więc poprawny format, a nie potwierdzenie, że identyfikator istnieje.</p>

<h2 id="pomylka">Nie pomyl z IPKSeF</h2>
<p>W schemacie faktury FA(3) występuje także element IPKSeF, czyli identyfikator płatności z linku do płatności. To zupełnie inny, 13-znakowy ciąg: trzy cyfry i dziesięć znaków alfanumerycznych. Nie jest identyfikatorem zbiorczym i nie wpisuje się go w tytule przelewu zamiast numeru KSeF.</p>

<h2 id="kiedy-uzyc">Kiedy identyfikator ma sens</h2>
<p>Gdy płacisz jednemu sprzedawcy za więcej niż trzy faktury, osobne numery nie zmieszczą się w 140 znakach. Wtedy identyfikator zbiorczy jest wygodniejszy. Porównanie obu dróg znajdziesz w tekście o <a href="/blog/przelew-za-kilka-faktur-ksef/">przelewie za kilka faktur KSeF</a>. W przelewie w mechanizmie podzielonej płatności identyfikator można wpisać w pole INV, co pokazujemy w <a href="/przelew-mpp-numer-ksef/">generatorze komunikatu MPP</a>.</p>
<h2 id="przyklad-tytulu">Przykład tytułu z identyfikatorem</h2>
<p>W zwykłym przelewie wystarczy wpisać sam identyfikator, na przykład <code>1111111111-IZ202607-65ED02180000-E7</code>. Zajmuje on 35 znaków, więc w polu 140 znaków zostaje jeszcze miejsce na krótki opis, np. „zapłata za faktury z października”. W przelewie MPP identyfikator trafia do pola INV: <code>/VAT/kwota/IDC/NIP/INV/identyfikator/TXT/opis</code>. Pamiętaj, żeby kwota przelewu odpowiadała sumie faktur objętych identyfikatorem, bo to ona jest podstawą rozliczenia.</p>
<h2 id="blad">Co zrobić, gdy walidator pokazuje błąd</h2>
<p>Najczęstsze przyczyny to ucięty ciąg przy kopiowaniu, spacja na końcu lub pomyłka litery O i cyfry 0 w części technicznej. Skopiuj identyfikator jeszcze raz z systemu. Jeśli błąd się powtarza, poproś sprzedawcę o ponowne przesłanie identyfikatora. Zbiorczą weryfikację wielu pozycji naraz wykonasz w <a href="/sprawdz-wiele-numerow-ksef/">sprawdzarce wielu numerów</a>.</p>
<h2 id="przyklad-planu">Przykład: dziesięć faktur, jeden identyfikator</h2>
<p>Wyobraź sobie, że w październiku dostałeś od jednego dostawcy dziesięć faktur. Osobne numery KSeF zajęłyby 350 znaków, a pole tytułu przelewu ma zwykle 140 znaków. Dlatego prosisz o identyfikator zbiorczy albo generujesz go w KSeF dla tych dziesięciu numerów. Zamiast dziesięciu ciągów wpisujesz jeden: 35 znaków. Zostaje miejsce na krótki opis, a dostawca po otrzymaniu płatności widzi, że dotyczy ona całego zestawu.</p>
<div class="table-wrap"><table>
<thead><tr><th scope="col">Wariant</th><th scope="col">Znaki w tytule</th><th scope="col">Mieści się w 140?</th></tr></thead>
<tbody>
<tr><td>10 numerów KSeF</td><td>350 i więcej</td><td>nie</td></tr>
<tr><td>3 numery KSeF</td><td>około 109</td><td>tak</td></tr>
<tr><td>1 identyfikator zbiorczy</td><td>35</td><td>tak</td></tr>
</tbody></table></div>
<h2 id="kto-generuje">Kto powinien wygenerować identyfikator</h2>
<p>Identyfikator może powstać po stronie sprzedawcy albo kupującego, o ile ma dostęp do faktur w KSeF. Według grafiki Ministerstwa Finansów z 9 listopada 2026 pierwsza część identyfikatora to NIP sprzedawcy. W praktyce najlepiej ustalić z kontrahentem, kto go przygotowuje, żeby nie powstały dwa różne identyfikatory dla tych samych faktur. Ponieważ jedna faktura może należeć do wielu identyfikatorów (do 132 w danym kontekście), nie jest to błąd, ale komplikuje późniejsze uzgadnianie płatności.</p>
<h2 id="bezpieczenstwo">Prywatność i bezpieczeństwo</h2>
<p>Nasz walidator działa w przeglądarce i nie wysyła wpisanego identyfikatora na serwer. Sam identyfikator nie zawiera kwot ani danych nabywcy, a jedynie NIP sprzedawcy, rok i miesiąc oraz część techniczną. Mimo to nie wklejaj go w publicznych miejscach, jeśli nie ma takiej potrzeby, bo wskazuje na zestaw Twoich faktur w systemie.</p>
<h2 id="terminy">Od kiedy to ma znaczenie</h2>
<p>Ministerstwo Finansów informuje, że obowiązek podawania numeru KSeF lub identyfikatora zbiorczego w płatnościach między podatnikami czynnymi został odroczony do końca 2026 roku. Oznacza to, że od 1 stycznia 2027 roku płatności za faktury z KSeF powinny zawierać te dane. Aktualne terminy i szczegóły zawsze sprawdzaj na stronie ksef.podatki.gov.pl, bo przepisy i komunikaty mogą się zmieniać. Do tego czasu warto przećwiczyć proces na kilku przelewach, żeby pierwszego stycznia nie robić tego pod presją terminu.</p>
<h2 id="checklista">Krótka lista kontrolna</h2>
<ul>
<li>ustal, kto przygotowuje identyfikator: Ty czy sprzedawca,</li>
<li>sprawdź, czy wszystkie faktury pochodzą od tego samego sprzedawcy,</li>
<li>zweryfikuj format w walidatorze przed wysłaniem przelewu,</li>
<li>zapisz identyfikator wraz z listą faktur, których dotyczy.</li>
</ul>
<h2 id="podsumowanie">Podsumowanie</h2>
<p>Identyfikator zbiorczy tworzy KSeF, a Ty możesz sprawdzić jego format w <a href="/identyfikator-zbiorczy-ksef/">walidatorze</a>. Pamiętaj o limitach i o tym, że obejmuje faktury jednego sprzedawcy.</p>
""",
    faq=[
        ("Czy mogę sam wyliczyć identyfikator zbiorczy?", "Nie. Część techniczną nadaje system, więc identyfikator generuje się w KSeF, w Aplikacji Podatnika lub przez API w programie."),
        ("Jaki format ma identyfikator zbiorczy KSeF?", "Ma format NIP-IZRRRRMM-12 znaków-2 znaki sumy kontrolnej, np. 1111111111-IZ202607-65ED02180000-E7, razem 35 znaków."),
        ("Czy identyfikator zbiorczy to to samo co IPKSeF?", "Nie. IPKSeF to 13-znakowy identyfikator płatności z linku w fakturze FA(3), a identyfikator zbiorczy ma 35 znaków."),
        ("Czy walidator potwierdzi, że identyfikator istnieje?", "Nie. Sprawdza format i sumę kontrolną. To, jakie faktury obejmuje identyfikator, wie tylko KSeF."),
    ],
    sources=[MF_NUM, IZ_PDF, IZ_PDF2, DOC_NUM, XSD],
)

C12 = dict(
    slug="komunikat-przelewu-mpp-wzor",
    title="Komunikat przelewu MPP – wzór /VAT/ /IDC/ /INV/",
    desc="Wzór komunikatu przelewu MPP z numerem KSeF: pola /VAT/, /IDC/, /INV/ i /TXT/, format kwoty, limit 140 znaków oraz przykład krok po kroku.",
    h1="Komunikat przelewu MPP – wzór z polami /VAT/, /IDC/, /INV/ i /TXT/",
    intro="Przelew w mechanizmie podzielonej płatności ma własny format komunikatu. Pokazujemy wzór, znaczenie każdego pola i przykład z numerem KSeF.",
    lead_tool=("/przelew-mpp-numer-ksef/", "generator komunikatu MPP"),
    date=("2026-11-17", "17 listopada 2026"),
    content="""
<h2 id="wzor">Wzór komunikatu</h2>
<p>Według specyfikacji mBanku dla przelewów w formacie pain.001 komunikat MPP składa się z pól w stałej kolejności: <code>/VAT/10n,2n/IDC/14x/INV/35x/TXT/33x</code>. Całość mieści się w polu o długości do 140 znaków. Gotowy komunikat zbudujesz w <a href="/przelew-mpp-numer-ksef/">generatorze komunikatu MPP</a>, a poniżej wyjaśniamy, co znaczy każda część.</p>
<div class="table-wrap"><table>
<thead><tr><th scope="col">Pole</th><th scope="col">Co wpisać</th><th scope="col">Format</th><th scope="col">Wymagane</th></tr></thead>
<tbody>
<tr><td>/VAT/</td><td>kwota podatku VAT z przecinkiem, np. 23,00</td><td>do 10 cyfr, przecinek, 2 cyfry</td><td>tak</td></tr>
<tr><td>/IDC/</td><td>identyfikator dostawcy, czyli NIP sprzedawcy</td><td>do 14 znaków</td><td>tak</td></tr>
<tr><td>/INV/</td><td>numer KSeF faktury lub identyfikator zbiorczy</td><td>do 35 znaków</td><td>tak</td></tr>
<tr><td>/TXT/</td><td>dowolny dodatkowy opis</td><td>do 33 znaków</td><td>nie</td></tr>
</tbody></table></div>

<h2 id="zasady">Zasady z dokumentów banków</h2>
<ul>
<li>Kwota VAT musi być większa niż 0,00 i nie większa niż kwota zapłaty, a separatorem jest przecinek.</li>
<li>Pole /TXT/ jest opcjonalne, a jeśli jest użyte, ma być ostatnie.</li>
<li>Przy ręcznym wpisywaniu niektóre banki, np. Deutsche Bank, dzielą komunikat na cztery linie: /VAT/, /IDC/, /INV/ i /TXT/.</li>
<li>W imporcie Elixir lub CSV w mBanku tytuł jest dzielony na sekcje po maksymalnie 35 znaków.</li>
</ul>
<p>Co do numeru KSeF Ministerstwo Finansów wskazuje, że w komunikacie przelewu MPP podaje się między innymi numer KSeF faktury, a zamiast niego można podać identyfikator zbiorczy. Obowiązek ten według MF został odroczony do końca 2026 roku, więc dotyczy płatności od 1 stycznia 2027.</p>

<h2 id="przyklad">Przykład krok po kroku</h2>
<p>Faktura ma VAT 230,00 zł, sprzedawca ma NIP 3786417439, a numer KSeF to <code>3786417439-20260928-AB12CD34EF56-78</code> (przykładowy zapis w formacie ze specyfikacji, nie prawdziwa faktura). Komunikat wygląda tak:</p>
<p><code>/VAT/230,00/IDC/3786417439/INV/3786417439-20260928-AB12CD34EF56-78/TXT/zaplata</code></p>
<div class="table-wrap"><table>
<thead><tr><th scope="col">Część</th><th scope="col">Znaki</th></tr></thead>
<tbody>
<tr><td>/VAT/230,00</td><td>11</td></tr>
<tr><td>/IDC/3786417439</td><td>15</td></tr>
<tr><td>/INV/ + numer KSeF</td><td>40</td></tr>
<tr><td>/TXT/zaplata</td><td>12</td></tr>
<tr><td><strong>Razem</strong></td><td><strong>78</strong></td></tr>
</tbody></table></div>
<p>Całość ma 78 znaków, więc mieści się w limicie 140. Przed użyciem sprawdź numer KSeF w <a href="/">walidatorze</a>, bo błąd w polu INV to najczęstsza pomyłka.</p>

<h2 id="kroki">Jak wypełnić przelew</h2>
<ol class="steps">
<li>Wybierz w banku przelew podzielony (MPP).</li>
<li>Wpisz kwotę VAT z faktury w polu /VAT/ z przecinkiem.</li>
<li>W /IDC/ wpisz NIP sprzedawcy, w /INV/ numer KSeF lub identyfikator zbiorczy.</li>
<li>Opcjonalnie dodaj krótki opis w /TXT/ na końcu.</li>
<li>Przed wysłaniem sprawdź, czy kwota VAT nie jest większa niż kwota przelewu.</li>
</ol>
<h2 id="bank">Różnice między bankami</h2>
<p>Każdy bank ma własny formularz: jedne mają osobne pola na kwotę VAT, NIP i numer faktury, inne wymagają wpisania całego komunikatu w jednym polu tytułu. Banki zmieniają formularze w związku z KSeF (mBank opublikował komunikat o zmianach w przelewach podzielonych 19.10.2026), dlatego zanim zrobisz pierwszy przelew po nowym roku, przetestuj go na małej kwocie albo przeczytaj aktualną instrukcję swojego banku. Dokładne wymagania zawsze są po stronie banku, a nie naszego generatora.</p>
<h2 id="blad">Typowe błędy</h2>
<p>Najczęściej mylone jest wpisanie kwoty brutto w polu /VAT/ zamiast kwoty podatku, użycie kropki zamiast przecinka w kwocie oraz wpisanie numeru faktury zamiast numeru KSeF. Zdarza się też przekroczenie 33 znaków w polu /TXT/. Generator wykrywa takie sytuacje i wskazuje pole, w którym jest problem, ale ostateczną walidację wykonuje bank.</p>
<h2 id="zbiorczy">Kilka faktur w jednym przelewie MPP</h2>
<p>Gdy płacisz za kilka faktur jednego sprzedawcy, w polu INV możesz użyć identyfikatora zbiorczego, jak opisujemy w tekście o <a href="/blog/przelew-za-kilka-faktur-ksef/">przelewie za kilka faktur KSeF</a>. Kwota VAT w komunikacie powinna wtedy odpowiadać sumie podatku z wszystkich faktur objętych identyfikatorem.</p>
<h2 id="przyklad-iz">Przykład z identyfikatorem zbiorczym</h2>
<p>Przy płatności za kilka faktur jednego sprzedawcy komunikat może wyglądać tak (zapis w formacie ze specyfikacji, nie prawdziwe dane): <code>/VAT/758,09/IDC/3786417439/INV/3786417439-IZ202708-AB12CD34EF56-78/TXT/zaplata</code>. Pole INV zawiera wtedy identyfikator zbiorczy zamiast numeru KSeF pojedynczej faktury. Długość pola INV pozostaje taka sama, czyli do 35 znaków, bo identyfikator ma budowę zbliżoną do numeru KSeF.</p>
<div class="table-wrap"><table>
<thead><tr><th scope="col">Sytuacja</th><th scope="col">Co w polu INV</th></tr></thead>
<tbody>
<tr><td>Jedna faktura</td><td>numer KSeF faktury</td></tr>
<tr><td>Kilka faktur jednego sprzedawcy</td><td>identyfikator zbiorczy</td></tr>
<tr><td>Faktura bez numeru KSeF (poza systemem)</td><td>zgodnie z zasadami banku i przepisów, sprawdź instrukcję</td></tr>
</tbody></table></div>
<h2 id="przekazanie">Przelew własny w MPP</h2>
<p>W dokumentach banków występuje także wariant przekazania własnego, czyli przeniesienia środków między własnymi rachunkami w ramach mechanizmu podzielonej płatności. Wtedy kwota VAT w komunikacie może być równa kwocie przelewu. Szczegóły i dopuszczalne wartości pola IDC zależą od banku, więc zawsze sprawdź jego opis.</p>
<h2 id="kontrola">Lista kontrolna przed wysłaniem</h2>
<ul>
<li>kwota VAT zapisana z przecinkiem i większa od zera,</li>
<li>NIP w polu IDC bez myślników i spacji,</li>
<li>numer KSeF skopiowany z faktury i sprawdzony w walidatorze,</li>
<li>tekst w polu TXT nie dłuższy niż 33 znaki,</li>
<li>całość nie dłuższa niż 140 znaków.</li>
</ul>
<h2 id="przechowywanie">Jak zapisać wzór na przyszłość</h2>
<p>Jeśli regularnie płacisz tym samym dostawcom w mechanizmie podzielonej płatności, warto przygotować szablony: stały NIP w polu IDC i krótki opis w polu TXT. Zmieniać będziesz tylko kwotę VAT i numer KSeF. Dzięki temu rzadziej pomylisz kolejność pól, a każdy przelew zajmie mniej czasu. Szablon możesz skopiować z generatora i wkleić do notatnika lub do arkusza, w którym prowadzisz płatności.</p>
<p>Zwróć uwagę na to, że bank może odrzucić przelew, w którym kolejność pól jest inna niż we wzorze. W dokumentach mBanku kolejność VAT, IDC, INV, TXT jest ściśle określona, a pole TXT może wystąpić tylko na końcu. Jeśli więc dostajesz komunikat błędu, sprawdź najpierw kolejność, potem format kwoty, a na końcu długość poszczególnych pól.</p>
<h2 id="dlaczego">Po co ten format</h2>
<p>Stała struktura komunikatu pozwala bankowi i systemowi rozliczeń automatycznie odczytać kwotę podatku, NIP dostawcy i numer dokumentu. Dzięki temu kwota VAT trafia na rachunek VAT sprzedawcy, a reszta na jego rachunek podstawowy. Jeśli któreś pole jest błędne, bank może odrzucić przelew albo zapytać o poprawkę, dlatego warto poświęcić minutę na kontrolę przed wysłaniem. Pomocna bywa też zasada: najpierw sprawdź numer KSeF, potem kwotę VAT, a dopiero na końcu opis.</p>
<h2 id="podsumowanie">Podsumowanie</h2>
<p>Komunikat MPP ma stałą kolejność pól: VAT, IDC, INV i opcjonalnie TXT. Zbuduj go w <a href="/przelew-mpp-numer-ksef/">generatorze komunikatu MPP</a> i zawsze sprawdź zasady swojego banku.</p>
""",
    faq=[
        ("Jak wygląda komunikat przelewu MPP?", "Ma postać /VAT/kwota VAT/IDC/NIP sprzedawcy/INV/numer KSeF/TXT/opis, przy czym pole TXT jest opcjonalne."),
        ("Jaki separator kwoty w polu /VAT/?", "Przecinek, np. 230,00. Kwota ma być większa od zera i nie większa niż kwota przelewu."),
        ("Czy w polu /INV/ można podać identyfikator zbiorczy?", "Tak. Ministerstwo Finansów wskazuje, że zamiast numeru KSeF można podać identyfikator zbiorczy."),
        ("Ile znaków może mieć komunikat MPP?", "Według specyfikacji mBanku całość mieści się w polu do 140 znaków, a pole /TXT/ ma do 33 znaków."),
    ],
    sources=[MBANK_SPEC, MBANK_IMPORT, MBANK_NEWS, DB, MF_NUM],
)


# ---------------------------------------------------------------- #13-15 (2026-11-18)
from sources import QR_DOC, MF_QR
C13 = dict(
    slug="kod-qr-ksef-jak-sprawdzic-fakture",
    title="Kod QR KSeF – jak sprawdzić fakturę telefonem?",
    desc="Jak sprawdzić fakturę z kodem QR KSeF telefonem: co zobaczysz po zeskanowaniu, jak rozpoznać adres MF, czym jest etykieta pod kodem i na co uważać.",
    h1="Kod QR KSeF – jak sprawdzić fakturę telefonem krok po kroku",
    intro="Dostałeś fakturę jako PDF lub wydruk z kodem QR? Możesz w kilka sekund sprawdzić, czy faktura rzeczywiście jest w KSeF. Pokazujemy, jak to zrobić bezpiecznie.",
    lead_tool=("/kod-qr-ksef/", "generator i dekoder kodu KOD I"),
    date=("2026-11-18", "18 listopada 2026"),
    content="""
<h2 id="po-co">Po co kod QR na fakturze</h2>
<p>Według dokumentacji Ministerstwa Finansów kody QR wprowadzono z myślą o sytuacjach, gdy faktura trafia do odbiorcy innym kanałem niż pobranie z API KSeF, na przykład jako PDF, wydruk albo załącznik e-mail. Każdy może wtedy sprawdzić, czy faktura znajduje się w systemie i czy nie została zmodyfikowana. Link z kodu możesz też rozłożyć na części w naszym <a href="/kod-qr-ksef/">dekoderze kodu KOD I</a>.</p>
<h2 id="kroki">Jak sprawdzić fakturę krok po kroku</h2>
<ol class="steps">
<li>Otwórz aparat w telefonie i skieruj go na kod QR na fakturze.</li>
<li>Nie klikaj od razu w link. Przeczytaj adres, który podpowiada telefon.</li>
<li>Sprawdź, czy adres zaczyna się od <code>https://qr.ksef.mf.gov.pl/</code> (środowisko produkcyjne). Adresy z <code>qr-test</code> i <code>qr-demo</code> należą do środowisk testowych i demo.</li>
<li>Otwórz link. Zobaczysz uproszczoną prezentację podstawowych danych faktury i informację, że jest w KSeF.</li>
<li>Porównaj dane z dokumentem: NIP sprzedawcy i datę wystawienia.</li>
</ol>
<p>Pełny dostęp do treści faktury, na przykład pobranie pliku XML, wymaga według dokumentacji wprowadzenia dodatkowych danych. Sama obecność faktury w systemie jest widoczna od razu.</p>
<h2 id="adresy">Adresy środowisk</h2>
<div class="table-wrap"><table>
<thead><tr><th scope="col">Środowisko</th><th scope="col">Adres kodu QR</th><th scope="col">Zastosowanie</th></tr></thead>
<tbody>
<tr><td>Testowe (TE)</td><td>qr-test.ksef.mf.gov.pl</td><td>testy integracji</td></tr>
<tr><td>Przedprodukcyjne (DEMO)</td><td>qr-demo.ksef.mf.gov.pl</td><td>próby przed produkcją</td></tr>
<tr><td>Produkcyjne (PROD)</td><td>qr.ksef.mf.gov.pl</td><td>prawdziwe faktury</td></tr>
</tbody></table></div>
<p>Na prawdziwej fakturze spodziewaj się adresu produkcyjnego. Jeśli kod prowadzi na zupełnie inną domenę, potraktuj go jak podejrzany i nie podawaj tam żadnych danych.</p>
<h2 id="etykieta">Co oznacza napis pod kodem</h2>
<p>Pod kodem QR znajduje się etykieta. Gdy numer KSeF jest znany, widać pod kodem właśnie ten numer. Gdy numeru jeszcze nie nadano, pojawia się napis <strong>OFFLINE</strong>. Dotyczy to faktur offline przed przesłaniem do systemu oraz faktur online oczekujących na numer. Numer z etykiety możesz przepisać do <a href="/">walidatora numeru KSeF</a> i sprawdzić jego poprawność.</p>
<h2 id="przyklad">Przykład linku z kodu</h2>
<p>Dokumentacja MF pokazuje przykładowy link dla środowiska testowego (dane przykładowe, nie prawdziwa faktura):</p>
<p><code>https://qr-test.ksef.mf.gov.pl/invoice/1111111111/01-02-2026/UtQp9Gpc51y-u3xApZjIjgkpZ01js-J8KflSPW8WzIE</code></p>
<div class="table-wrap"><table>
<thead><tr><th scope="col">Część linku</th><th scope="col">Znaczenie</th></tr></thead>
<tbody>
<tr><td>/invoice</td><td>kod weryfikacji faktury (KOD I)</td></tr>
<tr><td>1111111111</td><td>NIP sprzedawcy</td></tr>
<tr><td>01-02-2026</td><td>data wystawienia faktury (pole P_1), format DD-MM-RRRR</td></tr>
<tr><td>UtQp9G…WzIE</td><td>skrót SHA-256 pliku faktury w formacie Base64URL</td></tr>
</tbody></table></div>
<h2 id="uwaga">Na co uważać</h2>
<ul>
<li>Kod QR sam w sobie jest tylko linkiem. Oszust może wydrukować kod prowadzący na własną stronę, dlatego zawsze czytaj adres przed otwarciem.</li>
<li>Nie podawaj na stronie po zeskanowaniu haseł, tokenów ani danych logowania do KSeF. Weryfikacja faktury ich nie wymaga.</li>
<li>Dane z kodu porównaj z dokumentem. Zgodny NIP i data to dobry znak, ale nie zastępują sprawdzenia rachunku bankowego w innych źródłach.</li>
</ul>
<h2 id="kod2">A co z drugim kodem</h2>
<p>Na fakturach wystawionych w trybie offline mogą być dwa kody. Pierwszy (KOD I) służy do weryfikacji faktury po jej przesłaniu do KSeF, drugi (KOD II) do potwierdzenia autentyczności wystawcy. Szczegóły opisujemy w tekście <a href="/blog/kod-qr-ksef-co-zawiera/">co zawiera kod QR KSeF</a>.</p>
<h2 id="skan">Co zrobić, gdy kod się nie skanuje</h2>
<p>Zdarza się, że wydruk jest zbyt mały albo rozmazany. Spróbuj przybliżyć telefon, poprawić oświetlenie lub poprosić wystawcę o plik PDF. Dokumentacja przewiduje też, że jeśli kodu nie da się umieścić na fakturze, wystawca dostarcza go jako osobny plik graficzny lub link. Wystawca może więc przesłać sam link, który wkleisz do przeglądarki albo do naszego dekodera.</p>
<h2 id="skrot">Do czego służy skrót w linku</h2>
<p>Ostatni segment linku KOD I to skrót SHA-256 pliku faktury zapisany w formacie Base64URL. Skrót działa jak odcisk palca: ten sam plik zawsze daje ten sam wynik, a zmiana nawet jednego znaku w XML daje zupełnie inny ciąg. Dzięki temu system KSeF może powiązać link z konkretnym plikiem faktury i wykryć, że dokument został zmieniony po wystawieniu. Odbiorca nie musi liczyć skrótu ręcznie, bo robi to system po otwarciu linku, ale warto wiedzieć, skąd bierze się ten długi ciąg znaków.</p>
<h2 id="telefon-komputer">Telefon czy komputer</h2>
<p>Kod można sprawdzić także bez telefonu. Gdy dostajesz fakturę jako PDF na komputerze, najprościej skopiować link z wizualizacji, jeśli wystawca go dołączył, albo zeskanować kod ekranu telefonem. Można też użyć czytnika kodów QR w przeglądarce albo wgrać obraz do dowolnego programu, który odczytuje kody. Ważne, by przed otwarciem linku zawsze zobaczyć jego pełny adres, a nie tylko podgląd.</p>
<h2 id="co-dalej">Co zrobić, gdy dane się nie zgadzają</h2>
<ol class="steps">
<li>Nie płać faktury, dopóki nie wyjaśnisz rozbieżności.</li>
<li>Skontaktuj się z wystawcą znanym Ci kanałem, a nie numerem z samej faktury.</li>
<li>Poproś o numer KSeF i sprawdź go w <a href="/">walidatorze</a>.</li>
<li>Jeśli zależy Ci na pewności, poproś o plik XML pobrany z KSeF i porównaj dane.</li>
</ol>
<p>Pamiętaj, że niezgodność może być zwykłą pomyłką, na przykład literówką w nazwie albo inną datą wystawienia niż sprzedaży. Data w kodzie to data wystawienia z pola P_1, więc nie myl jej z datą sprzedaży ani terminem płatności.</p>
<h2 id="bezpieczenstwo-skanu">Bezpieczne skanowanie w praktyce</h2>
<p>Oszuści chętnie wykorzystują kody QR, bo użytkownik nie widzi, dokąd prowadzą. Dlatego przyjmij kilka prostych nawyków. Używaj aparatu systemowego, który pokazuje pełny adres przed otwarciem. Sprawdzaj, czy po nazwie domeny nie ma dziwnych dodatków, na przykład <code>qr.ksef.mf.gov.pl.inna-domena.pl</code>, bo liczy się końcówka przed pierwszym ukośnikiem. Nie instaluj żadnych aplikacji, o które prosi strona po zeskanowaniu kodu. Weryfikacja faktury w KSeF działa w przeglądarce i nie wymaga instalacji.</p>
<p>Jeśli faktura dotyczy dużej kwoty albo nowego kontrahenta, warto dodatkowo zadzwonić pod numer znany z innego źródła i potwierdzić numer rachunku. Kod QR potwierdza obecność faktury w systemie, ale nie odpowiada na pytanie, czy rachunek bankowy na niej jest właściwy. Z tego powodu dobrym zwyczajem jest porównywanie rachunku z poprzednimi fakturami od tego samego dostawcy.</p>
<h2 id="podsumowanie">Podsumowanie</h2>
<p>Zeskanuj kod, sprawdź adres, porównaj NIP i datę z dokumentem. Link rozłożysz na części w <a href="/kod-qr-ksef/">dekoderze KOD I</a>, a numer KSeF z etykiety sprawdzisz w <a href="/">walidatorze</a>.</p>
""",
    faq=[
        ("Jak sprawdzić fakturę po kodzie QR KSeF?", "Zeskanuj kod aparatem, sprawdź, czy adres to qr.ksef.mf.gov.pl, i otwórz link. Zobaczysz podstawowe dane faktury oraz informację o jej obecności w KSeF."),
        ("Czy po zeskanowaniu kodu trzeba się logować?", "Nie. Podstawowa weryfikacja nie wymaga logowania, a pełny dostęp do treści wymaga według dokumentacji dodatkowych danych."),
        ("Co oznacza napis OFFLINE pod kodem?", "Że numer KSeF nie został jeszcze nadany. Dotyczy faktur offline przed przesłaniem do systemu i faktur online oczekujących na numer."),
        ("Skąd mam wiedzieć, że kod nie jest fałszywy?", "Sprawdź domenę linku i porównaj NIP oraz datę z dokumentem. Kod to tylko link, więc adres zawsze trzeba przeczytać."),
    ],
    sources=[QR_DOC, MF_QR, MF_NUM],
)

C14 = dict(
    slug="kod-qr-ksef-co-zawiera",
    title="Co zawiera kod QR KSeF? KOD I i KOD II",
    desc="Co zawiera kod QR KSeF: budowa linku KOD I (NIP, data, skrót SHA-256) i KOD II (certyfikat, podpis), kiedy pojawia się który kod i jak je odróżnić.",
    h1="Co zawiera kod QR KSeF – budowa KOD I i KOD II",
    intro="Kody QR na fakturach KSeF to zwykłe linki, ale z konkretną budową. Rozkładamy na części KOD I i KOD II na podstawie dokumentacji Ministerstwa Finansów.",
    lead_tool=("/kod-qr-ksef/", "dekoder i generator KOD I"),
    date=("2026-11-18", "18 listopada 2026"),
    content="""
<h2 id="dwa-kody">Dwa rodzaje kodów</h2>
<p>Zgodnie z dokumentacją MF w trybie online na wizualizacji faktury jest jeden kod QR (KOD I). W trybie offline są dwa: KOD I do weryfikacji faktury po jej przesłaniu do KSeF oraz KOD II do potwierdzenia autentyczności wystawcy na podstawie certyfikatu KSeF. Każdy link rozłożysz w <a href="/kod-qr-ksef/">dekoderze kodu KOD I</a>.</p>
<div class="table-wrap"><table>
<thead><tr><th scope="col">Cecha</th><th scope="col">KOD I</th><th scope="col">KOD II</th></tr></thead>
<tbody>
<tr><td>Cel</td><td>weryfikacja i pobranie faktury</td><td>potwierdzenie autentyczności wystawcy</td></tr>
<tr><td>Kiedy</td><td>faktury online i offline</td><td>tylko faktury offline</td></tr>
<tr><td>Ścieżka</td><td>/invoice</td><td>/certificate</td></tr>
<tr><td>Podpis kluczem prywatnym</td><td>nie</td><td>tak, certyfikat KSeF typu Offline</td></tr>
<tr><td>Etykieta pod kodem</td><td>numer KSeF albo OFFLINE</td><td>CERTYFIKAT</td></tr>
</tbody></table></div>
<h2 id="kod1">Co zawiera KOD I</h2>
<p>Link KOD I składa się z adresu środowiska ze ścieżką <code>/invoice</code>, NIP-u sprzedawcy, daty wystawienia faktury z pola P_1 w formacie DD-MM-RRRR oraz skrótu pliku faktury obliczonego algorytmem SHA-256 w formacie Base64URL. Przykład z dokumentacji (dane testowe):</p>
<p><code>https://qr-test.ksef.mf.gov.pl/invoice/1111111111/01-02-2026/UtQp9Gpc51y-u3xApZjIjgkpZ01js-J8KflSPW8WzIE</code></p>
<p>Skrót działa jak odcisk palca pliku. Zmiana jednego znaku w XML daje zupełnie inny skrót, dlatego system może sprawdzić, czy faktura nie została zmodyfikowana.</p>
<h2 id="kod2">Co zawiera KOD II</h2>
<p>KOD II jest generowany wyłącznie dla faktur wystawianych w trybie offline (offline24, niedostępność systemu, tryb awaryjny). Link zawiera:</p>
<ul>
<li>adres środowiska ze ścieżką <code>/certificate</code>,</li>
<li>typ identyfikatora kontekstu: Nip, InternalId, NipVatUe lub PeppolId,</li>
<li>wartość identyfikatora kontekstu,</li>
<li>NIP sprzedawcy,</li>
<li>numer seryjny certyfikatu KSeF wystawcy,</li>
<li>skrót SHA-256 pliku faktury w Base64URL,</li>
<li>podpis linku kluczem prywatnym certyfikatu KSeF typu Offline, również w Base64URL.</li>
</ul>
<p>Dokumentacja podaje, że podpis może być wykonany algorytmem RSA (RSASSA-PSS, SHA-256) albo ECDSA na krzywej P-256. Podpis zapobiega sfałszowaniu linku przez kogoś, kto nie ma dostępu do certyfikatu. Certyfikat typu Authentication nie może być używany do generowania KODU II.</p>
<h2 id="przyklad">Przykład układu KOD II</h2>
<p>Układ linku w dokumentacji (dane przykładowe): <code>https://qr-test.ksef.mf.gov.pl/certificate/Nip/1111111111/1111111111/01F20A5D352AE590/UtQp9Gpc51y-u3xApZjIjgkpZ01js-J8KflSPW8WzIE/podpis</code>, gdzie w ostatnim segmencie stoi długi podpis w Base64URL. Segmenty to kolejno: typ kontekstu, wartość kontekstu, NIP sprzedawcy, numer seryjny certyfikatu, skrót faktury i podpis.</p>
<h2 id="weryfikacja">Co sprawdza system po zeskanowaniu KOD II</h2>
<ol class="steps">
<li>Czy certyfikat wystawcy istnieje w rejestrze, jest ważny i nie został odwołany ani zablokowany.</li>
<li>Czy podpis w adresie jest poprawny.</li>
<li>Czy podmiot z certyfikatu ma aktywne uprawnienia do wystawienia faktury w danym kontekście.</li>
<li>Czy kontekst ma prawo wystawiać faktury dla NIP-u sprzedawcy.</li>
</ol>
<p>Przykładowo księgowa wystawiająca fakturę w imieniu firmy musi mieć nadane prawo InvoiceWrite w kontekście tej firmy.</p>
<h2 id="etykiety">Etykiety pod kodami</h2>
<p>Pod KOD I widnieje numer KSeF, jeśli jest znany, a w przeciwnym razie napis OFFLINE. Pod KOD II znajduje się napis CERTYFIKAT. Kody muszą być zgodne z normą ISO/IEC 18004:2024. Numer z etykiety zweryfikujesz w <a href="/">walidatorze numeru KSeF</a>.</p>
<h2 id="bezpieczenstwo">Prywatny klucz tylko u wystawcy</h2>
<p>Do wygenerowania KODU II potrzebny jest klucz prywatny certyfikatu, który powinien zostać wyłącznie u wystawcy. Dlatego nasz dekoder tylko wyjaśnia budowę linku i nigdy nie prosi o klucz. Jeśli ktoś prosi Cię o klucz prywatny w zamian za sprawdzenie faktury, to nie jest oficjalna procedura.</p>
<h2 id="base64url">Czym jest Base64URL</h2>
<p>Skrót SHA-256 to 32 bajty danych. Aby dało się je bezpiecznie wstawić do adresu, kodowane są w formacie Base64URL, czyli odmianie Base64, w której zamiast znaków plus i ukośnik stosuje się myślnik i podkreślenie. Dzięki temu skrót nie psuje struktury adresu URL. Przykładowy skrót z dokumentacji, <code>UtQp9Gpc51y-u3xApZjIjgkpZ01js-J8KflSPW8WzIE</code>, ma 43 znaki i zawiera myślniki, co jest typowe dla tego formatu.</p>
<h2 id="srodowiska">Trzy środowiska, ten sam układ</h2>
<p>Układ linku jest taki sam we wszystkich środowiskach, zmienia się tylko początek adresu: qr-test.ksef.mf.gov.pl dla testów, qr-demo.ksef.mf.gov.pl dla środowiska przedprodukcyjnego i qr.ksef.mf.gov.pl dla produkcji. Dlatego przykłady z dokumentacji, które używają adresu testowego, pokazują dokładnie tę samą budowę, jaką ma link na prawdziwej fakturze.</p>
<h2 id="jak-odroznic">Jak odróżnić kody na wydruku</h2>
<p>Najłatwiej po etykiecie pod kodem. Jeśli widzisz numer KSeF albo słowo OFFLINE, to jest KOD I. Jeśli widzisz słowo CERTYFIKAT, to KOD II. Po zeskanowaniu rozpoznasz je także po ścieżce w adresie: <code>/invoice</code> dla KODU I i <code>/certificate</code> dla KODU II. Gdy na jednej fakturze są dwa kody, każdy z nich ma inną funkcję i oba warto sprawdzić.</p>
<h2 id="po-co-dwa">Po co dwa kody przy fakturach offline</h2>
<p>Faktura offline powstaje, zanim trafi do KSeF, więc w chwili wystawienia nie ma jeszcze numeru KSeF. KOD I pozwoli odbiorcy zweryfikować ją po przesłaniu do systemu, a KOD II potwierdza, że wystawił ją podmiot z ważnym certyfikatem i uprawnieniami. Bez drugiego kodu odbiorca nie miałby jak sprawdzić wystawcy, zanim faktura pojawi się w KSeF.</p>
<h2 id="przyklad-liczenie">Przykład: skąd bierze się skrót</h2>
<p>Załóżmy, że program wystawia fakturę jako plik XML. Oblicza dla niego skrót SHA-256, koduje wynik w Base64URL i wstawia do linku razem z NIP-em sprzedawcy oraz datą z pola P_1. Z tych samych trzech elementów powstaje link w KODZIE I, a w KODZIE II dochodzą jeszcze dane certyfikatu i podpis. Jeśli ktoś zmieni treść pliku, skrót przestanie pasować, więc link nie będzie wskazywał na zmienioną wersję. W naszym <a href="/kod-qr-ksef/">narzędziu KOD I</a> możesz wgrać plik XML i zobaczyć, jaki skrót i link z niego wynikają, a obliczenia odbywają się w Twojej przeglądarce.</p>
<div class="table-wrap"><table>
<thead><tr><th scope="col">Element</th><th scope="col">Skąd pochodzi</th></tr></thead>
<tbody>
<tr><td>NIP sprzedawcy</td><td>dane faktury (Podmiot1)</td></tr>
<tr><td>Data wystawienia</td><td>pole P_1 faktury</td></tr>
<tr><td>Skrót SHA-256</td><td>obliczany z całego pliku XML</td></tr>
<tr><td>Numer seryjny certyfikatu</td><td>certyfikat KSeF typu Offline (tylko KOD II)</td></tr>
</tbody></table></div>
<h2 id="podsumowanie">Podsumowanie</h2>
<p>KOD I to link do faktury z NIP-em, datą i skrótem SHA-256, a KOD II to dodatkowy, podpisany link potwierdzający wystawcę faktury offline. Wypróbuj <a href="/kod-qr-ksef/">dekoder KOD I</a> na swoim linku.</p>
""",
    faq=[
        ("Co zawiera KOD I w KSeF?", "Adres środowiska ze ścieżką /invoice, NIP sprzedawcy, datę wystawienia z pola P_1 (DD-MM-RRRR) i skrót SHA-256 pliku faktury w formacie Base64URL."),
        ("Kiedy na fakturze jest KOD II?", "Tylko dla faktur wystawionych w trybie offline. Potwierdza autentyczność wystawcy na podstawie certyfikatu KSeF typu Offline."),
        ("Po co w KOD II jest podpis?", "Podpis kluczem prywatnym certyfikatu zapobiega sfałszowaniu linku przez podmioty bez dostępu do certyfikatu."),
        ("Jaka norma obowiązuje dla kodów QR?", "Według dokumentacji MF kod QR musi być zgodny z normą ISO/IEC 18004:2024."),
    ],
    sources=[QR_DOC, MF_QR, MF_NUM],
)

C15 = dict(
    slug="czy-kod-qr-na-fakturze-ksef-jest-obowiazkowy",
    title="Czy kod QR na fakturze KSeF jest obowiązkowy?",
    desc="Czy kod QR na fakturze KSeF jest obowiązkowy? Wyjaśniamy, kiedy kod pojawia się na wizualizacji faktury, ile kodów jest w trybie online i offline i co z PDF.",
    h1="Czy kod QR na fakturze KSeF jest obowiązkowy – kiedy się pojawia",
    intro="W KSeF faktura jest plikiem XML, więc kod QR dotyczy jej wizualizacji. Wyjaśniamy, kiedy kod się pojawia i co mówi o tym dokumentacja MF, bez zgadywania przepisów.",
    lead_tool=("/kod-qr-ksef/", "generator kodu KOD I"),
    date=("2026-11-18", "18 listopada 2026"),
    content="""
<h2 id="odpowiedz">Krótka odpowiedź</h2>
<p>Faktura ustrukturyzowana to plik XML przesłany do KSeF i to on jest dokumentem w systemie. Kod QR dotyczy wizualizacji faktury, czyli PDF-a lub wydruku przekazywanego odbiorcy. Dokumentacja Ministerstwa Finansów mówi, że w zależności od trybu wystawienia na wizualizacji umieszcza się odpowiednie kody. Dokładne wymogi prawne sprawdź w przepisach i objaśnieniach MF, a kod KOD I wygenerujesz w <a href="/kod-qr-ksef/">generatorze kodu KOD I</a>.</p>
<div class="table-wrap"><table>
<thead><tr><th scope="col">Tryb wystawienia</th><th scope="col">Kody na wizualizacji</th><th scope="col">Etykieta</th></tr></thead>
<tbody>
<tr><td>Online</td><td>jeden kod: KOD I</td><td>numer KSeF</td></tr>
<tr><td>Offline, przed wysłaniem do KSeF</td><td>dwa kody: KOD I i KOD II</td><td>OFFLINE / CERTYFIKAT</td></tr>
<tr><td>Offline, już przesłana</td><td>KOD I (z numerem KSeF) i KOD II</td><td>numer KSeF / CERTYFIKAT</td></tr>
</tbody></table></div>
<h2 id="wizualizacja">Dlaczego mowa o wizualizacji</h2>
<p>Odbiorca faktury ustrukturyzowanej pobiera ją z KSeF jako XML. Kod QR przydaje się, gdy faktura trafia do niego innym kanałem: jako PDF, wydruk lub załącznik. Wtedy może sprawdzić, czy dokument jest w systemie i czy nie został zmieniony. To właśnie ten cel opisuje dokumentacja MF.</p>
<h2 id="brak-miejsca">Gdy kodu nie da się umieścić</h2>
<p>Dokumentacja przewiduje wprost, że jeśli nie ma możliwości umieszczenia kodu bezpośrednio na fakturze, na przykład format danych tego nie pozwala, należy dostarczyć go odbiorcy jako oddzielny plik graficzny lub link. Wystawca może więc przesłać sam link, który odbiorca wklei do <a href="/kod-qr-ksef/">dekodera</a> lub przeglądarki.</p>
<h2 id="kto-generuje">Kto generuje kod</h2>
<p>Generowanie kodów, zarówno dla faktur online, jak i offline, odbywa się lokalnie w aplikacji klienta na podstawie danych z wystawionej faktury. Oznacza to, że kod tworzy program, w którym wystawiasz fakturę lub generujesz jej wizualizację, a nie sam KSeF. Jeśli korzystasz z gotowego programu do fakturowania, zwykle robi to za Ciebie.</p>
<h2 id="co-sprawdzic">Co sprawdzić w swoim programie</h2>
<ol class="steps">
<li>Czy wizualizacja PDF zawiera kod QR pod numerem KSeF.</li>
<li>Czy adres w kodzie zaczyna się od qr.ksef.mf.gov.pl (produkcja).</li>
<li>Czy przy fakturach offline program tworzy dwa kody z etykietami OFFLINE i CERTYFIKAT.</li>
<li>Czy numer pod kodem pasuje do numeru KSeF faktury w <a href="/">walidatorze</a>.</li>
</ol>
<h2 id="odbiorca">Co z odbiorcą, który kodu nie sprawdza</h2>
<p>Odbiorca nie musi skanować kodu, by faktura była w systemie, bo źródłem jest plik w KSeF. Kod jest ułatwieniem weryfikacji, szczególnie dla osób, które dostały PDF. Jeśli masz wątpliwości co do dokumentu, możesz go porównać z fragmentem XML pobranym z KSeF, a skrót SHA-256 pliku powinien zgadzać się z tym z linku.</p>
<h2 id="wizualizacja-brak">Faktura bez kodu</h2>
<p>Jeśli otrzymałeś PDF bez kodu, nie oznacza to automatycznie, że faktury nie ma w KSeF. Poproś wystawcę o numer KSeF i sprawdź jego poprawność w walidatorze. Nie zakładaj z góry niczego, o czym nie mówią oficjalne źródła: kwestie obowiązków i ewentualnych konsekwencji sprawdzaj w przepisach i komunikatach MF na ksef.podatki.gov.pl.</p>
<h2 id="gdzie-szukac">Gdzie szukać wiążących informacji</h2>
<p>Wiążące zasady wystawiania faktur ustrukturyzowanych znajdziesz w przepisach ustawy o VAT i rozporządzeniach dostępnych w Internetowym Systemie Aktów Prawnych (isap.sejm.gov.pl) oraz w objaśnieniach na stronie ksef.podatki.gov.pl. Dokumentacja techniczna z repozytorium CIRFMF opisuje natomiast, jak kody są zbudowane i kiedy je generować. W razie wątpliwości co do konkretnego przypadku najlepiej sprawdzić te źródła albo zapytać księgowego, zamiast polegać na artykułach w internecie, także tym.</p>
<h2 id="wystawca-odbiorca">Wystawca a odbiorca</h2>
<div class="table-wrap"><table>
<thead><tr><th scope="col">Rola</th><th scope="col">Co zwykle robi z kodem</th></tr></thead>
<tbody>
<tr><td>Wystawca</td><td>generuje kod w programie i umieszcza go na wizualizacji</td></tr>
<tr><td>Odbiorca z dostępem do KSeF</td><td>pobiera XML z systemu, kod nie jest konieczny</td></tr>
<tr><td>Odbiorca z samym PDF</td><td>skanuje kod, by sprawdzić fakturę w KSeF</td></tr>
</tbody></table></div>
<h2 id="przyklad-pdf">Przykład z życia</h2>
<p>Wyobraź sobie, że kontrahent wysyła Ci e-mailem PDF z fakturą na kilka tysięcy złotych. Chcesz mieć pewność, że faktura jest w KSeF, zanim zapłacisz. Skanujesz kod KOD I, widzisz adres qr.ksef.mf.gov.pl, a po otwarciu informację o obecności faktury. Numer KSeF spod kodu wpisujesz do <a href="/">walidatora</a>, który sprawdza jego długość i sumę kontrolną CRC-8. To prosty sposób na wychwycenie literówek i podróbek.</p>
<h2 id="offline">Faktury offline i kody</h2>
<p>Przy fakturach offline kody mają szczególne znaczenie, bo faktura jest wystawiona, zanim trafi do KSeF, a odbiorca często dostaje ją w formie PDF lub wydruku. KOD I pozwala mu później sprawdzić fakturę w systemie, a KOD II potwierdza wystawcę. Dokumentacja wymienia tryby offline24, niedostępność systemu i tryb awaryjny jako sytuacje, w których generuje się KOD II. Szczegółowe zasady trybów offline opisuje ksef.podatki.gov.pl, dlatego jeśli wystawiasz takie faktury, sprawdź tam aktualne wytyczne.</p>
<p>Jeśli prowadzisz niewielką firmę i fakturujesz przez gotowy program, zapytaj jego dostawcę, jak program obsługuje kody w trybie online i offline. Zwykle wystarczy potwierdzenie, że wizualizacja zawiera kod i etykietę.</p>
<h2 id="wersje">Aktualność informacji</h2>
<p>Zasady KSeF były w ostatnich miesiącach doprecyzowywane, a terminy obowiązków zależą od wielkości firmy i miesięcznej sprzedaży. Dlatego przed podjęciem decyzji warto sprawdzić aktualny komunikat na stronie ksef.podatki.gov.pl w zakładce o podstawach prawnych i kluczowych terminach. Dokumentacja techniczna kodów QR nosi datę 21 sierpnia 2025 w repozytorium CIRFMF i może być aktualizowana, więc jeśli budujesz własne rozwiązanie, śledź zmiany w repozytorium. Ten tekst opisuje stan dokumentacji, a nie zastępuje przepisów ani porady księgowego.</p>
<h2 id="narzedzie">Jak wykorzystać nasze narzędzie</h2>
<p>W <a href="/kod-qr-ksef/">narzędziu KOD I</a> wkleisz link z kodu, aby rozbić go na NIP, datę i skrót, albo wgrasz plik XML i wygenerujesz link oraz kod QR. Dane nie opuszczają przeglądarki. Narzędzie nie prosi o klucz prywatny ani o token, a KOD II tylko tłumaczy.</p>
<p>Jeśli dostałeś sam plik XML, zobacz <a href="/blog/jak-otworzyc-plik-xml-ksef/">jak otworzyć plik XML z KSeF bez programu</a>.</p>
<h2 id="podsumowanie">Podsumowanie</h2>
<p>Kod QR to element wizualizacji faktury: jeden w trybie online, dwa w trybie offline. Zasady prawne weryfikuj w źródłach MF, a link KOD I zbuduj w <a href="/kod-qr-ksef/">generatorze</a>.</p>
""",
    faq=[
        ("Czy faktura w KSeF musi mieć kod QR?", "Dokumentacja MF opisuje, że na wizualizacji faktury umieszcza się kody zależnie od trybu wystawienia. Wymogi prawne sprawdź w przepisach i objaśnieniach MF."),
        ("Ile kodów QR jest na fakturze?", "W trybie online jeden (KOD I), w trybie offline dwa: KOD I i KOD II."),
        ("Kto generuje kod QR?", "Aplikacja klienta, lokalnie, na podstawie danych z wystawionej faktury. Sam KSeF kodu na PDF nie nakłada."),
        ("Co jeśli kodu nie da się umieścić na fakturze?", "Według dokumentacji należy dostarczyć go odbiorcy jako osobny plik graficzny lub link."),
    ],
    sources=[QR_DOC, MF_QR, MF_TERM],
)

from sources import MF_PYT, MF_AP, MF_PODR2, MF_APPDF, JPK_ZN, JPK_NEWS

# ---------------------------------------------------------------- #16 (2026-11-19)
C16 = dict(
    slug="jak-otworzyc-plik-xml-ksef",
    title="Jak otworzyć plik XML z KSeF bez programu?",
    desc="Jak otworzyć plik XML z KSeF bez programu do fakturowania? Przeglądarka, Aplikacja Podatnika MF i nasz czytnik: gdzie szukać kwoty, rachunku i terminu.",
    h1="Jak otworzyć plik XML z KSeF bez programu – krok po kroku",
    intro="Faktura z KSeF to plik XML, który wygląda jak ściana znaczników. Pokazujemy trzy sposoby otwarcia go bez programu księgowego i wskazujemy pola, w których siedzą kwota, rachunek i termin.",
    lead_tool=("/przelew-z-faktury-xml-ksef/", "czytnik faktury XML z danymi do przelewu"),
    date=("2026-11-19", "19 listopada 2026"),
    content="""
<h2 id="odpowiedz">Krótka odpowiedź</h2>
<p>Plik XML to zwykły tekst, więc otworzysz go w przeglądarce albo w Notatniku. Wygodniej jest jednak pobrać fakturę w formie PDF z Aplikacji Podatnika KSeF albo wczytać plik do <a href="/przelew-z-faktury-xml-ksef/">czytnika faktury XML z danymi do przelewu</a>, który wyciągnie kwotę, rachunek i termin. Poniżej opisujemy każdą z tych dróg.</p>
<div class="table-wrap"><table>
<thead><tr><th scope="col">Sposób</th><th scope="col">Co zobaczysz</th><th scope="col">Dla kogo</th></tr></thead>
<tbody>
<tr><td>Przeglądarka lub Notatnik</td><td>surowe znaczniki XML</td><td>ktoś, kto szuka jednej wartości</td></tr>
<tr><td>Aplikacja Podatnika KSeF</td><td>podgląd faktury i PDF</td><td>kto ma dostęp do KSeF</td></tr>
<tr><td>Czytnik z danymi do przelewu</td><td>odbiorca, rachunek, kwota, termin</td><td>kto chce zapłacić fakturę</td></tr>
</tbody></table></div>
<h2 id="przegladarka">Sposób 1: przeglądarka lub edytor tekstu</h2>
<p>Plik z rozszerzeniem .xml możesz przeciągnąć do okna przeglądarki albo kliknąć go prawym przyciskiem i wybrać „Otwórz za pomocą” Notatnika. Zobaczysz drzewo elementów w nawiasach ostrokątnych. Nic nie trzeba instalować, a plik nie jest nigdzie wysyłany. Wadą jest to, że nazwy pól są techniczne, a faktura nie wygląda jak dokument.</p>
<h2 id="aplikacja">Sposób 2: Aplikacja Podatnika KSeF</h2>
<p>Ministerstwo Finansów udostępnia bezpłatną Aplikację Podatnika KSeF 2.0, w której można wystawiać, odbierać i przeglądać faktury. Według podręcznika użytkownika na liście faktur zaznaczasz fakturę i wybierasz format z przycisku „Pobierz”. Nazwa pobranego pliku jest zgodna z numerem KSeF faktury. W jednej operacji można pobrać od 1 do 10 faktur, a przy kilku system zapisuje je jako archiwum ZIP. Kliknięcie numeru KSeF na liście otwiera ekran ze szczegółami: sprzedawca, nabywca, pozycje i pozostałe dane.</p>
<p>Wizualizacja nie ma jednego obowiązującego wzoru. Podręcznik MF zaznacza, że dostawcy programów mogą tworzyć własne wzory, a e-fakturę można zwizualizować także w bezpłatnych narzędziach ministerstwa.</p>
<h2 id="czytnik">Sposób 3: czytnik z danymi do przelewu</h2>
<p>Jeśli chcesz tylko zapłacić, wczytaj plik do <a href="/przelew-z-faktury-xml-ksef/">naszego czytnika</a>. Odczyt odbywa się lokalnie w przeglądarce. Narzędzie pokaże sprzedawcę, numer rachunku, kwotę, termin oraz przygotuje tytuł przelewu z numerem KSeF. Gdy numeru nie ma w nazwie pliku, wpisujesz go ręcznie, a my sprawdzamy jego sumę kontrolną.</p>
<h2 id="pola">Gdzie w XML są najważniejsze dane</h2>
<div class="table-wrap"><table>
<thead><tr><th scope="col">Element XML</th><th scope="col">Co oznacza</th></tr></thead>
<tbody>
<tr><td>Podmiot1</td><td>sprzedawca (dane identyfikacyjne i adres)</td></tr>
<tr><td>Podmiot2</td><td>nabywca</td></tr>
<tr><td>P_1</td><td>data wystawienia faktury</td></tr>
<tr><td>P_2</td><td>kolejny numer faktury nadany przez wystawcę</td></tr>
<tr><td>P_15</td><td>kwota należności ogółem</td></tr>
<tr><td>NrRB</td><td>pełny numer rachunku bankowego</td></tr>
<tr><td>Termin</td><td>termin płatności</td></tr>
</tbody></table></div>
<p>Opisy pochodzą ze schematu FA(3) opublikowanego przez Ministerstwo Finansów. Warto zapamiętać, że P_2 to numer nadany przez wystawcę, a numer KSeF to zupełnie inna wartość.</p>
<h2 id="przyklad">Przykład: szukamy kwoty i rachunku</h2>
<p>Dostałeś plik faktura.xml od dostawcy. Otwierasz go w przeglądarce i używasz wyszukiwania na stronie (Ctrl+F). Wpisujesz „P_15” i znajdujesz kwotę należności ogółem. Wpisujesz „NrRB” i widzisz numer rachunku. Wpisujesz „Termin” i trafiasz na datę płatności. W ten sposób w minutę masz dane do przelewu, choć trzeba uważać, bo na fakturze może być kilka rachunków lub kilka terminów, a przy fakturach w walucie obcej kwoty podatku są w osobnych polach.</p>
<h2 id="uwagi">Na co uważać</h2>
<ol class="steps">
<li>Sprawdź, czy plik to faktura FA(3). W nagłówku znajdziesz kod systemowy „FA (3)” i wersję schematu 1-0E.</li>
<li>Nie edytuj pliku w edytorze tekstu i nie zapisuj go ponownie. Zmiana choćby jednego znaku zmienia jego skrót, a ten jest podstawą kodu QR.</li>
<li>Nie wysyłaj faktur do przypadkowych stron internetowych. Wybieraj narzędzia, które, jak nasze, czytają plik lokalnie.</li>
<li>Numer KSeF nie jest elementem pliku. Wyjaśniamy to w tekście <a href="/blog/dlaczego-numeru-ksef-nie-ma-w-xml/">Dlaczego numeru KSeF nie ma w pliku XML</a>.</li>
</ol>
<h2 id="problemy">Najczęstsze problemy z otwarciem pliku</h2>
<div class="table-wrap"><table>
<thead><tr><th scope="col">Objaw</th><th scope="col">Co zrobić</th></tr></thead>
<tbody>
<tr><td>Plik ma rozszerzenie .zip</td><td>rozpakuj archiwum, bo kilka faktur z Aplikacji Podatnika jest zapisywanych jako ZIP</td></tr>
<tr><td>Polskie litery wyglądają dziwnie</td><td>ustaw w edytorze kodowanie UTF-8, które jest standardem dla XML</td></tr>
<tr><td>Cały plik jest w jednej linii</td><td>otwórz go w przeglądarce, która pokaże elementy w drzewie, i użyj Ctrl+F</td></tr>
<tr><td>Brakuje numeru KSeF</td><td>numer jest w nazwie pliku lub w UPO, a nie w treści XML</td></tr>
</tbody></table></div>
<p>Jeśli plik mimo to się nie otwiera, pobierz go jeszcze raz z Aplikacji Podatnika albo poproś wystawcę o ponowne wysłanie. Pamiętaj, że oryginałem faktury jest dokument w KSeF, a plik z e-maila to tylko jego kopia, którą można zawsze zweryfikować przez numer KSeF.</p>
<h2 id="pdf">Co z PDF-em</h2>
<p>Gdy fakturę trzeba przekazać komuś, kto nie ma dostępu do KSeF, korzysta się z wizualizacji, na przykład pliku PDF. Pytania i odpowiedzi MF wskazują, że wizualizacja powinna mieć kod QR, jeśli faktura jest przekazywana poza KSeF. Kod sprawdzisz w <a href="/kod-qr-ksef/">dekoderze kodu QR</a>.</p>
<h2 id="rodzaje">Nie każdy XML to faktura FA(3)</h2>
<p>W KSeF funkcjonują też inne struktury, na przykład faktury VAT RR w strukturze FA_RR. Aplikacja Podatnika obsługuje obie, ale nasz czytnik jest przygotowany do faktur FA(3), czyli zwykłych faktur sprzedaży. Jeśli w nagłówku widzisz inny kod formularza, dane do przelewu trzeba odczytać ręcznie albo w programie, który tę strukturę obsługuje. To samo dotyczy plików, które nie są fakturami, na przykład XML z potwierdzeniem odbioru.</p>
<h2 id="narzedzie">Jak wykorzystać nasze narzędzie</h2>
<p>W <a href="/przelew-z-faktury-xml-ksef/">czytniku faktury XML</a> upuszczasz plik, a w kilka sekund dostajesz gotową kartę płatności z przyciskami „Kopiuj”. Jeśli faktura ma adnotację podzielonej płatności, narzędzie przygotuje także komunikat MPP. Pliki czyta tylko Twoja przeglądarka.</p>
<h2 id="podsumowanie">Podsumowanie</h2>
<p>XML otworzysz w przeglądarce, ale do codziennej pracy lepsza jest Aplikacja Podatnika albo <a href="/przelew-z-faktury-xml-ksef/">czytnik danych do przelewu</a>. Kluczowe pola to P_15, NrRB i Termin.</p>
""",
    faq=[
        ("Czym otworzyć plik XML z KSeF?", "Wystarczy przeglądarka internetowa albo Notatnik, bo XML to zwykły tekst. Do wygodnego podglądu użyj Aplikacji Podatnika KSeF albo czytnika, który wyciąga dane do przelewu."),
        ("Czy mogę pobrać fakturę z KSeF jako PDF?", "Tak. Według podręcznika MF w Aplikacji Podatnika wybierasz fakturę na liście i format z przycisku „Pobierz”, a wizualizacja jest dostępna jako PDF."),
        ("Czy plik XML z KSeF można edytować?", "Nie powinno się tego robić. Faktura w KSeF jest dokumentem w systemie, a każda zmiana pliku zmienia jego skrót, więc kopia przestaje być zgodna z oryginałem."),
        ("Czy wczytanie XML do czytnika jest bezpieczne?", "W naszym czytniku plik jest odczytywany lokalnie w przeglądarce i nie jest wysyłany na serwer."),
    ],
    sources=[MF_APPDF, MF_PODR2, MF_PYT, MF_FA3, XSD],
)

# ---------------------------------------------------------------- #17 (2026-11-19)
C17 = dict(
    slug="dlaczego-numeru-ksef-nie-ma-w-xml",
    title="Dlaczego numeru KSeF nie ma w pliku XML faktury?",
    desc="Dlaczego numeru KSeF nie ma w pliku XML faktury? Wyjaśniamy, kiedy system go nadaje, czym różni się od P_2 i gdzie go znaleźć: UPO, lista faktur, nazwa pliku.",
    h1="Dlaczego numeru KSeF nie ma w pliku XML faktury – i gdzie go znaleźć",
    intro="Otwierasz fakturę XML, szukasz numeru KSeF i go nie widzisz. To nie błąd: według Ministerstwa Finansów numer nie jest elementem pliku. Wyjaśniamy dlaczego i gdzie go wziąć.",
    lead_tool=("/", "walidator numeru KSeF"),
    date=("2026-11-19", "19 listopada 2026"),
    content="""
<h2 id="odpowiedz">Krótka odpowiedź</h2>
<p>Numer KSeF nadaje system dopiero po wysłaniu faktury i jej przyjęciu. Ministerstwo Finansów pisze wprost, że numer jest zwracany w UPO i sam w sobie nie stanowi elementu pliku XML. Gdy już go masz, sprawdź go w <a href="/">walidatorze numeru KSeF</a>. Pole P_2 w pliku to inny numer, nadany przez wystawcę.</p>
<div class="table-wrap"><table>
<thead><tr><th scope="col">Cecha</th><th scope="col">Numer KSeF</th><th scope="col">Pole P_2</th></tr></thead>
<tbody>
<tr><td>Kto nadaje</td><td>system KSeF</td><td>wystawca faktury</td></tr>
<tr><td>Kiedy</td><td>po przyjęciu faktury</td><td>przy wystawianiu</td></tr>
<tr><td>Czy jest w XML</td><td>nie</td><td>tak</td></tr>
<tr><td>Długość</td><td>zawsze 35 znaków</td><td>dowolna, wg serii wystawcy</td></tr>
</tbody></table></div>
<h2 id="dlaczego">Dlaczego numeru nie da się wpisać do pliku</h2>
<p>Plik XML powstaje po stronie wystawcy, jeszcze przed wysłaniem do systemu. Numer KSeF składa się z NIP-u sprzedawcy, daty przyjęcia faktury, części technicznej i sumy kontrolnej CRC-8. Dokumentacja MF opisuje datę jako dzień przyjęcia faktury do dalszego przetwarzania, więc w chwili tworzenia pliku jeszcze nie istnieje. Dlatego system nadaje numer sam i odsyła go w potwierdzeniu.</p>
<p>MF zaznacza też, że numer KSeF oraz numer faktury wskazywany w polu P_2 to dwa różne numery, a numer KSeF wystawianej faktury nie stanowi elementu faktury. Różnice między nimi opisujemy w artykule <a href="/blog/czy-numer-ksef-to-numer-faktury/">Czy numer KSeF to numer faktury</a>.</p>
<h2 id="wyjatki">Kiedy numer KSeF jednak pojawia się w XML</h2>
<p>Nie mówimy tu o numerze własnej faktury, ale o numerach faktur powiązanych. Schemat FA(3) zawiera pola, w których wpisuje się numer innej faktury z KSeF:</p>
<div class="table-wrap"><table>
<thead><tr><th scope="col">Element XML</th><th scope="col">Opis ze schematu</th></tr></thead>
<tbody>
<tr><td>NrKSeFFaKorygowanej</td><td>numer identyfikujący fakturę korygowaną w KSeF</td></tr>
<tr><td>NrKSeFN</td><td>znacznik faktury korygowanej wystawionej poza KSeF</td></tr>
<tr><td>NrKSeFFaZaliczkowej</td><td>numer faktury zaliczkowej w KSeF, obowiązkowy, gdy zaliczkowa była wystawiona w KSeF</td></tr>
</tbody></table></div>
<p>MF przypomina, że w fakturze rozliczającej lub ostatniej zaliczkowej trzeba podać numer KSeF faktury zaliczkowej, a w korekcie numer KSeF faktury pierwotnej. Szczegóły dla korekt znajdziesz w tekście o <a href="/blog/numer-ksef-faktury-korygujacej/">numerze KSeF faktury korygującej</a>.</p>
<h2 id="droga">Droga faktury od wystawienia do numeru</h2>
<div class="table-wrap"><table>
<thead><tr><th scope="col">Krok</th><th scope="col">Co się dzieje</th><th scope="col">Czy numer KSeF już istnieje</th></tr></thead>
<tbody>
<tr><td>1. Wystawienie</td><td>program tworzy plik XML w strukturze FA(3)</td><td>nie</td></tr>
<tr><td>2. Wysłanie</td><td>wystawca przesyła plik do KSeF</td><td>nie</td></tr>
<tr><td>3. Przyjęcie</td><td>system przyjmuje fakturę i nadaje numer</td><td>tak</td></tr>
<tr><td>4. UPO</td><td>wystawca dostaje potwierdzenie z numerem</td><td>tak</td></tr>
<tr><td>5. Odbiór</td><td>nabywca widzi fakturę w swoim koncie KSeF</td><td>tak</td></tr>
</tbody></table></div>
<p>W pytaniach i odpowiedziach MF czytamy, że fakturę uznaje się za otrzymaną przez nabywcę w chwili nadania jej numeru KSeF, a sam KSeF jest podstawowym i wystarczającym kanałem jej udostępniania. Dla krajowego nabywcy z numerem NIP e-mail z plikiem ma więc charakter pomocniczy. Dlatego brak numeru w pliku, który dostałeś od dostawcy, nie oznacza, że faktura nie istnieje. Znaczy tylko, że numer trzeba pobrać z systemu lub od wystawcy.</p>
<h2 id="gdzie">Gdzie znaleźć numer KSeF faktury</h2>
<ol class="steps">
<li>W UPO, czyli Urzędowym Poświadczeniu Odbioru, które zwraca system.</li>
<li>Na liście faktur w Aplikacji Podatnika KSeF, gdzie numer jest widoczny przy każdej fakturze i otwiera szczegóły.</li>
<li>W nazwie pobranego pliku. Podręcznik MF mówi, że nazwa pliku jest zgodna z numerem KSeF faktury.</li>
<li>Na wizualizacji faktury, jeśli program umieszcza numer pod kodem QR.</li>
</ol>
<h2 id="przyklad">Przykład: płacisz fakturę z pliku XML</h2>
<p>Dostawca przysłał plik faktura.xml. W polu P_2 widzisz „FV/11/2026/044”, ale w tytule przelewu ma się znaleźć numer KSeF. Szukasz go więc w e-mailu z fakturą, w Aplikacji Podatnika albo w nazwie pliku pobranego z systemu, na przykład 5265877635-20250826-0100001AF629-AF.xml. Kopiujesz ten fragment bez rozszerzenia i wklejasz do <a href="/">walidatora</a>. Jeśli pasuje długość i suma kontrolna, możesz go użyć w tytule przelewu.</p>
<h2 id="po-co">Po co w ogóle numer, skoro jest P_2</h2>
<p>Numer z pola P_2 jest unikalny tylko w obrębie serii wystawcy, więc dwóch sprzedawców może mieć fakturę o tym samym numerze. Numer KSeF ma zawsze 35 znaków, zawiera NIP sprzedawcy i jest globalnie unikalny, dlatego jednoznacznie wskazuje fakturę w systemie. Właśnie dlatego od 2027 roku ma trafiać do tytułu przelewu, a nie numer z faktury.</p>
<h2 id="czytnik">Czytnik XML a numer KSeF</h2>
<p>Nasz <a href="/przelew-z-faktury-xml-ksef/">czytnik faktury XML</a> bierze numer z nazwy pliku. Gdy go tam nie ma, pole można wypełnić ręcznie. To zgodne z logiką systemu: numer jest informacją o fakturze, a nie jej treścią.</p>
<h2 id="upo">Czym jest UPO i po co je zachować</h2>
<p>UPO to Urzędowe Poświadczenie Odbioru, czyli dokument, który system zwraca po przyjęciu faktury. Według MF właśnie w nim znajdziesz numer KSeF. Wystawca, który prowadzi sprzedaż przez program, powinien mieć UPO w swoich dokumentach, a Aplikacja Podatnika pozwala pobierać je dla jednej lub wielu faktur. Jeśli kontrahent pyta o numer do przelewu, wystarczy skopiować go z UPO lub z listy faktur, zamiast wysyłać mu cały plik XML.</p>
<h2 id="bledy">Typowe błędy</h2>
<ul>
<li>Wpisanie do tytułu przelewu pola P_2 zamiast numeru KSeF.</li>
<li>Szukanie numeru w pliku, który otwarto w edytorze, i uznanie, że faktura jest niekompletna.</li>
<li>Użycie numeru faktury korygowanej zamiast numeru samej korekty w płatności.</li>
<li>Pomijanie sprawdzenia sumy kontrolnej przed wpisaniem numeru ręcznie.</li>
</ul>
<h2 id="gdzie-czytac">Źródła, które warto znać</h2>
<p>Najpewniejsze są strony ksef.podatki.gov.pl, a konkretnie opis numeru KSeF i zbiorczego identyfikatora oraz dokumentacja techniczna numeru w repozytorium CIRFMF. Opisują one budowę numeru, algorytm CRC-8 i moment nadania. Ten tekst streszcza je w wersji dla osoby, która płaci fakturę, i nie zastępuje przepisów ani porady księgowego.</p>
<h2 id="podsumowanie">Podsumowanie</h2>
<p>Numeru KSeF nie ma w XML, bo nadaje go system po przyjęciu faktury. Weź go z UPO, listy faktur lub nazwy pliku i sprawdź w <a href="/">walidatorze</a>, zanim wpiszesz go do przelewu.</p>
""",
    faq=[
        ("Dlaczego w pliku XML faktury nie ma numeru KSeF?", "Według MF numer nadaje system po wysłaniu i przyjęciu faktury, jest zwracany w UPO i nie stanowi elementu pliku XML."),
        ("Czy pole P_2 to numer KSeF?", "Nie. P_2 to kolejny numer faktury nadany przez wystawcę, a numer KSeF to osobny, 35-znakowy identyfikator z systemu."),
        ("Skąd wziąć numer KSeF, gdy mam sam plik XML?", "Z UPO, z listy faktur w Aplikacji Podatnika KSeF albo z nazwy pliku pobranego z systemu, która zgodnie z podręcznikiem MF odpowiada numerowi KSeF."),
        ("Czy numer KSeF wpisuje się w fakturze korygującej?", "Tak, ale jest to numer faktury korygowanej, wpisywany w polu NrKSeFFaKorygowanej, a nie numer samej korekty."),
    ],
    sources=[MF_NUM, DOC_NUM, MF_APPDF, XSD],
)

# ---------------------------------------------------------------- #18 (2026-11-19)
C18 = dict(
    slug="czy-numer-ksef-musi-byc-w-jpk",
    title="Czy numer KSeF musi być w JPK_VAT? Oznaczenia",
    desc="Czy numer KSeF musi być w JPK_VAT? Według MF nowe JPK_V7(3) ma pole NrKSeF oraz oznaczenia OFF, BFK i DI. Sprawdź, kiedy które stosować w sprzedaży i zakupach.",
    h1="Czy numer KSeF musi być w JPK_VAT – NrKSeF, OFF, BFK i DI",
    intro="Nowa struktura JPK_V7(3) ma pole na numer KSeF i trzy oznaczenia na faktury bez numeru. Wyjaśniamy, co mówi o nich Ministerstwo Finansów i jak sprawdzić listę numerów przed wysyłką pliku.",
    lead_tool=("/sprawdz-wiele-numerow-ksef/", "sprawdzanie wielu numerów KSeF naraz"),
    date=("2026-11-19", "19 listopada 2026"),
    content="""
<h2 id="odpowiedz">Krótka odpowiedź</h2>
<p>Tak, w nowej wersji JPK_VAT z deklaracją przy fakturach wykazuje się numer KSeF albo oznaczenie wskazujące, dlaczego go nie ma. Ministerstwo Finansów pisze, że struktury JPK_V7M(3) i JPK_V7K(3) obowiązują od 1 lutego 2026 r., a numer KSeF wykazuje się w części ewidencyjnej, zarówno w sprzedaży, jak i w zakupach. Listę numerów sprawdzisz wcześniej w <a href="/sprawdz-wiele-numerow-ksef/">narzędziu do sprawdzania wielu numerów KSeF</a>.</p>
<div class="table-wrap"><table>
<thead><tr><th scope="col">Oznaczenie</th><th scope="col">Znaczenie według MF</th></tr></thead>
<tbody>
<tr><td>NrKSeF</td><td>numer identyfikujący fakturę w KSeF</td></tr>
<tr><td>OFF</td><td>faktura z art. 106nf ust. 1 ustawy (awaria), która w dniu złożenia ewidencji nie ma numeru KSeF</td></tr>
<tr><td>BFK</td><td>faktura elektroniczna lub papierowa wystawiona poza KSeF</td></tr>
<tr><td>DI</td><td>dowód inny niż faktura</td></tr>
</tbody></table></div>
<h2 id="nrksef">Kiedy wpisać NrKSeF</h2>
<p>Według zestawienia MF numer wpisuje się, gdy faktura została wystawiona za pośrednictwem KSeF i na dzień złożenia JPK_VAT ma nadany numer. W sprzedaży dotyczy to wszystkich trybów wystawiania, czyli także offline24, awarii i niedostępności systemu, jeśli do chwili składania pliku faktury zostały przesłane do KSeF i mają numer. Liczy się więc stan na dzień złożenia ewidencji, a nie tryb wystawienia.</p>
<h2 id="off">Kiedy OFF</h2>
<p>OFF dotyczy faktury wystawionej w trybie awarii, która w dniu złożenia ewidencji nie ma jeszcze numeru KSeF. MF zaznacza, że po uzyskaniu numeru podatnik nie ma obowiązku korygować ewidencji.</p>
<h2 id="bfk">Kiedy BFK</h2>
<p>BFK oznacza fakturę wystawioną bez użycia KSeF. Zestawienie MF podaje wśród przypadków sprzedaży między innymi faktury wystawione w trakcie awarii całkowitej, faktury wystawione w 2026 r. poza KSeF przez podatników, którzy nie mają obowiązku wystawiania faktur w KSeF, oraz faktury przy wewnątrzwspólnotowym nabyciu towarów i imporcie usług. W zakupach wymieniono między innymi faktury wystawione przy użyciu kas rejestrujących, jeśli mogą być wystawiane do 31 grudnia 2026 r.</p>
<h2 id="di">Kiedy DI</h2>
<p>DI to dowód inny niż faktura, na przykład dowód wewnętrzny albo zbiorczy dowód sprzedaży z kas. MF wymienia też faktury offline24 i wystawione w czasie niedostępności systemu, które w dniu przesłania ewidencji nie mają numeru KSeF. Jeśli faktura była udostępniona nabywcy poza KSeF i oznaczono ją DI, po uzyskaniu numeru podatnik powinien skorygować oznaczenie numerem KSeF.</p>
<h2 id="v7m-v7k">JPK_V7M czy JPK_V7K</h2>
<p>Ministerstwo Finansów opublikowało dwie nowe struktury: JPK_V7M(3) dla podatników rozliczających się miesięcznie oraz JPK_V7K(3) dla rozliczających się kwartalnie. Oznaczenia dotyczące KSeF występują w obu. Nowe wzory uwzględniają zmiany wynikające z rozporządzenia Ministra Finansów i Gospodarki z 12 grudnia 2025 r., a pole ma postać węzła KSeF w wierszach sprzedaży i zakupu.</p>
<h2 id="sprzedaz-zakupy">Sprzedaż a zakupy: czym różnią się zasady</h2>
<div class="table-wrap"><table>
<thead><tr><th scope="col">Oznaczenie</th><th scope="col">Sprzedaż</th><th scope="col">Zakupy</th></tr></thead>
<tbody>
<tr><td>NrKSeF</td><td>faktura z KSeF ma numer w dniu składania pliku</td><td>faktura z KSeF ma numer w dniu składania pliku</td></tr>
<tr><td>OFF</td><td>faktura z awarii bez numeru</td><td>faktura wystawiona w czasie awarii, bez numeru</td></tr>
<tr><td>BFK</td><td>faktury poza KSeF, np. WNT, import usług</td><td>faktury z kas, WNT, import usług i inne przypadki z zestawienia</td></tr>
<tr><td>DI</td><td>dowody inne, np. wewnętrzne, zbiorcze z kas</td><td>wszystkie pozostałe dokumenty bez numeru KSeF</td></tr>
</tbody></table></div>
<p>Zestawienie MF osobno opisuje sprzedaż i zakupy, więc przy rozliczaniu kosztów nie przenoś automatycznie reguł ze sprzedaży. Jeśli nie masz pewności, który znacznik pasuje do dokumentu, sprawdź go w aktualnym zestawieniu na podatki.gov.pl.</p>
<h2 id="przyklad">Przykład: trzy faktury kosztowe</h2>
<div class="table-wrap"><table>
<thead><tr><th scope="col">Dokument</th><th scope="col">Co wpisać w ewidencji zakupu</th></tr></thead>
<tbody>
<tr><td>Faktura z KSeF z numerem 5265877635-20250826-0100001AF629-AF</td><td>NrKSeF z tym numerem</td></tr>
<tr><td>Faktura od dostawcy zagranicznego dla importu usług</td><td>BFK</td></tr>
<tr><td>Dowód wewnętrzny</td><td>DI</td></tr>
</tbody></table></div>
<p>Przed wysyłką pliku zrób prostą kontrolę: skopiuj numery z programu księgowego i wklej je do <a href="/sprawdz-wiele-numerow-ksef/">narzędzia sprawdzającego wiele numerów</a>. Wychwycisz literówki, numery o złej długości i błędne sumy kontrolne, zanim trafią do ewidencji. Narzędzie sprawdza format i CRC-8, ale nie potwierdza istnienia faktury w systemie.</p>
<h2 id="kontrola">Lista kontrolna przed wysyłką JPK</h2>
<ol class="steps">
<li>Zbierz numery KSeF faktur sprzedaży i zakupu za okres.</li>
<li>Sprawdź format i sumę kontrolną każdego numeru.</li>
<li>Dla dokumentów bez numeru dobierz oznaczenie: OFF, BFK lub DI.</li>
<li>Po uzyskaniu numeru dla faktur oznaczonych DI sprawdź, czy ewidencję trzeba skorygować.</li>
<li>Przeczytaj aktualne objaśnienia MF, bo oznaczenia dla konkretnych sytuacji bywają doprecyzowywane.</li>
</ol>
<h2 id="nrksef-brak">Co robić, gdy numeru jeszcze nie ma</h2>
<p>Zdarza się, że faktura została wystawiona, ale w dniu składania pliku nie masz jej numeru, bo w systemie jest awaria albo dokument wysłano w trybie offline. Wtedy nie wpisujesz numeru z głowy ani ze wzoru, tylko dobierasz właściwe oznaczenie z zestawienia MF. Pamiętaj o notatce w księgach, żeby po uzyskaniu numeru sprawdzić, czy dla danego oznaczenia wymagana jest korekta. Przy OFF jej nie trzeba robić, a przy DI w opisanym wyżej przypadku powinna nastąpić.</p>
<h2 id="aktualnosc">Aktualność informacji</h2>
<p>Zestawienie MF ma numer wersji, a jedna z poprawek usunęła przypadek użycia BFK przy imporcie towarów. Pokazuje to, że zasady doprecyzowuje się w trakcie. Dlatego w razie wątpliwości otwórz aktualną wersję dokumentu na podatki.gov.pl albo zapytaj księgowego. Ten artykuł streszcza wersję 1.1 i nie zastępuje przepisów.</p>
<h2 id="co-z-platnoscia">A płatność za fakturę</h2>
<p>Numer w JPK_VAT to coś innego niż numer w tytule przelewu. Obowiązek podawania numeru w płatności między czynnymi podatnikami dotyczy płatności od 1 stycznia 2027 r. Szczegóły opisujemy w tekście <a href="/blog/czy-numer-ksef-musi-byc-w-tytule-przelewu/">Czy numer KSeF musi być w tytule przelewu</a>.</p>
<h2 id="podsumowanie">Podsumowanie</h2>
<p>W JPK_V7(3) przy fakturze wpisujesz numer KSeF albo oznaczenie OFF, BFK lub DI. Zanim wyślesz plik, wklej numery do <a href="/sprawdz-wiele-numerow-ksef/">sprawdzarki wielu numerów</a> i porównaj z objaśnieniami MF.</p>
""",
    faq=[
        ("Czy numer KSeF trzeba podawać w JPK_VAT?", "Według MF w JPK_V7M(3) i JPK_V7K(3), obowiązujących od 1 lutego 2026 r., w części ewidencyjnej wykazuje się numer KSeF faktury albo oznaczenie OFF, BFK lub DI."),
        ("Co oznacza oznaczenie OFF w JPK_VAT?", "Dotyczy faktury wystawionej w trybie awarii, która w dniu złożenia ewidencji nie ma numeru KSeF. Po jego uzyskaniu nie trzeba korygować ewidencji."),
        ("Kiedy stosuje się BFK, a kiedy DI?", "BFK to faktura wystawiona poza KSeF, a DI to dowód inny niż faktura, w tym faktura offline24 bez numeru w dniu wysyłki. Listę przypadków znajdziesz w zestawieniu MF."),
        ("Czy narzędzie potwierdzi, że faktura jest w KSeF?", "Nie. Nasza sprawdzarka weryfikuje format numeru i sumę kontrolną CRC-8, a istnienie faktury potwierdza dopiero KSeF."),
    ],
    sources=[JPK_ZN, JPK_NEWS, MF_NUM, MF_TERM],
)

# ---------------------------------------------------------------- #19-21 (2026-11-20)
KPIR_ROZ = ("Rozporządzenie MFiG z 6 września 2025 r. w sprawie prowadzenia podatkowej księgi przychodów i rozchodów (Dz.U. 2025 poz. 1299) – ISAP", "https://isap.sejm.gov.pl/isap.nsf/DocDetails.xsp?id=WDU20250001299", "")
KPIR_BROSZ = ("podatki.gov.pl: broszura informacyjna JPK_PKPIR", "https://www.podatki.gov.pl/media/pbqdgqcp/broszura_informacyjna_dot_jpk_pkpir-3.pdf", "")
MF_PYT2 = ("Ministerstwo Finansów: Pytania i odpowiedzi KSeF 2.0 (pyt. 43–44)", "https://ksef.podatki.gov.pl/pytania-i-odpowiedzi-ksef-20/", "")
GOV_OSTATNI = ("gov.pl: Ostatni etap wdrożenia KSeF – zmiany od 1 stycznia 2027 r. (16.11.2026)", "https://www.gov.pl/web/finanse/ostatni-etap-wdrozenia-ksef-zmiany-od-1-stycznia-2027-r", "")

C19 = dict(
    slug="numer-ksef-w-kpir",
    title="Czy numer KSeF trzeba wpisać do KPiR? Kolumna 3",
    desc="Czy numer KSeF trzeba wpisać do KPiR? Według wzoru księgi od 2026 r. numer faktury z KSeF wpisuje się w kolumnie 3, a inny dowód w kolumnie 4. Zobacz przykład.",
    h1="Czy numer KSeF trzeba wpisać do KPiR – kolumna 3 i kolumna 4",
    intro="Od 2026 r. księga przychodów i rozchodów ma osobne miejsce na numer faktury z KSeF. Pokazujemy, co dokładnie mówi rozporządzenie i jak uniknąć pomyłek przy przepisywaniu 35 znaków.",
    lead_tool=("/sprawdz-wiele-numerow-ksef/", "sprawdzanie wielu numerów KSeF naraz"),
    date=("2026-11-20", "20 listopada 2026"),
    content="""
<h2 id="odpowiedz">Krótka odpowiedź</h2>
<p>Tak. Wzór podatkowej księgi przychodów i rozchodów z rozporządzenia Ministra Finansów i Gospodarki z 6 września 2025 r. (Dz.U. 2025 poz. 1299) zawiera 19 kolumn. Kolumna 3 jest przeznaczona na numer identyfikujący fakturę w KSeF, jeżeli faktura została wystawiona przy użyciu Krajowego Systemu e-Faktur. Kolumna 4 służy do wpisywania innego numeru dowodu księgowego. Zanim przepiszesz numery do księgi lub programu, możesz je sprawdzić w <a href="/sprawdz-wiele-numerow-ksef/">narzędziu do sprawdzania wielu numerów KSeF</a>.</p>
<div class="table-wrap"><table>
<thead><tr><th scope="col">Kolumna KPiR</th><th scope="col">Co wpisujesz</th><th scope="col">Przykład</th></tr></thead>
<tbody>
<tr><td>3</td><td>numer KSeF faktury wystawionej w KSeF</td><td class="mono">5265877635-20250826-0100001AF629-AF</td></tr>
<tr><td>4</td><td>inny numer dowodu księgowego</td><td>dowód wewnętrzny nr 12/2026</td></tr>
</tbody></table></div>
<h2 id="co-mowi-wzor">Co mówi wzór księgi</h2>
<p>Objaśnienia do wzoru wskazują, że kolumna 3 jest przeznaczona do wpisywania numeru identyfikującego fakturę w Krajowym Systemie e-Faktur, a kolumna 4 – innego numeru dowodu księgowego. Ta sama zasada dotyczy faktur sprzedaży i faktur kosztowych, o ile faktura jest z KSeF. W broszurze informacyjnej o JPK_PKPIR na podatki.gov.pl pole z numerem KSeF jest w strukturze opcjonalne, a obok niego jest osobne pole na numer dowodu księgowego (do 256 znaków).</p>
<p>Wniosek praktyczny: numer KSeF nie zastępuje numeru nadanego fakturze przez sprzedawcę. Według Ministerstwa Finansów to dwa różne numery – numer KSeF jest nadawany przez system, a numer z pola P_2 faktury nadaje wystawca. Dlatego przy fakturze z KSeF numer własny sprzedawcy możesz nadal zachować w opisie lub w polu o numerze dowodu, jeśli twój program tak to rozwiązuje. Sprawdź to w instrukcji swojego programu księgowego.</p>
<h2 id="kiedy-kolumna-4">Kiedy kolumna 4, a nie 3</h2>
<p>Do kolumny 4 trafiają dokumenty, które nie mają numeru KSeF. Typowe przykłady:</p>
<ul>
<li>faktura papierowa lub PDF wystawiona poza KSeF (np. od zagranicznego dostawcy),</li>
<li>dowód wewnętrzny, np. na paliwo lub drobne zakupy bez faktury,</li>
<li>faktura wystawiona w 2026 r. poza KSeF przez podatnika, który jeszcze nie miał obowiązku korzystania z systemu.</li>
</ul>
<p>Od 1 stycznia 2027 r., zgodnie z komunikatem Ministerstwa Finansów z 16 listopada 2026 r., obowiązek wystawiania faktur w KSeF obejmie także ostatnią grupę przedsiębiorców oraz faktury dotąd wystawiane z kas rejestrujących. Liczba dokumentów bez numeru KSeF będzie więc w księgach coraz mniejsza.</p>
<h2 id="przyklad">Przykład: trzy wiersze księgi</h2>
<p>Pan Marek prowadzi KPiR na jednoosobowej działalności. W listopadzie ma trzy dokumenty:</p>
<div class="table-wrap"><table>
<thead><tr><th scope="col">Dokument</th><th scope="col">Kolumna 3</th><th scope="col">Kolumna 4</th></tr></thead>
<tbody>
<tr><td>faktura zakupu z KSeF, nr sprzedawcy FV/118/11/2026</td><td class="mono">5265877635-20250826-0100001AF629-AF</td><td>puste albo nr własny wg programu</td></tr>
<tr><td>faktura od dostawcy z zagranicy (PDF)</td><td>puste</td><td>INV-2026-0914</td></tr>
<tr><td>dowód wewnętrzny na parking</td><td>puste</td><td>DW/11/2026</td></tr>
</tbody></table></div>
<p>Numer w pierwszym wierszu to ten sam ciąg, który widać w UPO i w pobranym z KSeF pliku. Wystarczy go skopiować – nie przepisuj ręcznie, bo jedna zamieniona litera A–F zmienia sumę kontrolną. Format i CRC-8 sprawdzisz w <a href="/">walidatorze numeru KSeF</a>.</p>
<h2 id="jak-skopiowac">Jak uniknąć błędów przy wpisywaniu numeru</h2>
<ol class="steps">
<li><strong>Kopiuj, nie przepisuj.</strong> Numer ma 35 znaków łącznie z trzema myślnikami; łatwo pomylić zero z literą O.</li>
<li><strong>Nie dopisuj daty.</strong> Data przyjęcia jest już wewnątrz numeru, drugiego bloku.</li>
<li><strong>Sprawdź długość.</strong> Krótszy lub dłuższy ciąg to nie jest numer KSeF 2.0.</li>
<li><strong>Zrób kontrolę zbiorczą.</strong> Wklej listę numerów z miesiąca do <a href="/sprawdz-wiele-numerow-ksef/">sprawdzarki zbiorczej</a> i pobierz wynik z oceną każdego wiersza.</li>
<li><strong>Dokumenty bez numeru oznacz osobno,</strong> żeby w kolumnie 3 nie wylądował numer faktury sprzedawcy.</li>
</ol>
<h2 id="program">A jeśli księga jest w programie</h2>
<p>Większość podatników prowadzi księgę w programie i numer KSeF zaciąga się automatycznie przy pobraniu faktury. Nasza sprawdzarka nie zastąpi programu, ale pomaga, gdy numery trzeba zweryfikować po imporcie z pliku CSV albo przepisaniu z wyciągu. Narzędzie sprawdza format, NIP, datę i sumę kontrolną CRC-8; nie potwierdza, że faktura istnieje w KSeF.</p>
<h2 id="jpk-pkpir">KPiR a plik JPK_PKPIR</h2>
<p>Księga w postaci elektronicznej jest przesyłana w strukturze JPK_PKPIR, a w opisie struktury na podatki.gov.pl numer KSeF ma własne pole obok numeru dowodu księgowego. Szczegóły techniczne, w tym to, kogo dotyczy wysyłka pliku i w jakich terminach, przeczytasz w broszurze MF i w rozporządzeniu – nie opisujemy ich tu, bo zależą od sytuacji podatnika.</p>
<h2 id="ryczalt">A ryczałt?</h2>
<p>Pamiętaj, że wzór KPiR i wzór ewidencji ryczałtowej to dwa różne dokumenty prawne.</p>
<p>Ewidencja przychodów dla ryczałtu ma własny wzór i własne rozporządzenie. W tym artykule omawiamy wyłącznie KPiR. Jeśli rozliczasz się ryczałtem, zajrzyj do rozporządzenia dotyczącego ewidencji przychodów albo zapytaj księgowego, jak jest tam oznaczony numer KSeF. Sprawę rozbieramy też w osobnym poradniku <a href="/ksef-od-2027-jdg/">KSeF od 2027 dla JDG</a>.</p>
<h2 id="platnosc">Numer w księdze a numer w przelewie</h2>
<p>Numer w KPiR to ewidencja. Obowiązek podania numeru w tytule płatności to osobna sprawa i dotyczy płatności od 1 stycznia 2027 r. między czynnymi podatnikami VAT. Jak ułożyć taki tytuł, opisujemy w tekście <a href="/blog/czy-numer-ksef-musi-byc-w-tytule-przelewu/">czy numer KSeF musi być w tytule przelewu</a>.</p>
<h2 id="audyt">Szybki audyt księgi na koniec miesiąca</h2>
<p>Przed zamknięciem miesiąca przejrzyj wiersze z kolumną 3. Każdy wpis powinien mieć 35 znaków, a kolumna 3 nie powinna zawierać numeru nadanego przez sprzedawcę. Wyeksportuj numery do pliku CSV, wklej je do sprawdzarki zbiorczej i popraw wiersze oznaczone jako błędne. To zajmuje kilka minut, a oszczędza szukania literówek przy późniejszym uzgadnianiu płatności.</p>
<h2 id="podsumowanie">Podsumowanie</h2>
<p>Numer faktury z KSeF wpisujesz w kolumnie 3 KPiR, a dokumenty bez numeru – w kolumnie 4. Kopiuj numery zamiast je przepisywać i sprawdź listę w <a href="/sprawdz-wiele-numerow-ksef/">narzędziu do sprawdzania wielu numerów</a>. W razie wątpliwości co do konkretnego dokumentu pytaj księgowego lub czytaj rozporządzenie.</p>
""",
    faq=[
        ("W której kolumnie KPiR wpisuje się numer KSeF?", "Według objaśnień do wzoru księgi w kolumnie 3, o ile faktura została wystawiona przy użyciu KSeF. Inny numer dowodu księgowego wpisuje się w kolumnie 4."),
        ("Czy numer KSeF zastępuje numer faktury sprzedawcy?", "Nie. MF opisuje je jako dwa różne numery: numer KSeF nadaje system, a numer z pola P_2 nadaje wystawca faktury."),
        ("Co wpisać w KPiR przy fakturze spoza KSeF?", "Numer takiej faktury, czyli inny dowód księgowy, wpisuje się w kolumnie 4, a kolumna 3 pozostaje pusta."),
        ("Czy mogę sprawdzić numery przed wpisaniem do księgi?", "Tak, nasza sprawdzarka weryfikuje długość, NIP, datę i sumę kontrolną CRC-8, ale nie potwierdza istnienia faktury w KSeF."),
    ],
    sources=[KPIR_ROZ, KPIR_BROSZ, MF_NUM, GOV_OSTATNI],
)

C20 = dict(
    slug="czy-numer-ksef-to-nip",
    title="Czy numer KSeF to NIP? Pierwsze 10 cyfr numeru",
    desc="Czy numer KSeF to NIP? Nie – ale zaczyna się od 10 cyfr NIP sprzedawcy. Zobacz, jak odczytać NIP, datę i sumę kontrolną z numeru na przykładzie MF.",
    h1="Czy numer KSeF to NIP – co oznaczają pierwsze 10 cyfr",
    intro="Numer KSeF zaczyna się od dziesięciu cyfr, które wyglądają jak NIP. Wyjaśniamy, skąd się biorą, czym numer KSeF różni się od NIP-u i jak policzyć kontrolę NIP z numeru.",
    lead_tool=("/", "walidator numeru KSeF"),
    date=("2026-11-20", "20 listopada 2026"),
    content="""
<h2 id="odpowiedz">Krótka odpowiedź</h2>
<p>Nie, numer KSeF to nie NIP. To 35-znakowy identyfikator faktury, który zaczyna się od NIP-u sprzedawcy. Dokumentacja Ministerstwa Finansów opisuje go jako ciąg złożony z NIP-u, daty przyjęcia faktury, części technicznej i sumy kontrolnej. Wkleisz go do <a href="/">walidatora numeru KSeF</a>, który rozbije numer na części i sprawdzi każdą z nich.</p>
<div class="table-wrap"><table>
<thead><tr><th scope="col">Cecha</th><th scope="col">NIP</th><th scope="col">Numer KSeF</th></tr></thead>
<tbody>
<tr><td>Co identyfikuje</td><td>podatnika</td><td>jedną fakturę w KSeF</td></tr>
<tr><td>Długość</td><td>10 cyfr</td><td>35 znaków z myślnikami</td></tr>
<tr><td>Kto nadaje</td><td>urząd skarbowy</td><td>system KSeF po przyjęciu faktury</td></tr>
<tr><td>Zmienia się?</td><td>nie</td><td>każda faktura ma inny</td></tr>
</tbody></table></div>
<h2 id="rozbior">Rozbiór numeru na przykładzie MF</h2>
<p>Przykład z dokumentacji MF: <span class="mono">5265877635-20250826-0100001AF629-AF</span>. Pierwszy blok to <span class="mono">5265877635</span> – NIP sprzedawcy. Dwa kolejne bloki to data przyjęcia faktury 2025-08-26 i część techniczna, a ostatnie dwa znaki to suma kontrolna CRC-8.</p>
<div class="table-wrap"><table>
<thead><tr><th scope="col">Część</th><th scope="col">Wartość</th><th scope="col">Rola</th></tr></thead>
<tbody>
<tr><td>NIP</td><td class="mono">5265877635</td><td>wskazuje sprzedawcę</td></tr>
<tr><td>Data</td><td class="mono">20250826</td><td>26 sierpnia 2025</td></tr>
<tr><td>Część techniczna</td><td class="mono">0100001AF629</td><td>12 znaków szesnastkowych</td></tr>
<tr><td>CRC-8</td><td class="mono">AF</td><td>kontrola błędów przepisania</td></tr>
</tbody></table></div>
<p>Pełny rozkład znak po znaku opisujemy w tekście <a href="/blog/z-czego-sklada-sie-numer-ksef/">z czego składa się numer KSeF</a>.</p>
<h2 id="kontrola-nip">Jak działa kontrola NIP</h2>
<p>NIP ma cyfrę kontrolną, czyli dziesiąty znak. Waga kolejnych cyfr to 6, 5, 7, 2, 3, 4, 5, 6, 7. Mnożysz cyfry przez wagi, sumujesz i dzielisz sumę przez 11; reszta musi być równa ostatniej cyfrze. Reszta 10 oznacza, że NIP jest nieprawidłowy.</p>
<p>Dla 5265877635: 5·6 + 2·5 + 6·7 + 5·2 + 8·3 + 7·4 + 7·5 + 6·6 + 3·7 = 30+10+42+10+24+28+35+36+21 = 236. Reszta z dzielenia 236 przez 11 to 5, a dziesiąta cyfra NIP-u to 5, więc kontrola się zgadza. Nasz walidator wykonuje tę kontrolę automatycznie i pokazuje, czy błąd tkwi w NIP-ie, czy w dalszej części numeru.</p>
<h2 id="dlaczego-nip">Dlaczego numer zaczyna się od NIP-u</h2>
<p>Według dokumentacji pierwszy blok to NIP sprzedawcy, więc numer KSeF od razu wskazuje, kto wystawił fakturę. Przy identyfikatorze zbiorczym ten blok jest też NIP-em, ale w środku zamiast daty stoi oznaczenie IZ z rokiem i miesiącem. Różnicę opisujemy w artykule <a href="/blog/identyfikator-zbiorczy-ksef-co-to-jest/">identyfikator zbiorczy KSeF – co to jest</a>.</p>
<h2 id="kiedy-nie-nip">Gdy pierwszy blok nie wygląda jak NIP</h2>
<p>Schemat FA(3) pozwala w polu numeru KSeF także na inne prefiksy niż 10 cyfr NIP (np. dla faktur wystawianych w szczególnych sytuacjach), dlatego nasz walidator w takim przypadku pokazuje ostrzeżenie, a nie błąd. Jeśli to twój przypadek, sprawdź opis pola w dokumentacji MF.</p>
<h2 id="przyklad">Przykład: skąd wiem, kto wystawił fakturę</h2>
<p>Pani Aneta dostała numer <span class="mono">9510001233-20261102-01A3F0C2B7D4-B8</span>. Pierwsze 10 cyfr to 9510001233. Liczy: 9·6 + 5·5 + 1·7 + 0·2 + 0·3 + 0·4 + 1·5 + 2·6 + 3·7 = 54+25+7+0+0+0+5+12+21 = 124, a 124 mod 11 = 3, co zgadza się z ostatnią cyfrą. Drugi blok to 2 listopada 2026 r. Gdy ten sam NIP widnieje w danych sprzedawcy na fakturze, numer pasuje do faktury; jeśli nie, warto zapytać sprzedawcę o poprawny numer. Tytuł przelewu z tym numerem ułożysz w <a href="/przelew-mpp-numer-ksef/">generatorze komunikatu MPP</a>.</p>
<h2 id="nip-vs-numer-faktury">NIP, numer KSeF i numer faktury – trzy różne rzeczy</h2>
<p>Na jednej fakturze spotkasz trzy identyfikatory, które łatwo pomylić. NIP wskazuje podatnika i nie zmienia się między fakturami. Numer faktury nadaje sprzedawca według własnej serii, np. FV/204/12/2026, i według MF jest wskazywany w polu P_2. Numer KSeF nadaje system po przyjęciu faktury; Ministerstwo Finansów zaznacza, że nie jest on elementem pliku XML. Do tytułu przelewu między czynnymi podatnikami VAT od 1 stycznia 2027 r. trafia numer KSeF, nie NIP i nie numer własny sprzedawcy.</p>
<div class="table-wrap"><table>
<thead><tr><th scope="col">Identyfikator</th><th scope="col">Przykład</th><th scope="col">Gdzie go znajdziesz</th></tr></thead>
<tbody>
<tr><td>NIP sprzedawcy</td><td class="mono">5265877635</td><td>dane sprzedawcy na fakturze</td></tr>
<tr><td>Numer faktury</td><td class="mono">FV/204/12/2026</td><td>nagłówek faktury, pole P_2</td></tr>
<tr><td>Numer KSeF</td><td class="mono">5265877635-20250826-0100001AF629-AF</td><td>UPO, aplikacja, nazwa pliku</td></tr>
</tbody></table></div>
<p>Więcej o różnicy między numerem KSeF a numerem faktury piszemy w artykule <a href="/blog/czy-numer-ksef-to-numer-faktury/">czy numer KSeF to numer faktury</a>.</p>
<h2 id="typowe-pomylki">Typowe pomyłki z NIP-em w numerze</h2>
<ul>
<li><strong>Wpisanie samego NIP-u w tytule przelewu.</strong> To tylko początek numeru KSeF, a nie cały identyfikator.</li>
<li><strong>Spacje lub myślniki w NIP-ie.</strong> W numerze KSeF pierwszy blok to 10 cyfr bez separatorów, a myślniki stoją dopiero między blokami.</li>
<li><strong>NIP kupującego zamiast sprzedawcy.</strong> W numerze KSeF faktury zakupu NIP jest zwykle NIP-em sprzedawcy, który wystawił fakturę.</li>
</ul>
<h2 id="czego-nie-wiem">Czego numer nie mówi</h2>
<p>Zgodność NIP-u z numerem nie potwierdza, że faktura istnieje w KSeF ani że kwota jest prawidłowa. Walidator sprawdza tylko format i sumy kontrolne. Istnienie faktury widać w KSeF lub w aplikacji, z której ją pobrano.</p>
<h2 id="przyklad-bledu">Przykład: NIP poprawny, numer błędny</h2>
<p>Poprawny NIP w pierwszym bloku nie gwarantuje poprawności reszty numeru. Weźmy numer <span class="mono">5265877635-20250826-0100001AF629-AA</span>, w którym zmieniono ostatnie dwa znaki. NIP nadal przechodzi kontrolę, data też jest prawidłowa, ale suma CRC-8 się nie zgadza, więc walidator zgłosi błąd właśnie w końcówce. Dzięki rozbiciu numeru na bloki od razu widać, gdzie leży problem i czy trzeba poprosić sprzedawcę o ponowne przesłanie numeru.</p>
<p>Tak samo działa to przy zamianie cyfr w NIP-ie: wynik kontroli wag od razu pokaże, że pierwszy blok jest nieprawidłowy. Dlatego przy każdym numerze patrz na wynik dla poszczególnych bloków, a nie tylko na ogólną ocenę.</p>
<h2 id="wskazowka">Wskazówka na koniec</h2>
<p>Jeśli sprzedawca poda ci sam NIP zamiast numeru KSeF, poproś o pełny numer z UPO albo z aplikacji. Sam NIP nie wystarczy do oznaczenia płatności, bo nie wskazuje konkretnej faktury. Gdy płacisz za kilka faktur jednego kontrahenta, zapytaj też, czy wygenerował identyfikator zbiorczy, który obejmuje je wszystkie.</p>
<h2 id="podsumowanie">Podsumowanie</h2>
<p>Numer KSeF to nie NIP, tylko 35-znakowy identyfikator faktury, w którym pierwsze 10 cyfr to NIP sprzedawcy. Wklej numer do <a href="/">walidatora</a>, żeby w sekundę zobaczyć NIP, datę i wynik sumy kontrolnej.</p>
""",
    faq=[
        ("Czy numer KSeF to to samo co NIP?", "Nie. NIP identyfikuje podatnika i ma 10 cyfr, a numer KSeF identyfikuje fakturę i ma 35 znaków. Pierwsze 10 cyfr numeru to NIP sprzedawcy."),
        ("Czy NIP w numerze KSeF zawsze jest NIP-em sprzedawcy?", "Według dokumentacji MF pierwszy blok to NIP sprzedawcy, ale schemat FA(3) dopuszcza też inne prefiksy w polu numeru KSeF, o czym ostrzega walidator."),
        ("Jak sprawdzić, czy NIP z numeru jest poprawny?", "Pomnóż cyfry przez wagi 6, 5, 7, 2, 3, 4, 5, 6, 7, zsumuj i podziel przez 11. Reszta musi być równa dziesiątej cyfrze."),
        ("Czy poprawny NIP w numerze oznacza, że faktura istnieje?", "Nie. Walidator sprawdza tylko format, NIP, datę i CRC-8, a istnienie faktury potwierdza dopiero KSeF."),
    ],
    sources=[MF_NUM, DOC_NUM, XSD, MF_TERM],
)

C21 = dict(
    slug="numer-ksef-blad-w-przelewie",
    title="Błędny numer KSeF w przelewie – co zrobić?",
    desc="Pomyłka w numerze KSeF w tytule przelewu? Sprawdź, jak ją wychwycić walidatorem, co zrobić przed i po wysłaniu płatności oraz kogo powiadomić.",
    h1="Błędny numer KSeF w przelewie – co zrobić krok po kroku",
    intro="Jedna zamieniona litera w 35 znakach i przelew ma zły numer. Pokazujemy, jak takie błędy wychwycić przed wysyłką i jak postąpić, gdy płatność już wyszła.",
    lead_tool=("/", "walidator numeru KSeF"),
    date=("2026-11-20", "20 listopada 2026"),
    content="""
<h2 id="odpowiedz">Krótka odpowiedź</h2>
<p>Przed wysłaniem przelewu sprawdź numer w <a href="/">walidatorze numeru KSeF</a>. Jeśli przelew już poszedł z błędnym numerem, poinformuj odbiorcę, której faktury dotyczy płatność, i przekaż mu prawidłowy numer. Poniżej opisujemy oba przypadki. Nie rozstrzygamy skutków prawnych – to pytanie do księgowego lub doradcy podatkowego.</p>
<h2 id="obowiazek">Kogo dotyczy obowiązek</h2>
<p>Według Ministerstwa Finansów przepis art. 108g ustawy o VAT stosuje się do płatności dokonanych od 1 stycznia 2027 r. Nabywca będący czynnym podatnikiem VAT, płacący za fakturę ustrukturyzowaną lub fakturę offline, ma podać numer KSeF faktury albo identyfikator zbiorczy. Komunikat MF z 16 listopada 2026 r. podkreśla, że obowiązek obejmie podatników czynnych VAT oraz transakcje w ramach MPP.</p>
<h2 id="typowe-bledy">Najczęstsze pomyłki</h2>
<div class="table-wrap"><table>
<thead><tr><th scope="col">Błąd</th><th scope="col">Jak go zauważyć</th></tr></thead>
<tbody>
<tr><td>numer ma 34 lub 36 znaków</td><td>walidator pokazuje błędną długość</td></tr>
<tr><td>litera spoza A–F w części technicznej</td><td>walidator wskazuje niedozwolony znak</td></tr>
<tr><td>zero zamienione na literę O</td><td>błędny znak lub zła suma CRC-8</td></tr>
<tr><td>numer faktury sprzedawcy zamiast numeru KSeF</td><td>ciąg z ukośnikami, bez 35 znaków</td></tr>
<tr><td>numer obcięty przez limit pola tytułu</td><td>długość mniejsza niż 35</td></tr>
<tr><td>identyfikator zbiorczy wpisany jako zwykły numer</td><td>w środku IZ zamiast daty</td></tr>
</tbody></table></div>
<h2 id="przed-wyslaniem">Przed wysłaniem przelewu</h2>
<ol class="steps">
<li>Skopiuj numer z UPO, z aplikacji lub z programu księgowego – nie przepisuj go z wydruku.</li>
<li>Wklej go do <a href="/">walidatora</a>. Zobaczysz długość, NIP, datę i wynik sumy kontrolnej.</li>
<li>Wstaw numer na początek tytułu, żeby bank go nie obciął. Przy kilku fakturach rozważ <a href="/identyfikator-zbiorczy-ksef/">identyfikator zbiorczy</a>.</li>
<li>Dla płatności MPP ułóż komunikat w <a href="/przelew-mpp-numer-ksef/">generatorze komunikatu MPP</a>, który pilnuje pól.</li>
<li>Po wklejeniu do banku porównaj ostatnie cztery znaki z oryginałem.</li>
</ol>
<h2 id="po-wyslaniu">Gdy przelew już wyszedł z błędem</h2>
<p>W materiałach MF nie znajdziesz procedury cofania takiego przelewu. Praktycznie możesz zrobić trzy rzeczy:</p>
<ul>
<li><strong>Zapisz dowód.</strong> Zrób zrzut potwierdzenia przelewu z kwotą, datą i błędnym tytułem.</li>
<li><strong>Napisz do odbiorcy.</strong> Podaj numer faktury sprzedawcy, kwotę, datę płatności i prawidłowy numer KSeF.</li>
<li><strong>Zapytaj księgowego,</strong> czy trzeba coś dodatkowo udokumentować.</li>
</ul>
<p>Nie wysyłaj drugiego przelewu na tę samą kwotę „dla pewności", bo zapłacisz podwójnie.</p>
<h2 id="przyklad">Przykład wiadomości do odbiorcy</h2>
<p>Pan Tomasz zapłacił za fakturę FV/204/12/2026 na 1 230,00 zł, ale w tytule wkleił numer z literą G. Po sprawdzeniu w walidatorze zauważa błąd i wysyła wiadomość:</p>
<p class="mono">Dzień dobry, w przelewie z 12.01.2027 na 1 230,00 zł za fakturę FV/204/12/2026 wpisałem błędny numer KSeF. Prawidłowy numer: 5265877635-20250826-0100001AF629-AF. Proszę o przypisanie płatności do tej faktury.</p>
<p>Taki komunikat ułatwia odbiorcy ręczne dopasowanie wpłaty. Zachowaj jego odpowiedź razem z potwierdzeniem przelewu.</p>
<h2 id="mpp">Błąd w przelewie MPP</h2>
<p>W podzielonej płatności numer KSeF stoi w polu <code>/INV/</code> komunikatu i ma 35 znaków. Jeśli błąd jest w tym polu, sprawdź w banku, czy da się anulować zlecenie przed realizacją. Po zaksięgowaniu zastosuj kroki jak wyżej. Szczegóły pola opisujemy w tekście <a href="/blog/komunikat-przelewu-mpp-wzor/">komunikat przelewu MPP – wzór</a>.</p>
<h2 id="co-sprawdzic">Czego narzędzie nie sprawdzi</h2>
<p>Walidator nie połączy się z KSeF. Potwierdzi, że numer ma poprawny format, NIP, datę i sumę kontrolną, ale nie zagwarantuje, że faktura o tym numerze istnieje. Dlatego porównuj numer z dokumentem, z którego go skopiowałeś. Numer z poprawną sumą kontrolną może należeć do innej faktury.</p>
<h2 id="lista-kontrolna">Lista kontrolna przy płatności za fakturę</h2>
<div class="table-wrap"><table>
<thead><tr><th scope="col">Krok</th><th scope="col">Co sprawdzasz</th><th scope="col">Narzędzie</th></tr></thead>
<tbody>
<tr><td>1</td><td>czy numer ma 35 znaków i poprawną sumę</td><td><a href="/">walidator</a></td></tr>
<tr><td>2</td><td>czy NIP w numerze zgadza się z NIP-em sprzedawcy</td><td>faktura lub UPO</td></tr>
<tr><td>3</td><td>czy numer stoi na początku tytułu</td><td>formularz banku</td></tr>
<tr><td>4</td><td>czy przy MPP numer jest w polu /INV/</td><td><a href="/przelew-mpp-numer-ksef/">generator MPP</a></td></tr>
</tbody></table></div>
<h2 id="kiedy-pytac">Kiedy zapytać księgowego</h2>
<p>Jeśli nie wiesz, czy twoja płatność w ogóle podlega obowiązkowi (np. odbiorca nie jest czynnym podatnikiem VAT albo płacisz w sposób niepozwalający podać tytułu), nie zgaduj. MF opisuje zakres obowiązku w pytaniach i odpowiedziach KSeF 2.0, a szczegółowe przypadki warto omówić z księgowym. Ten artykuł dotyczy wyłącznie technicznej strony pomyłek w numerze.</p>
<h2 id="jak-nie-popelnic">Jak ograniczyć liczbę pomyłek w firmie</h2>
<p>Najlepiej, gdy numer przechodzi z KSeF do banku bez ręcznego przepisywania. Jeśli to niemożliwe, ustal w firmie jedną regułę: numer zawsze kopiujemy i zawsze sprawdzamy w walidatorze przed zatwierdzeniem przelewu. Przy większej liczbie faktur wprowadź kontrolę zbiorczą, a przy kilku fakturach jednego sprzedawcy rozważ identyfikator zbiorczy, który zastępuje wiele numerów jednym. Pomyłki zdarzają się zwykle w ostatnich czterech znakach, dlatego porównuj właśnie ich koniec.</p>
<h2 id="partie">Wiele przelewów naraz</h2>
<p>Gdy płacisz dziesiątki faktur, wklej listę numerów do <a href="/sprawdz-wiele-numerow-ksef/">sprawdzarki zbiorczej</a> przed wygenerowaniem pliku przelewów. Zobaczysz, w których wierszach numer jest błędny, i poprawisz je, zanim wyślesz paczkę do banku.</p>
<h2 id="dokumentacja">Dokumentacja pomyłek</h2>
<p>Prowadź prostą listę przelewów, w których popełniono błąd w tytule: data, kwota, numer faktury, błędny i prawidłowy numer KSeF oraz data wiadomości do odbiorcy. Taka notatka pomaga księgowemu rozliczyć sprawę i pokazuje, że błąd został zauważony i wyjaśniony. Wystarczy arkusz z sześcioma kolumnami; nie musi to być osobny program.</p>
<h2 id="wskazowka">Wskazówka na koniec</h2>
<p>Zanim zatwierdzisz przelew w banku, przeczytaj tytuł jeszcze raz od końca: ostatnie cztery znaki numeru najłatwiej zepsuć przy kopiowaniu i to one zawierają sumę kontrolną. Jeśli bank ogranicza długość tytułu, upewnij się, że 35 znaków numeru mieści się w całości, a ewentualny dodatkowy opis stoi dopiero po nim.</p>
<h2 id="podsumowanie">Podsumowanie</h2>
<p>Najtańszy sposób na błąd w numerze KSeF to sprawdzenie go przed wysyłką. Jeśli przelew już wyszedł, zapisz dowód, napisz do odbiorcy z prawidłowym numerem i skonsultuj się z księgowym. Zacznij od <a href="/">walidatora numeru KSeF</a>.</p>
""",
    faq=[
        ("Co zrobić, gdy w tytule przelewu jest błędny numer KSeF?", "Zapisz potwierdzenie, napisz do odbiorcy z prawidłowym numerem i numerem faktury sprzedawcy oraz zapytaj księgowego, czy trzeba coś jeszcze udokumentować."),
        ("Czy trzeba wysłać drugi przelew?", "Nie ma takiej potrzeby, jeśli kwota była prawidłowa. Drugi przelew oznaczałby podwójną zapłatę, więc najpierw skontaktuj się z odbiorcą."),
        ("Od kiedy obowiązuje numer KSeF w przelewie?", "Według MF przepis art. 108g ustawy o VAT stosuje się do płatności dokonanych od 1 stycznia 2027 r."),
        ("Jak sprawdzić numer przed wysłaniem przelewu?", "Wklej go do walidatora. Sprawdzi długość, dozwolone znaki, NIP, datę i sumę kontrolną CRC-8."),
    ],
    sources=[MF_PYT2, GOV_OSTATNI, MF_NUM, MF_PODR2],
)

C22 = dict(
    slug="przelew-faktury-ksef-2026-zaplata-2027",
    title="Faktura z 2026, zapłata w 2027 – jaki tytuł?",
    desc="Faktura wystawiona w 2026 r., a płatność w 2027 r.? Sprawdź, o czym decyduje data płatności, i ułóż tytuł przelewu z numerem KSeF w walidatorze.",
    h1="Faktura z 2026 r., zapłata w 2027 r. – jaki tytuł przelewu",
    intro="Wiele firm zapłaci w styczniu za faktury z grudnia. Wyjaśniamy, czym rozstrzyga się obowiązek numeru KSeF w tytule przelewu i jak go przygotować.",
    lead_tool=("/", "walidator numeru KSeF i generator tytułu przelewu"),
    date=("2026-11-21", "21 listopada 2026"),
    content="""
<h2 id="odpowiedz">Krótka odpowiedź</h2>
<p>Według Ministerstwa Finansów przepis art. 108g ustawy o VAT stosuje się do płatności dokonanych od 1 stycznia 2027 r. Liczy się więc data zapłaty, a nie data wystawienia faktury. Jeśli płacisz w 2027 r. za fakturę z KSeF, przygotuj numer w <a href="/">walidatorze numeru KSeF</a>. Szczegóły w twoim przypadku potwierdź z księgowym.</p>
<h2 id="data-platnosci">Co decyduje: data wystawienia czy data płatności</h2>
<p>MF w komunikacie o ostatnim etapie wdrożenia KSeF pisze o płatnościach dokonanych od 1 stycznia 2027 r. Z tego wynika praktyczny wniosek: ten sam dokument może wymagać różnego opisu przelewu, zależnie od dnia, w którym środki wychodzą z rachunku. Dzień zlecenia i dzień realizacji mogą się różnić, zwłaszcza w okresie świątecznym, dlatego przy płatnościach na przełomie roku zapytaj bank, jak liczy datę.</p>
<div class="table-wrap"><table>
<thead><tr><th scope="col">Sytuacja</th><th scope="col">Co wpisać w tytule</th></tr></thead>
<tbody>
<tr><td>faktura z KSeF, płatność do 31.12.2026</td><td>dotychczasowy opis, np. numer faktury sprzedawcy</td></tr>
<tr><td>faktura z KSeF, płatność od 1.01.2027, obie strony czynnymi podatnikami VAT</td><td>numer KSeF faktury lub identyfikator zbiorczy</td></tr>
<tr><td>faktura wystawiona poza KSeF (tryb offline), płatność od 1.01.2027</td><td>zgodnie z materiałami MF – sprawdź w pytaniach i odpowiedziach KSeF 2.0</td></tr>
<tr><td>płatność MPP od 1.01.2027</td><td>numer KSeF w polu /INV/ komunikatu</td></tr>
</tbody></table></div>
<h2 id="przyklad">Przykład: faktura z 15 grudnia, zapłata 8 stycznia</h2>
<p>Firma Alfa wystawia 15 grudnia 2026 r. fakturę na 2 460,00 zł brutto. Termin płatności to 8 stycznia 2027 r., a nabywca jest czynnym podatnikiem VAT. Faktura trafia do KSeF i dostaje numer, np. 5265877635-20261215-0100001AF629-AF (przykład ilustracyjny). Nabywca w dniu płatności:</p>
<ol class="steps">
<li>kopiuje numer z aplikacji lub programu księgowego,</li>
<li>wkleja go do <a href="/">walidatora</a> i sprawdza długość, NIP, datę oraz sumę kontrolną,</li>
<li>wstawia numer na początek tytułu przelewu,</li>
<li>przy płatności MPP układa komunikat w <a href="/przelew-mpp-numer-ksef/">generatorze komunikatu MPP</a>.</li>
</ol>
<p>Gdyby ten sam przelew wyszedł 30 grudnia, obowiązek podania numeru jeszcze by nie działał, choć nic nie stoi na przeszkodzie, by podać go dobrowolnie.</p>
<h2 id="przelew-przyszly">Przelew z datą przyszłą i zlecenia stałe</h2>
<p>Jeśli w grudniu ustawisz przelew z datą realizacji w styczniu, sprawdź w banku, jak działa edycja tytułu przed wykonaniem. Zlecenia stałe i polecenia zapłaty często mają stały opis, który nie zmieni się sam. Przejrzyj je pod koniec roku: te, które dotyczą faktur z KSeF, mogą wymagać nowego tytułu. W materiałach MF nie znajdziesz instrukcji dla konkretnych banków, więc sprawdź ich komunikaty.</p>
<h2 id="wiele-faktur">Kilka faktur w jednym przelewie</h2>
<p>Gdy łączysz płatność za kilka faktur jednego sprzedawcy, MF przewiduje identyfikator zbiorczy. Opisujemy go w tekście o <a href="/blog/jak-wygenerowac-identyfikator-zbiorczy-ksef/">generowaniu identyfikatora zbiorczego</a>, a sam identyfikator sprawdzisz w <a href="/identyfikator-zbiorczy-ksef/">dedykowanym narzędziu</a>. Przy płatności za faktury z różnych lat zapytaj księgowego, jak je pogrupować.</p>
<h2 id="lista">Lista kontrolna na przełom roku</h2>
<div class="table-wrap"><table>
<thead><tr><th scope="col">Krok</th><th scope="col">Kiedy</th></tr></thead>
<tbody>
<tr><td>zrób listę niezapłaconych faktur z numerami KSeF</td><td>połowa grudnia</td></tr>
<tr><td>sprawdź numery w <a href="/sprawdz-wiele-numerow-ksef/">sprawdzarce zbiorczej</a></td><td>przed przygotowaniem paczki przelewów</td></tr>
<tr><td>zdecyduj, które płatności wychodzą w 2026 r., a które w 2027 r.</td><td>do końca grudnia</td></tr>
<tr><td>zaktualizuj opisy zleceń stałych</td><td>przed pierwszą płatnością w 2027 r.</td></tr>
</tbody></table></div>
<h2 id="dobrowolnie">Czy można podać numer wcześniej</h2>
<p>Przepisy nie zabraniają wpisania numeru KSeF w tytule przed 2027 r. Jeśli sprzedawca wystawił fakturę w KSeF, taki opis ułatwia mu dopasowanie wpłaty. Nie jest to jednak obowiązek wynikający z art. 108g, więc nie traktuj tego jako wymogu. W razie wątpliwości zapytaj kontrahenta, jak woli otrzymywać płatności.</p>
<h2 id="ograniczenia">Czego ten tekst nie rozstrzyga</h2>
<p>Nie opisujemy skutków podatkowych pomyłek ani wyjątków dla poszczególnych rodzajów płatności. Walidator sprawdza format numeru, a nie istnienie faktury w KSeF. Zakres obowiązku i jego szczegóły znajdziesz w pytaniach i odpowiedziach KSeF 2.0 na stronie MF oraz w komunikatach gov.pl; trudniejsze przypadki omów z księgowym. Pamiętaj też, że do końca 2026 r. mogą pojawić się nowe komunikaty, więc przed przelewem zajrzyj do źródeł wskazanych poniżej.</p>
<h2 id="przyklad-bank">Przykład: paczka przelewów na koniec roku</h2>
<p>Biuro rachunkowe obsługuje firmę, która ma w grudniu dwanaście niezapłaconych faktur z terminem w styczniu. Księgowa dzieli je na dwie grupy: te, które firma zapłaci jeszcze w 2026 r., i te, które wyjdą w 2027 r. Dla drugiej grupy wkleja numery KSeF do sprawdzarki zbiorczej, poprawia dwa błędne wiersze, a potem układa tytuły. Dzięki temu pierwsza paczka przelewów w styczniu jest gotowa w kilka minut, a nie w ostatniej chwili przed terminem płatności.</p>
<h2 id="pytania-do-banku">Pytania, które warto zadać bankowi</h2>
<ul>
<li>Jak bank liczy datę płatności przy przelewach z datą przyszłą?</li>
<li>Ile znaków mieści pole tytułu i czy numer KSeF zmieści się w nim w całości?</li>
<li>Czy da się edytować tytuł zlecenia stałego bez zakładania go od nowa?</li>
<li>Czy import pliku przelewów obsługuje komunikat MPP z polem /INV/?</li>
</ul>
<p>Odpowiedzi znajdziesz w regulaminie banku lub u opiekuna konta. Materiały MF nie opisują zasad poszczególnych banków, więc nie przyjmuj ich z góry.</p>
<h2 id="dokumenty">Co zachować na wypadek pytań</h2>
<p>Przy płatnościach na przełomie roku warto zachować potwierdzenie przelewu, numer KSeF faktury oraz datę, w której zlecono i zrealizowano płatność. Jeśli kontrahent zapyta, której faktury dotyczyła wpłata, odpowiesz jednym spojrzeniem na zestawienie. Taka lista nie jest wymogiem z ustawy, tylko praktycznym zabezpieczeniem.</p>
<h2 id="podsumowanie">Podsumowanie</h2>
<p>O opisie przelewu decyduje data płatności. Faktura z grudnia, zapłacona w styczniu 2027 r., podlega regule numeru KSeF, jeśli spełnione są warunki z art. 108g. Przygotuj numery wcześniej: sprawdź je w <a href="/">walidatorze</a>, a przy wielu fakturach w <a href="/sprawdz-wiele-numerow-ksef/">sprawdzarce zbiorczej</a>. Dzięki temu pierwszy przelew w nowym roku nie będzie wymagał pośpiechu.</p>
""",
    faq=[
        ("Czy liczy się data faktury czy data płatności?", "Według MF przepis art. 108g stosuje się do płatności dokonanych od 1 stycznia 2027 r., więc decyduje data zapłaty."),
        ("Czy za fakturę z grudnia 2026 trzeba podać numer KSeF w styczniu?", "Jeśli płatność następuje od 1 stycznia 2027 r. i spełnione są warunki z art. 108g, tak. Szczegóły omów z księgowym."),
        ("Czy mogę wpisać numer KSeF już w grudniu 2026?", "Przepisy tego nie zabraniają. To dobrowolne ułatwienie dla odbiorcy, a nie obowiązek z art. 108g."),
        ("Co ze zleceniami stałymi z ustalonym opisem?", "Opis zlecenia stałego nie zmieni się sam. Przejrzyj je przed pierwszą płatnością w 2027 r. i zaktualizuj tam, gdzie dotyczą faktur z KSeF."),
    ],
    sources=[MF_PYT2, GOV_OSTATNI, MF_NUM, MF_TERM],
)

C23 = dict(
    slug="czy-jdg-bez-vat-podaje-numer-ksef",
    title="JDG zwolniona z VAT a numer KSeF w przelewie",
    desc="JDG zwolniona z VAT: czy musisz podać numer KSeF w tytule przelewu? Wyjaśniamy zasadę z art. 108g i pokazujemy, jak sprawdzić numer w walidatorze.",
    h1="JDG zwolniona z VAT a numer KSeF w tytule przelewu",
    intro="Prowadzisz jednoosobową firmę zwolnioną z VAT i zastanawiasz się, czy od 2027 r. musisz wpisywać numer KSeF w przelewach. Oto zasada i kilka przykładów.",
    lead_tool=("/ksef-od-2027-jdg/", "kwestionariusz KSeF dla JDG"),
    date=("2026-11-21", "21 listopada 2026"),
    content="""
<h2 id="odpowiedz">Krótka odpowiedź</h2>
<p>Komunikat MF z 16 listopada 2026 r. mówi, że obowiązek z art. 108g obejmie podatników czynnych VAT oraz transakcje w ramach MPP. JDG zwolniona z VAT nie jest czynnym podatnikiem, więc ten obowiązek zwykle jej nie dotyczy. Sprawdź swoją sytuację w <a href="/ksef-od-2027-jdg/">kwestionariuszu KSeF dla JDG</a> i potwierdź z księgowym.</p>
<h2 id="dwie-sprawy">Dwie różne sprawy: wystawianie i płacenie</h2>
<p>KSeF dotyczy dwóch rzeczy. Pierwsza to wystawianie i odbieranie faktur w systemie. Druga to opis płatności za faktury z KSeF. Zwolnienie z VAT nie oznacza automatycznie, że firma jest poza KSeF – MF opisuje zasady wystawiania faktur osobno od zasad płatności. Ten tekst dotyczy wyłącznie tytułu przelewu.</p>
<div class="table-wrap"><table>
<thead><tr><th scope="col">Rola</th><th scope="col">Status VAT</th><th scope="col">Numer KSeF w przelewie</th></tr></thead>
<tbody>
<tr><td>płacisz za fakturę</td><td>nabywca zwolniony z VAT</td><td>obowiązek z art. 108g zwykle nie dotyczy</td></tr>
<tr><td>płacisz za fakturę</td><td>nabywca czynny, sprzedawca czynny</td><td>numer KSeF lub identyfikator zbiorczy</td></tr>
<tr><td>otrzymujesz płatność</td><td>sprzedawca zwolniony z VAT</td><td>zwykle bez obowiązku po stronie płacącego</td></tr>
<tr><td>płatność w MPP</td><td>strony objęte MPP</td><td>numer KSeF w polu /INV/</td></tr>
</tbody></table></div>
<h2 id="przyklady">Przykłady</h2>
<p>Pani Ewa prowadzi JDG zwolnioną z VAT i kupuje towar od hurtowni, która jest czynnym podatnikiem. Hurtownia wystawia fakturę w KSeF. Pani Ewa nie jest czynnym podatnikiem VAT, więc – zgodnie z komunikatem MF – obowiązek z art. 108g jej nie obejmuje. Może jednak dopisać numer KSeF dobrowolnie, bo hurtowni ułatwi to dopasowanie wpłaty.</p>
<p>Pan Marek ma JDG zwolnioną z VAT i wystawia faktury klientom. To klienci płacą, więc to oni decydują, jak opisać przelew. Jeśli klient jest czynnym podatnikiem, a Marek zwolnionym, zasady z art. 108g zwykle go nie wiążą. Marek może mimo to poprosić klientów o numer KSeF, żeby łatwiej księgować wpłaty.</p>
<h2 id="dobrowolnie">Dobrowolne podanie numeru</h2>
<p>Jeśli chcesz podać numer mimo braku obowiązku, skopiuj go z aplikacji i sprawdź w <a href="/">walidatorze numeru KSeF</a>. Numer ma 35 znaków, a ostatnie dwa to suma kontrolna CRC-8. Zły numer w tytule nie pomaga nikomu, więc lepiej go zweryfikować. Szczegóły budowy opisujemy w tekście <a href="/blog/z-czego-sklada-sie-numer-ksef/">z czego składa się numer KSeF</a>.</p>
<h2 id="zmiana-statusu">Zmiana statusu VAT w trakcie roku</h2>
<p>Zwolniona JDG może utracić zwolnienie lub zarejestrować się jako czynny podatnik VAT. Od tej chwili jest czynnym podatnikiem i obowiązek z art. 108g może jej dotyczyć. Z perspektywy płatności warto więc przygotować proces z wyprzedzeniem: ustal, skąd kopiujesz numery KSeF, i przetestuj walidator na kilku prawdziwych fakturach. Przy wielu płatnościach pomoże <a href="/sprawdz-wiele-numerow-ksef/">sprawdzarka zbiorcza</a>.</p>
<h2 id="mpp">A co z MPP</h2>
<p>Komunikat MF wymienia osobno transakcje w ramach MPP. Jeśli płacisz podzieloną płatnością, zapytaj księgowego, jak obowiązek działa w twoim przypadku, bo to zależy od rodzaju transakcji. Wzór pól komunikatu pokazuje <a href="/przelew-mpp-numer-ksef/">generator komunikatu MPP</a>, a opis pól znajdziesz w tekście <a href="/blog/komunikat-przelewu-mpp-wzor/">komunikat przelewu MPP – wzór</a>.</p>
<h2 id="ostroznie">Dlaczego warto zachować ostrożność</h2>
<p>Przepisy dotyczące KSeF są nowe, a MF publikuje kolejne wyjaśnienia. Zasada „zwolniony z VAT, więc bez numeru" jest uproszczeniem komunikatu MF, nie indywidualną interpretacją. Jeśli twoja sprawa jest nietypowa, np. łączysz sprzedaż zwolnioną i opodatkowaną, zapytaj księgowego lub zajrzyj do pytań i odpowiedzi KSeF 2.0. Nie opieraj się na samych forach.</p>
<h2 id="co-zrobic">Co zrobić teraz</h2>
<ol class="steps">
<li>Ustal swój status VAT: czynny czy zwolniony.</li>
<li>Wypełnij <a href="/ksef-od-2027-jdg/">kwestionariusz dla JDG</a>, żeby zobaczyć listę zmian od 1 stycznia 2027 r.</li>
<li>Zapytaj księgowego o MPP i nietypowe transakcje.</li>
<li>Przetestuj <a href="/">walidator</a> na kilku numerach.</li>
</ol>
<h2 id="lista-pytan">Pytania, które warto sobie zadać</h2>
<div class="table-wrap"><table>
<thead><tr><th scope="col">Pytanie</th><th scope="col">Dlaczego ma znaczenie</th></tr></thead>
<tbody>
<tr><td>Czy jestem czynnym podatnikiem VAT?</td><td>komunikat MF wiąże obowiązek z podatnikami czynnymi</td></tr>
<tr><td>Czy kontrahent jest czynnym podatnikiem?</td><td>od tego zależy, czy art. 108g w ogóle znajdzie zastosowanie do płatności</td></tr>
<tr><td>Czy płatność idzie w MPP?</td><td>MF wymienia MPP osobno</td></tr>
<tr><td>Czy faktura jest w KSeF?</td><td>numer KSeF istnieje tylko dla faktur z systemu</td></tr>
</tbody></table></div>
<h2 id="co-prosi-kontrahent">Gdy kontrahent prosi o numer</h2>
<p>Zdarza się, że firma-klient w ramach własnych procedur prosi wszystkich dostawców o numer KSeF w przelewie, także tych zwolnionych z VAT. To jej decyzja organizacyjna, a nie wymóg wobec ciebie. Jeśli chcesz ułatwić współpracę, możesz po prostu podać numer faktury z KSeF w wiadomości lub na fakturze. Wystarczy skopiować go z aplikacji, a poprawność sprawdzić w <a href="/">walidatorze</a>. Taki gest nic nie kosztuje i skraca czas księgowania wpłat.</p>
<h2 id="ksiegowanie">Księgowanie płatności w JDG</h2>
<p>Nawet bez obowiązku z art. 108g numer KSeF przydaje się w ewidencji: jednoznacznie wskazuje fakturę, której dotyczy płatność. Jeśli prowadzisz proste zestawienie należności, dodaj do niego kolumnę z numerem KSeF. Pomoże ci to szybciej znaleźć dokument, gdy kontrahent zapyta o płatność lub gdy księgowy poprosi o wyjaśnienie wpłaty z wyciągu.</p>
<h2 id="rozmowa-z-ksiegowym">Co zanieść do księgowego</h2>
<p>Przed rozmową przygotuj krótką listę: informację o swoim statusie VAT, rodzaje transakcji (sprzedaż krajowa, zakupy od czynnych podatników, płatności w MPP) oraz przykładowe faktury z numerami KSeF. Zapytaj wprost, czy w twoim przypadku którakolwiek płatność podlega art. 108g, i poproś o odpowiedź na piśmie lub w wiadomości. Taka notatka zostaje w aktach firmy i oszczędza kłopotu, gdy ktoś później zapyta, dlaczego przelewy miały taki, a nie inny tytuł. Wystarczy kilka zdań, a spokój na cały rok jest gwarantowany.</p>
<p>Warto też zapisać datę rozmowy oraz źródło, na którym oparł się księgowy, np. komunikat MF z 16 listopada 2026 r. albo pytania i odpowiedzi KSeF 2.0.</p>
<h2 id="podsumowanie">Podsumowanie</h2>
<p>Według komunikatu MF obowiązek numeru KSeF w przelewie dotyczy czynnych podatników VAT i transakcji w ramach MPP. JDG zwolniona z VAT zwykle nie musi go wpisywać, ale może to zrobić dobrowolnie. Zacznij od <a href="/ksef-od-2027-jdg/">kwestionariusza KSeF dla JDG</a>.</p>
""",
    faq=[
        ("Czy JDG zwolniona z VAT musi wpisać numer KSeF w tytule przelewu?", "Według komunikatu MF obowiązek z art. 108g obejmuje podatników czynnych VAT oraz transakcje w ramach MPP, więc zwolniona JDG zwykle nie musi. Potwierdź to z księgowym."),
        ("Czy mogę podać numer KSeF dobrowolnie?", "Tak. Ułatwia to odbiorcy dopasowanie wpłaty, ale nie jest to wymóg z art. 108g."),
        ("Czy zwolnienie z VAT oznacza brak KSeF?", "Nie. Wystawianie faktur i opis płatności to dwie osobne kwestie. Sprawdź swoją sytuację w kwestionariuszu dla JDG."),
        ("Co jeśli zarejestruję się jako czynny podatnik VAT?", "Jako czynny podatnik możesz podlegać obowiązkowi z art. 108g, więc przygotuj proces kopiowania i sprawdzania numerów."),
    ],
    sources=[GOV_OSTATNI, MF_PYT2, MF_TERM, MF_NUM],
)

C24 = dict(
    slug="ksef-jdg-od-czego-zaczac",
    title="KSeF w JDG – od czego zacząć? Lista kroków",
    desc="KSeF w jednoosobowej firmie: lista kroków przed 1 stycznia 2027 r. – konto w aplikacji, uprawnienia, faktury, płatności z numerem KSeF i kontrola błędów.",
    h1="KSeF w JDG – od czego zacząć przed 2027 rokiem",
    intro="Jednoosobowa firma nie potrzebuje wielkiego projektu wdrożeniowego, ale kilka kroków warto wykonać wcześniej. Oto praktyczna lista z odnośnikami do narzędzi.",
    lead_tool=("/ksef-od-2027-jdg/", "kwestionariusz KSeF dla JDG"),
    date=("2026-11-21", "21 listopada 2026"),
    content="""
<h2 id="odpowiedz">Krótka odpowiedź</h2>
<p>Zacznij od sprawdzenia, jakie obowiązki cię dotyczą, w <a href="/ksef-od-2027-jdg/">kwestionariuszu KSeF dla JDG</a>. Potem załóż dostęp do Aplikacji Podatnika KSeF, ustal z księgowym sposób wystawiania faktur i przygotuj opis przelewów. Stan prawny zmienia się, więc ostateczne terminy sprawdzaj na stronie ksef.podatki.gov.pl.</p>
<h2 id="kroki">Siedem kroków</h2>
<ol class="steps">
<li><strong>Ustal status VAT.</strong> Czynny podatnik czy zwolniony – od tego zależy część obowiązków, m.in. dotyczących przelewów.</li>
<li><strong>Sprawdź terminy.</strong> Według MF zwolnienie dla faktur do 10 000 zł miesięcznie i faktur z kas kończy się 31 grudnia 2026 r. Od 1 stycznia 2027 r. wystawianie faktur dla innych firm odbywa się w KSeF.</li>
<li><strong>Wejdź do Aplikacji Podatnika KSeF.</strong> Aplikacja jest udostępniana przez MF na ksef.podatki.gov.pl; zapoznaj się z jej podręcznikiem.</li>
<li><strong>Zapytaj księgowego o uprawnienia.</strong> Ustal, kto wystawia faktury i kto ma dostęp do dokumentów.</li>
<li><strong>Wybierz sposób wystawiania faktur:</strong> aplikacja MF, program fakturowy lub program księgowy.</li>
<li><strong>Przygotuj płatności.</strong> Naucz się kopiować numer KSeF i sprawdzać go w <a href="/">walidatorze</a>.</li>
<li><strong>Zrób próbę.</strong> Wystaw lub pobierz kilka faktur i prześledź cały obieg do przelewu.</li>
</ol>
<h2 id="harmonogram">Przykładowy harmonogram</h2>
<div class="table-wrap"><table>
<thead><tr><th scope="col">Kiedy</th><th scope="col">Zadanie</th><th scope="col">Pomoc</th></tr></thead>
<tbody>
<tr><td>teraz</td><td>kwestionariusz i rozmowa z księgowym</td><td><a href="/ksef-od-2027-jdg/">kwestionariusz</a></td></tr>
<tr><td>do połowy grudnia</td><td>dostęp do aplikacji, wybór programu</td><td>ksef.podatki.gov.pl</td></tr>
<tr><td>do końca grudnia</td><td>próbne faktury, test walidatora</td><td><a href="/">walidator</a></td></tr>
<tr><td>od 1 stycznia 2027</td><td>wystawianie w KSeF, płatności z numerem</td><td><a href="/przelew-mpp-numer-ksef/">generator MPP</a></td></tr>
</tbody></table></div>
<h2 id="przyklad">Przykład: grafik na umowie o dzieło i zlecenia dla firm</h2>
<p>Anna prowadzi JDG jako grafik i fakturuje kilkunastu klientów miesięcznie, w tym firmy. Dotąd wystawiała faktury w edytorze tekstu. W grudniu wykonuje trzy rzeczy: ustala z księgowym, że faktury będzie wystawiać w programie fakturowym zgodnym z KSeF, wypełnia kwestionariusz i próbuje pobrać z aplikacji MF dwie testowe faktury. Gdy w styczniu dostaje fakturę od dostawcy, kopiuje numer KSeF, wkleja go do walidatora i dopiero wtedy zleca przelew.</p>
<h2 id="platnosci">Płatności – część, o której łatwo zapomnieć</h2>
<p>Wiele poradników skupia się na wystawianiu faktur. Tymczasem od 1 stycznia 2027 r. nabywca będący czynnym podatnikiem, płacąc za fakturę z KSeF, ma podać numer KSeF albo identyfikator zbiorczy (art. 108g). Jeśli twoja firma jest zwolniona z VAT, zapoznaj się z tekstem <a href="/blog/czy-jdg-bez-vat-podaje-numer-ksef/">JDG zwolniona z VAT a numer KSeF</a>. Gdy płacisz za wiele faktur, użyj <a href="/sprawdz-wiele-numerow-ksef/">sprawdzarki zbiorczej</a>.</p>
<h2 id="faktury-kupowane">Faktury od dostawców</h2>
<p>Faktury kosztowe będziesz odbierać z KSeF. Ustal, kto je pobiera i jak trafiają do księgowości. Z aplikacji możesz je wyszukać i pobrać, a plik XML obejrzysz bez specjalnego programu – opisujemy to w tekście <a href="/blog/jak-otworzyc-plik-xml-ksef/">jak otworzyć plik XML z KSeF</a>. Zadbaj, by numer KSeF każdej faktury kosztowej trafił do ewidencji, bo przyda się przy płatności.</p>
<h2 id="bledy">Typowe potknięcia na starcie</h2>
<ul>
<li>przepisywanie numeru ręcznie zamiast kopiowania,</li>
<li>brak ustalenia z księgowym, kto odbiera faktury kosztowe,</li>
<li>założenie, że zwolnienie z VAT zwalnia z KSeF w ogóle,</li>
<li>pozostawienie testów na ostatni tydzień grudnia,</li>
<li>zlecenia stałe w banku ze starym opisem.</li>
</ul>
<h2 id="czego-nie-wiemy">Czego nie rozstrzygamy</h2>
<p>Nie podajemy terminów ani wysokości kar. Kwestie te mogą się zmienić, a ich status trzeba sprawdzać w oficjalnych źródłach, takich jak komunikaty gov.pl i ISAP. Ten artykuł jest ogólnym przewodnikiem, a nie doradztwem podatkowym, więc nietypowe przypadki omów z księgowym.</p>
<h2 id="przyklad-sklep">Przykład: mały sklep internetowy</h2>
<p>Pan Piotr prowadzi JDG ze sprzedażą hurtową akcesoriów do firm i detaliczną do osób prywatnych. Z komunikatów MF wie, że faktury dla osób fizycznych nieprowadzących działalności są w KSeF dobrowolne, natomiast faktury dla firm trzeba wystawiać w systemie. Dlatego ustala z księgowym, że faktury B2B będą szły przez program fakturowy z integracją z KSeF, a sprzedaż konsumencka zostanie bez zmian. Dodatkowo przygotowuje listę dostawców, od których będzie odbierał faktury, i dopisuje do ewidencji kolumnę z numerem KSeF.</p>
<h2 id="lista-kontrolna">Lista kontrolna na koniec grudnia</h2>
<div class="table-wrap"><table>
<thead><tr><th scope="col">Pozycja</th><th scope="col">Gotowe, gdy</th></tr></thead>
<tbody>
<tr><td>dostęp do aplikacji</td><td>potrafisz wejść i wyszukać fakturę</td></tr>
<tr><td>sposób wystawiania</td><td>wystawiłeś lub wczytałeś fakturę próbną</td></tr>
<tr><td>faktury kosztowe</td><td>wiadomo, kto je pobiera i jak trafiają do księgowości</td></tr>
<tr><td>płatności</td><td>numer przechodzi z aplikacji do banku bez przepisywania</td></tr>
<tr><td>zlecenia stałe</td><td>opisy sprawdzone i w razie potrzeby poprawione</td></tr>
</tbody></table></div>
<h2 id="dalsze-kroki">Co dalej po starcie</h2>
<p>Po pierwszych tygodniach 2027 r. przejrzyj, co poszło sprawnie, a co trzeba poprawić. Zwróć uwagę na czas, jaki zajmuje kopiowanie numerów, i na ewentualne błędy w przelewach – w razie pomyłki zajrzyj do tekstu <a href="/blog/numer-ksef-blad-w-przelewie/">błędny numer KSeF w przelewie</a>. Śledź też komunikaty MF, bo wyjaśnienia i terminy mogą się zmieniać.</p>
<h2 id="rozmowa-ksiegowy">Pytania do księgowego</h2>
<p>Zanim zaczniesz wdrożenie, zapytaj księgowego o cztery rzeczy: kto będzie pobierał faktury kosztowe z KSeF, w jakim programie prowadzona jest ewidencja, czy twoja sprzedaż obejmuje faktury dla firm i dla konsumentów oraz jak wygląda jego procedura dla płatności z numerem KSeF. Odpowiedzi zapisz w jednej notatce. Dzięki niej w styczniu nie będziesz zgadywać, kto za co odpowiada, a ewentualne zmiany w przepisach łatwiej naniesiesz na gotowy plan.</p>
<p>Jeśli pracujesz sam, rozpisz te role na siebie i ustaw sobie przypomnienie w kalendarzu na pierwszy tydzień stycznia.</p>
<h2 id="zasoby">Gdzie szukać oficjalnych informacji</h2>
<p>Najpewniejsze źródła to strona ksef.podatki.gov.pl z pytaniami i odpowiedziami KSeF 2.0, podręcznik użytkownika Aplikacji Podatnika oraz komunikaty na gov.pl. Zaglądaj tam co kilka tygodni, bo MF uzupełnia wyjaśnienia, a przy zmianie terminów lub zakresu obowiązków to właśnie tam pojawia się pierwsza informacja. Fora i grupy w mediach społecznościowych traktuj wyłącznie jako inspirację do pytań.</p>
<h2 id="podsumowanie">Podsumowanie</h2>
<p>Dla JDG wdrożenie KSeF to kilka konkretnych kroków: status VAT, dostęp do aplikacji, sposób wystawiania, odbiór faktur kosztowych i przelewy z numerem KSeF. Zacznij od <a href="/ksef-od-2027-jdg/">kwestionariusza KSeF dla JDG</a>, a numery do przelewów sprawdzaj w <a href="/">walidatorze</a>.</p>
""",
    faq=[
        ("Od czego zacząć wdrażanie KSeF w jednoosobowej firmie?", "Od ustalenia statusu VAT i sprawdzenia obowiązków w kwestionariuszu dla JDG, a następnie od rozmowy z księgowym o sposobie wystawiania faktur."),
        ("Czy JDG musi wystawiać faktury w KSeF od 2027 roku?", "Według MF zwolnienie dla faktur do 10 000 zł miesięcznie kończy się 31 grudnia 2026 r., a od 1 stycznia 2027 r. KSeF obejmuje faktury dla innych firm. Faktury dla osób fizycznych bez działalności są dobrowolne."),
        ("Gdzie znajdę Aplikację Podatnika KSeF?", "Na stronie ksef.podatki.gov.pl prowadzonej przez Ministerstwo Finansów."),
        ("Czy trzeba kupić specjalny program?", "Nie ma takiego wymogu w materiałach MF, bo faktury można wystawiać w aplikacji MF. Wybór programu ustal z księgowym."),
    ],
    sources=[MF_TERM, MF_AP, GOV_OSTATNI, MF_PYT2],
)

CAL_POSTS = [C01, C02, C03, C04, C05, C06, C07, C08, C09, C10, C11, C12, C13, C14, C15, C16, C17, C18, C19, C20, C21, C22, C23, C24]

C25 = dict(
    slug="ksef-jdg-ryczalt",
    title="KSeF a JDG na ryczałcie – co się zmienia?",
    desc="Czy ryczałt zwalnia z KSeF? Wyjaśniamy, że obowiązek dotyczy faktur, a nie formy opodatkowania, i co JDG na ryczałcie powinna przygotować przed 2027 r.",
    h1="KSeF a JDG na ryczałcie – co się zmienia",
    intro="Ryczałt upraszcza rozliczenia z podatku dochodowego, ale nie zmienia zasad wystawiania faktur. Sprawdź, co z tego wynika dla twojej firmy.",
    lead_tool=("/ksef-od-2027-jdg/", "kwestionariusz KSeF dla JDG"),
    date=("2026-11-22", "22 listopada 2026"),
    content="""
<h2 id="odpowiedz">Krótka odpowiedź</h2>
<p>Forma opodatkowania dochodu, czyli ryczałt, skala podatkowa lub podatek liniowy, nie decyduje o tym, czy faktura trafia do KSeF. Znaczenie ma to, czy wystawiasz faktury dla innych firm i czy jesteś podatnikiem VAT. Zakres obowiązków zależy od twojej sytuacji, dlatego zacznij od <a href="/ksef-od-2027-jdg/">kwestionariusza KSeF dla JDG</a>, a ostateczne terminy sprawdź na ksef.podatki.gov.pl.</p>
<h2 id="dwa-podatki">Dwa różne podatki – dwa różne obowiązki</h2>
<p>Ryczałt od przychodów ewidencjonowanych to forma rozliczania podatku dochodowego. KSeF dotyczy natomiast faktur ustrukturyzowanych, czyli dokumentów sprzedaży. Te dwie sprawy są od siebie niezależne: przedsiębiorca na ryczałcie może być czynnym podatnikiem VAT albo być zwolniony z VAT, a w obu przypadkach może wystawiać faktury dla firm.</p>
<div class="table-wrap"><table>
<thead><tr><th scope="col">Pytanie</th><th scope="col">Od czego zależy odpowiedź</th></tr></thead>
<tbody>
<tr><td>Czy muszę wystawiać faktury w KSeF?</td><td>od rodzaju nabywcy i obowiązujących terminów MF</td></tr>
<tr><td>Czy podaję numer KSeF w przelewie za zakupy?</td><td>od statusu VAT nabywcy, czyli ciebie jako płatnika</td></tr>
<tr><td>Jak prowadzę ewidencję przychodów?</td><td>od formy opodatkowania, czyli ryczałtu</td></tr>
</tbody></table></div>
<h2 id="przyklad">Przykład: konsultantka IT na ryczałcie</h2>
<p>Marta prowadzi JDG i rozlicza się ryczałtem. Wystawia około dziesięciu faktur miesięcznie dla firm. Z ryczałtu nie wynika dla niej żadne zwolnienie z KSeF. Według komunikatów MF od 1 stycznia 2027 r. faktury dla innych przedsiębiorców wystawia się w systemie, więc Marta ustala z księgowym program fakturowy, a w styczniu sprawdza, czy faktury trafiają do KSeF z numerami.</p>
<h2 id="platnosci">Płatności za zakupy firmowe</h2>
<p>Jeśli kupujesz towary lub usługi dla firmy, a twoja firma jest czynnym podatnikiem VAT, przy płatności za fakturę z KSeF podajesz numer KSeF lub identyfikator zbiorczy (art. 108g ustawy o VAT). Jeśli jesteś zwolniony z VAT, przeczytaj tekst <a href="/blog/czy-jdg-bez-vat-podaje-numer-ksef/">JDG zwolniona z VAT a numer KSeF</a>. Numer przed przelewem sprawdzisz w <a href="/">walidatorze numeru KSeF</a>.</p>
<h2 id="ewidencja">Ewidencja przychodów a numer KSeF</h2>
<p>Przepisy o ewidencji przychodów dla ryczałtu nie wymagają od ciebie wpisywania numeru KSeF do ewidencji; to, czy księgowy zechce mieć go w kolumnie, jest kwestią organizacji pracy. Praktycznie warto zapisywać numer przy każdej fakturze, bo ułatwia to wyszukiwanie i korektę. Więcej o ewidencji kosztów piszemy w tekście <a href="/blog/numer-ksef-w-kpir/">numer KSeF w KPiR</a>.</p>
<h2 id="co-zrobic">Co zrobić przed 2027 rokiem</h2>
<ol class="steps">
<li>Ustal status VAT swojej firmy.</li>
<li>Sprawdź obowiązki w kwestionariuszu.</li>
<li>Wejdź do Aplikacji Podatnika KSeF i zobacz, jak wyglądają faktury.</li>
<li>Uzgodnij z księgowym, kto pobiera faktury kosztowe.</li>
<li>Przećwicz kopiowanie numeru do przelewu.</li>
</ol>
<p>Pełną listę kroków znajdziesz w artykule <a href="/blog/ksef-jdg-od-czego-zaczac/">KSeF w JDG – od czego zacząć</a>.</p>
<h2 id="mity">Częste nieporozumienia</h2>
<ul>
<li>„Jestem na ryczałcie, więc KSeF mnie nie dotyczy” – forma opodatkowania nie jest kryterium wystawiania faktur w KSeF.</li>
<li>„Skoro nie jestem w VAT, nie muszę nic robić” – część obowiązków może cię nadal dotyczyć, zwłaszcza przy wystawianiu faktur firmom.</li>
<li>„Księgowy zrobi wszystko za mnie” – to dobry pomysł, ale płatności i obieg dokumentów nadal są po twojej stronie.</li>
</ul>
<h2 id="przyklad-2">Przykład: warsztat z fakturami dla firm i klientów prywatnych</h2>
<p>Pan Tomasz prowadzi warsztat na ryczałcie. Większość klientów to osoby prywatne, ale kilka firm flotowych dostaje faktury co miesiąc. Według komunikatów MF faktury dla osób fizycznych nieprowadzących działalności są w KSeF dobrowolne, natomiast faktury dla firm trzeba wystawiać w systemie. Dlatego Tomasz wybiera program, który obsługuje oba rodzaje sprzedaży, i prosi księgową o sprawdzenie, jak zapisywać numery KSeF w ewidencji.</p>
<h2 id="kontrola">Lista kontrolna na grudzień</h2>
<div class="table-wrap"><table>
<thead><tr><th scope="col">Pozycja</th><th scope="col">Gotowe, gdy</th></tr></thead>
<tbody>
<tr><td>program do faktur</td><td>wystawiłeś fakturę próbną lub testową</td></tr>
<tr><td>dostęp do aplikacji MF</td><td>umiesz wyszukać i pobrać fakturę</td></tr>
<tr><td>przelewy</td><td>numer przechodzi do banku bez przepisywania</td></tr>
<tr><td>ustalenia z księgowym</td><td>wiadomo, kto odbiera faktury kosztowe</td></tr>
</tbody></table></div>
<h2 id="rozmowa">Pytania do księgowego przy ryczałcie</h2>
<p>Zanim zaczniesz wdrożenie, zapytaj księgowego o pięć spraw: w jakim programie będą wystawiane faktury, kto pobiera faktury kosztowe z KSeF, czy numer KSeF ma trafiać do ewidencji, jak wygląda procedura płatności z numerem oraz kto odpowiada za sprawdzanie komunikatów MF. Odpowiedzi zapisz w jednej notatce. W małej firmie, gdzie wszystko robisz sam, taka notatka pełni rolę instrukcji na styczeń i oszczędza zgadywania, a gdy zmienią się przepisy, łatwo ją zaktualizować.</p>
<p>Warto też ustawić sobie przypomnienie, by w pierwszym tygodniu stycznia 2027 r. przejrzeć pierwsze faktury z KSeF i sprawdzić, czy numery trafiły do ewidencji oraz czy przelewy mają poprawny opis. Jeśli coś się nie zgadza, lepiej poprawić proces od razu niż po kilku miesiącach, gdy zbierze się wiele dokumentów do korekty.</p>
<h2 id="zrodla-info">Gdzie sprawdzać zmiany</h2>
<p>Terminy i zakres obowiązków mogą się zmieniać. Najpewniejsze źródła to ksef.podatki.gov.pl, komunikaty na gov.pl i ISAP. Nie podajemy tu kar ani ich terminów, bo ich status trzeba sprawdzać w obowiązujących przepisach. Tekst ma charakter ogólny i nie zastępuje porady księgowego, więc nietypowe przypadki omów ze specjalistą.</p>
<h2 id="ryczalt-vs-vat">Ryczałt a zwolnienie z VAT – nie to samo</h2>
<p>Częsty błąd to utożsamianie ryczałtu ze zwolnieniem z VAT. To dwa osobne ustawienia: jedno dotyczy podatku dochodowego, drugie podatku od towarów i usług. Możesz być ryczałtowcem i czynnym podatnikiem VAT, a także ryczałtowcem zwolnionym z VAT. Dlatego odpowiadając na pytanie o obowiązki w KSeF, zawsze zaczynaj od statusu VAT i rodzaju nabywców, a nie od formy rozliczenia dochodu. Jeśli masz wątpliwości, spisz oba ustawienia na jednej kartce i pokaż ją księgowemu.</p>
<h2 id="podsumowanie">Podsumowanie</h2>
<p>Ryczałt nie wyłącza cię z KSeF, bo system dotyczy faktur, a nie formy podatku dochodowego. Sprawdź swoje obowiązki w <a href="/ksef-od-2027-jdg/">kwestionariuszu KSeF dla JDG</a>, a numery do przelewów weryfikuj w <a href="/">walidatorze</a>. Dzięki temu styczeń 2027 r. nie będzie dla ciebie niespodzianką.</p>
""",
    faq=[
        ("Czy ryczałt zwalnia z KSeF?", "Nie wynika to z materiałów MF. KSeF dotyczy faktur, a nie formy opodatkowania dochodu, więc o obowiązkach decydują rodzaj sprzedaży i status VAT."),
        ("Czy JDG na ryczałcie podaje numer KSeF w przelewie?", "Obowiązek z art. 108g dotyczy płatności za faktury z KSeF dokonywanych przez czynnych podatników VAT. Jeśli nie jesteś czynnym podatnikiem, sprawdź to w komunikatach MF lub u księgowego."),
        ("Czy numer KSeF trzeba wpisywać do ewidencji ryczałtowca?", "Nie znaleźliśmy takiego wymogu w materiałach MF. Zapisywanie numeru jest jednak praktyczne, więc ustal to z księgowym."),
        ("Gdzie sprawdzić aktualne terminy KSeF?", "Na stronie ksef.podatki.gov.pl w zakładce o podstawach prawnych i kluczowych terminach."),
    ],
    sources=[MF_TERM, MF_AP, GOV_OSTATNI, MF_PYT2],
)

C26 = dict(
    slug="uzgadnianie-wyciagu-bankowego-numery-ksef",
    title="Wyciąg bankowy i numery KSeF – jak uzgadniać?",
    desc="Jak uzgodnić wyciąg bankowy z fakturami z KSeF: numer KSeF w opisie przelewu ułatwia parowanie płatności. Przykład tabeli i sposób kontroli plików CSV.",
    h1="Wyciąg bankowy i numery KSeF – jak uzgadniać płatności",
    intro="Numer KSeF w tytule przelewu może skrócić uzgadnianie wyciągu z fakturami. Pokazujemy, jak to zorganizować i jak sprawdzić większą liczbę numerów naraz.",
    lead_tool=("/sprawdz-wiele-numerow-ksef/", "sprawdzarkę zbiorczą numerów KSeF"),
    date=("2026-11-22", "22 listopada 2026"),
    content="""
<h2 id="odpowiedz">Krótka odpowiedź</h2>
<p>Uzgadnianie polega na zestawieniu wpłat i wypłat z wyciągu z listą faktur. Jeśli w opisie przelewu znajduje się numer KSeF, możesz parować płatność z fakturą po jednym unikalnym kluczu. Przed importem pliku sprawdź numery w <a href="/sprawdz-wiele-numerow-ksef/">sprawdzarce zbiorczej numerów KSeF</a>, żeby wychwycić literówki.</p>
<h2 id="dlaczego">Dlaczego numer KSeF pomaga</h2>
<p>Numer faktury nadany przez sprzedawcę może się powtarzać u różnych dostawców. Numer KSeF jest nadawany przez system i ma 35 znaków, więc nadaje się na identyfikator dokumentu. Budowę numeru opisuje dokumentacja MF; jeśli chcesz ją poznać, zajrzyj do tekstu <a href="/blog/z-czego-sklada-sie-numer-ksef/">z czego składa się numer KSeF</a>.</p>
<h2 id="tabela">Przykładowy arkusz uzgodnień</h2>
<div class="table-wrap"><table>
<thead><tr><th scope="col">Data</th><th scope="col">Kwota</th><th scope="col">Opis na wyciągu</th><th scope="col">Faktura</th><th scope="col">Status</th></tr></thead>
<tbody>
<tr><td>02.01.2027</td><td>1 230,00</td><td>numer KSeF w opisie</td><td>FV 15/2026</td><td>uzgodniona</td></tr>
<tr><td>03.01.2027</td><td>615,00</td><td>numer KSeF w opisie</td><td>FV 8/2027</td><td>uzgodniona</td></tr>
<tr><td>04.01.2027</td><td>2 000,00</td><td>brak numeru</td><td>do wyjaśnienia</td><td>otwarta</td></tr>
</tbody></table></div>
<p>Dane są przykładowe. W praktyce kolumnę z numerem KSeF dodajesz obok numeru faktury.</p>
<h2 id="kroki">Jak uzgadniać krok po kroku</h2>
<ol class="steps">
<li>Pobierz wyciąg z banku w pliku CSV lub w formacie, który obsługuje twój program.</li>
<li>Wyodrębnij z opisów ciągi długości 35 znaków i sprawdź je w sprawdzarce zbiorczej.</li>
<li>Połącz numery z listą faktur pobraną z KSeF lub z programu księgowego.</li>
<li>Oznacz płatności bez numeru jako do wyjaśnienia.</li>
<li>Porównaj sumy: wpłaty z wyciągu i kwoty faktur.</li>
</ol>
<h2 id="przyklad">Przykład: sklep hurtowy z dwudziestoma płatnościami dziennie</h2>
<p>Hurtownia otrzymuje dziennie około dwudziestu przelewów. Dotąd księgowa szukała faktur po kwocie i nazwie kontrahenta, a przy podobnych kwotach traciła czas. Po wprowadzeniu praktyki, że klienci wpisują numer KSeF w opisie, dopasowanie odbywa się automatycznie, a ręcznie weryfikowane są tylko wpłaty bez numeru. Hurtownia prosi klientów o kopiowanie numeru z faktury, a nie o jego przepisywanie.</p>
<h2 id="grupowe">Jedna wpłata za wiele faktur</h2>
<p>Gdy kontrahent płaci za kilka faktur jednym przelewem, w opisie może się pojawić identyfikator zbiorczy. Jak go przygotować, opisujemy w tekście <a href="/blog/jak-wygenerowac-identyfikator-zbiorczy-ksef/">jak wygenerować identyfikator zbiorczy KSeF</a>, a sprawdzisz go w <a href="/identyfikator-zbiorczy-ksef/">sprawdzarce identyfikatora zbiorczego</a>. Przy uzgadnianiu taki przelew rozbijasz na poszczególne faktury według zestawienia, które przygotował płatnik.</p>
<h2 id="bledy">Najczęstsze problemy</h2>
<ul>
<li>numer przepisany z błędem – kontrola sumy CRC w sprawdzarce wychwytuje część pomyłek,</li>
<li>spacje lub łamanie wiersza w opisie – usuń je przed porównaniem,</li>
<li>skrócony opis, bo bank ucina część tytułu – sprawdź limit znaków w swoim banku,</li>
<li>jeden przelew za kilka faktur bez zestawienia,</li>
<li>faktura korygująca z innym numerem KSeF niż faktura pierwotna.</li>
</ul>
<p>Dla korekt przeczytaj <a href="/blog/numer-ksef-faktury-korygujacej/">numer KSeF faktury korygującej</a>.</p>
<h2 id="csv">Kontrola numerów z pliku CSV</h2>
<p>Jeśli masz wiele pozycji, wklej numery do <a href="/sprawdz-wiele-numerow-ksef/">sprawdzarki zbiorczej</a>. Narzędzie liczy sumę kontrolną i pokazuje, które numery są poprawne formalnie. Pamiętaj, że poprawna suma nie dowodzi, że faktura istnieje w KSeF. Przetwarzanie odbywa się w twojej przeglądarce, więc dane nie są wysyłane na serwer.</p>
<h2 id="rytm">Jak często uzgadniać</h2>
<p>Przy dużej liczbie płatności najwygodniej uzgadniać wyciąg codziennie albo co kilka dni, bo wtedy niewyjaśnione przelewy są świeże i łatwo dopytać kontrahenta. Przy małej firmie wystarczy raz w tygodniu. Niezależnie od rytmu trzymaj stały schemat: pobranie wyciągu, kontrola numerów, zestawienie z fakturami, lista pozycji do wyjaśnienia i krótka notatka, co zrobiono. Takie podejście pozwala szybko znaleźć błąd, gdy suma na koniec miesiąca się nie zgadza.</p>
<p>Warto też przechowywać kopię arkusza uzgodnień razem z wyciągiem bankowym. Gdy później ktoś zapyta, dlaczego dana płatność została przypisana do danej faktury, odpowiedź będzie od ręki. Pamiętaj, aby numery KSeF zapisywać w osobnej kolumnie, bez spacji i łamania wierszy, bo ułatwia to filtrowanie i porównywanie w arkuszu kalkulacyjnym.</p>
<h2 id="kontrahenci">Jak prosić kontrahentów o poprawny opis</h2>
<p>Najprostszy sposób to dodać do stopki maila z fakturą jedno zdanie: „W tytule przelewu prosimy o skopiowanie numeru KSeF z faktury”. Część klientów nadal będzie pisać opis po swojemu, ale większość skorzysta z podpowiedzi. Gdy ktoś płaci bez numeru, nie odrzucaj wpłaty; zestaw ją ręcznie z fakturą po kwocie i nazwie, a następnie uprzejmie przypomnij o numerze przy kolejnej płatności. Dobrze jest też prowadzić listę klientów, którzy często pomijają numer, bo to oni generują najwięcej pracy przy uzgadnianiu.</p>
<p>W sporach o to, która faktura została opłacona, numer KSeF pomaga jednoznacznie wskazać dokument, bo nie powtarza się u różnych sprzedawców. Dzięki temu rozmowa z kontrahentem jest krótsza, a ewentualne wyjaśnienia nie wymagają przeglądania całej korespondencji ani archiwum faktur z kilku miesięcy.</p>
<h2 id="limity">Czego narzędzie nie robi</h2>
<p>Sprawdzarka nie łączy się z bankiem ani z KSeF i nie zaksięguje płatności. Nie podajemy też terminów ani kar, bo ich status trzeba weryfikować w oficjalnych źródłach: ksef.podatki.gov.pl, gov.pl i ISAP. Zasady księgowania omów z księgowym.</p>
<h2 id="arkusz-wskazowki">Wskazówki do arkusza</h2>
<p>W arkuszu kalkulacyjnym przydaje się kolumna pomocnicza, która sprawdza długość numeru i usuwa spacje, oraz osobna kolumna ze statusem uzgodnienia. Dzięki filtrowi po statusie szybko zobaczysz, które wpłaty czekają na wyjaśnienie. Na koniec miesiąca porównaj sumę uzgodnionych pozycji z saldem z wyciągu i zapisz różnicę, jeśli występuje. Jasna dokumentacja takich różnic oszczędza czas przy zamknięciu ksiąg i rozmowie z księgowym.</p>
<h2 id="przyklad-dalej">Przykład: pierwszy tydzień stycznia</h2>
<p>Biuro rachunkowe obsługujące kilkanaście małych firm w pierwszym tygodniu stycznia 2027 r. prosi każdego klienta o przesłanie wyciągu oraz listy faktur z numerami KSeF. Księgowa zestawia je w jednym arkuszu, oznacza pozycje bez numeru i wysyła klientom krótką listę pytań. Dzięki temu po pierwszym miesiącu wie, którzy klienci kopiują numer poprawnie, a którym trzeba przypomnieć o zasadach opisu płatności.</p>
<h2 id="podsumowanie">Podsumowanie</h2>
<p>Numer KSeF w opisie przelewu to wygodny klucz do uzgadniania wyciągu. Zadbaj, by numery były kopiowane, a przed importem sprawdzaj je w <a href="/sprawdz-wiele-numerow-ksef/">sprawdzarce zbiorczej</a>. Pojedynczy numer zweryfikujesz w <a href="/">walidatorze</a>.</p>
""",
    faq=[
        ("Czy numer KSeF ułatwia uzgadnianie wyciągu bankowego?", "Tak, bo to unikalny identyfikator dokumentu, który można zestawić z listą faktur zamiast szukać po kwocie."),
        ("Jak uzgodnić jeden przelew za wiele faktur?", "Poproś płatnika o zestawienie lub użyj identyfikatora zbiorczego i rozbij wpłatę na faktury według tego zestawienia."),
        ("Czy poprawna suma CRC oznacza, że faktura istnieje?", "Nie. Suma kontrolna potwierdza tylko formalną poprawność numeru, a istnienie faktury sprawdzasz w KSeF."),
        ("Czy dane z pliku są wysyłane na serwer?", "Nie, sprawdzarka działa w przeglądarce i nie wysyła wklejonych numerów."),
    ],
    sources=[MF_NUM, DOC_NUM, MF_PYT2, GOV_OSTATNI],
)

C27 = dict(
    slug="numer-ksef-na-paragonie-z-nip",
    title="Numer KSeF na paragonie z NIP i fakturze z kasy",
    desc="Czy paragon z NIP ma numer KSeF? Wyjaśniamy różnicę między paragonem a fakturą ustrukturyzowaną oraz gdzie szukać numeru KSeF przy zakupach firmowych.",
    h1="Numer KSeF na paragonie z NIP i fakturze z kasy",
    intro="Paragon z NIP to nie faktura. Numer KSeF otrzymuje dopiero faktura ustrukturyzowana przyjęta przez system. Sprawdź, co z tego wynika przy zakupach firmowych.",
    lead_tool=("/ksef-od-2027-jdg/", "kwestionariusz KSeF dla JDG"),
    date=("2026-11-22", "22 listopada 2026"),
    content="""
<h2 id="odpowiedz">Krótka odpowiedź</h2>
<p>Paragon fiskalny, także z NIP nabywcy, nie jest fakturą ustrukturyzowaną i nie ma numeru KSeF. Numer nadaje system po przyjęciu faktury. Jeśli chcesz mieć numer KSeF przy zakupie firmowym, potrzebna jest faktura wystawiona w KSeF. Ogólne obowiązki sprawdzisz w <a href="/ksef-od-2027-jdg/">kwestionariuszu KSeF dla JDG</a>, a aktualne zasady dla faktur z kas – w komunikatach MF.</p>
<h2 id="roznica">Paragon, faktura z kasy i faktura w KSeF</h2>
<div class="table-wrap"><table>
<thead><tr><th scope="col">Dokument</th><th scope="col">Numer KSeF</th><th scope="col">Uwagi</th></tr></thead>
<tbody>
<tr><td>paragon fiskalny</td><td>nie</td><td>dokument z kasy, nie faktura ustrukturyzowana</td></tr>
<tr><td>paragon z NIP nabywcy</td><td>nie</td><td>NIP na paragonie nie zastępuje faktury</td></tr>
<tr><td>faktura wystawiona w KSeF</td><td>tak</td><td>numer nadaje system po przyjęciu faktury</td></tr>
</tbody></table></div>
<p>Zasady dotyczące faktur wystawianych z kas rejestrujących oraz okres przejściowy zmieniały się w komunikatach MF, dlatego sprawdź bieżące wyjaśnienia na ksef.podatki.gov.pl, zanim ustalisz procedury w firmie.</p>
<h2 id="przyklad">Przykład: zakup materiałów biurowych</h2>
<p>Pani Ewa kupuje w sklepie papier i tonery dla swojej JDG. Przy kasie podaje NIP, a sprzedawca drukuje paragon. Na paragonie nie ma numeru KSeF, więc nie ma czego wpisać w tytule przelewu, bo za zakup zapłaciła od razu kartą. Gdyby sklep wystawił fakturę na jej firmę i przekazał ją przez KSeF, Ewa znalazłaby fakturę z numerem w aplikacji MF i mogłaby go wykorzystać, gdyby płaciła później przelewem.</p>
<h2 id="platnosc">Kiedy numer KSeF jest potrzebny w płatności</h2>
<p>Obowiązek podania numeru w przelewie dotyczy płatności za fakturę z KSeF dokonywanej przez czynnego podatnika VAT (art. 108g ustawy o VAT). Jeśli płacisz na miejscu kartą lub gotówką, sprawa wygląda inaczej niż przy przelewie. Szczegóły omawiamy w tekście <a href="/blog/czy-numer-ksef-musi-byc-w-tytule-przelewu/">czy numer KSeF musi być w tytule przelewu</a>. Numer przed zleceniem przelewu możesz sprawdzić w <a href="/">walidatorze numeru KSeF</a>.</p>
<h2 id="gdzie">Gdzie znaleźć numer KSeF</h2>
<ul>
<li>w Aplikacji Podatnika KSeF, w szczegółach pobranej faktury,</li>
<li>na wizualizacji faktury, gdy zawiera kod QR,</li>
<li>w programie fakturowym lub księgowym zintegrowanym z KSeF.</li>
</ul>
<p>Więcej o lokalizacji numeru piszemy w artykułach <a href="/blog/kod-qr-ksef-co-zawiera/">co zawiera kod QR KSeF</a> oraz <a href="/blog/jak-otworzyc-plik-xml-ksef/">jak otworzyć plik XML z KSeF</a>.</p>
<h2 id="kroki">Co zrobić, gdy masz tylko paragon</h2>
<ol class="steps">
<li>Zapytaj sprzedawcę, czy wystawi fakturę na firmę.</li>
<li>Sprawdź w komunikatach MF, jak obecnie wygląda dokumentowanie sprzedaży z kasy.</li>
<li>Zachowaj paragon zgodnie z zaleceniami księgowego.</li>
<li>Gdy faktura trafi do KSeF, pobierz ją z aplikacji i zapisz numer.</li>
</ol>
<h2 id="przyklad-2">Przykład: stacja paliw i firma transportowa</h2>
<p>Kierowca firmowy tankuje auto i prosi o fakturę na NIP firmy. Stacja może wystawić dokument według zasad obowiązujących w danym okresie. Księgowa po kilku dniach wyszukuje fakturę w KSeF po dacie i sprzedawcy, zapisuje numer w ewidencji i dopiero wtedy zleca ewentualne przelewy. Dzięki temu nie opiera się na samym paragonie, który numeru nie zawiera.</p>
<h2 id="bledy">Częste pomyłki</h2>
<ul>
<li>szukanie numeru KSeF na paragonie,</li>
<li>założenie, że NIP na paragonie oznacza fakturę,</li>
<li>wpisywanie w tytule przelewu numeru paragonu zamiast numeru KSeF,</li>
<li>brak ustalenia, kto w firmie prosi o faktury po zakupach.</li>
</ul>
<h2 id="praktyka">Dobre nawyki przy zakupach firmowych</h2>
<p>Jeśli często kupujesz drobne rzeczy dla firmy, ustal prostą zasadę: przy każdym zakupie, który ma być kosztem, od razu proś o fakturę na firmę, zamiast liczyć na to, że uda się ją uzyskać później. Faktura przekazana przez KSeF trafia do aplikacji, gdzie wyszukasz ją po dacie, NIP sprzedawcy lub kwocie. Dzięki temu masz komplet dokumentów w jednym miejscu, a księgowa nie musi zbierać paragonów w pudełku.</p>
<p>W firmie z kilkoma pracownikami przygotuj krótką instrukcję: kto prosi o fakturę, komu ją przekazuje i gdzie zapisuje numer KSeF. Taka instrukcja zajmuje pół strony, a znacznie ogranicza liczbę pytań w pierwszych tygodniach stycznia. Pamiętaj, że zasady dla sprzedaży z kas mogą się zmieniać, więc instrukcję trzeba okresowo sprawdzać. Dobrze też ustalić, kto w firmie ma dostęp do aplikacji i kto może pobierać faktury kosztowe, aby dokumenty nie wisiały u jednej osoby.</p>
<p>Jeśli zakupy robisz głównie online, dopisz w formularzu zamówienia dane firmy i NIP oraz wybierz opcję faktury. Po kilku dniach sprawdź w aplikacji, czy faktura jest dostępna, i zapisz jej numer KSeF. Takie sprawdzenie raz w tygodniu wystarczy, żeby żadna faktura nie umknęła przed końcem miesiąca.</p>
<h2 id="zrodla-info">Źródła i zastrzeżenia</h2>
<p>Zasady wystawiania faktur z kas i okresy przejściowe warto weryfikować na ksef.podatki.gov.pl, gov.pl i w ISAP. Nie podajemy tu kar ani ich terminów. Artykuł jest ogólnym omówieniem, nie doradztwem podatkowym.</p>
<h2 id="uwaga-kasa">Uwaga o dokumentach z kasy</h2>
<p>Jeśli prowadzisz sprzedaż z kasy i klienci proszą o faktury, śledź komunikaty MF dotyczące faktur wystawianych z kas rejestrujących i terminów przejściowych. Przepisy w tym obszarze były doprecyzowywane, więc dobrze jest raz na kilka tygodni sprawdzić stronę ksef.podatki.gov.pl i zapytać dostawcę kasy lub programu, jak wygląda obsługa faktur w KSeF. Zapisz odpowiedź w firmowej instrukcji, aby cały zespół postępował tak samo.</p>
<h2 id="faktura-do-paragonu">Przykład: faktura po zakupie online</h2>
<p>Firma zamawia sprzęt w sklepie internetowym i w formularzu zaznacza zakup na fakturę. Po kilku dniach księgowa wyszukuje fakturę w aplikacji KSeF po dacie i NIP sprzedawcy, zapisuje numer i dopiero wtedy opłaca zamówienie przelewem z tym numerem w opisie. Paragonu w takim przypadku nie ma, więc nie ma też ryzyka pomylenia numeru dokumentu z numerem KSeF.</p>
<h2 id="podsumowanie">Podsumowanie</h2>
<p>Numer KSeF ma faktura ustrukturyzowana, a nie paragon. Jeśli kupujesz dla firmy i potrzebujesz numeru, poproś o fakturę, pobierz ją z aplikacji i sprawdź numer w <a href="/">walidatorze</a>. Swoje obowiązki sprawdzisz w <a href="/ksef-od-2027-jdg/">kwestionariuszu dla JDG</a>.</p>
""",
    faq=[
        ("Czy paragon z NIP ma numer KSeF?", "Nie. Numer KSeF nadaje system faktury ustrukturyzowanej, a paragon nie jest taką fakturą."),
        ("Gdzie znajdę numer KSeF faktury za zakup firmowy?", "W Aplikacji Podatnika KSeF w szczegółach faktury, na wizualizacji z kodem QR lub w programie zintegrowanym z KSeF."),
        ("Czy przy płatności kartą w sklepie podaję numer KSeF?", "Obowiązek z art. 108g dotyczy płatności za faktury z KSeF, więc zakup z paragonem i płatnością na miejscu to inna sytuacja. Zasady sprawdź w komunikatach MF lub u księgowego."),
        ("Czy sprzedawca musi wystawić fakturę do paragonu?", "Zasady zależą od przepisów i okresów przejściowych, dlatego sprawdź aktualne wyjaśnienia MF na ksef.podatki.gov.pl."),
    ],
    sources=[MF_TERM, MF_PYT2, GOV_OSTATNI, MF_AP],
)

CAL_POSTS = CAL_POSTS + [C25, C26, C27]

C28 = dict(
    slug="wizualizacja-faktury-ksef-jak-wyglada",
    title="Wizualizacja faktury KSeF – jak wygląda PDF?",
    desc="Jak wygląda wizualizacja faktury KSeF, czym różni się od pliku XML i gdzie na niej szukać numeru KSeF oraz kodu QR. Praktyczny przewodnik dla firm.",
    h1="Wizualizacja faktury KSeF – jak wygląda PDF?",
    intro="Faktura w KSeF to plik XML, a PDF jest tylko jego czytelnym podglądem. Zobacz, co zawiera wizualizacja i gdzie na niej znaleźć numer KSeF oraz kod QR.",
    lead_tool=("/kod-qr-ksef/", "sprawdzanie i budowanie kodu QR KSeF"),
    date=("2026-11-23", "23 listopada 2026"),
    content="""
<h2 id="odpowiedz">Krótka odpowiedź</h2>
<p>Prawdziwą fakturą w KSeF jest plik XML w strukturze FA(3). Wizualizacja, czyli PDF lub wydruk, to jedynie czytelny podgląd danych z tego pliku. Na wizualizacji powinny być widoczne dane stron, pozycje, kwoty i oznaczenia KSeF, w tym numer KSeF oraz kod QR. Kod QR sprawdzisz w narzędziu <a href="/kod-qr-ksef/">kod QR KSeF – sprawdzanie i budowanie</a>.</p>
<h2 id="xml-pdf">XML a PDF: co jest fakturą</h2>
<div class="table-wrap"><table>
<thead><tr><th scope="col">Cecha</th><th scope="col">Plik XML</th><th scope="col">Wizualizacja (PDF)</th></tr></thead>
<tbody>
<tr><td>rola</td><td>faktura ustrukturyzowana</td><td>czytelny podgląd danych</td></tr>
<tr><td>numer KSeF</td><td>nadaje system po przyjęciu faktury</td><td>pokazany na wydruku obok kodu QR</td></tr>
<tr><td>do kogo trafia</td><td>do KSeF, skąd pobiera go nabywca</td><td>można przekazać dodatkowo, np. mailem</td></tr>
<tr><td>do przelewu</td><td>źródło danych: konto, kwota, termin</td><td>pomocniczo, do odczytu</td></tr>
</tbody></table></div>
<h2 id="elementy">Co zwykle widać na wizualizacji</h2>
<ul>
<li>dane sprzedawcy i nabywcy oraz ich numery NIP,</li>
<li>numer faktury nadany przez sprzedawcę (pole P_2) i data wystawienia (P_1),</li>
<li>tabela pozycji z cenami, stawkami VAT i sumami,</li>
<li>termin i forma płatności oraz rachunek bankowy, jeśli wystawca je podał,</li>
<li>numer KSeF i kod QR do weryfikacji faktury.</li>
</ul>
<p>Wygląd zależy od programu lub aplikacji, która tworzy wizualizację, bo układ nie jest narzucony jednym wzorem. Dane merytoryczne pochodzą zawsze z XML, więc w razie wątpliwości liczy się plik, a nie PDF. Strukturę pól opisuje <a href="/blog/jak-otworzyc-plik-xml-ksef/">artykuł o otwieraniu pliku XML z KSeF</a>.</p>
<h2 id="numer">Gdzie na PDF szukać numeru KSeF</h2>
<p>Numer ma 35 znaków: datę, NIP sprzedawcy, część techniczną i dwie cyfry kontrolne. Zwykle znajdziesz go w pobliżu kodu QR. Jeśli skopiowałeś go z PDF, wklej go do <a href="/">walidatora numeru KSeF</a>, który sprawdzi sumę kontrolną i datę. Budowę numeru wyjaśnia tekst <a href="/blog/jak-wyglada-numer-ksef-przyklad/">jak wygląda numer KSeF – przykład</a>.</p>
<h2 id="qr">Kod QR na wizualizacji</h2>
<p>Zgodnie z dokumentacją MF kod QR typu KOD I zawiera adres serwisu weryfikacji, datę wystawienia faktury z pola P_1, NIP sprzedawcy oraz skrót pliku faktury (SHA-256 w formacie Base64URL). Dzięki temu odbiorca może sprawdzić, czy dokument odpowiada fakturze w systemie. Szczegóły omawia artykuł <a href="/blog/kod-qr-ksef-co-zawiera/">co zawiera kod QR KSeF</a>.</p>
<h2 id="przyklad">Przykład: księgowa sprawdza fakturę od dostawcy</h2>
<p>Dostawca wysyła mailem PDF. Księgowa otwiera Aplikację Podatnika, wyszukuje fakturę po dacie i NIP sprzedawcy, pobiera XML i porównuje sumę brutto oraz numer rachunku z PDF. Numer KSeF z aplikacji zgadza się z tym na wydruku, więc może zlecić przelew z numerem w tytule. Gdyby kwoty się różniły, wiążący byłby plik w KSeF, a nie załącznik z poczty.</p>
<h2 id="kroki">Jak sprawdzić, czy PDF jest zgodny z fakturą</h2>
<ol class="steps">
<li>Odczytaj numer KSeF z wizualizacji.</li>
<li>Sprawdź go w <a href="/">walidatorze</a>, by wykluczyć literówkę.</li>
<li>Znajdź fakturę w Aplikacji Podatnika KSeF po numerze lub dacie.</li>
<li>Porównaj sprzedawcę, kwotę brutto i rachunek z danymi z XML.</li>
<li>Dopiero potem zleć przelew z numerem KSeF w tytule.</li>
</ol>
<h2 id="platnosc">Wizualizacja a płatność</h2>
<p>Numer rachunku i kwotę do zapłaty najlepiej brać z XML lub z aplikacji, a nie przepisywać ręcznie z PDF. Jeśli chcesz zobaczyć dane gotowe do przelewu, wklej plik do narzędzia <a href="/przelew-z-faktury-xml-ksef/">przelew z faktury XML</a>. Zasady dotyczące opisu przelewu opisujemy w tekście <a href="/blog/czy-numer-ksef-musi-byc-w-tytule-przelewu/">czy numer KSeF musi być w tytule przelewu</a>.</p>
<h2 id="bledy">Częste pomyłki</h2>
<ul>
<li>traktowanie PDF jako oryginału faktury,</li>
<li>płacenie na rachunek z samego maila lub PDF bez porównania z XML,</li>
<li>przepisywanie numeru KSeF z błędami, zwłaszcza w znakach podobnych do siebie,</li>
<li>zakładanie, że każdy program generuje wizualizację w identycznym układzie.</li>
</ul>
<h2 id="praktyka">Dobre nawyki w firmie</h2>
<p>Ustal, kto w firmie pobiera faktury z KSeF i gdzie zapisuje numer. Wizualizacje przechowuj razem z numerem KSeF, żeby przy rozliczeniu można było łatwo wrócić do faktury w systemie. Dla wielu faktur naraz skorzystaj z <a href="/sprawdz-wiele-numerow-ksef/">sprawdzania wielu numerów KSeF</a>. Pamiętaj, że w razie wątpliwości co do danych wiążący jest plik XML przyjęty przez KSeF.</p>
<p>Warto też przetestować, jak wizualizacje wyglądają w używanym programie fakturowym: wystaw fakturę testową, sprawdź czy widać na niej numer KSeF, kod QR, rachunek i termin płatności. Jeśli czegoś brakuje, zapytaj dostawcę oprogramowania, jak je włączyć. Dzięki temu klienci i księgowi dostaną komplet danych, a Ty unikniesz zbędnych pytań o to, gdzie znaleźć numer.</p>
<p>Jeśli odbierasz faktury od wielu dostawców, zwróć uwagę, że ich PDF-y mogą wyglądać zupełnie inaczej. To normalne, ponieważ układ zależy od programu. Zawsze szukaj tych samych elementów: numeru KSeF, NIP sprzedawcy, daty, kwoty brutto i rachunku. Gdy brakuje któregoś z nich, sięgnij do XML w aplikacji MF.</p>
<h2 id="wydruk">Wydruk, zapis i archiwizacja</h2>
<p>Wizualizację możesz wydrukować lub zapisać jako PDF, ale pamiętaj, że przechowujesz w ten sposób tylko podgląd. Dobrą praktyką jest archiwizowanie razem z nią pliku XML oraz numeru KSeF. Dzięki temu po latach odtworzysz fakturę bez zgadywania, który dokument był pierwotny. Zapytaj księgowego, w jakiej formie chce otrzymywać dokumenty kosztowe, i ustalcie jeden schemat nazewnictwa plików, na przykład data, sprzedawca i numer KSeF.</p>
<h2 id="mobilnie">Wizualizacja na telefonie</h2>
<p>Przy odbiorze faktur na telefonie wygodnie jest zeskanować kod QR z wydruku i porównać dane z tym, co widzisz w aplikacji. Jeśli dokument wygląda podejrzanie lub kod prowadzi na nieznaną stronę, nie płać i skontaktuj się ze sprzedawcą innym kanałem niż wiadomość, w której przyszedł plik.</p>
<h2 id="zrodla-info">Źródła i zastrzeżenia</h2>
<p>Opis kodów QR oparto na dokumentacji i stronach MF (ksef.podatki.gov.pl). Nie podajemy kar ani terminów sankcji. Tekst jest ogólnym omówieniem, nie doradztwem podatkowym.</p>
<h2 id="podsumowanie">Podsumowanie</h2>
<p>Wizualizacja faktury KSeF to wygodny podgląd, ale źródłem danych jest XML. Znajdź na niej numer KSeF i kod QR, sprawdź je w <a href="/kod-qr-ksef/">narzędziu do kodów QR</a> i <a href="/">walidatorze numeru</a>, a płać na podstawie danych z systemu.</p>
""",
    faq=[
        ("Czy PDF z KSeF jest oryginałem faktury?", "Nie. Fakturą ustrukturyzowaną jest plik XML przyjęty przez KSeF, a PDF to jego wizualizacja."),
        ("Czy każda wizualizacja wygląda tak samo?", "Nie. Układ zależy od programu lub aplikacji, ale dane pochodzą z tego samego pliku XML."),
        ("Gdzie na wizualizacji jest numer KSeF?", "Zwykle obok kodu QR. Jeśli go nie widzisz, pobierz fakturę z Aplikacji Podatnika KSeF."),
        ("Co zrobić, gdy dane w PDF różnią się od XML?", "Wiążący jest plik w KSeF. Skontaktuj się ze sprzedawcą, zanim zlecisz przelew."),
    ],
    sources=[MF_QR, QR_DOC, MF_AP, MF_FA3],
)

C29 = dict(
    slug="faktura-ksef-xml-przyklad",
    title="Przykładowa faktura XML KSeF FA(3) – omówienie",
    desc="Omówienie przykładowej faktury XML KSeF w strukturze FA(3): najważniejsze pola, kwoty, rachunek i termin płatności oraz jak z nich zrobić przelew.",
    h1="Przykładowa faktura XML KSeF FA(3) – omówienie",
    intro="Jak czytać fakturę XML w strukturze FA(3)? Omawiamy najważniejsze pola: daty, kwoty, rachunek i termin, czyli dane potrzebne do przelewu.",
    lead_tool=("/przelew-z-faktury-xml-ksef/", "przelew z faktury XML"),
    date=("2026-11-23", "23 listopada 2026"),
    content="""
<h2 id="odpowiedz">Krótka odpowiedź</h2>
<p>Faktura w KSeF to plik XML zgodny ze schematem FA(3). Do przelewu potrzebujesz kilku pól: nazwy i NIP sprzedawcy, kwoty należności, rachunku i terminu płatności. Wklej plik do narzędzia <a href="/przelew-z-faktury-xml-ksef/">przelew z faktury XML</a>, a odczyta je w przeglądarce, bez wysyłania pliku na serwer.</p>
<h2 id="pola">Najważniejsze pola faktury FA(3)</h2>
<div class="table-wrap"><table>
<thead><tr><th scope="col">Pole</th><th scope="col">Co oznacza</th><th scope="col">Po co do przelewu</th></tr></thead>
<tbody>
<tr><td>P_1</td><td>data wystawienia, RRRR-MM-DD</td><td>wyszukiwanie faktury, kod QR</td></tr>
<tr><td>P_2</td><td>numer faktury nadany przez sprzedawcę</td><td>identyfikacja dokumentu</td></tr>
<tr><td>P_15</td><td>należność ogółem</td><td>kwota przelewu</td></tr>
<tr><td>P_18A</td><td>mechanizm podzielonej płatności (1 – tak, 2 – nie)</td><td>wybór przelewu MPP</td></tr>
<tr><td>NrRB</td><td>rachunek bankowy sprzedawcy</td><td>odbiorca przelewu</td></tr>
<tr><td>Termin</td><td>termin płatności</td><td>data realizacji</td></tr>
</tbody></table></div>
<p>Jeśli w fakturze występuje sekcja rozliczenia z polem DoZaplaty, to ona wskazuje kwotę faktycznie do zapłaty po potrąceniach, więc ma pierwszeństwo przed samą sumą brutto. Pełny wykaz pól znajdziesz w schemacie XSD opublikowanym przez MF.</p>
<h2 id="przyklad">Przykład: odczyt danych krok po kroku</h2>
<p>Załóżmy fakturę z datą 2026-12-15 (P_1), numerem sprzedawcy FV/12/2026 (P_2), należnością 1 230,00 zł (P_15), P_18A = 2 i rachunkiem sprzedawcy w polu NrRB. Do przelewu zwykłego wpisujesz kwotę 1 230,00 zł, rachunek z NrRB, a w tytule numer KSeF, który system nadał fakturze. Numer faktury sprzedawcy z P_2 można dopisać w dalszej części opisu, jeśli bank ma na to miejsce. Przy P_18A = 1 użyj <a href="/przelew-mpp-numer-ksef/">kreatora przelewu MPP</a>. Przykład jest ilustracyjny, a nie prawdziwą fakturą.</p>
<h2 id="uklad">Jak zbudowany jest plik</h2>
<ul>
<li>nagłówek z kodem formularza i datą wytworzenia,</li>
<li>Podmiot1 – sprzedawca, Podmiot2 – nabywca,</li>
<li>sekcja Fa z datami, kwotami i adnotacjami,</li>
<li>wiersze faktury (FaWiersz) z nazwą, ilością i cenami,</li>
<li>płatność z terminem i rachunkiem.</li>
</ul>
<p>Plik możesz otworzyć w przeglądarce lub edytorze tekstu, a jak to zrobić, opisujemy w artykule <a href="/blog/jak-otworzyc-plik-xml-ksef/">jak otworzyć plik XML z KSeF</a>.</p>
<h2 id="numer">Skąd w pliku numer KSeF</h2>
<p>Numeru KSeF nie ma w treści faktury w chwili jej tworzenia, bo nadaje go system po przyjęciu dokumentu. Odczytasz go w Aplikacji Podatnika lub w danych pobranych z KSeF. Przed użyciem w przelewie sprawdź go w <a href="/">walidatorze numeru KSeF</a>.</p>
<h2 id="kroki">Jak przygotować przelew z pliku XML</h2>
<ol class="steps">
<li>Pobierz plik faktury z KSeF.</li>
<li>Wklej go do narzędzia lub otwórz w edytorze.</li>
<li>Odczytaj sprzedawcę, kwotę, rachunek i termin.</li>
<li>Dodaj numer KSeF do tytułu przelewu.</li>
<li>Jeśli P_18A = 1, przygotuj przelew w trybie podzielonej płatności.</li>
</ol>
<h2 id="bledy">Częste pomyłki</h2>
<ul>
<li>użycie numeru faktury sprzedawcy zamiast numeru KSeF w tytule,</li>
<li>pominięcie sekcji rozliczenia i wpisanie sumy brutto zamiast kwoty do zapłaty,</li>
<li>pomylenie rachunku z innej faktury lub wiadomości e-mail,</li>
<li>założenie, że każda faktura ma wszystkie pola opcjonalne.</li>
</ul>
<h2 id="praktyka">Dobre nawyki</h2>
<p>Przy większej liczbie faktur ustal stały sposób pracy: pobierasz pliki, odczytujesz dane, zapisujesz numery KSeF w ewidencji i dopiero potem przygotowujesz przelewy. Przed zleceniem wypłaty sprawdź rachunek na białej liście podatników VAT w sposób wskazany przez MF. Nie podajemy tu terminów ani kwot sankcji.</p>
<p>Narzędzia w przeglądarce nie wysyłają faktur na serwer, ale pamiętaj o ostrożności z plikami od nieznanych nadawców. Plik XML pobieraj tylko z Aplikacji Podatnika lub z zaufanego programu fakturowego. Jeśli dane wyglądają dziwnie, na przykład kwota znacząco różni się od oczekiwanej, skontaktuj się ze sprzedawcą przed płatnością.</p>
<p>Warto też zapisać sobie, które pola faktur są dla Twojej firmy najczęściej puste lub nietypowe. Dostawcy usług mają różne zwyczaje: jedni podają rachunek w każdej fakturze, inni tylko raz w umowie. Jeśli rachunku w pliku brak, nie zgaduj go, tylko sprawdź w umowie lub zapytaj sprzedawcę. To prosty nawyk, który chroni przed przelewem na błędne konto.</p>
<h2 id="przyklad-2">Przykład: faktura z dwiema stawkami VAT</h2>
<p>Gdy faktura zawiera pozycje z różnymi stawkami, kwoty netto i VAT są sumowane osobno dla każdej stawki w polach z grupy P_13 i P_14, na przykład P_13_1 i P_14_1 dla stawki podstawowej oraz P_13_2 i P_14_2 dla stawki obniżonej. Mimo to kwota do zapłaty jest jedna: wynika z pola P_15 albo z rozliczenia. Załóżmy pozycje 1 000,00 zł netto z VAT 23% oraz 500,00 zł netto z VAT 8%. VAT wynosi 230,00 zł i 40,00 zł, więc suma brutto to 1 770,00 zł (1 500,00 + 270,00). Taką kwotę wpisujesz w przelewie, a nie sumę pojedynczej stawki. Przykład jest wymyślony.</p>
<h2 id="walidacja">Dlaczego warto znać schemat</h2>
<p>Schemat FA(3) opublikowany przez MF określa, jakie elementy są wymagane, a jakie opcjonalne, oraz jakie wartości są dozwolone. Dzięki temu dwa różne programy fakturowe tworzą pliki o tej samej strukturze, a narzędzie do odczytu może je obsłużyć bez znajomości konkretnego dostawcy. Jeśli plik nie przechodzi walidacji względem schematu, system go nie przyjmie, więc faktura nie otrzyma numeru KSeF.</p>
<h2 id="daty">Daty w pliku XML</h2>
<p>Daty w fakturze zapisuje się w formacie RRRR-MM-DD, na przykład 2026-12-15. Pole P_1 to data wystawienia, a data dostawy lub wykonania usługi może być podana osobno w polu P_6. Termin płatności znajdziesz w sekcji płatności. Przy zlecaniu przelewu liczy się właśnie ten termin, a nie data wystawienia, dlatego zawsze sprawdzaj oba pola i zapisz je w ewidencji płatności firmy.</p>
<h2 id="dane-nabywcy">Dane nabywcy i sprzedawcy</h2>
<p>W sekcjach podmiotów znajdziesz NIP, nazwę i adres. Przy płatności ważny jest NIP sprzedawcy, bo w przelewie MPP trafia on do komunikatu, a w kodzie QR jest jednym z elementów. Zawsze porównaj go z danymi umowy lub poprzednich faktur, aby wykluczyć próbę oszustwa na zmianę rachunku.</p>
<h2 id="zrodla-info">Źródła i zastrzeżenia</h2>
<p>Opis pól oparto na schemacie FA(3) i stronach MF (ksef.podatki.gov.pl). Przykład liczbowy jest wymyślony dla ilustracji. Tekst nie jest doradztwem podatkowym.</p>
<h2 id="podsumowanie">Podsumowanie</h2>
<p>W fakturze FA(3) szukaj pól P_15, P_18A, NrRB i terminu. Wklej plik do narzędzia <a href="/przelew-z-faktury-xml-ksef/">przelew z faktury XML</a>, dodaj numer KSeF do tytułu i sprawdź go w <a href="/">walidatorze</a>.</p>
""",
    faq=[
        ("Które pole faktury FA(3) zawiera kwotę należności?", "Należność ogółem jest w polu P_15. Jeśli jest sekcja rozliczenia z DoZaplaty, ona wskazuje kwotę do zapłaty."),
        ("Jak poznać, że faktura jest objęta podzieloną płatnością?", "Wskazuje to pole P_18A w adnotacjach: 1 oznacza mechanizm podzielonej płatności, 2 jego brak."),
        ("Czy w pliku XML przykładowej faktury widać numer KSeF?", "W chwili wystawienia nie. Numer nadaje system po przyjęciu faktury i widać go w aplikacji lub danych pobranych z KSeF."),
        ("Czy plik XML wysyłam na serwer narzędzia?", "Nie. Narzędzie odczytuje plik lokalnie w przeglądarce."),
    ],
    sources=[XSD, MF_FA3, MF_PODR2, MF_AP],
)

C30 = dict(
    slug="split-payment-kilka-faktur-ksef",
    title="Split payment za kilka faktur KSeF – jak opisać?",
    desc="Jak opisać przelew split payment za kilka faktur z KSeF: kiedy użyć identyfikatora zbiorczego, jak wpisać numery KSeF i na co uważać w banku.",
    h1="Split payment za kilka faktur KSeF – jak opisać przelew?",
    intro="Płacisz jednym przelewem MPP za kilka faktur z KSeF? Sprawdź, jak podać numery KSeF lub identyfikator zbiorczy i co ustalić z bankiem.",
    lead_tool=("/przelew-mpp-numer-ksef/", "kreator przelewu MPP z numerem KSeF"),
    date=("2026-11-23", "23 listopada 2026"),
    content="""
<h2 id="odpowiedz">Krótka odpowiedź</h2>
<p>Przy jednym przelewie za kilka faktur z KSeF w opisie podaje się identyfikator zbiorczy, a nie listę numerów, o ile płacisz za wiele faktur jednego sprzedawcy jedną kwotą. Identyfikator ma budowę zbliżoną do numeru KSeF i jest opisany przez MF. Opis pod bank przygotujesz w <a href="/przelew-mpp-numer-ksef/">kreatorze przelewu MPP</a>, a identyfikator zbiorczy sprawdzisz w <a href="/identyfikator-zbiorczy-ksef/">narzędziu do identyfikatora zbiorczego</a>.</p>
<h2 id="warianty">Trzy sytuacje przy płatności za wiele faktur</h2>
<div class="table-wrap"><table>
<thead><tr><th scope="col">Sytuacja</th><th scope="col">Co robisz</th><th scope="col">Uwaga</th></tr></thead>
<tbody>
<tr><td>jedna faktura</td><td>numer KSeF w tytule</td><td>zwykły przelew MPP lub standardowy</td></tr>
<tr><td>kilka faktur, osobne przelewy</td><td>każdy przelew z własnym numerem KSeF</td><td>najprostsze, ale więcej pracy</td></tr>
<tr><td>kilka faktur jednym przelewem</td><td>identyfikator zbiorczy</td><td>sprawdź sposób wpisania w swoim banku</td></tr>
</tbody></table></div>
<p>Obowiązek podawania numeru KSeF w przelewie wynika z art. 108g ustawy o VAT i dotyczy płatności za faktury z KSeF dokonywanych przez czynnych podatników VAT. Aktualne zasady sprawdzaj na ksef.podatki.gov.pl.</p>
<h2 id="mpp">Jak MPP łączy się z numerem KSeF</h2>
<p>W przelewie podzielonej płatności komunikat zawiera kwotę VAT, kwotę brutto, NIP odbiorcy oraz numer faktury. Banki różnią się sposobem, w jaki przyjmują numer KSeF w polu numeru faktury lub w opisie, a część z nich dopiero dostosowuje formularze. Dlatego zajrzyj do instrukcji swojego banku albo zapytaj doradcę. Sam kreator pomaga złożyć dane w jednym miejscu: <a href="/blog/numer-ksef-w-przelewie-mpp/">artykuł o numerze KSeF w split payment</a> opisuje szczegóły.</p>
<h2 id="przyklad">Przykład: trzy faktury od jednego dostawcy</h2>
<p>Firma ma trzy faktury od tego samego dostawcy: 1 230,00 zł, 2 460,00 zł i 615,00 zł brutto, wszystkie z VAT 23%. Sumy: brutto 4 305,00 zł, w tym VAT 805,00 zł (230 + 460 + 115 zł). Dla jednego przelewu zbiorczego kwota brutto to 4 305,00 zł, a kwota VAT 805,00 zł. Zamiast trzech numerów KSeF w opisie podaje się wtedy identyfikator zbiorczy, o ile bank i sytuacja na to pozwalają. Przykład jest liczbowo ilustracyjny, a nie prawdziwą płatnością.</p>
<h2 id="kroki">Jak przygotować płatność</h2>
<ol class="steps">
<li>Zbierz numery KSeF wszystkich faktur i sprawdź je w <a href="/sprawdz-wiele-numerow-ksef/">sprawdzaniu wielu numerów</a>.</li>
<li>Zsumuj kwoty brutto i VAT, upewniając się, że faktury są od jednego sprzedawcy.</li>
<li>Ustal, czy masz identyfikator zbiorczy lub czy płacisz osobno.</li>
<li>Wpisz dane w formularzu MPP w banku.</li>
<li>Zapisz numer przelewu przy fakturach w ewidencji.</li>
</ol>
<h2 id="zbiorczy">Identyfikator zbiorczy</h2>
<p>Identyfikator zbiorczy służy do wskazania w jednej płatności kilku faktur. Jego strukturę opisuje MF w materiałach o numerze KSeF i identyfikatorze zbiorczym. W <a href="/blog/identyfikator-zbiorczy-ksef-co-to-jest/">artykule o identyfikatorze zbiorczym</a> pokazujemy, jak go rozpoznać. Nie zgaduj jego zasad: korzystaj wyłącznie z opisu publikowanego przez MF.</p>
<h2 id="bledy">Częste pomyłki</h2>
<ul>
<li>wpisanie listy numerów KSeF w polu, które mieści tylko jeden,</li>
<li>łączenie w jednej płatności faktur od różnych sprzedawców,</li>
<li>pomylenie kwoty VAT z kwotą brutto w formularzu MPP,</li>
<li>brak sprawdzenia, jak bank przyjmuje numer KSeF.</li>
</ul>
<h2 id="praktyka">Dobre nawyki</h2>
<p>Jeśli co miesiąc płacisz kilku dostawcom, przygotuj tabelę: sprzedawca, numery KSeF, kwota brutto, kwota VAT, termin. Przed zleceniem przelewu zweryfikuj rachunek sprzedawcy na białej liście. Dla dużych wolumenów zapytaj bank, czy obsługuje import przelewów z numerami KSeF, co oszczędza ręcznego wpisywania. Plik z danymi możesz przygotować w <a href="/sprawdz-wiele-numerow-ksef/">narzędziu do wielu numerów</a>.</p>
<p>Gdy wątpisz, czy w Twojej sytuacji wolno połączyć faktury, wybierz bezpieczniejszą drogę: osobne przelewy, każdy z własnym numerem KSeF. Jest to wolniejsze, ale nie wymaga interpretowania zasad, których bank mógł jeszcze nie wdrożyć. Później możesz przejść na identyfikator zbiorczy, gdy potwierdzisz sposób jego obsługi z doradcą bankowym lub księgowym.</p>
<p>Pamiętaj też o terminach płatności. Łączenie faktur w jeden przelew oznacza, że płacisz wszystkie w dniu zbliżającym się do najwcześniejszego terminu, aby żadna nie była przeterminowana. Zapisuj w ewidencji, którą płatnością uregulowano które faktury, bo przy uzgadnianiu wyciągu ułatwi to dopasowanie wpłat.</p>
<h2 id="przyklad-2">Przykład: kontrola przed wysłaniem przelewu</h2>
<p>Księgowa przygotowuje płatność za dwie faktury tego samego dostawcy. Najpierw sprawdza oba numery KSeF w walidatorze, potem otwiera fakturę w aplikacji i porównuje rachunek z białą listą. Następnie zestawia kwoty: brutto 2 000,00 zł i 1 000,00 zł, w tym VAT 373,98 zł i 186,99 zł, co daje 3 000,00 zł brutto i 560,97 zł VAT. Dopiero wtedy wpisuje wartości w formularzu MPP. Taka kontrola trwa kilka minut, a chroni przed błędnym przelewem, którego korekta bywa kłopotliwa. Liczby są ilustracyjne.</p>
<h2 id="rozliczenie">Rozliczenie po płatności</h2>
<p>Po wysłaniu przelewu zapisz w ewidencji datę, kwotę i numery KSeF opłaconych faktur. Przy uzgadnianiu wyciągu łatwo wtedy znaleźć, którą płatnością zamknięto które dokumenty. Pomaga w tym <a href="/blog/uzgadnianie-wyciagu-bankowego-numery-ksef/">uzgadnianie wyciągu bankowego z numerami KSeF</a>. Jeśli faktur jest wiele, trzymaj prosty arkusz z kolumnami: sprzedawca, numer KSeF, brutto, VAT, termin, data płatności.</p>
<h2 id="czesc">Płatność częściowa i korekty</h2>
<p>Gdy płacisz tylko część należności lub faktura została skorygowana, najpierw ustal, jaka kwota jest faktycznie do zapłaty. Przy korektach sprawdź numer KSeF faktury korygującej, który opisujemy w artykule <a href="/blog/numer-ksef-faktury-korygujacej/">numer KSeF faktury korygującej</a>. W razie wątpliwości co do sposobu opisania przelewu zapytaj księgowego lub bank.</p>
<h2 id="zrodla-info">Źródła i zastrzeżenia</h2>
<p>Informacje o numerze KSeF i identyfikatorze zbiorczym pochodzą ze stron MF (ksef.podatki.gov.pl). Nie podajemy kar ani terminów sankcji, a sposób obsługi w banku różni się. Tekst nie jest doradztwem podatkowym.</p>
<h2 id="podsumowanie">Podsumowanie</h2>
<p>Przy płatności za kilka faktur jedną z dróg jest identyfikator zbiorczy, drugą osobne przelewy. Przygotuj dane w <a href="/przelew-mpp-numer-ksef/">kreatorze MPP</a>, sprawdź numery w <a href="/">walidatorze</a> i potwierdź obsługę w swoim banku.</p>
""",
    faq=[
        ("Czy za kilka faktur z KSeF mogę zapłacić jednym przelewem?", "Tak, w określonych sytuacjach przy użyciu identyfikatora zbiorczego opisanego przez MF. Sprawdź też, jak obsługuje to Twój bank."),
        ("Czy w przelewie MPP trzeba podać numer KSeF?", "Przy płatności za fakturę z KSeF przez czynnego podatnika VAT numer KSeF ma być podany zgodnie z art. 108g ustawy o VAT. Sposób wpisania zależy od banku."),
        ("Czy mogę połączyć faktury od różnych sprzedawców?", "Nie, przelew trafia do jednego odbiorcy, więc faktury muszą być od tego samego sprzedawcy."),
    ],
    sources=[MF_NUM, MF_TERM, IZ_PDF2, MF_AP],
)

CAL_POSTS = CAL_POSTS + [C28, C29, C30]

C31 = dict(
    slug="blad-przepisania-numeru-ksef",
    title="Błąd przy przepisaniu numeru KSeF – jak go wykryć",
    desc="Pomyłka w jednym znaku numeru KSeF psuje opis przelewu. Zobacz, jak suma kontrolna CRC-8 wykrywa literówki i jak kopiować numer bezpiecznie.",
    h1="Błąd przy przepisaniu numeru KSeF – jak go wykryć?",
    intro="Jedna pomylona litera w numerze KSeF i opis przelewu jest błędny. Sprawdź, jak wykryć literówkę i jak kopiować numer bez pomyłek.",
    lead_tool=("/", "walidator numeru KSeF"),
    date=("2026-11-24", "24 listopada 2026"),
    content="""
<h2 id="odpowiedz">Krótka odpowiedź</h2>
<p>Najpewniej jest kopiować numer KSeF jako tekst z aplikacji lub pliku, a nie przepisywać go ręcznie. Jeśli musisz go wpisać, sprawdź go od razu w <a href="/">walidatorze numeru KSeF</a>. Suma kontrolna CRC-8, opisana przez MF, wychwytuje większość pojedynczych pomyłek, np. literę O zamiast zera.</p>
<h2 id="budowa">Co sprawdza walidator</h2>
<p>Numer KSeF ma 35 znaków: NIP sprzedawcy, datę przyjęcia faktury, 12-znakową część techniczną zapisaną szesnastkowo wielkimi literami oraz dwuznakową sumę kontrolną CRC-8. Według dokumentacji CIRFMF suma jest liczona z pierwszych 32 znaków (wielomian 0x07, wartość początkowa 0x00). Więcej o budowie znajdziesz w artykule <a href="/blog/z-czego-sklada-sie-numer-ksef/">z czego składa się numer KSeF</a>.</p>
<h2 id="przyklad">Przykład: jedna zmieniona litera</h2>
<p>Do przykładu używamy numeru z dokumentacji MF/CIRFMF: 5265877635-20250826-0100001AF629-AF. Suma kontrolna dla części z danymi wynosi AF, więc numer jest poprawny. Policzyliśmy też sumy dla dwóch typowych pomyłek:</p>
<div class="table-wrap"><table>
<thead><tr><th scope="col">Wpisany ciąg (część techniczna)</th><th scope="col">Co zmieniono</th><th scope="col">Suma wyliczona</th><th scope="col">Wynik</th></tr></thead>
<tbody>
<tr><td>0100001AF629</td><td>nic</td><td>AF</td><td>poprawny</td></tr>
<tr><td>0100001AF62O</td><td>cyfra 9 zastąpiona literą O</td><td>EA</td><td>błąd sumy</td></tr>
<tr><td>0100001af629</td><td>małe litery zamiast wielkich</td><td>05</td><td>błąd sumy</td></tr>
</tbody></table></div>
<p>Zwróć uwagę, że w drugim wierszu zmiana jednego znaku zmienia wynik sumy z AF na EA. Dlatego rozbieżność od razu widać w narzędziu. Przykład jest obliczony przez nas na podstawie opisu algorytmu MF; sam numer pochodzi z dokumentacji.</p>
<h2 id="mylone">Znaki, które najczęściej się mylą</h2>
<ul>
<li>zero (0) i litera O,</li>
<li>jedynka (1) i litera I lub l,</li>
<li>cyfra 8 i litera B,</li>
<li>małe litery zamiast wielkich w części szesnastkowej,</li>
<li>spacja doklejona na końcu po skopiowaniu,</li>
<li>pominięty myślnik lub dodatkowy znak na początku.</li>
</ul>
<p>W części technicznej i w sumie kontrolnej mogą występować tylko znaki 0–9 oraz A–F. Litery spoza tego zakresu, np. O czy I, są więc od razu podejrzane.</p>
<h2 id="kroki">Jak ograniczyć ryzyko pomyłki</h2>
<ol class="steps">
<li>Kopiuj numer z Aplikacji Podatnika lub z pliku, zamiast przepisywać go z wydruku.</li>
<li>Wklej go w <a href="/">walidatorze</a> i sprawdź, czy ma 35 znaków.</li>
<li>Przy wielu fakturach użyj <a href="/sprawdz-wiele-numerow-ksef/">sprawdzania wielu numerów</a> i wczytaj listę jednym ruchem.</li>
<li>Do przelewu wklej numer bez dodatkowych spacji.</li>
<li>Porównaj kwotę, NIP i rachunek z fakturą oraz białą listą.</li>
</ol>
<h2 id="kopiowanie">Kopiowanie z PDF i z wydruku</h2>
<p>Wizualizacja faktury w PDF zawiera numer KSeF jako tekst, ale część czytników przy kopiowaniu dokleja spacje, łamie wiersz lub zamienia myślniki na inne znaki. Po wklejeniu zawsze przejrzyj ciąg. Wydruk albo zdjęcie telefonem są najbardziej narażone na pomyłkę, bo litery i cyfry bywają podobne. Jak znaleźć numer w dokumentach, opisujemy w artykule <a href="/blog/gdzie-znalezc-numer-ksef-faktury/">gdzie znaleźć numer KSeF faktury</a>.</p>
<h2 id="przyklad2">Przykład: lista z kilku faktur</h2>
<p>Księgowa kopiuje do arkusza numery z dziesięciu faktur. Po wklejeniu zapisuje je w jednej kolumnie i wczytuje do narzędzia do wielu numerów. Dwa numery zostają oznaczone jako błędne: w jednym brakuje znaku, w drugim na końcu jest spacja. Poprawia je, kopiując numery ponownie z aplikacji, i dopiero wtedy przygotowuje przelewy. Dzięki temu bank nie dostaje błędnych opisów. To przykład ilustracyjny, bez prawdziwych danych.</p>
<h2 id="co-nie">Czego walidator nie sprawdzi</h2>
<p>Poprawna suma kontrolna oznacza, że numer ma prawidłową budowę. Nie oznacza jednak, że faktura o takim numerze istnieje w KSeF ani że należy do Twojego kontrahenta. Walidator działa w przeglądarce i nie łączy się z systemem MF, dlatego istnienie faktury potwierdzisz w Aplikacji Podatnika. Podobnie nie sprawdzi on, czy kwota w przelewie odpowiada fakturze.</p>
<p>Warto więc łączyć dwie kontrole: formalną, czyli walidator, i merytoryczną, czyli porównanie danych z dokumentem. W praktyce zajmuje to chwilę, a ogranicza liczbę przelewów, które trzeba wyjaśniać. Jeśli opis przelewu zawiera błąd, skontaktuj się z bankiem i sprzedawcą; zasady postępowania zależą od banku. Szerzej o tym piszemy w artykule <a href="/blog/numer-ksef-blad-w-przelewie/">numer KSeF – błąd w przelewie</a>.</p>
<h2 id="firma">Prosta procedura w firmie</h2>
<p>Jeśli płatności przygotowuje kilka osób, ustalcie jedną zasadę: numer KSeF trafia do przelewu wyłącznie przez kopiowanie i wklejanie, a ręczne wpisywanie jest wyjątkiem. Każdy wyjątek kończy się sprawdzeniem w walidatorze. Przydaje się też prosty arkusz z kolumnami: numer KSeF, wynik sprawdzenia, kwota brutto, kwota VAT, rachunek, data przelewu. Dzięki niemu druga osoba może szybko zweryfikować przygotowaną paczkę przed zatwierdzeniem w banku.</p>
<p>Przy dużej liczbie faktur dobrze jest zapisywać wynik sprawdzenia razem z numerem. Gdy po tygodniu ktoś zapyta, dlaczego przelew został wstrzymany, wystarczy otworzyć arkusz i zobaczyć, który numer miał błąd. Plik CSV z listą można wczytać do <a href="/sprawdz-wiele-numerow-ksef/">narzędzia do wielu numerów</a> ponownie po poprawkach.</p>
<h2 id="rozpoznanie">Jak rozpoznać typ błędu po komunikacie</h2>
<p>Komunikat o złej długości oznacza zwykle, że brakuje znaku albo doklejono spację. Komunikat o niedozwolonych znakach wskazuje na literę spoza zakresu A–F w części szesnastkowej. Komunikat o błędnej sumie kontrolnej mówi, że długość i znaki są w porządku, ale któryś znak został zmieniony. W takim przypadku porównaj numer znak po znaku z oryginałem w aplikacji.</p>
<p>Pamiętaj, że sprawdzenie formalne to dopiero pierwszy krok. Nawet gdy walidator potwierdza budowę numeru, przed zleceniem przelewu otwórz fakturę w aplikacji i upewnij się, że numer, kwota oraz rachunek sprzedawcy zgadzają się z dokumentem. Dwie krótkie kontrole zajmują mniej czasu niż wyjaśnianie błędnej płatności z bankiem i kontrahentem.</p>
<h2 id="zrodla-info">Źródła i zastrzeżenia</h2>
<p>Opis struktury i algorytmu pochodzi z dokumentacji numeru KSeF publikowanej przez MF i CIRFMF. Tekst nie jest doradztwem podatkowym, a o kwestiach spornych decyduje obowiązujące prawo i wyjaśnienia MF.</p>
<h2 id="podsumowanie">Podsumowanie</h2>
<p>Kopiuj zamiast przepisywać, a po wklejeniu sprawdź numer w <a href="/">walidatorze numeru KSeF</a>. Przy większej liczbie faktur skorzystaj z <a href="/sprawdz-wiele-numerow-ksef/">sprawdzania wielu numerów</a>. Gotowy opis przelewu złożysz w narzędziu na stronie głównej.</p>
""",
    faq=[
        ("Dlaczego numer KSeF wklejony z PDF jest uznany za błędny?", "Najczęściej czytnik PDF dokleił spację, złamał wiersz albo zmienił myślnik. Usuń dodatkowe znaki i sprawdź numer ponownie."),
        ("Czy literę O można pomylić z zerem w numerze KSeF?", "Tak, to częsta pomyłka przy przepisywaniu. W części szesnastkowej dozwolone są tylko 0–9 i A–F, więc litera O jest błędem."),
        ("Czy poprawna suma kontrolna oznacza, że faktura istnieje?", "Nie. Potwierdza tylko budowę numeru. Istnienie faktury sprawdzisz w Aplikacji Podatnika KSeF."),
        ("Jak sprawdzić kilkadziesiąt numerów KSeF naraz?", "Wklej listę do narzędzia do sprawdzania wielu numerów albo wczytaj plik CSV. Narzędzie oznaczy numery z błędami."),
    ],
    sources=[DOC_NUM, MF_NUM, MF_AP],
)

CAL_POSTS = CAL_POSTS + [C31]

C32 = dict(
    slug="data-w-numerze-ksef-co-oznacza",
    title="Data w numerze KSeF – co oznacza i skąd się bierze",
    desc="Drugi człon numeru KSeF to data przyjęcia faktury do dalszego przetwarzania, a nie data wystawienia. Zobacz przykład, tabelę i odpowiedzi na pytania.",
    h1="Data w numerze KSeF – co oznacza i skąd się bierze?",
    intro="W środku numeru KSeF stoi ośmiocyfrowa data. Sprawdź, co dokładnie oznacza, czym różni się od daty wystawienia faktury i jak ją odczytać.",
    lead_tool=("/", "walidator numeru KSeF"),
    date=("2026-11-25", "25 listopada 2026"),
    content="""
<h2 id="odpowiedz">Krótka odpowiedź</h2>
<p>Data w numerze KSeF zapisana jako RRRRMMDD to data przyjęcia faktury do dalszego przetwarzania w systemie. Tak opisuje ją dokumentacja MF i CIRFMF. Nie musi być identyczna z datą wystawienia faktury, którą sprzedawca wpisuje w polu P_1. Numer z datą możesz sprawdzić w <a href="/">walidatorze numeru KSeF</a>.</p>
<h2 id="budowa">Gdzie jest data w numerze</h2>
<p>Numer KSeF ma 35 znaków i składa się z czterech części oddzielonych myślnikami. Data jest drugą z nich, tuż po NIP-ie sprzedawcy. Poniżej rozbiliśmy przykład z dokumentacji CIRFMF.</p>
<div class="table-wrap"><table>
<thead><tr><th scope="col">Część</th><th scope="col">Przykład</th><th scope="col">Znaczenie</th></tr></thead>
<tbody>
<tr><td>NIP sprzedawcy</td><td>5265877635</td><td>10 cyfr</td></tr>
<tr><td>Data przyjęcia</td><td>20250826</td><td>26 sierpnia 2025 (RRRRMMDD)</td></tr>
<tr><td>Część techniczna</td><td>0100001AF629</td><td>12 znaków szesnastkowych, wielkie litery</td></tr>
<tr><td>Suma kontrolna</td><td>AF</td><td>CRC-8 z pierwszych 32 znaków</td></tr>
</tbody></table></div>
<p>Całość to 5265877635-20250826-0100001AF629-AF. Ogólną budowę omawiamy w artykule <a href="/blog/z-czego-sklada-sie-numer-ksef/">z czego składa się numer KSeF</a>.</p>
<h2 id="przyjecie">Data przyjęcia a data wystawienia</h2>
<p>Data wystawienia faktury to informacja zapisana w pliku XML przez sprzedawcę, w polu P_1. Data w numerze KSeF powstaje dopiero wtedy, gdy system przyjmie fakturę i nada jej numer. Dlatego obie daty mogą się różnić. Poniżej prosty przykład, który wymyśliliśmy wyłącznie dla ilustracji.</p>
<div class="table-wrap"><table>
<thead><tr><th scope="col">Element</th><th scope="col">Przykładowa wartość</th><th scope="col">Skąd pochodzi</th></tr></thead>
<tbody>
<tr><td>Data wystawienia (P_1)</td><td>2026-03-10</td><td>plik faktury XML</td></tr>
<tr><td>Data w numerze KSeF</td><td>20260310 lub późniejsza</td><td>przyjęcie faktury przez system</td></tr>
</tbody></table></div>
<p>Jeśli faktura została przyjęta tego samego dnia, obie daty będą takie same. Jeśli system przyjął ją później, w numerze zobaczysz późniejszą datę. Nie traktuj więc daty z numeru jako daty sprzedaży ani terminu płatności.</p>
<h2 id="odczyt">Jak odczytać datę z numeru krok po kroku</h2>
<ol class="steps">
<li>Skopiuj cały numer i sprawdź, czy ma 35 znaków.</li>
<li>Odetnij pierwsze 11 znaków, czyli NIP i myślnik.</li>
<li>Weź kolejne osiem cyfr, to jest RRRRMMDD.</li>
<li>Pierwsze cztery cyfry to rok, następne dwie miesiąc, ostatnie dwie dzień.</li>
<li>Porównaj wynik z datą przyjęcia widoczną przy fakturze w aplikacji.</li>
</ol>
<p>Dla przykładu 20250826 odczytujemy rok 2025, miesiąc 08 i dzień 26. Walidator robi to automatycznie i dodatkowo sprawdza, czy taka data w ogóle istnieje w kalendarzu.</p>
<h2 id="blad">Typowe błędy w części z datą</h2>
<ul>
<li>cyfry zamienione miejscami, np. 20252608 zamiast 20250826,</li>
<li>data zapisana ze znakami rozdzielającymi, np. 2025-08-26 albo 26-08-2025,</li>
<li>brakująca cyfra, przez co numer ma 34 znaki,</li>
<li>miesiąc większy niż 12 albo dzień niemożliwy w danym miesiącu.</li>
</ul>
<p>W numerze KSeF data jest zapisana bez znaków rozdzielających. Format z myślnikami dotyczy innego miejsca: w linku z kodu QR data wystawienia jest zapisana jako DD-MM-RRRR. Szczegóły opisaliśmy w artykule <a href="/blog/kod-qr-ksef-co-zawiera/">co zawiera kod QR KSeF</a>.</p>
<h2 id="po-co">Po co w numerze jest data</h2>
<p>Numer KSeF ma jednoznacznie identyfikować fakturę. Według dokumentacji składa się z NIP-u sprzedawcy, daty przyjęcia i części technicznej, a całość zamyka suma kontrolna. Dzięki takiej budowie już na pierwszy rzut oka widać, kto wystawił fakturę i kiedy trafiła do systemu. W praktyce pomaga to przy porządkowaniu list numerów, np. gdy sortujesz je w arkuszu, bo ten sam NIP z rosnącą datą ułoży się chronologicznie.</p>
<p>Pamiętaj jednak, że sama data nie wystarczy do identyfikacji. Unikalność zapewnia dopiero część techniczna, więc w przelewie zawsze podawaj pełny numer, a nie jego fragment. Zasady wpisywania numeru w tytule przelewu znajdziesz w artykule <a href="/blog/jak-wpisac-numer-ksef-w-tytule-przelewu/">jak wpisać numer KSeF w tytule przelewu</a>.</p>
<h2 id="arkusz">Przykład: porządkowanie listy w arkuszu</h2>
<p>Księgowa ma w arkuszu 40 numerów KSeF od różnych dostawców. Chce zobaczyć, które faktury zostały przyjęte w danym miesiącu. Dzieli numer na części: znaki od 12. do 19. to data przyjęcia. Następnie filtruje wiersze, w których te osiem cyfr zaczyna się od 202603. Pozostałe numery zostawia na później. Przed przelewami wczytuje całą listę do <a href="/sprawdz-wiele-numerow-ksef/">narzędzia do sprawdzania wielu numerów</a>, aby wychwycić literówki. To tylko przykład organizacji pracy, a nie wymóg prawny.</p>
<p>Taki podział przydaje się też przy uzgadnianiu płatności z wyciągiem bankowym, bo opis przelewu zawiera pełny numer, a data pozwala szybko znaleźć właściwy miesiąc. Więcej o tym piszemy w artykule o <a href="/blog/uzgadnianie-wyciagu-bankowego-numery-ksef/">uzgadnianiu wyciągu bankowego z numerami KSeF</a>.</p>
<h2 id="zastrzezenie">Czego nie wynika z daty w numerze</h2>
<p>Data przyjęcia nie jest ani terminem płatności, ani datą powstania obowiązku podatkowego. Nie rozstrzyga też, w którym okresie rozliczeniowym ujmiesz fakturę. Te kwestie zależą od przepisów i od konkretnej transakcji, więc w razie wątpliwości sprawdź wyjaśnienia na stronach MF albo zapytaj księgowego. Nasz walidator sprawdza wyłącznie budowę numeru, w tym poprawność zapisu daty, i nie łączy się z systemem KSeF.</p>
<h2 id="zrodla-info">Źródła i stan prawny</h2>
<p>Opis budowy numeru pochodzi z dokumentacji numeru KSeF publikowanej przez CIRFMF oraz ze stron MF o KSeF. Treść ma charakter informacyjny i nie stanowi doradztwa podatkowego.</p>
<h2 id="podsumowanie">Podsumowanie</h2>
<p>Data w numerze KSeF to data przyjęcia faktury do dalszego przetwarzania, zapisana jako RRRRMMDD. Odczytasz ją z drugiej części numeru. Gdy chcesz sprawdzić cały numer, użyj <a href="/">walidatora numeru KSeF</a>, a przy większej liczbie faktur skorzystaj ze <a href="/sprawdz-wiele-numerow-ksef/">sprawdzania wielu numerów</a>.</p>
""",
    faq=[
        ("Czy data w numerze KSeF to data wystawienia faktury?", "Nie. Według dokumentacji to data przyjęcia faktury do dalszego przetwarzania. Data wystawienia jest zapisana w polu P_1 pliku XML."),
        ("W jakim formacie jest data w numerze KSeF?", "Jako RRRRMMDD, czyli osiem cyfr bez myślników, np. 20250826 oznacza 26 sierpnia 2025."),
        ("Czy walidator sprawdza, czy data w numerze istnieje?", "Tak, narzędzie sprawdza zapis daty razem z długością, znakami i sumą kontrolną CRC-8."),
        ("Czy data w numerze KSeF wyznacza termin płatności?", "Nie. Termin płatności wynika z umowy lub faktury, a data z numeru jest tylko elementem identyfikatora."),
    ],
    sources=[DOC_NUM, MF_NUM, MF_AP],
)

CAL_POSTS = CAL_POSTS + [C32]

C33 = dict(
    slug="suma-kontrolna-crc8-numer-ksef",
    title="Suma kontrolna CRC-8 w numerze KSeF – jak działa",
    desc="Ostatnie dwa znaki numeru KSeF to suma kontrolna CRC-8. Zobacz parametry algorytmu, przykład z obliczeniem i to, co wychwytuje literówki w numerze.",
    h1="Suma kontrolna CRC-8 w numerze KSeF – jak działa?",
    intro="Dwa ostatnie znaki numeru KSeF to suma kontrolna. Sprawdź, jak się ją liczy, co wykrywa i czego nie potwierdza.",
    lead_tool=("/", "walidator numeru KSeF"),
    date=("2026-11-26", "26 listopada 2026"),
    content="""
<h2 id="odpowiedz">Krótka odpowiedź</h2>
<p>Suma kontrolna to dwa ostatnie znaki numeru KSeF, zapisane szesnastkowo wielkimi literami. Według dokumentacji CIRFMF liczy się ją algorytmem CRC-8 z pierwszych 32 znaków numeru, z wielomianem 0x07 i wartością początkową 0x00. Gotowy numer sprawdzisz w <a href="/">walidatorze numeru KSeF</a>.</p>
<h2 id="parametry">Parametry algorytmu</h2>
<p>Dokumentacja opisuje walidację w czterech krokach: sprawdzenie długości 35 znaków, rozdzielenie części danych (32 znaki) od sumy (2 znaki), obliczenie CRC-8 z części danych i porównanie wyniku z wartością w numerze.</p>
<div class="table-wrap"><table>
<thead><tr><th scope="col">Parametr</th><th scope="col">Wartość</th></tr></thead>
<tbody>
<tr><td>Algorytm</td><td>CRC-8</td></tr>
<tr><td>Wielomian</td><td>0x07</td></tr>
<tr><td>Wartość początkowa</td><td>0x00</td></tr>
<tr><td>Dane wejściowe</td><td>pierwsze 32 znaki numeru, razem z myślnikami</td></tr>
<tr><td>Wynik</td><td>2 znaki szesnastkowe, wielkie litery</td></tr>
</tbody></table></div>
<p>Przykładowo, jeśli obliczona suma wynosi 0x46, do numeru trafia ciąg 46. Całą budowę numeru opisujemy w artykule <a href="/blog/z-czego-sklada-sie-numer-ksef/">z czego składa się numer KSeF</a>.</p>
<h2 id="przyklad">Przykład z dokumentacji</h2>
<p>Weźmy numer 5265877635-20250826-0100001AF629-AF. Pierwsze 32 znaki to 5265877635-20250826-0100001AF629, a więc NIP, data i część techniczna wraz z dwoma myślnikami. CRC-8 z tego ciągu daje wartość AF, czyli dokładnie to, co stoi na końcu numeru. Numer przechodzi więc kontrolę sumy.</p>
<p>Zmieńmy teraz jeden znak i policzmy sumę ponownie. Wyniki obliczyliśmy tym samym algorytmem.</p>
<div class="table-wrap"><table>
<thead><tr><th scope="col">Zmiana w numerze</th><th scope="col">Obliczona suma</th><th scope="col">Suma w numerze</th><th scope="col">Wynik</th></tr></thead>
<tbody>
<tr><td>bez zmian</td><td>AF</td><td>AF</td><td>zgodna</td></tr>
<tr><td>ostatni znak części technicznej 9 zamiast 8</td><td>A8</td><td>AF</td><td>niezgodna</td></tr>
<tr><td>część techniczna kończy się na 2A zamiast 29</td><td>C0</td><td>AF</td><td>niezgodna</td></tr>
<tr><td>data 20250286 zamiast 20250826</td><td>65</td><td>AF</td><td>niezgodna</td></tr>
</tbody></table></div>
<p>Pierwszy wiersz tej tabeli to pierwotny numer, a w pozostałych zmieniono po jednym znaku (w drugim wierszu zmiana jest tylko w sumie). Każda taka literówka daje inną sumę, więc walidator ją zgłosi. Przy zamianie cyfr w dacie widać, że sama poprawność kalendarzowa nie wystarcza, bo suma też się nie zgadza.</p>
<h2 id="co-wykrywa">Co suma kontrolna wykrywa</h2>
<ul>
<li>przepisanie jednego znaku w części, z której liczona jest suma,</li>
<li>zamianę sąsiednich cyfr, np. w dacie,</li>
<li>pominięcie albo dodanie znaku, które i tak zmienia długość numeru,</li>
<li>pomyłkę w samej sumie, na przykład AE zamiast AF.</li>
</ul>
<p>Dwa znaki szesnastkowe dają 256 możliwych wartości, więc zdarzy się, że inny ciąg danych ma tę samą sumę. Dlatego suma jest zabezpieczeniem przed przypadkowymi błędami, a nie gwarancją. Praktyczne wskazówki znajdziesz w artykule o <a href="/blog/blad-przepisania-numeru-ksef/">błędzie przy przepisaniu numeru KSeF</a>.</p>
<h2 id="czego-nie">Czego suma nie potwierdza</h2>
<p>Poprawna suma mówi tylko tyle, że numer jest wewnętrznie spójny. Nie oznacza, że faktura istnieje w systemie, że należy do wskazanego sprzedawcy ani że została opłacona. Nasze narzędzie działa lokalnie w przeglądarce i nie łączy się z KSeF. Istnienie faktury sprawdzisz w Aplikacji Podatnika albo w swoim systemie księgowym.</p>
<h2 id="krok">Jak sprawdzić sumę krok po kroku</h2>
<ol class="steps">
<li>Skopiuj numer z faktury lub z aplikacji, zamiast przepisywać go ręcznie.</li>
<li>Wklej go w <a href="/">walidatorze numeru KSeF</a>.</li>
<li>Sprawdź komunikat o długości, znakach, dacie i sumie CRC-8.</li>
<li>Przy niezgodności porównaj numer znak po znaku z oryginałem, zwracając uwagę na 0 i O oraz 8 i B.</li>
<li>Dopiero poprawny numer wpisz w tytule przelewu.</li>
</ol>
<h2 id="lista">Przykład: lista numerów przed przelewami</h2>
<p>Dział finansów ma przygotować 25 przelewów, a numery KSeF dostał w arkuszu. Zamiast sprawdzać je pojedynczo, wczytuje całą listę do <a href="/sprawdz-wiele-numerow-ksef/">narzędzia do sprawdzania wielu numerów</a>. Wiersze z niezgodną sumą wracają do poprawy, a reszta idzie do banku. To tylko przykład organizacji pracy, nie wymóg prawny. Zasady wpisywania numeru w przelewie opisaliśmy w artykule <a href="/blog/jak-wpisac-numer-ksef-w-tytule-przelewu/">jak wpisać numer KSeF w tytule przelewu</a>.</p>
<h2 id="hex">Dlaczego suma jest zapisana szesnastkowo</h2>
<p>CRC-8 daje wynik od 0 do 255. W zapisie szesnastkowym mieści się on zawsze w dwóch znakach, od 00 do FF, dlatego numer ma stałą długość 35 znaków. Dokumentacja podaje, że wolno używać tylko cyfr 0–9 i liter A–F, a litery muszą być wielkie. Jeśli więc w sumie zobaczysz literę G, małą literę albo znak spoza tego zestawu, numer jest błędny jeszcze przed obliczeniem CRC.</p>
<p>W praktyce błędy zdarzają się najczęściej przy ręcznym przepisywaniu: litera O zamiast zera, litera B zamiast ósemki albo pominięty znak w części technicznej. Walidator zgłasza je osobnymi komunikatami, a ostatnim krokiem jest właśnie porównanie sumy. Jeśli kopiujesz numer z aplikacji, ryzyko takiej pomyłki jest dużo mniejsze, o czym piszemy w artykule o <a href="/blog/gdzie-znalezc-numer-ksef-faktury/">tym, gdzie znaleźć numer KSeF faktury</a>.</p>
<h2 id="zrodla-info">Źródła i stan prawny</h2>
<p>Parametry algorytmu i opis walidacji pochodzą z dokumentacji CIRFMF dla KSeF 2.0 oraz ze stron MF o numerze KSeF. Treść ma charakter informacyjny i nie stanowi doradztwa podatkowego.</p>
<h2 id="podsumowanie">Podsumowanie</h2>
<p>Suma kontrolna to CRC-8 z pierwszych 32 znaków numeru, zapisane jako dwa znaki szesnastkowe. Wychwytuje literówki, ale nie potwierdza istnienia faktury. Wklej numer w <a href="/">walidatorze numeru KSeF</a>, a przy dłuższej liście użyj <a href="/sprawdz-wiele-numerow-ksef/">sprawdzania wielu numerów</a>.</p>
""",
    faq=[
        ("Jak obliczyć sumę kontrolną numeru KSeF?", "Liczy się CRC-8 (wielomian 0x07, wartość początkowa 0x00) z pierwszych 32 znaków numeru i zapisuje wynik jako dwa znaki szesnastkowe."),
        ("Z jakich znaków liczona jest suma CRC-8?", "Z pierwszych 32 znaków numeru, czyli NIP-u, daty i części technicznej razem z dwoma myślnikami. Ostatnie dwa znaki to sama suma."),
        ("Czy mogę sam wyliczyć numer KSeF, znając sumę?", "Nie. Numer nadaje system, a suma kontrolna tylko sprawdza spójność zapisu."),
        ("Czy poprawna suma CRC-8 gwarantuje, że numer jest prawdziwy?", "Nie. Potwierdza tylko spójność zapisu, a przy 256 możliwych wartościach sumy inny ciąg znaków może mieć taką samą wartość."),
        ("Czy małe litery w sumie kontrolnej są poprawne?", "Według dokumentacji suma zapisywana jest wielkimi literami szesnastkowymi, czyli 0–9 i A–F."),
    ],
    sources=[DOC_NUM, MF_NUM, MF_AP],
)

CAL_POSTS = CAL_POSTS + [C33]

C34 = dict(
    slug="nip-w-numerze-ksef-jak-sprawdzic",
    title="NIP w numerze KSeF – jak sprawdzić jego poprawność",
    desc="Pierwsze 10 cyfr numeru KSeF to NIP sprzedawcy. Zobacz, jak sprawdzić jego cyfrę kontrolną wagami 6-5-7-2-3-4-5-6-7, na przykładach z obliczeniem.",
    h1="NIP w numerze KSeF – jak sprawdzić jego poprawność?",
    intro="Numer KSeF zaczyna się od 10 cyfr NIP sprzedawcy. Sprawdź, jak policzyć jego cyfrę kontrolną i co z tego wynika.",
    lead_tool=("/", "walidator numeru KSeF"),
    date=("2026-11-27", "27 listopada 2026"),
    content="""
<h2 id="odpowiedz">Krótka odpowiedź</h2>
<p>Pierwsze 10 znaków numeru KSeF to NIP sprzedawcy. Jego ostatnia cyfra jest cyfrą kontrolną: mnoży się pierwszych dziewięć cyfr przez wagi 6, 5, 7, 2, 3, 4, 5, 6, 7, sumuje wyniki i dzieli sumę przez 11. Reszta musi być równa dziesiątej cyfrze. Wszystko sprawdzisz automatycznie w <a href="/">walidatorze numeru KSeF</a>.</p>
<h2 id="gdzie">Gdzie w numerze jest NIP</h2>
<p>Według dokumentacji CIRFMF numer KSeF ma 35 znaków: NIP (10 cyfr), data (8 cyfr), część techniczna (12 znaków) i suma kontrolna (2 znaki), rozdzielone myślnikami. W numerze 5265877635-20250826-0100001AF629-AF NIP to 5265877635. Szerzej o budowie piszemy w artykule <a href="/blog/czy-numer-ksef-to-nip/">czy numer KSeF to NIP</a>.</p>
<h2 id="algorytm">Algorytm cyfry kontrolnej NIP</h2>
<ol class="steps">
<li>Weź pierwszych dziewięć cyfr NIP.</li>
<li>Pomnóż je kolejno przez wagi 6, 5, 7, 2, 3, 4, 5, 6, 7.</li>
<li>Zsumuj iloczyny.</li>
<li>Oblicz resztę z dzielenia sumy przez 11.</li>
<li>Reszta musi być równa dziesiątej cyfrze. Reszta 10 oznacza, że taki NIP jest niepoprawny.</li>
</ol>
<h2 id="przyklad">Przykład krok po kroku</h2>
<p>Weźmy NIP 5265877635 z przykładu w dokumentacji.</p>
<div class="table-wrap"><table>
<thead><tr><th scope="col">Cyfra</th><th scope="col">5</th><th scope="col">2</th><th scope="col">6</th><th scope="col">5</th><th scope="col">8</th><th scope="col">7</th><th scope="col">7</th><th scope="col">6</th><th scope="col">3</th></tr></thead>
<tbody>
<tr><td>Waga</td><td>6</td><td>5</td><td>7</td><td>2</td><td>3</td><td>4</td><td>5</td><td>6</td><td>7</td></tr>
<tr><td>Iloczyn</td><td>30</td><td>10</td><td>42</td><td>10</td><td>24</td><td>28</td><td>35</td><td>36</td><td>21</td></tr>
</tbody></table></div>
<p>Suma iloczynów wynosi 236. Po podzieleniu przez 11 (21 razy 11 to 231) zostaje reszta 5, a dziesiąta cyfra NIP to właśnie 5. NIP przechodzi kontrolę.</p>
<h2 id="bledy">Co wykryje kontrola – cztery przypadki</h2>
<div class="table-wrap"><table>
<thead><tr><th scope="col">NIP</th><th scope="col">Suma</th><th scope="col">Reszta</th><th scope="col">Ostatnia cyfra</th><th scope="col">Wynik</th></tr></thead>
<tbody>
<tr><td>5265877635</td><td>236</td><td>5</td><td>5</td><td>poprawny</td></tr>
<tr><td>5265877636</td><td>236</td><td>5</td><td>6</td><td>błędna cyfra kontrolna</td></tr>
<tr><td>5265877365</td><td>239</td><td>8</td><td>5</td><td>zamienione cyfry</td></tr>
<tr><td>5265877535</td><td>230</td><td>10</td><td>5</td><td>reszta 10, NIP niepoprawny</td></tr>
</tbody></table></div>
<p>Drugi wiersz pokazuje zmianę ostatniej cyfry, trzeci zamianę dwóch cyfr w środku, a czwarty zmianę jednej cyfry tak, że reszta wynosi 10. Wszystkie obliczenia wykonaliśmy tym samym algorytmem. Drugi przykład poprawnego NIP: 1234563218 (suma 118, reszta 8, ostatnia cyfra 8).</p>
<h2 id="czego-nie">Czego kontrola NIP nie potwierdza</h2>
<p>Poprawna cyfra kontrolna oznacza tylko, że NIP ma prawidłowy zapis. Nie wynika z niej, że firma istnieje, jest czynnym podatnikiem VAT ani że to ona wystawiła fakturę. Takie rzeczy sprawdza się w oficjalnych rejestrach, a nie w naszym narzędziu, które działa lokalnie w przeglądarce. Podobnie poprawny NIP w numerze KSeF nie dowodzi, że faktura jest w systemie.</p>
<h2 id="kolejnosc">W jakiej kolejności walidator sprawdza numer</h2>
<p>Najpierw długość i dozwolone znaki, potem NIP, data i na końcu suma CRC-8 z całych 32 znaków. Jeśli NIP jest błędny, a suma CRC-8 zgodna, numer mógł powstać z poprawnych danych, których NIP przepisano inaczej niż na fakturze. Zawsze porównaj go wtedy z oryginałem. O samej sumie CRC-8 piszemy w artykule <a href="/blog/suma-kontrolna-crc8-numer-ksef/">suma kontrolna CRC-8 w numerze KSeF</a>.</p>
<h2 id="lista">Przykład: kontrola listy sprzedawców</h2>
<p>Księgowa dostaje arkusz z 40 numerami KSeF od dostawców. Wczytuje go do <a href="/sprawdz-wiele-numerow-ksef/">narzędzia do sprawdzania wielu numerów</a>, które zaznacza wiersze z błędnym NIP lub sumą. Do poprawy wracają tylko te pozycje, a reszta trafia do przelewów. To przykład organizacji pracy, nie wymóg prawny.</p>
<h2 id="wskazowki">Praktyczne wskazówki</h2>
<ul>
<li>Kopiuj numer z aplikacji lub PDF zamiast przepisywać go ręcznie.</li>
<li>Usuń dodatkowe spacje, które dokleja czytnik PDF.</li>
<li>Przy błędzie NIP porównaj go z NIP-em na fakturze i w umowie.</li>
<li>Pamiętaj, że w schemacie FA(3) pole numeru KSeF może mieć inny prefiks, o czym ostrzega walidator.</li>
</ul>
<p>Jeśli numer ma błąd, sprawdź nasz poradnik o <a href="/blog/blad-przepisania-numeru-ksef/">błędzie przy przepisaniu numeru KSeF</a>.</p>
<h2 id="typowe">Typowe pomyłki przy przepisywaniu NIP</h2>
<p>Najczęściej myli się kolejność dwóch sąsiednich cyfr, pomija jedną cyfrę albo wpisuje NIP z myślnikami, choć w numerze KSeF występuje on w jednym ciągu 10 cyfr. Kontrola wag wychwytuje większość takich błędów, bo każda pozycja ma inną wagę, więc zamiana dwóch różnych cyfr zwykle zmienia sumę. Nie wychwyci jej, gdy zmiana daje tę samą resztę z dzielenia przez 11, dlatego warto zawsze porównać numer z oryginałem.</p>
<p>Warto też pamiętać, że NIP sprzedawcy znajdziesz na fakturze w danych sprzedawcy. Jeśli różni się od pierwszych 10 cyfr numeru KSeF, sprawdź, czy skopiowałeś numer właściwej faktury. W razie wątpliwości zapytaj sprzedawcę albo sprawdź fakturę w Aplikacji Podatnika KSeF. Po zmianach w tytule przelewu zajrzyj do artykułu <a href="/blog/jak-wpisac-numer-ksef-w-tytule-przelewu/">jak wpisać numer KSeF w tytule przelewu</a>.</p>
<h2 id="po-co">Po co sprawdzać NIP, skoro jest suma CRC-8</h2>
<p>Obie kontrole działają niezależnie. Suma CRC-8 obejmuje cały początek numeru, więc wychwytuje pomyłkę w dowolnym z 32 znaków, ale nie mówi, w którym miejscu błąd leży. Osobna kontrola NIP od razu wskazuje, że problem dotyczy identyfikatora sprzedawcy, a nie daty ani części technicznej. Dzięki temu łatwiej znaleźć przyczynę i poprawić tylko tę część, którą trzeba.</p>
<p>Gdy walidator pokazuje błąd tylko w NIP, a pozostałe kontrole przechodzą, sprawdź, czy numer nie pochodzi od innego podmiotu niż zakładałeś. Taką sytuację omawiamy też w artykule <a href="/blog/jak-sprawdzic-czy-numer-ksef-jest-poprawny/">jak sprawdzić, czy numer KSeF jest poprawny</a>.</p>
<h2 id="zrodla-info">Źródła i stan prawny</h2>
<p>Budowa numeru pochodzi z dokumentacji CIRFMF dla KSeF 2.0 i stron MF. Wzór wag NIP jest powszechnie stosowanym algorytmem walidacji numeru; treść ma charakter informacyjny i nie stanowi doradztwa podatkowego.</p>
<h2 id="podsumowanie">Podsumowanie</h2>
<p>NIP w numerze KSeF sprawdzisz wagami 6-5-7-2-3-4-5-6-7 i dzieleniem przez 11. Wynik potwierdza tylko poprawność zapisu. Wklej numer w <a href="/">walidatorze numeru KSeF</a>, a większą listę w <a href="/sprawdz-wiele-numerow-ksef/">sprawdzaniu wielu numerów</a>.</p>
""",
    faq=[
        ("Jak obliczyć cyfrę kontrolną NIP z numeru KSeF?", "Pomnóż pierwszych dziewięć cyfr przez wagi 6-5-7-2-3-4-5-6-7, zsumuj i weź resztę z dzielenia przez 11. Musi równać się dziesiątej cyfrze."),
        ("Co oznacza reszta 10 przy sprawdzaniu NIP?", "Taki NIP jest niepoprawny, bo cyfra kontrolna nie może mieć wartości 10."),
        ("Czy poprawny NIP w numerze KSeF oznacza, że sprzedawca jest czynnym podatnikiem VAT?", "Nie. Cyfra kontrolna sprawdza tylko zapis, a status podatnika weryfikuje się w oficjalnych rejestrach."),
        ("Co zrobić, gdy NIP w numerze KSeF jest błędny?", "Porównaj numer z oryginałem na fakturze lub w aplikacji i skopiuj go ponownie zamiast przepisywać."),
    ],
    sources=[DOC_NUM, MF_NUM, MF_AP],
)

CAL_POSTS = CAL_POSTS + [C34]
