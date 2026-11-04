# OPERACJA PUSTYNNA BURZA – WARGAME ALTERNATYWNY
## Dokument referencyjny | Arbiter: Claude

---

## I. KONTEKST FABULARNY

### Prolog

17 stycznia 1991 roku, godzina 02:38 czasu bagdadzkiego. Pierwsze śmigłowce AH-64 Apache z Task Force Normandy niszczą irackie stacje radarowe na zachodniej granicy. Nad Bagdadem pojawiają się zielone smugi ognia przeciwlotniczego — CNN transmituje na żywo. F-117 Nighthawk i pociski manewrujące Tomahawk uderzają w sieć dowodzenia i łączności Iraku. Operacja Pustynna Burza rozpoczęła się.

W tym wariancie alternatywnym Irak przyjmuje odmienną strategię obronną od historycznej. Zamiast rozciągniętej obrony wzdłuż granicy kuwejcko-saudyjskiej, siły irackie koncentrują się na dwóch rubieżach:

1. **Linia Eufratu** — główna rubież obronna, obsadzona przez dywizje piechoty i wzmocniona Gwardią Republikańską w rejonie Basry. Eufrat stanowi naturalną przeszkodę wodną, a miasta wzdłuż rzeki (Samawa, An-Nasiriyja, Basra) dają punkty oparcia.

2. **Kuwait City** — garnizon okupacyjny z umocnieniami miejskimi. Jednostki garnizonowe, bojówki i dywizje piechoty bronią miasta w terenie zabudowanym, wykorzystując przewagę obrońcy w walce miejskiej.

Francja, w tym wariancie, wysłała znacznie większe siły niż w rzeczywistości. Division Daguet rozrósł się do rangi korpusu (XXX), wyposażonego w czołgi Leclerc (historycznie jeszcze w fazie prób) i wzmocnionego dodatkowymi jednostkami kawalerii i rozpoznania. Daguet operuje na skrajnym zachodnim skrzydle koalicji.

Teatr afrykański (Gabon, Czad) jest **wyłączony z rozgrywki**.

---

## II. GRACZE

- **USER A** — kontroluje siły koalicji (USA, Wielka Brytania, Francja, Egipt, Syria, siły arabskie)
- **USER B** — kontroluje Irak
- **ARBITER (Claude)** — rozstrzyga wyniki działań, prowadzi narrację, rzuca kośćmi

---

## III. MECHANIKI GRY

### 1. Struktura tury

Każda tura = **6 godzin** czasu w grze.

```
1. Faza Wywiadu         — obie strony deklarują rozpoznanie
2. Faza Lotnicza        — USER A deklaruje uderzenia, USER B deklaruje OPL
3. Faza Lądowa          — obie strony deklarują ruchy i natarcia
4. Faza Rozstrzygnięcia — Arbiter ogłasza rezultaty
5. Faza Raportów        — Arbiter opisuje sytuację narracyjnie
```

### 2. Punkty Akcji (PA)

| Strona | PA/turę | Uzasadnienie |
|--------|---------|--------------|
| USER A (Koalicja) | **16** | Nadrzędność powietrzna, doskonała logistyka, łączność C2 |
| USER B (Irak) | **10** | Zdegradowana łączność, gorsza logistyka |

**Koszty PA:**

| Akcja | Koszt |
|-------|-------|
| Ruch jednej dywizji | 1 PA |
| Natarcie jedną dywizją | 2 PA |
| Skoordynowane natarcie (2+ dywizji na jeden cel) | 2 PA + 1 PA za każdą dodatkową |
| Uderzenie lotnicze (eskadra) | 1 PA |
| Obrona przeciwlotnicza (aktywna, per sektor) | 1 PA |
| Rozkaz taktyczny (zmiana szyku, zasadzka, odwrót) | 1 PA |
| Operacja specjalna (SOF, SCUD-hunting) | 2 PA |

### 3. Formuła rozstrzygnięcia walki

```
Wynik = (Moc atakującego + bonusy stałe)
      − (Moc obrońcy + bonusy stałe)
      ± Modyfikatory sytuacyjne
      + k6 (rzut Arbitra, 1–6)
```

**Modyfikatory sytuacyjne:**

| Warunek | Modyfikator |
|---------|-------------|
| Przewaga powietrzna atakującego | +2 |
| Obrona okopana/umocniona | +2 dla obrońcy |
| Nocne uderzenie z zaskoczenia | +1 atak |
| Zdegradowana łączność obrońcy | −1 obrona |
| Uderzenie z dwóch kierunków | +2 atak |
| Piasek, widoczność <1 km | −1 obie strony |
| SEAD (stłumienie OPL) | kasuje bonus OPL |

**Skala wyników:**

| Wynik | Rezultat |
|-------|----------|
| ≥+8 | Rozbicie — obrońca traci 50%+ mocy, wycofanie |
| +4 do +7 | Zdecydowane zwycięstwo — obrońca −3 mocy, oddaje sektor |
| +1 do +3 | Zwycięstwo taktyczne — obrońca −1 mocy, powolne cofanie |
| 0 | Pat — obie strony −1 mocy |
| −1 do −3 | Obrońca utrzymuje — atakujący −1 mocy |
| −4 do −7 | Odparcie — atakujący −3 mocy, cofnięty |
| ≤−8 | Klęska atakującego — atakujący −50% mocy |

### 4. Straty i stan dywizji

- Straty liczone w **punktach mocy bojowej**.
- Dywizja z mocą **0** = rozbita, usunięta z mapy.
- Dywizja z mocą **≤ połowa początkowej** = osłabiona, **−1 do rzutów**.

### 5. Lotnictwo

Uderzenia lotnicze zadają bezpośrednio **−1 do −3 mocy** celowi (zależnie od OPL i SEAD), niezależnie od walki lądowej.

### 6. Mgła wojny

- USER B **nie zna** pełnych ruchów USER A (deklaracje prywatne do Arbitra).
- USER A ma **przewagę rozpoznawczą** — Arbiter ujawnia ogólne pozycje irackie, ale nie szczegóły.
- **SCUD-y** — USER B deklaruje odpalenie Arbiterowi; Arbiter rzuca na skuteczność Patriotów.
- **Ukryte akcje** — USER B może raz na 3 tury zadeklarować akcję ukrytą (Arbiter nie ogłasza jej do rozstrzygnięcia).

### 7. Zasady specjalne

**Irackie podpalenie szybów naftowych** — USER B może zadeklarować w Kuwait City. Skutek: −1 dla lotnictwa koalicji w sektorze przez 4 tury, ale USER B traci 1 PA/turę (chaos logistyczny).

**SCUD vs Izrael** — każdy SCUD wystrzelony w Izrael uruchamia test polityczny (rzut Arbitra k6): na 1–2 Izrael wchodzi do wojny → −2 PA dla USER A przez 3 tury (zarządzanie kryzysem dyplomatycznym, ryzyko rozpadu koalicji arabskiej).

---

## IV. WARUNKI ZWYCIĘSTWA

### USER A (Koalicja) WYGRYWA — Irak poddaje się — gdy:
- **Kuwait City** przejęte w całości **ORAZ**
- **Linia Eufratu** przełamana **ORAZ**
- **Gwardia Republikańska** okrążona lub rozbita (moc = 0)

### USER A (Koalicja) PRZEGRYWA — wycofanie — gdy:
- Koalicja poniesie łącznie **≥10 punktów mocy bojowej** strat **ORAZ**
- Irak **utrzymuje Kuwait City** w momencie osiągnięcia tego progu

### USER B (Irak) WYGRYWA gdy:
- USER A zrealizuje warunki porażki (≥10 mocy strat + Kuwejt w irackich rękach)

---

## V. STAŁE MODYFIKATORY JEDNOSTEK

| Jednostka | Bonus | Uwagi |
|-----------|-------|-------|
| Division Daguet (GTIA-1 + GTR razem) | **+6** | Tylko gdy obie jednostki w tym samym sektorze |
| GTIA-1 (samodzielnie) | **+4** | — |
| GTR (samodzielnie) | **+4** | — |
| Gwardia Republikańska (wszystkie dywizje) | **+2** | — |
| Garnizon Kuwait City (GAR) | **+5** | Walka miejska, fortyfikacje |

---

## VI. ORDER OF BATTLE — STAN POCZĄTKOWY (17.01.1991, 02:38)

### KOALICJA (USER A)

#### Division Daguet (Francja) — skrajne zachodnie skrzydło, Tal'at

| Jednostka | Typ | Moc | Bonus | Lokalizacja |
|-----------|-----|-----|-------|-------------|
| **GTIA-1** (1er Groupement Tactique Inter-armes) | Pancerny (6e DLB + Leclerc) | **10/12** | +4 | **An-Nasiriyja (podejścia)** |
| **GTR** (Groupement Tactique de Reconnaissance) | Kawaleria/rozpoznanie | **9/10** | +4 | **An-Nasiriyja (podejścia)** |

#### Siły amerykańskie

| Jednostka | Typ | Moc | Lokalizacja |
|-----------|-----|-----|-------------|
| **101st Airborne** | Piechota powietrznodesantowa | **6/10** | Pustynia zachodnia |
| **24th Mechanized** | Zmechanizowana | **6/9** | Pustynia zachodnia |
| **1st Infantry** | Piechota | **11/11** | Południe od Rawdat Habbas |
| **3rd Armored** | Pancerna | **7/11** | Centrum Eufratu |
| **1st Cavalry** | Pancerna | **5/10** | Przy 3rd Armored |
| **1st Marine (1M)** | Piechota morska | **9/10** | Al-Dżahra |
| **2nd Marine (2M)** | Piechota morska | **9/10** | Al-Dżahra |
| **4th MEB** | Piechota morska (desant) | **7/8** | Kuwait City (Północ) |
| **82nd Airborne (BDE)** | Piechota spadochronowa | **2/6** | **WYCOFANA do Arabii Saudyjskiej** |

#### Siły kanadyjskie

| Jednostka | Typ | Moc | Lokalizacja |
|-----------|-----|-----|-------------|
| **1st Canadian (1CA)** | Pancerna | **8/10** | Pustynia zachodnia |

#### Siły brytyjskie

| Jednostka | Typ | Moc | Lokalizacja |
|-----------|-----|-----|-------------|
| **1st UK Armoured (1UK)** | Pancerna | **9/11** | **Al-Hamza (zasadzki)** |

#### Siły arabskie i sojusznicze

| Jednostka | Typ | Moc | Lokalizacja |
|-----------|-----|-----|-------------|
| **3. Dywizja** | Piechota | **6/6** | Centrum Eufratu |
| **4. Dywizja (egipska)** | Piechota | **6/6** | Pd-zach Kuwejt |
| **9. Dywizja (syryjska)** | Piechota | **6/6** | Centrum Eufratu |
| **ARAB (XXX)** | Siły arabskie (zbiorcze) | **11/11** | Kuwait City (Perymetr) |
| **1st (przy Kuwejcie)** | Piechota | **4/4** | Kuwait City (Perymetr) |

**Łączna moc koalicji: 146**

---

### IRAK (USER B)

#### Linia Eufratu — dywizje piechoty (rubież główna)

| Jednostka | Typ | Moc | Lokalizacja |
|-----------|-----|-----|-------------|
| **26. Dywizja** | Piechota | **0/4** | **ELIMINACJA (Samawa)** |
| **31. Dywizja** | Piechota | **0/4** | **ELIMINACJA (Samawa)** |
| **27. Dywizja** | Piechota | **0/4** | **ELIMINACJA (An-Nasiriyja — Daguet)** |
| **20. Dywizja** | Piechota | **1/4** | An-Nasiriyja (resztki po przeprawie) |
| **14. Dywizja** | Piechota | **2/4** | An-Nasiriyja (przeprawa z ciężkimi stratami) |
| **25. Dywizja** | Piechota | **0/4** | **ELIMINACJA (Pustynia zachodnia — 24th+101st)** |
| **45. Dywizja** | Piechota | **0/4** | ELIMINACJA (Al-Salman) |
| **30. Dywizja** | Piechota | **4/4** | Centrum |
| **7. Dywizja** | Piechota | **4/4** | Centrum |
| **16. Dywizja (FAW)** | Piechota | **4/4** | Przy Basrze (zachód) |

#### Gwardia Republikańska i elity — rejon Basry (bonus +2)

| Jednostka | Typ | Moc | Bonus | Lokalizacja |
|-----------|-----|-----|-------|-------------|
| **Hammurabi (HAM)** | Pancerna GR | **8/8** | +2 | Basra (zachód) |
| **51. Dywizja** | Zmechanizowana | **7/7** | — | Przy Hammurabi |
| **Nebukadnezar (NEBU)** | Piechota GR | **7/7** | +2 | Basra |
| **Tawakalna (TWK)** | Zmechanizowana GR | **7/7** | +2 | Basra (wschód) |
| **Medina (MADINA)** | Pancerna GR | **8/8** | +2 | Pd-wsch od Basry |
| **52. Dywizja** | Zmechanizowana | **7/7** | — | Rejon Basry (osłona Gwardii) |
| **17. Dywizja** | Pancerna | **7/7** | — | W drodze do Basry (odwrót) |
| **5. Dywizja** | Piechota (Zmech) | **0/7** | **ELIMINACJA (kontratak 3rd Armored/1st Cav)** |
| **6. Dywizja** | Piechota (Zmech) | **6/6** | — | W drodze do Basry (odwrót) |

#### Linia kuwejcka — garnizon i obrona

| Jednostka | Typ | Moc | Bonus | Lokalizacja |
|-----------|-----|-----|-------|-------------|
| **21. Dywizja** | Piechota | **0/4** | **ELIMINACJA (Al-Dżahra)** |
| **36. Dywizja** | Piechota | **0/4** | **ELIMINACJA (Al-Dżahra)** |
| **29. Dywizja** | Piechota | **0/4** | **ELIMINACJA (Al-Dżahra)** |
| **801. Brygada** | Piechota | **4/4** | — | Przy Kuwait City |
| **GAR (Garnizon)** | Garnizon/bojówki | **4/5** | **+5** | **Kuwait City** |
| **ZL** | Piechota | **5/5** | — | Przy Kuwait City |
| **B. Dywizja** | Piechota | **3/3** | — | Pd Kuwejt |
| **2. Dywizja** | Piechota | **4/4** | — | Pd Kuwejt |
| **8. Dywizja** | Piechota | **3/4** | — | Wybrzeże pd |
| **18. Dywizja** | Piechota | **4/8** | — | Wybrzeże pd |
| **15. Dywizja** | Piechota | **0/4** | **ELIMINACJA (Pd-zach Kuwejt)** |
| **11. Dywizja** | Piechota | **4/4** | — | Pd-wsch Kuwejt |
| **1. Dywizja** | Piechota | **4/4** | — | Pd-wsch Kuwejt |
| **19. Dywizja** | Piechota | **0/4** | ELIMINACJA (Lotnisko Kuwejt) |
| **3. Dywizja** | Piechota | **4/4** | — | Wschodni Kuwejt |

#### Inne

| Jednostka | Typ | Moc | Lokalizacja |
|-----------|-----|-----|-------------|
| **Rakiety SCUD-B** | Balistyczne | — | Zachodnia pustynia (mobilne) |
| **OPL (SA-2/3/6/8)** | Przeciwlotnicze | — | Sektory kluczowe |

**Łączna moc Iraku: ~171** (bez SCUD i OPL)

---

## VII. MAPA SEKTORÓW

```
[IRAK PÓŁNOCNY]     [BAGDAD]           [IRAN — neutralny]
                         |
[SAMAWA]            [AN-NASIRIYYA]      [AL-AMARA]
      |                  |                   |
[PUSTYNIA ZACH.]    [CENTRUM EUFRATU]   [BASRA — GR]
      |                  |                   |
[TAL'AT — Daguet]   [PÓŁ. KUWEJT]      [WYBRZEŻE]
      |                  |                   |
[RAFHA — 101st]     [KUWEJT CENTRUM]    [KUWAIT CITY — GAR]
      |                  |                   |
[RAWDAT HABBAS]     [PD KUWEJT]         [ZATOKA PERSKA]
      |                  |                   |
[HAFAR AL-BATIN]    [SIŁY ARABSKIE]     [FLOTA]
```

---

## VIII. HISTORIA KONFLIKTU

### Tura 0 — Przed godziną zero

Koalicja stacjonuje w Arabii Saudyjskiej od sierpnia 1990, budując siły w ramach Operacji Tarczy Pustynnej. Ultimatum ONZ minęło 15 stycznia. Dyplomacja zawiodła.

Irak, świadomy nadchodzącego ataku, podejmuje decyzję strategiczną odmienną od historycznej: zamiast rozpraszać siły wzdłuż granicy kuwejcko-saudyjskiej, koncentruje obronę na dwóch mocnych rubieżach — Eufracie i samym Kuwait City. Gwardia Republikańska zajmuje pozycje w rejonie Basry jako odwód operacyjny i obrona drugiej linii. Garnizon w Kuwait City przygotowuje się do walki miejskiej.

Francja, pod naciskiem prezydenta Mitterranda, wysyła znacząco więcej sił niż planowano. Division Daguet, rozrośnięty do rangi korpusu, otrzymuje czołgi Leclerc z przedseryjnej partii i dodatkowe jednostki kawalerii. Zostaje rozmieszczony na skrajnym zachodnim skrzydle — jego zadaniem będzie głębokie obejście irackiego ugrupowania.

### Tura 5 — 18 stycznia 1991, 08:38–14:38 — ZAKOŃCZONA

Upadek Samawy (zobliterowanie 26. i 31. DP) i odcięcie linii komunikacyjnych na Eufracie. Zdobycie Al-Dżahry przez Koalicję i zamknięcie kotła w Kuwait City. Krwawy kontratak iracki na pozycje 82. DP — 43 spadochroniarzy w niewoli. Publiczna prezentacja jeńców w irackiej telewizji wywołuje wstrząs w Waszyngtonie.

### Tura 6 — 18 stycznia 1991, 14:38–20:38 — ZAKOŃCZONA

Luna-M na zgrupowania Koalicji. Eliminacja 25., 27. i 5. DP. Daguet dociera pod An-Nasiriyję. Irak wysadza ostatni most, odwraca się za Eufrat. 1UK wchodzi w zasadzki w Al-Hamzie. Eskalacja do terroru międzynarodowego. Skutek odwrotny do zamierzonego — opinia publiczna USA radykalizuje się.

**Czekamy na deklaracje Wywiadu Tury 7.**

---

## IX. REJESTR TUR

| 1 | 17.01 02:38–08:38 | Zakończona | Uderzenie lotnicze, odwrót Iraku z Kuwejtu, podpalenie szybów | 0 | 5 (Lotnictwo) |
| 2 | 17.01 08:38–14:38 | Zakończona | Atak SCUD, upadek Al-Salman, wejście sił arabskich do Kuwejtu | 1 (KC-135) | 8 (Lotnictwo/45. DP) |
| 3 | 17.01 14:38–20:38 | Zakończona | Bitwa o Al-Salman, manewr VII Korpusu, upadek 19. DP | 4 (101st/GTR/1CA) | 8 (Lotnictwo/SCUD/19. DP) |
| 4 | 18.01 02:38–08:38 | Zakończona | Operacja Potop, okrążenie Kuwait City, konsolidacja Eufratu | 8 (1/3 DPanc/101st) | 14 (Lotnictwo/Kuwejt) |
| 5 | 18.01 08:38–14:38 | Zakończona | Upadek Samawy i Al-Dżahry, kontratak na 82nd, 43 jeńców | 6 (Marines/82nd/24th) | 18 (26/31/21/29/36/15 DP) |
| 6 | 18.01 14:38–20:38 | Zakończona | SCUD na Dhahran (28 KIA), zniszczenie mostów, dominacja powietrzna | 28 KIA (Dhahran) | Lotnictwo IZ-ELIMINACJA |

**Łączne straty USER A:** 13+28 KIA Dhahran ⚠️ KRYZYS POLITYCZNY
**Status Kuwait City:** Fortress City (podminowane, brak osłony dymnej — wygasła)
**Status Eufrat:** PRZECIĘTY — cztery mosty zniszczone, jeden uszkodzony (An-Nasiriyja)
**Status 27., 20., 14. DP:** ODCIĘTE od zaopatrzenia z Bagdadu
**Status Gwardii Republikańskiej:** pełna gotowość, Basra
**Status Szybów Naftowych:** PŁONĄ (sektor Południowy i Centrum Kuwejtu)
**Status Lotnictwa Iraku:** WYELIMINOWANE (F-117/AWACS search-and-destroy)

**Aktywne statusy specjalne:**
- **Zasłona Dymna (Kuwejt):** -1 dla lotnictwa koalicji w sektorach Kuwejt Pd/Centrum/City (1 tura).
- **Pola Minowe:** -1 mocy dla pierwszej jednostki koalicji wchodzącej do sektorów: Pd Kuwejt, Kuwejt Centrum, Samawa-Pd.
- **Iraka PA:** -1 PA/turę na stałe (podpalenie szybów).
- **Logistyka VII Korpusu:** Uszkodzona w Hafar al-Batin. Koalicja -1 PA w T4.
- **Mosty na Eufracie:** WSZYSTKIE ZNISZCZONE. Cały Eufrat jest barierą — przeprawa wymaga pontonowania lub zdobycia przyczółka.
- **Dominacja Powietrzna:** TOTALNA nad całym Irakiem.
- **Eufrat — Łuna-M:** Irak aktywował artyleryjskie rakiety Łuna-M z głowicami kasetowymi. Skuteczne ataki na zgrupowania. Brak efektywnego przeciwdziałania Patriot.
- **Terroryzm międzynarodowy:** Irak eskaluje do atakuów w krajach zachodnich. Efekt ODWROTNY — opinia publiczna USA jednoczy się. Kara Dhahran redukowana: Koalicja -1 PA w T7 zamiast -2.
- **Rzeka pod napięciem:** Linia Eufratu zaminowana elektrycznie. -2 mocy przy próbie przeprawy bez neutralizacji.
- **Fedaini i Peszmerga (+cywile z bronią):** +2 do obrony irackich sektorów miejskich.
- **Irak PA:** -1 PA/turę na stałe (podpalenie szybów).

*Dokument aktualizowany przez Arbitra po każdej turze.*
