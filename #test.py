#test

def add(num1, num2):
    return num1 + num2 

def subract(num1. num2):
    return num1 - num2

def divide(num1,num2):
    return num1/num2

def multiply(num1,num2):
    return num1 * num2

("Hello user!")
("Choose an operation to run today")
print("1, Add")
print("2, Subract")
print("3, Divide")
print("4, Multiply")
operation=str(input("Chose 1, 2, 3 ,or 4"))
if operation==("1"):
    print(" You chose addition!")
    num1=int(input("Chose a number to add"))
    num2=int(input("Chose a number to add"))
    print(num1 + num2)
elif operation==("2"):
    print(" You chose subtraction!")
    num1=int(input("Chose your first number"))
    num2=int(input("Chose your second number"))
    print(num1 - num2)
elif operation==("3"):
    print(" You chose division!")
    num1=int(input("Chose your divident"))
    num2=int(input("Chose your divisor"))
    print(num1 / num2)
elif operation==("4"):
    print(" You chose multiplication!")
    num1=int(input("Chose your first number"))
    num2=int(input("Chose your second number"))
    print(num1 * num2)
elif operation !=("1") ("2") ("3") ("4"):
    print("Please enter 1, 2, 3, or 4")

