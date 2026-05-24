class Solution:
    def pattern2(self, n): 
        alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        
        for i in range(1, n + 1):
            # 1. Print leading spaces to center the pyramid
            print("  " * (n - i), end="")
            char_index = 0
            
            # 3. Inner loop runs for the total characters in the row (1 to 2*i - 1)
            for j in range(1, 2 * i):
                print(alpha[char_index], end=" ") 
                # If we haven't reached the midpoint (i), increase the letter index
                if j < i:
                    char_index += 1
                # Once we pass the midpoint, start reversing the letter index
                else:
                    char_index -= 1
            print()

c1 = Solution()
c1.pattern2(4)