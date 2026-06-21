'''https://leetcode.com/problems/divide-two-integers/'''


# class Solution:

#     def divide(self, dividend: int, divisor: int) -> int:
#         MAX_INT = 2**31 - 1
#         MIN_INT = -(2**31)

#         if dividend == MIN_INT and divisor == -1:
#             return MAX_INT

#         sign = 1
#         if divisor < 0:
#             sign *= -1
#             divisor = abs(divisor)
#         if dividend < 0:
#             sign *= -1
#             dividend = abs(dividend)

#         # We will keep track of total count here
#         total_cnt = 0

#         # YOUR MAIN LOGIC: Keep going while divisor fits into what's left of the dividend
#         while divisor <= dividend:
#             res = divisor
#             cnt = 1

#             # UPGRADE: Instead of adding just 'divisor', we double our addition
#             # as long as it still fits inside the dividend!
#             while (res + res) <= dividend:
#                 res += res  # Double the current added amount
#                 cnt += cnt  # Double the count matching it

#             # Subtract what we successfully accumulated from the dividend
#             dividend -= res
#             # Add the count we accumulated to our total count
#             total_cnt += cnt

#         return sign * total_cnt


########################## STILL SOME PROBLEM WITH BIGGER NUMBER
# class Solution:
#     def divide(self, dividend: int, divisor: int) -> int:
#         # Fix 1: Correct the power operator syntax
#         MAX_INT = 2**31 - 1
#         MIN_INT = -(2**31)

#         # Fix 2: Handle the specific 32-bit overflow case up front
#         if dividend == MIN_INT and divisor == -1:
#             return MAX_INT

#         res, cnt = 0, 0
#         sign = 1

#         if divisor < 0:
#             sign = sign * (-1)
#             divisor = abs(divisor)
#         if dividend < 0:
#             sign = sign * (-1)
#             dividend = abs(dividend)

#         # YOUR LOGIC: Add divisor step-by-step
#         while (res + divisor) <= dividend:
#             res += divisor
#             cnt += 1

#         return sign * cnt
    

############### TOPTIMAL BIT MANIPULATION SOLUTION ################
class Solution:

    def divide(self, dividend: int, divisor: int) -> int:
        MAX_INT = 2**31 - 1
        MIN_INT = -(2**31)

        if dividend == divisor:
            return 1

        # Handle the specific overflow rule required by LeetCode up front
        if dividend == MIN_INT and divisor == -1:
            return MAX_INT

        sign = True
        if dividend < 0 and divisor >= 0:
            sign = False
        if dividend >= 0 and divisor < 0:
            sign = False

        dividend = abs(dividend)
        divisor = abs(divisor)

        final_count = 0
        while dividend >= divisor:
            cnt = 0
            # FIX 1: Shift 'divisor', not 'dividend'. Use explicit brackets.
            while dividend >= (divisor << (cnt + 1)):
                cnt += 1

            final_count += 1 << cnt
            # FIX 2: Optimized from (divisor * (1 << cnt)) to just bitwise shifting
            dividend = dividend - (divisor << cnt)

        # Handle 32-bit boundary clamps
        if final_count >= MAX_INT and sign == True:
            return MAX_INT
        if final_count >= 2**31 and sign == False:  # Clean negative overflow check
            return MIN_INT

        # FIX 3: Apply the negative sign if our sign flag is False
        return final_count if sign else -final_count



dividend = 7
divisor = -3
c1 = Solution()
print(c1.divide(dividend, divisor))