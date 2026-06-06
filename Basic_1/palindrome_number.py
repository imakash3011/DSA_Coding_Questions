class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        new_num = int(str(x)[::-1])
        if new_num == x:
            return True
        return False
    

c1 = Solution()
print(c1.isPalindrome(121))