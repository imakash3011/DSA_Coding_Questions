'''https://leetcode.com/problems/single-number-iii/description/?envType=problem-list-v2&envId=bit-manipulation'''


class Solution:

    def singleNumber(self, nums: list[int]) -> list[int]:
        # Step 1: XOR all numbers. The result will be (first_unique ^ second_unique)
        xor_all = 0
        for num in nums:
            xor_all ^= num

        # Step 2: Find the lowest set bit (the rightmost '1' bit)
        # This bit acts as our dividing line because the two unique numbers differ here.
        diff_bit = xor_all & -xor_all

        # Step 3: Divide the numbers into two groups and XOR them separately
        num1 = 0
        num2 = 0

        for num in nums:
            # Check if the bit at the diff_bit position is set to 1
            if num & diff_bit:
                num1 ^= num  # Group 1 XOR
            else:
                num2 ^= num  # Group 2 XOR

        return [num1, num2]


# Test it with your example
nums = [1, 2, 1, 3, 2, 5]
c1 = Solution()
print(c1.singleNumber(nums))  # Output: [3, 5] (or [5, 3])