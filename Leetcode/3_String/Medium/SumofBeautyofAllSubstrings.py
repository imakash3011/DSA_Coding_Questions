'''https://leetcode.com/problems/sum-of-beauty-of-all-substrings/description/'''


class Solution:
    def beautySum(self, s: str) -> int:
        total_beauty = 0
        n = len(s)
        
        # Iterate over each possible starting character of a substring
        for i in range(n):
            # Dictionary to keep track of character frequencies in the current window
            freq = {}
            
            # Expand the substring by moving the end pointer
            for j in range(i, n):
                char = s[j]
                freq[char] = freq.get(char, 0) + 1
                
                # Get all the frequencies of characters currently in the substring
                freq_values = freq.values()
                print(freq_values)
                
                # Beauty is the difference between highest and lowest frequencies
                total_beauty += max(freq_values) - min(freq_values)
                
        return total_beauty


s = "aabcb"
c1 = Solution()
print(c1.beautySum(s))