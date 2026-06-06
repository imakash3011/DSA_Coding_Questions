''' '''


class Solution:
    def findPages(self, nums, m):
        # Base condition: if students are more than books, it's impossible.
        if m > len(nums):
            return -1
        
        def max_pages_assigned(nums, max_pages_allowed):
            pages_student_has = 0
            students = 1
            for i in range(len(nums)):
                if pages_student_has + nums[i] <= max_pages_allowed:
                    pages_student_has += nums[i]
                else:
                    students += 1
                    pages_student_has = nums[i]
            
            return students

        # 1. Correct Search Space
        low = max(nums)
        high = sum(nums)
        while low<=high:
            mid = (low+high)//2
            students_needed = max_pages_assigned(nums, mid)
            if students_needed > m:  # DON'T COMPARE WITH MID ----- If we need more students than 'm', our max_pages_allowed is too low
                low = mid+1
            else:
                high = mid-1
        return low
       
nums = [12, 34, 67, 90]
m=2
c1 = Solution()
print(c1.findPages(nums,m))