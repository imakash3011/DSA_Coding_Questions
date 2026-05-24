def bubble_sort(nums):
    len_nums = len(nums)
    for i in range(len_nums):
        for j in range(i+1, len_nums):
            if nums[i]>nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
    return nums


nums = [5,8,1,6,9,2,4]
print(bubble_sort(nums))