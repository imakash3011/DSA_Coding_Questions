'''
https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/description/
'''

# class Solution:
#     def check(self, nums: List[int]) -> bool:
#         idx = -1
#         n = len(nums)
#         for i in range(n-1):
#             if nums[i+1]<nums[i]:
#                 idx = i+1
                
#         if idx == -1 :
#             return True

#         new_num = nums[idx:] +nums[:idx]
#         for i in range(n-1):
#             if new_num[i+1]< new_num[i]:
#                 return False

#         return True
    
class Solution:
    def check_sorted_array_2(self, nums):
        count=0
        n = len(nums)
        for i in range(1, n):
            if nums[i-1]>nums[i]:
                count+=1
        if nums[-1]>nums[0]:
            count+=1

        return count<=1


nums = [1,3,4, ]
c1 = Solution()
print(c1.check_sorted_array_2(nums))

