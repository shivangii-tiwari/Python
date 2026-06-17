#oops
#to handle real life entities
#code reusablity
#reduce code redundency
#it provide the structure
#class = bruprint,prototype product  then actual product(object)
#class-> blueprint of object
# object -> copy of class
# class:
#     proprties        (variables)
#     fuctionality     (functions)

# class creation :
#     Syntax : class classname:         it should be starting from capital letter but its not mandatory.
                    # PROPERTIES          tab space is mandatory
                    # functonality
# object creation:
# objname = classname()    we can create n number of object by using one class
# class smartphone:
#     ram = 8
#     rom = 256
#     color = 'lavender'
        
# s1 = smartphone()
# s2 = smartphone()

# print(type(s1))
# print(smartphone.ram, smartphone.color, smartphone.rom)
# print(s1.ram, s1.rom, s1.color)
# print(s2.ram, s2.rom, s2.color)  if we do changes on a particular object then it will not modify the class or other objects.
# smartphone.color = "white"
# print(smartphone.ram, smartphone.color, smartphone.rom)
# print(s1.ram, s1.rom, s1.color)
# print(s2.ram, s2.rom, s2.color)
# s1.color = "pink"
# print(smartphone.ram, smartphone.color, smartphone.rom)
# print(s1.ram, s1.rom, s1.color)
# print(s2.ram, s2.rom, s2.color)  if we do changes on smartphone on class it will modify all the objects.
# To access the properties:-
# classname.propertyname
# objname .propertyname

# TO modify the properties:-
# classname.propertyname = Value
# objname .propertyname = value

# memory allocation#when we use function inside the class so it is called method
# take notes
class Bank:
    bankname="sbI"
    IFSC = 'sbI000123'
    country = 'india'
    def details(obj,name,age,phone,pan,balance):# the problem in way to is taken after creating your account
        obj.name = name
        obj.age = age # self 
        obj.phone = phone
        obj.pan = pan
        obj.balance = balance
    c1 = bank()



    #way3
class bank:
#types of method
# 1. object\instance method
# 2. class method
# 3. static method
# 4. abstract method
class Bank:
    #static properties
    bname = "SBI"
    branch = 'hyd'
    def_init_(self,name,age,balance):
    self.name= Name
    self.age = age
    self.bal = balance
# object method
def display(self):
    print(self.name,self.age,self.bal)
# object method
def change_age(self,new_age):
    self.age = new_age
#object method
def deposite(self,amnt):
    if is_valid(amnt):  

# class method
@classmethod
def change_bdetails(cls,new_branch):
    cls.branch = branch
# class method
@classmethod
def bank_details(cls):
    print(cls.bname,cls.branch)



def is_ valid(amnt):
    if amnt






