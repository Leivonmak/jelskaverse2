from pathlib import Path
import re,json,hashlib,shutil
from datetime import date,datetime
ROOT=Path.cwd()
Y2=ROOT/'mg-wyciek-forum-x2007-rok-2.md'; Y3=ROOT/'mg-wyciek-forum-x2007-rok-3.md'
DAYS=['pn','wt','śr','czw','pt','sob','nd']; MONTHS={1:'I',2:'II',3:'III',4:'IV',5:'V',6:'VI',7:'VII'}
COUNTS={1:30,2:30,3:40,4:30,5:40,6:40,7:30}
ALLOWED=set('ArnaudDC Max_D Cyril_V Romain_G Théo_M Edouard_R Thomas_X07 Mathis_D Mathilde_X07 Capucine_E Lou_X07 Hugo_L Juliette Clémence Sarah Fiona Annika Elif Xiaomei ravel_X07 toni31_X07 hainsworth marta.chmie abenkirane katarzyna.majew bzawadzki saidi_X08 eline.dijk kaori_I nadia.rocha iris_D piotr_R olivier_X08 verdier_X08 vernier_08 bbouchet martinbenjamin_D zoe_P Titi_06 tonio_X06 Yanis.K lboulanger valentin_S coudray_X07 lacroix_X06 daumas_X06 augustin.richa clement.tourn cdurand gaelle_F ananya_X09 nadine_X09 mwu marta.wierz'.split())
AUTH='[N: ramy, daty i wybory autora zatwierdzone w czacie; P: realizacja literacka, dokumenty i nowe kwestie Toni na wyraźne upoważnienie autora z 22 X 2026]'
def parse(raw):
 entries=[]
 for block in re.split(r'(?m)^@@ ',raw)[1:]:
  ls=block.splitlines(); h=ls.pop(0).split('|'); assert len(h)==9,h
  typ,dt,tm,source,title,bt,k,sex,w=h; body=[]; ordinary=total=0; ps={}; hook=''
  for line in ls:
   if line.startswith('HOOK: '): hook=line[6:];continue
   m=re.match(r'^([+!])([1-7])? (.*)$',line)
   if m:
    ordinary+=m[1]=='+';total+=1; s=m[3];body.append(s)
    p=re.match(r'> \*\*([^*]+)\*\* \((\d\d:\d\d)\):',s)
    if p:
     assert p[1] in ALLOWED,(title,p[1])
     if m[2] and p[1]!='toni31_X07':ps[p[1]]=int(m[2])
   else:body.append(line)
  text='\n'.join(body).strip()
  assert hook and total and ordinary/total>=.6,(title,ordinary,total)
  assert not re.search(r'\b[CDTVF]\d{2,}\b',text),title
  assert not re.search(r'\b(?:WhatsApp|Instagram|Tinder|cringe|simp|sus|W5)\b',text),title
  entries.append(dict(typ=typ,dt=dt,tm=tm,source=source,title=title,bt=int(bt),k=int(k),sex=sex,w=w,body=text,ordinary=ordinary,total=total,ps=ps,hook=hook))
 return entries

def build(month,raw,state,drift,notes):
 section=f'3.{month+4}'; n=COUNTS[month]
 original={p:p.read_bytes() for p in (Y2,Y3)}
 both='\n'.join(b.decode('utf-8-sig') for b in original.values())
 mx={c:max(map(int,re.findall(r'\b'+c+r'(\d+)\b',both)),default=0) for c in 'CDTVF'}
 before=mx.copy(); entries=parse(raw);assert len(entries)==n,(month,len(entries))
 counts={b:sum(e['bt']==b for e in entries) for b in range(1,5)}
 assert list(counts.values())==[n*3//10,n//2,n//10,n//10],counts
 assert all(date.fromisoformat(e['dt']).year==2010 and date.fromisoformat(e['dt']).month==month for e in entries)
 keys=[e['dt']+' '+e['tm'].split('–')[0] for e in entries];assert keys==sorted(keys),'chronologia'
 old=original[Y3].decode('utf-8-sig'); heading=f'### {section} — {MONTHS[month]} 2010 — TYLKO MG';assert heading not in old
 chunks=[f'\n{heading}\n\n{AUTH}\n\n**Czytanie wyciągów:** francuskie wiadomości w przekładzie; cudzoziemcy po angielsku, Polacy po polsku. Szum liczony w widocznych jednostkach (wiadomościach, punktach odpisu, ujęciach), nie w słowach. To wybrane fragmenty, a nie próbka reprezentatywna promocji. 7P oznacza tylko wyrażone postawy; milczenie i wiadomość techniczna nie dowodzą obojętności. Terminy, konta i kadry są danymi archiwum fikcyjnego.\n']
 index=[]; toni=[]
 for e in entries:
  c=e['typ'];mx[c]+=1;ident=c+str(mx[c]);e['id']=ident;d=date.fromisoformat(e['dt']);tz='CEST' if date(2010,3,28)<=d<date(2010,10,31) else 'CET'
  pp='; '.join(f'{p} — {v}' for p,v in e['ps'].items()) or 'nieustalone (bez przypisywania postawy z czynności)'
  sx=e['sex'].split(',');assert len(sx)==3
  metric=f"*Metryka: 3S M {sx[0]} / K {sx[1]}, zakres {sx[2]}, poz. 6–7: 0 | 7P: {pp} | E: {'4 (odpis)' if c=='D' else '2–3; krótkie wpisy 1'} | W: {e['w']} | BT: {e['bt']}; blok 30/50/10/10 | K: K{e['k']} | Szum: {e['ordinary']}/{e['total']} = {e['ordinary']/e['total']:.0%}.*"
  chunks.append(f"\n##### {ident} — {e['title']} [P; N: zatwierdzone ramy]\n\n**Kanał / czas:** {e['source']}; {DAYS[d.weekday()]} {d.day} {MONTHS[month]} 2010, {e['tm']} {tz}.\n**BT:** {e['bt']}.\n\n{e['body']}\n\n**Źródło i korzyść STEEPLE [P]:** {e['hook']}\n\n{metric}\n")
  index.append(f"| {ident} | {d.day} {MONTHS[month]} | {e['source']} | {e['bt']} | {e['hook']} |")
  for ln in e['body'].splitlines():
   if '**toni31_X07**' in ln or 'Toni [N]' in ln or 'Toni [P' in ln:
    status='N' if 'Toni [N]' in ln else 'P: subagent, do kontroli MG'
    toni.append((ident,status,ln.removeprefix('> ')))
 ranges='; '.join(c+str(before[c]+1)+'–'+c+str(mx[c]) for c in 'CDTVF' if mx[c]>before[c])
 chunks.append(f'\n#### {section}.1 — Indeks i kontrola bloku\n\n| ID | Data 2010 | Nośnik | BT | Użycie w 2013 [P] |\n|---|---|---|:--:|---|\n'+'\n'.join(index)+f'\n\n**Bilans:** {n} pozycji; BT '+ '/'.join(str(counts[b]) for b in range(1,5))+' = 30/50/10/10. ID: '+ranges+'.\n\n**Stan po bloku [N + P]:**\n'+state+'\n\n**Dryf plotki [P]:**\n'+drift+'\n\n**Wątpliwości i kontrola ciągłości dla MG:**\n'+notes+'\n\n**Wypowiedzi Toni do kontroli:** nowe kwestie na upoważnienie autora oznaczone [P: subagent, do kontroli MG]; kwestie z briefu zachowują [N]. Poniższy wykaz obejmuje wszystkie kwestie z wyciągu.\n\n'+'\n'.join(f'- **{i} [{status}]:** {ln}' for i,status,ln in toni)+'\n\n---\n')
 text='\n'.join(chunks)
 # Every candidate and its audit are persisted before mutation of the user file.
 data=ROOT/'robocze'/f'steeple-2010-{month:02d}-dane.json';assert not data.exists()
 data.write_text(json.dumps(dict(month=month,raw=raw,state=state,drift=drift,notes=notes),ensure_ascii=False,indent=2)+'\n',encoding='utf-8',newline='\n')
 out=ROOT/'robocze'/f'steeple-2010-{month:02d}.md';out.write_text(text,encoding='utf-8',newline='\n')
 backup=ROOT/'archiwum'/'kopie-steeple-2010';backup.mkdir(exist_ok=True)
 dest=backup/(Y3.stem+'-'+datetime.now().strftime('%Y%m%d-%H%M%S-%f')+'.md')
 for p in (Y2,Y3):assert p.read_bytes()==original[p],'zmiana równoległa'
 shutil.copy2(Y3,dest)
 Y3.write_text(old.rstrip()+'\n\n'+text,encoding='utf-8',newline='\n')
 record=dict(month=month,section=section,count=n,ids=[e['id'] for e in entries],ranges=ranges,bt=counts,toni=toni,backup=str(dest),previous_sha256=hashlib.sha256(original[Y3]).hexdigest(),source_sha256=hashlib.sha256(Y3.read_bytes()).hexdigest(),entries=entries)
 (ROOT/'robocze'/f'steeple-2010-{month:02d}-kontrola.json').write_text(json.dumps(record,ensure_ascii=False,indent=2)+'\n',encoding='utf-8',newline='\n')
 print(json.dumps({k:v for k,v in record.items() if k not in ('entries','toni','ids')},ensure_ascii=False));print('Nowe kwestie Toni:',len(toni))
 return record
