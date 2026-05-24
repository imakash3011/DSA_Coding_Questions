'''
Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:

A
BB
CCC
DDDD
EEEEE
'''

#################### BRUTE FORCE APPROACH ##########################
class Solution:
    def pattern2(self, n): 
        alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        count=0
        for i in range(1, n+1):
            for j in range(1, i+1):
                print(alpha[count], end=" ")
                # count+=1
            print()
            count +=1

# c1 = Solution()
# c1.pattern2(4)


#################### OPTIMAL APPROACH ##########################

class Solution:
    def pattern2(self, n): 
        alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        count=1
        for i in range(n):
            print(" ".join(str(alpha[i]*count)))
            count+=1

c1 = Solution()
c1.pattern2(4)


