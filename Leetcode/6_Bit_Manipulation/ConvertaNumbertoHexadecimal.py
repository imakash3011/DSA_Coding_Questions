'''https://leetcode.com/problems/convert-a-number-to-hexadecimal/description/?envType=problem-list-v2&envId=bit-manipulation'''


class Solution:
    def toHex(self, num: int) -> str:
        if num ==0:
            return '0'

        digits = "0123456789abcdef"
        # Convert to a 32-bit unsigned integer to handle negative numbers automatically
        num = num & 0xFFFFFFFF
        res = []
        while num:
            res.append(digits[num % 16])  ## first time  10 means a and then 1 means 1
            num //= 16
        return ''.join(res[::-1])

num = -1
c1 = Solution()
print(c1.toHex(num))

