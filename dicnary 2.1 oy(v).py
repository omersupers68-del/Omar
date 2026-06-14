#-*- coding: utf-8 -*-

import os 
import csv 
import shutil
import time
import string
import random
main=True
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
    from wordfreq import zipf_frequency
    import arabic_reshaper
    from bidi.algorithm import get_display
    
except:
    input("disclamer:\nthis app needs to download some files and data so make sure you  are connected by internet(enter any thing) ")
    os.system('pip install requests')  
    os.system('pip install deep_translator')
    os.system('pip install wordfreq')
    os.system('pip install arabic-reshaper')
    os.system('pip install python-bidi==0.4.2')
    shaw()
    import requests
    from  deep_translator import GoogleTranslator  as gt
    from wordfreq import zipf_frequency 
    import arabic_reshaper
    from bidi.algorithm import get_display
#what?    
type(9)
le='ج ح خ ه ع غ ف ق ث ص ض ط ك د م ظ ن ز ت و ا ة ل ى ب ر ي ؤ س ء ش ذ'
aric=set(le.split(' '))
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
        
def clear():
    rows=[]
    with open('dicdata.csv','r')as di:
        mo=csv.reader(di)
        for row in mo:
                many=False
                if len(row)!=2:
                    many=False
                    continue
                if zipf_frequency(row[0],'en')>0:
                    for le in row[0]:
                        if le.isalpha():
                            if zipf_frequency(row[1],'ar')>0:
                                myame=0
                                for ale in row[1]:
                                    if ale in aric:
                                        myame+=1
                                if myame==len(row[1]):
                                    many=True    
                        else:
                            many=False
                            break                       
                if many:
                  rows.append(row)    
                    
                
    with open('dicdata.csv','w') as di :
        mi=csv.writer(di)
        mi.writerows(rows)
                                                     
def ar(text):
    return text #get_display(arabic_reshaper.reshape(text))
#storage
stpath='/storage/emulated/0/Android/data/ru.iiec.pydroid3/files'
if not os.path.exists(stpath+'/dicdata.csv'):
    if os.path.exists('dicdata.csv'):
        shutil.move('dicdata.csv',stpath)
    else:
        print('there are dangerous problems\n')
        print("I am sorry \nmain data not found\nplease ,check 'dicdata.csv' file\nGuideline:\n1-make the data file and the app file in the same folder\n2-you must use pydroid 3 to run this app\n3-if there no any thing work talk with the owner(omar)")
        main=False
if not os.path.exists(stpath+'/grs.csv'):
    if os.path.exists('grs.csv'):
        shutil.move('grs.csv',stpath)
    else:
        print('there are dangerous problems\n')
        print("I am sorry\nsome data not found\nplease check 'grs.csv' file\nGuideline:\n\n1-make the data file and the app file in same folder\n2-you must use pydroid 3 to run this app \n3-DO NOT use this app in simulation or matrix\n4-if there no any thing word talk with the owner(omar)")
        main=False
if not os.path.exists(stpath+'/token.txt'):
    if os.path.exists('token.txt'):
        shutil.move('token.txt',stpath)
    else:
        print('there are dangerous problems\n')    
        main=False    
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
with open('token.txt','r') as t:
    ever=t.read().split('∆')
    

token =ever[0]
chat_id =ever[1]
url = f"https://api.telegram.org/bot{token}/sendMessage"

v=False
try :
    with open('v.txt','r'):
        v=True
except :
    pass       
#main loop
smart=['come teach me','your brain is expensive','so smart','you are an native speaker']
c=0
#makeing data
if main:
    with open('dicdata.csv','r',encoding='utf-8') as de:
        wo = csv.reader(de)
        for row in wo:
            if len(row) >= 2:
                pe[row[0].lower()] = row[1]
                pa[row[1].lower()] = row[0]
    print('welcome to dicnary app')
    MSCI()
    
while main:
    
    if  not c > 0:
        if internet :
            if v:
                with open('v.txt','r') as v :
                    nm=v.read()
                    data1 = {
                 "chat_id": chat_id,
                 "text":f'from {nm}:user is online'}
                    requests.post(url, data=data1)
                    c+=1
    if not os.path.exists('dicdata.csv'):
        print("I am sorry \ndata not found\nplease ,check 'dicdata.csv' file\nGuideline:\n1-make the data file and the app file in the same folder\n2-you must use pydroid 3 to run this app\n3-if there no any thing work talk with the owner(omar)")
        break
        
    #choices
    if not v:
        print('ex-Auto-clean(you must do it just once for lifelong)')   
    print('1-from english to arabic')
    print('2-from arabic to english')
    print('3-feedback')
    print('4-test(still working on it)')
    print('5-exit')
    ch=input('enter your choice:')
   
    #choice one
    if ch=='1' or ch=='١':
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
                    ch1p+=1
                    if internet:
                        mp=0
                        new_word=gt(source='en',target='ar').translate(ein)
                        print(new_word)
                        if zipf_frequency(ein,'en')>0:
                            if zipf_frequency(new_word,'ar')>0:
                                for le in new_word:
                                    if le in string.ascii_lowercase or le in string.ascii_uppercase:
                                        mp+=1
                                    else:
                                        mp-=1
                                if mp==len(new_word):        
                                    with open('dicdata.csv','a',newline='',encoding='utf-8') as de:
                                        hi=csv.writer(de)
                                        kilo=[ein.lower(),new_word]
                                        hi.writerow(kilo)
                            
                    elif internet==False:    
                        print('not found\nyou can open internet to reseach\n') 
                        ch1p+=1          
    #choice two      
    elif ch=='2' or ch=='٢':
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
                            print(pa[ein.lower()])
                            ch2p+=1
                        except:
                            mp=0
                            ch2p+=1
                            if internet:   
                                 new_word=gt(source='ar',target='en').translate(ein)
                                 print(new_word)
                                 if zipf_frequency(ein,'ar')>0:
                                      if zipf_frequency(new_word,'en')>0:
                                          for le in new_word:
                                              if le in string.ascii_lowercase or le in string.ascii_uppercase:
                                                mp+=1
                                              else:
                                                mp-=1
                                          if mp==len(new_word):        
                                              with open('dicdata.csv','a',newline='',encoding='utf-8') as de:                                        
                                                hi=csv.writer(de)
                                                kilo=[new_word.lower(),ein]
                                                hi.writerow(kilo)
                                                  
                            else:                                                     
                                print('not found\nyou can open internet to reseach\n')
                                ch2p+=1
    #choice five
    elif ch=='5' or ch=='٥':
         shaw()
         print('exiting...')
         time.sleep(1)
         print('..')
         time.sleep(0.5)
         print('.')
         break
    #choice extension     
    elif not v:
        if ch=='ex':
            shaw()
            clear()
            with open('v.txt','w') as v:
                name=input('what is your name:')
                shaw()
                clear()
                v.write(name)
                v.write(':0')
    #feedback choice
    elif ch=='3' or ch=='٣':
        shaw()
        if internet :            
            text=input('enter your feedback:')
            nm=None
            with open('v.txt','r') as v :
                nm=v.read()
            data = {
         "chat_id": chat_id,
         "text":f'from {nm}:{text}'}    
            requests.post(url, data=data)
        else:
             print('no internet')
     #test choose
    elif ch=='4' or ch=='٤':
         shaw()
         while True:
             print('1-English words')
             print('2-Arabic gramer\n3-exit')
             ink=input('enter your choice:')
             wana=['1','2','3']
             if ink not in wana:
                 shaw()
                 print('please enter(1,2,3)')
             elif ink=='1' or ink=='١':
                 shaw()
                 score=0
                 cori={}          
                 wordsa=list(pe.items())       
                 for i in range(0,10):
                     word=random.choice(wordsa)
                     eword=word[0]
                     aword=word[1]
                     nu=random.randint(0,1)
                     leword=[]
                     laword=[]
                     choice=['A','B','C','D']
                     choi=[]
                     while True:
                         if len(leword)==3:
                             if len(leword)==3:
                                 break
                         word1=random.choice(wordsa)
                         if word != word1:
                             leword.append(word1[0])
                             laword.append(word1[1])
                     if nu==0:
                         print(ar(f' what is ({eword}) means in arabic\n'))
                         ac=False
                         bc=False
                         cc=False
                         i=random.choice(choice)                         
                         cor=f' {aword}-{i}'
                         nuw=i
                         if i =='A':
                                 choi.append(f' {laword[0]}-B')
                                 choi.append(f' {laword[1]}-C')
                                 choi.append(f' {laword[2]}-D')
                                 ac=True
                                 bc=False
                                 cc=False
                                 dc=False
                                 print(cor)
                                 print(choi[0])
                                 print(choi[1])
                                 print(choi[2])
                                 ion=input('enter(A,B,C,D):')
                                 shaw()
                                 if nuw.lower()==ion.lower():
                                     score+=1
                                 else:
                                     cori[aword]=eword                                 
                         elif i=='B':
                                 choi.append(f' {laword[0]}-A')
                                 choi.append(f' {laword[1]}-C')
                                 choi.append(f' {laword[2]}-D')
                                 ac=False
                                 bc=True
                                 cc=False
                                 dc=False
                                 print(choi[0])
                                 print(cor)
                                 print(choi[1])
                                 print(choi[2])
                                 ion=input('enter(A,B,C,D):')
                                 shaw()
                                 if nuw.lower()==ion.lower():
                                     score+=1
                                 else:
                                     cori[aword]=eword
                         elif i=='C':
                                 choi.append(f' {laword[0]}-A')
                                 choi.append(f' {laword[1]}-B')
                                 choi.append(f' {laword[2]}D')
                                 ac=False
                                 bc=False
                                 cc=True
                                 dc=False
                                 print(choi[0])
                                 print(choi[1])
                                 print(cor)
                                 print(choi[2])
                                 ion=input('enter(A,B,C,D):')
                                 shaw()
                                 if nuw.lower()==ion.lower():
                                     score+=1
                                 else:
                                     cori[aword]=eword                                 
                         elif i=='D':
                                 choi.append(f' {laword[0]}-A')
                                 choi.append(f' {laword[1]}-B')
                                 choi.append(f' {laword[2]}-C')
                                 ac=False
                                 bc=False
                                 cc=False
                                 dc=True
                                 print(choi[0])
                                 print(choi[1])
                                 print(choi[2])
                                 print(cor)
                                 ion=input('enter(A,B,C,D):')
                                 shaw()
                                 if nuw.lower()==ion.lower():
                                     score+=1
                                 else:
                                     cori[aword]=eword         
                     if nu==1:
                         print(ar(f' what is ({aword}) means in arabic\n'))
                         ac=False
                         bc=False
                         cc=False
                         i=random.choice(choice)                         
                         cor=f'{i}-{eword}'
                         nuw=i
                         if i =='A':
                                 choi.append(f'B-{leword[0]}')
                                 choi.append(f'C-{leword[1]}')
                                 choi.append(f'D-{leword[2]}')
                                 ac=True
                                 bc=False
                                 cc=False
                                 dc=False
                                 print(ar(cor))
                                 print(ar(choi[0]))
                                 print(ar(choi[1]))
                                 print(ar(choi[2]))
                                 ion=input('enter(A,B,C,D):')
                                 shaw()
                                 if nuw.lower()==ion.lower():
                                     score+=1
                                 else:
                                     cori[aword]=eword                                 
                         elif i=='B':
                                 choi.append(f'A-{leword[0]}')
                                 choi.append(f'C-{leword[1]}')
                                 choi.append(f'D-{leword[2]}')
                                 ac=False
                                 bc=True
                                 cc=False
                                 dc=False
                                 print(ar(choi[0]))
                                 print(ar(cor))
                                 print(ar(choi[1]))
                                 print(ar(choi[2]))
                                 ion=input('enter(A,B,C,D):')
                                 shaw()
                                 if nuw.lower()==ion.lower():
                                     score+=1
                                 else:
                                     cori[aword]=eword
                         elif i=='C':
                                 choi.append(f'A-{leword[0]}')
                                 choi.append(f'B-{leword[1]}')
                                 choi.append(f'D-{leword[2]}')
                                 ac=False
                                 bc=False
                                 cc=True
                                 dc=False
                                 print(ar(choi[0]))
                                 print(ar(choi[1]))
                                 print(ar(cor))
                                 print(ar(choi[2]))
                                 ion=input('enter(A,B,C,D):')
                                 shaw()
                                 if nuw.lower()==ion.lower():
                                     score+=1
                                 else:
                                     cori[aword]=eword                                 
                         elif i=='D':
                                 choi.append(f'A-{leword[0]}')
                                 choi.append(f'B-{leword[1]}')
                                 choi.append(f'C-{leword[2]}')
                                 ac=False
                                 bc=False
                                 cc=False
                                 dc=True
                                 print(ar(choi[0]))
                                 print(ar(choi[1]))
                                 print(ar(choi[2]))
                                 print(ar(cor))
                                 ion=input('enter(A,B,C,D):')
                                 shaw()
                                 if nuw.lower()==ion.lower():
                                     score+=1
                                 else:
                                     cori[aword]=eword
                        
                 shaw()            
                 print(f'you aswered {str(score)}/10') 
                 if score==10:
                     print(random.choice(smart))
                 if len(cori)>0:
                     print('your mistakes:')
                     for i in cori.items() :
                         print(f'{i[0]}:{i[1]}')       
                     input('enter any thing:')
                     shaw()      
                     
                                                                         
             elif ink=='2' or ink=='٢':
                 cong=False
                 
                 while True:
                     corio=[]
                     shaw()
                     with open('v.txt','r') as v:
                         main=v.read().split(':')
                         mais=main[1]
                         print(f'your score:{mais}')
                         print('1-Easy(your score>=0)')
                         print('2-Medium(your score>=25)')
                         print('3-Hard(your score>=50)')
                         print('4-Insane(your score>=75)')
                         print('5-exit')
                         if mais=='100':
                             cong=True
                             print('6-Congratulate')
                         inom=input('your choice:')
                         #exit
                         if inom=='5':
                             break
                         #easy
                         elif inom=='1':
                             corio=[]
                             shaw()
                             with open('grs.csv','r') as g:
                                 we=csv.reader(g)
                                 qus=[]
                                 on=0
                                 for i in we:
                                     qus.append(i)
                                     on+=1
                                     if on==100:
                                         break
                             aqus=[]       
                             while True:                                             
                                 qu=random.choice(qus)
                                 aqus.append(qu)
                                 if len(aqus)==10:
                                     aqus=aqus
                                     break
                             score=0
                             for i in aqus:
                                 shaw()
                                 print(ar(i[0]))
                                 an=input(ar(f'اعرب {i[1]}:'))
                                 if an==ar(i[2]):
                                     score+=1
                                 else:
                                     corio.append(i)    
                             if len(corio)>0:
                                 print('your mistakes')
                                 for i in corio:
                                     print('\n')
                                     print(ar(f'{i[0]}'))       
                                     print(ar(f'{i[1]}تعرب{i[2]}'))
                             input(ar(f'your score:{score}/10'))
                             add=score*5
                             with open('v.txt','w') as v:
                                 v.write(main[0]+':'+str(int(mais)+add))
                         #medium       
                         elif inom=='2':
                             shaw()
                             if int(mais) >= 25:
                                 with open('grs.csv','r') as g:
                                     we=csv.reader(g)
                                     qus=[]
                                     on=0
                                     for i in we:
                                         on+=1
                                         if on>=100 and on<201:
                                             qus.append(i)
                                         elif on==201:
                                             break
                                 aqus=[]       
                                 while True:                                             
                                     qu=random.choice(qus)
                                     aqus.append(qu)
                                     if len(aqus)==10:
                                         aqus=aqus
                                         break
                                 score=0
                                 for i in aqus:
                                     shaw()
                                     print(ar(i[0]))
                                     an=input(ar(f'اعرب {i[1]}:'))
                                     if an==ar(i[2]):
                                         score+=1
                                     else:
                                         corio.append(i)       
                                 if len(corio)>0:
                                     print('your mistakes')
                                     for i in corio:
                                         print('\n')
                                         print(ar(f'{i[0]}'))       
                                         print(ar(f'{i[1]}تعرب{i[2]}'))
                                 input(ar(f'your score:{score}/10'))
                                 add=score*10
                                 with open('v.txt','w') as v:
                                     v.write(main[0]+':'+str(int(mais)+add))
                                     
                             else:
                                 print('your score is lower than 25')
                          #hard       
                         elif inom=='3':
                             shaw()
                             if int(mais) >= 50:
                                 with open('grs.csv','r') as g:
                                     we=csv.reader(g)
                                     qus=[]
                                     on=0
                                     for i in we:
                                         on+=1
                                         if on>=200 and on<301:
                                             qus.append(i)
                                         elif on==301:
                                             break
                                 aqus=[]       
                                 while True:                                             
                                     qu=random.choice(qus)
                                     aqus.append(qu)
                                     if len(aqus)==10:
                                         aqus=set(aqus)
                                         break
                                 score=0
                                 for i in aqus:
                                     shaw()
                                     print(ar(i[0]))
                                     an=input(ar(f'اعرب {i[1]}:'))
                                     if an==ar(i[2]):
                                         score+=1
                                     else:
                                         corio.append(i)    
                                 if len(corio)>0:
                                     print('your mistakes')
                                     for i in corio:
                                         print('\n')
                                         print(ar(f'{i[0]}'))       
                                         print(ar(f'{i[1]}تعرب{i[2]}'))
                                 input(f'your score:{score}/10')
                                 add=score*15
                                 with open('v.txt','w') as v:
                                     v.write(main[0]+':'+str(int(mais)+add))
                             else:
                                 print('your score is lower than 50')
                          #insane       
                         elif inom=='4':
                             shaw()
                             if int(mais) >= 75:
                                 with open('grs.csv','r') as g:
                                     we=csv.reader(g)
                                     qus=[]
                                     on=0
                                     for i in we:
                                         on+=1
                                         if on>=100 and on<201:
                                             qus.append(i)
                                         elif on==201:
                                             break
                                 aqus=[]       
                                 while True:                                             
                                     qu=random.choice(qus)
                                     aqus.append(qu)
                                     if len(aqus)==10:
                                         aqus=set(aqus)
                                         break
                                 score=0
                                 for i in aqus:    
                                     shaw()
                                     print(ar(i[0]))
                                     an=input(ar(f'اعرب {i[1]}:'))
                                     if an==ar(i[2]):
                                         score+=1
                                     else:
                                         corio.append(i)
                                         
                                 if len(corio)>0:
                                     print('your mistakes')
                                     for i in corio:
                                         print('\n')
                                         print(ar(f'{i[0]}')) 
                                         print(ar(f'{i[1]}تعرب{i[2]}'))
                                 input(f'your score:{score}/10')
                                 add=score*20
                                 with open('v.txt','w') as v:
                                     v.write(main[0]+':'+str(int(mais)+add)) 
                             else:
                                 print('your score is lower than 75') 
                         elif cong:
                             if inom=='6':
                                 shaw()
                                 print('''from omar
                                 I thank you very much for solving these questions
                                 go to  feedback and enter(i am finished)
                                 ''')
                         else:
                             shaw()
                             if not cong:
                                 print('please,enter(1,2,3,4,5)')
                             elif cong:
                                 print('please,enter(1,2,3,4,5,6)')     
                     
             elif ink=='3' or ink =='٣':
                 shaw()
                 break
    #elif
    #easter egg situation
    elif ch.lower()=='easter eggs' :
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
    elif stupid>=10:
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
    