# FITER #filter is used to check the condition and map is used to perfom operation on each element in list
# syntax 
# filter(function,collection)
a=[2,4,3,5,7,9,8]
y=filter(lambda x:x%2!=0,a)
print(list(y))
u=map(lambda x:x%2!=0,a)
print(list(u))
#filter number greater than 45
d=[100,45,35,65,66,20,19]
h=filter(lambda x:x<45,d)
print(list(h))
#filter the number which are nrgative
v=[1,2,-5,10,-11,-12]
f=filter(lambda x:x<0,v)
print(list(f))
#3 filter the name which are starting from 'a'
w=['aman','rahul','aditya','rahul','lokesh','ambani']
d=filter(lambda x:x.startswith('a'),w)
print(list(d))
r=['python','java','AIML','cyber']
#filter the string greater than 5
u=filter(lambda x:len(x)>5,r)
print(list(u))
r=[12,15,30,45,27,20]
#filter the number divisible by 5 and 3 both
t=filter(lambda x: x%5==0 and x%3==0,r)
print(list(t))
#ends with 'n'
o=['nun','fun','sum','tum','run']
y=filter(lambda x:x.endswith('n'),o)
print(list(y))
h=[30,16,17,13,60,56]
#filter the voting age
d=filter(lambda x:x>18,h)
print(list(d))
#filter the paindrome word from the list
r=['racecar','python','radar','madam']
p=filter(lambda x:x[::-1]==x[::1],r)
print(list(p))
# filter functon is a function which is use to get only the requrie data from the collection
# in this case this function which we are using shoud return either trur or false
# in filter function if condition is satisfied it hold the value or else remove the object from collection
a=256
b=256
print(id(a))
print(id(b))
# 0 to 256=address same 
# after 256=it changes
# comprehension
# the phenomenan of creating a new collection by using less number of instruction
# we can use only on mutable datatype
# TYPES 
# 1. list comprehension
# 2. set comprehension
# 3. dict comprehension
# list comprehension
# the phenomenan of create a new list by using less number of instruction
# SYN:
# var=[val of var in coll if condition]
# var=[True Statment Block if cond else FBS for var in coll]
# var=[vae1,var2 for var1 in coll of var2 in coll]
# WAP create list consist of 1 to 10
# j=[1,2,3,4,5,6,7,8,9,10]
# out=[]
# for i in range(1,11):
#     out.append(i)
# print(out) 
# out=[i for i in range(1,11)]
# print(out)
# #wap to store square if it is even and store cube if it is odd
# j=[1,2,3,4,5,6,7,8,9,10]
# out=[]
# for i in range(1,11):
#     if i%2==0:
#  list comprihension
y = [i for i in range(1,200)]
print(y) 
# syn 
# [i for var in coll/range]
# [i for var in coll/range if(condition) ]      
l=[i for i in range(1,200)if i%2==0]
print(l)
[val if condit else val for var in coll/range]

    
