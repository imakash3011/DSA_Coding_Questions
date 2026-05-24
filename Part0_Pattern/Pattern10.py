'''
Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:
*
**
***
****
*****
****
***
**
*
'''

############### BRUTE FORCE APPROACH #####################
class Solution:
    def pattern2(self, n):
        for i in range(n):
            # print(" "*(n-i-1), end="")   ## remember this line to print extra space in different line
            for j in range(2*i+1):
                print("*", end="")
            print()
        n = n-1
        for i in range(n-1,-1,-1):
            # print(" "*(n-i-1), end="")   ## remember this line to print extra space in different line
            for j in range(2*i+1):
                print("*", end="")
            print()

# c1 = Solution()
# c1.pattern2(7)



############### OPTIMAL APPROACH #####################

class Solution:
    def pattern2(self, n):
        for i in range(n+1):
            print("*"*i)
        for i in range(n, -1, -1):
            print("*"*i)

c1 = Solution()
c1.pattern2(4)