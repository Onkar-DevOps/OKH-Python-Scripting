import random
game = ["Rock", "Paper", "Scissors"]

your_choice = int(input("Please enter your choice Rock = 0 Paper = 1 Scissors = 2 : "))
your_choice = game[your_choice]
computers_choice = random.choice(game)

print("Your choice is ", your_choice)
print("Computers choice is ", computers_choice)


if your_choice == "Rock" and computers_choice == "Scissors":
    print("You win")
elif your_choice == "Paper" and computers_choice == "Rock":
    print("You win")
elif your_choice == "Scissors" and computers_choice == "Paper":
    print("You win")
elif your_choice == "Scissors" and computers_choice == "Rock":
    print("You Loose")
elif your_choice == "Rock" and computers_choice == "Paper":
    print("You Loose")
elif your_choice == "Paper" and computers_choice == "Scissors":
    print("You Loose")
else:
    print ("Its a Draw")