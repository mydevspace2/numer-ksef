# -*- coding: utf-8 -*-
# Posty z kalendarza (work/seo/blog-calendar.md). Każdy: slug, title (<=60), desc (70–159), h1, intro, lead_tool,
# date (ISO, PL), content (HTML), faq [(q, a)], sources. Dopisuj nowe na końcu listy CAL_POSTS.
from sources import MF_NUM, MF_TERM, DOC_NUM, XSD, MF_QR, APP, MF_FA3

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

CAL_POSTS = [C01, C02, C03]
