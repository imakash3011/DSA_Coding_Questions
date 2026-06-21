'''https://leetcode.com/problems/letter-combinations-of-a-phone-number/'''


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        # Map phone digits to corresponding letters
        phone_map = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }
        
        result = []

        def helper_func(idx, current_combination):

            if idx==len(digits):
                result.append(current_combination)
                return
            
            current_digit = digits[idx]
            possible_letter = phone_map[current_digit]

            for letter in possible_letter:
                helper_func(idx +1 , current_combination+letter)
        
        helper_func(0, "")
        return result

# digits = "23"
# c1 = Solution()
# print(c1.letterCombinations(digits))
        

################### ANOTHER APPROACH ###################

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        # Map phone digits to corresponding letters
        phone_map = {
            "2": "abc", "3": "def", "4": "ghi", "5": "jkl",
            "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"
        }
        
        result = []

        def helper_func(idx, subset):

            if idx==len(digits):
                result.append(''.join(subset))
                return

            for ch in phone_map[digits[idx]]:
                subset.append(ch)
                helper_func(idx +1 , subset)
                subset.pop()
        
        helper_func(0, [])
        return result

digits = "23"
c1 = Solution()
print(c1.letterCombinations(digits))
        