import json
import os
try:
    with open('libdata.txt','r') as myf:
        books = json.load(myf)
except:
    books = {}

def shaw():
    if os.name=='nt':
        os.system('cls')
    else:
        os.system('clear')
bo=[]     
for i in books :
    bo.append(i)   



print('library app by omar hatim\n')
while True:
    print('1-add book')
    print('2-change pages')
    print('3-view')
    print('4-exit and save')
    print('5-remove book')

    choose = int(input('enter one number(1-5):'))
    shaw()

    if choose == 1:
        z = input('enter title:')
        x = int(input('enter number of pages:'))
        v = int(input('enter number you read:'))
        books[z] = {'pages': x, 'readed': v}
        print('\nsuccess\n')
        shaw()

    elif choose == 2:
        print('books:',' , '.join(bo))
        c = input('enter book name:')
        if c in books:
            kl = int(input('new number of pages:'))
            books[c]['readed'] = kl
        shaw()

    elif choose == 3:
        print('title::pages:readed')
        for title,info in books.items():
            print(f"{title}::{info['pages']}:{info['readed']}\n")
        input('finish')
        shaw()
    elif choose == 4:
        with open('libdata.txt','w') as myf:
            json.dump(books, myf)
        print('saved,bye')
        break
    elif choose ==5:
        for i in books :
            bo.append(i)
        an=input(' , '.join(bo)+'\n').lower()
        if an in bo:
            books.pop(an)
            input('succeeded')
            shaw()
        else:
            print('invald')