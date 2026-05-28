class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        res = 0
        n = len(nums)
        for i in range(n):
            if nums[i]!=0:
                nums[res] = nums[i]
                res+=1
        
        for i in range(res,n):
            nums[i] = 0
        return nums
    

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        left = 0

        for right in range(len(nums)):
            if nums[right] != 0:
                nums[right], nums[left] = nums[left], nums[right]
                left += 1
        
        return nums


nums = [0]
c1 = Solution()
print(c1.moveZeroes(nums))


