'''
This question is completely depend upon the "lower bound answer" 
what ever will be the lower bound index that will be the position where we need to insert the new element.
'''

class Solution:
    def SearchInsertPosition(self, nums, x):
        n = len(nums)
        left = 0
        right = n-1
        ans = n # by default we will return n is number doesn;t exist
        while left <= right:
            mid = (left+right)//2
            if nums[mid]>=x:
                ans = mid
                right= mid-1
            else:
                left = mid+1
        return ans     

c1 = Solution()
nums =[1,3,5,6]
x = 5
print(c1.SearchInsertPosition(nums, x))