def freq(num):
    dict1 = {}
    for i in num:
        dict1[i] = dict1.get(i,0)+1
    print(dict1)

num = [12,43,65,7,8,9,9,9,9,12,12,43]
freq(num)