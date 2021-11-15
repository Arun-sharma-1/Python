import string
import random
import os

def gen():
    s1=string.ascii_uppercase
    s2=string.ascii_lowercase
    s3=string.digits
    s4=string.punctuation

    passlen=int(input('Enter the length of password: '));
    l=[]
    l.extend(list(s1))
    l.extend(list(s2))
    l.extend(list(s3))
    l.extend(list(s4))
    random.shuffle(l)
    print(''.join(l[0:passlen]))
   
os.system('cls')
gen()