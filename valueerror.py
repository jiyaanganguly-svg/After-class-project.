try:
    number=int(input("Enter a Number:"))
    print("The number is entered is", number)

except ValueError as ex:
    print("Exeption:", ex)