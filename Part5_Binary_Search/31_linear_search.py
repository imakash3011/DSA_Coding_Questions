
def linear_search(nums,k):
    n = len(nums)

    for i in range(n):
        if nums[i]==k:
            return i


nums = [5,6,4,3,2,7,8,9,10]
k =9
print(linear_search(nums, k))