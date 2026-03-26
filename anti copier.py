import os
import shutil
from pathlib import Path
os.chdir('/storage/emulated/0/Download/')
pathes=[]
for root,dirs,files in os.walk(os.getcwd()):
    for file in files:
        pathes.append(os.path.join(root,file))
pp=set(pathes)
clean_pathes=list(pp)
mm={}
for i in clean_pathes:
    y=os.path.getsize(i)
    mm.update({i:y})
    
sizes = {}

for path, size in mm.items():
    if size in sizes:
        sizes[size].append(path)
    else:
        sizes[size] = [path]


 
for size, files in sizes.items():
   if len(files) > 1:
       n=[]
       for i in files:
           n.append(i)
       
       p=Path(n[0])
       j=p.name
       o=Path(n[1])
       j1=o.name
       if j==j1:
           print(p)
           print(o)
           print(size)
           print('\n'*5)
           
               
