def move_zero(lst):
    pos = 0
    n = len(lst)
    cnt= 0
    for i in range(n):
        if lst[i]!=0:
            lst[pos] = lst[i]
            pos +=1
        else:
            cnt +=1
    # print(lst, cnt)

    for i in range(pos, pos+cnt):
        lst[i] =0
    print(lst)


lst = [3,0,8,7,0,8,0,9,0,2,0,1]   ## keep sliding the value towards left side
move_zero(lst)