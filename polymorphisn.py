# poly = many,morphism = forms(method overloading is not possible in python)
# polymorphism makes code flexible
# POLYMORPHISM
# it is the phenomena of making the same operator or method to perform two or more operation #search concadination
# a =(4,5,6)
# b = (7,8,9)
# print(a+b)                internal operation of additon (it calls the function(__add__())its is called dunder,magic method(simlarly for __sub__(),__mul__(),__div__()))
s = {2,3,4}                 #add is example of multitasking
d = {4,5}
# print(s+d)
print(s.union(d))#in this way we add set by using union
print(int.__add__(10,20)) #dunder method
print(int.__mod__(10,20)) # for modules
# three types of division (__truediv__(),__mod__,__div__())
# HOW TO ACHIVE POLYMORPHISM
# * operator overloading
# * method overloading
# * method overridding (if method name is same then it overwrite the value and call the last value)
# OPERATOR OVERLOADING
class A:
    def __init__(self,a):
        self.a=a 
    def __add__(self,other):#other for other int we use
        return self.a+other.a  # return fuction means code loop se bahar
    
obj=A(10)                                            #we have to use optimize code so it work for all user
obj2=A(20)
print(obj+obj2) # not supporting addition use dunder method
# OPERATOR OVERLOADING
class A:
    def __init__(self,a):
        self.a=a 
    def __add__(self,other,shivi,hehe):
        return self.a+other.a+shivi.a+hehe.a
obj=A(10)                                            
obj2=A(20)
obj3=A(50)
obj4=A(90)
print(obj.__add__(obj2,obj3,obj4)) # if dont want to use'+' then u can use __add__.  
class A:
    def __init__(self,a):
        self.a=a 
    def __add__(self,other):#other for other int we use
        print (self.a+other.a)  # return fuction means code loop se bahar
        print (self.a-other.a)
obj=A(10)                                            #we have to use optimize code so it work for all user
obj2=A(20)
(obj+obj2)
class A:
    def __init__(self,a):
        self.a=a 
    def __add__(self,other):#other for other int we use
        yield (self.a+other.a)  # multtipul return so we use yeild keyword
        yield (self.a-other.a)
obj=A(10)                                            #we have to use optimize code so it work for all user
obj2=A(20)
(obj+obj2)
#METHOD OVERRADDING
class A:
    def display(self):
        print('a python')
    def display(self):
        print('hello')
    def display(self):
        print('TATA')
obj = A()
obj.display()
#MONKEY PATCHING
class A:
    def display(self):
        print('a python')
    a = display # this varible store the address of function
    def display(self):
        print('hello')
    b = display
    def display(self):
        print('TATA') # we cannot use super because parent class is neccessary for it
    c = display
obj = A()
obj.b()# so it call the  particular function b because it stores the address of it
# when we use same fuction name for two or more operation then the first fuction address overwrite by the address of next function
#     if you want to access the particular method we have to use of monkey patching
# MONKEY PATCHING
# it is the process of storing previous method address to a varible and accessing that method using the varible
#METHOD OVERLOADING
# same method work for diffrent parameter is method over loading
# it works in java not in Python
# it is the process of using same method name to perform two or more diffrent operation
# in python we are going to perform method overloading it will act as a method overwriting but in python  we can achive method over loading with the help of default parameter 
# class Test {
java works for method over loading
    void add(int a, int b){
        System.out.println(a+b);
    }

    void add(int a, int b, int c){
        System.out.println(a+b+c);
    }

    void add(int a, int b, int c, int d){
        System.out.println(a+b+c+d);
    }
} 
python do not work for method overloading
class Test:

    def add(self,a,b):
        print(a+b)

    def add(self,a,b,c):
        print(a+b+c)

obj = Test()

obj.add(10,20)
in this way we make work method overloading in python
class A:
    def display(self,*a):
        print(sum(a))
obj=A()
obj.display(10)
obj.display(10,30)
obj.display(10,100,144,66,78)
