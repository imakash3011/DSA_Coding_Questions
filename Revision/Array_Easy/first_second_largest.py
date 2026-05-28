def first_second_largest(nums):
    first, second = float('-inf'), float('-inf')
    for  i in nums:
        if i>first:
            second = first
            first = i
        elif i>second and i<first:
            second = i

    return first,  second

nums = [6,5,4,8,9,2,1,3]
print(first_second_largest(nums))