# Rotate an array by 1 place

def rotate_array(nums,k):
    return nums[-k:] +nums[:-k]

nums = [1,2,3,4,5,6,7,8,9]
k = 1
print(rotate_array(nums,k))