# ## Pyramid

class Solution:
    def pattern2(self, n): 
        alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        count=n
        for i in range(1, n+1):
            count = n-i
            for j in range(1, i+1):
                print(alpha[count], end=" ")
                count+=1
            print()
            count = n

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
