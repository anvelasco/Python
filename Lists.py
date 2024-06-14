#empty list

"""list1 = []"""

#list with values of the same type

"""list2 = [1,4,6,3,9]"""

#list with different data types

"""list3 = ["John",23,56.0,True]"""

#class enrrolled

"""coursesEnrolled = ["Python","Ruby","Java"]
print(coursesEnrolled)"""

#Accesing elements in a list

"""names = ["John","Sam","Barry","Lin"]
print(names)
print(names[0])
print(names[3])"""

#Slicing lists

"""names = ["John","Sam","Barry","Lin"]
print(names)
print(names[1:3])
print(names[2:])"""

#Updating lists

"""marks = [56,76,69,71,39]
marks[4] = 43 #Using the index to update the new value
print(marks)"""

#Deleting elements/lists

"""names = ["John","Sam","Barry","Lin"]
print(names)
del names[1]
print(names)
del names"""

#Operations on strings

"""list1 = [1,2,3]
list2 = [4,5,6]
print(list1+list2)
print(list1*3)

enrolledList = ["Sam","Mike","Kane","Nick"]
print("Sam" in enrolledList)
print("Samuel" in enrolledList)"""

#Iteration

fruits = ["Apple","Mango","Cherry","Banana"]
for i in fruits:
    if i == "Mango":
        print("Mango Found")
        break
else:
    print("Mangooo not found")