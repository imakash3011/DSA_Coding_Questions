'''
https://leetcode.com/problems/find-the-smallest-divisor-given-a-threshold/
'''
import math
from typing import List

class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        # Helper function to calculate the sum of divisions given a divisor
        def get_division_sum(divisor: int) -> int:
            total_sum = 0
            for num in nums:
                total_sum += math.ceil(num / divisor)
            return total_sum

        # The search space for the divisor
        left = 1
        right = max(nums)
        ans = right
        
        while left <= right:
            mid = (left + right) // 2
            
            # If the current sum is within the threshold, it's a valid candidate
            if get_division_sum(mid) <= threshold:
                ans = mid        # Record the valid divisor
                right = mid - 1  # Try to find a smaller valid divisor on the left
            else:
                left = mid + 1   # Divisor is too small, look on the right
                
        return ans

# Test Case
nums = [1, 2, 5, 9] 
threshold = 6
c1 = Solution()
print(c1.smallestDivisor(nums, threshold))  # Output: 5



