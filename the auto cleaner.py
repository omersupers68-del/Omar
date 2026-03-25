import os 
import shutil
from pathlib import Path 
os.chdir('/storage/emulated/0/Download')

pathes=[]
for root,dirs,files in os.walk(os.getcwd()):
    for file in files:
        pathes.append(os.path.join(root,file))  
    for dirname in dirs:
        pathes.append(os.path.join(root,dirname))
pp=set(pathes)
clean_pathes=list(pp)

for i in clean_pathes:
    p=Path(i)
    if p.is_dir():
        os.chdir(i)
        num=0
        for pd in os.listdir():
            num +=1
        if num==0:
            os.rmdir(i)
            print(p.stem)
    if p.is_file():
        if os.path.getsize(i)==0:
            os.remove(i)
            print(p.stem)
        
        