'''
Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:

*********
 *******
  *****
   ***
    *
'''

##################### BRUTE FORCE #######################
class Solution:
    def pattern8(self, n):
        for i in range(n-1,-1, -1):
            print(" "*(n-i-1), end="")   ## remember this line to print extra space in different line
            for j in range(2*i+1):
                print("*", end="")
            print()

# c1 = Solution()
# c1.pattern8(4)

##################### OPTIMAL APPROACH #######################

class Solution:
    def pattern8(self, n):
        for i in range(n-1,-1,-1):
            count = 2*i+1
            print(" "*(n-i-1)+"*"*count)
c1 = Solution()
c1.pattern8(4)
        