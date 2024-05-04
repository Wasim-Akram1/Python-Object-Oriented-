class Animal:
    def __init__(self,name,species):
        self.name=name
        self.species=species
    def makesound(self):
        print("Sound Made by Animal")
    def colour(self):
        print("Colour of the animal is")
'''class Dog(Animal):
    def __init__(self,name,breed):
        self.breed=breed
    def makesound(self):
        print("Bark")
d=Dog("Dog","BullDog")
d.makesound()
a=Animal("Dog","Dog")
a.makesound()'''

class Cat(Animal):
    def __init__(self,name,domain):
        self.domain=domain
    def colour(self):
        print("Brown")
a1=Animal("cat","cat")
a1.colour()
c=Cat("Cat","Cat")
c.colour()
