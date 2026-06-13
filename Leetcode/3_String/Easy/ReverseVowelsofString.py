'''https://leetcode.com/problems/reverse-vowels-of-a-string/description/?envType=problem-list-v2&envId=string'''

class Solution:
    def reverseVowels(self, s: str) -> str:

        vowels = set("AEIOUaeiou")

        arr = list(s)

        left = 0
        right = len(arr) - 1

        while left < right:

            # Find vowel from left
            while left < right and arr[left] not in vowels:
                left += 1

            # Find vowel from right
            while left < right and arr[right] not in vowels:
                right -= 1

            # Swap vowels
            arr[left], arr[right] = arr[right], arr[left]

            left += 1
            right -= 1

        return "".join(arr)
    
s = "IceCreAm"
c1 = Solution()
print(c1.reverseVowels(s))