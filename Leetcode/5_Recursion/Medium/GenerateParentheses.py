'''https://leetcode.com/problems/generate-parentheses/'''


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result =[]
        def helper_func(open_idx, close_idx, parenthesis):

            if open_idx==n and close_idx == n:
                result.append(parenthesis)
                return
            if open_idx<n:
                helper_func(open_idx+1,close_idx, parenthesis+"(")

            if close_idx<open_idx:
                helper_func(open_idx, close_idx+1, parenthesis + ")")
        
        helper_func(0,0, "")
        return result



n = 3
c1 = Solution()
print(c1.generateParenthesis(n))

# ["((()))","(()())","(())()","()(())","()()()"]
        