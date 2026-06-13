'''
https://leetcode.com/problems/majority-element/description/
'''

# class Solution:
#     def majorityElement(self, nums: List[int]) -> int:
#         dct = {}
#         for i in nums:
#             dct[i] = dct.get(i, 0)+1
#         count = -1
#         res = -1
#         for i,j in dct.items():
#             if j>=count:
#                 res = i
#                 count = j
#         return res
    
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dct = {}
        count = -1
        res = -1

        for i in nums:
            dct[i] = dct.get(i, 0)+1
            if  dct[i]>count:
                count = dct[i]
                res = i
        return res

nums = [3, 3, 6, 1]
c1 = Solution()
print(c1.majorityElement(nums))