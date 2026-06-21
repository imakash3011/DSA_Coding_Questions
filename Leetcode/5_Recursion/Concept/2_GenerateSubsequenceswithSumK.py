# Generate Subsequences with Sum K



################## OPTIMAL APPROACH WITH Positive Number only in array #######
class Solution:
    def subsets_sum_k(self, nums: List[int], target: int) -> List[List[int]]:
        result = []

        def helper_func(idx, total, subset):
            # Base Case 1: If we reached the target, save it
            if total == target:
                result.append(subset.copy())
                return  # Since all numbers are positive, adding more won't help

            # Base Case 2: Out of bounds or exceeded the target
            if idx >= len(nums) or total > target:
                return 
                
            # Choice 1: Include nums[idx]
            subset.append(nums[idx])
            helper_func(idx + 1, total + nums[idx], subset)   # Fixed: total + nums[idx]

            # Choice 2: Exclude nums[idx]
            subset.pop()
            helper_func(idx + 1, total, subset)  # IMPORTANT: Just pass total
        
        helper_func(0, 0, [])
        return result

# Test case
# nums = [5, 9, 4] 
# target = 9
# c1 = Solution()
# print(c1.subsets_sum_k(nums, target))  # Output: [[5, 4], [9]]




################## OPTIMAL APPROACH WITH Positive and Negative Number both in array #######

class Solution:
    def subsets_sum_k(self, nums: List[int], target: int) -> List[List[int]]:
        result = []

        def helper_func(idx, total, subset):
            # Base Case: We must look through the ENTIRE array before deciding
            if idx == len(nums):
                if total == target:
                    result.append(subset.copy())
                return
                
            # Choice 1: Include nums[idx]
            subset.append(nums[idx])
            helper_func(idx + 1, total + nums[idx], subset)

            # Choice 2: Exclude nums[idx]
            subset.pop()
            helper_func(idx + 1, total, subset)
        
        helper_func(0, 0, [])
        return result

# Test case with negative numbers
nums = [5, 4, -4, 9] 
target = 9
c1 = Solution()
print(c1.subsets_sum_k(nums, target))  
# Output: [[5, 4, -4, 9], [5, 4], [9]]






#################### BRUTE FORCE###########################

# class Solution:
#     def subsets_sum_k(self, nums: List[int], target:int) -> List[List[int]]:
#         result = []

#         def helper_func(idx,subset, target):
#             if idx >= len(nums):
#                 # print(subset)
#                 if sum(subset) == target:
#                     result.append(subset.copy())
#                 return

#             subset.append(nums[idx])
#             helper_func(idx+1,subset, target)

#             subset.pop()
#             helper_func(idx+1,subset, target)
        
#         helper_func(0, [] , target)
#         return result
            

# nums = [3,5,6,7,2,1] 
# target = 9
# c1 = Solution()
# print(c1.subsets_sum_k(nums, target))