# def div(a,b):
#     print(a/b)

# print(2/4)

## Suppose there is a case where we want to keep always num> deno for division but 
## we are not allowed to change the previous function or we don't have access to it.


# def smart_div(func):
#     def inner(a,b):
#         if a<b:
#             a,b = b,a
#         return func(a,b)
#     return inner
# div1 = smart_div(div)
# div1(2,4)

############## EASY LEVEL ##################

# def my_deco(func):
#     def wrapper():
#         print("Before execution")
#         func()
#         print("After Execution")
#     return wrapper


# def say_hello():
#     print("Helo")

# s1 = my_deco(say_hello)
# s1()

## using @decorator
# def my_deco(func):
#     def wrapper():
#         print("Before execution")
#         func()
#         print("After Execution")
#     return wrapper

# @my_deco
# def say_hello():
#     print("Helo")

# say_hello()


# Decorator with arguments

# def my_decorator(func):
#     def wrapper(*args, **kwargs):
#         print("Before execution")
#         rresult = func(*args, **kwargs)
#         print(rresult)
#         print("After execution")
#     return wrapper

# @my_decorator
# def add(a, b):
#     return a+b

# add(3,5)


# ##########

def authorize(func):
    def wrapper(user):
        if user!="admin":
            print("Access Denied")
            return
        return func(user)
    return wrapper

@authorize
def delete_data(user):
    print("data deleted!")

# delete_data("admin")
delete_data("guest")
