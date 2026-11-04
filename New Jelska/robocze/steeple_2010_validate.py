from pathlib import Path
from datetime import datetime,date
import re,json,hashlib,collections,shutil
root=Path.cwd();y3=root/'mg-wyciek-forum-x2007-rok-3.md';y2=root/'mg-wyciek-forum-x2007-rok-2.md'
s=y3.read_text(encoding='utf-8');needle='W lipcu zamknięto cztery zadania 20/20 z I–IV, bez dodatkowego wykonania w lecie.';assert s.count(needle)==1
b=root/'archiwum'/'kopie-steeple-2010'/(y3.stem+'-stan-koncowy-'+datetime.now().strftime('%Y%m%d-%H%M%S-%f')+'.md');shutil.copy2(y3,b)
s=s.replace(needle,'Do lipca wszystkie cztery zadania 20/20 z I–IV są zaliczone; bez dodatkowego wykonania w lecie.');y3.write_text(s,encoding='utf-8',newline='\n')
recs=[json.loads(p.read_text(encoding='utf-8')) for p in sorted((root/'robocze').glob('steeple-2010-??-kontrola.json'))]
entries=[e for r in recs for e in r['entries']];assert len(entries)==240
base=Path(recs[0]['backup']).read_text(encoding='utf-8').rstrip();assert s.startswith(base+'\n')
new=s[len(base):];assert new.count('*Metryka:')==240 and new.count('**Źródło i korzyść STEEPLE')==240
headings=re.findall(r'(?m)^##### ([CDTVF]\d+) —',new);assert len(headings)==240 and len(set(headings))==240
assert headings==[e['id'] for e in entries]
oldmanifest=json.loads((root/'robocze'/'steeple-2009-walidacja-koncowa.json').read_text(encoding='utf-8'))
y2expected=next(v for k,v in oldmanifest['sha256'].items() if k.endswith('rok-2.md'));assert hashlib.sha256(y2.read_bytes()).hexdigest()==y2expected
expected={'C':(297,394),'D':(222,297),'T':(189,233),'V':(98,105),'F':(89,101)}
for c,(lo,hi) in expected.items():assert [int(e['id'][1:]) for e in entries if e['typ']==c]==list(range(lo,hi+1))
for r in recs:
 n=r['count'];assert [r['bt'][str(b)] for b in range(1,5)]==[3*n//10,n//2,n//10,n//10]
 assert all(e['ordinary']/e['total']>=.6 for e in r['entries'])
 for e in r['entries']:
  assert e['hook'].strip() and '\u20ac' not in e['body'],e['id']
  assert not re.search(r'\b(?:201[1-9]|202\d)\b',e['body']),('przyszlosc',e['id'])
  assert not re.search(r'\b[CDTVF]\d{2,}\b',e['body']),e['id']
  if e['dt']>='2010-03-28':assert 'CEST' in new.split('##### '+e['id']+' —',1)[1].split('**BT:**',1)[0]
# Every required statement is checked against the source body, not only against its appendix.
quotes=json.loads((root/'robocze'/'steeple-2010-kwestie-toni.json').read_text(encoding='utf-8'))
bodies='\n'.join(e['body'] for e in entries)
fixed=[q['text'] for q in quotes if q['status'].startswith('N') and not q['text'].startswith('**')]
assert all(q in bodies for q in fixed)
assert "I don't have to be halal" in bodies
assert 'Trzy razy dwadzieścia. Dziękuję. Idę spać.' in bodies
assert 'Rezygnuję z Mines. Robię doktorat. Xiaomei, twoja kolej.' in bodies
assert new.count('### Stan po zamknięciu roku 3 (VII 2010)')==1
assert b'\r\n' not in y3.read_bytes()
# Cross-file unique headings, with pre-existing anomalies reported rather than repaired.
allheads=re.findall(r'(?m)^##### ([CDTVF]\d+) —',y2.read_text(encoding='utf-8')+'\n'+s)
dup={k:v for k,v in collections.Counter(allheads).items() if v>1}
assert not (set(dup)&set(headings)),dup
bt=collections.Counter(e['bt'] for e in entries);assert [bt[b] for b in range(1,5)]==[72,120,24,24]
lines=['# STEEPLE — raport MG: I–VII 2010','', '[P: redakcja na upoważnienie autora, 22 X 2026. Raport nie nadaje nowych numerów Z.]','',
'Zapisano 240 pozycji w §3.5–§3.11 roku 3 i końcowy stan po VII 2010. BT 72/120/24/24 = 30/50/10/10, identyczna proporcja w każdym miesiącu. Zastana treść roku 3 zachowana; rok 2 niezmieniony. Przed każdym blokiem sprawdzono obie numeracje i zrobiono kopię. Końcowe korekty dotyczą wyłącznie własnego dopisku: oznaczeń cytatów [N], dodania cytatów świadków do listy, rodzaju gramatycznego Bérénice Bouchet oraz zdania podsumowania o terminie zaliczenia zadań.','',
'| Blok | Liczba | Nowe ID |','|---|---:|---|']
for r in recs:lines.append(f"| {r['section']}, {r['month']:02d}/2010 | {r['count']} | {r['ranges']} |")
lines+=['','Łącznie: C297–C394; D222–D297; T189–T233; V98–V105; F89–F101. Pełne indeksy i każda nota STEEPLE są w pliku głównym oraz w miesięcznych wyciągach roboczych.','',
'## Kontrola i ograniczenia','',
'- 240 odrębnych nagłówków, 240 metryk i 240 konkretnych haków STEEPLE; ciągłość wszystkich pięciu numeracji bez luk w dopisku. Weryfikacja źródeł, kont, dat, stref czasu i dosłownych cytatów. Brak przyszłych dat w treści wiadomości. Starsze anomalie pozostawione poza tym zadaniem.',
'- Szum co najmniej 60% widocznych jednostek każdego wyciągu. Mianownik to wiadomości, punkty dokumentu lub ujęcia, nie liczba słów; nie doliczano niewidocznych wiadomości. To ograniczona miara tekstury, szczególnie przy długich cytatach [N].',
'- 7P opisuje tylko jawne postawy w wybranym materiale. Nie wyprowadza się reprezentatywnego rozkładu całej promocji z wrogiej selekcji lub z milczenia kont. Poziom 0 nie wchodzi do mediany 3S.',
'- Cztery zadania dodatkowe 20/20: Delmas i Vidal w I, Grandjean w II, Delmas w IV. Symulacja nie nadaje realnej władzy budżetowej; nauczanie tańca nie usuwa słabych umiejętności własnych.',
'- Wynik semestralny I oddzielony od trzeciej rocznej średniej i tytułu z VI. Soirée 19 VI bez prób i Q&A. Prywatna rozmowa Toni–Xiaomei po amphi nie jest ustalona ani źródłowana.',
'- 16 VII: dwa pamięciowe opisy świadków, nie pełny stenogram lub film. Ostatnie życzenie Toni szczere zgodnie z wyborem autora, bez wycofania zarzutów przez Asmę.',
'- TONI102 szczelny do 2013; 800 FRF zwrócone, 580 anulowane, brak zwycięzcy. Nie wymyślano jednakowych wpłat 49 kont ani intymnych faktów.',
'- Nie aktualizowano dawnego skróconego indeksu archiwalnego i nie księgowano Z. Nowe miesięczne indeksy kompletne.','',
'## Punkty do kontroli MG','',
'- Rozbieżność starszego R9: Dương Văn An wskazany jako X2008-253, właściwy wiersz ma X2008-025 i lokatę 253. Zgłoszono bez naprawiania spisu.',
'- Wykonawcze [P]: czterech kandydatów GénéK X2009, proporcje 58/21/13/8, przekazanie 28 VI, repertuar „Heroes” / „Un autre monde”, ograniczony zakres podpisów i dokumentów. Zwycięzca Clément i ramy wydarzeń pochodzą z odpowiedzi autora.',
'- Kraje/miasta dalszej formacji zatwierdzone; dokładne niepodane uczelnie Coquelicots pozostają nieustalone. Role R9 Érica i Dươnga pozostają rezerwą, bez wymuszania nowych scen lub dawnych dostępów.',
'- Starsze błędy nazwisk, euro, dawnych stref czasu i W5 zgłaszano w poprzednim raporcie 2009; nie poprawiano ich tutaj.','',
'## Wszystkie kwestie Toni do kontroli','',
f"{len(quotes)} zarejestrowanych kwestii: {sum(q['status'].startswith('P:') for q in quotes)} nowych [P] i {sum(q['status'].startswith('N') for q in quotes)} dostarczonych [N], w tym powtórzenia i cztery cytaty w relacjach świadków. Poniżej także drobne wpisy; brak ukrytych nowych deklaracji poza tym wykazem.",'']
for m in range(1,8):
 lines+=['',f'### {m:02d}/2010','']
 for q in quotes:
  if q['month']==m:lines.append(f"- **{q['id']} [{q['status']}]:** {q['text']}")
lines+=['','## Wynik technicznej kontroli','',f'- Zachowane numery końcowe: C394, D297, T233, V105, F101.',f'- Duplikaty nagłówków w latach 2–3: {json.dumps(dup,ensure_ascii=False)}.',f'- Końcowy SHA-256 roku 3: `{hashlib.sha256(y3.read_bytes()).hexdigest()}`.','- Osiem kopii przed blokami i główną kontrolą oraz dodatkowa kopia przed korektą zdania stanu; katalog `archiwum/kopie-steeple-2010/`.','']
report=root/'robocze'/'steeple-2010-raport-MG.md';report.write_text('\n'.join(lines),encoding='utf-8',newline='\n')
manifest=dict(total=240,bt=[bt[b] for b in range(1,5)],ranges=expected,toni_total=len(quotes),toni_new=sum(q['status'].startswith('P:') for q in quotes),toni_author=sum(q['status'].startswith('N') for q in quotes),preserved_year2=True,preserved_old_year3=True,duplicate_headings=dup,months=[dict(month=r['month'],section=r['section'],count=r['count'],ranges=r['ranges'],bt=r['bt'],minimum_noise=min(e['ordinary']/e['total'] for e in r['entries'])) for r in recs],sha256={str(p):hashlib.sha256(p.read_bytes()).hexdigest() for p in (y2,y3)},validation=['240 headings/metrics/hooks','IDs continuous and unique','BT exact per month','visible-unit noise >=60%','LF UTF-8','old year3 prefix unchanged','year2 checksum unchanged','fixed quotations present','school/WebiX sources only'])
(root/'robocze'/'steeple-2010-walidacja-koncowa.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2)+'\n',encoding='utf-8',newline='\n')
print(json.dumps({k:v for k,v in manifest.items() if k not in ('months','sha256')},ensure_ascii=False));print('Raport:',str(report));print('Wierszy roku 3:',len(s.splitlines()))
