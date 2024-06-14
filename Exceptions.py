#Basic program, syntax on exceptions
"""try:
    print(name)
except NameError as e:
    print("Some error acurred. Please contact the developer.",e)"""

"""name = "PythonX"
try:
    print(name)
except NemaError as e:
    print("Some error acurred. Please contact the developer.",e)"""

#Example on division
try:
    number1 = int(input("Enter the first number: "))
    number2 = int(input("Enter the Second number: "))
    print("Division is:",number1/number2)
except Exception as e:
    print("Oops, you cannot divide a number by zero")