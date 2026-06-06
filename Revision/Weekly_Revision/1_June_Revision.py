''' Aggressive Cow'''

def aggressive_cows_binary(stalls: list[int], cows: int) -> int:

    def valid_dist_check(stalls, mid, cows):
        last_placed = 0
        cnt_cows = 1
        for i in range(len(stalls)):
            if (stalls[i] - last_placed)>=mid:
                cnt_cows+=1
                last_placed = stalls[i]
            
            if cnt_cows>=cows:
                return True
        return False

    stalls.sort()
    low = 1
    high = stalls[-1] - stalls[0]
    best_ans = -1
    while low<=high:
        mid = (low+high)//2
        result = valid_dist_check(stalls, mid, cows)
        if result:
            best_ans = mid
            low = mid+1
        else:
            high = mid-1
    return best_ans



cows = 2
stalls = [4, 2, 1, 3, 6]

# print(aggressive_cows_linear(stalls, cows) )
print(aggressive_cows_binary(stalls, cows))


'''Find First and Last Position of Element in Sorted Array'''





'''https://takeuforward.org/plus/dsa/problems/floor-and-ceil-in-sorted-array?source=strivers-a2z-dsa-track'''
# Floor and Ceil in Sorted Array

class Solution:
    def getFloorAndCeil(self, nums, x):
        n = len(nums)
        low = 0
        high = n-1
        floor, ceil =0, 0
        while low<= high:
            mid = (low+high)//2
            if nums[mid]==x:
                return nums[mid], nums[mid]
            if nums[mid]>x:
                ceil = nums[mid]
                high = mid-1
            else:
                floor = nums[mid]
                low = mid+1            
        return floor, ceil


# nums =[3, 4, 4, 7, 8, 10]
# x = 5
# c1 = Solution()
# print(c1.getFloorAndCeil(nums, x))


''' Upper Bound'''

class Solution:
    def lowerBound(self, nums, x):
        n = len(nums)
        low = 0
        high = n-1
        while low<= high:
            mid = (low+high)//2
            if nums[mid]==x:
                return mid
            if nums[mid]>x:
                high = mid-1
            else:
                low = mid+1
        return low



# nums =[3,5,8,15,19]
# x = 9
# c1 = Solution()
# print(c1.lowerBound(nums, x))


''' Lower Bound'''
# class Solution:
#     def lowerBound(self, nums, x):
#         n = len(nums)
#         left = 0
#         right = n-1
#         while left<=right:
#             mid = (left+right)//2
#             if nums[mid]>=x:
#                 right = mid-1
#             else:
#                 left = mid+1

#         return left


# nums =[3,5,8,15,19]
# x = 9
# c1 = Solution()
# print(c1.lowerBound(nums, x))

'''https://leetcode.com/problems/binary-search/description/'''



# class Solution:
#     def search(self, nums: List[int], target: int) -> int:
#         n = len(nums)
#         left = 0
#         right = n-1
#         while left<=right:
#             mid = (left+right)//2
#             if nums[mid] == target:
#                 return mid
#             if target < nums[mid]:
#                 right = mid-1
#             else:
#                 left = mid+1
#         return mid


# nums = [-1,0,3,5,9,12] 
# target = 9
# c1 = Solution()
# print(c1.search(nums, target))
