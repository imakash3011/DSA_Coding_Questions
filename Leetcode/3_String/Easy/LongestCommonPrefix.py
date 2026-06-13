'''https://leetcode.com/problems/longest-common-prefix/'''


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_len = float('inf')
        val = ""
        for num in strs:
            if len(num)<min_len:
                min_len = len(num)
                val = num
        
        result= ""
        for i in range(len(val)):
            # print(num[i], i)
            for j in strs:
                # print(num[i], i, j)
                if num[i]!=j[i]:
                    return result
            result+=num[i]

        return result




strs = ["dog","racecar","car"]
c1 = Solution()
print(c1.longestCommonPrefix(strs))
