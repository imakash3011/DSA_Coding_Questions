## Ceil -> Smallest number in an array (>=tagret)
## Floor -> Largest number in array (<=tagret)

def ceil_the_floor_prob(nums, target):
    low = 0
    high = len(nums) - 1

    while low <= high:
        mid = (low + high) // 2
        
        if nums[mid] == target:
            return [nums[mid], nums[mid]]
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
            
    # After the loop, high is the floor index and low is the ceil index
    # We need to check if they are within the array bounds

    floor = nums[high] if high >= 0 else -1  # (After loop will end high and low will cross each other)
    ceil = nums[low] if low < len(nums) else -1
    
    return [floor, ceil]

nums = [3, 4, 4, 4, 8, 9, 10, 12, 12, 14, 15]
target = 11

print(ceil_the_floor_prob(nums, target))






###################### Approach 2 #######################
def ceil_the_floor(nums, target):
    n = len(nums)
    floor = -1
    ceil = -1
    low, high = 0, n-1
    while low<=high:
        mid = (low + high)//2

        if target == nums[mid]:
            return [nums[mid],nums[mid]]
        elif target<nums[mid]:
            ceil = nums[mid] 
            high = mid-1
        else:
            floor = nums[mid] 
            low = mid+1
    
    return [floor,ceil]


# nums = [3,4,4,4,8,9,10,12,12,14,15]
# target = 11 ## if present return that number itself otherwise return floor and ceiling

# print(ceil_the_floor(nums, target))