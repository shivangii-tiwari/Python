a=10  #copy 
b=a
print(b) # genral copy
id(a)
id(b)
print(id(a))
print(id(b))
a=20
print(b)
print(a)
s=[20,9.6,5+7j]
l=s
print(id(s))
print(id(l))
print(l)
l[1]=66
print(l)
print(s)
s=[20,9.6,5+7j,[True,45]]   #shallow copy
# shallow copy changes in nested list too so we need deep copy.
l=s.copy()
print(l)
print(id(l))
print(id(s))
s[2]=5555
print(s)
print(l)
l[3][1]=False
print(l)
print(s)
n=[20,9.6,5+7j,[True,45]]
import copy
n=copy.deepcopy(l)
