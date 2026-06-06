'''
https://leetcode.com/problems/maximum-product-subarray/description/
'''

################## OPTIMAL APPROACH ########################
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        max_pdt = float('-inf')
        prefix, suffix= 1, 1
        for i in range(n):
            # if nums==0: prefix =1  # Note this will skip 0 and cases like [-2,0,-1], will fail 
            if prefix == 0:
                prefix = 1
            if suffix == 0:
                suffix = 1
            prefix *= nums[i]
            suffix*= nums[n-i-1]   ### Smartly we're avoid another loop.. it is helping us to run inversely
            max_pdt = max(max_pdt, prefix, suffix)
        return max_pdt

nums = [-2,0,-1]
c1 = Solution()
print(c1.maxProduct(nums))


################### BRUTE FORCE APPROACH ####################
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        result = nums[0]
        n = len(nums)
        for i in range(n):
            temp = 1
            for j in range(i, n):
                temp *=nums[j]
                if temp>result:
                    result = temp                 
        return result 


# nums = [4]
# c1 = Solution()
# print(c1.maxProduct(nums))