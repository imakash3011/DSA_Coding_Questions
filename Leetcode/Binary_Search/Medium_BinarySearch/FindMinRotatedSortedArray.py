'''https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/'''

class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        low = 0
        high = n-1
        min_val = float('inf')
        while low<=high:
            mid = (low+high)//2
            if nums[mid]<=min_val:
                min_val = nums[mid]
            if nums[low]<=nums[mid]:  # If this is sorted take its minimum value and eliminate this half
                min_val = min(min_val, nums[low])
                low = mid+1  # Eliminate the sorted left half, search in the right half
            else:
                min_val = min(min_val, nums[mid])  # Eliminate the sorted right half, search in the left half
                high = mid-1
        return min_val


nums =[3,1,2]
c1 = Solution()
print(c1.findMin(nums))