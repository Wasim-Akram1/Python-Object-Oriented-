#class Varible
'''class Myclass:
    classVariable=0
    def __init__(self):
        Myclass.classVariable+=1
    def printclassVariable(self):
        print(Myclass.classVariable)
obj1=Myclass()
obj2=Myclass()
obj1.printclassVariable()
obj2.printclassVariable()'''

#Instance Variable
'''class Myclass:
    def __init__(self,name):
        self.name=name  #Instance Variable
    def printName(self):
        print(self.name)
obj1=Myclass("Wasim")
obj2=Myclass("Ramiz")
obj1.printName()
obj2.printName()'''

class Employee:
    company="Apple"
    noofemployees=0
    def __init__(self, name):
        self.name=name
        self.raiseamount=0.02
        Employee.noofemployees+=1
    def showDetails(self):
        print(f"the name of employee is {self.name} with {self.raiseamount} raise in {self.noofemployees} sized {self.company} company")
emp1=Employee("Wasim")
emp1.raiseamount=0.05
emp1.company="TCS"
Employee.showDetails(emp1)
emp2=Employee("Ramiz")
Employee.showDetails(emp2)

