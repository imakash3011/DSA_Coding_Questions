'''
https://leetcode.com/problems/maximum-subarray/description/
'''

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        curr_sum = 0
        max_element = nums[0]
        for num in nums:
            curr_sum+=num

            if curr_sum>max_element:
                max_element = curr_sum
            if curr_sum<0:
                curr_sum = 0
    
        return max_element
nums = [5,4,-1,7,8]
c1 = Solution()
print(c1.maxSubArray(nums))
