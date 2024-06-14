"""data = set()
print(type(data))"""

"""setOne = {1,2,3}
setTwo = {6,8.9,"James"}
print(setOne)
print(setTwo)"""

#Accessing Data

"""days = {"Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"}
#print(days)
for day in days:
    print(day)"""

#Operations

"""A = {1,2,3,4,5}
B = {4,5,6,7,8}
#using | operator
print(A|B)
#using union method
print(A.union(B))
#using & operator
print(A&B)
print(A.intersection(B))
#using - operator
print("A-B=",A-B)
print("B-A=",B-A)
#using diference() method
print("A-B=",A.difference(B))
print("B-A=",B.difference(A))"""

#Built in functions

"""age = {23,22,34,36,24,41}
print(len(age))
print(min(age))
print(max(age))"""

#Methods

"""age = {23,22,34,36,24,41}
age.add(56)
print(age)
age.remove(22)
print(age)
age.pop()
print(age)"""

"""A = {1,2,3
B = {1,2,3,4,5}
C = {100,101,102}
print(A.issubset(B))
print(B.issuperset(B))
print(A.isdisjoint(B))
print(A.isdisjoint(C))"""

bricsNations = {"B","R","I","C","S"}
bricsNations.discard("Z")
print(bricsNations)
bricsNations.remove("Z")
print(bricsNations)