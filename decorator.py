# decorator:adding the extra functionality to the main function
# syn:
# def <decorater_name>(function):
# def wrapper(*arg,**kwarg):
#     pre task
#     function(*arg,**kwarg):
#     post task
# return wrapper
# @<decorater_name>
# print("hii")
# main()

def my_decorator (func):
    def wrapper():
        print("this is start of decorator")
        func()
        print('this is end of decorator')
    return wrapper
@my_decorator
def greet():
    print('good morning')
greet()

def shivangi (func):
    def wrapper():
        print("this is start of life")
        func()
        print('this is end of war')
    return wrapper
@shivangi
def greet():
    print('waawoooo')
greet()

def shivangi (func):
    def wrapper():
        print("this is start of life") #two ways of calling decorator
        func()
        print('this is end of war')
    return wrapper
#@shivangi
def greet():
    print('good morning')
#greet()
e=shivangi(greet)
e()

# two types of my_decorator
# 1.buit-in (@classmethod,@abstractmethod,@login)
# 2.user-define