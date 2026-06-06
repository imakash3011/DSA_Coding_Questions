'''
https://leetcode.com/problems/remove-duplicates-from-sorted-array
'''

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        res = 1
        n = len(nums)
        if not nums:
            return 0
        for i in range( n-1):
            if nums[i]!=nums[i+1]:
                nums[res] = nums[i+1]
                res+=1
        return res

nums =[1,1,2]
c1 = Solution()
print(c1.removeDuplicates(nums))