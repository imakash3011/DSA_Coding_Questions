def insertion_sort(nums):
    n = len(nums)
    for i in range(1, n):
        key_ele = i  ## Start with second element as key element
        j = i-1  ## Consider first one as already sorted
        while j>=0 and nums[j]>key_ele:
            nums[j+1] = nums[j]  ## Move bigger element to one right side
            j-=1  
        nums[j+1] = key_ele  ## at correct position put the key_ele
    return nums


nums = [7, 4, 1, 5, 3]
print(insertion_sort(nums))