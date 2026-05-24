def factorial(num):
    if num<0:
        return
    for i in range(1,(num//2)+1):
        if num%i==0:
            print(i, end=" ")

num = 16
factorial(num)