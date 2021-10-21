import random

string_input = input("Enter with the names separeted by commas: ")
list_names = string_input.split(',')
#print(list_names)
print(list_names[random.randint(1,len(list_names))], "will pay the bill")