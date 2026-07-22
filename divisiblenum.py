print("Enter a number(Nmerator)")
numbern=int(input())
print("Enter a number (Denominator)")
numberd=int(input())
if numbern%numberd==0:
    print ("\n" +str(numbern)+ " is divisible by " +str(numberd))
else:
      print ("\n" +str(numbern)+ " is not divisible by " +str(numberd))