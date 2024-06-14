import math

# Basics of math module

"""print(math.sqrt(4))
print(math.fabs(-5))
print(math.floor(4.6))
print(math.pow(2,2))
print(math.trunc(7.999))"""

# Trgonometry

"""print(math.sin(0))
print(math.sin(3))
print(math.tan(3))
print(math.cos(3))"""

# Constants

"""print(math.pi)
print(math.tau)
print(math.e)
print("Positive infinity:",math.inf)
print("Negative infinity:",-math.inf)"""

# Circle exersize

"""radius = int(input("Enter the radius:"))
area = math.pi*radius*radius
print("The area is:",area)"""

# Randomness

"""import random
#Generate random number between 0 and 1
print(random.random())
#Generate random number between 1 and 100
print(random.randint(1,100))
#Generate random number between 1 and 10
print(random.randrange(1,10))
#Generate random number between 1 and 10 in steps of 2
print(random.randrange(1,10,2))"""

#Game

import random
generatedNumber = random.randrange(1,10)
userGuess = int(input("Guess a number between 1 and 10 "))
if userGuess == generatedNumber:
    print("You got it!")
elif userGuess < generatedNumber:
    print("Number too low")
else:
    print("Number too high")