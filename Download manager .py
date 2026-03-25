import os
import shutil
from pathlib import Path
files=['#Music','#Apps','#Photos','#Texts','#Videos','#Pdf(s)','#Python Programms','#Archive(s)']
os.chdir(os.getcwd()+'/Download')
m=Path(os.getcwd())
print('loading....\n')
for i in files:
    if os.path.exists(i):
        pass
    else:
        os.makedirs(i)
with open(m/'#Music'/'REMEBER(music is haram).txt','w') as f:
    f.write('just read the title')

print('welcome to download manager\n')
print('working...')
for i in os.listdir():
    if os.path.isfile(i):
        p=Path(os.getcwd()+'/'+i)
        o=p.suffix
        if o=='.txt':
            shutil.move(p,m/'Texts')
        elif o=='.apk':
            shutil.move(p,m/'Apps')
        elif o=='.mp3' or o=='.wav':
            shutil.move(p,m/'Music')
        elif o=='.mp4' or o=='.mkv':
            shutil.move(p,m/'Videos')
        elif o=='.jpg' or o=='.png':
            shutil.move(p,m/'Photos')
        elif o=='.py':
            shutil.move(p,m/'Python Programms')
        elif o=='.zip':
            shutil.move(p,m/'Archive(s)')
        elif o=='.pdf':
            shutil.move(p,m/'Pdf(s)')
print('finished')            


