# bitwise operator
# it will be only applicable for integer 

print(bin(7))
# bitwise and
print(bin(3&8))
print(bin(15&21))
print(int(0b101))
# bitwise or
print(bin(3 or 8))
#bitwiseXOR
print(bin(2^5))
#bitwise NOT
print(~(-13))
#bitwise right shift (vvi)
print((5<<2))
# /
#assingment
a=60
b=70
print((a+b))
# membership operator 
#it is used to check if value is the member of your collection or not
s={5,6,7,8,9,}
print(6 in s)
# in dictionary we can check for the key because key is visible layer
m=[4,6,7,[8,9]]
print(9 in m)
print(9 in m[-1])
print(9 not in m)
print(9 not in m[-1])
#identity operator
#it used to check weater the operands are sharing same memory address or not
# memory adress is same=true
# memory address is not same=false 
a=80
b=40
c=80
print((id(a))==(id(c)))
r=5
t=4
t=5
print(r is t)
print(id(r))
print(id(t))
# (==) for checking 
#output
a=5
b=6
a ,b=b,a
# sep = by default space space 
# end=\n by default net line
print(a,b,end='')
print(id(a),id(b))
c=5
g=6.9
v="hello"
# input formate
name ='kiki' 
print(f'my name is not {name}')
name =input ('enter your name: ')
print(type(name))
#if we write name it consider as string
#if we write number it consider as integer
age=23
print(f'my name is not {age}')
name =input ('enter your number: ')
print(type(age))
#
print(f'my list is ')
name =input ('enter your list: ')
print(type(list))
#if statment
money=int(input('enter a number😍'))
if money>=5000000000000000000:
    print("go to south korea")
else:
    print("go to north korea")