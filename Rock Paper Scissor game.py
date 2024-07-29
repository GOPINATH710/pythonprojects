import random

rock='''
       ______
______'  ____)
        (_____)
        (_____)
        (____)
______._(___) 
'''

paper='''
       _____
______'  ___)____
           ______)
           ______)
          _______)
______.________) 
'''



scissors='''
       ______
______'  ____)___
           ______)
           ______)
          (___)
______.___(__) 
'''


game=[rock,paper,scissors]
user_choice=int(input("0 for Rock \U0001FAA8,\n1 for paper \U0001F4C4,\n2 for scissor \u2702 \n Enter your choice:"))
if user_choice >3 or user_choice<0:
    print("entered number is invalid")
    quit()
else:
    print(game[user_choice])
    computer_choice=random.randint(0,2)
    print("computer choise:",game[computer_choice])
    #print(computer_choice)
    if computer_choice==user_choice:
        print("match drawn")
    elif computer_choice==0 and user_choice==2:
        print("you lose")
    elif user_choice==0 and computer_choice==2:
        print("you win")
    elif computer_choice>user_choice:
        print("you lose")
    elif user_choice>computer_choice:
        print("you win")

