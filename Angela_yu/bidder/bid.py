import os
# os.system('cls')
dict = {}
Flag = 1
def maxbid(name , bid ):
    highest_bid=0;
    winner=''
    for bidder in dict:
        if dict[bidder] > highest_bid:
            highest_bid=dict[bidder]
            winner = bidder
    print(f'The winner is {winner} with max bid ${highest_bid} ')
while Flag:
    name = input('What is your Name: ')
    bid =int(input('What is your bid '))
    dict[name]=bid
    ask = input('Is there are other who want to bid ? yes or no : ')
    if ask=='yes':
        os.system('cls')
    
    else:
        Flag=0
        os.system('cls')
        maxbid(name,bid)
 

