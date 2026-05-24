'''
Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:
1
22
333
4444
55555
'''

########### BRUTE FORCE ############

class Solution:
    def pattern4(self, n):
        for i in range(1, n+1):
            for j in range(i):
                print(i, end="")
            print()

# c1 = Solution()
# c1.pattern4(4)


########### OPTIMAL FORCE ############

class Solution:
    def pattern4(self, n):
        temp = 1
        val = 1
        for _ in range(1, n+1):
            print(str(val)*temp)
            val+=1
            temp+=1
c2 = Solution()
c2.pattern4(4)

