'''
Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:

*****
****
***
**
*
'''

############### BRUTE FORCE ####################
class Solution:
    def pattern5(self, n):
        for i in range(n, -1, -1):
            for j in range(i):
                print("*", end="")
            print()

# c1 = Solution()
# c1.pattern5(4)


############### OPTIMAL APPROACH ####################

class Solution:
    def pattern5(self, n):
        for i in range(n,0,-1):
            print("*"*i)
c2 = Solution()
c2.pattern5(4)
