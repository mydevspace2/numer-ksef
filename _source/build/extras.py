# -*- coding: utf-8 -*-
# Dodatkowe sekcje poradników (doklejane na końcu treści stron)

IZ_EXTRA = """
<h2>Identyfikator zbiorczy w tytule przelewu – przykłady</h2>
<div class="table-wrap"><table>
<thead><tr><th scope="col">Sytuacja</th><th scope="col">Co wpisać</th></tr></thead>
<tbody>
<tr><th scope="row">Zwykły przelew za 12 faktur od jednego dostawcy</th><td class="mono">1111111111-IZ202607-65ED02180000-E7</td></tr>
<tr><th scope="row">To samo, ale w MPP</th><td class="mono">/VAT/4600,00/IDC/1111111111/INV/1111111111-IZ202607-65ED02180000-E7</td></tr>
<tr><th scope="row">Dwie faktury – bez generowania identyfikatora</th><td>dwa numery KSeF oddzielone przecinkiem (zmieszczą się w 140 znakach)</td></tr>
<tr><th scope="row">Faktury od dwóch różnych sprzedawców</th><td>dwa osobne przelewy – identyfikator obejmuje tylko jednego sprzedawcę</td></tr>
</tbody></table></div>

<h2>Identyfikator zbiorczy czy kilka numerów KSeF?</h2>
<p>Przy dwóch lub trzech fakturach najprościej wpisać ich numery KSeF – w typowym polu tytułu o długości 140 znaków zmieszczą się trzy numery. Identyfikator zbiorczy opłaca się, gdy faktur jest więcej albo gdy płacisz w MPP: w komunikacie split payment pole <code>/INV/</code> mieści tylko 35 znaków, czyli dokładnie jeden numer KSeF lub jeden identyfikator zbiorczy. Wtedy identyfikator to jedyny sposób, żeby jednym przelewem MPP zapłacić za kilka faktur z KSeF.</p>
<p>Pamiętaj, że kwota przelewu powinna odpowiadać fakturom objętym identyfikatorem. Jeśli część faktur płacisz później, wygeneruj nowy identyfikator dla właściwego zestawu – jedna faktura może występować w wielu identyfikatorach (do 132 w danym kontekście), więc nie musisz się obawiać, że raz użyta faktura „przepadnie”.</p>

<h2>Jesteś odbiorcą płatności?</h2>
<p>Jeśli kontrahent zapłacił z identyfikatorem zbiorczym, sprawdź go tutaj, a następnie odczytaj w KSeF listę objętych nim faktur i rozlicz je w programie księgowym. Wpłaty z wielu tytułów naraz przejrzysz w <a href="/sprawdz-wiele-numerow-ksef/">masowym walidatorze</a> w trybie wyciągu bankowego.</p>
"""

QR_EXTRA = """
<h2>Jak sprawdzić fakturę w praktyce</h2>
<div class="table-wrap"><table>
<thead><tr><th scope="col">Sytuacja</th><th scope="col">Co zrobić</th></tr></thead>
<tbody>
<tr><th scope="row">Dostajesz PDF faktury mailem</th><td>Zeskanuj kod QR telefonem lub skopiuj link, wklej go w dekoderze powyżej i porównaj NIP oraz datę z treścią faktury.</td></tr>
<tr><th scope="row">Dostajesz fakturę papierową</th><td>Zrób zdjęcie kodu (w przeglądarkach z obsługą rozpoznawania kodów odczytamy je bezpośrednio) albo zeskanuj aparatem i wklej link.</td></tr>
<tr><th scope="row">Masz też plik XML</th><td>Wczytaj go w generatorze – dekoder porówna skrót z linku ze skrótem pliku. Zgodność oznacza, że PDF i XML opisują tę samą fakturę.</td></tr>
<tr><th scope="row">Pod kodem jest napis OFFLINE</th><td>Faktura nie miała jeszcze numeru KSeF. Sprawdź także KOD II (CERTYFIKAT) i upewnij się później, że faktura trafiła do KSeF.</td></tr>
<tr><th scope="row">Link prowadzi do innej domeny</th><td>Nie otwieraj go. Skontaktuj się z wystawcą innym kanałem niż mail, z którego przyszła faktura.</td></tr>
</tbody></table></div>

<h2>Dlaczego fałszywe kody QR to realne zagrożenie</h2>
<p>Kod QR ukrywa adres – człowiek nie widzi go, dopóki nie zeskanuje kodu. To ułatwia oszustwa typu „quishing”: podrobiona faktura z kodem prowadzącym do strony, która wygląda jak serwis Ministerstwa Finansów, a w rzeczywistości wyłudza dane logowania do banku albo do KSeF. Prawdziwa weryfikacja KOD I nie wymaga logowania ani podawania żadnych danych. Jeśli strona otwarta z kodu prosi o login, hasło, kod SMS albo dane karty – to oszustwo.</p>
<p>Nasz dekoder akceptuje wyłącznie trzy domeny MF i dodatkowo ostrzega przed adresami, które zawierają słowa „ksef” czy „mf-gov”, ale prowadzą gdzie indziej, a także przed linkami z loginem, portem lub nietypowymi parametrami. Kontrola działa lokalnie – link nie jest nigdzie wysyłany ani otwierany.</p>
"""

JDG_EXTRA = """
<h2>Lista kontrolna na grudzień 2026 r.</h2>
<ul>
<li><strong>Dostęp do KSeF.</strong> Sprawdź, czy możesz zalogować się do Aplikacji Podatnika KSeF lub czy Twój program do faktur jest połączony z KSeF.</li>
<li><strong>Uprawnienia.</strong> Jeśli faktury wystawia księgowa lub pracownik, nadaj im uprawnienia w KSeF.</li>
<li><strong>Dane kontrahentów.</strong> Uzupełnij NIP-y klientów – faktura w KSeF dla firmy wymaga poprawnego NIP nabywcy.</li>
<li><strong>Kasa fiskalna.</strong> Jeśli wystawiasz faktury do paragonów, ustal, jak od stycznia wystawisz je w KSeF.</li>
<li><strong>Przelewy.</strong> Sprawdź w swoim banku, gdzie w formularzu przelewu i przelewu MPP wpisuje się numer KSeF, i przetestuj jeden przelew.</li>
<li><strong>Tryb awaryjny i offline.</strong> Dowiedz się, jak wystawić fakturę, gdy KSeF lub internet nie działa – takie faktury trzeba później przesłać do systemu.</li>
</ul>
<p>Tę stronę zaktualizujemy po zakończeniu prac legislacyjnych nad przepisami o karach. Data „stan prawny na” u góry strony zawsze pokazuje, kiedy ostatnio sprawdzaliśmy przepisy.</p>
"""

MPP_EXTRA = """
<h2>Najczęstsze błędy w komunikacie MPP</h2>
<ul>
<li><strong>Kropka zamiast przecinka w kwocie VAT</strong> (<code>/VAT/230.00</code>) – bank może odrzucić przelew. Poprawnie: <code>/VAT/230,00</code>.</li>
<li><strong>Spacja po słowie kodowym</strong> (<code>/VAT/ 230,00</code>) – spacje między słowem kodowym a wartością są niedozwolone.</li>
<li><strong>Zła kolejność</strong> – zawsze VAT, IDC, INV, a na końcu opcjonalnie TXT. Każde słowo kodowe tylko raz.</li>
<li><strong>NIP nabywcy zamiast NIP sprzedawcy</strong> w <code>/IDC/</code> – wpisujesz identyfikator dostawcy, czyli wystawcy faktury (wyjątek: przekazanie własne).</li>
<li><strong>Numer faktury i numer KSeF razem w /INV/</strong> – nie zmieszczą się. Numer KSeF w /INV/, numer faktury w /TXT/.</li>
<li><strong>Literówka w numerze KSeF</strong> – generator liczy sumę kontrolną CRC-8, więc zablokuje komunikat z błędnym numerem.</li>
</ul>
"""

XML_EXTRA = """
<h2>Kilka faktur od jednego dostawcy</h2>
<p>Wczytaj wszystkie pliki naraz – każda faktura dostanie własną kartę z danymi do przelewu. Jeśli chcesz zapłacić je jednym przelewem, wpisz w tytule do trzech numerów KSeF (zrobisz to w <a href="/">generatorze tytułu</a>) albo wygeneruj w KSeF <a href="/identyfikator-zbiorczy-ksef/">identyfikator zbiorczy</a>. W przelewie MPP jedynym sposobem na zapłatę kilku faktur z KSeF jest identyfikator zbiorczy, bo pole <code>/INV/</code> mieści jeden numer.</p>

<h2>Bezpieczeństwo i prywatność</h2>
<p>Faktura to dane handlowe: kontrahenci, ceny, numery rachunków. Dlatego narzędzie nie wysyła pliku nigdzie – parsuje go przeglądarka za pomocą wbudowanego DOMParsera, z obsługą przestrzeni nazw FA(3). Możesz to sprawdzić, odłączając internet po załadowaniu strony: narzędzie dalej działa. Nie zapisujemy też niczego w pamięci przeglądarki; po odświeżeniu strony dane znikają.</p>
<p>Przed zapłatą zawsze porównaj numer rachunku z wcześniejszymi płatnościami dla tego dostawcy. Zmiana rachunku „na nowy” w fakturze to klasyczny sposób wyłudzeń – w razie wątpliwości potwierdź rachunek telefonicznie.</p>
"""

BULK_EXTRA = """
<h2>Typowe błędy wykrywane w listach</h2>
<div class="table-wrap"><table>
<thead><tr><th scope="col">Komunikat</th><th scope="col">Najczęstsza przyczyna</th></tr></thead>
<tbody>
<tr><th scope="row">Suma kontrolna się nie zgadza</th><td>Literówka przy przepisywaniu, zamieniona kolejność znaków albo numer z instrukcji banku (przykłady bankowe nie są prawdziwymi numerami)</td></tr>
<tr><th scope="row">Znak „O” zamiast zera / „I” zamiast jedynki</th><td>Ręczne przepisywanie z wydruku lub PDF-a; w numerze KSeF nie ma liter spoza A–F</td></tr>
<tr><th scope="row">Zła długość</th><td>Ucięty numer przy kopiowaniu z wąskiej kolumny w Excelu albo dopisana kropka czy przecinek na końcu</td></tr>
<tr><th scope="row">Pierwsze 10 cyfr to nie NIP</th><td>Pomylone cyfry na początku numeru</td></tr>
<tr><th scope="row">Data z przyszłości</th><td>Pomylony rok lub miesiąc w części z datą przyjęcia do KSeF</td></tr>
</tbody></table></div>
<p>Spacje, długie myślniki z Worda i małe litery poprawiamy automatycznie, więc nie zgłaszamy ich jako błędów – ale informujemy o poprawce w kolumnie uwag.</p>
"""

IZ_EXTRA += """
<h2>Bezpieczeństwo danych</h2>
<p>Walidator działa w całości w Twojej przeglądarce: identyfikator nie jest wysyłany na żaden serwer ani zapisywany. Możesz bezpiecznie sprawdzać identyfikatory klientów i dostawców, także na telefonie, bez logowania i bez instalowania aplikacji.</p>
"""
MPP_EXTRA += """
<p>Jeśli płacisz wiele faktur w MPP, przygotuj numery KSeF w <a href="/sprawdz-wiele-numerow-ksef/">masowym walidatorze</a>, a dane z pliku faktury przeniesiesz do generatora jednym kliknięciem z narzędzia <a href="/przelew-z-faktury-xml-ksef/">przelew z faktury XML</a>.</p>
"""
BULK_EXTRA += """
<h2>Prywatność dużych plików</h2>
<p>Rejestry faktur i wyciągi bankowe zawierają wrażliwe dane: nazwy kontrahentów, kwoty, numery rachunków. Dlatego cała analiza odbywa się lokalnie – plik nie opuszcza Twojego komputera, a po zamknięciu karty nie zostaje po nim ślad. Nie potrzebujesz konta ani instalacji, a narzędzie działa także bez internetu po załadowaniu strony. To ważne dla biur rachunkowych, które pracują na danych wielu klientów i muszą dbać o tajemnicę zawodową.</p>
"""
