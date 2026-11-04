from pathlib import Path
from datetime import datetime,timedelta
import shutil,json,sys,re,random,hashlib
sys.path.insert(0,'robocze')
from steeple_2009_build import build
root=Path.cwd();paths=[root/'mg-wyciek-forum-x2007-rok-2.md',root/'mg-wyciek-forum-x2007-rok-3.md'];originals={p:p.read_text(encoding='utf-8') for p in paths};updated=dict(originals)
changes={10:[('> **augustin.richa** (20:13): [Wpis redakcji wysłany z jego upoważnienia, nie bieżąca obecność konta.] Daty starych tekstów pozostają.','> **Juliette** (20:13): Ze starszej notatki Richarda: daty starych tekstów pozostają.'),('> **Juliette** (20:22): Dopiski korekt oznaczamy osobno.','> **Lou_X07** (20:22): Dopiski korekt oznaczamy osobno.'),('Wreszcie przegrała, a i tak połowa rozmowy o jej tyłku w stroju sportowym. Chyba nie o medal tu chodziło.','Wreszcie, kurwa, zwykła porażka, a wy dalej o jej tyłku w sportowym stroju. To było w ogóle o medal?'),('Zupę zamroziłam. Nikt jej nie wyrzuca!!!','Mama znowu pyta, czy wracam na weekend. Jakby do Marsylii było dwadzieścia minut!!!'),('I labelled the box. Even used a date.','Rugby bruise finally fading. The lecture bench still hurts.'),('I am away tomorrow. The spare key is signed in.',"I was on the wall all evening. My hands disagree with tomorrow's lab.")],11:[('Dopłata większa niż mój bilet.','dopłata, kurwa, większa niż bilet. nie jadę.')],12:[('Znowu wrócę autobusem.','kurwa, znowu autobus. pół nocy z torbą na kolanach.')],5:[('Put the band names in. I like credit for my noise.','Put the band names in. Credit for my own bloody noise would be nice.')]}
records=[];generated={};payloads={}
for month in range(5,13):
 dp=root/'robocze'/f'steeple-2009-{month:02d}-dane.json';d=json.loads(dp.read_text(encoding='utf-8'));rp=root/'robocze'/f'steeple-2009-{month:02d}-kontrola.json';rec=json.loads(rp.read_text(encoding='utf-8'))
 for a,b in changes.get(month,[]):assert d['raw'].count(a)==1,(month,a);d['raw']=d['raw'].replace(a,b)
 if month==10:
  a='- Jedyny wpis z nazwiskiem Richarda podczas dnia roboczego po wyjeździe to redakcyjna nota Juliette przywołująca jego wcześniejsze upoważnienie; nie jest nową obecnością konta. Nie utrwalać fikcji codziennego WebiX na FHM.'
  b='- W dniu roboczym po wyjeździe Juliette przytacza starszą notatkę Richarda pod własnym kontem. Richard nie loguje się w tej scenie. Nie utrwalać fikcji codziennego WebiX na FHM.'
  assert d['notes'].count(a)==1;d['notes']=d['notes'].replace(a,b)
 blocks=re.split(r'(?m)^@@ ',d['raw']);parts=[blocks[0]]
 for block,ident in zip(blocks[1:],rec['ids']):
  ls=block.splitlines();h=ls[0].split('|');typ=h[0]
  if typ in ('F','V'):h[7]='0,0,0'
  if typ in ('C','T') and '–' in h[2]:
   ta,tb=h[2].split('–');base=datetime.strptime(ta,'%H:%M');end=datetime.strptime(tb,'%H:%M');duration=int((end-base).total_seconds()//60);rng=random.Random(ident+'-2009');shift=rng.randint(-22,22) if base.hour>=3 else 0;base+=timedelta(minutes=shift);end+=timedelta(minutes=shift)
   ix=[i for i,l in enumerate(ls) if re.match(r'^[+!]\d? > \*\*[^*]+\*\* \(\d\d:\d\d\):',l)]
   if len(ix)>=2:
    n=len(ix)-1;remain=duration-2*n;assert remain>=0;ws=[rng.random()**2+.06 for _ in range(n)];gaps=[2+int(remain*w/sum(ws)) for w in ws]
    while sum(gaps)<duration:gaps[rng.randrange(n)]+=1
    assert min(gaps)>=2 and max(gaps)<=40;minute=0
    for j,i in enumerate(ix):
     tm=(base+timedelta(minutes=minute)).strftime('%H:%M');ls[i]=re.sub(r'(?<=\()\d\d:\d\d(?=\):)',tm,ls[i],count=1)
     if j<n:minute+=gaps[j]
   h[2]=base.strftime('%H:%M')+'–'+end.strftime('%H:%M')
  ls[0]='|'.join(h);parts.append('@@ '+'\n'.join(ls))
 d['raw']='\n'.join(parts);side=root/'robocze'/f'steeple-2009-{month:02d}.md';oldblock=side.read_text(encoding='utf-8');mm=re.search(r'^### ([\d.]+) — (.*?) — TYLKO MG$',oldblock,re.M);assert mm
 maxima={c:min([int(i[1:]) for i in rec['ids'] if i[0]==c] or [1])-1 for c in 'CDTVF'};text,entries,toni=build(month,mm[1],mm[2],**d,maxima=maxima,write=False);assert [e['id'] for e in entries]==rec['ids']
 target=paths[0 if month<=8 else 1];assert updated[target].count(oldblock)==1,(month,updated[target].count(oldblock));updated[target]=updated[target].replace(oldblock,text)
 rec['toni']=toni;rec['final_revision']='Kontrola źródeł, metryk obrazu, rytmu rozmów i notatki Richarda; tylko własne dodatki.';payloads[dp]=json.dumps(d,ensure_ascii=False,indent=2)+'\n';generated[side]=text;records.append((rp,rec))
backup=root/'archiwum'/'kopie-steeple-2009'/('kontrola-finalna-'+datetime.now().strftime('%Y%m%d-%H%M%S-%f'));backup.mkdir()
for p in paths:shutil.copy2(p,backup/p.name)
for p,s in updated.items():assert p.read_text(encoding='utf-8')==originals[p];p.write_text(s,encoding='utf-8',newline='\n')
for p,s in payloads.items():shutil.copy2(p,backup/p.name);p.write_text(s,encoding='utf-8',newline='\n')
for p,s in generated.items():shutil.copy2(p,backup/p.name);p.write_text(s,encoding='utf-8',newline='\n')
for p,rec in records:
 shutil.copy2(p,backup/p.name);rec['final_sha256']=hashlib.sha256(paths[0 if rec['month']<=8 else 1].read_bytes()).hexdigest();p.write_text(json.dumps(rec,ensure_ascii=False,indent=2)+'\n',encoding='utf-8',newline='\n')
print('Zrewidowano wyłącznie własne dodatki; ID i decyzje autora bez zmian. Kopia:',backup)
