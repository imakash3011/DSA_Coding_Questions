'''
https://leetcode.com/problems/single-number/description/
'''

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dct = {}
        for i in nums:
            dct[i] = dct.get(i, 0) +1

        for i,j in dct.items():
            if j==1:
                return i
        return -1
    


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        res = 0
        for n in nums:
            res ^= n
        return res

        
    

nums = [2,2,1]
c1 = Solution()
print(c1.singleNumber(nums))