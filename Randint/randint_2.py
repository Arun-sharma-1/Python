import random
highest=10
answer=random.randint(1,highest)
print(answer)

print("plz guess a no between 1 and {} ".format(highest))
guess=0
while guess!=answer:
    guess=int(input())

    if guess==0:
        break
    
    if guess==answer:
        print("You got it")
    else:
        if guess<answer:
            print("plz guess higher ")
        else:
            print("plz guess lower ")