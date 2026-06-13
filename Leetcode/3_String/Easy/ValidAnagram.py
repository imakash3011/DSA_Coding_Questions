'''https://leetcode.com/problems/valid-anagram/'''


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dct1 = {}
        dct2 = {}
        for i in  s:
            dct1[i] = dct1.get(i, 0)+1
        for j in  t:
            dct2[j] = dct2.get(j, 0)+1
        
        # print(dct1, dct2)
        return dct1 == dct2




s = "anagram" 
t = "nagaram"
c1 = Solution()
print(c1.isAnagram(s,t)) 