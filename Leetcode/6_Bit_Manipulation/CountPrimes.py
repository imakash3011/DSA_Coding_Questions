'''https://leetcode.com/problems/count-primes/'''


# class Solution:
#     def countPrimes(self, n: int) -> int:
#         if n <= 2:
#             return 0
        
#         # Create a tracker list where index represents the number.
#         # Initially, assume all numbers up to n-1 are prime.
#         is_prime = [True] * n
#         is_prime[0] = is_prime[1] = False # 0 and 1 are not prime
        
#         # Loop up to the square root of n
#         for i in range(2, int(n ** 0.5) + 1):
#             if is_prime[i]:
#                 # If i is prime, mark all of its multiples as False
#                 # We can start marking from i*i
#                 for j in range(i * i, n, i):
#                     is_prime[j] = False
                    
#         # Count how many True values remain in our tracker
#         return sum(is_prime)
        

class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        
        # 'primes_mask' is our bitmask. 
        # Bit 0 and Bit 1 are set to 1 because 0 and 1 are not prime.
        # All other bits are initially 0 (assumed prime).
        primes_mask = 3  # Binary: 11
        
        # Loop up to the square root of n
        for i in range(2, int(n ** 0.5) + 1):
            # Check if the i-th bit is 0 (which means 'i' is prime)
            if not (primes_mask & (1 << i)):
                # Mark multiples of i starting from i * i
                for j in range(i * i, n, i):
                    primes_mask |= (1 << j)
                    
        # To count the primes, we count the 0s up to the (n-1)th bit.
        # A quick way is to count how many 1s are set, and subtract from n.
        # .bit_count() is available in Python 3.10+
        return n - primes_mask.bit_count()
    
    
n = 2
c1 = Solution()
print(c1.countPrimes(n))
        
        