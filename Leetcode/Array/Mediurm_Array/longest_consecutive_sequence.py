'''
https://codeanddebug.in/blog/longest-consecutive-sequence/

https://leetcode.com/problems/longest-consecutive-sequence/description/
'''
########## BRUTE FORCE ############# 

# class Solution:
#     def longestConsecutive(self, nums: List[int]) -> int:
#         max_count = 0
#         for i in nums:
#             temp = i
#             cnt = 1
#             while temp+1 in nums:
#                 temp+=1
#                 cnt+=1
#             max_count = max(max_count, cnt)
#         return max_count
    

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
            
        nums = sorted(nums)
        
        # We start both at 1 because if the array has elements, 
        # the minimum sequence length is always 1.
        max_count = 1  
        temp = 1
        n = len(nums)
        
        for i in range(n - 1):
            # Condition 1: Consecutive element found
            if nums[i] + 1 == nums[i + 1]:
                temp += 1
                max_count = max(max_count, temp)
            # Condition 2: Duplicate element found  (IMPORTANT HERE WE DON'T HAVE TO INCREMENT)
            elif nums[i] == nums[i + 1]:
                continue # Skip it, do not reset temp!
            # Condition 3: Sequence broken
            else:
                temp = 1
        return max_count


nums= [1,0,1,2]

c1 = Solution()
print(c1.longestConsecutive(nums))