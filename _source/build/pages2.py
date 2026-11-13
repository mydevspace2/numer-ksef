# -*- coding: utf-8 -*-
from sources import *

# ---------------------------------------------------------------- XML
XMLP = dict(
    title="Przelew z faktury XML KSeF – dane do przelewu z pliku FA(3)",
    desc="Wczytaj fakturę XML z KSeF (FA3) i skopiuj dane do przelewu: odbiorca, rachunek, kwota, termin, tytuł z numerem KSeF i komunikat MPP. Bez wysyłania pliku.",
    app_name="Faktura XML z KSeF – dane do przelewu",
    h1="Faktura XML z KSeF → gotowe dane do przelewu (z numerem KSeF i MPP)",
    intro="Upuść plik XML faktury pobrany z KSeF. Odczytamy sprzedawcę, NIP, numer rachunku, kwotę i termin płatności, a potem przygotujemy tytuł przelewu z numerem KSeF i – jeśli faktura ma adnotację MPP – gotowy komunikat split payment.",
    trail=[("Strona główna", "/"), ("Przelew z faktury XML KSeF", "/przelew-z-faktury-xml-ksef/")],
    scripts=["page-xml.js"],
    tool="""
<section class="tool" aria-labelledby="h-xml">
  <h2 id="h-xml">Wczytaj fakturę XML (FA3)</h2>
  <label class="file" id="x-drop" for="x-file"><strong>Upuść plik .xml faktury lub kliknij, aby wybrać</strong><br><span class="hint">Możesz wybrać kilka plików. Plik czyta tylko Twoja przeglądarka.</span><input type="file" id="x-file" accept=".xml,application/xml,text/xml" multiple></label>
  <div class="field mt14"><label for="x-ksef">Numer KSeF faktury <span class="hint">(jeśli nie ma go w nazwie pliku)</span></label>
  <input id="x-ksef" class="mono" type="text" autocomplete="off" autocapitalize="characters" spellcheck="false" placeholder="5265877635-20250826-0100001AF629-AF" aria-describedby="x-ksef-msg"><p class="hint" id="x-ksef-msg" aria-live="polite"></p></div>
  <div class="btns"><button type="button" class="btn ghost" id="x-ex">Przykład: faktura MPP</button><a class="btn ghost" href="/assets/przyklad-fa3.xml" download>Pobierz przykładowy XML</a></div>
  <p class="privacy">🔒 Dane nie opuszczają Twojej przeglądarki.</p>
</section>
<div id="x-cards" aria-live="polite"></div>""",
    content="""
<h2>Jak zapłacić fakturę z KSeF w trzy minuty</h2>
<p>Od 1 lutego 2026 r. faktury w KSeF mają strukturę FA(3) – MF pisze, że <q>struktura logiczna FA(3) zastąpiła strukturę logiczną FA(2)</q>. Plik XML to dokument dla programów, nie dla ludzi: numer rachunku, kwota i termin płatności są ukryte w elementach o nazwach takich jak <code>NrRB</code>, <code>P_15</code> czy <code>Termin</code>. Darmowych przeglądarek faktur XML jest dużo, ale zwykle kończą się na wydruku. To narzędzie robi jedną rzecz: zamienia fakturę w gotowe dane do przelewu z przyciskami „Kopiuj”.</p>
<ol class="steps">
<li><strong>Pobierz XML</strong> z Aplikacji Podatnika KSeF lub z programu księgowego. Pliki eksportowane z KSeF mają zwykle numer KSeF w nazwie.</li>
<li><strong>Upuść plik</strong> w polu powyżej. Odczyt odbywa się lokalnie (DOMParser w przeglądarce).</li>
<li><strong>Sprawdź numer KSeF.</strong> Weźmiemy go z nazwy pliku albo wpisz go ręcznie – w obu przypadkach sprawdzimy sumę kontrolną.</li>
<li><strong>Kopiuj i płać:</strong> odbiorca, rachunek, kwota, tytuł, a przy fakturze z adnotacją MPP – komunikat <code>/VAT/…/IDC/…/INV/…</code>.</li>
</ol>

<h2>Skąd bierzemy dane – pola FA(3)</h2>
<div class="table-wrap"><table>
<thead><tr><th scope="col">Dane do przelewu</th><th scope="col">Element XML (FA3)</th><th scope="col">Uwagi</th></tr></thead>
<tbody>
<tr><th scope="row">Odbiorca i NIP</th><td><code>Podmiot1/DaneIdentyfikacyjne/Nazwa</code>, <code>NIP</code></td><td>NIP sprawdzamy cyfrą kontrolną</td></tr>
<tr><th scope="row">Numer rachunku</th><td><code>Platnosc/RachunekBankowy/NrRB</code></td><td>10–34 znaki; polski NRB/IBAN sprawdzamy sumą kontrolną; osobno rachunek faktora</td></tr>
<tr><th scope="row">Kwota do zapłaty</th><td><code>Rozliczenie/DoZaplaty</code>, a gdy go brak – <code>P_15</code></td><td>P_15 to należność ogółem</td></tr>
<tr><th scope="row">Kwota VAT</th><td>suma <code>P_14_1</code>…<code>P_14_5</code> (w walucie obcej: <code>P_14_xW</code> w PLN)</td><td>potrzebna do /VAT/ w MPP</td></tr>
<tr><th scope="row">Termin płatności</th><td><code>Platnosc/TerminPlatnosci/Termin</code></td><td>lub opis terminu (np. 14 dni od doręczenia)</td></tr>
<tr><th scope="row">Forma płatności</th><td><code>FormaPlatnosci</code></td><td>1 gotówka, 2 karta, 3 bon, 4 czek, 5 kredyt, 6 przelew, 7 mobilna</td></tr>
<tr><th scope="row">Split payment</th><td><code>Adnotacje/P_18A</code></td><td>1 = „mechanizm podzielonej płatności”</td></tr>
<tr><th scope="row">Numer faktury</th><td><code>P_2</code></td><td>trafia do tytułu lub do /TXT/</td></tr>
</tbody></table></div>

<h2>Dlaczego numeru KSeF nie ma w pliku XML</h2>
<p>To najczęstsze zaskoczenie. Ministerstwo Finansów wyjaśnia, że numer KSeF <q>zwracany jest w UPO … i sam w sobie nie stanowi elementu pliku xml</q>. Nadaje go system dopiero po przyjęciu faktury. Dlatego numer KSeF znajdziesz:</p>
<ul>
<li>w nazwie pliku pobranego z KSeF (narzędzie odczyta go automatycznie),</li>
<li>w UPO (Urzędowym Poświadczeniu Odbioru),</li>
<li>w Aplikacji Podatnika KSeF lub w programie księgowym.</li>
</ul>
<p>Wyjątek to faktura korygująca: zawiera numer KSeF faktury korygowanej (<code>NrKSeFFaKorygowanej</code>), ale nie własny.</p>

<h2>Tytuł przelewu i komunikat MPP</h2>
<p>Dla zwykłego przelewu przygotujemy tytuł: najpierw numer KSeF, a jeśli zostanie miejsce – numer faktury z pola P_2, w limicie 140 znaków. Gdy faktura ma adnotację <code>P_18A = 1</code> („mechanizm podzielonej płatności”), pokażemy komunikat MPP: kwota VAT z przecinkiem, NIP sprzedawcy w <code>/IDC/</code>, numer KSeF w <code>/INV/</code> i numer faktury w <code>/TXT/</code> (do 33 znaków). Komunikat możesz poprawić w <a href="/przelew-mpp-numer-ksef/">generatorze MPP</a> – dane przeniesiemy jednym kliknięciem.</p>

<h2>Na co uważać</h2>
<ul>
<li><strong>Rachunek z faktury a biała lista.</strong> Przy płatnościach powyżej 15 000 zł sprawdź rachunek w wykazie podatników VAT (białej liście). To narzędzie tego nie robi – wymagałoby wysłania danych na serwer.</li>
<li><strong>Faktura w walucie obcej.</strong> Pokażemy kwotę w walucie faktury, a do MPP weźmiemy VAT w złotych z pól <code>P_14_xW</code>.</li>
<li><strong>Starsze faktury FA(2).</strong> Też je odczytamy (po nazwach elementów), ale oznaczymy ostrzeżeniem.</li>
<li><strong>Faktura opłacona.</strong> Jeśli w XML jest <code>Zaplacono = 1</code>, ostrzeżemy, żeby nie zapłacić drugi raz.</li>
</ul>
""",
    faq=[
        ("Czy plik faktury jest wysyłany na serwer?", "Nie. Plik XML czyta tylko Twoja przeglądarka. Strona nie ma serwera, który mógłby go odebrać."),
        ("Dlaczego narzędzie nie widzi numeru KSeF?", "Bo numeru KSeF nie ma w pliku XML – system nadaje go po przyjęciu faktury i podaje w UPO. Odczytamy go z nazwy pliku z KSeF albo wpisz go ręcznie."),
        ("Jakie pliki są obsługiwane?", "Faktury XML w strukturze FA(3) (przestrzeń nazw http://crd.gov.pl/wzor/2025/06/25/13775/). Starsze FA(2) odczytamy z ostrzeżeniem. Nie obsługujemy PDF ani UPO."),
        ("Skąd wiadomo, że trzeba zapłacić w MPP?", "Z adnotacji P_18A = 1 („mechanizm podzielonej płatności”). Wtedy pokażemy gotowy komunikat /VAT/ /IDC/ /INV/ /TXT/."),
        ("Którą kwotę zapłacić: P_15 czy DoZaplaty?", "Jeśli faktura ma sekcję Rozliczenie z polem DoZaplaty (kwota po potrąceniach i obciążeniach), bierzemy ją. W przeciwnym razie należność ogółem z P_15."),
        ("Czy mogę wczytać kilka faktur naraz?", "Tak, wybierz kilka plików – dla każdego powstanie osobna karta płatności."),
    ],
    sources=[MF_FA3, XSD, MF_NUM, MBANK_SPEC],
)

# ---------------------------------------------------------------- QR
QRP = dict(
    title="Kod QR KSeF – generator KOD I i sprawdzanie linku weryfikacyjnego",
    desc="Wygeneruj KOD I KSeF z pliku XML (SHA-256 Base64URL, NIP, data) i sprawdź link z kodu QR na fakturze. Ochrona przed fałszywymi domenami. Bez wysyłania pliku.",
    app_name="Kod QR KSeF – generator KOD I i dekoder linków",
    h1="Kod QR KSeF – odczytaj link weryfikacyjny i sprawdź, czy faktura nie jest podróbką",
    intro="Wklej link z kodu QR na fakturze – sprawdzimy, czy prowadzi do prawdziwej domeny Ministerstwa Finansów i czy jego dane mają sens. Masz plik XML? Wygenerujemy KOD I i obraz QR prosto w przeglądarce.",
    trail=[("Strona główna", "/"), ("Kod QR KSeF", "/kod-qr-ksef/")],
    scripts=["qr.js", "page-qr.js"],
    tool="""
<section class="tool" aria-labelledby="h-dec">
  <h2 id="h-dec">Sprawdź link z kodu QR</h2>
  <div class="field"><label for="d-in">Link z kodu QR na fakturze</label>
  <input id="d-in" class="mono" type="url" autocomplete="off" spellcheck="false" placeholder="https://qr.ksef.mf.gov.pl/invoice/…"></div>
  <div id="d-scan" class="field" hidden><label for="d-img">…albo zrób zdjęcie kodu QR / wybierz obraz</label><input id="d-img" type="file" accept="image/*" capture="environment"></div>
  <div class="btns"><button type="button" class="btn" id="d-check">Sprawdź link</button><button type="button" class="btn ghost" id="d-ex">Przykład MF</button><button type="button" class="btn ghost" id="d-ex-bad">Przykład fałszywego linku</button></div>
  <div id="d-res" class="status" role="status" aria-live="polite"></div>
</section>
<section class="tool" aria-labelledby="h-gen">
  <h2 id="h-gen">Generator KOD I z pliku XML</h2>
  <label class="file" id="g-drop" for="g-file"><strong>Upuść plik XML faktury</strong><br><span class="hint">Skrót SHA-256 liczymy z oryginalnych bajtów pliku (WebCrypto).</span><input type="file" id="g-file" accept=".xml,application/xml,text/xml"></label>
  <p class="hint mt8" id="g-hash" aria-live="polite"></p>
  <div class="grid2 mt10">
    <div class="field"><label for="g-nip">NIP sprzedawcy</label><input id="g-nip" type="text" inputmode="numeric" autocomplete="off"></div>
    <div class="field"><label for="g-date">Data wystawienia (P_1)</label><input id="g-date" type="date"></div>
    <div class="field"><label for="g-ksef">Numer KSeF <span class="hint">(etykieta; puste = OFFLINE)</span></label><input id="g-ksef" class="mono" type="text" autocomplete="off" spellcheck="false" autocapitalize="characters"></div>
    <div class="field"><label for="g-env">Środowisko</label><select id="g-env"><option value="PROD">Produkcyjne – qr.ksef.mf.gov.pl</option><option value="TE">Testowe – qr-test.ksef.mf.gov.pl</option><option value="DEMO">Demo – qr-demo.ksef.mf.gov.pl</option></select></div>
  </div>
  <div class="btns"><button type="button" class="btn ghost" id="g-ex">Przykład: wczytaj przykładowy XML</button></div>
  <div id="g-stat" class="status" role="status" aria-live="polite"></div>
  <div id="g-out" hidden>
    <p class="label" id="g-link-l">Link KOD I</p>
    <p class="out" id="g-link" aria-labelledby="g-link-l"></p>
    <div class="out-row"><button type="button" class="btn small" data-copy="g-link">Kopiuj link</button><button type="button" class="btn ghost small" id="g-dl">Pobierz QR (SVG)</button></div>
    <div class="qrbox"><div id="g-qr"></div><div class="qrlabel" id="g-label"></div></div>
  </div>
  <p class="privacy">🔒 Dane nie opuszczają Twojej przeglądarki. Kod QR rysuje wbudowany koder – bez zewnętrznych bibliotek.</p>
</section>""",
    content="""
<h2>Po co jest kod QR na fakturze KSeF</h2>
<p>Faktura z KSeF przekazana poza systemem – w PDF, na papierze, mailem – ma kod QR, który pozwala każdemu sprawdzić, czy faktura naprawdę jest w KSeF i czy nikt jej nie zmienił. Według MF kod zawiera <q>adres zasobu …, datę wystawienia faktury … z pola P_1, identyfikator NIP sprzedawcy, wyróżnik faktury</q>. Wyróżnik to skrót SHA-256 pliku XML – zmiana choćby jednego znaku w fakturze daje zupełnie inny skrót.</p>

<h2>Budowa linku KOD I</h2>
<p>Dokumentacja KSeF 2.0 opisuje KOD I jako adres złożony z <q>daty wystawienia faktury (pole P_1) w formacie DD-MM-RRRR, NIP-u sprzedawcy, skrótu pliku faktury obliczonego algorytmem SHA-256 … w formacie Base64URL</q>. Kolejność w ścieżce: <code>/invoice/{NIP}/{DD-MM-RRRR}/{skrót}</code>. Oficjalny przykład:</p>
<blockquote class="mono">https://qr-test.ksef.mf.gov.pl/invoice/1111111111/01-02-2026/UtQp9Gpc51y-u3xApZjIjgkpZ01js-J8KflSPW8WzIE</blockquote>
<div class="table-wrap"><table>
<thead><tr><th scope="col">Środowisko</th><th scope="col">Domena</th><th scope="col">Skutki podatkowe</th></tr></thead>
<tbody>
<tr><th scope="row">Produkcyjne</th><td class="mono">https://qr.ksef.mf.gov.pl</td><td>tak</td></tr>
<tr><th scope="row">Testowe (TE)</th><td class="mono">https://qr-test.ksef.mf.gov.pl</td><td>nie</td></tr>
<tr><th scope="row">Demo</th><td class="mono">https://qr-demo.ksef.mf.gov.pl</td><td>nie</td></tr>
</tbody></table></div>
<p>Skrót ma 43 znaki Base64URL bez znaków „=” (32 bajty SHA-256). Pod kodem drukuje się numer KSeF, a jeśli faktury jeszcze nie przyjęto do systemu – napis <strong>OFFLINE</strong>. Kod musi być zgodny z normą ISO/IEC 18004:2024; nasz generator używa poziomu korekcji błędów M.</p>

<h2>Jak rozpoznać fałszywy kod QR</h2>
<ol class="steps">
<li><strong>Sprawdź domenę.</strong> Prawdziwy link zaczyna się dokładnie od <code>https://qr.ksef.mf.gov.pl/</code> (lub qr-test / qr-demo). Adresy typu „qr-ksef-mf.pl”, „ksef-weryfikacja.com” albo „qr.ksef.mf.gov.pl.cos.tam” to podróbki – nasz dekoder oznaczy je na czerwono.</li>
<li><strong>Porównaj dane.</strong> NIP i data w linku muszą zgadzać się z fakturą, którą trzymasz w ręku.</li>
<li><strong>Porównaj skrót.</strong> Wczytaj plik XML w generatorze – dekoder pokaże, czy skrót z linku pasuje do pliku.</li>
<li><strong>Otwórz link dopiero na końcu.</strong> Strona MF potwierdzi, czy faktura jest w KSeF. Nigdy nie podawaj na stronie z kodu QR loginu, hasła ani danych karty.</li>
</ol>

<h2>KOD II (CERTYFIKAT) – tylko objaśniamy</h2>
<p>Faktury wystawione offline mają drugi kod z napisem <strong>CERTYFIKAT</strong>. KOD II potwierdza tożsamość wystawcy i ma postać <code>/certificate/{typ kontekstu}/{identyfikator}/{NIP sprzedawcy}/{nr certyfikatu}/{skrót}/{podpis}</code>. Podpis tworzy się kluczem prywatnym certyfikatu KSeF (RSASSA-PSS z SHA-256 albo ECDSA P-256). Dlatego nie generujemy KOD II – wymagałoby to Twojego klucza prywatnego, którego nigdy nie należy wpisywać na żadnej stronie. Dekoder rozpozna KOD II i rozłoży go na części, a podpis weryfikuje serwis MF po otwarciu linku.</p>

<h2>Ważne przy generowaniu KOD I</h2>
<ul>
<li>Skrót liczymy z <strong>oryginalnych bajtów</strong> pliku. Nie otwieraj i nie zapisuj XML-a w edytorze przed generowaniem – zmiana kodowania, znaku BOM czy końców linii zmienia skrót.</li>
<li>Datę bierzemy z pola P_1 (data wystawienia), a nie z daty przyjęcia do KSeF.</li>
<li>Kod QR do płatności (standard ZBP) to coś innego – nie zmieści numeru KSeF, bo jego tytuł ma maks. 32 znaki.</li>
</ul>
""",
    faq=[
        ("Jak sprawdzić kod QR na fakturze KSeF?", "Zeskanuj go telefonem, ale zanim otworzysz link, wklej go tutaj. Sprawdzimy domenę (musi być qr.ksef.mf.gov.pl), NIP, datę i format skrótu. Potem otwórz link – strona MF potwierdzi fakturę."),
        ("Jaka jest prawdziwa domena kodów QR KSeF?", "https://qr.ksef.mf.gov.pl dla faktur produkcyjnych oraz qr-test.ksef.mf.gov.pl i qr-demo.ksef.mf.gov.pl dla środowisk testowych bez skutków podatkowych."),
        ("Co oznacza napis OFFLINE pod kodem QR?", "Faktura nie miała jeszcze numeru KSeF, gdy nadawano kod (np. wystawiona w trybie offline). Taka faktura ma też KOD II z napisem CERTYFIKAT."),
        ("Czy mogę wygenerować KOD II w tym narzędziu?", "Nie. KOD II wymaga podpisu kluczem prywatnym certyfikatu KSeF. Nigdy nie wpisuj klucza prywatnego na stronach internetowych. Dekoder pokaże tylko budowę KOD II."),
        ("Dlaczego mój skrót różni się od tego w kodzie?", "Plik XML różni się choćby jednym bajtem od faktury w KSeF – np. został zapisany ponownie w edytorze. Pobierz oryginał z KSeF."),
        ("Czy plik XML jest wysyłany na serwer?", "Nie. Skrót SHA-256 liczy Twoja przeglądarka (WebCrypto), a kod QR rysuje wbudowany koder bez zewnętrznych bibliotek."),
    ],
    sources=[QR_DOC, MF_QR, XSD, ZBP],
)

# ---------------------------------------------------------------- JDG
JDG = dict(
    title="KSeF od 2027 dla JDG – czy mnie dotyczy? Test w 30 sekund",
    desc="Co zmienia się w Twojej JDG 1 stycznia 2027 r.: koniec limitu 10 000 zł, faktury z kasy, numer KSeF w przelewach i MPP. Stan prawny na 13.11.2026.",
    app_name="Test: czy KSeF od 2027 dotyczy mojej JDG",
    h1="KSeF od 1 stycznia 2027 – czy dotyczy Twojej JDG? Sprawdź w 30 sekund",
    intro="Odpowiedz na kilka pytań, a pokażemy listę zmian z datami: wystawianie faktur w KSeF, odbieranie faktur, numer KSeF w przelewach i MPP. Pokazujemy też, że przepisy o karach są wciąż zmieniane.",
    trail=[("Strona główna", "/"), ("KSeF od 2027 dla JDG", "/ksef-od-2027-jdg/")],
    scripts=["page-jdg.js"],
    tool="""
<section class="tool" aria-labelledby="h-jdg">
  <h2 id="h-jdg">Czy KSeF mnie dotyczy?</h2>
  <form id="j-form" novalidate>
    <fieldset><legend>1. Czy wystawiasz faktury innym firmom (B2B)?</legend><div class="radios"><label><input type="radio" name="b2b" value="tak"> Tak</label><label><input type="radio" name="b2b" value="nie"> Nie, tylko konsumentom</label></div></fieldset>
    <fieldset><legend>2. Jaki masz status w VAT?</legend><div class="radios"><label><input type="radio" name="vat" value="czynny"> Czynny podatnik VAT</label><label><input type="radio" name="vat" value="zwolniony"> Zwolniony z VAT</label></div></fieldset>
    <fieldset><legend>3. Czy w 2026 r. wystawiasz faktury poza KSeF, bo sprzedaż fakturowana nie przekracza 10 000 zł miesięcznie?</legend><div class="radios"><label><input type="radio" name="small" value="tak"> Tak</label><label><input type="radio" name="small" value="nie"> Nie / nie wiem</label></div></fieldset>
    <fieldset><legend>4. Czy wystawiasz faktury z kasy fiskalnej?</legend><div class="radios"><label><input type="radio" name="cash" value="tak"> Tak</label><label><input type="radio" name="cash" value="nie"> Nie</label></div></fieldset>
    <fieldset><legend>5. Czy płacisz dostawcom przelewem za faktury?</legend><div class="radios"><label><input type="radio" name="pays" value="tak"> Tak</label><label><input type="radio" name="pays" value="nie"> Nie</label></div></fieldset>
    <fieldset><legend>6. Czy płacisz faktury w mechanizmie podzielonej płatności (MPP)?</legend><div class="radios"><label><input type="radio" name="mpp" value="tak"> Tak</label><label><input type="radio" name="mpp" value="nie"> Nie</label></div></fieldset>
    <div class="btns"><button type="submit" class="btn">Pokaż moje obowiązki</button><button type="button" class="btn ghost" id="j-reset">Zacznij od nowa</button></div>
  </form>
  <div id="j-out" aria-live="polite"></div>
  <p class="privacy">🔒 Dane nie opuszczają Twojej przeglądarki. Odpowiedzi nie są nigdzie zapisywane.</p>
</section>""",
    content="""
<h2>Stan prawny na 13 listopada 2026 r.</h2>
<div class="status warn"><p class="status-head"><span class="ico" aria-hidden="true">!</span>Kary za KSeF – przepisy w trakcie zmian</p>
<p>Przepisy o karach z art. 106ni ustawy o VAT są obecnie zmieniane w toku prac legislacyjnych. Dopóki prace się nie zakończą, nie przesądzamy, od kiedy i w jakim kształcie kary będą stosowane. Zmiany dotyczą kar, a <strong>nie samych obowiązków</strong>: wystawiania faktur w KSeF i podawania numeru KSeF w przelewach od 1 stycznia 2027 r. Zaktualizujemy tę stronę po zakończeniu prac.</p></div>

<h2>Najważniejsze daty</h2>
<div class="table-wrap"><table>
<thead><tr><th scope="col">Data</th><th scope="col">Co się dzieje</th><th scope="col">Kogo dotyczy</th></tr></thead>
<tbody>
<tr><th scope="row">do 31.12.2026</th><td>Można wystawiać faktury poza KSeF, jeśli miesięczna sprzedaż udokumentowana fakturami nie przekracza 10 000 zł (art. 145m); można też wystawiać faktury z kasy fiskalnej poza KSeF (art. 145n)</td><td>najmniejsze firmy, sprzedawcy z kasą</td></tr>
<tr><th scope="row">do 31.12.2026</th><td>Odroczony obowiązek podawania numeru KSeF w płatnościach (art. 108g) i w MPP</td><td>czynni podatnicy VAT</td></tr>
<tr><th scope="row">1.01.2027</th><td>Koniec obu zwolnień – faktury dla firm wystawiasz w KSeF</td><td>wszyscy wystawiający faktury firmom</td></tr>
<tr><th scope="row">1.01.2027</th><td>Numer KSeF lub identyfikator zbiorczy w przelewach, także w komunikacie MPP</td><td>płatności między czynnymi podatnikami VAT</td></tr>
<tr><th scope="row">w toku zmian</th><td>Kary z art. 106ni – przepisy są obecnie zmieniane w toku prac legislacyjnych</td><td>wystawcy faktur</td></tr>
</tbody></table></div>

<h2>Wystawianie faktur: koniec limitu 10 000 zł</h2>
<p>Do końca 2026 r. najmniejsi przedsiębiorcy mogą wystawiać faktury poza KSeF, jeśli ich miesięczna sprzedaż dokumentowana fakturami nie przekracza 10 000 zł. Tak samo faktury z kasy fiskalnej mogą powstawać poza systemem. Od 1 stycznia 2027 r. oba wyjątki znikają: każda faktura dla innej firmy powstaje w KSeF. Faktury dla konsumentów pozostają dobrowolne – MF: <q>Faktury na rzecz osób fizycznych nieprowadzących działalności gospodarczej mogą być wystawiane w KSeF dobrowolnie.</q></p>

<h2>Płatności: numer KSeF w przelewie</h2>
<p>Od 1 stycznia 2027 r. czynny podatnik VAT, który płaci innemu czynnemu podatnikowi VAT za fakturę z KSeF, podaje w przelewie numer KSeF – przy jednej fakturze sam numer, przy kilku identyfikator zbiorczy albo kilka numerów, o ile zmieszczą się w polu tytułu. Jeśli Ty lub kontrahent jesteście zwolnieni z VAT, podanie numeru jest dobrowolne. W MPP numer KSeF (lub identyfikator zbiorczy) trafia do pola <code>/INV/</code> komunikatu.</p>
<ol class="steps">
<li>Zapewnij sobie dostęp do KSeF: Aplikacja Podatnika KSeF lub program księgowy.</li>
<li>Ustal, skąd będziesz brać numery KSeF faktur zakupowych (UPO, program, nazwa pliku XML).</li>
<li>Sprawdzaj numery przed płatnością – <a href="/">walidator</a> lub <a href="/sprawdz-wiele-numerow-ksef/">sprawdzanie wielu numerów</a>.</li>
<li>Przy MPP używaj <a href="/przelew-mpp-numer-ksef/">generatora komunikatu MPP</a>.</li>
</ol>

<h2>Kary: co wiemy, a czego jeszcze nie</h2>
<p>Art. 106ni ustawy o VAT przewiduje kary m.in. za niewystawienie faktury w KSeF. Według omówień w prasie branżowej kara może wynieść do 100% kwoty VAT z faktury, a przy fakturze bez VAT – 18,7% kwoty należności ogółem. Przepisy o karach są jednak obecnie zmieniane w toku prac legislacyjnych, a ich ostateczny kształt i termin stosowania nie są jeszcze przesądzone. Planuj więc tak, jakby wszystkie obowiązki zaczynały się 1 stycznia 2027 r. – zmiany dotyczą kar, nie samych obowiązków. Aktualny stan sprawdzisz na stronie MF ksef.podatki.gov.pl.</p>
<p class="note">To narzędzie ma charakter informacyjny i nie stanowi porady podatkowej. W sprawach dotyczących Twojej firmy skonsultuj się z księgową lub doradcą podatkowym.</p>
""",
    faq=[
        ("Czy JDG musi wystawiać faktury w KSeF od 2027 r.?", "Tak, jeśli wystawia faktury innym firmom. Od 1 stycznia 2027 r. kończy się zwolnienie dla sprzedaży do 10 000 zł miesięcznie i dla faktur z kasy fiskalnej. Faktury dla konsumentów w KSeF pozostają dobrowolne."),
        ("Czy podatnik zwolniony z VAT musi podawać numer KSeF w przelewie?", "Nie. Obowiązek dotyczy płatności między czynnymi podatnikami VAT. Gdy jedna ze stron jest zwolniona z VAT, podanie numeru jest dobrowolne."),
        ("Od kiedy obowiązują kary za KSeF?", "Według obecnych przepisów od 1 stycznia 2027 r. Sejm 6 listopada 2026 r. uchwalił przesunięcie na 1 stycznia 2028 r., ale ustawa jest w Senacie i nie jest jeszcze obowiązującym prawem (stan na 13.11.2026)."),
        ("Co z fakturami z kasy fiskalnej?", "Do 31 grudnia 2026 r. można je wystawiać poza KSeF. Od 1 stycznia 2027 r. fakturę dla firmy trzeba wystawić w KSeF."),
        ("Czy muszę odbierać faktury przez KSeF?", "Tak – faktury od kontrahentów wystawiających w KSeF otrzymujesz przez system. Potrzebujesz dostępu przez Aplikację Podatnika KSeF lub program księgowy."),
        ("Czy przesunięcie kar oznacza przesunięcie obowiązków?", "Nie. Projekt dotyczy terminu stosowania kar. Obowiązki wystawiania faktur w KSeF i podawania numeru KSeF w przelewach od 1 stycznia 2027 r. pozostają."),
    ],
    sources=[MF_TERM, MF_NUM, GOV_KARY],
)

# ---------------------------------------------------------------- PRIVACY
PRIV = dict(
    title="Polityka prywatności – NumerKSeF",
    desc="Polityka prywatności serwisu NumerKSeF: narzędzia działają w przeglądarce, nie zbieramy danych, nie używamy ciasteczek ani narzędzi śledzących.",
    app=False, trust=False, related=False,
    h1="Polityka prywatności",
    intro="Krótko: nie zbieramy Twoich danych. Wszystkie narzędzia działają w Twojej przeglądarce.",
    trail=[("Strona główna", "/"), ("Polityka prywatności", "/polityka-prywatnosci/")],
    content="""
<h2>Przetwarzanie danych w narzędziach</h2>
<p>Numery KSeF, NIP-y, kwoty, pliki XML, pliki CSV i linki z kodów QR, które wpisujesz lub wczytujesz, są przetwarzane wyłącznie przez skrypty uruchomione w Twojej przeglądarce. Nie są wysyłane na żaden serwer – serwis to zestaw statycznych plików i nie ma zaplecza, które mogłoby je odebrać. Dane nie opuszczają Twojej przeglądarki i znikają po zamknięciu lub odświeżeniu strony.</p>
<h2>Ciasteczka i śledzenie</h2>
<p>Nie używamy ciasteczek, analityki, pikseli reklamowych, zewnętrznych czcionek ani bibliotek ładowanych z obcych serwerów (CDN). Nie wyświetlamy reklam.</p>
<h2>Tryb ciemny</h2>
<p>Jeśli przełączysz tryb jasny lub ciemny, zapamiętamy wybór w pamięci localStorage Twojej przeglądarki (klucz <code>theme</code>), aby kolejne strony wyświetlały się tak samo. Ta informacja nie jest nigdzie wysyłana i możesz ją usunąć, czyszcząc dane witryny w przeglądarce. Bez wyboru strona stosuje ustawienie systemu (prefers-color-scheme).</p>
<h2>Hosting</h2>
<p>Strona jest hostowana w usłudze GitHub Pages (GitHub, Inc.). Jak każdy serwer WWW, GitHub może technicznie rejestrować podstawowe dane połączenia (np. adres IP) w celu zapewnienia bezpieczeństwa i działania usługi. Nie mamy dostępu do tych danych. Szczegóły: <a href="https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement" rel="noopener" target="_blank">oświadczenie o prywatności GitHub</a>.</p>
<h2>Linki zewnętrzne</h2>
<p>Strony zawierają linki do źródeł (np. Ministerstwa Finansów, banków). Po przejściu na nie obowiązują zasady prywatności tych serwisów.</p>
<h2>Zmiany</h2>
<p>Jeśli zasady się zmienią, zaktualizujemy tę stronę i datę poniżej.</p>
""",
)

ABOUT = dict(
    title="O serwisie NumerKSeF – niezależne darmowe narzędzia KSeF",
    desc="NumerKSeF to niezależny serwis z darmowymi narzędziami do numerów KSeF, przelewów MPP i faktur XML. Nie jest związany z Ministerstwem Finansów. Nie stanowi porady podatkowej.",
    app=False, trust=False,
    h1="O serwisie NumerKSeF",
    intro="Darmowe, proste narzędzia, które pomagają przygotować się na numer KSeF w przelewach od 1 stycznia 2027 r.",
    trail=[("Strona główna", "/"), ("O serwisie", "/o-serwisie/")],
    content="""
<h2>Co robimy</h2>
<p>NumerKSeF to zestaw bezpłatnych narzędzi dla przedsiębiorców, księgowych i działów finansowych: walidator numeru KSeF i identyfikatora zbiorczego, generator tytułu przelewu i komunikatu MPP, masowa weryfikacja numerów z plików, odczyt danych do przelewu z faktury XML oraz generator i dekoder kodów QR KSeF.</p>
<h2>Zasady</h2>
<ul>
<li><strong>Prywatność.</strong> Wszystko działa w przeglądarce. Dane nie opuszczają Twojej przeglądarki. Bez rejestracji, reklam, ciasteczek i śledzenia.</li>
<li><strong>Źródła.</strong> Formaty i reguły opieramy na oficjalnej dokumentacji Ministerstwa Finansów (ksef.podatki.gov.pl, dokumentacja API KSeF 2.0, schemat FA(3)) oraz na specyfikacjach banków. Każda strona zawiera listę źródeł.</li>
<li><strong>Aktualność.</strong> Przy zmianach przepisów aktualizujemy treści i datę „ostatnia aktualizacja”. Stan prawny opisany w serwisie: 13 listopada 2026 r.</li>
</ul>
<h2>Niezależność</h2>
<p><strong>Serwis jest niezależny i nie jest powiązany z Ministerstwem Finansów, Krajową Administracją Skarbową ani żadnym bankiem.</strong> „KSeF” to nazwa Krajowego Systemu e-Faktur prowadzonego przez Ministerstwo Finansów; używamy jej wyłącznie w celu opisu.</p>
<h2>Zastrzeżenie</h2>
<p>Treści i wyniki narzędzi mają charakter informacyjny i <strong>nie stanowią porady podatkowej ani prawnej</strong>. Narzędzia sprawdzają poprawność zapisu (format, sumy kontrolne), a nie to, czy faktura istnieje w KSeF lub czy płatność jest prawidłowa. Za decyzje podatkowe odpowiada podatnik – w razie wątpliwości skonsultuj się z doradcą podatkowym lub księgową. Nie ponosimy odpowiedzialności za skutki użycia narzędzi.</p>
<h2>Uwagi i błędy</h2>
<p>Zauważyłeś błąd albo zmianę w przepisach? Zgłoś ją w repozytorium serwisu: <a href="https://github.com/mydevspace2/numer-ksef/issues" rel="noopener" target="_blank">github.com/mydevspace2/numer-ksef</a>.</p>
""",
    faq=[
        ("Czy NumerKSeF to strona Ministerstwa Finansów?", "Nie. To niezależny serwis, niezwiązany z Ministerstwem Finansów ani KAS. Oficjalne informacje o KSeF znajdziesz na ksef.podatki.gov.pl."),
        ("Czy narzędzia są płatne?", "Nie. Wszystkie narzędzia są bezpłatne i nie wymagają rejestracji."),
        ("Czy wyniki narzędzi to porada podatkowa?", "Nie. Wyniki mają charakter informacyjny. W sprawach podatkowych skonsultuj się z doradcą lub księgową."),
    ],
    sources=[MF_NUM, MF_TERM, DOC_NUM, XSD],
)
