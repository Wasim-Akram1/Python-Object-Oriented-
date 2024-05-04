'''class Animal:
    def __init__(self,name,species):
        self.name=name
        self.species=species
    def makesound(self):
        print("Sound made by animal")
class Mammal:
    def __init__(self,name,colour):
        self.name=name
        self.colour=colour
class Dog(Animal,Mammal):
    def __init__(self,name,breed,colour):
        Animal.__init__(self,name,species="Dog")
        Mammal.__init__(self,name,colour)
        self.breed=breed
    def makesound(self):
        print("Bark")
a=Animal("Dog",("Bull Dog"))
a.makesound()
d=Dog("Dog","Bull Dog","Red")
d.makesound()'''

class Employee:
    def __init__(self, name):
        self.name=name
    def show(self):
        print(f"The name is {self.name}")
class Dancer:
    def __init__(self,dance):
        self.dance=dance
    def show(self):
        print(f"The dance is {self.dance}")
class DancerEmployee(Employee, Dancer):
    def __init__(self,dance,name):
        self.dance=dance
        self.name=name
o=DancerEmployee("Kathak","Pragati")
print(o.name)
print(o.dance)
