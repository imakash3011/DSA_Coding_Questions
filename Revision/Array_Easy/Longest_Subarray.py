class Solution:
    def longestSubarray(self, nums, k):
        n = len(nums)
        for i in range(n):
            temp = 0
            digit_count = 0
            for j in range(i+1,n):
                if temp == k:
                    return digit_count
                else:
                    temp += nums[j]
                    digit_count +=1
        return digit_count

nums = [-3, 2, 1]
k=6
c1 = Solution()
print(c1.longestSubarray(nums, k))