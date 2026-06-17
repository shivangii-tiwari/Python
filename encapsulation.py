# class A:
#     a =10   # in varible we store dataset
#     b= 20
# print(a)        #kaggle is for database
# ENCAPSULATION
# IT is the concept of oops that means wrapping the data,attributes,varibles ,method inside a function or inside a class thath operate on thath data into a single Unit 
# and ristricting the direct access to the component
# encapculation means it is the process of hideing the detals of an object and allowing the access only through method
# it is a combination ofdata hiding and abstraction
# how to achive the encapsulation?
# we can achive encapculation by access specifier
# three types of access specifier
# 1. public access specifier  # by default all the attributes are public specifier
# 2. protected access specifier #for prodect data use(_)single underscore
# 3. privet access specifier # for privet data use(__)double underscore
# PUBLIC access specifier
class A:
    a='kikiiii'
    def show(self):
        print(self.a)
obj=A()
obj.show()
 #make a parent class A give some attributes and method then create child class B try access the property of classA in classB
class A:
    a='hehe'
    b='sisi' 
class B(A):
    c='fefe'
    d='wewe'
obj=B()
print(obj.a,obj.b,obj.c,obj.d)
# public access specifer
# public member can be access outside the class and also in derive class
# the normal members that we are created in normal class act as apublic member
# there is no need of underscore or any kind of initallization for public specifier
#protected access specifier
#(_) 
class A:   #in this access specifier we can access the attributes of parent class into the chlid class and also modifie it 
    def __init__(self):
        self._name='weeee'
        self._salary='700000000000'
class B(A):
    def show(self):
        print(self._name)
        print(self._salary)
obj = B()
print(obj._name)

class A:
    def __init__(self):
        self._name='weeee'
        self._salary='700000000000'
class B(A):
    def show(self):
        print(self._name)
        print(self._salary)
obj = B()
#print(obj.name)# not working without(_) in it,it only provide partial security
# in protected access specifier in this varible or method that is intented to be access witin the class and it's child class
# in python protected members can be represented by (_)
# we have mention single underscore before the attributr or method name
#privet access specifier
#in this attribute is privet
class A:
    __salary='80000000'
    __company='open AI'
class B(A):
    def show(self):
        print(self.__salary)
        print(self.__company)
obj = B()
        #obj.show()
print(obj._A__salary) # in this way we can access
#SYNTAX = obj_name/class_name._class__att/method => name mangling
#in this method is privet
class A:
    salary='80000000'
    company='open AI'
class B(A):
    def __show(self):
        print(self.salary)
        print(self.company)
obj = B()
obj._B__show()
#in this both are privet  attribute as well as method
class A:
    __salary='80000000'
    __company='open AI'
class B(A):
    def __show(self):
        print(self._A__salary) # attribute is privet so we can access it like (._A__salary) this under method 
        print(self._A__company)
obj = B()
obj._B__show() # method is also privet so we can access it like (._B__show()) this 
# these are the members of the class which will provide security to the members present inside the class
# to make privet members it is compulsory to make use of double under score(__) before the variable name or method name
# privet member cannot be access in the derived class but we can still access by using name mangling





