# Teksty promocyjne – NumerKSeF (DO RĘCZNEJ PUBLIKACJI, nic nie zostało opublikowane)

Zasady: najpierw konkretna pomoc, link tylko jeden i na końcu, bez dat i kwot kar, bez obietnic „zgodności”. Przed publikacją przeczytaj regulamin grupy/subu (wiele zabrania autopromocji – wtedy pisz bez linku albo zapytaj moderatora). Publikuj z odstępem kilku dni, nie wszystko naraz. Odpowiadaj tylko w wątkach, gdzie ktoś faktycznie pyta o ten temat.

---

## 1. Forum / Q&A (forum.gofin.pl, forum.ops.pl – odpowiedź w wątku o numerze KSeF w przelewie)

**Kontekst:** wątek typu „Od stycznia numer KSeF w tytule przelewu – jak to robić przy kilku fakturach?”

> Z tego, co jest na stronie MF (ksef.podatki.gov.pl, zakładka o numerze KSeF i identyfikatorze zbiorczym), obowiązek dotyczy płatności od 1 stycznia 2027 r. między czynnymi podatnikami VAT, także w MPP. W praktyce wygląda to tak:
>
> 1. **Jedna faktura** – w tytule wpisujesz jej numer KSeF (35 znaków, np. `5265877635-20250826-0100001AF629-AF`). Jeśli zostaje miejsce, dopisz za nim zwykły numer faktury, żeby sprzedawcy łatwiej było rozpoznać wpłatę.
> 2. **Kilka faktur jednego sprzedawcy** – zamiast listy numerów podajesz identyfikator zbiorczy (też 35 znaków, z literami IZ po NIP). Generuje się go w Aplikacji Podatnika KSeF albo w programie połączonym z API KSeF; może to zrobić wystawca albo nabywca.
> 3. **MPP** – numer KSeF idzie w pole `/INV/` komunikatu, w miejsce dotychczasowego numeru faktury.
>
> Jedna praktyczna rzecz: ostatnie dwa znaki numeru KSeF to suma kontrolna CRC-8, więc literówkę (np. literę O zamiast zera) da się wykryć przed wysłaniem przelewu. Banki raczej nie będą tego sprawdzać za nas.
>
> Do szybkiego sprawdzenia numeru i ułożenia tytułu zrobiłem darmowe narzędzie (działa w przeglądarce, nic nie wysyła): https://numerksef.dpdns.org/
>
> To nie jest porada podatkowa – przy nietypowych sytuacjach (zaliczki, korekty) warto potwierdzić z księgową.

---

## 2. Reddit (r/PolskaFinanse lub r/Polska – odpowiedź na pytanie JDG)

**Kontekst:** post „Mam JDG na VAT, od 2027 numer KSeF w przelewach – co muszę zmienić?”

> Krótko, z perspektywy kogoś, kto płaci faktury kontrahentom:
>
> - Liczy się **data płatności**, nie wystawienia faktury – przelew zrobiony w styczniu 2027 za fakturę z grudnia opisujesz już po nowemu (tak to czyta większość poradników, MF pisze o „płatnościach dokonanych od 1 stycznia 2027”).
> - Dotyczy to płatności między **czynnymi podatnikami VAT** za faktury z KSeF. Jak płacisz komuś zwolnionemu z VAT albo konsumentowi – nie dotyczy.
> - Numer KSeF **nie jest** numerem faktury (FV/1/2027) ani nie ma go w samym pliku XML – dostajesz go z KSeF/UPO, z programu do faktur albo spod kodu QR na PDF-ie.
> - Najwięcej roboty to nie sam przelew, tylko żeby numer KSeF był przy każdej fakturze kosztowej w miejscu, z którego płacisz (program księgowy, eksport do banku).
>
> Jeśli wklejasz numery ręcznie, sprawdzaj je – mają sumę kontrolną, więc jeden zły znak da się wyłapać. Ja używam do tego tego darmowego walidatora (bez rejestracji, dane zostają w przeglądarce): https://numerksef.dpdns.org/
>
> (Nie jestem doradcą podatkowym, to praktyka, nie porada.)

---

## 3. Grupa na Facebooku – małe firmy / JDG

> 📌 **Ściąga: co wpisać w tytule przelewu od 2027 r. (KSeF)**
>
> Dużo pytań o to w grupie, więc zebrałam w jednym miejscu (na podstawie informacji MF na ksef.podatki.gov.pl):
>
> ✅ Płacisz za **jedną fakturę** z KSeF innej firmie na VAT → w tytule **numer KSeF** tej faktury (35 znaków). Możesz dopisać po nim swój numer faktury.
> ✅ Płacisz **kilka faktur jednego dostawcy** jednym przelewem → **identyfikator zbiorczy** z KSeF zamiast listy numerów.
> ✅ Płacisz w **MPP (split payment)** → numer KSeF w polu numeru faktury w komunikacie MPP.
> ❌ Nie dotyczy płatności dla firm zwolnionych z VAT i dla konsumentów.
>
> Gdzie szukać numeru KSeF: w programie do faktur, w Aplikacji Podatnika KSeF, w UPO albo pod kodem QR na PDF-ie faktury.
>
> Tip: numer ma na końcu sumę kontrolną – jeśli przepisujesz go ręcznie, sprawdź go przed wysłaniem. Darmowy walidator + generator tytułu przelewu i komunikatu MPP (bez logowania, nic nie jest wysyłane na serwer): https://numerksef.dpdns.org/
>
> Jeśli ktoś ma inną sytuację (zaliczki, korekty) – piszcie w komentarzach, uzupełnię.

---

## 4. Grupa na Facebooku – księgowe / biura rachunkowe

> **Dla biur: szybka kontrola numerów KSeF z wyciągu bankowego**
>
> Od 2027 r. klienci będą wpisywać numery KSeF (albo identyfikatory zbiorcze) w tytułach przelewów, więc przy uzgadnianiu wpłat pojawi się nowy rodzaj błędów: literówki w 35-znakowym numerze, O zamiast 0, ucięte znaki, numer faktury zamiast numeru KSeF.
>
> Kilka obserwacji z testowania:
> 1. Numer KSeF i identyfikator zbiorczy mają **sumę kontrolną CRC-8** (dwa ostatnie znaki) – błąd w jednym znaku zwykle da się wykryć automatycznie.
> 2. Pierwsze 10 cyfr numeru to **NIP sprzedawcy**, potem data – to szybki test, czy klient nie wkleił numeru z innej faktury.
> 3. W komunikacie MPP numer siedzi w `/INV/`, a w zwykłym przelewie może być w dowolnym miejscu tytułu – przy imporcie wyciągu warto szukać wzorca, a nie stałej pozycji.
>
> Zrobiłam/zrobiłem darmowe narzędzie, które wyciąga numery KSeF z wklejonego wyciągu lub CSV, sprawdza każdy i eksportuje wynik do CSV (wszystko liczy się w przeglądarce, plik nie trafia na żaden serwer): https://numerksef.dpdns.org/sprawdz-wiele-numerow-ksef/
>
> Chętnie przyjmę uwagi, jakie formaty wyciągów warto jeszcze obsłużyć.

---

## 5. LinkedIn / GoWork – post profesjonalny

> **Numer KSeF w przelewie: mała zmiana, która może zatrzymać rozliczenia**
>
> Od płatności dokonanych 1 stycznia 2027 r. firmy będące czynnymi podatnikami VAT, płacąc za e-faktury z KSeF, podają w tytule przelewu numer KSeF faktury albo identyfikator zbiorczy – także w MPP (źródło: ksef.podatki.gov.pl).
>
> Z rozmów z przedsiębiorcami wynika, że problemem rzadko jest sam przepis. Problemem jest proces:
> • czy numer KSeF trafia do systemu, z którego robimy przelewy,
> • kto i gdzie generuje identyfikator zbiorczy przy płatnościach za kilka faktur,
> • jak dział należności dopasuje wpłatę, gdy klient wkleił numer z błędem.
>
> Warto przećwiczyć jeden „dzień płatności” jeszcze w tym roku: zwykły przelew, MPP i przelew zbiorczy.
>
> Przygotowałem bezpłatny zestaw narzędzi, który pomaga w tym teście – walidator numeru KSeF, generator komunikatu MPP i masowe sprawdzanie numerów z wyciągu. Działa w przeglądarce, bez rejestracji i bez wysyłania danych: https://numerksef.dpdns.org/
>
> Jak Wasze firmy przygotowują się do tej zmiany?
>
> #KSeF #eFaktura #finanse #księgowość #MŚP
