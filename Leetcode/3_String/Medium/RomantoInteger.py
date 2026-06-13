'''https://leetcode.com/problems/roman-to-integer/description/'''


class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        result = 0
        n = len(s)
        for i in range(n-1):
            curr_val = roman[s[i]]
            next_val = roman[s[i+1]]
            if curr_val<next_val:
                result -= curr_val
            else:
                result += curr_val
        result+= roman[s[-1]]
        
        return result



s ="III"
c1 = Solution()
print(c1.romanToInt(s))