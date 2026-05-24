def second_largest(nums):
    first = float('-inf')
    second = float('-inf')

    for i in nums:
        if i>first:
            # Update both: the old first becomes the second
            second = first
            first = i
        elif i>second and i!=first:
            # Update only second if i is between first and second
            second = i
    print(first, second)


nums = [2,3,55,666,77,66,88,99,888,333,246]
second_largest(nums) 