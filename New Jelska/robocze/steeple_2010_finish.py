from pathlib import Path
from datetime import datetime
import json,re,hashlib,shutil
root=Path.cwd();target=root/'mg-wyciek-forum-x2007-rok-3.md'
records=[json.loads(p.read_text(encoding='utf-8')) for p in sorted((root/'robocze').glob('steeple-2010-??-kontrola.json'))]
base=Path(records[0]['backup']).read_text(encoding='utf-8');old=target.read_text(encoding='utf-8');assert old.startswith(base.rstrip()+'\n')
prefix=base.rstrip();new=old[len(prefix):]
fixed=[
"I don't have to be halal",
'Dobra. Termin?',
'Miko wróciła. Tym razem tańczy z Fioną, nie ze mną. Dla dobra wszystkich stóp.',
'Nie jestem już GénéK. Pytajcie tego, kto ma kepi.',
'Trzy razy dwadzieścia. Dziękuję. Idę spać.',
'Rezygnuję z Mines. Robię doktorat. Xiaomei, twoja kolej.',
'Tytuł majora wynika z ocen, a oceny z prac sprawdzonych dwa razy, na ślepo. Jeśli ktoś uważa, że to folwark, niech pokaże, gdzie dostał gorszą ocenę za lepszą pracę. Jak nie pokaże, zostaje zazdrość, a na nią w Republice nie ma przepisu.',
'Trzy lata, trzy imprezy. Dziękuję, że tym razem nie kazaliście mi niczego udowadniać. Za was, nie za mnie. À vingt.',
'Wyjeżdżam. Ty zostajesz jeszcze rok. Chciałaś mi coś powiedzieć w twarz, to masz ostatnią okazję.',
'Nie zmienię zdania o laïcité. Ty nie zmienisz zdania o mnie. Przynajmniej w tym jesteśmy równe.',
'We Francji możesz się modlić, zasłaniać i mnie nie lubić. Do niczego z tego nie potrzebujesz mojej zgody. Ja twojej też nie.',
'Powodzenia na ostatnim roku. Serio.',
'Nie płaczcie. Lozanna jest dwie godziny pociągiem. Albo trzy, jak jedzie Fiona.'
]
# Corrections concern only the present agent's new appendices and one grammatical form.
newlines=[]; corrected_labels=0
for line in new.splitlines():
 if line.startswith('- **') and '[P: subagent, do kontroli MG]' in line and any(x in line for x in fixed):
  line=line.replace('[P: subagent, do kontroli MG]','[N]');corrected_labels+=1
 newlines.append(line)
new='\n'.join(newlines)+'\n'
needle='**bbouchet** (22:03): Wydrukowałem zasady.';assert new.count(needle)==1
new=new.replace(needle,'**bbouchet** (22:03): Wydrukowałam zasady.')
last='- **T232 [N]:** **toni31_X07** (09:44): '+fixed[-1];assert new.count(last)==1
witness='\n'.join('- **'+ident+' [N; pamięciowa relacja świadka, bez nagrania]:** '+q for ident,q in [('C390',fixed[8]),('C390',fixed[9]),('C391',fixed[10]),('C391',fixed[11])])
new=new.replace(last,last+'\n'+witness)
state=r'''
### Stan po zamknięciu roku 3 (VII 2010) — TYLKO MG

[N: wynik, wybory i kierunki zatwierdzone przez autora; P: wykonawcze daty, zapisy i uchwyty do dalszej redakcji. Stan szkolny na 31 VII 2010; kolumny „2013” są wiedzą MG.]

**Toni:** kończy pobyt w Palaiseau i wyjeżdża do Lozanny 21 VII. Trzy roczne średnie 20,00, ranking końcowy 1/497, major de promotion od 17 VI. Odmowa Mines pada publicznie 24 VI. Od IX 2010 czwarty rok jako MSc EPFL; dalszy doktorat w ścieżce formacji uzupełniającej, z zachowaniem dyspozycji IP. Brak nowego mandatu Khômiss i roli w intégration następnego rocznika.

| Osoba | Dalszy kierunek po Palaiseau [N; bez wymyślania niepodanych uczelni] |
|---|---|
| Xiaomei | Paryż, matematyka stosowana i finansowa; 2. w rankingu |
| Clémence | Mines, ostatnie miejsce po odmowie Toni; 19. w rankingu |
| Annika | Niemcy, fizyka ciała stałego; 11. |
| Elif | Tuluza, mechanika i konstrukcje; 64. |
| Sarah | Paryż, biologia i biotechnologia; 88. |
| Fiona | Wielka Brytania, mechanika i energia; 141. |
| Juliette | Paryż, dokończenie wymaganej formacji i kierunek dziennikarski; 203. |
| Arnaud | Mines; 3. w rankingu, prywatna krytyka odmowy Toni zachowana |
| Ravel | Dalsza ścieżka wojskowa; bez przenoszenia późniejszej jednostki i stopnia do lipca 2010 |

**Co pozostaje otwarte:**
- **Asma:** konflikt nie wygasa. Po eseju o „folwarku”, sporze o tytuł i ostatniej rozmowie 16 VII część indywidualnych zarzutów pozostaje sporna. Szczere pożegnanie Toni nie oznacza ugody. Dwa źródła C390–C391 są relacjami pamięciowymi o różnych fragmentach, bez nagrania.
- **Rejestr skarg:** ogólne zasady przyjęte 28 VI, rozdzielają potwierdzenie, odpowiedź i rozstrzygnięcie; wypowiedź oficjalna i prywatna wymagają jasnego oznaczenia. Brak zbiorowego oczyszczenia i brak sankcji zmieniającej akademicki wynik.
- **Marta:** działa wyłącznie na WebiX. Jej polityczna rama pozostaje materiałem prywatnym i szkolnym; żadnych polskich mediów przed 2013.
- **Khômiss:** Clément wybrany w maju, kepi przejmuje od Verdiera 28 VI. Własne obietnice zgody i procedur pozostają do sprawdzania. Dawny podpis Toni pod kartą zasad nie zastępuje bieżącej odpowiedzialności nowego GénéK.
- **TONI102:** zwrot całych 800 FRF i anulowanie 580 FRF zamknięte do 20 VII; zero gotówki i należności, bez zwycięzcy. Pokwitowania i rozmowy zachowane w 49 kontach. Toni ani salony zewnętrzne nie dowiadują się o nim w 2010. Pierwsze wyjście archiwum poza grupę to wyciek 2013.
- **Coquelicots i salony:** kontakt trwa po rozjeździe. Filles de l’X zachowuje 320 dostępów starszych i X2009, bez domniemania aktywności; Les grandes zachowuje trzy grupy potrzeb. Matrices nie jest jednolitym obozem. W lipcu zamknięto cztery zadania 20/20 z I–IV, bez dodatkowego wykonania w lecie.

**Uchwyty X2009 — do 2013, wyłącznie MG:**

| Osoba / konto | Status I 2013 ze spisu | Co może wrócić z 2010 [P] |
|---|---|---|
| Augustin Richard / `augustin.richa` | Badawczy MSc ENSAE, ocena inwestycji | Odpowiedzialność za podpisy, daty, granicę świadka i redaktora IK |
| Clément Tournier / `clement.tourn` | Czwarty rok Chimie, kataliza | Program i własne obowiązki GénéK, T217 oraz T228 |
| Coline-Océane Durand / `cdurand` | Staż PSA, Vélizy | Mylenie autorstwa zdjęcia i redakcji podpisu; nie była na balu |
| Gaëlle Fouquet / `gaelle_F` | Staż Saint-Gobain, Cavaillon | Pomoc Toni, C344; sprzeciw wobec etykiety osobistego zaplecza |
| Ananya Kulkarni / `ananya_X09` | Cherbourg, bezpieczeństwo instalacji | Odmowa tłumaczenia cudzych intencji i roli rzeczniczki |
| Nadine Essomba / `nadine_X09` | Badawczy MSc Ponts, mechanika gruntów | Konkretna pomoc naukowa bez lojalności politycznej i bez zgody na kopiowanie |
| Min Wu / `mwu` | Badawczy MSc matematyki stosowanej, równania różniczkowe | Korekty dat i roczników; pierwsze pytanie o anonimowość oceny |
| Marta Wierzbicka / `marta.wierz` | Badawczy MSc ENSAE, analiza transportu | Słabo przemyślane żarty przy dokumentach, bez utożsamiania z Chmielewską |

**Uchwyty X2008 — kontynuacja R9, bez dopisywania im wiedzy wstecz:**

| Osoba | Rola do 2013 / zachowany punkt zaczepienia |
|---|---|
| Piotr Rutkowski | Polski świadek własnych odbiorów i obiegu szkolnego; nie świadek rozmowy 16 VII |
| Katarzyna Majewska | Posiadaczka D63 według R9; ograniczony podpis i sprzeciw wobec fałszywej arytmetyki oskarżeń |
| Marta Chmielewska | Publicystka/blogerka dopiero w roli 2013; zachowane wcześniejsze teksty WebiX |
| Barbara Zawadzki | R9 „sufit 4,5”; pragmatyczne rozmowy, bez nowego domniemania intymnego faktu |
| Asma Benkirane | Własne listy i granice zgód; bez związku z realną rodziną o zbieżnym nazwisku |
| Harriet Ainsworth | Warunkowe poparcie procedury; anglojęzyczne źródło z własnymi zastrzeżeniami |
| Matthieu Verdier | Przekazanie funkcji i dokumentów; major X2008 oraz Mines to późniejsza rola R9, nie wynik z lipca 2010 |
| Olivier Cordeau | Krytyka zamiany skargi w plebiscyt i zawiedziony insider; nie zna automatycznie TONI102 |
| Éric Mbelek | Rezerwa R9 do analizy obrazu; nowe bloki nie ustanawiają jego wcześniejszego wglądu do prywatnych galerii |
| Dương Văn An | Rezerwa R9: AX „Mémoire des promos”; bez dopisywania rozmów lub dostępu w 2010 |

**Rozbieżność do MG, bez zmiany starszego tekstu:** R9 identyfikuje Dương Văn Ana jako X2008-253; właściwy wiersz spisu ma ID X2008-025 oraz lokatę 253. Nie rozstrzygnięto tego przez cichą poprawkę. Nie aktualizowano starszego skróconego indeksu `archiwum/lista-materialow-wyciek-x2007.md` ani rejestru decyzji Z. Pełny dopisek ma własne indeksy miesięczne.

---
'''
backup=root/'archiwum'/'kopie-steeple-2010'/(target.stem+'-kontrola-koncowa-'+datetime.now().strftime('%Y%m%d-%H%M%S-%f')+'.md');shutil.copy2(target,backup)
assert target.read_text(encoding='utf-8')==old
final=prefix+new.rstrip()+'\n\n'+state.lstrip();target.write_text(final,encoding='utf-8',newline='\n')
# Bring working excerpts and quote lists into line with the corrected final appendices.
all_toni=[]
for r in records:
 month=r['month'];mp=root/'robocze'/f'steeple-2010-{month:02d}.md';mt=mp.read_text(encoding='utf-8')
 lines=[]
 for line in mt.splitlines():
  if line.startswith('- **') and '[P: subagent, do kontroli MG]' in line and any(q in line for q in fixed):line=line.replace('[P: subagent, do kontroli MG]','[N]')
  lines.append(line)
 mt='\n'.join(lines)+'\n'
 if needle in mt:mt=mt.replace(needle,'**bbouchet** (22:03): Wydrukowałam zasady.')
 if month==7:assert mt.count(last)==1;mt=mt.replace(last,last+'\n'+witness)
 mp.write_text(mt,encoding='utf-8',newline='\n')
 for ident,status,line in r['toni']:
  status='N' if any(q in line for q in fixed) else 'P: subagent, do kontroli MG'
  all_toni.append(dict(month=month,id=ident,status=status,text=line))
for ident,q in [('C390',fixed[8]),('C390',fixed[9]),('C391',fixed[10]),('C391',fixed[11])]:all_toni.append(dict(month=7,id=ident,status='N; cytat w pamięciowej relacji świadka',text=q))
(root/'robocze'/'steeple-2010-kwestie-toni.json').write_text(json.dumps(all_toni,ensure_ascii=False,indent=2)+'\n',encoding='utf-8',newline='\n')
print(json.dumps(dict(corrected_quote_labels=corrected_labels,toni_total=len(all_toni),toni_new=sum(x['status'].startswith('P:') for x in all_toni),toni_author=sum(x['status'].startswith('N') for x in all_toni),backup=str(backup),sha256=hashlib.sha256(target.read_bytes()).hexdigest()),ensure_ascii=False))
