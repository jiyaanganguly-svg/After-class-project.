def calculatechange(paid, price):
    change = paid - price
    return change


snackprice = 25
print("===== SNACK VENDING MACHINE =====")
print(f"This snack costs {snackprice} units.")
print("Accepted coins: 1, 5, 10, 25")

totalinserted = 0
coinsinserted = 0

while totalinserted < snackprice:
    coin = int(input("Insert a coin (1, 5, 10, or 25): "))
    
    if coin !=1 and coin != 5 and coin != 10 and coin != 25:
        print("Invalid coin, try again!")
        continue
    
   
    totalinserted += coin
    coinsinserted += 1
    print(f"Inserted {coin}. Total so far: {totalinserted}")
   
    changedue = calculatechange(totalinserted, snackprice)
print("Thank you! Enjoy your snack.")
if changedue > 0:
    print(f"Your change is: {changedue} units.")

    if totalinserted>=snackprice:
        print("Dispensing your item...")
    if changedue==0:
        pass
    else:
        print("Here is your change {changedue} units")

    print ("=======Snack purchase summary======")
    print ("Snack price", snackprice)
    print ("Coins inserted", coinsinserted)
    print ("Change due", changedue)
    print("====================================")
    print("Thanks for your purchase. Have a wonderful day!")