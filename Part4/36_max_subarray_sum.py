
def max_subarray_sum(nums):
    max_sum = 0
    n = len(nums)
    temp = 0
    for i in range(n):
        if nums[i]>0:
            temp+= nums[i]
        else:
            if temp>max_sum:
                max_sum = temp
                temp =0
    return max_sum

nums = [-2, 1, -3, 4, -1, 2, 1, 6, -5, 4]   ## If you seen negative then make temp=0
print(max_subarray_sum(nums))