'''
https://takeuforward.org/plus/dsa/problems/leaders-in-an-array?source=strivers-a2z-dsa-track
'''

# class Solution:
#     def leaders(self, nums):
#         res =[]
#         n = len(nums)
#         if n==1:
#             return nums[0]
#         for i in range(n):
#             flag = True
#             for j in range(i+1, n):
#                 if nums[j]>nums[i]:
#                     flag = False
#                     continue
#             if flag == True:
#                 res.append(nums[i])

#         return res


class Solution:
    def leaders(self, nums):
        res = []
        n = len(nums)
        
        # Edge case: if the array is empty
        if n == 0:
            return res
            
        # 1. The rightmost element is always a leader (because no one is present after it so it is biggest)
        max_from_right = nums[-1]
        res.append(max_from_right)
        
        # 2. Scan the array from right to left (excluding the last element)
        for i in range(n - 2, -1, -1):
            if nums[i] >= max_from_right:
                res.append(nums[i])
                max_from_right = nums[i] # Update the maximum seen so far
                
        # 3. Since we traversed from right to left, the result is reversed.
        # Reverse it back to maintain original relative order.
        return res[::-1]

nums = [1, 2, 5, 3, 1, 2]
c1 = Solution()
print(c1.leaders(nums))