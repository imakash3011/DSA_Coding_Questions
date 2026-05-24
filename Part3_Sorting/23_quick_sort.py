def partition(nums, low , high):
    i = low
    j = high
    pivot = nums[low]

    while i<j:
        while nums[i]<=pivot and i<=high-1:
            i+=1
        while nums[j]>pivot and j>=low+1:
            j-=1
        if i<j:
            nums[i], nums[j] = nums[j], nums[i]
    nums[low], nums[j] = nums[j], nums[low]
    return j   ## this index is sorted that's why returning this.. similarily we will repeat for other indexes

def quick_sort_solution(nums, low, high):
    if low< high:
        pivot_sorted_idx = partition(nums, low, high)   ## by first run we will get first index where left will be smaller and right will be have larger element
        quick_sort_solution(nums, low, pivot_sorted_idx-1) ## running for quick sort for smaller side of pivot
        quick_sort_solution(nums, pivot_sorted_idx+1, high)  ## for larger side of the pivot
    return nums


nums = [4,1,7,6,3,2,8]
low = 0
high = len(nums)-1
print(quick_sort_solution(nums, low, high))