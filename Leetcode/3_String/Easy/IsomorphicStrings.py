'''https://leetcode.com/problems/isomorphic-strings/description/'''

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dct1 = {}
        dct2 = {}
        for i in s:
            dct1[i] = dct1.get(i, 0)+1

        for i in t:
            dct2[i] = dct2.get(i, 0)+1
        
        # print(dct1, dct2)
    
        return sorted(dct1.values()) == sorted(dct2.values())

        





s = "egg" 
t = "add"
c1 = Solution()
print(c1.isIsomorphic(s,t))