# -*- coding: utf-8 -*-
# v3 (13.11.2026): rozbudowa poradników na stronach narzędzi + dodatkowe pytania FAQ

HOME_EXTRA = """
<h2 id="przyklad">Przykład krok po kroku: od numeru do tytułu przelewu</h2>
<p>Załóżmy, że księgowa przesłała Ci numer <code>5265877635-20250826-0100001AF629-AF</code> i prosi o opłacenie faktury FV 12/11/2026. Oto, co sprawdza walidator, gdy klikniesz „Przykład”:</p>
<ol class="steps">
<li><strong>Długość.</strong> Po usunięciu spacji numer ma 35 znaków i cztery części rozdzielone myślnikami – format się zgadza.</li>
<li><strong>NIP 5265877635.</strong> Iloczyny cyfr i wag: 5×6 + 2×5 + 6×7 + 5×2 + 8×3 + 7×4 + 7×5 + 6×6 + 3×7 = 236. Reszta z dzielenia 236 przez 11 to 5, a ostatnia cyfra NIP-u to także 5 – NIP jest poprawny.</li>
<li><strong>Data 20250826.</strong> 26 sierpnia 2025 r. istnieje w kalendarzu i nie jest z przyszłości. Ponieważ jest wcześniejsza niż start KSeF 2.0, walidator doda ostrzeżenie, że to numer przykładowy lub z KSeF 1.0 – to oficjalny przykład z dokumentacji MF.</li>
<li><strong>Suma kontrolna.</strong> CRC-8 z pierwszych 32 znaków (<code>5265877635-20250826-0100001AF629</code>) wynosi AF i zgadza się z końcówką numeru. Gdyby ktoś przepisał końcówkę jako 7C, walidator pokaże błąd i podpowie poprawną wartość.</li>
<li><strong>Tytuł przelewu.</strong> Generator składa tekst <code>5265877635-20250826-0100001AF629-AF FV 12/11/2026</code> – 49 znaków, czyli daleko od limitu 140. Zostaje miejsce na dwa kolejne numery KSeF.</li>
</ol>

<h2 id="kogo-dotyczy">Kto musi wpisać numer KSeF w przelewie</h2>
<p>Obowiązek z art. 108g ustawy o VAT dotyczy relacji między dwoma czynnymi podatnikami VAT i płatności za faktury wystawione w KSeF. W innych sytuacjach numer możesz podać dobrowolnie – ułatwia to odbiorcy rozliczenie wpłaty.</p>
<div class="table-wrap"><table>
<thead><tr><th scope="col">Płacący</th><th scope="col">Odbiorca</th><th scope="col">Numer KSeF w przelewie od 1.01.2027</th></tr></thead>
<tbody>
<tr><th scope="row">Czynny podatnik VAT</th><td>Czynny podatnik VAT</td><td>Obowiązkowy (zwykły przelew i MPP)</td></tr>
<tr><th scope="row">Czynny podatnik VAT</th><td>Firma zwolniona z VAT</td><td>Dobrowolny</td></tr>
<tr><th scope="row">Firma zwolniona z VAT</th><td>Czynny podatnik VAT</td><td>Dobrowolny</td></tr>
<tr><th scope="row">Konsument</th><td>Dowolna firma</td><td>Nie dotyczy – faktury dla konsumentów w KSeF są dobrowolne</td></tr>
<tr><th scope="row">Dowolny płacący</th><td>Faktura z trybu awaryjnego lub offline niewprowadzona z powodu awarii</td><td>Wyjątek – podajesz zwykły numer faktury</td></tr>
</tbody></table></div>
<p>Obowiązek dotyczy polecenia przelewu i innych instrumentów płatniczych, które pozwalają podać tytuł płatności – nie płatności gotówką. Dotyczy też podmiotu trzeciego, który płaci za fakturę wystawioną na nabywcę, a przy poleceniu zapłaty – wystawcy faktury. Jeżeli płacisz kilka faktur jednym przelewem, możesz wpisać kilka numerów KSeF albo jeden <a href="/identyfikator-zbiorczy-ksef/">identyfikator zbiorczy</a>. Gdzie szukać numerów, opisujemy szczegółowo w artykule <a href="/blog/gdzie-znalezc-numer-ksef-faktury/">gdzie znaleźć numer KSeF faktury</a>, a zasady zapisu w tytule – w poradniku <a href="/blog/jak-wpisac-numer-ksef-w-tytule-przelewu/">jak wpisać numer KSeF w tytule przelewu</a>.</p>

<h2 id="dobre-praktyki">Dobre praktyki przed wysłaniem przelewu</h2>
<ul>
<li><strong>Kopiuj, nie przepisuj.</strong> 12 znaków szesnastkowych w części technicznej to idealne miejsce na pomyłkę O/0 lub B/8. Skopiuj numer z programu księgowego albo z UPO i wklej go tutaj.</li>
<li><strong>Numer KSeF na początku tytułu.</strong> Część banków skraca długie tytuły na potwierdzeniach. Gdy numer stoi na początku, odbiorca zobaczy go zawsze, a Twój opis najwyżej zostanie obcięty.</li>
<li><strong>Sprawdzaj całe paczki.</strong> Gdy płacisz kilkanaście faktur, wklej numery do narzędzia <a href="/sprawdz-wiele-numerow-ksef/">sprawdź wiele numerów KSeF</a> i pobierz raport CSV.</li>
<li><strong>Szablony w banku.</strong> Jeśli płacisz temu samemu dostawcy co miesiąc, nie zapisuj numeru KSeF w szablonie – każda faktura ma inny numer.</li>
</ul>
<p>Masz pytanie albo zauważyłeś błąd? Napisz przez stronę <a href="/kontakt/">Kontakt</a>. Zasady korzystania z narzędzi opisuje <a href="/regulamin/">Regulamin</a>, a sposób przetwarzania danych – <a href="/polityka-prywatnosci/">Polityka prywatności</a>. Więcej poradników znajdziesz na <a href="/blog/">blogu NumerKSeF</a>.</p>
"""

HOME_FAQ = [
    ("Czy numer KSeF to to samo co numer faktury?", "Nie. Numer faktury (pole P_2) nadaje wystawca i może mieć dowolną postać, np. FV/12/2027. Numer KSeF nadaje system po przyjęciu faktury, ma zawsze 35 znaków i zaczyna się od NIP-u wystawcy. Od 2027 r. w przelewie między czynnymi podatnikami VAT liczy się numer KSeF; numer faktury możesz dopisać, jeśli zmieści się w tytule."),
]

MPP_EXTRA = """
<h2 id="przyklad-mpp">Przykład: faktura 12 300 zł brutto zapłacona w MPP</h2>
<p>Dostawca o NIP 5265877635 wystawił w KSeF fakturę FV 7/01/2027 na 10 000 zł netto, 2 300 zł VAT, razem 12 300 zł. Faktura ma adnotację „mechanizm podzielonej płatności”, a jej numer KSeF to <code>5265877635-20250826-0100001AF629-AF</code> (oficjalny przykład MF). Tak budujemy komunikat:</p>
<ol class="steps">
<li><strong>/VAT/</strong> – kwota podatku z przecinkiem i dwoma miejscami po nim: <code>/VAT/2300,00</code>. Bez spacji, bez kropki jako separatora tysięcy.</li>
<li><strong>/IDC/</strong> – NIP wystawcy faktury, same cyfry: <code>/IDC/5265877635</code>.</li>
<li><strong>/INV/</strong> – cały numer KSeF z myślnikami: <code>/INV/5265877635-20250826-0100001AF629-AF</code>. To dokładnie 35 znaków – tyle, ile mieści pole.</li>
<li><strong>/TXT/</strong> – opcjonalnie Twój numer faktury: <code>/TXT/FV 7/01/2027</code>.</li>
</ol>
<p>Gotowy komunikat ma 84 znaki:</p>
<p class="mono">/VAT/2300,00/IDC/5265877635/INV/5265877635-20250826-0100001AF629-AF/TXT/FV 7/01/2027</p>
<p>W polu „kwota przelewu” wpisujesz całe 12 300,00 zł – bank sam przekaże 2 300 zł na rachunek VAT dostawcy, a 10 000 zł na jego rachunek rozliczeniowy. Jeśli formularz banku ma osobne pola (kwota VAT, NIP, numer faktury), skopiuj wartości przyciskami przy układzie czteroliniowym, zamiast wklejać cały komunikat.</p>

<h2 id="przed-po-2027">Pole /INV/ przed i po 1 stycznia 2027 r.</h2>
<div class="table-wrap"><table>
<thead><tr><th scope="col">Sytuacja</th><th scope="col">Do 31.12.2026</th><th scope="col">Od 1.01.2027</th></tr></thead>
<tbody>
<tr><th scope="row">Jedna faktura z KSeF</th><td>numer faktury lub numer KSeF</td><td>numer KSeF (35 znaków)</td></tr>
<tr><th scope="row">Kilka faktur z KSeF</th><td>okres, którego dotyczą faktury</td><td>identyfikator zbiorczy</td></tr>
<tr><th scope="row">Faktura spoza KSeF (awaria, tryb awaryjny)</th><td>numer faktury</td><td>numer faktury</td></tr>
<tr><th scope="row">Przekazanie między własnymi rachunkami VAT</th><td>PRZEKAZANIE WLASNE</td><td>PRZEKAZANIE WLASNE</td></tr>
</tbody></table></div>
<p>Wzory w tabeli opierają się na specyfikacji mBanku z 29.09.2026 r. i komunikatach MF. Banki aktualizują formularze w różnym tempie, dlatego przy pierwszej płatności w 2027 r. wyślij jeden przelew testowy i sprawdź, czy bank nie odrzucił komunikatu.</p>

<h2 id="mpp-kiedy">Kiedy w ogóle płacić w MPP</h2>
<p>Mechanizm podzielonej płatności jest obowiązkowy, gdy faktura dokumentuje sprzedaż towarów lub usług z załącznika nr 15 do ustawy o VAT, a kwota należności ogółem przekracza 15 000 zł. Wtedy sprzedawca umieszcza na fakturze adnotację „mechanizm podzielonej płatności” (w pliku FA(3) pole <code>P_18A</code> = 1). W pozostałych przypadkach MPP jest dobrowolny. Numer KSeF wpisujesz w komunikacie MPP niezależnie od tego, czy płacisz w nim z obowiązku, czy z wyboru. Jeżeli masz plik XML faktury, <a href="/przelew-z-faktury-xml-ksef/">przelew z faktury XML</a> sam odczyta to pole i przygotuje komunikat.</p>
<p>Więcej o samym zapisie numeru w zwykłym przelewie przeczytasz w artykule <a href="/blog/jak-wpisac-numer-ksef-w-tytule-przelewu/">jak wpisać numer KSeF w tytule przelewu</a>.</p>
"""

MPP_FAQ = [
    ("Czy każdą fakturę z numerem KSeF muszę płacić w MPP?", "Nie. MPP jest obowiązkowy tylko wtedy, gdy faktura obejmuje towary lub usługi z załącznika nr 15 do ustawy o VAT i kwota należności ogółem przekracza 15 000 zł. Numer KSeF podajesz w każdym przelewie między czynnymi podatnikami VAT – w zwykłym w tytule, a w MPP w polu /INV/."),
]

IZ_EXTRA = """
<h2 id="rozklad-iz">Przykład: rozkładamy identyfikator na części</h2>
<p>Weźmy oficjalny przykład z dokumentacji API KSeF: <code>1111111111-IZ202607-65ED02180000-E7</code>. Walidator czyta go tak:</p>
<div class="table-wrap"><table>
<thead><tr><th scope="col">Fragment</th><th scope="col">Co oznacza</th><th scope="col">Wynik kontroli</th></tr></thead>
<tbody>
<tr><th scope="row" class="mono">1111111111</th><td>NIP (wg grafiki MF z 9.11.2026 – NIP sprzedawcy)</td><td>suma kontrolna NIP poprawna</td></tr>
<tr><th scope="row" class="mono">IZ</th><td>oznaczenie identyfikatora zbiorczego (zamiast daty w numerze KSeF)</td><td>obecne</td></tr>
<tr><th scope="row" class="mono">202607</th><td>rok i miesiąc wygenerowania: lipiec 2026</td><td>miesiąc 01–12, nie z przyszłości</td></tr>
<tr><th scope="row" class="mono">65ED02180000</th><td>część techniczna – 12 znaków 0–9, A–F</td><td>format poprawny</td></tr>
<tr><th scope="row" class="mono">E7</th><td>CRC-8 z pierwszych 32 znaków, tak samo jak w numerze KSeF</td><td>zgodna</td></tr>
</tbody></table></div>
<p>Z samego ciągu nie da się odczytać, ile faktur obejmuje ani których. KSeF pozwala jednak „rozkodować” identyfikator – użytkownik z uprawnieniami zobaczy w systemie listę numerów KSeF, które obejmuje. Na fakturach w jednym identyfikatorze mogą występować różni nabywcy, ale zawsze ten sam sprzedawca.</p>

<h2 id="krok-po-kroku-iz">Jak zapłacić kilka faktur jednym przelewem – krok po kroku</h2>
<ol class="steps">
<li><strong>Zbierz faktury jednego sprzedawcy.</strong> Identyfikator obejmuje faktury tylko od jednego wystawcy. Faktury od dwóch dostawców to dwa przelewy.</li>
<li><strong>Wygeneruj identyfikator w KSeF.</strong> Może to zrobić wystawca, odbiorca faktur albo podmiot trzeci związany z fakturą, który ma odpowiednie uprawnienia. Program księgowy połączony z API KSeF obejmie do 500 faktur; w Aplikacji Podatnika KSeF, gdy MF udostępni tam tę funkcję, limit wyniesie 50. Przy płatności częściowej możesz przy generowaniu wskazać kwotę za każdą fakturę.</li>
<li><strong>Sprawdź go tutaj.</strong> Wklej wynik do walidatora powyżej – wychwyci literówkę, zanim pieniądze wyjdą z konta.</li>
<li><strong>Policz kwotę.</strong> Suma przelewu powinna odpowiadać sumie faktur objętych identyfikatorem. Przy MPP kwota w <code>/VAT/</code> to suma VAT z tych faktur.</li>
<li><strong>Wpisz identyfikator.</strong> W zwykłym przelewie – w tytule, w MPP – w polu <code>/INV/</code>. Pomoże w tym <a href="/przelew-mpp-numer-ksef/">generator komunikatu MPP</a>.</li>
</ol>
<p>Pełne omówienie, kiedy identyfikator się opłaca, a kiedy wystarczą zwykłe numery, znajdziesz w artykule <a href="/blog/identyfikator-zbiorczy-ksef-co-to-jest/">identyfikator zbiorczy KSeF – co to jest</a>.</p>
"""

IZ_FAQ = [
    ("Czy identyfikator zbiorczy może łączyć faktury z różnych miesięcy?", "Według informacji MF warunki są dwa: wszystkie faktury mają tego samego sprzedawcę, a ich liczba nie przekracza limitu (500, w Aplikacji Podatnika 50). Rok i miesiąc w identyfikatorze oznaczają moment jego wygenerowania, a nie datę faktur."),
    ("Czy identyfikator zbiorczy mogę wpisać w zwykłym przelewie, nie tylko w MPP?", "Tak. MF przewiduje identyfikator zbiorczy dla każdej płatności za więcej niż jedną fakturę: w zwykłym przelewie wpisujesz go w tytule, a w przelewie MPP w polu /INV/. W zwykłym przelewie możesz alternatywnie wpisać kilka numerów KSeF, jeśli zmieszczą się w polu tytułu."),
]

BULK_EXTRA = """
<h2 id="przyklad-lista">Przykład: kontrola listy przed paczką przelewów</h2>
<p>Księgowa przygotowała w Excelu zestawienie pięciu faktur do zapłaty. Kopiujesz kolumnę z numerami i wklejasz ją do pola powyżej. Wynik może wyglądać tak:</p>
<div class="table-wrap"><table>
<thead><tr><th scope="col">Wiersz</th><th scope="col">Wklejony tekst</th><th scope="col">Status</th><th scope="col">Co zrobić</th></tr></thead>
<tbody>
<tr><th scope="row">1</th><td class="mono">5265877635-20250826-0100001AF629-AF</td><td>poprawny (ostrzeżenie: data przykładowa)</td><td>nic</td></tr>
<tr><th scope="row">2</th><td class="mono">9510001233-20261102-01A3F0C2B7D4-B8</td><td>poprawny</td><td>nic</td></tr>
<tr><th scope="row">3</th><td class="mono">5265877635-20250826-0100001AF629-7C</td><td>błąd sumy kontrolnej</td><td>skopiuj numer ponownie z UPO</td></tr>
<tr><th scope="row">4</th><td class="mono">1111111111-IZ202607-65ED02180000-E7</td><td>identyfikator zbiorczy</td><td>upewnij się, że kwota obejmuje wszystkie faktury z IZ</td></tr>
<tr><th scope="row">5</th><td>FV/123/11/2026</td><td>brak numeru KSeF</td><td>ustal numer KSeF tej faktury</td></tr>
</tbody></table></div>
<p>Dwa wiersze wymagają poprawki, zanim przygotujesz przelewy. Raport CSV z kolumnami Wiersz, Status, Numer, Typ, NIP, Data, Uwagi i Tekst źródłowy możesz dołączyć do dokumentacji płatności albo odesłać dostawcy, prosząc o właściwe numery.</p>

<h2 id="skad-dane">Skąd brać dane do sprawdzenia</h2>
<ul>
<li><strong>Program księgowy lub ERP</strong> – wyeksportuj rejestr faktur zakupowych z kolumną „numer KSeF” do CSV i wgraj plik w całości. Narzędzie samo znajdzie numery w każdym wierszu, bez wskazywania kolumny.</li>
<li><strong>Arkusz Excel</strong> – zaznacz kolumnę, skopiuj (Ctrl+C) i wklej. Separator kolumn nie ma znaczenia.</li>
<li><strong>Wyciąg bankowy</strong> – w trybie wyciągu wklej tytuły wpłat (np. z eksportu historii rachunku). Każdy wiersz bez numeru KSeF lub identyfikatora dostanie status „Brak numeru”.</li>
<li><strong>Plik importu przelewów</strong> – przed wysłaniem paczki do banku sprawdź, czy w każdym tytule jest poprawny numer.</li>
</ul>
<p>Pojedynczy numer szybciej sprawdzisz w <a href="/">walidatorze numeru KSeF</a> na stronie głównej, który dodatkowo ułoży tytuł przelewu. Gdy nie wiesz, gdzie szukać numerów do listy, zajrzyj do artykułu <a href="/blog/gdzie-znalezc-numer-ksef-faktury/">gdzie znaleźć numer KSeF faktury</a>.</p>
<p>Dla odbiorców płatności przydatna jest też rutyna: raz w tygodniu wklej tytuły wpłat z ostatnich dni i odfiltruj w Excelu statusy inne niż „poprawny”. Szybko zobaczysz, którzy kontrahenci wciąż płacą bez numeru KSeF albo z literówką, i możesz im przypomnieć o nowych zasadach, zanim zaległości się nawarstwią.</p>
"""

BULK_FAQ = [
    ("Czy narzędzie znajdzie numer KSeF w środku dłuższego tytułu przelewu?", "Tak. W każdym wierszu szukamy ciągów pasujących do wzoru numeru KSeF lub identyfikatora zbiorczego, także otoczonych innym tekstem, np. „Zapłata 5265877635-20250826-0100001AF629-AF FV 12”. Jeśli wiersz zawiera kilka numerów, każdy zostanie sprawdzony."),
    ("Czy mogę sprawdzić numery z KSeF 1.0 (36 znaków)?", "Tak. Numer w starym, 36-znakowym formacie dostanie ostrzeżenie zamiast błędu, bo schemat FA(3) nadal go akceptuje. W raporcie CSV zobaczysz to w kolumnie Uwagi."),
]

XML_EXTRA = """
<h2 id="przyklad-xml">Przykład: co zobaczysz po wczytaniu pliku</h2>
<p>Przycisk „Przykład” wczytuje plik FA(3) z fakturą FV/123/11/2026 od firmy „Przykładowy Sprzedawca Sp. z o.o.”. Z pliku odczytujemy:</p>
<div class="table-wrap"><table>
<thead><tr><th scope="col">Dane w karcie płatności</th><th scope="col">Pole w XML</th><th scope="col">Wartość w przykładzie</th></tr></thead>
<tbody>
<tr><th scope="row">Data wystawienia</th><td class="mono">P_1</td><td>12.11.2026</td></tr>
<tr><th scope="row">Numer faktury</th><td class="mono">P_2</td><td>FV/123/11/2026</td></tr>
<tr><th scope="row">Netto i VAT (stawka 23%)</th><td class="mono">P_13_1, P_14_1</td><td>16 260,16 zł i 3 739,84 zł</td></tr>
<tr><th scope="row">Do zapłaty</th><td class="mono">P_15</td><td>20 000,00 zł</td></tr>
<tr><th scope="row">Rachunek</th><td class="mono">NrRB</td><td>60 1020 1026 0000 1234 5678 9012</td></tr>
<tr><th scope="row">Termin płatności</th><td class="mono">Termin</td><td>26.11.2026</td></tr>
<tr><th scope="row">Podzielona płatność</th><td class="mono">P_18A</td><td>1 – komunikat MPP</td></tr>
</tbody></table></div>
<p>Numer KSeF bierzemy z nazwy pliku (<code>5265877635-20250826-0100001AF629-AF.xml</code>), więc karta pokazuje gotowy komunikat <code>/VAT/3739,84/IDC/5265877635/INV/5265877635-20250826-0100001AF629-AF/TXT/FV FV/123/11/2026</code> – 89 znaków. Wystarczy skopiować rachunek, kwotę 20 000,00 zł i komunikat do formularza przelewu MPP.</p>

<h2 id="skad-plik">Skąd wziąć plik XML faktury</h2>
<ul>
<li><strong>Aplikacja Podatnika KSeF</strong> – w wykazie faktur zakupowych możesz pobrać plik XML faktury. Zapisz go pod nazwą zawierającą numer KSeF, jeśli system nie zrobił tego sam.</li>
<li><strong>Program księgowy</strong> – większość programów pobiera faktury z KSeF automatycznie i pozwala wyeksportować XML razem z numerem.</li>
<li><strong>Od sprzedawcy</strong> – kontrahent może przesłać XML mailem obok wizualizacji PDF. Wtedy numer KSeF ustal z UPO, kodu QR lub od sprzedawcy i wklej go ręcznie.</li>
</ul>
<p>Jeśli masz tylko numer KSeF bez pliku, sprawdź go w <a href="/">walidatorze numeru KSeF</a> i ułóż tytuł ręcznie. Wskazówki, gdzie szukać numeru, zebraliśmy w artykule <a href="/blog/gdzie-znalezc-numer-ksef-faktury/">gdzie znaleźć numer KSeF faktury</a>.</p>
<p class="note">Karta płatności nie zastępuje kontroli rachunku na białej liście podatników VAT. Przy fakturach powyżej 15 000 zł sprawdź rachunek dostawcy w wykazie Ministerstwa Finansów przed przelewem.</p>
"""

XML_FAQ = [
    ("Czy wizualizacja PDF wystarczy, żeby zapłacić fakturę z KSeF?", "Wystarczy, jeśli zawiera numer KSeF – zwykle jest on pod kodem QR. Plik XML jest jednak oryginałem faktury w KSeF, a PDF tylko jego obrazem. Wczytanie XML oszczędza przepisywania rachunku i kwot, a kod QR pozwala sprawdzić, czy PDF odpowiada fakturze w systemie."),
    ("Dlaczego kwota w karcie różni się od tej, którą znam z PDF?", "Najczęściej faktura ma pole DoZaplaty (np. po potrąceniu zaliczki) – wtedy pokazujemy obie kwoty. Jeśli różnica jest inna, sprawdź, czy PDF i XML dotyczą tej samej faktury, np. porównując link z kodu QR w naszym narzędziu do kodów QR."),
]

QR_EXTRA = """
<h2 id="przyklad-link">Przykład: rozkładamy link KOD I na części</h2>
<p>Dokumentacja MF podaje przykładowy link ze środowiska testowego: <code>https://qr-test.ksef.mf.gov.pl/invoice/1111111111/01-02-2026/UtQp9Gpc51y-u3xApZjIjgkpZ01js-J8KflSPW8WzIE</code>. Dekoder czyta go tak:</p>
<div class="table-wrap"><table>
<thead><tr><th scope="col">Fragment</th><th scope="col">Znaczenie</th></tr></thead>
<tbody>
<tr><th scope="row" class="mono">qr-test.ksef.mf.gov.pl</th><td>środowisko testowe MF – faktura bez skutków podatkowych. Na prawdziwej fakturze zobaczysz <code>qr.ksef.mf.gov.pl</code>.</td></tr>
<tr><th scope="row" class="mono">/invoice/</th><td>KOD I – weryfikacja faktury (KOD II ma w tym miejscu <code>/certificate/</code>)</td></tr>
<tr><th scope="row" class="mono">1111111111</th><td>NIP sprzedawcy – musi zgadzać się z NIP-em na fakturze</td></tr>
<tr><th scope="row" class="mono">01-02-2026</th><td>data wystawienia z pola P_1 w formacie DD-MM-RRRR</td></tr>
<tr><th scope="row" class="mono">UtQp9Gpc51y-…</th><td>skrót SHA-256 pliku XML w Base64URL – 43 znaki</td></tr>
</tbody></table></div>
<p>Jeśli dowolny z tych elementów nie pasuje do faktury, którą trzymasz w ręku, nie płać, dopóki nie wyjaśnisz sprawy ze sprzedawcą. Szczególnie podejrzana jest każda domena inna niż trzy oficjalne hosty MF – nawet jeśli wygląda podobnie, np. zawiera dodatkowe słowo lub inną końcówkę.</p>

<h2 id="qr-a-platnosc">Kod QR KSeF a kod QR do przelewu</h2>
<p>Na fakturze możesz spotkać dwa zupełnie różne kody. Kod QR KSeF prowadzi do strony MF i służy do weryfikacji faktury. Kod QR do płatności (standard 2D Związku Banków Polskich) wypełnia formularz przelewu w aplikacji banku. Ten drugi ma pole tytułu ograniczone do 32 znaków, więc nie zmieści 35-znakowego numeru KSeF – tytuł z numerem trzeba uzupełnić ręcznie. Gotowy tekst przygotujesz w <a href="/">walidatorze numeru KSeF</a>, a dla przelewów MPP w <a href="/przelew-mpp-numer-ksef/">generatorze komunikatu MPP</a>. Numer KSeF znajdziesz zwykle pod kodem QR – więcej o tym w artykule <a href="/blog/gdzie-znalezc-numer-ksef-faktury/">gdzie znaleźć numer KSeF faktury</a>.</p>
"""

QR_FAQ = [
    ("Czy kod QR KSeF musi być na każdej wizualizacji faktury?", "Według MF kod weryfikujący umieszcza się na wizualizacji faktury przekazywanej poza KSeF, np. jako PDF lub wydruk. Faktura offline ma dodatkowo KOD II z napisem CERTYFIKAT. Sam plik XML w KSeF kodu QR nie zawiera."),
]

JDG_EXTRA = """
<h2 id="scenariusze">Trzy typowe scenariusze</h2>
<div class="table-wrap"><table>
<thead><tr><th scope="col">Firma</th><th scope="col">Wystawianie faktur od 1.01.2027</th><th scope="col">Płatności za faktury zakupowe</th></tr></thead>
<tbody>
<tr><th scope="row">Programista na B2B, czynny VAT, faktury za ok. 8 000 zł miesięcznie</th><td>Koniec limitu 10 000 zł – faktury dla klienta tylko w KSeF</td><td>Numer KSeF w tytule przelewu do dostawców będących czynnymi podatnikami VAT</td></tr>
<tr><th scope="row">Usługi dla firm, zwolnienie z VAT</th><td>Faktury dla firm w KSeF</td><td>Numer KSeF w przelewie dobrowolny – warto go podawać, bo ułatwia rozliczenie</td></tr>
<tr><th scope="row">Sklep z kasą fiskalną, głównie konsumenci</th><td>Koniec wyjątku dla faktur z kasy – faktury dla firm w KSeF; dla konsumentów dobrowolnie</td><td>Zależnie od statusu VAT jak wyżej</td></tr>
</tbody></table></div>

<h2 id="przyklad-jdg">Przykład: pierwsza płatność w styczniu 2027 r.</h2>
<p>Pani Anna prowadzi biuro projektowe (czynny podatnik VAT). 5 stycznia 2027 r. otrzymuje przez KSeF fakturę za oprogramowanie od dostawcy, który też jest czynnym podatnikiem VAT. Faktura opiewa na 2 460 zł brutto, bez adnotacji o podzielonej płatności. Co robi?</p>
<ol class="steps">
<li>Odczytuje numer KSeF faktury w Aplikacji Podatnika lub w programie księgowym.</li>
<li>Wkleja numer do <a href="/">walidatora numeru KSeF</a> i sprawdza, że suma kontrolna się zgadza.</li>
<li>Kopiuje gotowy tytuł (numer KSeF, a po nim numer faktury) do zwykłego przelewu na 2 460 zł.</li>
<li>Jeśli w tym samym tygodniu płaci temu dostawcy jeszcze dwie faktury, może wpisać trzy numery w jednym tytule albo wygenerować <a href="/identyfikator-zbiorczy-ksef/">identyfikator zbiorczy</a>.</li>
</ol>
<p>Szczegóły zapisu w tytule przelewu opisuje artykuł <a href="/blog/jak-wpisac-numer-ksef-w-tytule-przelewu/">jak wpisać numer KSeF w tytule przelewu</a>.</p>

"""

JDG_FAQ_REPLACE = {
    "Od kiedy obowiązują kary za KSeF?": ("Czy za błędy w KSeF grożą już kary?", "Przepisy o karach (art. 106ni ustawy o VAT) są obecnie zmieniane w toku prac legislacyjnych, a ostateczny kształt i termin ich stosowania nie są jeszcze przesądzone. Sprawdzaj aktualne informacje na ksef.podatki.gov.pl. Same obowiązki – wystawianie faktur w KSeF i numer KSeF w przelewach od 1 stycznia 2027 r. – nie zależą od tych zmian."),
    "Czy przesunięcie kar oznacza przesunięcie obowiązków?": ("Czy zmiany w karach oznaczają przesunięcie obowiązków?", "Nie. Prace legislacyjne dotyczą kar. Obowiązki wystawiania faktur w KSeF i podawania numeru KSeF w przelewach od 1 stycznia 2027 r. pozostają bez zmian."),
}
JDG_FAQ = [
    ("Czy faktury dla konsumentów też muszą trafiać do KSeF?", "Nie. Ministerstwo Finansów wskazuje, że faktury na rzecz osób fizycznych nieprowadzących działalności gospodarczej mogą być wystawiane w KSeF dobrowolnie. Obowiązek dotyczy faktur dla firm."),
]

# ---- v3b: dodatkowe sekcje, by poradniki miały ok. 1000–1200 słów
IZ_EXTRA += """
<h2 id="platnosci-czesciowe">Płatności częściowe, waluta i opis</h2>
<p>Przy generowaniu identyfikatora zbiorczego obowiązkowo wskazujesz numery KSeF faktur. Ministerstwo Finansów przewiduje też trzy dane dodatkowe: kwotę płatności za każdą fakturę, kod waluty oraz opis faktur o długości do 512 znaków. Są one szczególnie przydatne, gdy płacisz tylko część należności – na przykład 50% każdej z dziesięciu faktur w ramach ugody z dostawcą. Odbiorca, który rozkoduje identyfikator w KSeF, zobaczy wtedy nie tylko listę faktur, ale też to, jaką kwotę przypisałeś do każdej z nich.</p>
<p>Nasze narzędzie tych danych nie odczyta, bo nie są zapisane w samym 35-znakowym ciągu – sprawdza wyłącznie jego budowę. Dlatego po wygenerowaniu identyfikatora zachowaj w dokumentacji płatności zestawienie faktur i kwot. W razie pytań kontrahenta szybciej wyjaśnisz, czego dotyczył przelew.</p>
<p>W jednym tytule zwykłego przelewu możesz też podać kilka identyfikatorów zbiorczych, o ile zmieszczą się w limicie pola – MF wprost dopuszcza taki wariant. W praktyce przy 140 znakach zmieszczą się trzy.</p>
"""

QR_EXTRA += """
<h2 id="krok-po-kroku-qr">Krok po kroku: weryfikacja faktury PDF przed zapłatą</h2>
<ol class="steps">
<li><strong>Odczytaj kod.</strong> Zeskanuj kod QR aparatem telefonu, ale nie otwieraj od razu strony – najpierw skopiuj link.</li>
<li><strong>Wklej link do dekodera.</strong> Narzędzie sprawdzi domenę, NIP (z sumą kontrolną), datę i długość skrótu.</li>
<li><strong>Porównaj z fakturą.</strong> NIP sprzedawcy i data wystawienia z linku muszą być takie same jak na PDF-ie.</li>
<li><strong>Otwórz stronę MF.</strong> Dopiero gdy domena to <code>qr.ksef.mf.gov.pl</code>, otwórz link – strona MF pokaże, czy faktura jest w KSeF.</li>
<li><strong>Zapłać z numerem KSeF.</strong> Numer spod kodu QR sprawdź w <a href="/">walidatorze numeru KSeF</a> i wpisz go w tytule przelewu.</li>
</ol>
<p>Sygnały ostrzegawcze, przy których warto wstrzymać płatność: domena inna niż oficjalna, NIP w linku różny od NIP-u na fakturze, numer rachunku inny niż zwykle u tego dostawcy, napis OFFLINE przy fakturze, która miała być wystawiona online, oraz presja na pilną zapłatę. Zmianę numeru rachunku zawsze potwierdź telefonicznie pod znanym Ci numerem kontrahenta, a nie tym podanym w mailu.</p>
"""

JDG_EXTRA += """
<h2 id="odbior-faktur">Odbieranie faktur zakupowych i JPK_VAT</h2>
<p>Od 1 stycznia 2027 r. faktury od kontrahentów, którzy wystawiają w KSeF, otrzymujesz przez system – nie musisz czekać na maila z PDF-em. Do odbierania potrzebujesz dostępu do KSeF: przez Aplikację Podatnika KSeF lub program księgowy. Jeśli prowadzi Cię biuro rachunkowe, zwykle to ono pobiera faktury, ale numery KSeF faktur zakupowych przydadzą się także Tobie, gdy samodzielnie płacisz przelewy.</p>
<p>Numer KSeF trafia też do ewidencji: według MF w strukturze JPK_VAT z deklaracją obowiązującej od 1 lutego 2026 r. (JPK_V7M(3) i JPK_V7K(3)) wykazuje się numer KSeF faktury – po stronie sprzedaży i zakupów. To kolejny powód, by numer był wpisany poprawnie już w momencie płatności.</p>
<h2 id="inne-sytuacje">Polecenie zapłaty i płatności za kogoś</h2>
<p>MF wskazuje, że obowiązek podania numeru KSeF dotyczy także wystawcy faktury, gdy płatność odbywa się poleceniem zapłaty, oraz podatników innych niż nabywca, którzy płacą za faktury wystawione na rzecz tego nabywcy. Obejmuje też faktury wystawione w trybie offline (niedostępność KSeF i offline24) – z wyjątkiem tych, które z powodu ogłoszonej awarii nie trafiły do systemu, oraz faktur z trybu awaryjnego.</p>
"""

MPP_EXTRA += """
<h2 id="mpp-za-kogos">Płacisz w MPP za fakturę innej firmy?</h2>
<p>Według MF obowiązek podania numeru KSeF dotyczy także podatników innych niż nabywca, którzy płacą za faktury wystawione na rzecz nabywcy – na przykład spółki z grupy regulującej zobowiązania siostrzanej firmy. Komunikat MPP budujesz wtedy tak samo: w <code>/IDC/</code> NIP wystawcy faktury, w <code>/INV/</code> numer KSeF tej faktury.</p>
"""

XML_EXTRA += """
<h2 id="korekty-zaliczki">Faktury korygujące, zaliczkowe i w walucie obcej</h2>
<p>Plik FA(3) faktury korygującej zawiera numer KSeF faktury pierwotnej (pole <code>NrKSeFFaKorygowanej</code>), a faktura rozliczająca zaliczki – numery KSeF faktur zaliczkowych. MF przypomina, że podawanie tych numerów w treści faktury zapewnia ciągłość transakcji. Nie myl ich jednak z numerem KSeF samego dokumentu, który właśnie wczytujesz – ten nadaje system przy przyjęciu korekty lub faktury końcowej i, jak przy każdej fakturze, nie ma go w treści pliku XML.</p>
<p>Przy fakturze w walucie obcej kwotę VAT w złotych znajdziesz w polach <code>P_14_xW</code> (np. <code>P_14_1W</code> dla stawki 23%). Ma to znaczenie przy MPP, bo podzieloną płatność realizuje się w złotych, a w polu <code>/VAT/</code> podaje się kwotę podatku w PLN. Zanim zapłacisz taką fakturę, porównaj kwoty z karty z wizualizacją faktury i ustal z księgową, którą kwotę przelać.</p>
"""

BULK_EXTRA += """
<h2 id="jak-czytac-raport">Jak czytać kolumnę „Data” w raporcie</h2>
<p>Data w raporcie to data przyjęcia faktury do KSeF zapisana w numerze, a nie data wystawienia. Mimo to pozwala wychwycić pomyłki: jeśli płacisz faktury za październik, a któryś numer ma datę sprzed pół roku, prawdopodobnie ktoś skopiował numer innej faktury tego samego dostawcy. Podobnie kolumna NIP pokazuje, czyj to numer – w paczce przelewów do jednego dostawcy wszystkie numery powinny zaczynać się od jego NIP-u. Posortuj raport w Excelu po kolumnie NIP, a odstające wiersze od razu rzucą się w oczy.</p>
"""

QR_EXTRA += """
<p>Jeśli sam wystawiasz faktury poza programem zintegrowanym z KSeF i tworzysz wizualizacje ręcznie, generator powyżej przygotuje KOD I z Twojego pliku XML. Pamiętaj, aby wczytać dokładnie ten plik, który został przesłany do KSeF – każda zmiana, nawet dodanie spacji, zmieni skrót SHA-256 i link przestanie pasować do faktury w systemie. Pod kodem umieść numer KSeF faktury, a jeśli faktura nie została jeszcze przyjęta przez KSeF – napis OFFLINE.</p>
"""

JDG_EXTRA += """
<p>Wszystkie te sytuacje sprowadzają się do jednej zasady: kto płaci przelewem za fakturę z KSeF między czynnymi podatnikami VAT, ten wpisuje jej numer KSeF. Jeżeli masz wątpliwości, czy Twoja sytuacja mieści się w obowiązku, porozmawiaj z księgową – a na wszelki wypadek podawaj numer zawsze, bo dobrowolne podanie niczym nie grozi i ułatwia kontrahentowi rozliczenie.</p>
"""

XML_EXTRA += """
<h2 id="kontrola-przed-przelewem">Szybka kontrola przed przelewem</h2>
<ul>
<li>Czy nazwa i NIP sprzedawcy zgadzają się z dostawcą, którego się spodziewasz?</li>
<li>Czy numer rachunku jest taki sam jak w poprzednich fakturach tego dostawcy?</li>
<li>Czy numer KSeF zaczyna się od NIP-u sprzedawcy i przechodzi kontrolę sumy?</li>
<li>Czy termin płatności nie minął i czy kwota uwzględnia zaliczki lub korekty?</li>
</ul>
"""

BULK_EXTRA += """
<p>Na koniec warto zachować raport CSV razem z potwierdzeniami przelewów. Gdy kontrahent zapyta, której faktury dotyczyła wpłata, w kilka sekund znajdziesz właściwy numer KSeF, datę jego nadania i status kontroli z dnia płatności – bez ponownego przeszukiwania programu księgowego czy historii rachunku.</p>
"""
