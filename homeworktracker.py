

totalhomework = 4
originalcount = totalhomework
print(f"You have {originalcount} homework tasks to finish today!")
 

completedcount = 0
tasknum = 1

while tasknum <= totalhomework:
 
    if tasknum == 1:
        nexttask = "Math work"
    elif tasknum == 2:
        nexttask = "Science worksheet"
    elif tasknum == 3:
        nexttask = "English writing"
    else:
        nexttask = "Coding practice"
 
    answer = input(f"Have you finished: {nexttask}? (yes/no): ")
 
    if answer == "yes":
        completedcount += 1
        tasknum += 1
        print("Great job! Homework task completed.")
    else:
        print("Okay, finish it and check again!")
 

    print("Homework tasks remaining:", totalhomework - completedcount)
    print()
 

print("===== ALL HOMEWORK COMPLETE! =====")
print("Great work finishing your homework today!\n")
 

print("Now let's safely peek at an infinite loop...")
testvalue = 0
safetycounter = 0
 
while testvalue <= 0:
    print("This condition never changes, so this would run forever!")
    safetycounter += 1
 
    if safetycounter == 3:
        print("(Stopping here on purpose - a real infinite loop never stops on its own!)")
        break
 

print("\n===== HOMEWORK COMPLETION SUMMARY =====")
print("Homework Assigned Today:", originalcount)
print("Homework Completed:", completedcount)
print("Homework Remaining:", totalhomework - completedcount)
print("=======================================")
