# class P1:
#     def show(self):
#         print('hello from A')
# class P2:
#     def display(self):
#         print('hello from B')
# class C(P1,P2):
#     pass
# obj = C()
# obj.show()
# obj.display()
class Vechile:
    vechile_name='ferrari'
    vechile_number='990099'
    fule_type='petrol'
class Car(Vechile):
    def J(self):
        print(self.vechile_name,self.vechile_number,self.fule_type)
class Bike(Vechile):
    def K(self):
        self.cc='18000'
        self.vechile_name='royal enfeild'
        print(self.vechile_name,self.vechile_number,self.cc)
obj = Car()
obj2 = Bike()
obj.J()
obj2.K()
