'''
https://takeuforward.org/plus/dsa/problems/leaders-in-an-array?source=strivers-a2z-dsa-track
'''

class Solution:
    def leaders(self, nums):
        res =[]
        n = len(nums)
        if n==1:
            return nums[0]
        for i in range(n):
            flag = True
            for j in range(i+1, n):
                if nums[j]>nums[i]:
                    flag = False
                    continue
            if flag == True:
                res.append(nums[i])

        return res


nums = [1, 2, 5, 3, 1, 2]
c1 = Solution()
print(c1.leaders(nums))