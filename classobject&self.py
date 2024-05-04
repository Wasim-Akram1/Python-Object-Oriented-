#Class & Object
'''class Details:
    name="Wasim Akram "
    age=22
obj1=Details()
print(obj1.name)
print(obj1.age)'''

#Self Parameter
'''class Details:
    name="Wasim Akram"
    age=22
    def desc(self):
        print(f"My name is {self.name} and i am {self.age} year old.")
obj1=Details()
obj1.desc()'''

#Practice
'''class Vehicle:
    max_speed="180km/hr."
    milege="20km/l"
Alto=Vehicle()
print(Alto.max_speed)
print(Alto.milege)'''

class Vehicle:
    max_speed="180km/hr."
    milege="20km/l"
    def desc(self):
        print(f"I Have Purchased a car with {self.max_speed} max speed and {self.milege} milege")
alto=Vehicle()
alto.desc()
