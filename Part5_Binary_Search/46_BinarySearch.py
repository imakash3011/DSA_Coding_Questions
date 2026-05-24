
## Binary Search is applied only on sorted array or list

def binary_search(nums, target):
    first = 0
    last = len(nums)

    for i in range(len(nums)):
        if first > last:
            break
        mid = (first+last)//2
        if nums[mid]==target:
            return mid
        if target<nums[mid]:
            last = mid-1
        else:
            first = mid+1
    return "Not Found"


nums =  [11,14,23,34,56,67,78,89,100]
target = 78
print(binary_search(nums, target))