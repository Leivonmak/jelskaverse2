from pathlib import Path
from steeple_2010_build import build
p=Path('robocze/steeple-2010-04-source.txt');s=p.read_text(encoding='utf-8').replace('2010-04-11|21:04–22:37','2010-04-11|21:04–22:50').replace('2010-04-24|21:10–22:47','2010-04-24|21:10–23:00');p.write_text(s,encoding='utf-8',newline='\n')
build(4,s,
'''- [N] Francuzi X2009 wracają z FHM do regularnych zajęć; nowi korzystają ze zwykłej pomocy akademickiej, bez rozpisywania wszystkich kontaktów Toni.
- [N] Toni publicznie wskazuje MSc EPFL na czwarty rok i dalsze badania. Nie ogłasza jeszcze odmowy Mines; doktorat nie zaczyna się w kwietniu.
- [N/P] Khômiss X2008 z Verdierem przedstawia kandydatury, w tym Clémenta. Toni nie ma roli w ich wyborze. Liczba czterech kandydatów jest wykonawczym [P], nie retconem listy trzynastu z poprzedniego roku.
- [N] Symulacja cięć binetowych Delmas kończy się 20/20; nie jest rzeczywistą decyzją Kès. To drugie zadanie drugiego semestru i czwarte od stycznia.
- [P] Nowy krok Asmy 10 IV dotyczy statusu starych skarg po końcu mandatu. Toni odpowiada ostro także na pytanie o dostępność planu studiów. Sprawa pozostaje otwarta.''',
'''- Publiczny plan EPFL → „wybór już zatwierdzony” → „Mines od dawna odrzucone”; ostatnie dwa ogniwa są plotką, nie wiedzą uczestników.
- Symulacja odmowy części środków → „Toni obcięła binetom fundusze” → jej rzekomy powrót do władzy; żadnego realnego cięcia nie dokonała.
- Jedna pomoc Gaëlle → „jej kandydatka” → utożsamienie wsparcia akademickiego z poparciem wyborczym; nie ustalono poparcia Toni.
- Cudzy komentarz o ciele → złość Gaëlle → fałszywa legenda osobistego konfliktu z Toni.''',
'''- Cztery kandydatury są propozycją literacką w zakresie zatwierdzonego wyboru; nie wymuszono nowych nazwisk i kont. Zwycięzcą w maju będzie Clément zgodnie z wyborem autora.
- Kwoty i dokumenty zadania są fikcyjne. Nie dopisano decyzji Toni o realnych pieniądzach, nominacji czy zaakceptowaniu stanowiska Asmy.
- Wszystkie źródła szkolne/WebiX. Fotografia basenu pochodzi z oficjalnej galerii dorosłych uczestników; bez nagości, ukrytego kadru i intymnego materiału. TONI102 pozostaje szczelny.''')
