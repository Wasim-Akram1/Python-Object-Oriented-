#Public 
'''class Student:
    def __init__(self, age, name):
        self.age=age
        self.name=name
obj=Student(22,"Wasim Akram")
print(obj.age)
print(obj.name)

#Private
class Student:
    def __init__(self, age, name):
        self.__age=age
        def __funcname(self):
            self.y=34
            print(self.y)
class Subject(Student):
    pass
obj=Student(22,"Wasim")
obj1=Subject
#print(obj.__age)
#print(obj.__funcname)
#print(obj1.__age)
print(obj1.funcname())

#Name Mangling
class Myclass:
    def __init__(self):
        self._private="I am private attribute"
        self.__mangled="I am mangled attribute"
Myobj=Myclass()
print(Myobj._private)
print(Myobj._Myclass__mangled)
print(Myobj.__mangled)'''

#Protected
class Student:
    def __init__(self):
        self._name="Wasim Akram"
    def _funcname(self):
        return "Python with wasim"
class Subject(Student):
    pass
obj=Student()
obj1=Subject()
print(obj._name)
print(obj._funcname())
print(obj1._name)
print(obj1._funcname())

