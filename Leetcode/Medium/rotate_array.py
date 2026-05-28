'''
https://leetcode.com/problems/rotate-array/description/
'''

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k = k%n

        left = nums[:-k]
        right = nums[-k:]
        nums[:] = right+left
        # print(left, right)
        return nums


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k %= n
        for _ in range(k):
            last = nums.pop()
            nums.insert(0, last)
        return nums


nums = [1,2,3,4,5,6,7]
k = 3
c1 = Solution()
print(c1.rotate(nums,k))
