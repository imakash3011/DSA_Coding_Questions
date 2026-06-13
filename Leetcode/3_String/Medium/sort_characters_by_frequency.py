'''https://leetcode.com/problems/sort-characters-by-frequency/'''

from collections import Counter

# class Solution:
#     def frequencySort(self, s: str) -> str:
#         # Step 1: Count the exact frequency of every character
#         # Counter("Aabb") becomes {'b': 2, 'A': 1, 'a': 1}
#         counts = Counter(s)
        
#         # Step 2: Sort the characters by frequency in descending order
#         # .most_common() automatically sorts by the highest count first!
#         result = []
#         for char, freq in counts.most_common():
#             # Multiply the character by its frequency and add to result
#             result.append(char * freq)
            
#         # Step 3: Join and return
#         return "".join(result)



class Solution:
    def frequencySort(self, s: str) -> str:
        result = []
        counter = Counter(s)
        for i, j in counter.most_common():
            result.append(i*j)
        
        return ''.join(result)


c1 = Solution()
s ="Aabb"
print(c1.frequencySort(s))
        