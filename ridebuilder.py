print("=====================================================")
print("         WELCOME TO TRANSPORTAION PICKER")
print("=====================================================")
print("First, pick your mode of transportation!")
print("1. Bike")
print("2. Walk")
print("3. Car")
choice=int(input("Enter 1, 2 or 3"))
if choice==1:
    print("You chose Bike!")
    print("Now chose your type of bike! ")
    print("1. Elctric Bike")
    print("2. Mountain Bike ")
    choice2=int(input("Enter 1 or 2"))
    if choice2==1:
        print("Avg distance per hour :20 mi")
        print("Even faster than normal bike!")
    else:
        print("Avg distance per hour :15 mi")
        print("Good choice for enviorment!")

elif choice==2:
    print("You chose Walk!")
    print("Choose your location!")
    print("1. City")
    print("2. Park")
    choice3=int(input("Enter 1 or 2"))
    if choice3==1:
        print("You chose to walk to the City!")
        print("Distance :6 mi")
        print("Daily exersize!")
    if choice3==2:
        print("You chose to walk to the Park!")
        print("Distance :1 mi")
        print("Daily exersize!")

elif choice==3:
    print("You chose Car!")
    print("Chose your Car!")
    print("1. Electric")
    print("2. Gas")
    choice4=int(input("Choose 1 or 2"))
    if choice4==1:
        print("You chose an electric car!")
        print("Good choice for enviornment!")
    if choice4==2:
        print("You chose a gas fueled car!")
        print("Very smooth ride!")
    print("====================================================")
    print("     THANK YOU FOR USING TRANSPORTATION PICKER")
    print("====================================================")