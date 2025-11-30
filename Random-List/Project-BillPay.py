import random
friends = ["Onkar", "Sukanya", "Sidharth", "Prachi", "Sudarshan"]

# option 1
print("Bill Will be paid by : ", friends[random.randint(0, 4)])

# option 2
# Use random.choice to pick an element directly (safer and cleaner than randint with indices).
# In this case you dont need to provide the last number of the list hence you dont need to know how many elements are there in the list.
print("Bill Will be paid by : ", random.choice(friends))
