class Solution:
    def lower_bound_func(self, nums, target):
        low, high = 0, len(nums) - 1
        ans = len(nums) # Default if no element is >= target

        while low <= high:
            mid = (low + high) // 2
            if nums[mid] >= target:
                ans = mid
                high = mid - 1 # Look for even smaller index on the left
            else:
                low = mid + 1
        return ans

    def upper_bound_func(self, nums, target):
        low, high = 0, len(nums) - 1
        ans = len(nums) # Default if no element is > target

        while low <= high:
            mid = (low + high) // 2
            if nums[mid] > target:
                ans = mid
                high = mid - 1 # Look for even smaller index on the left
            else:
                low = mid + 1
        return ans
    
    def result(self, nums, target):
        lb = self.lower_bound_func(nums, target)
        ub = self.upper_bound_func(nums, target)
        # ub - 1 gives the last occurrence of the target
        return lb, ub

# Usage
nums = [1, 2, 3, 3, 3, 3, 4, 5, 6, 7, 8, 9, 9, 10]
target = 3

sol = Solution()
lb, ub = sol.result(nums, target)

print(f"Lower Bound (index of first 3): {lb}")
print(f"Upper Bound (index of first element > 3): {ub}")
print(f"Range of 3: Indices {lb} to {ub - 1}")