'''
Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:
1
12
123
1234
12345
'''

########### BRUTE FORCE ################
class Solution:
    def pattern3(self, n):
        for i in range(n):
            for j in range(1, i+1+1):
                print(j, end="")
            print()

# c1 = Solution()
# c1.pattern3(4)

################## OPTIMAL APPROACH ###############

class Solution:
    def pattern3(self, n):
        temp = 1
        val = 0
        for _ in range(n):
            print(val*10 + temp)
            val = val*10 + temp
            temp+=1
            
c2 = Solution()
c2.pattern3(4)


