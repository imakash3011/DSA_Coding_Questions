'''
Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:

1        1
12      21
123    321
1234  4321
1234554321
'''

################ BRUTE FORCE APPROACH ####################
class Solution:
    def pattern12(self, n):
        for i in range(1, n+1):
            for j in range(1, i+1):
                print(j, end="")

            print("  "*(n-i), end="")

            for j in range( i,0, -1):  ## here second parameter is 0 and it is exclusive and loop will stop before 0 means 1 and if kept -1 it will stop at 0 (moving in opposite direction)
                print(j, end="")
            print()

# c1 = Solution()
# c1.pattern12(4)


################ OPTIMAL APPROACH ####################

class Solution:
    def pattern12(self, n):
        count = 1
        temp = 0
        for i in range(n):
            print(temp*10 + count, end="")
            print("  "*(n-i-1), end="")
            print(str(temp*10 + count)[::-1])
            temp = temp*10 + count
            count+=1

c1 = Solution()
c1.pattern12(4)







# class Solution:
#     def pattern2(self, n):
#         for i in range(1, n+1):
#             for j in range(1, i+1):
#                 print(j, end="")

#             print("  "*(n-i), end="")

#             for j in range(1, i+1):
#                 print(j, end="")
#             print()

# c1 = Solution()
# c1.pattern2(4)
