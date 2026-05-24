# 1. Polymorphism — Core Idea
# 👉 “One interface, multiple behaviors”
# Polymorphism allows the same function/method name to behave differently depending on the object.

# 🔑 Types of Polymorphism in Python
# 1. Method Overriding (Runtime Polymorphism)
        # Same method in parent & child class
        # Child changes behavior
# 2. Operator Overloading
    # Same operator behaves differently
    # Example: + for numbers vs strings
# 3. Duck Typing
    # “If it walks like a duck, it’s a duck”
    # No inheritance required

# ⚙️ Must-Know Concepts
    # Same method name, different behavior
    # Inheritance-based overriding
    # Use of super()
    # Dynamic typing (duck typing)
    # Operator overloading (__add__, etc.)

# Method Overriding
class Animal:
    def speak(self):
        print("Animal Speak")
class Dog(Animal):
    def speak(self):
        print("Dog barks")
class Cat(Animal):
    def speak(self):
        print("Cat Meow")

# a1 = Dog()
# a1.speak()

# animals = [Dog(), Cat()]
# for a in animals:
#     a.speak()


# # Same Function Different Types (example)
# print(len("Hello"))
# print(len([1, 2, 3]))


# INTERMEDIATE LEVEL

class Animal:
    def speak(self):
        print("Speaking....")

class Dog(Animal):
    def speak(self):
        super().speak()
        print("Dog is barking")

# animal1 = Dog()
# animal1.speak()


# Question 4: Duck Typing

# Create:
    # Bird → fly()
    # Airplane → fly()
# 👉 No inheritance

class Aeroplane:
    def fly(self):
        print("Aeroplane is flying....")

class Bird:
    def fly(self):
        print("Bird is flying....")

def start_flying(obj):
    obj.fly()

start_flying(Aeroplane())
start_flying(Bird())

