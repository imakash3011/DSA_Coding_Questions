'''https://leetcode.com/problems/single-number-ii/description/?envType=problem-list-v2&envId=bit-manipulation'''


class Solution:

    def singleNumber(self, nums: list[int]) -> int:
        ones = 0
        twos = 0
        for num in nums:
            # 'ones' will hold bits that appear odd times, but not 3 times
            ones = (ones ^ num) & ~twos

            # 'twos' will hold bits that appear even times (specifically twice)
            twos = (twos ^ num) & ~ones

        return ones


nums = [30000, 500, 100, 30000, 100, 30000, 100]
c1 = Solution()
print(c1.singleNumber(nums))  # Output: 500


'''
Approach
We use two variables, ones and twos.

ones: Holds bits that have appeared exactly once (modulo 3).
twos: Holds bits that have appeared exactly twice (modulo 3).
For each number num in the array:

Update ones: We XOR num into ones. However, if a bit is already in twos, it means this is the 3rd time we see it, so we shouldn't add it to ones. We use (num & ~twos) to ensure we only process bits not currently in twos.
Update twos: We XOR num into twos. Similarly, if a bit is now in ones (after the update above), it means it has appeared once, so it can't be in twos. We use (num & ~ones) to filter this.
'''