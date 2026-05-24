'''
https://leetcode.com/problems/frequency-of-the-most-frequent-element/description/
'''

class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        left, right =0, 0
        res, total = 0, 0 

        while right <len(nums):  ## we're moving right pointer faster so use right over here
            total +=nums[right]  ## as you keep moving right... save the sum of those value

            while nums[right]*(right - left +1) > total+k:  ## in case of INVALID Scenario 
                total -= nums[left] ## invalid scenario so remove left most value from total as we are not considering it any more in window
                left+=1
            # Keep track of the maximum frequency (window size) achieved
            res = max(res, right - left +1)
            right+=1

        return res
                
nums = [1,2,4] 
k = 5

c1 = Solution()
print(c1.maxFrequency(nums, k))