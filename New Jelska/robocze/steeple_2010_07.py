from pathlib import Path
from steeple_2010_build import build
p=Path('robocze/steeple-2010-07-source.txt');s=p.read_text(encoding='utf-8').replace('Dwie różne major','Dwa tytuły, dwie funkcje');p.write_text(s,encoding='utf-8',newline='\n')
build(7,s,
'''- [N] 14 VII Toni w zwykłym szyku X2007; sztandar niesie major d'entrée według tradycji. Bez udawanej degradacji względem jej funkcji z 2008.
- [N] Ostatnie spotkanie z Asmą 16 VII. Toni spokojna i ostra, końcowe „Powodzenia” szczere; Asma nie wybacza automatycznie i nie wycofuje skarg.
- [N/P] Źródłem są dwie wiadomości świadków spisane tego samego wieczoru: Mathilde zna początek, Capucine końcówkę. Żadnego nagrania, pełnego stenogramu ani wiedzy jednej osoby o całym zajściu. Cztery dostarczone kwestie Toni zachowane dosłownie we wspomnieniach.
- [N] TONI102: do 20 VII zwrot 800 FRF gotówki i anulowanie 580 FRF zobowiązań, brak zwycięzcy. 49 kont, zamknięte archiwum; pierwszy wyjściowy wyciek dopiero w 2013.
- [N] Toni wyjeżdża do Lozanny 21 VII; od IX MSc EPFL. Kontakty Coquelicots pozostają na WebiX, bez wspólnego miejsca zamieszkania. X2007 kończy pobyt w Palaiseau.''',
'''- Inny niosący sztandar → „Toni odsunięta” → kara za odmowę Mines; źródła podają odmienną podstawę funkcji.
- Dwie pamięciowe relacje → „pełny zapis awantury” → fikcyjne nagranie; brak źródła audio jest jawny.
- Szczere „Powodzenia” → „ugodzona skarga” → „Asma wszystko odwołała”; żaden z dwóch dalszych wniosków nie następuje.
- Zwrot puli → „wypłata zwycięzcy” → fałszywe intymne zdarzenie; zamknięta księga wyklucza taką interpretację.
- Rozjazd przyjaciółek → „grupa rozbita przez Toni” albo „tajna sieć w kilku miastach”; grupa pozostaje kontaktem, nie nową strukturą instytucjonalną.''',
'''- Żart o dwóch lub trzech godzinach do Lozanny pozostaje dostarczonym zdaniem autora, nie informacją o realnym rozkładzie kolei. Nie poprawiano cytatu.
- Ruch wakacyjny maleje: większość pozycji to dni przed rozjazdem i kilka źródeł tego samego zdarzenia; po 21 VII nie ma codziennego chóru obecnych na kampusie. Katalog selekcji nie jest miarą pełnego ruchu serwera.
- Zwroty zakładu są zagregowane z pokwitowań, bez wymyślania nieustalonego podziału 800 FRF na 49 osób. Potwierdzono sumę, nie sugerowano jednakowych wpłat każdego konta.
- Trzecia roczna średnia, major i relacja z amphi pozostają zamknięte faktami; część osobistych zarzutów pozostaje otwarta. Do listy kwestii Toni trzeba doliczyć cztery dosłowne cytaty obecne w pamięciowych relacjach świadków, nie w wiadomościach z jej konta.''')
