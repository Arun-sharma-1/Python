import random
import os
from data import *
from art import *
flag = True 
score=0
while flag:
    print(logo)
    a = random.randint(0, 20)
    b = random.randint(0, 20)
    with open('z.txt','a') as file:
         file.write(str(data[a]['follower_count']) +' ' + str(data[b]['follower_count']) )
         file.write(' ')
    print('Compare A: {0} , {1} from {2} '.format(data[a]['name'],data[a]['description'],data[a]['country']))
    print(vs)
    print('Compare B: {0} ,{1} from {2} '.format(data[b]['name'],data[b]['description'],data[b]['country']))
    
    choose = input('Who has more followers ? Type "a" or "b" ')

    if choose == 'a':
        if data[a]['follower_count'] > data[b]['follower_count']: #choose a 
            score+=1
            os.system('cls')
            print(f'You are right! current score: {score} ')
             
        else:
            flag=False
            exit()
    elif choose== 'b':
        if data[b]['follower_count'] > data[a]['follower_count']: #choose a 
            score+=1
            os.system('cls')
            print(f'You are right! current score: {score} ')
             
        else:
            flag=False
            exit()
    else:
        score+=1