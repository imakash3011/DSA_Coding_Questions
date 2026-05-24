## Hashing -> Prefilling the element 

# Constraints
# n = 1<=n[i]<=10
# n can can 10^8 elements
# m can can 10^8 elements


def hashing_and_freq(n,m):
    len_n = len(n)+1
    len_m = len(m)
    hash_list = [0] * len_n 
    # print(hash_list)
    for num in n:
        hash_list[num] += 1    ## we are treating index as number for this problem
    # print(hash_list)
    result = [0]*len_m
    print(hash_list[10])
    for i in range(len_m):
        curr_m = m[i]
        if curr_m<11 :
            result[i] = hash_list[m[i]]
        else:
            result[i] = 0
    print(result)

n = [5,3,2,2,1,5,5,7,5,10]
m = [10,111,1,9,5,67,2]
hashing_and_freq(n,m)
