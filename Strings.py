#Basic strings

"""username = input("Please enter your name ")
print("Hello", username)"""

#Formated Strings

"""name = input("Enter your name: ")
age = input("Enter your age: ")
print(("Hello, {}. You are {} years old").format(name,age))"""

#F-strings

"""name = input("Enter your name: ")
print(f"Hello, {name}!")"""

"""num1 = 5
num2 = 10
print(f"five plus ten is {num1 + num2}")"""

#Indeces

"""appName = "PythonX"
print(appName[0])
print(appName[2])"""

#Slicing

"""appName = "PythonX"
print(appName[:4])
print(appName[2:5])
print(appName[3:])
print(appName[::2])"""

#Simple operations

#concatenation

"""firstname = "John"
lastname = "Doe"
fullname = firstname+" "+lastname
print(fullname)

print(" ".join([firstname, lastname]))"""

#repetition

"""str = "Python"
print(str*2)"""

#Methods

str = "Python"
print(str.islower())
print(str.upper())
print(str.lower())
print(str.replace('P','A'))

str1 = "Love Python"
print(len(str1))

