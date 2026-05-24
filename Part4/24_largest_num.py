
def largest(nums):
    n = len(nums)
    largest_ele = nums[0]
    for i in range(n):
        largest_ele = max(nums[i], largest_ele)
    return largest_ele


nums = [55, 32, -97, 99, 3, 67]
print(largest(nums))



# # Defining Positive Infinity
# pos_inf = float('inf')

# # Defining Negative Infinity
# neg_inf = float('-inf')