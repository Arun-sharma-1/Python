import random
low=1
highest=1000
print("Enter a number between {} and {} ".format(low,highest))
guess=input("plz enter to start ")
guesses=1
while True:
    guess=low+(highest-low)//2
    high_low=input("my guess is {} . should  I guess higher or lower if higher enter 'h' if lower enter 'l' and if correct than enter'c'  ".format(guess)).casefold()
    if high_low=="h":
        low=guess+1
        
    elif high_low=="l":
        highest=guess-1
        
    elif high_low=="c":
        print("Yeah, i got it in {}  time " .format(guesses))
        break
    else:
        print("Enter h, l or c ")
    guesses+=1


# x=3
# x**=2
 #x=x**2
# print(x)

