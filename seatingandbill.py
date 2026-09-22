
 

def total_bill(billamount, tip):
    
    total = billamount * (1 + 0.01 * tip)
    total = round(total, 2)
    print(f"Please pay ${total}")
    return total
 

total_bill(150, 20)
 

def seatingarrangements(guests):
 

    if guests == 0 or guests == 1:
        return 1

    else:
        return guests * seatingarrangements(guests - 1)
 
 
# PART 4: Access and print the docstring
print(seatingarrangements.__doc__)
 
# PART 5: Display seating arrangement results
print("Seating arrangements for 1 guest:", seatingarrangements(1))
print("Seating arrangements for 2 guests:", seatingarrangements(2))
print("Seating arrangements for 3 guests:", seatingarrangements(3))
print("Seating arrangements for 5 guests:", seatingarrangements(5))
