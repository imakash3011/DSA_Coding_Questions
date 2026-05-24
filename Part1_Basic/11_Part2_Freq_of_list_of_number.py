
def find_freq(n,m):
    dct = {}
    for i in n:
        dct[i] = dct.get(i,0)+1
    print(dct)

    for j in m:
        if j in dct.keys():
            print(j, dct.get(j))
        else:
            print(j, 0)

n = [5,3,2,2,1,5,5,7,5,10]   ## Note all the number 
m = [10,111,1,9,5,67,2]
find_freq(n,m)
