'''
https://leetcode.com/problems/reverse-integer/submissions/2011575814/
'''


class Solution:
    def reverse(self, x: int) -> int:
        MAX_INT32 = 2**31 - 1   # 2147483647
        MIN_INT32 = -2**31      # -2147483648
        
        # Determine the sign upfront
        sign = -1 if x < 0 else 1
        copy_x = abs(x)
        result = 0
        
        while copy_x > 0:
            rem = copy_x % 10
            copy_x = copy_x // 10
            
            # --- CRITICAL ENVIRONMENT CHECK ---
            # Before doing result * 10, check if it will overflow the positive or negative boundaries
            if sign == 1:
                # If result is already greater than MAX_INT32 // 10, multiplying by 10 will overflow.
                # If it's exactly equal, checking if the remainder is greater than 7 (the last digit of 2147483647).
                if result > MAX_INT32 // 10 or (result == MAX_INT32 // 10 and rem > 7):
                    return 0
            else:
                # For negative numbers, we track the absolute limit (using absolute of MIN_INT32 // 10)
                # The last digit of -2147483648 is 8.
                if result > abs(MIN_INT32) // 10 or (result == abs(MIN_INT32) // 10 and rem > 8):
                    return 0
            
            # Safe to perform the calculation now
            result = result * 10 + rem
            
        return sign * result
    
# c1 = Solution()
# print(c1.reverse(-123))


class Solution:
    def reverse_num(self, n):
        min_int32 = -2**31
        max_int32 = 2**31-1
        sign = -1 if n<0 else 1
        rev_num = int(str(abs(n))[::-1])*sign
        if rev_num>max_int32 or rev_num<min_int32:
            return 0
        return rev_num

c1 = Solution()
print(c1.reverse_num(9646324351))
