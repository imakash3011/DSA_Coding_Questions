############# 1. Exercise  ##############


# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
   
# p1 = Person("akash", 10)
# p2 = Person("divanshu", 20)
# print(p1.name, p2.name)


############# 2. Exercise  ##############

# class Person:
#     def __init__(self, name):
#         self.name = name

#     def greet(self):
#         print("Hello, my name is", self.name)

# p3 = Person("Akash")
# p3.greet()

############# 3. Exercise  ##############

# class Car:
#     def __init__(self, color = "white"):
#         self.color = color
    
# c1 = Car()
# print(c1.color)

# c2 = Car("black")
# print(c2.color)


# INTERMEDIATE LEVEL
# ✅ Q4: Class variable vs instance variable

# class Employee:
#     company = "tata"

#     def __init__(self, name):
#         self.name = name

# emp1 = Employee("Akash")
# print(emp1.name)


##Encapsulation (private variable)

# class BankAccount:

#     def __init__(self):
#         self.__balance = 0
    
#     def deposit(self, amount):
#         self.__balance += amount
    
#     def check_balance(self):
#         print("Your balance is ", self.__balance)


# emp1 = BankAccount()
# emp1.check_balance()
# emp1.deposit(100)
# emp1.check_balance()


# Class method
# Create a class Student with a class method that changes school name.

class Student:
    school = "njms"

    # def school_name(self,name):
    #     self.name = name

    @classmethod
    def change_school(cls, new_name):
        cls.school = new_name

# Student.change_school("oxford public school")
# print(Student.school)

# Q7: Static method
class Check:

    @staticmethod  ## it will not take 'self' and 'cls'
    def even_check(number):
        if number%2==0:
            return "even"
        else:
            return "odd"
# c1= Check()
# print(c1.even_check(11))


# 🔴 ADVANCED LEVEL
# ✅ Q8: Inheritance

class  Animal:
    def speak(self):
        print("Animal speak")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

# ani1 = Dog()
# ani1.bark()
# ani1.speak()

# ✅ Q9: Method overriding
# Override parent method in child class.


class Animal:
    def speak(self):
        print("Hello bhaw bhaw")
    
class Dog(Animal):
    def speak(self):
        print("Hello Meow Meow")


# a1 = Animal()
# a1.speak()

# d1 = Dog()
# d1.speak()


# Q10: Multiple inheritance
# Create class Father, Mother, and child Child.

class Father:
    def skills(self):
        print("Gradening")
    
class Mother:
    def skills(self):
        print("Cooking")

class Children(Father, Mother):
    pass

# t1 = Children()
# t1.skills()



class Book:
    def __init__(self, title):
        self.title = title

    def __str__(self):
        return f"Book: {self.title}"

# b = Book("Python")
# print(b)


# Q12: Build a mini project (REAL understanding 🚀)

# Create a Library system:

# Add books
# Show books
# Borrow book

class Library:
    # all_book = [] (Will be same for all instance)
    def __init__(self):  ## If you will list here then it will be separate for all instances (recommended)
        self.all_book = []
    
    def add_book(self, book_name):
        self.all_book.append(book_name)
    
    def show_book(self):
        for i in self.all_book:
            print(i, end="\n")
    def borrow_book(self, book_name):
        self.all_book.remove(book_name)

# lib1 = Library()
# lib1.add_book("Java book")
# lib1.add_book("Python book")
# lib1.add_book("C book")
# lib1.show_book()
# print("________________")
# lib1.borrow_book("Python book")
# lib1.show_book()
# print("**************")
# lib2 = Library()
# lib2.show_book()


# Shopping Cart System
# Create a shopping cart system where:
# You can add items
# Remove items
# View total price
# Show cart items

class Shopping:

    def __init__(self):
        self.cart = {}
    def add_items(self, item, price):
        self.cart[item] = price

    def total_price(self):
        total = 0
        for i,j in self.cart.items():
            total+=j
        return total
    def view_cart(self):
        for i, j in self.cart.items():
            print(i)

shop1 = Shopping()
shop1.add_items("apple", 70)
shop1.add_items("orange", 20)
shop1.add_items("grapes", 34)
# print(shop1.total_price)

shop1.view_cart()
print(shop1.total_price())
