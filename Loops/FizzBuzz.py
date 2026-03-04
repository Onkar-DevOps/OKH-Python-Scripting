for number in range(1, 101):
    if (number%15) == 0:
        print("FizzBuzz")
    elif (number%5) == 0:
        print("Buzz")
    elif(number%3) == 0:
        print("Fizz")
    else:
        print(number)
#
#
# Division by number 15 is applied first
# Becuase if the number is devided by 15 then it should be replaced by fizzbuzz
# And no other condition should apply 