'''
Given an integer n. You need to recreate the pattern given below for any value of N. Let's say for N = 5, the pattern should look like as below:

1 
2 3 
4 5 6 
7 8 9 10 
11 12 13 14 15
'''

################### BRUTE FORCE #######################

class Solution:
    def pattern2(self, n): 
        count=1
        for i in range(1, n+1):
            for j in range(1, i+1):
                print(count, end=" ")
                count+=1
            print()

# c1 = Solution()
# c1.pattern2(4)


################## OPTIMAL APPROACH ######################

class Solution:
    def pattern2(self, n):
        row = 1
        target = 1  # The last number of the current row
        
        # Calculate the absolute last number we need to print
        total_numbers = (n * (n + 1)) // 2
        # print(total_numbers)
        
        for count in range(1, total_numbers + 1):
            print(count, end=" ")
            
            # If we hit the target end of the row, jump to the next line
            if count == target:
                print()
                row += 1
                target = (row * (row + 1)) // 2

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
