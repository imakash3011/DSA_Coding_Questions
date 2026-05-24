
def selection_sort(nums):
    n = len(nums)
    for i in range(n):
        min_idx = i
        for j in range(i+1,n):
            if nums[j]<nums[min_idx]:  ## Here J will always compared by min_idx as we keep moving in a loop
                min_idx = j
        nums[min_idx], nums[i] = nums[i], nums[min_idx]

    return nums

nums = [7, 4, 1, 5, 3]
print(selection_sort(nums))