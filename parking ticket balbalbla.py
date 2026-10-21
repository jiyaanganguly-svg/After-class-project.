
 

def calculate_change(paid, price):
    change = paid - price
    return change
 

ticketprice = 30
print("===== PARKING TICKET PAYMENT HELPER =====")
print(f"This parking ticket costs {ticketprice} units.")
print("Accepted coins: 1, 5, 10, 25\n")
 
totalinserted = 0
coinsinserted = 0
 

while True:
    coin = int(input("Insert a coin (1, 5, 10, or 25): "))
 

    if coin != 1 and coin != 5 and coin != 10 and coin != 25:
        print("Invalid coin, try again!\n")
        continue
 
  
    totalinserted += coin
    coinsinserted += 1
    print(f"Inserted {coin}. Total so far: {totalinserted}\n")
 

    if totalinserted >= ticketprice:
        print("Enough money inserted!\n")
        break
 

changedue = calculate_change(totalinserted, ticketprice)
 
print("Printing your parking ticket...")
 

if changedue == 0:
    pass
else:
    print(f"Here is your change: {changedue} units")

print("\n===== PAYMENT SUMMARY =====")
print("Ticket Price:", ticketprice)
print("Coins Inserted:", coinsinserted)
print("Total Paid:", totalinserted)
print("Change Given:", changedue)
print("===========================")
print("Parking ticket payment complete!")
