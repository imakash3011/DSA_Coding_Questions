## Increasing order

def recur(n):
    if n==0 :
        return
    recur(n-1)
    print(n) 

# recur(5)


## Decreasing order

def recur(n):
    if n==0 :
        return
    print(n)
    recur(n-1)
recur(5)
