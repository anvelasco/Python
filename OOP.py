#Classes basics
"""class Employee:
    empName = "John"
    age = 35
    designation = "Manager"

empOne = Employee()
empTwo = Employee()
print(empOne.empName)
print(empTwo.empName)"""

#Class is rigid therfore objects are immutable

#Non rigid class

"""class Employee:
    def __init__(self,empName,age,designation):
        self.empName = empName
        self.age = age
        self.designation = designation

empOne = Employee('John',35,'Manager')
empTwo = Employee('Sam',26,'Python Developer')
print(empOne.empName)
print(empTwo.empName)"""

#Adding methods

class Employee:
    totalEmployees = 0
    
    def __init__(self,empName,age,designation,salary):
        self.empName = empName
        self.age = age
        self.designation = designation
        self.salary = salary
        Employee.totalEmployees = Employee.totalEmployees+1

    def getEmpDetails(self):
        return self.empName,self.age,self.designation,self.salary
    
    def updateSalary(self,newSalary):
        self.salary = newSalary
        print('Salary updated')
        return self.salary
    
class Intern(Employee):
    
    def __init__(self, empName, age, designation, salary,internPeriod):
        self.internPeriod = internPeriod
        Employee.__init__(self,empName,age,designation,salary)

    def getPeriod(self):
        return 'Internship period (in months) is',self.internPeriod


empOne = Employee('John',35,'Manager',35000)
print(empOne.getEmpDetails())

empTwo = Employee('Sam',26,'Python Developer',27000)
print(empTwo.getEmpDetails())

empOne.updateSalary(40000)
print(empOne.getEmpDetails())
print(Employee.totalEmployees)

internOne = Intern('Tom',22,'Marketing Intern',12000,6)
print(internOne.getEmpDetails())
print(internOne.getPeriod())