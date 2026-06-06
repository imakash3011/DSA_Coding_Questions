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
                # print(complement, seen, seen[complement], [seen[complement], i])
                return [seen[complement], i]
            
            # If not found, save the current number and its index to memory
            seen[num] = i    # This problem have only solution

# class Solution:
#     def twoSum(self, nums: list[int], target: int) -> list[int]:
#         n = len(nums)
#         for i in range(n):
#             remaining = target - nums[i]
#             if remaining in nums:
#                 return i, nums.index(remaining)
#         remaining -1, -1

nums = [2,7,11,15]
target = 9
c1 = Solution()
print(c1.twoSum(nums, target))