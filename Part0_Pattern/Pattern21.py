# ## Pyramid

class Solution:
    def pattern2(self, n): 

        for i in range(n):
            for j in range(n):
                if (i==0 or i==n-1) or (j==0 or j==n-1):
                    print("*",end=" ")
                else:
                    print(" ",end=" ")
            print()

c1 = Solution()
c1.pattern2(4)






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
