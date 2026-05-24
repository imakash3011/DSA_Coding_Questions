def insertion_sort(nums):
    # Start from the second element (index 1)
    n = len(nums)
    for i in range(n):
        key_ele = nums[i]
        j = i-1
        print(j)
        # Move elements of arr[0..i-1] that are greater than key
        # to one position ahead of their current position
        while j>=0 and key_ele<nums[j]:
            nums[j+1] = nums[j]
            j -=1
        # Place the key in its correct position
        nums[j+1] = key_ele
    return nums

nums = [3,4,5,1,5,9,7,6]
print(insertion_sort(nums))