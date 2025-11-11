print("Welcome to the Tip Calculator - Tipwise")
bill = float(input("What was the total bill ? "))
tip = int(input("How much tip would you like to pay 10, 12 or 15 ? "))
people = int(input("How much people to split the bill: "))

final = (tip / 100 * bill + bill) / people
contry = round(final, 2)

print("Each person should pay $ ", contry)