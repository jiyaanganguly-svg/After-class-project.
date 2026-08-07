print("My Chore Checklist")
total_chores = int(input("How many chores do you have today? "))
print("You have", total_chores, "chores to finish today!")


completed_count = 0
chore_num = 1


while chore_num <= total_chores:

    
    if chore_num == 1:next_chore = "Make your bed"
    elif chore_num==2:next_chore ="Feed the pets"
    elif chore_num==3: next_chore="Wash dishes"
    else: nextchore="Take out trash"
    answer=input(f"Have you finished:, {nextchore}? Yes or no")