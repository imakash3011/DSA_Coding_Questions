'''
Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:

12345
1234
123
12
1
'''

################## BRUTE FORCE #################
class Solution:
    def pattern6(self, n):
        for i in range(n, 0, -1):
            for j in range(1, i+1):
                print(j, end="")
            print()

# c1 = Solution()
# c1.pattern6(4)



################## ANOTHER APPROACH #################

class Solution:
    def pattern6(self, n):
        for i in range(n,0,-1):
            print(" ".join(str(j) for j in range(1, i+1)))

# c1 = Solution()
# c1.pattern6(4)


################## ANOTHER APPROACH #################

class Solution:
    def pattern6(self, n):
        base_string = "".join(str(i) for i in range(1, n+1))
        # print(base_string)
        for i in range(n,0,-1):
            print(base_string[:i])   ## Still time complexity will be O(n^2) because of slicing and joining

c1 = Solution()
c1.pattern6(4)






















