# Holiday Activity Planner
# Lesson: Nested Conditional Statements
 
print("====================================")
print("    Welcome to Holiday Planner!     ")
print("====================================")
print()
 
print("Step 1: Pick your holiday type")
print("  1 - Beach Holiday")
print("  2 - Hiking Holiday")
print()
 
choice = int(input("Enter 1 or 2: "))
print()
 
if choice == 1:
    # Nested if-else - runs only when choice is 1
    print("Step 2: Pick your beach activity")
    print("  1 - Swimming")
    print("  2 - Sandcastle Building")
    print()
 
    beach_activity = int(input("Enter 1 or 2: "))
    print()
 
    if beach_activity == 1:
        print("You picked  : Swimming")
        print("Best time   : Morning")
        print("Remember    : Carry sunscreen and water")
    else:
        print("You picked  : Sandcastle Building")
        print("Best time   : Evening")
        print("Remember    : Carry a bucket and shovel")
 
elif choice == 2:
    # Nested if-else - runs only when choice is 2
    print("Step 2: Pick your Hiking activity")
    print("  1 - Big mountain")
    print("  2 - Small mountain")
    print()
 
    Hiking_activity = int(input("Enter 1 or 2: "))
    print()
 
    if Hiking_activity == 1:
        print("You picked  : Big mountain")
        print("Best for    : Exersize and veiws")
        print("Remember    : Wear durable hiking shoes and bring food and bug repellent")
    else:
        print("You picked  : Small mountain")
        print("Best for    : Beginner hikers and family")
        print("Remember    : Carry a flashlight omse bars and bug repellent")
 
else:
    print("That was not a valid choice.")
    print("Please enter 1 for Beach Holiday or 2 for Hiking Trip.")
 
print()
print("====================================")
print("   Your holiday/trip plan is ready!      ")
print("   Enjoy your trip!                 ")
print("====================================")
