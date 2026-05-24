'''
Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:
1 
0 1 
1 0 1 
0 1 0 1 
1 0 1 0 1
'''

################ BRUTE FORCE #############
class Solution:
    def pattern2(self, n):
        for i in range(n+1):
            for j in range(i):
                if (i+j)%2==0:
                    print(0, end="")
                else:
                    print(1, end="")
            print()

# c1 = Solution()
# c1.pattern2(4)


################ OPTIMAL FORCE #############

class Solution:
    def pattern2(self, n):
        for i in range(n+1):
            print(" ".join(str((i+j)%2) for j in range(i)))

c1 = Solution()
c1.pattern2(4)











# flag = False
# for i in range(1, 13):
#     for j in range(i):
#         if i%2==0:
#             flag = True
#         else:
#             flag = False

#         if flag == True:
#             if j%2==0:
#                 print(1, end=" ")
#             else:
#                 print(0, end=" ")
#         else:
#             if j%2==0:
#                 print(0, end=" ")
#             else:
#                 print(1, end=" ")
#     print()


# for i in range(1, 13):
#     for j in range(i):
#         # The pattern naturally flips based on whether (i + j) is even or odd
#         if (i + j) % 2 == 0:
#             print(1, end=" ")
#         else:
#             print(0, end=" ")
#     print()


# for i in range(1, 13):
#     # If (i + j) is even, it prints 1. If odd, it prints 0.
#     # (We use i + j + 1 to make sure even rows start with 1)
#     print(" ".join(str((i + j + 1) % 2) for j in range(i)))

# class Solution:
#     def pattern2(self, n):
#         for i in range(n-1, -1, -1):
#             # Calculate and print spaces and stars all at once
#             print(" " * (n - i - 1) + "*" * (2 * i + 1))

# c1 = Solution()
# c1.pattern2(4)