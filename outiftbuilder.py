print("===========================")
print("      OUTFIT BUILDER")
print("===========================")
temp=int(input("Enter Today's Temprature In Degrees Farenheight"))
if temp>=32 and temp<=70:
    outfit="jacket with cotton or warm pants"
    print("Temperature is cold today")
    print("Wear a", outfit)
if temp<=33:
    outfit="winter jacket with warm pants"
    print("Temperature is below freezing")
    print("Wear a", outfit)
if temp>=71:
    outfit="T shirt with shorts"
    print("Temperature is warm today")
    print("Wear a", outfit)
rain=(input("Is it raining today?"))
if rain=="yes":
    print("It is raining today")
    print("Bring umbrealla or raincoat with you if you go outside")
elif rain=="no":
    print("It is not raining today")
    print("You can go outside without any raingear")
else:
    print("Please answer yes or no")
    rain=(input("Is it raining today?"))
if rain=="yes":
    print("It is raining today")
    print("Bring umbrealla or raincoat with you if you go outside")
elif rain=="no":
    print("It is not raining today")
    print("You can go outside without any raingear")

wind=int(input("Enter the wind speed today in mph"))
if wind>=30<=65:
    print("Wind is mild") 
    print("Windbreaker needed")
if wind<=20:
    print("Wind is calm")
    print("No windbreaker needed")
if wind>=66:
    print("Wind is at dangerous speed")
    print("Try to stay indoors")
print("Weather check complete!")
print("Final summary")
