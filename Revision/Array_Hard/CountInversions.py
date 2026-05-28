class Solution:
    def numberOfInversions(self, nums):
        cnt = 0
        n = len(nums)
        for i in range(n):
            for j in range(i+1, n):
                if nums[i]>nums[j] and i<j:
                    cnt+=1
        
        return cnt

nums =  [-10, -5, 6, 11, 15, 17]
c1 = Solution()
print(c1.numberOfInversions(nums))