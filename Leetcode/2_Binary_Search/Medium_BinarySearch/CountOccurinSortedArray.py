'''
https://takeuforward.org/plus/dsa/problems/count-occurrences-in-a-sorted-array?source=strivers-a2z-dsa-track
'''

''' Use the same logic as First_last_position question logic and just subtract second-first from that logic to get answer'''

class Solution:
    def find_first_last(self, nums: List[int], target: int) -> List[int]:
        def search(find_first):
            n = len(nums)
            left, right =0, n-1
            ans = -1  
            while left<=right:
                mid = (left+right)//2
                if nums[mid]>target:
                    right = mid-1
                elif nums[mid]<target:
                    left= mid+1
                else:
                    ans = mid        # We found the target!
                    if find_first:   # Keep searching to the left
                        right = mid-1
                    else:            # Keep searching to the right
                        left = mid+1
            return ans

        first = search(True)  # 1. Find the first occurrence
        if first == -1:       # 2. If it's not found, return early
            return 0
        elif first == search(False):
            return first
        else:
            result = search(False)-first +1
        # 3. Find the last occurrence and return both
        return result
    
c1 = Solution()
nums =  [1,2,3,3,3,3,3,4,4,5,6]
x = 6
print(c1.find_first_last(nums, x))


##################### BUlky Answer ###################
class Solution:
    def find_first_last(self, nums: List[int], target: int) -> List[int]:
        # 1. Early exit for empty array
        if not nums:
            return [-1, -1]
        def is_first_search(first_search, nums, target):
            n = len(nums)
            left = 0
            right = n-1
            ans = -1
            if first_search:
                while left <= right:
                    mid = (left+right)//2
                    if nums[mid]>=target:
                        ans = mid
                        right= mid-1
                    else:
                        left = mid+1
            else:
                while left <= right:
                    mid = (left+right)//2
                    if nums[mid]>target:
                        ans = mid
                        right= mid-1
                    else:
                        left = mid+1
            return ans
        first = is_first_search(True, nums, target)
        
        # 2. Validate `first` immediately. 
        # If it returned -1 (target is larger than all elements) 
        # or the element at index `first` isn't our target, it doesn't exist.
        if first == -1 or nums[first] != target:
            return [-1, -1]

        upper_bound = is_first_search(False, nums, target)
        
        # 3. Handle the `last` calculation safely
        # If upper_bound is -1, it means NO element was strictly greater than the target.
        # This implies our target goes all the way to the end of the array.
        if upper_bound == -1:
            last = len(nums) - 1
        else:
            last = upper_bound - 1
        return first, last
    

# c1 = Solution()
# nums =[5,7,7,8,8,10]
# x = 10
# print(c1.find_first_last(nums, x))
