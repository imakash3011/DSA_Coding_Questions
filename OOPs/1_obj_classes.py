### 1. Write a Python program to create a Vehicle class with max_speed and mileage instance attributes.
# class Vehicle:
#     def __init__(self, max_speed, mileage):
#         # print("This is speed and mileage test!")
#         self.max_speed = max_speed 
#         self.mileage  = mileage
# model1 = Vehicle(10, 40)

# print(model1.max_speed, model1.mileage)


### 2. Create a Vehicle class without any variables and methods
# class Vehicle:
#     pass

# class Vehicle:
#     def __init__(self):
#         print("Hello.. Good Morning!")
# Vehicle()


### 3: Create a child class Bus that will inherit all of the variables and methods of the Vehicle class
# class Vehicle:
#     def __init__(self, mileage, max_speed):
#         self.mileage = mileage
#         self.max_spped = max_speed
#     def mileage_check(self):
#         print("Mileage of my car is", self.mileage)
#     def max_speed_check(self):
#         print("Max speed of the car is", self.max_speed)

# class Bus(Vehicle):
#     # def __init__(self, seat):
#     #     self.seat = seat
#     def seat_capacity(self, seat):
#         print("This bus seat capacity is", seat)

# # model3 = Bus(40, 100)
# # model3.mileage_check()

# # If you want to run it without any argument in Bus() then declare mileage=0, max_speed=0 in Vehicle init method
# model4 = Bus(3,4)
# model4.seat_capacity(45)

# Learning: When you use self, you are essentially saying, "Store this piece of information inside this specific instance of the object so I can find it later."




## 4 Define a property that must have the same value for every class instance (object)

# class Vehicle:
#     color = "white"

#     def __init__(self, mileage, speed):
#         self.mileage = mileage
#         self.speed = speed
    
#     def mileage_check(self):
#         print("This is the mileage of my vehicle", self.mileage)
    
#     def speed_car(self):
#         print("Speed of my vehicle is", self.speed)

# class Bus(Vehicle):
#     def bus_capacity(self, seat):
#         print("Capacity of the bus is", seat)

# model5 = Bus(23, 45)
# print(model5.color)
# model5.bus_capacity(98)



#### Write a program to determine which class a given Bus object belongs to.

# class Vehicle:
#     color = "white"

#     def __init__(self, mileage, speed):
#         self.mileage = mileage
#         self.speed = speed
    
#     def mileage_check(self):
#         print("This is the mileage of my vehicle", self.mileage)
    
#     def speed_car(self):
#         print("Speed of my vehicle is", self.speed)

# class Bus(Vehicle):
#     def bus_capacity(self, seat):
#         print("Capacity of the bus is", seat)

# model5 = Bus(23, 45)
# print(model5.color)
# model5.bus_capacity(98)

# print(type(model5))  ## Determine which class a given Bus object belongs to.
# print(isinstance(model5, Vehicle))  ## Determine if School_bus is also an instance of the Vehicle class
# print(issubclass(Bus, Vehicle)) ## Check object is a subclass of a particular class


#### Calculate the area of different shapes using OOP
class Shape:
    def area(self):
        raise NotImplementedError("Area method must be implemented by subclass")

class triangle(Shape):
    def __init__(self,radius):
        self.radius = radius
    def area(self):  ## Overriding Area method
        return 3.14*self.radius**2
    
class sqaure(Shape):
    def __init__(self, side):
        self.side = side
    def area(self):
        return self.side*self.side

area1 = sqaure(3)
print(area1.area())   

area1 = triangle(3)
print(area1.area())    



class Employee:
    raise_amount = 1.04
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first+'.'+last+'@company.com'
    
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay * Employee.raise_amount) ## Class variable can't be accessed directly it need class reference as well
        # self.pay = int(self.pay * self.raise_amount) ## I think it will change for each instance separately (But class will change for all employee)
emp_1 = Employee('akash', 'patel', 40)

print(Employee.__dict__)
print(emp_1.__dict__)