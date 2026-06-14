import os 
import csv 
import shutil
import time
import string

#functions
def shaw():
    if os.name=='nt':
        os.system('cls')
    else:
        os.system('clear')
#make sure to internet        
try:
    import requests
    from  deep_translator import GoogleTranslator  as gt
except:
    input("disclamer:\nthis app needs to download some files and data so make sure you  are connected by internet(enter any thing) ")
    os.system('pip install requests')  
    os.system('pip install deep_translator')
    shaw()
    import requests
    from  deep_translator import GoogleTranslator  as gt
    
#what?    
type(9)

numper='1092837465'

#funcions 2 
internet=None
def MSCI():
    global internet
    try:
        requests.get("https://www.google.com",timeout=3)
        internet=True
    except:
        internet=False   




#storage
stpath='/storage/emulated/0/Android/data/ru.iiec.pydroid3/files'
if os.path.exists('dicdata.csv'):
    shutil.move('dicdata.csv',stpath)
    
os.chdir('/storage/emulated/0/Android/data/ru.iiec.pydroid3/files')     
#blacklist words
blw=['fuck','shit','fuck you','fuck your mother','aha','7h7']
#white list
wlw=['love','i love you','i like you','good app']
  
#main variapls
po=[]
pe={}
pa={}
eword=[]
aword=[]
stupid=0
#main loop
print('welcome to dicnary app')
while True:
    MSCI()
    if not os.path.exists('dicdata.csv'):
        print("I am sorry \ndata not found\nplease ,check 'dicdata.csv' file\nGuideline:\n1-make the data file and the app file in the same folder\n2-you must use pydroid 3 to run this app\n3-if there no any thing work talk with the owner(omar)")
        break
        
    #choices
       
    print('1-from english to arabic')
    print('2-from arabic to english')
    print('3-exit')
    ch=input('enter your choice:')
    #makeing data
    with open('dicdata.csv','r') as de:
            wo=csv.DictReader(de)
            #filtering
            for i in wo:
                for l in i.values():            
                    po.append(l)
            for i in range(0,len(po)):
                v6=po[i]
                if i%2==0:
                    eword.append(v6)
                else:
                    aword.append(v6)
            #creating main dictnary
            for a in range(0,len(eword)):
                pe[eword[a]]=aword[a] 
                pa[aword[a]]=eword[a]    
    #choice one
    if ch=='1':
            MSCI()
            shaw()
            ch1p=0                
            while True:
                ein=input('enter(exit) to go back\nenter:')
                if ein.lower()=='exit':
                    shaw()
                    break
                if ch1p==3:
                    shaw()
                    ch1p=0    
                try:
                    print(pe[ein.lower()])
                    ch1p+=1
                except:
                    if internet:
                        new_word=gt(source='en',target='ar').translate(ein)
                        print(new_word)
                        with open('dicdata.csv','a',newline='',encoding='utf-8') as de:
                            hi=csv.writer(de)
                            kilo=[ein,new_word]
                            hi.writerow(kilo)
                            
                    elif internet==False:    
                        print('not found\nyou can open internet to reseach\n') 
                        ch1p+=1          
    #choice two      
    elif ch=='2':
                    MSCI()
                    shaw()
                    ch2p=0
                    while True:
                        ein=input('enter(exit) to go back\nenter:')
                        if ein.lower()=='exit':
                            shaw()
                            break
                        if ch2p==3:
                            shaw()
                            ch2p=0
                        try:
                            print(pa[ein])
                            ch2p+=1
                        except:
                            if internet:   
                                                  new_word=gt(source='en',target='ar').translate(ein)
                                                  print(new_word)
                                                  with open('dicdata.csv','a',newline=' ',encoding='utf-8') as de:
                                                      hi=csv.writer(de)
                                                      kilo=[ein,new_word]
                                                      hi.writerow(kilo)
                            else:                                                     
                                print('not found\nyou can open internet to reseach\n')
                                ch2p+=1
    #choice three
    elif ch=='3':
         shaw()
         print('exiting...')
         time.sleep(1)
         print('..')
         time.sleep(0.5)
         print('.')
         break                                            
    #elif
    #easter egg situation
    elif ch.lower()=='easter eggs':
        shaw()
        print('okay')
        print(blw)
        print(wlw)
        print('omar')
        print('be wrong 10 times\n\n')
    #omar situation
    elif ch.lower()=='omar':
        shaw()
        print('he creats me\n')
    #stupid situation
    elif stupid==10:
        shaw()
        print('i am sorry\nyou are very stupid\nyou used this pragramme wrong ten times')
        break
    #white situation
    elif ch.lower() in wlw:
        shaw()
        print('thanks\n')
    #black situation
    elif ch.lower() in blw:
        print("\nyou don't deserve this app !\n")
        break
    else:
        shaw()
        print('please,enter (1,2,3)')
        stupid+=1
    