import random;
# import os

from hangman_art import stages,logo
print(logo)
list=['ardvark','baboon','camel']
choosen_word=random.choice(list)
print(f'choosen word is {choosen_word}')


display=[];
for i in range(len(choosen_word)):
    display+='_'


lives=6
end_of_game=False;
while not end_of_game:
    guess=input("Guess a word: ").lower()
    # os.system('cls') 

    for letter in range(len(choosen_word)):
        if(choosen_word[letter]==guess): #checking characther by characther
            display[letter]=guess #assingning the charcther to the list
            i+=1   
    print(f"{' '.join(display)}")   #change list into string 
    # print(display)

    if '_' not in display:
        end_of_game=True;
        print("you won!") 

    if guess not in display:
        lives-=1
        print(f"You guessed {guess}, that's not in the word, you lose a life")
        print('-'*10)
        print(stages[lives])
        if(lives==0):
            end_of_game=True
            print("You lose")
