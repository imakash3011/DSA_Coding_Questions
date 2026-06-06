#################### USING Binary SEARCH #################
class Solution:
    def floorSqrt(self, n: int) -> int:
        low = 1
        high = n
        while low<=high:
            mid = (low+high)//2
            if mid*mid == n:
                return mid
            if mid*mid>n:
                high = mid-1
            else:
                low = mid+1
        return high



n = 50
c1 = Solution()
print(c1.floorSqrt(n))

#################### USING LINEAR SEARCH #################
class Solution:
    def floorSqrt(self, n: int) -> int:
        val =1
        for i in range(n):
            if (i*i<=n):
                val = i
            else:
                break
        return val

# n = 28
# c1 = Solution()
# print(c1.floorSqrt(n))

############## USING INBUID FUNCTION ###############
# class Solution:
#     def floorSqrt(self, n: int) -> int:
#         val = int(pow(n, 0.5))
#         return val



# n = 50
# c1 = Solution()
# print(c1.floorSqrt(n))