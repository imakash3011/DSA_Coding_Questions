# ## Pyramid

class Solution:
    def pattern2(self, n): 

        for i in range(1, n+1):
            for j in range(1, i+1):
                print("*", end=" ")

            print("    "*(n-i), end="")

            for j in range(1, i+1):
                print("*", end=" ")
            print()
    

        temp = n
        for i in range(1, n+1):
            for j in range(n-i,-1,-1):
                print("*", end=" ")

            print("    "*(n-temp), end="")
            for j in range(n-i,-1,-1):
                print("*", end=" ")
            temp-=1
            
            print()

            # print("__________")

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
