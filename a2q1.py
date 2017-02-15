from random import *

num = randint(0,100)

print("The secret number is: " + str(num))

while True:

        guess = (input("Guess a number: "))

        if not guess.isdigit():
            print("Invalid guess, game over!")
            break

        elif int(guess) > num:

            print("Guess lower")

        elif int(guess) < num:

            print("Guess higher")

        else:

            print("Correct, you win!")
            break


            
    




