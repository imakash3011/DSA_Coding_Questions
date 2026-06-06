'''https://leetcode.com/problems/median-of-two-sorted-arrays/description/'''


class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        # We always want to do binary search on the smaller array to reduce time complexity.
        if len(nums1) > len(nums2):
            return self.findMedianSortedArrays(nums2, nums1)
        
        n1 = len(nums1)
        n2 = len(nums2)
        
        low = 0
        high = n1
        
        while low <= high:
            cut1 = (low + high) // 2
            cut2 = (n1 + n2 + 1) // 2 - cut1
            
            # If cut1 is 0, it means nothing is picked from the left of nums1. Use -infinity.
            # If cut1 is n1, it means nothing is picked from the right of nums1. Use infinity.
            l1 = float('-inf') if cut1 == 0 else nums1[cut1 - 1]
            l2 = float('-inf') if cut2 == 0 else nums2[cut2 - 1]
            
            r1 = float('inf') if cut1 == n1 else nums1[cut1]
            r2 = float('inf') if cut2 == n2 else nums2[cut2]
            
            # Check if we found the valid partition
            if l1 <= r2 and l2 <= r1:
                # If the total length is even
                if (n1 + n2) % 2 == 0:
                    return (max(l1, l2) + min(r1, r2)) / 2.0
                # If the total length is odd
                else:
                    return float(max(l1, l2))
                
            # If l1 is greater than r2, we need to move the cut to the left
            elif l1 > r2:
                high = cut1 - 1
            # Otherwise, move the cut to the right
            else:
                low = cut1 + 1
                
        return 0.0

nums1 = [1,2] 
nums2 = [3,4]
c1 =Solution()
print(c1.findMedianSortedArrays(nums1, nums2))


######################### BRUTE FORCE APPROACH ##############################################
# class Solution:
#     def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
#         new_lst = nums1+nums2    ## Instead you can use merge sort as we have two sorted array
#         new_lst.sort() 
#         n = len(new_lst)
#         print(new_lst, n)
#         if n%2==0:
#             left = n//2-1
#             right = (n//2)
#             res = (new_lst[left] + new_lst[right])/2
#             return res
#         else:
#             mid = n//2
#             res = (new_lst[mid])
#             return res

# nums1 = [1,2] 
# nums2 = [3,4]
# c1 =Solution()
# print(c1.findMedianSortedArrays(nums1, nums2))