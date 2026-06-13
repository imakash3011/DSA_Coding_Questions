
# '''Capacity To Ship Packages Within D Days'''

# class Solution:
#     def shipWithinDays(self, weights: List[int], days: int) -> int:
#         def calc_capacity(weights, mid):
#             n = len(weights)
#             total = 0
#             cnt=0
#             for  i  in range(n):
#                 total+= weights[i]
#                 if total>mid:
#                     cnt+=1
#             return cnt


#         low = max(weights)
#         high = sum(weights)
#         while low<=high:
#             mid = (low+high)//2
#             day_req = calc_capacity(weights, mid)
#             if day_req<=days:
#                 high = mid-1
#             else:
#                 low=mid+1
#         return low



# weights = [1,2,3,4,5,6,7,8,9,10] 
# days = 5
# c1 = Solution()
# print(c1.shipWithinDays(weights, days))



'''https://leetcode.com/problems/find-the-smallest-divisor-given-a-threshold/description/'''

# import math

# class Solution:
#     def smallestDivisor(self, nums: List[int], threshold: int) -> int:
#         def find_divisor(nums, mid):
#             total = 0
#             for i in nums:
#                 total += math.ceil(i/mid)
#             return total


#         low = 1
#         high =max(nums)
#         while low<=high:
#             mid = (low+high)//2
#             res = find_divisor(nums, mid)
#             if res<=threshold:
#                 high = mid-1
#             else:
#                 low = mid+1
#         return low


# nums = [1,2,5,9]
# threshold = 6
# c1 = Solution()
# print(c1.smallestDivisor(nums, threshold))




'''Minimum Number of Days to Make m Bouquets'''

# class Solution:
#     def minDays(self, bloomDay: List[int], m: int, k: int) -> int:









# bloomDay = [1,10,3,10,2]
# m = 3 
# k = 1
# c1 = Solution()
# print(c1.minDays(bloomDay, m, k))




# ''' Aggressive Cow'''

# def aggressive_cows_binary(stalls: list[int], cows: int) -> int:

#     def valid_dist_check(stalls, mid, cows):
#         last_placed = 0
#         cnt_cows = 1
#         for i in range(len(stalls)):
#             if (stalls[i] - last_placed)>=mid:
#                 cnt_cows+=1
#                 last_placed = stalls[i]
            
#             if cnt_cows>=cows:
#                 return True
#         return False

#     stalls.sort()
#     low = 1
#     high = stalls[-1] - stalls[0]
#     best_ans = -1
#     while low<=high:
#         mid = (low+high)//2
#         result = valid_dist_check(stalls, mid, cows)
#         if result:
#             best_ans = mid
#             low = mid+1
#         else:
#             high = mid-1
#     return best_ans



# cows = 2
# stalls = [4, 2, 1, 3, 6]

# # print(aggressive_cows_linear(stalls, cows) )
# print(aggressive_cows_binary(stalls, cows))


# '''Find First and Last Position of Element in Sorted Array'''





# '''https://takeuforward.org/plus/dsa/problems/floor-and-ceil-in-sorted-array?source=strivers-a2z-dsa-track'''
# # Floor and Ceil in Sorted Array

# class Solution:
#     def getFloorAndCeil(self, nums, x):
#         n = len(nums)
#         low = 0
#         high = n-1
#         floor, ceil =0, 0
#         while low<= high:
#             mid = (low+high)//2
#             if nums[mid]==x:
#                 return nums[mid], nums[mid]
#             if nums[mid]>x:
#                 ceil = nums[mid]
#                 high = mid-1
#             else:
#                 floor = nums[mid]
#                 low = mid+1            
#         return floor, ceil


# # nums =[3, 4, 4, 7, 8, 10]
# # x = 5
# # c1 = Solution()
# # print(c1.getFloorAndCeil(nums, x))


# ''' Upper Bound'''

# class Solution:
#     def lowerBound(self, nums, x):
#         n = len(nums)
#         low = 0
#         high = n-1
#         while low<= high:
#             mid = (low+high)//2
#             if nums[mid]==x:
#                 return mid
#             if nums[mid]>x:
#                 high = mid-1
#             else:
#                 low = mid+1
#         return low



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
