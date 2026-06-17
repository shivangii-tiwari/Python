#WAP to find sum of all integers in a list
# y = [80,90,70,'hello',3+6j]
# sum = 0
# for i in y:
#     if type(i) == int:
#         sum = sum+i
# print(sum)
#WAP sum until user enter 0 using while loop and the program print total sum
# u = int(input("enter the integers: "))
# sum= 0
# while u!=0:
#     sum = sum +u
#     u = int(input("enter the integers: "))
# print("total sum:",sum)
#search palindrome number,eval
#WAP To find the 2nd largest from a given list
# e = [23,34,56,78] # check for sorted and unsorted
# largest=0
# second_largest=0
# for i in y:
#     if i>largest:
#         second_largest=largest
#         largest=i
#     elif i>second_largest and largest!=largest:
#         second_largest=i
# print("second_largest:" ,second_largest)
# WAP to check weather the number is prime or not
# u = int(input("enter the number: "))
# is_prime=False
# if u<=1:
#     is_prime=False
# else:
#     for i in range(2,u):#u//2+1 use it and tell why
#         if u % i==0:
#             is_prime=False
# if is_prime:
#     print("prime number")
# else:
#     print("not prime")# check the error
#WAP remove dublicate from list without using inbuilt function
# l = [3,4,4,5,6,7,3]
# #f = [3,4,5,6,7]
# e = []
# for i in l:
#     if i not in e:
#         e.append(i)
# print(e)
# WAP to get following output
y = (12,3.4,'hello',2+3j,'python','bye',False)
#o = ('hello':5,'python':6,'bye':3)
out={}
for i in y:
    if type(i)==str:
        out[i]=len(i)
print(out)
# WAP for
# i = 'abcabacbcbc'
# o = 'a3b4c4'  #solve this by yourself
#WAP for
y = 'abcabacbcbc'
#o = {a:3,b:4,c:4}
o = {}
for i in y:
    if i not in o:

    
        o[i]=len(i)  
print(o)
#WAP to check weather a number is perfect or not#perfect number
y = 6
sum = 0
for i in range(1,y):
    if y%i==0:
        sum = sum +0
if sum==y:
    print("perfect",y)
else:
    print("not perfect,y")#find error
