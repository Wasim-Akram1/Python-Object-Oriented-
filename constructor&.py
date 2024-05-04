#Parameterized Constructor
'''class Details:
    def __init__(self,animal,group):
        self.animal=animal
        self.group=group
obj1=Details("Crab","Crustaceans")
print(f"{obj1.animal} belongs to {obj1.group}")'''

#Default Constructor:
class Details:
    def __init__(self):
        print("Crab belong to Crustacians")
obj1=Details()
