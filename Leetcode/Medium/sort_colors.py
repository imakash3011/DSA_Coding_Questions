# class Solution:
#     def sortColors(self, nums: List[int]) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         dct = {}
#         for i in nums:
#             dct[i] = dct.get(i, 0)+1
        
#         sorted_list =[]
#         for i, j in sorted(dct.items()):
#             sorted_list.extend([i]*j)
#         nums[:] = sorted_list
#         return nums


        
# Dutch National Flag Algorithm (mid index travel and keep 0 left side and 2 right side)
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        n = len(nums)
        low = mid = 0
        high =n-1
        while mid<=high:
            if nums[mid]==0:
                nums[low],nums[mid] = nums[mid],nums[low] 
                low+=1
                mid+=1
            elif nums[mid]==1:
                mid+=1
            else:
                nums[mid], nums[high] = nums[high], nums[mid]
                high-=1
        return nums

## Bubble sort
# class Solution:
#     def sortColors(self, nums: List[int]) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         n = len(nums)
#         for i in range(n):
#             for j in range(i+1,n):
#                 if nums[j]<nums[i]:
#                     nums[i], nums[j] = nums[j], nums[i]
#         return nums

nums = [2,0,2,1,1,0]
c1= Solution()
print(c1.sortColors(nums))