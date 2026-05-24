
def find_freq_string(n,m):
    dct = {}
    for i in n:
        dct[i] = dct.get(i,0)+1

    for j in m:
        if j in dct.keys():
            print(j, dct.get(j))
        else:
            print(j, 0)
    # print(dct)

n = "azyxyyzaaaa"
m = ["d", "a", "y", "x"]
find_freq_string(n,m)
