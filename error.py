# a=int(input('enter the value: '))
# b=int(input('enter the value: '))
# print(a/b)
# exception handling
# syn
# try:
#     SB
# except:
#     SB 

# try:
#     a=int(input('enter the value: '))
#     b=int(input('enter the value: '))
#     print(a/b)
# except ZeroDivisionError:        # we can create multiple except block but only one try block
#     print('error hai bhai') 
# except ValueError:
#     print('fefe')
# exception handling 
# 1.specific exception handling #when we know the error we are going to face is known as specific exception handling 
# 2.genric  exception handling  #when we don't know the type of error we are going to have
# 3.default  exception handling 
#     1.custom  exception handling 
#     2.user-define  exception handling 
# specific exception handling
# example:
# try:
#     a=int(input('enter the value: '))
#     b=int(input('enter the value: '))
#     print(a/b)
# except ZeroDivisionError:        
#     print('error hai bhai')
# except ValueError:
#     print('fefe')
# a={1:2,5:6}
# print(a[9])
#zero division error, value error and keydivisionerror
# try:
#     a=int(input('enter the value: '))
#     b=int(input('enter the value: '))
#     print(a/b)
#     c={2:5,8:9}
#     print(c[10])
# except ZeroDivisionError:        
#     print('error hai bhai')
# except ValueError:
#     print('fefe')
# except KeyError:
#     print('phewwwww')
# genric  exception handling 
# example:
# try:
#     a=int(input('enter the value: '))
#     b=int(input('enter the value: '))
#     print(a/b)
# except Exception:        
#     print('hehehehe')
# SYN:
# try:
#     SB #you cannot handle all the error in exception block thats why we use specific one
# except Exception:
#     SB
# default  exception handling # it will handle keybordintrrupt and hardintrruption error
# while True:
#     print('hii')
a=int(input('enter:')) 
print(a)
# syn 
# try:
#     SB
# except:
#     SB
try:
      while True:
            print('hii')
except:
      print('errrorrrrrrrrrrrrr')#if we press ctrl +c then keyboardintrruption error occur and it will print this
# custom exception handling
Syn :
raise <exception>('message')
user define exception handling:
syn:
class Error_name(exception):
      pass
raise Error_name("message")

class AgeError(Exception):
    pass
try:
        age=int(input("enter the age: "))
        if age<18:
              raise AgeError('not eligible')
        else:
              print('Eligible')
except AgeError as E:
        print(E)
        
 #finally syntax        
try:
      SB
except:
      SB
finally:
      SB      #aur kuch except ho ya na ho finally last mai always except hoga 

try:
      a=int(input("enter a value:"))
      b=int(input("enter another value:"))
      print(a/b)
except ZeroDivisionError:
      print("error hai bhai")
finally:
      print("code is sucessful")
