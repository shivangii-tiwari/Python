# Looping statements
# Two types of loops in python are :- 
# While 
# For 



# While Loop:-
# syntax :- 
# initialization :- Starting point
# while condition(Statement block and updation) :- Breaking point

# Example:-

# i = 1
# while i<=10:
#     print(i)
#     i += 1 #also we can write i = i + 1


# i = 10
# while i > 0:
#     print(i)
#     i -= 1


# i = 2
# while i < 51:
#     print(i)
#     i = i + 2


# i = 1
# while i < 51:
#     if i % 2 == 0:
#        print(i)
#     i = i + 1


# i = 5 
# c = 1
# while i > 0:
#     c = c * i
#     i = i - 1
# print(c)
    
n=int(input("enter the number: "))
rev=0
while n!=0:
    e=n%10
    rev=rev*10+e
    
