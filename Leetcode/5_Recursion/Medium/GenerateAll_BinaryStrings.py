'''https://leetcode.com/problems/generate-binary-strings-without-adjacent-zeros/'''


class Solution:
    def validStrings(self, n: int) -> List[str]:
        result = []
        def helper_func(binary_str):
            if len(binary_str ) == n:
                result.append(binary_str)
                return
            
            helper_func(binary_str+"1")

            if not binary_str or binary_str[-1] !="0":
                helper_func(binary_str+"0")
        
        helper_func("")
        return result


n = 3
c1 = Solution()
print(c1.validStrings(n))
        




# class Solution:
#     def validStrings(self, n: int) -> List[str]:
#         result = []
#         max_val = (2**n) - 1
        
#         # Loop through every number from 0 to 2^n - 1
#         for idx in range(max_val + 1):
#             # 1. Convert to binary and pad with leading zeros to make it length 'n'
#             # '03b' for n=3 makes 1 into '001'
#             binary_str = f'{idx:0{n}b}' 
            
#             # 2. Check if '00' is in the string. 
#             # If '00' is NOT found, it means there are no adjacent zeros!
#             if "00" not in binary_str:
#                 result.append(binary_str)
                
#         return result

# # Test case
# n = 3
# c1 = Solution()
# print(c1.validStrings(n))
# # Output: ['010', '011', '101', '110', '111']