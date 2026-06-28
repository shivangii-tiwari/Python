# INHERITANCE
# it is a process of inherting or invoking the properties or attribute of parent class to child class is known as inheritance
# how to make inheritance class
#     SYNTAX
# Class <class name>:
#     attrributes/methods
# class <class_2> (class_name):
class Animal:#parent class/super/base class
     a = 'snake'
     b = 'rabbit'
class Bird():#child/derived class
     c = 'kiwi'
     d = 'peacock'
obj = Animal()
print(obj.a,obj.b)
obj_2 = Bird()
print(obj_2.c,obj_2.d)
class Animal:#parent class/super/base class
    a = 'snake'
    b = 'rabbit'
class Bird(Animal):#child/derived class
    c = 'kiwi'
    d = 'peacock'
obj = Bird()
print(obj.c,obj.d,obj.a,obj.b)
# create one inheritance 
# a = parent class
#     b = child class__
#     in class a there is consructor which print hello in class b there is method name display print helloworld
#in class a there is method which show print hello in class b there is method name display print helloworld
class A:
     def show(self):#to access the object memory address
          print('hello')
class B(A):
     def display(self):
          print('hello world')#when your method is already using print don't use print in obj but if it is using return thrn use print
obj = B()
obj.show()
obj.display()
# types of inheritance
# 1. single leve inharitance
# 2. muiti level inharitance
# 3. multiple inharitance
# 4. hierarichial inharitance
# 5. hybrid inharitance
# single level inheritance
# in single level inheritanc they are always only one parent ande one child class present
# in single class child class able to inherit all the propertis which are pesent in parent class
# Syntax 
#  Class <class name>:
#      attrributes/methods
#  class <class_2> (class_name):
#     A/M 
#     create a parent class employe
#     employ name 
#     salary
#     child class(devloper)
#         programming language
#         project
#         display method include
class Employe:
    employe_name = 'kiki'
    salary = '400000'
class Devloper(Employe):
    programming_language = 'python'
    project = 'library managment system'
    def display(self):
        print(self.employe_name)
        print(self.salary)
        print(self.programming_language)
        print(self.project)
obj=Devloper()
obj.display() #find benifit
# Multileve inheritance:
# it is a phenomena of driving properties from parent class or from one class to another class by concidering more than one level
# in this case the last derived class will having all the properties from its parent class
# it can easily assess all the attribute from all the parent class 
# SYNTAX 
# class 1:
#     A/M 
# class 2(1):
#     A/M 
# class 3(2):
#     A/M 
#     .
#     .
#     .
# class bank:
#     constructor
#     branch Name 
#     manager Name
#     class ATM
#     constructor
#     account_no
#     ifcs_code
#     class ATM2(ATM)
#         constructor
      #  print
class Bank:
    def __init__(self):
        self.branch_name = 'ICIC'
        self.manager_name = 'hehe'
class ATM(Bank):
    def __init__(self):
        super().__init__()  #for chaining the constructor
        self.account_no = '44556677'
        self.ifsc_code = '3e4r5t6y'
class ATM2(ATM):
    def __init__(self):
        super().__init__()#super is function because of parentesis
        print(self.branch_name)
        print(self.manager_name)
        print(self.account_no)
        print(self.ifsc_code)  
obj = ATM2()
#constructor chaning we have to chani the constructor from one to another and use to stop the overwriting
# contructor chaning
# it is the process of calling and invoking the parent class constructor inside clild class constructor
# in constructor chaning we have to follow the sayntax
# super().__init__(args)
# class_name.__init__(args)
# method chaning
# it is the process of calling or invoking parent class method inside the child class method
# the SYNTAX : super().method_name(args)#write inside the method
# parent_class_name.method_name(args)
# create a multilevel inheritance
# class a:
#     methods  hello
#     class b(a)
#         method 2  world
#         class c(b):
#             method 3  hello world
class A:
    def show(self):
        print('hello')
class B(A):
    def show(self):
        super().show()
        print('world')
class C(B):
    def show(self):
        super().show()
        print('hello world')
obj=C()
obj.show()

class A:
    def show(self):
        print('hello')
class B(A):
    def show(self):
        A.show(self)
        print('world')
class C(B):
    def show(self):
        B.show(self)
        print('hello world')
obj=C()
obj.show()
# multiple inheritance
# it is the phenomena of deriving the properties from multiple parent class to a single Child class
# SYNTAX 
# class p1:  #father
#     A/M
# class p2:  #mother
#     A/M
# class C:   #CHILD
#     A/M 
# create two parent clSS 
# class A with a method show thath print hello from A
# class B with method display that print hello from B
# CREATE a child class cthat inherit A and B 
class P1:
    def show(self):
        print('hello from A')
class P2:
    def display(self):
        print('hello from B')
class C(P1,P2):
    pass
obj = C()
obj.show()
obj.display()
# hierarichal inheritance
# It is the phenomena of deriving the properties attribute,method from single parent class to multiple child class
# Syntax 
# class A:
#     A/M
# class B(A):
#     A/M 
# class C(A):
#     A/M
# create a parent class vechile with attributes vechile name and vechile number
# create two child class car and bike
# create an object method for car and bike where in car class declare fule
#     type aS an attribute inside that print vechical number,vechical name and fule type same in bike
class Vechile:
    vechile_name='ferrari'
    vechile_number='990099'
    fule_type='petrol'
class Car(Vechile):
    def J(self):
        print(self.vechile_name,self.vechile_number,self.fule_type)
class Bike(Vechile):
    def K(self):
        self.cc='8000'
        print(self.vechile_name,self.vechile_number,self.cc)
obj = Car()
obj2 = Bike()
obj.J()
obj2.K()
# changed name of bike and we can change it because it is object member
class Vechile:  #do with using method and understand how and which change occur
    vechile_name='ferrari'
    vechile_number='990099'
    fule_type='petrol'
class Car(Vechile):
    def J(self):
        print(self.vechile_name,self.vechile_number,self.fule_type)
class Bike(Vechile):
    def K(self):
        self.cc='18000'
        self.vechile_name='royal enfeild'
        print(self.vechile_name,self.vechile_number,self.cc)
obj = Car()
obj2 = Bike()
obj.J()
obj2.K()
# hybrid inheritance
# combination of more than one or two or more type of inheritance
# H.W: debug the code given by sir and remember it and also explore flask and djngo




