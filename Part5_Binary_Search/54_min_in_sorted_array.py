# Intuition is... if a (ex:- Low to mid) is sorted means minimum will present on otherside.
## if on otherwse... mid to high if the sorted criteria is not being true then obviously it is breaking somewhere in the middle where minimum is present
 


def min_in_sorted_array(nums):
    n = len(nums)
    low = 0
    high = n-1
    min_val = float('inf')
    while low<=high:
        mid = (low+high)//2
        if nums[mid]<=nums[high]:
            min_val = min(min_val,nums[mid])
            high = mid-1  ## To check in opposite direction
        else:                                   
            min_val = min(min_val,nums[low])
            low = mid+1    ## Opposite of above scenrio where low is bigger than mid
    return min_val

nums = [4,5,6,7,0,1,2]
print(min_in_sorted_array(nums))
