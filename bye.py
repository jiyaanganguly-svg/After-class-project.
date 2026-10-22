valid=False
while not valid:
    try:
        n=int(input("Enter a Number:"))
        while n % 2==0:
            print("bye")
            n=int(input("Enter a Number:"))
            valid=True
    except ValueError
    print("Invalid")