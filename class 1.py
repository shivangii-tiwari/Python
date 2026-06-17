#python using interpreter
#python is dinamically
#WAP to find the reverse of a string without slicing
s = "python"
p = ""
for i in s:
    p = i + p

print(p)
#WAP to find sum of the digit of numbers
t = 2345
hehe = 0
while t>hehe:
    tae = t%10
    hehe +=tae
    t = t//10
    print(hehe)
#wAP to find the factoral of a number
t = 5
hehe = 1
while t>0:
    hehe *= t
    t -= 1
    print(hehe)
#WAP to find the largest even number in a list
ak = [1,2,3,4,5,6,7,8,9] 
kiko = 0
for i in ak:
   if i % 2 == 0:
       if i > kiko:
           kiko = i
print(kiko)


