## Array Medium Revised Today

# # Subarray Sum Equals K

# class Solution:
#     def subarraySum(self, nums: List[int], k: int) -> int:
#         current_sum = 0
#         cnt = 0
#         prefix_sums = {0:1}

#         for num in nums:
#             current_sum+=num
#             target = current_sum - k

#             if target in prefix_sums:
#                 cnt+= prefix_sums[target]
#             prefix_sums[current_sum] = prefix_sums.get(current_sum, 0)+1
#         return cnt


# nums = [1,1,1] 
# k = 2
# c1 = Solution()
# print(c1.subarraySum(nums, k))


# Spiral Matrix
# class Solution:
#     def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
#         row = len(matrix)
#         col = len(matrix[0])
#         left, top=0, 0
#         right, bottom = col-1, row-1
#         result = []
        
#         while left<=right and top<=bottom:
#             # Left to Right
#             for i in range(left, right+1):
#                 result.append(matrix[top][i])
#             top+=1
        
#             ## Top to bottom
#             for i in range(top, bottom+1):
#                 result.append(matrix[i][right])
#             right-=1

#             # Right to left
#             for i in range(right, left-1, -1):
#                 result.append(matrix[bottom][i])
#             bottom -=1

#             # bottom to top
#             for i in range(bottom, top-1, -1):
#                 result.append(matrix[i][left])
#             left+=1
        
#         return result


# matrix = [[1,2,3],[4,5,6],[7,8,9]]
# c1 = Solution()
# print(c1.spiralOrder(matrix))


## Rotate Image

# class Solution:
#     def rotate(self, matrix: List[List[int]]) -> None:
#         """
#         Do not return anything, modify matrix in-place instead.
#         """
#         row = len(matrix)
#         col = len(matrix[0])

#         for i in range(row):
#             for j in range(i+1, col):
#                 matrix[i][j], matrix[j][i] = matrix[j][i],matrix[i][j]
#         for k in range(row):
#             # print(matrix[k].reverse())
#             matrix[k].reverse()  # think matrix list of list.. here we are taking one list at a time and we reversing its number
        
#         return matrix


# matrix = [[1,2,3],[4,5,6],[7,8,9]]
# c1 = Solution()
# print(c1.rotate(matrix))



# Set Matrix Zeroes

# class Solution:
#     def setZeroes(self, matrix: List[List[int]]) -> None:
#         """
#         Do not return anything, modify matrix in-place instead.
#         """
#         row = len(matrix)
#         col = len(matrix[0])
#         new_matrix = []
#         row_lst = []
#         col_lst = []
#         for i in range(row):
#             for j in range(col):
#                 if matrix[i][j] == 0:
#                     row_lst.append(i)
#                     col_lst.append(j)

#         for i in range(row):
#             for j in range(col):
#                 if i in row_lst or j in col_lst:
#                     matrix[i][j]=0
#         return matrix


# matrix =[[1,1,1],[1,0,1],[1,1,1]]
# c1= Solution()
# print(c1.setZeroes(matrix))



# Longest Consecutive Sequence in an Array

# class Solution:
#     def longestConsecutive(self, nums: List[int]) -> int:
#         nums.sort()
#         n = len(nums)
#         max_val = 0
#         temp =1
#         for i in range(n-1):
#             if nums[i]+1 == nums[i+1]:  ## If next number is +1
#                 temp+=1
#                 max_val = max(max_val, temp) 
#             elif nums[i] == nums[i+1]: ## If next number is equal to current number
#                 continue
#             else:                ## If got any new sequence reset to one 
#                 temp = 1
#         return max_val

# nums = [0, 3, 7, 2, 5, 8, 4, 6, 0, 1]
# c1= Solution()
# print(c1.longestConsecutive(nums))


## Leaders in an Array

# class Solution:
#     def leaders(self, nums):
#         n = len(nums)
#         lst = []
#         if n==1:
#             return nums[0]
#         for i in range(n):
#             flag = True
#             for j in range(i+1,n):
#                 if nums[j]>nums[i]: 
#                     flag = False
#                     break
#             if flag == True:
#                 lst.append(nums[i])
#         return lst


# class Solution:
#     def leaders(self, nums):
#         n = len(nums)
#         lst = []
#         if n ==0:
#             return lst
        
#         max_from_right = nums[-1]
#         lst.append(max_from_right)
#         for i in range(n-2, -1, -1):
#             if nums[i]>nums[i+1]:
#                 lst.append(nums[i])
#                 max_from_right = nums[i]
        
#         return lst[::-1]

# nums =  [1, 2, 5, 3, 1, 2]
# c1 = Solution()
# print(c1.leaders(nums))



## next permutation

# class Solution:
#     def nextPermutation(self, nums: List[int]) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         n = len(nums)
#         break_point = -1
#         ## Find breakpoint
#         for i in range(n-2,-1, -1): 
#             if nums[i]<nums[i+1]:
#                 break_point = i
#                 break
#         # if no breakpoint means present in desc order then reverse array and return 
#         if break_point==-1:
#             nums.reverse()
#             return nums

#         ## find immediate next in suffix and swap with greatest element in prefix
#         for i in range(n-1,break_point,-1):
#             if nums[i]>nums[break_point]:
#                 nums[i], nums[break_point] = nums[break_point], nums[i]
#                 break
        
#         ## Reverse Suffix in nums
#         left = break_point+1
#         right = n-1
#         while left<right:
#             nums[left], nums[right] = nums[right], nums[left]

#         return nums


# nums = [3,2,1]
# c1 = Solution()
# print(c1.nextPermutation(nums))




## best time to buy stock
# class Solution:
#     def stockBuySell(self, arr, n):
#         max_profit = 0
#         min_price =float('inf')
#         for i in arr:
#             if i<min_price:
#                 min_price = i
#             if i-min_price > max_profit:
#                 max_profit = i-min_price
#         return max_profit
  

# prices =[10, 7, 5, 8, 11, 9]
# c1 = Solution()
# print(c1.stockBuySell(prices, 6))


# # Maximum Subarray

# class Solution:
#     def maxSubArray(self, nums: List[int]) -> int:
#         max_sum = 0
#         n = len(nums)
#         curr_sum = 0
#         for i in range(n):
#             curr_sum += nums[i]
#             if curr_sum>max_sum:
#                 max_sum = curr_sum
#             if curr_sum<0:
#                 curr_sum = 0
#         return max_sum



# nums =[5,4,-1,7,8]
# c1 = Solution()
# print(c1.maxSubArray(nums))




#Sort Colors

# class Solution:
#     def sortColors(self, nums: List[int]) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         # Dutch National Flag Algorithm 

#         n = len(nums)
#         low=mid =0
#         high = n-1
#         while mid<=high:
#             if nums[mid]==0:
#                 nums[low], nums[mid] = nums[mid], nums[low] 
#                 mid+=1
#                 low+=1
#             elif nums[mid]==1:
#                 mid +=1
#             else:
#                 nums[high], nums[mid] = nums[mid], nums[high]
#                 high-=1
#         return nums


# c1 = Solution()
# nums =[0,1,1,1,2,2,0,0,1]
# print(c1.sortColors(nums))


# https://leetcode.com/problems/two-sum/description/

# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         n = len(nums)
#         val_seen = {}
#         temp = 0
#         for idx, val in enumerate(nums):
#             remainder = target - val
#             if remainder in val_seen:
#                 return [val_seen[remainder], idx]  ## idx will give current index and val_seen[remainder] number has already appeared 
#             val_seen[val] = idx


# c1 = Solution()
# nums =[2,7,11,15]
# target=9
# print(c1.twoSum(nums, target))


#  https://takeuforward.org/plus/dsa/problems/longest-subarray-with-sum-k?source=strivers-a2z-dsa-track
# class Solution:
#     def longestSubarray(self, nums, k):
#         n = len(nums)
#         max_len = 0
        
#         for i in range(n):
#             temp_sum = 0
#             # Start j from i, not i+1, so we include nums[i]
#             for j in range(i, n):
#                 temp_sum += nums[j]
                
#                 # If we hit k, update max_len, but KEEP GOING (don't return)
#                 # because adding a '0' later might make the subarray longer.
#                 if temp_sum == k:
#                     max_len = max(max_len, j - i + 1)  ## This will automatically keep track of the cnt using j-i+1

#         return max_len

# c1 = Solution()
# nums = [-3, 2, 1] 
# k=6
# print(c1.longestSubarray(nums, k))


# https://leetcode.com/problems/move-zeroes/description/

# class Solution:
#     def moveZeroes(self, nums: List[int]) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         res = 0
#         n=len(nums)
#         for i in range(n):
#             if nums[i]!=0:
#                 nums[res] = nums[i]
#                 res+=1
#         for i in range(res, n):
#             nums[i] = 0
#         return nums

# nums = [0,1,0,3,12]
# c1 = Solution()
# print(c1.moveZeroes(nums))



# https://leetcode.com/problems/rotate-array/description/


# class Solution:
#     def rotate(self, nums: List[int], k: int) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         n = len(nums)
#         k = k%n
#         for i in range(k):
#             val = nums.pop()
#             nums.insert(0,val)
#         return nums

# nums = [1,2,3,4,5,6,7]
# k = 3
# c1 = Solution()
# print(c1.rotate(nums,k))


# class Solution:
#     def removeDuplicates(self, nums: List[int]) -> int:
#         n = len(nums)
#         cnt = 1  ## By default even if duplicate value present then next item will go to first index only [1,1,2] -> [1,2]
#         if not nums:
#             return 0
#         for i in range(n-1):
#             if nums[i]!=nums[i+1]:
#                 nums[cnt] = nums[i+1]
#                 cnt+=1
#         return cnt


# c1 = Solution()
# nums =[0,0,1,1,1,2,2,3,3,4]
# print(c1.removeDuplicates(nums))



# 1752. Check if Array Is Sorted and Rotated

# class Solution:
#     def check(self, nums: List[int]) -> bool:
#         n = len(nums)
#         cnt = 0
#         for i in range(n):
#             if nums[i-1]>nums[i]:  # first case -1 and 0 check this confirm whether rotated or not
#                 cnt+=1             
#         if nums[-1]>nums[0]:
#             cnt+=1
#         print(cnt)
#         return cnt<=1



# c1 = Solution()
# nums =  [1,2,3,4,5]
# print(c1.check(nums))


# Second Largest Element
# class Solution:
#     def secondLargestElement(self, nums):
#         first = second = float('-inf')
#         for i in nums:
#             if i>first:
#                 second = first
#                 first = i
#             elif i>second and i<first:
#                 second = i
#         return first, second


# c1 = Solution()
# nums =  [8, 8, 7, 6, 5]
# print(c1.secondLargestElement(nums))