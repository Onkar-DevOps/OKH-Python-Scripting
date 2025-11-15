print("Welcome to the roller-coster!" )
height = int(input("Enter your heigth: "))

if height >= 100:
    print("You can ride the rollercoster")
    age = int(input("Please enter the age: "))
    if age <=10:
        print ("Ticket value is 5$ ")
    elif age <= 20:
        print ("Ticket value is 10$ ")
    else:
        print ("ticket Value is 20$")    
else:
    print("Sorry!! You are Not eligible")