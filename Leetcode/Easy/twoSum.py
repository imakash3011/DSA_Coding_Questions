'''
https://leetcode.com/problems/two-sum/description/
'''


# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         n = len(nums)
#         for i in range(n):
#             for j in range(i+1,  n):
#                 if nums[i]+nums[j] == target:
#                     return [i,j]


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # Create a hash map to store: { number: its_index }
        seen = {}
        
        for i, num in enumerate(nums):
            # Calculate the exact number we need to reach the target
            complement = target - num
            
            # Check if this required number is already in our hash map memory
            if complement in seen:
                # If found, return the index of the complement and the current index
                return [seen[complement], i]
            
            # If not found, save the current number and its index to memory
            seen[num] = i

nums = [2,7,11,15]
target = 9
c1 = Solution()
print(c1.twoSum(nums, target))