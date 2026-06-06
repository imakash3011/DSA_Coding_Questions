'''
https://takeuforward.org/plus/dsa/problems/floor-and-ceil-in-sorted-array?source=strivers-a2z-dsa-track
'''

''' It is just a combination of lower and upper bound. '''


class Solution:
    def Floor_Ceil(self, nums, x):
        n = len(nums)
        left = 0
        right = n-1
        floor, ceil = -1, -1
        while left <= right:
            mid = (left+right)//2
            if nums[mid]==x:
                return nums[mid], nums[mid]
            if nums[mid]>x:
                ceil= nums[mid]  # consider mid as ceil for now and ultimately at the end it will become our answer
                right= mid-1
            else:
                floor = nums[mid] # consider mid as floor for now and ultimately at the end it will become our answer 
                left = mid+1
        return floor, ceil     

c1 = Solution()
nums =[5,7,7,8,8,10]
x = 9
print(c1.Floor_Ceil(nums, x))