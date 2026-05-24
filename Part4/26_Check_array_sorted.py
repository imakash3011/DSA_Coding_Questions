def check_array(nums):
    n = len(nums)-1
    for i in range(n):
        if nums[i]<=nums[i+1]:
            continue
        else:
            return False
    return True 

nums = [1,2,3,4,5,7,8,9,10]
print(check_array(nums))