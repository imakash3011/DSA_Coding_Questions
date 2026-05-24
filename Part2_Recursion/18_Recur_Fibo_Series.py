def fibo_series(n,first, second):
    if n==0:
        return 
    print(first, end=" ")
    fibo_series(n-1, second, first+ second)


first =0
second = 1
n = 8
fibo_series(n,first, second)

