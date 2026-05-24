'''
Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:
*
**
***
****
*****
'''

################### BRUTE FORCE #################
class Solution:
    def pattern2(self, n):
        for i in range(n):
            for _ in range(i+1):
                print("*", end="")
            print()

# c1 = Solution()
# c1.pattern2(4)



################### OPTIMAL Approach #################

class Solution:
    def pattern2(self, n):
        count = 1
        for _ in range(n):
            print("*"*count)
            count+=1

c2 = Solution()
c2.pattern2(4)