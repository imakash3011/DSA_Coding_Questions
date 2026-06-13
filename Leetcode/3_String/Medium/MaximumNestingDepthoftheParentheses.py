'''https://leetcode.com/problems/maximum-nesting-depth-of-the-parentheses/'''


class Solution:
    def maxDepth(self, s: str) -> int:
        cnt = 0
        max_val = 0
        for val in s:
            if val =="(":
                cnt+=1
                max_val = max(max_val, cnt)
            elif val == ")":
                cnt-=1
        return max_val
            


s = "(1)+((2))+(((3)))"
c1 = Solution()
print(c1.maxDepth(s))
        



