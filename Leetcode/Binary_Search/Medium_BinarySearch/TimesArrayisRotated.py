'''https://takeuforward.org/plus/dsa/problems/find-out-how-many-times-the-array-is-rotated?source=strivers-a2z-dsa-track'''

# class Solution:
#     def findKRotation(self, nums):
#         n = len(nums)
#         low = 0
#         high = n-1
#         min_val = float('inf')
#         min_idx = float('inf')
#         while low<=high:
#             mid = (low+high)//2
#             if nums[mid]<=min_val:
#                 min_val = nums[mid]
#                 min_idx = mid
#             if nums[low]<=nums[mid]:  # If this is sorted take its minimum value and eliminate this half
#                 # min_val = min(min_val, nums[low])
#                 min_idx = min(min_idx, low)
#                 low = mid+1  # Eliminate the sorted left half, search in the right half
#             else:
#                 # min_val = min(min_val, nums[mid])  # Eliminate the sorted right half, search in the left half
#                 min_idx = min(min_idx, mid)
#                 high = mid-1
        
#         return min_idx



class Solution:
    def findKRotation(self, nums):
        low = 0
        high = len(nums) - 1
        
        while low < high:
            mid = (low + high) // 2
            
            # If mid element is greater than high element, 
            # the minimum must be in the right half
            if nums[mid] > nums[high]:
                low = mid + 1
            # Otherwise, the minimum is in the left half (including mid)
            else:
                high = mid
                
        return low

nums =  [4, 5, 6, 7, 0, 1, 2, 3]
c1 = Solution()
print(c1.findKRotation(nums))