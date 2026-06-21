'''https://leetcode.com/problems/powx-n/description/'''


################ RECURSION ####################
class Solution:
    def myPow(self, x: float, n: int) -> float:
        # Helper function to compute positive powers efficiently
        def power_x_n(base, power):
            if power==0:
                return 1.0
            # If power is even, square the base and halve the power
            if power%2==0:
                # print(base, power)
                return power_x_n(base*base, power//2)
            # If power is odd, pull one base out and decrement the power by 1
            else:
                return base*power_x_n(base, power-1)
        
        # Handle the negative exponent edge case at the top level
        abs_n = abs(n)
        ans = power_x_n(x, abs_n)
        if n<0:
            return 1.0/ans
        return ans


x = 2.00000 
n = 10
c1 = Solution()
print(c1.myPow(x,n))

################### BRUTEFORCE ################
class Solution:
    def myPow(self, x: float, n: int) -> float:
        # Handle the base case where power is 0
        if n == 0:
            return 1.0
            
        ans = 1.0
        # Use absolute value to loop safely for negative powers
        abs_n = abs(n)
        
        for _ in range(abs_n):
            ans *= x
            
        # If the original power was negative, invert the answer
        if n < 0:
            return 1.0 / ans
            
        return ans

# x = 2.00000 
# n = -2
# c1 = Solution()
# print(c1.myPow(x,n))






