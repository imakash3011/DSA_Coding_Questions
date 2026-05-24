def search_rot_array(nums, target):
    low = 0
    high =len(nums)-1

    while low<=high:
        mid = (low+high)//2
        if nums[mid]==target:
            return mid
        
        if nums[low]<= nums[mid]:
            if nums[low]<=target < nums[mid]:
                high = mid-1
            else:
                low = mid+1
        else:
            if nums[mid]<target<=nums[high]:
                low = mid+1
            else:
                high = mid-1
    return -1

## This logic will work when we don't have duplicate (means low, mid and high value are not equal that's why they are helping us in guiding the direction)
nums = [11, 15, 20, 1, 4, 5, 6, 8, 9, 10]
# nums = [11, 15, 20, 21,23,34,45,56, 8, 9, 10]

target = 8
print(f"Index of {target}: {search_rot_array(nums, target)}")