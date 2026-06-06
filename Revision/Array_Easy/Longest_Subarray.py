'''https://takeuforward.org/plus/dsa/problems/longest-subarray-with-sum-k?source=strivers-a2z-dsa-track'''


class Solution:
    def longestSubarray(self, nums, k):
        n = len(nums)
        max_len = 0
        
        for i in range(n):
            temp_sum = 0
            # Start j from i, not i+1, so we include nums[i]
            for j in range(i, n):
                temp_sum += nums[j]
                
                # If we hit k, update max_len, but KEEP GOING (don't return)
                # because adding a '0' later might make the subarray longer.
                if temp_sum == k:
                    max_len = max(max_len, j - i + 1)
                    
        return max_len