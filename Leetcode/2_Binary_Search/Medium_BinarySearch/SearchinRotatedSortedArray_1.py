'''https://leetcode.com/problems/search-in-rotated-sorted-array/description/'''

# class Solution:
#     def search(self, nums: List[int], target: int) -> int:
#         n = len(nums)
#         left = 0
#         right = n-1
#         while left<=right:
#             mid = (left+right)//2
#             if nums[mid]==target:
#                 return mid
            
#             if nums[left]<nums[mid] and target<nums[mid]:
#                 right = mid-1
#             else:
#                 right = mid+1

#             if nums[right]>nums[mid] and target>nums[mid]:
#                 left = mid+1
#             else:
#                 left = mid-1

#         return -1

class Solution:
    # 1. Added 'self' and adjusted parameters to match LeetCode style
    def search(self, nums: list[int], target: int) -> int:
        n = len(nums)
        low, high = 0, n - 1
        
        while low <= high:
            mid = (high + low) // 2
            
            if nums[mid] == target:
                return mid
                
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
        return -1

# Driver code
nums = [4, 5, 6, 7, 0, 1, 2]
target = 0

c1 = Solution()
# 2. Correctly passes only two parameters now
print(f"Element found at index: {c1.search(nums, target)}")