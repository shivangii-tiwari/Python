# WAP to calcuclate a student's grades based on their score
# take a score(0-100)as input
# check input is invalid(less than 0 or greater than 100)
# above 90
# 80 to 89
# 70 to 79
# 60 to 69 
# below 60
# t = int(input("enter the score: "))
# if t>=90 and t<=100:
#     print("grade A")
# elif t>=80 and t<=89:
#     print("grade B")
# elif t>=70 and t<=79:
#     print("grade C")
# elif t>=60 and t<=69:
#     print("grade D")
# elif t<60 and t>10:
#     print("grade E")
# elif t<0 and t>100:
#     print("invalid") #modify little bit
#  take two cordinate x and y and check in which point the data points are present
# y = int(input("enter the x coordinate: "))
# x = int(input("enter the y coordinate: "))
# if x > 0 and y>0:
#     print("first quard")
# elif x<0 and y>0:
#     print("second quard")
# elif x<0 and y<0:
#     print("third quard")
# else:
#     print("fourth quard")
 #   wAP to c heck the given character is uppercase,lowercase,digit,specialcharacter
# p = (input("enter the character: "))
# if 'A'<=p<='Z':
#     print("upper case")
# elif 'a'<=p<='z':
#     print("lower case")
# elif '0'<=p<='9':
#     print("digit")
# else:
#     print("special char")
# WAP y = ['pro.html','google.com','pro1.txt']
# o/p = ['html':'pro','com':'google','txt':'pro1']
# y = ['pro.html','google.com','pro1.txt']
# h ={}
# for i in y:
#     name,key=i.split('.')
#     h[key]=name
# print(h)
#packing and unpacking
#AP to find the string value from tuple using packing
# def str(*a):
#     for i in a:
#         if type(i)==str:
#             print(i)
# str("hell","well","shell",56,3+4j)
# #WAP to print all the values from a tuple using packing
# def tup(*j):
#     for i in j:
#         print(i)
# tup("hell","well","shell",56,3+4j)
# def pack(**b):
#     print(type(b))
#     print(b)
# pack(a=1,b=2,c=3)
# WAPto print all the keys from a dict using packing
# def tae(**k):
#     for i in k.values():
#         print(i)
# tae(a=1,b=3,c=4)

# def tae(**k):
#     for i in k():
#         print(i)
# tae(a=1,b=3,c=4)
# def wee(*a,**b):
#     print(type(a))
#     print(a)
#     print(type(b))
#     print(b)
# wee(a=3,c=4,f=8)
# wee(10,50,r=5,i=9)
# wee(10,50,89)
def unpack(v1,v2,v3,v4):
    print(v1,v2,v3,v4)
unpack(*'abcd')
unpack(*range(1,5))

