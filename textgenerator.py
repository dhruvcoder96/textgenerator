import random
import string

p = input("Enter length of names = ")
c =  int(p)
alphastr= string.ascii_uppercase
cons = alphastr.replace('A','')
cons = cons.replace('E','')
cons = cons.replace('I','')
cons = cons.replace('O','')
cons = cons.replace('U','')
vow = "AEIOU"
patternMaker = "01"
str1=""
deffStr = ""
for i in range(0,c):
    g = random.choice(patternMaker)
    deffStr+=g
#deffStr = input("Enter pattern of text: 1 for vowel, 0 for consonant. ")
"""for i in range(1,c):
    l=input("enter c, v")
    for j in l:
        if j=='c':
            g=random.choice(cons)
            str1=str1+g
        elif j=='v':
            g=random.choice(vow)
            str1=str1+g"""
for i in deffStr:
    if i == '1':
        g = random.choice(vow)
        str1+=g
    else:
        g = random.choice(cons)
        str1+=g

print(str1)
