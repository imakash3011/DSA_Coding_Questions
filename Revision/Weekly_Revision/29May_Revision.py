''' https://takeuforward.org/plus/dsa/problems/pattern-9?source=strivers-a2z-dsa-track '''

class Solution:
    def pattern9(self, n):
            for i in range(n):
                print(" "*(n-i),"*"*(2*i+1) )
            for i in range(n, -1, -1):
                print(" "*(n-i),"*"*(2*i+1) )
c1 = Solution()
c1.pattern9(5)




# *****************************  PATTREN 7 *************************************
''' https://takeuforward.org/plus/dsa/problems/pattern-8?source=strivers-a2z-dsa-track '''
# class Solution:
#     def pattern7(self, n):
#         for i in range(n,0,-1):
#             print(" "*(n-i),end=" ")
#             for j in range(i):
#                 print("*", end=" ")
#             print()

# class Solution:
#     def pattern7(self, n):
#         for i in range(n, -1, -1):
#             print(" "*(n-i),"*"*(2*i+1) )

# c1 = Solution()
# c1.pattern7(5)

# *****************************  PATTREN 5 *************************************
'''https://takeuforward.org/plus/dsa/problems/pattern-7?source=strivers-a2z-dsa-track'''

# class Solution:
#     def pattern7(self, n):
#         for i in range(n):
#             print("  "*(n-i), end=" ")
#             for j in range(2*i+1):
#                 print("*",end=" ")
#             print()


# class Solution:
#     def pattern7(self, n):
#         temp = 0
#         for i in range(n):
#             temp = 2*i+1
#             print(" "*(n-i),"*"*temp)
            


# c1 = Solution()
# c1.pattern7(5)


# *****************************  PATTREN 5 *************************************

'''https://takeuforward.org/plus/dsa/problems/pattern-6?source=strivers-a2z-dsa-track'''

# class Solution:
#     def pattern6(self, n):
#         for i in range(n,0, -1):
#             for j in range(1,i+1):
#                 print(j,end=" ")
#             print()

# c1 = Solution()
# c1.pattern6(5)


# *****************************  PATTREN 5 *************************************
'''https://takeuforward.org/plus/dsa/problems/pattern-5?source=strivers-a2z-dsa-track'''
# class Solution:
#     def pattern5(self, n):
#         for i in range(n,0,-1):
#             print("*"*i)


# class Solution:
#     def pattern5(self, n):
#         for i in range(n,0,-1):
#             for j in range(i):
#                 print("*", end=" ")
#             print()

# c1 = Solution()
# c1.pattern5(5)


# *****************************  PATTREN 4 *************************************

'''https://takeuforward.org/plus/dsa/problems/pattern-4?source=strivers-a2z-dsa-track'''

# class Solution:
#     def pattern4(self, n):
#         for i in range(n):
#             for j in range(i):
#                 print(i,end=" ")
#             print()


# class Solution:
#     def pattern4(self, n):
#         for i in range(n):
#             print(str(i)*i)
# c1 = Solution()
# c1.pattern4(5)



# *****************************  PATTREN 3 *************************************
''' https://takeuforward.org/plus/dsa/problems/pattern-3?source=strivers-a2z-dsa-track '''


################### BRUTE FORCE #################
# class Solution:
#     def pattern3(self, n):
#         for i in range(1,n+1):
#             for j in range(1, i+1):
#                 print(j, end=" ")
# #             print()


# ################### OPTIMAL #################
# class Solution:
#     def pattern3(self, n):
#         res = 1
#         val = 0
#         for i in range(n):
#             val = val*10+res
#             res+=1
#             print(val)
        

# c1 = Solution()
# c1.pattern3(5)




# *****************************  PATTREN 2 *************************************

# '''
# # Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:
# # *
# # **
# # ***
# # ****
# # *****
# # '''

# ################### OPTIMAL FORCE #################
# class Solution:
#     def pattern2(self, n):
#         for i in range(1,n+1):
#             print("*"*i)

# c1 = Solution()
# c1.pattern2(4)



# '''
# Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:

# *****
# *****
# *****
# *****
# *****
# '''

# #########################  BRUTE FORCE

# class Solution:
#     def pattern1(self, n):
#         for i in range(n):
#             for j in range(n):
#                 print("*", end=" ")
#             print()

# n = 5
# c1 = Solution()
# c1.pattern1(n)

# ######################### OPTIMAL-FORCE
# class Solution:
#     def pattern1(self, n):
#         row = "*"*n
#         for i in range(n):
#             print(row)
#         print()

# # n = 5
# # c1 = Solution()
# # c1.pattern1(n)




# 