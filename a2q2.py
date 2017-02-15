factorial = 1

fact = input("Enter an integer: ")


while not fact.isdigit():
        print('Invalid input')
        fact = input("Enter an integer: ")

fact2 = fact

fact = int(fact)

while fact > 1:

    fact -= 1
    factorial = factorial*(fact+1)

print('The factorial of', fact2, 'is', factorial)
