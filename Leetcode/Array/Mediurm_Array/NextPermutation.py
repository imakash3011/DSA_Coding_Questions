'''
https://leetcode.com/problems/next-permutation/description/
'''

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        breaking_idx = -1
        n = len(nums)

        # Step 1: Find the breakpoint from the right
        for i in range(n-2, -1, -1):
            if nums[i]<nums[i+1]:
                breaking_idx = i
                break
        
        # Edge Case: If no breakpoint is found, the array is in descending order.
        # The next permutation is the entirely reversed (smallest) array.
        if breaking_idx == -1:
            return nums[::-1]
        
        # Step 2: Find the next greater element from the right to swap with
        for i in range( n-1, breaking_idx, -1):
            if nums[i]>nums[breaking_idx]:
                nums[i], nums[breaking_idx] = nums[breaking_idx], nums[i]
                break

        # Step 3: Reverse the suffix to make it as small as possible
        # We reverse everything to the right of the breakpoint_idx
        left = breaking_idx+1
        right = n-1

        while left<right:
            nums[left], nums[right] = nums[right], nums[left]
            left+=1
            right+=1
        
        return nums
        

nums = [3,2,1]
c1 = Solution()
print(c1.nextPermutation(nums))


################ TO find all permutation of a given number #############
# class Solution:
#     def nextPermutation(self, nums: List[int]) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         permutations = [[]]

#         for num in nums:
#             next_permutations =[]

#             for p  in permutations:
#                 for i in range(len(p)+1):
#                     new_p = p[:i]+[num]+p[i:]
#                     next_permutations.append(new_p)
#             permutations =next_permutations

#         return permutations
        


# nums = [1,2,3]
# c1 = Solution()
# print(c1.nextPermutation(nums))