class Student:
    def __init__(self,name,age,number):
        self.name = name
        self.age = age
        self.number = number

    def __str__(self):
        return f"{self.name} : {self.age} : {self.number}"

s1 = Student("Vihren",16,20108)
print(s1)

class Select:
    def __init__(self,column,value):
        self.column = column
        self.value = value
        


    def __str__(self):
        sum = self.value + self.column
        return f"{self.column} + {self.value} = {sum}"


    @staticmethod
    def func (atr):
        print(atr)
