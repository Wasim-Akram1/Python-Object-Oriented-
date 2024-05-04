#Class Method
'''class exampleClass:
    @classmethod
    def factorymethod(cls,argument1,argument2):
        return cls(argument1, argument2)'''

class Employee:
    company="Apple"
    def show(self):
        print(f"Name of Employee is {self.name} and works in {self.company} comapany")
    @classmethod
    def ChangeCompany(cls,NewCompany):
        cls.company=NewCompany
e1=Employee()
e1.name="Wasim Akram"
e1.show()
e1.ChangeCompany("Microsoft")
e1.show()
print(Employee.company)
