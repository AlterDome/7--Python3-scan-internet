#
# Author Rybochkin Aleksei
# 2023
#
# Выводит список DNS имен всего интернета по Ipv4
# Lists DNS names of the entire Internet over Ipv4
# Muestra una lista de nombres DNS de todo Internet vía IPv4
#####
import os
import sys

import ipaddress
from ipaddress import IPv4Address

import array as ar
import socket as sk

import time


###########

# ADR1.ADR2.ADR3.ADR4 : PORT
ADR1 = list(range(0,10))
ADR2 = list(range(0,10))
ADR3 = list(range(0,10))
ADR4 = list(range(0,10))

PORT = 21   #list(range(0,65536))

Spisok = open("Spisok.txt", "w")


#print(PORT1)
###########
if __name__ == "__main__":
   print(" Lets take a names  ")

s = sk.socket(sk.AF_INET, sk.SOCK_STREAM)


###########
a=0
b=0
c=0
d=0

aa=''
bb=''
cc=''
dd=''


stroka = list()

r1= [0, 11, 12, 13, 14, 15]
r2= [70, 71]
r3= [50, 52]
r4= [10, 20, 57]

lis = list()
for a in r1:
    for b in r2:
        for c in r3:
            for d in r4:  #range (70):

               # IPADR = str((ADR1,".",ADR2,".",ADR3,".",ADR4))
               # IPv4Address(IPADR)
                          
               # socket.connect(('a"."b"."c"."d', PORT))

               # lis = ipaddress.ip_address((a+"."+b+"."+c+"."+d))

               # lis = str(a+"."+b+"."+c+"."+d)                  

               # stroka = socket.gethostbyaddr("a+.+b+.+c+.+d")

               # stroka = a.join(str('.'))

              
                stroka = str(a) +'.'+  str(b) +'.'+ str(c) +'.'+ str(d)

                print(stroka)
                

                Spisok.write(str(a))
                Spisok.write(str("."))
                Spisok.write(str(b))
                Spisok.write(str("."))
                Spisok.write(str(c))
                Spisok.write(str("."))
                Spisok.write(str(d))
                Spisok.write(str(" = "))

                IPv4Address(stroka)

                lis = sk.gethostbyaddr('8.8.8.8')

              #  sk.connect((stroka, PORT))

                Spisok.write(str(lis))
                Spisok.write("\n")

                
    
###########
                
print(" It's OK  \n")
Spisok.close()


#####################################################    
if __name__ != "__main__":
    print(" The end... ")
