'''
https://leetcode.com/problems/subarray-sum-equals-k/description/
'''



############## BRUTE FORCE APPROACH ########################
# class Solution:
#     def subarraySum(self, nums: List[int], k: int) -> int:
#         cnt = 0
#         n = len(nums)
#         for i in range(n):
#             total = 0
#             for j in range(i,n):
#                 total +=nums[j]
#                 if total == k:
#                     cnt+=1
#         return cnt


class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        cnt = 0
        current_sum = 0
        
        # This dictionary stores: { past_sum : how_many_times_it_occurred }
        # Base case: A sum of 0 has occurred 1 time before we even start
        prefix_sums = {0: 1}  # to handle this type of case nums = [5, 2, 3] and k = 5 this initialization is required
        
        for num in nums:
            current_sum += num  # Keep track of the running total
            
            # This is your exact 'target' concept! 
            # If (current_sum - target) == k, then target == current_sum - k
            target = current_sum - k  
            
            # Instead of 'if target in nums[i+1:]', we check our history dictionary
            if target in prefix_sums:
                cnt += prefix_sums[target]
            
            # Record this current_sum into our history so future numbers can look back at it
            prefix_sums[current_sum] = prefix_sums.get(current_sum, 0) + 1
            
        return cnt
    
nums = [1, -1, 0]
k = 0
c1 = Solution()
print(c1.subarraySum(nums, k))  
