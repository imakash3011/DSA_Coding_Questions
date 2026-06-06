# class Solution:
#     def subarraysWithXorK(self, nums, k):
#         n = len(nums)
#         cnt = 0
#         for i in range(n):
#             temp = nums[i]
#             if temp == k:
#                 cnt+=1
#             for j in range(i+1,n):
#                 temp=temp^nums[j]
#                 if temp ==k:
#                     cnt+=1
#         return cnt


class Solution:
    def subarraysWithXorK(self, nums, k):
        seen = {0:1}
        xr = 0
        n = len(nums)
        max_len = 0
        for i in range(n):
            xr = xr^nums[i]
            target = xr^k
            if target in seen:
                max_len += seen[target]
            seen[xr] = seen.get(xr, 0)+1
        return max_len

nums =[4, 2, 2, 6, 4]
k = 6
c1 = Solution()
print(c1.subarraysWithXorK(nums, k))