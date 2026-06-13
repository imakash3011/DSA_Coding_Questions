'''https://leetcode.com/problems/largest-odd-number-in-string/'''

###################### OPTIMAL APPROACH ##################
class Solution:
    def largestOddNumber(self, num: str) -> str:
        for i in range(len(num)-1, -1, -1):
            if num[i] in {'1','3', '5', '7', '9' }:
                return num[:i+1]
        return ""


num ="35427"
c1 = Solution()
print(c1.largestOddNumber(num))

############# BRUTE FORCE ######################
class Solution:
    def largestOddNumber(self, num: str) -> str:
        val = int(num)
        while val>0:
            if val%2!=0:
                return str(val)
            val = val//10
        return ""
        
# num ="35427"
# c1 = Solution()
# print(c1.largestOddNumber(num))