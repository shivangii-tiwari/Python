# for i in[1,2,3]:
#     print(i)
# ITRATOR 
# it is the process of traversing to sequence getting and the value one by one
# the functon is used to perform Iteration
# for loop competly depend on itrator so that it has inbuild itrator
# to perfom itrator it consist of two method
# 1.iter 
# 2.next
# itrables=>list,tuple,dict,set
# itrate=traverse
# a=[1,2,30,40]
# it=iter(a)
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))#you can not traverse backward
# print((it))
# ok so we mostly use for loop because it is easy and have less no of code but it you are having larg number of data we use itrator acess data one by one(it all based on memory allocation)
# it is a function which is used to make the control to get pointed to the initial mode address
# syn 
# var_name=iter(itrable)
# next()(next function)
# it is a function which is use to get the values one by one, once you accessed all the object inside thge itrables that time it will thow stop itration error
# syn 
# next(itrator)
# class count:
    # def __init__(self,start, stop):
    #     self.start=start
    #     self.stop=stop 
    # def __iter__(self):#iter ka dunder method
    #     return self
    # def __next__(self):#next ka dunder method
    #     if self.start>=self.stop:
    #         raise StopIteration
    #     value=self.start
    #     self.start+
    
class countup:
    def __init__(self,start, stop):
            self.start=start
            self.stop=stop 
    def __iter__(self):#iter ka dunder method
            return self
    def __next__(self):#next ka dunder method
            if self.start>=self.stop:
                raise StopIteration
            value=self.start
            self.start+=1
            
            return value
counter=countup(1,5)
print(next(counter))
print(next(counter))
print(next(counter))
print(next(counter))
for i in counter:
     print(i) #(somthing like this)