class Solution:
    def subarraysWithXorK(self, nums, k):
        n = len(nums)
        cnt = 0
        for i in range(n):
            temp = nums[i]
            if temp == k:
                cnt+=1
            for j in range(i+1,n):
                temp=temp^nums[j]
                if temp ==k:
                    cnt+=1
        return cnt



nums =[4, 2, 2, 6, 4]
k = 6
c1 = Solution()
print(c1.subarraysWithXorK(nums, k))