def search_rot_array(nums, target):
    low = 0
    high =len(nums)-1

    while low<=high:
        mid = (low+high)//2
        if nums[mid]==target:
            return True
        if nums[mid]==nums[low]==nums[high] :  ## Additional line 
            low = low+1
            high = high-1            
        elif nums[low]<= nums[mid]:
            if nums[low]<=target < nums[mid]:
                high = mid-1
            else:
                low = mid+1
        else:
            if nums[mid]<target<=nums[high]:
                low = mid+1
            else:
                high = mid-1
    return False

## Previous logic will work only when we have separate value for low, mid and high (that's what we are doing here in additional "if" statement

nums = [7,7,7,7,7,7,7,1,2,3,4,5,7,7]

target = 7
print(f"Index of {target}: {search_rot_array(nums, target)}")