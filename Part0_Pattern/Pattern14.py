'''
Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:
A
AB
ABC
ABCD
ABCDE
'''
#################### BRUTE FORCE #####################
class Solution:
    def pattern2(self, n): 
        alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        count=0
        for i in range(1, n+1):
            for j in range(1, i+1):
                print(alpha[count], end=" ")
                count+=1
            print()
            count = 0

# c1 = Solution()
# c1.pattern2(4)


# class Solution:
#     def pattern2(self, n): 
#         alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#         for i in range(n+1):
#             print(" ".join(str(alpha[j]) for j in range(i)))

# c1 = Solution()
# c1.pattern2(4)


#################### OPTIMAL APPROACH #####################

class Solution:
    def pattern2(self, n): 
        alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        for i in range(n+1):
            print(" ".join(str(alpha[:i])))

c1 = Solution()
c1.pattern2(4)

