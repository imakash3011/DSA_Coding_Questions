def three_num_sum(arr):
    n = len(arr)

    result = []
    for i in range(n):
        for j in range(i+1,n):
            for k in range(j+1, n):
                if arr[i]+arr[j]+arr[k] == 0:
                    temp = []
                    temp.append(arr[i])
                    temp.append(arr[j])
                    temp.append(arr[k])
            if len(temp)!=0:
                result.append(temp)
            temp = []
    return result

arr = [-1, 0, 1, 2, -1, -4]
print(three_num_sum(arr))

##### SOLVE THE OPTIMIZE ONE #######

