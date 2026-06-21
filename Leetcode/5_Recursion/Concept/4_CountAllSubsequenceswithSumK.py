################## OPTIMAL APPROACH WITH Positive Number only in array #######
class Solution:
    def subsets_sum_k(self, nums: List[int], target: int) -> List[List[int]]:

        def helper_func(idx, total):
            # Base Case 1: If we reached the target, save it
            if total == target:
                return 1

            # Base Case 2: Out of bounds or exceeded the target
            if idx >= len(nums) or total > target:
                return 0

            pick = helper_func(idx + 1, total + nums[idx])  

            not_pick = helper_func(idx + 1, total) 

            return pick + not_pick
        

        return helper_func(0, 0)

# Test case
nums = [5, 9, 4] 
target = 9
c1 = Solution()
print(c1.subsets_sum_k(nums, target))  # Output: [[5, 4], [9]]

