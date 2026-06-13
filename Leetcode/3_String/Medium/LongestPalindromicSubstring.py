'''https://leetcode.com/problems/longest-palindromic-substring/description/'''


class Solution:
    def longestPalindrome(self, s: str) -> str:
        # Handle edge cases for empty strings or single characters
        if len(s) <= 1:
            return s
            
        def expand_around_center(left: int, right: int) -> str:
            # Keep expanding outwards as long as the characters match
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            # Return the valid palindromic substring
            # We use left + 1 because the while loop breaks after a mismatch
            return s[left + 1:right]

        longest = ""
        
        ## Main logic works when loops comes in the middle... 
        for i in range(len(s)):
            # Check for odd-length palindromes (e.g., "aba" centered at 'b')
            odd_pal = expand_around_center(i, i)
            
            # Check for even-length palindromes (e.g., "abba" centered between 'b' and 'b')
            even_pal = expand_around_center(i, i + 1)
            
            # Update the longest palindrome found so far
            longest = max(longest, odd_pal, even_pal, key=len)
            
        return longest
    
s = "cbbd"
c1 = Solution()
print(c1.longestPalindrome(s)) 

######################## BRUTEFORCE ##############################
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n <= 1:
            return s
        
        # FIX 1: Default to the first character instead of an empty string
        res = s[0] 
        
        # FIX 2: Default the starting max size to 1 instead of 0
        size_str = 1 
        
        for i in range(n):
            temp = s[i]
            for j in range(i + 1, n):
                temp += s[j]
                
                # Check if the substring reads the same forwards and backwards
                if temp == temp[::-1]:
                    if size_str < len(temp):
                        size_str = len(temp)
                        res = temp
                        
        return res
                
    
# s = "a"
# c1 = Solution()
# print(c1.longestPalindrome(s)) 