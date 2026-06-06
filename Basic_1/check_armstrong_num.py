class Solution:
    def isArmstrong(self, n):
        len_n = len(str(abs(n)))
        result = 0
        copy_n = n

        while copy_n>0:
            rem = copy_n %10
            result = result + rem**len_n
            copy_n = copy_n//10
        return result == n

c1 = Solution()
print(c1.isArmstrong(153))