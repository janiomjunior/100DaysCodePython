from art import logo
# calculator
#Add
def add(n1, n2):
    return n1 + n2

#subtract
def sub(n1, n2):
    return n1-n2

#Multiply
def mult(n1, n2):
    return n1*n2

#division
def div(n1, n2):
    return n1/n2

operations = {
    "+":add,
    "-":sub,
    "*":mult,
    "/":div,
}
print(logo)
next = 'y'
num1 = float(input("what is the first number?: "))
#print("Pick up one of the operations")
for operation in operations:
    print(operation)
choice = input("Pick up one of the operations: ")

while (next == 'y'):

    num2 = float(input("what is the next number?: "))
    answer = operations[choice](num1, num2)
    print(F"{num1} {choice} {num2} = {answer}")
    next = input(f"Type 'y' to calculate with {answer} or type 'n' to exit:")



