def bubble_sort(nums):
    n = len(nums)
    for i in range(n):
        for j in range(i+1, n):
            if nums[i]>nums[j]:
                nums[i], nums[j] = nums[j], nums[i] 
    return nums



nums = [7, 4, 1, 5, 3]
print(bubble_sort(nums))