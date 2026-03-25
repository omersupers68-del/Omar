import os 
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
while True:
    ch=input('enter to find the file or folder:').lower()
    print('\n')
    answer=[]
    for i in clean_pathes:
        p=Path(i)
        kl=p.name
        if ch in kl:
            print(i)
            print(p.name)
            print('\n'*2)            
        