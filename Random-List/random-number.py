import random

int1 = random.randint(1156546486, 5165486476)
#int1 = random.random()
print(int1)

toss = random.randint(0 , 1)
if toss == 0:
    print("Heads")
else:
    print("Tails")