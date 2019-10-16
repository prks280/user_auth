# from abc import ABC, abstractmethod
#
#
# class LivingThing(ABC):
#
#     @abstractmethod
#     def humans(self): pass
#
#     @abstractmethod
#     def animals(self): pass
#
#
# class Work(LivingThing):
#     def humans(self):
#         print('we can think and invent')
#
#     def animals(self):
#         print('we can save nature')
#
#
# obj = Work()
# obj.humans()
#
# class A():
#     def m1(self):
#         print('A.m1')
#
#
# class B(A):
#     def m1(self):
#         print('B.m2')
#
#
# class C(B,A):
#     def m1(self):
#         print('C.m3')
#
# c = C()
# c.m1()
# super(Honda_Cars, self).__init__()
#
#
# class Car():
#     def __init__(self, name, company, model, year):
#         self.name = name
#         self.company = company
#         self.model = model
#         self.year = year
#
#     def test(self):
#         print('car is {} years old'.format(2019 - self.year))
#
#
# class Honda_Cars(Car):
#
#     def __init__(self, types, name, company, model, year):
#         super().__init__(name, company, model, year)
#         self.type = types
#
#     def car_age(self):
#         super().test()
#
#
# h1 = Honda_Cars('petrol', 'r1 500', 'Honda', 'r15', 2017)
# h1.car_age()
# print(h1.__dict__)
#
#
# class A:
#     def __init__(self):
#         print('instance method called')
#
#     def test_method(self):
#         print('method of class A')
#
#
# class B(A):
#
#     variable_test = 'test'
#
#     def test_method(self):
#         print('method of class B')
#
#     @staticmethod
#     def test2():
#         print('method of class B')
#
#
# class C(B):
#     def test_method(self):
#         super().__init__()              # call constructor
#
#         A.test_method(self)             # ways to call parent method method
#         super().test2()
#         super(B, self).test_method()    # to call method of class A, we use super of class B
#
#         print(super().variable_test)    # access static variable
#         print(self.variable_test)       # access instance variable
#
#
# obj = C()
# obj.test_method()
#
# multiple except block
# try:
#     print(10/0)
# except FileExistsError as a:
#     print(a)
# except ZeroDivisionError as b:
#     print(b)
#
# multiple except block
# def fun(x, y):
#     try:
#         print(x / y)
#     except (ZeroDivisionError, TypeError, NameError) as e:
#         print(e)
#
#
# fun(2, 0)
#
# import os
#
# try:
#     print(1)
#     print(12)
#     os._exit(0)
#     print(13)
# except:
#     print(2)
#
# finally:
#     print(3)
#
# from abc import ABC, abstractmethod
#
#
# class LivingThing(ABC):
#
#     @abstractmethod
#     def humans(self): pass
#
#     @abstractmethod
#     def animals(self): pass
#
#
# class Work(LivingThing):
#     def humans(self):
#         print('we can think and invent')
#
#     def animals(self):
#         print('we can save nature')
#
#
# obj = Work()
# obj.humans()
#
#
# class ClassA():
#     def __fun(self):
#         print('class A function')
#
#
# class Class_B(Class_A):
#     def fun(self):
#         print('overriding class A function')
#
#
# a = ClassA()
# print(a._ClassA__fun())
#
#
# class SeeMee:
#     def youcanseeme(self):
#         return 'you can see me'
#
#     def __youcannotseeme(self):
#         return 'you cannot see me'
#
#
# # Outside class
# Check = SeeMee()
# print(Check.youcanseeme())
# print(Check._SeeMee__youcannotseeme())
#
#
#
#
# class A:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
#
# class B(A):
#     def __init__(self, name, age, salary):
#         super().__init__(name, age)
#         self.salary = salary
