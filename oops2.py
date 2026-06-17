# METHODS
# it has 3 type
# 1.object method
# 2. class method
# 3. static method
# obj method:the method which is use to perform and some operation on the object member is called object method
# they are used to access and modify the object members
# it is compulsory to pass self to store the address of object
# SYNTAX:
# class Cname:
#     statment Block 
#     def MEthod name(self):  #to access
#         print(args)
#     def Mname(self,new):  #to modify
#         self.var=new
#     obj=Cname(val1,val2,....val n)
#     obj.Mname()
# class School:
#         sname='SPS'
#         loc='araria'
#         principal='hehe'
#         timing='2:30PM-4:30PM'
#         def __init__(self,name,age,sid,bg):
#             self.name=name
#             self.age=age
#             self.sid=sid
#             self.bg=bg 
#         def display(self):
#             print(self.name,self.sid,self.age,self.bg)
#         def ch_age(self,new):
#             self.age=new
# st1= School('kiki',19,23,'B+')
# st1.display()
# st1.ch_age(30)
# st1.display()
# iclass Company:
#       Cname='hybe'
#       loc='korea'
#       CEO='shivang'
#       def __init__(self,ename,eid,salary,department):
#        self.ename=ename
#        self.eid=eid
#        self.salary=salary
#        self.department=department
#       def display(self):
#         print(self.ename,self.eid,self.salary,self.department)
#       def ch_ename(self,new):
#         self.ename=new  
# ep1 = Company('rishi',34,400000,'AI')
# ep2 = Company('kiki',56,50000,'DA')
# ep3 = Company('palak',23,30000,'applied science')
# ep4 = Company('niya',45,80000,'statics')
# ep1.display()
# ep1.ch_ename('feeee')
# ep1.display()
# 2. CLASS METHOD
# it is used to access and modify the class members
# we need to use 'cls'as an argument to store the address of the class members and it is compulsory to use @classmethod
# Syntax 
# class Cname:
#    statment Block 
#    @classmethod    #they called as decrator
#    def Mname(cls,args):
#       SB
#    @classmethod
#    def Mname(cls,new):
#       cls.var=new 
# obj=Cname(val)
# Cname.Mname(val)

# class Method:
#    sname='ABC'
#    loc='paris'
#    principal='palak'
#    timing='8:00AM-4:00PM'
#    @classmethod
#    def display(cls):
#       print(cls.sname,cls.loc,cls.principal,cls.timing)
#    @classmethod
#    def ch_time(cls,new,change):
#       cls.timing=new
#       cls.loc=change
# st1=Method()
# Method.display()
# Method.ch_time("3:30PM-4:30PM", "London")
# Method.display()
# class Company:
#      Cname='hybe'
#      loc='korea'
#      CEO='shivangi'
#      @classmethod
#      def display(cls):
#       print(cls.Cname,cls.loc,cls.CEO)
#      @classmethod
#      def ch_Cname(cls,new,change):
#       cls.Cname=new
#       cls.loc=change
# st1=Company()
# Company.display()
# Company.ch_Cname("YG entirterment", "London")
# Company.display()
# class Bank:
#   Bname='ICIC'
#   loc='mars'
#   manager='akansha'
#   def display(self):
#     print(self.Bname,self.loc,self.manager)
#   def ch_Bname(self,new):
#     self.Bname=new
#   @classmethod
#   def display(cls):
#     print(cls.Bname,cls.loc,cls.manager)
#   @classmethod
#   def ch_Bname(cls,new,change):
#     cls.Bname=new
#     cls.loc=change
#     ep1= Bank('kiki',19,23,'B+')
# st1.display()
# st1.ch_age(30)
# st1.display()
    
    

# 3. static method
# it is neither belongs to class members nor belongs to object address. but it will act as asupportive method for both class and object
# --decorator--
# @staticmethod
# Syntax 
# class Cname:
#   SB
#   @staticmethod
#   defMname(args):
#    SB
#   obj=Cname()
class Memory:
  name='aaaaaachiiiiiiii'
  role='khikhi'
  @staticmethod
  def nonsense(a,b):
    print(a+b)
st1=Memory()
Memory.nonsense(10,20)
st1.nonsense(10,20)

class Demo():
   @staticmethod
   def add (a,b):
    print(a+b) 
Demo.add(23,52)

#     why is this static method
#     because,
# it dose not use object members
# it dose not use class members
# it works independently
# static method is a normal helper function inside a class
   
