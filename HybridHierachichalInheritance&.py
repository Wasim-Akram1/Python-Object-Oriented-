'''class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def showdetails(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")

class Person(Human):
    def __init__(self, name, age, address):
        super().__init__(name, age)
        self.address = address

    def showdetails(self):
        print(f"Address: {self.address}")

class Program:
    def __init__(self, programname, duration):
        self.programname = programname
        self.duration = duration

# Example usage
program = Program("Computer", 4)
person = Person("John Due", 25, "123 main st.")  # Removed the 'program' argument
person.showdetails()'''

#Hierarchichal Inheritance
class Animal:
    def __init__(self,name):
        self.name=name
    def showdetails(self):
        print(f"name:-{self.name}")
class Dog(Animal):
    def speak(self):
        return f"{self.name} says Bho"
class Cat(Animal):
    def speak(self):
        return f"{self.name} speak meow"
d=Dog("Buddy")
c=Cat("Whiskers")
print(d.speak())
print(c.speak())
