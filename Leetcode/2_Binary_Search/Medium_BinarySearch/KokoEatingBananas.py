'''
https://leetcode.com/problems/koko-eating-bananas/
'''

import math
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        # Helper function to calculate the total hours needed for a specific speed 'k'
        def calculate_total_hours(piles: list[int], k: int) -> int:
            total = 0
            n = len(piles)
            for pile in piles:
                total+= math.ceil(pile/k)
            return total
        
        left = 1
        right = max(piles)
        while left<=right:
            mid = (left+right)//2
            total = calculate_total_hours(piles, mid)
            if total<= h:
                right = mid-1
            else:
                left = mid+1
        
        return left

# --- Example Usage (Matching the video) ---
piles = [3, 6, 7, 11]
H = 8
sol = Solution()
print(f"Minimum eating speed: {sol.minEatingSpeed(piles, H)}")
# Output: 4