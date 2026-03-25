import os
import shutil
from pathlib import Path
os.chdir(os.getcwd()+'/Download')
p=Path(os.getcwd())
n=p/'#Important files'
if not n.exists():
    os.makedirs('#Important files')
os.chdir(n)    
for i in os.listdir():
    id=n/i
    if id.suffix !='.zip':
        kl=id.stem+'.zip'
        pad=n/kl
        if not pad.exists():
            shutil.make_archive(i,'zip')








