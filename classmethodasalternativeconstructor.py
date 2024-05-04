'''class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    @classmethod
    def from_string(cls,string):
        name,age=string.split("-")
        return cls(name,int(age))
p=Person.from_string("Wasim Akram-22")
print(p.name)
print(p.age)

class Rectangle:
    def __init__(self,width,hight):
        self.width=hight
        self.width=width
    @classmethod
    def square(cls,size):
        return cls(size,size)
r=Rectangle.square(10)
print(r.width)'''



