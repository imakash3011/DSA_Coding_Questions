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
        # self.pay = int(self.pay * self.raise_amount)

    @classmethod  # instead of "self" we will use "cls"
    def set_raise_amt(cls, amount):
        cls.raise_amt = amount


emp_1 = Employee('akash', 'patel', 40)
emp_2 = Employee('divanshu', 'yadav', 60)

Employee.set_raise_amt(1.05)  ## will get reflected for all instance of class

print(Employee.raise_amt)
print(emp_1.raise_amt)
print(emp_2.raise_amt)

# print(Employee.__dict__)
# print(emp_1.__dict__)