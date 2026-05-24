def max_consecutive_one(nums):
    max_len = 0
    n = len(nums)
    temp = 0
    for i in range(n):
        if nums[i]==1:
            temp+=1
            # Update max_len if current streak is higher
            if temp>max_len:
                max_len = temp
        else:
            # We hit a 0, so the streak is over. Reset temp.
            temp = 0
    return max_len

nums = [1,1,0,1,0,1,1,1,1, 0,1,1]
print(max_consecutive_one(nums))