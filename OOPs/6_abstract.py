# Abstract Class = Blueprint class that forces child classes to implement certain methods
# You cannot create objects of an abstract class.

# How to Create Abstract Class in Python
# We use:
            # abc module
            # ABC
            # @abstractmethod

from abc import ABC, abstractmethod

class Animal(ABC): # <--- Must inherit from ABC
    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    # If we don't implement sound(), code will CRASH
    def sound(self):
        print("Barking")

    def legs(self):
        print("Dog have four legs")

ani1 = Dog()
ani1.legs()
ani1.sound()

# Key Rules for Abstract Classes
# Enforcement: A subclass is considered abstract until all abstract methods are overridden.
# No Instantiation: You cannot create an object of the Animal class (e.g., a = Animal() will fail).
# Contract: It acts as a "contract." It guarantees that any Animal object in your system will definitely have a .sound() method.