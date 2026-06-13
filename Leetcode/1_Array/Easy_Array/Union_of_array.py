## Union of two sorted array

class Solution:
    def unionArray(self, nums1, nums2):
        left = 0
        right = 0
        m = len(nums1)
        n = len(nums2)
        result = []
        while left<m and right<n:
            if nums1[left] == nums2[right]:
                if not result or result[-1] != nums1[left]:
                    result.append(nums1[left])
                left+=1
                right+=1
            elif nums1[left] < nums2[right]:
                if not result or result[-1] != nums1[left]:
                    result.append(nums1[left])
                left+=1
            else:
                if not result or result[-1] != nums2[right]:
                    result.append(nums2[right])
                right+=1
        
        while left<m:
            if not result or result[-1] != nums1[left]:
                result.append(nums1[left])
            left+=1
        
        while right<n:
            if not result or result[-1] != nums2[right]:
                result.append(nums2[right])
            right+=1

        return result

nums1 = [3, 4, 6, 7, 9, 9]
nums2 = [1, 5, 7, 8, 8]
c1 = Solution()
print(c1.unionArray(nums1, nums2))