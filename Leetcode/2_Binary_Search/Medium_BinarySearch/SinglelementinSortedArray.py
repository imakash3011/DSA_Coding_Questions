'''https://leetcode.com/problems/single-element-in-a-sorted-array/description/'''


class Solution:
    def singleNonDuplicate(self, nums: list[int]) -> int:
        low = 0
        high = len(nums) - 1
        
        while low < high:
            mid = (low + high) // 2
            
            # mid ^ 1 checks the expected partner index:
            # - If mid is even, mid ^ 1 is mid + 1
            # - If mid is odd, mid ^ 1 is mid - 1
            # print(low, high, mid, mid^1, nums[mid ^ 1])
            if nums[mid] == nums[mid ^ 1]:  ## Inituition if 1 element is single then no. of element will be 2*n+1 (this is where xor function is helping us to always look inot that side where we have 1 extra element and eliminate the other half )
                
                # The pattern is perfectly intact. 
                # The single element must lie to the right of mid.
                low = mid + 1
            else:
                # The pattern is broken. 
                # The single element is either at mid or to the left of mid.
                high = mid
                
        # When low == high, they point directly to the unique element
        return nums[low]

nums = [1,1,2,3,3,4,4,8,8]
c1= Solution()
print(c1.singleNonDuplicate(nums))