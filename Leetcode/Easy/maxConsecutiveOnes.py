'''
https://leetcode.com/problems/max-consecutive-ones/description/
'''

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        max_res = 0
        for i in nums:
            if i==1:
                count+=1
                if count>max_res:
                    max_res = count
            else:
                count = 0
        return max_res    


nums = [1,0,1,1,0,1]
c1 = Solution()
print(c1.findMaxConsecutiveOnes(nums))