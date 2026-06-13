'''https://leetcode.com/problems/count-good-numbers/description/'''

class Solution:
    MOD = 10**9 + 7

    def power(self, base, exp):
        if exp==0:
            return 1
            
        half = self.power(base, exp//2)
        half = (half * half)% self.MOD

        if exp%2==0:
            return half
        return (base*half)%self.MOD

    def countGoodNumbers(self, n: int) -> int:        
        even_pos = (n+1)//2
        odd_pos = n//2

        result = self.power(5, even_pos)* self.power(4, odd_pos)%self.MOD

        return result
n = 1
c1 = Solution()
print(c1.countGoodNumbers(n))

############## NOT OPTIMAL ###############
class Solution:
    MOD = 10**9 + 7

    def power(self, base, exp):
            result = 1
            for i in range(exp):
                result = (result*base)% self.MOD
            return result

    def countGoodNumbers(self, n: int) -> int:        
        even_pos = (n+1)//2
        odd_pos = n//2

        result = self.power(5, even_pos)* self.power(4, odd_pos)%self.MOD

        return result

# n = 50
# c1 = Solution()
# print(c1.countGoodNumbers(n))




# class Solution:
#     def countGoodNumbers(self, n: int) -> int:
#         MOD = 10**9 + 7
#         even_pos = (n+1)//2
#         odd_pos = n//2

#         result = (5**even_pos)*(4**odd_pos)
#         return result%MOD
        