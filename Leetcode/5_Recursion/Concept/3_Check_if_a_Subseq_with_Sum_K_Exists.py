############ WHEN SUBSET AND BOOLEAN RESULT BOTH ARE NEEDED ########


# class Solution:
#     def Check_if_a_Subseq_with_Sum_K_Exists(self, nums: List[int], target: int) -> List[List[int]]:
#         result = []

#         def helper_func(idx, total, subset):
#             # Base Case 1: If we reached the target, save it
#             if total == target:
#                 result.append(subset.copy())
#                 return True

#             # Base Case 2: Out of bounds or exceeded the target
#             if idx >= len(nums) or total > target:
#                 return False

#             subset.append(nums[idx])
#             if helper_func(idx + 1, total + nums[idx], subset):   # If this is True
#                 return True

#             subset.pop()
#             if helper_func(idx + 1, total, subset): # If this is True
#                 return True 

#             return False
        
#         has_subset = helper_func(0, 0,  [])
#         return has_subset, result[0] if has_subset else []

# # Test case
# nums = [5, 9, 4] 
# target = 9
# c1 = Solution()
# print(c1.Check_if_a_Subseq_with_Sum_K_Exists(nums, target))  # Output: [[5, 4], [9]]


######## WHEN NO SUBSET IS REQUIRED ##########

class Solution:
    def Check_if_a_Subseq_with_Sum_K_Exists(self, nums: List[int], target: int) -> List[List[int]]:

        def helper_func(idx, total):
            # Base Case 1: If we reached the target, save it
            if total == target:
                return True

            # Base Case 2: Out of bounds or exceeded the target
            if idx >= len(nums) or total > target:
                return False

            if helper_func(idx + 1, total + nums[idx]):   # If this is True
                return True

            if helper_func(idx + 1, total): # If this is True
                return True 

            return False

        return helper_func(0, 0 )

# Test case
nums = [5, 9, 4] 
target = 9
c1 = Solution()
print(c1.Check_if_a_Subseq_with_Sum_K_Exists(nums, target))  # Output: [[5, 4], [9]]