'''
Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:
*****
*****
*****
*****
*****
'''

####### Brute Force #######
class Solution:
    def pattern1(self, n):
        for i in range(n):
            for j in range(n):
                print("*", end="")
            print()

# c1 = Solution()
# c1.pattern1(4)

####### Optimal Approach #######

class Solution:
    def pattern1(self, n):
        row = "*"*n
        for _ in range(n):
            print(row)
        # print()  ## Not required because in above line we're not using " end='' "
c2 = Solution()
c2.pattern1(4)