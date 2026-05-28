'''
https://leetcode.com/problems/majority-element-ii/description/
'''

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n_3rd =len(nums)//3
        # print(n_3rd)

        dct = {}
        for i in nums:
            dct[i] = dct.get(i ,0 )+1
        result = []
        for i,j in dct.items():
            if j>n_3rd:
                result.append(i)
        
        return result

nums = [1,2]
c1 = Solution()
print(c1.majorityElement(nums))