# class Solution:
#     def findPeakElement(self, nums: List[int]) -> int:
#         n = len(nums)
#         low,high = 0, n-1
#         # peak_element = float('-inf')
#         while low<high:  # We loop until low and high converge to a single element
#             mid = (low+high)//2
#             if nums[mid]<nums[mid+1]:
#                 low = mid+1
#             else:
#                 high = mid  ## High will come to mid position that
#         return low
    
# nums = [1,2,3,1]
# c1 = Solution()
# print(c1.findPeakElement(nums))



class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n = len(nums)
        low,high = 0, n-1
        # peak_element = float('-inf')
        while low<=high:  # We loop until low and high converge to a single element
            mid = (low+high)//2
            if nums[mid]<nums[mid+1]:
                low = mid+1
            else:
                high = mid-1 ## High will come to mid position that
        return low
    
nums = [1,2,3,1]
c1 = Solution()
print(c1.findPeakElement(nums))








# 1. while low <= high (The "Find an Element" approach)
# Use this when you are searching for a specific target value in the array, and you want to look at every single individual element until you either find it or run out of options.


# 2. while low < high (The "Reduce the Range" approach)
# Use this when you are shrinking the search space to find a specific condition, boundary, or optimal value (like a minimum or a peak), rather than matching an exact target value.