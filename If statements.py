# Basic exersize

"""age = int(input("Enter your age: "))
if age >= 18:
    print("Congrats, you are alegible to vote!")
else:
    print("Sorry, you are not elegible to vote")"""

# Elif exersize

"""marks = int(input("Enter the grade in percentage: "))
if marks >= 90:
    print("Grade: Excelent")
elif marks <90 and marks >= 75:
    print("Grade: First Class") 
elif marks < 75 and marks >= 40:
    print("Grade: Average") 
else:
    print("Grade: Fail") """

# Nested exersize

"""username = input("Enter your username: ")
password = input("Enter your password: ")
if username == "John":
    if password == "12345":
        print("Login succesful")
    else:
        print("Incorrecct password")
else:
    print("User not found")"""

# Traffic light

"""light = input("Which color is the light on?")
if light == "Green":
    print("Go")
elif light == "Yellow":
    print("Slow down")
else:
    print("Stop")"""


# Game score

user1 = 9
user2 = 4
user3 = 7
if (user1 > user2) and (user1 > user3):
    print("User one scores highest!")
elif (user2 > user1) and (user2 > user3):
    print("User two scored highest!")
else:
    print("User three scored highest!")