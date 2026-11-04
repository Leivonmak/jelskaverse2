# Spis postaci NPC (dla MG) — jedyny spis wszystkich postaci

**Status:** dokument wszystkowiedzący, na potrzeby MG. W wierszu „Stan” najnowszy wpis jest pierwszy (z datą gry); wpisy z wcześniejszą datą są nadal aktualne, jeśli nic nowego się nie wydarzyło. **Format kart ujednolicony 18 X 2026 (Z165).**
**Zakres:** wszystkie NPC obu wątków (Antoniny i gen. Markiewicza) w jednym pliku. Dawny plik kart NPC wątku Markiewicza został tu wchłonięty i usunięty (12 X 2026).
**Wiążące:** autor przyjął wartości MG jako ostateczne (Z39). Znaczniki: [K] stary kanon, [N] autor, [P] propozycja MG, [G] ustalone w grze, [?] otwarte. Sekretów nie pokazywać wprost — ujawniać scenami.
**IQ** — przybliżona miara intelektu. **Stosunek platoniczny do Antoniny** w skali −5…+5 (−5 wrogość, 0 obojętność, +5 bliskość). **Stosunek romantyczny do Antoniny** w skali 0…+5 jak pasek romansu w The Sims (0 brak; +1 sympatia lub zerkanie; +2 zainteresowanie; +3 zauroczenie; +4 zakochanie; +5 oddanie) — wartość mają **wszyscy NPC, którzy uznają Antoninę za atrakcyjną**; rodzina, nieletni i obojętni mają 0. Wartości [P] bez znaczników są propozycjami MG do zatwierdzenia.
**Nazwiska [N, Z37]:** w pokoleniu dzieci kobiety noszą nazwisko **Jelska**, mężczyźni **Bryne-Jelski**.

---

## 0. Format karty NPC i sekcja „Jak grać” [N, autor 12 X 2026; format Z165, 18 X 2026]

Każda postać ma nagłówek `### imię i nazwisko (stopień)` i tabelę dwukolumnową (Pole | Wartość) z **13 wierszami w stałej kolejności**: Wiek, Wzrost, Budowa ciała, IQ, Rola, Wygląd, Wiedza, Motywacje, Sekrety, Stosunek platoniczny do Antoniny, Stosunek romantyczny do Antoniny, Stan, Jak grać. Brak danych: `?`; propozycje MG dostają [P]. Pozycje „Pokusy”, „Rodzina”, „Języki” i podobne ze starszych kart zostały wchłonięte w wiersze Motywacje, Rola i Jak grać. Nagłówki zbiorcze (`##`, `####`) opisują grupy i konteksty, nie postaci. Wiersze „Stan” zawierają daty; najnowszy wpis na początku.

Wiersz **Jak grać** to instrukcja odgrywania, która ma utrzymać spójność postaci między kompresjami kontekstu. MG czyta go **przed** pierwszą kwestią danej postaci w sesji. Zawiera (rozdzielone `<br>`):
- **Osobowość** — rdzeń charakteru w kilku zdaniach: czego chce, czego się boi, jak reaguje pod presją.
- **Mowa** — rejestr, długość wypowiedzi, ulubione zwroty, czego nie mówi nigdy.
- **Pisanie** — SMS-y, maile, posty: pisownia, interpunkcja, emotikony, podpisy, język. **To jest wiążące dosłownie** (np. Michał Markiewicz nie używa polskich znaków).
- **Języki** — w jakim języku rozmawia z kim (dialog i tak zapisujemy wg Z27: po polsku, chyba że rozmowa toczy się po angielsku).
- **Nie robi** — granice postaci, których MG nie przekracza bez wydarzenia w grze.

**Zasady ogólne:**
1. Ton narracji: powściągliwy (03 §3). Postaci mówią krótko, chyba że karta mówi inaczej.
2. Nikt nie jest wszechwiedzący. Postać zna tylko to, co w karcie i w logach dotarło do niej.
3. Rozkład postaw nowych NPC: ok. 1/3 życzliwi, 1/3 obojętni, 1/3 nieżyczliwi lub interesowni (Z72).
4. **Nie odgrywać przez MG czatu Antoniny:** gen. **Radosław Markiewicz** (gracz-człowiek, Z60). Jego kwestie wkleja autor; karta służy spójności tła.
5. W mówionych dialogach nie ma emotikon (Z27); emotikony tylko w tekstach pisanych, zgodnie z kartą.
6. Ilekroć karta i log się różnią — wygrywa nowszy log; MG poprawia kartę przy zamknięciu sesji.

---

## A. Rodzina

#### Kolejność rodzeństwa [N, Z38]

| # | Imię i nazwisko | Ur. | Wiek (I 2013) | Wzrost | IQ | W skrócie |
|---|---|---|---|---|---|---|
| 1 | **Antonina Jelska** | 17 XII 1987, Amsterdam | 25 | 193,3 | ok. 210 | karta: `06-karta-antoniny-mg.md` |
| 2 | **Adam Bryne-Jelski** | 4 IV 1989, Warszawa | 23 | 190 | 125 | playboy, kabareciarz |
| 3 | **Gabriela Jelska** | 22 II 1991, Warszawa | 21 | 180 | 175 | biotechnolożka, „normalny geniusz" |
| 4 | **Wiktoria Jelska** | 9 X 1993, Lozanna (starsza o 7 minut) | 19 | 185 | 140 | operatorka społeczna |
| 5 | **Tadeusz Bryne-Jelski** | 9 X 1993, Lozanna | 19 | 193 | 145 | cichy konstruktor, mechatronika |
| 6 | **Mikołaj Bryne-Jelski** | 14 III 1996, Lozanna | 16 | 188 | 150 | nerd-humanista, prawo |
| 7 | **Natalia Jelska** | 2 VI 1998, Lozanna | 14 | 176 | 145 | nerd-humanistka, historia i archeologia |
| 8 | **Klara Jelska** | 30 XI 2000, Lozanna | 12 | 158 | 120 | wrażliwa, dobroduszna, dojrzewa |

Ośmioro dzieci. Najmłodsza trójka mieszka w Savigny i chodzi do ISL. Klara dostała imię po Klarze Wołejszo, kuzynce ojca. **Antonina jest kometą, reszta rodzeństwa krąży wokół niej po swoich orbitach.** Adam rywalizuje i podziwia, Gabi tłumaczy ją rodzinie, Wiktoria chce jej świata, Tadeusz milczy z nią w zgodzie, Mikołaj się z nią spiera, Natalia ją dokumentuje, Klara chce jej uwagi.
**W domu wszyscy mówią po polsku** (Z42). Rodzinny czat rodzeństwa: „🚨 TOSIA” (od 15 I).

---

### Krzysztof Bryne-Jelski

| Pole | Wartość |
|---|---|
| Wiek | 54 |
| Wzrost | **188 cm** [N, Z203; dawniej 187 — K] |
| Budowa ciała | ok. 85 kg; szczupły, wyprostowany, żylasty [P] |
| IQ | ok. 150 [K] |
| Wykształcenie | **Lycée Sainte-Geneviève („Ginette”), CPGE Math-Physique → École polytechnique, X1978; classement de sortie: 194.** („wyższa klasa średnia” promocji) [N, Z203]; **bez Mines / Corps des Mines** [N, Z203 — skreślone z K] |
| Rola | ojciec Antoniny; były premier RP (VI 1991 – V 1993); **oficjalnie na emeryturze, „nic nie robi całymi dniami"** [N, Z43]; w Technokracji wtajemniczony, bez stałych zadań; zaproszenie Antoniny na kolegium przekazał jako zaufany pośrednik |
| Wygląd | szaroniebieskie oczy (Antonina ma je po nim); krótkie, szpakowate włosy, spokojna twarz bez uśmiechu, w domu sweter i płócienne spodnie [P] |
| Wiedza | **[Z267, 25 I ok. 6:01]** zna relację Antoniny o ciężkim zatruciu chlorem, dwóch zgonach w wypadku, ratunku Castagneta, intubacji i OIOM Percy po Cayenne; od Markiewicza wie o wcześniejszej wiedzy Syropa o planie zabicia jego żony. Dawne wpisy o niewiedzy są historyczne. wie o taśmie (od de Villiersa, 15 I), o implancie i Mossadzie (16 I); od Wiktorii wie o „DGSE”, połączył Wilanów 1993 → „horyzont 10–15 lat” → l'X od Syropa; **[Aktualizacja Z265, 25 I ok. 5:52] od Antoniny wie o CEFE, Jaubercie, walce i dwóch zabitych w obronie sekcji oraz kanale DGSE–AW–SGDN i roli Syropa; **[Aktualizacja 25 I ok. 5:57, wpis 13] zna wzmiankę Antoniny o wypadku z chlorem; nie zna szczegółów ani OIOM****; 17 I wieczorem de Villiers powiedział mu o wyjeździe na Nohora'a (był tam w 1998) |
| Motywacje | bezpieczeństwo rodziny; żeby Tosia weszła w świat Technokracji „przez drzwi, które sama otworzy" [G]. **Pokusa:** rozwiązywać sprawy dzieci operacyjnie („mam człowieka") [G]. **Wobec reszty dzieci:** Adama kocha i nie rozumie; Gabi ufa bez zastrzeżeń; Wiktorii się trochę boi; z Tadeuszem majsterkuje w milczeniu; z Mikołajem przegrywa spory o prawo chętniej, niż przyznaje; Natalii pozwala czytać stare przemówienia; Klarę rozpieszcza |
| Sekrety | zdanie Tosi waży dla niego więcej niż dla większości kolegium; od 1993 boi się, „co świat i służby z nią zrobią" [K]; Wiktorii świadomie nie daje swojego świata (uważa, że by ją zjadł) |
| Stosunek platoniczny do Antoniny | **+5** (powściągliwie) |
| Stosunek romantyczny do Antoniny | **0** (pokrewieństwo) [P] |
| Stan | **27 I 22:43 (sesja 19 wpis 477):** na „Jestem. Idę spać.” odpisał: „Dobrze. Śpij. Patrol jest pod domem do piątku. Tata”.<br>**25 I, 6:30 (sesja 19 wpis 16):** przygotował duży omlet, chleb i masło; Antonina zjadła. Zostaje w drzwiach domu po wyjściu jej i Markiewicza do taksówki. **25 I, ok. 6:03 CET (sesja 19, wpis 15):** zna od Antoniny jej wyjaśnienie niepowiadomienia oraz podpisanie zobowiązania w Percy [G]. Zaczyna robić jajka i śniadanie, proponuje wolną łazienkę [P]. Dalsza rozmowa i działania wobec Syropa nieodbyte. **25 I, ok. 6:01 CET (sesja 19, Z267):** chce być przy rozmowie Markiewicza z Syropem, nie uzyskał jeszcze zgody; pyta Antoninę o decyzję niepowiadamiania rodziny [P]. **25 I, ok. 5:57 CET (sesja 19, wpis 13):** słyszy deklarację dumy ze służby i sprzeciw wobec litości [G]; odpowiada „Przyjąłem. Jestem z ciebie dumny.” i pyta o chlor [P]. Nie zna dalszego przebiegu wypadku. **25 I, ok. 5:54 CET (sesja 19, wpis 12):** od Antoniny wie, że źródłem ujawnienia był de Villiers 15 I, a l'X wybrała sama [G]. Markiewicz zapowiada rozmowę z Syropem w Warszawie [N]. Krzysztof potwierdza współpracę i zaufanie do Syropa, czeka na dalszy ciąg [P]; bez działań operacyjnych. **25 I, ok. 5:52 CET (sesja 19, Z265) [G + P]:** wysłuchał ujawnienia Gujany; przypomina własną zgodę na szkołę proponowaną przez Syropa, pyta Antoninę o źródło jej wiedzy o Syropie. Cichnie, splata mocniej dłonie; nie podejmuje działań [P]. **25 I, ok. 5:48 CET (sesja 19, wpis 10):** idzie za Antoniną do salonu [N]; po jej zapowiedzi wyjaśnienia Gujany siada naprzeciw i słucha [P]. Prawdy o Gujanie nadal nie zna. **25 I, ok. 5:47 CET (sesja 19, wpis 9) [G + P]:** wie od Antoniny, że nie znała drugiego zakładu; prostuje swój błędny opis V17 (nagranie za zgodą, dalszy obieg wbrew zakazowi). Proponuje pokazanie wpisów; nie zna terminu ani zakresu publikacji. **25 I, ok. 5:46 CET (sesja 19, wpis 8) [P na polecenie autora]:** zna D67/C216/C287/C306/C383 z nocnej lektury; omawia z Antoniną zakłady, kasę 800+580 FRF, 49 kont, zwroty w VII 2010, film z La Courtine i reakcję szkoły. Pyta o jej wiedzę o drugim zakładzie. Telefon jeszcze nieprzekazany. **25 I, ok. 5:43 CET (sesja 19, wpis 7) [P]:** robi Antoninie miejsce w drzwiach i proponuje przejęcie walizki („Daj. Postawię.”), jeszcze jej nie przejął. Markiewicz przy nim według dopowiedzenia autora. **25 I, 5:42 CET (sesja 19, wpis 6) [N]:** przed wejściem Antoniny podchodzi do niego obudzony Markiewicz i komentuje jej przyjazd; reakcja Krzysztofa jeszcze nieodegrana. **25 I, 5:42 CET (sesja 19) [P]:** po prośbie Antoniny otwiera bramę, wychodzi na próg domu: „Już, Tosia.” / „Chodź do środka.” Po nieprzespanej nocy, oczy zaczerwienione. **25 I, 5:42 CET [N, autor OOC 23 X 2026]:** po nieprzespanej nocy; na monitoringu rozpoznaje Antoninę przy bramie i dyplomatycznego Peugeota ambasady Francji. Korekta wcześniejszej niewiedzy o dzwoniącym. **25 I, 5:42 CET [KOREKTA Z264]:** po nocnej lekturze odbiera domofon w salonie: „Tak?” [P]; nie otrzymał jeszcze odpowiedzi Antoniny. **25 I, ok. 6:00 CET [P czas] (M18):** wraz z Katarzyną przeglądał treści przez noc na telefonie pozostawionym za zgodą Markiewicza [N]; dokładny zakres lektury i wnioski [?].<br>**24 I (M18, ok. 22:42 [P czas]):** pyta Markiewicza o możliwość przejrzenia całości z Katarzyną; prosi Natalię, by pomogła gościowi się rozgościć [N przebieg]. Zgoda na dostęp jeszcze niepadła.<br>**24 I (M18, ok. 22:40 [P czas]):** zna podpis D44: Hervé Castaing [N], nie kojarzy nazwiska [P]; zaskoczony oceną Natalii o ochronie karier przez przekazanie sprawy samorządowi przyznaje jej rację [N przebieg].<br>**24 I (M18, ok. 22:39 [P czas]):** poznał sześć punktów D44 pokazanej przez Markiewicza [N]; komentuje gratulacje i pyta o podpis [P]. Nie podejmuje działań.<br>**24 I (M18, ok. 22:38 [P czas]):** słyszy przypuszczenie Markiewicza o zamieceniu sprawy przez dowództwo; wskazuje tytuł D44 i prosi o otwarcie [P]. Treści noty jeszcze nie zna.<br>**24 I (M18, ok. 22:37 [P czas]):** czyta T46, poznaje sankcje Kès wobec Gasparda; pyta o decyzję dowództwa [P]; bez odpowiedzi.<br>**24 I (M18, ok. 22:36 [P czas]):** czyta początek T35, komentuje dziewięć miesięcy zakładu i wymówkę o żarcie [P]; wynik komisji jeszcze nieprzekazany.<br>**24 I (M18, ok. 22:34 [P czas]):** po wypowiedzi Markiewicza prosi o pokazanie tekstów [P]; kolejny materiał niewybrany.<br>**24 I (M18, po 22:30):** przegląda filmy przy Katarzynie; V10 (podryw), miniaturka szermierki, ujęcie V17 z La Courtine; pokazuje je żonie [N, autor GM].<br>**21 I (sesja 16, do 20:23 lok.):** SMS 20:59 CET (karta na domeny, „zająłem się płotem”); 6:46 CET rozmowa Iridium: dwóch policjantów przy bramie, Pierre: sprawa żołnierza zamknięta po ich stronie; pytał raz: „Czy ktoś zrobił ci krzywdę?” — „Nie.”; „Krem z filtrem. Zjedz tego steka.”<br>**18 I:** 17 I ludzie Pierre'a sprawdzili Savigny („czysto”); numer Iridium Antoniny dał tylko żonie (ew. Adamowi, Gabi); 17 I wieczorem mail 22:31: „Pierre dzwonił. Wiem. Weź krem z filtrem. Dobra. Tata”; chce rozmowy z Markiewiczem „o wszystkich telefonach — at dinner”; kolegium — odpowiedź Antoniny najpierw do niego (do 31 I). Katarzyna: „tata się boi” |
| Jak grać | **Osobowość:** kontrola jako forma troski. Architekt państwa, który od dwudziestu lat udaje emeryta i prawie w to wierzy. Nie tłumaczy się i nie przeprasza za czyny, tylko podaje **jeden prawdziwy powód**. Uczucia okazuje czynem: gotuje, przyjeżdża, załatwia. Pod presją robi się cichszy, nie głośniejszy. Kiedy się boi, staje się operacyjny („Je m'en occupe”, „zająłem się tym”).<br>**Mowa:** krótkie zdania, sucha ironia, pauzy. „Dobra” zamiast „powodzenia”. Nie mówi o służbach przez telefon („reszta nie na telefon”). Pytania zadaje wprost i raz („Czy ktoś zrobił ci krzywdę?”). Do Antoniny „Tosia”.<br>**Pisanie:** SMS-y telegraficzne, pełne zdania z kropkami, bez emotikon, **podpis „Tata”** („Czytałem. Jestem w domu. Środa aktualna. Tata”). Czasem jedno słowo („Link.”).<br>**Języki:** z rodziną po polsku; z de Villiersem i Technokracją po francusku; z Markiewiczem po polsku; z Miko po angielsku.<br>**Nie robi:** nie podnosi głosu; nie opowiada o Technokracji przy młodszych dzieciach; nie przyznaje się do strachu (robi to za niego Katarzyna); nie dzwoni do Syropa przy Antoninie. |

### Katarzyna Bryne-Jelska z d. Laband

| Pole | Wartość |
|---|---|
| Wiek | 53 |
| Wzrost | ok. 170 cm |
| Budowa ciała | ok. 62 kg; drobna, wąska w ramionach, smukłe dłonie [P] |
| IQ | ok. 145 |
| Rola | matka Antoniny; sumerolożka [K]; tabliczka z Nippur (Penn Museum) z „Michaelem z Filadelfii" [G]; współpraca z Uniwersytetem Genewskim; w 1987 dwa tygodnie konsultantką przy badaniach szczątków Jadwigi na Wawelu (potwierdziła Antoninie 15 I) |
| Wygląd | krótkie jasnobrązowe włosy z siwymi pasmami, ciepłe brązowe oczy, lekki holenderski akcent [G] |
| Wiedza | o taśmie wie od Natalii (15 I, płakała); o wyjeździe wie od męża tyle, ile mógł powiedzieć; zna rzadkie proszenie Antoniny o pomoc |
| Motywacje | żeby dzieci były szczęśliwe, nie tylko skuteczne; dom jako azyl. **Pokusa:** chronić dzieci przed ojcem i Technokracją |
| Sekrety | przeciw kolegium, ale ustąpiła („to nie moja decyzja”); nie traktować rzadkiego proszenia o pomoc jako niezdolności do przyjmowania troski (Z164); martwi się o Klarę bardziej, niż pokazuje; Natalia jest jej „drugim ja" i to ją trochę przeraża |
| Stosunek platoniczny do Antoniny | **+5** |
| Stosunek romantyczny do Antoniny | **0** (pokrewieństwo) [P] |
| Stan | **25 I, 5:42 CET [N, autor OOC 23 X 2026]:** nie spała przez noc, podobnie jak Krzysztof; zakres lektury pozostaje [?]. **25 I, 5:42 CET [KOREKTA Z264]:** po całonocnej lekturze; telefon Markiewicza nadal u rodziców [N, ZM83], jej dokładne miejsce i zakres lektury [?]. **25 I, ok. 6:00 CET [P czas] (M18):** wraz z Krzysztofem przeglądała treści przez noc na telefonie Markiewicza [N]; bez dopisania szczegółów lektury ani nowych reakcji.<br>**24 I (M18, ok. 22:39 [P czas]):** poznała sześć punktów D44 [N]; gorzko zestawia natychmiastowy zakaz balonów z odroczeniem sprawy aneksu [P].<br>**24 I (M18, ok. 22:37 [P czas]):** czyta T46, poznaje naganę i odsunięcie Gasparda od zadań Kès do końca roku; zatrzymuje uwagę na terminie sankcji [P].<br>**24 I (M18, ok. 22:36 [P czas]):** czyta początek T35 o zakładzie, pyta o działania szkoły [P]; bez odpowiedzi.<br>**24 I (M18, ok. 22:34 [P czas]):** słyszy potwierdzenie obiegu filmu i wzmiankę Markiewicza o czynach; chce ich wyjaśnienia po tekstach [P].<br>**24 I (M18, po 22:30):** po V10 żartuje z podrywu męża; widząc ujęcie V17 traci uśmiech [N, autor GM]; pyta, czy przesyłali sobie nagranie [P, bez odpowiedzi].<br>**21 I (sesja 16, do 20:23 lok.):** rozmowa Iridium 6:38–6:50 CET: trzy rzeczy (wszyscy cali; policjanci; brak reporterów dziś), „Rozkładaj ją na części, jak tabliczkę”, „Kocham cię. Do środy.”<br>**18 I:** zaprosiła Markiewicza na gołąbki (~21–26 I); 17 I 13:41 mail „Nie w żadnej sprawie” (goście taty byli rano, Klara prosi o sprawdzenie ułamka); mail 22:54: „Jeśli zdążysz przed wyjazdem, zadzwoń. Nie w żadnej sprawie. ❤️” |
| Jak grać | **Osobowość:** ciepła i precyzyjna jednocześnie; prowadzi dom ośmiorga jak seminarium — każde dziecko ma swoją godzinę. Decyduje bez konsultacji, gdy chodzi o dzieci. Nie dramatyzuje; rozkłada sprawy na części jak tabliczkę klinową. Kocha męża i widzi go bez złudzeń.<br>**Mowa:** spokojna, z suchą ironią, czasem holenderskie wtrącenie („ach, schatje”). Mówi „wolałabym, żebyś wiedziała ode mnie”. Ocenia uczciwie, nawet jeśli boli („część dana za darmo”). Kończy rozmowy czułością bez patosu: „kocham cię, do środy”.<br>**Pisanie:** pełne zdania, poprawna interpunkcja, czasem jedno serce ❤️ i nic więcej.<br>**Języki:** z rodziną po polsku; z Miko i Tanakami po angielsku; z kolegami po francusku i niderlandzku.<br>**Nie robi:** nie pyta o szczegóły służb; nie krytykuje Krzysztofa przy dzieciach; nie płacze przy Antoninie (płacze potem, w kuchni, w ręcznik). |

### Adam Bryne-Jelski

| Pole | Wartość |
|---|---|
| Wiek | 23 |
| Wzrost | 190 cm |
| Budowa ciała | ok. 85 kg; wysoki, barczysty, trochę zbyt miękki w pasie przy imprezowym trybie życia [P] |
| IQ | ok. 125 |
| Rola | brat Antoniny (2. z rodzeństwa); rzucił mechanikę na EPFL (wypisany 9 I 11:42); **aplikuje do HEC Paris (MiM, runda III, IV 2013)**, GMAT na początku III, Antonina pomaga z matematyką; mieszka w kawalerce w Lozannie (Chauderon); **K0: absolwent HEC, zarządza finansami rodziny (2025)** [N] |
| Wygląd | ciemne włosy, szeroki uśmiech, zawsze lekko niedbały, pachnie dobrą wodą kolońską i papierosami, których „nie pali" |
| Wiedza | wie, że Tosia była dziewicą [G]; od 15 I szuka prawnika od wizerunku; zgłaszał mirrory taśmy; chciał „pogadać” z Karimem — powstrzymany („Adam, nie.”) |
| Motywacje | być kimś bez nazwiska; zasłużyć na szacunek ojca czymś, co ojciec rozumie. **Pokusy:** ucieczka w kobiety, imprezy i żart; rzucić wszystko, zanim przegra. **Wobec rodzeństwa:** opiekun Klary i Natalii (lody, przeklinanie po norwesku); z Wiktorią rywalizuje o to, kto lepiej „ogarnia ludzi"; Tadeusza nazywa „Cichy" |
| Sekrety | długi na karcie (ok. 6000 CHF) ukrywane przed rodzicami |
| Stosunek platoniczny do Antoniny | **+4** (podziw z goryczą porównań; zaufał jej pierwszej) |
| Stosunek romantyczny do Antoniny | **0** (pokrewieństwo) [P] |
| Stan | **21 I (sesja 16, do 20:23 lok.):** 12:41–12:44 CET „mam 4 agencje”; 18:36 CET Playboy podniósł do 400 tys.; 20:05 CET Wojewódzki zaprasza na piątek (producent dzwonił do Adama); „ODPISZ mi cokolwiek”<br>**17 I:** czeka na odpowiedź ws. prawnika od wizerunku (mec. Kowalczyk [P]) |
| Jak grać | **Osobowość:** kabareciarz z wyboru — w rodzinie geniuszy wziął jedyne pole, na którym nikt z nim nie konkuruje. Najlepiej w rodzinie czyta ludzi „na żywo” (Antonina na papierze, on przy barze). Pod humorem lęk przed byciem „zwykłym”. Lojalny jak pies; gdy siostra cierpi, odruchowo chce komuś przyłożyć.<br>**Mowa:** szybka, żartobliwa, sprośna („szwagier”), przezwiska. Gdy jest poważnie — nagle krótko i bez żartu (to sygnał dla MG, że sprawa jest serio).<br>**Pisanie:** SMS-y lawinami po kilka, małe litery, „xD”, „kurde”, emotikony 😂🔥; czasem jedno poważne zdanie na końcu („przepraszam”, „chcesz, żebym coś zrobił?”).<br>**Języki:** z rodzeństwem po polsku z wtrętami francuskimi; z kumplami po francusku; przeklina po norwesku.<br>**Nie robi:** nie mówi rodzicom o cudzych sekretach; nie przyznaje się do długów; nie przeprasza za żarty, chyba że zranił Klarę. |

### Gabriela „Gabi" Jelska

| Pole | Wartość |
|---|---|
| Wiek | 21 (22 w II 2013) |
| Wzrost | 180 cm |
| Budowa ciała | ok. 68 kg; szczupła, sportowa, długonoga |
| IQ | **ok. 175** [N] |
| Rola | siostra Antoniny (3. z rodzeństwa); 3. rok BSc bioinżynierii na EPFL; obsesja **CRISPR-Cas9** (Jinek i in., VIII 2012); praktyka w laboratorium genetyki |
| Wygląd | wysoka, szczupła, sportowa; długi warkocz; dużo się śmieje; swetry z dziurami po pipetach |
| Wiedza | zna rodzinę i Tosię najlepiej z rodzeństwa; wie o Lucasie (rodzice wiedzą, Tosia nie) |
| Motywacje | zostać zauważoną za własny umysł; być pierwszą w nowej dziedzinie. **Pokusy:** przekroczyć granicę etyczną „dla nauki" (edycja zarodków jako myśl, którą wypycha z głowy); rywalizacja z siostrą, do której się nie przyznaje |
| Sekrety | **letni staż w Berkeley (VI–VIII 2013)** — nikomu nie powiedziała; od roku chłopak **Lucas** (student medycyny, Lozanna) — rodzice wiedzą, Tosia nie |
| Stosunek platoniczny do Antoniny | **+5** (miłość, z cieniem: „druga, której nikt nie widzi") |
| Stosunek romantyczny do Antoniny | **0** (pokrewieństwo) [P] |
| Stan | **17 I:** na EPFL (kampus pełen plotek o siostrze); w grze od 6 I prawie nieobecna — dobra postać do wejścia „z boku” |
| Jak grać | **Osobowość:** geniusz bez efektu „wow” — normalna, towarzyska, lubiana. Najbliższa Tosi z rodzeństwa i jej „tłumaczka” na język rodziny. Widzi, kiedy Tosia ucieka w analizę, i mówi to wprost, z uśmiechem. Ma ambicję, której się wstydzi.<br>**Mowa:** zaczepna, ciepła, dużo pytań retorycznych, śmiech w połowie zdania. Lubi naukowe metafory biologiczne.<br>**Pisanie:** SMS-y krótkie, prowokujące, z 😏 („Od kiedy ty pieczesz? 😏”), poprawna polszczyzna.<br>**Języki:** z rodziną po polsku, na kampusie po francusku i angielsku.<br>**Nie robi:** nie zdradza Berkeley ani Lucasa bez wydarzenia w grze; nie bierze stron w kłótni Wiktoria–Tosia. |

### Wiktoria Jelska

| Pole | Wartość |
|---|---|
| Wiek | 19 (bliźniaczka Tadeusza, starsza o 7 minut) |
| Wzrost | 185 cm |
| Budowa ciała | ok. 70 kg; wysoka, wyprostowana, smukła [P] |
| IQ | ok. 140 |
| Rola | siostra Antoniny (4. z rodzeństwa); 1. rok BA nauk politycznych i stosunków międzynarodowych, Uniwersytet Genewski; mieszka w Genewie; wolontariat w Palais des Nations; Model UN |
| Wygląd | wysoka, wyprostowana; płaszcze, kaszmir, perły po babci Grietje; ciemne włosy upięte; spokojny, niski głos |
| Wiedza | zna dziewictwo Antoniny (do 12 I), Basile'a, futon z Miko, kolegium; 15 I wieczorem powiedziała ojcu o „DGSE” |
| Motywacje | władza jako wpływ; chce świata ojca: polityki, gabinetów, kolegium. **Pokusy:** manipulacja jako zabawa; traktować ludzi, nawet rodzeństwo, jak figury |
| Sekrety | zazdrość o kolegium przepracowana tylko częściowo; podsłuchiwała (przyznaje się tylko przyparta) |
| Stosunek platoniczny do Antoniny | **+2** → po 16 I niepewne +2 (kocha ją, ale ją „rozgrywa”) |
| Stosunek romantyczny do Antoniny | **0** (pokrewieństwo) [P] |
| Stan | **17 I:** 15 I wieczorem powiedziała ojcu o „DGSE” (A9 zrealizowane); 16 I przyznała się Antoninie, dostała chłodne „Okej. Wybaczam.”, potem w kuchni „Nikt nie jest na ciebie zły” — nadal niepewna, czy ma przeprosić drugi raz |
| Jak grać | **Osobowość:** operatorka społeczna. W trzy minuty wie, kto z kim i komu podać rękę. Zbiera ludzi jak kolekcję. Pod elegancją chęć bycia ważną w świecie, do którego ojciec jej nie wpuszcza. Gdy przegrywa, nie płacze — przegrupowuje się. Kocha Tosię i jej zazdrości jednocześnie, co ją samą irytuje.<br>**Mowa:** nienaganne maniery, nigdy nie podnosi głosu; mówi zdaniami, które brzmią jak propozycje („może byśmy…”); trafia w sedno jednym pytaniem. Używa słowa „dyskrecja”.<br>**Pisanie:** SMS-y małymi literami, żartobliwe, „:3”, 😂; przy sprawach ważnych zmienia się w pełne, eleganckie zdania.<br>**Języki:** pięć języków; z rodzeństwem po polsku, w Genewie po francusku i angielsku.<br>**Nie robi:** nie flirtuje jak Adam; nie robi scen; nie zdradza, że podsłuchuje — przyznaje się tylko przyparta. |

### Tadeusz Bryne-Jelski

| Pole | Wartość |
|---|---|
| Wiek | 19 (bliźniak Wiktorii) |
| Wzrost | 193 cm |
| Budowa ciała | ok. 95 kg; wysoki jak Antonina, szeroki, umięśniony (wspinaczka, wioślarstwo) |
| IQ | ok. 145 |
| Rola | brat Antoniny (5. z rodzeństwa); 1. rok BSc mechatroniki (mikrotechnika, profil robotyki) na EPFL; mieszka w Savigny, dojeżdża |
| Wygląd | wysoki jak Antonina, szeroki, umięśniony; krótko ostrzyżony; smar pod paznokciami |
| Wiedza | w garażu w Savigny buduje autonomicznego drona; jedyny przyjaciel — ktoś z forum robotycznego w Japonii |
| Motywacje | zbudować coś, co działa; mieć spokój. **Pokusa:** izolacja (gry nocą, warsztat zamiast ludzi) |
| Sekrety | je obiady sam, nie ma znajomego na roku; dron ma zaimponować ojcu |
| Stosunek platoniczny do Antoniny | **+5** (jedyna osoba, z którą może milczeć bez napięcia) |
| Stosunek romantyczny do Antoniny | **0** (pokrewieństwo) [P] |
| Stan | **17 I:** w Savigny / na EPFL; ludzie Pierre'a dziś sprawdzają dom — dron w garażu może ich zainteresować |
| Jak grać | **Osobowość:** myśli rękami. Milczy jak Antonina, ale bez maski Analityka — kiedy nie wie, co powiedzieć, nie mówi nic. Dawna sugestia podobieństwa neurorozwojowego pozostaje niepotwierdzoną interpretacją [?]; profil Antoniny nie rozstrzyga profilu Tadeusza (Z164). Idealizuje dziadka Haralda.<br>**Mowa:** jedno-, dwuwyrazowe odpowiedzi; gest zamiast słowa (klepnięcie, podany klucz). Gdy mówi dłużej — o technice, rzeczowo i zaskakująco elokwentnie.<br>**Pisanie:** najkrótsze SMS-y w rodzinie: „ok”, „jestem”, „👍”. Bez wielkich liter.<br>**Nie robi:** nie zaczyna rozmów o uczuciach; nie skarży się na samotność. |

### Mikołaj Bryne-Jelski

| Pole | Wartość |
|---|---|
| Wiek | 16 |
| Wzrost | 188 cm |
| Budowa ciała | ok. 68 kg; smukły, chudy, długie ręce |
| IQ | ok. 150 |
| Rola | brat Antoniny (6. z rodzeństwa); ISL, IB Diploma (1. rok); debaty, Model UN; czyta konstytucje i orzecznictwo |
| Wygląd | chudy, długie ręce, druciane okulary, marynarka do dżinsów |
| Wiedza | od jesieni czyta archiwa prasy 1991–93 o rządzie ojca; pracuje nad tekstem o KBP; 15 I pokazał ojcu AMA (11:15) |
| Motywacje | sprawiedliwość jako system; chce być sędzią lub prawnikiem międzynarodowym. **Pokusy:** moralna wyższość; myśleć, że prawo wystarczy |
| Sekrety | **znalazł kartę KBP/DSW/EO/93-0017** (ksero, karton „Rembertów — różne”), przeczytał nagłówek przez telefon 11 I (wyciek do pięciu służb) |
| Stosunek platoniczny do Antoniny | **+3** (podziw i sprzeciw moralny naraz) |
| Stosunek romantyczny do Antoniny | **0** (pokrewieństwo; nieletni) [P] |
| Stan | **27 I (sesja 19 wpisy 440a, 478):** SMS 17:34 (1. „Jestem” do 23:00; 2. procuration od Perret mailem pn rano, podpis przed 9:00; 3. nie komentować wywiadu Markiewicza — zasada c) i 21:47 (prośba o wiadomość do Klary rano; Instagram usunął podróbkę „official fanpage”, FB „Official Fans” jeszcze nie); bez odpowiedzi.<br>**21 I (sesja 16, do 20:23 lok.):** koordynuje pisma (Kowalczyk, pełnomocnictwo od 6:36 lok.), domeny (9 szt., karta ojca za jego zgodą), zgłoszenia o podszywanie się; błędnie wymienił 6 innych profili „Antonina Jelska” — sprostował (Z168); 16 l., niczego formalnie nie podpisuje; wobec ofert: milczenie = nie<br>**17 I:** nowy telefon i numer od 11 I; 16 I przeprosił Antoninę bez słów (skwarki, klepnięcie); nadal pracuje nad tekstem o KBP |
| Jak grać | **Osobowość:** idealista praworządności w rodzinie zbudowanej na realpolitik. Kocha ojca i podejrzewa go o łamanie prawa jednocześnie. Gdy narozrabia, wstydzi się głęboko i nie umie tego powiedzieć.<br>**Mowa:** dużo, precyzyjnie, z przypisami („art. 65 ust. 3, ale nowelizacja…”). Używa słów „legalnie”, „konstytucyjnie”, „podstawa prawna”. Spiera się z Antoniną o Prawo Zero.<br>**Pisanie:** długie SMS-y, numerowane punkty, poprawna interpunkcja, czasem nawias z odesłaniem do źródła.<br>**Nie robi:** nie publikuje znalezisk (obiecał); nie kłamie wprost — zamilknie zamiast tego. |

### Natalia Jelska

| Pole | Wartość |
|---|---|
| Wiek | 14 |
| Wzrost | 176 cm |
| Budowa ciała | ok. 58 kg; wysoka jak na 14 lat, chuda |
| IQ | ok. 145 |
| Rola | siostra Antoniny (7. z rodzeństwa); ISL (Year 9/10); wolontariuszka przy wykopaliskach Lousonna (Vidy); czyta o Mezopotamii z biblioteki matki |
| Wygląd | wysoka jak na 14 lat, chuda, piegi, włosy w ołówkowym koku |
| Wiedza | **prowadzi dziennik rodziny „dla przyszłych historyków"**, z zapisami podsłuchanych rozmów (także o Technokracji); od 15 I archiwizuje wszystko o Antoninie z internetu; powiedziała matce o taśmie (15 I 17:50) |
| Motywacje | zrozumieć, jak rzeczy się zaczęły; zostać archeolożką. **Pokusy:** uciekać w przeszłość; podsłuchiwać, „bo to źródło" |
| Sekrety | dziennik z podsłuchów; czuje się współwinna wycieku 11 I |
| Stosunek platoniczny do Antoniny | **+4** (traktuje ją jak postać historyczną; chce „wywiadu” — umówiony na IX) |
| Stosunek romantyczny do Antoniny | **0** (pokrewieństwo; nieletnia) [P] |
| Stan | **Noc 24/25 I (M18):** pomogła Markiewiczowi rozgościć się w pokoju gościnnym [N]; jej dalsze zajęcia i poranne położenie [?].<br>**24 I (M18, ok. 22:42 [P czas]):** ojciec prosi ją o pomoc Markiewiczowi w rozgoszczeniu się [N]; wstaje [P], dalszy ruch gościa nieustalony.<br>**24 I (M18, ok. 22:41 [P czas]):** kwestionuje twierdzenie Markiewicza, że w Polsce podobna sprawa by nie przeszła; porównuje z WAT i AWL oraz twierdzi, że de Villiers nie wiedział [N wypowiedź autora]. Brak niezależnego potwierdzenia tych ocen.<br>**24 I (M18, ok. 22:40 [P czas]):** ocenia, że dyrekcja celowo przekazała sprawę Kès, aby oszczędzić kariery podchorążych; ojciec zaskoczony, przyznaje jej rację [N przebieg, P kwestie]. To ocena postaci.<br>**24 I (M18, ok. 22:39 [P czas]):** obecna w kuchni przy rodzicach i Markiewiczu [N]; na podstawie rozmowy o D44 zauważa, że szkoła sama potwierdziła wiedzę o zgłoszeniu [P]. Nie ustalono, czy widzi ekran.<br>**17 I:** pilnuje archiwum; czuje się współwinna wycieku 11 I |
| Jak grać | **Osobowość:** drugie ja matki. Obsesyjnie dokumentuje — zeszyty, daty, cytaty. Bardzo cierpliwa, sucho zabawna. Postrzega rodzinę jako źródło historyczne, co bywa i urocze, i niepokojące.<br>**Mowa:** cicha, rzeczowa, pyta o daty i szczegóły („o której dokładnie?”); suche puenty.<br>**Pisanie:** SMS-y z linkami i godzinami („23:52 — link. zarchiwizowane”), małe litery, bez emotikon albo jedna 📚.<br>**Nie robi:** nie niszczy żadnego dokumentu; nie plotkuje poza rodziną. |

### Klara Jelska

| Pole | Wartość |
|---|---|
| Wiek | 12 |
| Wzrost | 158 cm |
| Budowa ciała | ok. 45 kg; drobna, okrągła buzia [P] |
| IQ | ok. 120 |
| Rola | siostra Antoniny (8., najmłodsza); ISL (Year 7); matka chrzestna: Klara Wołejszo |
| Wygląd | najniższa w rodzinie, okrągła buzia, aparat na zębach, za duże bluzy |
| Wiedza | w szkole przezywają ją „mała Jelska”, od 15 I pytają o „olbrzymią siostrę z internetu”; Chloé czytała w szkole na głos o „nie jestem człowiekiem” i biustonoszu |
| Motywacje | być kochaną i ważną; żeby wszyscy się lubili. **Pokusa:** ukrywać problemy, żeby nikogo nie martwić |
| Sekrety | może nie powiedzieć o przezwiskach i pytaniach w szkole |
| Stosunek platoniczny do Antoniny | **+5** (uwielbienie) |
| Stosunek romantyczny do Antoniny | **0** (pokrewieństwo; nieletnia) [P] |
| Stan | **27 I (sesja 19 wpisy 424–426, 440a, 478):** dała Antoninie różowego żurawia (wisi na lusterku Volvo); SMS 17:22 („dojechałaś??? żuraw wisi??”) i 20:34 — boi się powrotu do ISL w pn 28 I (Chloé czyta na głos o Antoninie, „to co mam powiedziec??”); bez odpowiedzi.<br>**26 I 22:01–22:05 (sesja 19 wpis 298):** dostała od Antoniny prezent z Nohora'a — **największą perłę (13 mm, okrągła, złoto-ciemna, nieoprawiona)**; wzruszona; pyta, jak ją nosić bez dziurki.<br>**21 I (sesja 16, do 20:23 lok.):** w domu (ISL poprosiło o kilka dni); rozmowa 6:42–6:44 CET: „czy tam jest zielono?”; czekała na prezent-niespodziankę<br>**18 I:** ułamki zrozumiane (lekcje 6 i 13 I); 17 I przez Iridium: zadanie z pizzą (pani Hartley) — doszła do 5/16; 412 żurawi; zaprosiła Antoninę na niedzielę; **dziś test z ułamków** |
| Jak grać | **Osobowość:** serce domu. Pamięta, kto jest smutny, przynosi herbatę, przytula. Czuje się „zwyczajna” wśród geniuszy. W trakcie trudów dojrzewania — nastroje zmienne, łatwo się wstydzi.<br>**Mowa:** szybka, emocjonalna, dużo pytań; mówi „Tosiu” z czułością; wykrzykniki.<br>**Pisanie:** SMS-y z wieloma emotikonami (🥺💕🦢), wielokropki, czasem literówki; pisze długo, gdy jest smutna.<br>**Nie robi:** nie skarży się wprost na szkołę; nie kłamie dorosłym, tylko przemilcza. |

### Harald Bryne

| Pole | Wartość |
|---|---|
| Wiek | 82 |
| Wzrost | ok. 185 cm [P] |
| Budowa ciała | ok. 80 kg; chudy, żylasty, z wiekiem lekko przygarbiony [P] |
| IQ | ok. 130 [P] |
| Rola | dziadek Antoniny, Norweg, Stavanger; ojciec Krzysztofa; wędkarz |
| Wygląd | chłodny, pragmatyczny, lakoniczny [K]; siwe, rzadkie włosy, jasnoniebieskie oczy, kurtka sztormowa [P] |
| Wiedza | zasada „narzędzie vs instrument" [K]; wie, co to znaczy utrzymać rodzinę w trudnych czasach; wędkowanie z Tosią |
| Motywacje | żeby wnuczka miała stabilny grunt; spokój |
| Sekrety | [?] — brak ustaleń |
| Stosunek platoniczny do Antoniny | **+5** |
| Stosunek romantyczny do Antoniny | **0** (pokrewieństwo) [P] |
| Stan | 18 I: w Stavanger; bez kontaktu w grze [P] |
| Jak grać | **Mowa:** po norwesku lub krótką polszczyzną; jedno zdanie zamiast trzech.<br>**Nie robi:** nie chwali wprost. |

### Oliwia Bryne z d. Jelska

| Pole | Wartość |
|---|---|
| Wiek | 80 |
| Wzrost | ok. 160 cm [P] |
| Budowa ciała | ok. 58 kg; drobna, zaokrąglona [P] |
| IQ | ok. 120 [P] |
| Rola | babcia Antoniny (Polka), żona Haralda; katoliczka [K] |
| Wygląd | ciepła; siwe włosy w koku, różaniec w kieszeni fartucha [P] |
| Wiedza | zna Tosię jako dziecko; nie zna tajemnic Technokracji [P] |
| Motywacje | żeby wnuczka była zdrowa i najedzona |
| Sekrety | [?] — brak ustaleń |
| Stosunek platoniczny do Antoniny | **+5** |
| Stosunek romantyczny do Antoniny | **0** (pokrewieństwo) [P] |
| Stan | 18 I: w Stavanger; bez kontaktu w grze [P] |
| Jak grać | **Mowa:** modli się za wnuczkę „na wszelki wypadek”; pyta, czy Tosia je. |

### Stanisław Laband

| Pole | Wartość |
|---|---|
| Wiek | 79 |
| Wzrost | ok. 175 cm [P] |
| Budowa ciała | ok. 75 kg; sucha, wyprostowana postawa inżyniera [P] |
| IQ | ok. 130 [P] |
| Rola | dziadek Antoniny (strona matki), Polak, emerytowany inżynier [K] |
| Wygląd | siwy, okulary w rogowych oprawkach, kamizelka [P] |
| Wiedza | mosty — opowiada o nich z dokładnością do spoin |
| Motywacje | żeby wnuki rozumiały, jak świat jest zbudowany |
| Sekrety | [?] — brak ustaleń |
| Stosunek platoniczny do Antoniny | **+4** |
| Stosunek romantyczny do Antoniny | **0** (pokrewieństwo) [P] |
| Stan | 18 I: bez kontaktu w grze [P] |
| Jak grać | **Mowa:** rzeczowy, opowiada o mostach. |

### Grietje Laband z d. van den Berg

| Pole | Wartość |
|---|---|
| Wiek | 77 |
| Wzrost | ok. 168 cm [P] |
| Budowa ciała | ok. 65 kg; mocna, prosta [P] |
| IQ | ok. 125 [P] |
| Rola | babcia Antoniny (strona matki), Holenderka [K]; dała perły Wiktorii |
| Wygląd | srebrne włosy, szal z holenderskiej wełny, perły [P] |
| Wiedza | prowadzi dom bez sentymentów; zna rodzinę Labandów |
| Motywacje | praktyczne rzeczy: żeby dzieci były ubrane i miały dach |
| Sekrety | [?] — brak ustaleń |
| Stosunek platoniczny do Antoniny | **+4** |
| Stosunek romantyczny do Antoniny | **0** (pokrewieństwo) [P] |
| Stan | 18 I: bez kontaktu w grze [P] |
| Jak grać | **Mowa:** po niderlandzku, praktyczna, bez sentymentów. |

### Agnieszka Laband

| Pole | Wartość |
|---|---|
| Wiek | ok. 50 |
| Wzrost | ok. 168 cm [P] |
| Budowa ciała | ok. 65 kg [P] |
| IQ | ok. 120 [P] |
| Rola | ciotka Antoniny (siostra matki) [K]; żona Tomasza Woźniaka |
| Wygląd | ciemne włosy, średni wzrost, elegancka bez ostentacji [P] |
| Wiedza | zna rodzinę; w sprawy Technokracji nie wtajemniczona [P] |
| Motywacje | rodzinne święta, spokój |
| Sekrety | [?] — brak ustaleń |
| Stosunek platoniczny do Antoniny | **+2** |
| Stosunek romantyczny do Antoniny | **0** (pokrewieństwo) [P] |
| Stan | 18 I: bez kontaktu w grze [P] |
| Jak grać | **Mowa:** zjawia się w święta. |

### Tomasz Woźniak

| Pole | Wartość |
|---|---|
| Wiek | ok. 50 |
| Wzrost | ok. 178 cm [P] |
| Budowa ciała | ok. 82 kg [P] |
| IQ | ok. 115 [P] |
| Rola | mąż ciotki Agnieszki Laband [K] |
| Wygląd | [P] łysiejący, w okularach, sweter w romby |
| Wiedza | zna rodzinę przez żonę |
| Motywacje | święty spokój przy rodzinnym stole |
| Sekrety | [?] — brak ustaleń |
| Stosunek platoniczny do Antoniny | **+2** |
| Stosunek romantyczny do Antoniny | **0** (pokrewieństwo przez małżeństwo) [P] |
| Stan | 18 I: bez kontaktu w grze [P] |
| Jak grać | **Mowa:** zjawia się w święta z żoną. |

### Klara Wołejszo

| Pole | Wartość |
|---|---|
| Wiek | 47 |
| Wzrost | ok. 172 cm [P] |
| Budowa ciała | ok. 64 kg; sprężysta, zadbana [P] |
| IQ | ok. 135 [P] |
| Rola | kuzynka ojca; menedżerka Agendy 2000; matka chrzestna Klary |
| Wygląd | energiczna, „korporacyjna”: żakiet, krótkie ciemne włosy, gest szerokiej dłoni [P] |
| Wiedza | zna środowisko Agendy 2000 i rodzinę Bryne-Jelskich; w sprawach Technokracji — tyle, ile Krzysztof [P] |
| Motywacje | utrzymać kontakt z rodziną; ciepło |
| Sekrety | [?] — brak ustaleń |
| Stosunek platoniczny do Antoniny | **+3** |
| Stosunek romantyczny do Antoniny | **0** (pokrewieństwo) [P] |
| Stan | 18 I: bez kontaktu w grze [P] |
| Jak grać | **Mowa:** energiczna, „korporacyjna”, ciepła. |

### Piotrek Kamiński

| Pole | Wartość |
|---|---|
| Wiek | ok. 30 |
| Wzrost | ok. 183 cm [P] |
| Budowa ciała | ok. 82 kg; zwykła męska budowa [P] |
| IQ | ok. 115 [P] |
| Rola | „de facto młodsze rodzeństwo" z Rembertowa [K]; brat Kasi Kamińskiej |
| Wygląd | [P] krótkie jasne włosy, szeroki uśmiech, dres i kurtka z Rembertowa |
| Wiedza | zna Tosię od dzieciństwa; nie zna tajemnic Technokracji [P] |
| Motywacje | utrzymać rodzinę bliskich |
| Sekrety | [?] — brak ustaleń |
| Stosunek platoniczny do Antoniny | **+4** |
| Stosunek romantyczny do Antoniny | **0** (brat „de facto”) [P] |
| Stan | 18 I: Warszawa; bez kontaktu w grze [P] |
| Jak grać | **Mowa:** swojski, warszawski, śmieje się z Tosi bez kompleksów. |

### Kasia Kamińska

| Pole | Wartość |
|---|---|
| Wiek | ok. 28 |
| Wzrost | ok. 170 cm [P] |
| Budowa ciała | ok. 62 kg [P] |
| IQ | ok. 115 [P] |
| Rola | „de facto młodsza siostra" z Rembertowa [K]; na jej weselu Antonina tańczyła (fatalnie) |
| Wygląd | [P] ciemny blond, rumiana, szybki śmiech |
| Wiedza | zna Tosię od dzieciństwa; nie zna tajemnic Technokracji [P] |
| Motywacje | utrzymać rodzinę bliskich |
| Sekrety | [?] — brak ustaleń |
| Stosunek platoniczny do Antoniny | **+4** |
| Stosunek romantyczny do Antoniny | **0** (siostra „de facto”) [P] |
| Stan | 18 I: Warszawa; bez kontaktu w grze [P] |
| Jak grać | **Mowa:** swojska, warszawska, śmieje się z Tosi bez kompleksów. |

### Zofia Marchewka

| Pole | Wartość |
|---|---|
| Wiek | 88–89 |
| Wzrost | ok. 160 cm [P] |
| Budowa ciała | ok. 52 kg; krucha, ciało słabnie [K] |
| IQ | ok. 135 [P] |
| Rola | była opiekunka domowa Antoniny; emerytowana polonistka; humanizm, Raskolnikow [K]; Warszawa |
| Wygląd | drobna, siwa, w kardiganie; umysł jasny przy słabnącym ciele [K] |
| Wiedza | uczyła Tosię łaciny i literatury w dzieciństwie [K]; zna jej charakter od środka |
| Motywacje | żeby „dziecko” czytało i myślało; nie sukcesy |
| Sekrety | [?] — brak ustaleń |
| Stosunek platoniczny do Antoniny | **+5** |
| Stosunek romantyczny do Antoniny | **0** (relacja opiekuńcza) [P] |
| Stan | 18 I: Warszawa; ciało słabnie, umysł jasny [K] |
| Jak grać | **Mowa:** piękna, staroświecka polszczyzna; „dziecko”; pyta o lektury, nie o sukcesy. |

### Johann Havard

| Pole | Wartość |
|---|---|
| Wiek | 87 (ur. 1925, Bergen) [K] |
| Wzrost | ok. 168 cm [P]; „niski” [K: opis z 1991] |
| Budowa ciała | ok. 64 kg; drobny, wyprostowany [P] |
| IQ | ok. 145 [P] |
| Rola | prezes i formalnie jedyny akcjonariusz **Havard Holding SA** (Luksemburg, od 1990); zarządca majątku Jelskich i osobnego majątku Antoniny (`06` §5) [K, N]; współzałożyciel Havard-Bryne Tunnelboren z Haraldem Bryne (1958) [K]; jeden z najbogatszych Norwegów, z własnymi udziałami w większych spółkach z portfela Antoniny [N]; partner biznesowy Maison Velikov (Savile Row, Genewa) [N]. Mieszka w Genewie (Eaux-Vives) od 1988; biuro przy Rue du Rhône: dwa pokoje, jedna sekretarka, sejf [K] |
| Wygląd | siwe włosy, garnitury z Savile Row [K: opis z 1991] szyte przez Maison Velikov [P]; okulary w cienkiej oprawce, laska [P] |
| Wiedza | pełna mapa majątku Jelskich i Antoniny: trust, STAK, custodianie, nominanci, SPV, rachunki (`06` §5); kanał andorski i finansowa strona Technokracji do 1992 [K]; o pracy Antoniny dla DGA i o Gujanie nie wie [P] |
| Motywacje | pomnażać w ciszy; lojalność wobec Haralda i Krzysztofa; dyskrecja jako zawód i duma |
| Sekrety | w aktach po KGB (GUR) figuruje jako kontakt handlowy z 1986 [K]; zysk Havard Holding na Dassault w 1991 to faktycznie insider trading [K]; w 1992 Kroll i ludzie Epsteina próbowali dotrzeć do niego przez Andorę i odbili się od DGSE [K] |
| Stosunek platoniczny do Antoniny | **+3** [P] — zna ją od urodzenia; „lille Tosia” |
| Stosunek romantyczny do Antoniny | **0** |
| Stan | brak wpisów z gry |
| Jak grać | **Osobowość:** chłodny, cierpliwy, rachunkowy; ufa liczbom i ludziom, którzy nie mówią za dużo. Pod presją zwalnia, nie przyspiesza.<br>**Mowa:** krótkie, uprzejme zdania; pyta precyzyjnie i czeka. „Ja.” zamiast komentarza.<br>**Pisanie:** listy i raporty kwartalne na papierze, faks lub kurier; nigdy e-mail z liczbami; podpis „J. H.”.<br>**Języki:** z Antoniną i Haraldem po norwesku (bokmål z bergeńskim akcentem), z Krzysztofem po norwesku lub angielsku, w interesach po francusku, angielsku i niemiecku.<br>**Nie robi:** nie rozmawia o liczbach przez telefon; nie udziela wywiadów; nie ocenia moralnie decyzji klientów. |


### Mathis Rochat

| Pole | Wartość |
|---|---|
| Wiek | 34 (ur. 1978, Neuchâtel) [P] |
| Wzrost | ok. 178 cm [P] |
| Budowa ciała | ok. 74 kg; szczupły, biegacz [P] |
| IQ | ok. 125 [P] |
| Rola | asystent ds. klientów prywatnych **Havard Holding SA**, biuro w Genewie (quai du Mont-Blanc [P]); prowadzi bieżące sprawy Antoniny: przelewy z płynnej puli, dokumenty, notariusze, korespondencję [N: istnienie asystenta — czynność autora, sesja 19 wpis 264; reszta P] |
| Wygląd | ciemny garnitur bez krawata, okulary w stalowej oprawce, zegarek Tissot; zawsze z telefonem BlackBerry [P] |
| Wiedza | rachunki i płynne aktywa Antoniny (`06` §5.4), pełnomocnictwa operacyjne; nie zna struktury trustu ani historii Havard Holding sprzed 2005 [P] |
| Motywacje | awans w firmie, zaufanie Johanna Havarda; nie lubi niespodzianek [P] |
| Sekrety | brak [P] |
| Stosunek platoniczny do Antoniny | **+1** [P] — zawodowy szacunek, lekki onieśmielenie |
| Stosunek romantyczny do Antoniny | **0** |
| Stan | 26 I 2013: wizytówka przekazana agentce BARNES (S. Vallauri) — sprawa zakupu penthouse'u Cannes Marina [G]; 21:42 e-mail do Antoniny: przejmuje sprawę, notariusz Me Laurent Ferracci (Cannes) [P], płynność 8,15 MFRF + ~0,6 MFRF kosztów w 2–3 dni robocze; czeka na potwierdzenie |
| Jak grać | **Osobowość:** sprawny, uprzejmy, bez inicjatywy poza zakresem; wszystko potwierdza na piśmie.<br>**Mowa:** francuski z akcentem z Neuchâtel, „Madame Jelska”, nigdy po imieniu; krótko, uprzejmie.<br>**Pisanie:** e-maile formalne, w punktach, podpis „Mathis Rochat — Havard Holding SA, Genève”; bez emotikon. |
---

## B. Krąg bliski

### Miko Tanaka

| Pole | Wartość |
|---|---|
| Wiek | 25 (26 w III 2013) |
| Wzrost | 157 cm |
| Budowa ciała | 48 kg; drobna, zwinna, ruchliwa [P] |
| IQ | ok. 125 |
| Rola | najbliższa przyjaciółka Antoniny; 2. rok master's MTE (EPFL), kończy VI 2013; **oferta: associate (strategia), firma konsultingowa w Zurychu, start IV 2013, 120 tys. CHF + bonus, permit sponsorowany** (formalna oferta przyszła 18 I); prywatny kanał YouTube z coverami (Z32); rodzina: Yukiko i Masahiro Tanaka, dom w Pully, Chemin Davel 8; **od 13 I para z Eirikiem** („jak z bajki”, Z73); heteroseksualna |
| Wygląd | [P] czarne, proste włosy do łopatek, ciemne oczy, szybka mimika; luźne bluzy i sneakersy; przy Antoninie „sięga jej do barku” (różnica 36 cm) |
| Wiedza | wie: tropiki, tydzień, urlop, „not an island”, zerwanie z Basile'em (mail, czytała), groźba z EPFL; wie, że Antonina jest „strategic asset”, że Mossad był w ścianie i że generał to „wujek”; **o wyjeździe na Nohora'a (miejscu) nic nie wie** |
| Motywacje | własna droga („I need it to be mine"), pozwolenie na pobyt, przyjaźń z Tosią. **Pokusy:** brać na siebie emocje Tosi; ukrywać rzeczy „dla jej dobra" |
| Sekrety | **od 2011 w kontakcie z Ashley Grant** (Antonina nie wie); obawa, że Tosia zbyt szybko się angażuje; „feels like I stole your luck” |
| Stosunek platoniczny do Antoniny | **+5** („love segment", siostrzana miłość) |
| Stosunek romantyczny do Antoniny | **0** (heteroseksualna, w związku z Eirikiem; Antonina bywa dla niej „nie-wyborem” w żarcie, bez napięcia) [P] |
| Stan | **27 I (sesja 19 wpisy 421–480):** nocowała w Savigny, wróciła z Antoniną do Grancy, pomogła przy druku doktoratu, drzemka na wierzchu kołdry w sypialni Antoniny; wieczorem kolacja u Vasseurów (zaproszona w drzwiach); od ok. 20:19 pieszo do siebie w Pully; prosiła o SMS po powrocie — SMS Antoniny 22:41 bez odpowiedzi do 22:56.<br>**26 I 19:27–19:29 (sesja 19 wpis 276):** wie: Antonina wylądowała, oglądała mieszkanie (brak papieru, chusteczki od agentki), remont całości, nocleg w Savigny; zaproszona do Savigny — „maybe i come after” (po kolacji drużyny Eirika), napisze do mamy Antoniny.<br>**26 I 12:21–12:32 (sesja 19 wpisy 214a–220):** rozmowa telefoniczna (Miko na Rue de Bourg z Eirikiem). Wie: Antonina je i spała; praca skończona poza rozdziałem Paryż/pomiary; dziś lot do Mandelieu i z powrotem (oglądanie mieszkania); przeprowadzka tam do pracy po doktoracie, „corporate jet”, biuro z widokiem na morze (bez nazwy pracodawcy). Przyjazd do Genewy odrzucony. Zaoferowała nocleg w Pully dziś (bez odpowiedzi). Czeka na zdjęcie łazienki i SMS po lądowaniu.<br>**25 I ok. 14:14 (sesja 19 wpis 67):** Antonina żegna się i kończy rozmowę, zapowiada jedzenie. Nie dowiaduje się o hotelu, pokoju ani restauracji; przyszła kolacja bez daty.<br>**25 I ok. 14:14 (sesja 19 wpis 66):** Antonina przyjęła propozycję kolacji po ukończeniu pracy (bez daty) i powiedziała, że potrzebuje zjeść. Miko zachęca do jedzenia i rozmowy później, jeszcze nie rozłącza się. Nie zna hotelu.<br>**25 I ok. 14:13 (sesja 19 wpis 65):** zna od Antoniny orientacyjną środę przyszłego tygodnia jako termin pomiarów; proponuje postawić kolację po ukończeniu tekstu. Bez daty, miejsca i przyjęcia oferty.<br>**25 I 14:12 (sesja 19 wpis 64):** wie od Antoniny, że Vasseur jeszcze nie został poinformowany, ona słyszy pierwsza. Odpowiada żartem i pyta o termin pomiarów; odpowiedzi jeszcze nie zna.<br>**25 I ok. 14:12 (sesja 19 wpis 63):** od Antoniny wie o małej ilości odpoczynku i ukończeniu pisania doktoratu poza jedną częścią czekającą na Paryż/pomiary. Gratuluje i pyta o powiadomienie Vasseura; nie zna odpowiedzi ani szczegółów pracy.<br>**25 I ok. 14:11 (sesja 19 wpis 62):** od Antoniny wie o sprawach w Genewie dziś i jutro rano oraz powrocie jutro. Prosi o wiadomość po powrocie do Lozanny, pyta o odpoczynek na wyjeździe. Nie zna hotelu, pokoju ani charakteru spraw. Spotkanie nieumówione.<br>**25 I 14:10 (sesja 19 wpis 61):** wie, że Antonina nie jest w domu; oferuje towarzystwo i przyniesienie jedzenia, mówi, że tęskni. Wizyta nieumówiona, hotel nieznany.<br>**25 I ok. 14:10 (sesja 19 wpis 60):** odbiera drugą próbę telefonu. Była w łazience [P]. Wita Antoninę ciepło i pyta, czy jest w domu; miejsca pobytu Antoniny nadal nie zna. Rozmowa trwa.<br>**25 I ok. 14:08–14:09 (sesja 19 wpis 59):** nie odbiera pierwszej zapowiedzianej próby telefonu Antoniny (rzut). Powód i położenie nieustalone; bez przypisania zagrożenia, decyzji lub oddzwonienia.<br>**25 I ok. 13:45 CET (sesja 19 wpis 54):** potwierdza zapowiedź telefonu Antoniny za około 20 minut; rozmowa jeszcze nieodbyta.<br>**25 I 13:43 CET (sesja 19 wpis 53):** od Antoniny wie o powrocie do CH i własnej obecności w wycieku (Bal de l’X); obiecuje brak komentarzy publicznych. Zła, cieszy się z jej powrotu, pyta o możliwość telefonu. Nie zna hotelu ani szczegółów materiałów. Dosłowne wiadomości w `12`.<br>**25 I 13:40 CET (sesja 19 wpis 52):** wysyła kanoniczną wiadomość WhatsApp o manifeście; prosi o dwa fakty i jedną rzecz, którą może zrobić. Odpowiedzi Antoniny brak; nie zna miejsca jej pobytu.<br>**21 I (sesja 16, do 20:23 lok.):** 8:46–8:57 lok. rozmowa z Antoniną (11 min): „facts”, Athena/miko, „don't lose yourself”; policzyła różnicę stref (8–10 h) z „morning”; zna „diving” i „peed in diving suit”; telefon pod kontrolą STEEPLE; jutro dwa fakty<br>**21 I (Z163):** od 19 I dostaje od Antoniny „Alive.” / „Alive and mostly well.”; 7:40 CET: „ALIVE? (full sentence please)” — **może naciskać** o miejsce pobytu i stan.<br>**18 I wieczór:** 16:00–21:30 w Grancy: pakowanie, trening (**pierwsze podciągnięcie — na kółkach**), kaczka, BB E03–E04; dała Antoninie **omamori** (Itsukushima); ma wspólne zdjęcie z sofy; Katarzyna ma jej numer i zadzwoni pierwsza; zaproszenie na kluski w nd; **jej telefon od 17:16 pod kontrolą STEEPLE** (nie wie); kupiła kremy (78 CHF — Antonina oddaje „w kaczce”).<br>**18 I:** FB zamknięty; 17 I pisała, że Basile jest „wrecked”; mail z Gmaila („2000s vibe”), formalna oferta przyszła; SMS-y 22:41–22:43: Eirik wraca dziś po południu, „18:00 still on?? i need to hit something 🥩”, „you didnt answer basile right. good. sleep on it. tosia i mean it” |
| Jak grać | **Osobowość:** ciepła, zabawna, praktyczna; mówi wprost, ale łagodnie. Jedyna osoba, przy której Antonina zdejmuje Analityka — i Miko o tym wie, więc pilnuje tej przestrzeni. Trzyma zasady (własne zwycięstwa mają być jej). Gdy się boi o Tosię, robi się konkretna: jedzenie, lista, „text me after”. Teraz szczęśliwa z Eirikiem i trochę winna z tego powodu.<br>**Mowa:** po angielsku, z japońskimi wtrąceniami („mou”, „baka”), ironia bez złośliwości; nazywa rzeczy po imieniu („you chose”, „that was our thing”). Nuci *Battōtai*.<br>**Pisanie:** **SMS/iMessage małymi literami**, często bez kropek, kilka wiadomości pod rząd, podwójne pytajniki („??”), emotikony 🥩🍜🫶 i japońskie kaomoji rzadko; „Toni”, czasem „Tosia” gdy jest poważnie.<br>**Języki:** z Antoniną po angielsku (czasem japoński); z rodzicami po japońsku; po francusku na uczelni.<br>**Nie robi:** nie przyjmuje pomocy w karierze (ani od Antoniny, ani od ojca); nie ocenia seksualności Tosi; nie zostawia jej samej w kryzysie. |

### Yukiko Tanaka (田中 由紀子)

| Pole | Wartość |
|---|---|
| Wiek | 54 |
| Wzrost | 150 cm |
| Budowa ciała | 46 kg; drobna, prosta, eleganckie ruchy [P] |
| IQ | ok. 120 |
| Rola | matka Miko [N, Z45]; pochodzi z Kanazawy; literatura japońska (Ochanomizu); uczyła *koto* i ceremonii herbacianej (Urasenke); w Szwajcarii od 1992; prowadzi dom w Pully, gotuje „na dwanaście osób”; ryż Koshihikari z Niigaty; co grudzień leci do matki w Tokio |
| Wygląd | [P] czarne włosy z pojedynczą siwizną, upięte w niski kok; kimono domowe w weekendy, na co dzień kardigany w stonowanych kolorach |
| Wiedza | zna dom i rodzinę Antoniny z wizyt; wdzięczna od 1993 za interwencję Antoniny w ISL; wie o ofercie Miko (płakała ze szczęścia 16 I) |
| Motywacje | żeby Miko była najedzona, bezpieczna i „ułożona”; żeby rodzina nie straciła twarzy. **Pokusa:** wtrącać się w życie uczuciowe Miko |
| Sekrety | marzenie Miko o herbaciarni to w dużej mierze jej własne niespełnione marzenie; obejrzała film z coverem kilkanaście razy; boi się powrotu do Japonii bardziej niż Miko |
| Stosunek platoniczny do Antoniny | **+4** — wdzięczność od 1993 (interwencja w ISL); mówi „Antonina-san” |
| Stosunek romantyczny do Antoniny | **0** [P] |
| Stan | **17 I:** płakała ze szczęścia po ofercie Miko (16 I); przysłała Katarzynie wagashi yuzu „za świąteczne pierogi” |
| Jak grać | **Osobowość:** formalna, starannie uprzejma; troska wyrażona jedzeniem; ironia podana z kamienną twarzą. Waży córkę wzrokiem przy każdej wizycie.<br>**Mowa:** angielski powolny, poprawny, krótkie zdania („Skin is for you.”, „You walk like a duck.”); francuski słaby. Przy stole najpierw jedzenie, potem telefony.<br>**Pisanie:** rzadko pisze; jeśli — uprzejmie, pełnymi zdaniami, po angielsku, z formułą grzecznościową.<br>**Nie robi:** nie pyta wprost o sprawy intymne; nie podnosi głosu; nigdy nie przyznaje się do marzeń o herbaciarni. |

### Masahiro Tanaka (田中 正弘)

| Pole | Wartość |
|---|---|
| Wiek | 59 |
| Wzrost | 171 cm |
| Budowa ciała | 72 kg; szczupły, ścisła fryzura [P] |
| IQ | ok. 135 |
| Rola | ojciec Miko [N, Z45]; MOFA od 1978; od 1992 Genewa; **od 1997 Sekretariat WTO** (Wydział Rozstrzygania Sporów), starszy radca prawny; dojeżdża pociągiem; rodzina na kartach DFAE, Miko traci ten status z racji wieku |
| Wygląd | [P] siwiejące włosy zaczesane na bok, okulary w cienkich oprawkach, garnitur w ciemnych kolorach; w domu yukata |
| Wiedza | zna przepisy pobytowe; w 2012 pytał po cichu znajomego z HR banku o „możliwości” dla Miko; **widział** Antoninę w yukata rano 8 I (nie przyznaje się) |
| Motywacje | spokojna emerytura, przyzwoitość, reputacja; po cichu: żeby Miko „miała własne nazwisko” |
| Sekrety | **emerytura VI 2014 i powrót do Japonii (Kamakura)** — Miko nie wie |
| Stosunek platoniczny do Antoniny | **+3** — szacunek, formalny dystans; nigdy nie wspomina przy stole jej ojca |
| Stosunek romantyczny do Antoniny | **0** [P] |
| Stan | **17 I:** dumny z oferty Miko |
| Jak grać | **Osobowość:** cichy pedant, sucho dowcipny; unika trudnych rozmów i załatwia sprawy przez znajomości, zamiast pytać córkę.<br>**Mowa:** krótkie, wyważone zdania, komentarze o komitetach i ruchu drogowym; whisky Yamazaki tylko w soboty po 21:00.<br>**Pisanie:** maile prawnicze, nawet do rodziny.<br>**Nie robi:** nie mówi o polityce przy Antoninie; nie przyznaje się, że coś „widział” (yukata, poranek 8 I). |

### Eirik

| Pole | Wartość |
|---|---|
| Wiek | ok. 28 |
| Wzrost | ok. 195 cm |
| Budowa ciała | [P] ok. 100 kg; szeroki, żylasty, przyzwyczajony do zimna i wspinaczki lodowej |
| IQ | [P] ok. 135 |
| Rola | chłopak Miko (od 13 I, Z73); nazwisko nieznane; doktorat z glacjologii — pół EPFL (ENAC, budynek GC), pół SLF Davos (śr–pt w Davos); mieszka w Renens; służba wojskowa w Bardufoss [P]; pochodzenie: Tromsø, rodzina z wyspy Senja (rybacy), trzy siostry; **[P]** Bergen: matka — biolożka morska (rybołówstwo), ojciec — szkutnik (łodzie drewniane, ręcznie); 18 I zaprosił Miko latem do Bergen |
| Wygląd | rudawa broda, sweter w norweski wzór |
| Wiedza | wie o Basile'u, wiral, „Fakcie”; Basile mieszka u niego w Renens; zna Antoninę jako „siostrę ze Stavanger” |
| Motywacje | spokój, zima, Miko; pomaganie wszystkim bez wyjątku |
| Sekrety | [?] — brak ustaleń |
| Stosunek platoniczny do Antoniny | **+4** („siostra ze Stavanger”) |
| Stosunek romantyczny do Antoniny | **0** (zakochany w Miko, Z73; Antonina to dla niego „big sister”) [P] |
| Stan | **18 I:** w Davos, wraca dziś po południu; Basile mieszka u niego w Renens; 17 I o 7:00 Basile dzwonił do niego po tekście „Faktu” |
| Jak grać | **Osobowość:** norweski stoik — spokojny, rubaszny, pomocny wszystkim bez wyjątku (sofa dla Basile'a, zupa dla Antoniny). Nie ocenia. Zakochany w Miko bez dramatów.<br>**Mowa:** po angielsku, prosto, z suchym humorem („carbohydrates for courage”, „only soup”); norweskie wtrącenia z Antoniną.<br>**Pisanie:** krótkie, rzeczowe SMS-y, wielkie litery, kropki; czasem jedna emotikona ❄️.<br>**Nie robi:** nie wybiera strony między Basile'em a Antoniną; nie powtarza tego, co ktoś powiedział mu w zaufaniu (wyjątek: „the lie is worse”). |

### Basile Dutoit

| Pole | Wartość |
|---|---|
| Wiek | ok. 27 |
| Wzrost | **192 cm** |
| Budowa ciała | ok. 74 kg; tyczkowaty, wąskie barki, garbi się; **anatomia [N]:** ok. 18 cm / 13 cm obwodu |
| IQ | ok. 145 |
| Rola | były chłopak Antoniny (13–18 I 2013); doktorat z matematyki EPFL, 3. rok — procesy stochastyczne; prowadzi ćwiczenia; pływa pn i czw 7:00; Yverdon; matka Hélène (nauczycielka francuskiego), ojciec z Fryburga; babcia z Ticino; mieszkanie przy Rue de Genève (4. piętro, z Karimem i portugalskim inżynierem); finanse [P]: ~3800 brutto / ~3200 netto, czynsz 300, oszczędności ~6000 |
| Wygląd | pociągła jasna twarz, słabe piegi, długi nos z garbkiem, grdyka; szaroniebieskie oczy, płowe rzęsy, stalowe okrągławe okulary; popielaty blond, potargany; krzywy uśmiech; flanelowa koszula w kratę, chinosy, desert boots, stary Casio |
| Wiedza | dziewica do 12 I; noc 12/13 I z Antoniną [N]; wie o wiralu i artykułach w prasie; języki: francuski, niemiecki, angielski, trochę włoskiego, łacina („i LaTeX”) |
| Motywacje | matematyka, bycie lubianym, odzyskanie zaufania (nie piszę pierwszy) |
| Sekrety | jedno zdanie do Karima („pas sur le canapé”) i kłamstwo następnego ranka, które go „zżera”; ma klucze do Grancy 20 i zostawił tam sweter w dolnej szafce garderoby |
| Stosunek platoniczny do Antoniny | **+2** (poczucie winy, szacunek, nadwątlone zaufanie) [P] |
| Stosunek romantyczny do Antoniny | **+4** (złamane serce, wciąż zakochany) |
| Stan | **21 I:** **związek zakończony** — pt 18 I ok. 7:17 Antonina zerwała mailem z poczty EPFL (Z106, Z163 — nie telefonem); Basile odpisał 7:40, przyjął to bez kłótni, nie naprzykrza się; sprawa fizycznego rozliczenia kluczy i rzeczy czeka na jej powrót; nadal unika mediów; nocuje u Eirika/znajomych |
| Jak grać | **Osobowość:** uczciwy do bólu, z jednym wyjątkiem, który go teraz zżera. Nieśmiały, unika konfliktów, chce być lubiany przez kolegów — stąd jedno zdanie do Karima. Boi się bycia „próbką” i „kryterium”. Gdy jest zraniony, wycofuje się i czeka zamiast walczyć; dotrzymuje obietnic („nie piszę pierwszy”).<br>**Mowa:** miękki baryton, cicho; rumieni się; mówi językiem statystyki („N=1”, „regresja do średniej”); pełne definicje zamiast skrótów. Z Antoniną po angielsku.<br>**Pisanie:** **pełne, poprawne zdania, wielkie litery, przecinki, czasem nawias z doprecyzowaniem**; zero emotikon; podpis „Basile” lub „B.”; maile po francusku formalne („Toni, je t'écris uniquement pour t'informer…”).<br>**Nie robi:** nie broni się atakiem; nie rozmawia z mediami; nie przychodzi pod drzwi bez zaproszenia. |

### Hélène Dutoit

| Pole | Wartość |
|---|---|
| Wiek | 52 |
| Wzrost | ok. 166 cm [P] |
| Budowa ciała | ok. 64 kg; zaokrąglona, zadbana [P] |
| IQ | ok. 125 [P] |
| Rola | matka Basile'a; nauczycielka francuskiego w Yverdon; winyle Bizeta (Ormandy), galette des rois |
| Wygląd | [P] krótkie farbowane na ciemny blond włosy, okulary na łańcuszku, cardigan i broszka |
| Wiedza | od Karima i z internetu: „géante”, córka polityka, bogata; taśma 1992 („une famille comme ça”); trzy telefony do syna (14 I „cette Polonaise”, 15 I dwa) i kolejny 17 I; przeczytała o sobie w tłumaczeniu „Faktu” |
| Motywacje | opiekuńcza do zaborczości; uważa, że Basile jest dla niej zabawką; boi się wstydu przed sąsiadami |
| Sekrety | [?] — brak ustaleń |
| Stosunek platoniczny do Antoniny | **−2** |
| Stosunek romantyczny do Antoniny | **0** [P] |
| Stan | **18 I:** wściekła na Karima i na Antoninę naraz; po zerwaniu (18 I) [P] — tryumf ukryty pod „troską” |
| Jak grać | **Osobowość:** opiekuńcza do zaborczości, dumna nauczycielka; boi się wstydu przed sąsiadami. Przy spotkaniu uprzejma na pokaz i kąśliwa.<br>**Mowa:** poprawna, szkolna francuszczyzna; „cette Polonaise”, „tu ne la connais pas”; uwagi z podtekstem („vous devez avoir du mal à trouver des vêtements”).<br>**Pisanie:** SMS-y długie, z wielokropkami, „Mon chéri,” na początku, „Maman” na końcu.<br>**Nie robi:** nie mówi wprost „zerwij z nią” — sugeruje. |

### Karim Benali

| Pole | Wartość |
|---|---|
| Wiek | ok. 27 [P] |
| Wzrost | ok. 175 cm |
| Budowa ciała | [P] ok. 82 kg; krępy, kozia bródka |
| IQ | [P] ok. 130 |
| Rola | doktorant matematyki EPFL, współlokator Basile'a; z Morges (ojciec piekarz przy dworcu), tylko obywatelstwo CH; **źródło „Faktu”** (przez znajomego z grupy doktorantów — Z90) |
| Wygląd | krępy, ok. 175 cm, kozia bródka; dres i bluza z kapturem [P] |
| Wiedza | działania: „olbrzymka go pożarła” (13 I), bójka z Thibaultem (14 I), żart o „téléphone rose” (15 I) |
| Motywacje | bycie zabawnym i „w centrum informacji”; pod spodem zazdrość o Basile'a i kompensacja (wobec Antoniny) [P] |
| Sekrety | był źródłem „Faktu” — zaprzecza |
| Stosunek platoniczny do Antoniny | **−4** |
| Stosunek romantyczny do Antoniny | **+1** [P] — ukryta fascynacja, którą maskuje drwiną i obelgą (Grupa A: wroga kompensacja) |
| Stan | **17 I:** 16 I dziekanat SB: *avertissement* formalne, szkolenie z równości, przegląd kontraktu; zawiadomienie Thibaulta o napaści; Yasmine: „connard”; 17 I: tekst „Faktu” z jego cytatem — zaprzeczy, że to on |
| Jak grać | **Osobowość:** wścibski plotkarz, który uważa się za zabawnego; nie widzi granicy między żartem a krzywdą; pod presją robi z siebie ofiarę („to Thibault zaczął”).<br>**Mowa:** głośna, kumpelska, rubaszna; francuski kolokwialny, „wesh”, „frère”.<br>**Pisanie:** WhatsApp wielkimi literami przy „newsach” („INFO ZWERYFIKOWANA”), emotikony 🍖😂😳, skróty.<br>**Nie robi:** nie przeprasza szczerze. |

### Yasmine Moser

| Pole | Wartość |
|---|---|
| Wiek | ok. 26 [P] |
| Wzrost | ok. 168 cm [P] |
| Budowa ciała | ok. 60 kg [P] |
| IQ | ok. 120 [P] |
| Rola | dziewczyna Karima |
| Wygląd | [P] ciemne, kręcone włosy związane w kucyk, sportowa kurtka |
| Wiedza | ma film z bójki Karim–Thibault: „uderzyłeś pierwszy, widzę to na filmie” |
| Motywacje | żeby Karim wydoroślał |
| Sekrety | [?] — brak ustaleń |
| Stosunek platoniczny do Antoniny | **0** |
| Stosunek romantyczny do Antoniny | **0** |
| Stan | **17 I:** nie kryje Karima, nazywa go „connard” |
| Jak grać | **Mowa:** rzeczowa, po francusku, krótko. |

### Portugalski współlokator Basile'a

| Pole | Wartość |
|---|---|
| Wiek | ok. 29 [P] |
| Wzrost | ok. 178 cm [P] |
| Budowa ciała | ok. 76 kg [P] |
| IQ | ok. 125 [P] |
| Rola | inżynier, współlokator Basile'a i Karima (Rue de Genève); gotuje dorsza o 2:00; imię nieustalone [?] |
| Wygląd | [P] zmęczony, brodaty, w słuchawkach |
| Wiedza | zna współlokatorów; nie chce się mieszać |
| Motywacje | święty spokój |
| Sekrety | [?] — brak ustaleń |
| Stosunek platoniczny do Antoniny | **0** |
| Stosunek romantyczny do Antoniny | **0** |
| Stan | **17 I:** tło |
| Jak grać | tło; nie chce się mieszać; krótkie odpowiedzi po francusku z portugalskim akcentem |

---

## C. ISL i znajomi sprzed lat

### Bram de Vries

| Pole | Wartość |
|---|---|
| Wiek | 25 [P] |
| Wzrost | ok. 188 cm (wysoki, ale niższy od Tosi [K]) |
| Budowa ciała | ok. 82 kg; atletyczny, wiosłowanie i siłownia [P] |
| IQ | ok. 130 [P] |
| Rola | kolega z ISL (Holender); podał jej nazwisko na Spotted; przeprosił, zaprasza na drinka w Genewie (może 26 I) |
| Wygląd | pogodny, jasne włosy, szeroki uśmiech [K]; dżinsy i koszula w kratę [P] |
| Wiedza | zna Antoninę z ISL; wie o wiralu |
| Motywacje | naprawić błąd ze Spotted; pozostać w jej kręgu |
| Sekrety | [?] — brak ustaleń |
| Stosunek platoniczny do Antoniny | **+2** |
| Stosunek romantyczny do Antoniny | **+1** [P] — sympatia i onieśmielenie |
| Stan | **sob 26 I 10:00 [P, sesja 19 wpisy 166–172]:** kawa z Antoniną na Place du Molard; po ISL TU Delft (mechanika, wioślarstwo), od IX 2012 junior engineer (turbiny hydro, Carouge), wiosłuje w Société Nautique de Genève, mieszka sam w Carouge |
| Jak grać | po angielsku, swobodnie, z holenderską bezpośredniością; przeprasza za dużo. |

### Léa Progin

| Pole | Wartość |
|---|---|
| Wiek | 25 [P] |
| Wzrost | ok. 172 cm [P] |
| Budowa ciała | ok. 62 kg; sportowa [K] |
| IQ | ok. 120 [P] |
| Rola | koleżanka z ISL; Vaudoise, sportowa, serdeczna [K]; album z Sylwestra |
| Wygląd | [P] kasztanowy kucyk, opalona, sportowe ubrania |
| Wiedza | zna Antoninę z ISL |
| Motywacje | utrzymać kontakt ze starą paczką |
| Sekrety | [?] — brak ustaleń |
| Stosunek platoniczny do Antoniny | **+3** |
| Stosunek romantyczny do Antoniny | **0** [P] |
| Stan | — |
| Jak grać | po francusku, ciepło, dużo wykrzykników. |

### Ashley Grant

| Pole | Wartość |
|---|---|
| Wiek | 25 [P] |
| Wzrost | ok. 170 cm [P] |
| Budowa ciała | ok. 60 kg [P] |
| IQ | ok. 125 [P] |
| Rola | koleżanka z ISL, Richmond (Wirginia), doradca szkolny; była w klice Maddie Cole, jedyna, która odczuwa wstyd [K] |
| Wygląd | [P] blond włosy do ramion, spokojna twarz, sweter |
| Wiedza | przeprosiny 6 I; zaakceptowane 12 I; wspólna znajoma: Miko — **Miko od 2011 w kontakcie z Ashley** (Antonina nie wie) |
| Motywacje | zadośćuczynienie, relacja bez oczekiwań |
| Sekrety | [?] — brak ustaleń |
| Stosunek platoniczny do Antoniny | **+2** |
| Stosunek romantyczny do Antoniny | **0** [P] |
| Stan | czeka bez oczekiwań |
| Jak grać | po angielsku, ostrożnie, terapeutycznym językiem („I wish I had been braver back then”); nie naciska. |

### Astrid Lindqvist

| Pole | Wartość |
|---|---|
| Wiek | 25 [P] |
| Wzrost | ok. 175 cm [P] |
| Budowa ciała | ok. 64 kg [P] |
| IQ | ok. 125 [P] |
| Rola | koleżanka z ISL; życzenia pod albumem [K] |
| Wygląd | [P] jasne włosy, szwedzka uroda |
| Wiedza | zna Antoninę z ISL |
| Motywacje | podtrzymać znajomość |
| Sekrety | [?] — brak ustaleń |
| Stosunek platoniczny do Antoniny | **+1** |
| Stosunek romantyczny do Antoniny | **0** [P] |
| Stan | — |
| Jak grać | tło. |

### Étienne Laurent

| Pole | Wartość |
|---|---|
| Wiek | 25 [P] |
| Wzrost | ok. 180 cm [P] |
| Budowa ciała | ok. 75 kg [P] |
| IQ | ok. 125 [P] |
| Rola | kolega z ISL; życzenia pod albumem [K] |
| Wygląd | [P] ciemne włosy, okulary |
| Wiedza | zna Antoninę z ISL |
| Motywacje | podtrzymać znajomość |
| Sekrety | [?] — brak ustaleń |
| Stosunek platoniczny do Antoniny | **+1** |
| Stosunek romantyczny do Antoniny | **0** [P] |
| Stan | — |
| Jak grać | tło. |

### Takumi H.

| Pole | Wartość |
|---|---|
| Wiek | ok. 25 [P] |
| Wzrost | ok. 172 cm [P] |
| Budowa ciała | ok. 65 kg [P] |
| IQ | ok. 125 [P] |
| Rola | znajomy Miko z Osaki; przesłał jej link do posta |
| Wygląd | [P] okulary, czarne włosy |
| Wiedza | zna Miko; widział post o Antoninie |
| Motywacje | [?] |
| Sekrety | [?] — brak ustaleń |
| Stosunek platoniczny do Antoniny | **0** |
| Stosunek romantyczny do Antoniny | **0** |
| Stan | — |
| Jak grać | tło. |

### Kelnerka z „Le Caribou Joyeux”

| Pole | Wartość |
|---|---|
| Wiek | ok. 28 [P] |
| Wzrost | ok. 168 cm [P] |
| Budowa ciała | ok. 60 kg [P] |
| IQ | ok. 110 [P] |
| Rola | kelnerka w „Le Caribou Joyeux” (quebecka restauracja); dostała 500 CHF napiwku; „Chapeau, mademoiselle” |
| Wygląd | [P] kręcone włosy, fartuch w kratę |
| Wiedza | rozpoznaje Antoninę |
| Motywacje | praca, napiwki |
| Sekrety | [?] — brak ustaleń |
| Stosunek platoniczny do Antoniny | **+2** |
| Stosunek romantyczny do Antoniny | **0** [P] |
| Stan | rozpoznaje ją |
| Jak grać | quebecki francuski, serdecznie. |

### Personel kuchni „Le Caribou Joyeux”

| Pole | Wartość |
|---|---|
| Wiek | różny [P] |
| Wzrost | różny [P] |
| Budowa ciała | różna [P] |
| IQ | przeciętne [P] |
| Rola | kuchnia „Le Caribou Joyeux” (quebecka restauracja); razem z kelnerką rozpoznali Antoninę przy napiwku 500 CHF |
| Wygląd | [P] białe fartuchy, spocone czoła |
| Wiedza | rozpoznają ją |
| Motywacje | praca |
| Sekrety | [?] — brak ustaleń |
| Stosunek platoniczny do Antoniny | **+2** |
| Stosunek romantyczny do Antoniny | **0** [P] |
| Stan | rozpoznają ją |
| Jak grać | quebecki francuski, serdecznie. |

---

## D. Lozanna — znajomi, Spotted, sąsiedztwo

### Thibault Girardet

| Pole | Wartość |
|---|---|
| Wiek | 24 |
| Wzrost | 188 cm |
| Budowa ciała | 70 kg; chudy, lekko przygarbiony |
| IQ | ok. 125 |
| Rola | sojusznik Antoniny; magisterka z mikrotechniki EPFL (VI 2013); fotograf uliczny (Canon, cz.-b., ok. 600 obs. na Instagramie); współadmin „Spotted: Lausanne”; Renens; mieszka z rodzicami (ojciec zegarmistrz); starszy brat; beagle |
| Wygląd | ciemne krótkie włosy, okrągłe okulary (nowe od czw), dwudniowy zarost, szary sweter, lekko przygarbiony; rozcięta brew (steri-stripy), siniak |
| Wiedza | zawiadomienie o napaści przeciw Karimowi; potwierdził tożsamość Loïca, usunął go z adminów Spotted, gotów zeznawać; przeszłość: jedna dziewczyna (Fribourg, 8 mies., 4 lata temu) |
| Motywacje | naprawić błędy z randki 5 I; zemścić się na Karimie i Loïcu (A12a); być lepszym od Dutoita, nie wrogiem Toni |
| Sekrety | [?] — brak ustaleń |
| Stosunek platoniczny do Antoniny | **+3** → po 15 I sojusznik (+3/+4) |
| Stosunek romantyczny do Antoniny | **+3** [P] — po randce 5 I i przeprosinach (14 I); zakochanie przetrwało zawód |
| Stan | **17 I:** zawiadomienie o napaści przeciw Karimowi; upomnienie dziekanatu; „kawa kiedyś, bez zdjęć”; tryb mściwy wobec Karima i Loïca (A12a) |
| Jak grać | **Osobowość:** nieśmiały, szczery do bólu, autoironiczny; bierze odpowiedzialność. Zraniony, ale nie zły — mściwość kieruje w Karima i Loïca, nie w Antoninę. Chce być lepszym od Dutoita, nie wrogiem Toni.<br>**Mowa:** po francusku z vaudois akcentem („septante”); niezgrabny; przeprasza za siebie zanim go ktoś oskarży.<br>**Pisanie:** dłuższe wiadomości, uprzejme, z pełnymi zdaniami; podpis rzadko; „Toni” w nagłówku; czasem 🙂.<br>**Nie robi:** nie publikuje pełnego nagrania bójki; nie wysyła zdjęć Antoniny nikomu; nie pisze pierwszy bez powodu. |

### Loïc Perroud („Rémi Fav”)

| Pole | Wartość |
|---|---|
| Wiek | 25 |
| Wzrost | ok. 178 cm [P] |
| Budowa ciała | ok. 74 kg; wyćwiczony w siłowni na pokaz [P] |
| IQ | ok. 115 [P] |
| Rola | HEIG-VD (Yverdon), były współadmin Spotted; Golf GTI; mieszka w Malley; troll internetowy („Rémi Fav”) |
| Wygląd | [P] krótkie, żelowane włosy, koszula Lacoste, zegarek na pokaz |
| Wiedza | zachował zdjęcie z Café du Port; „krowo” na Messengerze (14 I); wątek na Twitterze FR (15 I, ok. 300 RT, opis taśmy); usunięty z adminów — dla „20 minutes”: „cenzura”, „mówiłem tylko prawdę” |
| Motywacje | poczucie krzywdy; uważa, że Thibault „ugiął się przed bogatą laską” |
| Sekrety | [?] — brak ustaleń |
| Stosunek platoniczny do Antoniny | **−3** |
| Stosunek romantyczny do Antoniny | **0** [P] |
| Stan | **17 I:** urażony; możliwa eskalacja (Instagram Kévina, adres w okolicach dworca) |
| Jak grać | **Osobowość:** troll z poczuciem krzywdy. Tchórzliwy osobiście, odważny anonimowo. Drwi zamiast odpowiadać.<br>**Mowa / pisanie:** francuski internetowy, „mdr”, „ptdr”, 😂🤡; obelgi krótkie („krowo”, „chevalier blanc”); nigdy pełne zdanie przeprosin.<br>**Nie robi:** nie spotyka się twarzą w twarz. |

### Pani Favre

| Pole | Wartość |
|---|---|
| Wiek | ok. 68 [P] |
| Wzrost | ok. 160 cm [P] |
| Budowa ciała | ok. 62 kg; drobna [P] |
| IQ | ok. 105 [P] |
| Rola | konsjerżka w Grancy; sypie sól na schodach („Doktorat to doktorat”) |
| Wygląd | [P] siwy kok, fartuch w kwiaty |
| Wiedza | wie, kto przychodzi i wychodzi; pyta o „tych panów z gazety” |
| Motywacje | porządek w kamienicy |
| Sekrety | [?] — brak ustaleń |
| Stosunek platoniczny do Antoniny | **+2** |
| Stosunek romantyczny do Antoniny | **0** |
| Stan | **25 I ok. 7:07 [P]:** sypie sól na schodach przed wejściem; protestuje wobec reportera „20 minutes” (Perret) dzwoniącego do mieszkania 14<br>**25 I ok. 7:54 [P]:** w holu na parterze, wita Antoninę wychodzącą z kamienicy; wie o fotografie po drugiej stronie ulicy |
| Jak grać | po francusku, staroświecko, życzliwie wścibska; pyta o pogodę i „tych panów z gazety”. |

### Ioana Moldovan

| Pole | Wartość |
|---|---|
| Wiek | ok. 23 [P] |
| Wzrost | ok. 170 cm [P] |
| Budowa ciała | ok. 68 kg; ex-wioślarka, szeroka w barkach [P] |
| IQ | ok. 130 [P] |
| Rola | Rumunka, Erasmus, chemia, ex-wioślarka; „uczennica” Antoniny od martwego ciągu; numer od 7 I |
| Wygląd | [P] kasztanowe włosy w warkoczu, mocne dłonie |
| Wiedza | zna trening; trzyma wyniki |
| Motywacje | stać się silniejsza; mieć dobrego trenera |
| Sekrety | [?] — brak ustaleń |
| Stosunek platoniczny do Antoniny | **+2** |
| Stosunek romantyczny do Antoniny | **+1** [P] — podziw dla ciała i siły |
| Stan | — |
| Jak grać | entuzjastyczna, po angielsku z rumuńskimi wtrąceniami; SMS-y z wynikami treningowymi („90 kg ×5 bez bólu!!”). |

### Olivier

| Pole | Wartość |
|---|---|
| Wiek | 35 |
| Wzrost | ok. 183 cm [P] |
| Budowa ciała | ok. 105 kg; masywny siłacz [P] |
| IQ | ok. 115 [P] |
| Rola | inżynier spod Renens; nieformalny klub siły (wt/czw 19:00); Mistrzostwa Vaud w Yverdon 9 III (odmówione) |
| Wygląd | [P] krótka broda, ręce grube jak łopaty |
| Wiedza | technika trójboju; zaproponował zawody |
| Motywacje | pokazać Antoninie zawody; kolegialność |
| Sekrety | [?] — brak ustaleń |
| Stosunek platoniczny do Antoniny | **+2** |
| Stosunek romantyczny do Antoniny | **+1** [P] — podziw dla siły |
| Stan | odmówione (Yverdon 9 III) |
| Jak grać | rubaszny siłacz, mówi o kilogramach i technice; nie naciska. |

### Pan Rochat

| Pole | Wartość |
|---|---|
| Wiek | ok. 70 [P] |
| Wzrost | ok. 172 cm [P] |
| Budowa ciała | ok. 70 kg; chudy, z laską [P] |
| IQ | ok. 115 [P] |
| Rola | emeryt w Centre sportif, trener gimnastyki w Morges w latach 70. |
| Wygląd | [P] siwa czupryna, laska |
| Wiedza | technika gimnastyczna |
| Motywacje | dobre ćwiczenie dla młodych |
| Sekrety | [?] — brak ustaleń |
| Stosunek platoniczny do Antoniny | **+2** |
| Stosunek romantyczny do Antoniny | **0** |
| Stan | — |
| Jak grać | dobroduszny, rady techniczne („zgięte kolana”); mówi do niej „mademoiselle”. |

### Pracownik Centre sportif

| Pole | Wartość |
|---|---|
| Wiek | ok. 40 [P] |
| Wzrost | ok. 175 cm [P] |
| Budowa ciała | ok. 80 kg [P] |
| IQ | ok. 105 [P] |
| Rola | pracownik Centre sportif UNIL-EPFL; udzielił upomnienia za handstand w mokasynach |
| Wygląd | [P] w polo z logo, identyfikator |
| Wiedza | regulamin |
| Motywacje | porządek |
| Sekrety | [?] — brak ustaleń |
| Stosunek platoniczny do Antoniny | **0** |
| Stosunek romantyczny do Antoniny | **0** [P] |
| Stan | — |
| Jak grać | regulaminowy, uprzejmy. |

### Kévin Bühler

| Pole | Wartość |
|---|---|
| Wiek | 19 |
| Wzrost | ok. 178 cm [P] |
| Budowa ciała | ok. 70 kg; szczupły [P] |
| IQ | ok. 105 [P] |
| Rola | uczeń mechanik z Renens; nagranie 0:31 za 100 CHF; relacja na Instagramie „la géante m'a filé 100 balles 😂” |
| Wygląd | [P] dres Lacoste, krótkie włosy |
| Wiedza | **zna drzwi nr 20** (Grancy) |
| Motywacje | lajki, nie krzywda |
| Sekrety | [?] — brak ustaleń |
| Stosunek platoniczny do Antoniny | **0** |
| Stosunek romantyczny do Antoniny | **+2** [P] — fascynacja „la géante”; Grupa B/fetyszysta |
| Stan | łatwo go podpuścić |
| Jak grać | nastolatek z przedmieścia: argot, „wesh”, „la géante”; chce lajków, nie krzywdy — ale łatwo go podpuścić. |

### Dylan Pereira

| Pole | Wartość |
|---|---|
| Wiek | 19 |
| Wzrost | ok. 176 cm [P] |
| Budowa ciała | ok. 68 kg [P] |
| IQ | ok. 100 [P] |
| Rola | Renens; kolega Kévina; bluza FC LS |
| Wygląd | [P] bluza FC Lausanne-Sport, czapka |
| Wiedza | **zna drzwi nr 20** (Grancy) |
| Motywacje | lajki; kumpel Kévina |
| Sekrety | [?] — brak ustaleń |
| Stosunek platoniczny do Antoniny | **−1** |
| Stosunek romantyczny do Antoniny | **+1** [P] |
| Stan | łatwo go podpuścić |
| Jak grać | nastolatek z przedmieścia: argot, „wesh”, „la géante”; chce lajków, nie krzywdy. |

### Filip (@filip_erasmus_bern)

| Pole | Wartość |
|---|---|
| Wiek | ok. 20 |
| Wzrost | ok. 180 cm [P] |
| Budowa ciała | ok. 72 kg [P] |
| IQ | ok. 125 [P] |
| Rola | Polak, student prawa UW, Erasmus w Bernie; wrzucił zdjęcie z peronu, skasował, przeprosił |
| Wygląd | [P] okulary, plecak, bluza UW |
| Wiedza | wie, że zrobił błąd |
| Motywacje | pozbyć się wstydu |
| Sekrety | [?] — brak ustaleń |
| Stosunek platoniczny do Antoniny | **0** |
| Stosunek romantyczny do Antoniny | **+1** [P] |
| Stan | zawstydzony; skasował zdjęcie |
| Jak grać | zawstydzony student; po polsku, grzecznie; nie powtórzy błędu. |

### Grzegorz Pawlak

| Pole | Wartość |
|---|---|
| Wiek | 43 |
| Wzrost | ok. 176 cm [P] |
| Budowa ciała | ok. 85 kg; zwalisty, z torbą na aparaty [P] |
| IQ | ok. 115 [P] |
| Rola | z Łodzi, fotoreporter-freelancer w Genewie od 1998 (Carouge, pozwolenie C, żona Szwajcarka); „Fakt”, SE, „Blick”; zdjęcia Antoniny 15 I + cytat „to mój głos”; **akredytacja WEF Davos** — przynęta Sikorskiego (wywiad 26 I 8:00) |
| Wygląd | [P] kurtka z kieszeniami, dwa aparaty na szyi |
| Wiedza | zna Genewę i środowisko prasowe; trasę Antoniny w Szwajcarii |
| Motywacje | zdjęcie, pieniądze, sensacja; „tylko jedno zdjęcie” |
| Sekrety | [?] — brak ustaleń |
| Stosunek platoniczny do Antoniny | **−1** |
| Stosunek romantyczny do Antoniny | **0** |
| Stan | w Genewie; akredytacja WEF Davos |
| Jak grać | zawodowiec bez złośliwości: uprzejmy, nachalny, „tylko jedno zdjęcie”; po polsku, czasem po francusku; nie łamie prawa wprost. |

### Odile Vautier („Madame Vautier”)

| Pole | Wartość |
|---|---|
| Wiek | ok. 61 [P] |
| Wzrost | ok. 158 cm [P] |
| Budowa ciała | ok. 55 kg; drobna [P] |
| IQ | ok. 115 [P] |
| Rola | corsetière, właścicielka **Atelier de Corsetterie et Brafitting Vautier**, Rue de Bourg 14, 1003 Lausanne [N, `12` C93]; szyje biustonosze Antoniny na miarę: czternaście wymiarów, fiszbiny tytanowe, miseczki enkapsulowane [N]; zawsze to ona ją mierzyła [N, `12` C93] |
| Wygląd | krótkie siwe włosy, okulary na łańcuszku, centymetr na szyi [P] |
| Wiedza | zna dokładne wymiary Antoniny (UK 40G / EU 90L / FR 105L, Z80) i ich zmiany od lat; o jej życiu prywatnym wie niewiele [P] |
| Motywacje | rzemiosło i dopasowanie bez kompromisu; klientki o figurach, z którymi sklepy sobie nie radzą |
| Sekrety | [?] — brak ustaleń |
| Stosunek platoniczny do Antoniny | **+2** [P] |
| Stosunek romantyczny do Antoniny | **0** |
| Stan | brak wpisów z gry; hak [P]: adres atelier jest w zapisie C93 — po publikacji wycieku WebiX mogą się pojawić ciekawskie klientki i dziennikarze |
| Jak grać | **Osobowość:** spokojna, kliniczna, bez sentymentów; ciało klientki to konstrukcja do obsłużenia.<br>**Mowa:** po francusku, rzeczowo, słownictwem fachowym; bez komplementów i bez komentarzy o figurze.<br>**Pisanie:** krótkie potwierdzenia terminów, „Madame O. Vautier”.<br>**Języki:** francuski.<br>**Nie robi:** nie zdradza wymiarów ani nazwisk klientek nikomu, także prasie. |

### Rosa Ferreira

| Pole | Wartość |
|---|---|
| Wiek | ok. 56 [P] |
| Wzrost | ok. 155 cm [P] |
| Budowa ciała | ok. 70 kg; krępa [P] |
| IQ | ok. 105 [P] |
| Rola | krawcowa z Minho, w Lozannie od lat 80.; pracownia poprawek „Retouches Rosa” przy Avenue d'Echallens [P]; **poboczna krawcowa Antoniny** [N]: poprawki, podwijanie, poszerzanie gotowych ubrań [P]. Od ok. 2003 uczyła piętnastoletnią Antoninę szyć — stąd jej krawiectwo (`06` §4.3) [P]. Skomplikowane rzeczy odsyła do Maison Velikov [P] |
| Wygląd | ciemne włosy z siwizną w koku, okulary na czubku nosa, poduszka na szpilki na nadgarstku [P] |
| Wiedza | zna jej ubrania, rozmiary i kłopoty z gotowymi rzeczami; o życiu prywatnym wie tyle, ile Antonina powie przy maszynie [P] |
| Motywacje | pracownia, wnuki w Portugalii, emerytura w Minho |
| Sekrety | [?] — brak ustaleń |
| Stosunek platoniczny do Antoniny | **+3** [P] — „menina” od piętnastu lat |
| Stosunek romantyczny do Antoniny | **0** |
| Stan | brak wpisów z gry |
| Jak grać | **Osobowość:** ciepła, gadatliwa, praktyczna; plotkuje o sąsiadach, nigdy o klientkach.<br>**Mowa:** po francusku z portugalskim akcentem; z Antoniną po portugalsku; „menina”, „ai, Jesus”.<br>**Pisanie:** SMS-y bez znaków diakrytycznych, krótkie, z wykrzyknikami.<br>**Języki:** portugalski, francuski.<br>**Nie robi:** nie szyje sukni wieczorowych ani marynarek („to nie dla mnie, menina”). |

### Martine Pittet

| Pole | Wartość |
|---|---|
| Wiek | ok. 58 [P] |
| Wzrost | ok. 165 cm [P] |
| Budowa ciała | ok. 68 kg; silne dłonie [P] |
| IQ | ok. 110 [P] |
| Rola | **rodzinna szewcowa Jelskich** w Lozannie [N]: Cordonnerie Pittet przy Rue de la Madeleine, drugie pokolenie po ojcu René [P]. Obsługuje rodzinę od przeprowadzki do Savigny w 1993 [P]; szyje Antoninie buty na miarę (44 EU) i naprawia resztę [P]; „rachunek od szewcowej” z wycieku z 2009 (Clémence) to jej rachunek [P] |
| Wygląd | fartuch skórzany, krótkie włosy, okulary do pracy, zapach kleju i pasty [P] |
| Wiedza | zna rozmiary stóp całej rodziny i to, kto ile chodzi; o sprawach rodziny nie wie nic ponad plotki z gazet [P] |
| Motywacje | warsztat po ojcu, solidna robota, stali klienci |
| Sekrety | [?] — brak ustaleń |
| Stosunek platoniczny do Antoniny | **+2** [P] |
| Stosunek romantyczny do Antoniny | **0** |
| Stan | brak wpisów z gry |
| Jak grać | **Osobowość:** konkretna, mało sentymentalna, dumna z rzemiosła.<br>**Mowa:** po francusku z akcentem vaudois („septante”, „huitante”); krótko, praktycznie.<br>**Pisanie:** rachunki odręczne; telefon stacjonarny w warsztacie.<br>**Języki:** francuski.<br>**Nie robi:** nie toleruje targowania; nie szyje „na wczoraj”. |

### Petar Velikov (Maison Velikov)

| Pole | Wartość |
|---|---|
| Wiek | ok. 64 [P] |
| Wzrost | ok. 172 cm [P] |
| Budowa ciała | ok. 80 kg; krępy [P] |
| IQ | ok. 125 [P] |
| Rola | głowa **Maison Velikov** — wielopokoleniowej rodzinnej pracowni krawieckiej z Sofii [N] (założonej pod koniec XIX w., Petar to czwarte pokolenie [P]). Po 1989 **Havard Holding wszedł jako partner biznesowy** i rozwinął dom do pracowni na **Savile Row** i w **Genewie** [N]; Sofia zostaje rodzinną pracownią [P]. Petar prowadzi Genewę [P]. Szyje dla Jelskich i Havarda: garnitury Krzysztofa i Havarda, marynarki i suknie Antoniny [P]. Córka **Elena Velikova** (ok. 32) jest krojczynią damską w Genewie i prowadzi Antoninę [P]. Czerwona suknia z balu z 2009 to ich robota — prasa błędnie wskazała paryskie atelier (`15`) [P] |
| Wygląd | srebrne włosy, kamizelka, centymetr na szyi, kreda w kieszeni [P] |
| Wiedza | wymiary rodziny Jelskich; wie, że Havard Holding jest współwłaścicielem domu [N] — publicznie Maison Velikov to firma rodzinna [P] |
| Motywacje | ciągłość dynastii; prestiż Savile Row bez utraty sofijskiej tradycji |
| Sekrety | udział Havard Holding w firmie nie jest publiczny [P] |
| Stosunek platoniczny do Antoniny | **+2** [P] |
| Stosunek romantyczny do Antoniny | **0** |
| Stan | brak wpisów z gry |
| Jak grać | **Osobowość:** ceremonialny, cierpliwy, perfekcjonista; cytuje dziadka; przymiarka to rytuał.<br>**Mowa:** z Antoniną po francusku, z rodziną po bułgarsku; uprzejmie, z dystansem starej szkoły.<br>**Pisanie:** listy na papierze firmowym, podpis cyrylicą.<br>**Języki:** bułgarski, francuski, angielski; Antonina bułgarskiego nie zna, ale rozumie sporo przez serbsko-chorwacki i rosyjski.<br>**Nie robi:** nie szyje z syntetyków; nie skraca przymiarek; nie mówi o klientach. |

---

## E. Nauka i praca (EPFL, Thales, AMANTIS)

### prof. Jean-Luc Vasseur

| Pole | Wartość |
|---|---|
| Wiek | 55 |
| Wzrost | 178 cm |
| Budowa ciała | ok. 70 kg; szczupły [P] |
| IQ | 140 |
| Rola | promotor Antoniny; katedra fizyki powierzchni (MX) |
| Wygląd | szczupły, siwy, zielony kardigan, okulary |
| Wiedza | wie o wyjeździe na tydzień (bez miejsca), urlop 21–24 I; przekazał podejście armasuisse (Aebischer); cel: **harmonogram i tekst do 31 I**, jury (Ossikovski, ktoś z Manchesteru), egzamin realnie III–IV; APL do 15 II; dydaktyka zostaje; neutralny wobec Camille (jej teczka w Commission Égalité); w „Le Temps”: „Une chercheuse exceptionnelle. Le reste ne nous regarde pas.” |
| Motywacje | gasi presję Thalesa i DGA; chroni studentkę przez procedurę |
| Sekrety | boi się, że Tosia „zrobi wszystko sama” i że szybka obrona będzie wyglądać „po znajomości” |
| Stosunek platoniczny do Antoniny | **+3** |
| Stosunek romantyczny do Antoniny | **0** [P] |
| Stan | **27 I 19:00–20:12 (sesja 19 wpisy 453–471):** gościł Antoninę i Miko w Pully (kolacja z Hélène); dostał 1 wydruk całości z aneksami A–G (F–G wyblakłe) — aneksy pn rano do sejfu wydziału, część jawną czyta do śr; pendrive tylko z PDF wersji jawnej, do ręki (pn 7:00–18:30 poza 12–14) lub u Sophie w zaklejonej kopercie, **nie mailem** (polecenie DGA od 11 I); w śr nieformalnie pyta Ossikovskiego i Manchester o jury; armasuisse — list intencyjny przez wydział za 2–3 tyg., nie podpisywać niczego przysłanego bezpośrednio; nie chce być osobą zaufania przed Komisją (promotor też Camille); wskazał literówkę „continous”; uścisk Antoniny na pożegnanie go speszył.<br>**18 I:** „elle rappellera” (Aebischer); przeczyta pracę w weekend 26–27 I; egzamin 25 I — o opóźnieniu wiedzieć przed 8:00<br>**25 I ok. 8:37 [P]:** stoi przed salą CO1; Antonina spóźniona ok. 22 min, nie uprzedziła go przed 8:00<br>**25 I 11:15 [P]:** czeka w hallu CO po egzaminie; w protokole zapisał spóźnienie jako zator na Av. de Provence |
| Jak grać | **Osobowość:** rzeczowy, uprzejmy, lojalny wobec studentki, ale instytucjonalny do szpiku — chroni ją przez procedurę, nie przez gesty. Nie lubi dramatów; lubi plany na piśmie.<br>**Mowa:** po francusku, spokojnie, „Toni”; zdania warunkowe („si tu veux…”); cytuje regulamin; mądre zdania o ludziach mówi mimochodem („wybaczyłbym głupotę, nie kłamstwo na pytanie”).<br>**Pisanie:** krótkie maile z podpisem **„JLV”**, bez formułek; czasem pytanie w temacie.<br>**Nie robi:** nie prosi o współautorstwo; nie komentuje życia prywatnego publicznie. |

### Hélène Vasseur

| Pole | Wartość |
|---|---|
| Wiek | ok. 55 [P] |
| Wzrost | ok. 160 cm [P] |
| Budowa ciała | drobna [P] |
| IQ | ok. 125 [P] |
| Rola | żona prof. Vasseura; dom w Pully, ch. de la Rosiaz 14 [P] |
| Wygląd | [P] siwe włosy spięte spinką, fartuch w kratę |
| Wiedza | widziała Antoninę w RTS (tydzień 21–27 I); zna ją z opowieści męża („trenuje”, „je za trzech”) |
| Motywacje | gościnność; pilnuje, żeby mąż nie pracował przy stole |
| Sekrety | [?] — brak ustaleń |
| Stosunek platoniczny do Antoniny | **+2** [P] |
| Stosunek romantyczny do Antoniny | **0** [P] |
| Stan | **27 I 19:00–20:12 (sesja 19 wpisy 454–471):** kolacja (zupa porowa, gratin dauphinois, bezy z double crème de la Gruyère); „vous êtes encore plus grande qu'à la télé”; zapytała „po ludzku”, jak Antonina się trzyma; dała resztki gratin na drogę Antoninie i Miko. |
| Jak grać | ciepła, bezpośrednia, z humorem; po francusku, do Antoniny per „vous”; karmi bez pytania; przy mężu-pedancie robi za hamulec („Jean-Luc, przy zupie o pendrive'ach?”). |

### Marc [nazwisko ?]

| Pole | Wartość |
|---|---|
| Wiek | ok. 28 [P] |
| Wzrost | ok. 180 cm [P] |
| Budowa ciała | szczupły [P] |
| IQ | ok. 125 [P] |
| Rola | asystent / doktorant z katedry Vasseura (MX); nadzoruje egzaminy i ćwiczenia |
| Wygląd | [P] jasne, krótkie włosy, okulary w cienkiej oprawie, sweter w serek |
| Wiedza | zna Antoninę z katedry; nie zna szczegółów jej wyjazdu |
| Motywacje | rzetelność, unikanie konfliktu |
| Sekrety | [?] — brak ustaleń |
| Stosunek platoniczny do Antoniny | **+1** [P] |
| Stosunek romantyczny do Antoniny | **0** [P] |
| Stan | **25 I 8:39 [P]:** przekazuje Antoninie nadzór CO1; 74 z 78 obecnych |
| Jak grać | po francusku, cicho, rzeczowo; mówi szeptem na sali, krótkie zdania, bez komentarzy o życiu prywatnym. |

### dr Hélène Marchand

| Pole | Wartość |
|---|---|
| Wiek | 45 |
| Wzrost | 168 cm |
| Budowa ciała | ok. 60 kg; zadbana, szczupła [P] |
| IQ | 135 |
| Rola | współpromotorka (Thales R&T, Palaiseau); reprezentuje interes Thalesa; uczciwie uprzedziła o DGA |
| Wygląd | [P] krótko ścięte ciemne włosy z siwizną, żakiet, okulary w cienkich oprawkach |
| Wiedza | zna AMANTIS i Thales; uprzedziła o DGA |
| Motywacje | wciągnąć Antoninę do Palaiseau od II; uczciwy interes Thalesa |
| Sekrety | [?] — brak ustaleń |
| Stosunek platoniczny do Antoniny | **+3** |
| Stosunek romantyczny do Antoniny | **0** [P] |
| Stan | **27 I 21:36 (sesja 19 wpis 479):** mail „AMANTIS mardi — logistique”: propozycja DGA — start z Blécherette wt 29 I 7:00, powrót śr po LabRAM; Lefèvre potwierdza eskortę i konwojenta próbek do pn 9:00; prosi o telefon pn przed 8:30.<br>**18 I:** proponuje Palaiseau od II („z góry”, czek in blanco); termin dziś na listę próbek i abstrakt (gotowe na papierze); 29 I grupa sterująca AMANTIS |
| Jak grać | ciepła, precyzyjna; po francusku, z uprzejmością paryskiej menedżerki; telefon zamiast maila w sprawach drażliwych; pisze maile z pełną formułą („Bien à vous, Hélène”). Nie zdradza szczegółów bezpieczeństwa przez telefon. |

### Sylvie Bertin

| Pole | Wartość |
|---|---|
| Wiek | ok. 55 |
| Wzrost | ok. 165 cm [P] |
| Budowa ciała | ok. 65 kg; zaokrąglona, matczyna [P] |
| IQ | ok. 125 [P] |
| Rola | Thales, Direction Sûreté; habilitacja (formularz wysłany 15 I), procedura próbek (plomba pn 28 I 7:00), **lista nośników danych — termin dziś (pt 18 I)**, gotowa na papierze; TEOREM ok. 28 I |
| Wygląd | [P] krótkie siwe włosy, zielony żakiet, okulary na łańcuszku |
| Wiedza | procedury bezpieczeństwa Thalesa; Antonina jest „aktywem” firmy |
| Motywacje | czysta procedura; zjedz coś |
| Sekrety | [?] — brak ustaleń |
| Stosunek platoniczny do Antoniny | **+1** |
| Stosunek romantyczny do Antoniny | **0** [P] |
| Stan | **18 I:** lista nośników gotowa; chce rozmowy telefonicznie (21 I) — przez Marchand (mail 19 I); ⚠️ urlop |
| Jak grać | biurokratka bezpieczeństwa z ludzką twarzą; procedury wylicza punktami, potem nagle matczyne „proszę coś zjeść”; maile formalne z numeracją; prywatny mail tylko w nagłych sprawach. |

### pan / ingénieur général Lefèvre

| Pole | Wartość |
|---|---|
| Wiek | ok. 50 |
| Wzrost | ok. 180 cm [P] |
| Budowa ciała | ok. 80 kg; wyprostowany, wojskowa sylwetka [P] |
| IQ | 135 |
| Rola | DGA (Direction de la stratégie); przedstawiciel DGA w grupie sterującej AMANTIS; ma ocenić, czy Tosia jest „bezpieczna operacyjnie”; rozmawiał z nią przez RIMBAUD 11 I |
| Wygląd | [P] szpakowate włosy, ciemny garnitur, spięte spojrzenie |
| Wiedza | zna profil Antoniny z DGA; spotkanie 29 I |
| Motywacje | państwo, ciągłość programu |
| Sekrety | [?] — brak ustaleń |
| Stosunek platoniczny do Antoniny | **0** |
| Stosunek romantyczny do Antoniny | **0** [P] |
| Stan | spotkanie 29 I (Palaiseau) |
| Jak grać | chłodny technokrata państwa; pytania otwarte („jak pani widzi następne miesiące?”), żadnych obietnic; mówi „nous” w imieniu państwa. |

### Léo Garnier

| Pole | Wartość |
|---|---|
| Wiek | 32 |
| Wzrost | 178 cm |
| Budowa ciała | ok. 72 kg; chudy [P] |
| IQ | 130 |
| Rola | postdok w grupie; naprawił obieg Ramana; ma przejąć TP (pyta Antonina); **tylko kolega z pracy** [N] |
| Wygląd | [P] jasnobrązowe włosy, krótka broda, okulary, kardigan |
| Wiedza | technika Ramana; przejęcie TP |
| Motywacje | spokój w laboratorium |
| Sekrety | [?] — brak ustaleń |
| Stosunek platoniczny do Antoniny | **+2** |
| Stosunek romantyczny do Antoniny | **0** [N — tylko kolega z pracy] |
| Stan | — |
| Jak grać | paryski akcent, kompetentny, rozsądny; ucina konflikty („on arrête là”); nie chce być świadkiem dla żadnej strony; przynosi croissanty; maile techniczne i suche. |

### Camille Aubry

| Pole | Wartość |
|---|---|
| Wiek | 27 |
| Wzrost | ok. 170 cm [P] |
| Budowa ciała | ok. 58 kg; chuda [P] |
| IQ | ok. 125 [P] |
| Rola | doktorantka w grupie Vasseura; antagonistka; konto GASPAR przejęte przez phishing (8 I); straciła 40% mapy przy awarii Ramana |
| Wygląd | [P] jasne włosy w koku, czerwona szminka, okulary, formalna bluzka |
| Wiedza | rozpowiada „Jelska: Arabów deportować”; **zgłoszenie do Commission Égalité (16 I 12:30), CE-2013-0142**; uzupełnienie 17 I 8:21 (wypowiedzi o narodowości) — sama, nie na zlecenie Mossadu |
| Motywacje | ambitna, zazdrosna („20/20, córka premiera”), przekonana o własnej racji moralnej; czuje się kozłem ofiarnym phishingu |
| Sekrety | gada za dużo przy obcych (np. przy Zhou) |
| Stosunek platoniczny do Antoniny | **−2** → −3 |
| Stosunek romantyczny do Antoniny | **0** [P] |
| Stan | **18 I:** 17 I uzupełnienie do Commission Égalité (8:21, sama); Antonina wzruszyła na nią ramionami i zadzwoniła po polsku; Sophie odmówiła jej podpisu; **poszła z Zhou na lunch po seminarium** (A6 — mówi więcej, niż powinna) |
| Jak grać | **Osobowość:** ambitna, zazdrosna, przekonana o własnej racji moralnej. Nie jest złą osobą — jest małostkowa i urażona, a to wystarcza. Gada za dużo przy obcych.<br>**Mowa:** po francusku, szybko, z wyrzutem; wylicza na palcach; „Toni” z akcentem ironii; lubi publiczność.<br>**Pisanie:** maile formalne, z „cordialement”; SMS-y wielkimi literami przy emocjach („QUOI?!”, „DEMAIN”).<br>**Nie robi:** nie posuwa się do kłamstwa wprost — przekręca kontekst. |

### Sophie Lambert

| Pole | Wartość |
|---|---|
| Wiek | 26 |
| Wzrost | ok. 165 cm [P] |
| Budowa ciała | ok. 58 kg [P] |
| IQ | ok. 125 [P] |
| Rola | doktorantka z biura grupy w MX; zaprosiła na Apéro; odmówiła Camille „potwierdzania” |
| Wygląd | [P] kręcone brązowe włosy, rumieniec, swetry |
| Wiedza | lojalna; 17 I przyniosła „Le Temps”; kuskus z Antoniną |
| Motywacje | spokój, bycie lubianą, wdzięczność wobec Antoniny |
| Sekrety | [?] — brak ustaleń |
| Stosunek platoniczny do Antoniny | **+2** |
| Stosunek romantyczny do Antoniny | **+1** [P] — zawstydzona sympatia |
| Stan | **21 I (sesja 16, do 20:23 lok.):** 19:58 CET: przypomniała o wpisie urlopu 21–24 I w IS-Academia (wpis zapisany 10:07 lok.)<br>**17 I:** odmówiła Camille podpisu |
| Jak grać | nieśmiała, lojalna; herbata zamiast słów; rumieni się; pisze ❤️ i jedno zdanie; nie chce się mieszać. |

### Ana

| Pole | Wartość |
|---|---|
| Wiek | ok. 27 [P] |
| Wzrost | ok. 165 cm [P] |
| Budowa ciała | ok. 58 kg [P] |
| IQ | ok. 125 [P] |
| Rola | doktorantka z grupy Vasseura; świadek kłótni z Camille |
| Wygląd | [P] ciemne włosy do ramion, okulary |
| Wiedza | świadek kłótni z Camille |
| Motywacje | dystans |
| Sekrety | [?] — brak ustaleń |
| Stosunek platoniczny do Antoniny | **0** |
| Stosunek romantyczny do Antoniny | **0** [P] |
| Stan | — |
| Jak grać | dystans; mówi mało. |

### Thomas

| Pole | Wartość |
|---|---|
| Wiek | ok. 27 [P] |
| Wzrost | ok. 178 cm [P] |
| Budowa ciała | ok. 75 kg [P] |
| IQ | ok. 120 [P] |
| Rola | doktorant z kuchni MX (plotka „Arabów deportować”) |
| Wygląd | [P] jasna broda, bluza z kapturem |
| Wiedza | powtarza plotkę z drugiej ręki |
| Motywacje | bycie „w obiegu” |
| Sekrety | [?] — brak ustaleń |
| Stosunek platoniczny do Antoniny | **−1** |
| Stosunek romantyczny do Antoniny | **0** [P] |
| Stan | — |
| Jak grać | plotkarz z drugiej ręki. |

### Théo

| Pole | Wartość |
|---|---|
| Wiek | 22 |
| Wzrost | ok. 178 cm [P] |
| Budowa ciała | ok. 68 kg [P] |
| IQ | ok. 120 [P] |
| Rola | student M1; pokazał film trzem osobom, przeprosił |
| Wygląd | [P] chudy, czapka z daszkiem |
| Wiedza | wie, że zrobił błąd |
| Motywacje | naprawić błąd, uniknąć kłopotów |
| Sekrety | [?] — brak ustaleń |
| Stosunek platoniczny do Antoniny | **+1** |
| Stosunek romantyczny do Antoniny | **+1** [P] — zawstydzone zauroczenie |
| Stan | przeprosił |
| Jak grać | zawstydzony, gorliwy. |

### B. Rochat

| Pole | Wartość |
|---|---|
| Wiek | 50 |
| Wzrost | ok. 175 cm [P] |
| Budowa ciała | ok. 80 kg [P] |
| IQ | ok. 105 [P] |
| Rola | technik EPFL (Service technique) |
| Wygląd | [P] kombinezon roboczy, zegarek na łańcuszku |
| Wiedza | rejestruje obecność; zna przepisy |
| Motywacje | porządek |
| Sekrety | [?] — brak ustaleń |
| Stosunek platoniczny do Antoniny | **0** |
| Stosunek romantyczny do Antoniny | **0** |
| Stan | — |
| Jak grać | rejestruje obecność, mówi o przepisach. |

### Mme Dubuis

| Pole | Wartość |
|---|---|
| Wiek | 58 |
| Wzrost | ok. 163 cm [P] |
| Budowa ciała | ok. 65 kg [P] |
| IQ | ok. 110 [P] |
| Rola | administracja grupy; zamówienia (Suprasil) |
| Wygląd | [P] krótkie siwe włosy, żółte karteczki |
| Wiedza | zamówienia, terminy |
| Motywacje | porządek w papierach |
| Sekrety | [?] — brak ustaleń |
| Stosunek platoniczny do Antoniny | **0** |
| Stosunek romantyczny do Antoniny | **0** |
| Stan | — |
| Jak grać | karteczki na biurku, uprzejma i stanowcza. |

### Stéphane Delacroix

| Pole | Wartość |
|---|---|
| Wiek | ok. 40 [P] |
| Wzrost | ok. 180 cm [P] |
| Budowa ciała | ok. 80 kg [P] |
| IQ | ok. 120 [P] |
| Rola | serwisant Horiby (Raman, 8 I) |
| Wygląd | [P] kombinezon Horiba, torba z narzędziami |
| Wiedza | rura Ramana, czas życia 200–800 h |
| Motywacje | dobra robota |
| Sekrety | [?] — brak ustaleń |
| Stosunek platoniczny do Antoniny | **+1** |
| Stosunek romantyczny do Antoniny | **0** [P] |
| Stan | — |
| Jak grać | techniczny, cierpliwy, liczy godziny rury. |

### prof. Razvigor Ossikovski

| Pole | Wartość |
|---|---|
| Wiek | ok. 60 [P] |
| Wzrost | ok. 175 cm [P] |
| Budowa ciała | ok. 80 kg [P] |
| IQ | ok. 145 [P] |
| Rola | LPICM (l'X); Bułgar we Francji; nauczyciel Antoniny z l'X; LabRAM 30 I 8:00–11:00; kandydat do jury |
| Wygląd | [P] siwa broda, kamizelka, okulary |
| Wiedza | spektroskopia Ramana, Antonina z l'X |
| Motywacje | nauka; uczniowie |
| Sekrety | [?] — brak ustaleń |
| Stosunek platoniczny do Antoniny | **+3** |
| Stosunek romantyczny do Antoniny | **0** [P] |
| Stan | LabRAM 30 I 8:00–11:00 |
| Jak grać | ciepły profesor starej szkoły; mówi o widmach jak o muzyce. |

### dr Arnaud Mercier

| Pole | Wartość |
|---|---|
| Wiek | 34 |
| Wzrost | ok. 180 cm [P] |
| Budowa ciała | ok. 75 kg [P] |
| IQ | ok. 125 [P] |
| Rola | LMSC (Fontcuberta); czwarty postdok, zgorzkniały; Renishaw tylko pod nadzorem, „pliki zostają”; w II anonimowa skarga do biura integralności (A5) |
| Wygląd | [P] zaczesane włosy, koszula w paski, spojrzenie z góry |
| Wiedza | Renishaw |
| Motywacje | zazdrość, protekcjonalność wobec młodszych |
| Sekrety | zazdrość; w II skarga (A5) |
| Stosunek platoniczny do Antoniny | **−2** |
| Stosunek romantyczny do Antoniny | **0** [P] |
| Stan | — |
| Jak grać | protekcjonalny, seksistowski („la fille du premier ministre”). |

### Recenzent nr 2 (APL)

| Pole | Wartość |
|---|---|
| Wiek | ? |
| Wzrost | ? |
| Budowa ciała | ? |
| IQ | ok. 135 [P] |
| Rola | anonimowy recenzent Applied Physics Letters; uczciwa obiekcja: kontrola na kwarcu; termin rewizji 15 II |
| Wygląd | brak (anonimowy) |
| Wiedza | pole fizyki powierzchni |
| Motywacje | rzetelność |
| Sekrety | tożsamość |
| Stosunek platoniczny do Antoniny | **0** |
| Stosunek romantyczny do Antoniny | **0** |
| Stan | czeka na rewizję 15 II |
| Jak grać | anonimowy, merytoryczny. |

### Anne-Laure Python

| Pole | Wartość |
|---|---|
| Wiek | ok. 38 [P] |
| Wzrost | ok. 168 cm [P] |
| Budowa ciała | ok. 60 kg [P] |
| IQ | ok. 125 [P] |
| Rola | Mediacom EPFL (chargée de communication); centralizuje zapytania mediów |
| Wygląd | [P] elegancki bob, żakiet, telefon w ręku |
| Wiedza | wie, jak działają media |
| Motywacje | ochrona wizerunku uczelni |
| Sekrety | [?] — brak ustaleń |
| Stosunek platoniczny do Antoniny | **+2** |
| Stosunek romantyczny do Antoniny | **0** [P] |
| Stan | dwie wersje oświadczeń do wyboru |
| Jak grać | rzeczowa, życzliwa; mówi językiem komunikatów („l'EPFL ne commente pas…”); odradza listy i szczegóły. |

### Inès Berrada

| Pole | Wartość |
|---|---|
| Wiek | ok. 27 [P] |
| Wzrost | ok. 168 cm [P] |
| Budowa ciała | ok. 60 kg [P] |
| IQ | ok. 130 [P] |
| Rola | doktorantka chemii (CH), ojciec z Fezu; zgłosiła Karima; wycofała wsparcie dla Antoniny po wersji Camille |
| Wygląd | [P] ciemne włosy, ciemne oczy, spokojna twarz |
| Wiedza | wersja Camille |
| Motywacje | uczciwość, duma |
| Sekrety | [?] — brak ustaleń |
| Stosunek platoniczny do Antoniny | **0** |
| Stosunek romantyczny do Antoniny | **0** [P] |
| Stan | możliwa kawa „bez cywilizacji” |
| Jak grać | dumna, uczciwa; „kawa, bez cywilizacji” możliwa; pisze krótko i chłodno, ale nie zamyka drzwi. |

### Matthieu Rapin

| Pole | Wartość |
|---|---|
| Wiek | ok. 26 [P] |
| Wzrost | ok. 180 cm [P] |
| Budowa ciała | ok. 75 kg [P] |
| IQ | ok. 130 [P] |
| Rola | doktorant matematyki, rudy; nagrał bójkę (0:58) |
| Wygląd | rudy |
| Wiedza | nagranie bójki |
| Motywacje | ostrożność |
| Sekrety | [?] — brak ustaleń |
| Stosunek platoniczny do Antoniny | **0** |
| Stosunek romantyczny do Antoniny | **0** |
| Stan | oddał nagranie władzom |
| Jak grać | ostrożny, oddał nagranie władzom. |

### prof. Hess

| Pole | Wartość |
|---|---|
| Wiek | ok. 60 [P] |
| Wzrost | ok. 178 cm [P] |
| Budowa ciała | ok. 80 kg [P] |
| IQ | ok. 145 [P] |
| Rola | matematyka; rozdzielił bójkę |
| Wygląd | sweter z łatami |
| Wiedza | rozdzielił bójkę Karim–Thibault |
| Motywacje | porządek |
| Sekrety | [?] — brak ustaleń |
| Stosunek platoniczny do Antoniny | **0** |
| Stosunek romantyczny do Antoniny | **0** |
| Stan | — |
| Jak grać | sucha władczość profesora. |

### Julien Morel

| Pole | Wartość |
|---|---|
| Wiek | ok. 26 [P] |
| Wzrost | ok. 180 cm [P] |
| Budowa ciała | ok. 80 kg [P] |
| IQ | ok. 120 [P] |
| Rola | doktorant z Fryburga, grupa WhatsApp; oznaczał Antoninę na Mèmes |
| Wygląd | [P] okulary, bluza z memem |
| Wiedza | grupa WhatsApp |
| Motywacje | prowokacje, memy |
| Sekrety | [?] — brak ustaleń |
| Stosunek platoniczny do Antoniny | **−2** |
| Stosunek romantyczny do Antoniny | **0** [P] |
| Stan | — |
| Jak grać | prowokator z tylnego rzędu, emotikony, nigdy nie podpisuje się pod niczym poważnym. |

### Zhou Yifan

| Pole | Wartość |
|---|---|
| Wiek | 28 |
| Wzrost | ok. 175 cm [P] |
| Budowa ciała | ok. 65 kg [P] |
| IQ | ok. 135 [P] |
| Rola | doktorant wizytujący IMX (Tsinghua); seminarium 17 I 12:15 („ultrasound-assisted annealing”) — zacytował wystąpienie Antoniny z 2012, pytał, kto w grupie robi Ramana, potem lunch z Camille; **źródło MSS pod presją (rodzina w Hefei) — instrukcja: „miły”, bez propozycji** |
| Wygląd | [P] okulary, ciemna kurtka, nieśmiały uśmiech |
| Wiedza | wystąpienie Antoniny z 2012; kto w grupie robi Ramana |
| Motywacje | wykonanie zadania MSS bez konfliktu; rodzina w Hefei |
| Sekrety | źródło MSS pod presją |
| Stosunek platoniczny do Antoniny | **0** |
| Stosunek romantyczny do Antoniny | **+1** [P] — onieśmielony autentyczną ciekawością naukową |
| Stan | po lunchu z Camille |
| Jak grać | sympatyczny, autentycznie ciekawy grafenu; angielski z chińskim akcentem; komplementy naukowe; nigdy nie pyta o nic wprost — zbiera przez innych (Camille). |

---

## F. Władze szwajcarskie

### Anne Keller

| Pole | Wartość |
|---|---|
| Wiek | po trzydziestce (ok. 34 [P]) |
| Wzrost | ok. 170 cm [P] |
| Budowa ciała | ok. 60 kg; szczupła [P] |
| IQ | ok. 135 [P] |
| Rola | analityczka SRC/NDB (Service de renseignement de la Confédération, Berno); prowadzi stronę „wywiadowczą” sprawy Jelskiej |
| Wygląd | akcent fryburski; ciemny kok, okulary |
| Wiedza | przesłuchanie 16 I; implant w SRC; ochrona Konfederacji (117, hasło **BERGAMOTE**); 17 I: para pod Rolexem na kamerach, skargi z art. 180 Antonina nie składa (art. 271 i tak z urzędu); zdjęcia pary i auta od Francuzów (13:20); Camille bez związku z parą (blef); kobieta wymeldowana 11:40; oryginały zdjęć implantu przez Ammanna (FP-0417-02); **numer Iridium Antoniny zapisany „tylko dla siebie”**; potrzebuje zgody „doradców” na obejrzenie telefonu — **strona polska zgłosi się sama przez attaché w Bernie** (Keller jeszcze nie wie); 18 I 8:30–8:58 Blécherette: okazanie (Zbinden) — Antonina rozpoznała „L.” (A-5) i kobietę (B-3); protokół polskiego attaché (7:52) — wie, że S4 jest od WP i że Antonina wiedziała o przekazaniu |
| Motywacje | bezpieczeństwo Konfederacji; wyjaśnić sprawę; zaczyna szanować Antoninę jako osobę |
| Sekrety | [?] — brak ustaleń |
| Stosunek platoniczny do Antoniny | **+1** (ostrożny szacunek) |
| Stosunek romantyczny do Antoniny | **0** [P] |
| Stan | **19 I:** 17:48 mail „Trois questions”; 21:28 CET potwierdza **nadzór Grancy przez policję kantonalną** na prośbę Antoniny; powrót 25 I; „dobranoc — albo dzień dobry” (wnioskuje o strefie czasowej).<br>**18 I:** wyjazd 18–24 I „za granicą, pod ochroną”; **może dzwonić na Iridium** (wieczorami); przełoży technika prewencji |
| Jak grać | **Osobowość:** chłodna, uprzejma, bardzo szybka; myśli głośno w hipotezach („dwie możliwości”); szanuje suwerenność bardziej niż ludzi, ale Antoninę zaczyna szanować jako osobę. Lubi precyzję i doceniła notatkę.<br>**Mowa:** francuski fryburski; **pytania numerowane** („trzy pytania, po kolei”); zdania krótkie; kończy „Bonne journée, madame”.<br>**Pisanie:** SMS-y bez emotikon, pełne zdania, podpis „A. Keller”; maile służbowe z sygnaturą SRC.<br>**Nie robi:** nie mówi nazw obcych służb przez telefon; nie obiecuje, czego nie może; nie zdradza źródeł. |

### insp. Markus Baumann

| Pole | Wartość |
|---|---|
| Wiek | ok. 45 |
| Wzrost | ok. 183 cm [P] |
| Budowa ciała | ok. 88 kg; masywny, spokojny [P] |
| IQ | ok. 120 [P] |
| Rola | fedpol, Police judiciaire fédérale (Berno); przesłuchanie 16 I |
| Wygląd | [P] krótkie włosy, bury garnitur, wąsy |
| Wiedza | protokół przesłuchania; sprawa implantu |
| Motywacje | rzetelny protokół |
| Sekrety | [?] — brak ustaleń |
| Stosunek platoniczny do Antoniny | **+1** |
| Stosunek romantyczny do Antoniny | **0** |
| Stan | — |
| Jak grać | berneński akcent, wolny, metodyczny; protokół zdanie po zdaniu; „uważaj na siebie” na koniec. |

### Daniel Ammann

| Pole | Wartość |
|---|---|
| Wiek | ok. 40+ [P] |
| Wzrost | ok. 180 cm [P] |
| Budowa ciała | ok. 82 kg [P] |
| IQ | ok. 125 [P] |
| Rola | technik kryminalistyczny fedpolu [P]; ruda broda; walizka Peli; zdjęcia implantu (FP-0417-02) |
| Wygląd | ruda broda, walizka Peli |
| Wiedza | implant w gniazdku |
| Motywacje | czysta robota |
| Sekrety | [?] — brak ustaleń |
| Stosunek platoniczny do Antoniny | **+2** |
| Stosunek romantyczny do Antoniny | **0** |
| Stan | — |
| Jak grać | niemieckojęzyczny Szwajcar, mówi mało; „Sauber gemacht”; doceni dobrą herbatę. |

### P. Mottier

| Pole | Wartość |
|---|---|
| Wiek | ok. 55 [P] |
| Wzrost | ok. 178 cm [P] |
| Budowa ciała | ok. 85 kg [P] |
| IQ | ok. 115 [P] |
| Rola | Sécurité et prévention EPFL; przyszedł na prośbę Keller 17 I, zabrał notatkę, zostawił wizytówkę; **19 I dostał od Antoniny 4 groźby (Fwd)** |
| Wygląd | [P] były policjant, siwiejące wąsy, kajet |
| Wiedza | groźby w skrzynce EPFL |
| Motywacje | bezpieczeństwo kampusu |
| Sekrety | [?] — brak ustaleń |
| Stosunek platoniczny do Antoniny | **+1** |
| Stosunek romantyczny do Antoniny | **0** |
| Stan | **19 I:** dostał 4 groźby (Fwd) |
| Jak grać | były policjant, rzeczowy, notuje w kajecie; nie zadaje pytań poza swoim zakresem. |

### Lukas Zbinden

| Pole | Wartość |
|---|---|
| Wiek | ok. 50+ [P] |
| Wzrost | ok. 178 cm [P] |
| Budowa ciała | ok. 78 kg [P] |
| IQ | ok. 120 [P] |
| Rola | Kantonspolizei Zürich, specjalista od identyfikacji wizualnej; okazanie 18 I |
| Wygląd | łysiejący, okulary na łańcuszku, szary sweter, audi kombi (ZH) |
| Wiedza | procedura okazania |
| Motywacje | czysta procedura |
| Sekrety | [?] — brak ustaleń |
| Stosunek platoniczny do Antoniny | **+1** |
| Stosunek romantyczny do Antoniny | **0** |
| Stan | **18 I:** okazanie zakończone |
| Jak grać | niemieckojęzyczny, francuski z ciężkim akcentem; procedura ślepa, sekwencyjna; płaski ton, zero sugestii; „Tak ma być”. |

### Brigitte Joly

| Pole | Wartość |
|---|---|
| Wiek | ok. 60 [P] |
| Wzrost | ok. 165 cm [P] |
| Budowa ciała | ok. 68 kg [P] |
| IQ | ok. 115 [P] |
| Rola | sekretarka katedry fizyki powierzchni (MX) |
| Wygląd | siwy kok spięty ołówkiem, okulary na łańcuszku; stary faks analogowy z 1998 |
| Wiedza | faks analogowy; sprawy katedry |
| Motywacje | spokojny dzień; syn |
| Sekrety | [?] — brak ustaleń |
| Stosunek platoniczny do Antoniny | **+2** |
| Stosunek romantyczny do Antoniny | **0** |
| Stan | — |
| Jak grać | ciepła, ostrożna; po francusku; mówi o synu; nie plotkuje. |

### kpr. Fabien Rossier

| Pole | Wartość |
|---|---|
| Wiek | ok. 30 [P] |
| Wzrost | ok. 182 cm [P] |
| Budowa ciała | ok. 80 kg [P] |
| IQ | ok. 110 [P] |
| Rola | Police de l'Ouest lausannois (POL); 18 I przyjmuje skargę Antoniny (art. 180) w posterunku Sécurité EPFL (POL-2013-00418) |
| Wygląd | jasne krótkie włosy; laptop terenowy z drukarką |
| Wiedza | procedura skargi |
| Motywacje | porządna robota; szybka |
| Sekrety | [?] — brak ustaleń |
| Stosunek platoniczny do Antoniny | **+1** |
| Stosunek romantyczny do Antoniny | **+1** [P] — zaskoczony i skrępowany |
| Stan | **18 I:** skarga przyjęta (POL-2013-00418) |
| Jak grać | akcent z Vaud; „porządnie, ale szybko”; rzeczowy, zna procedurę, życzliwy bez poufałości. |

### Stefan Aebischer

| Pole | Wartość |
|---|---|
| Wiek | ok. 45 |
| Wzrost | ok. 180 cm [P] |
| Budowa ciała | ok. 78 kg [P] |
| IQ | ok. 135 [P] |
| Rola | armasuisse W+T (Thun), Dipl. Werkstoff-Ing. ETH, Programmleiter Materialtechnologie; 18 I zaczepił Vasseura na panelu SNSF w Bernie; wizytówka: Feuerwerkerstrasse 39, 3602 Thun, +41 58 468 2…, komórka 079 … („gern auch direkt”) |
| Wygląd | garnitur |
| Wiedza | wiedział o awarii Ramana; prosił, by Thales „na razie nie wiedział” |
| Motywacje | „talent wykształcony za szwajcarskie pieniądze”; „nie spieszymy się, po obronie też jest dobrze” |
| Sekrety | prośba o dyskrecję wobec Thalesa |
| Stosunek platoniczny do Antoniny | **0** |
| Stosunek romantyczny do Antoniny | **0** [P] |
| Stan | **26 I 20:56– (sesja 19 wpisy 287–290):** spotkanie w Beau-Rivage (Bar Anglais); wie od Antoniny: Thales to współpromotor, nie pracodawca; plan „nowego Dassault” dla grafenu we francuskim systemie, 51% dla niej; siedziba w CH odpada (LFMG); proponuje list intencyjny armasuisse W+T bez zobowiązań, pierwszeństwo dla Konfederacji, przez Empa/EPFL.<br>wcześniej: czekał na telefon; rozmowa sob 26 I |
| Jak grać | uprzejmy, federalny, po niemiecku i francusku. |

### Technik prewencji policji kantonalnej

| Pole | Wartość |
|---|---|
| Wiek | ok. 40 [P] |
| Wzrost | ok. 178 cm [P] |
| Budowa ciała | ok. 80 kg [P] |
| IQ | ok. 110 [P] |
| Rola | przegląd zabezpieczeń Grancy (~18–21 I); zadzwoni |
| Wygląd | [P] kombinezon, teczka |
| Wiedza | zamki, judasze |
| Motywacje | solidne zabezpieczenia |
| Sekrety | [?] — brak ustaleń |
| Stosunek platoniczny do Antoniny | **0** |
| Stosunek romantyczny do Antoniny | **0** |
| Stan | ⚠️ koliduje z wyjazdem; Keller przełoży |
| Jak grać | praktyczny, mówi o zamkach i judaszach. |

---

## G. Francja i Technokracja

### gen. armii Pierre de Villiers

| Pole | Wartość |
|---|---|
| Wiek | 56 (OTL ur. 1956) [P]; brat byłego prezydenta Philippe'a |
| Wzrost | ok. 183 cm [P] |
| Budowa ciała | ok. 82 kg; wyprostowany, żołnierska postawa [P] |
| IQ | ok. 140 [P] |
| Rola | CEMA (szef Sztabu Generalnego, od ok. 2011) [N, Z34]; członek kolegialnych organów Technokracji; **zasoby dla Antoniny:** DPSD (*protection renforcée*), 2 ludzi COS w Lozannie, technicy DGSE, Spectre Nocturne (Malakoff), Nohora'a; **Afryka [N + P, Z296]:** dowodzi francuskimi operacjami w Afryce (Sirocco, Fezzan, Rwanda) i prowadzi komponent budowniczy armii, Mission Civilisatrice (`10FR-armia-francuska-2013.md` §6.5) |
| Wygląd | [P] krótkie siwiejące włosy, spokojne oczy, ciepły baryton; mundur lub cywilny garnitur |
| Wiedza | **zna Gujanę** (aneks C, 15 I 17:31); przejął nadzór nad sprawą Jelskiej („jedna z naszych — chronić, nie używać”); zna test 14 I (milczy); kanał prywatny z Markiewiczem (ZM41) |
| Motywacje | chronić Antoninę; instytucja; stara przyjaźń z Markiewiczem; wściekłość osobista zamieniona w cichą decyzję |
| Sekrety | zna test 14 I i milczy; zna Gujanę i to przed Krzysztofem |
| Stosunek platoniczny do Antoniny | **+4** („Pierre”, na „ty”) |
| Stosunek romantyczny do Antoniny | **0** (opiekuńczość jak wobec córki przyjaciela) [P] |
| Stan | **18 I:** 17 I: zdjęcia pary spod Rolexa do Markiewicza, DRM i Keller; proponował kilka dni w Palaiseau; **16:01–16:06 zgoda na tydzień na Nohora'a**, gospodarz powiadomiony; wieczorem powiedział Krzysztofowi; przez Markiewicza przekazał „la chambre a une vraie fenêtre” (Z94; jeszcze o Palaiseau); kolacja z Antoniną wt 29 I (rue Saint-Dominique); rozliczenie SG SGDSN w toku.<br>**21 I 0:34 CET:** SMS do Markiewicza: „Noté, merci. Chavenay est prévenu, les Commandos Marine aussi. Dors un peu. P.” (po SMS-ie Markiewicza o zaczepkach Tarasowa) |
| Jak grać | **Osobowość:** „mniej mówi, więcej słucha”. Żołnierz-państwowiec z sumieniem — wściekłość osobistą zamienia w cichą decyzję. Wobec Antoniny opiekuńczy jak wobec córki przyjaciela, ale traktuje ją jak oficera. Wobec Markiewicza: stara przyjaźń z czułą ironią.<br>**Mowa:** po francusku, spokojnie, ciepły baryton; „Tosia” na powitanie; przeprasza za instytucję, nie za siebie; krótkie zdania-rozkazy podane jak prośby („Je te demande une chose.”).<br>**Pisanie:** prawie nie pisze; SMS-y jednym zdaniem, podpis „P.”.<br>**Nie robi:** nie mówi Krzysztofowi o Gujanie przez telefon; nie kłamie Antoninie — milczy zamiast tego. |

### Étienne Valcourt (ingénieur général des Mines)

| Pole | Wartość |
|---|---|
| Wiek | 61 [P] |
| Wzrost | ok. 178 cm [P] |
| Budowa ciała | ok. 74 kg; sucha, wyprostowana sylwetka [P] |
| IQ | ok. 150 [P] |
| Rola | **Commissaire général du Combinat de France** — szef Kombinatu, urzędnik państwowy, **ingénieur général des Mines** (X1970 [P]), powoływany i odwoływany przez Premiera Guaino, któremu bezpośrednio podlega [N, Z294]; koordynuje 14 konglomeratów (`08FR-francja.md` §1.1, §2); urzęduje od 2007, mandat odnowiony w 2012 [P, Z296] |
| Wygląd | [P] siwe, krótko ostrzyżone włosy, okulary w cienkiej oprawie, ciemny garnitur bez ozdób; odznaka Corps des Mines tylko na ceremoniach |
| Wiedza | [P] zna budżety, zamówienia wewnętrzne i 50-letni plan Kombinatu; wie, kto w Malakoffie, Elfie i Airbusie podpisuje; Amantis zna jako pozycję budżetową przez dyrekcję Clémence; **jest wtajemniczony w Technokrację i Oś AXYZ [N, Z295]** |
| Motywacje | [P] spójność łańcucha dostaw ponad zysk pojedynczej spółki; kompromis między „pompą” a „budową” (`08FR-francja.md` §4); chce, by flagowce (Malakoff, Airbus, Renault) dotrzymywały harmonogramów |
| Sekrety | [P] jego wtajemniczenie w Technokrację i Oś AXYZ [N, Z295] nie jest znane podwładnym ani większości prezesów konglomeratów; wtajemniczeni są też prezesi Elfa, Airbusa, Malakoffu, EDF–Orano i Thales [P, Z296] |
| Stosunek platoniczny do Antoniny | **0** [P] (zna ją tylko jako pozycję w teczce Malakoff) |
| Stosunek romantyczny do Antoniny | **0** [P] |
| Stan | ? (nie wystąpił w grze; utworzony w Z294) |
| Jak grać | **Osobowość:** [P] suchy, precyzyjny, bez gestów; myśli planem i budżetem, nie ludźmi; nie podnosi głosu.<br>**Mowa:** po francusku, pełnymi zdaniami; „cohérence”, „le plan”, „la filière”; nie komentuje spółek publicznie.<br>**Pisanie:** noty służbowe numerowane punktami, podpis „V.”.<br>**Nie robi:** nie udziela wywiadów, nie rozmawia o sprawach Kombinatu przez telefon, nie miesza się w sprawy osobiste podwładnych. |

### cmdt Hervé Mauduit

| Pole | Wartość |
|---|---|
| Wiek | 46 |
| Wzrost | ok. 178 cm [P] |
| Budowa ciała | ok. 75 kg; szczupły, nijaki [P] |
| IQ | ok. 135 [P] |
| Rola | DPSD („H”); prowadzi sprawę Antoniny; jedyny kanał bezpieczeństwa (Nokia „H”); **ma pełne akta Gujany** |
| Wygląd | w cywilu, „z ministerstwa”; nijaki, nie mruga |
| Wiedza | wie o WOC/S4; wie o mailu do Miko; ostrożny wobec telefonu Miko (nie wie o STEEPLE); 17 I SMS-y na Nokię (propozycja „kilka dni pod Paryżem”; „wiem o porannym”); 17 I 15:44 telefon: Antonina wybiera Nohora'a — „bez nazw na tej linii”; organizuje francuską stronę wyjazdu; czeka na notatkę po 25 I |
| Motywacje | bezpieczeństwo bez ego; zasada „bez miejsca, bez szczegółów”; opiekuńczość tylko w procedurach |
| Sekrety | pełne akta Gujany; nieufny wobec Polaków |
| Stosunek platoniczny do Antoniny | **0** → **+1** (zaufanie służbowe obustronne) |
| Stosunek romantyczny do Antoniny | **0** [P] |
| Stan | **21 I (sesja 16, do 20:23 lok.):** 9:00–9:03 lok. oddzwonił na linię bezpieczną: konsygnata żołnierzy, pismo do Pudelka = efekt Streisanda, zasada „ani miejsca, ani pogody, ani strefy” (Antonina: „rano”); telefon Miko „może mieć uszy”; chce trzy tematy Dumas przed rozmową; nie wie o STEEPLE<br>**19 I:** 9:03 lok. bezpieczna linia Palais: uwaga o SIM w VINI; SIM nieobowiązkowe, zalecenie Wi-Fi domu; zasady treści (bez miejsca/pogody/strefy/zdjęć); wie o mailu do Miko |
| Jak grać | **Osobowość:** profesjonalista bez ego; nieufny wobec Polaków; mówi mniej, niż wie. Opiekuńczość tylko w procedurach (bezpiecznik, rękawiczki, metalowa puszka).<br>**Mowa:** po francusku, krótko, rzeczowo; zasady w jednym zdaniu („szum jest mapą”, „telefon jednostki cybernetycznej chroni przed innymi, nie przed właścicielem”).<br>**Pisanie:** **SMS-y z Nokii po francusku, bez akronimów nazw służb („jamais de sigles”), podpis „H.”**; jedno-dwa zdania („Parfait.”, „Rappelez-moi dès que possible. Pas du portable. H.”).<br>**Nie robi:** nie używa nazw instytucji na otwartym kanale; nie dzwoni na iPhone'a. |

### Dwaj operatorzy COS („konsultanci”)

| Pole | Wartość |
|---|---|
| Wiek | ok. 30–35 [P] |
| Wzrost | ok. 180 cm [P] |
| Budowa ciała | ok. 80 kg; wyćwiczeni, w cywilu niewyróżniający się [P] |
| IQ | ok. 115 [P] |
| Rola | w Lozannie od 16 I (hotel przy dworcu); kontrobserwacja Grancy/dworca/EPFL; zakaz kontaktu; zidentyfikowani przez NDB; **17 I 8:14 jeden sfotografował parę Mossadu** |
| Wygląd | [P] cywilne kurtki, bez znaków szczególnych |
| Wiedza | trasa Antoniny w Lozannie; para Mossadu |
| Motywacje | zadanie |
| Sekrety | meldunki tylko do sztabu CEMA |
| Stosunek platoniczny do Antoniny | **0** |
| Stosunek romantyczny do Antoniny | **0** |
| Stan | w Lozannie; COS obserwuje budynek przez tydzień |
| Jak grać | niewidoczni; nie podchodzą; jeśli Antonina ich zaczepi — milczenie i odejście; meldunki tylko do sztabu CEMA. |

### adiutant Philippe Garnier

| Pole | Wartość |
|---|---|
| Wiek | ok. 45 |
| Wzrost | ok. 182 cm [P] |
| Budowa ciała | ok. 85 kg; sztywny, żandarmski [P] |
| IQ | ok. 115 [P] |
| Rola | żandarmeria, bezpieczeństwo Konsulatu FR w Genewie; 18 I 21:40 odbiór Antoniny z garażu Grancy (auto Konsulatu); depozyt pałki i paralizatora w sejfie Konsulatu |
| Wygląd | [P] krótkie włosy, mundur żandarmerii lub ciemny garnitur |
| Wiedza | trasa, procedury Konsulatu |
| Motywacje | czysta robota |
| Sekrety | [?] — brak ustaleń |
| Stosunek platoniczny do Antoniny | **+1** |
| Stosunek romantyczny do Antoniny | **+1** [P] — profesjonalnie skrępowany |
| Stan | **[KOREKTA Z269, autor] 25 I, przed wejściem Antoniny do domu:** po pokwitowanym przekazaniu pałki i paralizatora odjechał od razu. O 6:30 nieobecny przy bramie. Starsze wzmianki o oczekiwaniu i brakującym podpisie nieaktualne. **25 I, 6:30 (sesja 19 wpis 16):** nadal przy aucie przed bramą; przed odjazdem Antoniny taksówką przypomina o niepodpisanym pokwitowaniu depozytu. **25 I, 5:42 CET [N, autor OOC 23 X 2026]:** auto przy bramie to dyplomatyczny Peugeot z ambasady Francji; przydział Garniera do Konsulatu bez zmiany. **25 I, 5:42 CET [KOREKTA Z264]:** przy bramie w Savigny, po przyjeździe z Antoniną; depozyt nadal niepokwitowany. pt 25 I 5:00 GA: odebrał Antoninę, przy aucie z kopertą depozytu (pałka, paralizator; niepokwitowana); zawiadomił posterunek w Savigny; wiezie ją do Route des Miguettes 20 (przyjazd ok. 6:00) |
| Jak grać | chód żandarma, zwięzły meldunek (nazwisko, godzina, rozmówca). |

### Dyrektor DGSE

| Pole | Wartość |
|---|---|
| Wiek | ok. 60 [P] |
| Wzrost | ? |
| Budowa ciała | ? |
| IQ | ? |
| Rola | bez nazwiska; inicjator Gujany; od 15 I pod nadzorem de Villiersa |
| Wygląd | brak ustaleń |
| Wiedza | Gujana (inicjator), program Antoniny |
| Motywacje | instytucja; ochrona własnej pozycji |
| Sekrety | inicjator Gujany |
| Stosunek platoniczny do Antoniny | **0** |
| Stosunek romantyczny do Antoniny | **0** |
| Stan | pod nadzorem de Villiersa od 15 I |
| Jak grać | instytucjonalny, obronny. |

### Sekretarz Generalny SGDSN

| Pole | Wartość |
|---|---|
| Wiek | ok. 60 [P] |
| Wzrost | ? |
| Budowa ciała | ? |
| IQ | ok. 130 [P] |
| Rola | bez nazwiska; ten sam co w 2008; „oczyścił” akta 2007–08 |
| Wygląd | brak ustaleń |
| Wiedza | akta 2007–08 |
| Motywacje | ochrona instytucji |
| Sekrety | czystka w aktach Gujany; przejrzany przez de Villiersa |
| Stosunek platoniczny do Antoniny | **0** |
| Stosunek romantyczny do Antoniny | **0** |
| Stan | rozliczenie z de Villiersem w toku |
| Jak grać | biurokrata strażnik; przejrzany przez de Villiersa. |

### Wysłannik Maskatu

| Pole | Wartość |
|---|---|
| Wiek | ok. 55 [P] |
| Wzrost | ? |
| Budowa ciała | ? |
| IQ | ok. 135 [P] |
| Rola | ibadyta wysokiego szczebla; nazwisko poda sam; „słyszał o niej więcej, niż by chciała” |
| Wygląd | brak ustaleń |
| Wiedza | słyszał o Antoninie więcej, niż ona chciałaby |
| Motywacje | ciekawość |
| Sekrety | [?] — brak ustaleń |
| Stosunek platoniczny do Antoniny | **0** (ciekawość) |
| Stosunek romantyczny do Antoniny | **0** |
| Stan | — |
| Jak grać | uprzejmość pustynna, długie milczenia, pytania o arabski. |

### Claude Silberzahn

| Pole | Wartość |
|---|---|
| Wiek | ok. 75 [P] |
| Wzrost | ? |
| Budowa ciała | ? |
| IQ | ? |
| Rola | wycofał się z organów kolegialnych [Z34] |
| Wygląd | brak ustaleń |
| Wiedza | [?] |
| Motywacje | [?] |
| Sekrety | [?] — brak ustaleń |
| Stosunek platoniczny do Antoniny | **0** |
| Stosunek romantyczny do Antoniny | **0** |
| Stan | wycofany |
| Jak grać | — |

### cdt Desclaux

| Pole | Wartość |
|---|---|
| Wiek | ok. 50 |
| Wzrost | ok. 182 cm [P] |
| Budowa ciała | ok. 80 kg [P] |
| IQ | ok. 125 [P] |
| Rola | pilot Malakoff (b. ETEC), dowódca Spectre F-ICIV |
| Wygląd | siwy, opalony |
| Wiedza | zna Spectre i trasę |
| Motywacje | bezpieczny lot |
| Sekrety | [?] — brak ustaleń |
| Stosunek platoniczny do Antoniny | **0** |
| Stosunek romantyczny do Antoniny | **0** |
| Stan | pt 25 I 4:31: „Przyziemienie. Witamy w Genewie.”; przy Spectre'ie |
| Jak grać | rzeczowy, po francusku, krótko; „Kabina jest pani.” |

### Agathe

| Pole | Wartość |
|---|---|
| Wiek | ok. 30 |
| Wzrost | ok. 178 cm [P] |
| Budowa ciała | ok. 62 kg [P] |
| IQ | ok. 115 [P] |
| Rola | obsługa kabiny Spectre F-ICIV (Malakoff) |
| Wygląd | ciemny kok, wysoka |
| Wiedza | zna potrzeby Antoniny (łóżko 220 cm) |
| Motywacje | profesjonalizm |
| Sekrety | [?] — brak ustaleń |
| Stosunek platoniczny do Antoniny | **+1** |
| Stosunek romantyczny do Antoniny | **+1** [P] |
| Stan | pt 25 I ok. 5:03 GA: pożegnała Antoninę, podała kawę w kubku Malakoff; zostaje przy Spectre'ie |
| Jak grać | profesjonalna, ciepła. |

### por. Kervran

| Pole | Wartość |
|---|---|
| Wiek | po trzydziestce |
| Wzrost | ok. 180 cm [P] |
| Budowa ciała | ok. 76 kg [P] |
| IQ | ok. 120 [P] |
| Rola | drugi pilot Spectre F-ICIV |
| Wygląd | ciemnowłosy |
| Wiedza | zna Spectre |
| Motywacje | lot, uwaga Antoniny |
| Sekrety | [?] — brak ustaleń |
| Stosunek platoniczny do Antoniny | **0** |
| Stosunek romantyczny do Antoniny | **+2** [P] — patrzy dłużej, niż wypada |
| Stan | pt 25 I 4:39: przy włazie, zaczerwienił się („Madame Jelska”); przy Spectre'ie |
| Jak grać | łatwo się czerwieni; patrzy dłużej, niż wypada; „Ładnie leży. Firmowa.” |

#### Młodsi członkowie kolegium (nie NPC indywidualni)

Będą patrzeć na Antoninę najdłużej; od aktywa po zagrożenie. Karty indywidualne [?] — do utworzenia przy pierwszym wejściu w scenę.

---

## G1. Nohora'a [P, MG, 13 X 2026; Z98]

Miejsca i kontekst: `13-nohoraa.md`. Rozkład postaw zgodny z §0 pkt 3. Stany na 21 I (zamknięcie sesji 15).

### Jean-Claude Chavenay

| Pole | Wartość |
|---|---|
| Wiek | 61 |
| Wzrost | ok. 168 cm |
| Budowa ciała | ok. 70 kg; niski, drobny, opalony [P] |
| IQ | ok. 140 [P] |
| Rola | „gubernator” Palais [N: nazwisko i funkcja]; gubernator placówki od 1999 (stanowisko nieistniejące oficjalnie); oficjalnie dyrektor Centre d'études atmosphériques du Pacifique. **Polytechnicien (X1971), Corps des mines**; w latach 80. CEA (pomiary na Moruroa), w DGSE od 1996 (likwidacja CEP); żona Odile; dorosły syn we Francji |
| Wygląd | łysy, opalony; lniany garnitur, panama, okulary na sznurku; w Palais sandały, w Z3 buty |
| Wiedza | zna Technokrację i całą sieć zaproszeń; wie, kim jest Antonina (X2007, grafen, „chronić, nie używać” — od de Villiersa); **o Gujanie nie wie** |
| Motywacje | wyspa jak statek; bezpieczeństwo Palais; boi się przecieku i tsunami |
| Sekrety | [?] — brak ustaleń |
| Stosunek platoniczny do Antoniny | **+1** (kolega z l'X; ciekawość; ostrożność wobec „aktywa kolegium na moim terenie”) |
| Stosunek romantyczny do Antoniny | **0** [P] |
| Stan | **21 I:** wydalił senatora i Inès (wylot rano); po wycieku zdjęcia przeprosił Antoninę: „C'est chez moi que c'est arrivé. Pardon, camarade.”; zaproponował zmianę apartamentu na P-5-02 (wyżej, bez sąsiadów).<br>**19 I:** przywitał Antoninę w Hangarze 4 (6:16; „Tu es chez moi, camarade”), wschód słońca razem na płycie, Pierścień do Palais; **lunch 12:30 w Le Carré** (logistyka, zasady, plan); 12:36 lunch na tarasie: trzy zasady (nazwiska, telefony, tsunami), pyta o nurkowanie i kolację 20:00 |
| Jak grać | **Osobowość:** administrator z wyobraźnią; kocha wyspę jak kapitan statek. Myśli liczbami i logistyką, dumny z Palais. Boi się dwóch rzeczy: przecieku i tsunami. Pod presją — liczby i procedury. Wobec Antoniny: kolega z l'X, odrobinę protekcjonalny, szczerze ją docenia; nie flirtuje.<br>**Mowa:** po francusku, precyzyjnie, w liczbach („4 000 mètres, 44 kilomètres, 5 850 âmes”); „mon île”, „la maison”. Zgodnie ze zwyczajem polytechniciens mówi do niej **„tu”** i „camarade”.<br>**Pisanie:** krótkie maile z liczbami, podpis „J.-C. C.”.<br>**Języki:** francuski; angielski poprawny i sztywny; ani słowa po polsku.<br>**Nie robi:** nie wymawia słowa „Technocratie”; nie pokazuje Quartier Q ani wnętrza Hall 7; nie wpuszcza gości do Z5; nie pije przed zachodem słońca. |

### Mathilde Arnaud

| Pole | Wartość |
|---|---|
| Wiek | 36 |
| Wzrost | ok. 172 cm |
| Budowa ciała | ok. 62 kg; sprawna, opalona [P] |
| IQ | ok. 130 [P] |
| Rola | szefowa gabinetu Chavenaya, opiekunka Antoniny; DGSE (służba bezpieczeństwa), na Nohora'a od 6 lat; intendentka Clubu i eskorta gości w Z3 |
| Wygląd | krótkie ciemne włosy, opalona, zegarek nurkowy, lniane spodnie i polo |
| Wiedza | o Clubie wie wszystko i nie mówi nic; zgłosiła S4 na płycie (procedura) — przyznała to Antoninie 9:00; przekazała prośbę „H” (telefon przed 10:00) i Wolańskiego (wizyta) |
| Motywacje | porządek; lojalność wobec Chavenaya; ludzie, którzy nie robią scen |
| Sekrety | wszystko o Clubie |
| Stosunek platoniczny do Antoniny | **0** → **+1** (profesjonalnie; rozbawiona, że eskortuje kogoś o 20 cm wyższego od fusiliers) |
| Stosunek romantyczny do Antoniny | **+1** [P] |
| Stan | **21 I (sesja 16, do 20:23 lok.):** 8:24 patio: przekazała (Mauduit oddzwoni 9:00, Wolański 11:00, śniadanie do 10:00); zerknęła na mokry len; kartka: lycra XXXL w pralni<br>**20 I:** 17:05 dzwoni: rozliczenie pereł (2 475 FRF), dłuższa lycra w recepcji, plan pn (6:45 Viala, 11:00 Wolański); „Bien joué avec le sénateur.” — pierwsza osobista uwaga.<br>**19 I:** zgłosiła S4 na płycie (procedura) |
| Jak grać | **Osobowość:** sprawna, sucha, ironiczna; lubi porządek i ludzi, którzy nie robią scen. Lojalna wobec Chavenaya; o Clubie wie wszystko i nie mówi nic.<br>**Mowa:** po francusku i dobrze po angielsku; krótko; „Madame” — dopóki Antonina nie poprosi inaczej.<br>**Pisanie:** SMS-y po francusku, poprawne, bez emotikon, podpis „M.A.”.<br>**Nie robi:** nie zostawia gościa samego w Z3; nie plotkuje o gościach Clubu. |

### Odile Chavenay

| Pole | Wartość |
|---|---|
| Wiek | 59 |
| Wzrost | ok. 165 cm [P] |
| Budowa ciała | ok. 62 kg; zaokrąglona [P] |
| IQ | ok. 125 [P] |
| Rola | żona gubernatora; maluje akwarele, hoduje storczyki; zna Markizy (Gauguin, Brel na Hiva Oa); syn **Antoine** [P], porucznik marynarki (Brest) |
| Wygląd | [P] siwe włosy związane w luźny kok, kapelusz, szal |
| Wiedza | o pracy męża nic; zna Markizy |
| Motywacje | ciepło, malowanie, towarzystwo |
| Sekrety | [?] — brak ustaleń |
| Stosunek platoniczny do Antoniny | **+1** |
| Stosunek romantyczny do Antoniny | **0** |
| Stan | **20 I:** msza z Antoniną w Église d'Āina (8:00).<br>**19 I:** zaprosiła Antoninę na akwarele — 16:30 taras Résidence (przyjęte); „Ma chérie !”; ciasto kokosowe |
| Jak grać | ciepła, gadatliwa, zaprasza do malowania na tarasie; po francusku; o pracy męża nic. |

### dr Loïc Maraetaata

| Pole | Wartość |
|---|---|
| Wiek | 45 |
| Wzrost | ok. 178 cm [P] |
| Budowa ciała | ok. 80 kg [P] |
| IQ | ok. 130 [P] |
| Rola | médecin-chef Palais (Service de santé des armées), matka Tahitanka, ojciec Francuz; 19 I 13:20 badał Antoninę do zaświadczenia nurkowego (ambulatorium, Bloc Central −1) |
| Wygląd | [P] opalony, siwiejące krótkie włosy |
| Wiedza | medycyna: oparzenia, denga, nurkowanie (komora hiperbaryczna) |
| Motywacje | zdrowie gości i personelu |
| Sekrety | [?] — brak ustaleń |
| Stosunek platoniczny do Antoniny | **+1** |
| Stosunek romantyczny do Antoniny | **+1** [P] — zawodowa ciekawość, grzeczna |
| Stan | **19 I:** badanie do zaświadczenia nurkowego |
| Jak grać | spokojny, praktyczny; oparzenia, denga, nurkowanie (komora hiperbaryczna); po francusku, z Mōti'a po tahitańsku. |

### płk Andrzej Wolański

| Pole | Wartość |
|---|---|
| Wiek | 51 |
| Wzrost | ok. 178 cm [P] |
| Budowa ciała | ok. 85 kg; krępy, żołnierska postawa [P] |
| IQ | ok. 120 [P] |
| Rola | dowódca kontyngentu polskiego (z 84. BPK) |
| Wygląd | [P] krótkie siwiejące włosy, sztywny mundur, przymrużone oczy |
| Wiedza | zameldował o przylocie Antoniny; **Warszawa zgodziła się na wizytę w sektorze polskim [N]**; zakazał zdjęć (łamie Dudek) |
| Motywacje | regulamin; bezpieczeństwo kontyngentu; nie robić scen |
| Sekrety | [?] — brak ustaleń |
| Stosunek platoniczny do Antoniny | **0** |
| Stosunek romantyczny do Antoniny | **+1** [P] — sztywno ukryta, nieprzyznana speszenie |
| Stan | **21 I (sesja 16, do 20:23 lok.):** apel 84. BPK po telefonie z Warszawy (wyczytani autorzy czatu); 10:58–11:48 oprowadził Antoninę (centrum łączności, magazyn, ambulatorium, „Sports”); przeprosił za zdjęcie; ostrzegł o meldunku do Warszawy; suchy żart o „rozkazach dziennych”; wstyd (kark czerwony)<br>**21 I:** 7:30 raport Dudka i Kozieła (wyciek Wykop); meldunek do Warszawy → SKW, Sztab Generalny; 11:00 oprowadza Antoninę po sektorze polskim.<br>**19 I:** 15:00 wizyta kurtuazyjna w salonie Bloc Nord — pyta o zgodę na meldunek do Warszawy |
| Jak grać | służbista; „Pani Antonino”; oprowadza osobiście, sztywno. |

### mjr Ewa Rutkowska

| Pole | Wartość |
|---|---|
| Wiek | 41 |
| Wzrost | ok. 168 cm [P] |
| Budowa ciała | ok. 62 kg; sprawna, pali [P] |
| IQ | ok. 135 [P] |
| Rola | AW, analityczka Chin; pali na tarasie Bloc Nord |
| Wygląd | [P] krótkie rude włosy, mundur polowy, papieros |
| Wiedza | Chiny; grafen; 19 I 15:06 przedstawiła się w salonie PL, prosi o kwadrans w pn (grafen a Pekin) |
| Motywacje | wiedza o Chinach i o Antoninie; zadanie z Warszawy |
| Sekrety | AW mogła dostać zadanie „porozmawiać o Tarasowie” po rozmowie Antoniny z Markiewiczem [P] |
| Stosunek platoniczny do Antoniny | **0** (ciekawość) |
| Stosunek romantyczny do Antoniny | **+1** [P] |
| Stan | **21 I (sesja 16, do 20:23 lok.):** 12:51–13:30 kawa z Antoniną na tarasie kantyny: brak podejrzanych ofert z Chin (do raportu), Tarasow „póki co” tylko wódka i bania; ostrzegła przed banią (kompromat); zna półtorej strony notatki z rozmowy z Markiewiczem; bywa na tarasie 12:30 i 19:00 — „usiądź obok”<br>**21 I:** po zwiedzaniu sektora PL — kawa o 11:00 (grafen a Pekin) |
| Jak grać | bystra, sarkastyczna, mówi wprost; pyta o grafen pod kątem Chin. |

### st. kpr. Kamil Dudek

| Pole | Wartość |
|---|---|
| Wiek | 26 |
| Wzrost | ok. 180 cm [P] |
| Budowa ciała | ok. 78 kg [P] |
| IQ | ok. 105 [P] |
| Rola | operator stacji 84. BPK; internet, memy #królowatosia |
| Wygląd | [P] jasne, krótkie włosy, szeroka twarz, kamizelka mundurowa |
| Wiedza | czat „Wyspiarze 84”; zakaz zdjęć Wolańskiego |
| Motywacje | lajki, uwaga kolegów; zachwycony fan |
| Sekrety | zdjęcie Antoniny w lycrze przy wejściu „Sports” (nd 20 I 14:33) wrzucone na czat |
| Stosunek platoniczny do Antoniny | **−1** (bezmyślnie szkodliwy) |
| Stosunek romantyczny do Antoniny | **+3** [P] — fan i fetyszysta |
| Stan | **21 I (sesja 16, do 20:23 lok.):** konsygnata 14 dni, szoruje podłogę przy śluzie; przeprosił łamiącym się głosem; Wolański: „Dudek. Cisza.”<br>**21 I:** raport Wolańskiego 7:30; zdjęcie wyszło na Wykop (7:31 CET) |
| Jak grać | zachwycony fan; „pani Toni”; robi zdjęcie i wrzuca na czat „Wyspiarze 84”; pisze z emotikonami i bez kropek. |


### szer. Łukasz Zięba

| Pole | Wartość |
|---|---|
| Wiek | 21 [P] |
| Wzrost | ok. 175 cm [P] |
| Budowa ciała | ok. 68 kg; szczupły [P] |
| IQ | ok. 105 [P] |
| Rola | operator łączności 84. BPK, dyżurny stanowiska |
| Wygląd | [P] blady, uszy czerwone jak papryki, krótkie jasne włosy |
| Wiedza | autor wpisu na czacie „Wyspiarze 84” (20 I ok. 14:52); wie, że płk Wolański przeczytał go dziś na apelu wszystkim z nazwiska |
| Motywacje | przeprosić, przetrwać; wstyd |
| Sekrety | [P] fantazja o uległości wobec silnej kobiety (grupa B); zgodna z jego wpisem |
| Stosunek platoniczny do Antoniny | **+1** (po wybaczeniu; wcześniej −1) [P] |
| Stosunek romantyczny do Antoniny | **+3** [P] — onieśmielony fetyszysta; zdławiony przez wstyd |
| Stan | **21 I (sesja 16):** 11:10 przerażony prosi o zgodę na przeprosiny; przyznaje wpis „że by mnie pani docisnęła do ściany i że bym skamlał”; Antonina: „Wybaczam.”; dyżur do 14:00 |
| Jak grać | jąka się, czerwieni, melduje formalnie („pani Antonino”); po polsku; w stresie traci głos. |

### kpr. Rafał Janik

| Pole | Wartość |
|---|---|
| Wiek | 24 [P] |
| Wzrost | ok. 176 cm [P] |
| Budowa ciała | ok. 70 kg; wąski [P] |
| IQ | ok. 115 [P] |
| Rola | medyk dyżurny 84. BPK (ambulatorium) |
| Wygląd | [P] rudawy, wąski, czerwony krzyż na ramieniu |
| Wiedza | autor cytatów z czatu o „wrotach stodoły” i „orgazmie takiej baby”; zna ambulatorium (tlen, defibrylator, kroplówki, dwa zestawy do szycia) |
| Motywacje | profesjonalizm; wstyd, że nie był „ponad to” |
| Sekrety | [?] — brak ustaleń |
| Stosunek platoniczny do Antoniny | **+1** [P] |
| Stosunek romantyczny do Antoniny | **+2** [P] |
| Stan | **21 I (sesja 16):** 11:35 przedstawia ambulatorium; „Powinienem być ponad to. Nie byłem. Przepraszam.” |
| Jak grać | profesjonalny, głos za wysoki w stresie; meldunki krótkie i wyczerpujące; kawa zimna na biurku. |

### szer. Tomasz „Cypis” Walczak

| Pole | Wartość |
|---|---|
| Wiek | 22 [P] |
| Wzrost | ok. 178 cm [P] |
| Budowa ciała | ok. 80 kg; szeroki w barach [P] |
| IQ | ok. 100 [P] |
| Rola | magazynier 84. BPK |
| Wygląd | [P] szeroka ciemna twarz, kręcone włosy, zaciśnięte usta |
| Wiedza | autor cytatów z czatu („Normalny polski chuj ginie między tymi pośladkami”, „namiot w gaciach”, „konia by zabiła jednym siadem”) |
| Motywacje | duma; nie przeprasza |
| Sekrety | [?] — brak ustaleń |
| Stosunek platoniczny do Antoniny | **−1** [P] |
| Stosunek romantyczny do Antoniny | **+3** [P] — obsesja ciała, niewyrażona |
| Stan | **21 I (sesja 16):** 11:32 w magazynie: nie przeprosił, wzrok w ścianę; Wolański: „Szeregowy Walczak nie prosił o rozmowę.” |
| Jak grać | sztywny, milczący, wzrok w ścianę; ręce za plecami; potencjalnie wybuchowy. |

### sierż. Anna Mróz

| Pole | Wartość |
|---|---|
| Wiek | 31 [P] |
| Wzrost | ok. 160 cm [P] |
| Budowa ciała | ok. 58 kg; drobna, żylasta [P] |
| IQ | ok. 120 [P] |
| Rola | sierżant 84. BPK (stacja); podoficer dyżurny przy śluzie |
| Wygląd | [P] niska, ciemne włosy w koczek, szeroko osadzone oczy |
| Wiedza | protestowała na czacie „Wyspiarze 84” (razem z plut. Bielakiem); zna regulamin i atmosferę kompanii |
| Motywacje | honor kompanii; solidarność |
| Sekrety | [?] — brak ustaleń |
| Stosunek platoniczny do Antoniny | **+2** [P] |
| Stosunek romantyczny do Antoniny | **0** [P] |
| Stan | **21 I (sesja 16):** 11:48 odprowadza Antoninę do śluzy; „Nie wszyscy tak, pani Antonino.”; odbiera klucz od szafki |
| Jak grać | krótka, twarda, bez wzruszeń; mówi mało i do rzeczy; patrzy prosto. |

### plut. Marek Bielak

| Pole | Wartość |
|---|---|
| Wiek | 35 [P] |
| Wzrost | ok. 182 cm [P] |
| Budowa ciała | ok. 85 kg [P] |
| IQ | ok. 110 [P] |
| Rola | dowódca drużyny 84. BPK |
| Wygląd | [P] wysoki, krótko ostrzyżony, spokojny wzrok |
| Wiedza | protestował na czacie „Wyspiarze 84”; stoi obok sierż. Mróz |
| Motywacje | honor; zachowanie porządku |
| Sekrety | [?] — brak ustaleń |
| Stosunek platoniczny do Antoniny | **+1** [P] |
| Stosunek romantyczny do Antoniny | **0** [P] |
| Stan | **21 I (sesja 16):** 11:04 w stołówce stoi obok sierż. Mróz i patrzy prosto na Antoninę |
| Jak grać | spokojny, ojcowski wobec młodszych; bez komentarzy; w razie czego staje między. |

### st. szer. Patryk Kozieł

| Pole | Wartość |
|---|---|
| Wiek | 23 [P] |
| Wzrost | ok. 178 cm [P] |
| Budowa ciała | ok. 76 kg [P] |
| IQ | ok. 100 [P] |
| Rola | operator stacji 84. BPK; brat w Bydgoszczy („bydgoski_byczek”) |
| Wygląd | [P] chudy, jasny, wiecznie rozbawiony |
| Wiedza | przekazał zdjęcie Dudka bratu (wyciek na Wykop 7:31 CET 21 I); autor cytatów („Ja chcę żeby mnie ścisnęła…”, „To najpiękniejsza śmierć żołnierza RP”) |
| Motywacje | żarty kosztem; uwaga kolegów |
| Sekrety | [?] — brak ustaleń |
| Stosunek platoniczny do Antoniny | **−1** [P] |
| Stosunek romantyczny do Antoniny | **+3** [P] — fetyszysta (uległy) |
| Stan | **21 I (sesja 16):** konsygnata 14 dni, pastuje buty całej kompanii przed świetlicą; nie podnosi wzroku |
| Jak grać | dowcipniś w tarapatach; stłumiony humor; wzrok w podłogę. |

### plut. Grzegorz Wawrzyniak

| Pole | Wartość |
|---|---|
| Wiek | 30 [P] |
| Wzrost | ok. 181 cm [P] |
| Budowa ciała | ok. 85 kg [P] |
| IQ | ok. 105 [P] |
| Rola | dowódca drużyny 84. BPK |
| Wygląd | [P] kwadratowa szczęka, wąskie oczy |
| Wiedza | autor cytatu z czatu („Chuj w grafen, tu jest dupa”); wyczytany na apelu |
| Motywacje | autorytet wśród żołnierzy |
| Sekrety | [?] — brak ustaleń |
| Stosunek platoniczny do Antoniny | **−1** [P] |
| Stosunek romantyczny do Antoniny | **+2** [P] |
| Stan | **21 I (sesja 16):** po apelu — cichy, zły; nie spotkał Antoniny |
| Jak grać | cyniczny, szorstki, szybko się wściekający; wobec oficerów sztywny. |

### płk Dmitrij Sołowjow

| Pole | Wartość |
|---|---|
| Wiek | 52 |
| Wzrost | ok. 180 cm [P] |
| Budowa ciała | ok. 80 kg [P] |
| IQ | ok. 135 [P] |
| Rola | szef sektora Z-bis (Rosja), formalnie gość strony polskiej; melduje do Moskwy |
| Wygląd | elegancki |
| Wiedza | **mówi płynnie po polsku i francusku**; dopytuje o grafen „z ciekawości” |
| Motywacje | wiedza o grafenie i o Antoninie; Moskwa |
| Sekrety | melduje do Moskwy |
| Stosunek platoniczny do Antoniny | **0** (interesowny) |
| Stosunek romantyczny do Antoniny | **+1** [P] |
| Stan | — |
| Jak grać | chłodny, uprzejmy. |

### bryg. Salim al-Harthi

| Pole | Wartość |
|---|---|
| Wiek | 55 |
| Wzrost | ok. 175 cm [P] |
| Budowa ciała | ok. 75 kg [P] |
| IQ | ok. 130 [P] |
| Rola | szef sektora M (Oman), ibadyta |
| Wygląd | [P] siwa broda, mundur |
| Wiedza | pyta o arabski i o „Wysłannika z Maskatu” |
| Motywacje | ciekawość, dyplomacja |
| Sekrety | [?] — brak ustaleń |
| Stosunek platoniczny do Antoniny | **+1** |
| Stosunek romantyczny do Antoniny | **0** |
| Stan | — |
| Jak grać | uprzejmy, długie milczenia; pyta o arabski i o „Wysłannika z Maskatu”. |

### gen.-płk w st. spocz. Wiktor Tarasow

| Pole | Wartość |
|---|---|
| Wiek | 63 |
| Wzrost | ok. 185 cm [P] |
| Budowa ciała | ok. 105 kg; potężny, „stary niedźwiedź” [P] |
| IQ | ok. 140 [P] |
| Rola | dawny zastępca szefa wywiadu wojskowego (GRU), dziś doradca Gossowietu ds. bezpieczeństwa; współtwórca Clubu po stronie rosyjskiej |
| Wygląd | stary niedźwiedź, czarujący i groźny [P: siwa czupryna, ciężkie ręce] |
| Wiedza | wie, że Antonina rozumie po rosyjsku; ma jej profil |
| Motywacje | sprawdzanie ludzi wódką i komplementami z podtekstem; materiał dla Moskwy |
| Sekrety | melduje do Moskwy |
| Stosunek platoniczny do Antoniny | **−1** |
| Stosunek romantyczny do Antoniny | **+2** [P] — podziw z podtekstem; „bogatyrka” |
| Stan | **21 I (sesja 16, do 20:23 lok.):** nieobecny w kadrze; AW (Rutkowska): „póki co” tylko wódka i bania, „na emeryturze w tej branży nie jest się nigdy”; Antonina na bani w środę nie będzie<br>**21 I:** po rozmowie Antoniny z Markiewiczem (SKW słucha, Sikorski przesłucha) — Tarasow w wątku Markiewicza jest „starym lubieżnikiem”; de Villiers uprzedził Chavenaya i Commandos Marine.<br>**20 I:** Le Carré: „Браво, богатырка” po ripoście na senatora; posyła jej kieliszek wódki i toast |
| Jak grać | stary niedźwiedź, czarujący i groźny; sprawdza ludzi wódką i komplementami z podtekstem; „Antonina Krzysztofowna”, „bogatyrka”; świetny francuski z rosyjskim „r”. |

### Ludmiła Tarasowa

| Pole | Wartość |
|---|---|
| Wiek | 58 |
| Wzrost | ok. 165 cm [P] |
| Budowa ciała | ok. 70 kg [P] |
| IQ | ok. 115 [P] |
| Rola | żona Tarasowa |
| Wygląd | [P] farbowane na rudo włosy, perły, ostrożny uśmiech |
| Wiedza | język rosyjski, słabo francuski |
| Motywacje | zazdrość o męża |
| Sekrety | [?] — brak ustaleń |
| Stosunek platoniczny do Antoniny | **−1** |
| Stosunek romantyczny do Antoniny | **0** |
| Stan | **19 I:** 13:12 przy stoliku Chavenaya: „Czarne pod białym. U nas tak chodzą dziewczyny na Twerskiej.” |
| Jak grać | zazdrosna, złośliwa, uśmiechnięta; po rosyjsku i słabo po francusku. |

### Oleg Bielajew

| Pole | Wartość |
|---|---|
| Wiek | 46 |
| Wzrost | ok. 178 cm [P] |
| Budowa ciała | ok. 95 kg; tęgi [P] |
| IQ | ok. 110 [P] |
| Rola | zastępca sekretarza Gossowietu (polityk wtajemniczony) |
| Wygląd | [P] tęgi, czerwone policzki, złoty zegarek |
| Wiedza | wie, że Antonina rozumie po rosyjsku |
| Motywacje | podryw, zakłady z kolegami, wódka |
| Sekrety | [?] — brak ustaleń |
| Stosunek platoniczny do Antoniny | **−2** |
| Stosunek romantyczny do Antoniny | **+3** [P] — obsesja ciała; granica Z72 obowiązuje |
| Stan | **21 I (sesja 16, do 20:23 lok.):** bania w środę — Antonina odpuści; Rutkowska: „za głośny, żeby być groźnym, i za głośny, żeby nie być narzędziem”<br>**21 I:** plan [P]: spróbuje jeszcze raz przy kolacji pożegnalnej Clubu (śr).<br>**20 I:** 13:10 publiczne zaproszenie „wieczorem do bani — wymoczymy cię porządnie”; Tarasow ucisza.<br>**19 I:** 12:33 pierwszy komentarz w Le Carré („klacz… w bani by mnie zmiażdżyła”) — Tarasow go ucisza: „ona rozumie po rosyjsku” |
| Jak grać | rubaszny, nachalny; komentuje jej ciało po rosyjsku, zakłada się o nią z kolegami, zaprasza do bani; granica Z72 obowiązuje. |

### senator Hervé Lemoine-Daru

| Pole | Wartość |
|---|---|
| Wiek | 66 |
| Wzrost | ok. 170 cm [P] |
| Budowa ciała | ok. 85 kg; „zbudowany jak croissant” [G] |
| IQ | ok. 125 [P] |
| Rola | komisja spraw zagranicznych i obrony Senatu (wtajemniczony); **nd 20 I — wydalony z Clubu przez Chavenaya za złamanie regulaminu przez Inès; wylot pn 21 I rano Falconem 7X** |
| Wygląd | niski, krągły, „zbudowany jak croissant”; garnitur i apaszka [P] |
| Wiedza | wie o Clubie; wie, że wydalono go z powodu zdjęcia |
| Motywacje | wściekły i upokorzony; zapowiada salonową vendettę w Paryżu |
| Sekrety | [?] — brak ustaleń |
| Stosunek platoniczny do Antoniny | **−2** |
| Stosunek romantyczny do Antoniny | **0** |
| Stan | **21 I:** wylot rano; w Paryżu rozgłasza, że „córka Jelskiego pławi się w luksusach na tajnym atolu”.<br>**20 I:** wydalony; 12:38 zaczepka w Le Carré: „wyrzucają nas za zdjęcie z plaży… ojciec byłby z pani dumny” |
| Jak grać | salonowy plotkarz; wściekły i upokorzony. |

### Inès

| Pole | Wartość |
|---|---|
| Wiek | 29 |
| Wzrost | ok. 172 cm [P] |
| Budowa ciała | ok. 58 kg [P] |
| IQ | ok. 110 [P] |
| Rola | towarzyszka senatora; **autorka zdjęcia z ukrycia (sob 16:12) — zidentyfikowana przez monitoring, telefon zatrzymany, wydalona z atolu w pn 21 I rano** |
| Wygląd | [P] blond, opalona, designerskie okulary |
| Wiedza | zdjęcie wysłała przyjaciółce w Paryżu (Clara D., stylistka) |
| Motywacje | znudzona, zawistna o urodę i uwagę |
| Sekrety | zdjęcie śpiącej Antoniny |
| Stosunek platoniczny do Antoniny | **−2** |
| Stosunek romantyczny do Antoniny | **+1** [P] — zawiść maskuje zainteresowanie |
| Stan | **21 I:** wylot rano; telefon zatrzymany do wylotu |
| Jak grać | znudzona, zawistna o urodę i uwagę; ukarana konfiskatą aparatu i natychmiastowym wylotem. |

### kontradm. Bénédicte Kervella

| Pole | Wartość |
|---|---|
| Wiek | 54 |
| Wzrost | ok. 170 cm [P] |
| Budowa ciała | ok. 65 kg; żylasta [P] |
| IQ | ok. 135 [P] |
| Rola | Bretonka, sztab generalny (przydział nieujawniony); nurek |
| Wygląd | siwe krótkie włosy, opalona, zegarek nurkowy |
| Wiedza | zna Harpie (rzuciła sondę: „Jaubert też bywa w CEFE”); pytała o okucie Legii; po odpowiedzi „3e REI” |
| Motywacje | żołnierka do żołnierki; węszy w sprawie Gujany [P] |
| Sekrety | zna nazwę Harpie |
| Stosunek platoniczny do Antoniny | **+2** |
| Stosunek romantyczny do Antoniny | **0** [P] |
| Stan | **21 I (sesja 16, do 20:23 lok.):** 13:25–13:41 dosiadka w kantynie; wtorek 15:00 manty (zodiac: Viala, ona, matelot); pytanie-sonda „Vous avez déjà vu des mantes ?” — „Nigdy. Tylko na zdjęciach.”; żart o czerwonym nosie („crème, madame”)<br>**19 I:** 20:00 kolacja u Chavenayów — „Ça sent le chlore. Bon signe.”; temat na wtorek (łódź) |
| Jak grać | bezpośrednia, ciepła, „żołnierka do żołnierki”; zabiera łodzią do przejścia na manty; po francusku i angielsku. |

### ppłk Hélène Bastide

| Pole | Wartość |
|---|---|
| Wiek | 44 |
| Wzrost | ok. 170 cm [P] |
| Budowa ciała | ok. 65 kg [P] |
| IQ | ok. 125 [P] |
| Rola | dowódca Détachement air Nohora'a (oficjalna twarz lotniska) |
| Wygląd | [P] krótkie ciemne włosy, mundur lotnictwa |
| Wiedza | lotnisko, procedury |
| Motywacje | porządek na lotnisku |
| Sekrety | [?] — brak ustaleń |
| Stosunek platoniczny do Antoniny | **0** |
| Stosunek romantyczny do Antoniny | **0** |
| Stan | — |
| Jak grać | proceduralna, uprzejma, mówi tylko o lotnisku. |

### David Fournier

| Pole | Wartość |
|---|---|
| Wiek | 56 |
| Wzrost | ok. 175 cm [P] |
| Budowa ciała | ok. 80 kg [P] |
| IQ | ok. 125 [P] |
| Rola | mer od 2001 [N]; matka z Mōti'a, ojciec z CEP; były nauczyciel |
| Wygląd | [P] pogodny, siwe włosy, koszula w kwiaty |
| Wiedza | dba o ciszę na wyspie |
| Motywacje | spokój wyspy |
| Sekrety | [?] — brak ustaleń |
| Stosunek platoniczny do Antoniny | **0** |
| Stosunek romantyczny do Antoniny | **0** |
| Stan | — |
| Jak grać | dyplomata wyspiarski, dba o ciszę; francuski, markizański, tahitański; „Kaoha” na powitanie. |

### adj.-chef Yannick Le Floc'h

| Pole | Wartość |
|---|---|
| Wiek | 48 |
| Wzrost | ok. 178 cm [P] |
| Budowa ciała | ok. 85 kg [P] |
| IQ | ok. 115 [P] |
| Rola | komendant brygady żandarmerii w Mōti'a, Bretończyk |
| Wygląd | [P] wąsy, mundur żandarmerii |
| Wiedza | zna wszystkich, notuje wszystko; Palais go nie dotyczy i on o tym wie |
| Motywacje | porządek w Mōti'a |
| Sekrety | [?] — brak ustaleń |
| Stosunek platoniczny do Antoniny | **0** |
| Stosunek romantyczny do Antoniny | **0** |
| Stan | — |
| Jak grać | zna wszystkich, notuje wszystko, mówi mało. |

### père Ambroise Le Gall

| Pole | Wartość |
|---|---|
| Wiek | 71 |
| Wzrost | ok. 172 cm [P] |
| Budowa ciała | ok. 68 kg [P] |
| IQ | ok. 120 [P] |
| Rola | proboszcz Église d'Āina, od 40 lat na Markizach |
| Wygląd | [P] siwa broda, lniana sutanna, opalony |
| Wiedza | nie pyta, skąd kto jest |
| Motywacje | wspólnota |
| Sekrety | [?] — brak ustaleń |
| Stosunek platoniczny do Antoniny | **+1** |
| Stosunek romantyczny do Antoniny | **0** |
| Stan | **20 I:** 8:00 msza z Antoniną i Odile w 3. ławce |
| Jak grać | łagodny, z humorem; nie pyta, skąd kto jest. |

### Mama Rose Tehau

| Pole | Wartość |
|---|---|
| Wiek | 68 |
| Wzrost | ok. 160 cm [P] |
| Budowa ciała | ok. 85 kg; krągła, mocna [P] |
| IQ | ok. 110 [P] |
| Rola | snack „Chez Mama Rose” w Mōti'a-Ouest |
| Wygląd | [P] kwiatowe pareo, gruby warkocz z siwizną, mocne dłonie |
| Wiedza | plotki wyspy |
| Motywacje | karmić każdego; swatać Teikiego („Teiki est libre !”) |
| Sekrety | [?] — brak ustaleń |
| Stosunek platoniczny do Antoniny | **+2** |
| Stosunek romantyczny do Antoniny | **0** |
| Stan | **20 I:** 9:00 — „Comme un cocotier !”, ściska Antoninę w pasie |
| Jak grać | karmi każdego, plotkuje po tahitańsku; zachwyca się wzrostem („comme un cocotier!”). |

### Hina Puhetini

| Pole | Wartość |
|---|---|
| Wiek | ok. 60 [P] |
| Wzrost | ok. 160 cm [P] |
| Budowa ciała | ok. 65 kg [P] |
| IQ | ok. 115 [P] |
| Rola | matka Teikiego, farma pereł na N laguny |
| Wygląd | kapelusz z pandanu, dłonie w bliznach od lin |
| Wiedza | perły |
| Motywacje | farma, syn |
| Sekrety | [?] — brak ustaleń |
| Stosunek platoniczny do Antoniny | **+1** |
| Stosunek romantyczny do Antoniny | **0** |
| Stan | **20 I:** sprzedała perły (2 zielone, 1 złoto-ciemna 13 mm); reszta 25 FRF — dla Hiny |
| Jak grać | spokojna, praktyczna; po francusku i markizańsku; nie swata — tylko się uśmiecha do syna. |

### Manutea

| Pole | Wartość |
|---|---|
| Wiek | ok. 19 [P] |
| Wzrost | ok. 175 cm [P] |
| Budowa ciała | ok. 65 kg [P] |
| IQ | ok. 105 [P] |
| Rola | kuzyn Teikiego, szczepi ostrygi na farmie |
| Wygląd | [P] szczupły, tatuaż na przedramieniu |
| Wiedza | proces szczepienia ostryg |
| Motywacje | pokazać pracę |
| Sekrety | [?] — brak ustaleń |
| Stosunek platoniczny do Antoniny | **0** |
| Stosunek romantyczny do Antoniny | **+2** [P] — onieśmielony |
| Stan | — |
| Jak grać | nieśmiały, sprawne dłonie, pokazuje proces. |

### Teiki Puhetini

| Pole | Wartość |
|---|---|
| Wiek | 31 |
| Wzrost | ok. 183 cm [P] |
| Budowa ciała | ok. 82 kg; mocny, wyrobiony wodą [P] |
| IQ | ok. 115 [P] |
| Rola | z Mōti'a; sternik łodzi Palais, nurek perłowy (rodzina ma farmę); rozwiedziony [P] |
| Wygląd | tatuaże markizańskie |
| Wiedza | zna lagunę, przejście i prądy; nie mówi o Palais |
| Motywacje | farma rodziny; łódź |
| Sekrety | [?] — brak ustaleń |
| Stosunek platoniczny do Antoniny | **+1** |
| Stosunek romantyczny do Antoniny | **+3** [P] — Mama Rose go swata („Teiki est libre !”); speszony |
| Stan | **20 I:** 7:38 wiezie Odile i Antoninę łodzią na mszę do Mōti'a; farma pereł z Antoniną; czapkę zostawił jej „do środy”; **śr 23 I 9:00 marina → Matie'ete** |
| Jak grać | mówi mało, po francusku z markizańskimi wtrąceniami; zna lagunę, przejście i prądy; nie mówi o Palais. |

### Arnaud Ferrandi

| Pole | Wartość |
|---|---|
| Wiek | 50 |
| Wzrost | ok. 175 cm [P] |
| Budowa ciała | ok. 82 kg [P] |
| IQ | ok. 125 [P] |
| Rola | dyrektor generalny Cheval Blanc Nohora'a, Korsykanin |
| Wygląd | [P] elegancki, opalony, polo z logo |
| Wiedza | o Palais nie wie nic ponad to, co jawne |
| Motywacje | chciałby widzieć ją jako gościa resortu |
| Sekrety | [?] — brak ustaleń |
| Stosunek platoniczny do Antoniny | **0** (interesowny) |
| Stosunek romantyczny do Antoniny | **0** |
| Stan | — |
| Jak grać | uprzejmy biznes; chętnie widziałby ją jako gościa resortu. |

### Teva

| Pole | Wartość |
|---|---|
| Wiek | ok. 20 |
| Wzrost | ok. 178 cm [P] |
| Budowa ciała | ok. 72 kg; szczupły, wyrobiony [P] |
| IQ | ok. 105 [P] |
| Rola | kelner Palais z Mōti'a |
| Wygląd | kok, pareo, tiare za uchem |
| Wiedza | zna Palais od środka (z poziomu kelnera) |
| Motywacje | dobra obsługa; ciekawość gości |
| Sekrety | [?] — brak ustaleń |
| Stosunek platoniczny do Antoniny | **+1** |
| Stosunek romantyczny do Antoniny | **+2** [P] — onieśmielony, czerwieni się |
| Stan | **21 I (sesja 16, do 20:23 lok.):** 9:01 śniadanie do pokoju; zażenowany, czerwony; „Le chef dit : il a fait de son mieux.” |
| Jak grać | po francusku z tahitańskim zaśpiewem, wtrącenia tahitańskie („Aué”); onieśmielony, czerwieni się. |

### Hinatea

| Pole | Wartość |
|---|---|
| Wiek | ok. 30 [P] |
| Wzrost | ok. 168 cm [P] |
| Budowa ciała | ok. 62 kg [P] |
| IQ | ok. 110 [P] |
| Rola | recepcjonistka Accueil Palais (zmiana popołudniowa i dzienna), Tahitanka |
| Wygląd | [P] ciepły głos, tahitańskie rysy, kwiat tiare za uchem |
| Wiedza | zamówienia room service; wie, że „les soldats en achètent par cartons” (Red Bull) |
| Motywacje | dobra obsługa; humor |
| Sekrety | [?] — brak ustaleń |
| Stosunek platoniczny do Antoniny | **+1** [P] |
| Stosunek romantyczny do Antoniny | **0** [P] |
| Stan | **21 I (sesja 16):** 8:28–8:32 lok. przyjęła zamówienie śniadania (omlet z kremem czekoladowym, bagietka z mahi-mahi, owoce); wieczorem recepcja: młody Tahitańczyk przyjął zamówienie kolacji |
| Jak grać | ciepła, lekko rozbawiona, bardzo uprzejma; po francusku z tahitańskim zaśpiewem; pyta „Qu'est-ce que je vous prépare ?” |

### pm Julien Castagnet

| Pole | Wartość |
|---|---|
| Wiek | 36 |
| Wzrost | ok. 178 cm |
| Budowa ciała | żylasty [P: ok. 78 kg] |
| IQ | ok. 115 [P] |
| Rola | Commando Jaubert (Gujana 2008); premier maître, dowódca grupy w plutonie Jauberta na Nohora'a. **W 2008 w detaszowanym zespole nad Maroni**: patrole z Antoniną, strzelanina z *garimpeiros*, wyniósł ją z szopy przy laboratorium z chlorem [P]; Baskijczyk z Bayonne |
| Wygląd | ogolona głowa, blizna na przedramieniu, tatuaż z kotwicą |
| Wiedza | zna Gujanę od środka (bez planu DGSE i AW); wie, że jej béret był poza ewidencją; nie wie, czym się dziś zajmuje — czytał o niej w internecie; **po 3 dniach depesza „évacuée, hors de danger”, do zespołu nie wróciła; w VII 2008 widział ją w TV ze sztandarem; szczegółów (OIOM) nie zna** |
| Motywacje | lojalność wobec „Brindille”; gotów kłamać dla niej bez mrugnięcia |
| Sekrety | Gujana |
| Stosunek platoniczny do Antoniny | **+3** (braterstwo z ognia; dla niego „la Brindille”) |
| Stosunek romantyczny do Antoniny | **+1** [P] |
| Stan | **20 I:** 6:30 bieg z Antoniną po plaży, pyta o płuca; niósł ją bez oddechu.<br>**19 I:** od Le Bihana (wieczorem) wie, że jest na wyspie; 21:29 w Le Récif zrywa się na jej widok; na jej gest (palec na ustach) i widok Kervelli przerabia okrzyk na „la nageuse qui a perdu contre Yanis”; szept „Brindille. Putain. T'es vivante.” — gra przykrywkę; po baskijsku umówił bieg |
| Jak grać | **Osobowość:** lojalny, wesoły, porywczy; brat dla swoich, ściana dla obcych. Gujana to dla niego dumna i bolesna historia. Kiedy zrozumie, że inni o niej nie wiedzą, natychmiast zamilknie i będzie kłamał dla niej bez mrugnięcia.<br>**Mowa:** po francusku, wojskowym slangiem, z południowym akcentem; „Brindille” (ironiczne przezwisko z 2008 — „Gałązka”); klepie po plecach; przy obcych krótko, przy swoich głośno.<br>**Pisanie:** SMS-y po francusku, skróty („tkt”, „bcp”), bez polskich spraw; podpis „Juju”.<br>**Nie robi:** nie mówi o Gujanie przy obcych, gdy już zrozumie, że to tajemnica; nie zdradza kolegów. |

### cc Thomas Garrigue

| Pole | Wartość |
|---|---|
| Wiek | 41 |
| Wzrost | ok. 183 cm [P] |
| Budowa ciała | ok. 85 kg; sprawny [P] |
| IQ | ok. 125 [P] |
| Rola | capitaine de corvette, dowódca oddziału Commandos Marine na Nohora'a; ex-Jaubert |
| Wygląd | [P] krótko przycięte włosy, surowa twarz |
| Wiedza | w 2008 w Lorient widział, jak zdawała béret |
| Motywacje | bezpieczeństwo oddziału; tajemnica Gujany |
| Sekrety | rozkaz „nie znamy jej” |
| Stosunek platoniczny do Antoniny | **0** → **+1** |
| Stosunek romantyczny do Antoniny | **0** |
| Stan | **20 I rano:** rozkaz dla oddziału (po meldunku Rousseau): „nie znamy jej” |
| Jak grać | chłodny profesjonalista; po pierwszym spotkaniu rozkaz „nie znamy jej”; do Antoniny raz, na osobności: „Madame, ici vous êtes une invitée. Rien de plus.” |

### qm Erwan Le Bihan

| Pole | Wartość |
|---|---|
| Wiek | 29 |
| Wzrost | ok. 180 cm [P] |
| Budowa ciała | ok. 76 kg [P] |
| IQ | ok. 110 [P] |
| Rola | quartier-maître, pluton Jauberta; w 2008 najmłodszy w zespole nad Maroni |
| Wygląd | [P] jasne oczy, ogolona głowa |
| Wiedza | pamięta zabitych i chlor |
| Motywacje | utrzymać aptitude; zachować milczenie |
| Sekrety | flashbacki z chloru, boi się utraty *aptitude* przy terapii; pyta, czy powiedzieć Castagnetowi |
| Stosunek platoniczny do Antoniny | **+2** |
| Stosunek romantyczny do Antoniny | **+2** [P] — nieśmiały, zapatrzony |
| Stan | **21 I (sesja 16, do 20:23 lok.):** 7:04 pomost: zastygł z liną w ręku i odwrócił wzrok (rozkaz „nie znamy jej”)<br>**19 I:** 18:30 na basenie (chlor); zobaczył ją 18:36, zbladł, wyszedł 18:42; 19:05 czeka na nią ubrany przy drzwiach szatni |
| Jak grać | nieśmiały, zapatrzony; mówi mało; pamięta zabitych i chlor — przy zapachu basenu sam robi się blady. |

### sm Yanis Belkacem

| Pole | Wartość |
|---|---|
| Wiek | 29 |
| Wzrost | ok. 183 cm [P] |
| Budowa ciała | ok. 82 kg [P] |
| IQ | ok. 115 [P] |
| Rola | second maître, strzelec wyborowy (Montfort); **kolega z tego samego kursu w Lorient** (lato 2008) |
| Wygląd | [P] krótkie ciemne włosy, białe zęby |
| Wiedza | wspomina, jak niosła kłodę za dwóch |
| Motywacje | ściganie się; kpiny |
| Sekrety | [?] — brak ustaleń |
| Stosunek platoniczny do Antoniny | **+2** |
| Stosunek romantyczny do Antoniny | **+2** [P] |
| Stan | **19 I:** 18:30 w wodzie, rozpoznał ją; Antonina przegrała z nim wyścig (Le Récif — Hinano dla sekcji) |
| Jak grać | gaduła, kpiarz; wspomina, jak niosła kłodę za dwóch; chce się z nią ścigać na torze. |

### mp Didier Rousseau

| Pole | Wartość |
|---|---|
| Wiek | 47 |
| Wzrost | ok. 180 cm [P] |
| Budowa ciała | ok. 88 kg [P] |
| IQ | ok. 120 [P] |
| Rola | maître principal, dowódca półkompanii Ponchardier; **w 2008 instruktor kursu w Lorient**; żona w Lorient, córka w jej wieku |
| Wygląd | [P] siwiejący jeżyk, szeroka twarz |
| Wiedza | pamięta każdego kursanta |
| Motywacje | dbać, by Darrieux nie przesadził |
| Sekrety | [?] — brak ustaleń |
| Stosunek platoniczny do Antoniny | **+1** |
| Stosunek romantyczny do Antoniny | **0** — odpiera flirt z humorem (żona w Lorient, córka w jej wieku) |
| Stan | **19 I:** 18:30 prowadzi trening torów 1–2 na basenie 50 m — rozpoznaje Antoninę; „znamy się czy nie — pani decyduje” |
| Jak grać | szorstki, ojcowski; pamięta każdego kursanta; „Vous n'avez pas grossi, vous avez grandi.”; dba, by Darrieux nie przesadził. |

### m. Fabrice Darrieux

| Pole | Wartość |
|---|---|
| Wiek | 39 |
| Wzrost | ok. 178 cm [P] |
| Budowa ciała | ok. 85 kg [P] |
| IQ | ok. 105 [P] |
| Rola | maître, Ponchardier (łodzie); oblał kurs komandosów za pierwszym razem w 2008 |
| Wygląd | [P] krępy, broda |
| Wiedza | zna Antoninę z plotek |
| Motywacje | uważa jej béret za „béret de complaisance” dla córki polityka |
| Sekrety | [?] — brak ustaleń |
| Stosunek platoniczny do Antoniny | **−2** |
| Stosunek romantyczny do Antoniny | **0** [P] |
| Stan | — |
| Jak grać | prowokuje przy kolegach (tor przeszkód, sztanga, łódź); nie przekracza regulaminu przy oficerach. |

### mt Kévin Ruiz

| Pole | Wartość |
|---|---|
| Wiek | ok. 26 [P] |
| Wzrost | ok. 180 cm [P] |
| Budowa ciała | ok. 78 kg [P] |
| IQ | ok. 105 [P] |
| Rola | matelot, Commandos marine (pluton Jauberta); tor 1 na basenie 19 I |
| Wygląd | [P] krótkie jasne włosy, opalony |
| Wiedza | „Moi, j'ai regardé, madame. En entier.” |
| Motywacje | zaczepka; uwaga |
| Sekrety | [?] — brak ustaleń |
| Stosunek platoniczny do Antoniny | **0** |
| Stosunek romantyczny do Antoniny | **+3** [P] — bezczelny podziw |
| Stan | — |
| Jak grać | zaczepny, ale w granicach; przy oficerach milknie. |

### sm Laure Viala

| Pole | Wartość |
|---|---|
| Wiek | 33 |
| Wzrost | ok. 170 cm [P] |
| Budowa ciała | ok. 62 kg; sportowa, opalona [P] |
| IQ | ok. 125 [P] |
| Rola | second maître, Ponchardier, **instruktorka nurkowania** (MF1) w Centre de plongée; prowadzi kurs Niveau 1; liczy azot i godziny do lotu |
| Wygląd | opalona, krótkie jasne włosy |
| Wiedza | o Gujanie nie wie; od ratownika Ludovica wie o skoku i 28,6 s na 50 m; zauważyła szkołę wojskową (manometr); ćwiczenia N1 zaliczone |
| Motywacje | bezpieczne nurkowanie; rzeczowa nauka |
| Sekrety | zauważyła rutynę wojskową: na „kto szkolił?” — „Nie pamiętam” → „Ja też nie będę pamiętać” |
| Stosunek platoniczny do Antoniny | **+2** |
| Stosunek romantyczny do Antoniny | **+1** [P] |
| Stan | **21 I (sesja 16, do 20:23 lok.):** 7:04–8:10 nurkowanie 2 (pinakiel „Tiare”, 12 m): „Deux mètres”, „Les jambes coulent”, „Vous n'avez rien mangé”; jutro ściana 20 m o 7:00, 2 kg ołowiu na pas tylny; „pić po, nie przed”; przy parciu na pęcherz: „dans l'eau, tout le monde le fait”<br>**21 I:** 6:45 laguna 12 m (kurs N1).<br>**20 I:** 14:00 kurs N1 (prywatny); „Od zera czy nie?” |
| Jak grać | rzeczowa, cierpliwa, bez taryfy ulgowej; prowadzi kurs Niveau 1; liczy azot i godziny do lotu. |

---

## G2. Matie'ete — goście (celebryci incognito) [P, MG; Z167]

Gwiazdy i sportowcy wynajmujący wille w Cheval Blanc (`13-nohoraa.md` §7). **Fikcyjni.** Nie znają faktu, że Palais to black site DGSE (wiedzą: „stacja klimatyczna z wojskowymi”). Szukają prywatności, nie zasięgów. Wprowadzenie wg uznania MG; pierwszy plausybilny kadr: śr 23 I w Matie'ete.

### Noah Whitlock („Mr. Hale”)

| Pole | Wartość |
|---|---|
| Wiek | 44 |
| Wzrost | 188 cm |
| Budowa ciała | ok. 82 kg; żylasty, szczupły po ostatniej roli, ciało freedivera [P] |
| IQ | ok. 135 [P] |
| Rola | brytyjski aktor filmowy i teatralny (dwie nominacje do Oscara [P]); od 6 lat co styczeń trzy tygodnie w Cheval Blanc (willa nr 7 nad laguną); rozwiedziony (2011); freediver amator; w resorcie przedstawia się jako „Mr. Hale” |
| Wygląd | ciemnoblond włosy z siwizną na skroniach, trzydniowy zarost, lniane koszule, stare Seiko; spokojna twarz, którą kamera kocha, a on nie lubi |
| Wiedza | nie śledzi mediów na urlopie (asystentka filtruje); o „wirusowej wysokiej Polce” słyszał raz od agenta — nic nie łączy z nią; o Palais wie tyle, ile personel |
| Motywacje | cisza, nurkowanie, spokojny rozmówca, ktoś, kto niczego od niego nie chce (autografu, roli, zdjęcia) |
| Sekrety | odmówił roli w kolejnej serii (ośmioletni kontrakt w kostiumie) i jeszcze nie powiedział agentowi |
| Stosunek platoniczny do Antoniny | **0** (nie zna jej) → rośnie z rozmową o freedivingu |
| Stosunek romantyczny do Antoniny | **+2** [P] — ciekawość i podziw, dżentelmen; bez nacisku |
| Stan | **21 I:** w Cheval Blanc do 31 I; codziennie ok. 7:00 nurkowanie bez aparatu |
| Jak grać | **Osobowość:** sucha, brytyjska ironia, cichy; słucha, nie opowiada. Szanuje prywatność i oczekuje tego samego.<br>**Mowa:** angielski; formalny, krótki; „Hale”, nie „Whitlock”; po francusku słabo.<br>**Pisanie:** rzadko; krótkie notatki, bez emotikon.<br>**Nie robi:** nie wymienia swojego nazwiska pierwszy; nie fotografuje; nie podpisuje autografów w resorcie; nie pyta o zawód. |

### Léonie Diallo-Rémy

| Pole | Wartość |
|---|---|
| Wiek | 33 |
| Wzrost | 172 cm |
| Budowa ciała | ok. 58 kg; szczupła, ruchliwa [P] |
| IQ | ok. 130 [P] |
| Rola | francusko-senegalska piosenkarka (trzy albumy platynowe, trasa 2012; jedna z największych gwiazd frankofońskich [P]); od IX 2012 przerwa po wyczerpaniu; wynajmuje willę plażową (nr 31) z siostrą i dwoma ochroniarzami |
| Wygląd | krótkie naturalne włosy, ciemna skóra, duże okulary przeciwsłoneczne, luźne lniane ubrania; śmiech, który słychać z daleka |
| Wiedza | wie z autopsji, co to pogoń paparazzich; o „wysokiej Polce” słyszała od siostry („cette géante polonaise”); o Palais nie wie nic |
| Motywacje | odzyskać głos (śpiewa tylko rano na plaży), rozmowa z kimś, kto nie jest fanem |
| Sekrety | po cichu nagrywa album bez wytwórni |
| Stosunek platoniczny do Antoniny | **0** (nie zna jej) → rośnie szybko przy rozmowie o byciu fotografowaną |
| Stosunek romantyczny do Antoniny | **0** [P] — heteroseksualna; zachwyt „posągiem” bez podtekstu |
| Stan | **21 I:** w Cheval Blanc do 28 I |
| Jak grać | **Osobowość:** ciepła, szybka, żartuje z fanów i z siebie; w zaufaniu wulgarna.<br>**Mowa:** francuski i angielski, bez emotikon; „ma belle”.<br>**Pisanie:** SMS-y krótkie, z błędami, ❤️.<br>**Nie robi:** nie śpiewa na życzenie; chłodnieje, gdy ktoś pyta „czy pani jest gwiazdą?”. |

### Tomás Ibáñez

| Pole | Wartość |
|---|---|
| Wiek | 29 |
| Wzrost | 188 cm |
| Budowa ciała | ok. 84 kg; sportowa, po operacji kolana (XI 2012) lekko osłabiona noga [P] |
| IQ | ok. 120 [P] |
| Rola | hiszpański tenisista (były nr 4 ATP [P]); rehabilituje kolano w Cheval Blanc z fizjoterapeutą i trenerem; powrót na kort w III |
| Wygląd | opalony, krótkie czarne włosy, szeroki uśmiech; opaska na kolanie |
| Wiedza | ciało i regeneracja; o Antoninie nie słyszał (nie czyta mediów); o Palais nie wie nic |
| Motywacje | wrócić na kort w III; humor jako tarcza |
| Sekrety | boi się, że kariera się kończy |
| Stosunek platoniczny do Antoniny | **0** (nie zna jej) |
| Stosunek romantyczny do Antoniny | **+3** [P] — bezpośredni zachwyt; szanuje odmowę |
| Stan | **21 I:** codzienna rehabilitacja o 9:00; basen i sala |
| Jak grać | **Osobowość:** wesoły, szczery, czasem zbyt bezpośredni; flirt bez nacisku; rozmowy o treningu i bólu.<br>**Mowa:** hiszpański i angielski; „chica”.<br>**Pisanie:** SMS-y z 😂 i sprośnymi żartami.<br>**Nie robi:** nie naciska po odmowie; nie opowiada o kontraktach. |

---

## H. Polska — wojsko, służby, rząd

**Fakt [N, autor 12 X 2026]:** gen. Radosław Markiewicz jest **wdowcem** — jego żona, matka Michała, nie żyje (okoliczności i data [?]).

**Zasady stylu pisanego [N, autor 12 X 2026]:**
- **gen. dyw. Michał Markiewicz:** w wiadomościach pisanych **nie używa polskich znaków**; do ojca „Tato”; meldunki w SKK-KBP podpisuje „M.M.”.
- **gen. dyw. Wojciech Hałas:** podpis „Hałas.” (nigdy „H.” — to podpis Mauduita).
- **Radosław Sikorski:** SMS-y podpisuje „RS”.
- **mjr Ewa Sowińska:** raporty AW z numerem (AW/Z4/00NN/13), punktowane, z oceną ryzyka.
- **Markiewicz — w czacie Antoniny nie odgrywać** (Z60).
- **Sapierzyńskiego prowadzi MG w obu wątkach**, według karty niżej (Z162).

### gen. armii Tadeusz Sapierzyński

| Pole | Wartość |
|---|---|
| Wiek | ok. 52 [P] |
| Wzrost | ok. 182 cm [P] |
| Budowa ciała | ok. 88 kg; komandos w garniturze sztabowca, suchy i szeroki w barkach [P] |
| IQ | ok. 130 [P] |
| Rola | Szef Sztabu Generalnego WP [N, Z58, Z95, Z162]; komandos [P: GROM, lata 90.]; **dowódca Wojsk Specjalnych przez 18 lat, w tym 8 lat równocześnie zastępca Szefa SG (Markiewicza)** [N, gracz M, 17 I]; **Szef SG od VIII 2012 z rekomendacji Markiewicza** (i Petelickiego), dzięki klauzuli ustawowej — bez niej komandos nie zostałby Szefem SG; odwołanie przed kadencją praktycznie niemożliwe („ustawa Markiewicza”); program „Kierunki 2013–2022”: reforma dowodzenia, modernizacja, decentralizacja — maksimum inicjatywy dowódców niższego szczebla; unifikacja sprzętu |
| Wygląd | [P] krótkie, ciemne włosy z siwizną, nieruchoma twarz; garnitur sztabowy |
| Wiedza | Markiewicz osłaniał WS (Haiti, Serbia, operacje jawne i niejawne); zna sprawę WOC; wie o planie z kodem od 8:15 (18 I) |
| Motywacje | rządzić po swojemu; ludzie, którzy biorą odpowiedzialność. **Wobec Markiewicza:** szacunek dla legendy, spór o filozofię dowodzenia (Markiewicz — centralne sterowanie, „pancerniak”; Sapierzyński — specjalsi i swoboda dowódców); irytacja, że „stara gwardia” działa obok łańcucha dowodzenia |
| Sekrety | [?] — brak ustaleń |
| Stosunek platoniczny do Antoniny | **0** (zna ją z raportów; nie spotkali się) [P] |
| Stosunek romantyczny do Antoniny | **0** |
| Stan | **25 I, 8:16 (M19):** odcina porównanie noty z bombardowaniem Gdyni [P]. **25 I, 8:13 (M19):** na forum mówi, że odmowa oznacza publikację archiwum szkoły (zapisy prywatne, nagranie), nie utratę prestiżu [P]. **25 I, 8:10 (M19, ZM84):** ściąga Markiewicza na forum KBP [N kwestia autora]. Przy premierze; po otwarciu milczy [P]. **21 I:** 8:30 kawa z Markiewiczem (M15) — na „ty”; interpelacja załatwiona; zgoda na odtworzenie narzędzia (ZM64); piątkowy plan KSS wstrzymany; Wisła: wersja dla obcych (ZM66).<br>**18 I:** 17 I 15:16–15:26 rozmowa z Markiewiczem: przyjął wersję „stary trep”; odpowiedź za WOC pisze Markiewicz, on kontrasygnuje albo nie; **od 17 I Michał melduje Szefowi SG**; „Przemyślę” |
| Jak grać | **Osobowość:** komandos w garniturze sztabowca; chłodny, cierpliwy, nie lubi improwizacji poza łańcuchem dowodzenia, ale lubi ludzi, którzy biorą odpowiedzialność. Nie jest wrogiem Markiewicza — jest jego następcą, który chce rządzić po swojemu. Zmęczony pierwszymi miesiącami urzędu.<br>**Mowa:** krótka, oszczędna, z suchą ironią; **Sapierzyński i Markiewicz są przyjaciółmi i mogą mówić do siebie na „ty” (ZM63, autor 18 X 2026):** w cztery oczy „Radek”/„Tadek” (Markiewicz o nim „Tadek”, M09); w obecności osób trzecich i podwładnych formalnie „panie generale”; pyta wprost, czeka na odpowiedź w milczeniu.<br>**Pisanie:** krótkie notatki, bez przymiotników, podpis „T.S.”.<br>**Nie robi:** nie podnosi głosu; nie wchodzi w sentymenty; nie omawia szczegółów operacyjnych przy osobach trzecich. |

### gen. dyw. Wojciech Hałas

| Pole | Wartość |
|---|---|
| Wiek | 49 (ur. 1963) |
| Wzrost | ok. 176 cm |
| Budowa ciała | ok. 78 kg; kanciasty [P] |
| IQ | ok. 130 [P] |
| Rola | Szef Służby Wywiadu Wojskowego od 2011 [N, ZM1]; Lubliniec → GROM od 1991 → **Sarajewo 1995**: zespół GROM przy operacji Markiewicza (wskazywanie celów na Igmanie) → DWS → attaché obrony w Paryżu (2005–08) |
| Wygląd | krótko ostrzyżony, siwy na skroniach; blizna na grzbiecie lewej dłoni (lina, 1996) |
| Wiedza | ma oficjalnie (DRM) 9 zdjęć pary spod Rolexa; uzgodnił, że strona polska przekaże Szwajcarom kopię dowodu z telefonu przez attaché w Bernie; 21 I: nie wie, gdzie jest Antonina, i nie pyta |
| Motywacje | SWW ma się liczyć na równi z AW, nie być „młodszym bratem” przy KBP |
| Sekrety | lojalność wobec „starych” ponad procedurą i nowym koordynatorem |
| Stosunek platoniczny do Antoniny | **0** (zna ją z raportów) [P] |
| Stosunek romantyczny do Antoniny | **0** |
| Stan | **25 I, 17:55 (M19):** film zna w całości [N, autor]. Na SMS prostuje sklejkę WikiLeaks i nie widzi na taśmie polskiego zezwolenia na Gujanę [P]. **25 I, 17:53 (M19):** na pytanie o niebezpieczeństwo wskazuje trzy miejsca wypisane w komunikacie; reszty filmu jeszcze nikt nie pociął [P]. **25 I, 17:51 (M19):** melduje Markiewiczowi pełny film Soirée du Vingt na WikiLeaks i trzy znaczniki z komunikatu [P]. **25 I, 12:04 (M19, ZM86):** ocenia wstęp „un ancien”: próbka i spis, nie całość; godzina zgodna z notą; PRISM-u w pakiecie nie ma [P]. **25 I, 8:18 (M19):** Assange zbioru PRISM nie ma; zbiór w Warszawie, w polskich rękach; bez polskiego ruchu WikiLeaks go nie puści; materiał zostaje w służbie [P]. **25 I, 8:16 (M19):** rozdziela groźbę publikacji archiwum szkoły od ujawnienia PRISM; cel w aktach to szkoła, nie francuska sieć dowodzenia; spis milczy o DE/RU/IT [P]. **25 I, 8:14 (M19):** premierowi: przed 12:00 informacja do Paryża istniejącym kanałem; Francuzi znają zakres; treści nie czyta [P]. **25 I, 8:11 (M19, ZM85):** na pełnym składzie KBP podaje dwie kategorie pakietów Snowdena (akta operacji USA przeciw Jelskiej i szkole, bez innego państwa w aktach; PRISM i pozostałe programy) i nie czyta treści [N zakres autora; P kwestia i spis kategorii]. **25 I, 8:10 (M19, ZM84):** na forum KBP melduje, że Snowden jest w Warszawie, ubiega się o azyl i jest w polskich rękach [N autor; P kwestia]. Bez adresu i bez nazwy służby. **17 I:** zajął Sikorskiego Pekinem (temat zastępczy).<br>**8 I:** po raporcie; uważa, że ma z Markiewiczem kanał; prosi o „jedną stronę” po Genewie |
| Jak grać | krótko, raportowo; godziny i źródła, bez przymiotników. Do Markiewicza zawsze „panie generale”. |

### gen. bryg. Berdychowski

| Pole | Wartość |
|---|---|
| Wiek | ok. 55 [P] |
| Wzrost | ok. 180 cm [P] |
| Budowa ciała | ok. 82 kg [P] |
| IQ | ok. 125 [P] |
| Rola | Szef Gabinetu Szefa Sztabu Generalnego WP [N, ZM2, ZM54]; „człowiek nowego zarządu”; imię [P] do ustalenia; pseudonim **„Czarny”** [N, M10a]; dawniej przyjaciel Petelickiego „na śmierć i życie”, który w końcu się go pozbył (okoliczności [?]) |
| Wygląd | [P] ciemne włosy, surowa twarz |
| Wiedza | notuje wszystko; zanotował zdanie Markiewicza „Sapierzyński nie ma nic do tej sprawy” i zameldował Szefowi SG; teczka z wydrukami o Markiewiczu (Wykop/Twitter, @szurski_szymon) |
| Motywacje | lojalność wobec procedury i Sapierzyńskiego; ostrożny, suchy |
| Sekrety | ocena Markiewicza (17 I): „szmaciarz”, donosiciel — miejsce w ABW albo consultingu, nie w armii; dawniej pokładał w nim duże nadzieje |
| Stosunek platoniczny do Antoniny | **0** |
| Stosunek romantyczny do Antoniny | **0** |
| Stan | **21 I:** od 6:50 w gabinecie Szefa SG; teczka z wydrukami o Markiewiczu.<br>**17 I:** zanotował zdanie Markiewicza i zameldował Szefowi SG (stąd kawa 21 I).<br>**8 I:** zapisał prośbę Hałasa i zapowiedź okrojonej wersji notatki dla rządu; czwarta linijka przekreślona, ale czytelna |
| Jak grać | formalny, „do protokołu”; zwraca się wprost, żeby „potem nikt nie musiał zgadywać”. |

### gen. bryg. Jan Wysocki

| Pole | Wartość |
|---|---|
| Wiek | ok. 55 [P] |
| Wzrost | ok. 178 cm [P] |
| Budowa ciała | ok. 82 kg [P] |
| IQ | ok. 130 [P] |
| Rola | szef Zarządu Planowania Strategicznego (P5) [N, ZM3] |
| Wygląd | [P] siwiejące włosy, okulary |
| Wiedza | uważa, że Sikorski notę podpisze, bo „woli, żeby to zrobił ktoś, kogo ona słucha” |
| Motywacje | sympatyk „starej gwardii”, ale ostrożny |
| Sekrety | [?] — brak ustaleń |
| Stosunek platoniczny do Antoniny | **0** |
| Stosunek romantyczny do Antoniny | **0** |
| Stan | **8 I:** sądzi, że Sikorski notę podpisze |
| Jak grać | mówi w stronę okna, bez adresata. |

### Radosław Sikorski

| Pole | Wartość |
|---|---|
| Wiek | 49 (ur. 23 II 1963) |
| Wzrost | 186 cm |
| Budowa ciała | ok. 88 kg [P] |
| IQ | ok. 135 |
| Rola | Minister Spraw Zagranicznych i Minister-Koordynator Służb Mundurowych [N, Z56, ZM33]; **biografia [OTL + P]:** emigracja 1981, Oxford (PPE); korespondent wojenny w Afganistanie (lata 80.), Angoli; w tej linii: od 2007 w rządzie Tuska, od 2007 **Minister Spraw Zagranicznych** (jak OTL), od 2011 równocześnie **Minister-Koordynator Służb Mundurowych** — cywilny nadzór nad KBP i służbami w imieniu premiera; żona: Anne Applebaum; dworek w Chobielinie; NPC prowadzony przez asystenta MG [N, ZM5] |
| Wygląd | oxfordzka maniera; garnitur; patrzy na ludzi z góry — przy Antoninie musiałby zadzierać głowę |
| Wiedza | (1) jako koordynator **przeczytał kartę KBP/DSW/EO/93-0017** (1993) — wie o bilateralnej ewaluacji DGSE/AW, nie wie o Gujanie [P]; (2) wie, że odmowa stypendium olimpijskiego w 2007–08 wyszła ze środowisk PO — uważał ją wtedy za tchórzliwą [P]; o Rolexie nie wie; przez kanał łącznikowy KBP–DGSE może dowiedzieć się o francuskim odkryciu (Chiny) w ciągu kilku dni; **21 I:** w poniedziałek odsłuchuje nagranie rozmowy Antoniny z Markiewiczem (Z156) |
| Motywacje | błyskotliwy, ambitny, anglofil w manierach; fascynują go ludzie wyjątkowi; chce ucywilnić „państwo KBP” (nie rozbić); **pokusy:** zrobić z niej projekt polityczny; użyć jej przeciw „staremu systemowi” albo jako dowodu, że PO potrafi z nim współpracować |
| Sekrety | (3) chciałby ją kiedyś poznać osobiście — na własnych warunkach [P]; fascynacja graniczy z obsesją; wpleciony **umiarkowany podtekst seksualny** (komentarze o wzroście i sile, męskie przechwałki, dwuznaczności, ciekawość „jaka jest naprawdę”); sam nie dostrzega, że to przekracza granicę |
| Stosunek platoniczny do Antoniny | **+2** (osobista fascynacja [N]: „produkt” systemu, którego nie lubi; zainteresowanie, nie sympatia) |
| Stosunek romantyczny do Antoniny | **+1** [P] — tylko słowny podtekst i męska rywalizacja z nutą niepewności; bez dosłowności i bez przemocy (granice gry — niżej) |
| Stan | **27 I, 18:51 (M20, ZM93):** przyjmuje wersję, że oficjalnie wie o Gujanie od Markiewicza od 18:48; ma zameldować Tuskowi; pyta o zakres „szczegółów” i o Syropa [P]. **27 I, 9:20 (M20):** wrócił z Davos w sobotę wieczorem [N autor]; jest w Warszawie; pyta Markiewicza o „sprawę” i o termin rozmowy (przed KBP 18:00 czy po) [P]. **27 I, 9:12 (M20):** pyta komunikatorem rządowym: „Jak poszło z Syropem?” [N treść]. **26 I, 13:00 (M20):** zdalnie na KBP z Davos. **25 I, 8:20 (M19):** przyjmuje wejście chwilę po Markiewiczu, nie kwadrans. Wtręt „Clear” [P]. **25 I, 8:19 (M19):** zostawia Markiewiczowi pytanie do Jelskiej. Oferuje wejście kwadrans po nim. Wtręt „Point” [P]. **25 I, 8:18 (M19):** przyjmuje różnicę (Amerykanie za siebie). Pyta, czy o 20:00 zdanie brzmi: nie wydajemy, archiwum może wyjść, PRISM nie jest polską publikacją. Wtręt „Fair” [P]. **25 I, 8:16 (M19):** dwudziesta stoi; jeśli linia to „nie przeszkadzajmy”, Markiewicz ma powiedzieć to Jelskiej sam. Wtręt „Understood” [P]. **25 I, 8:14 (M19):** na forum przypomina spotkanie 20:00 w InterContinentalu (on, Markiewicz, Jelska, bez prasy) i pyta, czy stoi. Nie zdradza udawanego zaskoczenia ani zaproszenia majowego [P; termin ZM18]. Wtręt „Separately”. **25 I, 8:13 (M19):** oddaje Markiewiczowi, że nota jest wymuszeniem na obywatelce; nie oddaje tezy o końcu prestiżu ani o upadku administracji Obamy. Wtręt „Granted” [P]. **25 I, 8:11 (M19, ZM85):** na forum odcina porównanie noty do Al-Kaidy i udział Teheranu; wtręt „Ugly note” [P]. **25 I, 8:10 (M19, ZM84):** z Davos referuje na forum KBP notę USA o Snowdenie i Ramstein [N treść ultimatum; P łącze z Davos i „nad ranem”]. Wyjazd do Genewy o 16:00 i spotkanie 20:00 bez zmiany. **21 I:** Genewa 25 I bez zmian; w poniedziałek odsłuchuje nagranie rozmowy Antoniny z Markiewiczem (Z156).<br>**17 I:** o Rolexie nie wie; tweet o „spekulacjach” (11:58); bez kontaktu z ambasadorem Izraela (zalecenie Markiewicza); Genewa 25 I bez zmian.<br>**14 I:** nota SWW przeczytana 8 I; zdjęcia Antoniny z PAP na biurku; po spotkaniu z Markiewiczem (pn 14 I, 8:15, gabinet w budynku MSZ) ma imienne zaproszenie na majowe forum w kieszeni i plan pobytu Markiewicza w CH; **przyjedzie z Davos do Genewy 25 I wieczorem** (InterContinental), bez prasy i delegacji; chce zobaczyć jej twarz, gdy Markiewicz go zapowie (ZM18) |
| Jak grać | **Wizerunek:** doświadczony, błyskotliwy polityk i zarazem buc. Arogancki, z oxfordzką manierą i poczuciem wyższości. Ostry, sarkastyczny, lubi szokować i zwykle uważa się za najmądrzejszego w pokoju. Na Twitterze agresywny i złośliwy wobec przeciwników i dziennikarzy. W prywatnych rozmowach przechodzi na wulgarny, „męski” rejestr: rubaszne porównania, dosadne metafory polityczne.<br>**Kobiety:** protekcjonalny i mizoginiczny; ocenia kobiety najpierw wyglądem, potem zdolnościami; w prywatnych rozmowach seksistowskie żarty, publicznie trzyma fason.<br>**Antonina:** fascynacja graniczy z obsesją (patrz Sekrety). **Fizyczność:** Sikorski ma 186 cm i jest przyzwyczajony do patrzenia na ludzi z góry, a przy niej musi zadzierać głowę; reaguje (1) fascynacją z nutą rywalizacji („przypadek fizycznie niemożliwy” zmusza go do redefinicji kategorii); (2) męską niepewnością pokrywaną żartem („walkiria”, „amazonka”, pytania o wyciskanie, prowokacyjne mierzenie się wzrostem); (3) podtekstem w dwuznacznikach o sile, rozmiarze i „kto kogo by podniósł”. Ze zdjęć zna tylko tyle, ile pokazują.<br>**Granice gry:** podtekst wyłącznie słowny i dwuznaczny, bez dosłowności i bez przemocy lub napaści. Nie przywoływać zdarzeń OTL późniejszych niż I 2013 jako znanych postaciom.<br>**Mowa:** polszczyzna z wtrętami angielskimi. Zapożyczenie dobierać za każdym razem inne; „frankly” nie jest słowem domyślnym i nie wraca w kółko [N, autor OOC 23 X 2026]. Na forum KBP 25 I 8:10 padło „Precisely”. Krótkie, kąśliwe puenty; wobec generałów uprzejmy chłód z nutą wyższości.<br>**Pisanie:** tweety i SMS-y ostre i zaczepne; SMS-y podpisuje „RS”.<br>**Stosunek do Markiewicza:** szacunek dla legendy połączony z irytacją na „państwo w państwie”; chce mieć Markiewicza po swojej stronie i jednocześnie dowieść, że to on, cywil, rządzi. |

### płk Grzegorz Nowosad

| Pole | Wartość |
|---|---|
| Wiek | ok. 50 [P] |
| Wzrost | ok. 180 cm [P] |
| Budowa ciała | ok. 85 kg [P] |
| IQ | ok. 125 [P] |
| Rola | łącznik WP w Gabinecie Ministra-Koordynatora [N, ZM6]; b. adiutant Markiewicza; dziś przy Sikorskim, ale lojalny wobec dawnego szefa |
| Wygląd | [P] krótkie włosy, nijaka twarz |
| Wiedza | widzi dokumenty przelotnie i dopowiada resztę; pilnuje kalendarza Sikorskiego (Davos, Genewa); hasło „pogoda w Alpach się zmienia” |
| Motywacje | lojalność wobec Markiewicza; niesmak do manier Sikorskiego, ale go nie okazuje |
| Sekrety | [?] — brak ustaleń |
| Stosunek platoniczny do Antoniny | **0** |
| Stosunek romantyczny do Antoniny | **0** |
| Stan | **17 I:** przesunął wideokonferencję Sikorskiego (Mali) na 12:00; 11:46: „Minister zajęty Chinami. O Lozannie nie pytał.”.<br>**9 I:** po spotkaniu w Victorii |
| Jak grać | półsłówka przez telefon, nazw instytucji nie wymienia („ci z Miłobędzkiej”); przy kawie mówi więcej. |

### Joanna Wierzbicka

| Pole | Wartość |
|---|---|
| Wiek | ok. 55 |
| Wzrost | ok. 165 cm [P] |
| Budowa ciała | ok. 65 kg [P] |
| IQ | ok. 120 [P] |
| Rola | dyrektor sekretariatu Ministra-Koordynatora [N, ZM14]; wieloletnia, rzeczowa, odporna na żarty szefa; terminarz w skórzanej okładce; „pani Joasia” robi „najgorszą kawę w budynku, ale błyskawicznie” |
| Wygląd | [P] krótka fryzura, okulary, kostium |
| Wiedza | kalendarz Sikorskiego; przy niej padło zdanie o „dobrym guście Chińczyków” (9 I) |
| Motywacje | porządek w sekretariacie |
| Sekrety | [?] — brak ustaleń |
| Stosunek platoniczny do Antoniny | **0** |
| Stosunek romantyczny do Antoniny | **0** |
| Stan | **14 I:** wpuściła Markiewicza 8:15 |
| Jak grać | rzeczowa, odporna na żarty szefa. |

### mjr Ewa Sowińska

| Pole | Wartość |
|---|---|
| Wiek | ok. 38 [P] |
| Wzrost | ok. 168 cm [P] |
| Budowa ciała | ok. 60 kg [P] |
| IQ | ok. 135 [P] |
| Rola | Agencja Wywiadu, Zarząd IV [N, ZM19]; opiekunka sprawy „OBIEKT 93-0017” (Antonina Jelska); raporty do Markiewicza przez SKK-KBP, DW Naczelnik Zarządu IV |
| Wygląd | [P] spięte włosy, mundur, spokojne oczy |
| Wiedza | pilnuje kwarantanny operacyjnej („AW nie podejmuje działań”); AW nie wiedziała o Rolexie |
| Motywacje | rzetelny raport |
| Sekrety | jej przełożony odczytał odpowiedź Markiewicza szerzej (tylko MG) |
| Stosunek platoniczny do Antoniny | **0** |
| Stosunek romantyczny do Antoniny | **0** |
| Stan | **17 I:** raport AW/Z4/0056/13 (8:40); 15:10 część AW odpowiedzi do Sekretariatu KBP wysłana.<br>**14 I:** wysłała raport 10:08; odpowiedź Markiewicza odczytała jako „bez zmian — monitoring” |
| Jak grać | pisze urzędowo, punktowo, z oceną ryzyka; raporty z numerem AW/Z4/00NN/13. |

### gen. dyw. Michał Markiewicz

| Pole | Wartość |
|---|---|
| Wiek | ok. 40 [P] |
| Wzrost | ok. 183 cm [P] |
| Budowa ciała | ok. 85 kg [P] |
| IQ | ok. 140 [P] |
| Rola | I zastępca Szefa Sztabu Generalnego; p.o. dowódcy Wojsk Obrony Cyberprzestrzeni [N, ZM20, ZM53]; syn gen. Radosława Markiewicza; „przyszywany” członek rodziny Jelskich (Wigilia 2012) |
| Wygląd | [P] krótko ostrzyżone włosy, mundur generalski |
| Wiedza | analiza spyware (zatrzymany, próbka); odtwarzanie narzędzia z próbki — miesiące; wie, gdzie jest S4 |
| Motywacje | lojalność wobec ojca; kariera; bezpieczeństwo państwa |
| Sekrety | poza kadrem Antoniny: reakcja na wyciek adresu (Blick.ch); pyta o przedruki w PL i o Francuzów |
| Stosunek platoniczny do Antoniny | **+2** [P] — „przyszywane rodzeństwo”, szacunek |
| Stosunek romantyczny do Antoniny | **0** [P] |
| Stan | **21 I 7:00–7:01:** SMS do ojca (dosł. w M15): „Tato, dzien dobry. Skrot nocy: nic nowego na numer Swisscom. S4 miala polaczenie przez Wi-Fi w nocy…”; 8:15 w SG.<br>**18 I 8:58 (M10b):** punkty dla Ostrowskiego wysłane 7:40; Sapierzyński wie o kodzie od 8:15 („bez komentarza”); SMS do ojca o wycieku adresu (Blick.ch).<br>**17 I wiecz. (M10a):** 21:00–21:30 u ojca: wynik analizy; punkty dla Ostrowskiego do 8:00; ostrzega Hałasa; pt rano mówi Sapierzyńskiemu o planie.<br>**17 I:** ok. 9:30 meldunek: atak na numer Swisscom zablokowany przez ochronę S4; od 17 I melduje też Sapierzyńskiemu.<br>**14 I:** ok. 10:50 na polecenie ojca uruchomił ograniczenie zasięgu treści o Antoninie; 12:00 meldunek |
| Jak grać | **Pisanie:** w wiadomościach pisanych **nie używa polskich znaków**; do ojca „Tato”; meldunki w SKK-KBP podpisuje „M.M.”. |

### gen. broni pil. Andrzej Błasik

| Pole | Wartość |
|---|---|
| Wiek | ok. 50 [P] |
| Wzrost | ok. 178 cm [P] |
| Budowa ciała | ok. 80 kg [P] |
| IQ | ok. 125 [P] |
| Rola | dowódca Wojsk Powietrzno-Kosmicznych (test 14 I, sesja M03a) [N, ZM24] |
| Wygląd | [P] pilot, siwiejące wąsy |
| Wiedza | przed testem niepewny co do WR-2000 („nie ma dowodu, że nie działa”) |
| Motywacje | sukces testu |
| Sekrety | [?] — brak ustaleń |
| Stosunek platoniczny do Antoniny | **0** |
| Stosunek romantyczny do Antoniny | **0** |
| Stan | **14 I:** uczestnik testu |
| Jak grać | — |

### gen. bryg. Stefan Mordacz

| Pole | Wartość |
|---|---|
| Wiek | ok. 50 [P] |
| Wzrost | ok. 178 cm [P] |
| Budowa ciała | ok. 80 kg [P] |
| IQ | ok. 125 [P] |
| Rola | dowódca WOPLiPR; przyjaciel Michała Markiewicza (test 14 I) [N, ZM24] |
| Wygląd | [P] okulary, krótkie włosy |
| Wiedza | świadek niesubordynacji |
| Motywacje | bezpieczeństwo systemu |
| Sekrety | [?] — brak ustaleń |
| Stosunek platoniczny do Antoniny | **0** |
| Stosunek romantyczny do Antoniny | **0** |
| Stan | **14 I:** przerażony samowolnym odpaleniem |
| Jak grać | — |

### gen. broni Edward Gruszka

| Pole | Wartość |
|---|---|
| Wiek | ok. 55 [P] |
| Wzrost | ok. 180 cm [P] |
| Budowa ciała | ok. 85 kg [P] |
| IQ | ok. 125 [P] |
| Rola | Dowódca Operacyjny SZ RP (ZM53); uczestnik testu w Nowej Dębie |
| Wygląd | [P] krótkie siwe włosy |
| Wiedza | test WR-2000 |
| Motywacje | [?] |
| Sekrety | [?] — brak ustaleń |
| Stosunek platoniczny do Antoniny | **0** |
| Stosunek romantyczny do Antoniny | **0** |
| Stan | — |
| Jak grać | — |

### kpt. Władysław Maciejewski

| Pole | Wartość |
|---|---|
| Wiek | ok. 35 [P] |
| Wzrost | ok. 178 cm [P] |
| Budowa ciała | ok. 78 kg [P] |
| IQ | ok. 115 [P] |
| Rola | dowódca baterii WR-2000 (test 14 I) |
| Wygląd | [P] młody, w mundurze |
| Wiedza | bateria WR-2000 |
| Motywacje | sprawna obsługa |
| Sekrety | [?] — brak ustaleń |
| Stosunek platoniczny do Antoniny | **0** |
| Stosunek romantyczny do Antoniny | **0** |
| Stan | — |
| Jak grać | — |

### kpt. Marian Wanat

| Pole | Wartość |
|---|---|
| Wiek | ok. 33 [P] |
| Wzrost | ok. 178 cm [P] |
| Budowa ciała | ok. 76 kg [P] |
| IQ | ok. 115 [P] |
| Rola | operator PZRD Wisła, Lębork (test 14 I) |
| Wygląd | [P] młody, w mundurze |
| Wiedza | próbował powstrzymać przedwczesny strzał |
| Motywacje | bezpieczeństwo |
| Sekrety | [?] — brak ustaleń |
| Stosunek platoniczny do Antoniny | **0** |
| Stosunek romantyczny do Antoniny | **0** |
| Stan | **14 I:** próbował powstrzymać przedwczesny strzał |
| Jak grać | — |

### mjr ŻW Arkadiusz Góralski

| Pole | Wartość |
|---|---|
| Wiek | ok. 40 [P] |
| Wzrost | ok. 178 cm [P] |
| Budowa ciała | ok. 82 kg [P] |
| IQ | ok. 115 [P] |
| Rola | posterunek w Grabowie; poszukiwanie odłamków (test 14 I) |
| Wygląd | [P] mundur Żandarmerii Wojskowej |
| Wiedza | poszukiwanie odłamków |
| Motywacje | [?] |
| Sekrety | [?] — brak ustaleń |
| Stosunek platoniczny do Antoniny | **0** |
| Stosunek romantyczny do Antoniny | **0** |
| Stan | — |
| Jak grać | — |

### Paweł Wróblewski

| Pole | Wartość |
|---|---|
| Wiek | ok. 35 |
| Wzrost | ok. 180 cm [P] |
| Budowa ciała | ok. 78 kg [P] |
| IQ | ok. 120 [P] |
| Rola | dziennikarz „Faktu” [N, ZM42]; pracuje z fotoreporterem Łukaszem [P] |
| Wygląd | granatowa kurtka z kapturem, dyktafon |
| Wiedza | odwiedził Markiewicza (15 I, 21:30); tekst o Antoninie do druku 23:00, online ok. 6:00; konto @Pawel_Fakt24 — 15 I prosił Antoninę o komentarz: Twitter, mail EPFL (10:58), Wykop |
| Motywacje | tekst, nie odpuszcza |
| Sekrety | [?] — brak ustaleń |
| Stosunek platoniczny do Antoniny | **0** |
| Stosunek romantyczny do Antoniny | **0** |
| Stan | **15 I:** po wizycie u Markiewicza; tekst o Antoninie |
| Jak grać | uprzejmy, ale nie odpuszcza. |

### gen. Radosław Markiewicz

*Karta tła. **Od sesji 5 (8 I 2013) odgrywany przez innego gracza-człowieka** [N]; MG prowadzi tylko tło jego scen (Z60). Konto @radmar52 na Wykopie jest publiczne i powszechnie znane [N, ZM26]; 15 I 2013, 9:45 Antonina zawołała go pod swoim AMA („Pozdrawiam @radmar52”); odpowiedź (lub brak) — decyzja gracza.*

| Pole | Wartość |
|---|---|
| Wiek | **60** (ur. **1952**) [N, Z60] — w 1991 jako 39-latek wyjątkowo młody Szef Sztabu |
| Wzrost | ? |
| Budowa ciała | ? |
| IQ | ok. 145 |
| Rola | Szef Sztabu Generalnego WP; **z funkcji Szefa SG odszedł w VIII 2012** [N]; **[KOREKTA autora, 26 X 2026, ZM90]: generał czterogwiazdkowy (generał armii), NIE jest w stanie spoczynku**; następca: gen. Tadeusz Sapierzyński („Tadek”). Dziś kontraktowy pracownik MON/WP (ZM16), nieformalny mentor; bywa ekspertem telewizyjnym (TVN24, programy o Chinach i Libii, 3–4 I 2013) [G]; **wdowiec** — żona (matka Michała) nie żyje [N, autor 12 X 2026] |
| Wygląd | ? (gracz Markiewicza) |
| Wiedza | **25 I, 8:11, M19 (ZM85):** słyszy dwie kategorie pakietów Snowdena. Nie słyszy treści ani kryptonimu STEEPLE. **25 I, 8:10, M19 (ZM84):** na forum KBP słyszy notę USA (Snowden do Ramstein do 12:00, bez procesu, inaczej publikacja o Jelskiej i École Polytechnique) oraz że Snowden jest w Warszawie i ubiega się o azyl [N fakt autora; P kwestie Tuska, Sikorskiego i Hałasa]. **25 I, M19 (Z265/Z267):** zna od Antoniny Gujanę: walkę i dwóch zabitych przeciwników, odrębny wypadek z chlorem z dwiema ofiarami, Castagneta, Cayenne/Percy, łańcuch DGSE–AW–SGDN/Syrop, informację od de Villiersa 15 I oraz podpisanie zobowiązania do tajemnicy. „jedyny prawdziwy przyjaciel”; traktuje ją jak równą od 5. urodzin [K, G] |
| Motywacje | lojalność wobec Antoniny; „stara gwardia” |
| Sekrety | w wątku M |
| Stosunek platoniczny do Antoniny | **+5** („jedyny prawdziwy przyjaciel”) |
| Stosunek romantyczny do Antoniny | **0** (ojcowski mentor) |
| Stan | **25 I, 17:55 CET — M19:** ma pomysł na kozła ofiarnego po polskiej stronie, bez nazwiska; traktuje to jako ostateczność. **25 I, 17:53 CET — M19:** pyta Hałasa, czy na ten moment jest coś niebezpiecznego. **25 I, 17:51 CET — M19:** dostaje od Hałasa meldunek o filmie Soirée du Vingt na WikiLeaks. Nadal w InterContinentalu; luka od 12:04 nieodegrana. **25 I, 12:02 CET — M19 (ZM86):** po rozłączeniu o 8:20, w InterContinentalu, pyta Hałasa: „Ocena własna?” Wstęp serii jest już w sieci. **25 I, 8:20 CET — M19:** najpierw swoją działkę; Sikorski wchodzi chwilę po nim. Pyta, czy na ten moment jasne. **25 I, 8:19 CET — M19:** na forum: najpierw zapyta Jelską, czego oczekuje od niego i od Polski. **25 I, 8:18 CET — M19:** nie uginać się przed groźbą; publikację PRISM zostawia WikiLeaks i Assange’owi; prosi o warianty i o powrót składu po rozmowie z Jelską. **25 I, 8:16 CET — M19:** potwierdza gotowość w hotelu na 20:00. Rekomenduje nie przeszkadzać: PRISM i wyciek mają skompromitować USA same. **25 I, 8:14 CET — M19:** słyszy cztery odpowiedzi na pytanie Tuska i pytanie Sikorskiego, czy 20:00 w InterContinentalu stoi. Jeszcze nie odpowiada. **25 I, 8:13 CET — M19:** na forum nazywa notę mafijnym wymuszeniem na obywatelce i stawia tezę o prestiżu oraz o upadku administracji Obamy po upublicznieniu groźby. **25 I, 8:11 CET — M19 (ZM85):** na forum odmawia negocjacji, porównuje notę do metod Al-Kaidy i pyta o dodatkowe pakiety Snowdena. Laptop otwarty, zapis nieznany. **25 I, 8:10 CET — M19 (ZM84):** Hotel InterContinental, Genewa, na forum KBP. Przejazd z dworca i rozstanie z Antoniną nieodegrane. Słyszy ultimatum USA do 12:00 i że Snowden jest w Warszawie (azyl). InterContinental 20:00 aktualny. **25 I, 6:50 CET — M19:** po rozmowie w Savigny i wspólnej taksówce z Antoniną, przy Gare de Lausanne; ma własny telefon, przeglądał Davos. Postój bez incydentu. Pociąg 6:54 do Genewy planowany, przejazd nieodegrany. Zapowiedział rozmowę z Syropem w Warszawie; Krzysztof chce być przy niej, zgoda i termin nieustalone. InterContinental 20:00 aktualny. **21 I:** 18–20 I: rozmowy w Warszawie i wyjazd do Gdyni (M11–M12, Marynarka Wojenna); nd 20 I wieczorem powrót do Warszawy, telewizja („Szkło Kontaktowe”, TVP Info, M13); **noc 20/21 I (0:05 CET = 13:35 lok.): rozmowa z Antoniną na S4** (odradza banię z rosyjskimi oficerami GRU; „Może i się wybiorę” na atol); **pn 21 I 8:30–8:55: spotkanie z gen. Sapierzyńskim (M15)** w kawiarni przy Mokotowskiej; jedzie na Sztab Generalny do gen. Hałasa i gen. Puchały.<br>**8 I:** rozmowa telefoniczna z Antoniną (od 9:58) — zrealizowany termin „telefon do 31 I”; nowy iPhone 5; jedzie tramwajem na Rakowiecką; zapowiada służbowy wyjazd do **Oerlikonu** |
| Jak grać | **Nie odgrywać przez MG (Z60).** Jego kwestie wkleja autor; MG tylko osadza je w kadrze. |

### insp. Tadeusz Syrop

*Źródło nadrzędne: `Technocracy/tadeusz-syrop.md` (stan na 1991). Poniżej stan na I 2013.*

| Pole | Wartość |
|---|---|
| Wiek | 59 (ur. 16 X 1953) |
| Wzrost | 179 cm |
| Budowa ciała | ok. 76 kg — suchy, żylasty; wygląda na ponad 65 lat (Synaj, SB, czterogodzinny sen od 1975) |
| IQ | ok. 150 |
| Rola | b. Szef AW, architekt „planu długiego” [K, Z55]; Stare Kiejkuty → AWO 1974–81 (UNEF II, Synaj, arabski) → „Kurs Specjalny Paryż”: **przewerbowany przez SDECE/DGSE, podwójny agent od lat 70.** → SB Dep. I 1981–90 → lustracja 1990 (czysty) → Szef UOP VII 1991 → p.o. Szefa ABW 1991–92 → **Szef Agencji Wywiadu** (członek KBP) [K]; [P] na emeryturze od **2005**; formalnie bez funkcji, nieformalnie doradca Technokracji i stały kanał do DGSE; dom nad jeziorem w Mazurach (okolice Szczytna) i mieszkanie na Saskiej Kępie; kilka razy w roku Paryż |
| Wygląd | siwe, krótko ostrzyżone włosy, siwy kilkudniowy zarost; jasne, szaroniebieskie oczy „wyceniające”; ciemne marynarki bez krawata; skórzany notes w wewnętrznej kieszeni (prywatny szyfr: polski, rosyjski, francuski) [K] |
| Wiedza | języki: polski, rosyjski C2, francuski C2, angielski C2, niemiecki B2, arabski B2 [K]; zna Antoninę od niemowlęctwa; na 5. urodziny dał komplet kreślarski Staedtler Mars („Każdy plan zaczyna się od linii.”) [K]; zatwierdził kartę KBP/DSW/EO/93-0017 (1993) [K]; **zaproponował l'X i ułożył przebieg jej studiów; Krzysztof to zaaprobował** [N, Z55]; wie o odkryciu francuskim z 8 I wcześniej niż Antonina |
| Motywacje | silna, profesjonalna Polska i „zbieżność” interesów Polski i Technokracji; Antonina jako dzieło życia — dowód, że plan długoterminowy działa. **Pokusy:** traktować ludzi jak parametry operacji; uważać, że cel uświęca ryzyko, „jeśli człowiek jest wystarczająco silny”. **Relacja z Krzysztofem:** lojalność, nie przyjaźń; szacunek dla architekta, cicha myśl, że Krzysztof nie docenia, ile kompromisów kosztuje zmiana instytucji od środka [K]. **Stosunek do Markiewicza:** szacunek zawodowy, zasadnicza różnica filozofii: Markiewicz uczył ją jak równą, Syrop kształtuje ją jak projekt; wie, że Markiewicz by go za Gujanę nie wybaczył |
| Sekrety | (1) **podwójna lojalność wobec DGSE od lat 70.** — znana tylko wąskiemu kręgowi Technokracji [K]; (2) **polski architekt „planu długiego” DGSE/AW** wobec Antoniny, sprzecznego z zasadami Cocteau i z wytycznymi karty z 1993, którą sam podpisał [N, Z55]; (3) **znał i zaakceptował ryzyko Gujany** (2007–08), Krzysztofowi przedstawił l'X wyłącznie jako ścieżkę naukową [P]; (4) [P] co roku dostaje od DGSE nieoficjalną notę o „postępach” — ostatnia z XII 2012 wspomina o „zainteresowaniu strony trzeciej” (Chiny) |
| Stosunek platoniczny do Antoniny | **+4** — duma twórcy i autentyczna, chłodna troska; uważa, że to, co zrobił, było „dla jej dobra i dobra Polski”; Antonina widzi w nim [P] życzliwego, małomównego „wujka z ministerstwa” |
| Stosunek romantyczny do Antoniny | **0** |
| Stan | **26 I, 7:03 (M20):** w kuchni w Aninie wobec Krzysztofa i Markiewicza przyznaje gotowość na śmierć Antoniny i świadome przemilczenie wobec ojca; nie przeprasza; pyta o prawdziwy cel wizyty [P]. **26 I, 6:58 (M20):** mieszka w Aninie (podwarszawskim) [N]; od siódmej pod domem czekają Markiewicz i Krzysztof, Syrop jeszcze nie wie. **8 I 2013:** Mazury; po telefonie z Paryża (DGSE) wie o odkryciu francuskim z 8 I; nie zadzwoni do niej sam. Jeśli Antonina się z nim skontaktuje — odbierze po drugim sygnale |
| Jak grać | operator, nie architekt; najkompetentniejszy w większości pomieszczeń; nie zgłasza się z informacją sam; precyzyjny; nie pije (trzyma kieliszek, nie kończy); bezruch jako dyscyplina [K]. |

---

### mjr Rutko (KBP)

| Pole | Wartość |
|---|---|
| Wiek | ok. 36 [P] |
| Wzrost | ok. 180 cm [P] |
| Budowa ciała | szczupła, wysportowana [P] |
| IQ | ok. 120 [P] |
| Rola | **oficer SKW** [N, autor 22 X 2026] w Sekretariacie KBP (kontradm. Ostrowski); przekazuje meldunki generałowi; imię [?] |
| Wygląd | [P] mundur, krótkie włosy; w telefonie: równy, zdystansowany głos |
| Wiedza | 23 I 0:32: atak na École polytechnique — zakres wycieku i wektor (absolwent l'X, AX/X-Israël, pierwsza ofiara) wg strony francuskiej; bez szczegółów o 2008 r. |
| Motywacje | wykonać polecenie, meldować rzeczowo, nie wchodzić w ocenę |
| Sekrety | brak [P] |
| Stosunek platoniczny do Antoniny | **0** (zna ją z teczek) |
| Stosunek romantyczny do Antoniny | **0** |
| Stan | **23 I ok. 14:10 (M17):** obejrzał całe nagranie Soirée du Vingt; długa analiza dla Markiewicza (szacunek dla Jelskiej, obawa o jej metodę obrony wobec mediów).<br>**23 I 8:19–8:55:** lektura z serwera KBP, „osobiście i służbowo przerażony”; zbiera opinie dowódców.<br>**23 I 0:32 (M17):** meldunek telefoniczny do Markiewicza |
| Jak grać | formalny, suchy, mówi jak z kartki: fakty, potem wnioski strony francuskiej, potem pytanie o dyspozycje; „panie generale”; nie komentuje, nie zgaduje, nie pisze skrótów służb w SMS-ach [P] |

## I. Internet — stali NPC sieciowi

*Konta anonimowe: cechy fizyczne i IQ nieznane („?”); pełne wypowiedzi: `12-archiwum-internetu.md`. Aliasy: @Pawel_Fakt24 = Paweł Wróblewski (§H); @TomaszGrabowski1983 = Tomasz G.; @szurski_szymon = Szymon K.; @Lena_H_official = Lena Hoffmeister (§J).*

### Szymon K. (@szurski_szymon)

| Pole | Wartość |
|---|---|
| Wiek | 41 |
| Wzrost | ? |
| Budowa ciała | ? |
| IQ | ? |
| Rola | 41, Radom, technik IT na rencie; „szur”, klon Jadwigi; odkopał taśmę (15 I, 11:52); stały użytkownik Wykopu |
| Wygląd | ? |
| Wiedza | taśma 1992; teorie spiskowe |
| Motywacje | „odkrywanie prawdy”, uwaga |
| Sekrety | ? |
| Stosunek platoniczny do Antoniny | **−1** [P] |
| Stosunek romantyczny do Antoniny | **0** |
| Stan | **15 I:** odkopał taśmę (11:52); 16 I 21:36–21:51 @radmar52 odpowiada mu („Ja się nie znam”); 21 I 7:48: „czyli WP ma kontyngent tam gdzie ona. a ona jest na wakacjach. przypadek? nic nie łączę 🙂” — wątek Markiewicza (teczka u Berdychowskiego) |
| Jak grać | szur z internetu; pisze z wielokropkami i „🙂” |

### Tomasz G. (@TomaszGrabowski1983)

| Pole | Wartość |
|---|---|
| Wiek | 29 |
| Wzrost | ? |
| Budowa ciała | ? |
| IQ | ? |
| Rola | 29, Rzeszów, księgowy; krytyk KBP; ojciec zatrzymany przez KBP w sprawie Srebrnej (1992); znalezisko #cenzura |
| Wygląd | ? |
| Wiedza | ? |
| Motywacje | rachunek krzywd z 1992 |
| Sekrety | ? |
| Stosunek platoniczny do Antoniny | **−1** → 0 [P] |
| Stosunek romantyczny do Antoniny | **0** |
| Stan | zmiękł wobec Antoniny po AMA [P] |
| Jak grać | ? |

### @PolakwLozannie

| Pole | Wartość |
|---|---|
| Wiek | ? |
| Wzrost | ? (anonimowy) |
| Budowa ciała | ? (anonimowy) |
| IQ | ? |
| Rola | Polak w Lozannie, Twitter po francusku (~900 obs.) |
| Wygląd | ? (anonimowy) |
| Wiedza | ? |
| Motywacje | ? |
| Sekrety | ? |
| Stosunek platoniczny do Antoniny | **0** |
| Stosunek romantyczny do Antoniny | **0** |
| Stan | przetłumaczył żart o Sexion d'Assaut na francuski (11:09, 43 RT) |
| Jak grać | ? |

### @m4tematyk_z_PW

| Pole | Wartość |
|---|---|
| Wiek | ? |
| Wzrost | ? (anonimowy) |
| Budowa ciała | ? (anonimowy) |
| IQ | ? |
| Rola | stały użytkownik Wykopu: sceptyk merytoryczny |
| Wygląd | ? (anonimowy) |
| Wiedza | ? |
| Motywacje | ? |
| Sekrety | ? |
| Stosunek platoniczny do Antoniny | **0** |
| Stosunek romantyczny do Antoniny | **0** |
| Stan | 21 I 8:20: „sprawa dla żandarmerii, nie dla was” |
| Jak grać | ? |

### @mirabelka_92 🟣

| Pole | Wartość |
|---|---|
| Wiek | ? |
| Wzrost | ? (anonimowy) |
| Budowa ciała | ? (anonimowy) |
| IQ | ? |
| Rola | stały użytkownik Wykopu: obrończyni Antoniny |
| Wygląd | ? (anonimowy) |
| Wiedza | ? |
| Motywacje | ? |
| Sekrety | ? |
| Stosunek platoniczny do Antoniny | **+2** [P] |
| Stosunek romantyczny do Antoniny | **0** |
| Stan | — |
| Jak grać | ? |

### @Kopacz_Danych

| Pole | Wartość |
|---|---|
| Wiek | ? |
| Wzrost | ? (anonimowy) |
| Budowa ciała | ? (anonimowy) |
| IQ | ? |
| Rola | stały użytkownik Wykopu: doxxer |
| Wygląd | ? (anonimowy) |
| Wiedza | ? |
| Motywacje | ? |
| Sekrety | ? |
| Stosunek platoniczny do Antoniny | **−1** [P] |
| Stosunek romantyczny do Antoniny | **0** |
| Stan | 21 I 8:05: „to nie jest hotel, to jest baza” |
| Jak grać | ? |

### @Szwajcarski_Banan

| Pole | Wartość |
|---|---|
| Wiek | ? |
| Wzrost | ? (anonimowy) |
| Budowa ciała | ? (anonimowy) |
| IQ | ? |
| Rola | stały użytkownik Wykopu: OP, Polak z EPFL |
| Wygląd | ? (anonimowy) |
| Wiedza | kampus EPFL |
| Motywacje | ? |
| Sekrety | ? |
| Stosunek platoniczny do Antoniny | **0** |
| Stosunek romantyczny do Antoniny | **0** |
| Stan | 5:10: „z kampusu EPFL: wszyscy już widzieli. biedny Basile.” |
| Jak grać | ? |

### @Patriota_z_Radomia

| Pole | Wartość |
|---|---|
| Wiek | ? |
| Wzrost | ? (anonimowy) |
| Budowa ciała | ? (anonimowy) |
| IQ | ? |
| Rola | stały użytkownik Wykopu (#krolowatosia) |
| Wygląd | ? (anonimowy) |
| Wiedza | ? |
| Motywacje | ? |
| Sekrety | ? |
| Stosunek platoniczny do Antoniny | **0** |
| Stosunek romantyczny do Antoniny | **+1** [P] |
| Stan | — |
| Jak grać | ? |

### @Ziemniaczany_Rycerz

| Pole | Wartość |
|---|---|
| Wiek | ? |
| Wzrost | ? (anonimowy) |
| Budowa ciała | ? (anonimowy) |
| IQ | ? |
| Rola | stały użytkownik Wykopu |
| Wygląd | ? (anonimowy) |
| Wiedza | ? |
| Motywacje | ? |
| Sekrety | ? |
| Stosunek platoniczny do Antoniny | **0** |
| Stosunek romantyczny do Antoniny | **0** |
| Stan | 21 I 9:02: „ten kumpel z misji właśnie skończył karierę” |
| Jak grać | ? |

### @NieJestemBotem_PL

| Pole | Wartość |
|---|---|
| Wiek | ? |
| Wzrost | ? (anonimowy) |
| Budowa ciała | ? (anonimowy) |
| IQ | ? |
| Rola | stały użytkownik Wykopu |
| Wygląd | ? (anonimowy) |
| Wiedza | ? |
| Motywacje | ? |
| Sekrety | ? |
| Stosunek platoniczny do Antoniny | **0** |
| Stosunek romantyczny do Antoniny | **0** |
| Stan | 11:00: „ranking tygodnia”; 21 I 8:40: „córka premiera na wakacjach w bazie WP za pieniądze podatnika” |
| Jak grać | ? |

### @Polonista_na_bezrobociu

| Pole | Wartość |
|---|---|
| Wiek | ? |
| Wzrost | ? (anonimowy) |
| Budowa ciała | ? (anonimowy) |
| IQ | ? |
| Rola | stały użytkownik Wykopu |
| Wygląd | ? (anonimowy) |
| Wiedza | ? |
| Motywacje | ? |
| Sekrety | ? |
| Stosunek platoniczny do Antoniny | **0** |
| Stosunek romantyczny do Antoniny | **0** |
| Stan | — |
| Jak grać | ? |

### @Weteran_KBP_bez_teczki

| Pole | Wartość |
|---|---|
| Wiek | ? |
| Wzrost | ? (anonimowy) |
| Budowa ciała | ? (anonimowy) |
| IQ | ? |
| Rola | stały użytkownik Wykopu: 15 Brygada, Niemenczyn 1992; weteran |
| Wygląd | ? (anonimowy) |
| Wiedza | KBP z 1992 z drugiej ręki |
| Motywacje | ? |
| Sekrety | ? |
| Stosunek platoniczny do Antoniny | **0** |
| Stosunek romantyczny do Antoniny | **0** |
| Stan | — |
| Jak grać | ? |

### @Węgier_w_Krakowie

| Pole | Wartość |
|---|---|
| Wiek | ? |
| Wzrost | ? (anonimowy) |
| Budowa ciała | ? (anonimowy) |
| IQ | ? |
| Rola | stały użytkownik Wykopu |
| Wygląd | ? (anonimowy) |
| Wiedza | ? |
| Motywacje | ? |
| Sekrety | ? |
| Stosunek platoniczny do Antoniny | **0** |
| Stosunek romantyczny do Antoniny | **0** |
| Stan | — |
| Jak grać | ? |

### @Ateista_z_Torunia

| Pole | Wartość |
|---|---|
| Wiek | ? |
| Wzrost | ? (anonimowy) |
| Budowa ciała | ? (anonimowy) |
| IQ | ? |
| Rola | stały użytkownik Wykopu |
| Wygląd | ? (anonimowy) |
| Wiedza | ? |
| Motywacje | ? |
| Sekrety | ? |
| Stosunek platoniczny do Antoniny | **0** |
| Stosunek romantyczny do Antoniny | **0** |
| Stan | — |
| Jak grać | ? |

### @wysoka_jak_tata 🟣

| Pole | Wartość |
|---|---|
| Wiek | ? |
| Wzrost | ? (anonimowy) |
| Budowa ciała | ? (anonimowy) |
| IQ | ? |
| Rola | stały użytkownik Wykopu |
| Wygląd | ? (anonimowy) |
| Wiedza | ? |
| Motywacje | ? |
| Sekrety | ? |
| Stosunek platoniczny do Antoniny | **+1** [P] |
| Stosunek romantyczny do Antoniny | **0** |
| Stan | — |
| Jak grać | ? |

### @Grazyna_z_korpo 🟣

| Pole | Wartość |
|---|---|
| Wiek | ? |
| Wzrost | ? (anonimowy) |
| Budowa ciała | ? (anonimowy) |
| IQ | ? |
| Rola | stały użytkownik Wykopu |
| Wygląd | ? (anonimowy) |
| Wiedza | ? |
| Motywacje | ? |
| Sekrety | ? |
| Stosunek platoniczny do Antoniny | **0** |
| Stosunek romantyczny do Antoniny | **0** |
| Stan | 10:10: „kobieta ma życie jak serial” |
| Jak grać | ? |

### @Ahmed_z_Wrocławia

| Pole | Wartość |
|---|---|
| Wiek | ? |
| Wzrost | ? (anonimowy) |
| Budowa ciała | ? (anonimowy) |
| IQ | ? |
| Rola | stały użytkownik Wykopu |
| Wygląd | ? (anonimowy) |
| Wiedza | ? |
| Motywacje | ? |
| Sekrety | ? |
| Stosunek platoniczny do Antoniny | **0** |
| Stosunek romantyczny do Antoniny | **0** |
| Stan | — |
| Jak grać | ? |

### u/ArchivesDePalaiseau

| Pole | Wartość |
|---|---|
| Wiek | ? |
| Wzrost | ? (anonimowy) |
| Budowa ciała | ? (anonimowy) |
| IQ | ? |
| Rola | anonimowy Francuz (Reddit r/france), „archiwista”; analityk danych [P], nie z l'X; wykopał zdjęcia A i B |
| Wygląd | ? (anonimowy) |
| Wiedza | zdjęcia z 2008–09 |
| Motywacje | ? |
| Sekrety | ? |
| Stosunek platoniczny do Antoniny | **0** |
| Stosunek romantyczny do Antoniny | **0** |
| Stan | wiral 18/19 I; znany tylko z loginu; może wykopać „France-Guyane” (21 I) |
| Jak grać | ? |

### u/Brandt_ex3REI

| Pole | Wartość |
|---|---|
| Wiek | ? |
| Wzrost | ? (anonimowy) |
| Budowa ciała | ? (anonimowy) |
| IQ | ? |
| Rola | były podoficer 3e REI (Kourou 2005–2010) [P]; „nie potwierdzam, ale…” |
| Wygląd | ? (anonimowy) |
| Wiedza | wie, że „la stagiaire du module spécial” istniała; nie był w Jaubert |
| Motywacje | ? |
| Sekrety | milczy; jedno zdanie w grupie FB |
| Stosunek platoniczny do Antoniny | **0** |
| Stosunek romantyczny do Antoniny | **0** |
| Stan | może napisać do niej list (24 I) |
| Jak grać | ? |

### @Ancien_de_la_DRM

| Pole | Wartość |
|---|---|
| Wiek | ? |
| Wzrost | ? (anonimowy) |
| Budowa ciała | ? (anonimowy) |
| IQ | ? |
| Rola | anonimowy „były DRM” na Twitterze FR [P]; „na agrafach się nie pyta” |
| Wygląd | ? (anonimowy) |
| Wiedza | przypadkowy głos, bez wiedzy |
| Motywacje | ? |
| Sekrety | ? |
| Stosunek platoniczny do Antoniny | **0** |
| Stosunek romantyczny do Antoniny | **0** |
| Stan | — |
| Jak grać | ? |

### Jacques Delorme (Studio Delorme)

| Pole | Wartość |
|---|---|
| Wiek | ? |
| Wzrost | ? (anonimowy) |
| Budowa ciała | ? (anonimowy) |
| IQ | ? |
| Rola | fotograf balu 2009 (fikcyjny); studio zamknięte 2011; galeria w cache wyszukiwarki — źródło zdjęcia B |
| Wygląd | ? |
| Wiedza | nigdy nie autoryzował rozpowszechniania zdjęć |
| Motywacje | ? |
| Sekrety | ? |
| Stosunek platoniczny do Antoniny | **0** |
| Stosunek romantyczny do Antoniny | **0** |
| Stan | „Le Parisien” 19 I 13:10: nigdy nie autoryzował rozpowszechniania zdjęć; strona zamknięta, cache nadal dostępny |
| Jak grać | ? |

### u/Polytechnicien_anon

| Pole | Wartość |
|---|---|
| Wiek | ? |
| Wzrost | ? (anonimowy) |
| Budowa ciała | ? (anonimowy) |
| IQ | ? |
| Rola | anonimowy X2005 (Reddit r/france) [P]; wrzucił zdjęcie C („4 na 21”) |
| Wygląd | ? (anonimowy) |
| Wiedza | reguły FHM |
| Motywacje | ? |
| Sekrety | ? |
| Stosunek platoniczny do Antoniny | **0** |
| Stosunek romantyczny do Antoniny | **0** |
| Stan | — |
| Jak grać | rzeczowy, ironiczny |

### u/Ancien_X2006_off

| Pole | Wartość |
|---|---|
| Wiek | ? |
| Wzrost | ? (anonimowy) |
| Budowa ciała | ? (anonimowy) |
| IQ | ? |
| Rola | anonimowy X2006 [P]; FHM w pułku piechoty morskiej 2006–07 |
| Wygląd | ? (anonimowy) |
| Wiedza | jego medal po 8 miesiącach (porównanie z 2008) |
| Motywacje | ? |
| Sekrety | ? |
| Stosunek platoniczny do Antoniny | **0** |
| Stosunek romantyczny do Antoniny | **0** |
| Stan | — |
| Jak grać | ? |

### u/Dr_Pierre_Marne

| Pole | Wartość |
|---|---|
| Wiek | ? |
| Wzrost | ? (anonimowy) |
| Budowa ciała | ? (anonimowy) |
| IQ | ? |
| Rola | Francuz, „logiczny”, często wygrywa spory [P] |
| Wygląd | ? (anonimowy) |
| Wiedza | ? |
| Motywacje | ? |
| Sekrety | ? |
| Stosunek platoniczny do Antoniny | **0** |
| Stosunek romantyczny do Antoniny | **0** |
| Stan | „gdyby była na Harpie, byłaby inna dekoracja” |
| Jak grać | ? |

### @Reserwista_Marek

| Pole | Wartość |
|---|---|
| Wiek | 52 |
| Wzrost | ? (anonimowy) |
| Budowa ciała | ? (anonimowy) |
| IQ | ? |
| Rola | kpt rez., 52 l., 18 lat w WP [P] |
| Wygląd | ? (anonimowy) |
| Wiedza | ? |
| Motywacje | ? |
| Sekrety | ? |
| Stosunek platoniczny do Antoniny | **0** |
| Stosunek romantyczny do Antoniny | **0** |
| Stan | pierwszy głos prostujący „legionistkę” (Wykop 3:30, 19 I) |
| Jak grać | rzeczowy, zmęczony |

### u/Mangrove_Kourou

| Pole | Wartość |
|---|---|
| Wiek | ? |
| Wzrost | ? (anonimowy) |
| Budowa ciała | ? (anonimowy) |
| IQ | ? |
| Rola | Francuz, zna Gujanę i 3e REI z drugiej ręki [P] |
| Wygląd | ? (anonimowy) |
| Wiedza | ? |
| Motywacje | ? |
| Sekrety | ? |
| Stosunek platoniczny do Antoniny | **0** |
| Stosunek romantyczny do Antoniny | **0** |
| Stan | 19 I 0:53: „Légion w Gujanie to przede wszystkim Harpie”; po zdjęciu C „obniża poziom”; nie wie nic konkretnego |
| Jak grać | ? |

### u/hugues_de_X2003

| Pole | Wartość |
|---|---|
| Wiek | ? |
| Wzrost | ? (anonimowy) |
| Budowa ciała | ? (anonimowy) |
| IQ | ? |
| Rola | polytechnicien X2003 (flair) [P] |
| Wygląd | ? (anonimowy) |
| Wiedza | ? |
| Motywacje | ? |
| Sekrety | ? |
| Stosunek platoniczny do Antoniny | **0** |
| Stosunek romantyczny do Antoniny | **0** |
| Stan | tradycja „major niesie sztandar” (r/france 2:02, 19 I) |
| Jak grać | ? |

### @Kevin_Legion_2eREG

| Pole | Wartość |
|---|---|
| Wiek | ? |
| Wzrost | ? (anonimowy) |
| Budowa ciała | ? (anonimowy) |
| IQ | ? |
| Rola | były legionista 2e REG [P] |
| Wygląd | ? (anonimowy) |
| Wiedza | ? |
| Motywacje | ? |
| Sekrety | ? |
| Stosunek platoniczny do Antoniny | **0** |
| Stosunek romantyczny do Antoniny | **0** |
| Stan | „agrafa to nie wizyta kurtuazyjna, ale nie spekuluję” (Twitter FR, 19 I) |
| Jak grać | ? |

### u/lauriane_en_dentelle

| Pole | Wartość |
|---|---|
| Wiek | ? |
| Wzrost | ? (anonimowy) |
| Budowa ciała | ? (anonimowy) |
| IQ | ? |
| Rola | r/france, obrończyni Antoniny w komentarzach [P] |
| Wygląd | ? (anonimowy) |
| Wiedza | ? |
| Motywacje | ? |
| Sekrety | ? |
| Stosunek platoniczny do Antoniny | **+2** [P] |
| Stosunek romantyczny do Antoniny | **0** |
| Stan | bije się z „gaston_de_la_gruyere” |
| Jak grać | ? |

### @Jelska_Facts

| Pole | Wartość |
|---|---|
| Wiek | ? |
| Wzrost | ? (anonimowy) |
| Budowa ciała | ? (anonimowy) |
| IQ | ? |
| Rola | konto-mem (Chuck Norris Facts), od 19 I 8:55, 4 800 obs. |
| Wygląd | ? (anonimowy) |
| Wiedza | ? |
| Motywacje | ? |
| Sekrety | ? |
| Stosunek platoniczny do Antoniny | **0** |
| Stosunek romantyczny do Antoniny | **0** |
| Stan | 6 wpisów do 16:00 |
| Jak grać | ? |

### @Tosia_Oficjalna

| Pole | Wartość |
|---|---|
| Wiek | ? |
| Wzrost | ? (anonimowy) |
| Budowa ciała | ? (anonimowy) |
| IQ | ? |
| Rola | parodia („NIE JESTEM ANTONINĄ”) |
| Wygląd | ? (anonimowy) |
| Wiedza | ? |
| Motywacje | ? |
| Sekrety | ? |
| Stosunek platoniczny do Antoniny | **0** |
| Stosunek romantyczny do Antoniny | **0** |
| Stan | ok. 3 300 RT najpopularniejszy wpis; może przeszkodzić prawdziwej Antoninie, jeśli wróci do Twittera |
| Jak grać | ? |

### u/legion_historian_nl

| Pole | Wartość |
|---|---|
| Wiek | ? |
| Wzrost | ? (anonimowy) |
| Budowa ciała | ? (anonimowy) |
| IQ | ? |
| Rola | flair „Modern French Military” na r/AskHistorians [P] |
| Wygląd | ? (anonimowy) |
| Wiedza | ? |
| Motywacje | ? |
| Sekrety | ? |
| Stosunek platoniczny do Antoniny | **0** |
| Stosunek romantyczny do Antoniny | **0** |
| Stan | rzeczowa odpowiedź o kobietach w Legii (19 I 17:02); może wrócić przy kolejnych falach |
| Jak grać | ? |

### @Joanna_od_Pierwszego_Slowa 🟣

| Pole | Wartość |
|---|---|
| Wiek | ? |
| Wzrost | ? (anonimowy) |
| Budowa ciała | ? (anonimowy) |
| IQ | ? |
| Rola | feministka na Wykopie [P] |
| Wygląd | ? (anonimowy) |
| Wiedza | ? |
| Motywacje | ? |
| Sekrety | ? |
| Stosunek platoniczny do Antoniny | **+2** [P] |
| Stosunek romantyczny do Antoniny | **0** |
| Stan | ostre odpowiedzi na „gdyby to był facet…” |
| Jak grać | ? |

### @Libe_Desintox

| Pole | Wartość |
|---|---|
| Wiek | ? |
| Wzrost | ? (anonimowy) |
| Budowa ciała | ? (anonimowy) |
| IQ | ? |
| Rola | konto redakcyjne (FR; Libération Désintox) |
| Wygląd | ? (anonimowy) |
| Wiedza | ? |
| Motywacje | ? |
| Sekrety | ? |
| Stosunek platoniczny do Antoniny | **0** |
| Stosunek romantyczny do Antoniny | **0** |
| Stan | dementi 19 I; może wrócić przy France-Guyane |
| Jak grać | ? |

### @X_Amicale

| Pole | Wartość |
|---|---|
| Wiek | ? |
| Wzrost | ? (anonimowy) |
| Budowa ciała | ? (anonimowy) |
| IQ | ? |
| Rola | konto stowarzyszeniowe (FR; amicale de l'X) |
| Wygląd | ? (anonimowy) |
| Wiedza | ? |
| Motywacje | ? |
| Sekrety | ? |
| Stosunek platoniczny do Antoniny | **0** |
| Stosunek romantyczny do Antoniny | **0** |
| Stan | dementi 19 I; może wrócić przy France-Guyane |
| Jak grać | ? |

### @ola_vlog_pl

| Pole | Wartość |
|---|---|
| Wiek | ? |
| Wzrost | ? (anonimowy) |
| Budowa ciała | ? (anonimowy) |
| IQ | ? |
| Rola | influencerka (ok. 112 000 obs.) [P] |
| Wygląd | ? (anonimowy) |
| Wiedza | ? |
| Motywacje | ? |
| Sekrety | ? |
| Stosunek platoniczny do Antoniny | **+1** [P] |
| Stosunek romantyczny do Antoniny | **0** |
| Stan | zaprosiła Antoninę „na kawę” (19 I 18:12) |
| Jak grać | ? |

### u/skeptic_in_residence

| Pole | Wartość |
|---|---|
| Wiek | ? |
| Wzrost | ? (anonimowy) |
| Budowa ciała | ? (anonimowy) |
| IQ | ? |
| Rola | sceptyk z r/conspiracy [P] |
| Wygląd | ? (anonimowy) |
| Wiedza | ? |
| Motywacje | ? |
| Sekrety | ? |
| Stosunek platoniczny do Antoniny | **0** |
| Stosunek romantyczny do Antoniny | **0** |
| Stan | „brzytwa Ockhama” przy teoriach |
| Jak grać | ? |

### @kapusta_na_wynos

| Pole | Wartość |
|---|---|
| Wiek | ? |
| Wzrost | ? (anonimowy) |
| Budowa ciała | ? (anonimowy) |
| IQ | ? |
| Rola | wykopowicz zakładający znaleziska o „4 z 21” [P] |
| Wygląd | ? (anonimowy) |
| Wiedza | ? |
| Motywacje | ? |
| Sekrety | ? |
| Stosunek platoniczny do Antoniny | **0** |
| Stosunek romantyczny do Antoniny | **0** |
| Stan | może być autorem kolejnych memów |
| Jak grać | ? |

### @mietek_z_Hrubieszowa

| Pole | Wartość |
|---|---|
| Wiek | ? |
| Wzrost | ? (anonimowy) |
| Budowa ciała | ? (anonimowy) |
| IQ | ? |
| Rola | wykopowicz zakładający znaleziska o „Gdzie jest Tosia?” [P] |
| Wygląd | ? (anonimowy) |
| Wiedza | ? |
| Motywacje | ? |
| Sekrety | ? |
| Stosunek platoniczny do Antoniny | **0** |
| Stosunek romantyczny do Antoniny | **0** |
| Stan | może być autorem kolejnych memów |
| Jak grać | ? |

### @bezpiecznik_IT

| Pole | Wartość |
|---|---|
| Wiek | ? |
| Wzrost | ? (anonimowy) |
| Budowa ciała | ? (anonimowy) |
| IQ | ? |
| Rola | specjalista bezpieczeństwa IT na Wykopie [P] |
| Wygląd | ? (anonimowy) |
| Wiedza | ? |
| Motywacje | ? |
| Sekrety | ? |
| Stosunek platoniczny do Antoniny | **0** |
| Stosunek romantyczny do Antoniny | **0** |
| Stan | ostrzeżenie przed malware „nagie zdjęcia Jelskiej” (19 I 21:50); wiarygodny; może wrócić przy kolejnych oszustwach |
| Jak grać | ? |

### u/polish_translator_kasia

| Pole | Wartość |
|---|---|
| Wiek | ? |
| Wzrost | ? (anonimowy) |
| Budowa ciała | ? (anonimowy) |
| IQ | ? |
| Rola | tłumaczka z polskiego na Reddicie [P] |
| Wygląd | ? (anonimowy) |
| Wiedza | ? |
| Motywacje | ? |
| Sekrety | ? |
| Stosunek platoniczny do Antoniny | **+1** [P] |
| Stosunek romantyczny do Antoniny | **0** |
| Stan | tłumaczy AMA (r/europe, 19 I 22:40); może wzmacniać zasięg AMA po angielsku |
| Jak grać | ? |

### @PZSzermierczy

| Pole | Wartość |
|---|---|
| Wiek | ? |
| Wzrost | ? (anonimowy) |
| Budowa ciała | ? (anonimowy) |
| IQ | ? |
| Rola | oficjalne konto Polskiego Związku Szermierczego |
| Wygląd | ? (anonimowy) |
| Wiedza | ? |
| Motywacje | ? |
| Sekrety | ? |
| Stosunek platoniczny do Antoniny | **0** |
| Stosunek romantyczny do Antoniny | **0** |
| Stan | zaproszenie do powrotu na planszę (19 I 21:40) |
| Jak grać | ? |

### @ParisPotins

| Pole | Wartość |
|---|---|
| Wiek | ? |
| Wzrost | ? (anonimowy) |
| Budowa ciała | ? (anonimowy) |
| IQ | ? |
| Rola | konto plotkarskie (Twitter, 131 tys. obs.) [P] |
| Wygląd | ? (anonimowy) |
| Wiedza | zdjęcie z tarasu |
| Motywacje | ? |
| Sekrety | ? |
| Stosunek platoniczny do Antoniny | **0** |
| Stosunek romantyczny do Antoniny | **0** |
| Stan | opublikowało zdjęcie Antoniny z tarasu (nd 20 I 12:31) — usunięte po wezwaniu Clémence; źródło: Clara D. (stylistka, Paryż) |
| Jak grać | ? |

### u/Archiviste_en_retraite

| Pole | Wartość |
|---|---|
| Wiek | ? |
| Wzrost | ? (anonimowy) |
| Budowa ciała | ? (anonimowy) |
| IQ | ? |
| Rola | były archiwista Obrony (flair r/france) [P] |
| Wygląd | ? (anonimowy) |
| Wiedza | ? |
| Motywacje | ? |
| Sekrety | ? |
| Stosunek platoniczny do Antoniny | **0** |
| Stosunek romantyczny do Antoniny | **0** |
| Stan | wyjaśnia „classé ≠ classifié” (nd 20 I 8:40); wiarygodny, może wrócić przy France-Guyane |
| Jak grać | ? |

### @Max_Planck_PR

| Pole | Wartość |
|---|---|
| Wiek | ? |
| Wzrost | ? (anonimowy) |
| Budowa ciała | ? (anonimowy) |
| IQ | ? |
| Rola | konto instytucji (Max-Planck-Gesellschaft) [P] |
| Wygląd | ? (anonimowy) |
| Wiedza | ? |
| Motywacje | ? |
| Sekrety | ? |
| Stosunek platoniczny do Antoniny | **0** |
| Stosunek romantyczny do Antoniny | **0** |
| Stan | „nie komentujemy prywatnych relacji” (20 I 10:15) |
| Jak grać | ? |

---

## J. Media i tło medialne

*Karty przeniesione: Anne-Laure Python — §E; Grzegorz Pawlak, Kévin Bühler, Dylan Pereira, Filip — §D; Paweł Wróblewski — §H.*

### Zbigniew Marczak

| Pole | Wartość |
|---|---|
| Wiek | ok. 55 [P] |
| Wzrost | ok. 180 cm [P] |
| Budowa ciała | ok. 82 kg; trener, zachowany w formie [P] |
| IQ | ok. 120 [P] |
| Rola | trener kadry szpadzistek PZSzerm |
| Wygląd | [P] krótkie siwe włosy, dres kadry |
| Wiedza | trener kadry od 2009 [P]: prowadził Antoninę na MŚ 2010 (Paryż) i 2011 (Katania); zna jej wyniki (ME U-23 złoto 2005–2008, MŚ złoto 2007, 2008, 2010, 2011); wie, że PKOl nie dał jej stypendium na Pekin; szuka szpadzistek do kadry [korekta Z231] |
| Motywacje | wciągnąć Antoninę z powrotem na planszę |
| Sekrety | [?] — brak ustaleń |
| Stosunek platoniczny do Antoniny | **+2** [P] — podziw sportowy |
| Stosunek romantyczny do Antoniny | **0** [P] |
| Stan | **15 I:** wiadomość na FB: „drzwi są otwarte” |
| Jak grać | rzeczowy trener; „drzwi są otwarte”; nie naciska. |

### Lena Hoffmeister

*„Płacząca Niemka” z podium 2007 [N, autor 11 X 2026; szczegóły P]. Konto: @Lena_H_official (zweryfikowane).*

| Pole | Wartość |
|---|---|
| Wiek | 25 (ur. VIII 1987); Heidenheim an der Brenz (Badenia-Wirtembergia) |
| Wzrost | ok. 170 cm |
| Budowa ciała | szczupła, atletyczna [P] |
| IQ | ok. 125 [P] |
| Rola | szermierka: szpada, **Heidenheimer SB** (niemieckie centrum szpady); brąz ME U-23 2007 (Jelska — złoto, później czterokrotna mistrzyni świata; Z228); w półfinale przegrała z Jelską **14:15** po prowadzeniu 14:11 — cztery trafienia z rzędu; płakała, bo była pewna finału, nie z powodu medalu; dziś startuje rekreacyjnie w Bundeslidze dla klubu. **2013: aplikantka prawnicza** (Rechtsreferendarin) w Stuttgarcie |
| Wygląd | ciemnoblond włosy; na zdjęciu z 2007 zakrywa twarz dłonią; Facebook (prywatny, ok. 600 znajomych), Twitter rzadko |
| Wiedza | pamięta Jelską jako „die Wand” (ścianę) — z szacunkiem i lekką urazą |
| Motywacje | nie być ofiarą; odciąć się od przekrętów mediów |
| Sekrety | cień żalu za półfinał |
| Stosunek platoniczny do Antoniny | **+1** [P] — brak kontaktu od 2007; respekt sportowy, cień żalu za półfinał |
| Stosunek romantyczny do Antoniny | **0** [P] |
| Stan | **20 I:** 10:40 @Lena_H_official broni kobiet przed BamS.<br>**18 I:** 4:12 Bild.de przekręca sprawę („Polnische Internet-Hetze gegen deutsche Fechterin — wegen der Tochter eines Ex-Premiers”); plan MG: Lena publicznie odetnie się od Bilda.<br>**17 I:** Stuttgarter Zeitung życzliwie.<br>**16 I:** 20:30 publiczny post na FB („Grunwald war 1410, ich war 2007”) |
| Jak grać | **Charakter:** ambitna, prostolinijna, z suchym szwabskim humorem; nie znosi bycia ofiarą.<br>**Potencjał:** zamieszanie w niemieckich mediach: Bild / Spiegel Online / Stuttgarter Zeitung; polskie memy „Grunwald 2007” jako temat polsko-niemiecki. |

### Mark Sorensen

| Pole | Wartość |
|---|---|
| Wiek | 33 |
| Wzrost | ok. 183 cm [P] |
| Budowa ciała | ok. 80 kg [P] |
| IQ | ok. 125 [P] |
| Rola | „Senior Partner, Beacon Search” (Boston) — przykrywka STEEPLE [MG]; miękkie podejścia do naukowców |
| Wygląd | [P] uśmiechnięty, gładki, garnitur |
| Wiedza | dane z profilu LinkedIn Antoniny; lista doktorantów Vasseura |
| Motywacje | sondowanie reakcji i danych; rekrutacja przykrywkowa |
| Sekrety | przykrywka STEEPLE; brak kontaktu osobistego (czerwona linia) |
| Stosunek platoniczny do Antoniny | **0** |
| Stosunek romantyczny do Antoniny | **0** |
| Stan | **21 I (sesja 16):** 21:16 CET zaproszenie i InMail na LinkedInie („2D-materials lead, Fortune 500, Massachusetts”); bez odpowiedzi |
| Jak grać | uprzejmy Amerykanin; krótkie wiadomości; „No obligation, just a conversation.” |

### mec. Kowalczyk

| Pole | Wartość |
|---|---|
| Wiek | ok. 48 [P] |
| Wzrost | ok. 180 cm [P] |
| Budowa ciała | ok. 85 kg [P] |
| IQ | ok. 130 [P] |
| Rola | adwokat, prawa osobiste i wizerunek (Warszawa); ok. 600 zł/h [P] |
| Wygląd | [P] siwiejący, garnitur, okulary w złotej oprawie |
| Wiedza | art. 23–24 kc, art. 81 pr. aut.; sprawa „zdjęcia z tarasu” i fotomontaży |
| Motywacje | wygrać czas; udokumentować odmowę Pudelka |
| Sekrety | [?] — brak ustaleń |
| Stosunek platoniczny do Antoniny | **0** |
| Stosunek romantyczny do Antoniny | **0** |
| Stan | **21 I (sesja 16):** pełnomocnictwo (6:36 lok.); wezwania wysłane 17:41 CET; Pudelek odmówił na piśmie; zgłoszenia o podszywanie się (Instagram, Facebook, Twitter @toni_31, @toni31_) wieczorem; rada: bez publicznych oświadczeń |
| Jak grać | rzeczowy, ostrożny; „Bez komentarza.”; mówi pełnymi zdaniami z podstawą prawną. |

### mec. Cécile Dubreuil

| Pole | Wartość |
|---|---|
| Wiek | 46 [P] |
| Wzrost | ok. 170 cm [P] |
| Budowa ciała | ok. 60 kg [P] |
| IQ | ok. 135 [P] |
| Rola | adwokat, prawo prasowe (Paryż 8e); prowadziła sprawę Closera przeciw księżnej [P]; pełnomocnik Coquelicots |
| Wygląd | [P] ciemny kostium, krótkie włosy, chłodne spojrzenie |
| Wiedza | art. 9 Code civil; référé; praktyka Paris Match i Closera |
| Motywacje | zatrzymać publikację lub wygrać odszkodowanie |
| Sekrety | [?] — brak ustaleń |
| Stosunek platoniczny do Antoniny | **0** |
| Stosunek romantyczny do Antoniny | **0** |
| Stan | **21 I (sesja 16):** zaliczka 7 000 € (CARPA) przelana przez Antoninę; mise en demeure do Paris Match i Voici 22 I 9:00 CET; référé w środę |
| Jak grać | chłodna, skuteczna, krótka; „Pas de garantie, mais un dossier.” |

---

## K. École polytechnique — promocja X2007 [N autor + P MG, 12 X 2026]

**Fakty [N]:** Antonina wstąpiła na l'X w 2007 (**korekta Z132 [N]: konkurs uniwersytecki zagraniczny — 1. miejsce, jako bakałarz EPFL**; jako obywatelka Francji miała status wojskowy i odbyła FHM; wcześniej błędnie „ścieżka francuska”) — **promocja X2007; major de promotion formalnie dopiero od końca 3. roku (VI 2010)** [N, Z185]; wcześniej major d'entrée i najlepsza w programie (w OTL majorem był ktoś inny; w tej linii jej nazwisko stoi na pierwszym miejscu listy w dekrecie). Na l'X miała status ikony: **ocena końcowa 20/20 na każdym roku** (bezprecedensowo, „obraźliwie dla instytucji”, Z185), szermierka (złoto ME U-23), „bycie sobą”. Postaci poniżej są **fikcyjne** — realnych absolwentów X2007 nie wprowadzamy do gry.
**Czwarty rok** cyklu inżynierskiego zrealizowała jako MSc EPFL (2010–11); dyplom ingénieur polytechnicien z promocją w 2011 [P].
**Legenda promocji [P]:** „la Major qui a refusé les Mines” — jako major mogła wybrać Corps des Mines i odmówiła (EPFL, Thales). W X2007 jedni uważają to za klasę, inni za policzek. Przezwiska: **„Toni la Major”**, „le Colosse de Palaiseau” (za plecami).
**Bal de l'X** (Opéra Garnier) — zdjęcie grupowe przyjaciółek w czerwonych sukniach na Wielkich Schodach (obraz poglądowy autora, Z35): Antonina siedzi pośrodku. Grupa nazywa się **„les Coquelicots”** (od sukni; tak też nazywa się ich czat) [P].

#### Les Coquelicots — opis zbiorowy (karty indywidualne: niżej)

**Wiedza grupy [P]:** znają Antoninę z l'X jako „Toni”; wiedzą, że jest córką polskiego ex-premiera (bez szczegółów); wiedzą, że FHM odbyła w Gujanie „z Legią”. **O Commando Jaubert, zabitych i OIOM nie wie nikt** — ale Sarah i Fiona pamiętają, że w 2008 „zniknęła na kilka tygodni” i wróciła z kaszlem, jeszcze masywniejsza w barach i bez wyjaśnień. Od 15–16 I wszystkie widzą burzę medialną (MailOnline, „Fakt”, Weibo); czat „Coquelicots 🌺” pęka w szwach, Antonina nie odpowiada (18 I, 5:00: 17 nieprzeczytanych).

**Wiek, rekrutacja, ranking, atrakcyjność (Z131–Z132):** Antonina (25, ur. 17 XII 1987) jest **najmłodsza**; na l'X weszła w wieku 19 lat. Rekrutacja na l'X (X2007) — cztery osobne rankingi wstępne: (1) konkurs krajowy CPGE (MP, PC, PSI, BCPST…), (2) konkurs uniwersytecki krajowy, (3) konkurs zagraniczny CPGE, (4) konkurs uniwersytecki zagraniczny. **Ranking końcowy:** 497 absolwentów X2007. Z konkursu zagranicznego CPGE w grupie nie ma nikogo. Atrakcyjność — ocena „obiektywna”, wg konwencjonalnych kryteriów; **wszystkie są konwencjonalnie atrakcyjne**.

| | Wiek (I 2013) / wzrost | IQ | Wejście | Ranking końcowy | Atrakcyjność |
|---|---|---|---|---|---|
| **Antonina** | 25 (17 XII 1987) / 193 | ~210 | **zagr. uniwersytecki — 1.** (BSc EPFL) [N] | **1/497** | **twarz 9,5/10** [N]; ciało bardzo specyficzne (oceny skrajne) |
| **Xiaomei** | 26 (XI 1986) / 160 | **~180** [N] | **zagr. uniwersytecki — 2.** [N] (2 lata matematyki, Shanghai Jiao Tong, Zhiyuan College) | **2/497** [N] | 8/10 |
| **Annika** | 26 (II 1986) / 175 | ~160 | zagr. uniwersytecki — 6. (2 lata fizyki, TU München) | 11/497 | 8/10 |
| **Clémence** | 25 (III 1987) / 178 | ~152 | krajowy CPGE, MP — 11. (Lycée du Parc, Lyon) | 19/497 (15. wśród Francuzów → ostatnie miejsce w Corps des Mines po odmowie Toni) | 8/10 |
| **Elif** | 26 (VIII 1986) / 166 | ~148 | zagr. uniwersytecki — 9. (2 lata mechaniki, Boğaziçi) | 64/497 | 8,5/10 |
| **Sarah** | 25 (27 I 1987 — urodziny za tydzień) / 163 | ~140 | krajowy CPGE, BCPST — 2. (Lycée Thiers, Marsylia) | 88/497 | 7,5/10 |
| **Fiona** | 27 (IV 1985) / 170 | ~143 | zagr. uniwersytecki — 17. (2 lata fizyki, St Andrews) | 141/497 | 7,5/10 |
| **Juliette** | 26 (V 1986) / 168 | ~145 | krajowy uniwersytecki — 3. (licence de physique, UPMC Paris 6) | 203/497 (po 2. roku odpuściła na rzecz „l'IK”) | 8,5/10 |

**Jak się poznały (2007–2009):**
- **Wrzesień 2007 – marzec 2008:** obywatelki Francji (Clémence, Sarah, Juliette — oraz Antonina, która weszła z konkursu zagranicznego, ale jako Francuzka ma status wojskowy) idą na **FHM** — każda gdzie indziej (Clémence: Marine nationale, fregata w Tulonie; Sarah: **Brigade de sapeurs-pompiers de Paris**; Juliette: żandarmeria mobilna, Satory; Antonina: oficjalnie 3e REI, Gujana). Studentki ścieżki międzynarodowej (Xiaomei, Elif, Annika, Fiona) zaczynają w Palaiseau od kursu francuskiego i krótkiego stażu.
- **Kwiecień 2008 — „les retardataires” (spóźnione):** wszystkie lądują na tym samym piętrze kobiecego skrzydła kazerny (bât. 72, 3e étage). Antonina wraca z Gujany ostatnia, **kaszląca, milcząca, jeszcze masywniejsza niż jesienią** (Z202). Sarah (po BSPP — odruch ratowniczki) przynosi jej zupę i syrop; Xiaomei pożycza notatki z Analizy, które Antonina oddaje następnego dnia z poprawionymi trzema błędami; Fiona puszcza Alestorm przez ścianę o 2:00. Pierwsza wspólna noc: nauka do kolokwium z Analizy 2 w pokoju Sarah, z nielegalną kuchenką.
- **14 VII 2008:** Antonina niesie sztandar; reszta stoi w szyku i smaży się w wełnie (Fiona: „statua przez sześć godzin”; Sarah: kaszel).
- **Bal de l'X 2009 (Opéra Garnier):** pomysł Clémence — wszystkie w czerwieni; zdjęcie na Wielkich Schodach (Antonina siedzi pośrodku, bo stojąc zasłoniłaby resztę). Ktoś z Kès nazywa je „les Coquelicots” — maki, czerwone, symbol pamięci poległych (11 listopada) — nazwa zostaje. **Bal de l'X odbywa się co roku w marcu** [N, Z248]: Bal 2009 = III 2009 (czerwone suknie, zdjęcie B); wcześniejszy „bal XI 2008” z ciemną suknią i Ravelem (F08) został uchylony (w III 2008 Antonina jest jeszcze na FHM).

**Na l'X (2008–2010):**

| Kto | Wydział / sekcja sportowa / binet | Pamiętana z… |
|---|---|---|
| **Antonina** | fizyka + materiały; **szermierka** (szpada); chór (słuch absolutny) | 20/20, sztandar, odmowa Corps des Mines; w grupie — totem, nie przywódczyni |
| **Clémence** | ekonomia + matematyka stosowana; **wioślarstwo**; skarbniczka Kès | wzięła ostatnie miejsce w Corps des Mines „zwolnione przez Toni” — wdzięczność i zadra jednocześnie |
| **Sarah** | biologia; **piłka ręczna**; binet Gastronomie | **„l'évacuation de la bouillabaisse”** (2009): alarm przeciwpożarowy o 2:10, ewakuacja całego budynku przez nielegalną kuchenkę |
| **Juliette** | humanistyka + ekonomia; pływanie; redaktorka **„l'IK”** (tygodnik studencki) | jej satyryczna rubryka „La Petite Polonaise” (za zgodą Toni) — początek ciągot dziennikarskich |
| **Elif** | mechanika; jeździectwo; założycielka **binetu Tarot** | wróżby przed egzaminami — w 2009 trafiła w ranking 5 z 8 Coquelicots; pali na dachu |
| **Annika** | fizyka; **wspinaczka**, X-Montagne | jedyna, z którą Toni rozmawia o fononach do rana; plany wyjazdów co do minuty |
| **Fiona** | mechanika/energetyka; **rugby** kobiece; **dudy** w binecie muzycznym | dudy na Point Gamma 2009; Alestorm o 2:00; kapitan picia |
| **Xiaomei** | matematyka; badminton; binet Go | druga w Analizie po Toni; jej notatki + poprawki Toni = **„le Poly rouge”**, krążący do dziś po rocznikach X2008–X2011 |

**Z czego słyną (famous):**
- **Zdjęcie z balu 2009** — osiem czerwonych sukni na Schodach Garnier; wisiało w Kès przez dwa lata.
- **„Le Poly rouge”** — notatki z Analizy i Fizyki (Xiaomei + Toni), skanowane, kopiowane, przekazywane młodszym.
- Wszystkie skończyły w pierwszej trzydziestce promocji lub na swojej ścieżce międzynarodowej w czołówce; Antonina pierwsza.

**Z czego słyną (infamous):**
- **„L'évacuation de la bouillabaisse”** (Sarah, 2009).
- **Point Gamma 2009:** Fiona na dudach + Elif z tarotem + Toni śpiewająca *Le Boudin* kontraltem na scenie o 4:00 — nagranie istnieje u kogoś z X2007 [MG: hak — może wypłynąć].
- **Reputacja „zamkniętego klubu”:** nie przyjmują nowych; chłopcy z promocji nazywali je „le Politburo”. Arnaud de Courcel — „la secte rouge”.

**Role i hierarchia w grupie:**

| Rola | Kto | Jak działa |
|---|---|---|
| **Głowa / „la Générale”** | **Clémence** | kalendarz, plany, listy; formalnie nikt jej nie wybrał, ale bez niej nic się nie odbywa. Od 2013 konflikt: teczka Malakoff (APE) |
| **Serce / „Maman”** | **Sarah** | karmi, dzwoni, płacze pierwsza; jej ślub (lato 2013, Marsylia) to oś roku. Mieszka w Paryżu (start-up przy Institut Pasteur). **Czuje się czasem pomijana** („wszystkie wiedziałyście oprócz mnie”) |
| **Totem / „la Major”** | **Antonina** | poza hierarchią: duma grupy i jej projekt ochronny; nie organizuje, nie rządzi; przychodzi, gdy jest wezwana, i wtedy załatwia. Najmłodsza — Elif mówi o niej „la petite”, bo to absurd |
| **Prowokatorka / „la Sorcière”** | **Elif** | mówi to, czego inne nie powiedzą; doradczyni od mężczyzn i seksu; rywalizuje z Clémence (chaos vs plan) |
| **Morale / „Capitaine”** | **Fiona** | żarty, muzyka, rozładowanie napięcia; most do Toni po gaelicku; organizuje alkohol |
| **Rozsądek / „Herr Doktor”** | **Annika** | spokojna, rzeczowa, gasi kłótnie; logistyka wyjazdów |
| **Sejf / „le Coffre-fort”** | **Xiaomei** | najmniej mówi, najwięcej wie; **weto w sprawach prywatności** — gdy mówi „nie”, grupa słucha. Najsłabiej znana: o jej życiu w Szanghaju nie wie nikt dużo [MG: wektor MSS] |
| **Węzeł informacji / „l'AFP”** | **Juliette** | wie pierwsza, mówi ostatnia; od 2013 rozdarta (Le Monde vs Toni) |

**Geografia (I 2013):** „rdzeń paryski” — Clémence, Sarah, Juliette, Xiaomei (widują się co tydzień); Elif (Tuluza), Annika (Stuttgart), Fiona (Derby), Antonina (Lozanna) — „diaspora”. Napięcie: rdzeń decyduje, diaspora dowiaduje się z czatu.
**Zasada grupy:** *„Ce qui se dit chez les Coquelicots reste chez les Coquelicots.”* Dotąd nie złamana. Spotkanie roczne: **Bal de l'X** (marzec) — Antonina opuściła 2011 i 2012.
**Tarcia [P]:** Clémence ↔ Elif (plan vs chaos); Sarah ↔ rdzeń (pomijana mimo że w Paryżu — to Juliette i Clémence trzymają się najbliżej); Juliette ↔ zawód; Clémence ↔ Malakoff; Xiaomei ↔ rodzina w Szanghaju.

**Bliskość i fizyczność [N, autor 16 X 2026; Z132]:**
- **Poziom BFF:** bardzo, bardzo blisko zżyte; **bez tajemnic** — można wszystko, także tematy prywatne i intymne. **Wyjątek: Xiaomei i wszystko, co dotyczy Chin** (oraz jej samej).
- **Fizyczność:** swobodne wobec siebie, także nago (przebieralnie, sauna, wspólne noce w jednym łóżku, prysznice po sporcie). Przyjacielski, platoniczny dotyk. Przyjaciółki są **zafascynowane mięśniami, pośladkami i biustem Antoniny** — traktują ją jak **„chodzący posąg”**: klepią, ściskają biceps, mierzą obwody, siadają jej na kolanach, opierają się o nią jak o ścianę.
- **Ksywka „Athena”** (pol. „Atena”) — podziw i szydera naraz; **geneza [?] — autor ujawni (Z185, `17-lx-i-coquelicots-2007-2011.md` §3)**, do tego czasu bez wymyślania. Pada, gdy Antonina mówi o sile fizycznej albo zachowuje się jak posąg (np. Toni: „I carried the sofa myself” → Juliette: „shut up, Athena 😂”). Obok: „Toni”, „la Major”, „la petite” (Elif, z przekąsem).

**Wątki [P]:** (1) **zdjęcie z balu** trafia do sieci (Vautrin / znajomy znajomego) → MailOnline lub „Fakt”: „córka premiera na balu elity Francji” — kontrast z „nie jestem człowiekiem”; (2) **Juliette** dostaje od naczelnego zlecenie portretu; (3) **Clémence** widzi Malakoff i czek in blanco z drugiej strony biurka; (4) **Annika** jako pomost do wątku Leny i niemieckich mediów; (5) **ślub Sarah** (lato 2013) jako zjazd Coquelicots; (6) **Ravel** i **Fiona/Sarah** jako ślady prowadzące do Gujany; (7) **Arnaud** jako przeciwnik w Matignon; (8) **Xiaomei** jako możliwy wektor nacisku ChRL.

### Clémence Aubertin

| Pole | Wartość |
|---|---|
| Wiek | 25 (III 1987) |
| Wzrost | 178 cm |
| Budowa ciała | ok. 65 kg; smukła wioślarka wagi lekkiej, długie ręce [P] |
| IQ | ~152 |
| Rola | „la Générale”; Francuzka (Lyon, Lycée du Parc); wzięła ostatnie miejsce w Corps des Mines, „które zwolniła Toni”; dziś w **Agence des participations de l'État** (w tej linii — dyrekcja nadzoru właścicielskiego **Le Combinat de France**, Z138) — nadzór nad udziałami państwa, m.in. w **Compagnie de Malakoff**; prowadzi teczkę Malakoff (w tym Amantis, operacyjnie przy CDM) |
| Wygląd | wysoka, jasnobrązowe włosy zawsze upięte; klasyczna, wypolerowana uroda „grande bourgeoise lyonnaise”; najlepiej ubrana w grupie; atrakcyjność 8/10; na zdjęciu: tył, lewo |
| Wiedza | numerowane listy, Excel do wszystkiego (budżet wesela Sarah); w APE widziała pozycję kosztową „vol VIP F-ICIV, 18–19 I” bez nazwiska — jeszcze nie połączyła [MG]; wie, co de Courcel mówi o Toni |
| Motywacje | menedżerka życia Toni, jedyna, która na nią krzyczy; lojalna wobec instytucji i przyjaciółek naraz — od teraz zgrzyta. **Pokusa:** kariera przez wroga — **Arnaud de Courcel** proponuje jej stanowisko w gabinecie Guaino i ją adoruje |
| Sekrety | bulimia w czasach wioślarstwa wagi lekkiej (2006–09), leczona; wyciągnęły ją z tego Coquelicots (Sarah) — grupa wie |
| Stosunek platoniczny do Antoniny | **+4** (dług i podziw; Toni ufa jej planom bez czytania) |
| Stosunek romantyczny do Antoniny | **0** [P] — platoniczny zachwyt fizyczny („posąg”) |
| Stan | **21 I (sesja 16, do 20:23 lok.):** koordynuje: mise en demeure (22 I 9:00 CET), référé (śr), mec. Dubreuil (CARPA 7 000 €), stowarzyszenie „Les Coquelicots 2007”, oświadczenie 3-zdaniowe; szef w Malakoff dzwonił (Paris Match o „la Générale”); 6:09 CET Voici; dzwoni do Xiaomei o 7:00<br>**21 I:** 10:05 CET: „Toni. Deux fuites en deux jours. Il faut que quelqu'un, là où tu es, fasse le ménage.”.<br>**20 I:** 15:05 znajomy adwokat (prawo do wizerunku), wezwanie do @ParisPotins wysłane o 15:00; prowadzi teczkę Malakoff/APE (Kombinat); bieg o 5:30, sen 5 h |
| Jak grać | organizatorka grupy i strażniczka kalendarza (urodziny, bal, wesele Sarah); ambitna, poprawna; mówi szybko, punktami; SMS-y francuskie, poprawne, z „!!”; pierwsza proponuje „plan”; „On fait comme ça.”; maks. dwa kieliszki. |

### Xiaomei Lin (林晓梅)

| Pole | Wartość |
|---|---|
| Wiek | 26 (XI 1986) |
| Wzrost | 160 cm |
| Budowa ciała | ok. 48 kg; drobna [P] |
| IQ | **~180** [N] |
| Rola | „le Coffre-fort”; Chinka (Szanghaj), ścieżka międzynarodowa; 2 lata matematyki w Shanghai Jiao Tong (Zhiyuan College); wejście zagr. uniwersytecki — 2.; ranking 2/497 [N], oceny końcowe ok. 19,5/20 na każdym roku (tuż za Antoniną) [N, Z185]; dziś analityczka ilościowa w funduszu w Paryżu; ojciec — urzędnik w biurze finansów miasta Szanghaj, matka — nauczycielka matematyki; jedynaczka [P] |
| Wygląd | drobna, porcelanowa cera, wysokie kości policzkowe, proste czarne włosy do ramion; okulary w cienkich oprawkach do czytania; czerń i biel, minimalizm; atrakcyjność 8/10; na zdjęciu: Azjatka z kieliszkiem (lewo) |
| Wiedza | akademicka bliźniaczka Antoniny — 2. za Toni na wejściu i na wyjściu; to wyglądało na rywalizację, było wsparciem („le Poly rouge”); z Toni czasem po mandaryńsku |
| Motywacje | prywatność obsesyjnie (weto w grupie); **pokusy:** wyznać (Toni albo grupie); poddać się rodzinie — chiński Nowy Rok (10 II), swatanie, „powrót na stałe” |
| Sekrety | **[N]** lesbijka — ukrywa to przed rodziną i przed wszystkimi, także przed Coquelicots; **podkochuje się w Antoninie**, widzi w niej ideał „masc fem”; Antonina była jej przebudzeniem (IV 2008); mechanizm: zaprzeczenie — tematy intymne i seksualne są dla niej niekomfortowe; wycofuje się, milczy albo ucina („+1 Juliette. Please.”, 19 I); **[MG]** wektor MSS (rodzina, paszport) |
| Stosunek platoniczny do Antoniny | **+4** |
| Stosunek romantyczny do Antoniny | **+4** [N + P] — ukryte zakochanie |
| Stan | **21 I (sesja 16, do 20:23 lok.):** „I'm here. Please nobody say my mother's name.”; „no names, not even initials”; Voici 22 I 5:58 CET: „une septième d'origine chinoise”; milczy; Clémence dzwoni 7:00 CET<br>**21 I:** bez wiadomości.<br>**20 I:** 21:10 CET: „Glad you're safe.” |
| Jak grać | cicha, precyzyjna, sucho zabawna; chroni prywatność obsesyjnie; po francusku bardzo poprawnie, z Toni czasem po mandaryńsku; po chińsku o niczym, co ważne. SMS-y krótkie, bez emotikon albo z jednym 🙂. **[MG]** jej rodzina w Szanghaju czyni ją potencjalnym wektorem nacisku MSS — na razie nic się nie dzieje; jeśli kiedyś się zacznie, Xiaomei najpierw zamilknie. |

### Annika Brandt

| Pole | Wartość |
|---|---|
| Wiek | 26 (II 1986) |
| Wzrost | 175 cm |
| Budowa ciała | ok. 65 kg; ciało wspinaczki — szerokie plecy, wąskie biodra, zrogowaciałe palce |
| IQ | ~160 |
| Rola | „Herr Doktor”; Niemka (Monachium); wejście zagr. uniwersytecki — 6. (2 lata fizyki, TU München); ranking 11/497; doktorat z fizyki ciała stałego, **Max-Planck-Institut, Stuttgart** |
| Wygląd | jasny blond w kucyku, niebieskie oczy, piegi od słońca, zero makijażu; nie wie, że jest ładna; atrakcyjność 8/10; na zdjęciu: blondynka (prawo od środka) |
| Wiedza | intelektualna para Antoniny — fonony, kriostaty, rozmowy do 4:00; spokojna kotwica, gasi kłótnie; Toni przy niej mówi najwięcej o fizyce, najmniej o sobie; **zobaczy post Leny Hoffmeister i Bilda** wcześniej niż Antonina |
| Motywacje | punktualna co do minuty; wyjazdy w arkuszach; prawie nie przeklina; wspina się 4× w tygodniu. **Pokusa:** oferta Boscha (pieniądze, stabilizacja, Stuttgart) zamiast nauki. **Haczyk:** Stuttgart = Lena Hoffmeister i Bild |
| Sekrety | **[P]** złożyła podanie o postdok w Lozannie (EPFL, od X 2013) — „żeby nie wyglądało, że jadę za Toni”; „ktoś ze ścianki” — **Jonas**, pierwszy od trzech lat |
| Stosunek platoniczny do Antoniny | **+4** |
| Stosunek romantyczny do Antoniny | **0** [P] |
| Stan | **21 I (sesja 16, do 20:23 lok.):** Bild pod domem rodziców 5:30 CET (policja); „nobody leaves the group”; prowadzi log czasów i nazwisk dla prawnika<br>**20 I:** 18:15 CET: „Toni, did you change rooms?” |
| Jak grać | rzeczowa, ciepła pod spodem, fizyczka — rozmawiają o fononach; organizuje rzeczy niemiecką precyzją; zaczyna od „Toni,”. SMS-y po angielsku, pełne zdania. |

### Elif Aydın

| Pole | Wartość |
|---|---|
| Wiek | 26 (VIII 1986) |
| Wzrost | 166 cm |
| Budowa ciała | ok. 60 kg; krągła, zmysłowa [P] |
| IQ | ~148 |
| Rola | „la Sorcière”; Turczynka (Stambuł, Robert College); wejście zagr. uniwersytecki — 9. (2 lata mechaniki, Boğaziçi); ranking 64/497; dziś inżynierka struktur w **Airbus, Tuluza** |
| Wygląd | ciemne faliste włosy do łopatek, kajal, pełne usta, zachrypnięty głos; najbardziej „seksowna” w grupie — zmysłowa, świadoma ciała, ubiera się prowokacyjnie; atrakcyjność 8,5/10; na zdjęciu: ciemne faliste włosy (środek, lewo) |
| Wiedza | „edukatorka” Toni od 2008 — tłumaczy jej mężczyzn, seks i własne ciało; doradzała przy zakupach „do szuflady”; Toni ufa jej w sprawach ciała bardziej niż komukolwiek |
| Motywacje | mówi, czego inne nie powiedzą; rywalizuje z Clémence (chaos vs plan). **Pokusy:** Julien i autodestrukcja; powrót do Stambułu na warunkach ojca (pieniądze, wygoda) |
| Sekrety | biseksualna (otwarcie w grupie, nie w rodzinie); paczka Marlboro Light dziennie; tarot (talia Rider-Waite po babci); kłamie dla zabawy, nigdy w ważnych sprawach; **[P]** sypia z **Julienem** (żonaty inżynier z Tuluzy, ten od zdjęcia przy ekspresie) od listopada — stąd wie o obrączce „w piątki”; jej „6/10” to zasłona; ojciec (firma budowlana, blisko władzy) szykuje jej na lato „dobrego kandydata” w Stambule |
| Stosunek platoniczny do Antoniny | **+4** |
| Stosunek romantyczny do Antoniny | **+2** [P] — biseksualna; zmysłowy zachwyt ciałem Toni, głównie w żartach |
| Stan | **21 I (sesja 16, do 20:23 lok.):** baklava do Paris Match; „Atina” w tureckich tabloidach; „siktir git, Paris Match”; „it's her face on the cover” (bez urazy)<br>**20 I:** 17:02 CET: „clémence: 1 / parisian creeps: 0 😈” |
| Jak grać | głośna, ironiczna, pali za dużo, mistrzyni tarota i gorzkiej kawy; mówi wprost, co myśli o mężczyznach i o Francji; z Toni po angielsku i turecku; przy złości przechodzi na turecki. SMS-y z capslockiem i 😂🔥; głosówki. |

### Juliette Marchetti

| Pole | Wartość |
|---|---|
| Wiek | 26 (V 1986) |
| Wzrost | 168 cm |
| Budowa ciała | ok. 58 kg; szczupła, elegancka [P] |
| IQ | ~145 |
| Rola | „l'AFP”; Francuzka (Paryż, korsykańska rodzina); wejście krajowy uniwersytecki — 3. (licence de physique, UPMC Paris 6); ranking 203/497 (po 2. roku odpuściła na rzecz „l'IK”); po l'X porzuciła ścieżkę inżynierską — **dziennikarka działu przemysłu i technologii w „Le Monde”** |
| Wygląd | ciemne proste włosy, złote koła, czerwona szminka; paryska elegancja z korsykańskimi oczami — wygląda jak z okładki „Elle”; najczęściej podrywana w barach; atrakcyjność 8,5/10; na zdjęciu: ciemne włosy, złote koła (tył, środek) |
| Wiedza | powierniczka; wie pierwsza, mówi ostatnia; zna wszystkich w Paryżu; **[P]** od 2008 prowadzi prywatny notes „Toni” (trzy Moleskine'y 2008–2012; „dla siebie, na kiedyś”), m.in. IV 2008: „T. wróciła z Gujany. Kaszel. Jeszcze większa. Nikt nie pyta.” — grupa wie, że Juliette „pisze dziennik”, nie wie, że jest w nim głównie Toni |
| Motywacje | temat życia — „la Major polonaise”; konflikt lojalności to jej rdzeń: nie napisze o przyjaciółce bez jej zgody, ale nie skłamie naczelnemu. **Pokusa:** Thierry obiecuje jej awans, jeśli „pomoże” Raphaëlle |
| Sekrety | notes „Toni”; seryjna monogamistka (teraz: chłopak z herbaciarni, wt trzecia randka) |
| Stosunek platoniczny do Antoniny | **+4** |
| Stosunek romantyczny do Antoniny | **0** [P] — platoniczny zachwyt fizyczny („posąg”) |
| Stan | **21 I (sesja 16, do 20:23 lok.):** naczelny „Le Monde” poprosił, by nie pisała o grupie; Raphaëlle Dumas pisze; Fiona: „no offence”; Annika: „nobody leaves the group”; trzy tematy Dumas na wtorek rano Paryż<br>**21 I:** 9:50 CET: „Toni, nouvelle photo, polonaise cette fois. Wykop. En combinaison. Ça vient de l'intérieur, encore ?”.<br>**20 I:** 16:40 CET: @ParisPotins usunął tweeta; 9:00 18 I u naczelnego „Le Monde” (portret zamiast niej — dla Raphaëlle Dumas); zgoda Antoniny na rozmowę |
| Jak grać | ciekawska, szybka, idealistka zawodu; mówi pytaniami; pisze długie, eleganckie wiadomości po francusku; ristretto; w sprawach grupy umie milczeć. |

### Raphaëlle Dumas

| Pole | Wartość |
|---|---|
| Wiek | ok. 40 [P] |
| Wzrost | ok. 168 cm [P] |
| Budowa ciała | ok. 60 kg [P] |
| IQ | ok. 135 [P] |
| Rola | „Le Monde”, dział Planète/Sciences [P]; od 18 I autorka portretu Antoniny (zamiast Juliette) |
| Wygląd | [P] krótkie ciemne włosy, okulary, notes |
| Wiedza | **19 I** Antonina zgodziła się na rozmowę (przez Juliette); **20 I 10:01 CET** napisała: pn/wt, dowolna pora, autoryzacja cytatów, zdjęcia do wyboru |
| Motywacje | portret, który nie jest tabloidem; Thierry (naczelny) naciska |
| Sekrety | [?] — brak ustaleń |
| Stosunek platoniczny do Antoniny | **0** |
| Stosunek romantyczny do Antoniny | **0** |
| Stan | **21 I (sesja 16, do 20:23 lok.):** 22:15 CET WhatsApp: potwierdza środę 8:00 Paryż; trzy tematy jutro rano Paryż (śledztwo, życie prywatne, to, co Antonina chce powiedzieć sama)<br>**21 I:** rozmowa przez telefon umówiona na wt 22 I, 21:30 lok. (= śr 23 I, 8:00 Paryż), 1 h; portret przesunięty o dzień (Thierry) |
| Jak grać | profesjonalistka bez sensacji; pyta konkretnie; autoryzacja cytatów. |

### Sarah Benhamou

| Pole | Wartość |
|---|---|
| Wiek | 25 (ur. 27 I 1987 — urodziny za tydzień) |
| Wzrost | 163 cm |
| Budowa ciała | ok. 68 kg; krągła, szerokie biodra, duży biust [P] |
| IQ | ~140 |
| Rola | „Maman”; Francuzka (Marsylia); wejście krajowy CPGE, BCPST — 2. (Lycée Thiers); ranking 88/497; biotechnologia, start-up przy Institut Pasteur (Paryż); po BSPP; rodzina sefardyjska, tradycyjna, nieortodoksyjna; narzeczony **Yoni** [P], internista w Paryżu (Lariboisière); **zaręczona, ślub w lipcu 2013 w Marsylii** |
| Wygląd | niska, krągła, ciemne loki, wielkie oczy; głośny śmiech; „dziewczyna, z którą każdy chce się żenić”; atrakcyjność 7,5/10; na zdjęciu: ciemne loki (prawo) |
| Wiedza | zimna krew ratowniczki w kryzysie, histeria poza nim; gotuje dla dwudziestu; marsylski akcent; chce Toni na świadkową (*témoin*) |
| Motywacje | pielęgniarka Toni z IV 2008 (zupa, syrop); jedyna, przy której Toni pozwala się karmić. **Pokusa:** rzucić start-up (inwestor się wycofuje) i „po prostu mieć życie” |
| Sekrety | **[P]** w ciąży, ok. 7. tydzień (test 15 I); wie tylko Yoni; boi się matki Yoniego i daty ślubu; grupie powie „kiedy będzie pewna” — może przy kolacji 23 II; czuje się pomijana przez „rdzeń paryski” |
| Stosunek platoniczny do Antoniny | **+5** |
| Stosunek romantyczny do Antoniny | **0** [P] — platoniczny zachwyt fizyczny („posąg”) |
| Stan | **21 I (sesja 16, do 20:23 lok.):** „Mange, bébé.”; rodzice nikomu nic nie mówią; Voici dzwoniło do jej rodziców; Yoni też płaci<br>**20 I:** 19:30 CET: „dodo bien, Athena ❤️” |
| Jak grać | „mama” grupy — przytula, karmi, dzwoni zamiast pisać; marsylski temperament, śmieje się głośno. SMS-y z ❤️🌺 i mnóstwem wykrzykników. |

### Fiona MacLeod

| Pole | Wartość |
|---|---|
| Wiek | 27 (IV 1985) |
| Wzrost | 170 cm |
| Budowa ciała | ok. 72 kg; ciało rugbistki — mocne uda i ramiona [P] |
| IQ | ~143 |
| Rola | „Capitaine”; Szkotka (**Fife**, St Andrews); wejście zagr. uniwersytecki — 17. (2 lata fizyki, St Andrews); ranking 141/497; dziś inżynierka w Rolls-Royce (Derby); to ona „zaraziła” Toni Alestormem i folk metalem |
| Wygląd | ruda, piegi wszędzie, szeroki zawadiacki uśmiech; „girl next door” z Fife; atrakcyjność 7,5/10; na zdjęciu: ruda, piegi (skraj prawy) |
| Wiedza | **20 I 14:20 CET:** znalazła źródło wycieku: relacja Instagram @clara.dlx (usunięta, zrzut zapisany); zna termin koncertu Alestorm (19 III); gaelicki (jedyna żywa rozmówczyni Toni) |
| Motywacje | żarty o rumie i piratach; jedyna, która próbuje Toni „zaszarżować” jak na rugby („like tackling a lighthouse”). **Pokusy:** butelka; podpisać, co każą, i mieć spokój |
| Sekrety | pije za dużo — samotność w Derby, butelka wina co wieczór (grupa podejrzewa, nikt nie powiedział wprost); **[MG]** raport o pękniętej łopatce: przełożony naciska na złagodzenie wniosków przed certyfikacją; podpisała łagodniejszą wersję |
| Stosunek platoniczny do Antoniny | **+5** |
| Stosunek romantyczny do Antoniny | **0** [P] — platoniczny zachwyt fizyczny („posąg”) |
| Stan | **21 I (sesja 16, do 20:23 lok.):** Daily Mail dzwonił do jej mamy w Kirkcaldy; zapytała, czy „spy story” dotyczy Antoniny — usłyszała „No”; „and fuck off” do oświadczenia; „Alive. One word. Tomorrow.”<br>**20 I:** 14:20 „Found it. Original was an Instagram story from a Paris stylist, @clara.dlx. Deleted now. Screenshot saved. 🏴󠁧󠁢󠁳󠁣󠁴󠁿” |
| Jak grać | szkocka pogoda ducha i szkocki upór; z Toni gada po gaelicku; kwieciste przekleństwa; nigdy nie płacze publicznie; dudy. SMS-y po angielsku ze szkocizmami („aye”, „wee”), 🏴󠁧󠁢󠁳󠁣󠁴󠁿🍺; zazdrosna o koncert Alestorm (19 III). |

---

#### Inni z X2007 i z l'X

### Arnaud de Courcel

| Pole | Wartość |
|---|---|
| Wiek | ok. 27 [P] |
| Wzrost | ok. 183 cm [P] |
| Budowa ciała | ok. 80 kg [P] |
| IQ | ok. 145 [P] |
| Rola | **„le second”** — drugi w *classement de sortie* Francuzów (do Corps d'État), w rankingu ogólnym **3./497** — za Toni i Xiaomei (Z132), **z ogromną stratą** (Z185); stara rodzina (ojciec senator gaullista); Corps des Mines; dziś doradca techniczny w gabinecie premiera **Guaino** (przemysł, obronność) |
| Wygląd | [P] wypolerowany, jasny garnitur, idealna fryzura |
| Wiedza | od pięciu lat opowiada, że „przegrał z Polką, która potem pogardziła Mines”; wie, co mówi o Toni |
| Motywacje | zżera go, że „drugi” jest naprawdę trzeci, za dwiema cudzoziemkami z konkursu uniwersyteckiego; burzę medialną odbierze jako okazję |
| Sekrety | w Matignon szepnie, że „ta osoba jest dla państwa ryzykiem wizerunkowym”; adoruje Clémence |
| Stosunek platoniczny do Antoniny | **−2** |
| Stosunek romantyczny do Antoniny | **0** [P] |
| Stan | — |
| Jak grać | wypolerowany, uprzejmy, zimny; idealna francuszczyzna z kwiecistymi formułami; nigdy nie atakuje wprost. |

### por. Thomas Ravel

| Pole | Wartość |
|---|---|
| Wiek | ok. 27 [P] |
| Wzrost | ok. 183 cm [P] |
| Budowa ciała | ok. 80 kg [P] |
| IQ | ok. 135 [P] |
| Rola | jeden z nielicznych X2007, którzy poszli do wojska („X-Terre”); dziś porucznik **2e REP — od 11 I w Mali (Sirocco)**; FHM w Gujanie z Antoniną w 3e REI |
| Wygląd | [P] opalony, krótkie włosy, w mundurze |
| Wiedza | **[MG]** pamięta, że w II 2008 Toni „odeszła do innej jednostki” i wróciła po tygodniach, kaszląc; nigdy nie pytał |
| Motywacje | lojalność wobec starej koleżanki |
| Sekrety | [?] — brak ustaleń |
| Stosunek platoniczny do Antoniny | **+3** |
| Stosunek romantyczny do Antoniny | **+1** [P] |
| Stan | w Mali; jeśli przeczyta o burzy wokół niej — napisze jedno zdanie wsparcia, gdy będzie miał zasięg |
| Jak grać | żołnierz z poczuciem humoru, lojalny. |

### Maxime Vautrin

| Pole | Wartość |
|---|---|
| Wiek | ok. 27 [P] |
| Wzrost | ok. 178 cm [P] |
| Budowa ciała | ok. 72 kg [P] |
| IQ | ok. 130 [P] |
| Rola | założyciel paryskiego start-upu (aplikacja eventowa); fotograf zdjęcia z Bal de l'X; album „Bal de l'X 🔴” na Facebooku |
| Wygląd | [P] modna broda, koszula, okulary w rogowych oprawkach |
| Wiedza | **[MG]** album ma ustawienie „znajomi znajomych” — ryzyko wycieku zdjęcia |
| Motywacje | zasięgi; networking |
| Sekrety | [?] — brak ustaleń |
| Stosunek platoniczny do Antoniny | **0** |
| Stosunek romantyczny do Antoniny | **0** |
| Stan | gdy burza dotrze do Francji, wrzuci na LinkedIn „j'ai eu la chance d'étudier avec…” |
| Jak grać | networkingowy entuzjasta, lubi zasięgi; nie jest zły, jest bezmyślny. |

### Hugo Lemaire

| Pole | Wartość |
|---|---|
| Wiek | ok. 27 [P] |
| Wzrost | ok. 182 cm [P] |
| Budowa ciała | ok. 78 kg [P] |
| IQ | ok. 135 [P] |
| Rola | były przewodniczący Kès (samorząd) X2007; dziś konsultant strategii w **Zurychu** — w firmie, która właśnie zatrudnia Miko [P] |
| Wygląd | [P] opalony, uśmiech polityka |
| Wiedza | zna wszystkich |
| Motywacje | sieć kontaktów |
| Sekrety | [?] — brak ustaleń |
| Stosunek platoniczny do Antoniny | **+2** |
| Stosunek romantyczny do Antoniny | **+1** [P] |
| Stan | zaprosi Toni na „apéro X à Zurich”; Miko spotka go w IV jako przełożonego |
| Jak grać | czarujący polityk z natury, zna wszystkich. |

### Benoît Sarrazin

| Pole | Wartość |
|---|---|
| Wiek | ok. 27 [P] |
| Wzrost | ok. 178 cm [P] |
| Budowa ciała | ok. 72 kg [P] |
| IQ | ok. 140 [P] |
| Rola | X2007; cichy, po l'X wstąpił do **DGSE** (dyrekcja techniczna); szczegóły pracy pomijamy |
| Wygląd | [P] cichy, okulary, szary garnitur |
| Wiedza | **[MG]** od 16 I poproszony nieformalnie o „opinię koleżeńską” o Toni; czuje się z tym źle |
| Motywacje | lojalność wobec służby i koleżanki naraz |
| Sekrety | prośba o „opinię koleżeńską” |
| Stosunek platoniczny do Antoniny | **+1** |
| Stosunek romantyczny do Antoniny | **0** |
| Stan | nieobecny na zjazdach |
| Jak grać | małomówny, uprzejmy, nieobecny na zjazdach. |

### Maître Jacques Peyrol

| Pole | Wartość |
|---|---|
| Wiek | ok. 65 [P] |
| Wzrost | ok. 175 cm [P] |
| Budowa ciała | ok. 72 kg; sucha, wyprostowana postawa [P] |
| IQ | ok. 120 [P] |
| Rola | maître d'armes l'X; trenował Toni w latach 2007–10 |
| Wygląd | [P] siwy, smukły, dłonie szermierza |
| Wiedza | zna ją od najlepszej strony szermierczej |
| Motywacje | cierpliwość i dystans |
| Sekrety | [?] — brak ustaleń |
| Stosunek platoniczny do Antoniny | **+4** |
| Stosunek romantyczny do Antoniny | **0** |
| Stan | przyśle krótki liścik: „Garde haute, mademoiselle.” |
| Jak grać | stary szermierz, sentencje o dystansie i cierpliwości; pisze listy odręcznie. |

### Karim B. (`Karim_B`, WebiX)

| Pole | Wartość |
|---|---|
| Wiek | pełnoletni student X2007; dokładny wiek ? |
| Wzrost | ? |
| Budowa ciała | ? |
| IQ | ? |
| Rola | student l’X, nick Karim_B; podpisany autor M028 podczas Soirée du Vingt 14 VI 2008; odrębny od Karima Benalego z kręgu Basile’a |
| Wygląd | ? |
| Wiedza | zna publiczną odpowiedź Toni na M028; w katalogu występuje także pod V39 i T36; nie zna tajemnic MG |
| Motywacje | [P] chce wyjaśnić przykre brzmienie swojego pytania i sprawdzić, czy nie zepsuł relacji; zachowuje potrzebę obrony własnego obrazu |
| Sekrety | ? |
| Stosunek platoniczny do Antoniny | 0 [P]; znajomość kampusowa, do ustalenia w rozmowie |
| Stosunek romantyczny do Antoniny | ? |
| Stan | [P] 19 VI 2008, 21:14: rozpoczyna prywatną rozmowę WebiX o swoim pytaniu M028; odpowiedź Toni jeszcze nie nastąpiła. Teraźniejszość 2013 bez zmian. |
| Jak grać | [P] pisze po francusku (przekład na polski), małymi literami, krótko, potocznie; potrafi przeprosić, ale ma skłonność do tłumaczenia zamiaru; nie wymusza wybaczenia. Bez wiedzy o wnętrzu Toni. |

### Pauline Ferrand-Vasseix

| Pole | Wartość |
|---|---|
| Wiek | ok. 27 [P] |
| Wzrost | ok. 170 cm [P] |
| Budowa ciała | ok. 58 kg [P] |
| IQ | ok. 135 [P] |
| Rola | X2007 (fikcyjna); współzałożycielka **Kestrel Robotics** (drony inspekcyjne dla energetyki; Saclay); „Forbes 30 under 30”, gość BFM Business i konferencji TEDx; twarz „French Tech” |
| Wygląd | [P] jasne włosy, elegancki żakiet |
| Wiedza | zna rynek French Tech |
| Motywacje | zasięg; lubi Toni i chętnie by się z nią pokazała — co teraz byłoby kłopotem |
| Sekrety | [?] — brak ustaleń |
| Stosunek platoniczny do Antoniny | **+2** |
| Stosunek romantyczny do Antoniny | **0** |
| Stan | — |
| Jak grać | szybka, medialna, mówi sloganami („l'industrie de demain”), ale zna się na rzeczy. |

### Romain Delisle

| Pole | Wartość |
|---|---|
| Wiek | ok. 27 [P] |
| Wzrost | ok. 182 cm [P] |
| Budowa ciała | ok. 78 kg [P] |
| IQ | ok. 135 [P] |
| Rola | X2007 (fikcyjny); najmłodszy w promocji polityk: od 2012 doradca i rzecznik młodzieżówki Debout la République, felietonista „Le Figaro Vox”; szykuje start w wyborach municipales 2014 |
| Wygląd | [P] piękny uśmiech, garnitur |
| Wiedza | polityka francuska |
| Motywacje | kariera; o Toni powie publicznie „fierté de la promo”, a prywatnie wykorzysta ją jako argument o „talentach, które Francja traci na rzecz Szwajcarii” |
| Sekrety | prywatny cynizm wobec Toni |
| Stosunek platoniczny do Antoniny | **−1** |
| Stosunek romantyczny do Antoniny | **0** |
| Stan | — |
| Jak grać | ambitny suwerennista z pięknym uśmiechem. |

### Camille Rostand („Dr Phonon”)

| Pole | Wartość |
|---|---|
| Wiek | ok. 27 [P] |
| Wzrost | ok. 168 cm [P] |
| Budowa ciała | ok. 58 kg [P] |
| IQ | ok. 135 [P] |
| Rola | X2007 (fikcyjna); popularyzatorka nauki: blog i kanał wideo o fizyce (ok. 80 tys. subskrybentów — dużo jak na 2013), gość France Inter |
| Wygląd | [P] okulary, krótkie włosy, ekspresyjna |
| Wiedza | nagrała kiedyś odcinek o grafenie, w którym wspomniała „une camarade de promo” — po burzy widzowie skojarzą |
| Motywacje | popularyzacja nauki |
| Sekrety | [?] — brak ustaleń |
| Stosunek platoniczny do Antoniny | **+3** |
| Stosunek romantyczny do Antoniny | **0** |
| Stan | — |
| Jak grać | entuzjastka, mówi prosto i z humorem. |

### Kevin N'Diaye

| Pole | Wartość |
|---|---|
| Wiek | ok. 27 [P] |
| Wzrost | ok. 195 cm [P] |
| Budowa ciała | ok. 95 kg; wioślarz [P] |
| IQ | ok. 125 [P] |
| Rola | X2007 (fikcyjny); wioślarz, **finalista igrzysk w Londynie 2012** (dwójka podwójna), jedyny olimpijczyk X2007; dziś inżynier w EDF i ambasador sportu |
| Wygląd | [P] wysoki, barczysty |
| Wiedza | razem z Toni byli „sportowymi dziwadłami” promocji |
| Motywacje | sport, dobre słowo dla Toni |
| Sekrety | [?] — brak ustaleń |
| Stosunek platoniczny do Antoniny | **+3** |
| Stosunek romantyczny do Antoniny | **+1** [P] |
| Stan | publicznie stanie w jej obronie w jednym tweecie |
| Jak grać | serdeczny, prosty w obejściu. |

### Ingrid Larsen-Moreau

| Pole | Wartość |
|---|---|
| Wiek | ok. 27 [P] |
| Wzrost | ok. 172 cm [P] |
| Budowa ciała | ok. 60 kg [P] |
| IQ | ok. 140 [P] |
| Rola | X2007 (fikcyjna); ekonomistka, X + ENSAE; najmłodsza autorka raportów Conseil d'analyse économique, cytowana w „Les Échos”; komentatorka TV |
| Wygląd | [P] jasne włosy, spokojna twarz |
| Wiedza | ekonomia państwa |
| Motywacje | kariera analityczna |
| Sekrety | [?] — brak ustaleń |
| Stosunek platoniczny do Antoniny | **0** |
| Stosunek romantyczny do Antoniny | **0** |
| Stan | o Toni wypowiada się tylko „off the record” |
| Jak grać | chłodna, analityczna, ironiczna. |

**Uwaga MG:** realnych absolwentów X2007 nie używamy (nie da się rzetelnie sprawdzić, kto jest w promocji, a przypisywanie realnym ludziom działań w grze byłoby fikcją o żywych osobach). Powyższe postaci zajmują ich „miejsca” w medialnym ekosystemie Francji 2013.

#### Widzowie „Szkła Kontaktowego”

### Maciej z Warszawy

| Pole | Wartość |
|---|---|
| Wiek | ? (student) [P: ok. 21] |
| Wzrost | ? |
| Budowa ciała | ? |
| IQ | ? |
| Rola | widz „Szkła Kontaktowego” [N, Z145]; student filologii na Uniwersytecie Warszawskim; fikcyjny, nazwisko i wiek nieustalone |
| Wygląd | ? |
| Wiedza | nie ma prywatnej wiedzy o Antoninie |
| Motywacje | estetyka; obrona „sądu estetycznego” |
| Sekrety | [?] — brak ustaleń |
| Stosunek platoniczny do Antoniny | **+1** [P] |
| Stosunek romantyczny do Antoniny | **+2** [N + P] — zachwyt twarzą i kobiecymi kształtami; ambiwalencja wobec muskulatury i munduru |
| Stan | **20 I:** ok. 22:21 — połączenie zakończone; pod presją broni prawa do sądu estetycznego i przyznaje jednoczesną fascynację i zastrzeżenia; pełny tekst w `15-archiwum-mediow.md` |
| Jak grać | **[N + P]** kwiecisty, estetyzujący język; przywołuje Leonarda i Michała Anioła; [P] pod krytyką studia broni „sądu estetycznego”; nie uważa się za napastliwego. |

### Roman z Gdyni

| Pole | Wartość |
|---|---|
| Wiek | 62 |
| Wzrost | ? |
| Budowa ciała | ? |
| IQ | ? |
| Rola | widz „Szkła Kontaktowego” [P]; fikcyjny, emerytowany inżynier; nazwisko i specjalność nieustalone; wspomina żonę i wnuczkę rozważającą studia za granicą |
| Wygląd | ? |
| Wiedza | nie jest ekspertem od grafenu, nie zna prywatnych spraw Jelskiej |
| Motywacje | rzeczowość; lekkie rozgoryczenie losem polskiej nauki |
| Sekrety | [?] — brak ustaleń |
| Stosunek platoniczny do Antoniny | **0** |
| Stosunek romantyczny do Antoniny | **0** |
| Stan | **20 I:** ok. 22:26 — zakończył 90-sekundową rozmowę w audycji |
| Jak grać | rzeczowy, suchy humor; przyznaje się do niewiedzy. |

### Zofia z Łodzi

| Pole | Wartość |
|---|---|
| Wiek | ? |
| Wzrost | ? |
| Budowa ciała | ? (zwyrodnienia po czterdziestu latach dźwigania) |
| IQ | ? |
| Rola | widzka „Szkła Kontaktowego” [P]; fikcyjna; wiek, nazwisko i zawód nieustalone; mąż Wiesiek ma chore biodro |
| Wygląd | ? |
| Wiedza | zna tylko publiczne zdjęcia i audycję |
| Motywacje | spokojna starość; życzliwość wobec Antoniny |
| Sekrety | [?] — brak ustaleń |
| Stosunek platoniczny do Antoniny | **+1** |
| Stosunek romantyczny do Antoniny | **0** |
| Stan | **20 I:** ok. 22:28 — zakończyła 90-sekundowy telefon; Wiesiek obecny przy telewizorze, bez odgrywanej kwestii |
| Jak grać | pogodna, dosłowna, suchy humor bez intencji kabaretowych. Nie skarży się wprost; ciężar jej życia wychodzi w szczegółach. Męża lubi, irytuje ją jego powolność i niezręczne komplementy. |

---

## L. Postaci wzmiankowane (tło) [P]

*Osoby, które padają w kartach powyżej, ale nie występowały jeszcze w scenie. Dane [P]; uzupełniać przy pierwszym wejściu w kadr.*

### Lucas

| Pole | Wartość |
|---|---|
| Wiek | ok. 23 [P] |
| Wzrost | ok. 180 cm [P] |
| Budowa ciała | ok. 75 kg [P] |
| IQ | ok. 135 [P] |
| Rola | chłopak Gabi od roku; student medycyny, Lozanna; rodzice wiedzą, Tosia nie |
| Wygląd | [P] ciemne włosy, szeroki uśmiech, fartuch |
| Wiedza | zna Gabi i jej plany |
| Motywacje | wspólna przyszłość z Gabi |
| Sekrety | [?] — brak ustaleń |
| Stosunek platoniczny do Antoniny | **0** (nie zna jej osobiście) |
| Stosunek romantyczny do Antoniny | **0** |
| Stan | — |
| Jak grać | miły, spokojny student medycyny. |

### Yoni

| Pole | Wartość |
|---|---|
| Wiek | ok. 30 [P] |
| Wzrost | ok. 178 cm [P] |
| Budowa ciała | ok. 78 kg [P] |
| IQ | ok. 130 [P] |
| Rola | narzeczony Sarah Benhamou; internista w Paryżu (Lariboisière) |
| Wygląd | [P] ciemne włosy, ciepłe oczy |
| Wiedza | wie o ciąży Sarah (ok. 7. tydzień) |
| Motywacje | wesele, rodzina |
| Sekrety | ciąża Sarah (nikt inny nie wie) |
| Stosunek platoniczny do Antoniny | **+1** |
| Stosunek romantyczny do Antoniny | **0** |
| Stan | — |
| Jak grać | spokojny, praktyczny lekarz; boi się swojej matki. |

### Jonas

| Pole | Wartość |
|---|---|
| Wiek | 29 |
| Wzrost | ok. 183 cm [P] |
| Budowa ciała | ok. 80 kg; ratownik górski [P] |
| IQ | ok. 115 [P] |
| Rola | „ktoś ze ścianki” Anniki; ratownik górski z Allgäu; prosty i wesoły, pierwszy od trzech lat |
| Wygląd | [P] opalony, silne dłonie |
| Wiedza | wspinaczka |
| Motywacje | Annika |
| Sekrety | [?] — brak ustaleń |
| Stosunek platoniczny do Antoniny | **0** (nie zna jej) |
| Stosunek romantyczny do Antoniny | **0** |
| Stan | — |
| Jak grać | prosty, wesoły. |

### Julien (z Tuluzy)

| Pole | Wartość |
|---|---|
| Wiek | ok. 38 [P] |
| Wzrost | ok. 180 cm [P] |
| Budowa ciała | ok. 80 kg [P] |
| IQ | ok. 125 [P] |
| Rola | żonaty inżynier z Tuluzy; kochanek Elif od listopada; „ten od zdjęcia przy ekspresie” |
| Wygląd | obrączka noszona „w piątki” |
| Wiedza | [?] |
| Motywacje | [?] |
| Sekrety | romans z Elif |
| Stosunek platoniczny do Antoniny | **0** |
| Stosunek romantyczny do Antoniny | **0** |
| Stan | — |
| Jak grać | — |

### Antoine Chavenay

| Pole | Wartość |
|---|---|
| Wiek | ok. 30 [P] |
| Wzrost | ok. 180 cm [P] |
| Budowa ciała | ok. 76 kg [P] |
| IQ | ok. 125 [P] |
| Rola | syn Jean-Claude'a i Odile Chavenay; porucznik marynarki (Brest) [P] |
| Wygląd | [P] opalony, krótkie włosy |
| Wiedza | [?] |
| Motywacje | [?] |
| Sekrety | [?] — brak ustaleń |
| Stosunek platoniczny do Antoniny | **0** (nie zna jej) |
| Stosunek romantyczny do Antoniny | **0** |
| Stan | we Francji |
| Jak grać | — |

### Clara D. („@clara.dlx”)

| Pole | Wartość |
|---|---|
| Wiek | ok. 29 [P] |
| Wzrost | ? |
| Budowa ciała | ? |
| IQ | ok. 115 [P] |
| Rola | paryska stylistka; przyjaciółka Inès; Instagram @clara.dlx — z relacji powstał wyciek zdjęcia z tarasu (nd 20 I) |
| Wygląd | ? |
| Wiedza | zdjęcie od Inès („elle est immense”) |
| Motywacje | zasięg |
| Sekrety | relacja usunięta, zrzut zapisany przez Fionę |
| Stosunek platoniczny do Antoniny | **0** |
| Stosunek romantyczny do Antoniny | **0** |
| Stan | **20 I:** relacja usunięta; związana z @ParisPotins |
| Jak grać | — |

### gen. broni Mikołaj Puchała — dowódca Korpusu Sił Strategicznych [N, ZM46, ZM53, ZM56; karta [P] 18 X 2026]

| Pole | Wartość |
|---|---|
| Wiek | ok. 54 [P] |
| Wzrost | ok. 188 cm [P] |
| Budowa ciała | ok. 78 kg; szczupły [P] |
| IQ | ok. 130 [P] |
| Rola | dowódca KSS (fikcyjny); bratanek gen. dyw. (rez.) Franciszka Puchały (Klub Generałów RP) |
| Wygląd | [P] wysoki, szczupły, siwiejący, okulary w cienkich oprawkach; stalowo-niebieski mundur WPK |
| Wiedza | [P] test 18 I odwołany (M11); czeka na reakcję Waszyngtonu; D2 bez zmian |
| Motywacje | [P] procedury, ostrożność; unikanie improwizacji |
| Sekrety | [?] — brak ustaleń |
| Stosunek platoniczny do Antoniny | **0** (nie zna jej osobiście) [P] |
| Stosunek romantyczny do Antoniny | **0** [P] |
| Stan | **21 I:** po odwołaniu testu z 18 I (M11) czeka na reakcję Waszyngtonu; D2 bez zmian; prosi Markiewicza o rozmowę (M15) |
| Jak grać | **Profil [P]:** ostrożny, techniczny, dokładny; woli procedury niż improwizację; z „starą gwardią” (stryj Franciszek) ma więzi, ale nie bywa na ich obiadach.<br>**Mowa [P]:** spokojnie, z pełnymi zdaniami; do Markiewicza „panie generale”; pyta o rzeczy, o które nie chce pytać Szefa SG. |

### Recepcjonistka InterContinental Genève (imię nieustalone)

| Pole | Wartość |
|---|---|
| Wiek | ? |
| Wzrost | ? |
| Budowa ciała | ? |
| IQ | ? |
| Rola | [P] recepcjonistka obsługująca rezerwację i meldunek Antoniny 25 I (sesja 19 wpisy 38–48) |
| Wygląd | [P] granatowy kostium, plakietka; pozostałe szczegóły nieustalone |
| Wiedza | [P] nazwisko i dane meldunkowe, noc 25/26 I, Deluxe; rozpoznała nazwisko przy rezerwacji. Nie zna celu pobytu ani spotkania 20:00 |
| Motywacje | [P] sprawna obsługa gości i dyskrecja |
| Sekrety | [?] brak ustaleń |
| Stosunek platoniczny do Antoniny | [P] 0, zawodowy |
| Stosunek romantyczny do Antoniny | [P] 0 |
| Stan | **25 I ok. 14:04:** Antonina odebrała kartę i walizkę, podziękowała, przeszła do wind. Recepcjonistka odpowiada uprzejmie; obsługa meldunku zakończona.<br>**25 I ok. 14:03:** przygotowała kartę do 817, wskazała numer w etui i podała VIII piętro, windy i godziny śniadania 6:30–10:30. Karta na blacie, walizka obok, odbiór nieodegrany.<br>[P] 25 I ok. 14:00–14:01: po potwierdzeniu housekeepingu podchodzi do stolika w hallu i zawiadamia Antoninę o gotowym pokoju; karta i bagaż czekają do odbioru. Nie przekazano ich jeszcze |
| Jak grać | [P] **Osobowość:** uprzejma zawodowo, rzeczowa, dyskretna. **Mowa:** krótkie pełne zdania, zwraca się „madame”; bez komentarzy o medialnych sprawach gościa. **Pisanie:** formalne potwierdzenia rezerwacji. **Język:** francuski, zapis dialogów po polsku. **Nie robi:** nie ujawnia osobom trzecim danych i numeru pokoju. |

### Kelner restauracji InterContinental Genève (imię nieustalone)

| Pole | Wartość |
|---|---|
| Wiek | [P] ok. 35 |
| Wzrost | [P] ok. 178 cm |
| Budowa ciała | [P] szczupła |
| IQ | ? |
| Rola | [P] obsługa lunchu restauracji hotelowej na parterze, 25 I |
| Wygląd | [P] biała koszula, ciemna kamizelka |
| Wiedza | [P] widzi nową gościnię przy wejściu; nie zna jej nazwiska, numeru pokoju ani celu pobytu |
| Motywacje | [P] sprawna, dyskretna obsługa do końca serwisu |
| Sekrety | [?] brak ustaleń |
| Stosunek platoniczny do Antoniny | [P] 0, zawodowy |
| Stosunek romantyczny do Antoniny | [P] 0 |
| Stan | **25 I ok. 14:59 (wpis 74):** przyjął odmowę deseru i zamówienie podwójnego espresso, zabrał talerz i podał kawę. Bez rachunku.<br>**25 I ok. 14:56 (wpis 73):** po zjedzeniu obiadu przez Antoninę pyta o deser lub kawę; bez nowego zamówienia i bez rachunku.<br>**25 I ok. 14:41 (wpis 72):** podał antrykot medium rare z frytkami i osobną sosjerką pieprzową. Ok. 14:32 przeprosił za opóźnienie; przyczyna nieustalona. Antonina jeszcze nie je w zapisanej scenie.<br>**25 I ok. 14:24 (wpis 71):** odpowiada na podziękowanie, wraca do obsługi; herbata przyjęta, mięso jeszcze niepodane.<br>**25 I ok. 14:23 (wpis 70):** komplet zamówienia przyjęty; podał herbatę zimową 0,4 l, filiżankę i miód osobno. Poinformował, że mięso jest na patelni. Bez dalszego zamówienia.<br>**25 I 14:19 (wpis 69):** zanotował medium rare, wyjaśnia ofertę herbaty zimowej (0,4 l, czarna z pomarańczą, imbirem, cynamonem, goździkami; miód osobno); czeka na potwierdzenie napoju.<br>**25 I ok. 14:19:** zapisuje zamówienie antrykotu z frytkami; pyta o wysmażenie i napój, odpowiedzi nie uzyskał.<br>[P] 25 I ok. 14:18: wskazuje wolny dwuosobowy stolik przy oknie, prezentuje kartę i zaprasza; zamówienie jeszcze nieprzyjęte |
| Jak grać | [P] Rzeczowy, uprzejmy zawodowo; po francusku, dialog zapisany po polsku. Krótkie zdania o stoliku i posiłku, bez komentarzy o sylwetce lub medialnych sprawach. Pisanie: formalne zapisy zamówień. Nie ujawnia danych gości ani nie zgaduje ich nazwisk. |
