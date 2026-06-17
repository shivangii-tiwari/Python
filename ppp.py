# two types of contructor
# 1.parameterise 
# 2.non parameterise and  default constructor
# create a class called mobile
#     brand,price
#     create two diffrent objects display both object detals seperatly add a class member call catagory and catagory =electronics
# class mobile:
#     catagory=electronics
#     def __init__(self,brand,price):
#         self.brand=brand
#         self.price=price
#         def display_mobile_details(self):
#             print("\n----mobile details----")
#             print("catagory",mobile.catagory)
#             print("brand",self.brand)
#             print("price",self.price)
# pillars of oops 
# 1. inceritance
# 2. encapsulation
# 3. abstraction
# 4. polymorphism (ex=phone multitasker)
# class A:
#    def __init__(self):
#       print('hi')
#    def __init__(self):
#       print('hello')
# A()
class A:
   def display (self):
      print('hello')
   def display (self):
      print('bye-bye')
a=A()
a.display()
class A:
   def display (self):
      print('hello')
   def display (self,a):
      print('a')
a=A()
a.display(10)
# make a online shooping application
# create a class called shopping cart
# requirments (class members(platform name))
# constructor should initalze custmoer name,product list,total_amount
create object
object method(add product,remove method,update method,update platform name ,display the cart)

class shopping_cart:
   platform_name=hehe
   def __init__(self,Customer_name):
      self.customer_name=self.customer_name
      self.product_list=[]
      self.total_amount=0
   def add_product(self,product,price):
      self.product_list.append('product')
      self.total_amount += price
      print("add sucessfully")
      def remove_product(self,product,price):
         if product in product_list:
            self.product_list.remove(product)
            self.total_amount -= price
            print('removed successfully')
         else:
            print('product not found')
      def display_cart(self):
         print('shopping_cart:',shopping_cart.platform)
         print('customer_name:',self.customer_name)
         print('product_list:',self.product_list)
         print('total_amount:',self.total_amount)
         @classmethod
         def update_platform_name(cls,new_name):
            cls.platform_name=new_name
            print('platform name updated')
         @staticmethod
         def shopping_rules():
            print()


s1=shopping_cart("honey")
s
         
      

      self.product_list.remove(product)
    

      pass
   
   


    