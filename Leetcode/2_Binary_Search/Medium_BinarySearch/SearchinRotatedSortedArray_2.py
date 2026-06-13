'''https://leetcode.com/problems/search-in-rotated-sorted-array/description/'''

class Solution:
    # 1. Added 'self' and adjusted parameters to match LeetCode style
    def search(self, nums: list[int], target: int) -> int:
        n = len(nums)
        low, high = 0, n - 1
        
        while low <= high:
            mid = (high + low) // 2
            
            if nums[mid] == target:
                return True
            if nums[low]==nums[mid] and nums[mid]==nums[high]:   # ex. [3,1,2,3,3,3,3] for this type of cases we will have problem
                low = low+1
                high = high-1
                continue
                
            # Left half is sorted
            if nums[low] <= nums[mid]:
                if nums[low] <= target <= nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            # Right half is sorted
            else:
                if nums[mid] <= target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
        return False

# Driver code 
nums = [1]
target = 1

c1 = Solution()
# 2. Correctly passes only two parameters now
print(f"Element found : {c1.search(nums, target)}")