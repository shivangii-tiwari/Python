# ABSTRACTION
# how to achive abstraction
# 3 main components we can achive abstraction
# 1. abstract class
# 2. abstract method
# 3. concret class 
from abc import ABC,abstractmethod #ABC=abstract base class,abc is module 
class vechile(ABC): #create abstract class
    @abstractmethod
    def engine(self):
        pass
class car(vechile):#concret class
    def engine(self):
        print('start the engine')
obj=car()
obj.engine()

class vechile(ABC): #create abstract class
    @abstractmethod
    def engine(self):
        pass
class car(vechile):
    def fule(self): # it gives type error because it didn,t follow the rule
        print('start the engine')
#obj=car()
#obj.engine()
class payment(ABC):
    @abstractmethod
    def pay(self):
        pass
class UPI(payment):
    def pay(self):
        print('payment is done wit UPI')
class creditcard(payment):
        def pay(self):
            print('payment is done wit credit')
class crypto(payment):
    def otp(self):
        print('404')
#a=crypto() # dose not work because we are changing the method name

class payment(ABC):
    @abstractmethod
    def pay(self):
        pass
class UPI(payment):
    def pay(self):
        print('payment is done wit UPI')
class creditcard(payment):
        def pay(self):
            print('payment is done wit credit')
class crypto(payment):
    def pay(self):
        print('404')
a=crypto()
a.pay()
# it is the process of hiding the implimentation details and showing the esstinal features of an object to the user we will try to hide the actual implimentation and only provide the feature
# to achive abstraction we have to make an abstract class for that we have to import(from abc,import ABC,abstract method)
# there are thee main components of abstraction
# 1. abstract class
# 2. abstract method
# 3. concret class 
# abstract method
# it is the method which consist of function declaration but not function implimentation
# to make abstract method we have use abstract Decorator 
# SYNTAX 
# @abstractmethod
# def f_name(self):
#     pass
# abstract class
# it is the class in which we are trying to inherit ABC and it also consist of atleast one abstract method
# it is not possible to create an object using abstract class
#     SYNTAX 
#     from abc import ABC,abstractmethod
#     class <class_name>(ABC):
#        A/M
# concret class 
# it is a class which dosen't consist of any of the abstract method then we can call it as concret class
# its is poissble to create an object using concret class or for concret class
# 1. create an abstract class shape with and a abstract method area then create a child class(rectangle,square)impliment the area method inside child class
class shape(ABC):
    @abstractmethod
    def area(self):
        pass
class rectangle(shape):
    def area(self,a,b):
        print(a*b)
    def perimeter(self,a,b):# we can add extea method uder child class but dont forget the main parent class method
        print(2*(a+b))
class square(shape):
    def area(self,a):
        print(a**2)
a=rectangle()
a.area(2,3)
a.perimeter(2,3)
#abstract can have normal method also
from abc import ABC, abstractmethod

class Vehicle(ABC):

    def start(self):
        print("Vehicle Started")

    @abstractmethod
    def fuel_type(self):
        pass
# 2. create a abstract class employe
# create a abstract method salary(),emp_id(),project()
# create a child class(manager,devloper,tester)
#     implment salary,employ id,project inside manager,devloper and tester
class employe(ABC):
    @abstractmethod
    def salary(self):
        pass
    @abstractmethod
    def emp_id(self):
        pass
    @abstractmethod
    def project():
        pass
class manager(employe):
    def salary(self):
        print('20000000000')
    def emp_id(self):
        print('20')
    def project(self):
        print('kuch v')
class devloper(employe):
    def salary(self):
        print('60000000000')
    def emp_id(self):
        print('50')
    def project(self):
        print('wawoooooo')
class tester(employe):
    def salary(self):
        print('70000000000')
    def emp_id(self):
        print('80')
    def project(self):
        print('feeee')
a=manager()
a.salary()
a.emp_id()
a.project()
b=devloper()
b.salary()
b.emp_id()
b.project()
c=tester()
c.salary()
c.emp_id()
c.project()
#LAMBDA function
def square(a):
    print(a*a)
square(10)
a = lambda a:a**2
print(a(10))
print((lambda a:a**2)(20))
# it is a function which is anonymus in nature it is function withiout name  which is use to declear in one single line
# we have to make use of lambda key word to create a lambda function
# we can pass arguments accoding to the requirment
a=lambda a,b,c:a+b+c
print(a(8,9,7))
#SYNTAX:
# lambda argument: expression
# lambda a1,b1,c1: expression
# where it will return substraction
a=lambda a,b,c:a-b-c
print(a(8,9,7))
# write a program to check wether the number is greater or not if the number is greaater print hii else print byy by using lambda function
a=lambda a,b:print('hii')if a>b else print('bye')
a(2,3)
# SYNTAX (if-else/condition)
# lambda argument:value if cond1 else value2
a=lambda a,b:'hii' if a>b else 'bye'
print(a(7,6))
#SYNTAX 
#lambda argument:value1 if cond1 else value2 if cond2 else value3 if cond3
#WAP to print cube if value is oddelse squar if the value is even
q=lambda a : print(a**3) if a%2!=0 else print(a**2)
q(4)
w=lambda a,b,c:print(a) if a>b and b>c else print(b)if b>c  else print(c)#print gratest among 3 number
w(1,2,3)
e=lambda a: print('+')if a>0 else print('-')if a<0 else print(0)#check the number is positive,negative or zero
e(-1)
c=lambda a,b:print(a*b) if a>0 and b>0 else print('fuck you') #print area of rectangle
c(2,-3)
h=lambda p,r,t:print(p*r*t/100)#print simple intrest
h(20000000000000,5,6)
# mapping(map())
# SYNTAX 
# map(collection,function)  
a = [6,7,8,9,]
# b=map(a,lambda x:x*x)
# print(b) #modified it niche
b=map((lambda x:x*x),a)#without list it will return address

for i in b:
    print(i)# after that it will return empty list because object is finished
print(list(b))
#it is a function which is use to perform same set of operation for each and every value present inside the collection
q =['snake','rahul','kiki']
b=map(lambda x:x.upper(),q)
print(list(b))
#1
Q=[6,7,8,9]
y=map((lambda x:(x**2,x**3)),Q)
print(list(y))
#2
r = [200,800,900]
u=map(lambda x:x+(x*18/100),r)
print(list(u))
#3
l=['kiki','hehe','fefe']
w=map(lambda x:x[-1],l)
print(list(w))
#4
a=[60,120,180,300]
c=map(lambda x:x/60,a)
print(list(c))
#5
a=[2,3,4]
b=[6,7,8]
c=[8,9,1]
s=map(lambda x,y,z:(x+y+z),a,b,c)
print(list(s))
#6
d=[40,97,68,3]
v=map(lambda x:'even'if x%2==0 else 'odd',d)

print(list(v))
#7
s=['python','java','react','django']
n=map(lambda x:len(x),s)
print(list(n))
#8
w=[100000,500000,6000000]
l=map(lambda x:x-0.1*x,w)
print(list(l))
#9
k=['python','java','react']
b=map(lambda x:x[::-1],k)
print(list(b))
#10
k = [95,72,55,35,88]
m=map(lambda x: 'A'if x>80 else 'B'if x>70 else 'C'if x>50 else 'fail',k )
print(list(m))
#bonous
r=['hihi','wewe','sisi','didi']
j=[70,80,90,30]
n=map(lambda x,y:f'{x}-pass'if y>40 else f'{x}-fail',r,j)#use of fstring to insert the value under string
print(list(n))


    

