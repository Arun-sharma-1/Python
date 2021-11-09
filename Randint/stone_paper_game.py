import random
stone = ''' 
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)

'''
paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)

 '''
scissor = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)

 '''
my_choice=int(input('Enter your input 0 , 1, 2 : '))
computer_choice=random.randint(0,2)
if(my_choice==0 and computer_choice==1):
    print(stone)
    print(paper)
    print('You lose! ');
elif(my_choice==0 and computer_choice==2):
    print(stone)
    print(scissor)
    print('You won');
elif(my_choice==1 and computer_choice==0):
    print(paper)
    print(stone)
    print('You won! ');
elif(my_choice==1 and computer_choice==2):
    print(paper)
    print(scissor)
    print('You lose! ')
if(my_choice==2 and computer_choice==0):
    print(scissor)
    print(stone)
    print('You lose! ');
if(my_choice==2 and computer_choice==1):
    print(scissor)
    print(paper)
    print('You win! ');
else:
    print('Tie ')