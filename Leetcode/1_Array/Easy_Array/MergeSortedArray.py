'''
https://leetcode.com/problems/merge-sorted-array/description/
'''

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        result = []
        left = 0
        right = 0

        while left<m and right<n:
            if nums1[left]<=nums2[right]:
                result.append(nums1[left])
                left+=1
            else:
                result.append(nums2[right])
                right+=1
        while left<m:
            result.append(nums1[left])
            left+=1
        while right<n:
            result.append(nums2[right])
            right+=1
        nums1[:] = result
        return result       


nums1 = [1,2,3,0,0,0]
m = 3 
nums2 = [2,5,6]
n = 3
c1 = Solution()
print(c1.merge(nums1, m, nums2, n))