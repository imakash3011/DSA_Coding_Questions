'''Insertion Sort'''

class Solution:
    def insertionSort(self, nums):
        n = len(nums)
        for i in range(n):
            key_ele = nums[i]
            j = i-1
            while j>=0 and nums[j]>key_ele:
                nums[j+1] = nums[j]
                j-=1
            nums[j+1] = key_ele
        
        return nums


nums = [7, 4, 1, 5, 3]
c1 = Solution()
print(c1.insertionSort(nums))




'''Selection Sort'''

# class Solution:
#     def selectionSort(self, nums):
#         n = len(nums)
#         for i in range(n):
#             min_idx = i
#             for j in range(i+1,n):
#                 if nums[min_idx]>nums[j]:
#                     min_idx= j
#             # print(i, j)
#             nums[i], nums[min_idx] = nums[min_idx], nums[i]
#         return nums


# nums = [7, 4, 1, 5, 3]
# c1 = Solution()
# print(c1.selectionSort(nums))

'''4Sum'''

# class Solution:
#     def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
#         n = len(nums)
#         nums.sort()
#         res = []
#         for i in range(n-3):
#             if i>0 and nums[i]==nums[i-1]:
#                 continue
#             for j in range(i+1, n-2):
#                 if j>i+1 and nums[j]==nums[j-1]:
#                     continue
                
#                 left = j+1
#                 right = n-1

#                 while left<right:
#                     temp = nums[i]+nums[j]+nums[left]+nums[right]
#                     if temp>target:
#                         right-=1
#                     elif temp<target:
#                         left+=1
#                     else:
#                         res.append([nums[i], nums[j], nums[left], nums[right]])
#                         left+=1
#                         while left<right and nums[left]==nums[left-1]:
#                             left+=1
#             return res



# nums =[2,2,2,2,2]
# target = 8
# c1 = Solution()
# print(c1.fourSum(nums, target))


'''Reverse Pairs'''
# class Solution:
#     def threeSum(self, nums: list[int]) -> list[list[int]]:
#         res = []
#         n = len(nums)
#         nums.sort()
#         for i in range(n):
#             if i>0 and nums[i]==nums[i-1]:
#                 continue
#             j = i+1
#             k = n-1
#             while j<k:
#                 temp = nums[i]+nums[j]+nums[k]
#                 if temp>0:
#                     k-=1
#                 elif temp<0:
#                     j+=1
#                 else:
#                     res.append([nums[i], nums[j], nums[k]])
#                     j+=1
#                     while j<k and nums[j]==nums[j-1]:
#                         j+=1
#         return res


# nums = [-1,0,1,2,-1,-4]
# c1 = Solution()
# print(c1.threeSum(nums))

''' Count Inversions '''
# class Solution:
#     def numberOfInversions(self, nums):
#         n = len(nums)
#         cnt=0
#         for i in range(n):
#             for j in range(i+1, n):
#                 if nums[i]>nums[j] and i<j:
#                     cnt+=1
#         return cnt


# nums =   [-10, -5, 6, 11, 15, 17]
# c1=  Solution()
# print(c1.numberOfInversions(nums))



'''Find the repeating and missing number'''

# class Solution:
#     def findMissingRepeatingNumbers(self, nums):
#         n = len(nums)
#         dct = {}
#         dupli_number = 0
#         nums.sort()
#         for i in range(n-1):
#             if nums[i]==nums[i+1]:
#                 dupli_number = nums[i]
#         total = (n*(n+1)//2)
#         given_lst_sum = sum(nums)
#         actual = given_lst_sum-dupli_number
#         return [dupli_number, total - actual]


# nums = [3, 5, 4, 1, 1]
# c1 = Solution()
# print(c1.findMissingRepeatingNumbers(nums))

# class Solution:
#     def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
#         """
#         Do not return anything, modify nums1 in-place instead.
#         """
#         result =[]
#         left = 0
#         right = 0
#         while left<m and right<n:
#             if nums1[left]<=nums2[right]:
#                 result.append(nums1[left])
#                 left+=1
#             else:
#                 result.append(nums2[right])
#                 right+=1

#         while left<m:
#             result.append(nums1[left])
#             left+=1
#         while right<n:
#             result.append(nums2[right])
#             right+=1
#         nums1[:] = result
#         return nums1


# nums1 = [1,2,3,0,0,0] 
# m = 3 
# nums2 = [2,5,6] 
# n = 3
# c1 = Solution()
# print(c1.merge(nums1, m, nums2, n))






'''Merge Intervals'''


# class Solution:
#     def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
#         if not intervals:
#             return []
        
#         intervals.sort()

#         result = [intervals[0]]

#         for i in range(1, len(intervals)):
#             curr_interval = result[-1]   ## Pick from result
#             next_interval = intervals[i]  ## pick from given internal list of list
#             if curr_interval[1]>=next_interval[0]:
#                 curr_interval[1] = max(curr_interval[1], next_interval[1])  ## Updating the 1st index of list taken from result (a short of merging overlapping number)
#             else:
#                 result.append(next_interval)  ## Here mean we found a new interval
#         return result

# intervals = [[1,3],[2,6],[8,10],[15,18]]
# c1 = Solution()
# print
# print(c1.merge(intervals))







'''
Count subarrays with given xor K
# '''

# class Solution:
#     def subarraysWithXorK(self, nums, k):
#         n = len(nums)
#         cnt = 0
#         for i in range(n):
#             temp = nums[i]
#             if temp == k:
#                 cnt+=1
#             for j in range(i+1,n):
#                 temp = temp^nums[j]
#                 if temp == k:
#                     cnt+=1
#         return cnt


# nums = [4, 2, 2, 6, 4] 
# k = 6
# c1 = Solution()
# print(c1.subarraysWithXorK(nums, k))


'''Largest Subarray with Sum 0'''

# class Solution:
#     def maxLen(self, arr):
#         max_cnt = 0
#         n = len(arr)
#         for i in range(n):
#             curr_sum = arr[i]
#             cnt = 1
#             for j in range(i+1, n):
#                 curr_sum+= arr[j]
#                 cnt+=1
#                 # print(curr_sum)
#                 if curr_sum == 0 and cnt>max_cnt:
#                     max_cnt = cnt
#         return max_cnt


# arr = [2, 10, 4]
# c1 = Solution()
# print(c1.maxLen(arr))

'''3Sum'''

# class Solution:
#     def threeSum(self, nums: list[int]) -> list[list[int]]:




# nums = [-1,0,1,2,-1,-4]
# c1 = Solution()
# print(c1.threeSum(nums))



'''229. Majority Element II'''

# class Solution:
#     def majorityElement(self, nums: List[int]) -> List[int]:
#         n = len(nums)
#         n_3rd = n//2

#         dct = {}
#         for i in nums:
#             dct[i] = dct.get(i, 0)+1
#         result = []
#         for i,j in dct.items():
#             if j>n_3rd:
#                 result.append(i)
#         return result


# nums = [3,2,3]
# c1  = Solution()
# print(c1.majorityElement(nums))



'''https://leetcode.com/problems/pascals-triangle/description/'''

# class Solution:
#     def generate(self, numRows: int) -> List[List[int]]:
#         final_output = []
#         for i in range(numRows):
#             row = [1]*(i+1)  
#             if i>=2:
#                 prev = final_output[i-1]
#                 for j in range(1, i):
#                     row[j] = prev[j-1] + prev[j]
            
#             final_output.append(row)  ## for [1]& [1,1] means for 0 and 1 list will get appended in final_output
#         return final_output



# numRows = 5
# c1 = Solution()
# print(c1.generate(numRows))