def largest_element(nums):
    val = float('-inf')
    for i in nums:
        if i>val:
            val = i
    return val


nums = [3,2,1,7,6,54]
print(largest_element(nums))