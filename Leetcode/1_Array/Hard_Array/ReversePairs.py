'''
https://leetcode.com/problems/reverse-pairs/description/

'''
from typing import List

class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        def merge_sort(low: int, high: int) -> int:
            if low >= high:
                return 0
            
            mid = (low + high) // 2
            count = 0
            
            # 1. Recursively count reverse pairs in left and right halves
            count += merge_sort(low, mid)
            count += merge_sort(mid + 1, high)
            
            # 2. Count the reverse pairs across the left and right halves
            count += count_pairs(low, mid, high)
            
            # 3. Merge the two sorted halves
            merge(low, mid, high)
            
            return count

        def count_pairs(low: int, mid: int, high: int) -> int:
            right = mid + 1
            cnt = 0
            # Two-pointer approach to count pairs satisfying nums[i] > 2 * nums[j]
            for i in range(low, mid + 1):
                while right <= high and nums[i] > 2 * nums[right]:
                    right += 1
                cnt += (right - (mid + 1))
            return cnt

        def merge(low: int, mid: int, high: int):
            # Standard merge process to sort the array
            temp = []
            left = low
            right = mid + 1
            
            while left <= mid and right <= high:
                if nums[left] <= nums[right]:
                    temp.append(nums[left])
                    left += 1
                else:
                    temp.append(nums[right])
                    right += 1
                    
            while left <= mid:
                temp.append(nums[left])
                left += 1
                
            while right <= high:
                temp.append(nums[right])
                right += 1
                
            # Copy sorted elements back into the original array
            for i in range(low, high + 1):
                nums[i] = temp[i - low]

        return merge_sort(0, len(nums) - 1)

nums = [2, 4, 3, 5, 1]
c1 = Solution()
print(c1.reversePairs(nums))  # Output: 3


############### BRUTE FORCE ##################
class Solution:
    def reversePairs(self, nums: List[int]) -> int:
        cnt = 0
        n = len(nums)
        if n==1:
            return cnt
        for i in range(n):
            for j in range(i+1,n):
                if nums[i]> (2*nums[j]):
                    cnt+=1
        return cnt
        

# nums = [2,4,3,5,1]
# c1  = Solution()
# print(c1.reversePairs(nums))



######################## IDEA #################

# [  Left Sorted Half  ]   vs   [  Right Sorted Half  ]
#      i ->                         j ->
#    (Checks: nums[i] > 2 * nums[j])