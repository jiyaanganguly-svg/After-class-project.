# Number Guessing Game
secret = 27 
attempts = 5  
won = False
# Welcome player
print("Welcome to the Number Guessing Game")
print("Guess a number between 1 and 45. You have 5 attempts.")
guess = int(input("Enter your guess: "))
if guess==27:
    print("Congratulations! You got the secret number!")
else: 
    print("You guessed wrong! You now have 4 attempts left")
    guess2 = int(input("Enter your guess: "))
    if guess2==27:
       print("Congratulations! You got the secret number!")
    else:
       print("You guessed wrong! You now have 3 attempts left")
       guess3 = int(input("Enter your guess: "))
       if guess3==27:
        ("Congratulations! You got the secret number!")
       else:
          print("You guessed wrong! You now have 2 attempts left")
          guess4 = int(input("Enter your guess: "))
          if guess4==27:
            ("Congratulations! You got the secret number!")
          else:
            print("You guessed wrong! You now have 1 attempt left")
            guess5=int(input("Enter your last guess!"))
            if guess5==27:
               print("Congratualtions! You got the secret number")
            else:print("You guessed wrong! You now have no attempts left")









 


