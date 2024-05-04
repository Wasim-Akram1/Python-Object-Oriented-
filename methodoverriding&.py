'''class Shape:
    def __init__(self, x, y):
        self.x=x
        self.y=y
    def Area(self):
        return self.x*self.y
class Circle(Shape):
    def __init__(self, radius):
        self.radius=radius
        super().__init__(radius,radius)
    def Area(self):
        return 3.14*super().Area()
rec=Shape(3,5)
print(rec.Area())
c=Circle(5)
print(c.Area())

class Shape:
    def Area(self):
        pass
class Cirlce(Shape):
    def __init__(self,radius):
        self.radius=radius
    def Area(self):
        return 3.14*self.radius*self.radius
c=Cirlce(5)
print(c.Area())'''

class Shape:
    def Area(self):
        print("Calculating Area...")
class Circle(Shape):
    def __init__(self,radius):
        self.radius=radius
    def Area(self):
        print("Calculating the Area of circle:-")
        super().Area()
        return 3.14*self.radius*self.radius
c=Circle(5)
print(c.Area())


    
