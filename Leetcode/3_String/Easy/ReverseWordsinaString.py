'''https://leetcode.com/problems/reverse-words-in-a-string/'''

#################### TOPIMAL APPROACH #########


class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(s.split()[::-1])


s = "the sky is blue"
c1 = Solution()
print(c1.reverseWords(s))



################### BRUTE FORCE #################

class Solution:
    def reverseWords(self, s: str) -> str:
        new_str = ""
        s_lst = s.split(" ")
        print(s_lst)

        for word in s_lst[::-1]:
            new_str = str.strip(new_str) +" "+ word

        return new_str.strip(" ")




# s = "the sky is blue"
# c1 = Solution()
# print(c1.reverseWords(s))