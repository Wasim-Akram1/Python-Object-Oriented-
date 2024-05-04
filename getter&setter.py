#Getter
'''class Myclass:
    def __init__(self,value):
        self._value=value
    @property #Getter
    def value(self):
        return self._value
obj=Myclass(10)
print(obj.value)'''

#Setter
class Myclass:
    def __init__(self, value):
        self._value=value
    @property
    def value(self):
        return self._value
    @value.setter
    def value(self,new_value):
        self._value=new_value
obj=Myclass(20)
obj.value=20
print(obj.value)
