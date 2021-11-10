import random
print('Welcome to Number Guessing Game ')
print("I'm thinking of a number between 1 and 100 ")
diff = input("Type easy or hard : ")
res = random.randint(1, 100)
print(res)
chance = 0


def chances(chance):
    global diff
    if diff == 'easy':
        return 10
    else:
        return 5

chance=chances(chance)
print(f'You have {chance} attmpts remaining to guess the number ')

while chance:
        guess = int(input("Make a guess: "))
        if guess == res:
            print('You got it ! ')
            chance = 0
        elif guess > res:
            print('Too high ! ')
            chance-=1
            if chance==0:
                print('you have come out of chances')
            else:
                print(f'You have {chance} attmpt remaining to guess the number ')
            
        elif guess < res:
            print('Too low ')
            chance-=1
            if chance==0:
                print('you have come out of chances')
            else:
                print(f'You have {chance} attmpts remaining to guess the number ')
