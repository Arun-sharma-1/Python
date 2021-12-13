import random
HANGMAN = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']


WORDS = ["TOKYO", "ARUN", "BERLIN", "DENVER", "BOGOTA", "PROFESSOR", "SERGIO"]

MAX_WRONG = len(HANGMAN) - 1

# Pick a words
word = random.choice(WORDS)

# Dashes for each letter in a word
current_guess = "-" * len(word)

# Wrong guess counter
wrong_guess = 0

# Used letters Tracker
used_letter = []

# Main loop
print("Welcome to Hangman")
print("Try to Guess the Word")

while wrong_guess < MAX_WRONG and current_guess != word:
    print(HANGMAN[wrong_guess])
    print("You have used following letters:", used_letter)
    print("So far, the word is:", current_guess)

    guess = input("Enter your letter guess:")
    guess = guess.upper()

    # Check if letter was already used
    while guess in used_letter:
        print("Your have already guessed that letter", guess)
        guess = input("Enter your letter guess:")
        guess = guess.upper()

    # Add new guesses letter to list of guessed letters
    used_letter.append(guess)

    # Check guess
    if guess in word:
        print("Your have guessed correctly")

        # New word with guessed letter and dashes
        new_current_guess = ""
        for letter in range(len(word)):
            if guess == word[letter]:
                new_current_guess += guess
            else:
                new_current_guess += current_guess[letter]

        current_guess = new_current_guess

    else:
        print("Sorry that was incorrect")
        # Increase the number of incorrect by 1
        wrong_guess += 1

# End the game
if wrong_guess == MAX_WRONG:
    print(HANGMAN[wrong_guess])
    print("You have been hanged")
    print("The correct world is", word)
else:
    print("You have Won!")
