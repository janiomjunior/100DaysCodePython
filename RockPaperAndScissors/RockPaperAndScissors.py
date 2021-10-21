import random

rock = '''
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

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for paper or 2 for Scissors: "))
computer_choice = random.randint(0,2)
choices = {0:rock,1:paper,2:scissors}

print("the user choice was:", choices[user_choice] )
print("the computer choice was:", choices[computer_choice] )

if choices[user_choice] == rock and choices[computer_choice] == scissors:
    print("the user wins")
elif choices[user_choice] == scissors and choices[computer_choice] == paper:
    print("the user wins")
elif choices[user_choice] == paper and choices[computer_choice] == rock:
    print("the user wins")



