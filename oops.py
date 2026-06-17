# in oops we are having two imp terms
# 1. class:blueprint of object
# 2. object:it is isinstance of object
# class:
#     Syntax:
#         class class_name:
#             properties\behaviour(inshort classbody)
# object:
# object is a real world entity that is created from class 
#     syntax:
#     obj_name=Class_name(arguments)  #here arguments are optional

# advantage:
# help to solve real world problem
# reduce the line of code
# without argument
# object=Cname()
# 
# it creats an object when we call the address
# the object address should be stored in varible
# Types of class:
#     1. inbuild:all the datatypes are inbuild class because they are predefine
#     2. userdefine: the class which are created by user are user define class

# class Creation:
# a =23
# d =3
# demo=Creation()
# print (type(demo))
# memory allocatin:
# whenever we want access the values from the class or object we have to use Syntax
# class Creation:
#     a =23
#     b =89

# demo1 =Creation()
# demo2 =Creation()
# print(type(demo1))
# print(Creation.a,Creation.b)
# print(demo1.a,demo2.b)
# print(demo2.a,demo2.b)

# class Bank:
#     bname='SBI'
#     loc='korea'
#     manager='kikki'
# cus1=Bank()
# cus2=Bank()
# print(Bank.bname,Bank.loc,Bank.manager)
# print(cus1.bname,cus1.loc,cus1.manager)
# print(cus2.bname,cus2.loc,cus2.manager)
#     #modifying class
# Bank.loc='chandigarh'
# print(Bank.bname,Bank.loc,Bank.manager)
# print(cus1.bname,cus1.loc,cus1.manager)
# print(cus2.bname,cus2.loc,cus2.manager)
#     #modifying object
# cus1.loc='london'
# print(Bank.bname,Bank.loc,Bank.manager)
# print(cus1.bname,cus1.loc,cus1.manager)
# print(cus2.bname,cus2.loc,cus2.manager)
# cus2.loc='paris'
# print(Bank.bname,Bank.loc,Bank.manager)
# print(cus1.bname,cus1.loc,cus1.manager)
# print(cus2.bname,cus2.loc,cus2.manager)

#conclusion:
# modification done with respect to class will affect all the objects
# REASON:object are instance of the class

# modification done with respect to object will not affect the class and other objects
# REASON:Class are not depending on object
# states\property
# the data or a information stored inside a class\object is known as propertyof the class\object.object
#           or
# the variables or funcnality storing  inside the class are called states

# there are 2 types of states
# 1. genric states\class\static
# 2. specific\object
# these are the properties which will be come for every object

# genric state 
# the properties which are commom for all object is genric state
#example
# class School:
#     Sname='scottish public school'
#     loc= 'scottland'
#     principle = 'takla'
#     timing = '9:30AM-3:30PM'
# st1=School()
# print(School.Sname,School.loc,School.principle,School.timing)
# print(st1.Sname,st1.loc,st1.principle,st1.timing)

# specific state
# the  properties or functnality which will create outside the class after the object creation is specific state 
#  class School:
#     Sname='DPS'
#     loc='dehli'
#     principal='kooki'
#     timing='1:30PM-3:30PM'
# St1=School()
# St1.name='triiii'
# St1.id=45
# St1.age=30

# St2=School()
# St2.name='weeeee'
# St2.id=56
# St2.age=25
# print(St1.name,St1.id,St1.age)
# print(St2.name,St2.id,St2.age)
# difference between method and function
# function which we declar inside the class is called method
# if we declar function outside the class is called function
# example function
# def add():
#     print('hii')

# add()
# Method example
# class Demo:
#     def sho():
#         print("hii")

# Sho()

# contructor/__init__/initialisatrion
# constructor is special method
# it runs automatically when an object is created
# *it is used to initialize the member of the object
# *no need of calling the method,by default it will excute when we create object
# *self is mendatory argument to pass for the __init__ method
# we can pass argument in the object creation only if there is __init__method present inside the class
# __init__is the constructor method in Python 
# for__init__method,passing self is mandatory to store the address of the object
# syntax:
# class Cname:
#     block of Code 
# def __init__(self,var1,var2,....,var n)
#     self.var1=var1
#     self.var2=var2
#     .
#     .
#     self.varn=varn
# obje_name=Cname(val1,val2,...val n)
# class School:
#     Sname= 'caremal'
#     loc='nyc'
#     principal='vartika'
#     time='8:30am-6:30am'
#     def __init__(self,name,sid,age,bg):
#      self.name=name
#      self.age=age
#      self.sid=sid
#      self.bg=bg 
# st1=School('shivi',34,19,'ab-')
# print(st1.name,st1.sid,st1.age,st1.bg)
# st2=School('kiwi',56,18,'ab+')
# print(st2.name,st2.sid,st2.age,st2.bg)
# create a company having three class member one object with four object member 
class Company:
      Cname='hybe'
      loc='korea'
      CEO='shivangi'
      def __init__(self,ename,eid,salary,department):
       self.ename=ename
       self.eid=eid
       self.salary=salary
       self.department=department
ep1=Company('rishi',34,400000,'AI')
ep2=Company('kiki',56,50000,'DA')
ep3=Company('palak',23,30000,'applied science')
ep4=Company('niya',45,80000,'statics')
print(ep1.ename,ep1.eid,ep1.salary,ep1.department)
print(ep2.ename,ep2.eid,ep2.salary,ep2.department)
print(ep3.ename,ep3.eid,ep3.salary,ep3.department)
print(ep4.ename,ep4.eid,ep4.salary,ep4.department)
# class Makeup:
#   def __init__(self,brand,shade,price,sumdge proof)
#    self.brand=brand
#    self.shade=shade
#    self.price=price
#    self.sumdge proof=sumdge proof
#  m1=Makeup('mars',burnt red,2000,'no')
#  m2=Makeup('channel',cheery red,4500,'no')
#  m3=Makeup('laykme',chocolate brown,200,'yes')
#  m4=Makeup('blue heaven',pink,3000,yes)
#  print(m1.brand,m1.shade,m1.price,m1.sumdge proof)
# WAP to do write shift operation (k value is 3) question=1,2
# chochelet,string,logic2
e = [1,2,3,4]

last = e.pop()      # removes last element
e.insert(0, last)   # insert at beginning

print(e)

e = [1,2,3,4]
k = 3

for i in range(k):
    last = e.pop()
    e.insert(0, last)

print(e)

D = 'kiki'
len = len(D)
len = len//2
hehe=''



