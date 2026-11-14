# -*- coding: utf-8 -*-
# v3 (13.11.2026): Kontakt, Regulamin, Blog (indeks + 3 artykuły)
from sources import MF_NUM, MF_TERM, DOC_NUM, MBANK_SPEC, MBANK_NEWS, IZ_PDF, IZ_PDF2, MF_QR, APP, ZBP

EMAIL = "topelitemindset1@gmail.com"

KONTAKT = dict(
    title="Kontakt – NumerKSeF, darmowe narzędzia KSeF",
    desc="Kontakt z autorem serwisu NumerKSeF: zgłoś błąd w narzędziu, zaproponuj nową funkcję lub popraw informację o KSeF. Odpowiadamy mailowo.",
    app=False, trust=False, related=False,
    h1="Kontakt",
    intro="Masz pytanie o działanie narzędzi, znalazłeś błąd albo brakuje Ci jakiejś funkcji? Napisz do nas.",
    trail=[("Strona główna", "/"), ("Kontakt", "/kontakt/")],
    content="""
<h2>Adres e-mail</h2>
<p>Najszybciej skontaktujesz się z nami mailowo:</p>
<p class="mono"><strong>""" + EMAIL + """</strong></p>
<p>Adres podajemy jako tekst – skopiuj go do swojego programu pocztowego. Staramy się odpowiadać w ciągu kilku dni roboczych.</p>

<h2>Uwagi i zgłoszenia błędów</h2>
<p>Każda uwaga pomaga ulepszyć narzędzia. Jeśli zgłaszasz błąd, napisz:</p>
<ul>
<li>na której stronie wystąpił (np. walidator numeru, generator komunikatu MPP),</li>
<li>co wpisałeś lub jaki plik wczytałeś – <strong>bez prawdziwych danych kontrahentów</strong>; wystarczy opis lub zmieniony przykład,</li>
<li>jaki wynik zobaczyłeś, a jakiego się spodziewałeś,</li>
<li>z jakiej przeglądarki i urządzenia korzystasz.</li>
</ul>
<p>Chętnie poznamy też pomysły na nowe funkcje oraz informacje o zmianach w przepisach lub w formularzach banków, które powinniśmy uwzględnić.</p>

<h2>Czego nie robimy</h2>
<p>NumerKSeF to niezależny serwis, niezwiązany z Ministerstwem Finansów. Nie udzielamy porad podatkowych, nie mamy dostępu do Twoich faktur w KSeF i nie możemy sprawdzić, czy konkretna faktura istnieje w systemie. W sprawach dotyczących Twojej firmy skontaktuj się z księgową, doradcą podatkowym lub Krajową Informacją Skarbową. Informacje o samym systemie publikuje MF na stronie <a href="https://ksef.podatki.gov.pl/" rel="noopener" target="_blank">ksef.podatki.gov.pl</a>.</p>
<p>Zobacz też: <a href="/o-serwisie/">O serwisie</a> · <a href="/regulamin/">Regulamin</a> · <a href="/polityka-prywatnosci/">Polityka prywatności</a>.</p>
""",
)

REGULAMIN = dict(
    title="Regulamin korzystania z narzędzi – NumerKSeF",
    desc="Regulamin serwisu NumerKSeF: bezpłatne narzędzia KSeF bez rejestracji, dane przetwarzane wyłącznie w przeglądarce, brak gwarancji i charakter informacyjny.",
    app=False, trust=False, related=False,
    h1="Regulamin serwisu NumerKSeF",
    intro="Zasady korzystania z bezpłatnych narzędzi i treści dostępnych w serwisie numerksef.dpdns.org.",
    trail=[("Strona główna", "/"), ("Regulamin", "/regulamin/")],
    content="""
<h2>1. Postanowienia ogólne</h2>
<p>Serwis NumerKSeF (numerksef.dpdns.org) udostępnia bezpłatne narzędzia internetowe do pracy z numerami Krajowego Systemu e-Faktur (KSeF), przelewami i fakturami ustrukturyzowanymi oraz artykuły poradnikowe. Korzystając z serwisu, akceptujesz ten regulamin. Serwis jest niezależny i nie jest powiązany z Ministerstwem Finansów ani innymi organami administracji.</p>

<h2>2. Bezpłatność i brak rejestracji</h2>
<p>Wszystkie narzędzia są bezpłatne i nie wymagają zakładania konta, logowania ani podawania danych osobowych. Nie pobieramy opłat i nie oferujemy usług płatnych.</p>

<h2>3. Dane przetwarzane wyłącznie w przeglądarce</h2>
<p>Numery KSeF, NIP-y, kwoty, pliki XML i inne dane, które wpisujesz lub wczytujesz, są przetwarzane wyłącznie w Twojej przeglądarce, na Twoim urządzeniu. Nie są wysyłane na serwer serwisu ani do podmiotów trzecich i nie są przez nas zapisywane. Serwis nie łączy się z KSeF ani z bankami. Jedyną informacją zapisywaną lokalnie jest wybrany przez Ciebie tryb jasny lub ciemny (w pamięci localStorage przeglądarki). Szczegóły opisuje <a href="/polityka-prywatnosci/">Polityka prywatności</a>.</p>

<h2>4. Brak gwarancji</h2>
<p>Narzędzia i treści udostępniamy w stanie „takim, jaki jest”, bez jakichkolwiek gwarancji – w szczególności gwarancji poprawności, kompletności, aktualności ani przydatności do określonego celu. Narzędzia sprawdzają jedynie format i sumy kontrolne; nie potwierdzają, że faktura istnieje w KSeF, że numer należy do danej faktury ani że rachunek bankowy jest prawidłowy. Przed wykonaniem płatności zawsze porównaj wynik z dokumentami źródłowymi.</p>

<h2>5. Odpowiedzialność</h2>
<p>W najszerszym zakresie dopuszczalnym przez prawo nie odpowiadamy za szkody wynikłe z korzystania z serwisu lub z niemożności korzystania z niego, w tym za błędnie zrealizowane przelewy, odrzucone płatności czy skutki podatkowe. Odpowiedzialność za treść przelewów i rozliczenia podatkowe ponosi użytkownik.</p>

<h2>6. Charakter informacyjny treści</h2>
<p>Artykuły i opisy mają charakter wyłącznie informacyjny i nie stanowią porady podatkowej ani prawnej. Przepisy dotyczące KSeF wciąż się zmieniają – każdą stronę opatrujemy datą aktualizacji i linkami do źródeł. W sprawach dotyczących Twojej firmy skonsultuj się z księgową lub doradcą podatkowym.</p>

<h2>7. Zasady korzystania</h2>
<p>Nie wolno używać serwisu w sposób zakłócający jego działanie ani do celów niezgodnych z prawem, np. do tworzenia fałszywych kodów QR lub podrabiania faktur. Możesz swobodnie linkować do dowolnej strony serwisu.</p>

<h2>8. Zmiany regulaminu i kontakt</h2>
<p>Regulamin może być aktualizowany wraz z rozwojem serwisu; aktualna wersja jest zawsze dostępna na tej stronie. Pytania dotyczące regulaminu kieruj przez stronę <a href="/kontakt/">Kontakt</a>.</p>
""",
)

# ------------------------------------------------------------------ BLOG
POST1 = dict(
    slug="jak-wpisac-numer-ksef-w-tytule-przelewu",
    title="Jak wpisać numer KSeF w tytule przelewu? Wzory na 2027",
    desc="Jak wpisać numer KSeF w tytule przelewu od 1 stycznia 2027 r.: jedna faktura, kilka faktur, identyfikator zbiorczy i MPP. Wzory, limit 140 znaków, błędy.",
    h1="Jak wpisać numer KSeF w tytule przelewu – wzory i przykłady",
    intro="Od 1 stycznia 2027 r. przelew między czynnymi podatnikami VAT za fakturę z KSeF musi zawierać jej numer KSeF. Pokazujemy, jak zapisać go poprawnie w każdej typowej sytuacji.",
    lead_tool=("/", "walidator numeru KSeF"),
    content="""
<h2 id="kogo-dotyczy">Kogo dotyczy obowiązek</h2>
<p>Obowiązek wynika z art. 108g ustawy o VAT i zaczyna się 1 stycznia 2027 r. Ministerstwo Finansów pisze, że do końca 2026 r. <q>odroczony jest obowiązek podawania numeru KSeF faktury podczas płatności pomiędzy podatnikami czynnymi</q> oraz w ramach MPP. Dotyczy więc sytuacji, w której:</p>
<ul>
<li>płacisz <strong>przelewem</strong> lub innym instrumentem, który pozwala podać tytuł płatności (nie gotówką),</li>
<li>zarówno Ty, jak i odbiorca jesteście <strong>czynnymi podatnikami VAT</strong>,</li>
<li>płacisz za fakturę wystawioną <strong>w KSeF</strong>.</li>
</ul>
<p>Gdy jedna ze stron jest zwolniona z VAT, numer możesz podać dobrowolnie. Wyjątek stanowią faktury wystawione w trybie awaryjnym oraz faktury offline, które nie zostały wprowadzone do KSeF z powodu ogłoszonej awarii – przy nich podajesz zwykły numer faktury.</p>

<h2 id="wzory">Wzory tytułu przelewu</h2>
<p>Przepisy nie narzucają składni zwykłego tytułu – liczy się, żeby numer KSeF w nim był. Bank zwykle pozwala na 140 znaków, a numer KSeF ma ich 35. Sprawdzone wzory:</p>
<div class="table-wrap"><table>
<thead><tr><th scope="col">Sytuacja</th><th scope="col">Co wpisać w tytule</th><th scope="col">Długość</th></tr></thead>
<tbody>
<tr><th scope="row">Jedna faktura</th><td class="mono">5265877635-20250826-0100001AF629-AF</td><td>35 znaków</td></tr>
<tr><th scope="row">Jedna faktura + Twój opis</th><td class="mono">5265877635-20250826-0100001AF629-AF FV 12/11/2026</td><td>49 znaków</td></tr>
<tr><th scope="row">Dwie faktury</th><td class="mono">5265877635-20250826-0100001AF629-AF, 9510001233-20261102-01A3F0C2B7D4-B8</td><td>72 znaki</td></tr>
<tr><th scope="row">Trzy faktury</th><td>trzy numery oddzielone przecinkami</td><td>107 znaków</td></tr>
<tr><th scope="row">Cztery i więcej faktur jednego sprzedawcy</th><td class="mono">1111111111-IZ202607-65ED02180000-E7</td><td>35 znaków (identyfikator zbiorczy)</td></tr>
</tbody></table></div>
<p>Czwarty numer już się nie zmieści: 4 × 35 znaków plus separatory to ponad 140. Wtedy zamiast listy numerów użyj identyfikatora zbiorczego, który obejmuje do 500 faktur (w Aplikacji Podatnika KSeF do 50).</p>

<h2 id="przyklad">Przykład krok po kroku</h2>
<p>Firma Beta (czynny VAT) płaci firmie Alfa (czynny VAT, NIP 5265877635) za fakturę FV 12/11/2026 o numerze KSeF <code>5265877635-20250826-0100001AF629-AF</code>.</p>
<ol class="steps">
<li><strong>Znajdź numer KSeF.</strong> Księgowa Bety odczytuje go w programie księgowym, który pobrał fakturę z KSeF. Jeśli nie wiesz, gdzie szukać, przeczytaj artykuł <a href="/blog/gdzie-znalezc-numer-ksef-faktury/">gdzie znaleźć numer KSeF faktury</a>.</li>
<li><strong>Sprawdź go.</strong> Wkleja numer do <a href="/">walidatora numeru KSeF</a>. Narzędzie potwierdza długość, NIP Alfy na początku, datę i sumę kontrolną AF.</li>
<li><strong>Ułóż tytuł.</strong> W polu opisu dopisuje „FV 12/11/2026”. Wynik: <code>5265877635-20250826-0100001AF629-AF FV 12/11/2026</code>.</li>
<li><strong>Skopiuj do banku.</strong> Przycisk „Kopiuj” przenosi tekst do schowka – wystarczy wkleić go w polu „Tytuł” przelewu.</li>
</ol>
<p>Co dokładnie sprawdza walidator i jak rozpoznać typowe literówki, opisujemy w artykule <a href="/blog/jak-sprawdzic-czy-numer-ksef-jest-poprawny/">jak sprawdzić, czy numer KSeF jest poprawny</a>.</p>
<p>Kolejność ma znaczenie praktyczne: numer KSeF na początku tytułu nie zostanie obcięty nawet wtedy, gdy bank lub program odbiorcy skraca długie opisy.</p>

<h2 id="mpp">Numer KSeF w przelewie MPP</h2>
<p>W mechanizmie podzielonej płatności nie ma swobodnego tytułu. Bank oczekuje komunikatu w formacie <code>/VAT/10n,2n/IDC/14x/INV/35x/TXT/33x</code> o łącznej długości do 140 znaków. Numer KSeF lub identyfikator zbiorczy trafia do pola <code>/INV/</code>, które ma dokładnie 35 znaków. Twój własny numer faktury możesz dopisać w <code>/TXT/</code> (do 33 znaków). Przykład:</p>
<p class="mono">/VAT/230,00/IDC/5265877635/INV/5265877635-20250826-0100001AF629-AF/TXT/FV 12/11/2026</p>
<p>Komunikat najłatwiej przygotować w <a href="/przelew-mpp-numer-ksef/">generatorze komunikatu przelewu MPP z numerem KSeF</a>, który pilnuje przecinka w kwocie VAT, kolejności pól i zabronionych znaków. Część banków wprowadza osobne pola formularza – mBank zapowiedział, że w polu „Numer faktury” będzie można wpisać także numer KSeF.</p>

<h2 id="szczegolne">Szczególne sytuacje</h2>
<h3>Płatność częściowa</h3>
<p>Gdy płacisz tylko część jednej faktury, w tytule nadal wpisujesz jej numer KSeF – kwota przelewu po prostu jest niższa niż należność. Przy kilku fakturach płaconych częściowo pomocny jest identyfikator zbiorczy: podczas jego generowania można wskazać kwotę płatności za każdą fakturę, walutę i opis do 512 znaków.</p>
<h3>Faktura offline lub z trybu awaryjnego</h3>
<p>Numer KSeF podajesz także przy fakturach wystawionych w trybie offline (niedostępność KSeF, offline24), gdy zostały już przesłane do systemu. Nie musisz go podawać przy fakturach z trybu awaryjnego ani przy fakturach offline, które z powodu ogłoszonej awarii nie trafiły do KSeF – wtedy w tytule wpisz zwykły numer faktury.</p>
<h3>Polecenie zapłaty i płatność za kogoś</h3>
<p>Przy poleceniu zapłaty numer KSeF podaje wystawca faktury, który inicjuje pobranie środków. Jeśli za fakturę wystawioną na Twoją firmę płaci inny podatnik, np. spółka z grupy, to on musi wpisać numer KSeF w przelewie.</p>
<h3>Kilka faktur od różnych sprzedawców</h3>
<p>Każdy sprzedawca dostaje osobny przelew z numerami swoich faktur. Nie łącz w jednym tytule numerów od różnych firm – przelew trafia przecież na jeden rachunek.</p>

<h2 id="bledy">Najczęstsze błędy</h2>
<div class="table-wrap"><table>
<thead><tr><th scope="col">Błąd</th><th scope="col">Jak go uniknąć</th></tr></thead>
<tbody>
<tr><th scope="row">Litera O zamiast zera, I zamiast jedynki</th><td>Kopiuj numer zamiast przepisywać; walidator wskaże pozycję podejrzanego znaku.</td></tr>
<tr><th scope="row">Pominięty myślnik lub spacja w środku</th><td>Numer ma zawsze cztery części i trzy myślniki; wklej go w całości.</td></tr>
<tr><th scope="row">Numer faktury zamiast numeru KSeF</th><td>Numer faktury (np. FV/12/2027) nie zastępuje numeru KSeF – może być tylko dodatkiem.</td></tr>
<tr><th scope="row">Cztery numery w jednym tytule</th><td>Przekroczysz 140 znaków; użyj identyfikatora zbiorczego.</td></tr>
<tr><th scope="row">Numer z instrukcji banku</th><td>Przykłady z instrukcji są ilustracyjne i nie mają poprawnej sumy kontrolnej.</td></tr>
<tr><th scope="row">Stary numer w szablonie przelewu</th><td>Każda faktura ma inny numer KSeF – nie zapisuj go w stałym szablonie.</td></tr>
</tbody></table></div>

<h2 id="bank">Jak to wygląda w formularzu banku</h2>
<p>W większości bankowości internetowych zwykły przelew ma jedno pole „Tytuł” – wklejasz do niego cały tekst przygotowany w walidatorze. Przy przelewach MPP banki stosują różne formularze: jedne mają osobne pola na kwotę VAT, NIP i numer faktury, inne przyjmują cały komunikat w jednym polu. mBank zapowiedział, że w formularzu przelewu podzielonego pole „Numer faktury” przyjmie także numer KSeF, a dotychczasowe pole „Tytuł przelewu” zastąpi pole „Dodatkowe dane do faktury”. Przy pierwszej płatności w 2027 r. sprawdź, jak wygląda formularz w Twoim banku, i wyślij jeden przelew testowy.</p>
<p>Jeśli płacisz wiele faktur plikiem importu (np. Elixir z programu księgowego), sprawdź, czy program wstawia numer KSeF do tytułu. Gotowy plik możesz zweryfikować, wklejając tytuły do narzędzia <a href="/sprawdz-wiele-numerow-ksef/">sprawdź wiele numerów KSeF</a>.</p>

<h2 id="kod-qr">A co z kodem QR do płatności?</h2>
<p>Kody QR do przelewów (standard 2D Związku Banków Polskich) mają pole tytułu ograniczone do 32 znaków. Numer KSeF ma 35 znaków, więc się w nim nie zmieści. Po zeskanowaniu takiego kodu dopisz tytuł ręcznie, wklejając tekst przygotowany w walidatorze.</p>

<h2 id="podsumowanie">Podsumowanie</h2>
<ul>
<li>Od 1 stycznia 2027 r. numer KSeF w przelewie jest obowiązkowy między czynnymi podatnikami VAT.</li>
<li>Jedna faktura – jeden numer; kilka faktur – kilka numerów (do trzech w 140 znakach) albo identyfikator zbiorczy.</li>
<li>W MPP numer KSeF wpisujesz w <code>/INV/</code>, a numer faktury – opcjonalnie w <code>/TXT/</code>.</li>
<li>Przed wysłaniem przelewu sprawdź numer – literówka w 35 znakach zdarza się łatwo.</li>
</ul>
""",
    sources=[MF_TERM, MF_NUM, MBANK_SPEC, MBANK_NEWS, ZBP],
)

POST2 = dict(
    slug="gdzie-znalezc-numer-ksef-faktury",
    title="Gdzie znaleźć numer KSeF faktury? 6 miejsc",
    desc="Gdzie znaleźć numer KSeF faktury: Aplikacja Podatnika, program księgowy, UPO, nazwa pliku XML, kod QR na PDF. Dlaczego nie ma go w XML i jak go sprawdzić.",
    h1="Gdzie znaleźć numer KSeF faktury – 6 miejsc, w których go szukać",
    intro="Numer KSeF nadaje system po przyjęciu faktury, dlatego nie zawsze widać go od razu. Podpowiadamy, gdzie go szukać jako wystawca i jako nabywca.",
    lead_tool=("/", "sprawdź numer KSeF"),
    content="""
<h2 id="czym-jest">Czym jest numer KSeF i jak go rozpoznać</h2>
<p>Numer KSeF to unikalny identyfikator, który Krajowy System e-Faktur nadaje fakturze w chwili jej przyjęcia. Nie wybiera go wystawca i nie jest to numer faktury z pola P_2. Ma zawsze 35 znaków w układzie <code>NIP-RRRRMMDD-XXXXXXXXXXXX-XX</code>, np. <code>5265877635-20250826-0100001AF629-AF</code>:</p>
<ul>
<li>10 cyfr na początku to NIP wystawcy,</li>
<li>8 cyfr po pierwszym myślniku to data przyjęcia faktury do KSeF (nie data wystawienia),</li>
<li>12 znaków szesnastkowych to część techniczna,</li>
<li>2 ostatnie znaki to suma kontrolna CRC-8.</li>
</ul>
<p>Jeśli widzisz ciąg pasujący do tego wzoru, to prawie na pewno numer KSeF. Potwierdzisz to w kilka sekund w <a href="/">walidatorze numeru KSeF</a>. Więcej przykładów i podobnych numerów pokazujemy w artykule <a href="/blog/jak-wyglada-numer-ksef-przyklad/">jak wygląda numer KSeF</a>.</p>

<h2 id="szesc-miejsc">6 miejsc, w których znajdziesz numer KSeF</h2>
<div class="table-wrap"><table>
<thead><tr><th scope="col">Miejsce</th><th scope="col">Dla kogo</th><th scope="col">Uwagi</th></tr></thead>
<tbody>
<tr><th scope="row">1. Aplikacja Podatnika KSeF</th><td>wystawca i nabywca</td><td>bezpłatna aplikacja MF; numer widać w wykazie faktur sprzedażowych i zakupowych</td></tr>
<tr><th scope="row">2. Program księgowy lub fakturowy</th><td>wystawca i nabywca</td><td>programy zintegrowane z KSeF zapisują numer przy każdej fakturze</td></tr>
<tr><th scope="row">3. UPO</th><td>wystawca</td><td>urzędowe poświadczenie odbioru zawiera numer KSeF przyjętego dokumentu</td></tr>
<tr><th scope="row">4. Nazwa pliku XML</th><td>nabywca</td><td>pliki pobierane z KSeF często mają w nazwie numer KSeF</td></tr>
<tr><th scope="row">5. Wizualizacja PDF lub wydruk</th><td>nabywca</td><td>numer KSeF jest podpisem pod kodem QR (KOD I)</td></tr>
<tr><th scope="row">6. Sprzedawca</th><td>nabywca</td><td>gdy nie masz dostępu do KSeF, poproś kontrahenta o numer</td></tr>
</tbody></table></div>

<h3>1. Aplikacja Podatnika KSeF</h3>
<p>Po zalogowaniu się do bezpłatnej aplikacji Ministerstwa Finansów zobaczysz listy faktur wystawionych i otrzymanych. Każda pozycja ma swój numer KSeF. To najpewniejsze źródło, bo dane pochodzą wprost z systemu.</p>
<h3>2. Program księgowy</h3>
<p>Jeżeli fakturujesz w programie zintegrowanym z KSeF, po wysłaniu faktury program zapisuje zwrócony numer. Faktury zakupowe pobrane z KSeF również mają numer w osobnej kolumnie, którą zwykle można wyeksportować do Excela lub CSV.</p>
<h3>3. UPO – urzędowe poświadczenie odbioru</h3>
<p>Wystawca po wysłaniu faktury otrzymuje UPO. MF zaznacza, że numer KSeF <q>zwracany jest w UPO</q> – to dokument, do którego warto sięgnąć, gdy w programie czegoś brakuje.</p>
<h3>4. Nazwa pliku XML</h3>
<p>Numeru KSeF <strong>nie ma w treści pliku XML</strong> faktury – według MF nie stanowi on elementu pliku. Pliki pobierane z systemu lub z programów są jednak często nazywane numerem KSeF, np. <code>5265877635-20250826-0100001AF629-AF.xml</code>. Nasze narzędzie <a href="/przelew-z-faktury-xml-ksef/">przelew z faktury XML KSeF</a> odczytuje numer właśnie z nazwy pliku.</p>
<h3>5. Kod QR na wizualizacji</h3>
<p>Faktura przekazana poza KSeF, np. jako PDF, powinna mieć kod QR (KOD I). Pod nim umieszcza się numer KSeF, a gdy faktura jeszcze go nie ma – napis OFFLINE. Sam kod QR zawiera link weryfikacyjny, a nie numer KSeF; możesz go sprawdzić w narzędziu <a href="/kod-qr-ksef/">kod QR KSeF</a>.</p>
<h3>6. Kontrahent</h3>
<p>Jeśli faktura dotarła mailem bez numeru i nie masz dostępu do KSeF, poproś sprzedawcę o numer albo o wizualizację z kodem QR. Od 2027 r. będzie to standardowa prośba, bo bez numeru trudno poprawnie zapłacić.</p>

<h2 id="przyklad">Przykład: nabywca szuka numeru do przelewu</h2>
<p>Pan Tomasz dostał mailem fakturę w PDF od dostawcy materiałów biurowych. Pod kodem QR w rogu widnieje ciąg <code>9510001233-20261102-01A3F0C2B7D4-B8</code>. Kopiuje go do walidatora: 35 znaków, NIP 9510001233 poprawny, data 2 listopada 2026 r., suma kontrolna B8 zgodna. Walidator od razu układa tytuł przelewu, a Pan Tomasz dopisuje w opisie numer faktury dostawcy. Zajmuje to mniej niż minutę.</p>
<p>Gdyby pod kodem był napis OFFLINE, oznaczałoby to, że faktura nie miała jeszcze numeru KSeF w chwili tworzenia PDF-u. Wtedy numer trzeba odczytać z KSeF lub uzyskać od sprzedawcy, gdy faktura zostanie do systemu przesłana.</p>

<h2 id="kilka-faktur">Gdy płacisz kilka faktur naraz</h2>
<p>Zbierając numery do jednego przelewu, najwygodniej wyeksportować listę z programu księgowego i sprawdzić ją w narzędziu <a href="/sprawdz-wiele-numerow-ksef/">sprawdź wiele numerów KSeF</a>. Jeśli faktur od jednego sprzedawcy jest więcej niż trzy, zamiast numerów użyj identyfikatora zbiorczego – więcej w artykule <a href="/blog/identyfikator-zbiorczy-ksef-co-to-jest/">identyfikator zbiorczy KSeF – co to jest</a>. Gotowy numer wpiszesz w przelewie zgodnie z poradnikiem <a href="/blog/jak-wpisac-numer-ksef-w-tytule-przelewu/">jak wpisać numer KSeF w tytule przelewu</a>.</p>

<h2 id="jpk-korekty">Numer KSeF w JPK_VAT, korektach i fakturach końcowych</h2>
<p>Numer KSeF przydaje się nie tylko przy przelewie. Według MF w strukturze JPK_VAT z deklaracją obowiązującej od 1 lutego 2026 r. (JPK_V7M(3) i JPK_V7K(3)) wykazuje się numer KSeF faktury zarówno po stronie sprzedaży, jak i zakupów. Księgowa i tak musi go mieć – warto ustalić z nią, w jakiej formie będzie Ci go przekazywać do płatności, np. w eksporcie listy faktur do zapłaty.</p>
<p>Numer KSeF innej faktury znajdziesz też w treści niektórych dokumentów. Faktura korygująca do faktury ustrukturyzowanej podaje numer KSeF faktury pierwotnej, a faktura rozliczająca zaliczki – numery KSeF faktur zaliczkowych. To nie są numery KSeF dokumentu, który trzymasz w ręku: numer korekty lub faktury końcowej znajdziesz tak samo jak każdy inny – w KSeF, w programie, w UPO, w nazwie pliku lub pod kodem QR.</p>

<h2 id="jak-sprawdzic">Jak sprawdzić, czy znaleziony numer jest poprawny</h2>
<ol class="steps">
<li>Wklej numer do <a href="/">walidatora numeru KSeF</a> – sprawdzi długość, NIP, datę i sumę kontrolną CRC-8.</li>
<li>Porównaj NIP z początku numeru z NIP-em sprzedawcy na fakturze.</li>
<li>Gdy masz plik XML, wczytaj go w narzędziu <a href="/przelew-z-faktury-xml-ksef/">przelew z faktury XML</a>, a gdy PDF z kodem QR – sprawdź link w narzędziu <a href="/kod-qr-ksef/">kod QR KSeF</a>.</li>
</ol>
<p>Walidator potwierdza, że numer jest zbudowany poprawnie, ale nie to, że należy do konkretnej faktury. To wiadomo tylko w KSeF.</p>

<h2 id="czeste-pytania">Najczęstsze nieporozumienia</h2>
<ul>
<li><strong>„Numer KSeF jest w XML”</strong> – nie jest; szukaj go w UPO, w KSeF, w nazwie pliku lub pod kodem QR.</li>
<li><strong>„Data w numerze to data wystawienia”</strong> – to data przyjęcia faktury przez KSeF; może różnić się od daty z pola P_1.</li>
<li><strong>„Mogę sam utworzyć numer KSeF”</strong> – nie; nadaje go wyłącznie system. Numer „wymyślony” zwykle nie przejdzie kontroli sumy kontrolnej.</li>
<li><strong>„Numer zaczyna się od mojego NIP-u”</strong> – na fakturze zakupowej zaczyna się od NIP-u sprzedawcy, nie Twojego (wyjątkiem jest m.in. samofakturowanie).</li>
</ul>

<h2 id="podsumowanie">Podsumowanie</h2>
<p>Numer KSeF najszybciej znajdziesz w Aplikacji Podatnika KSeF lub w programie księgowym. Wystawca ma go dodatkowo w UPO, a nabywca – często w nazwie pliku XML i pod kodem QR na wizualizacji. Zanim wpiszesz go w przelewie, sprawdź go walidatorem: kilka sekund chroni przed literówką, której odbiorca nie dopasuje do faktury.</p>
""",
    sources=[MF_NUM, DOC_NUM, MF_QR, APP],
)

POST3 = dict(
    slug="identyfikator-zbiorczy-ksef-co-to-jest",
    title="Identyfikator zbiorczy KSeF – co to jest i kiedy go użyć",
    desc="Identyfikator zbiorczy KSeF: co to jest, jak wygląda, limity 500/50/132, jak go użyć w zwykłym przelewie i w MPP oraz kiedy lepiej podać kilka numerów KSeF.",
    h1="Identyfikator zbiorczy KSeF – co to jest i jak go używać w przelewach",
    intro="Płacisz jednemu dostawcy za wiele faktur naraz? Od 2027 r. zamiast listy numerów KSeF możesz wpisać w przelewie jeden identyfikator zbiorczy. Wyjaśniamy, jak działa.",
    lead_tool=("/identyfikator-zbiorczy-ksef/", "sprawdź identyfikator zbiorczy KSeF"),
    content="""
<h2 id="definicja">Co to jest identyfikator zbiorczy</h2>
<p>Identyfikator zbiorczy (zbiorczy identyfikator płatności) to 35-znakowy ciąg generowany w KSeF, który zastępuje w przelewie listę numerów KSeF kilku faktur. Ministerstwo Finansów przewiduje, że przy płatności za więcej niż jedną fakturę podaje się <q>zbiorczy identyfikator … lub kilka numerów KSeF lub kilka zbiorczych identyfikatorów</q>, z uwzględnieniem ograniczeń technicznych pola tytułu. W przelewie MPP identyfikator zastępuje wpisywany dawniej okres.</p>

<h2 id="budowa">Jak wygląda identyfikator zbiorczy</h2>
<p>Ma taką samą długość jak numer KSeF, ale zamiast pełnej daty zawiera litery IZ oraz rok i miesiąc wygenerowania. Oficjalny przykład: <code>1111111111-IZ202607-65ED02180000-E7</code>.</p>
<div class="table-wrap"><table>
<thead><tr><th scope="col">Cecha</th><th scope="col">Numer KSeF</th><th scope="col">Identyfikator zbiorczy</th></tr></thead>
<tbody>
<tr><th scope="row">Długość</th><td>35 znaków</td><td>35 znaków</td></tr>
<tr><th scope="row">Środkowa część</th><td>data RRRRMMDD</td><td>IZ + RRRRMM</td></tr>
<tr><th scope="row">Obejmuje</th><td>jedną fakturę</td><td>2–500 faktur (w Aplikacji Podatnika do 50)</td></tr>
<tr><th scope="row">Sprzedawcy</th><td>jeden</td><td>jeden – wszystkie faktury muszą mieć tego samego sprzedawcę</td></tr>
<tr><th scope="row">Suma kontrolna</th><td>CRC-8</td><td>CRC-8 (ten sam algorytm)</td></tr>
<tr><th scope="row">Kto nadaje</th><td>KSeF przy przyjęciu faktury</td><td>KSeF na żądanie wystawcy, odbiorcy lub podmiotu trzeciego</td></tr>
</tbody></table></div>
<p>Identyfikator może wygenerować wystawca, odbiorca faktur albo podmiot trzeci związany z fakturą, jeśli ma w KSeF uprawnienie do wystawiania lub przeglądania faktur albo do obsługi identyfikatorów zbiorczych. Dziś służą do tego programy finansowo-księgowe połączone z API KSeF; MF zapowiada tę funkcję także w Aplikacji Podatnika KSeF. Przy generowaniu można dodatkowo wskazać kwotę płatności za każdą fakturę, walutę i opis do 512 znaków – przydatne przy płatnościach częściowych. Limit 500 faktur może zostać zwiększony na uzasadniony wniosek.</p>
<p>Jedna faktura może wchodzić w skład wielu identyfikatorów – według MF w maksymalnie 132 w danym kontekście. Dzięki temu, jeśli plan płatności się zmieni, możesz wygenerować nowy identyfikator dla innego zestawu faktur.</p>

<h2 id="kiedy">Kiedy identyfikator zbiorczy, a kiedy kilka numerów</h2>
<ul>
<li><strong>Zwykły przelew, 2–3 faktury</strong> – najprościej wpisać numery KSeF oddzielone przecinkami; trzy numery zajmują 107 z 140 znaków.</li>
<li><strong>Zwykły przelew, 4 faktury i więcej</strong> – numery się nie zmieszczą, potrzebny jest identyfikator zbiorczy (lub kilka identyfikatorów, jeśli faktur jest ponad 500).</li>
<li><strong>Przelew MPP, 2 faktury i więcej</strong> – pole <code>/INV/</code> mieści dokładnie 35 znaków, czyli jeden numer KSeF albo jeden identyfikator. Przy kilku fakturach identyfikator jest jedynym sposobem na jeden przelew MPP.</li>
<li><strong>Faktury od różnych sprzedawców</strong> – identyfikator nie pomoże; każdy sprzedawca to osobny przelew.</li>
</ul>

<h2 id="przyklad">Przykład: 12 faktur od jednego dostawcy w MPP</h2>
<p>Hurtownia wystawiła w lipcu 12 faktur z adnotacją „mechanizm podzielonej płatności”. Łączny VAT wynosi 4 600 zł. Nabywca chce zapłacić wszystko jednym przelewem MPP:</p>
<ol class="steps">
<li>W programie księgowym połączonym z KSeF wskazuje numery KSeF 12 faktur hurtowni i generuje identyfikator zbiorczy, np. <code>1111111111-IZ202607-65ED02180000-E7</code>.</li>
<li>Sprawdza identyfikator w narzędziu <a href="/identyfikator-zbiorczy-ksef/">identyfikator zbiorczy KSeF</a> – format, NIP, miesiąc i suma kontrolna są poprawne.</li>
<li>Sumuje kwoty brutto 12 faktur i wpisuje je jako kwotę przelewu.</li>
<li>W <a href="/przelew-mpp-numer-ksef/">generatorze komunikatu MPP</a> wpisuje VAT 4 600,00, NIP hurtowni i identyfikator. Otrzymuje: <code>/VAT/4600,00/IDC/1111111111/INV/1111111111-IZ202607-65ED02180000-E7</code> (67 znaków).</li>
<li>Zachowuje listę faktur objętych identyfikatorem w dokumentacji płatności.</li>
</ol>

<p>W przykładzie zostało jeszcze 73 znaki wolnego miejsca, więc nabywca może dodać pole <code>/TXT/</code> z krótkim opisem, np. <code>/TXT/FV lipiec 2026</code> (maksymalnie 33 znaki). Opis nie zastępuje identyfikatora, ale ułatwia księgowości sprzedawcy szybkie przypisanie wpłaty, zanim ktoś rozkoduje identyfikator w KSeF. W zwykłym przelewie podobną rolę pełni dopisek po identyfikatorze, np. „faktury za lipiec, 12 szt.”.</p>

<h2 id="odbiorca">Co robi odbiorca płatności</h2>
<p>Sprzedawca, który otrzymał wpłatę z identyfikatorem zbiorczym, nie odczyta z samego ciągu, których faktur dotyczy. KSeF pozwala jednak rozkodować identyfikator, czyli wyświetlić numery KSeF faktur, które obejmuje, a także sprawdzić, w jakich identyfikatorach występuje dana faktura. Dopiero wtedy można rozliczyć wpłatę na poszczególne faktury. Nasze narzędzie sprawdzi tylko format i sumę kontrolną – to dobry pierwszy filtr, który wychwyci literówkę w tytule wpłaty.</p>

<h2 id="czesciowe">Identyfikator zbiorczy przy płatnościach częściowych</h2>
<p>MF przewiduje, że podczas generowania identyfikatora można oprócz numerów KSeF wskazać kwotę płatności za każdą fakturę, kod waluty i opis faktur do 512 znaków. Ma to znaczenie, gdy płacisz faktury tylko w części – na przykład w ratach uzgodnionych z dostawcą. Odbiorca po rozkodowaniu identyfikatora zobaczy, jaką kwotę przypisałeś do każdej faktury. Przy kolejnej racie wygenerujesz nowy identyfikator – limit 132 identyfikatorów na fakturę w danym kontekście w praktyce wystarczy na długi harmonogram spłat.</p>

<h2 id="kilka-iz">Kilka identyfikatorów w jednym przelewie i różni nabywcy</h2>
<p>MF dopuszcza podanie w tytule kilku identyfikatorów zbiorczych, o ile zmieszczą się w polu – w zwykłym przelewie o długości 140 znaków będą to maksymalnie trzy. Przyda się to np. wtedy, gdy płacisz ponad 500 faktur jednego dostawcy. W MPP takiej możliwości nie ma, bo <code>/INV/</code> mieści tylko jeden ciąg 35 znaków.</p>
<p>Ciekawostka: na fakturach objętych jednym identyfikatorem mogą występować różni nabywcy (Podmiot2). Warunkiem jest wyłącznie ten sam sprzedawca. Dzięki temu np. centrala firmy może jednym identyfikatorem i jednym przelewem zapłacić dostawcy za faktury wystawione na kilka podmiotów z grupy, o ile ma do nich dostęp w KSeF.</p>

<h2 id="pulapki">Pułapki</h2>
<div class="table-wrap"><table>
<thead><tr><th scope="col">Problem</th><th scope="col">Rozwiązanie</th></tr></thead>
<tbody>
<tr><th scope="row">Kwota przelewu nie zgadza się z fakturami w identyfikatorze</th><td>Wygeneruj nowy identyfikator dla faktur, które faktycznie płacisz.</td></tr>
<tr><th scope="row">Ponad 50 faktur w Aplikacji Podatnika</th><td>Podziel faktury na kilka identyfikatorów albo użyj programu księgowego (limit API to 500).</td></tr>
<tr><th scope="row">Faktury od dwóch spółek z jednej grupy</th><td>To dwóch sprzedawców – dwa identyfikatory i dwa przelewy.</td></tr>
<tr><th scope="row">Pomylenie z IPKSeF</th><td>IPKSeF to 13-znakowy identyfikator płatności z pliku FA(3) (link do płatności) – to inny identyfikator.</td></tr>
</tbody></table></div>
<p>Więcej o zapisie w zwykłym przelewie przeczytasz w artykule <a href="/blog/jak-wpisac-numer-ksef-w-tytule-przelewu/">jak wpisać numer KSeF w tytule przelewu</a>.</p>

<h2 id="podsumowanie">Podsumowanie</h2>
<ul>
<li>Identyfikator zbiorczy to 35-znakowy ciąg z literami IZ, który w przelewie zastępuje listę numerów KSeF.</li>
<li>Obejmuje od 2 do 500 faktur jednego sprzedawcy (w Aplikacji Podatnika do 50); jedna faktura może być w 132 identyfikatorach.</li>
<li>Może go wygenerować wystawca, odbiorca lub podmiot trzeci z odpowiednimi uprawnieniami w KSeF.</li>
<li>W zwykłym przelewie wpisujesz go w tytule, w MPP – w polu <code>/INV/</code>; w MPP to jedyny sposób na zapłatę kilku faktur jednym przelewem.</li>
<li>Ma tę samą sumę kontrolną CRC-8 co numer KSeF, więc literówkę wychwycisz przed wysłaniem przelewu.</li>
</ul>
<p>Masz już identyfikator? Sprawdź go w narzędziu <a href="/identyfikator-zbiorczy-ksef/">identyfikator zbiorczy KSeF – walidator</a>, a komunikat MPP przygotuj w <a href="/przelew-mpp-numer-ksef/">generatorze komunikatu MPP</a>.</p>
""",
    sources=[MF_NUM, IZ_PDF, IZ_PDF2, MBANK_SPEC],
)

POSTS = [POST1, POST2, POST3]
from posts_cal import CAL_POSTS
POSTS += CAL_POSTS


def post_page(p):
    url = "/blog/%s/" % p["slug"]
    lead_url, lead_anchor = p["lead_tool"]
    cta = ('<p class="note">Narzędzie do tego artykułu: <a href="%s">%s</a> – za darmo, dane nie opuszczają przeglądarki.</p>'
           % (lead_url, lead_anchor))
    d_iso, d_pl = p.get("date", ("2026-11-13", "13 listopada 2026"))
    return dict(
        title=p["title"], desc=p["desc"], app=False, trust=False, article=True, date_iso=d_iso, faq=p.get("faq"),
        h1=p["h1"], intro=p["intro"],
        trail=[("Strona główna", "/"), ("Blog", "/blog/"), (p["h1"].split(" – ")[0], url)],
        content='<p class="updated">Opublikowano: <time datetime="%s">%s r.</time></p>' % (d_iso, d_pl) + cta + p["content"],
        sources=p["sources"],
    ), url


def blog_index():
    cards = "".join('<a href="/blog/%s/"><strong>%s</strong><span>%s</span></a>' % (p["slug"], p["h1"], p["desc"]) for p in reversed(POSTS))
    return dict(
        title="Blog NumerKSeF – poradniki o numerze KSeF i przelewach",
        desc="Poradniki o KSeF: jak wygląda i jak sprawdzić numer KSeF, jak wpisać go w tytule przelewu, gdzie go znaleźć i czym jest identyfikator zbiorczy.",
        app=False, trust=False,
        h1="Blog: poradniki o KSeF i płatnościach",
        intro="Krótkie, konkretne artykuły o numerach KSeF, przelewach i MPP. Każdy odsyła do darmowego narzędzia, które pomoże od razu zastosować wiedzę.",
        trail=[("Strona główna", "/"), ("Blog", "/blog/")],
        content='<h2>Najnowsze artykuły</h2><div class="hub">%s</div>'
                '<p>Artykuły mają charakter informacyjny i nie stanowią porady podatkowej. Masz pomysł na temat? <a href="/kontakt/">Napisz do nas</a>.</p>' % cards,
    )
