'''https://leetcode.com/problems/check-if-bitwise-or-has-trailing-zeros/description/?envType=problem-list-v2&envId=bit-manipulation'''


class Solution:
    def hasTrailingZeros(self, nums: List[int]) -> bool:
        n = len(nums)
        for i in range(n):
            for  j in range(i+1, n):
                temp = nums[i] | nums[j]
                mask = 1<<0
                if temp&mask==0:
                    # print(nums[i], nums[j])
                    return True
        
        return False
        

nums = [2,4,8,16]
c1 = Solution()
print(c1.hasTrailingZeros(nums))