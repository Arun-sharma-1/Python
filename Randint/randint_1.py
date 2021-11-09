import random
highest=10
answer=random.randint(1,highest)
print(answer)

print("plz guess a no between 1 and {} ".format(highest))
guess=int(input())

if guess==answer:
    print("You got in 1st time")
else:
    if guess<answer:
        print("plz guess higher ")
    else:
        print("plz guess lower ")
    guess=int(input())

    if guess==answer:
        print("Yeah! u got it ")
    else:
        print("plz try again after sometime")
