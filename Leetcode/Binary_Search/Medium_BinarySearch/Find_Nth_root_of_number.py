'''
https://takeuforward.org/plus/dsa/problems/find-nth-root-of-a-number?source=strivers-a2z-dsa-track
'''

################# BINARY SEARCH ##############
# If you find a whole number that fits perfectly, return that number.
# If no whole number fits perfectly (the real answer is a decimal), return -1.


class Solution:
    def NthRoot(self, n, m):
        left = 1
        right = m
        while left<=right:
            mid = (left+right)//2
            if mid**n == m:
                return mid
            if mid**n>m:
                right=mid-1
            else:
                left = mid+1
        return -1


N = 4
M = 69
c1 = Solution()
print(c1.NthRoot(N, M))  # Output: 3

################# LINEAR #####################

class Solution:
    def NthRoot(self, n, m):
        for i in range(1, m + 1):
            # Calculate i raised to the power of n
            temp = i ** n 
            
            if temp == m:
                return i  # Return the base 'i', not the exponent
            elif temp > m:
                break     # Stop early if the power exceeds m
        return -1

# N = 3
# M = 27
# c1 = Solution()
# print(c1.NthRoot(N, M))  # Output: 3




################# IN BUILT #####################
class Solution:
    def NthRoot(self, n, m):
        val = int(pow(m,1/n))
        return val
      

# N = 3
# M = 27
# c1 = Solution()
# print(c1.NthRoot(N,M))