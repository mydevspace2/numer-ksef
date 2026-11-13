# KSeF free-tool research — competitors, gaps, build list, specs

Research date: 13 Nov 2026. Tools: web_search + web_fetch only (plus local Python to verify checksums and to read the official FA(3) XSD).
Baseline: the user's live site https://mydevspace2.github.io/numer-ksef/ already does a multi-line KSeF number check (format + CRC-8 + NIP/date) and builds one plain transfer title, with an explanation section. It does **not** do IZ (identyfikator zbiorczy) validation, MPP split-payment messages, XML input, QR links, or file/CSV input.

**What I could not get:** search volume figures. No keyword tool was reachable, so the ranking below rests on (a) how many free tools already serve each query, (b) how well, and (c) how directly the query is tied to the 1 Jan 2027 deadline. Treat the keyword lists as candidate phrases to check in Google Search Console or Keyword Planner, not as measured demand.

---

## 0. Legal timeline that drives demand (sourced)

- **From 1 Jan 2027, KSeF number or collective ID in payments.** Applies to payments between active VAT payers, including MPP. MF: "Do końca 2026 r. odroczony jest obowiązek podawania numeru KSeF faktury podczas płatności pomiędzy podatnikami czynnymi (art. 108g …) oraz w ramach MPP." https://ksef.podatki.gov.pl/informacje-ogolne-ksef-20/podstawy-prawne-oraz-kluczowe-terminy/
- **MF on the KSeF number and IZ (page modified 10.11.2026):**
  - "płatności za pojedynczą fakturę - podawany będzie numer KSeF faktury"
  - "płatności za więcej niż jedną fakturę - … zbiorczy identyfikator … lub kilka numerów KSeF lub kilka zbiorczych identyfikatorów (przy uwzględnieniu ograniczeń technicznych pola zawierającego tytuł płatności)"
  - MPP: "w komunikacie przelewu MPP podaje się między innymi numer KSeF faktury" and "zamiast wpisywania okresu … podaje identyfikator zbiorczy"
  - IZ limits: max 500 KSeF numbers per IZ (50 in Aplikacja Podatnika); one invoice can be in at most 132 IZs per context; all invoices in an IZ must have the same seller (Podmiot1).
  - Exemptions: invoices issued "w trybie awaryjnym" and offline invoices "nie zostały wprowadzone do systemu w związku z ogłoszoną awarią".
  - Source: https://ksef.podatki.gov.pl/informacje-ogolne-ksef-20/numer-ksef-i-zbiorczy-identyfikator/
- **10 000 zł exemption ends.** The 10 000 zł/month "wykluczeni cyfrowo" exemption and invoices from cash registers end on 31 Dec 2026 (same MF timeline page). From 1 Jan 2027, KSeF applies to all businesses that invoice other businesses.
- **Penalties likely move to 2028 (not yet law).** On 6 Nov 2026 the Sejm passed druk 3245, which moves the art. 106ni penalties from 1 Jan 2027 to 1 Jan 2028. It is in the Senate and is meant to take effect on 31 Dec 2026, so it is **not yet published law**. Sources: https://www.prawo.pl/podatki/mf-nie-bedzie-kar-za-bledy-w-ksef-do-konca-2027-roku,1552882.html and https://www.gov.pl/web/finanse/rada-ministrow-za-odroczeniem-kar-za-bledy-w-ksef-i-przedluzeniem-odwrotnego-obciazenia-vat (MF, 20.10.2026). Any "does KSeF apply to me" tool must show this as pending, with a date stamp.

---

## 1. Competitor analysis

### 1a. The four named sites

**ksefnarzedzia.pl/pl/numer-ksef/** (Radif Partners)
- **What it offers:**
  - A KSeF number validator that splits the number into NIP, date and ID and checks CRC-8.
  - An inline "offline deadline" calculator (counts working days, skips holidays).
  - Sister tools: an FA(3) XML reader, a 10 000 zł limit counter, an offline/outage mode calculator, a penalties page, a QR-link parse/build tool (`/pl/kod-qr-ksef/`), and "Kogo obejmuje / Od kiedy / dla małych firm" pages.
  - Polish and English, an embeddable widget page (`/pl/widget/`), a legal citation for every claim, and "everything runs in the browser".
- **Weaknesses:**
  - The validator takes **one number at a time**: no list, no CSV.
  - It explicitly does **not validate the IZ**: "zbiorczy identyfikator ma inną budowę".
  - **No transfer title or MPP builder** on the number page.
  - No export or copy-all.
  - The page is long and text-heavy, so the tool sits above a wall of text.
- **Overall:** the strongest competitor on authority and breadth. Our angle has to be workflow depth (from number to payment), not more explanation.

**ksef.shipailab.com/numer-ksef** (Ship AI Solutions, "Faktury KSeF" mobile app)
- **What it offers:** a pure article (guide) that funnels readers into a paid or waitlist mobile app. No on-page tool.
- **Weaknesses:**
  - There is no validator at all.
  - It is US-LLC content marketing.
  - It does say MPP is affected but gives no MPP format.
- **Overall:** easy to beat for any "tool" intent query.

**czytnikfaktur.com/numer-ksef/** (webinstudio, Korea; shows ads, with an "Ustawienia prywatności / reklamy" link)
- **What it offers:**
  - A guide plus a link to its FA(3) XML reader.
  - The reader validates the KSeF number **only when the number is in the filename or an UPO is loaded**, and has a manual "Sprawdź numer" field.
  - NIP checksum on seller and buyer.
  - It covers the 140-character title limit, "up to three 35-character numbers separated by commas" (citing the MF FAQ), and the IZ.
- **Weaknesses:**
  - No standalone number or IZ validator page.
  - No title or MPP builder.
  - It rejects 36-character KSeF 1.0 numbers as "zły format".
  - It carries ads.
  - Its PL/EN/UK pages are for a general audience.

**einvoicetool.com/pl/poradnik/numer-ksef** (multi-country e-invoice viewer, WordPress)
- **What it offers:**
  - A guide that uses a **fictional example number** (`1234567890-20260302-0A1B2C3D4E5F-7C`), not the MF one.
  - A CTA to its FA(3) viewer, a "walidator faktury" and print pages.
- **Weaknesses:**
  - No number validator.
  - No payment-title tool.
  - Generic and multi-country, so weak Polish-specific depth.

### 1b. Other free KSeF tool sites found

| Site | What it does | Weak / missing |
|---|---|---|
| **ranx.pl/numer-ksef-w-przelewie/** (CRE 8 sp. z o.o., finance-comparison site) | Number + CRC check. Plain and **MPP title builder**. **Bulk mode** (paste rows "numer;kwota;opis"). White-list (wykaz VAT) check when NIP and account are given. Explains why the ZBP payment QR cannot carry a KSeF number (title max 32 chars). | The **closest competitor to the user's site plus an MPP builder**. Buried in a bank-ranking site with an ad slot. No IZ-specific validation shown. No XML input. No CSV/file export. Copy is long. |
| **ksef.almmity.com/narzedzia/** | Free suite: white-list check with PDF proof, "Tytuł przelewu z numerem KSeF" (plain + MPP + IZ), FA(3) validator, FA(3) generator, correction generator, XML summary, NIP checksum, interest calculator, payment demand letter. | A funnel for a paid "KSeF Płatności" product. Tools are spread across separate pages. Generic UX. |
| **przelewyksef.pl** | Upload XML/ZIP from KSeF and get an **Elixir-O (PLI) bank import file** with the KSeF number in titles, MPP where `P_18A`=1, due dates, white-list check. Free tier is client-side. Reads the KSeF number from the filename or `_metadata.json` in the KSeF export ZIP. | Needs the XML. Nothing for "I just have the number". IZ support is only "coming in Pro". Admits banks have not published KSeF-in-MPP rules yet. |
| **klarbon.app** (`/ksef-qr-code-checker`, `/ksef-number-in-payments`) | QR checker from photo/PDF/link, comparing the SHA-256 with the XML. **Bank-statement checker**: tags each transfer as KSeF number / IZ / likely typo / none, and matches it to invoices. | English-first, beta. Polish SEO weak. |
| **ai-gov.pl/ksef/** (Jerzy Głowacki, open source) and **gzosip.bochnia.pl dekoder-qr-ksef** | QR decoders (paste an image, check the domain is `qr.ksef.mf.gov.pl`). | Bare UIs. No education. No XML hash compare (gzosip). |
| **odswiezona.pl/api-ksef** | A paid/limited API for building a QR link from XML. | API, not an end-user tool. |
| **XML viewers / visualisers** (saturated): systemfaktur.pl, ksefusz.pl (Pragma, FA1–3, FA_RR, PEF, UPO, 5 languages), wizualizacjaksef.pl, invoiceferry.com/pl, docfig.com (multi-file, ZIP, Excel), alltoolio.com (ZIP, Excel, builds KOD I), pdfowo.pl (uses the official MF visualisation library), einvoicechecker.com, ksef-pl.com (JSON export), pdfdoksef.pl, tablixa.app, autum8.co, xmlvalid.com | Open FA(3) XML, render it, print or save as PDF. Many are client-side, many do bulk, ZIP, Excel and QR. | **The market is saturated.** A new generic viewer will not rank. The only differentiator left is a viewer that ends in a **payment action** (copy the account, amount, KSeF title or MPP message). |
| **XSD validators** (saturated): ksefuj.to (open-source WASM, 42 business rules), ksefwalidator.pl, weryfikacjafaktur.pl, ksefka.com, aidoks.eu, invoicenavigator.eu, ksefgpt.pl, ewidencjafaktur.pl | FA(3) schema and business-rule validation. | Do not build one. |
| **IZ tools**: kseftools.pl (demo with an account), Deloitte taxCube (paid, bulk), A-Cube API `/collective-identifiers/validate` (paid API) | Generate or decode the IZ via the KSeF API, which needs auth. | **No free, client-side, SEO-oriented IZ format/checksum validator page was found.** Generating or decoding an IZ needs a KSeF login, so a free site can only validate format and CRC. |

---

## 2. Gap analysis (candidates evaluated)

| Candidate | Saturation | Gap | Verdict |
|---|---|---|---|
| **MPP / split-payment message builder** with the KSeF number (`/VAT/…/IDC/…/INV/…/TXT/…`) | Low–medium: ranx, almmity, przelewyksef (XML only) | Nobody does a clean, mobile-first builder that is validated field by field against the bank spec: VAT format `10n,2n` with a comma, VAT ≤ gross, `/TXT/` ≤ 33, total ≤ 140, forbidden characters, IZ allowed in `/INV/`, 35-character line split preview, and a "PRZEKAZANIE WLASNE" variant. Banks are changing their forms now (mBank 19.10.2026). | **BUILD #1** |
| **IZ (identyfikator zbiorczy) validator / decoder** | Very low for free client-side | Free pages explain the IZ but none validate it. Verified: the MF example `1111111111-IZ202607-65ED02180000-E7` passes the **same CRC-8** as the KSeF number. | **BUILD #2** (can be a mode of the existing validator plus its own landing page) |
| **Bulk / CSV KSeF number validator with export** (plus a "check my bank statement titles" mode) | Low: ranx bulk is paste-only, klarbon is EN/beta | Accountants paste columns from Excel or JPK and want a downloadable result (CSV with status per row, extracted NIP and date, error reason). | **BUILD #3** (extends the current tool) |
| **FA(3) XML → payment data** (drop XML, get account, amount, due date, KSeF title or MPP message) | Medium: przelewyksef does a bank file; viewers do not do payment | Viewers stop at "print PDF". Nobody gives a "copy payment fields" card for a one-off payer without a bank file. | **BUILD #4** (narrow viewer, not a general one) |
| **KSeF QR (KOD I) link decoder / generator** | Medium–high: ksefnarzedzia, klarbon, ai-gov.pl, gzosip, alltoolio | Only possible edges: phone-camera scan plus an anti-phishing explanation plus XML-hash compare, all in Polish. | **BUILD #5** (lower priority) |
| **"Does KSeF apply to me from 2027?" JDG checker** | Medium: ksefnarzedzia (Kogo obejmuje, Limit 10 000), wlimicie.pl, przewodnikjdg.pl, many articles | Demand will spike in Dec 2026 and Jan 2027. A short decision-tree tool combining *issuing* duties with *paying* duties (KSeF number in transfers) is rare: competitors split these. Legal status is in flux (Senate), so it needs a dated "stan prawny". | **BUILD #6** (content-tool hybrid) |
| **NIP checksum validator** | Very high (almmity, ksef-pl.com, countless generic ones) | None as a standalone page. | Embed as a component only |
| **Generic FA(3) viewer / PDF** | Very high (≥ 12 free tools) | — | Do not build standalone |
| **Payment QR (ZBP 2D) with KSeF number** | — | **Impossible.** The ZBP 2D standard caps "Tytuł płatności" at 32 characters, and a KSeF number has 35. | Use as an FAQ/content angle only |

**ZBP 2D QR title limit.** Rekomendacja ZBP "Standard 2D" (2013) says: "Tytuł płatności — Maksymalnie 32 znaki", "Nazwa Odbiorcy — Maksymalnie 20 znaków", "Maksymalna liczba znaków w 2D : 160". Source: https://www.zbp.pl/getContentAsset/806da831-e7e0-43e8-b361-c45f922cf529/1b52933d-ceff-4d97-bee2-094d491a3634/2013-12-03_-_Rekomendacja_-_Standard_2D.pdf?language=pl

---

## 3. Ranked build list (with Polish keywords and H1s)

Suggested URL structure on the existing site: `/numer-ksef/` (existing), plus sibling pages below. Each page: the tool above the fold, then a short "jak to działa", the spec table with sources, an FAQ, and cross-links. Client-side only, with no data leaving the browser; state that prominently.

### #1. MPP split-payment message builder with KSeF number
- **URL:** `/przelew-mpp-numer-ksef/`
- **H1:** **Komunikat przelewu MPP z numerem KSeF – generator split payment 2027**
- **Target keywords:** przelew podzielony numer KSeF · split payment numer KSeF · komunikat MPP numer KSeF · jak wypełnić przelew split payment 2027 · /VAT/ /IDC/ /INV/ /TXT/ · numer KSeF w polu numer faktury MPP · przelew MPP identyfikator zbiorczy · przekazanie własne MPP
- **Why first:** it is a natural extension of the existing tool, uses the same CRC code, and is under-served. Every MPP payer must change behaviour on 1 Jan 2027. ranx is the only real rival and it is buried in a bank-ranking site.
- **Features:**
  - Inputs: VAT amount, gross amount (optional, for the VAT ≤ gross check), seller NIP, KSeF number **or** IZ **or** (legacy) invoice number, optional text.
  - Live validation per field.
  - Output 1: the one-line `Ustrd` string.
  - Output 2: a 4-line layout (the Deutsche Bank style).
  - Output 3: a 35-character line-split preview (Elixir).
  - Copy buttons per field, because bank web forms now have separate fields (mBank: "w polu Numer faktury będzie można wprowadzić również numer faktury KSeF" and "pole Tytuł przelewu zastąpimy polem Dodatkowe dane do faktury", https://www.mbank.pl/komunikaty/klienci-firmowi/planowane-zmiany-w-przelewach-podzielonych-split-payment).
  - Date switch: a payment before 1 Jan 2027 may use the invoice number, from 1 Jan 2027 the KSeF number.
  - Optional bulk paste.

### #2. Collective identifier (IZ) validator
- **URL:** `/identyfikator-zbiorczy-ksef/`
- **H1:** **Identyfikator zbiorczy KSeF – sprawdź poprawność i rozłóż na części**
- **Target keywords:** identyfikator zbiorczy KSeF · zbiorczy identyfikator płatności KSeF · sprawdź identyfikator zbiorczy · IZ KSeF przykład · identyfikator zbiorczy w tytule przelewu · ile faktur w identyfikatorze zbiorczym · jak wygenerować identyfikator zbiorczy
- **Features:**
  - Accept the IZ.
  - Show NIP (with checksum), year-month of creation, technical part, CRC.
  - Explain clearly that only KSeF can decode which invoices it covers.
  - Point to Aplikacja Podatnika for generation.
  - Show the limits (500 / 50 / 132).
- Also: make the existing `/numer-ksef/` validator auto-detect IZ and KSeF number in one box.

### #3. Bulk / CSV validator with export, plus bank-statement title checker
- **URL:** `/sprawdz-wiele-numerow-ksef/` (or a tab on `/numer-ksef/` with its own landing page)
- **H1:** **Sprawdź wiele numerów KSeF naraz – lista, CSV, wyciąg bankowy**
- **Target keywords:** sprawdzenie numerów KSeF z pliku · walidator numerów KSeF CSV · lista numerów KSeF Excel · numer KSeF w wyciągu bankowym · przelew bez numeru KSeF · weryfikacja tytułów przelewów KSeF
- **Features:**
  - Paste or drop a CSV/TXT/XLSX column (start with CSV/TXT; XLSX via SheetJS is optional).
  - Auto-extract every 35/36-character candidate anywhere in each row, using a regex over free text.
  - Per-row status: OK / IZ / bad CRC / bad NIP / bad date / bad format / not found.
  - Column auto-detect.
  - Download CSV (UTF-8 with BOM for Excel PL) and copy.
  - "Statement mode": paste bank titles and flag rows with no KSeF number (the receiving side).

### #4. FA(3) XML → payment card ("zapłać fakturę z KSeF")
- **URL:** `/przelew-z-faktury-xml-ksef/`
- **H1:** **Faktura XML z KSeF → gotowe dane do przelewu (z numerem KSeF i MPP)**
- **Target keywords:** jak zapłacić fakturę z KSeF · dane do przelewu z faktury XML · numer rachunku z faktury KSeF · faktura KSeF XML przelew · podgląd faktury KSeF przelew · numer KSeF z nazwy pliku
- **Features:**
  - Drop one or more XML files (and the KSeF export ZIP if feasible).
  - Read seller name and NIP, `P_2`, `P_1`, `P_15`, VAT sum, `P_18A`, `NrRB`, `TerminPlatnosci/Termin`.
  - Take the KSeF number from the filename (or let the user paste it), validated by CRC.
  - Output a payment card with copy buttons, plus an MPP message when `P_18A`=1.
  - A minimal readable summary only, **not** a full visualiser (that market is saturated).

### #5. KSeF QR verification link — decoder and KOD I generator
- **URL:** `/kod-qr-ksef/`
- **H1:** **Kod QR KSeF – odczytaj link weryfikacyjny i sprawdź, czy faktura nie jest podróbką**
- **Target keywords:** kod QR KSeF weryfikacja · jak sprawdzić kod QR na fakturze KSeF · link qr.ksef.mf.gov.pl · KOD I KSeF · kod QR OFFLINE CERTYFIKAT · fałszywy kod QR faktura
- **Features:**
  - Paste a link, or scan with the phone camera (BarcodeDetector / jsQR fallback), or drop an image.
  - Parse environment, NIP (checksum), date, hash.
  - **Domain allow-list warning** (anti-phishing).
  - Optional XML drop: compute SHA-256/Base64URL and compare, then build KOD I and render the QR (ISO/IEC 18004, label = KSeF number or "OFFLINE").
  - KOD II: parse and explain only. Never ask for a private key.

### #6. "Czy KSeF mnie dotyczy od 2027?" checker for JDG
- **URL:** `/ksef-od-2027-jdg/`
- **H1:** **KSeF od 1 stycznia 2027 – czy dotyczy Twojej JDG? Sprawdź w 30 sekund**
- **Target keywords:** KSeF dla JDG 2027 · KSeF od 2027 kogo dotyczy · KSeF limit 10 000 zł koniec · czy JDG musi mieć KSeF · KSeF zwolniony z VAT 2027 · KSeF kasa fiskalna faktura 2027 · kary KSeF 2028
- **Features:**
  - 4–6 questions: invoices to firms? VAT active or exempt? monthly invoiced B2B sales ≤ 10 000 zł in 2026? invoices from a cash register or receipts with NIP? do you pay suppliers by transfer?
  - Result: a dated checklist of what changes on 1 Jan 2027 (issuing in KSeF, receiving, KSeF number in transfers only if both sides are VAT-active, MPP).
  - The penalties line shown with its status ("uchwalone przez Sejm 6.11.2026, w Senacie").
  - CTA to tools #1–#3.
  - Must carry a "stan prawny na …" date and sources, and needs updating after the Senate and President act.

(NIP validator: ship it as a shared component inside #1–#5 and show checksum results inline. No dedicated page.)

---

## 4. Exact technical specs for client-side JS

### 4.1 KSeF number — structure, regex, CRC-8 (official)
Source: https://raw.githubusercontent.com/CIRFMF/ksef-docs/main/faktury/numer-ksef.md
> "Zawsze ma długość **35 znaków**" · `9999999999-RRRRMMDD-FFFFFFFFFFFF-FF` · "`FFFFFFFFFFFF` – część techniczna składająca się z 12 znaków w zapisie szesnastkowym, tylko [0–9 A–F], wielkie litery" · "`FF` – suma kontrolna CRC-8" · "**Polinom:** `0x07`" · "**Wartość początkowa:** `0x00`" · "Format wyniku: 2-znakowy zapis szesnastkowy (HEX, wielkie litery)" · Validation: "Rozdzielenie części danych (32 znaki) i sumy kontrolnej (2 znaki)".

**FA(3) XSD pattern (`TNumerKSeF`).** This is what an XML field accepts, so it also **accepts the legacy 36-character form with an extra hyphen** and **non-NIP prefixes** (`M\d{9}`, `[A-Z]{3}\d{7}`). Source: https://raw.githubusercontent.com/CIRFMF/ksef-docs/main/faktury/schemy/FA/schemat_FA(3)_v1-0E.xsd (a local copy is at `work/fa3.xsd`).
```
([1-9]((\d[1-9])|([1-9]\d))\d{7}|M\d{9}|[A-Z]{3}\d{7})-(20[2-9][0-9]|2[1-9][0-9]{2}|[3-9][0-9]{3})(0[1-9]|1[0-2])(0[1-9]|[1-2][0-9]|3[0-1])-([0-9A-F]{6})-?([0-9A-F]{6})-([0-9A-F]{2})
```
**Recommendation:**
- Primary validation uses the 35-character KSeF 2.0 form.
- Recognise 36-character KSeF 1.0 numbers as "stary format KSeF 1.0", not as "invalid". czytnikfaktur notes that the API keeps 36-character compatibility.
- If the prefix is not a valid NIP but matches `M\d{9}` or `[A-Z]{3}\d{7}`, show a warning, not an error.

```js
function crc8(str){ // poly 0x07, init 0x00, over ASCII bytes of first 32 chars (hyphens included)
  let c = 0;
  for (const ch of str) { c ^= ch.charCodeAt(0);
    for (let i=0;i<8;i++) c = (c & 0x80) ? ((c << 1) ^ 0x07) & 0xFF : (c << 1) & 0xFF; }
  return c.toString(16).toUpperCase().padStart(2,'0');
}
const KSEF_RE = /^(\d{10})-(\d{4})(\d{2})(\d{2})-([0-9A-F]{12})-([0-9A-F]{2})$/;
const IZ_RE   = /^(\d{10})-IZ(\d{4})(\d{2})-([0-9A-F]{12})-([0-9A-F]{2})$/;
const isValid = s => s.length===35 && crc8(s.slice(0,32)) === s.slice(33);
// free-text extraction for bulk/statement mode:
const FIND_RE = /\b\d{10}-(?:\d{8}|IZ\d{6})-[0-9A-F]{6}-?[0-9A-F]{6}-[0-9A-F]{2}\b/gi;
```
Normalise input before checking: trim, uppercase, map Unicode dashes (– — ‑) to "-", and remove internal spaces. Tell the user which repair was applied, because a CRC failure after normalisation usually means O↔0 or I↔1.

**Verified with the code above (Python port, run 13.11.2026):**

| Example | Result |
|---|---|
| `5265877635-20250826-0100001AF629-AF` (MF docs) | ✔ CRC AF |
| `5265877635-20250709-0100E01D6840-3C` (MF QR slide) | ✔ |
| `1111111111-IZ202607-65ED02180000-E7` (MF IZ example) | ✔ CRC E7 — **IZ uses the same CRC-8** |
| `9510001233-20261102-01A3F0C2B7D4-B8` (przelewyksef sample) | ✔ |
| `3786417439-20260928-AB12CD34EF56-78` (mBank spec example) | ✘ CRC would be 3A, and the NIP checksum is also invalid. Bank examples are illustrative and the tool would rightly reject them. Worth an FAQ line: "przykłady z instrukcji banków nie są prawdziwymi numerami". |

### 4.2 Collective identifier (IZ)
- **Official format:** `9999999999-IZRRRRMM-FFFFFFFFFFFF-FF`. Parts: "NIP kontekstu uwierzytelnienia generującego…", "oznaczenie „IZ” oraz rok, miesiąc wygenerowania", "część techniczna składająca się z 12 znaków", "suma kontrolna (wartość wyliczana automatycznie)". Source: MF graphic PDF https://ksef.podatki.gov.pl/media/2z4jjjce/ksef-identyfikato-zbiorczy.pdf. A newer MF graphic dated 09.11.2026 labels the first part "NIP sprzedawcy": https://ksef.podatki.gov.pl/media/omem3la2/grafika-ksef-identyfikator-zbiorczy-09112026.pdf.
- **Official example:** `1111111111-IZ202607-65ED02180000-E7`, from the KSeF 2.0 OpenAPI spec as quoted by czytnikfaktur.com/zbiorczy-identyfikator-platnosci-ksef/ and fakturownia.pl. It **passes CRC-8 0x07/0x00** (verified above).
- **Limits:** 2–500 numbers (50 in Aplikacja Podatnika), max 132 IZs per invoice per context, same seller. Source: MF numer-ksef page (§0).
- **Separate concept:** the FA(3) `IPKSeF` element ("Identyfikator płatności Krajowego Systemu e-Faktur") is a different **13-character** ID: pattern `[0-9]{3}[a-zA-Z0-9]{10}`, used in `LinkDoPlatnosci` (`…?IPKSeF=…`). Do not confuse it with the IZ. Source: FA(3) XSD.

### 4.3 NIP checksum
Weights `6,5,7,2,3,4,5,6,7`; the sum mod 11 must equal the 10th digit; remainder 10 means invalid. As described on czytnikfaktur.com/numer-ksef/ (which cites the MF C# client). Verified: the MF example NIPs 5265877635 and 1111111111 pass.
```js
const nipOk = n => /^\d{10}$/.test(n) && (()=>{const w=[6,5,7,2,3,4,5,6,7];
  const s=w.reduce((a,x,i)=>a+x*+n[i],0)%11; return s!==10 && s===+n[9];})();
```
**Date part:** check that it is a real calendar date (handle leap years), not in the future relative to the user's clock, and ≥ 2022. The XSD year range is 2020–9999. For KSeF 2.0 numbers, expect dates from Feb 2026 onwards; earlier dates are KSeF 1.0 or test numbers, so show a warning, not an error.

### 4.4 MPP split-payment message (bank format, KSeF-aware)
**Primary source:** mBank MultiCash pain.001.001.09 spec v2.0.7 (29.09.2026), §3 "Płatność podzielona – opis szczegółów płatności w polu `<Ustrd>`", https://www.mbank.pl/pdf/msp-korporacje/bankowosc-elektroniczna/multicash-pain00100109-pl.pdf

- **Format:** `/VAT/10n,2n/IDC/14x/INV/35x/TXT/33x` in `<Ustrd>` (**140a** total).
- **Rules:**
  - "Obowiązkowe jest zachowanie kolejności poszczególnych słów kodowych. Każde słowo kodowe może wystąpić wyłącznie jeden raz."
  - "Niedozwolone są spacje pomiędzy słowem kodowym a znakiem."
- **`/VAT/` (M):** "Kwota podatku VAT … separatorem pomiędzy częścią całkowitą kwoty a częścią dziesiątą jest znak przecinka „,”. np. 23,00". "Pole wymagane oraz >0,00 i <= kwocie zapłaty". For an own transfer, gross = VAT.
- **`/IDC/` (M, 14x):** "Identyfikator dostawcy towaru lub usługodawcy (płatnika podatku VAT, wystawcy faktury)", or the client's own ID for "przekazanie własne".
- **`/INV/` (M, 35x):** "Numer faktury albo numer (identyfikator) KSeF". It holds one of:
  - for an invoice outside KSeF, e.g. `/INV/2027/01/25/1`
  - for an invoice in KSeF, e.g. `/INV/3786417439-20260928-AB12CD34EF56-78`
  - for many invoices outside KSeF, the period
  - for many KSeF invoices, the identyfikator zbiorczy, e.g. `/INV/3786417439-IZ202708-AB12CD34EF56-78`
  - "PRZEKAZANIE WLASNE" for transfers between the same client's VAT accounts
- **`/TXT/` (O, 33x):** "Dowolny tekst dotyczący płatności (Maksymalnie do 33 znaków alfanumerycznych)".
- **Examples (verbatim):**
  - `/VAT/23035,90/IDC/3786417439/INV/3786417439-20260928-AB12CD34EF56-78/TXT/dowolny tekst`
  - `/VAT/75809,43/IDC/3786417439/INV/3786417439-IZ202708-AB12CD34EF56-78/TXT/dowolny tekst`
- **Allowed characters in payment details:** "0-9, a-z, A-Z, &%()-{}/,. oraz polskie znaki". Forbidden: ": * ; ‘ “ ! + ? | #".
- **Optional category code:** `<CtgyPurp><Cd>VATX</Cd>` for MPP (pain.001).
- **Elixir/CSV import (mBank):** "Dla płatności w MPP, w polu „tytuł” muszą się znaleźć obowiązkowo 3 słowa kodowe (VAT, IDC, INV) … w ściśle określonej kolejności". The VAT amount "może zajmować od 4 do 13 znaków i mieścić się w przedziale od 0,01 do 9999999999,99 PLN". Document code "dla MPP musi być równy „53”" (51 for normal transfers). The title is split into sections of "maksymalnie 35 znaków na sekcję" joined by `|`. Source: https://www.mbank.pl/firmy/uslugi-serwis-transakcyjny/import-przelewow
- **Manual-entry layout:** Deutsche Bank's 4-line form: "Linia 1:/VAT/1230,00 · Linia 2:/IDC/1234567890 · Linia 3:/INV/ABC123 · Linia 4:/TXT/dodatkowy opis". "/TXT/ is optional and if is used must be the last one". Source: https://www.deutsche-bank.com.cn/poland/documents/kk/platnosci-split-informacja-dla-klientow.pdf
- **Implementation notes:**
  - A KSeF number exactly fills `/INV/` (35x), so the seller's own invoice number (`P_2`) can only go in `/TXT/` (≤ 33). This approach is used by przelewyksef.pl and ranx.pl. It is their convention, not a legal requirement.
  - Total length = 5+len(VAT)+5+len(NIP)+5+35 (+5+len(TXT)), which must be ≤ 140.
  - przelewyksef notes that banks have not all published KSeF-in-MPP rules, so tell users to test one transfer first.
  - **Legal basis for the switch:** MF's numer-ksef page (§0) and art. 108a ust. 3 pkt 3 from 1 Jan 2027, cited by czytnikfaktur and shipailab.

**Plain (non-MPP) transfer title.** There is no prescribed syntax. MF only says one number, or an IZ, or several numbers/IZs "przy uwzględnieniu ograniczeń technicznych pola". The bank title field is usually 140 characters (mBank `Ustrd` 140a), so at most 3 numbers fit (3×35 plus 2 separators = 107; a 4th does not fit). Recommendation: KSeF number first, then the seller's invoice number if space remains. czytnikfaktur attributes the "do trzech numerów oddzielonych przecinkami" guidance to the MF FAQ. I could not open the individual FAQ answers (the page loads them dynamically), so treat that wording as secondary.

### 4.5 KSeF QR verification link (KOD I / KOD II)
Source: https://raw.githubusercontent.com/CIRFMF/ksef-docs/main/kody-qr.md and https://ksef.podatki.gov.pl/informacje-ogolne-ksef-20/kody-weryfikujace-qr/

- **Hosts:**

  | Environment | Host |
  |---|---|
  | TE (test) | `https://qr-test.ksef.mf.gov.pl` |
  | DEMO | `https://qr-demo.ksef.mf.gov.pl` |
  | PROD | `https://qr.ksef.mf.gov.pl` |

- **KOD I:** "adresu URL: `https://qr-test.ksef.mf.gov.pl/invoice`, daty wystawienia faktury (pole `P_1`) w formacie DD-MM-RRRR, NIP-u sprzedawcy, skrótu pliku faktury obliczonego algorytmem SHA-256 … w formacie Base64URL".
  - Official example: `https://qr-test.ksef.mf.gov.pl/invoice/1111111111/01-02-2026/UtQp9Gpc51y-u3xApZjIjgkpZ01js-J8KflSPW8WzIE`
  - The path order is **/invoice/{NIP}/{DD-MM-RRRR}/{hash}**.
  - The hash is 43 Base64URL characters without padding. Verified: it decodes to 32 bytes.
- **Label under the code:** the KSeF number if it has been assigned, otherwise "**OFFLINE**". KOD II carries "**CERTYFIKAT**". The QR must comply with **ISO/IEC 18004:2024**.
- **KOD II:** `https://qr-test.ksef.mf.gov.pl/certificate/{ContextType: Nip|InternalId|NipVatUe|PeppolId}/{contextValue}/{sellerNIP}/{certSerial}/{hash}/{signature}`.
  - The signature is over the path without `https://` and without a trailing `/`.
  - Algorithms: RSASSA-PSS SHA-256 (MGF1-SHA256, salt 32, ≥ 2048-bit) or ECDSA P-256/SHA-256 (IEEE P1363 R||S recommended), Base64URL encoded.
  - **Our tool should only parse and explain KOD II.** It must never ask for a private key.
- **MF:** the code contains "adres zasobu …, datę wystawienia faktury … z pola P_1, identyfikator NIP sprzedawcy, wyróżnik faktury". The "wyróżnik" is the SHA-2 256-bit hash of the XML file.

```js
const QR_RE = /^https:\/\/(qr(?:-test|-demo)?)\.ksef\.mf\.gov\.pl\/invoice\/(\d{10})\/(\d{2})-(\d{2})-(\d{4})\/([A-Za-z0-9_-]{43})$/;
async function kod1FromFile(file, env='qr'){            // hash the RAW bytes exactly as received
  const buf = await file.arrayBuffer();
  const h = new Uint8Array(await crypto.subtle.digest('SHA-256', buf));
  const b64url = btoa(String.fromCharCode(...h)).replace(/\+/g,'-').replace(/\//g,'_').replace(/=+$/,'');
  const xml = new DOMParser().parseFromString(new TextDecoder().decode(buf),'application/xml');
  const ns='http://crd.gov.pl/wzor/2025/06/25/13775/';
  const nip = xml.getElementsByTagNameNS(ns,'Podmiot1')[0].getElementsByTagNameNS(ns,'NIP')[0].textContent.trim();
  const [y,m,d] = xml.getElementsByTagNameNS(ns,'P_1')[0].textContent.trim().split('-');
  return `https://${env}.ksef.mf.gov.pl/invoice/${nip}/${d}-${m}-${y}/${b64url}`;
}
```
- **Important:** do not re-serialise or pretty-print the XML before hashing. Any byte change (BOM, line endings) changes the hash.
- **For rendering:** a QR library (e.g. `qrcode` or `qrcode-generator`) at error-correction level M. Klarbon reports that level for real KSeF codes; MF only mandates ISO/IEC 18004:2024.
- **For camera scanning:** `BarcodeDetector` where supported, with a `jsQR` fallback.
- **Anti-phishing rule:** accept only the three hosts above. Flag test and demo links as "brak skutków podatkowych".

### 4.6 FA(3) XML — namespace and the fields needed
Source: the XSD at https://raw.githubusercontent.com/CIRFMF/ksef-docs/main/faktury/schemy/FA/schemat_FA(3)_v1-0E.xsd (also published at http://crd.gov.pl/wzor/2025/06/25/13775/; MF page https://ksef.podatki.gov.pl/informacje-ogolne-ksef-20/struktura-logiczna-fa-3/: "Od 1 lutego 2026 r. struktura logiczna FA(3) zastąpiła strukturę logiczną FA(2)").

- **targetNamespace:** `http://crd.gov.pl/wzor/2025/06/25/13775/`. Root element: `Faktura`.
- **FA(2) (legacy) namespace** for detection: `http://crd.gov.pl/wzor/2023/06/29/12648/`. Secondary source: toolswebpro.com and ksefka.com, not checked against the FA(2) XSD.
- **Header:**
  - `Naglowek/KodFormularza` has attributes `kodSystemowy` fixed `"FA (3)"` and `wersjaSchemy` fixed `"1-0E"`.
  - `Naglowek/WariantFormularza` = `3`.
  - `Naglowek/DataWytworzeniaFa`.
- **Parties:**
  - `Podmiot1/DaneIdentyfikacyjne/NIP`, `…/Nazwa` (seller); `Podmiot1/Adres/KodKraju`, `AdresL1`, `AdresL2`.
  - `Podmiot2/DaneIdentyfikacyjne/NIP` (or `KodUE`+`NrVatUE`, or `NrID`, or `BrakID`), `…/Nazwa` (buyer).
  - `Podmiot3` 0..100 (role codes, e.g. factor or payer).
- **Fa (the invoice body):**
  - `KodWaluty`, `P_1` (issue date, `RRRR-MM-DD`), `P_1M` (place), `P_2` (seller's invoice no.), `P_6` (supply date).
  - Net/VAT per rate: `P_13_1`/`P_14_1` (23/22 %), `P_13_2`/`P_14_2` (8/7 %), `P_13_3`/`P_14_3` (5 %), `P_13_4`/`P_14_4`, `P_13_5`/`P_14_5`, `P_13_6_1..3` (0 %), `P_13_7` (zw), `P_13_8`, `P_13_9`, `P_13_10` (odwrotne obciążenie), `P_13_11` (marża). Foreign-currency VAT in PLN: `P_14_xW`.
  - `P_15` (należność ogółem).
  - `Adnotacje/P_18A`: "mechanizm podzielonej płatności", 1 = yes, 2 = no.
  - `RodzajFaktury` ∈ {VAT, KOR, ZAL, ROZ, UPR, KOR_ZAL, KOR_ROZ}.
  - For corrections: `DaneFaKorygowanej/NrKSeFFaKorygowanej` (type `TNumerKSeF`) with flag `NrKSeF`.
- **Lines:** `FaWiersz` (0..10000) with `NrWierszaFa`, `P_7` (name), `P_8A` (unit), `P_8B` (qty), `P_9A` (net unit price), `P_11` (net value), `P_12` (rate: 23, 22, 8, 7, 5, 4, 3, "0 KR", "0 WDT", "0 EX", "zw", "oo", "np I", …).
- **Payment (`Platnosc`):**
  - `TerminPlatnosci/Termin` (date).
  - `FormaPlatnosci`: 1 Gotówka, 2 Karta, 3 Bon, 4 Czek, 5 Kredyt, **6 Przelew**, 7 Mobilna.
  - `RachunekBankowy/NrRB` (10–34 characters), `LinkDoPlatnosci`, `IPKSeF`.
  - Also `Rozliczenie/DoZaplaty` (amount payable after charges and deductions). Prefer it over `P_15` when present; alltoolio shows both.
- **The KSeF number is not in the XML.** MF: "Numer ten zwracany jest w UPO … i sam w sobie nie stanowi elementu pliku xml". So read it from:
  - the filename (KSeF exports are usually named with it, per czytnikfaktur and przelewyksef),
  - `_metadata.json` in the KSeF export ZIP (per przelewyksef),
  - the UPO element `NumerKSeFDokumentu` (per czytnikfaktur),
  - or manual paste.
- **Parsing:** `DOMParser` plus `getElementsByTagNameNS(ns, …)`, with a fallback to `localName` matching so FA(2) files still show a summary. Amounts are decimal strings with `.`; format them for display with `Intl.NumberFormat('pl-PL')`, and use a comma for the MPP `/VAT/`.

### 4.7 JDG checker — decision data (with sources)
- **Until 31.12.2026:** issuing outside KSeF is allowed if monthly invoiced sales are ≤ 10 000 zł (art. 145m); invoices from cash registers and receipts with NIP ≤ 450 zł are allowed (art. 145n).
- **From 1.01.2027:** both exemptions end. MF timeline page (§0); prawo.pl, 6.11.2026.
- **Payments with a KSeF number:** from 1.01.2027 only between **active** VAT payers (art. 108g). Voluntary when the seller or buyer is VAT-exempt (as stated on czytnikfaktur, citing the MF FAQ).
- **Penalties (art. 106ni):** up to 100 % of the VAT on the invoice, or 18.7 % of the gross amount when there is no VAT (as reported by wektorbiznesu.pl and payupfinance.pl). Planned start 1.01.2028 per Sejm vote of 6.11.2026; still pending in the Senate.
- **Consumer (B2C) invoices in KSeF remain optional.** MF: "Faktury na rzecz osób fizycznych nieprowadzących działalności gospodarczej mogą być wystawiane w KSeF dobrowolnie." (MF timeline page.)

---

## 5. Cross-cutting UX and SEO advantages to claim (from competitor weaknesses)
1. **One input box that auto-detects** a KSeF number, an IZ, a KOD I link, a NIP, or a list of these. Competitors run one tool per page.
2. **Bulk input plus CSV export everywhere.** Only ranx does paste-bulk, and nobody exports.
3. **Mobile-first with camera scan.** Most competitors are desktop text walls.
4. **No ads, no sign-up, no upload.** Say so above the fold (czytnikfaktur shows ads, almmity and shipailab are funnels).
5. **Explain errors specifically**, e.g. "znak 23: O zamiast 0?", "IZ – dobry format, ale tylko KSeF wie, jakie faktury obejmuje", "36 znaków = numer z KSeF 1.0".
6. **Dated legal status box** ("stan prawny na …") with official links. ksefnarzedzia sets the bar here.
7. **Avoid**: generic XML viewers, XSD validators, and standalone NIP pages. All are saturated.

## Files
- `/workspace/projects/4d33c9a5-39ad-43fa-885b-d72bfcc6b372/work/research.md`: this report.
- `/workspace/projects/4d33c9a5-39ad-43fa-885b-d72bfcc6b372/work/fa3.xsd`: the official FA(3) XSD (schemat_FA(3)_v1-0E), downloaded from github.com/CIRFMF/ksef-docs for reference while implementing #4 and #5.
