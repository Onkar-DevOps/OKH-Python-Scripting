print ("Welcome To Pizza Delivery !!")
size = input("Please select the size S, M or L: ")
cheese = input("Do you want extra cheese ? Enter Y or N: ")
bread = input("Do you want garlic bread ? Enter Y OR N: ")
bill = 0

# Pizza block
if size == "S":
    bill = 15
if size == "M":
    bill = 20
if size == "L":
    bill = 25

#Cheese Block
if cheese == "Y": 
    if size == "S":
        bill += 1
if cheese == "Y": 
    if size == "M":
        bill += 2
if cheese == "Y": 
    if size == "L":
        bill += 3

#Garlic Bread
if bread == "Y":
    bill += 5

print("Your Final Bill is $", bill)
