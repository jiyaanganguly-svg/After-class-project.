#Classroom points calculator
 

team1 = 234
team2 = 934
team3 = 213
team4 = 239
team5 = 65
 

total = team1 + team2 + team3 + team4 + team5
average = total / 5
 
print("Total points       :", total)
print("Average per team   :", average)
 

stars_per_point = 5
reward_stars = total * stars_per_point
print("Total reward stars :", reward_stars)
 

boxes = reward_stars // 50
leftover = reward_stars % 50
 
print("Full boxes packed  :", boxes)
print("Leftover stars     :", leftover)
 

last_week = 972
 
print("Better than last week? :", total > last_week)
print("Same as last week?     :", total == last_week)
print("At least as good?      :", total >= last_week)
 

total += 90
print("After bonus points :", total)
 

total -= 39
print("After missed tasks :", total)
 
 
reward_stars = total * stars_per_point
boxes = reward_stars //50
 
print("Final boxes packed :", boxes)
