# -*- coding: utf-8 -*-
from sources import *

EX = "5265877635-20250826-0100001AF629-AF"

# ---------------------------------------------------------------- HOME
HOME = dict(
    title="Numer KSeF – walidator i tytuł przelewu 2027 | NumerKSeF",
    desc="Sprawdź numer KSeF za darmo: suma kontrolna CRC-8, NIP i data. Ułóż tytuł przelewu z numerem KSeF (do 3 numerów, 140 znaków). Dane nie opuszczają przeglądarki.",
    app_name="Walidator numeru KSeF i generator tytułu przelewu",
    h1="Sprawdź numer KSeF i przygotuj tytuł przelewu",
    intro="Wklej numer KSeF – od razu zobaczysz, czy jest poprawny i dlaczego. Potem ułóż gotowy tytuł przelewu z maksymalnie trzema numerami. Od 1 stycznia 2027 r. numer KSeF w przelewie między czynnymi podatnikami VAT jest obowiązkowy.",
    trail=[("Strona główna", "/")],
    scripts=["page-home.js"],
    tool="""
<section class="tool" aria-labelledby="h-walidator">
  <h2 id="h-walidator">Walidator numeru KSeF</h2>
  <div class="field">
    <label for="k-in">Numer KSeF lub identyfikator zbiorczy</label>
    <input id="k-in" class="mono" type="text" inputmode="text" autocomplete="off" autocapitalize="characters" spellcheck="false" placeholder="5265877635-20250826-0100001AF629-AF" aria-describedby="k-hint">
    <p class="hint" id="k-hint">35 znaków: NIP-RRRRMMDD-12 znaków HEX-suma kontrolna. Spacje i długie myślniki poprawimy sami.</p>
  </div>
  <div class="btns">
    <button type="button" class="btn" id="k-check">Sprawdź</button>
    <button type="button" class="btn ghost" id="k-ex">Przykład</button>
    <button type="button" class="btn ghost" id="k-clear">Wyczyść</button>
    <button type="button" class="btn ghost" id="k-use" hidden>Użyj w tytule przelewu ↓</button>
  </div>
  <div id="k-res" class="status" role="status" aria-live="polite"></div>
</section>
<section class="tool" id="tytul" aria-labelledby="h-tytul">
  <h2 id="h-tytul">Generator tytułu przelewu z numerem KSeF</h2>
  <div class="grid2">
    <div class="field"><label for="t1">Numer KSeF lub identyfikator zbiorczy 1</label><input id="t1" class="mono" type="text" autocomplete="off" spellcheck="false" autocapitalize="characters"></div>
    <div class="field"><label for="t2">Numer 2 <span class="hint">(opcjonalnie)</span></label><input id="t2" class="mono" type="text" autocomplete="off" spellcheck="false" autocapitalize="characters"></div>
    <div class="field"><label for="t3">Numer 3 <span class="hint">(opcjonalnie)</span></label><input id="t3" class="mono" type="text" autocomplete="off" spellcheck="false" autocapitalize="characters"></div>
    <div class="field"><label for="t-extra">Dodatkowy opis <span class="hint">(np. numer faktury)</span></label><input id="t-extra" type="text" autocomplete="off" maxlength="140"></div>
  </div>
  <div class="btns"><button type="button" class="btn ghost" id="t-ex">Przykład</button><button type="button" class="btn ghost" id="t-clear">Wyczyść</button></div>
  <p class="label" id="t-out-l">Gotowy tytuł przelewu</p>
  <p class="out placeholder" id="t-out" aria-labelledby="t-out-l" aria-live="polite">Tu pojawi się tytuł przelewu.</p>
  <div class="out-row"><span class="counter" id="t-count">0 / 140 znaków</span><button type="button" class="btn small" id="t-copy" data-copy="t-out" disabled>Kopiuj tytuł</button></div>
  <div id="t-stat" class="status" role="status" aria-live="polite"></div>
  <p class="privacy">🔒 Dane nie opuszczają Twojej przeglądarki. Narzędzie sprawdza zapis numeru, a nie to, czy faktura istnieje w KSeF.</p>
</section>""",
    content="""
<h2>Wszystkie narzędzia w jednym miejscu</h2>
<p>Poza walidatorem na tej stronie masz do dyspozycji komplet darmowych narzędzi do płatności z numerem KSeF – od komunikatu MPP po kod QR. Każde działa w przeglądarce i nie wymaga logowania.</p>
<div class="hub">
<a href="/przelew-mpp-numer-ksef/"><strong>Komunikat przelewu MPP</strong><span>/VAT/ /IDC/ /INV/ /TXT/ z numerem KSeF, walidacja każdego pola i limit 140 znaków.</span></a>
<a href="/identyfikator-zbiorczy-ksef/"><strong>Identyfikator zbiorczy</strong><span>Płacisz za kilka faktur jednym przelewem? Sprawdź identyfikator zbiorczy.</span></a>
<a href="/sprawdz-wiele-numerow-ksef/"><strong>Wiele numerów naraz</strong><span>Wklej listę lub wyciąg bankowy, pobierz wyniki w CSV.</span></a>
<a href="/przelew-z-faktury-xml-ksef/"><strong>Przelew z faktury XML</strong><span>Plik FA(3) → rachunek, kwota, termin, tytuł i komunikat MPP.</span></a>
<a href="/kod-qr-ksef/"><strong>Kod QR KSeF</strong><span>Generator KOD I i dekoder linków z ochroną przed fałszywymi domenami.</span></a>
<a href="/ksef-od-2027-jdg/"><strong>KSeF dla JDG od 2027</strong><span>Krótka ankieta: co zmienia się w Twojej firmie 1 stycznia 2027 r.</span></a>
</div>

<h2>Od 1 stycznia 2027 r.: numer KSeF w tytule przelewu</h2>
<p>Do końca 2026 r. odroczony jest obowiązek podawania numeru KSeF przy płatnościach. Ministerstwo Finansów pisze wprost: <q>Do końca 2026 r. odroczony jest obowiązek podawania numeru KSeF faktury podczas płatności pomiędzy podatnikami czynnymi (art. 108g …) oraz w ramach MPP</q>. Od 1 stycznia 2027 r. czynny podatnik VAT, który płaci przelewem innemu czynnemu podatnikowi VAT za fakturę wystawioną w KSeF, podaje w przelewie jej numer KSeF.</p>
<ul>
<li><strong>Jedna faktura</strong> – <q>płatności za pojedynczą fakturę – podawany będzie numer KSeF faktury</q>.</li>
<li><strong>Kilka faktur</strong> – identyfikator zbiorczy albo kilka numerów KSeF (lub kilka identyfikatorów), <q>przy uwzględnieniu ograniczeń technicznych pola zawierającego tytuł płatności</q>.</li>
<li><strong>Przelew MPP</strong> – numer KSeF trafia do komunikatu split payment (pole <code>/INV/</code>). Do tego służy nasz <a href="/przelew-mpp-numer-ksef/">generator komunikatu MPP</a>.</li>
<li><strong>Wyjątki</strong> – faktury wystawione w trybie awaryjnym oraz faktury offline, które nie zostały wprowadzone do systemu w związku z ogłoszoną awarią.</li>
</ul>

<h2>Jak zbudowany jest numer KSeF</h2>
<p>Numer KSeF nadaje wyłącznie system po przyjęciu faktury. Według dokumentacji MF <q>zawsze ma długość 35 znaków</q> i wzór <code>9999999999-RRRRMMDD-FFFFFFFFFFFF-FF</code>. Oficjalny przykład to <code>%s</code>.</p>
<div class="table-wrap"><table>
<thead><tr><th scope="col">Część</th><th scope="col">Znaczenie</th><th scope="col">W przykładzie</th></tr></thead>
<tbody>
<tr><th scope="row">10 cyfr</th><td>NIP sprzedawcy (przy samofakturowaniu – NIP nabywcy, przy przedstawicielu podatkowym – NIP przedstawiciela)</td><td class="mono">5265877635</td></tr>
<tr><th scope="row">RRRRMMDD</th><td>Data przyjęcia faktury do KSeF – nie data wystawienia z pola P_1</td><td class="mono">20250826</td></tr>
<tr><th scope="row">12 znaków HEX</th><td>Część techniczna: tylko 0–9 i A–F, wielkie litery</td><td class="mono">0100001AF629</td></tr>
<tr><th scope="row">2 znaki HEX</th><td>Suma kontrolna CRC-8 z pierwszych 32 znaków</td><td class="mono">AF</td></tr>
</tbody></table></div>

<h2>Co dokładnie sprawdza walidator</h2>
<ol class="steps">
<li><strong>Porządkuje zapis.</strong> Usuwa spacje, zamienia długie myślniki (– —) na zwykłe i małe litery na wielkie. Zawsze informuje, co poprawił.</li>
<li><strong>Sprawdza długość i format.</strong> Gdy jakiś znak nie pasuje, wskazuje jego pozycję – np. „znak 23: „O” zamiast zera?”. Litery O i I to najczęstsze literówki.</li>
<li><strong>Liczy sumę kontrolną CRC-8.</strong> Według dokumentacji MF: polinom <code>0x07</code>, wartość początkowa <code>0x00</code>, wynik jako 2 znaki HEX. Pokazuje sumę podaną i obliczoną.</li>
<li><strong>Weryfikuje NIP.</strong> Wagi 6, 5, 7, 2, 3, 4, 5, 6, 7; reszta z dzielenia przez 11 musi równać się ostatniej cyfrze.</li>
<li><strong>Sprawdza datę.</strong> Musi istnieć w kalendarzu i nie może być z przyszłości. Daty sprzed 1 lutego 2026 r. oznaczamy jako numer z KSeF 1.0 lub przykładowy.</li>
</ol>
<p>Dwie sytuacje oznaczamy ostrzeżeniem, a nie błędem: <strong>stary format KSeF 1.0</strong> (36 znaków, z dodatkowym myślnikiem w części technicznej – schemat FA(3) nadal go akceptuje) oraz <strong>początek numeru, który nie jest NIP-em</strong>, ale pasuje do innych identyfikatorów dopuszczonych w schemacie (<code>M</code> + 9 cyfr albo 3 litery + 7 cyfr).</p>

<h2>Numer KSeF a numer faktury</h2>
<div class="table-wrap"><table>
<thead><tr><th scope="col"></th><th scope="col">Numer KSeF</th><th scope="col">Numer faktury</th></tr></thead>
<tbody>
<tr><th scope="row">Kto nadaje</th><td>System KSeF po przyjęciu faktury</td><td>Wystawca (pole P_2)</td></tr>
<tr><th scope="row">Gdzie go znajdziesz</th><td>W UPO, w Aplikacji Podatnika KSeF, w programie księgowym – nie ma go w pliku XML</td><td>W treści faktury</td></tr>
<tr><th scope="row">Długość</th><td>Zawsze 35 znaków</td><td>Dowolna</td></tr>
<tr><th scope="row">Rola w przelewie od 2027 r.</th><td>Obowiązkowy między czynnymi podatnikami VAT</td><td>Dodatkowo, jeśli zmieści się w tytule</td></tr>
</tbody></table></div>

<h2>Jak ułożyć tytuł przelewu</h2>
<p>Przepisy nie narzucają składni zwykłego tytułu przelewu. Pole tytułu w bankach ma zwykle 140 znaków, więc zmieszczą się najwyżej trzy numery KSeF: 3 × 35 znaków plus separatory to 107 znaków, a czwarty numer już się nie zmieści. Dlatego generator przyjmuje do trzech numerów, rozdziela je przecinkami i dopisuje Twój opis (np. numer faktury), pilnując limitu. Przy większej liczbie faktur od jednego sprzedawcy użyj <a href="/identyfikator-zbiorczy-ksef/">identyfikatora zbiorczego</a> – obejmuje do 500 faktur (50 w Aplikacji Podatnika KSeF).</p>
<p class="note">Przykłady z instrukcji banków (np. <code>3786417439-20260928-AB12CD34EF56-78</code>) są ilustracyjne – nie mają poprawnej sumy kontrolnej, więc walidator słusznie je odrzuci.</p>

<h2>Dlaczego numeru KSeF nie da się zapisać w kodzie QR do płatności</h2>
<p>Popularne kody QR do przelewu (standard 2D Związku Banków Polskich) mają pole „Tytuł płatności” ograniczone do 32 znaków, a numer KSeF ma 35. Tytuł z numerem KSeF trzeba więc wkleić ręcznie albo przygotować w pliku importu do banku. Nie myl tego z <a href="/kod-qr-ksef/">kodem QR KSeF</a> na fakturze – on służy do weryfikacji faktury, a nie do płatności.</p>
""" % EX,
    faq=[
        ("Ile znaków ma numer KSeF?", "35 znaków, licząc z myślnikami. Numery z KSeF 1.0 mogły mieć 36 znaków (dodatkowy myślnik w części technicznej) – walidator rozpoznaje je i pokazuje ostrzeżenie."),
        ("Gdzie znajdę numer KSeF faktury?", "W UPO (Urzędowym Poświadczeniu Odbioru), w Aplikacji Podatnika KSeF albo w programie księgowym połączonym z KSeF. Nie ma go w samym pliku XML faktury."),
        ("Czy od 2027 r. muszę podawać numer KSeF w przelewie?", "Tak, od 1 stycznia 2027 r., gdy czynny podatnik VAT płaci przelewem innemu czynnemu podatnikowi VAT za fakturę wystawioną w KSeF – także w MPP. Nie dotyczy to faktur wystawionych w trybie awaryjnym ani faktur offline, które nie trafiły do systemu z powodu ogłoszonej awarii."),
        ("Ile numerów KSeF zmieszczę w tytule przelewu?", "Najczęściej trzy. Typowe pole tytułu ma 140 znaków, a każdy numer 35. Przy większej liczbie faktur od jednego sprzedawcy użyj identyfikatora zbiorczego."),
        ("Co oznacza błąd sumy kontrolnej?", "Ostatnie dwa znaki nie pasują do reszty numeru – to prawie zawsze literówka (np. litera O zamiast zera). Skopiuj numer ponownie z UPO lub z programu."),
        ("Czy walidator sprawdza, czy faktura istnieje w KSeF?", "Nie. Sprawdza tylko poprawność zapisu: format, sumę kontrolną CRC-8, NIP i datę. Istnienie faktury potwierdzisz w KSeF lub przez kod QR na fakturze."),
        ("Czy mogę sam wygenerować numer KSeF?", "Nie. Numer KSeF nadaje wyłącznie system KSeF po przyjęciu faktury."),
    ],
    sources=[MF_NUM, MF_TERM, DOC_NUM, XSD, ZBP],
)

# ---------------------------------------------------------------- MPP
MPP = dict(
    title="Przelew MPP z numerem KSeF – generator komunikatu split payment",
    desc="Darmowy generator komunikatu MPP 2027: /VAT/ /IDC/ /INV/ /TXT/ z numerem KSeF lub identyfikatorem zbiorczym. Walidacja pól i limit 140 znaków.",
    app_name="Generator komunikatu przelewu MPP z numerem KSeF",
    h1="Komunikat przelewu MPP z numerem KSeF – generator split payment 2027",
    intro="Wpisz kwotę VAT, NIP sprzedawcy i numer KSeF – dostaniesz gotowy komunikat <code>/VAT/…/IDC/…/INV/…/TXT/…</code> sprawdzony pole po polu, w trzech układach: jedna linia, cztery linie i podział po 35 znaków.",
    trail=[("Strona główna", "/"), ("Przelew MPP z numerem KSeF", "/przelew-mpp-numer-ksef/")],
    scripts=["page-mpp.js"],
    tool="""
<section class="tool" aria-labelledby="h-mpp">
  <h2 id="h-mpp">Generator komunikatu MPP</h2>
  <div class="grid2">
    <div class="field"><label for="m-vat">Kwota VAT (zł) <span class="hint">– /VAT/</span></label><input id="m-vat" type="text" inputmode="decimal" autocomplete="off" placeholder="230,00" aria-describedby="m-vat-msg"><p class="hint" id="m-vat-msg" aria-live="polite"></p></div>
    <div class="field"><label for="m-gross">Kwota przelewu brutto (zł) <span class="hint">– do kontroli</span></label><input id="m-gross" type="text" inputmode="decimal" autocomplete="off" placeholder="1230,00" aria-describedby="m-gross-msg"><p class="hint" id="m-gross-msg" aria-live="polite"></p></div>
    <div class="field"><label for="m-nip">NIP sprzedawcy <span class="hint">– /IDC/</span></label><input id="m-nip" type="text" inputmode="numeric" autocomplete="off" placeholder="5265877635" aria-describedby="m-nip-msg"><p class="hint" id="m-nip-msg" aria-live="polite"></p></div>
    <div class="field"><label for="m-date">Data przelewu <span class="hint">(opcjonalnie)</span></label><input id="m-date" type="date"><p class="hint">Przed 1.01.2027 w /INV/ może być numer faktury.</p></div>
  </div>
  <div class="field" id="m-inv-wrap"><label for="m-inv">Numer KSeF, identyfikator zbiorczy lub numer faktury <span class="hint">– /INV/ (maks. 35 znaków)</span></label><input id="m-inv" class="mono" type="text" autocomplete="off" spellcheck="false" placeholder="5265877635-20250826-0100001AF629-AF" aria-describedby="m-inv-msg m-inv-kind"><p class="hint" id="m-inv-kind" aria-live="polite"></p><p class="hint" id="m-inv-msg" aria-live="polite"></p></div>
  <div class="field"><label for="m-txt">Dodatkowy tekst <span class="hint">– /TXT/ (opcjonalnie, maks. 33 znaki)</span></label><input id="m-txt" type="text" autocomplete="off" maxlength="60" placeholder="FV 12/11/2026" aria-describedby="m-txt-msg"><p class="hint" id="m-txt-msg" aria-live="polite"></p></div>
  <label class="check"><input type="checkbox" id="m-own"> Przekazanie własne między moimi rachunkami VAT (w /INV/ wpiszemy „PRZEKAZANIE WLASNE”)</label>
  <div class="btns mt14"><button type="button" class="btn ghost" id="m-ex">Przykład: jedna faktura</button><button type="button" class="btn ghost" id="m-ex-iz">Przykład: identyfikator zbiorczy</button><button type="button" class="btn ghost" id="m-clear">Wyczyść</button></div>
  <p class="label" id="m-out-l">Komunikat MPP (jedna linia)</p>
  <p class="out placeholder" id="m-out" aria-labelledby="m-out-l" aria-live="polite">Uzupełnij kwotę VAT, NIP i numer KSeF – komunikat pojawi się tutaj.</p>
  <div class="out-row"><span class="counter" id="m-count">0 / 140 znaków</span><button type="button" class="btn small" id="m-copy" data-copy="m-out" disabled>Kopiuj komunikat</button></div>
  <div id="m-stat" class="status" role="status" aria-live="polite"></div>
  <div id="m-split" hidden>
    <h3>Układ w 4 liniach – do formularzy z osobnymi polami</h3>
    <dl class="kv" id="m-lines4"></dl>
    <h3>Podział po 35 znaków (import Elixir / CSV)</h3>
    <ol class="lines35" id="m-lines35"></ol>
  </div>
  <p class="privacy">🔒 Dane nie opuszczają Twojej przeglądarki.</p>
</section>""",
    content="""
<h2>Jak wygląda komunikat MPP z numerem KSeF</h2>
<p>Przelew w mechanizmie podzielonej płatności (split payment) nie ma zwykłego tytułu. Zamiast niego bank oczekuje komunikatu ze słowami kodowymi w ściśle określonej kolejności. Specyfikacja mBanku dla pola <code>Ustrd</code> (140 znaków) opisuje format <code>/VAT/10n,2n/IDC/14x/INV/35x/TXT/33x</code> i dwie zasady: <q>Obowiązkowe jest zachowanie kolejności poszczególnych słów kodowych. Każde słowo kodowe może wystąpić wyłącznie jeden raz.</q> oraz <q>Niedozwolone są spacje pomiędzy słowem kodowym a znakiem.</q></p>
<div class="table-wrap"><table>
<thead><tr><th scope="col">Słowo kodowe</th><th scope="col">Co wpisać</th><th scope="col">Format</th><th scope="col">Wymagane</th></tr></thead>
<tbody>
<tr><th scope="row"><code>/VAT/</code></th><td>Kwota VAT z przecinkiem jako separatorem, np. 23,00. Musi być większa od 0,00 i nie wyższa niż kwota przelewu.</td><td>do 10 cyfr, przecinek, 2 cyfry</td><td>tak</td></tr>
<tr><th scope="row"><code>/IDC/</code></th><td>Identyfikator dostawcy – zwykle NIP sprzedawcy (wystawcy faktury); przy przekazaniu własnym Twój identyfikator</td><td>do 14 znaków</td><td>tak</td></tr>
<tr><th scope="row"><code>/INV/</code></th><td>Numer faktury albo numer KSeF; przy kilku fakturach z KSeF – identyfikator zbiorczy; „PRZEKAZANIE WLASNE” między własnymi rachunkami VAT</td><td>do 35 znaków</td><td>tak</td></tr>
<tr><th scope="row"><code>/TXT/</code></th><td>Dowolny tekst, np. Twój numer faktury</td><td>do 33 znaków</td><td>nie</td></tr>
</tbody></table></div>
<p>Przykłady ze specyfikacji banku (ilustracyjne, z niepoprawną sumą kontrolną):</p>
<blockquote class="mono">/VAT/23035,90/IDC/3786417439/INV/3786417439-20260928-AB12CD34EF56-78/TXT/dowolny tekst<br>/VAT/75809,43/IDC/3786417439/INV/3786417439-IZ202708-AB12CD34EF56-78/TXT/dowolny tekst</blockquote>

<h2>Co zmienia się 1 stycznia 2027 r.</h2>
<p>Ministerstwo Finansów potwierdza, że <q>w komunikacie przelewu MPP podaje się między innymi numer KSeF faktury</q>, a przy płatności za wiele faktur <q>zamiast wpisywania okresu … podaje identyfikator zbiorczy</q>. Do końca 2026 r. obowiązek jest odroczony – dlatego generator ma pole daty: przed 1 stycznia 2027 r. możesz wpisać numer faktury, a od tego dnia za faktury z KSeF podajesz numer KSeF lub identyfikator zbiorczy.</p>
<p>Numer KSeF ma dokładnie 35 znaków, czyli wypełnia całe pole <code>/INV/</code>. Twój numer faktury (pole P_2) zmieści się już tylko w <code>/TXT/</code> (do 33 znaków). Tak robi część narzędzi do płatności – to praktyka, a nie wymóg prawa.</p>

<h2>Jak użyć generatora – krok po kroku</h2>
<ol class="steps">
<li><strong>Kwota VAT.</strong> Wpisz ją z przecinkiem lub kropką – zamienimy na format banku (np. <code>1230,00</code>), bez spacji i separatorów tysięcy.</li>
<li><strong>Kwota brutto.</strong> Opcjonalnie: sprawdzimy, czy VAT nie przekracza kwoty przelewu.</li>
<li><strong>NIP sprzedawcy.</strong> Usuniemy myślniki i prefiks PL oraz sprawdzimy cyfrę kontrolną.</li>
<li><strong>Numer KSeF albo identyfikator zbiorczy.</strong> Rozpoznamy typ i sprawdzimy sumę kontrolną CRC-8. Numer w starym, 36-znakowym formacie nie zmieści się w <code>/INV/</code>.</li>
<li><strong>Tekst.</strong> Opcjonalnie, maks. 33 znaki. Zablokujemy znaki niedozwolone i słowa kodowe.</li>
<li><strong>Skopiuj.</strong> Całą linię albo poszczególne pola – w zależności od formularza Twojego banku.</li>
</ol>

<h2>Dozwolone i zabronione znaki</h2>
<p>W szczegółach płatności dozwolone są: <q>0-9, a-z, A-Z, &amp;%%()-{}/,. oraz polskie znaki</q>. Zabronione są m.in. <code>: * ; ‘ “ ! + ? | #</code>. Generator wskaże każdy niedozwolony znak w polu <code>/INV/</code> i <code>/TXT/</code>.</p>

<h2>Trzy układy tego samego komunikatu</h2>
<ul>
<li><strong>Jedna linia</strong> – do pola „Tytuł” w bankowości internetowej i do plików XML (pain.001).</li>
<li><strong>Cztery linie</strong> – część banków ma osobne pola. Deutsche Bank opisuje układ: <q>Linia 1:/VAT/1230,00 · Linia 2:/IDC/1234567890 · Linia 3:/INV/ABC123 · Linia 4:/TXT/dodatkowy opis</q>. mBank zapowiedział, że <q>w polu Numer faktury będzie można wprowadzić również numer faktury KSeF</q>, a <q>pole Tytuł przelewu zastąpimy polem Dodatkowe dane do faktury</q>.</li>
<li><strong>Po 35 znaków</strong> – w imporcie Elixir/CSV tytuł dzieli się na sekcje <q>maksymalnie 35 znaków na sekcję</q>. Dla MPP kod dokumentu to „53”, a w tytule muszą być trzy słowa kodowe (VAT, IDC, INV) w ściśle określonej kolejności.</li>
</ul>
<p class="note">Banki wciąż publikują swoje zasady dla numeru KSeF w MPP. Przed pierwszą płatnością w 2027 r. wyślij jeden przelew próbny i sprawdź, czy bank przyjął komunikat bez zmian.</p>
""",
    faq=[
        ("Co wpisać w /INV/ od 2027 roku?", "Numer KSeF faktury (35 znaków). Gdy płacisz jednym przelewem za kilka faktur z KSeF od tego samego sprzedawcy – identyfikator zbiorczy. Między własnymi rachunkami VAT – „PRZEKAZANIE WLASNE”."),
        ("Gdzie wpisać swój numer faktury, skoro /INV/ zajmuje numer KSeF?", "W polu /TXT/, które mieści do 33 znaków. Pole jest opcjonalne."),
        ("Czy kwotę VAT piszę z kropką czy z przecinkiem?", "Z przecinkiem, np. 23,00 – tego wymaga format banku. Generator sam zamieni kropkę na przecinek i usunie spacje."),
        ("Jaki jest limit długości komunikatu MPP?", "140 znaków dla całego komunikatu. /IDC/ do 14 znaków, /INV/ do 35, /TXT/ do 33. Z numerem KSeF i 10-cyfrowym NIP-em zostaje zwykle wystarczająco miejsca na krótki tekst."),
        ("Czy mogę zapłacić w MPP za kilka faktur jednym przelewem?", "Tak – w /INV/ podajesz wtedy identyfikator zbiorczy KSeF zamiast okresu. Wszystkie faktury w identyfikatorze muszą mieć tego samego sprzedawcę."),
        ("Które znaki są niedozwolone?", "Między innymi : * ; ‘ “ ! + ? | #. Dozwolone są cyfry, litery (także polskie), spacja oraz &amp; % ( ) - { } / , ."),
        ("Czy generator wysyła dane do banku?", "Nie. Wszystko dzieje się w Twojej przeglądarce. Kopiujesz gotowy tekst i wklejasz go w bankowości."),
    ],
    sources=[MBANK_SPEC, MBANK_IMPORT, MBANK_NEWS, DB, MF_NUM, MF_TERM],
)

# ---------------------------------------------------------------- IZ
IZ = dict(
    title="Identyfikator zbiorczy KSeF – sprawdź poprawność online",
    desc="Sprawdź identyfikator zbiorczy KSeF: format IZ, NIP, rok i miesiąc, suma kontrolna CRC-8. Limity 500/50/132, przykład MF i zasady użycia w przelewie.",
    app_name="Walidator identyfikatora zbiorczego KSeF",
    h1="Identyfikator zbiorczy KSeF – sprawdź poprawność i rozłóż na części",
    intro="Płacisz jednym przelewem za kilka faktur? Wklej identyfikator zbiorczy – sprawdzimy jego budowę, NIP, miesiąc wygenerowania i sumę kontrolną, zanim trafi do tytułu przelewu lub komunikatu MPP.",
    trail=[("Strona główna", "/"), ("Identyfikator zbiorczy KSeF", "/identyfikator-zbiorczy-ksef/")],
    scripts=["page-iz.js"],
    tool="""
<section class="tool" aria-labelledby="h-iz">
  <h2 id="h-iz">Walidator identyfikatora zbiorczego</h2>
  <div class="field">
    <label for="iz-in">Identyfikator zbiorczy</label>
    <input id="iz-in" class="mono" type="text" autocomplete="off" autocapitalize="characters" spellcheck="false" placeholder="1111111111-IZ202607-65ED02180000-E7" aria-describedby="iz-hint">
    <p class="hint" id="iz-hint">Wzór: 9999999999-IZRRRRMM-FFFFFFFFFFFF-FF (35 znaków).</p>
  </div>
  <div class="btns"><button type="button" class="btn" id="iz-check">Sprawdź</button><button type="button" class="btn ghost" id="iz-ex">Przykład MF</button><button type="button" class="btn ghost" id="iz-clear">Wyczyść</button></div>
  <div id="iz-res" class="status" role="status" aria-live="polite"></div>
  <p class="privacy">🔒 Dane nie opuszczają Twojej przeglądarki.</p>
</section>""",
    content="""
<h2>Czym jest identyfikator zbiorczy</h2>
<p>Identyfikator zbiorczy (w skrócie IZ) to jeden zapis, który zastępuje w przelewie wiele numerów KSeF. Ministerstwo Finansów przewiduje go dla <q>płatności za więcej niż jedną fakturę</q>: zamiast kilku numerów KSeF możesz podać zbiorczy identyfikator. W przelewie MPP identyfikator zbiorczy podaje się w polu <code>/INV/</code> <q>zamiast wpisywania okresu</q>. Obowiązek podawania numeru KSeF lub identyfikatora w płatnościach między czynnymi podatnikami VAT obowiązuje od 1 stycznia 2027 r.</p>

<h2>Budowa identyfikatora zbiorczego</h2>
<p>Według grafiki MF identyfikator ma wzór <code>9999999999-IZRRRRMM-FFFFFFFFFFFF-FF</code> i – tak jak numer KSeF – 35 znaków. Oficjalny przykład ze specyfikacji API KSeF 2.0 to <code>1111111111-IZ202607-65ED02180000-E7</code>.</p>
<div class="table-wrap"><table>
<thead><tr><th scope="col">Część</th><th scope="col">Znaczenie</th><th scope="col">W przykładzie</th></tr></thead>
<tbody>
<tr><th scope="row">10 cyfr</th><td>NIP kontekstu uwierzytelnienia generującego identyfikator (nowsza grafika MF z 09.11.2026 opisuje to pole jako „NIP sprzedawcy”)</td><td class="mono">1111111111</td></tr>
<tr><th scope="row">IZ + RRRRMM</th><td>Oznaczenie „IZ” oraz rok i miesiąc wygenerowania</td><td class="mono">IZ202607</td></tr>
<tr><th scope="row">12 znaków HEX</th><td>Część techniczna</td><td class="mono">65ED02180000</td></tr>
<tr><th scope="row">2 znaki HEX</th><td>Suma kontrolna (wyliczana automatycznie)</td><td class="mono">E7</td></tr>
</tbody></table></div>
<p>Sprawdziliśmy, że identyfikator zbiorczy używa <strong>tej samej sumy kontrolnej CRC-8</strong> co numer KSeF (polinom 0x07, wartość początkowa 0x00, liczona z pierwszych 32 znaków). Przykład MF daje sumę E7 – dokładnie taką, jak w identyfikatorze. Dzięki temu walidator wychwyci literówkę także w identyfikatorze zbiorczym.</p>

<h2>Limity identyfikatora zbiorczego</h2>
<div class="table-wrap"><table>
<thead><tr><th scope="col">Zasada</th><th scope="col">Limit</th></tr></thead>
<tbody>
<tr><th scope="row">Liczba numerów KSeF w jednym identyfikatorze</th><td>od 2 do 500</td></tr>
<tr><th scope="row">… gdy generujesz w Aplikacji Podatnika KSeF</th><td>do 50</td></tr>
<tr><th scope="row">W ilu identyfikatorach może być jedna faktura</th><td>maks. 132 (w danym kontekście)</td></tr>
<tr><th scope="row">Sprzedawca</th><td>wszystkie faktury muszą mieć tego samego sprzedawcę (Podmiot1)</td></tr>
</tbody></table></div>

<h2>Jak wygenerować identyfikator zbiorczy</h2>
<ol class="steps">
<li>Otwórz program księgowy połączony z API KSeF (MF zapowiada tę funkcję także w Aplikacji Podatnika KSeF).</li>
<li>Zaznacz faktury od jednego sprzedawcy, które chcesz zapłacić jednym przelewem.</li>
<li>Wygeneruj identyfikator zbiorczy i skopiuj go.</li>
<li>Sprawdź go tutaj, a potem wklej do <a href="/">tytułu przelewu</a> lub do <a href="/przelew-mpp-numer-ksef/">komunikatu MPP</a>.</li>
</ol>
<p>Generowanie i odczytanie, jakie faktury obejmuje identyfikator, wymaga zalogowania do KSeF. Dlatego żadna strona bez dostępu do Twojego konta – także ta – nie powie, które faktury kryją się za identyfikatorem. Walidator sprawdza wyłącznie poprawność zapisu.</p>

<h2>Najczęstsze pomyłki</h2>
<ul>
<li><strong>Numer KSeF zamiast identyfikatora</strong> – po NIP-ie jest 8 cyfr daty, a nie „IZ”. Walidator to rozpozna i powie, z czym masz do czynienia.</li>
<li><strong>Mylenie z IPKSeF</strong> – w schemacie FA(3) jest też element <code>IPKSeF</code> („Identyfikator płatności Krajowego Systemu e-Faktur”). To inny, 13-znakowy identyfikator używany w linku do płatności, a nie identyfikator zbiorczy.</li>
<li><strong>Litery O i I</strong> – w części technicznej mogą być tylko cyfry 0–9 i litery A–F.</li>
<li><strong>Miesiąc z przyszłości</strong> – identyfikator nie może mieć daty wygenerowania późniejszej niż bieżący miesiąc. Przykłady z instrukcji banków (np. <code>3786417439-IZ202708-AB12CD34EF56-78</code>) są ilustracyjne.</li>
</ul>
""",
    faq=[
        ("Jak wygląda identyfikator zbiorczy KSeF?", "Ma 35 znaków według wzoru 9999999999-IZRRRRMM-FFFFFFFFFFFF-FF, np. 1111111111-IZ202607-65ED02180000-E7 (przykład MF)."),
        ("Ile faktur może obejmować identyfikator zbiorczy?", "Od 2 do 500 numerów KSeF; w Aplikacji Podatnika KSeF do 50. Jedna faktura może trafić do maks. 132 identyfikatorów w danym kontekście."),
        ("Czy faktury od różnych sprzedawców mogą być w jednym identyfikatorze?", "Nie. Wszystkie faktury w identyfikatorze zbiorczym muszą mieć tego samego sprzedawcę."),
        ("Czy to narzędzie pokaże, jakie faktury obejmuje identyfikator?", "Nie – to wie tylko KSeF. Sprawdzisz to po zalogowaniu w Aplikacji Podatnika KSeF lub w programie połączonym z KSeF. Tu sprawdzisz poprawność zapisu."),
        ("Gdzie wpisać identyfikator zbiorczy w przelewie MPP?", "W pole /INV/ – zamiast numeru faktury lub okresu. Gotowy komunikat ułożysz w naszym generatorze MPP."),
        ("Czy identyfikator zbiorczy ma sumę kontrolną?", "Tak. Ostatnie dwa znaki to suma kontrolna – według naszych testów liczona tym samym algorytmem CRC-8 co w numerze KSeF."),
    ],
    sources=[MF_NUM, IZ_PDF, IZ_PDF2, DOC_NUM, XSD, MBANK_SPEC],
)

# ---------------------------------------------------------------- BULK
BULK = dict(
    title="Sprawdź wiele numerów KSeF naraz – lista, CSV, wyciąg bankowy",
    desc="Masowa weryfikacja numerów KSeF: wklej listę, wgraj plik CSV/TXT albo wyciąg bankowy. Status każdego wiersza, przyczyna błędu i eksport wyników do CSV.",
    app_name="Masowy walidator numerów KSeF z eksportem CSV",
    h1="Sprawdź wiele numerów KSeF naraz – lista, CSV, wyciąg bankowy",
    intro="Wklej kolumnę z Excela, wgraj plik CSV lub TXT albo wklej tytuły przelewów z wyciągu. Wyszukamy w tekście każdy numer KSeF i identyfikator zbiorczy, sprawdzimy je i pokażemy, które wiersze wymagają poprawki.",
    trail=[("Strona główna", "/"), ("Sprawdź wiele numerów KSeF", "/sprawdz-wiele-numerow-ksef/")],
    scripts=["page-bulk.js"],
    tool="""
<section class="tool" aria-labelledby="h-bulk">
  <h2 id="h-bulk">Masowa weryfikacja numerów KSeF</h2>
  <fieldset><legend>Tryb</legend><div class="radios">
    <label><input type="radio" name="b-mode" id="b-mode-list" checked> Lista numerów</label>
    <label><input type="radio" name="b-mode" id="b-mode-statement"> Wyciąg bankowy (oznacz wiersze bez numeru)</label>
  </div></fieldset>
  <div class="field"><label for="b-in">Wklej numery, wiersze CSV lub tytuły przelewów – jeden wpis w linii</label>
  <textarea id="b-in" class="mono" rows="7" spellcheck="false" autocomplete="off" placeholder="5265877635-20250826-0100001AF629-AF&#10;1111111111-IZ202607-65ED02180000-E7"></textarea></div>
  <label class="file" id="b-drop" for="b-file"><strong>Albo upuść tu plik CSV / TXT</strong><br><span class="hint">Plik czyta tylko Twoja przeglądarka.</span><input type="file" id="b-file" accept=".csv,.txt,text/csv,text/plain" multiple></label>
  <div class="btns mt12"><button type="button" class="btn" id="b-check">Sprawdź</button><button type="button" class="btn ghost" id="b-ex">Przykład: lista</button><button type="button" class="btn ghost" id="b-ex-statement">Przykład: wyciąg</button><button type="button" class="btn ghost" id="b-clear">Wyczyść</button></div>
  <div id="b-sum" class="status" role="status" aria-live="polite"></div>
  <div id="b-actions" class="btns" hidden><button type="button" class="btn" id="b-csv">Pobierz CSV</button><button type="button" class="btn ghost" id="b-copy">Kopiuj wyniki</button><label class="check self-c"><input type="checkbox" id="b-only-bad"> Pokaż tylko problemy</label></div>
  <div class="table-wrap" id="b-table" hidden><table class="res-table">
    <caption class="sr-only">Wyniki sprawdzenia</caption>
    <thead><tr><th scope="col">Wiersz</th><th scope="col">Status</th><th scope="col">Numer</th><th scope="col">Typ</th><th scope="col">NIP</th><th scope="col">Data</th><th scope="col">Uwagi</th></tr></thead>
    <tbody id="b-body"></tbody></table></div>
  <p class="privacy">🔒 Dane nie opuszczają Twojej przeglądarki – także wgrane pliki.</p>
</section>""",
    content="""
<h2>Do czego służy masowa weryfikacja</h2>
<p>Od 1 stycznia 2027 r. numer KSeF trafia do przelewów między czynnymi podatnikami VAT. Księgowość, która płaci dziesiątki faktur tygodniowo, nie sprawdzi każdego numeru ręcznie. Ten walidator przyjmuje całą listę naraz – prosto z Excela, z pliku CSV wyeksportowanego z programu, z rejestru faktur albo z wyciągu bankowego – i w ułamku sekundy pokazuje, które numery są poprawne, a które trzeba poprawić przed wysłaniem przelewów.</p>

<h2>Dwa tryby pracy</h2>
<div class="table-wrap"><table>
<thead><tr><th scope="col">Tryb</th><th scope="col">Dla kogo</th><th scope="col">Co robi</th></tr></thead>
<tbody>
<tr><th scope="row">Lista numerów</th><td>Płacący: księgowość przed wysłaniem paczki przelewów</td><td>Sprawdza każdy numer; jeśli wiersz nie zawiera rozpoznawalnego numeru, sprawdza cały wiersz i podaje przyczynę błędu</td></tr>
<tr><th scope="row">Wyciąg bankowy</th><td>Odbiorca płatności: kontrola wpływów i rozrachunków</td><td>Szuka numerów KSeF i identyfikatorów zbiorczych w tytułach przelewów i oznacza wiersze, w których płatnik nie podał numeru</td></tr>
</tbody></table></div>

<h2>Jak to działa – krok po kroku</h2>
<ol class="steps">
<li><strong>Wklej dane lub wgraj plik.</strong> Obsługujemy CSV (separator średnik, przecinek lub tabulator) i zwykły tekst. Plik nie jest nigdzie wysyłany – czyta go Twoja przeglądarka.</li>
<li><strong>Wyszukiwanie w tekście.</strong> W każdym wierszu szukamy wzorców 35-znakowych numerów KSeF, 36-znakowych numerów z KSeF 1.0 i identyfikatorów zbiorczych (z „IZ”), także gdy stoją w środku dłuższego tytułu, np. w komunikacie MPP. Nie musisz wskazywać kolumny.</li>
<li><strong>Weryfikacja.</strong> Każdy znaleziony numer przechodzi tę samą kontrolę co w <a href="/">pojedynczym walidatorze</a>: format, suma kontrolna CRC-8, NIP i data.</li>
<li><strong>Wyniki.</strong> Tabela pokazuje status, typ, NIP, datę i opis problemu. Możesz zostawić same problemy.</li>
<li><strong>Eksport.</strong> Pobierz CSV (UTF-8 z BOM, separator średnik – otwiera się poprawnie w polskim Excelu) albo skopiuj wyniki do schowka.</li>
</ol>

<h2>Co znaczą statusy</h2>
<div class="table-wrap"><table>
<thead><tr><th scope="col">Status</th><th scope="col">Znaczenie</th><th scope="col">Co zrobić</th></tr></thead>
<tbody>
<tr><td><span class="badge ok">Poprawny</span></td><td>Format, suma kontrolna, NIP i data się zgadzają</td><td>Można użyć w przelewie</td></tr>
<tr><td><span class="badge warn">Do sprawdzenia</span></td><td>Stary format KSeF 1.0 (36 znaków) albo początek numeru, który nie jest NIP-em</td><td>Potwierdź numer u wystawcy lub w KSeF</td></tr>
<tr><td><span class="badge bad">Błędny</span></td><td>Zła suma kontrolna, zły NIP, nieistniejąca data lub zły format</td><td>Skopiuj numer ponownie z UPO lub programu</td></tr>
<tr><td><span class="badge info">Brak numeru</span></td><td>W wierszu nie ma numeru KSeF ani identyfikatora zbiorczego</td><td>Przy płatności od czynnego podatnika VAT od 2027 r. – wyjaśnij z płatnikiem</td></tr>
</tbody></table></div>

<h2>Kontrola wyciągu bankowego po stronie odbiorcy</h2>
<p>Przepisy nakładają obowiązek podania numeru KSeF na płacącego, ale to odbiorca rozlicza wpływy. Tryb „Wyciąg bankowy” szybko pokaże, które wpłaty mają numer KSeF lub identyfikator zbiorczy, w których jest literówka, a w których numeru nie ma. Pamiętaj o wyjątkach: numer KSeF nie jest wymagany m.in. przy płatności od podatnika zwolnionego z VAT, od konsumenta oraz za faktury wystawione w trybie awaryjnym lub offline, które nie trafiły do systemu z powodu ogłoszonej awarii.</p>

<h2>Wskazówki dla dużych list</h2>
<ul>
<li>Narzędzie radzi sobie z tysiącami wierszy – limitem jest tylko pamięć przeglądarki.</li>
<li>Pliki XLSX zapisz najpierw jako CSV (Plik → Zapisz jako → CSV UTF-8).</li>
<li>Przy płatności za wiele faktur od jednego dostawcy rozważ <a href="/identyfikator-zbiorczy-ksef/">identyfikator zbiorczy</a> – w tytule zmieszczą się najwyżej trzy numery KSeF.</li>
<li>Gotowe numery wykorzystasz w <a href="/przelew-mpp-numer-ksef/">komunikacie MPP</a> lub w <a href="/">tytule przelewu</a>.</li>
</ul>
""",
    faq=[
        ("Czy mogę wgrać plik z Excela?", "Tak, w formacie CSV lub TXT. Plik XLSX zapisz najpierw jako „CSV UTF-8”. Plik czyta tylko Twoja przeglądarka – nie jest nigdzie wysyłany."),
        ("Czy muszę wskazać kolumnę z numerami?", "Nie. Narzędzie samo wyszukuje numery KSeF i identyfikatory zbiorcze w całym wierszu, także w środku dłuższego tytułu przelewu."),
        ("Jak otworzyć pobrany CSV w Excelu?", "Plik ma kodowanie UTF-8 z BOM i separator średnik, więc polski Excel otworzy go poprawnie, z polskimi znakami, po dwukrotnym kliknięciu."),
        ("Co oznacza „Brak numeru” w trybie wyciągu?", "W tytule tego przelewu nie znaleziono ani numeru KSeF, ani identyfikatora zbiorczego. Od 2027 r. przy płatnościach między czynnymi podatnikami VAT to sygnał do wyjaśnienia z płatnikiem."),
        ("Ile wierszy mogę sprawdzić naraz?", "Nie ma sztywnego limitu – tysiące wierszy sprawdzisz w kilka sekund. Wszystko liczy Twoje urządzenie."),
        ("Czy narzędzie sprawdza, czy faktury istnieją w KSeF?", "Nie. Sprawdza poprawność zapisu: format, sumę kontrolną CRC-8, NIP i datę. Istnienie faktury potwierdza tylko KSeF."),
    ],
    sources=[MF_NUM, DOC_NUM, MF_TERM, MBANK_IMPORT],
)
