class Employee:
    def __init__(self,name,id):
        self.name=name
        self.id=id
    def showDetail(self):
        print(f"the name of employee {self.id} is {self.name}")
class Programmer(Employee):
    def showLanguage(self):
        print("The default language is Python")
e1=Employee("Wasim Akram", 60)
e1.showDetail()
e2=Programmer("Farhan Khan",40)
e2.showDetail()
e2.showLanguage()
