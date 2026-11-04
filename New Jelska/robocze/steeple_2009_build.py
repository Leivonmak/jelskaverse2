from pathlib import Path
import re, json, hashlib, shutil
from datetime import date, datetime
ROOT=Path(__file__).resolve().parent.parent
DAYS=['pn','wt','śr','czw','pt','sob','nd']
MONTHS={5:'V',6:'VI',7:'VII',8:'VIII',9:'IX',10:'X',11:'XI',12:'XII'}
Y2=ROOT/'mg-wyciek-forum-x2007-rok-2.md'
Y3=ROOT/'mg-wyciek-forum-x2007-rok-3.md'
AUTH='[N: ramy i decyzje autora w czacie; P: wykonanie i nowe kwestie Toni na wyraźne upoważnienie autora z 22 X 2026]'

def parse(raw):
 out=[]
 for block in re.split(r'(?m)^@@ ',raw)[1:]:
  lines=block.splitlines(); h=lines[0].split('|'); assert len(h)==9,h
  typ,dt,tm,source,title,bt,k,sex,w=h
  body=[]; ordinary=0; total=0; ps={}; hook=''
  for line in lines[1:]:
   if line.startswith('HOOK: '): hook=line[6:]; continue
   m=re.match(r'^([+!])([1-7])? (.*)$',line)
   if m:
    total+=1; ordinary+=m[1]=='+'; text=m[3]; body.append(text)
    speaker=re.match(r'> \*\*([^*]+)\*\*',text)
    if speaker and typ in ('C','T'):
     name=speaker[1]; val=int(m[2] or 4)
     if name!='toni31_X07': ps[name]=val if val!=4 or name not in ps else ps[name]
   else:body.append(line)
  assert hook and total and ordinary/total>=.6,(title,ordinary,total)
  assert not re.search(r'\b[CDTVF]\d{2,}\b','\n'.join(body)),title
  out.append(dict(typ=typ,dt=dt,tm=tm,source=source,title=title,bt=int(bt),k=int(k),sex=sex,w=w,body='\n'.join(body).strip(),ordinary=ordinary,total=total,ps=ps,hook=hook))
 return out

def build(month,section,title,raw,state,drift,notes,maxima=None,write=True):
 original={p:p.read_bytes() for p in (Y2,Y3)}
 both='\n'.join(x.decode('utf-8-sig') for x in original.values())
 mx={c:max([int(v) for v in re.findall(r'\b'+c+r'(\d+)\b',both)] or [0]) for c in 'CDTVF'}
 if maxima is not None: mx.update(maxima)
 entries=parse('\n'+raw); n=len(entries)
 assert n==(40 if month in (5,6) else 20 if month in (7,8) else 30),(month,n)
 counts={b:sum(e['bt']==b for e in entries) for b in range(1,5)}
 assert list(counts.values())==[n*3//10,n//2,n//10,n//10],counts
 assert [e['dt']+' '+e['tm'].split('–')[0] for e in entries]==sorted(e['dt']+' '+e['tm'].split('–')[0] for e in entries),'chronologia'
 heading=f'### {section} — {title} — TYLKO MG'
 target=Y2 if month<=8 else Y3
 old=original[target].decode('utf-8-sig'); assert not write or heading not in old
 chunks=[f'\n{heading}\n\n{AUTH}\n\n**Zakres źródeł:** wyłącznie archiwa szkoły i WebiX. Poniżej krótkie, dosłowne wyciągi; znaczniki [P] dotyczą ich literackiej rekonstrukcji. Przekład francuskich rozmów na polski, angielskie wiadomości pozostawione w oryginale. Szum liczony według jawnych jednostek wyciągu: wiadomości, punktów dokumentu lub ujęć; podpisy redakcyjne MG nie wchodzą do mianownika.\n']
 index=[]; toni=[]
 for e in entries:
  c=e['typ']; mx[c]+=1; ident=c+str(mx[c]); e['id']=ident
  d=date.fromisoformat(e['dt']); dat=f'{DAYS[d.weekday()]} {d.day} {MONTHS[month]} 2009'; tz='CET' if d>=date(2009,10,25) else 'CEST'
  pcounts={p:list(e['ps'].values()).count(p) for p in range(1,8)}
  pp=', '.join(f'{p}: {v}' for p,v in pcounts.items() if v) or '— (brak jawnej deklaracji; nie wnioskować z obrazu)'
  sx=e['sex'].split(','); assert len(sx)==3
  metric=f"*Metryka: 3S M {sx[0]} / K {sx[1]}, zakres {sx[2]}, poz. 6–7: 0 | 7P (głosy wyciągu; 4 = bez oceny w tej rozmowie): {pp} | E: {'E4' if c=='D' else 'E2–E3'} | W: {e['w']} | BT: {e['bt']} (blok 30/50/10/10) | K: K{e['k']} | Szum: {e['ordinary']}/{e['total']} = {e['ordinary']/e['total']:.0%}.*"
  chunks.append(f"\n##### {ident} — {e['title']} [P; N: uzgodnione zdarzenia]\n\n**Kanał / czas:** {e['source']}; {dat}, {e['tm']} {tz}.\n**BT:** {e['bt']}.\n\n{e['body']}\n\n**Źródło i korzyść STEEPLE [P]:** {e['hook']}\n\n{metric}\n")
  index.append(f"| {ident} | {d.day} {MONTHS[month]} | {e['source']} | {e['bt']} | {e['hook'].split('. ')[0]} |")
  for ln in e['body'].splitlines():
   if '**toni31_X07**' in ln or 'Toni [N]' in ln or 'Toni [P' in ln:toni.append((ident,ln))
 chunks.append(f'\n#### {section}.1 — Indeks i kontrola bloku\n\n| ID | Data 2009 | Źródło | BT | Użycie w 2013 [P] |\n|---|---|---|:--:|---|\n'+'\n'.join(index)+'\n\n**Bilans:** '+str(n)+' pozycji; BT '+ '/'.join(str(counts[b]) for b in range(1,5))+' = 30/50/10/10. ID: '+ '; '.join(c+str(min(int(e['id'][1:]) for e in entries if e['typ']==c))+'–'+c+str(max(int(e['id'][1:]) for e in entries if e['typ']==c)) for c in 'CDTVF' if any(e['typ']==c for e in entries))+'.\n\n**Stan po bloku [N + P]:**\n'+state+'\n\n**Dryf plotki [P]:**\n'+drift+'\n\n**Uwagi dla MG / ciągłość:**\n'+notes+'\n\n**Nowe wypowiedzi Toni — kontrola MG:** autor powierzył ich sporządzenie agentowi na podstawie AMA, kwestionariusza i wizerunku. Poniżej wszystkie nowe zarejestrowane kwestie, również drobne [P: subagent, do kontroli MG]; cytaty dostarczone przez autora pozostają [N].\n\n'+'\n'.join(f'- **{i}:** {ln.removeprefix("> ")}' for i,ln in toni)+'\n\n---\n')
 text='\n'.join(chunks)
 if not write: return text, entries, toni
 if month==9:
  needle='*Pusty; pierwszy blok: IX 2009 (rentrée i intégration X2009).*'
  assert old.count(needle)==1; old=old.replace(needle,'*Katalog rozwijany miesiąc po miesiącu; numeracja wspólna z latami 1–2.*')
 stamp=datetime.now().strftime('%Y%m%d-%H%M%S-%f'); backup=ROOT/'archiwum'/'kopie-steeple-2009';backup.mkdir(exist_ok=True)
 for p in (Y2,Y3):assert p.read_bytes()==original[p], 'Zmiana rownolegla'
 shutil.copy2(target,backup/(target.stem+'-'+stamp+'.md'))
 with target.open('w',encoding='utf-8',newline='\n') as f:f.write(old.rstrip()+'\n\n'+text)
 out=ROOT/'robocze'/f'steeple-2009-{month:02d}.md'
 with out.open('w',encoding='utf-8',newline='\n') as f:f.write(text)
 record={'month':month,'section':section,'count':n,'ids':[e['id'] for e in entries],'bt':counts,'backup':str(backup/(target.stem+'-'+stamp+'.md')),'previous_sha256':hashlib.sha256(original[target]).hexdigest(),'source_sha256':hashlib.sha256(target.read_bytes()).hexdigest(),'toni':toni}
 (ROOT/'robocze'/f'steeple-2009-{month:02d}-kontrola.json').write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n',encoding='utf-8',newline='\n')
 print(json.dumps({k:v for k,v in record.items() if k not in ('toni','ids')},ensure_ascii=False));print('ID:', ', '.join(record['ids']));print('Toni:',len(toni))
 return entries
