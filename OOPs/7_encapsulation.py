# Encapsulation
# Bundling data (variables) + methods (functions)
# Restricting direct access using access modifiers


# Why it matters:
    # Protect data (data hiding)
    # Control access (validation)
    # Cleaner & maintainable code

# | Type      | Syntax   | Meaning                         |
# | --------- | -------- | ------------------------------- |
# | Public    | `name`   | Accessible everywhere           |
# | Protected | `_name`  | "Internal use" (convention)     |
# | Private   | `__name` | Name mangled (harder to access) |

# ⚙️ Key Concepts You MUST Know
    # Getter & Setter methods
    # Private variables (__var)
    # Property decorator (@property)
    # Data validation inside class
    # Controlled updates

# How Name Mangling Actually Works
# When you use double underscores (e.g., __marks), Python doesn't actually make the variable "invisible." Instead, it textually transforms the name to prevent accidental overrides in subclasses.


# Basic Encapsulation

class Students:
    def __init__(self):
        self.__marks = 0
    
    def set_marks(self, mark):
        self.__marks = mark
    
    def get_marks(self):
        print("Your mark is ", self.__marks)

# s1 = Students()
# s1.set_marks(92)
# s1.get_marks()


# Private Variable Access (python does name mangling)

# print(s1.__marks) # You will get error
# print(s1._Students__marks)  # you will have to use class name with single underscore to update


# INTERMEDIATE LEVEL

class BankAccount:
    def __init__(self):
        self.__balance = 0
        self.amount = 0
    def deposit(self, amount):
        self.__balance +=amount
    def withdraw(self, amount):
        self.__balance -= amount
    def get_balance(self):
        return self.__balance
# b1 = BankAccount()
# b1.deposit(1000)
# print(b1.get_balance())

# b1.withdraw(10)
# print(b1.get_balance())


# ADVANCED LEVEL

class Employee:
    def __init__(self):
        self.__salary = 0
    
    def update_salary(self, amount):
        self.__salary += amount
    def get_salary(self):
        return self.__salary

# e1 = Employee()
# e1.update_salary(99)
# print(e1.get_salary())


# Project: E-Commerce Product
class Product:
    def __init__(self):
        self.__price = 0
        self.__product = {}

    def set_price(self, prod, price):
        self.__price = price # Update the private price variable
        self.__product[prod] = price  # Store it in the dictionary
    
    def get_product(self):
        for i, j in self.__product.items():
            print(i, j)

p1 = Product()
p1.set_price("apple", 10)
p1.set_price("mango", 30)
p1.set_price("banana", 20)
p1.get_product()
    
