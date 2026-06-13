'''https://takeuforward.org/data-structure/remove-outermost-parentheses'''

class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        new_s = []
        cnt = 0
        for char in s:
            if char=='(':
                if cnt>0:
                    new_s.append(char)
                cnt+=1
            elif char == ')':
                cnt-=1
                if cnt>0:
                    new_s.append(char)
        return "".join(new_s)

s =   "(()())(())"
c1 = Solution()
print(c1.removeOuterParentheses(s))