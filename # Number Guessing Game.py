# Number Guessing Game
secret = 27 
attempts = 5  
won = False
# Welcome player
print("Welcome to the Number Guessing Game")
print("Guess a number between 1 and 45. You have 5 attempts.")

if attempts > 0:
  hearts = "You have no more guesses!"
attempts=5
guess = int(input("Enter your guess: "))
if guess==27:
    print("Congratulations! You got the secret number!")
else: 
    print("You guessed wrong! You now have 4 attempts left")
guess = int(input("Enter your guess: "))



 


