def fibo_recur(n, first, second):
    if n==0 or n==1:
        return 
    print(first)
    return fibo_recur(n-1, second, first+second)

n = 5
first = 0
second = 1
fibo_recur(n+1, first, second)
