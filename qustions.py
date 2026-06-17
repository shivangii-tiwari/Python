#1
class Animal:
    def eat(self):
        print('speices')
class Dog(Animal):
    def bark(self):
        print('bark_bark')
obj=Dog()
obj.eat()
obj.bark()
#2
class Employee:
    employe_name='kiki'
    salary='678900000000000'
class Devloper(Employee):
    programming_language='python'
obj=Devloper()
print(obj.employe_name,obj.salary,obj.programming_la)

