import random
import string

p = input("enter number of names")
c =  int(p)
alphastr= string.ascii_lowercase
cons = alphastr.replace('a','');
cons = cons.replace('e','');
cons = cons.replace('i','');
cons = cons.replace('o','');
cons = cons.replace('u','');
vow = "aeiou";
for i in range(1,c):
    str1=""
    l=input("enter c, v")
    for j in l:
        if j=='c':
            g=random.choice(cons);
            str1=str1+g;
        elif j=='v':
            g=random.choice(vow);
            str1=str1+g;
    print(str1+"\n")
