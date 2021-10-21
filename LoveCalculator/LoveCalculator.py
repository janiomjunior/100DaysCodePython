print("This is the true love game")
your_name = input("Enter with your name: ")
their_name = input("Enter with their name: ")
both_names = your_name.lower() + their_name.lower()
sum = both_names.count("t") + both_names.count("r") + both_names.count("u") + both_names.count("e") + both_names.count("l") + both_names.count("o") + both_names.count("v") + both_names.count("e")

if sum < 10 and sum > 90:
    print(f"Your score is ${sum}, you go together like coke and mentos.")
elif sum > 40 and  sum < 50 :
    print(f"Your score is ${sum}, you are alright together.")
else:
    print(f"Your score is ${sum}")