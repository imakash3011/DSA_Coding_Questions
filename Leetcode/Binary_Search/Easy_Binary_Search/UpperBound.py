'''
--------------- SEE DIFFERENCE CAREFULLY ---------------------
Lower Bound:- if a number is greater than or equal to "x"   (>=x)
Upper Bound: if a number is strictly greater than "x"  (>x)
'''

class Solution:
    def UpperBound(self, nums, x):
        n = len(nums)
        left = 0
        right = n-1
        ans = n # by default we will return n is number doesn;t exist
        while left <= right:
            mid = (left+right)//2
            if nums[mid]>x:
                ans = mid
                right= mid-1
            else:
                left = mid+1
        return ans     

c1 = Solution()
nums = [5,7,7,8,8,10]
x = 8
print(c1.UpperBound(nums, x))