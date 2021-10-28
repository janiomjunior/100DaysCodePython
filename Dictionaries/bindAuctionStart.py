import replit
from replit import clear
from art import logo
#HINT: You can call clear() to clear the output in the console.
print(logo)
answer = 'y'
bids = {}
while (answer.lower() == 'y'):
    key = input('Enter with your Name: ')
    bid = int(input('What is the bid price: '))
    bids[key] = bid
    answer = input("Anybody more will bid, type y or n: ")
    if answer.lower() == 'y':
        clear()
high_price = 0
name_high_price = ''
for key in bids:
    if bids[key] > high_price:
        high_price = bids[key]
        name_high_price = key
print(f"the winner is {name_high_price} with a bid of {high_price}")