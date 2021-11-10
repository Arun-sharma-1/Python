import random
from art import logo
import os


def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


def calculate_score(cards):
    # if 11 in cards and 10 in cards
    if(sum(cards) == 21 and len(cards) == 2):
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)


def compare(user_score, computer_score):
    if(user_score == computer_score):
        return 'Draw'
    elif computer_score == 0:
        return "Lose , computer has a Blackjack "
    elif user_score == 0:
        return "win , with a Black jack "
    elif user_score > 21:
        return "You went beyond limit , you lose "
    elif computer_score > 21:
        return "Computer went beyond limit, You Won"
    elif user_score > computer_score:
        return "YOU WON"
    else:
        return "YOU LOSE"


def playagain():
    print(logo)
    user_card = []
    computer_card = []
    is_game_over = False

    for _ in range(2):
        user_card.append(deal_card())
        computer_card.append(deal_card())

    while is_game_over == False:
        user_score = calculate_score(user_card)
        computer_score = calculate_score(computer_card)

        print(f"    Your card's: {user_card} , current score: {user_score}")
        print(f"    Computer card's: {computer_card} , computer score: {computer_score}")

        if user_score == 0 or computer_score == 0 or user_score >= 21:
            is_game_over = True
        else:
            user_deal = input('Type y to get anoter card , type n to pass: ')
            if user_deal == 'y':
                user_card.append(deal_card())
            else:
                is_game_over = True
    while computer_card != 0 and computer_score < 17:
        computer_card.append(deal_card())
        # print(computer_card[-1]) this card is choosen by computer
        computer_score = calculate_score(computer_card)

    print(compare(user_score, computer_score))


while input('Do you want to play game of blackjack express with Y or N') == 'y':
    os.system('cls')
    playagain()
