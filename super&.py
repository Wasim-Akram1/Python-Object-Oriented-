'''class Parentclass:
    def Parentmethod(self):
        print("This is Parent Method")
class Childclass(Parentclass):
    def Childmethod(self):
        print("This is child method")
        super().Parentmethod()
Child_object=Childclass()
Child_object.Childmethod()'''

class Employee:
    def __init__(self, name, id):
        self.name=name
        self.id=id
class Programmer(Employee):
    def __init__(self,name ,id , lang):
        super().__init__(name, id)
        self.lang=lang
Wasim=Employee("Wasim Akram", 60)
Ramiz=Programmer("Ramiz Khan",41,"Python Developer")
print(Wasim.name)
print(Wasim.id)
print(Ramiz.name)
print(Ramiz.id)
print(Ramiz.lang)
