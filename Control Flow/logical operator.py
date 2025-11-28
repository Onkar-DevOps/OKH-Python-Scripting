print("Welcome to the roller-coster!" )
height = int(input("Enter your heigth: "))
bill = 0

if height >= 100:
    print("You can ride the rollercoster")
    age = int(input("Please enter the age: "))
    if age <=10:
        bill = 5
    elif age <= 20:
        bill = 10
    elif age >=45 and age <=50:
        print("Free Ride")
    else:
        bill = 20
    photo = (input("Do you want photo ? Enter Y or N : "))
    if photo == "Y":
        bill += 3
    print("Your bill is ", bill)
else:
    print("Sorry!! You are Not eligible")