'''https://leetcode.com/problems/string-to-integer-atoi/description/'''

class Solution:
    def myAtoi(self, s: str) -> int:
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        
        i = 0
        n = len(s)
        
        # 1. Skip leading whitespaces ONLY
        while i < n and s[i] == ' ':
            i += 1
            
        # If we reached the end of the string, return 0
        if i == n:
            return 0
            
        # 2. Check for a single sign
        sign = 1
        if s[i] == '-':
            sign = -1
            i += 1
        elif s[i] == '+':
            i += 1
            
        # 3. Read digits sequentially
        res = 0
        while i < n and s[i].isdigit():
            res = res * 10 + int(s[i])
            i += 1
            
        # 4. Apply sign and clamp to 32-bit integer range
        res *= sign
        
        if res > INT_MAX:
            return INT_MAX
        if res < INT_MIN:
            return INT_MIN
            
        return res
    
s ="+-1"
c1 = Solution()
print(c1.myAtoi(s))