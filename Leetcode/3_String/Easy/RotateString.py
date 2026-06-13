'''https://leetcode.com/problems/rotate-string/'''


'''
For example, if s = "abcde" and goal = "cdeab":
s + s = "abcdeabcde"
You can clearly see "cdeab" sitting right inside it: "ab[cdeab]cde".
'''

class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        # A rotated string must be the exact same length
        if len(s) != len(goal):
            return False
            
        # Check if goal is a substring of s + s
        return goal in (s + s)
    
c1 = Solution()
s = "abcde" 
goal = "cdeab"
print(c1.rotateString(s, goal))

############### BRUTE FORCE ##################
class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        if len(s)!= len(goal):
            return False

        for _ in range(len(s)):
            if s==goal:
                return True
            s = s[1:] + s[0]
        return False

# c1 = Solution()
# s = "abcde" 
# goal = "cdeab"
# print(c1.rotateString(s, goal))