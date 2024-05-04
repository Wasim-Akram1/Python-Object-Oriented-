class Animal:
    def __init__(self,name,species):
        self.name=name
        self.species=species
    def showdetails(self):
        print(f"Name:-{self.name}")
        print(f"Species={self.species}")
class Dog(Animal):
    def __init__(self,name,breed):
        Animal.__init__(self,name,species="Dog")
        self.breed=breed
    def showdetails(self):
        Animal.showdetails(self)
        print(f"breed:-{self.breed}")
class Goldenretriver(Dog):
    def __init__(self,name,color):
        Dog.__init__(self,name,breed="Goldenretrievar")
        self.color=color
    def showdetails(self):
        Dog.showdetails(self)
        print(f"color:-{self.color}")
o=Goldenretriver("Max","Golden")
o.showdetails()
