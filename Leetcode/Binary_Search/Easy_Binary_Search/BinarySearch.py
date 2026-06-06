class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        left = 0
        right = n-1
        if n==1 and nums[0]==target:
            return 0
        while left<=right:
            mid = (left+right)//2
            if nums[mid] == target:
                return mid
            if nums[mid]< target:
                left=mid+1
            else:
                right= mid-1
        return -1
            

c1 = Solution()
nums = [5]
target = 5
print(c1.search(nums, target))