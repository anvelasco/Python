#Example of an empty Dictionary

"""dict1 = {}
#dictionary with integer keys and string variables
dict2 = {1:"John",2:"Sam"}"""

"""studentsEnrolled = {
    "John":"Python",
    "Sam":"Java",
    "Nick":["Python","JavaScript"],
}
print(studentsEnrolled)"""

#Manipulating Dictionaries

"""example = {1:"John",2:"Nick"}
print(example[1])
print(example.get(2))"""

#Updating Dictionaries

"""example = {1:"John",2:"Nick"}
del example[1]
example[1] = "Den"
example[3] = "Sim"
print(example)"""

#Functions

"""empData = {101:"Bravo",102:"Asten",103:"Kerry"}
print(empData.keys())
print(empData.values())
print(empData.items())

empData.update({104:"Curan",105:"Elly"})
print(empData)"""

#More types

#varDict = {"Asia":["India","UAE","China"],101:"Dalmatians"}
#print(varDict)
"""varDict = {"Asia":["India","UAE","China"]}
varDict["Asia"].append("Japan")
print(varDict)
varDict["Asia"].remove("China")
print(varDict)"""

#Iterating

"""empData = {101:"Bravo",102:"Sten"}
for i in empData:
    print(i)
for i in empData.values():
    print(i)
for i in empData.items():
    print(i)"""