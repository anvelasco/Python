#Range function

"""print(list(range(5)))#single argument signifies the end of the range (excluded)
print(list(range(1,5)))#two arguments signifies start and end of the range
print(list(range(1,10,2)))#three arguments signifies step size"""

#For loop

"""for i in range(5):
    print(i)

for i in range(5):
    print("PythonX")

for i in "PythonX":
    print(i)"""

#While loop

"""i = 0
while i<3:
    print("I Love Python")
    i=i+1"""

#Break statement

"""str = "Goodmorning"
for i in str:
    if i == "m":
        break
    else:
        print(i)"""

#Multiplication table exersize

"""num = int(input("Please enter the number to evaluate: "))
for i in range(1,11):
    print(i*num)"""

#Even numbers

num = int(input("Enter the number to end the sequence: "))
i = 0
while i<=num:
    if i%2 == 0:
        print(i)
    i=i+1