# -*- coding: utf-8 -*-
# Posty z kalendarza (work/seo/blog-calendar.md). Każdy: slug, title (<=60), desc (70–159), h1, intro, lead_tool,
# date (ISO, PL), content (HTML), faq [(q, a)], sources. Dopisuj nowe na końcu listy CAL_POSTS.
from sources import MF_NUM, MF_TERM, DOC_NUM, XSD, MF_QR, APP, MF_FA3
from sources import MF_NUM, MF_TERM, DOC_NUM, XSD, MF_QR, APP, MF_FA3, MBANK_SPEC, MBANK_IMPORT, MBANK_NEWS, DB
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

CAL_POSTS = [C01, C02, C03, C04, C05, C06]
