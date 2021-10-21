#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P
letters_rand = ''
symbols_rand = ''
numbers_rand = ''

for i in range(0, nr_letters):
    letters_rand += letters[random.randint(0,len(letters))]

for j in range(0, nr_symbols):
    symbols_rand += symbols[random.randint(0,len(symbols))]

for h in range(0, nr_numbers):
    numbers_rand += numbers[random.randint(0,len(numbers))]
easy_pass= letters_rand+symbols_rand+numbers_rand
print("Easy pass generator: ", easy_pass)

hard_pass = ''
for g in range(0,len(easy_pass)):
    hard_pass += easy_pass[random.randint(0,len(easy_pass))]

print("the hard password generated is: ", hard_pass)